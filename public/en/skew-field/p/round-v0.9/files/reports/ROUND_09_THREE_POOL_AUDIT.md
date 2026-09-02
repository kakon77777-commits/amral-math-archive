# Fourier-20 Three-Phenotype Pool and Moving-Knot B-spline Retention Audit

## 1. Three Fourier Parent Lineages

This round divides the 20-mode candidates into:

1. Dispersed parent lineage;
2. Local penetration parent lineage;
3. Mixed parent lineage.

Each pool generates 12 candidates that pass the positive curvature, radius of curvature, radial condition, and simple condition.

The local inheritance configuration is only used for initial screening; all final values are re-solved for full congruent placement.

## 2. Global Refinement Results

Dispersed parent lineage:

\[
e_{\mathrm{dist}}
=
0.003755030295.
\]

Local parent lineage:

\[
e_{\mathrm{loc}}
=
0.000000000000.
\]

Mixed parent lineage:

\[
\boxed{
e_{\mathrm{mix}}
=
0.004423629900.
}
\]

The refined candidates of the local parent lineage in this batch can all be absorbed by the Round 9 container, but the dispersed and mixed parent lineages still leave positive exposure.

## 3. Non-Fourier Retention Pool

This round uses moving-knot natural cubic B-spline logarithmic curvature for the first time:

\[
g(s)=\operatorname{Spline}\{(u_j,v_j)\},
\]

\[
\kappa(s)
=
\frac{
\pi e^{g(s)}
}{
\int_0^1e^{g(u)}du
}.
\]

Among the 20 candidates, the best value after refinement is:

\[
\boxed{
e_{\mathrm{spline}}
=
0.002135639003.
}
\]

Therefore, the phenomenon of "B-spline approaching closure" in Round 8 does not extend to moving knots and larger perturbation families.

## 4. Parent Lineage and Phenotype Decoupled Again

The maximum exposure component of the best candidate in the dispersed parent lineage accounts for:

\[
79.0587%,
\]

Effective gap box count:

\[
4.294804.
\]

It actually exhibits a tendency for deep local penetration.

The best candidate in the mixed parent lineage has five components, with the maximum component accounting for:

\[
63.2415%,
\]

Effective gap box count:

\[
10.332930.
\]

Therefore:

\[
\boxed{
\text{Spectral parent lineage}
\not\Rightarrow
\text{Final spatial phenotype}.
}
\]

## 5. Conclusion

Currently, local closure only appears in the local Fourier-20 parent lineage of this batch.

However:

- The dispersed Fourier-20 pool remains positive;
- The mixed Fourier-20 pool remains positive;
- The moving-knot B-spline pool also remains positive.

Therefore, the Round 9 container has not yet formed a stable closure for multiple families of curvature representations.