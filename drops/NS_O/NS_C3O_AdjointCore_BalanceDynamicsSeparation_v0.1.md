---
title: "Navier–Stokes C3-O：Adjoint Core Balance、Cancellation Corridor 與 Balance–Dynamics Separation"
subtitle: "Gauge-Clean Local Strain Balance, Asymptotic Boundary/Self-Amplification Regimes, and Why Energy-Balance Closeness Is Not Dynamical Closeness"
version: "v0.1"
date: "2026-08-14"
author: "Neo.K / EveMissLab"
language: "zh-TW"
status: "Theorem-style structural reduction / no-go note"
epistemic_status: "Exact adjoint-localized strain balance + asymptotic ratio classification + balance-versus-operator no-go. Does NOT prove Navier–Stokes regularity."
---

# Navier–Stokes C3-O
# Adjoint Core Balance、Cancellation Corridor 與 Balance–Dynamics Separation

## 0. 本輪定位

C3-N 已建立 exact localized strain balance：

$$
\frac12\frac d{dt}\int\chi|S|^2
+
\nu\int\chi|\nabla S|^2
=
-2\int\chi\det S
+
\mathcal C_\chi,
$$

其中：

$$
\begin{aligned}
\mathcal C_\chi
={}&
\frac12\int
|S|^2
(
\partial_t\chi
+
u\cdot\nabla\chi
+
\nu\Delta\chi
)
\\
&+
\frac13\int\nabla\chi\cdot F_B
+
\int\nabla\chi\cdot F_p.
\end{aligned}
$$

並且：

$$
F_B
=
\left(
A^2
-\frac12\operatorname{tr}(A^2)I
\right)u,
\qquad
A=\nabla u,
$$

以及：

$$
F_p
=
(\nabla^2p-\Delta p\,I)u.
$$

本輪的第一個問題：

> 能否把 cutoff 自己造成的 gauge/advection/diffusion terms完全剝除？

答案：

$$
\boxed{\textbf{YES}.}
$$

使用 strain transport-diffusion operator的 backward adjoint cutoff即可。

第二個問題：

> 若只剩 bulk strain self-amplification與真正的 boundary current，三種 asymptotic ratio regime能排除哪一些？

答案：

- boundary過度負向：
  $$
  \boxed{\rho\le-1}
  $$
  不能支援 positive local strain-energy growth；
- $\rho\to-1^+$：
  不被排除，但必須支付 increasingly precise gross cancellation；
- $\rho\to0$：
  也不能排除，而且**不能**解讀成 full dynamics接近 strain self-amplification model；
- $\rho\to+\infty$：
  boundary/pressure current成為主要 growth carrier。

最重要的結論：

$$
\boxed{
\text{balance closeness}
\neq
\text{dynamical/operator closeness}.
}
$$

---

# 1. Full strain equation

對 smooth incompressible Navier–Stokes：

$$
\partial_tu
-\nu\Delta u
+
(u\cdot\nabla)u
+
\nabla p
=
0,
$$

$$
\nabla\cdot u=0,
$$

strain：

$$
S
=
\frac12
(\nabla u+\nabla u^\top)
$$

滿足：

$$
\boxed{
\partial_tS
-
\nu\Delta S
+
(u\cdot\nabla)S
+
S^2
+
\frac14\omega\otimes\omega
-
\frac14|\omega|^2I
+
\nabla^2p
=
0.
}
$$

---

# 2. Adjoint cutoff

固定 ancestry window：

$$
I=[t_0,t_1].
$$

取 terminal cutoff：

$$
\chi_1(x)
$$

滿足：

$$
0\le\chi_1\le1,
$$

並 localized near child ancestry core。

令：

$$
\boxed{
\partial_t\chi
+
u\cdot\nabla\chi
+
\nu\Delta\chi
=
0
}
$$

在：

$$
t_0<t<t_1,
$$

以及 terminal condition：

$$
\boxed{
\chi(t_1,x)=\chi_1(x).
}
$$

令：

$$
\tau=t_1-t.
$$

則其變成 forward parabolic equation：

$$
\partial_\tau\chi
=
u(t_1-\tau)\cdot\nabla\chi
+
\nu\Delta\chi.
$$

所以在 smooth pre-singular window中，這是標準 parabolic adjoint construction。

---

# 3. Adjoint ancestry tube

此 cutoff不是固定 ball。

它會：

- backward follow velocity drift；
- backward diffuse over parabolic distance；
- 自動吸收 moving-core gauge和 advection cutoff terms。

本文稱：

$$
\boxed{
\textbf{Adjoint Ancestry Tube}.
}
$$

---

# 4. C3-O.1：Adjoint Core Balance Theorem

## 定理 4.1

若：

$$
\chi
$$

解 adjoint cutoff equation：

$$
\partial_t\chi
+
u\cdot\nabla\chi
+
\nu\Delta\chi
=
0,
$$

則：

$$
\boxed{
\frac12
\frac d{dt}
\int
\chi|S|^2
+
\nu
\int
\chi|\nabla S|^2
=
-2
\int
\chi\det S
+
\int
\nabla\chi\cdot J_{\rm corr},
}
$$

其中：

$$
\boxed{
J_{\rm corr}
=
\frac13F_B+F_p.
}
$$

### 證明

直接代入 C3-N 的 localized strain balance。

因：

$$
\partial_t\chi
+
u\cdot\nabla\chi
+
\nu\Delta\chi
=
0,
$$

第一整組 scalar cutoff terms exactly vanish。$\square$

---

# 5. Gauge-clean variables

定義：

$$
E_\chi(t)
=
\frac12
\int
\chi|S|^2dx,
$$

$$
D_\chi(t)
=
\nu
\int
\chi|\nabla S|^2dx,
$$

$$
A_\chi(t)
=
-2
\int
\chi\det S\,dx,
$$

以及：

$$
B_\chi(t)
=
\int
\nabla\chi\cdot J_{\rm corr}\,dx.
$$

則：

$$
\boxed{
E_\chi'
+
D_\chi
=
A_\chi+B_\chi.
}
$$

---

# 6. Window-integrated balance

對：

$$
I=[t_0,t_1],
$$

定義：

$$
\Delta E_I
=
E_\chi(t_1)-E_\chi(t_0),
$$

$$
D_I
=
\int_I
D_\chi(t)\,dt,
$$

$$
A_I
=
\int_I
A_\chi(t)\,dt,
$$

$$
B_I
=
\int_I
B_\chi(t)\,dt.
$$

則：

$$
\boxed{
\Delta E_I+D_I
=
A_I+B_I.
}
$$

且：

$$
D_I\ge0.
$$

---

# 7. Growth window

稱：

$$
I
$$

為 positive local strain-growth window，若：

$$
\Delta E_I>0.
$$

則：

$$
A_I+B_I
=
\Delta E_I+D_I
>
0.
$$

---

# 8. C3-O.2：Growth-Carrier Dichotomy

## 定理 8.1

對任何 positive local strain-growth window，必有以下之一：

### Branch A — Positive SSA-supported

$$
A_I>0
$$

而：

$$
B_I>-A_I.
$$

### Branch B — Boundary-current-driven

$$
A_I\le0
$$

且必然：

$$
\boxed{
B_I>
|A_I|+D_I.
}
$$

更精確：

$$
B_I
=
\Delta E_I+D_I-A_I.
$$

$\square$

---

# 9. Boundary ratio

在：

$$
A_I>0
$$

的 window定義：

$$
\boxed{
\rho_I
=
\frac{B_I}{A_I}.
}
$$

由 growth：

$$
A_I+B_I>0,
$$

得到：

$$
\boxed{
\rho_I>-1.
}
$$

---

# 10. C3-O.3：Hard Depletion Barrier

## 定理 10.1

若：

$$
A_I>0
$$

且：

$$
\rho_I\le-1,
$$

則：

$$
\boxed{
\Delta E_I\le-D_I\le0.
}
$$

所以此 window不可能是 positive strain-growth window。$\square$

---

# 11. Cancellation corridor

對：

$$
A_I>0,
$$

定義：

$$
\boxed{
\kappa_I
=
1+\rho_I
=
\frac{\Delta E_I+D_I}{A_I}.
}
$$

growth window有：

$$
\kappa_I>0.
$$

---

# 12. C3-O.4：Cancellation-Precision Debt

若：

$$
\rho_I\to-1^+
$$

沿某些 growth windows，

則：

$$
\kappa_I\to0^+.
$$

而：

$$
\boxed{
A_I
=
\frac{\Delta E_I+D_I}{\kappa_I}.
}
$$

所以若：

$$
\Delta E_I+D_I
$$

沒有同比例趨零，

則：

$$
A_I\to\infty,
$$

且：

$$
|B_I|\sim A_I.
$$

即：

$$
\boxed{
\text{large SSA}
+
\text{large opposite boundary current}
+
\text{small residual}.
}
$$

---

# 13. Fixed fractional growth版本

若：

$$
\Delta E_I
\ge
\gamma E_\chi(t_0)
$$

for fixed：

$$
\gamma>0,
$$

則：

$$
\boxed{
A_I
\ge
\frac{
\gamma E_\chi(t_0)
}{
\kappa_I
}.
}
$$

所以：

$$
\kappa_I\to0
$$

時，

gross self-amplification相對 local stock必須增大。

---

# 14. Ratio subsequence classification

考慮 infinitely many positive growth windows：

$$
I_n
$$

且：

$$
A_{I_n}>0.
$$

因：

$$
\rho_n>-1,
$$

可抽 subsequence落入：

## O-A — Cancellation corridor

$$
\rho_n\to-1^+.
$$

## O-B — Finite balance regime

存在：

$$
-1+\delta
\le
\rho_n
\le
M
$$

for some：

$$
\delta>0,
\quad
M<\infty.
$$

## O-C — Boundary-driven regime

$$
\rho_n\to+\infty.
$$

若有 infinitely many：

$$
A_{I_n}\le0
$$

growth windows，

它們自動屬於 boundary-current-driven branch。

---

# 15. Miller operator decomposition

Miller 將 full strain equation寫成：

$$
\boxed{
\partial_tS
-
\nu\Delta S
+
\frac23P_{st}(S^2)
+
\mathcal P_{NS}
=
0,
}
$$

其中：

$$
\boxed{
\mathcal P_{NS}
=
P_{st}
\left(
(u\cdot\nabla)S
+
\frac13S^2
+
\frac14\omega\otimes\omega
\right).
}
$$

strain self-amplification model則是：

$$
\boxed{
\partial_tS
-
\nu\Delta S
+
\frac23P_{st}(S^2)
=
0.
}
$$

---

# 16. Orthogonality

對 full-space strain：

$$
S\in L^2_{st},
$$

有：

$$
\boxed{
\langle
\mathcal P_{NS},
S
\rangle
=
0.
}
$$

所以 full N–S 與 SSA model具有同一 global strain-enstrophy growth identity：

$$
\boxed{
\frac d{dt}
\|S\|_2^2
=
-2\nu\|S\|_{\dot H^1}^2
-
4\int\det S.
}
$$

---

# 17. C3-O.5：Balance–Dynamics Separation No-Go

## 命題 17.1

$$
\langle\mathcal P_{NS},S\rangle=0
$$

不推出：

$$
\mathcal P_{NS}=0.
$$

因此：

$$
\boxed{
\text{the perturbation can be dynamically large while energy-orthogonal}.
}
$$

特別：

whole-space balance對所有 full N–S solutions都有：

$$
B_{\chi\equiv1}=0,
$$

但 full N–S strain equation並不因此等於 SSA model。

所以：

$$
\boxed{
\rho\to0
\not\Rightarrow
\text{dynamical closeness to SSA model}.
}
$$

$\square$

---

# 18. 為何這個 no-go重要？

Miller 的 SSA model：

- 位於同一 strain constraint space；
- 具有同一 enstrophy-growth identity；
- 具有相近的 middle-eigenvalue regularity structure；
- 對一類 initial data可 finite-time blow up。

所以：

$$
\boxed{
\text{strain-energy balance本身不足以區分
full N--S 與可 blow-up 的 SSA model}.
}
$$

---

# 19. Conditional full-N–S warning

Miller 的 SSA-model工作還證明一個 conditional full-N–S blow-up result：

若 full equation中相對 model 被丟掉的 terms滿足該文的 perturbative smallness hypothesis，

則在相應 initial-data條件下 full N–S 也會 finite-time blow up。

本文不重述完整 technical hypothesis。

保留的 structural conclusion是：

$$
\boxed{
\text{「depletion/orthogonal perturbation很小」本身不是 regularity方向。}
}
$$

---

# 20. Operator-level defect

因此真正需要和：

$$
\rho_I
$$

平行追蹤的是：

$$
\mathcal P_{NS}
$$

本身。

一個 scale-compatible candidate：

$$
\boxed{
\mathfrak P_I
=
\frac{
\int_I
\|\mathcal P_{NS}(t)\|_{\dot H^{-1}}^2dt
}{
\nu^2
\int_I
\|S(t)\|_{\dot H^1}^2dt
}
}
$$

在 denominator非零時。

---

# 21. Scaling audit

N–S scaling：

$$
S_\lambda
=
\lambda^2S(\lambda x,\lambda^2t).
$$

equation-level perturbation：

$$
(\mathcal P_{NS})_\lambda
=
\lambda^4
\mathcal P_{NS}(\lambda x,\lambda^2t).
$$

因此：

$$
\|\mathcal P_\lambda\|_{\dot H^{-1}}
=
\lambda^{3/2}
\|\mathcal P\|_{\dot H^{-1}},
$$

所以：

$$
\int
\|\mathcal P_\lambda\|_{\dot H^{-1}}^2dt
=
\lambda
\int
\|\mathcal P\|_{\dot H^{-1}}^2dt.
$$

同時：

$$
\int
\|S_\lambda\|_{\dot H^1}^2dt
=
\lambda
\int
\|S\|_{\dot H^1}^2dt.
$$

故：

$$
\boxed{
\mathfrak P_I
}
$$

scale invariant。

---

# 22. 注意：$\mathfrak P_I$ 只是 candidate diagnostic

目前未證：

$$
\mathfrak P_I<\varepsilon
\Rightarrow
\text{SSA approximation theorem},
$$

也未證：

$$
\mathfrak P_I\gg1
\Rightarrow
\text{regularity}.
$$

它的作用是避免：

$$
\boxed{
\text{zero energy pairing}
}
$$

被偷換成：

$$
\boxed{
\text{small operator}.
}
$$

---

# 23. Balance–Dynamics plane

真正 local state至少需要：

$$
\boxed{
(\rho_I,\mathfrak P_I).
}
$$

可區分：

## BD-1 — Balance-SSA / Operator-small

$$
|\rho_I|\ll1,
\qquad
\mathfrak P_I\ll1.
$$

這才是值得測試的 model-like candidate regime。

## BD-2 — Balance-SSA / Operator-large

$$
|\rho_I|\ll1,
\qquad
\mathfrak P_I\gtrsim1.
$$

energy balance看似 SSA，

但 hidden orthogonal dynamics很大。

## BD-3 — Cancellation corridor

$$
\rho_I\to-1^+.
$$

gross SSA與 boundary current大幅 cancellation。

## BD-4 — Boundary driven

$$
\rho_I\gg1
$$

或：

$$
A_I\le0,\quad B_I>0.
$$

---

# 24. Miller 2024/2026 對 operator-large regime 的警告

Miller 的 strain–vorticity interaction工作證：

$$
\boxed{
\langle-\Delta S,\omega\otimes\omega\rangle=0,
}
$$

並對 isolating reverse strain–vorticity interaction的 model equation建立 global regularity。

該工作也給出 regularity criteria，用來分析 advection何時 depletion nonlinearity。

所以：

$$
\boxed{
\text{large omitted/operator terms不必然是 blow-up driver；
它們可能是 depletion mechanism}.
}
$$

因此：

$$
\mathfrak P_I
$$

也必須再拆 type，而不能只看 magnitude。

---

# 25. Adjoint cutoff 的 X-Integration 意義

原 moving cutoff有：

- gauge；
- advection；
- diffusion；
- Betchov；
- pressure。

adjoint cutoff將前三者吸收到 cutoff evolution。

所以：

$$
\boxed{
B_\chi
=
\int\nabla\chi\cdot
\left(
\frac13F_B+F_p
\right)
}
$$

是更乾淨的 correction current。

新增：

$$
\boxed{
G_{\rm ADJ}
}
$$

bulk/boundary ratio應優先使用 adjoint cutoff，或明確扣除非-adjoint gauge terms。

---

# 26. Gauge-clean 不等於 boundary-small

即使：

$$
\partial_t\chi
+
u\cdot\nabla\chi
+
\nu\Delta\chi=0,
$$

仍可能：

$$
|B_\chi|
$$

很大。

尤其：

$$
F_p
$$

含 nonlocal pressure Hessian。

所以：

$$
\boxed{
\text{gauge-clean}
\neq
\text{boundary-small}.
}
$$

---

# 27. Pressure/Betchov correction split

定義：

$$
B_I
=
B_I^B+B_I^p,
$$

其中：

$$
B_I^B
=
\frac13
\int_I
\int
\nabla\chi\cdot F_B,
$$

$$
B_I^p
=
\int_I
\int
\nabla\chi\cdot F_p.
$$

若：

$$
|B_I|
$$

很大，

至少：

$$
|B_I^B|
\ge
\frac12|B_I|
$$

或：

$$
|B_I^p|
\ge
\frac12|B_I|.
$$

因此 boundary-dominated branch再分：

$$
\boxed{
\text{Betchov-current dominated}
\quad\vee\quad
\text{pressure-current dominated}.
}
$$

---

# 28. Cancellation corridor 的 component debt

若：

$$
\rho_I\to-1^+
$$

且：

$$
A_I>0,
$$

則：

$$
B_I\sim-A_I.
$$

所以至少一個：

$$
B_I^B,
\quad
B_I^p
$$

必須具有：

$$
O(A_I)
$$

magnitude。

near-perfect depletion不能靠所有 correction components都小完成。

---

# 29. Ratio route的最終裁決

### $\rho<-1$

positive growth不可能。

### $\rho\to-1^+$

survives，但付 cancellation-precision debt。

### $\rho\to0$

survives，且不能解讀為 dynamical SSA closeness。

### $\rho\to+\infty$

survives，boundary/pressure current成主要 carrier。

所以：

$$
\boxed{
\rho
}
$$

只能作：

$$
\boxed{
\text{local strain-energy growth carrier classifier}.
}
$$

不能作 standalone regularity parameter。

---

# 30. Balance Fixed Point / Dynamics Fixed Point Separation

即使：

$$
\rho_n\to0
$$

而：

$$
\frac{
\Delta E_n+D_n
}{
A_n
}
\to1,
$$

只代表：

$$
\boxed{
\text{strain-energy balance becomes SSA-like}.
}
$$

不代表：

$$
\boxed{
S_n
\text{ approaches an SSA-model solution}.
}
$$

本文稱：

$$
\boxed{
\textbf{Balance Fixed Point / Dynamics Fixed Point Separation}.
}
$$

這對 True ETN 非常重要：

relation-level balance convergence不能自動提升成 operator-level dynamical convergence。

---

# 31. True ETN 更新

local strain state應分兩層。

## Balance layer

$$
\boxed{
\Theta^{bal}
=
(E,D,A,B,\rho,\kappa).
}
$$

## Operator layer

$$
\boxed{
\Theta^{op}
=
\left(
\mathcal N_{SSA},
\mathcal P_{NS},
\mathfrak P,
\operatorname{Prov}
\right),
}
$$

其中：

$$
\mathcal N_{SSA}
=
\frac23P_{st}(S^2).
$$

因此：

$$
\boxed{
\Theta^{bal}\text{ convergence}
\not\Rightarrow
\Theta^{op}\text{ convergence}.
}
$$

---

# 32. X-Integration hard guards

## G-ADJ

ratio使用 adjoint cutoff或完整 gauge subtraction。

## G-GROW

ratio只在：

$$
\Delta E>0
$$

growth windows中作 growth-carrier判斷。

## G-RATIO

若：

$$
A>0,
$$

positive growth要求：

$$
\rho>-1.
$$

## G-CANCEL

若：

$$
\rho\to-1,
$$

必須保存 gross：

$$
A,\ B
$$

不能只保存 residual：

$$
A+B.
$$

## G-OP

$$
B/A\to0
$$

不得推出：

$$
\mathcal P_{NS}\to0.
$$

## G-PROJ

global：

$$
\langle\mathcal P_{NS},S\rangle=0
$$

只是 orthogonality，不是 smallness。

## G-PRESS

pressure與 Betchov correction必須分開保存。

---

# 33. 新 frontier：C3-P

C3-O 已回答：

> bulk/boundary ratio本身能不能成為 rigidity theorem？

答案：

$$
\boxed{
\textbf{不能。}
}
$$

missing information是：

$$
\boxed{
\text{orthogonal perturbation operator本身的 dynamical effect}.
}
$$

正式下一題：

$$
\boxed{
\textbf{C3-P — Operator-Level Depletion and Pressure/Betchov Current Rigidity}.
}
$$

---

# 34. C3-P proof obligations

## P1 — Local operator defect

為：

$$
\mathcal P_{NS}
=
P_{st}
\left(
(u\cdot\nabla)S
+
\frac13S^2
+
\frac14\omega\otimes\omega
\right)
$$

建立 ancestry-localized scale-critical norm。

## P2 — Small-operator regime

若：

$$
\mathfrak P_n\to0,
$$

能否 rigorously證 rescaled ancestry dynamics接近 SSA model？

需要 stability theorem，不是 balance identity。

## P3 — Large-operator depletion split

把：

$$
\mathcal P_{NS}
$$

拆成：

- advection；
- residual strain self-interaction；
- vorticity-to-strain coupling。

## P4 — Pressure current near/far split

對：

$$
F_p
=
(\nabla^2p-\Delta pI)u
$$

用 pressure Poisson equation做 core/far source decomposition。

## P5 — Betchov-current helical split

將：

$$
F_B
$$

分解到 local homochiral / heterochiral / nonlocal remainder。

## P6 — Cancellation corridor operator test

若：

$$
\rho_n\to-1^+,
$$

判定：

$$
\mathfrak P_n
$$

是否也必大。

## P7 — Balance/operator phase diagram

建立：

$$
(\rho_n,\mathfrak P_n)
$$

各 branch的 possible / known-regular / model-like-dangerous / open 區域。

## P8 — Adjoint cutoff propagation

分析 terminal ancestry cutoff向 earlier times的 radius、tails與 pressure sensitivity。

---

# 35. 正式狀態

$$
\boxed{
\begin{aligned}
\text{adjoint cutoff cancellation}
&:\ \mathrm{PROVED},\\
\text{gauge-clean strain balance}
&:\ \mathrm{PROVED},\\
\text{growth-carrier dichotomy}
&:\ \mathrm{PROVED},\\
\rho>-1\text{ necessary for }A>0\text{ growth}
&:\ \mathrm{PROVED},\\
\rho\le-1\text{ growth sector}
&:\ \mathrm{EXCLUDED},\\
\text{cancellation-precision debt}
&:\ \mathrm{PROVED},\\
\rho\to0\Rightarrow\text{SSA dynamical closeness}
&:\ \mathrm{FALSE/NO\mbox{-}GO},\\
\langle\mathcal P_{NS},S\rangle=0
&:\ \mathrm{EXTERNAL/STANDARD},\\
\text{SSA model finite-time blowup}
&:\ \mathrm{EXTERNAL\ THEOREM},\\
\text{conditional full-NS blowup under perturbative condition}
&:\ \mathrm{EXTERNAL\ THEOREM},\\
\mathfrak P_I\text{ scale invariance}
&:\ \mathrm{PROVED},\\
\mathfrak P_I\text{ as stability criterion}
&:\ \mathrm{OPEN},\\
\text{balance/operator rigidity}
&:\ \mathrm{OPEN}.
\end{aligned}
}
$$

---

# 36. 結論

C3-N 把 local strain dynamics寫成：

$$
\text{bulk SSA}
+
\text{boundary/gauge package}.
$$

C3-O 使用 adjoint cutoff把 gauge/advection/diffusion cutoff terms exact消掉：

$$
\boxed{
E_\chi'
+
D_\chi
=
A_\chi+B_\chi.
}
$$

對 positive strain-growth window：

若：

$$
A>0,
$$

必須：

$$
\boxed{
\rho=\frac BA>-1.
}
$$

因此：

$$
\boxed{
\rho\le-1
}
$$

是真正 hard depletion sector。

但：

$$
\rho\to-1^+,
\qquad
\rho\to0,
\qquad
\rho\to+\infty
$$

全部仍存活。

更重要的是：

$$
\boxed{
\text{SSA-like balance}
\not\Rightarrow
\text{SSA-like dynamics}.
}
$$

full N–S 被 SSA model丟掉的 perturbation對 global strain energy恰好正交，

所以它可以對當下 enstrophy derivative「看起來是零」，

卻仍對未來 dynamics具有 order-one作用。

因此 scalar ratio route已經走到極限。

下一輪必須升級到：

$$
\boxed{
\textbf{C3-P — Operator-Level Depletion and Pressure/Betchov Current Rigidity}.
}
$$

---

# References

1. E. Miller, *Finite-time blowup for a Navier–Stokes model equation for the self-amplification of strain*, Analysis & PDE 16 (2023), 997–1032; arXiv:1910.05415.
2. E. Miller, *On the interaction of strain and vorticity for solutions of the Navier–Stokes equation*, Pure and Applied Analysis 8 (2026), 247–270; arXiv:2407.02691.
3. M. Carbone, M. Wilczek, *Only two Betchov homogeneity constraints exist for isotropic turbulence*, Journal of Fluid Mechanics 948 (2022), R2; arXiv:2112.12820.
4. E. Miller, *A regularity criterion for the Navier–Stokes equation involving only the middle eigenvalue of the strain tensor*, Arch. Rational Mech. Anal. 235 (2020).
5. R. Betchov, *An inequality concerning the production of vorticity in isotropic turbulence*, Journal of Fluid Mechanics 1 (1956), 497–504.

# Internal dependencies

- `NS_C3M_VorticityStrain_Betchov_GeometryDebt_v0.1.md`
- `NS_C3N_LocalizedBetchov_StrainBoundaryBalance_v0.1.md`
- `NS_C3K_AbsoluteOccupancy_OneMomentGap_v0.1.md`
- `NS_C3L_CriticalMomentEscape_StrainGeometryDebt_v0.1.md`
- `NS_C3J_GaugeCorrected_Reentry_Hysteresis_NoGo_v0.1.md`
- `True ETN / 無限維張力場`
- `X_Integral_Unified_Program_v0.2.md`

Next:

$$
\boxed{
\textbf{C3-P — Operator-Level Depletion and Pressure/Betchov Current Rigidity}
}
$$
