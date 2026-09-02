---
title: "Navier–Stokes C6-P: Ancient Defect-State Classification, Record-Peak Derivative Rigidity, and Peak-Local Pressure Closure"
subtitle: "Record-Peak Boundedness Absorbs Every Fixed Derivative Order; Flattening Produces a Galilean-Trivial Ancient Profile; Remote Mass Tails Cannot Sustain Peak Pressure Hessian; Ancient TS/GP/HF Labels Require Local Absolute Inheritance"
version: "v0.1"
date: "2026-08-16"
author: "Neo.K / EveMissLab"
language: "en"
status: "C6 ancient-peak defect classification / fixed-order derivative-tower elimination / local pressure closure"
epistemic_status: "Exact record-peak scaling and pressure-tail estimates + external bounded-mild smoothing, analyticity, backward uniqueness and ancient-solution interfaces. Ancient TS/GP/HF inheritance remains conditional on local carrier and provenance gates. Does NOT prove Navier–Stokes global regularity."
---

# Navier–Stokes C6-P
# Ancient Defect-State Classification, Record-Peak Derivative Rigidity, and Peak-Local Pressure Closure

## 0. Current Stage Positioning

C6-O divides the Type-II carrier into:

$$
\boxed{
\text{PEAK-ANCIENT}
}
$$

or:

$$
\boxed{
\text{MASS-ESCAPE}
}
$$

or:

$$
\boxed{
\text{DERIVATIVE-RESTART}
}
$$

and the scenario-dependent:

$$
\boxed{
\text{EULER-SCENARIO}.
}
$$

where the record peak scaling:

$$
v_n(z,\tau)
=
A_n^{-1}
u
\left(
x_n+\frac{z}{A_n},
t_n+\frac{\tau}{A_n^2}
\right),
$$

with:

$$
A_n
=
\|u(t_n)\|_\infty
=
\max_{s\le t_n}
\|u(s)\|_\infty,
$$

gives:

$$
\boxed{
\|v_n(\tau)\|_\infty
\le1
\qquad
(\tau\le0),
}
$$

and after passing to a subsequence:

$$
v_n
\to
v_\infty
$$

locally,

where:

$$
\boxed{
v_\infty
}
$$

is a nontrivial bounded ancient Navier–Stokes solution.

C6-O left open:

1. can fixed derivative orders escape below the peak scale?
2. can high-order HF create an infinite derivative scale tower?
3. which TS / GP / HF observables actually pass to:
   $$
   v_\infty?
   $$
4. does mass-scale far pressure continue to drive peak GP?
5. what happens if the peak frame flattens?

C6-P obtains a major correction:

$$
\boxed{
\textbf{record-peak boundedness already eliminates every fixed-order derivative tower}.
}
$$

The only possible derivative escape is:

- spatial carrier escape;
- order-index escape:
  $$
  k_n\to\infty;
  $$
- or failure of theorem/geometry inheritance.

Moreover, the order-index branch must be interpreted relative to the analytic derivative baseline rather than the raw:

$$
A_k.
$$

Main results of this round:

1. bounded mild smoothing gives for every fixed:
   $$
   k
   $$
   a uniform peak-frame derivative bound:
   $$
   \boxed{
   \|D^kv_n(0)\|_\infty
   \le
   C_k(\nu);
   }
   $$
2. therefore:
   $$
   \boxed{
   A_{k,n}
   \le
   C_kA_n^{k+1};
   }
   $$
3. C6-O fixed-order:
   $$
   \widehat A_{k,n}^{peak}\to\infty
   $$
   branch is impossible at record peaks;
4. fixed-order derivative scale:
   $$
   b_{k,n}
   =
   A_{k,n}^{-1/(k+1)}
   $$
   obeys:
   $$
   \boxed{
   b_{k,n}/a_n
   \ge
   C_k^{-1/(k+1)};
   }
   $$
5. hence no fixed:
   $$
   k
   $$
   can generate an asymptotically smaller amplitude-normalized scale;
6. apparent derivative-tower escape can only be:
   $$
   \boxed{
   k_n\to\infty;
   }
   $$
7. bounded-data space analyticity shows large raw high-order derivatives can be analytic factorial growth rather than a new concentration scale;
8. therefore high-order escape must be tested with factorial/chain normalization;
9. record peak analyticity gives a uniform peak analytic radius on a fixed positive smoothing interval;
10. consequently the factorial-normalized derivative roots remain uniformly controlled in the peak frame;
11. high-order raw derivative growth is demoted from a physical scale defect;
12. if:
    $$
    \widehat A_{1,n}^{peak}\to0,
    $$
    then:
    $$
    v_\infty(\cdot,0)
    $$
    is a nonzero spatial constant;
13. backward uniqueness for bounded mild 3D N–S with nontrivial final data then gives:
    $$
    \boxed{
    v_\infty(x,\tau)\equiv b;
    }
    $$
14. therefore the flattening branch is a Galilean-trivial ancient profile;
15. it carries no derivative-based:
    $$
    TS/GP/HF
    $$
    defect;
16. if a fixed derivative order remains globally nonzero but its carrier escapes every bounded peak ball, this is:
    $$
    \boxed{
    \textbf{Derivative-Carrier Translation Escape};
    }
    $$
17. thus fixed-order HF ancient inheritance reduces to:
    - local capture;
    - or spatial carrier escape;
18. GP local geometry passes under:
    $$
    C^2_{\rm loc}
    $$
    convergence + nonzero peak-critical Q load + strict margins;
19. pressure Hessian obeys uniform peak-tail:
    $$
    O(R^{-2});
    $$
20. therefore:
    $$
    \boxed{
    \textbf{peak-local pressure Hessian is asymptotically finite-radius determined};
    }
    $$
21. finite-radius pressure source pieces pass under local convergence;
22. hence local GP pressure closes once provenance is repartitioned at the peak scale;
23. infinite mass-scale tail cannot remain an independent GP pressure-Hessian carrier;
24. TS middle-source density is local and can pass under local convergence;
25. TS operator source uses:
    $$
    P_{st}
    $$
    and remains nonlocal;
26. therefore TS ancient inheritance has a new:
    $$
    \boxed{
    \textbf{Projected-Operator Tail Gate};
    }
    $$
27. HF fixed-order local geometry can pass under local derivative capture + strict sign margin;
28. Grujić–Xu theorem status itself does not automatically pass to a bounded ancient profile;
29. ancient inheritance:
    $$
    \neq
    $$
    ancient recurrence;
30. C6-P final ancient-peak frontier becomes:
    $$
    \boxed{
    GP^{anc}_{loc}
    \vee
    HF^{anc}_{k,loc}
    \vee
    TS^{anc}_{loc/proj}
    \vee
    \text{FLAT}
    \vee
    \text{SPATIAL-CARRIER-ESCAPE}.
    }
    $$

---

# 1. Fresh primary-source audit

## 1.1 Bounded mild smoothing

Koch–Nadirashvili–Seregin–Šverák prove that bounded Navier–Stokes solutions enjoy parabolic smoothing and higher derivative bounds away from the initial time.

In particular, for bounded solutions on a fixed positive time interval,

for each:

$$
k=0,1,2,\ldots
$$

one obtains:

$$
\boxed{
\|\nabla^ku\|_{L^\infty}
\le
C(k,\delta,T,M)
}
$$

inside a shorter interval,

where:

$$
M
=
\|u\|_{L^\infty}.
$$

This is the key external input for fixed-order derivative rigidity at the record peak scale.

## 1.2 Space analyticity

Bounded initial data are contained in local:

$$
BMO
$$

spaces.

Xu proves local-in-time solvability and spatial analyticity for N–S with:

$$
bmo/BMO
$$

-type initial data,

and notes previous analytic results for:

$$
L^\infty
$$

initial velocity.

Thus a record peak field which is uniformly bounded on a fixed preceding time interval acquires a uniform positive spatial analyticity radius after a fixed smoothing delay.

This supplies the correct interpretation of high-order derivative growth.

## 1.3 Quantitative analyticity

Wang–Gao–Xue obtain quantitative derivative estimates and joint space-time analyticity for mild N–S solutions in critical settings,

with derivative growth of analytic/Gevrey type.

C6-P uses this only to support the factorial-normalized high-order guard,

not as a global:

$$
L^3
$$

bound on the ancient peak sequence.

## 1.4 Backward uniqueness with nontrivial final data

Lei–Yang–Yuan prove backward uniqueness for bounded mild 3D whole-space Navier–Stokes solutions with the same nontrivial final data, under bounded-vorticity / regularity assumptions satisfied by the smoothed ancient profiles used here.

Therefore if a bounded ancient profile equals a constant vector at:

$$
\tau=0,
$$

it must equal the same constant solution on every finite backward interval,

hence for all ancient times.

## 1.5 Pressure expansion

Bradshaw–Tsai provide a rigorous whole-space local pressure expansion.

Together with the:

$$
|\nabla^2K(x)|
\lesssim
|x|^{-5}
$$

pressure-Hessian kernel decay,

this supports finite-radius peak-pressure closure.

## 1.6 Recent Type-II analysis

Seregin's 2026 Type-II note studies particular local Type-II scenarios through Euler scaling and Euler Liouville theorems.

C6-P keeps this as a distinct scenario-dependent Type-II interface.

---

# 2. Record peak sequence

Let:

$$
t_n\uparrow T^\ast
$$

be amplitude record times:

$$
\boxed{
A_n
=
\|u(t_n)\|_\infty
=
\max_{0\le t\le t_n}
\|u(t)\|_\infty
\to\infty.
}
$$

Choose:

$$
x_n
$$

with:

$$
|u(x_n,t_n)|
=
A_n.
$$

Define peak scale:

$$
\boxed{
a_n=A_n^{-1}.
}
$$

---

# 3. Peak N–S rescaling

Define:

$$
\boxed{
v_n(z,\tau)
=
A_n^{-1}
u(
x_n+a_nz,
t_n+a_n^2\tau
).
}
$$

Then:

$$
v_n
$$

solves the same N–S equations.

For:

$$
\tau\le0,
$$

record maximality gives:

$$
\boxed{
\|v_n(\tau)\|_\infty
\le1.
}
$$

At:

$$
\tau=0,
$$

$$
\boxed{
|v_n(0,0)|=1.
}
$$

---

# 4. Fixed backward smoothing interval

Because:

$$
t_nA_n^2\to\infty,
$$

for large:

$$
n
$$

the full interval:

$$
[-2,0]
$$

lies inside the rescaled domain.

Therefore:

$$
\boxed{
\|v_n\|_{L^\infty(
\mathbb R^3\times[-2,0]
)}
\le1.
}
$$

---

# 5. C6-P.1: Fixed-Order Record-Peak Derivative Rigidity

Apply bounded mild smoothing on:

$$
[-2,0]
$$

and evaluate after a fixed positive smoothing gap.

For every fixed:

$$
k\ge1,
$$

there exists:

$$
C_k=C_k(\nu)
<\infty
$$

such that:

$$
\boxed{
\|D^kv_n(0)\|_\infty
\le
C_k
}
$$

for all sufficiently large:

$$
n.
$$

### In original variables

Since:

$$
D^kv_n
=
A_n^{-(k+1)}
D^ku,
$$

$$
\boxed{
A_{k,n}
\le
C_k
A_n^{k+1}.
}
$$

---

# 6. Correction to C6-O derivative trichotomy

C6-O allowed:

$$
\widehat A_{k,n}^{peak}
=
A_{k,n}/A_n^{k+1}
\to\infty
$$

for fixed:

$$
k.
$$

C6-P.1 gives:

$$
\boxed{
\widehat A_{k,n}^{peak}
\le
C_k.
}
$$

Therefore:

# 7. C6-P.2: Fixed-Order Derivative-Tower No-Go

For every fixed:

$$
k,
$$

the record-amplitude peak frame eliminates:

$$
\boxed{
\widehat A_{k,n}^{peak}\to\infty.
}
$$

Thus:

$$
\boxed{
\textbf{fixed-order derivative-tower restart is impossible at record peaks}.
}
$$

---

# 8. Fixed-order derivative scale lower bound

Recall:

$$
b_{k,n}
=
A_{k,n}^{-1/(k+1)}.
$$

Peak scale:

$$
a_n=A_n^{-1}.
$$

Then:

$$
\frac{
b_{k,n}
}{
a_n
}
=
\left(
\widehat A_{k,n}^{peak}
\right)^{-1/(k+1)}.
$$

Therefore:

# 9. C6-P.3: No Fixed-Order Subpeak Scale

$$
\boxed{
\frac{
b_{k,n}
}{
a_n
}
\ge
C_k^{-1/(k+1)}
>0.
}
$$

For each fixed:

$$
k,
$$

the derivative scale cannot become asymptotically smaller than the amplitude peak scale.

---

# 10. What derivative escape remains?

Only:

$$
\boxed{
k=k_n\to\infty
}
$$

can evade the fixed-order estimate by allowing:

$$
C_{k_n}
$$

itself to grow.

This is:

$$
\boxed{
\textbf{Order-Index Escape}.
}
$$

It is not automatically a physical secondary scale.

---

# 11. Analytic baseline

A bounded mild solution after a fixed positive smoothing time is spatially analytic.

Thus there exists a positive analytic radius:

$$
\rho_{an}>0
$$

depending on:

- the uniform bound;
- viscosity;
- fixed smoothing time;

but not on:

$$
n,
$$

such that:

$$
v_n(0)
$$

extends analytically to a uniform complex spatial neighborhood.

Consequently, Cauchy estimates give an all-order schematic bound:

$$
\boxed{
\|D^kv_n(0)\|_\infty
\le
C_0
\rho_{an}^{-k}
k!
}
$$

with constants uniform in:

$$
n.
$$

---

# 12. Analytic-normalized derivative root

Define:

$$
\boxed{
\mathfrak A_{k,n}^{an}
=
\frac{
\|D^kv_n(0)\|_\infty^{1/(k+1)}
}{
(k!)^{1/(k+1)}
}.
}
$$

Then:

$$
\boxed{
\mathfrak A_{k,n}^{an}
\le
C
}
$$

uniformly in:

$$
n,k
$$

up to harmless:

$$
k/(k+1)
$$

powers of:

$$
\rho_{an}^{-1}.
$$

---

# 13. Grujić–Xu peak root

Use the familiar normalized root:

$$
\boxed{
\mathcal R_{k,n}^{peak}
=
\frac{
\|D^kv_n(0)\|_\infty^{1/(k+1)}
}{
c^{k/(k+1)}
(k!)^{1/(k+1)}
}.
}
$$

For fixed:

$$
c>0
$$

chosen relative to the analytic radius,

$$
\boxed{
\sup_{n,k}
\mathcal R_{k,n}^{peak}
<\infty.
}
$$

### Meaning

The peak frame regularizes the all-order derivative roots after the same factorial normalization already built into the Grujić–Xu chain.

---

# 14. C6-P.4: Raw High-Order Growth Is Not a Physical Tower

At the record peak scale,

large:

$$
\|D^kv_n\|_\infty
$$

for:

$$
k\to\infty
$$

can be generated by ordinary analytic factorial growth.

Therefore:

$$
\boxed{
\textbf{raw high-order derivative growth cannot be interpreted as a new physical inner scale}.
}
$$

A true high-order escape must instead appear through:

- analytic radius collapse;
- geometry/sign carrier escape;
- theorem/order metadata;
- or another scale-invariant normalized quantity.

But the record peak boundedness supplies a uniform positive analytic radius, so the first route is absent on the fixed ancient peak interval.

---

# 15. Derivative tower correction

C6-O's:

$$
\boxed{
\text{Mass}
\gg
\text{Peak}
\gg
\text{Derivative}
}
$$

tower is therefore corrected.

At a **record amplitude peak**:

$$
\boxed{
\text{Mass}
\gg
\text{Peak},
}
$$

while every fixed derivative order is absorbed at the same peak scale up to order-dependent constants.

The remaining high-order issue is:

$$
\boxed{
\text{Order/Geometry Escape},
}
$$

not a sequence of fixed-order physical scales.

---

# 16. Peak ancient limit

After passing to a subsequence:

$$
\boxed{
v_n
\to
v_\infty
}
$$

in:

$$
C^\infty_{\rm loc}
(
\mathbb R^3\times(-\infty,0]
)
$$

on compact subsets, using bounded mild smoothing/diagonal compactness.

The limit is:

$$
\boxed{
\text{bounded ancient},
}
$$

with:

$$
\boxed{
|v_\infty(0,0)|=1.
}
$$

---

# 17. First derivative peak ratio

Define:

$$
\boxed{
\widehat A_{1,n}^{peak}
=
\|\nabla v_n(0)\|_\infty
=
A_{1,n}/A_n^2.
}
$$

By C6-P.1:

$$
\widehat A_{1,n}^{peak}
\le
C_1.
$$

After passing to a subsequence:

$$
\widehat A_{1,n}^{peak}
\to
a_1
\in[0,C_1].
$$

---

# 18. Flattening branch

Assume:

$$
\boxed{
a_1=0.
}
$$

Then:

$$
\|\nabla v_n(0)\|_\infty
\to0.
$$

Therefore:

$$
\boxed{
\nabla v_\infty(\cdot,0)=0.
}
$$

Since:

$$
|v_\infty(0,0)|=1,
$$

there exists:

$$
b\in\mathbb R^3,
\qquad
|b|=1,
$$

with:

$$
\boxed{
v_\infty(x,0)=b
\qquad
\forall x.
}
$$

---

# 19. Backward uniqueness setup

The constant field:

$$
\boxed{
w(x,\tau)=b
}
$$

is a bounded mild N–S solution with:

$$
\nabla p=0.
$$

On any finite ancient interval:

$$
[-T,0],
$$

both:

$$
v_\infty
$$

and:

$$
w
$$

are bounded mild solutions,

with bounded vorticity by smoothing,

and final data:

$$
v_\infty(\cdot,0)
=
w(\cdot,0)
=
b.
$$

---

# 20. C6-P.5: Ancient Flattening Rigidity Theorem

By backward uniqueness for bounded mild 3D N–S solutions with nontrivial final data:

$$
\boxed{
v_\infty(x,\tau)
\equiv
b
\qquad
\text{on }
\mathbb R^3\times[-T,0].
}
$$

Since:

$$
T>0
$$

is arbitrary:

$$
\boxed{
v_\infty(x,\tau)
\equiv
b
\qquad
\forall
\tau\le0.
}
$$

---

# 21. Interpretation of the flat ancient profile

For:

$$
v_\infty\equiv b,
$$

$$
\boxed{
S[v_\infty]=0,
}
$$

$$
\boxed{
\omega[v_\infty]=0,
}
$$

$$
\boxed{
Q[v_\infty]=0,
}
$$

$$
\boxed{
\nabla^2q_\infty=0.
}
$$

Every derivative:

$$
D^kv_\infty
$$

for:

$$
k\ge1
$$

vanishes.

Thus:

# 22. C6-P.6: Flattening Kills Peak-Inherited TS/GP/HF

The flat ancient branch carries no nontrivial peak-local:

$$
TS,
\quad
GP,
\quad
HF
$$

defect state.

Therefore if the original defect persists:

$$
\boxed{
\textbf{its carrier must escape the bounded ancient peak frame}.
}
$$

---

# 23. Galilean triviality

The constant ancient field:

$$
b
$$

is removed by a Galilean change of coordinates.

Thus C6 labels it:

$$
\boxed{
\textbf{FLAT / Galilean-trivial ancient profile}.
}
$$

It is not a singular mechanism.

---

# 24. Nonflat branch

Now assume:

$$
\boxed{
a_1>0.
}
$$

This only says:

$$
\|\nabla v_n(0)\|_\infty
$$

has a nonzero global peak-frame limit.

It does not say the derivative carrier lies near:

$$
z=0.
$$

The derivative maximum can escape spatially.

---

# 25. Fixed-order local capture

For:

$$
k\ge1,
$$

Define:

$$
\boxed{
\Gamma_{k,n}^{loc}(R)
=
\frac{
\|D^kv_n(0)\|_{L^\infty(B_R)}
}{
\|D^kv_n(0)\|_\infty
}
\in[0,1]
}
$$

when the denominator is nonzero.

---

# 26. C6-P.7: Fixed-Order Carrier Dichotomy

For fixed:

$$
k,
$$

after passing to a subsequence either:

## P-KVIS

there exist:

$$
R<\infty,
\qquad
\gamma_k>0
$$

such that:

$$
\boxed{
\Gamma_{k,n}^{loc}(R)
\ge
\gamma_k;
}
$$

or:

## P-KESC

for every fixed:

$$
R,
$$

$$
\boxed{
\Gamma_{k,n}^{loc}(R)
\to0.
}
$$

### Meaning

Because fixed-order amplitude cannot escape below the peak scale,

the remaining fixed-order fiber escape is **spatial carrier escape**.

---

# 27. Derivative-Carrier Translation Escape

P-KESC is called:

$$
\boxed{
\textbf{Derivative-Carrier Translation Escape}.
}
$$

The global:

$$
k
$$

-th derivative remains:

$$
O(1)
$$

in peak normalization,

but its maxima/high-set leave every bounded ancient peak region.

This is the corrected replacement for C6-O's fixed-order derivative-tower branch.

---

# 28. Local fixed-order inheritance

In P-KVIS,

strong:

$$
C^k_{\rm loc}
$$

convergence implies a nontrivial:

$$
D^kv_\infty
$$

on a fixed bounded peak region,

provided the selected component/sign carrier itself is also tight.

Thus fixed-order ancient derivative defects become local compactness problems.

---

# 29. HF ancient geometry setup

Fix:

$$
k.
$$

Let:

$$
E_{k,n}^{\sigma,i,\zeta}
=
\{
z:
\sigma D^\zeta v_{n,i}(z,0)
>
\lambda
\widehat A_{k,n}^{peak}
\}.
$$

Assume:

1.:
   $$
   \widehat A_{k,n}^{peak}
   \to
   A_k^\infty>0;
   $$
2. a selected carrier:
   $$
   E_{k,n}\cap B_R
   $$
   has nonzero local geometric mass;
3. the inequality has a strict margin;
4.:
   $$
   v_n\to v_\infty
   $$
   in:
   $$
   C^k(B_R).
   $$

Then the selected component/sign geometry passes to:

$$
v_\infty.
$$

---

# 30. C6-P.8: Conditional Fixed-Order Ancient HF Geometry Inheritance

Under the assumptions of §29:

$$
\boxed{
HF_{k,\rm geom}^{anc}
}
$$

exists as a local ancient defect state.

It preserves:

- derivative order:
  $$
  k;
  $$
- selected component/sign;
- local threshold geometry;
- strict sign margin;
- local absolute carrier load.

### Guard

This is **not yet** a Grujić–Xu theorem state.

---

# 31. Why Grujić–Xu theorem status does not automatically inherit

The Grujić–Xu higher-order regularity theorem was formulated for a finite-time N–S solution in a particular derivative-chain/theorem-window setup.

A bounded ancient profile may:

- lack the original finite-energy/global assumptions;
- have a different record/escape-time identity;
- have derivative maxima at spatial infinity;
- require new theorem-window selection.

Therefore:

$$
\boxed{
HF_{k,\rm geom}^{anc}
\neq
H_{\rm GX}^{anc}
}
$$

unless the theorem setup is reverified.

---

# 32. Ancient HF setup flag

Define:

$$
\boxed{
\mathsf{Setup}_{GX}^{anc}
\in\{0,1\}.
}
$$

Only:

$$
\mathsf{Setup}_{GX}^{anc}=1
$$

allows use of the harmonic/sparseness gate on the ancient profile.

This is a new legality interface.

---

# 33. Order-index escape

Even though every fixed:

$$
k
$$

is controlled,

one may choose:

$$
k_n\to\infty.
$$

But C6-P.4 shows raw derivative growth at:

$$
k_n
$$

can be ordinary analytic growth.

Thus define:

$$
\boxed{
\textbf{Order-Geometry Escape}
}
$$

only if the **normalized geometry/theorem carrier** escapes with:

$$
k_n,
$$

not merely:

$$
A_{k_n}\to\infty.
$$

---

# 34. High-order analytic guard

A high-order branch is physically meaningful only if at least one of:

- factorial-normalized root;
- sign-geometry occupancy;
- harmonic bad-core state;
- theorem clock/root ratio;
- source/provenance metadata;

has a nontrivial order-asymptotic defect.

Large:

$$
A_k
$$

alone is insufficient.

This reuses the C5-H static all-order no-go at the ancient peak level.

---

# 35. Local strain/vorticity convergence

Because:

$$
v_n
\to
v_\infty
$$

in:

$$
C^\infty_{\rm loc},
$$

on every compact cylinder:

$$
\boxed{
S[v_n]\to S[v_\infty],
}
$$

$$
\boxed{
\omega[v_n]\to\omega[v_\infty],
}
$$

and:

$$
\boxed{
Q[v_n]\to Q[v_\infty].
}
$$

Thus local finite-dimensional geometry has excellent ancient compactness.

---

# 36. Peak-local GP carrier

Fix:

$$
R_0<\infty.
$$

Assume:

$$
\boxed{
\int_{B_{R_0}}
|Q[v_n](z,0)|dz
\ge
q_0>0.
}
$$

Assume also strict:

- middle-gap;
- strain-direction;
- compressive-axis;

margins.

Then the corresponding Q-weighted carrier probabilities are tight and converge after passing to a subsequence under local:

$$
L^1
$$

convergence.

---

# 37. GP geometric inheritance

Let:

$$
K
$$

be a strong-middle cone center.

If:

$$
S[v_n]/|S[v_n]|
$$

lies in a strict cone around:

$$
K
$$

for all but a Q-weighted leakage:

$$
\epsilon_Q<\epsilon_0
$$

uniformly on:

$$
B_{R_0},
$$

then the same strict inequality passes to:

$$
v_\infty
$$

after reducing the margin harmlessly.

Thus:

$$
\boxed{
\textbf{Q/strain geometry is locally ancient-stable}.
}
$$

---

# 38. Peak pressure Hessian setup

Write the whole-space pressure Hessian schematically:

$$
\boxed{
\nabla^2q_n
=
\mathcal H(
v_n\otimes v_n
),
}
$$

where:

$$
\mathcal H
$$

is the corresponding second-derivative pressure singular integral.

For:

$$
R>2R_0,
$$

split:

$$
\boxed{
\nabla^2q_n
=
\nabla^2q_{n,\le R}
+
\nabla^2q_{n,>R}.
}
$$

---

# 39. Uniform tail bound

Record peak boundedness:

$$
|v_n|\le1
$$

on:

$$
\tau\le0.
$$

For:

$$
z\in B_{R_0},
$$

the far pressure-Hessian kernel gives:

$$
\begin{aligned}
|
\nabla^2q_{n,>R}(z,\tau)
|
&\le
C
\int_{|y|>R}
|z-y|^{-5}
|v_n(y,\tau)|^2dy
\\
&\le
C_{R_0}
R^{-2}.
\end{aligned}
$$

Therefore:

# 40. C6-P.9: Uniform Peak Pressure-Tail Closure

$$
\boxed{
\sup_{
n,\tau\le0,z\in B_{R_0}
}
|
\nabla^2q_{n,>R}
|
\le
C_{R_0}R^{-2}.
}
$$

Thus:

$$
\boxed{
\lim_{R\to\infty}
\sup_n
\|
\nabla^2q_{n,>R}
\|_{L^\infty(B_{R_0})}
=
0.
}
$$

---

# 41. Finite-radius pressure convergence

For fixed:

$$
R,
$$

the pressure source:

$$
v_n\otimes v_n
$$

converges strongly on:

$$
B_R
$$

under local:

$$
C^0
$$

convergence.

With the standard principal-value/local pressure representation,

the finite-radius pressure-Hessian contribution converges locally:

$$
\boxed{
\nabla^2q_{n,\le R}
\to
\nabla^2q_{\infty,\le R}.
}
$$

---

# 42. C6-P.10: Peak-Local Pressure Hessian Closure Theorem

Fix:

$$
R_0.
$$

First let:

$$
n\to\infty
$$

at fixed:

$$
R>2R_0,
$$

then let:

$$
R\to\infty.
$$

Using C6-P.9:

$$
\boxed{
\nabla^2q_n
\to
\nabla^2q_\infty
}
$$

locally on:

$$
B_{R_0}
$$

under the stated pressure representation/local convergence assumptions.

### Main meaning

$$
\boxed{
\textbf{the pressure Hessian of a bounded ancient peak is asymptotically determined by finite peak radii}.
}
$$

---

# 43. Pressure provenance at infinity removed

The mass-scale tail at:

$$
|z|\to\infty
$$

cannot carry an independent:

$$
O(1)
$$

peak pressure-Hessian state.

Therefore ancient GP provenance only needs to track:

- local peak core;
- finite-radius far source;
- the limit as the finite radius increases.

The infinite mass tail is not an independent GP Hessian carrier.

---

# 44. C6-P.11: Conditional Ancient GP Inheritance

Assume:

1. peak-local Q mass:
   $$
   \ge q_0>0;
   $$
2. strict strong-middle/directional margins;
3. mean/pressure response remains nondegenerate on the peak core;
4. pressure finite-radius provenance is legally repartitioned;
5. local convergence is strong enough.

Then:

$$
\boxed{
GP_{\rm loc}^{anc}
}
$$

is inherited by:

$$
v_\infty.
$$

Its pressure Hessian is the peak-local limit from C6-P.10.

---

# 45. Ancient GP state

Define:

$$
\boxed{
\Theta_{GP}^{anc}
=
\left\langle
Q\text{-load},
\vartheta,
[e_1],
\text{cone},
\nabla^2q,
\text{finite-radius provenance},
\text{signature}
\right\rangle.
}
$$

Cross-generation old provenance and old core identities are not inherited automatically.

---

# 46. Peak-local pressure signature

For a finite-radius harmonic/far component relative to:

$$
B_{R_0},
$$

define:

$$
F_{R_0,R}^{anc}
$$

from the source annulus/outside-core region up to:

$$
R.
$$

If:

$$
F_{R_0,R}^{anc}
$$

converges as:

$$
R\to\infty
$$

and has a nondegenerate determinant/signature gap,

the pressure signature becomes a legitimate ancient local state.

If the determinant tends to:

$$
0,
$$

the ancient state is on the signature boundary.

---

# 47. TS middle density

The positive middle source density:

$$
\boxed{
a_M[v]
=
\lambda_2^+(S[v])
|S[v]|^2
}
$$

is local in:

$$
v
$$

and its first derivatives.

Under:

$$
C^1_{\rm loc}
$$

convergence:

$$
\boxed{
a_M[v_n]
\to
a_M[v_\infty]
}
$$

locally.

Thus middle source absolute loads pass to the ancient profile under a nonzero local-mass assumption.

---

# 48. TS operator density is harder

C6-E/F used:

$$
\mathcal Q_{SV}
=
P_{st}
\left(
(v\cdot\nabla)S
+
S^2
+
\frac34
\omega\otimes\omega
\right).
$$

The projection:

$$
P_{st}
$$

onto the strain constraint space is nonlocal.

Therefore local:

$$
C^\infty
$$

convergence of:

$$
v_n
$$

does not by itself prove local convergence of:

$$
\mathcal Q_{SV}[v_n].
$$

---

# 49. Projected-operator tail

For fixed:

$$
R_0,
$$

split the source:

$$
F_n
=
(v_n\cdot\nabla)S_n
+
S_n^2
+
\frac34
\omega_n\otimes\omega_n
$$

into:

$$
F_{n,\le R}
+
F_{n,>R}.
$$

Define:

$$
\boxed{
\mathfrak T_{Pst,n}(R_0,R)
=
\|
P_{st}F_{n,>R}
\|_{X(B_{R_0})},
}
$$

for the local norm:

$$
X
$$

used by the intended TS theorem.

---

# 50. Projected-Operator Tail Gate

Define:

$$
\boxed{
\mathsf{Tail}_{Pst}^{anc}=0
}
$$

if:

$$
\boxed{
\lim_{R\to\infty}
\limsup_n
\mathfrak T_{Pst,n}(R_0,R)
=
0.
}
$$

If this fails:

$$
\boxed{
\textbf{Projected-Operator Tail Escape}
}
$$

remains.

Unlike pressure Hessian,

no universal:

$$
R^{-2}
$$

tail closure is proved here for:

$$
P_{st}.
$$

---

# 51. Why the pressure proof does not transfer automatically

Pressure Hessian kernel away from the core decays:

$$
|x-y|^{-5},
$$

which is integrable against a globally bounded source in three dimensions.

A generic order-zero Calderón–Zygmund kernel behaves:

$$
|x-y|^{-3},
$$

whose absolute tail is not integrable in three dimensions.

Therefore the boundedness:

$$
|v_n|\le1
$$

alone does not provide the same absolute far-tail closure for:

$$
P_{st}.
$$

Cancellation/provenance information is needed.

---

# 52. Conditional ancient TS inheritance

Assume:

1. local middle load remains:
   $$
   >m_0;
   $$
2. local operator load remains:
   $$
   >o_0;
   $$
3.:
   $$
   \mathsf{Tail}_{Pst}^{anc}=0;
   $$
4. source densities converge locally;
5. the peak time-window has a legal nondegenerate limit;
6. shared-source overlap stays:
   $$
   \Omega_{ST}\ge\omega_0.
   $$

Then:

$$
\boxed{
TS_{\rm loc}^{anc}
}
$$

passes to:

$$
v_\infty.
$$

### Status

$$
\boxed{
\mathrm{CONDITIONAL}.
}
$$

---

# 53. Ancient TS state

Define:

$$
\boxed{
\Theta_{TS}^{anc}
=
\left\langle
M_M,
M_O,
\Omega_{ST},
\Pi^\cap,
\vartheta,
\text{direction},
\text{time window},
\mathsf{Tail}_{Pst}
\right\rangle.
}
$$

This explicitly stores the nonlocal projected-operator tail.

---

# 54. Peak time normalization

For an original event duration:

$$
\Delta t_n,
$$

Define:

$$
\boxed{
\Theta_{t,n}^{peak}
=
A_n^2
\Delta t_n.
}
$$

C6-O separated:

-:
  $$
  \to0;
  $$
-:
  $$
  \to\Theta_\ast\in(0,\infty);
  $$
-:
  $$
  \to\infty.
  $$

C6-P keeps this as ancient inheritance metadata.

---

# 55. Instantaneous ancient label

If:

$$
\Theta_{t,n}^{peak}\to0,
$$

only one-time geometric/load information can pass directly.

Do not call the resulting object:

$$
TS^{anc}
$$

or dynamic:

$$
HF^{anc}
$$

without an independent persistence theorem.

It is:

$$
\boxed{
\textbf{instantaneous ancient defect geometry}.
}
$$

---

# 56. Finite-window ancient label

If:

$$
\Theta_{t,n}^{peak}
\to
\Theta_\ast
\in(0,\infty),
$$

and the carrier stays tight on the corresponding peak cylinder,

the full dynamic event can pass to a finite ancient-time interval.

This is the cleanest ancient inheritance regime.

---

# 57. Infinite-window ancient label

If:

$$
\Theta_{t,n}^{peak}\to\infty,
$$

one may select finite subwindows around a fixed ancient time only if the relevant defect reserves remain nondegenerate on them.

Otherwise the event may drift to:

$$
\tau\to-\infty
$$

or spread across the ancient history.

---

# 58. Ancient inheritance is not ancient recurrence

Even when:

$$
D^{anc}
$$

exists on:

$$
[-T,0],
$$

this does not prove it recurs for:

$$
\tau\to-\infty.
$$

A recurrent ancient defect state requires another theorem:

$$
\boxed{
D^{anc}(\tau_j)
\to
D_\ast
\qquad
\tau_j\to-\infty.
}
$$

No such general theorem is supplied by peak extraction.

---

# 59. Ancient recurrence + bounded critical norm

If an ancient defect state recurs while the field remains bounded in:

$$
L^3
$$

along a backward sequence,

Albritton–Barker's ancient:

$$
L^3
$$

Liouville theorem becomes an external kill gate.

But the peak ancient profile extracted from the original Type-II branch does not automatically satisfy this bound.

---

# 60. Flat ancient state and backward uniqueness

The flattening theorem is stronger than an ordinary Liouville statement:

if the final state is exactly the nonzero constant:

$$
b,
$$

backward uniqueness forces the entire ancient interval to be that constant solution.

Thus the flat branch is completely classified.

This is one of the few ancient branches C6 can eliminate at the defect level without additional global integrability.

---

# 61. Ancient derivative analyticity

Because:

$$
v_\infty
$$

is bounded ancient and smooth,

on every finite time slab:

$$
[-T,0]
$$

its spatial derivatives are bounded,

and each positive backward-time smoothing gap yields spatial analyticity.

Thus fixed-order ancient derivative states are regular objects.

The remaining difficulty is:

- spatial location;
- sign geometry;
- global theorem setup;

not derivative blow-up on the peak scale.

---

# 62. Order escape vs analyticity radius

If:

$$
k_n\to\infty,
$$

a raw derivative maximum may grow factorially even in a perfectly regular analytic profile.

Therefore the correct all-order carrier coordinate is not:

$$
A_{k_n},
$$

but a normalized root such as:

$$
\boxed{
\frac{
A_{k_n}^{1/(k_n+1)}
}{
(k_n!)^{1/(k_n+1)}
}.
}
$$

A genuine order-asymptotic defect would require this normalized quantity or the associated geometry to become critical.

---

# 63. Ancient Grujić–Xu root

For:

$$
v_\infty,
$$

define:

$$
\boxed{
\mathcal R_k^{anc}
=
\frac{
\|D^kv_\infty\|_\infty^{1/(k+1)}
}{
c^{k/(k+1)}
(k!)^{1/(k+1)}
}.
}
$$

On any ancient time slice with a uniform analytic radius:

$$
\boxed{
\sup_k
\mathcal R_k^{anc}
<\infty.
}
$$

Thus **order root blow-up** is incompatible with a fixed positive ancient analyticity radius.

---

# 64. What high-order HF can still do

Even with:

$$
\mathcal R_k^{anc}
$$

bounded,

the component/sign high sets can change with:

$$
k,
$$

and spatial carrier locations may escape.

Therefore the surviving ancient high-order problem is:

$$
\boxed{
\textbf{high-order sign geometry + carrier location},
}
$$

not raw amplitude escalation.

---

# 65. Pressure closure advantage

Among the ancient C6 labels:

$$
GP
$$

has a special structural advantage:

its nonlocal pressure **Hessian** channel closes at infinity through:

$$
R^{-2}
$$

tail decay in the bounded peak frame.

TS projected operator does not share this simple absolute tail control.

HF derivative fields are local but their global maxima may escape spatially.

Thus:

$$
\boxed{
GP^{anc}_{loc}
}
$$

is currently the most spatially closed ancient joint state.

---

# 66. Ancient GP remaining loopholes

Even after pressure tail closure:

- mean-strain rotation may absorb forcing;
- one/two-negative signature branches remain;
- local/far finite-radius provenance may switch;
- GP state need not recur in ancient time.

So pressure closure does not solve ancient GP recurrence.

---

# 67. Ancient HF remaining loopholes

Fixed-order scale escape is removed,

but:

- derivative carrier translation;
- sign geometry;
- order-index escape;
- theorem setup;

remain.

This is a much smaller frontier than C6-O.

---

# 68. Ancient TS remaining loopholes

- projected-operator tail;
- shared-source time persistence;
- source-carrier spatial escape;
- ancient-time recurrence.

These replace the earlier generic noncompactness.

---

# 69. Type-II Euler route

Some Type-II scenarios may be more naturally rescaled using Euler scaling rather than record-amplitude N–S scaling.

Seregin's 2026 analysis provides a rigorous example of this strategy for particular local scenarios.

C6-P therefore keeps:

$$
\boxed{
\mathsf{EULER}_{II}
}
$$

as a separate external branch.

The record-peak fixed-order derivative rigidity derived here concerns the exact N–S peak rescaling route.

---

# 70. Ancient state taxonomy

C6-P defines:

## P-A0 — FLAT

$$
\boxed{
v_\infty\equiv b.
}
$$

No peak-local TS/GP/HF.

## P-AGP

$$
\boxed{
GP_{\rm loc}^{anc}.
}
$$

Q/geometry + peak-local pressure closure.

## P-AHF

$$
\boxed{
HF_{k,\rm geom}^{anc}.
}
$$

Fixed-order local derivative/sign state.

## P-ATS

$$
\boxed{
TS_{\rm loc/proj}^{anc}.
}
$$

Local middle source + projected-operator tail gate.

## P-ESC

$$
\boxed{
\text{Spatial Carrier Escape}.
}
$$

The relevant fixed-order defect carrier leaves every bounded peak region.

## P-ORD

$$
\boxed{
\text{Order-Geometry Escape}.
}
$$

Only an order-asymptotic normalized geometry/theorem defect remains.

---

# 71. C6-P.12: Ancient Peak-State Reduction

For a Type-II record-peak sequence with bounded ancient limit,

after fixed-order derivative rigidity and pressure-tail closure,

every peak-scale C6 defect branch reduces to:

$$
\boxed{
\text{FLAT}
\vee
GP_{\rm loc}^{anc}
\vee
HF_{k,\rm geom}^{anc}
\vee
TS_{\rm loc/proj}^{anc}
\vee
\text{Spatial Carrier Escape}
\vee
\text{Order-Geometry Escape}.
}
$$

### Important

There is no remaining fixed-order physical derivative-tower branch at the record peak scale.

---

# 72. Ancient defect inheritance graph

Schematic:

$$
\boxed{
D^{mass}
\to
D^{peak}
}
$$

requires:

- peak tightness;
- local absolute load;
- local convergence;
- fixed-order capture;
- time-window legality;
- nonlocal-tail control if required.

Then:

$$
\boxed{
D^{peak}
\to
D^{anc}.
}
$$

If any condition fails:

$$
\boxed{
\text{carrier escapes}
}
$$

rather than producing a false ancient label.

---

# 73. Ancient Liouville interfaces

Current external kill gates include:

## P-L1

Ancient:

$$
L^3
$$

bounded along a backward sequence.

## P-L2

Type-I decay ancient profiles.

## P-L3

special symmetry / axisymmetric classes.

## P-L4

fixed/periodic/asymptotically DSS critical field profiles under the corresponding hypotheses.

## P-L5

FLAT branch by backward uniqueness.

Only P-L5 is automatic from the stated flattening antecedent.

---

# 74. Peak-local pressure closure and ancient Liouville

Because GP pressure Hessian is finite-radius determined,

if one obtains an ancient GP profile in a rigidity class,

remote mass tails do not obstruct the local pressure geometry needed for the Liouville analysis.

This strengthens the potential utility of ancient GP states relative to generic mass-scale GP states.

---

# 75. Record peak frame as a derivative regulator

The record peak normalization has a conceptual interpretation:

$$
\boxed{
A_0
}
$$

sets the parabolic scale:

$$
a_n=A_0^{-1}.
$$

Boundedness backward in time then forces every fixed derivative order to satisfy:

$$
A_k
\lesssim
A_0^{k+1}.
$$

Thus the record peak frame is a universal fixed-order derivative regulator.

This is analogous to converting raw derivative blow-up into normalized bounded shape variables.

---

# 76. Relation to Type-I scaling

In a Type-I branch:

$$
A_0
\lesssim
(T^\ast-t)^{-1/2}.
$$

Peak scale:

$$
a_n
$$

is comparable from below to the parabolic singular scale.

In Type-II:

$$
A_0
\sqrt{T^\ast-t}
\to\infty,
$$

so:

$$
a_n
\ll
\sqrt{T^\ast-t}.
$$

Yet the fixed-order derivative regulator remains valid in either record-peak normalization.

---

# 77. Derivative ratios as ancient state coordinates

Define:

$$
\boxed{
\mathbf A^{peak}
=
\left(
\widehat A_1^{peak},
\widehat A_2^{peak},
\ldots
\right).
}
$$

For each finite truncation:

$$
k\le K,
$$

the vector lies in a compact box:

$$
\boxed{
0\le
\widehat A_k^{peak}
\le
C_k.
}
$$

Hence every finite derivative-order state can be compactified without introducing new physical scales.

---

# 78. Infinite derivative vector caveat

The infinite product:

$$
\prod_{k\ge1}
[0,C_k]
$$

is compact in the product topology,

but that topology is too weak to control analyticity radius or high-order geometry by itself.

Thus C6 should keep:

- finite-order compactness;
- analytic/order root metadata;

separate.

---

# 79. Defect label inheritance and product topology

A TS/GP/HF label uses only finitely many derivatives at any fixed theorem/order stage,

so ancient local inheritance is compatible with finite-order:

$$
C^\infty_{\rm loc}
$$

convergence.

A chain with:

$$
k_n\to\infty
$$

is a different object and must be encoded in the order-asymptotic state.

---

# 80. Major semantic correction to C6-O

C6-O treated:

$$
\widehat A_k^{peak}\to\infty
$$

as a generic fixed-order route.

C6-P proves:

$$
\boxed{
\textbf{this cannot occur at record-amplitude peaks for any fixed }k.
}
$$

So any future file must replace:

$$
\text{DERIVATIVE-RESTART}
$$

by:

$$
\boxed{
\text{FIXED-ORDER SPATIAL ESCAPE}
\vee
\text{ORDER-GEOMETRY ESCAPE}.
}
$$

---

# 81. What C6-P eliminates

## P-DEL1

$$
\text{fixed-order derivative amplitude can outrun }A_0^{k+1}
\text{ at record peaks}.
$$

FALSE.

## P-DEL2

$$
\text{every high }A_k
\text{ creates a smaller physical peak scale}.
$$

FALSE.

## P-DEL3

$$
k\to\infty
\text{ raw derivative growth is automatically singular}.
$$

FALSE due to analytic factorial baseline.

## P-DEL4

$$
\widehat A_1^{peak}\to0
\text{ leaves an unknown ancient defect profile}.
$$

FALSE; the ancient limit is constant by backward uniqueness.

## P-DEL5

$$
\text{remote global mass tail can keep an independent }O(1)
\text{ pressure-Hessian state at the peak}.
$$

FALSE.

## P-DEL6

$$
\text{local velocity convergence automatically gives local }P_{st}\text{ operator convergence}.
$$

FALSE.

## P-DEL7

$$
\text{fixed-order HF geometry implies Grujić--Xu ancient theorem status}.
$$

FALSE without setup revalidation.

---

# 82. What remains open

## P-O1 — Projected-operator tail

Can:

$$
P_{st}
$$

tail be localized using additional cancellation/provenance from bounded ancient N–S?

## P-O2 — Ancient GP rigidity

Can nontrivial:

$$
GP_{\rm loc}^{anc}
$$

be classified or killed?

## P-O3 — Ancient HF geometry

Can fixed-order sign geometry recur indefinitely in a bounded ancient field?

## P-O4 — Order-geometry escape

Can:

$$
k_n\to\infty
$$

carry a genuine normalized geometric defect despite uniform analyticity?

## P-O5 — Spatial carrier escape

Can derivative/source carriers repeatedly escape to:

$$
|z|\to\infty
$$

while peak velocity stays nontrivial at:

$$
z=0?
$$

## P-O6 — Ancient TS recurrence

Can shared middle/operator events recur toward:

$$
\tau\to-\infty?
$$

## P-O7 — Type-II Euler interface

Which C6 normalized geometry survives Seregin-type Euler zooms?

---

# 83. Strategic interpretation

C6-O left a three-scale Type-II picture:

$$
\text{mass}
\gg
\text{peak}
\gg
\text{derivative}.
$$

C6-P now shows:

$$
\boxed{
\textbf{the last inequality is false for every fixed derivative order
when the peak is chosen at amplitude record times}.
}
$$

Record peak boundedness and parabolic smoothing give:

$$
A_k
\lesssim
A_0^{k+1}
$$

for fixed:

$$
k.
$$

Space analyticity then shows that high-order raw growth is the ordinary analytic baseline unless a normalized order/geometry quantity becomes critical.

So the Type-II structure simplifies back to:

$$
\boxed{
\text{mass scale}
\gg
\text{bounded ancient peak scale},
}
$$

plus possible:

- spatial carrier escape;
- order-index geometry escape.

At the same time,

the GP pressure problem simplifies dramatically:

$$
\boxed{
\textbf{pressure Hessian at a bounded ancient peak is peak-local in the large-radius limit}.
}
$$

The global mass tail cannot sustain the GP state from infinity.

The remaining genuinely nonlocal ancient difficulty is now:

$$
\boxed{
P_{st}
}
$$

inside the TS/operator channel.

Thus the most valuable next paper is no longer another derivative-scale restart.

It is:

> **Can bounded ancient defect states themselves recur or persist,
> once fixed derivative tower and pressure-tail escape are removed?**

---

# 84. Proposed C6-Q

$$
\boxed{
\textbf{C6-Q — Ancient Defect Rigidity,
Projected-Operator Tail Control,
and Spatial Carrier Escape}.
}
$$

---

# 85. C6-Q proof obligations

## Q1 — projected strain-operator kernel

Write:

$$
P_{st}
$$

in explicit Riesz/CZ form and identify cancellation structure.

## Q2 — ancient operator tail

Determine conditions under which:

$$
\mathsf{Tail}_{Pst}^{anc}=0.
$$

## Q3 — TS ancient closure

If operator tail closes, classify:

$$
TS^{anc}.
$$

## Q4 — GP ancient pressure recurrence

Use peak-local pressure closure to study backward-time recurrence/provenance.

## Q5 — fixed-order HF ancient geometry

Study sign-thick/sparse carrier dynamics with all amplitudes uniformly normalized.

## Q6 — carrier escape at peak infinity

Relate:

$$
|z_n|\to\infty
$$

to physical center motion:

$$
a_n|z_n|.
$$

## Q7 — order-asymptotic geometry

Combine ancient analyticity with Grujić–Xu factorial roots to constrain:

$$
k_n\to\infty.
$$

## Q8 — ancient backward uniqueness

Look for nontrivial final-state symmetries/degeneracies beyond FLAT which can be propagated backward.

## Q9 — external ancient Liouville gates

Audit which ancient TS/GP/HF states fall into known Liouville classes.

## Q10 — ancient carrier graph

Recompute only the peak-inherited ancient states plus spatial/order escape.

---

# 86. Major no-go audit

### NG-P1

$$
\text{record peak frame allows fixed-order derivative tower}.
$$

FALSE.

### NG-P2

$$
\text{high-order raw derivative growth}\Rightarrow\text{new scale}.
$$

FALSE.

### NG-P3

$$
\text{flattening ancient peak may hide TS/GP/HF}.
$$

FALSE.

### NG-P4

$$
\text{fixed-order derivative noncompactness must be scale escape}.
$$

FALSE; spatial carrier escape remains.

### NG-P5

$$
\text{pressure mass tail remains an independent ancient GP driver}.
$$

FALSE for pressure Hessian.

### NG-P6

$$
\text{TS projected operator has the same tail closure as pressure Hessian}.
$$

FALSE / NOT PROVED.

### NG-P7

$$
\text{ancient local HF geometry automatically activates the Grujić--Xu theorem}.
$$

FALSE.

### NG-P8

$$
\text{ancient inheritance}\Rightarrow\text{ancient recurrence}.
$$

FALSE.

---

# 87. X-Integration guards update

## G-RECPEAKDER

At record amplitude peaks preserve:

$$
A_k/A_0^{k+1}\le C_k.
$$

## G-ANBASE

Compare high-order growth to analytic/factorial baseline.

## G-FLATBU

A constant ancient final state propagates backward by bounded-mild backward uniqueness.

## G-KLOC

Fixed-order derivative carrier stores local-capture ratio:

$$
\Gamma_k^{loc}(R).
$$

## G-PLOCAL

Ancient GP pressure Hessian uses finite-radius provenance and tail closure.

## G-PSTTAIL

TS operator inheritance stores projected-operator tail explicitly.

## G-ANSETUP

Ancient HF geometry and ancient Grujić–Xu theorem status are distinct types.

## G-ANCREC

Ancient inheritance and ancient recurrence are distinct.

---

# 88. True ETN update

Ancient peak state:

$$
\boxed{
\Theta_{peak}^{C6P}
=
\left\langle
v_\infty,
\{\widehat A_k^{peak}\},
\rho_{an},
\{\Gamma_k^{loc}\},
\Theta_{GP}^{anc},
\Theta_{HF}^{anc},
\Theta_{TS}^{anc},
\mathsf{Tail}_{Pst},
\text{pressure tail},
\text{carrier escape}
\right\rangle.
}
$$

Ancient classes:

$$
\boxed{
\mathfrak A^{C6P}
=
\{
\text{FLAT},
\text{GP-ANC},
\text{HF-ANC},
\text{TS-ANC},
\text{SPATIAL-ESCAPE},
\text{ORDER-ESCAPE}
\}.
}
$$

---

# 89. Formal status

$$
\boxed{
\begin{aligned}
\text{record peak backward }L^\infty\text{ bound}
&:\ \mathrm{PROVED},\\
\text{fixed-order derivative bound}
&:\ \mathrm{EXTERNAL/PROVED},\\
A_k\le C_kA_0^{k+1}
&:\ \mathrm{PROVED},\\
\text{fixed-order derivative-tower restart}
&:\ \mathrm{NO\mbox{-}GO/PROVED},\\
\text{uniform peak spatial analyticity}
&:\ \mathrm{EXTERNAL/PROVED\ INTERFACE},\\
\text{factorial-normalized root control}
&:\ \mathrm{PROVED\ FROM\ ANALYTICITY},\\
\text{raw high-order derivative as physical scale}
&:\ \mathrm{REJECTED},\\
\text{flattening}\Rightarrow\text{constant ancient profile}
&:\ \mathrm{PROVED\ USING\ EXTERNAL\ BACKWARD\ UNIQUENESS},\\
\text{flattening peak-inherited TS/GP/HF}
&:\ \mathrm{NO\mbox{-}GO/PROVED},\\
\text{fixed-order local-capture dichotomy}
&:\ \mathrm{PROVED},\\
\text{fixed-order ancient HF geometry}
&:\ \mathrm{CONDITIONAL},\\
\text{ancient GX theorem status}
&:\ \mathrm{NOT\ AUTOMATIC},\\
\text{peak pressure-tail }O(R^{-2})
&:\ \mathrm{PROVED},\\
\text{peak-local pressure Hessian closure}
&:\ \mathrm{PROVED\ UNDER\ LOCAL\ CONVERGENCE},\\
\text{ancient GP inheritance}
&:\ \mathrm{CONDITIONAL},\\
\text{middle-source ancient inheritance}
&:\ \mathrm{CONDITIONAL/LOCAL},\\
\text{projected-operator ancient inheritance}
&:\ \mathrm{OPEN\ WITHOUT\ TAIL\ CONTROL},\\
\text{ancient recurrence}
&:\ \mathrm{OPEN},\\
\text{global regularity}
&:\ \mathrm{OPEN}.
\end{aligned}
}
$$

---

# 90. Conclusion

C6-O left a possible:

$$
\boxed{
\text{Subpeak Derivative Restart}
}
$$

under:

$$
A_k/A_0^{k+1}\to\infty.
$$

C6-P now proves this is impossible for every **fixed derivative order** at record amplitude peaks.

The reason is simple but strong:

record peak rescaling gives:

$$
\|v_n\|_\infty\le1
$$

on a fixed backward interval,

and bounded mild N–S smoothing gives:

$$
\boxed{
\|D^kv_n(0)\|_\infty
\le
C_k.
}
$$

Hence:

$$
\boxed{
A_k
\le
C_kA_0^{k+1}.
}
$$

So no fixed:

$$
k
$$

can generate a physical scale:

$$
\ll
A_0^{-1}.
$$

For:

$$
k\to\infty,
$$

space analyticity shows factorial raw derivative growth is normal.

Therefore the high-order problem must use:

$$
\boxed{
\textbf{factorial-normalized roots + geometry},
}
$$

not raw:

$$
A_k.
$$

Next,

if:

$$
A_1/A_0^2\to0,
$$

the ancient peak has constant final data:

$$
b.
$$

Bounded-mild backward uniqueness then gives:

$$
\boxed{
v_\infty\equiv b
}
$$

for all ancient time.

So the flat branch is completely derivative-trivial:

$$
\boxed{
TS=GP=HF=0
}
$$

at the peak.

The old defect, if any, must live elsewhere.

If the peak is nonflat,

fixed-order derivative defects have only two choices:

$$
\boxed{
\text{local ancient capture}
}
$$

or:

$$
\boxed{
\text{spatial carrier escape}.
}
$$

There is no third fixed-order inner-scale route.

For GP,

C6-O/P gives an especially strong closure:

$$
\boxed{
\sup_{B_{R_0}}
|\nabla^2q_{>R}|
\lesssim
R^{-2}.
}
$$

Thus the huge relative critical-mass tail at peak infinity cannot sustain a finite peak GP pressure Hessian.

Peak GP pressure is asymptotically determined by finite peak radii,

and local Q/strain/pressure geometry can pass to the bounded ancient limit if its absolute load and margins survive.

The difficult ancient nonlocality is now instead the TS projected operator:

$$
P_{st}.
$$

Its generic order-zero tail does not enjoy the same absolutely integrable:

$$
|x|^{-5}
$$

kernel as pressure Hessian.

So the C6 ancient frontier has dramatically simplified:

$$
\boxed{
\text{FLAT}
\vee
GP_{\rm loc}^{anc}
\vee
HF_{k,\rm geom}^{anc}
\vee
TS_{\rm loc/proj}^{anc}
\vee
\text{Spatial Carrier Escape}
\vee
\text{Order-Geometry Escape}.
}
$$

There is **no fixed-order derivative tower left** at the record peak.

The next target is therefore:

$$
\boxed{
\textbf{C6-Q — Ancient Defect Rigidity,
Projected-Operator Tail Control,
and Spatial Carrier Escape}.
}
$$

---

# References

1. G. Koch, N. Nadirashvili, G. Seregin, V. Šverák, *Liouville theorems for the Navier–Stokes equations and applications*, arXiv:0709.3599.
2. Z. Lei, Z. Yang, C. Yuan, *Backward Uniqueness for 3D Navier-Stokes Equations with Non-trivial Final Data and Applications*, arXiv:2311.02429, revised March 2026.
3. L. Xu, *Local-in-time Solvability and Space Analyticity for the Navier-Stokes Equations with BMO-type Initial Data*, arXiv:1810.13085; Arch. Ration. Mech. Anal. 236 (2020), 389–417.
4. C. Wang, Y. Gao, X. Xue, *Joint space-time analyticity of mild solutions to the Navier-Stokes equations*, arXiv:2112.03079.
5. Z. Bradshaw, T.-P. Tsai, *On the local pressure expansion for the Navier-Stokes equations*, arXiv:2001.11526.
6. D. Albritton, T. Barker, *On local Type I singularities of the Navier-Stokes equations and Liouville theorems*, arXiv:1811.00502.
7. Z. Grujić, L. Xu, *Asymptotic Criticality of the Navier-Stokes Regularity Problem*, arXiv:1911.00974; J. Math. Fluid Mech. 26, 53 (2024).
8. G. Seregin, *On potential Type II blowups for the Navier-Stokes equations*, arXiv:2606.29468 (2026).

# Internal dependencies

- `NS_C6O_PeakScale_DefectInheritance_TypeII_TwoScale_v0.1.md`
- `NS_C6N_NearLossless_AncientProfile_DefectRigidity_v0.1.md`
- `NS_C6M_CarrierCompleteness_SpectralPressure_NestedRigidity_v0.1.md`
- `NS_C6L_SingularCarrier_Spectator_Rebinding_v0.1.md`
- `NS_C6K_CriticalFiber_ProfileSplitting_v0.1.md`
- `NS_C6J_LogScale_RenormalizedFlow_CriticalFiberEscape_v0.1.md`
- `NS_C6I_CriticalDebt_CapacityInfinity_BarrierCycles_v0.1.md`
- `NS_C6H_BoundaryFaces_DebtCoercivity_CycleElimination_v0.1.md`
- `NS_C6G_TypedCrossDomainGraph_SCC_BoundarySurvivors_v0.1.md`
- `NS_C6F_SharedSource_CoreExtraction_CrossDomainRouting_v0.1.md`
- `NS_C6E_TemporalSpatial_SharedSource_TTrap_v0.1.md`
- `NS_C6D_GeometryPressure_Provenance_SignatureReturn_v0.1.md`
- `NS_C6C_DuhamelCoherence_ReentryCriticalSaturation_v0.1.md`
- `NS_C6B_ForcingReentry_HF_CycleTest_v0.1.md`
- `NS_C6A_CertifiedDefectGraph_TypedCycles_MinimalSurvivors_v0.1.md`

Next:

$$
\boxed{
\textbf{C6-Q — Ancient Defect Rigidity,
Projected-Operator Tail Control,
and Spatial Carrier Escape}
}
$$