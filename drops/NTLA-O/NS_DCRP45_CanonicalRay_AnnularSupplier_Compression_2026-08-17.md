# DCRP45 — Canonical-Ray Compression of the Annular Strain Supplier and the Signed Reproduction Frontier

**Series:** Independent Navier–Stokes Research Series  
**Date:** 2026-08-17  
**Status:** Proof-development checkpoint / cross-round compression  
**Immediate predecessor:** `NS_DCRP44_GaugeCovariant_PancakeConnection_Flatness_2026-08-17.md`

**Primary internal dependencies**
- DCRP-31 — finite-radius inward PFET matching layer
- DCRP-35 — finite-annulus enstrophy/affine-strain supplier
- DCRP-36 — affine-jet reproduction equation and five-dimensional phase frontier
- DCRP-40 — rank-two covariance/Floquet compression
- DCRP-41 — zero-shape-action moving pancake tensor
- DCRP-44 — gauge-flat scalar-connection classification

**External calibration**
- Agafontsev–Kuznetsov–Mailybaev, *Asymptotic solution for high vorticity regions in incompressible 3D Euler equations*, arXiv:1609.07782. Exact Euler pancake mechanisms combine shear with asymmetric straining and therefore show that nonzero local strain/pancake geometry is not itself contradictory.
- Enciso–Fernández–Meyer, *Vortex-sheet desingularization for three-dimensional ideal fluids*, arXiv:2607.19233. Thin sheet-like Euler vorticity organization is dynamically realizable.
- Seregin, *On potential Type II blowups for the Navier-Stokes equations*, arXiv:2606.29468. Current Type-II analysis continues to rely on Euler-scale local limits and Liouville-type exclusions.

No full Navier–Stokes regularity theorem is claimed.

---

# 0. Executive result

DCRP44 proposed the route

$$
\boxed{
\text{finite-annulus PFET/strain supplier}
\stackrel{?}{\Longrightarrow}
\mathcal C_{qz}\neq0
\ \vee\
\mathcal F_{sz}\neq0.
}
$$

This round shows that this implication is **false at leading affine order**.

A symmetric trace-free affine strain tensor relative to a fixed rank-two vorticity plane decomposes exactly into

$$
\boxed{
\mathrm{Sym}_0(3)
=
\underbrace{\mathbb R\,C_n}_{\text{canonical pancake ray}}
\oplus
\underbrace{\mathrm{Sym}_0(n^\perp)}_{\text{in-plane shape, 2D}}
\oplus
\underbrace{\{b\otimes n+n\otimes b:\ b\in n^\perp\}}_{\text{plane-motion/cross, 2D}},
}
$$

where

$$
\boxed{
C_n
=
P_n-2n\otimes n,
\qquad
P_n=I-n\otimes n.
}
$$

This is a $1+2+2=5$ dimensional orthogonal decomposition.

DCRP41 already proves that on the final **fixed-plane, zero-shape-action** equality branch, the total affine strain tensor must lie exactly on the one-dimensional canonical ray:

$$
\boxed{
A_{\rm tot}(s)
=
a(s)C_n.
}
$$

Therefore the four transverse affine degrees of freedom are not part of the final survivor:

- nonzero in-plane deviatoric component produces shape action;
- nonzero cross component produces plane motion.

DCRP35 localizes the necessary external strain supplier to a finite annulus. Once the near- and far-field errors are made small, the leading annular affine jet must therefore lie **arbitrarily close to the canonical pancake ray** on the final equality branch.

Hence:

$$
\boxed{
\textbf{the old five-dimensional affine-phase frontier collapses to a one-dimensional signed amplitude frontier.}
}
$$

This is the main new reduction.

The annular supplier does **not** automatically force the DCRP44 scalar-connection defects to be nonzero, because the pure canonical affine tensor

$$
a(s)C_n
$$

is fully compatible with the gauge-flat scalar-connection normal form

$$
F(q,z,s)=\beta(q,s)-2a(s)z,
$$

$$
\mathscr H(q,z,s)=k(s)q,
$$

for which

$$
\mathcal C_{qz}
=
\mathcal F_{sz}
=
0.
$$

So the direct “supplier destroys flatness” route is closed.

But the compression yields a stronger signed reproduction statement.

Project the DCRP36 annular jet equation

$$
A'+A
=
J_{\rm dil}
+
J_{\rm adv}
+
J_{\rm str}
$$

onto the canonical ray.

For

$$
a_A(s)
=
\frac{A(s):C_n}{6},
$$

define

$$
j_A(s)
=
\frac{
\left(
J_{\rm dil}
+
J_{\rm adv}
+
J_{\rm str}
\right):C_n
}{6}.
$$

On a fixed plane,

$$
\boxed{
a_A'+a_A=j_A.
}
$$

Because the final pancake equality branch has

$$
\boxed{
\frac1{S_0}
\int_0^{S_0}a(s)\,ds
=
\frac{2-3\gamma}{2}
>0,
}
$$

and the annular jet approximates the total canonical strain, the annular scalar projection has a positive period mean up to the controlled localization error.

Consequently its source satisfies a **signed**, not merely norm-level, reproduction requirement:

$$
\boxed{
\int_0^{S_0}j_A(s)\,ds
=
\int_0^{S_0}a_A(s)\,ds
>0
}
$$

after the supplier-alignment error is chosen sufficiently small.

Thus at least one of the canonical projections of

$$
J_{\rm dil},
\qquad
J_{\rm adv},
\qquad
J_{\rm str}
$$

must have positive signed period contribution.

The remaining frontier is therefore no longer a five-dimensional phase-cancellation problem.

It is:

$$
\boxed{
\textbf{
one-dimensional canonical-ray reproduction:
transport source
\ \vee\
internal annular stretching source.
}
}
$$

PFET remains a separate finite-annulus energy observable; no exact identity currently forces the signed affine-ray source to equal the DCRP31 pressure–energy flux.

The next step should therefore attack that **source-channel coupling**, not the already-closed affine geometry.

---

# 1. Fixed rank-two plane

Let

$$
n\in\mathbb S^2
$$

be the fixed normal of the rank-two vorticity plane.

Define

$$
\boxed{
P
=
I-n\otimes n.
}
\tag{1.1}
$$

The active vorticity satisfies

$$
\boxed{
\Omega\cdot n=0.
}
\tag{1.2}
$$

Define the canonical pancake tensor

$$
\boxed{
C
=
P-2n\otimes n.
}
\tag{1.3}
$$

Then

$$
C=C^T,
$$

$$
\operatorname{tr}C=0,
$$

and

$$
\boxed{
|C|_F^2=6.
}
\tag{1.4}
$$

---

# 2. Exact five-dimensional decomposition

Let

$$
A\in\mathrm{Sym}_0(3).
$$

Define its canonical scalar component

$$
\boxed{
a(A)
=
\frac{A:C}{6}.
}
\tag{2.1}
$$

Equivalently, since $\operatorname{tr}A=0$,

$$
\boxed{
a(A)
=
\frac12\operatorname{tr}(PAP)
=
-\frac12n\cdot An.
}
\tag{2.2}
$$

Define the in-plane deviatoric component

$$
\boxed{
S(A)
=
PAP-a(A)P.
}
\tag{2.3}
$$

Then

$$
S(A)n=0,
$$

$$
S(A)=S(A)^T,
$$

and its trace on $n^\perp$ is zero.

Define the cross/plane-motion vector

$$
\boxed{
b(A)
=
PAn
\in
n^\perp.
}
\tag{2.4}
$$

Then

$$
\boxed{
A
=
a(A)C
+
S(A)
+
b(A)\otimes n
+
n\otimes b(A).
}
\tag{2.5}
$$

## Theorem D45.1 — Canonical Pancake Decomposition

Equation (2.5) is the unique decomposition of any $A\in\mathrm{Sym}_0(3)$ into:

1. one canonical pancake amplitude;
2. a two-dimensional in-plane deviatoric tensor;
3. a two-dimensional cross/plane-motion vector.

Moreover the three summands are Frobenius orthogonal.

### Proof

The decomposition follows from splitting $A$ into the blocks defined by

$$
n^\perp\oplus\mathrm{span}\{n\}.
$$

Trace freeness forces the normal-normal coefficient to be minus the planar trace, producing the canonical tensor $C$.

The in-plane trace-free block has dimension two.

The off-diagonal block is determined by $b=PAn$ and has dimension two.

Orthogonality follows from support in distinct irreducible block types.

Dimension count:

$$
1+2+2=5
=
\dim\mathrm{Sym}_0(3).
$$

Therefore the decomposition is unique.

$$
\square
$$

---

# 3. What the core stretching functional actually sees

Let

$$
B(s)
=
\int_{B_{r_0}}
\Omega\otimes\Omega\,dy.
$$

Because

$$
\Omega\cdot n=0,
$$

we have

$$
Bn=0.
$$

Thus

$$
B=PBP.
$$

For the decomposition (2.5),

$$
\boxed{
A:B
=
a(A)\operatorname{tr}B
+
S(A):B.
}
\tag{3.1}
$$

The cross component

$$
b\otimes n+n\otimes b
$$

is invisible to the instantaneous vorticity-stretching work.

## Consequence

DCRP35's lower bound

$$
\int
(\Omega\cdot A\Omega)_+
$$

cannot by itself detect the plane-motion/cross component $b$.

That degree of freedom is controlled instead by DCRP41's moving-plane geometry.

This cleanly separates two observation channels:

$$
\boxed{
\text{enstrophy work}
\leftrightarrow
(a,S),
}
$$

$$
\boxed{
\text{plane motion}
\leftrightarrow
b.
}
$$

---

# 4. DCRP41 kills the four transverse components on the final equality branch

DCRP41 proves that zero shape action implies

$$
\boxed{
S_{\rm tot}(s)=0.
}
\tag{4.1}
$$

On a fixed-plane branch,

$$
n'(s)=0.
$$

Its normal equation gives

$$
\boxed{
P A_{\rm tot} n=0,
}
\tag{4.2}
$$

so

$$
\boxed{
b(A_{\rm tot})=0.
}
\tag{4.3}
$$

Therefore the total affine strain acting on the core is exactly

$$
\boxed{
A_{\rm tot}(s)
=
a(s)C.
}
\tag{4.4}
$$

This is not an approximation.

It is the exact DCRP41 zero-shape, fixed-plane equality tensor.

## Theorem D45.2 — Final Affine Geometry Is One-Dimensional

On the fixed-plane zero-shape-action rank-two equality branch,

$$
\boxed{
A_{\rm tot}(s)\in\mathbb R C
}
$$

for every $s$.

Thus all four transverse degrees of freedom in $\mathrm{Sym}_0(3)$ have already been removed before the DCRP44 scalar-flatness analysis begins.

---

# 5. Mean canonical amplitude is fixed and positive

DCRP40/41 gives

$$
\boxed{
c_\gamma
=
2-3\gamma
>0,
}
\tag{5.1}
$$

and

$$
\boxed{
\frac1{S_0}
\int_0^{S_0}
a(s)\,ds
=
\frac{c_\gamma}{2}.
}
\tag{5.2}
$$

Hence

$$
\boxed{
\overline a
=
\frac{2-3\gamma}{2}.
}
\tag{5.3}
$$

In the strict window

$$
\frac25<\gamma<\frac12,
$$

$$
\boxed{
\frac14
<
\overline a
<
\frac25.
}
\tag{5.4}
$$

Therefore the final fixed-plane pancake branch has a strictly positive average canonical extensional amplitude.

---

# 6. DCRP35 external annular source

DCRP35 decomposes the strain acting on a sufficiently small recurrent core into:

$$
\boxed{
S_{\rm tot}
=
H_{\rm ann}
+
E_{\rm loc},
}
\tag{6.1}
$$

where $H_{\rm ann}$ is generated by a fixed finite annulus and $E_{\rm loc}$ collects controlled near-field, far-field, overlap, and Taylor-remainder contributions.

The annular field is harmonic on the core and admits

$$
\boxed{
H_{\rm ann}(x,s)
=
A_{\rm ann}(s)
+
R_{\rm ann}(x,s),
}
\tag{6.2}
$$

with

$$
A_{\rm ann}(s)
\in
\mathrm{Sym}_0(3).
$$

The DCRP35 compact-class construction allows the non-annular and Taylor-remainder contributions to be made a prescribed small fraction of the supplier gap by choosing the core/annulus separation parameters.

For the present structural analysis, encode that control as

$$
\boxed{
\|A_{\rm tot}(s)-A_{\rm ann}(s)\|_F
\le
\varepsilon(s),
}
\tag{6.3}
$$

with

$$
\|\varepsilon\|_{L^\infty_s}
$$

as small as permitted by the declared compact supplier class.

This is the only approximation used in the canonical-ray compression theorem below.

---

# 7. Canonical-ray compression of the annular jet

Apply the orthogonal projection

$$
\Pi_C A
=
\frac{A:C}{6}C.
$$

Let

$$
A_{\rm ann}
=
a_{\rm ann}C
+
S_{\rm ann}
+
b_{\rm ann}\otimes n
+
n\otimes b_{\rm ann}.
$$

Since

$$
A_{\rm tot}=aC,
$$

equation (6.3) gives

$$
\boxed{
\left|
A_{\rm ann}
-
aC
\right|_F
\le
\varepsilon.
}
\tag{7.1}
$$

By orthogonality,

$$
\boxed{
|S_{\rm ann}|_F^2
+
2|b_{\rm ann}|^2
+
6|a_{\rm ann}-a|^2
\le
\varepsilon^2.
}
\tag{7.2}
$$

Hence:

$$
\boxed{
|S_{\rm ann}|
\le
\varepsilon,
}
\tag{7.3}
$$

$$
\boxed{
|b_{\rm ann}|
\le
\frac{\varepsilon}{\sqrt2},
}
\tag{7.4}
$$

and

$$
\boxed{
|a_{\rm ann}-a|
\le
\frac{\varepsilon}{\sqrt6}.
}
\tag{7.5}
$$

## Theorem D45.3 — Annular Supplier Canonical-Ray Concentration

On the final fixed-plane zero-shape equality branch, any finite-annulus affine supplier approximating the total core strain to accuracy $\varepsilon$ must lie within distance $\varepsilon$ of the one-dimensional canonical pancake ray.

Therefore the unresolved five-dimensional annular jet phase freedom collapses, in the equality limit, to one scalar amplitude.

---

# 8. Why this closes the direct DCRP44 supplier-versus-flatness route

DCRP44's flat scalar connection requires, in its canonical periodic gauge,

$$
\boxed{
F_z=-2a(s),
}
\tag{8.1}
$$

and

$$
\boxed{
\mathscr H=k(s)q.
}
\tag{8.2}
$$

This is perfectly compatible with the canonical affine tensor

$$
\boxed{
A_{\rm pan}=a(s)C.
}
\tag{8.3}
$$

Indeed take locally

$$
\boxed{
F(q,z,s)
=
\beta(q,s)-2a(s)z
}
\tag{8.4}
$$

with

$$
\beta_q\neq0.
$$

Then

$$
F_z+2a=0,
$$

so

$$
A_z=0,
$$

$$
\mathcal C_{qz}=0.
$$

Choose the scalar primitive

$$
\mathscr H=k(s)q.
$$

Then

$$
A_s=kq
$$

has no explicit $z$ dependence, hence

$$
\boxed{
\mathcal F_{sz}=0.
}
\tag{8.5}
$$

Thus a nonzero canonical pancake affine strain and a gauge-flat scalar connection coexist algebraically.

## Theorem D45.4 — Affine Supplier Does Not Force Scalar-Connection Nonflatness

The implication

$$
\boxed{
A_{\rm ann}\neq0
\Longrightarrow
\mathcal C_{qz}\neq0
\ \vee\
\mathcal F_{sz}\neq0
}
$$

is false at leading affine order.

The canonical one-dimensional supplier ray is compatible with

$$
\boxed{
\mathcal C_{qz}
=
\mathcal F_{sz}
=
0.
}
$$

This closes the direct DCRP45 contradiction attempt.

---

# 9. External calibration of the NO-GO

This negative result is consistent with known exact Euler pancake mechanisms.

Agafontsev–Kuznetsov–Mailybaev construct exact Euler solutions combining:

- shear;
- linear straining;
- thin pancake vorticity.

Thus one should not expect “nonzero linear strain + planar shear” alone to violate the local fluid equations.

The DCRP branch must be closed using the additional constraints that the external calibration lacks:

- strict Type-II DSS return;
- finite-energy same-parent ancestry;
- recurrent finite-annulus self-supply;
- inward PFET matching;
- scalar-connection flatness;
- absence of shape/plane defects.

---

# 10. The useful result: five dimensions become one

DCRP36's affine source lives in

$$
\mathrm{Sym}_0(3),
$$

a five-dimensional fiber.

Before DCRP41 the unresolved problem involved phase/alignment of all five components.

On the final fixed-plane zero-shape branch, DCRP45 shows:

$$
\boxed{
\mathrm{Sym}_0(3)
\longrightarrow
\mathbb R C
}
$$

up to the explicitly controlled annular localization error.

Thus the final supplier is characterized, to leading order, by the scalar function

$$
\boxed{
a_{\rm ann}(s).
}
\tag{10.1}
$$

This is a major reduction of the DCRP36 phase frontier.

---

# 11. Positive mean survives the annular approximation

From (7.5),

$$
|a_{\rm ann}-a|
\le
\frac{\varepsilon}{\sqrt6}.
$$

Therefore

$$
\left|
\frac1{S_0}
\int_0^{S_0}
a_{\rm ann}(s)\,ds
-
\frac{c_\gamma}{2}
\right|
\le
\frac{
\|\varepsilon\|_{L^\infty_s}
}{
\sqrt6
}.
$$

If the supplier decomposition is chosen so that

$$
\boxed{
\|\varepsilon\|_{L^\infty_s}
<
\frac{\sqrt6}{4}c_\gamma,
}
\tag{11.1}
$$

then

$$
\boxed{
\frac1{S_0}
\int_0^{S_0}
a_{\rm ann}(s)\,ds
>
\frac{c_\gamma}{4}
>0.
}
\tag{11.2}
$$

Thus the annular supplier is not merely nonzero in norm.

It has a **positive signed canonical-ray mean**.

---

# 12. Projected affine reproduction equation

DCRP36 gives the exact annular affine-jet reproduction equation

$$
\boxed{
A_{\rm ann}'
+
A_{\rm ann}
=
J_{\rm dil}
+
J_{\rm adv}
+
J_{\rm str}.
}
\tag{12.1}
$$

Because the plane is fixed,

$$
C'=0.
$$

Project onto $C$:

$$
\boxed{
a_{\rm ann}
=
\frac{
A_{\rm ann}:C
}{6}.
}
\tag{12.2}
$$

Define

$$
\boxed{
j_{\rm dil}
=
\frac{
J_{\rm dil}:C
}{6},
}
\tag{12.3}
$$

$$
\boxed{
j_{\rm adv}
=
\frac{
J_{\rm adv}:C
}{6},
}
\tag{12.4}
$$

$$
\boxed{
j_{\rm str}
=
\frac{
J_{\rm str}:C
}{6}.
}
\tag{12.5}
$$

Then exactly

$$
\boxed{
a_{\rm ann}'
+
a_{\rm ann}
=
j_{\rm dil}
+
j_{\rm adv}
+
j_{\rm str}.
}
\tag{12.6}
$$

This is the one-dimensional canonical-ray reproduction equation.

---

# 13. Signed period identity

Since $A_{\rm ann}$ is DSS-periodic,

$$
a_{\rm ann}(S_0)
=
a_{\rm ann}(0).
$$

Integrating (12.6),

$$
\boxed{
\int_0^{S_0}
\left(
j_{\rm dil}
+
j_{\rm adv}
+
j_{\rm str}
\right)ds
=
\int_0^{S_0}
a_{\rm ann}(s)\,ds.
}
\tag{13.1}
$$

Under (11.1),

$$
\boxed{
\int_0^{S_0}
\left(
j_{\rm dil}
+
j_{\rm adv}
+
j_{\rm str}
\right)ds
>
\frac{
c_\gamma S_0
}{4}.
}
\tag{13.2}
$$

This is stronger than the old statement that some reproduction source has nonzero $L^2$ norm.

It gives a **positive signed canonical-ray source budget**.

---

# Theorem D45.5 — Positive Signed Canonical-Ray Reproduction

On the fixed-plane zero-shape equality branch, after choosing the DCRP35 supplier decomposition with error satisfying (11.1),

$$
\boxed{
\int_0^{S_0}
\left(
j_{\rm dil}
+
j_{\rm adv}
+
j_{\rm str}
\right)ds
>
0.
}
$$

Hence at least one of the three source channels has positive period integral:

$$
\boxed{
\int j_{\rm dil}>0
\quad\vee\quad
\int j_{\rm adv}>0
\quad\vee\quad
\int j_{\rm str}>0.
}
\tag{13.3}
$$

### Proof

If all three period integrals were nonpositive, their sum would be nonpositive, contradicting (13.2).

$$
\square
$$

---

# 14. Interpretation of the three remaining source channels

The DCRP36 source decomposition now has a much sharper meaning.

## Canonical dilation-shell transport

$$
j_{\rm dil}
$$

is generated by the cutoff-shell part of the similarity dilation.

## Canonical advective transport

$$
j_{\rm adv}
$$

is generated by the annular material advection through the fixed source window.

## Canonical internal stretching

$$
j_{\rm str}
$$

is generated by nonlinear vorticity stretching inside the annulus.

At least one must contribute positively, in a signed sense, to rebuilding the canonical pancake strain every DSS period.

Thus the final source problem is:

$$
\boxed{
\text{signed canonical transport}
\ \vee\
\text{signed canonical internal stretching}.
}
$$

The five-dimensional orientation/phase problem has largely disappeared.

---

# 15. One-dimensional reproduction action

Define

$$
\boxed{
j_a
=
a_{\rm ann}'
+
a_{\rm ann}.
}
\tag{15.1}
$$

Periodicity gives

$$
\boxed{
\int_0^{S_0}
j_a^2ds
=
\int_0^{S_0}
\left(
(a_{\rm ann}')^2
+
a_{\rm ann}^2
\right)ds.
}
\tag{15.2}
$$

By Jensen,

$$
\int_0^{S_0}
a_{\rm ann}^2ds
\ge
S_0
\left(
\frac1{S_0}
\int_0^{S_0}
a_{\rm ann}ds
\right)^2.
$$

Under (11.1),

$$
\boxed{
\int_0^{S_0}
j_a^2ds
>
\frac{
c_\gamma^2S_0
}{16}.
}
\tag{15.3}
$$

Thus the annular canonical-ray supplier pays a fixed one-dimensional reproduction action.

This is the scalar projection of the DCRP36 five-dimensional action.

---

# 16. Why this still does not prove contradiction

Critical DSS scaling can support recurrent normalized affine moments without violating a raw finite-energy summability budget.

DCRP36 already proved that size-only affine taxation is critical and summable in physical scale.

The present reduction removes most orientation freedom, but it does not yet show that the signed one-dimensional source budget depletes across returns.

Therefore

$$
\boxed{
\text{positive signed canonical source per normalized period}
}
$$

is not yet a global contradiction.

A same-parent return-depletion or coupling theorem is still required.

---

# 17. PFET remains independent at the current theorem level

DCRP31 gives a finite-annulus period-averaged inward pressure–kinetic energy flux:

$$
\boxed{
\mathcal F_{\rm PFET}<0
}
$$

on a nontrivial set of finite radii, and a uniform annular aggregate gap on the compact strict class.

DCRP45 gives a positive canonical-ray affine-source integral:

$$
\boxed{
\int
(j_{\rm dil}+j_{\rm adv}+j_{\rm str})ds
>0.
}
$$

These are different functionals.

No established identity currently gives

$$
\boxed{
j_{\rm adv}
\equiv
-\mathcal F_{\rm PFET},
}
$$

or any fixed-sign equality between the affine-source moment and pressure–energy flux.

Therefore:

$$
\boxed{
\text{PFET positivity/inwardness}
}
$$

and

$$
\boxed{
\text{canonical affine reproduction}
}
$$

remain two simultaneous finite-annulus obligations rather than one already-merged tax.

This is an important STOP against overclaiming.

---

# 18. A common finite supplier package

DCRP35 already notes that the PFET witness and affine/enstrophy supplier need not occur at exactly the same radius, but they can be enclosed in one fixed finite normalized annular package.

Thus define a common supplier annulus

$$
\boxed{
\mathcal A_\ast
=
\{R_-<|y|<R_+\}
}
\tag{18.1}
$$

large enough to contain:

1. the DCRP31 inward PFET matching region;
2. the DCRP35 leading affine-strain supplier region;
3. the cutoff transition shells used in the DCRP36 reproduction equation.

Then the final rank-two equality branch contains within one finite normalized package:

$$
\boxed{
\text{inward energy supply}
}
$$

and

$$
\boxed{
\text{positive signed canonical-ray strain reproduction}.
}
$$

This is now the correct finite-domain target for a same-parent coupling theorem.

---

# 19. Updated final rank-two branch

After DCRP45, the most rigid surviving rank-two branch can be written:

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
\text{fixed plane}
\\
&+
\text{zero covariance-shape action}
\\
&+
\text{gauge-flat scalar connection}
\\
&+
\text{finite inward PFET matching}
\\
&+
\text{finite annular supplier asymptotic to }
a_{\rm ann}(s)C
\\
&+
\text{positive signed canonical-ray reproduction}.
\end{aligned}
}
$$

All four transverse affine-jet phase directions have been pushed into already-declared defect branches or the controlled localization error.

The survivor is therefore much closer to a one-dimensional pancake-amplitude recurrence problem.

---

# 20. New invariant branch diagram

The annular supplier now splits as:

$$
\boxed{
A_{\rm ann}
=
a_{\rm ann}C
+
A_{\rm ann}^{\perp}.
}
$$

Then:

## Branch A — transverse supplier survives

$$
\boxed{
A_{\rm ann}^{\perp}\not\to0.
}
$$

This must be balanced by other strain contributions to preserve the exact final affine geometry and therefore feeds:

- shape-action residual;
- plane-motion residual;
- non-annular cancellation carrier.

It is no longer the pure equality branch.

## Branch B — canonical-ray concentration

$$
\boxed{
A_{\rm ann}^{\perp}\to0.
}
$$

Then only

$$
a_{\rm ann}(s)
$$

survives and obeys the signed scalar reproduction ledger.

This is the final equality branch.

---

# 21. The direct flatness attack is now closed

DCRP44 asked whether a finite annular supplier could itself force

$$
\mathcal C_{qz}\neq0
$$

or

$$
\mathcal F_{sz}\neq0.
$$

DCRP45 answers:

$$
\boxed{
\textbf{No, not at leading affine order.}
}
$$

The canonical pancake ray is simultaneously compatible with:

- positive planar stretching;
- zero shape action;
- fixed plane;
- scalar-connection flatness.

Therefore future work should not continue trying to prove a purely algebraic implication

$$
A_{\rm ann}\neq0
\Rightarrow
\text{scalar curvature}.
$$

That route is closed.

---

# 22. What information is still missing?

The missing information is **source coupling**.

We now know:

$$
\boxed{
\int
j_a
>
0,
}
$$

and independently:

$$
\boxed{
\text{inward PFET}
>0
}
$$

in the appropriate sign convention.

But we do not know whether the same-parent dynamics can satisfy both indefinitely.

The natural next variables are therefore joint source moments on the common finite annulus:

$$
\boxed{
\left(
\mathcal F_{\rm PFET},
j_{\rm dil},
j_{\rm adv},
j_{\rm str}
\right).
}
$$

The next theorem should seek a sign, phase, or conservation coupling among them.

---

# 23. Candidate coupling routes

## Route 1 — Advective-source / PFET coupling

Both

$$
j_{\rm adv}
$$

and PFET involve finite-annulus transport by $V$.

Try to integrate by parts in the annular moment formula and identify a pressure/kinetic-energy piece or a boundary current.

Goal:

$$
\boxed{
j_{\rm adv}^{C}
=
\text{PFET-correlated term}
+
\text{controlled residual}.
}
$$

## Route 2 — Internal-stretching recursion

If

$$
j_{\rm str}
$$

supplies the canonical ray, then the annular vorticity internally stretches itself to reproduce the strain that stretches the inner core.

This suggests a nested supplier recursion.

Goal:

$$
\boxed{
j_{\rm str}>0
\Longrightarrow
\text{next-scale strain source}
\ \vee\
\text{critical exact eigenmode}.
}
$$

## Route 3 — Dilation-shell source

The signed

$$
j_{\rm dil}
$$

comes entirely from cutoff-shell transport.

A persistent positive mean may imply unavoidable motion through the finite annular package.

Goal:

$$
\boxed{
\int j_{\rm dil}>0
\Longrightarrow
\text{finite transition carrier}.
}
$$

These are now three scalar source channels rather than a five-dimensional phase problem.

---

# 24. NTLA-O interpretation

This round gives another concrete NTLA-O compression.

DCRP35 observes a five-dimensional external affine tensor.

DCRP41 applies a finer structural observer:

$$
\boxed{
A
\mapsto
(a,S,b).
}
$$

The equality branch imposes

$$
S=0,
$$

$$
b=0.
$$

Thus four affine distinctions are already assigned to defect branches.

The final observer quotient leaves only

$$
\boxed{
a.
}
$$

The NTLA-O observer tower is therefore:

$$
\boxed{
\mathrm{Sym}_0(3)
\rightarrow
(a,S,b)
\rightarrow
a
}
$$

on the final rank-two equality route.

This is exactly a case where increasing structural resolution does not create a new contradiction but compresses the survivor to a lower-dimensional realizability problem.

---

# 25. Status ledger

## PROVED this round

### D45-P1 — Five-dimensional orthogonal pancake decomposition

$$
A=aC+S+b\otimes n+n\otimes b.
$$

### D45-P2 — Enstrophy work sees only $(a,S)$

$$
A:B
=
a\,\operatorname{tr}B
+
S:B.
$$

### D45-P3 — Final fixed-plane zero-shape total affine tensor is one-dimensional

$$
A_{\rm tot}=aC.
$$

### D45-P4 — Annular supplier concentration

If the finite-annulus affine jet approximates the total core strain to error $\varepsilon$, then its four-dimensional transverse component has norm at most $\varepsilon$.

### D45-P5 — Direct supplier-to-scalar-curvature implication is false

A pure canonical affine supplier is compatible with

$$
\mathcal C_{qz}
=
\mathcal F_{sz}
=
0.
$$

### D45-P6 — Positive signed canonical-ray source

After sufficiently accurate annular localization,

$$
\int_0^{S_0}
(j_{\rm dil}+j_{\rm adv}+j_{\rm str})ds
>0.
$$

### D45-P7 — One-dimensional reproduction-action gap

$$
\int_0^{S_0}
|a_{\rm ann}'+a_{\rm ann}|^2ds
$$

has a strictly positive lower bound determined by $c_\gamma$ and the supplier-alignment tolerance.

---

# 26. DOWNGRADED / CLOSED ROUTES

## Closed direct route

$$
\boxed{
\text{nonzero finite-annulus affine supplier}
\Rightarrow
\text{DCRP44 nonflatness}
}
$$

is false.

## Reduced old frontier

The DCRP36 five-dimensional phase-coherence problem is no longer the correct final equality frontier on the fixed-plane zero-shape branch.

It collapses to one scalar canonical amplitude plus controlled transverse error.

---

# 27. Current STOP

$$
\boxed{
\textbf{
STOP-D45:
Finite-annulus strain supply is compatible with scalar-connection flatness; the final rank-two survivor reduces from a five-dimensional affine phase problem to a one-dimensional signed canonical-ray reproduction problem.
}
}
$$

---

# 28. Next autonomous step

## DCRP46 — Canonical-Ray Source Coupling

**Working title**

> **PFET–Affine Source Coupling, Canonical Advective Moment, and Annular Replenishment Dichotomy**

Primary target:

derive the canonical-ray projections

$$
j_{\rm dil},
\qquad
j_{\rm adv},
\qquad
j_{\rm str}
$$

more explicitly in physical/annular variables and test whether:

1. $j_{\rm adv}$ necessarily couples to the DCRP31 inward PFET current;
2. $j_{\rm dil}$ forces a finite annular transition carrier;
3. $j_{\rm str}$ creates a nested supplier recursion or an exact critical pancake eigenmode.

Desired result:

$$
\boxed{
\text{PFET-coupled transport}
\ \vee\
\text{finite transition}
\ \vee\
\text{nested internal supplier}
\ \vee\
\text{exact model branch}.
}
$$

Any one of these would further narrow the final rank-two survivor.

---

# 29. One-line checkpoint

The affine supplier does not break scalar flatness, but the combined DCRP35/41 geometry collapses its five-dimensional phase freedom to one positive canonical pancake amplitude whose periodic reproduction must be supplied by a signed finite-annulus transport/stretching channel.

---

**End checkpoint:** DCRP45  
**Next:** DCRP46 — PFET/Affine Canonical-Ray Source Coupling.
