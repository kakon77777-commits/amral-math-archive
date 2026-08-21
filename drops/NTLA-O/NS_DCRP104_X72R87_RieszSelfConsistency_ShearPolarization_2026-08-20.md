# DCRP104 / X72-R87 — Riesz Self-Consistency of Adjoint Rays, Frozen Coaxial L2 NO-GO, and Shear/Axisymmetric Polarization Survivors

**Series:** Independent Navier–Stokes Research Series / X72 Bridge  
**Date:** 2026-08-20  
**Status:** proof-development checkpoint / nonlocal Riesz self-consistency round  
**Immediate predecessor:** `NS_DCRP103_X72R86_AdjointEigenLock_FiveRayClassification_2026-08-20.md`

## Primary internal dependencies

- DCRP102 — backward-adjoint eigen-lock:
  \[
  -\nu\Delta\Phi+L_S(\Phi)+2S\mathcal T_0^*\Phi=\beta\Phi.
  \]
- DCRP103 — local five-ray classification:
  three simple-strain shear families, two coaxial rays, and an axisymmetric degeneracy block.
- X72 Round37/38 — pressure/Riesz operator normalization.

## Fresh primary-source calibration

- P. Constantin, M. Ignatova, V. Vicol, *On putative self-similarity for incompressible 3D Euler*, arXiv:2602.17570v3 (2026).
- R. Yu, *Filtered Vortex Stretching and Subgrid Defects for the Three-Dimensional Navier-Stokes Equations*, arXiv:2606.27560 (2026).
- E. Hess-Childs, M. Rosenzweig, S. Serfaty, *Another look at regularity in transport-commutator estimates*, arXiv:2601.02326 (2026).
- B. Álvarez-Samaniego, W. P. Álvarez-Samaniego, P. G. Fernández-Dalgo, *On the use of the Riesz transforms to determine the pressure term in the incompressible Navier-Stokes equations on the whole space*, arXiv:2004.02588.

The whole-space Riesz-pressure reference is used only to calibrate the standard Fourier/Riesz normalization.  
No full Navier–Stokes regularity theorem is claimed.

---

# 0. Executive result

DCRP103 reduced the local inviscid adjoint eigen-lock to:

\[
\boxed{
\mathsf K_{\rm coax}
\vee
\mathsf K_{\rm sh}^{12}
\vee
\mathsf K_{\rm sh}^{13}
\vee
\mathsf K_{\rm sh}^{23}
\vee
\mathsf K_{\rm axi}.
}
\]

DCRP104 imposes the nonlocal self-consistency:

\[
\boxed{
r=\mathcal T_0^*\Phi.
}
\]

For the X72 normalization

\[
\mathcal T_0
=
\nabla^2(-\Delta)^{-1}
+\frac13 I,
\]

the Fourier tensor symbol is

\[
\boxed{
M(n)
=
\frac13I-n\otimes n,
\qquad
n=\frac{\xi}{|\xi|}.
}
\]

Thus, for trace-free \(\Phi\),

\[
\boxed{
\widehat{\mathcal T_0^*\Phi}(\xi)
=
M(n):\widehat\Phi(\xi)
=
-n^\top\widehat\Phi(\xi)n.
}
\tag{0.1}
\]

The three D103 ray types behave very differently.

---

## Main result A — simple coaxial frozen \(L^2\) branch is impossible

For frozen simple strain and constant \(\beta\), the Riesz-loaded coaxial branch has:

\[
\Phi=A r,
\]

where \(A\in\mathrm{Sym}_0(3)\) is constant.

Self-consistency gives:

\[
\boxed{
[1-a(n)]\widehat r(\xi)=0,
\qquad
a(n):=M(n):A=-n^\top A n.
}
\tag{0.2}
\]

Hence Fourier support lies in:

\[
\boxed{
\Sigma_A
=
\{n\in S^2:a(n)=1\}.
}
\tag{0.3}
\]

Because \(A\) is trace-free, \(a(n)\equiv1\) on no open subset of \(S^2\).  
Indeed, if:

\[
-n^\top A n=1
\]

on an open sphere patch, real-analytic continuation gives:

\[
n^\top A n=-1
\]

for every \(n\), hence:

\[
A=-I,
\]

contradicting:

\[
\operatorname{tr}A=0.
\]

Therefore \(\Sigma_A\) has surface measure zero.

Its cone in \(\mathbb R^3\) also has Lebesgue measure zero.

If:

\[
r\in L^2(\mathbb R^3),
\]

then:

\[
\widehat r
\]

cannot be supported on this null set unless:

\[
r=0.
\]

Thus:

\[
\Phi=0.
\]

The pure \(r=0\) coaxial eigenrays are also killed: if

\[
\Phi=fH
\]

with fixed nonzero trace-free \(H\), then:

\[
0=\mathcal T_0^*\Phi
\]

forces:

\[
[n^\top Hn]\widehat f=0.
\]

The zero set of the nonzero quadratic form is again measure zero.

Hence:

## Theorem D104.1 — Frozen Coaxial \(L^2\) NO-GO

\[
\boxed{
\mathsf K_{\rm coax}^{\rm frozen}
\cap
L^2(\mathbb R^3)
=
\{0\}.
}
\tag{0.4}
\]

This removes one entire D103 node in the frozen whole-space \(L^2\) model.

---

## Main result B — simple single-shear branch survives

For one D103 shear family:

\[
\Phi
=
qH_{ij}
+
A_{ij,k}r,
\]

where:

\[
H_{ij}
=
e_i\otimes e_j+e_j\otimes e_i,
\]

and \(k\) is the complementary index.

Define:

\[
h_{ij}(n)
=
M(n):H_{ij}
=
-2n_i n_j,
\]

\[
a_{ij,k}(n)
=
M(n):A_{ij,k}.
\]

Then self-consistency is:

\[
\boxed{
[1-a_{ij,k}(n)]
\widehat r
=
h_{ij}(n)\widehat q.
}
\tag{0.5}
\]

Away from the resonance set:

\[
\Sigma_{ij,k}
=
\{n:1-a_{ij,k}(n)=0\},
\]

one has the exact order-zero multiplier:

\[
\boxed{
\widehat r
=
\frac{
h_{ij}(n)
}{
1-a_{ij,k}(n)
}
\widehat q.
}
\tag{0.6}
\]

Therefore, if \(\widehat q\) is any nonzero \(L^2\) function supported in an angular patch where:

\[
|1-a_{ij,k}(n)|\ge\delta>0,
\]

then:

\[
r\in L^2,
\]

and:

\[
\boxed{
\widehat\Phi
=
\left[
H_{ij}
+
A_{ij,k}
\frac{
h_{ij}(n)
}{
1-a_{ij,k}(n)
}
\right]
\widehat q
}
\tag{0.7}
\]

is a nonzero exact frozen Riesz-self-consistent adjoint eigen-lock.

Thus:

## Theorem D104.2 — Frozen Simple-Shear Survival

\[
\boxed{
\mathsf K_{\rm sh}^{ij}
\cap
L^2(\mathbb R^3)
\neq
\{0\}
}
\]

in the frozen inviscid self-consistency problem.

The simple shear branch does **not** require Fourier mass to live on the Riesz resonance cone.

It can live on an ordinary open frequency sector away from resonance.

---

## Main result C — axisymmetric degeneracy has an even larger polarization kernel

Let:

\[
S
=
a\,\operatorname{diag}(1,1,-2),
\qquad
a\neq0.
\]

The D103 cross-plane eigenspace has:

\[
\beta=-a,
\]

and basis:

\[
H_{13},H_{23}.
\]

For every Fourier direction \(n\), define:

\[
\boxed{
P_\times(n)
=
-n_2H_{13}
+
n_1H_{23}.
}
\tag{0.8}
\]

Then:

\[
M(n):H_{13}
=
-2n_1n_3,
\]

\[
M(n):H_{23}
=
-2n_2n_3,
\]

so:

\[
\boxed{
M(n):P_\times(n)=0.
}
\tag{0.9}
\]

Hence for any scalar:

\[
\chi(\xi)\in L^2,
\]

the field:

\[
\boxed{
\widehat\Phi(\xi)
=
P_\times(\widehat\xi)\chi(\xi)
}
\tag{0.10}
\]

satisfies:

\[
r=\mathcal T_0^*\Phi=0,
\]

while:

\[
L_S\Phi=-a\Phi.
\]

Thus:

## Theorem D104.3 — Axisymmetric Polarization Survivor

\[
\boxed{
\mathsf K_{\rm axi}^{\rm frozen}
\cap
L^2(\mathbb R^3)
}
\]

contains an infinite-dimensional nontrivial polarization kernel.

So axisymmetric degeneracy is structurally more flexible than the simple-strain one-ray branch.

---

# 1. Fourier symbol of \(\mathcal T_0\)

Use:

\[
\widehat{\partial_i\partial_j(-\Delta)^{-1}f}
=
-\frac{\xi_i\xi_j}{|\xi|^2}\widehat f.
\]

Hence:

\[
\widehat{\mathcal T_0f}
=
\left(
\frac13I
-
n\otimes n
\right)
\widehat f.
\]

Since \(M(n)\) is symmetric,

\[
\boxed{
\widehat{\mathcal T_0^*\Phi}
=
M(n):\widehat\Phi.
}
\tag{1.1}
\]

If \(\operatorname{tr}\Phi=0\),

\[
M(n):\Phi
=
-n^\top\Phi n.
\]

---

# 2. Coaxial loaded branch

D103 gives:

\[
\Phi
=
\frac{
2r
}{
\beta^2-d_S^2
}
(\beta S+2C_S^0).
\]

Define the constant trace-free tensor:

\[
\boxed{
A
=
\frac{
2
}{
\beta^2-d_S^2
}
(\beta S+2C_S^0).
}
\tag{2.1}
\]

Then:

\[
\Phi=Ar.
\]

Self-consistency is:

\[
r=\mathcal T_0^*(Ar).
\]

Fourier transforming:

\[
\widehat r
=
[M(n):A]\widehat r.
\]

So:

\[
\boxed{
[1+ n^\top A n]\widehat r=0.
}
\tag{2.2}
\]

The characteristic cone is:

\[
\boxed{
\Sigma_A
=
\{
\xi\neq0:
1+n^\top A n=0
\}.
}
\tag{2.3}
\]

For trace-free \(A\), this is either empty or a lower-dimensional real-algebraic cone.

It cannot contain a three-dimensional frequency open set.

This proves D104.1.

---

# 3. Pure coaxial \(r=0\) branch

At:

\[
\beta=\pm d_S,
\]

D103 forces:

\[
r=0,
\]

and:

\[
\Phi=f\Phi_\pm.
\]

Then:

\[
0
=
\widehat r
=
-[n^\top\Phi_\pm n]\widehat f.
\]

Since:

\[
\Phi_\pm\neq0,
\]

the quadratic form:

\[
n^\top\Phi_\pm n
\]

does not vanish identically.

Its zero cone has measure zero.

Thus:

\[
\boxed{
f\in L^2
\Longrightarrow
f=0.
}
\tag{3.1}
\]

So both loaded and unloaded frozen simple coaxial branches are eliminated in \(L^2\).

---

# 4. Explicit simple-shear coefficient tensor

Let the active shear pair be:

\[
(i,j),
\]

and let \(k\) be the complementary index.

Write:

\[
\Delta_{ij}
=
s_i-s_j
\neq0.
\]

D103 gives:

\[
\beta=-s_k,
\]

and:

\[
A_{ij,k}
=
\frac{
2
}{
s_k^2-d_S^2
}
(-s_kS+2C_S^0).
\]

Using:

\[
s_k^2-d_S^2
=
-\frac13(s_i-s_j)^2,
\]

one obtains, in the ordered eigenbasis \((i,j,k)\):

## Theorem D104.4 — Explicit shear loading tensor

\[
\boxed{
A_{ij,k}
=
\operatorname{diag}
\left(
9\frac{s_k}{\Delta_{ij}}-1,\,
-9\frac{s_k}{\Delta_{ij}}-1,\,
2
\right).
}
\tag{4.1}
\]

It is trace-free.

Therefore:

\[
a_{ij,k}(n)
=
-n^\top A_{ij,k}n
\]

and:

\[
\boxed{
1-a_{ij,k}(n)
=
3
\left[
n_k^2
+
3
\frac{s_k}{s_i-s_j}
(n_i^2-n_j^2)
\right].
}
\tag{4.2}
\]

The Riesz resonance cone is:

\[
\boxed{
\Sigma_{ij,k}
=
\left\{
n:
n_k^2
+
3
\frac{s_k}{s_i-s_j}
(n_i^2-n_j^2)
=0
\right\}.
}
\tag{4.3}
\]

The shear numerator is:

\[
\boxed{
h_{ij}(n)=-2n_in_j.
}
\tag{4.4}
\]

---

# 5. Concrete surviving simple-shear example

Take:

\[
\boxed{
S=\operatorname{diag}(1,0,-1).
}
\tag{5.1}
\]

Choose the shear pair:

\[
(i,j)=(1,3),
\qquad
k=2.
\]

Then:

\[
\beta=-s_2=0.
\]

D103 gives:

\[
\boxed{
A_{13,2}
=
\operatorname{diag}(-1,2,-1).
}
\tag{5.2}
\]

Hence:

\[
a(n)
=
1-3n_2^2,
\]

so:

\[
\boxed{
1-a(n)=3n_2^2.
}
\tag{5.3}
\]

Also:

\[
\boxed{
h_{13}(n)
=
-2n_1n_3.
}
\tag{5.4}
\]

Therefore:

\[
\boxed{
\widehat r
=
-\frac{
2n_1n_3
}{
3n_2^2
}
\widehat q.
}
\tag{5.5}
\]

Choose \(\widehat q\) supported in a small conical patch around:

\[
n_*=\frac1{\sqrt3}(1,1,1).
\]

There:

\[
1-a(n_*)=1,
\]

and:

\[
h_{13}(n_*)=-\frac23.
\]

The multiplier is smooth and bounded in a sufficiently small patch.

Thus any nonzero compactly supported \(L^2\) Fourier amplitude in that patch produces a nonzero exact frozen self-consistent shear-ray field.

This is an explicit whole-space \(L^2\) survivor of the Riesz self-consistency equation.

---

# 6. Meaning of the simple-shear resonance cone

The set:

\[
\Sigma_{ij,k}
\]

is **not** the support of every surviving shear field.

Rather, it is the singular set of the scalar transfer multiplier:

\[
\frac{h_{ij}}{1-a_{ij,k}}.
\]

Thus the shear branch splits into:

## off-resonance regular multiplier

\[
\boxed{
\operatorname{dist}
(
\operatorname{supp}\widehat q,
\Sigma_{ij,k}
)
>0;
}
\]

## near-resonance concentration

\[
\boxed{
\operatorname{dist}
(
\operatorname{supp}\widehat q,
\Sigma_{ij,k}
)
\to0.
}
\]

Only the second branch naturally suggests a scale/frequency concentration defect.

The first is a genuine ordinary order-zero Fourier survivor.

This corrects the initial expectation that every nonzero ray would have to live on a measure-zero Riesz resonance manifold.

---

# 7. Axisymmetric cross-plane polarization

For:

\[
S=a\operatorname{diag}(1,1,-2),
\]

the cross-plane block is:

\[
\operatorname{span}\{H_{13},H_{23}\},
\]

with eigenvalue:

\[
\beta=-a.
\]

Let:

\[
\widehat\Phi
=
q_1H_{13}+q_2H_{23}.
\]

Then:

\[
\widehat r
=
-2n_3
(n_1q_1+n_2q_2).
\]

Choose:

\[
\boxed{
q_1=-n_2\chi,
\qquad
q_2=n_1\chi.
}
\tag{7.1}
\]

Then:

\[
\boxed{
\widehat r=0.
}
\tag{7.2}
\]

Any:

\[
\chi\in L^2
\]

gives a nonzero self-consistent axisymmetric eigen-lock.

No measure-zero support is needed.

This is a genuine polarization kernel.

---

# 8. Axisymmetric planar polarization

The axisymmetric planar trace-free block has eigenvalue:

\[
\beta=2a
\]

and basis:

\[
D
=
\operatorname{diag}(1,-1,0),
\]

\[
H_{12}.
\]

For:

\[
\widehat\Phi
=
q_DD+q_HH_{12},
\]

one has:

\[
\widehat r
=
-(n_1^2-n_2^2)q_D
-
2n_1n_2q_H.
\]

Choose:

\[
\boxed{
q_D
=
-2n_1n_2\chi,
}
\]

\[
\boxed{
q_H
=
(n_1^2-n_2^2)\chi.
}
\tag{8.1}
\]

Then:

\[
\boxed{
\widehat r=0.
}
\tag{8.2}
\]

Thus the planar two-dimensional eigenspace also carries a nontrivial \(L^2\) polarization kernel.

The axisymmetric node is therefore highly non-rigid under \(\mathcal T_0^*\) alone.

---

# 9. Frozen viscous sidecar

Return to the full constant-coefficient eigen-lock:

\[
-\nu\Delta\Phi
+
L_S(\Phi)
+
2S\mathcal T_0^*\Phi
=
\beta\Phi,
\qquad
\nu>0.
\]

Fourier transforming gives:

\[
\boxed{
\mathscr M_\nu(\xi)\widehat\Phi(\xi)=0,
}
\tag{9.1}
\]

where:

\[
\mathscr M_\nu(\xi)
=
\nu|\xi|^2I_5
+
L_S
+
2S\otimes M(n)
-
\beta I_5.
\]

Its determinant is real analytic for:

\[
\xi\neq0.
\]

As:

\[
|\xi|\to\infty,
\]

\[
\det\mathscr M_\nu(\xi)
\sim
(\nu|\xi|^2)^5.
\]

Therefore the determinant is not identically zero.

Its zero set has three-dimensional Lebesgue measure zero.

Thus:

## Theorem D104.5 — Frozen Viscous \(L^2\) Eigen-Lock NO-GO

For:

- constant \(S\);
- constant \(\beta\);
- \(\nu>0\);

the exact whole-space \(L^2\) eigen-lock satisfies:

\[
\boxed{
\Phi=0.
}
\tag{9.2}
\]

This is a useful prelimit sidecar.

It does not eliminate the inviscid \(\nu\to0\) survivor.

---

# 10. Variable-coefficient scope

The actual strict DSS branch is not globally frozen.

For variable:

\[
S(x,s),
\qquad
\beta(x,s),
\qquad
\text{eigenframe}(x,s),
\]

the Fourier diagonalization above is not an exact global theorem.

In particular, the coaxial equation becomes a variable-coefficient singular-integral fixed point of schematic form:

\[
\boxed{
r
=
\mathcal T_0^*
[
A(x,s)r
].
}
\tag{10.1}
\]

The relevant principal symbol is:

\[
\boxed{
p(x,n)
=
1-M(n):A(x).
}
\tag{10.2}
\]

If the coefficient/eigenframe varies strongly, the freezing error itself is a gradient/state/commutator coordinate.

D104 therefore does **not** promote the frozen coaxial \(L^2\) NO-GO to an unconditional variable-coefficient theorem.

The legitimate conclusion is:

\[
\boxed{
\text{variable coaxial survivor}
\Longrightarrow
\text{microlocal resonance}
\vee
\text{coefficient/eigenframe modulation}.
}
\tag{10.3}
\]

This remains a next-step target.

---

# 11. Relation to Morrey / non-\(L^2\) strict DSS tails

The D104 coaxial NO-GO uses:

\[
L^2(\mathbb R^3).
\]

Strict Type-II profile control in the wider project may only give critical Morrey-type growth rather than global \(L^2\).

Therefore a nonzero coaxial profile may evade D104.1 by being:

- non-\(L^2\);
- tail-fed;
- distributional;
- local rather than whole-space.

These are not silently discarded.

They are routed to:

\[
\boxed{
R_{\rm tail}
\vee
R_{\rm crit}
\vee
R_{\rm state}.
}
\tag{11.1}
\]

So D104.1 is a strong frozen whole-space subbranch closure, not a global Type-II theorem.

---

# 12. Graph compression after D104

D103 had:

\[
\mathsf K_{\rm coax}
\vee
\mathsf K_{\rm sh}^{12}
\vee
\mathsf K_{\rm sh}^{13}
\vee
\mathsf K_{\rm sh}^{23}
\vee
\mathsf K_{\rm axi}.
\]

D104 refines:

\[
\boxed{
\mathsf K_{\rm coax}^{\rm frozen,L^2}
\Longrightarrow
0.
}
\tag{12.1}
\]

But:

\[
\boxed{
\mathsf K_{\rm sh}^{ij,\rm frozen,L^2}
\neq0,
}
\tag{12.2}
\]

and:

\[
\boxed{
\mathsf K_{\rm axi}^{\rm frozen,L^2}
\neq0.
}
\tag{12.3}
\]

The surviving simple-shear node further splits into:

\[
\boxed{
\mathsf K_{\rm sh}^{\rm off-res}
\vee
\mathsf K_{\rm sh}^{\rm near-res}.
}
\tag{12.4}
\]

The axisymmetric node contains genuine polarization kernels.

Thus the nonlocal self-consistency graph is no longer one generic “Riesz resonance” node.

It has three mathematically distinct mechanisms:

1. **coaxial spectral-support obstruction**;
2. **simple-shear scalar transfer multiplier**;
3. **axisymmetric vector polarization kernel**.

---

# 13. Why D104 does not close the TR angular cone

D103 already supplied a local shear eigen-lock with nonzero Riesz-kernel directional pairing.

D104 now shows that simple-shear eigen-lock can also pass the whole-space frozen \(L^2\) Riesz self-consistency test.

Therefore:

\[
\boxed{
\text{eigen-lock}
+
\text{Riesz self-consistency}
+
\text{local TR compatibility}
}
\]

is not yet contradictory.

The next rigidity theorem must use structure not yet consumed:

- spatial variation of the strain eigenframe;
- strict DSS recurrence;
- Kelvin second-moment orientation;
- fixed-sign TR pair-cell recurrence;
- or the near-resonance / polarization topology.

---

# 14. Status ledger

## PROVED this round

### D104-P1 — exact Fourier symbol:
\[
M(n)=\frac13I-n\otimes n.
\]

### D104-P2 — trace-free adjoint Riesz scalar:
\[
\widehat r=-n^\top\widehat\Phi n.
\]

### D104-P3 — frozen loaded coaxial self-consistency reduces to a quadratic resonance cone.

### D104-P4 — the frozen whole-space \(L^2\) coaxial branch is zero.

### D104-P5 — pure \(r=0\) frozen coaxial eigenrays are also zero in \(L^2\).

### D104-P6 — exact simple-shear scalar transfer multiplier.

### D104-P7 — explicit shear loading tensor:
\[
A_{ij,k}
=
\operatorname{diag}
\left(
9s_k/\Delta-1,
-9s_k/\Delta-1,
2
\right).
\]

### D104-P8 — explicit simple-shear resonance cone.

### D104-P9 — nonzero whole-space \(L^2\) frozen simple-shear self-consistent solutions exist off resonance.

### D104-P10 — axisymmetric cross-plane block contains an infinite-dimensional \(r=0\) polarization kernel.

### D104-P11 — axisymmetric planar block contains an infinite-dimensional \(r=0\) polarization kernel.

### D104-P12 — every exact constant-coefficient positive-viscosity \(L^2\) eigen-lock is zero.

---

# 15. What is NOT proved

D104 does not prove:

- the variable-coefficient coaxial branch is zero;
- simple-shear Riesz-loaded solutions extend to a strict DSS Euler profile;
- axisymmetric polarization fields satisfy the full adjoint path/TR/Kelvin system;
- near-resonance shear concentration is impossible;
- Morrey/non-\(L^2\) coaxial states are impossible;
- the frozen viscous NO-GO yields a uniform vanishing-viscosity contradiction;
- global Navier–Stokes regularity.

The remaining problem is no longer generic Riesz self-consistency.

It is **shear-polarized / axisymmetric-polarized recurrent transport geometry**.

---

# 16. STOP-D104

\[
\boxed{
\begin{minipage}{0.94\linewidth}
Imposing \(r=\mathcal T_0^*\Phi\) separates the D103 adjoint tensor rays into three genuinely different nonlocal mechanisms. The Riesz symbol is \(M(n)=I/3-n\otimes n\), so for trace-free tensors \(\widehat r=-n^\top\widehat\Phi n\). A frozen simple-strain coaxial ray has \(\Phi=Ar\), hence \([1+n^\top An]\widehat r=0\). Because \(A\) is trace-free, the characteristic set \(1+n^\top An=0\) is at most a measure-zero quadratic cone; therefore every whole-space \(L^2\) frozen coaxial eigen-lock is zero, including the pure \(r=0\) coaxial rays. In sharp contrast, a single-shear ray \(\Phi=qH_{ij}+A_{ij,k}r\) obeys \([1-a(n)]\widehat r=-2n_in_j\widehat q\). Away from the explicit quadratic resonance cone, this is an ordinary bounded order-zero multiplier, so nonzero whole-space \(L^2\) frozen shear eigen-locks exist. For \(S=\operatorname{diag}(1,0,-1)\), \(H_{13}\) gives \(\widehat r=-2n_1n_3\widehat q/(3n_2^2)\), which is perfectly regular on frequency patches away from \(n_2=0\). Axisymmetric strain is even less rigid: its two-dimensional shear eigenspaces admit Fourier-dependent polarizations that lie identically in the kernel of \(\mathcal T_0^*\), producing infinite-dimensional nonzero \(L^2\) \(r=0\) eigen-lock families. Finally, at fixed positive viscosity every globally frozen constant-\(S\), constant-\(\beta\) exact \(L^2\) eigen-lock is zero because the full Fourier determinant is a nontrivial analytic function whose characteristic set has measure zero. Thus the coaxial frozen node is genuinely removed, but Riesz self-consistency alone does not close the late survivor: the graph now splits into a simple-shear order-zero transfer branch, a near-resonance concentration branch, and an axisymmetric polarization branch.
\end{minipage}
}
\]

---

# 17. Next autonomous step

## DCRP105 / X72-R88 — Shear-Polarized TR Geometry and Vanishing-Viscosity Spectral Migration

**Working title**

> **Can the Frozen Simple-Shear / Axisymmetric Riesz Polarization Survivors Maintain the D102 Fixed-Sign TR Angular Cell and Kelvin Second-Moment Lock under Strict DSS Recurrence and Vanishing Viscosity?**

Primary tasks:

1. start with the simple-shear polarization:
   \[
   \widehat\Phi
   =
   P_{ij,k}(n)\widehat q;
   \]
2. derive the exact projection:
   \[
   [\delta u\cdot\nabla K_0]:H_{ij}
   \]
   in the strain eigenframe;
3. scalarize the recurrent TR angular cone;
4. compare its angular wedges with the Riesz resonance cone \(\Sigma_{ij,k}\);
5. test whether the Kelvin nematic covariance can remain compatible with one fixed shear wedge;
6. add the prelimit viscous symbol:
   \[
   \varepsilon|\xi|^2I+\mathscr M_0(n);
   \]
7. determine whether approximate eigen-lock requires:
   - frequency migration;
   - coefficient/eigenframe modulation;
   - or state/critical escape;
8. treat axisymmetric polarization as a separate vector-polarization branch.

Desired endpoint:

\[
\boxed{
\mathsf K_{\rm sh/axi}
\Longrightarrow
\text{one scalar/angular spectral conveyor}
\vee
R_{\rm scale}
\vee
R_{\rm state}
\vee
R_{\rm crit}.
}
\]

**End checkpoint:** DCRP104 / X72-R87.
