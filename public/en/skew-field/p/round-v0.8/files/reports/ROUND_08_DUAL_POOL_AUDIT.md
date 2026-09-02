# Fourier-18 Dual Pools and B-spline Reserve Audit

## 1. Motivation

Round 7 revealed two different spatial attacks:

- Distributed multi-lobe type;
- Local deep penetration type.

Round 8 no longer perturbs solely along a single parent lineage, but establishes:

1. Distributed parent Fourier-18 pool;
2. Local penetration parent Fourier-18 pool;
3. Non-Fourier smooth B-spline reserve pool.

## 2. Search Results

The distributed parent pool has a total of:

\[
24
\]

valid candidates, with the best refined exposure:

\[
\boxed{
e_{\mathrm{dist}}
=
0.004050690308.
}
\]

The local parent pool has a total of:

\[
24
\]

valid candidates, with the best value:

\[
e_{\mathrm{loc}}
=
0.003625184186.
\]

The B-spline pool has a total of:

\[
20
\]

valid candidates. After performing global placement refinement on all candidates with a fast exposure upper bound exceeding \(10^{-3}\), the best value is:

\[
e_{\mathrm{spline}}
=
0.000021419854.
\]

This batch of B-spline candidates did not leave any stable exposure above \(10^{-3}\).

## 3. Failure of Surrogate Ranking

The fast search uses local placements inherited from the parent curve.

However, after a complete global congruence search, the candidate ranking changes significantly.

The final strongest curve is not the one ranked first by the local surrogate.

Therefore:

\[
\boxed{
\text{Curve ranking in non-convex containers cannot be certified by a single inherited configuration.}
}
\]

Local clearance or local exposure surrogates can only be responsible for generating candidates; ultimately, one must re-evaluate:

\[
\inf_{g\in E(2)}
\mu_2
\left[
(gT_\rho(\gamma))\setminus C
\right].
\]

## 4. Dual Pools Did Not Form a Binary Closure

Both Fourier-18 parent lineages still leave curves with positive exposure.

However, the best value of the distributed parent lineage is slightly higher than that of the local parent lineage:

\[
e_{\mathrm{dist}}
>
e_{\mathrm{loc}}.
\]

Thus, the container is not left with only a single weak mode.

On the contrary, it can still be breached by different spectral parent lineages using different spatial patterns.