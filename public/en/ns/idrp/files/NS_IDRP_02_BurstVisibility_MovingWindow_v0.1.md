---
title: "Navier–Stokes Impulsive Defect Recurrence Program 02: Source-Impulse Visibility, Filtered Trace Variation, PFET Burst Coupling, Logarithmic Atom Thickening and Moving-Window Depletion"
short_title: "NS-IDRP 02"
series: "Navier–Stokes Impulsive Defect Recurrence Program"
cycle: "IX"
version: "v0.1"
date: "2026-08-16"
author: "Neo.K / EveMissLab"
language: "en"
status: "Burst-visibility compiler / logarithmic packet-or-burst thickening / PFET realization frontier"
epistemic_status: "Advances the Burst Visibility Problem. Starting from the exact localized filtered-enstrophy identity, proves a filtered mechanism-burst theorem: if a selected filtered-enstrophy atom loses a fixed amount on a window, then the loss is paid by diffusion, negative near-field stretching, far-field strain, commutator forcing, or localization. Inserting the external derivative-compatible commutator estimate converts the commutator branch into a scale-invariant critical increment defect modulo diffusion/localization. Thus rapid filtered-trace loss is not mechanism-invisible. Combines this with the DCRP logarithmic far-field atom floor to prove a full-parabolic-window packet-or-burst theorem: every selected logarithmic FAR atom either persists as a scale-critical filtered-enstrophy spacetime packet of the same logarithmic amplitude or generates an equally large mechanism burst on that same full parabolic window. Proves an abstract dual-source burst amplification theorem and applies it to velocity/vorticity nonlinear forcing: under uniform dual-profile cost, fixed causal fresh-source pairing on shrinking disjoint windows forces an L_t^{4/3} weak-topology source-action burst, with a global energy-class packing law. Defines Burst-to-Defect Realization (BDR) as the missing non-tautological bridge from source/mechanism bursts into the native finite-window NS defect quotient. Once BDR holds, the external finite-window combined observability constant gives a quantitative PFET lower bound; if the primitive channels are removed, the external trace-cost theorem yields controlled trace exactification or a relative left-singular invisible burst residual. Proves a conditional amplitude-weighted moving-window depletion compiler and a logarithmic-series threshold: if burst amplitude b_n is comparable to n^{-2/3}, depletion weights behave like n^{-s}, observability loss like n^{gamma}, and an unnormalized burst-depletion law with exponent q holds, then the burst series diverges when s+q(2/3+gamma)<=1 (with the expected logarithmic caveat at equality). Under the external exponential/logarithmically-admissible window growth model, the corresponding strict condition is s+2q/3+q C alpha<1. This shows logarithmic FAR bursts can only close through sufficiently linear/low-loss depletion; the general BDR/PFET bridge and invisible-burst exclusion remain open. No Impulsive Diffuse Recurrence exclusion, Forest Coercive Budget, Finite Forest Obstruction, atomic CN3, or Navier-Stokes regularity is proved."
canonical_source: "UTF-8 Markdown"
---

# Navier–Stokes Impulsive Defect Recurrence Program 02

# Source-Impulse Visibility, Filtered Trace Variation, PFET Burst Coupling, Logarithmic Atom Thickening and Moving-Window Depletion

## 0. Positioning of this paper

IDRP-01 proved two sharply different temporal facts.

First, in the strong Type-I critical branch, external concentration theory already gives full parabolic-thickness state packets.

Second, for a generic energy-class spectral atom, the universal:

$$
L_t^{4/3}\dot H_x^{-1}
$$

temporal action gives only a very subparabolic persistence floor.

The missing problem was:

$$
\boxed{\textbf{BVP — Burst Visibility Problem}.}
$$

The present paper shows that for **filtered vorticity traces**, rapid loss is not invisible at the mechanism-ledger level.

It also formulates the remaining non-tautological bridge to PFET moving-window observability.

---

# 1. Exact filtered enstrophy identity

Let:

$$
U_{\ell}=\varphi_{\ell}*u,
\qquad
\Omega_{\ell}=\nabla\times U_{\ell}.
$$

For a nonnegative localized cutoff:

$$
\chi,
$$

the exact external filtered-enstrophy identity is:

$$
\boxed{
E_{\chi}(s_1)
-
E_{\chi}(s_0)
+
P_{\chi}
=
V_{\chi}^{near}
+
V_{\chi}^{rem}
+
R_{\chi}
+
L_{\chi}.
}
$$

Here:

$$
E_{\chi}(t)
=
\frac r2
\int
\chi
|\Omega_{\ell}|^2dx,
$$

$$
P_{\chi}
=
r
\iint
\chi
|\nabla\Omega_{\ell}|^2,
$$

and the remaining terms are:

- near-field stretching;
- far/remainder strain;
- commutator forcing;
- cutoff/transport localization.

### Status

$$
\boxed{\mathrm{EXTERNAL/EXACT}.}
$$

---

# 2. Trace drop

Define the filtered trace loss:

$$
\boxed{
\Delta E_{\chi}
=
E_{\chi}(s_0)-E_{\chi}(s_1).
}
$$

Suppose:

$$
\boxed{\Delta E_{\chi}\ge a>0.}
$$

Write:

$$
V_{\chi}^{near}
=
(V_{\chi}^{near})_+
-
(V_{\chi}^{near})_-.
$$

---

# 3. CIV/IX-2.1 — Filtered Mechanism-Burst Visibility

## Theorem 3.1

Under Sections 1--2:

$$
\boxed{
a
\le
P_{\chi}
+
(V_{\chi}^{near})_-
+
|V_{\chi}^{rem}|
+
|R_{\chi}|
+
|L_{\chi}|.
}
$$

### Proof

The exact identity gives:

$$
\Delta E_{\chi}
=
P_{\chi}
-
V_{\chi}^{near}
-
V_{\chi}^{rem}
-
R_{\chi}
-
L_{\chi}.
$$

Use:

$$
-
V_{\chi}^{near}
\le
(V_{\chi}^{near})_-,
$$

and absolute values for the remaining signed terms.

$\square$

---

# 4. Interpretation

A rapidly disappearing filtered atom is not dynamically invisible.

Its loss is paid by at least one of:

$$
\boxed{\text{DIFFUSION}}
$$

$$
\boxed{\text{NEGATIVE NEAR-FIELD STRETCHING}}
$$

$$
\boxed{\text{FAR-FIELD}}
$$

$$
\boxed{\text{COMMUTATOR}}
$$

or:

$$
\boxed{\text{LOCALIZATION}.}
$$

The first two are dynamically favorable depletion channels.

The last three are explicit residual/mechanism bursts.

---

# 5. Good-depletion versus residual-burst split

Fix:

$$
0<\theta<1.
$$

If:

$$
\boxed{
P_{\chi}
+
(V_{\chi}^{near})_-
\ge
\theta a,
}
$$

then a fixed fraction of the trace loss is paid by good depletion.

Otherwise:

$$
\boxed{
|V_{\chi}^{rem}|
+
|R_{\chi}|
+
|L_{\chi}|
\ge
(1-\theta)a.
}
$$

Therefore one residual channel has magnitude at least:

$$
\boxed{(1-\theta)a/3.}
$$

---

# 6. External commutator insertion

At dyadic scale:

$$
r_k=2^{-k},
\qquad
\ell_k=\sigma_f r_k,
$$

the external filtered theory gives:

$$
\boxed{
F_k^{com}
\le
\eta P_k
+
C_{\eta,\varphi}
\widetilde{\mathcal S}_k^{(p)}
+
L_{k,inc}^{com},
}
$$

for:

$$
p\in[2,4].
$$

The quantity:

$$
\widetilde{\mathcal S}_k^{(p)}
$$

is the derivative-compatible scale-invariant increment defect.

### Status

$$
\boxed{\mathrm{EXTERNAL/PROVED}.}
$$

---

# 7. CIV/IX-2.2 — Filtered Burst Reduction to Critical Increment Defect

## Theorem 7.1

Suppose:

$$
\Delta E_k\ge a
$$

on one admissible dyadic filtered slab.

Then:

$$
\boxed{
a
\le
(1+\eta)P_k
+
(V_k^{near})_-
+
|V_k^{far}|
+
C_{\eta,\varphi}
\widetilde{\mathcal S}_k^{(p)}
+
L_k
+
L_{k,inc}^{com}.
}
$$

Consequently, if diffusion, negative near-field stretching, far-field work, and localization together contribute at most:

$$
(1-\vartheta)a
$$

for some:

$$
\vartheta>0,
$$

then:

$$
\boxed{
\widetilde{\mathcal S}_k^{(p)}
\ge
c_{\eta,\varphi}
\vartheta a.
}
$$

### Meaning

A filtered trace burst which is not already paid by good depletion, FAR, or localization forces a scale-critical increment defect.

$\square$

---

# 8. Partial closure of filtered BVP

For filtered vorticity traces:

$$
\boxed{\text{rapid atom loss}}
$$

has now been compiled into explicit mechanism channels.

Thus:

$$
\boxed{\textbf{filtered BVP is closed at the mechanism-ledger layer}.}
$$

It is **not** yet closed at the PFET moving-window layer.

---

# 9. Source impulse

Let:

$$
X
$$

be a Banach space and:

$$
X^\ast
$$

its dual.

Let:

$$
F\in L^{p}(I;X),
\qquad
\Phi\in L^{p'}(I;X^\ast),
$$

where:

$$
1<p<\infty,
\qquad
1/p+1/p'=1.
$$

Assume a causal/source pairing:

$$
\boxed{
\int_I
|
\langle
F(t),
\Phi(t)
\rangle
|dt
\ge
J.
}
$$

---

# 10. CIV/IX-2.3 — Dual Source-Burst Amplification

## Theorem 10.1

If:

$$
\boxed{
\|\Phi\|_{L^{p'}(I;X^\ast)}
\le
K
|I|^{1/p'},
}
$$

then:

$$
\boxed{
\int_I
\|F(t)\|_X^pdt
\ge
\frac{J^p}{K^p|I|^{p-1}}.
}
$$

### Proof

Hölder gives:

$$
J
\le
\|F\|_{L^p(I;X)}
\|\Phi\|_{L^{p'}(I;X^\ast)}
\le
K
|I|^{1/p'}
\|F\|_{L^p(I;X)}.
$$

Raise to the:

$$
p
$$

power.

$\square$

---

# 11. The critical $4/3$ source exponent

Set:

$$
p=\frac43,
\qquad
p'=4.
$$

Then:

$$
\boxed{
\int_I
\|F(t)\|_X^{4/3}dt
\ge
\frac{J^{4/3}}{K^{4/3}|I|^{1/3}}.
}
$$

Thus shortening the source window forces the same:

$$
|I|^{-1/3}
$$

burst exponent found in the spectral temporal-action theorem of IDRP-01.

---

# 12. Velocity nonlinear forcing

Let:

$$
\boxed{
\mathcal N
=
-\mathbb P
\nabla\cdot
(u\otimes u).
}
$$

The energy-class estimate from the prior CFOP/FCBP audit gives:

$$
\boxed{
\int_0^T
\|\mathcal N(t)\|_{\dot H^{-1}}^{4/3}dt
<
\infty.
}
$$

Dyadic projection preserves this bound up to a universal multiplier constant.

---

# 13. Vorticity nonlinear forcing

Let:

$$
\boxed{
\mathcal G
=
-\nabla\times\mathcal N.
}
$$

Then:

$$
\boxed{
\int_0^T
\|\mathcal G(t)\|_{\dot H^{-2}}^{4/3}dt
<
\infty.
}
$$

This is the natural weak topology for vorticity-source action at the energy level.

---

# 14. CIV/IX-2.4 — Disjoint Source-Burst Packing

## Theorem 14.1

Let:

$$
I_n
$$

be pairwise-disjoint intervals.

Suppose:

$$
F_n=P_{k_n}\mathcal N
$$

or the corresponding projected vorticity forcing, and:

$$
\int_{I_n}
|
\langle
F_n,
\Phi_n
\rangle
|dt
\ge
J_n.
$$

Assume:

$$
\|\Phi_n\|_{L^4(I_n;X^\ast)}
\le
K_n|I_n|^{1/4}.
$$

Then:

$$
\boxed{
\sum_n
\frac{J_n^{4/3}}{K_n^{4/3}|I_n|^{1/3}}
<
\infty.
}
$$

### Meaning

Fresh-source impulses can become arbitrarily strong only by paying at least one of:

- shrinking source pairing amplitude;
- growing dual cost;
- loss of time disjointness;
- or finite total action.

$\square$

---

# 15. Causal fresh-renewal specialization

Suppose the corrected causal ledger gives:

$$
\boxed{J_n\ge\sigma A_n}
$$

for a fixed inheritance deficit:

$$
\sigma>0.
$$

Then:

$$
\boxed{
\sum_n
\frac{A_n^{4/3}}{K_n^{4/3}|I_n|^{1/3}}
<
\infty
}
$$

up to the fixed factor:

$$
\sigma^{-4/3}.
$$

Thus the IDR-S branch has a true weak-source action packing law.

---

# 16. Source-action visibility is not PFET visibility

The nonlinear source may be large while one signed kinetic-energy-work pairing vanishes.

Therefore:

$$
\boxed{
\text{large source action}
\not\Rightarrow
\text{single signed work detector}.
}
$$

This is consistent with the FCBP single-energy-work no-go.

The correct target remains combined finite-window observability.

---

# 17. Burst-to-Defect Realization

Define:

$$
\boxed{\textbf{BDR — Burst-to-Defect Realization}.}
$$

For a burst package:

$$
\mathfrak B_W
$$

on a finite window:

$$
W,
$$

BDR asks for a native NS-realizable cleaned defect:

$$
d_W\in Y_W^{NS}
$$

such that:

$$
\boxed{
\|d_W\|_{Y_W}
\ge
c_B
\mathfrak b_W
-
\varepsilon_W,
}
$$

where:

$$
\mathfrak b_W
$$

is the burst amplitude and:

$$
\varepsilon_W
$$

is an explicit residual.

### Safety

The burst amplitude may not be copied into an artificial detector coordinate.

BDR must be non-tautological.

---

# 18. External combined observability

For:

$$
d\in Y_W^{NS},
$$

the external finite-window observability constant is:

$$
\boxed{
M_W
=
\sup_{0\neq d\in Y_W^{NS}}
\frac{\|d\|_{Y_W}}{\mathsf O_W(d)},
}
$$

where:

$$
\mathsf O_W
$$

is the combined pressure/flux/energy/trace observed strength.

Whenever:

$$
M_W<\infty,
$$

$$
\boxed{
\mathsf O_W(d)
\ge
\frac{\|d\|_{Y_W}}{M_W}.
}
$$

### Status

$$
\boxed{\mathrm{EXTERNAL/FINITE\mbox{-}WINDOW}.}
$$

---

# 19. CIV/IX-2.5 — BDR-to-PFET Visibility Compiler

## Theorem 19.1

Assume BDR on:

$$
W.
$$

If:

$$
M_W<\infty,
$$

then:

$$
\boxed{
\mathsf O_W(d_W)
\ge
\frac{c_B\mathfrak b_W-\varepsilon_W}{M_W}.
}
$$

If:

$$
\varepsilon_W
\le
\frac12c_B\mathfrak b_W,
$$

then:

$$
\boxed{
\mathsf O_W(d_W)
\ge
\frac{c_B}{2M_W}\mathfrak b_W.
}
$$

$\square$

---

# 20. Residual trace exactification

Suppose pressure, flux, and energy reductions leave a residual:

$$
g_W
$$

with native scale:

$$
\rho_W.
$$

The external trace-cost theorem gives:

$$
\boxed{\text{controlled combined trace cost}}
$$

or:

$$
\boxed{\text{relative left-singular invisible failure}.}
$$

In particular, if:

$$
\|g_W\|\lesssim\rho_W,
$$

failure of a uniform combined estimate produces normalized dual directions whose pressure/flux/energy/trace observations vanish relative to the residual pairing.

### Status

$$
\boxed{\mathrm{EXTERNAL/PROVED\ FINITE\mbox{-}WINDOW\ ALTERNATIVE}.}
$$

---

# 21. Burst amplitude can be the relative residual scale

For a decaying burst sequence:

$$
\mathfrak b_n\to0,
$$

one may set the branch-native relative scale:

$$
\boxed{\rho_n\asymp\mathfrak b_n}
$$

**only if** the BDR/residual construction proves:

$$
\|g_n\|\lesssim\mathfrak b_n.
$$

Then amplitude decay does not make the residual meaningless.

It becomes a **relative PFET trace-obstruction problem**.

---

# 22. Logarithmic FAR atom

DCRP-04 proved a selected-time filtered-vorticity atom:

$$
\boxed{
a_k
\gtrsim
\left[
1+\log(C/r_k)
\right]^{-2/3}
}
$$

whenever the annular FAR output is order one.

For dyadic:

$$
r_k=2^{-k},
$$

this is:

$$
\boxed{a_k\gtrsim(k+1)^{-2/3}}
$$

up to harmless constants.

---

# 23. Full parabolic window

Let:

$$
I_k
$$

be the full:

$$
r_k^2
$$

filtered slab.

At the selected atom time:

$$
t_k^\ast,
$$

let the localized filtered-enstrophy trace satisfy:

$$
\boxed{E_k(t_k^\ast)\ge c a_k.}
$$

Apply the trace persistence theorem over the remaining admissible full-scale window, using a symmetric or forward/backward version compatible with the location of:

$$
t_k^\ast.
$$

---

# 24. CIV/IX-2.6 — Logarithmic FAR Packet-or-Burst Thickening

## Theorem 24.1

Relative to the DCRP-04 FAR atom and an admissible full parabolic filtered slab, one of the following occurs.

### filtered packet

There exists a subwindow of normalized thickness bounded below by a fixed geometric constant on which:

$$
E_k(t)\ge c a_k.
$$

Consequently:

$$
\boxed{
r_k^{-1}
\iint
\chi_k
|\Omega_k|^2
\gtrsim
a_k.
}
$$

### mechanism burst

The integrated mechanism ledger on the full scale window satisfies:

$$
\boxed{
P_k
+
(V_k^{near})_-
+
|V_k^{far}|
+
C
\widetilde{\mathcal S}_k^{(p)}
+
L_k
+
L_{k,inc}^{com}
\gtrsim
a_k.
}
$$

### Meaning

The selected logarithmic FAR atom cannot remain a purely instantaneous object.

It becomes a full-window packet or a full-window mechanism burst of the same logarithmic order.

$\square$

---

# 25. Improvement over generic energy persistence

IDRP-01 energy-class spectral regularity gave only an:

$$
r^6
$$

scale persistence floor.

Theorem 24.1 uses the exact filtered Navier--Stokes balance and works on the full:

$$
r_k^2
$$

window.

Thus branch-specific structure recovers the four powers of:

$$
r
$$

which generic temporal regularity could not.

### Safety

The output amplitude:

$$
a_k
$$

still decays logarithmically.

Full time thickness does not imply fixed native separation.

---

# 26. Amplitude-aware depletion model

Suppose a burst sequence is BDR-realized as:

$$
d_n
$$

and a selected budget obeys an **unnormalized** depletion law:

$$
\boxed{
\mathscr B_n-\mathscr B_{n+1}
\ge
c
\lambda_n
\mathsf O_n(d_n)^q
-
e_n,
}
$$

with:

$$
\sum_ne_n<\infty.
$$

### Safety

This is a new conditional burst-depletion hypothesis.

The external moving-window theorem is formulated for normalized extracted defects with a fixed extraction lower bound.

The unnormalized law is not silently imported from that theorem.

---

# 27. CIV/IX-2.7 — Amplitude-Weighted Burst Depletion Compiler

## Theorem 27.1

Assume:

$$
\|d_n\|
\ge
c_B b_n,
$$

$$
M_n<\infty,
$$

and Section 26.

Then:

$$
\boxed{
\mathscr B_n-\mathscr B_{n+1}
\ge
c'
\lambda_n
b_n^q
M_n^{-q}
-
e_n.
}
$$

Therefore, if:

$$
\boxed{
\sum_n
\lambda_n
b_n^q
M_n^{-q}
=
\infty,
}
$$

the burst branch cannot persist indefinitely.

$\square$

---

# 28. Polynomial logarithmic threshold

Assume:

$$
\boxed{b_n\gtrsim(n+2)^{-\beta},}
$$

$$
\boxed{\lambda_n\gtrsim(n+2)^{-s},}
$$

and:

$$
\boxed{M_n\lesssim(n+2)^\gamma.}
$$

Then:

$$
\lambda_n
b_n^q
M_n^{-q}
\gtrsim
(n+2)^{-s-q(\beta+\gamma)}.
$$

---

# 29. CIV/IX-2.8 — Logarithmic Burst Series Threshold

## Theorem 29.1

Under Section 28, the amplitude-weighted depletion series diverges if:

$$
\boxed{s+q(\beta+\gamma)\le1.}
$$

For the DCRP logarithmic FAR amplitude:

$$
\beta=\frac23,
$$

the threshold is:

$$
\boxed{
s+q\left(\frac23+\gamma\right)\le1.
}
$$

### Consequences

For:

$$
q=1,
$$

one needs:

$$
\boxed{s+\gamma\le\frac13.}
$$

For:

$$
q\ge\frac32,
$$

there is no room with:

$$
s,\gamma\ge0
$$

except degenerate borderline cases.

$\square$

---

# 30. External exponential/logarithmic window growth

The external moving-window framework allows:

$$
\boxed{
M_n
\le
C
N_n^a
\exp(CN_n^b),
}
$$

and logarithmically admissible windows with:

$$
\boxed{N_n^b\le\alpha\log(n+2).}
$$

Thus:

$$
M_n^{-q}
\gtrsim
(n+2)^{-qC\alpha}
(\log(n+2))^{-aq/b}.
$$

---

# 31. CIV/IX-2.9 — Amplitude-Weighted Logarithmic Admissibility

## Theorem 31.1

Assume the amplitude-aware depletion model of Section 26, the DCRP burst amplitude:

$$
b_n\gtrsim(n+2)^{-2/3},
$$

the external growth form of Section 30, and:

$$
\lambda_n\gtrsim(n+2)^{-s}.
$$

Then the depletion series diverges whenever:

$$
\boxed{
s+\frac{2q}{3}+qC\alpha<1.
}
$$

At equality, divergence additionally depends on the logarithmic power:

$$
aq/b.
$$

### Meaning

The logarithmic FAR packet-or-burst is compatible with moving-window depletion only when the depletion law is sufficiently close to linear and the observation/window loss is mild enough.

$\square$

---

# 32. Comparison with external normalized moving-window theory

The external theorem assumes a fixed extracted defect norm:

$$
\|d_{n_k}\|\ge c_0>0
$$

and applies depletion to:

$$
\widehat d_{n_k}.
$$

The logarithmic FAR amplitude:

$$
b_n\to0
$$

does not automatically satisfy that extraction hypothesis.

Therefore Theorems 27.1--31.1 do not close the external moving-window theorem by themselves.

They identify the exact amplitude-aware extension needed for IDRP.

---

# 33. Relative invisible burst normal form

If BDR produces a residual of size:

$$
\rho_n\asymp b_n
$$

but combined observability degenerates relative to that scale, the external trace-cost theorem permits a relative left-singular invisible residual.

Define:

$$
\boxed{\textbf{RIB — Relative Invisible Burst}.}
$$

A RIB sequence has:

- burst-native residual scale:
  $$
  \rho_n\to0;
  $$
- nontrivial residual pairing relative to:
  $$
  \rho_n;
  $$
- pressure/flux/energy/trace dual observations vanishing relative to that pairing.

This is the natural surviving IDRP obstruction after burst amplitude is allowed to decay.

---

# 34. Filtered BVP status

At the mechanism level:

$$
\boxed{
\text{filtered BVP}
:
\mathrm{SUBSTANTIALLY\ CLOSED}.
}
$$

Rapid filtered trace loss forces explicit mechanism activity.

At the PFET level:

$$
\boxed{
\text{BDR/PFET BVP}
:
\mathrm{OPEN}.
}
$$

The remaining task is native burst-to-defect realization and relative invisible-burst exclusion.

---

# 35. Source impulse status

Source bursts have a genuine:

$$
L_t^{4/3}
$$

weak-topology packing law.

But large weak source action does not, by itself, imply pressure-flux-energy-trace visibility.

The missing theorem is again BDR or an equivalent source-to-audit transfer theorem.

The 2026 forced Navier--Stokes quantitative theory of Barker--Popkin shows that critical quantitative propagation can incorporate forcing under additional critical-bound/forcing hypotheses, but the forcing is itself a nontrivial source of large-scale loss.

This is useful calibration, not a universal BDR theorem.

---

# 36. IDRP-02 surviving temporal obstruction

After this paper, a recurrent impulsive branch must enter at least one of:

$$
\boxed{\textbf{RIB}}
$$

— relative invisible burst;

$$
\boxed{\textbf{AMP}}
$$

— burst amplitude decays too fast for the available depletion weights;

$$
\boxed{\textbf{OBS}}
$$

— moving-window observability constants grow too fast;

$$
\boxed{\textbf{BDR}}
$$

— burst-to-native-defect realization fails;

$$
\boxed{\textbf{RES}}
$$

— localization/exterior/representation residual remains unabsorbed.

This is a narrower temporal normal form than the original IDR class.

---

# 37. Strongest positive result

The main positive result is:

$$
\boxed{
\textbf{
rapid filtered trace loss is mechanism-visible,
and logarithmic FAR atoms are full-window packet-or-burst objects.
}
}
$$

Thus the temporal obstruction can no longer hide solely in instantaneous filtered trace loss.

---

# 38. Strongest remaining gap

The missing bridge is not temporal regularity.

It is:

$$
\boxed{
\textbf{
mechanism/source burst}
\Longrightarrow
\textbf{
native PFET defect with effective relative observability}.
}
}
$$

That is BDR plus relative moving-window rigidity.

---

# 39. Next paper

The next paper should attack the relative invisible burst directly:

$$
\boxed{
\textbf{
NS-IDRP 03 —
Relative Invisible Burst Kernels,
Burst-to-Defect Realization,
Source/Trace Dual Compatibility,
Amplitude-Normalized Audit
and Temporal Rigidity
}.
}
$$

Primary tasks:

1. construct a non-tautological BDR map for filtered/source bursts;
2. compare ANP source duals with PFET adjoint-trace duals;
3. normalize decaying burst residuals without copying the burst amplitude;
4. classify the relative left-singular kernel;
5. test whether model-cone/increment channels eliminate relative invisibility;
6. derive an amplitude-normalized depletion law or prove a no-go;
7. decide whether Cycle IX can exclude recurrent impulsive bursts.

---

# 40. Formal status ledger

$$
\boxed{
\begin{aligned}
\text{Filtered Mechanism-Burst Visibility}
&:\ \mathrm{PROVED},\\
\text{Filtered Burst to Critical Increment}
&:\ \mathrm{PROVED\ USING\ EXTERNAL\ COMMUTATOR\ ESTIMATE},\\
\text{Dual Source-Burst Amplification}
&:\ \mathrm{PROVED},\\
\text{Disjoint Source-Burst Packing}
&:\ \mathrm{PROVED},\\
\text{BDR-to-PFET Visibility}
&:\ \mathrm{PROVED\ CONDITIONAL},\\
\text{Logarithmic FAR Packet-or-Burst Thickening}
&:\ \mathrm{PROVED\ RELATIVE\ TO\ DCRP\ ATOM/EXTERNAL\ BALANCE},\\
\text{Amplitude-Weighted Burst Depletion}
&:\ \mathrm{PROVED\ CONDITIONAL},\\
\text{Logarithmic Burst Series Threshold}
&:\ \mathrm{PROVED\ CONDITIONAL},\\
\text{Amplitude-Weighted Logarithmic Admissibility}
&:\ \mathrm{PROVED\ CONDITIONAL},\\
\text{Burst-to-Defect Realization}
&:\ \mathrm{OPEN},\\
\text{Relative Invisible Burst exclusion}
&:\ \mathrm{OPEN},\\
\text{Impulsive Diffuse Recurrence exclusion}
&:\ \mathrm{OPEN},\\
\text{Forest Coercive Budget}
&:\ \mathrm{OPEN},\\
\text{Finite Forest Obstruction}
&:\ \mathrm{OPEN},\\
CN3_{\rm Atomic}
&:\ \mathrm{OPEN},\\
\text{Navier--Stokes regularity}
&:\ \mathrm{NOT\ PROVED}.
\end{aligned}
}
$$

---

# 41. Conclusion

IDRP-02 partially solves the Burst Visibility Problem.

The exact filtered-vorticity balance shows that rapid loss of a selected filtered atom cannot occur without explicit mechanism activity.

After derivative-compatible commutator insertion, a disappearing atom is paid by good depletion, far-field activity, a scale-critical increment defect, or localization.

The logarithmic FAR atoms from DCRP therefore admit a full-parabolic-window dichotomy: either they persist as filtered-enstrophy packets or they generate mechanism bursts of the same logarithmic order.

Fresh causal-source impulses have an analogous quantitative structure.

Duality converts fixed source pairing on short windows into an:

$$
L_t^{4/3}
$$

weak-source action burst, and disjoint bursts satisfy a global energy-class packing law.

The remaining difficulty is no longer showing that a burst exists.

It is showing that the burst has a **native PFET realization**.

Once a non-tautological burst-to-defect map exists, finite-window combined observability gives a direct observed-strength lower bound.

After pressure/flux/energy removal, the external trace-cost machinery further reduces failure to a relative left-singular invisible burst.

The logarithmic amplitude makes this distinction essential.

A full-window burst of size:

$$
k^{-2/3}
$$

is not a fixed defect.

An amplitude-aware depletion law would close it only under a sharp series condition, for example:

$$
s+q(2/3+\gamma)\le1
$$

in the polynomial-loss model.

Thus the new frontier is precise:

$$
\boxed{
\textbf{
relative burst realization
+
relative PFET rigidity.
}
}
$$

That is IDRP-03.

---

# References

1. R. Yu, *Filtered Vortex Stretching and Subgrid Defects for the Three-Dimensional Navier--Stokes Equations*, arXiv:2606.27560.
2. R. Yu, *Invisible Defect Cascades for Navier--Stokes Regularity*, arXiv:2606.12756.
3. R. Yu, *Coarse-Grained Resolution and Pressure--Flux Work Depletion for Navier--Stokes CKN Badness*, arXiv:2606.25322.
4. R. Yu, *Finite-Window Recursive Audit Chains for Navier--Stokes Generated Packages*, arXiv:2606.20899.
5. R. Yu, *Critical Ledgers and Scale-Defect Cascades for Navier--Stokes*, arXiv:2606.13887.
6. T. Barker, H. Popkin, *Quantitative estimates for the forced Navier--Stokes equations and applications*, arXiv:2602.09951.
7. `NS_IDRP_01_ImpulsePersistence_TraceThickening_v0.1.md`.
8. `NS_DCRP_CYCLE_VIII_HANDOFF_v1.0.md`.