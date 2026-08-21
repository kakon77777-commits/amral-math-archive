# DCRP46 — Gauge-Flat Annular Scalar Moment, Signed Transport Gap, and the Flat-Extension / Transition Dichotomy

**Series:** Independent Navier–Stokes Research Series  
**Date:** 2026-08-17  
**Status:** Proof-development checkpoint / finite-annulus scalar-current round  
**Immediate predecessor:** `NS_DCRP45_CanonicalRay_AnnularSupplier_Compression_2026-08-17.md`

**Primary internal dependencies**
- DCRP-31 — finite-radius inward PFET matching layer
- DCRP-35 — finite-annulus strain/enstrophy supplier
- DCRP-36 — exact annular affine-jet reproduction equation
- DCRP-41 — fixed-plane zero-shape moving-pancake tensor
- DCRP-42 — planar shear scalar equation
- DCRP-44 — gauge-flat scalar-connection theorem
- DCRP-45 — canonical-ray compression of the annular supplier

**External calibration checked before this round**
- D. S. Agafontsev, E. A. Kuznetsov, A. A. Mailybaev, *Asymptotic solution for high vorticity regions in incompressible 3D Euler equations*, arXiv:1609.07782.
- G. Seregin, *On potential Type II blowups for the Navier-Stokes equations*, arXiv:2606.29468.

These sources confirm that pancake/shear + strain geometry is not by itself contradictory and that Type-II analysis remains tied to Euler-scale local limits and Liouville-type exclusions. No full Navier–Stokes regularity claim is made here.

---

# 0. Executive result

DCRP45 reduced the final fixed-plane zero-shape annular supplier from a five-dimensional symmetric trace-free affine jet to a one-dimensional canonical pancake amplitude.

The remaining question was whether the signed reproduction could be supplied entirely by internal annular vortex stretching, or whether a genuine finite-annulus transport carrier is unavoidable.

This round gives a sharper dichotomy.

Assume the final fixed-plane, zero-shape, gauge-flat scalar branch extends across the common finite supplier annulus. Then the canonical annular strain amplitude can be written as a gauge-invariant weighted moment of the planar shear scalar $q$:

$$
\boxed{
a_\psi(s)
=
\int H_\psi(y)\,q(y,s)\,dy,
}
$$

where $H_\psi$ is compactly supported in the same finite annulus and annihilates the residual gauge $q\mapsto q-g(z,s)$.

In the unique DCRP44 periodic canonical gauge,

$$
\boxed{
D_sq+k(s)q=0,
\qquad
k(s)=1-\gamma-2a(s).
}
$$

Therefore the weighted annular canonical amplitude satisfies the exact transport identity

$$
\boxed{
a_\psi'(s)+k(s)a_\psi(s)
=
\mathcal T_\psi(s),
}
$$

where

$$
\boxed{
\mathcal T_\psi(s)
=
\int
q
\left[
W\cdot\nabla H_\psi
+
3\gamma H_\psi
\right]dy,
\qquad
W=\gamma y+V.
}
$$

This is a finite-annulus canonical scalar-moment transport current.

On the exact aligned supplier branch

$$
a_\psi(s)=a(s),
$$

periodicity yields

$$
\boxed{
\int_0^{S_0}
\mathcal T_\psi(s)\,ds
=
\int_0^{S_0}
k(s)a(s)\,ds.
}
$$

Using

$$
\frac1{S_0}\int_0^{S_0}a(s)\,ds
=
\frac{2-3\gamma}{2},
$$

and Jensen,

$$
\boxed{
\int_0^{S_0}
\mathcal T_\psi(s)\,ds
\le
-
\frac{
(1-2\gamma)(2-3\gamma)
}{2}
S_0
<0.
}
$$

Thus the fully flat recurrent pancake supplier cannot be maintained by zero canonical scalar transport.

A strictly signed finite-annulus transport current is compulsory.

The result is robust: if DCRP35/45 only gives

$$
|a_\psi-a|\le\delta,
$$

then on a compact strict Type-II class the same negative period gap survives once the annular localization error is sufficiently small.

Hence the final branch becomes:

$$
\boxed{
\textbf{
flat scalar structure fails somewhere in the supplier annulus}
}
$$

or

$$
\boxed{
\textbf{
flat structure extends and a strict signed finite-annulus scalar transport current is unavoidable}.
}
$$

This eliminates the “flat + aligned + zero-transport + pure internal reproduction” branch.

PFET is still a distinct observable. DCRP46 does not prove an exact equality between the scalar transport current and pressure–energy flux. What it does prove is that the final equality branch now carries **two simultaneous signed finite-annulus currents**:

1. the DCRP31 inward PFET gap;
2. the DCRP46 negative canonical scalar-moment transport gap.

The next problem is their same-parent coupling / return-depletion, not existence.

---

# 1. Fixed-plane scalar geometry

Work in coordinates in which the fixed rank-two vorticity plane is

$$
n^\perp,
\qquad
n=e_3.
$$

Write

$$
y=(y_h,z),
\qquad
y_h=(y_1,y_2).
$$

On the regular planar branch,

$$
\boxed{
\Omega_h
=
(\partial_2q,-\partial_1q),
\qquad
\Omega_3=0.
}
\tag{1.1}
$$

Equivalently,

$$
\Omega_h
=
-J\nabla_hq,
$$

where

$$
Jv=n\times v.
$$

The residual potential gauge is

$$
\boxed{
q\mapsto q-g(z,s).
}
\tag{1.2}
$$

DCRP44 shows that on the flat scalar-connection branch there is a unique $S_0$-periodic canonical gauge in which

$$
\boxed{
D_sq+k(s)q=0,
}
\tag{1.3}
$$

with

$$
\boxed{
k(s)=1-\gamma-2a(s).
}
\tag{1.4}
$$

---

# 2. Canonical pancake ray

Define

$$
P=I-n\otimes n,
$$

and

$$
\boxed{
C=P-2n\otimes n.
}
\tag{2.1}
$$

Thus, for $n=e_3$,

$$
C=\operatorname{diag}(1,1,-2),
$$

and

$$
|C|_F^2=6.
$$

For any symmetric trace-free affine strain tensor $A$ define its canonical-ray amplitude

$$
\boxed{
a_C(A)
=
\frac{A:C}{6}.
}
\tag{2.2}
$$

DCRP41 gives, on the fixed-plane zero-shape equality branch,

$$
\boxed{
A_{\rm tot}(s)=a(s)C.
}
\tag{2.3}
$$

It also gives the exact periodic mean

$$
\boxed{
\bar a
:=
\frac1{S_0}
\int_0^{S_0}a(s)\,ds
=
\frac{2-3\gamma}{2}.
}
\tag{2.4}
$$

For

$$
\frac25<\gamma<\frac12,
$$

$$
\boxed{
\bar a>0.
}
$$

---

# 3. Fixed annular strain moment

Let

$$
\psi\in C_c^\infty(\mathcal A_\ast)
$$

be a fixed cutoff supported in the common finite supplier annulus.

Using the DCRP35/36 strain kernel $K$, define

$$
\boxed{
A_\psi(s)
=
\int
K(-y)\psi(y)\Omega(y,s)\,dy.
}
\tag{3.1}
$$

Its canonical amplitude is

$$
\boxed{
a_\psi(s)
=
\frac{
C:A_\psi(s)
}{6}.
}
\tag{3.2}
$$

DCRP45 shows that on the final equality branch the annular supplier can be chosen so that

$$
\boxed{
|a_\psi(s)-a(s)|
\le
\delta
}
\tag{3.3}
$$

with $\delta$ arbitrarily small relative to the fixed compact-class supplier gap, after the near-, far-, and Taylor-remainder errors are pushed below the declared tolerance.

The ideal aligned branch is

$$
\boxed{
a_\psi=a.
}
\tag{3.4}
$$

---

# 4. Scalarization of the canonical annular strain moment

Because the strain kernel is linear in $\Omega$ and

$$
\Omega_h=-J\nabla_hq,
$$

there exists a smooth vector weight

$$
L_\psi(y)\in n^\perp
$$

supported in $\mathcal A_\ast$ such that

$$
\boxed{
a_\psi
=
\int
L_\psi(y)\cdot\nabla_hq(y,s)\,dy.
}
\tag{4.1}
$$

Define

$$
\boxed{
H_\psi(y)
=
-\nabla_h\cdot L_\psi(y).
}
\tag{4.2}
$$

Since the weight is compactly supported,

$$
\boxed{
a_\psi(s)
=
\int
H_\psi(y)q(y,s)\,dy.
}
\tag{4.3}
$$

This representation is exact.

---

# 5. Explicit standard-kernel form

With the standard Biot–Savart strain convention,

$$
S(0)
=
\frac{3}{8\pi}
\int
\frac{
(y\times\Omega)\otimes y
+
y\otimes(y\times\Omega)
}{
|y|^5
}
\,dy,
$$

one obtains

$$
\boxed{
a_\psi
=
\frac{3}{8\pi}
\int
\psi(y)
\frac{
z\,y_h\cdot\nabla_hq
}{
|y|^5
}
\,dy.
}
\tag{5.1}
$$

Hence one may take

$$
\boxed{
L_\psi(y)
=
\frac{3}{8\pi}
\psi(y)
\frac{
z\,y_h
}{
|y|^5
},
}
\tag{5.2}
$$

and

$$
\boxed{
H_\psi
=
-\frac{3}{8\pi}
\nabla_h\cdot
\left(
\psi(y)
\frac{
z\,y_h
}{
|y|^5
}
\right).
}
\tag{5.3}
$$

The exact normalization sign depends only on the fixed strain-kernel convention; the invariant definition (3.2) fixes the canonical sign throughout the argument.

---

# 6. Gauge annihilation

Let

$$
g=g(z,s).
$$

Then

$$
\begin{aligned}
\int
H_\psi(y)g(z,s)\,dy
&=
-\int
\nabla_h\cdot L_\psi(y)
\,g(z,s)\,dy
\\
&=
0,
\end{aligned}
$$

because $g$ is horizontally constant and $L_\psi$ has compact horizontal support.

Therefore

$$
\boxed{
\int H_\psi(q-g)\,dy
=
\int H_\psi q\,dy.
}
\tag{6.1}
$$

## Theorem D46.1 — Gauge-Invariant Canonical Scalar Moment

The canonical annular strain amplitude $a_\psi$ is represented by a scalar weight $H_\psi$ which annihilates the entire residual potential-gauge subspace.

Thus

$$
\boxed{
a_\psi
=
\int H_\psi[q]_{\mathcal G}
}
$$

depends only on the gauge quotient of the planar shear scalar.

This gives an explicit bridge between:

- DCRP44 scalar gauge geometry;
- DCRP45 canonical annular strain amplitude.

---

# 7. Flat-extension dichotomy

The DCRP44 scalar theorem is local to a regular fixed-plane patch.

Consider the common finite supplier annulus $\mathcal A_\ast$ from DCRP45.

There are two possibilities.

## Branch I — finite transition

At some point in $\mathcal A_\ast$, at least one of the following fails:

$$
\Omega\cdot n=0,
$$

$$
F_q\neq0,
$$

$$
\mathcal C_{qz}=0,
$$

$$
\mathcal F_{sz}=0,
$$

or the unique periodic canonical scalar gauge cannot be continued.

Then the finite supplier package contains a native transition/defect carrier.

No further scalar-flat analysis is needed on that branch.

## Branch II — flat extension

The entire support of $H_\psi$ remains in one regular fixed-plane gauge-flat scalar chart.

Then the unique periodic canonical $q$ exists throughout the annular moment support and satisfies

$$
D_sq+kq=0.
$$

The rest of this paper treats Branch II.

Thus any result proved below is part of a strict dichotomy:

$$
\boxed{
\text{finite transition defect}
\ \vee\
\text{flat-extension transport law}.
}
$$

---

# 8. Exact weighted transport identity

On the flat-extension branch,

$$
D_sq
=
\partial_sq
+
W\cdot\nabla q,
$$

where

$$
W=\gamma y+V.
$$

Since

$$
\nabla\cdot V=0,
$$

$$
\boxed{
\nabla\cdot W=3\gamma.
}
\tag{8.1}
$$

The scalar equation is

$$
\partial_sq
+
W\cdot\nabla q
+
k(s)q
=
0.
$$

Differentiate

$$
a_\psi(s)
=
\int H_\psi q\,dy.
$$

Because $H_\psi$ is time independent on the fixed-plane fixed-annulus branch,

$$
a_\psi'
=
-\int
H_\psi W\cdot\nabla q\,dy
-
k a_\psi.
$$

Integrating the transport term by parts,

$$
-\int
H_\psi W\cdot\nabla q
=
\int
q
\nabla\cdot(H_\psi W)\,dy.
$$

Thus

$$
\boxed{
a_\psi'
+
k a_\psi
=
\int
q
\left[
W\cdot\nabla H_\psi
+
3\gamma H_\psi
\right]dy.
}
\tag{8.2}
$$

Define

$$
\boxed{
\mathcal T_\psi(s)
=
\int
q
\left[
W\cdot\nabla H_\psi
+
3\gamma H_\psi
\right]dy.
}
\tag{8.3}
$$

## Theorem D46.2 — Canonical Scalar-Moment Transport Equation

On the flat-extension branch,

$$
\boxed{
a_\psi'
+
k(s)a_\psi
=
\mathcal T_\psi.
}
$$

The current $\mathcal T_\psi$ is supported entirely in the fixed finite supplier annulus.

It measures the transport required to maintain the gauge-invariant canonical scalar moment against the homogeneous pancake coefficient $k(s)$.

---

# 9. Why this current is not an arbitrary new observable

The left side of (8.2) is determined entirely by:

- the physical canonical annular strain amplitude $a_\psi$;
- the DCRP41 pancake coefficient $a(s)$ through
  $$
  k=1-\gamma-2a.
  $$

Hence once the unique DCRP44 canonical scalar gauge is selected,

$$
\boxed{
\mathcal T_\psi
=
a_\psi'+k a_\psi
}
\tag{9.1}
$$

is canonically determined.

Even if the integral representation (8.3) is rewritten using a different gauge representative, the value of $\mathcal T_\psi$ is fixed by (9.1).

Thus the signed transport gap below is not a gauge artifact.

---

# 10. Period identity

Because the DSS annular moment is periodic,

$$
a_\psi(S_0)
=
a_\psi(0).
$$

Integrating Theorem D46.2,

$$
\boxed{
\int_0^{S_0}
\mathcal T_\psi(s)\,ds
=
\int_0^{S_0}
k(s)a_\psi(s)\,ds.
}
\tag{10.1}
$$

The sign of this period integral is the next question.

---

# 11. Exact aligned branch

Assume first

$$
\boxed{
a_\psi(s)=a(s).
}
\tag{11.1}
$$

Then

$$
\int_0^{S_0}
\mathcal T_\psi ds
=
\int_0^{S_0}
\left[
(1-\gamma)a
-
2a^2
\right]ds.
$$

Let

$$
\bar a
=
\frac{2-3\gamma}{2}.
$$

By Jensen,

$$
\int_0^{S_0}
a^2ds
\ge
S_0\bar a^2.
$$

Therefore

$$
\begin{aligned}
\int_0^{S_0}
\mathcal T_\psi ds
&\le
S_0
\left[
(1-\gamma)\bar a
-
2\bar a^2
\right]
\\
&=
S_0\bar a(2\gamma-1).
\end{aligned}
$$

Since

$$
\bar a
=
\frac{2-3\gamma}{2},
$$

we obtain

$$
\boxed{
\int_0^{S_0}
\mathcal T_\psi(s)\,ds
\le
-
\frac{
(1-2\gamma)(2-3\gamma)
}{2}
S_0.
}
\tag{11.2}
$$

In the strict Type-II range

$$
\frac25<\gamma<\frac12,
$$

the right side is strictly negative.

---

# Theorem D46.3 — Strict Signed Canonical Transport Gap

On the exact aligned gauge-flat finite-annulus branch,

$$
\boxed{
-\int_0^{S_0}
\mathcal T_\psi(s)\,ds
\ge
\frac{
(1-2\gamma)(2-3\gamma)
}{2}
S_0
>0.
}
$$

Thus a nonzero recurrent canonical pancake supplier cannot satisfy

$$
\mathcal T_\psi\equiv0.
$$

More strongly, its period-averaged canonical scalar transport has a fixed sign and a quantitative lower bound.

This excludes the branch:

$$
\boxed{
\text{flat}
+
\text{aligned}
+
\text{periodic}
+
\text{zero canonical scalar transport}.
}
$$

---

# 12. Interpretation of the sign

The canonical scalar equation has mean coefficient

$$
\bar k
=
2\gamma-1
<0.
$$

Thus, in the chosen forward similarity time, the homogeneous scalar mode has net amplifying Floquet tendency.

A recurrent fixed annular canonical strain moment cannot simply follow that homogeneous material amplification.

The weighted finite-annulus transport current must compensate it.

The sign in Theorem D46.3 is exactly this compensation.

Therefore:

$$
\boxed{
\text{periodic Eulerian canonical supplier}
}
$$

requires

$$
\boxed{
\text{nonzero finite-annulus material/weight transport}.
}
$$

This is the gauge-invariant replacement for the raw scalar-turnover statement downgraded in DCRP43-QC.

---

# 13. Robust approximate branch

DCRP45 provides the approximate alignment

$$
|a_\psi-a|
\le
\delta.
$$

Write

$$
a_\psi=a+e,
$$

with

$$
|e|\le\delta.
$$

Then

$$
\int
\mathcal T_\psi
=
\int ka
+
\int ke.
$$

Define

$$
\boxed{
K_k
=
\frac1{S_0}
\int_0^{S_0}
|k(s)|ds.
}
\tag{13.1}
$$

Then

$$
\left|
\int_0^{S_0}
ke\,ds
\right|
\le
\delta K_kS_0.
$$

Let

$$
\boxed{
g_\gamma
=
\frac{
(1-2\gamma)(2-3\gamma)
}{2}.
}
\tag{13.2}
$$

From Theorem D46.3,

$$
\int ka
\le
-g_\gamma S_0.
$$

Therefore

$$
\boxed{
\int_0^{S_0}
\mathcal T_\psi ds
\le
-
\left(
g_\gamma-\delta K_k
\right)
S_0.
}
\tag{13.3}
$$

Hence if

$$
\boxed{
\delta K_k<g_\gamma,
}
\tag{13.4}
$$

the strict negative sign survives.

---

# Theorem D46.4 — Robust Finite-Annulus Transport Gap

On any compact strict Type-II class for which

$$
\gamma
\in
[\gamma_-,\gamma_+]
\Subset
\left(
\frac25,\frac12
\right),
$$

and

$$
K_k\le K_\ast,
$$

define

$$
g_\ast
=
\min_{\gamma\in[\gamma_-,\gamma_+]}
\frac{
(1-2\gamma)(2-3\gamma)
}{2}
>0.
$$

If the DCRP35/45 supplier localization is chosen so that

$$
\boxed{
\delta
<
\frac{
g_\ast
}{
2K_\ast
},
}
$$

then uniformly

$$
\boxed{
-\int_0^{S_0}
\mathcal T_\psi ds
\ge
\frac{
g_\ast
}{2}
S_0.
}
$$

Thus the signed transport gap is stable under the finite-annulus localization error.

---

# 14. Consequence for DCRP45's source-channel frontier

DCRP45 had reduced the five-dimensional affine reproduction problem to the scalar identity

$$
a_\psi'+a_\psi
=
j_{\rm dil}
+
j_{\rm adv}
+
j_{\rm str}.
$$

DCRP46 supplies, on the flat-extension branch,

$$
a_\psi'+k a_\psi
=
\mathcal T_\psi.
$$

Subtracting,

$$
\boxed{
j_{\rm dil}
+
j_{\rm adv}
+
j_{\rm str}
=
\mathcal T_\psi
+
(1-k)a_\psi.
}
\tag{14.1}
$$

Since

$$
1-k
=
\gamma+2a,
$$

$$
\boxed{
j_{\rm dil}
+
j_{\rm adv}
+
j_{\rm str}
=
\mathcal T_\psi
+
(\gamma+2a)a_\psi.
}
\tag{14.2}
$$

Thus, on the flat branch, the three DCRP36 source channels are not an unconstrained three-way phase problem.

Their sum is forced by:

1. a positive local pancake-stretching term;
2. the signed canonical scalar transport current.

This is a second compression after DCRP45.

---

# 15. Pure internal-reproduction branch is excluded

Suppose one attempts the equality mechanism:

$$
\boxed{
\text{periodic canonical supplier}
}
$$

with

$$
\boxed{
\mathcal T_\psi=0.
}
$$

Then Theorem D46.2 gives

$$
a_\psi'+ka_\psi=0.
$$

For a periodic nonzero $a_\psi$, this requires the Floquet multiplier

$$
\exp
\left(
-\int_0^{S_0}k(s)ds
\right)
=
1.
$$

But

$$
\int_0^{S_0}k(s)ds
=
(2\gamma-1)S_0
\neq0.
$$

Therefore:

## Theorem D46.5 — Zero-Transport Periodic Canonical Supplier NO-GO

On the strict Type-II flat-extension branch,

$$
\boxed{
\mathcal T_\psi\equiv0
}
$$

and

$$
\boxed{
a_\psi\not\equiv0
}
$$

cannot coexist with $S_0$-periodicity.

The quantitative Theorem D46.3 is stronger on the aligned equality branch.

---

# 16. Finite-annulus transition / transport dichotomy

Combine Sections 7 and 15.

## Theorem D46.6 — Flat-Extension / Transition Dichotomy

For the final fixed-plane zero-shape recurrent rank-two supplier package, at least one of the following must occur:

### Transition branch

The DCRP44 gauge-flat planar scalar structure fails somewhere inside the common finite supplier annulus.

Then there is a finite normalized transition/defect carrier.

### Flat-extension branch

The gauge-flat scalar structure extends across the annular canonical-moment support.

Then

$$
\boxed{
-\int_0^{S_0}
\mathcal T_\psi ds
>0,
}
$$

with the quantitative compact-class gap of Theorem D46.4.

Therefore the final survivor cannot hide both:

- all local scalar-connection defects;
- all finite-annulus canonical scalar transport.

At least one finite native observable is active.

---

# 17. Relation to DCRP31 PFET

DCRP31 gives a separate finite-annulus gap for the physical pressure–kinetic energy current:

$$
\boxed{
\mathcal F(R)
=
\int_0^{S_0}
\int_{\partial B_R}
(e+P)V\cdot n
\,dSds,
}
$$

with a compact-class inward aggregate lower bound

$$
\boxed{
\int_{R_0}^{R_1}
(-\mathcal F(R))_+
R^{-\kappa-1}dR
\ge
c_{\rm PFET}>0.
}
$$

DCRP46 gives another finite-annulus signed current:

$$
\boxed{
-\int_0^{S_0}
\mathcal T_\psi ds
\ge
c_{\rm tr}>0
}
$$

on the flat-extension branch.

The two currents are not identical.

PFET measures energy transfer and explicitly involves pressure.

$\mathcal T_\psi$ measures transport of the canonical planar-shear/strain moment.

No exact theorem currently gives

$$
\mathcal T_\psi
=
c\,\mathcal F
$$

or any universal same-sign pointwise relation.

This separation is retained deliberately.

---

# 18. Dual-current finite-annulus package

Nevertheless, on the most rigid final branch the same finite normalized package must carry both:

$$
\boxed{
\mathsf O_{\rm PFET}>0
}
$$

and

$$
\boxed{
\mathsf O_{\rm tr}>0,
}
$$

where the second may be defined by

$$
\boxed{
\mathsf O_{\rm tr}
=
-\int_0^{S_0}
\mathcal T_\psi ds.
}
$$

Thus define the finite-annulus dual-current observer

$$
\boxed{
\mathsf O_{\rm dual}
=
\left(
\mathsf O_{\rm PFET},
\mathsf O_{\rm tr}
\right).
}
\tag{18.1}
$$

On a compact aligned flat-extension class,

$$
\boxed{
\mathsf O_{\rm dual}
\in
[c_{\rm PFET},\infty)
\times
[c_{\rm tr},\infty).
}
\tag{18.2}
$$

This is a stronger local visibility statement than either ledger alone.

It is not yet a depletion theorem.

---

# 19. Why the result still does not close Navier–Stokes

Both normalized currents may recur critically under the DSS same-parent scaling.

DCRP31 already showed that a fixed normalized PFET event can correspond to a geometrically decaying raw physical energy transfer.

DCRP43-QC similarly showed that raw normalized scalar factors must be quotient-corrected before being treated as parent-level taxes.

Therefore:

$$
\boxed{
\text{two positive normalized finite-annulus gaps}
}
$$

do not by themselves imply an unsummable physical cost.

The remaining issue is same-parent **joint return depletion**.

---

# 20. Stronger interpretation of the DCRP36 transport/stretching split

DCRP36 originally classified affine reproduction into:

$$
J_{\rm dil},
\qquad
J_{\rm adv},
\qquad
J_{\rm str}.
$$

DCRP45 compressed their canonical projection to one scalar source sum.

DCRP46 now shows that, after imposing the flat scalar structure, the periodic canonical source cannot be understood as “internal stretching only with no transport.”

The scalar moment obeys its own continuity-type identity and requires a nonzero weighted transport current.

Thus the final equality branch has a compulsory **transport component in the scalar quotient geometry**, even if the vorticity-moment equation distributes its algebra among $J_{\rm adv}$ and $J_{\rm str}$.

This distinction matters:

$$
\boxed{
\text{algebraic source decomposition}
\neq
\text{intrinsic scalar transport requirement}.
}
$$

---

# 21. NTLA-O interpretation

This round gives the first clean NS use of the rebuilt NTLA-O local/global and quotient logic.

At coarse affine resolution the annular supplier is a five-dimensional tensor.

DCRP45 reduces it to one canonical amplitude.

DCRP44 quotients the scalar gauge and identifies the flat scalar connection.

DCRP46 asks whether that flat representation extends across the entire supplier support.

Hence:

$$
\boxed{
\text{core flatness}
\not\Rightarrow
\text{annular flat extension}.
}
$$

Failure of extension is a finite transition defect.

If extension succeeds, the compatible local sections satisfy an additional global annular transport identity with a strict signed period gap.

This is exactly a local-to-global/descent alternative:

$$
\boxed{
\text{failure of descent}
\ \vee\
\text{nonzero compatible transport}.
}
$$

---

# 22. Updated final rank-two survivor

After DCRP46, the surviving equality branch must satisfy:

$$
\boxed{
\begin{aligned}
&
\text{strict same-parent DSS}
\\
&+
\text{rank two}
\\
&+
\text{fixed vorticity plane}
\\
&+
\text{zero covariance-shape action}
\\
&+
\text{gauge-flat scalar connection}
\\
&+
\text{flat extension through the finite supplier annulus}
\\
&+
\text{canonical-ray annular supplier}
\\
&+
\text{strict signed canonical scalar transport}
\\
&+
\text{finite inward PFET matching}
\\
&+
\text{finite-energy unforced ancestry}.
\end{aligned}
}
$$

If any flat-extension condition fails, the failure is already a finite defect branch.

Thus the survivor is now a **joint two-current same-parent recurrence problem**.

---

# 23. Status ledger

## PROVED this round

### D46-P1 — Gauge-invariant scalar representation of canonical annular strain

$$
a_\psi
=
\int H_\psi q,
$$

with $H_\psi$ annihilating $q\mapsto q-g(z,s)$.

### D46-P2 — Exact finite-annulus scalar transport equation

$$
a_\psi'+ka_\psi
=
\mathcal T_\psi.
$$

### D46-P3 — Strict aligned signed transport gap

$$
-\int_0^{S_0}
\mathcal T_\psi ds
\ge
\frac{
(1-2\gamma)(2-3\gamma)
}{2}
S_0.
$$

### D46-P4 — Robust compact-class transport gap

The negative period sign survives sufficiently small DCRP35/45 supplier-alignment error.

### D46-P5 — Zero-transport periodic canonical supplier NO-GO

A nonzero periodic flat canonical supplier cannot have $\mathcal T_\psi\equiv0$.

### D46-P6 — Flat-extension / transition dichotomy

Either scalar flatness fails somewhere in the finite supplier annulus, or a strict finite-annulus signed transport current is mandatory.

---

# 24. Closed / downgraded routes

## Closed

The branch

$$
\boxed{
\text{fully flat}
+
\text{aligned}
+
\text{periodic}
+
\text{zero finite-annulus scalar transport}
}
$$

is excluded.

## Still open

A recurrent nonzero scalar transport current may coexist with the DCRP31 inward PFET current without violating a raw critical physical budget.

Therefore no global contradiction is claimed.

---

# 25. New STOP

$$
\boxed{
\textbf{
STOP-D46:
On the final flat-extension pancake branch, finite-annulus transport is not optional; it has a strict signed period gap. The remaining problem is joint same-parent return depletion of this transport current with PFET.
}
}
$$

---

# 26. Next autonomous step

## DCRP47 — Dual-Current Same-Parent Return Depletion

**Working title**

> **PFET–Scalar Transport Joint Return Map, Critical Scaling, and Two-Current Equality Classification**

Primary tasks:

1. derive the exact same-parent reroot scaling of the canonical scalar transport observable $\mathsf O_{\rm tr}$;
2. compare with the DCRP31 PFET scaling;
3. search for a quotient-invariant ratio or signed joint action;
4. test whether the pair can recur exactly without:
   - a finite transition defect;
   - a noncritical tail;
   - an exact scale-invariant equality mode.

Possible useful endpoint:

$$
\boxed{
\text{joint depletion}
\ \vee\
\text{critical equality mode}
\ \vee\
\text{transition}.
}
$$

If the joint pair remains exactly critical, classify the equality mode rather than forcing a false summability contradiction.

---

# 27. One-line checkpoint

The flat rank-two pancake branch now has a compulsory, quantitatively signed finite-annulus scalar transport current in addition to the mandatory inward PFET current; the remaining survivor is therefore a two-current same-parent recurrence problem.

---

**End checkpoint:** DCRP46  
**Next:** DCRP47 — Dual-Current Same-Parent Return Depletion.
