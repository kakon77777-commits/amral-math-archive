# NTLA-O V: Path Identity, Fundamental Groupoids, Coverings, Monodromy, and Holonomy
## From Different Paths with Same Endpoints to History-Sensitive Observer Transport

**English Title:** *NTLA-O V: Path Identity, Fundamental Groupoids, Coverings, Monodromy, and Holonomy — Toward History-Sensitive Observer Transport*  
**Series:** NTLA-O Series, Paper 6  
**Version:** v0.1 Formal Draft  
**Prerequisite Paper:** *NTLA-O IV: Local-Global Observation, Presheaves, Sheaves, Stalks, and Descent*  
**Author:** Neo.K  
**Theoretical Collation and Formalization Collaboration:** Aletheia / GPT-5.6 Sol  
**Date:** 2026-08-17

---

## Abstract

The previous four NTLA-O papers have established:

$$
\text{Set}
\rightarrow
\text{Distinction Family}
\rightarrow
\text{Observer Topology}
\rightarrow
\text{Local Sections}
\rightarrow
\text{Gluing}.
$$

However, even if local data are completely compatible and can be glued, another class of information remains unaddressed:

> **How is an observer state transported from one position to another?**

And:

> **If the starting and ending points are the same, but the paths taken are different, should the final observation state still be considered the same?**

This is precisely the most natural algebraic topology interface for the original NTLA concept: "It is not just about how many holes there are, but how they are connected."

This paper first distinguishes various path identities:

$$
\boxed{
\text{Raw Path}
}
$$

$$
\rightarrow
$$

$$
\boxed{
\text{Reparameterization Class}
}
$$

$$
\rightarrow
$$

$$
\boxed{
\text{Thin-Homotopy Class}
}
$$

$$
\rightarrow
$$

$$
\boxed{
\text{Endpoint-Fixed Homotopy Class}
}
$$

$$
\rightarrow
$$

$$
\boxed{
\text{Homological Information}.
}
$$

Different quotient levels preserve varying degrees of generative history.

For a general topological space $X$, this paper utilizes the fundamental groupoid:

$$
\Pi_1(X),
$$

whose objects are points, and whose morphisms are endpoint-fixed homotopy classes. The fundamental group and covering-space lifting are core structures in standard algebraic topology.

For a covering:

$$
p:\widetilde X\rightarrow X,
$$

path lifting generates fiber transport:

$$
T_{[\gamma]}:
p^{-1}(x)
\rightarrow
p^{-1}(y),
$$

and forms:

$$
\boxed{
T:\Pi_1(X)\rightarrow\mathbf{Set}.
}
$$

For loops, this yields a monodromy action. This provides a completely standard mathematical example:

$$
\boxed{
\text{same base endpoint}
\not\Rightarrow
\text{same lifted state}.
}
$$

This paper then strictly separates covering monodromy from connection holonomy. The parallel transport of a general smooth connection is more naturally described by the thin path groupoid; Schreiber and Waldorf formulated the parallel transport of a bundle connection as a functor from the path groupoid to the fiber category.

Therefore, "path difference" itself also possesses a resolution hierarchy.

The fundamental groupoid has already quotiented out endpoint-fixed homotopic paths; if the NTLA identity specification requires preserving a finer actual history, then:

$$
\Pi_1(X)
$$

is still too coarse.

Conversely, if one only takes:

$$
H_1(X),
$$

then the first homology will further lose the noncommutative order information present in the fundamental group.

Thus, this paper proposes:

$$
\boxed{
\operatorname{PathRes}(\mathcal O)
}
$$

as the path identity resolution of the observer, and formally establishes the:

$$
\boxed{
\text{Observer Position}
\times
\text{Local State}
\times
\text{Path Transport}
}
$$

three-axis structure.

**Keywords:** NTLA-O, path identity, fundamental groupoid, covering space, path lifting, monodromy, holonomy, thin homotopy, parallel transport, observer history

---

# 1. Why is a Sheaf Not Enough?

Paper 5 established:

$$
s_i\in\mathscr F(U_i)
$$

and investigated:

$$
s_i|_{U_i\cap U_j}
=
s_j|_{U_i\cap U_j}.
$$

This answers the question:

> Are observation states in different local domains compatible?

But it does not fully answer:

> When a state moves from $x$ to $y$, along which path does it arrive?

Suppose:

$$
x,y\in X
$$

and there exist two paths:

$$
\gamma_1,\gamma_2:
x\rightarrow y.
$$

Even if:

$$
\gamma_1(0)=\gamma_2(0)=x,
$$

and:

$$
\gamma_1(1)=\gamma_2(1)=y,
$$

it is still possible that:

$$
\boxed{
\gamma_1\neq\gamma_2.
}
$$

Therefore:

$$
\boxed{
\text{endpoint data}
}
$$

does not contain the complete:

$$
\boxed{
\text{path data}.
}
$$

---

# 2. Raw Path

Let:

$$
X
$$

be a topological space.

A path from $x$ to $y$ is a continuous map:

$$
\boxed{
\gamma:[0,1]\rightarrow X
}
$$

satisfying:

$$
\gamma(0)=x,
$$

$$
\gamma(1)=y.
$$

All such paths are denoted by:

$$
\boxed{
P(x,y).
}
$$

The finest identity can directly use the function identity:

$$
\boxed{
\gamma_1
\equiv_{\mathrm{raw}}
\gamma_2
\iff
\gamma_1=\gamma_2
}
$$

as map equality.

---

# 3. Raw Path is Usually Too Fine

If only the walking speed is changed, for example, there exists a strictly increasing valid reparameterization:

$$
\phi:[0,1]\rightarrow[0,1]
$$

such that:

$$
\gamma_2
=
\gamma_1\circ\phi,
$$

the geometric trajectory has not truly changed.

Certain studies may choose to treat them as identical.

Thus, we define:

$$
\boxed{
\equiv_{\mathrm{rep}}
}
$$

as an appropriate reparameterization equivalence.

Then:

$$
\boxed{
\equiv_{\mathrm{raw}}
\subseteq
\equiv_{\mathrm{rep}}.
}
$$

In other words, the reparameterization quotient has already discarded some time-parameter information.

---

# 4. The Re-emergence of Identity Specifications

NTLA-O does not presuppose which level is the true identity.

Instead, it requires specifying:

$$
\boxed{
\mathfrak I_{\mathrm{path}}.
}
$$

For instance, a certain problem might consider:

$$
\gamma
$$

and:

$$
\gamma\circ\phi
$$

to be the same.

Another problem might consider the speed history itself to be important, thus treating them as different.

Therefore:

$$
\boxed{
\text{path equality}
}
$$

is itself representation-relative.

---

# 5. Endpoint-Fixed Homotopy

For:

$$
\gamma_0,\gamma_1:x\rightarrow y,
$$

if there exists:

$$
H:[0,1]\times[0,1]\rightarrow X
$$

such that:

$$
H(s,0)=\gamma_0(s),
$$

$$
H(s,1)=\gamma_1(s),
$$

and:

$$
H(0,t)=x,
$$

$$
H(1,t)=y,
$$

then the two paths are said to be endpoint-fixed homotopic:

$$
\boxed{
\gamma_0
\simeq_{\partial}
\gamma_1.
}
$$

This relation identifies paths that can be continuously deformed into one another while keeping their endpoints fixed.

---

# 6. Fundamental Groupoid

For a topological space $X$, define:

$$
\boxed{
\Pi_1(X).
}
$$

Its:

### Objects

$$
\operatorname{Ob}\Pi_1(X)=X.
$$

### Morphisms

$$
\operatorname{Hom}_{\Pi_1(X)}(x,y)
=
P(x,y)/{\simeq_\partial}.
$$

That is:

$$
\boxed{
[\gamma]:
x\rightarrow y.
}
$$

Composition is given by path concatenation.

The inverse is given by the reversed path:

$$
\bar\gamma(t)=\gamma(1-t)
$$

.

The fundamental group and covering spaces are among the most basic path structures in traditional algebraic topology.

---

# 7. The Fundamental Group is a Single-Point Endomorphism

Fix:

$$
x\in X.
$$

Then:

$$
\boxed{
\pi_1(X,x)
=
\operatorname{Aut}_{\Pi_1(X)}(x).
}
$$

That is, the loop homotopy classes of:

$$
x\rightarrow x
$$

.

Therefore:

$$
\boxed{
\Pi_1(X)
}
$$

is more suitable than a single:

$$
\pi_1(X,x)
$$

for the multi-position observer in NTLA-O.

Because the observer can be distributed across multiple:

$$
x,y,z,\ldots
$$

without forcing all paths to first return to the same basepoint.

---

# 8. Observer Path Resolution

Define a set of path equivalence relations:

$$
R
$$

acting on:

$$
P(x,y).
$$

For an observer $\mathcal O$, let:

$$
R_{\mathcal O}^{\mathrm{path}}
$$

denote which paths it determines to be identical.

If:

$$
R_A
\subseteq
R_B,
$$

then:

$$
A
$$

preserves path distinctions at least as fine as $B$.

Thus, define:

$$
\boxed{
A
\preceq_{\mathrm{path}}
B
}
$$

if and only if:

$$
R_B
\subseteq
R_A,
$$

following the previous convention where "the finer observer is on the right."

---

# 9. Path Quotient Monotonicity

If:

$$
R_1\subseteq R_2,
$$

then there exists a natural surjection:

$$
\boxed{
P/R_1
\rightarrow
P/R_2.
}
$$

Therefore, every addition of a valid path-identification rule further loses historical information.

---

# Theorem 1: Path Quotient Information Monotonicity

If:

$$
R_1\subseteq R_2,
$$

then:

$$
\boxed{
|\,[\gamma]_{R_1}\text{ distinctions}\,|
\geq
|\,[\gamma]_{R_2}\text{ distinctions}\,|
}
$$

In the finite case, this is an ordinary cardinality comparison; in the general case, it is understood as the existence of the aforementioned natural quotient map.

Therefore:

$$
\boxed{
\text{coarser path identity}
\Rightarrow
\text{no more historical distinction}.
}
$$

---

# 10. The Fundamental Groupoid is Already a Form of History Compression

Since:

$$
\gamma_1\simeq_\partial\gamma_2
$$

implies:

$$
[\gamma_1]
=
[\gamma_2]
$$

holds in:

$$
\Pi_1(X)
$$

.

Therefore:

$$
\boxed{
\Pi_1(X)
}
$$

does not preserve raw path history.

It only preserves:

$$
\boxed{
\text{path identity modulo endpoint-fixed homotopy}.
}
$$

Thus, if the NTLA identity specification requires:

> Different actual trajectories traversed must be considered different,

then:

$$
\boxed{
\Pi_1(X)
\text{ is too coarse.}
}
$$

---

# 11. Covering Space

Let:

$$
\boxed{
p:\widetilde X\rightarrow X
}
$$

be a covering map.

For:

$$
x\in X,
$$

define the fiber:

$$
\boxed{
F_x
=
p^{-1}(x).
}
$$

One of the key properties of covering spaces is path lifting: given a base path and a starting point in the fiber, there exists a unique lifted path. Hatcher's chapter on covering spaces uses lifting properties as the core structure.

---

# 12. Path Lifting

Let:

$$
\gamma:[0,1]\rightarrow X
$$

and:

$$
\gamma(0)=x.
$$

Take:

$$
\tilde x\in F_x.
$$

Then there exists a unique:

$$
\tilde\gamma:[0,1]\rightarrow\widetilde X
$$

such that:

$$
p\circ\tilde\gamma=\gamma,
$$

and:

$$
\tilde\gamma(0)=\tilde x.
$$

Therefore, we can define:

$$
\boxed{
T_\gamma(\tilde x)
=
\tilde\gamma(1).
}
$$

If:

$$
\gamma:x\rightarrow y,
$$

then:

$$
\boxed{
T_\gamma:
F_x\rightarrow F_y.
}
$$

---

# 13. Lift Transport is a Bijection

The reversed path:

$$
\bar\gamma:y\rightarrow x
$$

provides the inverse transport.

Therefore:

$$
\boxed{
T_{\bar\gamma}
=
T_\gamma^{-1}.
}
$$

Thus:

$$
T_\gamma
$$

is a bijection.

---

# 14. Homotopy Invariance of Covering Transport

If:

$$
\gamma_0
\simeq_\partial
\gamma_1,
$$

then covering homotopy lifting guarantees that two lifted paths with the same starting lift will have the same endpoint. This is a standard result in covering-space lifting theory.

Therefore:

$$
\boxed{
T_{\gamma_0}
=
T_{\gamma_1}.
}
$$

Thus, the transport only depends on:

$$
[\gamma]\in\Pi_1(X).
$$

---

# 15. Covering Transport Functor

Therefore, we can define:

$$
\boxed{
T_p:
\Pi_1(X)
\rightarrow
\mathbf{Set}
}
$$

such that:

$$
x
\mapsto
F_x
$$

and:

$$
[\gamma]
\mapsto
T_{[\gamma]}.
$$

Concatenation satisfies:

$$
\boxed{
T_{[\delta]\circ[\gamma]}
=
T_{[\delta]}
\circ
T_{[\gamma]}.
}
$$

The identity path corresponds to the identity function.

Therefore, a covering is not just "many layers."

It is a:

$$
\boxed{
\text{path-dependent observer-state transport system}.
}
$$

---

# 16. Monodromy

If:

$$
\gamma:x\rightarrow x
$$

is a loop,

then:

$$
T_{[\gamma]}:
F_x\rightarrow F_x
$$

is a permutation.

Thus, we obtain:

$$
\boxed{
\rho_p:
\pi_1(X,x)
\rightarrow
\operatorname{Sym}(F_x).
}
$$

called the covering monodromy action/representation (depending on convention, it can be expressed as a left or right action).

Its significant implication is:

$$
\boxed{
\text{the base endpoint of the loop remains unchanged,
but the fiber state can change.}
}
$$

---

# 17. The Double Cover of the Circle

Consider:

$$
p:S^1\rightarrow S^1
$$

defined by:

$$
\boxed{
p(z)=z^2.
}
$$

At:

$$
x=1
$$

:

$$
F_1
=
\{1,-1\}.
$$

Consider the base loop:

$$
\gamma(t)
=
e^{2\pi it}.
$$

It starts from:

$$
1
$$

, goes around the circle once, and returns to:

$$
1.
$$

The lift starting at:

$$
\tilde\gamma(0)=1
$$

is:

$$
\boxed{
\tilde\gamma(t)=e^{\pi it}.
}
$$

Therefore:

$$
\tilde\gamma(1)=-1.
$$

That is:

$$
\boxed{
T_\gamma(1)=-1.
}
$$

---

# 18. Same Endpoint ≠ Same Lifted State

In the base space:

$$
\gamma(0)=\gamma(1)=1.
$$

But in the covering space:

$$
\tilde\gamma(0)=1,
$$

$$
\tilde\gamma(1)=-1.
$$

Therefore:

$$
\boxed{
\text{same base endpoint}
\not\Rightarrow
\text{same transported lifted state}.
}
$$

This is a very standard mathematical model for the original NTLA concept: "identical resulting positions do not imply identical connection histories."

---

# Theorem 2: Nontrivial Monodromy Implies Endpoint Insufficiency

If there exists:

$$
[\gamma]\in\pi_1(X,x)
$$

and:

$$
\tilde x\in F_x
$$

such that:

$$
T_{[\gamma]}(\tilde x)\neq\tilde x,
$$

then the base endpoint:

$$
x
$$

is insufficient to uniquely determine the lifted final state.

### Proof

The constant path:

$$
c_x
$$

satisfies:

$$
T_{[c_x]}(\tilde x)=\tilde x.
$$

While the loop:

$$
\gamma
$$

satisfies:

$$
T_{[\gamma]}(\tilde x)\neq\tilde x.
$$

Both paths have the same starting and ending points:

$$
x\rightarrow x,
$$

but yield different outputs.

Thus, the endpoint data is incomplete.

Q.E.D.

---

# 19. Base Observer and Lifted Observer

Consider:

$$
p:\widetilde X\rightarrow X.
$$

If the base-level observer can only read:

$$
p(\tilde x),
$$

then:

$$
\tilde x_1,\tilde x_2
$$

as long as:

$$
p(\tilde x_1)=p(\tilde x_2)
$$

they are quotiented as identical.

Therefore:

$$
\boxed{
K_B
=
\{
(\tilde x_1,\tilde x_2):
p(\tilde x_1)=p(\tilde x_2)
\}.
}
$$

If the lifted observer can directly read:

$$
\tilde x
$$

itself,

then:

$$
\boxed{
K_L
=
\Delta_{\widetilde X}.
}
$$

If there exists a nontrivial fiber:

$$
|F_x|>1,
$$

then:

$$
\boxed{
K_L\subsetneq K_B.
}
$$

---

# Theorem 3: Covering Observer Refinement

If the covering has a fiber:

$$
|p^{-1}(x)|>1,
$$

then the identity-level lifted observer possesses a strictly finer point-level distinguishing capability than the base observer that only reads the projection:

$$
\boxed{
K_L\subsetneq K_B.
}
$$

Q.E.D.

Note:

This does not automatically mean:

$$
L=I
$$

or:

$$
B=M.
$$

The M/I/E roles must still be judged relative to another specified reference domain.

Thus, this example illustrates once again:

$$
\boxed{
\text{geometric level}
\neq
\text{observer role}
\neq
\text{observer resolution}.
}
$$

---

# 20. Monodromy and Observer Memory

Consider:

$$
\tilde x
\xrightarrow{\gamma}
T_\gamma(\tilde x).
$$

If:

$$
T_\gamma
$$

depends on the loop class,

then the final state can retain partial path-history information.

Therefore, we can define:

$$
\boxed{
\operatorname{Mem}_{p}([\gamma],\tilde x)
=
T_{[\gamma]}(\tilde x).
}
$$

This is not psychological memory.

Rather:

$$
\boxed{
\text{transport state retains information about path class}.
}
$$

---

# 21. Monodromy Does Not Preserve Raw Paths

Since:

$$
\gamma_1\simeq_\partial\gamma_2
$$

yields:

$$
T_{\gamma_1}=T_{\gamma_2}.
$$

Therefore, covering monodromy preserves at most a representation of:

$$
\boxed{
\text{homotopy-class information}
}
$$

.

Even for different:

$$
[\gamma_1]\neq[\gamma_2]
$$

it is still possible to have:

$$
T_{\gamma_1}=T_{\gamma_2}.
$$

if the representation:

$$
\rho_p
$$

has a nontrivial kernel.

Therefore:

$$
\boxed{
\text{monodromy output}
}
$$

is generally coarser than:

$$
\boxed{
\pi_1
}
$$

.

---

# 22. Monodromy Kernel

Define:

$$
\boxed{
K_{\mathrm{mon}}
=
\ker\rho_p
}
$$

That is, the loop classes:

$$
[\gamma]
$$

that act as the identity on the fiber.

Therefore:

$$
\boxed{
\pi_1(X,x)/K_{\mathrm{mon}}
}
$$

is the loop-action structure that this covering can truly distinguish.

Thus:

$$
\boxed{
\text{topological path difference exists}
}
$$

does not imply:

$$
\boxed{
\text{this covering observes it}.
}
$$

This is completely consistent with the observer-relative principle of the entire NTLA-O.

---

# 23. The Fundamental Group May Still Be Too Fine or Too Coarse

If the observer only reads:

$$
\rho_p([\gamma]),
$$

then:

$$
\pi_1
$$

classes that fall into the same monodromy permutation are quotiented out.

Therefore:

$$
\boxed{
\text{fundamental-group distinction}
}
$$

and:

$$
\boxed{
\text{observer-effective distinction}
}
$$

are still different.

Conversely, if the study requires preserving raw path geometry,

then:

$$
\pi_1
$$

itself is too coarse.

---

# 24. First Homology Further Quotients Out Noncommutative Information

For a path-connected space $X$, the classical one-dimensional Hurewicz theorem gives:

$$
\boxed{
H_1(X;\mathbb Z)
\cong
\pi_1(X,x)_{\mathrm{ab}},
}
$$

meaning the first homology group is the abelianization of the fundamental group. This is a standard algebraic topology result.

Therefore, the commutator:

$$
aba^{-1}b^{-1}
$$

in:

$$
H_1
$$

becomes zero.

This implies that:

$$
ab
$$

and:

$$
ba
$$

no longer retain their complete order distinction in the abelianized information.

---

# 25. The Algebraic Topology Version of NTLA Connection Order

If the original NTLA identity requires:

$$
\boxed{
a\rightarrow b
\neq
b\rightarrow a,
}
$$

then only preserving:

$$
H_1
$$

might be an excessive coarsening.

Because:

$$
H_1
$$

is naturally abelianized.

Therefore:

$$
\boxed{
\text{homology equality}
}
$$

cannot imply:

$$
\boxed{
\text{path-order identity}.
}
$$

This directly supports the revision in NTLA 2.0 that "a coarse topological summary is not the complete identity."

---

# 26. Loop Identity Resolution Tower

For loops, one can establish:

$$
\boxed{
\text{Raw Loops}
}
$$

$$
\Downarrow
$$

$$
\boxed{
\text{Reparameterization Classes}
}
$$

$$
\Downarrow
$$

$$
\boxed{
\text{Thin-Homotopy Classes}
}
$$

$$
\Downarrow
$$

$$
\boxed{
\pi_1(X,x)
}
$$

$$
\Downarrow
$$

$$
\boxed{
H_1(X;\mathbb Z)
}
$$

$$
\Downarrow
$$

$$
\boxed{
\text{Selected Numerical Invariants}.
}
$$

With each step down, distinctions may be further quotiented out.

Therefore:

$$
\boxed{
\text{same lower-level invariant}
}
$$

generally cannot reverse-imply:

$$
\boxed{
\text{same higher-resolution path identity}.
}
$$

---

# 27. Thin Homotopy

Upon entering differential geometry, a finer path quotient than ordinary homotopy is required.

Roughly speaking, smooth paths:

$$
\gamma_0,
\gamma_1
$$

if they can be connected by a homotopy that does not sweep out a true two-dimensional area, are called thin-homotopic.

The technical definition is usually given in the form of a restriction on the homotopy differential rank. Thin homotopy is a standard tool for studying connection holonomy and higher gauge transport; Caetano–Picken and subsequent higher-gauge literature utilize this structure.

Denote:

$$
\boxed{
\gamma_0
\simeq_{\mathrm{thin}}
\gamma_1.
}
$$

We have:

$$
\boxed{
\simeq_{\mathrm{thin}}
\subseteq
\simeq_{\partial}.
}
$$

Because thin homotopy is specifically a type of homotopy.

Thus, the thin quotient preserves more path geometry than the ordinary fundamental-groupoid quotient.

---

# 28. Thin Path Groupoid

For a smooth manifold $M$, one can construct the thin path groupoid:

$$
\boxed{
\Pi_1^{\mathrm{thin}}(M).
}
$$

Its morphisms are the thin-homotopy classes of appropriate smooth paths.

The parallel-transport framework of Schreiber–Waldorf precisely connects the transport of a connection with a path-groupoid functor.

Therefore:

$$
\boxed{
\Pi_1^{\mathrm{thin}}(M)
}
$$

usually preserves finer path information than:

$$
\boxed{
\Pi_1(M)
}
$$

.

---

# 29. Connection and Parallel Transport

Let:

$$
\pi:E\rightarrow M
$$

be an appropriate smooth bundle, equipped with a connection:

$$
\nabla.
$$

For a path:

$$
\gamma:x\rightarrow y,
$$

parallel transport gives a fiber map:

$$
\boxed{
P_\gamma:
E_x
\rightarrow
E_y.
}
$$

Schreiber and Waldorf proved and systematized that: the parallel transport of a bundle connection can be described by a functor on the path groupoid, and can be characterized via local trivializations and smooth descent data.

---

# 30. Covering Monodromy and Connection Holonomy Cannot Be Conflated

The two are formally similar:

$$
\text{path}
\rightarrow
\text{fiber transformation}.
$$

But their mathematical structures are different.

### Covering monodromy

Primarily depends on:

$$
[\gamma]\in\Pi_1(X)
$$

i.e., the ordinary endpoint-fixed homotopy class.

### General connection transport

Naturally preserves down to:

$$
[\gamma]_{\mathrm{thin}}
$$

the finer path information of.

Therefore:

$$
\boxed{
\text{monodromy}
\neq
\text{general connection holonomy}.
}
$$

Even though both can be understood as transport.

---

# 31. Holonomy

Fix:

$$
x\in M.
$$

For a loop:

$$
\gamma:x\rightarrow x,
$$

parallel transport:

$$
P_\gamma:
E_x
\rightarrow
E_x
$$

is called the holonomy transformation along that loop.

Under an appropriate trivialization of a principal $G$-bundle, this can correspond to:

$$
\boxed{
\operatorname{Hol}(\gamma)\in G.
}
$$

The thin-homotopy formulation of holonomy is a mature approach in differential geometry and gauge theory.

---

# 32. Holonomy Exactly Describes "Returning to the Origin but with a Changed State"

The base path:

$$
\gamma(0)=\gamma(1)=x.
$$

However:

$$
\boxed{
P_\gamma(v)
\neq v
}
$$

may hold.

Thus, we again obtain:

$$
\boxed{
\text{same geometric basepoint}
\not\Rightarrow
\text{same transported internal state}.
}
$$

Similar to covering monodromy, but this time the difference may contain connection/curvature information, rather than a simple covering sheet permutation.

---

# 33. Holonomy-Sensitive Observer

Define an observer:

$$
\mathcal O_{\mathrm{hol}}
$$

that can read:

$$
P_\gamma.
$$

Then two loops:

$$
\gamma_1,\gamma_2
$$

can be defined as:

$$
\boxed{
\gamma_1
\sim_{\mathrm{hol},\mathcal O}
\gamma_2
}
$$

if:

$$
P_{\gamma_1}
=
P_{\gamma_2}.
$$

Thus, we obtain:

$$
\boxed{
K_{\mathrm{hol},\mathcal O}.
}
$$

This is yet another observer-specific quotient.

---

# 34. Holonomy is Not Raw History Either

Even if:

$$
\gamma_1\neq\gamma_2
$$

it is possible that:

$$
P_{\gamma_1}
=
P_{\gamma_2}.
$$

Therefore:

$$
\boxed{
\text{Holonomy identity}
}
$$

does not equal:

$$
\boxed{
\text{Raw path identity}.
}
$$

Conversely:

$$
\gamma_1\simeq_{\mathrm{thin}}\gamma_2
$$

appropriate connection transport cannot utilize these two thin-equivalent paths to generate a new distinction.

Therefore:

$$
\boxed{
\text{the transport formalism itself also has a path-resolution ceiling}.
}
$$

---

# 35. NTLA-O Path Resolution

Therefore, formally define:

$$
\boxed{
\operatorname{PathRes}(\mathcal O)
}
$$

as the path identity resolution preserved by the observer.

This paper does not require it to necessarily be a single integer.

More generally, let:

$$
\operatorname{PathRes}(\mathcal O)
$$

specify a path equivalence relation:

$$
R_{\mathcal O}^{\mathrm{path}}.
$$

For two observers:

$$
A,B
$$

If:

$$
R_A
\subsetneq
R_B,
$$

then:

$$
A
$$

preserves finer path history distinctions than $B$.

---

# 36. The Endpoint Observer is the Coarsest Kind

Define:

$$
E_{\mathrm{end}}(\gamma)
=
(\gamma(0),\gamma(1)).
$$

Then:

$$
\gamma_1
\sim_{\mathrm{end}}
\gamma_2
$$

only requires:

$$
\gamma_1(0)=\gamma_2(0)
$$

and:

$$
\gamma_1(1)=\gamma_2(1).
$$

This is a very coarse path observer.

---

# 37. Homotopy Observer

Define:

$$
E_{\pi_1}(\gamma)
=
[\gamma]_{\simeq_\partial}.
$$

Then:

$$
K_{\pi_1}
$$

is finer than the endpoint kernel.

Because different homotopy classes can have the same endpoints.

Therefore:

$$
\boxed{
K_{\pi_1}
\subseteq
K_{\mathrm{end}}.
}
$$

If there exist paths with the same endpoints but different homotopy classes, then it is a strict inclusion.

---

# 38. Raw Observer

If:

$$
E_{\mathrm{raw}}(\gamma)=\gamma,
$$

then:

$$
K_{\mathrm{raw}}
=
\Delta_P.
$$

Therefore:

$$
\boxed{
K_{\mathrm{raw}}
\subseteq
K_{\mathrm{thin}}
\subseteq
K_{\pi_1}
\subseteq
K_{\mathrm{end}}
}
$$

holds under the corresponding path class and regularity conditions.

This is the:

# **Path Observer Kernel Tower**

---

# 39. At Which Level Does the Distinction First Disappear?

Previously, NTLA defined:

$$
r(x,y)
$$

as the resolution level where the distinction is first seen.

Now, for paths, another quantity can be defined:

$$
\boxed{
q(\gamma_1,\gamma_2)
}
$$

representing:

> At which quotient level are the two paths first identified as identical?

For example:

If:

$$
\gamma_1\neq_{\mathrm{raw}}\gamma_2
$$

but:

$$
\gamma_1
\equiv_{\mathrm{rep}}
\gamma_2,
$$

then the distinction disappears at the reparameterization quotient.

If:

$$
\gamma_1
\not\simeq_{\mathrm{thin}}
\gamma_2
$$

but:

$$
\gamma_1\simeq_\partial\gamma_2,
$$

then the distinction does not disappear until the ordinary homotopy quotient.

---

# 40. Difference Emergence and Difference Collapse

Therefore, NTLA-O now has two complementary concepts:

$$
\boxed{
r(x,y)
}
$$

— the distinction is first seen by the observer;

and:

$$
\boxed{
q(\gamma_1,\gamma_2)
}
$$

— the distinction is first quotiented out by the quotient.

Together, they describe the:

$$
\boxed{
\text{difference lifecycle}.
}
$$

---

# 41. The Connection Between Path Transport and Sheaf Descent

Paper 5 investigated:

$$
\varphi_{ij}
$$

how local states transition over overlaps.

Paper 6 investigates:

$$
T_\gamma
$$

how states are transported along paths.

These two are not unrelated structures.

The transport-functor framework of Schreiber–Waldorf precisely places parallel transport, local trivializations, and smooth descent data into a unified categorical structure.

Therefore, NTLA-O can connect:

$$
\boxed{
\text{local transition}
}
$$

and:

$$
\boxed{
\text{path transport}
}
$$

into the same geometric main thread.

---

# 42. Observer Transport Structure

Thus, define:

$$
\boxed{
\mathfrak T_{\mathcal O}
=
\left(
X,
\mathscr F,
\mathcal P,
\mathcal T
\right)
}
$$

where:

- $X$: observer topology domain;
- $\mathscr F$: local observation states;
- $\mathcal P$: allowed path groupoid/path category;
- $\mathcal T$: transport functor.

For example:

$$
\boxed{
\mathcal T:
\mathcal P
\rightarrow
\mathbf C
}
$$

where:

$$
\mathbf C
$$

can be:

- $\mathbf{Set}$;
- vector spaces;
- groups;
- torsors;
- fibers;
- observer-state categories.

---

# 43. Transport Functoriality

If:

$$
\gamma:x\rightarrow y
$$

and:

$$
\delta:y\rightarrow z,
$$

then a reasonable transport must satisfy:

$$
\boxed{
T_{\delta\circ\gamma}
=
T_\delta
\circ
T_\gamma.
}
$$

and:

$$
\boxed{
T_{\operatorname{id}_x}
=
\operatorname{id}_{F_x}.
}
$$

Therefore:

$$
\boxed{
\text{history composition}
}
$$

corresponds to:

$$
\boxed{
\text{state transformation composition}.
}
$$

This is a very natural category-theoretic interface.

---

# 44. Noncommutative History

If there exist loops:

$$
a,b
$$

such that:

$$
[a][b]\neq[b][a]
$$

in:

$$
\pi_1(X,x)
$$

,

then:

$$
\boxed{
\text{path order matters}.
}
$$

If the transport representation can also distinguish:

$$
T_aT_b
\neq
T_bT_a,
$$

then the observer state directly preserves the noncommutative history.

---

# 45. Homology May Erase This Order

Upon entering:

$$
H_1
$$

,

the group operation is abelianized.

Therefore:

$$
[a]+[b]
=
[b]+[a].
$$

Thus:

$$
\boxed{
\text{noncommutative path history}
}
$$

in:

$$
H_1
$$

level may be unrecoverable.

This gives a very clear mathematical warning for the NTLA connection order:

$$
\boxed{
\text{If order is part of the identity,
do not solely preserve the abelianized invariant.}
}
$$

---

# 46. History-Sensitive NTLA Identity

Therefore, expand the identity specification of NTLA 2.0:

$$
\mathfrak I
$$

to:

$$
\boxed{
\mathfrak I
=
(
\mathfrak I_{\mathrm{state}},
\mathfrak I_{\mathrm{top}},
\mathfrak I_{\mathrm{path}},
\mathfrak I_{\mathrm{transport}}
).
}
$$

where:

### State identity

Looks at the final state.

### Topological identity

Looks at the spatial/connection topology.

### Path identity

Looks at which quotient level the path is preserved.

### Transport identity

Looks at what action the path has on the fiber/observer state.

---

# 47. Four Types of Sameness Should Not Be Conflated

It is possible that:

$$
x_{\mathrm{final}}
=
y_{\mathrm{final}},
$$

but:

$$
[\gamma_x]
\neq
[\gamma_y].
$$

It is also possible that:

$$
[\gamma_x]
=
[\gamma_y]
$$

at the ordinary homotopy level,

but:

$$
\gamma_x
\not\simeq_{\mathrm{thin}}
\gamma_y.
$$

It is even possible that two non-homotopic loops:

$$
[\gamma_x]\neq[\gamma_y]
$$

but for a certain covering representation:

$$
T_{\gamma_x}
=
T_{\gamma_y}.
$$

Therefore:

$$
\boxed{
\text{State Identity}
}
$$

$$
\neq
$$

$$
\boxed{
\text{Path Identity}
}
$$

$$
\neq
$$

$$
\boxed{
\text{Transport Identity}.
}
$$

---

# 48. M/I/E Roles Incorporating Transport

Paper 2 has:

$$
\rho_X(\mathcal O).
$$

Paper 5 adds:

$$
(U,s_U).
$$

This paper further adds:

$$
\gamma
$$

and:

$$
T_\gamma.
$$

Therefore, the observer state can be elevated to:

$$
\boxed{
\mathbf O_{\mathrm{path}}
=
\left(
\rho_X(\mathcal O),
U,
s_U,
R_{\mathcal O}^{\mathrm{path}},
T
\right).
}
$$

If all previous data are preserved, it can be written as:

$$
\boxed{
\mathbf O^\ast
=
\left(
S,
\rho,
\mathcal A,
\tau,
K,
\preceq,
\mathscr F,
R_{\mathrm{path}},
T
\right).
}
$$

---

# 49. Role Transition and Path Variation Are Still Different

The observer can have:

$$
\rho_X(\mathcal O)=I
$$

remain constant throughout,

but along an internal path:

$$
\gamma
$$

it is transported:

$$
s
\mapsto
T_\gamma(s).
$$

Therefore:

$$
\boxed{
\text{state transport}
\not\Rightarrow
\text{role transition}.
}
$$

Similarly, a role transition:

$$
I\rightarrow M
$$

does not automatically imply that:

$$
T_\gamma
$$

undergoes any nontrivial transformation.

---

# 50. Higher-Order Path Boundaries

The fundamental groupoid treats paths as morphisms.

But if one also needs to distinguish:

$$
H_1,H_2:
\gamma_1\Rightarrow\gamma_2
$$

these different homotopies,

then an ordinary groupoid is again insufficient.

It is necessary to enter:

$$
\boxed{
2\text{-groupoid}
}
$$

or even:

$$
\boxed{
\infty\text{-groupoid}.
}
$$

Higher-gauge theory has already used path $2$-groupoids and $2$-functors to describe higher parallel transport on curves and surfaces.

HoTT also views iterated identity structures—such as points, paths, and paths between paths—as an important intuition for higher groupoid-like structures.

---

# 51. NTLA-O Does Not Presuppose Preservation to Infinite Higher Orders

This point is particularly important.

NTLA-O does not claim that:

$$
\boxed{
\text{every application must completely preserve the }\infty\text{-groupoid}.
}
$$

Rather, it requires that:

$$
\boxed{
\text{the identity specification must state at which truncation level to stop.}
}
$$

For example, a certain application might only need:

$$
H_1.
$$

A certain application might need:

$$
\pi_1.
$$

A certain differential-geometric application might need:

$$
\Pi_1^{\mathrm{thin}}.
$$

Only a certain higher-gauge application might need:

$$
\Pi_2.
$$

---

# 52. Path Truncation Level

Therefore, we can define:

$$
\boxed{
\operatorname{TruncPath}(\mathcal O)
}
$$

to describe up to which level the observer preserves the path/higher-path structure.

But this quantity should not be simply understood as:

$$
0<1<2<3
$$

meaning "the higher, the better" inevitably.

Higher resolution entails higher information retention and computational cost.

Therefore:

$$
\boxed{
\text{resolution}
\neq
\text{utility}.
}
$$

---

# 53. A Complete NTLA Path Identity Ladder

Thus, this paper suggests:

$$
\boxed{
\mathcal P_{\mathrm{raw}}
}
$$

$$
\Downarrow
$$

$$
\boxed{
\mathcal P_{\mathrm{rep}}
}
$$

$$
\Downarrow
$$

$$
\boxed{
\Pi_1^{\mathrm{thin}}
}
$$

$$
\Downarrow
$$

$$
\boxed{
\Pi_1
}
$$

$$
\Downarrow
$$

$$
\boxed{
H_1
}
$$

$$
\Downarrow
$$

$$
\boxed{
\text{application-specific summary}.
}
$$

where each arrow is a candidate for an:

$$
\boxed{
\text{information-losing quotient / functor}
}
$$

.

---

# 54. Path Observation and the Original NTLA Proposition

The original NTLA intuition:

> Same number of holes, different connection methods, can still be different.

can now be upgraded to:

> Even if nodes, holes, starting points, and ending points are all identical, if the path class, transport action, or higher-order history differs, they may still be judged as different according to the identity specification.

Therefore:

$$
\boxed{
\text{same objects}
+
\text{same endpoints}
}
$$

still does not imply:

$$
\boxed{
\text{same NTLA identity}.
}
$$

The complete identity may at least depend on:

$$
\boxed{
\text{objects}
+
\text{connections}
+
\text{nesting}
+
\text{path classes}
+
\text{transport}.
}
$$

---

# 55. Core Theorem Group of This Paper

This paper obtains:

### Theorem A: Path Quotient Information Monotonicity

If:

$$
R_1\subseteq R_2,
$$

then there exists a:

$$
P/R_1\rightarrow P/R_2
$$

natural surjection.

### Theorem B: Covering Transport Functor

Covering path lifting induces:

$$
\boxed{
T_p:\Pi_1(X)\rightarrow\mathbf{Set}.
}
$$

### Theorem C: Nontrivial Monodromy Implies Endpoint Insufficiency

Nontrivial monodromy implies:

$$
\boxed{
\text{endpoint data cannot determine lifted state}.
}
$$

### Theorem D: Covering Observer Refinement

Under a nontrivial fiber:

$$
\boxed{
K_L\subsetneq K_B.
}
$$

### Theorem E: Fundamental Groupoid History Loss

Endpoint-fixed homotopic paths in:

$$
\Pi_1
$$

cannot be distinguished.

### Theorem F: Homological Abelianization Loss

For a path-connected $X$:

$$
H_1(X;\mathbb Z)
\cong
\pi_1(X,x)_{\mathrm{ab}},
$$

Therefore, noncommutative path-order information may be eliminated.

### Structure G: Connection Transport Functor

The parallel transport of a smooth bundle connection can be formulated by a path-groupoid functor.

---

# 56. Boundary with Traditional Mathematics

The following concepts used in this paper:

- paths;
- homotopies;
- fundamental group;
- fundamental groupoid;
- covering spaces;
- path lifting;
- monodromy;
- $H_1$;
- parallel transport;
- holonomy;
- thin homotopy;
- higher path groupoid;

all have existing theoretical backgrounds in topology, differential geometry, or higher category theory.

NTLA-O does not claim to have invented these structures.

This paper's own candidate contribution remains in the coupling of:

$$
\boxed{
\text{Observer Role}
}
$$

$$
+
$$

$$
\boxed{
\text{Observer Kernel}
}
$$

$$
+
$$

$$
\boxed{
\text{Path Identity Resolution}
}
$$

$$
+
$$

$$
\boxed{
\text{Transport Action}
}
$$

$$
+
$$

$$
\boxed{
\text{Explicit Identity Specification}.
}
$$

---

# 57. Statement of Theoretical Strength

This paper does not claim that:

- all histories in reality can be completely described by the fundamental groupoid;
- all path differences have physical significance;
- raw paths should always be preserved;
- homotopic paths are necessarily equivalent in all systems;
- holonomy is equivalent to memory;
- monodromy is equivalent to cognition;
- higher groupoids must be the internal data structures of AI;
- an observer with higher path resolution is necessarily smarter.

This paper only proposes that:

> When the identity of the research object depends on connection and transport history, path/groupoid/transport structures provide a more appropriate mathematical language than mere endpoints, Betti numbers, or homology summaries.

---

# 58. Conclusion of This Paper

At this stage, NTLA-O formally acquires its third mathematical axis.

The first is the:

$$
\boxed{
\text{Locality Axis}
}
$$

$$
U\supseteq V
\rightarrow
\mathscr F(U)\rightarrow\mathscr F(V)
\rightarrow
\mathscr F_x.
$$

The second is the:

$$
\boxed{
\text{Resolution Axis}
}
$$

$$
K_0
\supseteq
K_1
\supseteq
K_2
\supseteq
\cdots.
$$

The third is the newly added one in this paper:

$$
\boxed{
\text{Transport Axis}
}
$$

$$
x
\xrightarrow{\gamma}
y
$$

and:

$$
\boxed{
F_x
\xrightarrow{T_\gamma}
F_y.
}
$$

Therefore, NTLA-O is no longer just a "matryoshka topology."

It has become:

$$
\boxed{
\text{where}
\times
\text{what can be distinguished}
\times
\text{how states move}.
}
$$

More completely:

$$
\boxed{
\text{Role}
\times
\text{Locality}
\times
\text{Resolution}
\times
\text{Transport}.
}
$$

Among these, the most important conclusion is:

$$
\boxed{
\text{same endpoint}
\not\Rightarrow
\text{same path}
}
$$

$$
\boxed{
\text{same path homotopy class}
\not\Rightarrow
\text{same raw history}
}
$$

and:

$$
\boxed{
\text{different path classes}
\not\Rightarrow
\text{a particular observer distinguishes them}.
}
$$

Thus, "difference" must always specify:

$$
\boxed{
\text{at which path-resolution level,
by which observer,
and according to which transport representation it is determined.}
}
$$

This is precisely the formal algebraic topology version of the original NTLA principle: "as long as an effective difference exists in each connection, a distinct identity should be maintained."

---

# 59. Next Paper

Currently, we have the direct-limit direction of:

$$
\boxed{
\text{local restrictions}
}
$$

and the groupoid direction of:

$$
\boxed{
\text{path transport}
}
$$

.

The next paper will formally address a third structure that has long appeared but has not yet been fully encapsulated:

$$
\boxed{
K_0
\supseteq
K_1
\supseteq
K_2
\supseteq
\cdots.
}
$$

Thereby forming:

$$
\boxed{
X/K_0
\leftarrow
X/K_1
\leftarrow
X/K_2
\leftarrow
\cdots.
}
$$

And entering:

# **NTLA-O VI: Inverse Systems, Observer Towers, Inverse Limits, and Pro-Observer Identity**

Its core question will be:

> **If the final inverse limits of two systems are the same, but their entire histories of "at which level the distinction appears, and at which level it is quotiented out" are different, should they still be judged as identical by NTLA-O?**

The answer will lead to:

$$
\boxed{
\text{Limit Identity}
\neq
\text{Tower Identity}.
}
$$

This will formally advance the NTLA concept of "identical results do not equal identical generative histories" to the inverse-system level.

---

# References

1. Hatcher, A. *Algebraic Topology*, Chapter 1: Fundamental Group and Covering Spaces.
2. Hatcher, A. *Algebraic Topology*, covering-space lifting properties and homotopy lifting.
3. Schreiber, U., & Waldorf, K. (2009). *Parallel Transport and Functors*. Journal of Homotopy and Related Structures 4(1), 187–244.
4. Caetano, A., & Picken, R. F. (1994). *An Axiomatic Definition of Holonomy*. International Journal of Mathematics 5, 835–848.
5. Baez, J., & Schreiber, U. *Higher Gauge Theory*. Thin homotopy and higher holonomy structures.
6. Schreiber, U., & Waldorf, K. *Local Theory for 2-Functors on Path 2-Groupoids*.
7. The Univalent Foundations Program. *Homotopy Type Theory: Univalent Foundations of Mathematics*.
8. Neo.K & Aletheia (2026). *NTLA-O IV: Local-Global Observation, Presheaves, Sheaves, Stalks, and Descent*.

---

**Document Status:** Formal Draft v0.1  
**Series Position:** NTLA-O Series Paper 6 / 9  
**Next Paper:** NTLA-O VI — Inverse Systems, Observer Towers, Inverse Limits, and Pro-Observer Identity