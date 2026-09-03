工程紀錄 · 第三弧線 v2.1 · 2026-09-03 · VARIANCE_SAVING_CONVERTER · TWISTED_LOCAL_CORRELATION_GATE · RH_CLAIM_FALSE

# Twisted Local Correlation、Selberg Variance Saving 與 Fixed-Strip Exponent Drop

**RH-TwistedLocalCorrelation-ExponentDrop v2.1**

本節點承接：

- `RH-LocalPrime-MeanEnergyBridge v1.7`
- `RH-MellinSymmetry-PNTFilterBridge v1.9`
- `RH-FilteredPNT-GallagherStrengthAudit v2.0`

v2.0 已把目前已知方法的 strength 壓成 energy exponent：

$$
Q_h(T)
\lesssim
e^{\beta T+o(T)},
$$

其中：

$$
\boxed{
\beta
=
2
\sup_\rho
\left|
\Re\rho-\frac12
\right|.
}
$$

目前無條件技術停在：

$$
\beta=1,
$$

而 RH 對應：

$$
\beta=0.
$$

v2.1 不再建立新的 RH criterion，而做三件事：

1. 用 classical PNT mean-square / Selberg inverse theory 外部驗證 AMRAL 的 exponent progress meter；
2. 建立「variance fixed power saving $\kappa$ $\to$ energy exponent drop $\kappa$」的尺度轉換；
3. 明確定義 high-frequency Gallagher 真正需要的 phase-twisted local arithmetic object。

本輪最重要的結論：

$$
\boxed{
\text{若某個 centered local variance 相對自然尺度 }
XH^2
\text{ 有固定 }X^{-\kappa}
\text{ power saving，}
}
$$

則在 AMRAL strength scale 上：

$$
\boxed{
\beta\le1-\kappa.
}
$$

因此：

$$
\boxed{
\left|
\Re\rho-\frac12
\right|
\le
\frac{1-\kappa}{2}.
}
$$

所以第一個 genuine fixed-strip breakthrough 的最小 arithmetic content，就是任何：

$$
\boxed{
\kappa>0.
}
$$

現有無條件 almost-all short-interval results 通常只給：

$$
o(XH^2)
$$

或 logarithmic / subpower saving，對應：

$$
\kappa=0
$$

at fixed-power scale，因此仍不會使：

$$
\beta<1.
$$

**RH_CLAIM = False.**

---

# 0. Claim register

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE

CLASSICAL_MEANSQUARE_EXPONENT_ALIGNMENT = REFERENCE_VALIDATED
ZACCAGNINI_INVERSE_SCALE_ALIGNMENT = REFERENCE_VALIDATED

VARIANCE_POWER_SAVING_TO_ENERGY_DROP = CLOSED_AS_STRENGTH_CONVERTER
SUBPOWER_SAVING_TO_FIXED_STRIP = FALSE

TWISTED_TENT_MAIN_TERM = CLOSED
HIGH_FREQUENCY_GALLAGHER_REQUIRES_PHASE_TWIST = CLOSED_AS_METHOD_DIAGNOSIS

VERTICAL_AVERAGE_REPLACES_VERTICAL_SUPREMUM = FALSE
ZERO_DENSITY_REPLACES_RIGHTMOST_ZERO_CONTROL = FALSE

ANY_KAPPA_POSITIVE = FIRST_FIXED_STRIP_GATE
KAPPA_ONE = RH_EXPONENT_GATE

GLOBAL_KAPPA_POSITIVE = OPEN
GLOBAL_RH_CERTIFICATE = FALSE
```

---

# 1. Classical rightmost-zero parameter

Define:

$$
\boxed{
\Theta
=
\sup_\rho
\Re\rho.
}
$$

By functional-equation symmetry:

$$
\Theta
\in
\left[
\frac12,1
\right].
$$

The AMRAL horizontal displacement is:

$$
\Delta_\zeta
=
\Theta-\frac12.
$$

Therefore:

$$
\boxed{
\beta
=
2\Delta_\zeta
=
2\Theta-1.
}
$$

---

# 2. Classical PNT mean-square exponent

Let:

$$
E(x)=\psi(x)-x,
$$

and:

$$
\boxed{
I(X)
=
\int_X^{2X}
|E(x)|^2dx.
}
$$

A modern statement of the classical mean-square size is:

if:

$$
\Theta=\frac12,
$$

then:

$$
I(X)\asymp X^2.
$$

If:

$$
\Theta>\frac12,
$$

then for every:

$$
\varepsilon>0,
$$

$$
\boxed{
X^{2\Theta+1-\varepsilon}
\ll
I(X)
\ll
X^{2\Theta+1}.
}
$$

Hence define the dyadic PNT mean-square exponent:

$$
\boxed{
\delta_I
=
\limsup_{X\to\infty}
\frac{
\log I(X)
}{
\log X
}.
}
$$

Then:

$$
\boxed{
\delta_I
=
2\Theta+1.
}
$$

Consequently:

$$
\boxed{
\beta
=
\delta_I-2.
}
$$

Thus the AMRAL energy-exponent scale is exactly the classical mean-square exponent after critical normalization.

---

# 3. External inverse-theory confirmation

Zaccagnini studies the Selberg integral:

$$
J(x,\vartheta)
=
\int_x^{2x}
\left|
\psi(t)
-
\psi((1-\vartheta)t)
-
\vartheta t
\right|^2dt.
$$

At:

$$
\vartheta=1,
$$

this is essentially:

$$
J(x,1)=I(x)
$$

up to the harmless lower-end convention.

Zaccagnini explicitly proves the inverse implication:

if:

$$
\boxed{
J(x,1)\ll x^\delta
}
$$

for:

$$
2\le\delta\le3,
$$

then:

$$
\boxed{
\Theta
\le
\frac{\delta-1}{2}.
}
$$

Set:

$$
\delta=3-\kappa.
$$

Then:

$$
\Theta
\le
1-\frac{\kappa}{2}.
$$

Therefore:

$$
\boxed{
\beta
=
2\Theta-1
\le
1-\kappa.
}
$$

This is exactly the v2.0 AMRAL exponent-drop rule.

So the progress scale is not an artifact of the fixed-aperture reformulation; it is aligned with classical inverse Selberg theory.

---

# 4. Variance power-saving parameter

For a local additive interval length:

$$
H,
$$

the natural uncentered variance scale is:

$$
\boxed{
XH^2.
}
$$

Write a hypothetical centered Selberg / symmetry bound as:

$$
\boxed{
J_{\rm loc}(X,H)
\ll
XH^2
X^{-\kappa+o(1)}.
}
$$

Interpret:

### $\kappa=0$

Only subpower / logarithmic / $o(1)$ relative saving.

No fixed exponent improvement.

### $0<\kappa<1$

A true fixed power saving.

This is the first fixed-strip regime.

### $\kappa=1$

Variance reaches the scale:

$$
XH
\times
\text{subpower factors},
$$

which is the Selberg/RH-type square-root variance scale when $H$ is a fixed power or fixed fraction of $X$.

At fixed multiplicative aperture this corresponds to energy exponent zero.

---

# 5. Gallagher scale conversion

Take a spectral averaging width:

$$
U.
$$

Gallagher's principle associates it with frequency aperture:

$$
\Delta(\log n)
\asymp
\frac1U.
$$

At arithmetic size:

$$
n\asymp X,
$$

this corresponds to additive interval length:

$$
\boxed{
H
\asymp
\frac{X}{U}.
}
$$

For critical coefficients of size:

$$
\frac{\Lambda(n)}{\sqrt n},
$$

the local squared sum acquires a factor:

$$
X^{-1},
$$

and:

$$
d(\log x)
=
\frac{dx}{x}
$$

adds another:

$$
X^{-1}.
$$

Thus the natural Gallagher-transferred spectral square scale is:

$$
\boxed{
\frac{U^2}{X^2}
J_{\rm loc}(X,H).
}
$$

Substitute:

$$
H=\frac XU.
$$

If:

$$
J_{\rm loc}(X,H)
\ll
XH^2X^{-\kappa+o(1)},
$$

then:

$$
\begin{aligned}
\frac{U^2}{X^2}
J_{\rm loc}(X,H)
&\ll
\frac{U^2}{X^2}
\left[
X
\frac{X^2}{U^2}
X^{-\kappa+o(1)}
\right]
\\
&=
\boxed{
X^{1-\kappa+o(1)}.
}
\end{aligned}
$$

The spectral-window exponent cancels.

This is the v2.1 variance-saving converter.

---

# 6. Scale-invariance of the power-saving gate

The cancellation in Section 5 means:

$$
\boxed{
\text{fixed power saving }\kappa
\text{ is the invariant quantity,}
}
$$

not the particular choice of:

$$
H
$$

or:

$$
U.
$$

At strength level:

$$
\boxed{
\kappa
\longleftrightarrow
1-\beta.
}
$$

So choosing a clever short-interval exponent does not by itself create fixed-strip progress.

A method must produce a true fixed power saving relative to its natural variance scale.

---

# 7. Current unconditional Selberg scale

Classical unconditional work gives, in a broad range of relative interval sizes:

$$
\boxed{
J(X,\vartheta)
=
o(X^3\vartheta^2).
}
$$

For example the known almost-all short-interval range includes:

$$
\vartheta
\ge
X^{-5/6+\varepsilon}
$$

in the classical formulation.

Since:

$$
H=\vartheta X,
$$

the natural scale is:

$$
X^3\vartheta^2
=
XH^2.
$$

Thus the known result is:

$$
\boxed{
J=o(XH^2).
}
$$

This is a genuine asymptotic improvement.

But at fixed-power scale it only says:

$$
\kappa=0.
$$

An $o(1)$ factor is not the same as:

$$
X^{-\kappa}
$$

for any fixed:

$$
\kappa>0.
$$

Therefore it does not imply:

$$
\beta<1.
$$

---

# 8. RH Selberg scale as the opposite endpoint

Under RH, Selberg's strong bound has the shape:

$$
\boxed{
J(X,\vartheta)
\ll
X^2\vartheta
\log^2\left(
\frac2\vartheta
\right).
}
$$

Since:

$$
H=\vartheta X,
$$

this is:

$$
\boxed{
J
\ll
XH
\log^2\left(
\frac XH
\right).
}
$$

Relative to:

$$
XH^2,
$$

the saving is approximately:

$$
H^{-1}.
$$

If:

$$
H=X^{a+o(1)},
$$

this corresponds to:

$$
\kappa=a.
$$

In particular, for a fixed multiplicative aperture:

$$
H\asymp X,
$$

we have:

$$
a=1,
$$

hence:

$$
\kappa=1
$$

and:

$$
\beta=0.
$$

This matches RH.

---

# 9. Subpower Gallagher resolution

A particularly useful regime for v2.1 is:

$$
\boxed{
U=X^{o(1)}.
}
$$

For example:

$$
U=(\log X)^A.
$$

Then:

$$
H=\frac XU
=
X^{1-o(1)}.
$$

The associated log aperture:

$$
\frac1U
$$

shrinks only subexponentially in:

$$
T=\log X.
$$

By the v1.8 aperture-sensitivity theorem, such subexponential shrinkage does **not** alter the fixed exponential type of an off-axis mode.

Therefore this regime simultaneously gives:

- enough spectral averaging to use Gallagher machinery;
- no loss in horizontal exponent sensitivity.

---

# 10. What current unconditional variance becomes at subpower resolution

Take:

$$
U=X^{o(1)},
$$

$$
H=X/U.
$$

If current unconditional theory only gives:

$$
J=o(XH^2),
$$

then the transferred spectral scale is:

$$
\frac{U^2}{X^2}J
=
o(X).
$$

This is:

$$
\boxed{
X^{1-o_{\rm weak}(1)}
}
$$

in fixed-power language.

It still has:

$$
\beta=1.
$$

By contrast, the RH Selberg scale:

$$
J\ll XH\operatorname{polylog}X
$$

transfers to:

$$
\boxed{
U\operatorname{polylog}X
=
X^{o(1)},
}
$$

which is:

$$
\beta=0.
$$

So the two endpoint regimes are sharply separated.

---

# 11. Fixed-power variance saving is the first qualitative transition

Suppose for some:

$$
\kappa>0
$$

one proves at a subpower Gallagher resolution:

$$
\boxed{
J_{\rm loc}(X,X/U)
\ll
X
\left(
\frac XU
\right)^2
X^{-\kappa+o(1)}.
}
$$

Then Section 5 gives:

$$
\boxed{
\text{transferred energy}
\ll
X^{1-\kappa+o(1)}.
}
$$

The v2.0 / Zaccagnini inverse scale then gives:

$$
\boxed{
\Theta
\le
1-\frac{\kappa}{2}.
}
$$

and:

$$
\boxed{
\left|
\Re\rho-\frac12
\right|
\le
\frac{1-\kappa}{2}.
}
$$

Thus **any fixed $\kappa>0$** is a genuine fixed-strip breakthrough.

---

# 12. Exact phase-twisted local tent observable

To use a high-frequency Gallagher window centered near:

$$
\tau,
$$

the local arithmetic object is not the untwisted scalar discrepancy.

Define:

$$
\boxed{
\begin{aligned}
\mathfrak E_{h,\tau}(x)
&=
\sum_{
xe^{-h}<n<xe^h
}
\frac{\Lambda(n)}{\sqrt n}
\left(
h-\left|\log\frac nx\right|
\right)
n^{-i\tau}
\\
&\quad
-
x^{1/2-i\tau}
A_h(\tau),
\end{aligned}
}
$$

where:

$$
\boxed{
A_h(\tau)
=
\int_{-h}^{h}
T_h(v)
e^{-(1/2-i\tau)v}
dv.
}
$$

Because $T_h$ is even:

$$
\boxed{
A_h(\tau)
=
2
\frac{
\cosh((1/2-i\tau)h)-1
}{
(1/2-i\tau)^2
}.
}
$$

At:

$$
\tau=0,
$$

$$
A_h(0)
=
8
\left(
\cosh\frac h2-1
\right),
$$

recovering exactly the v1.6 main term.

---

# 13. Why the phase twist is unavoidable at high spectral center

If one studies a spectral window around:

$$
\tau_0,
$$

then:

$$
S(\tau+\tau_0)
$$

replaces each logarithmic frequency coefficient by:

$$
e^{-i\tau_0\log n}
=
n^{-i\tau_0}.
$$

Therefore every high-frequency Gallagher reduction produces a local sum of the form:

$$
\boxed{
\Lambda(n)
n^{-1/2-i\tau_0}
\times
\text{local weight}.
}
$$

So the correct arithmetic frontier is not merely:

```text
LOCAL PRIME COUNT
```

but:

```text
PHASE-TWISTED LOCAL PRIME CORRELATION.
```

---

# 14. Twisted second moment

For a fixed log block:

$$
t\in[T,T+1],
$$

define:

$$
\boxed{
\mathcal Q_{h,\tau}(T)
=
\int_T^{T+1}
\left|
\mathfrak E_{h,\tau}(e^t)
\right|^2dt.
}
$$

Expanding the prime–prime part produces phases:

$$
\boxed{
\left(
\frac nm
\right)^{-i\tau}.
}
$$

Thus the off-diagonal covariance is a Mellin/Fourier transform of the local log-ratio pair distribution.

This is the arithmetic object that can potentially interact with:

- Gallagher;
- large sieve;
- prime-pair correlations;
- Dirichlet-polynomial mean value;
- dispersion methods.

---

# 15. Vertical averaging is not enough by itself

The rightmost-zero parameter is:

$$
\Theta
=
\sup_\rho\Re\rho.
$$

A single zero at:

$$
\rho_0
=
\frac12+\delta+i\gamma_0
$$

already forces the horizontal exponent:

$$
\Delta_\zeta\ge\delta.
$$

Therefore a theorem that only controls:

```text
average over many vertical twist centers
```

can miss a sparse exceptional vertical block.

To infer a fixed zero strip one needs, in some equivalent form:

```text
uniform vertical-block control
```

or a theorem that rules out every exceptional block.

This is the same reason zero-density information alone cannot replace fixed zero-free-strip information.

---

# 16. External inverse-theory strength gate

Zaccagnini's 2000 inverse theorem is even more general.

He assumes bounds of the form:

$$
\boxed{
J(x,\vartheta)
\ll
\frac{
x^3\vartheta^2
}{
F(\vartheta x)
}
}
$$

uniformly for:

$$
G(x)^{-1}
\le
\vartheta
\le
1.
$$

He then derives zero-density and zero-free consequences depending on the strength of:

$$
F
$$

and the uniformity range:

$$
G.
$$

In particular:

- logarithmic/subpower $F$ recovers classical shrinking zero-free regions;
- a true fixed power $F(y)\asymp y^\kappa$ moves into fixed-power territory;
- the special $\vartheta=1$ argument directly gives the fixed-strip exponent relation.

Thus v2.1 is best viewed as a fixed-aperture / Gallagher-coordinate realization of a classical inverse-theory principle.

---

# 17. Method-strength classification

Every proposed correlation estimate should now be reduced to:

$$
\boxed{
\kappa
=
\liminf_{X\to\infty}
\frac{
\log
\left[
XH^2/J_{\rm loc}(X,H)
\right]
}{
\log X
}.
}
$$

Then:

### $\kappa=0$

No fixed-strip progress.

### $0<\kappa<1$

Genuine fixed zero-strip progress.

### $\kappa=1$

RH energy class.

This is the v2.1 arithmetic progress parameter.

---

# 18. Why logarithmic improvements are still useful but not qualitative

Suppose:

$$
J_{\rm loc}
\ll
\frac{
XH^2
}{
(\log X)^A
}.
$$

Then:

$$
\kappa=0.
$$

So no fixed strip follows.

Nevertheless such improvements can still:

- improve explicit finite-height bounds;
- lower numerical certificate cost;
- improve zero-density constants;
- improve PNT error subexponential factors.

They are real progress, but not an exponent-class transition.

---

# 19. Minimal v2.2 target

The smallest genuinely new theorem target can now be written without RH language.

Find any:

$$
\boxed{
\kappa>0
}
$$

and one admissible local/twisted correlation framework such that:

$$
\boxed{
J_{\rm centered}(X,H)
\ll
XH^2
X^{-\kappa+o(1)}
}
$$

uniformly in the parameters needed by the Mellin/Gallagher transfer.

The required uniformity includes whichever vertical twist centers are needed to prevent sparse off-axis exceptions.

If proved, this would imply a new fixed zeta zero strip.

No attempt should be labeled progress toward v2.2 unless its translated $\kappa$ is strictly positive.

---

# 20. Candidate arithmetic forms

Possible candidate inputs include:

### A. Weighted Selberg variance

$$
J_{w,\Lambda}(X,H).
$$

### B. Symmetry integral

$$
I_\Lambda(X,H).
$$

### C. Phase-twisted Cesàro variance

$$
J_{w,\Lambda,\tau}(X,H).
$$

### D. Finite-range log-ratio covariance

$$
\sum_{m,n}
\frac{
\Lambda(m)\Lambda(n)
}{
\sqrt{mn}
}
W
\left(
\log\frac mn
\right)
\left(
\frac mn
\right)^{-i\tau}
-
\text{renormalized main}.
$$

The last form is closest to v1.7–v1.9.

---

# 21. What current literature already says

Current unconditional almost-all short-interval theory gives impressive results, including:

$$
J=o(XH^2)
$$

in large ranges of $H$.

Modern higher-uniformity results for $\Lambda$ give strong almost-all estimates for additive intervals as short as powers around:

$$
X^{1/3+\varepsilon}
$$

for certain structured tests.

But these remain:

- almost-all rather than every vertical/spectral obstruction;
- subpower/logarithmic in the fixed exponent classification;
- not a fixed positive $\kappa$ theorem for the RH-complete centered variance.

Thus the v2.1 gate remains open.

---

# 22. Numerical / computational role

Finite computation can assist by:

1. measuring empirical:

$$
\kappa_{\rm eff}(X)
=
\frac{
\log[
XH^2/J(X,H)
]
}{
\log X
};
$$

2. comparing twisted and untwisted local variances;
3. identifying which log-ratio bands dominate correlation cancellation;
4. testing candidate renormalizations;
5. selecting promising kernels.

But:

$$
\boxed{
\kappa_{\rm eff}(X)>0
\text{ on a finite range}
}
$$

does not imply a global fixed $\kappa$.

---

# 23. GAP ledger

## CLOSED / REFERENCE-VALIDATED

### G1. Classical mean-square exponent alignment

```text
REFERENCE_VALIDATED
```

$$
\delta_I=2\Theta+1.
$$

### G2. Zaccagnini inverse exponent map

```text
REFERENCE_VALIDATED
```

$$
J(x,1)\ll x^{3-\kappa}
\Longrightarrow
\Theta\le1-\kappa/2.
$$

### G3. Gallagher variance-saving converter

```text
CLOSED_AS_STRENGTH_CONVERTER
```

$$
XH^2X^{-\kappa}
\to
X^{1-\kappa}
$$

under the critical normalization.

### G4. Twisted local main term

```text
CLOSED
```

$$
A_h(\tau)
=
2
\frac{
\cosh((1/2-i\tau)h)-1
}{
(1/2-i\tau)^2
}.
$$

---

## OPEN

### G5. Any fixed power variance saving

```text
OPEN
```

$$
\kappa>0.
$$

### G6. Uniform twisted local correlation bound

```text
OPEN
```

### G7. First fixed zero-strip breakthrough

```text
OPEN
```

### G8. $\kappa=1$

```text
OPEN_RH_COMPLETE
```

### G9. RH

```text
OPEN
```

---

# 24. Trust boundary

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE

KAPPA_CONVERTER = STRENGTH LAW
NOT A NEW CORRELATION ESTIMATE

CURRENT_UNCONDITIONAL_KAPPA = 0
AT FIXED-POWER CLASSIFICATION

NO FIXED POSITIVE KAPPA HAS BEEN PROVED

TWISTED_LOCAL_OBJECT = DEFINED
UNIFORM_TWISTED_BOUND = NOT PROVED

GLOBAL_RH_CERTIFICATE = FALSE
```

Forbidden:

$$
o(XH^2)
\Longrightarrow
\kappa>0.
$$

Forbidden:

$$
(\log X)^{-A}
\Longrightarrow
X^{-\kappa}.
$$

Forbidden:

$$
\text{average vertical control}
\Longrightarrow
\text{rightmost-zero exclusion}.
$$

---

# 25. One-line status

> v2.1 validates the AMRAL exponent-drop meter against classical inverse Selberg theory. The dyadic PNT mean-square exponent is $2\Theta+1$, so the AMRAL normalized energy exponent is exactly $\beta=2\Theta-1$. Zaccagnini independently proves that a bound $J(x,1)\ll x^{3-\kappa}$ forces $\Theta\le1-\kappa/2$, which is exactly $\beta\le1-\kappa$. Gallagher scaling shows why the same fixed power-saving parameter survives a change from spectral width $U$ to arithmetic interval $H=X/U$: a local variance $XH^2X^{-\kappa}$ transfers to critical spectral energy $X^{1-\kappa}$. Current unconditional almost-all short-interval results give $o(XH^2)$ or subpower savings, hence $\kappa=0$ at fixed-power scale; RH-scale Selberg variance corresponds to $\kappa=1$ at fixed multiplicative aperture. High-frequency Gallagher necessarily introduces the phase-twisted local tent sum with main term $A_h(\tau)=2[\cosh((1/2-i\tau)h)-1]/(1/2-i\tau)^2$. The first genuine nonbinary breakthrough is therefore precisely any uniform arithmetic theorem with fixed $\kappa>0$; this would produce a new fixed zero strip before full RH.

---

# 26. References

1. Alessandro Zaccagnini, **A conditional density theorem for the zeros of the Riemann zeta-function**, *Acta Arithmetica* 93 (2000), 293–301.  
   https://matwbn.icm.edu.pl/ksiazki/aa/aa93/aa9335.pdf

2. Alessandro Zaccagnini, **Primes in almost all short intervals**, *Acta Arithmetica* 84 (1998), 225–244.  
   DOI: https://doi.org/10.4064/aa-84-3-225-244

3. Daniel R. Johnston et al., modern mean-value discussion including the classical mean-square size of $\psi(x)-x$ in terms of $\Theta$, *Research in Number Theory* (2025).  
   https://link.springer.com/article/10.1007/s40993-025-00640-y

4. Giovanni Coppola, Maurizio Laporta, **A modified Gallagher's Lemma**, arXiv:1301.0008.  
   https://arxiv.org/abs/1301.0008

5. Giovanni Coppola, Maurizio Laporta, **A generalization of Gallagher's lemma for exponential sums**, arXiv:1411.1739.  
   https://arxiv.org/abs/1411.1739

6. Alessandro Zaccagnini, survey material on primes in almost all short intervals and Selberg integrals.  
   https://people.dmi.unipr.it/alessandro.zaccagnini/psfiles/papers/Q429.pdf

7. Kaisa Matomäki, Maksym Radziwiłł, Xuancheng Shao, Terence Tao, Joni Teräväinen, **Higher uniformity of arithmetic functions in short intervals II. Almost all intervals**, *Inventiones mathematicae* 244 (2026), 967–1091.  
   arXiv: https://arxiv.org/abs/2411.05770

8. AMRAL, **RH-FilteredPNT-GallagherStrengthAudit v2.0**.

9. AMRAL, **RH-MellinSymmetry-PNTFilterBridge v1.9**.

---

# 27. Provenance

研究主導：Neo.K

v2.1 variance-saving converter、classical inverse-theory alignment、twisted-local arithmetic definition、strength classification 與 canonical source 整理：ChatGPT / GPT-5.6 Sol

日期：2026-09-03

研究定位：AMRAL 黎曼猜想半自主研究線，第三弧線 fixed-power variance-saving / twisted local correlation 節點。

本文件是 research source artifact，不是 peer-reviewed publication。

所有 claim 必須依 Claim register、GAP ledger 與 Trust boundary 解讀。
