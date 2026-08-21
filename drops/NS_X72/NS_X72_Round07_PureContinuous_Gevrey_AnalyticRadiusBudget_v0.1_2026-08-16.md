# NS × X 積分 × 24/72 範式實戰
## Round 07 — Pure Continuous Gevrey Resummation / Analytic-Radius Budget Route

- 日期：2026-08-16
- 版本：v0.1
- 狀態：Proof-Route Experiment / Continuous-Only Gevrey Resummation Branch
- canonical source：UTF-8 Markdown
- canonical math delimiters：inline `$...$`；display `$$...$$`
- 前一輪：`NS_X72_Round06_PureContinuous_ContinuousHierarchy_SpectralCovariance_v0.1_2026-08-16.md`
- 本輪目標：將 Round 06 的實數 Sobolev hierarchy 一次重新積成 Gevrey / analytic generating carrier，判定「無限導數階層」是否真的是 Pure-C 的不可閉合 obstruction；並建立一個 adaptive analytic-radius budget，將可能的 singular escape 壓成單一連續半徑消耗問題。
- 非主張：本文沒有完成三維 Navier–Stokes global regularity。本文建立的是 continuous hierarchy resummation 與 analytic-radius budget reduction。

---

# 0. Round 06 handoff

Round 06 對任意實數：

$$
s\ge0
$$

建立：

$$
M_s
=
\|\Lambda^sS\|_2^2,
$$

$$
\alpha_s
=
\frac{
T_s
}{
\nu M_{s+1}
},
$$

$$
\kappa_s
=
\frac{
M_{s+1}
}{
M_s
},
$$

並得到 exact hierarchy law：

$$
\boxed{
\kappa_s'
=
2\nu\kappa_s
\left[
(\alpha_{s+1}-\alpha_s)\kappa_s
+
(\alpha_{s+1}-1)
(\kappa_{s+1}-\kappa_s)
\right].
}
\tag{0.1}
$$

Fourier probability measure：

$$
d\mu_s(\xi)
=
\frac{
|\xi|^{2s}
|\widehat S(\xi)|^2
}{
M_s
}
d\xi
$$

給出：

$$
\kappa_s
=
\mathbb E_{\mu_s}
|\xi|^2,
$$

以及：

$$
V_s
=
\operatorname{Var}_{\mu_s}
(|\xi|^2).
$$

並得到 continuous spectral-covariance law：

$$
\boxed{
\kappa_s'
=
2\kappa_s
(g_{s+1}-g_s)
-
2\nu V_s.
}
\tag{0.2}
$$

Round 06 的 STOP：

$$
\boxed{
\text{STOP-C10}
=
\text{Continuous Hierarchy-Slope / Spectral-Covariance Gap}.
}
$$

但當時仍未回答：

> 無限 hierarchy 本身能否被一個 continuous generating carrier 一次壓縮？

本輪直接回答此問題。

---

# 1. Projected strain seed

在 smooth rapidly decaying whole-space class，使用：

$$
\Lambda
=
(-\Delta)^{1/2}.
$$

projected strain equation：

$$
\boxed{
\partial_tS
+
\nu\Lambda^2S
=
F,
}
\tag{1.1}
$$

其中：

$$
F
=
\frac12
P_{st}(\omega\otimes\omega)
-
\mathcal R.
$$

本輪不需要再展開：

$$
F
$$

的全部 tensor structure。

只利用它作為 exact nonlinear transfer carrier。

---

# 2. Gevrey generating carrier

對：

$$
\tau\ge0,
\qquad
s\ge0,
$$

定義：

$$
\boxed{
\mathcal G_{\tau,s}(t)
=
\left\|
e^{\tau\Lambda}
\Lambda^sS(t)
\right\|_2^2.
}
\tag{2.1}
$$

Fourier 形式：

$$
\boxed{
\mathcal G_{\tau,s}
=
\int_{\mathbb R^3}
e^{2\tau|\xi|}
|\xi|^{2s}
|\widehat S(\xi)|^2
\,d\xi.
}
\tag{2.2}
$$

這是一個完全 continuous spectral carrier。

它不使用：

- dyadic shell；
- integer Fourier mode partition；
- finite Galerkin index；
- derivative-order recursion。

其主要 coordinates 為：

$$
\boxed{
(\tau,s,\xi)
\in
[0,\infty)
\times
[0,\infty)
\times
\mathbb R^3.
}
$$

---

# 3. Continuous Hierarchy Resummation Theorem

## Theorem 3.1

假設：

$$
\mathcal G_{\tau,s}<\infty
$$

對某：

$$
\tau>0.
$$

任取：

$$
0\le\tau'<\tau
$$

以及任意實數：

$$
a\ge0.
$$

令：

$$
\delta
=
\tau-\tau'>0.
$$

則：

$$
\boxed{
\mathcal G_{\tau',s+a}
\le
\left(
\frac{a}{e\delta}
\right)^{2a}
\mathcal G_{\tau,s}
}
\tag{3.1}
$$

其中：

$$
a=0
$$

時右側 multiplicative factor 定義為：

$$
1.
$$

### Proof

由定義：

$$
\mathcal G_{\tau',s+a}
=
\int
e^{2\tau'|\xi|}
|\xi|^{2s+2a}
|\widehat S|^2d\xi.
$$

重寫：

$$
e^{2\tau'|\xi|}
|\xi|^{2s+2a}
=
\left(
|\xi|^{2a}
e^{-2\delta|\xi|}
\right)
e^{2\tau|\xi|}
|\xi|^{2s}.
$$

對：

$$
r\ge0,
$$

函數：

$$
r^{2a}e^{-2\delta r}
$$

的最大值在：

$$
r=\frac{a}{\delta}
$$

取得，且：

$$
\sup_{r\ge0}
r^{2a}e^{-2\delta r}
=
\left(
\frac{a}{e\delta}
\right)^{2a}.
$$

故得到 (3.1)。

$$
\square
$$

---

# 4. Meaning of the resummation theorem

Theorem 3.1 表示：

若某一個：

$$
\boxed{
\mathcal G_{\tau,s}
}
$$

在正 analytic radius：

$$
\tau>0
$$

下有界，

則對每一個實數 derivative increment：

$$
a\ge0
$$

以及每一個較小半徑：

$$
\tau'<\tau
$$

都有：

$$
\boxed{
\|e^{\tau'\Lambda}\Lambda^{s+a}S\|_2
<\infty.
}
$$

所以 Round 06 的 infinite hierarchy：

$$
\left\{
M_s
\right\}_{s\ge0}
$$

不需要逐階 closure。

只要：

$$
\boxed{
\tau>0
}
$$

的一個 Gevrey carrier保持控制，

所有 higher derivative levels 同時被吸收。

因此：

$$
\boxed{
\textbf{
Infinite derivative hierarchy is not, by itself,
an essential obstruction to Pure-C.
}
}
\tag{4.1}
$$

Round 06 的 hierarchy representation problem 已被 resummed。

---

# 5. Gevrey norm is a continuous spectral exponential moment

定義：

$$
r
=
|\xi|.
$$

令：

$$
e(\xi,t)
=
|\widehat S(\xi,t)|^2.
$$

則：

$$
\mathcal G_{\tau,s}
=
\int
e^{2\tau r}
r^{2s}
e(\xi,t)
d\xi.
$$

因此它是 continuous spectral measure 對：

$$
e^{2\tau r}
$$

的 exponential moment。

本輪 X 積分可寫成：

$$
\boxed{
X_{\rm Gevrey}
=
\int_{\rm exp\ spectral\ weight}
X_{\rm hierarchy}.
}
\tag{5.1}
$$

其功能不是增加另一個 derivative。

而是一次保留整個 high-frequency tail。

---

# 6. Exact time-dependent Gevrey balance

允許 analytic radius：

$$
\tau=\tau(t)
$$

隨時間變動。

定義：

$$
G
=
\mathcal G_{\tau,s},
$$

$$
K
=
\left\|
e^{\tau\Lambda}
\Lambda^{s+\frac12}S
\right\|_2^2,
$$

$$
H
=
\left\|
e^{\tau\Lambda}
\Lambda^{s+1}S
\right\|_2^2.
$$

對：

$$
\mathcal G_{\tau(t),s}
$$

微分。

因：

$$
\partial_t
e^{\tau(t)\Lambda}
=
\tau'(t)
\Lambda
e^{\tau(t)\Lambda},
$$

由 (1.1) 得：

$$
\boxed{
\frac12
G'
+
\nu H
=
\tau'K
+
T_{\tau,s},
}
\tag{6.1}
$$

其中：

$$
\boxed{
T_{\tau,s}
=
\left\langle
e^{\tau\Lambda}
\Lambda^sF,
e^{\tau\Lambda}
\Lambda^sS
\right\rangle.
}
\tag{6.2}
$$

這是 analytic generating carrier 的 exact balance。

---

# 7. Analytic spectral probability measure

若：

$$
G>0,
$$

定義：

$$
\boxed{
d\mu_{\tau,s}(\xi)
=
\frac{
e^{2\tau|\xi|}
|\xi|^{2s}
|\widehat S(\xi)|^2
}{
G
}
d\xi.
}
\tag{7.1}
$$

則：

$$
\mu_{\tau,s}
$$

為 probability measure。

定義：

$$
\boxed{
m_{\tau,s}
=
\mathbb E_{\mu_{\tau,s}}[r]
=
\frac{K}{G},
}
\tag{7.2}
$$

以及：

$$
\boxed{
\kappa_{\tau,s}
=
\mathbb E_{\mu_{\tau,s}}[r^2]
=
\frac{H}{G}.
}
\tag{7.3}
$$

並定義：

$$
\boxed{
V_{\tau,s}
=
\operatorname{Var}_{\mu_{\tau,s}}(r)
=
\kappa_{\tau,s}
-
m_{\tau,s}^2
\ge0.
}
\tag{7.4}
$$

---

# 8. Exact nonlinear growth rate

定義 weighted nonlinear growth rate：

$$
\boxed{
g_{\tau,s}
=
\frac{
T_{\tau,s}
}{
G
}.
}
\tag{8.1}
$$

若：

$$
\kappa_{\tau,s}>0,
$$

定義 analytic nonlinear/dissipation ratio：

$$
\boxed{
\alpha_{\tau,s}
=
\frac{
g_{\tau,s}
}{
\nu\kappa_{\tau,s}
}
=
\frac{
T_{\tau,s}
}{
\nu H
}.
}
\tag{8.2}
$$

由 (6.1)：

$$
\boxed{
\frac12
\frac d{dt}
\log G
=
\nu
(\alpha_{\tau,s}-1)
\kappa_{\tau,s}
+
\tau'
m_{\tau,s}.
}
\tag{8.3}
$$

這是本輪核心 exact identity。

---

# 9. Fixed-radius interpretation

若：

$$
\tau'=0,
$$

則：

$$
\boxed{
\frac12
\frac d{dt}
\log G
=
\nu
(\alpha_{\tau,s}-1)
\kappa_{\tau,s}.
}
\tag{9.1}
$$

因此：

$$
\alpha_{\tau,s}<1
$$

表示 analytic weighted dissipation 勝；

$$
\alpha_{\tau,s}>1
$$

表示 analytic weighted nonlinear transfer 勝。

與 Round 05 / Round 06 相同，

但現在：

$$
\boxed{
\alpha_{\tau,s}
}
$$

同時看到整個 high-frequency tail。

---

# 10. Adaptive radius tax

若：

$$
m_{\tau,s}>0,
$$

定義：

$$
\boxed{
\rho_{\tau,s}
=
\nu
(\alpha_{\tau,s}-1)_+
\frac{
\kappa_{\tau,s}
}{
m_{\tau,s}
}.
}
\tag{10.1}
$$

這個量具有：

$$
\text{length}/\text{time}
$$

維度。

現在選擇 adaptive analytic radius：

$$
\boxed{
\tau'
=
-\rho_{\tau,s}.
}
\tag{10.2}
$$

若：

$$
\alpha_{\tau,s}\le1,
$$

則：

$$
\rho_{\tau,s}=0
$$

且：

$$
G'\le0.
$$

若：

$$
\alpha_{\tau,s}>1,
$$

則由 (8.3)：

$$
\frac12
\frac d{dt}
\log G
=
\nu
(\alpha_{\tau,s}-1)\kappa_{\tau,s}
-
\rho_{\tau,s}
m_{\tau,s}
=
0.
$$

所以統一得到：

$$
\boxed{
G'(t)\le0.
}
\tag{10.3}
$$

命名：

$$
\boxed{
\textbf{Adaptive Analytic-Radius Compensation Law}.
}
$$

---

# 11. Radius tax decomposes into mean frequency + spectral spread

由：

$$
\kappa_{\tau,s}
=
m_{\tau,s}^2
+
V_{\tau,s},
$$

有：

$$
\frac{
\kappa_{\tau,s}
}{
m_{\tau,s}
}
=
m_{\tau,s}
+
\frac{
V_{\tau,s}
}{
m_{\tau,s}
}.
$$

所以：

$$
\boxed{
\rho_{\tau,s}
=
\nu
(\alpha_{\tau,s}-1)_+
\left[
m_{\tau,s}
+
\frac{
V_{\tau,s}
}{
m_{\tau,s}
}
\right].
}
\tag{11.1}
$$

這把 analytic-radius 消耗拆成：

1. supercritical nonlinear excess：

$$
(\alpha_{\tau,s}-1)_+;
$$

2. mean active frequency：

$$
m_{\tau,s};
$$

3. spectral-spread surcharge：

$$
\frac{
V_{\tau,s}
}{
m_{\tau,s}
}.
$$

所以高頻越高、spectral distribution 越廣、nonlinearity 越超臨界，

analytic radius 消耗越快。

---

# 12. Round 06 spectral variance reappears as a radius cost

Round 06 中 viscosity 的 exact scale-damping 由 spectral variance 表示。

本輪 variance 不再只是：

$$
\kappa_s'
$$

的 damping term。

它直接出現在：

$$
\boxed{
\rho_{\tau,s}
}
$$

中。

也就是：

$$
\boxed{
\text{spectral spread}
}
$$

同時具有兩個角色：

- diffusion 利用 spread 來壓制 scale drift；
- 若 nonlinear transfer 已超臨界，維持 analytic norm 所需的 radius sacrifice 也因 spread 增加。

這建立 Round 06 與 Round 07 的直接連線。

---

# 13. Analytic-radius budget identity

由：

$$
\tau'
=
-\rho_{\tau,s},
$$

得到：

$$
\boxed{
\tau(t)
=
\tau_0
-
\int_{t_0}^t
\rho_{\tau(\sigma),s}(\sigma)
\,d\sigma.
}
\tag{13.1}
$$

而沿此 adaptive path：

$$
\boxed{
\mathcal G_{\tau(t),s}(t)
\le
\mathcal G_{\tau_0,s}(t_0).
}
\tag{13.2}
$$

所以一個 positive initial analytic radius：

$$
\tau_0
$$

可以被視為 finite continuous budget。

nonlinear supercritical transfer 透過：

$$
\rho
$$

消耗這個 budget。

---

# 14. Continuation theorem along the adaptive radius

## Theorem 14.1

假設 smooth solution 存在於：

$$
[t_0,T)
$$

且：

$$
\mathcal G_{\tau_0,s}(t_0)<\infty
$$

對某：

$$
\tau_0>0.
$$

令：

$$
\tau(t)
$$

滿足 adaptive law (10.2)。

若存在：

$$
\tau_{\min}>0
$$

使：

$$
\boxed{
\tau(t)\ge\tau_{\min}
\qquad
\forall t<T,
}
\tag{14.1}
$$

則所有 finite Sobolev levels 在：

$$
[t_0,T)
$$

上一致受控。

### Proof

由 (13.2)：

$$
\mathcal G_{\tau(t),s}(t)
\le
G_0.
$$

因：

$$
\tau(t)\ge\tau_{\min},
$$

選：

$$
\tau'
=
\frac12\tau_{\min}.
$$

則：

$$
\tau(t)-\tau'
\ge
\frac12\tau_{\min}.
$$

由 Theorem 3.1，對任意：

$$
a\ge0,
$$

有：

$$
\boxed{
\mathcal G_{\tau',s+a}(t)
\le
\left(
\frac{
2a
}{
e\tau_{\min}
}
\right)^{2a}
G_0.
}
\tag{14.2}
$$

所以任意 fixed high Sobolev norm 都 uniformly bounded。

在標準 strong-solution continuation framework 中，取足夠高階即可延拓解。

$$
\square
$$

---

# 15. Radius-Budget Necessity for a finite maximal time

假設：

$$
T_\ast<\infty
$$

是 strong solution maximal time。

在任何：

$$
t_0<T_\ast
$$

若存在：

$$
\tau_0>0
$$

使：

$$
\mathcal G_{\tau_0,s}(t_0)<\infty,
$$

則 adaptive path 不可能在整個：

$$
[t_0,T_\ast)
$$

保持：

$$
\tau(t)\ge\tau_{\min}>0.
$$

否則由 Theorem 14.1 可延拓超過：

$$
T_\ast.
$$

因此 potential singular branch 必使 adaptive radius budget耗盡或失去 continuation：

$$
\boxed{
\inf_{t<T_\ast}
\tau(t)
=
0.
}
\tag{15.1}
$$

在 adaptive ODE 持續可定義的情況下：

$$
\boxed{
\int_{t_0}^{T_\ast}
\rho_{\tau(t),s}(t)
\,dt
\ge
\tau_0.
}
\tag{15.2}
$$

這是：

$$
\boxed{
\textbf{Analytic-Radius Budget Necessity}.
}
$$

---

# 16. Important limitation

(15.2) 不是 contradiction。

原因：

$$
\tau_0
$$

是 finite positive budget。

而：

$$
\rho
$$

可能在有限時間內具有足夠大的 integral 將它吃光。

所以本輪並沒有證明：

$$
\boxed{
\int\rho<\tau_0.
}
$$

無條件成立。

因此：

$$
\boxed{
\text{analytic resummation closes the hierarchy representation,
but not the radius budget}.
}
\tag{16.1}
$$

---

# 17. Why Gevrey resummation is stronger than finite derivative closure

Round 06 問：

$$
\alpha_s
\quad
\text{for all }s.
$$

Round 07 改為：

$$
\boxed{
\mathcal G_{\tau,s}.
}
$$

由 Theorem 3.1，

一個 positive：

$$
\tau
$$

就控制所有 real higher levels：

$$
s+a.
$$

所以：

$$
\boxed{
\text{one analytic carrier}
}
$$

取代：

$$
\boxed{
\text{infinitely many derivative carriers}.
}
$$

這正是本輪 X 積分的真正功能：

$$
\boxed{
\int_{\rm Gevrey}
\left\{
M_s
\right\}_{s\ge0}
\rightsquigarrow
\mathcal G_{\tau,s}.
}
\tag{17.1}
$$

---

# 18. Analytic radius is conjugate to frequency

由：

$$
G
=
\int
e^{2\tau r}
r^{2s}e\,d\xi,
$$

對：

$$
\tau
$$

微分：

$$
\boxed{
\partial_\tau\log G
=
2m_{\tau,s}.
}
\tag{18.1}
$$

再微分：

$$
\boxed{
\partial_\tau m_{\tau,s}
=
2
V_{\tau,s}.
}
\tag{18.2}
$$

所以：

$$
\tau
$$

不是任意 auxiliary parameter。

它是 spectral frequency 的 exponential-tilt coordinate。

而 variance：

$$
V_{\tau,s}
$$

正是：

$$
m
$$

對 analytic radius 的 response。

因此：

$$
\boxed{
\text{analytic radius}
\leftrightarrow
\text{continuous frequency statistics}
}
$$

是一個精確 dual relation。

---

# 19. Exact spectral replicator identity

定義 local Fourier transfer rate：

$$
\vartheta(\xi,t)
=
\frac{
\operatorname{Re}
\left(
\widehat F(\xi,t):
\overline{\widehat S(\xi,t)}
\right)
}{
|\widehat S(\xi,t)|^2
}
$$

在：

$$
\widehat S\neq0
$$

處。

在：

$$
\widehat S=0
$$

處令：

$$
\vartheta=0.
$$

對任何適當 test function：

$$
\phi(r),
$$

analytic weighted probability measure滿足：

$$
\boxed{
\frac d{dt}
\mathbb E_{\mu_{\tau,s}}
[\phi(r)]
=
2
\operatorname{Cov}_{\mu_{\tau,s}}
\left(
\phi(r),
\vartheta
-
\nu r^2
+
\tau'r
\right).
}
\tag{19.1}
$$

特別取：

$$
\phi(r)=r,
$$

得到：

$$
\boxed{
m'
=
2
\operatorname{Cov}(r,\vartheta)
-
2\nu
\operatorname{Cov}(r,r^2)
+
2\tau'
V.
}
\tag{19.2}
$$

沿 adaptive path：

$$
\tau'\le0,
$$

最後一項：

$$
2\tau'V
\le0.
$$

因此 shrink analytic radius 在 weighted spectral state 中具有額外向低頻重新加權的效果。

這是 gauge compensation，不是物理能量消失。

---

# 20. Pure-C frontier compression

Round 06 的 Boss：

$$
\boxed{
\text{Continuous Infinite Hierarchy}.
}
$$

Round 07 顯示：

$$
\boxed{
\text{positive analytic radius}
\Longrightarrow
\text{all derivative levels jointly controlled}.
}
$$

所以 hierarchy 本身不再是 primary frontier。

新的 frontier：

$$
\boxed{
\textbf{Analytic-Radius Budget}.
}
$$

形式：

$$
\boxed{
\tau_0
\stackrel{\rho}{\longrightarrow}
\tau(t).
}
$$

Potential singularity 只能沿：

$$
\boxed{
\tau(t)\downarrow0
}
$$

的 adaptive closure path 逃逸。

---

# 21. STOP-C11 — Analytic-Radius Budget Gap

定義：

$$
\boxed{
\bot_X^{\mathrm{C11}}
=
\left\langle
\begin{array}{l}
\text{layer}
=
\mathrm{Gevrey\ resummation},
\\
\text{carrier}
=
\mathcal G_{\tau,s},
\\
\text{hierarchy}
=
\mathrm{resummed},
\\
\text{exact\ radius\ tax}
=
\rho_{\tau,s}
=
\nu
(\alpha_{\tau,s}-1)_+
\kappa_{\tau,s}/m_{\tau,s},
\\
\text{radius\ law}
=
\tau'
=
-\rho_{\tau,s},
\\
\text{norm\ law}
=
\mathcal G_{\tau(t),s}(t)
\le
\mathcal G_{\tau_0,s}(t_0),
\\
\text{missing}
=
\mathrm{unconditional\ proof\ that\ radius\ budget\ cannot\ be\ exhausted},
\\
\text{discrete\ intrusion}
=
\mathrm{false}.
\end{array}
\right\rangle.
}
$$

命名：

$$
\boxed{
\textbf{STOP-C11:
Analytic-Radius Budget Exhaustion Gap}.
}
$$

---

# 22. 24/72 interpretation

本輪仍然：

$$
\boxed{
B=\mathsf C.
}
$$

因為：

$$
\xi\in\mathbb R^3
$$

與：

$$
\tau\in[0,\infty)
$$

都是 continuous coordinates。

update mode 是 hybrid：

$$
\boxed{
\mathsf S_{\rm time}
+
\mathsf P_{\rm spectral/global}.
}
$$

observation mode：

$$
\boxed{
\mathsf X
\to
\mathsf C_{\rm targeted}
}
$$

再次出現。

原本無限 hierarchy 是 multi-observable：

$$
\mathsf X.
$$

經 Gevrey X 積分後：

$$
\mathcal G_{\tau,s}
$$

成為針對 analytic continuation 目標的 sufficient targeted carrier。

transition law仍：

$$
\boxed{
L=\mathsf F.
}
$$

沒有需要：

$$
\mathsf K
$$

或：

$$
\mathsf Q.
$$

---

# 23. 24/72 Ledger — Round 07

| Step | X object / operation | $B$ | $U$ | $O$ | $L$ | status |
|---|---|---|---|---|---|---|
| C64 | Gevrey carrier $\mathcal G_{\tau,s}$ | $\mathsf C$ | continuous spectral | $\mathsf X$→targeted | $\mathsf F$ | FORM |
| C65 | real-order hierarchy resummation | $\mathsf C$ | global | targeted | $\mathsf F$ | PROVED |
| C66 | time-varying radius balance | $\mathsf C$ | $\mathsf S/\mathsf P$ | targeted | $\mathsf F$ | EXACT |
| C67 | analytic probability $\mu_{\tau,s}$ | $\mathsf C$ | spectral | $\mathsf X$ | $\mathsf F$ | FORM |
| C68 | $\alpha_{\tau,s}$ | $\mathsf C$ | relational | targeted scalar | $\mathsf F$ | FORM |
| C69 | adaptive radius tax $\rho_{\tau,s}$ | $\mathsf C$ | feedback | scalar | $\mathsf F$ | EXACT DEFINITION |
| C70 | $G'\le0$ under $\tau'=-\rho$ | $\mathsf C$ | adaptive | scalar | $\mathsf F$ | PROVED |
| C71 | positive radius $\to$ all Sobolev levels | $\mathsf C$ | resummed | targeted | $\mathsf F$ | PROVED |
| C72 | finite-time singularity $\to$ radius-budget exhaustion | $\mathsf C$ | adaptive | targeted | $\mathsf F$ | NECESSARY under continuation assumptions |
| C73 | unconditional non-exhaustion of radius | $\mathsf C$ | — | targeted | $\mathsf F$ | OPEN / STOP-C11 |

---

# 24. No essential discrete intrusion

Round 07 甚至在面對：

$$
\text{all derivative orders}
$$

時仍未需要：

- dyadic decomposition；
- profile sequence；
- scale index；
- Galerkin truncation；
- discrete shell cascade。

因此：

$$
\boxed{
T_{\mathsf C\to\mathsf D}
=
\text{NOT YET REACHED}.
}
\tag{24.1}
$$

目前 Pure-C 路徑已成：

$$
\boxed{
\begin{aligned}
\mathsf C_{\rm energy}
&\to
\mathsf C_{\rm critical}
\\
&\to
\mathsf C_{\rm relational}
\\
&\to
\mathsf C_{\rm nonlocal}
\\
&\to
\mathsf C_{\rm projected}
\\
&\to
\mathsf C_{\rm gradient\ geometry}
\\
&\to
\mathsf C_{\rm infinite\ hierarchy}
\\
&\to
\mathsf C_{\rm Gevrey\ resummed}
\\
&\to
\mathsf C_{\rm radius\ budget}.
\end{aligned}
}
\tag{24.2}
$$

---

# 25. What the next proof must actually do

現在再研究：

$$
\alpha_s
$$

逐階 dynamics 已經不是最佳路線。

真正 closure-bearing 問題變成：

$$
\boxed{
\text{Can the adaptive radius tax }
\rho_{\tau,s}
\text{ be shown unable to exhaust every positive initial analytic radius?}
}
$$

即尋找：

$$
\boxed{
\int_{t_0}^{T_\ast}
\rho_{\tau(t),s}(t)
dt
<
\tau_0.
}
\tag{25.1}
$$

的無條件機制。

若能證，則：

$$
\tau(t)
$$

保持正值，

由 Theorem 14.1：

$$
\boxed{
\text{all high Sobolev norms remain bounded}
}
$$

從而排除：

$$
T_\ast<\infty.
$$

---

# 26. Candidate next route — exploit radius tax structure

由：

$$
\rho
=
\nu
(\alpha-1)_+
\left(
m+\frac Vm
\right),
$$

下一輪不應只估：

$$
\alpha.
$$

應同時研究：

$$
\boxed{
(\alpha-1)_+,
\quad
m,
\quad
V.
}
$$

可能的 cancellation targets：

1. high nonlinear excess：

$$
(\alpha-1)_+
$$

是否迫使 viscosity variance：

$$
V
$$

同步增加；

2. 若：

$$
V
$$

增加，是否反過來快速降低：

$$
\alpha
$$

或 nonlinear-frequency covariance；

3. 是否存在 continuous uncertainty relation：

$$
\boxed{
\text{supercritical transfer}
\Longrightarrow
\text{spectral broadening}
\Longrightarrow
\text{stronger viscous damping}
}
$$

形成 negative feedback；

4. 若 spectrum 趨向 narrow：

$$
V\to0,
$$

則是否被迫接近單頻 / self-similar rigid state，進而由已知 rigidity/Liouville cuts 排除。

這將把下一輪分成兩個 continuous cases：

$$
\boxed{
V\text{ large}
\quad\vee\quad
V\text{ small}.
}
$$

但仍不用離散 shell。

---

# 27. External primary-source anchors

1. Animikh Biswas, Joshua Hudson, Jing Tian, *Persistence time of solutions of the three-dimensional Navier-Stokes equations in Sobolev-Gevrey classes*, arXiv:1912.11192.
   - time-varying analytic Gevrey classes；
   - persistence times comparable to Sobolev existence times；
   - explicit discussion that Gevrey methods avoid recursive higher-derivative estimation and quantify analyticity radius.

2. Ciprian Foias and Roger Temam, *Gevrey class regularity for the solutions of the Navier-Stokes equations*, Journal of Functional Analysis 87 (1989), 359–369.
   - classical Gevrey regularity framework for Navier–Stokes.

3. Cong Wang, *Space-time analyticity and refined analyticity radius of the Navier-Stokes equations in the critical Besov spaces*, arXiv:2503.03658.
   - current analytic-radius / critical-space continuation of the Gevrey program.

4. Luan T. Hoang, Vincent R. Martinez, *Asymptotic expansion in Gevrey spaces for solutions of Navier-Stokes equations*, arXiv:1511.03523.
   - later Gevrey-space Navier–Stokes framework.

---

# 28. Commit state

$$
\boxed{
\begin{aligned}
\text{Route}
&:
\mathrm{Pure\ Continuous\ Gevrey\ Resummation},
\\
\text{Essential }\mathsf C\to\mathsf D
&:
\mathrm{Not\ reached},
\\
\text{Infinite derivative hierarchy}
&:
\mathrm{resummed},
\\
\text{Generating carrier}
&:
\mathcal G_{\tau,s},
\\
\text{Adaptive radius tax}
&:
\rho_{\tau,s},
\\
\text{Exact compensation}
&:
\tau'=-\rho,
\\
\text{Gevrey norm}
&:
\mathrm{nonincreasing\ along\ adaptive\ path},
\\
\text{Positive radius}
&:
\mathrm{controls\ all\ higher\ Sobolev\ levels},
\\
\text{Potential singular escape}
&:
\mathrm{analytic\ radius\ budget\ exhaustion},
\\
\text{STOP-C11}
&:
\mathrm{Analytic\text{-}Radius\ Budget\ Exhaustion\ Gap},
\\
\text{Next}
&:
\mathrm{Radius\text{-}Tax\ Feedback\ via\ spectral\ variance}.
\end{aligned}
}
$$
