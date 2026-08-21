---
title: "Navier–Stokes C5-D：Spatial–Matrix Motif Compatibility、Strong-Middle Cones 與 Quadratic/Pressure Convex-Hull Obstructions"
subtitle: "A Finite-Dimensional Incompatibility between Positive-Middle Strain Coherence, Seven-Point Quadratic Cancellation, and Common Far-Pressure Compensation"
version: "v0.1"
date: "2026-08-15"
author: "Neo.K / EveMissLab"
language: "zh-TW"
status: "Theorem-style spatial–matrix compatibility / first finite-dimensional recurrent-limit obstruction"
epistemic_status: "Exact finite-dimensional matrix algebra + conditional pointwise-cone interface + adjoint pressure ledger + convex-hull obstruction. Does NOT prove Navier–Stokes regularity."
---

# Navier–Stokes C5-D
# Spatial–Matrix Motif Compatibility、Strong-Middle Cones 與 Quadratic/Pressure Convex-Hull Obstructions

## 0. 本輪定位

C5-A 建立：

$$
\boxed{
\text{compensation-motif compactness}.
}
$$

C5-B 建立：

$$
\boxed{
\text{Young phase oscillation / load concentration defects}.
}
$$

C5-C 再證：

$$
\boxed{
\text{operator temporal phase}
=
\text{strain-dissipation-demand curvature source},
}
$$

但同時證明：

$$
\boxed{
\textbf{scalar temporal identities alone仍允許 separated compensation cycle}.
}
$$

所以 C5-D 正式離開 pure temporal scalar route，

把下列 objects放到同一 finite-dimensional spatial–matrix problem：

1. positive-middle strain direction；
2. local quadratic tensor：
   $$
   Q
   =
   S^2
   +
   \frac14\omega\otimes\omega
   -
   \frac14|\omega|^2I;
   $$
3. C4-J Seven-Point quadratic cancellation witness；
4. local adjoint pressure mean；
5. common harmonic far-pressure matrix；
6. C3-S convex-hull pressure geometry。

本輪得到 C5 第一個真正的：

$$
\boxed{
\textbf{finite-dimensional recurrent-limit incompatibility}.
}
$$

核心結果：

> 若 pointwise strain directions持續落在一個 sufficiently narrow、
> normalized middle eigenvalue strictly positive的 cone，
> 則所有 local quadratic tensors $Q$ 自動落入同一個 strict matrix half-space，
> **不需要任何 vorticity alignment 或 vorticity/strain ratio假設。**

因此：

$$
\boxed{
\text{Strong-Middle Pointwise Cone}
\Rightarrow
\text{Quadratic Coherence}
}
$$

而：

$$
\boxed{
\text{Seven-Point Zero-Barycenter Cancellation}
}
$$

與之不相容。

---

# 1. Fresh primary-source audit

本輪 external anchors：

## 1.1 Miller — middle strain geometry

Miller 的 strain formulation與 middle-eigenvalue regularity criterion證：

$$
\boxed{
\lambda_2^+
}
$$

是 scale-critical regularity channel，

且 strain constraint space：

$$
L^2_{st}
$$

與其 orthogonal complement對 N–S strain evolution具有實質意義。

## 1.2 Miller — strain/vorticity interaction

最新 strain-vorticity work證：

$$
\boxed{
\langle-\Delta S,\omega\otimes\omega\rangle=0,
}
$$

並把 strain / vorticity quadratic interaction與 advection depletion放到 operator architecture。

本輪不直接使用其 regularity theorem證明 matrix cone，

但用其 strain/vorticity decomposition確認：

$$
S^2,
\qquad
\omega\otimes\omega
$$

是 full N–S 真正的 local quadratic constituents。

## 1.3 Bradshaw–Tsai — local pressure expansion

whole-space N–S pressure具有 rigorous local expansion，

其中 near-field Calderón–Zygmund part與 far-field contribution可合法分開追蹤。

所以 C5-D 的 local pressure / common far-pressure matrix architecture具有 PDE provenance。

---

# 2. Local quadratic tensor

定義：

$$
\boxed{
Q(S,\omega)
=
S^2
+
\frac14
\omega\otimes\omega
-
\frac14
|\omega|^2I.
}
$$

其中：

$$
S=S^T,
\qquad
\operatorname{tr}S=0.
$$

注意：

$$
Q\in\operatorname{Sym}(3),
$$

一般：

$$
\operatorname{tr}Q
\ne0.
$$

pressure Hessian在 full strain equation中補足 trace / constraint complement。

---

# 3. Normalized positive-middle strain direction

取：

$$
\boxed{
K\in\operatorname{Sym}_0(3),
\qquad
|K|_F=1.
}
$$

ordered eigenvalues：

$$
\boxed{
k_1<k_2\le k_3,
}
$$

並假設：

$$
\boxed{
k_2>0.
}
$$

因 trace-free：

$$
k_1=-(k_2+k_3)<0.
$$

令：

$$
\boxed{
e_1
}
$$

為 $k_1$ 的 unit eigenvector。

---

# 4. Strong-middle shape parameter

定義：

$$
\boxed{
\theta_K
=
k_2k_3.
}
$$

由：

$$
|K|_F^2
=
k_1^2+k_2^2+k_3^2
=
1
$$

與：

$$
k_1=-(k_2+k_3),
$$

有：

$$
\boxed{
k_1^2-\frac12
=
k_2k_3
=
\theta_K.
}
$$

因：

$$
k_2,k_3>0,
$$

所以：

$$
\boxed{
\theta_K>0.
}
$$

### Interpretation

$\theta_K$量化 normalized strain shape離：

$$
\lambda_2=0
$$

的退化邊界有多遠。

若：

$$
k_2\downarrow0,
$$

則：

$$
\theta_K\downarrow0.
$$

---

# 5. Compressive-axis test tensor

定義：

$$
\boxed{
P_1
=
e_1\otimes e_1.
}
$$

以及：

$$
\boxed{
H_K
=
P_1
-
\frac{
1+\theta_K
}{
2
}
I.
}
$$

其 trace：

$$
\boxed{
\operatorname{tr}H_K
=
-\frac{
1+3\theta_K
}{
2
}.
}
$$

---

# 6. Vorticity positivity identity

計算：

$$
\boxed{
H_K
-
(\operatorname{tr}H_K)I
=
P_1+\theta_KI.
}
$$

因此：

$$
\boxed{
H_K:
\left[
\frac14
(
\omega\otimes\omega
-
|\omega|^2I
)
\right]
=
\frac14
\omega\cdot
(P_1+\theta_KI)
\omega.
}
$$

所以對任意：

$$
\omega\in\mathbb R^3,
$$

都有：

$$
\boxed{
H_K:
\left[
\frac14
(
\omega\otimes\omega
-
|\omega|^2I
)
\right]
\ge
\frac{
\theta_K
}{
4
}
|\omega|^2.
}
$$

### 關鍵

不需要：

- vorticity alignment；
- vorticity magnitude upper bound；
- helicity sign。

---

# 7. Strain-square positivity at cone center

因：

$$
P_1:K^2
=
k_1^2,
$$

$$
I:K^2
=
|K|_F^2
=
1,
$$

所以：

$$
H_K:K^2
=
k_1^2
-
\frac{
1+\theta_K
}{
2
}.
$$

用：

$$
k_1^2
=
\frac12+\theta_K,
$$

得到：

$$
\boxed{
H_K:K^2
=
\frac{
\theta_K
}{
2
}.
}
$$

---

# 8. Nearby strain directions

取 normalized：

$$
V\in\operatorname{Sym}_0(3),
\qquad
|V|_F=1.
$$

若：

$$
|V-K|_F
\le
\delta,
$$

則：

$$
V^2-K^2
=
(V-K)V
+
K(V-K).
$$

因此：

$$
\boxed{
|V^2-K^2|_F
\le
2\delta.
}
$$

所以：

$$
\boxed{
H_K:V^2
\ge
\frac{
\theta_K
}{2}
-
2
|H_K|_F
\delta.
}
$$

---

# 9. Strong-middle cone radius

定義：

$$
\boxed{
\delta_K
=
\frac{
\theta_K
}{
8|H_K|_F
}.
}
$$

若：

$$
\boxed{
|V-K|_F
\le
\delta_K,
}
$$

則：

$$
\boxed{
H_K:V^2
\ge
\frac{
\theta_K
}{
4
}.
}
$$

本文稱：

$$
\boxed{
\mathcal C_K
=
\{
V\in\operatorname{Sym}_0(3):
|V|_F=1,\ 
|V-K|_F\le\delta_K
\}
}
$$

為：

$$
\boxed{
\textbf{Strong-Middle Pointwise Strain Cone}.
}
$$

---

# 10. C5-D.1：Positive-Middle Cone → Quadratic Half-Space Theorem

## 定理 10.1

設：

$$
S\ne0,
$$

且：

$$
\boxed{
\frac{
S
}{
|S|_F
}
\in
\mathcal C_K.
}
$$

則對任意：

$$
\omega\in\mathbb R^3,
$$

有：

$$
\boxed{
H_K:
Q(S,\omega)
\ge
\frac{
\theta_K
}{
4
}
\left(
|S|_F^2
+
|\omega|^2
\right).
}
$$

若：

$$
S=0,
$$

同一 inequality仍成立。

### 證明

若：

$$
S=sV,
\qquad
s=|S|_F,
$$

則由 §9：

$$
H_K:S^2
=
s^2
H_K:V^2
\ge
\frac{
\theta_K
}{4}
|S|^2.
$$

再加 §6 的 vorticity lower bound。$\square$

---

# 11. Uniform half-space margin relative to $|Q|$

有：

$$
|S^2|_F
\le
|S|_F^2.
$$

另外：

$$
\left|
\omega\otimes\omega
-
|\omega|^2I
\right|_F
=
\sqrt2
|\omega|^2.
$$

所以：

$$
\boxed{
|Q|_F
\le
|S|^2
+
\frac{\sqrt2}{4}
|\omega|^2
\le
|S|^2+|\omega|^2.
}
$$

因此 C5-D.1 給：

$$
\boxed{
H_K:Q
\ge
\frac{
\theta_K
}{4}
|Q|.
}
$$

---

# 12. Unit half-space functional

定義：

$$
\boxed{
\widehat H_K
=
\frac{
H_K
}{
|H_K|_F
}.
}
$$

以及 margin：

$$
\boxed{
\gamma_K
=
\frac{
\theta_K
}{
4|H_K|_F
}
>0.
}
$$

則：

$$
\boxed{
\widehat H_K:
\frac{
Q
}{
|Q|
}
\ge
\gamma_K
}
$$

whenever：

$$
Q\ne0
$$

and the strain direction lies in：

$$
\mathcal C_K.
$$

---

# 13. First finite-dimensional consequence

所有 normalized quadratic directions：

$$
U
=
Q/|Q|
$$

都落在 strict half-space：

$$
\boxed{
\mathcal H_K^+
=
\{
U\in S^5:
\widehat H_K:U
\ge
\gamma_K
\}.
}
$$

因此：

$$
\boxed{
0
\notin
\operatorname{conv}
(
\mathcal H_K^+
).
}
$$

更強：

$$
\boxed{
\operatorname{dist}
\left(
0,
\operatorname{conv}
\mathcal H_K^+
\right)
\ge
\gamma_K.
}
$$

---

# 14. Weighted local quadratic mean

取：

$$
\chi\ge0.
$$

定義：

$$
\boxed{
A_\chi^Q
=
\int
\chi|Q|dx,
}
$$

$$
\boxed{
B_\chi^Q
=
\int
\chi Qdx.
}
$$

若：

$$
A_\chi^Q>0,
$$

coherence：

$$
\boxed{
\kappa_\chi^Q
=
\frac{
|B_\chi^Q|
}{
A_\chi^Q
}.
}
$$

---

# 15. C5-D.2：Strong-Middle Cone Forces Quadratic Coherence

若 $\chi$-relevant region中所有 nonzero strain directions滿足：

$$
S/|S|
\in
\mathcal C_K,
$$

則：

$$
\widehat H_K:B_\chi^Q
=
\int
\chi
\widehat H_K:Q
dx
\ge
\gamma_K
A_\chi^Q.
$$

所以：

$$
\boxed{
\kappa_\chi^Q
\ge
\gamma_K.
}
$$

### 結論

$$
\boxed{
\textbf{Strong-Middle Pointwise Cone}
\Rightarrow
\textbf{nondegenerate local quadratic mean coherence}.
}
$$

---

# 16. C5-D.3：Seven-Point Zero-Barycenter Incompatibility

C4-J 的 cancellation motif若：

$$
\kappa_j^Q\to0,
$$

可抽 Seven-Point limit：

$$
\boxed{
\sum_{i=1}^{7}
\alpha_i^\ast
U_i^\ast
=
0.
}
$$

但若 simultaneously：

$$
U_i^\ast
\in
\mathcal H_K^+
$$

for all：

$$
i,
$$

則：

$$
\widehat H_K:
\sum_i
\alpha_i^\ast U_i^\ast
\ge
\gamma_K
\sum_i\alpha_i^\ast
=
\gamma_K>0.
$$

矛盾。

因此：

$$
\boxed{
\textbf{Strong-Middle Cone}
\quad\text{and}\quad
\textbf{Seven-Point Zero-Barycenter Cancellation}
}
$$

不能同時存在於同一 recurrent limit。

---

# 17. 這是 C5 第一個真正 finite-dimensional incompatibility

C5-A/B/C 的 compactification本身只得到：

- limit states；
- defect measures；
- transition constraints。

C5-D.3 第一次得到：

$$
\boxed{
\textbf{兩個 recurrent limit motifs的 algebraic mutual exclusion}.
}
$$

這不是：

- norm divergence；
- integral budget；
- temporal packing。

它是純：

$$
\boxed{
\textbf{finite-dimensional convex geometry obstruction}.
}
$$

---

# 18. Approximate cone leakage

現實中 pointwise strain未必全部在 cone。

定義 good set：

$$
\boxed{
G_K
=
\left\{
x:
S(x)=0
\text{ or }
S(x)/|S(x)|
\in
\mathcal C_K
\right\}.
}
$$

定義 quadratic-mass leakage fraction：

$$
\boxed{
\varepsilon_\chi^K
=
\frac{
\int_{\mathbb R^3\setminus G_K}
\chi|Q|dx
}{
A_\chi^Q
}
}
$$

when：

$$
A_\chi^Q>0.
$$

---

# 19. C5-D.4：Quantitative Cone-Leakage / Cancellation Theorem

在 good region：

$$
\widehat H_K:Q
\ge
\gamma_K|Q|.
$$

在 bad region只有：

$$
\widehat H_K:Q
\ge
-|Q|.
$$

所以：

$$
\widehat H_K:B_\chi^Q
\ge
\left[
\gamma_K
(
1-\varepsilon_\chi^K
)
-
\varepsilon_\chi^K
\right]
A_\chi^Q.
$$

即：

$$
\boxed{
\kappa_\chi^Q
\ge
\left[
\gamma_K
-
(
1+\gamma_K
)
\varepsilon_\chi^K
\right]_+.
}
$$

---

# 20. Cancellation forces cone leakage

若：

$$
\kappa_\chi^Q
\le
\kappa_0
<
\gamma_K,
$$

則：

$$
\boxed{
\varepsilon_\chi^K
\ge
\frac{
\gamma_K-\kappa_0
}{
1+\gamma_K
}.
}
$$

特別：

若：

$$
\kappa_j^Q\to0,
$$

且：

$$
K_j\to K
$$

with：

$$
\lambda_2(K)>0,
$$

則：

$$
\boxed{
\liminf_j
\varepsilon_{\chi_j}^{K_j}
\ge
\frac{
\gamma_K
}{
1+\gamma_K
}
>0
}
$$

只要 cone margins保持 nondegenerate。

### 解讀

Quadratic cancellation若要存活，

必有 fixed fraction local quadratic mass由：

$$
\boxed{
\textbf{strain directions outside the strong-middle cone}
}
$$

承擔。

---

# 21. Recurrent-limit dichotomy

因此若：

$$
\kappa_j^Q\to0,
$$

只可能：

## D-Q1 — Middle-gap degeneration

$$
\boxed{
\theta_{K_j}
=
\lambda_2(K_j)\lambda_3(K_j)
\to0.
}
$$

或：

## D-Q2 — Strain-direction dispersion

$$
\boxed{
\varepsilon_{\chi_j}^{K_j}
\not\to0.
}
$$

也就是：

$$
\boxed{
\textbf{Q cancellation}
\Rightarrow
\textbf{normalized middle-gap degeneration}
\vee
\textbf{pointwise strain-direction leakage}.
}
$$

---

# 22. Meaning of middle-gap degeneration

因：

$$
|K_j|_F=1,
$$

若：

$$
\theta_{K_j}\to0
$$

且：

$$
\lambda_3(K_j)>0,
$$

則：

$$
\boxed{
\lambda_2(K_j)\to0.
}
$$

所以 normalized strain shape逼近：

$$
\boxed{
\lambda_2=0
}
$$

的 degenerate boundary，

schematically：

$$
(-1/\sqrt2,0,1/\sqrt2).
$$

這是：

$$
\boxed{
\textbf{Middle-Gap Degeneration Motif}.
}
$$

它不是 middle-strain positivity本身消失，

而是：

$$
\lambda_2^+
$$

相對 full strain amplitude變得太小。

---

# 23. Mean strain is not pointwise strain

C3-S 的：

$$
\boxed{
\text{strain cone}
}
$$

主要作用在 local mean matrices：

$$
M_i
$$

或：

$$
\bar S_R.
$$

C5-D.1–4 的 cone則是：

$$
\boxed{
\textbf{pointwise normalized strain-direction cone}.
}
$$

兩者不得混淆。

所以：

$$
\boxed{
\text{mean-strain cone}
\not\Rightarrow
\text{C5-D pointwise cone}
}
$$

without fluctuation control。

---

# 24. Mean-to-pointwise interface

令：

$$
\boxed{
\bar S_R
=
\frac1{
\int\chi
}
\int
\chi Sdx.
}
$$

假設：

$$
\bar S_R\ne0.
$$

定義：

$$
\boxed{
m_R
=
|\bar S_R|_F,
}
$$

$$
\boxed{
K_R
=
\frac{
\bar S_R
}{
m_R
}.
}
$$

---

# 25. Relative strain fluctuation

定義：

$$
\boxed{
\eta_R^S
=
\frac{
\|S-\bar S_R\|_{L^\infty(\operatorname{supp}\chi)}
}{
|\bar S_R|
}.
}
$$

若：

$$
\eta_R^S<1,
$$

則：

$$
S=m_R(K_R+E),
$$

$$
|E|\le\eta_R^S.
$$

---

# 26. Direction perturbation bound

若：

$$
V
=
\frac{
K+E
}{
|K+E|
},
$$

$$
|K|=1,
$$

$$
|E|\le\eta<1,
$$

則：

$$
\boxed{
|V-K|
\le
\frac{
2\eta
}{
1-\eta
}.
}
$$

所以若：

$$
\boxed{
\eta_R^S
\le
\eta_{K_R}^{crit}
:=
\frac{
\delta_{K_R}
}{
2+\delta_{K_R}
},
}
$$

則：

$$
\boxed{
S(x)/|S(x)|
\in
\mathcal C_{K_R}
}
$$

through the core。

---

# 27. C5-D.5：Mean-Coherence Excludes Quadratic Cancellation

若：

1. normalized mean direction：
   $$
   K_R
   $$
   satisfies：
   $$
   \lambda_2(K_R)>0;
   $$

2. relative fluctuation：
   $$
   \eta_R^S
   \le
   \eta_{K_R}^{crit};
   $$

則：

$$
\boxed{
\kappa_\chi^Q
\ge
\gamma_{K_R}
>0.
}
$$

因此：

$$
\boxed{
\textbf{Seven-Point quadratic cancellation is impossible on that core}.
}
$$

---

# 28. Cancellation forces strain fluctuation

反過來，

若：

$$
\kappa_\chi^Q
<
\gamma_{K_R},
$$

則：

$$
\boxed{
\eta_R^S
>
\eta_{K_R}^{crit}
}
$$

or normalized middle gap has already degenerated enough to make：

$$
\gamma_{K_R}
$$

small。

所以：

$$
\boxed{
\textbf{Quadratic cancellation}
\Rightarrow
\textbf{strain fluctuation / middle-gap debt}.
}
$$

---

# 29. Morrey derivative bridge

若：

$$
p>3,
$$

Morrey/Poincaré estimate給：

$$
\boxed{
\|S-\bar S_R\|_{L^\infty(B_R)}
\le
C_p
R^{1-3/p}
\|\nabla S\|_{L^p(B_R)}
}
$$

up to cutoff/ball constants。

因此若 cancellation要求：

$$
\eta_R^S
\ge
\eta_0>0,
$$

則：

$$
\boxed{
R^{1-3/p}
\|\nabla S\|_{L^p(B_R)}
\ge
c_p
\eta_0
|\bar S_R|.
}
$$

### 結論

Seven-Point cancellation若不走 middle-gap degeneration，

就必支付：

$$
\boxed{
\textbf{higher-derivative strain-fluctuation debt}.
}
$$

這直接接回：

- C3-V fluctuation/intermittency；
- C3-W/X/Y derivative geometry。

---

# 30. Quadratic intensity under cone coherence

C5-D.1還給：

$$
H_K:Q
\ge
\frac{
\theta_K
}{4}
|S|^2.
$$

所以：

$$
|Q|
\ge
\frac{
\theta_K
}{
4|H_K|
}
|S|^2
=
\gamma_K|S|^2.
$$

因此：

$$
\boxed{
A_\chi^Q
\ge
\gamma_K
\int
\chi|S|^2dx.
}
$$

---

# 31. Mean strain forces quadratic intensity

Jensen：

$$
\int
\chi|S|^2dx
\ge
\left(
\int\chi
\right)
|\bar S_R|^2.
$$

若：

$$
c_\chi R^3
\le
\int\chi
\le
C_\chi R^3,
$$

則：

$$
\boxed{
A_\chi^Q
\ge
c_\chi
\gamma_K
R^3
|\bar S_R|^2.
}
$$

定義 mean-strain critical amplitude：

$$
\boxed{
\mu_R
=
\frac{
R^2
|\bar S_R|
}{
\nu
}.
}
$$

則：

$$
\boxed{
a_\chi^Q
=
\frac{
R
}{
\nu^2
}
A_\chi^Q
\ge
c_\chi
\gamma_K
\mu_R^2.
}
$$

所以 strong-middle coherent mean core若：

$$
\mu_R\gtrsim1,
$$

local quadratic intensity自動 nondegenerate。

---

# 32. Local pressure re-entry

adjoint mean strain：

$$
\boxed{
M_\chi'
=
-B_\chi^Q-P_\chi,
}
$$

where：

$$
\boxed{
P_\chi
=
\int
\chi\nabla^2pdx.
}
$$

under cone coherence：

$$
\boxed{
\widehat H_K:B_\chi^Q
\ge
\gamma_K
A_\chi^Q.
}
$$

---

# 33. C5-D.6：Oriented Pressure Re-entry Theorem

假設：

$$
\boxed{
|M_\chi'|
\le
\varepsilon
A_\chi^Q,
}
$$

其中：

$$
0\le
\varepsilon
<
\gamma_K.
$$

由：

$$
P_\chi
=
-M_\chi'
-
B_\chi^Q,
$$

有：

$$
-\widehat H_K:P_\chi
=
\widehat H_K:B_\chi^Q
+
\widehat H_K:M_\chi'.
$$

所以：

$$
\boxed{
-\widehat H_K:P_\chi
\ge
(
\gamma_K-\varepsilon
)
A_\chi^Q.
}
$$

因此：

$$
\boxed{
|P_\chi|
\ge
(
\gamma_K-\varepsilon
)
A_\chi^Q.
}
$$

---

# 34. Critical pressure oscillation

C4-I / C3-X local Hessian estimate：

$$
\boxed{
|P_\chi|
\le
C
R^{-1}
\inf_{\ell\in\mathcal A_1}
\|
p-\ell
\|_{L^{3/2}(B_{CR})}.
}
$$

所以：

$$
\boxed{
\Pi_R^{(2)}
=
\nu^{-2}
\inf_{\ell\in\mathcal A_1}
\|
p-\ell
\|_{L^{3/2}(B_{CR})}
\ge
c
\frac{
R
}{
\nu^2
}
|P_\chi|.
}
$$

結合 §33：

$$
\boxed{
\Pi_R^{(2)}
\ge
c
(
\gamma_K-\varepsilon
)
a_\chi^Q.
}
$$

若再用 §31：

$$
\boxed{
\Pi_R^{(2)}
\ge
c
(
\gamma_K-\varepsilon
)
\gamma_K
\mu_R^2.
}
$$

---

# 35. C5-D.7：Strong-Middle Coherent Core Forces Pressure or Mean Rotation

若：

1. normalized mean direction：
   $$
   K_R
   $$
   有 uniform：
   $$
   \lambda_2(K_R)>0;
   $$

2. pointwise fluctuation小到進：
   $$
   \mathcal C_{K_R};
   $$

3. mean-strain amplitude：
   $$
   \mu_R\ge\mu_0>0;
   $$

則至少：

## D-MROT

$$
\boxed{
\frac{
R
}{
\nu^2
}
|M_\chi'|
\ge
c
\gamma_{K_R}
\mu_0^2,
}
$$

或：

## D-PRESS

$$
\boxed{
\Pi_R^{(2)}
\ge
c
\gamma_{K_R}^2
\mu_0^2.
}
$$

### 關鍵

Quadratic-cancellation branch已被 strong-middle pointwise cone排除，

所以 C4-I 的三分法：

$$
\text{Cancellation}
\vee
\text{Mean Rotation}
\vee
\text{Pressure}
$$

在此縮成：

$$
\boxed{
\text{Mean Rotation}
\vee
\text{Pressure Concentration}.
}
$$

---

# 36. Far harmonic pressure

Bradshaw–Tsai local pressure expansion允許 local / far pressure provenance。

對距 core足夠遠的 pressure source，

core內 far pressure為 harmonic，

其 Hessian可在小 core中展成：

$$
\boxed{
\nabla^2p_{far}(x)
=
F
+
\text{higher spatial remainder},
}
$$

其中 leading constant matrix：

$$
\boxed{
F\in\operatorname{Sym}_0(3)
}
$$

因 harmonicity：

$$
\operatorname{tr}F=0.
$$

這就是 C3-Q/S 的 far-pressure matrix architecture。

---

# 37. Trace-free part of the cone functional

$H_K$ 本身不 trace-free。

但對：

$$
F\in\operatorname{Sym}_0(3),
$$

只有：

$$
H_K^0
=
H_K
-
\frac13
(\operatorname{tr}H_K)I
$$

有作用。

直接計算：

$$
\boxed{
H_K^0
=
P_1
-
\frac13I.
}
$$

驚人地：

$$
\boxed{
H_K^0
}
$$

與：

$$
\theta_K
$$

無關。

它只依賴：

$$
\boxed{
\textbf{most-compressive eigenvector }e_1.
}
$$

---

# 38. Compressive-axis projector

定義：

$$
\boxed{
G(e)
=
e\otimes e
-
\frac13I
\in
\operatorname{Sym}_0(3).
}
$$

因此對 harmonic far-pressure matrix：

$$
F,
$$

$$
\boxed{
H_K:F
=
G(e_1):F.
}
$$

---

# 39. Multi-core common-pressure setting

考慮 cores：

$$
i=1,\ldots,m.
$$

每 core有：

- strong-middle cone center：
  $$
  K_i;
  $$
- compressive axis：
  $$
  e_i;
  $$
- local quadratic forcing；
- depleted mean rotation；
- same dominant far harmonic pressure matrix：
  $$
  F_\ast\in\operatorname{Sym}_0(3).
  $$

after absorbing local/far remainders，

suppose each core requires：

$$
\boxed{
G(e_i):F_\ast
\le
-c_i,
\qquad
c_i>0.
}
$$

---

# 40. C5-D.8：Compressive-Axis Convex-Hull Pressure Obstruction

## 定理 40.1

若：

$$
\boxed{
0
\in
\operatorname{conv}
\{
G(e_1),\ldots,G(e_m)
\},
}
$$

則不存在：

$$
F_\ast\in\operatorname{Sym}_0(3)
$$

與：

$$
c_i>0
$$

同時滿足：

$$
G(e_i):F_\ast
\le
-c_i
$$

for all：

$$
i.
$$

### 證明

存在：

$$
\alpha_i\ge0,
\qquad
\sum_i\alpha_i=1,
$$

使：

$$
\sum_i
\alpha_i
G(e_i)
=
0.
$$

乘：

$$
F_\ast
$$

：

$$
0
=
\sum_i
\alpha_i
G(e_i):F_\ast
\le
-
\sum_i
\alpha_ic_i
<0.
$$

矛盾。$\square$

---

# 41. Six-core witness

因：

$$
\operatorname{Sym}_0(3)
\simeq
\mathbb R^5,
$$

Carathéodory給：

若：

$$
0
\in
\operatorname{conv}
\{
G(e_i)
\}_{i\in I},
$$

則已存在：

$$
\boxed{
\le6
}
$$

個 compressive axes見證。

所以：

$$
\boxed{
\textbf{Six-Core Compressive-Axis Pressure Obstruction}.
}
$$

這和 C3-S 的 Six-Core Pressure Obstruction位於同一 dimension-five convex geometry，

但 witness object不同：

- C3-S：mean strain matrices；
- C5-D：compressive-axis STF projectors。

---

# 42. Orthogonal-triplet obstruction

若：

$$
e_1,e_2,e_3
$$

是一組 orthonormal basis，

則：

$$
\sum_{i=1}^{3}
e_i\otimes e_i
=
I.
$$

因此：

$$
\boxed{
G(e_1)+G(e_2)+G(e_3)
=
0.
}
$$

所以只需：

$$
\boxed{
3
}
$$

個 mutually orthogonal compressive axes，

就已：

$$
\boxed{
0
\in
\operatorname{conv}
\{
G(e_1),G(e_2),G(e_3)
\}.
}
$$

### C5-D.9：Orthogonal-Triplet Pressure Obstruction

三個 strong-middle coherent cores若：

1. compressive axes mutually orthogonal；
2. mean rotation depleted；
3. same dominant harmonic far-pressure matrix要同時補償；

則 impossible。

---

# 43. Meaning for pressure compensation

common far pressure若想支撐 many strong-middle coherent cores，

它不能容許 compressive axes在：

$$
\operatorname{Sym}_0(3)
$$

projector space中過度「包圍原點」。

所以 persistent common-pressure compensation要求：

$$
\boxed{
0
\notin
\operatorname{conv}
\{
G(e_i)
\}.
}
$$

等價存在某：

$$
F
$$

使：

$$
\boxed{
G(e_i):F
}
$$

具有 common sign。

這是一種：

$$
\boxed{
\textbf{Compressive-Axis Cone Coherence}.
}
$$

---

# 44. C5-D pressure escape classification

若 strong-middle pointwise coherence recurrently存在，

pressure若仍避免 contradiction，

至少需走：

## D-P1 — Mean-rotation escape

$$
\boxed{
M_\chi'
\text{ remains large}.
}
$$

## D-P2 — Pressure locality/source fragmentation

different cores不能再由同一 far harmonic matrix主導。

## D-P3 — Compressive-axis directional locking

$$
\boxed{
0
\notin
\operatorname{conv}
\{G(e_i)\}.
}
$$

## D-P4 — Strong-middle cone failure

strain direction disperses / middle gap degenerates。

## D-P5 — Pressure concentration

pressure local oscillation本身進 critical branch。

---

# 45. A C5 limit formulation

對每 recurrent core，

定義 normalized strain-direction measure：

$$
\boxed{
\nu_j^S
}
$$

on：

$$
S^4
\subset
\operatorname{Sym}_0(3)
$$

using selected local quadratic or strain-energy weight。

定義 quadratic-direction measure：

$$
\boxed{
\nu_j^Q
}
$$

on：

$$
S^5
\subset
\operatorname{Sym}(3)
$$

with：

$$
\chi|Q|
$$

weight。

---

# 46. Strong-middle support condition

若：

$$
\nu_j^S
$$

concentrates in：

$$
\mathcal C_K,
$$

則 C5-D.1 gives support constraint：

$$
\boxed{
\operatorname{supp}
\nu_j^Q
\subset
\mathcal H_K^+.
}
$$

hence any weak limit：

$$
\nu_\ast^Q
$$

also satisfies：

$$
\boxed{
\operatorname{supp}
\nu_\ast^Q
\subset
\mathcal H_K^+.
}
$$

---

# 47. C5-D.10：Limit Barycenter Incompatibility

若：

$$
\nu_\ast^S
$$

is supported inside one nondegenerate strong-middle cone：

$$
\mathcal C_K,
$$

then：

$$
\boxed{
\left|
\int
U
d\nu_\ast^Q(U)
\right|
\ge
\gamma_K.
}
$$

所以：

$$
\boxed{
\int
U
d\nu_\ast^Q(U)
=
0
}
$$

不可能。

### 結論

$$
\boxed{
\textbf{Q-cancellation limit}
}
$$

與：

$$
\boxed{
\textbf{single strong-middle strain-cone limit}
}
$$

互斥。

---

# 48. Recurrent limit escape

若：

$$
\int U\,d\nu_j^Q
\to0,
$$

則 any recurrent strain-direction limit必：

$$
\boxed{
\text{not be confined to a single positive-middle strong cone}
}
$$

unless：

$$
\boxed{
\theta_K\to0.
}
$$

因此：

$$
\boxed{
\textbf{Quadratic zero-barycenter}
\Rightarrow
\textbf{middle-gap degeneration}
\vee
\textbf{strain-direction mixing}.
}
$$

---

# 49. Relation to temporal motifs

C5-C 已證：

scalar temporal dynamics允許：

$$
O^+\to M
$$

separated compensation cycle。

C5-D現在說：

即使 temporal ordering合法，

若其中 Q-cancellation phase要補償 pressure，

它的 spatial/matrix state不能同時保持：

$$
\boxed{
\text{single strong-middle cone}.
}
$$

所以 recurrent temporal cycle必攜帶新的 spatial metadata：

$$
\boxed{
\text{directional dispersion}
\vee
\text{middle-gap degeneration}.
}
$$

這是 temporal→spatial compatibility第一次真正閉合。

---

# 50. Middle record toll與 strong-middle cone仍不同

C4-H只有：

$$
\boxed{
\int
\lambda_2^+
|S|^2
}
$$

record-window toll。

它不保證：

$$
\boxed{
\lambda_2(S)/|S|
\ge c_0
}
$$

pointwise。

所以 C5-D theorem不能直接從 C4-H middle toll啟動。

真正新增 gate是：

$$
\boxed{
\textbf{normalized strong-middle shape}.
}
$$

---

# 51. Strong-middle shape variable

對：

$$
S\ne0,
$$

定義：

$$
\boxed{
\vartheta(S)
=
\frac{
\lambda_2^+(S)
\lambda_3(S)
}{
|S|_F^2
}.
}
$$

若 normalized direction：

$$
K=S/|S|,
$$

則：

$$
\boxed{
\vartheta(S)
=
\theta_K.
}
$$

所以：

$$
\boxed{
\vartheta>0
}
$$

正是 C5-D half-space mechanism的 pointwise margin source。

---

# 52. C5-D survivor trichotomy for Q motif

如果 Seven-Point Q-cancellation recurrently active，

則至少：

## D-QGAP

$$
\boxed{
\vartheta
\to0
}
$$

on substantial quadratic mass；

或：

## D-QMIX

$$
\boxed{
\text{strain-direction cone leakage}
}
$$

carries substantial quadratic mass；

或：

## D-QDER

if mean direction remains coherent，

$$
\boxed{
R^{1-3/p}
\|\nabla S\|_{L^p}
/
|\bar S_R|
\gtrsim1.
}
$$

也就是 derivative fluctuation。

---

# 53. What C5-D has really eliminated

C4-J residual：

$$
\boxed{
Q
=
\text{Seven-Point Quadratic Cancellation}
}
$$

原本看起來是完全獨立 finite-dimensional compensator。

C5-D現在證：

$$
\boxed{
Q
}
$$

不能和：

$$
\boxed{
\text{strong-middle pointwise coherence}
}
$$

共存。

所以 Q不是 free compact motif。

它必同步：

$$
\boxed{
\text{Middle-Gap Degeneration}
\vee
\text{Strain-Direction Dispersion / Derivative Fluctuation}.
}
$$

---

# 54. Pressure geometry new bridge

同時，

strong-middle pointwise coherence若成立，

Q cancellation branch消失。

因此 local pressure avoidance只剩：

$$
\boxed{
\text{Mean Rotation}
\vee
\text{Pressure}.
}
$$

如果多 core再共享同一 far harmonic pressure，

pressure branch又受到：

$$
\boxed{
0
\notin
\operatorname{conv}
\{
e_i\otimes e_i-I/3
\}
}
$$

的 compressive-axis coherence要求。

所以：

$$
\boxed{
\textbf{pressure compensation itself produces a recurrent
axis-cone geometry}.
}
$$

---

# 55. C5-D first incompatibility cycle

目前可以寫：

$$
\boxed{
\begin{aligned}
&\text{Strong-Middle Pointwise Cone}\\
&\qquad\Downarrow\\
&\text{Quadratic Half-Space}\\
&\qquad\Downarrow\\
&\text{No Seven-Point Cancellation}\\
&\qquad\Downarrow\\
&\text{Mean Rotation}\vee\text{Pressure Re-entry}\\
&\qquad\Downarrow\\
&\text{if common far pressure: Compressive-Axis Convex-Hull Constraint}.
\end{aligned}
}
$$

而反方向：

$$
\boxed{
\text{Q Cancellation}
\Rightarrow
\text{Middle-Gap Degeneration}
\vee
\text{Direction Dispersion}.
}
$$

這就是 C5 第一個真正的：

$$
\boxed{
\textbf{spatial–matrix compatibility cycle}.
}
$$

---

# 56. Major no-go audit

### NG-D1

$$
\text{middle-strain record toll}
\Rightarrow
\text{strong-middle pointwise cone}.
$$

FALSE / not proved。

### NG-D2

$$
\text{mean-strain cone}
\Rightarrow
\text{pointwise strain cone}.
$$

FALSE without fluctuation control。

### NG-D3

$$
\text{positive-middle cone requires vorticity alignment}.
$$

FALSE。

C5-D test tensor handles arbitrary $\omega$。

### NG-D4

$$
\text{Q cancellation can coexist with uniform strong-middle pointwise cone}.
$$

FALSE。

### NG-D5

$$
\text{pressure re-entry}
\Rightarrow
\text{one common far-pressure matrix}.
$$

FALSE。

local/source-specific pressure may dominate。

### NG-D6

$$
\text{compressive-axis convex hull contains origin}
\Rightarrow
\text{pressure singularity contradiction}.
$$

FALSE。

It only obstructs one common far-pressure compensation matrix。

---

# 57. X-Integration guards 更新

## G-SCONEPT

mean cone與 pointwise normalized strain cone必分開。

## G-SMARGIN

strong-middle cone保留：

$$
\theta_K
=
\lambda_2(K)\lambda_3(K).
$$

## G-QHALF

quadratic directions必保存 half-space functional：

$$
H_K.
$$

## G-QLEAK

approximate cancellation必記 cone-leakage fraction：

$$
\varepsilon_\chi^K.
$$

## G-MIDGAP

$\theta_K\to0$ 是合法 boundary escape，

不得誤判為 cone theorem contradiction。

## G-PAXIS

far pressure與：

$$
G(e_1)
=
e_1\otimes e_1-I/3
$$

的 pairing需保存。

## G-FARCOMMON

multi-core pressure obstruction只有在 common far-matrix dominance證明後才能用。

---

# 58. True ETN 更新

C5-D spatial–matrix state：

$$
\boxed{
\Theta_\ast^{SM}
=
\left\langle
\nu_\ast^S,
\nu_\ast^Q,
\theta_\ast,
\gamma_\ast,
\varepsilon_\ast^{cone},
\mathcal U_\ast^{(7)},
\mu_\ast^R,
\Pi_\ast^{(2)},
\mathcal G_\ast^{axis}
\right\rangle.
}
$$

其中：

- $\nu_\ast^S$ = normalized strain-direction measure；
- $\nu_\ast^Q$ = quadratic-direction measure；
- $\theta_\ast$ = strong-middle shape margin；
- $\varepsilon^{cone}$ = Q-weighted cone leakage；
- $\mathcal U^{(7)}$ = Seven-Point witness；
- $\mu^R$ = mean-rotation metadata；
- $\mathcal G^{axis}$ = compressive-axis STF projector configuration。

---

# 59. C5 strategic status

C5-A：

$$
\text{motif compactness}.
$$

C5-B：

$$
\text{temporal Young / concentration defects}.
$$

C5-C：

$$
\text{temporal transition / curvature constraints}.
$$

C5-D：

$$
\boxed{
\textbf{first finite-dimensional recurrent-limit incompatibility}.
}
$$

具體：

$$
\boxed{
\text{Strong-Middle Cone}
\cap
\text{Seven-Point Zero-Barycenter}
=
\varnothing.
}
$$

而 common far-pressure compensation再受到：

$$
\boxed{
\text{compressive-axis convex-hull obstruction}.
}
$$

---

# 60. 新 frontier：C5-E

C5-D 最後留下三個 spatial escapes：

$$
\boxed{
\text{Middle-Gap Degeneration}
}
$$

$$
\boxed{
\text{Strain-Direction Dispersion / Derivative Fluctuation}
}
$$

$$
\boxed{
\text{Pressure Locality / Axis Locking / Mean Rotation}.
}
$$

所以正式下一題：

$$
\boxed{
\textbf{C5-E — Strain-Direction Defect Measures,
Middle-Gap Degeneration, and Derivative-Intermittency Closure}.
}
$$

---

# 61. C5-E proof obligations

## E1 — Strain-direction probability measure

用：

$$
\chi|Q|
$$

或 strain energy作 weight，

建立：

$$
\nu_j^S
$$

的 exact compactification與 strong-middle support spectrum。

## E2 — Middle-gap mass

定義：

$$
\boxed{
\mathfrak g_j(\delta)
=
\nu_j^S
\{
\vartheta(S)\le\delta
\}.
}
$$

研究 Q cancellation是否迫使 fixed mass進：

$$
\delta\downarrow0
$$

boundary。

## E3 — Directional dispersion defect

若 middle gap不退化，

量化 minimal number / angular diameter of strain cones required to allow Q zero barycenter。

## E4 — Mean-to-pointwise fluctuation

將：

$$
\eta_R^S
$$

用：

- Morrey；
- $D^2u$ active volume；
- C3-V fluctuation intermittency；

統一。

## E5 — Derivative-gate interface

若 Q motif recurrently需要：

$$
R^{1-3/p}
\|\nabla S\|_{L^p}
/|\bar S|
\gtrsim1,
$$

測是否能逼：

- derivative active-volume shrinkage；
- Grujić–Xu gate；
- 或 higher-order multiplicity。

## E6 — Axis-locking dynamics

若 common pressure永久要求：

$$
0\notin\operatorname{conv}\{G(e_i)\},
$$

研究 compressive axes是否被迫落入 fixed spherical cap。

## E7 — Axis locking × middle eigenframe

若 compressive axes鎖定，

是否限制：

- middle eigenvectors；
- vorticity geometry；
- mean rotation。

## E8 — Second finite-dimensional incompatibility

尋找：

$$
\boxed{
\text{axis locking}
+
\text{Q-cancellation-required dispersion}
}
$$

是否互斥。

---

# 62. 正式狀態

$$
\boxed{
\begin{aligned}
\theta_K=k_2k_3=k_1^2-\frac12
&:\ \mathrm{PROVED},\\
\text{compressive-axis test tensor}
&:\ \mathrm{DEFINED},\\
\text{vorticity contribution uniformly positive}
&:\ \mathrm{PROVED},\\
\text{strong-middle cone}\Rightarrow Q\text{ strict half-space}
&:\ \mathrm{PROVED},\\
\text{strong-middle cone}\Rightarrow\kappa_Q\ge\gamma_K
&:\ \mathrm{PROVED},\\
\text{Seven-Point zero barycenter under cone}
&:\ \mathrm{IMPOSSIBLE},\\
\text{cone-leakage lower bound under cancellation}
&:\ \mathrm{PROVED},\\
Q\text{-cancellation}\Rightarrow
\text{middle-gap degeneration or direction leakage}
&:\ \mathrm{PROVED},\\
\text{mean-to-pointwise interface}
&:\ \mathrm{CONDITIONAL\ ON\ FLUCTUATION},\\
\text{cancellation}\Rightarrow\text{Morrey derivative debt}
&:\ \mathrm{PROVED\ CONDITIONAL},\\
\text{oriented pressure re-entry}
&:\ \mathrm{PROVED\ UNDER\ CONE+MEAN\ STABILITY},\\
\text{compressive-axis convex-hull pressure obstruction}
&:\ \mathrm{PROVED},\\
\text{six-core witness}
&:\ \mathrm{PROVED},\\
\text{orthogonal-triplet obstruction}
&:\ \mathrm{PROVED},\\
\text{global regularity}
&:\ \mathrm{OPEN}.
\end{aligned}
}
$$

---

# 63. 結論

C5-C 證：

$$
\boxed{
\text{temporal scalar compensation cycle本身仍可存在}.
}
$$

C5-D 現在第一次把 recurrent compensation撞上真正 spatial–matrix geometry。

對 normalized positive-middle strain direction：

$$
K,
\qquad
\lambda_2(K)>0,
$$

定義：

$$
\boxed{
\theta_K
=
\lambda_2(K)\lambda_3(K)
=
\lambda_1(K)^2-\frac12
>0.
}
$$

再定義：

$$
\boxed{
H_K
=
e_1\otimes e_1
-
\frac{
1+\theta_K
}{2}
I.
}
$$

則在 sufficiently narrow strain cone內，

對**任意 vorticity**：

$$
\boxed{
H_K:Q
\ge
\frac{
\theta_K
}{4}
(
|S|^2+|\omega|^2
)
\ge
\frac{
\theta_K
}{4}
|Q|.
}
$$

所以 quadratic directions全部落同一 strict half-space：

$$
\boxed{
\widehat H_K:Q/|Q|
\ge
\gamma_K>0.
}
$$

因此：

$$
\boxed{
0
\notin
\operatorname{conv}\{Q/|Q|\}.
}
$$

Seven-Point zero-barycenter cancellation直接 impossible。

更定量地：

$$
\boxed{
\kappa_Q
\ge
[
\gamma_K
-
(1+\gamma_K)
\varepsilon_{\rm cone}
]_+.
}
$$

所以：

$$
\boxed{
Q\text{ cancellation}
\Rightarrow
\text{Middle-Gap Degeneration}
\vee
\text{Strain-Direction Leakage}.
}
$$

若 mean direction仍 coherent，

leakage再強迫：

$$
\boxed{
R^{1-3/p}
\|\nabla S\|_{L^p}
/
|\bar S_R|
\gtrsim1,
}
$$

把 Q motif直接送回 derivative/intermittency route。

另一方面，

strong-middle coherent core使 quadratic mean不再能 cancellation。

所以 mean rotation若也 depleted，

pressure必以 oriented方式 re-enter：

$$
\boxed{
-\widehat H_K:P_\chi
\gtrsim
A_\chi^Q.
}
$$

若多 cores再共享同一 harmonic far-pressure matrix：

$$
F_\ast\in\operatorname{Sym}_0(3),
$$

真正的 test direction簡化成：

$$
\boxed{
G(e_1)
=
e_1\otimes e_1-\frac13I.
}
$$

若：

$$
0
\in
\operatorname{conv}
\{G(e_{1,i})\},
$$

一個 common $F_\ast$不可能同時補償所有 cores。

因：

$$
\dim\operatorname{Sym}_0(3)=5,
$$

最多六 core就可見證。

更簡單：

三個 mutually orthogonal compressive axes直接：

$$
\boxed{
G(e_1)+G(e_2)+G(e_3)=0,
}
$$

所以已形成 **Orthogonal-Triplet Pressure Obstruction**。

這是 C5 到目前為止第一次真正得到：

$$
\boxed{
\textbf{finite-dimensional recurrent-limit incompatibility}.
}
$$

正式下一篇：

$$
\boxed{
\textbf{C5-E — Strain-Direction Defect Measures,
Middle-Gap Degeneration, and Derivative-Intermittency Closure}.
}
$$

---

# References

1. E. Miller, *A regularity criterion for the Navier–Stokes equation involving only the middle eigenvalue of the strain tensor*, arXiv:1710.05569; Arch. Rational Mech. Anal. 235 (2020).
2. E. Miller, *On the interaction of strain and vorticity for solutions of the Navier–Stokes equation*, arXiv:2407.02691v2; Pure and Applied Analysis 8 (2026), 247–270.
3. Z. Bradshaw, T.-P. Tsai, *On the local pressure expansion for the Navier–Stokes equations*, arXiv:2001.11526.
4. P. Constantin, *Pressure, Intermittency, Singularity*, arXiv:2301.04489.
5. Z. Grujić, L. Xu, *Asymptotic Criticality of the Navier–Stokes Regularity Problem*, Journal of Mathematical Fluid Mechanics 26, Article 53 (2024); arXiv:1911.00974.

# Internal dependencies

- `NS_C5C_TemporalCorrelation_CrossCurvatureOrdering_v0.1.md`
- `NS_C5B_TemporalYoung_PulsePhaseCompatibility_v0.1.md`
- `NS_C5A_RecordWindow_MotifCompactness_v0.1.md`
- `NS_C4J_CompensationRigidity_FinalSynchronizationAudit_v0.1.md`
- `NS_C4I_MiddleOperatorOverlap_PressureReentry_v0.1.md`
- `NS_C3S_StrainConeMargin_MergerRigidity_v0.1.md`
- `NS_C3U_PressureHeredity_MeanPointwiseRigidity_v0.1.md`
- `NS_C3V_TurnoverPacking_StrainFluctuationEscape_v0.1.md`
- `NS_C3W_PressureRotation_StrainSparseness_v0.1.md`
- `NS_C3X_JointPressureStrain_AnalyticityGap_v0.1.md`
- `NS_C3Y_DerivativeChain_IntermittencyTradeoff_v0.1.md`
- `True ETN / 無限維張力場`
- `X_Integral_Unified_Program_v0.2.md`

Next:

$$
\boxed{
\textbf{C5-E — Strain-Direction Defect Measures,
Middle-Gap Degeneration, and Derivative-Intermittency Closure}
}
$$
