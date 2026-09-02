# From the Original Kakeya Needle to the Moser Worm  
## Positive-Thickness Bridge Theory of Center-Generated Bi-directional Offset Spirals

**Subtitle:** Non-overlapping Orthogonal Sweeps, Area Invariants, and Universal Covering Functionals  
**Version:** v0.1  
**Date:** July 27, 2026  
**Nature:** Propositional Geometry Paper / Research Program  
**Status:** Some theorems are directly provable; bridge extrema and asymptotic propositions remain to be investigated

---

## Abstract

The original Kakeya needle problem, center-generated bi-directional offset spirals, and the Moser worm problem ostensibly study the rotation of a needle, the generation of spiral bands, and the universal covering of unit curves, respectively. In reality, all three share the same deep structure: how the directional variation of a one-dimensional geometric object translates into a supporting region with two-dimensional area.

This paper proposes the "Positive-Thickness Center-Generated Kakeya-Moser Bridge Theory." Its core method is to internalize the external rotational phase of the Kakeya needle into the tangential phase of a center curve, and to have a needle of length \(2\rho\) move continuously along the normal direction of the center curve. The resulting swept set is precisely the bi-directional normal band of the center curve. If the normal parameterization remains injective in its interior and \(\rho\|\kappa\|_\infty<1\), then the swept area satisfies the exact invariant

\[
\mu_2(S_\rho(\gamma))=2\rho L.
\]

If semicircular caps are added at both ends, the area of the complete tubular neighborhood is

\[
\mu_2(T_\rho(\gamma))=2\rho L+\pi\rho^2.
\]

Therefore, the degenerate pathway of the original Kakeya problem—which compresses the swept area toward zero through massive overlapping—is closed under the conditions of "positive thickness + no internal overlapping." However, the area of a single sweep consequently loses its shape dependence. The problem that truly retains a non-trivial extremal structure is transformed into: finding the minimum-area container that accommodates all center-generated positive-thickness sweeps via rigid motions. This is exactly a Moser-type universal covering problem.

This paper formalizes the differences and interfaces among the three, proves that orthogonal Kakeya sweeps are equivalent to bi-directional offset bands, derives the area invariant and the translation law of support functions, and proposes the new "center-generated Kakeya-Moser bridge functional," the zero-thickness asymptotic problem, the contact-saturated spiral proposition, and a research program on curvature concentration.

**Keywords:** Kakeya needle problem, Moser worm problem, center-generated spiral, tubular neighborhood, positive thickness, non-overlapping, support function, universal cover, curvature, geometric measure

---

# 1. Problem Background and Necessary Distinctions

## 1.1 The Original Kakeya Needle Problem

Let the unit needle be the line segment

\[
I=[-1/2,1/2]\times\{0\}.
\]

The original Kakeya problem investigates: does there exist a planar region of arbitrarily small area within which a single needle can move continuously and reverse its direction by \(180^\circ\)?

A configuration of the needle can be written as

\[
q(t)=(a(t),\phi(t))
\in SE(2),
\]

where \(a(t)\in\mathbb R^2\) is the needle center and \(\phi(t)\) is the rotational phase. The needle at time \(t\) is

\[
I_t=a(t)+R_{\phi(t)}I,
\]

and its swept set is

\[
K[q]
=
\bigcup_{t\in[0,1]}I_t.
\]

The original dynamic problem requires

\[
\phi(1)-\phi(0)=\pi
\]

and studies

\[
\inf_q\mu_2(K[q]).
\]

Two related but distinct formulations must be distinguished:

1. **Dynamic Kakeya needle problem:** Can the same needle complete a reversal along a continuous path?
2. **Static Besicovitch set:** Does a set contain a unit line segment in every direction?

The two are historically closely related, but "containing all directions" does not automatically provide a continuous configuration path for the same needle.

---

## 1.2 The Moser Worm Problem

Let

\[
\mathcal C_1
=
\left\{
\gamma:
\operatorname{Len}(\gamma)=1
\right\}
\]

be the family of all rectifiable planar curves of length one.

The Moser worm problem seeks a region \(C\) of minimum area such that any \(\gamma\in\mathcal C_1\) can be placed into \(C\) via translation and rotation:

\[
\forall\gamma\in\mathcal C_1,
\qquad
\exists g\in SE(2),
\qquad
g\gamma\subseteq C.
\]

Its functional is

\[
M^\ast
=
\inf_C
\left\{
\mu_2(C):
\forall\gamma\in\mathcal C_1,\,
\exists g\in SE(2),\,
g\gamma\subseteq C
\right\}.
\]

The original Kakeya problem studies the "continuous motion path of a single object"; Moser studies the "optimal static placement of all objects individually." The two cannot be directly regarded as the same problem.

---

## 1.3 Center-Generated Bi-directional Offset Spirals

Let the center generating line be an arc-length parameterized curve

\[
\gamma:[0,L]\to\mathbb R^2,
\qquad
\|\gamma'(s)\|=1.
\]

Let

\[
T(s)=\gamma'(s)
\]

be the unit tangent vector,

\[
N(s)
\]

be the unit normal vector, and represent the tangential phase \(\theta(s)\) by

\[
T(s)
=
(\cos\theta(s),\sin\theta(s)).
\]

The curvature is

\[
\kappa(s)=\theta'(s).
\]

The center-generated conditions include at least:

\[
\gamma(0)=0,
\]

and the radial non-retreating condition

\[
\frac{d}{ds}\|\gamma(s)\|
\geq0
\]

holds wherever differentiable.

If we further require

\[
\theta'(s)\geq0,
\]

then the direction of the curve rotates monotonically along the arc length, forming a turning generation outward from the center.

---

# 2. External Rotational Phase and Internal Tangential Phase

The directional variation in the original Kakeya problem is described by the external configuration angle

\[
\phi(t).
\]

The directional variation in the center-generated curve is described by the internal tangential angle

\[
\theta(s).
\]

The fundamental translation between the two is

\[
\boxed{
\phi(t)
\longleftrightarrow
\theta(s)+\frac{\pi}{2}
}.
\]

The reason is that this paper places the Kakeya needle along the normal of the center line. For each \(s\), define a normal needle of length \(2\rho\) as

\[
I_s
=
\left\{
\gamma(s)+tN(s):
-\rho\leq t\leq\rho
\right\}.
\]

The direction of the needle is \(N(s)\), and its directional angle is precisely

\[
\theta(s)+\frac{\pi}{2}.
\]

Therefore:

- The external needle direction of Kakeya becomes the normal direction of the curve;
- The time parameter of Kakeya becomes the arc-length parameter of the curve;
- The needle center path becomes the center generating line \(\gamma\).

---

# 3. Orthogonal Kakeya Motion

## Definition 3.1: Orthogonal Kakeya Motion

A motion of a needle of length \(2\rho\)

\[
q(s)=(a(s),\phi(s))
\]

is called an orthogonal Kakeya motion if it satisfies

\[
\|a'(s)\|=1
\]

and

\[
a'(s)\cdot
(\cos\phi(s),\sin\phi(s))
=
0.
\]

That is: the velocity of the needle center is always perpendicular to the needle itself.

If we set

\[
a(s)=\gamma(s),
\qquad
\phi(s)=\theta(s)+\frac{\pi}{2},
\]

then the above conditions hold automatically.

---

## Proposition 3.2: Orthogonal Motion-Center Curve Correspondence

Every \(C^1\) arc-length parameterized center curve \(\gamma\) naturally generates an orthogonal Kakeya motion:

\[
q_\gamma(s)
=
\left(
\gamma(s),
\theta(s)+\frac{\pi}{2}
\right).
\]

Conversely, any regular needle center path satisfying the orthogonality condition can, after choosing an orientation, be viewed as the normal needle motion of some center curve.

### Proof

From

\[
\gamma'(s)=T(s)
\]

and

\[
N(s)\perp T(s),
\]

we obtain

\[
\gamma'(s)\cdot N(s)=0.
\]

Since the direction vector of the needle is exactly \(N(s)\), the velocity of the needle center is perpendicular to the needle. The reverse construction recovers a tangent-normal frame from the orthogonal unit velocity and needle direction. This completes the proof.

---

# 4. Swept Sets and Bi-directional Offset Bands

## Definition 4.1: Bi-directional Normal Band

Define

\[
F_\rho(s,t)
=
\gamma(s)+tN(s),
\qquad
(s,t)\in[0,L]\times[-\rho,\rho].
\]

Its image set

\[
S_\rho(\gamma)
=
F_\rho
\left(
[0,L]\times[-\rho,\rho]
\right)
\]

is called the bi-directional normal band of the center curve.

---

## Theorem 4.2: Kakeya Sweep-Offset Band Identity

The swept set of the orthogonal Kakeya motion generated by the center curve \(\gamma\) is precisely

\[
\boxed{
\bigcup_{s\in[0,L]}I_s
=
S_\rho(\gamma)
}.
\]

### Proof

For a fixed \(s\), the position of the needle is

\[
I_s
=
\left\{
\gamma(s)+tN(s):
-\rho\leq t\leq\rho
\right\}.
\]

Taking the union over all \(s\) yields exactly the image of \(F_\rho\) over the entire parameter rectangle. This completes the proof.

---

# 5. Directional Completeness

Undirected line segment directions in the plane are represented by

\[
\mathbb R/\pi\mathbb Z;
\]

directed directions are represented by

\[
\mathbb R/2\pi\mathbb Z.
\]

## Proposition 5.1: Directional Completeness Condition

If \(\theta\) is continuous and

\[
\theta(L)-\theta(0)\geq\pi,
\]

then the normal needle \(I_s\) experiences at least all undirected directions.

If

\[
\theta(L)-\theta(0)\geq2\pi,
\]

then the normal needle completes at least one full cycle of all directed directions.

### Proof

The normal angle is

\[
\phi(s)=\theta(s)+\frac{\pi}{2}.
\]

By the intermediate value theorem for continuous functions, the image of \(\phi\) contains a complete angular interval of length at least \(\pi\) or \(2\pi\). Modulo \(\pi\) or \(2\pi\) respectively yields the result. This completes the proof.

---

# 6. Non-overlapping and Positive Area

## Definition 6.1: Internal Non-overlapping

Require

\[
F_\rho:
[0,L]\times(-\rho,\rho)
\to\mathbb R^2
\]

to be injective.

Boundaries may touch, but different parameter points must not map to the same internal area point.

A standard sufficient condition is

\[
\operatorname{reach}(\gamma)\geq\rho.
\]

Local regularity is guaranteed by

\[
\rho\|\kappa\|_\infty<1.
\]

---

## Theorem 6.2: Area Invariant of Non-overlapping Orthogonal Sweeps

Let \(\gamma\) be a \(C^2\) arc-length parameterized curve of length \(L\), and assume:

1. \(F_\rho\) is injective in the interior;
2. \(\rho\|\kappa\|_\infty<1\).

Then

\[
\boxed{
\mu_2(S_\rho(\gamma))
=
2\rho L
}.
\]

### Proof

From the Frenet formulas

\[
N'(s)=-\kappa(s)T(s),
\]

we obtain

\[
\frac{\partial F_\rho}{\partial s}
=
T(s)+tN'(s)
=
\left(
1-t\kappa(s)
\right)T(s),
\]

and

\[
\frac{\partial F_\rho}{\partial t}
=
N(s).
\]

The Jacobian is

\[
J_F(s,t)
=
\left|
\det
\left(
(1-t\kappa)T,N
\right)
\right|
=
|1-t\kappa(s)|.
\]

From

\[
\rho\|\kappa\|_\infty<1
\]

we know that over the entire parameter domain

\[
1-t\kappa(s)>0.
\]

Therefore

\[
\begin{aligned}
\mu_2(S_\rho(\gamma))
&=
\int_0^L
\int_{-\rho}^{\rho}
\left(
1-t\kappa(s)
\right)
\,dt\,ds\\
&=
\int_0^L
\left[
2\rho
-
\kappa(s)
\int_{-\rho}^{\rho}t\,dt
\right]ds\\
&=
\int_0^L2\rho\,ds\\
&=
2\rho L.
\end{aligned}
\]

This completes the proof.

---

## Corollary 6.3: Complete Tubular Neighborhood

If \(\gamma\) is an open curve, and two semicircular caps of radius \(\rho\) are added at both ends, then

\[
T_\rho(\gamma)
=
\gamma\oplus\rho B
\]

satisfies

\[
\boxed{
\mu_2(T_\rho(\gamma))
=
2\rho L+\pi\rho^2
}.
\]

If \(\gamma\) is a simple closed curve and the tubular neighborhood does not self-intersect, then there is no end-cap term:

\[
\boxed{
\mu_2(T_\rho(\gamma))
=
2\rho L.
}
\]

---

# 7. Closure of the Kakeya Degenerate Pathway

The original Kakeya problem allows needle positions at different times to highly overlap, thus the same region can be repeatedly used to support a massive number of directional states.

This paper adds:

\[
\rho>0
\]

and

\[
F_\rho
\text{ is injective in the interior}.
\]

Consequently, different time cross-sections cannot share a positive-area interior.

By Theorem 6.2:

\[
\mu_2(S_\rho(\gamma))
=
2\rho L>0.
\]

Therefore:

\[
\boxed{
\text{Positive thickness and non-overlapping conditions close the zero-area degenerate pathway of Kakeya.}
}
\]

But simultaneously, a deeper result emerges:

\[
\boxed{
\text{The area of a single sweep no longer depends on the shape of the center line.}
}
\]

As long as the length, thickness, and non-overlapping conditions are the same, circular arcs, spirals, smoothed polylines, or general curvature distributions all possess the same normal band area \(2\rho L\).

Therefore, the optimization problem must shift.

---

# 8. The Main Transition from Kakeya to Moser

The original Kakeya asks:

> What is the minimum area that must be swept by a single directionally complete motion of the same needle?

Under the restrictions of this paper, the answer is fixed by the area invariant to

\[
2\rho L.
\]

The non-trivial problem thus becomes:

> Which minimum-area region can, via different rigid placements, accommodate all qualifying directionally complete orthogonal sweeps?

This is precisely a Moser-type problem.

---

# 9. Center-Generated Kakeya-Moser Bridge Family

## Definition 9.1: Center-Generated Curve Family

Let

\[
\Gamma_{\mathrm{CG}}
(L,\rho,\tau)
\]

be all curves \(\gamma\) satisfying the following conditions:

1. \(\gamma:[0,L]\to\mathbb R^2\) is a \(C^2\) arc-length parameterized curve;
2. \(\gamma(0)=0\);
3. Radial non-retreating:
   \[
   \frac{d}{ds}\|\gamma(s)\|\geq0;
   \]
4. Tangential phase monotonicity:
   \[
   \theta'(s)\geq0;
   \]
5. Total turning:
   \[
   \theta(L)-\theta(0)\geq\tau;
   \]
6. Tubular regularity:
   \[
   \rho\|\kappa\|_\infty<1;
   \]
7. Internal non-overlapping:
   \[
   \operatorname{reach}(\gamma)\geq\rho.
   \]

When

\[
\tau=\pi
\]

the normal needle completes all undirected directions.

When

\[
\tau=2\pi
\]

the normal needle completes all directed directions.

---

## Definition 9.2: Bridge Universal Covering Functional

Define

\[
\mathfrak B(L,\rho,\tau)
=
\inf_C
\left\{
\mu_2(C):
\forall\gamma\in
\Gamma_{\mathrm{CG}}(L,\rho,\tau),
\,
\exists g\in SE(2),
\,
gT_\rho(\gamma)\subseteq C
\right\}.
\]

This functional is called:

\[
\boxed{
\text{Positive-thickness center-generated Kakeya-Moser bridge functional}.
}
\]

It simultaneously contains:

- Kakeya's directional completeness;
- The spiral's endogenous turning and outward center-pushing;
- Moser's universal covering of a curve family;
- Positive thickness and non-overlapping constraints in geometric measure.

---

# 10. Basic Area Bounds

## Theorem 10.1: Positive Lower Bound for Universal Containers

If the bridge family is non-empty, then any universal container \(C\) must accommodate at least one complete tubular object within it, therefore

\[
\boxed{
\mathfrak B(L,\rho,\tau)
\geq
2\rho L+\pi\rho^2.
}
\]

If studying the normal band without end caps, then

\[
\boxed{
\mathfrak B_{\mathrm{strip}}
(L,\rho,\tau)
\geq
2\rho L.
}
\]

### Proof

If

\[
gT_\rho(\gamma)\subseteq C,
\]

then by measure monotonicity and rigid motion invariance:

\[
\mu_2(C)
\geq
\mu_2(gT_\rho(\gamma))
=
\mu_2(T_\rho(\gamma)).
\]

Applying Corollary 6.3 yields the result. This completes the proof.

---

# 11. Upper Bound Interface with Moser Universal Containers

Let \(C\) be a Moser-type container that can accommodate all center curves of length \(L\).

If

\[
g\gamma\subseteq C,
\]

then

\[
g(\gamma\oplus\rho B)
=
g\gamma\oplus\rho B
\subseteq
C\oplus\rho B.
\]

Therefore:

\[
\boxed{
C\oplus\rho B
}
\]

is a universal container for all thickened curves.

Hence we have

\[
\boxed{
\mathfrak B(L,\rho,\tau)
\leq
\inf_{C\in\mathcal M_L}
\mu_2(C\oplus\rho B),
}
\]

where \(\mathcal M_L\) is the family of Moser universal containers for curves of length \(L\).

If \(C\) is a convex set, Steiner's formula gives

\[
\mu_2(C\oplus\rho B)
=
\mu_2(C)
+
\rho\,\operatorname{Per}(C)
+
\pi\rho^2.
\]

Therefore:

\[
\boxed{
\mathfrak B(L,\rho,\tau)
\leq
\inf_{C\in\mathcal M_L^{\mathrm{conv}}}
\left[
\mu_2(C)
+
\rho\operatorname{Per}(C)
+
\pi\rho^2
\right].
}
\]

This provides a direct upper bound transfer from existing Moser containers to the positive-thickness bridge problem.

---

# 12. Spirals as a Center-Generated Special Case

In polar coordinates, let

\[
\gamma(\vartheta)
=
r(\vartheta)
(\cos\vartheta,\sin\vartheta),
\]

and require

\[
r(0)=0,
\qquad
r'(\vartheta)\geq0.
\]

If

\[
r'(\vartheta)=b>0,
\]

then

\[
r(\vartheta)=b\vartheta
\]

is an Archimedean spiral.

The radial pitch per revolution is

\[
p=2\pi b.
\]

However:

\[
p\geq2\rho
\]

can only serve as a simple proxy for loop spacing in near-circular layers, and cannot replace the exact non-overlapping condition.

The exact condition remains

\[
\operatorname{reach}(\gamma)\geq\rho.
\]

Therefore, this paper defines "adjacent loop boundaries exactly touching" as:

\[
\boxed{
\operatorname{reach}(\gamma)=\rho,
}
\]

rather than relying solely on the radial pitch.

---

# 13. Circles, Spirals, and Complete Turning Units

A total turning angle equal to \(2\pi\) is not sufficient to deduce that the curve is a circle.

Only when the curvature is identical everywhere:

\[
\kappa(s)\equiv\frac1R
\]

is the complete \(2\pi\) turning unit a circle of radius \(R\).

Therefore:

\[
\boxed{
\text{A circle is a complete turning unit of constant curvature.}
}
\]

If, after completing a local complete turn, the generating radius continues to increase outward, the global geometry cannot be maintained as the same circle, but transforms into a spiral-like stratification.

Thus:

\[
\boxed{
\text{The circle is a local turning language;
the spiral is a global connection language for multiple turning units.}
}
\]

---

# 14. Support Function Interface

For any compact set \(X\subset\mathbb R^2\), the support function is

\[
h_X(u)
=
\sup_{x\in X}x\cdot u.
\]

The complete tubular neighborhood satisfies

\[
T_\rho(\gamma)
=
\gamma\oplus\rho B.
\]

The support function of a Minkowski sum is additive, therefore

\[
\boxed{
h_{T_\rho(\gamma)}(u)
=
h_\gamma(u)+\rho.
}
\]

If the container is \(C\), the rotational phase is \(\phi\), and the translation is \(t\), the covering gap field of the original curve is

\[
K_{C,\gamma}
(\theta;\phi,t)
=
h_\gamma(\theta-\phi)
+
t\cdot u_\theta
-
h_C(\theta).
\]

After thickening:

\[
\begin{aligned}
K_{C,T_\rho(\gamma)}
(\theta;\phi,t)
&=
h_\gamma(\theta-\phi)
+\rho
+t\cdot u_\theta
-h_C(\theta)\\
&=
K_{C,\gamma}
(\theta;\phi,t)
+\rho.
\end{aligned}
\]

Therefore:

\[
\boxed{
\text{Positive thickness manifests in the support space as a constant pressure uniformly added in all directions.}
}
\]

The curvature, spiral pitch, and turning distribution of the center line control the non-trivial directional skewness.

---

# 15. Three-Tier Ledger

This paper proposes three mutually coupled geometric ledgers.

## 15.1 Kakeya Direction Ledger

Records:

\[
(
s,\phi(s),\Delta\phi,
\text{directional coverage}
).
\]

## 15.2 Spiral Curvature Ledger

Records:

\[
(
s,\kappa(s),
\theta(s),
r(s),
\operatorname{reach}(\gamma)
).
\]

## 15.3 Moser Container Pressure Ledger

Records:

\[
(
\theta,
h_\gamma(\theta),
h_C(\theta),
K^+_{C,\gamma}(\theta)
).
\]

The interfaces among the three are:

\[
\boxed{
\phi(s)=\theta(s)+\frac{\pi}{2}
}
\]

and

\[
\boxed{
h_{T_\rho(\gamma)}=h_\gamma+\rho.
}
\]

---

# 16. Main New Propositions

## Proposition A: Positive-Thickness Degeneracy Blocking Proposition

For fixed

\[
L>0,\qquad\rho>0,
\]

all internally non-overlapping orthogonal Kakeya sweeps satisfy

\[
\mu_2(S_\rho(\gamma))=2\rho L.
\]

Therefore, the arbitrarily small area degeneracy of the original Kakeya cannot occur in this class.

---

## Proposition B: Extremum Shift Proposition

Once the area invariant holds, the swept area of a single motion no longer possesses shape extrema.

The non-trivial optimization shifts from

\[
\inf_\gamma\mu_2(S_\rho(\gamma))
\]

to

\[
\inf_C
\left\{
\mu_2(C):
C\text{ universally covers all }S_\rho(\gamma)
\right\}.
\]

Therefore:

\[
\boxed{
\text{The non-overlapping positive-thickness condition naturally translates Kakeya-type problems into Moser-type problems.}
}
\]

---

## Proposition C: Support Pressure Elevation Proposition

For any center-generated curve:

\[
K_{C,T_\rho(\gamma)}
=
K_{C,\gamma}+\rho.
\]

Positive thickness does not change the angular shape of the center line's support function; it only uniformly elevates the pressure in all directions.

---

# 17. New Conjectures and Research Questions

## Conjecture 17.1: Non-trivial Universal Margin

Define the cap-free area margin:

\[
\Xi(L,\rho,\tau)
=
\mathfrak B_{\mathrm{strip}}(L,\rho,\tau)
-
2\rho L.
\]

Conjecture that for the directionally complete family:

\[
\tau\geq\pi
\]

there exist certain parameter ranges such that

\[
\boxed{
\Xi(L,\rho,\tau)>0.
}
\]

This implies that there does not exist a region with an area equal to a single sweep that can accommodate all directionally complete center-generated sweeps.

---

## Conjecture 17.2: Thin-Thickness Asymptotic Law

Study

\[
\rho\to0^+
\]

as:

\[
\mathfrak B_{\mathrm{strip}}
(L,\rho,\tau).
\]

The lowest-order known lower bound is

\[
2\rho L.
\]

The new question is whether there exists

\[
c(L,\tau)>1
\]

such that

\[
\mathfrak B_{\mathrm{strip}}
(L,\rho,\tau)
\sim
2c(L,\tau)\rho L.
\]

If

\[
c(L,\tau)=1,
\]

then the universal covering margin only appears at higher orders.

If

\[
c(L,\tau)>1,
\]

then directional completeness leaves a normalizable area cost even in the zero-thickness limit.

---

## Conjecture 17.3: Contact-Saturated Spiral Proposition

Under fixed length, thickness, and total turning, the center-generated curve exerting the most container pressure likely lies on the contact-saturated boundary of:

\[
\operatorname{reach}(\gamma)=\rho.
\]

That is, adjacent layers are allowed to touch at the boundaries, but leave no excess gaps, nor do they overlap internally.

---

## Conjecture 17.4: Curvature Concentration Proposition

The most difficult bridge curve is not necessarily a constant-curvature spiral.

Its curvature might concentrate in finite-width turning layers, making multiple container contact branches simultaneously equal in height.

One can study:

\[
\theta_\varepsilon(s)
=
\theta_0
+
\Delta\theta\,F_\varepsilon(s),
\]

and check whether a finite

\[
\varepsilon>0
\]

generates a higher universal covering pressure than zero-width vertices or constant-curvature distributions.

---

# 18. Relationship with the Complete Moser Problem

The center-generated bridge family is merely a restricted subfamily of all curves of length \(L\):

\[
\Gamma_{\mathrm{CG}}
(L,\rho,\tau)
\subset
\mathcal C_L.
\]

Therefore, any complete Moser universal container must accommodate at least its center line.

If studying the thickened version, taking the Minkowski dilation of the Moser container directly yields an upper bound for the bridge problem.

The reverse direction is:

> If one can find objects in the center-generated bridge family that are harder to accommodate than existing test curves, they can directly serve as a new test family for Moser lower bounds or container pressure studies.

Thus, this bridge theory is not a replacement for the Moser problem, but a controllable intermediate curve family equipped with:

- Directional completeness;
- Positive thickness;
- Non-overlapping property;
- Curvature ledger;
- Spiral generation structure.

---

# 19. Research Procedure

Subsequent research can proceed sequentially:

1. Fix \(L,\rho,\tau\);
2. Generate center curves satisfying the reach condition;
3. Calculate normal sweeps and support functions;
4. Find the optimal rigid placement for candidate containers;
5. Establish the three-tier direction-curvature-support ledger;
6. Search for contact-saturated and branch-equal-height candidates;
7. Compare circular arcs, Archimedean spirals, variable-curvature spirals, and curvature concentration layers;
8. Establish interval arithmetic and reproducible certificates;
9. Feed the most difficult candidates back into the complete Moser worm study.

---

# 20. Limitations

This paper does not prove:

1. The Archimedean spiral is an extremum of the bridge family;
2. Contact-saturated curves are necessarily the hardest to accommodate;
3. \(\Xi(L,\rho,\tau)>0\);
4. The thin-thickness coefficient \(c(L,\tau)\) exists;
5. The bridge family can determine the optimal complete Moser container;
6. The original Kakeya, the bridge problem, and the Moser problem are mutually equivalent.

What this paper proves are the geometric interfaces and basic invariants, and it proposes a new universal covering problem.

---

# 21. Conclusion

The true intersection of the original Kakeya problem, center-generated bi-directional offset spirals, and the Moser worm problem is not simply a juxtaposition of three "area problems."

Its structure is:

\[
\boxed{
\text{Kakeya external directional motion}
\longrightarrow
\text{Center curve internal tangential generation}
\longrightarrow
\text{Positive-thickness normal sweep}
\longrightarrow
\text{Moser-type universal covering}.
}
\]

The center-generated curve internalizes the external rotational phase of the needle into the tangential phase:

\[
\phi=\theta+\frac{\pi}{2}.
\]

The bi-directional offset band transforms the continuous needle motion into a positive-area region:

\[
S_\rho(\gamma)
=
\bigcup_s I_s.
\]

The non-overlapping condition derives the exact area invariant:

\[
\boxed{
\mu_2(S_\rho(\gamma))
=
2\rho L.
}
\]

This invariant closes the zero-area degeneracy of Kakeya, while simultaneously shifting the core of optimization from "how much area is swept by a single motion" to:

\[
\boxed{
\text{Which minimum region can accommodate all directionally complete center-generated sweeps?}
}
\]

This is exactly what this paper proposes:

\[
\boxed{
\text{Positive-thickness center-generated Kakeya-Moser bridge problem}.
}
\]

---

# References

1. A. S. Besicovitch, *The Kakeya Problem*, The American Mathematical Monthly, 1963.
2. A. Chang and M. Csörnyei, *The Kakeya Needle Problem and the Existence of Besicovitch and Nikodym Sets for Rectifiable Sets*, Proceedings of the London Mathematical Society, 2019; arXiv:1609.01649.
3. R. Norwood, G. Poole, and M. Laidacker, *The Worm Problem of Leo Moser*, Discrete & Computational Geometry 7, 1992, 153–162.
4. T. Khandhawit, D. Pagonakis, and S. Sriswasdi, *Lower Bound for Convex Hull Area and Universal Cover Problems*, International Journal of Computational Geometry & Applications 23, 2013; arXiv:1101.5638.
5. W. Wichiramala and C. Panraksa, *Wetzel’s 30-60-90 Triangle Covers Unit Arcs*, arXiv:2606.14625, 2026.