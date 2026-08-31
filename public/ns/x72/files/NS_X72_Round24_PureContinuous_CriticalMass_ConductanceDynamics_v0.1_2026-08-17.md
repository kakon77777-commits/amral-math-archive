# NS × X 積分 × 24/72 範式實戰
## Round 24 — Pure Continuous Critical-Mass Conductance Dynamics / Neck-Restoration Route

- 日期：2026-08-17
- 版本：v0.1
- 狀態：Proof-Route Experiment / Continuous-Only Conductance Branch
- canonical source：UTF-8 Markdown
- canonical math delimiters：inline `$...$`；display `$$...$$`
- 前一輪：`NS_X72_Round23_PureContinuous_ConfluenceFeedback_SpectralGapLeakage_v0.1_2026-08-17.md`
- 本輪目標：直接研究 critical quotient mass
  $$
  d\mu_Q=m_Qdx
  $$
  的 continuous Cheeger conductance、isoperimetric profile與 material-cut dynamics。檢驗 viscosity 是否會自動把 disconnected / thin-neck critical mass恢復成足夠大的 spectral gap，並量化 selection對 neck restoration的競爭。
- 非主張：本文沒有證明 uniform-in-time positive conductance。相反地，本輪證明 strict positivity / topological reconnection不足以推出 quantitative spectral gap，並將剩餘 obstruction壓成 continuous neck-restoration與 source-contrast問題。

---

# 0. Round 23 handoff

Round 23 得到 dynamic intermittency comparison：

$$
\boxed{
(\log\mathfrak J)'
\le
-8\nu I_4
+
\sqrt{\mathfrak J-1}\,
\mathcal A_{\rm sel},
}
\tag{0.1}
$$

其中：

$$
I_4
=
\left\langle
|\nabla\log K|^2
\right\rangle_4.
$$

若 critical mass：

$$
\mu_Q
$$

具有 Poincaré constant：

$$
C_P,
$$

則：

$$
\boxed{
\mathfrak J-1
\le
4C_P
\mathfrak J
I_4.
}
\tag{0.2}
$$

所以需要：

$$
\boxed{
C_P(\mu_Q)
<\infty
}
$$

才能把 spatial Fisher smoothing轉成 intermittency restoring force。

但 nonlinear gauge本身不保證：

$$
C_P<\infty.
$$

Round 23 STOP：

$$
\boxed{
\text{STOP-C27}
=
\text{Critical-Mass Spectral-Gap / Source-Variance Leakage Gap}.
}
$$

---

# 1. Critical-mass equation

Round 21：

$$
\boxed{
\partial_t m
+
\operatorname{div}(bm)
=
\nu\Delta m
+
3(G-\bar G)m,
}
\tag{1.1}
$$

本輪簡寫：

$$
m=m_Q,
\qquad
b=b_Q,
\qquad
G=G_Q,
$$

以及：

$$
\bar G
=
\int
Gm\,dx.
$$

normalize：

$$
\boxed{
m\ge0,
\qquad
\int m\,dx=1.
}
\tag{1.2}
$$

這是一個 deterministic uniformly diffusive equation，但 drift：

$$
b_Q
=
u
-
3\frac{\chi_g}{r}n
$$

在 normalized form於：

$$
r\to0
$$

可能退化／顯得 singular。

因此所有 classical positivity statements必須附 coefficient-regularity條件，不能無條件套用。

---

# 2. Weighted perimeter

對 finite-perimeter set：

$$
A\subset\mathbb R^3,
$$

定義 critical-mass weighted perimeter：

$$
\boxed{
\operatorname{Per}_{\mu}(A)
=
\int_{\partial^\ast A}
m\,d\mathcal H^2.
}
\tag{2.1}
$$

smooth情況即：

$$
\operatorname{Per}_{\mu}(A)
=
\int_{\partial A}
m\,dS.
$$

令：

$$
a
=
\mu(A)
=
\int_A
m\,dx.
$$

---

# 3. Continuous Cheeger conductance

定義：

$$
\boxed{
h_Q(t)
=
\inf_{
0<\mu(A)<1
}
\frac{
\operatorname{Per}_{\mu}(A)
}{
\min\{
\mu(A),1-\mu(A)
\}
}.
}
\tag{3.1}
$$

dimension：

$$
[h_Q]
=
L^{-1}.
$$

NS scaling下：

$$
\boxed{
h_Q
\mapsto
\Lambda h_Q.
}
\tag{3.2}
$$

因此：

$$
\boxed{
\nu h_Q^2
}
$$

是一個 scale-critical mixing rate。

---

# 4. Continuous isoperimetric profile

比單一：

$$
h_Q
$$

更完整的 carrier是：

$$
\boxed{
\mathscr I_Q(s,t)
=
\inf_{
\mu(A)=s
}
\operatorname{Per}_{\mu}(A),
\qquad
s\in(0,1).
}
\tag{4.1}
$$

則：

$$
\boxed{
h_Q(t)
=
\inf_{0<s<1}
\frac{
\mathscr I_Q(s,t)
}{
\min\{s,1-s\}
}.
}
\tag{4.2}
$$

所以 connectivity本身可表示成一個 continuous mass-fraction profile：

$$
\boxed{
s\in(0,1)
\longmapsto
\mathscr I_Q(s,t).
}
$$

不需要 cluster graph。

---

# 5. Cheeger-to-Poincaré bridge

在標準 weighted Cheeger/Poincaré framework中：

$$
\boxed{
\lambda_1(\mu)
\ge
\frac{
h_Q^2
}{4},
}
\tag{5.1}
$$

所以：

$$
\boxed{
C_P
=
\lambda_1^{-1}
\le
\frac4{h_Q^2}.
}
\tag{5.2}
$$

因此 Round 23：

$$
\mathfrak J-1
\le
4C_P
\mathfrak J I_4
$$

可 sharpen 成：

$$
\boxed{
\mathfrak J-1
\le
\frac{
16
}{
h_Q^2
}
\mathfrak J I_4.
}
\tag{5.3}
$$

也就是：

$$
\boxed{
I_4
\ge
\frac{
h_Q^2
}{
16
}
\frac{
\mathfrak J-1
}{
\mathfrak J
}.
}
\tag{5.4}
$$

---

# 6. Conductance-based intermittency feedback

代入 Round 23：

$$
(\log\mathfrak J)'
\le
-8\nu I_4
+
\sqrt{\mathfrak J-1}
\mathcal A_{\rm sel},
$$

得到：

$$
\boxed{
(\log\mathfrak J)'
\le
-
\frac{
\nu h_Q^2
}{
2
}
\frac{
\mathfrak J-1
}{
\mathfrak J
}
+
\sqrt{\mathfrak J-1}
\mathcal A_{\rm sel}.
}
\tag{6.1}
$$

令：

$$
y
=
\sqrt{
\mathfrak J-1
}.
$$

則：

$$
\boxed{
y'
\le
-
\frac{
\nu h_Q^2
}{
4
}
y
+
\frac12
(1+y^2)
\mathcal A_{\rm sel}.
}
\tag{6.2}
$$

所以：

$$
\boxed{
\text{conductance mixing rate}
=
\frac{
\nu h_Q^2
}{4}.
}
\tag{6.3}
$$

---

# 7. Dimensionless conductance-feedback ratio

定義：

$$
\boxed{
\mathfrak R_{\rm cond}
=
\frac{
4\mathcal A_{\rm sel}
}{
\nu h_Q^2
}.
}
\tag{7.1}
$$

在 NS scaling下：

- $\mathcal A_{\rm sel}\mapsto\Lambda^2\mathcal A_{\rm sel}$；
- $h_Q^2\mapsto\Lambda^2h_Q^2$；

所以：

$$
\boxed{
\mathfrak R_{\rm cond}
}
$$

scale-invariant。

若：

$$
\boxed{
\mathfrak R_{\rm cond}<1,
}
\tag{7.2}
$$

則存在 Round 23 型 intermittency trapping window。

所以 feedback closure可濃縮成：

$$
\boxed{
\text{source-selection rate}
<
\text{critical-mass conductance mixing rate}.
}
$$

---

# 8. Material critical-mass cut

令：

$$
A_t
$$

由 drift：

$$
b
$$

advect：

$$
\frac{dX}{dt}
=
b(X,t).
$$

令：

$$
\boxed{
a(t)
=
\mu_t(A_t).
}
\tag{8.1}
$$

由 Reynolds transport及 (1.1)：

$$
\boxed{
a'
=
\nu
\int_{\partial A_t}
\partial_\eta m\,dS
+
3
\int_{A_t}
(G-\bar G)m\,dx.
}
\tag{8.2}
$$

其中：

$$
\eta
$$

為 outward normal。

---

# 9. Exact selection contrast across a cut

定義：

$$
\boxed{
\langle G\rangle_A
=
\frac1a
\int_A
Gm\,dx,
}
\tag{9.1}
$$

以及：

$$
\boxed{
\langle G\rangle_{A^c}
=
\frac1{1-a}
\int_{A^c}
Gm\,dx.
}
\tag{9.2}
$$

因：

$$
\bar G
=
a\langle G\rangle_A
+
(1-a)
\langle G\rangle_{A^c},
$$

有：

$$
\boxed{
\int_A
(G-\bar G)m\,dx
=
a(1-a)
\left[
\langle G\rangle_A
-
\langle G\rangle_{A^c}
\right].
}
\tag{9.3}
$$

所以：

$$
\boxed{
a'
=
\nu J_A
+
3a(1-a)
\Delta_A G,
}
\tag{9.4}
$$

其中：

$$
\boxed{
J_A
=
\int_{\partial A}
\partial_\eta m\,dS,
}
\tag{9.5}
$$

及：

$$
\boxed{
\Delta_A G
=
\langle G\rangle_A
-
\langle G\rangle_{A^c}.
}
\tag{9.6}
$$

---

# 10. Material-cut odds equation

令：

$$
\boxed{
\ell_A
=
\log
\frac{
a
}{
1-a
}.
}
\tag{10.1}
$$

則：

$$
\boxed{
\ell_A'
=
\nu
\frac{
J_A
}{
a(1-a)
}
+
3\Delta_A G.
}
\tag{10.2}
$$

命名：

$$
\boxed{
\textbf{Critical-Mass Cut Odds Equation}.
}
$$

所以兩個 critical-mass regions的相對 mass只被兩件事改變：

1. diffusive neck flux；
2. selection-rate contrast。

---

# 11. Diffusive neck score

若：

$$
m>0
$$

on：

$$
\Sigma=\partial A,
$$

則：

$$
J_A
=
\int_\Sigma
m\,
\partial_\eta\log m
\,dS.
$$

定義 weighted perimeter：

$$
P_A
=
\int_\Sigma
m\,dS,
$$

及 normal score：

$$
\boxed{
\kappa_1(A)
=
\frac1{P_A}
\int_\Sigma
m
\partial_\eta\log m
\,dS.
}
\tag{11.1}
$$

所以：

$$
\boxed{
J_A
=
P_A
\kappa_1(A).
}
\tag{11.2}
$$

因此 diffusion的 cut-to-cut communication strength具有兩個 factors：

$$
\boxed{
\text{neck mass }P_A
\times
\text{normal density score }\kappa_1.
}
$$

low conductance只壓低第一個 factor。

---

# 12. Material weighted-perimeter dynamics

令：

$$
\Sigma_t=\partial A_t
$$

smooth closed且由：

$$
b
$$

advect。

surface transport theorem：

$$
\frac d{dt}
\int_{\Sigma_t}
m\,dS
=
\int_{\Sigma_t}
\left[
D_t^b m
+
m\operatorname{div}_\Sigma b
\right]dS,
$$

其中：

$$
D_t^b
=
\partial_t+b\cdot\nabla.
$$

由 (1.1)：

$$
D_t^b m
=
\nu\Delta m
+
3(G-\bar G)m
-
m\operatorname{div}b.
$$

且：

$$
\operatorname{div}b
-
\operatorname{div}_\Sigma b
=
\eta^\top(\nabla b)\eta.
$$

故：

$$
\boxed{
P_A'
=
\int_{\Sigma}
\left[
\nu\Delta m
+
3(G-\bar G)m
-
m\,
\eta^\top(\nabla b)\eta
\right]dS.
}
\tag{12.1}
$$

---

# 13. Surface diffusion curvature

令 signed mean curvature：

$$
\boxed{
H_\Sigma
=
\operatorname{div}\eta.
}
\tag{13.1}
$$

在 surface：

$$
\Delta m
=
\partial_{\eta\eta}m
+
H_\Sigma
\partial_\eta m
+
\Delta_\Sigma m.
$$

closed surface上：

$$
\int_\Sigma
\Delta_\Sigma m\,dS=0.
$$

定義：

$$
\boxed{
\kappa_2(A)
=
\frac1{P_A}
\int_\Sigma
m
\left[
\partial_{\eta\eta}\log m
+
(\partial_\eta\log m)^2
+
H_\Sigma\partial_\eta\log m
\right]dS.
}
\tag{13.2}
$$

以及：

$$
\boxed{
B_n(A)
=
\frac1{P_A}
\int_\Sigma
m
\eta^\top(\nabla b)\eta
\,dS.
}
\tag{13.3}
$$

及 surface selection mean：

$$
\boxed{
G_\Sigma(A)
=
\frac1{P_A}
\int_\Sigma
Gm\,dS.
}
\tag{13.4}
$$

則：

$$
\boxed{
\frac{P_A'}{P_A}
=
\nu\kappa_2
+
3(G_\Sigma-\bar G)
-
B_n.
}
\tag{13.5}
$$

---

# 14. Exact material-cut conductance law

假設：

$$
a=\mu(A)\le\frac12.
$$

定義：

$$
\boxed{
\Phi_A
=
\frac{
P_A
}{
a
}.
}
\tag{14.1}
$$

由：

$$
\frac{a'}a
=
\nu
\Phi_A
\kappa_1
+
3(1-a)
\left[
\langle G\rangle_A
-
\langle G\rangle_{A^c}
\right],
$$

與 (13.5) 相減，

selection terms精確簡化為：

$$
G_\Sigma-\langle G\rangle_A.
$$

所以：

$$
\boxed{
\frac d{dt}
\log\Phi_A
=
\nu
\left[
\kappa_2
-
\Phi_A\kappa_1
\right]
+
3
\left[
G_\Sigma
-
\langle G\rangle_A
\right]
-
B_n.
}
\tag{14.2}
$$

命名：

$$
\boxed{
\textbf{Material-Cut Conductance Evolution Law}.
}
$$

這是本輪 strongest exact identity。

---

# 15. Three continuous mechanisms for neck collapse

Equation (14.2) 表示 material cut conductance可下降於三種機制。

## N1 — diffusion-curvature imbalance

$$
\boxed{
\kappa_2
<
\Phi_A\kappa_1.
}
$$

## N2 — selection interior bias

$$
\boxed{
G_\Sigma
<
\langle G\rangle_A.
}
$$

也就是 interior critical mass成長得比 boundary neck更快。

## N3 — normal drift deformation

$$
\boxed{
B_n>0.
}
$$

使 weighted boundary相對 interior mass被稀釋。

所以：

$$
\boxed{
\textbf{
positive diffusion does not by itself imply monotone conductance.
}
}
$$

---

# 16. Continuous cut profile rather than a single minimizer

Cheeger constant：

$$
h_Q
$$

是對所有 sets取 inf。

minimizing cut可能隨時間改變，

因此不應無證據地寫：

$$
h_Q'
=
\text{某單一 optimizer 的 derivative}.
$$

正確 carrier是 continuous family：

$$
\boxed{
A
\longmapsto
\left(
\mu(A),
P_A,
\kappa_1,
\kappa_2,
G_A,
G_\Sigma,
B_n
\right).
}
\tag{16.1}
$$

或 mass-fraction isoperimetric profile：

$$
\boxed{
\mathscr I_Q(s,t).
}
$$

optimizer switching是 variational envelope問題，

不等於 essential discreteness。

---

# 17. Conditional topological reconnection branch

若在某 interval：

- drift coefficients足夠 regular；
- lower-order source受控；
- uniform diffusion coefficient：
  $$
  \nu>0;
  $$

則標準 uniformly parabolic theory可給 heat-kernel positivity / Gaussian lower-bound類結果。

在這種 regular-coefficient branch，

非零：

$$
m(t_0)
$$

可在：

$$
t>t_0
$$

變成嚴格正 density。

因此：

$$
\boxed{
\text{exactly disconnected support}
}
$$

可被 viscosity消除。

但本路線不能在：

$$
r=0
$$

附近未控制：

$$
b_Q
$$

時無條件引用此 branch。

---

# 18. Strict positivity is not a quantitative conductance bound

即使：

$$
m(x)>0
\quad
\forall x,
$$

仍可能：

$$
\boxed{
h_Q\ll1.
}
$$

因此：

$$
\boxed{
\text{topological reconnection}
\neq
\text{quantitative mixing restoration}.
}
\tag{18.1}
$$

下面給一個 explicit continuous probability witness。

---

# 19. Two-Gaussian thin-neck witness

令：

$$
\phi_s(x)
=
\frac1{
(2\pi s^2)^{3/2}
}
\exp
\left(
-\frac{|x|^2}{2s^2}
\right).
$$

定義：

$$
\boxed{
m_{R,s}(x)
=
\frac12
\phi_s(x-Re_1)
+
\frac12
\phi_s(x+Re_1).
}
\tag{19.1}
$$

對所有：

$$
x,
$$

$$
m_{R,s}(x)>0.
$$

取 cut：

$$
A
=
\{x_1<0\}.
$$

由 symmetry：

$$
\mu(A)=\frac12.
$$

weighted perimeter：

$$
P_A
=
\int_{x_1=0}
m_{R,s}\,dS
$$

精確為：

$$
\boxed{
P_A
=
\frac1{
\sqrt{2\pi}\,s
}
\exp
\left(
-\frac{
R^2
}{
2s^2
}
\right).
}
\tag{19.2}
$$

所以：

$$
\boxed{
h(m_{R,s})
\le
\frac{
2
}{
\sqrt{2\pi}\,s
}
\exp
\left(
-\frac{
R^2
}{
2s^2
}
\right).
}
\tag{19.3}
$$

因此：

$$
\boxed{
R/s\to\infty
\Longrightarrow
h\to0
}
$$

即使 density everywhere positive。

---

# 20. Heat smoothing does not give a uniform rapid gap

若只考慮 heat evolution：

$$
\partial_tm=\nu\Delta m
$$

從：

$$
m_{R,s_0}
$$

出發，

則：

$$
s_t^2
=
s_0^2+2\nu t.
$$

所以：

$$
\boxed{
h(t)
\le
\frac{
2
}{
\sqrt{2\pi}\,s_t
}
\exp
\left(
-\frac{
R^2
}{
2s_t^2
}
\right).
}
\tag{20.1}
$$

對固定：

$$
t>0,
$$

令：

$$
R\to\infty,
$$

仍有：

$$
h(t)\to0.
$$

因此：

$$
\boxed{
\textbf{
uniform diffusion can make support positive instantly
without producing a separation-independent conductance lower bound.
}
}
\tag{20.2}
$$

quantitative reconnection timescale仍可依：

$$
R^2/\nu
$$

變得很大。

此 witness是 heat/probability model，不宣稱自身為 Navier–Stokes critical-mass solution。

---

# 21. Norm-level data cannot see arbitrary blob separation

translation-invariant norms：

$$
L^p,
\quad
\dot H^s,
\quad
\text{energy},
\quad
\text{critical amplitudes}
$$

本身不記錄兩個相同 localized structures之間的 physical separation。

Round 23 的 disjoint gauge-blob witness亦可任意平移兩 blobs。

所以不能只靠：

$$
\boxed{
\text{translation-invariant norm bounds}
}
$$

期待推出一個 geometry-independent：

$$
\boxed{
h_Q\ge h_\ast>0.
}
$$

還需要真正的：

$$
\boxed{
\text{mixing / localization / interaction geometry}.
}
$$

---

# 22. Selection can compete directly with neck repair

Cut odds equation：

$$
\ell_A'
=
\nu
\frac{
J_A
}{
a(1-a)
}
+
3\Delta_A G
$$

顯示：

若：

$$
\boxed{
3|\Delta_A G|
>
\nu
\left|
\frac{
J_A
}{
a(1-a)
}
\right|,
}
\tag{22.1}
$$

則 selection contrast可以在 instantaneous rate上壓過 diffusive cut exchange。

所以 viscosity是否能重新連接 critical mass，

不能只看：

$$
\nu>0.
$$

還必須比較：

$$
\boxed{
\text{cross-neck diffusion}
\quad\text{vs}\quad
\text{cross-cut growth selection}.
}
$$

---

# 23. Conductance restoration criterion for a material cut

由 (14.2)，若：

$$
\boxed{
\nu
\left[
\kappa_2
-
\Phi_A\kappa_1
\right]
+
3
\left[
G_\Sigma
-
\langle G\rangle_A
\right]
-
B_n
\ge0,
}
\tag{23.1}
$$

則：

$$
\boxed{
\Phi_A'(t)\ge0.
}
\tag{23.2}
$$

若對所有 near-minimizing cuts都能建立 uniform lower margin：

$$
\delta_{\rm neck}>0,
$$

則有希望推出：

$$
h_Q
$$

的 quantitative restoration。

本輪尚未得到這種 uniform estimate。

---

# 24. Conductance X-state

本輪可將 critical-mass mixing寫成：

$$
\boxed{
X_{\rm cond}
=
\left\langle
\mathscr I_Q(s),
h_Q,
\Phi_A,
\kappa_1,
\kappa_2,
\Delta_A G,
G_\Sigma-G_A,
B_n,
\mathcal A_{\rm sel}
\right\rangle.
}
\tag{24.1}
$$

其中：

- $s\in(0,1)$；
- $A$ 遍歷 measurable / finite-perimeter cuts；
- 所有 variables皆 continuous。

這是 Round 23 scalar：

$$
C_P
$$

的幾何展開。

---

# 25. STOP-C28 — Conductance-Restoration / Neck-Selection Gap

定義：

$$
\boxed{
\bot_X^{\mathrm{C28}}
=
\left\langle
\begin{array}{l}
\text{layer}
=
\mathrm{critical\text{-}mass\ conductance\ dynamics},
\\
\text{Cheeger\ carrier}
=
h_Q,
\\
\text{isoperimetric\ carrier}
=
\mathscr I_Q(s),
\\
\text{mixing\ rate}
=
\nu h_Q^2/4,
\\
\text{intermittency\ feedback}
=
\mathfrak R_{\rm cond}
=
4\mathcal A_{\rm sel}/(\nu h_Q^2),
\\
\text{material\ cut\ mass}
=
a'
=
\nu J_A
+
3a(1-a)\Delta_A G,
\\
\text{material\ conductance}
=
(\log\Phi_A)'
=
\nu(\kappa_2-\Phi_A\kappa_1)
+
3(G_\Sigma-G_A)
-
B_n,
\\
\text{topological\ reconnection}
\neq
\text{quantitative\ conductance},
\\
\text{strict\ positivity}
\not\Rightarrow
h_Q\ge h_\ast,
\\
\text{missing}
=
\mathrm{uniform\ control\ of\ neck\ diffusion,\ selection\ contrast,
and\ normal\ drift\ deformation},
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
\textbf{STOP-C28:
Critical-Mass Conductance-Restoration / Neck-Selection Gap}.
}
$$

---

# 26. 24/72 Ledger — Round 24

| Step | object | $B$ | $U$ | $O$ | $L$ | status |
|---|---|---|---|---|---|---|
| C307 | weighted perimeter | $\mathsf C$ | variational geometry | relational | $\mathsf F$ | FORM |
| C308 | Cheeger conductance $h_Q$ | $\mathsf C$ | global infimum | scalar | $\mathsf F$ | FORM |
| C309 | isoperimetric profile $\mathscr I_Q(s)$ | $\mathsf C$ | continuous mass fraction | profile | $\mathsf F$ | FORM |
| C310 | Cheeger–Poincaré bridge | $\mathsf C$ | global measure geometry | scalar | $\mathsf F$ | STANDARD |
| C311 | conductance feedback ODE | $\mathsf C$ | feedback | scalar | $\mathsf F$ | PROVED conditionally |
| C312 | scale-invariant $\mathfrak R_{\rm cond}$ | $\mathsf C$ | recognition | scalar | $\mathsf F$ | FORM |
| C313 | material cut mass law | $\mathsf C$ | transport/diffusion | relational | $\mathsf F$ | EXACT |
| C314 | selection contrast identity | $\mathsf C$ | measure | scalar | $\mathsf F$ | EXACT |
| C315 | cut odds equation | $\mathsf C$ | transport/selection | scalar | $\mathsf F$ | EXACT |
| C316 | material weighted-perimeter law | $\mathsf C$ | surface transport | relational | $\mathsf F$ | EXACT |
| C317 | surface diffusion curvature | $\mathsf C$ | surface geometry | $\mathsf X$ | $\mathsf F$ | EXACT |
| C318 | material-cut conductance law | $\mathsf C$ | coupled | targeted | $\mathsf F$ | EXACT |
| C319 | regular-coefficient positivity branch | $\mathsf C$ | parabolic smoothing | scalar | $\mathsf F$ | CONDITIONAL |
| C320 | positivity $\Rightarrow$ uniform conductance | $\mathsf C$ | measure geometry | scalar | $\mathsf F$ | REFUTED |
| C321 | two-Gaussian thin-neck witness | $\mathsf C$ | smooth density | relational | $\mathsf F$ | CONSTRUCTED |
| C322 | diffusion-only uniform rapid restoration | $\mathsf C$ | heat flow | targeted | $\mathsf F$ | REFUTED by separation family |
| C323 | uniform NS neck-restoration estimate | $\mathsf C$ | coupled NS | targeted | $\mathsf F$ | OPEN / STOP-C28 |

---

# 27. Continuous-versus-discrete status

conductance最常在 numerical / Markov-chain language中被畫成 graph。

但本輪全部使用：

- continuous probability density；
- finite-perimeter measurable sets；
- continuous mass fraction：
  $$
  s\in(0,1);
  $$
- continuous weighted surface measure；
- continuous surface transport。

沒有：

- graph vertices；
- cluster labels；
- component enumeration；
- discrete transition matrix。

因此：

$$
\boxed{
T_{\mathsf C\to\mathsf D}
=
\text{NOT YET REACHED}.
}
\tag{27.1}
$$

若未來為數值計算把：

$$
\mathscr I_Q(s)
$$

離散成 graph conductance，

那首先只是 numerical representation。

除非證明 continuous cut profile無法攜帶 closure所需資訊，

否則不算 essential：

$$
\mathsf C\to\mathsf D.
$$

---

# 28. Strongest results of Round 24

## R24-A — Conductance feedback rate

$$
\boxed{
y'
\le
-\frac{
\nu h_Q^2
}{4}
y
+
\frac12(1+y^2)\mathcal A_{\rm sel}.
}
$$

## R24-B — Exact cut odds dynamics

$$
\boxed{
\ell_A'
=
\nu\frac{J_A}{a(1-a)}
+
3\Delta_A G.
}
$$

## R24-C — Exact material-cut conductance dynamics

$$
\boxed{
(\log\Phi_A)'
=
\nu(\kappa_2-\Phi_A\kappa_1)
+
3(G_\Sigma-G_A)
-
B_n.
}
$$

## R24-D — Positivity is not mixing

$$
\boxed{
m>0
\not\Rightarrow
h_Q\ge h_\ast.
}
$$

## R24-E — Heat alone has a separation timescale

two-Gaussian model：

$$
\boxed{
h(t)
\lesssim
s_t^{-1}
\exp
\left(
-\frac{R^2}{2s_t^2}
\right),
\qquad
s_t^2=s_0^2+2\nu t.
}
$$

所以 large separation可讓 conductance restoration非常慢。

---

# 29. Next round — Nonlocal Cross-Blob Coupling

Round 24 顯示：

$$
\boxed{
\text{local diffusion}
}
$$

不能單獨提供 separation-independent gap。

但 Navier–Stokes不只是 local diffusion。

它還有：

- Biot–Savart velocity coupling；
- pressure Hessian；
- incompressibility；
- global quotient gauge。

所以下一輪直接測：

$$
\boxed{
\textbf{
Can nonlocal NS coupling provide a virtual connection
when critical mass has a thin or almost-empty neck?
}
}
$$

核心問題：

1. 兩個 high-mass blobs即使：
   $$
   h_Q\ll1,
   $$
   pressure / velocity field仍跨空間作用；

2. 把 source contrast：
   $$
   \Delta_A G
   $$
   拆成 local與 nonlocal cross-blob contribution；

3. 檢查 nonlocal pressure是否傾向同步兩 blob growth rate或反而可增加 selection contrast；

4. 定義 continuous cross-interaction kernel，不建立 blob graph；

5. 若 kernel interaction在 large separation以 algebraic tail衰減，而 conductance以 Gaussian/exponential neck衰減，則可能出現：
   $$
   \boxed{
   \text{nonlocal coupling dominates local neck communication}
   }
   $$
   的新 regime；

6. 這將重新接回 Round 04 的 pressure nonlocality，但以 conductance language重新攻擊。

---

# 30. External primary-source anchors

1. Sergey G. Bobkov, Michel Ledoux, *Weighted Poincaré-type inequalities for Cauchy and other convex measures*, arXiv:0906.1651.
   - weighted Poincaré / Cheeger-type measure geometry背景；
   - 本輪使用的 conductance-to-Poincaré route屬 classical weighted isoperimetric/spectral framework。

2. D. Kinzebulatov, Yu. A. Semenov, *Heat kernel bounds for parabolic equations with singular (form-bounded) vector fields*, arXiv:2103.11482.
   - uniformly elliptic parabolic equations在適當 drift/divergence assumptions下的 Gaussian heat-kernel lower/upper bound背景；
   - 本輪只用它支持「regular-coefficient branch可有 positivity / Gaussian propagation」的外部背景，不把其 assumptions無條件套到 $b_Q$。

本輪 material-cut mass law、odds law、weighted-perimeter dynamics、material-cut conductance law與 two-Gaussian thin-neck witness均為本文直接推導。

---

# 31. Commit state

$$
\boxed{
\begin{aligned}
\text{Route}
&=
\mathrm{Pure\ Continuous\ Critical\text{-}Mass\ Conductance\ Dynamics},
\\
\text{Essential }\mathsf C\to\mathsf D
&=
\mathrm{Not\ reached},
\\
\text{Connectivity carrier}
&=
\mathscr I_Q(s),\ h_Q,
\\
\text{Mixing rate}
&=
\nu h_Q^2/4,
\\
\text{Mass cut dynamics}
&=
\mathrm{diffusive\ neck\ flux}
+
\mathrm{selection\ contrast},
\\
\text{Conductance dynamics}
&=
\mathrm{diffusion\ curvature}
+
\mathrm{surface/interior\ selection}
+
\mathrm{normal\ drift},
\\
\text{Positivity}
&\neq
\mathrm{uniform\ spectral\ gap},
\\
\text{Diffusion-only restoration}
&=
\mathrm{separation\ dependent},
\\
\text{STOP-C28}
&=
\mathrm{Conductance\text{-}Restoration/Neck\text{-}Selection\ Gap},
\\
\text{Next}
&=
\mathrm{Nonlocal\ Cross\text{-}Blob\ Coupling}.
\end{aligned}
}
$$
