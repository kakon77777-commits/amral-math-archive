# NS × X 積分 × 24/72 範式實戰
## Round 61 — Pure Continuous Fast–Slow Stable-Bundle Factorization / Optimal Matching Exponent

- 日期：2026-08-18
- 版本：v0.1
- 狀態：Proof-Route Experiment / Continuous-Only Fast–Slow Grassmannian Branch
- canonical source：UTF-8 Markdown
- canonical math delimiters：inline `$...$`；display `$$...$$`
- 前一輪：`NS_X72_Round60_PureContinuous_SingularBoundaryLayer_WKBMatching_v0.1_2026-08-17.md`
- 本輪目標：Round 60 已找出真實 small-viscosity attenuation layer
  $$
  j_{\rm BL}\asymp \nu^{-1/3},
  $$
  但其初版 proof-route 使用
  $$
  j_m=\nu^{-1/4}
  $$
  作 matching point。若直接套 dichotomy roughness，該點的 slow-gap / coefficient-error 比值其實只到 $O(1)$，不足以構成嚴格 perturbative parameter。本輪：
  1. 修正 overlap exponent；
  2. 將 full three-dimensional minimal bundle分解成 two fast minimal lines + one slow WKB stable line；
  3. 將 three-plane matching縮成 fast Schur elimination + slow line matching；
  4. 用 full six-dimensional recurrence的 Grassmannian principal-angle diagnostics驗證新尺度。
- 主要結果：
  1. at $\nu=0$，每個 parity 的 large-$j$ cubic factorizes as
     $$
     \epsilon+r-r^2-\epsilon r^3
     =
     -(r-1)
     [
     \epsilon r^2+(1+\epsilon)r+\epsilon
     ],
     \qquad
     \epsilon=\frac{K^2}{16j^2};
     $$
  2. hence each parity has exactly one leading neutral root and one reciprocal fast pair；
  3. the fast roots satisfy
     $$
     r_{\rm fast}^{\min}
     =
     -\epsilon+O(\epsilon^2),
     \qquad
     r_{\rm fast}^{\max}
     =
     -\epsilon^{-1}+O(1);
     $$
  4. small viscosity couples only the two neutral directions at leading order，producing Round 60's slow $2\times2$ matrix；
  5. therefore the positive-viscosity three-dimensional minimal bundle has the asymptotic decomposition
     $$
     \boxed{
     E_\nu^{\min}
     =
     E_{\rm fast,e}^{\min}
     \oplus
     E_{\rm fast,o}^{\min}
     \oplus
     E_{\rm slow}^{-};
     }
     $$
  6. the two fast lines remain uniformly separated from the unit-circle slow dynamics and can be Schur-eliminated before the singular WKB matching；
  7. for a general overlap
     $$
     j_m=\nu^{-\alpha},
     $$
     three conservative errors are
     $$
     \nu^{1-3\alpha},
     \qquad
     \nu^{4\alpha-1},
     \qquad
     \nu^\alpha;
     $$
  8. balancing the two limiting exponents gives
     $$
     \boxed{
     \alpha_\ast=\frac27;
     }
     $$
  9. thus the first self-consistent rigorous overlap is
     $$
     \boxed{
     j_m=\nu^{-2/7},
     }
     $$
     with conservative bundle-matching error
     $$
     \boxed{
     O(\nu^{1/7});
     }
     $$
  10. the Round 60 choice $\alpha=1/4$ is retained as a useful diagnostic scale，but not as the preferred direct roughness proof scale；
  11. full 6D stable-plane principal-angle calculations at
      $$
      j_m=\nu^{-2/7}
      $$
      show convergence substantially faster than the conservative $\nu^{1/7}$ envelope；
  12. for $\nu=10^{-7}$ the largest principal angles are approximately
      $$
      7.27\times10^{-3}
      $$
      and
      $$
      2.14\times10^{-3}
      $$
      for the two source fibres；
  13. numerical log-slopes over the smallest three tested viscosities are approximately
      $$
      0.44
      $$
      and
      $$
      0.61,
      $$
      again much faster than $1/7$；
  14. the remaining proof obligation is now a quantitative **fast Schur graph + slow WKB graph transform**，not an opaque three-plane dichotomy theorem。
- 非主張：本輪 does not yet prove
  $$
  a_3(\nu)/\nu\to c_0.
  $$
  The factorization and exponent optimization are analytic；the full Grassmannian convergence rates are numerical diagnostics。The next round must turn the fast–slow decomposition into explicit invariant graph bounds and a rigorous small-viscosity positivity interval。

---

# 0. Round 60 handoff

Round 60 slow pair：

$$
\boxed{
\begin{pmatrix}
E_{j+1}\\
o_{j+1}
\end{pmatrix}
\approx
M(a_j)
\begin{pmatrix}
E_j\\
o_j
\end{pmatrix},
}
\tag{0.1}
$$

where：

$$
\boxed{
E_j=e_j/\nu,
}
\tag{0.2}
$$

$$
\boxed{
a_j=\frac{16\nu j^2}{K},
}
\tag{0.3}
$$

and：

$$
\boxed{
M(a)
=
\begin{pmatrix}
1&a\\
a&1+a^2
\end{pmatrix}.
}
\tag{0.4}
$$

Exact stable multiplier：

$$
\boxed{
\lambda_-(a)
=
e^{-2\operatorname{arsinh}(a/2)}.
}
\tag{0.5}
$$

Cubic WKB envelope：

$$
\boxed{
\exp
\left[
-\frac{16\nu}{3K}j^3
\right].
}
\tag{0.6}
$$

Thus：

$$
\boxed{
j_{\rm BL}
\asymp
\nu^{-1/3}.
}
\tag{0.7}
$$

Round 60 STOP：

$$
\boxed{
\text{STOP-C64}
=
\text{WKB Stable-Bundle / Rigorous Matching Gap}.
}
$$

---

# 1. Zero-viscosity parity cubic

Consider either parity sector at：

$$
\nu=0.
$$

The leading same-parity recurrence has：

$$
A_{-2}^{(2j)}
\sim
-\frac{K^3}{4j^2},
$$

$$
A_0^{(2j)}
\sim
4K,
$$

$$
A_2^{(2j)}
\sim
4K,
$$

$$
A_4^{(2j)}
\sim
-\frac{K^3}{4j^2}.
$$

After dividing by：

$$
4K
$$

and defining：

$$
\boxed{
\epsilon_j
=
\frac{K^2}{16j^2},
}
\tag{1.1}
$$

the leading frozen recurrence is：

$$
\boxed{
\epsilon_j x_{j-1}
+
x_j
-
x_{j+1}
-
\epsilon_j x_{j+2}
=
0.
}
\tag{1.2}
$$

For：

$$
x_j=r^j,
$$

$$
\boxed{
\epsilon+r-r^2-\epsilon r^3=0.
}
\tag{1.3}
$$

---

# 2. Exact leading factorization

The cubic factorizes exactly：

$$
\boxed{
\epsilon+r-r^2-\epsilon r^3
=
-(r-1)
\left[
\epsilon r^2
+
(1+\epsilon)r
+
\epsilon
\right].
}
\tag{2.1}
$$

Therefore one root is：

$$
\boxed{
r_0=1.
}
\tag{2.2}
$$

The remaining roots：

$$
\boxed{
r_\pm
=
\frac{
-(1+\epsilon)
\pm
\sqrt{
1+2\epsilon-3\epsilon^2
}
}{
2\epsilon
}.
}
\tag{2.3}
$$

Their product：

$$
\boxed{
r_+r_-=1.
}
\tag{2.4}
$$

---

# 3. Fast reciprocal pair

As：

$$
\epsilon\to0^+,
$$

the small root is：

$$
\boxed{
r_{\rm fast}^{\min}
=
-\epsilon
+
O(\epsilon^2),
}
\tag{3.1}
$$

and the reciprocal growing root is：

$$
\boxed{
r_{\rm fast}^{\max}
=
-\epsilon^{-1}
+
O(1).
}
\tag{3.2}
$$

Hence：

$$
\boxed{
|r_{\rm fast}^{\min}|
\asymp
j^{-2},
}
\tag{3.3}
$$

while：

$$
\boxed{
|r_{\rm fast}^{\max}|
\asymp
j^2.
}
\tag{3.4}
$$

The fast pair is therefore parametrically far from the neutral root：

$$
r_0=1.
$$

---

# 4. Endpoint admissible decomposition

At：

$$
\nu=0,
$$

each parity contributes：

$$
\boxed{
1\text{ neutral}
+
1\text{ fast minimal}
+
1\text{ fast growing}.
}
\tag{4.1}
$$

The Round 58–59 endpoint selection is not the whole bounded four-plane。

It chooses：

1. the even fast-minimal line；
2. the odd fast-minimal line；
3. the odd bounded-neutral Jost direction；

while excluding the even neutral direction。

Thus the endpoint selected three-plane is：

$$
\boxed{
E_0^{\rm Jost}
=
E_{\rm fast,e}^{\min}
\oplus
E_{\rm fast,o}^{\min}
\oplus
E_{\rm neutral,o}^{\rm Jost}.
}
\tag{4.2}
$$

---

# 5. Positive-viscosity minimal bundle

For：

$$
\nu>0,
$$

the two neutral parity directions couple through the viscous cross-parity term。

At leading order they become：

$$
\boxed{
1\text{ slow stable}
+
1\text{ slow unstable}.
}
\tag{5.1}
$$

The two fast minimal parity lines persist because their frozen moduli are：

$$
O(j^{-2}),
$$

well separated from the unit-scale slow dynamics。

Therefore：

$$
\boxed{
E_\nu^{\min}
=
E_{\rm fast,e}^{\min}(\nu)
\oplus
E_{\rm fast,o}^{\min}(\nu)
\oplus
E_{\rm slow}^{-}(\nu).
}
\tag{5.2}
$$

命名：

$$
\boxed{
\textbf{Fast–Slow Three-Bundle Factorization}.
}
$$

---

# 6. Why this reduces the proof burden

A black-box three-dimensional Grassmannian comparison treats all directions equally。

But the fast directions have：

$$
\boxed{
\text{stable multiplier}
\asymp
j^{-2}
}
$$

and reciprocal unstable multiplier：

$$
\asymp
j^2.
$$

Their stable/unstable gap is therefore order one or larger。

Only the slow neutral pair has a vanishing gap：

$$
\boxed{
1-\lambda_-
\asymp
a_j
=
\nu j^2.
}
\tag{6.1}
$$

Thus the rigorous strategy should be：

1. Schur-eliminate the fast stable/growing blocks with uniform bounds；
2. derive an effective slow $2\times2$ graph equation；
3. apply WKB / dichotomy roughness only to that slow graph；
4. reconstruct the full stable three-plane afterward。

This turns the singular part of the proof from dimension three to dimension one stable-versus-unstable matching。

---

# 7. General overlap exponent

Let：

$$
\boxed{
j_m
=
\nu^{-\alpha}.
}
\tag{7.1}
$$

To lie before the attenuation layer：

$$
j_m
\ll
\nu^{-1/3},
$$

we require：

$$
\boxed{
\alpha<1/3.
}
\tag{7.2}
$$

To make the slow spectral gap dominate the algebraic far-neighbor scale：

$$
\nu j_m^2
\gg
j_m^{-2},
$$

we require：

$$
\boxed{
\alpha>1/4.
}
\tag{7.3}
$$

Hence any direct perturbative overlap must satisfy：

$$
\boxed{
\frac14
<
\alpha
<
\frac13.
}
\tag{7.4}
$$

This excludes the endpoint value：

$$
\alpha=\frac14
$$

as the preferred direct roughness scale。

---

# 8. Three conservative matching errors

At：

$$
j_m=\nu^{-\alpha},
$$

the cumulative slow attenuation before matching is：

$$
\boxed{
\nu j_m^3
=
\nu^{1-3\alpha}.
}
\tag{8.1}
$$

The local far-neighbor perturbation relative to the slow gap is：

$$
\boxed{
\frac{
j_m^{-2}
}{
\nu j_m^2
}
=
\nu^{4\alpha-1}.
}
\tag{8.2}
$$

A deliberately coarse accumulated endpoint algebraic-tail allowance is：

$$
\boxed{
j_m^{-1}
=
\nu^\alpha.
}
\tag{8.3}
$$

Therefore define：

$$
\boxed{
\beta(\alpha)
=
\min
\{
1-3\alpha,\,
4\alpha-1,\,
\alpha
\}.
}
\tag{8.4}
$$

A first direct roughness proof can aim for：

$$
\boxed{
\operatorname{dist}
(
E_\nu^{\min},
E_0^{\rm Jost}
)
=
O(
\nu^{\beta(\alpha)}
).
}
\tag{8.5}
$$

---

# 9. Optimal overlap exponent

On：

$$
1/4<\alpha<1/3,
$$

the algebraic exponent：

$$
\alpha
$$

is larger than the two competing singular exponents near the optimum。

So optimize by balancing：

$$
\boxed{
1-3\alpha
=
4\alpha-1.
}
\tag{9.1}
$$

Hence：

$$
\boxed{
7\alpha=2,
}
$$

and：

$$
\boxed{
\alpha_\ast
=
\frac27.
}
\tag{9.2}
$$

At this value：

$$
\boxed{
1-3\alpha_\ast
=
4\alpha_\ast-1
=
\frac17.
}
\tag{9.3}
$$

while：

$$
\boxed{
\alpha_\ast
=
\frac27
>
\frac17.
}
\tag{9.4}
$$

Therefore：

$$
\boxed{
\beta_\ast
=
\frac17.
}
\tag{9.5}
$$

命名：

$$
\boxed{
\textbf{Optimal $2/7$ Matching Law}.
}
$$

---

# 10. Corrected first rigorous target

The first self-consistent coarse theorem target is therefore：

$$
\boxed{
j_m
=
\nu^{-2/7},
}
\tag{10.1}
$$

and：

$$
\boxed{
\operatorname{dist}
\left(
E_\nu^{\min}(j_m),
E_0^{\rm Jost}(j_m)
\right)
\le
C
\nu^{1/7}.
}
\tag{10.2}
$$

If the Round 59 center pullback is Lipschitz in the relevant Grassmann chart，then：

$$
\boxed{
\left|
\frac{
a_3(\nu)
}{
\nu
}
-
c_0
\right|
\le
C_\ast
\nu^{1/7}.
}
\tag{10.3}
$$

This would already prove：

$$
a_3(\nu)>0
$$

for sufficiently small positive viscosity。

---

# 11. Relation to Round 60's $\nu^{-1/4}$ diagnostic

Round 60 chose：

$$
j_m=\nu^{-1/4}.
$$

At that scale：

$$
\nu j_m^3
=
\nu^{1/4},
$$

and：

$$
j_m^{-1}
=
\nu^{1/4}.
$$

Those two errors are small。

However：

$$
\boxed{
\frac{
j_m^{-2}
}{
\nu j_m^2
}
=
1.
}
\tag{11.1}
$$

So the slow-gap roughness ratio does not vanish。

Thus：

$$
\nu^{-1/4}
$$

remains useful for numerical overlap diagnostics but is not the cleanest scale for a direct theorem based solely on gap-versus-error perturbation。

---

# 12. Six-dimensional Grassmannian diagnostic

To test the new proof geometry without compact hidden-block coordinate redundancy，the verification script works directly with the full six-dimensional parity-rescaled transfer state：

$$
\boxed{
Y_j
=
(
e_{j+1},
e_j,
e_{j-1},
o_{j+1},
o_j,
o_{j-1}
)^T.
}
\tag{12.1}
$$

For：

$$
\nu>0,
$$

the local deep-tail transfer is frozen at a large cutoff，its three smallest-modulus eigenvectors initialize the minimal three-plane，and that plane is propagated backward with repeated QR orthogonalization。

At：

$$
\nu=0,
$$

the comparison plane is built as：

- one even minimal line；
- the two-dimensional odd bounded plane；

then propagated to the same matching index。

The largest principal angle：

$$
\boxed{
\theta_{\max}
(
E_\nu^{\min},
E_0^{\rm Jost}
)
}
$$

is the diagnostic。

---

# 13. Small source fibre principal angles

For：

$$
K_-=\sqrt{17}-3,
$$

at：

$$
j_m
=
\operatorname{round}
(
\nu^{-2/7}
),
$$

the full six-dimensional diagnostics are：

$$
\boxed{
\begin{array}{c|c|c|c}
\nu
&
j_m
&
\theta_{\max}
&
\theta_{\max}/\nu^{1/7}
\\
\hline
10^{-3}
&
7
&
4.0018\times10^{-1}
&
1.0736
\\
10^{-4}
&
14
&
1.5765\times10^{-1}
&
5.8764\times10^{-1}
\\
10^{-5}
&
27
&
5.5745\times10^{-2}
&
2.8873\times10^{-1}
\\
10^{-6}
&
52
&
2.0005\times10^{-2}
&
1.4397\times10^{-1}
\\
10^{-7}
&
100
&
7.2661\times10^{-3}
&
7.2661\times10^{-2}
\end{array}
}
\tag{13.1}
$$

The conservative：

$$
\nu^{1/7}
$$

envelope is therefore not saturated。

---

# 14. Large source fibre principal angles

For：

$$
K_+=\sqrt{17}+3,
$$

$$
\boxed{
\begin{array}{c|c|c|c}
\nu
&
j_m
&
\theta_{\max}
&
\theta_{\max}/\nu^{1/7}
\\
\hline
10^{-3}
&
7
&
7.4004\times10^{-1}
&
1.9853
\\
10^{-4}
&
14
&
1.6917\times10^{-1}
&
6.3061\times10^{-1}
\\
10^{-5}
&
27
&
3.4820\times10^{-2}
&
1.8035\times10^{-1}
\\
10^{-6}
&
52
&
8.1205\times10^{-3}
&
5.8442\times10^{-2}
\\
10^{-7}
&
100
&
2.1440\times10^{-3}
&
2.1440\times10^{-2}
\end{array}
}
\tag{14.1}
$$

Again the normalized angle decreases rapidly。

---

# 15. Empirical Grassmannian exponents

A log-log fit over：

$$
\nu
=
10^{-5},
10^{-6},
10^{-7}
$$

gives：

### small fibre

$$
\boxed{
\theta_{\max}
\sim
\nu^{0.442\ldots}
}
\tag{15.1}
$$

### large fibre

$$
\boxed{
\theta_{\max}
\sim
\nu^{0.605\ldots}
}
\tag{15.2}
$$

These exponents are not claimed to be asymptotic invariants。

They show only that the first theorem target：

$$
O(\nu^{1/7})
$$

is extremely conservative。

---

# 16. Why faster numerical convergence is plausible

The conservative proof budget counts：

$$
j^{-2}
$$

far-neighbor terms as generic perturbations of the slow block。

But Round 59's endpoint Jost graph already contains these terms exactly。

After a true Schur elimination of the two fast parity modes，many nominal：

$$
O(j^{-2})
$$

effects are absorbed into the reference graph rather than appearing as external errors。

Thus the actual slow-graph mismatch can begin at a higher order than the naive：

$$
j^{-2}/(\nu j^2)
$$

budget。

This is the likely reason the observed principal angles decay much faster than：

$$
\nu^{1/7}.
$$

---

# 17. Fast Schur graph

Write the full transfer state as：

$$
\boxed{
Y_j
=
\begin{pmatrix}
Y_j^{\rm fast}
\\
Y_j^{\rm slow}
\end{pmatrix},
}
\tag{17.1}
$$

where：

$$
Y^{\rm fast}
$$

contains the two parity fast-minimal / growing coordinates，and：

$$
Y^{\rm slow}
$$

contains the coupled neutral pair。

Because the fast spectral separation is order one，seek invariant graphs：

$$
\boxed{
Y^{\rm fast}
=
\mathcal G_j^\pm
Y^{\rm slow}.
}
\tag{17.2}
$$

A graph-transform solve gives an effective slow transfer：

$$
\boxed{
Y_{j+1}^{\rm slow}
=
[
M(a_j)
+
\mathcal R_j(\nu)
]
Y_j^{\rm slow},
}
\tag{17.3}
$$

where：

$$
\mathcal R_j
$$

contains only Schur-renormalized corrections。

The key next estimate is to prove：

$$
\boxed{
\|
\mathcal R_j
\|
\ll
j^{-2}
}
\tag{17.4}
$$

after the endpoint reference geometry is absorbed。

If successful，the matching exponent can improve dramatically beyond：

$$
1/7.
$$

---

# 18. One-dimensional singular core

Once the two fast lines are reconstructed by：

$$
\mathcal G_j^\pm,
$$

the only vanishing-gap problem is the slow matrix：

$$
M(a_j)+\mathcal R_j.
$$

Its stable dimension is one。

Therefore the singular matching core can be represented by a scalar projective coordinate：

$$
\boxed{
z_j
=
\frac{
E_j
}{
o_j
}
}
\tag{18.1}
$$

or an equivalent Riccati variable。

For the reduced matrix：

$$
M(a),
$$

the stable projective fixed point is explicitly determined by：

$$
\lambda_-(a).
$$

Thus the next round can aim at a scalar nonautonomous Riccati enclosure rather than a full three-plane determinant。

命名：

$$
\boxed{
\textbf{Fast-Schur / Slow-Riccati Reduction}.
}
$$

---

# 19. STOP-C65 — Fast-Schur / Slow-Riccati Quantitative Gap

$$
\boxed{
\begin{aligned}
\text{layer}
&=
\mathrm{small\text{-}viscosity\ stable\text{-}bundle\ matching},
\\
\text{endpoint parity cubic}
&=
\mathrm{neutral}
+
\mathrm{fast\ reciprocal\ pair},
\\
\text{positive-viscosity minimal plane}
&=
2\text{ fast minimal lines}
+
1\text{ slow stable line},
\\
\text{preferred overlap}
&=
j_m=\nu^{-2/7},
\\
\text{conservative attenuation error}
&=
\nu^{1/7},
\\
\text{conservative gap/roughness error}
&=
\nu^{1/7},
\\
\text{algebraic endpoint error}
&=
\nu^{2/7}
\text{ or better},
\\
\text{first theorem candidate}
&=
\operatorname{dist}
(
E_\nu^{\min},
E_0^{\rm Jost}
)
=
O(\nu^{1/7}),
\\
\text{full principal-angle diagnostics}
&=
\mathrm{much\ faster\ than\ }\nu^{1/7},
\\
\text{remaining task}
&=
\mathrm{construct\ uniform\ fast\ Schur\ graphs}
\\
&\quad+
\mathrm{bound\ the\ effective\ slow\ Riccati\ remainder},
\\
\text{small-viscosity positivity}
&=
\mathrm{not\ yet\ rigorously\ extended\ to\ }\nu>0,
\\
T_{\mathsf C\to\mathsf D}
&=
\mathrm{NOT\ REACHED}.
\end{aligned}
}
$$

命名：

$$
\boxed{
\textbf{STOP-C65:
Fast-Schur / Slow-Riccati Quantitative Gap}.
}
$$

---

# 20. 24/72 Ledger — Round 61

| Step | object | $B$ | $U$ | $O$ | $L$ | status |
|---|---|---|---|---|---|---|
| C975 | zero-viscosity parity cubic | $\mathsf C$ | frozen Floquet transfer | scalar | $\mathsf F$ | DERIVED |
| C976 | exact neutral/fast factorization | $\mathsf C$ | local spectrum | scalar | $\mathsf F$ | EXACT leading |
| C977 | fast reciprocal roots | $\mathsf C$ | asymptotic spectrum | scalar | $\mathsf F$ | DERIVED |
| C978 | endpoint selected three-plane | $\mathsf C$ | Jost geometry | relational | $\mathsf F$ | IDENTIFIED |
| C979 | positive-viscosity fast–slow split | $\mathsf C$ | stable bundle | relational | $\mathsf F$ | IDENTIFIED asymptotically |
| C980 | proof-burden dimension reduction | $\mathsf C$ | Schur geometry | targeted | $\mathsf F$ | ROUTE DESIGNED |
| C981 | general overlap exponent | $\mathsf C$ | matched asymptotics | scalar | $\mathsf F$ | DERIVED |
| C982 | three conservative errors | $\mathsf C$ | roughness budget | scalar | $\mathsf F$ | DERIVED |
| C983 | optimal $\alpha=2/7$ | $\mathsf C$ | exponent optimization | scalar | $\mathsf F$ | PROVED within budget model |
| C984 | corrected $O(\nu^{1/7})$ target | $\mathsf C$ | matching theorem | targeted | $\mathsf F$ | THEOREM TARGET |
| C985 | 6D physical stable-plane diagnostic | $\mathsf C$ | Grassmannian transfer | profile | $\mathsf F$ | NUMERICALLY VERIFIED |
| C986 | small-fibre principal-angle collapse | $\mathsf C$ | parameter scaling | scalar | $\mathsf F$ | VERIFIED |
| C987 | large-fibre principal-angle collapse | $\mathsf C$ | parameter scaling | scalar | $\mathsf F$ | VERIFIED |
| C988 | fast Schur graph | $\mathsf C$ | invariant graph | relational | $\mathsf F$ | ROUTE DESIGNED |
| C989 | slow scalar Riccati reduction | $\mathsf C$ | projective dynamics | scalar | $\mathsf F$ | ROUTE DESIGNED |
| C990 | rigorous small-$\nu$ positivity interval | $\mathsf C$ | singular continuation | targeted | $\mathsf F$ | OPEN / STOP-C65 |

---

# 21. Continuous-versus-discrete status

The three-plane is the spectral admissible subspace of a continuous periodic Floquet operator。

The parity recurrence and principal angles are coordinate representations of that continuous operator family。

The exponent：

$$
2/7
$$

comes from balancing continuous singular-asymptotic scales：

- cumulative viscosity；
- spectral gap；
- operator-tail geometry。

No finite combinatorial proof mechanism is used。

Therefore：

$$
\boxed{
T_{\mathsf C\to\mathsf D}
=
\text{NOT YET REACHED}.
}
$$

---

# 22. Strongest results of Round 61

## R61-A — exact leading parity factorization

$$
\boxed{
\epsilon+r-r^2-\epsilon r^3
=
-(r-1)
[
\epsilon r^2+(1+\epsilon)r+\epsilon
].
}
$$

## R61-B — two fast lines plus one slow line

$$
\boxed{
E_\nu^{\min}
=
E_{\rm fast,e}^{\min}
\oplus
E_{\rm fast,o}^{\min}
\oplus
E_{\rm slow}^{-}.
}
$$

## R61-C — direct roughness overlap window

$$
\boxed{
1/4<\alpha<1/3.
}
$$

## R61-D — optimal conservative overlap

$$
\boxed{
\alpha_\ast=2/7,
\qquad
j_m=\nu^{-2/7}.
}
$$

## R61-E — first self-consistent matching exponent

$$
\boxed{
\operatorname{dist}
(
E_\nu^{\min},
E_0^{\rm Jost}
)
=
O(\nu^{1/7})
}
$$

is the corrected coarse theorem target。

## R61-F — full Grassmannian data are substantially better

At：

$$
\nu=10^{-7},
$$

$$
\boxed{
\theta_{\max,-}
\approx
7.27\times10^{-3},
}
$$

$$
\boxed{
\theta_{\max,+}
\approx
2.14\times10^{-3}.
}
$$

---

# 23. Next round — Fast Schur Graph / Slow Riccati Enclosure

Round 61 has reduced the singular three-plane problem to：

$$
\boxed{
2
\text{ uniformly fast lines}
+
1
\text{ singular slow line}.
}
$$

The next attack should exploit that reduction directly。

Concrete targets：

1. construct exact local parity fast eigenvectors to one additional order in：
   $$
   j^{-2};
   $$

2. build invariant fast Schur graphs over the slow pair；

3. prove a uniform graph-transform contraction for：
   $$
   j\ge j_m;
   $$

4. derive the corrected slow transfer：
   $$
   M(a_j)+\mathcal R_j;
   $$

5. prove an explicit bound：
   $$
   \|\mathcal R_j\|
   \le
   C
   j^{-p}
   $$
   with the largest available：
   $$
   p>2;
   $$

6. convert the slow stable line to a scalar Riccati equation；

7. compare that Riccati solution with the exact reduced stable root：
   $$
   \lambda_-(a_j);
   $$

8. propagate the slow-line enclosure to the Round 59 endpoint Jost graph；

9. extract an explicit：
   $$
   \left|
   a_3(\nu)/\nu-c_0
   \right|
   \le
   C_\ast\nu^\gamma;
   $$

10. choose a concrete：
    $$
    \nu_s>0
    $$
    for which Round 59's positive margins imply：
    $$
    a_3(\nu)>0
    \quad
    (0<\nu\le\nu_s).
    $$

This becomes：

$$
\boxed{
\textbf{Fast Schur Graph / Slow Riccati Enclosure}.
}
$$

---

# 24. External primary-source anchors

1. F. Battelli, M. Franca, K. J. Palmer, *Exponential Dichotomy for Noninvertible Linear Difference Equations*, arXiv:2111.04553.
   - proves roughness results for exponential dichotomies of linear difference equations；
   - relevant to the planned graph-transform control after the fast–slow split。

2. Evans M. Harrell II, Manwah Lilian Wong, *On the behavior at infinity of solutions to difference equations in Schroedinger form*, arXiv:1109.4691.
   - develops perturbative comparison of difference-equation solutions and a discrete Liouville–Green/WKB transformation；
   - relevant to controlling asymptotic solution spaces under small coefficient errors。

3. Yuri Latushkin, Shibi Vasudevan, *Fredholm determinants, continued fractions, Jost and Evans functions for a Jacobi matrix associated with the 2D-Euler equations*, arXiv:2401.14037.
   - relates hydrodynamic difference-equation Jost, Evans, Fredholm and continued-fraction representations；
   - relevant to the endpoint Jost-plane and projective/Riccati formulation。

All NS-specific factorization formulas，matching exponents and Grassmannian data in this round are direct derivations / computations of this project。

---

# 25. Commit state

$$
\boxed{
\begin{aligned}
\text{Route}
&=
\mathrm{Pure\ Continuous\ Fast\text{–}Slow\ Stable\text{-}Bundle\ Matching},
\\
\text{Essential }\mathsf C\to\mathsf D
&=
\mathrm{Not\ reached},
\\
\text{Round 60 WKB layer}
&=
\nu^{-1/3},
\\
\text{Round 60 direct overlap}
&=
\mathrm{corrected},
\\
\text{Preferred roughness overlap}
&=
\nu^{-2/7},
\\
\text{First rigorous error exponent target}
&=
1/7,
\\
\text{Three-plane singular core}
&\to
\text{one slow projective line after fast Schur elimination},
\\
\text{Numerical Grassmann convergence}
&=
\mathrm{stronger\ than\ coarse\ target},
\\
\text{STOP-C65}
&=
\mathrm{Fast\text{-}Schur/Slow\text{-}Riccati\ Quantitative\ Gap},
\\
\text{Next}
&=
\mathrm{Fast\ Schur\ Graph/Slow\ Riccati\ Enclosure}.
\end{aligned}
}
$$
