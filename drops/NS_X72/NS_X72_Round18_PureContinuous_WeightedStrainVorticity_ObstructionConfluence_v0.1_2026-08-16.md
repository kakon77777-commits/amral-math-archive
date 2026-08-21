# NS × X 積分 × 24/72 範式實戰
## Round 18 — Pure Continuous Weighted Strain–Vorticity Return / Obstruction-Confluence Route

- 日期：2026-08-16
- 版本：v0.1
- 狀態：Proof-Route Experiment / Continuous-Only Weighted Relational Return Branch
- canonical source：UTF-8 Markdown
- canonical math delimiters：inline `$...$`；display `$$...$$`
- 前一輪：`NS_X72_Round17_PureContinuous_LevelSurface_HodgeCoherence_v0.1_2026-08-16.md`
- 本輪目標：把 Round 17 的 critical weighted physical-gradient carrier
  $$
  E_M
  $$
  精確拆回 strain、vorticity、optimal quotient direction與 directional mismatch，並檢驗這條長距離 quotient/Hodge 路線是否重新匯流到 Round 03 的 vortex-stretching / middle-strain obstruction。
- 非主張：本輪沒有證明 middle-eigenvalue obstruction必然可被排除；本輪的主要成果是建立 exact carrier decomposition與一條 singularity-obstruction confluence chain。

---

# 0. Round 17 handoff

令：

$$
Q(t)
=
\mathfrak Q_3[u(t)],
$$

並令 optimal representative：

$$
v
=
u+\nabla q,
$$

$$
r
=
|v|,
$$

$$
n
=
\frac v{|v|}
$$

於：

$$
r>0.
$$

Round 17 定義 physical weighted-gradient carrier：

$$
\boxed{
E_M
=
\int_{\mathbb R^3}
r
\left[
|\nabla u|^2
+
|(\nabla u)^\top n|^2
\right]dx.
}
\tag{0.1}
$$

並證明：

$$
\boxed{
\frac d{dt}Q^2
\le
C E_M.
}
\tag{0.2}
$$

所以：

$$
\boxed{
\int_0^{T_\ast}
E_M(t)dt
<
\infty
}
\tag{0.3}
$$

足以保持：

$$
Q(t)
$$

有界。

Round 17 STOP：

$$
\boxed{
\text{STOP-C21}
=
\text{Level Hodge-Coherence / Critical Weighted-Gradient Gap}.
}
$$

---

# 1. Velocity-gradient decomposition

令：

$$
A
=
\nabla u
=
S+\Omega,
$$

其中：

$$
S^\top=S,
$$

$$
\Omega^\top=-\Omega.
$$

在三維：

$$
\boxed{
\Omega n
=
\frac12
\omega\times n.
}
\tag{1.1}
$$

且：

$$
\boxed{
|\Omega|^2
=
\frac12|\omega|^2.
}
\tag{1.2}
$$

因此：

$$
\boxed{
|\nabla u|^2
=
|S|^2
+
\frac12|\omega|^2.
}
\tag{1.3}
$$

---

# 2. Directional covector channel

因：

$$
A^\top
=
S-\Omega,
$$

有：

$$
\boxed{
A^\top n
=
Sn
-
\frac12
\omega\times n.
}
\tag{2.1}
$$

所以 Round 17 carrier變成：

$$
\boxed{
E_M
=
\int
r
\left[
|S|^2
+
\frac12|\omega|^2
+
\left|
Sn-\frac12\omega\times n
\right|^2
\right]dx.
}
\tag{2.2}
$$

這是本輪第一個核心 exact identity。

---

# 3. Longitudinal–tangential strain decomposition

令：

$$
s_n
=
n^\top Sn,
$$

以及：

$$
t_n
=
(I-n\otimes n)Sn.
$$

則：

$$
Sn
=
s_n n+t_n.
$$

而：

$$
\omega\times n
$$

與：

$$
n
$$

正交。

因此：

$$
\boxed{
\left|
Sn-\frac12\omega\times n
\right|^2
=
s_n^2
+
\left|
t_n-\frac12\omega\times n
\right|^2.
}
\tag{3.1}
$$

所以：

$$
\boxed{
\begin{aligned}
E_M
=
\int
r
\Bigg[
&
|S|^2
+
\frac12|\omega|^2
+
s_n^2
\\
&
+
\left|
t_n-\frac12\omega\times n
\right|^2
\Bigg]dx.
\end{aligned}
}
\tag{3.2}
$$

這把 carrier拆成四個非負 channels：

1. weighted strain amplitude；
2. weighted vorticity amplitude；
3. normal strain；
4. tangential strain–rotation mismatch。

---

# 4. Base weighted strain–vorticity carrier

定義：

$$
\boxed{
W_{SV}
=
\int
r
\left[
|S|^2
+
\frac12|\omega|^2
\right]dx.
}
\tag{4.1}
$$

由：

$$
|\nabla u|^2
=
|S|^2+\frac12|\omega|^2,
$$

亦可寫：

$$
\boxed{
W_{SV}
=
\int
r|\nabla u|^2dx.
}
\tag{4.2}
$$

因 directional term非負：

$$
\boxed{
W_{SV}
\le
E_M.
}
\tag{4.3}
$$

又：

$$
|A^\top n|^2
\le
|A|^2,
$$

所以：

$$
\boxed{
E_M
\le
2W_{SV}.
}
\tag{4.4}
$$

因此：

$$
\boxed{
W_{SV}
\le
E_M
\le
2W_{SV}.
}
\tag{4.5}
$$

命名：

$$
\boxed{
\textbf{Weighted Strain–Vorticity Equivalence}.
}
$$

---

# 5. Consequence — directional alignment is not the whole budget

即使達到 perfect directional matching：

$$
\boxed{
s_n=0,
}
$$

以及：

$$
\boxed{
t_n
=
\frac12\omega\times n,
}
$$

使：

$$
A^\top n=0,
$$

仍然有：

$$
\boxed{
E_M=W_{SV}.
}
$$

所以：

$$
\boxed{
\textbf{
no directional alignment can cancel the positive base weighted strain–vorticity energy.
}
}
$$

這和 vortex-stretching sign cancellation不同。

對 Round 17 budget而言，alignment只能消除額外方向 penalty，不能消除 base carrier。

---

# 6. Gauge representation of the directional term

由：

$$
v
=
u+\nabla q
=
rn,
$$

有：

$$
(\nabla v)^\top n
=
\nabla r.
$$

又：

$$
\nabla u
=
\nabla v-\nabla^2q.
$$

所以：

$$
\boxed{
(\nabla u)^\top n
=
\nabla r
-
\nabla^2q\,n.
}
\tag{6.1}
$$

因此：

$$
\boxed{
E_M
=
W_{SV}
+
\int
r
\left|
\nabla r-\nabla^2q\,n
\right|^2dx.
}
\tag{6.2}
$$

所以 Round 17 的 directional channel同時有兩個等價 interpretation：

$$
\boxed{
\text{strain–vorticity mismatch}
}
$$

與：

$$
\boxed{
\text{amplitude-gradient / gauge-curvature mismatch}.
}
$$

---

# 7. Connection to Round 15 Pythagorean geometry

Round 15 已有：

$$
\boxed{
E_M
=
D+H,
}
\tag{7.1}
$$

其中：

$$
D
=
\mathfrak D_3(v),
$$

$$
H
=
\mathcal H_Q.
$$

結合 (6.2)：

$$
\boxed{
D+H
=
W_{SV}
+
C_{\rm dir},
}
\tag{7.2}
$$

其中：

$$
\boxed{
C_{\rm dir}
=
\int
r
\left|
\nabla r-\nabla^2q\,n
\right|^2dx.
}
\tag{7.3}
$$

由 (4.5)：

$$
\boxed{
0
\le
C_{\rm dir}
\le
W_{SV}.
}
\tag{7.4}
$$

所以 nonlinear-Hodge distortion、quotient dissipation與 physical strain-vorticity geometry不是三個獨立世界。

它們滿足一個 exact bridge。

---

# 8. Weighted strain and weighted vorticity channels

定義：

$$
\boxed{
W_S
=
\int
r|S|^2dx,
}
\tag{8.1}
$$

以及：

$$
\boxed{
W_\omega
=
\frac12
\int
r|\omega|^2dx.
}
\tag{8.2}
$$

則：

$$
\boxed{
W_{SV}
=
W_S+W_\omega.
}
\tag{8.3}
$$

因此：

$$
\boxed{
\int_0^{T_\ast}
E_Mdt
=
\infty
}
$$

必須至少伴隨：

$$
\boxed{
\int_0^{T_\ast}
W_Sdt
=
\infty
}
$$

或：

$$
\boxed{
\int_0^{T_\ast}
W_\omega dt
=
\infty,
}
$$

或兩者共同 diverge。

這是 weighted relational二分。

---

# 9. Hölder reduction to the unweighted critical gradient norm

因：

$$
\|r\|_3
=
Q,
$$

Hölder：

$$
W_{SV}
=
\int
r|\nabla u|^2dx
\le
Q
\|\nabla u\|_3^2.
$$

由 (4.4)：

$$
\boxed{
E_M
\le
2Q
\|\nabla u\|_3^2.
}
\tag{9.1}
$$

所以 Round 17 differential inequality：

$$
(Q^2)'
\le
C E_M
$$

給：

$$
2QQ'
\le
C
Q
\|\nabla u\|_3^2.
$$

對非平凡：

$$
Q>0
$$

branch：

$$
\boxed{
Q'
\le
C
\|\nabla u\|_3^2.
}
\tag{9.2}
$$

因此：

$$
\boxed{
Q(T)
\le
Q(0)
+
C
\int_0^T
\|\nabla u(t)\|_3^2dt.
}
\tag{9.3}
$$

這是一個 scale-critical unweighted bridge。

---

# 10. Vorticity reduction

在 whole-space divergence-free setting，Riesz-transform / Biot–Savart boundedness給：

$$
\boxed{
\|\nabla u\|_3
\le
C
\|\omega\|_3.
}
\tag{10.1}
$$

所以：

$$
\boxed{
Q'
\le
C
\|\omega\|_3^2.
}
\tag{10.2}
$$

再由 interpolation：

$$
\|\omega\|_3
\le
\|\omega\|_2^{1/2}
\|\omega\|_6^{1/2},
$$

及 Sobolev：

$$
\|\omega\|_6
\le
C
\|\nabla\omega\|_2,
$$

得到：

$$
\boxed{
Q'
\le
C
\|\omega\|_2
\|\nabla\omega\|_2.
}
\tag{10.3}
$$

---

# 11. Energy–enstrophy-dissipation bridge

積分 (10.3)：

$$
Q(T)
\le
Q(0)
+
C
\int_0^T
\|\omega\|_2
\|\nabla\omega\|_2dt.
$$

Cauchy：

$$
\boxed{
Q(T)
\le
Q(0)
+
C
\left(
\int_0^T
\|\omega\|_2^2dt
\right)^{1/2}
\left(
\int_0^T
\|\nabla\omega\|_2^2dt
\right)^{1/2}.
}
\tag{11.1}
$$

energy inequality：

$$
\frac12
\|u(T)\|_2^2
+
\nu
\int_0^T
\|\nabla u\|_2^2dt
\le
\frac12
\|u_0\|_2^2.
$$

而 divergence-free whole-space：

$$
\|\nabla u\|_2
=
\|\omega\|_2.
$$

因此：

$$
\boxed{
\int_0^T
\|\omega\|_2^2dt
\le
\frac{
\|u_0\|_2^2
}{
2\nu
}.
}
\tag{11.2}
$$

代回：

$$
\boxed{
Q(T)
\le
Q(0)
+
C
\frac{
\|u_0\|_2
}{
\sqrt{\nu}
}
\left(
\int_0^T
\|\nabla\omega\|_2^2dt
\right)^{1/2}.
}
\tag{11.3}
$$

常數吸收數值因子。

---

# 12. Enstrophy-dissipation necessity

由 (11.3)：

若存在 finite maximal time：

$$
T_\ast<\infty
$$

且：

$$
Q(t)\to\infty
$$

沿：

$$
t\uparrow T_\ast,
$$

則必有：

$$
\boxed{
\int_0^{T_\ast}
\|\nabla\omega(t)\|_2^2dt
=
\infty.
}
\tag{12.1}
$$

命名：

$$
\boxed{
\textbf{Critical Quotient-to-Enstrophy-Dissipation Necessity}.
}
$$

所以 Round 17 weighted-gradient obstruction可被推回一個純 strain/vorticity derivative obstruction。

---

# 13. Return to the enstrophy identity

vorticity enstrophy：

$$
Y
=
\|\omega\|_2^2.
$$

exact equation：

$$
\boxed{
\frac12Y'
+
\nu
\|\nabla\omega\|_2^2
=
N(t),
}
\tag{13.1}
$$

其中：

$$
\boxed{
N(t)
=
\int
\omega^\top S\omega\,dx.
}
\tag{13.2}
$$

積分：

$$
\boxed{
\int_0^T
N(t)dt
=
\frac12
\left[
Y(T)-Y(0)
\right]
+
\nu
\int_0^T
\|\nabla\omega\|_2^2dt.
}
\tag{13.3}
$$

所以若 (12.1) 發生：

$$
\boxed{
\int_0^{T_\ast}
N(t)dt
=
+\infty.
}
\tag{13.4}
$$

也就是 finite-time critical quotient blow-up必須伴隨 infinite cumulative vortex-stretching production。

---

# 14. Return to the strain determinant

對 smooth divergence-free field，有 global identity：

$$
\boxed{
\int
\omega^\top S\omega\,dx
=
-4
\int
\det S\,dx.
}
\tag{14.1}
$$

因此：

$$
\boxed{
\int_0^{T_\ast}
\left[
-4
\int
\det S\,dx
\right]dt
=
+\infty.
}
\tag{14.2}
$$

所以 Round 18 的 long quotient route已重新回到 Round 03 的 strain-spectrum nonlinear production。

---

# 15. Return to the middle eigenvalue channel

Round 03 已證 pointwise algebraic inequality：

$$
\boxed{
-\det S
\le
\frac12
\lambda_2^+
|S|^2.
}
\tag{15.1}
$$

因此：

$$
N(t)
=
-4
\int
\det Sdx
\le
2
\int
\lambda_2^+
|S|^2dx.
$$

由 (13.4)：

$$
\boxed{
\int_0^{T_\ast}
\int
\lambda_2^+
|S|^2
dxdt
=
\infty.
}
\tag{15.2}
$$

所以：

$$
\boxed{
\textbf{
critical quotient blow-up forces infinite cumulative activity
in the positive middle-strain channel.
}
}
$$

---

# 16. Obstruction Confluence Chain

把 Sections 12–15 串起來：

$$
\boxed{
\begin{aligned}
Q(t)\to\infty
&\Longrightarrow
\int_0^{T_\ast}
\|\nabla\omega\|_2^2dt
=
\infty
\\
&\Longrightarrow
\int_0^{T_\ast}
\int
\omega^\top S\omega
\,dxdt
=
+\infty
\\
&\Longrightarrow
\int_0^{T_\ast}
\int
(-\det S)
\,dxdt
=
+\infty
\\
&\Longrightarrow
\int_0^{T_\ast}
\int
\lambda_2^+
|S|^2
\,dxdt
=
\infty.
\end{aligned}
}
\tag{16.1}
$$

命名：

$$
\boxed{
\textbf{Pure-Continuous Obstruction Confluence Chain}.
}
$$

這是本輪最重要的 proof-route result。

---

# 17. Why this confluence matters

Round 03 走的是：

$$
\boxed{
\text{strain/vorticity geometry}
}
$$

Round 12–17 走的是：

$$
\boxed{
\text{critical dual}
\to
\text{quotient}
\to
\text{one-form}
\to
p\text{-Hodge}
\to
\text{level surfaces}
}
$$

兩條路在 Round 18 重新匯流到：

$$
\boxed{
\lambda_2^+
\text{ / vortex stretching}
}
$$

所以目前至少兩個非常不同的 Pure-C proof architectures指向同一 geometric obstruction。

這不能被解讀成：

$$
\boxed{
\text{obstruction 已證不可突破}.
}
$$

但它表示：

$$
\boxed{
\textbf{
the remaining difficulty is becoming representation-stable
across distinct continuous reformulations.
}
}
\tag{17.1}
$$

這是一個重要 proof-map signal。

---

# 18. A base-floor no-go for directional-only repair

由：

$$
E_M
\ge
W_{SV}
=
\int
r
\left(
|S|^2+\frac12|\omega|^2
\right)dx,
$$

任何只試圖控制：

$$
n
$$

的方向 alignment，而不控制 weighted strain/vorticity amplitude，都不能單獨使：

$$
E_M
$$

integrable。

因此：

$$
\boxed{
\textbf{
pure directional optimization is insufficient for the Round 17 budget.
}
}
\tag{18.1}
$$

它必須與：

$$
r
$$

和：

$$
|S|,\ |\omega|
$$

的 amplitude correlation共同處理。

---

# 19. Critical amplitude–gradient carrier

定義：

$$
\boxed{
\mathfrak A_{SV}
=
\int
r
\left(
|S|^2+\frac12|\omega|^2
\right)dx.
}
\tag{19.1}
$$

它在 NS scaling下：

$$
\mathfrak A_{SV}
\mapsto
\lambda^2
\mathfrak A_{SV}.
$$

所以：

$$
\boxed{
\int
\mathfrak A_{SV}(t)dt
}
\tag{19.2}
$$

為 scale-invariant spacetime budget。

由 (4.5)：

$$
\boxed{
\int E_Mdt<\infty
\Longleftrightarrow
\int\mathfrak A_{SV}dt<\infty
}
\tag{19.3}
$$

至 universal constants。

所以 Round 17 weighted-gradient criterion可以完全改寫成 weighted strain–vorticity budget criterion。

---

# 20. What ordinary energy still fails to control

ordinary energy控制：

$$
\int
|\omega|^2
dxdt.
$$

但本輪需要：

$$
\int
r|\omega|^2
dxdt
$$

及：

$$
\int
r|S|^2
dxdt.
$$

多出的：

$$
\boxed{
r=|v|
}
$$

正是 critical quotient amplitude。

因此真正缺口可以描述為：

$$
\boxed{
\text{energy-level enstrophy}
\to
\text{critical amplitude-weighted enstrophy}.
}
$$

這是比單純「缺一階導數」更 relational 的說法。

---

# 21. STOP-C22 — Weighted Enstrophy / Vortex-Stretching Return Gap

定義：

$$
\boxed{
\bot_X^{\mathrm{C22}}
=
\left\langle
\begin{array}{l}
\text{layer}
=
\mathrm{weighted\ strain\text{-}vorticity\ return},
\\
\text{critical\ weighted\ carrier}
=
\mathfrak A_{SV},
\\
\text{Round17\ carrier}
=
E_M
\simeq
\mathfrak A_{SV},
\\
\text{directional\ mismatch}
=
\mathrm{nonnegative\ and\ nonessential\ for\ budget\ equivalence},
\\
\text{critical\ quotient\ blowup}
\Rightarrow
\int
\|\nabla\omega\|_2^2
=
\infty,
\\
\text{therefore}
\Rightarrow
\text{infinite cumulative vortex stretching},
\\
\text{therefore}
\Rightarrow
\text{infinite positive middle-strain activity},
\\
\text{missing}
=
\mathrm{unconditional\ suppression\ of\ this\ confluence\ channel},
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
\textbf{STOP-C22:
Weighted Enstrophy / Vortex-Stretching Return Gap}.
}
$$

---

# 22. 24/72 Ledger — Round 18

| Step | object | $B$ | $U$ | $O$ | $L$ | status |
|---|---|---|---|---|---|---|
| C214 | $E_M$ strain-vorticity decomposition | $\mathsf C$ | relational | $\mathsf X$ | $\mathsf F$ | EXACT |
| C215 | longitudinal/tangential split | $\mathsf C$ | geometry | relational | $\mathsf F$ | EXACT |
| C216 | base carrier $W_{SV}$ | $\mathsf C$ | recognition | targeted | $\mathsf F$ | FORM |
| C217 | $W_{SV}\le E_M\le2W_{SV}$ | $\mathsf C$ | comparison | scalar | $\mathsf F$ | PROVED |
| C218 | gauge representation of directional square | $\mathsf C$ | quotient/gauge | relational | $\mathsf F$ | EXACT |
| C219 | Hodge–strain bridge $D+H=W_{SV}+C_{\rm dir}$ | $\mathsf C$ | relational | $\mathsf X$ | $\mathsf F$ | EXACT |
| C220 | $E_M\le2Q\|\nabla u\|_3^2$ | $\mathsf C$ | Hölder | scalar | $\mathsf F$ | PROVED |
| C221 | $Q'\lesssim\|\nabla u\|_3^2$ | $\mathsf C$ | differential | scalar | $\mathsf F$ | PROVED |
| C222 | vorticity interpolation bridge | $\mathsf C$ | Sobolev | scalar | $\mathsf F$ | PROVED |
| C223 | $Q$ blowup $\Rightarrow\int\|\nabla\omega\|_2^2=\infty$ | $\mathsf C$ | necessity | scalar | $\mathsf F$ | PROVED |
| C224 | enstrophy production divergence | $\mathsf C$ | exact identity | relational | $\mathsf F$ | PROVED |
| C225 | determinant return | $\mathsf C$ | strain identity | relational | $\mathsf F$ | PROVED |
| C226 | middle-eigenvalue return | $\mathsf C$ | algebraic geometry | targeted | $\mathsf F$ | PROVED |
| C227 | unconditional suppression of confluence channel | $\mathsf C$ | — | targeted | $\mathsf F$ | OPEN / STOP-C22 |

---

# 23. Continuous-versus-discrete status

本輪是一次「長距離回到舊 obstruction」，

但所有連接都使用：

- continuous weighted integrals；
- continuous quotient representatives；
- continuous strain/vorticity fields；
- continuous Sobolev interpolation；
- continuous spacetime budgets。

沒有：

- dyadic scales；
- atoms；
- packet families；
- profile subsequences；
- discrete mode closure。

因此：

$$
\boxed{
T_{\mathsf C\to\mathsf D}
=
\text{NOT YET REACHED}.
}
\tag{23.1}
$$

---

# 24. Pure-C path now forms a loop

目前 proof map不再只是線。

它開始形成 loop：

$$
\boxed{
\begin{aligned}
\text{Round 03: strain/vorticity}
&\to
\cdots
\\
&\to
\text{Round 14--17: quotient/Hodge/layers}
\\
&\to
\text{Round 18: weighted strain/vorticity}
\\
&\to
\text{Round 03 obstruction core}.
\end{aligned}
}
\tag{24.1}
$$

但這不是論證循環。

因中間獲得了新的 necessary structures：

- quotient gauge；
- gauge curvature；
- gauge-Hessian distortion；
- continuous dangerous layers；
- Hodge coherence；
- critical weighted-gradient budget。

這是一個：

$$
\boxed{
\textbf{obstruction confluence loop}.
}
$$

---

# 25. Next round — Confluence attack

下一輪不應再開一個完全不同 representation。

既然兩條長路已匯流，

直接攻 confluence core。

候選主問題：

$$
\boxed{
\textbf{
Can simultaneous largeness of
critical quotient amplitude and middle-strain/vortex-stretching activity
force an additional incompatibility?
}
}
$$

具體：

1. 同時保留：
   $$
   Q,
   \quad
   W_{SV},
   \quad
   \lambda_2^+,
   \quad
   N=\int\omega^\top S\omega;
   $$

2. 檢查 optimal quotient gauge
   $$
   \operatorname{div}(|v|v)=0
   $$
   是否限制：
   $$
   \lambda_2^+
   $$
   在高 $r$ region 的排列；

3. 使用 continuous superlevels：
   $$
   E_\lambda=\{r>\lambda\}
   $$
   研究 weighted middle-strain activity：
   $$
   \int_{E_\lambda}
   \lambda_2^+
   |S|^2;
   $$

4. 檢查若 vortex stretching與 quotient amplitude同時集中，是否必須支付 Round 17 的 level-surface dissipation；

5. 這將是第一個真正的：
   $$
   \boxed{
   \text{two-route coupled attack}
   }
   $$
   而不是再造新表示。

---

# 26. External primary-source anchors

1. Evan Miller, *On the interaction of strain and vorticity for solutions of the Navier--Stokes equation*, arXiv:2407.02691.
   - strain–vorticity interaction；
   - global identity
     $$
     \langle S,\omega\otimes\omega\rangle
     =
     -4\int\det S;
     $$
   - nonlinear depletion analysis.

2. Alexis Vasseur, *Regularity criterion for 3D Navier-Stokes equations in terms of the direction of the velocity*, arXiv:0705.2446.
   - direction geometry與 regularity criterion；
   - 本輪 optimal quotient direction $n$ 不是直接等同於 $u/|u|$，只作外部 geometric-context anchor.

3. Hui Chen, Daoyuan Fang, Ting Zhang, *Critical regularity criteria for Navier-Stokes equations in terms of one directional derivative of the velocity*, arXiv:2007.10888.
   - critical gradient regularity criteria background；
   - 本輪 $\int\|\nabla u\|_3^2dt$ bridge與之只作方法學比較。

本輪 $E_M$ decomposition、weighted carrier equivalence、quotient-to-enstrophy-dissipation chain與 obstruction-confluence chain均為本文直接推導。

---

# 27. Commit state

$$
\boxed{
\begin{aligned}
\text{Route}
&=
\mathrm{Pure\ Continuous\ Weighted\ Strain\text{-}Vorticity\ Return},
\\
\text{Essential }\mathsf C\to\mathsf D
&=
\mathrm{Not\ reached},
\\
\text{Round17 carrier}
&=
E_M,
\\
\text{Equivalent base carrier}
&=
W_{SV},
\\
\text{Directional mismatch}
&=
\mathrm{nonnegative},
\\
\text{Critical quotient blowup}
&\Rightarrow
\mathrm{enstrophy\text{-}dissipation\ divergence},
\\
&\Rightarrow
\mathrm{vortex\text{-}stretching\ divergence},
\\
&\Rightarrow
\mathrm{middle\text{-}strain\ activity\ divergence},
\\
\text{Proof-map structure}
&=
\mathrm{obstruction\ confluence\ loop},
\\
\text{STOP-C22}
&=
\mathrm{Weighted\ Enstrophy/Vortex\text{-}Stretching\ Return\ Gap},
\\
\text{Next}
&=
\mathrm{Coupled\ Confluence\ Attack}.
\end{aligned}
}
$$
