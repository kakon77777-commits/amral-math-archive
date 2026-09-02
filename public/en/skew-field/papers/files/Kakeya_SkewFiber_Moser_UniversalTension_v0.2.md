# From the Original Kakeya Needle to the Moser Worm II  
## Measure-Preserving Skew-Line Fibers, Information-Faithful Kernels, and Universal Covering Tension

**Subtitle:** A Unified Extension of the Bridge Theory of Center-Generated Bidirectional Offset Spirals  
**Author:** Neo.K  
**Version:** v0.2  
**Date:** July 27, 2026  
**Research Nature:** Propositional Geometry Paper / Unified Framework / Interface for Subsequent Proofs  
**Status:** Tubular geometry section contains directly provable theorems; universal extrema, asymptotic laws, and optimal curves remain open propositions.

---

## Abstract

This paper unifies three previously separately developed research languages into a single geometric framework:

1. Directionally complete motion in the original Kakeya needle problem;
2. Positive-thickness sweeping of center-generated bidirectional offset spirals;
3. Covering tension in Moser-type universal accommodation problems.

This paper simultaneously incorporates two existing methodologies, "From 2D Total Measure to 1D Skew Lines" and "From 1D Metric Lines to Universal Covering Tension," proposing:

\[
\boxed{
\text{Measure-Preserving Skew-Line Fiber—Universal Covering Tension Theory}
}
\]

Its core geometric object is an arc-length parameterized center curve

\[
\gamma:[0,L]\to\mathbb R^2
\]

and its bidirectional normal strip

\[
S_\rho(\gamma)
=
\left\{
\gamma(s)+tN(s):
0\le s\le L,\;
-\rho\le t\le\rho
\right\}.
\]

If

\[
\operatorname{reach}(\gamma)>\rho,
\]

then the normal coordinates are injective, and the area element is

\[
d\mu_2
=
\left(
1-t\kappa(s)
\right)ds\,dt.
\]

From this, we immediately obtain the area invariant:

\[
\mu_2(S_\rho(\gamma))=2\rho L.
\]

This paper further proves a stronger measure expansion result: after projecting the normalized 2D area onto the center curve's arc-length parameter, the resulting marginal measure is exactly the uniform measure

\[
\frac{ds}{L}.
\]

Curvature information does not disappear due to the homogenization of the total measure; instead, it is transferred to the conditional density within each normal fiber:

\[
p_s(t)
=
\frac{1-t\kappa(s)}{2\rho}.
\]

Its first moment satisfies

\[
\mathbb E[t\mid s]
=
-\frac{\rho^2}{3}\kappa(s),
\]

hence

\[
\boxed{
\kappa(s)
=
-\frac{3}{\rho^2}
\mathbb E[t\mid s].
}
\]

Therefore, within the class of valid tubular curves with known \(L,\rho\), the 1D function of fiber skewness can recover the curvature, and then the center curve can be recovered via Frenet integration, up to a rigid body motion. This provides an information-faithful, invertible, and measure-preserving exact special case for the "1D skew-line expansion of a 2D total measure" within this restricted geometric class.

To handle general parameterizations, contact degeneracies, and congruent inclusions, this paper further introduces an information-faithful distance kernel:

\[
D_{\gamma,\rho}
\left(
(s,t),(s',t')
\right)
=
\left\|
\gamma(s)+tN(s)
-
\gamma(s')-t'N(s')
\right\|.
\]

Finally, for a candidate container \(C\), we define the universal uncovered tension of the positive-thickness bridge family:

\[
\mathfrak T_p
(C;L,\rho,\tau)
=
\sup_{\gamma\in\Gamma_{\mathrm{CG}}(L,\rho,\tau)}
\inf_{g\in E(2)}
\left[
\int_{T_\rho(\gamma)}
\operatorname{dist}(gx,C)^p
\,d\nu_{\gamma,\rho}(x)
\right]^{1/p}.
\]

The bridge universal accommodation problem can thus be precisely rewritten as:

\[
\mathfrak B(L,\rho,\tau)
=
\inf_C
\left\{
\mu_2(C):
\mathfrak T_p(C;L,\rho,\tau)=0
\right\}.
\]

The main conclusion of this paper is: under the conditions of positive thickness and non-overlapping, the individual swept area is fixed as a conserved quantity; the differences between different geometric objects are no longer manifested in the total area, but are transferred to fiber skewness, distance kernels, support pressures, and universal covering tensions. The Kakeya-type area extremum is thus naturally transformed into a Moser-type universal accommodation extremum.

**Keywords:** Kakeya needle problem, Moser's worm problem, measure preservation, skew lines, fiber geometry, center-generated spirals, tubular neighborhood, distance kernel, covering tension, support function, curvature reconstruction

---

# 1. Theoretical Origins and the Unified Problem

This paper is built upon three previous research nodes.

## 1.1 Positive-Thickness Kakeya–Moser Bridge

The first node transforms the external directional motion of the Kakeya needle into the internal tangential rotation of a center curve, and lets a positive-thickness needle move along the normal of the center curve.

Its basic correspondence is:

\[
\phi(s)
=
\theta(s)+\frac{\pi}{2}.
\]

Where:

- \(\phi(s)\) is the direction of the needle;
- \(\theta(s)\) is the tangential angle of the center curve.

The region swept by the needle is exactly the bidirectional normal strip of the center curve.

## 1.2 1D Skew-Line Expansion of 2D Total Measure

The second node proposes: a 2D set can be transformed, under the condition of total measure conservation, into capacity, topology, bifurcation, direction, and multi-scale skewness structures on a 1D parameter domain.

The core question is:

\[
\text{How can the same total measure of one be distributed in different geometric ways?}
\]

However, the 1D expansion of a general 2D set is not necessarily unique, nor is it necessarily information-faithful.

## 1.3 1D Indexing, Distance Kernels, and Covering Tension

The third node points out: if only the 1D order is retained, the original geometry is usually lost; if the complete two-point distance kernel is added

\[
D(s,t),
\]

then the original metric structure can be recovered on the quotient space.

Congruent inclusion can also be rewritten as an isometric embedding, and the uncovered portion can be measured by distance tension.

---

# 2. The Core Unification of This Paper

This paper combines the three into the following chain:

\[
\boxed{
\begin{aligned}
\text{Kakeya external directional phase}
&\longrightarrow
\text{Center curve internal tangential phase}\\
&\longrightarrow
\text{Bidirectional normal positive-thickness sweeping}\\
&\longrightarrow
\text{Measure-preserving skew-line fibers}\\
&\longrightarrow
\text{Information-faithful distance kernel}\\
&\longrightarrow
\text{Universal covering tension}\\
&\longrightarrow
\text{Moser-type minimal container}.
\end{aligned}
}
\]

The key to this chain is not just conceptual similarity, but that each layer has a clear mathematical interface.

---

# 3. Center Curve and Frenet Frame

Let

\[
\gamma:[0,L]\to\mathbb R^2
\]

be a \(C^2\) arc-length parameterized curve:

\[
\|\gamma'(s)\|=1.
\]

Define the tangent vector:

\[
T(s)=\gamma'(s),
\]

the normal vector:

\[
N(s)=R_{\pi/2}T(s),
\]

and let:

\[
T(s)
=
(\cos\theta(s),\sin\theta(s)).
\]

The curvature is:

\[
\kappa(s)=\theta'(s).
\]

The Frenet formulas are:

\[
T'(s)=\kappa(s)N(s),
\]

\[
N'(s)=-\kappa(s)T(s).
\]

---

# 4. Orthogonal Kakeya Motion

## Definition 4.1

Given a thickness radius \(\rho>0\), for each \(s\) define the normal needle:

\[
I_s
=
\left\{
\gamma(s)+tN(s):
-\rho\le t\le\rho
\right\}.
\]

Its length is:

\[
2\rho.
\]

The directional angle of the needle is:

\[
\phi(s)=\theta(s)+\frac{\pi}{2}.
\]

Because:

\[
T(s)\cdot N(s)=0,
\]

the velocity of the needle's center is always perpendicular to the needle's direction.

This is called the orthogonal Kakeya motion generated by \(\gamma\).

---

## Proposition 4.2: Directional Completeness

If:

\[
\theta(L)-\theta(0)\ge\pi,
\]

then the normal needle experiences all undirected directions.

If:

\[
\theta(L)-\theta(0)\ge2\pi,
\]

then the normal needle experiences all directed directions.

---

# 5. Bidirectional Normal Strip and Complete Tubular Neighborhood

Define the normal parameterization:

\[
F_\rho(s,t)
=
\gamma(s)+tN(s).
\]

The bidirectional normal strip is:

\[
S_\rho(\gamma)
=
F_\rho
\left(
[0,L]\times[-\rho,\rho]
\right).
\]

If semicircular caps of radius \(\rho\) are added at both ends, we obtain the complete tubular neighborhood:

\[
T_\rho(\gamma)
=
\gamma\oplus\rho B.
\]

We must distinguish between:

- \(S_\rho(\gamma)\): the direct sweeping of the normal cross-sections;
- \(T_\rho(\gamma)\): the complete thickening after taking the Minkowski sum with a disk of radius \(\rho\).

The simple translation law of the support function applies to \(T_\rho(\gamma)\).

---

# 6. Valid Tubular Condition

If:

\[
\operatorname{reach}(\gamma)>\rho,
\]

then every point at a distance less than \(\rho\) from the center curve has a unique nearest center point.

This guarantees:

1. The interior of the normal strip does not self-overlap;
2. \(F_\rho\) is injective within the parameter rectangle;
3. The local radius of curvature is greater than \(\rho\);
4. The Jacobian does not change sign.

All exact area and invertible expansion theorems in this paper are first stated under the condition:

\[
\operatorname{reach}(\gamma)>\rho
\]

The contact-saturated case:

\[
\operatorname{reach}(\gamma)=\rho
\]

is studied as its boundary limit.

---

# 7. Area Invariant

## Theorem 7.1: Area Invariant of Non-Overlapping Orthogonal Sweeping

If:

\[
\operatorname{reach}(\gamma)>\rho,
\]

then:

\[
\boxed{
\mu_2(S_\rho(\gamma))
=
2\rho L.
}
\]

### Proof

For the normal parameterization:

\[
F_\rho(s,t)=\gamma(s)+tN(s),
\]

we have:

\[
\partial_sF_\rho
=
T(s)+tN'(s)
=
(1-t\kappa(s))T(s),
\]

and:

\[
\partial_tF_\rho=N(s).
\]

Thus the Jacobian is:

\[
J_\rho(s,t)
=
\det
\left(
\partial_sF_\rho,\partial_tF_\rho
\right)
=
1-t\kappa(s).
\]

By the reach condition:

\[
1-t\kappa(s)>0.
\]

Therefore:

\[
\begin{aligned}
\mu_2(S_\rho(\gamma))
&=
\int_0^L
\int_{-\rho}^{\rho}
(1-t\kappa(s))
\,dt\,ds\\
&=
\int_0^L
2\rho\,ds\\
&=
2\rho L.
\end{aligned}
\]

This completes the proof.

---

## Corollary 7.2: Tubular Neighborhood with End Caps

For an open curve:

\[
\boxed{
\mu_2(T_\rho(\gamma))
=
2\rho L+\pi\rho^2.
}
\]

For a simple closed curve:

\[
\boxed{
\mu_2(T_\rho(\gamma))
=
2\rho L.
}
\]

---

# 8. Measure-Preserving Expansion

Let the normal parameter rectangle be:

\[
Q_{\rho,L}
=
[0,L]\times[-\rho,\rho].
\]

Define a measure on \(Q_{\rho,L}\):

\[
d\lambda_{\gamma,\rho}
=
(1-t\kappa(s))\,ds\,dt.
\]

By the area formula:

\[
(F_\rho)_*
\lambda_{\gamma,\rho}
=
\mu_2|_{S_\rho(\gamma)}.
\]

Therefore, the 2D area is not approximated into 1D data, but is exactly pulled back to a weighted measure on:

\[
\boxed{
\text{1D center base space}
\times
\text{1D normal fibers}
}
\]

---

## Definition 8.1: Measure-Preserving Skew-Line Fiber Expansion

Define:

\[
\mathfrak U_\rho
\left(
S_\rho(\gamma)
\right)
=
\left(
[0,L],
\{\mathcal F_s\}_{s\in[0,L]},
J_\gamma,
D_{\gamma,\rho}
\right),
\]

where:

\[
\mathcal F_s=[-\rho,\rho],
\]

\[
J_\gamma(s,t)=1-t\kappa(s),
\]

and \(D_{\gamma,\rho}\) is the distance kernel defined later.

This expansion is not an ordinary projection, nor does it merely retain the center curve; rather, it is:

\[
\boxed{
\text{1D base}
+
\text{normal fibers}
+
\text{measure Jacobian}
+
\text{geometric relation kernel}.
}
\]

---

# 9. Base Marginal Uniformity Theorem

For the normalized area measure of the normal strip, define:

\[
\nu_{\gamma,\rho}
=
\frac{\mu_2|_{S_\rho(\gamma)}}{2\rho L}.
\]

Let:

\[
\pi_s:
Q_{\rho,L}\to[0,L],
\qquad
\pi_s(s,t)=s.
\]

## Theorem 9.1: Base Marginal Uniformity

After projecting the normalized 2D area along the center parameter, we obtain:

\[
\boxed{
(\pi_s)_*
(F_\rho^{-1})_*
\nu_{\gamma,\rho}
=
\frac{ds}{L}.
}
\]

### Proof

For any measurable set \(E\subset[0,L]\):

\[
\begin{aligned}
\nu_{\gamma,\rho}
\left(
F_\rho(E\times[-\rho,\rho])
\right)
&=
\frac{1}{2\rho L}
\int_E
\int_{-\rho}^{\rho}
(1-t\kappa(s))
\,dt\,ds\\
&=
\frac{1}{2\rho L}
\int_E2\rho\,ds\\
&=
\frac{|E|}{L}.
\end{aligned}
\]

This completes the proof.

---

## Explanation

This theorem states:

\[
\boxed{
\text{Every unit of arc length carries the same total area }2\rho\,ds.
}
\]

Therefore, the normalized 2D total measure is exactly expanded into a uniform 1D capacity line.

This is precisely the exact realization of "normalized 2D total measure expanding to one" in tubular geometry.

---

# 10. Curvature Does Not Disappear: It Transfers to Fiber Skewness

Although the base marginal is uniform, for a fixed \(s\), the conditional density on the fiber is:

\[
\boxed{
p_s(t)
=
\frac{1-t\kappa(s)}{2\rho},
\qquad
-\rho\le t\le\rho.
}
\]

This density is linear in \(t\).

If:

\[
\kappa(s)=0,
\]

then:

\[
p_s(t)=\frac{1}{2\rho},
\]

the fiber distribution is completely uniform.

If:

\[
\kappa(s)>0,
\]

then the density increases on one side of the fiber and decreases on the other.

Therefore, after 1D reduction, curvature manifests as:

\[
\boxed{
\text{measure skewness within the normal fibers}.
}
\]

---

# 11. Curvature–Fiber First Moment Theorem

## Theorem 11.1

The conditional expected position of the fiber satisfies:

\[
\boxed{
m_\gamma(s)
:=
\mathbb E[t\mid s]
=
-\frac{\rho^2}{3}\kappa(s).
}
\]

Therefore:

\[
\boxed{
\kappa(s)
=
-\frac{3}{\rho^2}m_\gamma(s).
}
\]

### Proof

\[
\begin{aligned}
m_\gamma(s)
&=
\int_{-\rho}^{\rho}
t\,p_s(t)\,dt\\
&=
\frac{1}{2\rho}
\int_{-\rho}^{\rho}
t(1-t\kappa(s))\,dt\\
&=
-\frac{\kappa(s)}{2\rho}
\int_{-\rho}^{\rho}t^2\,dt\\
&=
-\frac{\kappa(s)}{2\rho}
\cdot
\frac{2\rho^3}{3}\\
&=
-\frac{\rho^2}{3}\kappa(s).
\end{aligned}
\]

This completes the proof.

---

## Corollary 11.2: Curvature Skew Line

We can define a 1D skew line:

\[
K_{\gamma,\rho}(s)
=
m_\gamma(s).
\]

Then:

\[
K_{\gamma,\rho}(s)=0
\]

corresponds to a local straight line,

\[
K_{\gamma,\rho}(s)\ne0
\]

corresponds to local curvature.

At this point, the "skew line" is no longer just a conceptual feature, but possesses an exact geometric inversion formula.

---

# 12. Information-Faithful Reconstruction Theorem

## Theorem 12.1: Reconstructing the Center Curve from the Fiber Skew Line

Given:

1. Curve length \(L\);
2. Thickness \(\rho\);
3. Fiber first moment function \(m_\gamma(s)\);
4. Initial position \(\gamma(0)\);
5. Initial tangential angle \(\theta(0)\).

Then \(\gamma\) can be uniquely reconstructed.

### Proof

By Theorem 11.1:

\[
\kappa(s)
=
-\frac{3}{\rho^2}m_\gamma(s).
\]

Integrating yields:

\[
\theta(s)
=
\theta(0)
+
\int_0^s\kappa(u)\,du.
\]

Finally:

\[
\gamma(s)
=
\gamma(0)
+
\int_0^s
(\cos\theta(u),\sin\theta(u))
\,du.
\]

This completes the proof.

---

## Corollary 12.2: Information Faithfulness in Rigid Body Equivalence Classes

If the initial position and initial angle are ignored, then:

\[
m_\gamma(s)
\]

determines the center curve up to a translation and rotation.

Therefore, within the class of valid tubular curves with fixed orientation parameters:

\[
\boxed{
(L,\rho,m_\gamma)
}
\]

is an information-faithful 1D representation of the rigid body equivalence class of the center curve.

If reflection or reverse parameterization is allowed, one must also establish the corresponding quotient relation for:

\[
m(s)
\longleftrightarrow
-m(L-s)
\]

---

# 13. Expansion–Backfilling Duality

Define the backfilling operator:

\[
\mathfrak T_\rho
(\gamma)
=
S_\rho(\gamma).
\]

Define the expansion operator:

\[
\mathfrak U_\rho
(S_\rho(\gamma))
=
(L,\rho,m_\gamma,D_{\gamma,\rho}).
\]

In the valid tubular class:

\[
\boxed{
\mathfrak T_\rho
\circ
\mathfrak R_\rho
\circ
\mathfrak U_\rho
=
\operatorname{Id},
}
\]

where \(\mathfrak R_\rho\) denotes the reconstruction of the center curve from \(m_\gamma\).

In other words:

\[
\boxed{
\text{2D normal strip}
\longrightarrow
\text{1D fiber skew line}
\longrightarrow
\text{center curve}
\longrightarrow
\text{2D normal strip}
}
\]

constitutes a measure-preserving expansion–backfilling cycle.

Note: This is not a general theorem for all 2D sets, but holds for sets with a unique normal tubular structure.

---

# 14. Information-Faithful Distance Kernel

Even though the fiber first moment is sufficient to reconstruct a valid center curve, a more general proof layer is still needed to handle:

- Contact saturation;
- Boundary degeneration;
- Different parameterizations;
- Non-standard fibers;
- General congruent embeddings;
- Faithful verification after numerical approximation.

For parameter points:

\[
z=(s,t),
\qquad
z'=(s',t'),
\]

define:

\[
\boxed{
D_{\gamma,\rho}(z,z')
=
\left\|
F_\rho(s,t)-F_\rho(s',t')
\right\|.
}
\]

If the normal parameterization loses injectivity, then \(D\) is a pseudometric. Define:

\[
z\sim z'
\iff
D_{\gamma,\rho}(z,z')=0.
\]

The quotient space:

\[
X_{\gamma,\rho}
=
Q_{\rho,L}/\!\sim
\]

equipped with the distance induced by \(D\), is isometric to the Euclidean metric space of the normal strip.

Therefore:

\[
\boxed{
\text{The skew-line fiber is a low-cost representation layer;
the distance kernel is an information-faithful proof layer.}
}
\]

---

# 15. Global 1D Indexing

If full integration with general 1D indexing theory is needed, one can take a surjection:

\[
\eta:[0,1]\to Q_{\rho,L},
\]

and define:

\[
q_{\gamma,\rho}
=
F_\rho\circ\eta.
\]

The distance kernel on the 1D index is:

\[
\widetilde D_{\gamma,\rho}(u,v)
=
\left\|
q_{\gamma,\rho}(u)
-
q_{\gamma,\rho}(v)
\right\|.
\]

Therefore, the complete 2D normal strip can be represented as:

\[
\boxed{
[0,1]
+
\widetilde D_{\gamma,\rho}(u,v).
}
\]

However, this global flattening hides the natural center curve–normal fiber structure.

Thus, this paper advocates:

- The geometric modeling layer uses a 1D base + fibers;
- The information-faithful proof layer can use a 1D index + distance kernel.

---

# 16. Minimal Sufficient Skew Line

A general 2D set may require the complete distance kernel for a faithful representation.

But for the valid tubular curve class in this paper, it has been proven that:

\[
m_\gamma(s)
\]

is sufficient to recover the curvature and the center curve.

Therefore, we can propose:

## Proposition 16.1: Task-Sufficient Skew Line

For the task:

\[
\mathcal T
=
\text{Rigid body identity determination of valid tubular curves},
\]

the representation:

\[
\mathfrak U^\star_{\mathcal T}
(\gamma)
=
(L,\rho,m_\gamma)
\]

is information-sufficient under fixed orientation parameters.

This is a precise candidate for the "minimal sufficient skew line" concept.

It is smaller than the complete distance kernel, but only applies to the restricted curve class.

---

# 17. Individual Area Conservation and Heteromorphic Tension

For all valid center curves:

\[
\mu_2(S_\rho(\gamma))
=
2\rho L.
\]

Therefore:

\[
\mu_2(S_\rho(\gamma_1))
=
\mu_2(S_\rho(\gamma_2))
\]

holds for any valid curves of the same length and same thickness.

But their:

- Support functions;
- Convex hulls;
- Directional widths;
- Distance kernels;
- Container embedding difficulties;

are generally different.

So:

\[
\boxed{
\text{Same total measure}
\not\Rightarrow
\text{Same accommodation tension}.
}
\]

This leads to the central principle of this paper:

\[
\boxed{
\text{After total measure is conserved, shape differences transform into differences in skewness and tension.}
}
\]

---

# 18. Uncovered Distance Tension

For a compact closed container \(C\subset\mathbb R^2\), define the local uncovered tension under a fixed configuration:

\[
\delta_{\gamma,\rho,C}(x;g)
=
\operatorname{dist}(gx,C).
\]

Let:

\[
\nu_{\gamma,\rho}
=
\frac{
\mu_2|_{T_\rho(\gamma)}
}{
\mu_2(T_\rho(\gamma))
}
\]

be the normalized area measure of the thickened curve.

For:

\[
1\le p<\infty,
\]

define:

\[
N_p
(T_\rho(\gamma),C;g)
=
\left[
\int_{T_\rho(\gamma)}
\operatorname{dist}(gx,C)^p
\,d\nu_{\gamma,\rho}(x)
\right]^{1/p}.
\]

Then take the infimum over rigid body motions:

\[
N_p
(T_\rho(\gamma),C)
=
\inf_{g\in E(2)}
N_p
(T_\rho(\gamma),C;g).
\]

---

## Theorem 18.1: Zero Tension and Exact Inclusion

If \(T_\rho(\gamma)\) is a compact set and \(C\) is a closed set, then:

\[
\boxed{
N_p(T_\rho(\gamma),C)=0
}
\]

under appropriate compactness conditions where the minimum is attainable or a zero-tension limit configuration exists, is equivalent to the existence of:

\[
g\in E(2)
\]

such that:

\[
gT_\rho(\gamma)\subseteq C.
\]

The version with fixed \(g\) holds directly:

\[
N_p(T_\rho(\gamma),C;g)=0
\iff
gT_\rho(\gamma)\subseteq C.
\]

---

# 19. Center-Generated Bridge Family

Let:

\[
\Gamma_{\mathrm{CG}}(L,\rho,\tau)
\]

be the family of center curves satisfying the following conditions:

1. \(C^2\) arc-length parameterized;
2. Length is \(L\);
3. \(\gamma(0)=0\);
4. Radially non-retrograde;
5. Tangential phase is monotonic;
6. Total turning is at least \(\tau\);
7. \(\operatorname{reach}(\gamma)>\rho\).

When:

\[
\tau=\pi
\]

the normal needle completes all undirected directions.

When:

\[
\tau=2\pi
\]

it completes all directed directions.

---

# 20. Universal Covering Tension

Define:

\[
\boxed{
\mathfrak T_p
(C;L,\rho,\tau)
=
\sup_{\gamma\in\Gamma_{\mathrm{CG}}(L,\rho,\tau)}
N_p(T_\rho(\gamma),C).
}
\]

Its meaning is:

> Among all valid center-generated thickened curves, select the object for which it is hardest to eliminate the uncovered tension with respect to the container \(C\).

If:

\[
\mathfrak T_p(C;L,\rho,\tau)=0,
\]

then every curve in the bridge family can be placed into \(C\) under some rigid body configuration.

---

# 21. Bridge Universal Accommodation Functional

Define:

\[
\boxed{
\mathfrak B
(L,\rho,\tau)
=
\inf_C
\left\{
\mu_2(C):
\mathfrak T_p(C;L,\rho,\tau)=0
\right\}.
}
\]

This is the positive-thickness center-generated Kakeya–Moser bridge problem of this paper.

It is not:

- The original Kakeya problem;
- The complete Moser's worm problem;
- The Lebesgue universal covering problem.

It is a controlled intermediate family between directionally complete motion and the universal accommodation of all unit curves.

---

# 22. Basic Area Lower Bound

Any container capable of accommodating all bridge objects must at least accommodate one complete thickened curve.

Therefore:

\[
\boxed{
\mathfrak B(L,\rho,\tau)
\ge
2\rho L+\pi\rho^2.
}
\]

For the normal strip version without end caps:

\[
\boxed{
\mathfrak B_{\mathrm{strip}}
(L,\rho,\tau)
\ge
2\rho L.
}
\]

Define the universal accommodation margin:

\[
\Xi(L,\rho,\tau)
=
\mathfrak B_{\mathrm{strip}}
(L,\rho,\tau)
-
2\rho L.
\]

The truly non-trivial question is:

\[
\boxed{
\Xi(L,\rho,\tau)
\stackrel{?}{>}0.
}
\]

---

# 23. Support Function Interface

The complete tubular neighborhood satisfies:

\[
T_\rho(\gamma)
=
\gamma\oplus\rho B.
\]

Therefore:

\[
\boxed{
h_{T_\rho(\gamma)}(u)
=
h_\gamma(u)+\rho.
}
\]

If the container gap field is defined as:

\[
K_{C,\gamma}
(\vartheta;\phi,a)
=
h_\gamma(\vartheta-\phi)
+
a\cdot u_\vartheta
-
h_C(\vartheta),
\]

then after thickening:

\[
\boxed{
K_{C,T_\rho(\gamma)}
=
K_{C,\gamma}+\rho.
}
\]

So the effect of positive thickness is:

\[
\boxed{
\text{The support pressure in all directions is uniformly elevated by }\rho.
}
\]

While the curvature distribution and the shape of the center curve determine the angular non-uniform skewness.

---

# 24. Three-Layer Architecture of Support, Tension, and Distance Kernel

This paper proposes a three-layer computation–proof architecture.

## 24.1 Support Layer

Uses:

\[
h_\gamma(\vartheta)
\]

and:

\[
K_{C,\gamma}(\vartheta)
\]

to quickly analyze directional pressure, phase, contact branches, and hard cases.

## 24.2 Tension Layer

Uses:

\[
N_p(T_\rho(\gamma),C)
\]

to measure the overall covering gap that the candidate container has yet to eliminate.

## 24.3 Distance Kernel Layer

Uses:

\[
D_{\gamma,\rho}
\]

to perform information-faithful geometric identity, isometric embedding, and final certificate verification.

Therefore:

\[
\boxed{
\text{support}
+
\text{tension}
+
\text{metric kernel}
}
\]

are respectively responsible for:

- Fast necessary conditions;
- Worst-case curve search and container optimization;
- Final faithful verification.

---

# 25. Division of Labor Between Skewness Field and Tension Functional

We can define the 1D state of the center-generated curve:

\[
\mathbf K_{\gamma,\rho}(s)
=
\left(
m_\gamma(s),
\kappa(s),
\theta(s),
r(s),
\operatorname{reach}_s(\gamma)
\right).
\]

Then add the directional parameter:

\[
\mathbf K_{\gamma,\rho}(s,\vartheta)
=
\left(
\mathbf K_{\gamma,\rho}(s),
h_\gamma(\vartheta),
K_{C,\gamma}(\vartheta)
\right).
\]

Where:

\[
\boxed{
\text{Skewness field}
}
\]

is responsible for local structure and candidate generation;

\[
\boxed{
\text{Covering tension}
}
\]

is responsible for global feasibility and worst-case determination.

---

# 26. Inclusion Relations Among Kakeya, Bridge Problems, and Moser

Let:

- \(\mathcal L\): Family of unit line segment directions;
- \(\Gamma_{\mathrm{CG}}\): Family of center-generated directionally complete curves;
- \(\mathcal C_L\): Family of all curves of length \(L\).

At the center curve layer, this can be written as:

\[
\mathcal L
\subset
\Gamma_{\mathrm{CG}}
\subset
\mathcal C_L
\]

an investigative inclusion relation, but note that:

- The original Kakeya also includes the requirement of a continuous motion path;
- Moser only requires the existence of an optimal placement for each curve individually;
- The bridge problem adds positive thickness, center generation, and non-overlapping.

Therefore, the three are not equivalent problems.

---

# 27. Heteromorphic Tension Separation Proposition for Equal Measures

## Proposition 27.1

There exist valid center curves of the same length and same thickness:

\[
\gamma_1,\gamma_2
\]

such that:

\[
\mu_2(S_\rho(\gamma_1))
=
\mu_2(S_\rho(\gamma_2)),
\]

but their support functions are different:

\[
h_{\gamma_1}
\ne
h_{\gamma_2}.
\]

Therefore, there exist certain containers \(C\) such that:

\[
N_p(T_\rho(\gamma_1),C)
\ne
N_p(T_\rho(\gamma_2),C).
\]

### Explanation

The area invariant only preserves the total measure, not the shape.

The curvature skew line, support function, and distance kernel preserve the shape distribution.

---

# 28. New Conjectures

## Conjecture 28.1: Positive Universal Margin

For some:

\[
L,\rho,\tau>0,
\]

we have:

\[
\boxed{
\Xi(L,\rho,\tau)>0.
}
\]

That is, there does not exist a region with an area exactly equal to the individual swept area that can accommodate all bridge family objects.

---

## Conjecture 28.2: Thin-Thickness Normalized Limit

Study:

\[
c(L,\tau)
=
\lim_{\rho\to0^+}
\frac{
\mathfrak B_{\mathrm{strip}}(L,\rho,\tau)
}{
2\rho L
},
\]

if the limit exists.

Possible scenarios:

\[
c(L,\tau)=1
\]

indicates that the universal margin is a higher-order infinitesimal;

\[
c(L,\tau)>1
\]

indicates that directional completeness still leaves a fixed cost after zero-thickness normalization.

---

## Conjecture 28.3: Contact Saturation Principle

The curve with the most universal container pressure may lie on the boundary:

\[
\operatorname{reach}(\gamma)=\rho
\]

That is, adjacent parts just touch, but no positive-area overlap occurs.

---

## Conjecture 28.4: Finite-Width Curvature Concentration

The hard case in the bridge family is not necessarily a constant-curvature spiral.

There may exist a finite-width curvature layer:

\[
\kappa_\varepsilon(s)
\]

that produces a higher container tension than a zero-width vertex or a uniform curvature distribution.

---

## Conjecture 28.5: Task-Sufficient Kernel

For the bridge universal accommodation task, there may exist a representation smaller than the complete distance kernel:

\[
\mathfrak U^\star_{\mathrm{bridge}}
\]

that retains all the information needed to determine:

\[
N_p(T_\rho(\gamma),C)=0
\]

but has a lower computational cost than the complete \(D_{\gamma,\rho}\).

Candidates include:

\[
(
m_\gamma,
h_\gamma,
\mathcal E_{\mathrm{contact}},
\operatorname{reach}
).
\]

---

# 29. Computational Research Architecture

## 29.1 Curve Generation

Using the curvature function as the main variable:

\[
\kappa(s).
\]

From:

\[
\theta(s)
=
\theta_0+\int_0^s\kappa(u)\,du
\]

and:

\[
\gamma(s)
=
\gamma_0+
\int_0^s
(\cos\theta(u),\sin\theta(u))
\,du
\]

reconstruct the center curve.

## 29.2 Validity Check

Check:

\[
\operatorname{reach}(\gamma)\ge\rho,
\]

Total turning:

\[
\int_0^L\kappa(s)\,ds\ge\tau,
\]

and center-generation conditions.

## 29.3 Skew-Line Representation

Compute:

\[
m_\gamma(s)
=
-\frac{\rho^2}{3}\kappa(s).
\]

## 29.4 Support Pressure

Compute:

\[
h_\gamma(\vartheta),
\qquad
K_{C,T_\rho(\gamma)}.
\]

## 29.5 Tension Optimization

Compute:

\[
\inf_{g\in E(2)}
N_p(T_\rho(\gamma),C;g).
\]

## 29.6 Faithful Verification

For the most difficult candidates, establish discrete matrices, interval certificates, or formalized congruent inclusion determinations for:

\[
D_{\gamma,\rho}
\]

---

# 30. Proof Levels

This paper advocates strictly distinguishing the following levels.

## Level 1: Skew-Line Heuristics

Uses:

\[
m_\gamma(s),
\quad
\kappa(s),
\quad
h_\gamma
\]

to search for hard cases.

## Level 2: Tension Computation

Uses:

\[
N_p
\]

to compare candidate containers and curves.

## Level 3: Distance Kernel Faithful Verification

Uses:

\[
D_{\gamma,\rho}
\]

to confirm that the geometry is not distorted by the compressed representation.

## Level 4: Interval Arithmetic

Bounds:

- Curve integrals;
- Support extrema;
- Rigid body configurations;
- Tension lower bounds.

## Level 5: Formal Proofs

Formalize in Lean, Coq, or other systems:

- Tubular area formula;
- Base marginal uniformity;
- Curvature first moment inversion;
- Zero-tension inclusion equivalence;
- Specific finite certificates.

---

# 31. What Has Been Proven and What Remains Unproven in This Paper

## Proven or Having Direct Standard Proofs

1. Orthogonal Kakeya sweeping equals the bidirectional normal strip;
2. The area of a valid normal strip is \(2\rho L\);
3. The center arc-length marginal of the normalized area is a uniform measure;
4. The fiber conditional density is:
   \[
   p_s(t)=\frac{1-t\kappa(s)}{2\rho};
   \]
5. The fiber first moment recovers the curvature;
6. The curvature and initial frame recover the center curve;
7. The support function of the complete thickening increases by \(\rho\);
8. Under a fixed configuration, zero distance tension is equivalent to exact inclusion.

## Unproven

1. The optimal shape of the bridge universal container;
2. \(\Xi(L,\rho,\tau)>0\);
3. The existence of the thin-thickness normalized limit;
4. Contact-saturated curves must be hard cases;
5. The optimal width of the curvature concentration family;
6. The existence and uniqueness of the minimal task-sufficient kernel;
7. Whether the bridge family can improve the known bounds of the complete Moser problem;
8. Complete formal proofs.

---

# 32. Theoretical Significance

This paper obtains a more precise conclusion than "2D to 1D".

For valid tubular curves:

\[
\boxed{
\text{2D total measure}
=
\text{1D uniform capacity base}
+
\text{normal fiber skewness}.
}
\]

The 1D base preserves:

\[
\frac{ds}{L},
\]

The fiber skewness preserves:

\[
\kappa(s).
\]

Therefore:

\[
\boxed{
\text{Area conservation}
\quad\text{and}\quad
\text{shape information conservation}
}
\]

can hold simultaneously in this restricted geometric class.

And when the total areas of the individual objects are all identical, what truly needs to be optimized is no longer the individual area, but:

\[
\boxed{
\text{the universal covering tension caused by multiple heteromorphic objects of equal measure on the same container.}
}
\]

---

# 33. Conclusion

This paper unifies the original Kakeya, center-generated spirals, measure-preserving skew lines, information-faithful distance kernels, and Moser universal accommodation into:

\[
\boxed{
\text{Measure-Preserving Skew-Line Fiber—Universal Covering Tension Theory}.
}
\]

Its core chain is:

\[
\boxed{
\begin{aligned}
\phi(s)
&=
\theta(s)+\frac{\pi}{2},\\
S_\rho(\gamma)
&=
\bigcup_s I_s,\\
\mu_2(S_\rho(\gamma))
&=
2\rho L,\\
(\pi_s)_*\nu_{\gamma,\rho}
&=
\frac{ds}{L},\\
p_s(t)
&=
\frac{1-t\kappa(s)}{2\rho},\\
\kappa(s)
&=
-\frac{3}{\rho^2}\mathbb E[t\mid s],\\
D_{\gamma,\rho}
&=
\text{Information-faithful kernel},\\
\mathfrak T_p(C)
&=
\text{Universal covering tension},\\
\mathfrak B
&=
\inf\{\mu_2(C):\mathfrak T_p(C)=0\}.
\end{aligned}
}
\]

Therefore, the basic philosophy of this new framework can be condensed as:

\[
\boxed{
\text{After total measure is conserved, geometry does not disappear;
it transforms from area differences into fiber skewness, distance relations, and covering tension.}
}
\]

The area degeneration in the original Kakeya problem is blocked under the conditions of positive thickness and non-overlapping; the individual area consequently becomes an invariant. The non-triviality of the problem thus shifts to a Moser-type problem:

\[
\boxed{
\text{Which minimal container can simultaneously eliminate the covering tension of all heteromorphic sweeps of equal measure?}
}
\]

This is the unified bridge problem proposed in this paper, and it is also the starting point for subsequent computations, interval certificates, and formalization research.

---

# References and Theoretical Origins

1. Neo.K, "From 2D Total Measure to 1D Skew Lines: A Measure-Preserving Geometric Expansion Framework", v0.1.
2. Neo.K, "From 1D Metric Lines to Universal Covering Tension: 1D Propositional Conjectures, Information-Faithful Conditions, and Local Reduction Methodologies for the Lebesgue Universal Covering Problem", v0.1.
3. Neo.K, "From the Original Kakeya Needle to the Moser Worm: Positive-Thickness Bridge Theory of Center-Generated Bidirectional Offset Spirals", v0.1.
4. A. S. Besicovitch, classical research on the Kakeya problem and sets of directional line segments.
5. R. Norwood, G. Poole, M. Laidacker, research on Leo Moser's worm problem.