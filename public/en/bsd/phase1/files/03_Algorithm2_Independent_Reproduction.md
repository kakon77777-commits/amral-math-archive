# 03 | Algorithm 2 Independent Reproduction

## 0. Purpose

Establish a mirror that relies only on the Python standard library to replay:

- squarefree;
- gcd;
- $a_p$;
- finite-field point count;
- $2$-adic valuation;
- quadratic splitting;
- cubic 2-division inertness;
- sign condition.

It does not implement the descent / isogeny / optimality / L-value parts of Algorithm 1.

---

# 1. Finite-field point count

For a general Weierstrass equation:

$$
y^2+a_1xy+a_3y
=
x^3+a_2x^2+a_4x+a_6,
$$

after fixing $x\in\mathbb F_p$, it is viewed as a quadratic equation in $y$.

For odd $p$, its discriminant is:

$$
D_x
=
(a_1x+a_3)^2
+
4(x^3+a_2x^2+a_4x+a_6).
$$

Therefore:

$$
\#\{y\}
=
1+\chi_p(D_x).
$$

Adding the point at infinity yields:

$$
\#E(\mathbb F_p).
$$

---

# 2. Ordinary test

$$
a_p(E)
=
p+1-\#E(\mathbb F_p).
$$

The program checks:

$$
p\nmid a_p(E).
$$

---

# 3. CLZ branch

For:

$$
46a1,
$$

the program obtains the exact same seven twists as the official implementation:

$$
1,185,265,305,745,785,905.
$$

---

# 4. Zhai branch

The $x$-coordinates of the $2$-torsion satisfy the cubic:

$$
4x^3+b_2x^2+2b_4x+b_6=0,
$$

where:

$$
b_2=a_1^2+4a_2,
$$

$$
b_4=2a_4+a_1a_3,
$$

$$
b_6=a_3^2+4a_6.
$$

Excluding the ramified primes ruled out by the theorem, a degree-$3$ polynomial modulo $p$ having no roots is equivalent to being irreducible, and thus corresponds to an inert prime.

For:

$$
106d1,
$$

it obtains the exact same $21$ twists as the official implementation.

---

# 5. Limitations

The inertness determination of this mirror uses cubic reduction modulo $p$.

In general number-field computations, a formal certificate should use:

```text
factorization of p O_F
```

or in Sage:

```python
F.ideal(p).is_prime()
```

In this test, by the theorem's condition:

$$
(d,3N)=1
$$

the relevant ramified bad primes are excluded, and the results are completely consistent with the official fixture.

However, full production should still rely on the Sage number-field backend as the authority.

---

# 6. Reproduction results

```text
46a1:
expected 7
actual   7
exact list match: PASS

106d1:
expected 21
actual   21
exact list match: PASS
```

Therefore:

$$
\boxed{
\text{The Algorithm 2 branch logic can be independently replayed.}
}
$$