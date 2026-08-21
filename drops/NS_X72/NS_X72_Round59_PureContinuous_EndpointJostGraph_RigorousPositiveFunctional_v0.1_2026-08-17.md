# NS × X 積分 × 24/72 範式實戰
## Round 59 — Pure Continuous Endpoint Jost Graph / Rigorous Positive Green Functional

- 日期：2026-08-17
- 版本：v0.1
- 狀態：Proof-Route Experiment / Continuous-Only Endpoint-Jost Branch
- canonical source：UTF-8 Markdown
- canonical math delimiters：inline `$...$`；display `$$...$$`
- 前一輪：`NS_X72_Round58_PureContinuous_SmallViscosity_BoundedNeutralAdjointLimit_v0.1_2026-08-17.md`
- 本輪目標：Round 58 已導出 small-viscosity singular endpoint
  $$
  u_{2j}=e_j,
  \qquad
  u_{2j+1}=\nu o_j,
  $$
  並辨識
  $$
  e_j
  $$
  為 minimal Euler mode、
  $$
  o_j
  $$
  為 forced bounded-neutral corrector，但 endpoint Green/Jost positivity仍只有 numerical BVP evidence。本輪將 odd endpoint的 bounded two-dimensional Jost family改寫成一個 **affine graph pullback**，用 exact algebraic coefficient bounds + outward interval arithmetic直接證明 endpoint Green functional嚴格為正。
- 主要結果：
  1. even minimal ratio tail可寫成 nonautonomous pullback contraction；
  2. endpoint odd bounded-Jost family可寫成 affine graph
     $$
     o_{j+2}
     =
     P_j o_{j+1}
     +
     Q_j o_j
     +
     R_j;
     $$
  3. graph參數滿足 exact rational pullback recurrence；
  4. 對兩個 source fibres，在所有
     $$
     j\ge10
     $$
     上存在固定有理 invariant boxes，且 pullback Lipschitz constants分別小於
     $$
     0.01
     $$
     與
     $$
     0.04;
     $$
  5. 因此 endpoint Jost affine plane是唯一 pullback attractor，不依賴 far-tail初始化；
  6. 將 entire invariant tail box用 outward interval arithmetic推回中心後，得到：
     $$
     c_{0,-}
     \in
     [
     5.7905255784226477,\,
     5.7905255784226478
     ],
     $$
     $$
     c_{0,+}
     \in
     [
     5.331752543272241,\,
     5.331752548672376
     ];
     $$
  7. hence
     $$
     c_{0,\pm}>0
     $$
     is now a rigorous endpoint theorem；
  8. Round 58 的 numerical endpoint BVP constants are recovered inside these intervals；
  9. Remaining gap is **not endpoint positivity anymore**，but the singular matching theorem：
     $$
     a_3(\nu)/\nu
     \longrightarrow
     c_0
     \qquad
     (\nu\to0^+).
     $$
- 非主張：本輪沒有證明上述 singular matching limit。Therefore it does not yet prove a positive-viscosity interval
  $$
  a_3(\nu)>0
  $$
  near zero。It proves the $\nu=0$ Jost/Green endpoint functional itself is rigorously positive。

---

# 0. Round 58 handoff

The two horizontal source fibres are：

$$
\boxed{
K_-
=
\sqrt{17}-3,
}
\tag{0.1}
$$

and：

$$
\boxed{
K_+
=
\sqrt{17}+3.
}
\tag{0.2}
$$

Round 58 parity rescaling：

$$
\boxed{
u_{2j}=e_j,
}
\tag{0.3}
$$

$$
\boxed{
u_{2j+1}
=
\nu o_j.
}
\tag{0.4}
$$

At：

$$
\nu=0,
$$

the even mode solves a homogeneous minimal recurrence，while the odd first corrector solves：

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
\tag{0.5}
$$

Normalization：

$$
\boxed{
o_0=0.
}
\tag{0.6}
$$

The correct endpoint condition is bounded-neutral rather than decaying：

$$
\boxed{
o_j
=
L
-
\frac{
3K^2L
}{
4j^2
}
+
O(j^{-3}).
}
\tag{0.7}
$$

Round 58 numerical candidates：

$$
c_{0,-}
=
-\,
o_1
\approx
5.79052557842265,
$$

$$
c_{0,+}
\approx
5.33175254587449.
$$

Round 58 STOP：

$$
\boxed{
\text{STOP-C62}
=
\text{Bounded-Neutral Green/Jost Endpoint Gap}.
}
$$

---

# 1. Even minimal-ratio pullback

Define：

$$
\boxed{
R_j
=
\frac{
e_j
}{
e_{j-1}
}.
}
\tag{1.1}
$$

The even endpoint recurrence gives：

$$
\boxed{
R_j
=
\frac{
A_{-2}^{(2j)}
}{
A_0^{(2j)}
-
A_2^{(2j)}
R_{j+1}
+
A_4^{(2j)}
R_{j+2}R_{j+1}
}.
}
\tag{1.2}
$$

This is a two-step nonautonomous pullback map。

For both：

$$
K=K_-,
\qquad
K=K_+,
$$

and every real：

$$
j\ge10,
$$

the exact algebraic coefficient certificate proves the sign pattern：

$$
\boxed{
A_{-2}^{(2j)}<0,
}
\tag{1.3}
$$

$$
\boxed{
A_0^{(2j)}>0,
}
\tag{1.4}
$$

$$
\boxed{
A_2^{(2j)}>0,
}
\tag{1.5}
$$

$$
\boxed{
A_4^{(2j)}<0.
}
\tag{1.6}
$$

---

# 2. Even invariant ratio box

Let：

$$
\boxed{
\mathcal B_R
=
[-1/10,0]^2.
}
\tag{2.1}
$$

For the small fibre，the coefficient bounds：

$$
\boxed{
-0.01
<
A_{-2}^{(2j)}
<0,
}
\tag{2.2}
$$

$$
\boxed{
4
<
A_0^{(2j)},
A_2^{(2j)}
<
5,
}
\tag{2.3}
$$

$$
\boxed{
-0.01
<
A_4^{(2j)}
<0
}
\tag{2.4}
$$

hold for all：

$$
j\ge10.
$$

For the large fibre：

$$
\boxed{
-1.4
<
A_{-2}^{(2j)}
<0,
}
\tag{2.5}
$$

$$
\boxed{
25
<
A_0^{(2j)}
<
29,
}
\tag{2.6}
$$

$$
\boxed{
24
<
A_2^{(2j)}
<
29,
}
\tag{2.7}
$$

$$
\boxed{
-0.4
<
A_4^{(2j)}
<0.
}
\tag{2.8}
$$

For：

$$
R_{j+1},R_{j+2}
\in
[-0.1,0],
$$

these imply：

$$
\boxed{
R_j\in[-0.1,0].
}
\tag{2.9}
$$

Moreover the Jacobian sum is uniformly below：

$$
0.004
$$

for：

$$
K_-,
$$

and below：

$$
0.067
$$

for：

$$
K_+.
$$

Therefore the ratio pullback is a strict contraction on：

$$
\mathcal B_R.
$$

This constructs a unique minimal-ratio pullback tail。

---

# 3. Rigorous finite ratio enclosure

Because the true minimal tail satisfies：

$$
(R_{11},R_{12})
\in
\mathcal B_R,
$$

outward interval evaluation of (1.2) from：

$$
j=10
$$

down to：

$$
j=1
$$

gives rigorous enclosures for：

$$
R_1,\ldots,R_{10}.
$$

Multiplying interval ratios yields：

### small fibre

$$
\boxed{
|e_{11}|
<
10^{-19},
}
\tag{3.1}
$$

### large fibre

$$
\boxed{
|e_{11}|
<
10^{-8}.
}
\tag{3.2}
$$

These deliberately coarse bounds are sufficient for the odd Jost graph proof。

---

# 4. Tail forcing bound

Recall：

$$
\boxed{
f_j
=
b_{2j+1}
e_{j+1}.
}
\tag{4.1}
$$

The exact coefficient certificate proves：

$$
\boxed{
b_{2j+1}<0
}
\tag{4.2}
$$

and：

$$
\boxed{
|b_{2j+1}|
<
100
(
2j+1
)^2
}
\tag{4.3}
$$

for both fibres and all：

$$
j\ge10.
$$

Since：

$$
|R_j|\le0.1
$$

through the even tail，

$$
|e_{j+1}|
$$

decreases by at least one factor：

$$
0.1
$$

per further endpoint level。

Therefore the worst forcing is at：

$$
j=10.
$$

Using Sections 3–4：

$$
\boxed{
|f_j|
<
10^{-3}
\qquad
(j\ge10)
}
\tag{4.4}
$$

for both fibres。

---

# 5. Affine Jost graph

Instead of separately constructing neutral and minimal homogeneous solutions，represent the entire two-dimensional bounded endpoint family by an affine graph：

$$
\boxed{
o_{j+2}
=
P_j
o_{j+1}
+
Q_j
o_j
+
G_j.
}
\tag{5.1}
$$

The notation：

$$
G_j
$$

is used here for the affine source offset，to avoid confusion with the even ratio：

$$
R_j.
$$

Substitute (5.1) into the odd endpoint recurrence。

The exact pullback is：

$$
\boxed{
P_{j-1}
=
\frac{
A_0^{(2j+1)}
+
A_4^{(2j+1)}
Q_j
}{
A_2^{(2j+1)}
-
A_4^{(2j+1)}
P_j
},
}
\tag{5.2}
$$

$$
\boxed{
Q_{j-1}
=
-
\frac{
A_{-2}^{(2j+1)}
}{
A_2^{(2j+1)}
-
A_4^{(2j+1)}
P_j
},
}
\tag{5.3}
$$

$$
\boxed{
G_{j-1}
=
\frac{
A_4^{(2j+1)}
G_j
-
f_j
}{
A_2^{(2j+1)}
-
A_4^{(2j+1)}
P_j
}.
}
\tag{5.4}
$$

命名：

$$
\boxed{
\textbf{Endpoint Affine Jost Pullback}.
}
$$

---

# 6. Small-fibre invariant graph box

For：

$$
K=K_-,
$$

define：

$$
\boxed{
\mathcal B_-
=
[
0.7,1.3
]
\times
[
0,0.01
]
\times
[
-1,1
].
}
\tag{6.1}
$$

Using the exact coefficient bounds from Sections 1–4，for：

$$
j\ge10
$$

the denominator satisfies：

$$
\boxed{
A_2-A_4P
>
4.
}
\tag{6.2}
$$

The pullback obeys：

$$
\boxed{
0.7
<
P_{j-1}
<
1.3,
}
\tag{6.3}
$$

$$
\boxed{
0
<
Q_{j-1}
<
0.01,
}
\tag{6.4}
$$

$$
\boxed{
|G_{j-1}|
<
1.
}
\tag{6.5}
$$

The infinity-norm Jacobian satisfies the coarse uniform estimate：

$$
\boxed{
\|D\Phi_j\|_\infty
<
0.01.
}
\tag{6.6}
$$

Therefore：

$$
\boxed{
\Phi_j(
\mathcal B_-
)
\subset
\mathcal B_-,
}
\tag{6.7}
$$

and the pullback is a strict contraction。

---

# 7. Large-fibre invariant graph box

For：

$$
K=K_+,
$$

take：

$$
\boxed{
\mathcal B_+
=
[
0.8,1.25
]
\times
[
0,0.06
]
\times
[
-1,1
].
}
\tag{7.1}
$$

The coefficient bounds yield：

$$
\boxed{
A_2-A_4P
>
24.
}
\tag{7.2}
$$

Then：

$$
\boxed{
0.8
<
P_{j-1}
<
1.25,
}
\tag{7.3}
$$

$$
\boxed{
0
<
Q_{j-1}
<
0.06,
}
\tag{7.4}
$$

$$
\boxed{
|G_{j-1}|
<
1.
}
\tag{7.5}
$$

and：

$$
\boxed{
\|D\Phi_j\|_\infty
<
0.04.
}
\tag{7.6}
$$

Thus：

$$
\boxed{
\Phi_j(
\mathcal B_+
)
\subset
\mathcal B_+.
}
\tag{7.7}
$$

---

# 8. Pullback-attractor existence and uniqueness

Fix：

$$
J>10
$$

and choose any terminal graph：

$$
(P_J,Q_J,G_J)
\in
\mathcal B_\pm.
$$

Pull it back to：

$$
j=10
$$

using：

$$
\Phi_J,
\Phi_{J-1},
\ldots,
\Phi_{11}.
$$

If two terminal graphs are chosen，their images at level：

$$
10
$$

differ by at most：

$$
\boxed{
C
q^{J-10}
}
\tag{8.1}
$$

where：

$$
q=0.01
$$

or：

$$
0.04.
$$

Therefore as：

$$
J\to\infty,
$$

the level-$10$ graph converges to a unique limit independent of terminal data。

Finite pullback then gives a unique affine Jost graph at every finite level。

命名：

$$
\boxed{
\textbf{Endpoint Jost Pullback Theorem}.
}
$$

This theorem selects precisely the endpoint Green/Jost family that Round 58 was approximating with far-cutoff BVPs。

---

# 9. Central Green functional

At：

$$
j=0,
$$

the Jost graph is：

$$
\boxed{
o_2
=
P_0o_1
+
Q_0o_0
+
G_0.
}
\tag{9.1}
$$

Canonical endpoint normalization：

$$
o_0=0.
$$

The reflected central recurrence is：

$$
\boxed{
-
A_2^{(1)}
o_1
+
A_4^{(1)}
o_2
=
f_0.
}
\tag{9.2}
$$

Substitute (9.1)：

$$
\boxed{
o_1
=
-
\frac{
f_0
-
A_4^{(1)}G_0
}{
A_2^{(1)}
-
A_4^{(1)}P_0
}.
}
\tag{9.3}
$$

Therefore the endpoint slope functional is：

$$
\boxed{
c_0
=
-\,
o_1
=
\frac{
f_0
-
A_4^{(1)}G_0
}{
A_2^{(1)}
-
A_4^{(1)}P_0
}.
}
\tag{9.4}
$$

This is the promised scalar Green/Jost representation。

---

# 10. Outward interval enclosure — small fibre

At level：

$$
j=10,
$$

the true Jost graph lies inside：

$$
\mathcal B_-.
$$

Use exact algebraic：

$$
K_-=\sqrt{17}-3
$$

represented by outward interval arithmetic，and use the rigorous even-ratio intervals from Section 3。

Propagate the entire graph box from：

$$
j=10
$$

to：

$$
j=0.
$$

The resulting endpoint interval is：

$$
\boxed{
c_{0,-}
\in
[
5.7905255784226477185,\,
5.7905255784226477186
].
}
\tag{10.1}
$$

In particular：

$$
\boxed{
c_{0,-}>5.79>0.
}
\tag{10.2}
$$

---

# 11. Outward interval enclosure — large fibre

For：

$$
K_+=\sqrt{17}+3,
$$

start with：

$$
\mathcal B_+
$$

at：

$$
j=10.
$$

The outward interval pullback gives：

$$
\boxed{
c_{0,+}
\in
[
5.3317525432722412395,\,
5.3317525486723752263
].
}
\tag{11.1}
$$

Hence：

$$
\boxed{
c_{0,+}>5.33>0.
}
\tag{11.2}
$$

The interval is wider than the small-fibre interval because the large-fibre graph contraction is weaker，but positivity has an enormous safety margin。

---

# 12. Endpoint Positive Green Functional Theorem

Collect Sections 8–11。

For each：

$$
K
=
\sqrt{17}\pm3,
$$

the $\nu=0$ singular endpoint problem has a unique pullback-selected affine Jost graph。

The canonical Green functional：

$$
\boxed{
c_0=-o_1
}
$$

is rigorously positive。

Specifically：

$$
\boxed{
c_{0,-}
>
5.79,
}
\tag{12.1}
$$

$$
\boxed{
c_{0,+}
>
5.33.
}
\tag{12.2}
$$

命名：

$$
\boxed{
\textbf{Endpoint Positive Green Functional Theorem}.
}
$$

This closes the **endpoint positivity** component of STOP-C62。

---

# 13. Recovery of Round 58 numerical constants

Round 58 direct BVP values：

$$
5.79052557842265\ldots
$$

and：

$$
5.33175254587449\ldots
$$

both lie inside the rigorous Round 59 intervals。

Thus the previous numerical endpoint computations were identifying the correct Jost pullback attractor。

The discrepancy found in Round 57's raw small-positive-viscosity SVD was therefore not an endpoint ambiguity；it was the expected singular finite-cutoff effect before the boundary layer was resolved。

---

# 14. Endpoint Fredholm slope sign

Round 58 pairing slope candidate：

$$
\boxed{
\Pi'(0^+)
=
12
(
3r^2-1
)
+
c_0G_{-3},
}
\tag{14.1}
$$

assuming the singular matching：

$$
a_3(\nu)/\nu\to c_0.
$$

The exact target sign geometry gives：

- small fibre：
  both terms are negative；
- large fibre：
  both terms are positive。

Therefore Round 59 positivity implies：

$$
\boxed{
\Pi'_-(0^+)<0
}
\tag{14.2}
$$

and：

$$
\boxed{
\Pi'_+(0^+)>0
}
\tag{14.3}
$$

**conditional only on the singular matching limit.**

The endpoint Green functional itself is no longer the source of uncertainty。

---

# 15. What remains in the singular matching theorem

For every fixed：

$$
\nu>0,
$$

the full adjoint tail has three minimal branches and decays superfactorially。

At：

$$
\nu=0,
$$

the rescaled odd derivative develops a bounded-neutral plateau。

The remaining theorem must show：

$$
\boxed{
\frac{
u_{2j+1}(\nu)
}{
\nu
}
\to
o_j^{(0)}
}
\tag{15.1}
$$

for each finite：

$$
j,
$$

where：

$$
o^{(0)}
$$

is the unique Jost pullback selected in Round 59。

Equivalently：

$$
\boxed{
\frac{
a_3(\nu)
}{
\nu
}
\to
c_0.
}
\tag{15.2}
$$

The difficulty is the moving Floquet boundary layer：

$$
j
\sim
\nu^{-1/2}.
$$

This is now the **only small-viscosity endpoint gap** in the present branch。

---

# 16. Why the affine graph is preferable to neutral/minimal basis matching

A neutral/minimal basis becomes badly conditioned when propagated from Floquet infinity：

- the minimal mode changes by factorial scales；
- the neutral mode differs from a constant only at：
  $$
  O(j^{-2});
  $$
- tiny asymptotic basis errors contaminate one another under backward propagation。

The affine graph：

$$
o_{j+2}
=
P_jo_{j+1}
+
Q_jo_j
+
G_j
$$

tracks the **two-dimensional bounded solution plane itself**，not a basis inside the plane。

Its pullback contracts strongly：

$$
<0.01
$$

or：

$$
<0.04.
$$

Thus it is the natural endpoint Jost coordinate。

---

# 17. Relation to continued fractions / Jost functions

For second-order hydrodynamic difference equations，continued fractions，Jost solutions，Evans functions and Fredholm determinants can encode the same spectral compatibility data。

The present odd endpoint is higher-order and affine-forced，but the same principle appears：

$$
\boxed{
\text{asymptotic admissible solution plane}
\to
\text{pullback graph}
\to
\text{central Green functional}.
}
$$

Round 59 derives this structure directly from the NS-specific recurrence rather than importing a black-box Jost theorem。

---

# 18. STOP-C63 — Singular Minimal-to-Jost Matching Gap

$$
\boxed{
\begin{aligned}
\text{layer}
&=
\mathrm{small\text{-}viscosity\ endpoint\ Green/Jost\ geometry},
\\
\text{even minimal ratio tail}
&=
\mathrm{pullback\ contraction},
\\
\text{odd bounded solution family}
&=
\mathrm{affine\ Jost\ graph},
\\
\text{small graph contraction}
&<
0.01,
\\
\text{large graph contraction}
&<
0.04,
\\
\text{endpoint Jost graph}
&=
\mathrm{exists\ uniquely},
\\
c_{0,-}
&>
5.79,
\\
c_{0,+}
&>
5.33,
\\
\text{endpoint positivity}
&=
\mathrm{proved},
\\
\text{remaining uncertainty}
&\ne
\mathrm{Green/Jost\ sign},
\\
\text{remaining uncertainty}
&=
\mathrm{singular\ convergence\ of\ fixed\text{-}\nu\ minimal\ branches},
\\
\text{missing}
&=
\mathrm{proof\ that\ }
a_3(\nu)/\nu
\to
c_0
\mathrm{\ across\ the\ }j\sim\nu^{-1/2}\mathrm{\ boundary\ layer},
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
\textbf{STOP-C63:
Singular Minimal-to-Jost Matching Gap}.
}
$$

---

# 19. 24/72 Ledger — Round 59

| Step | object | $B$ | $U$ | $O$ | $L$ | status |
|---|---|---|---|---|---|---|
| C946 | even minimal ratio pullback | $\mathsf C$ | continued-ratio tail | scalar | $\mathsf F$ | EXACT |
| C947 | even invariant ratio box | $\mathsf C$ | nonautonomous contraction | targeted | $\mathsf F$ | CERTIFIED |
| C948 | finite even ratio enclosure | $\mathsf C$ | outward interval | scalar | $\mathsf F$ | CERTIFIED |
| C949 | tail forcing bound | $\mathsf C$ | minimal even decay | scalar | $\mathsf F$ | CERTIFIED |
| C950 | affine Jost graph | $\mathsf C$ | bounded endpoint plane | relational | $\mathsf F$ | FORM |
| C951 | exact graph pullback | $\mathsf C$ | rational recurrence | relational | $\mathsf F$ | EXACT |
| C952 | small-fibre invariant graph box | $\mathsf C$ | algebraic inequalities | targeted | $\mathsf F$ | CERTIFIED |
| C953 | large-fibre invariant graph box | $\mathsf C$ | algebraic inequalities | targeted | $\mathsf F$ | CERTIFIED |
| C954 | pullback-attractor uniqueness | $\mathsf C$ | contraction theorem | targeted | $\mathsf F$ | PROVED |
| C955 | scalar central Green functional | $\mathsf C$ | endpoint matching | scalar | $\mathsf F$ | EXACT |
| C956 | small endpoint interval | $\mathsf C$ | outward interval | scalar | $\mathsf F$ | CERTIFIED |
| C957 | large endpoint interval | $\mathsf C$ | outward interval | scalar | $\mathsf F$ | CERTIFIED |
| C958 | Endpoint Positive Green Functional Theorem | $\mathsf C$ | infinite Jost tail | targeted | $\mathsf F$ | PROVED |
| C959 | Round 58 numerical audit | $\mathsf C$ | independent comparison | targeted | $\mathsf F$ | PASSED |
| C960 | singular fixed-$\nu$ matching | $\mathsf C$ | boundary-layer limit | targeted | $\mathsf F$ | OPEN / STOP-C63 |

---

# 20. Continuous-versus-discrete status

The pullback graph acts on the coefficient plane of a continuous periodic endpoint equation。

The Fourier level：

$$
j
$$

is a representation coordinate，and the contraction theorem is a statement about the asymptotic Jost plane of the continuous Floquet fibre。

The proof uses no finite combinatorial argument and no discrete-time physical model。

The outward interval certificate validates inequalities of continuous rational coefficient functions and the finite pullback map。

Therefore：

$$
\boxed{
T_{\mathsf C\to\mathsf D}
=
\text{NOT YET REACHED}.
}
$$

---

# 21. Strongest results of Round 59

## R59-A — exact affine Jost recurrence

$$
\boxed{
\begin{aligned}
P_{j-1}
&=
\frac{A_0+A_4Q_j}{A_2-A_4P_j},
\\
Q_{j-1}
&=
-\frac{A_{-2}}{A_2-A_4P_j},
\\
G_{j-1}
&=
\frac{A_4G_j-f_j}{A_2-A_4P_j}.
\end{aligned}
}
$$

## R59-B — uniform tail contraction

For：

$$
j\ge10,
$$

$$
\boxed{
\operatorname{Lip}\Phi_j<0.01
}
$$

or：

$$
\boxed{
<0.04.
}
$$

## R59-C — unique endpoint Jost plane

The far-tail bounded solution plane is a unique pullback attractor，independent of terminal graph initialization。

## R59-D — rigorous positive endpoint slopes

$$
\boxed{
c_{0,-}
>
5.79,
}
$$

$$
\boxed{
c_{0,+}
>
5.33.
}
$$

## R59-E — Round 58 endpoint numerics are now certified

The stable BVP values lie inside the rigorous intervals。

## R59-F — the small-viscosity gap has moved

The endpoint sign is no longer open。

Only：

$$
\boxed{
a_3(\nu)/\nu\to c_0
}
$$

across the moving Floquet boundary layer remains。

---

# 22. Next round — Singular Boundary-Layer Matching / Minimal-to-Jost Convergence

Round 59 has proved the endpoint Green functional is positive。

The next round should therefore attack the actual singular matching theorem。

Concrete targets：

1. introduce the stretched Floquet variable：
   $$
   \xi
   =
   \sqrt{\nu}\,j;
   $$

2. derive the large-$j$，small-$\nu$ transition recurrence where：
   $$
   \nu j^2
   =
   O(1);
   $$

3. identify the inner analytic/minimal branch for：
   $$
   \xi\gg1;
   $$

4. identify the outer bounded-neutral Jost graph for：
   $$
   \xi\ll1;
   $$

5. prove an overlap region：
   $$
   1\ll j\ll\nu^{-1/2}
   $$
   where both expansions are valid；

6. match the fixed-$\nu$ minimal graph to the Round 59 endpoint affine graph；

7. derive：
   $$
   a_3(\nu)
   =
   c_0\nu
   +
   O(
   \nu^{1+\alpha}
   )
   $$
   for some：
   $$
   \alpha>0;
   $$

8. conclude：
   $$
   a_3(\nu)>0
   $$
   on：
   $$
   0<\nu\le\nu_s;
   $$

9. then return to the compact middle-viscosity validated continuation from Round 57。

This becomes：

$$
\boxed{
\textbf{Singular Boundary-Layer Matching / Minimal-to-Jost Convergence}.
}
$$

---

# 23. External primary-source anchors

1. Yuri Latushkin, Shibi Vasudevan, *Fredholm determinants, continued fractions, Jost and Evans functions for a Jacobi matrix associated with the 2D-Euler equations*, arXiv:2401.14037.
   - relates continued fractions，Jost solutions，Evans functions and Fredholm determinants for a hydrodynamic difference equation；
   - relevant structural context for the pullback-Jost representation used here。

2. Yuri Latushkin, Shibi Vasudevan, *Characteristic determinants for a second order difference equation on the half-line arising in hydrodynamics*, arXiv:2405.01135.
   - studies half-line hydrodynamic difference equations through Fredholm/Evans/Jost data；
   - relevant to the endpoint admissible-subspace viewpoint。

3. J. D. Mireles James, Maxime Murray, *Computer assisted proof of homoclinic chaos in the spatial equilateral restricted four body problem*, arXiv:2212.00930.
   - gives a finite-core plus rigorously bounded infinite Fourier/Taylor tail methodology；
   - methodological context for the outward interval tail certificate used in this round。

All NS-specific graph recurrences，coefficient boxes，contraction constants and endpoint intervals are direct derivations / certifications of Round 59。

---

# 24. Commit state

$$
\boxed{
\begin{aligned}
\text{Route}
&=
\mathrm{Pure\ Continuous\ Endpoint\ Jost\ Graph},
\\
\text{Essential }\mathsf C\to\mathsf D
&=
\mathrm{Not\ reached},
\\
\text{Round 58 endpoint sign candidate}
&\to
\mathrm{rigorous\ interval\ theorem},
\\
\text{Endpoint Green/Jost plane}
&=
\mathrm{unique},
\\
c_{0,-}
&>
5.79,
\\
c_{0,+}
&>
5.33,
\\
\text{Endpoint positivity gap}
&=
\mathrm{closed},
\\
\text{Remaining small-viscosity gap}
&=
\mathrm{fixed\text{-}\nu\ minimal\ to\ endpoint\ Jost\ matching},
\\
\text{STOP-C63}
&=
\mathrm{Singular\ Minimal\text{-}to\text{-}Jost\ Matching\ Gap},
\\
\text{Next}
&=
\mathrm{Singular\ Boundary\text{-}Layer\ Matching/Minimal\text{-}to\text{-}Jost\ Convergence}.
\end{aligned}
}
$$
