---
title: "Navier–Stokes C5-G: Pressure-Signature Defects, Vorticity Constraint Complements, and Fixed-Order Derivative-Gate Closure"
subtitle: "A Theorem-Ready Fixed-k Direct Sparseness Gate, Pressure-Poisson Re-entry from Vorticity Leakage, and Signature-Boundary Compactification"
version: "v0.1"
date: "2026-08-15"
author: "Neo.K / EveMissLab"
language: "en"
status: "Theorem-style fixed-order gate closure / pressure-signature and constraint-complement reduction"
epistemic_status: "Exact component-volume geometry + direct interface to Grujić–Xu Theorem 3.5 + exact pressure Poisson/projection identities + conditional pressure-signature heredity. Does NOT prove Navier–Stokes regularity."
---

# Navier–Stokes C5-G
# Pressure-Signature Defects, Vorticity Constraint Complements, and Fixed-Order Derivative-Gate Closure

## 0. Current Positioning

C5-F compressed the residual network into:

$$
\boxed{
\text{Pressure-Signature Defect}
}
$$

$$
\boxed{
\text{Vorticity Constraint-Complement Defect}
}
$$

$$
\boxed{
\text{Fixed-Order Derivative-Gate Defect}
}
$$

$$
\boxed{
\text{Asymptotically-Critical Derivative-Order Escape}.
}
$$

Among these, the fixed-order direct gate is the most worthy of priority focus.

The reasons are:

C5-E/F have already discovered:

- middle-gap cubic intermittency can generate a very small strain active volume;
- strain-derivative leakage can generate critical $D^2u$ amplitude;
- the spatial exponent itself starts to become favorable;

but previously still retained:

- SHELLFULL;
- COMPSIGN;
- MULT;
- TIMECHAIN;

and other theorem-interface debts.

C5-G now makes a cleaner move:

> **Directly apply a global volume bound to the component/sign superlevel sets of the full $D^ku$.**

Thus:

- no shell-to-full conversion is needed;
- no strain-to-$Du$ conversion is needed;
- no need to guess the selected component/sign in advance;
- the component/sign high set required by Theorem 3.5 is directly controlled itself.

Main results of this round:

1. For any fixed $k\ge1$,
   the global volume of the full derivative component/sign superlevel set satisfies:
   $$
   \boxed{
   |V_{\lambda,k}^{i,\pm}|
   \le
   \lambda^{-2}
   \|D^ku\|_2^2
   \|D^ku\|_\infty^{-2};
   }
   $$
2. The volume-to-line lemma converts it into a theorem-ready 1D sparseness scale:
   $$
   \boxed{
   r_{vol,k}
   \lesssim
   \|D^ku\|_2^{2/3}
   \|D^ku\|_\infty^{-2/3};
   }
   $$
3. Compared with the Grujić–Xu 2024 Theorem 3.5 direct scale:
   $$
   \boxed{
   r_{GX,k}
   =
   \frac1{
   2^k c(M,\|u_0\|_2)
   \|D^ku(s)\|_\infty^{3/(2k+3)}
   }
   }
   $$
   ;
4. If at a theorem-admissible later time:
   $$
   s=s(t)
   $$
   we have:
   $$
   \boxed{
   r_{vol,k}(s)
   \le
   r_{GX,k}(s),
   }
   $$
   then Theorem 3.5 genuinely closes;
5. Therefore, the fixed-order `COMPSIGN` and `SHELLFULL` defects can be bypassed in this direct-volume route;
6. The only genuine fixed-order direct survivors remaining are:
   $$
   \boxed{
   \text{Derivative Effective-Volume / Multiplicity Defect}
   \vee
   \text{Theorem Later-Time Defect};
   }
   $$
7. For $k=1$:
   $$
   \|Du\|_2^2=2\|S\|_2^2,
   $$
   thus yielding an explicit strain-enstrophy / raw-gradient gate;
8. Pressure signature switching under the common hereditary far-matrix route must yield:
   $$
   \boxed{
   \text{Pressure Turnover/Fragmentation}
   \vee
   \det F\to0;
   }
   $$
9. Middle-gap degeneration will not erase the compressive axis,
   so the signature-boundary and axis metadata can be compactified simultaneously;
10. Vorticity-dominant leakage utilizes the exact pressure Poisson identity:
    $$
    \Delta p=-|S|^2+\frac12|\omega|^2
    $$
    to directly synchronize to:
    $$
    \boxed{
    (\Delta p)_+\text{ pressure-curvature activity};
    }
    $$
11. The vorticity strain-space complement is then compressed by the exact orthogonal ledger into:
    $$
    \boxed{
    \text{Actual Pressure Hessian}
    \vee
    \text{Advection Complement}
    \vee
    \text{Strain-Square Complement};
    }
    $$
12. Consequently, the `Vorticity Constraint-Complement Defect` is no longer a free motif;
13. If the fixed-$k$ direct gate permanently fails to close,
    it can be quantified as a recurrent concentration defect of:
    $$
    \boxed{
    \mathfrak G_k^{dir}>1
    }
    $$
14. The correct logic for derivative-order escalation becomes:
    - fixed $k$ recurrent concentration/time defect;
    - or eventually no fixed order survives, only then sending $k\to\infty$;
15. C5-G, for the first time, connects Grujić–Xu Theorem 3.5 into a genuinely measurable **theorem-ready fixed-order gate ratio**.

---

# 1. Fresh primary-source audit

## 1.1 Grujić–Xu 2024 — Theorem 3.5

Official version of record:

$$
\boxed{
\text{J. Math. Fluid Mech. 26, Article 53 (2024)}.
}
$$

For velocity:

Let:

$$
t
$$

be the:

$$
D^ku
$$

escape time.

Theorem 3.5 requires the existence of a later time:

$$
\boxed{
s=s(t)
}
$$

located in the explicit interval:

$$
t
+
C_1
\|D^ku(t)\|_\infty^{-6/(2k+3)}
\le
s
\le
t
+
C_2
\|D^ku(t)\|_\infty^{-6/(2k+3)}
$$

in $d=3$ notation,

such that for any:

$$
x_0,
$$

the selected:

$$
D^ku
$$

component/sign superlevel set:

$$
\boxed{
V_{\lambda}^{i,\pm}
=
\{
x:
(D^ku)_i^\pm(x,s)
>
\lambda
\|D^ku(s)\|_\infty
\}
}
$$

at some scale:

$$
\boxed{
\rho
\le
\frac1{
2^k c(M,\|u_0\|_2)
\|D^ku(s)\|_\infty^{3/(2k+3)}
}
}
$$

is 1D $\delta$-sparse around:

$$
x_0.
$$

Then:

$$
T^\ast
$$

is not a blow-up time.

### C5-G status

We treat this theorem as an external gate.

We do not modify the theorem hypotheses.

---

# 2. Grujić–Xu 2024 — Theorem 3.7

Theorem 3.7 obtains a fixed-$k$ a-priori volumetric sparseness scale from the Leray energy bound:

$$
\boxed{
r_{apr,k}
\sim
c(\|u_0\|_2)
\|D^ku\|_\infty^{-2/(2k+3)}
}
$$

for velocity in $d=3$.

While the Theorem 3.5 direct regularity scale exponent:

$$
\boxed{
\frac3{2k+3}
}
$$

is smaller.

This is the fixed-order scaling gap.

C5-G is not re-proving Theorem 3.7.

What we add is:

$$
\boxed{
\text{actual }L^2\text{ derivative concentration}
}
$$

as a direct volume estimate for the selected high-set.

---

# 3. Grujić–Xu 2024 — Theorem 3.14

The main asymptotic-critical theorem uses:

$$
\boxed{
\rho
\lesssim
\|D^ku\|_\infty^{-1/(k+1)}
}
$$

the velocity chain scale,

and requires:

- derivative-chain hypotheses;
- later analytic time;
- theorem constants;
- all $k\ge\ell$ structure.

The C5-G fixed-order direct route only uses:

$$
\boxed{
\textbf{Theorem 3.5}.
}
$$

We do not mix Theorem 3.14 into the fixed-order closure.

---

# 4. Fixed derivative quantities

Fix:

$$
k\ge1.
$$

At a pre-singular smooth time:

$$
s<T^\ast,
$$

define:

$$
\boxed{
A_k(s)
=
\|D^ku(s)\|_\infty,
}
$$

$$
\boxed{
L_k(s)
=
\|D^ku(s)\|_2.
}
$$

Hereafter, we omit:

$$
s
$$

if there is no confusion.

---

# 5. Selected component/sign high set

For any multi-index:

$$
|\zeta|=k,
$$

component:

$$
i,
$$

sign:

$$
\pm,
$$

define:

$$
\boxed{
V_{\lambda,k}^{\zeta,i,\pm}
=
\{
x:
(D^\zeta u_i)^\pm(x)
>
\lambda A_k
\}.
}
$$

Theorem 3.5 selects at each:

$$
x_0
$$

a:

$$
(\zeta,i,\pm)
$$

corresponding to the local maximal component/sign.

The volume bound of C5-G holds:

$$
\boxed{
\textbf{uniformly for all components/signs}.
}
$$

---

# 6. C5-G.1: Direct Component-Volume Bound

By Chebyshev's inequality:

$$
\lambda^2
A_k^2
|
V_{\lambda,k}^{\zeta,i,\pm}
|
\le
\int
|D^\zeta u_i|^2dx.
$$

Therefore:

$$
\boxed{
|
V_{\lambda,k}^{\zeta,i,\pm}
|
\le
\lambda^{-2}
\frac{
L_k^2
}{
A_k^2
}.
}
$$

### Key Point

There is no:

- strain/rotation decomposition;
- shell conversion;
- component selection issue.

---

# 7. Global-volume to 1D-line sparseness

We adopt the C3-W pure geometric lemma.

If a measurable:

$$
E\subset\mathbb R^3
$$

satisfies:

$$
|E|
<
c_3
\delta^3
r^3,
$$

then for any spatial base point:

$$
x_0,
$$

there exists a line direction:

$$
d=d(x_0)
$$

such that:

$$
E
$$

from:

$$
x_0-rd
\quad\text{to}\quad
x_0+rd
$$

has a one-dimensional occupancy:

$$
\le
\delta.
$$

---

# 8. Fixed-order effective-volume scale

Define:

$$
\boxed{
V_{k}^{eff}
=
\frac{
L_k^2
}{
A_k^2
}.
}
$$

with the dimension of volume.

After fixing the theorem pair:

$$
(\lambda,\delta)
$$

,

define:

$$
\boxed{
r_{vol,k}
=
C_{\lambda,\delta}
\left(
V_k^{eff}
\right)^{1/3}
=
C_{\lambda,\delta}
L_k^{2/3}
A_k^{-2/3}.
}
$$

---

# 9. C5-G.2: Uniform Component/Sign 1D Sparseness

For any:

$$
x_0,
$$

and the Theorem 3.5 selected:

$$
(\zeta,i,\pm),
$$

the superlevel set:

$$
V_{\lambda,k}^{\zeta,i,\pm}
$$

at scale:

$$
\boxed{
r_{vol,k}
}
$$

is 1D $\delta$-sparse around:

$$
x_0.
$$

### Proof

C5-G.1 gives the global volume bound.

Choose:

$$
r_{vol,k}
$$

such that:

$$
|V|
\le
c_3\delta^3r_{vol,k}^3.
$$

Apply the volume-to-line lemma. $\square$

---

# 10. Published direct target scale

Define:

$$
\boxed{
r_{GX,k}
=
\frac1{
2^k
c_{GX,k}
A_k^{3/(2k+3)}
},
}
$$

where:

$$
c_{GX,k}
=
c(M,\|u_0\|_2)
$$

represents the fixed theorem constant of Theorem 3.5.

---

# 11. Direct gate ratio

Define:

$$
\boxed{
\mathfrak G_k^{dir}
=
\frac{
r_{vol,k}
}{
r_{GX,k}
}.
}
$$

That is:

$$
\boxed{
\mathfrak G_k^{dir}
=
C_{\lambda,\delta}
2^k
c_{GX,k}
L_k^{2/3}
A_k^{-\frac23+\frac3{2k+3}}.
}
$$

Since:

$$
-\frac23
+
\frac3{2k+3}
=
-
\frac{
4k-3
}{
3(2k+3)
},
$$

Therefore:

$$
\boxed{
\mathfrak G_k^{dir}
=
C_{\lambda,\delta}
2^k
c_{GX,k}
L_k^{2/3}
A_k^{-\frac{4k-3}{3(2k+3)}}.
}
$$

---

# 12. C5-G.3: Fixed-Order Direct Gate Closure Theorem

## Theorem 12.1

Let:

$$
t
$$

be the:

$$
D^ku
$$

escape time in the sense of Theorem 3.5.

If there exists a theorem-admissible:

$$
s=s(t)
$$

such that:

$$
\boxed{
\mathfrak G_k^{dir}(s)
\le1,
}
$$

then the spatial condition in the hypotheses of Theorem 3.5 holds,

therefore:

$$
\boxed{
T^\ast
\text{ is not a blow-up time}.
}
$$

### Proof

By C5-G.2:

the selected component/sign superlevel set is 1D sparse at:

$$
r_{vol,k}
$$

.

If:

$$
r_{vol,k}\le r_{GX,k},
$$

taking:

$$
\rho=r_{vol,k}
$$

satisfies the published theorem scale bound. $\square$

---

# 13. Equivalent effective-volume condition

Cubing:

$$
r_{vol,k}
\le
r_{GX,k}
$$

is equivalent to:

$$
\boxed{
V_k^{eff}
\le
C_{k,\lambda,\delta,GX}
A_k^{-9/(2k+3)}.
}
$$

Since:

$$
V_k^{eff}=L_k^2/A_k^2,
$$

it can be written as:

$$
\boxed{
L_k^2
\le
C_{k,\lambda,\delta,GX}
A_k^{\frac{4k-3}{2k+3}}.
}
$$

### Important

The constants retain the dependence on Theorem 3.5's:

- $M$;
- $\|u_0\|_2$;
- $\lambda,\delta$;
- $k$;

.

We do not silently set them to $1$.

---

# 14. k=1 exact form

For:

$$
k=1,
$$

$$
\boxed{
\frac{
4k-3
}{
2k+3
}
=
\frac15.
}
$$

so the fixed-$k=1$ direct gate condition is:

$$
\boxed{
\|Du(s)\|_2^2
\le
C_{GX,1}
\|Du(s)\|_\infty^{1/5}.
}
$$

equivalently:

$$
\boxed{
\|Du(s)\|_\infty
\ge
C'_{GX,1}
\|Du(s)\|_2^{10}.
}
$$

with theorem constants included.

---

# 15. Strain form of k=1 gate

For a whole-space divergence-free smooth:

$$
u,
$$

we have:

$$
\boxed{
\|Du\|_2^2
=
\|\omega\|_2^2
=
2
\|S\|_2^2.
}
$$

Therefore:

$$
\boxed{
\|S(s)\|_2^2
\le
C
\|Du(s)\|_\infty^{1/5}
}
$$

at an admissible Theorem 3.5 later time,

is sufficient to close the fixed-$k=1$ gate.

### Interpretation

This is a:

$$
\boxed{
\textbf{raw-gradient peak vs strain-enstrophy concentration gate}.
}
$$

---

# 16. What happened to COMPSIGN?

The C5-A derivative defect:

$$
\mathrm{COMPSIGN}
$$

originally meant:

> We only have magnitude geometry,
> but the theorem requires component/sign geometry.

The C5-G direct-volume route directly applies a volume bound to the:

$$
(D^\zeta u_i)^\pm
$$

superlevel set.

Therefore, in the:

$$
\boxed{
\text{C5-G direct-volume gate}
}
$$

,

$$
\boxed{
\mathrm{COMPSIGN}
}
$$

is no longer an independent defect.

---

# 17. What happened to SHELLFULL?

Early C5-H had a shell/full derivative conversion issue.

C5-G now completely avoids using:

$$
u_q.
$$

It directly estimates the:

$$
\boxed{
D^ku
}
$$

full field.

Therefore:

$$
\boxed{
\mathrm{SHELLFULL}
}
$$

is also no longer an independent defect for the fixed-$k$ direct route.

---

# 18. What remains at fixed k?

Thus, the only genuine residuals for the fixed Theorem 3.5 route are:

## G-KMULT — Effective-volume / multiplicity defect

At all theorem-admissible later times:

$$
\boxed{
\mathfrak G_k^{dir}>1.
}
$$

That is, the:

$$
D^ku
$$

$L^2$ mass is too diffuse relative to the $L^\infty$ peak.

## G-KTIME — Later-time defect

The theorem interval after the escape-time consistently fails to align with the favorable geometry/amplitude window.

### Fixed-$k$ direct defect family

$$
\boxed{
\mathfrak D_k^{dir}
=
\{
\mathrm{MULT},
\mathrm{TIME}
\}.
}
$$

---

# 19. Relation to Theorem 3.7

Theorem 3.7 uses only kinetic energy / negative Sobolev control,

to obtain:

$$
r_{apr,k}
\sim
A_k^{-2/(2k+3)}.
$$

C5-G uses the actual:

$$
L_k/A_k
$$

effective volume,

to obtain:

$$
r_{vol,k}
\sim
L_k^{2/3}A_k^{-2/3}.
$$

If the derivative field is highly concentrated,

$$
r_{vol,k}
$$

can be smaller than:

$$
r_{GX,k}
\sim
A_k^{-3/(2k+3)},
$$

directly closing the gate.

Therefore, C5-G is measuring:

$$
\boxed{
\textbf{whether the fixed-order derivative concentration is sufficient to cross the scaling gap}.
}
$$

---

# 20. General fixed-order concentration index

Define:

$$
\boxed{
\mathfrak C_k^{eff}
=
\frac{
L_k^2
}{
A_k^{(4k-3)/(2k+3)}
}.
}
$$

Under a fixed theorem normalization,

the gate condition is simply:

$$
\boxed{
\mathfrak C_k^{eff}
\le
C_{GX,k}.
}
$$

### Guard

$\mathfrak C_k^{eff}$ alone is not a universal scale-invariant scalar;

it must be interpreted alongside:

$$
C_{GX,k}
$$

and NS scaling metadata.

The truly dimensionless object remains:

$$
\boxed{
\mathfrak G_k^{dir}
=
r_{vol,k}/r_{GX,k}.
}
$$

---

# 21. Fixed-order recurrent survivor

If a hypothetical blow-up exists,

then for any recurrent fixed:

$$
k
$$

direct route,

every relevant escape time:

$$
t
$$

must satisfy:

$$
\boxed{
\mathfrak G_k^{dir}(s)>1
}
$$

for all theorem-admissible:

$$
s
$$

or the favorable time does not fall within the theorem window.

Otherwise, Theorem 3.5 directly excludes:

$$
T^\ast.
$$

---

# 22. Derivative-order escalation update

C5-F:

$$
k_j^{best}=k_\ast
$$

or:

$$
k_j^{best}\to\infty.
$$

C5-G now goes further:

If a fixed:

$$
k_\ast
$$

is recurrent,

its direct defect is already compressed into:

$$
\boxed{
\mathrm{MULT}
\vee
\mathrm{TIME}.
}
$$

So if in the future we can, for each fixed:

$$
k
$$

exclude:

- effective-volume diffuseness;
- later-time mismatch;

only then is it legitimate to genuinely force the survivor route towards:

$$
\boxed{
k\to\infty.
}
$$

---

# 23. Pressure signature state

Returning to the C5-F common far-pressure matrix:

$$
\boxed{
F\in\operatorname{Sym}_0(3).
}
$$

If:

$$
F\ne0,
$$

normalize:

$$
\boxed{
\widehat F
=
\frac{
F
}{
|F|_F
}
\in
S^4\cap\operatorname{Sym}_0(3).
}
$$

---

# 24. Signature regions

Define:

$$
\boxed{
\mathcal S_{1-}
=
\{
\widehat F:
\operatorname{sig}F=(-,+,+)
\},
}
$$

$$
\boxed{
\mathcal S_{2-}
=
\{
\widehat F:
\operatorname{sig}F=(-,-,+)
\}.
}
$$

Both are open subsets.

Their common boundary is:

$$
\boxed{
\Sigma_P
=
\{
\widehat F:
\det F=0
\}.
}
$$

---

# 25. Signature defect distance

Define:

$$
\boxed{
d_{\rm sig}(F)
=
\operatorname{dist}
\left(
\widehat F,
\Sigma_P
\right).
}
$$

If:

$$
F=0,
$$

let:

$$
d_{\rm sig}=0.
$$

Therefore:

$$
\boxed{
d_{\rm sig}\in[0,1]
}
$$

is a compact pressure-signature metadata.

---

# 26. C5-G.4: Opposite Signature Matrices Must Cross the Boundary

If:

$$
F_0,F_1\in\operatorname{Sym}_0(3)
$$

is nonzero,

and the signatures:

$$
(-,+,+)
$$

and:

$$
(-,-,+)
$$

are different,

then the line segment:

$$
F(\theta)
=
(1-\theta)F_0+\theta F_1
$$

contains a:

$$
\theta_\ast\in(0,1)
$$

such that:

$$
\boxed{
\det F(\theta_\ast)=0.
}
$$

### Proof

$$
\det F_0<0,
$$

$$
\det F_1>0,
$$

and the determinant is continuous. $\square$

---

# 27. Signature switching + heredity

The far-pressure heredity framework of C3-U gives that:

$$
F_{j+1}-F_j
$$

can be controlled by:

- spatial motion;
- temporal turnover;
- source reclassification;

these three classes of defects.

If along a selected recurrent branch:

$$
\boxed{
\frac{
\|F_{j+1}-F_j\|
}{
\|F_j\|
}
\to0,
}
$$

we call it:

$$
\boxed{
\textbf{strong far-matrix heredity}.
}
$$

---

# 28. C5-G.5: Signature Switching Rigidity

Assume:

1. strong far-matrix heredity;
2. signatures recurrently switch between:
   $$
   (-,+,+)
   $$
   and:
   $$
   (-,-,+)
   $$
   .

Then along the switching subsequence:

$$
\boxed{
d_{\rm sig}(F_j)\to0.
}
$$

### Proof

For each opposite-signature pair:

$$
F_j,F_{j+1},
$$

there exists a singular:

$$
F_j^\ast.
$$

Therefore:

$$
\operatorname{dist}
(
F_j,
\{\det=0\}
)
\le
\|F_j-F_j^\ast\|
\le
\|F_{j+1}-F_j\|.
$$

Divide by:

$$
\|F_j\|
$$

and use heredity. $\square$

---

# 29. Pressure-signature trichotomy

Thus, a recurrent common far-pressure branch can only:

## G-PFIX

$$
\boxed{
\text{signature eventually fixed};
}
$$

or:

## G-PBOUND

$$
\boxed{
d_{\rm sig}(F_j)\to0;
}
$$

or:

## G-PTURN

$$
\boxed{
\|F_{j+1}-F_j\|/\|F_j\|
\not\to0
}
$$

That is:

- pressure turnover;
- source reclassification;
- spatial/far-field fragmentation.

---

# 30. Relation to C5-F axis locking

If the signature is fixed at:

$$
(-,+,+),
$$

the C5-F strong pressure margin can lock:

$$
e_1
$$

into one projective cap,

and conflict with nondegenerate-gap Q cancellation.

If the signature is fixed at:

$$
(-,-,+),
$$

it still retains the negative-plane belt geometry.

If:

$$
d_{\rm sig}\to0,
$$

the pressure matrix approaches the one-zero-eigenvalue boundary,

forming a:

$$
\boxed{
\textbf{Pressure Spectral-Gap Defect}.
}
$$

Therefore, the "signature degeneration" of C5-F is now formally compactified.

---

# 31. Middle-gap and pressure signature remain distinct

C5-F has proven:

the middle gap:

$$
\vartheta\to0
$$

will not erase the compressive axis.

C5-G now shows:

the pressure signature gap:

$$
d_{\rm sig}\to0
$$

is a far-pressure matrix eigenvalue degeneration.

The two are distinct compact boundaries:

$$
\boxed{
\text{Strain Middle-Gap}
\neq
\text{Pressure Signature-Gap}.
}
$$

The C5 state must preserve both simultaneously.

---

# 32. Pressure Poisson identity

For incompressible:

$$
u,
$$

$$
-\Delta p
=
\partial_i u_j
\partial_j u_i.
$$

Using:

$$
\nabla u=S+\Omega,
$$

$$
|\Omega|^2
=
\frac12
|\omega|^2,
$$

we have:

$$
\boxed{
-\Delta p
=
|S|^2
-
\frac12
|\omega|^2.
}
$$

Therefore:

$$
\boxed{
\Delta p
=
-|S|^2
+
\frac12
|\omega|^2.
}
$$

---

# 33. C5-E vorticity-dominant set

Recall:

$$
\boxed{
E_\omega(\eta)
=
\{
|S|^2
<
\eta|Q|
\}.
}
$$

and:

$$
\boxed{
|Q|
\le
|S|^2
+
c_\omega
|\omega|^2,
\qquad
c_\omega
=
\frac{\sqrt2}{4}.
}
$$

Therefore, in:

$$
E_\omega(\eta),
$$

$$
(1-\eta)|S|^2
<
\eta c_\omega|\omega|^2.
$$

That is:

$$
\boxed{
|S|^2
<
r_\eta
|\omega|^2,
\qquad
r_\eta
=
\frac{
\eta c_\omega
}{
1-\eta
}.
}
$$

---

# 34. C5-G.6: Vorticity-Dominant Leakage Forces Positive Pressure Laplacian

If:

$$
\boxed{
r_\eta<\frac12,
}
$$

for example:

$$
\eta\le\frac14,
$$

then in:

$$
E_\omega(\eta)
$$

pointwise:

$$
\boxed{
\Delta p
\ge
\left(
\frac12-r_\eta
\right)
|\omega|^2
>0.
}
$$

### Conclusion

$$
\boxed{
\textbf{Vorticity-Dominant Leakage}
\Rightarrow
\textbf{Positive Pressure-Poisson Curvature}
}
$$

on the same spatial set.

---

# 35. Critical pressure-Poisson stock

If the C5-E branch gives:

$$
\boxed{
\frac{
R
}{
\nu^2
}
\int_{E_\omega}
\chi|\omega|^2dx
\ge
w_0,
}
$$

then:

$$
\boxed{
\frac{
R
}{
\nu^2
}
\int
\chi
(\Delta p)_+
dx
\ge
c_\eta
w_0.
}
$$

This document calls this:

$$
\boxed{
\textbf{Pressure-Poisson Re-entry Certificate}.
}
$$

---

# 36. Why this is not yet $L^{3/2}$ pressure concentration

A large:

$$
\int
(\Delta p)_+
$$

does not by itself lower-bound:

$$
\inf_{\ell\in\mathcal A_1}
\|p-\ell\|_{3/2}
$$

without controlling:

- negative $\Delta p$ outside the leakage set;
- spatial oscillation scale;
- sign-coherent cutoff geometry.

Therefore:

$$
\boxed{
\text{Pressure-Poisson Re-entry}
}
$$

is a pressure-curvature synchronization,

not an automatic replacement for the C4-I pressure-oscillation theorem.

---

# 37. Strain-space orthogonal complement

Let:

$$
P_{st}
$$

be the:

$$
L^2
$$

orthogonal projection of symmetric-matrix fields onto the strain constraint space,

such as the Miller–Sawyer Helmholtz-type decomposition.

Define:

$$
\boxed{
P_{st}^{\perp}
=
I-P_{st}.
}
$$

---

# 38. Raw strain nonlinearity

The full strain equation is:

$$
\partial_tS
+
(u\cdot\nabla)S
-
\nu\Delta S
+
S^2
+
\frac14
(
\omega\otimes\omega
-
|\omega|^2I
)
+
\nabla^2p
=
0.
$$

Define:

$$
\boxed{
\mathcal A
=
(u\cdot\nabla)S,
}
$$

$$
\boxed{
\mathcal S
=
S^2,
}
$$

$$
\boxed{
\mathcal W
=
\frac14
(
\omega\otimes\omega
-
|\omega|^2I
).
}
$$

---

# 39. Exact constraint-complement pressure ledger

Since:

$$
\partial_tS-\nu\Delta S
$$

remains in the strain constraint space,

apply:

$$
P_{st}^{\perp}.
$$

to obtain:

$$
\boxed{
\nabla^2p
=
-
P_{st}^{\perp}
(
\mathcal A+\mathcal S+\mathcal W
).
}
$$

Define:

$$
\boxed{
C_A
=
P_{st}^{\perp}\mathcal A,
}
$$

$$
\boxed{
C_S
=
P_{st}^{\perp}\mathcal S,
}
$$

$$
\boxed{
C_\omega
=
P_{st}^{\perp}\mathcal W.
}
$$

Then:

$$
\boxed{
\nabla^2p
=
-
(
C_A+C_S+C_\omega
).
}
$$

---

# 40. C5-G.7: Vorticity-Complement Re-entry Trichotomy

If:

$$
\boxed{
\|C_\omega\|_2
\ge
c_0,
}
$$

then at least:

## G-CP

$$
\boxed{
\|\nabla^2p\|_2
\ge
c_0/3,
}
$$

or:

## G-CA

$$
\boxed{
\|C_A\|_2
\ge
c_0/3,
}
$$

or:

## G-CS

$$
\boxed{
\|C_S\|_2
\ge
c_0/3.
}
$$

up to harmless split constants.

### Conclusion

$$
\boxed{
\textbf{Vorticity Constraint-Complement Congestion}
}
$$

cannot exist in isolation.

It must synchronize with:

$$
\boxed{
\text{Actual Pressure Hessian}
\vee
\text{Advection Constraint Complement}
\vee
\text{Strain-Square Constraint Complement}.
}
$$

---

# 41. Two pressure re-entry mechanisms

C5-G now has two distinct pressure re-entry mechanisms:

## Trace / Poisson channel

vorticity-dominant physical set:

$$
\boxed{
\Delta p>0.
}
$$

## Constraint-complement channel

large:

$$
C_\omega
$$

forces:

$$
\boxed{
\nabla^2p
\vee
C_A
\vee
C_S.
}
$$

The two cannot be conflated into a single scalar pressure quantity.

---

# 42. Fixed k=1 now bypasses vorticity field conversion

C5-F previously split the raw:

$$
Du
$$

high set into the:

$$
S
$$

high set and the:

$$
\omega
$$

high set.

This is a useful spatial provenance.

But the C5-G fixed-$k=1$ direct gate applies a global volume bound directly to the:

$$
Du
$$

component/sign high set itself.

Therefore:

$$
\boxed{
\textbf{Theorem 3.5 spatial gate no longer needs vorticity-field conversion}.
}
$$

Vorticity geometry remains important for:

- Q cancellation;
- pressure;
- operator;

but it is no longer a necessary obstacle for fixed-$k=1$ component/sign conversion.

---

# 43. k=1 direct gate ratio in strain variables

Since:

$$
L_1^2
=
2\|S\|_2^2,
$$

$$
A_1
=
\|Du\|_\infty,
$$

Therefore:

$$
\boxed{
\mathfrak G_1^{dir}
=
C_{GX}
\|S\|_2^{2/3}
\|Du\|_\infty^{-1/15}.
}
$$

up to fixed theorem constants.

### Important

The exponent:

$$
1/15
$$

is very small.

So the k=1 direct closure requires:

$$
\boxed{
\textbf{very strong peak concentration relative to enstrophy}.
}
$$

This explains why k=1, although theorem-ready,

may still be a difficult gate.

---

# 44. k=2 direct gate ratio

$$
\boxed{
\mathfrak G_2^{dir}
=
C_{GX,2}
\|D^2u\|_2^{2/3}
\|D^2u\|_\infty^{-5/21}.
}
$$

Since:

$$
\frac{
4k-3
}{
3(2k+3)
}
=
\frac5{21}
$$

at:

$$
k=2.
$$

C5-E/F can provide:

- $D^2u$ amplitude lower bound;
- $\nabla S$ stock;

but the gate still depends on whether the amplitude is sufficiently concentrated relative to the $L^2$ mass.

---

# 45. General fixed-k behavior

The amplitude exponent in:

$$
\mathfrak G_k^{dir}
$$

is:

$$
\boxed{
\frac{
4k-3
}{
3(2k+3)
}
}
$$

which increases:

$$
\frac1{15},
\frac5{21},
\ldots
\to
\frac23.
$$

So purely at this effective-volume formula level:

$$
\boxed{
\text{higher derivative peak concentration
has stronger leverage against fixed-}k\text{ direct gap}.
}
$$

But:

$$
L_k
$$

may also rapidly grow.

So it is still not an automatic escalation closure.

---

# 46. Fixed-order direct defect state

For each:

$$
k,
$$

define:

$$
\boxed{
\Theta_k^{dir}
=
\left\langle
\mathfrak G_k^{dir},
\mathsf T_k
\right\rangle,
}
$$

where:

$$
\mathsf T_k
\in\{0,1\}
$$

indicates whether the theorem later-time gate is aligned.

A hypothetical survivor at fixed:

$$
k
$$

must recurrently satisfy:

$$
\boxed{
\mathfrak G_k^{dir}>1
}
$$

or:

$$
\boxed{
\mathsf T_k=0.
}
$$

---

# 47. Direct gate removes two old labels

For the Theorem 3.5 route:

$$
\boxed{
\mathrm{SHELLFULL},
\mathrm{COMPSIGN}
}
$$

have been bypassed by the full-field component-volume route.

So the C5-A derivative defect vector can be updated for the fixed direct route:

$$
\boxed{
d_k^{dir}
=
(
\mathrm{MULT},
\mathrm{TIME}
).
}
$$

### Chain route separate

Theorem 3.14 still has:

- chain;
- all-order synchronization;
- later analytic timing;

as additional hypotheses.

Therefore:

$$
\boxed{
\text{TIMECHAIN}
}
$$

remains in the chain-assisted route.

---

# 48. Fixed-order closure audit

For any fixed:

$$
k,
$$

if there exists a subsequence in the recurrent escape time sequence,

where each generation has an admissible:

$$
s_j
$$

and:

$$
\boxed{
\limsup_j
\mathfrak G_k^{dir}(s_j)
\le1,
}
$$

then for sufficiently large:

$$
j
$$

the Theorem 3.5 spatial gate closes,

contradicting:

$$
T^\ast
$$

being the first blow-up time.

So a fixed-order survivor must maintain:

$$
\boxed{
\liminf
\mathfrak G_k^{dir}>1
}
$$

along all admissible favorable subsequences,

or consistently exhibit a time-mismatch.

---

# 49. Pressure-signature defect state

The C5-F axis-pressure metadata is updated to:

$$
\boxed{
\Theta_\ast^P
=
\left\langle
\widehat F_\ast,
\operatorname{sig}F_\ast,
d_{\rm sig,\ast},
c_\ast^P,
\nu_\ast^{axis},
\mathsf H_\ast^P
\right\rangle.
}
$$

Where:

- $d_{\rm sig}$ = distance to det-zero boundary;
- $c^P$ = pressure-axis margin;
- $\mathsf H^P$ = far-matrix heredity status.

---

# 50. Vorticity-pressure defect state

Define:

$$
\boxed{
\Theta_\ast^{V/P}
=
\left\langle
\mathfrak W_\ast,
\mathfrak P_{\Delta,+},
\|C_\omega\|,
\|\nabla^2p\|,
\|C_A\|,
\|C_S\|
\right\rangle.
}
$$

It preserves:

- vorticity leakage stock;
- positive pressure-Poisson curvature;
- vorticity constraint complement;
- actual pressure Hessian;
- competing complement channels.

---

# 51. C5-G residual compression

C5-F residual:

$$
\text{Pressure Signature}
\vee
\text{Vorticity Complement}
\vee
\text{Fixed-Order Gate}
\vee
k\to\infty.
$$

After C5-G:

## Pressure signature

$$
\boxed{
\text{Fixed Signature}
\vee
\text{Signature-Boundary Defect}
\vee
\text{Pressure Turnover/Fragmentation}.
}
$$

## Vorticity complement

$$
\boxed{
\text{Pressure-Poisson Activity}
+
\left(
\text{Pressure Hessian}
\vee
\text{Advection Complement}
\vee
\text{Strain-Square Complement}
\right).
}
$$

## Fixed order

$$
\boxed{
\text{Effective-Volume Defect}
\vee
\text{Later-Time Defect}.
}
$$

---

# 52. What is now genuinely theorem-ready?

The following statement is no longer a pre-gate:

> At a Grujić–Xu Theorem 3.5 admissible later time $s$,
> if:
> $$
> \mathfrak G_k^{dir}(s)\le1,
> $$
> then regularity follows past $T^\ast$.

This uses exactly:

- full $D^ku$;
- selected component/sign superlevel sets;
- 1D sparseness;
- published theorem scale;
- theorem later-time window.

Therefore:

$$
\boxed{
\textbf{C5-G has a genuine theorem-ready fixed-order closure interface}.
}
$$

---

# 53. What remains non-theorem-ready?

The middle-gap strain active volume:

$$
E_c(S)
$$

itself is still not a Theorem 3.5 superlevel set.

The vorticity pressure-Poisson stock is also not a Grujić–Xu gate.

Pressure axis geometry is also not a standalone regularity theorem.

So C5-G only claims:

$$
\boxed{
\textbf{one direct fixed-order route is theorem-ready}.
}
$$

---

# 54. Can k=1 now solve the route?

Not yet.

A hypothetical survivor can keep:

$$
\boxed{
\mathfrak G_1^{dir}>1
}
$$

by making:

$$
\|S\|_2
$$

grow sufficiently rapidly relative to:

$$
\|Du\|_\infty.
$$

This is the:

$$
\boxed{
\textbf{Diffuse-Enstrophy / Insufficient-Peak-Concentration Defect}.
}
$$

No existing finite budget excludes this near a hypothetical blow-up.

---

# 55. Can fixed k=2 solve the route?

Not yet.

C5-F gives critical:

$$
D^2u
$$

amplitude somewhere,

but the $L^2$ derivative stock can grow comparably or faster,

keeping:

$$
\mathfrak G_2^{dir}>1.
$$

Therefore:

$$
\boxed{
\text{amplitude stock}
\neq
\text{effective-volume concentration}.
}
$$

remains the core distinction.

---

# 56. Derivative escalation logic after C5-G

For fixed:

$$
k,
$$

the survivor defect is only:

$$
\mathrm{MULT}
\vee
\mathrm{TIME}.
$$

Thus the entire C5 derivative route can be written as:

$$
\boxed{
\text{some fixed }k\text{ closes}
}
$$

or:

$$
\boxed{
\forall\text{ fixed }k,
\quad
\mathrm{MULT}_k
\vee
\mathrm{TIME}_k
\text{ recurrent}.
}
$$

Only in the second case,

do we then study whether:

$$
\boxed{
k\to\infty
}
$$

can compress these defects into incompatibility.

---

# 57. Relation to asymptotic criticality

The scale of Grujić–Xu Theorem 3.14:

$$
\|D^ku\|_\infty^{-1/(k+1)}
$$

and the gap with the a-priori scale vanish as:

$$
k\to\infty
$$

.

But C5-G reveals another dimension:

$$
\boxed{
\textbf{effective derivative volume}
}
$$

must also be compatible.

So if high-$k$ asymptotic criticality is to genuinely close the C5 survivor,

we must also study whether:

$$
\boxed{
\mathfrak G_k^{dir},
\quad
\mathrm{MULT}_k,
\quad
\mathrm{TIMECHAIN}_k
}
$$

can simultaneously maintain failure as:

$$
k\to\infty
$$

.

---

# 58. Major no-go audit

### NG-G1

$$
\text{middle-gap strain sparseness}
\Rightarrow
\text{Theorem 3.5}.
$$

FALSE by itself.

### NG-G2

$$
\text{component/sign conversion remains an unavoidable fixed-}k\text{ defect}.
$$

FALSE for the C5-G direct-volume route.

### NG-G3

$$
\text{shell/full conversion remains unavoidable}.
$$

FALSE for the C5-G direct-volume route.

### NG-G4

$$
\text{vorticity-dominant leakage}
\Rightarrow
L^{3/2}\text{ pressure concentration}.
$$

NOT PROVED.

It gives pressure-Poisson curvature first.

### NG-G5

$$
P_{st}^{\perp}(\omega\otimes\omega)
=
\nabla^2p.
$$

FALSE.

### NG-G6

$$
\text{pressure signature switching}
\Rightarrow
\det F\to0.
$$

Only under strong hereditary closeness.

Otherwise pressure turnover/fragmentation is legal.

### NG-G7

$$
\text{fixed-order direct defect failure}
\Rightarrow
k\to\infty.
$$

FALSE unless all fixed-order recurrent defects are excluded.

---

# 59. X-Integration Guards Update

## G-DIRECTFULL

The fixed-order direct gate prioritizes using the full:

$$
D^ku
$$

component/sign high set,

avoiding unnecessary shell/strain conversion.

## G-EFFVOLK

Preserve:

$$
V_k^{eff}
=
\|D^ku\|_2^2/\|D^ku\|_\infty^2.
$$

## G-GXRATIO

The theorem-ready gate preserves:

$$
\mathfrak G_k^{dir}
=
r_{vol,k}/r_{GX,k}.
$$

## G-GXTIME

$\mathfrak G_k^{dir}\le1$ can only close the gate at a Theorem 3.5 admissible later time.

## G-PSIGBOUND

Signature switching can only deduce the det-zero boundary when combined with heredity closeness.

## G-PPOIS

Vorticity-dominant leakage first records:

$$
(\Delta p)_+
$$

rather than direct $L^{3/2}$ pressure.

## G-PCOMPLEDGER

The vorticity constraint complement must be ledgered together with the actual pressure / advection / $S^2$ complement.

---

# 60. True ETN Update

C5-G derivative state:

$$
\boxed{
\Theta_\ast^{DG}
=
\left\langle
k,
A_k,
L_k,
V_k^{eff},
r_{vol,k},
r_{GX,k},
\mathfrak G_k^{dir},
\mathsf T_k
\right\rangle.
}
$$

pressure state:

$$
\boxed{
\Theta_\ast^{PS}
=
\left\langle
\widehat F,
\operatorname{sig}F,
d_{\rm sig},
\mathsf H^P,
\nu^{axis}
\right\rangle.
}
$$

vorticity-pressure state:

$$
\boxed{
\Theta_\ast^{VP}
=
\left\langle
\mathfrak W_R,
\mathfrak P_{\Delta,+},
C_\omega,
\nabla^2p,
C_A,
C_S
\right\rangle.
}
$$

---

# 61. C5 strategic status

C5-A:

$$
\text{motif compactness}.
$$

C5-B:

$$
\text{temporal oscillation/concentration}.
$$

C5-C:

$$
\text{temporal transition curvature}.
$$

C5-D:

$$
\text{first spatial–matrix incompatibility}.
$$

C5-E:

$$
Q\to\text{gap/derivative/vorticity defects}.
$$

C5-F:

$$
\text{axis/pressure signature + derivative escalation}.
$$

C5-G:

$$
\boxed{
\textbf{fixed-order direct derivative gate becomes theorem-ready};
}
$$

Meanwhile:

$$
\boxed{
\textbf{pressure signature and vorticity complement become compact,
routed defects rather than free escapes}.
}
$$

---

# 62. What remains most important

The fixed-order problem truly worth tackling now is no longer how the geometry transforms:

but rather:

$$
\boxed{
\textbf{Can a hypothetical blow-up keep }
\mathfrak G_k^{dir}>1
\textbf{ for every fixed }k
\textbf{ at every admissible later time?}
}
$$

This is the:

$$
\boxed{
\textbf{All-Order Effective-Volume Defect Problem}.
}
$$

If the answer is no,

some fixed $k$ direct gate closes.

If the answer is yes,

then the survivor must maintain at all derivative levels:

$$
\boxed{
\text{L}^2\text{ derivative mass sufficiently diffuse relative to peaks}.
}
$$

This is already a highly structured all-order constraint.

---

# 63. New Frontier: C5-H

The formal next topic:

$$
\boxed{
\textbf{C5-H — All-Order Effective-Volume Defects,
Derivative Concentration Ladders, and Asymptotic-Critical Compatibility}.
}
$$

---

# 64. C5-H proof obligations

## H1 — All-order direct gate ratios

Study the relation of:

$$
\boxed{
\mathfrak G_k^{dir}
}
$$

with:

$$
k
$$

,

and whether all fixed $k$ can simultaneously maintain:

$$
>1.
$$

## H2 — Derivative interpolation

Use Gagliardo–Nirenberg / log-convexity to

couple:

$$
L_k,
\quad
A_k
$$

across derivative levels.

## H3 — Effective-volume ladder

Define:

$$
\boxed{
V_k^{eff}
=
L_k^2/A_k^2
}
$$

and study:

$$
V_{k+1}^{eff}/V_k^{eff}.
$$

## H4 — Fixed-order defect inheritance

If:

$$
\mathfrak G_k^{dir}>1
$$

and:

$$
\mathfrak G_{k+1}^{dir}>1,
$$

does it force a certain derivative-chain monotonicity / multiplicity structure?

## H5 — Time-gate synchronization

Can the Theorem 3.5 admissible later windows for different:

$$
k
$$

be jointly extracted along the C5 record ladder?

## H6 — Link to Theorem 3.14

If all fixed direct gates fail,

measure whether this itself generates the ascending/descending derivative chain required by Theorem 3.14.

## H7 — High-k compactification

For:

$$
k\to\infty,
$$

compactify:

$$
\mathfrak G_k^{dir},
\quad
V_k^{eff},
\quad
A_k^{1/(k+1)},
\quad
L_k^{1/k}.
$$

## H8 — Asymptotic compatibility contradiction

Search for an incompatibility between:

$$
\boxed{
\text{all-order diffuse derivative mass}
}
$$

and:

$$
\boxed{
\text{asymptotically-critical chain geometry}
}
$$

.

---

# 65. Formal Status

$$
\boxed{
\begin{aligned}
\text{component/sign global-volume bound}
&:\ \mathrm{PROVED},\\
\text{volume-to-line fixed-}k\text{ sparseness}
&:\ \mathrm{PROVED},\\
\mathfrak G_k^{dir}\le1
\text{ at admissible time}
\Rightarrow
\text{Theorem 3.5 closure}
&:\ \mathrm{PROVED},\\
\text{fixed-}k\ \mathrm{COMPSIGN}
&:\ \mathrm{BYPASSED},\\
\text{fixed-}k\ \mathrm{SHELLFULL}
&:\ \mathrm{BYPASSED},\\
\text{fixed-order residual}
&:\ \mathrm{MULT}\vee\mathrm{TIME},\\
\text{pressure signature boundary compactification}
&:\ \mathrm{DEFINED/PROVED},\\
\text{signature switching + heredity}
\Rightarrow
d_{\rm sig}\to0
&:\ \mathrm{PROVED},\\
\text{vorticity-dominant leakage}
\Rightarrow
(\Delta p)_+
&:\ \mathrm{PROVED},\\
\text{constraint-complement pressure ledger}
&:\ \mathrm{PROVED},\\
\text{vorticity complement trichotomy}
&:\ \mathrm{PROVED},\\
\text{all fixed }k\text{ direct gates cannot all fail}
&:\ \mathrm{OPEN},\\
\text{global regularity}
&:\ \mathrm{OPEN}.
\end{aligned}
}
$$

---

# 66. Conclusion

C5-F left:

$$
\text{Pressure Signature}
\vee
\text{Vorticity Complement}
\vee
\text{Fixed-Order Gate}
\vee
k\to\infty.
$$

C5-G now genuinely connects the fixed-order route to the published theorem.

For any:

$$
k\ge1,
$$

the selected:

$$
D^ku
$$

component/sign high set directly satisfies:

$$
\boxed{
|V_{\lambda,k}|
\lesssim
\frac{
\|D^ku\|_2^2
}{
\|D^ku\|_\infty^2
}.
}
$$

Therefore:

$$
\boxed{
r_{vol,k}
\lesssim
\|D^ku\|_2^{2/3}
\|D^ku\|_\infty^{-2/3}.
}
$$

While the published Theorem 3.5 direct target is:

$$
\boxed{
r_{GX,k}
=
\frac1{
2^kc(M)
\|D^ku\|_\infty^{3/(2k+3)}
}.
}
$$

Thus at a theorem-admissible later time:

$$
\boxed{
\mathfrak G_k^{dir}
=
r_{vol,k}/r_{GX,k}
\le1
}
$$

the gate genuinely closes.

This is not a pre-gate.

It is already a:

$$
\boxed{
\textbf{theorem-ready fixed-order closure}.
}
$$

So the old defects of the fixed direct route:

$$
\mathrm{SHELLFULL},
\quad
\mathrm{COMPSIGN}
$$

can be bypassed.

What genuinely remains is only:

$$
\boxed{
\text{Effective-Volume Diffuseness}
\vee
\text{Later-Time Mismatch}.
}
$$

Regarding pressure,

if the common far matrix signature repeatedly switches under strong heredity,

it must force:

$$
\boxed{
\det F\to0.
}
$$

Otherwise, it must pay for pressure turnover / source fragmentation.

Regarding vorticity,

dominant leakage directly gives:

$$
\boxed{
\Delta p>0
}
$$

on the same leakage set,

and the strain-space complement exactly satisfies:

$$
\boxed{
\nabla^2p
=
-
(
C_A+C_S+C_\omega
).
}
$$

So the vorticity complement must be:

$$
\boxed{
\text{Pressure Hessian}
\vee
\text{Advection Complement}
\vee
\text{Strain-Square Complement}.
}
$$

Therefore, the hardest new problem after C5-G is already very clear:

> **Can a hypothetical singular survivor,
> at all fixed derivative orders,
> keep the $L^2$ mass of $D^ku$ sufficiently diffuse relative to the $L^\infty$ peak,
> such that $\mathfrak G_k^{dir}>1$,
> while simultaneously evading every Theorem 3.5 admissible later time?**

The formal next paper:

$$
\boxed{
\textbf{C5-H — All-Order Effective-Volume Defects,
Derivative Concentration Ladders, and Asymptotic-Critical Compatibility}.
}
$$

---

# References

1. Z. Grujić, L. Xu, *Asymptotic Criticality of the Navier–Stokes Regularity Problem*, Journal of Mathematical Fluid Mechanics 26, Article 53 (2024), DOI: 10.1007/s00021-024-00888-x; arXiv:1911.00974.
2. E. Miller, E. Sawyer, *A Helmholtz-type decomposition for the space of symmetric matrices*, arXiv:2111.12891.
3. E. Miller, *On the interaction of strain and vorticity for solutions of the Navier–Stokes equation*, arXiv:2407.02691v2; Pure and Applied Analysis 8 (2026).
4. Z. Bradshaw, T.-P. Tsai, *On the local pressure expansion for the Navier–Stokes equations*, arXiv:2001.11526.
5. E. Miller, *A regularity criterion for the Navier–Stokes equation involving only the middle eigenvalue of the strain tensor*, arXiv:1710.05569.

# Internal dependencies

- `NS_C5F_AxisPressureSignature_DerivativeGateEscalation_v0.1.md`
- `NS_C5E_StrainDirection_MiddleGap_DerivativeIntermittency_v0.1.md`
- `NS_C5D_SpatialMatrix_StrongMiddleQuadraticPressureObstruction_v0.1.md`
- `NS_C5C_TemporalCorrelation_CrossCurvatureOrdering_v0.1.md`
- `NS_C5B_TemporalYoung_PulsePhaseCompatibility_v0.1.md`
- `NS_C5A_RecordWindow_MotifCompactness_v0.1.md`
- `NS_C4J_CompensationRigidity_FinalSynchronizationAudit_v0.1.md`
- `NS_C3U_PressureHeredity_MeanPointwiseRigidity_v0.1.md`
- `NS_C3Y_DerivativeChain_IntermittencyTradeoff_v0.1.md`
- `True ETN / Infinite-Dimensional Tension Field`
- `X_Integral_Unified_Program_v0.2.md`

Next:

$$
\boxed{
\textbf{C5-H — All-Order Effective-Volume Defects,
Derivative Concentration Ladders, and Asymptotic-Critical Compatibility}
}
$$