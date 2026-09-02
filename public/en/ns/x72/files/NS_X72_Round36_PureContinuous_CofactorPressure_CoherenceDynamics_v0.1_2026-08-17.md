# NS × X Integral × 24/72 Paradigm Practice
## Round 36 — Pure Continuous Cofactor–Pressure Coherence Dynamics / Moving-Sign-Domain Route

- Date: 2026-08-17
- Version: v0.1
- Status: Proof-Route Experiment / Continuous-Only Pressure-Coherence-Dynamics Branch
- canonical source: UTF-8 Markdown
- canonical math delimiters: inline `$...$`; display `$$...$$`
- Previous round: `NS_X72_Round35_PureContinuous_CancellationReplenishment_Closure_v0.1_2026-08-17.md`
- Objective of this round: Round 35 has compressed the anisotropic pressure replenishment into the cofactor–pressure coherence
  $$
  \rho_p^-.
  $$
  This round establishes its moving-sign-domain exact dynamics: deriving the material equation of the trace-free cofactor tensor, the Riesz/transport-commutator equation of the anisotropic pressure Hessian, the negative-determinant domain boundary velocity, and the normalized Hilbert-coherence evolution. We examine whether the replenishing coherence automatically dephases, or if it can form exact/near phase locking.
- Non-claims: This document does not prove the existence of a persistent perfect replenishing lock in finite-energy Navier–Stokes flows, nor does it prove that the coherence must rotate rapidly. Instead, this document constructs a stationary affine structural witness to rule out universal dephasing; the true obstruction lies in the spacetime control of the pressure-response commutator, the moving sign boundary, and the relative angular forcing.

---

# 0. Round 35 handoff

Let:

$$
d=-\det S.
$$

negative determinant reserve region:

$$
\boxed{
A_-(t)
=
\{x:d(x,t)<0\}.
}
\tag{0.1}
$$

trace-free cofactor:

$$
\boxed{
C
=
C_S^0
=
S^2-\frac13|S|^2I.
}
\tag{0.2}
$$

anisotropic pressure Hessian:

$$
\boxed{
H
=
H_p^0
=
H_p-\frac{\Delta p}{3}I.
}
\tag{0.3}
$$

Round 35 replenishing coherence:

$$
\boxed{
\rho_p^-
=
-
\frac{
\int_{A_-}
C:H\,dx
}{
\|C\|_{2,A_-}
\|H\|_{2,A_-}
}.
}
\tag{0.4}
$$

anisotropic pressure replenishment:

$$
\boxed{
\mathcal P_{\rm aniso}
=
2
\rho_p^-
\|C\|_{2,A_-}
\|H\|_{2,A_-}.
}
\tag{0.5}
$$

Round 35 STOP:

$$
\boxed{
\text{STOP-C39}
=
\text{Replenishment-Closure / Cofactor–Pressure Coherence Gap}.
}
$$

---

# 1. Cofactor tensor as a polynomial of strain

For the trace-free symmetric:

$$
S,
$$

define:

$$
C
=
S^2-\frac13|S|^2I.
$$

Round 35 has proved:

$$
\boxed{
|C|
=
\frac{|S|^2}{\sqrt6}.
}
\tag{1.1}
$$

Therefore:

$$
C
$$

is a normalized quadratic carrier of the strain spectral shape.

---

# 2. Exact material dynamics of the trace-free cofactor

Let:

$$
G
=
D_tS.
$$

By direct differentiation:

$$
\boxed{
D_tC
=
GS+SG
-
\frac23
(S:G)I.
}
\tag{2.1}
$$

Navier–Stokes strain equation:

$$
\boxed{
G
=
\nu\Delta S
-
S^2
-
\frac14\omega\otimes\omega
+
\frac14|\omega|^2I
-
H_p.
}
\tag{2.2}
$$

Thus:

$$
D_tC
=
\mathcal A_\nu
+
\mathcal A_{\rm self}
+
\mathcal A_\omega
+
\mathcal A_p.
$$

---

# 3. Viscous cofactor forcing

$$
\boxed{
\mathcal A_\nu
=
\nu
\left[
(\Delta S)S
+
S(\Delta S)
-
\frac23
(S:\Delta S)I
\right].
}
\tag{3.1}
$$

This is a higher-derivative angular/amplitude forcing.

---

# 4. Self-amplification cofactor dynamics

For:

$$
G_{\rm self}
=
-S^2,
$$

by the Cayley–Hamilton theorem:

$$
S^3
=
\frac12|S|^2S
+
(\det S)I,
$$

and:

$$
\operatorname{tr}(S^3)=3\det S,
$$

we obtain:

$$
\boxed{
\mathcal A_{\rm self}
=
-|S|^2S.
}
\tag{4.1}
$$

This is the first important difference:

$$
\boxed{
-S^2
}
$$

does not directly rotate the strain eigenframe,

but generally changes the direction of the trace-free cofactor in the five-dimensional tensor space.

---

# 5. Vorticity contribution to cofactor dynamics

For:

$$
G_\omega
=
-\frac14\omega\otimes\omega
+
\frac14|\omega|^2I,
$$

we have:

$$
\boxed{
\begin{aligned}
\mathcal A_\omega
={}&
-\frac14
\left[
(\omega\otimes\omega)S
+
S(\omega\otimes\omega)
\right]
\\
&+
\frac12|\omega|^2S
+
\frac16
(\omega^\top S\omega)I.
\end{aligned}
}
\tag{5.1}
$$

Its trace is exactly zero.

---

# 6. Pressure contribution to cofactor dynamics

For:

$$
G_p=-H_p,
$$

we have:

$$
\boxed{
\mathcal A_p
=
-
(H_pS+SH_p)
+
\frac23
(S:H_p)I.
}
\tag{6.1}
$$

Thus, pressure not only acts as:

$$
H_p^0
$$

and:

$$
C
$$

as an external coherence partner,

but also directly enters:

$$
C
$$

its own dynamics.

This forms a closed nonlocal feedback loop:

$$
\boxed{
S
\to
C(S)
\leftrightarrow
H_p
\to
D_tS
\to
D_tC.
}
$$

---

# 7. Self-amplification cofactor angular speed

Define the normalized cofactor:

$$
\widehat C
=
\frac{C}{|C|}
$$

for:

$$
|S|>0.
$$

The angular component of the self contribution is:

$$
\boxed{
P_C^\perp
\mathcal A_{\rm self}
=
-|S|^2
P_C^\perp S.
}
\tag{7.1}
$$

And:

$$
\boxed{
C:S
=
3\det S,
}
\tag{7.2}
$$

$$
\boxed{
|C|^2
=
\frac16|S|^4.
}
\tag{7.3}
$$

Thus:

$$
\boxed{
|P_C^\perp S|^2
=
|S|^2
-
\frac{
54(\det S)^2
}{
|S|^4
}.
}
\tag{7.4}
$$

Define the self cofactor angular rate:

$$
\boxed{
\Omega_{C,\rm self}
=
\frac{
|P_C^\perp\mathcal A_{\rm self}|
}{
|C|
}.
}
\tag{7.5}
$$

we obtain:

$$
\boxed{
\Omega_{C,\rm self}
=
\sqrt6
|S|
\sqrt{
1-
\frac{
54(\det S)^2
}{
|S|^6
}
}.
}
\tag{7.6}
$$

---

# 8. Axisymmetric cofactor-shape lock

The sharp determinant inequality:

$$
|\det S|
\le
\frac1{
3\sqrt6
}
|S|^3
$$

is equivalent to:

$$
\frac{
54(\det S)^2
}{
|S|^6
}
\le1.
$$

Thus:

$$
\boxed{
\Omega_{C,\rm self}=0
}
$$

exactly on the determinant-shape extremal branch:

$$
\boxed{
\operatorname{spec}(S)
\propto
(-2,1,1)
}
$$

or its sign reversal.

Therefore:

$$
\boxed{
\textbf{
strain self-amplification rotates cofactor shape
unless the strain spectrum is axisymmetric/extremal.
}
}
\tag{8.1}
$$

This reconnects with the spectral-shape leakage from Round 23.

---

# 9. Pressure source scalar

Define:

$$
\boxed{
q
=
|S|^2
-
\frac12|\omega|^2.
}
\tag{9.1}
$$

Pressure Poisson equation:

$$
\boxed{
-\Delta p=q.
}
\tag{9.2}
$$

Let the trace-free Riesz operator be:

$$
\boxed{
\mathcal T_0
=
\nabla^2(-\Delta)^{-1}
+
\frac13I.
}
\tag{9.3}
$$

Then:

$$
\boxed{
H
=
H_p^0
=
\mathcal T_0q.
}
\tag{9.4}
$$

---

# 10. Exact material equation for the pressure source

From the strain and vorticity equations:

$$
\boxed{
\begin{aligned}
D_tq
={}&
\nu\Delta q
-
2\nu|\nabla S|^2
+
\nu|\nabla\omega|^2
\\
&-
6\det S
-
\frac32
\omega^\top S\omega
-
2S:H_p.
\end{aligned}
}
\tag{10.1}
$$

Define:

$$
\boxed{
\mathcal N_q
=
-2\nu|\nabla S|^2
+
\nu|\nabla\omega|^2
-
6\det S
-
\frac32\omega^\top S\omega
-
2S:H_p.
}
\tag{10.2}
$$

Thus:

$$
\boxed{
D_tq
=
\nu\Delta q
+
\mathcal N_q.
}
\tag{10.3}
$$

---

# 11. Exact anisotropic pressure-Hessian dynamics

Since:

$$
H=\mathcal T_0q
$$

and:

$$
\mathcal T_0
$$

commutes with:

$$
\Delta,
$$

the material derivative is:

$$
\boxed{
D_tH
=
\nu\Delta H
+
\mathcal T_0\mathcal N_q
+
[u\cdot\nabla,\mathcal T_0]q.
}
\tag{11.1}
$$

Name the transport–Riesz commutator:

$$
\boxed{
\mathcal C_{u,\mathcal T_0}[q]
=
[u\cdot\nabla,\mathcal T_0]q.
}
\tag{11.2}
$$

Thus, the pressure anisotropy dynamics are driven by three types of sources:

1. viscous smoothing:
   $$
   \nu\Delta H;
   $$
2. nonlocal transformed scalar production:
   $$
   \mathcal T_0\mathcal N_q;
   $$
3. transport/nonlocal noncommutation:
   $$
   \mathcal C_{u,\mathcal T_0}[q].
   $$

---

# 12. Why pressure coherence is a commutator problem

If:

$$
u\cdot\nabla
$$

and:

$$
\mathcal T_0
$$

commuted,

the pressure anisotropy would only need to follow:

$$
q
$$

's material production.

But the actual NS equations have the additional term:

$$
\boxed{
[u\cdot\nabla,\mathcal T_0]q.
}
$$

Thus, the dynamics of the pressure tensor relative to the local strain/cofactor frame contain a genuine nonlocal transport mismatch.

Therefore:

$$
\boxed{
\textbf{
cofactor–pressure coherence stability is partly a transport–Riesz commutator problem.
}
}
\tag{12.1}
$$

---

# 13. Moving negative-determinant domain

Negative reserve domain:

$$
A_-(t)
=
\{d<0\}.
$$

Round 33 determinant scalar PDE:

$$
\boxed{
D_td
-
\nu\Delta d
=
F_d,
}
\tag{13.1}
$$

where:

$$
F_d
=
\nu\mathcal G_{\det}
+
\frac14|S\omega|^2
+
\operatorname{cof}S:H_p.
$$

Assume:

$$
\nabla d\ne0
$$

on:

$$
\partial A_-(t).
$$

outward normal:

$$
\boxed{
\eta
=
\frac{
\nabla d
}{
|\nabla d|
}.
}
\tag{13.2}
$$

---

# 14. Exact sign-boundary velocity

Let:

$$
V_n
$$

be the Eulerian normal velocity of:

$$
\partial A_-
$$

From level-set kinematics:

$$
\boxed{
V_n
=
u\cdot\eta
-
\beta_d,
}
\tag{14.1}
$$

where:

$$
\boxed{
\beta_d
=
\frac{
\nu\Delta d
+
F_d
}{
|\nabla d|
}
=
\frac{
D_td
}{
|\nabla d|
}.
}
\tag{14.2}
$$

Thus, the normal velocity of the sign interface relative to the fluid itself is:

$$
\boxed{
V_n-u\cdot\eta
=
-\beta_d.
}
\tag{14.3}
$$

---

# 15. Moving-domain transport law

For a smooth scalar/tensor contraction:

$$
\Phi,
$$

and:

$$
\nabla\cdot u=0,
$$

we have:

$$
\boxed{
\frac d{dt}
\int_{A_-(t)}
\Phi\,dx
=
\int_{A_-}
D_t\Phi\,dx
-
\int_{\partial A_-}
\beta_d
\Phi\,dS.
}
\tag{15.1}
$$

Thus, the cofactor–pressure coherence has a third type of dynamics:

$$
\boxed{
\text{sign-domain boundary replacement}.
}
$$

Even if:

$$
C,H
$$

remain unchanged at fixed spatial points,

a changing:

$$
A_-
$$

can also change the integrated coherence.

---

# 16. Moving-domain Hilbert vectors

Define:

$$
\boxed{
B
=
-H.
}
\tag{16.1}
$$

Thus, the replenishing coherence is:

$$
\boxed{
\rho
=
\rho_p^-
=
\frac{
\int_{A_-}
C:B\,dx
}{
UV
},
}
\tag{16.2}
$$

where:

$$
\boxed{
U
=
\|C\|_{2,A_-},
\qquad
V
=
\|B\|_{2,A_-}.
}
\tag{16.3}
$$

Let:

$$
\widehat C
=
C/U,
$$

$$
\widehat B
=
B/V
$$

be the moving-domain $L^2$ unit tensors.

---

# 17. Exact moving-domain coherence dynamics

Let:

$$
\boxed{
\mathcal A_C
=
D_tC,
}
\tag{17.1}
$$

$$
\boxed{
\mathcal A_B
=
D_tB
=
-D_tH.
}
\tag{17.2}
$$

Then:

$$
\boxed{
\begin{aligned}
\rho'
={}&
\frac1U
\int_{A_-}
\mathcal A_C:
(
\widehat B-\rho\widehat C
)
dx
\\
&+
\frac1V
\int_{A_-}
\mathcal A_B:
(
\widehat C-\rho\widehat B
)
dx
\\
&+
\mathcal B_{\rm sign}.
\end{aligned}
}
\tag{17.3}
$$

where the moving-sign-boundary correction is:

$$
\boxed{
\begin{aligned}
\mathcal B_{\rm sign}
={}&
-
\frac1{UV}
\int_{\partial A_-}
\beta_d
C:B\,dS
\\
&+
\frac{\rho}{2U^2}
\int_{\partial A_-}
\beta_d
|C|^2dS
\\
&+
\frac{\rho}{2V^2}
\int_{\partial A_-}
\beta_d
|B|^2dS.
\end{aligned}
}
\tag{17.4}
$$

Name this:

$$
\boxed{
\textbf{Moving-Domain Cofactor–Pressure Coherence Equation}.
}
$$

---

# 18. Three angular drivers

Equation (17.3) splits the variation of:

$$
\rho_p^-
$$

into:

## A — cofactor angular dynamics

$$
\boxed{
D_tC
}
$$

is driven by:

- self-amplification shape;
- viscosity;
- vorticity;
- pressure.

## B — pressure-response angular dynamics

$$
\boxed{
D_tH
}
$$

is driven by:

- pressure-source production;
- viscosity;
- transport–Riesz commutator.

## C — moving sign-domain dynamics

$$
\boxed{
\mathcal B_{\rm sign}
}
$$

is driven by the relative motion of the:

$$
d=0
$$

interface.

Thus, persistent pressure replenishment is a three-layer locking problem.

---

# 19. Interior angular-speed bound

Define the cofactor tangent speed:

$$
\boxed{
\Omega_C
=
\frac{
\left\|
P_{\widehat C}^{\perp}
\mathcal A_C
\right\|_{2,A_-}
}{
U
}.
}
\tag{19.1}
$$

Define the pressure tangent speed:

$$
\boxed{
\Omega_H
=
\frac{
\left\|
P_{\widehat B}^{\perp}
\mathcal A_B
\right\|_{2,A_-}
}{
V
}.
}
\tag{19.2}
$$

Since:

$$
\|
\widehat B-\rho\widehat C
\|_2
=
\sqrt{
1-\rho^2
},
$$

we have:

$$
\boxed{
|
\rho'
-
\mathcal B_{\rm sign}
|
\le
\sqrt{
1-\rho^2
}
(
\Omega_C+\Omega_H
).
}
\tag{19.3}
$$

If:

$$
|\rho|<1,
$$

define:

$$
\theta
=
\arccos\rho.
$$

Then:

$$
\boxed{
\left|
\theta'
+
\frac{
\mathcal B_{\rm sign}
}{
\sqrt{
1-\rho^2
}
}
\right|
\le
\Omega_C+\Omega_H.
}
\tag{19.4}
$$

---

# 20. Coherence persistence burden

If:

$$
\rho\approx1
$$

is to be maintained for a long time,

one must simultaneously control:

$$
\boxed{
\text{relative cofactor/pressure tangent motion}
}
$$

and:

$$
\boxed{
\text{moving-sign-domain boundary flux}.
}
$$

Therefore:

$$
\boxed{
\text{pressure coherence lock}
}
$$

is not a single local alignment.

It requires:

$$
\boxed{
\mathcal A_C
\approx
\text{normalized }\mathcal A_B
}
$$

on tangent directions,

and that:

$$
\mathcal B_{\rm sign}
$$

cannot rapidly dismantle the lock.

---

# 21. Self-amplification does not guarantee dephasing

Round 27:

$$
-S^2
$$

does not directly rotate the strain eigenframe.

Round 36:

$$
-S^2
$$

generally rotates the direction of:

$$
C_S^0
$$

in the tensor-shape space,

but:

$$
\boxed{
\Omega_{C,\rm self}=0
}
$$

on axisymmetric determinant-extremal shapes.

Thus, a dangerous shape can exhibit:

$$
\boxed{
\text{large self-amplification}
+
\text{zero self-induced cofactor dephasing}.
}
$$

Therefore, there is no universal:

$$
\boxed{
\text{dangerous strain}
\Rightarrow
\Omega_C\ge c|S|
}
$$

with a fixed:

$$
c>0.
$$

---

# 22. Affine Perfect Coherence-Lock Witness

Let there be a constant trace-free symmetric matrix:

$$
S_0.
$$

Take the affine velocity:

$$
\boxed{
u(x)=S_0x.
}
\tag{22.1}
$$

and the quadratic pressure:

$$
\boxed{
p(x)
=
-\frac12
x^\top
S_0^2
x.
}
\tag{22.2}
$$

Then:

$$
\nabla\cdot u=0,
$$

$$
\Delta u=0,
$$

and:

$$
(u\cdot\nabla)u
=
S_0^2x
=
-\nabla p.
$$

Thus, this is a stationary affine Euler solution, which also satisfies the viscous NS equation since:

$$
\Delta u=0.
$$

It is not a whole-space finite-energy solution.

---

# 23. Perfect cofactor–pressure anti-alignment

For the affine witness:

$$
H_p
=
-S_0^2.
$$

Therefore:

$$
\boxed{
H_p^0
=
-
\left(
S_0^2
-
\frac13|S_0|^2I
\right)
=
-C_0.
}
\tag{23.1}
$$

Thus:

$$
\boxed{
B=-H_p^0=C_0.
}
$$

On any finite test region:

$$
\boxed{
\rho_p^-=1.
}
\tag{23.2}
$$

And:

$$
\boxed{
\rho_p^-(t)
\equiv1.
}
$$

If we choose:

$$
S_0
=
\operatorname{diag}(-1,-1,2),
$$

then:

$$
\det S_0=2,
$$

thus:

$$
d=-2<0.
$$

The entire local region is located on the negative determinant reserve branch.

Therefore:

$$
\boxed{
\textbf{
there is no universal positive lower bound on cofactor–pressure dephasing speed.
}
}
\tag{23.3}
$$

This witness only rules out purely local/geometric universal dephasing; it does not claim to be a finite-energy global regularity counterexample.

---

# 24. What locks in the affine witness

In the stationary affine witness:

- the cofactor tensor is fixed;
- the anisotropic pressure Hessian is fixed;
- the sign domain is fixed;
- the transport–Riesz response is globally and exactly balanced;
- the coherence is:
  $$
  \rho=1.
  $$

Thus, actual dephasing must come from:

$$
\boxed{
\text{spatial inhomogeneity}
+
\text{viscous gradients}
+
\text{vorticity geometry}
+
\text{nonlocal pressure response}
+
\text{sign-interface motion}.
}
$$

It is not automatically provided by the tensor algebra itself.

---

# 25. Pressure-response budget

From:

$$
D_tH
=
\nu\Delta H
+
\mathcal T_0\mathcal N_q
+
\mathcal C_{u,\mathcal T_0}[q],
$$

we obtain the schematic:

$$
\boxed{
\Omega_H
\lesssim
\frac{
\nu\|\Delta H\|_{2,A_-}
+
\|\mathcal T_0\mathcal N_q\|_{2,A_-}
+
\|\mathcal C_{u,\mathcal T_0}[q]\|_{2,A_-}
}{
\|H\|_{2,A_-}
}.
}
\tag{25.1}
$$

Thus, to prove that:

$$
\rho
$$

rapidly dephases,

one must have lower-bound information on the pressure angular forcing;

to prove that a persistent lock is expensive,

one needs upper-bound/control information.

Both require genuine nonlocal pressure-response estimates.

---

# 26. Commutator regularity burden

The transport–Riesz commutator:

$$
\boxed{
[u\cdot\nabla,\mathcal T_0]q
}
$$

is sensitive to velocity regularity.

Therefore:

$$
\boxed{
\text{pressure coherence dynamics}
}
$$

reconnects once again to:

- velocity-gradient control;
- singular-integral commutator estimates;
- higher spatial regularity.

This is consistent with the budget recycling from Round 30:

$$
\boxed{
\text{valid representation}
\neq
\text{free commutator budget}.
}
$$

---

# 27. Moving-sign boundary is an independent leakage channel

Even if:

$$
\mathcal A_C
$$

and:

$$
\mathcal A_B
$$

perfectly lock in the interior,

if:

$$
\beta_d
$$

on the:

$$
d=0
$$

surface reselects high/low coherence regions,

then:

$$
\mathcal B_{\rm sign}
$$

can still cause:

$$
\rho
$$

to change.

Thus:

$$
\boxed{
\text{fixed-domain coherence control}
}
$$

does not directly imply:

$$
\boxed{
\text{negative-reserve-domain coherence control}.
}
$$

A true global route requires:

$$
\boxed{
\text{tensor dynamics}
+
\text{pressure response}
+
\text{level-set transport}.
}
$$

---

# 28. Smooth-mask formulation

If:

$$
d=0
$$

is not a regular level set,

one can use a smooth mask:

$$
\boxed{
\chi_{\varepsilon}^-(d)
=
\chi(-d/\varepsilon)
}
\tag{28.1}
$$

with a smooth monotone:

$$
\chi.
$$

Define the weighted coherence:

$$
\boxed{
\rho_{\varepsilon}
=
-
\frac{
\int
\chi_\varepsilon^-(d)
C:Hdx
}{
\left(
\int
\chi_\varepsilon^-(d)|C|^2dx
\right)^{1/2}
\left(
\int
\chi_\varepsilon^-(d)|H|^2dx
\right)^{1/2}
}.
}
\tag{28.2}
$$

All time derivatives are classical weighted integrals.

Then study:

$$
\varepsilon\downarrow0.
$$

Thus, moving-domain singularities do not force the discretization into sign cells.

---

# 29. Coherence-lock alternatives

A long-lived positive:

$$
\rho_p^-
$$

can currently only rely on:

$$
\boxed{
\begin{aligned}
\mathrm{L1}:&
\quad
\text{axisymmetric/extremal cofactor-shape slowing},
\\
\mathrm{L2}:&
\quad
\text{pressure-response tangent locking},
\\
\mathrm{L3}:&
\quad
\text{transport–Riesz commutator balance},
\\
\mathrm{L4}:&
\quad
\text{moving sign-domain boundary balance},
\\
\mathrm{L5}:&
\quad
\text{strong amplitude modulation masking angular drift}.
\end{aligned}
}
\tag{29.1}
$$

None of these is a purely algebraic free regularizer.

---

# 30. STOP-C40 — Cofactor–Pressure Lock / Moving-Domain Commutator Gap

$$
\boxed{
\begin{aligned}
\text{layer}
&=
\mathrm{cofactor\text{-}pressure\ coherence\ dynamics},
\\
\text{cofactor equation}
&=
D_tC
=
\mathcal A_\nu
+
\mathcal A_{\rm self}
+
\mathcal A_\omega
+
\mathcal A_p,
\\
\text{self cofactor angular rate}
&=
\sqrt6|S|
\sqrt{
1-54(\det S)^2/|S|^6
},
\\
\text{axisymmetric self dephasing}
&=
0,
\\
\text{pressure anisotropy}
&=
\mathcal T_0q,
\\
\text{pressure dynamics}
&=
\nu\Delta H
+
\mathcal T_0\mathcal N_q
+
[u\cdot\nabla,\mathcal T_0]q,
\\
\text{sign-domain dynamics}
&=
\mathcal B_{\rm sign},
\\
\text{perfect local/affine lock}
&=
\mathrm{possible},
\\
\text{universal dephasing}
&=
\mathrm{false},
\\
\text{missing}
&=
\mathrm{finite\text{-}energy\ spacetime\ control
of\ relative\ tensor\ angular\ forcing,
transport\text{-}Riesz\ commutator,
and\ moving\ sign\ boundary},
\\
T_{\mathsf C\to\mathsf D}
&=
\mathrm{NOT\ REACHED}.
\end{aligned}
}
$$

Name this:

$$
\boxed{
\textbf{STOP-C40:
Cofactor–Pressure Lock / Moving-Domain Commutator Gap}.
}
$$

---

# 31. 24/72 Ledger — Round 36

| Step | object | $B$ | $U$ | $O$ | $L$ | status |
|---|---|---|---|---|---|---|
| C532 | cofactor material derivative | $\mathsf C$ | tensor PDE | relational | $\mathsf F$ | EXACT |
| C533 | self-amplification cofactor term | $\mathsf C$ | tensor algebra | targeted | $\mathsf F$ | EXACT |
| C534 | vorticity cofactor forcing | $\mathsf C$ | tensor coupling | relational | $\mathsf F$ | EXACT |
| C535 | pressure cofactor forcing | $\mathsf C$ | tensor coupling | relational | $\mathsf F$ | EXACT |
| C536 | self cofactor angular speed | $\mathsf C$ | tensor geometry | scalar | $\mathsf F$ | PROVED |
| C537 | axisymmetric angular lock | $\mathsf C$ | spectral shape | targeted | $\mathsf F$ | PROVED |
| C538 | pressure source $q$ dynamics | $\mathsf C$ | scalar PDE | relational | $\mathsf F$ | EXACT |
| C539 | anisotropic pressure dynamics | $\mathsf C$ | Riesz/transport | tensor | $\mathsf F$ | EXACT |
| C540 | transport–Riesz commutator | $\mathsf C$ | nonlocal transport | relational | $\mathsf F$ | IDENTIFIED |
| C541 | sign-boundary normal velocity | $\mathsf C$ | level-set transport | scalar | $\mathsf F$ | EXACT |
| C542 | moving-domain transport law | $\mathsf C$ | Reynolds transport | relational | $\mathsf F$ | EXACT |
| C543 | moving-domain coherence equation | $\mathsf C$ | Hilbert geometry | scalar | $\mathsf F$ | EXACT |
| C544 | interior angular-speed bound | $\mathsf C$ | tangent geometry | targeted | $\mathsf F$ | PROVED |
| C545 | affine perfect-lock witness | $\mathsf C$ | local affine flow | targeted | $\mathsf F$ | CONSTRUCTED |
| C546 | universal pressure dephasing | $\mathsf C$ | coherence dynamics | targeted | $\mathsf F$ | REFUTED |
| C547 | smooth-mask sign-domain route | $\mathsf C$ | regularization | profile | $\mathsf F$ | LEGAL |
| C548 | finite-energy coherence-lock exclusion | $\mathsf C$ | coupled NS | targeted | $\mathsf F$ | OPEN / STOP-C40 |

---

# 32. Continuous-versus-discrete status

All core objects in this round:

- continuous trace-free tensors;
- continuous Riesz operators;
- continuous commutators;
- continuous level-set velocity;
- continuous moving domains;
- continuous smooth sign masks;
- continuous Hilbert angles.

There are no:

- pressure modes enumeration;
- sign cells;
- discrete eigenframe states;
- graph level-set motion.

Therefore:

$$
\boxed{
T_{\mathsf C\to\mathsf D}
=
\text{NOT YET REACHED}.
}
$$

---

# 33. Strongest results of Round 36

## R36-A — exact cofactor material dynamics

$$
\boxed{
D_tC
=
(D_tS)S
+
S(D_tS)
-
\frac23
(S:D_tS)I.
}
$$

## R36-B — self-amplification cofactor angular rate

$$
\boxed{
\Omega_{C,\rm self}
=
\sqrt6|S|
\sqrt{
1-
54(\det S)^2/|S|^6
}.
}
$$

## R36-C — exact anisotropic pressure dynamics

$$
\boxed{
D_tH_p^0
=
\nu\Delta H_p^0
+
\mathcal T_0\mathcal N_q
+
[u\cdot\nabla,\mathcal T_0]q.
}
$$

## R36-D — moving sign-domain coherence equation

$$
\boxed{
\rho'
=
\text{cofactor tangent motion}
+
\text{pressure tangent motion}
+
\text{sign-boundary flux}.
}
$$

## R36-E — affine perfect-lock no-go

stationary affine strain gives:

$$
\boxed{
H_p^0=-C_S^0,
\qquad
\rho_p^-=1.
}
$$

Thus, a universal positive dephasing-speed lower bound does not exist.

---

# 34. Next round — Pressure-Response Lock Budget / Commutator Depletion

Round 36 has established that:

$$
\boxed{
\text{perfect coherence lock can exist in local affine geometry}.
}
$$

Thus, the next round will no longer attempt pointwise universal dephasing.

Instead, it directly asks:

$$
\boxed{
\text{how much commutator and gradient budget must finite-energy / inhomogeneous NS pay to maintain a near-affine pressure response lock?}
}
$$

Specifically:

1. Define the affine-response defect:
   $$
   E_p
   =
   H_p^0+C_S^0;
   $$

2. Derive:
   $$
   D_tE_p;
   $$

3. The stationary affine lock is exactly:
   $$
   E_p=0;
   $$

4. Examine how viscosity, vorticity, pressure-source nonlocality, and the Riesz commutator generate:
   $$
   E_p;
   $$

5. For:
   $$
   \|E_p\|_2^2
   $$
   establish a defect-energy equation;

6. If near-lock requires:
   $$
   E_p
   $$
   to be small, study the cancellation required to maintain it;

7. Connect the commutator budget to the higher-gradient / critical regularity from Round 30;

8. If $E_p$ cannot be suppressed by lower-order budgets, then the pressure replenishment lock is once again not a free mechanism.

---

# 35. External primary-source anchors

1. Maurizio Carbone, Michele Iovieno, Andrew D. Bragg, *Gauge symmetry and dimensionality reduction of the anisotropic pressure Hessian*, arXiv:1911.08652.
   - The anisotropic pressure Hessian is a nonlocal functional in velocity-gradient dynamics, exhibiting a significant alignment structure relative to the strain eigenframe / vorticity.

2. Josin Tom, Maurizio Carbone, Andrew D. Bragg, *Exploring the turbulent velocity gradients at different scales from the perspective of the strain-rate eigenframe*, arXiv:2005.04300.
   - The importance of strain-rate eigenframe dynamics and the anisotropic pressure Hessian for eigenframe rotation.

3. Borys Álvarez-Samaniego, Wilson P. Álvarez-Samaniego, Pedro G. Fernández-Dalgo, *On the use of the Riesz transforms to determine the pressure term in the incompressible Navier-Stokes equations on the whole space*, arXiv:2004.02588.
   - Background on the Riesz-transform representation of whole-space pressure.

4. Elias Hess-Childs, Matthew Rosenzweig, Sylvia Serfaty, *Another look at regularity in transport-commutator estimates*, arXiv:2601.02326.
   - Recent primary-source background on the sensitivity of Riesz-type transport commutator estimates to transport velocity regularity; this round only uses it as a structural anchor for the difficulty of the commutator budget.

The cofactor material dynamics, self-cofactor angular-rate identity, pressure-source dynamics, moving sign-domain coherence equation, and affine perfect-lock witness in this round are all directly derived in this document.

---

# 36. Commit state

$$
\boxed{
\begin{aligned}
\text{Route}
&=
\mathrm{Pure\ Continuous\ Cofactor\text{-}Pressure\ Coherence\ Dynamics},
\\
\text{Essential }\mathsf C\to\mathsf D
&=
\mathrm{Not\ reached},
\\
\text{Cofactor angular dynamics}
&=
\mathrm{self}
+
\mathrm{viscosity}
+
\mathrm{vorticity}
+
\mathrm{pressure},
\\
\text{Pressure angular dynamics}
&=
\mathrm{source}
+
\mathrm{viscosity}
+
\mathrm{transport\text{-}Riesz\ commutator},
\\
\text{Sign-domain angular dynamics}
&=
\mathrm{moving\ level\text{-}set\ flux},
\\
\text{Universal dephasing}
&=
\mathrm{false},
\\
\text{Perfect local affine lock}
&=
\mathrm{possible},
\\
\text{STOP-C40}
&=
\mathrm{Cofactor\text{-}Pressure\ Lock/Moving\text{-}Domain\ Commutator\ Gap},
\\
\text{Next}
&=
\mathrm{Pressure\text{-}Response\ Lock\ Budget/Commutator\ Depletion}.
\end{aligned}
}
$$