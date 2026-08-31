# NS × X 積分 × 24/72 範式實戰
## Round 34 — Pure Continuous Cancellation-Budget Dynamics / Sign-Selective Replenishment Route

- 日期：2026-08-17
- 版本：v0.1
- 狀態：Proof-Route Experiment / Continuous-Only Cancellation-Dynamics Branch
- canonical source：UTF-8 Markdown
- canonical math delimiters：inline `$...$`；display `$$...$$`
- 前一輪：`NS_X72_Round33_PureContinuous_SignedSource_CancellationRenormalization_v0.1_2026-08-17.md`
- 本輪目標：Round 33 已將 signed source拆成 net、total variation、concentration與 cancellation。本輪直接研究 cancellation coefficient與 cancellation reserve的 dynamics。核心問題：大量正負 dangerous activity若長時間互相抵消，viscosity、source production與 singular-kernel renormalization各要付出什麼 budget？
- 非主張：本文沒有證明 determinant cancellation一定消失，也沒有證明 renormalized pair cancellation不可長時間維持。本文證明的是：scalar diffusion的 Kato defect只會消耗 cancellation reserve；persistent cancellation需要 sign-selective replenishment。對 determinant，net-positive dangerous branch中的 nonnegative vorticity term同樣消耗 negative cancellation reserve；真正 replenishment重新落到 pressure / higher-gradient channels。

---

# 0. Round 33 handoff

對 signed source：

$$
W,
$$

Round 33 定義：

$$
\boxed{
M_W
=
\mathbb E[W],
\qquad
V_W
=
\mathbb E[|W|].
}
\tag{0.1}
$$

Jordan masses：

$$
\boxed{
P_W
=
\frac{
V_W+M_W
}{2},
\qquad
N_W
=
\frac{
V_W-M_W
}{2}.
}
\tag{0.2}
$$

cancellation coefficient：

$$
\boxed{
c_W
=
\frac{
M_W
}{
V_W
}
\in[-1,1].
}
\tag{0.3}
$$

以及 Cancellation-First Principle：

$$
\boxed{
\text{signed singular operator先保存 cancellation，
再取 magnitude / occupancy / probability}.
}
$$

Round 33 STOP：

$$
\boxed{
\text{STOP-C37}
=
\text{Signed-Variation / Cancellation-Renormalization Budget Gap}.
}
$$

---

# 1. Generic signed convection–diffusion density

先不直接處理：

$$
W
$$

本身。

令 signed density：

$$
\boxed{
\zeta(x,t)
}
$$

滿足：

$$
\boxed{
\partial_t\zeta
+
\operatorname{div}(b\zeta)
=
\nu\Delta\zeta
+
F.
}
\tag{1.1}
$$

假設：

- 足夠 decay；
- $\nu>0$；
- 所有積分可合法化。

在 critical-mass application中可取：

$$
\boxed{
\zeta
=
Wm_Q.
}
\tag{1.2}
$$

---

# 2. Signed net and total variation

定義：

$$
\boxed{
M(t)
=
\int
\zeta\,dx,
}
\tag{2.1}
$$

$$
\boxed{
V(t)
=
\int
|\zeta|dx.
}
\tag{2.2}
$$

由 (1.1)：

$$
\boxed{
M'
=
\int
Fdx.
}
\tag{2.3}
$$

Kato inequality給：

$$
\boxed{
V'
\le
\int
\operatorname{sgn}(\zeta)
Fdx.
}
\tag{2.4}
$$

---

# 3. Kato cancellation defect

定義 nonnegative defect：

$$
\boxed{
\mathcal D_K
=
\int
\operatorname{sgn}(\zeta)
Fdx
-
V'
\ge0.
}
\tag{3.1}
$$

所以 exact ledger：

$$
\boxed{
V'
=
\int
\operatorname{sgn}(\zeta)
Fdx
-
\mathcal D_K.
}
\tag{3.2}
$$

在 smooth convex regularization：

$$
\phi_\varepsilon(s)
=
\sqrt{
s^2+\varepsilon^2
},
$$

$\mathcal D_K$ 來自：

$$
\boxed{
\nu
\int
\phi_\varepsilon''(\zeta)
|\nabla\zeta|^2dx
}
\tag{3.3}
$$

的 zero-interface limit。

因此：

$$
\boxed{
\mathcal D_K
}
$$

測量 diffusion在 sign interface上 annihilate opposite-sign variation的速率。

---

# 4. Equal-Removal Law for Jordan masses

定義：

$$
P
=
\int
\zeta_+dx
=
\frac{
V+M
}{2},
$$

$$
N
=
\int
\zeta_-dx
=
\frac{
V-M
}{2}.
$$

由 (2.3)、(3.2)：

$$
\boxed{
P'
=
\int_{\{\zeta>0\}}
Fdx
-
\frac12
\mathcal D_K,
}
\tag{4.1}
$$

$$
\boxed{
N'
=
-
\int_{\{\zeta<0\}}
Fdx
-
\frac12
\mathcal D_K.
}
\tag{4.2}
$$

命名：

$$
\boxed{
\textbf{Kato Equal-Removal Law}.
}
$$

scalar diffusion defect以相同速率：

$$
\mathcal D_K/2
$$

消耗 positive與 negative Jordan mass，

因此保持 signed net：

$$
M=P-N
$$

不受 diffusion defect直接改變。

---

# 5. Cancellation coefficient dynamics

若：

$$
V>0,
$$

定義：

$$
\boxed{
c
=
\frac{
M
}{
V
}.
}
\tag{5.1}
$$

則：

$$
\boxed{
c'
=
\frac1V
\left[
\int
Fdx
-
c
\int
\operatorname{sgn}(\zeta)
Fdx
\right]
+
c
\frac{
\mathcal D_K
}{
V
}.
}
\tag{5.2}
$$

最後一項：

$$
\boxed{
c
\frac{
\mathcal D_K
}{
V
}
}
$$

永遠和：

$$
c
$$

同號。

所以：

$$
\boxed{
\textbf{
Kato diffusion defect pushes }|c|\textbf{ upward whenever }c\ne0.
}
}
\tag{5.3}
$$

換句話說：

$$
\boxed{
\text{diffusion weakens normalized sign cancellation}.
}
$$

---

# 6. Multiplicative-source covariance form

若：

$$
F=a\zeta,
$$

定義 variation probability：

$$
\boxed{
d\rho
=
\frac{
|\zeta|
}{
V
}
dx.
}
\tag{6.1}
$$

令：

$$
\sigma
=
\operatorname{sgn}\zeta.
$$

則：

$$
\boxed{
c
=
\langle\sigma\rangle_\rho.
}
\tag{6.2}
$$

並且：

$$
\boxed{
c'
=
\operatorname{Cov}_\rho
(
\sigma,a
)
+
c
\frac{
\mathcal D_K
}{
V
}.
}
\tag{6.3}
$$

所以 cancellation coefficient只有兩個 drivers：

1. sign-selective growth covariance；
2. Kato interface annihilation。

---

# 7. Pure diffusion branch

若：

$$
F=0,
$$

則：

$$
M'=0,
$$

$$
V'=-\mathcal D_K.
$$

因此：

$$
\boxed{
c'
=
c
\frac{
\mathcal D_K
}{
V
}.
}
\tag{7.1}
$$

如果：

$$
c\ne0,
$$

則：

$$
\boxed{
\frac d{dt}
|c|
=
|c|
\frac{
\mathcal D_K
}{
V
}
\ge0.
}
\tag{7.2}
$$

所以 pure scalar diffusion：

- 不改 net；
- 消耗 total variation；
- 暴露原本被 cancellation藏住的 signed imbalance。

如果：

$$
c=0,
$$

則：

$$
c(t)=0
$$

仍可保持，

但：

$$
V
$$

會因 diffusion下降。

所以：

$$
\boxed{
\text{cancellation ratio可以保持 perfect，
但 cancellation magnitude本身被消耗}.
}
$$

因此不能只追：

$$
c.
$$

---

# 8. Cancellation reserve

定義：

$$
\boxed{
R_{\rm can}
=
V-|M|
=
2
\min\{P,N\}.
}
\tag{8.1}
$$

這是可被正負相消的 actual magnitude。

若：

$$
M\ne0
$$

且 sign在 interval上固定，

由 (2.3)、(3.2)：

$$
\boxed{
R_{\rm can}'
=
\int
\left[
\operatorname{sgn}\zeta
-
\operatorname{sgn}M
\right]
Fdx
-
\mathcal D_K.
}
\tag{8.2}
$$

---

# 9. Sign-selective replenishment law

若：

$$
M>0,
$$

則：

$$
\boxed{
R_{\rm can}'
=
-2
\int_{\{\zeta<0\}}
Fdx
-
\mathcal D_K.
}
\tag{9.1}
$$

若：

$$
M<0,
$$

則：

$$
\boxed{
R_{\rm can}'
=
2
\int_{\{\zeta>0\}}
Fdx
-
\mathcal D_K.
}
\tag{9.2}
$$

因此 persistent cancellation reserve只能由：

$$
\boxed{
\textbf{minority-sign selective source production}
}
$$

補充。

命名：

$$
\boxed{
\textbf{Sign-Selective Cancellation Replenishment Law}.
}
$$

---

# 10. Cancellation-Sustenance Budget

假設：

$$
M>0
$$

on：

$$
I=[t_0,t_1].
$$

integrate (9.1)：

$$
\boxed{
\begin{aligned}
&
-2
\int_{t_0}^{t_1}
\int_{\{\zeta<0\}}
Fdxdt
\\
&=
R_{\rm can}(t_1)
-
R_{\rm can}(t_0)
+
\int_{t_0}^{t_1}
\mathcal D_Kdt.
\end{aligned}
}
\tag{10.1}
$$

若 cancellation reserve不顯著下降：

$$
R_{\rm can}(t_1)
\ge
R_{\rm can}(t_0)
-
\varepsilon,
$$

則：

$$
\boxed{
-2
\int_I
\int_{\{\zeta<0\}}
Fdxdt
\ge
\int_I
\mathcal D_Kdt
-
\varepsilon.
}
\tag{10.2}
$$

所以：

$$
\boxed{
\textbf{
long-lived cancellation must pay at least the cumulative Kato defect
through opposite-sign replenishment.
}
}
$$

---

# 11. Critical-mass signed source realization

Round 32 critical-mass density：

$$
m=m_Q
$$

obeys：

$$
\partial_tm+\operatorname{div}(bm)
=
\nu\Delta m
+
s\,m.
$$

令 signed observable：

$$
W.
$$

取：

$$
\boxed{
\zeta
=
Wm.
}
\tag{11.1}
$$

direct product rule：

$$
\boxed{
\partial_t\zeta
+
\operatorname{div}(b\zeta)
=
\nu\Delta\zeta
+
F_\zeta,
}
\tag{11.2}
$$

其中：

$$
\boxed{
\begin{aligned}
F_\zeta
={}&
sWm
\\
&+
m
\left[
D_bW
-
\nu\Delta W
-
2\nu
\nabla\log m\cdot\nabla W
\right].
\end{aligned}
}
\tag{11.3}
$$

所以 Sections 2–10 可直接套到 signed source relative to critical mass，

而不需要：

$$
\log W
$$

跨過 zero interface。

---

# 12. Determinant signed density

令：

$$
\boxed{
d
=
-\det S.
}
\tag{12.1}
$$

Round 33 scalar convection–diffusion form：

$$
\boxed{
\partial_td
+
u\cdot\nabla d
-
\nu\Delta d
=
F_d,
}
\tag{12.2}
$$

其中：

$$
\boxed{
F_d
=
\nu\mathcal G_{\det}
+
\frac14
|S\omega|^2
+
\operatorname{cof}S:H_p.
}
\tag{12.3}
$$

定義：

$$
\boxed{
M_D
=
\int
d\,dx,
}
\tag{12.4}
$$

$$
\boxed{
V_D
=
\int
|d|dx.
}
\tag{12.5}
$$

以及 determinant Kato defect：

$$
\boxed{
\mathcal D_D
\ge0.
}
\tag{12.6}
$$

---

# 13. Determinant cancellation coefficient

若：

$$
V_D>0,
$$

定義：

$$
\boxed{
c_D
=
\frac{
M_D
}{
V_D
}.
}
\tag{13.1}
$$

則：

$$
\boxed{
\begin{aligned}
c_D'
={}&
\frac1{V_D}
\left[
\int
F_ddx
-
c_D
\int
\operatorname{sgn}(d)
F_ddx
\right]
\\
&+
c_D
\frac{
\mathcal D_D
}{
V_D
}.
\end{aligned}
}
\tag{13.2}
$$

所以 scalar determinant diffusion component：

$$
\nu\Delta d
$$

本身永遠弱化：

$$
|c_D|<1
$$

的 normalized cancellation。

---

# 14. Net determinant and vortex stretching

whole-space identity：

$$
\boxed{
M_D
=
\int
(-\det S)dx
=
\frac14
\int
\omega^\top S\omega dx.
}
\tag{14.1}
$$

enstrophy balance：

$$
\boxed{
\frac12
\frac d{dt}
\|\omega\|_2^2
+
\nu
\|\nabla\omega\|_2^2
=
4M_D.
}
\tag{14.2}
$$

所以 dangerous net enstrophy-growth phase naturally對應：

$$
\boxed{
M_D>0.
}
$$

以下 cancellation budget先研究此 branch。

---

# 15. Determinant cancellation reserve in net-positive branch

若：

$$
M_D>0,
$$

定義：

$$
\boxed{
R_D
=
V_D-M_D
=
2
\int
d_-dx.
}
\tag{15.1}
$$

由 Sign-Selective Replenishment Law：

$$
\boxed{
R_D'
=
-2
\int_{\{d<0\}}
F_ddx
-
\mathcal D_D.
}
\tag{15.2}
$$

代入：

$$
F_d,
$$

得到：

$$
\boxed{
\begin{aligned}
R_D'
={}&
-2\nu
\int_{\{d<0\}}
\mathcal G_{\det}dx
\\
&-
\frac12
\int_{\{d<0\}}
|S\omega|^2dx
\\
&-
2
\int_{\{d<0\}}
\operatorname{cof}S:H_pdx
\\
&-
\mathcal D_D.
\end{aligned}
}
\tag{15.3}
$$

---

# 16. Vorticity coupling erodes determinant cancellation in the dangerous net branch

在：

$$
M_D>0
$$

branch，

$$
\frac14|S\omega|^2
$$

永遠非負。

但 negative determinant region：

$$
d<0
$$

正是 cancellation reserve的 minority-sign carrier。

所以它對：

$$
R_D'
$$

的 contribution為：

$$
\boxed{
-
\frac12
\int_{\{d<0\}}
|S\omega|^2dx
\le0.
}
\tag{16.1}
$$

因此：

$$
\boxed{
\textbf{
vorticity coupling does not replenish determinant sign cancellation
when net vortex-stretching production is positive;
it erodes the negative cancellation reserve.
}
}
\tag{16.2}
$$

這是本輪最強 NS-specific sign result之一。

---

# 17. Determinant Cancellation-Sustenance Inequality

令：

$$
I=[t_0,t_1]
$$

且：

$$
M_D>0
$$

throughout。

若：

$$
R_D(t_1)
\ge
R_D(t_0)-\varepsilon,
$$

由 (15.3)：

$$
\boxed{
\begin{aligned}
&
-2
\int_I
\int_{\{d<0\}}
\left[
\nu\mathcal G_{\det}
+
\operatorname{cof}S:H_p
\right]
dxdt
\\
&\ge
\int_I
\mathcal D_Ddt
+
\frac12
\int_I
\int_{\{d<0\}}
|S\omega|^2dxdt
-
\varepsilon.
\end{aligned}
}
\tag{17.1}
$$

命名：

$$
\boxed{
\textbf{Determinant Cancellation-Sustenance Inequality}.
}
$$

所以長時間把 large two-sided determinant activity藏在 cancellation裡，

真正 replenishment只能由：

$$
\boxed{
\text{pressure-Hessian}
+
\text{tensor-diffusion curvature}
}
$$

在 negative determinant region提供足夠 opposite-sign work。

又回到 Round 04 / 05。

---

# 18. Cancellation reserve and source concentration are independent

即使：

$$
R_{\rm can}
$$

很大，

source magnitude仍可能：

- spatially diffuse；
- spatially intermittent。

因此 cancellation dynamics與 Round 31 participation仍是不同 coordinates：

$$
\boxed{
X_{\rm signed}
=
\left\langle
V,
c,
R_{\rm can},
\mathfrak J_{|\zeta|}
\right\rangle.
}
\tag{18.1}
$$

其中：

- $V$：total activity；
- $c$：net balance；
- $R_{\rm can}$：cancelable minority reserve；
- $\mathfrak J$：carrier concentration。

沒有一個 scalar能取代全部資訊。

---

# 19. Cancellation exposure

定義 normalized Kato erosion rate：

$$
\boxed{
\delta_K
=
\frac{
\mathcal D_K
}{
V
}.
}
\tag{19.1}
$$

及 cumulative cancellation exposure：

$$
\boxed{
\Gamma_{\rm can}(I)
=
\int_I
\delta_K(t)dt.
}
\tag{19.2}
$$

在 source-free branch：

$$
F=0,
$$

有：

$$
\boxed{
c'
=
c\delta_K.
}
$$

所以：

$$
\boxed{
|c(t_1)|
=
|c(t_0)|
\exp
\Gamma_{\rm can}(I)
}
\tag{19.3}
$$

直到：

$$
|c|
$$

逼近 geometric bound：

$$
1.
$$

equivalently：

$$
V
$$

被削減到：

$$
|M|.
$$

因此：

$$
\Gamma_{\rm can}
$$

是一個 continuous sign-mixing erosion clock。

---

# 20. Renormalized singular-pair source dynamics

Round 33 對 even mean-zero kernel：

$$
K(z)
$$

定義：

$$
\boxed{
q_f(x,z,t)
=
\frac12
K(z)
\Delta_z^2f(x,t),
}
\tag{20.1}
$$

其中：

$$
\boxed{
\Delta_z^2f(x)
=
f(x+z)
+
f(x-z)
-
2f(x).
}
\tag{20.2}
$$

假設：

$$
f
$$

滿足：

$$
\boxed{
\partial_tf
+
u\cdot\nabla f
-
\nu\Delta f
=
R_f.
}
\tag{20.3}
$$

---

# 21. Exact second-difference transport equation

令 center-material derivative：

$$
D_t^x
=
\partial_t
+
u(x,t)\cdot\nabla_x.
$$

則：

$$
\boxed{
\begin{aligned}
D_t^x
\Delta_z^2f
-
\nu
\Delta_x
\Delta_z^2f
={}&
\Delta_z^2R_f
+
\mathcal C_u[f],
\end{aligned}
}
\tag{21.1}
$$

其中 transport commutator：

$$
\boxed{
\begin{aligned}
\mathcal C_u[f](x,z)
={}&
[
u(x)-u(x+z)
]
\cdot
\nabla f(x+z)
\\
&+
[
u(x)-u(x-z)
]
\cdot
\nabla f(x-z).
\end{aligned}
}
\tag{21.2}
$$

所以：

$$
q_f
$$

滿足：

$$
\boxed{
D_t^xq_f
-
\nu\Delta_xq_f
=
\widetilde F_f,
}
\tag{21.3}
$$

其中：

$$
\boxed{
\widetilde F_f
=
\frac12
K(z)
[
\Delta_z^2R_f
+
\mathcal C_u[f]
].
}
\tag{21.4}
$$

---

# 22. Renormalized pair cancellation ledger

在：

$$
(x,z)
$$

space上定義：

$$
\boxed{
\widetilde M_f
=
\iint
q_f
\,dxdz,
}
\tag{22.1}
$$

$$
\boxed{
\widetilde V_f
=
\iint
|q_f|
\,dxdz,
}
\tag{22.2}
$$

對合法 truncated / absolutely convergent domain。

則：

$$
\boxed{
\widetilde M_f'
=
\iint
\widetilde F_f
\,dxdz,
}
\tag{22.3}
$$

及 Kato：

$$
\boxed{
\widetilde V_f'
=
\iint
\operatorname{sgn}(q_f)
\widetilde F_f
\,dxdz
-
\widetilde{\mathcal D}_K,
}
\tag{22.4}
$$

其中：

$$
\boxed{
\widetilde{\mathcal D}_K
\ge0.
}
$$

所以 Round 34 的 cancellation-reserve machinery完整移植到 cancellation-preserving pair representation。

---

# 23. Pair cancellation is replenished by a transport commutator

Equation (21.4)顯示 renormalized pair signed activity的 source來自：

$$
\boxed{
\Delta_z^2R_f
}
$$

以及：

$$
\boxed{
\mathcal C_u[f].
}
$$

即使 original singular kernel本身只是一個 static convolution，

其 cancellation dynamics也由：

$$
\boxed{
\text{field source}
+
\text{velocity-increment transport commutator}
}
$$

供應。

所以 persistent nonlocal sign cancellation同樣不是免費。

---

# 24. Near-diagonal commutator integrability

若：

$$
u
$$

locally Lipschitz，

且：

$$
\nabla f
$$

locally bounded，

則：

$$
|u(x)-u(x\pm z)|
\lesssim
|z|
\|\nabla u\|_{\infty,\mathrm{loc}}.
$$

所以：

$$
\boxed{
|\mathcal C_u[f](x,z)|
\lesssim
|z|
\|\nabla u\|_{\infty,\mathrm{loc}}
\|\nabla f\|_{\infty,\mathrm{loc}}.
}
\tag{24.1}
$$

乘：

$$
|K(z)|
\sim
|z|^{-3}
$$

與三維 volume：

$$
r^2dr,
$$

得到：

$$
\boxed{
r^{-3}
\cdot
r
\cdot
r^2dr
=
O(1)dr.
}
\tag{24.2}
$$

所以 transport commutator在 smooth/Lipschitz branch near diagonal仍可積分。

真正 absolute-variation cost仍落在 spatial regularity / increment budget。

---

# 25. Pair cancellation replenishment is another higher-regularity bill

雖然 second-difference renormalization移除了 raw logarithmic divergence，

要控制：

$$
\widetilde F_f
$$

仍需：

- velocity increments；
- source second differences；
- local gradients。

對 pressure source：

$$
f_p
=
|S|^2
-
\frac12|\omega|^2,
$$

這要求 higher spatial regularity。

對 Biot–Savart strain：

$$
f=\omega,
$$

則要求 vorticity increment control。

所以：

$$
\boxed{
\textbf{
renormalization makes the representation legal,
but sustained cancellation still spends higher-regularity budget.
}
}
\tag{25.1}
$$

---

# 26. Cancellation / phase confluence

Round 10 Fourier signed transfer：

$$
\mathcal T
=
A\sin\Phi.
$$

Round 27 nonlocal angular coupling：

$$
\mathcal C
=
A\cos\theta.
$$

Round 34 signed-source ledger：

$$
M
=
P-N.
$$

三者共同結構：

$$
\boxed{
\text{large unsigned activity}
+
\text{small signed net}
=
\text{persistent cancellation organization}.
}
$$

差別只在 representation：

- Fourier phase；
- angular phase；
- physical-space sign interface；
- singular-kernel shell cancellation。

所以：

$$
\boxed{
\textbf{phase locking and sign cancellation are now one obstruction family.}
}
\tag{26.1}
$$

---

# 27. Cancellation-Sustenance Trichotomy

若 large total activity：

$$
V
$$

長時間存在，

但 signed net：

$$
|M|\ll V,
$$

則 persistent cancellation只能靠：

$$
\boxed{
\begin{aligned}
\mathrm{C1}:&
\quad
\text{weak Kato/interface erosion},
\\
\mathrm{C2}:&
\quad
\text{strong minority-sign selective replenishment},
\\
\mathrm{C3}:&
\quad
\text{renormalized phase/sign organization
that keeps producing opposite signs}.
\end{aligned}
}
\tag{27.1}
$$

如果：

$$
\mathcal D_K
$$

大，

C1不可行；

若 replenishment budget有限，

C2不可行；

則 cancellation reserve必下降。

---

# 28. STOP-C38 — Cancellation-Reserve / Sign-Selective Replenishment Gap

$$
\boxed{
\begin{aligned}
\text{layer}
&=
\mathrm{signed\ cancellation\ dynamics},
\\
\text{net}
&=
M,
\\
\text{variation}
&=
V,
\\
\text{cancellation coefficient}
&=
c=M/V,
\\
\text{cancellation reserve}
&=
R_{\rm can}=V-|M|,
\\
\text{Kato defect}
&=
\mathcal D_K\ge0,
\\
\text{diffusion effect}
&=
\text{equal Jordan-mass removal / cancellation erosion},
\\
\text{persistent cancellation}
&=
\text{requires minority-sign replenishment},
\\
\text{determinant net-positive branch}
&:
\frac14|S\omega|^2
\text{ erodes negative reserve},
\\
\text{determinant replenishment}
&=
\text{pressure + tensor-diffusion curvature},
\\
\text{renormalized pair replenishment}
&=
\text{source second difference + transport commutator},
\\
\text{missing}
&=
\text{unconditional spacetime control of sign-selective replenishment
and renormalized cancellation work},
\\
T_{\mathsf C\to\mathsf D}
&=
\text{NOT REACHED}.
\end{aligned}
}
$$

命名：

$$
\boxed{
\textbf{STOP-C38:
Cancellation-Reserve / Sign-Selective Replenishment Gap}.
}
$$

---

# 29. 24/72 Ledger — Round 34

| Step | object | $B$ | $U$ | $O$ | $L$ | status |
|---|---|---|---|---|---|---|
| C492 | signed convection–diffusion density | $\mathsf C$ | PDE | relational | $\mathsf F$ | FORM |
| C493 | Kato defect $\mathcal D_K$ | $\mathsf C$ | diffusion/interface | scalar | $\mathsf F$ | FORM / NONNEGATIVE |
| C494 | Kato Equal-Removal Law | $\mathsf C$ | Jordan dynamics | targeted | $\mathsf F$ | PROVED |
| C495 | cancellation coefficient dynamics | $\mathsf C$ | signed measure | scalar | $\mathsf F$ | EXACT |
| C496 | multiplicative covariance law | $\mathsf C$ | variation measure | scalar | $\mathsf F$ | EXACT |
| C497 | pure-diffusion cancellation erosion | $\mathsf C$ | Kato flow | targeted | $\mathsf F$ | PROVED |
| C498 | cancellation reserve $R_{\rm can}$ | $\mathsf C$ | Jordan geometry | scalar | $\mathsf F$ | FORM |
| C499 | sign-selective replenishment law | $\mathsf C$ | signed source | targeted | $\mathsf F$ | EXACT |
| C500 | cancellation-sustenance budget | $\mathsf C$ | spacetime integral | targeted | $\mathsf F$ | PROVED |
| C501 | critical-mass signed realization | $\mathsf C$ | measure/PDE | relational | $\mathsf F$ | EXACT |
| C502 | determinant cancellation dynamics | $\mathsf C$ | strain PDE | relational | $\mathsf F$ | EXACT |
| C503 | determinant vorticity erosion | $\mathsf C$ | sign geometry | targeted | $\mathsf F$ | PROVED |
| C504 | determinant sustenance inequality | $\mathsf C$ | pressure/higher derivative | targeted | $\mathsf F$ | PROVED |
| C505 | cancellation exposure $\Gamma_{\rm can}$ | $\mathsf C$ | time integral | scalar | $\mathsf F$ | FORM |
| C506 | second-difference transport equation | $\mathsf C$ | increment PDE | relational | $\mathsf F$ | EXACT |
| C507 | renormalized pair Kato ledger | $\mathsf C$ | product/increment space | scalar | $\mathsf F$ | CONDITIONAL EXACT |
| C508 | transport-commutator source | $\mathsf C$ | increment geometry | relational | $\mathsf F$ | EXACT |
| C509 | near-diagonal commutator integrability | $\mathsf C$ | singular kernel | targeted | $\mathsf F$ | PROVED in smooth branch |
| C510 | phase/sign obstruction confluence | $\mathsf C$ | representation map | $\mathsf X$ | $\mathsf F$ | IDENTIFIED |
| C511 | unconditional cancellation-work bound | $\mathsf C$ | coupled NS | targeted | $\mathsf F$ | OPEN / STOP-C38 |

---

# 30. Continuous-versus-discrete status

本輪全部使用：

- continuous signed densities；
- continuous zero interfaces；
- continuous Kato defect；
- continuous Jordan measures；
- continuous material/source transport；
- continuous separation vector：
  $$
  z\in\mathbb R^3;
  $$
- continuous second differences。

沒有：

- sign-state automaton；
- positive/negative cell counting；
- discrete shell index；
- graph cancellation flow。

所以：

$$
\boxed{
T_{\mathsf C\to\mathsf D}
=
\text{NOT YET REACHED}.
}
$$

---

# 31. Strongest results of Round 34

## R34-A — Kato Equal-Removal Law

$$
\boxed{
P'
=
\int_{\zeta>0}F
-
\frac12\mathcal D_K,
}
$$

$$
\boxed{
N'
=
-
\int_{\zeta<0}F
-
\frac12\mathcal D_K.
}
$$

## R34-B — Cancellation coefficient dynamics

$$
\boxed{
c'
=
\frac{
\int F
-
c\int\operatorname{sgn}\zeta\,F
}{
V
}
+
c\frac{\mathcal D_K}{V}.
}
$$

## R34-C — Cancellation reserve dynamics

for $M>0$：

$$
\boxed{
R_{\rm can}'
=
-2
\int_{\zeta<0}F
-
\mathcal D_K.
}
$$

## R34-D — Determinant cancellation-sustenance burden

for $M_D>0$：

$$
\boxed{
\begin{aligned}
&
-2
\int_I
\int_{d<0}
[
\nu\mathcal G_{\det}
+
\operatorname{cof}S:H_p
]
\\
&\ge
\int_I\mathcal D_D
+
\frac12
\int_I
\int_{d<0}|S\omega|^2
-
\varepsilon
\end{aligned}
}
$$

whenever cancellation reserve is maintained up to $\varepsilon$.

## R34-E — Renormalized pair transport

$$
\boxed{
D_t^x\Delta_z^2f
-
\nu\Delta_x\Delta_z^2f
=
\Delta_z^2R_f
+
\mathcal C_u[f].
}
$$

所以 cancellation-preserving singular source也有自己的 Kato / replenishment ledger。

---

# 32. Next round — Cancellation-Replenishment Budget Closure

Round 34 已經把 persistent cancellation的必要供電來源找出來。

下一輪不再研究：

$$
c
$$

怎麼定義。

直接問：

$$
\boxed{
\text{minority-sign replenishment budget到底能不能長時間支付？}
}
$$

具體：

1. determinant net-positive branch：
   $$
   -\int_{d<0}
   \operatorname{cof}S:H_p
   $$
   是否有 sign / variance / nonlocal depletion；

2. tensor-diffusion curvature：
   $$
   -\nu
   \int_{d<0}
   \mathcal G_{\det}
   $$
   能否由 determinant Kato defect吸收；

3. pressure replenishment若要長期維持 cancellation，是否再次需要 quadrupole coherence locking；

4. renormalized pair commutator：
   $$
   \mathcal C_u[f]
   $$
   是否可由 velocity-increment / second-difference budget吸收；

5. 將 Round 34 cancellation exposure與 Round 29 lock exposure比較；

6. 若 cancellation replenishment有限，large unsigned activity將逐步暴露成 net dangerous production；

7. 若 replenishment可無界，新的 obstruction core就是 sign-selective pressure / increment forcing；

8. 繼續保持 continuous representation。

---

# 33. External primary-source anchors

1. J. Endal, E. R. Jakobsen, *$L^1$ contraction for bounded (non-integrable) solutions of degenerate parabolic equations*, arXiv:1404.6418.
   - diffusion / degenerate parabolic equations中的 $L^1$ contraction與 comparison背景；
   - 本輪 Kato-style total-variation ledger只使用這類 classical parabolic contraction結構作外部背景。

2. Borys Álvarez-Samaniego, Wilson P. Álvarez-Samaniego, Pedro G. Fernández-Dalgo, *On the use of the Riesz transforms to determine the pressure term in the incompressible Navier-Stokes equations on the whole space*, arXiv:2004.02588.
   - whole-space pressure的 Riesz-transform singular-integral representation背景。

3. Joan Mateu, Joan Orobitg, Joan Verdera, *Estimates for the maximal singular integral in terms of the singular integral: the case of even kernels*, arXiv:0707.4610.
   - smooth homogeneous even Calderón–Zygmund kernels與 cancellation結構的 primary-source背景。

4. Evan Miller, *On the interaction of strain and vorticity for solutions of the Navier--Stokes equation*, arXiv:2407.02691.
   - strain–vorticity interaction與 nonlinear depletion背景。

本輪 Kato Equal-Removal Law、Cancellation-Reserve Dynamics、Determinant Cancellation-Sustenance Inequality與 renormalized second-difference transport equation均為本文直接推導。

---

# 34. Commit state

$$
\boxed{
\begin{aligned}
\text{Route}
&=
\mathrm{Pure\ Continuous\ Cancellation\text{-}Budget\ Dynamics},
\\
\text{Essential }\mathsf C\to\mathsf D
&=
\mathrm{Not\ reached},
\\
\text{Diffusion}
&=
\mathrm{cancellation\ erosion},
\\
\text{Persistent cancellation}
&=
\mathrm{minority\text{-}sign\ replenishment},
\\
\text{Determinant vorticity term}
&=
\mathrm{negative\text{-}reserve\ erosion\ when\ }M_D>0,
\\
\text{Determinant replenishment}
&=
\mathrm{pressure}
+
\mathrm{tensor\text{-}diffusion\ curvature},
\\
\text{Renormalized pair replenishment}
&=
\mathrm{source\ second\ difference}
+
\mathrm{transport\ commutator},
\\
\text{Phase/sign cancellation}
&=
\mathrm{one\ obstruction\ family},
\\
\text{STOP-C38}
&=
\mathrm{Cancellation\text{-}Reserve/Sign\text{-}Selective\ Replenishment\ Gap},
\\
\text{Next}
&=
\mathrm{Cancellation\text{-}Replenishment\ Budget\ Closure}.
\end{aligned}
}
$$
