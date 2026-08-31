---
title: "Navier–Stokes Coercive Synchronization Program 01：Spatial Concentration Synchronizer、Window Capture、Shell Atomization 與 Wavelength-Cell Dispersion"
short_title: "NS-CSP 01"
series: "Navier–Stokes Coercive Synchronization Program"
cycle: "II"
version: "v0.1"
date: "2026-08-15"
author: "Neo.K / EveMissLab"
language: "zh-TW"
status: "Theorem-style synchronization advance / Cycle-II opening paper"
epistemic_status: "Proves a deterministic wavelength-cell inequality that synchronizes localized dyadic strain L2 mass with the epsilon=1/2 Bradshaw–Grujic frequency-window L-infinity density; combines it with Cycle-I ultraviolet middle-strain intermittency to obtain a rigorous window/shell/space synchronization alternative. It quantifies shell atomization and spatial dispersion as multiplicity defects. It does NOT prove that Navier–Stokes singularity formation avoids these defects, does NOT prove Type-I concentration implies wavelength-cell strain concentration, and does NOT prove Navier–Stokes regularity."
canonical_source: "UTF-8 Markdown"
---

# Navier–Stokes Coercive Synchronization Program 01

# Spatial Concentration Synchronizer、Window Capture、Shell Atomization 與 Wavelength-Cell Dispersion

## 0. Cycle-II launch point

Cycle I ended with the **Coercive Synchronization Problem**.

A hypothetical finite-time singularity must make several standard-PDE coercive actions diverge, including:

$$
\mathcal A_{mid}
=
\int_0^{T_\ast}
\|\lambda_2^+(t)\|_2^4dt,
$$

and the Bradshaw--Grujic moving frequency-window action:

$$
\mathcal A_{freq,\epsilon}
=
\int_0^{T_\ast}
\Phi_\epsilon(t)^{2/(1-\epsilon)}dt,
$$

where:

$$
\Phi_\epsilon(t)
=
\sup_{
J_{low}(t)
\le j\le
J_{high}(t)
}
2^{-\epsilon j}
\|\Delta_j u(t)\|_\infty.
$$

Cycle I proved:

$$
\boxed{
\text{middle-strain critical action is temporally intermittent}
}
$$

and:

$$
\boxed{
\text{its high-amplitude spikes force strain energy beyond every fixed Fourier cutoff}.
}
$$

But it also proved a no-go:

$$
\boxed{
\text{fixed-frequency }L^2
\not\Rightarrow
L^\infty
}
$$

on:

$$
\mathbb R^3
$$

without spatial concentration.

The purpose of this paper is to insert the missing object:

$$
\boxed{
\textbf{wavelength-scale spatial concentration}.
}
$$

---

# 1. Normalized viscosity convention

For the synchronization estimates we use unit viscosity:

$$
\nu=1.
$$

The purely spatial inequalities below do not depend on this normalization.

The standard Navier--Stokes scaling is:

$$
u_\lambda(x,t)
=
\lambda
u(\lambda x,\lambda^2t).
$$

---

# 2. Dyadic velocity and strain

Let:

$$
u_j
=
\Delta_j u,
$$

and:

$$
S
=
\nabla_{sym}u.
$$

Since Littlewood--Paley projection commutes with constant-coefficient differentiation:

$$
\boxed{
S_j
=
\Delta_jS
=
\nabla_{sym}u_j.
}
$$

---

# 3. Band Bernstein estimate

For a standard dyadic annular multiplier:

$$
\boxed{
\|S_j\|_\infty
\le
C_\Delta
2^j
\|u_j\|_\infty.
}
$$

Therefore:

$$
\boxed{
\|u_j\|_\infty
\ge
C_\Delta^{-1}
2^{-j}
\|S_j\|_\infty.
}
$$

---

# 4. Local finite-volume lower bound

For every measurable set:

$$
E\subset\mathbb R^3
$$

with finite positive volume:

$$
\boxed{
\|S_j\|_\infty
\ge
|E|^{-1/2}
\|S_j\|_{L^2(E)}.
}
$$

For a ball:

$$
B(x,R),
$$

this gives:

$$
\boxed{
\|S_j\|_\infty
\ge
c
R^{-3/2}
\|S_j\|_{L^2(B(x,R))}.
}
$$

---

# 5. CII-1.1 — Spatial Concentration Synchronizer

## Theorem 5.1

For every dyadic shell:

$$
j,
$$

every:

$$
x\in\mathbb R^3,
$$

every:

$$
R>0,
$$

and every:

$$
0<\epsilon<1,
$$

one has:

$$
\boxed{
2^{-\epsilon j}
\|u_j\|_\infty
\ge
c
2^{-(1+\epsilon)j}
R^{-3/2}
\|S_j\|_{L^2(B(x,R))}.
}
$$

### Proof

Combine Sections 3 and 4:

$$
\begin{aligned}
2^{-\epsilon j}\|u_j\|_\infty
&\ge
C_\Delta^{-1}
2^{-(1+\epsilon)j}
\|S_j\|_\infty
\\
&\ge
c
2^{-(1+\epsilon)j}
R^{-3/2}
\|S_j\|_{L^2(B(x,R))}.
\end{aligned}
$$

$\square$

---

# 6. Wavelength-sized cell

Let:

$$
\boxed{
R
=
A2^{-j},
\qquad
A\ge1.
}
$$

Then Theorem 5.1 becomes:

$$
\boxed{
2^{-\epsilon j}
\|u_j\|_\infty
\ge
c
A^{-3/2}
2^{(1/2-\epsilon)j}
\|S_j\|_{L^2(B(x,A2^{-j}))}.
}
$$

---

# 7. Why $\epsilon=1/2$ is canonical

Take:

$$
\boxed{
\epsilon=\frac12.
}
$$

The residual dyadic scale factor disappears:

$$
\boxed{
2^{-j/2}
\|u_j\|_\infty
\ge
c
A^{-3/2}
\|S_j\|_{L^2(B(x,A2^{-j}))}.
}
$$

This is the key synchronization identity of the paper.

It compares:

- the exact instantaneous density used in the:
  $$
  \epsilon=\frac12
  $$
  Bradshaw--Grujic action;
- wavelength-cell strain:
  $$
  L^2
  $$
  mass.

No temporal persistence assumption is required.

---

# 8. Critical action exponent at $\epsilon=1/2$

For:

$$
\epsilon=\frac12,
$$

the frequency-window exponent is:

$$
\boxed{
\frac{2}{1-\epsilon}
=
4.
}
$$

Hence:

$$
\boxed{
\Phi_{1/2}(t)^4
}
$$

has the same temporal exponent as:

$$
\boxed{
\|\lambda_2^+(t)\|_2^4.
}
$$

This exact exponent match is the reason:

$$
\epsilon=\frac12
$$

is the natural first synchronization slice.

---

# 9. Middle-strain action density

Define:

$$
\boxed{
g(t)
=
\|\lambda_2^+(t)\|_2^2.
}
$$

Then:

$$
\boxed{
\text{middle-strain critical density}
=
g(t)^2.
}
$$

Cycle I proved, under hypothetical finite blow-up:

$$
g\in
L^1(0,T_\ast)
\setminus
L^2(0,T_\ast).
$$

For every:

$$
M>0,
$$

the spike set:

$$
E_M
=
\{
t:
g(t)>M
\}
$$

satisfies:

$$
\boxed{
\int_{E_M}
g(t)^2dt
=
\infty.
}
$$

---

# 10. Cycle-I UV strain input

For every fixed Fourier cutoff:

$$
\Lambda<\infty,
$$

Cycle I proved that for sufficiently high:

$$
M_\Lambda,
$$

the set:

$$
E_{M_\Lambda}
$$

satisfies:

$$
\boxed{
\int_{E_{M_\Lambda}}
\|
\Pi_{>\Lambda}S(t)
\|_2^4dt
=
\infty,
}
$$

and pointwise on this spike set:

$$
\boxed{
\|
\Pi_{>\Lambda}S(t)
\|_2^2
\ge
\frac12
g(t).
}
$$

---

# 11. Dyadic UV strain energy

Fix:

$$
J_\Lambda
$$

corresponding to:

$$
2^{J_\Lambda}
\sim
\Lambda.
$$

Define:

$$
\boxed{
\mathcal E_{UV}(t)
=
\sum_{j>J_\Lambda}
\|S_j(t)\|_2^2.
}
$$

Standard Littlewood--Paley:

$$
L^2
$$

equivalence gives:

$$
\boxed{
\mathcal E_{UV}(t)
\ge
c_\Delta
\|
\Pi_{>\Lambda'}S(t)
\|_2^2
}
$$

for a harmless nearby cutoff:

$$
\Lambda'\sim\Lambda.
$$

Therefore on sufficiently high middle-strain spikes:

$$
\boxed{
\mathcal E_{UV}(t)
\ge
c_0g(t).
}
$$

---

# 12. Bradshaw--Grujic relevant window

For:

$$
\epsilon=\frac12,
$$

let:

$$
\boxed{
\mathcal W(t)
=
\{
j:
J_{low}(t)
\le
j
\le
J_{high}(t)
\}.
}
$$

This is the finite moving LP window appearing in the external frequency-localized regularity theorem.

Define its UV intersection:

$$
\boxed{
\mathcal W_{UV}(t)
=
\mathcal W(t)
\cap
\{
j>J_\Lambda
\}.
}
$$

---

# 13. Window-capture ratio

Define:

$$
\boxed{
c_{win}(t)
=
\frac{
\sum_{j\in\mathcal W_{UV}(t)}
\|S_j(t)\|_2^2
}{
\mathcal E_{UV}(t)
}.
}
$$

If:

$$
\mathcal E_{UV}(t)>0,
$$

then:

$$
0\le c_{win}(t)\le1.
$$

This measures how much of the UV strain energy is actually visible to the standard-PDE relevant frequency window.

---

# 14. Window mismatch

If:

$$
c_{win}(t)\ll1,
$$

then most UV middle-strain energy lies outside the finite moving window used by the Bradshaw--Grujic action.

This is a genuine synchronization defect:

$$
\boxed{
\textbf{window mismatch}.
}
$$

It is not a contradiction.

---

# 15. Shell weights inside the window

If:

$$
c_{win}(t)>0,
$$

define:

$$
\boxed{
p_j^{sh}(t)
=
\frac{
\|S_j(t)\|_2^2
}{
\sum_{k\in\mathcal W_{UV}(t)}
\|S_k(t)\|_2^2
},
\qquad
j\in\mathcal W_{UV}(t).
}
$$

Then:

$$
\sum_jp_j^{sh}=1.
$$

Define the shell atom:

$$
\boxed{
a_{sh}(t)
=
\max_{
j\in\mathcal W_{UV}(t)
}
p_j^{sh}(t).
}
$$

The maximum exists because the window is finite.

---

# 16. Shell atomization

If:

$$
a_{sh}(t)
$$

is small,

the relevant-window strain energy is spread over many shells.

Define the inverse atom:

$$
\boxed{
\mathfrak M_{sh}(t)
=
\frac1{a_{sh}(t)}.
}
$$

This is an effective shell multiplicity.

---

# 17. CII-1.2 — Shell Multiplicity Debt

## Theorem 17.1

If:

$$
a_{sh}(t)\le\eta,
$$

then at least:

$$
\boxed{
\frac1{2\eta}
}
$$

dyadic shells are required to carry half of the relevant-window strain energy.

### Proof

Every shell carries at most:

$$
\eta
$$

of the normalized mass.

Any collection of:

$$
N
$$

shells carries at most:

$$
N\eta.
$$

To reach:

$$
1/2
$$

one needs:

$$
N\eta\ge1/2.
$$

$\square$

---

# 18. Wavelength-cell partition

Fix:

$$
A\ge1.
$$

For each:

$$
j,
$$

partition:

$$
\mathbb R^3
$$

into disjoint cubes:

$$
\{
Q_{j,m}^{A}
\}_{m\in\mathbb Z^3}
$$

with side length:

$$
\boxed{
A2^{-j}.
}
$$

---

# 19. Spatial weights

For a nonzero shell:

$$
S_j,
$$

define:

$$
\boxed{
p_{j,m}^{sp}(t)
=
\frac{
\|S_j(t)\|_{L^2(Q_{j,m}^A)}^2
}{
\|S_j(t)\|_2^2
}.
}
$$

Then:

$$
\sum_mp_{j,m}^{sp}=1.
$$

Define spatial atom:

$$
\boxed{
a_{sp}(j,t)
=
\sup_m
p_{j,m}^{sp}(t).
}
$$

---

# 20. Spatial dispersion

Small:

$$
a_{sp}(j,t)
$$

means the shell energy is dispersed among many wavelength-sized cells.

Define:

$$
\boxed{
\mathfrak M_{sp}(j,t)
=
\frac1{
a_{sp}(j,t)
}.
}
$$

---

# 21. CII-1.3 — Wavelength-Cell Multiplicity Debt

## Theorem 21.1

If:

$$
a_{sp}(j,t)\le\sigma,
$$

then at least:

$$
\boxed{
\frac1{2\sigma}
}
$$

wavelength cells are required to carry half of the shell:

$$
L^2
$$

energy.

### Proof

Identical to Theorem 17.1 using the spatial probability weights. $\square$

---

# 22. Canonical carrier shell

Whenever:

$$
c_{win}(t)>0,
$$

choose:

$$
\boxed{
j_\star(t)
\in
\mathcal W_{UV}(t)
}
$$

such that:

$$
p_{j_\star}^{sh}(t)
=
a_{sh}(t).
$$

This is the strongest strain shell inside the relevant moving window.

---

# 23. Good synchronization set

Fix thresholds:

$$
0<\chi,\eta,\sigma<1.
$$

Define:

$$
\boxed{
\mathcal G_M(\chi,\eta,\sigma)
}
$$

as the set of:

$$
t\in E_M
$$

such that:

$$
c_{win}(t)\ge\chi,
$$

$$
a_{sh}(t)\ge\eta,
$$

and:

$$
a_{sp}(j_\star(t),t)>\sigma.
$$

For each such time choose one wavelength cell:

$$
Q_\star(t)
$$

satisfying:

$$
\boxed{
\|S_{j_\star}(t)\|_{L^2(Q_\star)}^2
\ge
\sigma
\|S_{j_\star}(t)\|_2^2.
}
$$

---

# 24. Local strain mass on the good set

On:

$$
\mathcal G_M(\chi,\eta,\sigma),
$$

we have:

$$
\begin{aligned}
\|S_{j_\star}\|_{L^2(Q_\star)}^2
&\ge
\sigma
\|S_{j_\star}\|_2^2
\\
&\ge
\sigma\eta
\sum_{j\in\mathcal W_{UV}}
\|S_j\|_2^2
\\
&\ge
\sigma\eta\chi
\mathcal E_{UV}.
\end{aligned}
$$

For sufficiently high middle-strain spike threshold:

$$
M,
$$

Section 11 gives:

$$
\boxed{
\|S_{j_\star}\|_{L^2(Q_\star)}^2
\ge
c_0
\chi\eta\sigma
g(t).
}
$$

---

# 25. CII-1.4 — Same-Time Coercive Synchronizer

## Theorem 25.1

On:

$$
\mathcal G_M(\chi,\eta,\sigma),
$$

for sufficiently high:

$$
M,
$$

one has:

$$
\boxed{
\Phi_{1/2}(t)^4
\ge
c
A^{-6}
\chi^2
\eta^2
\sigma^2
g(t)^2.
}
$$

### Proof

Since:

$$
j_\star(t)
\in
\mathcal W(t),
$$

the frequency-window supremum obeys:

$$
\Phi_{1/2}(t)
\ge
2^{-j_\star/2}
\|u_{j_\star}(t)\|_\infty.
$$

Theorem 7 gives:

$$
2^{-j_\star/2}
\|u_{j_\star}\|_\infty
\ge
c
A^{-3/2}
\|S_{j_\star}\|_{L^2(Q_\star)}.
$$

Section 24 gives:

$$
\|S_{j_\star}\|_{L^2(Q_\star)}^2
\ge
c_0
\chi\eta\sigma
g(t).
$$

Raise to the fourth power. $\square$

---

# 26. Why this theorem matters

Theorem 25.1 is not merely:

$$
\mathcal A_{mid}=\infty
\Longrightarrow
\mathcal A_{freq}=\infty.
$$

That implication was already known separately from external regularity theorems.

The new statement is pointwise-in-time:

$$
\boxed{
\text{middle-strain spike}
+
\text{window capture}
+
\text{shell concentration}
+
\text{spatial concentration}
}
$$

forces:

$$
\boxed{
\text{frequency-window action density at the same time}.
}
$$

This is a genuine synchronization bridge.

---

# 27. Synchronization defects

Define three defect sets inside:

$$
E_M.
$$

## D-WIN — Window mismatch

$$
\boxed{
\mathcal D_{win}
=
\{
t:
c_{win}(t)<\chi
\}.
}
$$

## D-SHELL — Shell atomization

$$
\boxed{
\mathcal D_{sh}
=
\{
t:
c_{win}\ge\chi,
\;
a_{sh}<\eta
\}.
}
$$

## D-SPACE — Wavelength-cell dispersion

$$
\boxed{
\mathcal D_{sp}
=
\{
t:
c_{win}\ge\chi,
\;
a_{sh}\ge\eta,
\;
a_{sp}(j_\star,t)\le\sigma
\}.
}
$$

The complement is:

$$
\mathcal G_M(\chi,\eta,\sigma).
$$

---

# 28. CII-1.5 — Synchronization Alternative

## Theorem 28.1

For every fixed:

$$
0<\chi,\eta,\sigma<1,
$$

and sufficiently high:

$$
M,
$$

at least one of the following occurs:

### SYNC

$$
\boxed{
\int_{\mathcal G_M}
g(t)^2dt
=
\infty.
}
$$

Then:

$$
\boxed{
\int_{\mathcal G_M}
\Phi_{1/2}(t)^4dt
=
\infty.
}
$$

So the middle-strain and frequency-window actions synchronize on the same time set.

### DEF-WIN

$$
\boxed{
\int_{\mathcal D_{win}}
g(t)^2dt
=
\infty.
}
$$

### DEF-SHELL

$$
\boxed{
\int_{\mathcal D_{sh}}
g(t)^2dt
=
\infty.
}
$$

### DEF-SPACE

$$
\boxed{
\int_{\mathcal D_{sp}}
g(t)^2dt
=
\infty.
}
$$

### Proof

The four sets partition:

$$
E_M.
$$

Cycle I gives:

$$
\int_{E_M}g^2=\infty.
$$

If the good set carries infinite action, Theorem 25.1 gives SYNC.

Otherwise the finite union of defect sets must contain at least one set carrying infinite:

$$
g^2
$$

action. $\square$

---

# 29. This is the first Cycle-II enclosure

The Coercive Synchronization Problem is therefore reduced to:

$$
\boxed{
\text{same-time synchronization}
}
$$

or one of only three defects:

$$
\boxed{
\text{window mismatch}
\vee
\text{shell atomization}
\vee
\text{spatial dispersion}.
}
$$

This is substantially narrower than the Cycle-I no-go:

$$
L^2
\not\Rightarrow
L^\infty.
$$

---

# 30. Quantitative meaning of DEF-SHELL

On:

$$
\mathcal D_{sh},
$$

at least:

$$
\frac1{2\eta}
$$

relevant-window shells are required to carry half the window strain energy.

Thus avoiding synchronization by shell spreading incurs:

$$
\boxed{
\text{frequency multiplicity}.
}
$$

---

# 31. Quantitative meaning of DEF-SPACE

On:

$$
\mathcal D_{sp},
$$

at least:

$$
\frac1{2\sigma}
$$

wavelength cells are needed to carry half of the selected shell energy.

Thus avoiding synchronization by physical dispersion incurs:

$$
\boxed{
\text{spatial multiplicity}.
}
$$

This is exactly the mechanism missing from the Cycle-I fixed-annulus translate counterexample.

---

# 32. Quantitative meaning of DEF-WIN

On:

$$
\mathcal D_{win},
$$

at least:

$$
1-\chi
$$

of the UV strain energy lies outside the Bradshaw--Grujic relevant moving window:

$$
\boxed{
\sum_{
j>J_\Lambda,
\;
j\notin\mathcal W(t)
}
\|S_j\|_2^2
>
(1-\chi)
\mathcal E_{UV}(t).
}
$$

Hence window mismatch is not an abstract label.

It is a measurable failure of the standard regularity window to capture the middle-strain UV action.

---

# 33. Persistent synchronization failure

Suppose there are no fixed:

$$
\chi,\eta,\sigma>0
$$

for which SYNC occurs.

Then for every such triple, some defect carries infinite middle-strain critical action.

The next mathematical problem becomes:

$$
\boxed{
\text{can true N--S dynamics sustain infinite critical action entirely through these defects?}
}
$$

---

# 34. Spatial multiplicity as an inverse concentration scale

Define:

$$
\boxed{
\mathfrak M_{sp}(j,t)
=
a_{sp}(j,t)^{-1}.
}
$$

If:

$$
\mathfrak M_{sp}\gg1,
$$

a single dyadic shell is physically spread over many wavelength cells.

This is distinct from spectral dispersion:

$$
D_{eig}(S).
$$

One is:

$$
\boxed{
\text{physical-space multiplicity},
}
$$

the other:

$$
\boxed{
\text{Fourier-radius dispersion}.
}
$$

They must not be conflated.

---

# 35. Shell multiplicity is not spectral variance

Similarly:

$$
\mathfrak M_{sh}\gg1
$$

means energy is spread over many dyadic labels inside the moving window.

This does not automatically imply large:

$$
D_{eig}(S),
$$

because many active shells may occupy a bounded logarithmic range.

So Cycle II should not silently identify:

$$
\boxed{
\text{dyadic multiplicity}
}
$$

with:

$$
\boxed{
\text{Laplacian-eigenfunction residual}.
}
$$

---

# 36. Type-I spatial concentration interface

Barker--Prange prove, under a Type-I blow-up hypothesis, that if:

$$
(0,T_\ast)
$$

is singular then there is universal critical:

$$
L^3
$$

velocity concentration on balls of radius:

$$
\boxed{
R
=
O(
\sqrt{T_\ast-t}
).
}
$$

This confirms that spatial concentration on shrinking parabolic scales is a genuine part of standard N--S singularity theory.

However:

$$
\boxed{
\text{local }L^3\text{ velocity concentration}
}
$$

does not by itself prove:

$$
\boxed{
a_{sp}(j_\star,t)\ge\sigma
}
$$

for a dyadic strain shell at wavelength:

$$
2^{-j_\star}.
$$

That bridge remains OPEN.

---

# 37. Quantitative spatial-concentration interface

Barker--Prange's later quantitative concentration work develops quantitative local concentration / regularity technology, including Type-I concentration estimates and backward propagation tools.

Again, this provides a standard-PDE concentration interface.

But Cycle II does not import:

$$
\boxed{
\text{velocity concentration}
\Rightarrow
\text{wavelength strain-shell concentration}
}
$$

without proof.

---

# 38. Tao frequency propagation interface

Tao's quantitative critical:

$$
L^3
$$

analysis develops quantitative frequency-localized propagation and concentration estimates from pointwise frequency activity.

This supports the reverse direction:

$$
\boxed{
\text{frequency activity}
\to
\text{spacetime concentration / propagation}.
}
$$

CSP-01 studies the missing converse-type synchronization:

$$
\boxed{
\text{localized strain energy}
\to
\text{frequency-window activity}.
}
$$

---

# 39. New synchronization guards

Add:

### $G_{\rm WINCAP}$

UV middle-strain energy must record what fraction lies inside the standard moving frequency window.

### $G_{\rm SHATOM}$

window energy must record shell atomization / multiplicity.

### $G_{\rm SPATOM}$

selected shell must record wavelength-cell spatial atomization / multiplicity.

### $G_{\rm EPSHALF}$

the exact scale-free strain-to-frequency synchronizer in this paper uses:

$$
\epsilon=\frac12;
$$

other exponents carry an additional scale factor and must be audited separately.

### $G_{\rm CONCINT}$

Type-I local velocity concentration must not be silently promoted to dyadic strain-shell concentration.

---

# 40. Synchronization defect vector

Define:

$$
\boxed{
\mathbf D_{sync}(t)
=
\left(
c_{win}(t),
a_{sh}(t),
a_{sp}(j_\star(t),t)
\right).
}
$$

This is not a new blow-up score.

It records the three exact places where Cycle-I middle/frequency action synchronization can fail.

---

# 41. Cycle-II immediate frontier

Theorem 28.1 gives three branches.

The next paper should first attack the branch most directly tied to real spatial geometry:

$$
\boxed{
\textbf{DEF-SPACE}.
}
$$

Why?

Because:

- Cycle I already proved UV middle-strain intermittency;
- Bradshaw--Grujic already supplies the relevant finite frequency window;
- shell atomization is primarily Fourier combinatorics;
- spatial dispersion is exactly the missing ingredient exposed by the fixed-annulus translate no-go;
- Barker--Prange concentration theory provides a natural external PDE interface.

---

# 42. Next paper

$$
\boxed{
\textbf{
NS-CSP 02 —
Spatial Multiplicity、
Concentration Radius、
Local Smoothing Contrapositives
與 Strain-Shell Core Extraction
}.
}
$$

Primary tasks:

1. convert:
   $$
   a_{sp}\to0
   $$
   into a quantitative spatial multiplicity / radius statement;
2. compare wavelength-cell multiplicity with:
   $$
   R\sim\sqrt{T_\ast-t};
   $$
3. use localized smoothing contrapositive to test whether extreme spatial dispersion is compatible with singularity;
4. seek a local:
   $$
   L^3
   \to
   \text{dyadic strain-shell}
   $$
   extraction lemma;
5. classify the residual alternative as spatial fragmentation versus coherent concentration.

---

# 43. Formal status ledger

$$
\boxed{
\begin{aligned}
\text{spatial concentration synchronizer}
&:\ \mathrm{PROVED},\\
\epsilon=\frac12\text{ scale cancellation}
&:\ \mathrm{PROVED},\\
\text{window-capture ratio}
&:\ \mathrm{DEFINED},\\
\text{shell multiplicity debt}
&:\ \mathrm{PROVED},\\
\text{wavelength-cell multiplicity debt}
&:\ \mathrm{PROVED},\\
\text{same-time coercive synchronizer}
&:\ \mathrm{PROVED},\\
\text{synchronization alternative}
&:\ \mathrm{PROVED},\\
\text{Type-I local }L^3\text{ concentration}
&:\ \mathrm{EXTERNAL},\\
\text{Type-I concentration}
\Rightarrow
\text{dyadic strain-cell concentration}
&:\ \mathrm{OPEN},\\
\text{window mismatch exclusion}
&:\ \mathrm{OPEN},\\
\text{shell atomization exclusion}
&:\ \mathrm{OPEN},\\
\text{spatial dispersion exclusion}
&:\ \mathrm{OPEN},\\
\text{Coercive Synchronization Problem}
&:\ \mathrm{OPEN},\\
\text{Navier--Stokes regularity}
&:\ \mathrm{NOT\ PROVED}.
\end{aligned}
}
$$

---

# 44. Conclusion

Cycle I ended with:

$$
\boxed{
\text{UV }L^2\text{ strain}
\not\Rightarrow
\text{moving-window }L^\infty
}
$$

without spatial concentration.

CSP-01 inserts exactly that missing variable.

For a wavelength cell:

$$
R=A2^{-j},
$$

the choice:

$$
\epsilon=\frac12
$$

gives:

$$
\boxed{
2^{-j/2}
\|\Delta_ju\|_\infty
\gtrsim
A^{-3/2}
\|\Delta_jS\|_{L^2(B_R)}.
}
$$

Therefore whenever a middle-strain UV spike:

1. is substantially captured by the relevant moving frequency window;
2. is not atomized over too many dyadic shells;
3. is not dispersed over too many wavelength cells;

the middle-strain and frequency-window action densities collide at the same time:

$$
\boxed{
\Phi_{1/2}^4
\gtrsim
\chi^2
\eta^2
\sigma^2
g^2.
}
$$

Hence the Cycle-I synchronization gap reduces to only three defects:

$$
\boxed{
\text{window mismatch}
\vee
\text{shell atomization}
\vee
\text{spatial dispersion}.
}
$$

This is the first theorem-level compression of the Coercive Synchronization Problem.

The next target is spatial dispersion.

---

# References

1. Z. Bradshaw, Z. Grujic, *Frequency localized regularity criteria for the 3D Navier–Stokes equations*, Archive for Rational Mechanics and Analysis 224 (2017), 125–133; arXiv:1501.01043v2.
2. T. Barker, C. Prange, *Localized smoothing for the Navier–Stokes equations and concentration of critical norms near singularities*, Archive for Rational Mechanics and Analysis 236 (2020), 1487–1541; arXiv:1812.09115v2.
3. T. Barker, C. Prange, *Quantitative regularity for the Navier–Stokes equations via spatial concentration*, Communications in Mathematical Physics 385 (2021), 717–792; arXiv:2003.06717.
4. T. Tao, *Quantitative bounds for critically bounded solutions to the Navier–Stokes equations*, arXiv:1908.04958v2.
5. E. Miller, *A regularity criterion for the Navier–Stokes equation involving only the middle eigenvalue of the strain tensor*, Archive for Rational Mechanics and Analysis 235 (2020), 99–139; arXiv:1710.05569.
6. `NS_RFP_12_DangerousCore_Realizability_StandardPDE_v0.1.md`.
7. `NS_RFP_CYCLE_I_STANDARD_PDE_RECOMPILATION_v1.0.md`.
