# -*- coding: utf-8 -*-
"""
Site-wide nav refresh, both languages, from the single canonical template
in amral_nav.py. Coverage comes from walking the filesystem directly (site
root down), never from any generator's own manifest of what it built --
that was the exact design flaw caught before this script was written (a
manifest-derived coverage count cannot see a page no generator knows
about, which is precisely how the 244-page ZH gap and the EN homepage's
stale nav went unnoticed).

Run this after adding a new entry to CASES in amral_nav.py -- it is the
entire process for propagating a new case into every page's nav.

Default mode is dry-run: writes a report to nav_refresh_report.txt and
changes nothing. Pass --apply to actually write.

    python refresh_all_nav.py            # dry run, review the report first
    python refresh_all_nav.py --apply    # write

newline="" is used on both read and write so a page whose nav doesn't
change is byte-identical afterward, regardless of that file's own
line-ending convention.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import amral_nav as N

nav_re = re.compile(r'<nav class="sitenav">.*?</nav>', re.DOTALL)

APPLY = "--apply" in sys.argv


def walk_lang(lang, root):
    pages = []
    for dirpath, dirnames, filenames in os.walk(root):
        if lang == "zh" and dirpath == root:
            dirnames[:] = [d for d in dirnames if d != "en"]  # en/ is a separate root, walked on its own pass
        if lang == "en" and os.path.basename(dirpath) in N.EN_EXCLUDED_OWN_SECTIONS:
            dirnames[:] = []  # don't descend into excluded sections either
            continue
        if "index.html" in filenames:
            pages.append(os.path.join(dirpath, "index.html"))
    return pages


def diff_signature(old_nav, new_nav):
    old_items = re.findall(r'>([^<]+)</a>', old_nav)
    new_items = re.findall(r'>([^<]+)</a>', new_nav)
    added = [x for x in new_items if x not in old_items]
    removed = [x for x in old_items if x not in new_items]
    reordered = (old_items == new_items) is False and not added and not removed
    parts = []
    if added:
        parts.append("+" + ",".join(added))
    if removed:
        parts.append("-" + ",".join(removed))
    if reordered:
        parts.append("reordered-only")
    return " ".join(parts) if parts else "(no visible label change)"


def main():
    out = []
    changes = {}  # signature -> count
    examples = {}
    to_write = []
    skipped_out_of_scope = 0
    no_nav_found = 0
    unchanged = 0

    for lang, root in [("zh", N.ZH_ROOT), ("en", N.EN_ROOT)]:
        for path in walk_lang(lang, root):
            with open(path, encoding="utf-8", newline="") as f:
                content = f.read()
            page_dir = os.path.dirname(path)
            new_nav = N.render_nav(lang, page_dir)
            if new_nav is None:
                skipped_out_of_scope += 1
                continue
            m = nav_re.search(content)
            if not m:
                no_nav_found += 1
                out.append(f"NO NAV: [{lang}] {os.path.relpath(path, root)}")
                continue
            old_nav = m.group(0)
            if old_nav == new_nav:
                unchanged += 1
                continue
            sig = f"[{lang}] " + diff_signature(old_nav, new_nav)
            changes[sig] = changes.get(sig, 0) + 1
            examples.setdefault(sig, os.path.relpath(path, root))
            to_write.append((path, content, old_nav, new_nav))

    out.append(f"Unchanged (already canonical): {unchanged}")
    out.append(f"Out of scope (excluded sections): {skipped_out_of_scope}")
    out.append(f"No nav block found: {no_nav_found}")
    out.append(f"Pages that WOULD change: {len(to_write)}")
    out.append("")
    for sig, count in sorted(changes.items(), key=lambda x: -x[1]):
        out.append(f"{count:4d} pages -- {sig}  (example: {examples[sig]})")

    result_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "nav_refresh_report.txt")
    with open(result_path, "w", encoding="utf-8") as f:
        f.write("\n".join(out))
    print(f"Report written to {result_path}")

    if not APPLY:
        print("Dry run only. Re-run with --apply to write changes.")
        return

    print(f"Applying {len(to_write)} changes...")
    written = 0
    for path, content, old_nav, new_nav in to_write:
        new_content = content.replace(old_nav, new_nav, 1)
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write(new_content)
        written += 1
    print(f"Wrote {written} files.")


if __name__ == "__main__":
    main()
