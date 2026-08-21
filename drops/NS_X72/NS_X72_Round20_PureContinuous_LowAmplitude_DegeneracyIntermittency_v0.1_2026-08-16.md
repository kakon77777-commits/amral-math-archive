# NS × X 積分 × 24/72 範式實戰
## Round 20 — Pure Continuous Low-Amplitude Degeneracy / Normalized-Deformation Intermittency Route

- 日期：2026-08-16
- 版本：v0.1
- 狀態：Proof-Route Experiment / Continuous-Only Degenerate-Sublevel Branch
- canonical source：UTF-8 Markdown
- canonical math delimiters：inline `$...$`；display `$$...$$`
- 前一輪：`NS_X72_Round19_PureContinuous_CoupledConfluence_MiddleStrain_QuotientAmplitude_v0.1_2026-08-16.md`
- 本輪目標：直接研究上一輪唯一尚未解剖的 escape channel
  $$
  |v|\approx0
  $$
  且 physical strain / middle strain仍大的情況。把 inverse-amplitude carrier重新表達成 critical quotient mass下的 normalized-deformation moment，並判定 low-amplitude escape究竟需要 amplitude cliff、direction turning、gauge-Hessian blow-up或 high-rate intermittency。
- 非主張：本文沒有證明 normalized fourth moment可由 second moment無條件控制；本輪的 strongest result反而顯示這是新的 concentration/intermittency frontier。

---

# 0. Round 19 handoff

令：

$$
Q
=
\mathfrak Q_3[u],
$$

optimal representative：

$$
v
=
u+\nabla q,
$$

以及：

$$
r=|v|.
$$

Round 19 證明 dangerous determinant production可與 middle-strain channel constant-factor比較：

$$
\boxed{
\frac13
\lambda_2^+
|S|^2
\le
(-\det S)_+
\le
\frac12
\lambda_2^+
|S|^2.
}
\tag{0.1}
$$

並證明：

$$
\boxed{
\lambda_2^+
\le
|Sn|
\qquad
\forall n\in\mathbb S^2.
}
\tag{0.2}
$$

所以 dangerous middle strain不能靠選方向逃走。

剩餘 escape是：

$$
\boxed{
r=|v|\downarrow0
}
$$

while strain remains large。

Round 19 定義：

$$
\boxed{
\mathcal I_0
=
\int_{\{r>0\}}
\frac{|S|^4}{r}dx,
}
\tag{0.3}
$$

並得到：

$$
\boxed{
P_+^2
\le
\frac14
E_M
\mathcal I_0,
}
\tag{0.4}
$$

其中：

$$
P_+
=
\int
(-\det S)_+dx.
$$

本輪直接分析：

$$
\mathcal I_0.
$$

---

# 1. Critical quotient mass measure

因：

$$
Q^3
=
\int
r^3dx,
$$

若：

$$
Q>0,
$$

定義 probability measure：

$$
\boxed{
d\mu_Q(x)
=
\frac{
r(x)^3
}{
Q^3
}
dx.
}
\tag{1.1}
$$

這是 optimal quotient representative 自己產生的 scale-critical mass distribution。

在 NS scaling：

$$
v_\Lambda(x,t)
=
\Lambda
v(\Lambda x,\Lambda^2t),
$$

measure：

$$
r^3dx
$$

保持不變。

所以：

$$
\boxed{
\mu_Q
}
$$

是一個 natural critical probability carrier。

---

# 2. Normalized strain rate

在：

$$
r>0
$$

定義：

$$
\boxed{
K_S
=
\frac{
|S_u|
}{
r
}.
}
\tag{2.1}
$$

它在 NS scaling下：

$$
\boxed{
(K_S)_\Lambda
=
\Lambda K_S.
}
\tag{2.2}
$$

因此：

$$
K_S
$$

是一個 inverse-length / deformation-rate variable。

---

# 3. Weighted strain is the second normalized moment

Round 18 weighted strain carrier：

$$
W_S
=
\int
r|S_u|^2dx.
$$

因：

$$
|S_u|=rK_S,
$$

有 exact identity：

$$
\boxed{
W_S
=
\int
r^3K_S^2dx
=
Q^3
\mathbb E_{\mu_Q}
[K_S^2].
}
\tag{3.1}
$$

所以 Round 17–18 critical weighted physical-gradient budget至少包含 normalized strain rate的 second moment。

---

# 4. The inverse-amplitude carrier is exactly the fourth moment

Round 19：

$$
\mathcal I_0
=
\int
\frac{
|S_u|^4
}{
r
}
dx.
$$

使用：

$$
|S_u|=rK_S,
$$

得到：

$$
\boxed{
\mathcal I_0
=
\int
r^3K_S^4dx
=
Q^3
\mathbb E_{\mu_Q}
[K_S^4].
}
\tag{4.1}
$$

這是本輪第一個核心 identity。

因此：

$$
\boxed{
\textbf{
low-amplitude inverse-strain escape is exactly a fourth-moment problem
for normalized strain under critical quotient mass.
}
}
\tag{4.2}
$$

---

# 5. Degeneracy–Intermittency Ratio

若：

$$
W_S>0,
$$

定義 dimensionless ratio：

$$
\boxed{
\mathfrak J_S
=
\frac{
Q^3\mathcal I_0
}{
W_S^2
}.
}
\tag{5.1}
$$

由 Sections 3–4：

$$
\boxed{
\mathfrak J_S
=
\frac{
\mathbb E_{\mu_Q}[K_S^4]
}{
\mathbb E_{\mu_Q}[K_S^2]^2
}.
}
\tag{5.2}
$$

Cauchy / Jensen：

$$
\boxed{
\mathfrak J_S\ge1.
}
\tag{5.3}
$$

命名：

$$
\boxed{
\textbf{Normalized-Strain Intermittency Ratio}.
}
$$

它測量：

> normalized strain rate是否集中在相對少量的 critical quotient mass上。

---

# 6. Sharpened determinant-production inequality

由 Round 19：

$$
P_+
\le
\frac12
\int
\lambda_2^+
|S|^2dx.
$$

又：

$$
\lambda_2^+
\le
|S|,
$$

所以：

$$
P_+
\le
\frac12
\int
|S|^3dx.
$$

重寫：

$$
|S|^3
=
r^3K_S^3.
$$

因此：

$$
\boxed{
P_+
\le
\frac12
Q^3
\mathbb E_{\mu_Q}[K_S^3].
}
\tag{6.1}
$$

moment interpolation：

$$
\mathbb E[K_S^3]
\le
\mathbb E[K_S^2]^{1/2}
\mathbb E[K_S^4]^{1/2}.
$$

所以：

$$
\boxed{
P_+
\le
\frac12
\sqrt{
W_S
\mathcal I_0
}.
}
\tag{6.2}
$$

這比 Round 19 的：

$$
E_M
$$

upper envelope稍尖，因：

$$
W_S\le E_M.
$$

---

# 7. Production–Intermittency form

由：

$$
\mathcal I_0
=
\mathfrak J_S
\frac{
W_S^2
}{
Q^3
},
$$

(6.2) 變成：

$$
\boxed{
P_+
\le
\frac12
\frac{
W_S^{3/2}
}{
Q^{3/2}
}
\sqrt{
\mathfrak J_S
}.
}
\tag{7.1}
$$

因此 normalized production efficiency：

$$
\boxed{
\Pi_S
=
\frac{
2Q^{3/2}P_+
}{
W_S^{3/2}
}
}
\tag{7.2}
$$

滿足：

$$
\boxed{
\Pi_S^2
\le
\mathfrak J_S.
}
\tag{7.3}
$$

所以若 dangerous determinant production相對 weighted strain budget異常高，

normalized strain intermittency必同步高。

---

# 8. Continuous rate-tail representation

定義 critical-mass tail：

$$
\boxed{
M_S(\kappa)
=
\int_{\{K_S>\kappa\}}
r^3dx.
}
\tag{8.1}
$$

則：

$$
M_S(\kappa)
$$

是 continuous rate threshold：

$$
\kappa\in(0,\infty)
$$

下的 critical mass。

layer-cake：

$$
\boxed{
W_S
=
2
\int_0^\infty
\kappa
M_S(\kappa)
d\kappa.
}
\tag{8.2}
$$

以及：

$$
\boxed{
\mathcal I_0
=
4
\int_0^\infty
\kappa^3
M_S(\kappa)
d\kappa.
}
\tag{8.3}
$$

所以 second-to-fourth moment gap就是：

$$
\boxed{
\text{linear rate-tail weight}
\quad\text{versus}\quad
\text{cubic rate-tail weight}.
}
$$

沒有 discrete bins。

---

# 9. High-rate witness from intermittency

因：

$$
\mathbb E[K_S^4]
\le
\operatorname*{ess\,sup}
K_S^2
\,
\mathbb E[K_S^2],
$$

有：

$$
\boxed{
\operatorname*{ess\,sup}_{\mu_Q}
K_S^2
\ge
\mathfrak J_S
\mathbb E_{\mu_Q}[K_S^2].
}
\tag{9.1}
$$

因此：

$$
\boxed{
\operatorname*{ess\,sup}_{\mu_Q}
K_S
\ge
\sqrt{
\mathfrak J_S
}
\frac{
W_S^{1/2}
}{
Q^{3/2}
}.
}
\tag{9.2}
$$

所以 large $\mathfrak J_S$ 一定真的產生 high normalized deformation rate，而不是純 algebraic ratio artifact。

---

# 10. Exact normalized decomposition of the optimal representative

在：

$$
r>0,
$$

寫：

$$
v=rn.
$$

則：

$$
\boxed{
\nabla v
=
n\otimes\nabla r
+
r\nabla n.
}
\tag{10.1}
$$

由：

$$
n\cdot\partial_jn=0,
$$

有：

$$
\boxed{
\frac{
|\nabla v|^2
}{
r^2
}
=
|\nabla\log r|^2
+
|\nabla n|^2.
}
\tag{10.2}
$$

這是 exact amplitude–direction split。

---

# 11. The nonlinear gauge removes one logarithmic degree of freedom

critical gauge：

$$
\operatorname{div}(r^2n)=0
$$

給：

$$
\boxed{
n\cdot\nabla\log r
=
-\frac12
\operatorname{div}n.
}
\tag{11.1}
$$

令：

$$
P_n^\perp
=
I-n\otimes n.
$$

所以：

$$
\boxed{
\nabla\log r
=
P_n^\perp\nabla\log r
-
\frac12
(\operatorname{div}n)n.
}
\tag{11.2}
$$

從而：

$$
\boxed{
|\nabla\log r|^2
=
|P_n^\perp\nabla\log r|^2
+
\frac14
(\operatorname{div}n)^2.
}
\tag{11.3}
$$

所以沿 $n$ 的 logarithmic amplitude slope不是獨立自由變量。

它被 direction divergence精確決定。

---

# 12. Normalized gauge Hessian

定義：

$$
\boxed{
K_q
=
\frac{
\nabla^2q
}{
r
}
}
\tag{12.1}
$$

於：

$$
r>0.
$$

因：

$$
\nabla u
=
\nabla v-\nabla^2q,
$$

所以：

$$
\boxed{
\frac{
S_u
}{
r
}
=
\operatorname{sym}
\left[
n\otimes\nabla\log r
+
\nabla n
-
K_q
\right].
}
\tag{12.2}
$$

再用 (11.2)：

$$
\boxed{
\begin{aligned}
\frac{
S_u
}{
r
}
=
\operatorname{sym}
\Big[
&
n\otimes
P_n^\perp\nabla\log r
-
\frac12
(\operatorname{div}n)
n\otimes n
\\
&
+
\nabla n
-
K_q
\Big].
\end{aligned}
}
\tag{12.3}
$$

這是本輪第二個核心 exact identity。

---

# 13. Low-amplitude strain trichotomy

由 (12.3)，存在 universal constant：

$$
C
$$

使：

$$
\boxed{
K_S
\le
C
\left[
|P_n^\perp\nabla\log r|
+
|\nabla n|
+
|K_q|
\right].
}
\tag{13.1}
$$

其中：

$$
|\operatorname{div}n|
\le
\sqrt3|\nabla n|
$$

已吸收到第二項。

因此：

$$
\boxed{
\textbf{
large normalized strain at low amplitude requires at least one of:
}
}
$$

$$
\boxed{
\begin{aligned}
\mathrm{A}:&
\quad
\text{transverse logarithmic amplitude cliff},
\\
\mathrm{B}:&
\quad
\text{rapid direction turning},
\\
\mathrm{C}:&
\quad
\text{normalized optimal-gauge Hessian blow-up}.
\end{aligned}
}
\tag{13.2}
$$

這是 low-amplitude escape的 relational trichotomy。

---

# 14. Exact normalized Hodge budget

Round 15：

$$
D
=
\int
r
\left(
|\nabla v|^2
+
|\nabla r|^2
\right)dx.
$$

使用 (10.2)：

$$
\boxed{
D
=
\int
r^3
\left[
2|\nabla\log r|^2
+
|\nabla n|^2
\right]dx.
}
\tag{14.1}
$$

由 (11.3)：

$$
\boxed{
D
=
\int
r^3
\left[
2|P_n^\perp\nabla\log r|^2
+
\frac12(\operatorname{div}n)^2
+
|\nabla n|^2
\right]dx.
}
\tag{14.2}
$$

同時 Round 15 gauge-Hessian distortion：

$$
H
=
\int
r
\left(
|\nabla^2q|^2
+
|\nabla^2q\,n|^2
\right)dx
$$

變成：

$$
\boxed{
H
=
\int
r^3
\left[
|K_q|^2
+
|K_qn|^2
\right]dx.
}
\tag{14.3}
$$

所以：

$$
\boxed{
E_M=D+H
}
$$

正好是 critical mass measure下這些 normalized deformation rates的 second moment總和。

---

# 15. Second-Moment / Fourth-Moment Barrier

由 Section 14：

$$
\frac{
E_M
}{
Q^3
}
$$

控制 normalized amplitude/direction/gauge rates的 second moments。

但：

$$
\boxed{
\frac{
\mathcal I_0
}{
Q^3
}
=
\mathbb E_{\mu_Q}
[K_S^4]
}
$$

是 normalized strain 的 fourth moment。

因此現有 Pure-C coercive geometry給：

$$
\boxed{
L^2(d\mu_Q)
}
$$

型 normalized-rate control，

而 low-amplitude escape要求控制：

$$
\boxed{
L^4(d\mu_Q).
}
$$

命名：

$$
\boxed{
\textbf{Second-Moment / Fourth-Moment Barrier}.
}
$$

---

# 16. Why second moment alone cannot control fourth moment

在一般 probability measure class中，不存在 universal：

$$
\boxed{
\mathbb E[K^4]
\le
C
\mathbb E[K^2]^2
}
\tag{16.1}
$$

對固定 universal $C$ 成立。

例如令：

$$
K_N=N
$$

在 probability：

$$
N^{-2}
$$

的集合上，其他地方：

$$
K_N=0.
$$

則：

$$
\mathbb E[K_N^2]=1,
$$

但：

$$
\mathbb E[K_N^4]=N^2.
$$

所以：

$$
\boxed{
\textbf{
second-to-fourth moment upgrade requires additional anti-concentration structure.
}
}
\tag{16.2}
$$

這只是 measure-level no-go，不宣稱該 abstract distribution可由 actual NS normalized strain field任意 realize。

真正 proof obligation是從 NS + nonlinear gauge導出 extra structure。

---

# 17. Gauge-invariant vorticity at low amplitude

因：

$$
\nabla\times\nabla q=0,
$$

有：

$$
\boxed{
\omega
=
\nabla\times u
=
\nabla\times v.
}
\tag{17.1}
$$

而：

$$
v=rn,
$$

所以：

$$
\boxed{
\omega
=
\nabla r\times n
+
r\nabla\times n.
}
\tag{17.2}
$$

除以：

$$
r>0,
$$

得到：

$$
\boxed{
\frac{
\omega
}{
r
}
=
\nabla\log r\times n
+
\nabla\times n.
}
\tag{17.3}
$$

注意：

$$
(n\cdot\nabla\log r)n
$$

與 $n$ cross後消失。

所以：

$$
\boxed{
\frac{
\omega
}{
r
}
=
P_n^\perp\nabla\log r\times n
+
\nabla\times n.
}
\tag{17.4}
$$

因此 low-amplitude large vorticity只能由：

$$
\boxed{
\text{transverse amplitude cliff}
\quad\vee\quad
\text{direction turning}
}
$$

產生。

gauge Hessian不影響 vorticity。

---

# 18. Strain-only low-amplitude escape is a gauge-Hessian channel

若在某 low-amplitude region：

$$
\frac{|\omega|}{r}
$$

保持受控，

但：

$$
K_S=\frac{|S|}{r}
$$

很大，

則由 Sections 13 與 17，

純 amplitude/direction mechanisms不能單獨解釋全部 strain growth。

因此 large normalized strain必須顯著使用：

$$
\boxed{
K_q
=
\frac{\nabla^2q}{r}.
}
$$

所以 low-amplitude escape還可細分：

$$
\boxed{
\text{rotational degeneracy}
\quad\vee\quad
\text{gauge-curvature degeneracy}.
}
\tag{18.1}
$$

這重新接回 Round 15 的：

$$
H.
$$

---

# 19. Exact-zero set is a true degeneracy of the nonlinear-Hodge metric

Round 15 metric：

$$
M_v
=
r(I+n\otimes n).
$$

當：

$$
r\downarrow0,
$$

它退化。

在：

$$
r=0
$$

處：

$$
\boxed{
M_v=0
}
$$

formal。

所以 weighted Hodge energies：

$$
D,
\qquad
H
$$

對 exact-zero set失去直接 coercive weight。

這正是 low-amplitude escape存在的結構原因。

---

# 20. Local affine witness — exact zero does not force safe strain

取 trace-free symmetric：

$$
A
=
\operatorname{diag}(-2a,a,a),
\qquad
a>0.
$$

在 local affine model令：

$$
u(x)=Ax.
$$

定義：

$$
q(x)
=
-\frac12
x^\top A x.
$$

則：

$$
\nabla q=-Ax,
$$

所以：

$$
\boxed{
v=u+\nabla q=0.
}
$$

同時：

$$
\operatorname{div}u
=
\operatorname{tr}A
=
0.
$$

而：

$$
S_u=A,
$$

故：

$$
\boxed{
\lambda_2(S_u)=a>0.
}
$$

nonlinear gauge：

$$
\operatorname{div}(|v|v)=0
$$

trivially成立。

所以：

$$
\boxed{
\textbf{
the nonlinear gauge alone does not algebraically exclude
dangerous positive middle strain on an exact-zero representative set.
}
}
\tag{20.1}
$$

此 affine field不是 whole-space finite-energy NS solution。

它只是一個 local structural witness，排除「$v=0$ 自動代表 safe strain」的錯誤推論。

---

# 21. Exact-zero / near-zero dichotomy

因此 low-amplitude obstruction分成兩類。

## Z0 — exact-zero strain channel

若：

$$
\{r=0,\ |S|>0\}
$$

具有 nontrivial relevant measure/trace，

則 inverse-amplitude formulation應視為：

$$
\boxed{
\mathcal I_0=+\infty.
}
$$

weighted critical mass：

$$
r^3dx
$$

完全看不到該 exact-zero contribution。

## Z1 — near-zero intermittency channel

若 exact-zero strain channel可排除，

剩餘 danger由：

$$
r>0
$$

但：

$$
K_S=\frac{|S|}{r}
$$

具有 large fourth moment描述。

即：

$$
\boxed{
\mathfrak J_S
\gg1.
}
$$

---

# 22. Continuous sublevel representation

定義：

$$
F_4(\eta)
=
\int_{\{0<r<\eta\}}
|S|^4dx.
$$

因：

$$
\frac1r
=
\int_r^\infty
\eta^{-2}d\eta,
$$

Tonelli：

$$
\boxed{
\mathcal I_0
=
\int_0^\infty
\frac{
F_4(\eta)
}{
\eta^2
}
d\eta
}
\tag{22.1}
$$

對 $r>0$ contribution。

所以 near-zero escape完全由 continuous sublevel function：

$$
\eta
\longmapsto
F_4(\eta)
$$

描述。

例如若近零有：

$$
F_4(\eta)
\le
C
\eta^{1+\delta}
$$

對某：

$$
\delta>0,
$$

則：

$$
\int_0^{\eta_0}
\frac{
F_4(\eta)
}{
\eta^2
}
d\eta
<
\infty.
$$

所以 sufficiently fast sublevel decay會封住 near-zero inverse-amplitude divergence。

---

# 23. Continuous normalized-rate layer

也可以直接對：

$$
K_S
$$

做 continuous rate layers：

$$
\mathcal R_\kappa
=
\left\{
\frac{
|S|
}{
|v|
}
>
\kappa
\right\}.
$$

由 (8.2)–(8.3)：

$$
\boxed{
\begin{aligned}
W_S
&=
2
\int_0^\infty
\kappa
\left[
\int_{\mathcal R_\kappa}
r^3dx
\right]
d\kappa,
\\
\mathcal I_0
&=
4
\int_0^\infty
\kappa^3
\left[
\int_{\mathcal R_\kappa}
r^3dx
\right]
d\kappa.
\end{aligned}
}
\tag{23.1}
$$

所以 zero/near-zero problem可以完全改寫成 continuous normalized-rate tail。

---

# 24. STOP-C24 — Normalized-Deformation Intermittency / Zero-Set Degeneracy Gap

定義：

$$
\boxed{
\bot_X^{\mathrm{C24}}
=
\left\langle
\begin{array}{l}
\text{layer}
=
\mathrm{low\text{-}amplitude\ quotient\ degeneracy},
\\
\text{critical\ mass}
=
d\mu_Q=r^3dx/Q^3,
\\
\text{normalized\ strain}
=
K_S=|S|/r,
\\
\text{weighted\ strain}
=
Q^3\mathbb E[K_S^2],
\\
\text{inverse\ carrier}
=
Q^3\mathbb E[K_S^4],
\\
\text{intermittency}
=
\mathfrak J_S
=
\mathbb E[K_S^4]/\mathbb E[K_S^2]^2,
\\
\text{rate\ decomposition}
=
\text{amplitude cliff}
\vee
\text{direction turning}
\vee
\text{normalized gauge Hessian},
\\
\text{exact-zero gauge coercivity}
=
\mathrm{degenerate},
\\
\text{exact-zero safe-strain implication}
=
\mathrm{false},
\\
\text{missing}
=
\mathrm{anti\text{-}concentration\ or\ zero\text{-}set\ control
sufficient\ to\ upgrade\ second\ to\ fourth\ moment},
\\
\text{essential\ discrete\ intrusion}
=
\mathrm{false}.
\end{array}
\right\rangle.
}
$$

命名：

$$
\boxed{
\textbf{STOP-C24:
Normalized-Deformation Intermittency / Zero-Set Degeneracy Gap}.
}
$$

---

# 25. 24/72 Ledger — Round 20

| Step | object | $B$ | $U$ | $O$ | $L$ | status |
|---|---|---|---|---|---|---|
| C242 | critical mass $\mu_Q$ | $\mathsf C$ | measure/quotient | $\mathsf X$ | $\mathsf F$ | FORM |
| C243 | normalized strain $K_S$ | $\mathsf C$ | relational | scalar field | $\mathsf F$ | FORM |
| C244 | $W_S=Q^3\mathbb E[K_S^2]$ | $\mathsf C$ | moment | scalar | $\mathsf F$ | EXACT |
| C245 | $\mathcal I_0=Q^3\mathbb E[K_S^4]$ | $\mathsf C$ | moment | scalar | $\mathsf F$ | EXACT |
| C246 | intermittency ratio $\mathfrak J_S$ | $\mathsf C$ | recognition | scalar | $\mathsf F$ | FORM |
| C247 | production–intermittency bound | $\mathsf C$ | moment interpolation | targeted | $\mathsf F$ | PROVED |
| C248 | continuous rate tails | $\mathsf C$ | layer-cake | profile | $\mathsf F$ | EXACT |
| C249 | $\nabla v/r$ amplitude–direction split | $\mathsf C$ | differential | relational | $\mathsf F$ | EXACT |
| C250 | gauge logarithmic constraint | $\mathsf C$ | constraint | relational | $\mathsf F$ | EXACT |
| C251 | normalized strain decomposition | $\mathsf C$ | quotient/gauge | $\mathsf X$ | $\mathsf F$ | EXACT |
| C252 | low-amplitude trichotomy | $\mathsf C$ | relational | $\mathsf X$ | $\mathsf F$ | PROVED |
| C253 | normalized Hodge second-moment budget | $\mathsf C$ | variational | $\mathsf X$ | $\mathsf F$ | EXACT |
| C254 | second-to-fourth moment closure | $\mathsf C$ | moment | targeted | $\mathsf F$ | NO-GO without extra structure |
| C255 | normalized vorticity decomposition | $\mathsf C$ | curl geometry | relational | $\mathsf F$ | EXACT |
| C256 | exact-zero dangerous-strain witness | $\mathsf C$ | local affine | targeted | $\mathsf F$ | CONSTRUCTED structural witness |
| C257 | continuous sublevel inverse carrier | $\mathsf C$ | layer-cake | profile | $\mathsf F$ | EXACT |
| C258 | unconditional anti-concentration / zero-set closure | $\mathsf C$ | — | targeted | $\mathsf F$ | OPEN / STOP-C24 |

---

# 26. Continuous-versus-discrete status

本輪直接進入：

- zero set；
- near-zero tubular/sublevel regions；
- normalized deformation-rate tails。

仍然全部可用：

$$
r\in[0,\infty),
\qquad
\eta\in(0,\infty),
\qquad
\kappa\in(0,\infty)
$$

的 continuous coordinates描述。

沒有：

- countable zero components；
- discrete strata index；
- dyadic near-zero shells；
- atomic decomposition。

因此：

$$
\boxed{
T_{\mathsf C\to\mathsf D}
=
\text{NOT YET REACHED}.
}
\tag{26.1}
$$

---

# 27. Strongest results of Round 20

## R20-A — critical second/fourth moment identification

$$
\boxed{
W_S
=
Q^3\mathbb E_{\mu_Q}[K_S^2],
}
$$

$$
\boxed{
\mathcal I_0
=
Q^3\mathbb E_{\mu_Q}[K_S^4].
}
$$

## R20-B — intermittency controls production efficiency

$$
\boxed{
\frac{
2Q^{3/2}P_+
}{
W_S^{3/2}
}
\le
\sqrt{
\mathfrak J_S
}.
}
$$

## R20-C — normalized strain decomposition

$$
\boxed{
\frac{
S_u
}{
r
}
=
\operatorname{sym}
\left[
n\otimes\nabla\log r
+
\nabla n
-
\frac{\nabla^2q}{r}
\right].
}
$$

## R20-D — low-amplitude trichotomy

$$
\boxed{
\text{large }|S|/|v|
\Rightarrow
\text{amplitude cliff}
\vee
\text{direction turning}
\vee
\text{normalized gauge-Hessian blow-up}.
}
$$

## R20-E — exact-zero is not automatically safe

The local affine witness has：

$$
v=0,
\qquad
\lambda_2(S_u)>0.
$$

所以 zero set本身不是 automatic safe branch。

---

# 28. Next round — dynamic intermittency / critical-mass transport

下一輪不再追：

$$
r\to0
$$

的位置本身。

直接追：

$$
\boxed{
\mu_Q
}
$$

與：

$$
\boxed{
K_S
}
$$

的 dynamics。

核心問題：

1. critical mass density：
   $$
   r^3
   $$
   是否滿足某個 transport–diffusion balance；

2. normalized strain rate：
   $$
   K_S=|S|/r
   $$
   的 material growth如何和 $r$ 的 collapse競爭；

3. $\mathfrak J_S$ 是否有 self-regularizing dynamics；

4. 若 fourth moment增加，是否必強迫 second moment / Hodge budget同步增加；

5. 若 high-rate tail只能靠 mass集中到 increasingly thin regions，使用 continuous concentration function，不使用 dyadic scales；

6. 只有當 concentration compactness本身無法避免 subsequence / profile index，才第一次認真測試：
   $$
   \mathsf C\to\mathsf D.
   $$

---

# 29. External primary-source anchors

1. Alexis Vasseur, *Regularity criterion for 3D Navier-Stokes equations in terms of the direction of the velocity*, arXiv:0705.2446.
   - velocity magnitude/direction decomposition與 direction-divergence regularity criterion提供外部幾何背景；
   - 本輪 $n=v/|v|$ 是 optimal quotient representative direction，不等同於原 velocity direction。

2. Evan Miller, *A regularity criterion for the Navier-Stokes equation involving only the middle eigenvalue of the strain tensor*, arXiv:1710.05569.
   - positive middle-strain channel作為 scale-critical regularity/blow-up carrier的 primary-source背景。

3. Evan Miller, *On the interaction of strain and vorticity for solutions of the Navier--Stokes equation*, arXiv:2407.02691.
   - strain–vorticity interaction與 determinant/enstrophy structure的 primary-source背景。

本輪 critical mass moments、normalized-strain intermittency、normalized gauge decomposition、exact-zero affine witness與 second/fourth-moment barrier均為本文直接推導。

---

# 30. Commit state

$$
\boxed{
\begin{aligned}
\text{Route}
&=
\mathrm{Pure\ Continuous\ Low\text{-}Amplitude\ Degeneracy},
\\
\text{Essential }\mathsf C\to\mathsf D
&=
\mathrm{Not\ reached},
\\
\text{Critical mass}
&=
d\mu_Q=r^3dx/Q^3,
\\
\text{Normalized strain}
&=
K_S=|S|/r,
\\
\text{Second moment}
&=
W_S/Q^3,
\\
\text{Fourth moment}
&=
\mathcal I_0/Q^3,
\\
\text{Intermittency ratio}
&=
\mathfrak J_S,
\\
\text{Low-amplitude mechanisms}
&=
\mathrm{amplitude\ cliff}
\vee
\mathrm{direction\ turning}
\vee
\mathrm{gauge\ Hessian},
\\
\text{Exact-zero safe branch}
&=
\mathrm{false},
\\
\text{STOP-C24}
&=
\mathrm{Normalized\text{-}Deformation\ Intermittency/Zero\text{-}Set\ Degeneracy\ Gap},
\\
\text{Next}
&=
\mathrm{Dynamic\ Intermittency/Critical\text{-}Mass\ Transport}.
\end{aligned}
}
$$
