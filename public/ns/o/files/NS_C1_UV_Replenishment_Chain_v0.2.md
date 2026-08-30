---
title: "Navier–Stokes C1：高頻逃逸與非線性 UV 補給鏈"
subtitle: "From Finite-Time Blow-up to a Source-Certified Multiscale Replenishment Chain"
version: "v0.2"
date: "2026-08-14"
author: "Neo.K / EveMissLab"
language: "zh-TW"
status: "Theorem-style research note"
epistemic_status: "C1a/C1b proved from standard external regularity input; persistent triadic genealogy remains open."
---

# Navier–Stokes C1：高頻逃逸與非線性 UV 補給鏈

## 0. 目的

前一版整合框架提出：

$$
\mathrm{Blowup}(T_\ast)
\Longrightarrow
\mathrm{XLegalUVChain}.
$$

本輪把它拆成三層：

$$
\boxed{\mathrm{C1a}=\text{High-frequency tail escape}},
$$

$$
\boxed{\mathrm{C1b}=\text{Nonlinear UV replenishment chain}},
$$

$$
\boxed{\mathrm{C1c}=\text{Persistent triadic genealogy}}.
$$

其中 C1a、C1b 本輪閉合；C1c 仍 open。

---

# 1. 問題設定

考慮三維不可壓 Navier–Stokes：

$$
\partial_tu+(u\cdot\nabla)u+\nabla p=\nu\Delta u,
$$

$$
\nabla\cdot u=0.
$$

使用 Leray projector：

$$
\partial_tu-\nu\Delta u
=
-\mathbb P\nabla\cdot(u\otimes u).
$$

假設 $u$ 是由光滑、快速衰減、divergence-free 初值 $u_0$ 產生的 maximal classical solution，且 maximal time

$$
0<T_\ast<\infty.
$$

---

# 2. 外部輸入：critical $L^3$ blow-up criterion

Escauriaza–Seregin–Šverák 的 endpoint regularity theorem，以及 Tao 的 quantitative version，給出：若

$$
\sup_{0<t<T_\ast}\|u(t)\|_{L^3(\mathbb R^3)}<\infty,
$$

則解不能在 $T_\ast$ 發生 finite-time singularity。

故假如 $T_\ast$ 真是有限 blow-up time：

$$
\boxed{
\limsup_{t\uparrow T_\ast}\|u(t)\|_3=\infty.
}
$$

classical solution 亦滿足 energy equality：

$$
\frac12\|u(t)\|_2^2
+
\nu\int_0^t\|\nabla u(s)\|_2^2\,ds
=
\frac12\|u_0\|_2^2,
$$

所以：

$$
\boxed{\|u(t)\|_2\le\|u_0\|_2.}
$$

---

# 3. Littlewood–Paley cutoff

令 $P_{\le J}$ 為平滑 low-pass projector，頻率支撐在 $|\xi|\lesssim2^J$；令

$$
P_{>J}=I-P_{\le J}.
$$

Bernstein inequality：

$$
\|P_{\le J}f\|_3
\le
C_{\mathrm{LP}}2^{J/2}\|f\|_2.
$$

因此：

$$
\boxed{
\|P_{\le J}u(t)\|_3
\le
C_{\mathrm{LP}}2^{J/2}\|u_0\|_2.
}
$$

---

# 4. C1a：高頻尾端逃逸定理

## 定理 4.1（Fixed-cutoff UV escape）

若 $T_\ast<\infty$ 為 maximal classical blow-up time，則對每個固定 $J\in\mathbb Z$：

$$
\boxed{
\limsup_{t\uparrow T_\ast}\|P_{>J}u(t)\|_3=\infty.
}
$$

### 證明

由

$$
u=P_{\le J}u+P_{>J}u
$$

與 triangle inequality：

$$
\|P_{>J}u(t)\|_3
\ge
\|u(t)\|_3-\|P_{\le J}u(t)\|_3.
$$

而

$$
\|P_{\le J}u(t)\|_3
\le
C_{\mathrm{LP}}2^{J/2}\|u_0\|_2
$$

對固定 $J$ 是 uniform finite constant。

再用：

$$
\limsup_{t\uparrow T_\ast}\|u(t)\|_3=\infty,
$$

即得結論。$\square$

---

# 5. ETN 翻譯

定理 4.1 的標準 PDE 內容是：

$$
\forall J<\infty,\quad
\text{critical }L^3\text{ mass cannot remain below the fixed spectral ceiling }2^J.
$$

在 True ETN 語言中可描述為：

$$
\boxed{
\text{No finite-scale tension cap contains a hypothetical blow-up trajectory}.
}
$$

ETN 在此只是結構翻譯；真正 theorem 是定理 4.1。

---

# 6. X-Integral observation certificate

定義：

$$
X(J,t)
=
\left\langle
u(t),
P_{\le J}u(t),
P_{>J}u(t),
\|P_{>J}u(t)\|_3
\right\rangle.
$$

來源：

$$
\operatorname{Prov}X(J,t)
=
\left\langle
u_0,\text{same N--S solution},t,J,P_{>J}
\right\rangle.
$$

因此定理 4.1 給出：

$$
\boxed{
\forall J,\ \forall A>0,\
\exists t<T_\ast:
\|P_{>J}u(t)\|_3>A.
}
$$

這是一條合法的 observational multiscale escape certificate，但還不是 causal genealogy。

---

# 7. 固定時刻高頻尾端趨零

對任意固定 $t_0<T_\ast$，classical solution 滿足 $u(t_0)\in L^3$。

Littlewood–Paley approximation identity：

$$
P_{\le J}u(t_0)\to u(t_0)
\quad\text{in }L^3
$$

as $J\to\infty$。

所以：

$$
\boxed{
\|P_{>J}u(t_0)\|_3\to0.
}
$$

與定理 4.1 合併：

- 固定時刻：極高頻尾端 eventually small；
- 固定 cutoff：接近 $T_\ast$ 時尾端 eventually arbitrarily large。

故 hypothetical blow-up 必須持續把新的 critical content 推往更高尺度。

---

# 8. 遞迴尺度—時間選取

取：

$$
A_n\uparrow\infty,
\qquad
\varepsilon_n\downarrow0.
$$

可遞迴選：

$$
t_0<t_1<t_2<\cdots<T_\ast,
$$

$$
J_1<J_2<J_3<\cdots,
$$

使：

$$
t_n\uparrow T_\ast,
\qquad
J_n\uparrow\infty,
$$

且：

$$
\boxed{
\|P_{>J_n}u(t_{n-1})\|_3\le\varepsilon_n,
}
$$

$$
\boxed{
\|P_{>J_n}u(t_n)\|_3\ge A_n.
}
$$

理由：先固定 $t_{n-1}$，用高頻尾端趨零選 $J_n$；再固定 $J_n$，用定理 4.1 選更晚的 $t_n$。

---

# 9. Duhamel identity

在 $t_{n-1}<t_n$：

$$
u(t_n)
=
e^{\nu(t_n-t_{n-1})\Delta}u(t_{n-1})
-
\int_{t_{n-1}}^{t_n}
e^{\nu(t_n-s)\Delta}
\mathbb P\nabla\cdot(u\otimes u)(s)\,ds.
$$

投影到 $>J_n$：

$$
P_{>J_n}u(t_n)
=
e^{\nu(t_n-t_{n-1})\Delta}
P_{>J_n}u(t_{n-1})
-
\mathcal N_n,
$$

其中

$$
\boxed{
\mathcal N_n
=
\int_{t_{n-1}}^{t_n}
e^{\nu(t_n-s)\Delta}
P_{>J_n}
\mathbb P\nabla\cdot(u\otimes u)(s)\,ds.
}
$$

---

# 10. Heat part 不產生高頻增長

heat semigroup 在 $L^3$ 為 contraction：

$$
\|e^{\nu\tau\Delta}f\|_3\le\|f\|_3.
$$

故：

$$
\left\|
e^{\nu(t_n-t_{n-1})\Delta}
P_{>J_n}u(t_{n-1})
\right\|_3
\le\varepsilon_n.
$$

由 reverse triangle inequality：

$$
\|\mathcal N_n\|_3
\ge
\|P_{>J_n}u(t_n)\|_3
-
\left\|
e^{\nu(t_n-t_{n-1})\Delta}
P_{>J_n}u(t_{n-1})
\right\|_3.
$$

所以：

$$
\boxed{
\|\mathcal N_n\|_3\ge A_n-\varepsilon_n.
}
$$

---

# 11. C1b：非線性 UV 補給鏈定理

## 定理 11.1（Nonlinear UV Replenishment Chain）

若 $T_\ast<\infty$ 是 maximal finite blow-up time，則對任意

$$
A_n\uparrow\infty,\qquad\varepsilon_n\downarrow0,
$$

存在：

$$
t_n\uparrow T_\ast,
\qquad
J_n\uparrow\infty,
$$

使每一 interval $[t_{n-1},t_n]$ 的 nonlinear UV source object $\mathcal N_n$ 滿足：

$$
\boxed{
\|\mathcal N_n\|_3\ge A_n-\varepsilon_n.
}
$$

因此：

$$
\boxed{
\mathrm{finite\ blowup}
\Rightarrow
\text{arbitrarily high-frequency nonlinear replenishment at arbitrarily late times}.
}
$$

$\square$

---

# 12. 這比 C1a 多了什麼？

C1a 只說：

$$
\text{高頻必須很大}.
$$

C1b 說：

$$
\boxed{
\text{高頻不能只靠之前已存在的 tail 經 linear evolution 保存}.
}
$$

因為我們刻意讓 $t_{n-1}$ 的 $>J_n$ tail 小於 $\varepsilon_n$，而 $t_n$ 的同一 tail 大於 $A_n$。

heat part 只會收縮；故差額必須由原 N–S nonlinearity：

$$
\mathbb P\nabla\cdot(u\otimes u)
$$

補進去。

這已是 causal source statement。

---

# 13. X-Integration replenishment certificate

定義：

$$
\operatorname{XUVRepCert}_n
=
\left\langle
t_{n-1},
t_n,
J_n,
\varepsilon_n,
A_n,
S_n,
N_n,
G_n
\right\rangle,
$$

其中：

$$
S_n=\|P_{>J_n}u(t_{n-1})\|_3,
$$

$$
N_n=\|\mathcal N_n\|_3.
$$

守衛：

1. $t_{n-1}<t_n<T_\ast$；
2. $J_{n-1}<J_n$；
3. 所有 object 來自同一條 N–S trajectory；
4. $S_n\le\varepsilon_n$；
5. $\|P_{>J_n}u(t_n)\|_3\ge A_n$；
6. heat evolution 不放大 $L^3$ tail；
7. $N_n\ge A_n-\varepsilon_n$。

故每一步都具有可重播的來源、尺度與時間證書。

---

# 14. Fourier parent-scale lemma

使用 dyadic shells $\Delta_j$。

對標準 compactly-supported Littlewood–Paley multipliers，存在 universal integer $C_0$，使若 output 在 shell $j$，而兩 input shell 都滿足：

$$
j_1,j_2<j-C_0,
$$

則：

$$
\boxed{
\Delta_j
\mathbb P\nabla\cdot
(\Delta_{j_1}u\otimes\Delta_{j_2}u)
=
0.
}
$$

因為 Fourier support 要求：

$$
\xi=\eta+(\xi-\eta).
$$

兩個遠低於 $2^j$ 的 input frequencies 不可能相加到 output frequency $\sim2^j$。

所以任何生成 shell $j$ 的 nonlinear interaction 至少有一個 parent：

$$
\boxed{
\max\{j_1,j_2\}\ge j-C_0.
}
$$

這證明：

$$
\boxed{
\text{arbitrarily high output cannot be generated directly from two uniformly low-frequency parents}.
}
$$

---

# 15. C1c 仍未證

parent-scale support rule 不足以證：

1. canonical parent；
2. quantitatively large individual triad；
3. 同一 branch 跨所有 $n$ 延續；
4. cancellation 不破壞 genealogy；
5. 存在 nested causal branch：

$$
(j_1,t_1)\prec(j_2,t_2)\prec\cdots,
\qquad j_n\to\infty.
$$

故：

$$
\boxed{
\mathrm{C1c}
=
\text{Persistent Triadic Genealogy}
}
$$

仍為 OPEN。

---

# 16. C1 status

## C1a — CLOSED

$$
\boxed{
\mathrm{Blowup}
\Rightarrow
\forall J,\
\limsup_{t\uparrow T_\ast}
\|P_{>J}u(t)\|_3=\infty.
}
$$

## C1b — CLOSED

$$
\boxed{
\mathrm{Blowup}
\Rightarrow
\exists(J_n,t_n,\mathcal N_n):
J_n\to\infty,\
t_n\to T_\ast,\
\|\mathcal N_n\|_3\to\infty.
}
$$

## C1c — OPEN

$$
\boxed{
\mathrm{Blowup}
\Rightarrow
\text{one persistent source-preserving triadic genealogy to }j=\infty.
}
$$

---

# 17. 下一主問題

有兩條路。

## Route A — C1c genealogy extraction

研究：

$$
\mathcal N_n
=
\sum_{j>J_n}
\sum_{j_1,j_2}
\mathcal N_{j;j_1,j_2}^{(n)}
$$

能否從大 aggregate output 抽出 quantitatively persistent parent branch。

可能需要：

- paraproduct grouping；
- square-function orthogonality；
- frequency envelopes；
- concentration compactness；
- tree-selection lemma。

主要 no-go：

$$
\boxed{
\text{large aggregate output}
\not\Rightarrow
\text{one large triad}.
}
$$

## Route B — C2 coercive replenishment cost

跳過 canonical genealogy，直接問：

> 每一次 UV replenishment 是否必須支付某個正的、可加總的 coercive cost？

若可證：

$$
\sum_n\operatorname{Cost}(\mathcal N_n)=\infty
$$

但 N–S 的全域可用 budget 有限，則：

$$
\boxed{
\text{infinite UV replenishment chain}
\Rightarrow
\text{contradiction}.
}
$$

這將直接進入 C2 — Finite Obstruction。

---

# 18. No-go

禁止：

$$
\|P_{>J}u\|_3\to\infty
\Rightarrow
\exists j:\|\Delta_j u\|_3\to\infty
$$

的無證推論。

禁止：

$$
\|\mathcal N_n\|_3\gg1
\Rightarrow
\exists\text{ single large triad}.
$$

禁止把：

$$
\max(j_1,j_2)\ge j-C_0
$$

誤寫成 parent amplitude lower bound。

X 積分也不創造物理 interaction；它只保存原 N–S interaction 的來源、尺度、守衛與證書。

---

# 19. 結論

本輪將：

$$
\mathrm{Blowup}
\Rightarrow
\mathrm{UV\ escape}
$$

從概念框架升級成兩條必要條件：

$$
\boxed{
\forall J<\infty,\quad
\limsup_{t\uparrow T_\ast}
\|P_{>J}u(t)\|_3=\infty,
}
$$

以及：

$$
\boxed{
\exists J_n\uparrow\infty,\ 
t_n\uparrow T_\ast:
\|\mathcal N_n\|_3
\ge
A_n-\varepsilon_n
\to\infty.
}
$$

因此 hypothetical singularity 必須在愈來愈高的尺度上持續獲得 nonlinear replenishment。

下一個真正 frontier 是：

$$
\boxed{
\text{C1c genealogy extraction}
\quad\text{vs}\quad
\text{C2 coercive replenishment cost}.
}
$$

---

# References

1. C. L. Fefferman, *Existence and Smoothness of the Navier–Stokes Equation*, Clay Mathematics Institute.
2. L. Escauriaza, G. A. Seregin, V. Šverák, *$L_{3,\infty}$-solutions of the Navier–Stokes equations and backward uniqueness*, Russian Mathematical Surveys 58 (2003), 211–250.
3. T. Tao, *Quantitative bounds for critically bounded solutions to the Navier–Stokes equations*, arXiv:1908.04958.
4. I. Gallagher, G. S. Koch, F. Planchon, *A profile decomposition approach to the $L^\infty_t(L^3_x)$ Navier–Stokes regularity criterion*, arXiv:1012.0145.
5. I. Gallagher, G. S. Koch, F. Planchon, *Blow-up of critical Besov norms at a potential Navier–Stokes singularity*, arXiv:1407.4156.

# Internal dependencies

- `NS_ETN_XIntegration_Multiscale_NonCollapse_v0.1.md`
- `True ETN / 無限維張力場`
- `X_Integral_Unified_Program_v0.2.md`
- `X_Integral_Kakeya_PreMeasure_Reinterpretation_v0.1.md`
- `X_Singularity_Theory_Foundations_v0.1.md`
