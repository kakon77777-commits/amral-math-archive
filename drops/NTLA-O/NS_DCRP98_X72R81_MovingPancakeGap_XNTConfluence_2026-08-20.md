# DCRP98 / X72-R81 — Moving-Pancake Scope Repair, Reverse-Pancake Phase, and Dual-Lock Confluence into X/N/T

**Series:** Independent Navier–Stokes Research Series / X72 Bridge  
**Date:** 2026-08-20  
**Status:** proof-development checkpoint / dual-lock-to-X72 compiler round  
**Immediate predecessor:** `NS_DCRP97_X72R80_DualLockPSD_PancakeGap_2026-08-20.md`

## Primary internal dependencies

- DCRP40 — rank-two vorticity covariance / Floquet normal compression.
- DCRP41 — planar covariance-shape disk / moving pancake-jet normal form.
- DCRP50 — exact-affine central pancake NO-GO / three-component X72 response.
- DCRP60 — formal rank-two equality closure into \(X\vee N\vee T\).
- DCRP79–80 — late X72/T noncompactness compiler.
- DCRP96–97 — sign-coherent SGS Kelvin-slip / dual-lock covariance / frozen pancake gap.

## Fresh primary-source calibration

- R. Yu, *Filtered Vortex Stretching and Subgrid Defects for the Three-Dimensional Navier–Stokes Equations*, arXiv:2606.27560 (2026).
- P. Constantin, M. Ignatova, V. Vicol, *On putative self-similarity for incompressible 3D Euler*, arXiv:2602.17570 (2026).
- E. Miller, *A locally anisotropic regularity criterion for the Navier–Stokes equation in terms of vorticity*, arXiv:2002.02152.

No external regularity criterion is imported into the proof.

No full Navier–Stokes regularity theorem is claimed.

---

# 0. Executive result

D97 proved that a positive-forward D96 dual-lock covariance cannot converge to the **frozen** canonical pancake tensor

\[
A_*
=
\frac{c_\gamma}{2}P_{n^\perp}
-
c_\gamma n\otimes n.
\]

That statement is correct.

But the stronger statement

> positive forward dual lock stays uniformly away from the entire D41 pancake equality manifold

was too strong.

D41's actual zero-shape equality manifold is the **moving pancake jet**

\[
\boxed{
A_{\rm pan}(s)
=
a(s)
\left[
P_{n^\perp}
-
2n\otimes n
\right]
-
\left[
n'\otimes n
+
n\otimes n'
\right],
}
\tag{0.1}
\]

with the exact periodic balance

\[
\boxed{
\frac1{S_0}
\int_0^{S_0}
a(s)\,ds
=
\frac{c_\gamma}{2}
>0.
}
\tag{0.2}
\]

Thus \(a(s)\) may fluctuate and may in principle become negative on part of the cycle.

Let \(Q\ge0\) be the D96 velocity-increment covariance and assume exact increment–vorticity plane lock

\[
\boxed{
Qn=0.
}
\tag{0.3}
\]

Then the moving-plane cross terms in (0.1) do not pair with \(Q\):

\[
(n'\otimes n+n\otimes n'):Q=0.
\]

Therefore

# Main moving-pancake work identity

\[
\boxed{
-A_{\rm pan}:Q
=
-a(s)\operatorname{tr}Q.
}
\tag{0.4}
\]

So positive SGS forward work **can** coexist algebraically with zero planar shape action if it occurs during a temporary

\[
\boxed{
a(s)<0
}
\]

reverse-pancake phase.

This is the missing D97 correction.

However this does **not** create a new terminal mechanism.

D50 proves that on the central \(c=1/2\) rank-two response branch, a nonzero planar-vorticity state cannot have the actual local strain equal to the pointwise canonical moving pancake jet on an open flat patch. Every active central survivor must instead carry at least one of:

1. non-affine strain relative to the D41 moving pancake;
2. covariance/core turnover or structured cancellation;
3. a nonzero remaining X72 pressure-response defect;
4. the nonlinear perfect-response wave–pseudo-eikonal branch.

D60 subsequently closes the full strongest rank-two equality package: a nonzero global continuation cannot remain simultaneously in fixed-plane/zero-shape/perfect-response/zero-residual equality and must enter

\[
\boxed{
X\vee N\vee T.
}
\tag{0.5}
\]

Therefore D98 obtains the compiler-level conclusion

\[
\boxed{
\mathsf C_{\rm dual}
\Longrightarrow
R_{\rm IV\mbox{-}unlock}
\vee
X
\vee
N
\vee
T
\vee
R_{\rm state}
\vee
R_{\rm crit}.
}
\tag{0.6}
\]

Since persistent increment–vorticity carrier unlock is itself a covariance/state transition,

\[
R_{\rm IV\mbox{-}unlock}
\subseteq
R_{\rm state},
\]

the genuinely compact carrier-locked dual-lock conveyor has no independent terminal status:

\[
\boxed{
\mathsf C_{\rm dual}^{\rm compact,locked}
\Longrightarrow
X\vee N\vee T.
}
\tag{0.7}
\]

D98 therefore reconnects the entire late Kelvin/SGS phase-slip chain to the older X72/rank-two compiler.

---

# 1. Scope repair from D97

D97 used the frozen tensor

\[
A_*
=
\frac{c_\gamma}{2}
P
-
c_\gamma n\otimes n
\]

as a convenient equality anchor.

This is the unique frozen-affine periodic rank-two tensor.

But D41 proves that zero covariance-shape action allows the larger time-dependent family

\[
A_{\rm pan}(s)
=
a(s)(P-2n\otimes n)
-
(n'\otimes n+n\otimes n').
\]

The full-cycle constraint is only

\[
\langle a\rangle
=
c_\gamma/2.
\]

Therefore D97's fixed-tensor distance

\[
\|S-A_*\|
\]

does not by itself measure distance from the entire moving-pancake manifold.

This is corrected in D98.

---

# 2. D41 shape decomposition

Let \(B_\omega\) be the rank-two vorticity covariance with normal \(n\).

In the Fermi–Walker frame of \(n^\perp\), D41 writes the normalized planar covariance shape as

\[
C
=
\frac12(I_2+Z),
\]

with

\[
Z=
\begin{pmatrix}
z_1&z_2\\
z_2&-z_1
\end{pmatrix},
\qquad
|z|<1.
\]

Let the in-plane deviatoric affine strain be

\[
S_{\rm sh}
=
\begin{pmatrix}
s_1&s_2\\
s_2&-s_1
\end{pmatrix}.
\]

Then the exact shape equation is

\[
\boxed{
z'
=
2(I_2-zz^T)s.
}
\tag{2.1}
\]

Hence

\[
\boxed{
s
=
\frac12
(I_2-zz^T)^{-1}z'.
}
\tag{2.2}
\]

The shape action is

\[
\boxed{
|S_{\rm sh}|_F^2
=
\frac{(r')^2}{2(1-r^2)^2}
+
2r^2(\theta')^2.
}
\tag{2.3}
\]

Thus:

- \(S_{\rm sh}=0\) iff planar covariance shape is static;
- nonzero planar deviatoric affine strain is exactly covariance-shape motion.

The zero-shape branch is precisely the moving pancake family.

---

# 3. Exact contraction with a plane-locked increment covariance

Let

\[
Q=Q^T\ge0,
\qquad
Qn=0,
\]

and let

\[
\tau=\operatorname{tr}Q>0.
\]

Use

\[
A_{\rm pan}
=
a(P-2nn)
-
(n'n+nn').
\]

Then

\[
P:Q=\tau,
\]

\[
(n\otimes n):Q=n^TQn=0,
\]

and

\[
(n'\otimes n):Q
=
n'^TQn
=
0,
\]

\[
(n\otimes n'):Q
=
n^TQn'
=
0.
\]

Therefore:

## Theorem D98.1 — Moving-Pancake SGS Work

\[
\boxed{
-A_{\rm pan}:Q
=
-a\tau.
}
\tag{3.1}
\]

This is exact.

---

# 4. Forward work requires a reverse-pancake phase on the pure affine branch

Suppose the actual resolved strain equals the moving pancake:

\[
S=A_{\rm pan}.
\]

If at an active phase-slip event

\[
\Pi_{\rm SGS}
=
-S:Q
\ge
c_E>0,
\]

then:

\[
-a\tau
\ge
c_E.
\]

Therefore:

## Corollary D98.2 — Reverse-Pancake Requirement

\[
\boxed{
a
\le
-\frac{c_E}{\tau}
<0.
}
\tag{4.1}
\]

So the zero-shape pure-affine forward-SGS event must occur while the plane is locally compressive and the normal is locally extensional—the sign-reverse of the mean pancake geometry.

---

# 5. Window-integrated version

Let \(I\subset[0,S_0]\) be one normalized recurrence window.

Assume:

\[
Qn=0,
\]

\[
S=A_{\rm pan},
\]

and

\[
0<\tau(s)\le\tau_+.
\]

If

\[
\int_I
\Pi_{\rm SGS}(s)\,ds
\ge
W_0>0,
\]

then

\[
-\int_I
a(s)\tau(s)\,ds
\ge
W_0.
\]

Hence:

## Theorem D98.3 — Negative-Pancake Action

\[
\boxed{
\int_I
a_-(s)\,ds
\ge
\frac{W_0}{\tau_+}.
}
\tag{5.1}
\]

where

\[
a_-=\max\{-a,0\}.
\]

This is a scale-normalized reverse-pancake action.

---

# 6. Reverse phase implies scalar reproduction excess

D41 gives

\[
\frac1{S_0}
\int_0^{S_0}a\,ds
=
m
:=
\frac{c_\gamma}{2}
>0.
\]

Write

\[
a=m+\widetilde a,
\qquad
\int_0^{S_0}\widetilde a\,ds=0.
\]

On the set where \(a<0\),

\[
|a-m|
=
m+a_-
\ge
a_-.
\]

Thus from D98.3,

\[
\int_I
|a-m|\,ds
\ge
\frac{W_0}{\tau_+}.
\]

By Cauchy–Schwarz,

\[
\boxed{
\int_0^{S_0}
|a-m|^2ds
\ge
\frac{
W_0^2
}{
\tau_+^2|I|
}.
}
\tag{6.1}
\]

Therefore

\[
\int_0^{S_0}a^2ds
=
m^2S_0
+
\int_0^{S_0}|a-m|^2ds
\]

satisfies

## Theorem D98.4 — Reverse-Phase Reproduction Excess

\[
\boxed{
\int_0^{S_0}
a^2ds
\ge
\frac{c_\gamma^2}{4}S_0
+
\frac{
W_0^2
}{
\tau_+^2|I|
}.
}
\tag{6.2}
\]

D41's moving-pancake reproduction action

\[
\int|A_{\rm pan}|_F^2
=
6\int a^2
+
2\int|n'|^2
\]

therefore acquires a strict excess beyond the Jensen minimum whenever a pure-affine forward phase exists.

This is a normalized visibility statement, not a physical depletion contradiction.

---

# 7. Periodic sign reversal forces temporal variation

Let

\[
a_{\min}
=
\min a,
\qquad
a_{\max}
=
\max a.
\]

D98.2 gives

\[
a_{\min}
\le
-\frac{c_E}{\tau_+}
\]

for a pointwise event.

The positive mean gives

\[
a_{\max}
\ge
m
=
c_\gamma/2.
\]

For a periodic absolutely continuous scalar,

\[
\operatorname{TV}(a)
\ge
2(a_{\max}-a_{\min}).
\]

Therefore:

## Theorem D98.5 — Reverse-Pancake Phase-Front Action

\[
\boxed{
\int_0^{S_0}|a'|ds
\ge
c_\gamma
+
\frac{2c_E}{\tau_+}.
}
\tag{7.1}
\]

The reverse-pancake survivor is necessarily a nontrivial temporal phase-front, not a stationary equality tensor.

Again, this is not yet a global physical budget.

---

# 8. Actual strain decomposition

The actual local strain need not equal the affine moving pancake.

Write:

\[
\boxed{
S
=
A_{\rm pan}
+
S_{\rm sh}
+
E.
}
\tag{8.1}
\]

Here:

- \(A_{\rm pan}\) is the D41 zero-shape moving pancake determined by scalar \(a\) and plane motion \(n'\);
- \(S_{\rm sh}\) is the in-plane deviatoric affine shape strain reconstructed by D41 from \(z'\);
- \(E\) is the remaining non-affine/local strain residual.

For plane-locked \(Q\),

\[
\boxed{
\Pi_{\rm SGS}
=
-a\tau
-
S_{\rm sh}:Q
-
E:Q.
}
\tag{8.2}
\]

Thus positive forward work must be financed by at least one of:

\[
\boxed{
\text{reverse pancake}
\vee
\text{planar shape motion}
\vee
\text{non-affine strain}.
}
\tag{8.3}
\]

If \(Qn\neq0\), there is additionally the D97 increment–vorticity unlock branch.

---

# 9. Planar shape motion is not hidden

D41's exact inversion gives

\[
S_{\rm sh}
=
\frac12
(I_2-zz^T)^{-1}z'
\]

in disk coordinates.

Therefore a fixed lower bound on

\[
|S_{\rm sh}|
\]

forces a fixed covariance-shape action.

On a compact rank-two class away from rank-one collapse,

\[
|z|\le1-\eta,
\]

the inverse is uniformly bounded and

\[
|z'|
\asymp
|S_{\rm sh}|.
\]

Thus:

\[
\boxed{
\text{persistent planar shape financing}
\Longrightarrow
\text{persistent rank-two covariance shape motion}.
}
\tag{9.1}
\]

This is already an exit from the zero-shape equality hypothesis used by the D40–60 rigid pancake package.

At the terminal compiler level it is a covariance/state-transition coordinate unless the full periodic shape motion is retained and analyzed dynamically.

---

# 10. Increment–vorticity unlock is a state transition

D97 defines

\[
\theta_Q
=
\frac{n^TQn}{\operatorname{tr}Q}.
\]

If

\[
\theta_Q\ge\theta_0>0
\]

on the recurring compact branch, the velocity-increment covariance has a persistent normal component relative to the rank-two vorticity plane.

There is no theorem identifying this state with the D40 rank-two carrier.

Therefore:

## Theorem D98.6 — Carrier-Unlock Absorption

\[
\boxed{
R_{\rm IV\mbox{-}unlock}
\subseteq
R_{\rm state}
}
\tag{10.1}
\]

at the late compiler level.

The plane-locked branch is the only one that can remain inside the old rank-two equality architecture.

---

# 11. D50 exact-affine central NO-GO

D50 studies the central mixed-cofactor-invisible response:

\[
c=B_q=\frac12.
\]

Its pointwise canonical fixed-plane pancake strain is

\[
A_{\rm pan}
=
a(s)\operatorname{diag}(1,1,-2).
\]

D50 proves:

\[
\boxed{
S=A_{\rm pan}
+
\text{nonzero planar vorticity}
+
\text{central perfect response}
}
\]

cannot hold on an open central flat patch.

The exact constitutive system forces the planar vorticity to vanish.

Therefore every nonzero active central survivor must carry at least one of:

\[
\boxed{
E\neq0
\vee
T
\vee
X
\vee
\text{nonlinear perfect-response wave--pseudo-eikonal state}.
}
\tag{11.1}
\]

So the reverse-pancake pure-affine phase is not an independent perfect-response escape.

---

# 12. D60 global rank-two equality closure

D60 defines the strongest rank-two equality package by:

- strict Type-II DSS;
- nonzero recurrent rank-two vorticity covariance;
- no rank-one collapse;
- no rank-three lift;
- fixed vorticity plane / zero plane-motion action;
- zero covariance-shape action;
- gauge-flat scalar connection;
- perfect central scalar response;
- perfect local X72 pressure response;
- zero covariance residual.

D60 proves:

## Theorem D60.1

A nonzero global continuation cannot satisfy all equality hypotheses.

Every nonzero continuation enters

\[
\boxed{
X
\vee
N
\vee
T.
}
\tag{12.1}
\]

Here:

- \(X\) = X72 pressure-response / realizability visibility;
- \(N\) = positive non-affine vorticity-stretching channel;
- \(T\) = covariance/material turnover channel.

D98 uses this theorem as a **compiler**, not as a new proof of any individual local implication.

---

# 13. Main D98 confluence theorem

Assume the D96/D97 compact phase-slip forward-work branch with:

1. bounded critical reservoirs;
2. nonzero rank-two vorticity carrier;
3. no fiber/concentration escape;
4. fixed relative filter scale;
5. material carrier compactness;
6. positive recurring SGS forward work;
7. positive recurring Kelvin-slip detector.

Then:

- if increment covariance unlocks from the vorticity plane:
  \[
  R_{\rm state};
  \]
- if the vorticity rank/plane/shape leaves the D40–41 equality package:
  \[
  R_{\rm state}\vee T;
  \]
- if the branch remains inside the strongest rank-two equality package:
  D60 forces
  \[
  X\vee N\vee T.
  \]

Therefore:

## Theorem D98.7 — Dual-Lock / XNT Confluence

\[
\boxed{
\mathsf C_{\rm dual}
\Longrightarrow
X
\vee
N
\vee
T
\vee
R_{\rm state}
\vee
R_{\rm crit}.
}
\tag{13.1}
\]

In particular, on the compact carrier-locked bounded-reservoir branch:

\[
\boxed{
\mathsf C_{\rm dual}^{\rm compact,locked}
\Longrightarrow
X
\vee
N
\vee
T.
}
\tag{13.2}
\]

There is no independent compact dual-lock terminal.

---

# 14. Relation to the D97 frozen equality gap

D97's theorem remains useful.

It gives the local quantitative statement

\[
\frac{3c_\gamma}{2}\theta_Q
+
\|S-A_*\|_{\rm op}
\ge
\frac{c_\gamma}{2}
+
\frac{c_E^*}{\tau}.
\]

D98 clarifies its meaning:

\[
\|S-A_*\|
\]

may come from:

1. moving-pancake scalar modulation \(a-c_\gamma/2\);
2. plane motion \(n'\);
3. planar covariance-shape strain;
4. non-affine strain \(E\).

Only the last three are immediate departures from the moving-pancake equality family.

The first is the reverse-pancake temporal phase identified in D98.

Thus D97 was a correct **frozen-state gap**, but not by itself a full **moving-manifold gap**.

---

# 15. The reverse-pancake branch is not discarded

D98 does not claim

\[
a(s)<0
\]

is impossible.

A periodic scalar with positive mean can certainly be negative on part of the cycle.

Therefore the correct result is not:

\[
\text{reverse pancake}
\Longrightarrow
\text{contradiction}.
\]

It is:

\[
\boxed{
\text{reverse pancake}
\Longrightarrow
\text{nontrivial temporal reproduction/pressure dynamics}.
}
\tag{15.1}
\]

If the branch additionally tries to remain:

- rank-two;
- zero-shape;
- turnover-free;
- X72-perfect;
- globally same-parent;

the old D50–60 closure removes the pure equality continuation.

So no new terminal name is required.

---

# 16. X72 role after D98

D98 does **not** prove a local inequality

\[
\|S-A_{\rm pan}\|
\lesssim
|E_p|.
\]

That would be unjustified.

Instead X72 appears through the already-established rank-two equality closure:

\[
\boxed{
\text{no }X
+
\text{no }N
+
\text{no }T
\Longrightarrow
\text{maximally rigid pancake equality package},
}
\]

and D50–60 show that no nonzero global continuation exists there.

Thus X72 is used as a **transverse observer coordinate**, exactly as intended by D60.

---

# 17. Relation to D79–80

D60's \(T\) branch is material/covariance turnover.

D79–80 later catalogued and absorbed material noncompactness into:

\[
R_{\rm tail}
\vee
R_{\rm fil}
\vee
R_{\rm state}
\vee
R_K.
\]

D81–91 subsequently reduced the Kelvin/tail/filamentation descendants back into finite-scale/state/critical coordinates.

Therefore D98's return to \(X\vee N\vee T\) does not reopen an uncontrolled geometric tree.

It reconnects the newest phase-slip branch to a previously finite compiler.

---

# 18. What has actually been closed

D98 removes the following independent terminal candidates:

- frozen pancake dual-lock cone;
- moving-pancake pure-affine forward-work escape;
- increment/vorticity plane unlock as a new geometry;
- reverse-pancake temporal phase as a new terminal.

The remaining branch is only:

\[
\boxed{
X
\vee
N
\vee
T
\vee
R_{\rm state}
\vee
R_{\rm crit}.
}
\]

This is an old finite proof frontier, not a new one created by the Kelvin-reset program.

---

# 19. Status ledger

## PROVED this round

### D98-P1 — D97 frozen-pancake transversality is corrected to the full moving-pancake manifold.

### D98-P2 — exact moving-pancake/plane-locked work identity:

\[
-A_{\rm pan}:Q
=
-a\,\operatorname{tr}Q.
\]

### D98-P3 — pure-affine positive forward work requires a reverse-pancake phase \(a<0\).

### D98-P4 — window-integrated forward work forces a positive negative-pancake action.

### D98-P5 — reverse-pancake work forces strict excess in the D41 scalar reproduction action.

### D98-P6 — pointwise reverse phase plus positive DSS mean forces nonzero temporal phase-front variation.

### D98-P7 — actual forward work decomposes into reverse-pancake, shape-motion, and non-affine-strain financing.

### D98-P8 — persistent increment–vorticity plane unlock is a state/covariance transition.

### D98-P9 — D50 excludes the nonzero pure-affine central perfect-response pancake.

### D98-P10 — D60 compiles any strongest rank-two equality continuation into \(X\vee N\vee T\).

### D98-P11 — the compact dual-lock phase-slip conveyor is not an independent terminal:

\[
\mathsf C_{\rm dual}^{\rm compact,locked}
\Longrightarrow
X\vee N\vee T.
\]

---

# 20. What is NOT proved

D98 does not prove:

- reverse-pancake phases are impossible;
- every non-affine strain gap gives positive \(N\) pointwise;
- every shape-action event is globally non-summable;
- \(X\), \(N\), or \(T\) is individually impossible;
- the old X/N/T recurrence loop is globally closed;
- global Navier–Stokes regularity.

The newest phase-slip/Young-profile branch has now **reconverged** to the old finite X72 frontier.

The next step should therefore not invent another local covariance geometry.

It should attack the recurrence of \(X/N/T\) using the new Kelvin-slip sidecar.

---

# 21. STOP-D98

\[
\boxed{
\begin{minipage}{0.94\linewidth}
D97 correctly excluded the frozen canonical pancake but overstated the conclusion if read as exclusion of the full D41 moving-pancake manifold. D41's zero-shape equality is
\[
A_{\rm pan}(s)
=
a(s)(P-2nn)
-(n'n+nn'),
\qquad
\langle a\rangle=c_\gamma/2>0.
\]
For a plane-locked increment covariance \(Qn=0\), the moving-plane terms are invisible to SGS energy transfer and
\[
-A_{\rm pan}:Q=-a\,\operatorname{tr}Q.
\]
Thus positive forward SGS work can occur inside zero shape-action only during a temporary reverse-pancake phase \(a<0\); it then forces a quantitative negative-pancake action, extra scalar reproduction action, and temporal phase-front variation. For the actual strain, forward work decomposes into reverse-pancake, covariance-shape, and non-affine-strain financing. Increment–vorticity carrier unlock is already a state transition. If the branch remains carrier-locked and inside the strongest rank-two equality package, D50 eliminates the nonzero pure-affine central pancake and D60 proves that every nonzero global continuation must exit into \(X\vee N\vee T\). Therefore the D96/D97 dual-lock phase-slip conveyor is not a new compact terminal: on the compact locked bounded-reservoir branch it necessarily reconverges to the pre-existing X72/non-affine-stretching/turnover compiler.
\end{minipage}
}
\]

---

# 22. Next autonomous step

## DCRP99 / X72-R82 — X/N/T Recurrence with the Kelvin-Slip Sidecar

**Working title**

> **Can the Old X/N/T Rank-Two Recurrence Loop Persist When Every Bounded Number of Generations Must Also Carry a Sign-Coherent Kelvin Phase Slip?**

Primary tasks:

1. start from:
   \[
   \mathsf C_{\rm dual}
   \Longrightarrow
   X\vee N\vee T;
   \]
2. use D95:
   \[
   \mathcal V_{\Gamma,+}^{\rm SGS}(N)\gtrsim N;
   \]
3. revisit the old D60–80 loop:
   \[
   N/T\rightarrow\text{finite supplier}\rightarrow\text{rank-two}\rightarrow X/N/T;
   \]
4. determine whether an \(N\) or \(T\) recurrence can remain sign-incoherent while the Kelvin sidecar is sign-coherent;
5. test whether the X branch can remain work/phase-slip orthogonal on the same finite state;
6. finite-pigeonhole the joint state:
   \[
   (\text{X/N/T type},\ \text{Kelvin-slip orientation});
   \]
7. seek a fixed positive-density **joint** recurrence coordinate;
8. if no contradiction results, isolate one final:
   \[
   \text{X72--Kelvin locked conveyor}.
   \]

Desired endpoint:

\[
\boxed{
\text{late compact survivor}
\Longrightarrow
\text{one joint X72--Kelvin finite-dimensional normal form}
\vee
R_{\rm state}
\vee
R_{\rm crit}.
}
\]

**End checkpoint:** DCRP98 / X72-R81.
