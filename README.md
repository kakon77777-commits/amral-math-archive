# amral-math-archive

A direct handoff point for raw mathematical research material — Neo drops packages
here, Claude reads them directly from this repo instead of a local `Downloads\<name>\`
folder.

## Why this exists

Every AMRAL program line so far (BSD, CPL, RH, Moser, skew-field, P/NP, GLC, CCM) started
as raw zip packages sitting in a local folder that had to exist on the machine running
the session. This repo replaces that step for material Neo wants to hand over cleanly,
without needing to have it locally organized first. It's separate from
[amral-research-trees](https://github.com/kakon77777-commits/amral-research-trees),
which holds the *processed* output — the raw material AI research work gets mirrored
into after it's been built into the curated site at amral.evemisslab.com. This repo is
upstream of that: raw drops, before anything has been read or built.

## Convention

One top-level folder per project or line, named however makes sense at the time
(e.g. `NS/`, `CCM-followups/`). No fixed structure is imposed in advance — whatever
Neo drops in (zips, loose `.md` files, whatever the source naturally is) gets read
as-is, same as the local-folder workflow it replaces.

## Status

Just created 2026-08-18. Empty until the first drop.
