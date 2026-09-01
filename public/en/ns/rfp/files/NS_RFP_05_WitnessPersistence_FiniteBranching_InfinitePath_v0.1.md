---
title: "Navier–Stokes Reverse Formation Program 05: Witness Persistence, Finite Branching, Survivor Recursion, and Infinite Ancestry Path Extraction"
short_title: "NS-RFP 05"
version: "v0.1"
date: "2026-08-14"
author: "Neo.K / EveMissLab"
language: "en"
status: "Theorem-style quantifier-closure architecture / persistence reduction"
epistemic_status: "Proves a finite-branching path-extraction theorem for thresholded RFP witness graphs, gives an exact backward survivor recursion and finite-horizon obstruction certificate, and separates persistent infinite ancestry from bottleneck-collapse escape. The graph theorem is exact once the node and compatibility certificates are supplied. The PDE bridge score needed for full provenance compatibility remains open. This paper does NOT prove full Chain Necessity, Finite Obstruction for all Navier–Stokes ancestries, or Navier–Stokes regularity."
canonical_source: "UTF-8 Markdown"
---

# Navier–Stokes Reverse Formation Program 05

# Witness Persistence, Finite Branching, Survivor Recursion, and Infinite Ancestry Path Extraction

## 0. Context of this Paper

NS-RFP 02 established:

$$
\boxed{
\text{first-passage levels}
}
$$

and:

$$
\boxed{
\text{nonlinear source debt}.
}
$$

NS-RFP 03 established the:

$$
\boxed{
(k;p,q)
}
$$

exact signed parent-output ledger.

NS-RFP 04 further established the:

$$
\boxed{
(a;k;p,q)
}
$$

spacetime soft-tube ledger,

as well as the quantitative parent tightness criterion:

$$
\boxed{
1-C_J^{par}(L)
\le
C2^{-L}\mathfrak V_J.
}
$$

Therefore:

$$
\sup_J\mathfrak V_J<\infty
$$

can upgrade subsequential parent tightness to quantitative uniform parent tightness.

However, RFP-04 explicitly left open:

$$
\boxed{
\textbf{Witness Persistence / Chain Stitching}.
}
$$

That is:

$$
\boxed{
\forall J\;\exists v_J
}
$$

cannot be surreptitiously replaced by:

$$
\boxed{
\exists(v_J)_{J\ge J_0}
\;\forall J:
v_J\text{ compatible with }v_{J+1}.
}
$$

This paper specifically addresses this global quantifier gap.

---

# 1. Core no-go: Layer-wise existence does not equal persistent existence

Even if every first-passage level:

$$
J
$$

has a good spacetime witness:

$$
v_J,
$$

it is possible that all witnesses at level $J$ only extend to a finite depth,

while level $J+1$ utilizes another batch of mutually incompatible witnesses.

Thus, in general:

$$
\boxed{
\forall J\;\exists v_J
\quad\not\Rightarrow\quad
\exists(v_J)_J\;\forall J.
}
$$

More precisely,

layer-wise existence:

$$
v_J\in V_J
$$

does not imply the existence of an:

$$
v_J\sim_Jv_{J+1}
$$

infinite compatible sequence.

This is not a problem unique to Navier–Stokes,

but rather a quantifier issue when upgrading finite-horizon information to an infinite path.

---

# 2. RFP-04 local-source ledger

RFP-04 defines:

$$
\Lambda^{loc,(J)}_{a;k;p,q}
=
-
\int_{s_J}^{t_J}
\left\langle
\mathcal T_k
\left(
\chi_{J,a}
u_p\otimes u_q
\right),
\varphi_{J,k}
\right\rangle dr,
$$

where:

$$
\mathcal T_k
=
\Delta_k\mathbb P\nabla\cdot.
$$

Since:

$$
\sum_a\chi_{J,a}=1,
$$

there is an exact refinement explicitly stated for the first time in this paper.

---

# 3. C5.1 — Exact Local-Source Refinement

## Theorem 3.1

For each:

$$
k,p,q,
$$

we have:

$$
\boxed{
\sum_a
\Lambda^{loc,(J)}_{a;k;p,q}
=
\Lambda^{(J)}_{k;p,q}.
}
$$

Therefore:

$$
\boxed{
\sum_{a,k,p,q}
\Lambda^{loc,(J)}_{a;k;p,q}
=
R_J.
}
$$

### Proof

By linearity:

$$
\sum_a
\mathcal T_k
\left(
\chi_{J,a}
F_{p,q}
\right)
=
\mathcal T_k
\left(
\left(
\sum_a\chi_{J,a}
\right)
F_{p,q}
\right)
=
\mathcal T_kF_{p,q}.
$$

Substituting this back into the dual pairing and time integral yields the result. $\square$

---

# 4. Local positive / negative ledger

Define:

$$
\boxed{
P_J^{loc}
=
\sum_{a,k,p,q}
[
\Lambda^{loc,(J)}_{a;k;p,q}
]_+,
}
$$

and:

$$
\boxed{
N_J^{loc}
=
\sum_{a,k,p,q}
[
\Lambda^{loc,(J)}_{a;k;p,q}
]_-.
}
$$

Then:

$$
\boxed{
P_J^{loc}-N_J^{loc}=R_J>0.
}
$$

Thus:

$$
P_J^{loc}>0.
$$

---

# 5. Positive local-source probability

For each positive local-source entry:

$$
v
=
(a;k;p,q),
$$

define:

$$
\boxed{
\pi_J(v)
=
\frac{
[
\Lambda^{loc,(J)}_v
]_+
}{
P_J^{loc}
}.
}
$$

Then:

$$
\boxed{
\pi_J(v)\ge0,
\qquad
\sum_v\pi_J(v)=1.
}
$$

Therefore, each PF-A edge naturally carries a countable positive witness probability ledger.

Note:

$$
\pi_J
$$

is not a stochastic dynamics.

It is merely a normalized bookkeeping measure of the gross positive local-source activity.

---

# 6. Node strength

We call:

$$
\boxed{
\sigma_J(v)
=
\pi_J(v)
}
$$

the witness node strength.

If:

$$
\sigma_J(v)\ge\theta,
$$

then:

$$
[
\Lambda^{loc,(J)}_v
]_+
\ge
\theta P_J^{loc}
\ge
\theta R_J.
$$

Thus, any fixed positive gross share is automatically a fixed positive net-debt share.

---

# 7. Thresholded witness set

For:

$$
0<\theta\le1,
$$

define:

$$
\boxed{
\mathcal W_J(\theta)
=
\left\{
v:
\sigma_J(v)\ge\theta
\right\}.
}
$$

---

# 8. C5.2 — Uniform Finite-Level Bound

## Theorem 8.1

For all:

$$
J,
$$

we have:

$$
\boxed{
|\mathcal W_J(\theta)|
\le
\left\lfloor
\frac1\theta
\right\rfloor.
}
$$

### Proof

If:

$$
m
=
|\mathcal W_J(\theta)|,
$$

then:

$$
1
=
\sum_v\pi_J(v)
\ge
m\theta.
$$

Hence:

$$
m\le\theta^{-1}.
$$

$\square$

---

# 9. Significance: Finite branching does not require a uniform cancellation gap

The tube cancellation ratio in RFP-04 can be very close to:

$$
1.
$$

But as long as we use the normalized positive local-source probability:

$$
\pi_J,
$$

any fixed node threshold:

$$
\theta>0
$$

automatically yields a:

$$
\boxed{
\text{uniform finite number of strong nodes per level}.
}
$$

Therefore, the finite branching required for graph compactness can be decoupled from the cancellation magnitude.

---

# 10. Maximal witness atom

Define:

$$
\boxed{
\mathfrak a_J
=
\sup_v
\pi_J(v).
}
$$

Since:

$$
\pi_J
$$

is a countable summable positive sequence,

and sums to:

$$
1,
$$

the supremum is attained by some entry.

Thus:

$$
\boxed{
0<\mathfrak a_J\le1.
}
$$

---

# 11. Effective local multiplicity

Define the inverse participation quantity:

$$
\boxed{
\mathfrak M_J^{eff}
=
\left(
\sum_v
\pi_J(v)^2
\right)^{-1}.
}
$$

Then:

$$
\mathfrak M_J^{eff}\ge1.
$$

---

# 12. C5.3 — Atomization / Multiplicity Debt

## Theorem 12.1

We have:

$$
\boxed{
\mathfrak M_J^{eff}
\ge
\frac1{\mathfrak a_J}.
}
$$

Therefore, if:

$$
\mathfrak a_J\to0,
$$

then:

$$
\boxed{
\mathfrak M_J^{eff}\to\infty.
}
$$

### Proof

Since:

$$
\pi_J(v)^2
\le
\mathfrak a_J\pi_J(v),
$$

hence:

$$
\sum_v\pi_J(v)^2
\le
\mathfrak a_J
\sum_v\pi_J(v)
=
\mathfrak a_J.
$$

Taking the reciprocal yields the result. $\square$

---

# 13. Witness atomization escape

If along some subsequence:

$$
\boxed{
\mathfrak a_J\to0,
}
$$

we call this:

$$
\boxed{
\textbf{local witness atomization escape}.
}
$$

Its significance is:

the gross positive local-source activity cannot be carried by any fixed-share spacetime parent witness.

And Theorem 12.1 tells us:

$$
\boxed{
\text{atomization}
\Longrightarrow
\text{effective multiplicity divergence}.
}
$$

So this is not a free escape.

---

# 14. Time seam

The first-passage construction gives:

$$
s_J
=
\tau_J,
$$

$$
t_J
=
\tau_{J+1}.
$$

Therefore, adjacent PF-A edges naturally have:

$$
\boxed{
t_J
=
s_{J+1}.
}
$$

Thus, the time ordering of the persistence graph is not an additional assumption.

What truly needs to be proven is:

$$
\boxed{
\text{frequency/source/spatial compatibility across the shared seam}.
}
$$

---

# 15. Frequency-link predicate

If:

$$
v=(a;k;p,q)
\in\mathcal W_J,
$$

and:

$$
w=(a';k';p',q')
\in\mathcal W_{J+1},
$$

define the strongest first-generation frequency link:

$$
\boxed{
\mathfrak f_J(v,w)
=
\mathbf 1_{
\{
p',q'
\}
\ni k
}.
}
$$

That is, the output shell of the previous edge:

$$
k
$$

must become an exact dyadic parent of the next edge.

This is strong compatibility.

Future work may study bounded-shell bridge versions,

but this paper does not automatically treat:

$$
|k-p'|=O(1)
$$

as an exact parent identity.

---

# 16. Geometric tube seam

At the shared time:

$$
t_J=s_{J+1},
$$

the terminal cutoff of the previous tube:

$$
a
$$

is:

$$
\chi_{J,a}(t_J).
$$

The backward tube of the next edge:

$$
a'
$$

also has at the same time:

$$
\chi_{J+1,a'}(t_J).
$$

Define the normalized geometric overlap:

$$
\boxed{
\mathfrak o_J(a,a')
=
\frac{
\int
\chi_{J,a}(t_J,x)
\chi_{J+1,a'}(t_J,x)
\,dx
}{
\int
\chi_{J,a}(t_J,x)\,dx
}.
}
$$

The terminal cells are compactly supported, so the denominator is finite and positive.

---

# 17. C5.4 — Seam Partition Identity

## Theorem 17.1

For fixed:

$$
J,a,
$$

we have:

$$
\boxed{
\mathfrak o_J(a,a')\ge0,
}
$$

and:

$$
\boxed{
\sum_{a'}
\mathfrak o_J(a,a')
=
1.
}
$$

### Proof

Nonnegativity comes from:

$$
\chi\ge0.
$$

Also, since the adjoint partition of the next edge satisfies:

$$
\sum_{a'}
\chi_{J+1,a'}(t_J,x)=1,
$$

we have:

$$
\begin{aligned}
\sum_{a'}
\mathfrak o_J(a,a')
&=
\frac{
\int
\chi_{J,a}(t_J,x)
\sum_{a'}
\chi_{J+1,a'}(t_J,x)
dx
}{
\int\chi_{J,a}(t_J,x)dx
}
\\
&=
1.
\end{aligned}
$$

$\square$

---

# 18. C5.5 — Effective Spatial Fan-Out Bound

## Theorem 18.1

Fix:

$$
0<\gamma\le1.
$$

Let:

$$
\mathcal A_{J+1}(a;\gamma)
=
\left\{
a':
\mathfrak o_J(a,a')\ge\gamma
\right\}.
$$

Then:

$$
\boxed{
|
\mathcal A_{J+1}(a;\gamma)
|
\le
\left\lfloor
\frac1\gamma
\right\rfloor.
}
$$

### Proof

If there are:

$$
m
$$

overlaps of at least:

$$
\gamma,
$$

then by Theorem 17.1:

$$
1
=
\sum_{a'}\mathfrak o_J(a,a')
\ge
m\gamma.
$$

$\square$

---

# 19. Soft tails do not equal infinite effective branching

The adjoint cutoffs at earlier times have noncompact tails.

But Theorem 18.1 shows:

For any fixed positive overlap threshold:

$$
\gamma>0,
$$

a tube can only have finitely many:

$$
\gamma
$$

-significant child tubes.

Therefore:

$$
\boxed{
\text{soft spatial tails}
\neq
\text{infinite effective seam branching at fixed positive share}.
}
$$

---

# 20. Why are frequency link + tube overlap still not enough?

Even if:

$$
\mathfrak f_J(v,w)=1
$$

and:

$$
\mathfrak o_J(a,a')>0,
$$

it still only means:

- the frequency labels can connect;
- the spacetime tubes geometrically connect at the seam.

It has not yet proven that:

> the new output stock genuinely generated by the previous witness pays for a portion of the child parent source in the next interval.

Thus, a third layer is needed:

$$
\boxed{
\textbf{inter-edge PDE bridge certificate}.
}
$$

---

# 21. Bridge score placeholder

This paper defines a typed quantity:

$$
\boxed{
\mathfrak b_J(v,w)
\in[0,1].
}
$$

Its semantic requirement is that:

$$
\mathfrak b_J(v,w)>0
$$

can only hold when an existing equation-level certificate proves that:

the witness-associated output contribution from the previous edge can be traced to the selected parent source of the next edge.

Currently, the universal lower bound and complete construction of:

$$
\mathfrak b_J
$$

have not yet been proven.

It is the PDE-facing obligation of the next paper.

---

# 22. Stock compatibility and provenance compatibility

Define the stock-level score:

$$
\boxed{
\mathfrak c_J^{stock}(v,w)
=
\mathfrak f_J(v,w)
\mathfrak o_J(a,a').
}
$$

Then define the full provenance score:

$$
\boxed{
\mathfrak c_J^{prov}(v,w)
=
\mathfrak c_J^{stock}(v,w)
\mathfrak b_J(v,w).
}
$$

Therefore:

$$
0\le
\mathfrak c_J^{prov}
\le
\mathfrak c_J^{stock}
\le1.
$$

---

# 23. Hard guard: Stock continuity does not equal source provenance

$$
\boxed{
G_{\rm BRIDGE}:
\quad
\mathfrak c_J^{stock}>0
\not\Rightarrow
\mathfrak c_J^{prov}>0.
}
$$

That is:

$$
\boxed{
\text{same shell}
+
\text{same spatial seam}
}
$$

still cannot substitute for a true equation-level source bridge.

---

# 24. Layered witness graph

Fix an infinite PF-A level set:

$$
J_0,
J_0+1,
J_0+2,\ldots.
$$

Define the vertices:

$$
\boxed{
V
=
\bigsqcup_{J\ge J_0}
V_J,
}
$$

where:

$$
V_J
=
\left\{
v:
\pi_J(v)>0
\right\}.
$$

If using the provenance graph,

an edge:

$$
v\to w
$$

exists if and only if:

$$
\boxed{
\mathfrak c_J^{prov}(v,w)>0.
}
$$

The thresholded graph requires fixed positive node and edge floors.

---

# 25. Thresholded ancestry graph

Fix:

$$
0<\theta\le1,
\qquad
0<\gamma\le1.
$$

Define:

$$
\boxed{
V_J^{\theta}
=
\left\{
v:
\pi_J(v)\ge\theta
\right\}.
}
$$

and:

$$
\boxed{
E_J^{\theta,\gamma}
=
\left\{
(v,w):
v\in V_J^\theta,
\quad
w\in V_{J+1}^\theta,
\quad
\mathfrak c_J^{prov}(v,w)\ge\gamma
\right\}.
}
$$

---

# 26. C5.6 — Uniform Finite Branching

## Theorem 26.1

The thresholded provenance graph:

$$
\mathcal G^{\theta,\gamma}
$$

satisfies at every level:

$$
\boxed{
|V_J^\theta|
\le
\left\lfloor
\frac1\theta
\right\rfloor.
}
$$

Therefore, the out-degree of every vertex satisfies:

$$
\boxed{
\deg^+(v)
\le
\left\lfloor
\frac1\theta
\right\rfloor.
}
$$

Thus:

$$
\boxed{
\mathcal G^{\theta,\gamma}
\text{ is uniformly finitely branching}.
}
$$

### Proof

The first equation follows from Theorem 8.1.

Every child must be located in:

$$
V_{J+1}^{\theta},
$$

so the out-degree does not exceed the number of nodes in the next level. $\square$

---

# 27. Finite-horizon ancestry path

For:

$$
N\ge0,
$$

define the horizon:

$$
[J_0,J_0+N].
$$

A:

$$
(\theta,\gamma)
$$

-qualified finite path is:

$$
\boxed{
\pi_N
=
(v_{J_0},v_{J_0+1},\ldots,v_{J_0+N})
}
$$

satisfying:

$$
v_J\in V_J^\theta,
$$

and:

$$
(v_J,v_{J+1})
\in
E_J^{\theta,\gamma}
$$

holds for all adjacent levels.

Denote the finite path set by:

$$
\boxed{
\mathscr P_N(\theta,\gamma).
}
$$

---

# 28. What does the global quantifier truly need?

We can now precisely distinguish between:

$$
\boxed{
\forall N\;
\mathscr P_N(\theta,\gamma)\neq\varnothing
}
$$

and:

$$
\boxed{
\exists
(v_J)_{J\ge J_0}
\text{ an infinite }
(\theta,\gamma)
\text{-qualified path}.
}
$$

In a general infinitely branching graph,

the former cannot be unconditionally upgraded to the latter.

But Theorem 26.1 provides exactly the required finite branching.

---

# 29. Backward survivor recursion

Fix a finite terminal horizon:

$$
N.
$$

Let the terminal survivor set be:

$$
\boxed{
S_{J_0+N}^{(N)}
=
V_{J_0+N}^{\theta}.
}
$$

Recursively define backward:

$$
\boxed{
S_J^{(N)}
=
\left\{
v\in V_J^\theta:
\exists
w\in
S_{J+1}^{(N)}
\text{ with }
(v,w)\in
E_J^{\theta,\gamma}
\right\}.
}
$$

This is called the:

$$
\boxed{
\textbf{Backward Survivor Recursion}.
}
$$

---

# 30. C5.7 — Finite-Horizon Survivor Criterion

## Theorem 30.1

We have:

$$
\boxed{
\mathscr P_N(\theta,\gamma)
\neq
\varnothing
}
$$

if and only if:

$$
\boxed{
S_{J_0}^{(N)}
\neq
\varnothing.
}
$$

### Proof

If a path exists,

its terminal node is in:

$$
S_{J_0+N}^{(N)}.
$$

Looking backward level by level,

the nodes on the path all belong to the survivor set according to the recursion.

Hence the root node is in:

$$
S_{J_0}^{(N)}.
$$

Conversely,

if:

$$
v_{J_0}\in S_{J_0}^{(N)},
$$

by the survivor definition, we can choose a:

$$
v_{J_0+1}\in S_{J_0+1}^{(N)}
$$

compatible with it.

Finitely many recursive choices up to the terminal level yield the path. $\square$

---

# 31. Survivor sets are monotonic with respect to the horizon

For fixed:

$$
J,
$$

if:

$$
N_2>N_1\ge J-J_0,
$$

then:

$$
\boxed{
S_J^{(N_2)}
\subseteq
S_J^{(N_1)}.
}
$$

Because a node that can extend to a farther horizon can certainly extend to a nearer horizon.

---

# 32. C5.8 — Infinite Path Extraction Theorem

## Theorem 32.1

Fix:

$$
\theta>0,
\qquad
\gamma>0.
$$

If:

$$
\boxed{
\forall N\ge0,
\quad
\mathscr P_N(\theta,\gamma)
\neq
\varnothing,
}
$$

then there exists an infinite:

$$
(\theta,\gamma)
$$

-qualified provenance path:

$$
\boxed{
v_{J_0}
\to
v_{J_0+1}
\to
v_{J_0+2}
\to\cdots.
}
$$

### Proof

By Theorem 26.1:

$$
V_{J_0}^{\theta}
$$

is finite.

By Theorem 30.1,

all:

$$
S_{J_0}^{(N)}
$$

are nonempty.

And Section 31 gives the nested property:

$$
S_{J_0}^{(N+1)}
\subseteq
S_{J_0}^{(N)}.
$$

Nested nonempty subsets in a finite set have a nonempty intersection:

$$
\bigcap_N
S_{J_0}^{(N)}
\neq
\varnothing.
$$

Take:

$$
v_{J_0}
$$

in this intersection.

It has an extension for any horizon.

Its acceptable children are located in the finite:

$$
V_{J_0+1}^{\theta}.
$$

At least one child must be extendable to arbitrarily large horizons;

otherwise, all children would each only have a finite extension depth,

and taking the maximum would cause:

$$
v_{J_0}
$$

to also have only a finite extension depth,

a contradiction.

Select this child as:

$$
v_{J_0+1}.
$$

Repeating the same argument,

recursively yields the infinite path. $\square$

---

# 33. This is the RFP version of the Kőnig-type infinity principle

Theorem 32.1 is a direct realization of the classical finitely-branching infinity principle on the RFP witness graph.

But this paper provides a self-contained survivor proof,

so it does not treat the graph-theory theorem as an unchecked black box.

The most important logical form is:

$$
\boxed{
\left[
\forall N\;
\exists\text{ qualified finite ancestry of depth }N
\right]
+
\text{finite branching}
}
$$

implies:

$$
\boxed{
\exists\text{ one qualified infinite ancestry}.
}
$$

This is exactly the global quantifier bridge that has been missing in the previous papers.

---

# 34. Finite stitching obstruction

If there exists:

$$
N_\ast<\infty
$$

such that:

$$
\boxed{
S_{J_0}^{(N_\ast)}
=
\varnothing,
}
$$

then:

$$
\mathscr P_{N_\ast}(\theta,\gamma)
=
\varnothing.
$$

We call:

$$
\boxed{
N_\ast
}
$$

the:

$$
\boxed{
\textbf{finite stitching obstruction horizon}.
}
$$

---

# 35. Obstruction certificate

A finite stitching obstruction certificate can be saved as:

$$
\boxed{
\mathsf{StitchCert}
=
\left\langle
J_0,
N_\ast,
\theta,
\gamma,
\{V_J^\theta\},
\{E_J^{\theta,\gamma}\},
\{S_J^{(N_\ast)}\},
\mathsf{Reasons}
\right\rangle.
}
$$

where:

$$
\mathsf{Reasons}
$$

saves for each pruned node:

- no frequency-linked child;
- insufficient tube seam overlap;
- failed PDE bridge certificate;
- child node below strength threshold;
- source/projection/localization guard failure.

Therefore:

$$
\boxed{
\text{global path failure}
}
$$

can be compressed into a:

$$
\boxed{
\text{finite backward-pruning certificate}.
}
$$

---

# 36. Minimal obstruction horizon

Define:

$$
\boxed{
H_\ast(\theta,\gamma)
=
\inf
\left\{
N:
S_{J_0}^{(N)}
=
\varnothing
\right\}.
}
$$

If the set is empty,

let:

$$
H_\ast(\theta,\gamma)=\infty.
$$

By Theorem 32.1:

$$
\boxed{
H_\ast(\theta,\gamma)=\infty
}
$$

if and only if there exists an infinite:

$$
(\theta,\gamma)
$$

-qualified path.

---

# 37. Global quantifier compiler

So after fixing:

$$
\theta,\gamma>0
$$

,

the RFP persistence problem is exactly rewritten as:

$$
\boxed{
H_\ast(\theta,\gamma)
<
\infty
}
$$

or:

$$
\boxed{
H_\ast(\theta,\gamma)
=
\infty.
}
$$

The first is a finite obstruction.

The second directly gives an infinite path.

This is the most important quantifier compilation of this paper.

---

# 38. But fixed positive thresholds might not exist

Full Chain Necessity cannot pre-assume that:

$$
\theta>0
$$

and:

$$
\gamma>0
$$

can be uniformly fixed.

It may happen that:

$$
\text{Every finite horizon has a candidate path,}
$$

but all long paths are forced to pass through:

$$
\text{weaker and weaker witnesses}
$$

or:

$$
\text{weaker and weaker compatibility}.
$$

This is the next escape:

$$
\boxed{
\textbf{persistence bottleneck collapse}.
}
$$

---

# 39. Unthresholded positive candidate paths

Let:

$$
\mathscr P_N^+
$$

be all finite sequences:

$$
(v_{J_0},\ldots,v_{J_0+N})
$$

such that:

$$
\pi_J(v_J)>0
$$

and:

$$
\mathfrak c_J^{prov}(v_J,v_{J+1})>0.
$$

If:

$$
\mathscr P_N^+=\varnothing,
$$

then the horizon:

$$
N
$$

has already encountered an absolute finite stitching obstruction.

---

# 40. Path bottleneck

For:

$$
\pi
=
(v_{J_0},\ldots,v_{J_0+N})
\in
\mathscr P_N^+,
$$

define:

$$
\boxed{
\operatorname{Bot}(\pi)
=
\min
\left\{
\min_{J_0\le J\le J_0+N}
\pi_J(v_J),
\;
\min_{J_0\le J<J_0+N}
\mathfrak c_J^{prov}(v_J,v_{J+1})
\right\}.
}
$$

Thus:

$$
0<
\operatorname{Bot}(\pi)
\le1.
$$

---

# 41. Horizon bottleneck

Define:

$$
\boxed{
\beta_N
=
\sup_{\pi\in\mathscr P_N^+}
\operatorname{Bot}(\pi).
}
$$

If:

$$
\mathscr P_N^+=\varnothing,
$$

define:

$$
\beta_N=0.
$$

---

# 42. C5.9 — Bottleneck Monotonicity

## Theorem 42.1

We have:

$$
\boxed{
\beta_{N+1}
\le
\beta_N.
}
$$

Therefore, the limit:

$$
\boxed{
\beta_\infty
=
\lim_{N\to\infty}\beta_N
}
$$

exists in:

$$
[0,1].
$$

### Proof

Truncating the last node of any length:

$$
N+1
$$

path,

yields a length:

$$
N
$$

path.

Truncation does not decrease the bottleneck.

Therefore:

$$
\sup_{\mathscr P_{N+1}}
\operatorname{Bot}
\le
\sup_{\mathscr P_N}
\operatorname{Bot}.
$$

$\square$

---

# 43. C5.10 — Persistence Trichotomy

## Theorem 43.1

It exactly falls into one of the following three categories:

### P-A — Finite stitching obstruction

There exists:

$$
N_\ast<\infty
$$

such that:

$$
\boxed{
\mathscr P_{N_\ast}^+
=
\varnothing.
}
$$

### P-B — Bottleneck collapse

For all:

$$
N,
$$

we have:

$$
\mathscr P_N^+\neq\varnothing,
$$

but:

$$
\boxed{
\beta_\infty=0.
}
$$

### P-C — Uniform persistent ancestry

$$
\boxed{
\beta_\infty>0.
}
$$

And in this case, there exists an infinite provenance path:

$$
(v_J)_{J\ge J_0}
$$

and some:

$$
\delta>0
$$

such that:

$$
\boxed{
\pi_J(v_J)\ge\delta,
}
$$

and:

$$
\boxed{
\mathfrak c_J^{prov}(v_J,v_{J+1})
\ge\delta
}
$$

for all:

$$
J\ge J_0.
$$

### Proof

If some finite path set is empty, it is P-A.

Otherwise, all:

$$
\beta_N>0.
$$

By monotonicity,

$$
\beta_\infty
$$

exists.

If it is:

$$
0,
$$

we get P-B.

If:

$$
\beta_\infty>0,
$$

choose:

$$
0<\delta<\beta_\infty.
$$

For each:

$$
N,
$$

by the definition of supremum, there exists:

$$
\operatorname{Bot}(\pi_N)>\delta.
$$

Thus:

$$
\mathscr P_N(\delta,\delta)\neq\varnothing
$$

for all $N$.

Theorem 32.1 gives an infinite:

$$
(\delta,\delta)
$$

-qualified path. $\square$

---

# 44. This is a proof-space enclosure, not a regularity theorem

Theorem 43.1 is already exhaustive for the persistence quantifier.

But:

$$
P\mbox{-}A
$$

is only a finite obstruction relative to the current:

$$
\mathfrak c^{prov}
$$

and the node class.

If the compatibility module is incomplete,

it cannot be directly claimed as:

$$
\text{dynamically impossible}.
$$

And:

$$
P\mbox{-}B
$$

might also be a true singularity ancestry:

it just lacks a uniform positive bottleneck.

So PDE estimates are still needed to exclude:

$$
P\mbox{-}B
$$

or to convert its vanishing bottleneck into a new quantitative debt.

---

# 45. Two-parameter feasibility region

For each:

$$
N,
$$

define:

$$
\boxed{
\mathcal F_N
=
\left\{
(\theta,\gamma)\in(0,1]^2:
\mathscr P_N(\theta,\gamma)\neq\varnothing
\right\}.
}
$$

It has the property:

$$
\boxed{
\mathcal F_{N+1}
\subseteq
\mathcal F_N.
}
$$

And if:

$$
(\theta,\gamma)\in\mathcal F_N,
$$

then any:

$$
0<\theta'\le\theta,
\qquad
0<\gamma'\le\gamma
$$

is also in:

$$
\mathcal F_N.
$$

Thus:

$$
\mathcal F_N
$$

is a downward-closed feasible region.

---

# 46. Persistent feasible core

Define:

$$
\boxed{
\mathcal F_\infty
=
\bigcap_{N\ge0}
\mathcal F_N.
}
$$

If there exists:

$$
(\theta,\gamma)
\in
\mathcal F_\infty
$$

with:

$$
\theta>0,
\quad
\gamma>0,
$$

then by Theorem 32.1:

$$
\boxed{
\text{an infinite persistent ancestry exists}.
}
$$

If all finite horizons are feasible,

but:

$$
\mathcal F_\infty
$$

has no positive-positive point,

it is another way of expressing:

$$
\boxed{
\text{persistence bottleneck collapses toward the threshold axes}.
}
$$

---

# 47. Typed causes of bottleneck collapse

P-B should not be treated as a single failure.

It may arise from at least:

### B-NODE

$$
\boxed{
\text{node-strength atomization}
}
$$

i.e., the strong local source share tends to zero.

### B-SEAM

$$
\boxed{
\text{tube seam overlap degeneration}
}
$$

i.e., spatial continuity can only rely on increasingly smaller overlaps.

### B-BRIDGE

$$
\boxed{
\text{PDE bridge degeneration}
}
$$

i.e.:

$$
\mathfrak b_J\to0
$$

along every long candidate path.

### B-TRADE

There is a horizon-dependent tradeoff between node strength and compatibility;

both may individually have strong candidates,

but they cannot be simultaneously maintained on the same path.

Therefore:

$$
\boxed{
\beta_\infty=0
}
$$

is a global persistence defect,

not a single local observable.

---

# 48. Spatial fan-out and bottleneck collapse

If:

$$
\mathfrak o_J(a,a')\ge\gamma,
$$

Theorem 18.1 gives that under a fixed:

$$
\gamma>0
$$

the spatial fan-out is finite.

Therefore, if persistence can only rely on:

$$
\gamma_J\to0,
$$

this is not a trivial artifact of soft tails,

but rather:

$$
\boxed{
\text{effective spatial branching scale diverges}.
}
$$

Since:

$$
|\mathcal A_{J+1}(a;\gamma_J)|
\lesssim
\gamma_J^{-1}.
$$

Thus:

$$
\boxed{
\gamma_J\to0
\Longrightarrow
\text{spatial branching debt can diverge}.
}
$$

---

# 49. Node atomization and branching debt

If:

$$
\mathfrak a_J\to0,
$$

Theorem 12.1 gives:

$$
\mathfrak M_J^{eff}\to\infty.
$$

Thus, node bottleneck collapse must be accompanied by:

$$
\boxed{
\text{local-source activity spread across more effective spacetime parent entries}.
}
$$

This is the persistence-level analogue of the RFP-03 parent multiplicity debt.

---

# 50. Strong-node branching bound

For fixed:

$$
\theta>0,
$$

we have:

$$
|V_J^\theta|
\le
\theta^{-1}.
$$

So the total number of thresholded path candidates of any length:

$$
N
$$

has a coarse bound:

$$
\boxed{
|\mathscr P_N(\theta,\gamma)|
\le
\theta^{-(N+1)}.
}
$$

This bound is not computationally optimal,

but it proves that the candidate space for each fixed horizon is finite.

---

# 51. Survivor recursion is verifiable by finite computation

For fixed:

$$
J_0,
N,\theta,\gamma,
$$

as long as:

- node ledger entries can be certified;
- compatibility predicates can be certified;
- bridge scores have verifiable lower bounds;

then:

$$
S_J^{(N)}
$$

can be computed backward from the terminal level in finitely many steps.

Therefore:

$$
\boxed{
\text{finite-horizon path existence}
}
$$

is not an existential black box.

It can output the:

$$
\boxed{
\text{survivor set}
}
$$

or a:

$$
\boxed{
\text{finite obstruction certificate}.
}
$$

---

# 52. But finite computation alone still cannot prove continuum closure

If we only verify:

$$
N\le N_{\max},
$$

we can only obtain:

$$
H_\ast(\theta,\gamma)>N_{\max}.
$$

We cannot deduce:

$$
H_\ast(\theta,\gamma)=\infty.
$$

To upgrade from all finite horizons to an infinite path,

we still need a theorem-level:

$$
\boxed{
\forall N
}
$$

statement,

or a resolution-independent analytic estimate guaranteeing that the survivor recursion never empties.

Thus:

$$
\boxed{
\text{large finite depth}
\neq
\text{infinite ancestry}.
}
$$

---

# 53. Legitimacy levels of finite obstruction

This paper distinguishes:

### O-CERT — Certificate-class obstruction

The thresholded witness graph empties at a finite horizon.

### O-DYN — Dynamical obstruction

It has been proven that any true N--S ancestry must fall into this certificate class,

so the graph emptying genuinely excludes the dynamics.

Only:

$$
O\mbox{-}DYN
$$

can enter the final Finite Obstruction theorem.

Therefore, we add:

$$
\boxed{
G_{\rm COMPLETE}:
\quad
\text{certificate-class exhaustion must be proved before finite graph failure is called dynamical impossibility}.
}
$$

---

# 54. This prevents a very dangerous false proof

The erroneous form:

$$
\text{my selected witness graph has no infinite path}
$$

therefore:

$$
\text{Navier--Stokes has no singularity}.
$$

This is completely invalid,

unless one first proves:

$$
\boxed{
\text{every singularity ancestry must be represented in the selected graph}.
}
$$

That is:

$$
\boxed{
\text{graph completeness}.
}
$$

This is the same class of theorem-safety guard as the previous:

$$
\text{balance closeness}
\neq
\text{dynamics closeness}
$$

and:

$$
\text{certificate failure}
\neq
\text{dynamical impossibility}
$$

.

---

# 55. RFP-05 Master Persistence Enclosure

## Theorem 55.1

Consider an infinite PF-A first-passage subsequence.

Given a valid RFP-04 local-source ledger and a certified provenance compatibility score:

$$
\mathfrak c_J^{prov}.
$$

then the persistence problem must fall into:

$$
\boxed{
P\mbox{-}A
\vee
P\mbox{-}B
\vee
P\mbox{-}C,
}
$$

where:

### P-A

A finite horizon exhibits a:

$$
\boxed{
\text{stitching obstruction}.
}
$$

### P-B

Arbitrarily long finite paths exist,

but:

$$
\boxed{
\beta_\infty=0
}
$$

and persistence can only occur via a vanishing node / seam / bridge bottleneck.

### P-C

There exists:

$$
\boxed{
\text{one infinite provenance path with uniform positive node and compatibility floors}.
}
$$

Furthermore:

- node-floor collapse must pay an effective multiplicity debt;
- seam-floor collapse allows the effective spatial branching scale to diverge;
- any P-A result must first pass $G_{\rm COMPLETE}$ to be upgraded to a dynamical obstruction.

$\square$

---

# 56. Relationship with the PF-B synchronous branch

RFP-03 has proven:

Any infinite first-passage sequence has a subsequence falling into:

$$
PF\mbox{-}A
$$

or:

$$
PF\mbox{-}B.
$$

This paper primarily handles the persistence quantifier of:

$$
PF\mbox{-}A
$$

.

If there are only finitely many PF-A edges,

then there must be an infinite:

$$
PF\mbox{-}B
$$

synchronous/deep-tail subsequence.

This branch still belongs to the:

$$
\boxed{
\text{Synchronous-Bypass / Carrier-Depth Escape}.
}
$$

Thus, Full Chain Necessity currently still requires:

$$
\boxed{
\text{PF-A persistence closure}
+
\text{PF-B synchronous resolution}.
}
$$

---

# 57. Relationship with the 2026 finite-window / finite-chain literature

Recent Navier–Stokes finite-window research has explicitly developed:

- finite-scale supply--tax reductions;
- finite-window local-to-clean transfer;
- recursive finite-chain audit propagation;
- finite-chain CKN-bad-scale counting.

These works are highly suitable for providing:

$$
\boxed{
\text{one-step / finite-horizon PDE certificates}.
}
$$

But finite-chain propagation itself still does not automatically equal:

$$
\boxed{
\text{one infinite persistent ancestry}.
}
$$

RFP-05 specifically unpacks this logical transition:

$$
\boxed{
\text{finite-horizon admissibility}
+
\text{positive bottleneck}
+
\text{finite branching}
\Longrightarrow
\text{infinite path}.
}
$$

---

# 58. Graph-theoretic calibration

Classical infinity lemmas provide for finitely branching trees:

> arbitrarily deep finite branches imply an infinite ray.

This paper does not directly assume the RFP witness system to be a tree.

Instead:

1. It first forms a layered directed graph;
2. It treats finite compatible paths as tree nodes;
3. It uses survivor recursion to self-prove infinite path extraction.

Therefore, graph theory here is not a PDE input,

but rather a:

$$
\boxed{
\text{quantifier-closure engine}.
}
$$

---

# 59. X-Integration Update: Persistence Compiler

Add a new X-level operator:

$$
\boxed{
\mathsf{Persist}_{\theta,\gamma}^{N}
}
$$

Input:

$$
\left(
V_{J_0}^{\theta},
\ldots,
V_{J_0+N}^{\theta},
E_{J_0}^{\theta,\gamma},
\ldots,
E_{J_0+N-1}^{\theta,\gamma}
\right),
$$

Output:

$$
\boxed{
\mathsf{SURVIVE}
}
$$

if:

$$
S_{J_0}^{(N)}\neq\varnothing,
$$

or:

$$
\boxed{
\mathsf{OBSTRUCTED}
}
$$

if:

$$
S_{J_0}^{(N)}=\varnothing.
$$

---

# 60. Persistence provenance certificate

If:

$$
\mathsf{SURVIVE},
$$

save:

$$
\boxed{
\mathsf{PersistCert}_N
=
\left\langle
\{S_J^{(N)}\},
\mathsf{ParentPointers},
\mathsf{NodeScores},
\mathsf{CompatibilityScores},
\mathsf{GuardStates}
\right\rangle.
}
$$

If:

$$
\mathsf{OBSTRUCTED},
$$

save:

$$
\boxed{
\mathsf{ObstructCert}_N
=
\left\langle
\{S_J^{(N)}\},
\mathsf{PruneReasons},
\mathsf{CompletenessStatus}
\right\rangle.
}
$$

In particular:

$$
\mathsf{CompletenessStatus}
$$

must not be omitted.

---

# 61. New guards

### $G_{\rm QUANT}$

$$
\forall J\exists v_J
$$

must not be surreptitiously replaced by:

$$
\exists(v_J)_J\forall J.
$$

### $G_{\rm FINBR}$

Finite-horizon-to-infinite extraction must have finite branching or another explicit compactness theorem.

### $G_{\rm SEAM}$

Spatial tube continuity must save a seam overlap certificate.

### $G_{\rm BRIDGE}$

Stock/tube continuity must not substitute for an equation-level provenance bridge.

### $G_{\rm SURV}$

Finite path existence uses backward survivor recursion or an equivalent exact certificate.

### $G_{\rm BOT}$

If a uniform positive bottleneck does not exist,

the bottleneck-collapse branch must be retained,

and one must not forcefully extract a strong infinite path.

### $G_{\rm COMPLETE}$

Certificate-class obstruction can only be upgraded to dynamical obstruction when class completeness is proven.

---

# 62. Guard Library v4

Therefore:

$$
\boxed{
\mathcal G_{NS}^{(4)}
=
\mathcal G_{NS}^{(3)}
\cup
\{
G_{\rm QUANT},
G_{\rm FINBR},
G_{\rm SEAM},
G_{\rm BRIDGE},
G_{\rm SURV},
G_{\rm BOT},
G_{\rm COMPLETE}
\}.
}
$$

---

# 63. Where is Chain Necessity narrowed down to now?

At RFP-01:

$$
\boxed{
\text{UV escape}
\stackrel{?}{\Longrightarrow}
\text{full formation ancestry}.
}
$$

After RFP-02:

$$
\boxed{
\text{first-passage skeleton}
+
\text{source debt}.
}
$$

After RFP-03:

$$
\boxed{
\text{exact parent ledger}.
}
$$

After RFP-04:

$$
\boxed{
\text{uniform-tightness budget}
+
\text{spacetime source-core ledger}.
}
$$

After RFP-05:

$$
\boxed{
\text{finite-horizon compatible ancestry}
+
\text{positive bottleneck}
\Longrightarrow
\text{infinite persistent path}.
}
$$

Thus, the main gap in Full Chain Necessity has been highly concentrated on:

$$
\boxed{
\textbf{inter-edge PDE bridge lower bounds}
}
$$

and:

$$
\boxed{
\textbf{bottleneck-collapse exclusion / debt}.
}
$$

Additionally, it still retains the:

$$
PF\mbox{-}B
$$

synchronous bypass branch.

---

# 64. The true PDE frontier of the next paper

Therefore, the next paper should not go back to expand more graph notation first.

The formal frontier is:

$$
\boxed{
\textbf{NS-RFP 06 — Inter-Edge Bridge Realization, Source-Stock Propagation, and Persistence Bottleneck Lower Bounds}.
}
$$

Core issues:

1. Decompose the actual nonlinear output increment of the previous edge onto the shared seam;
2. Prove how its heat/nonlinear continuation enters the parent source of the next edge;
3. Establish the equation-level formula for:
   $$
   \mathfrak b_J(v,w)
   $$
   ;
4. Find sufficient conditions such that:
   $$
   \mathfrak b_J(v,w)\ge\gamma_0>0;
   $$
5. If there is no uniform lower bound,
   convert:
   $$
   \mathfrak b_J\to0
   $$
   into a source dilution / cancellation / transport escape debt;
6. Interface the tube seam overlap with the actual field stock rather than pure geometry;
7. Determine whether the bottleneck-collapse P-B can be excluded or rigidified by the exact N--S structure.

---

# 65. Formal status ledger

$$
\boxed{
\begin{aligned}
\text{exact local-source refinement}
&:\ \mathrm{PROVED},\\
\text{positive local-source probability ledger}
&:\ \mathrm{DEFINED},\\
\text{fixed-threshold finite level bound}
&:\ \mathrm{PROVED},\\
\text{atomization implies effective multiplicity divergence}
&:\ \mathrm{PROVED},\\
\text{time seam identity}
&:\ \mathrm{PROVED\ from\ first\mbox{-}passage\ construction},\\
\text{adjoint seam partition identity}
&:\ \mathrm{PROVED},\\
\text{effective spatial fan-out bound}
&:\ \mathrm{PROVED},\\
\text{stock compatibility score}
&:\ \mathrm{DEFINED},\\
\text{universal PDE bridge score}
&:\ \mathrm{OPEN},\\
\text{thresholded graph finite branching}
&:\ \mathrm{PROVED},\\
\text{backward survivor recursion}
&:\ \mathrm{DEFINED},\\
\text{finite-horizon survivor criterion}
&:\ \mathrm{PROVED},\\
\text{finite-horizon to infinite path extraction}
&:\ \mathrm{PROVED},\\
\text{finite stitching obstruction certificate}
&:\ \mathrm{PROVED\ relative\ to\ certified\ graph},\\
\text{persistence bottleneck monotonicity}
&:\ \mathrm{PROVED},\\
\text{persistence trichotomy}
&:\ \mathrm{PROVED},\\
\text{graph completeness for all N--S ancestries}
&:\ \mathrm{OPEN},\\
\text{uniform positive provenance bottleneck}
&:\ \mathrm{OPEN},\\
\text{PF-B synchronous resolution}
&:\ \mathrm{OPEN},\\
\text{full Chain Necessity}
&:\ \mathrm{OPEN},\\
\text{Finite Obstruction}
&:\ \mathrm{OPEN},\\
\text{Navier--Stokes regularity}
&:\ \mathrm{NOT\ PROVED}.
\end{aligned}
}
$$

---

# 66. Conclusion

RFP-05 does not solve a new local PDE estimate.

It solves what has been accumulating over the first four papers:

$$
\boxed{
\textbf{global quantifier conversion problem}.
}
$$

For fixed positive node and compatibility thresholds:

$$
\theta,\gamma>0,
$$

the strong witness levels are automatically finite:

$$
|V_J^\theta|
\le
\theta^{-1}.
$$

Therefore:

$$
\boxed{
\forall N
\;\exists
\text{ qualified finite ancestry of depth }N
}
$$

can be rigorously upgraded to:

$$
\boxed{
\exists
\text{ one infinite qualified ancestry}.
}
$$

And if the finite-horizon extension fails,

the backward survivor recursion will empty at some finite:

$$
N_\ast
$$

,

leaving a:

$$
\boxed{
\text{finite stitching obstruction certificate}.
}
$$

If arbitrarily long finite paths all exist,

but no uniform threshold can be maintained,

then the problem is forced into a:

$$
\boxed{
\text{persistence bottleneck collapse}.
}
$$

Thus, the persistence space has been compressed into:

$$
\boxed{
\text{finite obstruction}
\vee
\text{bottleneck collapse}
\vee
\text{infinite persistent path}.
}
$$

This is a truly exhaustive proof-space enclosure.

But the full Navier–Stokes conclusion still requires proving that:

$$
\boxed{
\mathfrak b_J
}
$$

is not an arbitrary abstract compatibility score,

but can obtain a sufficient quantitative lower bound from exact N--S Duhamel / source-stock propagation.

Therefore, the next round formally enters:

$$
\boxed{
\textbf{NS-RFP 06 — Inter-Edge Bridge Realization, Source-Stock Propagation, and Persistence Bottleneck Lower Bounds}.
}
$$

---

# References

1. R. Diestel, *Graph Theory*, Springer. Classical infinity principles for finitely branching trees are used only as graph-theoretic calibration; the RFP path-extraction theorem is proved self-contained above.
2. T. Barker, H. Popkin, *Quantitative estimates for the forced Navier–Stokes equations and applications*, arXiv:2602.09951 (2026).
3. R. Yu, *Critical Ledgers and Scale-Defect Cascades for Navier–Stokes*, arXiv:2606.13887 (2026).
4. R. Yu, *Finite-Window Singularity Audits and Local-to-Clean Defect Transfer for Navier–Stokes*, arXiv:2606.15086 (2026).
5. R. Yu, *Finite-Window Recursive Audit Chains for Navier–Stokes Generated Packages*, arXiv:2606.20899 (2026).
6. R. Yu, *Finite-Chain CKN-Bad Scale Counting for Navier–Stokes: Standard PDE Closure and Canonical Detector Realization*, arXiv:2606.21783 (2026).

# Internal dependencies

- `NS_RFP_01_SingularityFormationAncestry_FiniteObstruction_v0.1.md`
- `NS_RFP_02_CriticalUV_FirstPassage_SourceDebt_v0.1.md`
- `NS_RFP_03_DualWitness_ParentLedger_CarrierEscape_v0.1.md`
- `NS_RFP_04_SpatialTube_PressureCompatible_UniformParentTightness_v0.1.md`
- `NS_C3O_AdjointCore_BalanceDynamicsSeparation_v0.2.md`
- `NS_ETN_XIntegration_Multiscale_NonCollapse_v0.1.md`
- `True ETN / Infinite-Dimensional Tension Field`
- `X_Integral_Unified_Program_v0.2.md`

# Next

$$
\boxed{
\textbf{NS-RFP 06 — Inter-Edge Bridge Realization, Source-Stock Propagation, and Persistence Bottleneck Lower Bounds}
}
$$