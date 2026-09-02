# DCRP65 / X72-R48 — Pressure-Source Flatness NO-GO and Closure of All Single-Factor Triple-Increment Null Channels

**Series:** Independent Navier–Stokes Research Series / X72 Bridge  
**Date:** 2026-08-18  
**Status:** Proof-development checkpoint / Round38 null-channel elimination  
**Immediate predecessor:** `NS_DCRP64_X72R47_ConstantDefectNoGo_ForcedIncrementBudget_2026-08-18.md`

**Primary internal dependencies**
- DCRP-30 — strict DSS sublinear period-averaged local velocity-energy growth
- DCRP-38 — covariance ledger
- DCRP-61–64 — aligned/no-turnover pressure-defect reduction and forced $E_p$ increments
- X72 Round37 — $E_p=H_P^0+C_S^0$, $H_P^0=\mathcal T_0 q$
- X72 Round38 — exact transport–Riesz triple-increment identity and null channels N1/N2/N3
- X72 Round41 — Piola/cofactor reduction

**External calibration**
- Hess-Childs, Rosenzweig, Serfaty, *Another look at regularity in transport-commutator estimates*, arXiv:2601.02326.
- Álvarez-Samaniego, Álvarez-Samaniego, Fernández-Dalgo, *On the use of the Riesz transforms to determine the pressure term in the incompressible Navier-Stokes equations on the whole space*, arXiv:2004.02588.

The external references calibrate the whole-space Riesz pressure normalization and generic transport–Riesz commutator difficulty. The branch-specific identities below are derived directly.

No full Navier–Stokes regularity theorem is claimed.

---

# 0. Executive result

X72 Round38 writes the pressure-response commutator pairing as

$$
\boxed{
\begin{aligned}
\langle E_p,[V\cdot\nabla,\mathcal T_0]q\rangle
=
-\frac12\operatorname{p.v.}\iint
&[\delta_{xy}V\cdot\nabla K_0(x-y)]
\\
&:\delta_{xy}E_p\,\delta_{xy}q\,dxdy,
\end{aligned}
}
$$

with pressure source

$$
\boxed{
q
=
|S|^2-\frac12|\Omega|^2
=
-\Delta P.
}
$$

Round38 identifies three exact single-factor null channels:

$$
\boxed{
\text{N1: }\delta E_p=0,
}
$$

$$
\boxed{
\text{N2: }\delta q=0,
}
$$

$$
\boxed{
\text{N3: }\delta V=0.
}
$$

DCRP64 already closes N1 on the aligned/no-turnover finite-compensation branch by proving a strictly positive pressure-defect pair-increment budget.

DCRP65 closes N2 and N3.

The pressure source has the exact divergence form

$$
\boxed{
q
=
\partial_i\partial_j(V_iV_j)
}
$$

for every smooth divergence-free profile.

Suppose N2 holds globally:

$$
\boxed{
q(y,s)=q_0(s).
}
$$

The strict DSS Euler tail satisfies the period-averaged local velocity-energy bound

$$
\boxed{
\mathcal E(R)
=
\int_0^{S_0}\int_{B_R}|V|^2
\le
CR^\kappa,
\qquad
0<\kappa<1.
}
$$

Testing the double-divergence identity against a spatial cutoff $\chi(y/R)$ gives, distributionally in similarity time,

$$
\boxed{
q_0(s)=0.
}
$$

In fact the argument only requires $\kappa<5$.

Now use the X72 whole-space Riesz pressure normalization

$$
\boxed{
H_P^0=\mathcal T_0q.
}
$$

If $q\equiv0$, then

$$
\boxed{
H_P^0=0,
\qquad
\Delta P=0,
\qquad
H_P=0.
}
$$

But DCRP62 proves on a materially persistent aligned state

$$
\boxed{
H_P\Omega
=
-(\lambda'+\lambda+\lambda^2)\Omega.
}
$$

Therefore a nonzero aligned branch with $q=0$ must satisfy

$$
\boxed{
\lambda'+\lambda+\lambda^2=0.
}
$$

Integrating one DSS period gives

$$
\boxed{
0
=
\int_0^{S_0}\lambda\,ds
+
\int_0^{S_0}\lambda^2ds.
}
$$

But no-turnover periodic covariance forces

$$
\boxed{
\int_0^{S_0}\lambda\,ds
=
\lambda_*S_0,
\qquad
\lambda_*
=
\frac{2-3\gamma}{2}>0.
}
$$

Contradiction.

Hence:

$$
\boxed{
\textbf{Round38 N2 cannot support the recurrent aligned/no-turnover branch.}
}
$$

N3 is simpler:

$$
\boxed{
\delta V\equiv0
\Longrightarrow
V\text{ spatially constant}
\Longrightarrow
\Omega=\nabla\times V=0,
}
$$

contradicting the nonzero recurrent covariance.

DCRP65 also sharpens the transport side.

For the trace-free Riesz kernel

$$
K_0(z)
\propto
|z|^{-3}(I-3n\otimes n),
\qquad
n=z/|z|,
$$

an affine velocity increment

$$
\delta V=Az
$$

can make the pointwise transport kernel factor

$$
\boxed{
(Az)\cdot\nabla K_0(z)
}
$$

vanish for every $z\neq0$ **only if**

$$
\boxed{
A=0.
}
$$

Thus even the stronger affine transport-kernel silence has no nontrivial exact mode.

Combining D64 and D65:

$$
\boxed{
\delta E_p\not\equiv0,
\qquad
\delta q\not\equiv0,
\qquad
\delta V\not\equiv0
}
$$

on every nonzero recurrent aligned/no-turnover branch.

Therefore all **single-factor** Round38 null mechanisms are gone.

If the exact triple pairing still vanishes, it must do so through a genuinely relational mechanism:

$$
\boxed{
\text{pair/support decorrelation}
\ \vee\
\text{tensor/angular orthogonality}
\ \vee\
\text{multiscale sign cancellation}
\ \vee\
\text{critical principal-value cancellation}.
}
$$

The X branch is no longer an amplitude-degeneracy problem.

It is now a **pure correlation problem** among three individually active increments.

The final rank-two frontier becomes

$$
\boxed{
\mathsf X_{\rm corr}
\vee
\mathsf T,
}
$$

where $\mathsf X_{\rm corr}$ is the nontrivial Round38 triple-increment correlation/cancellation class, and $\mathsf T$ remains same-parent material turnover.

---

# 1. Pressure source as a double divergence

Let

$$
\boxed{
L=\nabla V.
}
$$

For incompressible flow,

$$
\boxed{
\nabla\cdot V=0.
}
$$

The pressure source is

$$
\boxed{
q
=
|S|^2-\frac12|\Omega|^2
=
\operatorname{tr}(L^2).
}
\tag{1.1}
$$

Now compute:

$$
\begin{aligned}
\partial_i\partial_j(V_iV_j)
&=
\partial_i
\left[
(\partial_jV_i)V_j
+V_i(\partial_jV_j)
\right]
\\
&=
\partial_i
\left[
(\partial_jV_i)V_j
\right]
\\
&=
(\partial_i\partial_jV_i)V_j
+
(\partial_jV_i)(\partial_iV_j)
\\
&=
(\partial_jV_i)(\partial_iV_j).
\end{aligned}
$$

The last quantity is

$$
\operatorname{tr}(L^2).
$$

Therefore:

## Theorem D65.1 — Exact Pressure-Source Double-Divergence Identity

$$
\boxed{
q
=
\partial_i\partial_j(V_iV_j).
}
\tag{1.2}
$$

This identity is purely local and uses only incompressibility.

---

# 2. Assume the Round38 N2 null channel

Round38 N2 is the exact global condition

$$
\boxed{
q(y,s)=q_0(s).
}
\tag{2.1}
$$

The function may depend on similarity time but not on space.

---

# 3. Period-averaged sublinear velocity energy

The admissible profile satisfies

$$
\boxed{
\mathcal E(R)
=
\int_0^{S_0}
\int_{B_R}
|V(y,s)|^2\,dy\,ds
\le
CR^\kappa
}
\tag{3.1}
$$

with

$$
\boxed{
0<\kappa<1.
}
\tag{3.2}
$$

For the pressure-source flatness argument one only needs

$$
\boxed{
\kappa<5.
}
\tag{3.3}
$$

---

# 4. Spatial cutoff test

Choose

$$
\boxed{
\chi\in C_c^\infty(\mathbb R^3),
\qquad
\int\chi\neq0,
}
$$

and define

$$
\boxed{
\chi_R(y)=\chi(y/R).
}
\tag{4.1}
$$

Then

$$
\boxed{
\int\chi_Rdy
=
R^3\int\chi.
}
\tag{4.2}
$$

Also

$$
\boxed{
|D^2\chi_R|
\lesssim R^{-2}.
}
\tag{4.3}
$$

Let

$$
\zeta\in C_c^\infty(0,S_0)
$$

be an arbitrary temporal test.

Using Theorem D65.1,

$$
\begin{aligned}
&\int_0^{S_0}
\zeta(s)
q_0(s)
\left[
\int\chi_Rdy
\right]ds
\\
&\qquad=
\int_0^{S_0}
\zeta(s)
\int
V_iV_j
\partial_i\partial_j\chi_R
\,dy\,ds.
\end{aligned}
\tag{4.4}
$$

---

# 5. Energy bound kills the spatially constant source

The RHS satisfies

$$
\begin{aligned}
|\mathrm{RHS}|
&\lesssim
R^{-2}
\int_{\operatorname{supp}\zeta}
\int_{B_{CR}}
|V|^2dy\,ds
\\
&\lesssim
R^{\kappa-2}.
\end{aligned}
\tag{5.1}
$$

The LHS is

$$
R^3
\left[
\int\chi
\right]
\int_0^{S_0}
\zeta(s)q_0(s)ds.
$$

Therefore

$$
\boxed{
\left|
\int_0^{S_0}
\zeta q_0ds
\right|
\lesssim
R^{\kappa-5}.
}
\tag{5.2}
$$

Let $R\to\infty$.

Since $\kappa<5$,

$$
\boxed{
\int_0^{S_0}\zeta(s)q_0(s)ds=0
}
$$

for every temporal test $\zeta$.

Thus:

## Theorem D65.2 — Spatially Constant Pressure Source Must Vanish

Under any period-averaged local velocity-energy bound

$$
\mathcal E(R)=O(R^\kappa),
\qquad
\kappa<5,
$$

a spatially constant pressure source satisfies

$$
\boxed{
q_0(s)=0
}
\tag{5.3}
$$

in the sense of distributions in similarity time, hence pointwise for smooth profiles.

---

# 6. Whole-space X72 pressure normalization

X72 uses

$$
\boxed{
H_P^0
=
\mathcal T_0q.
}
\tag{6.1}
$$

If $q\equiv0$, then

$$
\boxed{
H_P^0=0.
}
\tag{6.2}
$$

But $q=-\Delta P$, so also

$$
\boxed{
\Delta P=0.
}
\tag{6.3}
$$

Therefore

$$
\boxed{
H_P=0.
}
\tag{6.4}
$$

This step is inside the canonical whole-space Riesz-normalized pressure representative used by X72.

---

# 7. Aligned pressure compatibility

DCRP62 proves on a materially persistent aligned branch

$$
\boxed{
H_P\Omega
=
-(\lambda'+\lambda+\lambda^2)\Omega.
}
\tag{7.1}
$$

If $H_P=0$ and $\Omega\neq0$, then

$$
\boxed{
\lambda'
+
\lambda
+
\lambda^2
=
0.
}
\tag{7.2}
$$

---

# 8. Periodic positive-mean contradiction

Integrate (7.2) over one period.

Since $\lambda$ is periodic,

$$
\int_0^{S_0}\lambda'ds=0.
$$

Therefore

$$
\boxed{
0
=
\int_0^{S_0}\lambda ds
+
\int_0^{S_0}\lambda^2ds.
}
\tag{8.1}
$$

But D64 gives

$$
\boxed{
\int_0^{S_0}\lambda ds
=
\lambda_*S_0,
}
\tag{8.2}
$$

where

$$
\boxed{
\lambda_*
=
\frac{2-3\gamma}{2}
>0.
}
\tag{8.3}
$$

Contradiction.

## Theorem D65.3 — Round38 N2 Pressure-Source Null NO-GO

A nonzero recurrent aligned/no-turnover finite-compensation branch in the strict DSS energy class cannot satisfy

$$
\boxed{
q(x,s)=q_0(s)
}
$$

globally.

Equivalently,

$$
\boxed{
\delta q\not\equiv0.
}
\tag{8.4}
$$

---

# 9. Round38 N3 velocity null channel

If

$$
\boxed{
\delta_{xy}V=0
}
$$

for all pairs, then $V$ is spatially constant and

$$
\boxed{
\Omega=\nabla\times V=0.
}
$$

This contradicts $Z(s)>0$.

Therefore:

## Theorem D65.4 — Round38 N3 Velocity Null NO-GO

$$
\boxed{
\delta V\not\equiv0.
}
\tag{9.1}
$$

---

# 10. Stronger affine transport-kernel rigidity

Up to a nonzero scalar constant,

$$
\boxed{
K_0(z)
=
|z|^{-3}
(I-3n\otimes n),
\qquad
n=z/|z|.
}
\tag{10.1}
$$

Let

$$
\boxed{
\delta V=Az.
}
\tag{10.2}
$$

Set

$$
\boxed{
a(n)=n^TAn.
}
\tag{10.3}
$$

Direct differentiation gives

$$
\boxed{
(Az)\cdot\nabla K_0(z)
\propto
-3|z|^{-3}
\left[
aI
+
(An)\otimes n
+
n\otimes(A^Tn)
-
5a\,n\otimes n
\right].
}
\tag{10.4}
$$

Assume

$$
\boxed{
(Az)\cdot\nabla K_0(z)=0
}
\tag{10.5}
$$

for every $z\neq0$.

Take a unit $n$ and $v\perp n$.

Sandwich (10.4) between $v^T$ and $v$.

Only $a|v|^2$ survives, hence $a(n)=0$ for every unit $n$.

Thus the symmetric part of $A$ vanishes:

$$
\boxed{
A^T=-A.
}
\tag{10.6}
$$

For skew $A$, (10.4) becomes

$$
\boxed{
(An)\otimes n
-
n\otimes An
=
0.
}
\tag{10.7}
$$

Apply this tensor to $n$.

Since $n\cdot An=0$,

$$
An=0
$$

for every unit $n$.

Therefore:

## Theorem D65.5 — Affine Transport-Kernel Silence Rigidity

$$
\boxed{
(Az)\cdot\nabla K_0(z)\equiv0
\Longrightarrow
A=0.
}
\tag{10.8}
$$

There is no nontrivial affine velocity-gradient mode making the Round38 transport kernel factor vanish pointwise for every pair.

---

# 11. D64 already closes N1

DCRP64 proves

$$
\boxed{
\int_0^{S_0}
\iint
\phi(x)\phi(y)
|\delta_{xy}E_p|_F^2
\,dxdy\,ds
\ge
c_E>0.
}
\tag{11.1}
$$

Therefore

$$
\boxed{
\delta E_p\not\equiv0.
}
\tag{11.2}
$$

---

# 12. All exact single-factor null channels are closed

Combine:

$$
\boxed{
\delta E_p\not\equiv0,
\qquad
\delta q\not\equiv0,
\qquad
\delta V\not\equiv0.
}
\tag{12.1}
$$

Therefore:

## Theorem D65.6 — Triple-Active Regime

No exact Round38 silence on the current nonzero branch can be explained by globally deleting one increment factor.

---

# 13. What is not yet proved

Theorem D65.6 does **not** imply

$$
\boxed{
\langle E_p,[V\cdot\nabla,\mathcal T_0]q\rangle\neq0.
}
$$

Three nonzero increments may still yield zero principal-value pairing through:

1. pair/support decorrelation;
2. tensor/angular orthogonality;
3. multiscale sign cancellation;
4. critical principal-value cancellation;
5. one factor becoming small precisely where the other two are large.

Thus the remaining problem is correlation, not amplitude.

---

# 14. Exact remaining Round38 equality condition

Define

$$
\boxed{
\mathfrak Q_{TR}
=
\operatorname{p.v.}
\int_0^{S_0}
\iint
[
\delta V\cdot\nabla K_0
]
:
\delta E_p
\,
\delta q
\,dxdy\,ds.
}
\tag{14.1}
$$

Round38 gives

$$
\boxed{
\mathfrak Q_{TR}
=
-2
\int_0^{S_0}
\langle
E_p,[V\cdot\nabla,\mathcal T_0]q
\rangle ds.
}
\tag{14.2}
$$

After D65, a silent X72 transport branch requires

$$
\boxed{
\mathfrak Q_{TR}=0
}
\tag{14.3}
$$

while all three increment fields are nontrivial.

This is a pure relational orthogonality condition.

---

# 15. Pair-support decorrelation is now a first-class escape

It remains possible that the large pair sets of

$$
\delta E_p,
\qquad
\delta q,
\qquad
\delta V
$$

have weak joint overlap.

Therefore the next observer must measure **joint pair-scale occupancy**, not only three separate increment norms.

---

# 16. Angular cancellation is genuinely different

Even with joint overlap,

$$
\boxed{
[\delta V\cdot\nabla K_0(z)]:\delta E_p
}
$$

has no fixed sign.

The Riesz kernel is angularly indefinite.

Thus a final coercive estimate must exploit actual Euler/vorticity geometry rather than generic Calderón–Zygmund positivity.

---

# 17. Relation to X72 Round41

Round41 shows that the special-cofactor commutator can be reduced by Piola structure and that its residual nonlocality is vorticity-generated.

After D65, any use of that reduction must resolve a genuinely three-way correlation among:

$$
\boxed{
\text{transport geometry},
\quad
\text{vorticity/cofactor defect},
\quad
\text{pressure-source variation}.
}
$$

---

# 18. Conditional compact-class source gap

If the admissible aligned/no-turnover class is compact in a topology that passes:

- the similarity Euler equations;
- the X72 Riesz pressure normalization;
- the positive covariance lower bound;
- the DCRP30 energy growth bound;

then Theorem D65.3 implies a positive distance of $q$ from spatial constants.

D65 does **not** claim this compactness unconditionally.

---

# 19. New X branch normal form

D64 gave forced pressure-defect increments.

D65 removes all factorwise exact nulls.

The remaining X branch is therefore

$$
\boxed{
\mathsf X_{\rm corr},
}
$$

a genuinely relational triple-increment cancellation class.

The global frontier is

$$
\boxed{
\text{rank-two continuation}
\Longrightarrow
\mathsf X_{\rm corr}
\vee
\mathsf T.
}
\tag{19.1}
$$

---

# 20. Status ledger

## PROVED this round

### D65-P1

$$
q=\partial_i\partial_j(V_iV_j).
$$

### D65-P2

A globally spatially constant pressure source vanishes under

$$
\mathcal E(R)=O(R^\kappa),
\qquad
\kappa<5.
$$

### D65-P3

Round38 N2 is impossible on the recurrent aligned/no-turnover branch.

### D65-P4

Round38 N3 is impossible on a nonzero vorticity branch.

### D65-P5

$$
(Az)\cdot\nabla K_0(z)\equiv0
\Rightarrow
A=0.
$$

### D65-P6

All exact factorwise Round38 null channels N1/N2/N3 are closed.

### D65-P7

The remaining silent X branch is purely relational/correlational.

---

# 21. New STOP

$$
\boxed{
\textbf{
STOP-D65:
D64 and D65 close every exact single-factor null channel in the X72 Round38 triple-increment identity. The pressure source cannot be globally constant in the strict DSS energy class, a constant velocity kills vorticity, and the pressure defect already has forced pair increments. Any remaining silent X branch is therefore a genuine pair-support, tensor-angle, scale-sign, or principal-value correlation cancellation among three individually active increments.
}
}
$$

---

# 22. Next autonomous step

## DCRP66 / X72-R49 — Triple-Increment Correlation Rigidity

**Working title**

> **Joint Pair-Scale Occupancy, Pressure-Source/Cofactor Overlap, and Angular Silence of the Transport–Riesz Triple Product**

Primary tasks:

1. define a joint pair-scale measure for
   $$
   |\delta E_p|,
   \quad
   |\delta q|,
   \quad
   |\delta V|;
   $$
2. determine whether D64 forced $E_p$ increments and D65 nonflat $q$ can be pairwise segregated under
   $$
   E_p=\mathcal T_0q+C_S^0;
   $$
3. use Round41's Piola/cofactor identity to replace generic $\delta C$ by actual vorticity-stress structure;
4. classify exact angular orthogonality of
   $$
   [\delta V\cdot\nabla K_0]:\delta E_p;
   $$
5. test whether zero triple correlation forces:
   - near-affine velocity;
   - pressure-source/cofactor scale separation;
   - vorticity-stress orientation lock;
   - or a new explicit cancellation normal form;
6. if an overlap lower bound is possible, derive a positive transport–Riesz transfer budget and feed it into X72 Round37.

Desired endpoint:

$$
\boxed{
\mathsf X_{\rm corr}
\Longrightarrow
\text{positive commutator transfer}
\vee
\text{one explicit relational cancellation normal form}.
}
$$

---

# 23. One-line checkpoint

All factorwise Round38 nulls are now gone: the pressure source cannot be globally flat, the velocity cannot be constant, and the pressure-response defect already has forced increments, so any surviving X72 silence is a genuine three-factor correlation/angular cancellation rather than an amplitude-degenerate equality mode.

---

**End checkpoint:** DCRP65 / X72-R48  
**Next:** DCRP66 / X72-R49 — Triple-Increment Correlation Rigidity.
