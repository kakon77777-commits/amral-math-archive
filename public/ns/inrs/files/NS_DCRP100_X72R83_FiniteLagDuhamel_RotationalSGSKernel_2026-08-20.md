# DCRP100 / X72-R83 — Finite-Lag X-Defect Duhamel Split, Cross-Level Scope Repair, and the Rotational SGS Transfer Kernel

**Series:** Independent Navier–Stokes Research Series / X72 Bridge  
**Date:** 2026-08-20  
**Status:** proof-development checkpoint / finite-lag X–Kelvin transfer round  
**Immediate predecessor:** `NS_DCRP99_X72R82_XKelvin_BoundedLagSynchronization_2026-08-20.md`

## Primary internal dependencies

- DCRP63 — X branch split into pressure-defect oscillation vs temporal Floquet modulation.
- DCRP81–85 — filtered Kelvin SGS circulation and increment/trace compiler.
- DCRP95 — sign-coherent SGS Kelvin phase-slip conveyor.
- DCRP99 — fixed oriented Kelvin-slip coordinate + fixed X detector + fixed bounded lag.
- X72 Round37 — exact affine-response defect PDE.
- X72 Round38 — pressure self-commutator null identity and transport–Riesz triple-increment pairing.

## Fresh primary-source calibration

- R. Yu, *Filtered Vortex Stretching and Subgrid Defects for the Three-Dimensional Navier–Stokes Equations*, arXiv:2606.27560 (2026).
- R. Yu, *Coarse-Grained Resolution and Pressure-Flux Work Depletion for Navier-Stokes CKN Badness*, arXiv:2606.25322 (2026).
- R. Yu, *A Structural Audit of Navier-Stokes Obstruction Calculus*, arXiv:2606.25341 (2026).
- G. L. Eyink, *The Cascade of Circulations in Fluid Turbulence*, arXiv:physics/0606159.
- P. Constantin, M. Ignatova, V. Vicol, *On putative self-similarity for incompressible 3D Euler*, arXiv:2602.17570v3.

No full Navier–Stokes regularity theorem is claimed.

---

# 0. Executive result

D99 produced the final compact recurrence word:

\[
\boxed{
\sigma_*
\delta_\Gamma^{\rm SGS}(n)\ge c_{\rm slip}
}
\]

and

\[
\boxed{
X_*(n+\ell_*)\ge c_X
}
\]

on a positive-density set, with fixed bounded lag:

\[
|\ell_*|<\infty.
\]

The tempting next step is:

\[
\text{Kelvin SGS reset}
\Longrightarrow
\text{later X72 defect}.
\]

DCRP100 shows that this implication is **not presently justified as a direct coercive transfer**.

There are two independent reasons.

## Reason 1 — level mismatch

The D95 Kelvin reset is a **filtered prelimit SGS circulation source**:

\[
f_\ell
=
-\nabla\cdot R_\ell.
\]

The X72 Round37 pressure-response defect is a profile/NS defect variable:

\[
E
=
H_p^0+C_S^0.
\]

Its exact equation is:

\[
\boxed{
D_tE
-
\nu\Delta E
=
-
\mathscr L_S[E]
+
\mathcal F_E,
}
\tag{0.1}
\]

with:

\[
\boxed{
\mathcal F_E
=
-2\nu Q_C
+
V_C
+
\mathcal T_0N_0
+
[u\cdot\nabla,\mathcal T_0]q.
}
\tag{0.2}
\]

The filtered SGS force does **not** appear as a separate additive term in this already-passed-to-profile equation.

A scale-uniform filtered-to-profile transfer bridge is therefore required before one can claim direct causation.

## Reason 2 — rotational SGS kernel

Even at the filtered forced-equation level, Kelvin circulation measures the rotational/loop component of \(f_\ell\), while the most direct strain/pressure response sees the symmetric gradient:

\[
(\operatorname{Sym}\nabla f_\ell)^0.
\]

There is an exact local algebraic kernel.

Let:

\[
\boxed{
f(x)=Bx,
\qquad
B^T=-B.
}
\tag{0.3}
\]

Then:

\[
\boxed{
\operatorname{Sym}\nabla f=0,
}
\tag{0.4}
\]

but for a loop enclosing nonzero oriented area:

\[
\boxed{
\oint_Cf\cdot dx\neq0.
}
\tag{0.5}
\]

Moreover in three dimensions define:

\[
\boxed{
R_B(x)
=
-\frac15
\left[
(Bx)\otimes x
+
x\otimes(Bx)
\right].
}
\tag{0.6}
\]

Then:

\[
\boxed{
\nabla\cdot R_B=-Bx,
}
\tag{0.7}
\]

so:

\[
\boxed{
-\nabla\cdot R_B=f.
}
\tag{0.8}
\]

On a bounded ball one may add a sufficiently large constant isotropic tensor:

\[
R_B+cI
\]

to make the stress positive semidefinite locally without changing its divergence.

This is an algebraic local stress witness only; D100 does **not** claim that every such stress is globally realizable as an actual Reynolds covariance of a Navier–Stokes field.

Consequently there is no universal instantaneous inequality of the form:

\[
\boxed{
|\Gamma_{\rm SGS}|
\le
C
\|
(\operatorname{Sym}\nabla f_\ell)^0
\|
}
\]

on the full stress class.

The correct D100 result is therefore a finite-channel Duhamel compiler, not a direct Kelvin-to-X coercivity theorem.

---

# 1. Exact X72 Round37 defect PDE

Round37 defines:

\[
\boxed{
\mathcal T_0
=
\nabla^2(-\Delta)^{-1}
+
\frac13I.
}
\]

The exact pressure-response defect PDE is:

\[
D_tE
-
\nu\Delta E
=
-\mathscr L_S[E]
+
\mathcal F_E,
\]

where:

\[
\mathscr L_S[E]
=
L_S(E)
+
2\mathcal T_0(S:E),
\]

and:

\[
\mathcal F_E
=
F_1+F_2+F_3+F_4,
\]

with:

\[
\boxed{
F_1=-2\nu Q_C,
}
\]

\[
\boxed{
F_2=V_C,
}
\]

\[
\boxed{
F_3=\mathcal T_0N_0,
}
\]

\[
\boxed{
F_4=[u\cdot\nabla,\mathcal T_0]q.
}
\]

This is the exact starting point for a finite-lag X transfer analysis.

---

# 2. Evolution family and exact Duhamel formula

Write the defect PDE as:

\[
\partial_tE
=
\mathcal A_E(t)E
+
\mathcal F_E(t),
\]

where:

\[
\boxed{
\mathcal A_E(t)
=
\nu\Delta
-
u\cdot\nabla
-
\mathscr L_S.
}
\tag{2.1}
\]

On a smooth compact normalized branch, let:

\[
\mathcal U_E(t,s)
\]

be the evolution family generated by \(\mathcal A_E\).

Then:

## Theorem D100.1 — Exact X-Defect Duhamel Formula

\[
\boxed{
E(t_1)
=
\mathcal U_E(t_1,t_0)E(t_0)
+
\int_{t_0}^{t_1}
\mathcal U_E(t_1,s)
\mathcal F_E(s)
\,ds.
}
\tag{2.2}
\]

Let \(\Psi_X\) be one fixed linear dual detector from the finite D99 X test family.

Then:

\[
\boxed{
\begin{aligned}
\langle E(t_1),\Psi_X\rangle
={}&
\langle
E(t_0),
\mathcal U_E(t_1,t_0)^*\Psi_X
\rangle
\\
&+
\sum_{r=1}^4
\int_{t_0}^{t_1}
\left\langle
F_r(s),
\mathcal U_E(t_1,s)^*\Psi_X
\right\rangle
ds.
\end{aligned}
}
\tag{2.3}
\]

This is the exact finite-lag adjoint transfer identity available from the current X72 equation.

---

# 3. Five X-support channels

Define:

\[
\boxed{
M_X
=
\left|
\left\langle
E(t_0),
\mathcal U_E(t_1,t_0)^*\Psi_X
\right\rangle
\right|
}
\tag{3.1}
\]

and:

\[
\boxed{
I_r
=
\left|
\int_{t_0}^{t_1}
\left\langle
F_r,
\mathcal U_E(t_1,s)^*\Psi_X
\right\rangle ds
\right|.
}
\tag{3.2}
\]

If:

\[
|\langle E(t_1),\Psi_X\rangle|
\ge
c_X,
\]

then:

## Theorem D100.2 — Finite-Lag X Source Pigeonhole

\[
\boxed{
M_X
\vee
I_1
\vee
I_2
\vee
I_3
\vee
I_4
\ge
\frac{c_X}{5}.
}
\tag{3.3}
\]

Thus every pressure-response X event at the fixed D99 lag is supplied by at least one of:

1. inherited X-defect memory;
2. viscous/strain-gradient mismatch;
3. vorticity/cofactor forcing;
4. transformed pressure-source mismatch;
5. transport–Riesz commutator.

This is an exact finite forcing alphabet.

---

# 4. X modulation subtype must be separated

D63 shows that the aligned/no-turnover X branch splits into:

\[
\boxed{
X_{\rm osc}
\vee
X_{\rm mod}.
}
\]

The \(X_{\rm osc}\) branch is a spatial pressure/cofactor defect and fits the linear defect-observer Duhamel analysis above.

The \(X_{\rm mod}\) branch instead satisfies a finite-dimensional Floquet/Fisher modulation condition such as:

\[
\int
Z(\lambda-\lambda_*)^2
\gtrsim
\int Z.
\]

Therefore:

## Theorem D100.3 — X-Type Split

The D99 bounded-lag word refines to:

\[
\boxed{
\mathsf C_{X\Gamma}^{\ell_*}
\Longrightarrow
\mathsf C_{X_{\rm mod}\Gamma}^{\ell_*}
\vee
\mathsf C_{X_{\rm osc}\Gamma}^{\ell_*}.
}
\tag{4.1}
\]

Only the second branch is governed directly by (2.3).

This avoids mixing a temporal eigenvalue-modulation observable with a pressure-defect tensor observable.

---

# 5. Forced coarse-grained gradient identity

Now return to the filtered Navier–Stokes equation:

\[
\boxed{
\partial_tU
-
\nu\Delta U
+
(U\cdot\nabla)U
+
\nabla P
=
f_\ell,
}
\tag{5.1}
\]

where:

\[
\boxed{
f_\ell
=
-\nabla\cdot R_\ell.
}
\tag{5.2}
\]

Let:

\[
L=\nabla U,
\qquad
S=\operatorname{Sym}L,
\qquad
A=\operatorname{Skew}L.
\]

Differentiating gives:

\[
D_tL
-
\nu\Delta L
+
L^2
+
H_P
=
\nabla f_\ell.
\]

Take the trace-free symmetric part.

## Theorem D100.4 — Exact Forced Gradient-Response Identity

\[
\boxed{
D_tS
-
\nu\Delta S
+
H_P^0
+
(S^2+A^2)^0
=
(\operatorname{Sym}\nabla f_\ell)^0.
}
\tag{5.3}
\]

Define the trace-free filtered gradient-response tensor:

\[
\boxed{
\mathcal G_\ell
=
H_P^0
+
(S^2+A^2)^0.
}
\tag{5.4}
\]

Then:

\[
\boxed{
\mathcal G_\ell
=
(\operatorname{Sym}\nabla f_\ell)^0
-
D_tS
+
\nu\Delta S.
}
\tag{5.5}
\]

This is the exact direct filtered force-to-gradient response.

---

# 6. Relation to the X72 pressure-response tensor

Let:

\[
\Omega=\nabla\times U,
\]

and:

\[
W_\Omega
=
\Omega\otimes\Omega
-
\frac13|\Omega|^2I.
\]

For the X72-type tensor:

\[
E_{p,\ell}^{X72}
=
H_P
+
S^2
-
\frac16|\Omega|^2I,
\]

the filtered pressure Poisson equation is modified by \(f_\ell\):

\[
\Delta P
+
|S|^2
-
\frac12|\Omega|^2
=
\nabla\cdot f_\ell.
\]

A direct computation gives:

## Theorem D100.5 — Filtered X72/Gradient Response Bridge

\[
\boxed{
\mathcal G_\ell
=
E_{p,\ell}^{X72}
+
\frac14W_\Omega
-
\frac13
(\nabla\cdot f_\ell)I.
}
\tag{6.1}
\]

Since:

\[
f_\ell=-\nabla\cdot R_\ell,
\]

\[
\boxed{
\mathcal G_\ell
=
E_{p,\ell}^{X72}
+
\frac14W_\Omega
+
\frac13
(\nabla\cdot\nabla\cdot R_\ell)I.
}
\tag{6.2}
\]

Thus even at the filtered level the direct symmetric-gradient response is not the same object as the X72 pressure-response tensor.

Vorticity stress and the isotropic SGS pressure source must also be separated.

---

# 7. Kelvin circulation sees the rotational force sector

The SGS Kelvin flux around a closed filtered material loop is:

\[
\boxed{
K_\ell(C,t)
=
\oint_C
f_\ell\cdot dx
}
\tag{7.1}
\]

up to the sign convention of D81/D95.

By Stokes:

\[
\boxed{
K_\ell(C,t)
=
\int_{\Sigma_C}
\nabla\times f_\ell\cdot n
\,dA.
}
\tag{7.2}
\]

Therefore Kelvin reset sees:

\[
\boxed{
\nabla\times f_\ell,
}
\]

whereas the direct filtered gradient response sees:

\[
\boxed{
(\operatorname{Sym}\nabla f_\ell)^0.
}
\]

These are independent components of the first derivative of \(f_\ell\).

---

# 8. Exact rotational-force kernel

Let:

\[
B^T=-B,
\]

and define:

\[
\boxed{
f(x)=Bx.
}
\]

Then:

\[
\nabla f=B,
\]

so:

## Theorem D100.6 — Rigid Vortex-Force Kernel

\[
\boxed{
\operatorname{Sym}\nabla f=0,
}
\tag{8.1}
\]

\[
\boxed{
\nabla\cdot f=0,
}
\tag{8.2}
\]

but generally:

\[
\boxed{
\nabla\times f\neq0.
}
\tag{8.3}
\]

If:

\[
Bx=b\times x,
\]

then:

\[
\boxed{
\nabla\times f=2b.
}
\tag{8.4}
\]

For any oriented loop with vector area \(\mathcal A_C\):

\[
\boxed{
\oint_Cf\cdot dx
=
2b\cdot\mathcal A_C.
}
\tag{8.5}
\]

Hence:

\[
\boxed{
K_\ell\neq0
\quad\text{while}\quad
(\operatorname{Sym}\nabla f)^0=0.
}
\tag{8.6}
\]

This is a sharp pointwise/local transfer-orthogonality witness.

---

# 9. Symmetric stress realization of the kernel

In three dimensions define:

\[
\boxed{
R_B(x)
=
-\frac15
\left[
(Bx)\otimes x
+
x\otimes(Bx)
\right].
}
\tag{9.1}
\]

This tensor is symmetric.

A direct differentiation gives:

## Theorem D100.7 — Symmetric-Stress Vortex-Force Realization

\[
\boxed{
\nabla\cdot R_B
=
-Bx.
}
\tag{9.2}
\]

Thus:

\[
\boxed{
-\nabla\cdot R_B
=
f.
}
\tag{9.3}
\]

On a fixed bounded ball \(B_R\), choose:

\[
c>
\sup_{x\in B_R}
\|R_B(x)\|_{\rm op}.
\]

Then:

\[
\boxed{
R_B+cI
\ge0
}
\tag{9.4}
\]

throughout the ball, while:

\[
\nabla\cdot(R_B+cI)
=
\nabla\cdot R_B.
\]

Therefore the rotational transfer kernel is compatible with a locally positive-semidefinite symmetric stress field.

### Important scope

D100 does **not** claim that this constructed stress is globally realizable as the exact filter covariance of one incompressible velocity field.

Its role is algebraic:

> positivity and symmetry of the stress alone do not imply Kelvin-to-symmetric-gradient coercivity.

---

# 10. Direct coercivity NO-GO

Suppose one attempted a universal estimate:

\[
\boxed{
\left|
\oint_C
(-\nabla\cdot R)\cdot dx
\right|
\le
C
\|
(\operatorname{Sym}\nabla\nabla\cdot R)^0
\|_{\mathcal Y}.
}
\tag{10.1}
\]

The stress of D100.7 gives a nonzero left side and zero direct symmetric-gradient force response in the interior.

Therefore:

## Theorem D100.8 — Kelvin-to-Direct-X Coercivity NO-GO

No such universal estimate can hold on the full local symmetric-stress class.

A direct cross-observer theorem requires additional dynamical/geometric restrictions on the SGS stress.

---

# 11. Why bounded lag does not fix the algebraic kernel

D99 proves:

\[
\Gamma_{\rm slip}(n)>0
\]

and:

\[
X(n+\ell_*)>0.
\]

This is a recurrence statement.

It does not imply:

\[
X(n+\ell_*)
=
\mathcal B_{\Gamma\to X}
\Gamma_{\rm slip}(n).
\]

The X defect may be carried by:

- pre-existing defect memory;
- \(F_1\);
- \(F_2\);
- \(F_3\);
- \(F_4\).

Therefore:

## Theorem D100.9 — Correlation/Causation Separation

\[
\boxed{
\text{bounded-lag X–Kelvin word}
\not\Rightarrow
\text{direct Kelvin-to-X source coercivity}.
}
\tag{11.1}
\]

The correct consequence is a finite forcing-channel split.

---

# 12. Finite-lag X-source compiler

Combine D99 with D100.2–3.

On the recurrent bounded-lag word, after finite detector/type pigeonholing, one fixed branch recurs at positive density:

\[
\boxed{
\mathsf C_{X_{\rm mod}\Gamma}^{\ell_*}
}
\]

or, on \(X_{\rm osc}\),

one of:

\[
\boxed{
\mathsf C_{{\rm mem}\Gamma}^{\ell_*},
}
\]

\[
\boxed{
\mathsf C_{Q_C\Gamma}^{\ell_*},
}
\]

\[
\boxed{
\mathsf C_{V_C\Gamma}^{\ell_*},
}
\]

\[
\boxed{
\mathsf C_{N_0\Gamma}^{\ell_*},
}
\]

\[
\boxed{
\mathsf C_{{\rm TR}\Gamma}^{\ell_*}.
}
\]

Thus:

## Theorem D100.10 — Finite-Lag Forcing Normal Form

\[
\boxed{
\mathsf C_{X\Gamma}^{\ell_*}
\Longrightarrow
\mathsf C_{X_{\rm mod}\Gamma}^{\ell_*}
\vee
\mathsf C_{{\rm mem}\Gamma}^{\ell_*}
\vee
\mathsf C_{Q_C\Gamma}^{\ell_*}
\vee
\mathsf C_{V_C\Gamma}^{\ell_*}
\vee
\mathsf C_{N_0\Gamma}^{\ell_*}
\vee
\mathsf C_{{\rm TR}\Gamma}^{\ell_*}
\vee
R_{\rm bridge}
\vee
R_{\rm state}
\vee
R_{\rm crit}.
}
\tag{12.1}
\]

Here \(R_{\rm bridge}\) records failure of the chosen filtered/prelimit X observable to shadow the profile-level X detector over the fixed lag.

This is the honest finite-lag transfer compiler.

---

# 13. Why the transport–Riesz branch has the highest leverage

Round38 proves the exact pairing identity:

\[
\boxed{
\begin{aligned}
\left\langle
E,
[u\cdot\nabla,\mathcal T_0]q
\right\rangle
=
-\frac12
\operatorname{p.v.}
\iint
&
[
\delta_{xy}u
\cdot
\nabla K_0(x-y)
]
\\
&:
\delta_{xy}E
\,
\delta_{xy}q
\,dxdy.
\end{aligned}
}
\tag{13.1}
\]

Thus the transport–Riesz source is an exact **triple-increment functional**.

The D95 SGS Kelvin slip is also generated by:

\[
R_\ell
\]

and hence by velocity-increment covariance.

Therefore the only D100 forcing branch that immediately shares the same native microstructure language as Kelvin slip is:

\[
\boxed{
\mathsf C_{{\rm TR}\Gamma}^{\ell_*}.
}
\]

This makes it the highest-leverage next target.

---

# 14. Pressure self-commutator cancellation

Round38 also proves:

\[
\boxed{
\left\langle
H_p^0,
[u\cdot\nabla,\mathcal T_0]q
\right\rangle
=
0.
}
\tag{14.1}
\]

Therefore:

\[
\boxed{
\left\langle
E_p,
[u\cdot\nabla,\mathcal T_0]q
\right\rangle
=
\left\langle
C_S^0,
[u\cdot\nabla,\mathcal T_0]q
\right\rangle.
}
\tag{14.2}
\]

The transport–Riesz branch detects **pressure/cofactor incompatibility**, not pressure self-interaction.

This suggests that a future Kelvin-to-X bridge should target the cofactor/increment geometry rather than the pure pressure Hessian.

---

# 15. Transfer-orthogonal source normal form

D100 isolates the direct local kernel:

\[
\boxed{
\mathcal K_{\Gamma\perp X}^{\rm rot}
=
\left\{
f:
(\operatorname{Sym}\nabla f)^0=0,
\quad
\oint_Cf\cdot dx\neq0
\right\}.
}
\tag{15.1}
\]

Its affine core is:

\[
\boxed{
f(x)=Bx,
\qquad
B^T=-B.
}
\tag{15.2}
\]

This is a rigid rotational/vortex-force jet.

If the actual recurrent SGS reset converges toward this kernel, direct strain response is suppressed while circulation reset remains active.

The later X event must then be generated by memory or one of the indirect Round37 forcing channels.

Thus the kernel is not itself a contradiction.

It is the exact obstruction to the naive cross-observer coercivity theorem.

---

# 16. Updated late architecture

D99 gave:

\[
\boxed{
\text{late compact survivor}
\Longrightarrow
\mathsf C_{X\Gamma}^{\ell_*}
\vee
R_{\rm state}
\vee
R_{\rm crit}.
}
\]

D100 refines the compact conveyor into a finite forcing alphabet.

No new infinite geometric branch appears.

The unresolved compact problem is now:

\[
\boxed{
\text{one fixed X source channel}
+
\text{one fixed oriented Kelvin-slip channel}
+
\text{one fixed lag}.
}
\]

This is significantly narrower than the D99 correlation word.

---

# 17. Status ledger

## PROVED this round

### D100-P1 — exact X72 defect evolution-family Duhamel formula.

### D100-P2 — one fixed-lag X pressure event is supported by one of five finite Duhamel channels.

### D100-P3 — D63 modulation X must be separated from pressure-defect X.

### D100-P4 — exact forced coarse-grained gradient-response identity.

### D100-P5 — exact relation between filtered gradient response and X72-type pressure response plus vorticity stress / SGS trace correction.

### D100-P6 — Kelvin circulation sees the curl/rotational SGS-force sector.

### D100-P7 — rigid skew-affine SGS force has nonzero circulation but zero symmetric-gradient response.

### D100-P8 — explicit symmetric stress \(R_B\) produces that rigid vortex force; local PSD can be enforced by adding a constant isotropic tensor.

### D100-P9 — no universal instantaneous Kelvin-to-direct-X coercivity exists on the full symmetric-stress class.

### D100-P10 — bounded lag is recurrence correlation, not direct source causation.

### D100-P11 — the bounded-lag X–Kelvin conveyor reduces to a finite X-source channel alphabet.

### D100-P12 — transport–Riesz is the highest-leverage branch because both it and SGS Kelvin slip have exact increment representations.

---

# 18. What is NOT proved

D100 does not prove:

- the rotational SGS stress witness is globally realizable by a Navier–Stokes Reynolds stress;
- the D99 Kelvin event directly causes the later X event;
- the filtered SGS force appears as a separate forcing term in the already-taken Euler/profile X72 defect equation;
- the finite-lag bridge residual is automatically small;
- one of the five X source channels is globally impossible;
- the transport–Riesz / Kelvin joint increment functional is coercive;
- global Navier–Stokes regularity.

The remaining problem is now a **finite-lag source-channel compatibility problem**.

---

# 19. STOP-D100

\[
\boxed{
\begin{minipage}{0.94\linewidth}
The D99 bounded-lag X72–Kelvin word does not by itself imply a direct Kelvin-to-X causal transfer. X72 Round37 gives the exact affine-response defect equation \(D_tE-\nu\Delta E=-\mathscr L_S[E]+\mathcal F_E\), with four forcing channels: viscous/strain-gradient mismatch, vorticity/cofactor forcing, transformed pressure-source mismatch, and transport–Riesz commutator. The exact adjoint Duhamel formula therefore decomposes any later linear X pressure test into inherited X memory plus those four channels. The D95 Kelvin reset, by contrast, is a filtered prelimit SGS circulation source \(f_\ell=-\nabla\cdot R_\ell\), so a filtered-to-profile bridge is required before it can be inserted into the Round37 source equation. Even at the filtered level there is no universal direct coercivity: the direct gradient response sees \((\operatorname{Sym}\nabla f_\ell)^0\), whereas Kelvin circulation sees \(\nabla\times f_\ell\). The rigid vortex force \(f(x)=Bx\), \(B^T=-B\), has zero symmetric gradient but nonzero loop circulation; moreover \(R_B=-[(Bx)\otimes x+x\otimes(Bx)]/5\) is symmetric and satisfies \(-\nabla\cdot R_B=f\), and can be made locally PSD by adding a constant isotropic tensor. Thus positive Kelvin slip can be direct-X-orthogonal. The correct late compiler is finite: one fixed lag and oriented Kelvin source paired with either X temporal modulation, inherited defect memory, viscous-gradient forcing, vorticity/cofactor forcing, transformed pressure forcing, or transport–Riesz forcing. The transport–Riesz branch is now the highest-leverage target because Round38 represents it by an exact triple-increment functional, while the SGS Kelvin source is also increment-generated.
\end{minipage}
}
\]

---

# 20. Next autonomous step

## DCRP101 / X72-R84 — Joint Kelvin / Transport–Riesz Increment Profile

**Working title**

> **Can the Same Critical Increment Young Profile Sustain Sign-Coherent SGS Kelvin Slip and a Fixed-Lag Transport–Riesz X72 Forcing without Developing an Oriented Third-Moment / Cofactor Lock?**

Primary tasks:

1. start from the recurrent branch:
   \[
   \mathsf C_{{\rm TR}\Gamma}^{\ell_*};
   \]
2. write the SGS Kelvin flux as an increment-covariance functional;
3. write Round38's X forcing as the exact triple-increment functional:
   \[
   \delta u\,\delta E\,\delta q;
   \]
4. pull the X test back over the fixed lag;
5. extract a joint Young/profile representation of:
   - second increment moment for Kelvin;
   - third mixed increment moment for X;
6. determine whether:
   - centered isotropic covariance,
   - pressure-compatible covariance,
   - rotational SGS kernel,
   can support both fixed signs;
7. seek a finite-dimensional oriented second/third-moment cone;
8. route concentration/fiber failure to state/critical escape.

Desired endpoint:

\[
\boxed{
\mathsf C_{{\rm TR}\Gamma}^{\ell_*}
\Longrightarrow
\text{oriented joint increment-moment lock}
\vee
R_{\rm state}
\vee
R_{\rm crit}.
}
\]

**End checkpoint:** DCRP100 / X72-R83.
