---
title: "Navier–Stokes C3-C: Class-II Nonlocal Quadratic Tax, Radial-Drift Congestion, and the III/IV Forward-Surviving Families"
subtitle: "Quadratic Nonlocality Tax, Radial-Drift Congestion, and the Forward-Surviving Heterochiral Classes"
version: "v0.1"
date: "2026-08-14"
author: "Neo.K / EveMissLab"
language: "en-US"
status: "Theorem-style structural reduction note"
epistemic_status: "Exact consequences of triadwise energy/helicity conservation plus Waleffe helical decomposition. No global regularity proof."
---

# Navier–Stokes C3-C
# Class-II Nonlocal Quadratic Tax, Radial-Drift Congestion, and the III/IV Forward-Surviving Families

## 0. Current Positioning

C3-B has compressed the hypothetical singular pair-production core into:

$$
\boxed{
\text{High--High Heterochiral UV Pair-Production Chain}.
}
$$

Where:

- the production of positive critical absolute helicity by homochiral triads is zero;
- the unique-sign mode of divergent pair production must escape any fixed frequency cutoff;
- each UV unique-sign mode requires at least one comparable-high partner.

This round prioritizes Class II:

$$
(s_k,s_p,s_q)=(+,-,-),
\qquad
0<k\le p\le q.
$$

The goal is to answer:

> If $k\ll p\sim q$, can Class II truly serve as a highly efficient UV pair-production mechanism?

Answer:

$$
\boxed{
\text{Class II can exist, but when strongly nonlocal, it must simultaneously pay}
}
$$

$$
\boxed{
\text{quadratic critical-production tax}
+
\text{radial-drift congestion}.
}
$$

---

# 1. Review of Triad Transfer Algebra

For any helical triad:

$$
\mathbf k+\mathbf p+\mathbf q=0,
$$

Ordering:

$$
0<k\le p\le q,
$$

Modal energies:

$$
e_k,\ e_p,\ e_q.
$$

Triadwise energy and signed helicity conservation:

$$
\dot e_k+\dot e_p+\dot e_q=0,
$$

$$
s_k k\dot e_k+s_p p\dot e_p+s_q q\dot e_q=0.
$$

Thus, there exists a scalar transfer parameter $\Theta_\tau$:

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

This equation only uses exact triad invariants.

---

# 2. Class II Exact Equations

Class II:

$$
(+--).
$$

Substituting:

$$
s_k=+1,\quad s_p=-1,\quad s_q=-1.
$$

We obtain:

$$
\boxed{
\dot e_k
=
(q-p)\Theta_\tau,
}
$$

$$
\boxed{
\dot e_p
=
-(q+k)\Theta_\tau,
}
$$

$$
\boxed{
\dot e_q
=
(p+k)\Theta_\tau.
}
$$

The unique-helicity-sign mode is the smallest wavenumber $k$.

Critical pair-production contribution:

$$
\boxed{
\mathcal R_{\mathrm{II}}
=
k(q-p)\Theta_\tau.
}
$$

---

# 3. Triangle Geometry Gives the First Suppression

From:

$$
\mathbf k+\mathbf p+\mathbf q=0
$$

the triangle inequality gives:

$$
q\le p+k.
$$

Therefore:

$$
\boxed{
0\le q-p\le k.
}
$$

Thus:

$$
\boxed{
|\mathcal R_{\mathrm{II}}|
\le
k^2|\Theta_\tau|.
}
$$

This is the radial-gap suppression already observed in the previous round.

However, what we need to compare in this round is not just the absolute coefficient, but how small it is relative to the true high-frequency exchange within the triad.

---

# 4. High Critical Exchange Scale

Define two high-mode critical exchange magnitudes:

$$
X_p
=
p|\dot e_p|,
$$

$$
X_q
=
q|\dot e_q|.
$$

In Class II:

$$
X_p
=
p(q+k)|\Theta_\tau|,
$$

$$
X_q
=
q(p+k)|\Theta_\tau|.
$$

Since:

$$
q\ge p,
$$

Therefore:

$$
\boxed{
X_p\ge p^2|\Theta_\tau|,
}
$$

and:

$$
\boxed{
X_q\ge p^2|\Theta_\tau|.
}
$$

Let:

$$
X_{\mathrm{hi}}
=
\min\{X_p,X_q\}.
$$

Then:

$$
\boxed{
X_{\mathrm{hi}}
\ge
p^2|\Theta_\tau|.
}
$$

---

# 5. C3-C.1: Quadratic Nonlocality Tax

## Theorem 5.1

A Class II triad satisfies:

$$
\boxed{
|\mathcal R_{\mathrm{II}}|
\le
\left(\frac{k}{p}\right)^2
X_{\mathrm{hi}}.
}
$$

### Proof

From:

$$
|\mathcal R_{\mathrm{II}}|
\le
k^2|\Theta_\tau|
$$

and:

$$
X_{\mathrm{hi}}
\ge
p^2|\Theta_\tau|,
$$

we directly obtain:

$$
|\mathcal R_{\mathrm{II}}|
\le
\frac{k^2}{p^2}
X_{\mathrm{hi}}.
$$

$\square$

---

# 6. Dyadic Form

If:

$$
p\ge2^N k,
$$

Then:

$$
\boxed{
|\mathcal R_{\mathrm{II}}|
\le
2^{-2N}
X_{\mathrm{hi}}.
}
$$

Thus, for each additional dyadic separation:

$$
N\mapsto N+1,
$$

the Class II pair-production decreases relative to the hidden high critical exchange by a factor of:

$$
4.
$$

This document refers to this as:

$$
\boxed{
\textbf{Class-II Quadratic Nonlocality Tax}.
}
$$

---

# 7. Hidden-Exchange Debt

Rewriting Theorem 5.1:

If:

$$
\mathcal R_{\mathrm{II}}\ne0,
$$

Then:

$$
\boxed{
X_{\mathrm{hi}}
\ge
\left(\frac{p}{k}\right)^2
|\mathcal R_{\mathrm{II}}|.
}
$$

Therefore, if:

$$
\chi_\tau
=
\frac{k}{p}
\ll1,
$$

to generate a fixed amount of critical pair production, it requires:

$$
\boxed{
\chi_\tau^{-2}
}
$$

times the magnitude of hidden high-frequency critical exchange.

This is not a new finite budget theorem.

It is an exact **congestion certificate**:

> The more nonlocal the pair production, the larger the underlying high-mode exchange circulation must be.

---

# 8. Energy-Transfer Cancellation Ratio

Class II has:

$$
\dot e_p+\dot e_q
=
-\dot e_k.
$$

While:

$$
|\dot e_k|
=
(q-p)|\Theta_\tau|
\le
k|\Theta_\tau|.
$$

At the same time:

$$
|\dot e_p|
=
(q+k)|\Theta_\tau|
\ge
p|\Theta_\tau|,
$$

$$
|\dot e_q|
=
(p+k)|\Theta_\tau|
\ge
p|\Theta_\tau|.
$$

Therefore:

## Theorem 8.1 (High-Exchange Cancellation)

$$
\boxed{
\frac{
|\dot e_p+\dot e_q|
}{
\min\{|\dot e_p|,|\dot e_q|\}
}
\le
\frac{k}{p}.
}
$$

When:

$$
k/p\to0,
$$

the two high-mode energy transfers become:

$$
\boxed{
\text{large opposite transfers + small residual}.
}
$$

This is the exact algebraic version of the pair cancellation described by Waleffe for strongly nonlocal reverse-type interactions.

---

# 9. Donor/Receiver Orientation of Positive Pair Production

Assuming nondegeneracy:

$$
q>p.
$$

Class II:

$$
\mathcal R_{\mathrm{II}}
=
k(q-p)\Theta_\tau.
$$

Therefore:

$$
\mathcal R_{\mathrm{II}}>0
\iff
\Theta_\tau>0.
$$

In this case:

$$
\dot e_k>0,
$$

$$
\dot e_p<0,
$$

$$
\dot e_q>0.
$$

Thus:

$$
\boxed{
\text{Class II positive pair production: }
p\text{ is the donor, }
k,q\text{ are receivers}.
}
$$

That is:

$$
\boxed{
p
\longrightarrow
\{k,q\}.
}
$$

---

# 10. Class II is Not a Pure Forward Transfer

For strongly nonlocal:

$$
k\ll p\sim q,
$$

positive pair production simultaneously:

1. sends a small fraction of the transfer to the low mode $k$;
2. moves the main high-end transfer from $p$ to the nearby $q$.

It is not a pure forward pattern of the form:

$$
k\to p\to q
$$

where the lowest mode directly feeds the higher modes.

This is consistent with Waleffe's structural description of the small-scale same-helicity nonlocal R-class:

- the high-end local exchange is large;
- the feedback to the low mode is small;
- the large high transfers nearly cancel in pairs;
- the net effect approximates wave-number-space advection.

---

# 11. Radial Step Bound

The Class II high receiver is:

$$
q.
$$

The high donor is:

$$
p.
$$

High-end radial advancement:

$$
\Delta_{\mathrm{rad}}
=
q-p.
$$

The triangle inequality has given:

$$
q-p\le k.
$$

Dividing by $p$:

$$
\boxed{
\frac{q-p}{p}
\le
\frac{k}{p}.
}
$$

Define:

$$
\delta_\tau
=
\frac{q-p}{p},
$$

$$
\chi_\tau
=
\frac{k}{p}.
$$

Then:

$$
\boxed{
0\le\delta_\tau\le\chi_\tau\le1.
}
$$

Therefore, nonlocality:

$$
\chi_\tau\ll1
$$

automatically implies:

$$
\delta_\tau\ll1.
$$

---

# 12. Class-II Radial Genealogy

Consider an idealized source-preserving Class-II high-end genealogy:

$$
p_0
\to
q_0=p_1
\to
q_1=p_2
\to
\cdots.
$$

Let the $n$-th step be:

$$
q_n=p_n(1+\delta_n),
$$

where:

$$
0\le\delta_n\le\chi_n.
$$

Then:

$$
p_{n+1}
=
p_n(1+\delta_n).
$$

Therefore:

$$
\boxed{
p_n
=
p_0
\prod_{j=0}^{n-1}
(1+\delta_j).
}
$$

---

# 13. C3-C.2: Radial-Drift Congestion Lemma

## Theorem 13.1

If a Class-II high-end genealogy satisfies:

$$
p_n\to\infty,
$$

then it must hold that:

$$
\boxed{
\sum_{n=0}^{\infty}
\delta_n
=
\infty.
}
$$

Thus, it must also hold that:

$$
\boxed{
\sum_{n=0}^{\infty}
\chi_n
=
\infty.
}
$$

### Proof

If:

$$
\sum_n\delta_n<\infty,
$$

Then:

$$
\sum_n\log(1+\delta_n)
\le
\sum_n\delta_n
<
\infty.
$$

Therefore, the product:

$$
\prod_n(1+\delta_n)
$$

converges to a finite positive number.

Thus:

$$
p_n
=
p_0
\prod_{j<n}(1+\delta_j)
$$

remains bounded, which contradicts:

$$
p_n\to\infty
$$

Hence:

$$
\sum_n\delta_n=\infty.
$$

From:

$$
\delta_n\le\chi_n,
$$

we obtain:

$$
\sum_n\chi_n=\infty.
$$

$\square$

---

# 14. Uniform Nonlocality Congestion

If the entire chain satisfies:

$$
\chi_n\le\varepsilon<1,
$$

then at each step:

$$
p_{n+1}\le(1+\varepsilon)p_n.
$$

To cross from:

$$
p_0
$$

to:

$$
2p_0,
$$

it requires at least:

$$
m
\ge
\frac{\log2}{\log(1+\varepsilon)}.
$$

When:

$$
\varepsilon\ll1,
$$

we have:

$$
\log(1+\varepsilon)\sim\varepsilon.
$$

Therefore:

$$
\boxed{
m
\gtrsim
\frac{1}{\varepsilon}.
}
$$

This is **Class-II step congestion**.

---

# 15. Quadratic Tax + Linear Congestion

Strongly nonlocal Class II simultaneously possesses:

### Per-step pair-production efficiency

$$
\boxed{
\frac{|\mathcal R_{\mathrm{II}}|}{X_{\mathrm{hi}}}
\le
\chi^2.
}
$$

### Number of steps required per dyadic scale traversal

$$
\boxed{
m
\gtrsim
\chi^{-1}
}
$$

if $\chi$ is approximately uniform.

Therefore, the more nonlocal it is:

- the less production efficiency there is per step;
- the more steps are required to traverse a dyadic scale.

This document refers to this as:

$$
\boxed{
\textbf{Quadratic Tax + Linear Congestion}.
}
$$

This is still not a contradiction, because we do not yet have:

$$
\sum X_{\mathrm{hi}}<\infty.
$$

But it turns the strongly nonlocal Class II into a very expensive genealogy.

---

# 16. Class III Exact Orientation

Class III:

$$
(+-+).
$$

Transfer:

$$
\dot e_k
=
-(p+q)\Theta_\tau,
$$

$$
\dot e_p
=
(q-k)\Theta_\tau,
$$

$$
\dot e_q
=
(p+k)\Theta_\tau.
$$

The unique sign is at the medium mode:

$$
p.
$$

Pair production:

$$
\mathcal R_{\mathrm{III}}
=
p(q-k)\Theta_\tau.
$$

If:

$$
\mathcal R_{\mathrm{III}}>0,
$$

Then:

$$
\Theta_\tau>0.
$$

Therefore:

$$
\boxed{
\dot e_k<0,
\qquad
\dot e_p>0,
\qquad
\dot e_q>0.
}
$$

That is:

$$
\boxed{
k
\longrightarrow
\{p,q\}.
}
$$

The lowest mode is the donor.

This is a direct forward-compatible orientation.

---

# 17. Class III Strongly Nonlocal Regime Has No $k/p$ Suppression

If:

$$
k\ll p\sim q,
$$

Since:

$$
q\le p+k,
$$

we have:

$$
q\sim p.
$$

And:

$$
q-k
\sim p.
$$

Therefore:

$$
\boxed{
|\mathcal R_{\mathrm{III}}|
\sim
p^2|\Theta_\tau|
}
$$

at the radial algebra level, there is no:

$$
(k/p)^2
$$

tax.

Thus, Class III is a true nonlocal survivor.

---

# 18. Class IV Exact Orientation

Class IV:

$$
(++-).
$$

Transfer:

$$
\dot e_k
=
(p+q)\Theta_\tau,
$$

$$
\dot e_p
=
-(q+k)\Theta_\tau,
$$

$$
\dot e_q
=
(k-p)\Theta_\tau.
$$

The unique sign is at the largest mode:

$$
q.
$$

Pair production:

$$
\mathcal R_{\mathrm{IV}}
=
q(k-p)\Theta_\tau.
$$

Since:

$$
k-p\le0,
$$

If:

$$
\mathcal R_{\mathrm{IV}}>0,
$$

Then:

$$
\Theta_\tau<0.
$$

Thus:

$$
\boxed{
\dot e_k<0,
\qquad
\dot e_p>0,
\qquad
\dot e_q>0.
}
$$

That is, similarly:

$$
\boxed{
k
\longrightarrow
\{p,q\}.
}
$$

The lowest mode is the donor.

---

# 19. Class IV is the Only Top-Unique Class

The positions of the unique-sign modes for the three heterochiral classes:

| Class | signs | unique-sign wavenumber |
|---|---|---|
| II | $(+--)$ | $k$ smallest |
| III | $(+-+)$ | $p$ middle |
| IV | $(++-)$ | $q$ largest |

Therefore:

$$
\boxed{
\text{Class IV is the only class that places the unique-helicity mode at the maximum wavenumber of the triad}.
}
$$

Thus, if we track the:

$$
\text{unique-sign critical pair-production frontier},
$$

Class IV is the only pair-production class that is **directly frontier-capable**.

The precise meaning of this statement is:

> Within a single triad, only the positive pair-production target of Class IV is the maximum wavenumber of that triad.

It does not imply that a global blow-up must consist solely of Class IV.

---

# 20. Ancestry Demand of Class III

The Class III unique mode is located at:

$$
p,
$$

But the same positive pair-production event also has a high receiver at:

$$
q\ge p
$$

Therefore, Class III can forward transfer, but the unique-sign target is not the triad frontier.

To continuously push the unique-sign pair-production frontier higher, a Class III event requires:

- a higher $q$ mode to form simultaneously;
- or the next generation to use $q$ as an ancestry source;
- or other classes to be responsible for frontier extension.

Thus, it still carries an ancestry obligation.

---

# 21. C3-C.3: Forward-Compatible Survivor Classification

Define a positive pair-production event as **forward-compatible** if the lowest wavenumber $k$ is the energy donor.

Then, from the exact transfer signs:

$$
\boxed{
\text{Class III and Class IV are forward-compatible}.
}
$$

Whereas in Class II positive pair production, the donor is:

$$
p,
$$

not $k$.

Therefore:

$$
\boxed{
\text{Class II is not forward-compatible in this precise sense}.
}
$$

This is an algebraic classification and does not rely on the Waleffe instability assumption.

---

# 22. Relationship with Waleffe's R/F Classification

Waleffe classified elementary helical interactions into reverse-type and forward-type families based on the helicity signs of the small-scale modes.

For the ordering in this document:

- the two higher modes $p,q$ of Class II have the same sign;
- the $p,q$ of Classes III/IV have opposite signs.

This is consistent with Waleffe's structural analysis that:

- nonlocal same-small-scale-sign interactions feature large local exchanges and strong cancellation;
- opposite-small-scale-sign interactions support forward transfer;

This document does not use his statistical instability assumption to prove the transfer signs.

All sign orientations in this document are directly derived from the condition:

$$
\mathcal R_\tau>0
$$

and the exact conservation algebra.

---

# 23. X-Integration Guards of C3-C

For the Class-II chain, we add:

### G-$\chi$ — Nonlocality Ratio

$$
\chi_n=\frac{k_n}{p_n}.
$$

### G-$\delta$ — Radial Drift

$$
\delta_n=\frac{q_n-p_n}{p_n}.
$$

And:

$$
0\le\delta_n\le\chi_n.
$$

### G-tax — Production Efficiency

$$
\frac{|\mathcal R_n|}{X_{\mathrm{hi},n}}
\le
\chi_n^2.
$$

### G-drift — UV Escape

If:

$$
p_n\to\infty,
$$

it must hold that:

$$
\sum_n\delta_n=\infty.
$$

### G-congestion

If:

$$
\chi_n\le\varepsilon,
$$

crossing each dyadic scale requires at least:

$$
O(\varepsilon^{-1})
$$

steps.

Therefore, a Class-II singular certificate cannot simply state:

$$
\text{all interactions legal}.
$$

It must also carry:

$$
\boxed{
\text{hidden exchange debt}
+
\text{radial drift debt}
+
\text{step congestion}.
}
$$

---

# 24. An Important No-Go

Currently, we cannot directly deduce a contradiction from:

$$
X_{\mathrm{hi}}
\ge
\chi^{-2}|\mathcal R|
$$

Because there is no proven global finite bound:

$$
\boxed{
\int
\sum_{\tau}
X_{\mathrm{hi},\tau}\,dt
<
\infty.
}
$$

This quantity is the absolute high-frequency exchange variation; energy conservation only controls the signed net transfer, not the absolute turnover.

Therefore:

$$
\boxed{
\text{nonlocality tax}
\neq
\text{finite-budget proof}.
}
$$

This must be explicitly maintained.

---

# 25. Conditional Suppression Theorem

## Theorem 25.1

Let:

$$
\mathfrak C_{II}^{(N)}
$$

denote all Class-II triads satisfying:

$$
p\ge2^N k.
$$

Define their cumulative pair production:

$$
P_{II}^{(N)}
=
\int
\sum_{\tau\in\mathfrak C_{II}^{(N)}}
|\mathcal R_\tau(t)|
\,dt,
$$

and the hidden high-exchange variation:

$$
V_{II}^{(N)}
=
\int
\sum_{\tau\in\mathfrak C_{II}^{(N)}}
X_{\mathrm{hi},\tau}(t)
\,dt.
$$

Then:

$$
\boxed{
P_{II}^{(N)}
\le
2^{-2N}
V_{II}^{(N)}.
}
$$

### Proof

Applying triad-by-triad:

$$
|\mathcal R_\tau|
\le
2^{-2N}X_{\mathrm{hi},\tau}
$$

then integrating and summing. $\square$

---

# 26. Conditional Consequence

If in the future we can prove some form of:

$$
V_{II}^{(N)}
=
o(2^{2N})
$$

as:

$$
N\to\infty,
$$

Then:

$$
\boxed{
P_{II}^{(N)}\to0.
}
$$

That is, strongly nonlocal Class II is asymptotically negligible for cumulative pair production.

Therefore, the new specific proof target is:

$$
\boxed{
\text{Control the growth rate of }V_{II}^{(N)}.
}
$$

This is more precise than vaguely stating 'nonlocal Class II should be unimportant'.

---

# 27. Survivor Map

Current critical pair-production classes:

## Homochiral

$$
\boxed{
\mathcal R=0.
}
$$

Eliminated as a production source.

## Class II Local / Moderately Nonlocal

Still survives.

## Class II Strongly Nonlocal

Possesses:

$$
\boxed{
\chi^2\text{ production tax}
+
\chi^{-1}\text{ traversal congestion}
}
$$

But not yet completely eliminated.

## Class III

Forward-compatible; strongly nonlocal regime is not subject to the radial-gap tax.

$$
\boxed{
\text{SURVIVOR}.
}
$$

## Class IV

Forward-compatible; unique sign is located at the highest mode.

$$
\boxed{
\text{PRIMARY FRONTIER SURVIVOR}.
}
$$

---

# 28. New Mainline: C3-D

After C3-C, the most worthwhile direct target is:

$$
\boxed{
\textbf{C3-D — Forward Heterochiral Frontier Rigidity}.
}
$$

Core survivors:

$$
\boxed{
\text{Classes III/IV}
+
\text{non-negligibly local Class II}.
}
$$

Among them, Class IV has the highest priority because it directly performs positive pair production on the highest unique-helicity mode.

---

# 29. C3-D Proof Obligations

## D1 — Class-IV Dyadic Frontier Production

Define:

$$
\mathcal R_{IV,q}
$$

as the Class-IV positive production where the unique-sign highest mode is located in shell $q$.

From the C3-B unique-sign UV escape, investigate whether it can be proven that:

$$
\boxed{
\sum_{q>Q}
\int
[\mathcal R_{IV,q}]_+dt
}
$$

must have a nontrivial lower envelope in a blow-up scenario.

## D2 — Separate III from IV Ancestry

The Class III unique mode is not the top mode.

Establish the ancestry graph:

$$
p_{\rm unique}
\leftarrow
(k,q)
$$

and track the source of $q$.

Determine whether an infinite III-only genealogy inevitably:

- transitions into a IV step;
- or requires infinite pre-existing higher-frequency ancestry.

## D3 — Absolute Exchange Variation

Attempt to control:

$$
V_{II}^{(N)}.
$$

Candidate tools:

- dyadic commutators;
- local energy flux;
- scale-locality estimates;
- dissipation wavenumber;
- frequency-envelope variation;
- wave-space telescoping.

## D4 — Wave-Space Advection Formulation

For nonlocal Class II:

$$
q-p\le k\ll p.
$$

Treat the high-end $p\to q$ as a small radial step.

Investigate whether the aggregate Class-II high transfer can be rewritten as a discrete/continuous divergence:

$$
\partial_\kappa
\mathcal J(\kappa)
$$

so that a large number of opposite high exchanges telescopically cancel, leaving only the shell-boundary flux.

If successful, it might reduce:

$$
V_{II}
$$

from an absolute exchange to a boundary variation.

This is most directly related to the wave-number-space advection structure described by Waleffe.

---

# 30. Formal Status

$$
\boxed{
\begin{aligned}
\text{Class-II exact transfer equations}
&:\ \mathrm{PROVED},\\
\text{quadratic nonlocality tax}
&:\ \mathrm{PROVED},\\
\text{high-exchange cancellation ratio}
&:\ \mathrm{PROVED},\\
\text{radial step bound}
&:\ \mathrm{PROVED},\\
\text{radial-drift congestion lemma}
&:\ \mathrm{PROVED},\\
\text{Class III forward-compatible}
&:\ \mathrm{PROVED},\\
\text{Class IV forward-compatible}
&:\ \mathrm{PROVED},\\
\text{Class IV top-unique}
&:\ \mathrm{PROVED},\\
\text{strongly nonlocal Class II globally negligible}
&:\ \mathrm{OPEN},\\
V_{II}^{(N)}=o(2^{2N})
&:\ \mathrm{OPEN},\\
\text{Forward Heterochiral Frontier Rigidity}
&:\ \mathrm{OPEN}.
\end{aligned}
}
$$

---

# 31. Conclusion

This round does not prove N–S regularity.

However, it extracts two exact costs from the Class-II strong-nonlocal route:

$$
\boxed{
\frac{|\mathcal R_{II}|}{X_{\rm hi}}
\le
\left(\frac{k}{p}\right)^2
}
$$

and:

$$
\boxed{
p_n\to\infty
\Rightarrow
\sum_n
\frac{q_n-p_n}{p_n}
=
\infty.
}
$$

Therefore, if strongly nonlocal Class II is to proceed all the way to the UV, it must:

1. accept quadratic production inefficiency at each step;
2. compensate for scale growth with a large number of small radial steps;
3. maintain a massive, nearly mutually canceling high-mode exchange circulation.

In contrast:

$$
\boxed{
\text{Classes III/IV positive pair production is directly fed by the lowest mode to higher modes}.
}
$$

And:

$$
\boxed{
\text{Class IV is the only class where the unique-helicity target is located at the highest frequency of the triad}.
}
$$

Thus, the next main battlefield is formally narrowed down to:

$$
\boxed{
\textbf{C3-D — Forward Heterochiral Frontier Rigidity}
}
$$

Prioritizing:

$$
\boxed{
\text{Class IV frontier production}
+
\text{Class III ancestry}
+
\text{Class-II wave-space telescoping}.
}
$$

---

# References

1. F. Waleffe, *The nature of triad interactions in homogeneous turbulence*, Physics of Fluids A 4 (1992), 350–363.
2. F. Waleffe, *Inertial transfers in the helical decomposition*, Physics of Fluids A 5 (1993).
3. L. Biferale, E. S. Titi, *On the Global Regularity of a Helical-decimated Version of the 3D Navier–Stokes Equations*, arXiv:1303.1215.
4. G. Sahoo, L. Biferale, *Disentangling the triadic interactions in Navier-Stokes equations*, arXiv:1510.09006.
5. G. Sahoo, L. Biferale, *Energy Cascade and Intermittency in Helically Decomposed Navier-Stokes Equations*, arXiv:1709.03713.
6. Z. Lei, F.-H. Lin, Y. Zhou, *Structure of Helicity and Global Solutions of Incompressible Navier–Stokes Equation*, arXiv:1505.00142.

# Internal Dependencies

- `NS_C1_UV_Replenishment_Chain_v0.2.md`
- `NS_C2_Critical_Toll_Spike_Packing_v0.3.md`
- `NS_C3A_Conservation_Criticality_Helical_Pair_Production_v0.1.md`
- `NS_C3B_BiHelical_Equalization_UniqueSign_UV_Escape_v0.1.md`
- `True ETN / Infinite-Dimensional Tension Field`
- `X_Integral_Unified_Program_v0.2.md`

Next:

$$
\boxed{
\textbf{C3-D — Forward Heterochiral Frontier Rigidity}
}
$$