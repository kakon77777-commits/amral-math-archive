# Attack-Response Sequence and Convergence Criteria

## 1. Basic Ledger

Let:

\[
e_n
=
\mathcal A_{C_{n-1}}(\gamma_n)
\]

be the exposed area of the \(n\)-th attack curve with respect to the fixed old container.

Let:

\[
A_n
\]

be the area of the simply connected container after adding the first \(n\) test families and re-optimizing.

Define:

\[
\Delta A_n
=
A_n-A_{n-1}.
\]

By the direct inclusion construction:

\[
0\le\Delta A_n\le e_n
\]

holds, subject to numerical error and within the same container class.

Furthermore, define the absorption coefficient:

\[
\eta_n
=
\frac{e_n-\Delta A_n}{e_n},
\]

and the novelty coefficient:

\[
\nu_n
=
\frac{\Delta A_n}{e_n}
=
1-\eta_n.
\]

## 2. Numerical Values for Two Rounds

Round 5:

\[
e_5
=
0.006664458451,
\]

\[
\Delta A_5
=
0.002818179861,
\]

\[
\eta_5
\approx
57.7133%.
\]

Round 6:

\[
e_6
=
0.004934177792,
\]

\[
\Delta A_6
=
0.004464130667,
\]

\[
\eta_6
\approx
9.5443%.
\]

Although:

\[
e_6<e_5,
\]

we have:

\[
\Delta A_6>\Delta A_5.
\]

Therefore, merely tracking the decrease in the exposed attack area is insufficient to determine whether the container area sequence is converging.

## 3. Necessary Monitored Quantities

At a minimum, the following should be monitored simultaneously:

1. Exposed attack area:
   \[
   e_n;
   \]

2. Net area increment:
   \[
   \Delta A_n;
   \]

3. Absorption coefficient:
   \[
   \eta_n;
   \]

4. Holdout residual attack (not involved in training):
   \[
   e_n^{\mathrm{holdout}}.
   \]

For a monotonic area sequence \(A_n\), if a finite upper bound exists, then \(A_n\) converges; however, this upper bound and the complete family density have not yet been established in finite-sample experiments.

A more practically useful numerical stopping condition should simultaneously require:

\[
e_n^{\mathrm{holdout}}\le\varepsilon_{\mathrm{attack}},
\]

\[
\Delta A_n\le\varepsilon_{\mathrm{area}},
\]

and hold consistently across multiple Fourier dimensions, B-spline grids, and random seeds.

## 4. Round 6 Determination

An independent Fourier-14 audit yields:

\[
e_6^{\mathrm{holdout}}
=
0.006847625978.
\]

This is higher than the formal attack area of Round 6, and accounts for approximately the following percentage of the monomer tubular area:

\[
8.0535%.
\]

Therefore:

\[
\boxed{
\text{There is currently no evidence of monotonic convergence or approximate closure.}
}
\]

Round 7 should directly use this Fourier-14 curve as the attack seed.