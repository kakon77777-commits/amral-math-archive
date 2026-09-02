# Transient Pressurizing Curves: Separation of Historical Necessity and Final-State Activity

## 1. Phenomenon

The round 9 attack curve leaves on the fixed round 8 container:

\[
e_9
=
0.004050717099.
\]

It forces the container to increase from:

\[
A_8
=
0.208938653597
\]

to:

\[
A_9
=
0.211402629026.
\]

However, after rearranging all curves in round 9, the exposure left by removing this curve is only:

\[
\ell_9
=
0.000664164818.
\]

and:

\[
\ell_9<10^{-3}.
\]

## 2. Definition

A curve \(\gamma_n\) is called a **transient pressurizing curve** in the container sequence if:

\[
\mathcal A_{C_{n-1}}(\gamma_n)
\ge
\varepsilon_{\mathrm{attack}},
\]

but after the update:

\[
\mathcal L_{C_n}(\gamma_n)
<
\varepsilon_{\mathrm{active}},
\]

where \(\mathcal L\) is the final-state leave-one-out exposure.

This indicates that:

- The curve historically triggered the expansion of the container;
- After the update, the other skeletons of the container have collectively covered its main pressure;
- The static final-state activity ledger will underestimate its causal role.

## 3. Historical Activity and Final-State Activity

Therefore, a distinction should be made between:

### Final-State Active Family

Those that still leave a significant exposure after being removed from the current container.

### Historical Pressurizing Family

Those that previously caused a significant positive exposure to the previous container and led to an area increase.

The two are not equivalent:

\[
\boxed{
\text{Historically Necessary}
\not\Rightarrow
\text{Final-State Active}.
}
\]

## 4. Impact on the Research Ledger

Subsequent alternating research cannot solely save the final leave-one-out rankings.

At a minimum, the following must be saved simultaneously:

\[
e_n,
\qquad
\Delta A_n,
\qquad
\ell_n.
\]

where:

- \(e_n\): The attack pressure on the fixed old container;
- \(\Delta A_n\): The net increment after the container responds;
- \(\ell_n\): The static activity of the new curve in the final-state container.

These three quantities respectively describe:

\[
\text{Attack Intensity},
\quad
\text{Causal Area Cost},
\quad
\text{Final-State Structural Necessity}.
\]