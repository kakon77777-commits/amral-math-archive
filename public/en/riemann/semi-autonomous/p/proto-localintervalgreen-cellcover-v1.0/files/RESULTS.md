# Results

## Main Certificate

The maximum passed test radius is

$$
h_*=\frac{89}{50\,000\,000}
=1.78\times10^{-6}.
$$

On the maximal Cartesian product box where all $58$ positions can vary independently:

| Quantity | Strict Bound |
|---|---:|
| Neumann defect $\|I-RA\|_\infty$ | $\le 0.02755725053402449$ |
| First principal minor $T_{11}$ | $\ge 0.33057431704010146$ |
| $\det T$ | $\ge 0.0000669375118837732$ |
| Maximum projected Gram term width | $\le 0.004529609514787403$ |

The four conditions are respectively satisfied:

$$
0.02755725053402449<1,
\qquad
0.33057431704010146>0,
$$

$$
0.0000669375118837732>0.
$$

Therefore, the abstract operator family within the maximal box is strictly positive.

## Radius Steps

| Uniform radius $h$ | Result | Failure type | Neumann defect upper bound | Determinant lower bound |
|---:|---|---|---:|---:|
| $0$ | Pass | — | $6.86\times10^{-15}$ | $0.1129495436$ |
| $10^{-8}$ | Pass | — | $1.5482\times10^{-4}$ | $0.1123297712$ |
| $10^{-6}$ | Pass | — | $0.0154815855$ | $0.0501779260$ |
| $1.78\times10^{-6}$ | Pass | — | $0.0275572505$ | $6.69375\times10^{-5}$ |
| $1.8\times10^{-6}$ | Inconclusive | Sylvester lower bound failure | $0.0278668833$ | $-0.0012315226$ |
| $10^{-4}$ | Inconclusive | Neumann inverse failure | $1.5483670681$ | Not reached |
| $10^{-3}$ | Inconclusive | Neumann inverse failure | $15.5091628504$ | Not reached |

This table only provides the pass/inconclusive bracket of the current interval prover:

$$
1.78\times10^{-6}
\le h_{\mathrm{cert}},
\qquad
h=1.8\times10^{-6}
\text{ is not certified by this method}.
$$

It does not imply that the true positivity threshold lies between the two.

## Improvement over v0.9

The operator norm budget of v0.9 only certified

$$
h_{0.9}=2\times10^{-15}.
$$

Thus, the exact improvement factor for the radius is

$$
\frac{h_*}{h_{0.9}}
=890\,000\,000.
$$

This improvement comes from directly retaining the Green pairing, structural projection, and low negative-rank Schur geometry, rather than compressing all positional perturbations into a single worst-case operator norm beforehand.

## Covering Certificate Family

The maximal certificate consists of only a single $58$-dimensional leaf box, but it simultaneously covers all independent position choices. Any closed rational sub-box coordinate-wise contained in this leaf box inherits the certificate, thus yielding a downward-closed family that requires no leaf-by-leaf recomputation.

## Corner Counter-Diagnosis

Taking the deterministic adversarial signs found by v0.9 at radius $0.016$, and switching to the exact displacement

$$
h_{\mathrm{corner}}=10^{-3},
$$

and fixing all positions at this rational corner. A zero-width recomputation yields

$$
\det T
\ge 0.1098330850588932>0.
$$

Therefore, the full-box Neumann failure at $h=10^{-3}$ cannot be interpreted as a counterexample having appeared at that corner or within the entire box.

## Unfinished Items

- The $58$ synthetic positions have not yet been proven to be the occupancy data of actual zeta zeros.
- The admissibility of the test function for the zeta explicit formula and the coefficient transfer have not yet been completed.
- The lift from the local finite-height certificate to the full critical strip RH criterion has not yet been closed.
- The strict radius still differs significantly in scale from the v0.9 floating-point diagnosis of approximately $0.016$, indicating that matrix interval dependency is the next technical bottleneck.