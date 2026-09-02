# Round 10 Global Phase Certificate Interface

## Generated Machine-Readable Ledgers

- `data/phase_contact_intervals.csv`
- `data/round10_summary.json`
- `data/round10_global_exclusion_audit.json`

## Each Interval Contains

$$
(
I_k,
\Sigma_k,
\min s'(I_k),
\max s'(I_k),
\{\phi:s'(\phi)=0\},
\min_{I_k}s
).
$$

## Next Level of Rigor

1. Enclose each contact transition using interval arithmetic;
2. Replace PCHIP coordinates with arbitrary-precision integrals or provable integral envelopes;
3. Establish $s'(\phi)$ intervals for fixed signature formulas;
4. Apply the interval Newton method to smooth stationary points;
5. Construct dedicated difference envelopes for $120^\circ$ and $270^\circ$.

## Final Goal

Generate a machine-readable certificate:

$$
\forall \phi\in[0,2\pi),
\qquad
s(\phi)\ge s(3\pi/2).
$$

This round does not yet claim to have completed this rigorous certificate.