# Finite Certificate Frontier: Exact Finite Collatz Coverage and the Global Gap
## — Series Capstone from Local Affine Atlas and Descent Sieve to Integer-Anchored Hard Branches

**English Title:** *Finite Certificate Frontiers for the Collatz Map: Exact Finite Coverage, Hard Prefix Domains, and the Remaining Global Quantifier Gap*

**作者：** Neo.K  
**機構：** Yiyannuo Technology Co., Ltd. (EveMissLab)  
**系列：** Collatz Operation Translation Series — Paper 09  
**版本：** v0.1.1  
**日期：** 2026-08-11  
**修訂日期：** 2026-08-14

---

## Abstract

The previous eight papers in this series have decomposed the finite local dynamics of the modified Collatz map

$$
T(n)=
\begin{cases}
n/2,&n\equiv0\pmod2,\\[2mm]
(3n+1)/2,&n\equiv1\pmod2
\end{cases}
$$

into:

$$
\boxed{
\text{finite parity word}
\longleftrightarrow
\text{unique residue cylinder}
\longrightarrow
\text{exact affine operator}
\longrightarrow
\text{local identity chart}
}
$$

and established:

$$
T^k(r_w+2^ka)=m_w+3^{u(w)}a,
$$

$$
T^k(n)<n
\iff
b_w<(2^k-3^{u(w)})n,
$$

as well as exact inverse recovery, valuation language, generalized $mx+r$, and RCOT algebraic boundaries.

This paper completes the final step: organizing the aforementioned local structures into a **finite exact certificate system**, and explicitly delineating the final insurmountable quantifier gap between finite verification and the global Collatz conjecture.

This paper first adopts the coefficient stopping-time formulation. For $n>1$, define:

$$
\boxed{
\sigma(n)
=
\inf\{j\ge1:T^j(n)<n\}.
}
$$

If all $n>1$ have finite $\sigma(n)$, then strong induction implies that all positive integers eventually enter the $1\leftrightarrow2$ cycle. Therefore:

$$
\boxed{
\text{Collatz conjecture}
\iff
\forall n>1,\ \sigma(n)<\infty.
}
$$

For a finite parity word

$$
w=w_1\cdots w_k
$$

and each of its prefixes $w_{\le j}$, let:

$$
u_j=u(w_{\le j}),
\qquad
b_j=b_{w_{\le j}},
\qquad
\Delta_j=2^j-3^{u_j}.
$$

From the exact affine formula in previous papers:

$$
T^j(n)-n
=
\frac{b_j-\Delta_jn}{2^j}.
$$

Thus, the condition that an input has **not yet descended** within the first $k$ steps can be completely exactified. Define the hard-prefix domain:

$$
\boxed{
H_w
=
\left\{
n\in\Omega_w:
T^j(n)\ge n,\ 1\le j\le k
\right\}.
}
$$

If the prefix $w_{\le j}$ is an expanding-skeleton:

$$
\Delta_j<0,
$$

then $T^j(n)>n$ holds automatically for all positive admissible $n$, imposing no upper bound on the hard domain.

If:

$$
\Delta_j>0,
$$

then:

$$
T^j(n)\ge n
\iff
n\le
\left\lfloor
\frac{b_j}{\Delta_j}
\right\rfloor.
$$

Therefore:

$$
\boxed{
H_w
=
\Omega_w
\cap
[1,h(w)]
}
$$

where:

$$
\boxed{
h(w)
=
\min_{
1\le j\le k,\ \Delta_j>0
}
\left\lfloor
\frac{b_j}{\Delta_j}
\right\rfloor
}
$$

If there is no contracting prefix, define:

$$
h(w)=+\infty.
$$

This is the first core result of this paper: **the "not-yet-descended set" of a finite parity prefix is not a fuzzy dynamical set, but the intersection of a unique residue cylinder and an exact integer height bound.**

Next, for the finite verification domain:

$$
I_N=[2,N]\cap\mathbb Z
$$

define the depth-$k$ hard frontier:

$$
\boxed{
\mathfrak F_k(N)
=
\{
w\in\{D,U\}^k:
H_w\cap I_N\neq\varnothing
\}.
}
$$

This paper proves:

$$
\boxed{
\mathfrak F_k(N)=\varnothing
}
$$

if and only if:

$$
\boxed{
\sigma(n)\le k
\quad
\forall\,2\le n\le N.
}
$$

Therefore, for a fixed finite $N$, Collatz verification can be completely rewritten as:

> Continuously refine residue cylinders until the finite hard frontier is empty.

This turns finite verification into an exact set-cover / frontier-extinction problem, eliminating the need to treat every complete trajectory as an independent proof object.

This paper defines five classes of finite certificates:

1. **Terminal Certificate**: Directly reaches $1$ or $2$;
2. **Descent Certificate**: A finite prefix satisfies $T^j(n)<n$;
3. **Cylinder Threshold Certificate**: An entire residue cylinder descends above a certain exact threshold;
4. **Merge Certificate**: The trajectory merges in finite time with a trajectory already proven from a smaller starting point;
5. **Inverse/Preimage Certificate**: Uses exact inverse fibers to prove a state lies on the path of an already proven smaller starting point.

A finite certificate family:

$$
\boxed{
\mathcal C_N
}
$$

is called coverage-complete if:

$$
\boxed{
I_N
\subseteq
\bigcup_{\gamma\in\mathcal C_N}D_\gamma
}
$$

and each certificate can be checked via finite integer arithmetic, finite word recurrence, congruence, transport identity, or an explicit dependency graph.

In the simplest strong-induction version, only descent / terminal certificates are needed. If:

$$
T^j(n)<n,
$$

then $T^j(n)$ is already proven to converge by the smaller-starting-point hypothesis, so $n$ converges. Merge / preimage certificates further allow:

$$
T^j(n)=T^\ell(n_0),
\qquad
n_0<n,
$$

Even if the common merge state itself is not smaller than $n$, convergence can still be inherited from the known trajectory of $n_0$.

This paper revises the earlier BCCP into:

$$
\boxed{
\text{finite bidirectional coverage-complete certification}.
}
$$

Its reasonable goal is not to directly claim "all natural numbers have been covered by bidirectional construction," but to establish an exact proof-object family for each finite $N$:

$$
\mathcal C_N.
$$

This paper also incorporates the residue threshold compiler from previous experiments into a pure mathematical framework. For:

$$
n=r+2^ka,
$$

if:

$$
T^k(n)=m_r+3^ua,
$$

then:

$$
T^k(n)<n
$$

is equivalent to:

$$
\boxed{
(2^k-3^u)a>m_r-r.
}
$$

Thus, each contracting chart can be pre-compiled into an exact integer quotient threshold:

$$
\boxed{
a>
\frac{m_r-r}{2^k-3^u}.
}
$$

This is the mathematical essence of the earlier $k=16$ threshold certificates. In the previous prototype for $1\le n<2^{20}$, the number of $k=16$ direct strict-descent certificates was:

$$
938413,
$$

and can be completely explained by the $58651$ contracting residue classes from Paper 05 plus finite boundary corrections.

This paper further addresses the easily misused "infinite hard tree". For each formal infinite parity sequence, its nested residues:

$$
r_k\bmod2^k
$$

naturally define a $2$-adic integer; but this $2$-adic integer is not necessarily an ordinary positive integer. Therefore:

$$
\boxed{
\text{infinite formal hard branch}
\not\Rightarrow
\text{positive-integer Collatz counterexample}.
}
$$

To precisely correspond to ordinary positive integers, this paper defines an **integer-anchored branch**. If the canonical residues of a nested branch:

$$
0\le r_k<2^k
$$

have a fixed:

$$
n\in\mathbb Z_{>0}
$$

such that:

$$
\boxed{
r_k=n
}
$$

holds for all sufficiently large $k$, then the branch is said to be anchored at $n$. This eventual stabilization condition exactly characterizes an ordinary positive integer embedded in $\mathbb Z_2$.

This paper proves:

$$
\boxed{
\sigma(n)=\infty
}
$$

if and only if the parity-prefix chain of $n$ forms an anchored hard branch, that is:

$$
\boxed{
n\in H_{w_{\le k}(n)}
\quad
\forall k.
}
$$

Therefore:

$$
\boxed{
\text{Collatz conjecture}
\iff
\text{there exists no integer-anchored infinite hard branch for }n>1.
}
$$

This formulation is more precise than "the hard-prefix tree is well-founded". Requiring **all formal $2$-adic hard branches** to vanish yields an overly strong condition; Collatz only needs to exclude infinite obstructions anchored by ordinary positive integers.

This paper also obtains another exact global formulation:

$$
\boxed{
\forall N\ge2,\ \exists K(N)<\infty:
\mathfrak F_{K(N)}(N)=\varnothing.
}
$$

This is equivalent to:

$$
\forall n>1,\ \sigma(n)<\infty
$$

but cannot be generally swapped to:

$$
\boxed{
\exists K\ \forall N:
\mathfrak F_K(N)=\varnothing.
}
$$

The latter is equivalent to all stopping times having a global uniform bound, which is far stronger than Collatz and incompatible with known/observed unbounded stopping-time behavior.

This is exactly the final quantifier boundary of this series:

$$
\boxed{
\forall N\,\exists K(N)
\not\Rightarrow
\exists K\,\forall N.
}
$$

Angeltveit's 2026 finite verification algorithm is highly consistent with the certificate viewpoint of this paper: his algorithm recursively splits by the lowest $k$ bits, uses a descent sieve, preimage sieve, and path-merging sieve, and explicitly points out that the fraction requiring explicit checking can approach 0, but the actual number of integers to check still goes to infinity. Barina's public verification has advanced the complete verification frontier to $2^{71}$. These results all support the final positioning of this paper: **finite residue-class pruning can be extremely powerful, even driving survivor density to zero, but finite computational completeness and infinite universal proof remain distinct propositions.**

This paper therefore caps the entire nine-paper series with the following sentence:

$$
\boxed{
\textbf{Collatz dynamics is locally affine-trivializable,
finitely certificate-compressible,
but globally itinerary-unresolved.}
}
$$

English:

> **Collatz dynamics can be exactly affinized and even locally trivialized within fixed finite decision domains; any finite range can be organized into a machine-checkable finite certificate coverage problem; but the global conjecture remains equivalent to excluding all infinite non-descending itineraries anchored by ordinary positive integers.**

This paper does not claim to have proven the Collatz conjecture. What it accomplishes is: exactifying all parts of this series that can be exactified, and explicitly isolating the final universal obligation that cannot be automatically deduced from these local theorems.

**Keywords:** Collatz conjecture, finite certificate, stopping time, residue cylinder, descent sieve, path merging, hard frontier, 2-adic parity, strong induction, operation translation

---

# 1. The Final Proof Obligation of the Series

The Collatz conjecture can be written as:

$$
\forall n>0,\quad
T^j(n)\in\{1,2\}
$$

for some $j$.

But for strong induction, it is more convenient to use the stopping-time form.

---

# 2. Coefficient Stopping Time

For:

$$
n>1,
$$

define:

$$
\boxed{
\sigma(n)
=
\inf\{j\ge1:T^j(n)<n\}.
}
$$

If it does not exist, let:

$$
\sigma(n)=\infty.
$$

Note:

$$
\sigma(1)
$$

does not need to be defined as finite, because $1$ is the induction base / a member of the terminal cycle.

---

# 3. Finite Stopping Time $\Rightarrow$ Collatz

## Theorem 3.1

If:

$$
\boxed{
\sigma(n)<\infty
\quad
\forall n>1,
}
$$

then the Collatz conjecture holds.

### Proof

By strong induction on $n$.

Base:

$$
1
$$

is already in the terminal cycle.

For:

$$
n>1,
$$

there exists:

$$
j
$$

such that:

$$
T^j(n)<n.
$$

By the induction hypothesis:

$$
T^j(n)
$$

eventually reaches 1.

Thus $n$ also eventually reaches 1.

Q.E.D.

---

# 4. Collatz $\Rightarrow$ Finite Stopping Time

If $n>1$ eventually reaches:

$$
1<n,
$$

then the first time it drops below $n$ along the way gives:

$$
\sigma(n)<\infty.
$$

Therefore:

## Theorem 4.1

$$
\boxed{
\text{Collatz}
\iff
\forall n>1,\ \sigma(n)<\infty.
}
$$

This is the foundation of the global equivalence in this paper.

---

# 5. Prefix Affine Data

For a length-$k$ word:

$$
w=w_1\cdots w_k,
$$

let the prefix be:

$$
w_{\le j}=w_1\cdots w_j.
$$

Denote:

$$
u_j=u(w_{\le j}),
$$

$$
b_j=b_{w_{\le j}}.
$$

Then from Paper 02:

$$
\boxed{
T^j(n)
=
\frac{3^{u_j}n+b_j}{2^j}
}
$$

holds for:

$$
n\in\Omega_w
$$

and:

$$
1\le j\le k.
$$

---

# 6. Prefix Drift Gap

Define:

$$
\boxed{
\Delta_j
=
2^j-3^{u_j}.
}
$$

Therefore:

$$
\boxed{
T^j(n)-n
=
\frac{b_j-\Delta_jn}{2^j}.
}
$$

Whether each prefix has already achieved strict descent is thus an exact linear inequality.

---

# 7. Hard Prefix Domain

## Definition 7.1

$$
\boxed{
H_w
=
\left\{
n\in\Omega_w:
T^j(n)\ge n
\quad
\forall\,1\le j\le k
\right\}.
}
$$

That is:

> All positive integers that have prefix $w$ but have not yet obtained a strong-induction descent certificate up to depth $k$.

---

# 8. Expanding Prefixes Impose No Restrictions on the Hard Domain

If:

$$
\Delta_j<0,
$$

that is:

$$
3^{u_j}>2^j,
$$

then:

$$
b_j-\Delta_jn
=
b_j+(3^{u_j}-2^j)n>0.
$$

Therefore:

$$
\boxed{
T^j(n)>n
}
$$

for all positive admissible $n$.

Thus, this prefix cannot provide a descent certificate.

---

# 9. Contracting Prefixes Provide a Hard Height

If:

$$
\Delta_j>0,
$$

then:

$$
T^j(n)\ge n
$$

iff:

$$
b_j\ge\Delta_jn.
$$

Therefore:

$$
\boxed{
n
\le
\left\lfloor
\frac{b_j}{\Delta_j}
\right\rfloor.
}
$$

Thus, a contracting prefix generates an exact upper bound for those that have not yet descended.

---

# 10. Hard Height Theorem

Define:

$$
\boxed{
h(w)
=
\min_{
j\le k,\ \Delta_j>0
}
\left\lfloor
\frac{b_j}{\Delta_j}
\right\rfloor
}
$$

If there is no:

$$
\Delta_j>0,
$$

let:

$$
h(w)=+\infty.
$$

Then:

## Theorem 10.1

$$
\boxed{
H_w
=
\Omega_w
\cap
[1,h(w)].
}
$$

If:

$$
h(w)=+\infty,
$$

that is:

$$
H_w=\Omega_w.
$$

---

# 11. Proof

$n\in H_w$ iff for all prefixes:

$$
T^j(n)\ge n.
$$

Expanding prefixes hold automatically.

Contracting prefixes require:

$$
n\le
\left\lfloor b_j/\Delta_j\right\rfloor.
$$

Therefore, the intersection of all conditions is exactly the minimum upper bound.

Q.E.D.

---

# 12. The Importance of This Result

A hard domain does not need to store:

$$
T(n),T^2(n),\ldots,T^k(n)
$$

the entire numerical path.

It only needs to store:

$$
\boxed{
(r_w,2^k,h(w)).
}
$$

That is:

$$
\boxed{
\text{one residue cylinder}
\cap
\text{one height cap}.
}
$$

This is a highly compressed form of finite obstruction.

---

# 13. Hard Domains Can Be Finite or Infinite

If the word has encountered at least one contracting prefix so far:

$$
h(w)<\infty,
$$

then:

$$
H_w
$$

is a finite set.

If all prefixes are on the expanding-skeleton side:

$$
h(w)=\infty,
$$

then:

$$
H_w=\Omega_w
$$

remains an infinite arithmetic progression.

Therefore, hard-prefix analysis simultaneously distinguishes between:

- finite correction obstructions;
- pure skeleton obstructions.

---

# 14. Finite Verification Interval

Fix:

$$
N\ge2.
$$

Define:

$$
\boxed{
I_N
=
\{2,3,\ldots,N\}.
}
$$

We only ask:

> Has every starting value in $I_N$ obtained a finite stopping-time certificate?

---

# 15. Depth-$k$ Hard Frontier

Define:

$$
\boxed{
\mathfrak F_k(N)
=
\left\{
w\in\{D,U\}^k:
H_w\cap I_N\neq\varnothing
\right\}.
}
$$

Each element is:

> A parity cylinder that still contains at least one non-descending starting value up to depth $k$.

---

# 16. Frontier Extinction Theorem

## Theorem 16.1

$$
\boxed{
\mathfrak F_k(N)=\varnothing
}
$$

iff:

$$
\boxed{
\sigma(n)\le k
\quad
\forall n\in I_N.
}
$$

### Proof

If the frontier is empty, then for any $n\le N$, its length-$k$ parity word $w_k(n)$ does not contain $n$ in $H_w$, so there exists $j\le k$:

$$
T^j(n)<n.
$$

Conversely, if all $n\le N$ descend within $k$ steps, then no hard domain can intersect with $I_N$.

Q.E.D.

---

# 17. The Frontier Form of Finite Verification

Therefore, for a fixed $N$:

$$
\boxed{
\text{verify Collatz on }[2,N]
}
$$

is equivalent to:

$$
\boxed{
\text{refine hard cylinders until }\mathfrak F_k(N)=\varnothing.
}
$$

This is not a heuristic.

It is an exact finite equivalence.

---

# 18. Basic Definition of a Finite Certificate

A finite certificate:

$$
\gamma
$$

contains:

1. source domain $D_\gamma$;
2. finite word / affine data;
3. claim type;
4. exact target relation;
5. if needed, dependency on previously certified objects.

And requires:

$$
\boxed{
\text{all checks terminate in finite exact arithmetic}.
}
$$

---

# 19. Terminal Certificate

If:

$$
T^j(n)\in\{1,2\},
$$

then:

$$
\boxed{
\gamma_T(n,j)
}
$$

directly proves convergence.

Its dependency rank is 0.

---

# 20. Descent Certificate

If:

$$
T^j(n)<n,
$$

then:

$$
\boxed{
\gamma_D(n,j)
}
$$

proves $n$ converges via strong induction.

This is the most fundamental finite certificate.

---

# 21. Cylinder Threshold Certificate

For word $w$:

$$
T^k(n)
=
\frac{3^un+b_w}{2^k}.
$$

If:

$$
3^u<2^k,
$$

define:

$$
\theta_w
=
\left\lfloor
\frac{b_w}{2^k-3^u}
\right\rfloor+1.
$$

Then:

$$
\boxed{
D_{\gamma_w}
=
\{
n\in\Omega_w:n\ge\theta_w
\}
}
$$

all starting values in it share the same descent proof.

Thus, a single certificate can cover an infinite arithmetic subset.

---

# 22. Quotient-Threshold Compiler

Write:

$$
n=r_w+2^ka,
$$

and:

$$
T^k(n)=m_w+3^ua.
$$

Then:

$$
T^k(n)<n
$$

iff:

$$
m_w+3^ua
<
r_w+2^ka.
$$

Therefore:

$$
\boxed{
(2^k-3^u)a
>
m_w-r_w.
}
$$

If:

$$
2^k>3^u,
$$

it can be pre-compiled as:

$$
\boxed{
a
>
\frac{m_w-r_w}{2^k-3^u}.
}
$$

This is an integer hot-loop certificate, not a floating log approximation.

---

# 23. Exact Quotient Threshold

We can define:

$$
\boxed{
q_w
=
\left\lfloor
\frac{m_w-r_w}
{2^k-3^u}
\right\rfloor+1.
}
$$

Then:

$$
\boxed{
a\ge q_w
\Rightarrow
T^k(r_w+2^ka)
<
r_w+2^ka.
}
$$

Therefore, the certificate payload can be reduced to:

$$
\boxed{
(r_w,k,u,m_w,q_w).
}
$$

---

# 24. Interfacing with the Earlier $k=16$ Prototype

The previous prototype for:

$$
1\le n<2^{20}
$$

used:

$$
k=16.
$$

Paper 05 has proven that the number of length-16 contracting residue classes is:

$$
\boxed{
58651
}
$$

After finite positive-domain and strict-equality corrections,

the actual direct strict-descent certificates cover:

$$
\boxed{
938413
}
$$

starting values.

Therefore, the "pruning" in early benchmarks can be completely reinterpreted as:

$$
\boxed{
\text{finite certificate coverage ratio}.
}
$$

---

# 25. Merge Certificate

Descent is not the only usable strong-induction information.

If:

$$
T^j(n)
=
T^\ell(n_0)
$$

and:

$$
n_0<n,
$$

then by the induction hypothesis:

$$
n_0
$$

converges.

Therefore, its subsequent state:

$$
T^\ell(n_0)
$$

converges.

Thus $n$ also converges.

Define:

$$
\boxed{
\gamma_M
=
(n,n_0,j,\ell)
}
$$

as a merge certificate.

---

# 26. Path Merging Does Not Require the Merge State to be Smaller Than $n$

What matters is:

$$
n_0<n,
$$

rather than:

$$
T^j(n)<n.
$$

Therefore, the merge sieve can exclude more starting values than a simple descent sieve.

This is fully compatible with Angeltveit's 2026 path-merging sieve.

---

# 27. Preimage / Inverse-Fiber Certificate

If it can be proven that:

$$
n=T^\ell(n_0)
$$

for some:

$$
n_0<n,
$$

then $n$ itself lies on the trajectory of an already proven smaller starting value.

For example, the modified inverse:

$$
n\equiv2\pmod3
$$

when:

$$
n=T\left(\frac{2n-1}{3}\right).
$$

If:

$$
\frac{2n-1}{3}<n,
$$

then $n$ can be directly excluded as a new starting case.

This is a preimage certificate.

---

# 28. Inverse Fibers from Paper 04 Enter the Certificate System

Accelerated odd map:

$$
R_\kappa(t)
=
\frac{2^\kappa t-1}{3}.
$$

If:

$$
2^\kappa t\equiv1\pmod3,
$$

then $R_\kappa(t)$ is the exact odd predecessor of $t$.

Therefore, inverse-fiber data can serve as:

- merge proofs;
- preimage sieves;
- known terminal basin certificates.

---

# 29. Certificate Dependency Graph

If only descent certificates are used,

strong induction itself provides the dependency:

$$
n\to m<n.
$$

If merge / preimage are added,

a directed dependency graph can be established:

$$
\gamma_i\to\gamma_j.
$$

Requiring the existence of a rank:

$$
\rho:\mathcal C_N\to\mathbb N
$$

such that for every dependency edge:

$$
\boxed{
\rho(\gamma_j)<\rho(\gamma_i).
}
$$

Then the finite dependency graph has no cycles,

and all certificates eventually resolve to terminal objects.

---

# 30. Coverage-Complete Certificate Family

## Definition 30.1

For:

$$
I_N=[2,N],
$$

a finite family:

$$
\mathcal C_N
$$

If it satisfies:

$$
\boxed{
I_N
\subseteq
\bigcup_{\gamma\in\mathcal C_N}D_\gamma
}
$$

and all certificate claims / dependencies are exact-valid,

then it is called:

$$
\boxed{
\mathcal C_N
\text{ coverage-complete}.
}
$$

---

# 31. Finite Certificate Completeness Theorem

If:

$$
\mathcal C_N
$$

is coverage-complete,

and the dependency graph is well-ranked to terminal cases,

then:

$$
\boxed{
\text{Collatz is verified for every }2\le n\le N.
}
$$

This is a finite theorem.

---

# 32. The Formal Revised Version of BCCP

Old BCCP:

$$
\text{Forward}
+
\text{Backward}
+
\text{Coverage}.
$$

Now it can be rewritten as:

### Forward certificate

Finite word / affine descent.

### Backward certificate

Preimage / inverse fiber / merge.

### Coverage completeness

$$
I_N
\subseteq
\cup D_\gamma.
$$

Therefore:

$$
\boxed{
\text{BCCP}_{\mathrm{finite}}
=
\text{bidirectional finite proof-object coverage}.
}
$$

---

# 33. Why is Finite BCCP Rigorous?

Because for a fixed:

$$
N,
$$

all:

- source values;
- words;
- congruences;
- inequalities;
- dependency graphs;

are finite.

Thus, they can be recomputed by an independent checker.

It does not require:

- probabilistic extrapolation;
- decimal digit heuristics;
- infinite tree assertions.

---

# 34. Machine-Checkable Certificate Schema

Conceptually, a chart certificate can store:

$$
\boxed{
\gamma=
(
\text{type},
w,k,u,b,r,m,
L,U,
\theta,
\text{dependencies}
).
}
$$

where:

- $w$: parity word;
- $k$: depth;
- $u$: odd-step count;
- $b$: affine correction;
- $r$: source residue;
- $m$: target base;
- $[L,U]$: finite coverage range;
- $\theta$: descent threshold;
- dependencies: merge/preimage references.

The checker only needs to verify:

$$
F_w(x)
=
\frac{3^ux+b}{2^k},
$$

$$
r\equiv-b3^{-u}\pmod{2^k},
$$

and the corresponding inequality / merge identity.

---

# 35. The Difference Between Proof Objects and Trajectory Logs

A trajectory log stores:

$$
n,T(n),T^2(n),\ldots.
$$

A certificate stores:

$$
\boxed{
\text{an entire congruence family plus a finite proof rule}.
}
$$

Therefore:

$$
\boxed{
\text{trajectory enumeration}
\to
\text{structural proof compression}.
}
$$

This is the core value of operation translation for finite verification.

---

# 36. Comparison with Angeltveit's 2026 Algorithm

Angeltveit's 2026 verification algorithm:

1. Recursive split by least significant bits;
2. Simultaneous processing of the same residue family;
3. Uses descent sieve;
4. Uses mod-$9$ preimage sieve;
5. Uses path-merging sieve;
6. Explicitly iterates the remaining survivors.

This is highly consistent with this paper's:

$$
\boxed{
\text{residue frontier}
+
\text{descent certificates}
+
\text{inverse/merge certificates}
}
$$

---

# 37. However, This Paper Does Not Claim This Verification Idea as a New Discovery

Low-bit parity grouping, lookup-table sieves, descent sieves, and preimage sieves all have established traditions in computational Collatz.

Angeltveit also explicitly states that many of these sieves are standard ideas, and his novelties lie primarily in recursively adding bits and overall algorithmic scaling.

The work of this paper is:

$$
\boxed{
\text{Unifying the local algebra of the previous eight papers into certificate semantics}.
}
$$

---

# 38. Current Computational Context of the Finite Frontier

Barina has publicly reported complete convergence verification for:

$$
\boxed{
n<2^{71}
}
$$

Angeltveit 2026 proposes:

> The time growth required to expand from $2^N$ to $2^{N+1}$ can be compressed to less than a factor of 2,

and estimates that his method could push to higher ranges using similar resources.

These are all advancements in the:

$$
\boxed{
\text{finite certificate / computation frontier}
}
$$

rather than an infinite proof.

---

# 39. Survivor Fraction $\to0$ Still Does Not Equal a Proof

Angeltveit points out:

As:

$$
N\to\infty,
$$

the fraction requiring explicit checking can approach:

$$
0.
$$

But he also explicitly points out:

$$
\boxed{
\text{the number of integers to check still goes to infinity}.
}
$$

This sentence is almost the computational version of the global quantifier gap in this paper.

---

# 40. Why Can't We Deduce the Universal from "Fraction Approaching Zero"?

Because:

$$
\boxed{
\frac{|E_N|}{N}\to0
}
$$

does not mean:

$$
\boxed{
E_N=\varnothing
}
$$

for sufficiently large $N$.

It is even possible that:

$$
|E_N|\to\infty
$$

while simultaneously:

$$
|E_N|/N\to0.
$$

Therefore:

$$
\boxed{
\text{density-zero survivors}
\neq
\text{no survivors}.
}
$$

This is completely consistent with the quantifier warning in Paper 05:

$$
P_k\to1
$$

---

# 41. The Temptation of Infinite Hard Branches

It is natural to think:

> If the hard-prefix tree has no infinite branches, doesn't that prove Collatz?

As a sufficient condition, this is correct.

But treating it as an equivalent condition would be too strong.

The reason lies in $2$-adic completion.

---

# 42. Infinite Parity Prefixes Define a $2$-adic Integer

Paper 03:

Each finite parity prefix corresponds to:

$$
r_k\bmod2^k.
$$

Nested prefixes:

$$
r_{k+1}\equiv r_k\pmod{2^k}.
$$

Therefore:

$$
(r_k)
$$

defines an inverse-limit point:

$$
\boxed{
x\in\mathbb Z_2.
}
$$

But:

$$
x
$$

is not necessarily in:

$$
\mathbb Z_{>0}.
$$

---

# 43. Formal Infinite Branches Are Not Ordinary Integer Counterexamples

Thus, there might exist:

$$
\boxed{
\text{an infinite formal parity/hard branch}
}
$$

but its $2$-adic limit:

$$
x
$$

is:

- a negative integer;
- a nonordinary $2$-adic integer;
- or another point not in the positive naturals.

Therefore:

$$
\boxed{
\text{formal branch existence}
\not\Rightarrow
\text{positive-integer counterexample}.
}
$$

---

# 44. Canonical Residues

For each modulo:

$$
2^k
$$

class, choose the canonical representative:

$$
\boxed{
0\le r_k<2^k.
}
$$

If the branch comes from a fixed ordinary positive integer $n$,

then when:

$$
2^k>n,
$$

we have:

$$
\boxed{
r_k=n.
}
$$

Therefore, the canonical residues will eventually stabilize.

---

# 45. Integer-Anchored Branch

## Definition 45.1

An infinite nested parity branch:

$$
w_1\prec w_2\prec\cdots
$$

is called anchored at:

$$
n\in\mathbb Z_{>0}
$$

if there exists:

$$
K
$$

such that:

$$
\boxed{
r_{w_k}=n
\quad
\forall k\ge K.
}
$$

This is equivalent to its $2$-adic point being exactly the ordinary positive integer $n$.

---

# 46. Anchored Hard Branch

If furthermore:

$$
\boxed{
n\in H_{w_k}
\quad
\forall k,
}
$$

then it is called an:

$$
\boxed{
\text{integer-anchored infinite hard branch}.
}
$$

That is:

> The same ordinary positive integer $n$ has not obtained a descent certificate at any finite depth.

---

# 47. Counterexample Equivalence Theorem

## Theorem 47.1

For:

$$
n>1,
$$

the following are equivalent:

1. $\sigma(n)=\infty$;
2. For all $k$:
   $$
   T^j(n)\ge n
   \quad
   1\le j\le k;
   $$
3. The parity-prefix chain of $n$ is an integer-anchored infinite hard branch.

### Proof

(1)$\Rightarrow$(2): The definition of infinite stopping time.

(2)$\Rightarrow$(3): The canonical residue of $n$ equals $n$ after $2^k>n$, and every prefix is hard.

(3)$\Rightarrow$(1): If descent occurs at some finite $j$, then all longer prefixes are no longer hard, a contradiction.

Q.E.D.

---

# 48. The Minimal Obstruction Form of Global Collatz

Therefore:

## Theorem 48.1

$$
\boxed{
\text{Collatz conjecture}
}
$$

is equivalent to:

$$
\boxed{
\text{There exists no infinite hard branch anchored at }n>1.
}
$$

This is what this paper considers the cleanest global remainder statement.

---

# 49. Why Not "The Entire Hard Tree is Well-Founded"?

If we require:

$$
\boxed{
\text{no infinite formal hard branch in }\mathbb Z_2,
}
$$

that would exclude all nonordinary $2$-adic obstructions.

The Collatz conjecture itself does not require this.

Therefore:

$$
\boxed{
\text{2-adic global well-foundedness}
}
$$

is a stronger proposition.

This paper only retains:

$$
\boxed{
\text{positive-integer anchored well-foundedness}.
}
$$

---

# 50. Finite Frontier Function

If Collatz is verified for:

$$
[2,N]
$$

define:

$$
\boxed{
K(N)
=
\min
\{
k:
\mathfrak F_k(N)=\varnothing
\}.
}
$$

It is exactly:

$$
\boxed{
K(N)=\max_{2\le n\le N}\sigma(n)
}
$$

under the strict stopping-time definition.

Thus, the finite certificate depth is a natural frontier complexity statistic.

---

# 51. The Quantifier Form of the Global Conjecture

Collatz is equivalent to:

$$
\boxed{
\forall N\ge2,\ \exists K(N)<\infty:
\mathfrak F_{K(N)}(N)=\varnothing.
}
$$

Note the quantifier order:

$$
\boxed{
\forall N\,\exists K(N).
}
$$

---

# 52. Cannot Be Swapped for Uniform Depth

The stronger proposition:

$$
\exists K\ \forall N:
\mathfrak F_K(N)=\varnothing.
$$

is equivalent to:

$$
\boxed{
\sigma(n)\le K
\quad
\forall n>1.
}
$$

That is, all stopping times have a uniform global bound.

Collatz does not require this.

Therefore:

$$
\boxed{
\forall N\,\exists K(N)
\not\equiv
\exists K\,\forall N.
}
$$

---

# 53. This is the Final Quantifier Gap of the Series

The previous eight papers can be:

- exact for fixed $w$;
- exact for fixed $k$;
- exact for fixed $N$;
- exact for finite families.

But Collatz is an unbounded statement for:

$$
\boxed{
\forall n
}
$$

Therefore, any finite certificate framework, without additional theorems controlling:

$$
K(N)
$$

or anchored hard branches,

cannot be upgraded to a global proof simply by "succeeding for every tested $N$".

---

# 54. Finite Certificate Frontier

This paper ultimately calls:

$$
\boxed{
\mathfrak F_k(N)
}
$$

the hard side of the **Finite Certificate Frontier**.

Conversely, domains that have been certified by:

- descent;
- merge;
- preimage;
- terminal;

constitute the certified side.

Therefore:

$$
I_N
=
\boxed{
\text{Certified Region}
\sqcup
\text{Hard Frontier}.
}
$$

---

# 55. Frontier Refinement

From depth:

$$
k
$$

to:

$$
k+1,
$$

we only need to expand the cylinders in:

$$
\mathfrak F_k(N)
$$

Already certified charts do not need to be expanded again.

So the algorithmic search tree is:

$$
\boxed{
\text{expand only surviving proof obligations}.
}
$$

This is the natural form of certificate-oriented computation.

---

# 56. Monotonicity of the Hard Frontier

For a fixed $N$, consider the unproven starting-value set:

$$
E_k(N)
=
\{
n\in I_N:
\sigma(n)>k
\}.
$$

Then:

$$
\boxed{
E_{k+1}(N)\subseteq E_k(N).
}
$$

And:

$$
\mathfrak F_k(N)
$$

is merely the compressed representation of $E_k(N)$ in the level-$k$ residue atlas.

Therefore:

$$
\boxed{
\text{frontier refinement is monotone in obligations}.
}
$$

---

# 57. Certificate Compression Ratio

We can define:

$$
\boxed{
\eta_k(N)
=
1-
\frac{|E_k(N)|}{N-1}.
}
$$

representing the starting-value fraction that has obtained a descent certificate at depth-$k$.

We can also define the chart-level:

$$
\boxed{
\eta_k^{\mathrm{chart}}
=
1-
\frac{|\mathfrak F_k(N)|}{2^k}
}
$$

But the two should not be confused.

Paper 05 has shown:

$$
\boxed{
\text{chart density}
\neq
\text{finite strict certificate density}
}
$$

will have minor differences under finite boundaries.

---

# 58. Certificate Minimality is Not a Necessary Condition

A finite range may have many different certificate families:

$$
\mathcal C_N.
$$

One can pursue:

- minimum certificate count;
- minimum total word length;
- minimum verifier work;
- maximum cylinder coverage;
- maximum merge reuse.

But these are proof compression optimizations,

which do not affect logical validity.

---

# 59. Separation of Proof Complexity and Truth

That Collatz is true for:

$$
[2,N]
$$

only means there exists some finite brute-force proof.

The RCOT certificate framework is concerned with:

$$
\boxed{
\text{Whether it can be expressed using more structured, smaller, and more reusable proof objects}.
}
$$

Therefore:

$$
\boxed{
\text{verification complexity}
\neq
\text{mathematical truth}.
}
$$

---

# 60. The Final Structural Map of the Series

Paper 01:

$$
\text{Correction of prior research evidence}.
$$

Paper 02:

$$
\text{finite word}\to\text{affine operator}.
$$

Paper 03:

$$
\text{word}\leftrightarrow2^k\text{ cylinder}\to\text{identity chart}.
$$

Paper 04:

$$
2^k\text{ source}\leftrightarrow3^u\text{ target}.
$$

Paper 05:

$$
\text{exact contraction boundary}.
$$

Paper 06:

$$
\text{valuation-language compression}.
$$

Paper 07:

$$
mx+r\text{ generalization}.
$$

Paper 08:

$$
\text{algebraic domain / breakage ladder}.
$$

Paper 09:

$$
\boxed{
\text{all local results}
\to
\text{finite proof-object frontier}
\to
\text{global quantifier boundary}.
}
$$

---

# 61. Summary of Main Theorems in This Paper

## Theorem A — Collatz / Finite Stopping-Time Equivalence

$$
\boxed{
\text{Collatz}
\iff
\forall n>1,\sigma(n)<\infty.
}
$$

## Theorem B — Hard Height Formula

$$
\boxed{
H_w
=
\Omega_w\cap[1,h(w)].
}
$$

## Theorem C — Frontier Extinction

$$
\boxed{
\mathfrak F_k(N)=\varnothing
\iff
\sigma(n)\le k
\quad\forall2\le n\le N.
}
$$

## Theorem D — Cylinder Quotient Certificate

$$
\boxed{
(2^k-3^u)a>m_w-r_w
\Rightarrow
T^k(n)<n.
}
$$

## Theorem E — Finite Coverage Completeness

$$
\boxed{
I_N
\subseteq
\bigcup_{\gamma\in\mathcal C_N}D_\gamma
}
$$

plus valid ranked dependencies implies convergence for all $n\le N$.

## Theorem F — Anchored Hard Branch Equivalence

$$
\boxed{
\sigma(n)=\infty
\iff
n\text{ anchors an infinite hard branch}.
}
$$

## Theorem G — Global Frontier Form

$$
\boxed{
\text{Collatz}
\iff
\forall N\ge2,\exists K(N):
\mathfrak F_{K(N)}(N)=\varnothing.
}
$$

---

# 62. What Does This Paper Not Prove?

This paper does not prove that:

$$
\mathfrak F_k(N)
$$

has a uniform extinction depth for all $N$.

It does not prove a closed asymptotic upper bound for:

$$
K(N)
$$

It does not exclude integer-anchored infinite hard branches.

It does not convert:

$$
P_k\to1
$$

or survivor density $\to0$ into emptiness.

It does not infer the infinite domain just because finite verification has reached $2^{71}$.

Therefore, this paper is not a Collatz proof.

---

# 63. Final Conclusion of the Series

After nine papers, it can be stated very precisely:

### Completed

$$
\boxed{
\text{finite-word arithmetic}
}
$$

Allows exact affine compression.

$$
\boxed{
\text{finite itinerary legality}
}
$$

Allows exact residue coding.

$$
\boxed{
\text{fixed-chart dynamics}
}
$$

Allows identity trivialization.

$$
\boxed{
\text{forward / inverse local transport}
}
$$

Allows exact recovery.

$$
\boxed{
\text{finite contraction}
}
$$

Has an exact threshold.

$$
\boxed{
\text{finite range verification}
}
$$

Can be rewritten as certificate coverage / frontier extinction.

### Not Yet Completed

$$
\boxed{
\text{all ordinary positive-integer itineraries}
}
$$

Whether they all obtain a descent / merge / terminal certificate in finite time.

---

# 64. The Final Capstone Sentence

The final core sentence of this series is:

$$
\boxed{
\textbf{Collatz dynamics is locally affine-trivializable,
finitely certificate-compressible,
but globally itinerary-unresolved.}
}
$$

English:

> **Collatz dynamics can be exactly affinized and even locally trivialized within finite valid decision domains; any finite verification domain can be compressed into a machine-checkable certificate coverage problem; but the global conjecture still requires excluding all infinite non-descending itineraries anchored by ordinary positive integers.**

Therefore, what remains truly unsolved is not:

$$
\boxed{
\text{how to compute one finite Collatz block}.
}
$$

but rather:

$$
\boxed{
\text{whether every positive-integer anchored itinerary eventually leaves the hard frontier}.
}
$$

With this, the series is capped.

---

# References

1. Vigleik Angeltveit, *An improved algorithm for checking the Collatz conjecture for all $n<2^N$*, arXiv:2602.10466 (2026).
2. David Barina, *Improved verification limit for the convergence of the Collatz conjecture*, The Journal of Supercomputing 81, 810 (2025).
3. David Barina, *Convergence verification of the Collatz problem*, The Journal of Supercomputing 77 (2021).
4. Terence Tao, *Almost all orbits of the Collatz map attain almost bounded values*, Forum of Mathematics, Pi 10 (2022), arXiv:1909.03562.
5. Olivier Rozier, Claude Terracol, *Paradoxical behavior in Collatz sequences*, arXiv:2502.00948.
6. Tong Niu, *Parity vectors and paradoxical sequences in the accelerated Collatz map*, arXiv:2605.13886.
7. Mike Winkler, *Deterministic Structures in the Stopping Time Dynamics of the $3x+1$ Problem* (2026 preprint).
8. Collatz Operation Translation Series — Papers 01–08.
9. Operation Translation Series A — Papers 01–07.

---

# Series Capstone Declaration

**Collatz Operation Translation Series — Papers 01–09: Completed.**

If research continues in the future, a new series should be established, rather than expanding this series indefinitely.

Directions that can be extended but are not included in this series include:

- hard-frontier asymptotics;
- certificate minimization complexity;
- formal proof assistant verification;
- accelerated valuation-code frontier;
- generalized $mx+r$ certificate phase diagrams;
- RCOT in noncommutative/state-machine systems.

All of the above belong to a new series, not unfinished chapters of this paper.