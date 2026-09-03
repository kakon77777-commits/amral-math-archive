工程紀錄 · 第三弧線 v2.0 · 2026-09-03 · METHOD_STRENGTH_AUDIT · EXPONENTIAL_CLASS_GAP · RH_CLAIM_FALSE

# Filtered PNT / Gallagher Strength Audit：已知方法距離 RH 還差多少？

**RH-FilteredPNT-GallagherStrengthAudit v2.0**

本節點承接：

- `RH-FixedAperture-LocalPrimeDiscrepancy v1.6`
- `RH-FixedAperture-v1.65-IndependentAudit`
- `RH-LocalPrime-MeanEnergyBridge v1.7`
- `RH-LocalEnergy-CorrelationApertureTradeoff v1.8`
- `RH-MellinSymmetry-PNTFilterBridge v1.9`

v1.9 已經完成表示層 renormalization：

$$
\mathfrak E_h(e^t)
=
(K_h\ast e)(t),
$$

其中：

$$
e(t)
=
e^{-t/2}
[
\psi(e^t)-e^t
]
$$

是 classical normalized PNT error，而 $K_h$ 是 fixed compact FIR filter。

v1.7 另定義：

$$
Q_h(T)
=
\int_h^T
|\mathfrak E_h(e^t)|^2dt
$$

並得到：

$$
RH
\Longleftrightarrow
Q_h(T)=O_h(T),
$$

以及更一般的 quantitative energy exponent：

$$
\eta_h
=
\inf
\left\{
\eta\ge0:
Q_h(T)=O(e^{2\eta T})
\right\}
=
\Delta_\zeta,
$$

其中：

$$
\Delta_\zeta
=
\sup_\rho
\left|
\Re\rho-\frac12
\right|.
$$

v2.0 不再推新的 criterion。

唯一任務：

> 把目前可用的 PNT error、zero-density、Montgomery–Vaughan Dirichlet mean value、Gallagher/Cesàro smoothing、short-interval almost-all estimates，逐項翻譯成 $Q_h(T)$ 的 strength，判斷真正差距是 logarithmic、polynomial，還是 exponential class。

本輪結論：

```text
CURRENT_UNCONDITIONAL_ENERGY_EXPONENT = 1
RH_ENERGY_EXPONENT = 0

GAP_TYPE = EXPONENTIAL_CLASS
NOT_LOGARITHMIC

GALLAGHER = TRANSFER_PRINCIPLE
NOT_CANCELLATION_SOURCE

GENERIC_DIRICHLET_MEAN_VALUE = DIAGONAL_N_BARRIER
ZERO_DENSITY_WITHOUT_FIXED_ZERO_FREE_STRIP = INSUFFICIENT
ALMOST_ALL_SHORT_INTERVAL = INSUFFICIENT_FOR_UNIFORM_RH_GATE

FIRST_NONTRIVIAL_PROGRESS_GATE =
    ANY FIXED ENERGY EXPONENT < 1
```

**RH_CLAIM = False.**

---

# 0. Canonical progress parameter

Define:

$$
\boxed{
\beta_h
=
2\eta_h.
}
$$

Then:

$$
\boxed{
\beta_h
=
2\Delta_\zeta.
}
$$

Thus:

$$
0\le\beta_h\le1.
$$

Interpretation:

$$
\boxed{
Q_h(T)
\approx
e^{\beta_h T}
\times
\text{subexponential factors}
}
$$

at exponential-type level.

The three important regimes are:

### Critical-strip scale

$$
\beta_h=1.
$$

This only recovers:

$$
0<\Re\rho<1.
$$

### Fixed improved strip

$$
\beta_h<1.
$$

Then:

$$
\left|
\Re\rho-\frac12
\right|
\le
\frac{\beta_h}{2}
<
\frac12.
$$

### RH scale

$$
\boxed{
\beta_h=0.
}
$$

Then:

$$
RH.
$$

This gives AMRAL a continuous progress meter rather than a binary solved / unsolved flag.

---

# 1. Current zero-free-region / PNT-error input

Bellotti's 2025 zero-density work obtains the PNT error at the strength allowed by the Korobov–Vinogradov zero-free region without the earlier $(1-\varepsilon)$ loss.

Write:

$$
\frac{
|\psi(x)-x|
}{x}
\ll
e^{-\omega(x)}.
$$

For the Korobov–Vinogradov region,

$$
\boxed{
\omega(x)
=
d
\frac{
(\log x)^{3/5}
}{
(\log\log x)^{1/5}
},
}
$$

where:

$$
d
=
\left(
\frac{
5^6A_0^3
}{
2^2 3^4
}
\right)^{1/5},
$$

and a current asymptotic zero-free-region constant quoted by Bellotti is:

$$
A_0=\frac1{48.0718}.
$$

For the strength audit only the asymptotic fact matters:

$$
\boxed{
\omega(x)=o(\log x).
}
$$

---

# 2. Translate current PNT error into the AMRAL log observable

Set:

$$
x=e^t.
$$

Then:

$$
E(x)
=
\psi(x)-x
$$

satisfies:

$$
|E(e^t)|
\ll
e^t
e^{-\Omega(t)},
$$

where:

$$
\boxed{
\Omega(t)
=
d
\frac{
t^{3/5}
}{
(\log t)^{1/5}
}.
}
$$

Therefore normalized PNT error:

$$
e(t)
=
e^{-t/2}E(e^t)
$$

satisfies:

$$
\boxed{
|e(t)|
\ll
\exp
\left[
\frac t2-\Omega(t)
\right].
}
$$

Since the v1.9 FIR kernel $K_h$ has fixed compact support and finite $L^1$ norm:

$$
\mathfrak E_h(e^t)
=
K_h\ast e(t)
$$

inherits the same exponential class:

$$
\boxed{
|\mathfrak E_h(e^t)|
\ll_h
\exp
\left[
\frac t2-\Omega(t)+o(\Omega(t))
\right].
}
$$

---

# 3. Current unconditional energy scale

Squaring:

$$
|\mathfrak E_h(e^t)|^2
\ll_h
\exp
\left[
t-2\Omega(t)+o(\Omega(t))
\right].
$$

Therefore a unit log-block obeys at best from this input:

$$
\boxed{
E_T(h)
\ll
\exp
\left[
T-2\Omega(T)+o(\Omega(T))
\right].
}
$$

The cumulative energy has the same exponential type:

$$
\boxed{
Q_h(T)
\ll
\exp
\left[
T-2\Omega(T)+o(\Omega(T))
\right].
}
$$

Since:

$$
\frac{\Omega(T)}{T}\to0,
$$

this gives:

$$
\boxed{
\beta_h\le1,
}
$$

but no fixed improvement:

$$
\beta_h\le1-\varepsilon.
$$

Thus the best current PNT error still lives in exponential class $1$ in the v1.7 energy variable.

The subexponential factor is highly nontrivial and sharp relative to the known zero-free region, but it does not reduce the fixed exponential rate.

---

# 4. Why better constants in the same zero-free-region shape do not cross the gate

Suppose one improves:

$$
d
$$

in:

$$
\Omega(T)
=
dT^{3/5}
(\log T)^{-1/5}.
$$

For every finite:

$$
d>0,
$$

still:

$$
\frac{
2\Omega(T)
}{T}
\to0.
$$

Hence:

$$
T-2\Omega(T)
=
(1-o(1))T.
$$

Therefore:

$$
\boxed{
\text{any improvement only inside the same }
T^{3/5}(\log T)^{-1/5}
\text{ correction cannot produce }
\beta_h<1.
}
$$

This is an exponential-class barrier, not a constant-optimization barrier.

---

# 5. First fixed-strip progress gate

Suppose one could prove, for some fixed:

$$
\varepsilon>0,
$$

$$
\boxed{
Q_h(T)
\ll
e^{(1-\varepsilon)T+o(T)}.
}
$$

Then:

$$
\beta_h\le1-\varepsilon.
$$

By:

$$
\beta_h=2\Delta_\zeta,
$$

this would imply:

$$
\boxed{
\left|
\Re\rho-\frac12
\right|
\le
\frac{1-\varepsilon}{2}.
}
$$

Equivalently:

$$
\boxed{
\frac{\varepsilon}{2}
\le
\Re\rho
\le
1-\frac{\varepsilon}{2}.
}
$$

This would be a genuinely new fixed zero-free strip near both edges.

Thus AMRAL should treat:

```text
ENERGY EXPONENT < 1
```

as the first qualitative success milestone.

---

# 6. Full RH gate

To prove RH it is enough to prove:

$$
Q_h(T)=e^{o(T)}.
$$

v1.7 gives even stronger equivalent natural forms:

$$
Q_h(T)=O(T^A)
$$

for any one finite $A$, or naturally:

$$
Q_h(T)=O(T).
$$

So the full strength gap is:

$$
\boxed{
e^{T-o(T)}
\quad\longrightarrow\quad
e^{o(T)}.
}
$$

This is not a missing logarithm.

It is a collapse of the leading exponential rate from:

$$
1
$$

to:

$$
0.
$$

---

# 7. Zero-density estimates: why density alone cannot close the energy exponent

A zero-density theorem controls:

$$
N(\sigma,U)
=
\#\{
\rho:
\Re\rho>\sigma,\,
0<\Im\rho<U
\}.
$$

Such estimates can strongly restrict how many zeros lie far to the right.

However v1.65 / v1.7 give:

$$
\eta_h
=
\sup_\rho
\left|
\Re\rho-\frac12
\right|.
$$

Thus energy exponential type depends on the **rightmost zero**, not its density.

Even one zero:

$$
\rho_0
$$

with:

$$
\Re\rho_0
=
\frac12+\delta
$$

forces exponential type:

$$
\eta_h\ge\delta.
$$

Therefore:

$$
\boxed{
\text{a density estimate allowing even finitely many zeros to the right of a fixed line cannot establish the corresponding energy exponent bound}.
}
$$

To cross:

$$
\beta_h<1
$$

one needs an actual fixed zero-free strip, or an argument logically equivalent to excluding every zero beyond that strip.

This explains why Bellotti's powerful zero-density theorem can optimize the PNT subexponential error while the fixed energy exponent remains $1$.

---

# 8. Montgomery–Vaughan mean-value theorem

For a Dirichlet polynomial:

$$
D(\tau)
=
\sum_{n\le N}
a_n n^{-i\tau},
$$

the Montgomery–Vaughan mean-value theorem gives:

$$
\boxed{
\int_0^U
|D(\tau)|^2d\tau
=
(U+O(N))
\sum_{n\le N}|a_n|^2.
}
$$

Take the natural critical prime coefficient scale:

$$
a_n
\sim
\frac{\Lambda(n)}{\sqrt n}.
$$

Then:

$$
\boxed{
\sum_{n\le N}|a_n|^2
\sim
\frac12(\log N)^2.
}
$$

Set:

$$
N=e^T.
$$

If the spectral interval length $U$ is only polynomial or subexponential in $T$, then:

$$
O(N)
$$

dominates and gives:

$$
\boxed{
\int_0^U
|D(\tau)|^2d\tau
\ll
e^T
\operatorname{poly}(T).
}
$$

Again the exponential class is:

$$
1.
$$

This is the generic Dirichlet-polynomial diagonal barrier.

---

# 9. Why generic mean value cannot see the needed centered cancellation

The $O(N)$ term arises from frequency spacing:

$$
\log(n+1)-\log n
\asymp
\frac1N.
$$

A generic mean-value theorem must tolerate arbitrary coefficients.

It cannot exploit the highly structured cancellation between:

- von Mangoldt coefficients;
- deterministic PNT background;
- off-diagonal correlations.

Thus generic Dirichlet mean value recovers the same exponential class as the raw prime self-energy in v1.8.

The theorem is doing exactly what it should; the missing ingredient is arithmetic structure.

---

# 10. Gallagher weighted lemma

For an absolutely convergent exponential sum:

$$
S(\tau)
=
\sum_\nu
s(\nu)e^{2\pi i\nu\tau},
$$

Coppola–Laporta's weighted Gallagher lemma gives a transfer of the form:

$$
\boxed{
m_{\delta,U}
\|S\|_{L^2(-U,U)}^2
\le
\int_{\mathbb R}
\left|
\sum_\nu
s(\nu)
w_\delta(x-\nu)
\right|^2dx,
}
$$

where:

$$
m_{\delta,U}
=
\min_{|\tau|\le U}
|\widehat w_\delta(\tau)|^2.
$$

For the Cesàro weight:

$$
C_\delta(x)
=
\left(
1-\frac{|x|}{\delta}
\right)_+,
$$

one obtains the familiar smoothed local-square inequality.

This is extremely close in shape to the v1.6 tent observable.

---

# 11. Gallagher is a bridge, not a cancellation theorem

The right side of the weighted Gallagher inequality is itself:

$$
\boxed{
\text{a local weighted mean square}.
}
$$

Thus Gallagher can translate:

```text
spectral exponential-sum energy
```

into:

```text
Cesàro / local arithmetic energy.
```

But it does not supply a new upper bound for the local arithmetic energy.

If one bounds the right-hand side by absolute values or generic coefficient size, the exponential-class $1$ barrier reappears.

Therefore:

$$
\boxed{
\text{Gallagher removes a representation barrier;
it does not remove the RH correlation barrier.}
}
$$

---

# 12. Fixed aperture and the Gallagher bandwidth condition

For the Cesàro weight, a nontrivial lower Fourier multiplier over:

$$
|\tau|\le U
$$

requires roughly:

$$
\boxed{
\delta U
=
\theta
<
1
}
$$

with fixed $\theta$.

If one identifies the local frequency aperture with fixed log-width:

$$
\delta\asymp h,
$$

then direct unmodulated Gallagher controls only:

$$
U
=
O_h(1).
$$

To study a spectral window centered at a large ordinate:

$$
\tau_0,
$$

one applies Gallagher to:

$$
S(\tau+\tau_0),
$$

which replaces coefficients by phase-twisted coefficients:

$$
\boxed{
s(\nu)
\longmapsto
s(\nu)e^{2\pi i\nu\tau_0}.
}
$$

Therefore high-frequency Gallagher control requires a family of **twisted local arithmetic sums**, not merely the untwisted scalar local discrepancy.

This is another reason Gallagher is best regarded as a method interface rather than an immediate closure theorem.

---

# 13. Twisted-local correlation gate

A Gallagher-based RH proof along this route would ultimately need control of objects schematically of the form:

$$
\boxed{
\sum_{\nu}
s(\nu)
C_h(x-\nu)
e^{i\tau_0\nu},
}
$$

uniformly enough in large:

$$
\tau_0.
$$

For prime frequencies:

$$
\nu=\log n,
$$

this becomes a Mellin phase:

$$
n^{i\tau_0}.
$$

So the missing arithmetic input is not just local prime count.

It is a phase-sensitive local correlation / Dirichlet-polynomial estimate at RH strength.

---

# 14. Short-interval almost-all results

Modern results of Matomäki, Radziwiłł, Shao, Tao, and Teräväinen prove very strong higher-uniformity estimates for $\Lambda$ on almost all additive short intervals, with ranges such as:

$$
H\ge X^{1/3+\varepsilon}
$$

for the von Mangoldt function in their stated higher-uniformity setting.

These theorems are major unconditional advances.

However they do not directly close v2.0 because:

1. they are **almost-all** in the interval origin;
2. the arithmetic function is compared with a structured approximant $\Lambda^\sharp$;
3. the AMRAL RH gate is a uniform all-scale condition;
4. one exceptional off-axis zero cannot be averaged away at exponential-type level.

Therefore:

$$
\boxed{
\text{almost-all local pseudorandomness}
\not\Longrightarrow
\text{uniform RH-complete energy bound}.
}
$$

---

# 15. Strength table

The current method landscape can be summarized as follows.

| Method / input | Translated $Q_h(T)$ strength | Energy exponent $\beta_h$ | What it proves |
|---|---:|---:|---|
| Trivial critical-strip scale | $\exp(T+o(T))$ | $1$ | $0<\Re\rho<1$ scale |
| Current VK / Bellotti PNT error | $\exp(T-2\Omega(T)+o(\Omega(T)))$ | $1$ | subexponential improvement, no fixed strip |
| Generic Montgomery–Vaughan | $\exp(T)\operatorname{poly}(T)$ | $1$ | generic diagonal control |
| Gallagher lemma alone | transfer only | none by itself | spectral ↔ local-energy bridge |
| Any future fixed saving | $\exp((1-\varepsilon)T+o(T))$ | $\le1-\varepsilon$ | new fixed zero strip |
| Subexponential energy | $\exp(o(T))$ | $0$ | RH |
| Natural RH mean energy | $O(T)$ | $0$ | RH |

This is the canonical v2.0 strength ladder.

---

# 16. Method-strength gate for future AI research

Every candidate theorem should be translated into:

$$
Q_h(T)
\le
\mathcal B(T).
$$

Then compute:

$$
\boxed{
\beta_{\rm candidate}
=
\limsup_{T\to\infty}
\frac{
\log\mathcal B(T)
}{T}.
}
$$

Interpretation:

### If:

$$
\beta_{\rm candidate}=1,
$$

the theorem may improve constants or subexponential factors but gives no fixed zero strip.

### If:

$$
0<\beta_{\rm candidate}<1,
$$

it is genuine new zero-strip progress.

### If:

$$
\beta_{\rm candidate}=0,
$$

and the bound is rigorous globally, it closes RH through v1.7.

This should be applied before spending large AI compute on a candidate method.

---

# 17. No-go checklist

The following are now known insufficient by themselves.

## N1. Better Korobov–Vinogradov constants

```text
INSUFFICIENT FOR EXPONENT DROP
```

## N2. Zero-density without fixed exclusion

```text
INSUFFICIENT FOR SUPREMUM CONTROL
```

## N3. Generic Dirichlet mean value

```text
DIAGONAL N BARRIER
```

## N4. Gallagher lemma without a new local correlation estimate

```text
TRANSFER ONLY
```

## N5. Almost-all short-interval estimates

```text
DO NOT GIVE UNIFORM ALL-SCALE GATE
```

## N6. Finite computation to a very high $T$

```text
DOES NOT CONTROL THE EXPONENTIAL TAIL
```

---

# 18. What kind of theorem would actually count as progress?

The next theorem does **not** need to prove RH.

A meaningful intermediate target is any fixed:

$$
\varepsilon>0
$$

such that:

$$
\boxed{
Q_h(T)
\ll
e^{(1-\varepsilon)T}
\operatorname{poly}(T).
}
$$

This would imply the new zero strip:

$$
\boxed{
\frac{\varepsilon}{2}
\le
\Re\rho
\le
1-\frac{\varepsilon}{2}.
}
$$

Thus v2.0 recommends a staged research program:

```text
Stage 0:
beta = 1
current unconditional class

Stage 1:
prove beta < 1
first fixed-strip breakthrough

Stage 2:
push beta downward

Stage 3:
beta = 0
RH
```

This produces measurable mathematical progress even if RH itself remains open.

---

# 19. Recommended v2.1 direction

Do not simply apply another generic mean-value inequality.

Recommended node:

`RH-TwistedLocalCorrelation-ExponentDrop-v2.1`

Primary question:

$$
\boxed{
\text{Can arithmetic structure beat the generic }e^T
\text{ diagonal class by a fixed exponential factor?}
}
$$

Concrete tasks:

1. define the phase-twisted local tent sum required by high-frequency Gallagher;
2. subtract the deterministic PNT background before estimating;
3. compute its exact second moment as a shifted prime-correlation form;
4. identify which off-diagonal prime correlations could cancel a fixed fraction of the diagonal exponential mass;
5. compare with known prime-pair / Selberg / large-sieve estimates;
6. seek any theorem yielding:
   $$
   \beta<1;
   $$
7. reject methods that only improve:
   $$
   e^{-o(T)}
   $$
   factors.

This gives a nonbinary research objective.

---

# 20. GAP ledger

## CLOSED / AUDITED

### G1. Current PNT-error energy class

```text
CLOSED_AS_STRENGTH_AUDIT
```

$$
\beta=1.
$$

### G2. Generic Dirichlet mean-value class

```text
CLOSED_AS_STRENGTH_AUDIT
```

$$
\beta=1.
$$

### G3. Gallagher role

```text
CLASSIFIED_AS_TRANSFER_PRINCIPLE
```

### G4. Zero-density limitation

```text
CLOSED_AS_STRUCTURAL_DIAGNOSIS
```

Density without fixed exclusion cannot control the rightmost-zero exponent.

### G5. First fixed-strip gate

```text
DEFINED
```

$$
\beta<1.
$$

---

## OPEN

### G6. Any unconditional exponent drop

```text
OPEN
```

$$
\beta<1.
$$

### G7. Twisted local correlation estimate

```text
OPEN
```

### G8. Fixed zero-strip improvement

```text
OPEN
```

### G9. Energy exponent zero

```text
OPEN_RH_COMPLETE
```

### G10. RH

```text
OPEN
```

---

# 21. Trust boundary

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE

CURRENT_UNCONDITIONAL_EXPONENT = 1
RH_EXPONENT = 0

NO FIXED EXPONENT SAVING HAS BEEN PROVED

GALLAGHER_RELEVANT = TRUE
GALLAGHER_SUFFICIENT_ALONE = FALSE

BELLOTTI_PNT_RESULT = EXTERNAL_PREPRINT_INPUT
GENERIC_MONTGOMERY_VAUGHAN = CLASSICAL_INPUT

GLOBAL_RH_CERTIFICATE = FALSE
```

Forbidden:

$$
\text{subexponential saving inside }e^T
\Longrightarrow
\text{fixed zero strip}.
$$

Forbidden:

$$
\text{few bad zeros}
\Longrightarrow
\text{small energy exponent}.
$$

Forbidden:

$$
\text{Gallagher transform}
\Longrightarrow
\text{Gallagher cancellation theorem}.
$$

---

# 22. One-line status

> v2.0 performs the requested strength audit instead of creating another RH-equivalent formulation. The current best zero-free-region/PNT-error technology translates into filtered local energy of size $\exp[T-2dT^{3/5}(\log T)^{-1/5}+o(T^{3/5})]$, which still has fixed exponential class $1$. Generic Montgomery–Vaughan Dirichlet-polynomial mean value lands in the same class because its $O(N)$ diagonal term becomes $N=e^T$. Weighted Gallagher/Cesàro lemmas correctly transform spectral mean square into local weighted arithmetic mean square, but they do not provide the missing cancellation; at high spectral ordinates they additionally require phase-twisted local sums. Zero-density information alone cannot close the gap because the energy exponent is controlled by the single rightmost zero, not the number of such zeros. Therefore the present gap is not logarithmic: RH requires the energy exponent to collapse from $1$ to $0$. The first genuinely new milestone is any fixed exponent drop $\beta<1$, which would already imply a new fixed zero strip. v2.1 should target a twisted centered local-correlation estimate capable of beating the generic $e^T$ class by a fixed exponential factor.

---

# 23. References

1. Chiara Bellotti, **A new zero-density estimate for $\zeta(s)$ and the error term in the Prime Number Theorem**, arXiv:2508.02041, 2025.  
   https://arxiv.org/abs/2508.02041

2. Daniel R. Johnston, **Zero-density estimates and the optimality of the error term in the prime number theorem**, arXiv:2411.13791.  
   https://arxiv.org/abs/2411.13791

3. Giovanni Coppola, Maurizio Laporta, **A generalization of Gallagher's lemma for exponential sums**, arXiv:1411.1739; Šiauliai Mathematical Seminar 10:18 (2015), 29–47.  
   https://arxiv.org/abs/1411.1739

4. Giovanni Coppola, Maurizio Laporta, **A modified Gallagher's Lemma**, arXiv:1301.0008.  
   https://arxiv.org/abs/1301.0008

5. H. L. Montgomery and R. C. Vaughan, classical mean-value theorem for Dirichlet polynomials. A modern statement:
   $$
   \int_1^U
   \left|
   \sum_{n\le N}a(n)n^{-it}
   \right|^2dt
   =
   (U+O(N))
   \sum_{n\le N}|a(n)|^2.
   $$

6. Richard P. Brent, David J. Platt, Timothy S. Trudgian, **The mean square of the error term in the prime number theorem**, *Journal of Number Theory* 238 (2022), 740–762.  
   DOI: https://doi.org/10.1016/j.jnt.2021.09.016  
   arXiv: https://arxiv.org/abs/2008.06140

7. Kaisa Matomäki, Maksym Radziwiłł, Xuancheng Shao, Terence Tao, Joni Teräväinen, **Higher uniformity of arithmetic functions in short intervals II. Almost all intervals**, *Inventiones mathematicae* 244 (2026), 967–1091.  
   DOI: https://doi.org/10.1007/s00222-026-01408-6  
   arXiv: https://arxiv.org/abs/2411.05770

8. AMRAL, **RH-MellinSymmetry-PNTFilterBridge v1.9**.

9. AMRAL, **RH-LocalPrime-MeanEnergyBridge v1.7**.

---

# 24. Provenance

研究主導：Neo.K

v2.0 method-strength audit、PNT-error exponent translation、Gallagher role classification、Dirichlet mean-value barrier analysis 與 canonical source 整理：ChatGPT / GPT-5.6 Sol

日期：2026-09-03

研究定位：AMRAL 黎曼猜想半自主研究線，第三弧線 method-strength / exponent-drop gate 節點。

本文件是 research source artifact，不是 peer-reviewed publication。

所有 claim 必須依 Claim register、GAP ledger 與 Trust boundary 解讀。
