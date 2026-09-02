# DCRP66 / X72-R49 — Cofactor-Null Repair, Two-Stress Source Identity, and the True Triple-Correlation Frontier

**Series:** Independent Navier–Stokes Research Series / X72 Bridge  
**Date:** 2026-08-18  
**Status:** Proof-development checkpoint / cofactor-null repair and correlation reduction  
**Immediate predecessor:** `NS_DCRP65_X72R48_SingleFactorNullClosure_CorrelationFrontier_2026-08-18.md`

**Primary internal dependencies**
- DCRP-38 — isotropic covariance ledger
- DCRP-61–65 — aligned/no-turnover X-branch compression
- X72 Round38 — Pressure Self-Commutator Null Identity and equivalent cofactor triple-increment identity
- X72 Round41 — Piola–Vorticity Cofactor Decomposition / Projection Identity
- X72 Round42–43 — actual vorticity-stress visibility / realizability

**External calibration**
- Hess-Childs, Rosenzweig, Serfaty, *Another look at regularity in transport-commutator estimates*, arXiv:2601.02326.
- Galanti, Gibbon, Heritage, *Vorticity alignment results for the three-dimensional Euler and Navier-Stokes equations*, arXiv:chao-dyn/9709003.

No full Navier–Stokes regularity theorem is claimed.

---

# 0. Executive result

DCRP65 stated that all three factorwise Round38 null channels were closed by showing

$$
\delta E_p\not\equiv0,
\qquad
\delta q\not\equiv0,
\qquad
\delta V\not\equiv0.
$$

That statement needs one refinement.

X72 Round38 had already proved the exact **Pressure Self-Commutator Null Identity**

$$
\boxed{
\left\langle
\mathcal T_0q,
[V\cdot\nabla,\mathcal T_0]q
\right\rangle
=
0,
}
$$

and therefore

$$
\boxed{
\left\langle
E_p,
[V\cdot\nabla,\mathcal T_0]q
\right\rangle
=
\left\langle
C_S^0,
[V\cdot\nabla,\mathcal T_0]q
\right\rangle.
}
$$

Equivalently, the exact Round38 triple-increment identity can be written as

$$
\boxed{
\begin{aligned}
\left\langle
E_p,
[V\cdot\nabla,\mathcal T_0]q
\right\rangle
=
-\frac12\operatorname{p.v.}\iint
&
[
\delta V\cdot\nabla K_0
]
\\
&:
\delta C_S^0\,
\delta q\,dxdy.
\end{aligned}
}
$$

Thus the **genuinely relevant defect factor is $\delta C_S^0$, not merely $\delta E_p$**.

D64's forced $\delta E_p$ budget is still a real pressure-defect theorem, but by itself it does not rule out the possibility

$$
\boxed{
\delta C_S^0=0
}
$$

with all $E_p$ variation sitting in the pressure-Hessian component.

DCRP66 repairs this missing null channel.

Let

$$
\boxed{
C
=
C_S^0
=
S^2-\frac13|S|^2I.
}
$$

For every trace-free symmetric $3\times3$ strain tensor,

$$
\boxed{
|C|_F^2
=
\frac16|S|_F^4.
}
$$

Hence

$$
\boxed{
|S|^2
=
\sqrt6\,|C|.
}
$$

On the aligned branch

$$
S\Omega=\lambda(s)\Omega,
$$

if $C(y,s)=K(s)$ is spatially constant, then $|S|^2$ is spatially constant and

$$
\boxed{
K\Omega
=
\left(
\lambda^2-\frac13|S|^2
\right)\Omega
=
\kappa(s)\Omega.
}
$$

Multiply by $\Omega$ and integrate in the isotropic covariance observer:

$$
B
=
\int\phi\,\Omega\otimes\Omega
=
\rho I,
\qquad
\rho>0.
$$

Then

$$
\boxed{
(K-\kappa I)B=0.
}
$$

Since $B$ is invertible,

$$
\boxed{
K=\kappa I.
}
$$

But $K$ is trace free, so

$$
\boxed{
K=0.
}
$$

The strain-cofactor norm identity then forces

$$
\boxed{
S=0,
}
$$

and hence

$$
\boxed{
\lambda=0.
}
$$

Therefore a spatially constant cofactor can occur only at a zero-stretching instant.

It cannot persist through a no-turnover DSS period because periodic covariance requires

$$
\boxed{
\frac1{S_0}\int_0^{S_0}\lambda(s)\,ds
=
\lambda_*
=
\frac{2-3\gamma}{2}
>0.
}
$$

Thus:

$$
\boxed{
\textbf{
the missing cofactor-factor null channel is impossible.
}
}
$$

After D66 the factorwise statement is finally correct in the actual cofactor representation:

$$
\boxed{
\delta C_S^0\not\equiv0,
\qquad
\delta q\not\equiv0,
\qquad
\delta V\not\equiv0.
}
$$

DCRP66 also exposes a new exact algebraic coupling between the pressure source, strain cofactor, and actual vorticity stress.

Let

$$
\boxed{
W_\Omega
=
\Omega\otimes\Omega-\frac13|\Omega|^2I.
}
$$

Since

$$
|W_\Omega|^2
=
\frac23|\Omega|^4,
$$

we have

$$
|\Omega|^2
=
\sqrt{\frac32}\,|W_\Omega|.
$$

The pressure source is

$$
q
=
|S|^2-\frac12|\Omega|^2.
$$

Therefore:

## Two-Stress Source Identity

$$
\boxed{
q
=
\sqrt6\,|C_S^0|
-
\sqrt{\frac38}\,|W_\Omega|.
}
$$

For every pair $(x,y)$,

$$
\boxed{
\delta q
=
\sqrt6\,\delta|C_S^0|
-
\sqrt{\frac38}\,\delta|W_\Omega|.
}
$$

In particular:

$$
\boxed{
|\delta q|
\le
\sqrt6\,|\delta C_S^0|
+
\sqrt{\frac38}\,
|\delta W_\Omega|.
}
$$

And exact source-flat pairs satisfy the amplitude lock

$$
\boxed{
\delta q=0
\iff
\delta|W_\Omega|
=
4\,\delta|C_S^0|.
}
$$

So the remaining correlation problem is not a generic triple of unrelated increments.

The scalar source increment is exactly the difference between:

- strain-cofactor amplitude variation;
- actual vorticity-stress amplitude variation.

This converts the Round38 correlation frontier into a **two-stress correlation problem**.

If $\delta q$ is large where $\delta C$ is small, then the Two-Stress Source Identity forces the variation into $|\delta W_\Omega|$.

If $\delta W_\Omega$ is small, then $\delta q$ must overlap with cofactor-amplitude variation.

Thus pair-support decorrelation between $C$ and $q$ can occur only by transferring source variation into the actual vorticity-stress amplitude.

That route lands directly in the X72 Round41–43 Piola–vorticity program.

The updated X branch is therefore:

$$
\boxed{
\mathsf X_{\rm corr}
\Longrightarrow
\mathsf X_{Cq}
\vee
\mathsf X_{C\omega}
\vee
\mathsf X_{\rm ang},
}
$$

where:

### $\mathsf X_{Cq}$

cofactor and pressure-source increments overlap nontrivially;

### $\mathsf X_{C\omega}$

source/cofactor decorrelation is paid by actual vorticity-stress amplitude increments;

### $\mathsf X_{\rm ang}$

all amplitudes are active but the transport–Riesz tensor pairing cancels angularly / across scales.

This is a smaller and more native frontier than the generic three-increment formulation.

---

# 1. Important correction to the D65 factorwise statement

Round38 defines

$$
\boxed{
E_p
=
H_P^0+C_S^0,
}
$$

with

$$
\boxed{
H_P^0=\mathcal T_0q.
}
$$

The exact pressure self-commutator identity is

$$
\boxed{
\langle
H_P^0,
[V\cdot\nabla,\mathcal T_0]q
\rangle
=
0.
}
\tag{1.1}
$$

Therefore

$$
\boxed{
\langle
E_p,
[V\cdot\nabla,\mathcal T_0]q
\rangle
=
\langle
C_S^0,
[V\cdot\nabla,\mathcal T_0]q
\rangle.
}
\tag{1.2}
$$

Round38 further gives the centered identity

$$
\boxed{
\begin{aligned}
\langle
E_p,
[V\cdot\nabla,\mathcal T_0]q
\rangle
=
-\frac12\operatorname{p.v.}\iint
&
[
\delta V\cdot\nabla K_0
]
\\
&:
\delta C_S^0
\,
\delta q\,dxdy.
\end{aligned}
}
\tag{1.3}
$$

Thus D65's closure of $\delta E_p=0$ is useful but is not the complete cofactor-factor closure.

The missing exact null is:

$$
\boxed{
\delta C_S^0=0.
}
\tag{1.4}
$$

D66 closes it.

---

# 2. Trace-free strain cofactor invariant

Let

$$
\boxed{
C
=
S^2-\frac13|S|^2I,
}
\tag{2.1}
$$

with

$$
S=S^\top,
\qquad
\operatorname{tr}S=0.
$$

Let the eigenvalues of $S$ be

$$
s_1,s_2,s_3,
\qquad
s_1+s_2+s_3=0.
$$

For three trace-free eigenvalues, Newton's identities give

$$
\boxed{
s_1^4+s_2^4+s_3^4
=
\frac12
(s_1^2+s_2^2+s_3^2)^2.
}
\tag{2.2}
$$

Therefore

$$
\begin{aligned}
|C|^2
&=
\operatorname{tr}
\left(
S^2-\frac13|S|^2I
\right)^2
\\
&=
\operatorname{tr}S^4
-
\frac23|S|^4
+
\frac13|S|^4
\\
&=
\frac16|S|^4.
\end{aligned}
$$

Thus:

## Theorem D66.1 — Cofactor-Norm / Strain-Norm Identity

$$
\boxed{
|C_S^0|^2
=
\frac16|S|^4.
}
\tag{2.3}
$$

Equivalently,

$$
\boxed{
|S|^2
=
\sqrt6\,|C_S^0|.
}
\tag{2.4}
$$

This is exact and pointwise.

---

# 3. Aligned cofactor eigenvalue

Assume

$$
\boxed{
S\Omega=\lambda(s)\Omega.
}
\tag{3.1}
$$

Then

$$
S^2\Omega
=
\lambda^2\Omega.
$$

Therefore

$$
\boxed{
C\Omega
=
\left(
\lambda^2-\frac13|S|^2
\right)\Omega.
}
\tag{3.2}
$$

Define

$$
\boxed{
\kappa_C(y,s)
=
\lambda(s)^2-\frac13|S(y,s)|^2.
}
\tag{3.3}
$$

Then

$$
\boxed{
C\Omega=\kappa_C\Omega.
}
\tag{3.4}
$$

---

# 4. Assume the missing cofactor null channel

Suppose at a fixed time

$$
\boxed{
C(y,s)=K(s)
}
\tag{4.1}
$$

is spatially constant on the covariance observer domain.

By Theorem D66.1,

$$
|S|^2
=
\sqrt6|K|
$$

is also spatially constant.

Because $\lambda(s)$ is spatially uniform on the aligned branch,

$$
\kappa_C
=
\lambda^2-\frac13|S|^2
$$

is a scalar depending only on time.

Hence

$$
\boxed{
K\Omega=\kappa_C\Omega
}
\tag{4.2}
$$

throughout the observer.

---

# 5. Isotropic covariance forces the constant cofactor to be scalar

The finite compensation branch has

$$
\boxed{
B
=
\int
\phi
\Omega\otimes\Omega\,dy
=
\rho I,
}
\tag{5.1}
$$

with

$$
\rho>0.
$$

From (4.2),

$$
(K-\kappa_C I)\Omega=0.
$$

Multiply by $\Omega$ and integrate:

$$
\boxed{
(K-\kappa_C I)B=0.
}
\tag{5.2}
$$

Since

$$
B=\rho I
$$

is invertible,

$$
\boxed{
K=\kappa_C I.
}
\tag{5.3}
$$

But $C$ is trace free, so

$$
\operatorname{tr}K=0.
$$

Therefore

$$
\boxed{
\kappa_C=0,
\qquad
K=0.
}
\tag{5.4}
$$

---

# 6. Zero cofactor forces zero strain

By Theorem D66.1,

$$
K=C=0
$$

implies

$$
\boxed{
|S|=0.
}
$$

Thus

$$
\boxed{
S=0.
}
\tag{6.1}
$$

Then from alignment,

$$
S\Omega=\lambda\Omega,
$$

and the active covariance has nonzero vorticity, so

$$
\boxed{
\lambda=0.
}
\tag{6.2}
$$

Therefore:

## Theorem D66.2 — Instantaneous Constant-Cofactor Rigidity

On an aligned full-rank isotropic covariance state,

$$
\boxed{
C_S^0(y,s)
\text{ spatially constant}
\Longrightarrow
S=0
\Longrightarrow
\lambda=0.
}
\tag{6.3}
$$

No nonzero aligned stretching state can have a spatially constant strain cofactor.

---

# 7. Periodic cofactor-null channel is impossible

The no-turnover periodic covariance branch requires

$$
\boxed{
\frac1{S_0}
\int_0^{S_0}
\lambda(s)ds
=
\lambda_*
=
\frac{2-3\gamma}{2}
>0.
}
\tag{7.1}
$$

If

$$
\delta C_S^0\equiv0
$$

for almost every time through a complete period, Theorem D66.2 gives

$$
\lambda(s)=0
$$

for almost every time.

This contradicts (7.1).

Hence:

## Theorem D66.3 — Round38 Cofactor-Factor Null NO-GO

$$
\boxed{
\delta C_S^0\not\equiv0
}
\tag{7.2}
$$

on every nonzero recurrent aligned/no-turnover branch.

This is the missing factorwise closure left implicit by D65.

---

# 8. Corrected factorwise Round38 closure

D65 proves

$$
\boxed{
\delta q\not\equiv0,
\qquad
\delta V\not\equiv0.
}
$$

D66 proves

$$
\boxed{
\delta C_S^0\not\equiv0.
}
$$

Therefore the actual equivalent cofactor triple identity has all three factors active:

## Theorem D66.4 — True Cofactor Triple-Active Regime

$$
\boxed{
\delta V\not\equiv0,
\qquad
\delta C_S^0\not\equiv0,
\qquad
\delta q\not\equiv0.
}
\tag{8.1}
$$

Only after D66 is the single-factor null-channel closure complete in the representation that actually controls the commutator energy.

---

# 9. Actual vorticity-stress amplitude

Define

$$
\boxed{
W_\Omega
=
\Omega\otimes\Omega
-\frac13|\Omega|^2I.
}
\tag{9.1}
$$

Its exact algebraic norm is

$$
\boxed{
|W_\Omega|^2
=
\frac23|\Omega|^4.
}
\tag{9.2}
$$

Hence

$$
\boxed{
|\Omega|^2
=
\sqrt{\frac32}\,
|W_\Omega|.
}
\tag{9.3}
$$

---

# 10. Two-Stress Source Identity

The pressure source is

$$
\boxed{
q
=
|S|^2-\frac12|\Omega|^2.
}
\tag{10.1}
$$

Use Theorem D66.1 and (9.3):

$$
|S|^2
=
\sqrt6|C|,
$$

and

$$
\frac12|\Omega|^2
=
\sqrt{\frac38}|W_\Omega|.
$$

Therefore:

## Theorem D66.5 — Two-Stress Source Identity

$$
\boxed{
q
=
\sqrt6\,|C_S^0|
-
\sqrt{\frac38}\,|W_\Omega|.
}
\tag{10.2}
$$

The scalar pressure source is exactly the difference of two native stress amplitudes:

- the strain cofactor amplitude;
- the actual vorticity-stress amplitude.

---

# 11. Pairwise source decomposition

For every pair $(x,y)$,

$$
\boxed{
\delta q
=
\sqrt6\,\delta|C|
-
\sqrt{\frac38}\,
\delta|W_\Omega|.
}
\tag{11.1}
$$

Since the Frobenius norm is 1-Lipschitz,

$$
|\delta|C||
\le
|\delta C|,
$$

and

$$
|\delta|W_\Omega||
\le
|\delta W_\Omega|.
$$

Therefore:

## Corollary D66.6 — Source-Increment Envelope

$$
\boxed{
|\delta q|
\le
\sqrt6\,|\delta C|
+
\sqrt{\frac38}\,
|\delta W_\Omega|.
}
\tag{11.2}
$$

Thus source variation cannot be supported independently of both stress increments.

---

# 12. Exact source-flat amplitude lock

If

$$
\boxed{
\delta q=0,
}
$$

then from (11.1),

$$
\sqrt6\,
\delta|C|
=
\sqrt{\frac38}\,
\delta|W_\Omega|.
$$

The ratio is exactly

$$
\frac{\sqrt6}{\sqrt{3/8}}
=
4.
$$

Therefore:

## Corollary D66.7 — Four-to-One Source-Flat Lock

$$
\boxed{
\delta q=0
\iff
\delta|W_\Omega|
=
4\,\delta|C_S^0|.
}
\tag{12.1}
$$

Round38's source-flat direction is therefore a precise stress-amplitude locking condition, not a free scalar degeneracy.

D65 rules out this lock globally over the entire nonzero DSS branch.

---

# 13. Cofactor-flat pairs force vorticity-stress source variation

On a pair where

$$
\delta C=0,
$$

we also have

$$
\delta|C|=0.
$$

Then (11.1) becomes

$$
\boxed{
\delta q
=
-\sqrt{\frac38}\,
\delta|W_\Omega|.
}
\tag{13.1}
$$

Thus any source variation on a cofactor-flat pair is **pure actual-vorticity-stress amplitude variation**.

This is the first exact bridge from pair-support decorrelation to the X72 Piola–vorticity branch.

---

# 14. Vorticity-stress-flat pairs force cofactor/source overlap

Conversely, if

$$
\delta W_\Omega=0,
$$

then

$$
\delta|W_\Omega|=0
$$

and

$$
\boxed{
\delta q
=
\sqrt6\,\delta|C|.
}
\tag{14.1}
$$

Hence every nonzero source increment on a vorticity-stress-flat pair necessarily overlaps cofactor-amplitude variation.

---

# 15. Pair-support decorrelation is no longer arbitrary

Suppose a sequence of pair regions tries to satisfy:

$$
|\delta C|\ll|\delta q|.
$$

By Corollary D66.6, this forces

$$
|\delta W_\Omega|
\gtrsim
|\delta q|.
$$

Schematically:

$$
\boxed{
\text{source/cofactor decorrelation}
\Longrightarrow
\text{vorticity-stress amplitude participation}.
}
\tag{15.1}
$$

Therefore the old generic support-decorrelation route has only one place to go:

$$
\boxed{
W_\Omega.
}
$$

This is exactly the nonlinear stress whose Piola visibility/realizability has been developed in X72 Round41–43.

---

# 16. Corrected Round38 correlation identity

Because the pressure component is self-null,

$$
\boxed{
\begin{aligned}
\mathfrak Q_{TR}
:={}&
\operatorname{p.v.}
\int_0^{S_0}
\iint
[
\delta V\cdot\nabla K_0
]
:
\delta C
\,
\delta q
\,dxdy\,ds
\\
={}&
-2
\int_0^{S_0}
\langle
E_p,
[V\cdot\nabla,\mathcal T_0]q
\rangle ds.
\end{aligned}
}
\tag{16.1}
$$

After D66:

$$
\delta V,\quad
\delta C,\quad
\delta q
$$

are all individually active.

But $\delta q$ is itself constrained by (11.1).

So the true correlation problem is

$$
\boxed{
\delta V
\quad\times\quad
\delta C
\quad\times\quad
\left(
\sqrt6\,\delta|C|
-
\sqrt{\frac38}\,\delta|W_\Omega|
\right).
}
\tag{16.2}
$$

This is substantially more structured than a generic triple product.

---

# 17. Split the correlation into two native pieces

Insert (11.1) into (16.1):

$$
\boxed{
\mathfrak Q_{TR}
=
\sqrt6\,\mathfrak Q_{CC}
-
\sqrt{\frac38}\,
\mathfrak Q_{C\omega},
}
\tag{17.1}
$$

where

$$
\boxed{
\mathfrak Q_{CC}
=
\operatorname{p.v.}
\int\!\!\int\!\!\int
[
\delta V\cdot\nabla K_0
]
:
\delta C
\,
\delta|C|,
}
\tag{17.2}
$$

and

$$
\boxed{
\mathfrak Q_{C\omega}
=
\operatorname{p.v.}
\int\!\!\int\!\!\int
[
\delta V\cdot\nabla K_0
]
:
\delta C
\,
\delta|W_\Omega|.
}
\tag{17.3}
$$

Thus any exact silence satisfies the signed balance

$$
\boxed{
\sqrt6\,\mathfrak Q_{CC}
=
\sqrt{\frac38}\,
\mathfrak Q_{C\omega}.
}
\tag{17.4}
$$

Equivalently,

$$
\boxed{
\mathfrak Q_{C\omega}
=
4\mathfrak Q_{CC}.
}
\tag{17.5}
$$

This is the new **correlation-balance equality**.

---

# 18. Meaning of the two pieces

## $\mathfrak Q_{CC}$ — cofactor self-amplitude transport correlation

This measures transport-kernel correlation between:

- cofactor orientation increment $\delta C$;
- cofactor amplitude increment $\delta|C|$.

It is purely strain/cofactor geometry.

## $\mathfrak Q_{C\omega}$ — cofactor/vorticity-stress amplitude correlation

This measures the same cofactor orientation increment against:

$$
\delta|W_\Omega|.
$$

It is the direct bridge to X72 Round41–43.

Thus exact X72 silence no longer means “some triple cancellation.”

It requires an exact four-to-one balance between two native correlation channels.

---

# 19. New correlation normal form

The X branch now has three possibilities:

### Cq-overlap / cofactor self-correlation

$$
\boxed{
\mathfrak Q_{CC}
}
$$

is the dominant active correlation.

### Piola–vorticity transfer

$$
\boxed{
\mathfrak Q_{C\omega}
}
$$

carries the source variation through actual vorticity-stress amplitude.

### exact balance / angular cancellation

The two nonzero channels satisfy

$$
\boxed{
\mathfrak Q_{C\omega}=4\mathfrak Q_{CC}
}
$$

after principal-value/angular integration.

The last case is now the sharp equality condition.

---

# 20. Relation to X72 Round41

Round41's Piola–Vorticity Projection Identity is

$$
\boxed{
\mathcal T_0^\ast C
=
-\frac16q
-
\mathfrak V_\Omega,
}
\tag{20.1}
$$

where

$$
\boxed{
\mathfrak V_\Omega
=
\frac1{12}|\Omega|^2
+
\frac14
\mathcal R_i\mathcal R_j
(\Omega_i\Omega_j).
}
\tag{20.2}
$$

So both the scalar projection of $C$ and the source-increment identity of D66 fail to become purely local for exactly the same reason:

$$
\boxed{
\text{actual vorticity stress}.
}
$$

This independently confirms that the $\mathfrak Q_{C\omega}$ branch is the correct native escape when cofactor/source overlap degenerates.

---

# 21. What D66 does not yet prove

D66 does **not** prove:

$$
\mathfrak Q_{TR}\neq0.
$$

It also does not prove either

$$
\mathfrak Q_{CC}
$$

or

$$
\mathfrak Q_{C\omega}
$$

has a fixed sign.

The Riesz kernel remains angularly indefinite.

What D66 proves is:

1. the cofactor factor itself cannot be globally null;
2. source variation is exactly tied to cofactor and vorticity-stress amplitudes;
3. a silent commutator must satisfy the exact balance
   $$
   \mathfrak Q_{C\omega}=4\mathfrak Q_{CC}.
   $$

The remaining equality class is therefore considerably smaller.

---

# 22. Corrected status of D64/D65

## D64 remains valid

The pressure-response defect has a forced spatial increment budget modulo constants.

## D65 N2/N3 remain valid

The source cannot be globally constant and velocity cannot be globally constant.

## D65 factorwise sentence is repaired

The commutator's equivalent cofactor representation required a separate proof that

$$
\delta C\not\equiv0.
$$

D66 supplies that proof.

Thus no previous theorem is discarded; the representation-level gap is closed.

---

# 23. Updated global frontier

After D66:

$$
\boxed{
\text{rank-two continuation}
\Longrightarrow
\mathsf X_{\rm 2stress}
\vee
\mathsf T,
}
\tag{23.1}
$$

where $\mathsf X_{\rm 2stress}$ is the cofactor/vorticity-stress correlation problem governed by

$$
\boxed{
\mathfrak Q_{TR}
=
\sqrt6\,\mathfrak Q_{CC}
-
\sqrt{\frac38}\mathfrak Q_{C\omega}.
}
$$

A silent X branch must satisfy the exact balance

$$
\boxed{
\mathfrak Q_{C\omega}
=
4\mathfrak Q_{CC}.
}
$$

The generic three-unrelated-increment picture is gone.

---

# 24. Status ledger

## PROVED this round

### D66-P1 — cofactor norm identity

$$
|C_S^0|^2
=
\frac16|S|^4.
$$

### D66-P2 — instantaneous constant-cofactor rigidity

Aligned full-rank isotropic covariance plus spatially constant $C_S^0$ forces

$$
S=0,
\qquad
\lambda=0.
$$

### D66-P3 — periodic cofactor-factor null NO-GO

$$
\delta C_S^0\not\equiv0.
$$

### D66-P4 — true cofactor triple-active regime

$$
\delta V,\delta C_S^0,\delta q
$$

are all nontrivial.

### D66-P5 — Two-Stress Source Identity

$$
q
=
\sqrt6|C_S^0|
-
\sqrt{\frac38}|W_\Omega|.
$$

### D66-P6 — source-increment envelope

$$
|\delta q|
\le
\sqrt6|\delta C|
+
\sqrt{\frac38}|\delta W_\Omega|.
$$

### D66-P7 — exact four-to-one source-flat amplitude lock

$$
\delta q=0
\iff
\delta|W_\Omega|
=
4\delta|C|.
$$

### D66-P8 — exact cofactor/vorticity correlation split

$$
\mathfrak Q_{TR}
=
\sqrt6\,\mathfrak Q_{CC}
-
\sqrt{\frac38}\mathfrak Q_{C\omega}.
$$

### D66-P9 — silent-correlation equality

$$
\mathfrak Q_{TR}=0
\Rightarrow
\mathfrak Q_{C\omega}=4\mathfrak Q_{CC}.
$$

---

# 25. New STOP

$$
\boxed{
\textbf{
STOP-D66:
The Round38 commutator sees only the strain-cofactor component, so D65 required one missing repair: a spatially constant cofactor would still null the true triple identity even with nonconstant pressure defect. Isotropic rank-three covariance plus aligned stretching now rules that out. Moreover the pressure source is exactly the difference of strain-cofactor and actual-vorticity-stress amplitudes, so every silent X branch must satisfy a precise four-to-one balance between cofactor self-correlation and cofactor–vorticity-stress correlation.
}
}
$$

---

# 26. Next autonomous step

## DCRP67 / X72-R50 — Four-to-One Correlation-Balance Rigidity

**Working title**

> **Cofactor Self-Correlation versus Piola–Vorticity Correlation and the Exact Silent-Balance Manifold**

Primary tasks:

1. analyze
   $$
   \mathfrak Q_{C\omega}=4\mathfrak Q_{CC};
   $$
2. use the actual vorticity-stress cone
   $$
   W_\Omega
   =
   \Omega\otimes\Omega-\frac13|\Omega|^2I
   $$
   and the aligned relation $S\Omega=\lambda\Omega$;
3. determine whether cofactor orientation increments and vorticity-stress amplitude increments can realize the exact 4:1 principal-value correlation ratio;
4. split amplitude change from orientation change in
   $$
   \delta C;
   $$
5. exploit Round41 Piola–vorticity projection identity to replace the $C\omega$ channel by visible/invisible vorticity-stress variables;
6. classify exact angular cancellation under the 4:1 balance;
7. prove:
   - positive commutator transfer;
   - or one explicit two-stress silent normal form.

Desired endpoint:

$$
\boxed{
\mathsf X_{\rm 2stress}
\Longrightarrow
\text{positive transfer}
\vee
\text{explicit two-stress equality geometry}.
}
$$

---

# 27. One-line checkpoint

The Round38 correlation frontier is now a two-stress problem: the true commutator factor is a necessarily nonconstant strain cofactor, while the pressure source is exactly the difference between cofactor amplitude and actual vorticity-stress amplitude; exact silence requires the rigid correlation balance $\mathfrak Q_{C\omega}=4\mathfrak Q_{CC}$.

---

**End checkpoint:** DCRP66 / X72-R49  
**Next:** DCRP67 / X72-R50 — Four-to-One Correlation-Balance Rigidity.
