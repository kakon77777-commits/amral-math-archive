# NS × X 積分 × 24/72 範式實戰
## Round 16 — Pure Continuous Layer-Cake / Superlevel-Distortion Route

- 日期：2026-08-16
- 版本：v0.1
- 狀態：Proof-Route Experiment / Continuous-Only Amplitude-Level Branch
- canonical source：UTF-8 Markdown
- canonical math delimiters：inline `$...$`；display `$$...$$`
- 前一輪：`NS_X72_Round15_PureContinuous_pHodge_GaugeHessianDistortion_v0.1_2026-08-16.md`
- 本輪目標：不用 dyadic decomposition、atomic decomposition 或離散 shell，直接以 continuous amplitude threshold
  $$
  \lambda\in(0,\infty)
  $$
  分解 Round 15 的 quotient dissipation $D$ 與 gauge-Hessian distortion $H$。檢驗全域 distortion ratio $\Xi_Q$ 若變危險，是否必然在某個 continuous superlevel layer 上留下可定位 witness。
- 非主張：本文沒有證明所有 superlevel distortion ratios 都受控；相反地，本輪把全域 obstruction壓成 continuous tail ratio、surface ratio與 level-boundary flux問題。

---

# 0. Round 15 handoff

令

$$
Q
=
\mathfrak Q_3[u],
$$

optimal representative：

$$
v=u+\nabla q,
$$

並設

$$
r=|v|,
\qquad
n=\frac v{|v|}
$$

於 $r>0$。

Round 15 定義：

$$
D
=
\int_{\mathbb R^3}
r
\left(
|\nabla v|^2
+
|\nabla r|^2
\right)dx,
$$

以及：

$$
H
=
\int_{\mathbb R^3}
r
\left(
|\nabla^2q|^2
+
|\nabla^2q\,n|^2
\right)dx.
$$

並得到：

$$
\boxed{
\frac13
\frac d{dt}Q^3
+
\nu D
=
I_Q,
}
\tag{0.1}
$$

以及：

$$
\boxed{
|I_Q|
\le
C
Q
H^{1/2}
D^{1/2}.
}
\tag{0.2}
$$

定義：

$$
\boxed{
\Xi_Q
=
\frac{
Q^2H
}{
\nu^2D
}.
}
\tag{0.3}
$$

若：

$$
\frac d{dt}Q^3>0,
$$

則：

$$
\boxed{
\Xi_Q
>
c_0
}
\tag{0.4}
$$

對某 universal threshold $c_0>0$。

Round 15 STOP：

$$
\boxed{
\text{STOP-C19}
=
\text{Weighted Gauge-Hessian / Quotient-Dissipation Gap}.
}
$$

---

# 1. Continuous superlevel sets

對每個：

$$
\lambda\ge0,
$$

定義：

$$
\boxed{
E_\lambda
=
\{
x\in\mathbb R^3:
r(x)>\lambda
\}.
}
\tag{1.1}
$$

distribution function：

$$
\boxed{
V(\lambda)
=
|E_\lambda|.
}
\tag{1.2}
$$

定義 unweighted local densities：

$$
\boxed{
A
=
|\nabla v|^2+|\nabla r|^2,
}
\tag{1.3}
$$

以及：

$$
\boxed{
B
=
|\nabla^2q|^2
+
|\nabla^2q\,n|^2.
}
\tag{1.4}
$$

在 $r=0$ 處第二項定義為零。

tail profiles：

$$
\boxed{
d(\lambda)
=
\int_{E_\lambda}
A\,dx,
}
\tag{1.5}
$$

$$
\boxed{
h(\lambda)
=
\int_{E_\lambda}
B\,dx.
}
\tag{1.6}
$$

兩者皆 nonincreasing。

---

# 2. Exact layer-cake identities

因：

$$
r(x)
=
\int_0^\infty
\mathbf 1_{\{r(x)>\lambda\}}
\,d\lambda,
$$

Tonelli 給：

$$
\boxed{
D
=
\int_0^\infty
d(\lambda)\,d\lambda,
}
\tag{2.1}
$$

以及：

$$
\boxed{
H
=
\int_0^\infty
h(\lambda)\,d\lambda.
}
\tag{2.2}
$$

同理：

$$
r^3
=
\int_0^\infty
3\lambda^2
\mathbf 1_{\{r>\lambda\}}
d\lambda,
$$

所以：

$$
\boxed{
Q^3
=
\|v\|_3^3
=
3
\int_0^\infty
\lambda^2
V(\lambda)
\,d\lambda.
}
\tag{2.3}
$$

因此 critical amplitude、dissipation與 gauge distortion全部可由同一個 continuous level parameter：

$$
\lambda
$$

描述。

---

# 3. Tail distortion ratio

當：

$$
d(\lambda)>0,
$$

定義：

$$
\boxed{
\theta(\lambda)
=
\frac{
h(\lambda)
}{
d(\lambda)
}.
}
\tag{3.1}
$$

再定義 dimensionless superlevel distortion ratio：

$$
\boxed{
\xi_Q(\lambda)
=
\frac{
Q^2
}{
\nu^2
}
\theta(\lambda)
=
\frac{
Q^2h(\lambda)
}{
\nu^2d(\lambda)
}.
}
\tag{3.2}
$$

若：

$$
d(\lambda)=0<h(\lambda),
$$

定義：

$$
\xi_Q(\lambda)=+\infty.
$$

---

# 4. Global distortion is a continuous weighted average of tail distortion

由 (2.1)–(2.2)：

$$
\frac HD
=
\frac{
\int_0^\infty
\theta(\lambda)d(\lambda)d\lambda
}{
\int_0^\infty
d(\lambda)d\lambda
}.
$$

所以：

$$
\boxed{
\Xi_Q
=
\frac{
\int_0^\infty
\xi_Q(\lambda)
d(\lambda)d\lambda
}{
\int_0^\infty
d(\lambda)d\lambda
}.
}
\tag{4.1}
$$

因此：

$$
\boxed{
\Xi_Q
\le
\operatorname*{ess\,sup}_{\lambda>0}
\xi_Q(\lambda).
}
\tag{4.2}
$$

這是一個 exact mean-value structure。

---

# 5. Continuous Superlevel Distortion Witness

由 Round 15：

$$
\frac d{dt}Q^3>0
\Longrightarrow
\Xi_Q>c_0.
$$

由 (4.2)：

$$
\boxed{
\frac d{dt}Q^3>0
\Longrightarrow
\exists\lambda_\ast>0
:
\xi_Q(\lambda_\ast)>c_0
}
\tag{5.1}
$$

在 essential-supremum sense。

命名：

$$
\boxed{
\textbf{Continuous Superlevel Distortion Witness}.
}
$$

意思：

> 全域 critical quotient 真正增長時，gauge-Hessian distortion 不能只以不可定位的 weighted average 存在；至少有一個實數 amplitude threshold，其整個 high-amplitude tail 已跨過相同量級的 distortion/dissipation 門檻。

這不是 dyadic pigeonhole。

threshold：

$$
\lambda_\ast
$$

屬於 continuous amplitude continuum。

---

# 6. Coarea representation

假設在固定 smooth time slice：

$$
r
$$

足夠 regular。

對 a.e. regular value：

$$
\lambda,
$$

coarea formula給：

$$
\boxed{
-d'(\lambda)
=
\int_{\{r=\lambda\}}
\frac{
A
}{
|\nabla r|
}
\,dS.
}
\tag{6.1}
$$

以及：

$$
\boxed{
-h'(\lambda)
=
\int_{\{r=\lambda\}}
\frac{
B
}{
|\nabla r|
}
\,dS.
}
\tag{6.2}
$$

同時：

$$
\boxed{
-V'(\lambda)
=
\int_{\{r=\lambda\}}
\frac1{|\nabla r|}
\,dS.
}
\tag{6.3}
$$

在 critical points 可用 standard a.e. coarea interpretation。

---

# 7. Surface distortion ratio

定義：

$$
a_\Sigma(\lambda)
=
-d'(\lambda),
$$

$$
b_\Sigma(\lambda)
=
-h'(\lambda).
$$

當：

$$
a_\Sigma(\lambda)>0,
$$

定義 instantaneous level-surface distortion ratio：

$$
\boxed{
\sigma(\lambda)
=
\frac{
b_\Sigma(\lambda)
}{
a_\Sigma(\lambda)
}.
}
\tag{7.1}
$$

tail ratio：

$$
\theta=\frac hd.
$$

直接微分：

$$
\boxed{
\theta'(\lambda)
=
\frac{
a_\Sigma(\lambda)
}{
d(\lambda)
}
\left[
\theta(\lambda)
-
\sigma(\lambda)
\right].
}
\tag{7.2}
$$

命名：

$$
\boxed{
\textbf{Continuous Tail–Surface Ratio Equation}.
}
$$

---

# 8. Interpretation of the ratio equation

若：

$$
\sigma(\lambda)
<
\theta(\lambda),
$$

則：

$$
\theta'(\lambda)>0.
$$

也就是移除當前 level surface後，剩餘更高 amplitude tail變得更 distorted。

若：

$$
\sigma(\lambda)
>
\theta(\lambda),
$$

則：

$$
\theta'(\lambda)<0.
$$

因此 high-amplitude distortion growth不是離散 shell hopping。

它可以被描述成 continuous amplitude-coordinate 上：

$$
\boxed{
\text{tail ratio}
\leftrightarrow
\text{boundary-surface ratio}
}
$$

的流動。

---

# 9. Continuous superlevel Sobolev bridge

令：

$$
0\le\lambda<\mu.
$$

取：

$$
f_\lambda
=
(r-\lambda)_+.
$$

Sobolev：

$$
\|f_\lambda\|_6^2
\le
C
\int_{E_\lambda}
|\nabla r|^2dx
\le
C d(\lambda).
$$

但在：

$$
E_\mu,
$$

有：

$$
f_\lambda
\ge
\mu-\lambda.
$$

因此：

$$
\boxed{
(\mu-\lambda)^2
V(\mu)^{1/3}
\le
C
d(\lambda).
}
\tag{9.1}
$$

命名：

$$
\boxed{
\textbf{Continuous Interlevel Sobolev Constraint}.
}
$$

這表示：

> 要讓高 amplitude superlevel set保持大體積，較低 threshold 上必須支付 gradient dissipation。

---

# 10. Deviatoric curvature tail

Round 15 已證：

$$
I_Q
=
\int
r^3
n^\top H_q^0n\,dx,
$$

其中：

$$
H_q^0
=
\nabla^2q
-
\frac13(\Delta q)I.
$$

定義：

$$
\boxed{
c(\lambda)
=
\int_{E_\lambda}
n^\top H_q^0n\,dx.
}
\tag{10.1}
$$

layer-cake：

$$
\boxed{
I_Q
=
3
\int_0^\infty
\lambda^2
c(\lambda)
\,d\lambda.
}
\tag{10.2}
$$

所以 critical quotient growth本身也可用 continuous amplitude layers精確重寫。

---

# 11. Tail curvature bound

存在 universal：

$$
C_0>0
$$

使：

$$
|H_q^0|
\le
C_0|\nabla^2q|.
$$

因此：

$$
|c(\lambda)|
\le
C_0
\left(
\int_{E_\lambda}
|\nabla^2q|^2dx
\right)^{1/2}
V(\lambda)^{1/2}.
$$

由：

$$
h(\lambda)
\ge
\int_{E_\lambda}
|\nabla^2q|^2dx,
$$

得到：

$$
\boxed{
|c(\lambda)|
\le
C_0
h(\lambda)^{1/2}
V(\lambda)^{1/2}.
}
\tag{11.1}
$$

所以：

$$
\boxed{
|I_Q|
\le
3C_0
\int_0^\infty
\lambda^2
h(\lambda)^{1/2}
V(\lambda)^{1/2}
\,d\lambda.
}
\tag{11.2}
$$

---

# 12. Continuous Dangerous-Layer Witness

定義：

$$
\boxed{
\Gamma_Q(\lambda)
=
\frac{
3C_0
\lambda^2
h(\lambda)^{1/2}
V(\lambda)^{1/2}
}{
\nu d(\lambda)
}
}
\tag{12.1}
$$

於：

$$
d(\lambda)>0.
$$

若所有：

$$
\lambda
$$

都滿足：

$$
\Gamma_Q(\lambda)\le1,
$$

則由 (11.2)：

$$
|I_Q|
\le
\nu
\int_0^\infty
d(\lambda)d\lambda
=
\nu D.
$$

因此：

$$
\frac d{dt}Q^3
\le0.
$$

反過來：

$$
\boxed{
\frac d{dt}Q^3>0
\Longrightarrow
\exists\lambda_\ast:
\Gamma_Q(\lambda_\ast)>1.
}
\tag{12.2}
$$

命名：

$$
\boxed{
\textbf{Continuous Dangerous-Layer Witness}.
}
$$

這比 Section 5 更直接把 growth與：

- tail gauge Hessian；
- tail volume；
- tail dissipation；

放在同一個 threshold。

---

# 13. Cross-level necessary condition

在 (9.1) 選：

$$
\mu=\lambda,
\qquad
\lambda_0=\frac\lambda2.
$$

得到：

$$
\frac{\lambda^2}{4}
V(\lambda)^{1/3}
\le
C
d(\lambda/2).
$$

所以：

$$
\boxed{
V(\lambda)^{1/2}
\le
C
\frac{
d(\lambda/2)^{3/2}
}{
\lambda^3
}.
}
\tag{13.1}
$$

代入：

$$
\Gamma_Q(\lambda)>1
$$

得到必要條件：

$$
\boxed{
h(\lambda)^{1/2}
d(\lambda/2)^{3/2}
>
c
\nu
\lambda
d(\lambda)
}
\tag{13.2}
$$

對某 universal：

$$
c>0.
$$

所以 dangerous high-amplitude layer需要一個 continuous two-threshold imbalance：

$$
\boxed{
\lambda/2
\longrightarrow
\lambda.
}
$$

注意：

$$
\frac12
$$

在這裡只是方便選擇，不是 dyadic hierarchy。

可對任意：

$$
0<\alpha<1
$$

選：

$$
\lambda_0=\alpha\lambda.
$$

---

# 14. Localizing nonlinear-Hodge orthogonality

Round 15 differentiated gauge：

$$
\operatorname{div}
\left(
M_v\partial_\ell v
\right)
=
0,
$$

其中：

$$
M_v
=
r(I+n\otimes n).
$$

全空間測：

$$
q_\ell=\partial_\ell q
$$

得到 global orthogonality：

$$
\int
\nabla q_\ell
\cdot
M_v
\partial_\ell v
dx
=
0.
$$

現在限制到：

$$
E_\lambda.
$$

對 regular level，integration by parts給：

$$
\boxed{
\int_{E_\lambda}
\nabla q_\ell
\cdot
M_v
\partial_\ell v
dx
=
\int_{\partial E_\lambda}
q_\ell
\left(
M_v\partial_\ell v
\right)
\cdot
\nu_\lambda
\,dS.
}
\tag{14.1}
$$

其中：

$$
\nu_\lambda
$$

為 $E_\lambda$ outward normal。

定義：

$$
\boxed{
\mathcal B_Q(\lambda)
=
\sum_{\ell=1}^3
\int_{\partial E_\lambda}
q_\ell
\left(
M_v\partial_\ell v
\right)
\cdot
\nu_\lambda
\,dS.
}
\tag{14.2}
$$

---

# 15. Local Pythagorean identity acquires a boundary flux

定義：

$$
D_M(\lambda)
=
\sum_\ell
\int_{E_\lambda}
\partial_\ell v
\cdot
M_v
\partial_\ell v\,dx,
$$

$$
H_M(\lambda)
=
\sum_\ell
\int_{E_\lambda}
\nabla q_\ell
\cdot
M_v
\nabla q_\ell\,dx,
$$

以及：

$$
E_M^u(\lambda)
=
\sum_\ell
\int_{E_\lambda}
\partial_\ell u
\cdot
M_v
\partial_\ell u\,dx.
$$

因：

$$
\partial_\ell u
=
\partial_\ell v-\nabla q_\ell,
$$

由 (14.1)：

$$
\boxed{
E_M^u(\lambda)
=
D_M(\lambda)
+
H_M(\lambda)
-
2\mathcal B_Q(\lambda).
}
\tag{15.1}
$$

這就是 localized nonlinear-Hodge Pythagorean identity。

全空間：

$$
\mathcal B_Q=0
$$

時恢復 Round 15：

$$
E_M^u=D+H.
$$

---

# 16. Localization is not free

Section 15 顯示：

$$
\boxed{
\text{global nonlinear-Hodge orthogonality}
}
$$

不會無損地限制到每個：

$$
E_\lambda.
$$

localization生成：

$$
\boxed{
\text{level-surface boundary flux }\mathcal B_Q(\lambda).
}
$$

因此即使 Continuous Superlevel Distortion Witness告訴我們：

> 某一層一定很危險，

要把 global Pythagorean coercivity搬到該層時，必須控制：

$$
\boxed{
\mathcal B_Q(\lambda).
}
$$

這是本輪真正的新 obstruction。

---

# 17. Boundary flux is continuous, not discrete

level boundary：

$$
\partial E_\lambda
=
\{r=\lambda\}
$$

隨：

$$
\lambda
$$

連續掃過 amplitude geometry。

所以：

$$
\mathcal B_Q:
(0,\infty)
\to\mathbb R
$$

是一個 continuous-level flux profile。

目前沒有任何理由必須把：

$$
\lambda
$$

替換成：

$$
2^j.
$$

因此 level localization本身仍然完全 Pure-C。

---

# 18. Layer profile as an X-state

本輪建立：

$$
\boxed{
X_{\rm layer}(\lambda)
=
\left\langle
V(\lambda),
d(\lambda),
h(\lambda),
\theta(\lambda),
\sigma(\lambda),
c(\lambda),
\Gamma_Q(\lambda),
\mathcal B_Q(\lambda)
\right\rangle.
}
\tag{18.1}
$$

整個 weighted nonlinear-Hodge obstruction被提升成 continuous field：

$$
\boxed{
\lambda
\longmapsto
X_{\rm layer}(\lambda).
}
\tag{18.2}
$$

所以 Round 15 的單一 global ratio：

$$
\Xi_Q
$$

現在被 resolution 成一條 continuous amplitude-profile。

---

# 19. Observation update

只知道：

$$
\Xi_Q
$$

能告訴：

$$
\exists\lambda_\ast
$$

危險，

但不能告訴：

- danger在哪個 threshold；
- tail ratio如何隨 threshold移動；
- level surface本身的 distortion density；
- localized orthogonality boundary flux。

因此：

$$
\boxed{
\mathsf C_{\Xi_Q}
\to
\mathsf X_{\rm layer}
}
$$

是本輪 observation refinement。

但：

$$
X_{\rm layer}
$$

仍是 continuous object。

---

# 20. STOP-C20 — Continuous Layer Distortion / Boundary-Flux Gap

定義：

$$
\boxed{
\bot_X^{\mathrm{C20}}
=
\left\langle
\begin{array}{l}
\text{layer}
=
\mathrm{continuous\ amplitude\ superlevels},
\\
\text{global\ distortion}
=
\mathrm{weighted\ average\ of\ tail\ ratios},
\\
\text{positive\ growth}
\Rightarrow
\mathrm{dangerous\ continuous\ layer},
\\
\text{tail\ evolution}
=
\theta'
=
(a_\Sigma/d)(\theta-\sigma),
\\
\text{interlevel\ constraint}
=
(\mu-\lambda)^2V(\mu)^{1/3}
\lesssim
d(\lambda),
\\
\text{localized\ Hodge\ identity}
=
E_M^u
=
D_M+H_M-2\mathcal B_Q,
\\
\text{missing}
=
\mathrm{unconditional\ control\ of\ dangerous\ tail\ ratio\ and\ boundary\ flux},
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
\textbf{STOP-C20:
Continuous Layer-Distortion / Boundary-Flux Gap}.
}
$$

---

# 21. 24/72 Ledger — Round 16

| Step | object | $B$ | $U$ | $O$ | $L$ | status |
|---|---|---|---|---|---|---|
| C181 | superlevel sets $E_\lambda$ | $\mathsf C$ | level organization | relational | $\mathsf F$ | FORM |
| C182 | layer-cake $D,H$ | $\mathsf C$ | continuous integral | targeted | $\mathsf F$ | EXACT |
| C183 | distribution formula for $Q^3$ | $\mathsf C$ | continuous integral | scalar | $\mathsf F$ | EXACT |
| C184 | tail ratio $\theta$ | $\mathsf C$ | recognition | scalar profile | $\mathsf F$ | FORM |
| C185 | $\Xi_Q$ as weighted average | $\mathsf C$ | continuous profile | scalar | $\mathsf F$ | EXACT |
| C186 | continuous distortion witness | $\mathsf C$ | mean-value | targeted | $\mathsf F$ | PROVED |
| C187 | coarea surface densities | $\mathsf C$ | surface organization | $\mathsf X$ | $\mathsf F$ | EXACT a.e. |
| C188 | tail–surface ratio ODE | $\mathsf C$ | continuous $\lambda$ flow | scalar profile | $\mathsf F$ | EXACT |
| C189 | interlevel Sobolev constraint | $\mathsf C$ | continuous thresholds | targeted | $\mathsf F$ | PROVED |
| C190 | curvature layer-cake | $\mathsf C$ | continuous integral | relational | $\mathsf F$ | EXACT |
| C191 | dangerous-layer witness $\Gamma_Q$ | $\mathsf C$ | necessity | scalar profile | $\mathsf F$ | PROVED |
| C192 | cross-level danger condition | $\mathsf C$ | continuous two-threshold | targeted | $\mathsf F$ | PROVED |
| C193 | localized Hodge orthogonality | $\mathsf C$ | level surface | relational | $\mathsf F$ | EXACT |
| C194 | boundary flux $\mathcal B_Q$ | $\mathsf C$ | surface flux | $\mathsf X$ | $\mathsf F$ | FORM |
| C195 | localized Pythagorean | $\mathsf C$ | surface/global | relational | $\mathsf F$ | EXACT |
| C196 | unconditional boundary-flux control | $\mathsf C$ | level geometry | targeted | $\mathsf F$ | OPEN / STOP-C20 |

---

# 22. Continuous-versus-discrete status

本輪明確採用：

$$
\boxed{
\lambda\in(0,\infty)
}
$$

而不是：

$$
\lambda_j=2^j.
$$

所有 pigeonhole / localization statement都由 continuous integral與 essential supremum完成。

因此：

$$
\boxed{
T_{\mathsf C\to\mathsf D}
=
\text{NOT YET REACHED}.
}
\tag{22.1}
$$

甚至現在可以更精確地說：

> dyadic shell若未來出現，必須證明它提供 continuous $\lambda$ profile無法提供的 essential information；否則它只能算 convenience discretization。

---

# 23. Strongest results of Round 16

## R16-A — global-to-layer witness

$$
\boxed{
Q^3{}'>0
\Longrightarrow
\exists\lambda_\ast:
\xi_Q(\lambda_\ast)>c_0.
}
$$

## R16-B — dangerous growth layer

$$
\boxed{
Q^3{}'>0
\Longrightarrow
\exists\lambda_\ast:
\Gamma_Q(\lambda_\ast)>1.
}
$$

## R16-C — continuous tail-surface dynamics

$$
\boxed{
\theta'
=
\frac{a_\Sigma}{d}
(\theta-\sigma).
}
$$

## R16-D — localization cost

$$
\boxed{
E_M^u(\lambda)
=
D_M(\lambda)
+
H_M(\lambda)
-
2\mathcal B_Q(\lambda).
}
$$

所以 global orthogonality不是免費 localizable。

---

# 24. Next round — Level-Surface Flux Geometry

下一輪不再研究 global：

$$
\Xi_Q.
$$

直接研究：

$$
\boxed{
\mathcal B_Q(\lambda)
}
$$

以及：

$$
\boxed{
\sigma(\lambda).
}
$$

核心問題：

1. level-set normal：
   $$
   \nu_\lambda
   =
   -\frac{\nabla r}{|\nabla r|}
   $$
   是否把 boundary flux連到 amplitude-gradient geometry；

2. nonlinear gauge：
   $$
   \operatorname{div}(r^2n)=0
   $$
   對 level surface上的 normal/tangential decomposition有何 exact restriction；

3. $\mathcal B_Q$ 能否拆成 mean curvature、normal gauge Hessian、tangential derivative等 continuous surface invariants；

4. dangerous $\Gamma_Q>1$ 是否強迫 surface area / curvature / flux同時異常；

5. 若 level surfaces topology改變，也先用 continuous Morse/stratified description；只有真的需要 countable component enumeration時才考慮 $\mathsf D$。

---

# 25. External primary-source anchors

1. Tobias Barker, Wendong Wang, *Estimates of the singular set for the Navier-Stokes equations with supercritical assumptions on the pressure*, arXiv:2111.15444.
   - NS regularity analysis中使用 velocity-gradient weighted quantities
     $$
     |\nabla v|^2|v|^{q-2}
     $$
     的 primary-source背景；本輪 $D$ 的 $|v|$-weighted structure與之只作方法學比較。

2. Yanqing Wang, Wei Wei, Huan Yu, *$\varepsilon$-regularity criteria in Lorentz spaces to the 3D Navier-Stokes equations*, arXiv:1909.09957.
   - distribution-function/Lorentz critical regularity背景；本輪 continuous superlevel profile formulas為本文直接推導。

本文的 layer-cake identities、tail-ratio equation、dangerous-layer witness、cross-level inequality與 localized Hodge boundary-flux identity均為本文直接推導。

---

# 26. Commit state

$$
\boxed{
\begin{aligned}
\text{Route}
&=
\mathrm{Pure\ Continuous\ Layer\text{-}Cake/Superlevel},
\\
\text{Essential }\mathsf C\to\mathsf D
&=
\mathrm{Not\ reached},
\\
\text{Global distortion}
&=
\mathrm{continuous\ weighted\ average},
\\
\text{Positive growth}
&=
\mathrm{forces\ dangerous\ continuous\ layer},
\\
\text{Amplitude coordinate}
&=
\lambda\in(0,\infty),
\\
\text{Tail dynamics}
&=
\theta'=(a_\Sigma/d)(\theta-\sigma),
\\
\text{Interlevel constraint}
&=
(\mu-\lambda)^2V(\mu)^{1/3}\lesssim d(\lambda),
\\
\text{Localization cost}
&=
\mathcal B_Q(\lambda),
\\
\text{STOP-C20}
&=
\mathrm{Continuous\ Layer\text{-}Distortion/Boundary\text{-}Flux\ Gap},
\\
\text{Next}
&=
\mathrm{Level\text{-}Surface\ Flux\ Geometry}.
\end{aligned}
}
$$
