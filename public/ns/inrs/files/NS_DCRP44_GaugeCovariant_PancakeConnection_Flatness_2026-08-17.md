# DCRP44 — Gauge-Covariant Pancake Scalar Connection, Flatness Defects, and Canonical Eigenmode Classification

**Series:** Independent Navier–Stokes Research Series  
**Date:** 2026-08-17  
**Status:** Proof-development checkpoint / gauge repair round  
**Immediate predecessor:** `NS_DCRP43_QC_SameParent_Scalar_GaugeQuotient_Audit_2026-08-17.md`

**Primary internal dependencies**
- DCRP-30: exact same-parent reroot identity
- DCRP-31: finite-radius inward PFET matching layer
- DCRP-35: finite-annulus enstrophy/strain supplier
- DCRP-40/41: rank-two planar / moving-pancake reduction
- DCRP-42: planar potential–shear scalar reduction

**External calibration**
- Agafontsev–Kuznetsov–Mailybaev, *Asymptotic solution for high vorticity regions in incompressible 3D Euler equations*, arXiv:1609.07782.
- Enciso–Fernández–Meyer, *Vortex-sheet desingularization for three-dimensional ideal fluids*, arXiv:2607.19233.
- Seregin, *On potential Type II blowups for the Navier-Stokes equations*, arXiv:2606.29468.

No full Navier–Stokes regularity theorem is claimed.

---

# 0. Executive result

DCRP43-QC showed that the scalar

$$
q=w-\partial_z\phi
$$

has a residual gauge freedom

$$
q\mapsto q-g(z,s),
$$

and that the bare DCRP-42 condition

$$
G
=
F_z+2a
=
0
$$

is not invariant under this gauge when

$$
F_q\neq0.
$$

This round repairs that problem.

The main result is that the planar scalar reduction admits a natural gauge-covariant connection on the local $(q,z,s)$ characteristic space.

On the regular nondegenerate patch

$$
F_q\neq0,
$$

define

$$
\boxed{
A_z
=
\frac{F_z+2a}{F_q},
}
$$

and

$$
\boxed{
A_s
=
\mathscr H
-
W_3A_z,
\qquad
W_3=\gamma z+F.
}
$$

Under the residual scalar gauge

$$
q'=q-g(z,s),
$$

these coefficients transform exactly as

$$
\boxed{
A_z'
=
A_z\circ T_g+g_z,
}
$$

$$
\boxed{
A_s'
=
A_s\circ T_g+g_s,
}
$$

where

$$
T_g(q',z,s)
=
(q'+g(z,s),z,s).
$$

Thus the differential operators

$$
\boxed{
\mathcal D_z
=
\partial_z-A_z\partial_q,
}
$$

$$
\boxed{
\mathcal D_s
=
\partial_s-A_s\partial_q
}
$$

are gauge-covariant geometric objects.

Two native defects then emerge.

First,

$$
\boxed{
\mathcal C_{qz}
=
\partial_qA_z
=
\partial_q
\left(
\frac{F_z+2a}{F_q}
\right)
}
$$

is gauge invariant up to the natural coordinate composition.

Equivalently, without division,

$$
\boxed{
\mathfrak C_{qz}
=
F_qF_{zq}
-
(F_z+2a)F_{qq}
}
$$

is an everywhere-defined numerator invariant.

Second, define the connection curvature

$$
\boxed{
\mathcal F_{sz}
=
\partial_sA_z
-
\partial_zA_s
-
A_s\partial_qA_z
+
A_z\partial_qA_s.
}
$$

Then

$$
\boxed{
[\mathcal D_s,\mathcal D_z]
=
-\mathcal F_{sz}\partial_q.
}
$$

The zero/nonzero status of $\mathcal F_{sz}$ is gauge invariant.

The decisive theorem is:

> On a regular nondegenerate fixed-plane patch, the DCRP-42 periodic homogeneous canonical scalar gauge
>
> $$
> G=0,
> \qquad
> D_sq+k(s)q=0
> $$
>
> exists locally if and only if
>
> $$
> \boxed{
> \mathcal C_{qz}=0,
> \qquad
> \mathcal F_{sz}=0,
> }
> $$
>
> together with the strict Type-II nonresonance
>
> $$
> \int_0^{S_0}k(s)\,ds
> =
(2\gamma-1)S_0
\neq0.
> $$

Moreover, the resulting periodic homogeneous gauge is unique.

This repairs DCRP-42:

$$
\boxed{
\text{bare }G=0
}
$$

should no longer be treated as the invariant equality branch.

The invariant branch is

$$
\boxed{
\textbf{flat scalar-connection branch}
:
\mathcal C_{qz}
=
\mathcal F_{sz}
=
0.
}
$$

Any nonzero defect becomes a native gauge-invariant residual branch.

This is a genuine structural reduction.

---

# 1. DCRP-42 local scalar system

On a regular fixed-plane planar-vorticity patch,

$$
V_h=\nabla_h\phi,
$$

$$
w=V_3,
$$

and

$$
\boxed{
q=w-\phi_z.
}
\tag{1.1}
$$

The planar vorticity is

$$
\boxed{
\Omega_h
=
J\nabla_hq.
}
\tag{1.2}
$$

The normal vorticity equation gives

$$
\Omega_h\cdot\nabla_hw=0.
$$

Hence on a connected regular patch where

$$
\nabla_hq\neq0,
$$

there is a constitutive function

$$
\boxed{
w
=
F(q,z,s).
}
\tag{1.3}
$$

Define

$$
W
=
\gamma y+V,
$$

$$
D_s
=
\partial_s+W\cdot\nabla.
$$

DCRP-42 derives

$$
\boxed{
D_sq+\mathscr H(q,z,s)=0,
}
\tag{1.4}
$$

with

$$
\boxed{
\mathscr H_q
=
1-\gamma+F_z,
}
\tag{1.5}
$$

where $F_z$ denotes partial differentiation at fixed $q$.

On the fixed-plane pancake branch, define

$$
\boxed{
k(s)
=
1-\gamma-2a(s),
}
\tag{1.6}
$$

and

$$
\boxed{
G(q,z,s)
=
F_z(q,z,s)+2a(s).
}
\tag{1.7}
$$

Then

$$
\boxed{
\mathscr H_q
=
k+G.
}
\tag{1.8}
$$

---

# 2. Residual potential gauge

The horizontal potential is not unique.

For arbitrary smooth $h(z,s)$,

$$
\phi'
=
\phi+h(z,s)
$$

gives the same

$$
V_h=\nabla_h\phi.
$$

Define

$$
g(z,s)
=
h_z(z,s).
$$

Then

$$
\boxed{
q'
=
q-g(z,s).
}
\tag{2.1}
$$

Locally, any smooth $g(z,s)$ can be realized by a suitable $h$.

Thus the local scalar gauge group is the additive translation group

$$
\boxed{
q\mapsto q-g(z,s).
}
$$

---

# 3. Transformation of the constitutive function

The physical normal velocity $w$ must remain unchanged.

If

$$
q=q'+g(z,s),
$$

define

$$
\boxed{
F'(q',z,s)
=
F(q'+g(z,s),z,s).
}
\tag{3.1}
$$

Then

$$
w
=
F(q,z,s)
=
F'(q',z,s).
$$

Differentiating,

$$
\boxed{
F_q'
=
F_q\circ T_g,
}
\tag{3.2}
$$

$$
\boxed{
F_z'
=
(F_z+F_qg_z)\circ T_g,
}
\tag{3.3}
$$

where

$$
T_g(q',z,s)
=
(q'+g(z,s),z,s).
$$

Therefore

$$
\boxed{
G'
=
(G+F_qg_z)\circ T_g.
}
\tag{3.4}
$$

This re-derives the DCRP43-QC observation:

$$
G=0
$$

is not gauge invariant when

$$
F_q\neq0.
$$

---

# 4. Transformation of the scalar transport potential

From

$$
q'
=
q-g(z,s),
$$

we obtain

$$
D_sq'
=
D_sq
-
g_s
-
W_3g_z,
$$

where

$$
\boxed{
W_3
=
\gamma z+w
=
\gamma z+F(q,z,s).
}
\tag{4.1}
$$

Since

$$
D_sq+\mathscr H(q,z,s)=0,
$$

the transformed equation is

$$
D_sq'
+
\mathscr H'(q',z,s)
=
0
$$

with

$$
\boxed{
\mathscr H'
=
\left[
\mathscr H
+
g_s
+
W_3g_z
\right]\circ T_g.
}
\tag{4.2}
$$

Differentiating with respect to $q'$ gives

$$
\mathscr H_q'
=
\left[
\mathscr H_q
+
F_qg_z
\right]\circ T_g
=
\left[
1-\gamma+F_z+F_qg_z
\right]\circ T_g
$$

which equals

$$
1-\gamma+F_z'.
$$

So the scalar reduction is exactly gauge covariant.

---

# 5. The nondegenerate normal-shear connection coefficient

Assume on the regular patch

$$
\boxed{
F_q\neq0.
}
\tag{5.1}
$$

Define

$$
\boxed{
A_z
=
\frac{G}{F_q}
=
\frac{F_z+2a}{F_q}.
}
\tag{5.2}
$$

Using (3.2)–(3.4),

$$
A_z'
=
\frac{
G+F_qg_z
}{
F_q
}
\circ T_g.
$$

Therefore

$$
\boxed{
A_z'
=
(A_z+g_z)\circ T_g.
}
\tag{5.3}
$$

This is the exact transformation law of a connection coefficient under a fiber translation.

---

# 6. First gauge-invariant defect

Differentiate (5.3) with respect to $q'$.

Because $g_z$ is independent of $q'$,

$$
\boxed{
\partial_{q'}A_z'
=
(\partial_qA_z)\circ T_g.
}
\tag{6.1}
$$

Thus the zero/nonzero status of

$$
\boxed{
\mathcal C_{qz}
=
\partial_qA_z
}
\tag{6.2}
$$

is gauge invariant.

Expanding,

$$
\boxed{
\mathcal C_{qz}
=
\frac{
F_qF_{zq}
-
(F_z+2a)F_{qq}
}{
F_q^2
}.
}
\tag{6.3}
$$

Define the denominator-free defect

$$
\boxed{
\mathfrak C_{qz}
=
F_qF_{zq}
-
(F_z+2a)F_{qq}.
}
\tag{6.4}
$$

Under the gauge transformation,

$$
\boxed{
\mathfrak C_{qz}'
=
\mathfrak C_{qz}\circ T_g.
}
\tag{6.5}
$$

This follows from the exact cancellation of the added $g_z$ terms.

## Theorem D44.1 — Gauge-Invariant Normal-Shear Flatness Defect

The scalar

$$
\mathfrak C_{qz}
$$

is invariant under the residual potential gauge up to the natural reparameterization $T_g$.

Hence

$$
\boxed{
\mathfrak C_{qz}=0
}
$$

is a native observer-independent property of the local planar-shear representation.

---

# 7. What $\mathcal C_{qz}=0$ means

On the nondegenerate patch,

$$
\mathcal C_{qz}=0
$$

is equivalent to

$$
\partial_qA_z=0.
$$

Hence

$$
\boxed{
A_z=A_0(z,s)
}
\tag{7.1}
$$

is independent of the scalar fiber coordinate.

Then solve locally

$$
\boxed{
g_z=-A_0(z,s).
}
\tag{7.2}
$$

Under this gauge,

$$
A_z'=0.
$$

Since

$$
F_q'\neq0,
$$

this is equivalent to

$$
\boxed{
G'=0.
}
\tag{7.3}
$$

Conversely, if some gauge has

$$
G'=0,
$$

then

$$
A_z'=0,
$$

hence

$$
\partial_{q'}A_z'=0,
$$

and therefore

$$
\mathcal C_{qz}=0.
$$

## Theorem D44.2 — $z$-Gauge Flattening Criterion

On a connected regular patch with

$$
F_q\neq0,
$$

there exists locally a residual scalar gauge in which

$$
G=0
$$

if and only if

$$
\boxed{
\mathcal C_{qz}=0.
}
$$

Thus the invariant content of “$G=0$ is reachable” is not the bare equation $G=0$ itself, but the vanishing of the gauge-flatness defect $\mathcal C_{qz}$.

---

# 8. The degenerate branch $F_q=0$

If

$$
F_q=0
$$

on a regular connected patch, then

$$
\nabla_hw
=
F_q\nabla_hq
=
0.
$$

Therefore

$$
\boxed{
w=w(z,s)
}
$$

is horizontally uniform on that patch.

Moreover the gauge law (3.4) reduces to

$$
\boxed{
G'=G.
}
$$

So in this degenerate branch,

$$
G
$$

is already gauge invariant.

If in addition

$$
G=0,
$$

then

$$
F_z=-2a(s),
$$

hence

$$
\boxed{
w(z,s)
=
-2a(s)z+c(s).
}
\tag{8.1}
$$

This is an exact affine normal velocity.

Thus the $F_q=0$ branch is not a loophole in the gauge repair.

It is a separate, more rigid branch.

---

# 9. The second connection coefficient

Define

$$
\boxed{
A_s
=
\mathscr H
-
W_3A_z,
}
\tag{9.1}
$$

where

$$
W_3=\gamma z+F.
$$

Using the transformation laws,

$$
\mathscr H'
=
(\mathscr H+g_s+W_3g_z)\circ T_g,
$$

$$
A_z'
=
(A_z+g_z)\circ T_g,
$$

and

$$
W_3'
=
W_3\circ T_g,
$$

we obtain

$$
\boxed{
A_s'
=
(A_s+g_s)\circ T_g.
}
\tag{9.2}
$$

Thus $(A_s,A_z)$ transform exactly like two connection coefficients for the translation gauge.

---

# 10. Gauge-covariant horizontal lifts

Define differential operators on the local $(q,z,s)$ characteristic space:

$$
\boxed{
\mathcal D_z
=
\partial_z-A_z\partial_q,
}
\tag{10.1}
$$

$$
\boxed{
\mathcal D_s
=
\partial_s-A_s\partial_q.
}
\tag{10.2}
$$

Under

$$
q'=q-g(z,s),
$$

the coordinate derivatives transform as

$$
\partial_z\big|_{q'}
=
\partial_z\big|_q
+
g_z\partial_q,
$$

$$
\partial_s\big|_{q'}
=
\partial_s\big|_q
+
g_s\partial_q.
$$

Together with (5.3) and (9.2), this gives

$$
\boxed{
\mathcal D_z'
=
\mathcal D_z,
}
$$

$$
\boxed{
\mathcal D_s'
=
\mathcal D_s
}
$$

as geometric vector fields.

This makes the gauge structure explicit.

---

# 11. Scalar-connection curvature

Compute the commutator:

$$
[\mathcal D_s,\mathcal D_z]
=
-\mathcal F_{sz}\partial_q,
$$

where

$$
\boxed{
\mathcal F_{sz}
=
\partial_sA_z
-
\partial_zA_s
-
A_s\partial_qA_z
+
A_z\partial_qA_s.
}
\tag{11.1}
$$

Because the vector fields $\mathcal D_s,\mathcal D_z$ themselves are gauge covariant, the zero/nonzero status of

$$
\mathcal F_{sz}
$$

is gauge invariant.

More explicitly,

$$
\boxed{
\mathcal F_{sz}'
=
\mathcal F_{sz}\circ T_g.
}
\tag{11.2}
$$

## Theorem D44.3 — Gauge-Covariant Scalar-Connection Curvature

The commutator defect

$$
\mathcal F_{sz}
$$

is a native gauge-invariant local scalar-connection obstruction.

If

$$
\mathcal F_{sz}\neq0,
$$

the $(z,s)$ scalar-transport distribution is not flat.

---

# 12. An exact identity for $\partial_qA_s$

Using

$$
\mathscr H_q
=
k+G,
$$

$$
G=F_qA_z,
$$

and

$$
(W_3)_q=F_q,
$$

differentiate

$$
A_s=\mathscr H-W_3A_z.
$$

Then

$$
\begin{aligned}
\partial_qA_s
&=
k+G
-
F_qA_z
-
W_3\partial_qA_z
\\
&=
k-W_3\partial_qA_z.
\end{aligned}
$$

Thus

$$
\boxed{
\partial_qA_s
=
k-W_3\mathcal C_{qz}.
}
\tag{12.1}
$$

Therefore if

$$
\mathcal C_{qz}=0,
$$

then automatically

$$
\boxed{
\partial_qA_s=k(s).
}
\tag{12.2}
$$

So after the first flatness defect vanishes, the scalar-fiber slope of $A_s$ is already forced to be the canonical pancake coefficient.

This is an important rigidity gain.

---

# 13. Reduction in a $G=0$ gauge

Assume

$$
\mathcal C_{qz}=0.
$$

Choose the local gauge from Theorem D44.2 with

$$
A_z=0,
$$

equivalently

$$
G=0.
$$

Then

$$
A_s=\mathscr H.
$$

From (12.2),

$$
\mathscr H_q=k(s).
$$

Therefore

$$
\boxed{
\mathscr H(q,z,s)
=
k(s)q+C(z,s).
}
\tag{13.1}
$$

In this gauge the curvature becomes

$$
\mathcal F_{sz}
=
-\partial_zA_s
=
-\partial_zC(z,s).
$$

Hence

$$
\boxed{
\mathcal F_{sz}=0
\iff
C(z,s)=C(s).
}
\tag{13.2}
$$

The second curvature therefore detects whether the remaining additive scalar forcing can be made purely time dependent after $z$-flattening.

---

# 14. Residual gauge preserving $G=0$

Once

$$
A_z=0,
$$

a further gauge transformation preserves $A_z=0$ precisely when

$$
g_z=0.
$$

Hence the residual gauge is

$$
\boxed{
g=g(s).
}
\tag{14.1}
$$

Under this transformation,

$$
q'=q-g(s).
$$

Equation (13.1) transforms to

$$
A_s'
=
k(s)q'
+
\left[
k(s)g(s)+C(s)+g_s(s)
\right].
$$

Therefore the remaining additive term vanishes precisely if

$$
\boxed{
g_s+k(s)g=-C(s).
}
\tag{14.2}
$$

---

# 15. Strict Type-II Floquet nonresonance

DCRP-42 gives

$$
\boxed{
\frac1{S_0}
\int_0^{S_0}k(s)\,ds
=
2\gamma-1
<
0.
}
\tag{15.1}
$$

Thus

$$
\boxed{
\int_0^{S_0}k(s)\,ds
=
(2\gamma-1)S_0
\neq0.
}
\tag{15.2}
$$

The homogeneous residual-gauge equation

$$
g_s+kg=0
$$

has one-period multiplier

$$
\boxed{
M_g
=
\exp
\left(
-\int_0^{S_0}k(s)\,ds
\right)
=
e^{(1-2\gamma)S_0}
\neq1.
}
\tag{15.3}
$$

Therefore the periodic boundary-value problem

$$
g_s+kg=-C(s),
\qquad
g(s+S_0)=g(s)
$$

has a unique periodic solution.

This is a standard first-order Floquet nonresonance fact and can also be verified directly by variation of constants.

---

# 16. Canonical periodic scalar-gauge theorem

We can now combine the two flatness defects.

## Theorem D44.4 — Gauge-Invariant Characterization of the DCRP-42 Canonical Scalar Eigenmode

Consider a connected regular fixed-plane patch satisfying

$$
F_q\neq0,
$$

with $S_0$-periodic coefficients and strict Type-II parameter

$$
1-2\gamma>0.
$$

Then the following are equivalent, locally in the $z$-direction:

### (A)

There exists an $S_0$-periodic residual potential gauge in which

$$
\boxed{
G=0
}
$$

and

$$
\boxed{
D_sq+k(s)q=0.
}
$$

### (B)

The gauge-invariant defects vanish:

$$
\boxed{
\mathcal C_{qz}=0,
}
$$

$$
\boxed{
\mathcal F_{sz}=0.
}
$$

### Proof

#### (A) implies (B)

In the canonical gauge,

$$
G=0,
$$

so

$$
A_z=0.
$$

Therefore

$$
\mathcal C_{qz}
=
\partial_qA_z
=
0.
$$

Also

$$
D_sq+kq=0
$$

means

$$
\mathscr H=kq.
$$

Hence

$$
A_s=kq.
$$

Since $A_z=0$ and $A_s$ has no explicit $z$ dependence at fixed $q$,

$$
\mathcal F_{sz}=0.
$$

Gauge covariance implies the defects vanish in every gauge.

#### (B) implies (A)

From

$$
\mathcal C_{qz}=0,
$$

Theorem D44.2 gives a local periodic gauge with

$$
A_z=0,
$$

hence

$$
G=0.
$$

Then

$$
A_s=kq+C(z,s).
$$

Because

$$
\mathcal F_{sz}=0,
$$

equation (13.2) gives

$$
C=C(s).
$$

The residual gauge preserving $A_z=0$ has $g=g(s)$.

Solve

$$
g_s+kg=-C(s).
$$

By strict Type-II Floquet nonresonance, there is a unique periodic solution.

In this gauge,

$$
A_s=kq,
$$

hence

$$
\mathscr H=kq
$$

and therefore

$$
D_sq+kq=0.
$$

This proves (A).

$$
\square
$$

---

# 17. Uniqueness of the periodic canonical gauge

Suppose $q$ and $\widetilde q$ are two $S_0$-periodic gauges both satisfying

$$
G=0,
$$

$$
D_sq+kq=0,
$$

and

$$
D_s\widetilde q+k\widetilde q=0.
$$

Because both have $G=0$ and $F_q\neq0$, their gauge difference satisfies

$$
g_z=0.
$$

So

$$
\widetilde q=q-g(s).
$$

Subtracting the two homogeneous scalar equations gives

$$
g_s+kg=0.
$$

Periodicity and

$$
M_g\neq1
$$

force

$$
g\equiv0.
$$

Therefore:

## Theorem D44.5 — Uniqueness of the Strict-Type-II Periodic Canonical Scalar Gauge

On the nondegenerate flat scalar-connection branch,

$$
\boxed{
\text{the }S_0\text{-periodic gauge satisfying }
G=0,\ 
D_sq+kq=0
\text{ is unique}.
}
$$

This is important.

DCRP43-QC correctly showed that raw $q$ is not gauge invariant.

DCRP44 now shows that on the genuinely flat equality branch, the strict-Type-II periodicity condition selects a unique canonical representative.

Thus the DCRP-42 scalar eigenmode can be restored in an invariant way:

$$
\boxed{
\text{flat connection class}
\longrightarrow
\text{unique periodic scalar representative}.
}
$$

---

# 18. Revised rank-two scalar branch classification

The old branch split

$$
G\neq0
\quad\vee\quad
G=0
$$

is gauge dependent.

Replace it by the following invariant split.

---

## Branch I — Degenerate normal coupling

$$
\boxed{
F_q=0.
}
$$

Then

$$
\nabla_hw=0.
$$

If $G=0$ as well, the normal velocity is exactly affine:

$$
w=-2az+c(s).
$$

---

## Branch II — Native scalar-connection nonflatness

$$
\boxed{
F_q\neq0,
\qquad
\mathcal C_{qz}\neq0.
}
$$

Then no residual scalar gauge can make

$$
G=0
$$

throughout the patch.

This is a genuine gauge-invariant non-affine normal-shear residual.

---

## Branch III — $z$-flat but $(s,z)$-curved

$$
\boxed{
F_q\neq0,
\qquad
\mathcal C_{qz}=0,
\qquad
\mathcal F_{sz}\neq0.
}
$$

Then one may gauge

$$
G=0,
$$

but the remaining scalar transport connection cannot be reduced to the homogeneous DCRP-42 eigenmode.

This is another native gauge-invariant residual.

---

## Branch IV — Fully flat canonical scalar connection

$$
\boxed{
F_q\neq0,
\qquad
\mathcal C_{qz}=0,
\qquad
\mathcal F_{sz}=0.
}
$$

Then a unique periodic canonical gauge exists with

$$
\boxed{
G=0,
}
$$

$$
\boxed{
D_sq+k(s)q=0.
}
$$

Only on this branch should the exact DCRP-42 scalar eigenmode and its periodic integrating factor be treated as the canonical equality state.

---

# 19. Impact on DCRP-42

This round produces both a correction and a rescue.

## Correction

The raw statement

$$
\boxed{
G=0
}
$$

is not a gauge-invariant branch definition.

## Rescue

The existence of the DCRP-42 canonical scalar eigenmode is equivalent, on the regular nondegenerate branch, to the invariant conditions

$$
\boxed{
\mathcal C_{qz}=0,
\qquad
\mathcal F_{sz}=0.
}
$$

Strict Type-II periodicity then makes the canonical homogeneous scalar gauge unique.

Thus DCRP-42 does not need to be discarded.

It should be rewritten as a **flat scalar-connection theorem**.

---

# 20. NTLA-O interpretation

This is an explicit NS example of why the observer/judgment quotient must be applied before declaring a difference native.

The raw observer sees

$$
F_z+2a.
$$

But a scalar gauge shift changes it.

The next observer level identifies the connection coefficient

$$
A_z=\frac{F_z+2a}{F_q}.
$$

This still changes by an additive gauge derivative.

The invariant observer sees

$$
\boxed{
\partial_qA_z
}
$$

and the commutator curvature

$$
\boxed{
\mathcal F_{sz}.
}
$$

Thus the NTLA-O refinement chain is

$$
\boxed{
G
\rightarrow
A_z
\rightarrow
(\mathcal C_{qz},\mathcal F_{sz}).
}
$$

Only the final defects are native to the gauge quotient.

This is exactly the “first illegal lift / first invariant distinction” logic for which NTLA-O was rebuilt.

---

# 21. Relation to the previous transport–projection plan

DCRP43-QC proposed attacking

$$
[D_s,\Pi_{\mathcal G}]q.
$$

That remains possible after fixing a canonical local gauge projection.

However DCRP44 shows that this is **not the first structural question**.

Before constructing an arbitrary projection, one should first ask whether the scalar connection is intrinsically flat.

If either

$$
\mathcal C_{qz}\neq0
$$

or

$$
\mathcal F_{sz}\neq0,
$$

a native gauge-invariant residual already exists and no horizontal projection is needed to manufacture one.

Only the fully flat branch requires the more delicate replenishment/PFET attack.

Therefore the priority has changed.

---

# 22. Current strongest rank-two equality branch

After the gauge repair, the most rigid surviving scalar pancake state must satisfy at least:

$$
\boxed{
F_q\neq0,
}
$$

$$
\boxed{
\mathcal C_{qz}=0,
}
$$

$$
\boxed{
\mathcal F_{sz}=0,
}
$$

and therefore admits the unique periodic canonical gauge

$$
\boxed{
D_sq+k(s)q=0.
}
$$

In addition the broader DCRP chain still requires:

- rank exactly two;
- zero rank-three lift;
- zero plane-motion defect;
- zero shape-action defect;
- strict same-parent DSS return;
- finite-energy / unforced ancestry;
- DCRP-31 finite inward PFET matching layer;
- DCRP-35 recurrent finite-annulus strain/enstrophy supplier.

This is a narrower survivor than DCRP-42 had before the gauge audit.

---

# 23. What remains on the fully flat branch?

Once

$$
\mathcal C_{qz}
=
\mathcal F_{sz}
=
0,
$$

the scalar equation reduces canonically to

$$
D_sq+kq=0.
$$

But DCRP43-QC already proved that the same-parent root scaling cancels at the physical reconstruction level.

Therefore the remaining obstruction cannot be:

$$
\boxed{
\text{raw scalar multiplier alone}.
}
$$

The next genuinely native questions are now:

1. can the unique canonical flat scalar state be maintained by the same-parent finite annular vorticity reservoir required by DCRP-35?
2. can the same finite matching region simultaneously supply the inward PFET required by DCRP-31?
3. does exact flat scalar transport force a nontrivial spatial sheet turnover that is visible in gauge-invariant vorticity geometry?
4. do the PFET and strain suppliers induce a nonzero scalar-connection curvature, contradicting full flatness?

Question 4 is especially attractive.

It would convert the existing finite-annulus supplier into a direct contradiction with

$$
\mathcal F_{sz}=0
$$

or

$$
\mathcal C_{qz}=0.
$$

---

# 24. New next target

## DCRP45 — Finite-Annulus Supplier versus Scalar-Connection Flatness

The next autonomous step should attempt to prove:

> A nonzero recurrent finite-annulus strain/PFET supplier cannot preserve
>
> $$
> \mathcal C_{qz}
> =
> \mathcal F_{sz}
> =
> 0
> $$
>
> throughout a nontrivial strict rank-two periodic core, unless the flow falls into an already-known exact affine/shear model or an integrable tail branch.

A first route is to express

$$
F_q,
\quad
F_z,
\quad
\mathscr H
$$

in terms of physical derivatives of

$$
w,
\quad
q,
\quad
\Omega_h,
$$

then insert the DCRP-35 affine strain supplier

$$
S_{\rm ext}(s)
$$

and DCRP-31 finite PFET matching field.

If either supplier forces

$$
\partial_q
\left(
\frac{F_z+2a}{F_q}
\right)
\neq0
$$

or

$$
\mathcal F_{sz}\neq0,
$$

the canonical flat pancake branch closes.

If not, the surviving branch becomes an exact flat connection model and can be compared directly against known pancake/shear solutions.

---

# 25. Status ledger

## PROVED this round

### D44-P1

Exact gauge transformation:

$$
q'=q-g(z,s),
$$

$$
F'=F\circ T_g,
$$

$$
\mathscr H'
=
(\mathscr H+g_s+W_3g_z)\circ T_g.
$$

### D44-P2

Connection coefficient:

$$
A_z
=
\frac{F_z+2a}{F_q}
$$

transforms as

$$
A_z'
=
(A_z+g_z)\circ T_g.
$$

### D44-P3

Gauge-invariant normal-shear defect:

$$
\mathfrak C_{qz}
=
F_qF_{zq}
-
(F_z+2a)F_{qq}.
$$

### D44-P4

Local $G=0$ gauge exists on $F_q\neq0$ patch iff

$$
\mathcal C_{qz}=0.
$$

### D44-P5

Second coefficient

$$
A_s=\mathscr H-W_3A_z
$$

transforms as

$$
A_s'
=
(A_s+g_s)\circ T_g.
$$

### D44-P6

Gauge-covariant curvature:

$$
\mathcal F_{sz}
=
\partial_sA_z
-
\partial_zA_s
-
A_sA_{z,q}
+
A_zA_{s,q}.
$$

### D44-P7

Exact identity:

$$
A_{s,q}
=
k-W_3A_{z,q}.
$$

### D44-P8

Vanishing

$$
\mathcal C_{qz}
=
\mathcal F_{sz}
=
0
$$

is equivalent to existence of the periodic homogeneous DCRP-42 scalar gauge on the nondegenerate strict-Type-II patch.

### D44-P9

That periodic canonical gauge is unique.

---

# 26. Corrected STOP

The old STOP was:

$$
\boxed{
\text{raw scalar turnover is not an independent native tax}.
}
$$

The new result is stronger:

$$
\boxed{
\textbf{
STOP-D44:
The true canonical pancake equality branch is the gauge-flat scalar-connection class, not the bare }G=0\textbf{ class.}
}
$$

Any nonzero

$$
\mathcal C_{qz}
$$

or

$$
\mathcal F_{sz}
$$

is now a native residual.

The only branch requiring further replenishment analysis is

$$
\boxed{
\mathcal C_{qz}
=
\mathcal F_{sz}
=
0.
}
$$

---

# 27. One-line checkpoint

The DCRP42 gauge loophole has been repaired: the canonical pancake scalar eigenmode is exactly the unique periodic representative of a gauge-flat scalar connection, and the surviving rank-two branch is now reduced to the simultaneous vanishing of two native flatness defects plus the existing PFET/strain supplier constraints.

---

**End checkpoint:** DCRP44  
**Next autonomous step:** DCRP45 — Finite-Annulus PFET/Strain Supplier versus Scalar-Connection Flatness.
