# DCRP103 / X72-R86 — Adjoint Eigen-Lock Compatibility, Five-Ray Spectrum, and the Nonlocal Riesz-Loaded Tensor-Ray Normal Forms

**Series:** Independent Navier–Stokes Research Series / X72 Bridge  
**Date:** 2026-08-20  
**Status:** proof-development checkpoint / tensor-ray classification round  
**Immediate predecessor:** `NS_DCRP102_X72R85_BackwardAdjoint_CopulaCone_2026-08-20.md`

## Primary internal dependencies

- X72 Round37 — affine-response defect operator
  \[
  \mathscr L_S[E]=L_S(E)+2\mathcal T_0(S:E).
  \]
- DCRP67–68 — cofactor self-lock spectral geometry / axisymmetric integrability collapse.
- DCRP102 — adjoint eigen-lock kernel
  \[
  -\nu\Delta\Phi+L_S(\Phi)+2S\mathcal T_0^*\Phi=\beta\Phi.
  \]
- DCRP102 — recurrent oriented TR angular pair cone.

## Fresh primary-source calibration

- E. Hess-Childs, M. Rosenzweig, S. Serfaty, *Another look at regularity in transport-commutator estimates*, arXiv:2601.02326 (2026).
- E. Hess-Childs, M. Rosenzweig, S. Serfaty, *A sharp commutator estimate for all Riesz modulated energies*, arXiv:2511.13461 (2025).
- R. Yu, *Filtered Vortex Stretching and Subgrid Defects for the Three-Dimensional Navier–Stokes Equations*, arXiv:2606.27560 (2026).
- D. S. Agafontsev, E. A. Kuznetsov, A. A. Mailybaev, *Asymptotic solution for high vorticity regions in incompressible 3D Euler equations*, arXiv:1609.07782.

The external exact-pancake literature is used only as a calibration that axisymmetric strain/shear geometries are locally realizable in Euler-type dynamics; it is not identified with the D103 adjoint eigen-lock.

No full Navier–Stokes regularity theorem is claimed.

---

# 0. Executive result

D102 left the compact regular-pair survivor with the dichotomy

\[
\boxed{
\mathsf A_{\rm adj}>0
\vee
\mathsf K_{\rm adj\mbox{-}eig}.
}
\]

D103 classifies the second branch.

The exact eigen-lock equation is

\[
\boxed{
-\nu\Delta\Phi
+
L_S(\Phi)
+
2S\,r
=
\beta\Phi,
\qquad
r:=\mathcal T_0^*\Phi.
}
\tag{0.1}
\]

The highest-leverage algebra is the inviscid / locally affine core:

\[
\boxed{
L_S(\Phi)+2rS=\beta\Phi.
}
\tag{0.2}
\]

Let \(S\in\mathrm{Sym}_0(3)\), \(S\neq0\), and diagonalize

\[
S=\operatorname{diag}(s_1,s_2,s_3),
\qquad
s_1+s_2+s_3=0.
\]

Then every off-diagonal component satisfies

\[
\boxed{
(s_i+s_j-\beta)\Phi_{ij}=0.
}
\tag{0.3}
\]

Hence a nonzero shear component obeys

\[
\boxed{
\beta=s_i+s_j=-s_k.
}
\tag{0.4}
\]

The nonlocal scalar \(r=\mathcal T_0^*\Phi\) never changes this shear resonance because the forcing \(2rS\) is coaxial/diagonal in the \(S\)-eigenframe.

For simple strain, define

\[
\boxed{
C_S^0
=
S^2-\frac13|S|^2I
}
\tag{0.5}
\]

and

\[
\boxed{
d_S
=
\sqrt{\frac23}|S|.
}
\tag{0.6}
\]

The diagonal trace-free space is exactly

\[
\boxed{
\operatorname{span}\{S,C_S^0\}.
}
\]

Moreover

\[
\boxed{
L_S(S)=2C_S^0,
}
\tag{0.7}
\]

\[
\boxed{
L_S(C_S^0)=\frac{|S|^2}{3}S.
}
\tag{0.8}
\]

Therefore, when \(r=0\), the complete local spectrum of \(L_S\) on the five-dimensional space \(\mathrm{Sym}_0(3)\) is

# Five-Ray Spectrum

\[
\boxed{
\operatorname{spec}L_S
=
\left\{
-s_1,-s_2,-s_3,
+\sqrt{\frac23}|S|,
-\sqrt{\frac23}|S|
\right\}.
}
\tag{0.9}
\]

The first three eigenrays are the shear tensors

\[
E_{23},\quad E_{13},\quad E_{12},
\]

and the two diagonal/coaxial eigenrays are

\[
\boxed{
\Phi_\pm
=
\beta_\pm S+2C_S^0,
\qquad
\beta_\pm
=
\pm d_S.
}
\tag{0.10}
\]

When \(r\neq0\), the nonlocal Riesz scalar loads only the diagonal sector.

For every

\[
\beta^2\neq d_S^2,
\]

the forced diagonal component is uniquely

\[
\boxed{
\Phi_{\rm diag}
=
\frac{
2r
}{
\beta^2-d_S^2
}
\left(
\beta S+2C_S^0
\right).
}
\tag{0.11}
\]

Thus, on a simple-strain point, every nonzero inviscid eigen-lock belongs to one of only two classes:

## Class A — coaxial Riesz-loaded family

\[
\boxed{
\Phi
=
\frac{
2r
}{
\beta^2-d_S^2
}
(\beta S+2C_S^0)
}
\tag{0.12}
\]

with no shear component;

or, if \(r=0\),

\[
\boxed{
\beta=\pm d_S,
\qquad
\Phi\parallel\Phi_\pm.
}
\tag{0.13}
\]

## Class B — one single-shear resonance family

For exactly one pair \(i<j\), with complementary index \(k\),

\[
\boxed{
\beta=-s_k,
}
\tag{0.14}
\]

and

\[
\boxed{
\Phi
=
qE_{ij}
+
\frac{
2r
}{
s_k^2-d_S^2
}
\left(
-s_kS+2C_S^0
\right),
}
\tag{0.15}
\]

where \(q\) is the shear amplitude.

For simple strain,

\[
\boxed{
s_k^2\neq d_S^2,
}
\]

so the formula is nonsingular.

Two different shear pairs cannot be simultaneously active unless the strain has repeated eigenvalues.

Therefore the five-dimensional eigen-lock problem has collapsed to

\[
\boxed{
\text{coaxial family}
\vee
\text{one of three shear families}
\vee
\text{strain spectral degeneracy}.
}
\tag{0.16}
\]

D103 also proves that the recurrent TR angular cone does **not** eliminate the shear family locally.

There is an exact local compatibility witness:

\[
S=\operatorname{diag}(1,0,-1),
\]

\[
\Phi=E_{13}+E_{31},
\]

\[
r=0,
\qquad
\beta=0.
\]

Then

\[
L_S(\Phi)=0.
\]

For the 3D trace-free Riesz kernel

\[
K_0(z)
\propto
|z|^{-3}
\left(
I-3\hat z\otimes\hat z
\right),
\]

take

\[
z=e_3,
\qquad
\delta u=e_1.
\]

A direct differentiation gives

\[
\boxed{
(\delta u\cdot\nabla)K_0(e_3)
\propto
-(E_{13}+E_{31}).
}
\tag{0.17}
\]

Hence

\[
\boxed{
G:\Phi\neq0.
}
\tag{0.18}
\]

Choosing the sign of \(\delta q\) appropriately yields a positive TR angular factor.

So:

\[
\boxed{
\text{local tensor-ray algebra}
\not\Rightarrow
\text{TR angular contradiction}.
}
\tag{0.19}
\]

The remaining obstruction is no longer five-dimensional tensor algebra.

It is the **global/nonlocal self-consistency and spatial integrability** of these finite ray families.

---

# 1. Coordinate-free commutator constraint

Start from

\[
L_S(\Phi)+2rS=\beta\Phi.
\]

Because \(S\) commutes with the forcing \(2rS\), take commutators with \(S\).

The isotropic trace-correction term in \(L_S\) also commutes with \(S\).

Thus

\[
[S,L_S(\Phi)]
=
[S,S\Phi+\Phi S].
\]

A direct expansion gives

\[
[S,S\Phi+\Phi S]
=
[S^2,\Phi].
\]

Therefore:

## Theorem D103.1 — Eigen-lock commutator equation

\[
\boxed{
[S^2,\Phi]
=
\beta[S,\Phi].
}
\tag{1.1}
\]

Equivalently,

\[
\boxed{
[S^2-\beta S,\Phi]=0.
}
\tag{1.2}
\]

This equation is independent of the nonlocal scalar \(r\).

It is the algebraic reason the Riesz loading cannot alter shear resonance.

---

# 2. Off-diagonal resonance

In the eigenbasis of \(S\),

\[
[S^2,\Phi]_{ij}
=
(s_i^2-s_j^2)\Phi_{ij},
\]

\[
[S,\Phi]_{ij}
=
(s_i-s_j)\Phi_{ij}.
\]

Hence

\[
(s_i-s_j)
(s_i+s_j-\beta)
\Phi_{ij}
=
0.
\]

Therefore:

## Theorem D103.2 — Shear resonance condition

For every \(i\neq j\),

\[
\boxed{
(s_i-s_j)
(s_i+s_j-\beta)
\Phi_{ij}=0.
}
\tag{2.1}
\]

If \(S\) is simple:

\[
s_i\neq s_j,
\]

then:

\[
\boxed{
\Phi_{ij}\neq0
\Longrightarrow
\beta=s_i+s_j=-s_k.
}
\tag{2.2}
\]

---

# 3. Multiple shear components force strain degeneracy

Suppose \(S\) is simple.

If:

\[
\Phi_{12}\neq0
\]

and:

\[
\Phi_{13}\neq0,
\]

then:

\[
\beta=-s_3
\]

and:

\[
\beta=-s_2.
\]

Thus:

\[
s_2=s_3,
\]

contradicting simplicity.

The same argument applies to every pair.

Therefore:

## Theorem D103.3 — Single-shear theorem

On a simple-strain eigen-lock point:

\[
\boxed{
\text{at most one off-diagonal shear pair is active.}
}
\tag{3.1}
\]

If two shear pairs are active, the strain has a repeated eigenvalue.

If all three are active, trace-free symmetry forces:

\[
\boxed{
S=0.
}
\tag{3.2}
\]

---

# 4. The diagonal algebra is generated by \(S\) and its cofactor

Assume \(S\) is simple and nonzero.

Every trace-free diagonal tensor commuting with \(S\) is a polynomial in \(S\) of degree at most two.

Modulo the identity, the diagonal trace-free space is

\[
\boxed{
\operatorname{span}\{S,C_S^0\}.
}
\tag{4.1}
\]

Using

\[
C_S^0
=
S^2-\frac13|S|^2I,
\]

one gets:

\[
L_S(S)
=
2S^2-\frac23|S|^2I
=
2C_S^0.
\]

So

\[
\boxed{
L_S(S)=2C_S^0.
}
\tag{4.2}
\]

Next,

\[
\begin{aligned}
L_S(C_S^0)
&=
SC_S^0+C_S^0S
-\frac23(S:C_S^0)I
\\
&=
2S^3
-\frac23|S|^2S
-\frac23\operatorname{tr}(S^3)I.
\end{aligned}
\]

For a trace-free \(3\times3\) matrix,

\[
S^3
=
\frac12|S|^2S
+
\det(S)I,
\]

and:

\[
\operatorname{tr}(S^3)=3\det S.
\]

Hence the identity terms cancel and:

\[
\boxed{
L_S(C_S^0)
=
\frac13|S|^2S.
}
\tag{4.3}
\]

This is an exact two-dimensional closure.

---

# 5. The two diagonal eigenvalues

Write

\[
\Phi_{\rm diag}
=
aS+bC_S^0.
\]

When \(r=0\),

\[
L_S(\Phi_{\rm diag})
=
\beta\Phi_{\rm diag}
\]

gives

\[
\frac{|S|^2}{3}b
=
\beta a,
\]

\[
2a
=
\beta b.
\]

For a nonzero solution,

\[
\boxed{
\beta^2
=
\frac23|S|^2.
}
\tag{5.1}
\]

Therefore:

\[
\boxed{
\beta_\pm
=
\pm\sqrt{\frac23}|S|.
}
\tag{5.2}
\]

Choosing \(b=2\) gives:

\[
a=\beta_\pm,
\]

so:

\[
\boxed{
\Phi_\pm
=
\beta_\pm S+2C_S^0.
}
\tag{5.3}
\]

These are the two coaxial diagonal eigenrays.

---

# 6. Complete five-ray spectrum for \(r=0\)

The three shear tensors are:

\[
E_{12}
=
e_1\otimes e_2+e_2\otimes e_1,
\]

and cyclic permutations.

Since:

\[
L_S(E_{ij})
=
(s_i+s_j)E_{ij}
=
-s_kE_{ij},
\]

the full spectrum on \(\mathrm{Sym}_0(3)\) is:

## Theorem D103.4 — Five-Ray Spectrum

\[
\boxed{
\operatorname{spec}L_S
=
\left\{
-s_1,-s_2,-s_3,
+d_S,-d_S
\right\},
}
\tag{6.1}
\]

with

\[
d_S=\sqrt{\frac23}|S|.
\]

For simple \(S\), all eigenspaces are one-dimensional unless accidental equality among these five scalar eigenvalues occurs.

---

# 7. Riesz-loaded diagonal solution

Now restore:

\[
r=\mathcal T_0^*\Phi.
\]

The diagonal equation is:

\[
L_S(\Phi_{\rm diag})
+
2rS
=
\beta\Phi_{\rm diag}.
\]

Write:

\[
\Phi_{\rm diag}=aS+bC_S^0.
\]

Then:

\[
\frac{|S|^2}{3}b+2r
=
\beta a,
\]

\[
2a
=
\beta b.
\]

Let:

\[
d_S^2=\frac23|S|^2.
\]

If:

\[
\beta^2\neq d_S^2,
\]

solve:

\[
\boxed{
b
=
\frac{4r}{\beta^2-d_S^2},
}
\tag{7.1}
\]

\[
\boxed{
a
=
\frac{2\beta r}{\beta^2-d_S^2}.
}
\tag{7.2}
\]

Therefore:

## Theorem D103.5 — Riesz-loaded coaxial response

\[
\boxed{
\Phi_{\rm diag}
=
\frac{
2r
}{
\beta^2-d_S^2
}
\left(
\beta S+2C_S^0
\right).
}
\tag{7.3}
\]

At:

\[
\beta=\pm d_S,
\]

solvability forces:

\[
\boxed{
r=0,
}
\tag{7.4}
\]

after which the pure diagonal eigenray \(\Phi_\pm\) is recovered.

---

# 8. Simple-strain shear normal form

Suppose:

\[
\Phi_{ij}\neq0.
\]

Then:

\[
\beta=-s_k.
\]

For simple strain, the denominator:

\[
s_k^2-d_S^2
\]

cannot vanish.

Indeed:

\[
s_k^2=d_S^2
\]

is equivalent to:

\[
s_i=s_j,
\]

which is axisymmetric degeneracy.

Therefore:

## Theorem D103.6 — Single-shear Riesz-loaded normal form

For simple \(S\),

\[
\boxed{
\Phi
=
qE_{ij}
+
\frac{
2r
}{
s_k^2-d_S^2
}
\left(
-s_kS+2C_S^0
\right),
}
\tag{8.1}
\]

with:

\[
\boxed{
\beta=-s_k.
}
\tag{8.2}
\]

The nonlocal Riesz scalar adds only a coaxial correction.

The shear resonance itself remains exact.

---

# 9. Axisymmetric strain degeneracy

Every nonzero trace-free symmetric \(3\times3\) tensor with a repeated eigenvalue is, after rotation,

\[
\boxed{
S
=
\operatorname{diag}(a,a,-2a),
\qquad
a\neq0.
}
\tag{9.1}
\]

The diagonal cofactor is proportional to \(S\):

\[
\boxed{
C_S^0=-aS.
}
\tag{9.2}
\]

The five-dimensional tensor space decomposes into three \(L_S\)-eigenspaces:

## axial/pancake ray

\[
\boxed{
V_{-2a}
=
\operatorname{span}\{S\};
}
\tag{9.3}
\]

## planar anisotropy/shear block

\[
\boxed{
V_{2a}
=
\mathrm{Sym}_0(n^\perp),
\qquad
\dim V_{2a}=2;
}
\tag{9.4}
\]

## cross-plane shear block

\[
\boxed{
V_{-a}
=
\operatorname{span}\{E_{13},E_{23}\},
\qquad
\dim V_{-a}=2.
}
\tag{9.5}
\]

Thus:

\[
\boxed{
\operatorname{spec}L_S
=
\{-2a,\ 2a,\ -a\}
}
\tag{9.6}
\]

with multiplicities:

\[
1,\ 2,\ 2.
\]

The Riesz forcing \(2rS\) lies entirely in \(V_{-2a}\).

Therefore, for:

\[
\beta\neq-2a,
\]

the forced axial component is:

\[
\boxed{
\Phi_{\rm ax}
=
\frac{2r}{\beta+2a}S.
}
\tag{9.7}
\]

If:

\[
\beta=2a
\]

or:

\[
\beta=-a,
\]

one may add an arbitrary vector from the corresponding 2D eigenspace.

If:

\[
\beta=-2a,
\]

solvability requires:

\[
r=0.
\]

This is the complete local axisymmetric eigen-lock classification.

---

# 10. Local TR compatibility witness

The tensor-ray normal forms are not automatically killed by the D102 recurrent TR angular cone.

Take:

\[
\boxed{
S
=
\operatorname{diag}(1,0,-1).
}
\tag{10.1}
\]

Choose:

\[
\boxed{
\Phi
=
E_{13}
=
e_1\otimes e_3+e_3\otimes e_1.
}
\tag{10.2}
\]

Then:

\[
s_1+s_3=0,
\]

so:

\[
\boxed{
L_S(\Phi)=0.
}
\tag{10.3}
\]

Thus:

\[
r=0,
\qquad
\beta=0
\]

is a valid local adjoint eigen-lock.

Now use the standard three-dimensional trace-free Riesz Hessian kernel:

\[
\boxed{
K_0(z)
=
c
\left[
|z|^{-3}I
-
3|z|^{-5}z\otimes z
\right].
}
\tag{10.4}
\]

Set:

\[
z=e_3,
\qquad
v=\delta u=e_1.
\]

Because:

\[
z\cdot v=0,
\]

differentiate in the \(v\)-direction:

\[
\boxed{
(v\cdot\nabla)K_0(e_3)
=
-3c
(E_{13}).
}
\tag{10.5}
\]

Therefore:

\[
\boxed{
G:\Phi
=
-6c
\neq0
}
\tag{10.6}
\]

under the unnormalized convention \(|E_{13}|^2=2\).

Choosing the sign of:

\[
\delta q
\]

appropriately gives:

\[
\boxed{
(G:\Phi)\delta q>0.
}
\tag{10.7}
\]

Thus:

## Theorem D103.7 — Local eigen-lock/TR compatibility NO-GO

The adjoint tensor-ray eigen-lock and the recurrent TR angular cone are locally algebraically compatible.

Pure pointwise tensor algebra cannot close the branch.

---

# 11. Meaning of the compatibility witness

D103.7 is deliberately modest.

It proves only:

> the local shear-ray normal form is not annihilated by the actual directional derivative geometry of the Riesz kernel.

It does **not** construct:

- a global X72 adjoint solution;
- a DSS profile;
- a Navier–Stokes singularity;
- a globally self-consistent \(r=\mathcal T_0^*\Phi\).

The missing constraints are now:

1. spatial integrability of \(\Phi\);
2. nonlocal Riesz self-consistency;
3. material recurrence;
4. pair-scale compactness;
5. compatibility with the recurrent Kelvin second-moment state.

---

# 12. Global self-consistency equations

The pointwise classification becomes genuinely nonlocal through:

\[
\boxed{
r=\mathcal T_0^*\Phi.
}
\tag{12.1}
\]

## Coaxial branch

Insert D103.5:

\[
\boxed{
r
=
\mathcal T_0^*
\left[
\frac{
2r
}{
\beta^2-d_S^2
}
(
\beta S+2C_S^0
)
\right].
}
\tag{12.2}
\]

This is a scalar nonlocal fixed-point equation for \(r\).

## Single-shear branch

Insert D103.6:

\[
\boxed{
r
=
\mathcal T_0^*
\left[
qE_{ij}
+
\frac{
2r
}{
s_k^2-d_S^2
}
(
-s_kS+2C_S^0
)
\right].
}
\tag{12.3}
\]

This is a coupled shear-amplitude / scalar-Riesz self-consistency system.

These are the actual next global equations.

---

# 13. Why the nonlocal term is now the central obstruction

Before D103, the eigen-lock kernel lived in the full tensor equation:

\[
L_S(\Phi)+2S\mathcal T_0^*\Phi=\beta\Phi.
\]

After D103:

- the local five-dimensional tensor algebra is completely classified;
- the off-diagonal resonance is explicit;
- the diagonal response is explicit;
- axisymmetric degeneracy is explicit;
- local TR compatibility is explicit.

What remains is the operator equation generated by:

\[
\boxed{
\mathcal T_0^*.
}
\]

Therefore the eigen-lock branch has changed from a local tensor mystery into a nonlocal scalar/shear fixed-point problem.

---

# 14. Compact angular-action consequence

Let \(\mathscr K_{\rm ray}\) be the union of:

- coaxial Riesz-loaded normal forms;
- three single-shear normal forms;
- axisymmetric degeneracy blocks.

On a sequentially compact normalized class, suppose the recurrent adjoint state stays a fixed positive distance from:

\[
\mathscr K_{\rm ray}.
\]

Then the continuous angular-action functional cannot vanish.

By compactness:

## Theorem D103.8 — Angular-action gap away from ray kernel

There exists:

\[
\boxed{
c_{\rm adj}>0
}
\]

such that:

\[
\boxed{
\int_I\Omega_\Phi\,ds
\ge
c_{\rm adj}
}
\tag{14.1}
\]

on every recurrent fixed-lag source window in that separated compact class.

Thus the only way to make adjoint angular action arbitrarily small is to approach one of the explicit ray normal forms.

---

# 15. Zero-lag relation to the old cofactor self-lock geometry

D67–68 studied the much more special instantaneous cofactor branch.

There, alignment and the exact cofactor formula reduced the tensor geometry to one transverse anisotropy scalar and two axisymmetric self-lock spectra; full velocity-gradient integrability then removed those as nontrivial isotropic-covariance recurrent equality modes.

D103 should not identify the generic finite-lag adjoint ray:

\[
\Phi
\]

with the instantaneous strain cofactor:

\[
C_S^0.
\]

But there is now a precise bridge question:

> does the nonlocal X72 adjoint self-consistency force the generic ray families to collapse toward the older cofactor self-lock geometry?

That is a legitimate future theorem target.

---

# 16. External calibration

The modern transport–Riesz literature shows that generic commutator control remains regularity-sensitive; this supports the decision not to estimate D103's remaining operator by a soft universal norm inequality.

Yu's filtered-vorticity result similarly shows that critical increment control naturally reaches generalized Young-profile compactness, but not automatically the full adjoint/Riesz path self-consistency required here.

The exact Euler pancake literature shows that axisymmetric straining plus shear can be locally realizable, so D103 does not declare the axisymmetric spectral block contradictory merely because it resembles pancake geometry.

---

# 17. Updated late graph

D102 had:

\[
\boxed{
\mathsf C_{\rm adj\mbox{-}copula}^{\ell_*}
\Longrightarrow
\mathsf A_{\rm adj}>0
\vee
\mathsf K_{\rm adj\mbox{-}eig}
\vee
R_{\rm escape}.
}
\]

D103 refines the eigen-lock node:

\[
\boxed{
\mathsf K_{\rm adj\mbox{-}eig}
\Longrightarrow
\mathsf K_{\rm coax}
\vee
\mathsf K_{\rm sh}^{12}
\vee
\mathsf K_{\rm sh}^{13}
\vee
\mathsf K_{\rm sh}^{23}
\vee
\mathsf K_{\rm axi}
}
\tag{17.1}
\]

where:

- \(\mathsf K_{\rm coax}\) = coaxial Riesz-loaded fixed-point family;
- \(\mathsf K_{\rm sh}^{ij}\) = one single-shear resonance plus forced coaxial correction;
- \(\mathsf K_{\rm axi}\) = axisymmetric spectral-degeneracy block.

This is the graph-theoretic compression achieved in D103.

---

# 18. Status ledger

## PROVED this round

### D103-P1 — coordinate-free eigen-lock commutator equation:
\[
[S^2,\Phi]=\beta[S,\Phi].
\]

### D103-P2 — exact shear resonance:
\[
\Phi_{ij}\neq0\Rightarrow\beta=s_i+s_j=-s_k.
\]

### D103-P3 — simple strain admits at most one active shear pair.

### D103-P4 — diagonal simple-strain sector is exactly:
\[
\operatorname{span}\{S,C_S^0\}.
\]

### D103-P5 — exact two-dimensional operator identities:
\[
L_S(S)=2C_S^0,
\qquad
L_S(C_S^0)=\frac{|S|^2}{3}S.
\]

### D103-P6 — complete five-ray spectrum for \(r=0\):
\[
\{-s_1,-s_2,-s_3,\pm\sqrt{2/3}|S|\}.
\]

### D103-P7 — exact Riesz-loaded coaxial solution.

### D103-P8 — exact single-shear Riesz-loaded normal form.

### D103-P9 — \(s_k^2=d_S^2\) is exactly the axisymmetric degeneracy condition.

### D103-P10 — complete axisymmetric eigenspace decomposition.

### D103-P11 — exact local Riesz-kernel/shear-ray witness shows eigen-lock can support nonzero TR angular pairing.

### D103-P12 — away from the explicit ray kernel, compactness yields a positive adjoint angular-action gap.

---

# 19. What is NOT proved

D103 does not prove:

- the coaxial nonlocal fixed-point equation has only the zero solution;
- the single-shear Riesz-loaded system is globally inconsistent;
- the local TR compatibility witness extends to a DSS profile;
- axisymmetric adjoint rays are impossible;
- the adjoint angular-action gap has a finite physical global budget;
- the Riesz scalar \(r\) is controlled by the Kelvin second-moment state;
- global Navier–Stokes regularity.

The remaining eigen-lock problem is now **nonlocal self-consistency / spatial integrability**, not five-dimensional tensor algebra.

---

# 20. STOP-D103

\[
\boxed{
\begin{minipage}{0.94\linewidth}
The D102 adjoint eigen-lock kernel can be solved completely at the local tensor-algebra level. Diagonalizing the trace-free strain \(S=\operatorname{diag}(s_1,s_2,s_3)\), the commutator identity \([S^2,\Phi]=\beta[S,\Phi]\) forces every nonzero shear component to satisfy \(\beta=s_i+s_j=-s_k\). For simple strain, at most one shear pair can be active. The diagonal trace-free sector is exactly \(\operatorname{span}\{S,C_S^0\}\), with \(L_S(S)=2C_S^0\) and \(L_S(C_S^0)=|S|^2S/3\). Hence when \(r=\mathcal T_0^*\Phi=0\), the full five-dimensional spectrum is
\[
\{-s_1,-s_2,-s_3,\pm\sqrt{2/3}|S|\},
\]
i.e. three shear rays plus two coaxial rays. When \(r\neq0\), the nonlocal Riesz term loads only the coaxial sector:
\[
\Phi_{\rm diag}
=
\frac{2r}{\beta^2-\frac23|S|^2}
(\beta S+2C_S^0),
\]
while every active shear still obeys the exact resonance \(\beta=-s_k\). Repeated strain eigenvalues form one explicit axisymmetric degeneracy block. This classification is sharp at the local level: \(S=\operatorname{diag}(1,0,-1)\), \(\Phi=E_{13}\), \(r=0\) is an exact shear eigen-lock, and the directional derivative of the actual 3D trace-free Riesz kernel at \(z=e_3\) in direction \(e_1\) is proportional to \(-E_{13}\), so the recurrent TR angular factor can be nonzero. Thus tensor-ray algebra alone cannot close the survivor. The remaining eigen-lock gap has now moved entirely to the global equations \(r=\mathcal T_0^*\Phi\): a coaxial scalar nonlocal fixed-point problem or one of three shear–Riesz self-consistency systems. Away from these explicit ray families, compactness gives a uniform positive adjoint angular-action gap.
\end{minipage}
}
\]

---

# 21. Next autonomous step

## DCRP104 / X72-R87 — Riesz Self-Consistency of the Adjoint Ray Families

**Working title**

> **Can the Coaxial or Single-Shear Adjoint Ray Satisfy \(r=\mathcal T_0^*\Phi\) on a Strict DSS Compact Profile without Developing a Nonlocal Spectral / Tail / State Defect?**

Primary tasks:

1. start from the coaxial equation:
   \[
   r
   =
   \mathcal T_0^*
   \left[
   \frac{2r}{\beta^2-d_S^2}
   (\beta S+2C_S^0)
   \right];
   \]
2. start from the shear equation:
   \[
   r
   =
   \mathcal T_0^*
   \left[
   qE_{ij}
   +
   \frac{2r}{s_k^2-d_S^2}
   (-s_kS+2C_S^0)
   \right];
   \]
3. isolate constant-coefficient/frozen-frame Fourier symbols;
4. determine the symbol-level kernel and resonance set;
5. test whether nonzero \(L^2\)/Morrey profiles can live on the resonance set;
6. separate whole-space Fourier nulls from local/tail-fed states;
7. route failure of coefficient compactness to state/critical escape;
8. seek:
   \[
   \mathsf K_{\rm ray}
   \Longrightarrow
   \text{nonlocal spectral resonance}
   \vee
   R_{\rm tail}
   \vee
   R_{\rm state}
   \vee
   R_{\rm crit}.
   \]

Desired endpoint:

\[
\boxed{
\text{adjoint eigen-lock}
\Longrightarrow
\text{one explicit Riesz spectral resonance manifold}
\vee
R_{\rm known}.
}
\]

**End checkpoint:** DCRP103 / X72-R86.
