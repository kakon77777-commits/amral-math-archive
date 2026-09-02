# 01 | Theorem 2.18 Condition Graph

## A. Base curve $E/\mathbb Q$

Let the conductor be $N$.

### E1 — Semistable

$$
E\text{ semistable}.
$$

### E2 — Small prime trace

$$
a_3(E)\in\{-2,-1,0,1,2\}.
$$

Equivalent to excluding:

$$
a_3(E)=\pm3.
$$

### E3 — Rational-isogeny exclusion

$$
E\text{ has no rational }p\text{-isogeny},
\qquad
p\in\{3,5,7\}.
$$

### E4 — Ramification at multiplicative primes

For each:

$$
p\mid N,
$$

there exists another multiplicative prime:

$$
q\mid N,\qquad q\ne p,
$$

such that:

$$
E[p]
$$

is ramified at $q$.

For semistable curves, Algorithm 1 in the paper converts this into a minimal discriminant valuation condition.

### E5 — Optimality

$$
E
$$

is the $\Gamma_0(N)$-optimal representative of its isogeny class.

### E6 — Analytic rank zero

$$
\operatorname{ord}_{s=1}L(E,s)=0.
$$

### E7 — 2-part of BSD

$$
\operatorname{BSD}(E,2)
$$

has been unconditionally verified.

---

# B. Branch 8a: No rational 2-torsion

$$
E(\mathbb Q)[2]=0,
$$

$$
\operatorname{ord}_2 L^{(\mathrm{alg})}(E,1)=0.
$$

This branch is handled by Zhai-type results.

---

# C. Branch 8b: Exactly one rational 2-torsion point

$$
E(\mathbb Q)[2]\cong\mathbb Z/2\mathbb Z,
$$

$$
\operatorname{ord}_2 L^{(\mathrm{alg})}(E,1)=-1.
$$

Write:

$$
E:y^2=f(x),
$$

and let the rational 2-torsion point be:

$$
(x_0,0).
$$

Require that:

$$
f'(x_0),\quad -f'(x_0),\quad -\Delta_E
$$

are all non-squares in $\mathbb Q$.

Let:

$$
E'=E/E(\mathbb Q)[2].
$$

Further require that:

$$
\Sha(E')[2]=0,
$$

and simultaneously check in the algorithm in the paper that:

$$
E'(\mathbb Q)[2]\cong\mathbb Z/2\mathbb Z.
$$

---

# D. Common conditions for twist $d$

$$
d\text{ squarefree},
$$

$$
(d,3N)=1,
$$

$$
d\equiv1\pmod4,
$$

and for all:

$$
p\mid d,
$$

$E$ is ordinary at $p$.

For a good prime:

$$
\#E(\mathbb F_p)=p+1-a_p(E),
$$

while the official program uses:

$$
p\nmid a_p(E)
$$

for the ordinary test.

---

# E. Twist conditions for the Zha16 branch

If:

$$
E(\mathbb Q)[2]=0,
$$

then:

1. Every $p\mid d$ is inert in the cubic 2-division field
   $$
   \mathbb Q[x]/(f_2(x))
   $$
2. Every $p\mid N$ splits in
   $$
   \mathbb Q(\sqrt d)
   $$
3. If:
   $$
   \Delta_E>0,
   $$
   then:
   $$
   d>0.
   $$

---

# F. Twist conditions for the CLZ20 branch

If:

$$
E(\mathbb Q)[2]\cong\mathbb Z/2\mathbb Z,
$$

then for every $p\mid d$:

$$
p\equiv1\pmod4,
$$

$$
\operatorname{ord}_2\#E(\mathbb F_p)=1.
$$

and require that:

$$
d\equiv1\pmod8,
$$

and that every odd:

$$
p\mid N
$$

splits in:

$$
\mathbb Q(\sqrt d).
$$

---

# G. Output semantics

Algorithm 2 does not return "all twists satisfying BSD".

It only enumerates a theorem-guaranteed subfamily:

$$
\boxed{
\text{admissible}
\Rightarrow
\text{BSD follows from cited theorems}.
}
$$

The converse does not hold:

$$
\boxed{
\text{not admissible}
\not\Rightarrow
\text{BSD false}.
}
$$