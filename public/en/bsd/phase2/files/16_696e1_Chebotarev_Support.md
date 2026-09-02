# 16｜696.e1 Chebotarev Support Family

## Prime family

Definition:

$$
\mathcal P
=
\left\{
q\text{ prime}:
q\equiv1\pmod{24},
\left(\frac q{29}\right)=1,
f_2\bmod q\text{ irreducible}
\right\}.
$$

---

# Why the splitting conditions work

If:

$$
q\equiv1\pmod{24},
$$

then:

$$
q\equiv1\pmod8,
\qquad
q\equiv1\pmod3.
$$

Therefore, in:

$$
\mathbb Q(\sqrt q)
$$

we have:

- $2$ splits;
- $3$ splits.

Furthermore, with:

$$
\left(\frac q{29}\right)=1,
$$

we get that $29$ splits.

Thus, all primes dividing the conductor:

$$
2,3,29
$$

split.

---

# Chebotarev compatibility

Let $L$ be the Galois closure of $f_2$.

$$
\mathrm{Gal}(L/\mathbb Q)=S_3.
$$

The quadratic resolvent is:

$$
F_0=\mathbb Q(\sqrt{-174}).
$$

Let:

$$
K=\mathbb Q(\zeta_{24},\sqrt{29}).
$$

$K$ is abelian, and the only nontrivial normal abelian subfield of the $S_3$ extension is $F_0$.

Moreover:

$$
\sqrt{-174}=\sqrt{-6}\sqrt{29},
$$

and:

$$
\mathbb Q(\sqrt{-6})\subset\mathbb Q(\zeta_{24}).
$$

Therefore:

$$
L\cap K=F_0.
$$

Thus:

$$
[LK:\mathbb Q]=48.
$$

Take:

$$
(\sigma,1),
$$

where $\sigma$ is a 3-cycle in $S_3$.

The 3-cycle is trivial on $F_0$, so this is a valid element in the fiber-product Galois group.

The size of its conjugacy class is:

$$
2.
$$

Hence, the Chebotarev density is:

$$
\boxed{
\frac2{48}=\frac1{24}.
}
$$

---

# Automatic ordinary

$q$ is inert in the cubic field:

$$
\Longleftrightarrow
\mathrm{Frob}_q
\text{ is an order-3 element in }GL_2(\mathbb F_2)\simeq S_3.
$$

The characteristic polynomial of an order-3 element is:

$$
X^2+X+1,
$$

so its trace is:

$$
1\pmod2.
$$

Thus:

$$
a_q(E)\equiv1\pmod2.
$$

That is, $a_q$ is odd.

For $q\ge5$, if it is supersingular:

$$
q\mid a_q
$$

combined with the Hasse bound, this would force:

$$
a_q=0,
$$

which is a contradiction.

Therefore:

$$
\boxed{
q\in\mathcal P\Rightarrow q\text{ good ordinary for }E.
}
$$

---

# First explicit prime

$$
q=241.
$$

Check:

$$
241\equiv1\pmod{24},
$$

$$
241\bmod29=9
$$

which is a quadratic residue,

$f_2 \bmod 241$ has no roots, hence it is irreducible.

By direct point counting:

$$
a_{241}(E)=-7.
$$

So the first explicit twist parameter can be chosen as:

$$
\boxed{d=241}.
$$