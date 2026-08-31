# NS × X 積分 × 24/72 範式實戰
## Round 71 — Pure Continuous Secant Riccati Volterra / Direct $O(\nu)$ Jost Bridge

- 日期：2026-08-18
- 版本：v0.1
- 狀態：Proof-Route Experiment / Continuous-Only Secant Jost-Bridge Branch
- 前一輪：Round 70 — Dual Scalar Volterra Kernel
- canonical math delimiters：inline `$...$`；display `$$...$$`

## 0. 為什麼 Round 71 放棄「先證 derivative」

Round 70 把 ordinary-viscosity tangent 化成 scalar Jost kernel，但在極小 viscosity 下，finite-$J$ terminal eigenspace derivative仍會和 local source sum產生不必要的 cancellation。

然而 Round 68 真正需要的不是 derivative 本身。

它只需要中央 sign cone不要離開 endpoint 太遠。

因此 Round 71 改比較：

$$
\boxed{
R_n^\nu-R_n^0
}
$$

而不是：

$$
\partial_\nu R_n.
$$

這會把 local source 從：

$$
O(\nu)
$$

直接降成：

$$
\boxed{
O(\nu^2).
}
$$

---

# 1. Parity-rescaled transfer

沿用 Round 70：

$$
r_n=
\begin{cases}
u_n,&n\ {\rm even},\\
u_n/\nu,&n\ {\rm odd}.
\end{cases}
$$

在這個 chart：

$$
T_n^\nu=T_n^0
$$

for odd $n$，而 even $n$：

$$
\boxed{
T_n^\nu
=
T_n^0
+
\nu^2\mathcal E_n.
}
\tag{1.1}
$$

只有一個 transfer entry進入 $\mathcal E_n$。

---

# 2. Exact Secant Riccati Identity

寫：

$$
T_n^\nu
=
\begin{pmatrix}
A_n^\nu&B_n\\
C_n&D_n
\end{pmatrix}.
$$

令：

$$
R_n^\nu
=
(X_n^\nu)^{-1}
(
B_n-R_{n+1}^\nu D_n
),
$$

其中：

$$
X_n^\nu
=
R_{n+1}^\nu C_n-A_n^\nu.
$$

endpoint graph：

$$
R_n^0
=
(X_n^0)^{-1}
(
B_n-R_{n+1}^0D_n
).
$$

定義：

$$
\Delta R_n
=
R_n^\nu-R_n^0.
$$

因：

$$
A_n^\nu
=
A_n^0+\nu^2E_n
$$

on even layers，直接相減得到：

$$
\boxed{
\Delta R_n
=
(X_n^\nu)^{-1}
\left[
\nu^2E_nR_n^0
-
\Delta R_{n+1}
Y_n^0
\right],
}
\tag{2.1}
$$

where：

$$
\boxed{
Y_n^0
=
C_nR_n^0+D_n.
}
\tag{2.2}
$$

odd layer同式但 source 為零。

命名：

$$
\boxed{
\textbf{Secant Riccati Volterra Identity}.
}
$$

這是一個 exact finite-difference identity，不含 Taylor remainder。

---

# 3. 為什麼 secant 比 tangent 更適合最後封口

ordinary tangent local source：

$$
\partial_\nu(\nu^2)
=
2\nu.
$$

secant source則保留完整：

$$
\nu^2.
$$

因此 transition scale：

$$
n\sim\nu^{-1/3}
$$

上，local coefficient雖然有：

$$
|b_n/A_4^{(n)}|
\sim
n^4,
$$

但 secant kernel的 leading scale變成：

$$
\nu^2n^4
\times
n^{-2}
=
\nu^2n^2.
$$

對 transition width求和：

$$
\sum_{n\lesssim\nu^{-1/3}}
\nu^2n^2
=
O(\nu).
$$

所以中央 graph displacement天然就是：

$$
\boxed{
R_1^\nu-R_1^0
=
O(\nu).
}
$$

這正是 Round 60 數值一直看到的 linear matching law。

---

# 4. Corrected affine-Jost central chart

沿用 Round 69 的 true affine endpoint plane，先 subtract even-driven odd particular response。

central base：

$$
\boxed{
(e_0,\widetilde o_2,o_0),
}
$$

central output：

$$
\boxed{
(e_2,e_1,\widetilde o_1).
}
$$

endpoint graph的 condition numbers只有：

$$
\kappa_-\approx1.447,
\qquad
\kappa_+\approx1.579.
$$

所以最後 closure不需要在病態 companion chart 裡讀 central cone。

---

# 5. Exact central scalar solve

令：

$$
x
=
\widetilde o_2
=
o_2-o_{2,0}.
$$

在 sheared chart，$n=1$ central equation可寫成：

$$
\boxed{
c_0(R^\nu)
+
c_1(R^\nu)x
=
0.
}
\tag{5.1}
$$

endpoint：

$$
c_0(R^0)=0.
$$

且 exact endpoint Jost data給：

### small fibre

$$
\boxed{
c_{1,-}(R^0)
>
0.62,
}
\tag{5.2}
$$

### large fibre

$$
\boxed{
|c_{1,+}(R^0)|
>
4.47.
}
\tag{5.3}
$$

兩個 coefficient function對 graph entries 的 Lipschitz constants可粗取：

$$
\boxed{
L_-<5.21,
}
\tag{5.4}
$$

$$
\boxed{
L_+<33.1.
}
\tag{5.5}
$$

---

# 6. Central Secant-Cone Bridge Lemma

Suppose：

$$
\boxed{
\|R_1^\nu-R_1^0\|_{\max}
\le
8\times10^4\,\nu
}
\tag{6.1}
$$

for：

$$
0<\nu\le10^{-6}.
$$

Then：

$$
\delta
:=
\|R_1^\nu-R_1^0\|_{\max}
\le
0.08.
$$

### small fibre

Denominator remains：

$$
c_1>0.20.
$$

The central solve gives：

$$
|x|<2.1.
$$

Using the rigorous endpoint cone：

$$
e_{1,-}^0<-0.917,
$$

$$
4.16<o_{2,-}^0<4.17,
$$

we still obtain：

$$
\boxed{
e_{1,-}<-0.6,
}
$$

and：

$$
\boxed{
2<o_{2,-}<7.
}
$$

This is far inside Round 68's sufficient cone：

$$
e_1\le-0.1,
\qquad
0\le o_2\le100.
$$

### large fibre

Similarly：

$$
|c_1|>1.8,
$$

$$
|x|<1.5,
$$

and：

$$
\boxed{
e_{1,+}<-0.5,
\qquad
o_{2,+}>2.
}
$$

Hence the large sign cone also survives。

Therefore：

$$
\boxed{
\|R_1^\nu-R_1^0\|_{\max}
\le
8\times10^4\nu
\Longrightarrow
a_{3,\pm}(\nu)>0
}
\tag{6.2}
$$

through the entire final strip。

This completely bypasses a derivative theorem。

---

# 7. Corrected secant diagnostics

Using the true affine endpoint plane，the maximum graph-entry secant slopes are：

### small fibre

$$
\boxed{
\frac{
\|R_1^\nu-R_1^0\|_{\max}
}{
\nu
}
\approx
115.8
}
\tag{7.1}
$$

through the tested microscopic strip。

### large fibre

$$
\boxed{
\frac{
\|R_1^\nu-R_1^0\|_{\max}
}{
\nu
}
\approx
12.6
\text{--}
13.0.
}
\tag{7.2}
$$

The verifier extends this diagnostic to：

$$
\nu=10^{-9}.
$$

Compare with the sufficient theorem constant：

$$
8\times10^4.
$$

The proof target is therefore roughly：

- $700$ times looser on the small fibre；
- more than $6000$ times looser on the large fibre。

These remain diagnostics，not the missing uniform theorem。

---

# 8. Exact coefficient tail bound

The secant local source contains：

$$
\nu^2
\frac{
b_n
}{
A_4^{(n)}
}.
$$

Round 71 proves algebraically that for every real：

$$
n\ge100,
$$

the normalized coefficient ratio is strictly decreasing。

### small fibre

$$
\boxed{
\left|
\frac{
b_n
}{
A_4^{(n)}
}
\right|
<
14n^4.
}
\tag{8.1}
$$

At $n=100$ the exact value is：

$$
13.6558370\ldots n^4.
$$

### large fibre

$$
\boxed{
\left|
\frac{
b_n
}{
A_4^{(n)}
}
\right|
<
0.054n^4.
}
\tag{8.2}
$$

At $n=100$：

$$
0.05375034\ldots n^4.
$$

The verifier proves monotonicity by differentiating the exact algebraic ratio，shifting：

$$
n=m+100,
$$

and verifying every coefficient of the derivative numerator is negative while every denominator coefficient is positive in：

$$
\mathbb Q(\sqrt{17})[m].
$$

So this part is rigorous rather than sampled。

---

# 9. Cubic-WKB secant envelope

The exact secant dual formula has a scalar local kernel：

$$
\kappa_n^{\rm sec}.
$$

The remaining directional object is the Jost Green factor multiplying：

$$
\nu^2 b_n/A_4^{(n)}.
$$

Round 70 diagnostics suggest the natural majorant：

$$
\boxed{
|\kappa_n^{\rm sec}|
\lesssim
C
\nu^2n^2
e^{-c\nu n^3}.
}
\tag{9.1}
$$

This is exactly the expected cubic-WKB form。

---

# 10. Analytic sum of the cubic envelope

For：

$$
h(x)
=
\nu x^2
e^{-c\nu(x^3-N^3)},
$$

one has exactly：

$$
\boxed{
\int_N^\infty
h(x)\,dx
=
\frac1{3c}.
}
\tag{10.1}
$$

At：

$$
c=0.01,
$$

the integral is：

$$
33.\overline3.
$$

For：

$$
\nu\le10^{-6},
\qquad
N\ge100,
$$

the unimodal discrete correction is $<0.1$，so：

$$
\boxed{
\sum_{n\ge N}
\nu n^2
e^{-0.01\nu(n^3-N^3)}
<
34.
}
\tag{10.2}
$$

This summation estimate is rigorous and viscosity-uniform。

---

# 11. Candidate final Green-factor cone

Define the directional secant Green factor $\Gamma_n$ so that：

$$
|\kappa_n^{\rm sec}|
=
\nu^2
\left|
\frac{
b_n
}{
A_4^{(n)}
}
\right|
\Gamma_n.
$$

The next theorem only needs a deliberately loose cone such as：

$$
\boxed{
n^2
e^{\,0.02\nu(n^3-N_\ast^3)_+}
\Gamma_n
\le
200,
}
\tag{11.1}
$$

where：

$$
\boxed{
N_\ast
=
2\nu^{-1/3}.
}
\tag{11.2}
$$

Why this is enough：

For the worst small fibre coefficient：

$$
|b_n/A_4|\le14n^4.
$$

Before $N_\ast$：

$$
\sum
|\kappa_n|
\lesssim
14\times200
\nu^2
\sum_{n\le2\nu^{-1/3}}
n^2
<
8.4\times10^3\nu.
$$

After $N_\ast$，using the cubic envelope：

$$
\sum
|\kappa_n|
<
\frac{
14\times200
}{
3(0.02)
}
\nu
<
4.67\times10^4\nu.
$$

Thus：

$$
\boxed{
\text{$n\ge100$ source budget}
<
5.51\times10^4\nu.
}
\tag{11.3}
$$

The Central Secant-Cone Lemma allows：

$$
8\times10^4\nu.
$$

So the first $99$ layers plus the terminal pairing still receive a budget exceeding：

$$
\boxed{
2.4\times10^4\nu.
}
$$

Their actual diagnostics are vastly smaller。

---

# 12. What remains now

Round 70's generic task：

$$
\text{prove scalar kernel summability}
$$

has now been reduced to one concrete inequality：

$$
\boxed{
n^2
e^{0.02\nu(n^3-N_\ast^3)_+}
\Gamma_n
\le200.
}
$$

Everything around it is already accounted for：

- coefficient growth：proved；
- cubic summation：proved；
- central sign tolerance：proved；
- endpoint chart conditioning：proved；
- observed secant slope：$\sim115.8/13$；
- allowed slope：$8\times10^4$。

So the remaining theorem is a **directional Green-factor / Jost roughness estimate**。

---

# 13. STOP-C75 — Directional Green-Factor / Secant Jost-Passage Gap

$$
\boxed{
\begin{aligned}
\text{layer}
&=
\mathrm{parity\text{-}rescaled\ secant\ Riccati\ bridge},
\\
\Delta R_n
&=
(X_n^\nu)^{-1}
[
\nu^2E_nR_n^0
-
\Delta R_{n+1}Y_n^0
],
\\
\text{central sufficient displacement}
&=
8\times10^4\nu,
\\
\text{observed central slope}
&\approx
115.8,\ 13,
\\
|b/A_4|_{K_-}
&<
14n^4,
\\
|b/A_4|_{K_+}
&<
0.054n^4,
\\
\text{cubic envelope sum}
&<
34,
\\
\text{candidate directional cone}
&=
n^2e^{0.02\nu(n^3-N_\ast^3)_+}\Gamma_n\le200,
\\
\text{candidate }n\ge100\text{ budget}
&<
5.51\times10^4\nu,
\\
\text{remaining center+terminal budget}
&>
2.4\times10^4\nu,
\\
\text{remaining theorem}
&=
\mathrm{uniform\ directional\ Green\ factor}
\\
&\quad+
\mathrm{finite\ center/terminal\ closure},
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
\textbf{STOP-C75:
Directional Green-Factor / Secant Jost-Passage Gap}.
}
$$

---

# 14. 24/72 Ledger — Round 71

| Step | object | $B$ | $U$ | $O$ | $L$ | status |
|---|---|---|---|---|---|---|
| C1114 | secant graph $\Delta R$ | $\mathsf C$ | Jost Grassmannian | relational | $\mathsf F$ | DEFINED |
| C1115 | exact secant Riccati identity | $\mathsf C$ | graph difference | matrix | $\mathsf F$ | PROVED |
| C1116 | $\nu^2$ secant local source | $\mathsf C$ | parameter injection | scalar | $\mathsf F$ | EXACT |
| C1117 | central affine quotient | $\mathsf C$ | endpoint shear | scalar | $\mathsf F$ | EXACT |
| C1118 | central secant-cone lemma | $\mathsf C$ | sign geometry | targeted | $\mathsf F$ | PROVED CONDITIONAL |
| C1119 | corrected secant slopes | $\mathsf C$ | graph diagnostic | profile | $\mathsf F$ | VERIFIED |
| C1120 | small-fibre coefficient bound | $\mathsf C$ | tail coefficient | scalar | $\mathsf F$ | PROVED |
| C1121 | large-fibre coefficient bound | $\mathsf C$ | tail coefficient | scalar | $\mathsf F$ | PROVED |
| C1122 | cubic envelope summation | $\mathsf C$ | WKB majorant | scalar | $\mathsf F$ | PROVED |
| C1123 | directional Green-factor cone | $\mathsf C$ | dual Jost kernel | scalar | $\mathsf F$ | TARGET |
| C1124 | $n\ge100$ budget reduction | $\mathsf C$ | final bridge budget | scalar | $\mathsf F$ | PROVED CONDITIONAL |
| C1125 | finite-center/terminal budget | $\mathsf C$ | closure remainder | targeted | $\mathsf F$ | OPEN / STOP-C75 |

---

# 15. Continuous-versus-discrete status

The secant graph compares two continuous-viscosity admissible subspaces of the same periodic Floquet operator family。

The index $n$ remains a Fourier/Floquet coordinate。

The remaining theorem is a uniform continuous-parameter directional Green estimate。

Therefore：

$$
\boxed{
T_{\mathsf C\to\mathsf D}
=
\text{NOT YET REACHED}.
}
$$

---

# 16. Next round — Directional Green Cone / Final Secant Closure

Concrete targets：

1. move from the ill-conditioned companion graph to the Round 63 fast-Schur/Jost frame；
2. identify the two scalar primal/dual factors inside $\Gamma_n$；
3. prove their product carries the algebraic factor：
   $$
   n^{-2};
   $$
4. use Round 60's stable multiplier to prove：
   $$
   e^{-0.02\nu(n^3-N_\ast^3)}
   $$
   attenuation beyond the transition；
5. certify the first $99$ layers with a fixed endpoint-Jost interval box；
6. kill the terminal secant pairing by the same WKB attenuation；
7. conclude：
   $$
   \|R_1^\nu-R_1^0\|_{\max}
   <
   8\times10^4\nu;
   $$
8. invoke the Central Secant-Cone Lemma；
9. if successful：
   $$
   a_{3,\pm}(\nu)>0
   \qquad
   \forall\nu>0.
   $$

This becomes：

$$
\boxed{
\textbf{Directional Green Cone / Final Secant Closure}.
}
$$

---

# 17. External primary-source anchors

Fresh primary-source check before this round：

1. F. Battelli，M. Franca，K. J. Palmer，*Exponential Dichotomy for Noninvertible Linear Difference Equations*，arXiv:2111.04553.
   - roughness and persistence of difference-equation dichotomies；
   - relevant to lifting the reduced WKB Green bound to the full Jost bundle。

2. Pierre Del Moral，Emma Horton，*A note on Riccati matrix difference equations*，arXiv:2107.12918.
   - time-varying Riccati semigroup representations and uniform Riccati bounds；
   - relevant to the secant graph transform。

3. Fritz Gesztesy，Yuri Latushkin，Kevin Zumbrun，*Derivatives of (Modified) Fredholm Determinants and Stability of Standing and Traveling Waves*，arXiv:0802.1665.
   - develops parameter-derivative/Fredholm-determinant methods for semi-separable kernels；
   - adjacent framework for interpreting the dual Jost sensitivity kernel。

4. Yuri Latushkin，Shibi Vasudevan，*Fredholm determinants, continued fractions, Jost and Evans functions for a Jacobi matrix associated with the 2D-Euler equations*，arXiv:2401.14037.
   - hydrodynamic Jost/Evans/Fredholm/continued-fraction equivalence；
   - directly adjacent to the present Jost-Green formulation。

These are framework anchors only。The NS-specific secant identity，coefficient inequalities，central-cone budget and numerical slopes above are direct results of this series。
