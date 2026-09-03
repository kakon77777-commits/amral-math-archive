工程紀錄 · 第三弧線 v1.8 · 2026-09-03 · CORRELATION_CANCELLATION · APERTURE_COMPLEXITY_NO_GO · RH_CLAIM_FALSE

# Local Energy Correlation Cancellation 與 Aperture–Information Tradeoff

**RH-LocalEnergy-CorrelationApertureTradeoff v1.8**

本節點承接：

- `RH-FixedAperture-LocalPrimeDiscrepancy v1.6`
- `RH-FixedAperture-v1.65-IndependentAudit`
- `RH-LocalPrime-MeanEnergyBridge v1.7`

v1.7 已把 RH 的 fixed-aperture tail obligation 弱化成 positive mean-energy：

$$
Q_h(T)
=
\int_h^T
|\mathfrak E_h(e^t)|^2\,dt,
$$

並得到：

$$
RH
\Longleftrightarrow
Q_h(T)=O_h(T),
$$

而任何有限 polynomial growth：

$$
Q_h(T)=O(T^A)
$$

也足以推出 RH。

v1.8 不再建立新的 RH equivalent criterion，而回答兩個工程問題：

1. 為什麼 finite-range prime pair energy 仍然需要巨大 cancellation？
2. 能不能再縮小 aperture，使每個 checkpoint 只含 uniformly finite primes，從而真正變成 finite-state / finite-cardinality 問題？

本輪答案：

```text
PAIR-ENERGY ABSOLUTE-BOUND STRATEGY = NO-GO
RENORMALIZED CORRELATION CANCELLATION = NECESSARY

FIXED TEMPORAL SUPPORT = COMPATIBLE WITH RH SENSITIVITY
UNIFORMLY SMALL RAW EVENT CARDINALITY VIA EXPONENTIAL APERTURE SHRINKING
    = INCOMPATIBLE WITH FULL RH SENSITIVITY

SECOND DIFFERENCE = MINIMAL LOCAL AFFINE-MEMORY ERASER
APERTURE RESPONSE ORDER = 2

FINITE GLOBAL PROOF = FALSE
RH_PROVED = FALSE
RH_DISPROVED = FALSE
```

核心結論：

> v1.6–v1.7 的「finite memory」已接近此類 local linear filter 在保留完整 RH sensitivity 下所能做到的極限。若要再把 raw active-prime 數壓成 subexponential / bounded cardinality，aperture 必須指數縮小；但任何能消除 prime ramp 長期記憶的 local affine-memory eraser 都至少具有二階 spectral zero，因此會以至少 $h^2$ 同時抑制 off-axis mode。真正的下一步不能再靠縮 window，而必須靠 correlation compression。

**RH_CLAIM = False.**

---

# 0. Claim register

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE

PRIME_SELF_ENERGY_ASYMPTOTIC = CLOSED
DYADIC_SELF_ENERGY_COEFFICIENT = CLOSED

ABSOLUTE_TERM_BOUNDING_SUFFICIENT = FALSE
RH_CORRELATION_CANCELLATION_LAW = CLOSED_AS_REDUCTION

AFFINE_MEMORY_ERASER_MOMENT_ORDER = AT_LEAST_2
SHRINKING_APERTURE_MODE_ATTENUATION = CLOSED
FULL_RH_SENSITIVITY_REQUIRES_SUBEXPONENTIAL_APERTURE_SHRINK = CLOSED_IN_FILTER_MODEL

RAW_ACTIVE_CARDINALITY_COMPRESSION_BY_EXPONENTIAL_SHRINK = RH_BLIND
ANALYTIC_AGGREGATION_COMPRESSION = NOT_RULED_OUT

GLOBAL_CORRELATION_BOUND = OPEN
FINITE_GLOBAL_PROOF = FALSE
```

---

# 1. Local discrepancy and positive energy

For fixed $h>0$ define the tent:

$$
T_h(v)
=
(h-|v|)_+.
$$

Define the weighted prime-power field:

$$
P_h(t)
=
\sum_{q=p^k}
\frac{\Lambda(q)}{\sqrt q}
T_h(t-\log q).
$$

Define the smooth density:

$$
M_h(t)
=
8e^{t/2}
\left(
\cosh\frac h2-1
\right).
$$

Then the local discrepancy from v1.6 is:

$$
\boxed{
\mathfrak E_h(e^t)
=
P_h(t)-M_h(t).
}
$$

The cumulative energy is:

$$
\boxed{
Q_h(T)
=
\int_h^T
\left[
P_h(t)-M_h(t)
\right]^2dt.
}
$$

This is nonnegative and monotone in $T$.

---

# 2. Self-pair component

Expand only the prime–prime square:

$$
P_h(t)^2.
$$

The diagonal / self-pair component is:

$$
\boxed{
S_h(T)
=
\sum_{q=p^k}
\frac{\Lambda(q)^2}{q}
\int_h^T
T_h(t-\log q)^2dt.
}
$$

The full-line tent self-overlap is:

$$
\boxed{
C_h(0)
=
\int_{\mathbb R}
T_h(t)^2dt
=
\frac{2h^3}{3}.
}
$$

For prime powers satisfying:

$$
2h\le\log q\le T-h,
$$

their whole tent lies inside the integration interval, so their self-energy contribution is exactly:

$$
\frac{2h^3}{3}
\frac{\Lambda(q)^2}{q}.
$$

---

# 3. Weighted square von Mangoldt asymptotic

The prime-power sum satisfies:

$$
\boxed{
\sum_{n\le X}
\frac{\Lambda(n)^2}{n}
=
\frac12(\log X)^2
+
O(1).
}
$$

Sketch:

the higher prime powers contribute a convergent correction:

$$
\sum_p
(\log p)^2
\sum_{k\ge2}
\frac1{p^k}
<
\infty.
$$

For the prime part:

$$
\sum_{p\le X}
\frac{(\log p)^2}{p}
$$

partial summation with the prime number theorem:

$$
\vartheta(X)=X+o(X)
$$

and its standard effective form gives:

$$
\frac12(\log X)^2+O(1).
$$

Therefore the interior self-pair sum has quadratic growth in logarithmic height.

Boundary prime powers with:

$$
T-h<\log q<T+h
$$

contribute only:

$$
O_h(T)
$$

because the weighted-square mass in a fixed logarithmic shell is $O_h(T)$.

Thus:

## Theorem 3.1 · Prime self-energy

$$
\boxed{
S_h(T)
=
\frac{h^3}{3}T^2
+
O_h(T).
}
$$

---

# 4. Dyadic self-energy

For:

$$
h=\log2,
$$

the coefficient is:

$$
\boxed{
\frac{(\log2)^3}{3}
\approx
0.111008\ldots
}
$$

so:

$$
S_{\log2}(T)
\sim
0.111008\ldots\,T^2.
$$

This is already much larger than the RH target:

$$
Q_{\log2}(T)=O(T).
$$

Therefore the total RH energy cannot be established by bounding all prime-pair pieces in absolute value.

---

# 5. Correlation remainder

Define:

$$
\boxed{
R_h(T)
=
Q_h(T)-S_h(T).
}
$$

$R_h$ contains:

- off-diagonal prime–prime interactions;
- prime–archimedean cross terms;
- archimedean square;
- finite integration-boundary effects.

Under RH, v1.7 gives:

$$
Q_h(T)=O_h(T).
$$

Combining with Theorem 3.1:

$$
\boxed{
RH
\Longrightarrow
R_h(T)
=
-\frac{h^3}{3}T^2
+
O_h(T).
}
$$

Conversely, if this cancellation law holds, then:

$$
Q_h(T)=O(T)
$$

and v1.7 gives RH.

Thus:

## Theorem 5.1 · Natural correlation cancellation form

$$
\boxed{
RH
\Longleftrightarrow
R_h(T)
=
-\frac{h^3}{3}T^2
+
O_h(T).
}
$$

A much weaker but still RH-sufficient statement is:

$$
R_h(T)=O(T^A)
$$

for any finite $A$, because:

$$
S_h(T)=O(T^2)
$$

would then imply polynomial growth of $Q_h$.

The true obstacle is therefore cancellation of the much larger raw prime/background contributions down to a polynomial logarithmic scale.

---

# 6. Why absolute pair estimates are structurally wrong

The kernel from v1.7 is positive:

$$
C_h(d)
=
\int_{\mathbb R}
T_h(t)T_h(t-d)\,dt
\ge0.
$$

So every raw prime–prime pair term has nonnegative weight.

The total discrepancy energy becomes small only after subtracting the smooth archimedean background and combining many off-diagonal terms.

Hence a strategy of the form:

```text
bound every prime-pair term by its absolute value
sum the bounds
show the total is small
```

cannot reach the RH scale.

At minimum one must preserve the centered signed covariance structure.

This is the same general phenomenon that underlies the classical connection between prime short-interval variance and pair correlation of zeta zeros: the important object is a variance / centered two-point statistic, not the absolute mass of individual pairs.

---

# 7. Hyperuniformity-like interpretation

If the local weighted prime events behaved like an uncorrelated point process with the same mean intensity, one would expect a shot-noise self-energy of quadratic logarithmic order:

$$
\asymp T^2.
$$

RH instead requires:

$$
Q_h(T)=O(T).
$$

So RH imposes one full power of logarithmic suppression on this particular weighted local variance.

This is naturally described as a hyperuniformity-like cancellation.

The terminology is not claimed as new: Torquato, Zhang, and de Courcy-Ireland have studied hyperuniform and effectively limit-periodic structure in prime configurations, conditionally on Hardy–Littlewood-type prime-pair information.

The present AMRAL statistic is different:

- log-prime coordinates;
- von Mangoldt weights $\Lambda(q)/\sqrt q$;
- fixed tent aperture;
- direct Suzuki / Weil origin;
- RH-equivalent energy growth.

So the external hyperuniformity literature is best treated as structural analogy, not theorem identification.

---

# 8. Numerical sanity: dyadic local energy cancellation

The reference implementation evaluates, for:

$$
h=\log2,
$$

unit-log blocks:

$$
[m,m+1].
$$

For each block it separately computes:

- total local discrepancy energy;
- raw prime self-energy;
- the remainder.

Typical reference values are:

```text
m=1:
total energy  ~ 0.00136
self energy   ~ 0.289
remainder     ~ -0.288

m=5:
total energy  ~ 0.00087
self energy   ~ 1.189
remainder     ~ -1.188

m=8:
total energy  ~ 0.00094
self energy   ~ 1.878
remainder     ~ -1.877
```

So even at small computational scales, the observable already displays very strong cancellation between the raw self component and the rest.

This is only a finite numerical sanity check.

It is not evidence for the global RH tail.

---

# 9. Independent zero-side energy check

Under RH:

$$
D_h(t)
=
2
\sum_{\gamma>0}
c_\gamma(h)\cos(\gamma t),
$$

for simple positive ordinates, with:

$$
c_\gamma(h)
=
\frac{1-\cos(\gamma h)}{\gamma^2}.
$$

Therefore the mean energy of:

$$
\mathfrak E_h(e^t)
=
-2D_h(t)+o(1)
$$

is:

$$
\boxed{
\mathcal M_h
=
8
\sum_{\gamma>0}
\left[
\frac{1-\cos(\gamma h)}{\gamma^2}
\right]^2
}
$$

with multiplicities handled in the grouped-frequency version.

For:

$$
h=\log2,
$$

using only the first $100$ positive zeta zeros in a reference computation gives:

$$
\boxed{
\mathcal M_{\log2}^{(100)}
\approx
0.0009248172.
}
$$

This is already close to the prime-side finite block energies around $0.0009$.

Again, this is a cross-normalization sanity check, not a proof of RH.

---

# 10. Why second difference is the minimal finite-memory local linear filter

The prime contribution in the cumulative Suzuki function is a linear ramp:

$$
(t-a)_+.
$$

A local linear filter $\mathcal L$ that completely removes old affine memory must annihilate both:

$$
1
$$

and:

$$
t.
$$

For a compact kernel $\kappa$ this means:

$$
\boxed{
\int\kappa(u)\,du=0,
}
$$

and:

$$
\boxed{
\int u\kappa(u)\,du=0.
}
$$

Therefore its transform has at least a second-order zero at frequency $0$.

The centered second difference used in v1.6 is the minimal discrete example:

$$
\frac12
[
f(t+h)+f(t-h)-2f(t)
].
$$

It annihilates every affine function exactly.

A first difference does not:

for a sufficiently old ramp,

$$
(t+h-a)_+-(t-a)_+
=
h,
$$

so a permanent memory remains.

Thus:

$$
\boxed{
\text{finite removal of linear prime-ramp memory requires filter order }\ge2.
}
$$

---

# 11. General narrow-aperture response

Let a scaled local affine-memory eraser have first nonzero moment of order:

$$
m\ge2.
$$

Applied to an exponential mode:

$$
e^{\lambda t},
$$

its narrow-aperture multiplier behaves as:

$$
\boxed{
M_h(\lambda)
=
c_m(\lambda h)^m
+
O(h^{m+1})
}
$$

for fixed $\lambda$ and:

$$
h\to0.
$$

For the canonical second difference:

$$
M_h(\lambda)
=
\cosh(\lambda h)-1
=
\frac{\lambda^2h^2}{2}
+
O(h^4).
$$

So order $m=2$ is optimal among affine-memory-erasing local filters in terms of retaining small-aperture spectral sensitivity.

Higher-order memory erasers attenuate the signal even more strongly.

---

# 12. Shrinking aperture and off-axis mode attenuation

Consider a variable aperture:

$$
h(t)\to0.
$$

Let an off-axis zero generate a mode with horizontal growth exponent:

$$
\delta
=
\left|
\Re\rho-\frac12
\right|
>0.
$$

For the second-difference filter, the asymptotic mode size is:

$$
\boxed{
\asymp
h(t)^2e^{\delta t}.
}
$$

Suppose:

$$
-\log h(t)
=
\alpha t+o(t).
$$

Then the filtered mode has exponential rate:

$$
\boxed{
\delta-2\alpha.
}
$$

More generally, an order-$m$ affine-memory eraser has rate:

$$
\delta-m\alpha.
$$

Therefore if:

$$
\alpha>0,
$$

all sufficiently small off-axis displacements:

$$
0<\delta<m\alpha
$$

can be suppressed to non-growing modes.

To preserve sensitivity to arbitrarily small:

$$
\delta>0,
$$

one needs:

$$
\boxed{
\alpha=0,
}
$$

that is:

$$
\boxed{
-\log h(t)=o(t).
}
$$

So full RH sensitivity forbids exponential aperture shrinkage in this filter class.

---

# 13. Block-average active-prime cardinality

Now consider a block:

$$
t\in[T,T+1]
$$

with an aperture:

$$
h_T.
$$

Let:

$$
N_T(t)
=
\#\{
p\text{ prime}:
|\log p-t|<h_T
\}.
$$

By Fubini:

$$
\int_T^{T+1}
N_T(t)\,dt
$$

is the sum, over primes, of the amount of time their aperture interval overlaps the block.

Every prime with:

$$
T+h_T
<
\log p
<
T+1-h_T
$$

contributes exactly:

$$
2h_T.
$$

Hence:

$$
\boxed{
\int_T^{T+1}
N_T(t)\,dt
\ge
2h_T
\left[
\pi(e^{T+1-h_T})
-
\pi(e^{T+h_T})
\right].
}
$$

If:

$$
h_T\to0,
$$

the two endpoints still differ by an asymptotically fixed factor $e$.

The ordinary prime number theorem therefore gives:

$$
\boxed{
\int_T^{T+1}
N_T(t)\,dt
\gtrsim
c
\frac{
h_Te^T
}{T}
}
$$

for a fixed positive constant $c$ and large $T$.

Thus the average raw active-prime count has the information-scale:

$$
\boxed{
\text{active cardinality}
\sim
\frac{h_Te^T}{T}
}
$$

at exponential-order level.

Prime powers only increase the event count, so primes alone suffice for this lower bound.

---

# 14. Cardinality–sensitivity no-go

Suppose one tries to make the average raw active-prime cardinality subexponential:

$$
\int_T^{T+1}
N_T(t)\,dt
=
e^{o(T)}.
$$

Section 13 forces:

$$
h_Te^T
=
e^{o(T)},
$$

hence:

$$
\boxed{
-\log h_T
\ge
T-o(T).
}
$$

So the aperture decay exponent satisfies:

$$
\alpha\ge1.
$$

But for an affine-memory eraser of minimal order:

$$
m=2,
$$

the off-axis response exponent is:

$$
\delta-2\alpha.
$$

Every nontrivial zeta zero lies in the critical strip, so:

$$
\delta\le\frac12.
$$

With:

$$
\alpha\ge1,
$$

one gets:

$$
\delta-2\alpha
\le
-\frac32.
$$

Thus every possible off-axis mode is exponentially suppressed.

Therefore:

## Theorem 14.1 · Raw cardinality vs. RH sensitivity no-go

Within the class of local linear filters that erase affine prime-ramp memory:

> a blockwise aperture schedule that compresses the average raw active-prime count to subexponential size by exponential aperture shrinkage cannot retain full sensitivity to arbitrarily small off-critical zero displacements.

For the minimal second-order filter, the conflict is already absolute: the shrinkage required for subexponential raw event count suppresses every possible zeta off-axis mode.

---

# 15. What this no-go does NOT say

The theorem does not prove that RH cannot have a finite proof.

It does not rule out:

- analytic compression of many primes into one exact sum;
- symbolic prime-counting identities;
- recursive certificates;
- generating-function compression;
- formal tail invariants;
- arithmetic transforms that do not enumerate raw events;
- nonlocal proof methods.

It only rules out the naive route:

```text
make the local window exponentially tiny
-> leave only finitely / subexponentially many raw primes
-> keep the same affine-memory-erasing filter
-> hope RH sensitivity survives.
```

That route loses the signal.

So:

$$
\boxed{
\text{raw event reduction}
\neq
\text{proof-information compression}.
}
$$

The remaining hope for genuine finite closure must come from compression of structure, not deletion of arithmetic input.

---

# 16. Aperture–complexity phase diagram

For a second-order memory eraser with:

$$
h(t)\asymp e^{-\alpha t},
$$

one gets two competing exponents.

### Raw active-prime exponent

At PNT density scale:

$$
\boxed{
1-\alpha.
}
$$

### Detectable off-axis growth exponent

For zero displacement $\delta$:

$$
\boxed{
\delta-2\alpha.
}
$$

Thus:

```text
alpha = 0
    full RH sensitivity
    exponentially many raw local primes

0 < alpha < 1
    fewer raw primes
    blind to sufficiently small delta

alpha >= 1
    subexponential / bounded raw-cardinality regime
    blind to every possible zeta off-axis delta <= 1/2
```

This makes the locality tradeoff explicit.

---

# 17. Consequence for the AMRAL roadmap

v1.6–v1.8 now imply:

$$
\boxed{
\text{do not continue shrinking the aperture as the main closure strategy}.
}
$$

The fixed aperture is not an arbitrary inconvenience.

It is what preserves sensitivity to arbitrarily small horizontal zero displacement while still erasing permanent prime-ramp memory.

The next closure strategy should instead hold:

$$
h>0
$$

fixed and compress the large number of local primes through a correlation invariant.

---

# 18. The new smallest GAP

The v1.7 energy can be written as:

$$
Q_h(T)
=
S_h(T)+R_h(T).
$$

The self part is explicit:

$$
S_h(T)
=
\frac{h^3}{3}T^2+O_h(T).
$$

Therefore the remaining arithmetic problem is:

$$
\boxed{
\text{control the centered finite-range correlation remainder }R_h(T).
}
$$

Natural targets:

### Strong natural target

$$
R_h(T)
=
-\frac{h^3}{3}T^2
+
O_h(T).
$$

Equivalent to the natural RH energy law.

### Much weaker but still sufficient target

$$
R_h(T)=O(T^A)
$$

for any finite $A$.

This already forces polynomial $Q_h(T)$ and hence RH by v1.7.

So the next frontier is not an eigenvalue margin and not a pointwise prime discrepancy.

It is:

$$
\boxed{
\text{polynomial renormalized finite-range covariance}.
}
$$

---

# 19. Relation to known pair-correlation / Selberg-integral literature

Goldston and Montgomery established deep connections between Selberg-type short-interval prime variance and pair correlation of zeta zeros.

Later work by Languasco, Perelli, and Zaccagnini developed generalized Selberg integrals and generalized pair-correlation functions.

This supports the direction of v1.8:

> a centered local-prime $L^2$ statistic should naturally be attacked through correlation methods rather than termwise bounds.

However, the AMRAL observable differs from the standard additive short-interval Selberg integral:

- it uses logarithmic / multiplicative coordinates;
- it uses $\Lambda(n)/\sqrt n$;
- its aperture is fixed in log scale;
- its kernel is triangular;
- its exact RH connection comes through Suzuki's $\Psi$ / Weil framework.

Therefore existing Selberg-integral theorems cannot be imported without a normalization and strength audit.

---

# 20. Numerical cross-check package

The v1.8 reference package computes:

1. unit-log dyadic total energy;
2. raw prime self-energy;
3. correlation remainder;
4. first-$N$ zero spectral prediction for the RH mean-energy constant;
5. synthetic shrinking-aperture responses for exponential modes.

For $h=\log2$, first-$100$ positive zeta zeros give:

$$
\mathcal M_{\log2}^{(100)}
\approx
0.0009248172.
$$

The finite prime-side block energies around $m=3,\ldots,8$ are approximately:

$$
0.0009,
$$

while their self-energy alone grows from order $0.7$ to order $1.9$.

The normalization agreement is strong, but finite numerical agreement is not a global theorem.

---

# 21. GAP ledger

## CLOSED / REDUCED

### G1. Prime self-energy

```text
CLOSED
```

$$
S_h(T)
=
\frac{h^3}{3}T^2+O_h(T).
$$

### G2. RH covariance cancellation form

```text
CLOSED_AS_REDUCTION
```

$$
RH
\Longleftrightarrow
R_h(T)
=
-\frac{h^3}{3}T^2+O_h(T).
$$

### G3. Minimal memory-erasing filter order

```text
CLOSED
```

Affine ramp memory requires at least second-order annihilation.

### G4. Exponential aperture attenuation

```text
CLOSED
```

second-order mode exponent:

$$
\delta-2\alpha.
$$

### G5. Raw-cardinality compression conflict

```text
CLOSED_IN_FILTER_MODEL
```

subexponential average raw prime count requires shrinkage that destroys full RH sensitivity.

---

## OPEN

### G6. Polynomial correlation remainder

```text
OPEN_RH_COMPLETE
```

$$
R_h(T)=O(T^A)
$$

for finite $A$.

### G7. Natural linear total energy

```text
OPEN
```

$$
Q_h(T)=O(T).
$$

### G8. Correlation invariant

```text
OPEN
```

Need symbolic / analytic compression of many local prime events.

### G9. Genuine finite global proof object

```text
OPEN
```

### G10. RH

```text
OPEN
```

---

# 22. Next node

Recommended:

`RH-RenormalizedLocalCorrelation-v1.9`

Primary task:

1. expand $R_h(T)$ exactly into off-diagonal prime-pair and prime-background terms;
2. cancel the deterministic PNT-scale terms analytically before estimating;
3. express the remaining statistic in a form comparable to:
   - Selberg integral;
   - Gallagher lemma;
   - large sieve;
   - Dirichlet-polynomial mean square;
4. determine the weakest known correlation bound that would imply:
   $$
   R_h(T)=O(T^A).
   $$
5. prove no-go statements for any imported theorem whose strength is visibly insufficient.

Do not shrink $h$ as the main strategy.

---

# 23. Trust boundary

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE

FINITE_MEMORY = TRUE
FINITE_RAW_CARDINALITY = FALSE

APERTURE_CARDINALITY_NO_GO = FILTER-CLASS RESULT
NOT A NO-GO FOR FINITE MATHEMATICAL PROOFS

GLOBAL_CORRELATION_BOUND = NOT_PROVED
GLOBAL_RH_CERTIFICATE = FALSE
```

Forbidden:

$$
\text{strong finite cancellation numerically}
\Longrightarrow RH.
$$

Forbidden:

$$
\text{hyperuniformity analogy}
\Longrightarrow
\text{the exact AMRAL energy theorem is known}.
$$

Forbidden:

$$
\text{raw-event cardinality no-go}
\Longrightarrow
\text{no finite proof exists}.
$$

---

# 24. One-line status

> v1.8 shows why the fixed-aperture local-prime reduction does not become globally finite by simply shrinking the window. The prime self-energy alone grows as $(h^3/3)T^2$, while RH requires total mean energy only $O(T)$, forcing a large centered covariance cancellation. At the same time, any local linear filter that completely erases the affine prime-ramp memory must have at least a second-order spectral zero; shrinking its aperture exponentially as $h(t)\sim e^{-\alpha t}$ attenuates an off-axis zero mode from exponent $\delta$ to at most $\delta-2\alpha$. PNT block counting shows that making the average raw active-prime cardinality subexponential requires approximately $\alpha\ge1$, which would suppress every possible zeta off-axis displacement. Thus fixed temporal memory is compatible with RH sensitivity, but raw-event finite cardinality is not obtainable by aperture shrinkage. Genuine finite closure must compress the local prime stream through a correlation / energy invariant rather than deleting events. The next frontier is polynomial control of the renormalized finite-range covariance remainder.

---

# 25. References

1. Masatoshi Suzuki, **Aspects of the screw function corresponding to the Riemann zeta-function**, *Journal of the London Mathematical Society* 108 (2023), 1448–1487.  
   DOI: https://doi.org/10.1112/jlms.12785  
   arXiv: https://arxiv.org/abs/2206.03682

2. Richard P. Brent, David J. Platt, Timothy S. Trudgian, **The mean square of the error term in the prime number theorem**, *Journal of Number Theory* 238 (2022), 740–762.  
   DOI: https://doi.org/10.1016/j.jnt.2021.09.016  
   arXiv: https://arxiv.org/abs/2008.06140

3. Alessandro Zaccagnini, **The Selberg integral and a new pair-correlation function for the zeros of the Riemann zeta-function**, arXiv:1603.02952.  
   https://arxiv.org/abs/1603.02952

4. Salvatore Torquato, Ge Zhang, Matthew de Courcy-Ireland, **Uncovering Multiscale Order in the Prime Numbers via Scattering**, *Journal of Statistical Mechanics: Theory and Experiment* 2018, 093401.  
   DOI: https://doi.org/10.1088/1742-5468/aad6be  
   arXiv: https://arxiv.org/abs/1802.10498

5. Salvatore Torquato, Ge Zhang, Matthew de Courcy-Ireland, **Hidden Multiscale Order in the Primes**, arXiv:1804.06279.  
   https://arxiv.org/abs/1804.06279

6. AMRAL, **RH-FixedAperture-LocalPrimeDiscrepancy v1.6**.

7. AMRAL, **RH-FixedAperture-v1.65-IndependentAudit**.

8. AMRAL, **RH-LocalPrime-MeanEnergyBridge v1.7**.

---

# 26. Provenance

研究主導：Neo.K

v1.8 correlation-cancellation audit、self-energy asymptotic、aperture–cardinality no-go、numerical cross-check 與 canonical source 整理：ChatGPT / GPT-5.6 Sol

日期：2026-09-03

研究定位：AMRAL 黎曼猜想半自主研究線，第三弧線 local covariance / information-locality tradeoff 節點。

本文件是 research source artifact，不是 peer-reviewed publication。

所有 claim 必須依 Claim register、GAP ledger 與 Trust boundary 解讀。
