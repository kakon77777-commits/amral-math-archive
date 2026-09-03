工程紀錄 · 第三弧線 v2.6 · 2026-09-03 · CAUSAL_FACTORIZATION · FOUR_STATE_TRANSFER · RH_CLAIM_FALSE

# Cauchy Resolvent 的一階 Causal Factorization 與四維 Transfer State

**RH-CauchyResolvent-CausalStateFactorization v2.6**

本節點承接：

- `RH-CauchyPoisson-TwistScalarization v2.5`

v2.5 把整個 vertical twist family 壓成固定 Cauchy scalar：

$$
\mathscr W_h(T)
=
\int_T^{T+1}
\mathcal C_h(t)\,dt,
$$

其中：

$$
\mathcal C_h(t)
=
\iint
e^{-|u-v|}
\,d\mu_t(u)d\mu_t(v),
$$

而：

$$
d\mu_t(u)
=
T_h(t-u)
\left[
\sum_{q=p^k}
\frac{\Lambda(q)}{\sqrt q}
\delta_{\log q}(du)
-
e^{u/2}du
\right].
$$

v2.5 又把這個 quadratic form寫成二階 resolvent：

$$
(1-\partial_u^2)y_t=\mu_t.
$$

v2.6 利用 exponential Green kernel 的 Markov / semiseparable structure，再降一階。

核心結果：

令：

$$
\boxed{
(\partial_u+1)s_t=\mu_t
}
$$

採用左側 causal boundary：

$$
s_t(-\infty)=0.
$$

則：

$$
\boxed{
\mathcal C_h(t)
=
2
\int_{\mathbb R}
|s_t(u)|^2du.
}
$$

因此二階 Helmholtz Green energy可以精確 factor成一階 causal state energy。

對 local support：

$$
[a,b]
=
[t-h,t+h],
$$

若只積到右端 $b$：

$$
\boxed{
\mathcal C_h(t)
=
E_t(b)+s_t(b)^2,
}
$$

其中：

$$
E_t'(u)=2s_t(u)^2,
\qquad
E_t(a)=0.
$$

prime atoms只讓 $s$ jump；$E$ 本身不 jump。

background segments則有 exact affine-quadratic transfer。

所以整個 local Cauchy energy可由：

$$
\boxed{
X=(1,s,s^2,E)^\top
}
$$

這個固定四維 state，沿 ordered prime log-points依次乘 transfer matrices精確得到。

這將 v2.5 原本看似 quadratic pair problem 的：

$$
O(N^2)
$$

互動，改寫成：

$$
\boxed{
O(N)
}
$$

event sweep，且 state dimension與 active prime數 $N$ 無關。

這是一個真正的 finite-dimensional compression。

它仍然不是 finite-number-of-events global proof。

**RH_CLAIM = False.**

---

# 0. Claim register

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE

CAUCHY_KERNEL_CAUSAL_FACTORIZATION = CLOSED
PREFIX_DISSIPATION_IDENTITY = CLOSED

PRIME_ATOM_SCALAR_JUMP = CLOSED
BACKGROUND_EXACT_SEGMENT_TRANSFER = CLOSED
FOUR_STATE_LINEAR_LIFT = CLOSED

PAIRWISE_QUADRATIC_COST = REDUCED_TO_LINEAR_EVENT_SWEEP
STATE_DIMENSION = 4
EVENT_COUNT = STILL_UNBOUNDED

ACTUAL_LOCAL_PRIME_BACKGROUND_CROSSCHECK = PASSED_REFERENCE_NUMERICS

GLOBAL_POLYNOMIAL_ENERGY_BOUND = OPEN
GLOBAL_RH_CERTIFICATE = FALSE
```

---

# 1. Cauchy quadratic form

Let $\mu$ be a real compactly supported finite signed measure.

Define:

$$
\boxed{
\mathcal C(\mu)
=
\iint
e^{-|u-v|}
\,d\mu(u)d\mu(v).
}
$$

Using the Fourier convention:

$$
\widehat\mu(\tau)
=
\int
e^{-i\tau u}d\mu(u),
$$

the Cauchy identity gives:

$$
\boxed{
\mathcal C(\mu)
=
\int_{\mathbb R}
\frac{
|\widehat\mu(\tau)|^2
}{
\pi(1+\tau^2)
}
d\tau.
}
$$

So $\mathcal C(\mu)\ge0$.

---

# 2. Spectral factorization of the Cauchy weight

Factor:

$$
1+\tau^2
=
(1+i\tau)(1-i\tau).
$$

Define $s$ by:

$$
\boxed{
(\partial_u+1)s=\mu,
}
$$

with causal condition:

$$
s(-\infty)=0.
$$

Then:

$$
\widehat s(\tau)
=
\frac{
\widehat\mu(\tau)
}{
1+i\tau
}.
$$

By Parseval:

$$
\begin{aligned}
2
\int_{\mathbb R}
|s(u)|^2du
&=
\frac1\pi
\int_{\mathbb R}
\frac{
|\widehat\mu(\tau)|^2
}{
1+\tau^2
}
d\tau.
\end{aligned}
$$

Hence:

## Theorem 2.1 · Causal spectral factorization

$$
\boxed{
\mathcal C(\mu)
=
2
\int_{\mathbb R}
|s(u)|^2du.
}
$$

This is the minimum-phase / causal factorization of the Cauchy kernel.

---

# 3. Relation to the v2.5 Helmholtz resolvent

v2.5 used:

$$
(1-\partial_u^2)y=\mu.
$$

Since:

$$
\boxed{
1-\partial_u^2
=
(1-\partial_u)(1+\partial_u),
}
$$

the new causal state is one first-order factor of the Helmholtz operator.

The two energy identities are:

$$
\boxed{
\mathcal C(\mu)
=
2
\|s\|_{L^2}^2
=
2
\left(
\|y\|_{L^2}^2
+
\|y'\|_{L^2}^2
\right).
}
$$

Thus v2.6 is not a new kernel.

It is an exact first-order factorization of the v2.5 kernel.

---

# 4. Causal state as a one-sided convolution

The solution is:

$$
\boxed{
s(u)
=
\int_{(-\infty,u]}
e^{-(u-v)}
\,d\mu(v).
}
$$

So the entire left history enters future propagation through one scalar:

$$
s(u).
$$

For $u_2>u_1$ with no source between them:

$$
\boxed{
s(u_2)
=
e^{-(u_2-u_1)}
s(u_1).
}
$$

This is the exact Markov property of the exponential kernel.

---

# 5. Prefix quadratic form

Assume:

$$
\operatorname{supp}\mu
\subset[a,b].
$$

Let:

$$
\mu_u
=
\mu|_{[a,u]}.
$$

Define:

$$
q(u)
=
\mathcal C(\mu_u).
$$

Let $s(u)$ denote the right-continuous causal state after any atom at $u$.

---

# 6. Continuous source law

Suppose on an open interval there are no atoms and:

$$
d\mu(u)=f(u)du.
$$

Then:

$$
\boxed{
s'(u)
=
-s(u)+f(u).
}
$$

The prefix quadratic form changes as:

$$
\boxed{
q'(u)
=
2s(u)f(u).
}
$$

Therefore:

$$
\begin{aligned}
\frac d{du}
\left[
q(u)-s(u)^2
\right]
&=
2sf
-
2s(-s+f)
\\
&=
\boxed{
2s(u)^2.
}
\end{aligned}
$$

---

# 7. Prime atom law

Suppose $\mu$ has an atom of weight:

$$
a
$$

at:

$$
u=u_0.
$$

Then:

$$
\boxed{
s^+
=
s^-+a.
}
$$

The prefix quadratic form jumps:

$$
\boxed{
q^+
=
q^-
+
2as^-
+
a^2.
}
$$

But:

$$
(s^+)^2-(s^-)^2
=
2as^-+a^2.
$$

Therefore:

$$
\boxed{
q-s^2
\text{ does not jump at an atom}.
}
$$

This is the key cancellation law.

---

# 8. Prefix dissipation identity

Start at:

$$
a^-
$$

with:

$$
s=0,
\qquad
q=0.
$$

Sections 6–7 imply:

## Theorem 8.1 · Prefix dissipation

$$
\boxed{
q(u)
=
s(u)^2
+
2
\int_a^u
s(v)^2dv.
}
$$

The first term is the current boundary state energy.

The second is accumulated nonnegative dissipation.

Prime atoms do not directly change the dissipation variable.

---

# 9. Full compact-source energy

At the right support boundary:

$$
b,
$$

there is no later forcing.

For:

$$
u>b,
$$

$$
s(u)
=
s(b)e^{-(u-b)}.
$$

So:

$$
2
\int_b^\infty
s(u)^2du
=
s(b)^2.
$$

Therefore:

## Theorem 9.1 · Compact-support causal energy

$$
\boxed{
\mathcal C(\mu)
=
2
\int_a^\infty
s(u)^2du.
}
$$

Equivalently, if:

$$
E(b)
=
2
\int_a^b
s(u)^2du,
$$

then:

$$
\boxed{
\mathcal C(\mu)
=
E(b)+s(b)^2.
}
$$

---

# 10. Apply to the AMRAL local source

Fix:

$$
t,
$$

and:

$$
a=t-h,
\qquad
b=t+h.
$$

The source is:

$$
\boxed{
d\mu_t(u)
=
T_h(t-u)
\left[
\sum_q
\frac{\Lambda(q)}{\sqrt q}
\delta_{\log q}(du)
-
e^{u/2}du
\right].
}
$$

Only:

$$
e^{t-h}<q<e^{t+h}
$$

occur.

---

# 11. Prime jump amplitude

At:

$$
x_q=\log q,
$$

the atom weight is:

$$
\boxed{
A_q(t)
=
\frac{\Lambda(q)}{\sqrt q}
T_h(t-x_q).
}
$$

So the event update is simply:

$$
\boxed{
s
\leftarrow
s+A_q(t).
}
$$

No matrix grows with the number of active primes.

---

# 12. Smooth background forcing

The continuous source is:

$$
\boxed{
f_t(u)
=
-
T_h(t-u)e^{u/2}.
}
$$

On the left half:

$$
a\le u\le t,
$$

$$
\boxed{
f_t(u)
=
-(u-a)e^{u/2}.
}
$$

On the right half:

$$
t\le u\le b,
$$

$$
\boxed{
f_t(u)
=
-(b-u)e^{u/2}
=
(u-b)e^{u/2}.
}
$$

So on every branch:

$$
\boxed{
f(u)
=
e^{u/2}(mu+c)
}
$$

with constant $m,c$.

---

# 13. Exact continuous segment solution

Consider a source-free-of-atoms segment:

$$
[x_0,x_1]
$$

with:

$$
f(u)
=
e^{u/2}(mu+c).
$$

Define:

$$
\boxed{
p=\frac{2m}{3},
}
$$

$$
\boxed{
r_0
=
\frac{2c}{3}
-
\frac{4m}{9}.
}
$$

Then:

$$
\boxed{
P(u)
=
e^{u/2}
(pu+r_0)
}
$$

satisfies:

$$
P'+P=f.
$$

Let:

$$
\Delta=x_1-x_0,
$$

$$
\rho=e^{-\Delta}.
$$

For initial state:

$$
s_0=s(x_0),
$$

the endpoint is:

$$
\boxed{
s_1
=
P(x_1)
+
\rho
[
s_0-P(x_0)
].
}
$$

Thus:

$$
\boxed{
s_1
=
\rho s_0+c_{\rm seg},
}
$$

where:

$$
c_{\rm seg}
=
P(x_1)-\rho P(x_0).
$$

---

# 14. Exact segment energy

Define primitives:

$$
\boxed{
F_2(u)
=
e^u
\left[
p^2(u^2-2u+2)
+
2pr_0(u-1)
+
r_0^2
\right],
}
$$

so:

$$
F_2'(u)=P(u)^2.
$$

Also define:

$$
\boxed{
F_1(u)
=
e^{-u/2}
\left[
-2pu-4p-2r_0
\right],
}
$$

so:

$$
F_1'(u)
=
e^{-u/2}
(pu+r_0).
$$

Let:

$$
J_2
=
F_2(x_1)-F_2(x_0),
$$

$$
J_1
=
F_1(x_1)-F_1(x_0),
$$

and:

$$
P_0=P(x_0).
$$

The energy increment:

$$
\Delta E
=
2
\int_{x_0}^{x_1}
s(u)^2du
$$

has exact quadratic form:

$$
\boxed{
\Delta E
=
A_2s_0^2
+
A_1s_0
+
A_0,
}
$$

with:

$$
\boxed{
A_2
=
1-\rho^2,
}
$$

$$
\boxed{
A_1
=
4e^{x_0}J_1
-
2A_2P_0,
}
$$

and:

$$
\boxed{
A_0
=
2J_2
-
4e^{x_0}J_1P_0
+
A_2P_0^2.
}
$$

All coefficients are elementary functions of the segment endpoints.

---

# 15. Four-state linear lift

Define:

$$
\boxed{
X
=
\begin{pmatrix}
1\\
s\\
s^2\\
E
\end{pmatrix}.
}
$$

A continuous segment has:

$$
s_1
=
\rho s_0+c_{\rm seg}.
$$

Therefore:

$$
s_1^2
=
\rho^2s_0^2
+
2\rho c_{\rm seg}s_0
+
c_{\rm seg}^2.
$$

Together with Section 14:

$$
\boxed{
X_1
=
M_{\rm seg}
X_0,
}
$$

where:

$$
\boxed{
M_{\rm seg}
=
\begin{pmatrix}
1 & 0 & 0 & 0\\
c_{\rm seg} & \rho & 0 & 0\\
c_{\rm seg}^2 & 2\rho c_{\rm seg} & \rho^2 & 0\\
A_0 & A_1 & A_2 & 1
\end{pmatrix}.
}
$$

This is exact.

---

# 16. Prime-atom transfer matrix

For a prime atom of weight:

$$
a_q,
$$

the update:

$$
s^+=s^-+a_q
$$

lifts to:

$$
\boxed{
X^+
=
M_{\rm atom}(a_q)
X^-,
}
$$

where:

$$
\boxed{
M_{\rm atom}(a)
=
\begin{pmatrix}
1&0&0&0\\
a&1&0&0\\
a^2&2a&1&0\\
0&0&0&1
\end{pmatrix}.
}
$$

Again the state dimension is fixed.

---

# 17. Exact local sweep algorithm

For fixed:

$$
t,
$$

construct ordered breakpoints:

1. left boundary:
   $$
   t-h;
   $$
2. all active prime points:
   $$
   \log q;
   $$
3. center:
   $$
   t;
   $$
4. right boundary:
   $$
   t+h.
   $$

Initialize:

$$
X=
(1,0,0,0)^\top.
$$

Sweep left to right.

Between breakpoints:

- use the left-background segment matrix before $t$;
- use the right-background segment matrix after $t$.

At each prime point apply:

$$
M_{\rm atom}(A_q(t)).
$$

At the end:

$$
\boxed{
\mathcal C_h(t)
=
E(b)+s(b)^2.
}
$$

---

# 18. Complexity reduction

A direct pair expansion over $N$ active prime points contains:

$$
O(N^2)
$$

prime-pair terms.

The causal sweep performs:

$$
O(N)
$$

constant-size transfers.

State dimension:

$$
\boxed{
4
}
$$

is independent of $N$.

Thus:

$$
\boxed{
\text{pair-correlation complexity}
\rightarrow
\text{constant-dimensional sequential state}.
}
$$

This is a genuine computational / certificate compression.

---

# 19. What actually carries the cancellation

v1.8 showed that raw prime self-energy is much larger than the final centered energy.

In the causal representation, one never forms:

```text
huge prime-prime positive term
+
huge background-background positive term
-
huge cross term.
```

Instead the signed source enters:

$$
s'+s=\mu
$$

before squaring.

Prime/background cancellation therefore occurs directly in the scalar state:

$$
s.
$$

Only after centering do we form:

$$
s^2.
$$

This is numerically and conceptually better conditioned.

---

# 20. Atom-only special case

If the source consists only of ordered atoms:

$$
x_1<\cdots<x_N
$$

with weights:

$$
a_j,
$$

define gaps:

$$
d_j=x_j-x_{j-1},
$$

and:

$$
r_j=e^{-d_j}.
$$

Then the causal state obeys:

$$
\boxed{
s_j
=
r_js_{j-1}
+
a_j.
}
$$

This is the exact one-dimensional Markov recursion behind the exponential covariance matrix:

$$
K_{ij}
=
e^{-|x_i-x_j|}.
$$

The same kernel is the stationary Ornstein–Uhlenbeck covariance up to scale.

Classical work by Rybicki–Press and later semiseparable / celerite methods exploits exactly this exponential-kernel Markov structure for linear-time matrix computation.

v2.6 does not claim this general kernel fact is new.

---

# 21. External semiseparable alignment

Rybicki and Press showed that matrices generated by the exponential covariance:

$$
e^{-\lambda|t_i-t_j|}
$$

have tridiagonal inverse and support:

$$
O(N)
$$

algorithms.

Later generalized Rybicki–Press and celerite methods exploit sums of exponential kernels through banded / semiseparable representations.

The AMRAL-specific contribution of v2.6 is not the semiseparable kernel itself.

It is the exact specialization to the centered local von-Mangoldt / archimedean source together with:

- the causal dissipation identity;
- the explicit tent-background segment transfer;
- the four-state lifted certificate architecture.

---

# 22. Reference numerical validation

The v2.6 reference package independently computes the same local Cauchy energy in two ways.

### Route A · Causal transfer

- exact elementary background segment maps;
- exact prime jumps;
- final:
  $$
  E+s^2.
  $$

### Route B · Direct pair expansion

- exact prime–prime exponential kernel;
- numerical prime–background integrals;
- numerical background–background triangular double integral.

Tests use the actual local source:

$$
T_h(t-u)
\left[
\sum_q
\frac{\Lambda(q)}{\sqrt q}\delta_{\log q}
-
e^{u/2}du
\right]
$$

for:

$$
h=\log2
$$

at several moderate $t$ values.

The two channels agree to numerical quadrature precision.

This is a normalization check, not RH evidence.

---

# 23. What has become genuinely finite-dimensional?

For every fixed $t$:

```text
STATE DIMENSION = 4
```

regardless of the number of active prime powers.

This is stronger than the earlier statement:

```text
finite number of active primes per checkpoint.
```

However:

```text
NUMBER OF EVENT TRANSFERS
```

still grows without bound with $t$.

Thus v2.6 gives:

$$
\boxed{
\text{finite-dimensional state}
}
$$

but not:

$$
\boxed{
\text{finite-number-of-events global proof}.
}
$$

---

# 24. Remaining theorem barrier

v2.5 showed:

$$
RH
\Longleftrightarrow
\mathscr W_h(T)=O_h(1),
$$

and any:

$$
\mathscr W_h(T)=O(T^A)
$$

with finite $A$ is sufficient for RH.

v2.6 rewrites:

$$
\mathscr W_h(T)
=
\int_T^{T+1}
\left[
E_t(b)+s_t(b)^2
\right]dt,
$$

where $(s,E)$ are generated by the fixed-dimensional transfer system.

Therefore the global GAP becomes:

$$
\boxed{
\text{prove polynomial growth of the output of a four-state,
infinitely-driven prime event system}.
}
$$

This is not solved by the finite-dimensional representation alone.

---

# 25. New canonical state-machine interpretation

The local RH process can now be represented as:

```text
INPUT STREAM
    prime log-point
    prime jump weight

CONTINUOUS SERVICE
    explicit archimedean forcing

CAUSAL STATE
    s

DISSIPATION STATE
    E

LIFTED CERTIFICATE STATE
    (1, s, s^2, E)

OUTPUT
    C_h(t) = E + s^2
```

This is the closest this research line has yet come to a literal finite-dimensional arithmetic state machine.

---

# 26. Suggested v2.7 direction

Recommended:

`RH-CausalState-MovingWindowInvariant-v2.7`

The next question should not be another kernel transform.

It should study the movement of the center:

$$
t\mapsto t+dt.
$$

Prime events occur at:

$$
\boxed{
\log q-h,
\qquad
\log q,
\qquad
\log q+h.
}
$$

corresponding to:

```text
ENTER
CENTER
EXIT
```

of the tent aperture.

Tasks:

1. derive exact updates of the causal transfer state when $t$ crosses each event;
2. avoid rescanning the full active prime list after every event;
3. seek a finite-dimensional moving-window state or a small collection of semiseparable aggregates;
4. derive a recurrence for:
   $$
   \mathcal C_h(t)
   $$
   between events;
5. look for a conservation / dissipation inequality that bounds the event-driven output polynomially;
6. formalize the finite transfer matrices.

This is the natural next autonomous-research GAP.

---

# 27. GAP ledger

## CLOSED / REDUCED

### G1. Causal Cauchy factorization

```text
CLOSED
```

$$
\mathcal C(\mu)
=
2\|s\|_2^2.
$$

### G2. Prefix dissipation law

```text
CLOSED
```

### G3. Exact background segment map

```text
CLOSED
```

### G4. Prime jump map

```text
CLOSED
```

### G5. Four-state lift

```text
CLOSED
```

### G6. Pairwise-to-linear event complexity

```text
CLOSED_AS_ALGORITHM
```

---

## OPEN

### G7. Moving-window finite-state recurrence

```text
OPEN
```

### G8. Event-driven invariant

```text
OPEN
```

### G9. Polynomial global Cauchy energy

```text
OPEN_RH_COMPLETE
```

### G10. Finite global proof object

```text
OPEN
```

### G11. RH

```text
OPEN
```

---

# 28. Trust boundary

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE

FOUR_STATE_LOCAL_COMPRESSION = EXACT
LINEAR_EVENT_SWEEP = EXACT

FINITE_STATE_DIMENSION != FINITE GLOBAL PROOF
O(N) COMPUTATION != ALL-SCALE THEOREM

GLOBAL_POLYNOMIAL ENERGY BOUND = NOT PROVED
GLOBAL_RH_CERTIFICATE = FALSE
```

Forbidden:

$$
\text{state dimension }4
\Longrightarrow
\text{RH is a finite computation}.
$$

Forbidden:

$$
O(N)
\Longrightarrow
O(1).
$$

Forbidden:

$$
\text{positive dissipation identity}
\Longrightarrow
\text{uniform output bound}.
$$

---

# 29. One-line status

> v2.6 factors the v2.5 Cauchy/Helmholtz energy into a first-order causal state. For any compact signed source $\mu$, if $(\partial_u+1)s=\mu$ with left-causal boundary, then the Cauchy quadratic form is exactly $2\int|s|^2$. On a finite support interval the prefix identity is $q=s^2+2\int s^2$, and the quantity $q-s^2$ is continuous across every prime atom and increases between atoms at rate $2s^2$. For the AMRAL source, prime powers are scalar jumps while the smooth archimedean background is an elementary forcing $e^{u/2}(mu+c)$. Every background segment has an exact affine state map and quadratic energy increment, so after lifting to $(1,s,s^2,E)$ both background propagation and prime jumps become fixed $4\times4$ transfer matrices. This reduces an apparent $O(N^2)$ local pair-correlation computation to an exact $O(N)$ event sweep with constant state dimension, matching the known Markov / semiseparable structure of the exponential kernel. The remaining RH barrier is no longer pair enumeration but an infinitely driven finite-dimensional state-output bound. The next target is a moving-window ENTER/CENTER/EXIT recurrence and a polynomial event invariant.

---

# 30. References

1. G. B. Rybicki, W. H. Press, **A Class of Fast Methods for Processing Irregularly Sampled or Otherwise Inhomogeneous One-Dimensional Data**, *Physical Review Letters* 74 (1995), 1060–1063.  
   DOI: https://doi.org/10.1103/PhysRevLett.74.1060

2. Sivaram Ambikasaran, **Generalized Rybicki Press algorithm**, *Numerical Linear Algebra with Applications* 22 (2015), 1102–1114.  
   DOI: https://doi.org/10.1002/nla.2003  
   arXiv: https://arxiv.org/abs/1409.7852

3. Daniel Foreman-Mackey et al., **Fast and Scalable Gaussian Process Modeling with Applications to Astronomical Time Series**, 2017.  
   Exponential / sums-of-exponentials kernels are treated through semiseparable linear-time structure.

4. Michel J. G. Weber, **Cauchy Means of Dirichlet Polynomials**, *Journal of Approximation Theory* 204 (2016), 61–79.  
   DOI: https://doi.org/10.1016/j.jat.2016.01.001

5. AMRAL, **RH-CauchyPoisson-TwistScalarization v2.5**.

---

# 31. Provenance

研究主導：Neo.K

v2.6 causal factorization、dissipation identity、exact background transfer、four-state lift、actual-source reference cross-check 與 canonical source 整理：ChatGPT / GPT-5.6 Sol

日期：2026-09-03

研究定位：AMRAL 黎曼猜想半自主研究線，第三弧線 causal state / finite-dimensional Green transfer 節點。

本文件是 research source artifact，不是 peer-reviewed publication。

所有 claim 必須依 Claim register、GAP ledger 與 Trust boundary 解讀。
