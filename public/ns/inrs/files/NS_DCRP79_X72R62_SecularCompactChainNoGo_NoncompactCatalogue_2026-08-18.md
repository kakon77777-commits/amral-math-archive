# DCRP79 / X72-R62 — Secular Shape Drift, Compact Infinite-Carrier NO-GO, and the Remaining Material Noncompactness Catalogue

**Series:** Independent Navier–Stokes Research Series / X72 Bridge  
**Date:** 2026-08-18  
**Status:** Proof-development checkpoint / infinite material-chain compactification round  
**Immediate predecessor:** `NS_DCRP78_X72R61_TiltPressure_CoherentReturnNoGo_2026-08-18.md`

**Primary internal dependencies**
- DCRP76 — \(2\gamma\) resonant infinite material conveyor
- DCRP77 — stretch-selection / first-crossing trichotomy
- DCRP78 — \(E_p=0\) moving-frame ODE and coherent-return NO-GO
- RMRM/DCRP same-parent bridge — material tail escape / filamentation / state-transition compactness failure alternatives

**External calibration searched before this round**
- Gregory Seregin, *On potential Type II blowups for the Navier-Stokes equations*, arXiv:2606.29468 — current Type-II analysis via Euler scaling and Liouville-type limits.
- Gregory Seregin, *A note on certain scenarios of Type II blowups of suitable weak solutions to the Navier-Stokes equations*, arXiv:2507.08733v2 — Euler-scaled Type-II scenario reduction.
- Runlong Yu, *A Structural Audit of Navier-Stokes Obstruction Calculus*, arXiv:2606.25341 — finite-scale obstruction/compactness audit context.

No theorem from these papers is imported into the new secular identities below.

No full Navier–Stokes regularity theorem is claimed.

---

# 0. Executive result

DCRP78 left the X-free dynamic T branch in the form

\[
\boxed{
\mathsf T_{\rm drift}
\ \vee\
\mathsf T_{\rm preselect}.
}
\]

The first branch is a single material carrier whose normalized strain/tilt shape never returns.

The second keeps selecting new pre-existing high-stretch material and pushes its origin upstream.

DCRP79 asks whether the first branch can nevertheless remain in a compact normalized state set forever.

It cannot.

The key observation is stronger than subsequence recurrence.

Inside the D78 pressure-perfect nonaligned resonant system

\[
E_p=0,
\]

the moving-frame shape variables satisfy

\[
\boxed{
\lambda'
=
2\rho^2-\lambda-\frac16m,
}
\]

\[
\boxed{
\frac{\rho'}{\rho}
=
a-1-\lambda,
}
\]

\[
\boxed{
a'
=
-2\rho^2+2b^2-a+\frac1{12}m,
}
\]

\[
\boxed{
b'
=
-(1+\lambda+2a)b,
}
\]

\[
\boxed{
m'
=
2(\lambda-1)m.
}
\]

Here:

- \(\lambda=\xi^\top S\xi\);
- \(\rho=|D_s\xi|>0\);
- \(a=u^\top Su\);
- \(b=u^\top Sv\);
- \(m=|\Omega|^2\).

Define two scalar shape functionals:

\[
\boxed{
F
=
a+\log\rho+\frac12\lambda,
}
\]

and, on \(b\neq0\),

\[
\boxed{
G
=
\log|b|+2\log\rho.
}
\]

Direct substitution gives two **exact secular laws**:

## Secular law I

\[
\boxed{
F'
=
-\rho^2
+
2b^2
-
1
-
\frac32\lambda.
}
\]

## Secular law II

\[
\boxed{
G'
=
-3(1+\lambda).
}
\]

Now impose the D76 resonant condition on every DSS material stage:

\[
\boxed{
\int_{nS_0}^{(n+1)S_0}\lambda\,ds
=
\gamma S_0.
}
\]

Then at the stroboscopic times

\[
s_N=NS_0,
\]

\[
\boxed{
G(s_N)-G(0)
=
-3(1+\gamma)NS_0.
}
\]

Thus, if the normalized nonaligned shape stays in a compact interior set

\[
\boxed{
0<\rho_-\le\rho(s)\le\rho_+<\infty,
}
\]

with \(a,\lambda\) uniformly bounded, then \(b\) decays exponentially from period to period.

Uniform within-period boundedness then gives

\[
\boxed{
\int_0^\infty b(s)^2\,ds<\infty.
}
\]

Now integrate the \(F\)-law over \(N\) periods:

\[
\boxed{
\begin{aligned}
F(s_N)-F(0)
={}&
-\int_0^{s_N}\rho^2ds
+
2\int_0^{s_N}b^2ds
\\
&-
\left(
1+\frac{3\gamma}{2}
\right)s_N.
\end{aligned}
}
\]

Discard the nonpositive \(-\int\rho^2\) term.

Since \(\int b^2<\infty\),

\[
\boxed{
F(s_N)
\le
C
-
\left(
1+\frac{3\gamma}{2}
\right)NS_0
\to-\infty.
}
\]

But in a compact interior shape class,

\[
a,\lambda,\log\rho
\]

are all uniformly bounded.

Contradiction.

Therefore:

## Main theorem

\[
\boxed{
\textbf{
an infinite \(E_p=0\), \(2\gamma\)-resonant material shape-drift chain cannot remain in any compact nonaligned normalized shape class.
}
}
\]

No recurrence-subsequence theorem is needed.

The chain is forced to leave compactness secularly.

---

# 1. Exact D78 pressure-perfect shape system

Use the D78 moving frame

\[
(\xi,u,v),
\]

with

\[
\rho=|D_s\xi|>0.
\]

For

\[
E_p=0,
\]

the shape system is

\[
\boxed{
\lambda'
=
2\rho^2-\lambda-\frac16m,
}
\tag{1.1}
\]

\[
\boxed{
\rho'
=
(a-1-\lambda)\rho,
}
\tag{1.2}
\]

\[
\boxed{
a'
=
-2\rho^2+2b^2-a+\frac1{12}m,
}
\tag{1.3}
\]

\[
\boxed{
b'
=
-(1+\lambda+2a)b,
}
\tag{1.4}
\]

\[
\boxed{
m'
=
2(\lambda-1)m.
}
\tag{1.5}
\]

The present round does not assume shape return.

---

# 2. First secular combination

Define

\[
F
=
a+\log\rho+\frac12\lambda.
\]

Differentiate.

Using (1.1)–(1.3):

\[
\begin{aligned}
F'
={}&
\left[
-2\rho^2+2b^2-a+\frac1{12}m
\right]
\\
&+
\left[
a-1-\lambda
\right]
\\
&+
\frac12
\left[
2\rho^2-\lambda-\frac16m
\right].
\end{aligned}
\]

All \(a\) and \(m\) terms cancel.

Thus:

## Theorem D79.1 — Exact Secular \(F\)-Law

\[
\boxed{
F'
=
-\rho^2
+
2b^2
-
1
-
\frac32\lambda.
}
\tag{2.1}
\]

This identity holds pointwise in material time.

---

# 3. Second secular combination

On an interval where \(b\neq0\), define

\[
G
=
\log|b|+2\log\rho.
\]

Then:

\[
\begin{aligned}
G'
&=
-(1+\lambda+2a)
+
2(a-1-\lambda)
\\
&=
-3-3\lambda.
\end{aligned}
\]

Therefore:

## Theorem D79.2 — Exact Secular \(G\)-Law

\[
\boxed{
G'
=
-3(1+\lambda).
}
\tag{3.1}
\]

If \(b=0\) at one time, (1.4) gives:

\[
\boxed{
b\equiv0
}
\]

along the whole connected material interval.

So the \(b=0\) branch is even simpler.

---

# 4. Stroboscopic resonant multiplier for \(b\)

Let

\[
s_n=nS_0.
\]

Assume the D76 local resonant-carrier law period by period:

\[
\boxed{
\int_{s_n}^{s_{n+1}}\lambda ds
=
\gamma S_0.
}
\tag{4.1}
\]

Integrate D79.2 over \(N\) periods:

\[
\boxed{
G(s_N)-G(0)
=
-3(1+\gamma)NS_0.
}
\tag{4.2}
\]

Hence, for \(b(0)\neq0\),

\[
\boxed{
|b(s_N)|
=
|b(0)|
\left[
\frac{\rho(0)}{\rho(s_N)}
\right]^2
e^{-3(1+\gamma)NS_0}.
}
\tag{4.3}
\]

---

# 5. Compact interior shape implies exponential \(b\)-decay

Assume:

\[
\boxed{
0<\rho_-\le\rho(s)\le\rho_+<\infty.
}
\tag{5.1}
\]

Then:

\[
\boxed{
|b(s_N)|
\le
C_b
e^{-3(1+\gamma)NS_0}.
}
\tag{5.2}
\]

Assume also:

\[
|\lambda(s)|\le L,
\qquad
|a(s)|\le A.
\]

Equation (1.4) implies on each fixed period:

\[
|b(s)|
\le
e^{(1+L+2A)S_0}
|b(s_N)|.
\]

Therefore:

## Theorem D79.3 — Finite Total Transverse-Shear Action

\[
\boxed{
\int_0^\infty
b(s)^2ds
<
\infty
}
\tag{5.3}
\]

on every compact interior resonant \(E_p=0\) shape chain.

If \(b\equiv0\), the same conclusion is trivial.

---

# 6. Secular \(F\)-drift

Integrate D79.1 over \(N\) periods:

\[
\begin{aligned}
F(s_N)-F(0)
={}&
-\int_0^{s_N}\rho^2ds
+
2\int_0^{s_N}b^2ds
\\
&-
s_N
-
\frac32
\int_0^{s_N}\lambda ds.
\end{aligned}
\]

Use resonance:

\[
\int_0^{s_N}\lambda ds
=
\gamma s_N.
\]

Therefore:

## Theorem D79.4 — Exact Stroboscopic Secular Drift

\[
\boxed{
\begin{aligned}
F(s_N)-F(0)
={}&
-\int_0^{s_N}\rho^2ds
+
2\int_0^{s_N}b^2ds
\\
&-
\left(
1+\frac{3\gamma}{2}
\right)s_N.
\end{aligned}
}
\tag{6.1}
\]

Hence:

\[
\boxed{
F(s_N)
\le
F(0)
+
2\int_0^\infty b^2ds
-
\left(
1+\frac{3\gamma}{2}
\right)NS_0.
}
\tag{6.2}
\]

Thus:

\[
\boxed{
F(s_N)\to-\infty.
}
\tag{6.3}
\]

---

# 7. Compact nonaligned infinite-chain NO-GO

If:

\[
|\lambda|\le L,
\qquad
|a|\le A,
\]

and:

\[
0<\rho_-\le\rho\le\rho_+,
\]

then:

\[
F
=
a+\log\rho+\lambda/2
\]

is bounded above and below.

But D79.4 gives:

\[
F(s_N)\to-\infty.
\]

Contradiction.

Therefore:

## Theorem D79.5 — Compact Infinite Carrier NO-GO

There is no infinite material trajectory satisfying all of:

1. \(E_p=0\);
2. period-by-period \(2\gamma\) resonant stretching;
3. nonalignment \(\rho>0\);
4. uniformly bounded normalized \(\lambda,a,b,\rho,\rho^{-1}\).

Equivalently:

\[
\boxed{
\text{compact interior infinite resonant shape drift}
\Longrightarrow
\mathsf X.
}
\tag{7.1}
\]

This is stronger than the original D79 plan of extracting a recurrent subsequence.

---

# 8. Why recurrence is unnecessary

A compact dynamical system can have aperiodic recurrent orbits, so a naive “compactness gives a periodic carrier” argument would have been false.

D79 avoids that trap.

The contradiction is **secular**:

\[
F(s_N)
\sim
-
\left(
1+\frac{3\gamma}{2}
\right)NS_0.
\]

Thus even an irrational/chaotic compact orbit is impossible under the exact pressure-perfect resonant shape equations.

This is an important audit improvement.

---

# 9. Exact ways to escape D79.5

An X-free infinite local carrier must violate at least one compact-interior hypothesis.

Thus:

## A. alignment-boundary escape

\[
\boxed{
\inf_n\rho(s_n)=0.
}
\]

The nonaligned tilt chart degenerates toward:

\[
D_s\xi=0.
\]

If a recurrent aligned carrier emerges, D62 sends it to X.

If \(\rho\to0\) only asymptotically without recurrence, the branch is an explicit alignment-boundary noncompactness.

---

## B. tilt blow-up

\[
\boxed{
\sup_n\rho(s_n)=\infty.
}
\]

The material vorticity direction develops unbounded normalized angular velocity.

This is a shape/filamentation transition defect.

---

## C. strain-shape blow-up

At least one of:

\[
\boxed{
|\lambda_n|\to\infty,
\qquad
|a_n|\to\infty,
\qquad
|b_n|\to\infty.
}
\]

Then the normalized local velocity-gradient shape leaves every compact set.

This is explicit state-transition compactness failure.

---

# 10. Spatial compactness can also fail while pointwise shape stays bounded

D79.5 addresses pointwise moving-frame shape compactness.

A packet may still evade global material compactification through spatial mechanisms.

The inherited same-parent bridge already identifies the relevant alternatives.

---

## D. normalized support escape

The carrier packet leaves every fixed normalized supplier annulus:

\[
\boxed{
\operatorname{dist}
(D_n,0)
\to\infty
}
\]

or its diameter grows without normalized control.

This is the pre-existing:

\[
\boxed{
\text{material tail escape / tail-fed replenishment}.
}
\]

It is exactly the natural realization of the D77 preselection branch.

---

## E. material filamentation / director oscillation

The pointwise shape variables remain bounded but the material packet loses spatial equicontinuity:

\[
\boxed{
\|\nabla\xi_n\|,
\quad
\|\nabla S_n\|,
\quad
\text{or material-line complexity}
\to\infty.
}
\]

Then strong packet-state compactness fails through filamentation.

This is already an inherited material-transition defect.

---

## F. packet multiplicity explosion

One incoming packet is repeatedly split into an increasing number of descendant packets, or the selector requires an unbounded number of material components.

Then no finite packet-state compiler can shadow the material return.

This is:

\[
\boxed{
\text{material state/transition multiplicity noncompactness}.
}
\]

---

## G. singular/new-material injection

If outgoing carrier measure is not absolutely continuous with respect to incoming material measure, D77 already identifies an explicit material injection event.

This is a turnover/transition defect, not a hidden equality mode.

---

# 11. Preselection is now identified with material-tail/noncompact replenishment

D77's pure-preselection route assumed the outgoing resonant carrier is already present in the incoming high-stretch tail.

If this process is iterated indefinitely and no finite stage creates high stretch dynamically, then the source of the carrier is pushed indefinitely upstream.

In the same-parent DSS geometry, this means:

\[
\boxed{
\text{high-stretch source escapes every finite material ancestry depth}.
}
\]

Therefore:

## Theorem D79.6 — Preselection / Upstream-Escape Identification

The indefinitely X-free pure-preselection branch is a material-tail / ancestry noncompactness branch.

It is not a compact local equality state.

---

# 12. Connection with the earlier same-parent transition normal form

The earlier RMRM same-parent bridge already produced a compact-class alternative of the form:

\[
\boxed{
\text{material tail escape}
\ \vee\
\text{material filamentation}
\ \vee\
\text{viscous circulation residue}
\ \vee\
\text{state/loop transition mismatch}.
}
\]

D79 independently arrives at the same geometry from the late X72/T chain.

This is a strong consistency check.

The late proof tree has not created a new mysterious compact endpoint.

It has reconverged to the already-declared material noncompactness coordinates.

---

# 13. Prelimit Navier–Stokes ancestry note

The current D79 secular argument is an Euler-profile argument.

When this material chain is shadowed back to the Navier–Stokes parent, an additional inherited alternative remains:

\[
\boxed{
\text{nonvanishing second-order viscous Kelvin/circulation residue}.
}
\]

D79 does not eliminate that prelimit channel.

If the viscous residue vanishes, the material noncompactness must be visible through one of the Euler alternatives A–G.

If it does not vanish, that residue is already an explicit Navier–Stokes ancestry defect.

---

# 14. A compact-chain theorem without topology overclaim

The correct theorem is not:

> every compact infinite chain contains a periodic orbit.

That statement is false in general dynamics.

The correct result is:

## Theorem D79.7 — Secular Compact-Chain Exclusion

For the exact \(E_p=0\), \(2\gamma\)-resonant D78 shape dynamics, **uniform compactness of the nonaligned normalized shape variables is itself impossible**, because the scalar \(F\) has a strict negative secular drift after the transverse shear \(b\) is damped by the scalar \(G\).

Thus no recurrence theorem is needed.

---

# 15. Quantitative compact-class escape time

Assume the normalized shape remains inside:

\[
\boxed{
|\lambda|\le L,
\qquad
|a|\le A,
\qquad
\rho_-\le\rho\le\rho_+.
}
\]

Then:

\[
F
\ge
-A+\log\rho_- -\frac L2
=:F_-.
\]

Let:

\[
B_\infty
=
\int_0^\infty b^2ds<\infty.
\]

D79.4 gives:

\[
F(s_N)
\le
F(0)+2B_\infty
-
c_FNS_0,
\]

where:

\[
\boxed{
c_F
=
1+\frac{3\gamma}{2}>0.
}
\]

Therefore the chain must exit the compact shape box by:

\[
\boxed{
N
\le
\frac{
F(0)+2B_\infty-F_-
}{
c_FS_0
}.
}
\tag{15.1}
\]

So on a fixed compact class the X-free material chain has a finite normalized escape depth.

This is a genuine finite-depth transition theorem.

---

# 16. What happens at finite-depth escape

At or before the bound (15.1), at least one of the following occurs:

\[
\boxed{
E_p\neq0,
}
\]

or:

\[
\boxed{
\rho\downarrow0,
}
\]

or:

\[
\boxed{
\rho,\lambda,a,b
\text{ leave the compact shape range},
}
\]

or a spatial/material compactness coordinate fails.

Therefore the chain cannot hide forever inside a finite normalized state compiler.

---

# 17. Updated X/T frontier

D78 had:

\[
\mathsf T_{\rm dyn}
\Longrightarrow
\mathsf X
\vee
\mathsf T_{\rm drift}
\vee
\mathsf T_{\rm preselect}.
\]

D79 now proves:

\[
\boxed{
\mathsf T_{\rm drift}^{\rm compact}
\Longrightarrow
\mathsf X.
}
\]

And:

\[
\boxed{
\mathsf T_{\rm preselect}^{\infty}
\Longrightarrow
\text{material-tail/ancestry noncompactness}.
}
\]

Therefore the genuinely X-free T remainder is:

\[
\boxed{
\mathsf T_{\rm noncomp}.
}
\]

It is no longer a compact recurrent flow state.

It is one of a finite catalogue of explicit noncompactness/transition modes.

Thus:

## Theorem D79.8 — Late-Stage Frontier Compression

\[
\boxed{
\text{rank-two continuation}
\Longrightarrow
\mathsf X
\vee
\mathsf T_{\rm noncomp}.
}
\tag{17.1}
\]

Where \(\mathsf T_{\rm noncomp}\) is explicitly:

- alignment-boundary escape;
- shape blow-up;
- support/tail escape;
- material filamentation;
- packet-multiplicity explosion;
- singular material injection;
- or prelimit viscous circulation residue when lifting back to Navier–Stokes.

No compact X-free material equality state remains in the D76–79 chain.

---

# 18. Why this is genuinely an endgame compression

The remaining X branch is a finite active pressure/cofactor/transport defect.

The remaining T branch is no longer an ordinary recurrent material mechanism.

It is an explicit failure of compact same-parent material return.

So the late proof problem has become:

\[
\boxed{
\text{finite active X72 defect}
}
\]

versus:

\[
\boxed{
\text{explicit material/state noncompactness}.
}
\]

This is a much sharper distinction than the original broad X/T split.

---

# 19. What D79 does not prove

D79 does **not** prove:

- every material noncompactness mode is impossible;
- tail-fed preselection cannot exist;
- exponential filamentation cannot exist;
- packet multiplicity cannot diverge;
- the prelimit viscous Kelvin residue vanishes;
- global Navier–Stokes regularity.

The remaining problem has been classified, not finished.

---

# 20. New STOP

\[
\boxed{
\textbf{
STOP-D79:
The infinite X-free material shape-drift branch cannot remain compact. In the exact pressure-perfect resonant moving-frame system the scalar combinations }F=a+\log\rho+\lambda/2\textbf{ and }G=\log|b|+2\log\rho\textbf{ satisfy }F'=-\rho^2+2b^2-1-\tfrac32\lambda\textbf{ and }G'=-3(1+\lambda)\textbf{. Resonance makes }b\textbf{ exponentially decay on every compact nonaligned shape class, after which }F\textbf{ drifts linearly to }-\infty\textbf{, contradicting compactness without invoking any recurrence theorem. Thus every X-free infinite T chain must lose compactness explicitly through alignment degeneration, shape blow-up, tail/support escape, filamentation, multiplicity/injection, or the inherited prelimit viscous-circulation residue. No compact X-free material equality state remains.}
}
\]

---

# 21. Next autonomous step

## DCRP80 / X72-R63 — Noncompact T Escape Absorption Audit

**Working title**

> **Can Each Explicit Material Noncompactness Mode Be Absorbed into Existing X72 / RMRM Defect Coordinates?**

Primary tasks:

1. take the D79 catalogue:
   - \(\rho\to0\);
   - shape blow-up;
   - support escape;
   - filamentation;
   - packet multiplicity;
   - injection;
   - viscous Kelvin residue;
2. identify which are already quantitatively represented by:
   - D77 tilt/X first-crossing action;
   - D31 PFET;
   - D35/D59 turnover;
   - D33 material holonomy/filamentation;
   - X72 pressure/cofactor transition;
3. determine whether any noncompact mode is truly new;
4. seek a finite terminal compiler:
   \[
   \mathsf T_{\rm noncomp}
   \Longrightarrow
   \mathsf X
   \vee
   \mathsf R_{\rm known}
   \vee
   \text{one genuinely new noncompact escape};
   \]
5. if every mode is inherited, return to the strongest unresolved quantitative defect rather than generating further geometry.

Desired endpoint:

\[
\boxed{
\text{late T noncompactness}
=
\text{finite list of already-known proof obligations}.
}
\]

---

# 22. One-line checkpoint

The infinite material escape can no longer hide inside a compact normalized state space: exact secular identities force any X-free resonant carrier to leave compactness in finite normalized depth, so the remaining T branch is now only an explicit catalogue of material/state noncompactness modes rather than a recurrent equality state.

---

**End checkpoint:** DCRP79 / X72-R62  
**Next:** DCRP80 / X72-R63 — Noncompact T Escape Absorption Audit.
