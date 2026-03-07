from __future__ import annotations

import importlib.util
import re
from pathlib import Path
from typing import Any, Callable, Dict, List

from jinja2 import Environment
from markdown.extensions import Extension
from markdown.preprocessors import Preprocessor


class _MacroEnv:
    """Minimal stand-in for the mkdocs-macros `env` helper."""

    def __init__(self, project_dir: Path, docs_dir: str):
        self.project_dir = str(project_dir)
        self.conf = {"docs_dir": docs_dir}
        self._macros: Dict[str, Callable[..., Any]] = {}
        self.variables: Dict[str, Any] = {}

    def macro(self, func: Callable[..., Any]) -> Callable[..., Any]:
        self._macros[func.__name__] = func
        return func

    @property
    def macros(self) -> Dict[str, Callable[..., Any]]:
        return self._macros


def _load_macro_module(project_dir: Path, docs_dir: str, module_path: Path) -> Dict[str, Callable[..., Any]]:
    env = _MacroEnv(project_dir, docs_dir)
    spec = importlib.util.spec_from_file_location("site_macros", module_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot import macros module from {module_path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)  # type: ignore[attr-defined]
    if hasattr(module, "define_env"):
        module.define_env(env)
    return {**env.variables, **env.macros}


class _MacroPreprocessor(Preprocessor):
    """Render Markdown through Jinja so legacy macros keep working."""

    FENCE_RE = re.compile(r"^(\s*)(`{3,}|~{3,})(.*)$")

    def __init__(self, macros: Dict[str, Callable[..., Any]]):
        super().__init__()
        self._jinja = Environment(
            autoescape=False,
            trim_blocks=False,
            lstrip_blocks=False,
            keep_trailing_newline=True,
        )
        self._jinja.globals.update(macros)

    def run(self, lines: List[str]) -> List[str]:
        protected = self._wrap_code_fences(lines)
        template = self._jinja.from_string("\n".join(protected))
        rendered = template.render()
        return rendered.splitlines()

    def _wrap_code_fences(self, lines: List[str]) -> List[str]:
        """Inject {% raw %} ... {% endraw %} around fenced code blocks."""
        result: List[str] = []
        in_fence = False
        fence_marker = ""

        for line in lines:
            match = self.FENCE_RE.match(line)
            if not in_fence and match:
                in_fence = True
                fence_marker = match.group(2)
                result.append("{% raw %}")
                result.append(line)
                continue

            if in_fence:
                result.append(line)
                if match and match.group(2) == fence_marker and match.group(3).strip() == "":
                    in_fence = False
                    fence_marker = ""
                    result.append("{% endraw %}")
                continue

            result.append(line)

        if in_fence:
            result.append("{% endraw %}")

        return result


class MacroExtension(Extension):
    """Markdown extension exposed to Zensical."""

    def __init__(self, **kwargs: Any):
        self.config = {
            "project_dir": [".", "Project root path"],
            "docs_dir": ["docs", "Documentation directory"],
            "macros_file": ["docs/macros/main.py", "Path to macros entry point"],
        }
        super().__init__(**kwargs)

    def extendMarkdown(self, md):
        project_dir = Path(self.getConfig("project_dir")).resolve()
        docs_dir = self.getConfig("docs_dir")
        macros_file = Path(self.getConfig("macros_file"))
        if not macros_file.is_absolute():
            macros_file = (project_dir / macros_file).resolve()

        macros = _load_macro_module(project_dir, docs_dir, macros_file)
        md.preprocessors.register(_MacroPreprocessor(macros), "zensical_macros", 25)
