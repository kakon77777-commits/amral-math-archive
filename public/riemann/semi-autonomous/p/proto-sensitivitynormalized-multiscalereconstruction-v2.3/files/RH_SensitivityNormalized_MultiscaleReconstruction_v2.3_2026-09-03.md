工程紀錄 · 第三弧線 v2.3 · 2026-09-03 · MULTISCALE_RECONSTRUCTION · SENSITIVITY_NORMALIZATION · RH_CLAIM_FALSE

# Sensitivity-Normalized Multiscale Reconstruction 與 False-$\kappa$ Conservation Law

**RH-SensitivityNormalized-MultiscaleReconstruction v2.3**

本節點承接：

- `RH-LocalEnergy-CorrelationApertureTradeoff v1.8`
- `RH-TwistedLocalCorrelation-ExponentDrop v2.1`
- `RH-ApertureAdmissibility-FalseKappaAudit v2.2`

v2.2 已指出：

> raw short-interval power saving 不能直接解讀成 RH-sensitive $\kappa$，因為 shrinking aperture 本身會以二階因子抑制 off-axis zero mode。

v2.3 進一步把這個現象升級成一個**精確 multiscale identity**。

對：

$$
D_h(t)
=
\frac12
\left[
\Psi(t+h)+\Psi(t-h)-2\Psi(t)
\right],
$$

若：

$$
H=mh,
\qquad
m\in\mathbb N,
$$

則：

$$
\boxed{
D_H(t)
=
\sum_{k=-(m-1)}^{m-1}
(m-|k|)
D_h(t+kh).
}
$$

因此定義 sensitivity-normalized observable：

$$
\boxed{
\widetilde D_h(t)
=
\frac{D_h(t)}{h^2},
}
$$

便得到：

$$
\boxed{
\widetilde D_H(t)
=
\sum_{k=-(m-1)}^{m-1}
p_{k,m}
\widetilde D_h(t+kh),
}
$$

其中：

$$
\boxed{
p_{k,m}
=
\frac{m-|k|}{m^2}
}
$$

且：

$$
p_{k,m}\ge0,
$$

$$
\boxed{
\sum_{k=-(m-1)}^{m-1}p_{k,m}=1.
}
$$

也就是：

> **大孔徑 normalized RH observable 是小孔徑 normalized observables 的精確凸組合。**

這個 identity 把 v2.2 的 qualitative false-$\kappa$ 警告變成 quantitatively exact 的 scale-conversion law。

**RH_CLAIM = False.**

---

# 0. Claim register

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE

SECOND_DIFFERENCE_MULTISCALE_IDENTITY = CLOSED
SENSITIVITY_NORMALIZED_CONVEX_RECONSTRUCTION = CLOSED
NORMALIZED_ENERGY_JENSEN_BOUND = CLOSED

RAW_ENERGY_RECONSTRUCTION_COST = m^4
MODAL_m4_COST_ASYMPTOTICALLY_SHARP = TRUE

SECOND_ORDER_KAPPA_CORRECTION = CLOSED
GENERAL_ORDER_KAPPA_CORRECTION = CLOSED_AT_FILTER_SCALING_LEVEL

TWIST_RESONANCE_ZERO_RESPONSE = CLOSED
NORMALIZED_ZERO_RESPONSE_APERTURE_INDEPENDENT = CLOSED_AS_LIMIT

RAW_SHORT_INTERVAL_SAVING = NOT_RH_KAPPA
SENSITIVITY_CORRECTED_SAVING = CANONICAL

CURRENT_CORRECTED_FIXED_KAPPA_POSITIVE = NOT_PROVED
GLOBAL_RH_CERTIFICATE = FALSE
```

---

# 1. The second-difference operator

Define:

$$
\Delta_h^2f(t)
=
f(t+h)+f(t-h)-2f(t).
$$

Then:

$$
D_h(t)
=
\frac12
\Delta_h^2\Psi(t).
$$

The operator annihilates affine functions:

$$
\Delta_h^2(a+bt)=0.
$$

This is why it removes the permanent linear prime-ramp memory in Suzuki's arithmetic formula.

---

# 2. Exact multiscale identity

Let:

$$
m\ge1
$$

be an integer.

Define triangular coefficients:

$$
w_{k,m}
=
m-|k|,
\qquad
|k|\le m-1.
$$

Then:

## Theorem 2.1 · Second-difference multiscale reconstruction

For every function for which the shifts are defined,

$$
\boxed{
\Delta_{mh}^2f(t)
=
\sum_{k=-(m-1)}^{m-1}
w_{k,m}
\Delta_h^2f(t+kh).
}
$$

---

# 3. Algebraic proof

Let $S_h$ be the shift operator:

$$
S_hf(t)=f(t+h).
$$

Then:

$$
\Delta_h^2
=
S_h+S_h^{-1}-2.
$$

The Laurent-polynomial identity is:

$$
\boxed{
z^m+z^{-m}-2
=
(z+z^{-1}-2)
\sum_{k=-(m-1)}^{m-1}
(m-|k|)z^k.
}
$$

Setting:

$$
z=S_h
$$

gives Theorem 2.1.

Equivalently, on the Fourier circle:

$$
\frac{
\sin^2(m\theta/2)
}{
\sin^2(\theta/2)
}
=
\sum_{k=-(m-1)}^{m-1}
(m-|k|)e^{ik\theta},
$$

the Fejér-kernel identity.

So the multiscale reconstruction is an exact Fejér convolution.

---

# 4. Weight sum

The triangular weight total is:

$$
\boxed{
\sum_{k=-(m-1)}^{m-1}
(m-|k|)
=
m^2.
}
$$

Therefore for:

$$
H=mh,
$$

we have:

$$
\boxed{
D_H(t)
=
\sum_k
w_{k,m}
D_h(t+kh).
}
$$

This raw identity contains an $m^2$ amplitude amplification.

That amplification is exactly what reconstructs the low-frequency information suppressed by the smaller aperture.

---

# 5. Sensitivity-normalized observable

Define:

$$
\boxed{
\widetilde D_h(t)
=
\frac{
D_h(t)
}{
h^2
}.
}
$$

Since:

$$
H^2=m^2h^2,
$$

divide the raw reconstruction by $H^2$:

$$
\begin{aligned}
\widetilde D_H(t)
&=
\frac1{m^2h^2}
\sum_k
w_{k,m}D_h(t+kh)
\\
&=
\sum_k
\frac{w_{k,m}}{m^2}
\widetilde D_h(t+kh).
\end{aligned}
$$

Hence:

## Theorem 5.1 · Convex multiscale reconstruction

$$
\boxed{
\widetilde D_H(t)
=
\sum_k
p_{k,m}
\widetilde D_h(t+kh),
}
$$

where:

$$
p_{k,m}
=
\frac{m-|k|}{m^2},
$$

$$
p_{k,m}\ge0,
$$

and:

$$
\boxed{
\sum_kp_{k,m}=1.
}
$$

So sensitivity normalization converts the scale change into a convex average.

---

# 6. Jensen energy inequality

Because:

$$
x\mapsto|x|^2
$$

is convex,

$$
\boxed{
|\widetilde D_H(t)|^2
\le
\sum_k
p_{k,m}
|\widetilde D_h(t+kh)|^2.
}
$$

For any interval $I$:

$$
\boxed{
\int_I
|\widetilde D_H(t)|^2dt
\le
\sum_k
p_{k,m}
\int_{I+kh}
|\widetilde D_h(u)|^2du.
}
$$

Therefore:

$$
\boxed{
E_H^{\rm norm}(I)
\le
\sup_{|s|\le H}
E_h^{\rm norm}(I+s),
}
$$

where $E_h^{\rm norm}$ denotes the normalized local $L^2$ energy.

This is a much cleaner statement than the raw $m^4$ amplification law.

---

# 7. Raw energy reconstruction cost

Without sensitivity normalization, weighted Cauchy gives:

$$
\left|
\sum_kw_{k,m}z_k
\right|^2
\le
\left(
\sum_kw_{k,m}
\right)
\left(
\sum_kw_{k,m}|z_k|^2
\right).
$$

Using:

$$
\sum_kw_{k,m}=m^2,
$$

one obtains:

$$
\boxed{
E_H^{\rm raw}
\le
m^4
\sup E_h^{\rm raw}.
}
$$

Thus the raw energy reconstruction cost is:

$$
\boxed{
m^4.
}
$$

This is exactly the energy-level compensation for the $h^2$ aperture attenuation.

---

# 8. Modal sharpness

Take:

$$
f(t)=e^{\lambda t}.
$$

Then:

$$
D_h[f](t)
=
\left[
\cosh(\lambda h)-1
\right]
e^{\lambda t}.
$$

Thus:

$$
\boxed{
\frac{
D_H[f](t)
}{
D_h[f](t)
}
=
\frac{
\cosh(\lambda H)-1
}{
\cosh(\lambda H/m)-1
}.
}
$$

As:

$$
m\to\infty
$$

with $H,\lambda$ fixed and $\lambda\neq0$:

$$
\cosh(\lambda H/m)-1
\sim
\frac{\lambda^2H^2}{2m^2}.
$$

Therefore:

$$
\boxed{
\frac{
D_H[f]
}{
D_h[f]
}
\sim
C_{\lambda,H}m^2,
}
$$

where:

$$
C_{\lambda,H}
=
\frac{
2[\cosh(\lambda H)-1]
}{
\lambda^2H^2
}.
$$

Hence the corresponding energy ratio is asymptotically:

$$
\boxed{
\asymp m^4.
}
$$

So the $m^4$ reconstruction cost is not merely a loose Cauchy artifact.

It is the correct modal scale.

---

# 9. Aperture-independent normalized modal response

For the normalized observable:

$$
\widetilde D_h[f](t)
=
\frac{
\cosh(\lambda h)-1
}{
h^2
}
e^{\lambda t}.
$$

As:

$$
h\to0,
$$

$$
\boxed{
\widetilde D_h[f](t)
\longrightarrow
\frac{\lambda^2}{2}
e^{\lambda t}.
}
$$

Thus sensitivity normalization removes the low-aperture attenuation.

For an off-axis zeta mode:

$$
\lambda
=
\rho-\frac12,
$$

the horizontal exponential rate:

$$
\Re\lambda
$$

remains visible independently of the shrinking aperture at fixed-power level.

---

# 10. Raw versus corrected energy exponent

Let a broad RH-sensitive aperture $H_0$ be fixed.

Let a fine aperture satisfy:

$$
h_X
=
H_0X^{-\alpha+o(1)}.
$$

Then:

$$
m_X
=
\frac{H_0}{h_X}
=
X^{\alpha+o(1)}.
$$

Suppose the raw fine-scale energy satisfies:

$$
\boxed{
E_{\rm fine}(X)
\ll
X^{\beta_{\rm raw}+o(1)}.
}
$$

Multiscale reconstruction gives the broad bound:

$$
\boxed{
E_{\rm broad}(X)
\ll
X^{\beta_{\rm raw}+4\alpha+o(1)}.
}
$$

Define:

$$
\boxed{
\beta_{\rm corrected}
=
\beta_{\rm raw}+4\alpha.
}
$$

This is the safe RH-sensitive exponent transported back to a fixed aperture.

---

# 11. Corrected $\kappa$

v2.1 used:

$$
\kappa=1-\beta.
$$

If a shrinking-aperture theorem superficially suggests:

$$
\kappa_{\rm raw}
=
1-\beta_{\rm raw},
$$

then the sensitivity-corrected saving is:

$$
\boxed{
\kappa_{\rm corrected}
=
\kappa_{\rm raw}
-
4\alpha.
}
$$

For a second-order filter:

```text
RAW SAVING
-
APERTURE ENERGY ATTENUATION
=
RH-SENSITIVE SAVING.
```

A positive RH-sensitive breakthrough requires:

$$
\boxed{
\kappa_{\rm raw}
>
4\alpha.
}
$$

---

# 12. General filter-order law

Suppose a local filter annihilates polynomial memory through degree:

$$
r-1.
$$

Its first nonzero aperture response is order:

$$
h^r.
$$

If:

$$
h_X
\asymp
X^{-\alpha},
$$

then:

- amplitude attenuation:
  $$
  X^{-r\alpha};
  $$
- energy attenuation:
  $$
  X^{-2r\alpha}.
  $$

Therefore the general sensitivity correction is:

$$
\boxed{
\beta_{\rm corrected}
=
\beta_{\rm raw}
+
2r\alpha,
}
$$

and:

$$
\boxed{
\kappa_{\rm corrected}
=
\kappa_{\rm raw}
-
2r\alpha.
}
$$

For the affine-memory-erasing second difference:

$$
r=2,
$$

recovering:

$$
4\alpha.
$$

---

# 13. Additive symmetry normalization

Consider:

$$
\Sigma_H(x)
=
\psi(x+H)-2\psi(x)+\psi(x-H).
$$

Let:

$$
r=\frac Hx.
$$

v2.2 showed that a zero mode contributes:

$$
\Sigma_{\rho,H}(x)
=
-\frac{x^\rho}{\rho}
\left[
(1+r)^\rho+(1-r)^\rho-2
\right].
$$

For:

$$
r\to0,
$$

$$
\Sigma_{\rho,H}(x)
\sim
-(\rho-1)r^2x^\rho.
$$

Therefore the sensitivity-normalized additive symmetry is:

$$
\boxed{
\widetilde\Sigma_H(x)
=
r^{-2}
x^{-1/2}
\Sigma_H(x).
}
$$

For a fixed zero:

$$
\rho=\frac12+\delta+i\gamma,
$$

$$
\boxed{
\widetilde\Sigma_{\rho,H}(x)
\sim
-(\rho-1)
x^{\delta+i\gamma}.
}
$$

The shrinking-window attenuation is gone.

---

# 14. Correct way to audit a short-interval mean square

Suppose a theorem gives:

$$
I_\Lambda(X,H)
=
\int_X^{2X}
|\Sigma_H(x)|^2dx
\le
\mathcal B(X,H).
$$

The RH-sensitive normalized block energy is not:

$$
\frac{
I_\Lambda(X,H)
}{
X^2
}.
$$

It is approximately:

$$
\boxed{
\mathcal E_{\rm sens}(X,H)
\asymp
\left(
\frac XH
\right)^4
\frac{
I_\Lambda(X,H)
}{
X^2
}.
}
$$

The factor:

$$
\boxed{
(X/H)^4
}
$$

is mandatory for a second-order symmetry statistic.

Any raw power saving that disappears after this rescaling is a false-$\kappa$ effect.

---

# 15. Why strong short-symmetry theorems do not automatically transfer

Coppola's short-interval symmetry work provides strong Large-Sieve-based mean-square estimates.

The 2003 paper explicitly emphasizes that:

- it studies genuinely short intervals;
- the theorem controls an **average of symmetry sums**, not directly the full Selberg variance;
- the author remarks that a sufficiently strong direct symmetry bound would have major consequences for zeta zeros.

The later 2010 paper gives the well-known estimate:

$$
I_\Lambda(N,h)
\ll
NhL^5
+
Nh^{21/20}L^2.
$$

These are important arithmetic cancellation results.

But before translating any such bound into the AMRAL $\kappa$ ladder one must:

1. identify the exact statistic;
2. identify its aperture;
3. apply the sensitivity normalization;
4. preserve the theorem's precise range and averaging structure.

Thus no raw exponent should be promoted directly.

---

# 16. Fejér interpretation

The convex weights:

$$
p_{k,m}
=
\frac{m-|k|}{m^2}
$$

are the normalized Fourier coefficients of the Fejér kernel.

So Theorem 5.1 can be read as:

> coarse sensitivity-normalized second difference = Fejér average of fine sensitivity-normalized second differences.

This provides an intuitive reason for the conservation law.

Shrinking the aperture does not destroy the information if the observable is correctly renormalized.

It merely spreads the broad-scale information across many fine-scale positions.

---

# 17. Information conservation law

The scale tradeoff can now be stated as:

$$
\boxed{
\text{aperture shrink}
+
\text{sensitivity normalization}
+
\text{multiscale aggregation}
=
\text{fixed-aperture information}.
}
$$

Therefore:

$$
\boxed{
\text{apparent short-scale power saving}
}
$$

must be compared only **after** the normalization / aggregation cost is restored.

This is the precise meaning of:

```text
FALSE-KAPPA CONSERVATION LAW.
```

---

# 18. Twisted tent response

Define:

$$
\boxed{
B_h(z)
=
\int_{-h}^{h}
T_h(v)e^{-zv}dv
=
2
\frac{
\cosh(hz)-1
}{
z^2
},
}
$$

with removable value:

$$
B_h(0)=h^2.
$$

For the phase-twisted local prime observable of v2.1, a zero:

$$
\rho
=
\frac12+\delta+i\gamma
$$

contributes a nontrivial-zero term proportional to:

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

---

# 19. Resonance at the zero ordinate

Set:

$$
\tau=\gamma.
$$

Then:

$$
\boxed{
-
B_h(\delta)
X^\delta.
}
$$

Since:

$$
B_h(\delta)
=
2
\frac{
\cosh(h\delta)-1
}{
\delta^2
}
>0
$$

for real:

$$
\delta\neq0,
$$

the vertical oscillation has been completely removed.

Moreover:

$$
\boxed{
\frac{
B_h(\delta)
}{
h^2
}
\to1
}
$$

as:

$$
h\to0.
$$

So after sensitivity normalization, even a shrinking aperture retains full resonant amplitude at the exponential-type level.

This provides a second, independent justification for the $h^{-2}$ normalization.

---

# 20. Uniform twist remains necessary

The multiscale normalization does not eliminate the vertical problem.

A hypothetical off-axis zero at ordinate:

$$
\gamma
$$

is detected most strongly near:

$$
\tau=\gamma.
$$

Therefore:

```text
average over most twists
```

still does not imply:

```text
no resonant exceptional twist.
```

Any fixed-strip theorem must control:

- all required twist blocks; or
- a positive global quantity in which a single resonance cannot hide.

This remains the v2.1 / v2.3 twisted-correlation gate.

---

# 21. A safe theorem-import protocol

For every short-interval / symmetry / large-sieve theorem:

### Step 1

Identify the filter order:

$$
r.
$$

### Step 2

Identify aperture exponent:

$$
\alpha
=
\frac{
\log(X/H)
}{
\log X
}.
$$

### Step 3

Translate the raw bound to its energy exponent:

$$
\beta_{\rm raw}.
$$

### Step 4

Correct:

$$
\boxed{
\beta_{\rm corrected}
=
\beta_{\rm raw}
+
2r\alpha.
}
$$

### Step 5

Compute:

$$
\boxed{
\kappa_{\rm corrected}
=
1-\beta_{\rm corrected}.
}
$$

### Step 6

Audit:

- exact statistic;
- averaging structure;
- vertical twist uniformity;
- boundary terms.

Only if:

$$
\boxed{
\kappa_{\rm corrected}>0
}
$$

after all audits should the theorem be called a fixed-strip progress candidate.

---

# 22. Why exponent-admissible apertures are simpler

If:

$$
\alpha(X)\to0,
$$

then:

$$
2r\alpha(X)\to0.
$$

So raw and corrected fixed-power exponents agree asymptotically.

This recovers v2.2:

$$
\boxed{
H=X^{1-o(1)}
}
$$

is precisely the regime where sensitivity normalization costs only:

$$
X^{o(1)}.
$$

That is why fixed multiplicative windows and subpower Gallagher resolution are the cleanest RH-sensitive scales.

---

# 23. Numerical validation

The reference implementation checks:

1. the exact multiscale identity for several analytic test functions;
2. the convex weights sum to $1$;
3. the raw modal reconstruction ratio approaches $m^2$;
4. the normalized modal response approaches $\lambda^2/2$;
5. the twisted tent normalized response approaches $1$ at resonance;
6. the corrected-$\kappa$ ladder.

These are algebra / normalization checks only.

They are not numerical evidence for RH.

---

# 24. What v2.3 says about the search for $\kappa>0$

The answer is now more precise.

A short-interval theorem may show a large raw power saving.

But the only meaningful question is:

$$
\boxed{
\kappa_{\rm corrected}
=
\kappa_{\rm raw}
-
2r\alpha
>0
\ ?
}
$$

For the v1.6 second-order filter:

$$
\boxed{
\kappa_{\rm corrected}
=
\kappa_{\rm raw}
-
4\alpha.
}
$$

No audited theorem in the present pipeline has yet produced:

$$
\kappa_{\rm corrected}>0
$$

with the required statistic and vertical uniformity.

So the first fixed-strip breakthrough remains open.

---

# 25. Next node

Recommended:

`RH-SensitivityNormalized-TwistedVariance-v2.4`

Fix a concrete aperture family.

Preferred first choice:

$$
\boxed{
h=\log2.
}
$$

Alternative:

$$
H=\frac X{(\log X)^A}.
$$

Then:

1. work only with sensitivity-normalized observables;
2. derive the exact phase-twisted second moment;
3. isolate diagonal / off-diagonal terms;
4. apply large-sieve / dispersion / averaged Hardy–Littlewood inputs;
5. translate every candidate bound through:
   $$
   \kappa_{\rm corrected};
   $$
6. reject any theorem whose saving disappears after normalization;
7. search specifically for a genuinely positive corrected $\kappa$.

---

# 26. GAP ledger

## CLOSED / CORRECTED

### G1. Second-difference multiscale reconstruction

```text
CLOSED
```

### G2. Sensitivity-normalized convex averaging

```text
CLOSED
```

### G3. Raw $m^4$ energy cost

```text
CLOSED
```

### G4. $m^4$ modal sharpness

```text
CLOSED_AS_ASYMPTOTIC_MODAL_SCALE
```

### G5. Second-order corrected $\kappa$

```text
CLOSED
```

$$
\kappa_{\rm corrected}
=
\kappa_{\rm raw}-4\alpha.
$$

### G6. Twisted resonance normalization

```text
CLOSED
```

---

## OPEN

### G7. Any corrected $\kappa>0$

```text
OPEN
```

### G8. Uniform twisted sensitivity-normalized variance

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

# 27. Trust boundary

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE

MULTISCALE_IDENTITY = EXACT
SENSITIVITY_NORMALIZATION = EXACT

RAW_SHORT_INTERVAL_SAVING != RH_PROGRESS
WITHOUT SCALE CORRECTION

NO POSITIVE CORRECTED KAPPA HAS BEEN PROVED

GLOBAL_RH_CERTIFICATE = FALSE
```

Forbidden:

$$
\kappa_{\rm raw}>0
\Longrightarrow
\kappa_{\rm corrected}>0.
$$

Forbidden:

$$
\text{fine-scale variance bound}
\Longrightarrow
\text{broad-scale bound}
$$

without the exact reconstruction / normalization cost.

Forbidden:

$$
\text{average twist control}
\Longrightarrow
\text{all resonance control}.
$$

---

# 28. One-line status

> v2.3 converts the v2.2 aperture-sensitivity warning into an exact multiscale conservation law. For $H=mh$, the broad second difference is the triangular Fejér reconstruction of fine second differences, and after defining the sensitivity-normalized observable $\widetilde D_h=D_h/h^2$, the broad observable becomes an exact convex combination of shifted fine observables. Without this normalization, broad energy can cost $m^4$ relative to fine energy, and this $m^4$ factor is asymptotically sharp on exponential zero modes. Therefore a shrinking-aperture theorem with raw energy exponent $\beta_{\rm raw}$ at $h/H=X^{-\alpha}$ has safe RH-sensitive exponent $\beta_{\rm corrected}=\beta_{\rm raw}+4\alpha$, or $\kappa_{\rm corrected}=\kappa_{\rm raw}-4\alpha$. More generally an order-$r$ memory eraser costs $2r\alpha$ at energy level. The same normalization restores the full zero-mode amplitude: at vertical resonance $\tau=\gamma$, the twisted tent response is $-B_h(\delta)X^\delta$ with $B_h(\delta)/h^2\to1$. Thus any future short-interval power saving must be sensitivity-normalized before entering the AMRAL zero-strip ladder. No positive corrected $\kappa$ has yet been proved.

---

# 29. References

1. Giovanni Coppola, **On the symmetry of primes in almost all short intervals**, *Ricerche di Matematica* 52 (2003), 21–29.  
   Public author PDF: https://giovannicoppola.name/files/articoli/10_avp_2003.pdf

2. Giovanni Coppola, **On the symmetry of primes**, arXiv:1009.6121, 2010.  
   https://arxiv.org/abs/1009.6121

3. Giovanni Coppola, **On the Symmetry Integral**, arXiv:1007.1018.  
   https://arxiv.org/abs/1007.1018

4. Giovanni Coppola, Maurizio Laporta, **A modified Gallagher's Lemma**, arXiv:1301.0008.

5. Alessandro Zaccagnini, **Primes in almost all short intervals**, *Acta Arithmetica* 84 (1998), 225–244.

6. AMRAL, **RH-LocalEnergy-CorrelationApertureTradeoff v1.8**.

7. AMRAL, **RH-TwistedLocalCorrelation-ExponentDrop v2.1**.

8. AMRAL, **RH-ApertureAdmissibility-FalseKappaAudit v2.2**.

---

# 30. Provenance

研究主導：Neo.K

v2.3 multiscale reconstruction、sensitivity normalization、corrected-$\kappa$ conservation law、twisted resonance normalization 與 canonical source 整理：ChatGPT / GPT-5.6 Sol

日期：2026-09-03

研究定位：AMRAL 黎曼猜想半自主研究線，第三弧線 multiscale sensitivity / valid power-saving transport 節點。

本文件是 research source artifact，不是 peer-reviewed publication。

所有 claim 必須依 Claim register、GAP ledger 與 Trust boundary 解讀。
