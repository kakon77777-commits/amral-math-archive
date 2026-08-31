# NS × X 積分 × 24/72 範式實戰
## Round 36 — Pure Continuous Cofactor–Pressure Coherence Dynamics / Moving-Sign-Domain Route

- 日期：2026-08-17
- 版本：v0.1
- 狀態：Proof-Route Experiment / Continuous-Only Pressure-Coherence-Dynamics Branch
- canonical source：UTF-8 Markdown
- canonical math delimiters：inline `$...$`；display `$$...$$`
- 前一輪：`NS_X72_Round35_PureContinuous_CancellationReplenishment_Closure_v0.1_2026-08-17.md`
- 本輪目標：Round 35 已把 anisotropic pressure replenishment壓成 cofactor–pressure coherence
  $$
  \rho_p^-.
  $$
  本輪建立其 moving-sign-domain exact dynamics：推導 trace-free cofactor tensor的 material equation、anisotropic pressure Hessian的 Riesz/transport-commutator equation、negative-determinant domain boundary velocity與 normalized Hilbert-coherence evolution。檢驗 replenishing coherence是否自動 dephase，或可形成 exact/near phase locking。
- 非主張：本文沒有證明 finite-energy Navier–Stokes flow存在 persistent perfect replenishing lock，也沒有證明 coherence一定快速旋轉。本文反而構造 stationary affine structural witness，排除 universal dephasing；真正 obstruction落在 pressure-response commutator、moving sign boundary與 relative angular forcing的 spacetime control。

---

# 0. Round 35 handoff

令：

$$
d=-\det S.
$$

negative determinant reserve region：

$$
\boxed{
A_-(t)
=
\{x:d(x,t)<0\}.
}
\tag{0.1}
$$

trace-free cofactor：

$$
\boxed{
C
=
C_S^0
=
S^2-\frac13|S|^2I.
}
\tag{0.2}
$$

anisotropic pressure Hessian：

$$
\boxed{
H
=
H_p^0
=
H_p-\frac{\Delta p}{3}I.
}
\tag{0.3}
$$

Round 35 replenishing coherence：

$$
\boxed{
\rho_p^-
=
-
\frac{
\int_{A_-}
C:H\,dx
}{
\|C\|_{2,A_-}
\|H\|_{2,A_-}
}.
}
\tag{0.4}
$$

anisotropic pressure replenishment：

$$
\boxed{
\mathcal P_{\rm aniso}
=
2
\rho_p^-
\|C\|_{2,A_-}
\|H\|_{2,A_-}.
}
\tag{0.5}
$$

Round 35 STOP：

$$
\boxed{
\text{STOP-C39}
=
\text{Replenishment-Closure / Cofactor–Pressure Coherence Gap}.
}
$$

---

# 1. Cofactor tensor as a polynomial of strain

對 trace-free symmetric：

$$
S,
$$

定義：

$$
C
=
S^2-\frac13|S|^2I.
$$

Round 35 已證：

$$
\boxed{
|C|
=
\frac{|S|^2}{\sqrt6}.
}
\tag{1.1}
$$

因此：

$$
C
$$

是 strain spectral shape的一個 normalized quadratic carrier。

---

# 2. Exact material dynamics of the trace-free cofactor

令：

$$
G
=
D_tS.
$$

直接 differentiation：

$$
\boxed{
D_tC
=
GS+SG
-
\frac23
(S:G)I.
}
\tag{2.1}
$$

Navier–Stokes strain equation：

$$
\boxed{
G
=
\nu\Delta S
-
S^2
-
\frac14\omega\otimes\omega
+
\frac14|\omega|^2I
-
H_p.
}
\tag{2.2}
$$

所以：

$$
D_tC
=
\mathcal A_\nu
+
\mathcal A_{\rm self}
+
\mathcal A_\omega
+
\mathcal A_p.
$$

---

# 3. Viscous cofactor forcing

$$
\boxed{
\mathcal A_\nu
=
\nu
\left[
(\Delta S)S
+
S(\Delta S)
-
\frac23
(S:\Delta S)I
\right].
}
\tag{3.1}
$$

這是 higher-derivative angular/amplitude forcing。

---

# 4. Self-amplification cofactor dynamics

對：

$$
G_{\rm self}
=
-S^2,
$$

由 Cayley–Hamilton：

$$
S^3
=
\frac12|S|^2S
+
(\det S)I,
$$

以及：

$$
\operatorname{tr}(S^3)=3\det S,
$$

得到：

$$
\boxed{
\mathcal A_{\rm self}
=
-|S|^2S.
}
\tag{4.1}
$$

這是第一個重要差異：

$$
\boxed{
-S^2
}
$$

不直接旋轉 strain eigenframe，

但一般會改變 trace-free cofactor在五維 tensor space中的方向。

---

# 5. Vorticity contribution to cofactor dynamics

對：

$$
G_\omega
=
-\frac14\omega\otimes\omega
+
\frac14|\omega|^2I,
$$

有：

$$
\boxed{
\begin{aligned}
\mathcal A_\omega
={}&
-\frac14
\left[
(\omega\otimes\omega)S
+
S(\omega\otimes\omega)
\right]
\\
&+
\frac12|\omega|^2S
+
\frac16
(\omega^\top S\omega)I.
\end{aligned}
}
\tag{5.1}
$$

其 trace精確為零。

---

# 6. Pressure contribution to cofactor dynamics

對：

$$
G_p=-H_p,
$$

有：

$$
\boxed{
\mathcal A_p
=
-
(H_pS+SH_p)
+
\frac23
(S:H_p)I.
}
\tag{6.1}
$$

所以 pressure不只作為：

$$
H_p^0
$$

與：

$$
C
$$

的外部 coherence partner，

也直接進入：

$$
C
$$

本身的 dynamics。

這形成一個 closed nonlocal feedback loop：

$$
\boxed{
S
\to
C(S)
\leftrightarrow
H_p
\to
D_tS
\to
D_tC.
}
$$

---

# 7. Self-amplification cofactor angular speed

定義 normalized cofactor：

$$
\widehat C
=
\frac{C}{|C|}
$$

於：

$$
|S|>0.
$$

self contribution的 angular component：

$$
\boxed{
P_C^\perp
\mathcal A_{\rm self}
=
-|S|^2
P_C^\perp S.
}
\tag{7.1}
$$

而：

$$
\boxed{
C:S
=
3\det S,
}
\tag{7.2}
$$

$$
\boxed{
|C|^2
=
\frac16|S|^4.
}
\tag{7.3}
$$

所以：

$$
\boxed{
|P_C^\perp S|^2
=
|S|^2
-
\frac{
54(\det S)^2
}{
|S|^4
}.
}
\tag{7.4}
$$

定義 self cofactor angular rate：

$$
\boxed{
\Omega_{C,\rm self}
=
\frac{
|P_C^\perp\mathcal A_{\rm self}|
}{
|C|
}.
}
\tag{7.5}
$$

得到：

$$
\boxed{
\Omega_{C,\rm self}
=
\sqrt6
|S|
\sqrt{
1-
\frac{
54(\det S)^2
}{
|S|^6
}
}.
}
\tag{7.6}
$$

---

# 8. Axisymmetric cofactor-shape lock

sharp determinant inequality：

$$
|\det S|
\le
\frac1{
3\sqrt6
}
|S|^3
$$

等價於：

$$
\frac{
54(\det S)^2
}{
|S|^6
}
\le1.
$$

所以：

$$
\boxed{
\Omega_{C,\rm self}=0
}
$$

恰在 determinant-shape extremal branch：

$$
\boxed{
\operatorname{spec}(S)
\propto
(-2,1,1)
}
$$

或 sign reversal。

因此：

$$
\boxed{
\textbf{
strain self-amplification rotates cofactor shape
unless the strain spectrum is axisymmetric/extremal.
}
}
\tag{8.1}
$$

這和 Round 23 spectral-shape leakage重新接上。

---

# 9. Pressure source scalar

定義：

$$
\boxed{
q
=
|S|^2
-
\frac12|\omega|^2.
}
\tag{9.1}
$$

pressure Poisson：

$$
\boxed{
-\Delta p=q.
}
\tag{9.2}
$$

令 trace-free Riesz operator：

$$
\boxed{
\mathcal T_0
=
\nabla^2(-\Delta)^{-1}
+
\frac13I.
}
\tag{9.3}
$$

則：

$$
\boxed{
H
=
H_p^0
=
\mathcal T_0q.
}
\tag{9.4}
$$

---

# 10. Exact material equation for the pressure source

由 strain與vorticity equations：

$$
\boxed{
\begin{aligned}
D_tq
={}&
\nu\Delta q
-
2\nu|\nabla S|^2
+
\nu|\nabla\omega|^2
\\
&-
6\det S
-
\frac32
\omega^\top S\omega
-
2S:H_p.
\end{aligned}
}
\tag{10.1}
$$

定義：

$$
\boxed{
\mathcal N_q
=
-2\nu|\nabla S|^2
+
\nu|\nabla\omega|^2
-
6\det S
-
\frac32\omega^\top S\omega
-
2S:H_p.
}
\tag{10.2}
$$

所以：

$$
\boxed{
D_tq
=
\nu\Delta q
+
\mathcal N_q.
}
\tag{10.3}
$$

---

# 11. Exact anisotropic pressure-Hessian dynamics

因：

$$
H=\mathcal T_0q
$$

且：

$$
\mathcal T_0
$$

commutes with：

$$
\Delta,
$$

material derivative：

$$
\boxed{
D_tH
=
\nu\Delta H
+
\mathcal T_0\mathcal N_q
+
[u\cdot\nabla,\mathcal T_0]q.
}
\tag{11.1}
$$

命名 transport–Riesz commutator：

$$
\boxed{
\mathcal C_{u,\mathcal T_0}[q]
=
[u\cdot\nabla,\mathcal T_0]q.
}
\tag{11.2}
$$

所以 pressure anisotropy dynamics由三類 source：

1. viscous smoothing：
   $$
   \nu\Delta H;
   $$
2. nonlocal transformed scalar production：
   $$
   \mathcal T_0\mathcal N_q;
   $$
3. transport/nonlocal noncommutation：
   $$
   \mathcal C_{u,\mathcal T_0}[q].
   $$

---

# 12. Why pressure coherence is a commutator problem

若：

$$
u\cdot\nabla
$$

與：

$$
\mathcal T_0
$$

commuted，

pressure anisotropy只需跟隨：

$$
q
$$

的 material production。

但 actual NS多出：

$$
\boxed{
[u\cdot\nabla,\mathcal T_0]q.
}
$$

所以 pressure tensor相對 local strain/cofactor frame的 dynamics包含真正 nonlocal transport mismatch。

因此：

$$
\boxed{
\textbf{
cofactor–pressure coherence stability is partly a transport–Riesz commutator problem.
}
}
\tag{12.1}
$$

---

# 13. Moving negative-determinant domain

negative reserve domain：

$$
A_-(t)
=
\{d<0\}.
$$

Round 33 determinant scalar PDE：

$$
\boxed{
D_td
-
\nu\Delta d
=
F_d,
}
\tag{13.1}
$$

其中：

$$
F_d
=
\nu\mathcal G_{\det}
+
\frac14|S\omega|^2
+
\operatorname{cof}S:H_p.
$$

假設：

$$
\nabla d\ne0
$$

on：

$$
\partial A_-(t).
$$

outward normal：

$$
\boxed{
\eta
=
\frac{
\nabla d
}{
|\nabla d|
}.
}
\tag{13.2}
$$

---

# 14. Exact sign-boundary velocity

令：

$$
V_n
$$

為：

$$
\partial A_-
$$

的 Eulerian normal velocity。

由 level-set kinematics：

$$
\boxed{
V_n
=
u\cdot\eta
-
\beta_d,
}
\tag{14.1}
$$

其中：

$$
\boxed{
\beta_d
=
\frac{
\nu\Delta d
+
F_d
}{
|\nabla d|
}
=
\frac{
D_td
}{
|\nabla d|
}.
}
\tag{14.2}
$$

所以 sign interface相對 fluid本身的 normal velocity是：

$$
\boxed{
V_n-u\cdot\eta
=
-\beta_d.
}
\tag{14.3}
$$

---

# 15. Moving-domain transport law

對 smooth scalar/tensor contraction：

$$
\Phi,
$$

且：

$$
\nabla\cdot u=0,
$$

有：

$$
\boxed{
\frac d{dt}
\int_{A_-(t)}
\Phi\,dx
=
\int_{A_-}
D_t\Phi\,dx
-
\int_{\partial A_-}
\beta_d
\Phi\,dS.
}
\tag{15.1}
$$

所以 cofactor–pressure coherence有第三種 dynamics：

$$
\boxed{
\text{sign-domain boundary replacement}.
}
$$

即使：

$$
C,H
$$

在 fixed spatial points不變，

changing：

$$
A_-
$$

也可改變 integrated coherence。

---

# 16. Moving-domain Hilbert vectors

定義：

$$
\boxed{
B
=
-H.
}
\tag{16.1}
$$

這樣 replenishing coherence：

$$
\boxed{
\rho
=
\rho_p^-
=
\frac{
\int_{A_-}
C:B\,dx
}{
UV
},
}
\tag{16.2}
$$

其中：

$$
\boxed{
U
=
\|C\|_{2,A_-},
\qquad
V
=
\|B\|_{2,A_-}.
}
\tag{16.3}
$$

令：

$$
\widehat C
=
C/U,
$$

$$
\widehat B
=
B/V
$$

作為 moving-domain $L^2$ unit tensors。

---

# 17. Exact moving-domain coherence dynamics

令：

$$
\boxed{
\mathcal A_C
=
D_tC,
}
\tag{17.1}
$$

$$
\boxed{
\mathcal A_B
=
D_tB
=
-D_tH.
}
\tag{17.2}
$$

則：

$$
\boxed{
\begin{aligned}
\rho'
={}&
\frac1U
\int_{A_-}
\mathcal A_C:
(
\widehat B-\rho\widehat C
)
dx
\\
&+
\frac1V
\int_{A_-}
\mathcal A_B:
(
\widehat C-\rho\widehat B
)
dx
\\
&+
\mathcal B_{\rm sign}.
\end{aligned}
}
\tag{17.3}
$$

其中 moving-sign-boundary correction：

$$
\boxed{
\begin{aligned}
\mathcal B_{\rm sign}
={}&
-
\frac1{UV}
\int_{\partial A_-}
\beta_d
C:B\,dS
\\
&+
\frac{\rho}{2U^2}
\int_{\partial A_-}
\beta_d
|C|^2dS
\\
&+
\frac{\rho}{2V^2}
\int_{\partial A_-}
\beta_d
|B|^2dS.
\end{aligned}
}
\tag{17.4}
$$

命名：

$$
\boxed{
\textbf{Moving-Domain Cofactor–Pressure Coherence Equation}.
}
$$

---

# 18. Three angular drivers

Equation (17.3) 將：

$$
\rho_p^-
$$

的變化分成：

## A — cofactor angular dynamics

$$
\boxed{
D_tC
}
$$

由：

- self-amplification shape；
- viscosity；
- vorticity；
- pressure；

驅動。

## B — pressure-response angular dynamics

$$
\boxed{
D_tH
}
$$

由：

- pressure-source production；
- viscosity；
- transport–Riesz commutator；

驅動。

## C — moving sign-domain dynamics

$$
\boxed{
\mathcal B_{\rm sign}
}
$$

由：

$$
d=0
$$

interface的 relative motion驅動。

所以 persistent pressure replenishment是一個三層 locking問題。

---

# 19. Interior angular-speed bound

定義 cofactor tangent speed：

$$
\boxed{
\Omega_C
=
\frac{
\left\|
P_{\widehat C}^{\perp}
\mathcal A_C
\right\|_{2,A_-}
}{
U
}.
}
\tag{19.1}
$$

定義 pressure tangent speed：

$$
\boxed{
\Omega_H
=
\frac{
\left\|
P_{\widehat B}^{\perp}
\mathcal A_B
\right\|_{2,A_-}
}{
V
}.
}
\tag{19.2}
$$

因：

$$
\|
\widehat B-\rho\widehat C
\|_2
=
\sqrt{
1-\rho^2
},
$$

有：

$$
\boxed{
|
\rho'
-
\mathcal B_{\rm sign}
|
\le
\sqrt{
1-\rho^2
}
(
\Omega_C+\Omega_H
).
}
\tag{19.3}
$$

若：

$$
|\rho|<1,
$$

定義：

$$
\theta
=
\arccos\rho.
$$

則：

$$
\boxed{
\left|
\theta'
+
\frac{
\mathcal B_{\rm sign}
}{
\sqrt{
1-\rho^2
}
}
\right|
\le
\Omega_C+\Omega_H.
}
\tag{19.4}
$$

---

# 20. Coherence persistence burden

若：

$$
\rho\approx1
$$

要長時間保持，

必須同時控制：

$$
\boxed{
\text{relative cofactor/pressure tangent motion}
}
$$

以及：

$$
\boxed{
\text{moving-sign-domain boundary flux}.
}
$$

因此：

$$
\boxed{
\text{pressure coherence lock}
}
$$

不是單一 local alignment。

它要求：

$$
\boxed{
\mathcal A_C
\approx
\text{normalized }\mathcal A_B
}
$$

on tangent directions，

且：

$$
\mathcal B_{\rm sign}
$$

不能快速拆散 lock。

---

# 21. Self-amplification does not guarantee dephasing

Round 27：

$$
-S^2
$$

不直接旋轉 strain eigenframe。

Round 36：

$$
-S^2
$$

一般會旋轉：

$$
C_S^0
$$

在 tensor-shape space中的方向，

但：

$$
\boxed{
\Omega_{C,\rm self}=0
}
$$

on axisymmetric determinant-extremal shapes。

所以 dangerous shape可以存在：

$$
\boxed{
\text{large self-amplification}
+
\text{zero self-induced cofactor dephasing}.
}
$$

因此沒有 universal：

$$
\boxed{
\text{dangerous strain}
\Rightarrow
\Omega_C\ge c|S|
}
$$

with fixed：

$$
c>0.
$$

---

# 22. Affine Perfect Coherence-Lock Witness

令 constant trace-free symmetric matrix：

$$
S_0.
$$

取 affine velocity：

$$
\boxed{
u(x)=S_0x.
}
\tag{22.1}
$$

以及 quadratic pressure：

$$
\boxed{
p(x)
=
-\frac12
x^\top
S_0^2
x.
}
\tag{22.2}
$$

則：

$$
\nabla\cdot u=0,
$$

$$
\Delta u=0,
$$

且：

$$
(u\cdot\nabla)u
=
S_0^2x
=
-\nabla p.
$$

所以這是 stationary affine Euler solution，亦滿足 viscous NS equation因：

$$
\Delta u=0.
$$

它不是 whole-space finite-energy solution。

---

# 23. Perfect cofactor–pressure anti-alignment

對 affine witness：

$$
H_p
=
-S_0^2.
$$

因此：

$$
\boxed{
H_p^0
=
-
\left(
S_0^2
-
\frac13|S_0|^2I
\right)
=
-C_0.
}
\tag{23.1}
$$

所以：

$$
\boxed{
B=-H_p^0=C_0.
}
$$

在任何有限 test region上：

$$
\boxed{
\rho_p^-=1.
}
\tag{23.2}
$$

並且：

$$
\boxed{
\rho_p^-(t)
\equiv1.
}
$$

若選：

$$
S_0
=
\operatorname{diag}(-1,-1,2),
$$

則：

$$
\det S_0=2,
$$

所以：

$$
d=-2<0.
$$

整個 local region都位於 negative determinant reserve branch。

因此：

$$
\boxed{
\textbf{
there is no universal positive lower bound on cofactor–pressure dephasing speed.
}
}
\tag{23.3}
$$

此 witness只排除 purely local/geometric universal dephasing，不宣稱 finite-energy global regularity counterexample。

---

# 24. What locks in the affine witness

在 stationary affine witness：

- cofactor tensor固定；
- anisotropic pressure Hessian固定；
- sign domain固定；
- transport–Riesz response整體精確平衡；
- coherence：
  $$
  \rho=1.
  $$

所以 actual dephasing必須來自：

$$
\boxed{
\text{spatial inhomogeneity}
+
\text{viscous gradients}
+
\text{vorticity geometry}
+
\text{nonlocal pressure response}
+
\text{sign-interface motion}.
}
$$

不是 tensor algebra本身自動提供。

---

# 25. Pressure-response budget

由：

$$
D_tH
=
\nu\Delta H
+
\mathcal T_0\mathcal N_q
+
\mathcal C_{u,\mathcal T_0}[q],
$$

得到 schematic：

$$
\boxed{
\Omega_H
\lesssim
\frac{
\nu\|\Delta H\|_{2,A_-}
+
\|\mathcal T_0\mathcal N_q\|_{2,A_-}
+
\|\mathcal C_{u,\mathcal T_0}[q]\|_{2,A_-}
}{
\|H\|_{2,A_-}
}.
}
\tag{25.1}
$$

所以若要證：

$$
\rho
$$

快速 dephase，

必須對 pressure angular forcing有 lower information；

若要證 persistent lock expensive，

則需 upper/control information。

兩者都需要真正 nonlocal pressure-response estimates。

---

# 26. Commutator regularity burden

transport–Riesz commutator：

$$
\boxed{
[u\cdot\nabla,\mathcal T_0]q
}
$$

對 velocity regularity敏感。

因此：

$$
\boxed{
\text{pressure coherence dynamics}
}
$$

再次接回：

- velocity-gradient control；
- singular-integral commutator estimates；
- higher spatial regularity。

這與 Round 30 budget recycling一致：

$$
\boxed{
\text{representation合法}
\neq
\text{commutator budget免費}.
}
$$

---

# 27. Moving-sign boundary is an independent leakage channel

即使：

$$
\mathcal A_C
$$

與：

$$
\mathcal A_B
$$

在 interior完美 lock，

若：

$$
\beta_d
$$

在：

$$
d=0
$$

surface上重新選取高/低 coherence regions，

則：

$$
\mathcal B_{\rm sign}
$$

仍可讓：

$$
\rho
$$

改變。

所以：

$$
\boxed{
\text{fixed-domain coherence control}
}
$$

不能直接推出：

$$
\boxed{
\text{negative-reserve-domain coherence control}.
}
$$

真正 global route需要：

$$
\boxed{
\text{tensor dynamics}
+
\text{pressure response}
+
\text{level-set transport}.
}
$$

---

# 28. Smooth-mask formulation

若：

$$
d=0
$$

不是 regular level set，

可用 smooth mask：

$$
\boxed{
\chi_{\varepsilon}^-(d)
=
\chi(-d/\varepsilon)
}
\tag{28.1}
$$

with smooth monotone：

$$
\chi.
$$

定義 weighted coherence：

$$
\boxed{
\rho_{\varepsilon}
=
-
\frac{
\int
\chi_\varepsilon^-(d)
C:Hdx
}{
\left(
\int
\chi_\varepsilon^-(d)|C|^2dx
\right)^{1/2}
\left(
\int
\chi_\varepsilon^-(d)|H|^2dx
\right)^{1/2}
}.
}
\tag{28.2}
$$

所有 time derivatives皆為 classical weighted integrals。

再研究：

$$
\varepsilon\downarrow0.
$$

所以 moving-domain singularities不迫使離散 sign cells。

---

# 29. Coherence-lock alternatives

long-lived positive：

$$
\rho_p^-
$$

目前只能靠：

$$
\boxed{
\begin{aligned}
\mathrm{L1}:&
\quad
\text{axisymmetric/extremal cofactor-shape slowing},
\\
\mathrm{L2}:&
\quad
\text{pressure-response tangent locking},
\\
\mathrm{L3}:&
\quad
\text{transport–Riesz commutator balance},
\\
\mathrm{L4}:&
\quad
\text{moving sign-domain boundary balance},
\\
\mathrm{L5}:&
\quad
\text{strong amplitude modulation masking angular drift}.
\end{aligned}
}
\tag{29.1}
$$

沒有一條是 purely algebraic free regularizer。

---

# 30. STOP-C40 — Cofactor–Pressure Lock / Moving-Domain Commutator Gap

$$
\boxed{
\begin{aligned}
\text{layer}
&=
\mathrm{cofactor\text{-}pressure\ coherence\ dynamics},
\\
\text{cofactor equation}
&=
D_tC
=
\mathcal A_\nu
+
\mathcal A_{\rm self}
+
\mathcal A_\omega
+
\mathcal A_p,
\\
\text{self cofactor angular rate}
&=
\sqrt6|S|
\sqrt{
1-54(\det S)^2/|S|^6
},
\\
\text{axisymmetric self dephasing}
&=
0,
\\
\text{pressure anisotropy}
&=
\mathcal T_0q,
\\
\text{pressure dynamics}
&=
\nu\Delta H
+
\mathcal T_0\mathcal N_q
+
[u\cdot\nabla,\mathcal T_0]q,
\\
\text{sign-domain dynamics}
&=
\mathcal B_{\rm sign},
\\
\text{perfect local/affine lock}
&=
\mathrm{possible},
\\
\text{universal dephasing}
&=
\mathrm{false},
\\
\text{missing}
&=
\mathrm{finite\text{-}energy\ spacetime\ control
of\ relative\ tensor\ angular\ forcing,
transport\text{-}Riesz\ commutator,
and\ moving\ sign\ boundary},
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
\textbf{STOP-C40:
Cofactor–Pressure Lock / Moving-Domain Commutator Gap}.
}
$$

---

# 31. 24/72 Ledger — Round 36

| Step | object | $B$ | $U$ | $O$ | $L$ | status |
|---|---|---|---|---|---|---|
| C532 | cofactor material derivative | $\mathsf C$ | tensor PDE | relational | $\mathsf F$ | EXACT |
| C533 | self-amplification cofactor term | $\mathsf C$ | tensor algebra | targeted | $\mathsf F$ | EXACT |
| C534 | vorticity cofactor forcing | $\mathsf C$ | tensor coupling | relational | $\mathsf F$ | EXACT |
| C535 | pressure cofactor forcing | $\mathsf C$ | tensor coupling | relational | $\mathsf F$ | EXACT |
| C536 | self cofactor angular speed | $\mathsf C$ | tensor geometry | scalar | $\mathsf F$ | PROVED |
| C537 | axisymmetric angular lock | $\mathsf C$ | spectral shape | targeted | $\mathsf F$ | PROVED |
| C538 | pressure source $q$ dynamics | $\mathsf C$ | scalar PDE | relational | $\mathsf F$ | EXACT |
| C539 | anisotropic pressure dynamics | $\mathsf C$ | Riesz/transport | tensor | $\mathsf F$ | EXACT |
| C540 | transport–Riesz commutator | $\mathsf C$ | nonlocal transport | relational | $\mathsf F$ | IDENTIFIED |
| C541 | sign-boundary normal velocity | $\mathsf C$ | level-set transport | scalar | $\mathsf F$ | EXACT |
| C542 | moving-domain transport law | $\mathsf C$ | Reynolds transport | relational | $\mathsf F$ | EXACT |
| C543 | moving-domain coherence equation | $\mathsf C$ | Hilbert geometry | scalar | $\mathsf F$ | EXACT |
| C544 | interior angular-speed bound | $\mathsf C$ | tangent geometry | targeted | $\mathsf F$ | PROVED |
| C545 | affine perfect-lock witness | $\mathsf C$ | local affine flow | targeted | $\mathsf F$ | CONSTRUCTED |
| C546 | universal pressure dephasing | $\mathsf C$ | coherence dynamics | targeted | $\mathsf F$ | REFUTED |
| C547 | smooth-mask sign-domain route | $\mathsf C$ | regularization | profile | $\mathsf F$ | LEGAL |
| C548 | finite-energy coherence-lock exclusion | $\mathsf C$ | coupled NS | targeted | $\mathsf F$ | OPEN / STOP-C40 |

---

# 32. Continuous-versus-discrete status

本輪所有核心 objects：

- continuous trace-free tensors；
- continuous Riesz operators；
- continuous commutators；
- continuous level-set velocity；
- continuous moving domains；
- continuous smooth sign masks；
- continuous Hilbert angles。

沒有：

- pressure modes enumeration；
- sign cells；
- discrete eigenframe states；
- graph level-set motion。

因此：

$$
\boxed{
T_{\mathsf C\to\mathsf D}
=
\text{NOT YET REACHED}.
}
$$

---

# 33. Strongest results of Round 36

## R36-A — exact cofactor material dynamics

$$
\boxed{
D_tC
=
(D_tS)S
+
S(D_tS)
-
\frac23
(S:D_tS)I.
}
$$

## R36-B — self-amplification cofactor angular rate

$$
\boxed{
\Omega_{C,\rm self}
=
\sqrt6|S|
\sqrt{
1-
54(\det S)^2/|S|^6
}.
}
$$

## R36-C — exact anisotropic pressure dynamics

$$
\boxed{
D_tH_p^0
=
\nu\Delta H_p^0
+
\mathcal T_0\mathcal N_q
+
[u\cdot\nabla,\mathcal T_0]q.
}
$$

## R36-D — moving sign-domain coherence equation

$$
\boxed{
\rho'
=
\text{cofactor tangent motion}
+
\text{pressure tangent motion}
+
\text{sign-boundary flux}.
}
$$

## R36-E — affine perfect-lock no-go

stationary affine strain gives：

$$
\boxed{
H_p^0=-C_S^0,
\qquad
\rho_p^-=1.
}
$$

所以 universal positive dephasing-speed lower bound不存在。

---

# 34. Next round — Pressure-Response Lock Budget / Commutator Depletion

Round 36 已經知道：

$$
\boxed{
\text{perfect coherence lock在 local affine geometry中可存在}.
}
$$

所以下一輪不再嘗試 pointwise universal dephasing。

直接問：

$$
\boxed{
\text{finite-energy / inhomogeneous NS要維持 near-affine pressure response lock，
到底要支付多少 commutator與 gradient budget？}
}
$$

具體：

1. 定義 affine-response defect：
   $$
   E_p
   =
   H_p^0+C_S^0;
   $$

2. 推導：
   $$
   D_tE_p;
   $$

3. stationary affine lock恰為：
   $$
   E_p=0;
   $$

4. 檢查 viscosity、vorticity、pressure-source nonlocality與 Riesz commutator如何製造：
   $$
   E_p;
   $$

5. 對：
   $$
   \|E_p\|_2^2
   $$
   建立 defect-energy equation；

6. 若 near-lock要求：
   $$
   E_p
   $$
   小，研究維持它所需的 cancellation；

7. 將 commutator budget接 Round 30 higher-gradient / critical regularity；

8. 若 $E_p$ 無法被低階 budget壓住，則 pressure replenishment lock再次不是免費機制。

---

# 35. External primary-source anchors

1. Maurizio Carbone, Michele Iovieno, Andrew D. Bragg, *Gauge symmetry and dimensionality reduction of the anisotropic pressure Hessian*, arXiv:1911.08652.
   - anisotropic pressure Hessian是 velocity-gradient dynamics中的 nonlocal functional，並展現相對 strain eigenframe / vorticity的顯著 alignment structure。

2. Josin Tom, Maurizio Carbone, Andrew D. Bragg, *Exploring the turbulent velocity gradients at different scales from the perspective of the strain-rate eigenframe*, arXiv:2005.04300.
   - strain-rate eigenframe dynamics與 anisotropic pressure Hessian對 eigenframe rotation的重要性。

3. Borys Álvarez-Samaniego, Wilson P. Álvarez-Samaniego, Pedro G. Fernández-Dalgo, *On the use of the Riesz transforms to determine the pressure term in the incompressible Navier-Stokes equations on the whole space*, arXiv:2004.02588.
   - whole-space pressure的 Riesz-transform representation背景。

4. Elias Hess-Childs, Matthew Rosenzweig, Sylvia Serfaty, *Another look at regularity in transport-commutator estimates*, arXiv:2601.02326.
   - Riesz-type transport commutator estimates對 transport velocity regularity敏感的近期 primary-source背景；本輪只作 commutator budget難度之結構錨點。

本輪 cofactor material dynamics、self-cofactor angular-rate identity、pressure-source dynamics、moving sign-domain coherence equation與 affine perfect-lock witness均為本文直接推導。

---

# 36. Commit state

$$
\boxed{
\begin{aligned}
\text{Route}
&=
\mathrm{Pure\ Continuous\ Cofactor\text{-}Pressure\ Coherence\ Dynamics},
\\
\text{Essential }\mathsf C\to\mathsf D
&=
\mathrm{Not\ reached},
\\
\text{Cofactor angular dynamics}
&=
\mathrm{self}
+
\mathrm{viscosity}
+
\mathrm{vorticity}
+
\mathrm{pressure},
\\
\text{Pressure angular dynamics}
&=
\mathrm{source}
+
\mathrm{viscosity}
+
\mathrm{transport\text{-}Riesz\ commutator},
\\
\text{Sign-domain angular dynamics}
&=
\mathrm{moving\ level\text{-}set\ flux},
\\
\text{Universal dephasing}
&=
\mathrm{false},
\\
\text{Perfect local affine lock}
&=
\mathrm{possible},
\\
\text{STOP-C40}
&=
\mathrm{Cofactor\text{-}Pressure\ Lock/Moving\text{-}Domain\ Commutator\ Gap},
\\
\text{Next}
&=
\mathrm{Pressure\text{-}Response\ Lock\ Budget/Commutator\ Depletion}.
\end{aligned}
}
$$
