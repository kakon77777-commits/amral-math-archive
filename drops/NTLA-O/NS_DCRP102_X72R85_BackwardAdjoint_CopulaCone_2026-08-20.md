# DCRP102 / X72-R85 — Backward Adjoint X-Test Dynamics, Oriented Pair-Copula Cone, and the No-Invariant-Sign-Cone Audit

**Series:** Independent Navier–Stokes Research Series / X72 Bridge  
**Date:** 2026-08-20  
**Status:** proof-development checkpoint / backward-adjoint copula-rigidity round  
**Immediate predecessor:** `NS_DCRP101_X72R84_JointPathYoung_SecondThirdMomentLock_2026-08-20.md`

## Primary internal dependencies

- X72 Round37 — exact affine-response defect equation.
- X72 Round38 — exact transport–Riesz pair/triple-increment identity.
- DCRP65–68 — factorwise null closure, correlation frontier, two-stress geometry, self-lock integrability collapse.
- DCRP95–96 — sign-coherent Kelvin slip / nematic second-moment lock.
- DCRP99–101 — bounded-lag X–Kelvin word / finite Duhamel forcing / second–third moment path-copula lock.

## Fresh primary-source calibration

- E. Hess-Childs, M. Rosenzweig, S. Serfaty, *Another look at regularity in transport-commutator estimates*, arXiv:2601.02326 (2026).
  Generic Riesz-type transport commutator estimates retain a sharp regularity burden; BMO does not generally replace the Lipschitz-gradient hypothesis, although defective estimates are available in almost-Lipschitz regimes.
- E. Hess-Childs, M. Rosenzweig, S. Serfaty, *A sharp commutator estimate for all Riesz modulated energies*, arXiv:2511.13461 (2025).
- R. Yu, *Filtered Vortex Stretching and Subgrid Defects for the Three-Dimensional Navier–Stokes Equations*, arXiv:2606.27560 (2026).
  At the critical exponent, bounded derivative-compatible velocity-increment defects yield cylindrical generalized Young profiles; this does not by itself furnish tightness for D101's enlarged finite-lag adjoint tuple.

No full Navier–Stokes regularity theorem is claimed.

---

# 0. Executive result

D101 reduced the selected compact transport–Riesz/Kelvin branch to one finite-lag path profile carrying

\[
\boxed{
\sigma_\Gamma\mathcal L_\Gamma(M^{(2)})\ge c_\Gamma>0
}
\]

and

\[
\boxed{
\sigma_{\rm TR}\mathcal L_{\rm TR}(M^{(3)})\ge c_{\rm TR}>0.
}
\]

The next question is whether the pulled-back X72 adjoint test has a sign/phase rigidity strong enough to collapse this mixed third-order copula.

D102 proves that there is **no generic invariant sign cone** for the adjoint tensor.

The X72 defect equation is

\[
D_tE-\nu\Delta E=-\mathscr L_S[E]+\mathcal F_E,
\]

with

\[
\mathscr L_S[E]
=
L_S(E)+2\mathcal T_0(S:E),
\]

\[
L_S(E)
=
ES+SE-\frac23(S:E)I.
\]

Writing

\[
\partial_tE
=
\mathcal A_E(t)E+\mathcal F_E,
\qquad
\mathcal A_E
=
\nu\Delta-u\cdot\nabla-\mathscr L_S,
\]

the backward adjoint satisfies

\[
\boxed{
-\partial_s\Phi
=
\nu\Delta\Phi
+
u\cdot\nabla\Phi
-
\mathscr L_S^*[\Phi].
}
\tag{0.1}
\]

On trace-free symmetric tensors,

\[
\boxed{
\mathscr L_S^*[\Phi]
=
L_S(\Phi)
+
2S\,\mathcal T_0^*\Phi.
}
\tag{0.2}
\]

Along a forward material trajectory,

\[
\boxed{
D_s\Phi
=
-\nu\Delta\Phi
+
\mathscr L_S^*[\Phi].
}
\tag{0.3}
\]

Thus the pulled-back X test is dynamically rotated/stretched by local strain and a nonlocal Riesz scalar.

Even the **local** part already prevents a generic detector half-space maximum principle.

Take

\[
G=\operatorname{diag}(1,-1,0),
\]

\[
\Phi_0=\operatorname{diag}(1,1,-2).
\]

Then

\[
G:\Phi_0=0.
\]

For

\[
S=\pm G,
\]

one has

\[
L_S(\Phi_0)=\pm2G,
\]

so

\[
\boxed{
G:L_S(\Phi_0)=\pm4.
}
\tag{0.4}
\]

The same boundary point of the detector half-space can be pushed to either side by admissible trace-free strain.

Hence

\[
\boxed{
\text{fixed-sign TR recurrence}
\not\Rightarrow
\text{generic pointwise sign preservation of }\delta\Phi_X.
}
\tag{0.5}
\]

What the fixed-sign TR branch **does** force is a recurrent **oriented pair-copula cone** on a regular pair-scale cylinder.

After removing principal-value / scale concentration and path-profile escape, there is a fixed normalized pair cylinder on which

\[
\boxed{
[\delta u\cdot\nabla K_0]:\delta\Phi_X\,\delta q
}
\]

has fixed sign and uniformly positive pair-space occupancy.

Equivalently, after fixing the sign of \(\delta q\), the tensor angle between

\[
G_{xy}:=[\delta u\cdot\nabla K_0]
\]

and

\[
\delta\Phi_X
\]

lies in one strict angular cone on a positive-measure pair set.

The remaining compact survivor is therefore a **dynamically propagated oriented adjoint-copula state**.

---

# 1. Exact adjoint of the local strain operator

Work in

\[
\mathrm{Sym}_0(3)
\]

with Frobenius pairing.

For trace-free symmetric \(E,\Phi,S\),

\[
L_S(E)
=
ES+SE-\frac23(S:E)I.
\]

Because

\[
\Phi:I=0,
\]

\[
\langle\Phi,L_S(E)\rangle
=
\langle\Phi,ES+SE\rangle.
\]

By cyclicity of trace,

\[
\langle\Phi,ES+SE\rangle
=
\langle E,S\Phi+\Phi S\rangle.
\]

Projecting back to trace-free tensors gives

\[
\boxed{
L_S^*=L_S.
}
\tag{1.1}
\]

So the local strain operator is self-adjoint on \(\mathrm{Sym}_0(3)\).

---

# 2. Adjoint of the Riesz scalar coupling

Recall

\[
\mathcal T_0
=
\nabla^2(-\Delta)^{-1}
+
\frac13I,
\]

viewed as

\[
\text{scalar}\to\mathrm{Sym}_0(3).
\]

Its Hilbert adjoint is

\[
\boxed{
\mathcal T_0^*\Phi
=
(-\Delta)^{-1}\partial_i\partial_j\Phi_{ij}
+
\frac13\operatorname{tr}\Phi.
}
\tag{2.1}
\]

On trace-free tensors,

\[
\boxed{
\mathcal T_0^*\Phi
=
(-\Delta)^{-1}\partial_i\partial_j\Phi_{ij}.
}
\tag{2.2}
\]

For

\[
2\mathcal T_0(S:E),
\]

\[
\begin{aligned}
\langle\Phi,2\mathcal T_0(S:E)\rangle
&=
2\langle\mathcal T_0^*\Phi,S:E\rangle
\\
&=
\langle E,2S\,\mathcal T_0^*\Phi\rangle.
\end{aligned}
\]

Therefore

## Theorem D102.1 — Exact defect-adjoint strain operator

\[
\boxed{
\mathscr L_S^*[\Phi]
=
L_S(\Phi)
+
2S\,\mathcal T_0^*\Phi.
}
\tag{2.3}
\]

The adjoint contains a nonlocal scalar projection even when the terminal X detector is tensorial.

---

# 3. Exact backward adjoint equation

The forward equation is

\[
\partial_tE
=
\nu\Delta E
-u\cdot\nabla E
-\mathscr L_S[E]
+\mathcal F_E.
\]

Since

\[
\nabla\cdot u=0,
\]

\[
(-u\cdot\nabla)^*
=
u\cdot\nabla.
\]

Hence

## Theorem D102.2 — Backward X72 adjoint

\[
\boxed{
-\partial_s\Phi
=
\nu\Delta\Phi
+
u\cdot\nabla\Phi
-
L_S(\Phi)
-
2S\,\mathcal T_0^*\Phi.
}
\tag{3.1}
\]

Along a forward material path,

\[
D_s=\partial_s+u\cdot\nabla,
\]

so

\[
\boxed{
D_s\Phi
=
-\nu\Delta\Phi
+
L_S(\Phi)
+
2S\,\mathcal T_0^*\Phi.
}
\tag{3.2}
\]

In the inviscid/profile limit,

\[
\boxed{
D_s\Phi
=
L_S(\Phi)
+
2S\,\mathcal T_0^*\Phi.
}
\tag{3.3}
\]

---

# 4. Exact pair-increment adjoint equation

Let

\[
X(s),Y(s)
\]

be two forward material trajectories.

Write

\[
\delta\Phi
=
\Phi(X,s)-\Phi(Y,s),
\]

\[
\delta S
=
S(X,s)-S(Y,s),
\]

and

\[
r=\mathcal T_0^*\Phi,
\qquad
\delta r=r(X)-r(Y).
\]

Define

\[
B(S,\Phi)
=
S\Phi+\Phi S-\frac23(S:\Phi)I.
\]

Then

\[
B(S_X,\Phi_X)-B(S_Y,\Phi_Y)
=
B(S_X,\delta\Phi)
+
B(\delta S,\Phi_Y),
\]

and

\[
S_Xr_X-S_Yr_Y
=
S_X\delta r+\delta S\,r_Y.
\]

Therefore

## Theorem D102.3 — Material pair-adjoint increment equation

\[
\boxed{
\begin{aligned}
\frac d{ds}\delta\Phi
={}&
-\nu\,\delta(\Delta\Phi)
+B(S_X,\delta\Phi)
+B(\delta S,\Phi_Y)
\\
&+
2S_X\delta r
+
2\delta S\,r_Y.
\end{aligned}
}
\tag{4.1}
\]

The pair increment is generated/rotated by:

1. backward diffusion / second-gradient mismatch;
2. action on the existing pair increment;
3. strain increment \(\delta S\);
4. nonlocal adjoint-Riesz increment \(\delta r\).

Thus \(\delta\Phi_X\) is not a passive fixed detector tensor.

---

# 5. Zero pair increment is not invariant

If

\[
\delta\Phi=0
\]

at one time, (4.1) gives

\[
\boxed{
\frac d{ds}\delta\Phi
=
-\nu\delta(\Delta\Phi)
+
B(\delta S,\Phi_Y)
+
2S_X\delta r
+
2\delta S\,r_Y.
}
\tag{5.1}
\]

Thus exact pairwise adjoint equality is immediately destroyed unless a nontrivial compatibility relation holds among:

- \(\delta S\);
- \(\delta r\);
- viscous second gradients.

---

# 6. No generic invariant detector half-space

Fix a trace-free tensor detector \(G\).

One might hope the adjoint evolution preserves

\[
G:\Phi\ge0.
\]

This is false already for the local operator.

Take

\[
G=\operatorname{diag}(1,-1,0),
\]

\[
\Phi_0=\operatorname{diag}(1,1,-2).
\]

Then

\[
G:\Phi_0=0.
\]

For

\[
S=G,
\]

\[
L_S(\Phi_0)=2G,
\]

and

\[
G:L_S(\Phi_0)=4>0.
\]

For

\[
S=-G,
\]

\[
G:L_S(\Phi_0)=-4<0.
\]

Therefore

## Theorem D102.4 — No local invariant half-space

There is no universal detector half-space

\[
\{\Phi:G:\Phi\ge0\}
\]

preserved by the admissible local trace-free strain action.

The full adjoint Riesz term adds further nonlocal mixing.

---

# 7. Adjoint tensor-direction equation

Whenever

\[
\Phi\neq0,
\]

write

\[
\widehat\Phi=\frac{\Phi}{|\Phi|}.
\]

Let

\[
P_{\widehat\Phi^\perp}
\]

be orthogonal projection in the five-dimensional tensor space \(\mathrm{Sym}_0(3)\).

From (3.2),

## Theorem D102.5 — Adjoint angular velocity

\[
\boxed{
D_s\widehat\Phi
=
\frac1{|\Phi|}
P_{\widehat\Phi^\perp}
\left[
-\nu\Delta\Phi
+
L_S(\Phi)
+
2S\mathcal T_0^*\Phi
\right].
}
\tag{7.1}
\]

Define

\[
\boxed{
\Omega_\Phi
=
\frac1{|\Phi|}
\left|
P_{\widehat\Phi^\perp}
\left[
-\nu\Delta\Phi
+
L_S(\Phi)
+
2S\mathcal T_0^*\Phi
\right]
\right|.
}
\tag{7.2}
\]

If

\[
\Omega_\Phi=0,
\]

the adjoint tensor direction is an instantaneous eigen-direction of the full defect-adjoint operator.

---

# 8. Zero angular action normal form

On an interval \(I\), if

\[
\Omega_\Phi\equiv0,
\]

then

\[
\boxed{
-\nu\Delta\Phi
+
L_S(\Phi)
+
2S\mathcal T_0^*\Phi
=
\beta(s,x)\Phi
}
\tag{8.1}
\]

for some scalar \(\beta\).

Thus zero adjoint angular action is the nonlocal tensor-ray condition

\[
\boxed{
\Phi
\text{ remains on one ray under the adjoint defect operator.}
}
\]

Call this

\[
\boxed{
\mathsf K_{\rm adj\mbox{-}eig}.
}
\]

---

# 9. Transport–Riesz integrand as an angular observable

At a pair \((x,y)\), define

\[
\boxed{
G_{xy}
=
[\delta_{xy}u\cdot\nabla K_0(x-y)]
\in\mathrm{Sym}_0(3).
}
\tag{9.1}
\]

Then the generic D101 finite-lag TR integrand is

\[
\boxed{
h_{xy}
=
(G_{xy}:\delta\Phi_X)\,\delta q.
}
\tag{9.2}
\]

If all three factors are nonzero, write

\[
\cos\theta_{xy}
=
\frac{G_{xy}:\delta\Phi_X}
{|G_{xy}||\delta\Phi_X|}.
\]

Then

\[
\boxed{
h_{xy}
=
|G_{xy}|
|\delta\Phi_X|
|\delta q|
\operatorname{sgn}(\delta q)
\cos\theta_{xy}.
}
\tag{9.3}
\]

The TR sign is therefore a joint amplitude–angle–scalar-sign condition.

---

# 10. Regular pair-cylinder extraction

The principal-value kernel is singular.

D102 therefore does **not** infer pointwise sign directly from the total PV integral.

Split the pair domain into normalized pair annuli

\[
\sigma_j\le|x-y|\le\Sigma_j.
\]

If no fixed regular pair cylinder carries a definite fraction of the recurrent signed TR source, then the source is escaping through:

- shrinking pair scale;
- principal-value concentration;
- tail pair scale;
- path-profile lack of tightness.

Record this as

\[
\boxed{
R_{\rm PV/scale}
\vee
R_{\rm path/fib}
\vee
R_{\rm state}
\vee
R_{\rm crit}.
}
\tag{10.1}
\]

D102 studies the complementary regular pair-cylinder branch.

---

# 11. Positive TR integral forces positive pair occupancy

Normalize one selected regular pair cylinder to total pair measure \(1\).

Assume compact bounds

\[
|G_{xy}|\le M_G,
\]

\[
|\delta\Phi_X|\le M_\Phi,
\]

\[
|\delta q|\le M_q.
\]

Then

\[
|h_{xy}|
\le
M:=M_GM_\Phi M_q.
\]

Suppose

\[
\int h_{xy}\,d\mu_{\rm pair}
\ge
c_{\rm TR}>0.
\]

Set

\[
A_+
=
\{h_{xy}\ge c_{\rm TR}/2\}.
\]

Then

\[
c_{\rm TR}
\le
M\mu(A_+)
+
\frac{c_{\rm TR}}2[1-\mu(A_+)].
\]

Hence

## Theorem D102.6 — Positive pair occupancy

\[
\boxed{
\mu(A_+)
\ge
\frac{c_{\rm TR}}{2M-c_{\rm TR}}
>0.
}
\tag{11.1}
\]

Thus the TR source cannot be supported only by arbitrarily sparse pair states on a compact bounded-amplitude cylinder.

---

# 12. Oriented angular cone

On \(A_+\),

\[
h_{xy}\ge c_{\rm TR}/2.
\]

Split \(A_+\) by the sign of \(\delta q\), and keep one sign cell with at least half the occupancy.

Fix

\[
\sigma_q=\operatorname{sgn}(\delta q).
\]

Then

\[
\boxed{
\sigma_q\cos\theta_{xy}
\ge
\frac{c_{\rm TR}}{2M_GM_\Phi M_q}
=:
\eta_\theta>0
}
\tag{12.1}
\]

on a positive-measure pair subset.

Thus the fixed-sign TR branch forces the strict tensor-angle cone

\[
\boxed{
\mathcal C_{\rm ang}
=
\left\{
(G,\Delta\Phi,c):
\operatorname{sgn}(c)
\frac{G:\Delta\Phi}{|G||\Delta\Phi|}
\ge\eta_\theta
\right\}.
}
\tag{12.2}
\]

This is the local geometric meaning of the third-order copula lock.

---

# 13. Finite angular-cell recurrence

Cover the compact normalized pair-state space by finitely many cells resolving:

- pair direction \(z/|z|\);
- normalized transport tensor \(G/|G|\);
- normalized adjoint increment direction \(\delta\Phi/|\delta\Phi|\);
- sign of \(\delta q\);
- amplitude bands.

Because \(\mathcal C_{\rm ang}\) has positive pair occupancy on every selected recurrent TR event, one cell carries a fixed fraction of that occupancy.

Across the positive-density generation set, finite pigeonholing gives:

## Theorem D102.7 — Recurrent oriented adjoint pair cell

There exists one fixed pair cell \(\mathfrak c_*\) such that:

1. \(\mathfrak c_*\subset\mathcal C_{\rm ang}\);
2. \(\mathfrak c_*\) recurs on a positive-density generation subsequence;
3. its pair-space occupancy is uniformly positive.

Thus the D101 abstract third-order copula becomes an explicit recurrent oriented angular pair state.

---

# 14. Why no static symmetry argument closes it

A fixed-sign angular pair state is not ruled out by:

- zero barycenter;
- sign-symmetric velocity increments;
- Kelvin second-moment lock;
- pairwise marginal information.

D101 already gave a parity-copula counterexample.

D102 adds the dynamical fact that even at \(G:\Phi=0\), local strain may push the adjoint test to either side.

So there is no generic fixed tensor reflection or half-space maximum principle forcing angular cancellation.

The remaining lock is genuinely dynamical/path-dependent.

---

# 15. Adjoint phase-lock versus angular action

For a recurrent source cell, follow the pulled-back test over its fixed lag interval.

Define the angular action

\[
\boxed{
\mathcal A_{\rm adj}
=
\int_I\Omega_\Phi\,ds.
}
\tag{15.1}
\]

There are two exact possibilities:

### A. positive angular action

\[
\boxed{
\mathcal A_{\rm adj}>0.
}
\tag{15.2}
\]

### B. adjoint eigen-lock

\[
\boxed{
\mathcal A_{\rm adj}=0
}
\]

and therefore

\[
\boxed{
-\nu\Delta\Phi
+
L_S(\Phi)
+
2S\mathcal T_0^*\Phi
=
\beta\Phi.
}
\tag{15.3}
\]

If a compact recurrent subfamily stays a positive distance from the eigen-lock set, continuity/compactness upgrades (15.2) to a uniform gap

\[
\boxed{
\mathcal A_{\rm adj}\ge c_{\rm adj}>0.
}
\tag{15.4}
\]

Without that separation one must retain the eigen-lock limit as a genuine alternative.

Therefore

## Theorem D102.8 — Adjoint phase dichotomy

\[
\boxed{
\mathsf C_{2+3}^{\ell_*}
\Longrightarrow
\mathsf A_{\rm adj}>0
\vee
\mathsf K_{\rm adj\mbox{-}eig}
\vee
R_{\rm PV/scale}
\vee
R_{\rm path/fib}
\vee
R_{\rm state}
\vee
R_{\rm crit}.
}
\tag{15.5}
\]

---

# 16. Zero-lag relation to D65–68

When

\[
\ell_*=0
\]

and

\[
\Phi_X=E_p,
\]

Round38 pressure self-commutator cancellation reduces the test increment to the strain-cofactor sector.

D65 closes every factorwise zero mechanism.

D66 reduces exact silence to the two-stress \(4:1\) correlation manifold.

D67–68 show the strongest aligned self-lock geometries are highly rigid: only two axisymmetric spectral modes avoid intrinsic cofactor self-rotation, and full gradient integrability removes those as nontrivial isotropic-covariance recurrent equality states.

Thus the zero-lag branch already strongly favors real cofactor-shape action over a static tensor axis.

D102 does **not** transplant that conclusion automatically to generic \(\ell_*\neq0\), because the pulled-back adjoint test is not the instantaneous cofactor.

---

# 17. External commutator calibration

Modern Riesz-commutator results reinforce the methodological choice here.

Generic Riesz-type transport commutator control retains a sharp velocity-regularity burden; in general a BMO gradient bound cannot replace the standard Lipschitz-type control, though defective estimates exist near the almost-Lipschitz threshold.

So D102 does not try to close the recurrent TR branch by a generic soft commutator estimate.

Instead it exploits the special recurrent adjoint pair state.

Likewise Yu's critical filtered-vorticity work supplies cylindrical Young profiles for velocity increments, but does not automatically furnish the enlarged adjoint/path tuple required here.

Thus path-profile/fiber escape remains a real interface condition.

---

# 18. Updated late compact normal form

D101 gave

\[
\boxed{
\mathsf C_{2+3}^{\ell_*}.
}
\]

D102 refines it to the dynamically propagated oriented copula

\[
\boxed{
\mathsf C_{\rm adj\mbox{-}copula}^{\ell_*}
}
\]

with:

1. fixed Kelvin second-moment sign;
2. fixed lag;
3. fixed TR source sign;
4. fixed regular pair-scale cell;
5. positive occupancy of one oriented tensor-angle cone;
6. backward adjoint evolution governed by (3.1);
7. either positive adjoint angular action or an adjoint eigen-lock kernel.

---

# 19. Status ledger

## PROVED this round

### D102-P1 — exact adjoint of the X72 strain/Riesz linear operator.

### D102-P2 — exact backward X72 adjoint equation.

### D102-P3 — exact material pair-increment adjoint equation.

### D102-P4 — zero pair increment is not generically invariant.

### D102-P5 — no universal local detector half-space is invariant under trace-free strain action.

### D102-P6 — exact adjoint tensor-direction/angular-velocity equation.

### D102-P7 — zero angular action is an explicit nonlocal adjoint eigen-lock condition.

### D102-P8 — on a regular compact pair cylinder, fixed positive TR source forces uniformly positive pair occupancy.

### D102-P9 — positive TR source forces a strict oriented tensor-angle cone after fixing \(\delta q\) sign.

### D102-P10 — finite pair-state pigeonholing yields one recurrent oriented angular cell.

### D102-P11 — generic finite-lag adjoint lock cannot be reduced to D65–68 instantaneous cofactor geometry without an additional adjoint-lock bridge.

### D102-P12 — the late compact path-copula survivor splits into positive adjoint angular action or one explicit adjoint eigen-lock normal form.

---

# 20. What is NOT proved

D102 does not prove:

- the adjoint eigen-lock kernel is empty;
- positive adjoint angular action has a finite global capacity;
- a regular pair-scale cylinder exists if PV mass concentrates at vanishing pair scale;
- Yu's velocity Young profile automatically lifts to the full adjoint path tuple;
- generic finite-lag \(\Phi_X\) equals the instantaneous X72 cofactor/defect state;
- the recurrent oriented pair cell is incompatible with Navier–Stokes dynamics;
- global Navier–Stokes regularity.

The remaining problem is now an **adjoint eigen-lock / angular-action rigidity problem**.

---

# 21. STOP-D102

\[
\boxed{
\begin{minipage}{0.94\linewidth}
The D101 Kelvin/TR second–third moment lock does not imply a static sign constraint on the pulled-back X72 test. The exact backward adjoint equation is
\[
-\partial_s\Phi
=
\nu\Delta\Phi
+
u\cdot\nabla\Phi
-
L_S(\Phi)
-
2S\mathcal T_0^*\Phi,
\]
and along forward material paths
\[
D_s\Phi
=
-\nu\Delta\Phi
+
L_S(\Phi)
+
2S\mathcal T_0^*\Phi.
\]
Its pair increment is driven by the existing adjoint increment, strain increment, nonlocal adjoint-Riesz increment, and viscous second gradients. There is no generic detector half-space maximum principle: at \(G:\Phi=0\), admissible local strains \(S=\pm G\) push the detector projection to opposite signs. Therefore fixed-sign transport–Riesz recurrence cannot be interpreted as pointwise adjoint sign preservation. On the complementary regular pair-scale branch, however, a fixed positive TR source and compact amplitude bounds force a positive-measure pair set on which the transport tensor \(G_{xy}=[\delta u\cdot\nabla K_0]\), the adjoint increment \(\delta\Phi_X\), and the sign of \(\delta q\) lie in one strict oriented angular cone. Finite pair-state pigeonholing yields one recurrent angular cell with uniformly positive occupancy. Following the pulled-back test across the fixed lag gives a new exact dichotomy: either the adjoint direction pays positive angular action, or it lies in the explicit nonlocal tensor-ray eigen-lock kernel
\[
-\nu\Delta\Phi+L_S(\Phi)+2S\mathcal T_0^*\Phi=\beta\Phi.
\]
Thus the final compact survivor is no longer an abstract third-order copula; it is a dynamically propagated oriented adjoint-copula state.
\end{minipage}
}
\]

---

# 22. Next autonomous step

## DCRP103 / X72-R86 — Adjoint Eigen-Lock Compatibility / Tensor-Ray Rigidity

**Working title**

> **Can a Nonzero Trace-Free Backward X72 Test Remain on One Tensor Ray under \(L_S+2S\mathcal T_0^*\) while its pair increments stay inside the recurrent TR angular cone?**

Primary tasks:

1. start from
   \[
   -\nu\Delta\Phi+L_S(\Phi)+2S\mathcal T_0^*\Phi=\beta\Phi;
   \]
2. in the inviscid compact profile branch, diagonalize \(S\);
3. solve the five-dimensional tensor-ray algebra;
4. separate:
   - diagonal/coaxial adjoint rays;
   - off-diagonal shear rays;
   - nonlocal \(r=\mathcal T_0^*\Phi\) locking;
5. impose incompressibility and X72 carrier geometry;
6. test whether the recurrent TR angular cone can persist on each ray family;
7. if eigen-lock is excluded away from finitely many rays, obtain a compact-class angular-action gap;
8. otherwise isolate the finite tensor-ray normal forms.

Desired endpoint:

\[
\boxed{
\mathsf K_{\rm adj\mbox{-}eig}
\Longrightarrow
\text{finite tensor-ray normal forms}
\vee
R_{\rm state}
\vee
R_{\rm crit}.
}
\]

**End checkpoint:** DCRP102 / X72-R85.
