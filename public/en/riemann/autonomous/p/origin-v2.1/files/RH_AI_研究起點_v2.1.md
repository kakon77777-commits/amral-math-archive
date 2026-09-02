# RH AI Research Starting Point v2.1: Unified Certificate Backend

This release integrates RH-W-18. Major additions include:

- A common manifest for W-04 to W-17;
- Single `rhcert.py` verification entry point;
- Native verifier adapter;
- Artifact SHA-256 identity;
- Claim firewall;
- Legacy incomplete and superseded states;
- Three-layer adversarial red-team.

To run:

```bash
cd RH_W_18_Engineering_Package_v0.1
python rhcert.py verify
python redteam_backend.py
```

This release does not prove or disprove the Riemann Hypothesis.