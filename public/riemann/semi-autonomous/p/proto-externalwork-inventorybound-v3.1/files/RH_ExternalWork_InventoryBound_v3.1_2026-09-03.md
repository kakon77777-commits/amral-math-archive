工程紀錄 · 第四弧線 v3.1 · 2026-09-03 · RENEWAL_REWARD_DECOMPOSITION · BOUNDARY_ONLY_NO_GO · 23_STATE_TRACKER · RH_CLAIM_FALSE

# External Work Inventory Bound：Lifecycle Renewal–Reward 分解與 Boundary-Only No-Go

**RH-ExternalWork-InventoryBound v3.1**

本節點承接：

- `RH-ArithmeticInnovation-WorkIdentity v3.0`
- `RH-CausalState-MovingWindowRecurrence v2.7`
- `RH-ArithmeticInnovation-EnergyGate v2.9`

v3.0 已證：

> 完整 ENTER/CENTER/EXIT lifecycle 的 acceleration work 與 kinetic action會 universal cancellation。

因此 v3.1 檢查一個自然猜想：

> 若完整 lifecycle work 都會 cancel，是否可以把一個 block 內所有 completed interior interactions 全部 telescoping 掉，只留下有限 temporal boundary inventory？

答案：

$$
\boxed{\text{不可以。}}
$$

原因是 work cancellation 與 stored-energy area 是不同量。

對任意 pair $(u,v)$，其 pair stored-energy profile：

$$
G_{u,v}(t)
=
e^{-|u-v|}
T_h(t-u)
T_h(t-v)
$$

具有正的完整 lifecycle area：

$$
\boxed{
\int_{\mathbb R}
G_{u,v}(t)dt
=
e^{-|u-v|}
C_h(u-v),
}
$$

其中：

$$
C_h(d)
=
\int_{\mathbb R}
T_h(s)T_h(s-d)ds.
$$

只要：

$$
|u-v|<2h,
$$

就有：

$$
C_h(d)>0.
$$

所以 completed interior lifecycle雖然在 **work** 上 net neutral，仍然對 **block stored-energy integral** 留下完整 reward。

正確的 block identity是：

$$
\boxed{
J_h(t)
=
\mathcal R_h(t)
+
\mathcal U_h(t),
}
$$

其中：

- $J_h(t)$：截至 $t$ 的 cumulative stored-energy area；
- $\mathcal R_h(t)$：已完成 pair lifecycles 的 cumulative full reward；
- $\mathcal U_h(t)$：當下仍 active lifecycles 的 accrued-but-unsettled inventory。

因此：

$$
\boxed{
\int_T^{T+L}
\mathcal C_h(t)dt
=
\Delta\mathcal R_h[T,T+L]
+
\Delta\mathcal U_h[T,T+L].
}
$$

這是 exact renewal–reward decomposition。

關鍵分界：

```text
U_h(t)
    = finite-memory boundary inventory

R_h(t)
    = cumulative arithmetic bulk correlation
```

所以 boundary inventory確實 finite-local，但 interior bulk correlation不能被消去。

更進一步，completed-reward flux可由固定的 one-sided future field追蹤，而且只需要：

$$
\lambda=-1,\qquad j=0,1,2,3
$$

的左右 relative innovation moments。

因此在 v2.7 的 18-state moving system上：

- 新增四個 moments；
- 新增一個 completed-reward scalar；

即可得到固定：

$$
\boxed{
23\text{-state}
}
$$

renewal tracker，並輸出：

$$
\boxed{
\mathcal U_h=J_h-\mathcal R_h.
}
$$

所以 v3.1 取得：

```text
BOUNDARY INVENTORY = FINITE-DIMENSIONAL
BULK COMPLETED REWARD = STILL ARITHMETIC
BOUNDARY-ONLY GLOBAL CLOSURE = NO-GO
```

**RH_CLAIM = False.**

---

# 0. Claim register

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE

PAIR_LIFECYCLE_SUPPORT = CLOSED
PAIR_FULL_REWARD_KERNEL = CLOSED
RENEWAL_REWARD_IDENTITY = CLOSED

BOUNDARY_ONLY_ENERGY_TELESCOPING = FALSE
COMPLETED_INTERIOR_REWARD_VANISHES = FALSE

UNFINISHED_INVENTORY_FINITE_MEMORY = TRUE
COMPLETION_FIELD_FINITE_MOMENT_REPRESENTATION = CLOSED

V27_STATE_DIMENSION = 18
V31_EXTRA_MOMENTS = 4
V31_COMPLETION_REWARD_SCALAR = 1
V31_RENEWAL_TRACKER_DIMENSION = 23

BULK_COMPLETED_REWARD_CORRELATION = OPEN_ARITHMETIC_OBJECT
GLOBAL_POLYNOMIAL_BLOCK_ENERGY = OPEN_RH_COMPLETE

GLOBAL_RH_CERTIFICATE = FALSE
```

---

# 1. Pair lifecycle geometry

Let:

$$
T_h(x)
=
(h-|x|)_+.
$$

For two source locations:

$$
u,v\in\mathbb R,
$$

define:

$$
d=u-v,
$$

$$
m=\frac{u+v}{2}.
$$

The pair stored-energy profile is:

$$
\boxed{
G_{u,v}(t)
=
e^{-|d|}
T_h(t-u)
T_h(t-v).
}
$$

It is nonzero iff both tents overlap.

---

# 2. Pair lifecycle start and completion time

If:

$$
|d|\ge2h,
$$

the two tent lifecycles never overlap and:

$$
G_{u,v}\equiv0.
$$

Assume:

$$
|d|<2h.
$$

Then:

$$
\boxed{
s(u,v)
=
\max(u,v)-h
}
$$

is the pair lifecycle start, and:

$$
\boxed{
e(u,v)
=
\min(u,v)+h
}
$$

is the completion time.

Equivalently, define half-duration:

$$
\boxed{
\ell(d)
=
h-\frac{|d|}{2}.
}
$$

Then:

$$
\boxed{
\operatorname{supp}_tG_{u,v}
=
[m-\ell(d),m+\ell(d)].
}
$$

The lifecycle duration is:

$$
\boxed{
2h-|d|.
}
$$

---

# 3. Full pair lifecycle reward

Define the tent autocorrelation:

$$
\boxed{
C_h(d)
=
\int_{\mathbb R}
T_h(t)
T_h(t-d)dt.
}
$$

Writing:

$$
r=|d|,
$$

$$
\boxed{
C_h(d)
=
\begin{cases}
\displaystyle
\frac{2h^3}{3}
-
hr^2
+
\frac{r^3}{2},
&
0\le r\le h,
\\
\displaystyle
\frac{(2h-r)^3}{6},
&
h\le r\le2h,
\\
0,
&
r\ge2h.
\end{cases}
}
$$

Therefore:

## Theorem 3.1 · Full lifecycle reward

$$
\boxed{
\mathcal H_h(d)
=
\int_{\mathbb R}
G_{u,v}(t)dt
=
e^{-|d|}
C_h(d).
}
$$

For:

$$
|d|<2h,
$$

$$
\mathcal H_h(d)>0.
$$

---

# 4. Work neutrality does not erase stored-energy area

v3.0 proved that for a complete pair lifecycle:

$$
\text{kinetic action}
+
\text{acceleration work}
=
0.
$$

But Theorem 3.1 gives:

$$
\boxed{
\int G_{u,v}(t)dt>0
}
$$

for every nonzero same-sign pair coefficient with overlap.

So:

```text
NET WORK = 0
```

does not imply:

```text
STORED-ENERGY AREA = 0.
```

These are different lifecycle quantities.

---

# 5. Boundary-only inventory no-go

Suppose one hoped to find a per-pair inventory:

$$
V_{u,v}(t)
$$

such that:

1. $V_{u,v}$ is compactly supported in the pair lifecycle;
2.
   $$
   V_{u,v}'(t)=G_{u,v}(t).
   $$

Then:

$$
\int_{\mathbb R}
G_{u,v}(t)dt
=
V_{u,v}(+\infty)
-
V_{u,v}(-\infty)
=
0.
$$

But Theorem 3.1 gives:

$$
\int G_{u,v}
=
\mathcal H_h(d)>0.
$$

Contradiction.

Therefore:

## Theorem 5.1 · Boundary-only no-go

A positive pair stored-energy lifecycle cannot be represented as the derivative of an inventory that vanishes both before and after the lifecycle.

Some permanent completed-reward bookkeeping is mathematically unavoidable.

---

# 6. General signed source

Let:

$$
\eta
$$

be a compact real signed finite measure.

Define:

$$
d\mu_t(u)
=
T_h(t-u)d\eta(u).
$$

The pointwise Cauchy energy is:

$$
\boxed{
\mathcal C_h(t)
=
\iint
G_{u,v}(t)
\,d\eta(u)d\eta(v).
}
$$

Define cumulative energy area:

$$
\boxed{
J_h(t)
=
\int_{-\infty}^{t}
\mathcal C_h(s)ds.
}
$$

---

# 7. Completed lifecycle reward

Define:

$$
\boxed{
\mathcal R_h(t)
=
\iint
\mathbf1_{
e(u,v)\le t
}
\mathcal H_h(u-v)
\,d\eta(u)d\eta(v).
}
$$

Terms with:

$$
|u-v|\ge2h
$$

contribute zero automatically because:

$$
\mathcal H_h(u-v)=0.
$$

$\mathcal R_h(t)$ is the cumulative reward of pair lifecycles that have fully completed by time $t$.

---

# 8. Accrued unfinished inventory

For one pair define:

$$
A_t(u,v)
=
\begin{cases}
0,
&
t\le s(u,v),
\\
\displaystyle
\int_{s(u,v)}^{t}
G_{u,v}(r)dr,
&
s(u,v)<t<e(u,v),
\\
0,
&
t\ge e(u,v).
\end{cases}
$$

The reset to zero after completion means the full reward has been transferred into:

$$
\mathcal R_h.
$$

Define:

$$
\boxed{
\mathcal U_h(t)
=
\iint
A_t(u,v)
\,d\eta(u)d\eta(v).
}
$$

This is the accrued but unsettled lifecycle inventory.

---

# 9. Renewal–reward identity

Pairwise, there are exactly three regimes.

### Before pair start

$$
J_{uv}=0,
\qquad
R_{uv}=0,
\qquad
U_{uv}=0.
$$

### During lifecycle

$$
J_{uv}
=
\int_s^tG,
$$

$$
R_{uv}=0,
$$

$$
U_{uv}
=
\int_s^tG.
$$

### After completion

$$
J_{uv}
=
\mathcal H_h(d),
$$

$$
R_{uv}
=
\mathcal H_h(d),
$$

$$
U_{uv}=0.
$$

Therefore:

## Theorem 9.1 · Renewal–reward decomposition

$$
\boxed{
J_h(t)
=
\mathcal R_h(t)
+
\mathcal U_h(t).
}
$$

This is exact for compact signed finite measures by bilinearity and approximation.

---

# 10. Exact block identity

For any:

$$
L>0,
$$

subtract Theorem 9.1 at:

$$
T
$$

and:

$$
T+L.
$$

Then:

## Theorem 10.1 · Block reward identity

$$
\boxed{
\int_T^{T+L}
\mathcal C_h(t)dt
=
\left[
\mathcal R_h(T+L)-\mathcal R_h(T)
\right]
+
\left[
\mathcal U_h(T+L)-\mathcal U_h(T)
\right].
}
$$

Interpretation:

```text
BLOCK STORED-ENERGY AREA
=
COMPLETED BULK REWARD
+
CHANGE OF UNFINISHED BOUNDARY INVENTORY.
```

---

# 11. Unfinished inventory has finite temporal memory

A pair contributes to:

$$
\mathcal U_h(t)
$$

only when:

$$
s(u,v)<t<e(u,v).
$$

Equivalently:

$$
|t-u|<h,
$$

and:

$$
|t-v|<h.
$$

Therefore:

$$
\boxed{
\mathcal U_h(t)
}
$$

depends only on:

$$
\boxed{
\eta|_{[t-h,t+h]}.
}
$$

Thus unfinished inventory is genuinely finite-memory.

---

# 12. Completed reward is the unavoidable bulk term

By contrast:

$$
\mathcal R_h(t)
$$

stores full lifecycle rewards after the corresponding interactions have ended.

It is not a finite-memory state if represented pair-by-pair.

The block increment:

$$
\Delta\mathcal R_h[T,T+L]
$$

contains every pair lifecycle completing inside the block.

So v3.1 gives:

$$
\boxed{
\text{finite-memory boundary}
+
\text{nontrivial arithmetic bulk}.
}
$$

This is the correct decomposition.

---

# 13. Pair-midpoint bulk / boundary geometry

For a pair with:

$$
m=\frac{u+v}{2},
$$

$$
\ell(d)=h-\frac{|d|}{2},
$$

its temporal support is:

$$
[m-\ell,m+\ell].
$$

For a block:

$$
I=[T,T+L],
$$

the pair is fully contained iff:

$$
\boxed{
T+\ell(d)
\le
m
\le
T+L-\ell(d).
}
$$

It intersects the block only if:

$$
\boxed{
T-\ell(d)
<
m
<
T+L+\ell(d).
}
$$

So every block has:

- fully completed interior pair lifecycles;
- fixed-width clipped boundary lifecycles.

But the interior pair reward is:

$$
\mathcal H_h(d),
$$

not zero.

---

# 14. Long-block consequence

If:

$$
L>2h,
$$

all pairs whose midpoint satisfies:

$$
T+h
\le
m
\le
T+L-h
$$

are guaranteed to complete entirely inside the block.

Therefore the block contains a genuine interior correlation region of length:

$$
L-2h.
$$

Increasing block length does not turn the problem into boundary-only bookkeeping.

It increases the amount of completed bulk correlation.

---

# 15. Full lifecycle kernel is a compact correlation kernel

Define:

$$
\boxed{
\mathcal H_h(d)
=
e^{-|d|}
C_h(d).
}
$$

Properties:

1. even;
2. compact support:
   $$
   |d|<2h;
   $$
3. nonnegative pointwise;
4. positive definite.

Positive definiteness follows because:

- $e^{-|d|}$ is positive definite;
- $C_h$ is an autocorrelation and hence positive definite;
- the pointwise product of positive-definite kernels is positive definite.

Thus:

$$
\boxed{
\iint
\mathcal H_h(u-v)
d\eta(u)d\eta(v)
\ge0.
}
$$

This is the total all-time lifecycle energy.

---

# 16. Relation to weighted Selberg correlation averages

Weighted Selberg integrals are quadratic means whose square expansion becomes an average of shifted correlations.

Coppola–Laporta explicitly develop this weighted-Selberg / correlation-average bridge, including Cesàro weights.

The AMRAL lifecycle kernel:

$$
\mathcal H_h(d)
=
e^{-|d|}C_h(d)
$$

is a log-coordinate, Cauchy-tapered compact correlation kernel.

Thus the unavoidable bulk term is not an accidental artifact of the work formulation.

It is the same type of arithmetic two-point content that Selberg/symmetry methods are designed to study.

---

# 17. Recent prime-pair method alignment

Chou, Haag, Huryn, and Ledoan relate Hardy–Littlewood prime-pair error to norms of a von-Mangoldt exponential sum.

This independently reinforces the structural fact:

```text
prime-pair error / correlations
<->
quadratic or norm information of prime exponential sums.
```

v3.1 does not import their theorem as an RH bound.

It uses it only as external method alignment for the remaining bulk-correlation object.

---

# 18. One-sided completion kernel

Let:

$$
r\in[0,2h).
$$

Define:

$$
\boxed{
H_h^{+}(r)
=
e^{-r}C_h(r).
}
$$

Suppose the earlier source is at:

$$
x.
$$

Its pair interactions with later sources:

$$
x<v<x+2h
$$

all complete at:

$$
\boxed{
t=x+h.
}
$$

Define the future completion field:

$$
\boxed{
\Gamma_h(x)
=
\int_{(x,x+2h)}
H_h^{+}(v-x)
\,d\eta(v).
}
$$

---

# 19. Relative-coordinate completion field

At completion time:

$$
t=x+h,
$$

write:

$$
v=t+d,
\qquad
-h<d<h.
$$

Then:

$$
r=v-x=d+h.
$$

For:

$$
-h<d<0,
$$

$$
\boxed{
C_h(d+h)
=
\frac{h^3}{6}
-
\frac{h^2}{2}d
+
\frac h2d^2
+
\frac12d^3.
}
$$

For:

$$
0<d<h,
$$

$$
\boxed{
C_h(d+h)
=
\frac{h^3}{6}
-
\frac{h^2}{2}d
+
\frac h2d^2
-
\frac16d^3.
}
$$

Therefore:

$$
\boxed{
H_h^+(d+h)
=
e^{-h}e^{-d}
P_\pm(d),
}
$$

where the polynomial degree is at most three.

---

# 20. Completion field from eight innovation moments

Define extended relative innovation moments:

$$
\boxed{
R^S_{-1,j}(t)
=
\int_{D_S}
e^{-d}d^j
\,d\mathfrak I(t+d),
\qquad
j=0,1,2,3.
}
$$

Then:

## Theorem 20.1 · Finite moment completion field

$$
\boxed{
\Gamma_h(t-h)
=
e^{-h}
\left[
\sum_{j=0}^3
p_j^-R^L_{-1,j}(t)
+
\sum_{j=0}^3
p_j^+R^R_{-1,j}(t)
\right],
}
$$

where:

$$
\boxed{
(p_0^-,p_1^-,p_2^-,p_3^-)
=
\left(
\frac{h^3}{6},
-\frac{h^2}{2},
\frac h2,
\frac12
\right),
}
$$

and:

$$
\boxed{
(p_0^+,p_1^+,p_2^+,p_3^+)
=
\left(
\frac{h^3}{6},
-\frac{h^2}{2},
\frac h2,
-\frac16
\right).
}
$$

So completed-reward flux has a fixed finite moment representation.

---

# 21. Continuous completion flux

For the actual arithmetic innovation:

$$
d\eta=d\mathfrak I,
$$

the continuous component is:

$$
-e^{x/2}dx.
$$

At completion time:

$$
t=x+h,
$$

the earlier continuous source has density:

$$
-e^{(t-h)/2}.
$$

Therefore its off-diagonal completion-reward density is:

$$
\boxed{
\dot{\mathcal R}_{\rm cont}(t)
=
-2e^{(t-h)/2}
\Gamma_h(t-h).
}
$$

This accounts for:

- background–background pairs;
- background-earlier / prime-later pairs.

---

# 22. Prime EXIT completion jump

For a prime power $q$:

$$
x_q=\log q,
$$

$$
c_q=\frac{\Lambda(q)}{\sqrt q},
$$

its completion time as the earlier source is:

$$
t_q=x_q+h.
$$

The diagonal full reward is:

$$
\boxed{
c_q^2C_h(0)
=
\frac{2h^3}{3}c_q^2.
}
$$

Its off-diagonal later-source reward is:

$$
2c_q\Gamma_h(x_q).
$$

Thus:

## Theorem 22.1 · Prime completion jump

$$
\boxed{
\Delta\mathcal R_q
=
\frac{2h^3}{3}c_q^2
+
2c_q\Gamma_h(x_q).
}
$$

The future field excludes the same atom at $x_q$.

This completion event occurs exactly at the prime's EXIT event.

---

# 23. Fixed-dimensional renewal tracker

v2.7 uses 18 moving scalars.

Its moment bank already includes:

$$
R^{L/R}_{-1,0},
\qquad
R^{L/R}_{-1,1}
$$

after critical centering / coordinate conversion.

To evaluate Theorem 20.1, add only:

$$
R^{L/R}_{-1,2},
\qquad
R^{L/R}_{-1,3}.
$$

That is four extra moment states.

Add one scalar:

$$
\mathcal R_h
$$

for cumulative completed reward.

Therefore the renewal-extended system has:

$$
\boxed{
18+4+1=23
}
$$

scalar states.

Since v2.7 already tracks:

$$
J_h,
$$

the unfinished inventory is:

$$
\boxed{
\mathcal U_h
=
J_h-\mathcal R_h.
}
$$

---

# 24. What becomes finite-dimensional?

The renewal tracker gives fixed-dimensional access to:

- cumulative stored-energy area:
  $$
  J_h;
  $$
- cumulative completed reward:
  $$
  \mathcal R_h;
  $$
- unfinished finite-memory inventory:
  $$
  \mathcal U_h.
  $$

No pair list or pair matrix is required for the state representation.

However:

$$
\boxed{
\mathcal R_h
}
$$

still integrates an infinite arithmetic event stream.

Finite dimension does not imply a finite global theorem.

---

# 25. Why $\mathcal U_h$ is not enough

Suppose one could prove:

$$
|\mathcal U_h(t)|
\le
\operatorname{poly}(t).
$$

Then:

$$
\int_T^{T+L}\mathcal C_h
=
\Delta\mathcal R_h
+
\operatorname{poly}(T).
$$

The block energy is still controlled by:

$$
\Delta\mathcal R_h.
$$

So a boundary-inventory theorem alone does not close RH.

The bulk completion reward must also be controlled.

---

# 26. Why $\mathcal R_h$ is not a free monotone quantity

Although:

$$
\mathcal H_h(d)\ge0
$$

pointwise, the arithmetic source:

$$
d\mathfrak I
$$

is signed.

Therefore cross terms can be negative.

The block increment:

$$
\Delta\mathcal R_h
$$

is a signed centered correlation quantity, not a monotone prime count.

This is where arithmetic cancellation can occur.

---

# 27. Bulk correlation is the real remaining theorem

The v3.1 decomposition proves:

```text
completed interior lifecycles
    DO NOT disappear

unfinished boundary lifecycles
    ARE finite-memory
```

Therefore a genuine energy proof must control a centered bulk lifecycle correlation.

This can be attacked through:

- weighted Selberg / symmetry integrals;
- dispersion;
- prime-pair correlation;
- Cauchy / exponential-sum methods;
- arithmetic innovation mean square.

The work formalism has not removed that theorem.

It has identified it exactly.

---

# 28. Positive-work warning

v3.0 suggested studying positive external work.

v3.1 adds a caution:

A bound on:

$$
\sum
(\mathcal W_q^{\rm ext})_+
$$

may be much stronger than necessary, because the block energy depends on signed cumulative lifecycle reward plus boundary inventory.

Taking positive parts before completed rewards have canceled may destroy the arithmetic cancellation one hopes to exploit.

So:

```text
POSITIVE WORK
```

is a candidate diagnostic, not yet the canonical theorem target.

The canonical target should preserve signed bulk correlation as long as possible.

---

# 29. Reference finite-source validation

The v3.1 package checks for finite signed atomic sources:

1. direct numerical:
   $$
   J_h(t)=\int_{-\infty}^t\mathcal C_h;
   $$
2. direct completed reward:
   $$
   \mathcal R_h(t);
   $$
3. direct accrued unfinished inventory:
   $$
   \mathcal U_h(t);
   $$
4. identity:
   $$
   J_h=\mathcal R_h+\mathcal U_h;
   $$
5. block identity:
   $$
   \int_T^{T+L}\mathcal C_h
   =
   \Delta\mathcal R_h+\Delta\mathcal U_h;
   $$
6. relative-moment completion field formula.

It also evaluates actual prime EXIT completion rewards against the exact archimedean continuum background.

These are normalization checks only.

---

# 30. New smallest GAP

The hoped-for boundary-only closure is now rejected.

The next genuine target is:

$$
\boxed{
\text{control the signed completed-lifecycle bulk reward increment}
}
$$

at a strength that gives:

$$
\boxed{
\Delta\mathcal R_h[T,T+1]
=
e^{2\sigma T}
\operatorname{poly}(T)
}
$$

with:

$$
\sigma<\frac12,
$$

while keeping:

$$
\Delta\mathcal U_h
$$

at the same or lower scale.

This is a direct correlation theorem.

---

# 31. Suggested v3.2 direction

Recommended:

`RH-CompletedReward-CorrelationKernel v3.2`

Tasks:

1. derive the exact completion-reward flux in the 23-state centered coordinates;
2. express:
   $$
   \Delta\mathcal R_h[T,T+1]
   $$
   as a one-sided compact correlation average;
3. compare the kernel:
   $$
   e^{-r}C_h(r)
   $$
   with weighted Selberg / dispersion kernels;
4. audit whether the one-sided completion ordering gives any advantage over the symmetric block energy;
5. derive its zero-side transfer function;
6. determine whether controlling completed reward is strictly weaker, equivalent, or stronger than the v2.5 Cauchy block scalar;
7. reject the route if it is merely another exact reformulation with no strength gain.

This is the correct next audit.

---

# 32. GAP ledger

## CLOSED / REDUCED

### G1. Pair lifecycle support

```text
CLOSED
```

### G2. Full pair reward kernel

```text
CLOSED
```

### G3. Renewal–reward decomposition

```text
CLOSED
```

### G4. Boundary-only telescoping

```text
NO_GO
```

### G5. Finite-memory unfinished inventory

```text
CLOSED
```

### G6. Completion-field finite moments

```text
CLOSED
```

### G7. 23-state renewal tracker

```text
CLOSED_AS_REPRESENTATION
```

---

## OPEN

### G8. Signed completed-reward bulk bound

```text
OPEN
```

### G9. Any fixed exponent $\sigma<1/2$

```text
OPEN
```

### G10. Polynomial Cauchy block energy

```text
OPEN_RH_COMPLETE
```

### G11. RH

```text
OPEN
```

---

# 33. Trust boundary

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE

BOUNDARY INVENTORY FINITE-MEMORY = TRUE
BOUNDARY INVENTORY ALONE SUFFICIENT = FALSE

COMPLETED REWARD TRACKER FINITE-DIMENSIONAL = TRUE
COMPLETED REWARD GLOBAL BOUND = NOT PROVED

RENEWAL-REWARD IDENTITY = UNIVERSAL GEOMETRY
BULK CORRELATION BOUND = ARITHMETIC CONTENT

GLOBAL_RH_CERTIFICATE = FALSE
```

Forbidden:

$$
\text{completed work cancels}
\Longrightarrow
\text{completed stored-energy reward cancels}.
$$

Forbidden:

$$
\mathcal U_h
\text{ bounded}
\Longrightarrow
RH.
$$

Forbidden:

$$
23\text{-state tracker}
\Longrightarrow
\text{finite global proof}.
$$

---

# 34. One-line status

> v3.1 shows that the hoped-for boundary-only telescoping of block energy is impossible. A pair source has finite lifecycle support, but its complete stored-energy reward is the strictly positive kernel $\mathcal H_h(d)=e^{-|d|}C_h(d)$, so universal work neutrality does not erase its spacetime energy area. The correct exact identity is renewal–reward: cumulative energy $J_h(t)$ equals completed lifecycle reward $\mathcal R_h(t)$ plus unfinished accrued inventory $\mathcal U_h(t)$; therefore every block energy equals the completed bulk reward increment plus the change of finite-memory boundary inventory. The boundary inventory depends only on sources in $[t-h,t+h]$, but the completed bulk term is an unavoidable centered pair-correlation quantity. The completion flux itself is still finite-dimensional: its one-sided future field uses only the $\lambda=-1$ relative innovation moments through degree three. Adding four such moments and one completed-reward scalar to the v2.7 moving state gives a 23-state renewal tracker with $\mathcal U_h=J_h-\mathcal R_h$. Thus finite-dimensional boundary bookkeeping is achievable, but it does not remove the arithmetic bulk theorem. The next node should audit the one-sided completed-reward correlation kernel and determine whether it offers any genuine strength advantage over the existing Cauchy/Selberg energy formulation.

---

# 35. References

1. Giovanni Coppola, Maurizio Laporta, **Generations of Correlation Averages**, *Journal of Numbers* (2014), Article ID 140840.  
   DOI: https://doi.org/10.1155/2014/140840

2. Giovanni Coppola, Maurizio Laporta, **Symmetry and short interval mean-squares**, *Proceedings of the Steklov Institute of Mathematics* 299 (2017), 56–77.  
   DOI: https://doi.org/10.1134/S0081543817080041

3. Leon Chou, Summer Haag, Jake Huryn, Andrew Ledoan, **The error term in counting prime pairs**, *Journal of Number Theory* 278 (2026), 422–450.  
   DOI: https://doi.org/10.1016/j.jnt.2025.04.009

4. AMRAL, **RH-ArithmeticInnovation-WorkIdentity v3.0**.

5. AMRAL, **RH-CausalState-MovingWindowRecurrence v2.7**.

---

# 36. Provenance

研究主導：Neo.K

v3.1 pair lifecycle reward、renewal–reward decomposition、boundary-only no-go、completion-field finite-moment reduction、23-state renewal tracker、reference implementation 與 canonical source 整理：ChatGPT / GPT-5.6 Sol

日期：2026-09-03

研究定位：AMRAL 黎曼猜想半自主研究線，第四弧線 completed-lifecycle bulk correlation / finite-memory inventory 節點。

本文件是 research source artifact，不是 peer-reviewed publication。

所有 claim 必須依 Claim register、GAP ledger 與 Trust boundary 解讀。
