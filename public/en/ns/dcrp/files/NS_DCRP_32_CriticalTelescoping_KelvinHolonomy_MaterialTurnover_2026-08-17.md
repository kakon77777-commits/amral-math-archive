# NS-DCRP-32 — Critical Telescoping No-Go, DSS Kelvin-Holonomy Rigidity, and Mandatory Material Turnover

- date: 2026-08-17
- status: research proof checkpoint
- canonical source: UTF-8 Markdown
- canonical math delimiters: `$...$` and `$$...$$`
- objective:
  1. audit whether the mandatory DCRP-31 PFET matching-layer payment can contradict the finite Navier--Stokes kinetic-energy budget by direct summation;
  2. prove the exact critical telescoping obstruction to every energy-homogeneous summation closure;
  3. replace energy summation by the Euler Kelvin/Weber material invariant;
  4. derive the DSS similarity-circulation contraction law;
  5. prove that strict DSS recurrence with zero material holonomy forces vanishing circulation and, under the critical tail growth, the zero profile;
  6. isolate mandatory material turnover/holonomy as the non-energy return carrier of the strict Type-II branch.
- no full Navier--Stokes regularity claim is made.
- principal external primary sources:
  - P. Constantin, M. Ignatova, V. Vicol, *On putative self-similarity for incompressible 3D Euler*, arXiv:2602.17570v3;
  - D. Chae, T.-P. Tsai, *On discretely self-similar solutions of the Euler equations*, arXiv:1304.7414;
  - L. Xue, *Discretely self-similar singular solutions for the incompressible Euler equations*, arXiv:1408.6619v2.
- internal dependencies:
  - DCRP-29 raw-energy atom/material crossing split;
  - DCRP-30 same-parent DSS recurrence and exponent window;
  - DCRP-31 radial PFET matching-layer rigidity.
- no novelty/priority claim is made without independent audit.

---

# 1. Executive result

DCRP-31 proved that every nonzero smooth strict compact DSS Euler profile in

$$
\boxed{
1<\alpha<\frac32
}
\tag{1.1}
$$

or equivalently

$$
\boxed{
\frac25<\gamma<\frac12,
\qquad
\gamma=\frac1{\alpha+1},
}
\tag{1.2}
$$

must have a finite-radius inward period-averaged Euler pressure--kinetic flux.

The first result of DCRP-32 is a structural NO-GO.

In the strict geometric atom-free recurrence,

$$
\boxed{
\beta_{n+1}
=
q\beta_n,
\qquad
0<q<1,
}
\tag{1.3}
$$

where

$$
\beta_n
$$

is the raw physical kinetic energy associated with the shrinking Type-II core.

Any raw return payment which is homogeneous of the same physical kinetic-energy degree has the form

$$
\boxed{
\mathcal P_n^{raw}
=
\beta_n
\mathcal P_\ast
+
o(\beta_n)
}
\tag{1.4}
$$

for a fixed normalized profile payment

$$
\mathcal P_\ast.
$$

Therefore:

$$
\boxed{
\sum_{n=0}^\infty
\mathcal P_n^{raw}
<
\infty.
}
\tag{1.5}
$$

In the exact geometric model:

$$
\boxed{
\sum_{n=0}^\infty
(1-q)\beta_n
=
\beta_0.
}
\tag{1.6}
$$

Thus:

$$
\boxed{
\textbf{
mandatory normalized PFET per DSS return}
\not\Rightarrow
\textbf{
divergence of total raw kinetic-energy transfer}.
}
}
\tag{1.7}
$$

This is not a missing estimate.

It is a critical telescoping mechanism.

Any closure based only on adding kinetic-energy-homogeneous raw payments across the DSS return chain is structurally incapable of producing a contradiction.

The second result replaces raw-energy summation with a material Euler invariant.

For a DSS Euler solution written in similarity variables, let:

$$
V(y,s)
$$

be periodic in:

$$
s
$$

with period:

$$
S_0.
$$

Define the similarity material velocity:

$$
\boxed{
W(y,s)
=
\gamma y
+
V(y,s).
}
\tag{1.8}
$$

Let:

$$
Y(a,s)
$$

be the similarity Lagrangian flow:

$$
\boxed{
\partial_sY
=
W(Y,s),
\qquad
Y(a,0)=a.
}
\tag{1.9}
$$

Because:

$$
\nabla\cdot V=0,
$$

$$
\boxed{
\nabla\cdot W
=
3\gamma.
}
\tag{1.10}
$$

Hence the similarity flow satisfies the exact Jacobian law:

$$
\boxed{
\det
\nabla_aY(a,s)
=
e^{3\gamma s}.
}
\tag{1.11}
$$

The third and central result is the DSS Kelvin law.

Let:

$$
C_0
$$

be a smooth closed loop and:

$$
C_s
=
Y(C_0,s)
$$

its similarity-material image.

Define:

$$
\boxed{
\Gamma_{ss}(s;C_0)
=
\oint_{C_s}
V(y,s)\cdot dy.
}
\tag{1.12}
$$

The ordinary physical Euler Kelvin theorem transforms exactly into:

$$
\boxed{
e^{(1-2\gamma)s}
\Gamma_{ss}(s;C_0)
=
\Gamma_{ss}(0;C_0).
}
\tag{1.13}
$$

Therefore over one DSS period:

$$
\boxed{
\Gamma_{ss}
(
S_0;C_0
)
=
\rho_\Gamma
\Gamma_{ss}
(
0;C_0
),
}
\tag{1.14}
$$

where:

$$
\boxed{
\rho_\Gamma
=
e^{-(1-2\gamma)S_0}.
}
\tag{1.15}
$$

In the strict Type-II window:

$$
\gamma<1/2,
$$

so:

$$
\boxed{
0<\rho_\Gamma<1.
}
\tag{1.16}
$$

Equivalently, if the DSS spatial scaling factor is:

$$
\Lambda>1,
$$

with:

$$
S_0
=
(\alpha+1)\log\Lambda,
$$

then:

$$
\boxed{
\rho_\Gamma
=
\Lambda^{-(\alpha-1)}.
}
\tag{1.17}
$$

Thus **similarity-material circulation strictly contracts every DSS period**.

This is a normalized return-depletion law which is not a kinetic-energy budget.

Now use profile periodicity.

Since:

$$
V(y,S_0)=V(y,0),
$$

the circulation after one period is the circulation of the same phase field:

$$
V(\cdot,0)
$$

on the new geometric loop:

$$
\Phi(C_0),
$$

where:

$$
\Phi
=
Y(\cdot,S_0)
$$

is the similarity Poincare map.

Hence:

$$
\boxed{
\oint_{
\Phi(C_0)
}
V(y,0)\cdot dy
=
\rho_\Gamma
\oint_{C_0}
V(y,0)\cdot dy.
}
\tag{1.18}
$$

This gives an exact **material circulation holonomy law**.

If:

$$
C_0
$$

is a recurrent material loop in the similarity chart, in the sense that for some sequence:

$$
m_j\to\infty,
$$

$$
\boxed{
\Phi^{m_j}(C_0)
\to
C_0
}
\tag{1.19}
$$

in a topology in which circulation is continuous, then periodicity gives:

$$
\oint_{
\Phi^{m_j}(C_0)
}
V\cdot dy
\to
\oint_{C_0}
V\cdot dy.
$$

But the Kelvin holonomy law gives:

$$
\boxed{
\oint_{
\Phi^{m_j}(C_0)
}
V\cdot dy
=
\rho_\Gamma^{m_j}
\oint_{C_0}
V\cdot dy
\to0.
}
\tag{1.20}
$$

Therefore:

$$
\boxed{
\oint_{C_0}
V\cdot dy
=
0.
}
\tag{1.21}
$$

Thus:

$$
\boxed{
\textbf{
strict DSS recurrent material loop}
\Longrightarrow
\textbf{
zero circulation}.
}
}
\tag{1.22}
$$

This is stronger than an energy summation statement.

It is a direct incompatibility between:

- DSS state recurrence;
- material recurrence;
- Kelvin circulation;
-:

  $$
  \gamma<1/2.
  $$

The fourth result converts this into profile rigidity.

Suppose every sufficiently small material loop in the active core is recurrent with zero material-holonomy defect.

Then every such loop has zero circulation.

By Stokes:

$$
\boxed{
\nabla\times V
=
0
}
\tag{1.23}
$$

in the active core.

If zero material holonomy holds through an exhaustion of the connected strong profile, then:

$$
\boxed{
\nabla\times V=0
}
\tag{1.24}
$$

globally.

Since:

$$
\nabla\cdot V=0,
$$

every component of:

$$
V
$$

is harmonic.

Now impose the DCRP critical-tail growth:

$$
\boxed{
\int_0^{S_0}
\int_{B_R}
|V|^2
dyds
\le
CR^\kappa,
\qquad
0<\kappa<1.
}
\tag{1.25}
$$

For a harmonic component:

$$
V_j(\cdot,s),
$$

the mean-value inequality yields, for fixed:

$$
x,
$$

$$
|V_j(x,s)|^2
\le
CR^{-3}
\int_{B_R(x)}
|V_j(y,s)|^2dy.
$$

Integrating in:

$$
s
$$

and using:

$$
B_R(x)
\subset
B_{R+|x|}(0),
$$

one obtains:

$$
\boxed{
\int_0^{S_0}
|V_j(x,s)|^2ds
\le
C_x
R^{\kappa-3}.
}
\tag{1.26}
$$

Let:

$$
R\to\infty.
$$

Because:

$$
\kappa<3,
$$

$$
V_j(x,s)=0
$$

for almost every:

$$
s.
$$

Smoothness gives:

$$
\boxed{
V\equiv0.
}
\tag{1.27}
$$

Therefore:

$$
\boxed{
\textbf{
nonzero strict DSS strong profile}
\Longrightarrow
\textbf{
nontrivial material circulation holonomy / turnover}.
}
}
\tag{1.28}
$$

This provides a second strict return witness besides PFET.

The fifth result is a volume-expansion calibration.

The Poincare map:

$$
\Phi
$$

satisfies:

$$
\boxed{
\det
D\Phi
=
e^{3\gamma S_0}
>
1.
}
\tag{1.29}
$$

Hence for every measurable:

$$
A
$$

with finite positive volume:

$$
\boxed{
|\Phi(A)|
=
e^{3\gamma S_0}
|A|.
}
\tag{1.30}
$$

Therefore:

$$
\boxed{
\Phi(A)=A
}
\tag{1.31}
$$

is impossible for:

$$
0<|A|<\infty.
$$

A state can be DSS-periodic while its material labels are not.

This confirms geometrically that the strict Type-II recurrent core must be **materially replenished/turned over**.

The volume expansion itself is partly generated by the canonical similarity dilation and is therefore **not** declared a tax by fiat.

Its correct role is to show that exact state recurrence cannot be identified with exact material-particle recurrence.

The circulation holonomy law supplies the gauge-invariant dynamical content.

The sixth result is a compact-class finite witness.

Let:

$$
\mathscr C_{\rm DSS}^{mat}
$$

be a sequentially compact class of nonzero strict DSS profiles satisfying:

-:

  $$
  \gamma
  \in
  [2/5+\delta,1/2-\delta];
  $$

- fixed translation/rotation/pressure gauges;
- the critical tail envelope;
- a fixed nontriviality condition;
- strong local:

  $$
  C^1
  $$

  compactness.

If the material circulation-holonomy observable vanished on **all** loops in every profile, the previous theorem would force every profile to be zero.

By compactness, there is therefore a finite family of loop templates / local loop charts and:

$$
\boxed{
c_{\rm hol}>0
}
\tag{1.32}
$$

such that every profile has at least one declared loop with:

$$
\boxed{
\left|
\oint_{
\Phi(C)
}
V\cdot dy
-
\oint_C
V\cdot dy
\right|
\ge
c_{\rm hol}.
}
\tag{1.33}
$$

The exact Kelvin law gives the equivalent form:

$$
\boxed{
(1-\rho_\Gamma)
\left|
\oint_C
V\cdot dy
\right|
\ge
c_{\rm hol}.
}
\tag{1.34}
$$

Thus the infinite material-loop family can be compressed to a finite recurrence witness on a compact normalized class.

This may be included as a native transition/holonomy residual:

$$
\boxed{
\mathsf R_{\rm hol}.
}
\tag{1.35}
$$

The strongest strict compact Type-II zero-cost branch then satisfies:

$$
\boxed{
\mathsf O_{\rm PFET}>0
\quad\text{and}\quad
\mathsf R_{\rm hol}>0.
}
\tag{1.36}
$$

It cannot belong to an exact MORP kernel in which both PFET and native transition residuals vanish.

The final limitation of this round is important.

The Kelvin contraction does **not** imply that the **state** circulation amplitude globally decreases from DSS period to DSS period.

The profile is periodic.

Instead:

- circulation on each **same material loop** contracts in similarity coordinates;
- the periodic state can replenish nonzero circulation only by bringing in different material loops / labels.

Thus:

$$
\boxed{
\textbf{
Kelvin depletion}
\Longrightarrow
\textbf{
material replenishment requirement},
}
\tag{1.37}
$$

not immediate triviality of the state.

This produces a non-energy replenishment problem analogous to the earlier supplier problem, but now with an exact Euler invariant.

The new exact frontier is:

$$
\boxed{
\textbf{
Material-Circulation Replenishment /
Same-Parent Holonomy Taxation Lemma}.
}
\tag{1.38}
$$

The target is to prove that the continual replacement of circulation-bearing material loops required by a strict DSS state necessarily produces one of:

1. nonzero material pressure/PFET work already detected by DCRP-29/31;
2. a scale/spatial transition carrier;
3. a finite positive material holonomy return tax compatible with MORP minimality;
4. a contradiction with same-parent Navier--Stokes viscous ancestry.

This route avoids the energy-telescoping obstruction rather than trying to sum through it.

---

# 2. Critical Telescoping No-Go

Assume exact geometric raw-energy scaling:

$$
\boxed{
\beta_n
=
\beta_0q^n,
\qquad
0<q<1.
}
\tag{2.1}
$$

Suppose a raw payment is proportional to the energy lost between adjacent returns:

$$
\boxed{
\mathcal P_n
=
\beta_n-\beta_{n+1}.
}
\tag{2.2}
$$

Then:

$$
\boxed{
\mathcal P_n
=
(1-q)\beta_n.
}
\tag{2.3}
$$

Therefore:

$$
\boxed{
\sum_{n=0}^{N}
\mathcal P_n
=
\beta_0-\beta_{N+1}.
}
\tag{2.4}
$$

Let:

$$
N\to\infty.
$$

Since:

$$
\beta_n\to0,
$$

$$
\boxed{
\sum_{n=0}^{\infty}
\mathcal P_n
=
\beta_0.
}
\tag{2.5}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

This is the exact critical telescoping model.

---

# 3. Homogeneous energy-channel version

Let:

$$
\mathcal Q
$$

be any return observable whose raw physical dimension is identical to kinetic energy.

Suppose exact DSS gives:

$$
\boxed{
\mathcal Q_{n+1}
=
q
\mathcal Q_n.
}
\tag{3.1}
$$

Then:

$$
\boxed{
\sum_n
\mathcal Q_n
<
\infty.
}
\tag{3.2}
$$

Thus every degree-one energy-like return budget is vulnerable to the same geometric summability.

This includes the naive raw version of the DCRP-31 matching-layer PFET.

A different invariant or a strict return-level monotonicity theorem is required.

---

# 4. DSS similarity variables

Let the backward Euler similarity exponent be:

$$
\gamma
=
\frac1{\alpha+1}.
$$

Write:

$$
\boxed{
u(x,t)
=
(-t)^{-(1-\gamma)}
V(y,s),
}
\tag{4.1}
$$

with:

$$
\boxed{
y
=
(-t)^{-\gamma}x,
}
\tag{4.2}
$$

and:

$$
\boxed{
s
=
-\log(-t).
}
\tag{4.3}
$$

A DSS solution has:

$$
\boxed{
V(y,s+S_0)
=
V(y,s).
}
\tag{4.4}
$$

The physical particle path:

$$
X(t)
$$

becomes the similarity trajectory:

$$
\boxed{
Y(s)
=
(-t)^{-\gamma}
X(t).
}
\tag{4.5}
$$

Differentiate:

$$
\boxed{
\partial_sY
=
\gamma Y
+
V(Y,s).
}
\tag{4.6}
$$

---

# 5. Similarity flow Jacobian

Let:

$$
W(y,s)
=
\gamma y
+
V(y,s).
$$

Because:

$$
\nabla\cdot V=0,
$$

$$
\boxed{
\nabla\cdot W
=
3\gamma.
}
\tag{5.1}
$$

Let:

$$
Y(a,s)
$$

be the flow map.

Liouville's formula gives:

$$
\boxed{
\partial_s
\det
\nabla_aY
=
3\gamma
\det
\nabla_aY.
}
\tag{5.2}
$$

Since:

$$
Y(a,0)=a,
$$

$$
\boxed{
\det
\nabla_aY(a,s)
=
e^{3\gamma s}.
}
\tag{5.3}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

This agrees with the self-similar Lagrangian formula in Constantin--Ignatova--Vicol.

---

# 6. Physical Kelvin theorem in similarity variables

Let:

$$
C(t)
$$

be a physical material loop.

Euler Kelvin gives:

$$
\boxed{
\Gamma_{\rm phys}(t)
=
\oint_{C(t)}
u(x,t)\cdot dx
=
\mathrm{constant}.
}
\tag{6.1}
$$

Since:

$$
x
=
(-t)^\gamma y,
$$

$$
dx
=
(-t)^\gamma dy,
$$

and:

$$
u
=
(-t)^{-(1-\gamma)}
V,
$$

one obtains:

$$
\boxed{
\Gamma_{\rm phys}(t)
=
(-t)^{2\gamma-1}
\Gamma_{ss}(s),
}
\tag{6.2}
$$

where:

$$
\boxed{
\Gamma_{ss}(s)
=
\oint_{C_s}
V(y,s)\cdot dy.
}
\tag{6.3}
$$

Because:

$$
-t=e^{-s},
$$

$$
(-t)^{2\gamma-1}
=
e^{(1-2\gamma)s}.
$$

Therefore:

$$
\boxed{
e^{(1-2\gamma)s}
\Gamma_{ss}(s)
=
\Gamma_{ss}(0).
}
\tag{6.4}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

This is the time-periodic DSS version of the self-similar Kelvin theorem.

---

# 7. One-period circulation contraction

Set:

$$
s=S_0.
$$

Then:

$$
\boxed{
\Gamma_{ss}(S_0)
=
e^{-(1-2\gamma)S_0}
\Gamma_{ss}(0).
}
\tag{7.1}
$$

For:

$$
\gamma<1/2,
$$

define:

$$
\boxed{
\rho_\Gamma
=
e^{-(1-2\gamma)S_0}
\in(0,1).
}
\tag{7.2}
$$

Thus:

$$
\boxed{
|\Gamma_{ss}(mS_0)|
=
\rho_\Gamma^m
|\Gamma_{ss}(0)|.
}
\tag{7.3}
$$

Every fixed material loop loses similarity-coordinate circulation exponentially under repeated DSS periods.

---

# 8. Poincare-map holonomy

Let:

$$
\Phi
=
Y(\cdot,S_0).
$$

Because:

$$
V(\cdot,S_0)=V(\cdot,0),
$$

$$
\Gamma_{ss}(S_0;C_0)
=
\oint_{\Phi(C_0)}
V(y,0)\cdot dy.
$$

Therefore:

$$
\boxed{
\oint_{\Phi(C)}
V\cdot dy
=
\rho_\Gamma
\oint_C
V\cdot dy.
}
\tag{8.1}
$$

Define the circulation holonomy residual:

$$
\boxed{
\mathcal H_\Gamma(C)
=
\left|
\oint_{\Phi(C)}
V\cdot dy
-
\oint_C
V\cdot dy
\right|.
}
\tag{8.2}
$$

Then exactly:

$$
\boxed{
\mathcal H_\Gamma(C)
=
(1-\rho_\Gamma)
\left|
\oint_C
V\cdot dy
\right|.
}
\tag{8.3}
$$

Thus nonzero loop circulation automatically creates a nonzero material-return residual.

---

# 9. Recurrent-loop rigidity

Suppose:

$$
\Phi^{m_j}(C)
\to
C
$$

in:

$$
C^1
$$

or another topology in which:

$$
C\mapsto
\oint_C
V\cdot dy
$$

is continuous.

Then periodicity gives:

$$
\oint_{\Phi^{m_j}(C)}
V\cdot dy
\to
\oint_C
V\cdot dy.
$$

But:

$$
\oint_{\Phi^{m_j}(C)}
V\cdot dy
=
\rho_\Gamma^{m_j}
\oint_C
V\cdot dy
\to0.
$$

Hence:

$$
\boxed{
\oint_C
V\cdot dy
=
0.
}
\tag{9.1}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 10. Small-loop circulation and vorticity

If:

$$
\Omega
=
\nabla\times V
$$

is nonzero at:

$$
y_0,
$$

choose a sufficiently small oriented disk:

$$
D_\varepsilon
$$

through:

$$
y_0
$$

with normal approximately parallel to:

$$
\Omega(y_0).
$$

By Stokes:

$$
\boxed{
\oint_{
\partial D_\varepsilon
}
V\cdot dy
=
\int_{
D_\varepsilon
}
\Omega\cdot n
dS.
}
\tag{10.1}
$$

For sufficiently small:

$$
\varepsilon,
$$

the right side is nonzero.

Therefore every vortical point produces a local loop with nonzero material holonomy.

---

# 11. Zero circulation on all loops implies irrotationality

On a simply connected region:

$$
G,
$$

if:

$$
\boxed{
\oint_C
V\cdot dy
=
0
}
\tag{11.1}
$$

for every smooth closed loop:

$$
C\subset G,
$$

then:

$$
\boxed{
\nabla\times V=0
}
\tag{11.2}
$$

in:

$$
G.
$$

This is the usual circulation characterization of a gradient field.

Combined with:

$$
\nabla\cdot V=0,
$$

one obtains:

$$
\boxed{
\Delta V=0.
}
\tag{11.3}
$$

---

# 12. Harmonic critical-tail Liouville lemma

## Lemma 12.1

Let:

$$
V:
\mathbb R^3\times[0,S_0]
\to
\mathbb R^3
$$

be smooth, periodic in:

$$
s,
$$

and assume:

$$
\boxed{
\nabla\cdot V
=
0,
\qquad
\nabla\times V
=
0.
}
\tag{12.1}
$$

Assume:

$$
\boxed{
\int_0^{S_0}
\int_{B_R}
|V|^2
dyds
\le
CR^\kappa
}
\tag{12.2}
$$

for some:

$$
\kappa<3.
$$

Then:

$$
\boxed{
V\equiv0.
}
\tag{12.3}
$$

### Proof

Each component:

$$
V_j(\cdot,s)
$$

is harmonic.

For fixed:

$$
x,
$$

the harmonic mean-value estimate gives:

$$
|V_j(x,s)|^2
\le
CR^{-3}
\int_{
B_R(x)
}
|V_j(y,s)|^2dy.
$$

Integrate over:

$$
s.
$$

For:

$$
R>|x|+1,
$$

$$
B_R(x)
\subset
B_{2R}(0).
$$

Therefore:

$$
\int_0^{S_0}
|V_j(x,s)|^2ds
\le
CR^{-3}
(2R)^\kappa.
$$

Let:

$$
R\to\infty.
$$

Since:

$$
\kappa<3,
$$

the right side tends to zero.

Thus:

$$
V_j(x,s)=0
$$

for almost every:

$$
s.
$$

Smoothness gives:

$$
V_j=0.
$$

$$
\square
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 13. NEW THEOREM — Strict DSS Material-Holonomy Rigidity

## Theorem 13.1

Let:

$$
V
$$

be a smooth nonzero DSS Euler profile with:

$$
\boxed{
\gamma<1/2
}
\tag{13.1}
$$

and the critical/sub-volume energy growth:

$$
\boxed{
\int_0^{S_0}
\int_{B_R}
|V|^2
\le
CR^\kappa,
\qquad
\kappa<3.
}
\tag{13.2}
$$

Then:

$$
\boxed{
\exists
C:
\mathcal H_\Gamma(C)>0.
}
\tag{13.3}
$$

Equivalently:

$$
\boxed{
\textbf{
nonzero strict DSS profile}
\Longrightarrow
\textbf{
nonzero material circulation holonomy}.
}
\tag{13.4}
$$

### Proof

Assume:

$$
\mathcal H_\Gamma(C)=0
$$

for every smooth loop.

Since:

$$
1-\rho_\Gamma>0,
$$

equation (8.3) implies:

$$
\oint_CV\cdot dy=0
$$

for every loop.

Hence:

$$
\nabla\times V=0.
$$

Use Lemma 12.1.

Then:

$$
V=0,
$$

contradiction.

$$
\square
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 14. Material volume expansion

The one-period Poincare map has:

$$
\boxed{
\det D\Phi
=
e^{3\gamma S_0}.
}
\tag{14.1}
$$

Therefore:

$$
\boxed{
|\Phi(A)|
=
e^{3\gamma S_0}
|A|
}
\tag{14.2}
$$

for measurable:

$$
A.
$$

If:

$$
0<|A|<\infty,
$$

then:

$$
\boxed{
\Phi(A)\neq A.
}
\tag{14.3}
$$

This proves:

$$
\boxed{
\textbf{
DSS state periodicity}
\neq
\textbf{
material-label periodicity}.
}
\tag{14.4}
$$

The similarity coordinates continually relabel/turn over material.

The canonical volume factor comes from the similarity dilation and is not itself declared an obstruction cost.

---

# 15. Kelvin versus state recurrence

The DSS state is periodic:

$$
V(s+S_0)=V(s).
$$

But a same material loop obeys:

$$
\Gamma_{ss}(s+S_0)
=
\rho_\Gamma\Gamma_{ss}(s).
$$

Thus a periodic state with nonzero vorticity must continually present **new circulation-bearing material geometry** to the same Eulerian chart.

This is the precise replenishment principle:

$$
\boxed{
\textbf{
state recurrence}
+
\textbf{
Kelvin depletion on each material loop}
\Longrightarrow
\textbf{
material turnover / holonomy}.
}
\tag{15.1}
$$

---

# 16. Why Kelvin avoids energy telescoping

The raw energy carrier has:

$$
\beta_{n+1}=q\beta_n,
$$

so energy-like payments geometrically sum.

Kelvin circulation instead obeys exact conservation in physical material coordinates.

The strict similarity contraction occurs only after changing to the rescaled chart.

Therefore the contradiction mechanism is not:

$$
\sum_n
\text{payment}_n
=
\infty.
$$

It is:

$$
\boxed{
\textbf{
the same material object cannot both obey Kelvin and return unchanged in a }\gamma<1/2\textbf{ DSS chart}.
}
}
\tag{16.1}
$$

This is a return-compatibility rigidity rather than a budget contradiction.

---

# 17. Compact-class finite holonomy witness

Let:

$$
\mathscr C
$$

be a compact class of smooth strict DSS profiles satisfying:

$$
\boxed{
\gamma
\le
1/2-\delta
}
\tag{17.1}
$$

for:

$$
\delta>0,
$$

the critical tail envelope, fixed gauges, and a fixed nontriviality normalization.

For each:

$$
V\in\mathscr C,
$$

Theorem 13.1 gives at least one loop:

$$
C_V
$$

with:

$$
\mathcal H_\Gamma^V(C_V)>0.
$$

Continuity in the:

$$
C^1
$$

profile/loop topology gives an open neighborhood of:

$$
V
$$

on which a nearby loop template retains a positive holonomy.

Compactness gives a finite subcover.

Hence there are finitely many loop charts/templates and:

$$
\boxed{
c_{\rm hol}>0
}
\tag{17.2}
$$

such that every:

$$
V\in\mathscr C
$$

has one declared loop satisfying:

$$
\boxed{
\mathcal H_\Gamma(C)
\ge
c_{\rm hol}.
}
\tag{17.3}
$$

Status:

$$
\boxed{
\textbf{PROVED conditional on the compact }C^1\textbf{ profile class}.
}
$$

---

# 18. Native status of the holonomy observable

The holonomy is generated entirely from:

- the Euler/vanishing-viscosity profile;
- its material flow map;
- circulation of the velocity one-form.

No singularity certificate is copied into the detector.

Thus it is a legitimate candidate native transition coordinate:

$$
\boxed{
\mathsf R_{\rm hol}.
}
\tag{18.1}
$$

It should live with:

- moving-center residual;
- material-window deformation;
- return-map residual;

inside:

$$
\mathsf R_{\rm nat}.
$$

It is not a positivity tax declared from compactification alone.

---

# 19. Exact strict zero-transition branch excluded

Suppose a strict compact DSS profile satisfies:

$$
\boxed{
\mathsf R_{\rm hol}=0.
}
\tag{19.1}
$$

Then all declared circulation holonomy vanishes.

After finite-compiler completion / compactness, Theorem 13.1 forces:

$$
V=0.
$$

Therefore:

$$
\boxed{
\textbf{
nonzero strict compact DSS}
\cap
\ker
\mathsf R_{\rm hol}
=
\varnothing.
}
\tag{19.2}
$$

Combined with DCRP-31:

$$
\boxed{
\textbf{
strict compact DSS}
\Longrightarrow
\mathsf O_{\rm PFET}>0
\quad\text{and}\quad
\mathsf R_{\rm hol}>0.
}
\tag{19.3}
$$

This is a stronger equality-manifold exclusion than PFET alone.

---

# 20. What is not proved

DCRP-32 does **not** prove that:

$$
\mathsf R_{\rm hol}
$$

is monotone along arbitrary Navier--Stokes transitions.

It does not prove:

$$
\boxed{
\mathfrak J(TD)
+
\mathsf R_{\rm hol}(D)
\le
\mathfrak J(D).
}
\tag{20.1}
$$

It also does not prove that a new circulation-bearing material loop cannot enter from the DSS tail each period.

Indeed such replenishment is exactly how a periodic Eulerian state can coexist with Kelvin contraction on each fixed material loop.

Thus the remaining issue is material replenishment.

---

# 21. Relationship to the outgoing property

Constantin--Ignatova--Vicol identify:

$$
\gamma y+U(y)
$$

as the self-similar Lagrangian velocity and show that a local outgoing property forces:

$$
\gamma\ge1/2
$$

for nontrivial smooth self-similar Euler profiles.

The DCRP strict branch has:

$$
\gamma<1/2.
$$

Thus it must possess a non-outgoing/trapped Lagrangian mechanism.

DCRP-32 sharpens this:

a trapped/recurrent material loop with nonzero circulation is impossible.

Hence the non-outgoing mechanism must involve:

- zero-circulation recurrent geometry;
- material turnover;
- separatrix/stagnation structure;
- or circulation-bearing labels continually entering/leaving the recurrent chart.

This further narrows the Lagrangian normal form.

---

# 22. Weber formula calibration

The self-similar Weber formula provides the differential-form origin of the Kelvin contraction.

For the steady self-similar normalization in the external source, the pulled-back velocity one-form acquires the factor:

$$
e^{(1-2\gamma)s}.
$$

Exact terms do not affect closed-loop circulation.

This is why:

$$
\gamma=1/2
$$

is the distinguished circulation-neutral similarity exponent.

The DCRP strict branch lies strictly on the circulation-contracting side.

---

# 23. A new equality-manifold interpretation

The DCRP strict DSS equality branch can now be described as follows.

If the state profile returns exactly but:

$$
\gamma<1/2,
$$

then:

### state sector

$$
V(s+S_0)=V(s);
$$

### material sector

every same material loop has:

$$
\Gamma_{ss}(s+S_0)
=
\rho_\Gamma\Gamma_{ss}(s),
\qquad
\rho_\Gamma<1.
$$

Therefore exact recurrence requires continuous **state/material label replacement**.

The equality object is not a fixed material coherent structure.

It is a stationary/periodic Eulerian pattern sustained by material turnover.

This is the correct strong Type-II normal form.

---

# 24. Candidate replenishment ledger

Let:

$$
K
$$

be a fixed normalized core.

Let:

$$
\mathcal L_K(s)
$$

be an admissible family of material loops intersecting the core.

Define a circulation capacity:

$$
\boxed{
\mathcal C_K(s)
=
\sup_{
C\in\mathcal L_K(s)
}
\left|
\oint_C
V(y,s)\cdot dy
\right|.
}
\tag{24.1}
$$

State periodicity suggests:

$$
\mathcal C_K(s+S_0)
=
\mathcal C_K(s)
$$

after the same core gauge.

Kelvin contraction gives:

$$
\rho_\Gamma
\mathcal C_K(s)
$$

as the maximum contribution coming from **the same material loops** after one period, modulo loop escape.

Thus the missing amount:

$$
\boxed{
(1-\rho_\Gamma)
\mathcal C_K
}
\tag{24.2}
$$

must be replenished by:

- new material loops entering:

  $$
  K;
  $$

- deformation/escape of the old loops;
- pressure/SGS/material transfer across the recurrent core boundary.

This suggests a genuine circulation-replenishment ledger.

A fully rigorous compact formulation is the next task.

---

# 25. Why circulation capacity is promising

Unlike raw energy:

$$
\beta_n,
$$

the physical circulation of a fixed material loop is not geometrically depleted by viscosity-free Euler dynamics.

The contraction factor:

$$
\rho_\Gamma
$$

is entirely a consequence of representing that conserved physical circulation in the shrinking DSS chart.

Therefore a stationary normalized circulation capacity cannot be maintained by telescoping a finite initial circulation of the same labels.

It requires continual material replacement.

This is structurally different from energy refill.

---

# 26. Navier--Stokes ancestry issue

The actual prelimit parent is Navier--Stokes, not Euler.

For a physical material loop:

$$
C_t,
$$

smooth Navier--Stokes circulation obeys a viscous correction involving:

$$
\nu\Delta u.
$$

DCRP-28 showed that the Type-II **energy-level** viscous residue may vanish.

That does not automatically control the circulation correction, which is one derivative higher.

Therefore one must not simply claim:

$$
\text{Type-II inviscid energy limit}
\Longrightarrow
\text{prelimit Kelvin circulation exact}.
$$

The Euler Kelvin law is exact only at the strong inviscid profile level.

Bridging it back to the same physical Navier--Stokes loops requires an additional circulation/second-derivative compactness theorem.

This is a major safety condition.

---

# 27. Two routes for the next round

There are now two precise routes.

## Route A — profile-level material replenishment

Stay in the exact Euler DSS limit and prove:

$$
\boxed{
\text{nonzero periodic circulation capacity}
\Longrightarrow
\text{positive material boundary turnover / PFET}.
}
\tag{27.1}
$$

This would close the strong profile equality manifold.

## Route B — same-parent Navier--Stokes circulation shadowing

Prove that vanishing-viscosity Type-II extraction preserves enough loop circulation to transfer the Euler holonomy gap back to actual preterminal Navier--Stokes material loops.

Then the holonomy becomes a true same-parent native return tax.

Route B is stronger but technically requires higher-order control.

---

# 28. Updated strict Type-II branch tree

The strict compact same-parent Type-II state now satisfies:

$$
\boxed{
\text{DSS}
+
\gamma\in(2/5,1/2).
}
$$

DCRP-31 gives:

$$
\boxed{
\mathsf O_{\rm PFET}>0.
}
$$

DCRP-32 gives:

$$
\boxed{
\mathsf R_{\rm hol}>0.
}
$$

Thus the state is simultaneously:

- pressure--kinetic flux active;
- materially non-recurrent at the circulation level.

If either coordinate vanishes, the strict strong profile is excluded.

The only surviving exact strong state is a **materially replenished DSS pattern**.

---

# 29. Correct next frontier

The next target is:

$$
\boxed{
\textbf{
Material-Circulation Replenishment /
Same-Parent Holonomy Taxation Lemma}.
}
$$

A useful theorem would show:

> Let:
>
> $$
> V
> $$
>
> be a nonzero strict DSS Euler profile in:
>
> $$
> 2/5<\gamma<1/2.
> $$
>
> Assume the normalized state returns to the same core every period.
>
> Then the circulation capacity lost from the previous generation of material loops:
>
> $$
> (1-\rho_\Gamma)\mathcal C_K
> $$
>
> must be supplied by a quantitatively nonzero:
>
> $$
> \text{material boundary turnover}
> \ \vee\
> \text{pressure/PFET work}
> \ \vee\
> \text{scale/spatial transition}.
> $$
>
> If all three vanish, the state circulation capacity decays geometrically, contradicting DSS periodicity unless:
>
> $$
> V=0.
> $$

A second theorem should then shadow this profile-level replenishment back to the actual Navier--Stokes parent.

---

# 30. Source-status audit

## Constantin--Ignatova--Vicol 2026

The primary source explicitly defines the self-similar Lagrangian transport velocity:

$$
\gamma y+U(y),
$$

derives:

$$
\det\nabla_aY=e^{3\gamma s},
$$

derives the self-similar Weber formula, and obtains the self-similar Kelvin circulation relation:

$$
e^{(1-2\gamma)s}
\Gamma_{ss}(s)
=
\Gamma_{ss}(0).
$$

The source highlights:

$$
\gamma=1/2
$$

as the distinguished circulation-neutral exponent.

It also proves that the local outgoing property forces:

$$
\gamma\ge1/2.
$$

## Chae--Tsai

Euler DSS is equivalent to a time-periodic similarity profile with period:

$$
S_0.
$$

This supplies the periodic state side of the Kelvin-holonomy contradiction.

## Xue

The critical DSS tail growth:

$$
R^{3-2\alpha}
$$

in admissible nontrivial classes provides the sub-volume growth used to eliminate globally irrotational strong profiles.

---

# 31. End state

The energy-summation route has an exact structural NO-GO:

$$
\boxed{
\sum_n
(1-q)\beta_n
=
\beta_0.
}
$$

Therefore DCRP-31 PFET visibility alone cannot yield a global kinetic-energy contradiction.

The non-energy replacement is DSS Kelvin holonomy:

$$
\boxed{
\Gamma_{ss}(s+S_0)
=
e^{-(1-2\gamma)S_0}
\Gamma_{ss}(s).
}
$$

For:

$$
\gamma<1/2,
$$

the factor is strictly less than one.

Thus:

$$
\boxed{
\textbf{
same material loop}
+
\textbf{
DSS geometric recurrence}
+
\textbf{
nonzero circulation}
}
$$

are incompatible.

If every loop has zero holonomy, the profile is globally irrotational.

Together with divergence-free and the critical sub-volume energy growth, this forces:

$$
\boxed{
V=0.
}
$$

Therefore every nonzero strict DSS strong profile necessarily has:

$$
\boxed{
\textbf{
material circulation holonomy / turnover}.
}
$$

Combined with DCRP-31:

$$
\boxed{
\textbf{
strict compact DSS}
\Longrightarrow
\textbf{
inward PFET}
+
\textbf{
material holonomy}.
}
$$

The next single frontier is:

$$
\boxed{
\textbf{
Material-Circulation Replenishment /
Same-Parent Holonomy Taxation.
}
}
$$