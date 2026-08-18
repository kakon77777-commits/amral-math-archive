# amral

Dedicated repo for AMRAL (amral.evemisslab.com) — separated out from the `unbounded-axiom`
monorepo on 2026-08-18 as AMRAL outgrew sharing a repo with logic-matrix. Local working
copy: `D:\Ai\work together\amral\`.

## Layout

- **`public/`** — the deployed site. Assets-only Cloudflare Worker, config in
  `wrangler.jsonc`. Deploy with `npx wrangler deploy` from this repo's root.
- **`_ziputil.py`, `build_manifest*.py`, `extract_package_files*.py`** — build tooling
  used when turning a raw research drop into detail pages under `public/`.
- **`drops/`** — where Neo hands over new raw material. Since this repo is checked out
  locally, he puts files here directly instead of uploading anywhere first. One
  top-level folder per project or line, named however makes sense at the time (e.g.
  `NS/`, `CCM-followups/`). No fixed structure imposed in advance.

## Related repos

- [amral-research-trees](https://github.com/kakon77777-commits/amral-research-trees) —
  mirror of raw research source `.md` behind each curated page on the live site, for
  AI/agent consumption (has its own [remote MCP server](https://github.com/kakon77777-commits/amral-research-trees-mcp)).
  Distinct from `drops/` above: that repo holds *processed* output mirrored after
  building; `drops/` here is *upstream* of that, raw material before anything's been
  read or built.
- [amral-archive-api](https://github.com/kakon77777-commits/amral-archive-api) — a
  FastAPI ingestion service for AI agents that can't handle zips/filesystems directly.

## History

Originally created 2026-08-18 as a narrower GitHub-based raw-drop intake point (see the
`drops/` folder for what that was). Repurposed the same day into the full dedicated
AMRAL repo once Neo pointed out the obvious: since work happens via a local coding
agent, there's no reason to route local-to-local handoffs through GitHub at all — a
local folder does that job directly, and this repo's job narrowed to "the actual site's
source of truth," with `drops/` kept as the one place inside it still meant for raw,
unprocessed material.

The site's old location, `D:\Ai\work together\unbounded-axiom\amral\`, is untouched and
still what's live-deployed as of this repo's creation — see that repo's own notes for
when/whether deploys cut over to here.
