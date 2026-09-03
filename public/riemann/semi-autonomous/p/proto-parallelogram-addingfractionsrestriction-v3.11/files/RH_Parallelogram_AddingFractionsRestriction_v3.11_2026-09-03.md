工程紀錄 · 第五弧線 v3.11 · 2026-09-03 · ODD_ADDING_FRACTIONS_NO_GAIN · MODULATED_PAIRING_GATE · PARALLELOGRAM_FOURIER_LIFT · RH_CLAIM_FALSE

# Parallelogram Adding-Fractions Restriction：Odd-Theorem No-Gain、Even Pairing 結構與 Modulated Pairing Gate

**RH-Parallelogram-AddingFractionsRestriction v3.11**

本節點承接：

- `RH-Parallelogram-SobolevTailTransfer v3.10`
- `RH-Parallelogram-SobolevConductor v3.9`

v3.10 將 deterministic high-conductor barrier壓成：

$$
\boxed{
\text{SUPER-}\sqrt N
\text{ RATIONAL RESTRICTION}.
}
$$

本來最自然的下一步是直接使用 Bloom–Kuperberg 的 adding-fractions theorem。

v3.11 完成這個 audit，得到一個重要 negative result：

$$
\boxed{
\text{Bloom--Kuperberg odd adding-fractions theorem}
}
$$

直接套在 near-zero two-fraction partial sum上，**不改善** classical large-sieve finite-resolution exponent。

所以原本：

```text
super-sqrt(N)
    ->
apply odd adding fractions
    ->
fixed power gain
```

這條捷徑必須停止。

真正和我們四階問題對應的外部 theorem，不是 odd theorem，而是 Kuperberg / Montgomery–Soundararajan 的 **even pairing decomposition**。

Kuperberg 2025 對 smooth weighted refined singular-series sums證明：

$$
\boxed{
V_k
=
\sum_{\sigma\in B_k}
\prod_{(i,j)\in\sigma}
V_2(i,j)
+
O(
h^{k/2-1/(7k)}
\cdot
\text{conductor factor}
)
}
$$

and for the full smooth refined singular-series sum：

$$
\boxed{
R_k(h;f_1,\ldots,f_k)
=
\text{pairing expansion}
+
O_{k,f_i,\varepsilon}
(
h^{k/2-1/(7k)+\varepsilon}
).
}
$$

For：

$$
k=4,
$$

the pairing-free error exponent is：

$$
\boxed{
2-\frac1{28}.
}
$$

v3.11 identifies a new route：

> represent the exact parallelogram relation by a finite Fourier average, then seek a version of the even pairing theorem uniform in the modulation parameter.

The exact relation：

$$
d_1+d_4=d_2+d_3
$$

can be imposed, for any：

$$
M>4H,
$$

by：

$$
\boxed{
\mathbf1_{
d_1+d_4-d_2-d_3=0
}
=
\frac1M
\sum_{j=0}^{M-1}
e\left(
\frac jM
(
d_1+d_4-d_2-d_3
)
\right).
}
$$

If：

$$
\lambda_j=\frac jM,
$$

then physical modulation satisfies the exact exponential-sum translation：

$$
\boxed{
E_{f,H}^{(\lambda)}(\alpha)
=
E_{f,H}(\alpha+\lambda).
}
$$

So the parallelogram problem becomes an **average of shifted smooth singular-series moment problems**。

Kuperberg's published Lemma 5.1 is uniform for arbitrary additive shift $\alpha$，and Lemma 5.3 is stated for arbitrary：

$$
\alpha_1,\alpha_2.
$$

This makes a modulation-uniform extension plausible。

However the published Theorem 1.4 / 1.6 does **not** state uniformity when the shifts vary with $H$，and its proof is omitted by reference to the Montgomery–Vaughan / Montgomery–Soundararajan argument。

Therefore v3.11 does not promote the uniform extension to theorem。

Instead it isolates the canonical next lemma：

## Uniform Modulated Pairing Gate $\operatorname{UMP4}(\delta)$

For all：

$$
\lambda\in\mathbb R/\mathbb Z,
$$

prove a pairing decomposition for the sign pattern：

$$
(+\lambda,-\lambda,-\lambda,+\lambda)
$$

with error：

$$
\boxed{
O(
H^{2-\delta+\varepsilon}
)
}
$$

uniformly in $\lambda$。

If：

$$
\boxed{
\operatorname{UMP4}(1/28)
}
$$

holds with the published Kuperberg exponent, then finite Fourier averaging transfers the same：

$$
H^{2-1/28+\varepsilon}
$$

pairing-free error to the exact parallelogram constraint, with **no Fourier-averaging loss**。

This is now a much more precise and literature-aligned continuation than direct use of the odd theorem。

No RH claim is made。

**RH_CLAIM = False.**

---

# 0. Claim register

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE

BLOOM_KUPERBERG_ODD_THEOREM = EXTERNAL_PUBLISHED

DIRECT_NEAR_ZERO_THREE_FRACTION_LOCALIZATION = CLOSED
DIRECT_ODD_THEOREM_RESTRICTION_GAIN = NONE

EVEN_SMOOTH_PAIRING_THEOREM = EXTERNAL_PUBLISHED
K4_PUBLISHED_PAIRING_ERROR_EXPONENT = 2 - 1/28

PARALLELOGRAM_FINITE_FOURIER_LIFT = CLOSED
MODULATED_EXPONENTIAL_SUM_TRANSLATION = CLOSED

KUPERBERG_LEMMA_5_1_SHIFT_UNIFORM = EXTERNAL_CONFIRMED
KUPERBERG_LEMMA_5_3_SHIFT_UNIFORM = EXTERNAL_CONFIRMED

FULL_THEOREM_MODULATION_UNIFORMITY = NOT_PUBLISHED
UMP4_DELTA_POSITIVE = OPEN

PARALLELOGRAM_CONNECTED_FIXED_POWER = NOT_PROVED
FULL_DETERMINISTIC_ETA_M_POSITIVE = NOT_PROVED
ACTUAL_PRIME_DEVIATION = OPEN

GLOBAL_RH_CERTIFICATE = FALSE
```

---

# 1. Bloom–Kuperberg odd adding-fractions theorem

Bloom–Kuperberg prove near-optimal bounds for an **odd** number of fractions。

A representative consequence says：

for odd：

$$
k\ge3,
$$

the number of solutions to：

$$
\boxed{
\frac{a_1}{q_1}
+\cdots+
\frac{a_k}{q_k}
\in\mathbb Z
}
$$

with：

$$
|a_i|\le n,
\qquad
q_i\le Q,
\qquad
\gcd(a_i,q_i)=1,
$$

is：

$$
\boxed{
\ll
(\log Q)^{O(1)}
n^{(k+1)/2}
Q^{(k-1)/2}.
}
$$

Their more flexible theorem allows different denominator ranges：

$$
Q_i
$$

and intervals：

$$
A_i
$$

of lengths：

$$
\delta_i\ge Q_i^{-1}.
$$

For：

$$
2m+1
$$

fractions, some：

$$
m+1
$$

interval lengths appear in the bound。

This theorem is essentially optimal for odd moments。

---

# 2. Why odd parity matters

For even：

$$
k,
$$

rational equations contain large perfect-matching / pairing families。

This is exactly the same structure responsible for Gaussian even moments in the Montgomery–Soundararajan refined singular-series theory。

Bloom–Kuperberg's strongest new theorem is designed for odd：

$$
k,
$$

where a perfect matching of all variables cannot occur。

Our deterministic covariance is fourth order。

Therefore：

$$
\boxed{
\text{parity mismatch is structural, not cosmetic}.
}
$$

---

# 3. Near-zero pair-sum model

Let：

$$
Q\ge\sqrt N.
$$

Consider reduced fractions：

$$
x=\frac{a_1}{q_1},
\qquad
y=\frac{a_2}{q_2},
$$

with：

$$
q_1,q_2\le Q.
$$

Let：

$$
\beta=\frac br
$$

be reduced with：

$$
r\le Q^2,
$$

and impose：

$$
\boxed{
x+y+\beta\in\mathbb Z,
}
$$

$$
\boxed{
\|\beta\|\le N^{-1}.
}
$$

This is the natural three-fraction lift of a near-zero two-fraction sum。

---

# 4. Localization for $\sqrt N\le Q\le N$

Partition：

$$
\mathbb R/\mathbb Z
$$

into：

$$
O(Q)
$$

arcs：

$$
I_j
$$

of length：

$$
Q^{-1}.
$$

If：

$$
x\in I_j
$$

and：

$$
\|\beta\|\le N^{-1},
$$

then：

$$
y
$$

lies in an opposite arc enlarged by：

$$
N^{-1}.
$$

Because：

$$
Q\le N,
$$

this enlarged arc still has length：

$$
O(Q^{-1}).
$$

Thus use the interval lengths：

$$
\delta_1\asymp Q^{-1},
$$

$$
\delta_2\asymp Q^{-1},
$$

$$
\delta_3\asymp N^{-1}.
$$

The denominator bounds are：

$$
Q_1=Q_2=Q,
\qquad
Q_3=Q^2.
$$

Since：

$$
Q^2\ge N,
$$

the Bloom–Kuperberg interval theorem is applicable to the $\beta$ interval。

---

# 5. Odd-theorem bound in the critical range

For three fractions the theorem selects two interval lengths。

The largest possible product among：

$$
\delta_1\delta_2,
\quad
\delta_1\delta_3,
\quad
\delta_2\delta_3
$$

is：

$$
\asymp Q^{-2}.
$$

Therefore one localized arc contributes at most：

$$
\boxed{
(\log Q)^{O(1)}
Q^4Q^{-2}
=
(\log Q)^{O(1)}
Q^2.
}
$$

There are：

$$
O(Q)
$$

arcs。

Hence：

## Proposition 5.1

For：

$$
\sqrt N\le Q\le N,
$$

the direct odd-theorem localization gives：

$$
\boxed{
\mathcal N(Q,N)
\ll
(\log Q)^{O(1)}
Q^3.
}
$$

---

# 6. Range $Q\ge N$

Now use arcs of length：

$$
N^{-1}.
$$

This is allowed because：

$$
N^{-1}\ge Q^{-1}.
$$

All three relevant intervals then have length：

$$
O(N^{-1}).
$$

The theorem gives per arc：

$$
\boxed{
(\log Q)^{O(1)}
\frac{Q^4}{N^2}.
}
$$

There are：

$$
O(N)
$$

arcs。

Therefore：

## Proposition 6.1

For：

$$
Q\ge N,
$$

$$
\boxed{
\mathcal N(Q,N)
\ll
(\log Q)^{O(1)}
\frac{Q^4}{N}.
}
$$

---

# 7. Compare with finite-resolution scale

The generic number of near-opposite pairs among：

$$
\asymp Q^2
$$

Farey fractions is governed by：

$$
\boxed{
\frac{Q^4}{N}
+
Q^2.
}
$$

This is the same scale encoded by the：

$$
N+Q^2
$$

large-sieve transition。

For：

$$
\sqrt N\le Q\le N,
$$

$$
\frac{Q^4}{N}
\le
Q^3.
$$

At：

$$
Q=N,
$$

the two are equal at：

$$
N^3.
$$

For：

$$
Q>N,
$$

Proposition 6.1 is exactly：

$$
Q^4/N
$$

up to logarithms。

Thus：

## Theorem 7.1 · Direct Odd Adding-Fractions No-Gain

The off-the-shelf Bloom–Kuperberg odd theorem, used through the natural three-fraction lift, provides **no improvement in the finite-resolution exponent** throughout：

$$
Q\ge\sqrt N.
$$

It is either weaker than or equal to the standard resolution scale。

---

# 8. Strategic consequence

Reject the route：

```text
super-sqrt(N) restriction
    ->
three-fraction lift
    ->
odd adding-fractions theorem
    ->
power saving
```

This does not close SRR or STR。

The reason is exactly the even-pairing structure that the odd theorem avoids。

---

# 9. The relevant even theorem

Kuperberg's smooth-weight extension of Montgomery–Soundararajan gives：

$$
\boxed{
V_k(q,H;f_1,\ldots,f_k)
=
\sum_{\sigma\in B_k}
\prod_{(i,j)\in\sigma}
V_2(q,H;f_i,f_j)
+
\operatorname{Err}_k
}
$$

with：

$$
\boxed{
\operatorname{Err}_k
\ll
H^{k/2-1/(7k)}
\left(
\frac q{\phi(q)}
\right)^{C_k}.
}
$$

For the full refined singular-series sum with smooth weights：

$$
R_k(H;f_1,\ldots,f_k),
$$

the published theorem gives：

$$
\boxed{
R_k
=
\text{explicit pairing expansion}
+
O_{k,f_i,\varepsilon}
(
H^{k/2-1/(7k)+\varepsilon}
).
}
$$

---

# 10. Fourth-order exponent

For：

$$
k=4,
$$

$$
\boxed{
\frac k2-\frac1{7k}
=
2-\frac1{28}.
}
$$

Thus the pairing-free smooth fourth moment already has a genuine power saving：

$$
\boxed{
H^{2-1/28+\varepsilon}.
}
$$

This is qualitatively different from the direct odd-theorem near-collision bound。

---

# 11. Exact finite Fourier enforcement of a parallelogram

Let：

$$
d_i\in\mathbb Z,
$$

with：

$$
|d_1+d_4-d_2-d_3|<M.
$$

Then character orthogonality gives：

## Theorem 11.1

$$
\boxed{
\mathbf1_{
d_1+d_4=d_2+d_3
}
=
\frac1M
\sum_{j=0}^{M-1}
e\left(
\frac jM
(
d_1+d_4-d_2-d_3
)
\right).
}
$$

For offsets of size：

$$
O(H),
$$

it is enough to choose：

$$
M>4H.
$$

No approximation is involved。

---

# 12. Modulated smooth exponential sums

Recall：

$$
\boxed{
E_{f,H}(\alpha)
=
\sum_{m\in\mathbb Z}
f(m/H)e(m\alpha).
}
$$

For：

$$
\lambda\in\mathbb R/\mathbb Z,
$$

define physical modulation：

$$
f_{\lambda,H}(x)
=
f(x)
e(\lambda Hx).
$$

At lattice points：

$$
x=m/H,
$$

$$
f_{\lambda,H}(m/H)
=
f(m/H)e(\lambda m).
$$

Therefore：

## Theorem 12.1 · Exact Modulation Translation

$$
\boxed{
E_{f_{\lambda,H},H}(\alpha)
=
E_{f,H}(\alpha+\lambda).
}
$$

Similarly：

$$
E_{f_{-\lambda,H},H}(\alpha)
=
E_{f,H}(\alpha-\lambda).
$$

---

# 13. Parallelogram sign pattern

The relation：

$$
d_1+d_4-d_2-d_3=0
$$

corresponds to the modulation vector：

$$
\boxed{
(+\lambda,-\lambda,-\lambda,+\lambda).
}
$$

Thus an exact parallelogram-constrained refined singular-series sum is a normalized average of shifted fourth moments with this sign pattern。

---

# 14. Why there is no Fourier averaging loss

Suppose for every：

$$
\lambda_j=\frac jM
$$

one has an error：

$$
|\operatorname{Err}(\lambda_j)|
\le
C H^{2-\delta}.
$$

Then：

$$
\left|
\frac1M
\sum_{j=0}^{M-1}
\operatorname{Err}(\lambda_j)
\right|
\le
C H^{2-\delta}.
$$

Therefore the exact Fourier lift costs **no factor $M$**。

The only missing issue is uniformity of the pairing theorem in：

$$
\lambda.
$$

---

# 15. Published shift-uniform ingredients

Kuperberg's smooth proof records two important estimates。

### Lemma 5.1

The relevant quadratic sum is evaluated for：

$$
\boxed{
\text{any }\alpha\in\mathbb R.
}
$$

### Lemma 5.3

The relevant paired exponential sum is bounded for arbitrary：

$$
\boxed{
\alpha_1,\alpha_2\in\mathbb R.
}
$$

The paired output depends on：

$$
\alpha_1-\alpha_2.
$$

So several local ingredients of the proof are already shift-uniform。

---

# 16. Why full modulation uniformity is not yet a theorem here

Kuperberg's Theorem 1.4 states the result for fixed smooth functions：

$$
f_i.
$$

The parallelogram lift would formally replace them by：

$$
f_i(x)e(\pm\lambda Hx),
$$

which depends on：

$$
H.
$$

If one treats these merely as new functions, the published constant：

$$
O_{f_1,\ldots,f_k}
$$

need not be uniform。

One must instead rerun the proof using the exact shifted form：

$$
E_{f,H}(\alpha\pm\lambda),
$$

and verify that **every non-diagonal Montgomery–Vaughan estimate is uniform under those shifts**。

The published paper says the proof of the smooth theorem is identical to the earlier pairing proof and omits it。

Therefore the required global uniformity is not explicitly available from the theorem statement。

---

# 17. Uniform Modulated Pairing Gate

Define：

## $\operatorname{UMP4}(\delta)$

For fixed smooth compactly supported base weights：

$$
f_1,\ldots,f_4,
$$

let：

$$
R_4^{(\lambda)}
$$

be the fourth refined moment with exponential sums shifted by：

$$
(+\lambda,-\lambda,-\lambda,+\lambda).
$$

Let：

$$
\mathcal P_4^{(\lambda)}
$$

denote the complete three-pairing main-term expansion at that shift。

We say：

$$
\operatorname{UMP4}(\delta)
$$

holds if：

$$
\boxed{
\sup_{\lambda\in\mathbb R/\mathbb Z}
\left|
R_4^{(\lambda)}
-
\mathcal P_4^{(\lambda)}
\right|
\ll_\varepsilon
H^{2-\delta+\varepsilon}.
}
$$

---

# 18. Conditional parallelogram theorem

Combine Theorems 11.1 and Definition 17。

## Theorem 18.1 · Conditional Modulated Transfer

If：

$$
\boxed{
\operatorname{UMP4}(\delta)
}
$$

holds, then the corresponding smooth exact-parallelogram **pairing-connected** refined singular-series sum satisfies：

$$
\boxed{
O_\varepsilon(
H^{2-\delta+\varepsilon}
).
}
$$

There is no loss from enforcing the additive relation。

---

# 19. Published exponent target

The fixed-modulation theorem has：

$$
\delta=\frac1{28}
$$

at fourth order。

Therefore the natural target is：

$$
\boxed{
\operatorname{UMP4}
\left(
\frac1{28}
\right).
}
$$

If the existing proof is fully shift-portable, no new exponent technology is required。

The task would be a **uniformity extraction** from the established pairing proof。

---

# 20. Relation to v3.6 pair channels

For：

$$
\{0,h,d,h+d\},
$$

the three formal Wick channels are：

$$
\boxed{
\mu_h^2,
}
$$

$$
\boxed{
\mu_d^2,
}
$$

and：

$$
\boxed{
\mu_{h+d}\mu_{|h-d|}.
}
$$

v3.6 defined：

$$
\mathfrak K_4
=
\mathfrak S_0(0,h,d,h+d)
-
\mu_h^2.
$$

So v3.6 removes only the first pairing before forming the covariance model。

The modulated pairing route says the deterministic problem should be reorganized as：

```text
three explicit two-point pairing channels
+
pairing-connected fourth cumulant.
```

The fourth cumulant is the natural object to which the：

$$
1/28
$$

pairing-error exponent should apply。

---

# 21. Important cancellation warning

The three pairing channels cannot be bounded independently by absolute value without recentering。

For the constrained parallelogram family they contain nonzero lower-order / mean pieces that cancel against each other and against the connected term。

v3.7–v3.8 already found an exact example：

$$
\beta=0
$$

pairing structure cancels an entire spectral axis after pair centering。

Therefore future decomposition must preserve signed pairing cancellation。

---

# 22. Smooth vs. sharp Cesàro geometry

The v3.6 canonical weight：

$$
\Omega_N(h,d)
$$

comes from ordered parallelograms with triangular endpoint weights。

Theorem 18.1 is stated for a smooth product-weight parallelogram sum。

Passing from that smooth model to the exact：

$$
\Omega_N
$$

requires a geometry / partition transfer。

Because：

$$
\Omega_N
$$

is piecewise polynomial with finite-difference control, this transfer is plausible but is **not closed in v3.11**。

Thus there are two distinct next checks：

```text
A. modulation uniformity of the pairing theorem

B. smooth-parallelogram to exact Cesaro-weight transfer
```

Do not merge them into one unsupported claim。

---

# 23. Why this route is better aligned than the odd theorem

The odd adding-fractions theorem solves the no-perfect-matching combinatorics。

Our fourth-order problem explicitly has perfect matchings。

Kuperberg's even theorem already performs the correct operation：

$$
\boxed{
\text{extract all pairings}
+
\text{power-save the non-pairing remainder}.
}
$$

The parallelogram restriction should therefore be attacked by preserving that pairing decomposition under modulation, rather than by pretending the four-fraction equation is an odd-moment problem。

---

# 24. Candidate autonomous theorem schema

A candidate proof should record：

```text
base smooth weights
modulation sign vector
lambda range
whether constants depend on lambda
non-diagonal estimate used
pairing terms extracted
error exponent delta
sharp/smooth geometry transfer
```

Reject any argument that：

- invokes the odd theorem without comparing its count to $Q^4/N+Q^2$；
- treats $O_{f_\lambda}$ as uniform in $\lambda$ without proof；
- drops pairing terms before the Fourier average；
- converts the smooth constrained theorem directly to $\Omega_N$ without a geometry transfer。

---

# 25. Current deterministic status

After v3.11：

```text
direct odd adding-fractions route
    CLOSED AS NO-GAIN

published even pairing exponent
    1/28

exact parallelogram Fourier lift
    CLOSED

local shift-uniform lemmas
    PUBLISHED

global modulation-uniform pairing theorem
    OPEN

smooth-to-Cesaro geometry transfer
    OPEN

full deterministic eta_M > 0
    OPEN
```

---

# 26. Suggested v3.12 direction

Recommended：

`RH-ModulatedPairingUniformity v3.12`

Do not return immediately to generic adding-fractions counting。

Tasks：

1. rewrite Kuperberg's smooth $V_4$ proof with shifted arguments：
   $$
   E_{f_i,H}(\alpha+\lambda_i);
   $$
2. inspect each non-diagonal Montgomery–Vaughan lemma for dependence on absolute location versus frequency differences；
3. prove or refute uniformity for：
   $$
   (\lambda,-\lambda,-\lambda,\lambda);
   $$
4. identify the exact shifted versions of the three $V_2$ pairing terms；
5. establish：
   $$
   \operatorname{UMP4}(1/28)
   $$
   if the proof ports without loss；
6. if uniformity loses：
   $$
   H^\theta,
   $$
   record the corrected exponent：
   $$
   \delta_{\rm corrected}
   =
   1/28-\theta;
   $$
7. only after UMP4 is settled, solve the smooth-to-$\Omega_N$ geometry transfer；
8. if UMP4 fails, return to a genuinely new pairing-aware adding-fractions theorem rather than the published odd theorem。

---

# 27. GAP ledger

## CLOSED / REDUCED

### G1. Direct odd-theorem near-zero count

```text
CLOSED
```

### G2. Direct odd-theorem fixed restriction gain

```text
NONE
```

### G3. Exact parallelogram Fourier lift

```text
CLOSED
```

### G4. Modulated exponential-sum translation

```text
CLOSED
```

### G5. Published fourth-order pairing exponent

```text
1/28
```

---

## OPEN

### G6. UMP4$(1/28)$

```text
OPEN
```

### G7. Smooth-to-Cesàro transfer

```text
OPEN
```

### G8. Full deterministic：

$$
\eta_M>0
$$

```text
OPEN
```

### G9. Actual prime deviation

```text
OPEN
```

### G10. Complete quartic：

$$
\eta_Q>0
$$

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

ODD ADDING-FRACTIONS NO-GAIN
    = DERIVED FROM PUBLISHED THEOREM

EVEN PAIRING 1/28 EXPONENT
    = EXTERNAL PUBLISHED RESULT

UMP4
    = NOT PUBLISHED
    = NOT PROVED HERE

SHIFT-UNIFORM LOCAL LEMMAS
    !=
FULL SHIFT-UNIFORM THEOREM

NO ETA_M > 0 PROVED
NO ETA_Q > 0 PROVED

GLOBAL_RH_CERTIFICATE = FALSE
```

Forbidden：

$$
\text{Kuperberg fixed smooth theorem}
\Longrightarrow
\operatorname{UMP4}
$$

without re-auditing constants。

Forbidden：

$$
Q^3
\Longrightarrow
\text{improvement over }Q^4/N
$$

when：

$$
Q<N.
$$

Forbidden：

$$
\text{pairing-free error}
\Longrightarrow
\text{full }\mathfrak K_4\text{ bound}
$$

without restoring and controlling the pairing channels。

---

# 29. One-line status

> v3.11 audits the proposed adding-fractions continuation and finds that the published odd theorem does not improve the super-$\sqrt N$ finite-resolution exponent when applied through the natural three-fraction lift. Localizing two denominator-$Q$ fractions whose sum is within $N^{-1}$ of an integer gives the Bloom–Kuperberg bound $Q^3(\log Q)^{O(1)}$ for $\sqrt N\le Q\le N$ and $Q^4N^{-1}(\log Q)^{O(1)}$ for $Q\ge N$; these are respectively worse than or equal to the generic $Q^4/N+Q^2$ resolution scale. The mismatch is structural: the current problem is fourth order and dominated by perfect-match pairing geometry, whereas the new adding-fractions theorem is strongest for odd numbers of summands. The relevant published result is instead Kuperberg's smooth even pairing theorem, whose fourth-order non-pairing error has exponent $2-1/28$. The exact parallelogram constraint can be enforced by a normalized finite Fourier average, and physical modulation acts only by translating each exponential-sum argument. Kuperberg's local smooth lemmas are already stated uniformly for arbitrary additive shifts, suggesting a possible uniform extension. However the full theorem is stated only for fixed smooth weights and its proof is omitted by reference to earlier Montgomery–Vaughan/Soundararajan arguments, so uniformity in a modulation of size depending on $H$ is not yet justified. The new canonical gate is UMP4: prove the fourth-order pairing decomposition uniformly for the sign pattern $(+\lambda,-\lambda,-\lambda,+\lambda)$. If the published $1/28$ exponent survives uniformly, exact Fourier averaging would transfer the same fixed power saving to a smooth pairing-connected parallelogram sum with no averaging loss.

---

# 30. References

1. Thomas F. Bloom, Vivian Kuperberg, **Odd moments and adding fractions**, *Proceedings of the London Mathematical Society* 131 (2025), e70068.  
   DOI: https://doi.org/10.1112/plms.70068  
   arXiv: https://arxiv.org/abs/2312.09021

2. Vivian Kuperberg, **Sums of singular series along arithmetic progressions and with smooth weights**, *International Journal of Number Theory* 21 (2025), 53–74.  
   DOI: https://doi.org/10.1142/S1793042125500046  
   arXiv: https://arxiv.org/abs/2301.06095

3. Hugh L. Montgomery, K. Soundararajan, **Primes in short intervals**, *Communications in Mathematical Physics* 252 (2004), 589–617.

4. Hugh L. Montgomery, Robert C. Vaughan, classical reduced-residue / pairing estimates underlying the refined singular-series moment method.

5. AMRAL, **RH-Parallelogram-SobolevTailTransfer v3.10**.

---

# 31. Provenance

研究主導：Neo.K

v3.11 direct odd-theorem no-gain audit、near-zero localization、exact parallelogram Fourier lift、modulated exponential-sum translation、UMP4 gate、published pairing-theorem comparison、reference implementation 與 canonical source 整理：ChatGPT / GPT-5.6 Sol

日期：2026-09-03

研究定位：AMRAL 黎曼猜想半自主研究線，第五弧線 pairing-aware rational restriction / modulation uniformity gate。

本文件是 research source artifact，不是 peer-reviewed publication。

所有 claim 必須依 Claim register、GAP ledger 與 Trust boundary 解讀。
