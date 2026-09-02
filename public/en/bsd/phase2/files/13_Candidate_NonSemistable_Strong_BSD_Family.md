# 13 | Candidate Non-Semistable Strong-BSD Family Schema v0.2

**Status: Research candidate; no formal new theorem claimed yet.**

Let $E/\mathbf Q$ be an optimal, analytic-rank-$0$ elliptic curve, not necessarily semistable.

Goal: Find a finitely verifiable base certificate such that a Banwait-style infinite twist family
$\mathcal D(E)$ satisfies:

$$
\forall d\in\mathcal D(E),\quad
\operatorname{BSD}(E_d).
$$

## B0 — 2-part anchor

- Banwait–Huang Theorem 2.14 branch;
- $\operatorname{BSD}(E,2)$;
- twist local/splitting conditions;
- Recommended $c_E=1$.

## B1 — ordinary ramification reservoir

Let

$$
W_{\rm mult}^{odd}(E)=
\{q\text{ odd}:q\parallel N_E\}.
$$

Require it to be non-empty and:

$$
g_{\rm mult}^{odd}(E)
=
\gcd_{q\in W_{\rm mult}^{odd}(E)}
v_q(\Delta_{\min})
$$

be a power of $2$.

## B2 — FW nonsplit reservoir

$$
W_-(E)\ne\varnothing,
$$

and:

$$
g_-(E)
=
\gcd_{q\in W_-(E)}
v_q(\Delta_{\min})
$$

is a power of $2$.

## B3 — fixed additive odd primes

Exactly verify one by one:

```text
FW-H1
FW-H2
period / Manin
```

H3 is provided by B2.

## B4 — fixed multiplicative odd primes

Finitely check the corresponding multiplicative theorem hypotheses and distinct ramified witnesses one by one.

## B5 — twist support

Requirements for primes $p\mid d$:

- Avoid 3;
- Good ordinary;
- Avoid finite residual-reducibility/image exceptions;
- Maintain the splitting / inertness conditions required by Theorem 2.14.

## Pending obligations

1. Exact H1 backend for fixed additive primes;
2. Exact H2 local residual backend for fixed additive primes;
3. Formal theorem table for the fixed multiplicative branch;
4. Manin-period compatibility;
5. Chebotarev / CRT simultaneous compatibility for all support restrictions;
6. Final all-prime cover proof.

Until these six items are completed, this will not be upgraded to a theorem.