# NS × X 積分 × 24/72 範式實戰
## Round 39 — Pure Continuous Critical Endpoint / Dini–Hardy Compensation Route

- 日期：2026-08-17
- 版本：v0.1
- 狀態：Proof-Route Experiment / Continuous-Only Critical-Endpoint Branch
- canonical source：UTF-8 Markdown
- canonical math delimiters：inline `$...$`；display `$$...$$`
- 前一輪：`NS_X72_Round38_PureContinuous_TransportRiesz_TripleIncrementDepletion_v0.1_2026-08-17.md`
- 本輪目標：Round 38 將 transport–Riesz defect forcing壓成 triple-increment critical endpoint
  $$
  s_u+s_E+s_q=1.
  $$
  本輪研究這一個 derivative 如何在 $u$、$E_p$、$q$ 間連續分配，檢驗 defect viscosity、incompressibility、pressure div–curl compensation與 quadratic source structure能否提供缺少的 Dini/log gain。
- 非主張：本文沒有證明 critical Dini integral由 basic NS energy自動有限。本文證明的是：defect viscosity可支付完整一個 derivative；incompressibility提供 Hardy-space cancellation upgrade，但不自動提供 radial Dini summability；另一條把 derivative放到 $q$ 的 endpoint route又精確返回 Round 05 的 $H^1$ strain budget。

---

# 0. Round 38 handoff

Round 38 exact commutator pairing：

$$
\boxed{
\begin{aligned}
\left\langle
E,
[u\cdot\nabla,\mathcal T_0]q
\right\rangle
=
-\frac12
\operatorname{p.v.}
\iint
&
[
\delta_{xy}u
\cdot
\nabla K_0(x-y)
]
\\
&:
\delta_{xy}E
\,
\delta_{xy}q
\,dxdy.
\end{aligned}
}
\tag{0.1}
$$

其中：

$$
|\nabla K_0(z)|
\lesssim
|z|^{-4}.
$$

若：

$$
\frac1{p_u}
+
\frac1{p_E}
+
\frac1{p_q}
=
1,
$$

且 increments具有：

$$
r^{s_u},
\qquad
r^{s_E},
\qquad
r^{s_q},
$$

local absolute convergence需要：

$$
\boxed{
s_u+s_E+s_q>1.
}
$$

exact NS critical endpoint：

$$
\boxed{
s_u+s_E+s_q=1.
}
$$

Round 38 STOP：

$$
\boxed{
\text{STOP-C42}
=
\text{Triple-Increment Endpoint / Critical Dini Gap}.
}
$$

---

# 1. Defect viscosity pays one full derivative

Round 37 defect energy直接控制：

$$
\nabla E\in L^2.
$$

對 translation：

$$
\delta_zE(x)
=
E(x+z)-E(x),
$$

有：

$$
\boxed{
\|\delta_zE\|_2
\le
|z|
\|\nabla E\|_2.
}
\tag{1.1}
$$

所以在 Round 38 pairing中選：

$$
p_E=2,
$$

及：

$$
\boxed{
\frac1{p_u}
+
\frac1{p_q}
=
\frac12,
}
\tag{1.2}
$$

可把一個完整 radial power交給 defect viscosity。

---

# 2. Endpoint pair-Dini carrier

定義 translation modulus：

$$
\boxed{
\omega_{f,p}(r)
=
\sup_{|z|\le r}
\|\delta_zf\|_p.
}
\tag{2.1}
$$

由 (0.1)、(1.1)，near-diagonal pairing滿足：

$$
\boxed{
\begin{aligned}
\left|
\langle
E,\mathcal K_uq
\rangle_{\rm near}
\right|
\lesssim
\|\nabla E\|_2
\mathfrak D_{u,q}^{p_u,p_q}(\ell),
\end{aligned}
}
\tag{2.2}
$$

其中：

$$
\boxed{
\mathfrak D_{u,q}^{p_u,p_q}(\ell)
=
\int_0^\ell
\frac{
\omega_{u,p_u}(r)
\omega_{q,p_q}(r)
}{
r
}
dr.
}
\tag{2.3}
$$

命名：

$$
\boxed{
\textbf{Endpoint Pair-Dini Carrier}.
}
$$

所以 defect viscosity已把：

$$
s_E=1
$$

支付掉。

critical remainder變成：

$$
\boxed{
s_u+s_q=0
}
$$

上的 Dini summability問題。

---

# 3. Pair-Dini scale criticality

由：

$$
\frac1{p_u}
+
\frac1{p_q}
=
\frac12,
$$

NS scaling給：

$$
\omega_{u,p_u}
\mapsto
\Lambda^{1-3/p_u}
\omega_{u,p_u},
$$

$$
\omega_{q,p_q}
\mapsto
\Lambda^{4-3/p_q}
\omega_{q,p_q}.
$$

因此：

$$
\boxed{
\mathfrak D_{u,q}
\mapsto
\Lambda^{7/2}
\mathfrak D_{u,q}.
}
\tag{3.1}
$$

而：

$$
\|\nabla E\|_2
\mapsto
\Lambda^{7/2}
\|\nabla E\|_2.
$$

所以 product：

$$
\boxed{
\|\nabla E\|_2
\mathfrak D_{u,q}
}
$$

scale為：

$$
\Lambda^7,
$$

正好 matching defect-energy derivative。

因此 Pair-Dini Carrier本身不是 arbitrary subcritical artifact。

---

# 4. Weighted Dini trade law

對任意 measurable weight：

$$
w(r)>0,
$$

Cauchy–Schwarz給：

$$
\boxed{
\begin{aligned}
\mathfrak D_{u,q}(\ell)
\le{}&
\left[
\int_0^\ell
\omega_{u,p_u}(r)^2
w(r)
\frac{dr}{r}
\right]^{1/2}
\\
&\times
\left[
\int_0^\ell
\omega_{q,p_q}(r)^2
w(r)^{-1}
\frac{dr}{r}
\right]^{1/2}.
\end{aligned}
}
\tag{4.1}
$$

命名：

$$
\boxed{
\textbf{Continuous Dini-Gain Exchange Law}.
}
$$

所以 endpoint log gain不必平均分給：

$$
u
$$

與：

$$
q.
$$

它可以 continuous redistribution：

$$
w(r)
$$

在兩個 fields之間。

例如：

$$
w(r)
=
\left[
\log
\frac{e\ell}{r}
\right]^\alpha.
$$

可把 logarithmic burden偏向任一 source。

---

# 5. Translation continuity is not Dini summability

若：

$$
f\in L^p,
$$

則：

$$
\boxed{
\omega_{f,p}(r)\to0
}
$$

as：

$$
r\downarrow0.
$$

但：

$$
\omega(r)\to0
$$

本身不推出：

$$
\boxed{
\int_0^\ell
\omega(r)
\frac{dr}{r}
<
\infty.
}
$$

例如 abstract modulus：

$$
\boxed{
\omega(r)
=
\frac1{
\sqrt{
\log(e/r)
}
}
}
\tag{5.1}
$$

趨近零，

但：

$$
\boxed{
\int_0
\omega(r)^2
\frac{dr}{r}
=
\infty.
}
\tag{5.2}
$$

所以 mere $L^p$ translation continuity不會自動封住 critical Dini endpoint。

---

# 6. Incompressible pressure source as a div–curl sum

pressure source：

$$
\boxed{
q
=
|S|^2
-
\frac12|\omega|^2
=
\sum_{i,j}
(\partial_i u_j)
(\partial_j u_i).
}
\tag{6.1}
$$

對固定：

$$
j,
$$

令：

$$
A^{(j)}
=
\nabla u_j,
$$

以及：

$$
B^{(j)}
=
\partial_j u.
$$

則：

$$
\boxed{
\nabla\times A^{(j)}=0,
}
\tag{6.2}
$$

而 incompressibility給：

$$
\boxed{
\nabla\cdot B^{(j)}
=
\partial_j
(\nabla\cdot u)
=
0.
}
\tag{6.3}
$$

並：

$$
\boxed{
q
=
\sum_j
A^{(j)}
\cdot
B^{(j)}.
}
\tag{6.4}
$$

所以：

$$
q
$$

是 classical div–curl compensated product。

---

# 7. Hardy-space pressure-source upgrade

由 div–curl / incompressible pressure regularity theory，

在 smooth decaying branch：

$$
\boxed{
\|q\|_{\mathcal H^1}
\lesssim
\|\nabla u\|_2^2.
}
\tag{7.1}
$$

其中：

$$
\mathcal H^1
$$

是 real Hardy space，不是 Sobolev $H^1$。

這可被理解為：

$$
\boxed{
\text{incompressibility turns a generic }L^1\text{ quadratic source
into a compensated Hardy source}.
}
\tag{7.2}
$$

而 Riesz transforms在：

$$
\mathcal H^1
$$

上有 boundedness，

所以 pressure response的 signed cancellation確實比 generic quadratic source好。

---

# 8. Hardy gain is not a Dini gain

但：

$$
\mathcal H^1
$$

主要控制：

- cancellation；
- singular integral integrability；
- frequency/angular compensation。

Round 39 Pair-Dini要求：

$$
\boxed{
\int
\omega_{u,p_u}(r)
\omega_{q,p_q}(r)
\frac{dr}{r}.
}
$$

這是：

$$
\boxed{
\text{scale-local absolute translation summability}.
}
$$

兩者不是同一種 regularity。

因此：

$$
\boxed{
\textbf{
Hardy compensation can legalize pressure cancellation
without providing the missing radial Dini summability.
}
}
\tag{8.1}
$$

這和 incompressible pressure regularity研究中的 endpoint delicacy一致。

---

# 9. Exact pressure-source increment

直接由：

$$
q
=
|S|^2-\frac12|\omega|^2
$$

有：

$$
\boxed{
\delta q
=
(S_x+S_y):\delta S
-
\frac12
(\omega_x+\omega_y)\cdot\delta\omega.
}
\tag{9.1}
$$

因此：

$$
\boxed{
|\delta q|
\le
(
|S_x|+|S_y|
)
|\delta S|
+
\frac12
(
|\omega_x|+|\omega_y|
)
|\delta\omega|.
}
\tag{9.2}
$$

incompressibility本身沒有讓：

$$
\delta q
$$

自動多出一個 radial power。

真正 gain若存在，必須來自：

- strain/vorticity increment regularity；
- cancellation between the two quadratic pieces；
- stronger compensated function-space estimate。

---

# 10. Divergence-free local no-extra-power witness

沿用 Round 35 divergence-free polynomial field：

$$
\boxed{
\begin{aligned}
u_1
&=
-x_1
+
\frac12x_1^2
+
\frac12x_2^2,
\\
u_2
&=
-(1+x_1)x_2,
\\
u_3
&=
2x_3.
\end{aligned}
}
\tag{10.1}
$$

其：

$$
\nabla\cdot u=0,
$$

且 strain：

$$
\boxed{
S
=
\operatorname{diag}
(
-1+x_1,
-1-x_1,
2
).
}
\tag{10.2}
$$

vorticity：

$$
\omega
=
(0,0,-2x_2).
$$

所以：

$$
\boxed{
q
=
6
+
2x_1^2
-
2x_2^2.
}
\tag{10.3}
$$

在：

$$
x_2=0,
\qquad
x_1\ne0,
$$

沿：

$$
e_1
$$

small increment：

$$
h
$$

有：

$$
\boxed{
\delta_hq
=
4x_1h
+
2h^2.
}
\tag{10.4}
$$

所以 generically：

$$
\boxed{
|\delta_hq|
\asymp
|h|.
}
\tag{10.5}
$$

因此 purely algebraic incompressibility不會強迫：

$$
\delta q=o(r).
$$

此 witness不是 whole-space finite-energy NS solution。

---

# 11. Longitudinal incompressibility gives mean cancellation, not radial gain

取 affine divergence-free：

$$
u(x)=Ax,
\qquad
\operatorname{tr}A=0.
$$

則：

$$
\delta_zu
=
Az.
$$

longitudinal component：

$$
\boxed{
e\cdot\delta_zu
=
r
e^\top Ae.
}
\tag{11.1}
$$

對 sphere average：

$$
\boxed{
\int_{\mathbb S^2}
e^\top Ae
\,d\Omega
=
\frac{
\operatorname{tr}A
}{3}
|\mathbb S^2|
=
0.
}
\tag{11.2}
$$

但 pointwise：

$$
e^\top Ae
$$

generically nonzero。

所以 incompressibility提供：

$$
\boxed{
\text{angular mean cancellation}
}
$$

而不是 universal：

$$
\boxed{
o(r)
}
$$

longitudinal increment。

---

# 12. Pressure source is not independent of the defect

Round 38：

$$
H
=
\mathcal T_0q,
$$

以及：

$$
\boxed{
\mathcal T_0^\ast
\mathcal T_0
=
\frac23I.
}
\tag{12.1}
$$

因此：

$$
\boxed{
q
=
\frac32
\mathcal T_0^\ast H.
}
\tag{12.2}
$$

又：

$$
H=E-C.
$$

所以：

$$
\boxed{
q
=
\frac32
\mathcal T_0^\ast
(E-C).
}
\tag{12.3}
$$

命名：

$$
\boxed{
\textbf{Pressure-Source / Defect Compatibility Identity}.
}
$$

對：

$$
1<p<\infty,
$$

Riesz boundedness給：

$$
\boxed{
\|\delta_zq\|_p
\le
C_p
\left[
\|\delta_zE\|_p
+
\|\delta_zC\|_p
\right].
}
\tag{12.4}
$$

所以：

$$
q
$$

的 endpoint modulus不是新的 independent field。

它重新回到：

$$
\boxed{
\text{defect increments}
+
\text{cofactor/strain increments}.
}
$$

---

# 13. Cofactor increment returns to strain increments

Round 38 exact：

$$
\boxed{
\begin{aligned}
\delta C
={}&
\frac12
[
(S_x+S_y)\delta S
+
\delta S(S_x+S_y)
]
\\
&-
\frac13
[
(S_x+S_y):\delta S
]
I.
\end{aligned}
}
\tag{13.1}
$$

因此：

$$
\boxed{
|\delta C|
\le
C
(
|S_x|+|S_y|
)
|\delta S|.
}
\tag{13.2}
$$

所以：

$$
\boxed{
\text{pressure-source Dini gap}
\to
\text{defect Dini}
+
\text{strain-amplitude × strain-increment Dini}.
}
\tag{13.3}
$$

這再次把 endpoint route接回 Round 05 higher-gradient strain problem。

---

# 14. Alternative derivative allocation — put the derivative on $q$

Round 38 triple identity也可選：

$$
\boxed{
p_u=6,
\qquad
p_E=6,
\qquad
p_q=\frac32.
}
\tag{14.1}
$$

若：

$$
q\in W^{1,3/2},
$$

則：

$$
\boxed{
\|\delta_zq\|_{3/2}
\le
|z|
\|\nabla q\|_{3/2}.
}
\tag{14.2}
$$

因此：

$$
\boxed{
\begin{aligned}
|
\langle E,\mathcal K_uq\rangle_{\rm near}
|
\lesssim
\|\nabla q\|_{3/2}
\mathfrak D_{u,E}^{6,6}(\ell),
\end{aligned}
}
\tag{14.3}
$$

其中：

$$
\boxed{
\mathfrak D_{u,E}^{6,6}(\ell)
=
\int_0^\ell
\frac{
\omega_{u,6}(r)
\omega_{E,6}(r)
}{
r
}
dr.
}
\tag{14.4}
$$

所以 one-total-derivative可以連續地從：

$$
E
$$

移到：

$$
q.
$$

---

# 15. The $q$-derivative bill is exactly higher-gradient strain

由：

$$
q
=
|S|^2
-
\frac12|\omega|^2,
$$

有：

$$
\boxed{
\nabla q
=
2S:\nabla S
-
\omega\cdot\nabla\omega
}
\tag{15.1}
$$

in component notation。

因此：

$$
\boxed{
\|\nabla q\|_{3/2}
\le
2
\|S\|_6
\|\nabla S\|_2
+
\|\omega\|_6
\|\nabla\omega\|_2.
}
\tag{15.2}
$$

Sobolev + divergence-free Hodge：

$$
\|S\|_6
\lesssim
\|\nabla S\|_2,
$$

$$
\|\omega\|_6
\lesssim
\|\nabla\omega\|_2
\asymp
\|\nabla S\|_2.
$$

所以：

$$
\boxed{
\|\nabla q\|_{3/2}
\lesssim
\|\nabla S\|_2^2.
}
\tag{15.3}
$$

因此把 endpoint derivative交給：

$$
q
$$

並沒有創造新 reservoir。

它精確回到 Round 05 / 18：

$$
\boxed{
\text{strain }H^1
\text{ / palinstrophy-scale budget}.
}
$$

---

# 16. Critical Sobolev endpoint leaves a logarithmic translation gap

如果：

$$
u\in\dot H^1,
$$

Sobolev只給 critical：

$$
u\in L^6.
$$

同樣若：

$$
E\in\dot H^1,
$$

則：

$$
E\in L^6.
$$

但：

$$
L^6
$$

translation continuity本身不保證：

$$
\boxed{
\int_0^\ell
\frac{
\omega_{u,6}(r)
\omega_{E,6}(r)
}{
r
}
dr
<
\infty.
}
\tag{16.1}
$$

這是 endpoint Sobolev embedding留下的 logarithmic modulus gap。

---

# 17. Critical high-frequency modulus witness

令非零 smooth compactly supported：

$$
\phi,
\qquad
\Psi,
$$

並定義：

$$
\boxed{
f_N(x)
=
N^{1/2}
\phi(Nx),
}
\tag{17.1}
$$

$$
\boxed{
g_N(x)
=
N^{1/2}
\Psi(Nx).
}
\tag{17.2}
$$

則：

$$
\boxed{
\|\nabla f_N\|_2
\sim1,
\qquad
\|\nabla g_N\|_2
\sim1,
}
\tag{17.3}
$$

以及：

$$
\boxed{
\|f_N\|_6
\sim1,
\qquad
\|g_N\|_6
\sim1.
}
\tag{17.4}
$$

但對 fixed small：

$$
\ell>0,
$$

在：

$$
r\gtrsim N^{-1}
$$

的 range，

其 $L^6$ translation sup-moduli可保持 order one。

所以：

$$
\boxed{
\int_0^\ell
\frac{
\omega_{f_N,6}(r)
\omega_{g_N,6}(r)
}{
r
}
dr
\gtrsim
c\log N.
}
\tag{17.5}
$$

因此不存在 purely functional universal estimate：

$$
\boxed{
\mathfrak D_{f,g}^{6,6}
\le
C
\|\nabla f\|_2
\|\nabla g\|_2
}
\tag{17.6}
$$

with scale-independent：

$$
C.
$$

此 witness不是 NS-compatible field construction。

它只排除「critical $\dot H^1$ 自動給 Dini product」的 functional shortcut。

---

# 18. Smooth-time finiteness versus terminal spacetime blow-up

對 classical solution的任意 fixed：

$$
t<T,
$$

fields smooth，

所以：

$$
\boxed{
\mathfrak D_{u,q}(t;\ell)
<
\infty
}
$$

for sufficiently small：

$$
\ell.
$$

因此 Round 39 obstruction不是：

$$
\boxed{
\text{regular time spatial Dini legality}.
}
$$

真正問題是：

$$
\boxed{
\text{as }t\uparrow T,
\text{ Dini coefficient是否可失去 uniform / spacetime integrability}.
}
\tag{18.1}
$$

也就是：

$$
\boxed{
\int_0^T
\mathfrak D_{u,q}(t;\ell(t))^2dt
}
$$

或其 weighted版本是否可能 diverge。

這是一個 terminal critical concentration problem。

---

# 19. Viscosity gives smoothing, but not a future-uniform endpoint bound for free

heat operator在任何 strictly positive time increment後提供 spatial smoothing。

但 NS hypothetical blow-up問題要求：

$$
t\uparrow T
$$

時 uniform / integrable control。

如果 smoothing constants本身依賴於：

- critical norm；
- higher gradients；
- nonlinear forcing；

並在：

$$
T
$$

附近失控，

那「每個 $t<T$ 都 smooth」並不能封住 continuation gap。

所以：

$$
\boxed{
\textbf{
instantaneous parabolic smoothing
does not by itself give the terminal critical Dini budget.
}
}
\tag{19.1}
$$

---

# 20. Pressure endpoint warning from incompressible regularity theory

incompressibility確實能讓 pressure比 generic quadratic product更 regular。

但已知 pressure regularity theory也顯示：

- Sobolev / Besov upgrade在 interior fractional exponents非常有效；
- 某些 endpoint estimates失敗；
- endpoint counterexamples可由 high-frequency divergence-free fields構造。

所以 Round 39 不能僅由：

$$
\nabla\cdot u=0
$$

宣稱：

$$
\boxed{
\text{automatic endpoint Dini improvement}.
}
$$

這與 Sections 10、17 的 route-level witnesses一致。

---

# 21. Hardy–Dini mismatch

目前 incompressibility提供：

$$
\boxed{
q\in\mathcal H^1
}
$$

型 compensation。

Round 38–39 defect pairing需要：

$$
\boxed{
\text{critical translation Dini summability}.
}
$$

因此 remaining bridge可寫成：

$$
\boxed{
\mathcal H^1
\quad\stackrel{?}{\Longrightarrow}\quad
\text{usable transport–Riesz defect pairing endpoint}.
}
\tag{21.1}
$$

直接 implication false / unavailable at this level。

但 Hardy structure suggests a new dual route：

$$
\boxed{
\mathcal H^1
-
\mathrm{BMO}
}
$$

pairing，

而不是強迫：

$$
q
$$

進高 $L^p$ increment spaces。

這將是下一輪的新攻擊方向。

---

# 22. Dual commutator identity

因：

$$
D_u^\ast=-D_u,
$$

有：

$$
\boxed{
\begin{aligned}
\langle
E,
[D_u,\mathcal T_0]q
\rangle
&=
\left\langle
[D_u,\mathcal T_0^\ast]E,
q
\right\rangle.
\end{aligned}
}
\tag{22.1}
$$

所以如果：

$$
q\in\mathcal H^1,
$$

一條可能的 endpoint bypass是控制：

$$
\boxed{
[D_u,\mathcal T_0^\ast]E
}
$$

於：

$$
\mathrm{BMO}.
$$

這不需要先把：

$$
q
$$

放進：

$$
L^3,L^6
$$

等高 integrability spaces。

但 commutator-BMO estimate本身非常 delicate，

不能預設它由 basic energy成立。

---

# 23. Endpoint derivative-allocation simplex

Round 38 critical equation：

$$
\boxed{
s_u+s_E+s_q=1
}
$$

可視為 continuous simplex。

Round 39辨識兩個 endpoints：

## Endpoint E

$$
\boxed{
s_E=1,
\qquad
s_u+s_q=0.
}
$$

由 defect viscosity支付 derivative，

剩 Pair-Dini。

## Endpoint q

$$
\boxed{
s_q=1,
\qquad
s_u=s_E=0.
}
$$

由：

$$
\|\nabla q\|_{3/2}
\lesssim
\|\nabla S\|_2^2
$$

支付 derivative，

但回到 higher-gradient strain budget。

中間所有：

$$
0<s_E,s_q<1
$$

只是 continuous interpolation / redistribution。

沒有 discrete scale transition。

---

# 24. Obstruction confluence

Round 38：

$$
\text{transport–Riesz critical increment}
$$

Round 39 現在分裂後又匯流：

$$
\boxed{
\begin{aligned}
\text{put derivative on }E
&\to
\text{critical Dini modulus},
\\
\text{put derivative on }q
&\to
\text{Round 05 }H^1\text{ strain},
\\
\text{use incompressibility}
&\to
\text{Hardy cancellation but endpoint mismatch}.
\end{aligned}
}
\tag{24.1}
$$

所以：

$$
\boxed{
\textbf{
the endpoint obstruction is representation-stable under derivative redistribution.
}
}
\tag{24.2}
$$

---

# 25. STOP-C43 — Critical Dini / Hardy–Increment Mismatch Gap

$$
\boxed{
\begin{aligned}
\text{layer}
&=
\mathrm{critical\ endpoint\ closure},
\\
\text{defect viscosity}
&=
\mathrm{pays\ one\ full\ }E\mathrm{\ derivative},
\\
\text{remaining endpoint}
&=
\mathfrak D_{u,q}
=
\int
\omega_u\omega_q
\,dr/r,
\\
\text{Dini gain}
&=
\mathrm{continuously\ redistributable},
\\
\text{incompressibility}
&=
\mathrm{div\text{-}curl/Hardy\ compensation},
\\
\text{Hardy compensation}
&\neq
\mathrm{automatic\ Dini\ summability},
\\
\text{pressure source}
&=
\frac32
\mathcal T_0^\ast(E-C),
\\
\text{q-derivative route}
&\to
\|\nabla S\|_2^2
\text{ higher-gradient budget},
\\
\text{critical }H^1\to L^6
&=
\mathrm{insufficient\ for\ uniform\ Dini\ product},
\\
\text{regular times}
&=
\mathrm{Dini\ finite},
\\
\text{true danger}
&=
\mathrm{terminal\ spacetime\ Dini\ concentration},
\\
\text{missing}
&=
\mathrm{Hardy\text{-}BMO\ or\ parabolic\ endpoint\ mechanism
that\ controls\ the\ defect\ pairing\ at\ critical\ scale},
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
\textbf{STOP-C43:
Critical Dini / Hardy–Increment Mismatch Gap}.
}
$$

---

# 26. 24/72 Ledger — Round 39

| Step | object | $B$ | $U$ | $O$ | $L$ | status |
|---|---|---|---|---|---|---|
| C587 | defect one-derivative transfer | $\mathsf C$ | translation / viscosity | targeted | $\mathsf F$ | EXACT |
| C588 | Pair-Dini carrier $\mathfrak D_{u,q}$ | $\mathsf C$ | continuous modulus | scalar | $\mathsf F$ | FORM |
| C589 | Pair-Dini scaling | $\mathsf C$ | scaling | scalar | $\mathsf F$ | PROVED |
| C590 | weighted Dini exchange | $\mathsf C$ | continuous weight | profile | $\mathsf F$ | PROVED |
| C591 | translation continuity no-go | $\mathsf C$ | modulus | targeted | $\mathsf F$ | PROVED abstractly |
| C592 | div–curl pressure source | $\mathsf C$ | incompressibility | relational | $\mathsf F$ | EXACT |
| C593 | Hardy pressure-source upgrade | $\mathsf C$ | compensated compactness | scalar | $\mathsf F$ | STANDARD / PRIMARY-SOURCE ANCHOR |
| C594 | Hardy–Dini distinction | $\mathsf C$ | function-space map | targeted | $\mathsf F$ | IDENTIFIED |
| C595 | exact $q$ increment | $\mathsf C$ | quadratic source | relational | $\mathsf F$ | EXACT |
| C596 | divergence-free no-extra-power witness | $\mathsf C$ | local structural field | targeted | $\mathsf F$ | CONSTRUCTED |
| C597 | longitudinal angular-mean cancellation | $\mathsf C$ | sphere geometry | scalar | $\mathsf F$ | PROVED |
| C598 | source-defect compatibility | $\mathsf C$ | Riesz inversion | relational | $\mathsf F$ | EXACT |
| C599 | cofactor-to-strain increment return | $\mathsf C$ | tensor algebra | relational | $\mathsf F$ | EXACT |
| C600 | q-derivative allocation | $\mathsf C$ | endpoint redistribution | targeted | $\mathsf F$ | PROVED |
| C601 | $\|\nabla q\|_{3/2}$ budget | $\mathsf C$ | Sobolev/Hodge | scalar | $\mathsf F$ | PROVED |
| C602 | critical $H^1$ Dini no-go | $\mathsf C$ | scaling family | targeted | $\mathsf F$ | CONSTRUCTED |
| C603 | smooth-time versus terminal Dini | $\mathsf C$ | parabolic regularity | relational | $\mathsf F$ | CLARIFIED |
| C604 | dual commutator identity | $\mathsf C$ | Hardy–BMO duality route | targeted | $\mathsf F$ | EXACT |
| C605 | unconditional endpoint closure | $\mathsf C$ | coupled NS | targeted | $\mathsf F$ | OPEN / STOP-C43 |

---

# 27. Continuous-versus-discrete status

本輪所有 scale objects：

$$
r\in(0,\ell),
$$

以及 weight：

$$
w(r)>0
$$

皆 continuous。

derivative allocation：

$$
s_u+s_E+s_q=1
$$

也是 continuous simplex。

沒有：

- dyadic shell index；
- discrete regularity ladder；
- frequency lattice；
- endpoint state enumeration。

甚至 logarithmic gain也直接以：

$$
\int_0^\ell
\cdots
\frac{dr}{r}
$$

表示。

所以：

$$
\boxed{
T_{\mathsf C\to\mathsf D}
=
\text{NOT YET REACHED}.
}
$$

---

# 28. Strongest results of Round 39

## R39-A — defect-viscosity derivative transfer

$$
\boxed{
|\langle E,\mathcal K_uq\rangle_{\rm near}|
\lesssim
\|\nabla E\|_2
\int_0^\ell
\omega_{u,p_u}(r)
\omega_{q,p_q}(r)
\frac{dr}{r}.
}
$$

## R39-B — continuous Dini-gain exchange

$$
\boxed{
\mathfrak D_{u,q}
\le
\left(
\int
\omega_u^2w\,dr/r
\right)^{1/2}
\left(
\int
\omega_q^2w^{-1}\,dr/r
\right)^{1/2}.
}
$$

## R39-C — incompressible Hardy compensation

$$
\boxed{
q
=
\sum_j
\nabla u_j
\cdot
\partial_ju,
}
$$

with curl-free / divergence-free pairing，hence：

$$
\boxed{
\|q\|_{\mathcal H^1}
\lesssim
\|\nabla u\|_2^2.
}
$$

## R39-D — source-defect compatibility

$$
\boxed{
q
=
\frac32
\mathcal T_0^\ast
(E-C).
}
$$

## R39-E — q-derivative route returns to strain $H^1$

$$
\boxed{
\|\nabla q\|_{3/2}
\lesssim
\|\nabla S\|_2^2.
}
$$

## R39-F — endpoint Sobolev does not automatically give Dini

bounded critical：

$$
\dot H^1
\to
L^6
$$

norms can coexist with logarithmically growing translation-Dini modulus。

---

# 29. Next round — Hardy–BMO Dual Commutator Route

Round 39 顯示：

$$
\boxed{
q\in\mathcal H^1
}
$$

是 energy/enstrophy level真正由 incompressibility免費提供的 cancellation gain。

而 defect pairing exact dual form：

$$
\boxed{
\langle
E,
[D_u,\mathcal T_0]q
\rangle
=
\langle
[D_u,\mathcal T_0^\ast]E,
q
\rangle.
}
$$

所以下一輪直接研究：

1. 是否能控制：
   $$
   [D_u,\mathcal T_0^\ast]E
   $$
   於 BMO / Campanato；

2. Hardy–BMO duality能否避開 $q$ 的高 $L^p$ increment要求；

3. incompressibility是否讓 dual commutator再出現 skew / trace-free cancellation；

4. recent Riesz transport-commutator BMO no-go到底卡在哪個一般性 assumptions；

5. 我們這個特殊：
   $$
   E=H+C
   $$
   是否比 generic commutator有額外 null structure；

6. 若 BMO route失敗，回頭研究 parabolic endpoint Dini propagation；

7. 全程保持 continuous singular-integral / Campanato representation。

---

# 30. External primary-source anchors

1. Dong Li, Xiaoyi Zhang, *A regularity upgrade of pressure*, arXiv:2106.11852.
   - incompressibility可讓 pressure獲得超出 generic product rule的 Sobolev/Besov/Hardy regularity；
   - Theorem 1.2 gives Hardy-space control of second pressure derivatives from $W^{1,2}$ velocity；
   - the same paper constructs endpoint failures, so incompressibility不能被當成 automatic endpoint Besov/Dini gain。

2. Ruilin Hu, Phuoc-Tai Nguyen, Quoc-Hung Nguyen, Ping Zhang, *Quantitative bounds for bounded solutions to the Navier-Stokes equations in endpoint critical Besov spaces*, arXiv:2411.06483.
   - endpoint critical Besov regularity仍需 delicate quantitative analysis；用作 endpoint difficulty背景，不作本輪定理來源。

3. Elias Hess-Childs, Matthew Rosenzweig, Sylvia Serfaty, *Another look at regularity in transport-commutator estimates*, arXiv:2601.02326.
   - Riesz-type transport commutator的 velocity regularity / BMO endpoint限制背景。

本輪 Pair-Dini reduction、weighted Dini exchange、source-defect inversion、$\nabla q$ endpoint estimate、critical translation-modulus witness與 dual commutator identity均為本文直接推導。

---

# 31. Commit state

$$
\boxed{
\begin{aligned}
\text{Route}
&=
\mathrm{Pure\ Continuous\ Critical\ Endpoint/Dini\text{-}Hardy\ Compensation},
\\
\text{Essential }\mathsf C\to\mathsf D
&=
\mathrm{Not\ reached},
\\
\text{Defect viscosity}
&=
\mathrm{pays\ one\ derivative},
\\
\text{Remaining endpoint}
&=
\mathrm{Pair\text{-}Dini\ modulus},
\\
\text{Incompressibility gain}
&=
\mathrm{Hardy/div\text{-}curl\ cancellation},
\\
\text{Automatic Dini gain}
&=
\mathrm{false/unavailable},
\\
\text{q derivative}
&=
\mathrm{Round\ 05\ higher\text{-}gradient\ return},
\\
\text{Critical }H^1\text{ Sobolev}
&=
\mathrm{leaves\ logarithmic\ modulus\ gap},
\\
\text{STOP-C43}
&=
\mathrm{Critical\ Dini/Hardy\text{-}Increment\ Mismatch\ Gap},
\\
\text{Next}
&=
\mathrm{Hardy\text{-}BMO\ Dual\ Commutator\ Route}.
\end{aligned}
}
$$
