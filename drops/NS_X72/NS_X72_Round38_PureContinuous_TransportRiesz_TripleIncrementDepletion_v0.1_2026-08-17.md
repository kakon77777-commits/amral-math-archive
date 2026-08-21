# NS × X 積分 × 24/72 範式實戰
## Round 38 — Pure Continuous Transport–Riesz Commutator Depletion / Triple-Increment Route

- 日期：2026-08-17
- 版本：v0.1
- 狀態：Proof-Route Experiment / Continuous-Only Pairing-Level Commutator Branch
- canonical source：UTF-8 Markdown
- canonical math delimiters：inline `$...$`；display `$$...$$`
- 前一輪：`NS_X72_Round37_PureContinuous_PressureResponse_DefectEnergy_v0.1_2026-08-17.md`
- 本輪目標：Round 37 將 affine-response defect
  $$
  E_p=H_p^0+C_S^0
  $$
  的主要獨立 nonlocal forcing壓成 transport–Riesz commutator
  $$
  [u\cdot\nabla,\mathcal T_0]q.
  $$
  本輪不先估整個 commutator norm，而直接研究 defect-energy pairing
  $$
  \langle E_p,[u\cdot\nabla,\mathcal T_0]q\rangle.
  $$
  利用 $\mathcal T_0$ 的 self-adjoint / constant-symbol-norm 結構、incompressibility與 even kernel symmetry，建立 pressure self-commutator null identity、exact triple-increment representation、critical continuous increment budget與 Dini endpoint barrier。
- 非主張：本文沒有證明 critical endpoint increment budget由 basic NS energy無條件控制。本文證明的是：Round 37 的 commutator norm估計過於粗糙；在 defect-energy pairing層級存在兩層 exact cancellation，使 regularity burden下降為 one-total-derivative increment problem。

---

# 0. Round 37 handoff

Round 37 定義 affine-response defect：

$$
\boxed{
E
=
E_p
=
H+C,
}
\tag{0.1}
$$

其中：

$$
H
=
H_p^0,
$$

$$
C
=
C_S^0.
$$

pressure source：

$$
\boxed{
q
=
|S|^2-\frac12|\omega|^2.
}
\tag{0.2}
$$

trace-free Riesz operator：

$$
\boxed{
H
=
\mathcal T_0q.
}
\tag{0.3}
$$

defect PDE：

$$
\boxed{
D_tE-\nu\Delta E
=
-\mathscr L_S[E]
+
\mathcal F_E^{(0)}
+
\mathcal K_uq,
}
\tag{0.4}
$$

where：

$$
\boxed{
\mathcal K_uq
=
[u\cdot\nabla,\mathcal T_0]q,
}
\tag{0.5}
$$

and：

$$
\boxed{
\mathcal F_E^{(0)}
=
-2\nu Q_C
+
V_C
+
\mathcal T_0N_0.
}
\tag{0.6}
$$

Round 37 只用 norm envelope處理：

$$
\mathcal K_uq.
$$

本輪專門尋找 pairing-level depletion。

Round 37 STOP：

$$
\boxed{
\text{STOP-C41}
=
\text{Affine-Response Defect / Critical Commutator–Gradient Gap}.
}
$$

---

# 1. Fourier symbol of the trace-free pressure operator

對：

$$
\xi\ne0,
$$

令：

$$
n_\xi
=
\frac{\xi}{|\xi|}.
$$

$\mathcal T_0$ 的 matrix multiplier：

$$
\boxed{
M_0(\xi)
=
\frac13I
-
n_\xi\otimes n_\xi.
}
\tag{1.1}
$$

其 eigenvalues：

$$
-\frac23,
\qquad
\frac13,
\qquad
\frac13.
$$

因此：

$$
\boxed{
|M_0(\xi)|_F^2
=
\frac23.
}
\tag{1.2}
$$

所以作為 scalar-to-tracefree-tensor operator：

$$
\boxed{
\mathcal T_0^\ast
\mathcal T_0
=
\frac23I.
}
\tag{1.3}
$$

此外：

$$
\mathcal T_0
$$

是 real self-adjoint Fourier multiplier。

---

# 2. Divergence-free transport is skew-adjoint

令：

$$
D_u
=
u\cdot\nabla.
$$

若：

$$
\nabla\cdot u=0
$$

且 fields足夠 decay，

則：

$$
\boxed{
D_u^\ast
=
-D_u.
}
\tag{2.1}
$$

所以對 scalar：

$$
f,
$$

$$
\boxed{
\langle f,D_uf\rangle=0.
}
\tag{2.2}
$$

對 tensor field同樣 componentwise成立。

---

# 3. Pressure Self-Commutator Null Identity

令：

$$
H
=
\mathcal T_0q.
$$

則：

$$
\boxed{
\begin{aligned}
\langle
H,
[D_u,\mathcal T_0]q
\rangle
={}&
\langle
\mathcal T_0q,
D_u\mathcal T_0q
\rangle
\\
&-
\langle
\mathcal T_0q,
\mathcal T_0D_uq
\rangle.
\end{aligned}
}
\tag{3.1}
$$

第一項由 skew-adjointness：

$$
=0.
$$

第二項由：

$$
\mathcal T_0^\ast\mathcal T_0
=
\frac23I
$$

得到：

$$
-\frac23
\langle
q,D_uq
\rangle
=
0.
$$

所以：

$$
\boxed{
\left\langle
H_p^0,
[u\cdot\nabla,\mathcal T_0]q
\right\rangle
=
0.
}
\tag{3.2}
$$

命名：

$$
\boxed{
\textbf{Pressure Self-Commutator Null Identity}.
}
$$

---

# 4. The defect commutator only sees pressure–cofactor incompatibility

因：

$$
E=H+C,
$$

由 (3.2)：

$$
\boxed{
\left\langle
E,
\mathcal K_uq
\right\rangle
=
\left\langle
C,
\mathcal K_uq
\right\rangle.
}
\tag{4.1}
$$

所以 transport–Riesz commutator不是 pressure Hessian自己的 $L^2$ energy injection。

它只在：

$$
\boxed{
\text{local cofactor geometry}
\quad\text{與}\quad
\text{nonlocal pressure response}
}
$$

不完全相容時出現在 defect energy。

這修正 Round 37 將 commutator視為獨立 additive pressure forcing的粗略 picture。

---

# 5. Kernel form

令：

$$
K_0(z)
$$

為：

$$
\mathcal T_0
$$

的 trace-free even Calderón–Zygmund kernel。

則：

$$
\boxed{
K_0(-z)=K_0(z),
}
\tag{5.1}
$$

$$
\boxed{
|K_0(z)|
\lesssim
|z|^{-3},
}
\tag{5.2}
$$

$$
\boxed{
|\nabla K_0(z)|
\lesssim
|z|^{-4}.
}
\tag{5.3}
$$

並且 angular mean zero。

由 divergence-free integration by parts：

$$
\boxed{
\mathcal K_uq(x)
=
\operatorname{p.v.}
\int
[
u(x)-u(y)
]
\cdot
\nabla K_0(x-y)
\,q(y)\,dy.
}
\tag{5.4}
$$

---

# 6. Pair kernel symmetry

定義 tensor pair kernel：

$$
\boxed{
G_u(x,y)
=
[
u(x)-u(y)
]
\cdot
\nabla K_0(x-y).
}
\tag{6.1}
$$

因：

- $u(x)-u(y)$ 在交換 $x,y$ 時變號；
- $\nabla K_0$ 因 $K_0$ even而是 odd；

所以：

$$
\boxed{
G_u(y,x)
=
G_u(x,y).
}
\tag{6.2}
$$

此外 commutator annihilates constants，

所以 principal-value sense下：

$$
\boxed{
\int
G_u(x,y)dy
=
0,
}
\tag{6.3}
$$

且由 symmetry：

$$
\boxed{
\int
G_u(x,y)dx
=
0.
}
\tag{6.4}
$$

---

# 7. Exact Triple-Increment Pairing Identity

令：

$$
\delta_{xy}u
=
u(x)-u(y),
$$

$$
\delta_{xy}E
=
E(x)-E(y),
$$

$$
\delta_{xy}q
=
q(x)-q(y).
$$

由 pair symmetry及 zero-row identities：

$$
\boxed{
\begin{aligned}
\left\langle
E,
\mathcal K_uq
\right\rangle
=
-\frac12
\operatorname{p.v.}
\iint
&
\left[
\delta_{xy}u
\cdot
\nabla K_0(x-y)
\right]
\\
&:
\delta_{xy}E
\,
\delta_{xy}q
\,dxdy.
\end{aligned}
}
\tag{7.1}
$$

命名：

$$
\boxed{
\textbf{Transport–Riesz Triple-Increment Identity}.
}
$$

這是本輪最重要的 exact representation。

---

# 8. Equivalent cofactor triple-increment identity

由 (4.1)：

$$
\boxed{
\begin{aligned}
\left\langle
E,
\mathcal K_uq
\right\rangle
=
-\frac12
\operatorname{p.v.}
\iint
&
[
\delta u
\cdot
\nabla K_0
]
\\
&:
\delta C
\,
\delta q
\,dxdy.
\end{aligned}
}
\tag{8.1}
$$

而 pressure component本身滿足：

$$
\boxed{
\operatorname{p.v.}
\iint
[
\delta u
\cdot\nabla K_0
]
:
\delta H
\,
\delta q
\,dxdy
=
0.
}
\tag{8.2}
$$

所以 commutator depletion可在：

- defect increment；
- 或 local cofactor increment；

兩種表示下追蹤。

---

# 9. Cofactor and pressure-source increments

cofactor：

$$
C
=
S^2-\frac13|S|^2I.
$$

有 exact：

$$
\boxed{
\begin{aligned}
\delta C
={}&
\frac12
\left[
(S_x+S_y)\delta S
+
\delta S(S_x+S_y)
\right]
\\
&-
\frac13
[
(S_x+S_y):\delta S
]
I.
\end{aligned}
}
\tag{9.1}
$$

所以：

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
\tag{9.2}
$$

pressure source：

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
\tag{9.3}
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
\tag{9.4}
$$

所以 commutator真正測：

$$
\boxed{
\text{velocity increment}
\times
\text{defect/cofactor increment}
\times
\text{strain-vorticity source increment}.
}
$$

---

# 10. Critical triple-increment budget

令：

$$
1\le
p_u,p_E,p_q
\le\infty,
$$

滿足：

$$
\boxed{
\frac1{p_u}
+
\frac1{p_E}
+
\frac1{p_q}
=
1.
}
\tag{10.1}
$$

定義 translation increment：

$$
\delta_zu(x)
=
u(x+z)-u(x),
$$

等等。

定義：

$$
\boxed{
\mathfrak I_{\rm TR}^{p_u,p_E,p_q}
=
\int_{\mathbb R^3}
\frac{
\|\delta_zu\|_{p_u}
\|\delta_zE\|_{p_E}
\|\delta_zq\|_{p_q}
}{
|z|^4
}
dz.
}
\tag{10.2}
$$

由 (7.1) 及 Hölder：

$$
\boxed{
\left|
\langle
E,
\mathcal K_uq
\rangle
\right|
\le
C
\mathfrak I_{\rm TR}^{p_u,p_E,p_q}.
}
\tag{10.3}
$$

命名：

$$
\boxed{
\textbf{Critical Transport–Riesz Increment Budget}.
}
$$

---

# 11. Exact NS scaling of the increment budget

NS scaling：

$$
u_\Lambda(x,t)
=
\Lambda
u(\Lambda x,\Lambda^2t).
$$

因：

$$
E_\Lambda
=
\Lambda^4
E(\Lambda x,\Lambda^2t),
$$

及：

$$
q_\Lambda
=
\Lambda^4
q(\Lambda x,\Lambda^2t),
$$

且 (10.1)，

可直接驗證：

$$
\boxed{
\mathfrak I_{\rm TR}[u_\Lambda,E_\Lambda,q_\Lambda]
=
\Lambda^7
\mathfrak I_{\rm TR}[u,E,q].
}
\tag{11.1}
$$

而 defect-energy derivative：

$$
\frac d{dt}
\|E\|_2^2
$$

也 scaling為：

$$
\Lambda^7.
$$

因此：

$$
\boxed{
\mathfrak I_{\rm TR}
}
$$

是 pairing本身的 scale-critical instantaneous budget。

---

# 12. Continuous increment modulus

定義：

$$
\boxed{
\omega_{f,p}(r)
=
\sup_{|z|\le r}
\|\delta_zf\|_p.
}
\tag{12.1}
$$

near diagonal由：

$$
|\nabla K_0(z)|
\lesssim
|z|^{-4}
$$

有：

$$
\boxed{
\mathfrak I_{\rm TR}^{\rm near}
\lesssim
\int_0^{r_0}
\frac{
\omega_{u,p_u}(r)
\omega_{E,p_E}(r)
\omega_{q,p_q}(r)
}{
r^2
}
dr.
}
\tag{12.2}
$$

所以真正 local proof obligation是一個 continuous Dini-type integral。

沒有 dyadic scale decomposition。

---

# 13. One-total-derivative threshold

假設 small scale：

$$
\omega_{u,p_u}(r)
\lesssim
r^{s_u},
$$

$$
\omega_{E,p_E}(r)
\lesssim
r^{s_E},
$$

$$
\omega_{q,p_q}(r)
\lesssim
r^{s_q}.
$$

則 (12.2) behaves like：

$$
\boxed{
\int_0
r^{
s_u+s_E+s_q-2
}
dr.
}
\tag{13.1}
$$

所以 absolute local convergence要求：

$$
\boxed{
s_u+s_E+s_q>1.
}
\tag{13.2}
$$

命名：

$$
\boxed{
\textbf{One-Total-Derivative Triple-Increment Threshold}.
}
$$

---

# 14. Why the endpoint is exactly scale-critical

Besov-type spatial norms scale：

$$
\|u\|_{\dot B^{s_u}_{p_u}}
\mapsto
\Lambda^{
1+s_u-3/p_u
},
$$

$$
\|E\|_{\dot B^{s_E}_{p_E}}
\mapsto
\Lambda^{
4+s_E-3/p_E
},
$$

$$
\|q\|_{\dot B^{s_q}_{p_q}}
\mapsto
\Lambda^{
4+s_q-3/p_q
}.
$$

乘起來並用：

$$
\frac1{p_u}
+
\frac1{p_E}
+
\frac1{p_q}
=1,
$$

得到 scaling：

$$
\boxed{
\Lambda^{
6+s_u+s_E+s_q
}.
}
\tag{14.1}
$$

要 match commutator pairing：

$$
\Lambda^7,
$$

恰好要求：

$$
\boxed{
s_u+s_E+s_q=1.
}
\tag{14.2}
$$

所以：

- $>1$ 是 subcritical regularity branch；
- $=1$ 是 exact critical endpoint；
- $<1$ 是 supercritical from this pairing viewpoint。

---

# 15. Critical Dini endpoint

當：

$$
s_u+s_E+s_q=1,
$$

單純 power counting給：

$$
\int_0
\frac{dr}{r},
$$

log divergence。

因此 critical endpoint需要比純 power bound多一點 continuous summability：

$$
\boxed{
\int_0^{r_0}
\frac{
\omega_{u,p_u}(r)
\omega_{E,p_E}(r)
\omega_{q,p_q}(r)
}{
r^2
}
dr
<
\infty.
}
\tag{15.1}
$$

可由：

- Dini improvement；
- little-Besov / vanishing endpoint modulus；
- logarithmic gain；

實現。

本輪不宣稱任一 endpoint condition由 NS basic energy自動提供。

命名：

$$
\boxed{
\textbf{Triple-Increment Critical Dini Barrier}.
}
$$

---

# 16. Pairing-level depletion versus norm-level commutator control

Round 37 schematic norm route：

$$
\|
[u\cdot\nabla,\mathcal T_0]q
\|_p
\lesssim
\|\nabla u\|_\infty
\|q\|_p
$$

要求 velocity field接近 Lipschitz。

Round 38 pairing route只需要：

$$
\boxed{
\text{combined increment regularity}
}
$$

超過 one derivative：

$$
s_u+s_E+s_q>1.
$$

所以：

$$
\boxed{
\textbf{
pairing-level cancellation is strictly more structure-aware
than estimating the full commutator norm.
}
}
\tag{16.1}
$$

這不表示 endpoint已閉合。

它只是把 proof obligation降到真正 defect-weighted critical increment space。

---

# 17. Continuous near/far scale split

取：

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
\frac12.
}
\tag{17.1}
$$

對任意：

$$
\ell>0,
$$

定義 near coefficient：

$$
\boxed{
A_{u,q}(\ell)
=
\int_{|z|\le\ell}
\frac{
\|\delta_zu\|_{p_u}
\|\delta_zq\|_{p_q}
}{
|z|^3
}
dz,
}
\tag{17.2}
$$

以及 far coefficient：

$$
\boxed{
B_{u,q}(\ell)
=
\int_{|z|>\ell}
\frac{
\|\delta_zu\|_{p_u}
\|\delta_zq\|_{p_q}
}{
|z|^4
}
dz.
}
\tag{17.3}
$$

使用：

$$
\|\delta_zE\|_2
\le
|z|
\|\nabla E\|_2
$$

near，

以及：

$$
\|\delta_zE\|_2
\le
2\|E\|_2
$$

far，

得到：

$$
\boxed{
\left|
\langle
E,\mathcal K_uq
\rangle
\right|
\le
C
A_{u,q}(\ell)
\|\nabla E\|_2
+
C
B_{u,q}(\ell)
\|E\|_2.
}
\tag{17.4}
$$

---

# 18. Viscous absorption of the near commutator

Young：

$$
\boxed{
C
A_{u,q}
\|\nabla E\|_2
\le
\frac{\nu}{4}
\|\nabla E\|_2^2
+
\frac{
C
}{
\nu
}
A_{u,q}^2.
}
\tag{18.1}
$$

所以：

$$
\boxed{
\begin{aligned}
\left|
\langle
E,\mathcal K_uq
\rangle
\right|
\le{}&
\frac{\nu}{4}
\|\nabla E\|_2^2
\\
&+
\frac{
C
}{
\nu
}
A_{u,q}(\ell)^2
+
C
B_{u,q}(\ell)
\|E\|_2.
\end{aligned}
}
\tag{18.2}
$$

這是：

$$
\boxed{
\textbf{Pairing-Level Commutator Depletion Estimate}.
}
$$

所以 near-diagonal commutator可以被 defect viscosity吸收一部分。

剩餘成本轉成：

$$
A_{u,q}^2
$$

與 far-field：

$$
B_{u,q}\|E\|_2.
$$

---

# 19. Refined defect-energy inequality

Round 37 defect energy：

$$
\frac12
(\|E\|_2^2)'
+
\nu
\|\nabla E\|_2^2
=
-
\langle
E,\mathscr L_S[E]
\rangle
+
\langle
E,\mathcal F_E^{(0)}
\rangle
+
\langle
E,\mathcal K_uq
\rangle.
$$

套用 Round 37 local linear estimate與 (18.2)：

$$
\boxed{
\begin{aligned}
\frac12
(\|E\|_2^2)'
+
\frac{\nu}{2}
\|\nabla E\|_2^2
\lesssim{}&
\frac1\nu
\|S\|_3^2
\|E\|_2^2
\\
&+
\frac1\nu
\|\mathcal F_E^{(0)}\|_{6/5}^2
\\
&+
\frac1\nu
A_{u,q}(\ell)^2
\\
&+
B_{u,q}(\ell)
\|E\|_2.
\end{aligned}
}
\tag{19.1}
$$

所以 transport–Riesz term不再需要獨立：

$$
\|\mathcal K_uq\|_{6/5}
$$

control。

---

# 20. Conditional triple-increment closure

若 interval：

$$
[0,T]
$$

上：

$$
\boxed{
\int_0^T
\|S\|_3^2dt
<
\infty,
}
\tag{20.1}
$$

$$
\boxed{
\int_0^T
\|\mathcal F_E^{(0)}\|_{6/5}^2dt
<
\infty,
}
\tag{20.2}
$$

以及存在 continuous scale choice：

$$
\ell(t)>0
$$

使：

$$
\boxed{
\int_0^T
A_{u,q}(\ell(t))^2dt
<
\infty,
}
\tag{20.3}
$$

並且 far-field term可積分，

則 defect energy可由 Gronwall控制。

這比 Round 37 的 full commutator norm assumption弱，

但仍不是 basic-energy closure。

---

# 21. Pressure component is exactly transport-neutral

Pressure Self-Commutator Null Identity還有一個概念後果。

因：

$$
\|H\|_2^2
=
\frac23
\|q\|_2^2,
$$

divergence-free transport同時保持 formal：

$$
L^2
$$

pairing的 skew structure。

commutator：

$$
[D_u,\mathcal T_0]
$$

恰好維護：

$$
H=\mathcal T_0q
$$

這個 algebraic isometry relation。

因此：

$$
\boxed{
\textbf{
the transport–Riesz commutator is not an arbitrary pressure noise;
it is the compatibility correction required by transporting a nonlocal pressure response.
}
}
\tag{21.1}
$$

在 affine-response defect energy裡，

真正留下的是 compatibility mismatch with：

$$
C_S^0.
$$

---

# 22. Affine and homogeneous null channels

Triple-Increment Identity立即顯示：

如果任一：

$$
\delta u,
\qquad
\delta E,
\qquad
\delta q
$$

在 relevant pair region為零，

則 pairing vanish。

所以：

## N1 — spatially constant defect

$$
\boxed{
E(x)=E_0
\Rightarrow
\langle E,\mathcal K_uq\rangle=0.
}
$$

## N2 — constant pressure source

$$
\boxed{
q(x)=q_0
\Rightarrow
\mathcal K_uq=0.
}
$$

## N3 — constant velocity

trivial transport null。

stationary affine perfect lock：

$$
E=0,
\qquad
q=\text{constant}
$$

同時位於 N1/N2。

這解釋 Round 36 affine perfect-lock witness為何 commutator完全沉默。

---

# 23. Relation to Onsager-type commutator geometry

Euler / Onsager energy flux分析中，

nonlinear energy transfer可透過 increments與 commutator cancellation表達，

critical total fractional regularity會決定 anomalous flux能否存在。

Round 38 的 operator與物理量不同，

但結構上同樣出現：

$$
\boxed{
\text{singular kernel}
+
\text{multiple increments}
+
\text{critical endpoint summability}.
}
$$

因此可將：

$$
s_u+s_E+s_q=1
$$

稱為：

$$
\boxed{
\text{Onsager-like triple-increment critical geometry}
}
$$

但不是 Onsager theorem本身。

---

# 24. Why this still does not close Pure-C

Round 38 將最粗的：

$$
\|\nabla u\|_\infty
$$

commutator burden大幅削弱。

但尚缺：

1. basic NS energy是否能推出 critical：

   $$
   \mathfrak I_{\rm TR}<\infty;
   $$

2. endpoint：

   $$
   s_u+s_E+s_q=1
   $$

   的 Dini / little-Besov gain；

3. pressure source：

   $$
   q=|S|^2-\frac12|\omega|^2
   $$

   的 critical increment control；

4. defect：

   $$
   E
   $$

   在 endpoint space的 propagation；

5. interaction with Round 37 critical：

   $$
   \|S\|_{L_t^2L_x^3}.
   $$

所以 commutator obstacle被縮小，

但沒有消失。

---

# 25. STOP-C42 — Triple-Increment Endpoint / Critical Dini Gap

$$
\boxed{
\begin{aligned}
\text{layer}
&=
\mathrm{transport\text{-}Riesz\ commutator\ depletion},
\\
\mathcal T_0^\ast\mathcal T_0
&=
\frac23I,
\\
\text{pressure self-commutator pairing}
&=
0,
\\
\text{defect commutator}
&=
\text{triple increment},
\\
\text{kernel singularity}
&=
|z|^{-4},
\\
\text{increment threshold}
&=
s_u+s_E+s_q>1,
\\
\text{critical endpoint}
&=
s_u+s_E+s_q=1,
\\
\text{endpoint obstruction}
&=
\text{Dini/log summability},
\\
\text{near commutator}
&=
\text{partly absorbable by }\nu\|\nabla E\|_2^2,
\\
\text{full commutator norm control}
&=
\text{not required at pairing level},
\\
\text{missing}
&=
\text{unconditional critical increment/Dini control
for }u,E,q,
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
\textbf{STOP-C42:
Triple-Increment Endpoint / Critical Dini Gap}.
}
$$

---

# 26. 24/72 Ledger — Round 38

| Step | object | $B$ | $U$ | $O$ | $L$ | status |
|---|---|---|---|---|---|---|
| C568 | $\mathcal T_0$ Fourier symbol | $\mathsf C$ | Fourier integral | tensor | $\mathsf F$ | EXACT |
| C569 | $\mathcal T_0^\ast\mathcal T_0=2I/3$ | $\mathsf C$ | multiplier algebra | scalar | $\mathsf F$ | EXACT |
| C570 | skew transport | $\mathsf C$ | incompressible transport | relational | $\mathsf F$ | EXACT |
| C571 | Pressure Self-Commutator Null | $\mathsf C$ | operator cancellation | targeted | $\mathsf F$ | PROVED |
| C572 | defect/cofactor commutator reduction | $\mathsf C$ | compatibility | targeted | $\mathsf F$ | EXACT |
| C573 | commutator increment kernel | $\mathsf C$ | singular integral | relational | $\mathsf F$ | EXACT |
| C574 | pair kernel symmetry | $\mathsf C$ | exchange symmetry | relational | $\mathsf F$ | EXACT |
| C575 | Triple-Increment Pairing Identity | $\mathsf C$ | pair integration | targeted | $\mathsf F$ | EXACT |
| C576 | cofactor/source increment factorization | $\mathsf C$ | local algebra | relational | $\mathsf F$ | EXACT |
| C577 | critical increment budget $\mathfrak I_{\rm TR}$ | $\mathsf C$ | continuous increments | scalar | $\mathsf F$ | FORM |
| C578 | exact scaling of $\mathfrak I_{\rm TR}$ | $\mathsf C$ | scaling | scalar | $\mathsf F$ | PROVED |
| C579 | continuous modulus criterion | $\mathsf C$ | continuous scale | profile | $\mathsf F$ | PROVED |
| C580 | one-total-derivative threshold | $\mathsf C$ | fractional regularity | scalar | $\mathsf F$ | PROVED |
| C581 | critical Dini endpoint | $\mathsf C$ | endpoint summability | targeted | $\mathsf F$ | IDENTIFIED |
| C582 | near/far continuous split | $\mathsf C$ | scale integral | profile | $\mathsf F$ | PROVED |
| C583 | viscous near-commutator absorption | $\mathsf C$ | defect energy | targeted | $\mathsf F$ | PROVED |
| C584 | refined defect-energy inequality | $\mathsf C$ | energy synthesis | scalar | $\mathsf F$ | CONDITIONAL |
| C585 | full norm route necessity | $\mathsf C$ | commutator analysis | targeted | $\mathsf F$ | REFUTED at pairing level |
| C586 | unconditional critical Dini closure | $\mathsf C$ | coupled NS | targeted | $\mathsf F$ | OPEN / STOP-C42 |

---

# 27. Continuous-versus-discrete status

本輪刻意沒有使用：

- Littlewood–Paley shell index；
- dyadic decomposition；
- Fourier mode lattice；
- discrete scale sequence。

核心 carrier是：

$$
\boxed{
z\in\mathbb R^3
}
$$

的 continuous translation increments，

與：

$$
\boxed{
r\in(0,\infty)
}
$$

的 continuous modulus integral。

即使提到 Besov / Onsager-like endpoint，

實際 proof obligation已寫成 continuous Dini integral：

$$
\int
\frac{
\omega_u(r)\omega_E(r)\omega_q(r)
}{
r^2
}dr.
$$

所以：

$$
\boxed{
T_{\mathsf C\to\mathsf D}
=
\text{NOT YET REACHED}.
}
$$

---

# 28. Strongest results of Round 38

## R38-A — Pressure Self-Commutator Null

$$
\boxed{
\left\langle
H_p^0,
[u\cdot\nabla,\mathcal T_0]q
\right\rangle
=
0.
}
$$

## R38-B — Exact triple-increment pairing

$$
\boxed{
\begin{aligned}
\left\langle
E_p,
[u\cdot\nabla,\mathcal T_0]q
\right\rangle
=
-\frac12
\iint
&
[
\delta u\cdot\nabla K_0
]
:
\delta E_p
\,
\delta q.
\end{aligned}
}
$$

## R38-C — critical increment budget

$$
\boxed{
\left|
\langle
E_p,\mathcal K_uq
\rangle
\right|
\lesssim
\int
\frac{
\|\delta_zu\|_{p_u}
\|\delta_zE_p\|_{p_E}
\|\delta_zq\|_{p_q}
}{
|z|^4
}dz.
}
$$

## R38-D — exact one-total-derivative threshold

$$
\boxed{
s_u+s_E+s_q>1
}
$$

gives local absolute convergence，

while：

$$
\boxed{
s_u+s_E+s_q=1
}
$$

is the NS scale-critical logarithmic endpoint。

## R38-E — pairing-level viscosity absorption

$$
\boxed{
|\langle E,\mathcal K_uq\rangle|
\le
\frac{\nu}{4}\|\nabla E\|_2^2
+
\frac C\nu A_{u,q}^2
+
CB_{u,q}\|E\|_2.
}
$$

所以 full commutator norm control不是 defect-energy route的必要條件。

---

# 29. Next round — Critical Endpoint Closure / Dini Gain

Round 38 將 transport–Riesz obstruction壓成：

$$
\boxed{
s_u+s_E+s_q=1
}
$$

critical endpoint。

下一輪直接研究：

1. NS viscosity是否能對：
   $$
   E_p
   $$
   提供足夠 little-scale gain；

2. pressure source：
   $$
   q=|S|^2-\frac12|\omega|^2
   $$
   的 increment是否因 strain–vorticity cancellation比 generic quadratic source更好；

3. incompressibility能否讓：
   $$
   \delta u
   $$
   的 longitudinal part進一步消失；

4. continuous modulus：
   $$
   \omega_u(r)\omega_E(r)\omega_q(r)
   $$
   是否有 extra $o(r)$；

5. 若只有 exact critical：
   $$
   O(r),
   $$
   是否可由 logarithmic viscosity / parabolic smoothing得到 Dini summability；

6. 若 endpoint仍無 gain，這將成為一個真正 representation-stable critical obstruction；

7. 全程保持 continuous scales，不切 dyadic shells。

---

# 30. External primary-source anchors

1. Borys Álvarez-Samaniego, Wilson P. Álvarez-Samaniego, Pedro G. Fernández-Dalgo, *On the use of the Riesz transforms to determine the pressure term in the incompressible Navier-Stokes equations on the whole space*, arXiv:2004.02588.
   - whole-space pressure的 Riesz-transform representation背景。

2. Elias Hess-Childs, Matthew Rosenzweig, Sylvia Serfaty, *Another look at regularity in transport-commutator estimates*, arXiv:2601.02326.
   - Riesz-type transport commutator對 velocity regularity敏感；一般情況下常用 Lipschitz gradient control不能任意降到 BMO。

3. Matthew Rosenzweig, Sylvia Serfaty, *Sharp commutator estimates of all order for Coulomb and Riesz modulated energies*, arXiv:2407.15650.
   - Riesz interaction transport derivatives可被視為 commutator quadratic forms，並利用其特殊 cancellation structure建立 sharp estimates。

4. A. Cheskidov, P. Constantin, S. Friedlander, R. Shvydkoy, *Energy conservation and Onsager's conjecture for the Euler equations*, arXiv:0704.0759.
   - 用 fractional regularity / flux cancellation描述 Euler critical energy transfer的 primary-source背景；
   - 本輪只將其視為 increment-criticality的 structural analogy，不把 Round 38 等同於 Onsager theorem。

本輪 $\mathcal T_0^\ast\mathcal T_0=2I/3$、Pressure Self-Commutator Null Identity、Triple-Increment Pairing Identity、critical increment scaling與 Pairing-Level Commutator Depletion Estimate均為本文直接推導。

---

# 31. Commit state

$$
\boxed{
\begin{aligned}
\text{Route}
&=
\mathrm{Pure\ Continuous\ Transport\text{-}Riesz\ Commutator\ Depletion},
\\
\text{Essential }\mathsf C\to\mathsf D
&=
\mathrm{Not\ reached},
\\
\text{Pressure self commutator}
&=
0,
\\
\text{Defect commutator}
&=
\mathrm{triple\ increment},
\\
\text{Critical regularity}
&=
s_u+s_E+s_q=1,
\\
\text{Subcritical closure}
&=
s_u+s_E+s_q>1,
\\
\text{Endpoint}
&=
\mathrm{continuous\ Dini/log\ barrier},
\\
\text{Near commutator}
&=
\mathrm{viscously\ absorbable\ conditionally},
\\
\text{Full commutator norm}
&=
\mathrm{not\ required},
\\
\text{STOP-C42}
&=
\mathrm{Triple\text{-}Increment\ Endpoint/Critical\ Dini\ Gap},
\\
\text{Next}
&=
\mathrm{Critical\ Endpoint\ Closure/Dini\ Gain}.
\end{aligned}
}
$$
