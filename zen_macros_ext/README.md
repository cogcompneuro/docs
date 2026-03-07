## zen-macros-ext

> **Workaround** — This extension is a temporary workaround until Zensical supports
> native template variables.
> Track progress at <https://github.com/zensical/backlog/issues/16>. Once that issue is
> closed, move the variables from `docs/macros/main.py` into `zensical.toml` (or
> whatever mechanism Zensical provides) and remove this package.

`zen-macros-ext` is a small Markdown extension that lets projects keep their existing
[mkdocs-macros-plugin](https://mkdocs-macros-plugin.readthedocs.io/) content when
migrating from MkDocs to [Zensical](https://zensical.org).
Instead of re-writing every `{{ macro() }}` usage, this extension renders Markdown
through a Jinja runtime **before** the standard Markdown pipeline is invoked, meaning
all legacy macros continue to work without touching the original pages.

### Key Features

- Loads any `docs/macros/main.py` module that exposes the usual `define_env(env)`
  entrypoint.
- Mimics the `env.macro` decorator to register macros and exposes them as Jinja globals.
- Wraps fenced code blocks with `{% raw %}` / `{% endraw %}` so documentation pages can
  still show literal `{{ ... }}` samples without Jinja trying to evaluate them.
- Stays compatible with the MkDocs toolchain—projects can keep running mkdocs-macros for
  the classic workflow while Zensical loads this extension.

### Installation

The package is currently distributed as a local editable dependency.
From the repository root:

```bash
source .venv/bin/activate
pip install -e packages/zen_macros_ext
```

You can copy `packages/zen_macros_ext/` into any other project or publish it to PyPI.
The extension has only two runtime dependencies: `markdown` and `jinja2`.

### Configuration (Zensical)

Add the extension to `zensical.toml` (or `mkdocs.yml`) under
`project.markdown_extensions`. Example for Zensical:

```toml
[project.markdown_extensions."zen_macros_ext:MacroExtension"]
project_dir = "."
docs_dir = "docs"
macros_file = "docs/macros/main.py"
```

Settings:

| key | default | description |
| --- | --- | --- |
| `project_dir` | `"."` | Root directory used to resolve the macros module. |
| `docs_dir` | `"docs"` | Documentation directory (mirrors MkDocs/Zensical setting). |
| `macros_file` | `"docs/macros/main.py"` | Path to the legacy macros entry point. |

### How It Works

1. The extension loads `macros_file` via `importlib`.
2. It instantiates a lightweight environment object that exposes the same API
   (`env.project_dir`, `env.conf`, `@env.macro`) that mkdocs-macros expects.
3. After `define_env(env)` registers all macros, they are injected as globals into a
   Jinja `Environment`.
4. A Markdown preprocessor runs before any other extension, rendering the page through
   Jinja and returning the resulting Markdown to the regular pipeline.

Any macro that returned Markdown (like cards, quizzes, objectifs lists, etc.)
continues to render exactly as it did under the MkDocs toolchain.

### Sharing With Zensical

If you want to share this extension with the Zensical team or other users, simply zip
the `packages/zen_macros_ext/` directory or publish it on PyPI. Once installed, the only
additional step for adopters is to reference the extension in their configuration (see
above). No template overrides or content changes are required.
