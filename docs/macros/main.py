"""Expose CCN date variables to Markdown as Jinja macros.

Each year's dates live in a per-year template at
``docs/<year>/assets/dates.yml``. This module loads every such template and
registers its entries so pages can reference them as ``{{ <name> }}``.
"""

from __future__ import annotations

from pathlib import Path

import yaml

_DOCS_DIR = Path(__file__).resolve().parent.parent


def define_env(env) -> None:
    """Register every year's date variables from its assets template."""
    for dates_file in sorted(_DOCS_DIR.glob("*/assets/dates.yml")):
        data = yaml.safe_load(dates_file.read_text(encoding="utf-8")) or {}
        env.variables.update(data)
