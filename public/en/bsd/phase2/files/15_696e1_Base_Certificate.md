# 15｜696.e1 Base Certificate

## Curve

$$
E:\ y^2=x^3+x^2+8x-16.
$$

$$
N=696=2^3\cdot3\cdot29.
$$

$$
\Delta_{\min}=-2^{11}\cdot3\cdot29<0.
$$

$$
E(\mathbb Q)_{\rm tors}=0.
$$

analytic / algebraic rank:

$$
0.
$$

optimal, Manin constant:

$$
1.
$$

---

# Base BSD(E,2)

Recall from the introduction of Banwait–Huang:

> full BSD has been verified for analytic rank $0/1$ elliptic curves up to conductor $5000$.

Therefore, for this curve:

$$
696<5000,\qquad r_{\rm an}=0
$$

we have:

$$
\boxed{\operatorname{BSD}(E)}
$$

already rigorously verified.

In particular:

$$
\boxed{\operatorname{BSD}(E,2)}.
$$

Here we do not use:

```text
analytic Sha = 1 => actual Sha = 1
```

which would be a circular inference.

---

# Lalg gate

LMFDB:

$$
\Sha_{\rm an}=1,
\qquad
\prod c_p=1,
\qquad
|E(\mathbb Q)_{\rm tors}|=1,
\qquad
Reg=1.
$$

By the definition of analytic Sha:

$$
\frac{L(E,1)}{\Omega_E}=1.
$$

Therefore:

$$
\boxed{
v_2(L^{alg}(E,1))=0.
}
$$

---

# 2-division cubic

Since $a_1=a_3=0$:

$$
f_2(x)
=
x^3+x^2+8x-16.
$$

It has no rational roots, and is therefore irreducible over $\mathbb Q$.

Its discriminant is:

$$
\operatorname{disc}(f_2)
=
-11136
=
-2^7\cdot3\cdot29.
$$

It is not a square.

Thus, the Galois closure is:

$$
S_3.
$$

quadratic resolvent:

$$
\mathbb Q(\sqrt{-174}).
$$