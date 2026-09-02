# 14 | Candidate Sieve: Why did 696.e1 emerge?

## Cheap gates first

In this round, we switch to:

```text
rank/optimal/Manin
→ 2-part Lalg valuation
→ base BSD(E,2)
→ odd multiplicative reservoirs
→ fixed additive primes
→ residual images
→ only then local Iwasawa/FW
```

instead of first performing expensive local Galois analysis on every curve.

---

# 696.e1

$$
E=[0,1,0,8,-16].
$$

### Base

- rank $0$;
- torsion trivial;
- optimal;
- Manin $1$;
- conductor $696<5000$;
- $\Sha_{\rm an}=1$;
- Tamagawa product $1$.

Therefore:

$$
L^{alg}(E,1)=1,
\qquad
v_2(L^{alg})=0.
$$

It falls exactly into the Theorem 2.14:

```text
no rational 2-torsion
negative discriminant
```

branch.

### Odd local structure

```text
2  additive II*                 vDelta=11
3  split multiplicative I1     vDelta=1
29 nonsplit multiplicative I1  vDelta=1
```

Thus:

$$
W_{\rm mult}^{odd}=\{3,29\},
$$

$$
W_-=\{29\}.
$$

And all relevant gcds are $1$.

### Residual images

LMFDB records maximal image for all primes.

Therefore:

- support prime residual irreducibility;
- fixed multiplicative residual irreducibility;
- no rational isogeny;
- twist irreducibility preservation;

All are extremely clean.

---

# Control: 116.b1

`116.b1` similarly has:

- rank $0$;
- a beautiful cheap 2-part anchor;
- nonsplit multiplicative $29$.

But its odd bad structure only has:

```text
2 additive
29 nonsplit multiplicative
```

So when the fixed multiplicative is:

$$
p=29
$$

there is no other:

$$
q\neq29,\quad q\parallel N
$$

to act as a residual-ramification witness.

Therefore, it is currently flagged by:

```text
FAIL_FIXED_MULTIPLICATIVE_WITNESS
```

and eliminated.

This shows that the key to `696.e1` is not simply "having a nonsplit prime", but rather:

$$
\boxed{
\text{at least two odd multiplicative reservoirs,
with at least one being nonsplit.}
}
$$