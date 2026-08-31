---
title: "Navier–Stokes Coercive Synchronization Program 02：Spatial-Atom Equivalence、Type-I Enstrophy-Core UV Extraction 與 Parabolic Packing"
short_title: "NS-CSP 02"
series: "Navier–Stokes Coercive Synchronization Program"
cycle: "II"
version: "v0.1"
date: "2026-08-15"
author: "Neo.K / EveMissLab"
language: "zh-TW"
status: "Theorem-style spatial-defect compression / Type-I core synchronization"
epistemic_status: "Proves a two-sided equivalence between wavelength-cell vorticity atomization and scaled dyadic velocity L-infinity amplitude, proves a Type-I singular-core ultraviolet vorticity extraction theorem from Barker–Prange enstrophy concentration and Lorentz–Bernstein bounds, derives parabolic packing inequalities, and reduces Type-I spatial synchronization failure to core-window mismatch, core-shell atomization, or super-parabolic micro-packing. It does NOT prove these defects impossible, does NOT identify the core vorticity carrier with the middle-strain carrier, and does NOT prove Navier–Stokes regularity."
canonical_source: "UTF-8 Markdown"
---

# Navier–Stokes Coercive Synchronization Program 02

# Spatial-Atom Equivalence、Type-I Enstrophy-Core UV Extraction 與 Parabolic Packing

## 0. 本文定位

CSP-01 proved a same-time synchronization statement of the form:

$$
\boxed{
\Phi_{1/2}(t)^4
\gtrsim
\chi^2
\eta^2
\sigma^2
g(t)^2
}
$$

whenever a middle-strain UV spike simultaneously has:

1. moving-window capture;
2. a non-atomized dyadic carrier shell;
3. wavelength-cell spatial concentration.

The residual synchronization defects were:

$$
\boxed{
D_{\rm win}
\vee
D_{\rm shell}
\vee
D_{\rm space}.
}
$$

The present paper attacks:

$$
\boxed{
D_{\rm space}.
}
$$

The first result identifies spatial atomization as the exact fixed-shell mechanism behind the Cycle-I:

$$
L^2
\not\Rightarrow
L^\infty
$$

no-go.

The second result connects this deterministic geometry to a genuine standard-PDE singular core in the Type-I setting.

---

# 1. Vorticity formulation

Let:

$$
\omega
=
\nabla\times u.
$$

For a dyadic velocity shell:

$$
u_j=\Delta_ju,
$$

define:

$$
\omega_j
=
\Delta_j\omega
=
\nabla\times u_j.
$$

For divergence-free:

$$
u_j,
$$

we have the exact vector identity:

$$
-\Delta u_j
=
\nabla\times\omega_j.
$$

Hence:

$$
\boxed{
u_j
=
(-\Delta)^{-1}
\nabla\times\omega_j.
}
$$

On one annulus this is an order:

$$
-1
$$

smooth Fourier multiplier.

---

# 2. Global shell strain--vorticity identity

For every divergence-free dyadic block:

$$
u_j,
$$

$$
\boxed{
\|\omega_j\|_2^2
=
\|\nabla u_j\|_2^2
=
2
\|S_j\|_2^2.
}
$$

Thus the global shell carrier selected using strain energy is equivalent, up to a fixed factor, to the same shell selected using vorticity energy.

Local spatial distributions need not coincide pointwise.

---

# 3. Wavelength-cell partition

Fix:

$$
A\ge1.
$$

For shell:

$$
j,
$$

partition:

$$
\mathbb R^3
$$

into disjoint cubes:

$$
\mathcal Q_j^A
=
\{
Q_{j,m}^A
\}_{m\in\mathbb Z^3}
$$

with side length:

$$
\boxed{
\ell_j
=
A2^{-j}.
}
$$

---

# 4. Vorticity spatial atom

For:

$$
\omega_j\neq0,
$$

define:

$$
\boxed{
a_{\omega}^{A}(j,t)
=
\sup_{
Q\in\mathcal Q_j^A
}
\frac{
\|\omega_j(t)\|_{L^2(Q)}^2
}{
\|\omega_j(t)\|_2^2
}.
}
$$

Thus:

$$
0<
a_{\omega}^{A}(j,t)
\le1.
$$

Define spatial multiplicity:

$$
\boxed{
\mathfrak M_{\omega}^{A}(j,t)
=
\frac1{
a_{\omega}^{A}(j,t)
}.
}
$$

---

# 5. Lower atom-to-amplitude estimate

Band Bernstein gives:

$$
\boxed{
\|\omega_j\|_\infty
\le
C_\Delta
2^j
\|u_j\|_\infty.
}
$$

For every cell:

$$
Q
$$

of volume:

$$
A^3 2^{-3j},
$$

$$
\|\omega_j\|_\infty
\ge
A^{-3/2}
2^{3j/2}
\|\omega_j\|_{L^2(Q)}.
$$

Taking cells approaching the spatial atom gives:

$$
\boxed{
2^{-j/2}
\|u_j\|_\infty
\ge
c
A^{-3/2}
\left(
a_{\omega}^{A}(j,t)
\right)^{1/2}
\|\omega_j\|_2.
}
$$

---

# 6. Band inverse kernel

Let:

$$
\widetilde\Delta_j
$$

be a smooth annular multiplier equal to:

$$
1
$$

on the Fourier support of:

$$
\Delta_j.
$$

Using:

$$
u_j
=
(-\Delta)^{-1}
\nabla\times\omega_j,
$$

write:

$$
\boxed{
u_j
=
K_j*\omega_j,
}
$$

where:

$$
K_j(x)
=
2^{2j}K(2^jx)
$$

for a Schwartz matrix kernel:

$$
K.
$$

---

# 7. Cellwise kernel summation

For fixed:

$$
x,
$$

$$
\begin{aligned}
|u_j(x)|
&\le
\sum_{
Q\in\mathcal Q_j^A
}
\|K_j(x-\cdot)\|_{L^2(Q)}
\|\omega_j\|_{L^2(Q)}
\\
&\le
\left(
a_{\omega}^{A}
\right)^{1/2}
\|\omega_j\|_2
\sum_Q
\|K_j(x-\cdot)\|_{L^2(Q)}.
\end{aligned}
$$

By scaling and Schwartz decay:

$$
\boxed{
\sup_{j,x}
2^{-j/2}
\sum_Q
\|K_j(x-\cdot)\|_{L^2(Q)}
\le
C_A
<
\infty.
}
$$

---

# 8. CII-2.1 — Spatial-Atom Equivalence Theorem

## Theorem 8.1

For every fixed:

$$
A\ge1,
$$

there exist:

$$
0<c_A\le C_A<\infty
$$

such that every nonzero divergence-free dyadic block satisfies:

$$
\boxed{
c_A
\left(
a_{\omega}^{A}(j,t)
\right)^{1/2}
\|\omega_j(t)\|_2
\le
2^{-j/2}
\|u_j(t)\|_\infty
\le
C_A
\left(
a_{\omega}^{A}(j,t)
\right)^{1/2}
\|\omega_j(t)\|_2.
}
$$

One may take the lower constant with explicit dependence:

$$
c_A
\gtrsim
A^{-3/2}.
$$

### Proof

The lower bound is Section 5.

The upper bound is Sections 6--7. $\square$

---

# 9. Meaning of Theorem 8.1

At a fixed annular shell:

$$
j,
$$

the gap between:

$$
\boxed{
\text{global shell }L^2
}
$$

and:

$$
\boxed{
\text{scaled shell }L^\infty
}
$$

is, up to fixed kernel constants, exactly:

$$
\boxed{
\sqrt{
a_{\omega}^{A}
}.
}
$$

Thus the Cycle-I far-separated-translate no-go is precisely:

$$
\boxed{
a_{\omega}^{A}\to0.
}
$$

Spatial dispersion is not merely one possible explanation for:

$$
L^2\not\Rightarrow L^\infty;
$$

for one band-limited shell it is the canonical explanation.

---

# 10. Absolute cell mass versus relative atom

A small relative atom:

$$
a_{\omega}^{A}
$$

does not imply every cell has dynamically negligible absolute mass.

A shell may have enormous global:

$$
L^2
$$

mass while each individual cell is only a small fraction.

Therefore synchronization with a singular core should also track:

$$
\boxed{
\text{absolute local shell enstrophy}.
}
$$

This motivates the Type-I part of the paper.

---

# 11. Type-I setting

Normalize the candidate singular point to:

$$
(x_\ast,T_\ast)
=
(0,0).
$$

Assume a suitable finite-energy solution on:

$$
[-1,0]
$$

satisfies the Type-I Lorentz bound:

$$
\boxed{
\|u\|_{
L_t^\infty
L_x^{3,\infty}
(\mathbb R^3\times(-1,0))
}
\le
M.
}
$$

Assume:

$$
(0,0)
$$

is singular.

---

# 12. External Type-I enstrophy concentration

Barker--Prange prove that for sufficiently large:

$$
M,
$$

there is:

$$
S^\sharp(M)\in(0,1/4]
$$

such that for a full-measure set of times:

$$
t\in[-1,0),
$$

the vorticity satisfies:

$$
\boxed{
\int_{
B_0(
4(S^\sharp)^{-1/2}(-t)^{1/2}
)
}
|\omega(x,t)|^2dx
>
M^2
(-t)^{-1/2}
\sqrt{
S^\sharp
}.
}
$$

Define the Type-I core radius:

$$
\boxed{
R_I(t)
=
4
(S^\sharp)^{-1/2}
(-t)^{1/2}.
}
$$

Then the concentration inequality becomes:

$$
\boxed{
R_I(t)
\int_{
B_{R_I(t)}
}
|\omega(x,t)|^2dx
>
4M^2.
}
$$

Equivalently:

$$
\boxed{
\|\omega(t)\|_{
L^2(B_{R_I(t)})
}
>
2M
R_I(t)^{-1/2}.
}
$$

This is an external theorem input.

---

# 13. Lorentz--Bernstein low-frequency estimate

Let:

$$
P_{\le J}
$$

be a smooth low-frequency projector.

Standard Lorentz-space Bernstein estimates give:

$$
\boxed{
\|P_{\le J}u(t)\|_\infty
\le
C
2^J
M.
}
$$

Therefore:

$$
\boxed{
\|P_{\le J}\omega(t)\|_\infty
\le
C
2^{2J}
M.
}
$$

Hence on a ball:

$$
B_R,
$$

$$
\boxed{
\|P_{\le J}\omega(t)\|_{
L^2(B_R)
}
\le
C
M
R^{-1/2}
(2^JR)^2.
}
$$

---

# 14. Core parabolic frequency

Choose a universal:

$$
0<\kappa_0<1
$$

small enough that:

$$
C\kappa_0^2
\le
1.
$$

Define:

$$
J_I(t)
$$

by:

$$
\boxed{
2^{J_I(t)}
R_I(t)
\le
\kappa_0
<
2^{J_I(t)+1}
R_I(t).
}
$$

Thus:

$$
2^{J_I(t)}
\asymp
R_I(t)^{-1}.
$$

---

# 15. CII-2.2 — Type-I Singular-Core UV Extraction

## Theorem 15.1

Under the Type-I hypotheses of Section 11, for almost every:

$$
t
$$

in the Barker--Prange full-measure set:

$$
\boxed{
\|
P_{>J_I(t)}
\omega(t)
\|_{
L^2(B_{R_I(t)})
}
\ge
M
R_I(t)^{-1/2}.
}
$$

### Proof

Section 12 gives:

$$
\|\omega\|_{
L^2(B_{R_I})
}
>
2M
R_I^{-1/2}.
$$

By Section 13 and the definition of:

$$
J_I,
$$

$$
\|P_{\le J_I}\omega\|_{
L^2(B_{R_I})
}
\le
M
R_I^{-1/2}.
$$

Using:

$$
\omega
=
P_{\le J_I}\omega
+
P_{>J_I}\omega
$$

and the triangle inequality yields the result. $\square$

---

# 16. Interpretation

The singular Type-I parabolic core cannot be supported entirely by frequencies:

$$
\boxed{
2^j
\ll
R_I(t)^{-1}.
}
$$

A fixed fraction of its critical enstrophy norm must lie at:

$$
\boxed{
\text{parabolic frequency or above}.
}
$$

This is a standard-PDE singular-core ultraviolet extraction result.

---

# 17. Local high-tail shell gross

Define:

$$
\boxed{
H_I(t)
=
\sum_{
j>J_I(t)
}
\|\omega_j(t)\|_{
L^2(B_{R_I(t)})
}.
}
$$

Since the solution is smooth for:

$$
t<0,
$$

the sum is finite.

The triangle inequality and Theorem 15.1 give:

$$
\boxed{
H_I(t)
\ge
M
R_I(t)^{-1/2}.
}
$$

---

# 18. Local moving-window capture

Let:

$$
\mathcal W(t)
=
\{
j:
J_{low}(t)
\le
j
\le
J_{high}(t)
\}
$$

be the Bradshaw--Grujic moving relevant frequency window.

Define the local Type-I core window:

$$
\boxed{
\mathcal W_I(t)
=
\mathcal W(t)
\cap
\{
j>J_I(t)
\}.
}
$$

Define the local window-capture ratio:

$$
\boxed{
c_{I,win}(t)
=
\frac{
\sum_{
j\in\mathcal W_I(t)
}
\|\omega_j(t)\|_{
L^2(B_{R_I(t)})
}
}{
H_I(t)
}.
}
$$

Then:

$$
0\le
c_{I,win}(t)
\le1.
$$

---

# 19. Local shell atom

If:

$$
c_{I,win}(t)>0,
$$

define:

$$
\boxed{
a_{I,sh}(t)
=
\max_{
j\in\mathcal W_I(t)
}
\frac{
\|\omega_j(t)\|_{
L^2(B_{R_I(t)})
}
}{
\sum_{
k\in\mathcal W_I(t)
}
\|\omega_k(t)\|_{
L^2(B_{R_I(t)})
}
}.
}
$$

Choose a maximizing shell:

$$
\boxed{
j_I^\star(t).
}
$$

---

# 20. Core-shell lower bound

If:

$$
c_{I,win}(t)\ge\chi
$$

and:

$$
a_{I,sh}(t)\ge\eta,
$$

then:

$$
\boxed{
\|\omega_{j_I^\star}(t)\|_{
L^2(B_{R_I(t)})
}
\ge
\chi
\eta
M
R_I(t)^{-1/2}.
}
$$

---

# 21. Parabolic packing number

Fix wavelength cells with:

$$
A=1.
$$

For a shell:

$$
j,
$$

define:

$$
\boxed{
\Theta_I(j,t)
=
2^j
R_I(t).
}
$$

A ball:

$$
B_{R_I(t)}
$$

intersects at most:

$$
\boxed{
N_I(j,t)
\le
C
\left(
1+
\Theta_I(j,t)
\right)^3
}
$$

dyadic wavelength cubes of side:

$$
2^{-j}.
$$

---

# 22. CII-2.3 — Parabolic Packing Lemma

## Theorem 22.1

For any shell:

$$
j,
$$

there exists a wavelength cube:

$$
Q_\star
$$

intersecting:

$$
B_{R_I(t)}
$$

such that:

$$
\boxed{
\|\omega_j(t)\|_{
L^2(Q_\star)
}
\ge
C^{-1/2}
\left(
1+
\Theta_I(j,t)
\right)^{-3/2}
\|\omega_j(t)\|_{
L^2(B_{R_I(t)})
}.
}
$$

### Proof

The ball is covered by at most:

$$
N_I
$$

intersecting cells.

The sum of their squared:

$$
L^2
$$

masses is at least the squared mass on the ball.

One cell carries at least:

$$
N_I^{-1}
$$

of the squared mass. $\square$

---

# 23. Core carrier to frequency amplitude

Apply Theorem 22.1 to:

$$
j_I^\star(t).
$$

CSP-01 / the vorticity version of the local synchronizer gives:

$$
\boxed{
2^{-j_I^\star/2}
\|u_{j_I^\star}(t)\|_\infty
\ge
c
\|\omega_{j_I^\star}(t)\|_{
L^2(Q_\star)
}.
}
$$

Therefore Sections 20--22 yield:

$$
\boxed{
2^{-j_I^\star/2}
\|u_{j_I^\star}(t)\|_\infty
\ge
c
\chi
\eta
M
R_I(t)^{-1/2}
\left(
1+
\Theta_I(j_I^\star,t)
\right)^{-3/2}.
}
$$

---

# 24. CII-2.4 — Type-I Core Synchronizer

## Theorem 24.1

Assume:

$$
c_{I,win}(t)\ge\chi,
$$

$$
a_{I,sh}(t)\ge\eta,
$$

and:

$$
\Theta_I(j_I^\star(t),t)\le H.
$$

Then:

$$
\boxed{
\Phi_{1/2}(t)^4
\ge
c
\chi^4
\eta^4
M^4
(1+H)^{-6}
R_I(t)^{-2}.
}
$$

Since:

$$
R_I(t)^2
=
16
(S^\sharp)^{-1}
(-t),
$$

one has:

$$
\boxed{
\Phi_{1/2}(t)^4
\ge
c(M,\chi,\eta,H)
\frac1{-t}.
}
$$

### Proof

Because:

$$
j_I^\star(t)
\in
\mathcal W(t),
$$

$$
\Phi_{1/2}(t)
\ge
2^{-j_I^\star/2}
\|u_{j_I^\star}(t)\|_\infty.
$$

Use Section 23 and raise to the fourth power. $\square$

---

# 25. Logarithmic-time measure

Define the singular logarithmic measure:

$$
\boxed{
d\mu_{\log}(t)
=
\frac{dt}{-t},
\qquad
t<0.
}
$$

For every:

$$
t_0<0,
$$

$$
\boxed{
\mu_{\log}((t_0,0))
=
\infty.
}
$$

Thus Theorem 24.1 converts a good Type-I core time directly into a lower bound for the frequency-window action density with respect to logarithmic time.

---

# 26. Type-I core defect sets

Fix:

$$
0<\chi,\eta<1,
$$

and:

$$
H<\infty.
$$

On the Barker--Prange full-measure time set define:

## Core-window mismatch

$$
\boxed{
\mathcal D_{I,win}
=
\{
t:
c_{I,win}(t)<\chi
\}.
}
$$

## Core-shell atomization

$$
\boxed{
\mathcal D_{I,sh}
=
\{
t:
c_{I,win}(t)\ge\chi,
\;
a_{I,sh}(t)<\eta
\}.
}
$$

## Super-parabolic micro-packing

$$
\boxed{
\mathcal D_{I,micro}
=
\{
t:
c_{I,win}(t)\ge\chi,
\;
a_{I,sh}(t)\ge\eta,
\;
\Theta_I(j_I^\star,t)>H
\}.
}
$$

## Good Type-I core

The complement:

$$
\boxed{
\mathcal G_I(\chi,\eta,H).
}
$$

---

# 27. CII-2.5 — Type-I Spatial-Core Alternative

## Theorem 27.1

At least one of the following four sets has infinite logarithmic measure:

### CORE-SYNC

$$
\boxed{
\mu_{\log}
(
\mathcal G_I
)
=
\infty.
}
$$

Then:

$$
\boxed{
\int_{
\mathcal G_I
}
\Phi_{1/2}(t)^4dt
=
\infty.
}
$$

### CORE-WIN

$$
\boxed{
\mu_{\log}
(
\mathcal D_{I,win}
)
=
\infty.
}
$$

### CORE-SHELL

$$
\boxed{
\mu_{\log}
(
\mathcal D_{I,sh}
)
=
\infty.
}
$$

### MICRO-PACK

$$
\boxed{
\mu_{\log}
(
\mathcal D_{I,micro}
)
=
\infty.
}
$$

### Proof

The Barker--Prange concentration set has full Lebesgue measure near:

$$
0,
$$

hence full:

$$
\mu_{\log}
$$

measure modulo a null set.

The four sets partition it.

A finite union of finite:

$$
\mu_{\log}
$$

measure sets cannot cover:

$$
(t_0,0).
$$

On the good set use Theorem 24.1. $\square$

---

# 28. Meaning of CORE-WIN

CORE-WIN says:

$$
\boxed{
\text{the singular-core UV vorticity stock avoids the standard moving relevant frequency window}.
}
$$

This is stronger and more local than CSP-01's global window mismatch.

It is a direct spatial/frequency synchronization defect at the singular core.

---

# 29. Meaning of CORE-SHELL

CORE-SHELL says the moving window captures the core UV stock,

but no shell carries a fixed fraction of the local shell gross.

If:

$$
a_{I,sh}\le\eta,
$$

then at least:

$$
\boxed{
\frac1{2\eta}
}
$$

window shells are needed to carry half of the local window:

$$
L^2
$$

shell-gross.

Thus this defect incurs local frequency multiplicity.

---

# 30. Meaning of MICRO-PACK

MICRO-PACK says:

$$
\boxed{
2^{j_I^\star}
R_I
\gg1.
}
$$

The selected carrier wavelength:

$$
2^{-j_I^\star}
$$

is much smaller than the parabolic singular-core radius:

$$
R_I.
$$

The number of wavelength cells inside the singular core is:

$$
\boxed{
N_I
\sim
\left(
2^{j_I^\star}
R_I
\right)^3.
}
$$

Thus spatial dispersion is recompiled into:

$$
\boxed{
\textbf{super-parabolic spatial multiplicity}.
}
$$

---

# 31. Concentration radius formulation

For a shell:

$$
\omega_j,
$$

and:

$$
0<\kappa<1,
$$

define the shell concentration radius:

$$
\boxed{
r_\kappa(j,t)
=
\inf
\left\{
R>0:
\exists x
\text{ with }
\|\omega_j\|_{L^2(B(x,R))}^2
\ge
\kappa
\|\omega_j\|_2^2
\right\}.
}
$$

---

# 32. CII-2.6 — Atom / Concentration-Radius Packing Inequality

## Theorem 32.1

For fixed cell factor:

$$
A\ge1,
$$

one has:

$$
\boxed{
\kappa
\le
C
a_{\omega}^{A}(j,t)
\left(
1+
\frac{
r_\kappa(j,t)
}{
A2^{-j}
}
\right)^3.
}
$$

Therefore:

$$
\boxed{
r_\kappa(j,t)
\ge
A2^{-j}
\left[
c
\left(
\frac{
\kappa
}{
a_{\omega}^{A}(j,t)
}
\right)^{1/3}
-
1
\right]_+.
}
$$

### Proof

Any ball of radius:

$$
r_\kappa
$$

meets at most:

$$
C
(
1+r_\kappa/(A2^{-j})
)^3
$$

cells.

Each cell carries at most:

$$
a_\omega^A
$$

of total squared shell mass.

Sum over intersecting cells. $\square$

---

# 33. D-SPACE becomes concentration-radius inflation

Theorem 32.1 gives a geometric interpretation:

$$
\boxed{
a_\omega^A\to0
}
$$

with fixed:

$$
\kappa
$$

forces:

$$
\boxed{
\frac{
r_\kappa
}{
2^{-j}
}
\to\infty.
}
$$

Thus persistent D-SPACE means:

> a fixed fraction of shell energy cannot be captured in any bounded number of wavelengths.

This is the exact concentration-radius form of spatial fragmentation.

---

# 34. Relation to Type-I core radius

Suppose a selected shell satisfies:

$$
\boxed{
\|\omega_j\|_{
L^2(B_{R_I})
}^2
\ge
\kappa
\|\omega_j\|_2^2.
}
$$

Then:

$$
r_\kappa(j,t)
\le
R_I(t).
$$

Theorem 32.1 yields:

$$
\boxed{
a_\omega^A(j,t)
\ge
c
\kappa
\left(
1+
\frac{
R_I(t)
}{
A2^{-j}
}
\right)^{-3}.
}
$$

Therefore if:

$$
2^jR_I(t)\le H,
$$

the spatial atom has a fixed lower bound.

---

# 35. Parabolic core-capture synchronizer

## Theorem 35.1

Fix:

$$
\kappa>0,
\qquad
H<\infty.
$$

Suppose the selected moving-window shell:

$$
j_\star(t)
$$

satisfies:

$$
\|\omega_{j_\star}\|_{
L^2(B_{R_I})
}^2
\ge
\kappa
\|\omega_{j_\star}\|_2^2
$$

and:

$$
2^{j_\star}R_I\le H.
$$

Then:

$$
\boxed{
a_\omega^A(j_\star,t)
\ge
c_{A,H}
\kappa.
}
$$

Consequently the CSP-01 spatial dispersion defect cannot occur below any:

$$
\sigma
<
c_{A,H}\kappa.
$$

$\square$

---

# 36. What Type-I enstrophy concentration does not prove

The Barker--Prange theorem gives concentration of the **total vorticity enstrophy** in:

$$
B_{R_I}.
$$

It does not by itself prove:

$$
\boxed{
\|\omega_{j_\star}\|_{
L^2(B_{R_I})
}^2
\ge
\kappa
\|\omega_{j_\star}\|_2^2
}
$$

for the shell selected by CSP-01's global middle-strain/window geometry.

Therefore the missing bridge is now:

$$
\boxed{
\textbf{singular-core-to-carrier-shell alignment}.
}
$$

---

# 37. Local smoothing contrapositive status

Barker--Prange local smoothing says, after scaling, sufficiently small local critical:

$$
L^3
$$

initial data in a ball yields short-time interior smoothness.

Their Type-I singularity theorem uses the contrapositive to force local:

$$
L^3
$$

concentration at the singular point.

The later quantitative work further forces local vorticity enstrophy concentration and propagates it backward.

These theorems validate the singular-core geometry used here.

They do **not** directly identify the CSP carrier shell.

---

# 38. Core-alignment defect

Define:

$$
\boxed{
D_{\rm ALIGN}
}
$$

to mean:

> the standard-PDE singular-core enstrophy and the CSP middle/frequency carrier shell fail to have a uniform local overlap.

This defect is more precise than the original:

$$
D_{\rm space}.
$$

The spatial problem is therefore reduced to:

$$
\boxed{
D_{\rm ALIGN}
\vee
D_{I,win}
\vee
D_{I,sh}
\vee
D_{I,micro}.
}
$$

---

# 39. Why $D_{\rm ALIGN}$ is genuinely new

CSP-01 used global:

$$
L^2
$$

middle-strain / shell quantities.

Barker--Prange gives a local singular-core vorticity quantity.

Global shell equivalence:

$$
\|\omega_j\|_2^2
=
2\|S_j\|_2^2
$$

does not imply local core equivalence.

Thus:

$$
\boxed{
\text{global shell identity}
\neq
\text{local singular-core alignment}.
}
$$

No current theorem in the program closes this gap.

---

# 40. Enstrophy propagation significance

Barker--Prange also prove backward propagation of Type-I vorticity concentration across well-separated times.

Thus:

$$
D_{\rm ALIGN}
$$

cannot be dismissed merely as a single-time concentration artifact.

The standard PDE singular core has genuine backward persistence.

What remains open is whether the **same dyadic carrier geometry** persists with it.

---

# 41. New guards

Add:

### $G_{\rm ATOMEQ}$

At fixed band, scaled:

$$
L^\infty
$$

amplitude and wavelength-cell vorticity atomization must be treated as quantitatively equivalent.

### $G_{\rm TYPEIUV}$

Under Type-I singular-core hypotheses, low frequencies:

$$
2^jR_I\ll1
$$

cannot carry all local enstrophy.

### $G_{\rm COREWIN}$

Distinguish global moving-window capture from singular-core moving-window capture.

### $G_{\rm CORESH}$

Distinguish global shell atomization from local singular-core shell atomization.

### $G_{\rm PACK}$

Track:

$$
\Theta_I
=
2^jR_I
$$

as the parabolic wavelength packing number.

### $G_{\rm ALIGN}$

Do not infer local carrier-shell capture from global strain/vorticity shell equivalence.

---

# 42. Cycle-II frontier update

CSP-01 residual defects:

$$
D_{\rm win}
\vee
D_{\rm shell}
\vee
D_{\rm space}.
$$

CSP-02 resolves the internal structure of:

$$
D_{\rm space}.
$$

In the Type-I singular-core setting the spatial branch becomes:

$$
\boxed{
\text{CORE-SYNC}
}
$$

or:

$$
\boxed{
D_{\rm ALIGN}
\vee
D_{I,win}
\vee
D_{I,sh}
\vee
D_{I,micro}.
}
$$

The next most natural target is shell atomization and its relation to spectral dispersion.

---

# 43. Next paper

$$
\boxed{
\textbf{
NS-CSP 03 —
Shell Atomization、
Spectral-Variance Geometry、
Approximate Eigen-Shells
與 Resonant Transfer
}.
}
$$

Main tasks:

1. compare dyadic shell multiplicity with the exact:
   $$
   D_{eig}(S)
   $$
   spectral-variance identity;
2. prove quantitative variance lower bounds for genuinely separated shell clusters;
3. distinguish many-shell occupancy inside one bounded log-frequency band from true spectral-radius dispersion;
4. connect high--high resonant parent geometry to multi-shell dispersion;
5. attack:
   $$
   D_{\rm shell}
   $$
   and:
   $$
   D_{I,sh}.
   $$

---

# 44. Formal status ledger

$$
\boxed{
\begin{aligned}
\text{wavelength-cell vorticity atom}
&:\ \mathrm{DEFINED},\\
\text{spatial-atom equivalence}
&:\ \mathrm{PROVED},\\
\text{Type-I enstrophy concentration}
&:\ \mathrm{EXTERNAL},\\
\text{Type-I low-frequency exclusion}
&:\ \mathrm{PROVED},\\
\text{Type-I singular-core UV extraction}
&:\ \mathrm{PROVED},\\
\text{parabolic packing lemma}
&:\ \mathrm{PROVED},\\
\text{Type-I core synchronizer}
&:\ \mathrm{PROVED\ CONDITIONALLY},\\
\text{Type-I spatial-core alternative}
&:\ \mathrm{PROVED},\\
\text{atom/concentration-radius inequality}
&:\ \mathrm{PROVED},\\
\text{parabolic core-capture synchronizer}
&:\ \mathrm{PROVED\ CONDITIONALLY},\\
\text{singular-core-to-carrier-shell alignment}
&:\ \mathrm{OPEN},\\
\text{core-window mismatch exclusion}
&:\ \mathrm{OPEN},\\
\text{core-shell atomization exclusion}
&:\ \mathrm{OPEN},\\
\text{super-parabolic micro-packing exclusion}
&:\ \mathrm{OPEN},\\
\text{Coercive Synchronization Problem}
&:\ \mathrm{OPEN},\\
\text{Navier--Stokes regularity}
&:\ \mathrm{NOT\ PROVED}.
\end{aligned}
}
$$

---

# 45. Conclusion

CSP-02 identifies the exact fixed-shell spatial mechanism behind:

$$
L^2
\not\Rightarrow
L^\infty.
$$

For every band-limited vorticity shell:

$$
\boxed{
2^{-j/2}
\|u_j\|_\infty
\asymp_A
\sqrt{
a_\omega^A(j,t)
}
\,
\|\omega_j\|_2.
}
$$

Thus wavelength-cell atomization is the correct spatial defect coordinate.

In the Type-I singular-core setting, Barker--Prange enstrophy concentration plus Lorentz--Bernstein yields:

$$
\boxed{
\|
P_{>J_I(t)}
\omega(t)
\|_{
L^2(B_{R_I(t)})
}
\gtrsim
M
R_I(t)^{-1/2},
\qquad
2^{J_I(t)}
\asymp
R_I(t)^{-1}.
}
$$

Hence a Type-I singular core necessarily contains parabolic-or-higher-frequency vorticity stock.

If that stock:

1. enters the moving relevant frequency window;
2. has a local shell atom;
3. does not escape to frequencies with:
   $$
   2^jR_I\to\infty;
   $$

then the same singular core forces:

$$
\boxed{
\Phi_{1/2}(t)^4
\gtrsim
\frac{
c(M)
}{
T_\ast-t
}.
}
$$

The residual Type-I spatial synchronization defects are therefore:

$$
\boxed{
\text{core-window mismatch}
\vee
\text{core-shell atomization}
\vee
\text{super-parabolic micro-packing}
}
$$

plus the independent global-to-core carrier alignment problem:

$$
\boxed{
D_{\rm ALIGN}.
}
$$

The original spatial-dispersion defect has therefore been decomposed into explicit, measurable, scale-compatible geometric mechanisms.

---

# References

1. T. Barker, C. Prange, *Localized smoothing for the Navier–Stokes equations and concentration of critical norms near singularities*, Archive for Rational Mechanics and Analysis 236 (2020), 1487–1541; arXiv:1812.09115v2.
2. T. Barker, C. Prange, *Quantitative regularity for the Navier–Stokes equations via spatial concentration*, Communications in Mathematical Physics 385 (2021), 717–792; arXiv:2003.06717v3.
3. Z. Bradshaw, Z. Grujic, *Frequency localized regularity criteria for the 3D Navier–Stokes equations*, Archive for Rational Mechanics and Analysis 224 (2017), 125–133; arXiv:1501.01043v2.
4. T. Tao, *Quantitative bounds for critically bounded solutions to the Navier–Stokes equations*, arXiv:1908.04958v2.
5. `NS_CSP_01_SpatialConcentration_Synchronizer_v0.1.md`.
6. `NS_RFP_CYCLE_I_STANDARD_PDE_RECOMPILATION_v1.0.md`.
