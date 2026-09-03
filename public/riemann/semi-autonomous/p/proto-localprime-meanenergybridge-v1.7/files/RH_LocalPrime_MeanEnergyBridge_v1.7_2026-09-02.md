工程紀錄 · 第三弧線 v1.7 · 2026-09-02 · MEAN_ENERGY_BRIDGE · FINITE_RANGE_PAIR_FORM · RH_CLAIM_FALSE

# Fixed-Aperture Local Prime Mean-Energy Bridge

**RH-LocalPrime-MeanEnergyBridge v1.7**

本節點承接 `RH-FixedAperture-LocalPrimeDiscrepancy v1.6` 與 `RH-FixedAperture-v1.65-IndependentAudit`。

v1.65 已確認，對任意固定 $h>0$，

$$
D_h(t)
=
\frac12
\left[
\Psi(t+h)+\Psi(t-h)-2\Psi(t)
\right]
$$

是一個忠實的 RH observable；其 exponential growth type 精確記錄 zeta zeros 對 critical line 的最大水平偏離。

v1.7 不再要求 pointwise tail

$$
D_h(t)=e^{o(t)}
$$

或

$$
\mathfrak E_h(x)=x^{o(1)}.
$$

本輪把 proof obligation 弱化成 mean energy / weighted $L^2$：

$$
\boxed{
RH
\Longleftrightarrow
\int_0^\infty
\frac{|D_h(t)|^2}{(1+t)^2}\,dt
<\infty.
}
$$

等價地，對 local prime discrepancy：

$$
\boxed{
RH
\Longleftrightarrow
\int_1^\infty
\frac{
|\mathfrak E_h(x)|^2
}{
x(1+\log x)^2
}
\,dx
<\infty.
}
$$

更適合有限 checkpoint 工程的自然形式是

$$
\boxed{
RH
\Longleftrightarrow
Q_h(T)=O(T),
}
$$

其中

$$
Q_h(T)
=
\int_h^T
|\mathfrak E_h(e^t)|^2\,dt.
$$

每一個 finite $Q_h(T)$ 只需要 $p^k<e^{T+h}$ 的有限 prime-power data；而其 quadratic prime interaction 在 log-prime space 中只有固定作用半徑 $2h$。

**RH_CLAIM = False.**

---

# 0. Claim register

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE

LAPLACE_MULTIPLIER_IDENTITY = CLOSED
FIXED_WEIGHT_L2_CRITERION = CLOSED_AS_REDUCTION
LOCAL_PRIME_WEIGHTED_ENERGY_CRITERION = CLOSED_AS_REDUCTION
LINEAR_CUMULATIVE_ENERGY_CRITERION = CLOSED_AS_REDUCTION

ENERGY_EXPONENT_EQUALS_ZERO_STRIP_WIDTH = CLOSED_AS_REDUCTION
FINITE_RANGE_PAIR_FORM = CLOSED
DYADIC_PAIR_RADIUS = FACTOR_4

FINITE_Q_T_COMPUTABILITY = TRUE
FINITE_GLOBAL_PROOF = FALSE

GLOBAL_ENERGY_BOUND = OPEN
GLOBAL_RH_CERTIFICATE = FALSE
```

---

# 1. External baseline

Suzuki proved

$$
\int_0^\infty
\Psi(t)e^{izt}\,dt
=
-\frac1{z^2}
\frac{\xi'}{\xi}
\left(
\frac12-iz
\right),
\qquad
\Im z>\frac12,
$$

and

$$
RH
\Longleftrightarrow
\Psi(t)=O(1).
$$

Mean-square RH diagnostics are already classical in spirit. Brent–Platt–Trudgian proved that under RH,

$$
I(X)
=
\int_X^{2X}
(\psi(x)-x)^2\,dx
\ll X^2,
$$

and explicitly note that if RH is false, $I(X)/X^2$ is unbounded.

Thus v1.7 is a fixed-aperture local mean-energy reformulation, not a claim that mean-square methods themselves are new.

---

# 2. One-sided Laplace transform of the aperture difference

Define

$$
\mathcal P(z)
=
\int_0^\infty
\Psi(t)e^{izt}\,dt.
$$

For fixed $h>0$, define the compact-interval entire functions

$$
A_h^+(z)
=
\int_0^h
\Psi(u)e^{izu}\,du,
$$

$$
A_h^-(z)
=
\int_0^h
\Psi(u)e^{-izu}\,du.
$$

Using the even extension of $\Psi$,

$$
D_h(t)
=
\frac12
[
\Psi(t+h)+\Psi(|t-h|)-2\Psi(t)
].
$$

Let

$$
\mathcal D_h(z)
=
\int_0^\infty
D_h(t)e^{izt}\,dt.
$$

A direct shift calculation gives

$$
\boxed{
\mathcal D_h(z)
=
(\cos(zh)-1)\mathcal P(z)
+
E_h(z),
}
$$

where

$$
\boxed{
E_h(z)
=
\frac12
\left[
e^{izh}A_h^-(z)
-
e^{-izh}A_h^+(z)
\right].
}
$$

Because $A_h^\pm$ only integrate over $[0,h]$,

$$
E_h
$$

is entire.

Substituting Suzuki,

$$
\boxed{
\mathcal D_h(z)
=
-(\cos(zh)-1)
\frac1{z^2}
\frac{\xi'}{\xi}
\left(
\frac12-iz
\right)
+
E_h(z).
}
$$

The identity is initially valid for $\Im z>1/2$.

---

# 3. Aperture multiplier does not hide off-axis zeros

Suppose

$$
\rho=\beta+i\gamma
$$

is a nontrivial zero with $\beta>1/2$.

Set

$$
z_\rho
=
-\gamma
+
i
\left(
\beta-\frac12
\right).
$$

Then $\Im z_\rho>0$ and

$$
\frac12-iz_\rho=\rho.
$$

For the aperture multiplier to cancel the pole one would need

$$
\cos(z_\rho h)=1.
$$

But the complex solutions of $\cos z=1$ are

$$
z=2\pi k,
\qquad
k\in\mathbb Z,
$$

all real.

Hence every off-critical right-half zero survives as a pole of the transformed $D_h$ expression.

---

# 4. Fixed polynomial-weight $L^2$ criterion

## Theorem 4.1

For every fixed $h>0$,

$$
\boxed{
RH
\Longleftrightarrow
\int_0^\infty
\frac{|D_h(t)|^2}{(1+t)^2}\,dt
<\infty.
}
$$

### RH implies convergence

Under RH, $\Psi(t)=O(1)$, hence $D_h(t)=O_h(1)$ and the weighted integral converges.

### Convergence implies RH

Assume

$$
\mathcal H_h
=
\int_0^\infty
\frac{|D_h(t)|^2}{(1+t)^2}\,dt
<\infty.
$$

For any $y>0$, Cauchy–Schwarz gives

$$
\begin{aligned}
\int_0^\infty
|D_h(t)|e^{-yt}\,dt
&\le
\mathcal H_h^{1/2}
\left[
\int_0^\infty
(1+t)^2e^{-2yt}\,dt
\right]^{1/2}
\\
&<
\infty.
\end{aligned}
$$

Thus $\mathcal D_h(z)$ is holomorphic throughout $\Im z>0$.

On the overlap $\Im z>1/2$ it equals the meromorphic $\xi'/\xi$ expression from Section 2. By analytic continuation, an uncancelled pole cannot occur in the upper half-plane. Section 3 shows every zero with $\Re\rho>1/2$ would give such a pole. Functional-equation symmetry then forces every nontrivial zero onto $\Re s=1/2$.

The same proof works with $(1+t)^{-p}$ for any fixed $p>1$; v1.7 uses $p=2$ as canonical normalization.

---

# 5. Local-prime discrepancy version

Define

$$
\begin{aligned}
\mathfrak E_h(x)
&=
\sum_{
xe^{-h}<n<xe^h
}
\frac{\Lambda(n)}{\sqrt n}
\left(
h-\left|\log\frac nx\right|
\right)
\\
&\quad
-
8\sqrt x
\left(
\cosh\frac h2-1
\right).
\end{aligned}
$$

v1.65 established

$$
D_h(t)
=
-\frac12
\mathfrak E_h(e^t)
-
\mathcal R_h(t),
$$

where

$$
\mathcal R_h(t)=O_h(e^{-5t/2}).
$$

The correction is harmless for every polynomially weighted $L^2$ condition. Therefore

## Theorem 5.1

$$
\boxed{
RH
\Longleftrightarrow
\int_1^\infty
\frac{
|\mathfrak E_h(x)|^2
}{
x(1+\log x)^2
}
\,dx
<\infty.
}
$$

For the dyadic aperture $h=\log2$,

$$
\begin{aligned}
\mathfrak E_2(x)
&=
\sum_{x/2<n<2x}
\frac{\Lambda(n)}{\sqrt n}
\left(
\log2-\left|\log\frac nx\right|
\right)
\\
&\quad
-
(6\sqrt2-8)\sqrt x,
\end{aligned}
$$

and RH is equivalent to

$$
\boxed{
\int_1^\infty
\frac{
|\mathfrak E_2(x)|^2
}{
x(1+\log x)^2
}
\,dx
<\infty.
}
$$

This is a single positive scalar convergence problem, but still ranges over infinitely large $x$.

---

# 6. Cumulative local energy

Define

$$
\boxed{
Q_h(T)
=
\int_h^T
|\mathfrak E_h(e^t)|^2\,dt.
}
$$

Equivalently,

$$
Q_h(T)
=
\int_{e^h}^{e^T}
|\mathfrak E_h(x)|^2
\frac{dx}{x}.
$$

## Theorem 6.1

For any fixed $h>0$,

$$
\boxed{
RH
\Longleftrightarrow
Q_h(T)=O_h(T).
}
$$

Under RH, $\mathfrak E_h(e^t)=O_h(1)$, so the linear bound is immediate.

Conversely, if $Q_h(T)=O(T)$, integration by parts against $e^{-2yt}$ yields

$$
\int_h^\infty
|\mathfrak E_h(e^t)|^2e^{-2yt}\,dt<\infty
$$

for every $y>0$. Cauchy–Schwarz then gives the upper-half-plane holomorphy required in Section 4.

In fact, any polynomial cumulative growth suffices:

$$
\boxed{
Q_h(T)=O(T^A)
\text{ for some finite }A
\Longrightarrow RH.
}
$$

Thus mean energy is a genuinely weaker local obligation than pointwise boundedness.

---

# 7. Unit-log block energies

Define

$$
\boxed{
E_m(h)
=
\int_m^{m+1}
|\mathfrak E_h(e^t)|^2\,dt.
}
$$

A stronger but useful criterion is

$$
\boxed{
RH
\Longleftrightarrow
\sup_{m\ge0}E_m(h)<\infty.
}
$$

Uniform block $L^2$ bounds imply Laplace $L^1$ convergence by summing Cauchy–Schwarz estimates over unit blocks.

The fixed-weight criterion can also be written as the positive series

$$
\boxed{
RH
\Longleftrightarrow
\sum_{m=0}^\infty
\frac{E_m(h)}{(m+1)^2}
<\infty.
}
$$

Every term is finite and finitely computable; the number of terms is still infinite.

---

# 8. Quantitative energy exponent

Let

$$
\Delta_\zeta
=
\sup_\rho
\left|
\Re\rho-\frac12
\right|.
$$

Define

$$
\boxed{
\eta_h
=
\inf
\left\{
\eta\ge0:
Q_h(T)=O(e^{2\eta T})
\right\}.
}
$$

Then

## Theorem 8.1

$$
\boxed{
\eta_h=\Delta_\zeta.
}
$$

The upper bound follows from the v1.65 pointwise exponential-type estimate.

For the lower bound, if $Q_h(T)=O(e^{2\eta T})$, then for every $y>\eta$ the exponentially weighted $L^2$ integral converges. This makes the transform holomorphic in $\Im z>y$, excluding zeros with horizontal displacement greater than $y$. Letting $y\downarrow\eta$ proves the reverse inequality.

Thus mean-energy growth measures exactly the same zero-strip width as pointwise growth, while permitting local spikes.

---

# 9. Signed local discrepancy measure

Define the logarithmic prime–archimedean discrepancy measure

$$
\boxed{
d\nu(u)
=
\sum_{q=p^k}
\frac{\Lambda(q)}{\sqrt q}
\delta_{\log q}(du)
-
e^{u/2}\mathbf1_{u\ge0}\,du.
}
$$

Let

$$
T_h(v)=(h-|v|)_+.
$$

For $t\ge h$,

$$
\boxed{
\mathfrak E_h(e^t)
=
\int_{\mathbb R}
T_h(t-u)\,d\nu(u).
}
$$

So the entire local arithmetic observable is one fixed compact probe translated through a signed prime–archimedean measure.

---

# 10. Finite-range positive quadratic form

Define

$$
\boxed{
K_{h,T}(u,v)
=
\int_h^T
T_h(t-u)T_h(t-v)\,dt.
}
$$

Then

$$
\boxed{
Q_h(T)
=
\iint
K_{h,T}(u,v)
\,d\nu(u)d\nu(v).
}
$$

Because each tent has support radius $h$,

$$
K_{h,T}(u,v)=0
$$

if

$$
|u-v|\ge2h.
$$

Hence two prime powers $q,r$ can directly interact in the quadratic prime part only when

$$
\boxed{
e^{-2h}
<
\frac qr
<
e^{2h}.
}
$$

For $h=\log2$,

$$
\boxed{
\frac14<\frac qr<4.
}
$$

So the total system is globally infinite but has finite multiplicative interaction radius.

---

# 11. Full tent autocorrelation

On the full real line let

$$
C_h(d)
=
\int_{\mathbb R}
T_h(t)T_h(t-d)\,dt.
$$

Writing $r=|d|$,

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

Thus the interior prime-pair interaction is a compact cubic B-spline in log-ratio.

---

# 12. Every finite energy prefix is finite

For $t\le T$, the local aperture only needs prime powers with

$$
q<e^{T+h}.
$$

Therefore each finite $Q_h(T)$ is a finite arithmetic object plus explicit continuous archimedean integrals.

For $h=\log2$ the cutoff is

$$
q<2e^T.
$$

This is the strongest legitimate finite statement:

$$
\boxed{
\text{every finite energy prefix is a finite problem}.
}
$$

It does not imply the global RH problem has finitely many prefixes.

---

# 13. Under RH: exact asymptotic mean energy

Under RH all Suzuki zero parameters are real and

$$
D_h(t)
=
\sum_\gamma
\frac{1-\cos(\gamma h)}{\gamma^2}
e^{i\gamma t}.
$$

The coefficient series is absolutely summable.

Combining repeated ordinates into distinct frequencies $\lambda$, define

$$
a_\lambda(h)
=
m_\lambda
\frac{1-\cos(\lambda h)}{\lambda^2}.
$$

Standard mean-square Parseval theory for absolutely convergent almost-periodic Fourier series gives

$$
\boxed{
\lim_{T\to\infty}
\frac1T
\int_0^T
|D_h(t)|^2\,dt
=
\sum_\lambda
|a_\lambda(h)|^2.
}
$$

Since

$$
\mathfrak E_h(e^t)
=
-2D_h(t)+O_h(e^{-5t/2}),
$$

we obtain

$$
\boxed{
\lim_{T\to\infty}
\frac{Q_h(T)}{T}
=
4
\sum_\lambda
|a_\lambda(h)|^2
}
$$

under RH.

The expected RH regime is therefore not zero energy but a finite nonzero asymptotic energy density.

---

# 14. Relation to classical PNT mean square

Brent–Platt–Trudgian study

$$
I(X)
=
\int_X^{2X}
(\psi(x)-x)^2\,dx.
$$

Under RH they prove $I(X)\ll X^2$, and if RH is false then $I(X)/X^2$ is unbounded.

The v1.7 object is analogous but structurally different:

$$
\boxed{
\text{global additive PNT mean square}
}
$$

versus

$$
\boxed{
\text{fixed-aperture multiplicative local discrepancy energy}.
}
$$

The v1.7 advantages are:

- fixed aperture;
- finite prime memory;
- finite pair-interaction radius;
- direct Suzuki / Weil spectral meaning;
- positive monotone cumulative energy.

---

# 15. What remains open

The natural v1.7 tail target is

$$
\boxed{
\sup_{T\ge T_0}
\frac{Q_h(T)}{T}
<\infty.
}
$$

A weaker theorem of the form

$$
Q_h(T)=O(T^A)
$$

for any finite $A$ would already imply RH.

This is now a two-point local-correlation problem:

$$
\boxed{
\iint
K_{h,T}(u,v)
\,d\nu(u)d\nu(v)
=
O(T^A).
}
$$

Possible tools include:

- Selberg-type mean-square methods;
- multiplicative local prime correlations;
- Fourier / large-sieve control of the signed local measure;
- event-cluster energy cancellation;
- Toeplitz / Levinson identities from v1.5–v1.6.

No existing short-interval theorem located in this audit automatically supplies the required RH-complete all-scale bound.

---

# 16. Is it finite now?

The correct classification is:

```text
FINITE PRIME SUPPORT PER FIXED T = TRUE
FINITE PRIME DATA PER FINITE Q_h(T) = TRUE
FINITE PAIR INTERACTION RADIUS = TRUE
ONE POSITIVE SCALAR ENERGY = TRUE
ONE POSITIVE CONVERGENCE SERIES = TRUE

FINITE NUMBER OF SCALES = FALSE
FINITE GLOBAL ENUMERATION = FALSE
TAIL INVARIANT = OPEN
```

A genuine finite proof object would require one theorem that closes all sufficiently large $T$ at once, for example an explicit polynomial bound on $Q_h(T)$ beyond a finite $T_0$.

That theorem is still RH-complete in strength.

---

# 17. GAP ledger

## CLOSED / REDUCED

### G1. Laplace multiplier identity

```text
CLOSED
```

### G2. Fixed weighted-$L^2$ criterion

```text
CLOSED_AS_REDUCTION
```

### G3. Local-prime weighted-energy criterion

```text
CLOSED_AS_REDUCTION
```

### G4. Linear cumulative energy criterion

```text
CLOSED_AS_REDUCTION
```

### G5. Energy exponent

```text
CLOSED_AS_REDUCTION
```

$$
\eta_h=\Delta_\zeta.
$$

### G6. Finite-range pair interaction

```text
CLOSED
```

---

## OPEN

### G7. Unconditional polynomial energy bound

```text
OPEN_RH_COMPLETE
```

### G8. Natural linear energy invariant

```text
OPEN
```

### G9. Finite-range pair-correlation bound

```text
OPEN
```

### G10. Finite global closure

```text
OPEN
```

### G11. RH

```text
OPEN
```

---

# 18. Trust boundary

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE

V1_7_MEAN_ENERGY_REDUCTION = VALID
FINITE_PREFIX_COMPUTABILITY = TRUE
FINITE_PAIR_RADIUS = TRUE

GLOBAL_ENERGY_BOUND = NOT_PROVED
FINITE_GLOBAL_PROBLEM = FALSE
NOVELTY_PRIORITY = NOT_ESTABLISHED

GLOBAL_RH_CERTIFICATE = FALSE
```

Forbidden:

$$
\text{each finite }Q_h(T)
\Longrightarrow
RH.
$$

Forbidden:

$$
\text{finite interaction radius}
\Longrightarrow
\text{finite total graph}.
$$

Forbidden:

$$
\text{good finite numerical energy}
\Longrightarrow
\text{global mean-energy theorem}.
$$

---

# 19. One-line status

> v1.7 weakens the v1.6/v1.65 pointwise tail obligation to a positive mean-energy problem. For any fixed aperture $h>0$, RH is equivalent to one polynomially weighted $L^2$ convergence condition, equivalently to a weighted local-prime discrepancy energy. A stronger natural form is $Q_h(T)=O(T)$, and under RH the normalized energy has an explicit almost-periodic spectral limit. Every finite $Q_h(T)$ uses finitely many prime powers and the prime-pair interaction has fixed logarithmic range $2h$; for $h=\log2$, direct prime-pair interactions occur only within a factor $4$. The remaining global obstruction is now a positive finite-range two-point energy bound rather than pointwise control, but infinitely many scales are still present.

---

# 20. References

1. Masatoshi Suzuki, **Aspects of the screw function corresponding to the Riemann zeta-function**, *Journal of the London Mathematical Society* 108 (2023), 1448–1487.  
   DOI: https://doi.org/10.1112/jlms.12785  
   arXiv: https://arxiv.org/abs/2206.03682

2. Juan Arias de Reyna, **Explicit formula and quasicrystal definition**, arXiv:2402.10604.  
   https://arxiv.org/abs/2402.10604

3. Richard P. Brent, David J. Platt, Timothy S. Trudgian, **The mean square of the error term in the prime number theorem**, *Journal of Number Theory* 238 (2022), 740–762.  
   DOI: https://doi.org/10.1016/j.jnt.2021.09.016  
   arXiv: https://arxiv.org/abs/2008.06140

4. Kaisa Matomäki, Maksym Radziwiłł, Xuancheng Shao, Terence Tao, Joni Teräväinen, **Higher uniformity of arithmetic functions in short intervals II. Almost all intervals**, *Inventiones mathematicae* 244 (2026), 967–1091.  
   DOI: https://doi.org/10.1007/s00222-026-01408-6

5. AMRAL, **RH-FixedAperture-LocalPrimeDiscrepancy v1.6**, 2026-09-02.

6. AMRAL, **RH-FixedAperture-v1.65-IndependentAudit**, 2026-09-02.

---

# 21. Provenance

研究主導：Neo.K

v1.7 mean-energy reduction、Laplace boundary audit、finite-range pair formulation、reference implementation 與 canonical source 整理：ChatGPT / GPT-5.6 Sol

日期：2026-09-02

研究定位：AMRAL 黎曼猜想半自主研究線，第三弧線 local-prime mean-energy / finite-range pair-correlation 節點。

本文件是 research source artifact，不是 peer-reviewed publication。

所有 claim 必須依 Claim register、GAP ledger 與 Trust boundary 解讀。
