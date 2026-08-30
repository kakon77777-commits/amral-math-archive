---
title: "Navier–Stokes C3-N：Localized Betchov Boundary Current 與 Strain Self-Amplification 局部平衡"
subtitle: "Localized Betchov Currents, Boundary Compensation, and the Exact Local Strain Self-Amplification Balance"
version: "v0.1"
date: "2026-08-14"
author: "Neo.K / EveMissLab"
language: "zh-TW"
status: "Theorem-style structural reduction / no-go note"
epistemic_status: "Contains exact kinematic divergence identities and localized strain-energy balance. Uses external primary literature for Betchov divergence structure and strain dynamics. Does NOT prove Navier–Stokes regularity."
---

# Navier–Stokes C3-N
# Localized Betchov Boundary Current 與 Strain Self-Amplification 局部平衡

## 0. 本輪定位

C3-M 已得到：

1. pointwise vortex stretching：

$$
\alpha
=
\xi\cdot S\xi
=
\lambda_2
+
(\lambda_3-\lambda_2)c_3
-
(\lambda_2-\lambda_1)c_1;
$$

2. global Betchov relation：

$$
\int
\omega\cdot S\omega\,dx
=
-4
\int
\det S\,dx;
$$

3. 因此 global integration會把 vorticity–strain orientation information坍縮掉；

4. 真正值得研究的是 localized quantity：

$$
\int
\chi
\left(
\omega\cdot S\omega
+
4\det S
\right)dx.
$$

上一輪仍只知道：

> local surplus必須在 core外被 global compensation。

本輪把這件事正式閉合：

$$
\boxed{
\text{localized Betchov mismatch本身就是一個 exact spatial divergence current}.
}
$$

因此它不只是「某處補回來」，

而是：

$$
\boxed{
\text{必須穿過 localization boundary}.
}
$$

更進一步，full strain equation localized後可以精確寫成：

$$
\boxed{
\text{bulk strain self-amplification}
+
\text{boundary/gauge corrections}.
}
$$

這把 C3-M 的 geometry debt第一次轉成真正的 local balance law。

---

# 1. 設定

考慮 smooth divergence-free velocity：

$$
u:\mathbb R^3\times[0,T)\to\mathbb R^3,
$$

$$
\nabla\cdot u=0.
$$

定義 velocity gradient：

$$
\boxed{
A_{ij}
=
\partial_j u_i.
}
$$

分解：

$$
A=S+\Omega,
$$

其中：

$$
S
=
\frac12(A+A^\top),
$$

$$
\Omega
=
\frac12(A-A^\top).
$$

vorticity：

$$
\omega=\nabla\times u.
$$

因 incompressibility：

$$
\operatorname{tr}A
=
\operatorname{tr}S
=
0.
$$

---

# 2. Pointwise algebra：$A^3$ 與 Betchov density

antisymmetric part滿足：

$$
\Omega^2
=
\frac14
\left(
\omega\otimes\omega
-
|\omega|^2I
\right).
$$

所以：

$$
\operatorname{tr}(S\Omega^2)
=
\frac14
\omega\cdot S\omega
$$

因：

$$
\operatorname{tr}S=0.
$$

展開：

$$
\operatorname{tr}(A^3)
=
\operatorname{tr}(S^3)
+
3\operatorname{tr}(S\Omega^2).
$$

對 trace-free $3\times3$ symmetric matrix：

$$
\operatorname{tr}(S^3)
=
3\det S.
$$

故：

$$
\boxed{
\operatorname{tr}(A^3)
=
3\det S
+
\frac34
\omega\cdot S\omega.
}
$$

因此：

$$
\boxed{
\omega\cdot S\omega
+
4\det S
=
\frac43
\operatorname{tr}(A^3).
}
$$

定義：

$$
\boxed{
b_B
=
\omega\cdot S\omega
+
4\det S.
}
$$

---

# 3. External kinematic input：$\operatorname{tr}(A^3)$ 是 divergence

Carbone–Wilczek 對 Betchov constraints的分析明確寫出：

$$
\boxed{
\operatorname{tr}(A^3)
=
\nabla\cdot F_B,
}
$$

其中：

$$
\boxed{
F_B
=
\left(
A^2
-
\frac12
\operatorname{tr}(A^2)I
\right)u.
}
$$

component form：

$$
\boxed{
(F_B)_i
=
u_k
\partial_j u_i
\partial_k u_j
-
\frac12
u_i
\partial_k u_j
\partial_j u_k.
}
$$

因此：

$$
\boxed{
b_B
=
\frac43
\nabla\cdot F_B.
}
$$

這是一個 pointwise kinematic identity。

不使用 Navier–Stokes time evolution。

---

# 4. C3-N.1：Localized Betchov Boundary Theorem

## 定理 4.1

令：

$$
\chi\in C_c^\infty(\mathbb R^3).
$$

則：

$$
\boxed{
\int_{\mathbb R^3}
\chi
\left(
\omega\cdot S\omega
+
4\det S
\right)dx
=
-\frac43
\int_{\mathbb R^3}
\nabla\chi\cdot F_B\,dx.
}
$$

### 證明

由：

$$
b_B
=
\frac43\nabla\cdot F_B,
$$

integration by parts即得。$\square$

---

# 5. Sharp-domain form

若：

$$
\Omega\subset\mathbb R^3
$$

為 smooth bounded domain，

則 divergence theorem給：

$$
\boxed{
\int_{\Omega}
\left(
\omega\cdot S\omega
+
4\det S
\right)dx
=
\frac43
\int_{\partial\Omega}
F_B\cdot n\,dS.
}
$$

特別對 ball：

$$
B_R(x_0),
$$

$$
\boxed{
\int_{B_R(x_0)}
\left(
\omega\cdot S\omega
+
4\det S
\right)dx
=
\frac43
\int_{\partial B_R(x_0)}
F_B\cdot n\,dS.
}
$$

所以：

$$
\boxed{
\text{local Betchov mismatch = spatial boundary current}.
}
$$

---

# 6. 這真正閉合了什麼？

C3-M 定義：

$$
b_B
=
\omega\cdot S\omega
+
4\det S.
$$

global：

$$
\int b_B=0.
$$

此前只知道：

$$
\int\chi b_B
=
-
\int(1-\chi)b_B.
$$

本輪更強：

$$
\boxed{
\int\chi b_B
}
$$

不需要知道 entire exterior volume。

它由：

$$
\boxed{
\nabla\chi\cdot F_B
}
$$

在 cutoff transition layer直接決定。

所以：

$$
\boxed{
\text{Betchov compensation是 boundary-mediated，而非任意 far-volume bookkeeping}.
}
$$

---

# 7. Boundary-current magnitude

由：

$$
F_B
=
\left(
A^2
-
\frac12\operatorname{tr}(A^2)I
\right)u,
$$

有：

$$
\boxed{
|F_B|
\le
C
|u|
|\nabla u|^2.
}
$$

所以：

## 推論 7.1

$$
\boxed{
\left|
\int
\chi b_B
\right|
\le
C
\|\nabla\chi\|_\infty
\int_{\operatorname{supp}\nabla\chi}
|u|
|\nabla u|^2dx.
}
$$

---

# 8. Ball-scale estimate

取：

$$
\chi_R(x)
=
\chi_0
\left(
\frac{x-x_0}{R}
\right),
$$

其中：

$$
\chi_0=1
$$

於 $B_1$，

支撐於：

$$
B_2.
$$

則：

$$
|\nabla\chi_R|
\lesssim
R^{-1}.
$$

令 transition annulus：

$$
\mathcal A_R
=
B_{2R}(x_0)\setminus B_R(x_0).
$$

則：

$$
\boxed{
\left|
\int
\chi_Rb_B
\right|
\le
\frac{C}{R}
\int_{\mathcal A_R}
|u|
|\nabla u|^2dx.
}
$$

---

# 9. Dimensionless boundary compensation

定義 annular critical velocity amplitude：

$$
\boxed{
a_R
=
\frac{
R
\|u\|_{L^\infty(\mathcal A_R)}
}{
\nu
}.
}
$$

定義 normalized annular gradient stock：

$$
\boxed{
d_R
=
\frac{
R
}{
\nu^2
}
\int_{\mathcal A_R}
|\nabla u|^2dx.
}
$$

定義 normalized localized Betchov defect：

$$
\boxed{
\widehat{\mathfrak B}_R
=
\frac{
R^3
}{
\nu^3
}
\left|
\int
\chi_Rb_Bdx
\right|.
}
$$

則：

## 定理 9.1

$$
\boxed{
\widehat{\mathfrak B}_R
\le
C
a_R
d_R.
}
$$

所以 local Betchov mismatch需要 boundary layer同時具有：

- critical velocity amplitude；
- gradient stock。

---

# 10. Companion：second Betchov invariant

同樣：

$$
\operatorname{tr}(A^2)
=
|S|^2
-
\frac12|\omega|^2.
$$

而：

$$
\boxed{
\operatorname{tr}(A^2)
=
\nabla\cdot(Au).
}
$$

因：

$$
(Au)_i
=
u_j\partial_j u_i.
$$

所以：

## 定理 10.1

$$
\boxed{
\int
\chi
\left(
|S|^2
-
\frac12|\omega|^2
\right)dx
=
-
\int
\nabla\chi\cdot(Au)\,dx.
}
$$

因此 local strain/enstrophy magnitude mismatch同樣是 boundary current。

---

# 11. Localized Betchov pair

我們現在有兩個 exact local identities：

$$
\boxed{
\int\chi
\left(
|S|^2
-
\frac12|\omega|^2
\right)
=
-\int\nabla\chi\cdot Au,
}
$$

以及：

$$
\boxed{
\int\chi
\left(
\omega\cdot S\omega
+
4\det S
\right)
=
-\frac43
\int\nabla\chi\cdot F_B.
}
$$

所以：

$$
\boxed{
\text{magnitude balance}
+
\text{production balance}
}
$$

兩者的 global identities都可理解成 boundary current在 whole-space limit消失。

---

# 12. External numerical interface

Encinar 2023 對 homogeneous isotropic turbulence的 DNS / filtered velocity-gradient analysis發現：

- Betchov 的 strain/vorticity magnitude balance；
- vortex-stretching / strain-self-amplification production balance；

在 local coarse-graining後通常於數個 filter widths的 physical distance內達到主要 cancellation；

其報告的 characteristic Betchov scale約為：

$$
O(3)
$$

個 filtered structure widths。

本文不把此數值結果當 arbitrary Navier–Stokes theorem。

但定理 4.1提供其 exact kinematic interpretation：

$$
\boxed{
\text{local mismatch只能透過 localization boundary current存在}.
}
$$

---

# 13. Strain equation

full 3D N–S strain equation：

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

因：

$$
\operatorname{tr}S=0,
$$

$I$ term與 $S$ pairing為零。

---

# 14. Nonlinear strain pairing

有：

$$
S:S^2
=
\operatorname{tr}(S^3)
=
3\det S.
$$

以及：

$$
S:
\left(
\frac14\omega\otimes\omega
\right)
=
\frac14
\omega\cdot S\omega.
$$

所以：

$$
\boxed{
3\det S
+
\frac14\omega\cdot S\omega
=
2\det S
+
\frac14b_B.
}
$$

---

# 15. Pressure Hessian也是 divergence current

定義：

$$
\boxed{
F_p
=
\left(
\nabla^2p
-
\Delta p\,I
\right)u.
}
$$

則：

## 引理 15.1

$$
\boxed{
\nabla\cdot F_p
=
S:\nabla^2p.
}
$$

### 證明

因：

$$
\nabla\cdot
\left(
\nabla^2p-\Delta p\,I
\right)
=
0,
$$

所以：

$$
\nabla\cdot F_p
=
\left(
\nabla^2p-\Delta pI
\right):\nabla u.
$$

Hessian為 symmetric，

故：

$$
\nabla^2p:\nabla u
=
\nabla^2p:S.
$$

而：

$$
\Delta p\,\operatorname{tr}\nabla u
=
0.
$$

$\square$

---

# 16. Moving cutoff

令：

$$
\chi=\chi(t,x)
$$

smooth compactly supported。

定義 local strain energy：

$$
\boxed{
E_S^\chi(t)
=
\frac12
\int
\chi(t,x)
|S(x,t)|^2dx.
}
$$

---

# 17. C3-N.2：Exact Local Strain Self-Amplification Balance

## 定理 17.1

對 smooth N–S solution：

$$
\boxed{
\frac d{dt}
E_S^\chi
+
\nu
\int
\chi
|\nabla S|^2dx
=
-2
\int
\chi
\det S\,dx
+
\mathcal C_\chi,
}
$$

其中：

$$
\boxed{
\begin{aligned}
\mathcal C_\chi
={}&
\frac12
\int
|S|^2
\left(
\partial_t\chi
+
u\cdot\nabla\chi
+
\nu\Delta\chi
\right)dx
\\
&+
\frac13
\int
\nabla\chi\cdot F_B\,dx
\\
&+
\int
\nabla\chi\cdot F_p\,dx.
\end{aligned}
}
$$

### 證明

將 strain equation與：

$$
\chi S
$$

作 $L^2$ pairing。

---

## Time derivative

$$
\int
\chi S:\partial_tS
=
\frac12
\frac d{dt}
\int
\chi|S|^2
-
\frac12
\int
(\partial_t\chi)|S|^2.
$$

---

## Viscosity

$$
-\nu
\int
\chi S:\Delta S
=
\nu
\int
\chi|\nabla S|^2
-
\frac\nu2
\int
(\Delta\chi)|S|^2.
$$

---

## Advection

因：

$$
\nabla\cdot u=0,
$$

$$
\int
\chi
S:(u\cdot\nabla S)
=
-\frac12
\int
|S|^2
u\cdot\nabla\chi.
$$

---

## Cubic nonlinear terms

$$
\int
\chi
\left[
3\det S
+
\frac14\omega\cdot S\omega
\right]
=
2
\int
\chi\det S
+
\frac14
\int
\chi b_B.
$$

而：

$$
\frac14
\int\chi b_B
=
-\frac13
\int\nabla\chi\cdot F_B.
$$

---

## Pressure

$$
\int
\chi
S:\nabla^2p
=
-
\int
\nabla\chi\cdot F_p.
$$

整理即得。$\square$

---

# 18. 這個 identity 的核心含義

在 local strain $L^2$ balance中：

$$
\boxed{
-2\int\chi\det S
}
$$

是唯一保留於 **bulk volume** 的 cubic production項。

其他：

- vorticity interaction和 self-amplification的 Betchov mismatch；
- advection；
- pressure Hessian；
- cutoff motion；
- viscous localization correction；

全部進入：

$$
\boxed{
\mathcal C_\chi
}
$$

這個 boundary/gauge correction package。

所以：

$$
\boxed{
\textbf{Local Strain Growth}
=
\textbf{Bulk Self-Amplification}
+
\textbf{Boundary/Transport Compensation}.
}
$$

---

# 19. Whole-space limit

形式取：

$$
\chi\to1
$$

且 fields sufficiently decay，

則：

$$
\nabla\chi,
\quad
\Delta\chi,
\quad
\partial_t\chi
\to0.
$$

所以：

$$
\mathcal C_\chi\to0.
$$

recover：

$$
\boxed{
\frac12
\frac d{dt}
\|S\|_2^2
+
\nu
\|\nabla S\|_2^2
=
-2
\int
\det S.
}
$$

等價：

$$
\boxed{
\frac d{dt}
\|S\|_2^2
=
-2\nu
\|\nabla S\|_2^2
-
4
\int\det S.
}
$$

這是標準 global strain-enstrophy identity。

---

# 20. 與 Miller strain decomposition 的關係

Miller 將 full strain equation寫成：

$$
\partial_tS
-
\nu\Delta S
+
\frac23P_{st}(S^2)
+
P_{st}
\left(
(u\cdot\nabla)S
+
\frac13S^2
+
\frac14\omega\otimes\omega
\right)
=
0.
$$

global $L^2$ pairing中，第二個 projected nonlinear package與 $S$ orthogonal。

strain self-amplification model：

$$
\partial_tS
-
\nu\Delta S
+
\frac23P_{st}(S^2)
=
0
$$

保留和 full N–S 相同的 global strain-enstrophy growth identity，

而此 model對一族 initial data可 finite-time blow up。

本輪定理 17.1補充：

$$
\boxed{
\text{global orthogonality在 localization 後轉化成 boundary/gauge current}.
}
$$

這不是說 local full N–S等於 self-amplification model。

boundary package：

$$
\mathcal C_\chi
$$

可以和 bulk term同階，甚至主導。

---

# 21. Local production dichotomy

定義：

$$
\boxed{
\mathcal A_\chi
=
-2
\int
\chi\det S\,dx
}
$$

為 local bulk self-amplification。

則：

$$
\boxed{
\frac d{dt}
E_S^\chi
+
\nu
\int\chi|\nabla S|^2
=
\mathcal A_\chi
+
\mathcal C_\chi.
}
$$

因此如果某 ancestry core中 local strain growth很大，

至少必須：

$$
\boxed{
|\mathcal A_\chi|
\text{ large}
}
$$

或：

$$
\boxed{
|\mathcal C_\chi|
\text{ large}.
}
$$

這只是 exact dichotomy，

不是 regularity theorem。

---

# 22. Boundary package 的各型態

$$
\mathcal C_\chi
$$

至少包含：

## C-GAUGE

$$
\frac12
\int
|S|^2\partial_t\chi.
$$

moving core reclassification。

## C-ADV

$$
\frac12
\int
|S|^2u\cdot\nabla\chi.
$$

physical advection through boundary。

## C-DIFF

$$
\frac\nu2
\int
|S|^2\Delta\chi.
$$

viscous boundary correction。

## C-BETCHOV

$$
\frac13
\int
\nabla\chi\cdot F_B.
$$

vortex-stretching / strain-self-amplification local mismatch current。

## C-PRESS

$$
\int
\nabla\chi\cdot F_p.
$$

pressure-Hessian boundary current。

---

# 23. Ball-scale correction bound

對 fixed：

$$
\chi_R,
$$

可得 schematic：

$$
\boxed{
\begin{aligned}
|\mathcal C_{\chi_R}|
\lesssim{}&
\frac{\nu}{R^2}
\int_{\mathcal A_R}
|S|^2
\\
&+
\frac1R
\int_{\mathcal A_R}
|u||S|^2
\\
&+
\frac1R
\int_{\mathcal A_R}
|u||\nabla u|^2
\\
&+
\frac1R
\int_{\mathcal A_R}
|u|
\left(
|\nabla^2p|
+
|\Delta p|
\right).
\end{aligned}
}
$$

若 cutoff moving，

另加：

$$
\boxed{
\|\partial_t\chi_R\|_\infty
\int_{\mathcal A_R}
|S|^2.
}
$$

---

# 24. Pressure caveat

雖然：

$$
S:\nabla^2p
$$

已被寫成 boundary divergence，

$$
F_p
$$

仍包含：

$$
\nabla^2p.
$$

而 pressure Hessian 是 nonlocal quantity。

所以：

$$
\boxed{
\text{pressure bulk term消失}
\not\Rightarrow
\text{pressure influence變成 local}.
}
$$

它只是被精確搬到 boundary current。

這是 X-Integration 的 provenance-preserving transformation，

不是 physical locality theorem。

---

# 25. Scaling audit

N–S scaling：

$$
u_\lambda(x,t)
=
\lambda u(\lambda x,\lambda^2t).
$$

則：

$$
S_\lambda
=
\lambda^2S(\lambda x,\lambda^2t),
$$

$$
\omega_\lambda
=
\lambda^2\omega(\lambda x,\lambda^2t).
$$

所以：

$$
b_{B,\lambda}
=
\lambda^6
b_B(\lambda x,\lambda^2t).
$$

對 core radius：

$$
R_\lambda=\lambda^{-1}R,
$$

有：

$$
\boxed{
\int
\chi_{R_\lambda}
b_{B,\lambda}
dx
=
\lambda^3
\int
\chi_Rb_Bdx.
}
$$

---

# 26. C3-N.3：Boundary Compensation is Same-Scale as Bulk Self-Amplification

同樣：

$$
\int
\chi_{R_\lambda}
\det S_\lambda\,dx
=
\lambda^3
\int
\chi_R\det S\,dx.
$$

因此：

$$
\boxed{
\text{localized Betchov boundary correction}
}
$$

與：

$$
\boxed{
\text{bulk strain self-amplification}
}
$$

具有完全相同的 instantaneous scaling：

$$
\lambda^3.
$$

所以：

## No-Go 26.1

$$
\boxed{
R\to0
\text{ 並不因 scaling 本身使 boundary Betchov correction perturbatively small}.
}
$$

---

# 27. Viscous-window scaling

一個 scale：

$$
\lambda
$$

的 viscous time：

$$
\tau_\lambda
\sim
(\nu\lambda^2)^{-1}.
$$

instantaneous Betchov/self-amplification rate：

$$
\sim
\lambda^3.
$$

所以 over one viscous window：

$$
\boxed{
\text{integrated contribution}
\sim
\lambda
}
$$

under normalized fixed-shape scaling。

因此 boundary compensation位於和 enstrophy growth同一個 supercritical level。

---

# 28. Boundary-current finite-budget no-go

global kinetic energy只控制：

$$
\nu
\int
\|\nabla u\|_2^2dt.
$$

它沒有控制：

$$
\boxed{
\int
\frac1R
\int_{\mathcal A_R}
|u||\nabla u|^2
dxdt
}
$$

uniformly over shrinking：

$$
R.
$$

所以：

$$
\boxed{
\text{exact boundary representation}
\neq
\text{finite boundary budget}.
}
$$

這是本輪最重要的 no-go之一。

---

# 29. Kinematic current ≠ temporal energy flux

$$
F_B
$$

是使：

$$
\nabla\cdot F_B
=
\operatorname{tr}(A^3)
$$

成立的 kinematic spatial current。

它不是：

- kinetic-energy current；
- sign-definite flux；
- conserved temporal charge；
- irreversible expenditure。

因此：

$$
\boxed{
\int_{\partial B_R}F_B\cdot n
}
$$

不能直接當成「每代付一次的有限 cost」。

---

# 30. Local Betchov compensation 与 C3-J gauge audit

C3-J 已指出 moving core會產生：

$$
\partial_t\chi
$$

gauge sweep。

C3-N 表明 Betchov mismatch由：

$$
\nabla\chi\cdot F_B
$$

形成。

兩者是不同 type：

$$
\boxed{
\partial_t\chi
\neq
\nabla\chi\cdot F_B.
}
$$

所以：

- core 自己移動造成的 reclassification；
- local Betchov compensation current；

不得混同。

---

# 31. Spatial compensation真的必須碰 boundary

假設：

$$
\chi_R=1
$$

on：

$$
B_R,
$$

transition only in：

$$
\mathcal A_R.
$$

若：

$$
F_B=0
$$

on：

$$
\mathcal A_R,
$$

則：

$$
\boxed{
\int
\chi_R
\left(
\omega\cdot S\omega+4\det S
\right)
=
0.
}
$$

所以 weighted core內若存在 Betchov mismatch，

boundary layer必須有 nonzero：

$$
F_B.
$$

這是 exact source condition。

---

# 32. 但 boundary current不要求远场 defect直接进入 core

$$
F_B
$$

只依賴 boundary layer上的：

$$
u,\nabla u.
$$

far-space defect可以：

- 透過 pressure / Biot–Savart-like global influence改變 boundary fields；
- 經 earlier dynamics輸送到 boundary；
- 或完全 decouple。

localized identity本身不能區分這些 provenance。

所以仍需 X-certificate保存 boundary fields來源。

---

# 33. Local Betchov current與 phase-space ancestry

對 ancestry core：

$$
R_n
\sim
\lambda_n^{-1},
$$

定義：

$$
\boxed{
\mathfrak J_{B,n}
=
\frac43
\int_{\partial B_{R_n}(x_n)}
F_B\cdot n\,dS.
}
$$

則：

$$
\boxed{
\mathfrak J_{B,n}
=
\int_{B_{R_n}(x_n)}
\left(
\omega\cdot S\omega
+
4\det S
\right)dx.
}
$$

所以每代 core可以附加：

$$
\boxed{
\operatorname{XBetchov}_n
=
\left\langle
\mathfrak J_{B,n},
\mathcal V_n,
\mathcal A_n,
\operatorname{ProvBoundary}_n
\right\rangle.
}
$$

其中：

- $\mathcal V_n$ = core vortex stretching；
- $\mathcal A_n=-4\int\det S$ = strain self-amplification representation；
- $\operatorname{ProvBoundary}$ = current on boundary。

---

# 34. Betchov sign convention

定義：

$$
\mathcal V_\chi
=
\int
\chi
\omega\cdot S\omega,
$$

$$
\mathcal A_\chi
=
-4
\int
\chi
\det S.
$$

則：

$$
b_B
=
\omega\cdot S\omega
-
(-4\det S).
$$

所以：

$$
\boxed{
\mathcal V_\chi
-
\mathcal A_\chi
=
-\frac43
\int
\nabla\chi\cdot F_B.
}
$$

即：

$$
\boxed{
\text{local VS}
-
\text{local SSA}
=
\text{boundary Betchov current}.
}
$$

whole space：

$$
\boxed{
\mathcal V=\mathcal A.
}
$$

---

# 35. Local VS/SSA imbalance theorem

## 定理 35.1

若：

$$
\mathcal V_\chi
\ge
(1+\delta)
\mathcal A_\chi
$$

且：

$$
\mathcal A_\chi>0,
$$

則：

$$
\boxed{
\left|
\int
\nabla\chi\cdot F_B
\right|
\ge
\frac34
\delta
\mathcal A_\chi.
}
$$

同樣若 SSA明顯大於 VS，

boundary current magnitude也必 comparable。

所以 local production mechanisms只有在 boundary current夠大時才能顯著失衡。

---

# 36. Encinar 2023 的位置

Encinar 的 DNS結果顯示：

filtered VS / SSA mismatch通常在少數 filter widths內被 spatial averaging大幅取消。

本輪 theorem不給：

$$
3\times\text{filter width}
$$

這個 numerical constant。

它只證：

$$
\boxed{
\text{任何 cancellation length都必須透過 Betchov boundary current形成}.
}
$$

所以：

- exact theorem = divergence/boundary identity；
- numerical evidence = characteristic local cancellation radius。

兩者嚴格分開。

---

# 37. Miller self-amplification warning

Miller 的 strain self-amplification model保留：

$$
-2\int\det S
$$

bulk growth mechanism，

並對一族 data finite-time blow up。

所以：

$$
\boxed{
\text{boundary correction small}
}
$$

不能自動被解讀成「好事」。

反而：

如果 local full N–S dynamics在某 sense過度接近 pure self-amplification model，

可能更接近 dangerous strain-growth route。

但：

$$
\boxed{
\text{small local }\mathcal C_\chi
\Rightarrow
\text{full N--S blow-up}
}
$$

完全未證。

只可作 structural warning。

---

# 38. Miller 2024/2026 depletion interface

Miller 的 strain-vorticity interaction work證：

$$
\boxed{
\langle-\Delta S,\omega\otimes\omega\rangle=0,
}
$$

並建立 global regular strain-vorticity interaction model。

其 regularity criteria顯示：

full N–S若 blow up，

certain perturbation packages involving：

$$
(u\cdot\nabla)S,
\quad
S^2,
\quad
\omega\otimes\omega
$$

不能相對 dissipative strain scale保持過小。

因此：

$$
\boxed{
\text{advection/depletion corrections不是可隨意刪除的 decoration}.
}
$$

C3-N localized balance提供新的 physical-space interface來追蹤這些 correction如何穿過 ancestry boundary。

---

# 39. C3-N 主 reduction

現在 hypothetical ancestry core若 strain growth進入 singular regime，

至少有：

## Branch N-A — Bulk self-amplification

$$
\boxed{
-2
\int
\chi_n\det S
}
$$

主導。

這接：

- $\lambda_2^+$ divergence；
- two-positive-eigenvalue geometry；
- strain self-amplification model。

## Branch N-B — Boundary/depletion compensation

$$
\boxed{
|\mathcal C_{\chi_n}|
}
$$

與 bulk term同階或更大。

則 singular route必須持續產生：

- advection boundary flux；
- pressure-Hessian boundary current；
- Betchov VS/SSA current；
- diffusion/gauge corrections。

---

# 40. 這是不是 contradiction？

不是。

兩 branch都可能在 N–S scaling下保持 nontrivial。

特別：

$$
\boxed{
\mathcal C_{\chi_n}
}
$$

與：

$$
\boxed{
\int\chi_n\det S
}
$$

在：

$$
R_n\sim\lambda_n^{-1}
$$

下同階。

所以 shrink ancestry core本身不會選出 Branch N-A 或 N-B。

---

# 41. 真正新的 rigidity target

要前進，必須研究 ratio：

$$
\boxed{
\mathfrak D_n
=
\frac{
\mathcal C_{\chi_n}
}{
-2\int\chi_n\det S
}
}
$$

在 bulk denominator非零時。

可能性：

### N-R1 — $\mathfrak D_n\to0$

core逐漸 self-amplification dominated。

### N-R2 — $\mathfrak D_n\to-1$

boundary/depletion近乎完全抵銷 bulk production。

### N-R3 — $\mathfrak D_n$ oscillatory / unbounded

core與 exterior持續交換主導。

不同 branch可能需要完全不同 rigidity theorem。

---

# 42. X-Integration hard guards 更新

## G-B3

保存：

$$
\operatorname{tr}(A^3)
$$

的 exact Betchov current：

$$
F_B.
$$

## G-B2

保存：

$$
\operatorname{tr}(A^2)
$$

的 magnitude current：

$$
Au.
$$

## G-BULK

bulk self-amplification：

$$
-2\int\chi\det S.
$$

## G-BDRY

boundary package：

$$
\mathcal C_\chi.
$$

## G-PRESS

pressure current：

$$
F_p.
$$

不得因其在 boundary integral中就誤稱 local。

## G-FLUXTYPE

Betchov current不是 energy flux。

## G-SCALE

boundary與bulk同 scaling；

禁止以：

$$
R\to0
$$

自動宣布 boundary negligible。

---

# 43. True ETN 更新

ancestry core的 strain tension state可寫：

$$
\boxed{
\Theta_n^{strain}
=
\left\langle
E_{S,n},
D_{S,n},
A_{SSA,n},
J_{B,n},
J_{adv,n},
J_{press,n},
J_{diff,n},
J_{gauge,n}
\right\rangle.
}
$$

exact balance：

$$
\boxed{
\dot E_{S,n}
+
D_{S,n}
=
A_{SSA,n}
+
\sum J_{n}.
}
$$

因此 True ETN 在此不是「幾個力量相加」的比喻。

它直接對應一個 exact typed local balance。

---

# 44. 新 frontier：C3-O

本輪已關閉：

$$
\boxed{
\text{localized Betchov compensation是否真是 boundary term？}
}
$$

答案：

$$
\boxed{
\textbf{YES，exactly}.
}
$$

但也證明：

$$
\boxed{
\text{boundary current與bulk self-amplification同 scaling}.
}
$$

所以新的核心不是「boundary存在嗎？」

而是：

> hypothetical singular ancestry中，boundary/depletion package相對於 bulk strain self-amplification，必須採取什麼 asymptotic ratio？

正式定義：

$$
\boxed{
\textbf{C3-O — Boundary Depletion versus Strain Self-Amplification Rigidity}.
}
$$

---

# 45. C3-O proof obligations

## O1 — Bulk/boundary ratio classification

研究：

$$
\mathfrak D_n
=
\frac{
\mathcal C_{\chi_n}
}{
A_{SSA,n}
}.
$$

抽 subsequence使其：

- convergence；
- sign；
- boundedness；

可分類。

## O2 — Self-amplification-dominated branch

若：

$$
\mathfrak D_n\to0,
$$

比較 rescaled ancestry core與 Miller strain self-amplification model。

需要 full dynamical closeness，

不能只靠一條 energy balance。

## O3 — Depletion-dominated branch

若：

$$
\mathfrak D_n\approx-1,
$$

證：

$$
\boxed{
\text{boundary correction必須持續與 bulk SSA phase-lock}.
}
$$

研究此 persistent cancellation是否與：

- first-crossing timing；
- phase efficiency；
- spatial direction roughness；
- pressure nonlocality；

兼容。

## O4 — Pressure current decomposition

對：

$$
F_p
=
(\nabla^2p-\Delta pI)u
$$

做 near/far pressure decomposition。

判定 ancestry core的 pressure compensation有多少來自：

- local core；
- far defect；
- moving gauge。

## O5 — Betchov current frequency decomposition

對：

$$
F_B
=
(A^2-\tfrac12\operatorname{tr}(A^2)I)u
$$

做 LP/helical decomposition。

研究：

$$
\boxed{
\text{local heterochiral ancestry}
}
$$

在 Betchov boundary current中佔多少。

## O6 — Localized Miller perturbation

嘗試建立：

$$
\boxed{
\text{localized analogue of Miller perturbative criteria}
}
$$

用 boundary/depletion norm衡量 full local dynamics距離：

- strain self-amplification model；
- strain-vorticity interaction model；

的程度。

## O7 — Betchov-current total variation

雖然 current非 sign-definite，

研究 shrinking ancestry boundary上的：

$$
\int
|J_{B,n}|
$$

是否能由 critical moment / strain geometry限制。

## O8 — Experimental audit

用 DNS / synthetic divergence-free fields測：

$$
\mathfrak D_n
$$

與：

- local VS/SSA ratio；
- $\lambda_2^+$；
- helicity pair-production；
- phase efficiency；

的關係。

數值結果嚴格標為 evidence。

---

# 46. 正式狀態

$$
\boxed{
\begin{aligned}
b_B=\frac43\operatorname{tr}(A^3)
&:\ \mathrm{PROVED},\\
\operatorname{tr}(A^3)=\nabla\cdot F_B
&:\ \mathrm{EXTERNAL/STANDARD},\\
\text{localized Betchov boundary theorem}
&:\ \mathrm{PROVED},\\
\text{ball surface-current form}
&:\ \mathrm{PROVED},\\
\text{boundary magnitude bound}
&:\ \mathrm{PROVED},\\
\text{dimensionless compensation bound}
&:\ \mathrm{PROVED},\\
\text{localized second Betchov identity}
&:\ \mathrm{PROVED},\\
S:\nabla^2p=\nabla\cdot F_p
&:\ \mathrm{PROVED},\\
\text{exact local strain self-amplification balance}
&:\ \mathrm{PROVED},\\
\text{unique bulk cubic strain production}
&:\ \mathrm{PROVED/STRUCTURAL},\\
\text{boundary correction becomes small as }R\to0
&:\ \mathrm{FALSE/NO\mbox{-}GO},\\
\text{Betchov current has finite additive budget}
&:\ \mathrm{NOT\ PROVED},\\
\text{Betchov current is an energy flux}
&:\ \mathrm{FALSE/TYPE\ ERROR},\\
\text{bulk/boundary asymptotic rigidity}
&:\ \mathrm{OPEN}.
\end{aligned}
}
$$

---

# 47. 結論

C3-M 發現：

$$
\boxed{
\text{global Betchov identity會坍縮 local orientation}.
}
$$

C3-N 現在把被坍縮的資訊精確找回來：

$$
\boxed{
\omega\cdot S\omega
+
4\det S
=
\frac43\nabla\cdot F_B.
}
$$

因此：

$$
\boxed{
\text{localized VS--SSA mismatch}
=
\text{Betchov boundary current}.
}
$$

它不是任意 far-field compensation。

它必須穿過 localization boundary。

進一步 full strain equation給：

$$
\boxed{
\frac12\frac d{dt}\int\chi|S|^2
+
\nu\int\chi|\nabla S|^2
=
-2\int\chi\det S
+
\mathcal C_\chi.
}
$$

所以 local strain balance真正變成：

$$
\boxed{
\textbf{bulk strain self-amplification}
+
\textbf{boundary/depletion package}.
}
$$

而所有：

- vorticity mismatch；
- advection；
- pressure Hessian；
- localization diffusion；
- moving-core gauge；

都被明確保存於：

$$
\mathcal C_\chi.
$$

但這仍不是 regularity proof。

因：

$$
\boxed{
\mathcal C_\chi
}
$$

和：

$$
\boxed{
-2\int\chi\det S
}
$$

在 parabolic shrinking core上具有相同 scaling。

所以真正的新 frontier是：

$$
\boxed{
\textbf{bulk SSA}
\quad\text{vs}\quad
\textbf{persistent boundary depletion}.
}
$$

下一輪：

$$
\boxed{
\textbf{C3-O — Boundary Depletion versus Strain Self-Amplification Rigidity}.
}
$$

---

# References

1. M. Carbone, M. Wilczek, *Only two Betchov homogeneity constraints exist for isotropic turbulence*, Journal of Fluid Mechanics 948 (2022), R2; arXiv:2112.12820.
2. R. Betchov, *An inequality concerning the production of vorticity in isotropic turbulence*, Journal of Fluid Mechanics 1 (1956), 497–504.
3. E. Miller, *Finite-time blowup for a Navier–Stokes model equation for the self-amplification of strain*, arXiv:1910.05415.
4. E. Miller, *On the interaction of strain and vorticity for solutions of the Navier–Stokes equation*, arXiv:2407.02691.
5. M. P. Encinar, *A length scale for non-local multi-scale gradient interactions in isotropic turbulence*, Journal of Fluid Mechanics 971 (2023), A40.
6. E. Miller, *A regularity criterion for the Navier–Stokes equation involving only the middle eigenvalue of the strain tensor*, arXiv:1710.05569.
7. Z. Grujić, *Logarithmic Depletion of Vortex Stretching and Singularity Evasion in the 3D Navier–Stokes Equations*, arXiv:2607.08866.

# Internal dependencies

- `NS_C1_UV_Replenishment_Chain_v0.2.md`
- `NS_C2_Critical_Toll_Spike_Packing_v0.3.md`
- `NS_C3A_Conservation_Criticality_Helical_Pair_Production_v0.1.md`
- `NS_C3B_BiHelical_Equalization_UniqueSign_UV_Escape_v0.1.md`
- `NS_C3C_ClassII_Nonlocality_Tax_Radial_Congestion_v0.1.md`
- `NS_C3D_CutoffFlux_HelicalKernel_Nonlocality_v0.1.md`
- `NS_C3E_ViscousWindow_PhaseEfficiency_Zeno_v0.1.md`
- `NS_C3F_PhaseSpace_Ancestry_Cone_v0.1.md`
- `NS_C3G_FirstCrossing_CausalAncestry_DepletionNoGo_v0.1.md`
- `NS_C3H_Ancestry_Renormalization_CriticalCompactnessBarrier_v0.1.md`
- `NS_C3I_FrontierUVCap_DefectTrichotomy_v0.1.md`
- `NS_C3J_GaugeCorrected_Reentry_Hysteresis_NoGo_v0.1.md`
- `NS_C3K_AbsoluteOccupancy_OneMomentGap_v0.1.md`
- `NS_C3L_CriticalMomentEscape_StrainGeometryDebt_v0.1.md`
- `NS_C3M_VorticityStrain_Betchov_GeometryDebt_v0.1.md`
- `True ETN / 無限維張力場`
- `X_Integral_Unified_Program_v0.2.md`

Next:

$$
\boxed{
\textbf{C3-O — Boundary Depletion versus Strain Self-Amplification Rigidity}
}
$$
