---
title: "Navier–Stokes Ancestry Necessity Program 07：Horizon-Persistent Branch Extraction、Strong-Child Compactness、Causal Edge Closure 與 Renewal-Rate Alternative"
short_title: "NS-ANP 07"
series: "Navier–Stokes Ancestry Necessity Program"
cycle: "IV"
version: "v0.1"
date: "2026-08-15"
author: "Neo.K / EveMissLab"
language: "zh-TW"
status: "Horizon-persistence reduction / compactness and renewal alternative"
epistemic_status: "Develops the final actual-branch persistence layer after ANP-06. Proves abstract finite-child and compact-child Horizon-Persistent Child criteria; under threshold-finite strong-child branching, failure of HPC forces horizon transmission collapse. Proves a horizon-cut dual-ledger theorem: if propagated inheritance across a shrinking terminal window is small, normalized fresh-source rate must diverge at least like the inverse window length. Establishes a local Causal Edge Closure theorem for normalized bounded-relative-frequency, band-limited C3_W edges under strong local compactness and controlled kernel-inflated footprints; nontrivial edge limits follow under a uniform transmission floor. Critical profile decomposition and Type-I ancient-solution literature are used as external compactness calibration, but profile/ancient limits are not identified with actual ancestry chains in the original solution. Actual HP1/HPC remain unproved without a horizon transmission noncollapse or actual-child compactness theorem. Full CN3 Chain Necessity, Finite Obstruction, and Navier-Stokes regularity remain OPEN."
canonical_source: "UTF-8 Markdown"
---

# Navier–Stokes Ancestry Necessity Program 07

# Horizon-Persistent Branch Extraction、Strong-Child Compactness、Causal Edge Closure 與 Renewal-Rate Alternative

## 0. 本文定位

ANP-06 reduced strong Chain Necessity to the horizon-persistence obligations:

$$
HP1,
\quad
HP2,
\quad
HP3,
\quad
HP4.
$$

The present paper asks:

> what exactly prevents a horizon-persistent marked causal branch from being extracted?

The answer is now split into two fundamentally different failure mechanisms:

$$
\boxed{
D_{\rm HTRANS}
}
$$

and:

$$
\boxed{
D_{\rm HCOMP}.
}
$$

The first is transmission degeneration.

The second is compactness/edge-closure degeneration.

The paper also proves that direct inheritance collapse over vanishing terminal windows forces an increasingly large fresh-source renewal rate.

---

# 1. Horizon gates

For:

$$
q\in\mathbb N,
$$

define:

$$
\boxed{
\mathcal H_q
=
\{
\mathsf F:
T_\ast-2^{-q}<t(\mathsf F)<T_\ast,
\quad
k(\mathsf F)\ge q
\}.
}
$$

The gates are nested:

$$
\boxed{
\mathcal H_{q+1}
\subset
\mathcal H_q.
}
$$

Universal causal-state entry gives nonempty arbitrarily high gates.

---

# 2. Horizon reach

For a marked causal node:

$$
\mathsf P,
$$

define:

$$
\boxed{
r_H(\mathsf P)
=
\sup
\{
q:
\mathsf P
\leadsto_{C3}
\mathcal H_q
\}.
}
$$

Use the convention:

$$
r_H(\mathsf P)=\infty
$$

when the node has marked C3 descendants in every sufficiently high horizon gate.

Such a node is:

$$
\boxed{
\text{horizon-persistent}.
}
$$

---

# 3. Immediate marked children

Let:

$$
\mathcal C(\mathsf P)
$$

be the set of admissible immediate marked C3 children of:

$$
\mathsf P
$$

under a fixed generation semantics.

Every:

$$
\mathsf C\in\mathcal C(\mathsf P)
$$

has a positive edge transmission coordinate:

$$
\boxed{
\vartheta(
\mathsf P\to\mathsf C
)
>0.
}
$$

---

# 4. CIV-7.1 — Finite-Child Horizon Persistence

## Theorem 4.1

Assume:

$$
\mathsf P
$$

is horizon-persistent and:

$$
\mathcal C(\mathsf P)
$$

is finite.

Assume every marked descendant path from:

$$
\mathsf P
$$

to a sufficiently high horizon gate begins through one member of:

$$
\mathcal C(\mathsf P).
$$

Then at least one:

$$
\mathsf C_\ast
\in
\mathcal C(\mathsf P)
$$

is horizon-persistent.

### Proof

For every sufficiently large:

$$
q,
$$

choose a path from:

$$
\mathsf P
$$

to:

$$
\mathcal H_q.
$$

Its first child belongs to the finite set:

$$
\mathcal C(\mathsf P).
$$

One child occurs for infinitely many:

$$
q.
$$

Because the gates are nested, that child reaches every fixed gate and is horizon-persistent.

$\square$

---

# 5. Strong-child threshold

For:

$$
\eta>0,
$$

define the strong child set:

$$
\boxed{
\mathcal C_\eta(\mathsf P)
=
\left\{
\mathsf C\in\mathcal C(\mathsf P):
\vartheta(
\mathsf P\to\mathsf C
)
\ge
\eta
\right\}.
}
$$

Define:

$$
\boxed{
\textbf{TFB — threshold-finite branching}
}
$$

by:

$$
\boxed{
|\mathcal C_\eta(\mathsf P)|<\infty
\quad
\forall
\eta>0.
}
$$

TFB is weaker than finite total branching.

---

# 6. Horizon strong transmission

For:

$$
q
$$

define:

$$
\boxed{
\Theta_q(\mathsf P)
=
\sup
\left\{
\vartheta(
\mathsf P\to\mathsf C
):
\mathsf C
\text{ is the first child of a marked path from }
\mathsf P
\text{ to }
\mathcal H_q
\right\}.
}
$$

If no such path exists, set:

$$
\Theta_q(\mathsf P)=0.
$$

For a horizon-persistent parent:

$$
\Theta_q(\mathsf P)>0
$$

for arbitrarily large:

$$
q.
$$

---

# 7. CIV-7.2 — Strong-Transmission HPC Criterion

## Theorem 7.1

Assume:

1. $\mathsf P$ is horizon-persistent;
2. TFB holds at $\mathsf P$;
3. there exists:
   $$
   \eta_0>0
   $$
   such that:
   $$
   \Theta_q(\mathsf P)
   \ge
   \eta_0
   $$
   for infinitely many:
   $$
   q.
   $$

Then:

$$
\boxed{
\mathsf P
\text{ has a horizon-persistent child}.
}
$$

### Proof

For each qualifying:

$$
q,
$$

choose a first child with transmission at least:

$$
\eta_0/2.
$$

All such children lie in the finite set:

$$
\mathcal C_{\eta_0/2}(\mathsf P).
$$

Apply the infinite pigeonhole principle.

$\square$

---

# 8. Horizon transmission collapse

Define:

$$
\boxed{
D_{\rm HTRANS}(\mathsf P)
}
$$

by:

$$
\boxed{
\Theta_q(\mathsf P)
\to0
\quad
\text{along the horizon gates reached by }
\mathsf P.
}
$$

---

# 9. CIV-7.3 — HPC Failure / Transmission Collapse Alternative

## Theorem 9.1

Assume:

- $\mathsf P$ is horizon-persistent;
- TFB holds;
- $\mathsf P$ has no horizon-persistent child.

Then:

$$
\boxed{
D_{\rm HTRANS}(\mathsf P)
}
$$

must hold.

### Proof

If horizon transmission did not collapse, some:

$$
\eta_0>0
$$

would occur along infinitely many horizon gates.

Theorem 7.1 would then produce a horizon-persistent child.

Contradiction.

$\square$

---

# 10. Meaning of D-HTRANS

Horizon persistence can fail even though every finite causal edge is legal.

The failure mechanism is:

> the causal contribution that survives into later and later horizon gates is distributed among children with smaller and smaller individual transmission.

This is not source nonexistence.

It is **horizon causal fragmentation**.

---

# 11. Compact-child persistence

Finite branching is not the only route.

Let:

$$
\mathcal C_\eta(\mathsf P)
$$

be a strong-child family equipped with a topology:

$$
\tau_C.
$$

Define the fixed-gate reach set:

$$
\boxed{
\mathcal R_q(\mathsf P)
=
\left\{
\mathsf C\in
\mathcal C(\mathsf P):
\mathsf C
\leadsto_{C3}
\mathcal H_q
\right\}.
}
$$

---

# 12. CIV-7.4 — Compact-Child Horizon Persistence

## Theorem 12.1

Assume:

1. $\mathsf P$ is horizon-persistent;
2. for some:
   $$
   \eta_0>0,
   $$
   every sufficiently high reached gate has a first child in:
   $$
   \mathcal C_{\eta_0}(\mathsf P);
   $$
3. $\mathcal C_{\eta_0}(\mathsf P)$ is sequentially compact in:
   $$
   \tau_C;
   $$
4. for every fixed:
   $$
   r,
   $$
   the set:
   $$
   \mathcal R_r(\mathsf P)
   \cap
   \mathcal C_{\eta_0}(\mathsf P)
   $$
   is sequentially closed.

Then:

$$
\boxed{
\mathsf P
\text{ has a horizon-persistent child}.
}
$$

### Proof

Choose:

$$
q_n\to\infty
$$

and strong first children:

$$
\mathsf C_n
$$

leading to:

$$
\mathcal H_{q_n}.
$$

Sequential compactness gives:

$$
\mathsf C_n
\to
\mathsf C_\ast.
$$

Fix:

$$
r.
$$

For all sufficiently large:

$$
n,
$$

$$
q_n\ge r,
$$

and:

$$
\mathcal H_{q_n}
\subset
\mathcal H_r.
$$

Hence:

$$
\mathsf C_n\in\mathcal R_r.
$$

Closedness gives:

$$
\mathsf C_\ast\in\mathcal R_r.
$$

Since:

$$
r
$$

is arbitrary:

$$
r_H(\mathsf C_\ast)=\infty.
$$

$\square$

---

# 13. Compactness failure coordinate

Define:

$$
\boxed{
D_{\rm HCOMP}
}
$$

as failure of at least one of:

1. strong-child sequential compactness;
2. fixed-gate reach closure;
3. C3 edge closure;
4. nontriviality under the child limit.

Thus the horizon problem has the reduction:

$$
\boxed{
\text{HPC}
\vee
D_{\rm HTRANS}
\vee
D_{\rm HCOMP}.
}
$$

---

# 14. Horizon-cut dual ledger

Let:

$$
\mathsf C_n
$$

be terminal marked nodes with:

$$
t_n\uparrow T_\ast.
$$

Let:

$$
A_n>0
$$

be their terminal dual amplitudes.

Choose shrinking terminal windows:

$$
\delta_n>0,
\qquad
\delta_n\to0,
$$

and set:

$$
a_n=t_n-\delta_n.
$$

The ANP-06 dual ledger gives:

$$
\boxed{
A_n
=
\mathcal I_n
+
\mathcal Q_n,
}
$$

where:

$$
\mathcal I_n
$$

is the homogeneous propagated inheritance contribution from:

$$
a_n,
$$

and:

$$
\mathcal Q_n
$$

is the intervening source contribution.

---

# 15. Fresh-source ratio

Define:

$$
\boxed{
i_n
=
\frac{
\mathcal I_n
}{
A_n
},
}
$$

and:

$$
\boxed{
q_n
=
\frac{
\mathcal Q_n
}{
A_n
}.
}
$$

Then:

$$
\boxed{
1=i_n+q_n.
}
$$

If:

$$
i_n\le1-\sigma,
$$

for:

$$
\sigma>0,
$$

then:

$$
\boxed{
q_n\ge\sigma.
}
$$

---

# 16. Fresh-source rate

Define:

$$
\boxed{
\mathfrak R_{\rm fresh,n}
=
\frac{
1
}{
\delta_nA_n
}
\int_{a_n}^{t_n}
\left|
\langle
F_{k_n}(s),
\Phi_n(s)
\rangle
\right|ds.
}
$$

---

# 17. CIV-7.5 — Horizon Renewal-Rate Theorem

## Theorem 17.1

If:

$$
i_n
\le
1-\sigma
$$

for some fixed:

$$
\sigma>0,
$$

then:

$$
\boxed{
\mathfrak R_{\rm fresh,n}
\ge
\frac{
\sigma
}{
\delta_n
}.
}
$$

Hence if:

$$
\delta_n\to0,
$$

$$
\boxed{
\mathfrak R_{\rm fresh,n}
\to\infty.
}
$$

### Proof

The absolute source integral dominates the signed source contribution:

$$
\int
|\langle F,\Phi\rangle|
\ge
\mathcal Q_n
\ge
\sigma A_n.
$$

Divide by:

$$
\delta_nA_n.
$$

$\square$

---

# 18. Interpretation of the renewal-rate theorem

Near the singular horizon, the terminal marked state must be explained by one of:

### PERSISTENT PROPAGATION

A nontrivial fraction comes from an earlier propagated state.

### FRESH RENEWAL

A fixed fraction is recreated by nonlinear source inside an increasingly short terminal window, forcing source-rate growth at least:

$$
O(\delta^{-1}).
$$

This is a causal relation statement, not a regularity contradiction.

---

# 19. Horizon causal-flux alternative

For a shrinking horizon window:

$$
[t-\delta,t],
$$

define the normalized causal flux:

$$
\boxed{
\mathcal F_{\rm causal}
=
\max
\left\{
\frac{
[\mathcal I]_+
}{
A_c
},
\,
\frac{
1
}{
A_c
}
\int_{t-\delta}^{t}
|\langle F,\Phi\rangle|ds
\right\}.
}
$$

The exact dual ledger implies:

$$
\boxed{
\mathcal F_{\rm causal}
\ge
\frac12.
}
$$

Thus causal influence cannot disappear across a horizon cut.

It may change from persistent-state transport to fresh nonlinear source generation.

---

# 20. Causal flow versus causal lineage

Theorem 19 proves a horizon-directed **causal flux** statement.

It does not prove that the flux travels through one persistent marked lineage.

This distinction is fundamental:

$$
\boxed{
\text{causal flux necessity}
\neq
\text{causal lineage necessity}.
}
$$

The former is now quantitatively controlled.

The latter is CN3.

---

# 21. Normalized source-edge family

Consider a sequence of weighted C3_W source-parent edges:

$$
\mathsf P_n
\overset{C3_W}{\longrightarrow}
\mathsf C_n.
$$

Normalize each edge by:

1. translating the child footprint centroid to:
   $$
   0;
   $$
2. scaling the child output shell to:
   $$
   k=0;
   $$
3. normalizing the child weighted shell amplitude to:
   $$
   1.
   $$

Assume:

### B1 — bounded relative frequencies

Parent/partner shell offsets relative to the child are bounded by:

$$
L_0.
$$

### B2 — bounded shell state norms

The normalized participating dyadic fields are uniformly bounded in global:

$$
L^2.
$$

### B3 — controlled footprint class

The kernel-inflated weights have uniformly bounded mass, aperture, and fixed-scale smoothing bounds.

### B4 — positive transmission floor

$$
\vartheta_n
\ge
\vartheta_0>0.
$$

---

# 22. Band-limited compactness

Under B1--B2, each normalized dyadic field has Fourier support in one of finitely many fixed annuli and is uniformly bounded in:

$$
L^2.
$$

Bernstein gives uniform:

$$
H^m
$$

bounds for every fixed:

$$
m
$$

after normalization.

Rellich compactness gives, after subsequence extraction:

$$
\boxed{
f_n
\to
f
\quad
\text{strongly in }
L^2_{\rm loc}.
}
$$

for every participating normalized dyadic state.

---

# 23. Footprint compactness

The ANP-03 kernel-inflated weights are convolutions with fixed smooth probability kernels after normalization.

Under B3 they have uniformly bounded derivatives on compact sets and tight mass from the aperture bound.

Hence, after subsequence extraction:

$$
\boxed{
\psi_n
\to
\psi
}
$$

locally uniformly and weakly in:

$$
L^1.
$$

The limit is a nonnegative controlled-aperture footprint.

---

# 24. Bilinear product closure

If:

$$
f_n\to f,
\qquad
g_n\to g
$$

strongly in:

$$
L^2_{\rm loc},
$$

and both families are uniformly band-limited/bounded, then:

$$
\boxed{
f_ng_n
\to
fg
}
$$

strongly in:

$$
L^1_{\rm loc}.
$$

After the fixed normalized dyadic projector is applied, projected bilinear source atoms converge locally.

---

# 25. CIV-7.6 — Local Causal Edge Closure

## Theorem 25.1

Under B1--B4, a sequence of normalized C3_W bilinear source-parent edges admits a subsequence whose node data converge and whose realized local weighted bilinear source contribution converges to the corresponding source contribution of the limit fields.

In particular the limiting source edge remains:

$$
\boxed{
C3_W
}
$$

provided the normalized provenance/representation maps converge in the same finite-offset class.

### Meaning

Causal Edge Closure is available on the **bounded normalized profile branch**.

$\square$

---

# 26. Nontriviality of the edge limit

Because:

$$
\vartheta_n
\ge
\vartheta_0>0,
$$

and child amplitude is normalized to:

$$
1,
$$

the parent weighted state lower bound stays uniformly positive.

Thus the limit parent node is nonzero.

---

# 27. CIV-7.7 — Nontrivial Limit on the Strong Compact Branch

## Theorem 27.1

Under B1--B4:

$$
\boxed{
HP3
+
HP4
}
$$

are satisfied for the normalized local C3_W edge subsequence.

That is:

- nonlinear causal contribution survives the limit;
- the marked parent state does not vanish.

$\square$

---

# 28. What can still destroy compact C3 closure?

The hypotheses B1--B4 isolate the remaining escapes:

### $D_{\rm FJUMP}$

Relative frequency offsets become unbounded.

### $D_{\rm GNORM}$

Normalized participating global shell:

$$
L^2
$$

norms blow up.

### $D_{\rm SPACE}$

Footprint tightness/aperture fails.

### $D_{\rm HTRANS}$

Transmission tends to zero.

Thus:

$$
\boxed{
D_{\rm HCOMP}
\subset
D_{\rm FJUMP}
\vee
D_{\rm GNORM}
\vee
D_{\rm SPACE}
\vee
D_{\rm HTRANS}
}
$$

for the local C3_W source class.

---

# 29. Critical profile decomposition calibration

Gallagher--Koch--Planchon develop Navier--Stokes profile decomposition in critical Besov spaces and construct critical elements/minimal blow-up data under hypothetical blow-up assumptions.

Bahouri--Chemin--Gallagher develop stability under rescaled weak convergence by profile decomposition and propagation of profiles.

These results demonstrate that translation/scaling/profile-splitting defects can be systematically decomposed in critical spaces.

They do not by themselves identify one actual C3 ancestry branch in the original solution.

---

# 30. Type-I ancient-profile calibration

Albritton--Barker prove that local Type-I singularities are equivalent to existence of a nontrivial mild bounded ancient solution satisfying a Type-I decay condition.

Thus Type-I blow-up admits a nontrivial renormalized ancient profile description.

This gives strong evidence that:

$$
\boxed{
HP4\text{-type nontriviality}
}
$$

can survive rescaling in the Type-I state layer.

It does not prove actual-node horizon persistence in the original solution.

---

# 31. Minimal critical element calibration

Rusin--Sverak and Gallagher--Koch--Planchon show, under hypothetical blow-up assumptions in suitable critical spaces, the existence of minimal blow-up data/critical elements.

This is a concentration-compactness selection principle.

ANP requires more:

$$
\boxed{
\text{minimal/compact state profile}
+
\text{actual source provenance}
+
\text{same-solution branch realization}.
}
$$

---

# 32. Profile chain versus actual chain

A profile decomposition may produce:

$$
\boxed{
\Gamma_\infty^{prof}.
}
$$

Strong Chain Necessity requires:

$$
\boxed{
\Gamma_\infty^{act}
}
$$

inside the original solution.

A profile chain can support a compactness proof or contradiction.

It is not automatically an actual causal lineage.

---

# 33. Horizon-persistence reduction

The results of this paper give:

$$
\boxed{
\text{HPC}
\vee
D_{\rm HTRANS}
\vee
D_{\rm FJUMP}
\vee
D_{\rm GNORM}
\vee
D_{\rm SPACE}.
}
$$

On the bounded normalized strong-child branch, CEC and nontrivial limit are no longer the primary obstacle.

The principal actual-lineage obstruction is horizon transmission/branch persistence.

---

# 34. HP status update

### HP1 — Horizon-persistent actual node

Still:

$$
\boxed{
\mathrm{OPEN}.
}
$$

### HP2 — Horizon-Persistent Child

Proved under:

- finite-child condition;
- threshold-finite + noncollapsing transmission;
- compact-child + reach-closure conditions.

Unconditional status:

$$
\boxed{
\mathrm{OPEN}.
}
$$

### HP3 — Causal Edge Closure

$$
\boxed{
\mathrm{PROVED\ ON\ THE\ BOUNDED\ NORMALIZED\ C3_W\ BRANCH}.
}
$$

### HP4 — Nontrivial Limit

$$
\boxed{
\mathrm{PROVED\ ON\ THE\ SAME\ STRONG\ COMPACT\ BRANCH}.
}
$$

---

# 35. Strong Chain-Necessity test

CN3 would follow if one proves:

1. an actual HP1 node;
2. recursive HPC;
3. exclusion/absorption of:
   $$
   D_{\rm HTRANS},
   D_{\rm FJUMP},
   D_{\rm GNORM},
   D_{\rm SPACE};
   $$
4. bounded normalized C3 edge closure on the surviving branch.

Items 1--3 remain incomplete.

Therefore:

$$
\boxed{
CN3
:
\mathrm{OPEN}.
}
$$

---

# 36. The actual remaining question

The problem is no longer generic compactness.

It is:

> can causal influence reaching arbitrarily late dangerous states keep splitting into weaker and/or more scale-separated branches so that no single actual child remains horizon-persistent?

This is a **causal fragmentation** problem.

---

# 37. Horizon-renewal interpretation of transmission collapse

If:

$$
D_{\rm HTRANS}
$$

occurs repeatedly, older marked causal contributions become negligible in later gates.

The dual horizon-cut theorem then forces later nodes to be increasingly supported by fresh nonlinear source in short windows.

Thus:

$$
\boxed{
D_{\rm HTRANS}
\Longrightarrow
\text{asymptotically fresh causal renewal}
}
$$

at the direct cut level.

The missing theorem is whether repeated fresh renewal can itself be organized into one marked C3 lineage or must pay an already-known coercive action strongly enough to close the branch.

---

# 38. Next paper

The next paper should target exactly this:

$$
\boxed{
\textbf{
NS-ANP 08 —
Horizon Transmission Rigidity、
Fresh-Source Cascade、
Actual-Branch Shadowing
與 Strong Chain-Necessity Closure
}.
}
$$

Primary tasks:

1. quantify repeated:
   $$
   D_{\rm HTRANS};
   $$
2. connect fresh-source rates to DRC driver/model-cone/dissipation actions;
3. determine whether source-renewal packets themselves admit horizon-persistent C3 parents;
4. control:
   $$
   D_{\rm FJUMP},
   D_{\rm GNORM},
   D_{\rm SPACE};
   $$
5. attempt an actual-branch shadowing theorem;
6. decide CN3.

Finite Obstruction remains after this.

---

# 39. Formal status ledger

$$
\boxed{
\begin{aligned}
\text{finite-child HPC criterion}
&:\ \mathrm{PROVED},\\
\text{strong-transmission HPC criterion}
&:\ \mathrm{PROVED},\\
\text{HPC failure}\Rightarrow D_{\rm HTRANS}
&:\ \mathrm{PROVED\ UNDER\ TFB},\\
\text{compact-child HPC criterion}
&:\ \mathrm{PROVED},\\
\text{horizon renewal-rate theorem}
&:\ \mathrm{PROVED},\\
\text{horizon causal-flux lower bound}
&:\ \mathrm{PROVED},\\
\text{band-limited normalized node compactness}
&:\ \mathrm{PROVED\ UNDER\ B1\mbox{-}B3},\\
\text{local C3 edge closure}
&:\ \mathrm{PROVED\ UNDER\ B1\mbox{-}B4},\\
\text{nontrivial C3 limit}
&:\ \mathrm{PROVED\ UNDER\ B1\mbox{-}B4},\\
HP1
&:\ \mathrm{OPEN},\\
HP2
&:\ \mathrm{OPEN\ UNCONDITIONALLY},\\
HP3
&:\ \mathrm{PARTIALLY\ CLOSED},\\
HP4
&:\ \mathrm{PARTIALLY\ CLOSED},\\
CN3
&:\ \mathrm{OPEN},\\
\text{Finite Obstruction}
&:\ \mathrm{OPEN},\\
\text{Navier--Stokes regularity}
&:\ \mathrm{NOT\ PROVED}.
\end{aligned}
}
$$

---

# 40. Conclusion

ANP-07 narrows the strong Chain-Necessity gap again.

Horizon-Persistent Child is automatic if the relevant first-generation child family is finite.

It is also automatic on a compact strong-child family with closed gate reach.

Under threshold-finite branching, failure of HPC forces:

$$
\boxed{
\Theta_q\to0,
}
$$

that is, horizon transmission collapse.

At the same time, the exact dual ledger proves that loss of propagated inheritance across a shrinking terminal window forces fresh nonlinear source at a rate at least:

$$
\boxed{
O(\delta^{-1}).
}
$$

So horizon causality cannot disappear.

It can only become increasingly fresh and fragmented.

For normalized C3_W edges with bounded relative scales, bounded shell norms, controlled footprints, and a transmission floor, the nonlinear causal edge is compact and survives the limit.

Thus the principal remaining obstacle is not generic weak compactness.

It is actual-branch horizon persistence:

$$
\boxed{
\text{does some nontrivial causal lineage survive all the way to }T_\ast?
}
$$

That is the target of ANP-08.

---

# References

1. I. Gallagher, G. S. Koch, F. Planchon, *A profile decomposition approach to the $L^\infty_t(L^3_x)$ Navier--Stokes regularity criterion*, arXiv:1012.0145.
2. H. Bahouri, J.-Y. Chemin, I. Gallagher, *Stability by rescaled weak convergence for the Navier--Stokes equations*, arXiv:1310.0256.
3. D. Albritton, T. Barker, *On local Type I singularities of the Navier--Stokes equations and Liouville theorems*, arXiv:1811.00502.
4. W. Rusin, V. Sverak, *Minimal initial data for potential Navier--Stokes singularities*, arXiv:0911.0500.
5. T. Tao, *Quantitative bounds for critically bounded solutions to the Navier--Stokes equations*, arXiv:1908.04958.
6. S. Palasek, *Improved quantitative regularity for the Navier--Stokes equations in a scale of critical spaces*, arXiv:2101.08586.
7. T. Barker, *Quantitative classification of potential Navier--Stokes singularities beyond the blow-up time*, arXiv:2510.20757.
8. `NS_ANP_06_SingularHorizon_ExtractionAudit_v0.1.md`.
