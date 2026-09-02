# 07 | BSD Certificate Globalizer

## 0. Purpose

Establish a research control quantity that does not obscure a single uncertified curve simply because "most curves are already certified".

Note: It is faithful to the **certification status**, not directly faithful to the BSD truth value.

---

# 1. Canonical enumeration

Establish a computable enumeration:

$$
\mathcal E
=
\{E_1,E_2,\ldots\}
$$

using conductor, isogeny label, etc.

Each $E_i$ represents a $\mathbb Q$-isogeny class.

---

# 2. Certificate target

Fix a target level:

$$
\ell_\star\in\{C6,C7,C8,C9,C10\}.
$$

After the $k$-th round, let:

$$
H_k(\ell_\star)
=
\left\{
i:
\ell_k(E_i)<\ell_\star
\right\}.
$$

If the research only adds certificates without revoking valid ones:

$$
H_{k+1}\subseteq H_k.
$$

---

# 3. Faithful unresolved mass

Take:

$$
s>1.
$$

Define:

$$
\boxed{
\mathfrak B_k(s;\ell_\star)
=
\sum_{i\in H_k(\ell_\star)}
i^{-s}.
}
$$

Any fixed uncertified class leaves a positive mass.

Therefore:

$$
\mathfrak B_k=0
\iff
H_k=\varnothing
$$

holds in a finite benchmark.

For an infinite enumeration, if the certificate system is monotone, then:

$$
\lim_{k\to\infty}\mathfrak B_k=0
$$

which means every fixed class eventually leaves the unresolved frontier.

---

# 4. It is not a proof of BSD

Even if:

$$
\mathfrak B_k\to0,
$$

it only means that:

> The adopted certificate system covers the enumeration domain pointwise.

To deduce BSD, one also needs:

1. Every certificate is sound;
2. The target claim is indeed equivalent to the BSD component;
3. The enumeration covers all $E/\mathbb Q$;
4. Certificate generation does not use BSD as an oracle;
5. A finite stage is genuinely reached for all curves.

Therefore:

$$
\boxed{
\text{Certificate Globalizer}
\neq
\text{Truth Oracle}.
}
$$

---

# 5. Practical applications

It can compare:

- Which Agent route reduces more unresolved mass per round;
- Whether high conductor curves are permanently forgotten;
- Whether rank $2+$ forms a non-decreasing tail;
- Whether a theorem only handles high-density subfamilies or covers them pointwise;
- Whether the proof backlog is merely transferred to another component.

---

# 6. Multidimensional version

One can separately define:

$$
\mathfrak B^{W}_k
$$

the weak BSD backlog,

$$
\mathfrak B^{F}_k
$$

the $\Sha$ finiteness backlog,

$$
\mathfrak B^{S}_k
$$

and the strong formula backlog.

This avoids a single total score masking the situation where:

$$
\text{rank is proven, but }\Sha\text{ is not closed}.
$$