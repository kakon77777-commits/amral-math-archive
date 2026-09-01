---
title: "Navier–Stokes Ancestry Necessity Program 02: Recursive Edge Compatibility, Adjoint-Footprint Aperture, Canonical Footprint Nodes, and Parent-Localization Gap"
short_title: "NS-ANP 02"
series: "Navier–Stokes Ancestry Necessity Program"
cycle: "IV"
version: "v0.1"
date: "2026-08-15"
author: "Neo.K / EveMissLab"
language: "en"
status: "Theorem-style recursive-footprint compatibility / geometric source-locality audit"
epistemic_status: "Proves a second-moment aperture estimate for the terminal-core adjoint footprint under the Type-I L_t^infty L_x^{3,infty} bound, yielding quantitative core-scale mass recapture over parabolic time windows. Proves exact adjoint semigroup provenance and introduces a canonical Footprint Spectrum Node whose spatial weight and full dyadic state profile are stable under backward recursion, thereby closing the footprint/representation component of Recursive Edge Compatibility. Derives exact shellwise weighted vorticity identities and monotone square-tail observables. A functional-analytic no-go shows that localization of the adjoint weight alone does not force localization of a weighted nonlinear source. Thus weighted-footprint recursion is proved, while geometric source-parent recapture remains open. The resulting edge is recursively stable at the weighted-state level but is not yet a full geometric C3 source ancestry edge. Chain Necessity, Finite Obstruction, and Navier-Stokes regularity are NOT proved."
canonical_source: "UTF-8 Markdown"
---

# Navier–Stokes Ancestry Necessity Program 02

# Recursive Edge Compatibility, Adjoint-Footprint Aperture, Canonical Footprint Nodes, and Parent-Localization Gap

## 0. Context of this Paper

ANP-01 proved:

$$
\boxed{
\mathrm{SCPB\mbox{-}W}
:
\text{weighted output-local Source--Core Provenance}
}
$$

and obtained a genuine:

$$
\boxed{
C2
}
$$

forward PDE causal edge.

It left open:

$$
\boxed{
\mathrm{SCPB\mbox{-}G}
:
\text{geometric parent/source localization},
}
$$

and:

$$
\boxed{
\mathrm{SCPB\mbox{-}R}
:
\text{recursive core recapture}.
}
$$

The present paper separates these two issues.

The first result is positive:

> the adjoint causal footprint itself has quantitatively controlled aperture in the Type-I branch.

The second result is also positive:

> the adjoint footprint and its full dyadic state profile form a recursively stable node class.

The third result is a no-go:

> geometric concentration of the adjoint weight does not, by itself, force the nonlinear source density to be concentrated in the same region.

Therefore Recursive Edge Compatibility is partly closed at the **footprint/state representation layer**, but full source-parent geometric recapture remains open.

---

# 1. Normalization

Normalize viscosity:

$$
\boxed{
\nu=1.
}
$$

Fix a terminal Type-I core time:

$$
t_j<T_\ast,
$$

terminal core center:

$$
x_\ast=0,
$$

and radius:

$$
R=R_j.
$$

Let:

$$
\chi_j(x)
=
\phi(x/R)
$$

with:

$$
0\le\phi\le1,
$$

$$
\phi=1
\quad
\text{on }B_1,
$$

and:

$$
\operatorname{supp}\phi
\subset
B_2.
$$

Let:

$$
\chi(s,x)
$$

solve:

$$
\boxed{
\partial_s\chi
+
u\cdot\nabla\chi
+
\Delta\chi
=
0,
\qquad
\chi(t_j)=\chi_j.
}
$$

Assume:

$$
\boxed{
\|u\|_{L_t^\infty L_x^{3,\infty}}
\le
M.
}
$$

---

# 2. Reverse-time footprint dynamics

Set:

$$
\tau=t_j-s,
$$

and:

$$
\rho(\tau,x)
=
\chi(t_j-\tau,x).
$$

Then:

$$
\boxed{
\partial_\tau\rho
=
u(t_j-\tau,x)\cdot\nabla\rho
+
\Delta\rho
=
\nabla\cdot(u\rho)+\Delta\rho.
}
$$

This is the adjoint/provenance dynamics; physical Navier--Stokes causality remains forward in time.

---

# 3. Mass, centroid and aperture

Define:

$$
m
=
\int\rho dx.
$$

Then:

$$
\boxed{
m\asymp_\phi R^3
}
$$

and is constant.

Define:

$$
c(\tau)
=
\frac1m
\int x\rho dx.
$$

Then:

$$
\boxed{
c'(\tau)
=
-
\frac1m
\int u\rho dx.
}
$$

Define:

$$
I(\tau)
=
\int|x-c(\tau)|^2\rho dx,
$$

and:

$$
\boxed{
A(\tau)^2
=
\frac{I(\tau)}{mR^2}.
}
$$

At terminal time:

$$
A(0)\le C_\phi.
$$

---

# 4. CIV-2.1 — Exact aperture evolution

## Theorem 4.1

$$
\boxed{
I'(\tau)
=
-2\int(x-c)\cdot u\rho dx
+
6m.
}
$$

### Proof

Differentiate the centered second moment. The centroid derivative term vanishes because:

$$
\int(x-c)\rho dx=0.
$$

Using:

$$
\partial_\tau\rho
=
\nabla\cdot(u\rho)+\Delta\rho,
$$

integration by parts gives the stated identity.

$\square$

---

# 5. Lorentz interpolation

Let:

$$
f=|x-c|\rho.
$$

Because:

$$
0\le\rho\le1,
$$

$$
\|f\|_1
\le
m^{1/2}I^{1/2},
$$

and:

$$
\|f\|_2
\le
I^{1/2}.
$$

Real interpolation yields:

$$
\boxed{
\|f\|_{L^{3/2,1}}
\le
C
m^{1/6}I^{1/2}.
}
$$

Lorentz Hölder then gives:

$$
\boxed{
\left|
\int(x-c)\cdot u\rho
\right|
\le
CM
m^{1/6}I^{1/2}.
}
$$

Therefore:

$$
\boxed{
I'
\le
CMm^{1/6}I^{1/2}
+
6m.
}
$$

---

# 6. CIV-2.2 — Type-I adjoint aperture theorem

Since:

$$
m\asymp_\phi R^3,
$$

$$
I=mR^2A^2,
$$

we obtain:

$$
\frac{d}{d\tau}A^2
\le
\frac{C_\phi M}{R^2}A
+
\frac{C_\phi}{R^2}.
$$

Using:

$$
A\le1+A^2,
$$

$$
\boxed{
\frac{d}{d\tau}(1+A^2)
\le
\frac{C_\phi(1+M)}{R^2}
(1+A^2).
}
$$

Thus for:

$$
0\le\tau\le\vartheta R^2,
$$

$$
\boxed{
A(\tau)^2
\le
(1+A(0)^2)
\exp
\left(
C_\phi(1+M)\vartheta
\right)
-1.
}
$$

Define:

$$
\boxed{
A_\ast(M,\phi,\vartheta)
}
$$

by the right-hand side.

This closes the aperture quantity left OPEN in ANP-01 on fixed parabolic windows.

$\square$

---

# 7. Footprint mass recapture

For:

$$
K>0,
$$

Chebyshev gives:

$$
\boxed{
\int_{|x-c(\tau)|>KR}\rho dx
\le
\frac{A(\tau)^2}{K^2}m.
}
$$

Hence for every:

$$
\varepsilon>0,
$$

choosing:

$$
K\ge
A_\ast\varepsilon^{-1/2}
$$

gives:

$$
\boxed{
\int_{B(c(\tau),KR)}\rho dx
\ge
(1-\varepsilon)m.
}
$$

ANP-01's centroid estimate gives, for:

$$
\tau\le\vartheta R^2,
$$

$$
|c(\tau)|
\le
C_\phi M\vartheta R.
$$

Therefore:

$$
\boxed{
\int_{
B(0,A_{\rm rec}R)
}
\rho dx
\ge
(1-\varepsilon)m,
}
$$

where:

$$
A_{\rm rec}
=
K+C_\phi M\vartheta.
$$

---

# 8. CIV-2.3 — Same-center footprint recapture

## Theorem 8.1

For fixed:

$$
\vartheta>0,
\qquad
\varepsilon\in(0,1),
$$

there exists:

$$
A_{\rm rec}
=
A_{\rm rec}
(M,\phi,\vartheta,\varepsilon)
<\infty
$$

such that for:

$$
0\le t_j-s\le\vartheta R^2,
$$

$$
\boxed{
\int_{
B(0,A_{\rm rec}R)
}
\chi(s,x)dx
\ge
(1-\varepsilon)
\int\chi_jdx.
}
$$

Thus the terminal-core causal footprint is geometrically recaptured, in mass, by a controlled enlargement of the same singular-center core.

$\square$

---

# 9. Critical-drift calibration

Qian--Xi prove fundamental-solution bounds for parabolic equations with divergence-free drift in critical and supercritical Lebesgue classes; in dimension three the strong critical class:

$$
L_t^\infty L_x^3
$$

admits Gaussian-type fundamental-solution bounds.

ANP-02 does not import that theorem into the weak:

$$
L_t^\infty L_x^{3,\infty}
$$

Type-I setting.

The aperture estimate above is derived directly from the weak-L3 bound.

---

# 10. Footprint localization is not source localization

Theorem 8.1 controls:

$$
\chi dx.
$$

It does not automatically control:

$$
\chi Fdx
$$

for a nonlinear source density:

$$
F.
$$

A small region of footprint mass may carry very large source amplitude.

---

# 11. CIV-2.4 — Footprint/source localization no-go

## Theorem 11.1

There is no universal implication:

$$
\boxed{
\int_{\Omega^c}\chi dx
\ll
\int\chi dx
\Longrightarrow
\int_{\Omega^c}\chi Fdx
\ll
\int\chi Fdx
}
$$

for arbitrary nonnegative:

$$
F.
$$

### Proof

Choose:

$$
F_\varepsilon
$$

supported where:

$$
\chi\le\varepsilon
$$

and scale its amplitude so:

$$
\int\chi F_\varepsilon=1.
$$

The whole weighted source may then lie in a region of arbitrarily small footprint weight.

This is a functional-analytic construction, not a Navier--Stokes source construction.

$\square$

---

# 12. Adjoint propagator

For:

$$
r<s<t<T_\ast,
$$

define:

$$
\mathsf A_{s,t}
$$

as the adjoint map carrying terminal data at:

$$
t
$$

to time:

$$
s.
$$

---

# 13. CIV-2.5 — Adjoint semigroup provenance

## Theorem 13.1

$$
\boxed{
\mathsf A_{r,s}
\mathsf A_{s,t}
=
\mathsf A_{r,t}.
}
$$

### Proof

Both sides solve the same linear adjoint equation on:

$$
[r,s]
$$

with the same terminal data at:

$$
s.
$$

Uniqueness gives equality.

$\square$

---

# 14. Stable provenance identifier

Fix terminal core cutoff:

$$
\chi_j.
$$

Define:

$$
\chi_s
=
\mathsf A_{s,t_j}\chi_j.
$$

Then:

$$
\boxed{
\operatorname{Prov}(\chi_s)
=
\operatorname{Prov}(\chi_j)
}
$$

for every:

$$
s<t_j.
$$

Recursive backward propagation does not reset the branch identity.

---

# 15. Canonical Footprint Node

Define:

$$
\boxed{
\mathsf F(s)
=
(
s,
\chi_s,
\omega(s),
\mathbf e^\chi(s),
\operatorname{Prov}_j
).
}
$$

Here:

$$
\mathbf e^\chi(s)
=
\{
e_k^\chi(s)
\}_{k\in\mathbb Z},
$$

with:

$$
\boxed{
e_k^\chi(s)
=
\frac12
\int
\chi_s
|\omega_k(s)|^2dx.
}
$$

The full vorticity state is retained as the canonical state object.

The weighted dyadic spectrum is a stable derived coordinate.

---

# 16. Shellwise filtered vorticity dynamics

Each block:

$$
\omega_k
=
\Delta_k\omega
$$

satisfies:

$$
\boxed{
\partial_t\omega_k
+
u\cdot\nabla\omega_k
=
\Delta_k(S\omega)
-
[
\Delta_k,u\cdot\nabla
]\omega
+
\Delta\omega_k.
}
$$

---

# 17. CIV-2.6 — Exact shellwise footprint provenance

## Theorem 17.1

For:

$$
t_i<t_j,
$$

$$
\boxed{
e_k^\chi(t_j)
=
e_k^\chi(t_i)
+
\mathcal S_k^{str}
+
\mathcal S_k^{tr}
-
\mathcal D_k,
}
$$

where:

$$
\mathcal S_k^{str}
=
\int_{t_i}^{t_j}
\int
\chi\,
\omega_k\cdot
\Delta_k(S\omega)
\,dx\,ds,
$$

$$
\mathcal S_k^{tr}
=
-
\int_{t_i}^{t_j}
\int
\chi\,
\omega_k\cdot
[
\Delta_k,u\cdot\nabla
]\omega
\,dx\,ds,
$$

and:

$$
\mathcal D_k
=
\int_{t_i}^{t_j}
\int
\chi
|\nabla\omega_k|^2dx\,ds.
$$

$\square$

---

# 18. Monotone square-tail coordinate

Define:

$$
\boxed{
\mathcal E_{>J}^{sq}(s)
=
\sum_{k>J}
e_k^\chi(s).
}
$$

Then:

$$
J'\le J
$$

implies:

$$
\boxed{
\mathcal E_{>J'}^{sq}(s)
\ge
\mathcal E_{>J}^{sq}(s).
}
$$

Thus changing the queried threshold downward does not change the node semantics or provenance.

---

# 19. CIV-2.7 — Footprint Representation Stability

## Theorem 19.1

The canonical Footprint Node class is closed under:

1. adjoint backward propagation;
2. recursive reuse at earlier times;
3. dyadic threshold changes through the stored full spectrum;
4. shellwise source accounting.

Define:

$$
\boxed{
\mathrm{REC\mbox{-}F}
}
$$

as this footprint/state representation recursion property.

Then:

$$
\boxed{
\mathrm{REC\mbox{-}F}
:
\mathrm{PROVED}.
}
$$

$\square$

---

# 20. Hybrid continuity/discreteness

The canonical node stores:

- continuous solution:
  $$
  \omega(s,x);
  $$
- continuous adjoint footprint:
  $$
  \chi_s(x);
  $$
- discrete dyadic profile:
  $$
  \mathbf e^\chi(s).
  $$

Thus the recursive state is hybrid but semantically stable.

No discrete node is interpreted as a physical time jump.

---

# 21. Pseudolocal parent split

Let:

$$
\Delta_k
$$

have Schwartz kernel:

$$
K_k(x)
=
2^{3k}K(2^kx).
$$

For an output region:

$$
B(c,AR)
$$

and:

$$
2^kR\asymp1,
$$

split a parent/source field:

$$
F=F_{\rm near}+F_{\rm far},
$$

where:

$$
F_{\rm near}
=
\mathbf 1_{B(c,(A+B)R)}F.
$$

For every:

$$
N,
$$

the remote contribution obeys:

$$
\boxed{
\|
\Delta_kF_{\rm far}
\|_{L^2(B(c,AR))}
\le
C_N
B^{-N}
\|F_{\rm far}\|_2.
}
$$

This is the band-passed pseudolocal decay used to audit parent provenance.

---

# 22. Parent leakage coordinate

Define:

$$
\boxed{
\mathfrak L_{A,B}^{par}
}
$$

as the fraction of realized weighted source contribution that requires parent/source field outside the controlled enlargement:

$$
B(c,(A+B)R).
$$

The exact formula is channel dependent.

Pseudolocality proves decay with separation.

It does not prove the remote parent norm is itself small.

---

# 23. CIV-2.8 — Geometric parent localization reduction

## Theorem 23.1

At parabolic frequency:

$$
2^kR\asymp1,
$$

source-parent provenance satisfies the structural alternative:

$$
\boxed{
\text{LOCAL-PARENT}
\vee
R_{\rm PLEAK},
}
$$

where:

### LOCAL-PARENT

A quantitatively nontrivial fraction of the realized source is backed by parent/source field in a controlled enlargement of the footprint core.

### $R_{\rm PLEAK}$

Remote parent gross is large enough to survive Schwartz kernel decay.

Thus geometric same-core parent localization is reduced to a pseudolocal leakage problem.

Exclusion of:

$$
R_{\rm PLEAK}
$$

is OPEN.

$\square$

---

# 24. Recursive Edge Compatibility decomposition

Define:

$$
\boxed{
\mathrm{REC}
=
\mathrm{REC\mbox{-}F}
+
\mathrm{REC\mbox{-}S},
}
$$

where:

### REC-F

Footprint/state representation recursion.

Status:

$$
\boxed{
\mathrm{PROVED}.
}
$$

### REC-S

Source-parent recapture into a quantitatively nontrivial reusable state node.

Status:

$$
\boxed{
\mathrm{OPEN}.
}
$$

---

# 25. Causal level update

ANP-01 established a weighted source-core:

$$
C2
$$

edge.

ANP-02 now proves:

- controlled footprint aperture;
- same-center footprint-mass recapture;
- persistent adjoint provenance;
- recursively stable Footprint Node semantics.

Therefore the weighted branch satisfies:

$$
\boxed{
C2+\mathrm{REC\mbox{-}F}.
}
$$

This is a diagnostic tag, not a new ANP-00 causality level.

Full:

$$
C3
$$

still requires:

$$
\boxed{
\mathrm{REC\mbox{-}S}.
}
$$

---

# 26. Current Causal Atom audit

For the recursive Footprint Node edge:

### ST

PASS.

### REL

EVO / SRC / PROV / SCALE.

### EX

- solution: PASS;
- footprint node: PASS;
- weighted edge: PASS;
- recursive footprint chain: PASS;
- source-parent chain: OPEN.

### DEF

Stable Footprint Node.

### JUD

- time: PASS;
- hypotheses: PASS;
- PDE: PASS;
- representation: PASS;
- footprint provenance: PASS;
- parent-source locality: CONDITIONAL/OPEN;
- recursive source-parent legality: OPEN.

### DYN

Exact vorticity plus adjoint dynamics.

### NUM

Includes:

$$
A(\tau),
$$

$$
\mu_{\rm out}(K)
=
\frac1m
\int_{|x-c|>KR}\chi,
$$

$$
\mathfrak L^{par},
$$

and:

$$
\mathbf e^\chi.
$$

---

# 27. Phase-like regimes

The recursive footprint can pass through:

- inherited-state regime;
- stretching-source regime;
- scale-transfer regime;
- local-parent regime;
- parent-leakage regime;
- dissipation-boundary regimes through:
  $$
  J-Q(t).
  $$

All are pre-singularity operational regimes.

---

# 28. Predictability

The aperture theorem yields a P2 conditional forecast:

given a Type-I terminal core and a backward interval:

$$
\tau\le\vartheta R^2,
$$

the admissible adjoint provenance footprint must satisfy:

$$
\boxed{
A(\tau)
\le
A_\ast(M,\vartheta,\phi).
}
$$

This predicts the allowed provenance geometry.

It does not predict blow-up.

---

# 29. Interpretability

ANP-02 now makes the recursive weighted edge interpretable in:

- time;
- same-center footprint region;
- dyadic scale profile;
- state variable;
- exact adjoint/vorticity mechanism;
- aperture and source contribution coordinates;
- provenance legality.

The remaining interpretability gap is explicitly:

$$
\boxed{
\text{which nonlinear parent state inside/outside the footprint actually carries the source?}
}
$$

---

# 30. External calibration

Barker--Prange's localized smoothing/concentration work shows that local-in-space critical control is central near potential singularities.

Qian--Xi prove critical divergence-free drift fundamental-solution estimates in strong critical Lebesgue spaces, including Gaussian-type bounds for:

$$
L_t^\infty L_x^3
$$

in dimension three.

ANP-02's weak-L3 aperture theorem is independent of those stronger heat-kernel hypotheses.

---

# 31. What ANP-02 closes

ANP-01's aperture gap is closed:

$$
\boxed{
\text{adjoint aperture}
:
\mathrm{PROVED}.
}
$$

The representation/provenance part of Recursive Edge Compatibility is closed:

$$
\boxed{
\mathrm{REC\mbox{-}F}
:
\mathrm{PROVED}.
}
$$

Same-center footprint-mass recapture over parabolic windows is proved.

---

# 32. What remains open

The dominant remaining gap is now:

$$
\boxed{
\textbf{Source-Parent Recapture}.
}
$$

Specifically:

1. control or absorb:
   $$
   R_{\rm PLEAK};
   $$
2. extract one or finitely many weighted parent-state carriers;
3. make those parent states recursively legal nodes.

This is:

$$
\boxed{
\mathrm{REC\mbox{-}S}.
}
$$

---

# 33. Next paper

The next paper is:

$$
\boxed{
\textbf{
NS-ANP 03 —
Source-Parent Recapture,
Pseudolocal Leakage,
Weighted Parent-State Extraction
and C3 Causal Upgrade
}.
}
$$

The original non-Type-I entry paper is moved one slot later.

Primary tasks:

1. adapt DRC signed parent ledgers to the adjoint footprint;
2. separate local-parent source from pseudolocal leakage;
3. extract finite weighted parent-state carriers;
4. define source-parent recursive node semantics;
5. prove or isolate the exact obstruction to:
   $$
   C2+\mathrm{REC\mbox{-}F}
   \to
   C3.
   $$

---

# 34. Formal status ledger

$$
\boxed{
\begin{aligned}
\text{adjoint second-moment evolution}
&:\ \mathrm{PROVED},\\
\text{Type-I aperture inequality}
&:\ \mathrm{PROVED},\\
\text{parabolic-window aperture control}
&:\ \mathrm{PROVED},\\
\text{same-center footprint-mass recapture}
&:\ \mathrm{PROVED},\\
\text{source localization from footprint mass alone}
&:\ \mathrm{NO\mbox{-}GO},\\
\text{adjoint semigroup provenance}
&:\ \mathrm{PROVED},\\
\text{canonical Footprint Node}
&:\ \mathrm{DEFINED},\\
\text{exact shellwise footprint provenance}
&:\ \mathrm{PROVED},\\
\text{monotone square-tail representation}
&:\ \mathrm{PROVED},\\
\mathrm{REC\mbox{-}F}
&:\ \mathrm{PROVED},\\
\text{pseudolocal parent-localization reduction}
&:\ \mathrm{PROVED},\\
R_{\rm PLEAK}\text{ exclusion}
&:\ \mathrm{OPEN},\\
\mathrm{REC\mbox{-}S}
&:\ \mathrm{OPEN},\\
\text{full C3 source ancestry edge}
&:\ \mathrm{OPEN},\\
\text{Full Chain Necessity}
&:\ \mathrm{OPEN},\\
\text{Finite Obstruction}
&:\ \mathrm{OPEN},\\
\text{Navier--Stokes regularity}
&:\ \mathrm{NOT\ PROVED}.
\end{aligned}
}
$$

---

# 35. Conclusion

ANP-02 proves that the adjoint causal footprint is not geometrically uncontrolled.

Under the Type-I weak-$L^3$ bound:

$$
\boxed{
A_\chi(\tau)
\le
A_\ast(M,\vartheta)
}
$$

for:

$$
\tau\le\vartheta R^2.
$$

Therefore almost all footprint mass is recaptured in a controlled enlargement of the same singular-center core.

The adjoint semigroup also provides exact recursive provenance:

$$
\boxed{
\mathsf A_{r,s}
\mathsf A_{s,t}
=
\mathsf A_{r,t}.
}
$$

By storing the full weighted dyadic state spectrum, the frequency representation is recursively stable.

Thus the footprint/state component of Recursive Edge Compatibility is closed.

The remaining problem is genuinely nonlinear:

$$
\boxed{
\text{does the source packet's parent state also live in the same causal footprint strongly enough to become the next legal ancestry node?}
}
$$

Pseudolocality reduces failure of that statement to remote parent leakage, but does not exclude it.

That is the exact target of ANP-03.

---

# References

1. T. Barker, C. Prange, *Localized smoothing for the Navier--Stokes equations and concentration of critical norms near singularities*, Archive for Rational Mechanics and Analysis 236 (2020), 1487--1541; arXiv:1812.09115.
2. T. Barker, C. Prange, *Quantitative regularity for the Navier--Stokes equations via spatial concentration*, Communications in Mathematical Physics 385 (2021), 717--792; arXiv:2003.06717.
3. Z. Qian, G. Xi, *Parabolic equations with divergence-free drift in space $L_t^lL_x^q$*, arXiv:1704.02173.
4. E. Miller, *On the interaction of strain and vorticity for solutions of the Navier--Stokes equation*, Pure and Applied Analysis 8 (2026), 247--270; arXiv:2407.02691.
5. `NS_ANP_00_PreSingularity_CausalRelationDomain_v0.1.md`.
6. `NS_ANP_01_SourceCore_Provenance_AdjointTube_v0.1.md`.