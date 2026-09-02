# NS × X Integral × 24/72 Paradigm in Practice
## Round 60 — Pure Continuous Singular Boundary-Layer Matching / $\nu^{-1/3}$ WKB Transition

- Date: 2026-08-17
- Version: v0.1
- Status: Proof-Route Experiment / Continuous-Only Singular-Matching Branch
- canonical source: UTF-8 Markdown
- canonical math delimiters: inline `$...$`; display `$$...$$`
- Previous round: `NS_X72_Round59_PureContinuous_EndpointJostGraph_RigorousPositiveFunctional_v0.1_2026-08-17.md`
- Current round objective: Round 59 has rigorously proved the $\nu=0$ endpoint Jost/Green functional
  $$
  c_{0,\pm}>0.
  $$
  Remaining gap:
  $$
  a_3(\nu)/\nu
  \to
  c_0
  \qquad
  (\nu\to0^+).
  $$
  This round directly analyzes the singular transition scale between the fixed-$\nu$ minimal tail and the endpoint bounded-neutral tail.
- Primary results:
  1. previous
     $$
     n_{\rm contract}
     \asymp
     \nu^{-1/2}
     $$
     is only the scale where the **crude original-tail Banach estimate** becomes strongly contractive;
  2. actual neutral-to-minimal attenuation occurs much earlier, at a cumulative WKB scale
     $$
     \boxed{
     j_{\rm BL}
     \asymp
     \nu^{-1/3};
     }
     $$
  3. after setting
     $$
     E_j=e_j/\nu,
     $$
     the leading parity-coupled slow pair is
     $$
     \binom{E_{j+1}}{o_{j+1}}
     \approx
     M(a_j)
     \binom{E_j}{o_j},
     $$
     with
     $$
     a_j=
     \frac{16\nu j^2}{K},
     $$
     $$
     M(a)
     =
     \begin{pmatrix}
     1&a\\
     a&1+a^2
     \end{pmatrix};
     $$
  4. the reduced matrix has determinant one and exact stable multiplier
     $$
     \boxed{
     \lambda_-(a)
     =
     e^{-2\operatorname{arsinh}(a/2)};
     }
     $$
  5. for small $a$,
     $$
     \log\lambda_-(a)
     =
     -a
     +
     O(a^3),
     $$
     hence
     $$
     \boxed{
     \prod_{\ell\le j}\lambda_-(a_\ell)
     \approx
     \exp
     \left[
     -
     \frac{16\nu}{3K}
     j^3
     \right];
     }
     $$
  6. predicted half-decay scale
     $$
     \boxed{
     j_{1/2}
     \sim
     \left(
     \frac{
     3K\log2
     }{
     16\nu
     }
     \right)^{1/3};
     }
     $$
  7. direct sparse solves of the **full rescaled recurrence** show observed half-decay / predicted half-decay ratios approaching $1$ on both source fibres;
  8. at $\nu=10^{-7}$ the ratios are approximately
     $$
     0.9873
     $$
     and
     $$
     0.9954;
     $$
  9. the matching geometry now has three distinct scales:
     $$
     \boxed{
     1
     \ll
     j
     \ll
     \nu^{-1/3}
     }
     $$
     endpoint/Jost outer region,
     $$
     \boxed{
     j\sim\nu^{-1/3}
     }
     $$
     WKB attenuation layer, and
     $$
     \boxed{
     j\gtrsim\nu^{-1/2}
     }
     $$
     strongly contractive deep minimal tail;
  10. choosing an overlap
      $$
      j_{\rm m}
      =
      \nu^{-1/4}
      $$
      leaves both cumulative viscous attenuation and algebraic coefficient-tail errors asymptotically small, suggesting a coarse matching error
      $$
      O(\nu^{1/4})
      $$
      after a rigorous dichotomy-roughness argument.
- Non-claims: This round does **not** yet promote
  $$
  a_3(\nu)/\nu\to c_0
  $$
  to a theorem. The $2\times2$ reduced slow-pair law and its multiplier are exact for the leading boundary-layer model; the full recurrence numerical collapse strongly validates the scale. The remaining rigorous task is stable-bundle / graph matching with controlled $O(j^{-2})$ errors across the near-neutral WKB layer.

---

# 0. Round 59 handoff

Round 59 endpoint Green functional:

$$
\boxed{
c_{0,-}
\in
[
5.7905255784226477185,\,
5.7905255784226477186
],
}
\tag{0.1}
$$

$$
\boxed{
c_{0,+}
\in
[
5.3317525432722412395,\,
5.3317525486723752263
].
}
\tag{0.2}
$$

Thus:

$$
\boxed{
c_{0,\pm}>0
}
\tag{0.3}
$$

rigorously.

The only small-viscosity gap:

$$
\boxed{
a_3(\nu)/\nu
\longrightarrow
c_0.
}
\tag{0.4}
$$

Round 59 STOP:

$$
\boxed{
\text{STOP-C63}
=
\text{Singular Minimal-to-Jost Matching Gap}.
}
$$

---

# 1. Rescaled small-viscosity recurrence

Round 58 rescaling:

$$
\boxed{
u_{2j}=e_j,
}
\tag{1.1}
$$

$$
\boxed{
u_{2j+1}
=
\nu o_j.
}
\tag{1.2}
$$

For large Fourier level:

$$
n,
$$

Rounds 53–58 give:

$$
\boxed{
A_{-2}^{(n)}
=
-\frac{
K^3
}{
n^2
}
+
O(n^{-3}),
}
\tag{1.3}
$$

$$
\boxed{
A_0^{(n)}
=
4K
+
O(n^{-1}),
}
\tag{1.4}
$$

$$
\boxed{
A_2^{(n)}
=
4K
+
O(n^{-1}),
}
\tag{1.5}
$$

$$
\boxed{
A_4^{(n)}
=
-\frac{
K^3
}{
n^2
}
+
O(n^{-3}),
}
\tag{1.6}
$$

and:

$$
\boxed{
b_n
=
-16n^2
[
1+O(n^{-1})
].
}
\tag{1.7}
$$

The rescaled equations are:

$$
\boxed{
\begin{aligned}
0
={}&
-
A_{-2}^{(2j)}
e_{j-1}
+
A_0^{(2j)}
e_j
-
A_2^{(2j)}
e_{j+1}
\\
&+
A_4^{(2j)}
e_{j+2}
-
\nu^2
b_{2j}
o_j,
\end{aligned}
}
\tag{1.8}
$$

and:

$$
\boxed{
\begin{aligned}
0
={}&
-
A_{-2}^{(2j+1)}
o_{j-1}
+
A_0^{(2j+1)}
o_j
\\
&-
b_{2j+1}
e_{j+1}
-
A_2^{(2j+1)}
o_{j+1}
+
A_4^{(2j+1)}
o_{j+2}.
\end{aligned}
}
\tag{1.9}
$$

---

# 2. Why $\nu^{-1/2}$ was not the matching-layer scale

Round 57 tail contraction:

$$
q_n(K,\nu)
\sim
\frac{
K
}{
2\nu n^2
}.
$$

Hence:

$$
q_n<1
$$

once:

$$
n
\gtrsim
\nu^{-1/2}.
$$

But this only says the **solve-for-next-coefficient Banach map** has become contractive.

It does not say the neutral odd plateau waits until that depth before it begins to attenuate.

The actual attenuation is cumulative and begins through a small per-step stable multiplier long before:

$$
q_n
$$

becomes much smaller than one.

Therefore distinguish:

$$
\boxed{
n_{\rm contract}
\asymp
\nu^{-1/2}
}
\tag{2.1}
$$

from:

$$
\boxed{
j_{\rm BL}
\asymp
\nu^{-1/3}.
}
\tag{2.2}
$$

---

# 3. Slow parity-pair scaling

Define:

$$
\boxed{
E_j
=
e_j/\nu.
}
\tag{3.1}
$$

In the transition region:

$$
j\to\infty,
\qquad
\nu\to0^+,
$$

retain the dominant:

$$
A_0,
A_2,
b
$$

terms and use:

$$
n\approx2j.
$$

Equation (1.8) gives:

$$
\boxed{
E_{j+1}
=
E_j
+
a_j
o_j
+
\text{lower-order terms},
}
\tag{3.2}
$$

and (1.9) gives:

$$
\boxed{
o_{j+1}
=
o_j
+
a_j
E_{j+1}
+
\text{lower-order terms},
}
\tag{3.3}
$$

where:

$$
\boxed{
a_j
=
\frac{
16\nu j^2
}{
K
}.
}
\tag{3.4}
$$

The neglected same-parity far-neighbor terms are:

$$
O(j^{-2})
$$

relative to the order-one diagonal coefficients.

---

# 4. Reduced boundary-layer transfer matrix

Ignoring the:

$$
O(j^{-2})
$$

terms gives:

$$
\boxed{
\begin{pmatrix}
E_{j+1}
\\
o_{j+1}
\end{pmatrix}
=
M(a_j)
\begin{pmatrix}
E_j
\\
o_j
\end{pmatrix},
}
\tag{4.1}
$$

with:

$$
\boxed{
M(a)
=
\begin{pmatrix}
1&a
\\
a&1+a^2
\end{pmatrix}.
}
\tag{4.2}
$$

Its determinant:

$$
\boxed{
\det M(a)=1.
}
\tag{4.3}
$$

Trace:

$$
\boxed{
\operatorname{tr}M(a)
=
2+a^2.
}
\tag{4.4}
$$

Therefore the two multipliers are positive reciprocal roots:

$$
\boxed{
\lambda_\pm(a)
=
\frac{
2+a^2
\pm
a\sqrt{a^2+4}
}{
2
}.
}
\tag{4.5}
$$

---

# 5. Exact stable multiplier

Use:

$$
\sqrt{
1+\frac{a^2}{4}
}
-
\frac a2
=
e^{-\operatorname{arsinh}(a/2)}.
$$

Then:

$$
\boxed{
\lambda_-(a)
=
\left[
\frac{
\sqrt{a^2+4}-a
}{
2
}
\right]^2
}
\tag{5.1}
$$

and hence:

$$
\boxed{
\lambda_-(a)
=
e^{-2\operatorname{arsinh}(a/2)}.
}
\tag{5.2}
$$

Named:

$$
\boxed{
\textbf{Slow-Pair Exact Stable Multiplier}.
}
$$

This identity is exact for the reduced boundary-layer matrix.

---

# 6. Small-$a$ WKB expansion

As:

$$
a\to0,
$$

$$
\boxed{
2\operatorname{arsinh}(a/2)
=
a
-
\frac{
a^3
}{
24
}
+
O(a^5).
}
\tag{6.1}
$$

Therefore:

$$
\boxed{
\log
\lambda_-(a)
=
-a
+
\frac{
a^3
}{
24
}
+
O(a^5).
}
\tag{6.2}
$$

For:

$$
a_j
=
16\nu j^2/K,
$$

the cumulative leading exponent is:

$$
\boxed{
\sum_{\ell=1}^j
a_\ell
=
\frac{
16\nu
}{
K
}
\sum_{\ell=1}^j
\ell^2.
}
\tag{6.3}
$$

Thus:

$$
\boxed{
\sum_{\ell=1}^j
a_\ell
=
\frac{
16\nu
}{
3K
}
j^3
+
O(\nu j^2).
}
\tag{6.4}
$$

---

# 7. WKB attenuation law

The reduced stable envelope satisfies:

$$
\boxed{
\prod_{\ell=1}^j
\lambda_-(a_\ell)
=
\exp
\left[
-
2
\sum_{\ell=1}^j
\operatorname{arsinh}
\left(
\frac{
8\nu\ell^2
}{
K
}
\right)
\right].
}
\tag{7.1}
$$

In the pre-transition regime:

$$
\nu j^2\ll1,
$$

$$
\boxed{
\prod_{\ell=1}^j
\lambda_-(a_\ell)
=
\exp
\left[
-
\frac{
16\nu
}{
3K
}
j^3
+
O(
\nu j^2
+
\nu^3j^7
)
\right].
}
\tag{7.2}
$$

Named:

$$
\boxed{
\textbf{Cubic WKB Attenuation Law}.
}
$$

---

# 8. Boundary-layer scale

A finite order-one attenuation occurs when:

$$
\frac{
16\nu
}{
3K
}
j^3
=
O(1).
$$

Therefore:

$$
\boxed{
j_{\rm BL}
\asymp
\left(
\frac K\nu
\right)^{1/3}.
}
\tag{8.1}
$$

For half-decay, set the leading exponent to:

$$
\log2.
$$

Then:

$$
\boxed{
j_{1/2}^{\rm WKB}
=
\left(
\frac{
3K\log2
}{
16\nu
}
\right)^{1/3}.
}
\tag{8.2}
$$

This is the principal new scale of Round 60.

---

# 9. Full recurrence direct-solve diagnostic

The attached verification script solves the complete rescaled recurrence:

- no reduced $2\times2$ truncation;
- both far-neighbor:
  $$
  A_{-2},
  \quad
  A_4
  $$
  channels included;
- full viscosity parameter included;
- sparse finite section taken deep beyond the observed attenuation layer.

To define a half-decay diagnostic, the endpoint plateau magnitude:

$$
|L|
$$

is estimated from the direct $\nu=0$ endpoint BVP at a deep pre-cutoff location.

Then:

$$
j_{1/2}^{\rm obs}
$$

is the last index where:

$$
|o_j|
>
|L|/2.
$$

---

# 10. Small source fibre WKB collapse

For:

$$
K_-
=
\sqrt{17}-3,
$$

the observed versus predicted scale is:

$$
\boxed{
\begin{array}{c|c|c|c}
\nu
&
j_{1/2}^{\rm obs}
&
j_{1/2}^{\rm WKB}
&
j_{\rm obs}/j_{\rm WKB}
\\
\hline
10^{-3}
&
4
&
5.2652
&
0.7597
\\
10^{-4}
&
10
&
11.3436
&
0.8816
\\
10^{-5}
&
23
&
24.4389
&
0.9411
\\
10^{-6}
&
52
&
52.6521
&
0.9876
\\
10^{-7}
&
112
&
113.4355
&
0.9873
\end{array}
}
\tag{10.1}
$$

The convergence toward the cubic WKB scale is clear.

---

# 11. Large source fibre WKB collapse

For:

$$
K_+
=
\sqrt{17}+3,
$$

$$
\boxed{
\begin{array}{c|c|c|c}
\nu
&
j_{1/2}^{\rm obs}
&
j_{1/2}^{\rm WKB}
&
j_{\rm obs}/j_{\rm WKB}
\\
\hline
10^{-4}
&
19
&
20.9974
&
0.9049
\\
10^{-5}
&
44
&
45.2375
&
0.9726
\\
10^{-6}
&
96
&
97.4613
&
0.9850
\\
10^{-7}
&
209
&
209.9739
&
0.9954
\end{array}
}
\tag{11.1}
$$

At:

$$
\nu=10^{-3},
$$

the full profile never develops a sufficiently clean half-plateau before attenuation, so that point is intentionally omitted from the ratio table.

---

# 12. Three-scale singular geometry

Round 60 distinguishes three different Floquet depths.

## S1 — outer endpoint/Jost region

$$
\boxed{
1
\ll
j
\ll
\nu^{-1/3}.
}
\tag{12.1}
$$

Here:

$$
\sum_{\ell\le j}
a_\ell
=
o(1),
$$

so the neutral plateau is only weakly attenuated.

## S2 — WKB attenuation layer

$$
\boxed{
j
\sim
\nu^{-1/3}.
}
\tag{12.2}
$$

Here cumulative stable decay becomes order one.

## S3 — strongly contractive deep tail

$$
\boxed{
j
\gtrsim
\nu^{-1/2}.
}
\tag{12.3}
$$

Here the crude original recurrence Banach coefficient:

$$
q_n
$$

is already strictly below one with a strong margin.

Thus:

$$
\boxed{
\nu^{-1/3}
\ll
\nu^{-1/2}
}
$$

as:

$$
\nu\to0^+.
$$

The matching transition occurs before the deep contraction regime.

---

# 13. Why an overlap region exists

Choose:

$$
\boxed{
j_{\rm m}
=
\nu^{-1/4}.
}
\tag{13.1}
$$

Then:

$$
\boxed{
j_{\rm m}
\to\infty
}
$$

but:

$$
\boxed{
j_{\rm m}
\ll
\nu^{-1/3}.
}
$$

The cumulative reduced viscous attenuation to this depth is:

$$
\boxed{
\nu j_{\rm m}^3
=
\nu^{1/4}
\to0.
}
\tag{13.2}
$$

The sum of algebraic far-neighbor coefficient errors from this depth outward is of order:

$$
\boxed{
\sum_{j\ge j_{\rm m}}
j^{-2}
=
O(
j_{\rm m}^{-1}
)
=
O(
\nu^{1/4}
).
}
\tag{13.3}
$$

Thus the same exponent:

$$
\nu^{1/4}
$$

appears from both sides of the rough matching estimate.

---

# 14. Coarse matching theorem candidate

The natural rigorous target is now:

$$
\boxed{
\operatorname{dist}
\left(
E_{\nu}^{\min}
(
j_{\rm m}
),
E_0^{\rm Jost}
(
j_{\rm m}
)
\right)
\lesssim
\nu^{1/4},
}
\tag{14.1}
$$

where:

- $E_{\nu}^{\min}$ is the positive-viscosity minimal subspace;
- $E_0^{\rm Jost}$ is the Round 59 endpoint bounded/minimal Jost plane.

If (14.1) is proved, Round 59's strong pullback contraction from:

$$
j_{\rm m}
$$

to the center would give:

$$
\boxed{
\frac{
a_3(\nu)
}{
\nu
}
=
c_0
+
O(
\nu^{1/4}
).
}
\tag{14.2}
$$

This is far weaker than the numerically observed:

$$
O(\nu)
$$

error, but more than sufficient to establish positivity for sufficiently small viscosity.

---

# 15. Numerical central matching is actually much sharper

The full sparse BVP gives:

### small fibre

$$
\boxed{
\frac{
a_3(\nu)
}{
\nu
}
-
c_{0,-}
\approx
10.1371\nu
}
\tag{15.1}
$$

for sufficiently small:

$$
\nu.
$$

### large fibre

$$
\boxed{
\frac{
a_3(\nu)
}{
\nu
}
-
c_{0,+}
\approx
-3.43535\nu.
}
\tag{15.2}
$$

Thus the actual connection appears to possess a first boundary-layer correction of order:

$$
\nu,
$$

much smaller than the proposed coarse:

$$
\nu^{1/4}
$$

rigorous envelope.

This suggests substantial cancellation beyond the crude roughness estimate.

---

# 16. Exact reduced-model stable eigenvector

For:

$$
M(a),
$$

the stable eigenvector can be taken as:

$$
\boxed{
v_-(a)
=
\begin{pmatrix}
-\dfrac{
a
}{
1-\lambda_-(a)
}
\\
1
\end{pmatrix}.
}
\tag{16.1}
$$

As:

$$
a\to0^+,
$$

$$
\boxed{
v_-(a)
=
\begin{pmatrix}
-1
\\
1
\end{pmatrix}
+
O(a).
}
\tag{16.2}
$$

This fast stable direction is only one part of the full three-dimensional minimal bundle.

The other two branches converge toward the endpoint's minimal-even / bounded-neutral Jost geometry.

Therefore a rigorous proof must track the full three-plane, not only one multiplier.

---

# 17. Why the full stable-plane problem is still nontrivial

The reduced $2\times2$ slow-pair model explains the visible attenuation scale.

But the complete adjoint problem has:

$$
\boxed{
3
\text{ minimal branches}
}
$$

for every:

$$
\nu>0.
$$

At:

$$
\nu=0,
$$

these reorganize into:

1. one superfactorial minimal even mode;
2. one bounded-neutral odd mode;
3. one additional bounded/minimal odd direction in the full Jost plane.

Thus the singular limit is a **Grassmannian matching problem**, not a scalar WKB matching.

The new WKB law identifies the correct transition scale and spectral gap needed for a dichotomy-roughness proof.

---

# 18. Rigorous route through dichotomy roughness

In the WKB layer:

$$
j
\sim
\nu^{-1/3},
$$

the reduced slow spectral gap scales as:

$$
\boxed{
1-\lambda_-
\asymp
a_j
\asymp
\nu^{1/3}.
}
\tag{18.1}
$$

The omitted far-neighbor coefficient scale is:

$$
\boxed{
j^{-2}
\asymp
\nu^{2/3}.
}
\tag{18.2}
$$

Therefore:

$$
\boxed{
\frac{
\text{coefficient perturbation}
}{
\text{slow spectral gap}
}
\asymp
\nu^{1/3}
\to0.
}
\tag{18.3}
$$

This is exactly the scale separation needed for a roughness / graph-transform theorem to compare the full minimal bundle with the reduced WKB bundle through the transition region.

So Round 60 reduces the matching gap to a quantitatively favorable perturbation problem.

---

# 19. STOP-C64 — WKB Stable-Bundle / Rigorous Matching Gap

$$
\boxed{
\begin{aligned}
\text{layer}
&=
\mathrm{small\text{-}viscosity\ boundary\text{-}layer\ matching},
\\
\text{crude deep contraction scale}
&\sim
\nu^{-1/2},
\\
\text{actual attenuation scale}
&\sim
\nu^{-1/3},
\\
a_j
&=
16\nu j^2/K,
\\
M(a)
&=
\begin{pmatrix}
1&a\\
a&1+a^2
\end{pmatrix},
\\
\lambda_-(a)
&=
e^{-2\operatorname{arsinh}(a/2)},
\\
\text{WKB envelope}
&\sim
\exp[
-16\nu j^3/(3K)
],
\\
j_{1/2}
&\sim
[
3K\log2/(16\nu)
]^{1/3},
\\
\text{full recurrence diagnostics}
&=
\mathrm{collapse\ to\ WKB\ scale},
\\
\text{transition spectral gap}
&\sim
\nu^{1/3},
\\
\text{coefficient error}
&\sim
\nu^{2/3},
\\
\text{favorable roughness ratio}
&\sim
\nu^{1/3},
\\
\text{candidate coarse matching}
&=
a_3(\nu)/\nu
=
c_0
+
O(\nu^{1/4}),
\\
\text{numerical actual matching}
&=
c_0
+
O(\nu),
\\
\text{missing}
&=
\mathrm{rigorous\ three\text{-}plane\ dichotomy/graph\ matching}
\\
&\quad
\mathrm{through\ }j\sim\nu^{-1/3},
\\
T_{\mathsf C\to\mathsf D}
&=
\mathrm{NOT\ REACHED}.
\end{aligned}
}
$$

Named:

$$
\boxed{
\textbf{STOP-C64:
WKB Stable-Bundle / Rigorous Matching Gap}.
}
$$

---

# 20. 24/72 Ledger — Round 60

| Step | object | $B$ | $U$ | $O$ | $L$ | status |
|---|---|---|---|---|---|---|
| C961 | deep contraction vs matching-scale distinction | $\mathsf C$ | singular Floquet geometry | relational | $\mathsf F$ | IDENTIFIED |
| C962 | slow parity-pair scaling | $\mathsf C$ | singular rescaling | relational | $\mathsf F$ | DERIVED |
| C963 | reduced $2\times2$ transfer matrix | $\mathsf C$ | boundary-layer dynamics | matrix | $\mathsf F$ | EXACT leading model |
| C964 | exact stable multiplier | $\mathsf C$ | local spectrum | scalar | $\mathsf F$ | PROVED for reduced model |
| C965 | cubic WKB attenuation | $\mathsf C$ | cumulative spectrum | scalar | $\mathsf F$ | DERIVED |
| C966 | $\nu^{-1/3}$ boundary-layer scale | $\mathsf C$ | singular asymptotics | targeted | $\mathsf F$ | DERIVED |
| C967 | WKB half-decay prediction | $\mathsf C$ | asymptotic observable | scalar | $\mathsf F$ | DERIVED |
| C968 | full sparse BVP diagnostics | $\mathsf C$ | exact recurrence numerics | profile | $\mathsf F$ | VERIFIED |
| C969 | small-fibre WKB collapse | $\mathsf C$ | cutoff/parameter test | scalar | $\mathsf F$ | VERIFIED |
| C970 | large-fibre WKB collapse | $\mathsf C$ | cutoff/parameter test | scalar | $\mathsf F$ | VERIFIED |
| C971 | three singular scales | $\mathsf C$ | matching geometry | profile | $\mathsf F$ | IDENTIFIED |
| C972 | overlap $j_m=\nu^{-1/4}$ | $\mathsf C$ | matched asymptotics | scalar | $\mathsf F$ | ROUTE DESIGNED |
| C973 | transition gap/error ratio | $\mathsf C$ | dichotomy roughness | scalar | $\mathsf F$ | DERIVED |
| C974 | full three-plane matching | $\mathsf C$ | Grassmannian graph transform | targeted | $\mathsf F$ | OPEN / STOP-C64 |

---

# 21. Continuous-versus-discrete status

The WKB boundary-layer variable:

$$
\nu^{1/3}j
$$

is a singular scaling coordinate of the continuous periodic Floquet problem.

The integer sideband label is again only the Fourier chart of:

$$
x_3.
$$

The WKB law describes the asymptotic stable bundle of the continuous periodic adjoint operator.

No finite mode counting or discrete physical dynamics is used as closure.

Therefore:

$$
\boxed{
T_{\mathsf C\to\mathsf D}
=
\text{NOT YET REACHED}.
}
$$

---

# 22. Strongest results of Round 60

## R60-A — exact reduced stable multiplier

$$
\boxed{
\lambda_-(a)
=
e^{-2\operatorname{arsinh}(a/2)}.
}
$$

## R60-B — actual boundary-layer scale

$$
\boxed{
j_{\rm BL}
\asymp
\nu^{-1/3},
}
$$

not:

$$
\nu^{-1/2}.
$$

## R60-C — cubic attenuation

$$
\boxed{
\text{stable amplitude}
\sim
\exp
[
-16\nu j^3/(3K)
].
}
$$

## R60-D — full recurrence verifies the scale

At:

$$
\nu=10^{-7},
$$

observed / predicted half-decay ratios are approximately:

$$
\boxed{
0.9873
}
$$

and:

$$
\boxed{
0.9954.
}
$$

## R60-E — favorable transition perturbation ratio

At:

$$
j\sim\nu^{-1/3},
$$

$$
\boxed{
\frac{
j^{-2}
}{
1-\lambda_-
}
\asymp
\nu^{1/3}.
}
$$

Thus full-bundle matching is perturbatively favorable.

## R60-F — singular matching now has a concrete graph-transform target

A coarse route to:

$$
\boxed{
a_3(\nu)/\nu
=
c_0
+
O(\nu^{1/4})
}
$$

has been identified; the actual numerical error appears $O(\nu)$.

---

# 23. Next round — Three-Plane Dichotomy Roughness / Small-Viscosity Positivity

Round 60 has now identified the correct layer and the correct gap-to-error ratio.

The next round should convert this into a true matching theorem.

Concrete targets:

1. write the full six-dimensional rescaled transfer system;
2. choose:
   $$
   j_-
   =
   \nu^{-1/4},
   \qquad
   j_+
   =
   C\nu^{-1/3};
   $$

3. construct the reduced three-dimensional WKB minimal bundle on:
   $$
   [j_-,j_+];
   $$

4. use dichotomy roughness / graph transform to prove full minimal-bundle distance:
   $$
   O(\nu^{1/4});
   $$

5. identify the reduced bundle limit at:
   $$
   j_-
   $$
   with the Round 59 Jost plane;

6. use the Round 59 pullback contraction to propagate the bundle enclosure to the center;

7. conclude:
   $$
   \left|
   a_3(\nu)/\nu-c_0
   \right|
   \le
   C\nu^{1/4};
   $$

8. choose an explicit:
   $$
   \nu_s>0
   $$
   so the bound is smaller than:
   $$
   c_0/2;
   $$

9. thereby prove:
   $$
   a_3(\nu)>0
   $$
   for:
   $$
   0<\nu\le\nu_s.
   $$

This becomes:

$$
\boxed{
\textbf{Three-Plane Dichotomy Roughness / Small-Viscosity Positivity}.
}
$$

---

# 24. External primary-source anchors

1. Frédéric Klopp, Alexander Fedotov, *The complex WKB method for difference equations and Airy functions*, arXiv:1810.04918.
   - develops WKB asymptotics for finite-difference equations with a small parameter and turning-point geometry;
   - relevant methodological context for the discrete/WKB viewpoint, not a source for the NS-specific multiplier.

2. M. I. Ayzatsky, *A note on the WKB solutions of difference equations*, arXiv:1806.02196.
   - compares WKB constructions for difference equations and emphasizes Riccati-based formulations;
   - relevant to the graph/multiplier representation used here.

3. F. Battelli, M. Franca, K. J. Palmer, *Exponential Dichotomy for Noninvertible Linear Difference Equations*, arXiv:2111.04553.
   - proves roughness results for dichotomies under perturbation;
   - relevant framework for the next step of controlling the full stable bundle against the reduced WKB system.

All NS-specific slow-pair formulas, the $\nu^{-1/3}$ scale, half-decay diagnostics and sparse recurrence data in Round 60 are direct derivations / computations of this project.

---

# 25. Commit state

$$
\boxed{
\begin{aligned}
\text{Route}
&=
\mathrm{Pure\ Continuous\ Singular\ Boundary\text{-}Layer\ Matching},
\\
\text{Essential }\mathsf C\to\mathsf D
&=
\mathrm{Not\ reached},
\\
\text{Endpoint positivity}
&=
\mathrm{rigorous},
\\
\text{Actual singular layer}
&=
\nu^{-1/3},
\\
\text{Reduced stable multiplier}
&=
\mathrm{exact},
\\
\text{Full recurrence WKB collapse}
&=
\mathrm{verified},
\\
\text{Transition gap/error ratio}
&=
O(\nu^{1/3}),
\\
\text{Singular matching theorem}
&=
\mathrm{not\ yet\ claimed},
\\
\text{STOP-C64}
&=
\mathrm{WKB\ Stable\text{-}Bundle/Rigorous\ Matching\ Gap},
\\
\text{Next}
&=
\mathrm{Three\text{-}Plane\ Dichotomy\ Roughness/Small\text{-}Viscosity\ Positivity}.
\end{aligned}
}
$$