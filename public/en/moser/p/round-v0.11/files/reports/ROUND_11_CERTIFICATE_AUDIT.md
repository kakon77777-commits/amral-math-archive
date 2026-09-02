# Round 11 Special Branch and Interval Box Audit

## $270^\circ$ Envelope

```text
[0.9989143390757518, 0.9989143390935133]
```

## $120^\circ-270^\circ$ Envelope

```text
[1.6349560074843125e-09, 1.6417123458293262e-09]
```

## Smooth Candidate Minus Event Control

```text
['0.000010581943243125044870175099443519782731773287807896210561320048743665520857071074', '0.000010581961004625044870175099443519782731773287807896210561320048743665520857071074']
```

## Derivative Boxes

- Number of intervals: 18
- Adaptive subboxes: 579
- Unresolved subboxes: 0

## Root Boxes

- Smooth stationary points: 12
- All second derivative boxes exclude zero: True

## Boundaries

- Internal boundaries: 17
- Signs of derivatives on both sides directly determined: 16
- All boundaries are verified via derivative classification, scaled neighborhood lower bounds, or special branch certificates.

## Limitations

Full directed-rounding was not used in this round. The analytical error bounds of `special_branch_verify.py` can be recalculated independently, but the complete derivative boxes should still be re-verified by Arb/MPFI.