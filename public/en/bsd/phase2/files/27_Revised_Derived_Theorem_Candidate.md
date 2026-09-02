# 27 | Revised Derived Theorem Candidate

Let:

$$
E:\ y^2=x^3+x^2+8x-16.
$$

Let:

$$
\mathcal P
=
\left\{
q\text{ prime}:
q\equiv1\pmod{24},\
\left(\frac q{29}\right)=1,\
x^3+x^2+8x-16
\text{ irreducible mod }q
\right\}.
$$

Then:

$$
\delta(\mathcal P)=\frac1{24}.
$$

**Derived theorem candidate:**

$$
\boxed{
\forall q\in\mathcal P,\quad
\operatorname{BSD}(E^{(q)})
}
$$

where $E^{(q)}$ denotes the quadratic twist by $q$.

## Proof router

### p=2

Banwait–Huang Theorem 2.14 + Creutz–Miller base full BSD.

### p=q

Quadratic-twist clause of BSTW Theorem 9.21(c) + rank-zero descent,
ramK witness $29$.

### odd good ordinary p

Skinner Theorem C, witness $29$.

### p=3

Skinner Theorem C, witness $29$.

### p=29

Skinner Theorem C, witness $3$.

### odd good supersingular p

Fouquet–Wan Theorem 1.7 + Corollary 1.10, nonsplit Steinberg witness $29$.

Exhaustive over all primes.

## Claim label

Current:

```text
DERIVED THEOREM CANDIDATE
```

If it further passes the novelty/citation referee, it may advance to:

```text
PREPRINT CANDIDATE
```

Whether it can be called a "new theorem" must be determined separately by a novelty audit.