# 19｜Independent Referee / Local Agent Handoff

## Goal

Do not search for more curves.

First attempt to refute:

> `696.e1` family theorem.

---

# Referee A — Theorem 2.14

For:

$$
E=[0,1,0,8,-16]
$$

Verify item by item:

```text
optimal
odd Manin
analytic rank 0
BSD(E,2) rigorous source
E(Q)[2]=0
Delta<0
v2(Lalg)=0
```

Then verify for symbolic $q\in\mathcal P$:

```text
squarefree
gcd(q,696)=1
q mod 4 = 1
2,3,29 split in Q(sqrt(q))
q inert in 2-division cubic
```

Output PASS/FAIL.

---

# Referee B — Odd ordinary/additive branches

Only use the non-semistable replacement explicitly permitted by Banwait–Huang Remark 2.10:

```text
semistability used only to manufacture ramified witness
```

Verify the theorem hypotheses for witness $3$ / $29$ branch by branch.

---

# Referee C — Fouquet–Wan

Preferentially use the stronger but simpler sufficient hypotheses of FW Theorem 1.1, instead of manually rewriting the most general Theorem 1.7.

Verify for arbitrary good supersingular $p$:

```text
absolute irreducibility
local forbidden semisimplifications impossible
ell=29
ell||N(E_q)
dim E_q[p]^I_29 = 1
dim E_q[p]^G_Q29 = 0
```

In particular, check:

```text
nonsplit multiplicative
<=>
FW nontrivial unramified quadratic Steinberg twist
```

---

# Referee D — Period

Prove that for the good supersingular $p$ used by FW:

```text
p does not divide Manin-period discrepancy
```

Preferentially cite published Manin-constant results, and do not rely on the unpublished Edixhoven remark.

---

# Referee E — Chebotarev

Independently recompute:

```text
disc(f2) = -11136
Gal = S3
quadratic resolvent = Q(sqrt(-174))
K = Q(zeta_24, sqrt(29))
L intersect K = Q(sqrt(-174))
[LK:Q] = 48
class size = 2
density = 1/24
```

---

# Referee F — Search for counterexample prime

Write a program to sweep at least:

$$
q<10^7
$$

all $\mathcal P$ primes.

For each:

```text
a_q odd
ordinary
all splitting predicates
f2 irreducible
```

Any mismatch immediately results in FAIL.

The numerical sweep is not a theorem proof, just a search for implementation/case bugs.

---

# Stop rule

If Referees A–E all PASS:

```text
upgrade to DERIVED THEOREM / PREPRINT CANDIDATE
```

If any item FAILs:

```text
freeze scaling
return to exact failed lemma
```