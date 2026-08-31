---
title: "Navier–Stokes Reverse Formation Program 05：Witness Persistence、Finite Branching、Survivor Recursion 與 Infinite Ancestry Path Extraction"
short_title: "NS-RFP 05"
version: "v0.1"
date: "2026-08-14"
author: "Neo.K / EveMissLab"
language: "zh-TW"
status: "Theorem-style quantifier-closure architecture / persistence reduction"
epistemic_status: "Proves a finite-branching path-extraction theorem for thresholded RFP witness graphs, gives an exact backward survivor recursion and finite-horizon obstruction certificate, and separates persistent infinite ancestry from bottleneck-collapse escape. The graph theorem is exact once the node and compatibility certificates are supplied. The PDE bridge score needed for full provenance compatibility remains open. This paper does NOT prove full Chain Necessity, Finite Obstruction for all Navier–Stokes ancestries, or Navier–Stokes regularity."
canonical_source: "UTF-8 Markdown"
---

# Navier–Stokes Reverse Formation Program 05

# Witness Persistence、Finite Branching、Survivor Recursion 與 Infinite Ancestry Path Extraction

## 0. 本文定位

NS-RFP 02 建立：

$$
\boxed{
\text{first-passage levels}
}
$$

與：

$$
\boxed{
\text{nonlinear source debt}.
}
$$

NS-RFP 03 建立：

$$
\boxed{
(k;p,q)
}
$$

exact signed parent-output ledger。

NS-RFP 04 再建立：

$$
\boxed{
(a;k;p,q)
}
$$

spacetime soft-tube ledger，

以及 quantitative parent tightness criterion：

$$
\boxed{
1-C_J^{par}(L)
\le
C2^{-L}\mathfrak V_J.
}
$$

因此：

$$
\sup_J\mathfrak V_J<\infty
$$

可將 subsequential parent tightness升級成 quantitative uniform parent tightness。

但 RFP-04 明確留下：

$$
\boxed{
\textbf{Witness Persistence / Chain Stitching}.
}
$$

也就是：

$$
\boxed{
\forall J\;\exists v_J
}
$$

不能被偷換成：

$$
\boxed{
\exists(v_J)_{J\ge J_0}
\;\forall J:
v_J\text{ compatible with }v_{J+1}.
}
$$

本文專門處理這個全域量詞缺口。

---

# 1. 核心 no-go：逐層存在不等於持續存在

即使每個 first-passage level：

$$
J
$$

都有一個 good spacetime witness：

$$
v_J,
$$

也可能 level $J$ 的所有 witnesses都只延伸有限深度，

而 level $J+1$ 使用的是另一批互不相容的 witnesses。

所以一般而言：

$$
\boxed{
\forall J\;\exists v_J
\quad\not\Rightarrow\quad
\exists(v_J)_J\;\forall J.
}
$$

更精確地，

逐層存在：

$$
v_J\in V_J
$$

不推出存在：

$$
v_J\sim_Jv_{J+1}
$$

的 infinite compatible sequence。

這不是 Navier--Stokes 特有問題，

而是 finite-horizon information升級成 infinite path時的量詞問題。

---

# 2. RFP-04 local-source ledger

RFP-04 定義：

$$
\Lambda^{loc,(J)}_{a;k;p,q}
=
-
\int_{s_J}^{t_J}
\left\langle
\mathcal T_k
\left(
\chi_{J,a}
u_p\otimes u_q
\right),
\varphi_{J,k}
\right\rangle dr,
$$

其中：

$$
\mathcal T_k
=
\Delta_k\mathbb P\nabla\cdot.
$$

因：

$$
\sum_a\chi_{J,a}=1,
$$

有一個本文首先明示的 exact refinement。

---

# 3. C5.1 — Exact Local-Source Refinement

## Theorem 3.1

對每個：

$$
k,p,q,
$$

有：

$$
\boxed{
\sum_a
\Lambda^{loc,(J)}_{a;k;p,q}
=
\Lambda^{(J)}_{k;p,q}.
}
$$

因此：

$$
\boxed{
\sum_{a,k,p,q}
\Lambda^{loc,(J)}_{a;k;p,q}
=
R_J.
}
$$

### Proof

由 linearity：

$$
\sum_a
\mathcal T_k
\left(
\chi_{J,a}
F_{p,q}
\right)
=
\mathcal T_k
\left(
\left(
\sum_a\chi_{J,a}
\right)
F_{p,q}
\right)
=
\mathcal T_kF_{p,q}.
$$

代回 dual pairing與 time integral即得。$\square$

---

# 4. Local positive / negative ledger

定義：

$$
\boxed{
P_J^{loc}
=
\sum_{a,k,p,q}
[
\Lambda^{loc,(J)}_{a;k;p,q}
]_+,
}
$$

以及：

$$
\boxed{
N_J^{loc}
=
\sum_{a,k,p,q}
[
\Lambda^{loc,(J)}_{a;k;p,q}
]_-.
}
$$

則：

$$
\boxed{
P_J^{loc}-N_J^{loc}=R_J>0.
}
$$

所以：

$$
P_J^{loc}>0.
$$

---

# 5. Positive local-source probability

對每個 positive local-source entry：

$$
v
=
(a;k;p,q),
$$

定義：

$$
\boxed{
\pi_J(v)
=
\frac{
[
\Lambda^{loc,(J)}_v
]_+
}{
P_J^{loc}
}.
}
$$

則：

$$
\boxed{
\pi_J(v)\ge0,
\qquad
\sum_v\pi_J(v)=1.
}
$$

因此每個 PF-A edge自然帶一個 countable positive witness probability ledger。

注意：

$$
\pi_J
$$

不是 stochastic dynamics。

它只是 gross positive local-source activity的 normalized bookkeeping measure。

---

# 6. Node strength

稱：

$$
\boxed{
\sigma_J(v)
=
\pi_J(v)
}
$$

為 witness node strength。

若：

$$
\sigma_J(v)\ge\theta,
$$

則：

$$
[
\Lambda^{loc,(J)}_v
]_+
\ge
\theta P_J^{loc}
\ge
\theta R_J.
$$

所以任何 fixed positive gross share自動也是 fixed positive net-debt share。

---

# 7. Thresholded witness set

對：

$$
0<\theta\le1,
$$

定義：

$$
\boxed{
\mathcal W_J(\theta)
=
\left\{
v:
\sigma_J(v)\ge\theta
\right\}.
}
$$

---

# 8. C5.2 — Uniform Finite-Level Bound

## Theorem 8.1

對所有：

$$
J,
$$

有：

$$
\boxed{
|\mathcal W_J(\theta)|
\le
\left\lfloor
\frac1\theta
\right\rfloor.
}
$$

### Proof

若：

$$
m
=
|\mathcal W_J(\theta)|,
$$

則：

$$
1
=
\sum_v\pi_J(v)
\ge
m\theta.
$$

故：

$$
m\le\theta^{-1}.
$$

$\square$

---

# 9. 重要意義：finite branching 不需 uniform cancellation gap

RFP-04 的 tube cancellation ratio可以很接近：

$$
1.
$$

但只要我們使用 normalized positive local-source probability：

$$
\pi_J,
$$

任何 fixed node threshold：

$$
\theta>0
$$

都自動給：

$$
\boxed{
\text{uniform finite number of strong nodes per level}.
}
$$

所以 graph compactness所需的 finite branching可以和 cancellation magnitude分離。

---

# 10. Maximal witness atom

定義：

$$
\boxed{
\mathfrak a_J
=
\sup_v
\pi_J(v).
}
$$

因：

$$
\pi_J
$$

是 countable summable positive sequence，

且總和為：

$$
1,
$$

supremum由某個 entry attained。

所以：

$$
\boxed{
0<\mathfrak a_J\le1.
}
$$

---

# 11. Effective local multiplicity

定義 inverse participation quantity：

$$
\boxed{
\mathfrak M_J^{eff}
=
\left(
\sum_v
\pi_J(v)^2
\right)^{-1}.
}
$$

則：

$$
\mathfrak M_J^{eff}\ge1.
$$

---

# 12. C5.3 — Atomization / Multiplicity Debt

## Theorem 12.1

有：

$$
\boxed{
\mathfrak M_J^{eff}
\ge
\frac1{\mathfrak a_J}.
}
$$

因此若：

$$
\mathfrak a_J\to0,
$$

則：

$$
\boxed{
\mathfrak M_J^{eff}\to\infty.
}
$$

### Proof

因：

$$
\pi_J(v)^2
\le
\mathfrak a_J\pi_J(v),
$$

故：

$$
\sum_v\pi_J(v)^2
\le
\mathfrak a_J
\sum_v\pi_J(v)
=
\mathfrak a_J.
$$

取倒數即得。$\square$

---

# 13. Witness atomization escape

若沿某 subsequence：

$$
\boxed{
\mathfrak a_J\to0,
}
$$

稱：

$$
\boxed{
\textbf{local witness atomization escape}.
}
$$

其意義是：

gross positive local-source activity無法由任何 fixed-share spacetime parent witness承載。

而 Theorem 12.1 告訴我們：

$$
\boxed{
\text{atomization}
\Longrightarrow
\text{effective multiplicity divergence}.
}
$$

所以這不是免費 escape。

---

# 14. Time seam

first-passage construction給：

$$
s_J
=
\tau_J,
$$

$$
t_J
=
\tau_{J+1}.
$$

因此相鄰 PF-A edges天然有：

$$
\boxed{
t_J
=
s_{J+1}.
}
$$

所以 persistence graph的 time ordering不是額外假設。

真正需要證的是：

$$
\boxed{
\text{frequency/source/spatial compatibility across the shared seam}.
}
$$

---

# 15. Frequency-link predicate

若：

$$
v=(a;k;p,q)
\in\mathcal W_J,
$$

以及：

$$
w=(a';k';p',q')
\in\mathcal W_{J+1},
$$

定義 strongest first-generation frequency link：

$$
\boxed{
\mathfrak f_J(v,w)
=
\mathbf 1_{
\{
p',q'
\}
\ni k
}.
}
$$

也就是前一 edge 的 output shell：

$$
k
$$

必須成為下一 edge 的一個 exact dyadic parent。

這是 strong compatibility。

未來可研究 bounded-shell bridge版本，

但本文不把：

$$
|k-p'|=O(1)
$$

自動當作 exact parent identity。

---

# 16. Geometric tube seam

在 shared time：

$$
t_J=s_{J+1},
$$

前一 tube：

$$
a
$$

的 terminal cutoff為：

$$
\chi_{J,a}(t_J).
$$

下一 edge 的 backward tube：

$$
a'
$$

在同一時間也有：

$$
\chi_{J+1,a'}(t_J).
$$

定義 normalized geometric overlap：

$$
\boxed{
\mathfrak o_J(a,a')
=
\frac{
\int
\chi_{J,a}(t_J,x)
\chi_{J+1,a'}(t_J,x)
\,dx
}{
\int
\chi_{J,a}(t_J,x)\,dx
}.
}
$$

terminal cells compactly supported，所以 denominator finite and positive。

---

# 17. C5.4 — Seam Partition Identity

## Theorem 17.1

對 fixed：

$$
J,a,
$$

有：

$$
\boxed{
\mathfrak o_J(a,a')\ge0,
}
$$

以及：

$$
\boxed{
\sum_{a'}
\mathfrak o_J(a,a')
=
1.
}
$$

### Proof

nonnegativity來自：

$$
\chi\ge0.
$$

又因下一 edge 的 adjoint partition滿足：

$$
\sum_{a'}
\chi_{J+1,a'}(t_J,x)=1,
$$

所以：

$$
\begin{aligned}
\sum_{a'}
\mathfrak o_J(a,a')
&=
\frac{
\int
\chi_{J,a}(t_J,x)
\sum_{a'}
\chi_{J+1,a'}(t_J,x)
dx
}{
\int\chi_{J,a}(t_J,x)dx
}
\\
&=
1.
\end{aligned}
$$

$\square$

---

# 18. C5.5 — Effective Spatial Fan-Out Bound

## Theorem 18.1

固定：

$$
0<\gamma\le1.
$$

令：

$$
\mathcal A_{J+1}(a;\gamma)
=
\left\{
a':
\mathfrak o_J(a,a')\ge\gamma
\right\}.
$$

則：

$$
\boxed{
|
\mathcal A_{J+1}(a;\gamma)
|
\le
\left\lfloor
\frac1\gamma
\right\rfloor.
}
$$

### Proof

若有：

$$
m
$$

個 overlap至少：

$$
\gamma,
$$

則由 Theorem 17.1：

$$
1
=
\sum_{a'}\mathfrak o_J(a,a')
\ge
m\gamma.
$$

$\square$

---

# 19. Soft tails 不等於 infinite effective branching

adjoint cutoff earlier times具有 noncompact tails。

但 Theorem 18.1 表明：

對任何 fixed positive overlap threshold：

$$
\gamma>0,
$$

一條 tube只能有有限個：

$$
\gamma
$$

-significant child tubes。

因此：

$$
\boxed{
\text{soft spatial tails}
\neq
\text{infinite effective seam branching at fixed positive share}.
}
$$

---

# 20. 為何 frequency link + tube overlap 還不夠？

即使：

$$
\mathfrak f_J(v,w)=1
$$

以及：

$$
\mathfrak o_J(a,a')>0,
$$

仍只表示：

- frequency label可以接；
- spacetime tubes在 seam幾何相接。

它還沒有證明：

> 前一 witness真正生成的新 output stock在下一 interval中支付了 child parent source的一部分。

所以需要第三個 layer：

$$
\boxed{
\textbf{inter-edge PDE bridge certificate}.
}
$$

---

# 21. Bridge score placeholder

本文定義一個 typed quantity：

$$
\boxed{
\mathfrak b_J(v,w)
\in[0,1].
}
$$

其語義要求是：

$$
\mathfrak b_J(v,w)>0
$$

只能在已有 equation-level certificate證明：

前一 edge witness-associated output contribution能被追蹤到下一 edge 的 selected parent source時成立。

目前：

$$
\mathfrak b_J
$$

的 universal lower bound與完整 construction尚未證明。

它是下一篇的 PDE-facing obligation。

---

# 22. Stock compatibility 與 provenance compatibility

定義 stock-level score：

$$
\boxed{
\mathfrak c_J^{stock}(v,w)
=
\mathfrak f_J(v,w)
\mathfrak o_J(a,a').
}
$$

再定義 full provenance score：

$$
\boxed{
\mathfrak c_J^{prov}(v,w)
=
\mathfrak c_J^{stock}(v,w)
\mathfrak b_J(v,w).
}
$$

因此：

$$
0\le
\mathfrak c_J^{prov}
\le
\mathfrak c_J^{stock}
\le1.
$$

---

# 23. Hard guard：stock continuity 不等於 source provenance

$$
\boxed{
G_{\rm BRIDGE}:
\quad
\mathfrak c_J^{stock}>0
\not\Rightarrow
\mathfrak c_J^{prov}>0.
}
$$

也就是：

$$
\boxed{
\text{same shell}
+
\text{same spatial seam}
}
$$

仍不能替代真正的 equation-level source bridge。

---

# 24. Layered witness graph

固定一個 infinite PF-A level set：

$$
J_0,
J_0+1,
J_0+2,\ldots.
$$

定義 vertices：

$$
\boxed{
V
=
\bigsqcup_{J\ge J_0}
V_J,
}
$$

其中：

$$
V_J
=
\left\{
v:
\pi_J(v)>0
\right\}.
$$

若使用 provenance graph，

edge：

$$
v\to w
$$

存在當且僅當：

$$
\boxed{
\mathfrak c_J^{prov}(v,w)>0.
}
$$

thresholded graph則要求 fixed positive node與edge floors。

---

# 25. Thresholded ancestry graph

固定：

$$
0<\theta\le1,
\qquad
0<\gamma\le1.
$$

定義：

$$
\boxed{
V_J^{\theta}
=
\left\{
v:
\pi_J(v)\ge\theta
\right\}.
}
$$

以及：

$$
\boxed{
E_J^{\theta,\gamma}
=
\left\{
(v,w):
v\in V_J^\theta,
\quad
w\in V_{J+1}^\theta,
\quad
\mathfrak c_J^{prov}(v,w)\ge\gamma
\right\}.
}
$$

---

# 26. C5.6 — Uniform Finite Branching

## Theorem 26.1

thresholded provenance graph：

$$
\mathcal G^{\theta,\gamma}
$$

每一 level皆滿足：

$$
\boxed{
|V_J^\theta|
\le
\left\lfloor
\frac1\theta
\right\rfloor.
}
$$

因此每一 vertex的 out-degree滿足：

$$
\boxed{
\deg^+(v)
\le
\left\lfloor
\frac1\theta
\right\rfloor.
}
$$

所以：

$$
\boxed{
\mathcal G^{\theta,\gamma}
\text{ is uniformly finitely branching}.
}
$$

### Proof

第一式由 Theorem 8.1。

每個 child必位於：

$$
V_{J+1}^{\theta},
$$

所以 out-degree不超過下一 level node數。$\square$

---

# 27. Finite-horizon ancestry path

對：

$$
N\ge0,
$$

定義 horizon：

$$
[J_0,J_0+N].
$$

一條：

$$
(\theta,\gamma)
$$

-qualified finite path是：

$$
\boxed{
\pi_N
=
(v_{J_0},v_{J_0+1},\ldots,v_{J_0+N})
}
$$

滿足：

$$
v_J\in V_J^\theta,
$$

且：

$$
(v_J,v_{J+1})
\in
E_J^{\theta,\gamma}
$$

對所有相鄰 levels成立。

記 finite path set：

$$
\boxed{
\mathscr P_N(\theta,\gamma).
}
$$

---

# 28. 全域量詞真正需要什麼？

我們現在可以精確區分：

$$
\boxed{
\forall N\;
\mathscr P_N(\theta,\gamma)\neq\varnothing
}
$$

與：

$$
\boxed{
\exists
(v_J)_{J\ge J_0}
\text{ an infinite }
(\theta,\gamma)
\text{-qualified path}.
}
$$

在一般 infinitely branching graph中，

前者不能無條件升級到後者。

但 Theorem 26.1提供了正好需要的 finite branching。

---

# 29. Backward survivor recursion

固定 finite terminal horizon：

$$
N.
$$

令 terminal survivor set：

$$
\boxed{
S_{J_0+N}^{(N)}
=
V_{J_0+N}^{\theta}.
}
$$

向後遞迴定義：

$$
\boxed{
S_J^{(N)}
=
\left\{
v\in V_J^\theta:
\exists
w\in
S_{J+1}^{(N)}
\text{ with }
(v,w)\in
E_J^{\theta,\gamma}
\right\}.
}
$$

這稱：

$$
\boxed{
\textbf{Backward Survivor Recursion}.
}
$$

---

# 30. C5.7 — Finite-Horizon Survivor Criterion

## Theorem 30.1

有：

$$
\boxed{
\mathscr P_N(\theta,\gamma)
\neq
\varnothing
}
$$

當且僅當：

$$
\boxed{
S_{J_0}^{(N)}
\neq
\varnothing.
}
$$

### Proof

若存在 path，

其 terminal node在：

$$
S_{J_0+N}^{(N)}.
$$

逐步向前一 level看，

path上的 node皆依 recursion屬於 survivor set。

故 root node在：

$$
S_{J_0}^{(N)}.
$$

反之，

若：

$$
v_{J_0}\in S_{J_0}^{(N)},
$$

由 survivor definition可選一個：

$$
v_{J_0+1}\in S_{J_0+1}^{(N)}
$$

與之相容。

有限次遞迴選擇至 terminal level即得到 path。$\square$

---

# 31. Survivor sets 對 horizon 單調

對 fixed：

$$
J,
$$

若：

$$
N_2>N_1\ge J-J_0,
$$

則：

$$
\boxed{
S_J^{(N_2)}
\subseteq
S_J^{(N_1)}.
}
$$

因為能延伸到更遠 horizon 的 node一定能延伸到較近 horizon。

---

# 32. C5.8 — Infinite Path Extraction Theorem

## Theorem 32.1

固定：

$$
\theta>0,
\qquad
\gamma>0.
$$

若：

$$
\boxed{
\forall N\ge0,
\quad
\mathscr P_N(\theta,\gamma)
\neq
\varnothing,
}
$$

則存在一條 infinite：

$$
(\theta,\gamma)
$$

-qualified provenance path：

$$
\boxed{
v_{J_0}
\to
v_{J_0+1}
\to
v_{J_0+2}
\to\cdots.
}
$$

### Proof

由 Theorem 26.1：

$$
V_{J_0}^{\theta}
$$

有限。

由 Theorem 30.1，

所有：

$$
S_{J_0}^{(N)}
$$

非空。

且 Section 31 給 nested：

$$
S_{J_0}^{(N+1)}
\subseteq
S_{J_0}^{(N)}.
$$

有限集合中的 nested nonempty subsets有 nonempty intersection：

$$
\bigcap_N
S_{J_0}^{(N)}
\neq
\varnothing.
$$

取：

$$
v_{J_0}
$$

在此 intersection。

它對任意 horizon皆有延伸。

其可接受 children位於 finite：

$$
V_{J_0+1}^{\theta}.
$$

至少一個 child必可延伸至 arbitrarily large horizons；

否則所有 children各自只有 finite extension depth，

取最大值便會使：

$$
v_{J_0}
$$

也只有 finite extension depth，

矛盾。

選此 child為：

$$
v_{J_0+1}.
$$

重複相同 argument，

遞迴得到 infinite path。$\square$

---

# 33. 這就是 Kőnig-type infinity principle 的 RFP 版本

Theorem 32.1 是 classical finitely-branching infinity principle 在 RFP witness graph上的直接實現。

但本文給出 self-contained survivor proof，

所以不把 graph-theory theorem當作未檢查 black box。

最重要的邏輯形式是：

$$
\boxed{
\left[
\forall N\;
\exists\text{ qualified finite ancestry of depth }N
\right]
+
\text{finite branching}
}
$$

推出：

$$
\boxed{
\exists\text{ one qualified infinite ancestry}.
}
$$

這正是前幾篇一直缺的 global quantifier bridge。

---

# 34. Finite stitching obstruction

若存在：

$$
N_\ast<\infty
$$

使：

$$
\boxed{
S_{J_0}^{(N_\ast)}
=
\varnothing,
}
$$

則：

$$
\mathscr P_{N_\ast}(\theta,\gamma)
=
\varnothing.
$$

稱：

$$
\boxed{
N_\ast
}
$$

為：

$$
\boxed{
\textbf{finite stitching obstruction horizon}.
}
$$

---

# 35. Obstruction certificate

一個 finite stitching obstruction certificate可保存：

$$
\boxed{
\mathsf{StitchCert}
=
\left\langle
J_0,
N_\ast,
\theta,
\gamma,
\{V_J^\theta\},
\{E_J^{\theta,\gamma}\},
\{S_J^{(N_\ast)}\},
\mathsf{Reasons}
\right\rangle.
}
$$

其中：

$$
\mathsf{Reasons}
$$

對每個被 prune 的 node保存：

- no frequency-linked child；
- insufficient tube seam overlap；
- failed PDE bridge certificate；
- child node below strength threshold；
- source/projection/localization guard failure。

因此：

$$
\boxed{
\text{global path failure}
}
$$

可以被壓縮成：

$$
\boxed{
\text{finite backward-pruning certificate}.
}
$$

---

# 36. Minimal obstruction horizon

定義：

$$
\boxed{
H_\ast(\theta,\gamma)
=
\inf
\left\{
N:
S_{J_0}^{(N)}
=
\varnothing
\right\}.
}
$$

若集合空，

令：

$$
H_\ast(\theta,\gamma)=\infty.
$$

由 Theorem 32.1：

$$
\boxed{
H_\ast(\theta,\gamma)=\infty
}
$$

當且僅當存在 infinite：

$$
(\theta,\gamma)
$$

-qualified path。

---

# 37. Global quantifier compiler

所以固定：

$$
\theta,\gamma>0
$$

後，

RFP persistence問題被 exact改寫為：

$$
\boxed{
H_\ast(\theta,\gamma)
<
\infty
}
$$

或：

$$
\boxed{
H_\ast(\theta,\gamma)
=
\infty.
}
$$

第一種是 finite obstruction。

第二種直接給 infinite path。

這是本文最重要的 quantifier compilation。

---

# 38. 但 fixed positive thresholds 可能不存在

Full Chain Necessity不能預先假設：

$$
\theta>0
$$

與：

$$
\gamma>0
$$

可以 uniformly固定。

可能發生：

$$
\text{每個 finite horizon都有 candidate path，}
$$

但所有長路徑都被迫經過：

$$
\text{weaker and weaker witnesses}
$$

或：

$$
\text{weaker and weaker compatibility}.
$$

這就是下一個 escape：

$$
\boxed{
\textbf{persistence bottleneck collapse}.
}
$$

---

# 39. Unthresholded positive candidate paths

令：

$$
\mathscr P_N^+
$$

為所有 finite sequences：

$$
(v_{J_0},\ldots,v_{J_0+N})
$$

使：

$$
\pi_J(v_J)>0
$$

且：

$$
\mathfrak c_J^{prov}(v_J,v_{J+1})>0.
$$

若：

$$
\mathscr P_N^+=\varnothing,
$$

則 horizon：

$$
N
$$

已經發生 absolute finite stitching obstruction。

---

# 40. Path bottleneck

對：

$$
\pi
=
(v_{J_0},\ldots,v_{J_0+N})
\in
\mathscr P_N^+,
$$

定義：

$$
\boxed{
\operatorname{Bot}(\pi)
=
\min
\left\{
\min_{J_0\le J\le J_0+N}
\pi_J(v_J),
\;
\min_{J_0\le J<J_0+N}
\mathfrak c_J^{prov}(v_J,v_{J+1})
\right\}.
}
$$

所以：

$$
0<
\operatorname{Bot}(\pi)
\le1.
$$

---

# 41. Horizon bottleneck

定義：

$$
\boxed{
\beta_N
=
\sup_{\pi\in\mathscr P_N^+}
\operatorname{Bot}(\pi).
}
$$

若：

$$
\mathscr P_N^+=\varnothing,
$$

定義：

$$
\beta_N=0.
$$

---

# 42. C5.9 — Bottleneck Monotonicity

## Theorem 42.1

有：

$$
\boxed{
\beta_{N+1}
\le
\beta_N.
}
$$

因此 limit：

$$
\boxed{
\beta_\infty
=
\lim_{N\to\infty}\beta_N
}
$$

存在於：

$$
[0,1].
$$

### Proof

任何 length：

$$
N+1
$$

path 截斷最後一個 node後，

得到 length：

$$
N
$$

path。

截斷不會降低 bottleneck。

因此：

$$
\sup_{\mathscr P_{N+1}}
\operatorname{Bot}
\le
\sup_{\mathscr P_N}
\operatorname{Bot}.
$$

$\square$

---

# 43. C5.10 — Persistence Trichotomy

## Theorem 43.1

exactly落入以下三類之一：

### P-A — Finite stitching obstruction

存在：

$$
N_\ast<\infty
$$

使：

$$
\boxed{
\mathscr P_{N_\ast}^+
=
\varnothing.
}
$$

### P-B — Bottleneck collapse

對所有：

$$
N,
$$

有：

$$
\mathscr P_N^+\neq\varnothing,
$$

但：

$$
\boxed{
\beta_\infty=0.
}
$$

### P-C — Uniform persistent ancestry

$$
\boxed{
\beta_\infty>0.
}
$$

且此時存在 infinite provenance path：

$$
(v_J)_{J\ge J_0}
$$

與某：

$$
\delta>0
$$

使：

$$
\boxed{
\pi_J(v_J)\ge\delta,
}
$$

以及：

$$
\boxed{
\mathfrak c_J^{prov}(v_J,v_{J+1})
\ge\delta
}
$$

for all：

$$
J\ge J_0.
$$

### Proof

若某 finite path set空，為 P-A。

否則所有：

$$
\beta_N>0.
$$

由 monotonicity：

$$
\beta_\infty
$$

存在。

若為：

$$
0,
$$

得到 P-B。

若：

$$
\beta_\infty>0,
$$

選：

$$
0<\delta<\beta_\infty.
$$

對每個：

$$
N,
$$

由 supremum定義存在：

$$
\operatorname{Bot}(\pi_N)>\delta.
$$

所以：

$$
\mathscr P_N(\delta,\delta)\neq\varnothing
$$

for all $N$。

Theorem 32.1給 infinite：

$$
(\delta,\delta)
$$

-qualified path。$\square$

---

# 44. 這是 proof-space enclosure，不是 regularity theorem

Theorem 43.1 對 persistence quantifier已經 exhaustive。

但：

$$
P\mbox{-}A
$$

只是相對目前：

$$
\mathfrak c^{prov}
$$

與 node class 的 finite obstruction。

若 compatibility module不完整，

它不能直接被宣稱：

$$
\text{dynamically impossible}.
$$

而：

$$
P\mbox{-}B
$$

也可能是真實 singularity ancestry：

它只是沒有 uniform positive bottleneck。

所以仍需 PDE estimate排除：

$$
P\mbox{-}B
$$

或把其 vanishing bottleneck轉成新的 quantitative debt。

---

# 45. Two-parameter feasibility region

對每個：

$$
N,
$$

定義：

$$
\boxed{
\mathcal F_N
=
\left\{
(\theta,\gamma)\in(0,1]^2:
\mathscr P_N(\theta,\gamma)\neq\varnothing
\right\}.
}
$$

它具有：

$$
\boxed{
\mathcal F_{N+1}
\subseteq
\mathcal F_N.
}
$$

且若：

$$
(\theta,\gamma)\in\mathcal F_N,
$$

則任何：

$$
0<\theta'\le\theta,
\qquad
0<\gamma'\le\gamma
$$

也在：

$$
\mathcal F_N.
$$

所以：

$$
\mathcal F_N
$$

是 downward-closed feasible region。

---

# 46. Persistent feasible core

定義：

$$
\boxed{
\mathcal F_\infty
=
\bigcap_{N\ge0}
\mathcal F_N.
}
$$

若存在：

$$
(\theta,\gamma)
\in
\mathcal F_\infty
$$

with：

$$
\theta>0,
\quad
\gamma>0,
$$

則由 Theorem 32.1：

$$
\boxed{
\text{an infinite persistent ancestry exists}.
}
$$

若所有 finite horizons可行，

但：

$$
\mathcal F_\infty
$$

沒有 positive-positive point，

就是另一種表示：

$$
\boxed{
\text{persistence bottleneck collapses toward the threshold axes}.
}
$$

---

# 47. Bottleneck collapse 的 typed causes

P-B 不應被當作單一 failure。

可能至少來自：

### B-NODE

$$
\boxed{
\text{node-strength atomization}
}
$$

即 strong local source share趨零。

### B-SEAM

$$
\boxed{
\text{tube seam overlap degeneration}
}
$$

即 spatial continuity只能靠越來越小 overlap。

### B-BRIDGE

$$
\boxed{
\text{PDE bridge degeneration}
}
$$

即：

$$
\mathfrak b_J\to0
$$

along every long candidate path。

### B-TRADE

node strength與compatibility存在 horizon-dependent tradeoff，

兩者個別可能有 strong candidates，

但無法在同一 path上同時保持。

所以：

$$
\boxed{
\beta_\infty=0
}
$$

是 global persistence defect，

不是單一 local observable。

---

# 48. Spatial fan-out 與 bottleneck collapse

若：

$$
\mathfrak o_J(a,a')\ge\gamma,
$$

Theorem 18.1給 fixed：

$$
\gamma>0
$$

下 spatial fan-out finite。

因此若 persistence只能靠：

$$
\gamma_J\to0,
$$

這不是 soft tails的 trivial artifact，

而是：

$$
\boxed{
\text{effective spatial branching scale diverges}.
}
$$

因：

$$
|\mathcal A_{J+1}(a;\gamma_J)|
\lesssim
\gamma_J^{-1}.
$$

所以：

$$
\boxed{
\gamma_J\to0
\Longrightarrow
\text{spatial branching debt can diverge}.
}
$$

---

# 49. Node atomization 與 branching debt

若：

$$
\mathfrak a_J\to0,
$$

Theorem 12.1給：

$$
\mathfrak M_J^{eff}\to\infty.
$$

所以 node bottleneck collapse必須伴隨：

$$
\boxed{
\text{local-source activity spread across more effective spacetime parent entries}.
}
$$

這是 persistence-level analogue of RFP-03 parent multiplicity debt。

---

# 50. Strong-node branching bound

對 fixed：

$$
\theta>0,
$$

有：

$$
|V_J^\theta|
\le
\theta^{-1}.
$$

所以任一 length：

$$
N
$$

的 thresholded path candidate總數有粗 bound：

$$
\boxed{
|\mathscr P_N(\theta,\gamma)|
\le
\theta^{-(N+1)}.
}
$$

這個 bound不是計算上最有效，

但它證明每個 fixed horizon的 candidate space有限。

---

# 51. Survivor recursion 是 finite computation 可驗證的

對 fixed：

$$
J_0,
N,\theta,\gamma,
$$

只要：

- node ledger entries可 certified；
- compatibility predicates可 certified；
- bridge scores有可驗證 lower bounds；

則：

$$
S_J^{(N)}
$$

可以由 terminal level向後有限步計算。

所以：

$$
\boxed{
\text{finite-horizon path existence}
}
$$

不是 existential black box。

它可以輸出：

$$
\boxed{
\text{survivor set}
}
$$

或：

$$
\boxed{
\text{finite obstruction certificate}.
}
$$

---

# 52. 但 finite computation 仍不能單獨證 continuum closure

若只驗證：

$$
N\le N_{\max},
$$

只能得到：

$$
H_\ast(\theta,\gamma)>N_{\max}.
$$

不能推出：

$$
H_\ast(\theta,\gamma)=\infty.
$$

要從所有 finite horizons提升成 infinite path，

仍需要 theorem-level：

$$
\boxed{
\forall N
}
$$

statement，

或 resolution-independent analytic estimate保證 survivor recursion永不清空。

所以：

$$
\boxed{
\text{large finite depth}
\neq
\text{infinite ancestry}.
}
$$

---

# 53. Finite obstruction 的合法性等級

本文區分：

### O-CERT — Certificate-class obstruction

thresholded witness graph在 finite horizon清空。

### O-DYN — Dynamical obstruction

已證明任何真實 N--S ancestry都必落在該 certificate class，

所以 graph清空真的排除 dynamics。

只有：

$$
O\mbox{-}DYN
$$

才能進入最終 Finite Obstruction theorem。

因此新增：

$$
\boxed{
G_{\rm COMPLETE}:
\quad
\text{certificate-class exhaustion must be proved before finite graph failure is called dynamical impossibility}.
}
$$

---

# 54. 這防止一個很危險的假證明

錯誤形式：

$$
\text{my selected witness graph has no infinite path}
$$

所以：

$$
\text{Navier--Stokes has no singularity}.
$$

這完全不成立，

除非先證：

$$
\boxed{
\text{every singularity ancestry must be represented in the selected graph}.
}
$$

也就是：

$$
\boxed{
\text{graph completeness}.
}
$$

這和此前：

$$
\text{balance closeness}
\neq
\text{dynamics closeness}
$$

以及：

$$
\text{certificate failure}
\neq
\text{dynamical impossibility}
$$

是同一類 theorem-safety guard。

---

# 55. RFP-05 Master Persistence Enclosure

## Theorem 55.1

考慮一條 infinite PF-A first-passage subsequence。

給定 RFP-04 合法 local-source ledger與一個 certified provenance compatibility score：

$$
\mathfrak c_J^{prov}.
$$

則 persistence problem必落入：

$$
\boxed{
P\mbox{-}A
\vee
P\mbox{-}B
\vee
P\mbox{-}C,
}
$$

其中：

### P-A

finite horizon出現：

$$
\boxed{
\text{stitching obstruction}.
}
$$

### P-B

arbitrarily long finite paths存在，

但：

$$
\boxed{
\beta_\infty=0
}
$$

而 persistence只能經由 vanishing node / seam / bridge bottleneck。

### P-C

存在：

$$
\boxed{
\text{one infinite provenance path with uniform positive node and compatibility floors}.
}
$$

此外：

- node-floor collapse必支付 effective multiplicity debt；
- seam-floor collapse允許 effective spatial branching scale diverge；
- any P-A result要升級成 dynamical obstruction必先通過 $G_{\rm COMPLETE}$。

$\square$

---

# 56. 與 PF-B synchronous branch 的關係

RFP-03 已證：

任意 infinite first-passage sequence有 subsequence落入：

$$
PF\mbox{-}A
$$

或：

$$
PF\mbox{-}B.
$$

本文主要處理：

$$
PF\mbox{-}A
$$

的 persistence quantifier。

若只有 finitely many PF-A edges，

則必有 infinite：

$$
PF\mbox{-}B
$$

synchronous/deep-tail subsequence。

該 branch仍屬：

$$
\boxed{
\text{Synchronous-Bypass / Carrier-Depth Escape}.
}
$$

所以 Full Chain Necessity目前仍需：

$$
\boxed{
\text{PF-A persistence closure}
+
\text{PF-B synchronous resolution}.
}
$$

---

# 57. 與 2026 finite-window / finite-chain literature 的關係

近期 Navier--Stokes finite-window研究已明確發展：

- finite-scale supply--tax reductions；
- finite-window local-to-clean transfer；
- recursive finite-chain audit propagation；
- finite-chain CKN-bad-scale counting。

這些工作非常適合提供：

$$
\boxed{
\text{one-step / finite-horizon PDE certificates}.
}
$$

但 finite-chain propagation本身仍不自動等於：

$$
\boxed{
\text{one infinite persistent ancestry}.
}
$$

RFP-05 專門把這個 logical transition拆開：

$$
\boxed{
\text{finite-horizon admissibility}
+
\text{positive bottleneck}
+
\text{finite branching}
\Longrightarrow
\text{infinite path}.
}
$$

---

# 58. Graph-theoretic calibration

classical infinity lemmas對 finitely branching trees提供：

> arbitrarily deep finite branches imply an infinite ray.

本文不直接把 RFP witness system假設成 tree。

而是：

1. 先形成 layered directed graph；
2. 將 finite compatible paths當作 tree nodes；
3. 用 survivor recursion自證 infinite path extraction。

所以 graph theory在此不是 PDE input，

而是：

$$
\boxed{
\text{quantifier-closure engine}.
}
$$

---

# 59. X-Integration 更新：Persistence Compiler

新增一個 X-level operator：

$$
\boxed{
\mathsf{Persist}_{\theta,\gamma}^{N}
}
$$

輸入：

$$
\left(
V_{J_0}^{\theta},
\ldots,
V_{J_0+N}^{\theta},
E_{J_0}^{\theta,\gamma},
\ldots,
E_{J_0+N-1}^{\theta,\gamma}
\right),
$$

輸出：

$$
\boxed{
\mathsf{SURVIVE}
}
$$

若：

$$
S_{J_0}^{(N)}\neq\varnothing,
$$

或：

$$
\boxed{
\mathsf{OBSTRUCTED}
}
$$

若：

$$
S_{J_0}^{(N)}=\varnothing.
$$

---

# 60. Persistence provenance certificate

若：

$$
\mathsf{SURVIVE},
$$

保存：

$$
\boxed{
\mathsf{PersistCert}_N
=
\left\langle
\{S_J^{(N)}\},
\mathsf{ParentPointers},
\mathsf{NodeScores},
\mathsf{CompatibilityScores},
\mathsf{GuardStates}
\right\rangle.
}
$$

若：

$$
\mathsf{OBSTRUCTED},
$$

保存：

$$
\boxed{
\mathsf{ObstructCert}_N
=
\left\langle
\{S_J^{(N)}\},
\mathsf{PruneReasons},
\mathsf{CompletenessStatus}
\right\rangle.
}
$$

特別：

$$
\mathsf{CompletenessStatus}
$$

不得省略。

---

# 61. New guards

新增：

### $G_{\rm QUANT}$

$$
\forall J\exists v_J
$$

不得偷換成：

$$
\exists(v_J)_J\forall J.
$$

### $G_{\rm FINBR}$

finite-horizon-to-infinite extraction必須有 finite branching或其他明示 compactness theorem。

### $G_{\rm SEAM}$

spatial tube continuity必須保存 seam overlap certificate。

### $G_{\rm BRIDGE}$

stock/tube continuity不得替代 equation-level provenance bridge。

### $G_{\rm SURV}$

finite path existence使用 backward survivor recursion或等價 exact certificate。

### $G_{\rm BOT}$

若 uniform positive bottleneck不存在，

必保留 bottleneck-collapse branch，

不得硬抽 strong infinite path。

### $G_{\rm COMPLETE}$

certificate-class obstruction只有在 class completeness已證時才能升級成 dynamical obstruction。

---

# 62. Guard Library v4

因此：

$$
\boxed{
\mathcal G_{NS}^{(4)}
=
\mathcal G_{NS}^{(3)}
\cup
\{
G_{\rm QUANT},
G_{\rm FINBR},
G_{\rm SEAM},
G_{\rm BRIDGE},
G_{\rm SURV},
G_{\rm BOT},
G_{\rm COMPLETE}
\}.
}
$$

---

# 63. Chain Necessity 現在縮到哪裡？

RFP-01 時：

$$
\boxed{
\text{UV escape}
\stackrel{?}{\Longrightarrow}
\text{full formation ancestry}.
}
$$

RFP-02 後：

$$
\boxed{
\text{first-passage skeleton}
+
\text{source debt}.
}
$$

RFP-03 後：

$$
\boxed{
\text{exact parent ledger}.
}
$$

RFP-04 後：

$$
\boxed{
\text{uniform-tightness budget}
+
\text{spacetime source-core ledger}.
}
$$

RFP-05 後：

$$
\boxed{
\text{finite-horizon compatible ancestry}
+
\text{positive bottleneck}
\Longrightarrow
\text{infinite persistent path}.
}
$$

所以 Full Chain Necessity的主缺口已經高度集中到：

$$
\boxed{
\textbf{inter-edge PDE bridge lower bounds}
}
$$

以及：

$$
\boxed{
\textbf{bottleneck-collapse exclusion / debt}.
}
$$

另外仍保留：

$$
PF\mbox{-}B
$$

synchronous bypass branch。

---

# 64. 下一篇的真正 PDE frontier

因此下一篇不應先回去擴充更多 graph notation。

正式 frontier是：

$$
\boxed{
\textbf{NS-RFP 06 — Inter-Edge Bridge Realization、Source-Stock Propagation 與 Persistence Bottleneck Lower Bounds}.
}
$$

核心問題：

1. 將前一 edge 的 actual nonlinear output increment分解到 shared seam；
2. 證明其 heat/nonlinear continuation如何進入下一 edge parent source；
3. 建立：
   $$
   \mathfrak b_J(v,w)
   $$
   的 equation-level formula；
4. 找 sufficient conditions使：
   $$
   \mathfrak b_J(v,w)\ge\gamma_0>0;
   $$
5. 若無 uniform lower bound，
   將：
   $$
   \mathfrak b_J\to0
   $$
   轉成 source dilution / cancellation / transport escape debt；
6. 將 tube seam overlap與 actual field stock而非純 geometry對接；
7. 判定 bottleneck-collapse P-B 是否可由 exact N--S structure排除或 rigidify。

---

# 65. Formal status ledger

$$
\boxed{
\begin{aligned}
\text{exact local-source refinement}
&:\ \mathrm{PROVED},\\
\text{positive local-source probability ledger}
&:\ \mathrm{DEFINED},\\
\text{fixed-threshold finite level bound}
&:\ \mathrm{PROVED},\\
\text{atomization implies effective multiplicity divergence}
&:\ \mathrm{PROVED},\\
\text{time seam identity}
&:\ \mathrm{PROVED\ from\ first\mbox{-}passage\ construction},\\
\text{adjoint seam partition identity}
&:\ \mathrm{PROVED},\\
\text{effective spatial fan-out bound}
&:\ \mathrm{PROVED},\\
\text{stock compatibility score}
&:\ \mathrm{DEFINED},\\
\text{universal PDE bridge score}
&:\ \mathrm{OPEN},\\
\text{thresholded graph finite branching}
&:\ \mathrm{PROVED},\\
\text{backward survivor recursion}
&:\ \mathrm{DEFINED},\\
\text{finite-horizon survivor criterion}
&:\ \mathrm{PROVED},\\
\text{finite-horizon to infinite path extraction}
&:\ \mathrm{PROVED},\\
\text{finite stitching obstruction certificate}
&:\ \mathrm{PROVED\ relative\ to\ certified\ graph},\\
\text{persistence bottleneck monotonicity}
&:\ \mathrm{PROVED},\\
\text{persistence trichotomy}
&:\ \mathrm{PROVED},\\
\text{graph completeness for all N--S ancestries}
&:\ \mathrm{OPEN},\\
\text{uniform positive provenance bottleneck}
&:\ \mathrm{OPEN},\\
\text{PF-B synchronous resolution}
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

# 66. 結論

RFP-05 解決的不是一個新的 local PDE estimate。

它解決的是前四篇一直累積的：

$$
\boxed{
\textbf{global quantifier conversion problem}.
}
$$

對 fixed positive node與compatibility thresholds：

$$
\theta,\gamma>0,
$$

strong witness levels自動 finite：

$$
|V_J^\theta|
\le
\theta^{-1}.
$$

因此：

$$
\boxed{
\forall N
\;\exists
\text{ qualified finite ancestry of depth }N
}
$$

可以 rigorously提升成：

$$
\boxed{
\exists
\text{ one infinite qualified ancestry}.
}
$$

而如果 finite-horizon extension失敗，

backward survivor recursion會在某個 finite：

$$
N_\ast
$$

清空，

留下：

$$
\boxed{
\text{finite stitching obstruction certificate}.
}
$$

如果 arbitrarily long finite paths都存在，

但任何 uniform threshold都無法維持，

則問題被迫落入：

$$
\boxed{
\text{persistence bottleneck collapse}.
}
$$

所以 persistence space已被壓成：

$$
\boxed{
\text{finite obstruction}
\vee
\text{bottleneck collapse}
\vee
\text{infinite persistent path}.
}
$$

這是一個真正 exhaustive 的 proof-space enclosure。

但 full Navier--Stokes conclusion仍需要證明：

$$
\boxed{
\mathfrak b_J
}
$$

不是一個任意抽象 compatibility score，

而能由 exact N--S Duhamel / source-stock propagation得到足夠的 quantitative lower bound。

因此下一輪正式進入：

$$
\boxed{
\textbf{NS-RFP 06 — Inter-Edge Bridge Realization、Source-Stock Propagation 與 Persistence Bottleneck Lower Bounds}.
}
$$

---

# References

1. R. Diestel, *Graph Theory*, Springer. Classical infinity principles for finitely branching trees are used only as graph-theoretic calibration; the RFP path-extraction theorem is proved self-contained above.
2. T. Barker, H. Popkin, *Quantitative estimates for the forced Navier–Stokes equations and applications*, arXiv:2602.09951 (2026).
3. R. Yu, *Critical Ledgers and Scale-Defect Cascades for Navier–Stokes*, arXiv:2606.13887 (2026).
4. R. Yu, *Finite-Window Singularity Audits and Local-to-Clean Defect Transfer for Navier–Stokes*, arXiv:2606.15086 (2026).
5. R. Yu, *Finite-Window Recursive Audit Chains for Navier–Stokes Generated Packages*, arXiv:2606.20899 (2026).
6. R. Yu, *Finite-Chain CKN-Bad Scale Counting for Navier–Stokes: Standard PDE Closure and Canonical Detector Realization*, arXiv:2606.21783 (2026).

# Internal dependencies

- `NS_RFP_01_SingularityFormationAncestry_FiniteObstruction_v0.1.md`
- `NS_RFP_02_CriticalUV_FirstPassage_SourceDebt_v0.1.md`
- `NS_RFP_03_DualWitness_ParentLedger_CarrierEscape_v0.1.md`
- `NS_RFP_04_SpatialTube_PressureCompatible_UniformParentTightness_v0.1.md`
- `NS_C3O_AdjointCore_BalanceDynamicsSeparation_v0.2.md`
- `NS_ETN_XIntegration_Multiscale_NonCollapse_v0.1.md`
- `True ETN / 無限維張力場`
- `X_Integral_Unified_Program_v0.2.md`

# Next

$$
\boxed{
\textbf{NS-RFP 06 — Inter-Edge Bridge Realization、Source-Stock Propagation 與 Persistence Bottleneck Lower Bounds}
}
$$
