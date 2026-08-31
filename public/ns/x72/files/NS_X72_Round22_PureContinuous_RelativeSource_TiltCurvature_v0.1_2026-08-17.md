# NS × X 積分 × 24/72 範式實戰
## Round 22 — Pure Continuous Relative-Source Decomposition / Continuous Tilt-Curvature Route

- 日期：2026-08-17
- 版本：v0.1
- 狀態：Proof-Route Experiment / Continuous-Only Relative-Source Branch
- canonical source：UTF-8 Markdown
- canonical math delimiters：inline `$...$`；display `$$...$$`
- 前一輪：`NS_X72_Round21_PureContinuous_CriticalMass_Replicator_IntermittencyDynamics_v0.1_2026-08-17.md`
- 本輪目標：把 Round 21 的抽象 relative source
  $$
  \mathcal R_S
  $$
  與 intermittency production
  $$
  \mathcal P_{\rm sel}
  $$
  完整拆開。辨識 strain self-amplification、vorticity coupling、pressure Hessian、relative diffusion、quotient growth與 gauge maintenance各自如何進入 normalized-deformation intermittency；並將 discrete-looking $p=0,2,4$ moments重積成 continuous moment-order tilt
  $$
  p\in[0,\infty).
  $$
- 非主張：本文沒有證明 selection curvature無條件被 relative Fisher dissipation壓制。本文的主要成果是 exact tilt-curvature law、relative-source decomposition與 weighted-pressure commutator reduction。

---

# 0. Round 21 handoff

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

以及：

$$
K
=
K_S
=
\frac{|S|}{r}
$$

於：

$$
r>0,\quad |S|>0.
$$

critical mass：

$$
\boxed{
d\mu_0
=
d\mu_Q
=
\frac{r^3}{Q^3}dx.
}
\tag{0.1}
$$

strain-energy measure：

$$
\boxed{
d\mu_2
=
d\nu_S
=
\frac{r|S|^2}{W_S}dx.
}
\tag{0.2}
$$

Round 21 intermittency：

$$
\boxed{
\mathfrak J_S
=
\frac{
\mathbb E_{\mu_0}[K^4]
}{
\mathbb E_{\mu_0}[K^2]^2
}
=
1+\chi^2(\mu_2\|\mu_0).
}
\tag{0.3}
$$

並得到：

$$
\boxed{
\mathfrak J_S'
=
-2\nu\mathcal F_{\rm rel}
+
\mathcal P_{\rm sel}.
}
\tag{0.4}
$$

Round 21 STOP：

$$
\boxed{
\text{STOP-C25}
=
\text{Relative-Source / Critical-Mass Separation Gap}.
}
$$

---

# 1. Strain amplitude equation

Navier–Stokes strain equation：

$$
\boxed{
D_tS
=
\nu\Delta S
-
S^2
-
\frac14\omega\otimes\omega
+
\frac14|\omega|^2I
-
H_p,
}
\tag{1.1}
$$

其中：

$$
D_t
=
\partial_t+u\cdot\nabla,
$$

$$
H_p
=
\nabla^2p.
$$

令：

$$
e
=
|S|^2.
$$

因：

$$
\operatorname{tr}S=0,
$$

有：

$$
S:I=0.
$$

因此：

$$
\boxed{
D_te
=
\nu\Delta e
-
2\nu|\nabla S|^2
+
F_S,
}
\tag{1.2}
$$

其中：

$$
\boxed{
F_S
=
-6\det S
-
\frac12\omega^\top S\omega
-
2S:H_p.
}
\tag{1.3}
$$

這裡使用三維 trace-free identity：

$$
\operatorname{tr}(S^3)=3\det S.
$$

---

# 2. Quotient amplitude equation

Round 21 已有：

$$
\boxed{
D_tr
=
\nu\Delta r
-
\nu r|\nabla n|^2
+
\gamma_Qr
+
n\cdot\nabla\chi_g,
}
\tag{2.1}
$$

其中：

$$
n=\frac vr,
$$

$$
\boxed{
\gamma_Q
=
-
n^\top S n,
}
\tag{2.2}
$$

而：

$$
\chi_g
$$

為維持 nonlinear optimal gauge：

$$
\operatorname{div}(rv)=0
$$

的 gauge-maintenance potential。

---

# 3. Weighted strain density

定義：

$$
\boxed{
\zeta_S
=
r|S|^2
=
re.
}
\tag{3.1}
$$

則：

$$
W_S
=
\int
\zeta_Sdx.
$$

Round 21 common critical-mass drift：

$$
\boxed{
b_Q
=
u
-
3\frac{\chi_g}{r}n.
}
\tag{3.2}
$$

以及：

$$
\boxed{
G_Q
=
\gamma_Q-\nu K_D,
}
\tag{3.3}
$$

其中：

$$
\boxed{
K_D
=
\frac{
|\nabla v|^2+|\nabla r|^2
}{
r^2
}
=
2|\nabla\log r|^2
+
|\nabla n|^2.
}
\tag{3.4}
$$

---

# 4. Exact relative-source definition

在：

$$
\zeta_S>0
$$

定義：

$$
\boxed{
\mathcal R_S
=
\frac{
\partial_t\zeta_S
+
\operatorname{div}(b_Q\zeta_S)
-
\nu\Delta\zeta_S
}{
\zeta_S
}
-
3G_Q.
}
\tag{4.1}
$$

因此：

$$
\boxed{
\partial_t\zeta_S
+
\operatorname{div}(b_Q\zeta_S)
=
\nu\Delta\zeta_S
+
\left(
3G_Q+\mathcal R_S
\right)\zeta_S.
}
\tag{4.2}
$$

---

# 5. Exact decomposition of $\mathcal R_S$

直接代入 Sections 1–3，得到：

$$
\boxed{
\mathcal R_S
=
\mathcal R_{\rm self}
+
\mathcal R_{\rm vort}
+
\mathcal R_{\rm press}
+
\mathcal R_{\rm quot}
+
\mathcal R_{\rm diff}
+
\mathcal R_{\rm gauge},
}
\tag{5.1}
$$

其中：

$$
\boxed{
\mathcal R_{\rm self}
=
-6
\frac{
\det S
}{
|S|^2
},
}
\tag{5.2}
$$

$$
\boxed{
\mathcal R_{\rm vort}
=
-\frac12
\frac{
\omega^\top S\omega
}{
|S|^2
},
}
\tag{5.3}
$$

$$
\boxed{
\mathcal R_{\rm press}
=
-2
\frac{
S:H_p
}{
|S|^2
},
}
\tag{5.4}
$$

$$
\boxed{
\mathcal R_{\rm quot}
=
-2\gamma_Q,
}
\tag{5.5}
$$

以及：

$$
\boxed{
\begin{aligned}
\mathcal R_{\rm diff}
={}&
3\nu K_D
-
\nu|\nabla n|^2
-
2\nu
\frac{
|\nabla S|^2
}{
|S|^2
}
\\
&-
2\nu
\nabla\log r
\cdot
\nabla\log|S|^2,
\end{aligned}
}
\tag{5.6}
$$

及：

$$
\boxed{
\mathcal R_{\rm gauge}
=
-\frac2r
n\cdot\nabla\chi_g
-
\frac{3\chi_g}{r}
\left[
n\cdot\nabla\log|S|^2
+
\operatorname{div}n
\right].
}
\tag{5.7}
$$

所有 division formulas只在：

$$
r>0,\quad |S|>0
$$

使用；zero sets應回到 density equation (4.2)。

---

# 6. Gauge source simplifies through the nonlinear critical gauge

Round 20 nonlinear gauge：

$$
\operatorname{div}(r^2n)=0
$$

給：

$$
\boxed{
\operatorname{div}n
=
-2
n\cdot\nabla\log r.
}
\tag{6.1}
$$

又：

$$
K
=
\frac{|S|}{r}.
$$

所以：

$$
n\cdot\nabla\log|S|^2
+
\operatorname{div}n
=
2n\cdot\nabla\log K.
$$

故：

$$
\boxed{
\mathcal R_{\rm gauge}
=
-\frac2r
n\cdot\nabla\chi_g
-
\frac{
6\chi_g
}{
r
}
n\cdot\nabla\log K.
}
\tag{6.2}
$$

所以 dynamic gauge對 relative intermittency的影響只經：

- gauge-potential slope；
- normalized strain-rate slope；

進入。

---

# 7. Relative diffusion in normalized variables

在：

$$
|S|>0
$$

令 normalized strain orientation：

$$
\widehat S
=
\frac S{|S|}.
$$

則：

$$
\boxed{
\frac{
|\nabla S|^2
}{
|S|^2
}
=
|\nabla\log|S||^2
+
|\nabla\widehat S|^2.
}
\tag{7.1}
$$

使用：

$$
\nabla\log|S|
=
\nabla\log r
+
\nabla\log K,
$$

可將 (5.6) 化為：

$$
\boxed{
\mathcal R_{\rm diff}
=
2\nu
\left[
|\nabla n|^2
-
|\nabla\widehat S|^2
-
|\nabla\log K|^2
-
4
\nabla\log r
\cdot
\nabla\log K
\right].
}
\tag{7.2}
$$

因此 relative diffusion本身不是純負項。

common viscous anti-intermittency與 local strain-orientation / quotient-amplitude geometry會彼此耦合。

---

# 8. Continuous moment-order tilt

對任意 real：

$$
p\ge0
$$

且 moment finite時，定義：

$$
\boxed{
Z_p
=
\mathbb E_{\mu_0}[K^p].
}
\tag{8.1}
$$

以及：

$$
\boxed{
d\mu_p
=
\frac{
K^p
}{
Z_p
}
d\mu_0.
}
\tag{8.2}
$$

特殊值：

$$
\boxed{
\mu_0=\mu_Q,
}
$$

$$
\boxed{
\mu_2=\nu_S,
}
$$

以及：

$$
\boxed{
d\mu_4
=
\frac{
K^4
}{
\mathbb E_{\mu_0}[K^4]
}
d\mu_0.
}
\tag{8.3}
$$

所以 Round 21 的：

$$
0,\ 2,\ 4
$$

不是本質離散 moment orders。

它們是 continuous tilt family：

$$
\boxed{
p\in[0,\infty)
}
$$

中的三個 slices。

---

# 9. Relative Fisher term becomes a $\mu_4$ expectation

Round 21：

$$
f_S
=
\frac{
d\mu_2
}{
d\mu_0
}
=
\frac{
K^2
}{
Z_2
}.
$$

所以：

$$
\boxed{
\nabla f_S
=
2f_S
\nabla\log K.
}
\tag{9.1}
$$

relative Fisher：

$$
\mathcal F_{\rm rel}
=
\int
|\nabla f_S|^2d\mu_0.
$$

因此：

$$
\boxed{
\mathcal F_{\rm rel}
=
4
\mathfrak J_S
\mathbb E_{\mu_4}
\left[
|\nabla\log K|^2
\right].
}
\tag{9.2}
$$

所以 common viscosity anti-intermittency term：

$$
-2\nu\mathcal F_{\rm rel}
$$

精確變成：

$$
\boxed{
-8\nu
\mathfrak J_S
\mathbb E_{\mu_4}
\left[
|\nabla\log K|^2
\right].
}
\tag{9.3}
$$

---

# 10. Exact selection term in the $0$–$2$–$4$ tilt hierarchy

Round 21：

$$
\mathcal P_{\rm sel}
=
\int
f_S^2
\left[
3G_Q
+
2\mathcal R_S
-
2\overline C_S
+
3\overline G_Q
\right]
d\mu_0.
$$

其中：

$$
\overline G_Q
=
\mathbb E_{\mu_0}[G_Q],
$$

$$
\overline C_S
=
\mathbb E_{\mu_2}
[
3G_Q+\mathcal R_S
].
$$

因：

$$
\frac{
f_S^2
}{
\mathfrak J_S
}
d\mu_0
=
d\mu_4,
$$

得到：

$$
\boxed{
\begin{aligned}
\frac{
\mathcal P_{\rm sel}
}{
\mathfrak J_S
}
={}&
3
\left[
\langle G_Q\rangle_4
-
2\langle G_Q\rangle_2
+
\langle G_Q\rangle_0
\right]
\\
&+
2
\left[
\langle\mathcal R_S\rangle_4
-
\langle\mathcal R_S\rangle_2
\right],
\end{aligned}
}
\tag{10.1}
$$

其中：

$$
\langle A\rangle_p
=
\mathbb E_{\mu_p}[A].
$$

命名：

$$
\boxed{
\textbf{Tilt-Selection Decomposition}.
}
$$

---

# 11. Exact logarithmic intermittency law

由：

$$
\mathfrak J_S'
=
-2\nu\mathcal F_{\rm rel}
+
\mathcal P_{\rm sel}
$$

除以：

$$
\mathfrak J_S>0
$$

並使用 Sections 9–10：

$$
\boxed{
\begin{aligned}
\frac d{dt}
\log\mathfrak J_S
={}&
-8\nu
\langle
|\nabla\log K|^2
\rangle_4
\\
&+
3
\left[
\langle G_Q\rangle_4
-
2\langle G_Q\rangle_2
+
\langle G_Q\rangle_0
\right]
\\
&+
2
\left[
\langle\mathcal R_S\rangle_4
-
\langle\mathcal R_S\rangle_2
\right].
\end{aligned}
}
\tag{11.1}
$$

這是本輪 strongest exact identity。

---

# 12. Continuous tilt derivatives

令：

$$
L
=
\log K.
$$

對任意不顯式依賴 $p$ 的 observable：

$$
A(x,t),
$$

exponential-tilt calculus給：

$$
\boxed{
\frac d{dp}
\langle A\rangle_p
=
\operatorname{Cov}_{\mu_p}(A,L).
}
\tag{12.1}
$$

再微分：

$$
\boxed{
\frac{d^2}{dp^2}
\langle A\rangle_p
=
\operatorname{Cov}_{\mu_p}
\left(
A,
(L-\langle L\rangle_p)^2
\right).
}
\tag{12.2}
$$

所以 tilt-order curvature本身是一個 covariance。

---

# 13. Continuous Tilt-Curvature Intermittency Law

由 fundamental theorem of calculus：

$$
\boxed{
\begin{aligned}
&
\langle G_Q\rangle_4
-
2\langle G_Q\rangle_2
+
\langle G_Q\rangle_0
\\
&=
\int_0^2
\int_s^{s+2}
\operatorname{Cov}_{\mu_\tau}
\left(
G_Q,
(L-\langle L\rangle_\tau)^2
\right)
d\tau ds.
\end{aligned}
}
\tag{13.1}
$$

以及：

$$
\boxed{
\langle\mathcal R_S\rangle_4
-
\langle\mathcal R_S\rangle_2
=
\int_2^4
\operatorname{Cov}_{\mu_p}
(
\mathcal R_S,L
)
dp.
}
\tag{13.2}
$$

代入 (11.1)：

$$
\boxed{
\begin{aligned}
(\log\mathfrak J_S)'
={}&
-8\nu
\langle
|\nabla L|^2
\rangle_4
\\
&+
3
\int_0^2
\int_s^{s+2}
\operatorname{Cov}_{\mu_\tau}
\left(
G_Q,
(L-\langle L\rangle_\tau)^2
\right)
d\tau ds
\\
&+
2
\int_2^4
\operatorname{Cov}_{\mu_p}
(
\mathcal R_S,L
)
dp.
\end{aligned}
}
\tag{13.3}
$$

命名：

$$
\boxed{
\textbf{Continuous Tilt-Curvature Intermittency Law}.
}
$$

所以 intermittency growth需要兩種 continuous moment-order bias：

1. critical-mass growth field對 log-rate dispersion的 positive tilt curvature；
2. strain-specific relative source對 log normalized-rate的 positive covariance。

---

# 14. Intermittency growth necessity

若：

$$
(\log\mathfrak J_S)'>0,
$$

則必有：

$$
\boxed{
\begin{aligned}
&
3
\int_0^2
\int_s^{s+2}
\operatorname{Cov}_{\mu_\tau}
\left(
G_Q,
(L-\langle L\rangle_\tau)^2
\right)
d\tau ds
\\
&+
2
\int_2^4
\operatorname{Cov}_{\mu_p}
(
\mathcal R_S,L
)
dp
\\
&>
8\nu
\langle
|\nabla L|^2
\rangle_4.
\end{aligned}
}
\tag{14.1}
$$

所以 normalized strain intermittency要增長，

NS selection/source在 continuous moment-order axis上的偏向，必須打敗 spatial relative-Fisher smoothing。

---

# 15. Pressure source under a general tilt

定義 raw $p$-moment：

$$
\boxed{
\mathcal M_p
=
\int
r^{3-p}
|S|^pdx
=
Q^3Z_p.
}
\tag{15.1}
$$

由：

$$
\mathcal R_{\rm press}
=
-2
\frac{
S:H_p
}{
|S|^2
},
$$

得到：

$$
\boxed{
\langle
\mathcal R_{\rm press}
\rangle_p
=
-\frac2{\mathcal M_p}
\int
w_p
S:H_p\,dx,
}
\tag{15.2}
$$

其中：

$$
\boxed{
w_p
=
r^{3-p}
|S|^{p-2}.
}
\tag{15.3}
$$

特殊：

$$
\boxed{
w_2=r,
}
$$

$$
\boxed{
w_4=\frac{|S|^2}{r}.
}
$$

---

# 16. Weighted pressure cancellation identity

對任意 smooth scalar weight：

$$
w,
$$

使用：

$$
S:H_p
=
\partial_j u_i
\partial_{ij}p
$$

與：

$$
\nabla\cdot u=0,
$$

integration by parts給：

$$
\boxed{
\int
w
S:H_p\,dx
=
\int
u\cdot
\left[
(\Delta p)I-H_p
\right]
\nabla w\,dx.
}
\tag{16.1}
$$

當：

$$
w\equiv1,
$$

右側為零，恢復 global pressure cancellation：

$$
\boxed{
\int
S:H_pdx=0.
}
$$

所以 weighted relative-source中的 pressure並不是 raw bulk term。

它完全轉化成：

$$
\boxed{
\text{pressure anisotropy}
\times
\text{tilt-weight gradient}.
}
$$

命名：

$$
\boxed{
\textbf{Weighted Pressure-Commutator Identity}.
}
$$

---

# 17. Pressure contribution to intermittency is a weight-geometry contrast

由 Sections 15–16：

$$
\boxed{
\begin{aligned}
\langle
\mathcal R_{\rm press}
\rangle_4
={}&
-\frac2{\mathcal M_4}
\int
u\cdot
\left[
(\Delta p)I-H_p
\right]
\nabla
\left(
\frac{|S|^2}{r}
\right)
dx,
\\
\langle
\mathcal R_{\rm press}
\rangle_2
={}&
-\frac2{\mathcal M_2}
\int
u\cdot
\left[
(\Delta p)I-H_p
\right]
\nabla r
\,dx.
\end{aligned}
}
\tag{17.1}
$$

因此：

$$
\boxed{
\langle
\mathcal R_{\rm press}
\rangle_4
-
\langle
\mathcal R_{\rm press}
\rangle_2
}
$$

只看到：

> pressure anisotropy對 high-normalized-strain tilt weight與普通 strain-energy weight的不同作用。

這是 Round 04 pressure nonlocality在 dynamic-intermittency language中的 return。

---

# 18. Self-amplification source under the tilt hierarchy

由：

$$
\mathcal R_{\rm self}
=
-6
\frac{\det S}{|S|^2},
$$

有：

$$
\boxed{
\langle
\mathcal R_{\rm self}
\rangle_p
=
-\frac6{\mathcal M_p}
\int
r^{3-p}
|S|^{p-2}
\det S\,dx.
}
\tag{18.1}
$$

特別：

$$
\boxed{
\langle
\mathcal R_{\rm self}
\rangle_2
=
-\frac6{W_S}
\int
r\det S\,dx,
}
\tag{18.2}
$$

以及：

$$
\boxed{
\langle
\mathcal R_{\rm self}
\rangle_4
=
-\frac6{\mathcal I_0}
\int
\frac{|S|^2}{r}
\det S\,dx.
}
\tag{18.3}
$$

所以：

$$
\boxed{
\langle
\mathcal R_{\rm self}
\rangle_4
-
\langle
\mathcal R_{\rm self}
\rangle_2
}
$$

精確測量：

> strain self-amplification是否 preferentially集中在 high normalized-strain-rate regions。

---

# 19. Vorticity-coupling source under the tilt hierarchy

同理：

$$
\boxed{
\langle
\mathcal R_{\rm vort}
\rangle_p
=
-\frac1{2\mathcal M_p}
\int
r^{3-p}
|S|^{p-2}
\omega^\top S\omega
\,dx.
}
\tag{19.1}
$$

所以：

$$
\boxed{
\langle
\mathcal R_{\rm vort}
\rangle_4
-
\langle
\mathcal R_{\rm vort}
\rangle_2
}
$$

測量：

> vortex-stretching interaction是否 preferentially落在 high-$K$ tail。

Round 18–19 的 obstruction confluence因此在 $\mathfrak J_S$ dynamics中直接重現。

---

# 20. Quotient-growth source under the tilt hierarchy

由：

$$
\mathcal R_{\rm quot}
=
-2\gamma_Q,
$$

其 contribution：

$$
\boxed{
\langle
\mathcal R_{\rm quot}
\rangle_4
-
\langle
\mathcal R_{\rm quot}
\rangle_2
=
-2
\left[
\langle\gamma_Q\rangle_4
-
\langle\gamma_Q\rangle_2
\right].
}
\tag{20.1}
$$

因此若 high-normalized-strain regions更偏向：

$$
\gamma_Q>0
$$

的 compressive quotient-growth geometry，

它會直接成為 intermittency selection source。

---

# 21. Diffusion and gauge terms remain genuinely relational

由 (7.2)：

$$
\mathcal R_{\rm diff}
$$

包含：

$$
|\nabla n|^2,
$$

$$
|\nabla\widehat S|^2,
$$

$$
|\nabla\log K|^2,
$$

以及：

$$
\nabla\log r\cdot\nabla\log K.
$$

而：

$$
\mathcal R_{\rm gauge}
$$

由 (6.2) 只依賴：

$$
n\cdot\nabla\chi_g,
$$

及：

$$
n\cdot\nabla\log K.
$$

所以剩餘 relative source不是 scalar amplitude problem。

它是：

$$
\boxed{
\text{orientation}
+
\text{rate gradient}
+
\text{quotient amplitude}
+
\text{gauge feedback}
}
$$

的 relational field。

---

# 22. Three exact pressure/self/vorticity conclusions

本輪對三個主要 nonlinear source得到：

## P1 — pressure

$$
\boxed{
\text{unweighted pressure cancels;
relative pressure survives only as a weight-gradient commutator}.
}
$$

## P2 — strain self-amplification

$$
\boxed{
\text{intermittency sees whether determinant production is biased toward high }K.
}
$$

## P3 — vortex stretching

$$
\boxed{
\text{intermittency sees whether }\omega^\top S\omega
\text{ is biased toward high }K.
}
$$

因此：

$$
\boxed{
\textbf{
intermittency is not caused merely by large nonlinear production;
it requires nonlinear production to be preferentially organized
in the high normalized-deformation tail.
}
}
\tag{22.1}
$$

---

# 23. Conditional self-closing branch

由 (13.3)，若：

$$
\boxed{
\begin{aligned}
&
3
\int_0^2
\int_s^{s+2}
\operatorname{Cov}_{\mu_\tau}
\left(
G_Q,
(L-\langle L\rangle_\tau)^2
\right)
d\tau ds
\\
&+
2
\int_2^4
\operatorname{Cov}_{\mu_p}
(
\mathcal R_S,L
)
dp
\\
&\le
8\nu
\langle
|\nabla L|^2
\rangle_4,
\end{aligned}
}
\tag{23.1}
$$

則：

$$
\boxed{
\mathfrak J_S'(t)\le0.
}
\tag{23.2}
$$

所以 Pure-C dynamic intermittency closure已經被壓成一條單一 continuous tilt-covariance inequality。

---

# 24. Why this is not yet QED

目前沒有從 ordinary NS energy / enstrophy / critical quotient control無條件推出 (23.1)。

特別：

- determinant self-amplification可能偏向 high-$K$ regions；
- vortex stretching可能偏向 high-$K$ regions；
- pressure anisotropy可能與 tilt-weight gradient強相關；
- gauge feedback可能維持 high-$K$ tail。

所以：

$$
\boxed{
\text{viscous relative Fisher smoothing exists,
but source organization can still defeat it}.
}
$$

---

# 25. STOP-C26 — Continuous Tilt-Selection / Relative-Source Gap

定義：

$$
\boxed{
\bot_X^{\mathrm{C26}}
=
\left\langle
\begin{array}{l}
\text{layer}
=
\mathrm{continuous\ moment\text{-}order\ intermittency},
\\
\text{tilt\ family}
=
\mu_p,\quad p\in[0,\infty),
\\
\text{spatial\ anti\text{-}intermittency}
=
8\nu\langle|\nabla\log K|^2\rangle_4,
\\
\text{growth\text{-}selection\ curvature}
=
\partial_p^2\langle G_Q\rangle_p,
\\
\text{relative\ source\ bias}
=
\partial_p\langle\mathcal R_S\rangle_p,
\\
\text{pressure}
=
\mathrm{weight\text{-}gradient\ commutator},
\\
\text{self\text{-}amplification}
=
\mathrm{high\text{-}K\ determinant\ bias},
\\
\text{vorticity\ coupling}
=
\mathrm{high\text{-}K\ stretching\ bias},
\\
\text{missing}
=
\mathrm{unconditional\ domination\ of\ continuous\ tilt\ bias
by\ relative\ Fisher\ smoothing},
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
\textbf{STOP-C26:
Continuous Tilt-Selection / Relative-Source Gap}.
}
$$

---

# 26. 24/72 Ledger — Round 22

| Step | object | $B$ | $U$ | $O$ | $L$ | status |
|---|---|---|---|---|---|---|
| C276 | strain-amplitude PDE | $\mathsf C$ | differential | relational | $\mathsf F$ | EXACT |
| C277 | exact relative source $\mathcal R_S$ | $\mathsf C$ | coupled | $\mathsf X$ | $\mathsf F$ | EXACT |
| C278 | six-source decomposition | $\mathsf C$ | relational | $\mathsf X$ | $\mathsf F$ | EXACT |
| C279 | gauge-source simplification | $\mathsf C$ | nonlinear gauge | targeted | $\mathsf F$ | EXACT |
| C280 | normalized diffusion decomposition | $\mathsf C$ | differential | relational | $\mathsf F$ | EXACT |
| C281 | continuous tilt $\mu_p$ | $\mathsf C$ | continuous $p$ | profile | $\mathsf F$ | FORM |
| C282 | relative Fisher as $\mu_4$ expectation | $\mathsf C$ | measure | scalar | $\mathsf F$ | EXACT |
| C283 | tilt-selection decomposition | $\mathsf C$ | measure hierarchy | scalar | $\mathsf F$ | EXACT |
| C284 | log-intermittency law | $\mathsf C$ | coupled | scalar | $\mathsf F$ | EXACT |
| C285 | tilt derivative covariance | $\mathsf C$ | continuous $p$ | relational | $\mathsf F$ | EXACT |
| C286 | continuous tilt-curvature law | $\mathsf C$ | continuous moment order | profile | $\mathsf F$ | EXACT |
| C287 | weighted pressure commutator | $\mathsf C$ | nonlocal/weight | relational | $\mathsf F$ | EXACT |
| C288 | determinant high-$K$ bias | $\mathsf C$ | strain geometry | targeted | $\mathsf F$ | EXACT reformulation |
| C289 | stretching high-$K$ bias | $\mathsf C$ | strain-vorticity | targeted | $\mathsf F$ | EXACT reformulation |
| C290 | unconditional tilt-bias domination | $\mathsf C$ | — | targeted | $\mathsf F$ | OPEN / STOP-C26 |

---

# 27. Continuous-versus-discrete status

本輪最容易看似離散的量：

$$
p=0,2,4
$$

再次被重積為：

$$
\boxed{
p\in[0,\infty)
}
$$

的 continuous moment-order axis。

而：

$$
\mathfrak J_S
$$

growth最後寫成：

- physical-space Fisher gradient；
- moment-order covariance curvature。

因此仍沒有必要引入：

- integer moment hierarchy；
- discrete tail bins；
- atomic probability states；
- stochastic transition kernel。

所以：

$$
\boxed{
B=\mathsf C,
\qquad
L=\mathsf F,
}
$$

且：

$$
\boxed{
T_{\mathsf C\to\mathsf D}
=
\text{NOT YET REACHED}.
}
\tag{27.1}
$$

---

# 28. Strongest results of Round 22

## R22-A — exact relative-source decomposition

$$
\boxed{
\mathcal R_S
=
\mathcal R_{\rm self}
+
\mathcal R_{\rm vort}
+
\mathcal R_{\rm press}
+
\mathcal R_{\rm quot}
+
\mathcal R_{\rm diff}
+
\mathcal R_{\rm gauge}.
}
$$

## R22-B — exact log-intermittency law

$$
\boxed{
\begin{aligned}
(\log\mathfrak J_S)'
={}&
-8\nu
\langle|\nabla\log K|^2\rangle_4
\\
&+
3
\left[
\langle G_Q\rangle_4
-
2\langle G_Q\rangle_2
+
\langle G_Q\rangle_0
\right]
\\
&+
2
\left[
\langle\mathcal R_S\rangle_4
-
\langle\mathcal R_S\rangle_2
\right].
\end{aligned}
}
$$

## R22-C — continuous moment-order formulation

$$
\boxed{
\text{finite differences in }p
=
\text{continuous covariance integrals in }p.
}
$$

## R22-D — weighted pressure transmutation

$$
\boxed{
\int
wS:H_p
=
\int
u\cdot[(\Delta p)I-H_p]\nabla w.
}
$$

所以 pressure relative source只經 tilt-weight gradients留下。

---

# 29. Next round — confluence-feedback closure test

下一輪不再繼續擴張 source taxonomy。

直接把 Round 19 的：

$$
\lambda_2^+,
\quad
(-\det S)_+,
\quad
\chi_C
$$

代入 Round 22 的 tilt-covariance law。

核心問題：

1. dangerous determinant equivalence是否讓：
   $$
   \mathcal R_{\rm self}
   $$
   的 positive high-$K$ bias可直接用 confluence ratio控制；

2. middle-strain floor是否限制：
   $$
   \partial_p\langle\mathcal R_{\rm self}\rangle_p;
   $$

3. vorticity coupling是否可和 determinant source在 tilt difference中部分抵消或同號化；

4. weighted pressure commutator能否由：
   $$
   |\nabla\log K|
   $$
   的 relative Fisher term吸收；

5. 若這幾項能形成：
   $$
   \text{source bias}
   \le
   c\nu
   \langle|\nabla\log K|^2\rangle_4
   $$
   ，將第一次形成真正的 self-closing feedback candidate。

---

# 30. External primary-source anchors

1. Evan Miller, *On the interaction of strain and vorticity for solutions of the Navier--Stokes equation*, arXiv:2407.02691.
   - strain–vorticity interaction；
   - projected strain structure；
   - global enstrophy identities與 nonlinear depletion背景。

2. Evan Miller, *A regularity criterion for the Navier-Stokes equation involving only the middle eigenvalue of the strain tensor*, arXiv:1710.05569.
   - positive middle-eigenvalue channel的 scale-critical regularity背景。

本輪 relative-source decomposition、continuous tilt calculus、log-intermittency law與 weighted pressure-commutator identity均為本文直接推導。

---

# 31. Commit state

$$
\boxed{
\begin{aligned}
\text{Route}
&=
\mathrm{Pure\ Continuous\ Relative\text{-}Source/Tilt\ Curvature},
\\
\text{Essential }\mathsf C\to\mathsf D
&=
\mathrm{Not\ reached},
\\
\text{Normalized rate}
&=
K=|S|/|v|,
\\
\text{Tilt family}
&=
\mu_p,\ p\in[0,\infty),
\\
\text{Spatial smoothing}
&=
8\nu\langle|\nabla\log K|^2\rangle_4,
\\
\text{Moment-order danger}
&=
\mathrm{selection\ curvature}
+
\mathrm{relative\ source\ covariance},
\\
\text{Pressure source}
&=
\mathrm{weight\text{-}gradient\ commutator},
\\
\text{Self/vorticity source}
&=
\mathrm{high\text{-}K\ preferential\ bias},
\\
\text{STOP-C26}
&=
\mathrm{Continuous\ Tilt\text{-}Selection/Relative\text{-}Source\ Gap},
\\
\text{Next}
&=
\mathrm{Confluence\text{-}Feedback\ Closure\ Test}.
\end{aligned}
}
$$
