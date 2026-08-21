# NS × X 積分 × 24/72 範式實戰
## Round 21 — Pure Continuous Critical-Mass Replicator / Dynamic Intermittency Route

- 日期：2026-08-17
- 版本：v0.1
- 狀態：Proof-Route Experiment / Continuous-Only Dynamic-Intermittency Branch
- canonical source：UTF-8 Markdown
- canonical math delimiters：inline `$...$`；display `$$...$$`
- 前一輪：`NS_X72_Round20_PureContinuous_LowAmplitude_DegeneracyIntermittency_v0.1_2026-08-16.md`
- 本輪目標：不再只研究 low-amplitude set 的位置。直接研究 critical quotient mass
  $$
  d\mu_Q=\frac{|v|^3}{Q^3}dx
  $$
  以及 normalized strain rate
  $$
  K_S=\frac{|S|}{|v|}
  $$
  的 deterministic dynamics。建立 critical-mass transport–diffusion–selection equation，將 Round 20 的 normalized-strain intermittency ratio改寫成兩個 probability measures 的 $\chi^2$ separation，並找出 diffusion anti-intermittency 與 NS relative-source production之間的 exact competition。
- 非主張：本輪沒有證明 intermittency ratio無條件下降。相反地，本輪證明 common diffusion具有 exact anti-separation term，但 Navier–Stokes strain dynamics提供額外 selection / relative-source terms，其符號尚未被控制。

---

# 0. Round 20 handoff

令：

$$
Q
=
\mathfrak Q_3[u],
$$

optimal representative：

$$
v=u+\nabla q,
$$

$$
r=|v|,
$$

$$
n=\frac v{|v|}
$$

於：

$$
r>0.
$$

Round 20 定義 critical quotient probability measure：

$$
\boxed{
d\mu_Q
=
\frac{r^3}{Q^3}dx,
}
\tag{0.1}
$$

以及 normalized strain rate：

$$
\boxed{
K_S
=
\frac{|S|}{r}.
}
\tag{0.2}
$$

並證明：

$$
\boxed{
W_S
=
Q^3
\mathbb E_{\mu_Q}[K_S^2],
}
\tag{0.3}
$$

以及：

$$
\boxed{
\mathcal I_0
=
Q^3
\mathbb E_{\mu_Q}[K_S^4].
}
\tag{0.4}
$$

intermittency ratio：

$$
\boxed{
\mathfrak J_S
=
\frac{
\mathbb E_{\mu_Q}[K_S^4]
}{
\mathbb E_{\mu_Q}[K_S^2]^2
}
\ge1.
}
\tag{0.5}
$$

Round 20 STOP：

$$
\boxed{
\text{STOP-C24}
=
\text{Normalized-Deformation Intermittency / Zero-Set Degeneracy Gap}.
}
$$

本輪問：

$$
\boxed{
\text{Does NS dynamics itself suppress or create }\mathfrak J_S?
}
$$

---

# 1. Optimal representative evolution

Round 14–20 representative equation：

$$
\boxed{
\partial_t v
+
\mathcal L_u^{(1)}v
=
\nu\Delta v
+
\nabla\chi_g,
}
\tag{1.1}
$$

其中：

$$
\mathcal L_u^{(1)}v
=
(u\cdot\nabla)v
+
(\nabla u)^\top v,
$$

而：

$$
\chi_g
$$

是維持當下 optimal nonlinear gauge：

$$
\operatorname{div}(rv)=0
$$

所需的 scalar gauge-maintenance potential。

記：

$$
\boxed{
\gamma_Q
=
-
n^\top S_un.
}
\tag{1.2}
$$

---

# 2. Exact amplitude equation

對 (1.1) 與：

$$
n=\frac v{|v|}
$$

pair。

使用：

$$
n^\top(\nabla u)^\top n
=
n^\top S_un
=
-\gamma_Q,
$$

以及：

$$
n\cdot\Delta v
=
\Delta r
-
r|\nabla n|^2,
$$

得到：

$$
\boxed{
(\partial_t+u\cdot\nabla)r
=
\nu\Delta r
-
\nu r|\nabla n|^2
+
\gamma_Q r
+
n\cdot\nabla\chi_g.
}
\tag{2.1}
$$

所以 quotient amplitude由：

- viscosity；
- direction turning；
- compressive strain；
- dynamic gauge maintenance；

共同演化。

---

# 3. Exact critical-mass density equation

令：

$$
\boxed{
\rho_Q
=
r^3.
}
\tag{3.1}
$$

定義 local normalized-Hodge dissipation rate：

$$
\boxed{
K_D
=
\frac{
|\nabla v|^2+|\nabla r|^2
}{
r^2
}
}
\tag{3.2}
$$

於：

$$
r>0.
$$

由 convex chain rule：

$$
r\,v\cdot\Delta v
=
\frac13\Delta(r^3)
-
r
\left(
|\nabla v|^2+|\nabla r|^2
\right).
$$

又 nonlinear gauge：

$$
\operatorname{div}(rv)=0
$$

給：

$$
rv\cdot\nabla\chi_g
=
\operatorname{div}(\chi_g rv).
$$

所以：

$$
\boxed{
\begin{aligned}
\partial_t\rho_Q
+
\operatorname{div}(u\rho_Q)
={}&
\nu\Delta\rho_Q
\\
&+
3
\left(
\gamma_Q-\nu K_D
\right)
\rho_Q
\\
&+
3\operatorname{div}(\chi_g rv).
\end{aligned}
}
\tag{3.3}
$$

---

# 4. Effective deterministic critical-mass drift

在：

$$
r>0
$$

定義：

$$
\boxed{
b_Q
=
u
-
3
\frac{
\chi_g
}{
r
}
n.
}
\tag{4.1}
$$

因：

$$
\rho_Q
\left(
-3\frac{\chi_g}{r}n
\right)
=
-3\chi_g r^2n
=
-3\chi_g rv,
$$

(3.3) 可寫成：

$$
\boxed{
\partial_t\rho_Q
+
\operatorname{div}(b_Q\rho_Q)
=
\nu\Delta\rho_Q
+
3G_Q\rho_Q,
}
\tag{4.2}
$$

其中：

$$
\boxed{
G_Q
=
\gamma_Q-\nu K_D.
}
\tag{4.3}
$$

注意：

$$
b_Q
$$

在：

$$
r\to0
$$

的 normalized representation可顯得 singular，

但原始 physical gauge flux：

$$
-3\chi_g rv
=
-3\chi_g r^2n
$$

在 $\chi_g$ bounded時反而隨 $r^2$ 退化。

因此：

$$
\boxed{
\text{singular normalized drift}
\neq
\text{automatically singular physical flux}.
}
\tag{4.4}
$$

---

# 5. Exact logarithmic critical-quotient growth rate

因：

$$
Q^3
=
\int\rho_Qdx,
$$

對 (4.2) 積分：

$$
\boxed{
\frac d{dt}Q^3
=
3Q^3
\mathbb E_{\mu_Q}[G_Q].
}
\tag{5.1}
$$

因此：

$$
\boxed{
\frac d{dt}
\log Q
=
\mathbb E_{\mu_Q}[G_Q].
}
\tag{5.2}
$$

命名：

$$
\boxed{
\textbf{Critical-Mass Mean-Growth Identity}.
}
$$

也就是：

> critical quotient norm的 logarithmic growth，正好是 critical mass distribution下 local growth field $G_Q$ 的平均。

---

# 6. Normalized critical-mass replicator–diffusion equation

令：

$$
m_Q
=
\frac{
\rho_Q
}{
Q^3
}
$$

為 $\mu_Q$ 的 Lebesgue density。

由 (4.2) 與 (5.1)：

$$
\boxed{
\partial_t m_Q
+
\operatorname{div}(b_Qm_Q)
=
\nu\Delta m_Q
+
3
\left(
G_Q-\overline G_Q
\right)m_Q,
}
\tag{6.1}
$$

其中：

$$
\boxed{
\overline G_Q
=
\mathbb E_{\mu_Q}[G_Q].
}
\tag{6.2}
$$

這是一個 deterministic：

$$
\boxed{
\text{transport}
+
\text{diffusion}
+
\text{replicator/selection}
}
$$

equation。

「replicator」只描述 normalized mass在高於平均 growth區域被相對放大的數學形式。

它不引入隨機 physical state。

---

# 7. 24/72 classification audit — probability does not imply stochastic transition

Equation (6.1) 使用 probability density：

$$
m_Q.
$$

但：

$$
m_Q
$$

是單一 deterministic Navier–Stokes state：

$$
u(t)
$$

的 normalized structural observable。

給定：

$$
u(t),
$$

$$
m_Q(t)
$$

被唯一決定。

所以本輪：

$$
\boxed{
L=\mathsf F
}
$$

仍然成立。

不能因為寫成：

$$
\text{Fokker–Planck-like}
$$

或 probability-measure language，

就把 72 transition-law axis偷換成：

$$
\mathsf K.
$$

因此：

$$
\boxed{
\textbf{
probability representation
does not imply stochastic transition law.
}
}
\tag{7.1}
$$

這是本輪對 24/72 framework本身的一個 consistency check。

---

# 8. Exact observable covariance law

對 smooth time-dependent scalar observable：

$$
\phi(x,t),
$$

由 (6.1) integration by parts：

$$
\boxed{
\begin{aligned}
\frac d{dt}
\mathbb E_{\mu_Q}[\phi]
={}&
\mathbb E_{\mu_Q}
\left[
\partial_t\phi
+
b_Q\cdot\nabla\phi
+
\nu\Delta\phi
\right]
\\
&+
3
\operatorname{Cov}_{\mu_Q}
(\phi,G_Q).
\end{aligned}
}
\tag{8.1}
$$

所以 critical mass的 structural selection由：

$$
\boxed{
\operatorname{Cov}_{\mu_Q}
(\phi,G_Q)
}
$$

精確控制。

若 observable在高-growth區域較大，selection會提高其 normalized expectation。

---

# 9. Critical-mass entropy balance

在 smooth positive-density regime定義 Shannon-type entropy：

$$
\boxed{
\mathscr H_Q
=
-
\int
m_Q\log m_Q\,dx.
}
\tag{9.1}
$$

由 (6.1)：

$$
\boxed{
\begin{aligned}
\mathscr H_Q'
={}&
\mathbb E_{\mu_Q}
[
\operatorname{div}b_Q
]
\\
&+
\nu
\int
|\nabla\log m_Q|^2
d\mu_Q
\\
&-
3
\operatorname{Cov}_{\mu_Q}
(
\log m_Q,
G_Q
).
\end{aligned}
}
\tag{9.2}
$$

三個 terms：

1. deterministic drift compression / expansion；
2. positive Fisher-information diffusion；
3. growth-selection concentration / deconcentration。

所以 viscosity確實提供 anti-concentration entropy production，

但：

$$
\boxed{
\text{entropy is not automatically monotone}
}
$$

因 gauge drift與 selection covariance沒有 universal sign。

---

# 10. Strain-energy probability measure

假設：

$$
W_S
=
\int
r|S|^2dx
>0.
$$

定義 weighted strain-energy measure：

$$
\boxed{
d\nu_S
=
\frac{
r|S|^2
}{
W_S
}
dx.
}
\tag{10.1}
$$

由：

$$
d\mu_Q
=
\frac{
r^3
}{
Q^3
}
dx,
$$

有：

$$
\boxed{
\frac{
d\nu_S
}{
d\mu_Q
}
=
\frac{
K_S^2
}{
\mathbb E_{\mu_Q}[K_S^2]
}.
}
\tag{10.2}
$$

令：

$$
\boxed{
f_S
=
\frac{
d\nu_S
}{
d\mu_Q
}.
}
\tag{10.3}
$$

則：

$$
\mathbb E_{\mu_Q}[f_S]=1.
$$

---

# 11. Intermittency is exactly a $\chi^2$ measure separation

Round 20：

$$
\mathfrak J_S
=
\frac{
\mathbb E[K_S^4]
}{
\mathbb E[K_S^2]^2
}.
$$

由 (10.2)：

$$
\boxed{
\mathfrak J_S
=
\int
f_S^2
d\mu_Q.
}
\tag{11.1}
$$

因此 Pearson $\chi^2$ divergence：

$$
\chi^2
(\nu_S\|\mu_Q)
=
\int
(f_S-1)^2d\mu_Q
$$

滿足：

$$
\boxed{
\mathfrak J_S-1
=
\chi^2
(\nu_S\|\mu_Q).
}
\tag{11.2}
$$

命名：

$$
\boxed{
\textbf{Intermittency–Measure-Separation Identity}.
}
$$

所以 Round 20 的 normalized-deformation intermittency有一個非常直接的意思：

> strain-weighted energy measure與 critical quotient-mass measure彼此分離了多少。

---

# 12. Anti-concentration inequality

對任意 measurable set：

$$
A,
$$

Cauchy–Schwarz：

$$
\nu_S(A)
=
\int_A
f_Sd\mu_Q
$$

$$
\le
\mu_Q(A)^{1/2}
\left(
\int_A
f_S^2d\mu_Q
\right)^{1/2}.
$$

所以：

$$
\boxed{
\nu_S(A)^2
\le
\mathfrak J_S
\mu_Q(A).
}
\tag{12.1}
$$

因此如果某個 set承擔固定 fraction：

$$
\nu_S(A)\ge\beta>0,
$$

則：

$$
\boxed{
\mathfrak J_S
\ge
\frac{
\beta^2
}{
\mu_Q(A)
}.
}
\tag{12.2}
$$

命名：

$$
\boxed{
\textbf{Critical-Mass Anti-Concentration Inequality}.
}
$$

---

# 13. Low-amplitude escape becomes measure singularization

令：

$$
A_\eta
=
\{
0<r<\eta
\}.
$$

如果存在：

$$
\eta_j\downarrow0
$$

使：

$$
\mu_Q(A_{\eta_j})
\to0
$$

但：

$$
\nu_S(A_{\eta_j})
\ge
\beta>0,
$$

則由 (12.2)：

$$
\boxed{
\mathfrak J_S
\to\infty.
}
\tag{13.1}
$$

所以 near-zero strain escape等價於：

$$
\boxed{
\text{strain-energy measure becomes singularly concentrated
relative to critical quotient mass}.
}
$$

如果 exact-zero set：

$$
\{r=0,\ |S|>0\}
$$

本身存在 relevant singular contribution，

則 Round 20 convention直接給：

$$
\mathcal I_0=+\infty,
$$

屬於更強的 Z0 branch。

---

# 14. Effective critical-mass participation fraction

定義：

$$
\boxed{
\mathfrak m_{\rm eff}
=
\frac1{\mathfrak J_S}.
}
\tag{14.1}
$$

因：

$$
\mathfrak J_S\ge1,
$$

有：

$$
0<\mathfrak m_{\rm eff}\le1.
$$

它可視為 strain energy相對 critical mass的一個 inverse-participation fraction。

large：

$$
\mathfrak J_S
$$

意味：

$$
\mathfrak m_{\rm eff}
\ll1.
$$

也就是 dangerous normalized strain只佔用非常少的 quotient-critical mass。

---

# 15. Continuous moment-order field

對 real：

$$
p\ge0
$$

定義：

$$
\boxed{
\mathcal M_p
=
\int
r^{3-p}
|S|^pdx
=
Q^3
\mathbb E_{\mu_Q}
[K_S^p].
}
\tag{15.1}
$$

特殊值：

$$
\boxed{
\mathcal M_0=Q^3,
}
$$

$$
\boxed{
\mathcal M_2=W_S,
}
$$

$$
\boxed{
\mathcal M_4=\mathcal I_0.
}
$$

所以 Round 20 所謂 second/fourth moment並不需要作為兩個 discrete moment階。

它們其實是 continuous：

$$
\boxed{
p\in[0,\infty)
}
$$

moment-order field的兩個 slices。

---

# 16. Continuous moment convexity

令：

$$
F(p)
=
\log
\mathbb E_{\mu_Q}
[K_S^p]
$$

在 moments finite且 logarithmic differentiation合法處。

定義 $p$-tilted measure：

$$
\boxed{
d\mu_p
=
\frac{
K_S^p
}{
\mathbb E_{\mu_Q}[K_S^p]
}
d\mu_Q.
}
\tag{16.1}
$$

則：

$$
\boxed{
F'(p)
=
\mathbb E_{\mu_p}
[
\log K_S
],
}
\tag{16.2}
$$

以及：

$$
\boxed{
F''(p)
=
\operatorname{Var}_{\mu_p}
(
\log K_S
)
\ge0.
}
\tag{16.3}
$$

所以 moment-order geometry本身是 convex。

---

# 17. Intermittency as continuous moment-space curvature

因：

$$
F(0)=0,
$$

有：

$$
\log\mathfrak J_S
=
F(4)-2F(2)+F(0).
$$

因此：

$$
\boxed{
\log\mathfrak J_S
=
\int_0^2
\int_s^{s+2}
F''(\tau)
\,d\tau\,ds.
}
\tag{17.1}
$$

代入 (16.3)：

$$
\boxed{
\log\mathfrak J_S
=
\int_0^2
\int_s^{s+2}
\operatorname{Var}_{\mu_\tau}
(
\log K_S
)
\,d\tau\,ds.
}
\tag{17.2}
$$

命名：

$$
\boxed{
\textbf{Continuous Moment-Curvature Identity}.
}
$$

因此 intermittency不是「第四階減第二階」這種離散現象。

它是：

$$
\boxed{
\text{normalized deformation rate沿 continuous moment order }p
\text{ 的統計曲率}.
}
$$

---

# 18. Exact common-Markov anti-separation lemma

考慮兩個 probability densities：

$$
m_1,
\qquad
m_2
$$

若它們都只 obey同一 deterministic drift–diffusion：

$$
\partial_t m_j
+
\operatorname{div}(b m_j)
=
\nu\Delta m_j,
$$

令：

$$
f=\frac{m_2}{m_1}.
$$

則直接計算：

$$
\boxed{
\frac d{dt}
\int
f^2m_1dx
=
-2\nu
\int
m_1
|\nabla f|^2dx
\le0.
}
\tag{18.1}
$$

所以：

$$
\boxed{
\textbf{
common deterministic transport does not create }\chi^2\textbf{ separation,
and common viscosity strictly dissipates it.
}
}
$$

這是一個 direct PDE calculation，不需要 stochastic ontology。

---

# 19. Actual strain measure does not follow the same generator

weighted strain density：

$$
\zeta_S
=
r|S|^2
$$

不只被：

$$
b_Q,
\qquad
\nu
$$

transport/diffuse。

strain equation：

$$
(\partial_t+u\cdot\nabla)S
=
\nu\Delta S
-
S^2
-
\frac14\omega\otimes\omega
+
\frac14|\omega|^2I
-
\nabla^2p
$$

會額外產生：

- strain self-interaction；
- vorticity–strain coupling；
- local pressure-Hessian contraction；
- cross-diffusion between $r$ and $|S|^2$；
- gauge-maintenance terms。

因此定義 exact relative-source rate：

$$
\boxed{
\mathcal R_S
=
\frac1{\zeta_S}
\left[
\partial_t\zeta_S
+
\operatorname{div}(b_Q\zeta_S)
-
\nu\Delta\zeta_S
\right]
-
3G_Q
}
\tag{19.1}
$$

於：

$$
\zeta_S>0.
$$

這不是 approximation。

它是「weighted strain density相對 critical-mass common generator多出的全部 source」之 exact definition。

---

# 20. Normalized strain-measure equation

令：

$$
m_S
=
\frac{
\zeta_S
}{
W_S
}
$$

為 $\nu_S$ density。

由 (19.1)，其 normalized equation可寫：

$$
\boxed{
\begin{aligned}
\partial_t m_S
+
\operatorname{div}(b_Qm_S)
={}&
\nu\Delta m_S
\\
&+
\left[
3G_Q+\mathcal R_S
-
\overline C_S
\right]
m_S,
\end{aligned}
}
\tag{20.1}
$$

其中：

$$
\boxed{
\overline C_S
=
\mathbb E_{\nu_S}
[
3G_Q+\mathcal R_S
].
}
\tag{20.2}
$$

因此 $\mu_Q$ 與 $\nu_S$：

- share deterministic drift；
- share viscosity；
- differ in normalized selection/source structure。

---

# 21. Exact dynamic intermittency equation

令：

$$
f_S
=
\frac{
m_S
}{
m_Q
}.
$$

由 (6.1) 與 (20.1) 直接計算：

$$
\boxed{
\begin{aligned}
\mathfrak J_S'
={}&
-2\nu
\int
m_Q
|\nabla f_S|^2dx
\\
&+
\int
f_S^2
\Big[
3G_Q
+
2\mathcal R_S
-
2\overline C_S
+
3\overline G_Q
\Big]
d\mu_Q.
\end{aligned}
}
\tag{21.1}
$$

其中：

$$
\overline G_Q
=
\mathbb E_{\mu_Q}[G_Q].
$$

定義：

$$
\boxed{
\mathcal F_{\rm rel}
=
\int
m_Q|\nabla f_S|^2dx
}
\tag{21.2}
$$

以及：

$$
\boxed{
\mathcal P_{\rm sel}
=
\int
f_S^2
\Big[
3G_Q
+
2\mathcal R_S
-
2\overline C_S
+
3\overline G_Q
\Big]
d\mu_Q.
}
\tag{21.3}
$$

則：

$$
\boxed{
\mathfrak J_S'
=
-2\nu
\mathcal F_{\rm rel}
+
\mathcal P_{\rm sel}.
}
\tag{21.4}
$$

命名：

$$
\boxed{
\textbf{Dynamic Intermittency Balance}.
}
$$

---

# 22. Interpretation of the dynamic intermittency balance

第一項：

$$
\boxed{
-2\nu\mathcal F_{\rm rel}\le0
}
$$

是 exact relative Fisher-information dissipation。

它會把：

$$
\nu_S
$$

與：

$$
\mu_Q
$$

重新混合。

第二項：

$$
\boxed{
\mathcal P_{\rm sel}
}
$$

收集：

- critical-mass growth selection；
- strain-specific nonlinear source；
- pressure-Hessian source；
- gauge/source mismatch。

所以：

$$
\boxed{
\textbf{
intermittency can grow only if relative NS selection/source production
beats common viscous mixing.
}
}
\tag{22.1}
$$

這是本輪最重要的 dynamic reduction。

---

# 23. Conditional anti-intermittency branch

若在 interval：

$$
I
$$

上：

$$
\boxed{
\mathcal P_{\rm sel}
\le
2\nu
\mathcal F_{\rm rel},
}
\tag{23.1}
$$

則：

$$
\boxed{
\mathfrak J_S'
\le0.
}
\tag{23.2}
$$

更強若：

$$
\mathcal P_{\rm sel}
\le
(2-\delta)\nu
\mathcal F_{\rm rel}
$$

對：

$$
\delta>0,
$$

則：

$$
\boxed{
\mathfrak J_S'
\le
-\delta\nu
\mathcal F_{\rm rel}.
}
\tag{23.3}
$$

所以 dynamic intermittency closure已被壓成：

$$
\boxed{
\text{selection/source production}
\quad\text{versus}\quad
\text{relative Fisher mixing}.
}
$$

---

# 24. Why diffusion alone is not enough

Equation (21.4) 同時回答 Round 20 的問題。

common viscosity確實具有 exact self-regularizing mechanism：

$$
-2\nu\mathcal F_{\rm rel}.
$$

但 full NS 還有：

$$
\mathcal P_{\rm sel},
$$

沒有 universal sign。

所以：

$$
\boxed{
\text{viscous anti-concentration exists,
but it is not by itself a global regularity proof}.
}
$$

真正缺的是：

$$
\boxed{
\mathcal P_{\rm sel}
\stackrel{?}{\le}
2\nu\mathcal F_{\rm rel}
}
$$

或其 time-integrated weaker version。

---

# 25. A new representation-stable interpretation of intermittency

Round 20：

$$
\mathfrak J_S
$$

看起來只是 moment ratio。

Round 21 得到三個等價視角：

$$
\boxed{
\begin{aligned}
\mathfrak J_S
&=
\frac{
\mathbb E[K_S^4]
}{
\mathbb E[K_S^2]^2}
\\
&=
1+\chi^2(\nu_S\|\mu_Q)
\\
&=
\exp
\left[
\int_0^2
\int_s^{s+2}
\operatorname{Var}_{\mu_\tau}
(\log K_S)
d\tau ds
\right].
\end{aligned}
}
\tag{25.1}
$$

所以 normalized-deformation intermittency同時是：

- moment gap；
- measure separation；
- continuous moment-space curvature。

這已經具有相當強的 representation stability。

---

# 26. STOP-C25 — Relative-Source / Critical-Mass Separation Gap

定義：

$$
\boxed{
\bot_X^{\mathrm{C25}}
=
\left\langle
\begin{array}{l}
\text{layer}
=
\mathrm{dynamic\ critical\ mass/intermittency},
\\
\text{critical\ mass\ PDE}
=
\mathrm{deterministic\ transport+diffusion+selection},
\\
\text{quotient\ growth}
=
\overline G_Q,
\\
\text{intermittency}
=
1+\chi^2(\nu_S\|\mu_Q),
\\
\text{common\ viscosity}
=
-2\nu\mathcal F_{\rm rel},
\\
\text{relative\ NS\ production}
=
\mathcal P_{\rm sel},
\\
\text{exact\ balance}
=
\mathfrak J_S'
=
-2\nu\mathcal F_{\rm rel}
+
\mathcal P_{\rm sel},
\\
\text{missing}
=
\mathrm{unconditional\ domination\ of\ relative\ production\ by\ viscous\ mixing},
\\
\text{probability\ representation}
\neq
\text{stochastic\ law},
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
\textbf{STOP-C25:
Relative-Source / Critical-Mass Separation Gap}.
}
$$

---

# 27. 24/72 Ledger — Round 21

| Step | object | $B$ | $U$ | $O$ | $L$ | status |
|---|---|---|---|---|---|---|
| C259 | amplitude equation | $\mathsf C$ | transport/elliptic | relational | $\mathsf F$ | EXACT |
| C260 | critical-mass density $\rho_Q$ | $\mathsf C$ | continuous measure | targeted | $\mathsf F$ | FORM |
| C261 | deterministic critical-mass PDE | $\mathsf C$ | $\mathsf S+\mathsf P$ | $\mathsf X$ | $\mathsf F$ | EXACT |
| C262 | mean growth identity | $\mathsf C$ | recognition | scalar | $\mathsf F$ | EXACT |
| C263 | normalized replicator–diffusion | $\mathsf C$ | continuous selection | measure | $\mathsf F$ | EXACT |
| C264 | probability $\Rightarrow\mathsf K$ | — | — | — | — | REFUTED as classification inference |
| C265 | observable covariance law | $\mathsf C$ | selection | relational | $\mathsf F$ | EXACT |
| C266 | critical-mass entropy balance | $\mathsf C$ | diffusion/selection | scalar | $\mathsf F$ | EXACT under smoothness |
| C267 | strain-energy measure $\nu_S$ | $\mathsf C$ | measure | $\mathsf X$ | $\mathsf F$ | FORM |
| C268 | intermittency–$\chi^2$ identity | $\mathsf C$ | recognition | scalar | $\mathsf F$ | EXACT |
| C269 | anti-concentration inequality | $\mathsf C$ | measure geometry | targeted | $\mathsf F$ | PROVED |
| C270 | continuous moment field $\mathcal M_p$ | $\mathsf C$ | continuous $p$ | profile | $\mathsf F$ | FORM |
| C271 | moment-curvature identity | $\mathsf C$ | exponential tilt | profile | $\mathsf F$ | EXACT |
| C272 | common-Markov anti-separation | $\mathsf C$ | drift/diffusion | scalar | $\mathsf F$ | PROVED |
| C273 | strain relative-source $\mathcal R_S$ | $\mathsf C$ | nonlinear NS | $\mathsf X$ | $\mathsf F$ | EXACT DEFINITION |
| C274 | dynamic intermittency balance | $\mathsf C$ | measure coupling | scalar | $\mathsf F$ | EXACT |
| C275 | unconditional $\mathcal P_{\rm sel}\le2\nu\mathcal F_{\rm rel}$ | $\mathsf C$ | coupled NS | targeted | $\mathsf F$ | OPEN / STOP-C25 |

---

# 28. Continuous-versus-discrete status

本輪看起來最容易誤判成「離散／隨機」：

- probability measure；
- replicator；
- Fokker–Planck-like diffusion；
- moment hierarchy。

但：

1. measure來自單一 deterministic state；
2. transition仍由 NS deterministic PDE決定；
3. moment order已提升為：
   $$
   p\in[0,\infty);
   $$
4. concentration以 continuous measure divergence描述。

所以：

$$
\boxed{
B=\mathsf C,
\qquad
L=\mathsf F,
}
$$

仍保持。

因此：

$$
\boxed{
T_{\mathsf C\to\mathsf D}
=
\text{NOT YET REACHED}.
}
\tag{28.1}
$$

---

# 29. Strongest results of Round 21

## R21-A — deterministic critical-mass replicator equation

$$
\boxed{
\partial_t m_Q
+
\operatorname{div}(b_Qm_Q)
=
\nu\Delta m_Q
+
3(G_Q-\bar G_Q)m_Q.
}
$$

## R21-B — exact critical growth rate

$$
\boxed{
(\log Q)'
=
\mathbb E_{\mu_Q}[G_Q].
}
$$

## R21-C — intermittency is measure separation

$$
\boxed{
\mathfrak J_S-1
=
\chi^2(\nu_S\|\mu_Q).
}
$$

## R21-D — concentration witness

$$
\boxed{
\nu_S(A)^2
\le
\mathfrak J_S\mu_Q(A).
}
$$

## R21-E — continuous moment curvature

$$
\boxed{
\log\mathfrak J_S
=
\int_0^2\int_s^{s+2}
\operatorname{Var}_{\mu_\tau}(\log K_S)
\,d\tau ds.
}
$$

## R21-F — dynamic intermittency balance

$$
\boxed{
\mathfrak J_S'
=
-2\nu\mathcal F_{\rm rel}
+
\mathcal P_{\rm sel}.
}
$$

所以 viscosity確實提供 exact anti-intermittency mechanism，

但 NS relative source仍可能打敗它。

---

# 30. Next round — relative-source decomposition

下一輪不再研究：

$$
\mathfrak J_S
$$

作 abstract ratio。

直接展開：

$$
\boxed{
\mathcal R_S
}
$$

與：

$$
\boxed{
\mathcal P_{\rm sel}.
}
$$

核心問題：

1. 把 relative source拆成：
   $$
   \text{strain self-amplification}
   +
   \text{vorticity coupling}
   +
   \text{pressure Hessian}
   +
   \text{cross diffusion}
   +
   \text{gauge maintenance};
   $$

2. 檢查哪些 terms在 $\chi^2$ balance中有 exact cancellation；

3. pressure Hessian是否再次可被 global/quotient projection消掉；

4. dangerous middle-strain channel是否正好出現在 positive relative selection term；

5. 若剩餘 $\mathcal P_{\rm sel}$ 可被 Round 05 / Round 19 confluence carriers上界，則可能形成第一次真正的 self-closing feedback loop；

6. 仍保持 continuous measures，不做 particle / atom approximation。

---

# 31. External primary-source anchors

1. Evan Miller, *On the interaction of strain and vorticity for solutions of the Navier--Stokes equation*, arXiv:2407.02691.
   - strain–vorticity interaction、projected strain structure與 nonlinear depletion的 primary-source背景。

2. Evan Miller, *A regularity criterion for the Navier-Stokes equation involving only the middle eigenvalue of the strain tensor*, arXiv:1710.05569.
   - positive middle-strain channel的 scale-critical regularity背景。

3. Alexis Vasseur, *Regularity criterion for 3D Navier-Stokes equations in terms of the direction of the velocity*, arXiv:0705.2446.
   - amplitude/direction geometric regularity route的 primary-source背景；本輪 optimal quotient direction不同於原 velocity direction。

本輪 critical-mass PDE、$\chi^2$ identity、continuous moment-curvature identity與 dynamic intermittency balance均為本文直接推導。

---

# 32. Commit state

$$
\boxed{
\begin{aligned}
\text{Route}
&=
\mathrm{Pure\ Continuous\ Critical\text{-}Mass\ Dynamic\ Intermittency},
\\
\text{24/72 substrate}
&=
\mathsf C,
\\
\text{24/72 transition law}
&=
\mathsf F,
\\
\text{Probability representation}
&\neq
\mathrm{stochastic\ ontology},
\\
\text{Critical mass}
&=
\mu_Q,
\\
\text{Strain measure}
&=
\nu_S,
\\
\text{Intermittency}
&=
1+\chi^2(\nu_S\|\mu_Q),
\\
\text{Viscous mechanism}
&=
-2\nu\mathcal F_{\rm rel},
\\
\text{Dangerous mechanism}
&=
\mathcal P_{\rm sel},
\\
\text{STOP-C25}
&=
\mathrm{Relative\text{-}Source/Critical\text{-}Mass\ Separation\ Gap},
\\
\text{Essential }\mathsf C\to\mathsf D
&=
\mathrm{Not\ reached},
\\
\text{Next}
&=
\mathrm{Relative\text{-}Source\ Decomposition}.
\end{aligned}
}
$$
