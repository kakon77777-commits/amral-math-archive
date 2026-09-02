# Dual Ledger of Historical Pressure Memory and Final-State Activity

## 1. Three Different Quantities

For the \(n\)-th round attack curve, record:

\[
e_n
=
\mathcal A_{C_{n-1}}(\gamma_n),
\]

\[
\Delta A_n
=
A_n-A_{n-1},
\]

\[
\ell_n
=
\text{curve }\gamma_n
\text{ in final leave-one-out ledger}.
\]

They respectively describe:

- The attack intensity against the fixed old container;
- The causal area cost after the container's response;
- The necessity of the final-state structure after the update.

## 2. Classification

Define the persistence ratio:

\[
\pi_n=\frac{\ell_n}{e_n}.
\]

If:

\[
e_n\ge\varepsilon_{\mathrm{attack}},
\qquad
\ell_n<\varepsilon_{\mathrm{active}},
\]

then it is a **transient pressure curve**.

If:

\[
e_n\ge\varepsilon_{\mathrm{attack}},
\qquad
\ell_n\ge\varepsilon_{\mathrm{active}},
\]

then it is a **persistent skeleton curve**.

## 3. Round 10 Results

\[
e_{10}
=
0.004423629900,
\]

\[
\Delta A_{10}
=
0.002395303600,
\]

\[
\ell_{10}
=
0.002307467379.
\]

Therefore:

\[
\pi_{10}
=
52.1623%.
\]

Fourier-20 is a persistent skeleton.

The leave-one-out exposure of the 9th round attack in \(C_{10}\) is only:

\[
0.000044750202,
\]

It still belongs to the transient pressure type.

## 4. Memory Principle

Container optimization cannot solely retain the current final-state active family.

All curves that have ever satisfied:

\[
e_n\ge\varepsilon_{\mathrm{attack}}
\]

should be kept in the historical test set to prevent the container from reopening patched gaps when compressing the current active skeleton.

Therefore:

\[
\boxed{
\text{Container State}
=
\text{Final-State Active Skeleton}
+
\text{Historical Pressure Memory}.
}
\]