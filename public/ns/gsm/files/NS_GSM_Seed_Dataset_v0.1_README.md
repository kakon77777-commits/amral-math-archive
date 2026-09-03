# NS_GSM Seed Dataset v0.1

Canonical code: `NS_GSM`

This package is the first executable seed dataset for Closure-Space Mathematics applied to the long-horizon Navier–Stokes research corpus.

## Scope

`observed-relative`

It does **not** claim:
- route completeness;
- representation completeness;
- absolute proof-space coverage;
- Navier–Stokes global regularity;
- physical Navier–Stokes validation;
- generalized NS-like family closure.

## Seed design

There are **7 logical seed units built from 5 physical source artifacts**.

C1 and C2 are canonical proof-obligation targets extracted from the ETN–X foundational source. They are not fabricated as independent source documents.

## Files

- `dataset.yaml`
- `domains.yaml`
- `series.yaml`
- `artifacts.yaml`
- `claims.yaml`
- `routes.yaml`
- `obstructions.yaml`
- `survivors.yaml`
- `frontiers.yaml`
- `bridges.yaml`
- `debts.yaml`
- `certificates.yaml`
- `nonclaims.yaml`
- `graph_snapshot_v0.1.json`
- `source_manifest_v0.1.json`
- `seed_assertions_v0.1.json`
- `validation_report_v0.1.json`

## Key runtime expectations

1. Artifact labels never directly mutate root theorem status.
2. `NO-GO` is represented as an obstruction object.
3. `STOP` is represented as a frontier object.
4. `SURVIVOR` is an OPEN route-role, not a proof.
5. D104's narrow positive-viscosity no-go remains valid in its declared scope, while D105 blocks silent uniform promotion to vanishing viscosity.
6. Root formal NS target remains OPEN.
