---
title: "Navier–Stokes Coercive Synchronization Program 04：Moving-Window Capture、Dissipation-Wavenumber Geometry、Escape Intervals 與 UV Stock Placement"
short_title: "NS-CSP 04"
series: "Navier–Stokes Coercive Synchronization Program"
cycle: "II"
version: "v0.1"
date: "2026-08-15"
author: "Neo.K / EveMissLab"
language: "zh-TW"
status: "Theorem-style moving-window synchronization / escape-interval reduction"
epistemic_status: "Uses the exact Bradshaw–Grujic window construction at epsilon=1/2 to prove window domination on their active escape intervals, shows the Cheskidov–Shvydkoy dissipation wavenumber lies below the Bradshaw–Grujic upper endpoint up to fixed constants, absorbs fixed window-edge padding into a stronger standard regularity window, and proves a same-time middle/frequency synchronization theorem that does not require the middle-strain carrier itself to lie inside the moving window. Consequently, the global moving-window defect is reduced to shell/spatial carrier defects or an escape-gap temporal mismatch. It does NOT exclude the escape-gap branch, prove singular-core/carrier alignment, or prove Navier–Stokes regularity."
canonical_source: "UTF-8 Markdown"
---

# Navier–Stokes Coercive Synchronization Program 04

# Moving-Window Capture、Dissipation-Wavenumber Geometry、Escape Intervals 與 UV Stock Placement

## 0. 本文定位

CSP-01 reduced same-time synchronization failure to:

$$
D_{\rm win}
\vee
D_{\rm shell}
\vee
D_{\rm space}.
$$

CSP-02 decomposed:

$$
D_{\rm space},
$$

and CSP-03 proved that severe global:

$$
D_{\rm shell}
$$

forces same-time synchronization of the middle-strain and approximate-eigenfunction actions, leaving only finite window-edge leakage and alignment defects.

The present paper attacks:

$$
\boxed{
D_{\rm win}
}
$$

and:

$$
\boxed{
D_{\rm EDGE}.
}
$$

The central observation is that the Bradshaw--Grujic moving window already comes with a hidden domination theorem on the local-wellposedness escape intervals used in their proof.

Once this is made explicit, a middle-strain carrier does **not** need to lie in the moving window itself in order to force same-time frequency-window activity.

---

# 1. Canonical epsilon slice

Fix:

$$
\boxed{
\epsilon=\frac12.
}
$$

Define the critical Besov amplitude:

$$
\boxed{
B(t)
=
\|u(t)\|_{\dot B^{-1/2}_{\infty,\infty}}
=
\sup_j
2^{-j/2}
\|\dot\Delta_j u(t)\|_\infty.
}
$$

Let:

$$
E_2
=
\|u\|_{L^\infty(0,T;L^2)}.
$$

---

# 2. Bradshaw--Grujic endpoints at epsilon one-half

Their endpoint definitions become:

$$
\boxed{
2^{J_{\rm high}(t)}
=
c_1
B(t)^2,
}
$$

and:

$$
\boxed{
2^{J_{\rm low}(t)}
=
c_2
\frac{
B(t)
}{
E_2
}.
}
$$

Here:

$$
c_1,c_2>0
$$

are universal constants from the theorem.

Thus the multiplicative window width is:

$$
\boxed{
2^{J_{\rm high}-J_{\rm low}}
=
\frac{
c_1
}{
c_2
}
E_2
B(t).
}
$$

---

# 3. The window widens near a hypothetical singularity

Bradshaw--Grujic local well-posedness implies that if regularity is lost at:

$$
T,
$$

then:

$$
B(t)
\gtrsim
(T-t)^{-1/4}.
$$

Therefore:

$$
\boxed{
J_{\rm low}(t)\to+\infty,
\qquad
J_{\rm high}(t)\to+\infty,
}
$$

and:

$$
\boxed{
J_{\rm high}(t)-J_{\rm low}(t)\to+\infty.
}
$$

Hence the standard relevant window moves to the ultraviolet while containing an increasing number of dyadic scales.

---

# 4. Low-mode suppression

Bradshaw--Grujic Lemma 3 gives, for every:

$$
t,
$$

$$
\boxed{
\sup_{
j\le J_{\rm low}(t)
}
2^{-j/2}
\|\dot\Delta_j u(t)\|_\infty
<
\frac12
B(t).
}
$$

Thus the global Besov maximum can never be carried purely by frequencies strictly below the lower endpoint.

---

# 5. Escape times and active intervals

Bradshaw--Grujic define escape times:

$$
t_0
$$

for the Besov norm and attach a local-wellposedness interval:

$$
(t_0',t_0'').
$$

Let:

$$
\boxed{
I_{\rm BG}
=
\bigcup_{
t_0\in\mathcal E
}
(t_0',t_0'')
}
$$

denote the union of these active escape intervals.

Their Lemma 6 proves that if the critical Besov action diverges, then all of that divergence may be localized to:

$$
I_{\rm BG}.
$$

At:

$$
\epsilon=\frac12,
$$

this means:

$$
\boxed{
\int_0^T
B(t)^4dt
=
\infty
\iff
\int_{I_{\rm BG}}
B(t)^4dt
=
\infty.
}
$$

---

# 6. High-mode suppression on the active intervals

For:

$$
t\in I_{\rm BG},
$$

the proof of Bradshaw--Grujic Theorem 2 gives:

$$
\boxed{
\sup_{
j\ge J_{\rm high}(t)
}
2^{-j/2}
\|\dot\Delta_j u(t)\|_\infty
<
\frac12
B(t).
}
$$

Together with Section 4, both frequency exteriors are subdominant.

---

# 7. Moving-window density

Define:

$$
\boxed{
\Phi(t)
=
\Phi_{1/2}(t)
=
\sup_{
J_{\rm low}(t)
\le j\le
J_{\rm high}(t)
}
2^{-j/2}
\|\dot\Delta_j u(t)\|_\infty.
}
$$

Integer endpoint rounding may be absorbed into a fixed:

$$
O(1)
$$

padding constant and does not affect the statements below.

---

# 8. CII-4.1 — Escape-Interval Window Domination

## Theorem 8.1

For every:

$$
t\in I_{\rm BG},
$$

$$
\boxed{
\Phi(t)
\ge
\frac12
B(t).
}
$$

### Proof

Suppose instead:

$$
\Phi(t)
<
B(t)/2.
$$

Section 4 bounds all low modes by:

$$
B(t)/2.
$$

Section 6 bounds all high modes by:

$$
B(t)/2.
$$

The middle window is also below:

$$
B(t)/2.
$$

Therefore:

$$
\sup_j
2^{-j/2}
\|\dot\Delta_ju(t)\|_\infty
<
B(t),
$$

contradicting the definition of:

$$
B(t).
$$

The same argument applies if the supremum is not attained, by taking a maximizing sequence. $\square$

---

# 9. Consequence

On:

$$
I_{\rm BG},
$$

the moving finite window captures at least a fixed fraction of the **global critical Besov amplitude**.

This is stronger than a statement about one selected physical carrier shell.

Thus:

$$
\boxed{
\text{a particular middle-strain carrier need not itself lie in the moving window}.
}
$$

It is enough for that carrier to force the global Besov amplitude to be large.

The moving window then inherits a fixed fraction automatically.

---

# 10. CSP carrier-core hypothesis

Let:

$$
g(t)
=
\|\lambda_2^+(t)\|_2^2.
$$

Fix:

$$
\kappa>0.
$$

We say that a time:

$$
t
$$

has a:

$$
\kappa
$$

-wavelength carrier if there exist:

$$
j_\star(t),
\qquad
Q_\star(t),
$$

with:

$$
\ell(Q_\star)
=
A2^{-j_\star},
$$

such that:

$$
\boxed{
\|S_{j_\star}(t)\|_{
L^2(Q_\star)
}^2
\ge
\kappa
g(t).
}
$$

This single parameter:

$$
\kappa
$$

may arise as the product of:

- UV capture;
- shell atom;
- wavelength-cell spatial atom.

---

# 11. CSP-01 local carrier estimate

CSP-01 proved:

$$
\boxed{
2^{-j_\star/2}
\|u_{j_\star}(t)\|_\infty
\ge
c
A^{-3/2}
\|S_{j_\star}(t)\|_{
L^2(Q_\star)
}.
}
$$

Therefore a:

$$
\kappa
$$

-wavelength carrier gives:

$$
\boxed{
B(t)
\ge
c
A^{-3/2}
\kappa^{1/2}
g(t)^{1/2}.
}
$$

---

# 12. CII-4.2 — Window-Free Same-Time Synchronizer on Escape Intervals

## Theorem 12.1

If:

$$
t\in I_{\rm BG}
$$

has a:

$$
\kappa
$$

-wavelength carrier, then:

$$
\boxed{
\Phi(t)^4
\ge
c
A^{-6}
\kappa^2
g(t)^2.
}
$$

### Proof

The carrier estimate gives:

$$
B(t)
\ge
c
A^{-3/2}
\kappa^{1/2}
g(t)^{1/2}.
$$

Theorem 8.1 gives:

$$
\Phi(t)\ge B(t)/2.
$$

Raise to the fourth power. $\square$

---

# 13. Why this removes the old window-capture hypothesis

CSP-01 required:

$$
c_{\rm win}(t)\ge\chi
$$

before it could synchronize middle-strain and frequency-window densities.

Theorem 12.1 removes this requirement on:

$$
I_{\rm BG}.
$$

The carrier may sit:

- below the window;
- inside the window;
- above the window.

Its only job is to make:

$$
B(t)
$$

large.

The Bradshaw--Grujic window then captures another shell carrying at least half that critical amplitude.

So on active escape intervals:

$$
\boxed{
D_{\rm win}
\text{ is not an independent same-time scale-placement defect}.
}
$$

---

# 14. Severe shell atomization alternative

CSP-03 proved that severe global spectral shell atomization synchronizes the middle-strain and approximate-eigenfunction actions.

Thus at a high middle-strain spike time, either:

1. there is a fixed-share spectral/dyadic carrier after finite LP padding; or
2. the approximate-eigenfunction residual already satisfies:
   $$
   D_{\rm eig}(S)^4
   \gtrsim
   g(t)^2.
   $$

Therefore shell atomization need not be retained as a separate escape when analyzing Theorem 12.1.

---

# 15. Spatial atomization alternative

CSP-02 proved that fixed-shell failure of:

$$
L^2
\to
L^\infty
$$

is exactly wavelength-cell spatial atomization.

Thus if a fixed-share shell exists but no:

$$
\kappa
$$

-wavelength carrier can be extracted, the failure is quantified by:

$$
\boxed{
a_{\omega}^{A}\to0
}
$$

or equivalently by concentration-radius inflation.

---

# 16. High middle-strain spike set

For:

$$
M>0,
$$

define:

$$
E_M
=
\{
t:
g(t)>M
\}.
$$

Cycle I proved that under hypothetical finite blow-up:

$$
\boxed{
\int_{E_M}
g(t)^2dt
=
\infty
}
$$

for every:

$$
M>0.
$$

---

# 17. Carrier-good set

Fix:

$$
\kappa>0.
$$

Define:

$$
\boxed{
\mathcal C_\kappa
=
\{
t\in E_M:
\text{a }
\kappa
\text{-wavelength carrier exists}
\}.
}
$$

Its complement contains only shell/spatial concentration defects already typed in CSP-02/03.

---

# 18. Escape-overlap set

Define:

$$
\boxed{
\mathcal O_{\kappa,M}
=
E_M
\cap
I_{\rm BG}
\cap
\mathcal C_\kappa.
}
$$

On this set Theorem 12.1 gives same-time synchronization.

---

# 19. CII-4.3 — Escape-Overlap Synchronization Alternative

## Theorem 19.1

For every fixed:

$$
M,\kappa>0,
$$

at least one of the following holds:

### EO-SYNC

$$
\boxed{
\int_{
\mathcal O_{\kappa,M}
}
g(t)^2dt
=
\infty.
}
$$

Then:

$$
\boxed{
\int_{
\mathcal O_{\kappa,M}
}
\Phi(t)^4dt
=
\infty.
}
$$

### EO-CARRIER

$$
\boxed{
\int_{
E_M\cap
\mathcal C_\kappa^c
}
g(t)^2dt
=
\infty.
}
$$

Then shell/eigen or spatial-concentration defects carry infinite middle action.

### EO-GAP

$$
\boxed{
\int_{
E_M\setminus
I_{\rm BG}
}
g(t)^2dt
=
\infty.
}
$$

### Proof

The three sets cover:

$$
E_M.
$$

Cycle I gives:

$$
\int_{E_M}g^2=\infty.
$$

A finite union of finite integrals cannot equal infinity.

On EO-SYNC apply Theorem 12.1. $\square$

---

# 20. The new residual window defect

The old:

$$
D_{\rm win}
$$

was a frequency-placement statement.

Theorem 19.1 replaces it by:

$$
\boxed{
D_{\rm GAP}
:
\quad
\int_{
E_M\setminus I_{\rm BG}
}
g(t)^2dt
=
\infty.
}
$$

This is a **temporal escape-set mismatch**.

It says:

> the middle-strain critical action may live predominantly in the gaps between the Bradshaw--Grujic local-wellposedness escape intervals.

Thus the remaining window problem is temporal, not primarily spectral.

---

# 21. Two Bradshaw--Grujic escape-set geometries

Their Lemma 6 proof gives two cases.

## Terminal-coverage case

There exists:

$$
t_0<T
$$

such that:

$$
\boxed{
[t_0,T)
\subset
I_{\rm BG}.
}
$$

## Recurrent-gap case

There is an infinite sequence of disjoint active intervals approaching:

$$
T,
$$

with nontrivial gaps between them.

---

# 22. CII-4.4 — Terminal-Coverage Collapse of the Window Defect

## Theorem 22.1

In the terminal-coverage case:

$$
\boxed{
D_{\rm GAP}
\text{ cannot occur near }T.
}
$$

Therefore every sufficiently late middle-strain critical spike must either:

1. synchronize with:
   $$
   \Phi^4;
   $$
2. pay the shell/eigen defect;
3. pay the spatial-concentration defect.

### Proof

For:

$$
t\ge t_0,
$$

one has:

$$
t\in I_{\rm BG}.
$$

Therefore:

$$
E_M\setminus I_{\rm BG}
$$

is contained in a compact earlier-time interval.

Smoothness before:

$$
T
$$

makes:

$$
g^2
$$

integrable there. $\square$

---

# 23. Recurrent-gap defect

Only the second Bradshaw--Grujic case can support persistent:

$$
D_{\rm GAP}.
$$

Thus the moving-window problem is reduced to:

$$
\boxed{
\textbf{recurrent temporal gaps between critical Besov escape intervals}.
}
$$

This is much narrower than generic frequency-window mismatch.

---

# 24. Fixed endpoint padding

For:

$$
C\in\mathbb N,
$$

define the padded window:

$$
\boxed{
\mathcal W_C(t)
=
\{
j:
J_{\rm low}(t)-C
\le j\le
J_{\rm high}(t)+C
\}.
}
$$

Define:

$$
\boxed{
\Phi_C(t)
=
\sup_{
j\in\mathcal W_C(t)
}
2^{-j/2}
\|\dot\Delta_j u(t)\|_\infty.
}
$$

Clearly:

$$
\Phi_C(t)\ge\Phi(t).
$$

---

# 25. CII-4.5 — Padded-Window Coercivity

## Theorem 25.1

If:

$$
\boxed{
\int_0^T
\Phi_C(t)^4dt
<
\infty,
}
$$

then the solution is regular on:

$$
(0,T].
$$

Therefore finite-time blow-up requires:

$$
\boxed{
\int_0^T
\Phi_C(t)^4dt
=
\infty
}
$$

for every fixed:

$$
C.
$$

### Proof

Since:

$$
\Phi\le\Phi_C,
$$

finite padded-window action implies finite Bradshaw--Grujic action.

Apply their Theorem 2. $\square$

---

# 26. Consequence for D-EDGE

CSP-03 introduced:

$$
D_{\rm EDGE}
$$

when a fixed-share carrier lies in a fixed number of shells just outside the moving window.

Theorem 25.1 shows:

$$
\boxed{
D_{\rm EDGE}
}
$$

is not an independent coercive escape.

Any fixed:

$$
O(1)
$$

edge leakage can be absorbed into a padded moving window that remains a valid standard-PDE regularity criterion.

Thus:

$$
\boxed{
D_{\rm EDGE}
\text{ is removed from the primitive global defect list}.
}
$$

---

# 27. Cheskidov--Shvydkoy dissipation wavenumber

Normalize:

$$
\nu=1.
$$

Define:

$$
\boxed{
\Lambda(t)
=
2^{Q(t)}
}
$$

by:

$$
\boxed{
Q(t)
=
\min
\{
q:
2^{-p}
\|u_p(t)\|_\infty
<
c_0,
\quad
\forall p>q
\}.
}
$$

For:

$$
1<\Lambda(t)<\infty,
$$

their definition implies:

$$
\boxed{
\|u_{Q(t)}(t)\|_\infty
\ge
c_0
\Lambda(t).
}
$$

---

# 28. CII-4.6 — Dissipation-Wavenumber / Upper-Window Comparison

## Theorem 28.1

For:

$$
1<\Lambda(t)<\infty,
$$

$$
\boxed{
\Lambda(t)
\le
c_0^{-2}
B(t)^2.
}
$$

Since:

$$
2^{J_{\rm high}(t)}
=
c_1B(t)^2,
$$

there is a universal:

$$
C_Q
$$

such that:

$$
\boxed{
Q(t)
\le
J_{\rm high}(t)
+
C_Q.
}
$$

### Proof

At:

$$
q=Q(t),
$$

$$
B(t)
\ge
2^{-Q/2}
\|u_Q(t)\|_\infty
\ge
c_0
2^{Q/2}.
$$

Hence:

$$
2^Q
\le
c_0^{-2}
B(t)^2.
$$

Compare with the Bradshaw--Grujic upper endpoint. $\square$

---

# 29. Meaning of Theorem 28.1

The Bradshaw--Grujic upper window reaches at least to the dissipation wavenumber, up to a fixed dyadic offset.

Therefore frequencies far above:

$$
J_{\rm high}
$$

are also far into the Cheskidov--Shvydkoy viscous-dominated range.

This reclassifies high-end window escape as:

$$
\boxed{
\textbf{deep dissipation-range overshoot}.
}
$$

It is not an unclassified inertial-range branch.

---

# 30. Standard high-frequency viscous absorption

By definition of:

$$
Q(t),
$$

for every:

$$
p>Q(t),
$$

$$
\boxed{
2^{-p}
\|u_p(t)\|_\infty
<
c_0.
}
$$

Cheskidov--Shvydkoy use precisely this condition to absorb high-frequency nonlinear terms into viscosity in their regularity estimate.

Thus high-frequency stock above:

$$
Q(t)
$$

may exist,

but its direct role in the nonlinear energy estimate is quantitatively constrained by viscosity.

---

# 31. Dissipation-wavenumber path action

Cheskidov--Shvydkoy prove:

$$
\boxed{
\Lambda\in
L^{5/2}(0,T)
\Longrightarrow
\text{regularity}.
}
$$

They also prove:

$$
\Lambda\in
L^1(0,T)
$$

for every Leray--Hopf solution.

Therefore hypothetical finite blow-up requires:

$$
\boxed{
\int_0^T
\Lambda(t)^{5/2}dt
=
\infty.
}
$$

while still satisfying:

$$
\boxed{
\int_0^T
\Lambda(t)dt
<
\infty.
}
$$

This is another temporal intermittency condition on the dissipation scale.

---

# 32. Dissipation-scale intermittency

Define:

$$
h(t)
=
\Lambda(t).
$$

A hypothetical singularity must satisfy:

$$
\boxed{
h\in
L_t^1
\setminus
L_t^{5/2}.
}
$$

Thus the dissipation wavenumber itself must become increasingly intermittent in time.

This is structurally parallel to the Cycle-I middle-strain result:

$$
g
\in
L_t^1
\setminus
L_t^2.
$$

No synchronization between these two intermittent quantities is yet proved.

---

# 33. Cheskidov--Dai shell-time criterion

Cheskidov--Dai prove that regularity follows if:

$$
\limsup_{
q\to\infty
}
\int_{\mathcal T_q}^{T}
\|\Delta_q\omega(t)\|_\infty dt
$$

is sufficiently small, for an appropriate sequence:

$$
\mathcal T_q\uparrow T.
$$

Therefore hypothetical blow-up requires recurrent non-small shell-vorticity time integrals near arbitrarily high frequencies.

This supports the interpretation that dangerous high-frequency overshoot must carry persistent time-integrated activity, not merely isolated instantaneous stock.

---

# 34. Low-window exterior

Bradshaw--Grujic low-mode suppression holds for every time:

$$
t.
$$

Hence no global Besov maximum may be hidden strictly below:

$$
J_{\rm low}(t).
$$

Any global critical amplitude not captured by the moving window must therefore, outside:

$$
I_{\rm BG},
$$

be carried at the upper side.

This is the precise sense in which residual:

$$
D_{\rm GAP}
$$

is linked to high-frequency overshoot.

---

# 35. High-overshoot defect

Define:

$$
\boxed{
D_{\rm HI}
}
$$

as times:

$$
t\notin I_{\rm BG}
$$

for which a near-maximizing Besov shell lies above:

$$
J_{\rm high}(t).
$$

By Theorem 28.1, such a shell lies beyond the dissipation wavenumber up to a fixed offset.

Thus:

$$
\boxed{
D_{\rm HI}
\subset
\text{deep dissipation-range overshoot}
}
$$

modulo fixed dyadic constants.

---

# 36. Escape-gap versus high-overshoot

If:

$$
D_{\rm GAP}
$$

carries infinite middle-strain action,

there are two possibilities:

1. the middle-strain carrier defects already occur:
   shell/eigen or spatial concentration failure;
2. a carrier exists, forces:
   $$
   B(t)
   $$
   large, but the Besov maximum sits above:
   $$
   J_{\rm high}(t),
   $$
   because:
   $$
   t\notin I_{\rm BG}.
   $$

Thus the unresolved window branch becomes:

$$
\boxed{
\text{escape-gap temporal mismatch}
+
\text{deep dissipation-range overshoot}.
}
$$

---

# 37. Type-I singular-core version

Return to the CSP-02 Type-I singular core.

Suppose at a Type-I core time there is a local carrier shell:

$$
j^\star(t)
$$

and wavelength cell satisfying:

$$
\boxed{
\|\omega_{j^\star}(t)\|_{
L^2(Q_\star)
}
\ge
\kappa
M
R_I(t)^{-1/2}.
}
$$

Then the vorticity version of CSP-01 gives:

$$
\boxed{
B(t)
\ge
c
\kappa
M
R_I(t)^{-1/2}.
}
$$

---

# 38. CII-4.7 — Type-I Core Window-Free Synchronizer on Escape Intervals

## Theorem 38.1

If the Type-I core time:

$$
t
$$

lies in:

$$
I_{\rm BG}
$$

and admits the local carrier of Section 37, then:

$$
\boxed{
\Phi(t)^4
\ge
c
\kappa^4
M^4
R_I(t)^{-2}.
}
$$

Since:

$$
R_I(t)^2
\asymp_M
T_\ast-t,
$$

$$
\boxed{
\Phi(t)^4
\ge
\frac{
c(M,\kappa)
}{
T_\ast-t
}.
}
$$

### Proof

Section 37 gives the Besov lower bound.

Theorem 8.1 transfers it to the moving window. $\square$

---

# 39. Consequence for local core-window mismatch

CSP-02 introduced:

$$
D_{I,\rm win}.
$$

Theorem 38.1 shows that, on:

$$
I_{\rm BG},
$$

the local carrier itself need not lie in the moving window.

If the Type-I singular core produces any wavelength-localized carrier of sufficient absolute mass,

the moving window is forced active through the global Besov norm.

Therefore:

$$
\boxed{
D_{I,\rm win}
}
$$

is also not a primitive same-time defect on the active escape intervals.

---

# 40. Type-I residual temporal defect

The unresolved Type-I window mismatch is therefore:

$$
\boxed{
D_{I,\rm GAP}
:
\text{singular-core carrier times lie persistently outside }
I_{\rm BG}.
}
$$

This is again temporal rather than spectral.

---

# 41. Updated global synchronization defects

After CSP-03 and CSP-04, the global primitive synchronization defects are reduced to:

$$
\boxed{
D_{\rm SPACE}
\vee
D_{\rm GAP},
}
$$

with severe shell atomization absorbed by:

$$
D_{\rm eig}
$$

same-time synchronization and fixed edge leakage absorbed by padded windows.

CSP-02 further decomposes:

$$
D_{\rm SPACE}.
$$

Therefore the new genuinely global temporal frontier is:

$$
\boxed{
D_{\rm GAP}.
}
$$

---

# 42. Updated Type-I core defects

In the Type-I architecture, the residual defects become:

$$
\boxed{
D_{\rm ALIGN}
\vee
D_{\rm SHALIGN}
\vee
D_{I,\rm sh}
\vee
D_{I,\rm micro}
\vee
D_{I,\rm GAP}.
}
$$

The explicit local window-capture defect is removed on:

$$
I_{\rm BG}.
$$

---

# 43. What has actually been eliminated?

We have not proved that all UV strain stock lies in the Bradshaw--Grujic moving window.

Instead we proved something stronger for synchronization:

$$
\boxed{
\text{on }I_{\rm BG},
\text{ it does not need to}.
}
$$

Any localized dangerous carrier anywhere in frequency forces:

$$
B(t)
$$

large, and the theorem's own moving window then captures a fixed fraction of:

$$
B(t).
$$

This is why the old:

$$
D_{\rm win}
$$

is not the correct residual object.

---

# 44. The new missing theorem

The remaining problem is:

$$
\boxed{
\textbf{Escape-Interval Synchronization Problem}.
}
$$

Can the middle-strain critical action, or the Type-I singular-core carrier activity, concentrate predominantly in:

$$
I_{\rm BG}^c
$$

while the critical Besov/frequency-window action concentrates on:

$$
I_{\rm BG}?
$$

This is now a pure pathwise temporal synchronization question.

---

# 45. Why this is not measure theory

Cycle I already proved that unrelated divergent actions may live on disjoint spike sets.

To eliminate:

$$
D_{\rm GAP},
$$

one needs a Navier--Stokes propagation estimate coupling:

- middle-strain bursts;
- Besov escape times;
- local-wellposedness intervals;
- possibly first-passage macro edges.

No measure-theoretic divergence argument can do this.

---

# 46. New guards

Add:

### $G_{\rm BGDOM}$

On Bradshaw--Grujic active escape intervals:

$$
\Phi_{1/2}\ge B/2.
$$

### $G_{\rm WINFREE}$

A localized middle-strain carrier need not itself lie inside the moving window to force frequency-window activity on:

$$
I_{\rm BG}.
$$

### $G_{\rm PADWIN}$

Fixed:

$$
O(1)
$$

window padding remains a valid stronger regularity window and absorbs finite edge leakage.

### $G_{\rm DISSUP}$

The Cheskidov--Shvydkoy dissipation wavenumber satisfies:

$$
Q(t)\le
J_{\rm high}(t)+O(1)
$$

at:

$$
\epsilon=1/2.
$$

### $G_{\rm GAP}$

Moving-window synchronization failure after the above reductions must preserve whether critical middle action lies outside:

$$
I_{\rm BG}.
$$

---

# 47. Next paper

The original Cycle-II roadmap planned to move next to core/model-cone alignment.

CSP-04 reveals a sharper global frontier first.

The next paper should attack:

$$
\boxed{
D_{\rm GAP}.
}
$$

Therefore:

$$
\boxed{
\textbf{
NS-CSP 05 —
Escape-Time Synchronization、
Middle-Strain Burst Propagation、
Besov Recovery Windows
與 Temporal Gap Rigidity
}.
}
$$

Primary tasks:

1. relate middle-strain burst times to nearby Besov escape times;
2. use local well-posedness recovery intervals as temporal barriers;
3. compare first-passage macro intervals with:
   $$
   I_{\rm BG};
   $$
4. determine whether recurrent:
   $$
   I_{\rm BG}^c
   $$
   gaps can carry infinite:
   $$
   g^2
   $$
   action;
5. if not, close the global middle/frequency synchronization;
6. if yes, quantify the temporal-gap escape.

---

# 48. Formal status ledger

$$
\boxed{
\begin{aligned}
\text{BG endpoint formulas at }\epsilon=1/2
&:\ \mathrm{EXTERNAL/VERIFIED},\\
\text{low-mode suppression}
&:\ \mathrm{EXTERNAL/VERIFIED},\\
\text{high-mode suppression on escape intervals}
&:\ \mathrm{EXTERNAL/VERIFIED},\\
\text{escape-interval window domination}
&:\ \mathrm{PROVED},\\
\text{window-free same-time synchronizer}
&:\ \mathrm{PROVED},\\
\text{escape-overlap synchronization alternative}
&:\ \mathrm{PROVED},\\
\text{terminal-coverage collapse of }D_{\rm GAP}
&:\ \mathrm{PROVED},\\
\text{padded-window coercivity}
&:\ \mathrm{PROVED},\\
D_{\rm EDGE}\text{ as primitive defect}
&:\ \mathrm{REMOVED},\\
\text{dissipation-wavenumber / upper-window comparison}
&:\ \mathrm{PROVED},\\
\Lambda\in L^1
&:\ \mathrm{EXTERNAL},\\
\Lambda\in L^{5/2}\Rightarrow\text{ regularity}
&:\ \mathrm{EXTERNAL},\\
\text{Type-I core window-free synchronizer}
&:\ \mathrm{PROVED\ CONDITIONALLY},\\
\text{escape-gap temporal mismatch exclusion}
&:\ \mathrm{OPEN},\\
\text{deep dissipation-range overshoot exclusion}
&:\ \mathrm{OPEN},\\
\text{Coercive Synchronization Problem}
&:\ \mathrm{OPEN},\\
\text{Navier--Stokes regularity}
&:\ \mathrm{NOT\ PROVED}.
\end{aligned}
}
$$

---

# 49. Conclusion

The main outcome of CSP-04 is that the old moving-window defect was incorrectly typed.

At:

$$
\epsilon=\frac12,
$$

Bradshaw--Grujic give:

$$
2^{J_{\rm low}}
\sim
\frac{
B
}{
E_2
},
\qquad
2^{J_{\rm high}}
\sim
B^2.
$$

On their active escape intervals:

$$
I_{\rm BG},
$$

both exterior regions carry less than half the global critical Besov amplitude.

Therefore:

$$
\boxed{
\Phi_{1/2}(t)
\ge
\frac12
B(t).
}
$$

Any wavelength-localized middle-strain carrier anywhere in frequency gives:

$$
B(t)
\gtrsim
\sqrt{
\kappa g(t)
},
$$

hence:

$$
\boxed{
\Phi_{1/2}(t)^4
\gtrsim
\kappa^2
g(t)^2
}
$$

at the same time.

So on:

$$
I_{\rm BG},
$$

window placement itself is no longer an obstruction.

Fixed window-edge leakage is absorbed by padded windows.

The upper endpoint also reaches the Cheskidov--Shvydkoy dissipation wavenumber up to fixed dyadic constants:

$$
\boxed{
Q(t)
\le
J_{\rm high}(t)+O(1).
}
$$

Thus truly high exterior activity is already in the viscous-dominated range.

The global moving-window problem is therefore reduced from:

$$
\boxed{
\text{frequency placement mismatch}
}
$$

to:

$$
\boxed{
\textbf{escape-gap temporal mismatch}.
}
$$

The next synchronization problem is temporal.

---

# References

1. Z. Bradshaw, Z. Grujic, *Frequency localized regularity criteria for the 3D Navier–Stokes equations*, Archive for Rational Mechanics and Analysis 224 (2017), 125–133; arXiv:1501.01043v2.
2. A. Cheskidov, R. Shvydkoy, *A unified approach to regularity problems for the 3D Navier–Stokes and Euler equations: the use of Kolmogorov's dissipation range*, Journal of Mathematical Fluid Mechanics 16 (2014), 263–273; arXiv:1102.1944v2.
3. A. Cheskidov, M. Dai, *Regularity criteria for the 3D Navier–Stokes and MHD equations*, arXiv:1507.06611.
4. `NS_CSP_01_SpatialConcentration_Synchronizer_v0.1.md`.
5. `NS_CSP_02_SpatialAtom_TypeI_CoreExtraction_ParabolicPacking_v0.1.md`.
6. `NS_CSP_03_ShellAtom_SpectralVariance_ResonantTransfer_v0.1.md`.
7. `NS_RFP_12_DangerousCore_Realizability_StandardPDE_v0.1.md`.
