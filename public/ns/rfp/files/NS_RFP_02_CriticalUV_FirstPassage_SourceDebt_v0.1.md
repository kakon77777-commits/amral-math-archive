---
title: "Navier–Stokes Reverse Formation Program 02：Critical UV First-Passage Skeleton、Shell Carrier/Bypass Dichotomy 與 Nonlinear Source Debt"
short_title: "NS-RFP 02"
version: "v0.1"
date: "2026-08-14"
author: "Neo.K / EveMissLab"
language: "zh-TW"
status: "Theorem-style structural advance / partial Chain-Necessity bridge"
epistemic_status: "Proves that critical UV escape generates a canonical adjacent-scale first-passage skeleton and an equation-level nonlinear source debt on every non-synchronous edge. Does NOT yet prove source-resolved ancestry, spatial-core ancestry, Finite Obstruction, or Navier–Stokes regularity."
canonical_source: "UTF-8 Markdown"
---

# Navier–Stokes Reverse Formation Program 02

# Critical UV First-Passage Skeleton、Shell Carrier/Bypass Dichotomy 與 Nonlinear Source Debt

## 0. 本文定位

NS-RFP 01 將 Navier–Stokes singularity problem 重寫為：

$$
\boxed{
\text{State}
+
\text{Edge}
+
\text{Guard}
+
\text{Escape}
+
\text{Closure}.
}
$$

並提出兩個終極 proof obligations：

$$
\boxed{
\textbf{Chain Necessity}
+
\textbf{Finite Obstruction}.
}
$$

第一個 obligation 是：

$$
\operatorname{Blowup}(T_\ast)
\Longrightarrow
\exists
\Gamma_\infty
\in
\mathfrak A_{NS}^{\infty}.
$$

此前已知的 internal reduction 只到：

$$
\boxed{
\operatorname{Blowup}(T_\ast)
\Longrightarrow
\text{critical UV escape}.
}
$$

本文攻擊兩者之間的第一座橋。

主結果不是完整 Chain Necessity。

本文證明：

$$
\boxed{
\text{critical UV escape}
\Longrightarrow
\text{canonical adjacent-scale first-passage skeleton}
}
$$

並進一步證明：

$$
\boxed{
\text{every non-synchronous first-passage edge carries a positive nonlinear Duhamel source debt}.
}
$$

所以：

$$
\boxed{
\text{high-frequency presence}
}
$$

第一次被提升為：

$$
\boxed{
\text{time-ordered scale crossing}
+
\text{equation-level source burden}.
}
$$

仍缺的資訊是：

$$
\boxed{
\text{which parent interaction generated the child?}
}
$$

以及：

$$
\boxed{
\text{where is the physical-space ancestry core?}
}
$$

---

# 1. Setting

考慮三維不可壓縮 Navier–Stokes：

$$
\partial_tu
-\nu\Delta u
+
\mathbb P\nabla\cdot(u\otimes u)
=
0,
$$

$$
\nabla\cdot u=0,
$$

在：

$$
0\le t<T_\ast
$$

上 smooth。

$\mathbb P$ 為 Leray projector。

假設：

$$
T_\ast<\infty
$$

為 maximal smooth existence time。

取標準 smooth homogeneous Littlewood–Paley decomposition：

$$
u
=
\sum_{j\in\mathbb Z}
u_j,
$$

其中：

$$
u_j
=
\Delta_j u.
$$

本文所有 high-frequency quantities 都在 smooth pre-singular interval 上使用，因此不涉及 distribution-level low-frequency ambiguity。

---

# 2. Critical UV input

此前已證 reduction：

## Proposition 2.1 — Critical UV Necessity

若：

$$
T_\ast
$$

為真正 finite singular time，

則對任意固定 dyadic cutoff：

$$
J<\infty,
$$

有：

$$
\boxed{
\limsup_{t\uparrow T_\ast}
\|P_{>J}u(t)\|_{L^3}
=
\infty.
}
$$

證明只使用：

- critical $L^3$ blow-up criterion；
- energy bound；
- Bernstein inequality。

本文以 Proposition 2.1 為 internal proved input。

---

# 3. 為何直接使用 $\|P_{>J}u\|_3$ 不夠乾淨？

對：

$$
H_J(t)
=
\|P_{>J}u(t)\|_3,
$$

$J$ 增加時沒有 pointwise norm monotonicity：

$$
H_{J+1}(t)
\le
H_J(t)
$$

一般不成立。

原因是：

$$
L^3
$$

不是 frequency-orthogonal norm。

若直接用：

$$
H_J
$$

定義 first-passage time，

無法自動得到：

$$
\tau_J
\le
\tau_{J+1}.
$$

所以需要一個：

- critical；
- dyadic；
- high-tail；
- 對 $J$ 單調；

的 replacement。

---

# 4. Critical shell burden

定義：

$$
\boxed{
\mathcal B_J(t)
=
\left(
\sum_{j>J}
\|u_j(t)\|_{L^3}^2
\right)^{1/2}.
}
$$

稱為：

$$
\boxed{
\textbf{critical shell burden}.
}
$$

每個：

$$
\|u_j\|_3
$$

在 Navier–Stokes scaling 下是 critical amplitude。

$\mathcal B_J$ 是 high-frequency shell amplitudes 的 $\ell^2$ aggregation。

---

# 5. $\mathcal B_J$ 的 scale monotonicity

由定義：

$$
\mathcal B_{J+1}(t)^2
=
\sum_{j>J+1}
\|u_j(t)\|_3^2
\le
\sum_{j>J}
\|u_j(t)\|_3^2.
$$

因此：

$$
\boxed{
\mathcal B_{J+1}(t)
\le
\mathcal B_J(t).
}
$$

這是 exact。

---

# 6. Littlewood–Paley domination

Littlewood–Paley square-function inequality給出：

$$
\|P_{>J}u\|_3
\le
C_{\rm LP}
\left\|
\left(
\sum_{j>J}
|u_j|^2
\right)^{1/2}
\right\|_3.
$$

又由：

$$
\left\|
\sum_{j>J}|u_j|^2
\right\|_{3/2}
\le
\sum_{j>J}
\||u_j|^2\|_{3/2},
$$

有：

$$
\left\|
\left(
\sum_{j>J}|u_j|^2
\right)^{1/2}
\right\|_3
\le
\left(
\sum_{j>J}
\|u_j\|_3^2
\right)^{1/2}.
$$

所以：

$$
\boxed{
\|P_{>J}u(t)\|_3
\le
C_{\rm LP}\mathcal B_J(t).
}
$$

---

# 7. C2.1 — Shell-Burden UV Necessity

## Theorem 7.1

若：

$$
T_\ast
$$

為 finite singular time，

則對任意固定：

$$
J<\infty,
$$

有：

$$
\boxed{
\limsup_{t\uparrow T_\ast}
\mathcal B_J(t)
=
\infty.
}
$$

### Proof

若某固定 $J$ 有：

$$
\sup_{t<T_\ast}\mathcal B_J(t)<\infty,
$$

則由 Littlewood–Paley domination：

$$
\sup_{t<T_\ast}
\|P_{>J}u(t)\|_3
<
\infty,
$$

與 Proposition 2.1 矛盾。$\square$

---

# 8. Pre-singular compact-window tail vanishing

## Lemma 8.1

對任意：

$$
t_0<T_\ast,
$$

有：

$$
\boxed{
\sup_{0\le t\le t_0}
\mathcal B_J(t)
\to0
\qquad
(J\to\infty).
}
$$

### Proof

因 solution 在 compact pre-singular interval：

$$
[0,t_0]
$$

上 smooth，

對任意足夠大：

$$
m>1/2
$$

有：

$$
\sup_{0\le t\le t_0}
\|u(t)\|_{H^m}
<
\infty.
$$

Bernstein 與 dyadic Sobolev estimate給出：

$$
\|u_j(t)\|_3
\le
C2^{j/2}\|u_j(t)\|_2
\le
C2^{-j(m-1/2)}
\|u(t)\|_{H^m}.
$$

因此：

$$
\mathcal B_J(t)^2
\le
C
\|u(t)\|_{H^m}^2
\sum_{j>J}
2^{-2j(m-1/2)}.
$$

右側在：

$$
[0,t_0]
$$

上一致趨零。$\square$

---

# 9. Continuity

## Lemma 9.1

對每個固定：

$$
J,
$$

函數：

$$
t\mapsto\mathcal B_J(t)
$$

在：

$$
[0,T_\ast)
$$

連續。

### Proof sketch

每個：

$$
u_j(t)
$$

在 $L^3$ 中連續。

對任何 compact：

$$
[0,t_0]\subset[0,T_\ast),
$$

Lemma 8.1 的相同 Sobolev domination使 dyadic $\ell^2$ tail 一致收斂。

因此有限部分連續，加上一致小 tail，得到 $\mathcal B_J$ 連續。$\square$

---

# 10. First-passage time

固定 critical threshold：

$$
M>0.
$$

由 smooth initial data：

$$
\mathcal B_J(0)\to0.
$$

所以存在：

$$
J_0(M)
$$

使：

$$
\mathcal B_J(0)<M
$$

對所有：

$$
J\ge J_0(M).
$$

定義：

$$
\boxed{
\tau_J(M)
=
\inf
\left\{
t\in[0,T_\ast):
\mathcal B_J(t)\ge M
\right\}.
}
$$

由 Theorem 7.1，此集合非空。

由 continuity：

$$
\boxed{
\mathcal B_J(\tau_J(M))
=
M.
}
$$

---

# 11. C2.2 — UV First-Passage Skeleton Theorem

## Theorem 11.1

假設 finite-time blow-up。

對任意固定：

$$
M>0,
$$

以及所有充分大的：

$$
J,
$$

first-passage times滿足：

$$
\boxed{
\tau_J(M)
\le
\tau_{J+1}(M)
<
T_\ast,
}
$$

且：

$$
\boxed{
\tau_J(M)
\uparrow
T_\ast
\qquad
(J\to\infty).
}
$$

### Proof

由：

$$
\mathcal B_{J+1}(t)
\le
\mathcal B_J(t),
$$

若 deeper tail 已達 threshold：

$$
\mathcal B_{J+1}(t)\ge M,
$$

則：

$$
\mathcal B_J(t)\ge M.
$$

所以：

$$
\tau_J(M)
\le
\tau_{J+1}(M).
$$

令：

$$
\tau_\infty
=
\lim_{J\to\infty}\tau_J(M)
\le
T_\ast.
$$

若：

$$
\tau_\infty<T_\ast,
$$

取：

$$
t_0
$$

滿足：

$$
\tau_\infty<t_0<T_\ast.
$$

則對所有充分大 $J$：

$$
\tau_J(M)<t_0.
$$

因此：

$$
\sup_{0\le t\le t_0}
\mathcal B_J(t)
\ge
M.
$$

但 Lemma 8.1 給出：

$$
\sup_{0\le t\le t_0}
\mathcal B_J(t)\to0.
$$

矛盾。

故：

$$
\tau_\infty=T_\ast.
$$

$\square$

---

# 12. 第一個真正的 bounded-gap skeleton

Theorem 11.1 給出 canonical sequence：

$$
\boxed{
\mathfrak S_M
=
\left\{
(\tau_J(M),J)
\right\}_{J\ge J_0(M)}.
}
$$

它滿足：

$$
J\to J+1
$$

的 exact adjacent-scale progression。

所以：

$$
\boxed{
\text{blow-up}
\Longrightarrow
\text{an adjacent-dyadic-scale, time-ordered UV crossing skeleton}.
}
$$

這比任意抽取：

$$
j_n\to\infty
$$

強。

但：

$$
\boxed{
\mathfrak S_M
\neq
\text{source-traceable ancestry}.
}
$$

目前只得到：

$$
\text{crossing order},
$$

沒有得到：

$$
\text{parent identity}.
$$

---

# 13. First-passage shell decomposition

由定義：

$$
\mathcal B_J(t)^2
=
\|u_{J+1}(t)\|_3^2
+
\mathcal B_{J+1}(t)^2.
$$

在：

$$
t=\tau_J(M)
$$

有：

$$
M^2
=
\|u_{J+1}(\tau_J)\|_3^2
+
\mathcal B_{J+1}(\tau_J)^2.
$$

定義：

$$
\boxed{
\eta_J(M)
=
\frac{
\mathcal B_{J+1}(\tau_J(M))
}{
M
},
}
$$

以及：

$$
\boxed{
\beta_J(M)
=
\frac{
\|u_{J+1}(\tau_J(M))\|_3
}{
M
}.
}
$$

則：

$$
\boxed{
\eta_J(M)^2+\beta_J(M)^2=1.
}
$$

---

# 14. C2.3 — Shell Carrier / Deep-Tail Bypass Dichotomy

## Theorem 14.1

每個 first-passage scale：

$$
J
$$

exactly滿足：

$$
\boxed{
\beta_J
=
\sqrt{1-\eta_J^2}.
}
$$

因此可分：

## Branch SC — Shell-carrier

若存在：

$$
\delta>0
$$

使：

$$
\eta_J\le1-\delta,
$$

則：

$$
\boxed{
\|u_{J+1}(\tau_J)\|_3
\ge
M\sqrt{1-(1-\delta)^2}.
}
$$

所以 crossing 有 order-$M$ 的 immediate-shell carrier。

## Branch DB — Deep-tail bypass

若：

$$
\eta_J\to1,
$$

則：

$$
\beta_J\to0.
$$

也就是：

$$
\boxed{
\text{threshold is already carried mainly by scales deeper than }J+1.
}
$$

---

# 15. 重要 no-go：adjacent crossing 不等於 adjacent source

即使：

$$
\tau_J
\le
\tau_{J+1}
$$

並且 scale index只差：

$$
1,
$$

仍不能推出：

$$
u_{J+1}
\text{ generated }
u_{J+2}.
$$

特別在：

$$
\eta_J\approx1
$$

時，

child threshold 可能已經由遠 deeper tail 支撐。

所以：

$$
\boxed{
\text{adjacent first-passage skeleton}
\neq
\text{adjacent nonlinear cascade}.
}
$$

這是本文第二個核心 no-go。

---

# 16. Edge delay

定義：

$$
\boxed{
\Delta\tau_J(M)
=
\tau_{J+1}(M)-\tau_J(M)
\ge0.
}
$$

以及 parabolically normalized delay：

$$
\boxed{
\Theta_J(M)
=
2^{2J}
\Delta\tau_J(M).
}
$$

對 dyadic Navier–Stokes rescaling：

$$
u^{(m)}(x,t)
=
2^m
u(2^m x,2^{2m}t),
$$

threshold：

$$
M
$$

保持不變，

而 index平移。

因此：

$$
\boxed{
\Theta_J
}
$$

是 dyadic scale-covariant diagnostic。

---

# 17. Delay regime

目前無 theorem 排除：

$$
\Theta_J\to0,
$$

$$
\Theta_J\sim1,
$$

或：

$$
\Theta_J\to\infty.
$$

它們分別對應：

- faster-than-parabolic crossing；
- parabolic-scale crossing；
- slower-than-parabolic crossing。

但：

$$
\sum_J\Delta\tau_J
=
T_\ast-\tau_{J_0}
$$

只控制 unnormalized total delay。

它**不**單獨控制：

$$
\Theta_J.
$$

所以：

$$
\boxed{
\text{finite terminal time}
\not\Rightarrow
\text{parabolic edge timing}.
}
$$

---

# 18. Duhamel representation

對：

$$
s<t<T_\ast,
$$

每個 dyadic block：

$$
u_j(t)
=
e^{\nu(t-s)\Delta}u_j(s)
-
\int_s^t
e^{\nu(t-r)\Delta}
\Delta_j
\mathbb P\nabla\cdot(u\otimes u)(r)
\,dr.
$$

heat semigroup 在：

$$
L^3
$$

上 contractive：

$$
\|e^{\nu(t-s)\Delta}f\|_3
\le
\|f\|_3.
$$

---

# 19. Damped nonlinear tail source

對：

$$
s<t,
$$

定義：

$$
\boxed{
\mathcal N_J(r;t)
=
\left(
\sum_{j>J}
\left\|
e^{\nu(t-r)\Delta}
\Delta_j
\mathbb P\nabla\cdot(u\otimes u)(r)
\right\|_3^2
\right)^{1/2}.
}
$$

由 Duhamel、$L^3$ heat contraction、Minkowski inequality in $\ell^2$：

$$
\boxed{
\mathcal B_J(t)
\le
\mathcal B_J(s)
+
\int_s^t
\mathcal N_J(r;t)\,dr.
}
$$

這裡沒有把 heat flow 當 source。

heat evolution只能 transport / dissipate existing shell burden；

critical tail burden 的正增量必須由 nonlinear Duhamel term支付。

---

# 20. C2.4 — Nonlinear Source Debt Theorem

## Theorem 20.1

令：

$$
s_J
=
\tau_J(M),
$$

$$
t_J
=
\tau_{J+1}(M).
$$

則：

$$
\mathcal B_{J+1}(t_J)
=
M.
$$

定義 first-passage deficit：

$$
\boxed{
d_J(M)
=
M
-
\mathcal B_{J+1}(s_J)
=
M(1-\eta_J).
}
$$

則：

$$
\boxed{
\int_{s_J}^{t_J}
\mathcal N_{J+1}(r;t_J)\,dr
\ge
d_J(M).
}
$$

### Proof

由 Duhamel tail inequality：

$$
M
=
\mathcal B_{J+1}(t_J)
\le
\mathcal B_{J+1}(s_J)
+
\int_{s_J}^{t_J}
\mathcal N_{J+1}(r;t_J)\,dr.
$$

移項即得：

$$
\int_{s_J}^{t_J}
\mathcal N_{J+1}(r;t_J)\,dr
\ge
M-\mathcal B_{J+1}(s_J).
$$

$\square$

---

# 21. Source debt 的意義

若：

$$
\eta_J<1,
$$

則：

$$
d_J>0.
$$

因此：

$$
\boxed{
\text{the deeper-tail threshold cannot be reached by pure heat evolution alone}.
}
$$

必須有真正 Navier–Stokes nonlinear source：

$$
\mathbb P\nabla\cdot(u\otimes u)
$$

在：

$$
[\tau_J,\tau_{J+1}]
$$

上支付至少：

$$
d_J
$$

的 aggregate damped source burden。

這是本文從：

$$
\text{high-frequency presence}
$$

走向：

$$
\text{source traceability}
$$

的第一個 equation-level bridge。

---

# 22. Synchronous branch

若：

$$
\tau_{J+1}
=
\tau_J,
$$

則由 first-passage continuity：

$$
\mathcal B_{J+1}(\tau_J)=M.
$$

所以：

$$
\eta_J=1,
$$

$$
d_J=0,
$$

以及：

$$
\beta_J=0.
$$

此時 deeper tail 與 parent tail 同時 first-cross threshold。

稱：

$$
\boxed{
\textbf{synchronous deep-tail crossing}.
}
$$

這不是 source-free dynamics。

它只表示：

$$
[\tau_J,\tau_{J+1}]
$$

這個 interval collapse 到 zero，

因此此 edge 無法用正時間 Duhamel increment解析來源。

這是新的 escape class。

---

# 23. Sequential source-paid branch

若：

$$
\tau_{J+1}>\tau_J
$$

且：

$$
\eta_J<1,
$$

則：

$$
d_J>0.
$$

稱：

$$
\boxed{
\textbf{sequential source-paid crossing}.
}
$$

其必要條件是：

$$
\boxed{
\int_{\tau_J}^{\tau_{J+1}}
\mathcal N_{J+1}(r;\tau_{J+1})\,dr
\ge
M(1-\eta_J).
}
$$

這是一個真正 source burden certificate。

---

# 24. Source burden 不等於 parent identification

Theorem 20.1 仍不能推出：

$$
\boxed{
\text{which dyadic parent pair generated the debt}.
}
$$

因：

$$
\mathbb P\nabla\cdot(u\otimes u)
$$

包含所有 quadratic interactions。

因此：

$$
\boxed{
\text{source existence}
\neq
\text{source identity}.
}
$$

這是完整 Chain Necessity 尚未完成的核心缺口。

---

# 25. Bony source split

使用 paraproduct decomposition：

$$
u\otimes u
=
T_u u
+
T_u^\ast u
+
R(u,u).
$$

抽象分成：

$$
\mathsf{LH},
\qquad
\mathsf{HL},
\qquad
\mathsf{HH}.
$$

也就是：

- low--high；
- high--low；
- high--high/resonant。

對應：

$$
\mathcal N_J
\le
\mathcal N_J^{LH}
+
\mathcal N_J^{HL}
+
\mathcal N_J^{HH}.
$$

---

# 26. C2.5 — Coarse Source-Class Debt

## Corollary 26.1

在 sequential source-paid edge：

$$
d_J>0,
$$

至少存在一個 source class：

$$
\sigma_J
\in
\{
LH,HL,HH
\}
$$

使：

$$
\boxed{
\int_{\tau_J}^{\tau_{J+1}}
\mathcal N_{J+1}^{\sigma_J}(r;\tau_{J+1})\,dr
\ge
\frac{d_J}{3}.
}
$$

### Proof

由：

$$
\mathcal N_{J+1}
\le
\mathcal N_{J+1}^{LH}
+
\mathcal N_{J+1}^{HL}
+
\mathcal N_{J+1}^{HH},
$$

以及 Theorem 20.1，

三者 time-integrated sum 至少為：

$$
d_J.
$$

所以至少一項不小於：

$$
d_J/3.
$$

$\square$

---

# 27. 目前首次得到的 source typing

因此 sequential edge 已經可以標記：

$$
\boxed{
e_J^{FP}
=
\left(
J,
J+1,
\tau_J,
\tau_{J+1},
\eta_J,
d_J,
\sigma_J
\right).
}
$$

其中：

$$
\sigma_J
$$

至少能 coarse-grain 到：

$$
LH,
\quad
HL,
\quad
HH.
$$

這仍不是：

$$
(p,q)\to k
$$

的 exact triad provenance。

但已經不是純 scalar crossing。

---

# 28. Exact triad provenance gap

要從：

$$
\sigma_J
$$

升級到 exact parent set：

$$
\mathcal P_J
=
\{
(p,q):
p+q=k,
\text{ significant source}
\},
$$

需要：

- frequency-localized lower bounds；
- cancellation control；
- Leray projection geometry；
- possible helical decomposition；
- source persistence across the interval。

因此：

$$
\boxed{
\text{coarse source class}
\not\Rightarrow
\text{exact parent provenance}.
}
$$

此 gap 留給 RFP-03 / RFP-05。

---

# 29. Initial-tail contamination

first-passage source theorem 已經自動處理一個重要問題。

在：

$$
[\tau_J,\tau_{J+1}],
$$

deeper tail初始 stock：

$$
\mathcal B_{J+1}(\tau_J)
$$

被明確扣除。

source debt只計：

$$
M-\mathcal B_{J+1}(\tau_J).
$$

所以：

$$
\boxed{
\text{old high-frequency stock}
}
$$

與：

$$
\boxed{
\text{new nonlinear supply}
}
$$

不被混在一起。

這正是原 X-Guard：

$$
G_{\rm source}
$$

要求的 provenance separation。

---

# 30. Heat-tax refinement

Theorem 20.1 只使用 heat contraction：

$$
\|e^{\nu(t-s)\Delta}f\|_3
\le
\|f\|_3.
$$

對 frequency-localized block其實可使用：

$$
\|e^{\nu(t-s)\Delta}u_j(s)\|_3
\le
Ce^{-c\nu2^{2j}(t-s)}
\|u_j(s)\|_3.
$$

因此可定義 heat-taxed stock：

$$
\boxed{
\mathcal H_J(s,t)
=
\left(
\sum_{j>J}
e^{-2c\nu2^{2j}(t-s)}
\|u_j(s)\|_3^2
\right)^{1/2}.
}
$$

則預期更強 estimate：

$$
\mathcal B_J(t)
\le
C\mathcal H_J(s,t)
+
\int_s^t
\mathcal N_J(r;t)\,dr.
$$

這使 source debt 可進一步扣除 viscous survival。

本文把 sharp constants 與 exact cutoff convention 留給下一版。

---

# 31. Source-profit ratio

對：

$$
d_J>0,
$$

定義：

$$
\boxed{
\Pi_J^{src}
=
\frac{
\int_{\tau_J}^{\tau_{J+1}}
\mathcal N_{J+1}(r;\tau_{J+1})\,dr
}{
d_J
}.
}
$$

Theorem 20.1 給出：

$$
\boxed{
\Pi_J^{src}\ge1.
}
$$

但：

$$
\Pi_J^{src}\gg1
$$

可能代表：

- strong source with cancellation；
- source injected into many deeper shells；
- inefficient transfer；
- repeated generation and dissipation。

所以：

$$
\boxed{
\text{large source budget}
\neq
\text{efficient ancestry}.
}
$$

---

# 32. First-passage edge state

本文建議 RFP edge state 第一版升級為：

$$
\boxed{
\Xi_J(M)
=
\left(
\tau_J,
\tau_{J+1},
\Theta_J,
\eta_J,
\beta_J,
d_J,
\Pi_J^{src},
\sigma_J
\right).
}
$$

它保存：

- crossing time；
- normalized delay；
- immediate-shell carrier fraction；
- deep-tail bypass fraction；
- nonlinear source debt；
- coarse source type。

這是從 C3 scalar state 到 formation edge state 的第一次具體升級。

---

# 33. Threshold family

單一：

$$
M
$$

仍可能隱藏 amplitude structure。

因此可同時考慮：

$$
M_1<M_2<\cdots.
$$

得到二參數 first-passage lattice：

$$
\boxed{
\tau_J(M).
}
$$

它滿足：

$$
M_1\le M_2
\Longrightarrow
\tau_J(M_1)
\le
\tau_J(M_2),
$$

以及：

$$
J_1\le J_2
\Longrightarrow
\tau_{J_1}(M)
\le
\tau_{J_2}(M).
$$

所以：

$$
\boxed{
(J,M)
\mapsto\tau_J(M)
}
$$

形成一個 monotone UV first-passage surface。

---

# 34. Amplitude–scale partial order

定義：

$$
(J,M)\preceq(K,N)
$$

若：

$$
J\le K,
\qquad
M\le N.
$$

則：

$$
\boxed{
\tau_J(M)
\le
\tau_K(N).
}
$$

這提供一個不依賴人工選取 subsequence 的 canonical partial order。

future ancestry 可以嘗試從這張 first-passage surface 選出：

$$
\text{source-compatible paths}.
$$

---

# 35. Threshold robustness

若完整 Chain Necessity 只在某個特製 threshold：

$$
M
$$

下成立，

可能只是 instrumentation artifact。

因此真正 robust result 應研究：

$$
M\in[M_-,M_+]
$$

的 family，

並尋找：

$$
\boxed{
\text{threshold-uniform source / timing / carrier estimates}.
}
$$

這是未來 Finite Obstruction 所需的 uniformity。

---

# 36. Spatial core gap

目前：

$$
\mathcal B_J(t)
$$

是 global frequency quantity。

它沒有指定：

$$
\Omega_J.
$$

所以目前只證：

$$
\boxed{
\text{frequency ancestry skeleton}.
}
$$

尚未證：

$$
\boxed{
\text{spacetime ancestry tube}.
}
$$

要接到 RFP-01 state：

$$
X_J
=
(t_J,\lambda_J,\Omega_J,\ldots),
$$

還必須加入：

- critical norm concentration；
- local smoothing contrapositive；
- pressure-compatible localization；
- adjoint ancestry tube。

---

# 37. Barker–Prange interface

現有 localized smoothing / concentration theory 在特定 blow-up regimes 中提供：

$$
R(t)
\sim
\sqrt{T_\ast-t}
$$

附近的 critical concentration information。

這提供可能的 bridge：

$$
(\tau_J,J)
\Longrightarrow
\Omega_J.
$$

但本文不把 Type-I 或其他附加 hypotheses 下的 concentration theorem 偷換成 unrestricted Chain Necessity。

所以：

$$
\boxed{
\text{global first-passage skeleton}
+
\text{localized concentration theorem}
}
$$

目前只是下一步 interface，不是已完成 theorem。

---

# 38. 2026 Critical-Ledger work 的關係

2026 年 Runlong Yu 的 finite-scale critical-ledger work 考慮 suitable weak solutions 的 admissible nested parabolic-window chain：

$$
Q_{k+1}\subset Q_k,
$$

並證明 persistent scale-critical badness 在有限多尺度存活時，必支付：

$$
\text{untaxed critical supply}
$$

或：

$$
\text{localization leakage}.
$$

其 theorem deliberately finite-scale，並明確不宣稱 global regularity。

這和 NS-RFP 有高度結構相似性，但 logical entry point 不同。

該工作從：

$$
\boxed{
\text{an admissible parabolic chain is given}
}
$$

開始。

NS-RFP 02 則處理：

$$
\boxed{
\text{can a canonical scale-time skeleton be forced by blow-up necessity itself?}
}
$$

本文答案是：

$$
\boxed{
\textbf{YES at global-frequency first-passage level}.
}
$$

但：

$$
\boxed{
\textbf{NOT YET at spatially localized source-resolved ancestry level}.
}
$$

兩條路徑因此互補。

---

# 39. Yu ledger 與 source debt 的對接

Yu 的 finite-scale language區分：

$$
\text{supply},
\quad
\text{tax},
\quad
\text{leakage}.
$$

本文 first-passage identity則自然產生：

$$
\text{old stock}
=
\mathcal B_{J+1}(\tau_J),
$$

$$
\text{required new burden}
=
d_J,
$$

$$
\text{nonlinear supply}
=
\int\mathcal N_{J+1}.
$$

因此可以預期未來建立 dictionary：

$$
\boxed{
\text{first-passage debt}
\leftrightarrow
\text{finite-scale untaxed supply ledger}.
}
$$

但目前兩者使用不同 state space：

- 本文：global frequency shell burden；
- Yu：localized CKN parabolic-window coordinates。

正式 equivalence 尚未證。

---

# 40. Tao quantitative interface

Tao 的 quantitative critical-$L^3$ theory 說明：

若：

$$
T_\ast
$$

為 finite blow-up time，

critical $L^3$ norm 不只 qualitative 發散，還必沿某些 times 具有 quantitative lower growth。

這可能把：

$$
M
$$

從 fixed threshold family 升級成：

$$
M=M(t)
$$

或：

$$
M_J\to\infty.
$$

若能建立：

$$
\tau_J(M_J)\to T_\ast
$$

的 quantitative relation，

即可把 source debt：

$$
d_J
$$

升級成 asymptotic lower bound。

本文不完成此 quantitative upgrade。

---

# 41. Stronger moving-threshold problem

考慮：

$$
M_J\uparrow\infty.
$$

定義：

$$
\tau_J(M_J).
$$

問題：

是否存在 scale law：

$$
M_J
$$

使：

$$
\tau_J(M_J)<T_\ast
$$

對所有充分大 $J$，

且仍有：

$$
\tau_J(M_J)\uparrow T_\ast?
$$

fixed-$M$ theorem不能直接推出 arbitrary：

$$
M_J\to\infty.
$$

這是一個新的 quantitative Chain-Necessity obligation。

---

# 42. Distributed-shell escape

即使：

$$
\mathcal B_J\to\infty,
$$

也可能：

$$
\sup_{j>J}
\|u_j\|_3
$$

保持相對小，

而由很多 shells共同支撐：

$$
\mathcal B_J.
$$

所以：

$$
\boxed{
\text{UV burden divergence}
}
$$

具有兩種基本 geometry：

$$
\boxed{
\text{single/few-shell concentration}
\quad\vee\quad
\text{many-shell distribution}.
}
$$

本文 carrier/bypass ratio只開始區分 immediate shell 與 deeper tail，

尚未完成 deeper tail 的 entropy / occupancy census。

---

# 43. Shell entropy candidate

令：

$$
w_j(t;J)
=
\frac{
\|u_j(t)\|_3^2
}{
\mathcal B_J(t)^2
},
\qquad
j>J.
$$

則：

$$
\sum_{j>J}w_j=1.
$$

可定義：

$$
\boxed{
\mathsf H_J
=
-\sum_{j>J}
w_j\log w_j.
}
$$

它可以區分：

- low entropy：few-shell carrier；
- high entropy：distributed-shell burden。

但：

$$
\mathsf H_J
$$

目前只是 diagnostic。

尚未證它有 regularity 或 singularity criterion 意義。

---

# 44. Source entropy

同理 nonlinear debt 可能由：

$$
LH,
\quad
HL,
\quad
HH
$$

共同支付。

可將各 class integrated source burden正規化後形成：

$$
\mathsf H_J^{src}.
$$

這將來可測：

$$
\boxed{
\text{source concentration}
\quad\text{vs}\quad
\text{source diversification}.
}
$$

但任何 entropy quantity都不得取代 exact PDE source identity。

---

# 45. RFP-02 到目前為止真正完成了什麼？

此前：

$$
\operatorname{Blowup}
\Longrightarrow
\text{UV tail unbounded}.
$$

本文提升成：

$$
\boxed{
\operatorname{Blowup}
\Longrightarrow
\mathfrak S_M
=
\{(\tau_J(M),J)\}_{J\to\infty},
}
$$

其中：

$$
\tau_J\le\tau_{J+1},
$$

$$
\tau_J\uparrow T_\ast,
$$

且：

$$
J\to J+1.
$$

再進一步：

$$
\boxed{
d_J>0
\Longrightarrow
\text{positive nonlinear Duhamel source debt}.
}
$$

以及：

$$
\boxed{
\text{at least one of }LH,HL,HH
\text{ pays a fixed fraction of that debt}.
}
$$

---

# 46. 仍沒有證明什麼？

本文沒有證：

$$
u_{J+1}
\to
u_{J+2}
$$

是 direct parent-child generation。

沒有證：

$$
\Omega_{J+1}\subset\Omega_J.
$$

沒有證：

$$
\Theta_J
$$

bounded。

沒有證：

$$
d_J
$$

uniformly positive。

沒有證 synchronous branch 不可能。

沒有證 deep-tail bypass 不可能。

沒有證 finite guard family阻斷所有 skeletons。

因此：

$$
\boxed{
\text{First-Passage Skeleton}
\neq
\text{Full Formation Ancestry}.
}
$$

---

# 47. Partial Chain Necessity theorem

可將本文成果壓成：

## Theorem 47.1 — Partial Chain Necessity

若 finite-time singularity 存在，

則對每個 fixed critical threshold：

$$
M>0
$$

及所有充分大 dyadic scales $J$，

存在 canonical first-passage states：

$$
Y_J(M)
=
\left(
\tau_J(M),
J,
\mathcal B_J=M,
\eta_J,
\beta_J
\right)
$$

使：

$$
\tau_J(M)
\uparrow T_\ast,
$$

$$
J\to J+1,
$$

且每個 edge：

$$
Y_J\to Y_{J+1}
$$

滿足以下之一：

### PF-A — Sequential source-paid

$$
d_J>0
$$

且：

$$
\int_{\tau_J}^{\tau_{J+1}}
\mathcal N_{J+1}
\ge
d_J.
$$

### PF-B — Synchronous/deep-tail bypass

$$
d_J=0
$$

而 deeper tail 已在同一 first-passage time 支撐 threshold。

所以：

$$
\boxed{
\operatorname{Blowup}
\Longrightarrow
\text{an infinite adjacent-scale first-passage skeleton with a source-paid / bypass dichotomy at every edge}.
}
$$

$\square$

---

# 48. 為何這仍不是完整 CN？

完整 Chain Necessity 要求：

$$
\Gamma_\infty
\in
\mathfrak A_{NS}^{\infty}
$$

每一 edge 都有：

$$
\mathsf{Src},
\quad
\mathsf{Prov},
\quad
\mathsf{Guard}.
$$

Theorem 47.1 的 PF-A 有 aggregate nonlinear source burden，

但 PF-B 仍可繞過 positive interval debt。

而 PF-A 也只識別 coarse source class，

尚未識別 exact parent interaction。

因此完整 CN 被壓縮成兩個 sharper subproblems：

$$
\boxed{
\textbf{Synchronous-Bypass Resolution}
}
$$

與：

$$
\boxed{
\textbf{Exact Parent Resolution}.
}
$$

---

# 49. New Obligation SB — Synchronous-Bypass Resolution

若 infinitely many：

$$
J
$$

滿足：

$$
d_J\to0
$$

或甚至：

$$
d_J=0,
$$

則 deeper critical burden 幾乎無需在：

$$
[\tau_J,\tau_{J+1}]
$$

新生成。

可能解釋：

1. pre-existing deep-tail reservoir；
2. many-shell simultaneous buildup；
3. nonlocal scale jump；
4. threshold artifact；
5. true fast cascade。

需要證明這些 alternatives 中哪些是 N–S realizable。

---

# 50. New Obligation PR — Exact Parent Resolution

對 PF-A，

已知：

$$
\int
\mathcal N_{J+1}
\ge
d_J.
$$

下一步需要找：

$$
\mathcal P_J
$$

使：

$$
\boxed{
\mathcal P_J
\to
\text{child debt}
}
$$

具有 quantitative lower bound。

候選 parent classes：

$$
\text{local triad},
$$

$$
\text{high--low},
$$

$$
\text{high--high},
$$

$$
\text{nonlocal pressure-mediated},
$$

$$
\text{vorticity/strain channel}.
$$

這是 RFP-03 / RFP-05 的核心。

---

# 51. 下一篇應如何改 roadmap？

原 roadmap 的 RFP-03 是：

> Local Operator Ancestry Norms and Projection–Cutoff Commutators.

本文後建議保留，但加上一個更精確 subtitle：

$$
\boxed{
\textbf{NS-RFP 03 — Exact Parent Resolution through Local Operator Ancestry Norms}
}
$$

並要求它直接處理：

$$
\text{PF-A parent resolution}
$$

與：

$$
\text{PF-B synchronous bypass}.
$$

---

# 52. 與 C3-O 的重新連接

C3-O 證明：

$$
\text{balance closeness}
\not\Rightarrow
\text{operator closeness}.
$$

RFP-02 現在給出：

$$
\text{tail crossing}
\not\Rightarrow
\text{parent identification}.
$$

兩者具有同一 information-loss pattern：

$$
\boxed{
\text{observable event}
\neq
\text{dynamical provenance}.
}
$$

因此新系列真正需要保存的是：

$$
\boxed{
\text{event}
+
\text{source debt}
+
\text{parent identity}
+
\text{transition history}.
}
$$

---

# 53. X-Integration 更新

RFP-02 可以把 X-formation judgment升級為：

$$
\frac{
\Gamma\vdash
Y_J
\to
Y_{J+1}
\qquad
d_J>0
\qquad
\Gamma\vdash
\mathsf{Debt}_{NS}(J)\ge d_J
}{
\Gamma\vdash
e_J^{FP}
:
\mathsf{source\mbox{-}paid\ candidate}
}.
$$

但仍不能推出：

$$
\Gamma\vdash
e_J^{FP}
:
\mathsf{fully\ source\mbox{-}resolved}.
$$

除非再有：

$$
G_{\rm parent}
=
\mathrm{PASS}.
$$

新增 guard：

$$
\boxed{
G_{\rm PARENT}.
}
$$

---

# 54. New Guard — $G_{\rm SYNC}$

同步 edge：

$$
d_J=0
$$

不能被當成：

$$
\text{no dynamics happened}.
$$

新增：

$$
\boxed{
G_{\rm SYNC}:
\quad
\text{zero first-passage interval debt is not zero historical source}.
}
$$

它和 C3-O 的：

$$
\text{zero pairing}
\neq
\text{zero operator}
$$

具有相同 no-go 結構。

---

# 55. New Guard — $G_{\rm STOCK}$

任何 child burden必須拆：

$$
\boxed{
\text{old stock}
+
\text{new supply}.
}
$$

不得把：

$$
\mathcal B_{J+1}(\tau_J)
$$

誤記成：

$$
[\tau_J,\tau_{J+1}]
$$

內生成的 source。

新增：

$$
\boxed{
G_{\rm STOCK}.
}
$$

---

# 56. New Guard — $G_{\rm SHELL}$

若：

$$
\eta_J\to1,
$$

不得把 scale label：

$$
J+1
$$

誤認為 actual carrier scale。

新增：

$$
\boxed{
G_{\rm SHELL}:
\quad
\text{scale crossing label is not carrier identification}.
}
$$

---

# 57. RFP Guard Library v1

因此：

$$
\mathcal G_{NS}^{(1)}
=
\mathcal G_{NS}^{(0)}
\cup
\{
G_{\rm PARENT},
G_{\rm SYNC},
G_{\rm STOCK},
G_{\rm SHELL}
\}.
$$

RFP-02 不只產生 theorem。

它還新增四個 formation-specific no-go guards。

---

# 58. Formal status

$$
\boxed{
\begin{aligned}
\text{critical shell burden definition}
&:\ \mathrm{DEFINED},\\
\text{shell-burden UV necessity}
&:\ \mathrm{PROVED},\\
\text{compact-window high-tail vanishing}
&:\ \mathrm{PROVED},\\
\text{first-passage time monotonicity}
&:\ \mathrm{PROVED},\\
\tau_J(M)\uparrow T_\ast
&:\ \mathrm{PROVED},\\
\text{adjacent-scale first-passage skeleton}
&:\ \mathrm{PROVED},\\
\text{shell carrier/bypass identity}
&:\ \mathrm{PROVED},\\
\text{nonlinear source debt}
&:\ \mathrm{PROVED},\\
\text{coarse }LH/HL/HH\text{ source-class debt}
&:\ \mathrm{PROVED},\\
\text{parabolic normalized delay boundedness}
&:\ \mathrm{OPEN},\\
\text{synchronous-bypass resolution}
&:\ \mathrm{OPEN},\\
\text{exact parent provenance}
&:\ \mathrm{OPEN},\\
\text{spatial-core ancestry}
&:\ \mathrm{OPEN},\\
\text{full Chain Necessity}
&:\ \mathrm{OPEN},\\
\text{Finite Obstruction}
&:\ \mathrm{OPEN},\\
\text{Navier--Stokes regularity}
&:\ \mathrm{NOT\ PROVED}.
\end{aligned}
}
$$

---

# 59. 結論

此前的 strongest internal reduction 是：

$$
\boxed{
\operatorname{Blowup}(T_\ast)
\Longrightarrow
\text{critical UV escape}.
}
$$

RFP-02 將它第一次升級為：

$$
\boxed{
\operatorname{Blowup}(T_\ast)
\Longrightarrow
\text{canonical adjacent-scale UV first-passage skeleton}.
}
$$

對每個 fixed critical threshold：

$$
M>0,
$$

存在：

$$
\tau_J(M)\uparrow T_\ast
$$

且：

$$
J\to J+1.
$$

每一 crossing 再 exact 分解成：

$$
\boxed{
\text{immediate-shell carrier}
+
\text{deeper-tail bypass}.
}
$$

更重要的是，

每一個非同步／有 deficit 的 edge 都必須支付：

$$
\boxed{
\text{positive nonlinear Duhamel source debt}.
}
$$

所以：

$$
\boxed{
\text{high-frequency appearance}
}
$$

不再只是 endpoint fact。

它開始具有：

$$
\boxed{
\text{time order}
+
\text{scale order}
+
\text{source burden}.
}
$$

完整 Chain Necessity 尚差：

$$
\boxed{
\text{Synchronous-Bypass Resolution}
+
\text{Exact Parent Resolution}
+
\text{Spatial-Core Attachment}.
}
$$

下一輪正式進入：

$$
\boxed{
\textbf{NS-RFP 03 — Exact Parent Resolution through Local Operator Ancestry Norms}
}
$$

---

# References

1. L. Escauriaza, G. Seregin, V. Šverák, *$L_{3,\infty}$-solutions of Navier–Stokes equations and backward uniqueness*, Russian Mathematical Surveys 58 (2003), 211–250.
2. I. Gallagher, G. S. Koch, F. Planchon, *Blow-up of critical Besov norms at a potential Navier–Stokes singularity*, Communications in Mathematical Physics 343 (2016), 39–82; arXiv:1407.4156.
3. T. Tao, *Quantitative bounds for critically bounded solutions to the Navier–Stokes equations*, arXiv:1908.04958.
4. T. Barker, C. Prange, *Localized smoothing for the Navier–Stokes equations and concentration of critical norms near singularities*, Archive for Rational Mechanics and Analysis 236 (2020), 1487–1541; arXiv:1812.09115.
5. T. Barker, C. Prange, *Quantitative regularity for the Navier–Stokes equations via spatial concentration*, Communications in Mathematical Physics 385 (2021), 717–792; arXiv:2003.06717.
6. W. Tan, *The localized characterization for the singularity formation in the Navier–Stokes equations*, arXiv:2107.04597.
7. T. Barker, H. Popkin, *Quantitative estimates for the forced Navier–Stokes equations and applications*, arXiv:2602.09951 (2026).
8. R. Yu, *Critical Ledgers and Scale-Defect Cascades for Navier–Stokes*, arXiv:2606.13887 (2026).

# Internal dependencies

- `NS_RFP_01_SingularityFormationAncestry_FiniteObstruction_v0.1.md`
- `NS_ETN_XIntegration_Multiscale_NonCollapse_v0.1.md`
- `NS_C3O_AdjointCore_BalanceDynamicsSeparation_v0.2.md`
- `True ETN / 無限維張力場`
- `X_Integral_Unified_Program_v0.2.md`

# Next

$$
\boxed{
\textbf{NS-RFP 03 — Exact Parent Resolution through Local Operator Ancestry Norms}
}
$$
