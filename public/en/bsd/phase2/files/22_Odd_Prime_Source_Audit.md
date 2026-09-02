# 22 | Odd Prime Source Audit

Let $d=q$ be the support prime.

## A. $p=q$: additive twist

Banwait–Huang Proposition 2.9 Item 1 directly reduces this case to BSTW Theorem 9.21(c).

The proof lists:

- $p\ge5$;
- $p\nmid6N$;
- $p$ is good ordinary for the base $E$;
- $\bar\rho_{E,p}$ is irreducible;
- `(ramK)`: there exists $\ell\parallel N$, $\ell\nmid D_K$, residually ramified.

For `696.e1`:

- $q\equiv1\pmod{24}$;
- $q\neq29$;
- support inertness implies ordinary;
- the base mod-$q$ image is maximal, hence absolutely/ordinarily residually irreducible;
- take $\ell=29$;
- $v_{29}(\Delta)=1$, so $q\nmid1$;
- $29\nmid D_K=q$.

Therefore, PASS.

Banwait Remark 2.10 explicitly states that semistability in Item 1 is only used to automatically generate a ramified witness;
in the non-semistable case, one can simply treat the witness as a hypothesis.

---

## B. good ordinary $p$

Directly apply Skinner Theorem C:

- $p\ge3$;
- good ordinary;
- $E_q[p]$ is irreducible;
- there exists another multiplicative $\ell$ that is residually ramified;
- $L(E_q,1)\ne0$.

Take:

$$
\ell=29.
$$

The good ordinary $p$ is not equal to $29$, and $p\nmid v_{29}(\Delta)=1$.

PASS.

---

## C. multiplicative $p=3$

Skinner Theorem C **explicitly states $p\ge3$**.

Take the witness:

$$
\ell=29.
$$

PASS.

---

## D. multiplicative $p=29$

Take the witness:

$$
\ell=3.
$$

Because:

$$
v_3(\Delta)=1.
$$

PASS.

---

# Important simplification

Since the base curve mod-$\ell$ image is maximal for all $\ell$,
the quadratic twist only tensors by a scalar character, hence irreducibility is preserved.

Therefore, the ordinary branch no longer needs to be split into reducible/irreducible subcases.