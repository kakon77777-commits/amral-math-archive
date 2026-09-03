工程紀錄 · 第三弧線 v2.4 · 2026-09-03 · BANDLIMITED_TWIST_GATE · LOCAL_AVERAGE_EQUIVALENCE · RH_CLAIM_FALSE

# Band-limited Twist Averaging Gate 與 Uniform Local-Correlation Frontier

**RH-BandlimitedTwist-AveragingGate v2.4**

本節點承接：

- `RH-MellinSymmetry-PNTFilterBridge v1.9`
- `RH-FilteredPNT-GallagherStrengthAudit v2.0`
- `RH-TwistedLocalCorrelation-ExponentDrop v2.1`
- `RH-ApertureAdmissibility-FalseKappaAudit v2.2`
- `RH-SensitivityNormalized-MultiscaleReconstruction v2.3`

v2.1–v2.3 已把真正 RH-sensitive progress gate 壓成：

$$
\kappa_{\rm corrected}>0,
$$

並排除 shrinking-aperture false-$\kappa$。

v2.4 回到 high-frequency Gallagher / twisted local correlation，處理一個剩餘問題：

> 若偏軸零點在特定 vertical twist 附近共振，是否真的需要對每一個 $\tau\in\mathbb R$ 做 pointwise uniform theorem？

本輪答案：

$$
\boxed{
\text{不需要 pointwise continuum control；
uniform fixed-width twist-band average 已與 pointwise control 同 exponent strength。}
}
$$

原因不是 probabilistic averaging，而是 fixed aperture帶來的**精確 band limitation**。

對 fixed：

$$
h>0,
$$

twisted block energy：

$$
\mathcal Q_{h,\tau}(T)
$$

作為 $\tau$ 的函數，其 Fourier support 包含在：

$$
\boxed{
[-2h,2h].
}
$$

因此：

$$
\boxed{
\sup_{\tau}
\mathcal Q_{h,\tau}(T)
\asymp_h
\sup_{j\in\mathbb Z}
\int_j^{j+1}
\mathcal Q_{h,\tau}(T)\,d\tau
}
$$

在有限性／power-exponent sense，常數只依賴固定 $h$ 與所選 reproducing kernel。

所以 twisted route 的 vertical quantifier可以從 continuum pointwise family壓成：

```text
COUNTABLE UNIT-BAND VARIANCE CERTIFICATES
```

然而 method-strength audit 仍然顯示：

- generic large sieve / Montgomery–Vaughan：$\beta=1$；
- Gallagher：transfer，不提供 missing cancellation；
- Barban–Davenport–Halberstam：平均的是 moduli / residue classes，不是 Mellin twists；
- averaged Hardy–Littlewood / almost-all shift results：目前主要是 logarithmic / subpower saving 或 shift-average control；
- no audited theorem gives:
  $$
  \kappa_{\rm corrected}>0
  $$
  uniformly over all twist bands。

所以 v2.4 改善的是**vertical quantifier geometry與 proof engineering**，不是 RH 本身。

**RH_CLAIM = False.**

---

# 0. Claim register

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE

RELATIVE_TWIST_LOCAL_OBSERVABLE = DEFINED
TWIST_BLOCK_PAIR_FORM = CLOSED
TWIST_BANDLIMIT = CLOSED

UNIFORM_POINTWISE_TO_UNIT_BAND_AVERAGE = CLOSED_AS_BANDLIMITED_EQUIVALENCE
CONTINUUM_TWIST_QUANTIFIER = REDUCED_TO_COUNTABLE_BANDS

GLOBAL_LONG_TWIST_AVERAGE_SUFFICIENT = FALSE
GENERIC_LARGE_SIEVE_EXPONENT = 1
BDH_DIRECT_MELLIN_TWIST_TRANSFER = NOT_AVAILABLE
AVERAGED_HL_FIXED_KAPPA = NOT_AVAILABLE_IN_AUDITED_SOURCES

ANY_CORRECTED_KAPPA_POSITIVE = OPEN
GLOBAL_RH_CERTIFICATE = FALSE
```

---

# 1. Prime–archimedean discrepancy measure

Use the log-coordinate signed measure:

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

For fixed aperture:

$$
h>0,
$$

let:

$$
T_h(v)
=
(h-|v|)_+.
$$

The untwisted local discrepancy is:

$$
\mathfrak E_h(e^t)
=
\int
T_h(t-u)\,d\nu(u).
$$

---

# 2. Relative phase twist

Define the relative twist observable:

$$
\boxed{
\mathcal F_{h,\tau}(t)
=
\int_{\mathbb R}
T_h(t-u)
e^{-i\tau(u-t)}
\,d\nu(u).
}
$$

The factor:

$$
e^{-i\tau(u-t)}
$$

uses frequency relative to the local center $t$ rather than the absolute phase $e^{-i\tau u}$.

This removes a harmless global phase:

$$
\left|
\mathcal F_{h,\tau}(t)
\right|
=
\left|
e^{i\tau t}
\int
T_h(t-u)e^{-i\tau u}d\nu(u)
\right|.
$$

At:

$$
\tau=0,
$$

$$
\boxed{
\mathcal F_{h,0}(t)
=
\mathfrak E_h(e^t).
}
$$

So the untwisted RH-complete observable remains a member of the twisted family.

---

# 3. Finite support in relative log coordinate

For fixed $t$:

$$
T_h(t-u)\neq0
$$

only when:

$$
|u-t|<h.
$$

Set:

$$
v=u-t.
$$

Then:

$$
\boxed{
\mathcal F_{h,\tau}(t)
=
\int_{-h}^{h}
T_h(v)e^{-i\tau v}
\,d\nu_t(v),
}
$$

where $\nu_t$ is the translated local signed measure.

Therefore, as a function of $\tau$:

$$
\boxed{
\mathcal F_{h,\tau}(t)
}
$$

is the Fourier transform of a compactly supported distribution / finite signed measure on:

$$
[-h,h].
$$

It is an entire function of exponential type at most $h$.

---

# 4. Twisted unit-log block energy

Define:

$$
\boxed{
\mathcal Q_{h,\tau}(T)
=
\int_T^{T+1}
\left|
\mathcal F_{h,\tau}(t)
\right|^2dt.
}
$$

For each finite $T$ this is finite and nonnegative.

At:

$$
\tau=0,
$$

it is the v1.7/v1.9 local block energy.

---

# 5. Exact finite-range pair form

Expanding the square:

$$
\begin{aligned}
\mathcal Q_{h,\tau}(T)
&=
\int_T^{T+1}
\iint
T_h(t-u)T_h(t-v)
\\
&\qquad\qquad\times
e^{-i\tau(u-v)}
d\nu(u)d\nu(v)
\,dt.
\end{aligned}
$$

Define:

$$
\boxed{
K_{h,T}(u,v)
=
\int_T^{T+1}
T_h(t-u)T_h(t-v)\,dt.
}
$$

Then:

## Theorem 5.1 · Twisted local covariance

$$
\boxed{
\mathcal Q_{h,\tau}(T)
=
\iint
K_{h,T}(u,v)
e^{-i\tau(u-v)}
d\nu(u)d\nu(v).
}
$$

Since two tents overlap only if:

$$
|u-v|<2h,
$$

we have:

$$
\boxed{
K_{h,T}(u,v)=0
\quad
\text{for }
|u-v|\ge2h.
}
$$

So the twist is the Fourier variable dual to the finite log-ratio difference:

$$
u-v.
$$

---

# 6. Exact twist bandlimit

Theorem 5.1 shows that $\mathcal Q_{h,\tau}(T)$ is the Fourier transform in $\tau$ of a finite signed correlation measure supported on:

$$
[-2h,2h].
$$

Therefore:

## Theorem 6.1 · Twist bandlimit

$$
\boxed{
\operatorname{supp}
\widehat{\mathcal Q_{h,\cdot}(T)}
\subset
[-2h,2h].
}
$$

This is exact.

The bandwidth does not grow with:

- $T$;
- the number of active prime powers;
- the zero ordinate;
- the twist center.

It depends only on the fixed aperture $h$.

---

# 7. Twist-window averaging formula

Let:

$$
W\in L^1(\mathbb R)
$$

be an integrable twist window.

Use:

$$
\widehat W(d)
=
\int_{\mathbb R}
W(\tau)e^{-i\tau d}\,d\tau.
$$

Then:

$$
\boxed{
\begin{aligned}
&
\int_{\mathbb R}
W(\tau-\tau_0)
\mathcal Q_{h,\tau}(T)
\,d\tau
\\
&=
\iint
K_{h,T}(u,v)
e^{-i\tau_0(u-v)}
\widehat W(u-v)
\,d\nu(u)d\nu(v).
\end{aligned}
}
$$

Thus twist averaging inserts a deterministic taper:

$$
\widehat W(u-v)
$$

into the local log-ratio correlation.

This is the exact Gallagher / large-sieve method interface.

---

# 8. Wide twist windows localize log-ratio differences

If:

$$
W_U(\tau)
=
W(\tau/U),
$$

then:

$$
\widehat W_U(d)
=
U\widehat W(Ud).
$$

As $U$ grows, the factor becomes concentrated at:

$$
|d|
\lesssim
\frac1U.
$$

For prime powers:

$$
m,n\asymp X,
$$

$$
d
=
\log\frac mn
\approx
\frac{m-n}{X}.
$$

Therefore wide twist averaging isolates additive shifts:

$$
\boxed{
|m-n|
\lesssim
\frac XU.
}
$$

This recovers the v2.1 Gallagher scale:

$$
H
\asymp
\frac XU.
$$

---

# 9. Bandlimited reproducing lemma

Let:

$$
q(\tau)\ge0
$$

be continuous, with:

$$
\operatorname{supp}\widehat q
\subset[-B,B].
$$

Choose:

$$
\phi\in\mathcal S(\mathbb R)
$$

such that:

$$
\widehat\phi(\xi)=1
$$

on a neighbourhood of:

$$
[-B,B].
$$

Then:

$$
\boxed{
q=q\ast\phi.
}
$$

Define the unit-band mass:

$$
\boxed{
M(q)
=
\sup_{j\in\mathbb Z}
\int_j^{j+1}
q(\tau)\,d\tau.
}
$$

Because $\phi$ is Schwartz, the constant:

$$
C_\phi
=
\sup_{x\in\mathbb R}
\sum_{j\in\mathbb Z}
\sup_{s\in[j,j+1]}
|\phi(x-s)|
$$

is finite.

Therefore:

$$
\begin{aligned}
q(x)
&\le
\int q(s)|\phi(x-s)|ds
\\
&\le
M(q)C_\phi.
\end{aligned}
$$

Hence:

$$
\boxed{
\sup_{\tau}q(\tau)
\le
C_\phi
\sup_{j\in\mathbb Z}
\int_j^{j+1}q(\tau)d\tau.
}
$$

Conversely:

$$
\boxed{
\int_j^{j+1}q(\tau)d\tau
\le
\sup_\tau q(\tau).
}
$$

So pointwise and unit-band average bounds are equivalent up to a fixed constant depending only on the bandwidth.

---

# 10. Apply the reproducing lemma to the twisted energy

Set:

$$
q_T(\tau)
=
\mathcal Q_{h,\tau}(T).
$$

By Theorem 6.1:

$$
B=2h
$$

is fixed.

Therefore:

## Theorem 10.1 · Unit-band twist equivalence

$$
\boxed{
\sup_{\tau\in\mathbb R}
\mathcal Q_{h,\tau}(T)
\asymp_h
\sup_{j\in\mathbb Z}
\int_j^{j+1}
\mathcal Q_{h,\tau}(T)d\tau.
}
$$

The equivalence is in the sense of two-sided fixed multiplicative constants.

Thus any power-exponent estimate on one side transfers unchanged to the other.

---

# 11. Continuum twist quantifier becomes countable

A theorem of the form:

$$
\boxed{
\sup_{j\in\mathbb Z}
\int_j^{j+1}
\mathcal Q_{h,\tau}(T)d\tau
\ll
e^{(1-\kappa)T+o(T)}
}
$$

implies:

$$
\boxed{
\sup_{\tau}
\mathcal Q_{h,\tau}(T)
\ll_h
e^{(1-\kappa)T+o(T)}.
}
$$

In particular:

$$
\tau=0
$$

satisfies the same bound, so v2.1 gives the corresponding fixed zero strip.

Therefore the twisted vertical requirement can be organized as:

```text
j = ...,-2,-1,0,1,2,...
```

unit-band certificates.

This is countable, though still infinite.

---

# 12. Why one global long twist average is not enough

Suppose one only proves:

$$
\int_{-V}^{V}
\mathcal Q_{h,\tau}(T)d\tau
\le
\mathcal B(T,V).
$$

If:

$$
V\to\infty,
$$

this allows a finite number of fixed-width resonance bands to have much larger local mass than the global average.

Band limitation prevents infinitely narrow spikes, but it does not prevent finitely many width-$O_h(1)$ exceptional bands.

Therefore:

$$
\boxed{
\text{global average over an expanding twist range}
\not\Longrightarrow
\text{uniform unit-band control}.
}
$$

What is needed is either:

1. uniform local averages in every twist center; or
2. a positive global mechanism that rules out every exceptional band.

---

# 13. Resonance interpretation

For the phase-twisted tent family, define:

$$
B_h(z)
=
2
\frac{\cosh(hz)-1}{z^2}.
$$

A hypothetical zero:

$$
\rho
=
\frac12+\delta+i\gamma
$$

contributes a mode proportional to:

$$
\boxed{
-
B_h
\left(
\delta+i(\gamma-\tau)
\right)
X^{\delta+i(\gamma-\tau)}.
}
$$

At:

$$
\tau=\gamma,
$$

the vertical phase is removed:

$$
\boxed{
-
B_h(\delta)X^\delta.
}
$$

So the unit band containing $\gamma$ is the natural resonance band for that zero.

Band limitation says that this resonance is a finite-width spectral phenomenon, not a delta spike.

---

# 14. Generic large-sieve / Montgomery–Vaughan barrier

For a fixed local arithmetic center:

$$
X=e^T,
$$

the twisted prime sum is a Dirichlet polynomial with frequencies:

$$
\log n,
$$

for:

$$
n\asymp_h X.
$$

The smallest adjacent log spacing is:

$$
\log(n+1)-\log n
\asymp
\frac1X.
$$

A generic nonharmonic large-sieve / Montgomery–Vaughan estimate over a unit twist interval therefore carries a spacing constant of size:

$$
\boxed{
X.
}
$$

For natural coefficients:

$$
a_n
\asymp
\frac{\Lambda(n)}{\sqrt n}
\times
\text{bounded aperture weight},
$$

the local coefficient square mass is:

$$
\boxed{
\sum_{n\asymp_h X}|a_n|^2
\asymp_h
\log X
}
$$

at leading scale.

Thus generic mean value gives:

$$
\boxed{
\int_j^{j+1}
\left|
\sum a_n n^{-i\tau}
\right|^2d\tau
\ll_h
X\operatorname{polylog}X.
}
$$

That is:

$$
\boxed{
\beta=1.
}
$$

Centering by the deterministic main term does not create cancellation inside a generic coefficient-blind inequality.

So generic large sieve still does not give:

$$
\kappa>0.
$$

---

# 15. Barban–Davenport–Halberstam audit

Barban–Davenport–Halberstam theorems control variance over:

- moduli $q$;
- residue classes $a$.

Modern forms and short-interval analogues are powerful tools for prime distribution in arithmetic progressions.

But the v2.4 twisted variable is a continuous Mellin character:

$$
n^{-i\tau},
$$

and its pair phase is:

$$
\left(\frac nm\right)^{-i\tau}.
$$

This is not a Dirichlet character modulo $q$.

No direct identity converts a standard BDH modulus average into the required uniform Mellin twist-band bound.

Therefore:

```text
BDH = IMPORTANT DISTRIBUTION INPUT
BDH = NOT A DIRECT V2.4 CLOSURE THEOREM
```

Any proposed use requires an additional transform / dispersion argument.

---

# 16. Current averaged Hardy–Littlewood correlation audit

Current unconditional work proves strong average forms of Hardy–Littlewood / Chowla-type correlations over shifts and higher-uniformity statements for $\Lambda$.

The savings appearing in audited results are primarily:

- logarithmic;
- subpower;
- average over shifts;
- almost-all over interval positions.

These are major results.

But a fixed positive v2.4 $\kappa$ would imply a new fixed zero strip.

No audited unconditional result supplies the necessary:

$$
\boxed{
X^{-\kappa}
}
$$

power saving with:

- sensitivity-normalized aperture;
- centered main term;
- uniform unit twist-band control.

So:

$$
\boxed{
\kappa_{\rm corrected}=0
}
$$

remains the audited state.

---

# 17. 2026 prime-pair error work

Chou, Haag, Huryn, and Ledoan relate the error term in Hardy–Littlewood prime-pair counting to the $L^1$ norm of a von-Mangoldt prime exponential sum.

This is relevant because it further confirms the structural bridge:

```text
PRIME-PAIR ERROR
<->
EXPONENTIAL-SUM NORM.
```

However the result is a relation between quantities; it does not by itself supply the uniform fixed-power bound required by v2.4.

So it is another method/interface result rather than the missing $\kappa>0$ theorem.

---

# 18. Current method-strength table

| Method | What it controls | v2.4 limitation | Audited fixed-power class |
|---|---|---|---:|
| Generic Montgomery–Vaughan / large sieve | twist mean square | spacing / diagonal $X$ barrier | $\beta=1$ |
| Gallagher / Cesàro | spectral ↔ local weighted square | transfer only | no $\kappa$ alone |
| BDH / Montgomery–Hooley | moduli / residue-class variance | not Mellin twist family | no direct $\kappa$ |
| Averaged Hardy–Littlewood shifts | averaged prime correlations | log/subpower + averaging | $\kappa=0$ |
| Almost-all short intervals | most positions | sparse exceptions allowed | no rightmost-zero exclusion |
| Uniform twisted unit-band power saving | exactly needed object | currently open | $\kappa>0$ would be progress |

---

# 19. Logical minimum versus methodological twisted target

It is important not to overstate the need for twists.

### Logical minimum

The untwisted block:

$$
\mathcal Q_{h,0}(T)
$$

alone is already RH-complete through v1.7.

So a theorem:

$$
\boxed{
\mathcal Q_{h,0}(T)
\ll
e^{(1-\kappa)T+o(T)}
}
$$

would already give a fixed zero strip.

### Methodological twisted target

Twists are introduced because:

- Gallagher is spectral;
- resonance can isolate vertical frequencies;
- pair-correlation tools naturally use Fourier / Mellin phase.

For this route the safe averaged target is:

$$
\boxed{
\sup_j
\int_j^{j+1}
\mathcal Q_{h,\tau}(T)d\tau
\ll
e^{(1-\kappa)T+o(T)}.
}
$$

This is stronger than the logical minimum but better matched to available analytic tools.

---

# 20. New smallest twisted GAP

Fix:

$$
h=\log2.
$$

Find any:

$$
\boxed{
\kappa>0
}
$$

such that:

$$
\boxed{
\sup_{j\in\mathbb Z}
\int_j^{j+1}
\int_T^{T+1}
\left|
\mathcal F_{h,\tau}(t)
\right|^2
dt\,d\tau
\ll
e^{(1-\kappa)T+o(T)}.
}
$$

By Theorem 10.1 this gives pointwise twist control of the same exponent.

By taking:

$$
\tau=0,
$$

v2.1 then gives:

$$
\boxed{
\left|
\Re\rho-\frac12
\right|
\le
\frac{1-\kappa}{2}.
}
$$

This is the canonical v2.4 fixed-strip target.

---

# 21. Pair-correlation formulation of the GAP

Using Theorem 7.1 with a fixed nonnegative unit-band window $W$:

$$
\boxed{
\begin{aligned}
&
\int
W(\tau-\tau_0)
\mathcal Q_{h,\tau}(T)d\tau
\\
&=
\iint
K_{h,T}(u,v)
e^{-i\tau_0(u-v)}
\widehat W(u-v)
d\nu(u)d\nu(v).
\end{aligned}
}
$$

Therefore the missing theorem is equivalently a uniform bound for a centered finite-range log-ratio covariance with phase:

$$
\boxed{
e^{-i\tau_0(u-v)}.
}
$$

This is now the exact arithmetic object to hand to:

- dispersion methods;
- averaged Hardy–Littlewood machinery;
- bilinear forms;
- large-sieve refinements.

No further conceptual translation is needed.

---

# 22. Certificate architecture

The vertical dimension can now be represented as unit bands:

```text
twist_band_id = integer j
twist_interval = [j, j+1]

t_block_id = integer T-block
t_interval = [T, T+1]

aperture = fixed h

local_prime_cutoff
centered_main_normalization
band_energy_interval

sensitivity_normalized = true
kappa_candidate
source_hash
implementation_hash
```

Research agents may scan finite rectangles:

$$
|j|\le J,
\qquad
T\le T_{\max},
$$

but finite scanning remains evidence only.

A theorem still has to close all:

$$
j\in\mathbb Z,
\qquad
T\to\infty.
$$

---

# 23. GAP ledger

## CLOSED / REDUCED

### G1. Twisted finite-range pair form

```text
CLOSED
```

### G2. Twist bandwidth

```text
CLOSED
```

$$
[-2h,2h].
$$

### G3. Pointwise / unit-band exponent equivalence

```text
CLOSED
```

### G4. Continuum twist to countable bands

```text
CLOSED_AS_REDUCTION
```

### G5. Generic large-sieve class

```text
AUDITED
```

$$
\beta=1.
$$

### G6. BDH direct applicability

```text
NOT_DIRECT
```

---

## OPEN

### G7. Uniform unit-band fixed saving

```text
OPEN
```

$$
\kappa>0.
$$

### G8. Centered phase-twisted pair correlation theorem

```text
OPEN
```

### G9. First fixed zero-strip breakthrough

```text
OPEN
```

### G10. $\kappa=1$

```text
OPEN_RH_COMPLETE
```

### G11. RH

```text
OPEN
```

---

# 24. Trust boundary

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE

TWIST_BANDLIMIT = EXACT
UNIT_BAND_REDUCTION = EXACT_AT_STRENGTH_LEVEL

GLOBAL_TWIST_AVERAGE != UNIFORM_LOCAL_AVERAGE
GENERIC_LARGE_SIEVE != ARITHMETIC_CANCELLATION

NO POSITIVE CORRECTED KAPPA HAS BEEN PROVED

GLOBAL_RH_CERTIFICATE = FALSE
```

Forbidden:

$$
\int_{-V}^{V}\mathcal Q\,d\tau
\text{ small on average}
\Longrightarrow
\sup_\tau\mathcal Q
\text{ small}.
$$

Forbidden:

$$
\text{BDH variance}
\Longrightarrow
\text{Mellin twist variance}
$$

without a proved bridge.

Forbidden:

$$
\text{finite number of twist bands checked}
\Longrightarrow
\text{global vertical theorem}.
$$

---

# 25. One-line status

> v2.4 turns the vertical twist problem into a fixed-bandwidth harmonic-analysis problem. For fixed aperture $h$, the relative twisted observable is the Fourier transform of a local signed measure supported in $[-h,h]$, so its unit-log block energy $\mathcal Q_{h,\tau}(T)$ has twist Fourier support exactly inside $[-2h,2h]$. A Schwartz reproducing-kernel argument then shows that uniform pointwise twist bounds and uniform unit-band twist-average bounds are equivalent up to fixed $h$-dependent constants; the continuum vertical quantifier can therefore be organized as countably many integer twist-band certificates. Twist-window averaging inserts the Fourier taper $\widehat W(u-v)$ into the finite-range log-ratio covariance, giving an exact Gallagher/large-sieve interface. However generic Montgomery–Vaughan / large-sieve estimates still hit the $X=e^T$ spacing barrier and remain in energy class $\beta=1$; BDH controls a different character family; current averaged Hardy–Littlewood and almost-all short-interval results do not provide a uniform sensitivity-normalized $X^{-\kappa}$ saving over every twist band. The smallest twisted fixed-strip target is now explicit: for fixed $h=\log2$, prove any $\kappa>0$ in the uniform unit-band double mean square. No such positive corrected $\kappa$ has yet been obtained in this research line.

---

# 26. References

1. Giovanni Coppola, Maurizio Laporta, **A modified Gallagher's Lemma**, arXiv:1301.0008.  
   https://arxiv.org/abs/1301.0008

2. Giovanni Coppola, Maurizio Laporta, **A generalization of Gallagher's lemma for exponential sums**, arXiv:1411.1739.  
   https://arxiv.org/abs/1411.1739

3. Alessandro Languasco, Alberto Perelli, Alessandro Zaccagnini, **Explicit relations between pair correlation of zeros and primes in short intervals**, *Journal of Mathematical Analysis and Applications* 394 (2012), 761–771.  
   DOI: https://doi.org/10.1016/j.jmaa.2012.04.058

4. H. L. Montgomery and R. C. Vaughan, classical mean-value theorem for Dirichlet polynomials.

5. Adam J. Harper, **Simple Barban–Davenport–Halberstam type asymptotics for general sequences**, *Journal of the London Mathematical Society* (2025).  
   DOI: https://doi.org/10.1112/jlms.70293

6. Glyn Harman, **The Montgomery–Hooley theorem in short intervals**, *Mathematika* 59 (2013), 129–139.  
   DOI: https://doi.org/10.1112/S0025579312001052

7. Kaisa Matomäki, Maksym Radziwiłł, Xuancheng Shao, Terence Tao, Joni Teräväinen, **Higher uniformity of arithmetic functions in short intervals II. Almost all intervals**, *Inventiones mathematicae* 244 (2026), 967–1091.  
   DOI: https://doi.org/10.1007/s00222-026-01408-6

8. Leon Chou, Summer Haag, Jake Huryn, Andrew Ledoan, **The error term in counting prime pairs**, *Journal of Number Theory* 278 (2026), 422–450.  
   DOI: https://doi.org/10.1016/j.jnt.2025.04.009

9. AMRAL, **RH-TwistedLocalCorrelation-ExponentDrop v2.1**.

10. AMRAL, **RH-SensitivityNormalized-MultiscaleReconstruction v2.3**.

---

# 27. Provenance

研究主導：Neo.K

v2.4 bandlimited-twist reduction、unit-band averaging equivalence、pair-covariance interface、method-strength audit 與 canonical source 整理：ChatGPT / GPT-5.6 Sol

日期：2026-09-03

研究定位：AMRAL 黎曼猜想半自主研究線，第三弧線 bandlimited vertical averaging / twisted local covariance 節點。

本文件是 research source artifact，不是 peer-reviewed publication。

所有 claim 必須依 Claim register、GAP ledger 與 Trust boundary 解讀。
