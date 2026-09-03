工程紀錄 · 第五弧線 v3.15 · 2026-09-03 · PRIME_SHELL_TAIL · AXIS_FREE_FIXED_POWER · FULL_DETERMINISTIC_MODEL_CLOSED · RH_CLAIM_FALSE

# Axis-Free Mixed Ramanujan Tail：Prime-Set Shell、$Q=N^{1/2}$ Balance 與 Deterministic Model Fixed-Power Closure

**RH-AxisFree-MixedRamanujanTail v3.15**

本節點承接：

- `RH-Parallelogram-ConstraintAdaptedPairing v3.13`
- `RH-PairSquareAxis-RamanujanTail v3.14`
- `RH-Parallelogram-SobolevTailTransfer v3.10`

v3.14 closed the one-dimensional axis：

$$
\boxed{
\mathfrak M_{\rm axis}(N)
\ll_\varepsilon
N^{17/4+\varepsilon}.
}
$$

Thus the remaining deterministic model is the genuinely two-dimensional axis-free covariance：

$$
\boxed{
\mathfrak K_4^\perp(h,d).
}
$$

v3.15 proves a fixed-power bound for this remaining deterministic component。

The key is to stop demanding a single closed-form two-dimensional Ramanujan coefficient and instead use the natural **prime-set shell expansion** of the finite Euler approximants。

---

## Main result

For every：

$$
\varepsilon>0,
$$

the axis-free deterministic parallelogram contribution satisfies：

$$
\boxed{
\mathfrak M_{\perp,N}
\ll_\varepsilon
N^{9/2+\varepsilon}.
}
$$

Therefore the full deterministic four-point model satisfies：

$$
\boxed{
\mathfrak M_{4,N}
\ll_\varepsilon
N^{9/2+\varepsilon}.
}
$$

because the previously closed one-dimensional axis has exponent：

$$
\frac{17}{4}
<
\frac92.
$$

Relative to the original：

$$
N^5
$$

quartic barrier：

$$
\boxed{
\eta_M
=
\frac12.
}
$$

This is the first completed **full deterministic fixed-power saving** in the fifth arc。

It is not yet a zero-strip result because the actual-prime deviation：

$$
\mathfrak E_{4,N}
$$

remains open。

---

# 0. Claim register

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE

AXIS_FIXED_POWER = CLOSED_FROM_V3_14
AXIS_EXPONENT = 17/4 + epsilon

FINITE_Q_MIXED_SOBOLEV = q^(o(1))
PRIME_SET_SHELL_DECOMPOSITION = CLOSED

SHELL_AXES_ZERO = CLOSED
SHELL_MIXED_ANTIDERIVATIVE = CLOSED
SHELL_SOBOLEV_NORM = q^(o(1))

LOW_PRIME_SHELL_RESTRICTION = CLOSED
HIGH_PRIME_SHELL_POINTWISE_TAIL = CLOSED

CANONICAL_SPLIT_Q = N^(1/2)
AXIS_FREE_EXPONENT = 9/2 + epsilon
AXIS_FREE_SAVING = 1/2

FULL_DETERMINISTIC_EXPONENT = 9/2 + epsilon
FULL_DETERMINISTIC_ETA_M = 1/2

ACTUAL_PRIME_DEVIATION = OPEN
COMPLETE_QUARTIC_ETA_Q_POSITIVE = NOT_PROVED

GLOBAL_RH_CERTIFICATE = FALSE
```

---

# 1. Finite-prime cumulative model

For a finite set of primes：

$$
P,
$$

let：

$$
q_P
=
\prod_{p\in P}p.
$$

Let：

$$
\boxed{
\mathfrak K_{4,q_P}^{\perp}(h,d)
}
$$

denote the v3.13 double-centered finite Euler-product covariance。

For every squarefree：

$$
r,
$$

write：

$$
\boxed{
\mathfrak K_r^\perp
}
$$

for the corresponding cumulative model using exactly the primes dividing：

$$
r.
$$

Set：

$$
\mathfrak K_1^\perp=0.
$$

---

# 2. Exact prime-set shell

Define the subset Möbius difference：

## Definition 2.1

$$
\boxed{
\mathfrak D_q^\perp
=
\sum_{r\mid q}
\mu(q/r)
\mathfrak K_r^\perp,
}
$$

for squarefree：

$$
q>1.
$$

Then Boolean-lattice Möbius inversion gives：

$$
\boxed{
\mathfrak K_q^\perp
=
\sum_{r\mid q}
\mathfrak D_r^\perp.
}
$$

For nested finite prime sets, the full axis-free model is the prime-set shell limit：

$$
\boxed{
\mathfrak K_4^\perp
=
\sum_{\substack{
q\ge2\\
q\ {\rm squarefree}
}}
\mathfrak D_q^\perp,
}
$$

with the convergence interpreted first through finite Euler products and then pointwise / in the previously established almost-periodic sense。

---

# 3. Shell spectral support

Every finite cumulative：

$$
\mathfrak K_r^\perp
$$

is：

$$
r
$$

-periodic in both variables。

Therefore all of its rational Fourier frequencies have reduced denominators dividing：

$$
r.
$$

Hence the shell：

$$
\mathfrak D_q^\perp
$$

also has every coordinate denominator dividing：

$$
q.
$$

Thus：

## Lemma 3.1

The low prime-shell sum：

$$
\boxed{
\mathfrak K_{\le Q}^{\perp}
=
\sum_{\substack{
q\le Q\\
q\ {\rm squarefree}
}}
\mathfrak D_q^\perp
}
$$

has rational Fourier support inside：

$$
\boxed{
\mathcal F_Q
\times
\mathcal F_Q,
}
$$

where：

$$
\mathcal F_Q
$$

is the Farey set of reduced denominators at most：

$$
Q.
$$

---

# 4. Shell axes remain zero

v3.12–v3.13 prove for every cumulative finite conductor：

$$
\widehat{
\mathfrak K_r^\perp
}(\alpha,0)=0,
$$

and：

$$
\widehat{
\mathfrak K_r^\perp
}(0,\beta)=0.
$$

The shell is a linear combination of these cumulative models。

Therefore：

## Lemma 4.1

$$
\boxed{
\widehat{
\mathfrak D_q^\perp
}(\alpha,0)=0,
}
$$

and：

$$
\boxed{
\widehat{
\mathfrak D_q^\perp
}(0,\beta)=0.
}
$$

So every shell has a two-direction periodic antiderivative。

---

# 5. Shell mixed antiderivative

Let：

$$
\mathfrak G_r^{(2)}
$$

be the v3.13 mixed antiderivative of：

$$
\mathfrak K_r^\perp.
$$

Define：

$$
\boxed{
\mathfrak G_q^{\rm sh}
=
\sum_{r\mid q}
\mu(q/r)
\mathfrak G_r^{(2)}.
}
$$

Then：

$$
\boxed{
\Delta_h\Delta_d
\mathfrak G_q^{\rm sh}
=
\mathfrak D_q^\perp.
}
$$

---

# 6. Shell Sobolev norm

v3.13 gives, for every：

$$
\varepsilon>0,
$$

$$
\boxed{
\|
\mathfrak G_r^{(2)}
\|_{B^2}
\ll_\varepsilon
r^\varepsilon.
}
$$

Therefore：

$$
\begin{aligned}
\|
\mathfrak G_q^{\rm sh}
\|_{B^2}
&\le
\sum_{r\mid q}
\|
\mathfrak G_r^{(2)}
\|_{B^2}
\\
&\ll_\varepsilon
\tau(q)q^\varepsilon
\\
&\ll_\varepsilon
q^{2\varepsilon}.
\end{aligned}
$$

Renaming：

$$
2\varepsilon\mapsto\varepsilon
$$

gives：

## Theorem 6.1

$$
\boxed{
\|
\mathfrak G_q^{\rm sh}
\|_{B^2}
\ll_\varepsilon
q^\varepsilon.
}
$$

---

# 7. Low-shell coefficient norm

Let：

$$
\mathfrak G_{\le Q}
=
\sum_{\substack{
q\le Q\\
q\ {\rm squarefree}
}}
\mathfrak G_q^{\rm sh}.
$$

Using only the triangle inequality：

$$
\begin{aligned}
\|
\mathfrak G_{\le Q}
\|_{\ell^2(\widehat{\ }) }
&\le
\sum_{q\le Q}
\|
\mathfrak G_q^{\rm sh}
\|_{\ell^2(\widehat{\ })}
\\
&\ll_\varepsilon
\sum_{q\le Q}
q^\varepsilon.
\end{aligned}
$$

Therefore：

## Theorem 7.1

$$
\boxed{
\|
\mathfrak G_{\le Q}
\|_{\ell^2(\widehat{\ })}
\ll_\varepsilon
Q^{1+\varepsilon}.
}
$$

No orthogonality between different shells is assumed。

This is deliberately conservative。

---

# 8. Two-dimensional low-shell large sieve

The differentiated exact Cesàro weight is：

$$
\boxed{
F_N(h,d)
=
\Delta_h^-
\Delta_d^-
\Omega_N(h,d).
}
$$

v3.13 gives：

$$
\boxed{
\|F_N\|_2
\ll
N^3.
}
$$

The product Farey large sieve from v3.10 gives：

$$
\boxed{
\sum_{\alpha,\beta\in\mathcal F_Q}
|
\widehat F_N(\alpha,\beta)
|^2
\ll
(N+Q^2)^2
N^6.
}
$$

---

# 9. Low-shell weighted contribution

Double summation by parts gives：

$$
\boxed{
\mathfrak M_{\perp,\le Q}(N)
=
\sum_{h,d}
F_N(h,d)
\mathfrak G_{\le Q}(h,d).
}
$$

Equivalently in frequency space。

By Cauchy–Schwarz, Sections 7–8：

## Theorem 9.1 · Low Prime-Shell Bound

$$
\boxed{
|
\mathfrak M_{\perp,\le Q}(N)
|
\ll_\varepsilon
N^3
(N+Q^2)
Q^{1+\varepsilon}.
}
$$

---

# 10. Euler-product components of $\mathfrak K_4^\perp$

The physical function：

$$
\mathfrak K_4^\perp
$$

is a finite linear combination of：

- ordinary Hardy–Littlewood singular series for subsets of：
  $$
  \{0,h,d,h+d\};
  $$
- squared pair singular series in：
  $$
  h
  $$
  and：
  $$
  d;
  $$
- constants。

Every nonconstant component has an Euler product：

$$
\boxed{
\mathcal F(h,d)
=
\prod_p
L_p(h,d).
}
$$

Write：

$$
\boxed{
L_p=1+\delta_p.
}
$$

---

# 11. Local discriminant

For each component there is a fixed nonzero polynomial product of pair differences：

$$
\boxed{
\Delta(h,d)
}
$$

built from a subset of：

$$
h,
\quad
d,
\quad
h+d,
\quad
h-d.
$$

On the v3.6 **genuine four-distinct region**：

$$
|h|,|d|\ll N,
\qquad
h\ne d,
$$

the relevant collision discriminants are nonzero and satisfy：

$$
\boxed{
0<
|\Delta(h,d)|
\ll
N^{C}
}
$$

for an absolute component-dependent：

$$
C.
$$

The excluded lower-dimensional collision line：

$$
h=d
$$

is **not** included in the pointwise Euler-shell tail estimate below；it remains covered by the v3.6：

$$
N^{4+o(1)}
$$

lower-dimensional bound。

If：

$$
p\nmid\Delta(h,d),
$$

all relevant local shifts are distinct modulo：

$$
p.
$$

Then：

$$
\boxed{
\delta_p(h,d)
=
O(p^{-2}).
}
$$

If：

$$
p\mid\Delta(h,d),
$$

then：

$$
\boxed{
\delta_p(h,d)
=
O(p^{-1}).
}
$$

Small primes are absorbed into the implied constant。

---

# 12. Prime-set Euler shell bound

For squarefree：

$$
q,
$$

the exact Euler shell of one component is：

$$
\boxed{
\delta_q(h,d)
=
\prod_{p\mid q}
\delta_p(h,d).
}
$$

Section 11 gives：

$$
\boxed{
|
\delta_q(h,d)
|
\le
C^{\omega(q)}
\frac{
\gcd(
q,\operatorname{rad}\Delta(h,d)
)
}{
q^2
}.
}
$$

---

# 13. High-shell divisor summation

Use：

$$
\gcd(q,D)
=
\sum_{a\mid(q,D)}
\phi(a).
$$

For every fixed：

$$
\varepsilon>0,
$$

$$
C^{\omega(q)}
\ll_\varepsilon
q^\varepsilon.
$$

Therefore：

$$
\begin{aligned}
\sum_{q>Q}
|
\delta_q(h,d)
|
&\ll_\varepsilon
\sum_{a\mid\operatorname{rad}\Delta}
\phi(a)
\sum_{\substack{
q>Q\\
a\mid q
}}
q^{-2+\varepsilon}
\\
&\ll_\varepsilon
Q^{-1+\varepsilon}
\sum_{a\mid\operatorname{rad}\Delta}
a^\varepsilon.
\end{aligned}
$$

The divisor sum is：

$$
N^\varepsilon
$$

uniformly on：

$$
|h|,|d|\ll N.
$$

Thus：

## Theorem 13.1 · Pointwise Euler-Shell Tail

For every component：

$$
\boxed{
\sum_{q>Q}
|
\delta_q(h,d)
|
\ll_\varepsilon
N^\varepsilon
Q^{-1+\varepsilon}.
}
$$

Since：

$$
\mathfrak K_4^\perp
$$

contains only finitely many such components：

## Corollary 13.2

On the genuine four-distinct region：

$$
h\ne d,
$$

$$
\boxed{
|
\mathfrak K_{\perp,>Q}(h,d)
|
\ll_\varepsilon
N^\varepsilon
Q^{-1+\varepsilon}
}
$$

uniformly on the relevant：

$$
O(N)\times O(N)
$$

box。

The deleted collision line contributes only：

$$
N^{4+o(1)}
$$

to the weighted model and is therefore lower order than the final：

$$
N^{9/2+\varepsilon}
$$

bound。

---

# 14. High-shell weighted contribution

The exact Cesàro parallelogram weight satisfies：

$$
\boxed{
\sum_{h,d}
|\Omega_N(h,d)|
\ll
N^5.
}
$$

Therefore Corollary 13.2 gives：

## Theorem 14.1 · High Prime-Shell Bound

$$
\boxed{
|
\mathfrak M_{\perp,>Q}(N)
|
\ll_\varepsilon
N^{5+\varepsilon}
Q^{-1+\varepsilon}.
}
$$

No finite-box rational restriction theorem is required for this high part。

---

# 15. Optimize the prime-shell split

Write：

$$
Q=N^\theta.
$$

The useful regime begins at：

$$
\theta\ge\frac12.
$$

Then：

$$
N+Q^2
\asymp
Q^2.
$$

Theorem 9.1 has exponent：

$$
\boxed{
3+3\theta.
}
$$

Theorem 14.1 has exponent：

$$
\boxed{
5-\theta.
}
$$

Balance：

$$
3+3\theta
=
5-\theta.
$$

Therefore：

$$
\boxed{
\theta=\frac12.
}
$$

The balancing point lies exactly at the Farey critical scale：

$$
\boxed{
Q=N^{1/2}.
}
$$

---

# 16. Full axis-free fixed-power bound

At：

$$
Q=N^{1/2},
$$

Theorem 9.1 gives：

$$
\boxed{
N^{9/2+\varepsilon}.
}
$$

Theorem 14.1 gives the same：

$$
\boxed{
N^{9/2+\varepsilon}.
}
$$

Therefore：

## Theorem 16.1 · Axis-Free Deterministic Closure

$$
\boxed{
\mathfrak M_{\perp,N}
\ll_\varepsilon
N^{9/2+\varepsilon}.
}
$$

Relative to：

$$
N^5,
$$

$$
\boxed{
\eta_\perp
=
\frac12.
}
$$

---

# 17. Combine with the 1D axis

v3.14 gives：

$$
\boxed{
\mathfrak M_{\rm axis}(N)
\ll_\varepsilon
N^{17/4+\varepsilon}.
}
$$

Since：

$$
\frac{17}{4}
=
4.25
<
4.5
=
\frac92,
$$

the axis-free term dominates。

Hence：

## Theorem 17.1 · Full Deterministic Four-Point Model

$$
\boxed{
\mathfrak M_{4,N}
\ll_\varepsilon
N^{9/2+\varepsilon}.
}
$$

Thus：

$$
\boxed{
\eta_M
=
\frac12.
}
$$

The deterministic refined-singular-series covariance has been removed as an：

$$
N^5
$$

barrier。

---

# 18. Why this is a genuine stage closure

The fifth arc decomposition is：

$$
\boxed{
\mathfrak Q_N
=
\mathfrak M_{4,N}
+
\mathfrak E_{4,N}.
}
$$

v3.15 proves：

$$
\boxed{
\mathfrak M_{4,N}
=
O_\varepsilon(
N^{9/2+\varepsilon}
).
}
$$

Therefore any future failure to prove：

$$
\eta_Q>0
$$

cannot be blamed on the deterministic Hardy–Littlewood / refined singular-series model at the trivial：

$$
N^5
$$

scale。

The remaining first-order barrier is：

$$
\boxed{
\mathfrak E_{4,N},
}
$$

the actual prime deviation from the correctly centered four-point model。

---

# 19. What this does not imply

The v3.6 Gate B requires a bound on：

$$
\boxed{
\mathfrak Q_N
}
$$

itself。

Even though：

$$
\mathfrak M_{4,N}
\ll
N^{9/2+\varepsilon},
$$

the actual prime deviation may still be：

$$
N^{5-o(1)}.
$$

Therefore no：

$$
\eta_Q>0
$$

has been proved。

Consequently no new：

$$
\kappa_I>0
$$

or zero strip has been obtained。

---

# 20. Relation to multidimensional Ramanujan expansions

Arithmetic functions of several variables admit absolutely convergent multiple Ramanujan expansions under multivariable Delange/Wintner-type conditions。

Tóth's general theorem provides the appropriate abstract framework and exhibits coefficients controlled by least-common-multiple structure in many multiplicative examples。

The v3.15 proof does not require a single canonical product-Ramanujan basis for：

$$
\mathfrak K_4^\perp.
$$

The prime-set shell expansion is preferable here because the parallelogram function depends on mixed linear forms：

$$
h,
\quad
d,
\quad
h+d,
\quad
h-d.
$$

The shell method retains those arithmetic collision geometries directly。

---

# 21. Why the high-tail estimate survives mixed linear forms

The only information needed from the local geometry is：

```text
generic prime
    local defect O(p^-2)

collision prime dividing a fixed linear discriminant
    local defect O(p^-1)
```

For a finite system of fixed linear forms, the collision discriminant contains only finitely many factors built from their pairwise differences。

Thus the same：

$$
\gcd(q,\Delta)/q^2
$$

shell majorant works uniformly。

This makes the high-shell argument robust under the parallelogram mixed forms。

---

# 22. Conservative nature of the low-shell estimate

The low-shell proof uses only：

$$
\boxed{
\left\|
\sum_{q\le Q}
\mathfrak G_q^{\rm sh}
\right\|_2
\le
\sum_{q\le Q}
\|
\mathfrak G_q^{\rm sh}
\|_2.
}
$$

It assumes **no orthogonality** between different shell conductors。

If future work proves square-sum or quasi-orthogonality across prime-set shells, the factor：

$$
Q
$$

could improve toward：

$$
Q^{1/2}.
$$

That would move the axis-free exponent from：

$$
9/2
$$

toward the heuristic：

$$
13/3.
$$

No such improvement is used in v3.15。

---

# 23. Autonomous progress metric

The deterministic branch is now certified：

```text
eta_axis = 3/4
eta_axis_free = 1/2
eta_M = 1/2
```

The research optimizer should no longer spend its main budget improving：

$$
\mathfrak M_{4,N}
$$

unless doing so materially helps the actual-prime deviation。

The new target is：

$$
\boxed{
\mathfrak E_{4,N}.
}
$$

---

# 24. New actual-prime gate

Define：

## Four-Point Prime Deviation Gate $\operatorname{FPD}(\eta)$

There exists：

$$
\eta>0
$$

such that：

$$
\boxed{
|
\mathfrak E_{4,N}
|
\ll
N^{5-\eta+o(1)}.
}
$$

Then：

$$
\mathfrak Q_N
=
\mathfrak M_{4,N}
+
\mathfrak E_{4,N}
$$

satisfies：

$$
\boxed{
|\mathfrak Q_N|
\ll
N^{5-\min(1/2,\eta)+o(1)}.
}
$$

Hence v3.6 gives：

$$
\boxed{
I(N)
\ll
N^{
3-
\frac12
\min(1/2,\eta)
+o(1)
}.
}
$$

In particular, **any**：

$$
\eta>0
$$

for actual-prime deviation would now imply a genuine fixed zero strip。

---

# 25. Suggested v3.16 direction

Recommended：

`RH-FourPointPrimeDeviation v3.16`

Stop refining the deterministic singular-series model。

Tasks：

1. write：
   $$
   \mathfrak E_{4,N}
   $$
   explicitly in terms of：
   $$
   \Lambda
   $$
   minus the refined four-point model；
2. use the constraint-adapted axis/axis-free split on the **actual prime residual** as well；
3. compare with：
   - Chou–Haag–Huryn–Ledoan pair-error variance；
   - Matomäki–Radziwiłł–Shao–Tao–Teräväinen higher uniformity；
   - dispersion / bilinear decompositions of $\Lambda$；
4. identify whether current theorems give only：
   $$
   N^{5-o(1)}
   $$
   or any true fixed：
   $$
   N^{5-\eta};
   $$
5. derive the first prime-specific lemma sufficient for：
   $$
   \operatorname{FPD}(\eta);
   $$
6. do not revisit deterministic model representations unless the prime deviation proof needs them。

This is the transition from deterministic Hardy–Littlewood geometry to actual-prime arithmetic。

---

# 26. GAP ledger

## CLOSED / REDUCED

### G1. 1D deterministic axis

```text
CLOSED
```

$$
N^{17/4+\varepsilon}.
$$

### G2. Axis-free prime-shell low part

```text
CLOSED
```

### G3. Axis-free prime-shell high tail

```text
CLOSED
```

### G4. Axis-free fixed power

```text
N^{9/2+\varepsilon}
```

### G5. Full deterministic model

```text
N^{9/2+\varepsilon}
```

### G6. Deterministic saving

```text
eta_M = 1/2
```

---

## OPEN

### G7. Actual prime four-point deviation

```text
OPEN
```

### G8. Any：

$$
\eta_{\rm FPD}>0
$$

```text
OPEN
```

### G9. Complete quartic：

$$
\eta_Q>0
$$

```text
OPEN
```

### G10. Mean-square：

$$
\kappa_I>0
$$

```text
OPEN
```

### G11. RH

```text
OPEN
```

---

# 27. Trust boundary

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE

DETERMINISTIC eta_M = 1/2
    = HARDY-LITTLEWOOD MODEL ONLY

ACTUAL PRIME DEVIATION
    = NOT BOUNDED AT FIXED POWER HERE

eta_M > 0
    DOES NOT IMPLY
eta_Q > 0

NO NEW ZERO STRIP YET

GLOBAL_RH_CERTIFICATE = FALSE
```

Forbidden：

$$
\mathfrak M_{4,N}\ll N^{9/2}
\Longrightarrow
\mathfrak Q_N\ll N^{9/2}.
$$

Forbidden：

$$
\eta_M=\frac12
\Longrightarrow
\Theta\le\frac34.
$$

The actual-prime deviation remains additive and may dominate。

Forbidden：

$$
\text{Euler-shell pointwise tail}
\Longrightarrow
\text{same bound for prime deviation}.
$$

The prime deviation is not an Euler product。

---

# 28. One-line status

> v3.15 closes the full deterministic refined-singular-series component at fixed power. The axis-free covariance is expanded by squarefree prime-set shells using Boolean Möbius inversion of the finite Euler approximants. Every shell preserves the double-axis cancellation and hence admits a mixed antiderivative. The v3.13 finite-conductor mixed Sobolev bound gives each shell antiderivative $q^{o(1)}$ norm; summing all shells with prime-set conductor $q\le Q$ by the triangle inequality costs only $Q^{1+o(1)}$. Their rational frequencies lie in the product Farey set of denominator at most $Q$, so the two-dimensional large sieve and double summation by parts bound the low-shell contribution by $N^3(N+Q^2)Q^{1+o(1)}$. For the high shells, the physical deterministic model is a finite linear combination of Euler products. Each local Euler defect is $O(p^{-2})$ at generic primes and $O(p^{-1})$ only when $p$ divides one of finitely many parallelogram collision forms. Consequently an exact squarefree shell is bounded by $C^{\omega(q)}\gcd(q,\operatorname{rad}\Delta)/q^2$, and divisor summation gives the uniform pointwise tail $N^{o(1)}Q^{-1+o(1)}$. Weighted by the exact Cesàro parallelogram kernel, the high contribution is $N^{5+o(1)}Q^{-1}$. Balancing low and high at the Farey threshold $Q=N^{1/2}$ yields the full axis-free bound $N^{9/2+\varepsilon}$. Combining with the v3.14 one-dimensional axis bound $N^{17/4+\varepsilon}$ gives the full deterministic model $\mathfrak M_{4,N}\ll_\varepsilon N^{9/2+\varepsilon}$, a genuine deterministic saving $\eta_M=1/2$. This does not yet imply a zero strip: the remaining and now canonical obstruction is the actual-prime four-point deviation $\mathfrak E_{4,N}$.

---

# 29. References

1. László Tóth, **Ramanujan expansions of arithmetic functions of several variables**, *The Ramanujan Journal* 47 (2018), 589–603.  
   arXiv: https://arxiv.org/abs/1704.02881

2. Vivian Kuperberg, **Sums of singular series along arithmetic progressions and with smooth weights**, *International Journal of Number Theory* 21 (2025), 53–74.  
   arXiv: https://arxiv.org/abs/2301.06095

3. D. A. Goldston, Julian Ziegler Hunts, Timothy Ngotiaoco, **The Tail of the Singular Series for the Prime Pair and Goldbach Problems**, *Functiones et Approximatio Commentarii Mathematici* 56 (2017), 117–141.  
   arXiv: https://arxiv.org/abs/1409.2151

4. AMRAL, **RH-Parallelogram-ConstraintAdaptedPairing v3.13**.

5. AMRAL, **RH-PairSquareAxis-RamanujanTail v3.14**.

---

# 30. Provenance

研究主導：Neo.K

v3.15 prime-set shell expansion、axis-free low/high conductor bounds、Euler discriminant tail、$Q=N^{1/2}$ optimization、full deterministic $\eta_M=1/2$ closure、reference implementation 與 canonical source 整理：ChatGPT / GPT-5.6 Sol

日期：2026-09-03

研究定位：AMRAL 黎曼猜想半自主研究線，第五弧線 deterministic model closure / transition to actual-prime deviation。

本文件是 research source artifact，不是 peer-reviewed publication。

所有 claim 必須依 Claim register、GAP ledger 與 Trust boundary 解讀。
