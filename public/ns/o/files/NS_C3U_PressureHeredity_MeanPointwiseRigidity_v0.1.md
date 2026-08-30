---
title: "Navier–Stokes C3-U：Pressure-Poor Heredity Decomposition、Adjoint Mean-Strain Transport 與 Mean-to-Pointwise Rigidity"
subtitle: "A Conditional Heredity Theory for Weak Far-Pressure Support, Exact Adjoint Mean-Strain Transport, and Morrey/Shell Criteria for Upgrading Mean Strain to Pointwise Middle-Eigenvalue Geometry"
version: "v0.1"
date: "2026-08-14"
author: "Neo.K / EveMissLab"
language: "zh-TW"
status: "Theorem-style structural reduction / conditional rigidity note"
epistemic_status: "Exact pressure-matrix decomposition + exact adjoint mean-strain identity + standard Morrey/Weyl consequences + conditional ancestry heredity. Does NOT prove Navier–Stokes regularity."
---

# Navier–Stokes C3-U
# Pressure-Poor Heredity Decomposition、Adjoint Mean-Strain Transport 與 Mean-to-Pointwise Rigidity

## 0. 本輪定位

C3-T 把前一輪的兩個 survivor branch壓成兩個傳遞缺口：

### Uniform-cone branch

已有：

$$
K_\ast:v_{n,i}
\ge\gamma_0>0,
$$

但：

$$
\boxed{
\text{mean-strain cone}
\not\Rightarrow
\text{pointwise }\lambda_2^+\text{ geometry}.
}
$$

真正缺：

$$
\boxed{
\textbf{Mean-to-Pointwise Strain Rigidity}.
}
$$

### Cone-degeneration branch

每尺度都有 pressure-poor six-core witness，

但：

$$
\boxed{
\text{per-level pressure-poor witness}
\not\Rightarrow
\text{pressure-poor causal ray}.
}
$$

真正缺：

$$
\boxed{
\textbf{Pressure-Poor Heredity}.
}
$$

本輪得到：

1. parent→child far-pressure matrix變化可精確拆成：
   - spatial shift；
   - near/far reclassification；
   - temporal pressure-source turnover；
2. spatial shift本身有額外：
   $$
   \kappa^{-1}
   $$
   suppression；
3. reclassification由 annular rescaled enstrophy控制；
4. temporal turnover需要 pressure-source：
   $$
   f=\operatorname{tr}((\nabla u)^2)
   $$
   的 $L^1$ turnover，energy inequality本身不控制它；
5. adjoint cutoff下 local mean strain有 exact transport identity；
6. mean-strain direction rotation由一個 matrix nonlinear-turnover debt控制；
7. far-pressure direction turnover + mean-strain direction turnover共同控制 pressure efficiency的 parent→child變化；
8. 因此得到一個真正的 **Conditional Pressure-Poor Heredity Theorem**；
9. mean→pointwise可由 $p>3$ 的 local Morrey–Poincaré fluctuation bound閉合；
10. endpoint $p=3$ 正好失去 $L^\infty$ oscillation control；
11. 對 band-limited strain shell還有更局部的 eigenvalue-sign persistence；
12. 但 shell→full strain仍需 remainder smallness；
13. 即使 pointwise middle-strain event完全閉合，一個 parabolic event只支付 $O(1)$ critical Miller toll，無限 Zeno events仍與 hypothetical blow-up相容；
14. 所以本輪得到的是 PDE-level conditional interface，不是 global contradiction。

---

# 1. Pressure source與 Hessian kernel

whole-space pressure：

$$
-\Delta p
=
f,
$$

其中：

$$
\boxed{
f
=
\operatorname{tr}
((\nabla u)^2).
}
$$

pressure Hessian：

$$
\boxed{
H_p(x,t)
=
\nabla^2p(x,t)
=
\int_{\mathbb R^3}
K(x-y)f(y,t)\,dy
}
$$

以 principal-value / local-pressure expansion意義理解。

遠離：

$$
x=y
$$

時，kernel滿足：

$$
\boxed{
|\nabla^mK(z)|
\le
C_m|z|^{-3-m}.
}
$$

---

# 2. Parent / child ancestry geometry

考慮 causal parent：

$$
P
=
(x_p,t_p,R_p)
$$

與 child：

$$
C
=
(x_c,t_c,R_c),
$$

其中：

$$
t_p<t_c.
$$

eventual local ancestry給 bounded scale jump：

$$
\boxed{
c_LR_p
\le
R_c
\le
C_LR_p
}
$$

for fixed positive constants。

通常 forward UV ancestry有：

$$
R_c\le R_p,
$$

但以下只需 comparability。

定義 displacement：

$$
\boxed{
d_{pc}
=
|x_c-x_p|.
}
$$

phase-space ancestry route希望：

$$
d_{pc}\lesssim R_p.
$$

---

# 3. Smooth far cutoffs

固定：

$$
\kappa\gg1.
$$

取 parent far cutoff：

$$
\psi_p(y)
$$

使：

$$
\psi_p=0
$$

on：

$$
B_{\kappa R_p}(x_p),
$$

且：

$$
\psi_p=1
$$

outside：

$$
B_{2\kappa R_p}(x_p).
$$

child同樣：

$$
\psi_c.
$$

定義：

$$
f_p=f(\cdot,t_p),
\qquad
f_c=f(\cdot,t_c).
$$

以及 far matrices：

$$
\boxed{
H_p
=
T_{x_p}(\psi_pf_p),
}
$$

$$
\boxed{
H_c
=
T_{x_c}(\psi_cf_c),
}
$$

其中：

$$
T_x(g)
=
\int
K(x-y)g(y)\,dy.
$$

---

# 4. C3-U.1：Exact Pressure-Heredity Decomposition

加入兩個 intermediate terms：

$$
T_{x_c}(\psi_pf_c),
$$

$$
T_{x_c}(\psi_pf_p).
$$

則 exact：

$$
\boxed{
H_c-H_p
=
\Delta H_{\rm recl}
+
\Delta H_{\rm time}
+
\Delta H_{\rm space},
}
$$

其中：

## Reclassification

$$
\boxed{
\Delta H_{\rm recl}
=
T_{x_c}
\left[
(\psi_c-\psi_p)f_c
\right].
}
$$

## Temporal source turnover

$$
\boxed{
\Delta H_{\rm time}
=
T_{x_c}
\left[
\psi_p(f_c-f_p)
\right].
}
$$

## Spatial center shift

$$
\boxed{
\Delta H_{\rm space}
=
T_{x_c}(\psi_pf_p)
-
T_{x_p}(\psi_pf_p).
}
$$

這是 algebraic exact decomposition。

---

# 5. Spatial-shift estimate

假設：

$$
d_{pc}
\le
c_0R_p,
$$

以及：

$$
\kappa\ge4c_0.
$$

則對：

$$
y\in\operatorname{supp}\psi_p,
$$

$$
|x_p-y|
\gtrsim
\kappa R_p,
$$

且：

$$
|x_c-y|
\gtrsim
\kappa R_p.
$$

mean value theorem給：

$$
|K(x_c-y)-K(x_p-y)|
\le
C
d_{pc}
(\kappa R_p)^{-4}.
$$

所以：

## 定理 5.1

$$
\boxed{
|\Delta H_{\rm space}|
\le
C
d_{pc}
(\kappa R_p)^{-4}
\|f_p\|_1.
}
$$

由：

$$
\|f_p\|_1
\le
\|\nabla u(t_p)\|_2^2,
$$

得到：

$$
\boxed{
|\Delta H_{\rm space}|
\le
C
d_{pc}
\kappa^{-4}
R_p^{-4}
\|\nabla u(t_p)\|_2^2.
}
$$

---

# 6. Normalized spatial-turnover debt

定義：

$$
\boxed{
\mathfrak E_p
=
\frac{
R_p
\|\nabla u(t_p)\|_2^2
}{
\nu^2
}.
}
$$

以及 parent-scale normalized matrix：

$$
\widehat H
=
\frac{
R_p^4
}{
\nu^2
}
H.
$$

則：

$$
\boxed{
|\Delta\widehat H_{\rm space}|
\le
C
\frac{
d_{pc}
}{
R_p
}
\kappa^{-4}
\mathfrak E_p.
}
$$

因此若：

$$
d_{pc}=O(R_p),
$$

spatial center movement只支付：

$$
\boxed{
O(\kappa^{-4}\mathfrak E_p).
}
$$

它比 far Hessian amplitude的：

$$
O(\kappa^{-3}\mathfrak E_p)
$$

多一個：

$$
\kappa^{-1}.
$$

---

# 7. Reclassification annulus

$\psi_c-\psi_p$只支撐在 parent/child near–far definitions不同的 region。

記：

$$
\boxed{
\mathcal A_{pc}
=
\operatorname{supp}
(\psi_c-\psi_p).
}
$$

在 bounded scale jump、bounded center shift及 sufficiently large $\kappa$下，

此 region與 child center距離：

$$
\asymp
\kappa R_p
$$

up to fixed constants。

所以：

$$
\boxed{
|\Delta H_{\rm recl}|
\le
C
(\kappa R_p)^{-3}
\int_{\mathcal A_{pc}}
|f_c(y)|\,dy.
}
$$

由：

$$
|f_c|
\le
|\nabla u(t_c)|^2,
$$

定義：

$$
\boxed{
\mathfrak E_{pc}^{ann}
=
\frac{
R_p
}{
\nu^2
}
\int_{\mathcal A_{pc}}
|\nabla u(y,t_c)|^2dy.
}
$$

得到：

## 定理 7.1

$$
\boxed{
|\Delta\widehat H_{\rm recl}|
\le
C
\kappa^{-3}
\mathfrak E_{pc}^{ann}.
}
$$

---

# 8. Temporal source turnover

對 common parent far classification：

$$
\psi_p,
$$

有：

$$
\boxed{
|\Delta H_{\rm time}|
\le
C
(\kappa R_p)^{-3}
\|
\psi_p(f_c-f_p)
\|_1.
}
$$

定義 dimensionless temporal pressure-source turnover：

$$
\boxed{
\mathfrak T_{pc}^{far}
=
\frac{
R_p
}{
\nu^2
}
\|
\psi_p(f_c-f_p)
\|_1.
}
$$

則：

## 定理 8.1

$$
\boxed{
|\Delta\widehat H_{\rm time}|
\le
C
\kappa^{-3}
\mathfrak T_{pc}^{far}.
}
$$

---

# 9. Temporal turnover可以寫成時間導數債

smooth window上：

$$
f_c-f_p
=
\int_{t_p}^{t_c}
\partial_tf(\cdot,s)\,ds.
$$

因此：

$$
\boxed{
\mathfrak T_{pc}^{far}
\le
\frac{
R_p
}{
\nu^2
}
\int_{t_p}^{t_c}
\|
\psi_p\partial_tf(s)
\|_1ds
}
$$

加上若 cutoff本身也 time-dependent 時的 cutoff-turnover項。

而：

$$
f
=
\partial_i u_j\partial_j u_i.
$$

schematically：

$$
|\partial_tf|
\lesssim
|\nabla u|
|\nabla\partial_tu|.
$$

所以：

$$
\boxed{
\|\partial_tf\|_1
\lesssim
\|\nabla u\|_2
\|\nabla\partial_tu\|_2.
}
$$

energy inequality本身不控制：

$$
\boxed{
\int
\|\nabla\partial_tu\|_2dt.
}
$$

因此 temporal pressure-source turnover不是 energy-level finite budget。

---

# 10. Pressure-Heredity Debt Theorem

綜合：

## 定理 10.1

在 bounded displacement / bounded scale-jump ancestry step中：

$$
\boxed{
|\Delta\widehat H_{pc}|
\le
C
\left[
\frac{d_{pc}}{R_p}
\kappa^{-4}\mathfrak E_p
+
\kappa^{-3}
\mathfrak E_{pc}^{ann}
+
\kappa^{-3}
\mathfrak T_{pc}^{far}
\right].
}
$$

up to fixed comparability constants。

因此 parent→child far-pressure matrix variation的三個真正 carrier是：

$$
\boxed{
\text{spatial shift}
+
\text{reclassification}
+
\text{temporal source turnover}.
}
$$

---

# 11. Spatial shift不是主要 heredity obstacle

如果：

$$
d_{pc}=O(R_p),
$$

且：

$$
\mathfrak E_p
$$

沒有比 $\kappa^4$更快增長，

spatial contribution可透過大：

$$
\kappa
$$

壓小。

真正難點在：

$$
\boxed{
\mathfrak E_{pc}^{ann}
}
$$

與：

$$
\boxed{
\mathfrak T_{pc}^{far}.
}
$$

所以：

$$
\boxed{
\text{pressure非局部}
}
$$

本身不是 heredity 的完整答案。

真正缺的是：

$$
\boxed{
\text{far-source temporal stability}
+
\text{near/far classification stability}.
}
$$

---

# 12. Matrix-direction stability

令：

$$
H_p\ne0,
\qquad
H_c\ne0.
$$

定義 pressure support directions：

$$
\boxed{
K_p^H
=
-\frac{H_p}{|H_p|},
\qquad
K_c^H
=
-\frac{H_c}{|H_c|}.
}
$$

若：

$$
|H_c-H_p|
\le
\varepsilon_H
|H_p|,
\qquad
0<\varepsilon_H<\frac12,
$$

則 normalization map的 elementary estimate給：

$$
\boxed{
|K_c^H-K_p^H|
\le
4\varepsilon_H.
}
$$

所以 nondegenerate far matrix若變化相對小，其 direction也穩定。

---

# 13. Adjoint mean-strain transport

現在處理 local mean strain方向。

取 adjoint cutoff：

$$
\boxed{
\partial_t\chi
+
u\cdot\nabla\chi
+
\nu\Delta\chi
=
0.
}
$$

定義 matrix mean numerator：

$$
\boxed{
M_\chi(t)
=
\int
\chi(x,t)
S(x,t)\,dx.
}
$$

strain equation：

$$
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
$$

---

# 14. C3-U.2：Exact Adjoint Mean-Strain Transport Identity

## 定理 14.1

$$
\boxed{
\frac d{dt}
M_\chi(t)
=
-
\int
\chi
\left[
S^2
+
\frac14\omega\otimes\omega
-
\frac14|\omega|^2I
+
\nabla^2p
\right]dx.
}
$$

### 證明

計算：

$$
\frac d{dt}
\int\chi S
=
\int
(\partial_t\chi)S
+
\int
\chi\partial_tS.
$$

代入 adjoint cutoff與 strain equation。

diffusion：

$$
-\nu\int(\Delta\chi)S
+
\nu\int\chi\Delta S
=
0
$$

by integration by parts。

advection：

$$
-\int(u\cdot\nabla\chi)S
-
\int\chi(u\cdot\nabla)S
=
0
$$

因：

$$
\nabla\cdot u=0.
$$

剩餘即得。$\square$

---

# 15. Mean-strain turnover debt

定義：

$$
\boxed{
\mathcal R_S
=
S^2
+
\frac14\omega\otimes\omega
-
\frac14|\omega|^2I
+
\nabla^2p.
}
$$

則：

$$
\boxed{
M_\chi(t_c)-M_\chi(t_p)
=
-
\int_{t_p}^{t_c}
\int
\chi\mathcal R_S
\,dxdt.
}
$$

因此：

$$
\boxed{
|M_c-M_p|
\le
\int_{t_p}^{t_c}
\int
\chi
\left(
|S|^2
+
C|\omega|^2
+
|\nabla^2p|
\right)
dxdt.
}
$$

---

# 16. Mean-direction stability

若：

$$
M_p\ne0,
$$

且：

$$
|M_c-M_p|
\le
\varepsilon_M|M_p|,
\qquad
\varepsilon_M<\frac12,
$$

定義：

$$
v_p=\frac{M_p}{|M_p|},
\qquad
v_c=\frac{M_c}{|M_c|}.
$$

則：

$$
\boxed{
|v_c-v_p|
\le
4\varepsilon_M.
}
$$

所以 mean-strain orientation heredity需要：

$$
\boxed{
\text{small adjoint matrix-turnover relative to }|M_p|.
}
$$

---

# 17. Pressure support efficiency

定義：

$$
\boxed{
\eta_p
=
K_p^H:v_p,
}
$$

$$
\boxed{
\eta_c
=
K_c^H:v_c.
}
$$

positive common far-pressure support代表：

$$
\eta>0.
$$

pressure-poor代表：

$$
\eta
$$

小。

---

# 18. C3-U.3：Conditional Pressure-Poor Heredity Theorem

## 定理 18.1

若 parent→child一步滿足：

$$
\eta_p\le\eta_0,
$$

$$
|K_c^H-K_p^H|
\le\delta_H,
$$

$$
|v_c-v_p|
\le\delta_M,
$$

則：

$$
\boxed{
\eta_c
\le
\eta_0
+
\delta_H
+
\delta_M.
}
$$

### 證明

$$
\eta_c-\eta_p
=
(K_c^H-K_p^H):v_c
+
K_p^H:(v_c-v_p).
$$

由 unit norms：

$$
|\eta_c-\eta_p|
\le
|K_c^H-K_p^H|
+
|v_c-v_p|.
$$

$\square$

---

# 19. Quantitative sufficient heredity conditions

結合 §10、§12、§16：

若：

1. parent far matrix nondegenerate：
   $$
   |H_p|\ge h_p>0;
   $$

2. pressure-matrix turnover滿足：
   $$
   \frac{
   |H_c-H_p|
   }{
   |H_p|
   }
   \le
   \varepsilon_H;
   $$

3. adjoint mean-strain turnover滿足：
   $$
   \frac{
   |M_c-M_p|
   }{
   |M_p|
   }
   \le
   \varepsilon_M;
   $$

則：

$$
\boxed{
\eta_c
\le
\eta_p
+
4\varepsilon_H
+
4\varepsilon_M.
}
$$

所以 pressure-poor heredity不是不存在；

它有一個 exact conditional sufficient criterion。

---

# 20. Pressure-Heredity Triad of Debts

真正需要控制的是：

## U-H1 — Far-matrix reclassification debt

$$
\boxed{
\kappa^{-3}
\mathfrak E_{pc}^{ann}.
}
$$

## U-H2 — Far-source temporal turnover debt

$$
\boxed{
\kappa^{-3}
\mathfrak T_{pc}^{far}.
}
$$

## U-H3 — Mean-strain rotation debt

$$
\boxed{
\frac{
1
}{
|M_p|
}
\int_{t_p}^{t_c}
\int
\chi
|\mathcal R_S|
\,dxdt.
}
$$

spatial center shift則是相對較可控的：

$$
\boxed{
\frac{d_{pc}}{R_p}
\kappa^{-4}
\mathfrak E_p.
}
$$

---

# 21. Energy-only heredity no-go

global energy控制：

$$
\nu
\int
\|\nabla u\|_2^2dt.
$$

它不直接控制：

- instantaneous annular:
  $$
  \mathfrak E_{pc}^{ann};
  $$
- far pressure-source turnover:
  $$
  \mathfrak T_{pc}^{far};
  $$
- adjoint mean-strain matrix turnover:
  $$
  \int\chi|\mathcal R_S|.
  $$

因此：

$$
\boxed{
\text{Pressure-Poor Heredity}
}
$$

不能由 energy inequality單獨關閉。

---

# 22. Bounded-generation heredity criterion

若存在 fixed：

$$
L<\infty
$$

使每個 pressure-poor ancestry node在至多：

$$
L
$$

代內有 descendant，

且沿 parent→descendant path：

$$
\sum
(
\delta_H+\delta_M
)
\le
\varepsilon_0,
$$

則：

$$
\boxed{
\eta_{desc}
\le
\eta_{parent}
+
\varepsilon_0.
}
$$

若 threshold設計留有 margin，

即可 preserve pressure-poor status並抽 infinite bounded-gap poor ray。

這把 C3-T 的 combinatorial heredity criterion轉成 PDE sufficient condition。

---

# 23. Mean-to-pointwise：Morrey–Poincaré route

現在處理 uniform cone branch。

取 ball：

$$
B_R=B_R(x_0).
$$

定義 ordinary spatial mean：

$$
\boxed{
\bar S_R
=
\fint_{B_R}
S(x)\,dx.
}
$$

對：

$$
p>3,
$$

Morrey–Poincaré給：

$$
\boxed{
\|S-\bar S_R\|_{L^\infty(B_{R/2})}
\le
C_p
R^{1-3/p}
\|\nabla S\|_{L^p(B_R)}.
}
$$

---

# 24. C3-U.4：Mean-to-Pointwise Middle-Eigenvalue Theorem

## 定理 24.1

若：

$$
\boxed{
\lambda_2(\bar S_R)
>
C_p
R^{1-3/p}
\|\nabla S\|_{L^p(B_R)},
}
$$

則：

$$
\boxed{
\lambda_2(S(x))>0
}
$$

對：

$$
x\in B_{R/2}
$$

成立。

### 證明

Weyl inequality：

$$
\lambda_2(S(x))
\ge
\lambda_2(\bar S_R)
-
\|S(x)-\bar S_R\|_{\rm op}.
$$

而：

$$
\|\cdot\|_{\rm op}
\le
\|\cdot\|_F.
$$

代入 Morrey bound即得。$\square$

---

# 25. Negative-sign version

若：

$$
\boxed{
\lambda_2(\bar S_R)
<
-
C_p
R^{1-3/p}
\|\nabla S\|_{L^p(B_R)},
}
$$

則：

$$
\boxed{
\lambda_2(S(x))<0
}
$$

on：

$$
B_{R/2}.
$$

---

# 26. Scale-invariant oscillation ratio

若：

$$
\bar S_R\ne0,
$$

定義：

$$
\boxed{
\mathfrak O_{p,R}
=
\frac{
C_p
R^{1-3/p}
\|\nabla S\|_{L^p(B_R)}
}{
|\bar S_R|
}.
}
$$

以及 normalized middle gap：

$$
\boxed{
\delta_{2,R}
=
\frac{
\lambda_2(\bar S_R)
}{
|\bar S_R|
}.
}
$$

則：

$$
\boxed{
\mathfrak O_{p,R}
<
\delta_{2,R}
}
$$

保證 pointwise：

$$
\lambda_2>0.
$$

N–S scaling下：

$$
\boxed{
\mathfrak O_{p,R}
}
$$

是 dimensionless / scale-invariant。

---

# 27. Endpoint barrier

在：

$$
p=3,
$$

$W^{1,3}$ 不嵌入：

$$
L^\infty.
$$

所以：

$$
\boxed{
R^{1-3/p}
\|\nabla S\|_{L^p}
}
$$

的 Morrey pointwise mechanism在：

$$
p=3
$$

正好失效。

因此 mean→pointwise rigidity需要：

- $p>3$ local oscillation；
- 或 endpoint BMO/logarithmic type information；
- 或 band-limited structure。

這是一個 genuine endpoint barrier。

---

# 28. Energy / enstrophy層級不足

energy控制：

$$
\nabla u
$$

in：

$$
L_t^2L_x^2.
$$

而：

$$
\nabla S
$$

相當於：

$$
\nabla^2u.
$$

Mean-to-pointwise theorem要求：

$$
\nabla S\in L_x^p,
\qquad
p>3
$$

在相關 core/time。

所以：

$$
\boxed{
\text{energy/enstrophy budget}
\not\Rightarrow
\text{Morrey fluctuation smallness}.
}
$$

---

# 29. Band-limited shell route

對 strain shell：

$$
S_q
=
\Delta_qS,
$$

有 Bernstein：

$$
\boxed{
\|\nabla S_q\|_\infty
\le
C
\lambda_q
\|S_q\|_\infty.
}
$$

令：

$$
R=\lambda_q^{-1}.
$$

假設某點：

$$
x_0
$$

有：

$$
\boxed{
\lambda_2(S_q(x_0))
\ge
\delta
\|S_q\|_\infty
}
$$

for：

$$
\delta>0.
$$

---

# 30. C3-U.5：Band-Limited Middle-Eigenvalue Persistence

## 定理 30.1

存在 universal：

$$
c>0
$$

使：

$$
\boxed{
|x-x_0|
\le
c\delta R
}
$$

時：

$$
\boxed{
\lambda_2(S_q(x))
\ge
\frac{\delta}{2}
\|S_q\|_\infty.
}
$$

### 證明

Bernstein給：

$$
\|S_q(x)-S_q(x_0)\|
\le
C
\lambda_q
\|S_q\|_\infty
|x-x_0|.
$$

取：

$$
|x-x_0|
\le
\frac{\delta}{2C}\lambda_q^{-1}.
$$

再用 Weyl。$\square$

---

# 31. Shell-to-full pointwise transfer

令 remainder：

$$
\boxed{
R_q^S
=
S-S_q.
}
$$

若在上述 subcore：

$$
\boxed{
\|R_q^S\|_{L^\infty,op}
\le
\frac{\delta}{4}
\|S_q\|_\infty,
}
$$

則：

$$
\boxed{
\lambda_2(S(x))
\ge
\frac{\delta}{4}
\|S_q\|_\infty
>0.
}
$$

因此 band-limited route的兩個 proof obligations是：

1. shell eigenvalue-gap anchor；
2. full-strain remainder smallness。

---

# 32. Frontier velocity crossing並不自動給 strain anchor

C3-G first crossing控制：

$$
\|u_q\|_\infty
\sim
\nu\lambda_q.
$$

但這不推出：

$$
\boxed{
\|S_q\|_\infty
\gtrsim
\nu\lambda_q^2
}
$$

在同一點或同一 core。

velocity near maximum甚至可能有 gradient較小。

因此：

$$
\boxed{
\text{velocity frontier core}
}
$$

不能自動升格成：

$$
\boxed{
\text{strain eigenvalue core}.
}
$$

這是另一個 type gap。

---

# 33. Operator-active core可能更適合 strain anchor

Miller operator core由：

$$
\mathcal Q_{SV}
$$

與：

$$
\Delta S
$$

local ratio選出。

它天然更接近 strain derivatives，

但：

$$
\boxed{
\|\Delta S\|_2\text{ large}
}
$$

仍不推出：

$$
\boxed{
\lambda_2(S)\text{ positive}.
}
$$

所以 operator selection與 middle-eigenvalue geometry仍需額外 matrix-sign information。

---

# 34. 若 pointwise positive-middle event成功閉合

為 scaling audit暫取：

$$
\nu=1.
$$

假設在 parabolic event：

$$
B_{cR}(x_n)
\times
[t_n-cR^2,t_n]
$$

上有：

$$
\boxed{
\lambda_2^+(S)
\ge
c_0R^{-2}.
}
$$

則每一時間：

$$
\|\lambda_2^+\|_{L^3(B_{cR})}
\ge
cR^{-1}.
$$

所以：

$$
\boxed{
\int_{t_n-cR^2}^{t_n}
\|\lambda_2^+(t)\|_3^2dt
\ge
c_1>0.
}
$$

---

# 35. C3-U.6：Parabolic Middle-Strain Toll

每一個 amplitude：

$$
R^{-2}
$$

、volume：

$$
R^3
$$

、duration：

$$
R^2
$$

的 coherent positive-middle event支付：

$$
\boxed{
O(1)
}
$$

scale-critical：

$$
L_t^2L_x^3
$$

toll。

所以 infinitely many disjoint such events imply：

$$
\boxed{
\int
\|\lambda_2^+\|_3^2dt
=
\infty.
}
$$

這正與 Miller blow-up necessity相容。

---

# 36. Pointwise closure仍不形成 contradiction

因此即使 mean-to-pointwise route完全成功，

它最多可能實現：

$$
\boxed{
\text{known necessary }\lambda_2^+\text{ critical divergence}.
}
$$

無限 parabolic Zeno events每次付 fixed critical toll，

總和發散，

正是 hypothetical blow-up允許的情況。

所以：

$$
\boxed{
\text{pointwise middle-strain rigidity}
\neq
\text{regularity proof}.
}
$$

仍需要另一個 finite budget / incompatible geometry。

---

# 37. C3-U 的 Pressure-Poor Heredity Status

現在 pressure-poor heredity不再是模糊 OPEN。

它被壓成：

$$
\boxed{
\text{Heredity holds conditionally if}
}
$$

以下三個 turnover保持小：

1. far source reclassification；
2. far source temporal change；
3. local mean strain rotation。

其中 spatial center drift已有更強：

$$
\kappa^{-4}
$$

control。

所以真正下一步可以直接針對：

$$
\boxed{
\mathfrak E_{pc}^{ann},
\quad
\mathfrak T_{pc}^{far},
\quad
\mathfrak R_{S,pc}
}
$$

三個 quantities。

---

# 38. C3-U 的 Mean-to-Pointwise Status

mean→pointwise也不再只是概念 gap。

有兩條 rigorous sufficient routes：

## Route U-M1 — Morrey

$$
p>3,
$$

$$
\lambda_2(\bar S_R)
>
C
R^{1-3/p}
\|\nabla S\|_p.
$$

## Route U-M2 — Band-limited

shell eigen-gap anchor：

$$
\lambda_2(S_q(x_0))
\ge
\delta\|S_q\|_\infty
$$

+

full remainder small。

所以真正 missing不是 algebra。

而是：

$$
\boxed{
\text{能否由 singular ancestry已知 constraints
強迫其中一條 sufficient route成立？}
}
$$

目前 OPEN。

---

# 39. Major no-go

### NG-U1

$$
\text{bounded spatial ancestry displacement}
\Rightarrow
\text{pressure-poor heredity}.
$$

FALSE；還有 temporal/reclassification/strain-rotation debts。

### NG-U2

$$
\text{far pressure harmonic}
\Rightarrow
\text{far matrix direction time-stable}.
$$

FALSE without source-turnover control。

### NG-U3

$$
\text{energy inequality}
\Rightarrow
\mathfrak T_{pc}^{far}\text{ finite/small per event}.
$$

NOT PROVED。

### NG-U4

$$
\text{mean-strain narrow cone}
\Rightarrow
\text{pointwise }\lambda_2\text{ sign}.
$$

FALSE without fluctuation control。

### NG-U5

$$
W^{1,3}\text{ local control}
\Rightarrow
L^\infty\text{ oscillation control}.
$$

FALSE at endpoint。

### NG-U6

$$
\text{velocity shell critical amplitude}
\Rightarrow
\text{strain shell eigen-gap anchor}.
$$

FALSE / not established。

### NG-U7

$$
\text{pointwise middle-strain event}
\Rightarrow
\text{contradiction}.
$$

FALSE；it realizes known critical blow-up toll。

---

# 40. X-Integration guards 更新

## G-PHD

Pressure Heredity Decomposition：

$$
\Delta H
=
\Delta H_{\rm recl}
+
\Delta H_{\rm time}
+
\Delta H_{\rm space}.
$$

## G-ANN

保存 reclassification annulus：

$$
\mathfrak E_{pc}^{ann}.
$$

## G-PTURN

保存 far pressure-source turnover：

$$
\mathfrak T_{pc}^{far}.
$$

## G-MTURN

保存 adjoint mean-strain matrix turnover。

## G-HDIR

far matrix magnitude接近零時不得討論穩定 direction。

## G-MORREY

mean→pointwise若用 Morrey，必須：

$$
p>3.
$$

## G-ENDPOINT

$p=3$ 不能靜默使用 $L^\infty$ Morrey embedding。

## G-SHELLGAP

band-limited route必須保存 shell eigenvalue gap。

## G-SHELLREM

shell pointwise sign不得忽略 full-strain remainder。

---

# 41. True ETN 更新

Pressure heredity state：

$$
\boxed{
\Theta_{pc}^{press}
=
\left\langle
H_p,H_c,
\Delta H_{\rm space},
\mathfrak E_{pc}^{ann},
\mathfrak T_{pc}^{far},
K_p^H,K_c^H
\right\rangle.
}
$$

Mean-strain transport state：

$$
\boxed{
\Theta_{pc}^{mean}
=
\left\langle
M_p,M_c,
\int\chi\mathcal R_S,
v_p,v_c
\right\rangle.
}
$$

Pointwise upgrade state：

$$
\boxed{
\Theta_R^{pt}
=
\left\langle
\bar S_R,
\delta_{2,R},
\mathfrak O_{p,R},
S_q,
R_q^S
\right\rangle.
}
$$

Pressure-poor heredity變成：

$$
\boxed{
\text{small pressure-direction turnover}
+
\text{small mean-strain-direction turnover}.
}
$$

---

# 42. 新 frontier：C3-V

C3-U 已經把兩個 transfer gaps變成可計算 debts。

正式下一題：

$$
\boxed{
\textbf{C3-V — Turnover Packing and Strain-Fluctuation Escape}.
}
$$

---

# 43. C3-V proof obligations

## V1 — Temporal pressure-turnover packing

研究：

$$
\mathfrak T_{pc}^{far}
$$

沿 infinitely many viscous ancestry windows能否有 finite global budget。

若無，formalize其 critical moment scaling。

## V2 — Reclassification-annulus packing

研究：

$$
\sum_n
\mathfrak E_{p_nc_n}^{ann}
$$

是否受：

- active-worldvolume；
- shell occupancy；
- enstrophy；

限制。

## V3 — Mean-strain rotation packing

由：

$$
M'
=
-\int\chi\mathcal R_S
$$

研究跨無限 generations的：

$$
\sum_n
|v_{n+1}-v_n|.
$$

若 finite，得到 matrix-direction convergence。

## V4 — Heredity closure

若 V1–V3能控制，

套 C3-U Conditional Pressure-Poor Heredity，

抽 pressure-poor ancestry ray。

## V5 — Morrey fluctuation branch

研究：

$$
\mathfrak O_{p,R}
$$

若不 small，

是否強迫：

$$
\nabla S
$$

higher-moment escape。

## V6 — Band-limited strain anchor

尋找 operator-active / helical ancestry條件，

是否強迫某 shell：

$$
\lambda_2(S_q)
$$

有 nontrivial eigen-gap。

## V7 — Remainder trichotomy

若 shell eigen-gap存在但 full pointwise sign失敗，

則 remainder：

$$
R_q^S
$$

必與 shell同階。

將 remainder分：

- IR；
- UV；
- spatial；
- pressure/projection。

## V8 — Critical toll compatibility

任何 pointwise closure都必與 Miller：

$$
L_t^2L_x^3
$$

divergence正確對齊，

禁止把必要 divergence誤認成 contradiction。

---

# 44. 正式狀態

$$
\boxed{
\begin{aligned}
\text{pressure heredity exact decomposition}
&:\ \mathrm{PROVED},\\
\text{spatial far-matrix variation }\sim\kappa^{-4}
&:\ \mathrm{PROVED},\\
\text{reclassification bound by annular enstrophy}
&:\ \mathrm{PROVED},\\
\text{temporal far-source turnover bound}
&:\ \mathrm{PROVED},\\
\text{energy controls temporal turnover}
&:\ \mathrm{NOT\ PROVED},\\
\text{adjoint mean-strain transport identity}
&:\ \mathrm{PROVED},\\
\text{conditional pressure-poor heredity}
&:\ \mathrm{PROVED},\\
\text{unconditional pressure-poor heredity}
&:\ \mathrm{OPEN},\\
\text{Morrey mean-to-pointwise theorem }p>3
&:\ \mathrm{PROVED/STANDARD},\\
\text{endpoint }p=3\text{ mean-to-pointwise}
&:\ \mathrm{NO\mbox{-}GO\ by\ Morrey},\\
\text{band-limited eigenvalue persistence}
&:\ \mathrm{PROVED},\\
\text{shell-to-full transfer under remainder smallness}
&:\ \mathrm{PROVED\ CONDITIONAL},\\
\text{frontier velocity}\Rightarrow\text{strain eigen-gap}
&:\ \mathrm{NOT\ PROVED},\\
\text{parabolic middle-strain event has fixed critical toll}
&:\ \mathrm{PROVED/SCALING},\\
\text{pointwise closure}\Rightarrow\text{regularity}
&:\ \mathrm{FALSE/NO\mbox{-}GO},\\
\text{turnover-packing/fluctuation rigidity}
&:\ \mathrm{OPEN}.
\end{aligned}
}
$$

---

# 45. 結論

C3-T 留下兩個 propagation problems。

C3-U 現在把 pressure heredity拆成 exact：

$$
\boxed{
\Delta H
=
\Delta H_{\rm space}
+
\Delta H_{\rm recl}
+
\Delta H_{\rm time}.
}
$$

其中：

$$
\boxed{
|\Delta\widehat H_{\rm space}|
\lesssim
\frac dR
\kappa^{-4}
\mathfrak E_R,
}
$$

所以 bounded ancestry displacement本身相對可控。

真正 pressure-heredity gaps是：

$$
\boxed{
\kappa^{-3}
\mathfrak E_{pc}^{ann}
}
$$

與：

$$
\boxed{
\kappa^{-3}
\mathfrak T_{pc}^{far}.
}
$$

同時 adjoint cutoff給 local mean strain exact transport：

$$
\boxed{
M_\chi'
=
-
\int
\chi
\left[
S^2
+
\frac14\omega\otimes\omega
-
\frac14|\omega|^2I
+
\nabla^2p
\right].
}
$$

所以 mean-strain direction rotation也是一筆明確的 matrix-turnover debt。

只要 far-matrix direction與 mean-strain direction都穩定，

pressure-poor property就可 parent→child傳遞。

因此 heredity現在是：

$$
\boxed{
\textbf{conditional theorem},
}
$$

不是純粹黑箱 OPEN。

Mean→pointwise這邊也同樣：

$$
\boxed{
\lambda_2(\bar S_R)
>
C
R^{1-3/p}
\|\nabla S\|_{L^p},
\quad p>3
}
$$

就足以得到：

$$
\boxed{
\lambda_2(S(x))>0
}
$$

在 inner core。

或者用 band-limited shell eigen-gap + remainder smallness。

所以真正未閉合的已經不是「能不能升級」。

而是：

> singular ancestry已知的 budgets，能不能強迫 pressure turnover小、mean rotation小，或 strain fluctuation小？

下一輪：

$$
\boxed{
\textbf{C3-V — Turnover Packing and Strain-Fluctuation Escape}.
}
$$

---

# References

1. E. Miller, *A regularity criterion for the Navier–Stokes equation involving only the middle eigenvalue of the strain tensor*, arXiv:1710.05569; Arch. Rational Mech. Anal. 235 (2020).
2. E. Miller, *On the interaction of strain and vorticity for solutions of the Navier–Stokes equation*, arXiv:2407.02691; Pure and Applied Analysis 8 (2026).
3. Z. Bradshaw, T.-P. Tsai, *On the local pressure expansion for the Navier–Stokes equations*, arXiv:2001.11526.
4. T. Barker, C. Prange, *Localized smoothing for the Navier–Stokes equations and concentration of critical norms near singularities*, arXiv:1812.09115.
5. A. Cheskidov, M. Dai, *Regularity criteria for the 3D Navier–Stokes and MHD equations*, arXiv:1507.06611.

# Internal dependencies

- `NS_C3T_PressureDiversification_ConeEigenvalue_HeredityGap_v0.1.md`
- `NS_C3S_StrainConeMargin_MergerRigidity_v0.1.md`
- `NS_C3R_MultiCore_PressureHorizon_StrainConvexity_v0.1.md`
- `NS_C3Q_PressureProjection_OperatorLocalization_v0.1.md`
- `NS_C3P_OperatorEscape_FarPressureMatrix_v0.1.md`
- `NS_C3O_AdjointCore_BalanceDynamicsSeparation_v0.1.md`
- `NS_C3L_CriticalMomentEscape_StrainGeometryDebt_v0.1.md`
- `NS_C3G_FirstCrossing_CausalAncestry_DepletionNoGo_v0.1.md`
- `True ETN / 無限維張力場`
- `X_Integral_Unified_Program_v0.2.md`

Next:

$$
\boxed{
\textbf{C3-V — Turnover Packing and Strain-Fluctuation Escape}
}
$$
