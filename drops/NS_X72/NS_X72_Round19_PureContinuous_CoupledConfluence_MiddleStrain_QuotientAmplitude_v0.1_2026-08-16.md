# NS × X 積分 × 24/72 範式實戰
## Round 19 — Pure Continuous Coupled Confluence / Middle-Strain–Quotient-Amplitude Route

- 日期：2026-08-16
- 版本：v0.1
- 狀態：Proof-Route Experiment / Two-Route Coupled Pure-C Branch
- canonical source：UTF-8 Markdown
- canonical math delimiters：inline `$...$`；display `$$...$$`
- 前一輪：`NS_X72_Round18_PureContinuous_WeightedStrainVorticity_ObstructionConfluence_v0.1_2026-08-16.md`
- 本輪目標：不再開新 representation。直接耦合兩條已匯流的 Pure-C 路線：
  1. critical quotient amplitude
     $$
     r=|v|;
     $$
  2. middle-strain / determinant / vortex-stretching geometry
     $$
     \lambda_2^+,\quad(-\det S)_+.
     $$
  建立兩者之間的 exact algebraic comparability、direction-independent floor、continuous confluence layers與 low-amplitude escape carrier。
- 非主張：本輪沒有排除 low-amplitude degeneracy channel；相反地，本輪將「middle-strain 可以和 quotient amplitude 空間分離」這件事形式化成新的 continuous sublevel obstruction。

---

# 0. 24/72 branch audit

目前整個 NS 實驗仍然是 24/72 framework。

但我們刻意只在 substrate axis 上死扣：

$$
\boxed{
B=\mathsf C.
}
$$

所以到 Round 19 為止，並不是「跑完 24/72 後發現只有連續」。

更精確是：

$$
\boxed{
\text{we are exhausting the Pure-C substrate slice before switching substrate}.
}
$$

在這個 slice 內，其他 axes 已經發生多次變化：

- update organization：
  $$
  \mathsf S,\quad
  \mathsf P,\quad
  \mathsf R,
  \quad
  \text{hybrid continuous routes};
  $$
- observation：
  $$
  \mathsf C
  \to
  \mathsf X
  \to
  \mathsf C_{\rm targeted}
  $$
  多次往返；
- transition law仍然：
  $$
  \boxed{
  L=\mathsf F.
  }
  $$

因此目前結果只表示：

$$
\boxed{
\textbf{
NS Pure-C proof search has not yet forced an essential discrete substrate.
}
}
$$

不表示一般世界、一般數學或完整 72 格只需要 continuous substrate。

---

# 1. Round 18 confluence core

Round 18 建立：

$$
Q(t)
=
\mathfrak Q_3[u(t)]
$$

與 weighted physical-gradient carrier：

$$
E_M
$$

之間的 bridge，並證明 potential critical quotient blow-up：

$$
Q(t)\to\infty
$$

會迫使：

$$
\int_0^{T_\ast}
\|\nabla\omega\|_2^2dt
=
\infty,
$$

進而迫使 cumulative vortex stretching：

$$
\int_0^{T_\ast}
\int
\omega^\top S\omega\,dxdt
=
+\infty.
$$

最後回到：

$$
\boxed{
\int_0^{T_\ast}
\int
\lambda_2^+
|S|^2dxdt
=
\infty.
}
$$

所以本輪直接耦合：

$$
r=|v|
$$

與：

$$
\lambda_2^+.
$$

---

# 2. Exact eigenvalue parametrization on the dangerous branch

令 strain eigenvalues：

$$
\lambda_1
\le
\lambda_2
\le
\lambda_3,
$$

且：

$$
\lambda_1+\lambda_2+\lambda_3=0.
$$

在 dangerous branch：

$$
\lambda_2>0.
$$

令：

$$
b=\lambda_2>0,
$$

以及：

$$
k
=
\frac{\lambda_3}{\lambda_2}
\ge1.
$$

則：

$$
\boxed{
\lambda_3=kb,
}
$$

以及：

$$
\boxed{
\lambda_1=-(1+k)b.
}
\tag{2.1}
$$

所以：

$$
\boxed{
|S|^2
=
2b^2
(1+k+k^2).
}
\tag{2.2}
$$

而：

$$
\boxed{
-\det S
=
b^3k(1+k).
}
\tag{2.3}
$$

---

# 3. Two-sided determinant–middle-eigenvalue equivalence

由 (2.2)–(2.3)：

$$
\frac{
-\det S
}{
b|S|^2
}
=
\frac{
k(1+k)
}{
2(1+k+k^2)
}.
$$

對：

$$
k\ge1,
$$

有：

$$
\boxed{
\frac13
\le
\frac{
k(1+k)
}{
2(1+k+k^2)
}
<
\frac12.
}
\tag{3.1}
$$

因此：

$$
\boxed{
\frac13
\lambda_2
|S|^2
\le
-\det S
\le
\frac12
\lambda_2
|S|^2
}
\tag{3.2}
$$

在：

$$
\lambda_2>0
$$

區域。

若：

$$
\lambda_2\le0,
$$

則：

$$
\det S\ge0
$$

而：

$$
(-\det S)_+=0.
$$

所以全域 pointwise：

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
\tag{3.3}
$$

命名：

$$
\boxed{
\textbf{Dangerous Determinant Equivalence}.
}
$$

Round 03 只需要了右側上界。

Round 19 補出左側，顯示 dangerous determinant 與 positive middle-eigenvalue density其實是 constant-factor equivalent。

---

# 4. Spectral eccentricity does not destroy the equivalence

parameter：

$$
k=\frac{\lambda_3}{\lambda_2}
$$

可以任意大。

但：

$$
\frac{
k(1+k)
}{
2(1+k+k^2)
}
$$

始終落在：

$$
\left[
\frac13,\frac12
\right).
$$

所以：

$$
\boxed{
\text{even extreme strain spectral eccentricity cannot separate }
(-\det S)_+
\text{ from }
\lambda_2^+|S|^2
\text{ by more than universal constants}.
}
$$

這表示 Round 03 obstruction core比原先使用單向 inequality時更 rigid。

---

# 5. Direction-Independent Middle-Eigenvalue Floor

在：

$$
\lambda_2=b>0,
$$

三個 eigenvalue absolute values為：

$$
|\lambda_1|
=
(1+k)b
\ge2b,
$$

$$
|\lambda_2|
=
b,
$$

$$
|\lambda_3|
=
kb
\ge b.
$$

所以 smallest singular value of $S$ 恰為：

$$
b.
$$

因此對任意 unit vector：

$$
n\in\mathbb S^2,
$$

都有：

$$
\boxed{
|Sn|
\ge
\lambda_2.
}
\tag{5.1}
$$

加 positive part可寫：

$$
\boxed{
\lambda_2^+
\le
|Sn|
}
\tag{5.2}
$$

對所有 unit $n$ 成立。

命名：

$$
\boxed{
\textbf{Direction-Independent Middle-Strain Floor}.
}
$$

---

# 6. Consequence for the optimal quotient direction

Round 14–18 的：

$$
n
=
\frac v{|v|}
$$

不是任意外加 direction。

它是 optimal critical quotient representative的方向。

但 (5.2) 對所有：

$$
n
$$

都成立。

所以：

$$
\boxed{
\textbf{
positive middle strain cannot be hidden by choosing a favorable optimal quotient direction.
}
}
\tag{6.1}
$$

這排除一個 potential escape：

> 也許 nonlinear gauge只要把 $n$ 選到 strain 的弱方向，就能躲開 $\lambda_2^+$。

在：

$$
\lambda_2>0
$$

時不存在比：

$$
\lambda_2
$$

更弱的 singular direction。

---

# 7. Weighted middle-strain floor

乘上：

$$
r=|v|\ge0,
$$

由 (5.2)：

$$
\boxed{
r(\lambda_2^+)^2
\le
r|Sn|^2
\le
r|S|^2.
}
\tag{7.1}
$$

積分：

$$
\boxed{
\int
r(\lambda_2^+)^2dx
\le
W_S
\le
E_M.
}
\tag{7.2}
$$

其中：

$$
W_S
=
\int
r|S|^2dx.
$$

所以 Round 17 physical weighted-gradient carrier必然看得到 positive middle eigenvalue的 weighted square。

---

# 8. Directional trichotomy

Round 18 定義：

$$
d_n
=
Sn
-
\frac12
\omega\times n.
$$

則：

$$
Sn
=
d_n
+
\frac12
\omega\times n.
$$

由：

$$
(\lambda_2^+)^2
\le
|Sn|^2
$$

及：

$$
|a+b|^2
\le
2|a|^2+2|b|^2,
$$

得到：

$$
\boxed{
(\lambda_2^+)^2
\le
2|d_n|^2
+
\frac12
|\omega\times n|^2.
}
\tag{8.1}
$$

所以 positive middle strain如果很大，至少必須出現在：

1. strain–rotation mismatch：
   $$
   |d_n|;
   $$
2. transverse vorticity：
   $$
   |\omega\times n|;
   $$

之一。

兩者都已經包含在：

$$
E_M.
$$

---

# 9. Define the confluence ratio

在：

$$
r>0
$$

定義：

$$
\boxed{
\chi_C
=
\frac{
\lambda_2^+
}{
r
}.
}
\tag{9.1}
$$

若：

$$
r=0
\quad\text{且}\quad
\lambda_2^+>0,
$$

定義：

$$
\chi_C=+\infty.
$$

若兩者皆為零，令：

$$
\chi_C=0.
$$

under NS scaling：

$$
r_\Lambda
=
\Lambda r,
$$

$$
(\lambda_2^+)_\Lambda
=
\Lambda^2\lambda_2^+,
$$

所以：

$$
\boxed{
(\chi_C)_\Lambda
=
\Lambda\chi_C.
}
\tag{9.2}
$$

因此：

$$
\chi_C
$$

是一個 inverse-length / critical-rate type variable。

---

# 10. Determinant production as a weighted expectation of $\chi_C$

在：

$$
\lambda_2>0
$$

region：

$$
(-\det S)_+
=
c(k)
\lambda_2^+
|S|^2
$$

其中：

$$
\boxed{
\frac13
\le
c(k)
<
\frac12.
}
$$

但：

$$
\lambda_2^+
|S|^2
=
\chi_C
\left(
r|S|^2
\right).
$$

所以：

$$
\boxed{
\frac13
\chi_C
r|S|^2
\le
(-\det S)_+
\le
\frac12
\chi_C
r|S|^2.
}
\tag{10.1}
$$

定義 positive-strain weighted measure：

$$
\boxed{
d\mu_C
=
\mathbf 1_{\{\lambda_2>0\}}
r|S|^2dx.
}
\tag{10.2}
$$

則：

$$
\boxed{
\frac13
\int
\chi_C\,d\mu_C
\le
\int
(-\det S)_+dx
\le
\frac12
\int
\chi_C\,d\mu_C.
}
\tag{10.3}
$$

這是兩條 proof route的 exact coupling formula。

---

# 11. Interpretation

Round 03 的 dangerous strain production：

$$
(-\det S)_+
$$

現在可解讀為：

$$
\boxed{
\text{critical weighted strain budget}
\times
\text{middle-strain / quotient-amplitude rate}.
}
$$

也就是：

$$
\boxed{
\text{production}
\sim
\chi_C
\,d\mu_C.
}
$$

所以 obstruction core不再只是：

$$
\lambda_2^+
$$

或：

$$
r.
$$

而是兩者的 relational ratio：

$$
\boxed{
\chi_C=\lambda_2^+/r.
}
$$

---

# 12. Continuous confluence layers

對：

$$
\eta\ge0,
$$

定義：

$$
\boxed{
\mathcal C_\eta
=
\{
x:
\chi_C(x)>\eta
\}.
}
\tag{12.1}
$$

layer-cake：

$$
\boxed{
\int
\chi_C\,d\mu_C
=
\int_0^\infty
\mu_C(\mathcal C_\eta)
\,d\eta.
}
\tag{12.2}
$$

所以 positive determinant production可由 continuous ratio-level field：

$$
\eta\in(0,\infty)
$$

表示。

這是另一個 continuous layer coordinate。

沒有 dyadic ratio bins。

---

# 13. Confluence-layer witness

令：

$$
P_+(t)
=
\int
(-\det S)_+dx.
$$

由 (10.3)：

$$
\int
\chi_C\,d\mu_C
\ge
2P_+.
$$

如果：

$$
\mu_C(\mathbb R^3)>0,
$$

定義 weighted mean confluence rate：

$$
\boxed{
\bar\chi_C
=
\frac{
\int
\chi_C\,d\mu_C
}{
\mu_C(\mathbb R^3)
}.
}
\tag{13.1}
$$

則：

$$
\boxed{
2
\frac{
P_+
}{
\mu_C(\mathbb R^3)
}
\le
\bar\chi_C
\le
3
\frac{
P_+
}{
\mu_C(\mathbb R^3)
}.
}
\tag{13.2}
$$

因此 production相對 weighted strain budget若變大，必然代表：

$$
\chi_C
$$

的 weighted mean變大。

---

# 14. Median confluence witness

由 layer-cake / Markov逆向平均值原理：

若：

$$
\bar\chi_C>0,
$$

則不能對 a.e. $\mu_C$ 有：

$$
\chi_C<
\frac12\bar\chi_C.
$$

更精確，必存在 positive $\mu_C$-measure set：

$$
\boxed{
\left\{
\chi_C
\ge
\frac12\bar\chi_C
\right\}
}
\tag{14.1}
$$

承擔非零 weighted strain mass。

因此 large production-to-budget ratio必須出現在實際 continuous ratio layers，而不能只由 measure-zero spike生成 weighted mean。

---

# 15. Low-amplitude escape carrier

confluence ratio：

$$
\chi_C
=
\frac{
\lambda_2^+
}{
r
}
$$

暴露一個新的 potential escape：

$$
r\downarrow0
$$

而：

$$
\lambda_2^+
$$

仍大。

為量化它，定義：

$$
\boxed{
\mathcal I_0
=
\int_{\{r>0\}}
\frac{
|S|^4
}{
r
}
dx,
}
\tag{15.1}
$$

並約定若在：

$$
r=0
$$

上：

$$
|S|>0
$$

具有 positive measure / nonintegrable trace，則：

$$
\mathcal I_0=+\infty.
$$

這是 inverse-amplitude strain carrier。

---

# 16. Overlap–degeneracy inequality

令：

$$
M_2
=
\int
\lambda_2^+
|S|^2dx.
$$

Cauchy–Schwarz：

$$
M_2
=
\int
\left(
\sqrt r\,\lambda_2^+
\right)
\left(
\frac{
|S|^2
}{
\sqrt r
}
\right)dx.
$$

所以：

$$
M_2^2
\le
\left(
\int
r(\lambda_2^+)^2dx
\right)
\mathcal I_0.
$$

由 (7.2)：

$$
\boxed{
M_2^2
\le
E_M
\mathcal I_0.
}
\tag{16.1}
$$

再由 Dangerous Determinant Equivalence：

$$
P_+
\le
\frac12M_2,
$$

所以：

$$
\boxed{
P_+^2
\le
\frac14
E_M
\mathcal I_0.
}
\tag{16.2}
$$

命名：

$$
\boxed{
\textbf{Overlap–Degeneracy Inequality}.
}
$$

---

# 17. Meaning of the overlap–degeneracy inequality

strong dangerous determinant production需要兩類資源的乘積：

$$
\boxed{
\text{high-amplitude weighted physical-gradient budget}
}
$$

與：

$$
\boxed{
\text{inverse-amplitude strain concentration}.
}
$$

若：

$$
E_M
$$

沒有相應放大，

則：

$$
\mathcal I_0
$$

必須放大。

所以 middle-strain activity如果想避開 quotient amplitude weight：

$$
r,
$$

它只能往：

$$
\boxed{
r\approx0
}
$$

的 degeneracy region逃。

---

# 18. Continuous sublevel representation of the inverse-amplitude escape

對：

$$
r>0,
$$

有：

$$
\boxed{
\frac1r
=
\int_r^\infty
\frac{
d\eta
}{
\eta^2
}.
}
\tag{18.1}
$$

因此 Tonelli：

$$
\boxed{
\mathcal I_0
=
\int_0^\infty
\frac1{\eta^2}
\left[
\int_{\{0<r<\eta\}}
|S|^4dx
\right]
d\eta.
}
\tag{18.2}
$$

所以 low-amplitude escape同樣可以完全用 continuous sublevel parameter：

$$
\eta\in(0,\infty)
$$

描述。

沒有必要先切成：

$$
2^{-j}.
$$

---

# 19. High-overlap versus low-amplitude escape

本輪因此形成兩個 coupled continuous channels。

## Channel O — overlap

dangerous middle strain與 nondegenerate quotient amplitude重疊：

$$
\boxed{
r(\lambda_2^+)^2
}
$$

由：

$$
E_M
$$

直接支付。

## Channel Z — zero-amplitude degeneracy

dangerous strain避開 weight：

$$
r
$$

並進入：

$$
r\approx0
$$

區域，

由：

$$
\boxed{
\mathcal I_0
=
\int
|S|^4/r
}
$$

記錄。

因此：

$$
\boxed{
\textbf{
Middle-strain danger cannot simply disappear from the quotient route:
it must appear as weighted overlap or low-amplitude degeneracy.
}
}
\tag{19.1}
$$

---

# 20. Why this still does not close NS

Round 17–18 已經知道 potential singularity可使：

$$
\int E_Mdt
=
\infty.
$$

所以 (16.2) 本身不會產生 contradiction。

同時：

$$
\mathcal I_0
$$

目前沒有 ordinary energy-level global bound。

所以新 coupling formula把逃逸路線縮窄，

但沒有排除：

$$
\boxed{
E_M\to\text{large}
}
$$

或：

$$
\boxed{
\mathcal I_0\to\text{large}.
}
$$

---

# 21. New representation-stable core

目前至少三種 continuous descriptions：

1. strain determinant：
   $$
   (-\det S)_+;
   $$
2. middle eigenvalue：
   $$
   \lambda_2^+|S|^2;
   $$
3. quotient-amplitude confluence：
   $$
   \chi_C\,r|S|^2;
   $$

在 dangerous branch上全部 constant-factor等價。

所以：

$$
\boxed{
\textbf{
the obstruction core is no longer tied to a single representation.
}
}
\tag{21.1}
$$

這是 Round 18 obstruction confluence的進一步 strengthening。

---

# 22. STOP-C23 — Confluence-Ratio / Low-Amplitude Degeneracy Gap

定義：

$$
\boxed{
\bot_X^{\mathrm{C23}}
=
\left\langle
\begin{array}{l}
\text{layer}
=
\mathrm{coupled\ quotient/strain\ confluence},
\\
\text{determinant}
\asymp
\lambda_2^+|S|^2,
\\
\text{directional\ escape}
=
\mathrm{impossible\ when\ }\lambda_2>0,
\\
\text{weighted\ floor}
=
\int r(\lambda_2^+)^2
\le
E_M,
\\
\text{confluence\ ratio}
=
\chi_C=\lambda_2^+/r,
\\
\text{production}
\asymp
\int\chi_C\,d\mu_C,
\\
\text{low-amplitude\ escape}
=
\mathcal I_0=\int|S|^4/r,
\\
\text{overlap–degeneracy}
=
P_+^2
\lesssim
E_M\mathcal I_0,
\\
\text{missing}
=
\mathrm{unconditional\ control\ of\ weighted\ overlap\ or\ inverse-amplitude\ sublevel\ escape},
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
\textbf{STOP-C23:
Confluence-Ratio / Low-Amplitude Degeneracy Gap}.
}
$$

---

# 23. 24/72 Ledger — Round 19

| Step | object | $B$ | $U$ | $O$ | $L$ | status |
|---|---|---|---|---|---|---|
| C228 | 24/72 slice audit | $\mathsf C$ fixed | mixed | mixed | $\mathsf F$ fixed | CLARIFIED |
| C229 | dangerous eigenvalue parametrization | $\mathsf C$ | algebraic | relational | $\mathsf F$ | EXACT |
| C230 | two-sided determinant equivalence | $\mathsf C$ | algebraic | targeted | $\mathsf F$ | PROVED |
| C231 | spectral eccentricity robustness | $\mathsf C$ | algebraic | targeted | $\mathsf F$ | PROVED |
| C232 | direction-independent middle-strain floor | $\mathsf C$ | geometry | relational | $\mathsf F$ | PROVED |
| C233 | weighted $\lambda_2^+$ square floor | $\mathsf C$ | quotient coupling | targeted | $\mathsf F$ | PROVED |
| C234 | directional trichotomy | $\mathsf C$ | strain/vorticity geometry | $\mathsf X$ | $\mathsf F$ | PROVED |
| C235 | confluence ratio $\chi_C$ | $\mathsf C$ | relational | scalar field | $\mathsf F$ | FORM |
| C236 | determinant as $\chi_C$-weighted measure | $\mathsf C$ | measure/geometry | targeted | $\mathsf F$ | EXACT |
| C237 | continuous confluence layers | $\mathsf C$ | layer-cake | profile | $\mathsf F$ | EXACT |
| C238 | inverse-amplitude carrier $\mathcal I_0$ | $\mathsf C$ | sublevel geometry | scalar | $\mathsf F$ | FORM |
| C239 | overlap–degeneracy inequality | $\mathsf C$ | Cauchy coupling | relational | $\mathsf F$ | PROVED |
| C240 | continuous sublevel resummation | $\mathsf C$ | layer-cake | profile | $\mathsf F$ | EXACT |
| C241 | unconditional confluence closure | $\mathsf C$ | coupled | targeted | $\mathsf F$ | OPEN / STOP-C23 |

---

# 24. Continuous-versus-discrete status

本輪新增兩種 layer variables：

$$
\eta
=
\chi_C\text{ threshold},
$$

以及：

$$
\eta
=
r\text{ sublevel threshold}.
$$

兩者都在：

$$
(0,\infty)
$$

continuous range。

所以：

$$
\boxed{
T_{\mathsf C\to\mathsf D}
=
\text{NOT YET REACHED}.
}
\tag{24.1}
$$

目前仍然沒有任何 proof step需要把 continuous layer改成 countable shell才成立。

---

# 25. Strongest results of Round 19

## R19-A — Dangerous Determinant Equivalence

$$
\boxed{
\frac13\lambda_2^+|S|^2
\le
(-\det S)_+
\le
\frac12\lambda_2^+|S|^2.
}
$$

## R19-B — No Directional Escape

$$
\boxed{
\lambda_2^+
\le
|Sn|
\quad
\forall n\in\mathbb S^2.
}
$$

## R19-C — Exact confluence carrier

$$
\boxed{
(-\det S)_+
\asymp
\frac{\lambda_2^+}{|v|}
\left(
|v||S|^2
\right).
}
$$

## R19-D — Overlap–Degeneracy Inequality

$$
\boxed{
P_+^2
\lesssim
E_M
\mathcal I_0.
}
$$

所以危險 middle-strain activity只能：

$$
\boxed{
\text{overlap with quotient amplitude}
\quad\vee\quad
\text{escape into low-amplitude degeneracy}.
}
$$

---

# 26. Next round — low-amplitude degeneracy geometry

雙路合擊後，真正還沒被解剖的是：

$$
\boxed{
r\approx0
}
$$

channel。

下一輪直接研究：

$$
\mathcal Z_\eta
=
\{0<|v|<\eta\}.
$$

核心問題：

1. $v$ 是 unique $L^3$ quotient minimizer；
2. gauge：
   $$
   \operatorname{div}(|v|v)=0;
   $$
3. 若 $|v|$ 很小但 $|S_u|$ 很大，因：
   $$
   \nabla u
   =
   \nabla v-\nabla^2q,
   $$
   大 strain必須由：
   $$
   \nabla v
   $$
   或：
   $$
   \nabla^2q
   $$
   承擔；
4. 檢查這是否會迫使 Round 15 的 gauge-Hessian distortion：
   $$
   H
   $$
   或 Round 17 surface dissipation增大；
5. 若 $v=0$ set形成退化 strata，先使用 continuous zero-set / tubular-neighborhood geometry；
6. 只有若零集結構真的需要 countable atom/component enumeration才能閉合，才考慮：
   $$
   \mathsf C\to\mathsf D.
   $$

---

# 27. External primary-source anchors

1. Evan Miller, *A regularity criterion for the Navier-Stokes equation involving only the middle eigenvalue of the strain tensor*, arXiv:1710.05569.
   - middle eigenvalue of strain作為 scale-critical blow-up/regularity channel的 primary-source背景。

2. Evan Miller, *On the interaction of strain and vorticity for solutions of the Navier--Stokes equation*, arXiv:2407.02691.
   - strain–vorticity interaction與
     $$
     \langle S,\omega\otimes\omega\rangle
     =
     -4\int\det S
     $$
     的 primary-source背景。

本輪 two-sided determinant equivalence、direction-independent floor、confluence ratio與 overlap–degeneracy inequality均為本文直接推導。

---

# 28. Commit state

$$
\boxed{
\begin{aligned}
\text{Route}
&=
\mathrm{Pure\ Continuous\ Coupled\ Confluence},
\\
\text{24/72 status}
&=
\mathrm{Pure\text{-}C\ substrate\ slice,\ not\ full\ grid},
\\
\text{Essential }\mathsf C\to\mathsf D
&=
\mathrm{Not\ reached},
\\
\text{Dangerous determinant}
&\asymp
\lambda_2^+|S|^2,
\\
\text{Directional escape}
&=
\mathrm{ruled\ out},
\\
\text{Confluence ratio}
&=
\chi_C=\lambda_2^+/|v|,
\\
\text{Overlap carrier}
&=
E_M,
\\
\text{Degenerate escape carrier}
&=
\mathcal I_0,
\\
\text{STOP-C23}
&=
\mathrm{Confluence\text{-}Ratio/Low\text{-}Amplitude\ Degeneracy\ Gap},
\\
\text{Next}
&=
\mathrm{Low\text{-}Amplitude\ Degeneracy\ Geometry}.
\end{aligned}
}
$$
