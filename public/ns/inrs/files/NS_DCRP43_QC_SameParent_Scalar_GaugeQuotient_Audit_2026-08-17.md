# DCRP43-QC — Same-Parent Scalar Reroot Audit, Gauge-Quotient Collapse, and the Gauge-Invariant Pancake Frontier

**Series:** Independent Navier–Stokes Research Series  
**Date:** 2026-08-17  
**Status:** Research proof checkpoint / correction-and-reduction round  
**Primary internal dependencies:**
- `NS_DCRP_30_SameParent_DSS_ExponentWindow_TailEscape_2026-08-17.md`
- `NS_DCRP_34_KelvinQuotient_OseenCriticality_CirculationCascade_2026-08-17.md`
- `NS_DCRP_35_DSS_Enstrophy_AnnularStrain_AffineJetSupplier_2026-08-17.md`
- `NS_DCRP_40_RankTwo_PlanarCovariance_FloquetCompression_2026-08-17.md`
- `NS_DCRP_42_PlanarShearScalar_PancakeTurnover_2026-08-17.md`
- previous working note `NS_DCRP43_Poincare_Scalar_Transfer_Material_Nonrecurrence_2026-08-17.md`

**External calibration checked this round:**
- D. Chae & T.-P. Tsai, *On discretely self-similar solutions of the Euler equations*, arXiv:1304.7414.
- D. Chae, *Remarks on the asymptotically discretely self-similar solutions of the Navier-Stokes and the Euler equations*, arXiv:1306.0305.
- P. Constantin, M. Ignatova, V. Vicol, *On putative self-similarity for incompressible 3D Euler*, arXiv:2602.17570.
- G. Seregin, *On potential Type II blowups for the Navier-Stokes equations*, arXiv:2606.29468.

No full Navier–Stokes regularity claim is made.

---

# 0. Executive result

The quotient-correct audit produces a **mixed negative/positive result**.

## Positive

The DCRP-30 exact same-parent reroot identity gives exact transformation laws for the planar shear scalar and its horizontal gradient.

If

$$
v_{n+1}(y,\tau)
=
c_n
v_n
\left(
b_n+\lambda_ny,
d_n+c_n\lambda_n\tau
\right),
$$

with

$$
\lambda_n=\frac{\ell_{n+1}}{\ell_n},
\qquad
\mu_n=\frac{a_{n+1}}{a_n},
\qquad
c_n=\frac{\lambda_n}{\mu_n},
$$

then, modulo the natural potential gauge,

$$
\boxed{
[q_{n+1}]
=
c_n
[q_n]\circ\mathcal R_n,
}
$$

where

$$
\mathcal R_n(y,\tau)
=
\left(
b_n+\lambda_ny,
d_n+c_n\lambda_n\tau
\right).
$$

The horizontal gradient, hence planar vorticity, is gauge independent and satisfies exactly

$$
\boxed{
\nabla_hq_{n+1}
=
c_n\lambda_n
(\nabla_hq_n)\circ\mathcal R_n,
}
$$

and therefore

$$
\boxed{
\Omega_{h,n+1}
=
\frac{\lambda_n^2}{\mu_n}
\Omega_{h,n}\circ\mathcal R_n.
}
$$

In the exact strict DSS return,

$$
\lambda=e^{-\gamma S_0},
\qquad
\mu=e^{(1-2\gamma)S_0},
$$

hence

$$
c=e^{-(1-\gamma)S_0},
$$

and

$$
\boxed{
\frac{\lambda^2}{\mu}
=
e^{-S_0}.
}
$$

Thus the normalized planar vorticity reroot multiplier is exactly $e^{-S_0}$, independent of $\gamma$.

## Correction

The absolute scalar

$$
q=w-\partial_3\phi
$$

is not invariant under the residual planar-potential gauge

$$
\phi
\mapsto
\phi+h(z,s).
$$

Indeed

$$
q
\mapsto
q-\partial_zh.
$$

Therefore the raw scalar capacity

$$
\int_K|q|^pdy
$$

and likewise the gauge-fixed DCRP-42 quantity based on

$$
r=\eta(s)q
$$

are **not intrinsic geometric observables without a declared potential gauge**.

The quotient of $q$ by this gauge is locally equivalent to the planar vorticity:

$$
\boxed{
[q]_{\mathcal G}
\longleftrightarrow
\Omega_h
=
J\nabla_hq.
}
$$

Consequently the DCRP-42 scalar route is a very useful **dynamical scalarization** of the planar-vorticity branch, but its raw $|r|^p$ turnover cannot yet be promoted to a new gauge-invariant same-parent parent-level tax.

This is a genuine reduction.

The next native target is no longer “raw scalar turnover $\Rightarrow$ contradiction.”

It is:

$$
\boxed{
\textbf{
Gauge-Invariant Sheet Turnover /
Quotient Scalar Oscillation /
Finite-PFET Coupling.
}
}
$$

---

# 1. Notation repair

DCRP-30 uses $r_n$ for the physical spatial root scale, while DCRP-42 uses $r$ for the renormalized shear scalar.

To avoid collision in this checkpoint, write the Type-II spatial root scale as

$$
\boxed{
\ell_n.
}
$$

Thus the exact Type-II normalization is

$$
v_n(y,\tau)
=
\frac{\ell_n}{a_n}
U
\left(
x_n+\ell_n y,
t_n+\frac{\ell_n^2}{a_n}\tau
\right).
$$

Define

$$
\boxed{
\lambda_n
=
\frac{\ell_{n+1}}{\ell_n},
}
$$

$$
\boxed{
\mu_n
=
\frac{a_{n+1}}{a_n},
}
$$

and

$$
\boxed{
c_n
=
\frac{\lambda_n}{\mu_n}.
}
$$

Then DCRP-30 proves exactly

$$
\boxed{
v_{n+1}(y,\tau)
=
c_n
v_n
\left(
b_n+\lambda_ny,
d_n+c_n\lambda_n\tau
\right).
}
\tag{1.1}
$$

No PDE estimate is used in (1.1).

---

# 2. Planar potential–shear representation

On a fixed-plane planar-vorticity patch, DCRP-42 writes

$$
v_h=\nabla_h\phi,
$$

$$
w=v_3,
$$

and defines

$$
\boxed{
q=w-\partial_3\phi.
}
\tag{2.1}
$$

The planar vorticity is

$$
\boxed{
\Omega_h
=
\left(
\partial_2q,
-\partial_1q
\right)
=
J\nabla_hq.
}
\tag{2.2}
$$

The crucial point for the present audit is that $\phi$ is determined by $v_h$ only up to

$$
\boxed{
\phi
\mapsto
\phi+h(z,\tau),
}
\tag{2.3}
$$

because

$$
\nabla_hh(z,\tau)=0.
$$

Therefore

$$
\boxed{
q
\mapsto
q-h_z(z,\tau).
}
\tag{2.4}
$$

The horizontal gradient is invariant:

$$
\boxed{
\nabla_hq
\mapsto
\nabla_hq.
}
\tag{2.5}
$$

Hence $\Omega_h$ is gauge invariant.

---

# 3. Exact same-parent transformation of the planar potential

Let

$$
z
=
b_n+\lambda_ny,
$$

$$
\sigma
=
d_n+c_n\lambda_n\tau.
$$

From the horizontal component of (1.1),

$$
v_{h,n+1}(y,\tau)
=
c_n
\nabla_h\phi_n(z,\sigma).
$$

A compatible potential is therefore

$$
\boxed{
\phi_{n+1}(y,\tau)
=
\frac{c_n}{\lambda_n}
\phi_n(z,\sigma)
+
h_n(y_3,\tau),
}
\tag{3.1}
$$

where

$$
h_n
$$

is the residual potential gauge.

Indeed,

$$
\nabla_{h,y}
\phi_{n+1}
=
\frac{c_n}{\lambda_n}
\lambda_n
\nabla_{h,z}\phi_n
=
c_n
\nabla_{h,z}\phi_n.
$$

The vertical velocity satisfies

$$
\boxed{
w_{n+1}(y,\tau)
=
c_n
w_n(z,\sigma).
}
\tag{3.2}
$$

Meanwhile

$$
\partial_{y_3}\phi_{n+1}
=
c_n
\partial_{z_3}\phi_n(z,\sigma)
+
\partial_{y_3}h_n.
$$

Hence

$$
\boxed{
q_{n+1}(y,\tau)
=
c_n
q_n(z,\sigma)
-
\partial_{y_3}h_n(y_3,\tau).
}
\tag{3.3}
$$

This is the exact same-parent scalar reroot law.

---

# 4. The scalar reroot law is naturally a quotient law

Define the gauge subspace

$$
\boxed{
\mathcal G
=
\left\{
g(y_3,\tau)
\right\}.
}
\tag{4.1}
$$

Define the quotient scalar class

$$
\boxed{
[q]
\in
\mathcal Q
:=
\mathcal S/\mathcal G.
}
\tag{4.2}
$$

Equation (3.3) then becomes independent of the arbitrary $h_n$:

$$
\boxed{
[q_{n+1}]
=
c_n
[q_n]\circ\mathcal R_n,
}
\tag{4.3}
$$

where

$$
\mathcal R_n(y,\tau)
=
(z,\sigma).
$$

## Theorem D43-QC.1 — Same-Parent Shear Quotient Covariance

The natural same-parent transformation of the planar shear scalar is not an equality of representatives $q$, but the quotient covariance

$$
\boxed{
[q_{n+1}]
=
\frac{\lambda_n}{\mu_n}
[q_n]\circ\mathcal R_n.
}
$$

This is exact.

---

# 5. Exact gauge-invariant planar-vorticity covariance

Differentiate (3.3) horizontally.

Because

$$
\partial_{y_i}
h_n(y_3,\tau)=0
\qquad
(i=1,2),
$$

we obtain

$$
\partial_{y_i}q_{n+1}
=
c_n\lambda_n
\partial_{z_i}q_n(z,\sigma).
$$

Thus

$$
\boxed{
\nabla_hq_{n+1}
=
c_n\lambda_n
(\nabla_hq_n)\circ\mathcal R_n.
}
\tag{5.1}
$$

Since

$$
c_n\lambda_n
=
\frac{\lambda_n^2}{\mu_n},
$$

the planar vorticity transforms as

$$
\boxed{
\Omega_{h,n+1}
=
\frac{\lambda_n^2}{\mu_n}
\Omega_{h,n}\circ\mathcal R_n.
}
\tag{5.2}
$$

## Theorem D43-QC.2 — Planar Vorticity Reroot Covariance

Equation (5.2) is exact and independent of the residual potential gauge.

---

# 6. Strict DSS factors

In the exact strict same-parent DSS branch, with

$$
\gamma
=
\frac1{\alpha+1},
$$

the period scaling may be written

$$
\boxed{
\lambda
=
e^{-\gamma S_0}.
}
\tag{6.1}
$$

DCRP-34 gives the exact amplitude-normalization ratio

$$
\boxed{
\mu
=
e^{(1-2\gamma)S_0}.
}
\tag{6.2}
$$

Therefore

$$
\boxed{
c
=
\frac{\lambda}{\mu}
=
e^{-(1-\gamma)S_0}.
}
\tag{6.3}
$$

and

$$
\boxed{
c\lambda
=
\frac{\lambda^2}{\mu}
=
e^{-S_0}.
}
\tag{6.4}
$$

The normalized root-transition multipliers are therefore:

### velocity / scalar representative

$$
\boxed{
v,\ [q]:
\quad
e^{-(1-\gamma)S_0};
}
\tag{6.5}
$$

### planar vorticity / horizontal shear gradient

$$
\boxed{
\Omega_h,\ \nabla_hq:
\quad
e^{-S_0}.
}
\tag{6.6}
$$

The second factor is independent of $\gamma$.

---

# 7. Quotient-correct physical representatives

The normalized velocity is

$$
v_n
=
\frac{\ell_n}{a_n}
U.
$$

Therefore the physical velocity reconstruction factor is

$$
\boxed{
\frac{a_n}{\ell_n}.
}
\tag{7.1}
$$

Since $q$ has the same velocity scaling as $v$, define the physical shear representative

$$
\boxed{
\widehat q_n
=
\frac{a_n}{\ell_n}
q_n.
}
\tag{7.2}
$$

At matched physical spacetime points,

$$
\widehat q_{n+1}
=
\widehat q_n
$$

modulo the corresponding transported potential gauge.

Indeed,

$$
\frac{a_{n+1}}{\ell_{n+1}}
c_n
=
\frac{\mu_na_n}{\lambda_n\ell_n}
\frac{\lambda_n}{\mu_n}
=
\frac{a_n}{\ell_n}.
$$

Thus the same-parent reroot itself introduces no physical shear discrepancy.

Similarly physical vorticity is reconstructed by

$$
\boxed{
\widehat\Omega_{h,n}
=
\frac{a_n}{\ell_n^2}
\Omega_{h,n}.
}
\tag{7.3}
$$

Using (5.2),

$$
\frac{a_{n+1}}{\ell_{n+1}^2}
\frac{\lambda_n^2}{\mu_n}
=
\frac{\mu_na_n}{\lambda_n^2\ell_n^2}
\frac{\lambda_n^2}{\mu_n}
=
\frac{a_n}{\ell_n^2}.
$$

Hence

$$
\boxed{
\widehat\Omega_{h,n+1}
=
\widehat\Omega_{h,n}
}
\tag{7.4}
$$

at matched physical spacetime points.

## Theorem D43-QC.3 — Root Independence of Physical Shear/Vorticity Reconstruction

The canonical same-parent reroot exactly cancels the normalized $q$ and $\Omega_h$ multipliers once the physical reconstruction factors are restored.

Therefore the reroot multipliers themselves are **coordinate/normalization covariance**, not a same-parent physical tax.

---

# 8. Exact transformation of normalized scalar $L^p$ capacity

Let

$$
A
$$

be a normalized region in the $(n+1)$ root and define its matched region in the $n$ root:

$$
\boxed{
A'
=
b_n+\lambda_n A.
}
\tag{8.1}
$$

For a gauge-compatible representative with $h_{n,z}=0$, or for a quotient seminorm with the gauge removed, the scalar amplitude scales by $c_n$ and

$$
dy
=
\lambda_n^{-3}dz.
$$

Therefore

$$
\boxed{
\int_A|q_{n+1}|^pdy
=
c_n^p
\lambda_n^{-3}
\int_{A'}|q_n|^pdz.
}
\tag{8.2}
$$

Thus the normalized capacity reroot factor is

$$
\boxed{
c_n^p\lambda_n^{-3}
=
\lambda_n^{p-3}\mu_n^{-p}.
}
\tag{8.3}
$$

In the strict DSS branch,

$$
\boxed{
\lambda^{p-3}\mu^{-p}
=
e^{[3\gamma-p(1-\gamma)]S_0}.
}
\tag{8.4}
$$

This is **not** the DCRP-42 material-flow multiplier

$$
e^{[3\gamma+p(1-2\gamma)]S_0}.
$$

They represent two different operations:

1. same-parent coordinate reroot;
2. material transport within one DSS profile.

They must not be conflated.

---

# 9. Quotient-correct physical scalar capacity

The physical region corresponding to normalized $A$ has volume element

$$
dx
=
\ell_n^3dy.
$$

Physical shear amplitude scales as

$$
q^{phys}
=
\frac{a_n}{\ell_n}q_n.
$$

Therefore define

$$
\boxed{
\widehat{\mathcal Q}_{p,n}(A)
=
a_n^p
\ell_n^{3-p}
\int_A|q_n|^pdy.
}
\tag{9.1}
$$

Using (8.2),

$$
\begin{aligned}
\widehat{\mathcal Q}_{p,n+1}(A)
&=
a_{n+1}^p
\ell_{n+1}^{3-p}
c_n^p\lambda_n^{-3}
\int_{A'}|q_n|^p
\\
&=
\mu_n^p
\lambda_n^{3-p}
a_n^p\ell_n^{3-p}
\left(
\frac{\lambda_n}{\mu_n}
\right)^p
\lambda_n^{-3}
\int_{A'}|q_n|^p
\\
&=
a_n^p\ell_n^{3-p}
\int_{A'}|q_n|^p.
\end{aligned}
$$

Hence

$$
\boxed{
\widehat{\mathcal Q}_{p,n+1}(A)
=
\widehat{\mathcal Q}_{p,n}(A').
}
\tag{9.2}
$$

## Theorem D43-QC.4 — Same-Parent Capacity Cancellation

The exact reroot scaling of the raw normalized scalar capacity is entirely canceled by the physical amplitude/volume reconstruction factors.

Therefore

$$
\boxed{
\int|q|^pdy
}
$$

is not itself a same-parent invariant or a parent-level tax.

A parent-level statement must use a quotient-correct physical or gauge-invariant observable.

---

# 10. Exact normalized vorticity $L^p$ reroot factor

From (5.2),

$$
|\Omega_{h,n+1}|^p
=
\left(
\frac{\lambda_n^2}{\mu_n}
\right)^p
|\Omega_{h,n}|^p\circ\mathcal R_n.
$$

Thus

$$
\boxed{
\int_A|\Omega_{h,n+1}|^pdy
=
\lambda_n^{2p-3}
\mu_n^{-p}
\int_{A'}|\Omega_{h,n}|^pdz.
}
\tag{10.1}
$$

In strict DSS,

$$
\boxed{
\lambda^{2p-3}\mu^{-p}
=
e^{(3\gamma-p)S_0}.
}
\tag{10.2}
$$

For $p=2$:

$$
\boxed{
\int_A|\Omega_{h,n+1}|^2dy
=
e^{-(2-3\gamma)S_0}
\int_{A'}|\Omega_{h,n}|^2dz.
}
\tag{10.3}
$$

The exponent

$$
\boxed{
2-3\gamma
}
$$

is exactly the positive similarity enstrophy-demand coefficient appearing in DCRP-35.

This identifies a direct scaling bridge between the planar scalar representation and the existing enstrophy ledger.

---

# 11. Physical vorticity capacity is root independent

The physical vorticity reconstruction is

$$
\Omega^{phys}
=
\frac{a_n}{\ell_n^2}\Omega_n.
$$

Hence

$$
\boxed{
\widehat{\mathcal O}_{p,n}(A)
=
a_n^p
\ell_n^{3-2p}
\int_A|\Omega_n|^pdy.
}
\tag{11.1}
$$

Using (10.1),

$$
\boxed{
\widehat{\mathcal O}_{p,n+1}(A)
=
\widehat{\mathcal O}_{p,n}(A').
}
\tag{11.2}
$$

Again the same-parent root scaling cancels exactly.

So the DCRP-35 enstrophy demand is a dynamical periodic-balance issue, not a root-normalization mismatch.

---

# 12. Gauge quotient of $q$ is locally equivalent to planar vorticity

Define

$$
\mathcal G
=
\{
g(z,s)
\}.
$$

Consider the map

$$
\boxed{
\mathfrak D_h:
[q]
\mapsto
\nabla_hq.
}
\tag{12.1}
$$

This is well defined because

$$
\nabla_hg(z,s)=0.
$$

If

$$
\mathfrak D_h[q_1]
=
\mathfrak D_h[q_2],
$$

then

$$
\nabla_h(q_1-q_2)=0.
$$

On each connected horizontal patch,

$$
q_1-q_2
=
g(z,s)
$$

for some $g\in\mathcal G$.

Therefore

$$
[q_1]=[q_2].
$$

So $\mathfrak D_h$ is injective.

Since

$$
\Omega_h
=
J\nabla_hq,
$$

the gauge quotient class of $q$ contains exactly the same local pointwise structural information as the planar vorticity.

## Theorem D43-QC.5 — Gauge-Quotient Collapse

On a connected regular horizontal patch,

$$
\boxed{
[q]_{\mathcal G}
\longleftrightarrow
\Omega_h
}
$$

is locally one-to-one.

Equivalently,

$$
\boxed{
\text{the intrinsic state content of the planar shear scalar modulo potential gauge is planar vorticity}.
}
$$

This is a major interpretation correction.

The scalar formulation is still dynamically useful, but it is not a new independent gauge-invariant state variable.

---

# 13. Raw scalar $L^p$ capacity is not gauge invariant

Under

$$
q
\mapsto
q-g(z,s),
$$

in general

$$
\int_K|q|^pdy
\neq
\int_K|q-g|^pdy.
$$

Likewise

$$
r=\eta(s)q
$$

changes by

$$
r
\mapsto
r-\eta(s)g(z,s).
$$

Therefore the DCRP-42 quantity

$$
\boxed{
\mathcal Q_{p,K}
=
\int_K|r|^pdy
}
$$

is a **gauge-fixed scalar capacity**, not an intrinsic planar-vorticity invariant.

DCRP-42 explicitly assumes a chosen periodic potential gauge, so its theorem remains mathematically valid in that declared gauge.

What fails is the stronger interpretation:

$$
\boxed{
\text{raw }|r|^p\text{ throughput}
\Rightarrow
\text{gauge-independent parent-level tax}.
}
$$

That implication is not established.

---

# 14. The $G=0$ branch also needs gauge bookkeeping

DCRP-42 defines

$$
w=F(q,z,s)
$$

and

$$
\boxed{
G
=
\partial_zF+2a(s).
}
\tag{14.1}
$$

Under

$$
q'=q-g(z,s),
$$

the same physical $w$ is represented by

$$
F'(q',z,s)
=
F(q'+g(z,s),z,s).
$$

At fixed $q'$,

$$
\partial_zF'
=
F_z
+
F_qg_z.
$$

Thus

$$
\boxed{
G'
=
G
+
F_qg_z.
}
\tag{14.2}
$$

Therefore the bare condition

$$
G=0
$$

is not invariant under an unrestricted residual potential gauge unless, for example,

$$
g_z=0
$$

or

$$
F_q=0,
$$

or a canonical gauge has already been fixed.

## Consequence

The fixed-plane $G=0$ scalar eigenmode should be treated as a **gauge-fixed equality branch** unless a separate canonical-gauge theorem or gauge-invariant reformulation is supplied.

This does not invalidate the calculations within the declared gauge.

It changes the strength of the branch as a physical classification statement.

---

# 15. Reclassification of the previous DCRP43 working note

The previous working note proved, in the DCRP-42 periodic gauge:

$$
r\circ\Phi
=
e^{(1-2\gamma)S_0}r,
$$

and corresponding $|r|^p$ material-transfer identities.

These remain algebraically correct under the stated fixed gauge and canonical-branch assumptions.

However the following interpretations must be downgraded:

## Still valid

- Poincaré scalar eigenfunction in the chosen periodic gauge;
- fixed-similarity-core scalar throughput identity;
- nonrecurrence of nonzero scalar representatives **within that gauge**;
- existence of normalized similarity-coordinate turnover relative to a fixed normalized core.

## Not yet gauge/quotient invariant

- a native physical material-sheet tax;
- a new independent same-parent scalar obstruction;
- a gauge-independent nonzero-label nonrecurrence theorem;
- an intrinsic transition carrier defined solely by $|r|^p$.

Therefore the earlier object

$$
\mathcal C_{\rm turn}(K)
=
K\triangle\Phi^{-1}(K)
$$

is presently best interpreted as a

$$
\boxed{
\text{fixed-similarity-observer turnover carrier},
}
$$

not yet as an intrinsic physical sheet-transition carrier.

---

# 16. Fixed similarity core versus moving physical core

A fixed normalized core

$$
K
subset
\mathbb R^3_y
$$

corresponds at root $n$ to the physical region

$$
\boxed{
K_n^{phys}
=
x_n+\ell_nK.
}
\tag{16.1}
$$

Under strict DSS,

$$
\ell_{n+1}
=
\lambda\ell_n,
\qquad
0<\lambda<1.
$$

Thus the physical observation window shrinks from one root to the next.

Material labels leaving a fixed **similarity** core may therefore reflect:

1. actual physical transport;
2. shrinking/recentering of the observation window;
3. both.

Hence

$$
\boxed{
\text{fixed-similarity turnover}
\neq
\text{intrinsic physical sheet transition}.
}
$$

A same-parent replenishment theorem must quotient this observer-window motion.

This is the exact analogue of the DCRP-32 → DCRP-34 Kelvin correction.

---

# 17. Main conclusion of the quotient audit

The audit therefore does **not** produce a new positive scalar tax.

Instead it produces a clean structural reduction:

$$
\boxed{
\textbf{
STOP-D43-QC-A:
Raw pancake scalar capacity is not a native same-parent invariant.
}
}
$$

More precisely:

1. root-normalization covariance is completely explicit and removable;
2. residual potential gauge changes $q$ by functions of $(z,s)$;
3. the quotient class $[q]$ is locally equivalent to planar vorticity;
4. the gauge-invariant $p=2$ scaling returns directly to the DCRP-35 enstrophy exponent $2-3\gamma$.

Thus any genuinely new scalar obstruction must exploit something beyond the already-known gauge-invariant planar-vorticity state.

Possible genuinely new content could still lie in:

- lower-order quotient norms of $[q]$;
- scalar level-set topology;
- sheet-support transport;
- gauge-invariant oscillation;
- noncommutation between gauge projection and material transport;
- finite PFET coupling.

---

# 18. Correct next variable: quotient scalar oscillation

A natural gauge-invariant lower-order scalar observable is

$$
\boxed{
\|[q]\|_{L^p/\mathcal G}
=
\inf_{g=g(z,s)}
\|q-g\|_{L^p(K)}.
}
\tag{18.1}
$$

This is invariant under

$$
q\mapsto q+h(z,s).
$$

For corresponding normalized sets under same-parent reroot, the gauge subspace maps into itself, hence

$$
\boxed{
\|[q_{n+1}]\|_{L^p(A)/\mathcal G}
=
c_n\lambda_n^{-3/p}
\|[q_n]\|_{L^p(A')/\mathcal G}.
}
\tag{18.2}
$$

Equivalently,

$$
\boxed{
\|[q_{n+1}]\|_{L^p/\mathcal G}^p
=
\lambda_n^{p-3}\mu_n^{-p}
\|[q_n]\|_{L^p/\mathcal G}^p.
}
\tag{18.3}
$$

This is the correct gauge-quotient analogue of the raw scalar capacity reroot law.

What is not yet known is whether the DCRP-42 material equation descends to a closed positive-source equation for this quotient norm.

That is now a precise next problem.

---

# 19. Gauge projection does not obviously commute with material transport

Let

$$
\Pi_{\mathcal G}
$$

denote a chosen projection onto the gauge subspace, for example a horizontal slice mean in a product-type core.

Define

$$
\boxed{
q^\circ
=
q-\Pi_{\mathcal G}q.
}
\tag{19.1}
$$

Then

$$
q^\circ
$$

is gauge invariant under the corresponding canonical projection.

However

$$
D_s
$$

contains the normal velocity

$$
W_3=w=F(q,z,s),
$$

which can depend horizontally through $q$.

Therefore in general

$$
\boxed{
[D_s,\Pi_{\mathcal G}]
\neq0.
}
\tag{19.2}
$$

This commutator is potentially valuable.

It measures precisely the failure of the scalar material dynamics to descend trivially to the gauge quotient.

A nonzero commutator may encode:

- sheet exchange;
- vertical layer transport;
- non-affine normal shear;
- boundary/matching-layer coupling.

This is a much more promising native scalar object than raw $|q|^p$ turnover.

---

# 20. Proposed next theorem target

## DCRP44 — Gauge-Projected Pancake Turnover / Transport-Projection Commutator

Choose a canonical gauge projection

$$
\Pi_{\mathcal G}.
$$

Derive the exact equation for

$$
q^\circ
=
(I-\Pi_{\mathcal G})q.
$$

Starting from

$$
D_sq+k(s)q=0
$$

on the gauge-fixed $G=0$ branch,

apply

$$
I-\Pi_{\mathcal G}
$$

to obtain schematically

$$
\boxed{
D_sq^\circ
+
k(s)q^\circ
=
-[D_s,\Pi_{\mathcal G}]q.
}
\tag{20.1}
$$

The right-hand side is gauge invariant once $\Pi_{\mathcal G}$ is fixed canonically.

The desired dichotomy is:

$$
\boxed{
[D_s,\Pi_{\mathcal G}]q\neq0
}
$$

giving a finite sheet/layer transition observable,

or

$$
\boxed{
[D_s,\Pi_{\mathcal G}]q=0,
}
$$

in which case the quotient scalar inherits the homogeneous amplification law and one may seek a gauge-invariant turnover theorem.

This is the corrected scalar frontier.

---

# 21. Coupling to DCRP-35 and DCRP-31

If the quotient scalar route collapses to its gradient,

$$
\nabla_hq
\leftrightarrow
\Omega_h,
$$

then the next ledger is already available:

DCRP-35 proves

$$
\boxed{
\mathcal S(R)
=
(2-3\gamma)\mathcal O(R)
+
\mathcal J_\omega(R),
}
$$

so a nonzero periodic vorticity core requires

$$
\boxed{
\text{positive vortex stretching}
\quad\text{or}\quad
\text{inward enstrophy turnover}.
}
$$

It also localizes the external strain supplier to a finite annulus.

DCRP-31 independently forces a finite-radius inward PFET matching layer.

Therefore a successful DCRP44 commutator theorem should be connected to the already finite structures:

$$
\boxed{
\text{gauge-projected scalar transition}
}
$$

$$
\longrightarrow
$$

$$
\boxed{
\text{finite annular vorticity/strain supplier}
}
$$

and/or

$$
\boxed{
\text{finite PFET matching layer}.
}
$$

This is more precise than trying to tax the raw scalar $L^p$ flux directly.

---

# 22. NTLA-O interpretation

This round is an explicit NS example of NTLA-O quotient discipline.

The raw observer sees

$$
q.
$$

But the physical planar-vorticity structure is insensitive to

$$
q
\mapsto
q+g(z,s).
$$

Therefore the correct observer kernel must first quotient the gauge direction:

$$
\boxed{
q
\mapsto
[q]_{\mathcal G}.
}
$$

Only after this quotient may one ask whether a difference is native.

Thus:

$$
\boxed{
\text{Raw scalar difference}
\not\Rightarrow
\text{physical structural difference}.
}
$$

The correct chain is

$$
\boxed{
q
\rightarrow
[q]_{\mathcal G}
\rightarrow
\nabla_hq
\leftrightarrow
\Omega_h.
}
$$

This is precisely the reason the rebuilt NTLA-O framework is useful for the current NS frontier.

---

# 23. Status ledger

## PROVED in this round

### QC-1

Exact same-parent scalar transformation modulo potential gauge:

$$
[q_{n+1}]
=
\frac{\lambda_n}{\mu_n}
[q_n]\circ\mathcal R_n.
$$

### QC-2

Exact planar-vorticity reroot covariance:

$$
\Omega_{h,n+1}
=
\frac{\lambda_n^2}{\mu_n}
\Omega_{h,n}\circ\mathcal R_n.
$$

### QC-3

Strict-DSS normalized planar-vorticity multiplier:

$$
e^{-S_0}.
$$

### QC-4

Root independence of physical shear and physical planar vorticity at matched physical spacetime points.

### QC-5

Exact normalized scalar $L^p$ reroot factor:

$$
\lambda_n^{p-3}\mu_n^{-p}.
$$

### QC-6

Exact physical scalar-capacity reroot cancellation:

$$
a_n^p\ell_n^{3-p}
\int|q_n|^p
$$

is representation independent at matched physical sets.

### QC-7

Gauge quotient of $q$ is locally equivalent to planar vorticity.

### QC-8

The bare $G=0$ condition is gauge dependent under unrestricted residual $z$-dependent potential gauge unless extra gauge restrictions are imposed.

---

## DOWNGRADED

The previous interpretation

$$
\boxed{
\text{raw }|r|^p\text{ turnover}
=
\text{new native same-parent scalar tax}
}
$$

is not justified.

The turnover theorem remains valid in the declared periodic gauge as a normalized similarity-observer statement.

---

## OPEN

1. canonical gauge existence and uniqueness;
2. gauge-projected scalar turnover;
3. material-transport / gauge-projection commutator;
4. finite-annulus localization of any nonzero quotient residual;
5. coupling to DCRP-31 PFET and DCRP-35 annular strain;
6. eventual elimination or classification of the rank-two pancake survivor.

---

# 24. New exact STOP

$$
\boxed{
\textbf{
STOP-D43-QC:
Raw scalar-capacity turnover does not survive the required quotient audit as an independent native tax.
}
}
$$

The scalar route is not discarded.

It is **reduced** to the gauge-invariant question:

$$
\boxed{
\textbf{
Does the gauge-quotient scalar dynamics carry a nonzero transport-projection residual?
}
}
$$

This becomes DCRP44.

---

# 25. Next autonomous step

## DCRP44

**Working title:**

> **Gauge-Projected Pancake Scalar, Transport–Projection Commutator, and Finite Sheet-Replenishment Carrier**

Primary task:

1. select a canonical local gauge projection;
2. derive
   $$
   [D_s,\Pi_{\mathcal G}]q;
   $$
3. determine whether zero commutator forces a stronger planar normal form;
4. if the commutator is nonzero, localize it to a finite sheet/matching carrier;
5. compare its support/work with DCRP-31 PFET and DCRP-35 annular strain supply.

A useful outcome exists in either direction:

- **commutator zero:** stronger rigidity / scalar branch collapses toward an exact sheet eigenmode;
- **commutator nonzero:** native gauge-invariant replenishment defect.

---

# 26. One-line checkpoint

The quotient audit removes the raw scalar $L^p$ turnover as an independent same-parent tax, identifies the intrinsic scalar quotient with planar vorticity, and replaces the old frontier by a sharper gauge-projected transport-commutator problem.

---

**End checkpoint:** DCRP43-QC  
**Next:** DCRP44 — Gauge-Projected Pancake Turnover / Transport–Projection Commutator.
