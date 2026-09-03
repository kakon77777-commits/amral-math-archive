# -*- coding: utf-8 -*-
"""
Single source of truth for AMRAL's site nav, both languages.

Before this existed, every page carried its own literal copy of the nav
block, written by whichever one-off generator script built that page.
611 ZH pages alone had drifted into 4 different item sets by 2026-09-03
(see identities/witness/memory/project-amral-collatz-integration.md),
and existence-checkers never caught it, because a missing nav LINK is not
a broken one -- there was no file anywhere declaring which items a page's
nav should have, so nothing could be compared against.

To add a new case when a section ships: append one entry to CASES below,
then run `python refresh_all_nav.py --apply` from this directory. That is
the entire process -- do not hand-edit any page's nav block directly, and
do not write a new one-off generator that embeds its own nav template;
both are exactly how the drift happened the first time.

Case order matches the template already in production use on every
Collatz page (the freshest, most-recently-verified template on the site
as of 2026-09-03) -- not an invented order.

PRE_ITEMS_ZH and PRE_ITEMS_EN must name the same slugs, in the same order
-- one case list, labels translated, per line. An earlier version of this
module excluded research-modes/data-access from PRE_ITEMS_EN on the belief
that EN deliberately omitted them; 墜衡 (independent live verification,
2026-09-03) found both pages fully built and translated, orphaned from
EN nav entirely as a result -- unreachable from any other EN page, and
themselves stuck on a stale template no refresh run could fix, since the
exclusion lived in this file, not in coverage. Two per-language lists that
can independently drift is the exact failure this module exists to end;
keep them in lockstep.
"""
import os

TOOLS_DIR = os.path.dirname(os.path.abspath(__file__))
PUBLIC = os.path.normpath(os.path.join(TOOLS_DIR, "..", "..", "public"))
ZH_ROOT = PUBLIC
EN_ROOT = os.path.join(PUBLIC, "en")

# (slug, label)
PRE_ITEMS_ZH = [
    ("about", "關於"),
    ("methodology", "方法論"),
    ("protocols", "研究協議"),
    ("validation", "驗證"),
    ("research-modes", "自主模式"),
    ("data-access", "資料存取"),
]
PRE_ITEMS_EN = [
    ("about", "About"),
    ("methodology", "Methodology"),
    ("protocols", "Protocols"),
    ("validation", "Validation"),
    ("research-modes", "Research Modes"),
    ("data-access", "Data Access"),
]

# Canonical case order -- append new cases here, in ship order.
CASES = [
    ("riemann", "黎曼猜想", "Riemann Hypothesis"),
    ("moser", "Moser 蟲問題", "Moser's Worm Problem"),
    ("skew-field", "歪度場", "Skew Field"),
    ("p-np-dual", "P/NP 對偶預演", "P/NP Dual Rehearsal"),
    ("glc-framework", "GLC 閉合框架", "GLC Closure Framework"),
    ("bsd", "BSD 猜想", "BSD Conjecture"),
    ("cpl", "臨界線比例梯", "Critical-Line Proportion Ladder"),
    ("ccm", "CCM 計算複合方法論", "CCM Computational Composite Methodology"),
    ("ns", "NS 納維-斯托克斯", "Navier–Stokes"),
    ("collatz", "考拉茲猜想", "Collatz Conjecture"),
]
CASE_SLUGS = {slug for slug, _, _ in CASES}


def relpath_slash(target_dir, from_dir):
    r = os.path.relpath(target_dir, from_dir).replace("\\", "/")
    return r + "/" if r != "." else "./"


def active_section(page_dir, lang_root):
    """First path segment under the language root, or None at site root."""
    rel = os.path.relpath(page_dir, lang_root).replace("\\", "/")
    if rel == ".":
        return None
    return rel.split("/")[0]


def in_scope(lang, active):
    if active is None:
        return True  # site root
    pre_slugs = {s for s, _ in (PRE_ITEMS_ZH if lang == "zh" else PRE_ITEMS_EN)}
    return active in CASE_SLUGS or active in pre_slugs


def render_nav(lang, page_dir):
    """Build the canonical <nav>...</nav> block for a ZH or EN page at
    page_dir. Returns None if this page is out of the canonical vocabulary
    (site utility pages not in PRE_ITEMS/CASES) -- caller should leave such
    pages untouched."""
    lang_root = ZH_ROOT if lang == "zh" else EN_ROOT
    other_root = EN_ROOT if lang == "zh" else ZH_ROOT
    active = active_section(page_dir, lang_root)
    if not in_scope(lang, active):
        return None

    ups = relpath_slash(lang_root, page_dir)
    pre_items = PRE_ITEMS_ZH if lang == "zh" else PRE_ITEMS_EN

    lines = ['<nav class="sitenav"><div class="inner">']
    brand_href = "./" if active is None else ups
    lines.append(f'  <a class="brand" href="{brand_href}">AMRAL</a>')

    def item(slug, label):
        if slug == active:
            href = relpath_slash(os.path.join(lang_root, slug), page_dir)
            lines.append(f'  <a class="link active" href="{href}">{label}</a>')
        else:
            lines.append(f'  <a class="link" href="{ups}{slug}/">{label}</a>')

    for slug, label in pre_items:
        item(slug, label)
    for slug, zh_label, en_label in CASES:
        item(slug, zh_label if lang == "zh" else en_label)

    # lang-switch: mirror path in the OTHER language tree
    rel_from_root = os.path.relpath(page_dir, lang_root).replace("\\", "/")
    other_dir = other_root if rel_from_root == "." else os.path.join(other_root, rel_from_root)
    ups_to_other = relpath_slash(other_dir, page_dir)
    if lang == "zh":
        lines.append(f'  <a class="lang-switch" href="{ups_to_other}" hreflang="en">EN</a>')
    else:
        lines.append(f'  <a class="lang-switch" href="{ups_to_other}" hreflang="zh-Hant">中文</a>')

    lines.append('</div></nav>')
    return "\n".join(lines)
