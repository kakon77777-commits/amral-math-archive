---
title: "Navier–Stokes C4-D: Amplitude-to-Flux Branching Bridge, Local Work Cancellation, and Helical-Cancellation Rigidity"
subtitle: "A Persistence-or-Work Theorem for Critical Shell Crossings and a Same-Event Reduction from Amplitude Growth to Source Overcapacity, Energy Work, or Helical/Spatial Cancellation"
version: "v0.1"
date: "2026-08-15"
author: "Neo.K / EveMissLab"
language: "en"
status: "Theorem-style shared-event coupling / structural reduction"
epistemic_status: "Exact first-crossing envelope calculus + band-limited localization + helical triad algebra. The final bridge is branching, not a direct amplitude-to-flux implication. Does NOT prove Navier–Stokes regularity."
---

# Navier–Stokes C4-D
# Amplitude-to-Flux Branching Bridge, Local Work Cancellation, and Helical-Cancellation Rigidity

## 0. Current Round Positioning

C4-C has established multiple same-event edges:

$$
\text{UV amplitude}
\to
\text{critical helical / strain / vorticity stock},
$$

$$
\text{robust heterochiral highest-mode gain}
\to
\text{positive helical variation},
$$

$$
\text{strain growth}
\to
\text{pressure}
\vee
\text{Betchov}
\vee
\text{vortex stretching},
$$

$$
\text{Miller operator escape}
\to
\text{advection}
\vee
S^2
\vee
\omega^2.
$$

However, the most critical hereditary UV anchor:

$$
a_q^\sigma(t)
=
\frac{
\|u_q^\sigma(t)\|_\infty
}{
\nu\lambda_q
}
$$

remains an amplitude event,

while the strongest antecedent of the helical triad coupling is:

$$
\boxed{
\text{positive high-mode nonlinear energy work}.
}
$$

C4-C has proven:

$$
\boxed{
\text{amplitude}
\not\Rightarrow
\text{flux}
}
$$

from norm data alone.

The work of C4-D:

> No longer pursues the false direct implication,
> but rather proves a branching bridge on the true N–S evolution.

Main results:

1. A critical shell first crossing must fall into:
   $$
   \boxed{
   \text{viscous-scale persistence}
   \vee
   \text{fast amplitude crossing};
   }
   $$
2. The positive amplitude variation of a fast crossing must be positively driven by the nonlinear source at the maximum point;
3. The output shell band-limit transforms the pointwise source into a shell-scale positive local nonlinear-work ball;
4. An integrated fast crossing must therefore pay:
   $$
   \boxed{
   \text{source-overcapacity impulse}
   \vee
   \text{positive shell nonlinear work}
   \vee
   \text{spatial work cancellation};
   }
   $$
5. This is the true **Amplitude-to-Work Branching Bridge**;
6. If the positive shell work is borne by the highest-rank robust heterochiral triads, it immediately synchronizes with critical helical production;
7. Robust helical cancellation is not an independent escape:
   negative pair production simultaneously implies negative highest-mode nonlinear work;
8. Therefore, robust helical cancellation can be reduced back to:
   $$
   \boxed{
   \text{high-mode work cancellation debt};
   }
   $$
9. The only truly remaining UV work escapes are:
   - non-top-rank gain;
   - homochiral gain;
   - radial-gap degeneration;
   - work cancellation;
10. Thus, the Amplitude-to-Flux Barrier of C4-C is partially closed:
    $$
    \boxed{
    \text{direct bridge FALSE},
    \quad
    \text{finite branching bridge TRUE}.
    }
    $$

---

# 1. Fresh primary-source audit

This round's fresh audit aligns with:

## Cheskidov–Dai

The frequency-localized vorticity regularity criteria confirm:

$$
\boxed{
\text{potential singularity must repeatedly pay a high-frequency critical toll}.
}
$$

However, it does not automatically yield the shell energy-flux sign.

## Waleffe 1992

The helical Fourier decomposition classifies triadic interactions by helicity signs,

and shows that different helical classes possess different energy-transfer directions and local/nonlocal transfer structures.

The triad ratio calculations in this round are built upon:

- triad energy conservation;
- triad helicity conservation;

without using turbulence statistical closure.

## Lei–Lin–Zhou

The critical helical energy identity confirms:

$$
\boxed{
\text{helical critical stock / pair-production is a true full N--S PDE quantity}.
}
$$

## Biferale–Titi

The single-helicity-sign decimated N–S possesses sign-definite critical helicity and is globally regular,

therefore the homochiral branch cannot be conflated with the full heterochiral production route.

---

# 2. Shell equation

Fix a dyadic shell:

$$
q
$$

and helicity:

$$
\sigma.
$$

Let:

$$
\boxed{
f(t,x)
=
u_q^\sigma(t,x)
=
\Delta_qP^\sigma u(t,x).
}
$$

Let:

$$
\lambda
=
\lambda_q.
$$

Define the shell nonlinear source:

$$
\boxed{
N(t,x)
=
\Delta_q
P^\sigma
\mathbb P
\nabla\cdot(u\otimes u).
}
$$

Then:

$$
\boxed{
\partial_tf
-
\nu\Delta f
+
N
=
0.
}
$$

The Fourier supports of $f$ and $N$ are both located in:

$$
|\xi|\asymp\lambda
$$

the fixed annulus.

Thus, by Bernstein's inequality:

$$
\boxed{
\|\nabla f\|_\infty
\le
C_f
\lambda
\|f\|_\infty,
}
$$

$$
\boxed{
\|\nabla N\|_\infty
\le
C_N
\lambda
\|N\|_\infty.
}
$$

---

# 3. Critical amplitude

Define:

$$
\boxed{
a(t)
=
\frac{
\|f(t)\|_\infty
}{
\nu\lambda
}.
}
$$

Fix:

$$
0<\beta_0<\beta_1.
$$

Let:

$$
t_1
$$

be a certain:

$$
\beta_1
$$

first / hysteretic crossing:

$$
\boxed{
a(t_1)=\beta_1.
}
$$

Let:

$$
t_0<t_1
$$

be the time of the last:

$$
a(t_0)=\beta_0
$$

before the crossing,

if it exists.

Then:

$$
\boxed{
a(t)>\beta_0
\qquad
t_0<t<t_1.
}
$$

---

# 4. Viscous window

Fix:

$$
\theta>0.
$$

Define:

$$
\boxed{
\tau_\lambda
=
\frac{
\theta
}{
\nu\lambda^2
}.
}
$$

Consider the backward window:

$$
\boxed{
I_\lambda
=
[t_1-\tau_\lambda,t_1].
}
$$

---

# 5. C4-D.1: Persistence-or-Fast-Crossing Dichotomy

## Theorem 5.1

For any:

$$
\beta_0<\beta_1,
$$

there must be:

## Branch D-PERSIST

$$
\boxed{
a(t)>\beta_0
\qquad
\forall t\in I_\lambda;
}
$$

or:

## Branch D-FAST

there exists:

$$
t_0\in I_\lambda
$$

such that:

$$
a(t_0)=\beta_0,
$$

$$
a(t_1)=\beta_1,
$$

and:

$$
\boxed{
t_1-t_0
\le
\frac{
\theta
}{
\nu\lambda^2
}.
}
$$

### Proof

If within the backward viscous window there is no:

$$
\beta_0
$$

crossing,

and:

$$
a(t_1)=\beta_1>\beta_0,
$$

by the definition of the last crossing,

the entire window can only maintain:

$$
a>\beta_0.
$$

Otherwise, the last crossing must fall within the window. $\square$

---

# 6. C4 synchronization meaning

Therefore, every:

$$
\beta_1
$$

crossing is not an arbitrary pulse.

It first already satisfies:

$$
\boxed{
\textbf{one full viscous window of UV persistence}
}
$$

or:

$$
\boxed{
\textbf{fast nonlinear crossing}.
}
$$

D-PERSIST can be directly routed back to the C4-A persistence-to-synchronization machinery.

Thus, C4-D truly only needs to study:

$$
\boxed{
\text{D-FAST}.
}
$$

---

# 7. Sup norm envelope

Let:

$$
\boxed{
M(t)
=
\|f(t)\|_\infty.
}
$$

In a smooth pre-singular interval,

$f$ and:

$$
\partial_tf
$$

are both continuous and band-limited,

therefore:

$$
M(t)
$$

is locally Lipschitz.

Moreover:

$$
f(t)\in L^2
$$

and band-limited,

so:

$$
f(t,x)\to0
$$

as:

$$
|x|\to\infty,
$$

therefore:

$$
M(t)
$$

is achieved at some:

$$
x_t
$$

.

---

# 8. Envelope derivative

At a.e. time where:

$$
M
$$

is differentiable,

there exists a maximizing point:

$$
x_t
$$

and:

$$
\boxed{
e_t
=
\frac{
f(t,x_t)
}{
M(t)
}
}
$$

such that:

$$
\boxed{
M'(t)
=
e_t\cdot
\partial_tf(t,x_t).
}
$$

This is a standard max-envelope / Danskin-type fact.

---

# 9. Sign of viscosity at the amplitude maximum

At:

$$
x_t
$$

we have:

$$
\nabla|f|^2=0,
$$

$$
\Delta|f|^2\le0.
$$

And:

$$
f\cdot\Delta f
=
\frac12
\Delta|f|^2
-
|\nabla f|^2.
$$

Therefore:

$$
\boxed{
e_t\cdot\Delta f(t,x_t)
\le0.
}
$$

---

# 10. C4-D.2: Positive Amplitude Variation Requires Positive Nonlinear Source

From the shell equation:

$$
\partial_tf
=
\nu\Delta f-N.
$$

So:

$$
M'
=
\nu e\cdot\Delta f
-
e\cdot N
\le
-
e\cdot N.
$$

Thus, at the differentiability times where:

$$
M'(t)>0
$$

:

$$
\boxed{
g(t)
:=
-e_t\cdot N(t,x_t)
\ge
M'(t)>0.
}
$$

This is an exact same-time amplitude/source coupling.

---

# 11. Positive variation budget of a fast crossing

In D-FAST:

$$
M(t_1)-M(t_0)
=
\nu\lambda
(\beta_1-\beta_0).
$$

Let:

$$
\Delta\beta
=
\beta_1-\beta_0.
$$

Since:

$$
M
$$

is absolutely continuous:

$$
\boxed{
\int_{t_0}^{t_1}
[M'(t)]_+dt
\ge
\nu\lambda
\Delta\beta.
}
$$

Therefore, a fast crossing must pay a fixed amplitude positive variation.

---

# 12. Source efficiency

When:

$$
M'(t)>0
$$

define:

$$
\boxed{
\eta(t)
=
\frac{
g(t)
}{
\|N(t)\|_\infty
}
\in(0,1].
}
$$

Fix:

$$
0<\eta_0<1.
$$

Define:

$$
G
=
\{
t:
M'(t)>0,\ 
\eta(t)\ge\eta_0
\},
$$

$$
B
=
\{
t:
M'(t)>0,\ 
\eta(t)<\eta_0
\}.
$$

---

# 13. Good/bad positive variation split

From:

$$
\int[M']_+
\ge
\nu\lambda\Delta\beta,
$$

at least:

## D-SRC

$$
\boxed{
\int_B
M'(t)dt
\ge
\frac12
\nu\lambda\Delta\beta,
}
$$

or:

## D-WORK

$$
\boxed{
\int_G
M'(t)dt
\ge
\frac12
\nu\lambda\Delta\beta.
}
$$

---

# 14. Source-overcapacity branch

On:

$$
B
$$

:

$$
g
<
\eta_0
\|N\|_\infty.
$$

And:

$$
g\ge M'.
$$

So:

$$
\boxed{
\|N(t)\|_\infty
>
\frac{
M'(t)
}{
\eta_0
}.
}
$$

Therefore:

## Theorem 14.1

If D-SRC holds,

$$
\boxed{
\frac1{
\nu\lambda
}
\int_B
\|N(t)\|_\infty dt
\ge
\frac{
\Delta\beta
}{
2\eta_0
}.
}
$$

This document refers to this as:

$$
\boxed{
\textbf{Nonlinear Source-Overcapacity Impulse}.
}
$$

---

# 15. Spatial stock of source-overcapacity

Since:

$$
N
$$

is band-limited,

Bernstein's inequality implies in reverse:

$$
\|N\|_2
\ge
c
\lambda^{-3/2}
\|N\|_\infty.
$$

So a large source-overcapacity also implies:

$$
\boxed{
\text{a large shell-local nonlinear-source stock}.
}
$$

Currently, there is no finite critical budget that can directly rule out this branch.

---

# 16. Local work density

In the D-WORK branch,

consider:

$$
t\in G.
$$

Let:

$$
x=x_t,
\quad
e=e_t,
\quad
M=M(t),
\quad
g=g(t).
$$

Define the nonlinear shell work density:

$$
\boxed{
w(t,y)
=
-f(t,y)\cdot N(t,y).
}
$$

At:

$$
y=x
$$

:

$$
\boxed{
w(t,x)
=
M g
>0.
}
$$

---

# 17. C4-D.3: Band-Limited Local Positive-Work Ball

## Theorem 17.1

There exists a universal:

$$
c_\ast>0
$$

depending only on the LP cutoff,

such that for:

$$
t\in G
$$

the ball:

$$
\boxed{
B_t
=
B
\left(
x_t,
c_\ast
\eta_0
\lambda^{-1}
\right)
}
$$

satisfies:

$$
\boxed{
w(t,y)
\ge
c_\ast
M(t)g(t)
\qquad
y\in B_t.
}
$$

### Proof

By Bernstein's inequality:

$$
|f(y)-Me|
\le
C_f
\lambda M|y-x|,
$$

$$
|N(y)-N(x)|
\le
C_N
\lambda
\|N\|_\infty
|y-x|.
$$

Take:

$$
|y-x|
\le
c_\ast\eta_0\lambda^{-1}.
$$

Since:

$$
g\ge
\eta_0\|N\|_\infty,
$$

we can make:

$$
-e\cdot N(y)
\ge
\frac34g,
$$

and:

$$
|f(y)-Me|
\le
\frac{
\eta_0
}{8}
M.
$$

Thus:

$$
-f(y)\cdot N(y)
\ge
\frac34Mg
-
\frac{\eta_0}{8}
M\|N\|_\infty
\ge
\frac58Mg.
$$

Adjusting the universal constant yields the result. $\square$

---

# 18. Local positive work rate

The ball volume:

$$
|B_t|
\asymp
\eta_0^3
\lambda^{-3}.
$$

So:

$$
\boxed{
L(t)
:=
\int_{B_t}
w(t,y)dy
\ge
c
\eta_0^3
\lambda^{-3}
M(t)
g(t).
}
$$

Moreover:

$$
g\ge M',
$$

and on the crossing interval:

$$
M(t)\ge
\nu\lambda\beta_0.
$$

Therefore:

$$
\boxed{
L(t)
\ge
c
\eta_0^3
\nu
\beta_0
\lambda^{-2}
M'(t).
}
$$

---

# 19. C4-D.4: Integrated Local Work Toll

If D-WORK holds:

$$
\int_GM'dt
\ge
\frac12
\nu\lambda\Delta\beta,
$$

So:

$$
\boxed{
\int_G
L(t)dt
\ge
c
\eta_0^3
\beta_0
\Delta\beta
\frac{
\nu^2
}{
\lambda
}.
}
$$

Multiplying by the critical weight:

$$
\lambda/\nu^2,
$$

we obtain:

$$
\boxed{
\frac{
\lambda
}{
\nu^2
}
\int_G
L(t)dt
\ge
c
\eta_0^3
\beta_0
\Delta\beta.
}
$$

This is the:

$$
\boxed{
\textbf{scale-invariant integrated local nonlinear-work toll}.
}
$$

---

# 20. Global shell nonlinear work

Define:

$$
\boxed{
W_q^\sigma(t)
=
-\int_{\mathbb R^3}
f(t,x)\cdot N(t,x)dx.
}
$$

The shell energy balance is:

$$
\boxed{
\frac12
\frac d{dt}
\|f\|_2^2
+
\nu
\|\nabla f\|_2^2
=
W_q^\sigma.
}
$$

Note that:

$$
W_q^\sigma
$$

is the **nonlinear shell energy input**,

not the total energy derivative after deducting viscosity.

---

# 21. Positive / negative spatial work variation

Define:

$$
\boxed{
W^+(t)
=
\int
[w(t,x)]_+
dx,
}
$$

$$
\boxed{
W^-(t)
=
\int
[-w(t,x)]_+
dx.
}
$$

Then:

$$
\boxed{
W_q^\sigma
=
W^+-W^-.
}
$$

and:

$$
W^+(t)\ge L(t)
$$

for:

$$
t\in G.
$$

---

# 22. C4-D.5: Local-to-Global Work Cancellation Identity

For any:

$$
t,
$$

$$
\boxed{
[W_q^\sigma(t)]_+
+
W^-(t)
\ge
W^+(t).
}
$$

Therefore, on the good-source set:

$$
\boxed{
[W_q^\sigma]_+
+
W^-
\ge
L.
}
$$

Integrating over time:

$$
\boxed{
\int_G
[W_q^\sigma]_+dt
+
\int_G
W^-dt
\ge
c
\eta_0^3
\beta_0
\Delta\beta
\frac{
\nu^2
}{
\lambda
}.
}
$$

---

# 23. C4-D.6: Amplitude-to-Work Branching Bridge

Define the dimensionless quantities:

$$
\boxed{
\mathfrak F_q
=
\frac{
\lambda
}{
\nu^2
}
\int_G
[W_q^\sigma(t)]_+
dt,
}
$$

$$
\boxed{
\mathfrak C_q^{sp}
=
\frac{
\lambda
}{
\nu^2
}
\int_G
W^-(t)dt.
}
$$

Then every D-FAST crossing satisfies at least one of the following:

## Source-overcapacity

$$
\boxed{
\frac1{
\nu\lambda
}
\int_B
\|N\|_\infty dt
\ge
\frac{
\Delta\beta
}{
2\eta_0
},
}
$$

or:

## Positive shell work

$$
\boxed{
\mathfrak F_q
\ge
c
\eta_0^3
\beta_0
\Delta\beta,
}
$$

or:

## Spatial work cancellation

$$
\boxed{
\mathfrak C_q^{sp}
\ge
c
\eta_0^3
\beta_0
\Delta\beta.
}
$$

This is the:

$$
\boxed{
\textbf{Amplitude-to-Work Branching Bridge}.
}
$$

---

# 24. C4-B synchronization consequence

Therefore, a critical shell crossing is now compressed into:

$$
\boxed{
\text{UV persistence}
}
$$

or:

$$
\boxed{
\text{source-overcapacity}
}
$$

or:

$$
\boxed{
\text{positive nonlinear energy work}
}
$$

or:

$$
\boxed{
\text{spatial work cancellation}.
}
$$

It cannot simply escape via a:

$$
\boxed{
\text{zero-duty amplitude pulse with no other debt}
}
$$

.

This is a truly N–S-specific result that goes beyond the C4-B generic pulse no-go.

---

# 25. Spatial work-cancellation geometry

At good-source times:

$$
w\ge cMg
$$

in:

$$
B_t.
$$

If the global work is heavily cancelled,

then there must be a comparable:

$$
W^-
$$

.

Moreover:

$$
|w|
\le
M
\|N\|_\infty
\le
\frac{
Mg
}{
\eta_0
}
$$

holds in the whole space only for $|f|\le M$.

Thus, if at some time:

$$
W^-
\ge
c
\eta_0^3
Mg\lambda^{-3},
$$

the negative-work set:

$$
\Omega_-
=
\{w<0\}
$$

must satisfy:

$$
\boxed{
|\Omega_-|
\ge
c
\eta_0^4
\lambda^{-3}.
}
$$

Therefore, strong spatial work cancellation requires another opposite-work region of shell-volume scale.

This document refers to this as the:

$$
\boxed{
\textbf{Work-Dipole / Work-Multiplicity Debt}.
}
$$

---

# 26. Triad decomposition of positive shell work

Now we only process the:

$$
\mathfrak F_q
$$

branch.

In a finite Galerkin truncation,

the shell nonlinear work can be decomposed into triad contributions:

$$
\boxed{
W_q^\sigma
=
\sum_{\tau\ni(q,\sigma)}
w_{\tau\to q,\sigma}.
}
$$

Define the positive variation:

$$
\boxed{
G_q^+
=
\sum_\tau
[w_{\tau\to q,\sigma}]_+.
}
$$

Then:

$$
\boxed{
G_q^+
\ge
[W_q^\sigma]_+.
}
$$

After time integration:

$$
\boxed{
\int_G
G_q^+dt
\ge
\int_G
[W_q^\sigma]_+dt.
}
$$

---

# 27. Rank split

The strongest helical table of C4-C assumes the receiving mode is the highest wavenumber in the triad.

So define:

$$
\boxed{
G_q^+
=
G_{\rm top}^+
+
G_{\rm nontop}^+.
}
$$

where:

## Top-rank

the receiving:

$$
q
$$

is the highest wavenumber in the triad.

## Non-top

there exists a participating mode in the triad with:

$$
r>q
$$

.

---

# 28. Rank-defect branch

If:

$$
G_{\rm nontop}^+
$$

accounts for the majority of the positive shell work,

then:

$$
\boxed{
\text{the amplitude-crossing shell is being fed by interactions
already involving still-higher absolute frequencies}.
}
$$

This does not necessarily mean the higher mode itself is critical-active,

but it indicates:

$$
\boxed{
\textbf{higher-frequency participation cannot be removed from provenance}.
}
$$

This document refers to this as the:

$$
\boxed{
\textbf{Rank-Defect / Higher-Frequency-Participation Branch}.
}
$$

---

# 29. Top-rank helical split

For:

$$
G_{\rm top}^+,
$$

subdivide further:

$$
\boxed{
G_{\rm top}^+
=
G_{\rm hom}^+
+
G_{\rm deg}^+
+
G_{\rm rob}^+.
}
$$

where:

- hom = homochiral Class I;
- deg = II/III radial-gap degenerate;
- rob = robust heterochiral II/III/IV.

---

# 30. Robust heterochiral coefficient

For:

$$
\tau\in\mathrm{rob},
$$

C4-C has proven the existence of:

$$
c_\ast=c(c_L,\delta)>0
$$

such that:

$$
\boxed{
\mathcal R_\tau
=
\kappa_\tau
q_\tau
\dot e_{q_\tau},
}
$$

where:

$$
\boxed{
c_\ast
\le
\kappa_\tau
\le
1.
}
$$

Important:

This identity holds for both:

$$
\dot e_q>0
$$

and:

$$
\dot e_q<0
$$

,

because:

$$
\mathcal R_\tau
$$

has the same sign as the nonlinear energy derivative of the highest mode.

---

# 31. C4-D.7: Helical Cancellation Forces High-Mode Work Cancellation

For the robust heterochiral top-rank pool, define:

$$
\boxed{
X_+
=
\sum_{\tau\in rob}
[q_\tau\dot e_{q_\tau}]_+,
}
$$

$$
\boxed{
X_-
=
\sum_{\tau\in rob}
[-q_\tau\dot e_{q_\tau}]_+.
}
$$

critical helical variations:

$$
P_+
=
\sum_{\tau\in rob}
[\mathcal R_\tau]_+,
$$

$$
P_-
=
\sum_{\tau\in rob}
[-\mathcal R_\tau]_+.
$$

Then:

$$
\boxed{
c_\ast X_+
\le
P_+
\le
X_+,
}
$$

and:

$$
\boxed{
c_\ast X_-
\le
P_-
\le
X_-.
}
$$

If:

$$
\boxed{
P_+-P_-
\le
\eta
c_\ast
X_+
}
$$

for:

$$
0<\eta<1,
$$

then:

$$
P_-
\ge
(1-\eta)c_\ast X_+.
$$

And:

$$
P_-\le X_-.
$$

So:

$$
\boxed{
X_-
\ge
(1-\eta)c_\ast X_+.
}
$$

### Conclusion

$$
\boxed{
\textbf{robust helical cancellation}
\Rightarrow
\textbf{comparable negative highest-mode energy work}.
}
$$

Helical cancellation is not a completely independent new escape.

It must revert to high-mode work cancellation.

---

# 32. This is stronger than C4-C

C4-C only had:

$$
\boxed{
P_+
\text{ large}
\Rightarrow
\text{net helicity}
\vee
P_-\text{ cancellation}.
}
$$

C4-D now compresses the second branch further into:

$$
\boxed{
P_-\text{ cancellation}
\Rightarrow
X_-\text{ high-mode back-transfer}.
}
$$

So in the robust sector:

$$
\boxed{
\text{helical cancellation}
}
$$

is actually just:

$$
\boxed{
\textbf{the critical-weighted image of energy-work cancellation}.
}
$$

---

# 33. Positive shell work → helical branching edge

If the positive shell-work branch:

$$
\mathfrak F_q
\ge
F_0,
$$

and in the integrated positive triad variation:

1. the non-top fraction is not dominant;
2. the homochiral fraction is not dominant;
3. the radial-degenerate fraction is not dominant;

then the robust heterochiral top-rank:

$$
X_+
$$

has a fixed fraction lower bound.

At this point, at least:

## D-HNET

$$
\boxed{
\text{net positive critical helical production}
}
$$

or:

## D-HCANCEL

$$
\boxed{
\text{comparable negative high-mode work variation}.
}
$$

Therefore, shell positive work cannot disappear cost-free in the robust heterochiral sector via 'pure helical cancellation'.

---

# 34. Full amplitude-crossing branch tree

A:

$$
\beta_0\to\beta_1
$$

critical shell first crossing must now enter:

---

## Branch A — Viscous persistence

$$
\boxed{
a_q^\sigma(t)\ge\beta_0
}
$$

through one full preceding viscous window.

---

## Branch B — Nonlinear source overcapacity

$$
\boxed{
\frac1{\nu\lambda}
\int
\|N_q^\sigma\|_\infty dt
\gtrsim
1.
}
$$

---

## Branch C — Spatial work cancellation

$$
\boxed{
\frac\lambda{\nu^2}
\int
W_q^-dt
\gtrsim
1.
}
$$

accompanied by an opposite-work region / work multiplicity.

---

## Branch D — Rank defect

Positive shell input is primarily borne by triads involving still-higher absolute frequencies.

---

## Branch E — Homochiral top-rank gain

pair-production silent / sign-definite-helicity-like transfer structure.

---

## Branch F — Radial-gap degeneration

heterochiral II/III coupling coefficients tend to zero.

---

## Branch G — Robust heterochiral net production

$$
\boxed{
\text{positive critical helical production}
}
$$

synchronized.

---

## Branch H — Robust work cancellation

Helical negative cancellation forces comparable negative high-mode nonlinear work.

---

# 35. C4-D.8: Amplitude-to-Flux Barrier — Partial Closure

Thus, the status of C4-C's:

$$
\boxed{
\text{Amplitude-to-Flux Barrier}
}
$$

is now:

## Direct implication

$$
\boxed{
\text{amplitude crossing}
\Rightarrow
\text{positive flux}
}
$$

remains:

$$
\boxed{
\mathrm{FALSE}.
}
$$

## Branching implication

$$
\boxed{
\text{amplitude crossing}
\Rightarrow
\text{finite structured branch set}
}
$$

is now:

$$
\boxed{
\mathrm{PROVED}.
}
$$

This is the primary closure of this round.

---

# 36. Correction to C4-B pulse-capacity

C4-B stated that the integrated critical toll could be paid by a narrow high pulse.

C4-D now proves:

For a UV amplitude first crossing,

even if it takes the pulse route,

it cannot be described solely as a 'pulse'.

It must pay:

$$
\boxed{
\text{source impulse}
\vee
\text{critical nonlinear work}
\vee
\text{work cancellation}.
}
$$

Therefore:

$$
\boxed{
\textbf{UV pulse capacity has an N--S-specific structured payload}.
}
$$

---

# 37. But new carrier relay can still exist

Each generation:

$$
q_n\uparrow\infty
$$

can choose a different branch:

- Generation $n$ source overcapacity;
- Generation $n+1$ homochiral;
- The next generation rank defect;

etc.

So C4-D still does not yield a global contradiction.

But the branch set has become finite and typed,

therefore C4 can reuse:

$$
\boxed{
\text{finite recurrent branch reduction}.
}
$$

---

# 38. C4-D.9: Recurrent Escape-Branch Reduction

If infinite critical crossings exist,

and each time they fall into the finite branch family:

$$
\mathcal B
=
\{A,B,C,D,E,F,G,H\},
$$

then there exists:

$$
\boxed{
B_\ast\in\mathcal B
}
$$

that appears repeatedly in an infinite subsequence.

Thus, subsequent C4 does not need to handle all crossing escapes simultaneously.

It can attack one by one:

$$
\boxed{
\textbf{one recurrent amplitude-crossing escape mode}.
}
$$

---

# 39. Which branches already have old rigidity?

## A — Persistence

Returns to C4-A synchronization.

## B — Source overcapacity

Still lacks a critical source-capacity budget.

## C / H — Work cancellation

Can be merged to study total nonlinear-work variation / work-dipole geometry.

## D — Rank defect

Connects to C1/C3-G absolute-frequency ancestry and carrier relay.

## E — Homochiral

Connects to Biferale–Titi / heterochiral leakage.

## F — Radial degeneration

Connects to C3-C/D radial congestion.

## G — Positive helical production

Connects to C3-A/B critical pair-production divergence.

Therefore:

$$
\boxed{
\text{most of the C4-D branch family already has a C3 dependence graph}.
}
$$

---

# 40. Source-overcapacity scaling

Normalized source impulse:

$$
\boxed{
\mathfrak S_q
=
\frac1{
\nu\lambda
}
\int
\|N_q^\sigma\|_\infty dt.
}
$$

During a viscous crossing:

$$
|I|
\sim
(\nu\lambda^2)^{-1},
$$

a critical-size nonlinear source:

$$
\|N_q\|_\infty
\sim
\nu^2\lambda^3
$$

exactly yields:

$$
\mathfrak S_q
\sim1.
$$

So the source-overcapacity branch is scale-critical,

and cannot be directly ruled out by ordinary energy.

---

# 41. Work-cancellation scaling

Critical nonlinear shell work rate:

$$
W_q
\sim
\nu^3\lambda.
$$

over viscous time:

$$
(\nu\lambda^2)^{-1}
$$

integrated ordinary energy work:

$$
\sim
\nu^2\lambda^{-1}.
$$

After critical weighting:

$$
\lambda
$$

:

$$
\sim
\nu^2.
$$

So:

$$
\boxed{
\mathfrak C_q^{sp}\sim O(1)
}
$$

is likewise a scale-critical variation.

This again explains why a generic finite energy budget will not shut it down.

---

# 42. Homochiral branch caveat

The Biferale–Titi regularity theorem operates on:

$$
\boxed{
\text{the full evolution projected onto a single helicity-sign subspace}.
}
$$

C4-D Branch E only indicates:

$$
\boxed{
\text{selected positive high-mode gain is primarily borne by homochiral triads}.
}
$$

It does not mean the full N–S evolution is already helical-decimated.

So one cannot directly apply:

$$
\boxed{
\text{homochiral gain}
\Rightarrow
\text{regular}.
}
$$

What truly needs to be controlled is:

$$
\boxed{
\text{heterochiral leakage}.
}
$$

---

# 43. Rank-defect caveat

Non-top positive shell gain only proves:

$$
\boxed{
\text{still-higher absolute frequencies participate}.
}
$$

It does not prove:

$$
\boxed{
\text{those higher modes are already critical-active}.
}
$$

So the D branch must connect to:

- source amplitude;
- parent criticality;
- shell occupancy;

in order to form an ancestry contradiction.

---

# 44. Radial degeneration caveat

II/III coupling can escape due to:

$$
\frac{q-p}{q}\to0
$$

or:

$$
\frac{q-k}{q}\to0
$$

.

This branch is not phase cancellation,

but rather:

$$
\boxed{
\text{kinematic helical coupling coefficient itself collapse}.
}
$$

So it must be handled using C3-C/D radial congestion,

and cannot be handled by helical total variation.

---

# 45. X-Integration guards update

## G-HCROSS

Crossing is first split into persistence / fast.

## G-MAXSRC

Fast amplitude growth must preserve the maximizing-point nonlinear source projection.

## G-SEFF

Preserve:

$$
\eta
=
\frac{
-e\cdot N(x_{\max})
}{
\|N\|_\infty
}.
$$

## G-LWORK

Good efficiency generates a local positive-work ball.

## G-WCANCEL

If local positive work does not become net shell input,

the missing amount enters the spatial negative-work debt.

## G-RANK

Shell gain must preserve the receiving mode rank before entering the helical table.

## G-HCWORK

Robust helical cancellation must preserve the corresponding negative high-mode work.

## G-BRANCH

Amplitude-to-Flux only allows a branching bridge,

and must not be re-elevated to a direct implication.

---

# 46. True ETN update

Amplitude crossing state:

$$
\boxed{
\Theta_q^{cross}
=
\left\langle
\beta_0,\beta_1,
I_\lambda,
M',
N,
\eta,
L_{\rm local},
W_q,
W^-,
\operatorname{Rank},
\operatorname{HelClass},
\operatorname{RadialGap}
\right\rangle.
}
$$

transition:

$$
\boxed{
\text{Crossing}
\to
\text{Persistence}
\vee
\text{Source}
\vee
\text{WorkCancellation}
\vee
\text{RankDefect}
\vee
\text{Homochiral}
\vee
\text{RadialDegeneration}
\vee
\text{HelicalNet}
\vee
\text{RobustBackTransfer}.
}
$$

---

# 47. Strategic consequence

The core barrier of C4-C was originally:

$$
\boxed{
\text{amplitude is not flux}.
}
$$

C4-D does not negate this statement.

Instead, it proves:

$$
\boxed{
\text{an amplitude crossing is not an arbitrary non-flux event}.
}
$$

In the N–S shell evolution,

it either:

- is already persistent;
- has an excessive nonlinear source;
- generates critical local energy work;
- if the work is hidden, there must be cancellation;
- if the work is truly input into the UV shell, the helical structure further compresses it into a finite branch family.

Therefore, the hereditary amplitude ancestry is truly connected for the first time to:

$$
\boxed{
\text{energy-work / helical closure graph}.
}
$$

---

# 48. New frontier: C4-E

What is most worth doing now is not to attack the direct flux implication again.

The remaining finite branch family for an amplitude crossing is:

$$
\boxed{
\text{Source Overcapacity}
\vee
\text{Work Cancellation}
\vee
\text{Rank Defect}
\vee
\text{Homochiral}
\vee
\text{Radial Degeneration}
\vee
\text{Helical Net Production}.
}
$$

Thus, the official next topic is:

$$
\boxed{
\textbf{C4-E — Recurrent Escape-Branch Rigidity and UV Closure Graph}.
}
$$

---

# 49. C4-E proof obligations

## E1 — Recurrent source-overcapacity

If:

$$
\mathfrak S_{q_n}\gtrsim1
$$

infinitely often,

can it be converted into:

- critical operator debt;
- higher derivative toll;
- source active-volume packing?

## E2 — Recurrent work cancellation

If:

$$
\mathfrak C_{q_n}^{sp}\gtrsim1
$$

infinitely often,

study:

- work-sign active volume;
- work-dipole separation;
- total work variation;
- pressure / phase transport.

## E3 — Rank-defect chain

If shell crossings are repeatedly powered by still-higher modes,

prove whether it forms:

$$
\boxed{
\text{strictly faster absolute-frequency ancestry}
}
$$

or pre-existing UV congestion.

## E4 — Homochiral dominance

If positive work is repeatedly homochiral-dominated,

quantify the heterochiral leakage:

$$
\varepsilon_{het,n}.
$$

If the leakage tends to zero,

compare with helical-decimated regular dynamics;

if it does not tend to zero,

return to the heterochiral branch.

## E5 — Radial-gap degeneration

When repeatedly:

$$
\delta_n\to0
$$

,

connect to C3-C/D radial congestion,

and study the required triad multiplicity.

## E6 — Helical net production

If:

$$
\mathcal R_+
$$

repeatedly synchronizes with the crossing,

the UV / helical channels now achieve true shared-event synchronization.

Then, together with:

- strain;
- operator;

search for the next edge.

## E7 — Branch transition graph

Establish the possible / forbidden transitions for:

$$
B_i
\to
B_j
$$

.

## E8 — C4 UV closure audit

Determine whether the amplitude hereditary chain has been compressed into:

$$
\boxed{
\text{finite recurrent structural motifs}
}
$$

sufficient to enter a stronger compactness / contradiction stage.

---

# 50. Official status

$$
\boxed{
\begin{aligned}
\text{persistence-or-fast-crossing dichotomy}
&:\ \mathrm{PROVED},\\
\text{positive amplitude variation}\Rightarrow\text{positive nonlinear source at max}
&:\ \mathrm{PROVED},\\
\text{band-limited local positive-work ball}
&:\ \mathrm{PROVED},\\
\text{integrated critical local-work toll}
&:\ \mathrm{PROVED},\\
\text{source-overcapacity impulse branch}
&:\ \mathrm{PROVED},\\
\text{local-to-global work cancellation branch}
&:\ \mathrm{PROVED},\\
\text{Amplitude-to-Work branching bridge}
&:\ \mathrm{PROVED},\\
\text{direct amplitude}\Rightarrow\text{positive flux}
&:\ \mathrm{FALSE},\\
\text{positive shell work}\Rightarrow\text{positive triad variation}
&:\ \mathrm{PROVED},\\
\text{rank-defect branch}
&:\ \mathrm{DEFINED/EXACT\ PROVENANCE},\\
\text{robust heterochiral }\mathcal R=\kappa q\dot e_q
&:\ \mathrm{PROVED},\\
\text{helical cancellation}\Rightarrow\text{high-mode work cancellation}
&:\ \mathrm{PROVED},\\
\text{full amplitude crossing finite branch reduction}
&:\ \mathrm{PROVED},\\
\text{global regularity}
&:\ \mathrm{OPEN}.
\end{aligned}
}
$$

---

# 51. Conclusion

C4-C left behind the:

$$
\boxed{
\text{Amplitude-to-Flux Barrier}.
}
$$

C4-D now rewrites it into a truly N–S-specific theorem:

For a critical shell crossing:

$$
\beta_0
\to
\beta_1,
$$

there is first:

$$
\boxed{
\text{full viscous-window persistence}
\vee
\text{fast crossing}.
}
$$

In a fast crossing,

the viscosity at the maximum point cannot positively increase the amplitude,

therefore the positive amplitude variation must be provided by the nonlinear source:

$$
\boxed{
-e\cdot N
\ge
M'.
}
$$

The band-limit then expands the pointwise source into a shell-scale local positive-work ball.

Thus, the entire crossing must pay:

$$
\boxed{
\text{source overcapacity}
\vee
\text{positive nonlinear shell work}
\vee
\text{spatial work cancellation}.
}
$$

This is the:

$$
\boxed{
\textbf{Amplitude-to-Work Branching Bridge}.
}
$$

If it enters the positive shell-work branch,

it further undergoes triad rank / helical class decomposition:

$$
\boxed{
\text{rank defect}
\vee
\text{homochiral}
\vee
\text{radial degeneration}
\vee
\text{robust heterochiral}.
}
$$

And in the robust heterochiral case:

$$
\boxed{
\mathcal R_\tau
=
\kappa_\tau
q_\tau\dot e_{q_\tau},
\qquad
c_\ast\le\kappa_\tau\le1.
}
$$

So if helical cancellation occurs,

it must synchronously generate comparable negative highest-mode work:

$$
\boxed{
\text{helical cancellation}
\Rightarrow
\text{high-mode back-transfer}.
}
$$

Therefore, 'positive and negative helicity cancelling each other out' is no longer a completely independent hidden channel.

C4 now for the first time truly connects the:

$$
\boxed{
\text{hereditary UV amplitude crossing}
}
$$

to the:

$$
\boxed{
\text{energy-work / helical shared-event closure graph}.
}
$$

Next round:

$$
\boxed{
\textbf{C4-E — Recurrent Escape-Branch Rigidity and UV Closure Graph}.
}
$$

---

# References

1. F. Waleffe, *The nature of triad interactions in homogeneous turbulence*, Physics of Fluids A 4 (1992), 350–363, DOI: 10.1063/1.858309.
2. A. Cheskidov, M. Dai, *Regularity criteria for the 3D Navier–Stokes and MHD equations*, arXiv:1507.06611.
3. A. Cheskidov, R. Shvydkoy, *On the regularity of weak solutions of the 3D Navier–Stokes equations in \(B^{-1}_{\infty,\infty}\)*, arXiv:0708.3067.
4. Z. Lei, F.-H. Lin, Y. Zhou, *Structure of Helicity and Global Solutions of Incompressible Navier–Stokes Equation*, arXiv:1505.00142.
5. L. Biferale, E. S. Titi, *On the Global Regularity of a Helical-decimated Version of the 3D Navier–Stokes Equations*, arXiv:1303.1215.

# Internal dependencies

- `NS_C4C_SharedEventCoupling_AmplitudeFluxBarrier_v0.1.md`
- `NS_C4B_TemporalSynchronization_CarrierRelayNoGo_v0.1.md`
- `NS_C4A_UnifiedSurvivorState_SynchronizationClosure_v0.1.md`
- `NS_C3G_FirstCrossing_CausalAncestry_DepletionNoGo_v0.1.md`
- `NS_C3E_ViscousWindow_PhaseEfficiency_Zeno_v0.1.md`
- `NS_C3D_CutoffFlux_HelicalKernel_Nonlocality_v0.1.md`
- `NS_C3C_ClassII_Nonlocality_Tax_Radial_Congestion_v0.1.md`
- `NS_C3B_BiHelical_Equalization_UniqueSign_UV_Escape_v0.1.md`
- `NS_C3K_AbsoluteOccupancy_OneMomentGap_v0.1.md`
- `True ETN / Infinite-dimensional tension field`
- `X_Integral_Unified_Program_v0.2.md`

Next:

$$
\boxed{
\textbf{C4-E — Recurrent Escape-Branch Rigidity and UV Closure Graph}
}
$$