---
title: "Navier–Stokes C3-D: Cutoff-Flux Signatures, Helical Kernel Nonlocality Exponents, and Class-II Logarithmic Reversal"
subtitle: "Cutoff-Flux Signatures, Helical-Kernel Nonlocality Exponents, and Logarithmic Flux Reversal of Strongly Nonlocal Class-II Triads"
version: "v0.1"
date: "2026-08-14"
author: "Neo.K / EveMissLab"
language: "en-US"
status: "Theorem-style structural reduction note"
epistemic_status: "Exact single-triad algebra + standard Waleffe helical coefficient + conditional external scale-locality comparison. Does NOT prove Navier–Stokes global regularity."
---

# Navier–Stokes C3-D
# Cutoff-Flux Signatures, Helical Kernel Nonlocality Exponents, and Class-II Logarithmic Reversal

## 0. Current Positioning

C3-C has compressed the hypothetical singular production core down to:

$$
\boxed{
\text{high--high heterochiral UV pair-production}.
}
$$

and proved that for Class II:

$$
(+--),\qquad 0<k\le p\le q,
$$

strong nonlocality

$$
\chi=\frac{k}{p}\ll1
$$

results in:

$$
\boxed{
\text{quadratic pair-production tax}
+
\text{radial-drift congestion}.
}
$$

This round further asks:

> What do these massive, nearly canceling high--high exchanges actually leave behind for the energy flux crossing the spectral cutoff?

The answer is divided into three layers:

1. The large high--high turnover of Class II mostly circulates internally on the same side of the cutoff;
2. Positive Class-II pair production exhibits a **reverse-then-forward sign change** with respect to the cutoff flux;
3. Positive Classes III/IV exhibit a **uniform forward sign** across the entire scale interval of the triad.

Furthermore, the Waleffe helical coefficient itself imposes a new strong-nonlocal kernel tax:

$$
\boxed{
\mathrm{Class\ II}:O(\chi^2),
\qquad
\mathrm{Class\ III/IV}:O(\chi)
}
$$

relative to the raw cubic amplitude scale.

---

# 1. Setup and Notation

Consider a helical Fourier triad:

$$
\mathbf k+\mathbf p+\mathbf q=0,
$$

with its wavenumber magnitudes ordered as:

$$
0<k\le p\le q.
$$

modal energies:

$$
e_k,\qquad e_p,\qquad e_q.
$$

triadwise exact conservation:

$$
\dot e_k+\dot e_p+\dot e_q=0,
$$

$$
s_k k\dot e_k+s_p p\dot e_p+s_q q\dot e_q=0.
$$

Four independent sign configurations:

$$
\mathrm I:(+++),
$$

$$
\mathrm{II}:(+--),
$$

$$
\mathrm{III}:(+-+),
$$

$$
\mathrm{IV}:(++-).
$$

Global sign reversal is considered the same class.

---

# 2. Review of the Transfer Vector

There exists a scalar transfer parameter $\Theta_\tau$:

$$
\begin{pmatrix}
\dot e_k\\
\dot e_p\\
\dot e_q
\end{pmatrix}
=
\Theta_\tau
\begin{pmatrix}
s_pp-s_qq\\
s_qq-s_kk\\
s_kk-s_pp
\end{pmatrix}.
$$

Thus:

## Class II

$$
\dot e_k=(q-p)\Theta_\tau,
$$

$$
\dot e_p=-(q+k)\Theta_\tau,
$$

$$
\dot e_q=(p+k)\Theta_\tau.
$$

critical pair production:

$$
\mathcal R_{II}
=
k(q-p)\Theta_\tau.
$$

If:

$$
\mathcal R_{II}>0
$$

and $q>p$, then:

$$
\Theta_\tau>0.
$$

---

## Class III

$$
\dot e_k=-(p+q)\Theta_\tau,
$$

$$
\dot e_p=(q-k)\Theta_\tau,
$$

$$
\dot e_q=(p+k)\Theta_\tau.
$$

$$
\mathcal R_{III}
=
p(q-k)\Theta_\tau.
$$

positive pair production implies:

$$
\Theta_\tau>0.
$$

---

## Class IV

$$
\dot e_k=(p+q)\Theta_\tau,
$$

$$
\dot e_p=-(q+k)\Theta_\tau,
$$

$$
\dot e_q=(k-p)\Theta_\tau.
$$

$$
\mathcal R_{IV}
=
q(k-p)\Theta_\tau.
$$

positive pair production implies:

$$
\Theta_\tau<0.
$$

Let:

$$
\Psi_\tau=-\Theta_\tau>0.
$$

Then:

$$
\dot e_k=-(p+q)\Psi_\tau,
$$

$$
\dot e_p=(q+k)\Psi_\tau,
$$

$$
\dot e_q=(p-k)\Psi_\tau.
$$

---

# 3. Sharp Cutoff Triad Flux

For a cutoff:

$$
K>0,
$$

define the high-side energy of a single triad:

$$
E_{>K}^{(\tau)}
=
\sum_{r\in\{k,p,q\},\,r>K}
e_r.
$$

Define the triad cutoff flux:

$$
\boxed{
\Phi_\tau(K)
=
\left(
\frac{d}{dt}
E_{>K}^{(\tau)}
\right)_{\mathrm{nonlinear}}.
}
$$

This document adopts the sign convention:

$$
\Phi_\tau(K)>0
$$

indicating that energy flows through the triad **toward the higher wavenumber side above the cutoff**.

---

# 4. C3-D.1: Class-II Cutoff-Flux Signature

## Theorem 4.1

Consider a positive-pair-producing Class-II triad:

$$
(+--),
$$

$$
q>p,
$$

$$
\Theta_\tau>0.
$$

Then:

$$
\boxed{
\Phi_{II}(K)
=
\begin{cases}
0,
&
0<K<k,
\\[1mm]
-(q-p)\Theta_\tau,
&
k<K<p,
\\[1mm]
(p+k)\Theta_\tau,
&
p<K<q,
\\[1mm]
0,
&
K>q.
\end{cases}
}
$$

### Proof

- $K<k$: All three modes are on the high side; by energy conservation, the total derivative is zero.
- $k<K<p$: The high side contains $p,q$:

$$
\Phi
=
\dot e_p+\dot e_q
=
-\dot e_k
=
-(q-p)\Theta_\tau.
$$

- $p<K<q$: The high side contains only $q$:

$$
\Phi
=
\dot e_q
=
(p+k)\Theta_\tau.
$$

- $K>q$: The high side contains no modes from this triad.

$\square$

---

# 5. Sign Reversal of Class II

Therefore:

$$
\boxed{
k<K<p
\quad\Rightarrow\quad
\Phi_{II}(K)<0,
}
$$

But:

$$
\boxed{
p<K<q
\quad\Rightarrow\quad
\Phi_{II}(K)>0.
}
$$

Thus, a Class II with positive critical pair production is not "globally forward".

It possesses:

$$
\boxed{
\text{broad reverse interval}
+
\text{narrow forward window}.
}
$$

---

# 6. Geometric Thickness of the Forward Window

Class II triangle geometry:

$$
q-p\le k.
$$

Therefore, large positive high--high transfer only crosses cutoffs:

$$
K\in(p,q),
$$

with a linear width:

$$
\boxed{
q-p\le k.
}
$$

If:

$$
k\ll p\sim q,
$$

then the large forward-flux window only occupies a relative thickness of the high scale:

$$
\boxed{
\frac{q-p}{p}
\le
\frac{k}{p}
=
\chi.
}
$$

---

# 7. Boundary-Layer Localization

Fix a high cutoff:

$$
K.
$$

If the large $p\to q$ transfer of a Class-II positive triad is positive for $\Phi_{II}(K)$, it must be that:

$$
p<K<q.
$$

Also:

$$
q-p\le k.
$$

Therefore:

$$
\boxed{
K-k<p<K<q<K+k.
}
$$

So:

$$
\boxed{
\text{strongly nonlocal Class-II large forward transfer
can only be generated by a high pair falling within an }O(k)\text{ boundary layer of the cutoff}.
}
$$

This is pure Fourier geometry, without using any turbulence scaling assumptions.

---

# 8. C3-D.2: Classes III/IV Uniform Forward Signature

## Theorem 8.1

If a Class III or Class IV triad is generating positive critical pair production, then:

$$
\boxed{
\Phi_\tau(K)>0
\qquad
\forall K\in(k,q).
}
$$

### Class III

positive pair production implies:

$$
\Theta_\tau>0.
$$

When:

$$
k<K<p,
$$

$$
\Phi_{III}
=
\dot e_p+\dot e_q
=
-\dot e_k
=
(p+q)\Theta_\tau>0.
$$

When:

$$
p<K<q,
$$

$$
\Phi_{III}
=
\dot e_q
=
(p+k)\Theta_\tau>0.
$$

---

### Class IV

Let:

$$
\Psi_\tau=-\Theta_\tau>0.
$$

When:

$$
k<K<p,
$$

$$
\Phi_{IV}
=
\dot e_p+\dot e_q
=
-\dot e_k
=
(p+q)\Psi_\tau>0.
$$

When:

$$
p<K<q,
$$

$$
\Phi_{IV}
=
\dot e_q
=
(p-k)\Psi_\tau\ge0.
$$

strictly positive when nondegenerate $p>k$.

$\square$

---

# 9. Forward-Sign Classification

Therefore, positive pair-production triads possess:

$$
\boxed{
\begin{array}{c|c}
\text{Class}&\text{cutoff-flux signature}\\
\hline
II&\text{reverse on }(k,p),\ \text{forward on }(p,q)\\
III&\text{forward on all }(k,q)\\
IV&\text{forward on all }(k,q)
\end{array}
}
$$

This is stronger than the previous round's "whether the lowest mode is a donor".

Classes III/IV are not just donor-orientation forward-compatible, but rather:

$$
\boxed{
\textbf{uniformly forward across every intermediate spectral cutoff}.
}
$$

---

# 10. Log-Cutoff Integrated Flux

Define:

$$
\boxed{
\mathfrak F_\tau
=
\int_0^\infty
\Phi_\tau(K)\,
\frac{dK}{K}.
}
$$

$dK/K$ is the logarithmic scale measure.

For Class II:

$$
\boxed{
\mathfrak F_{II}
=
-(q-p)\Theta_\tau
\log\frac{p}{k}
+
(p+k)\Theta_\tau
\log\frac{q}{p}.
}
$$

---

# 11. Nonlocal Variables

Define:

$$
\chi
=
\frac{k}{p},
$$

$$
\delta
=
\frac{q-p}{p}.
$$

Triangle geometry gives:

$$
\boxed{
0<\delta\le\chi\le1
}
$$

for nonzero positive Class-II pair production.

The above equation can be rewritten as:

$$
\frac{
\mathfrak F_{II}
}{
p\delta\Theta_\tau
}
=
-
\log\frac1\chi
+
\frac{1+\chi}{\delta}
\log(1+\delta).
$$

---

# 12. C3-D.3: Log-Cutoff Reversal Threshold

For:

$$
\delta>0,
$$

there is the elementary bound:

$$
\frac{\log(1+\delta)}{\delta}
\le1.
$$

Thus:

$$
\frac{
\mathfrak F_{II}
}{
p\delta\Theta_\tau
}
\le
-
\log\frac1\chi
+
1+\chi.
$$

Let:

$$
\chi_\ast
$$

be the unique positive root of the equation:

$$
\log\frac1{\chi_\ast}
=
1+\chi_\ast
$$

Equivalently:

$$
\boxed{
\chi_\ast
=
W(e^{-1})
\approx
0.278464542761.
}
$$

where $W$ is the Lambert $W$ function.

## Theorem 12.1

If a positive Class-II triad satisfies:

$$
\boxed{
\frac{k}{p}
<
\chi_\ast
\approx0.27846,
}
$$

then:

$$
\boxed{
\mathfrak F_{II}<0.
}
$$

$\square$

---

# 13. Significance: The Scale-Averaged Direction of Strongly Nonlocal Class II is Reverse

Therefore, even if a sufficiently nonlocal positive-pair-producing Class II event possesses:

$$
p\to q
$$

a local high-end forward transfer,

when we account for all intermediate cutoffs together using the logarithmic scale measure:

$$
\boxed{
\text{reverse contribution dominates}.
}
$$

This is an exact single-triad cutoff formulation of Waleffe's observation that "large local transfers of nonlocal R-class approximately cancel, and the net effect has a reverse character."

---

# 14. Log-Cutoff Flux of Classes III/IV

By Theorem 8.1:

$$
\Phi_{III}(K)>0,
$$

$$
\Phi_{IV}(K)>0
$$

for all:

$$
K\in(k,q).
$$

Thus:

$$
\boxed{
\mathfrak F_{III}>0,
\qquad
\mathfrak F_{IV}>0.
}
$$

So under positive pair-production:

$$
\boxed{
\text{III/IV are log-scale uniformly forward},
}
$$

while sufficiently nonlocal II:

$$
\boxed{
\text{log-scale net reverse}.
}
$$

---

# 15. Compensation Obligation

If a hypothetical mechanism simultaneously requires:

1. Massive positive critical pair production;
2. Net forward energy delivery across a large scale interval;

then strongly nonlocal positive Class-II triads cannot provide both simultaneously on their own.

Their:

$$
\mathfrak F_{II}<0.
$$

Therefore, compensation must be provided by:

- Classes III/IV;
- or more local Class II;
- or other forward channels.

This document refers to this as the:

$$
\boxed{
\textbf{Forward-Flux Compensation Obligation}.
}
$$

**Important:**

This document has not yet proven that a finite-time singularity necessarily requires a positive:

$$
\mathfrak F
$$

log-integrated energy flux.

Therefore, the Compensation Obligation is a conditional structural rule for scenarios "requiring forward energy ancestry," not a global regularity theorem.

---

# 16. Waleffe Helical Coupling Coefficient

Under the standard Waleffe helical normalization, the magnitude of the single triad geometric coefficient can be written as:

$$
\boxed{
|g_{s_ks_ps_q}(k,p,q)|
=
\frac{Q}{4kpq}
\left|
s_kk+s_pp+s_qq
\right|,
}
$$

ignoring pure phase / basis normalization conventions.

Where:

$$
Q^2
=
2(k^2p^2+p^2q^2+q^2k^2)
-k^4-p^4-q^4.
$$

$Q$ is equal to a fixed multiple of the wave-number triangle area.

Therefore:

$$
Q
\le
2kp.
$$

---

# 17. C3-D.4: Helical Geometry Nonlocality Bounds

## Class II

$$
(+--):
$$

$$
|k-p-q|
=
p+q-k
\le
2q.
$$

So:

$$
\boxed{
|g_{II}|
\le
C.
}
$$

A universal $C$ can be chosen under the above normalization.

---

## Class III

$$
(+-+):
$$

$$
|k-p+q|
=
k+(q-p)
\le
2k.
$$

Therefore:

$$
\boxed{
|g_{III}|
\le
C\frac{k}{q}
\le
C\frac{k}{p}.
}
$$

---

## Class IV

$$
(++-):
$$

$$
|k+p-q|
=
k-(q-p)
\le
k.
$$

Therefore:

$$
\boxed{
|g_{IV}|
\le
C\frac{k}{q}
\le
C\frac{k}{p}.
}
$$

---

# 18. Geometric Interpretation

So under strong nonlocality:

$$
\chi=\frac{k}{p}\to0
$$

we have:

$$
\boxed{
g_{II}=O(1),
}
$$

But:

$$
\boxed{
g_{III},g_{IV}=O(\chi).
}
$$

This is exactly why individual nonlocal R/Class-II triads can have very large raw high-mode turnover:

their geometric coupling does not automatically vanish.

Conversely, the helical geometry of forward Classes III/IV inherently carries a linear nonlocality suppression.

---

# 19. Pair-Production Kernel Bound

Let:

$$
a_k
=
|u^{s_k}(\mathbf k)|,
\qquad
a_p
=
|u^{s_p}(\mathbf p)|,
\qquad
a_q
=
|u^{s_q}(\mathbf q)|.
$$

From the helical amplitude equation, the transfer scalar satisfies:

$$
|\Theta_\tau|
\le
C
|g_\tau|
a_ka_pa_q.
$$

Therefore:

## Class II

$$
|\mathcal R_{II}|
=
k(q-p)|\Theta_\tau|.
$$

From:

$$
q-p\le k,
$$

and:

$$
|g_{II}|\le C,
$$

we obtain:

$$
\boxed{
|\mathcal R_{II}|
\le
C
k^2
a_ka_pa_q.
}
$$

---

## Class III

$$
|\mathcal R_{III}|
=
p(q-k)|\Theta_\tau|.
$$

Using:

$$
q-k\le q,
$$

and:

$$
|g_{III}|
\le
C\frac{k}{q},
$$

we obtain:

$$
\boxed{
|\mathcal R_{III}|
\le
C
kp
a_ka_pa_q.
}
$$

---

## Class IV

$$
|\mathcal R_{IV}|
=
q(p-k)|\Theta_\tau|.
$$

Using:

$$
p-k\le p,
$$

and:

$$
|g_{IV}|
\le
C\frac{k}{q},
$$

we obtain:

$$
\boxed{
|\mathcal R_{IV}|
\le
C
kp
a_ka_pa_q.
}
$$

---

# 20. C3-D.5: Nonlocality Exponent Classification

Let:

$$
\chi=\frac{k}{p}.
$$

Since a strong nonlocal triad has:

$$
q\sim p.
$$

So relative to the raw cubic high-frequency scale:

$$
p^2a_ka_pa_q,
$$

we have:

$$
\boxed{
\frac{
|\mathcal R_{II}|
}{
p^2a_ka_pa_q
}
\lesssim
\chi^2,
}
$$

and:

$$
\boxed{
\frac{
|\mathcal R_{III}|
}{
p^2a_ka_pa_q
}
\lesssim
\chi,
}
$$

$$
\boxed{
\frac{
|\mathcal R_{IV}|
}{
p^2a_ka_pa_q
}
\lesssim
\chi.
}
$$

Therefore:

$$
\boxed{
\mathrm{II}:\text{ quadratic nonlocality exponent},
}
$$

$$
\boxed{
\mathrm{III/IV}:\text{ linear nonlocality exponent}.
}
$$

---

# 21. Amplitude Compensation Debt

If a sequence of increasingly nonlocal triads:

$$
\chi_n\to0
$$

is to maintain a non-vanishing normalized pair production, then the cubic amplitude product must compensate at least:

### Class II

$$
\boxed{
a_{k_n}a_{p_n}a_{q_n}
\gtrsim
\chi_n^{-2}
}
$$

relative to a fixed normalized production scale.

### Classes III/IV

At least:

$$
\boxed{
a_{k_n}a_{p_n}a_{q_n}
\gtrsim
\chi_n^{-1}.
}
$$

This is a schematic normalized statement; the true dimensional version must retain $p_n^2$.

This document refers to this as the:

$$
\boxed{
\textbf{Amplitude Compensation Debt}.
}
$$

It has not yet been closed by a finite global norm budget.

---

# 22. Relationship with the Aluie–Eyink Scale-Locality Theorem

Aluie–Eyink's study on sharp spectral filters proves:

Under the assumption of a positive inertial-range velocity scaling exponent:

$$
0<\sigma_p<1
$$

the SGS energy flux and logarithmic inter-band transfer are dominated by scale-local triads.

Specifically, for the nonlocal band contribution where $P\gg K$, their rigorous bounds contain a decay factor, such as:

$$
\left(\frac{K}{P}\right)^{2\sigma_3}.
$$

They also explicitly point out:

$$
\boxed{
\text{scale-locality is not an unconditional property of arbitrary Navier--Stokes solutions};
}
$$

the proof relies on turbulent scaling assumptions.

---

# 23. Cannot Improperly Use the Locality Theorem to Solve the Clay Problem

Therefore, we must not write:

$$
\text{Aluie--Eyink}
\Rightarrow
\text{all nonlocal blow-up routes impossible}.
$$

The correct way to use it is:

## Conditional Locality Dichotomy

Assume a hypothetical near-singular solution still satisfies a set of uniform inertial-type scaling bounds in some high-frequency window.

Then the strongly nonlocal SGS flux contribution is asymptotically negligible.

So if a blow-up route **must rely on strong nonlocality**, it requires at least:

$$
\boxed{
\text{breakdown of those scale-locality hypotheses}.
}
$$

Therefore:

$$
\boxed{
\text{nonlocal singular route}
\Rightarrow
\text{either amplitude compensation or scaling-law breakdown}.
}
$$

This is a research dichotomy, not a regularity theorem.

---

# 24. X-Integration Guards Update

Added for heterochiral events:

### G-FSIG — cutoff-flux signature

Preserve:

$$
K\mapsto\Phi_\tau(K).
$$

Cannot preserve only a single transfer amplitude.

### G-FWIN — forward-window width

Class II:

$$
\operatorname{width}_{\log}
(p,q)
=
\log(q/p)
\le
\chi.
$$

### G-LOG — log-cutoff sign

If:

$$
\chi<\chi_\ast,
$$

positive Class II must be marked:

$$
\boxed{
\mathfrak F_{II}<0.
}
$$

### G-KERNEL — helical geometry suppression

Preserve:

$$
g_{II}=O(1),
$$

$$
g_{III/IV}=O(\chi).
$$

### G-AMP — amplitude compensation

If:

$$
\chi\to0
$$

but production does not vanish, the source of amplitude growth must be explicitly recorded.

---

# 25. Survivor Map v2

## Homochiral

$$
\mathcal R=0.
$$

production source eliminated.

## Strongly Nonlocal Class II

Possesses:

- quadratic pair-production tax;
- radial-drift congestion;
- broad reverse cutoff interval;
- narrow forward window;
- $\mathfrak F_{II}<0$ when sufficiently nonlocal.

Therefore:

$$
\boxed{
\text{cannot solely serve as broad-band forward energy ancestry}.
}
$$

But may still contribute to critical pair production.

## Strongly Nonlocal Class III

Possesses:

- uniform forward cutoff sign;
- geometric $O(\chi)$ suppression;
- amplitude compensation debt.

Still survives.

## Strongly Nonlocal Class IV

Possesses:

- uniform forward cutoff sign;
- unique sign at the highest mode;
- geometric $O(\chi)$ suppression;
- amplitude compensation debt.

Remains a primary frontier survivor.

## Local / Moderately Nonlocal III/IV

Not subject to small-$\chi$ suppression.

$$
\boxed{
\textbf{CURRENT PRIMARY SURVIVOR CORE}.
}
$$

---

# 26. New Core Reduction

Through C3-D:

$$
\boxed{
\text{singular production route}
}
$$

if it exists, increasingly looks like:

$$
\boxed{
\textbf{moderately local / local heterochiral forward frontier}
}
$$

or must pay:

$$
\boxed{
\text{extreme amplitude compensation}
+
\text{scale-locality breakdown}
}
$$

to sustain a strong nonlocal route.

---

# 27. Next Topic: C3-E

After this round, the most worthy subject of study is no longer "nonlocal Class II".

Define:

$$
\boxed{
\textbf{C3-E — Local Heterochiral Frontier Coherence}.
}
$$

Question:

> When the survivor is forced into $k\sim p\sim q$ or at least bounded scale ratio heterochiral triads, can it form an infinite UV genealogy with continuously compatible phase, space, helicity, and lineage in finite time?

Here, strong-nonlocal cancellation no longer saves us.

What truly needs to be attacked:

- triad phase coherence;
- spatial concentration;
- vorticity alignment;
- branching multiplicity;
- local shell residence time;
- viscosity at comparable scale;
- repeated legality of X-Integration.

---

# 28. C3-E Proof Obligations

## E1 — Local pair-production packing

Constraint:

$$
c\le\frac{k}{p}\le1
$$

for fixed:

$$
c>0.
$$

Establish dyadic shell pair-production:

$$
\mathcal R_q^{\rm loc}.
$$

Investigate whether blow-up requires:

$$
\sum_q
\int
[\mathcal R_q^{\rm loc}]_+dt
=
\infty.
$$

## E2 — Phase coherence duration

Helical transfer contains:

$$
\Re
\left(
g_\tau
u_k u_p u_q
\right).
$$

Large amplitude does not imply positive production.

Requires phase alignment to persist over enough time intervals.

## E3 — Local residence-time bound

If:

$$
k\sim p\sim q\sim\lambda,
$$

viscous time:

$$
\tau_\nu
\sim
(\nu\lambda^2)^{-1}.
$$

Investigate whether positive pair-production coherence must be completed within an:

$$
O(\lambda^{-2})
$$

window.

## E4 — Branching congestion

The number of local triads is massive.

But to form a source-preserving singular genealogy, one cannot rely solely on "having many triads".

It requires:

$$
\boxed{
\text{parent identity}
+
\text{child identity}
+
\text{sign}
+
\text{phase}
+
\text{space overlap}
}
$$

to be simultaneously glueable generation by generation.

## E5 — X non-collapse

Investigate whether the aggregation of a massive number of local triads into a scalar flux collapses genealogy differences.

X-Integration requires:

$$
\boxed{
\text{aggregate flux}
\neq
\text{source-certified persistent chain}.
}
$$

This may become a new proof barrier, or it may be the location to find an obstruction.

---

# 29. Formal Status

$$
\boxed{
\begin{aligned}
\text{Class-II cutoff-flux signature}
&:\ \mathrm{PROVED},\\
\text{III/IV uniform forward signature}
&:\ \mathrm{PROVED},\\
\text{Class-II boundary-layer forward window}
&:\ \mathrm{PROVED},\\
\text{Class-II log-cutoff reversal threshold}
&:\ \mathrm{PROVED},\\
\chi_\ast=W(e^{-1})
&:\ \mathrm{PROVED},\\
\text{Waleffe geometry nonlocal bounds}
&:\ \mathrm{PROVED\ from\ standard\ coefficient},\\
\text{II quadratic kernel exponent}
&:\ \mathrm{PROVED},\\
\text{III/IV linear kernel exponent}
&:\ \mathrm{PROVED},\\
\text{amplitude compensation debt}
&:\ \mathrm{DERIVED},\\
\text{unconditional aggregate nonlocal suppression}
&:\ \mathrm{OPEN},\\
\text{local heterochiral frontier obstruction}
&:\ \mathrm{OPEN}.
\end{aligned}
}
$$

---

# 30. Conclusion

C3-C has pointed out that the Class II strong nonlocal route is extremely expensive.

C3-D further proves:

$$
\boxed{
\text{positive Class II is reverse with respect to the cutoff flux for }k<K<p,
}
$$

while:

$$
\boxed{
\text{only the narrow window }p<K<q\text{ is forward}.
}
$$

Even when:

$$
\frac{k}{p}
<
W(e^{-1})
\approx0.27846,
$$

its logarithmically scale-integrated energy flux must be:

$$
\boxed{
\mathfrak F_{II}<0.
}
$$

In contrast, positive Classes III/IV:

$$
\boxed{
\Phi(K)>0
\quad
\forall K\in(k,q).
}
$$

Therefore, III/IV are the true broad-band forward-compatible pair-production classes.

On the other hand, Waleffe helical geometry tells us:

$$
\boxed{
\text{all strong-nonlocal forward classes still pay at least an }O(k/p)\text{ kernel tax}.
}
$$

Thus, the survivor is once again compressed toward:

$$
\boxed{
\textbf{local / moderately local heterochiral forward frontier}.
}
$$

The next round formally transitions to:

$$
\boxed{
\textbf{C3-E — Local Heterochiral Frontier Coherence}.
}
$$

---

# References

1. F. Waleffe, *The nature of triad interactions in homogeneous turbulence*, Physics of Fluids A 4 (1992), 350–363.
2. F. Waleffe, *Inertial transfers in the helical decomposition*, Physics of Fluids A 5 (1993).
3. H. Aluie, G. L. Eyink, *Localness of energy cascade in hydrodynamic turbulence, I. Smooth coarse-graining*, arXiv:0909.2386.
4. H. Aluie, G. L. Eyink, *Localness of energy cascade in hydrodynamic turbulence, II. Sharp spectral filter*, arXiv:0909.2451.
5. L. Biferale, E. S. Titi, *On the Global Regularity of a Helical-decimated Version of the 3D Navier–Stokes Equations*, arXiv:1303.1215.
6. G. Sahoo, L. Biferale, *Disentangling the triadic interactions in Navier-Stokes equations*, arXiv:1510.09006.

# Internal Dependencies

- `NS_C1_UV_Replenishment_Chain_v0.2.md`
- `NS_C2_Critical_Toll_Spike_Packing_v0.3.md`
- `NS_C3A_Conservation_Criticality_Helical_Pair_Production_v0.1.md`
- `NS_C3B_BiHelical_Equalization_UniqueSign_UV_Escape_v0.1.md`
- `NS_C3C_ClassII_Nonlocality_Tax_Radial_Congestion_v0.1.md`
- `True ETN / Infinite-Dimensional Tension Field`
- `X_Integral_Unified_Program_v0.2.md`

Next:

$$
\boxed{
\textbf{C3-E — Local Heterochiral Frontier Coherence}
}
$$