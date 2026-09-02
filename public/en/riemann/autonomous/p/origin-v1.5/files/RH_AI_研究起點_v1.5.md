# RH AI Research Starting Point v1.5: Mixed-Order Dictionaries and Cross-Regularity Cancellation

- Date: 2026-07-23
- Original Research Concept: Neo.K
- Mathematical Engineering: Aletheia (GPT-5.6 Thinking)
- Status: Non-proof research engineering; no claim that RH is solved

---

## 1. Milestones of this Version

`v1.4` established the duality law of kernel orders: low-order B-splines have higher prime-boundary sensitivity, while high-order B-splines possess better Archimedean tail bounds and certificate conditions.

`v1.5` places two types of regularity into the same real Weil test space for the first time:

$$
v^{(1)}_j=h^{-1/2}\beta_1((x-t_j)/h),
\qquad
v^{(3)}_j=h^{-1/2}\beta_3((x-t_j)/h).
$$

By convolution closure:

$$
1\times1\to\beta_3,
\qquad
1\times3\to\beta_5,
\qquad
3\times3\to\beta_7.
$$

Thus, the same matrix simultaneously carries:

$$
\varepsilon^3,\qquad\varepsilon^5,\qquad\varepsilon^7
$$

three arithmetic activation scales.

---

## 2. The First Mixed-Order Strict Chamber

Fix:

$$
h=\frac3{20},\qquad d=\frac9{40},\qquad N=5\text{ per channel}.
$$

The total dimension is $10$, and the maximum correlation radius is $3/2<\log5$, so the complete von Mangoldt set is exactly:

$$
\{2,3,4\}.
$$

The three types of blocks have different support fields of view, forming a multi-distance arithmetic sensor rather than repeated copies of the same activation map.

---

## 3. Exact Spectral Bounds

A purely rational $LDL^T$ proof for the full mixed interval family shows:

$$
\lambda_{\min}^{\rm mixed}>\frac1{2000}.
$$

A rational integer witness proves:

$$
\lambda_{\min}^{\rm mixed}<\frac1{1000}.
$$

Therefore:

$$
\boxed{
5\times10^{-4}
<\lambda_{\min}^{\rm mixed}
<10^{-3}
}.
$$

Meanwhile, the exact lower bounds for the isolated channels are:

$$
\lambda_{\min}^{(m=3)}>\frac1{250}=0.004,
$$

$$
\lambda_{\min}^{(m=1)}>\frac1{20}=0.05.
$$

Thus, the mixed low mode is not an extension of any single isolated channel.

---

## 4. Cross-Regularity Cancellation Mode

For the exact witness:

$$
Q(c)=Q_{11}(c_1)+2Q_{13}(c_1,c_3)+Q_{33}(c_3).
$$

The verifier proves:

$$
Q_{11}>0,
\qquad
Q_{33}>0,
\qquad
2Q_{13}<0,
\qquad
Q(c)>0.
$$

The cross-block cancellation eliminates approximately $93.4\%$ of the energy from the two self-blocks, leaving a generalized Rayleigh quotient of about:

$$
9.7385\times10^{-4}
$$

Hence, it is formally named:

$$
\boxed{\text{Cross-Regularity Cancellation Mode}}
$$

This demonstrates that the mixed kernel is not merely a "sensor plus certifier," but rather generates novel spectral geometry that does not exist in single-kernel spaces.

---

## 5. Engineering Closure

This version accomplishes:

- Universal B-spline correlation cores of degrees $3,5,7$;
- Three degree-specific Archimedean tail bounds;
- Block-wise prime-power support compilation;
- Exact mixed Gram matrices;
- Exact mixed lower bounds;
- Exact rational witness upper bounds;
- Exact self/cross sign decompositions;
- Independent cross-validation using 80-digit mpmath.

---

## 6. Boundaries and Next Node

This version remains a finite-dimensional certificate:

$$
\text{mixed 10D positivity}\centernot\Longrightarrow RH.
$$

No true Weil negative witness has been found.

Next node:

$$
\boxed{\texttt{RH-W-13-CROSS-REGULARITY-CONTINUATION}}.
$$

We will adaptively adjust along the mixed witness:

$$
h,\qquad d,\qquad \alpha
$$

where $\alpha$ controls the relative scale or preconditioner of the two channels, with the goal of isolating:

- True Weil energy descent;
- Gram near-linear dependence;
- The contribution of the prime-power block to the cancellation direction;
- Stable low spectral bands versus accidental single-point cancellations.