---
title: "Navier–Stokes C3-U: Pressure-Poor Heredity Decomposition, Adjoint Mean-Strain Transport, and Mean-to-Pointwise Rigidity"
subtitle: "A Conditional Heredity Theory for Weak Far-Pressure Support, Exact Adjoint Mean-Strain Transport, and Morrey/Shell Criteria for Upgrading Mean Strain to Pointwise Middle-Eigenvalue Geometry"
version: "v0.1"
date: "2026-08-14"
author: "Neo.K / EveMissLab"
language: "en-US"
status: "Theorem-style structural reduction / conditional rigidity note"
epistemic_status: "Exact pressure-matrix decomposition + exact adjoint mean-strain identity + standard Morrey/Weyl consequences + conditional ancestry heredity. Does NOT prove Navier–Stokes regularity."
---

# Navier–Stokes C3-U
# Pressure-Poor Heredity Decomposition, Adjoint Mean-Strain Transport, and Mean-to-Pointwise Rigidity

## 0. Current Round Positioning

C3-T compresses the two survivor branches from the previous round into two propagation gaps:

### Uniform-cone branch

Already have:

$$
K_\ast:v_{n,i}
\ge\gamma_0>0,
$$

But:

$$
\boxed{
\text{mean-strain cone}
\not\Rightarrow
\text{pointwise }\lambda_2^+\text{ geometry}.
}
$$

What is truly missing:

$$
\boxed{
\textbf{Mean-to-Pointwise Strain Rigidity}.
}
$$

### Cone-degeneration branch

There is a pressure-poor six-core witness at every scale,

But:

$$
\boxed{
\text{per-level pressure-poor witness}
\not\Rightarrow
\text{pressure-poor causal ray}.
}
$$

What is truly missing:

$$
\boxed{
\textbf{Pressure-Poor Heredity}.
}
$$

Obtained in this round:

1. The parent→child far-pressure matrix variation can be exactly decomposed into:
   - spatial shift;
   - near/far reclassification;
   - temporal pressure-source turnover;
2. The spatial shift itself has an additional:
   $$
   \kappa^{-1}
   $$
   suppression;
3. Reclassification is controlled by the annular rescaled enstrophy;
4. Temporal turnover requires the $L^1$ turnover of the pressure-source:
   $$
   f=\operatorname{tr}((\nabla u)^2)
   $$
   which is not controlled by the energy inequality itself;
5. Under the adjoint cutoff, the local mean strain has an exact transport identity;
6. The mean-strain direction rotation is controlled by a matrix nonlinear-turnover debt;
7. The far-pressure direction turnover + mean-strain direction turnover jointly control the parent→child variation of pressure efficiency;
8. Thus, a genuine **Conditional Pressure-Poor Heredity Theorem** is obtained;
9. The mean→pointwise upgrade can be closed by a local Morrey–Poincaré fluctuation bound for $p>3$;
10. The endpoint $p=3$ exactly loses $L^\infty$ oscillation control;
11. For a band-limited strain shell, there is an even more localized eigenvalue-sign persistence;
12. But the shell→full strain transfer still requires remainder smallness;
13. Even if the pointwise middle-strain event is completely closed, a single parabolic event only pays an $O(1)$ critical Miller toll, and infinite Zeno events remain compatible with a hypothetical blow-up;
14. Therefore, what is obtained in this round is a PDE-level conditional interface, not a global contradiction.

---

# 1. Pressure source and Hessian kernel

The whole-space pressure is:

$$
-\Delta p
=
f,
$$

where:

$$
\boxed{
f
=
\operatorname{tr}
((\nabla u)^2).
}
$$

The pressure Hessian is:

$$
\boxed{
H_p(x,t)
=
\nabla^2p(x,t)
=
\int_{\mathbb R^3}
K(x-y)f(y,t)\,dy
}
$$

understood in the sense of principal-value / local-pressure expansion.

Away from:

$$
x=y
$$

, the kernel satisfies:

$$
\boxed{
|\nabla^mK(z)|
\le
C_m|z|^{-3-m}.
}
$$

---

# 2. Parent / child ancestry geometry

Consider a causal parent:

$$
P
=
(x_p,t_p,R_p)
$$

and child:

$$
C
=
(x_c,t_c,R_c),
$$

where:

$$
t_p<t_c.
$$

The eventual local ancestry gives a bounded scale jump:

$$
\boxed{
c_LR_p
\le
R_c
\le
C_LR_p
}
$$

for fixed positive constants.

Usually, forward UV ancestry has:

$$
R_c\le R_p,
$$

but only comparability is needed below.

Define the displacement:

$$
\boxed{
d_{pc}
=
|x_c-x_p|.
}
$$

The phase-space ancestry route expects:

$$
d_{pc}\lesssim R_p.
$$

---

# 3. Smooth far cutoffs

Fix:

$$
\kappa\gg1.
$$

Take the parent far cutoff:

$$
\psi_p(y)
$$

such that:

$$
\psi_p=0
$$

on:

$$
B_{\kappa R_p}(x_p),
$$

and:

$$
\psi_p=1
$$

outside:

$$
B_{2\kappa R_p}(x_p).
$$

Similarly for the child:

$$
\psi_c.
$$

Define:

$$
f_p=f(\cdot,t_p),
\qquad
f_c=f(\cdot,t_c).
$$

and the far matrices:

$$
\boxed{
H_p
=
T_{x_p}(\psi_pf_p),
}
$$

$$
\boxed{
H_c
=
T_{x_c}(\psi_cf_c),
}
$$

where:

$$
T_x(g)
=
\int
K(x-y)g(y)\,dy.
$$

---

# 4. C3-U.1: Exact Pressure-Heredity Decomposition

Introduce two intermediate terms:

$$
T_{x_c}(\psi_pf_c),
$$

$$
T_{x_c}(\psi_pf_p).
$$

Then we have the exact identity:

$$
\boxed{
H_c-H_p
=
\Delta H_{\rm recl}
+
\Delta H_{\rm time}
+
\Delta H_{\rm space},
}
$$

where:

## Reclassification

$$
\boxed{
\Delta H_{\rm recl}
=
T_{x_c}
\left[
(\psi_c-\psi_p)f_c
\right].
}
$$

## Temporal source turnover

$$
\boxed{
\Delta H_{\rm time}
=
T_{x_c}
\left[
\psi_p(f_c-f_p)
\right].
}
$$

## Spatial center shift

$$
\boxed{
\Delta H_{\rm space}
=
T_{x_c}(\psi_pf_p)
-
T_{x_p}(\psi_pf_p).
}
$$

This is an algebraic exact decomposition.

---

# 5. Spatial-shift estimate

Assume:

$$
d_{pc}
\le
c_0R_p,
$$

and:

$$
\kappa\ge4c_0.
$$

Then for:

$$
y\in\operatorname{supp}\psi_p,
$$

$$
|x_p-y|
\gtrsim
\kappa R_p,
$$

and:

$$
|x_c-y|
\gtrsim
\kappa R_p.
$$

the mean value theorem gives:

$$
|K(x_c-y)-K(x_p-y)|
\le
C
d_{pc}
(\kappa R_p)^{-4}.
$$

Therefore:

## Theorem 5.1

$$
\boxed{
|\Delta H_{\rm space}|
\le
C
d_{pc}
(\kappa R_p)^{-4}
\|f_p\|_1.
}
$$

From:

$$
\|f_p\|_1
\le
\|\nabla u(t_p)\|_2^2,
$$

we obtain:

$$
\boxed{
|\Delta H_{\rm space}|
\le
C
d_{pc}
\kappa^{-4}
R_p^{-4}
\|\nabla u(t_p)\|_2^2.
}
$$

---

# 6. Normalized spatial-turnover debt

Define:

$$
\boxed{
\mathfrak E_p
=
\frac{
R_p
\|\nabla u(t_p)\|_2^2
}{
\nu^2
}.
}
$$

and the parent-scale normalized matrix:

$$
\widehat H
=
\frac{
R_p^4
}{
\nu^2
}
H.
$$

Then:

$$
\boxed{
|\Delta\widehat H_{\rm space}|
\le
C
\frac{
d_{pc}
}{
R_p
}
\kappa^{-4}
\mathfrak E_p.
}
$$

Thus if:

$$
d_{pc}=O(R_p),
$$

the spatial center movement only pays:

$$
\boxed{
O(\kappa^{-4}\mathfrak E_p).
}
$$

Compared to the far Hessian amplitude of:

$$
O(\kappa^{-3}\mathfrak E_p)
$$

it has an extra factor of:

$$
\kappa^{-1}.
$$

---

# 7. Reclassification annulus

$\psi_c-\psi_p$ is supported only in the region where the parent/child near–far definitions differ.

Denote:

$$
\boxed{
\mathcal A_{pc}
=
\operatorname{supp}
(\psi_c-\psi_p).
}
$$

Under bounded scale jump, bounded center shift, and sufficiently large $\kappa$,

the distance from this region to the child center is:

$$
\asymp
\kappa R_p
$$

up to fixed constants.

Therefore:

$$
\boxed{
|\Delta H_{\rm recl}|
\le
C
(\kappa R_p)^{-3}
\int_{\mathcal A_{pc}}
|f_c(y)|\,dy.
}
$$

From:

$$
|f_c|
\le
|\nabla u(t_c)|^2,
$$

define:

$$
\boxed{
\mathfrak E_{pc}^{ann}
=
\frac{
R_p
}{
\nu^2
}
\int_{\mathcal A_{pc}}
|\nabla u(y,t_c)|^2dy.
}
$$

we obtain:

## Theorem 7.1

$$
\boxed{
|\Delta\widehat H_{\rm recl}|
\le
C
\kappa^{-3}
\mathfrak E_{pc}^{ann}.
}
$$

---

# 8. Temporal source turnover

For the common parent far classification:

$$
\psi_p,
$$

we have:

$$
\boxed{
|\Delta H_{\rm time}|
\le
C
(\kappa R_p)^{-3}
\|
\psi_p(f_c-f_p)
\|_1.
}
$$

Define the dimensionless temporal pressure-source turnover:

$$
\boxed{
\mathfrak T_{pc}^{far}
=
\frac{
R_p
}{
\nu^2
}
\|
\psi_p(f_c-f_p)
\|_1.
}
$$

Then:

## Theorem 8.1

$$
\boxed{
|\Delta\widehat H_{\rm time}|
\le
C
\kappa^{-3}
\mathfrak T_{pc}^{far}.
}
$$

---

# 9. Temporal turnover can be written as a time-derivative debt

On a smooth window:

$$
f_c-f_p
=
\int_{t_p}^{t_c}
\partial_tf(\cdot,s)\,ds.
$$

Thus:

$$
\boxed{
\mathfrak T_{pc}^{far}
\le
\frac{
R_p
}{
\nu^2
}
\int_{t_p}^{t_c}
\|
\psi_p\partial_tf(s)
\|_1ds
}
$$

plus a cutoff-turnover term if the cutoff itself is also time-dependent.

And:

$$
f
=
\partial_i u_j\partial_j u_i.
$$

schematically:

$$
|\partial_tf|
\lesssim
|\nabla u|
|\nabla\partial_tu|.
$$

Therefore:

$$
\boxed{
\|\partial_tf\|_1
\lesssim
\|\nabla u\|_2
\|\nabla\partial_tu\|_2.
}
$$

The energy inequality itself does not control:

$$
\boxed{
\int
\|\nabla\partial_tu\|_2dt.
}
$$

Therefore, the temporal pressure-source turnover is not an energy-level finite budget.

---

# 10. Pressure-Heredity Debt Theorem

Combining the above:

## Theorem 10.1

In an ancestry step with bounded displacement / bounded scale-jump:

$$
\boxed{
|\Delta\widehat H_{pc}|
\le
C
\left[
\frac{d_{pc}}{R_p}
\kappa^{-4}\mathfrak E_p
+
\kappa^{-3}
\mathfrak E_{pc}^{ann}
+
\kappa^{-3}
\mathfrak T_{pc}^{far}
\right].
}
$$

up to fixed comparability constants.

Therefore, the three true carriers of the parent→child far-pressure matrix variation are:

$$
\boxed{
\text{spatial shift}
+
\text{reclassification}
+
\text{temporal source turnover}.
}
$$

---

# 11. Spatial shift is not the main heredity obstacle

If:

$$
d_{pc}=O(R_p),
$$

and:

$$
\mathfrak E_p
$$

does not grow faster than $\kappa^4$,

the spatial contribution can be suppressed by a large:

$$
\kappa
$$

.

The real difficulties lie in:

$$
\boxed{
\mathfrak E_{pc}^{ann}
}
$$

and:

$$
\boxed{
\mathfrak T_{pc}^{far}.
}
$$

Therefore:

$$
\boxed{
\text{pressure nonlocality}
}
$$

itself is not the complete answer to heredity.

What is truly missing is:

$$
\boxed{
\text{far-source temporal stability}
+
\text{near/far classification stability}.
}
$$

---

# 12. Matrix-direction stability

Let:

$$
H_p\ne0,
\qquad
H_c\ne0.
$$

Define the pressure support directions:

$$
\boxed{
K_p^H
=
-\frac{H_p}{|H_p|},
\qquad
K_c^H
=
-\frac{H_c}{|H_c|}.
}
$$

If:

$$
|H_c-H_p|
\le
\varepsilon_H
|H_p|,
\qquad
0<\varepsilon_H<\frac12,
$$

then an elementary estimate of the normalization map gives:

$$
\boxed{
|K_c^H-K_p^H|
\le
4\varepsilon_H.
}
$$

Therefore, if a nondegenerate far matrix has a relatively small variation, its direction is also stable.

---

# 13. Adjoint mean-strain transport

Now we handle the local mean strain direction.

Take the adjoint cutoff:

$$
\boxed{
\partial_t\chi
+
u\cdot\nabla\chi
+
\nu\Delta\chi
=
0.
}
$$

Define the matrix mean numerator:

$$
\boxed{
M_\chi(t)
=
\int
\chi(x,t)
S(x,t)\,dx.
}
$$

The strain equation is:

$$
\partial_tS
-
\nu\Delta S
+
(u\cdot\nabla)S
+
S^2
+
\frac14\omega\otimes\omega
-
\frac14|\omega|^2I
+
\nabla^2p
=
0.
$$

---

# 14. C3-U.2: Exact Adjoint Mean-Strain Transport Identity

## Theorem 14.1

$$
\boxed{
\frac d{dt}
M_\chi(t)
=
-
\int
\chi
\left[
S^2
+
\frac14\omega\otimes\omega
-
\frac14|\omega|^2I
+
\nabla^2p
\right]dx.
}
$$

### Proof

Compute:

$$
\frac d{dt}
\int\chi S
=
\int
(\partial_t\chi)S
+
\int
\chi\partial_tS.
$$

Substitute the adjoint cutoff and the strain equation.

Diffusion:

$$
-\nu\int(\Delta\chi)S
+
\nu\int\chi\Delta S
=
0
$$

by integration by parts.

Advection:

$$
-\int(u\cdot\nabla\chi)S
-
\int\chi(u\cdot\nabla)S
=
0
$$

since:

$$
\nabla\cdot u=0.
$$

The remainder yields the result. $\square$

---

# 15. Mean-strain turnover debt

Define:

$$
\boxed{
\mathcal R_S
=
S^2
+
\frac14\omega\otimes\omega
-
\frac14|\omega|^2I
+
\nabla^2p.
}
$$

Then:

$$
\boxed{
M_\chi(t_c)-M_\chi(t_p)
=
-
\int_{t_p}^{t_c}
\int
\chi\mathcal R_S
\,dxdt.
}
$$

Thus:

$$
\boxed{
|M_c-M_p|
\le
\int_{t_p}^{t_c}
\int
\chi
\left(
|S|^2
+
C|\omega|^2
+
|\nabla^2p|
\right)
dxdt.
}
$$

---

# 16. Mean-direction stability

If:

$$
M_p\ne0,
$$

and:

$$
|M_c-M_p|
\le
\varepsilon_M|M_p|,
\qquad
\varepsilon_M<\frac12,
$$

define:

$$
v_p=\frac{M_p}{|M_p|},
\qquad
v_c=\frac{M_c}{|M_c|}.
$$

Then:

$$
\boxed{
|v_c-v_p|
\le
4\varepsilon_M.
}
$$

Therefore, mean-strain orientation heredity requires:

$$
\boxed{
\text{small adjoint matrix-turnover relative to }|M_p|.
}
$$

---

# 17. Pressure support efficiency

Define:

$$
\boxed{
\eta_p
=
K_p^H:v_p,
}
$$

$$
\boxed{
\eta_c
=
K_c^H:v_c.
}
$$

Positive common far-pressure support means:

$$
\eta>0.
$$

Pressure-poor means:

$$
\eta
$$

is small.

---

# 18. C3-U.3: Conditional Pressure-Poor Heredity Theorem

## Theorem 18.1

If a parent→child step satisfies:

$$
\eta_p\le\eta_0,
$$

$$
|K_c^H-K_p^H|
\le\delta_H,
$$

$$
|v_c-v_p|
\le\delta_M,
$$

Then:

$$
\boxed{
\eta_c
\le
\eta_0
+
\delta_H
+
\delta_M.
}
$$

### Proof

$$
\eta_c-\eta_p
=
(K_c^H-K_p^H):v_c
+
K_p^H:(v_c-v_p).
$$

By unit norms:

$$
|\eta_c-\eta_p|
\le
|K_c^H-K_p^H|
+
|v_c-v_p|.
$$

$\square$

---

# 19. Quantitative sufficient heredity conditions

Combining §10, §12, and §16:

If:

1. the parent far matrix is nondegenerate:
   $$
   |H_p|\ge h_p>0;
   $$

2. the pressure-matrix turnover satisfies:
   $$
   \frac{
   |H_c-H_p|
   }{
   |H_p|
   }
   \le
   \varepsilon_H;
   $$

3. the adjoint mean-strain turnover satisfies:
   $$
   \frac{
   |M_c-M_p|
   }{
   |M_p|
   }
   \le
   \varepsilon_M;
   $$

Then:

$$
\boxed{
\eta_c
\le
\eta_p
+
4\varepsilon_H
+
4\varepsilon_M.
}
$$

Therefore, pressure-poor heredity is not non-existent;

it has an exact conditional sufficient criterion.

---

# 20. Pressure-Heredity Triad of Debts

What truly needs to be controlled are:

## U-H1 — Far-matrix reclassification debt

$$
\boxed{
\kappa^{-3}
\mathfrak E_{pc}^{ann}.
}
$$

## U-H2 — Far-source temporal turnover debt

$$
\boxed{
\kappa^{-3}
\mathfrak T_{pc}^{far}.
}
$$

## U-H3 — Mean-strain rotation debt

$$
\boxed{
\frac{
1
}{
|M_p|
}
\int_{t_p}^{t_c}
\int
\chi
|\mathcal R_S|
\,dxdt.
}
$$

The spatial center shift is relatively more controllable:

$$
\boxed{
\frac{d_{pc}}{R_p}
\kappa^{-4}
\mathfrak E_p.
}
$$

---

# 21. Energy-only heredity no-go

Global energy controls:

$$
\nu
\int
\|\nabla u\|_2^2dt.
$$

It does not directly control:

- instantaneous annular:
  $$
  \mathfrak E_{pc}^{ann};
  $$
- far pressure-source turnover:
  $$
  \mathfrak T_{pc}^{far};
  $$
- adjoint mean-strain matrix turnover:
  $$
  \int\chi|\mathcal R_S|.
  $$

Therefore:

$$
\boxed{
\text{Pressure-Poor Heredity}
}
$$

cannot be closed by the energy inequality alone.

---

# 22. Bounded-generation heredity criterion

If there exists a fixed:

$$
L<\infty
$$

such that every pressure-poor ancestry node has a descendant within at most:

$$
L
$$

generations,

and along the parent→descendant path:

$$
\sum
(
\delta_H+\delta_M
)
\le
\varepsilon_0,
$$

Then:

$$
\boxed{
\eta_{desc}
\le
\eta_{parent}
+
\varepsilon_0.
}
$$

If the threshold is designed with a margin,

one can preserve the pressure-poor status and extract an infinite bounded-gap poor ray.

This translates the combinatorial heredity criterion of C3-T into a PDE sufficient condition.

---

# 23. Mean-to-pointwise: Morrey–Poincaré route

Now we handle the uniform cone branch.

Take a ball:

$$
B_R=B_R(x_0).
$$

Define the ordinary spatial mean:

$$
\boxed{
\bar S_R
=
\fint_{B_R}
S(x)\,dx.
}
$$

For:

$$
p>3,
$$

Morrey–Poincaré gives:

$$
\boxed{
\|S-\bar S_R\|_{L^\infty(B_{R/2})}
\le
C_p
R^{1-3/p}
\|\nabla S\|_{L^p(B_R)}.
}
$$

---

# 24. C3-U.4: Mean-to-Pointwise Middle-Eigenvalue Theorem

## Theorem 24.1

If:

$$
\boxed{
\lambda_2(\bar S_R)
>
C_p
R^{1-3/p}
\|\nabla S\|_{L^p(B_R)},
}
$$

Then:

$$
\boxed{
\lambda_2(S(x))>0
}
$$

for:

$$
x\in B_{R/2}
$$

holds.

### Proof

Weyl's inequality:

$$
\lambda_2(S(x))
\ge
\lambda_2(\bar S_R)
-
\|S(x)-\bar S_R\|_{\rm op}.
$$

And:

$$
\|\cdot\|_{\rm op}
\le
\|\cdot\|_F.
$$

Substituting the Morrey bound yields the result. $\square$

---

# 25. Negative-sign version

If:

$$
\boxed{
\lambda_2(\bar S_R)
<
-
C_p
R^{1-3/p}
\|\nabla S\|_{L^p(B_R)},
}
$$

Then:

$$
\boxed{
\lambda_2(S(x))<0
}
$$

on:

$$
B_{R/2}.
$$

---

# 26. Scale-invariant oscillation ratio

If:

$$
\bar S_R\ne0,
$$

Define:

$$
\boxed{
\mathfrak O_{p,R}
=
\frac{
C_p
R^{1-3/p}
\|\nabla S\|_{L^p(B_R)}
}{
|\bar S_R|
}.
}
$$

and the normalized middle gap:

$$
\boxed{
\delta_{2,R}
=
\frac{
\lambda_2(\bar S_R)
}{
|\bar S_R|
}.
}
$$

Then:

$$
\boxed{
\mathfrak O_{p,R}
<
\delta_{2,R}
}
$$

guarantees pointwise:

$$
\lambda_2>0.
$$

Under N–S scaling:

$$
\boxed{
\mathfrak O_{p,R}
}
$$

is dimensionless / scale-invariant.

---

# 27. Endpoint barrier

At:

$$
p=3,
$$

$W^{1,3}$ does not embed into:

$$
L^\infty.
$$

Therefore:

$$
\boxed{
R^{1-3/p}
\|\nabla S\|_{L^p}
}
$$

the Morrey pointwise mechanism of:

$$
p=3
$$

exactly fails at:

(handled above)

Thus, mean→pointwise rigidity requires:

- $p>3$ local oscillation;
- or endpoint BMO/logarithmic type information;
- or band-limited structure.

This is a genuine endpoint barrier.

---

# 28. Energy / enstrophy level insufficiency

Energy controls:

$$
\nabla u
$$

in:

$$
L_t^2L_x^2.
$$

While:

$$
\nabla S
$$

is equivalent to:

$$
\nabla^2u.
$$

The mean-to-pointwise theorem requires:

$$
\nabla S\in L_x^p,
\qquad
p>3
$$

at the relevant core/time.

Therefore:

$$
\boxed{
\text{energy/enstrophy budget}
\not\Rightarrow
\text{Morrey fluctuation smallness}.
}
$$

---

# 29. Band-limited shell route

For the strain shell:

$$
S_q
=
\Delta_qS,
$$

we have the Bernstein inequality:

$$
\boxed{
\|\nabla S_q\|_\infty
\le
C
\lambda_q
\|S_q\|_\infty.
}
$$

Let:

$$
R=\lambda_q^{-1}.
$$

Assume at some point:

$$
x_0
$$

we have:

$$
\boxed{
\lambda_2(S_q(x_0))
\ge
\delta
\|S_q\|_\infty
}
$$

for:

$$
\delta>0.
$$

---

# 30. C3-U.5: Band-Limited Middle-Eigenvalue Persistence

## Theorem 30.1

There exists a universal:

$$
c>0
$$

such that when:

$$
\boxed{
|x-x_0|
\le
c\delta R
}
$$

:

$$
\boxed{
\lambda_2(S_q(x))
\ge
\frac{\delta}{2}
\|S_q\|_\infty.
}
$$

### Proof

Bernstein gives:

$$
\|S_q(x)-S_q(x_0)\|
\le
C
\lambda_q
\|S_q\|_\infty
|x-x_0|.
$$

Take:

$$
|x-x_0|
\le
\frac{\delta}{2C}\lambda_q^{-1}.
$$

Then apply Weyl's inequality. $\square$

---

# 31. Shell-to-full pointwise transfer

Let the remainder be:

$$
\boxed{
R_q^S
=
S-S_q.
}
$$

If in the above subcore:

$$
\boxed{
\|R_q^S\|_{L^\infty,op}
\le
\frac{\delta}{4}
\|S_q\|_\infty,
}
$$

Then:

$$
\boxed{
\lambda_2(S(x))
\ge
\frac{\delta}{4}
\|S_q\|_\infty
>0.
}
$$

Therefore, the two proof obligations for the band-limited route are:

1. shell eigenvalue-gap anchor;
2. full-strain remainder smallness.

---

# 32. Frontier velocity crossing does not automatically give a strain anchor

The C3-G first crossing controls:

$$
\|u_q\|_\infty
\sim
\nu\lambda_q.
$$

But this does not imply:

$$
\boxed{
\|S_q\|_\infty
\gtrsim
\nu\lambda_q^2
}
$$

at the same point or in the same core.

The velocity near its maximum might even have a smaller gradient.

Therefore:

$$
\boxed{
\text{velocity frontier core}
}
$$

cannot automatically be upgraded to:

$$
\boxed{
\text{strain eigenvalue core}.
}
$$

This is another type gap.

---

# 33. Operator-active core might be more suitable for a strain anchor

The Miller operator core is selected by the local ratio of:

$$
\mathcal Q_{SV}
$$

and:

$$
\Delta S
$$

It is naturally closer to strain derivatives,

but:

$$
\boxed{
\|\Delta S\|_2\text{ large}
}
$$

still does not imply:

$$
\boxed{
\lambda_2(S)\text{ positive}.
}
$$

Therefore, operator selection and middle-eigenvalue geometry still require additional matrix-sign information.

---

# 34. If the pointwise positive-middle event is successfully closed

For a scaling audit, temporarily take:

$$
\nu=1.
$$

Assume on the parabolic event:

$$
B_{cR}(x_n)
\times
[t_n-cR^2,t_n]
$$

we have:

$$
\boxed{
\lambda_2^+(S)
\ge
c_0R^{-2}.
}
$$

Then at each time:

$$
\|\lambda_2^+\|_{L^3(B_{cR})}
\ge
cR^{-1}.
$$

Therefore:

$$
\boxed{
\int_{t_n-cR^2}^{t_n}
\|\lambda_2^+(t)\|_3^2dt
\ge
c_1>0.
}
$$

---

# 35. C3-U.6: Parabolic Middle-Strain Toll

Every coherent positive-middle event with amplitude:

$$
R^{-2}
$$

, volume:

$$
R^3
$$

, and duration:

$$
R^2
$$

pays an:

$$
\boxed{
O(1)
}
$$

scale-critical:

$$
L_t^2L_x^3
$$

toll.

Therefore, infinitely many disjoint such events imply:

$$
\boxed{
\int
\|\lambda_2^+\|_3^2dt
=
\infty.
}
$$

This is exactly compatible with the Miller blow-up necessity.

---

# 36. Pointwise closure still does not form a contradiction

Thus, even if the mean-to-pointwise route is completely successful,

it can at most realize:

$$
\boxed{
\text{known necessary }\lambda_2^+\text{ critical divergence}.
}
$$

Infinite parabolic Zeno events each pay a fixed critical toll,

summing to divergence,

which is exactly the scenario allowed by a hypothetical blow-up.

Therefore:

$$
\boxed{
\text{pointwise middle-strain rigidity}
\neq
\text{regularity proof}.
}
$$

Another finite budget / incompatible geometry is still needed.

---

# 37. Pressure-Poor Heredity Status of C3-U

Now pressure-poor heredity is no longer a vague OPEN.

It is compressed into:

$$
\boxed{
\text{Heredity holds conditionally if}
}
$$

the following three turnovers remain small:

1. far source reclassification;
2. far source temporal change;
3. local mean strain rotation.

Among them, the spatial center drift already has a stronger:

$$
\kappa^{-4}
$$

control.

Therefore, the true next step can directly target:

$$
\boxed{
\mathfrak E_{pc}^{ann},
\quad
\mathfrak T_{pc}^{far},
\quad
\mathfrak R_{S,pc}
}
$$

these three quantities.

---

# 38. Mean-to-Pointwise Status of C3-U

Mean→pointwise is also no longer just a conceptual gap.

There are two rigorous sufficient routes:

## Route U-M1 — Morrey

$$
p>3,
$$

$$
\lambda_2(\bar S_R)
>
C
R^{1-3/p}
\|\nabla S\|_p.
$$

## Route U-M2 — Band-limited

shell eigen-gap anchor:

$$
\lambda_2(S_q(x_0))
\ge
\delta\|S_q\|_\infty
$$

+

full remainder small.

Therefore, what is truly missing is not the algebra.

But rather:

$$
\boxed{
\text{Can the known constraints of singular ancestry force one of the sufficient routes to hold?}
}
$$

Currently OPEN.

---

# 39. Major no-go

### NG-U1

$$
\text{bounded spatial ancestry displacement}
\Rightarrow
\text{pressure-poor heredity}.
$$

FALSE; there are also temporal/reclassification/strain-rotation debts.

### NG-U2

$$
\text{far pressure harmonic}
\Rightarrow
\text{far matrix direction time-stable}.
$$

FALSE without source-turnover control.

### NG-U3

$$
\text{energy inequality}
\Rightarrow
\mathfrak T_{pc}^{far}\text{ finite/small per event}.
$$

NOT PROVED.

### NG-U4

$$
\text{mean-strain narrow cone}
\Rightarrow
\text{pointwise }\lambda_2\text{ sign}.
$$

FALSE without fluctuation control.

### NG-U5

$$
W^{1,3}\text{ local control}
\Rightarrow
L^\infty\text{ oscillation control}.
$$

FALSE at endpoint.

### NG-U6

$$
\text{velocity shell critical amplitude}
\Rightarrow
\text{strain shell eigen-gap anchor}.
$$

FALSE / not established.

### NG-U7

$$
\text{pointwise middle-strain event}
\Rightarrow
\text{contradiction}.
$$

FALSE; it realizes known critical blow-up toll.

---

# 40. X-Integration guards update

## G-PHD

Pressure Heredity Decomposition:

$$
\Delta H
=
\Delta H_{\rm recl}
+
\Delta H_{\rm time}
+
\Delta H_{\rm space}.
$$

## G-ANN

Preserve reclassification annulus:

$$
\mathfrak E_{pc}^{ann}.
$$

## G-PTURN

Preserve far pressure-source turnover:

$$
\mathfrak T_{pc}^{far}.
$$

## G-MTURN

Preserve adjoint mean-strain matrix turnover.

## G-HDIR

Stable direction must not be discussed when the far matrix magnitude is close to zero.

## G-MORREY

If Morrey is used for mean→pointwise, it must be:

$$
p>3.
$$

## G-ENDPOINT

$p=3$ cannot silently use the $L^\infty$ Morrey embedding.

## G-SHELLGAP

The band-limited route must preserve the shell eigenvalue gap.

## G-SHELLREM

The shell pointwise sign must not ignore the full-strain remainder.

---

# 41. True ETN update

Pressure heredity state:

$$
\boxed{
\Theta_{pc}^{press}
=
\left\langle
H_p,H_c,
\Delta H_{\rm space},
\mathfrak E_{pc}^{ann},
\mathfrak T_{pc}^{far},
K_p^H,K_c^H
\right\rangle.
}
$$

Mean-strain transport state:

$$
\boxed{
\Theta_{pc}^{mean}
=
\left\langle
M_p,M_c,
\int\chi\mathcal R_S,
v_p,v_c
\right\rangle.
}
$$

Pointwise upgrade state:

$$
\boxed{
\Theta_R^{pt}
=
\left\langle
\bar S_R,
\delta_{2,R},
\mathfrak O_{p,R},
S_q,
R_q^S
\right\rangle.
}
$$

Pressure-poor heredity becomes:

$$
\boxed{
\text{small pressure-direction turnover}
+
\text{small mean-strain-direction turnover}.
}
$$

---

# 42. New frontier: C3-V

C3-U has already turned the two transfer gaps into computable debts.

The formal next problem is:

$$
\boxed{
\textbf{C3-V — Turnover Packing and Strain-Fluctuation Escape}.
}
$$

---

# 43. C3-V proof obligations

## V1 — Temporal pressure-turnover packing

Investigate whether:

$$
\mathfrak T_{pc}^{far}
$$

can have a finite global budget along infinitely many viscous ancestry windows.

If not, formalize its critical moment scaling.

## V2 — Reclassification-annulus packing

Investigate whether:

$$
\sum_n
\mathfrak E_{p_nc_n}^{ann}
$$

is constrained by:

- active-worldvolume;
- shell occupancy;
- enstrophy;

## V3 — Mean-strain rotation packing

From:

$$
M'
=
-\int\chi\mathcal R_S
$$

investigate across infinite generations:

$$
\sum_n
|v_{n+1}-v_n|.
$$

If finite, obtain matrix-direction convergence.

## V4 — Heredity closure

If V1–V3 can be controlled,

apply the C3-U Conditional Pressure-Poor Heredity,

to extract a pressure-poor ancestry ray.

## V5 — Morrey fluctuation branch

Investigate whether, if:

$$
\mathfrak O_{p,R}
$$

is not small,

it forces a higher-moment escape for:

$$
\nabla S
$$

## V6 — Band-limited strain anchor

Search for operator-active / helical ancestry conditions,

to see if they force a certain shell:

$$
\lambda_2(S_q)
$$

to have a nontrivial eigen-gap.

## V7 — Remainder trichotomy

If the shell eigen-gap exists but the full pointwise sign fails,

then the remainder:

$$
R_q^S
$$

must be of the same order as the shell.

Divide the remainder into:

- IR;
- UV;
- spatial;
- pressure/projection.

## V8 — Critical toll compatibility

Any pointwise closure must correctly align with the Miller:

$$
L_t^2L_x^3
$$

divergence,

forbidding the misidentification of a necessary divergence as a contradiction.

---

# 44. Formal status

$$
\boxed{
\begin{aligned}
\text{pressure heredity exact decomposition}
&:\ \mathrm{PROVED},\\
\text{spatial far-matrix variation }\sim\kappa^{-4}
&:\ \mathrm{PROVED},\\
\text{reclassification bound by annular enstrophy}
&:\ \mathrm{PROVED},\\
\text{temporal far-source turnover bound}
&:\ \mathrm{PROVED},\\
\text{energy controls temporal turnover}
&:\ \mathrm{NOT\ PROVED},\\
\text{adjoint mean-strain transport identity}
&:\ \mathrm{PROVED},\\
\text{conditional pressure-poor heredity}
&:\ \mathrm{PROVED},\\
\text{unconditional pressure-poor heredity}
&:\ \mathrm{OPEN},\\
\text{Morrey mean-to-pointwise theorem }p>3
&:\ \mathrm{PROVED/STANDARD},\\
\text{endpoint }p=3\text{ mean-to-pointwise}
&:\ \mathrm{NO\mbox{-}GO\ by\ Morrey},\\
\text{band-limited eigenvalue persistence}
&:\ \mathrm{PROVED},\\
\text{shell-to-full transfer under remainder smallness}
&:\ \mathrm{PROVED\ CONDITIONAL},\\
\text{frontier velocity}\Rightarrow\text{strain eigen-gap}
&:\ \mathrm{NOT\ PROVED},\\
\text{parabolic middle-strain event has fixed critical toll}
&:\ \mathrm{PROVED/SCALING},\\
\text{pointwise closure}\Rightarrow\text{regularity}
&:\ \mathrm{FALSE/NO\mbox{-}GO},\\
\text{turnover-packing/fluctuation rigidity}
&:\ \mathrm{OPEN}.
\end{aligned}
}
$$

---

# 45. Conclusion

C3-T left two propagation problems.

C3-U now decomposes pressure heredity into the exact:

$$
\boxed{
\Delta H
=
\Delta H_{\rm space}
+
\Delta H_{\rm recl}
+
\Delta H_{\rm time}.
}
$$

where:

$$
\boxed{
|\Delta\widehat H_{\rm space}|
\lesssim
\frac dR
\kappa^{-4}
\mathfrak E_R,
}
$$

so the bounded ancestry displacement itself is relatively controllable.

The true pressure-heredity gaps are:

$$
\boxed{
\kappa^{-3}
\mathfrak E_{pc}^{ann}
}
$$

and:

$$
\boxed{
\kappa^{-3}
\mathfrak T_{pc}^{far}.
}
$$

Meanwhile, the adjoint cutoff gives the local mean strain an exact transport:

$$
\boxed{
M_\chi'
=
-
\int
\chi
\left[
S^2
+
\frac14\omega\otimes\omega
-
\frac14|\omega|^2I
+
\nabla^2p
\right].
}
$$

Therefore, the mean-strain direction rotation is also an explicit matrix-turnover debt.

As long as both the far-matrix direction and the mean-strain direction are stable,

the pressure-poor property can be propagated from parent→child.

Thus, heredity is now a:

$$
\boxed{
\textbf{conditional theorem},
}
$$

not a pure black-box OPEN.

The same applies to the mean→pointwise side:

$$
\boxed{
\lambda_2(\bar S_R)
>
C
R^{1-3/p}
\|\nabla S\|_{L^p},
\quad p>3
}
$$

is sufficient to obtain:

$$
\boxed{
\lambda_2(S(x))>0
}
$$

in the inner core.

Alternatively, use the band-limited shell eigen-gap + remainder smallness.

Therefore, what is truly unclosed is no longer 'whether it can be upgraded'.

But rather:

> Can the known budgets of singular ancestry force the pressure turnover to be small, the mean rotation to be small, or the strain fluctuation to be small?

Next round:

$$
\boxed{
\textbf{C3-V — Turnover Packing and Strain-Fluctuation Escape}.
}
$$

---

# References

1. E. Miller, *A regularity criterion for the Navier–Stokes equation involving only the middle eigenvalue of the strain tensor*, arXiv:1710.05569; Arch. Rational Mech. Anal. 235 (2020).
2. E. Miller, *On the interaction of strain and vorticity for solutions of the Navier–Stokes equation*, arXiv:2407.02691; Pure and Applied Analysis 8 (2026).
3. Z. Bradshaw, T.-P. Tsai, *On the local pressure expansion for the Navier–Stokes equations*, arXiv:2001.11526.
4. T. Barker, C. Prange, *Localized smoothing for the Navier–Stokes equations and concentration of critical norms near singularities*, arXiv:1812.09115.
5. A. Cheskidov, M. Dai, *Regularity criteria for the 3D Navier–Stokes and MHD equations*, arXiv:1507.06611.

# Internal dependencies

- `NS_C3T_PressureDiversification_ConeEigenvalue_HeredityGap_v0.1.md`
- `NS_C3S_StrainConeMargin_MergerRigidity_v0.1.md`
- `NS_C3R_MultiCore_PressureHorizon_StrainConvexity_v0.1.md`
- `NS_C3Q_PressureProjection_OperatorLocalization_v0.1.md`
- `NS_C3P_OperatorEscape_FarPressureMatrix_v0.1.md`
- `NS_C3O_AdjointCore_BalanceDynamicsSeparation_v0.1.md`
- `NS_C3L_CriticalMomentEscape_StrainGeometryDebt_v0.1.md`
- `NS_C3G_FirstCrossing_CausalAncestry_DepletionNoGo_v0.1.md`
- `True ETN / Infinite-dimensional tension field`
- `X_Integral_Unified_Program_v0.2.md`

Next:

$$
\boxed{
\textbf{C3-V — Turnover Packing and Strain-Fluctuation Escape}
}
$$