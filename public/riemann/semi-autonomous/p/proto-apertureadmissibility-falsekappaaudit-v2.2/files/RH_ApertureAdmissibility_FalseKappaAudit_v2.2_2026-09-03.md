工程紀錄 · 第三弧線 v2.2 · 2026-09-03 · APERTURE_ADMISSIBILITY · FALSE_KAPPA_AUDIT · RH_CLAIM_FALSE

# Aperture Admissibility、Additive Symmetry Blindness 與 False-$\kappa$ Audit

**RH-ApertureAdmissibility-FalseKappaAudit v2.2**

本節點承接：

- `RH-LocalEnergy-CorrelationApertureTradeoff v1.8`
- `RH-FilteredPNT-GallagherStrengthAudit v2.0`
- `RH-TwistedLocalCorrelation-ExponentDrop v2.1`

v2.1 建立 fixed-power variance-saving 進度參數：

$$
\kappa>0
$$

作為第一個 fixed zero-strip breakthrough gate。

但 v2.2 發現一個必須正式補上的 scope condition：

> 文獻中確實存在很強、甚至表面上呈 fixed-power saving 的 additive symmetry / short-interval mean-square bounds；然而若 arithmetic aperture 本身以固定冪速度縮小，該 statistic 也會同步衰減 off-axis zeta mode。未經 sensitivity normalization 的 raw power saving 不能直接輸入 v2.1 的 $\kappa$ converter。

因此 v2.2 的任務不是否定 v2.1，而是定義：

```text
RH-SENSITIVE APERTURE CLASS
```

以及：

```text
FALSE-KAPPA DETECTOR.
```

本輪結論：

$$
\boxed{
\text{對二階 affine-memory-erasing symmetry filter，完整 RH sensitivity 要求}
\quad
H=X^{1-o(1)}.
}
$$

任何固定：

$$
H=X^a,
\qquad
a<1,
$$

都會對 sufficiently small off-axis displacement 失明。

更強地，若：

$$
a<\frac34,
$$

則 unrenormalized additive second-symmetry statistic 對**所有可能的固定 zeta off-axis modes**都呈衰減。

因此 Coppola 類短 additive symmetry bounds 可以有很漂亮的 power saving而不推出 fixed zero strip，並不矛盾。

在真正 RH-sensitive 的 admissible regime：

$$
H=X^{1-o(1)},
$$

目前 audited unconditional Selberg/PNT results仍只給：

$$
o(XH^2)
$$

或 logarithmic/subpower saving，也就是：

$$
\boxed{
\kappa_{\rm admissible}=0
}
$$

at fixed-power classification。

**RH_CLAIM = False.**

---

# 0. Claim register

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE

ADDITIVE_SYMMETRY_ZERO_MODE_RESPONSE = CLOSED
SECOND_ORDER_APERTURE_ATTENUATION = CLOSED

FIXED_POWER_SHRINKING_APERTURE_FULL_RH_SENSITIVE = FALSE
SUBEXPONENTIAL_LOG_APERTURE_RH_SENSITIVE = TRUE_AT_EXPONENTIAL_TYPE

TOTAL_BLINDNESS_THRESHOLD_A_LT_3_OVER_4 = CLOSED_FOR_FIXED_ZERO_MODES

V2_1_KAPPA_CONVERTER = VALID_WITH_APERTURE_NORMALIZATION_SCOPE
RAW_SHORT_INTERVAL_KAPPA = NOT_AUTOMATICALLY_RH_COMPARABLE

CURRENT_ADMISSIBLE_UNCONDITIONAL_KAPPA = 0
ANY_ADMISSIBLE_KAPPA_POSITIVE = OPEN

GLOBAL_RH_CERTIFICATE = FALSE
```

---

# 1. Additive symmetry statistic

Consider the classical additive prime symmetry sum:

$$
\boxed{
\Sigma_H(x)
=
\psi(x+H)
-
2\psi(x)
+
\psi(x-H).
}
$$

Up to endpoint conventions this is the same right-minus-left prime symmetry:

$$
\sum_{x<n\le x+H}\Lambda(n)
-
\sum_{x-H<n\le x}\Lambda(n).
$$

This is the basic object in the symmetry-integral literature.

Coppola studies its mean square:

$$
I_\Lambda(X,H)
=
\int_X^{2X}
|\Sigma_H(x)|^2dx
$$

or discrete equivalents and related weighted variants.

Strong unconditional bounds are known for short additive ranges.

---

# 2. Exact response of one zeta zero mode

The explicit formula contribution of a nontrivial zero:

$$
\rho
$$

to $\psi(x)$ has the form:

$$
-\frac{x^\rho}{\rho}.
$$

Let:

$$
r=\frac Hx.
$$

Then the symmetry response of this single zero mode is:

$$
\boxed{
\Sigma_{\rho,H}(x)
=
-\frac{x^\rho}{\rho}
\left[
(1+r)^\rho
+
(1-r)^\rho
-
2
\right].
}
$$

This formula is exact whenever:

$$
0<r<1.
$$

---

# 3. Small-aperture expansion

For fixed $\rho$ and:

$$
r\to0,
$$

binomial expansion gives:

$$
\boxed{
\begin{aligned}
(1+r)^\rho
+
(1-r)^\rho
-
2
&=
\rho(\rho-1)r^2
\\
&\quad
+
\frac{
\rho(\rho-1)(\rho-2)(\rho-3)
}{12}
r^4
+
O_\rho(r^6).
\end{aligned}
}
$$

Therefore:

$$
\boxed{
\Sigma_{\rho,H}(x)
=
-(\rho-1)
r^2x^\rho
+
O_\rho(r^4x^\rho).
}
$$

After critical normalization:

$$
x^{-1/2},
$$

the leading magnitude is:

$$
\boxed{
\asymp_\rho
r^2
x^{\Re\rho-1/2}.
}
$$

Thus additive second symmetry is a second-order high-pass filter in relative aperture.

---

# 4. Fixed-power additive aperture

Set:

$$
H=X^a,
\qquad
0<a<1.
$$

Then:

$$
r
=
\frac HX
=
X^{a-1}.
$$

Define horizontal displacement:

$$
\delta
=
\Re\rho-\frac12.
$$

The critically normalized fixed-zero response has power exponent:

$$
\boxed{
\delta
-
2(1-a).
}
$$

So:

$$
\boxed{
x^{-1/2}
\Sigma_{\rho,H}(x)
\asymp
X^{\delta-2(1-a)}
}
$$

at fixed-zero mode level.

---

# 5. Blindness to sufficiently small off-axis displacement

For every fixed:

$$
a<1,
$$

choose any:

$$
0<\delta<2(1-a).
$$

Then:

$$
\delta-2(1-a)<0.
$$

Hence the fixed off-axis zero mode decays in the raw normalized additive symmetry statistic.

Therefore:

## Theorem 5.1 · Fixed-power aperture blindness

Any fixed-power additive aperture:

$$
H=X^a,
\qquad
a<1,
$$

fails to retain growth sensitivity to arbitrarily small positive horizontal zero displacement.

So raw power savings in such a statistic cannot be interpreted directly as a fixed zero-strip saving.

---

# 6. Total blindness threshold

Every nontrivial zeta zero lies in:

$$
0<\Re\rho<1.
$$

Thus:

$$
0<\delta<\frac12
$$

for a right-half off-axis zero.

If:

$$
a<\frac34,
$$

then:

$$
2(1-a)>\frac12.
$$

Therefore for every possible fixed off-axis displacement:

$$
0<\delta\le\frac12,
$$

we have:

$$
\delta-2(1-a)<0.
$$

Hence:

## Theorem 6.1 · Unrenormalized total fixed-mode blindness

If:

$$
\boxed{
H=X^a,
\qquad
a<\frac34,
}
$$

then the critically normalized unrenormalized additive second-symmetry statistic makes every possible fixed off-axis zeta zero mode decay.

This does not mean the statistic contains no arithmetic information.

It means its raw power scale is not a direct RH-sensitive exponent gauge.

---

# 7. Coppola-type symmetry bounds are therefore not paradoxical

Coppola proves strong unconditional estimates for prime symmetry integrals. One form is:

$$
\boxed{
I_\Lambda(N,H)
\ll
NH(\log N)^5
+
NH^{21/20}(\log N)^2.
}
$$

Other symmetry-integral results obtain square-root-cancellation-type bounds such as:

$$
I_f(N,H)\ll NH
$$

for suitable sieve functions and short-range hypotheses.

These are genuinely strong arithmetic results.

But they are typically studied in genuinely additive-short regimes, including logarithmic windows and ranges such as:

$$
H=o(\sqrt N)
$$

in the general symmetry-integral framework.

In log coordinates:

$$
h_{\log}
\asymp
\frac HN.
$$

For:

$$
H\le N^{1/2-o(1)},
$$

the aperture shrinks at least like:

$$
N^{-1/2+o(1)}.
$$

Section 6 shows this is far inside the total fixed-zero blindness regime for the unrenormalized second symmetry.

Therefore:

$$
\boxed{
\text{strong Coppola symmetry saving}
\not\Longrightarrow
\text{new zeta fixed zero strip}.
}
$$

There is no contradiction.

---

# 8. Apparent raw saving versus RH-sensitive saving

Suppose one compares a raw symmetry estimate to the naive variance scale:

$$
XH^2.
$$

A bound:

$$
I_\Lambda(X,H)
\ll
XH
\operatorname{polylog}X
$$

looks like a relative saving:

$$
H^{-1}.
$$

If:

$$
H=X^a,
$$

this looks like:

$$
X^{-a}.
$$

Naively one might write:

$$
\kappa_{\rm raw}=a.
$$

But Sections 4–6 show that the statistic itself has also attenuated an off-axis mode by:

$$
X^{-2(1-a)}.
$$

Hence:

```text
RAW POWER SAVING
```

contains both:

- true arithmetic cancellation;
- aperture-induced signal attenuation.

Without a sensitivity-normalized transfer theorem the two cannot be identified.

This is the core False-$\kappa$ warning.

---

# 9. RH-sensitive aperture exponent

Define:

$$
\boxed{
\alpha(X)
=
\frac{
\log(X/H)
}{
\log X
}.
}
$$

For:

$$
H=X^a,
$$

$$
\alpha=1-a.
$$

For a second-order memory eraser, a fixed off-axis mode exponent changes from:

$$
\delta
$$

to:

$$
\delta-2\alpha
$$

at fixed-power level.

To retain sensitivity to every arbitrarily small fixed:

$$
\delta>0,
$$

we need:

$$
\boxed{
\alpha(X)\to0.
}
$$

Equivalently:

$$
\boxed{
H=X^{1-o(1)}.
}
$$

This is the additive-coordinate expression of the v1.8 subexponential-aperture condition.

---

# 10. Admissible aperture class

Define an RH-sensitive additive aperture family to be **exponent-admissible** if:

$$
\boxed{
\frac{
\log(X/H)
}{
\log X
}
\to0.
}
$$

Equivalent forms:

$$
H=X^{1-o(1)},
$$

or:

$$
\frac H X
=
X^{-o(1)}.
$$

Examples:

### Admissible

$$
H=\frac X{(\log X)^A}.
$$

$$
H=Xe^{-\sqrt{\log X}}.
$$

$$
H=cX
$$

with fixed:

$$
0<c<1.
$$

### Not exponent-admissible

$$
H=X^{0.99}.
$$

$$
H=X^{3/4}.
$$

$$
H=X^{1/2}.
$$

$$
H=(\log X)^A.
$$

The distinction is about preserving fixed exponential type, not about whether the short-interval problem is mathematically interesting.

---

# 11. General filter-order version

Let a local linear filter erase polynomial memory through degree:

$$
m-1.
$$

Then its low-aperture transfer begins at order:

$$
m.
$$

For log aperture:

$$
h_{\log}
=
X^{-\alpha+o(1)},
$$

a zero displacement mode:

$$
X^\delta
$$

is transformed to:

$$
\boxed{
X^{\delta-m\alpha+o(1)}.
}
$$

Thus full sensitivity to arbitrarily small:

$$
\delta>0
$$

requires:

$$
\boxed{
\alpha=0.
}
$$

The second-difference / affine-memory-erasing case has:

$$
m=2.
$$

This generalizes the v1.8 aperture–information tradeoff.

---

# 12. Scope correction to v2.1

v2.1 derived the variance-saving converter:

$$
XH^2X^{-\kappa}
\quad\leadsto\quad
X^{1-\kappa}
$$

under the critical Gallagher normalization.

This converter remains valid as a strength law for the **properly normalized Gallagher/Cesàro object**.

However it must not be applied mechanically to an arbitrary raw short-interval symmetry estimate.

The safe scope is:

1. fixed multiplicative/log aperture; or
2. exponent-admissible aperture:
   $$
   H=X^{1-o(1)};
   $$
3. correct sensitivity normalization included in the transfer;
4. required twist uniformity retained.

So v2.2 records:

```text
V2_1_CONVERTER = VALID
BUT
RAW_SHORT_INTERVAL_BOUND -> KAPPA
REQUIRES APERTURE / NORMALIZATION AUDIT.
```

---

# 13. Why subpower Gallagher resolution is safe

v2.1 recommended:

$$
U=X^{o(1)}.
$$

Then Gallagher arithmetic scale:

$$
H=\frac XU
$$

satisfies:

$$
H=X^{1-o(1)}.
$$

Thus:

$$
\alpha(X)\to0.
$$

For every fixed off-axis displacement:

$$
\delta>0,
$$

the aperture attenuation is only:

$$
X^{-o(1)}.
$$

Therefore it does not change the fixed exponential class.

This is exactly why subpower Gallagher resolution is the natural RH-sensitive regime.

---

# 14. Current unconditional Selberg result inside the admissible regime

Zaccagnini records the unconditional classical estimate:

$$
\boxed{
J(X,H)
=
o(XH^2)
}
$$

for a broad range including:

$$
H\ge
X^{1/6+\varepsilon}
$$

in the standard formulation.

This range certainly includes every exponent-admissible aperture:

$$
H=X^{1-o(1)}
$$

for sufficiently large $X$.

More explicit versions improve the variance by logarithmic / subpower factors.

But:

$$
o(XH^2)
$$

does not imply:

$$
XH^2X^{-\kappa}
$$

for any fixed:

$$
\kappa>0.
$$

Therefore the currently audited unconditional state in the RH-sensitive admissible class is still:

$$
\boxed{
\kappa_{\rm admissible}=0.
}
$$

---

# 15. Almost-all short-interval progress does not change this classification

Modern short-interval theorems are substantially stronger in many additive ranges.

They can show PNT-type behavior for almost all intervals far shorter than the exponent-admissible class.

Such results remain highly important.

But two separate issues prevent automatic v2.1 exponent progress:

1. fixed-power shrinking apertures can attenuate RH modes;
2. almost-all control does not automatically exclude a sparse vertical/rightmost-zero obstruction.

Therefore:

$$
\boxed{
\text{shorter interval}
\neq
\text{stronger RH-sensitive exponent theorem}.
}
$$

---

# 16. A False-$\kappa$ audit protocol

Every future candidate variance theorem should record:

```text
1. arithmetic window H(X)

2. aperture exponent
   alpha(X) = log(X/H)/log X

3. filter vanishing order m

4. raw variance natural scale

5. claimed raw power saving kappa_raw

6. sensitivity normalization

7. whether alpha -> 0

8. vertical twist uniformity

9. translated RH-sensitive exponent beta
```

Then classify:

### SAFE

```text
alpha -> 0
correct normalization
required twists controlled
```

### FALSE-KAPPA RISK

```text
limsup alpha > 0
and raw saving is quoted before sensitivity normalization
```

### NOT COMPARABLE

```text
different filter order / different main term / average-only twist control
```

This protocol should be used before promoting an external short-interval theorem into the AMRAL exponent ladder.

---

# 17. Exact zero-mode audit for a candidate theorem

For an additive second-symmetry theorem at aperture:

$$
H(X),
$$

the fastest sanity check is to evaluate:

$$
\boxed{
M_{\rho,X}
=
\frac{
(1+H/X)^\rho
+
(1-H/X)^\rho
-
2
}{
\rho
}.
}
$$

If:

$$
|M_{\rho,X}|
$$

already carries a fixed negative power of $X$ for a candidate off-axis displacement, then part of the apparent variance saving is simply filter attenuation.

This should be automated in the research pipeline.

---

# 18. Computational reference examples

For a fixed-power aperture:

$$
H=X^a,
$$

the asymptotic normalized zero-mode exponent is:

$$
\delta-2(1-a).
$$

Examples:

### $a=1/2$

$$
\delta-1<0
$$

for every possible:

$$
\delta\le1/2.
$$

Complete fixed-zero decay.

### $a=3/4$

$$
\delta-\frac12.
$$

Only an edge-limit displacement:

$$
\delta=\frac12
$$

would be neutral; all actual interior fixed displacements decay.

### $a=0.9$

$$
\delta-0.2.
$$

The statistic remains blind to:

$$
0<\delta<0.2.
$$

### $a=1-o(1)$

$$
\delta-o(1)>0
$$

for every fixed:

$$
\delta>0.
$$

Full fixed-exponent sensitivity is restored.

---

# 19. What v2.2 says about "can $\kappa>0$ be obtained?"

The answer must be split.

## Raw short-interval $\kappa$

Yes.

Strong symmetry / large-sieve / dispersion estimates can exhibit apparent fixed power savings in shrinking additive windows.

## RH-sensitive admissible $\kappa$

In the sources audited here:

$$
\boxed{
\text{no fixed }\kappa>0
\text{ is currently obtained unconditionally}.
}
$$

Current admissible results remain in:

$$
\kappa=0
$$

with $o(1)$, logarithmic, or subpower improvements.

This is the quantity relevant to the v2.1 fixed zero-strip program.

---

# 20. New smallest GAP

The smallest genuine arithmetic target is now:

choose an exponent-admissible aperture such as:

$$
\boxed{
H
=
\frac X{(\log X)^A},
}
$$

or directly use fixed log aperture $h>0$.

Then prove, with the required centered/twisted normalization, any fixed:

$$
\boxed{
\kappa>0
}
$$

power saving.

In the direct AMRAL variable, one may target:

$$
\boxed{
\int_{\log X}^{\log X+1}
\left|
\mathfrak E_{h,\tau}(e^t)
\right|^2dt
\ll
X^{1-\kappa+o(1)}
}
$$

uniformly in the twist regime required by the transfer.

This cannot be explained away by aperture attenuation because $h$ is fixed.

---

# 21. Suggested v2.3 direction

Recommended:

`RH-AdmissibleTwistedVariance-v2.3`

Do not study shorter and shorter raw intervals.

Fix either:

$$
h=\log2
$$

or:

$$
H=X/(\log X)^A.
$$

Then:

1. write the exact phase-twisted centered second moment;
2. expand it into diagonal and off-diagonal log-ratio correlations;
3. analytically subtract every deterministic main term;
4. determine which off-diagonal shift ranges must supply a fixed $X^{-\kappa}$ saving;
5. compare with:
   - large sieve;
   - dispersion;
   - Hardy–Littlewood prime-pair heuristics;
   - known averaged prime-pair theorems;
6. identify whether a fixed $\kappa$ would require a genuinely new prime-pair theorem or can emerge from an existing bilinear estimate.

This keeps the aperture inside the RH-sensitive class.

---

# 22. GAP ledger

## CLOSED / CORRECTED

### G1. Additive symmetry zero response

```text
CLOSED
```

### G2. Fixed-power aperture blindness

```text
CLOSED
```

### G3. Total blindness for $a<3/4$

```text
CLOSED_FOR_FIXED_ZERO_MODES
```

### G4. Exponent-admissible aperture class

```text
DEFINED
```

$$
H=X^{1-o(1)}.
$$

### G5. v2.1 scope condition

```text
CORRECTED
```

Raw shrinking-window savings require normalization audit before conversion to $\kappa$.

---

## OPEN

### G6. Admissible fixed power saving

```text
OPEN
```

$$
\kappa>0.
$$

### G7. Uniform twisted admissible variance

```text
OPEN
```

### G8. First fixed zero-strip breakthrough

```text
OPEN
```

### G9. $\kappa=1$

```text
OPEN_RH_COMPLETE
```

### G10. RH

```text
OPEN
```

---

# 23. Trust boundary

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE

RAW_POWER_SAVING_EXISTS_IN_LITERATURE = TRUE
RAW_POWER_SAVING_IS_RH_KAPPA = FALSE_IN_GENERAL

CURRENT_AUDITED_ADMISSIBLE_KAPPA = 0

APERTURE_BLINDNESS_RESULT =
    FILTER / MODE-SENSITIVITY STATEMENT
NOT A NO-GO FOR SHORT-INTERVAL NUMBER THEORY

GLOBAL_RH_CERTIFICATE = FALSE
```

Forbidden:

$$
I_\Lambda(X,H)\ll XH
\Longrightarrow
\kappa>0
$$

without an aperture/normalization audit.

Forbidden:

$$
H=X^a,\ a<1
\Longrightarrow
\text{full fixed-exponent RH sensitivity}.
$$

Forbidden:

$$
\text{almost-all short-interval theorem}
\Longrightarrow
\text{rightmost-zero exclusion}.
$$

---

# 24. One-line status

> v2.2 resolves an apparent paradox in the exponent-drop program. Strong unconditional prime-symmetry bounds already exist and can look like fixed power savings relative to $XH^2$, but they operate in shrinking additive apertures. For a single zeta zero mode, the additive second-symmetry multiplier is $[(1+H/x)^\rho+(1-H/x)^\rho-2]/\rho$, whose leading term is $(\rho-1)(H/x)^2$. Thus for $H=X^a$ the critically normalized off-axis exponent becomes $\delta-2(1-a)$. Any fixed $a<1$ is blind to sufficiently small horizontal displacement, and $a<3/4$ makes every possible fixed off-axis zeta zero mode decay. Therefore raw short-interval power saving is not automatically the RH-sensitive $\kappa$ of v2.1. Full fixed-exponent sensitivity requires the exponent-admissible class $H=X^{1-o(1)}$, including fixed multiplicative windows and subpower Gallagher resolution. In this admissible class, the audited unconditional Selberg results still give only $o(XH^2)$ or logarithmic/subpower savings, hence $\kappa=0$ at fixed-power scale. The first genuine next target remains a centered, properly normalized, twist-uniform fixed power saving $\kappa>0$ inside an admissible aperture.

---

# 25. References

1. Giovanni Coppola, **On the symmetry of primes**, arXiv:1009.6121, 2010.  
   https://arxiv.org/abs/1009.6121

2. Giovanni Coppola, **On the Symmetry Integral**, arXiv:1007.1018, 2010.  
   https://arxiv.org/abs/1007.1018

3. Giovanni Coppola, **Introducing weighted Selberg integrals**, Journées Arithmétiques XXVIII material.  
   Public author copy: https://www.giovannicoppola.name/files/articoli/9_ja28copp.pdf

4. Alessandro Zaccagnini, **Primes in almost all short intervals**, *Acta Arithmetica* 84 (1998), 225–244.  
   https://eudml.org/doc/207144

5. Alessandro Zaccagnini, survey / lecture material summarizing:
   $$
   J(X,H)=o(XH^2)
   $$
   in the classical unconditional almost-all range.  
   https://people.dmi.unipr.it/alessandro.zaccagnini/psfiles/papers/Q429.pdf

6. Alessandro Zaccagnini, **A conditional density theorem for the zeros of the Riemann zeta-function**, *Acta Arithmetica* 93 (2000), 293–301.

7. AMRAL, **RH-LocalEnergy-CorrelationApertureTradeoff v1.8**.

8. AMRAL, **RH-TwistedLocalCorrelation-ExponentDrop v2.1**.

---

# 26. Provenance

研究主導：Neo.K

v2.2 aperture-admissibility audit、additive-symmetry zero-mode analysis、false-$\kappa$ correction、literature strength classification 與 canonical source 整理：ChatGPT / GPT-5.6 Sol

日期：2026-09-03

研究定位：AMRAL 黎曼猜想半自主研究線，第三弧線 aperture sensitivity / valid exponent-progress gate 節點。

本文件是 research source artifact，不是 peer-reviewed publication。

所有 claim 必須依 Claim register、GAP ledger 與 Trust boundary 解讀。
