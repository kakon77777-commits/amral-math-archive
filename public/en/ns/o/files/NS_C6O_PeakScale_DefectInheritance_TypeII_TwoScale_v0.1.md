---
title: "Navier–Stokes C6-O: Peak-Scale Defect Inheritance, Type-II Ancient Carriers, and Mass–Peak Two-Scale Closure"
subtitle: "Type-II Dominant Carriers Split Mass and Peak Scales; Global Relative Critical Mass Escapes Every Bounded Peak Region, while Local Defect Metadata Can Inherit Only Through Peak-Tight Absolute Carriers; Remote Mass Tails Decouple from Peak Pressure Hessian"
version: "v0.1"
date: "2026-08-16"
author: "Neo.K / EveMissLab"
language: "en"
status: "C6 Type-II mass/peak closure / ancient defect inheritance / derivative-tower and pressure-tail audit"
epistemic_status: "Exact scaling, tightness, derivative-scale, pressure-tail and carrier-inheritance identities + conditional ancient-limit inheritance + external Type-II/ancient-profile interfaces. Does NOT classify all bounded ancient solutions and does NOT prove Navier–Stokes global regularity."
---

# Navier–Stokes C6-O
# Peak-Scale Defect Inheritance, Type-II Ancient Carriers, and Mass–Peak Two-Scale Closure

## 0. Current Positioning

C6-N reclassifies the singular carrier into:

$$
\boxed{
\text{Type-I Absolute Carrier}
}
$$

or:

$$
\boxed{
\text{Type-II Relative-Dominant Carrier}
}
$$

or:

$$
\boxed{
\text{Carrier/Peak Label Escape}.
}
$$

where the Type-II relative-dominant carrier:

$$
C_n
=
B_{\ell_n}(x_n^C)
$$

satisfies:

$$
\int_{C_n}|u(x,t_n)|^3dx
\ge
\beta_\ast
\|u(t_n)\|_3^3,
$$

and is proven by C6-N to satisfy:

$$
\boxed{
\ell_n
A_n^C
\to\infty.
}
$$

Therefore, the peak-amplitude scale:

$$
\boxed{
a_n
=
(A_n^C)^{-1}
}
$$

satisfies:

$$
\boxed{
a_n/\ell_n\to0.
}
$$

That is:

$$
\boxed{
\textbf{mass scale}
\gg
\textbf{peak scale}.
}
$$

Performing exact N–S rescaling at the record peak scale:

$$
v_n(z,\tau)
=
A_n^{-1}
u
\left(
x_n+\frac z{A_n},
t_n+\frac{\tau}{A_n^2}
\right),
$$

extracts a:

$$
\boxed{
\textbf{nontrivial bounded ancient N--S profile}.
}
$$

However, C6-N simultaneously proves:

$$
\boxed{
\textbf{bounded ancient peak profile is a global }L^3
\textbf{ relative spectator}.
}
$$

Because:

$$
\|v_n\|_\infty\le1,
$$

and:

$$
\|v_n(0)\|_3
=
\|u(t_n)\|_3
\to\infty.
$$

Thus, a fixed:

$$
B_R
$$

only carries a vanishing global relative:

$$
L^3
$$

fraction.

C6-O formally asks:

> **If the global critical mass entirely escapes to the spatial infinity of the ancient peak frame, can the TS / GP / HF defect labels still remain in the bounded peak core?**

In other words:

$$
\boxed{
\textbf{critical mass inheritance}
\neq
\textbf{defect inheritance}.
}
$$

Main results of this stage:

1. Define the mass/peak scale ratio:
   $$
   \mathfrak R_n^{MP}
   =
   A_n\ell_n;
   $$
2. Type-II relative dominance yields:
   $$
   \mathfrak R_n^{MP}\to\infty;
   $$
3. The global normalized:
   $$
   L^3
   $$
   mass probability tends to zero for every fixed ball in the peak frame;
4. Therefore:
   $$
   \boxed{
   \textbf{relative singular-mass probability is never peak-tight};
   }
   $$
5. Define the independent peak defect tightness:
   $$
   \Theta_D^{peak};
   $$
6. The defect label can be:
   - peak-tight;
   - partial;
   - peak-escaped;
7. If the defect label is peak-tight,
   it must asymptotically decouple from the global relative:
   $$
   L^3
   $$
   probability;
8. Therefore, ancient defect inheritance must utilize:
   $$
   \boxed{
   \textbf{local absolute defect load};
   }
   $$
9. Establish the general Local Absolute Defect Inheritance Lemma;
10. Dimensionless local margins can be passed to the ancient profile under strong local convergence;
11. Global-normalized carrier probabilities do not necessarily transfer;
12. Define the derivative-to-peak ratio:
    $$
    \widehat A_{k,n}^{peak}
    =
    A_{k,n}/A_{0,n}^{k+1};
    $$
13. Yielding:
    - flattening;
    - peak-scale derivative;
    - subpeak derivative escape;
14. If:
    $$
    \widehat A_{k,n}^{peak}\to\infty,
    $$
    the derivative scale:
    $$
    b_{k,n}=A_{k,n}^{-1/(k+1)}
    $$
    satisfies:
    $$
    b_{k,n}/a_n\to0;
    $$
15. Thus, high-order HF can re-trigger:
    $$
    \boxed{
    \textbf{Derivative-Tower Restart};
    }
    $$
16. If:
    $$
    \widehat A_{k,n}^{peak}\to0,
    $$
    the ancient peak's:
    $$
    D^k v_\infty
    $$
    vanishes;
17. For:
    $$
    k=1,
    $$
    the peak ancient profile becomes flat/constant in spatial variables;
18. HF global-threshold labels can only be legally inherited when the derivative amplitude is captured by the peak frame;
19. TS requires an additional:
    $$
    \boxed{
    \textbf{Peak Time-Window Gate};
    }
    $$
20. GP local geometry can be inherited under:
    $$
    C^2_{\rm loc}
    $$
    convergence + nondegenerate Q mass/margins;
21. Far-pressure provenance must be repartitioned;
22. Record peak frame:
    $$
    \|v_n(\tau)\|_\infty\le1;
    $$
23. The contribution of the remote pressure-Hessian source:
    $$
    |y|>R
    $$
    to a fixed peak core is:
    $$
    \boxed{
    O(R^{-2});
    }
    $$
24. Therefore, although the mass-scale tail carries almost all of the global relative:
    $$
    L^3
    $$
    mass, it cannot maintain an:
    $$
    O(1)
    $$
    far-pressure Hessian influence on a fixed peak core;
25. This is the:
    $$
    \boxed{
    \textbf{Mass-Tail / Peak-Pressure Decoupling};
    }
    $$
26. Type-II ancient peak pressure provenance thus becomes a peak-local finite-radius problem;
27. The recent 2026 Seregin Type-II work provides another conditional external interface:
    certain Type-II scenarios can generate an ancient Euler limit via Euler scaling and utilize Euler Liouville analysis;
28. C6-O does not apply this scenario theorem as a universal N–S Type-II kill;
29. The current Type-II carrier is ultimately partitioned into:
    $$
    \boxed{
    \text{Peak-Inherited Ancient Defect}
    \vee
    \text{Mass-Scale Defect / Peak Escape}
    \vee
    \text{Subpeak Derivative Restart}.
    }
    $$
30. Only if the ancient peak profile inherits the defect label can it legally connect to:
    - ancient Liouville;
    - Type-I decay;
    - ancient GP/HF/TS rigidity;
31. If the label peak-escapes,
    the ancient profile and the C6 defect cycle must be viewed as two distinct carriers.

---

# 1. Fresh primary-source audit

## 1.1 Singular zoom-in and bounded ancient profiles

Albritton–Barker prove that under suitable weak-solution hypotheses an interior/boundary singularity generates a nontrivial mild bounded ancient Navier–Stokes solution by zooming in.

They also prove local:

$$
L^3
$$

divergence in every fixed ball around a singular point.

Thus the two facts coexist:

- local absolute critical mass grows;
- peak-normalized ancient fields can be bounded.

This already signals a multi-scale concentration structure.

## 1.2 Ancient Type-I gate

Albritton–Barker prove a correspondence between local Type-I singularity and nontrivial mild bounded ancient solutions satisfying an appropriate Type-I decay condition,

and a Liouville theorem for ancient solutions bounded in:

$$
L^3
$$

along a backward sequence.

These are conditional ancient rigidity gates.

## 1.3 General bounded ancient problem

Koch–Nadirashvili–Seregin–Šverák study mild bounded ancient N–S solutions.

The general three-dimensional bounded-ancient Liouville problem is not solved in full.

Therefore ancient extraction is not itself a contradiction.

## 1.4 Profile decomposition

Gallagher–Koch–Planchon show that bounded critical sequences admit scale/core profile decomposition and nonlinear profile evolution.

This remains relevant only after a bounded **physical** critical chunk is legally identified.

## 1.5 Pressure local expansion

Bradshaw–Tsai give a rigorous whole-space local pressure expansion.

This lets C6 preserve the distinction between:

- local pressure;
- far pressure;
- pressure provenance.

In the peak frame the far-source partition must be recomputed.

## 1.6 Recent Type-II analysis

Seregin's 2026 note studies particular local Type-II blow-up scenarios using zooms based on Euler scaling and Liouville-type theorems for Euler limit equations.

In one of the paper's scenario theorems, a rescaled limit solves the Euler equations in an ancient space-time domain.

C6-O uses this only as a **conditional external Type-II interface**.

---

# 2. Type-II mass/peak scales

Let:

$$
t_n\uparrow T^\ast.
$$

Let:

$$
\ell_n
$$

be a critical-mass carrier scale.

Let:

$$
A_n
=
\|u(t_n)\|_\infty
$$

be the chosen record peak amplitude,

and:

$$
\boxed{
a_n
=
A_n^{-1}
}
$$

the peak scale.

Define:

$$
\boxed{
\mathfrak R_n^{MP}
=
\frac{
\ell_n
}{
a_n
}
=
A_n\ell_n.
}
$$

For a relative-dominant Type-II carrier:

$$
\boxed{
\mathfrak R_n^{MP}\to\infty.
}
$$

---

# 3. Peak-amplitude rescaling

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

Define:

$$
\boxed{
v_n(z,\tau)
=
A_n^{-1}
u
\left(
x_n+a_nz,
t_n+a_n^2\tau
\right).
}
$$

Since:

$$
a_n=A_n^{-1},
$$

this is exact N–S scaling.

Pressure:

$$
\boxed{
q_n(z,\tau)
=
A_n^{-2}
p
\left(
x_n+a_nz,
t_n+a_n^2\tau
\right).
}
$$

---

# 4. Record-time bound

Take:

$$
t_n
$$

as amplitude record times:

$$
A_n
=
\max_{s\le t_n}
\|u(s)\|_\infty.
$$

Then:

$$
\boxed{
\|v_n(\tau)\|_\infty
\le1
\qquad
\tau\le0.
}
$$

And:

$$
\boxed{
|v_n(0,0)|=1.
}
$$

After local parabolic compactness:

$$
v_n
\to
v_\infty
$$

locally along a subsequence,

with:

$$
\boxed{
v_\infty
}
$$

a nontrivial bounded ancient N–S solution.

---

# 5. Mass scale in peak variables

A physical ball:

$$
B_{\ell_n}(x_n)
$$

becomes:

$$
\boxed{
B_{\mathfrak R_n^{MP}}(0)
}
$$

in peak variables.

Since:

$$
\mathfrak R_n^{MP}\to\infty,
$$

the mass carrier expands to spatial infinity in the bounded ancient peak frame.

---

# 6. Peak-frame global critical-mass probability

At:

$$
\tau=0,
$$

define:

$$
\boxed{
d\mu_{3,n}^{peak}(z)
=
\frac{
|v_n(z,0)|^3
}{
\|v_n(0)\|_3^3
}dz.
}
$$

N–S critical scaling gives:

$$
\boxed{
\|v_n(0)\|_3
=
\|u(t_n)\|_3
\to\infty.
}
$$

---

# 7. C6-O.1: Peak Relative-Mass Escape Theorem

For any fixed:

$$
R<\infty,
$$

record normalization gives:

$$
|v_n(z,0)|
\le1.
$$

Therefore:

$$
\int_{B_R}
|v_n|^3dz
\le
|B_R|
=
c_3R^3.
$$

Hence:

$$
\boxed{
\mu_{3,n}^{peak}(B_R)
\le
\frac{
c_3R^3
}{
\|v_n(0)\|_3^3
}
\to0.
}
$$

### Conclusion

$$
\boxed{
\textbf{global relative }L^3\textbf{ singular mass escapes every bounded peak-frame region}.
}
$$

---

# 8. Peak relative mass is not tight

Define tightness coefficient:

$$
\boxed{
\Theta_3^{peak}
=
\lim_{R\to\infty}
\liminf_n
\mu_{3,n}^{peak}(B_R).
}
$$

By C6-O.1:

for every finite:

$$
R,
$$

the inner:

$$
\liminf
$$

is:

$$
0.
$$

Thus:

$$
\boxed{
\Theta_3^{peak}=0.
}
$$

So the global relative:

$$
L^3
$$

carrier is fully non-tight in the ancient peak frame.

---

# 9. Peak defect-carrier measure

Let:

$$
\eta_n^D
$$

be a defect carrier probability at:

$$
t_n.
$$

Push it into peak variables:

$$
\boxed{
\eta_{n}^{D,peak}
=
(T_n^{peak})^{-1}_\#
\eta_n^D,
}
$$

where:

$$
T_n^{peak}(z)
=
x_n+a_nz.
$$

---

# 10. Defect peak tightness

Define:

$$
\boxed{
\Theta_D^{peak}
=
\lim_{R\to\infty}
\liminf_n
\eta_n^{D,peak}(B_R).
}
$$

Possible regimes:

## O-DT

$$
\boxed{
\Theta_D^{peak}=1.
}
$$

Peak-tight defect carrier.

## O-DP

$$
\boxed{
0<\Theta_D^{peak}<1.
}
$$

Partial peak inheritance + partial escape.

## O-DE

$$
\boxed{
\Theta_D^{peak}=0.
}
$$

Peak-label escape.

---

# 11. Relative mass vs peak-tight defect

Suppose:

$$
\Theta_D^{peak}=1.
$$

Given:

$$
\varepsilon>0,
$$

choose:

$$
R
$$

such that:

$$
\liminf_n
\eta_n^{D,peak}(B_R)
\ge
1-\varepsilon.
$$

But:

$$
\mu_{3,n}^{peak}(B_R)\to0.
$$

The common mass satisfies:

$$
|
\mu_{3,n}^{peak}\wedge
\eta_n^{D,peak}
|
\le
\mu_{3,n}^{peak}(B_R)
+
\eta_n^{D,peak}(B_R^c).
$$

Therefore:

$$
\limsup_n
|
\mu_{3,n}^{peak}\wedge
\eta_n^{D,peak}
|
\le
\varepsilon.
$$

Let:

$$
\varepsilon\downarrow0.
$$

---

# 12. C6-O.2: Peak-Tight Defect / Relative-Mass Decoupling

$$
\boxed{
\Theta_D^{peak}=1
\Rightarrow
1-d_{TV}
(
\mu_{3,n}^{peak},
\eta_n^{D,peak}
)
\to0.
}
$$

### Interpretation

A defect label which genuinely stays localized in the bounded ancient peak core is necessarily a **global relative $L^3$ spectator** in that frame.

Therefore:

$$
\boxed{
\textbf{relative singular-mass overlap cannot be the inheritance criterion for ancient peak defects}.
}
$$

---

# 13. Ancient inheritance must be absolute/local

C6-N already corrected:

$$
\boxed{
\text{Absolute Critical Carrier}
\neq
\text{Relative Dominant Carrier}.
}
$$

C6-O now sharpens:

the bounded ancient peak profile can only inherit a defect through:

$$
\boxed{
\textbf{local absolute defect loads and local dimensionless geometry},
}
$$

not through fixed global:

$$
L^3
$$

fractions.

---

# 14. Local defect density

Let:

$$
\mathcal A_D[v]
\ge0
$$

be a local or localized defect density depending continuously on:

$$
v,
\nabla v,\ldots,D^mv
$$

on a compact region.

Examples:

- middle source:
  $$
  \lambda_2^+|S|^2;
  $$
- Q-weighted GP geometry:
  $$
  \chi|Q|;
  $$
- selected derivative local energy/volume;
- locally represented source terms.

Fix:

$$
K
\Subset
\mathbb R^3\times(-\infty,0].
$$

Define:

$$
\boxed{
M_{D,n}(K)
=
\int_K
\mathcal A_D[v_n].
}
$$

---

# 15. C6-O.3: Local Absolute Defect Inheritance Lemma

Assume:

1.:
   $$
   v_n\to v_\infty
   $$
   in:
   $$
   C^m(K);
   $$
2.:
   $$
   \mathcal A_D[v_n]
   \to
   \mathcal A_D[v_\infty]
   $$
   in:
   $$
   L^1(K);
   $$
3.:
   $$
   M_{D,n}(K)
   \ge
   m_0>0.
   $$

Then:

$$
\boxed{
\int_K
\mathcal A_D[v_\infty]
\ge
m_0.
}
$$

If:

$$
\eta_{D,n}^{K}
=
\frac{
\mathcal A_D[v_n]
}{
M_{D,n}(K)
}
$$

and:

$$
M_{D,n}(K)\to M_{D,\infty}>0,
$$

then:

$$
\boxed{
\eta_{D,n}^{K}
\to
\eta_{D,\infty}^{K}
}
$$

in total variation.

### Meaning

A nonvanishing local absolute defect load passes to the bounded ancient limit under sufficient local strong convergence.

---

# 16. Strict-margin inheritance

Suppose a dimensionless defect condition is written:

$$
\boxed{
F[v_n]\ge\delta+\varepsilon
}
$$

on the relevant local carrier,

with:

$$
\varepsilon>0
$$

fixed.

If:

$$
F[v_n]\to F[v_\infty]
$$

uniformly on the carrier,

then:

$$
\boxed{
F[v_\infty]\ge\delta+\varepsilon/2
}
$$

for large:

$$
n
$$

and in the limit.

Thus strict:

- middle-gap margins;
- cone margins;
- pressure signature gaps;
- sign-threshold margins;

are stable under strong local convergence.

Critical boundary cases with zero margin require separate compactification.

---

# 17. Peak derivative scaling

Let:

$$
\boxed{
A_{k,n}
=
\max_{|\zeta|=k,i}
\|
D^\zeta u_i(t_n)
\|_\infty.
}
$$

Under peak scaling:

$$
v_n
=
A_{0,n}^{-1}
u(
x_n+A_{0,n}^{-1}z
),
$$

$$
D^kv_n
=
A_{0,n}^{-(k+1)}
D^ku.
$$

Therefore:

# 18. Peak-normalized derivative amplitude

$$
\boxed{
\widehat A_{k,n}^{peak}
=
\frac{
A_{k,n}
}{
A_{0,n}^{k+1}
}
=
\|D^kv_n(0)\|_\infty.
}
$$

This is dimensionless.

---

# 19. C6-O.4: Derivative-to-Peak Trichotomy

After subsequence:

## O-K0 — Flattening

$$
\boxed{
\widehat A_{k,n}^{peak}\to0.
}
$$

## O-K1 — Peak-scale derivative

$$
\boxed{
\widehat A_{k,n}^{peak}
\to
a_k
\in(0,\infty).
}
$$

## O-K∞ — Subpeak derivative escape

$$
\boxed{
\widehat A_{k,n}^{peak}\to\infty.
}
$$

---

# 20. Flattening branch

If:

$$
\widehat A_{k,n}^{peak}\to0,
$$

then:

$$
\boxed{
D^kv_n
\to0
}
$$

uniformly globally at:

$$
\tau=0
$$

and locally in the ancient limit whenever the convergence propagates.

Thus:

$$
\boxed{
D^kv_\infty(\cdot,0)=0.
}
$$

For:

$$
k=1,
$$

$$
\boxed{
\nabla v_\infty(\cdot,0)=0,
}
$$

so:

$$
v_\infty(\cdot,0)
$$

is spatially constant.

If the same derivative vanishing persists in time under the limiting dynamics,

the ancient profile is spatially constant.

### Guard

C6-O does not infer temporal constancy solely from one time slice.

---

# 21. GP/TS consequence of $k=1$ flattening

GP and TS geometry depend on:

- strain;
- vorticity;
- middle eigenvalue;
- Q/source densities.

If:

$$
\boxed{
\widehat A_{1,n}^{peak}\to0,
}
$$

then on bounded peak regions at:

$$
\tau=0,
$$

$$
S[v_n],
\omega[v_n]
\to0.
$$

Therefore derivative-based:

$$
TS/GP
$$

local absolute loads vanish in the peak limit at that time.

Thus:

$$
\boxed{
\textbf{$k=1$ flattening is a peak-label escape mechanism for derivative-based TS/GP states}.
}
$$

---

# 22. Subpeak derivative scale

Define:

$$
\boxed{
b_{k,n}
=
A_{k,n}^{-1/(k+1)}.
}
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
\frac{
A_{k,n}
}{
A_{0,n}^{k+1}
}
\right)^{-1/(k+1)}
=
\left(
\widehat A_{k,n}^{peak}
\right)^{-1/(k+1)}.
$$

Therefore:

# 23. C6-O.5: Derivative-Tower Restart Theorem

If:

$$
\boxed{
\widehat A_{k,n}^{peak}\to\infty,
}
$$

then:

$$
\boxed{
b_{k,n}/a_n\to0.
}
$$

Thus the global:

$$
k
$$

-th derivative defect lives on a scale strictly below the peak-amplitude scale.

This is:

$$
\boxed{
\textbf{Derivative-Tower Restart}.
}
$$

### Main consequence

A global-threshold HF state cannot automatically inherit to a bounded ancient peak profile if its normalizing derivative maximum escapes to a subpeak scale.

---

# 24. Global HF threshold in peak variables

A selected high set:

$$
E_{k,n}^{HF}
=
\{
\sigma D^ku_i
>
\lambda A_{k,n}
\}
$$

becomes:

$$
\boxed{
\widehat E_{k,n}^{HF}
=
\{
\sigma D^kv_{n,i}
>
\lambda
\widehat A_{k,n}^{peak}
\}.
}
$$

If:

$$
\widehat A_{k,n}^{peak}\to\infty
$$

while:

$$
v_n\to v_\infty
$$

in:

$$
C^k_{\rm loc},
$$

then for every fixed compact:

$$
K,
$$

$$
\boxed{
\widehat E_{k,n}^{HF}
\cap K
=
\varnothing
}
$$

eventually.

So the global HF carrier leaves every bounded peak region.

---

# 25. C6-O.6: HF Peak-Inheritance Gate

A global-threshold HF label can survive in the bounded ancient peak frame only if:

1.:
   $$
   \widehat A_{k,n}^{peak}
   $$
   does not diverge;
2. the selected component/sign carrier remains peak-tight;
3. strict sign-threshold margin survives;
4. theorem-time/window metadata have a nondegenerate peak-time representation.

Otherwise the HF label is:

$$
\boxed{
\textbf{peak-escaped}
}
$$

or triggers:

$$
\boxed{
\textbf{Derivative-Tower Restart}.
}
$$

---

# 26. HF peak/local amplitude capture

Define local peak-frame:

$$
k
$$

-th derivative amplitude:

$$
\boxed{
A_{k,n}^{loc}(R)
=
\|
D^kv_n(0)
\|_{L^\infty(B_R)}.
}
$$

Define:

$$
\boxed{
\Gamma_{k,n}^{loc}
=
\frac{
A_{k,n}^{loc}(R)
}{
\widehat A_{k,n}^{peak}
}
\in[0,1].
}
$$

If:

$$
\Gamma_{k,n}^{loc}\to0,
$$

the global derivative peak is spectator to the bounded ancient peak core.

If:

$$
\Gamma_{k,n}^{loc}\ge\gamma_k>0,
$$

the global HF normalization is partially captured locally.

---

# 27. TS source scaling at the peak

Strain scales:

$$
S[v_n]
=
A_n^{-2}
S[u].
$$

Thus:

$$
\lambda_2^+[S[v_n]]
|S[v_n]|^2
=
A_n^{-6}
\lambda_2^+[S[u]]
|S[u]|^2.
$$

At fixed time:

$$
dz
=
A_n^3dx.
$$

Therefore local middle source mass scales:

$$
\boxed{
m_M^{peak}
=
A_n^{-3}
m_M^{phys}.
}
$$

This is exactly the criticalized same-time middle load at peak scale:

$$
r=a_n.
$$

---

# 28. GP Q scaling at the peak

Quadratic tensor:

$$
Q
$$

has pointwise N–S degree:

$$
4.
$$

Hence:

$$
\boxed{
Q[v_n]
=
A_n^{-4}
Q[u].
}
$$

At fixed time:

$$
\boxed{
\int
|Q[v_n]|dz
=
A_n^{-1}
\int
|Q[u]|dx.
}
$$

Thus a peak-local GP carrier requires a nonvanishing **peak-critical Q load**:

$$
\boxed{
A_n^{-1}
A_{\chi_n}^{Q}
}
$$

on the corresponding peak core.

---

# 29. Peak time-window ratio

Let a TS/HF event have physical duration:

$$
\Delta t_n.
$$

Peak scaling uses:

$$
a_n^2=A_n^{-2}.
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

This is the event duration in peak ancient time:

$$
\tau.
$$

---

# 30. C6-O.7: Peak Time-Window Trichotomy

After subsequence:

## O-T0

$$
\boxed{
\Theta_{t,n}^{peak}\to0.
}
$$

The event collapses to an instantaneous slice in the ancient frame.

## O-T1

$$
\boxed{
\Theta_{t,n}^{peak}
\to
\Theta_\ast
\in(0,\infty).
}
$$

The event lives on a finite nondegenerate ancient-time interval.

## O-T∞

$$
\boxed{
\Theta_{t,n}^{peak}\to\infty.
}
$$

The event spans an unbounded ancient-time interval.

### Consequence

A TS/HF **dynamic** label can be inherited as one finite ancient event only in O-T1,

or after selecting/recentering a legal finite subwindow in O-T∞.

O-T0 retains only instantaneous geometry unless stronger time regularity supplies a limit.

---

# 31. TS Peak-Window Gate

To inherit a TS shared-source state to:

$$
v_\infty,
$$

one needs:

1. a peak-visible spatial source carrier;
2. nonvanishing peak-critical middle/operator absolute loads;
3.:
   $$
   \Theta_{t,n}^{peak}
   $$
   not collapsing uncontrollably;
4. strong enough local spacetime convergence of the source densities;
5. overlap:
   $$
   \Omega_{ST}
   $$
   preserved on the selected peak cylinder.

This is:

$$
\boxed{
\textbf{TS Peak-Window Gate}.
}
$$

No global TS label transfers merely from the existence of an ancient peak profile.

---

# 32. GP local geometry inheritance

Suppose on a fixed peak ball:

$$
B_R
$$

we have:

$$
v_n(\cdot,0)
\to
v_\infty(\cdot,0)
$$

in:

$$
C^2.
$$

Then:

- strain;
- vorticity;
- Q;
- eigenvalues;
- strain directions away from zero;
- middle-gap ratios away from degeneracy;

converge locally.

If:

$$
\boxed{
\int_{B_R}
|Q[v_n]|dz
\ge
q_0>0,
}
$$

and the GP cone/gap conditions have strict margins,

then the local GP geometry passes to:

$$
v_\infty.
$$

---

# 33. GP pressure needs a tail audit

Pressure Hessian:

$$
\nabla^2q_n
$$

is nonlocal.

Even if:

$$
v_n\to v_\infty
$$

strongly locally,

remote mass can in principle influence the local pressure.

But record normalization gives a strong tail bound.

---

# 34. Pressure Hessian kernel

For whole-space N–S:

$$
p
=
K_{ij}*(u_iu_j)
$$

modulo the standard pressure normalization,

where:

$$
K_{ij}(z)
\sim
|z|^{-3}.
$$

Away from:

$$
z=0,
$$

$$
\boxed{
|\nabla^2K_{ij}(z)|
\le
C|z|^{-5}.
}
$$

---

# 35. Peak pressure tail

Fix:

$$
R_0<\infty.
$$

For:

$$
R>2R_0,
$$

define pressure Hessian contribution from:

$$
|y|>R.
$$

For:

$$
x\in B_{R_0},
$$

$$
|x-y|
\ge
|y|-R_0
\ge
|y|/2.
$$

Record peak bound:

$$
|v_n(y,\tau)|\le1
\qquad
\tau\le0.
$$

Thus:

$$
\begin{aligned}
|
\nabla^2 q_{n,>R}(x,\tau)
|
&\le
C
\int_{|y|>R}
|x-y|^{-5}
|v_n(y,\tau)|^2dy
\\
&\le
C
\int_R^\infty
r^{-5}r^2dr.
\end{aligned}
$$

Therefore:

# 36. C6-O.8: Mass-Tail / Peak-Pressure Decoupling Theorem

$$
\boxed{
\sup_{
n,\tau\le0,x\in B_{R_0}
}
|
\nabla^2q_{n,>R}(x,\tau)
|
\le
C_{R_0}
R^{-2}.
}
$$

Hence:

$$
\boxed{
\lim_{R\to\infty}
\sup_{
n,\tau\le0,x\in B_{R_0}
}
|
\nabla^2q_{n,>R}
|
=
0.
}
$$

### Main meaning

The spatial tail which carries almost all of the global relative:

$$
L^3
$$

mass in the ancient peak frame cannot maintain an:

$$
O(1)
$$

pressure-Hessian influence on a fixed peak core.

---

# 37. Pressure mass vs pressure influence

C6-O.1 says:

$$
\boxed{
\text{relative }L^3\text{ mass}
}
$$

moves to:

$$
|z|\to\infty.
$$

C6-O.8 says:

$$
\boxed{
\text{pressure-Hessian influence from that remote tail}
\to0
}
$$

on fixed peak cores.

Thus:

$$
\boxed{
\textbf{global critical-mass dominance}
\neq
\textbf{local GP pressure dominance}.
}
$$

This is a major mass–peak two-scale closure.

---

# 38. Peak pressure provenance repartition

Because remote mass-scale sources:

$$
|z|\sim\mathfrak R_n^{MP}\to\infty
$$

decouple at Hessian level,

the pressure source relevant to a peak-scale GP state must come from:

- local peak core;
- finite peak-radius far source;
- finite-range pressure structure;

not the asymptotically remote mass tail.

Therefore:

$$
\boxed{
\textbf{primary mass-scale pressure provenance cannot be copied into the peak frame}.
}
$$

It must be recomputed.

---

# 39. Local pressure convergence consequence

Suppose:

$$
v_n
\to
v_\infty
$$

strongly on every fixed:

$$
B_R\times[-T,0].
$$

Split pressure Hessian into:

- sources inside:
  $$
  B_R;
  $$
- sources outside:
  $$
  B_R.
  $$

The inside term passes by local convergence/principal-value pressure theory under the corresponding regularity,

while the outside Hessian tail is uniformly:

$$
O(R^{-2}).
$$

Thus, under the standard pressure normalization:

$$
\boxed{
\nabla^2q_n
\to
\nabla^2q_\infty
}
$$

locally after:

1. first taking:
   $$
   n\to\infty;
   $$
2. then:
   $$
   R\to\infty.
   $$

### Status

Conditional on the stated local convergence/pressure representation.

---

# 40. C6-O.9: Conditional Ancient GP Inheritance Theorem

Assume:

1.:
   $$
   v_n\to v_\infty
   $$
   strongly enough locally for:
   $$
   S,\omega,Q,\nabla^2q;
   $$
2. a fixed peak core carries:
   $$
   \int|Q[v_n]|
   \ge q_0>0;
   $$
3. middle-gap / strain-direction / pressure-signature margins stay strictly nondegenerate;
4. pressure provenance is repartitioned relative to the peak core.

Then:

$$
\boxed{
\text{local GP metadata pass to }
v_\infty.
}
$$

### Guard

Cross-generation:

- heredity;
- old common-far identity;
- old core graph;

do not pass automatically.

---

# 41. Ancient GP node

Define:

$$
\boxed{
GP^{anc}
}
$$

as a bounded ancient solution carrying on some finite cylinder:

- nonzero absolute Q load;
- nondegenerate strong-middle geometry;
- local pressure-Hessian response;
- legally defined local/far pressure provenance.

This is a local ancient joint state,

not automatically a recurrent GP cycle.

---

# 42. Ancient HF node

Define:

$$
\boxed{
HF^{anc}_k
}
$$

when the bounded ancient profile carries:

- finite peak-normalized:
  $$
  k
  $$
  -derivative amplitude;
- selected component/sign geometry;
- nondegenerate spatial bad/good set;
- a legal finite ancient-time window.

Global Grujić–Xu theorem status must be re-evaluated for the ancient solution.

---

# 43. Ancient TS node

Define:

$$
\boxed{
TS^{anc}
}
$$

when the bounded ancient profile carries on a finite cylinder:

- nonzero absolute middle load;
- nonzero operator/source load;
- nondegenerate shared-source overlap;
- finite ancient-time persistence.

This requires spacetime, not only slice, inheritance.

---

# 44. Ancient-label inheritance graph

A Type-II defect may route:

$$
\boxed{
TS/GP/HF
\to
TS^{anc}/GP^{anc}/HF^{anc}
}
$$

only if the corresponding peak inheritance gates hold.

Otherwise:

$$
\boxed{
\text{defect label remains on the mass scale or moves to a subpeak scale}.
}
$$

---

# 45. Peak-label escape branch

If:

$$
\Theta_D^{peak}=0,
$$

the defect carrier probability leaves every bounded ancient peak region.

Then:

$$
v_\infty
$$

is a bounded ancient **unlabeled peak profile** relative to that defect.

The old C6 cycle lives at the larger mass scale,

while the amplitude peak is a separate fiber object.

This is:

$$
\boxed{
\textbf{Mass/Peak Defect Decoupling}.
}
$$

---

# 46. Partial inheritance

If:

$$
0<\Theta_D^{peak}<1,
$$

a finite fraction of defect carrier remains in the peak frame,

while the rest escapes toward the mass scale.

Then the correct limit object is:

$$
\boxed{
\textbf{ancient peak defect}
+
\textbf{escaping defect tail}.
}
$$

No one-node ancient label is complete.

---

# 47. Full peak tightness

If:

$$
\Theta_D^{peak}=1,
$$

the entire normalized defect carrier is tight in the peak frame.

Then, subject to local compactness/stability:

$$
\boxed{
\text{the defect carrier can have a full ancient probability limit}.
}
$$

But C6-O.2 still says this label is a global relative:

$$
L^3
$$

spectator.

This is not a problem:

ancient carrier status is local/absolute.

---

# 48. Local absolute peak carrier

For a peak core:

$$
B_R,
$$

define local absolute critical loads:

$$
\boxed{
\mathbf A_{peak,n}^{D}(R)
}
$$

containing whichever are relevant:

- :
  $$
  \int_{B_R}|v_n|^3;
  $$
- :
  $$
  \int_{B_R}\lambda_2^+|S|^2;
  $$
- :
  $$
  \int_{B_R}|Q|;
  $$
- local derivative high-set measure;
- aligned finite-radius pressure capacity;
- TS shared-source spacetime mass.

Ancient label inheritance should require:

$$
\boxed{
\liminf_n
\|
\mathbf A_{peak,n}^{D}(R)
\|
>0
}
$$

for some fixed:

$$
R.
$$

---

# 49. Absolute ancient carrier floor from peak nontriviality

Since:

$$
|v_\infty(0,0)|=1
$$

and:

$$
v_\infty
$$

is continuous,

there exists:

$$
R_0>0
$$

such that:

$$
|v_\infty(z,0)|
\ge
1/2
$$

on a sufficiently small neighborhood of:

$$
0.
$$

Hence:

$$
\boxed{
\int_{B_{R_0}}
|v_\infty(z,0)|^3dz
>0.
}
$$

So the bounded ancient peak is automatically an **absolute local velocity critical carrier**.

### Guard

This does not imply any derivative-based TS/GP/HF defect label.

---

# 50. Flat ancient peak

It is logically possible at the level of current compactness information that:

$$
v_\infty(\cdot,0)
$$

is spatially constant near/all of the peak frame,

so:

$$
S[v_\infty]=0
$$

and derivative-based defect labels vanish.

C6-O calls:

$$
\boxed{
\textbf{Ancient Flat-Peak Escape}.
}
$$

### Guard

This is a state-space possibility/edge failure,

not a construction of a singular solution.

---

# 51. Derivative order $k=1$ and local geometry

For:

$$
k=1,
$$

$$
\boxed{
\widehat A_{1,n}^{peak}
=
A_{1,n}/A_{0,n}^2.
}
$$

Three regimes:

## O-S0

$$
\widehat A_{1,n}^{peak}\to0.
$$

Ancient peak flattening.

## O-S1

$$
\widehat A_{1,n}^{peak}\asymp1.
$$

Strain/vorticity geometry may survive at amplitude scale.

## O-S∞

$$
\widehat A_{1,n}^{peak}\to\infty.
$$

A smaller gradient scale:

$$
A_{1,n}^{-1/2}
\ll
A_{0,n}^{-1}
$$

exists.

Thus GP/TS geometry can itself be a **subpeak** phenomenon.

---

# 52. Mass–peak–gradient three-scale tower

A Type-II relative-dominant carrier can therefore have:

$$
\boxed{
\ell_n
\gg
a_n
\gg
b_{1,n}
}
$$

if:

$$
\widehat A_{1,n}^{peak}\to\infty.
$$

More generally:

$$
\boxed{
\ell_n
\gg
a_n
\gg
b_{k,n}
}
$$

for any escaping derivative order.

This is:

$$
\boxed{
\textbf{Mass–Peak–Derivative Tower}.
}
$$

---

# 53. No finite scale closure from amplitude alone

The existence of bounded ancient:

$$
v_\infty
$$

at peak scale does not prove the critical derivative fiber has compactified.

If:

$$
\widehat A_{k,n}^{peak}\to\infty,
$$

the high derivative defect lives below the ancient peak scale.

Thus:

$$
\boxed{
\textbf{ancient velocity compactness}
\neq
\textbf{high-derivative compactness}.
}
$$

This is a new critical fiber layer.

---

# 54. Pressure-tail decoupling closes one mass/peak loophole

C6-L/M worried:

a huge spectator mass at the mass scale might still drive the peak through far pressure.

C6-O.8 shows:

at the bounded record-peak normalization,

sources escaping to:

$$
|z|\to\infty
$$

produce vanishing pressure-Hessian influence:

$$
O(R^{-2}).
$$

Therefore:

$$
\boxed{
\textbf{mass-scale relative }L^3\textbf{ tail cannot preserve an }O(1)
\textbf{ GP Hessian label at the peak by itself}.
}
$$

Any inherited:

$$
GP^{anc}
$$

pressure signature must be supported by finite peak-frame pressure sources.

---

# 55. Pressure gradient vs Hessian guard

C6-O.8 is specifically a:

$$
\boxed{
\nabla^2p
}
$$

tail estimate.

The pressure itself and lower derivatives have different far-field decay/invariance issues.

C6 GP geometry uses pressure Hessian,

so the theorem closes the relevant channel.

Do not upgrade it to a statement about every pressure observable.

---

# 56. Duhamel/nonlinear tail guard

Unlike pressure Hessian,

nonlocal projection operators of order:

$$
0
$$

can have slower spatial kernels.

Therefore C6-O does not claim every far-field nonlinear influence decouples as:

$$
R^{-2}.
$$

The mass-tail closure is strongest for the GP pressure-Hessian channel.

HF/TS nonlinear inheritance still needs its own source localization/coherence audit.

---

# 57. Type-II peak routes

C6-O now distinguishes two external Type-II zoom interfaces.

## O-NS

Peak parabolic amplitude scale:

$$
a_n=A_n^{-1}
$$

with:

$$
a_n^2
$$

time scaling.

This preserves exact Navier–Stokes and yields a bounded ancient N–S profile.

## O-EULER

For particular Type-II scenarios with a different zoom balance,

recent Seregin analysis uses Euler scaling and obtains ancient Euler limit equations under its stated hypotheses.

### Guard

$$
\boxed{
\textbf{O-EULER is scenario-conditional, not universal for all C6 Type-II carriers}.
}
$$

---

# 58. Relation to C6-K conditional Eulerization

C6-K observed that amplitude normalization without the matching N–S parabolic spatial/time normalization formally suppresses linear/viscous terms and can lead to an Euler-dominant limit under compactness assumptions.

Seregin's recent Type-II program provides a rigorous external example of this general idea in specific local Type-II scenarios:

$$
\boxed{
\text{Type-II zoom}
\to
\text{ancient Euler structure}
}
$$

under additional scale/local-energy hypotheses.

This validates the **interface**,

not a blanket identification.

---

# 59. Ancient N–S rigidity gates

If a peak-inherited:

$$
TS^{anc},
GP^{anc},
HF^{anc}
$$

state also satisfies:

- bounded:
  $$
  L^3
  $$
  along a backward sequence;
- Type-I decay;
- axisymmetric/no-swirl or another known ancient Liouville class;
- another profile-specific rigidity hypothesis;

then known external ancient-solution theorems may eliminate it.

Without these assumptions:

$$
\boxed{
\textbf{bounded ancient profile remains open in general 3D}.
}
$$

---

# 60. Ancient Euler rigidity gate

For a scenario entering an ancient Euler limit,

one may use whatever Euler Liouville/conservation theorem is valid for the resulting function class.

C6-O does not state a universal ancient Euler Liouville theorem.

The exact scenario assumptions and limit class must be preserved.

---

# 61. Peak-inherited defect cycle semantics

Suppose:

$$
D_n
$$

is a recurrent Type-II defect label.

A peak-inherited ancient state requires:

1. same defect carrier remains peak-tight/partially tight;
2. local absolute defect load survives;
3. derivative scale does not escape below the peak for the observables used;
4. time-window representation remains legal;
5. pressure provenance is recomputed;
6. strict margins survive local convergence.

Only then:

$$
\boxed{
D_n
\to
D^{anc}.
}
$$

---

# 62. Peak-inherited state is not automatically recurrent

An ancient profile:

$$
v_\infty(\tau)
$$

exists for:

$$
\tau\le0.
$$

A defect at:

$$
\tau=0
$$

does not prove:

$$
D^{anc}
$$

recurs for:

$$
\tau\to-\infty.
$$

Therefore:

$$
\boxed{
\textbf{ancient inheritance}
\neq
\textbf{ancient recurrence}.
}
$$

A separate ancient-time heredity theorem is required.

---

# 63. Mass-scale defect branch

If:

$$
\Theta_D^{peak}=0,
$$

but the mass-scale defect remains absolute-visible,

then:

$$
\boxed{
\text{defect cycle lives on the expanding mass scale in peak variables}.
}
$$

The bounded ancient peak profile is then a local amplitude object,

not the defect carrier.

The correct full state is two-scale:

$$
\boxed{
(
v_\infty^{peak},
D^{mass}
).
}
$$

---

# 64. Two-scale skew product

Define:

$$
\boxed{
\Theta_n^{MP}
=
\left(
\Theta_n^{mass},
\Theta_n^{peak},
\mathfrak R_n^{MP}
\right),
}
$$

where:

$$
\mathfrak R_n^{MP}\to\infty.
$$

A complete Type-II cycle must explain:

- evolution at mass scale;
- peak ancient dynamics;
- transfer of labels/pressure/source between scales.

This is a two-scale skew product,

not a single defect node.

---

# 65. Subpeak derivative branch

If:

$$
\widehat A_{k,n}^{peak}\to\infty,
$$

augment:

$$
\Theta_n^{MP}
$$

by:

$$
\boxed{
\Theta_n^{der,k}
}
$$

at scale:

$$
b_{k,n}.
$$

Then:

$$
\boxed{
\ell_n
\gg
a_n
\gg
b_{k,n}.
}
$$

The full state becomes a multi-level tower rather than only mass/peak pair.

---

# 66. Peak-scale closure test

For each Type-II candidate defect cycle:

### O-Test 1 — Peak tightness

Does the defect carrier remain in bounded peak radii?

### O-Test 2 — Absolute load

Does the relevant local critical defect load stay:

$$
>0?
$$

### O-Test 3 — Derivative scale

Are the derivative orders used by the label:

$$
O(1)
$$

in peak normalization?

### O-Test 4 — Time window

Does the dynamic defect occupy a legal ancient-time window?

### O-Test 5 — Pressure

Does the local/far pressure provenance survive after tail decoupling/repartition?

### O-Test 6 — Ancient rigidity

Does the inherited ancient state enter an external Liouville/regularity class?

If any early test fails,

the label remains on another scale/fiber.

---

# 67. C6-O.10: Mass–Peak Two-Scale Closure Theorem

Consider a Type-II relative-dominant carrier sequence at record peak times.

After subsequence one of:

## O-A — Peak-Inherited Ancient Defect

There exists a bounded peak region/time window carrying:

- nonzero local absolute defect load;
- stable defect margins;
- legal pressure/source metadata;

and no required derivative scale escapes below:

$$
a_n.
$$

Then a corresponding local ancient defect state:

$$
D^{anc}
$$

can be extracted conditionally on the local convergence hypotheses.

## O-B — Mass-Scale Defect / Peak Escape

The defect carrier is not peak-tight or its local absolute load vanishes.

Then:

$$
v_\infty
$$

is an unlabeled/partially labeled ancient peak profile,

while the defect remains at:

$$
\ell_n
$$

or another larger scale.

## O-C — Subpeak Derivative Restart

For some required derivative order:

$$
k,
$$

$$
\widehat A_{k,n}^{peak}\to\infty.
$$

Then:

$$
b_{k,n}\ll a_n
$$

and the defect must be rebound below the amplitude scale.

### Additional fact

In every branch the global relative:

$$
L^3
$$

mass escapes bounded peak regions;

and its remote pressure-Hessian influence on fixed peak cores vanishes.

---

# 68. Significance of O-A

O-A is the only branch where the external bounded-ancient literature can directly see the C6 defect label.

Even then:

$$
\boxed{
\textbf{ancient Liouville still requires additional hypotheses}.
}
$$

So O-A is an interface,

not a completed contradiction.

---

# 69. Significance of O-B

O-B says the C6 cycle and the bounded ancient amplitude peak are different carriers.

This invalidates any argument which:

1. extracts a bounded ancient profile;
2. applies a Liouville theorem;
3. concludes the old mass-scale defect cycle is killed;

without proving peak-label inheritance.

---

# 70. Significance of O-C

O-C shows:

even the bounded ancient amplitude peak may fail to resolve the high-order critical fiber.

The defect can descend to another smaller scale:

$$
b_{k,n}.
$$

Thus Type-II blow-up can generate a **scale tower**:

$$
\boxed{
\text{mass}
\to
\text{peak}
\to
\text{derivative}.
}
$$

No finite-depth theorem is established here.

---

# 71. Carrier completeness correction after C6-O

C6-M asked whether TS/GP/HF carry a fixed fraction of global critical mass.

C6-N corrected the minimal notion to local absolute critical visibility.

C6-O adds:

$$
\boxed{
\textbf{carrier completeness must also be scale-indexed}.
}
$$

A label may be:

- mass-scale complete;
- peak-scale complete;
- derivative-scale complete;
- spectator at another scale.

Therefore a single global carrier flag is insufficient.

---

# 72. Scale-indexed carrier label

Define:

$$
\boxed{
\mathsf{Carr}(D;\ell)
}
$$

to mean:

defect:

$$
D
$$

has a nonzero local absolute critical carrier at scale:

$$
\ell.
$$

For Type-II:

$$
\boxed{
\mathsf{Carr}(D;\ell_n)
}
$$

does not imply:

$$
\boxed{
\mathsf{Carr}(D;a_n).
}
$$

Likewise:

$$
\mathsf{Carr}(D;a_n)
$$

does not imply:

$$
\mathsf{Carr}(D;b_{k,n}).
$$

---

# 73. Peak scale pressure visibility is localizable

A particularly strong C6-O result is:

although:

$$
L^3
$$

carrier completeness is scale-indexed,

GP pressure-Hessian influence on fixed peak cores is asymptotically **localizable** because of:

$$
R^{-2}
$$

tail decay.

Thus pressure Hessian is better behaved across the mass/peak split than global critical mass itself.

This may become a key rigidity advantage for ancient:

$$
GP^{anc}.
$$

---

# 74. Peak GP carrier test

A peak ancient GP state should track:

$$
\boxed{
\Theta_{GP}^{peak}
=
\left(
\int_{B_R}|Q|,
\vartheta,
[e_1],
\nabla^2q,
\operatorname{sig}F_R,
\text{finite-radius provenance}
\right).
}
$$

It should **not** retain the old mass-scale far-pressure label verbatim.

---

# 75. Peak HF carrier test

A peak ancient HF state should track:

$$
\boxed{
\Theta_{HF,k}^{peak}
=
\left(
\widehat A_k^{peak},
\Gamma_k^{loc},
\text{component/sign geometry},
\Theta_t^{peak},
\text{setup}
\right).
}
$$

If:

$$
\widehat A_k^{peak}\to\infty,
$$

the state exits to derivative-tower restart.

---

# 76. Peak TS carrier test

A peak ancient TS state should track:

$$
\boxed{
\Theta_{TS}^{peak}
=
\left(
M_M^{peak},
M_O^{peak},
\Omega_{ST}^{peak},
\Theta_t^{peak},
\text{shared source carrier}
\right).
}
$$

If either source load vanishes,

the peak ancient profile is TS-spectator even when a mass-scale TS state persists.

---

# 77. Recent Type-II interface and C6

Seregin's recent Type-II analysis reinforces a key C6-O methodological lesson:

$$
\boxed{
\textbf{Type-II scenarios require choosing the zoom according to the dominant scaling balance}.
}
$$

Different Type-II regimes can produce:

- bounded ancient N–S peak profiles;
- Euler-dominant ancient limits;
- further critical scale escape.

C6 should not force all Type-II carriers into one universal normalization.

---

# 78. External ancient profile gates

Potential external kills after O-A include:

## O-K1 — ancient $L^3$ backward-sequence bound

Albritton–Barker Liouville gate.

## O-K2 — Type-I ancient decay

Type-I ancient equivalence/rigidity framework.

## O-K3 — special symmetry classes

Known ancient Liouville theorems in axisymmetric/special regimes.

## O-K4 — self-similar/DSS ancient recurrence

Chae/Chae–Wolf style field-level no-go if applicable.

None is universal for arbitrary bounded ancient 3D profiles.

---

# 79. Type-II Euler external gate

For a scenario satisfying the hypotheses of a Type-II Euler-scaling theorem,

an ancient Euler limit can carry its own:

- local energy;
- vorticity;
- conservation;
- Liouville constraints.

C6-O records this as:

$$
\boxed{
\mathsf{EULER\_TYPEII}
}
$$

rather than merging it with:

$$
GP/HF/TS^{anc}.
$$

---

# 80. Current Type-II carrier taxonomy

C6-O final taxonomy:

$$
\boxed{
\mathfrak T^{II}_{carrier}
=
\{
\text{PEAK-ANCIENT},
\text{MASS-ESCAPE},
\text{DERIVATIVE-RESTART},
\text{EULER-SCENARIO}
\}.
}
$$

These branches can overlap in different observables,

so they are typed routes rather than mutually exclusive physical universes.

---

# 81. What C6-O eliminates

## O-DEL1

$$
\text{bounded ancient peak}
\Rightarrow
\text{global critical-mass carrier}.
$$

FALSE.

## O-DEL2

$$
\text{peak-tight defect}
\Rightarrow
\text{positive global relative }L^3\text{ overlap}.
$$

FALSE; the overlap tends to zero.

## O-DEL3

$$
\text{mass-scale far pressure tail can maintain arbitrary }O(1)
\text{ peak pressure Hessian}.
$$

FALSE under record peak boundedness; tail is:

$$
O(R^{-2}).
$$

## O-DEL4

$$
\text{all derivative orders are resolved by peak-amplitude scaling}.
$$

FALSE.

## O-DEL5

$$
\text{global HF threshold automatically passes to the ancient peak}.
$$

FALSE.

## O-DEL6

$$
\text{ancient extraction automatically inherits TS/GP/HF}.
$$

FALSE.

## O-DEL7

$$
\text{all Type-II branches should use the same N–S peak zoom}.
$$

FALSE as a universal methodological rule; specific Euler-scaling scenarios exist.

---

# 82. What remains open

## O-R1 — Local absolute defect completeness at the peak

Does every actual Type-II singular peak carry at least one TS/GP/HF absolute defect label?

## O-R2 — GP ancient rigidity

Can a peak-inherited GP state be ruled out or classified?

## O-R3 — HF derivative tower depth

Can:

$$
b_{k,n}\ll a_n
$$

repeat indefinitely?

## O-R4 — TS ancient source inheritance

Can shared source overlap pass robustly to an ancient limit?

## O-R5 — Mass-scale cycle dynamics

If label peak-escapes, can the larger mass-scale defect recur independently of the peak?

## O-R6 — pressure provenance at the peak

Can finite-radius local/far pressure structure become hereditary in ancient time?

## O-R7 — Type-II Euler route compatibility

Which C6 carrier metadata survive an Euler scaling rather than N–S peak scaling?

---

# 83. Strategic interpretation

C6-N found:

$$
\boxed{
\textbf{mass compactness}
\neq
\textbf{peak compactness}.
}
$$

C6-O now resolves part of that mismatch.

The global relative:

$$
L^3
$$

mass must leave every bounded ancient peak region.

But that does **not** prevent a local absolute TS/GP/HF label from surviving.

In fact, the correct ancient inheritance test is:

$$
\boxed{
\textbf{peak tightness}
+
\textbf{local absolute defect load}
+
\textbf{scale-compatible derivatives}
+
\textbf{finite-time-window compatibility}
+
\textbf{pressure repartition}.
}
$$

At the same time,

the huge mass tail at:

$$
|z|\to\infty
$$

becomes harmless to the local **pressure Hessian** at rate:

$$
R^{-2}.
$$

So the mass/peak two-scale problem is not one inseparable global object.

It separates into:

$$
\boxed{
\text{global critical-mass tail}
}
$$

and:

$$
\boxed{
\text{local ancient defect dynamics}.
}
$$

The remaining obstacle is now highly specific:

> **which C6 defect labels can survive as nonzero local absolute structures in a bounded ancient peak profile?**

And if a derivative label cannot,

does it always trigger another lower scale?

That is the natural next paper.

---

# 84. Proposed C6-P

$$
\boxed{
\textbf{C6-P — Ancient Defect-State Classification,
Derivative-Tower Rigidity,
and Peak-Local Pressure Closure}.
}
$$

---

# 85. C6-P proof obligations

## P1 — ancient TS stability

Give sufficient compactness/margin conditions for:

$$
TS^{anc}.
$$

## P2 — ancient GP stability

Preserve:

- strong-middle geometry;
- Q load;
- local pressure Hessian;
- finite-radius provenance.

## P3 — ancient HF stability

Preserve component/sign geometry with peak-local derivative normalization.

## P4 — flattening branch

Classify bounded ancient peaks with:

$$
\widehat A_1^{peak}\to0.
$$

## P5 — derivative tower

If:

$$
\widehat A_k^{peak}\to\infty,
$$

rebind at:

$$
b_{k,n}
$$

and recompute horizon/label metadata.

## P6 — derivative-tower nesting

Find a retention/scale law analogous to C6-M nested carrier rigidity.

## P7 — ancient pressure heredity

Use peak pressure tail decoupling to test whether local/far GP provenance can stabilize for:

$$
\tau\to-\infty.
$$

## P8 — ancient Liouville interfaces

Audit all usable bounded ancient no-go hypotheses.

## P9 — Type-II Euler route

Map C6 metadata under Seregin-type Euler scaling where legal.

## P10 — singular carrier graph rebuild

Replace generic Type-II node by:

- peak ancient labeled states;
- mass-scale states;
- derivative subpeak states;
- Euler-scenario states.

---

# 86. Major no-go audit

### NG-O1

$$
\text{global relative }L^3\text{ mass stays tight at a bounded ancient peak}.
$$

FALSE.

### NG-O2

$$
\text{ancient defect inheritance should use global relative mass}.
$$

FALSE.

### NG-O3

$$
\text{peak-tight defect label has nonzero global relative }L^3\text{ overlap}.
$$

FALSE.

### NG-O4

$$
\text{far mass-scale tail preserves }O(1)\text{ pressure-Hessian forcing at the peak}.
$$

FALSE under record peak boundedness.

### NG-O5

$$
\text{peak scaling resolves all HF derivative maxima}.
$$

FALSE.

### NG-O6

$$
\widehat A_k^{peak}\to\infty
\text{ can remain a bounded peak-scale HF label}.
$$

FALSE.

### NG-O7

$$
\text{ancient peak label automatically recurrent in ancient time}.
$$

FALSE.

### NG-O8

$$
\text{all Type-II scenarios have the same limit equation}.
$$

FALSE as a methodological claim; scenario-dependent Euler limits exist.

---

# 87. X-Integration guards update

## G-MP

Preserve separately:

$$
\ell_n,
\quad
a_n,
\quad
\mathfrak R_n^{MP}.
$$

## G-PKTIGHT

Every ancient defect inheritance stores:

$$
\Theta_D^{peak}.
$$

## G-ABSANC

Use local absolute defect loads, not global relative:

$$
L^3
$$

fractions, for ancient inheritance.

## G-DERPK

Store:

$$
\widehat A_k^{peak}.
$$

## G-DERTOWER

$$
\widehat A_k^{peak}\to\infty
$$

triggers derivative-scale rebinding.

## G-PKWIN

Dynamic labels store:

$$
\Theta_t^{peak}.
$$

## G-PTAIL

Mass-tail pressure-Hessian influence obeys the peak-tail audit.

## G-PPART

Pressure provenance is repartitioned at the peak scale.

## G-TYPEIIROUTE

Keep Navier–Stokes peak scaling and scenario-specific Euler scaling as different routes.

---

# 88. True ETN update

Type-II two-scale state:

$$
\boxed{
\Theta_{MP}^{C6O}
=
\left\langle
\ell_n,
a_n,
\mathfrak R_n^{MP},
\mu_{3,n}^{peak},
\eta_{D,n}^{peak},
\Theta_D^{peak},
\mathbf A_{peak,n}^D,
\{\widehat A_{k,n}^{peak}\},
\Theta_{t,n}^{peak},
\nabla^2q_n,
\text{pressure provenance},
\text{route}
\right\rangle.
}
$$

Peak inheritance classes:

$$
\boxed{
\mathfrak I_{peak}
=
\{
\text{ANCIENT-LABELED},
\text{MASS-ESCAPE},
\text{DERIVATIVE-RESTART},
\text{PARTIAL}
\}.
}
$$

---

# 89. Formal status

$$
\boxed{
\begin{aligned}
\mathfrak R_n^{MP}\to\infty
&:\ \mathrm{PROVED\ FROM\ C6N\ TYPEII\ BRANCH},\\
\text{peak relative-mass escape}
&:\ \mathrm{PROVED},\\
\Theta_3^{peak}=0
&:\ \mathrm{PROVED},\\
\text{peak defect tightness}
&:\ \mathrm{DEFINED},\\
\text{peak-tight defect/global-relative-mass decoupling}
&:\ \mathrm{PROVED},\\
\text{local absolute defect inheritance}
&:\ \mathrm{PROVED\ UNDER\ STRONG\ LOCAL\ CONVERGENCE},\\
\widehat A_{k}^{peak}
&:\ \mathrm{DEFINED},\\
\text{derivative-to-peak trichotomy}
&:\ \mathrm{PROVED},\\
\text{derivative-tower restart}
&:\ \mathrm{PROVED},\\
\text{HF peak inheritance}
&:\ \mathrm{CONDITIONAL},\\
\text{TS peak-window inheritance}
&:\ \mathrm{CONDITIONAL},\\
\text{GP local geometry inheritance}
&:\ \mathrm{CONDITIONAL},\\
\text{mass-tail/peak-pressure Hessian decoupling}
&:\ \mathrm{PROVED},\\
\text{full pressure provenance inheritance}
&:\ \mathrm{NOT\ AUTOMATIC},\\
\text{ancient TS/GP/HF state}
&:\ \mathrm{DEFINED},\\
\text{ancient label recurrence}
&:\ \mathrm{OPEN},\\
\text{Seregin Type-II Euler route}
&:\ \mathrm{EXTERNAL/SCENARIO\mbox{-}CONDITIONAL},\\
\text{mass--peak two-scale closure reduction}
&:\ \mathrm{PROVED\ AT\ CURRENT\ STATE\ LEVEL},\\
\text{global regularity}
&:\ \mathrm{OPEN}.
\end{aligned}
}
$$

---

# 90. Conclusion

C6-N showed:

$$
\boxed{
\text{relative-dominant Type-II carrier}
}
$$

has two separated scales:

$$
\boxed{
\ell_n
\gg
a_n.
}
$$

C6-O now determines what this means for defect inheritance.

At peak amplitude scale:

$$
a_n=A_n^{-1},
$$

record rescaling yields:

$$
\boxed{
\|v_n(\tau)\|_\infty\le1,
}
$$

and a nontrivial bounded ancient N–S limit.

But global relative:

$$
L^3
$$

mass obeys:

$$
\boxed{
\mu_{3,n}^{peak}(B_R)\to0
}
$$

for every fixed:

$$
R.
$$

So:

$$
\boxed{
\textbf{global critical mass never becomes a compact ancient carrier}.
}
$$

If a TS/GP/HF defect label remains peak-tight,

it therefore becomes a global relative:

$$
L^3
$$

spectator.

This is not a defect.

It means:

$$
\boxed{
\textbf{ancient label inheritance must be local/absolute rather than globally relative}.
}
$$

Then C6-O adds the derivative-scale trichotomy:

$$
\boxed{
\widehat A_{k,n}^{peak}
=
A_{k,n}/A_{0,n}^{k+1}.
}
$$

If:

$$
\to0,
$$

the ancient peak flattens at derivative order:

$$
k.
$$

If:

$$
O(1),
$$

that derivative order really lives at peak scale.

If:

$$
\to\infty,
$$

the scale:

$$
b_{k,n}
=
A_{k,n}^{-1/(k+1)}
$$

satisfies:

$$
\boxed{
b_{k,n}\ll a_n,
}
$$

so high-order defect must restart below the ancient peak scale.

Thus Type-II can produce:

$$
\boxed{
\text{mass}
\gg
\text{peak}
\gg
\text{derivative}
}
$$

tower.

For GP pressure,

the two-scale problem is better behaved:

the global relative mass tail escapes to:

$$
|z|\to\infty,
$$

but record peak boundedness and pressure-Hessian kernel decay give:

$$
\boxed{
\sup_{B_{R_0}}
|\nabla^2q_{>R}|
\lesssim
R^{-2}.
}
$$

Hence:

$$
\boxed{
\textbf{mass-scale tail cannot maintain an }O(1)
\textbf{ pressure-Hessian label at the bounded ancient peak}.
}
$$

Peak GP pressure must come from finite peak radii and its provenance must be rebuilt there.

Therefore the Type-II branch finally reduces to:

$$
\boxed{
\textbf{Peak-Inherited Ancient Defect}
}
$$

or:

$$
\boxed{
\textbf{Mass-Scale Defect / Peak Label Escape}
}
$$

or:

$$
\boxed{
\textbf{Subpeak Derivative Restart}.
}
$$

A recent 2026 Type-II analysis by Seregin supplies an additional, scenario-dependent Euler-scaling route, showing that specific Type-II scalings can lead to ancient Euler limits and Euler Liouville analysis; C6-O keeps this as a distinct external interface rather than a universal identification.

The next real target is therefore:

> **classify the defect states which can actually survive on a bounded ancient peak, and determine whether derivative-tower restarts can continue indefinitely.**

---

# 91. Proposed C6-P

$$
\boxed{
\textbf{C6-P — Ancient Defect-State Classification,
Derivative-Tower Rigidity,
and Peak-Local Pressure Closure}.
}
$$

---

# References

1. D. Albritton, T. Barker, *Localised necessary conditions for singularity formation in the Navier–Stokes equations with curved boundary*, arXiv:1811.00507; J. Differential Equations 269 (2020), 7529–7573.
2. D. Albritton, T. Barker, *On local Type I singularities of the Navier–Stokes equations and Liouville theorems*, arXiv:1811.00502; J. Math. Fluid Mech. 21 (2019), 43.
3. G. Koch, N. Nadirashvili, G. Seregin, V. Šverák, *Liouville theorems for the Navier–Stokes equations and applications*, arXiv:0709.3599.
4. I. Gallagher, G. S. Koch, F. Planchon, *A profile decomposition approach to the $L^\infty_t(L^3_x)$ Navier–Stokes regularity criterion*, arXiv:1012.0145.
5. Z. Bradshaw, T.-P. Tsai, *On the local pressure expansion for the Navier–Stokes equations*, arXiv:2001.11526.
6. Z. Grujić, L. Xu, *Asymptotic Criticality of the Navier–Stokes Regularity Problem*, arXiv:1911.00974; J. Math. Fluid Mech. 26, 53 (2024).
7. G. Seregin, *On potential Type II blowups for the Navier–Stokes equations*, arXiv:2606.29468 (2026).
8. T. Barker, C. Prange, *Localized smoothing for the Navier–Stokes equations and concentration of critical norms near singularities*, arXiv:1812.09115.

# Internal dependencies

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
\textbf{C6-P — Ancient Defect-State Classification,
Derivative-Tower Rigidity,
and Peak-Local Pressure Closure}
}
$$