"""Date variables exposed as Jinja macros via zen_macros_ext.

This is a workaround until Zensical supports native template variables:
https://github.com/zensical/backlog/issues/16

Once that issue is closed, these variables should be moved to zensical.toml
(under [project.extra] or a dedicated variables section) and this file and the
zen_macros_ext package can be removed.
"""

from __future__ import annotations


def define_env(env):
    """Register date variables for use in Markdown as {{ var_name }}."""

    # ── 2025 Proceedings ──────────────────────────────────────────────
    env.variables["abstract_deadline_2025"] = "Feb 17, 2025"
    env.variables["abstract_deadline_plus_one_2025"] = "Feb 18, 2025"
    env.variables["submission_deadline_2025"] = "Feb 20, 2025"
    env.variables["review_period_2025"] = "Mar 4 - Mar 31, 2025"
    env.variables["reviews_due_2025"] = "Mar 31, 2025"
    env.variables["reviews_released_2025"] = "Apr 3, 2025"
    env.variables["author_response_period_2025"] = "Apr 3 - Apr 14, 2025"
    env.variables["author_response_due_2025"] = "Apr 14, 2025"
    env.variables["discussion_period_2025"] = "Apr 15 - Apr 21, 2025"
    env.variables["poster_acceptances_2025"] = "Apr 18, 2025"
    env.variables["meta_review_period_2025"] = "Apr 22 - May 5, 2025"
    env.variables["meta_review_due_2025"] = "May 5, 2025"
    env.variables["final_decisions_period_2025"] = "May 6 - May 12, 2025"
    env.variables["proceedings_decisions_2025"] = "May 13, 2025"
    env.variables["presenter_selection_period_2025"] = "May 14 - Jun 12, 2025"
    env.variables["talk_selections_2025"] = "Jun 13, 2025"

    # ── 2025 Extended Abstracts ───────────────────────────────────────
    env.variables["ea_submission_deadline_2025"] = "Apr 10, 2025"
    env.variables["ea_desk_rejection_period_2025"] = "Apr 11 - Apr 14, 2025"
    env.variables["ea_review_period_2025"] = "Apr 18 - May 18, 2025"
    env.variables["ea_reviews_due_2025"] = "May 18, 2025"

    # ── 2026 Proceedings ──────────────────────────────────────────────
    env.variables["abstract_deadline_2026"] = "Feb 9, 2026"
    env.variables["abstract_deadline_plus_one_2026"] = "Feb 10, 2026"
    env.variables["submission_deadline_2026"] = "Feb 12, 2026"
    env.variables["enrollment_period_2026"] = "Feb 10 - Feb 12, 2026"
    env.variables["assignment_period_2026"] = "Feb 13 - Feb 16, 2026"
    env.variables["adjustment_period_2026"] = "Feb 17 - Feb 23, 2026"
    env.variables["review_period_2026"] = "Feb 24 - Mar 23, 2026"
    env.variables["reviews_due_2026"] = "Mar 23, 2026"
    env.variables["emergency_review_period_2026"] = "Mar 24 - Mar 25, 2026"
    env.variables["reviews_released_2026"] = "Mar 26, 2026"
    env.variables["author_response_period_2026"] = "Mar 26 - Apr 6, 2026"
    env.variables["author_response_due_2026"] = "Apr 6, 2026"
    env.variables["discussion_period_2026"] = "Apr 7 - Apr 13, 2026"
    env.variables["discussion_due_2026"] = "Apr 13, 2026"
    env.variables["poster_acceptances_2026"] = "Apr 20, 2026"
    env.variables["meta_review_period_2026"] = "Apr 14 - Apr 27, 2026"
    env.variables["meta_review_due_2026"] = "Apr 27, 2026"
    env.variables["final_decisions_period_2026"] = "Apr 28 - May 11, 2026"
    env.variables["proceedings_decisions_2026"] = "May 12, 2026"
    env.variables["presenter_selection_period_2026"] = "May 13 - Jun 11, 2026"
    env.variables["talk_selections_2026"] = "Jun 12, 2026"

    # ── 2026 Extended Abstracts ───────────────────────────────────────
    env.variables["ea_submission_deadline_2026"] = "Apr 2, 2026"
    env.variables["ea_desk_rejection_period_2026"] = "Apr 3 - Apr 12, 2026"
    env.variables["ea_review_period_2026"] = "Apr 13 - May 18, 2026"
    env.variables["ea_reviews_due_2026"] = "May 18, 2026"
