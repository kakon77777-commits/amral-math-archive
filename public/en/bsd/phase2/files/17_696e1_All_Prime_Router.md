# 17｜696.e1 All-Prime Router

Let:

$$
q\in\mathcal P,
\qquad
d=q.
$$

By Theorem 2.14:

$$
L(E_q,1)\neq0
$$

and:

$$
\operatorname{BSD}(E_q,2).
$$

Now we only need odd primes.

---

# Case A — $p=q$

$E$ at $q$ is:

- good;
- ordinary;
- $q\ge5$;
- residually irreducible.

Take the witness:

$$
\ell=29.
$$

Since:

$$
v_{29}(\Delta_E)=1,
$$

we have:

$$
q\nmid v_{29}(\Delta_E),
$$

thus it is residually ramified.

Moreover, $29$ splits in $\mathbb Q(\sqrt q)$, so the local twist at $29$ is trivial.

Therefore, the additive-twist ordinary branch can be applied.

---

# Case B — $p\nmid q$, good ordinary

The quadratic twist preserves residual irreducibility.

When a direct ramified witness is needed:

- If $p=3$: this case does not occur, since $3$ is bad;
- If $p=29$: this case does not occur, since $29$ is bad;
- For other $p$: take $29$.

Since:

$$
p\nmid1=v_{29}(\Delta_E).
$$

the ramified-prime condition holds directly.

---

# Case C — fixed multiplicative primes

There are only:

$$
p=3,\ 29.
$$

### $p=3$

Residually irreducible.

Take:

$$
q_0=29.
$$

### $p=29$

Residually irreducible.

Take:

$$
q_0=3.
$$

Both valuations are:

$$
1.
$$

Thus, residual ramification holds.

---

# Case D — good supersingular

This is the branch where semistability was originally truly stuck.

We use the Fouquet–Wan sufficient theorem interface.

## FW-H1

The good supersingular local representation is irreducible, hence the global residual representation is absolutely irreducible.

## FW-H2

The local residual representation is irreducible, so it cannot semisimplify into the character direct sums prohibited by FW.

## FW-H3

Take:

$$
\ell=29.
$$

$29$ is nonsplit multiplicative, and:

$$
v_{29}(\Delta)=1.
$$

Any good supersingular odd $p$ satisfies:

$$
p\neq29,
\qquad
p\nmid1.
$$

Thus the residual Steinberg extension is ramified, and the nonsplit condition gives a nontrivial unramified quadratic twist.

---

# Period / Manin issue

The FW $p$-part corollary uses the modular period.

For a good supersingular $p$, $p$ is a good reduction prime, therefore:

$$
p\nmid N_{E_q}.
$$

The Manin constant has no $p$-adic contribution at such primes (we can use known results on the support of the Manin constant).

Additionally, all mod-$\ell$ images of the base curve are maximal; the twist preserves odd-$\ell$ irreducibility, and the $2$-torsion field remains unchanged, so $E_q$ has no rational prime-degree isogeny.

This keeps the optimal/isogeny transfer issue clean.

---

# Exhaustion

For $E_q$, an odd $p$ can only be:

1. $p=q$ additive;
2. good ordinary;
3. multiplicative $3/29$;
4. good supersingular.

All four classes are covered.

Therefore, the prime router has no missing branches.