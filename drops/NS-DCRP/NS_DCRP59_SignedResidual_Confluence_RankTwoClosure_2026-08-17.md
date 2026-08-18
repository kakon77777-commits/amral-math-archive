# DCRP59 — Signed Residual-Channel Confluence and Rank-Two Equality Closure

**Series:** Independent Navier–Stokes Research Series  
**Date:** 2026-08-17  
**Status:** Proof-development checkpoint / residual-confluence round  
**Immediate predecessor:** `NS_DCRP58_CylindricalTail_Elimination_OuterEqualityClosure_2026-08-17.md`

**Primary internal dependencies**
- DCRP-35 — strict-DSS enstrophy ledger and inward enstrophy turnover
- DCRP-38 — exact covariance ledger and residual split
- DCRP-54 — unavoidable localized X72 visibility leakage
- DCRP-55/56 — finite compensation requires isotropic rank-three covariance lift
- DCRP-57 — isotropic covariance residual gap
- DCRP-58 — globally transparent fixed-plane tail eliminated
- X72 Round42–43 — visible/invisible vorticity-stress projection and global realizability frontier

**External calibration checked before this round**
- Dongho Chae & Tai-Peng Tsai, *On discretely self-similar solutions of the Euler equations*, arXiv:1304.7414.
- Liutang Xue, *Discretely self-similar singular solutions for the incompressible Euler equations*, arXiv:1408.6619.
- Gregory Seregin, *On potential Type II blowups for the Navier-Stokes equations*, arXiv:2606.29468.

These references calibrate the DSS Euler / Type-II setting only. No full Navier–Stokes regularity theorem is claimed.

---

# 0. Executive result

DCRP58 closed the globally transparent fixed-plane tail.

Therefore any exact compensation of the recurrent DCRP54 X72 visibility leakage must occur through the **finite compensation branch**.

DCRP55/56 show that finite full compensation forces the cumulative vorticity covariance to become isotropic rank three:

$$
\boxed{
B(s)=\rho(s)I,
\qquad
\rho(s)>0.
}
$$

Moreover the isotropic covariance obeys

$$
\boxed{
\rho(s)
\ge
\frac12 Z_{\rm in}(s),
}
$$

where

$$
\boxed{
Z_{\rm in}(s)
=
\int
\chi_{\rm in}(y)
|\Omega(y,s)|^2dy
}
$$

is the recurrent inner rank-two vorticity mass.

DCRP38 gives the exact covariance ledger

$$
\boxed{
B'
=
AB+BA
-
c_\gamma B
+
R_B,
}
$$

with

$$
\boxed{
c_\gamma=2-3\gamma>0,
}
$$

and the exact residual split

$$
\boxed{
R_B
=
R_B^{na}
+
R_B^{tr},
}
$$

where

$$
\boxed{
R_B^{na}
=
\int
\phi
\left[
E C_\Omega
+
C_\Omega E
\right]dy,
}
$$

and

$$
\boxed{
R_B^{tr}
=
\int
(W\cdot\nabla\phi)
C_\Omega\,dy.
}
$$

Here

$$
C_\Omega=\Omega\otimes\Omega,
$$

$$
S=A+E,
$$

and $\phi$ is the fixed covariance-core cutoff.

For the isotropic state,

$$
\boxed{
R_B
=
\left[
\rho'
+
c_\gamma\rho
\right]I
-
2\rho A.
}
$$

Taking the trace and integrating one period gives the exact positive budget

$$
\boxed{
\int_0^{S_0}
\operatorname{tr}R_B\,ds
=
3c_\gamma
\int_0^{S_0}
\rho(s)\,ds.
}
$$

Using

$$
\rho\ge\frac12Z_{\rm in},
$$

$$
\boxed{
\int_0^{S_0}
\operatorname{tr}R_B\,ds
\ge
\frac32c_\gamma
\int_0^{S_0}
Z_{\rm in}(s)\,ds.
}
$$

The key advance of DCRP59 is that this **signed** positive residual cannot hide through cancellation between the two DCRP38 mechanisms.

Since

$$
\operatorname{tr}R_B
=
\operatorname{tr}R_B^{na}
+
\operatorname{tr}R_B^{tr},
$$

at least one of the two period integrals must satisfy

$$
\boxed{
\int_0^{S_0}
\operatorname{tr}R_B^{na}\,ds
\ge
\frac34
c_\gamma
\int_0^{S_0}
Z_{\rm in}\,ds,
}
$$

or

$$
\boxed{
\int_0^{S_0}
\operatorname{tr}R_B^{tr}\,ds
\ge
\frac34
c_\gamma
\int_0^{S_0}
Z_{\rm in}\,ds.
}
$$

These traces have direct dynamical meanings.

For the non-affine channel,

$$
\boxed{
\operatorname{tr}R_B^{na}
=
2
\int
\phi\,
\Omega\cdot E\Omega\,dy.
}
$$

Hence one branch is the quantitative positive non-affine vortex-stretching gap

$$
\boxed{
\int_0^{S_0}
\int
\phi\,
\Omega\cdot E\Omega
\,dy\,ds
\ge
\frac38
(2-3\gamma)
\int_0^{S_0}
Z_{\rm in}(s)\,ds.
}
$$

For the turnover channel,

$$
\boxed{
\operatorname{tr}R_B^{tr}
=
\int
(W\cdot\nabla\phi)
|\Omega|^2dy.
}
$$

If the covariance cutoff is chosen radial and nonincreasing,

$$
\phi=\phi(R),
\qquad
\phi'(R)\le0,
$$

then by coarea and the DCRP35 enstrophy flux

$$
\boxed{
\mathcal J_\omega(R)
=
\int_0^{S_0}
\int_{\partial B_R}
\frac12|\Omega|^2
W\cdot n\,dS\,ds,
}
$$

one has

$$
\boxed{
\int_0^{S_0}
\operatorname{tr}R_B^{tr}ds
=
2
\int_0^\infty
[-\phi'(R)]
[-\mathcal J_\omega(R)]
\,dR.
}
$$

Thus the turnover branch forces the quantitative smoothed inward-enstrophy gap

$$
\boxed{
\int_0^\infty
[-\phi'(R)]
\mathcal J_{\omega,\rm in}(R)
\,dR
\ge
\frac38
(2-3\gamma)
\int_0^{S_0}
Z_{\rm in}(s)\,ds.
}
$$

Therefore finite X72 visibility compensation has now been fully absorbed into two **already-existing DCRP defect routes**:

$$
\boxed{
\textbf{
positive non-affine strain work}
}
$$

or

$$
\boxed{
\textbf{
positive inward enstrophy turnover}.
}
$$

No third zero-residual finite equality state remains.

Combining D54–D59 produces the main confluence theorem of this checkpoint:

> A nonzero recurrent inner rank-two null-envelope core cannot be extended to a globally transparent zero-residual rank-two equality state.
>
> If the X72 visibility leak is left uncanceled, the solution is already in the X72 projection-defect branch.
>
> If it is compensated finitely, covariance becomes rank three and the exact covariance ledger forces a quantitative positive non-affine-strain or inward-enstrophy-turnover channel.
>
> If one tries to compensate through a fixed-plane transparent tail, DCRP58 rules that tail out under the strict DSS sublinear velocity-energy law.

Thus the long DCRP rank-two equality route has reached a genuine **branch confluence**:

$$
\boxed{
\text{rank-two local equality}
}
$$

can continue globally only by entering one of

$$
\boxed{
\text{X72 visibility defect},
}
$$

$$
\boxed{
\text{non-affine strain defect},
}
$$

$$
\boxed{
\text{inward covariance/enstrophy turnover},
}
$$

or a higher-rank transition already outside the rank-two equality class.

This is a reusable rank-two closure theorem for the larger RMRM proof tree.

It is still not a complete Navier–Stokes regularity proof: the confluence theorem routes the survivor into previously identified nonzero defect branches; those branches must still be globally closed or shown incompatible with the original NS blowup ancestry.

---

# 1. Exact covariance residual split

DCRP38 chooses a fixed cutoff

$$
\boxed{
0\le\phi\le1,
\qquad
\phi\in C_c^\infty,
}
\tag{1.1}
$$

and defines

$$
\boxed{
B(s)
=
\int
\phi
\Omega\otimes\Omega\,dy.
}
\tag{1.2}
$$

Write the strain as

$$
\boxed{
S(y,s)=A(s)+E(y,s),
}
\tag{1.3}
$$

with

$$
A(s)\in\mathrm{Sym}_0(3).
$$

Then the exact covariance ledger is

$$
\boxed{
B'
=
AB+BA
-
c_\gamma B
+
R_B,
}
\tag{1.4}
$$

where

$$
\boxed{
c_\gamma
=
2-3\gamma>0,
}
\tag{1.5}
$$

and

$$
\boxed{
R_B
=
R_B^{na}
+
R_B^{tr}.
}
\tag{1.6}
$$

The two mechanisms are

$$
\boxed{
R_B^{na}
=
\int
\phi
\left[
E(\Omega\otimes\Omega)
+
(\Omega\otimes\Omega)E
\right]dy,
}
\tag{1.7}
$$

and

$$
\boxed{
R_B^{tr}
=
\int
(W\cdot\nabla\phi)
\Omega\otimes\Omega\,dy.
}
\tag{1.8}
$$

---

# 2. Insert the finite X72 compensation state

DCRP55/56 prove that complete finite angular compensation of the D54 visibility leakage requires

$$
\boxed{
B(s)=\rho(s)I.
}
\tag{2.1}
$$

Strictly speaking one chooses the DCRP38 covariance cutoff so that it contains the finite inner+compensation package whose cumulative dyadic moment is isotropized.

DCRP56 gives

$$
\boxed{
\rho(s)
\ge
\frac12Z_{\rm in}(s),
}
\tag{2.2}
$$

where

$$
\boxed{
Z_{\rm in}(s)
=
\int
\chi_{\rm in}
|\Omega|^2dy.
}
\tag{2.3}
$$

The inner core is recurrent and nonzero, so

$$
\boxed{
\int_0^{S_0}
Z_{\rm in}(s)ds>0.
}
\tag{2.4}
$$

---

# 3. Exact isotropic residual formula

For

$$
B=\rho I,
$$

$$
B'=\rho'I,
$$

and

$$
AB+BA=2\rho A.
$$

Equation (1.4) gives

$$
\boxed{
R_B
=
(\rho'+c_\gamma\rho)I
-
2\rho A.
}
\tag{3.1}
$$

Taking the trace,

$$
\boxed{
\operatorname{tr}R_B
=
3(\rho'+c_\gamma\rho).
}
\tag{3.2}
$$

Because $\rho$ is $S_0$-periodic,

$$
\boxed{
\int_0^{S_0}\rho' ds=0.
}
\tag{3.3}
$$

Therefore:

## Theorem D59.1 — Positive Signed Total Residual Budget

$$
\boxed{
\int_0^{S_0}
\operatorname{tr}R_B\,ds
=
3c_\gamma
\int_0^{S_0}
\rho(s)ds.
}
\tag{3.4}
$$

Using (2.2),

$$
\boxed{
\int_0^{S_0}
\operatorname{tr}R_B\,ds
\ge
\frac32
c_\gamma
\int_0^{S_0}
Z_{\rm in}(s)ds.
}
\tag{3.5}
$$

This is a **signed** positive period budget, not merely a norm lower bound.

---

# 4. Signed residual-channel dichotomy

Define

$$
\boxed{
\mathfrak R_{na}
=
\int_0^{S_0}
\operatorname{tr}R_B^{na}(s)ds,
}
\tag{4.1}
$$

and

$$
\boxed{
\mathfrak R_{tr}
=
\int_0^{S_0}
\operatorname{tr}R_B^{tr}(s)ds.
}
\tag{4.2}
$$

Then

$$
\boxed{
\mathfrak R_{na}
+
\mathfrak R_{tr}
=
3c_\gamma
\int_0^{S_0}\rho ds.
}
\tag{4.3}
$$

If both were strictly less than half of the right side, their sum would be smaller than the right side.

Therefore:

## Theorem D59.2 — Signed Residual-Channel Confluence

At least one of

$$
\boxed{
\mathfrak R_{na}
\ge
\frac32
c_\gamma
\int_0^{S_0}\rho ds
}
\tag{4.4}
$$

or

$$
\boxed{
\mathfrak R_{tr}
\ge
\frac32
c_\gamma
\int_0^{S_0}\rho ds
}
\tag{4.5}
$$

must hold.

Using

$$
\rho\ge\frac12Z_{\rm in},
$$

at least one satisfies

$$
\boxed{
\mathfrak R_{\bullet}
\ge
\frac34
c_\gamma
\int_0^{S_0}
Z_{\rm in}(s)ds.
}
\tag{4.6}
$$

This is the central DCRP59 dichotomy.

---

# 5. Non-affine trace identity

From (1.7),

$$
\begin{aligned}
\operatorname{tr}R_B^{na}
&=
\int
\phi
\operatorname{tr}
\left[
E\Omega\otimes\Omega
+
\Omega\otimes\Omega E
\right]dy
\\
&=
2
\int
\phi
\Omega\cdot E\Omega\,dy.
\end{aligned}
$$

Hence:

$$
\boxed{
\operatorname{tr}R_B^{na}
=
2
\int
\phi
\Omega\cdot E\Omega\,dy.
}
\tag{5.1}
$$

The non-affine residual channel therefore measures a **signed non-affine vorticity-stretching work**.

---

# Theorem D59.3 — Quantitative Positive Non-Affine Work Branch

If the non-affine channel wins Theorem D59.2, then

$$
\boxed{
\int_0^{S_0}
\int
\phi
\Omega\cdot E\Omega
\,dy\,ds
\ge
\frac34
c_\gamma
\int_0^{S_0}\rho(s)ds.
}
\tag{5.2}
$$

Using DCRP56,

$$
\boxed{
\int_0^{S_0}
\int
\phi
\Omega\cdot E\Omega
\,dy\,ds
\ge
\frac38
(2-3\gamma)
\int_0^{S_0}
Z_{\rm in}(s)ds.
}
\tag{5.3}
$$

Thus finite visibility compensation can remain periodic only if the non-affine strain remainder performs a quantitatively positive amount of work on the vorticity covariance.

This is stronger than merely proving

$$
E\neq0.
$$

---

# 6. Absolute non-affine strain consequence

Since

$$
|\Omega\cdot E\Omega|
\le
|E|_F|\Omega|^2,
$$

Theorem D59.3 immediately gives:

## Corollary D59.4 — Weighted Non-Affine Strain Gap

On the non-affine branch,

$$
\boxed{
\int_0^{S_0}
\int
\phi
|E|_F
|\Omega|^2
\,dy\,ds
\ge
\frac38
(2-3\gamma)
\int_0^{S_0}
Z_{\rm in}(s)ds.
}
\tag{6.1}
$$

So the non-affine branch cannot be made arbitrarily small in the vorticity-weighted spacetime norm.

---

# 7. Turnover trace identity

From (1.8),

$$
\boxed{
\operatorname{tr}R_B^{tr}
=
\int
(W\cdot\nabla\phi)
|\Omega|^2dy.
}
\tag{7.1}
$$

This is the covariance-level transport of enstrophy through the fixed observer window.

It has exactly the same structure as the DCRP35 enstrophy transport term.

---

# 8. Radial covariance observer

Choose the fixed covariance cutoff radial:

$$
\boxed{
\phi(y)=\varphi(|y|),
}
\tag{8.1}
$$

with

$$
\boxed{
\varphi'(R)\le0.
}
\tag{8.2}
$$

Then

$$
\nabla\phi
=
\varphi'(R)n_R.
$$

Integrating (7.1) over a period and using coarea,

$$
\begin{aligned}
\mathfrak R_{tr}
&=
\int_0^\infty
\varphi'(R)
\left[
\int_0^{S_0}
\int_{\partial B_R}
|\Omega|^2W\cdot n
\,dSds
\right]dR
\\
&=
2
\int_0^\infty
\varphi'(R)
\mathcal J_\omega(R)
\,dR.
\end{aligned}
$$

Define

$$
\boxed{
f_\phi(R)
=
-\varphi'(R)\ge0.
}
\tag{8.3}
$$

Then

$$
\boxed{
\mathfrak R_{tr}
=
2
\int_0^\infty
f_\phi(R)
[-\mathcal J_\omega(R)]
\,dR.
}
\tag{8.4}
$$

---

# 9. Inward enstrophy turnover

DCRP35 defines

$$
\boxed{
\mathcal J_{\omega,\rm in}(R)
=
[-\mathcal J_\omega(R)]_+.
}
\tag{9.1}
$$

Because

$$
-\mathcal J_\omega
\le
\mathcal J_{\omega,\rm in},
$$

and

$$
f_\phi\ge0,
$$

equation (8.4) gives

$$
\boxed{
\mathfrak R_{tr}
\le
2
\int_0^\infty
f_\phi(R)
\mathcal J_{\omega,\rm in}(R)
\,dR.
}
\tag{9.2}
$$

Therefore:

## Theorem D59.5 — Quantitative Smoothed Inward-Turnover Branch

If the turnover channel wins Theorem D59.2, then

$$
\boxed{
\int_0^\infty
[-\varphi'(R)]
\mathcal J_{\omega,\rm in}(R)
\,dR
\ge
\frac34
c_\gamma
\int_0^{S_0}\rho(s)ds.
}
\tag{9.3}
$$

Using DCRP56,

$$
\boxed{
\int_0^\infty
[-\varphi'(R)]
\mathcal J_{\omega,\rm in}(R)
\,dR
\ge
\frac38
(2-3\gamma)
\int_0^{S_0}
Z_{\rm in}(s)ds.
}
\tag{9.4}
$$

Thus the covariance-turnover residual is not an abstract matrix defect.

It forces an actual positive weighted inward enstrophy transport through a finite annular window.

---

# 10. Unified signed channel theorem

Combine Theorems D59.3 and D59.5.

## Theorem D59.6 — Signed Finite-Compensation Confluence

Every recurrent finite full-angular X72 compensation of a nonzero inner rank-two null-envelope core satisfies at least one of:

### non-affine strain branch

$$
\boxed{
\int_0^{S_0}
\int
\phi
\Omega\cdot E\Omega
\,dy\,ds
\ge
\frac38
(2-3\gamma)
\int_0^{S_0}
Z_{\rm in}(s)ds;
}
\tag{10.1}
$$

### inward enstrophy-turnover branch

$$
\boxed{
\int_0^\infty
[-\varphi'(R)]
\mathcal J_{\omega,\rm in}(R)
\,dR
\ge
\frac38
(2-3\gamma)
\int_0^{S_0}
Z_{\rm in}(s)ds.
}
\tag{10.2}
$$

The right side is strictly positive for a recurrent nonzero inner core.

Thus there is no third finite compensation branch with both channels negligible.

---

# 11. Relationship to the DCRP35 enstrophy dichotomy

DCRP35 already proves that a recurrent strict-DSS vorticity core must be sustained by:

$$
\boxed{
\text{positive vortex stretching}
}
$$

or

$$
\boxed{
\text{inward enstrophy turnover}.
}
$$

D59 sharpens this specifically on the finite X72 compensation branch.

The stretching alternative is not allowed to remain purely within the canonical affine equality strain.

It must contain a positive **non-affine** contribution:

$$
\boxed{
\Omega\cdot E\Omega>0
}
$$

in the period-integrated weighted sense.

Otherwise the finite compensation must be maintained by the same inward enstrophy-turnover mechanism already exposed by DCRP35.

Therefore the D54–58 visibility-compensation machinery does not create a new hidden third source.

It confluences back into the existing DCRP35 source classification.

---

# 12. Relationship to the DCRP38 residual tree

DCRP38 defines

$$
R_B=0
$$

as the exact affine/no-turnover covariance equality branch.

D59 proves much more than

$$
R_B\neq0.
$$

It identifies a signed lower bound for at least one of the two exact mechanisms composing $R_B$.

Therefore:

$$
\boxed{
\text{finite rank-three compensation}
}
$$

is completely absorbed into

$$
\boxed{
R_B^{na}\text{ branch}
}
$$

or

$$
\boxed{
R_B^{tr}\text{ branch}.
}
$$

No new residual identity class is needed.

---

# 13. Relationship to X72 pressure/cofactor defect

The non-affine strain branch naturally interacts with X72's pressure/cofactor program because the affine-response defect

$$
E_p
=
H_P^0+C_S^0
$$

measures departure from the perfect affine strain-pressure relation.

However D59 does **not** claim a universal inequality of the form

$$
|R_B^{na}|
\lesssim
|E_p|
$$

or its converse.

The X72 Round37 defect equation explicitly contains higher-gradient and transport–Riesz forcing, so such a direct algebraic equivalence would be unjustified.

The correct conclusion is only:

$$
\boxed{
R_B^{na}\neq0
}
$$

routes the branch to the existing non-affine/pressure-response analysis.

A new estimate is required if one wants to close that branch via $E_p$.

This STOP is retained to avoid overclaiming.

---

# 14. Relationship to PFET

The turnover channel in D59 is **enstrophy turnover**:

$$
\mathcal J_{\omega,\rm in}.
$$

DCRP31 PFET is an energy/pressure flux:

$$
\mathcal F_{\rm PFET}.
$$

DCRP49 already proved that pressure-Neumann and PFET observables cannot be universally identified.

Likewise D59 does not identify inward enstrophy turnover with PFET.

What is now known is that the same finite normalized supplier package must carry:

- DCRP31 inward PFET;
- and, on the turnover subbranch, a positive smoothed inward enstrophy flux.

Their joint same-parent compatibility remains a future coupling question.

---

# 15. Transparent tail branch is unavailable

DCRP55 offered the alternative:

$$
\boxed{
\text{finite compensation}
\quad\vee\quad
\text{noncompact transparent tail}.
}
$$

DCRP58 proves the second alternative impossible in the strict DSS sublinear-energy class if the branch remains globally fixed-plane rank two.

Therefore every exact transparent continuation is finite and hence falls under Theorem D59.6.

This is what converts D59 from a conditional finite-branch estimate into a genuine confluence theorem for the maximally rigid rank-two visibility-compensation route.

---

# 16. Nontransparent branch

There remains one logically distinct possibility:

the outer/global flow simply does **not** cancel the D54 X72 localization leakage.

Then the global profile retains a nonzero X72 visibility/projection defect.

That branch is already outside the perfect visibility equality state.

It belongs directly to the X72 Round42–43 transfer/realizability defect route.

Thus the global alternatives are now exhaustive at this level:

$$
\boxed{
\text{X72 visibility defect}
}
$$

or

$$
\boxed{
\text{positive non-affine strain work}
}
$$

or

$$
\boxed{
\text{positive inward enstrophy turnover}.
}
$$

A rank-three covariance transition is the geometric mechanism leading into the last two finite branches.

---

# 17. Rank-two equality confluence theorem

Collect the established chain.

### Step 1 — local rank-two equality

DCRP50–53 isolate a nonzero recurrent inner rank-two null-envelope core.

### Step 2 — unavoidable X72 localization leak

DCRP54 proves every finite observation of that core has

$$
\mathcal C_\chi\neq0.
$$

### Step 3 — outer compensation alternatives

DCRP55 gives:

$$
\text{finite rank lift}
\quad\vee\quad
\text{transparent tail}.
$$

### Step 4 — tail elimination

DCRP58 excludes the global fixed-plane transparent tail under the strict DSS sublinear-energy law.

### Step 5 — finite rank-three state

DCRP56 identifies complete finite compensation as

$$
B=\rho I.
$$

### Step 6 — signed residual confluence

D59 forces a positive non-affine strain-work gap or positive inward enstrophy-turnover gap.

Therefore:

## Theorem D59.7 — Rank-Two Transparent Equality Confluence

A nonzero recurrent rank-two null-envelope equality core cannot admit a global continuation satisfying simultaneously:

$$
\boxed{
\text{global X72 visibility transparency},
}
$$

$$
\boxed{
\text{rank-two fixed-plane identity},
}
$$

and

$$
\boxed{
R_B^{na}=R_B^{tr}=0.
}
$$

Every global continuation must enter at least one of:

$$
\boxed{
\mathfrak D_{\rm X72}\neq0,
}
$$

$$
\boxed{
\mathfrak W_{na}
:=
\int\phi\,
\Omega\cdot E\Omega
>0,
}
$$

or

$$
\boxed{
\mathfrak J_{\omega,\rm in}>0.
}
$$

Moreover on the finite compensation route at least one of the last two satisfies the quantitative lower bound (10.1) or (10.2).

This is the current rank-two closure theorem.

---

# 18. What “rank-two closure” means here

It is essential to state the strength correctly.

D59.7 does **not** say:

$$
\boxed{
\text{Navier–Stokes singularity impossible}.
}
$$

It says:

> The long exact rank-two / zero-residual / transparent equality route can no longer survive globally.

Any hypothetical blowup ancestor must activate a nonzero defect/turnover mechanism already present elsewhere in the RMRM/DCRP/X72 tree.

So the branch has been **closed as an equality branch** and absorbed into the larger proof tree.

This is precisely the kind of branch closure needed before a global proof can be assembled.

---

# 19. RMRM handoff state

The rank-two handoff can now be summarized as:

$$
\boxed{
\text{rank-two survivor}
}
$$

$$
\Longrightarrow
$$

$$
\boxed{
\mathsf X
\vee
\mathsf N
\vee
\mathsf T,
}
$$

where:

### X — X72 visibility/pressure-realizability defect

$$
\boxed{
\mathsf X
:
\text{global visibility transparency fails}.
}
$$

### N — non-affine strain-work defect

$$
\boxed{
\mathsf N
:
\int
\phi\,
\Omega\cdot E\Omega
\text{ has a positive period gap}.
}
$$

### T — inward covariance/enstrophy turnover

$$
\boxed{
\mathsf T
:
\int
[-\phi']
\mathcal J_{\omega,\rm in}
\text{ has a positive period gap}.
}
$$

No fourth exact rank-two equality state remains in the present branch analysis.

---

# 20. Quantitative common gap

Define

$$
\boxed{
G_{\rm in}
=
(2-3\gamma)
\int_0^{S_0}
Z_{\rm in}(s)ds.
}
\tag{20.1}
$$

Then

$$
G_{\rm in}>0.
$$

D59.6 gives:

$$
\boxed{
\mathsf N
\ge
\frac38G_{\rm in}
}
$$

or

$$
\boxed{
\mathsf T
\ge
\frac38G_{\rm in}.
}
$$

This gives the rank-two handoff a common quantitative scale.

The factor is not claimed optimal.

Its importance is that the confluence is not merely qualitative.

---

# 21. A norm-level backup theorem

For completeness, define

$$
\boxed{
A_{na}
=
\int_0^{S_0}
\|R_B^{na}\|_Fds,
}
$$

$$
\boxed{
A_{tr}
=
\int_0^{S_0}
\|R_B^{tr}\|_Fds.
}
$$

D57 gives

$$
\int_0^{S_0}
\|R_B\|_Fds
\ge
\frac{\sqrt3}{2}
c_\gamma
\int Z_{\rm in}.
$$

Since

$$
R_B=R_B^{na}+R_B^{tr},
$$

$$
A_{na}+A_{tr}
\ge
\int\|R_B\|.
$$

Thus at least one satisfies

$$
\boxed{
A_{\bullet}
\ge
\frac{\sqrt3}{4}
c_\gamma
\int_0^{S_0}
Z_{\rm in}.
}
\tag{21.1}
$$

This norm dichotomy is weaker in interpretation but remains valid without choosing a radial cutoff.

---

# 22. Non-affine norm corollary

Since

$$
\|R_B^{na}\|_F
\le
2
\int
\phi
|E|_F
|\Omega|^2dy,
$$

the norm-level non-affine branch implies

$$
\boxed{
\int_0^{S_0}
\int
\phi
|E|_F|\Omega|^2
\ge
\frac{\sqrt3}{8}
c_\gamma
\int_0^{S_0}
Z_{\rm in}.
}
\tag{22.1}
$$

This is a second independent quantitative estimate for the non-affine branch.

It is not as physically signed as Theorem D59.3, but it measures the size of the non-affine strain itself.

---

# 23. Turnover norm corollary

Likewise

$$
\|R_B^{tr}\|_F
\le
\int
|W\cdot\nabla\phi|
|\Omega|^2dy.
$$

Therefore the turnover norm branch implies

$$
\boxed{
\int_0^{S_0}
\int
|W\cdot\nabla\phi|
|\Omega|^2
\,dy\,ds
\ge
\frac{\sqrt3}{4}
c_\gamma
\int_0^{S_0}
Z_{\rm in}(s)ds.
}
\tag{23.1}
$$

Thus even without radial monotonicity, the finite observer window has a positive total-variation covariance-turnover gap.

---

# 24. Why the signed theorem is stronger

The norm estimates in Sections 21–23 only prove that some residual is large.

The signed trace theorem proves that the residual must do positive work against the exact similarity covariance demand.

On the non-affine branch this means

$$
\Omega\cdot E\Omega
$$

has positive period contribution.

On the turnover branch it means the radial observer sees net inward enstrophy transport after smoothing.

This directional information is the main improvement of DCRP59 over DCRP57.

---

# 25. NTLA-O interpretation

The finite rank-three state passes the coarse global visibility observer.

A finer dynamical observer decomposes its residual into two legal mechanisms:

$$
R_B^{na},
\qquad
R_B^{tr}.
$$

The signed period trace proves that their sum cannot be observationally equivalent to zero.

A still finer observer then resolves the positive source:

$$
\boxed{
\text{non-affine work}
}
$$

or

$$
\boxed{
\text{inward turnover}.
}
$$

Thus the NTLA-O refinement is:

$$
\boxed{
\text{global multipole transparency}
}
$$

$$
\Downarrow
$$

$$
\boxed{
\text{rank-three isotropy}
}
$$

$$
\Downarrow
$$

$$
\boxed{
\text{positive residual}
}
$$

$$
\Downarrow
$$

$$
\boxed{
\text{non-affine source}
\ \vee\
\text{turnover source}.
}
$$

The equality state disappears under increased structural resolution.

---

# 26. Updated final branch tree

The rank-two route after D59 is:

## Branch X — X72 defect

The D54 visibility leakage is not globally canceled.

Then

$$
\boxed{
\mathfrak D_{\rm X72}\neq0.
}
$$

## Branch N — finite non-affine source

The leakage is compensated finitely, producing isotropic rank three, and

$$
\boxed{
\int
\phi
\Omega\cdot E\Omega
\ge
\frac38G_{\rm in}.
}
$$

## Branch T — finite inward turnover

The leakage is compensated finitely, producing isotropic rank three, and

$$
\boxed{
\int
[-\phi']
\mathcal J_{\omega,\rm in}
\ge
\frac38G_{\rm in}.
}
$$

## Transparent rank-two tail

$$
\boxed{
\text{CLOSED by DCRP58}.
}
$$

Thus every continuation has entered a declared nonzero-defect branch.

---

# 27. Status ledger

## PROVED this round

### D59-P1 — Positive signed total residual period

$$
\int
\operatorname{tr}R_B
=
3(2-3\gamma)\int\rho.
$$

### D59-P2 — Signed residual-channel dichotomy

At least one of

$$
\int\operatorname{tr}R_B^{na}
$$

or

$$
\int\operatorname{tr}R_B^{tr}
$$

carries at least half the total positive trace budget.

### D59-P3 — Quantitative non-affine work branch

$$
\int
\phi\Omega\cdot E\Omega
\ge
\frac38
(2-3\gamma)
\int Z_{\rm in}.
$$

### D59-P4 — Quantitative smoothed inward-turnover branch

$$
\int
[-\phi']
\mathcal J_{\omega,\rm in}
\ge
\frac38
(2-3\gamma)
\int Z_{\rm in}.
$$

### D59-P5 — Weighted non-affine strain norm gap

On the non-affine norm branch,

$$
\int
\phi|E||\Omega|^2
\gtrsim
(2-3\gamma)\int Z_{\rm in}.
$$

### D59-P6 — Total-variation turnover gap

On the turnover norm branch,

$$
\int
|W\cdot\nabla\phi||\Omega|^2
\gtrsim
(2-3\gamma)\int Z_{\rm in}.
$$

### D59-P7 — Rank-two transparent equality confluence

The global transparent zero-residual rank-two equality state has no remaining branch.

---

# 28. Closed / open routes

## Closed

- transparent rank-two tail;
- transparent finite rank-three state with both
  $$
  R_B^{na}=0,
  \qquad
  R_B^{tr}=0;
  $$
- finite compensation with both residual channels arbitrarily small relative to the recurrent inner enstrophy.

## Open but already identified elsewhere

- quantitative global closure of the non-affine strain-work branch;
- quantitative global closure of inward enstrophy turnover jointly with PFET;
- nonzero X72 visibility/pressure-realizability defect branch;
- fully rank-three RMRM dynamics.

No new equality branch is introduced by D59.

---

# 29. New STOP

$$
\boxed{
\textbf{
STOP-D59:
The finite rank-three compensation branch has fully confluenced into existing defects: periodicity forces either a quantitatively positive non-affine vorticity-stretching contribution or a quantitatively positive inward enstrophy-turnover contribution. Together with D58's tail elimination, the transparent zero-residual rank-two equality route has no remaining continuation.
}
}
$$

---

# 30. Next autonomous step

## DCRP60 — RMRM Rank-Two Closure Package / Defect Absorption Audit

**Working title**

> **Rank-Two Closure Theorem, Defect-Branch Dependency Map, and the Next Global Frontier**

Primary tasks:

1. package DCRP38–59 into a concise theorem dependency graph;
2. formally state the hypotheses under which the rank-two exact-equality route is closed;
3. audit the three surviving defect branches:
   - X72 visibility/pressure defect;
   - positive non-affine strain work;
   - inward enstrophy turnover;
4. compare each with earlier RMRM checkpoints to determine whether it is already covered or genuinely new;
5. choose the single strongest unresolved global branch and resume proof work there rather than continuing rank-two local refinements.

Desired endpoint:

$$
\boxed{
\text{formal rank-two closure handoff}
+
\text{one uniquely prioritized global frontier}.
}
$$

---

# 31. One-line checkpoint

The finite outer-compensation branch no longer contains an equality survivor: its exact positive covariance trace budget forces either positive non-affine vortex-stretching work or positive inward enstrophy turnover at a fixed fraction of the recurrent inner enstrophy, while D58 has already removed the transparent rank-two tail.

---

**End checkpoint:** DCRP59  
**Next:** DCRP60 — Rank-Two Closure Package / Defect Absorption Audit.
