---
title: "Navier–Stokes Reverse Formation Program 04：Adjoint Spacetime Tube Ledger、Pressure-Compatible Localization 與 Quantitative Uniform Parent Tightness"
short_title: "NS-RFP 04"
version: "v0.1"
date: "2026-08-14"
author: "Neo.K / EveMissLab"
language: "zh-TW"
status: "Theorem-style structural advance / frequency-to-spacetime bridge"
epistemic_status: "Builds an exact adjoint spacetime-tube refinement of the RFP-03 parent ledger; proves a pressure-compatible band-passed Leray commutator estimate and pseudolocality; derives a scale-invariant quantitative tail bound that upgrades parent tightness whenever a dissipation-output budget is bounded. Does NOT prove that this budget is universally bounded, witness persistence across all edges, full Chain Necessity, Finite Obstruction, or Navier–Stokes regularity."
canonical_source: "UTF-8 Markdown"
---

# Navier–Stokes Reverse Formation Program 04

# Adjoint Spacetime Tube Ledger、Pressure-Compatible Localization 與 Quantitative Uniform Parent Tightness

## 0. 本文定位

NS-RFP 03 已將 PF-A source-paid first-passage edge 的 aggregate nonlinear source debt提升成 exact signed dyadic parent-output ledger：

$$
\boxed{
R_J
=
\sum_{k,p,q}
\Lambda^{(J)}_{k;p,q}
\ge
d_J.
}
$$

其中：

$$
(k;p,q)
$$

是 exact dyadic output-parent labels。

RFP-03 並證明：

$$
\text{far upward quadratic jump}
$$

不可能，而 large positive parent-output gap：

$$
g(k;p,q)
=
\max\{p,q\}-k
$$

只能由 near-resonant high--high parents支付。

但 RFP-03 留下兩個直接缺口：

$$
\boxed{
\text{per-edge parent tightness}
\not\Rightarrow
\text{uniform chain tightness},
}
$$

以及：

$$
\boxed{
\text{global-frequency provenance}
\not\Rightarrow
\text{spacetime provenance}.
}
$$

本文同時攻這兩個問題。

核心結果：

1. 建立 scale-invariant dissipation-output budget：
   $$
   \mathfrak V_J
   =
   \mathfrak E_J\mathfrak O_J;
   $$
2. 證明 quantitative parent-tail estimate：
   $$
   \boxed{
   1-C_J^{par}(L)
   \le
   C2^{-L}\mathfrak V_J;
   }
   $$
3. 因而：
   $$
   \sup_J\mathfrak V_J<\infty
   \Longrightarrow
   \text{uniform parent tightness};
   $$
4. 反之 PS / PE parent escape 必迫使：
   $$
   \mathfrak V_J\to\infty
   $$
   沿相應 subsequence；
5. 將 C3-O backward adjoint cutoff升級為 nonnegative partition of unity，建立 exact：
   $$
   (a;k;p,q)
   $$
   spacetime-tube parent ledger；
6. 對 band-passed Leray source：
   $$
   \mathcal T_k
   =
   \Delta_k\mathbb P\nabla\cdot
   $$
   證明 pressure-compatible commutator estimate與 spatial pseudolocality；
7. 建立：
   $$
   \boxed{
   \text{tube contribution}
   =
   \text{tube-local source}
   +
   \text{commutator/leakage tax}.
   }
   $$

本文因此第一次把：

$$
\boxed{
\text{frequency parent ledger}
}
$$

推到：

$$
\boxed{
\text{spacetime soft-tube parent ledger}.
}
$$

---

# 1. Setting

考慮三維不可壓縮 Navier--Stokes：

$$
\partial_tu
-
\nu\Delta u
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

本文沿用 RFP-03 的 compact pre-singular smooth/decay assumptions，使 Littlewood--Paley series、Bochner integrals、dyadic parent sums與 dual pairings可逐項交換。

---

# 2. RFP-03 PF-A edge input

固定 threshold：

$$
M>0.
$$

對 PF-A edge：

$$
d_J>0,
$$

令：

$$
s_J=\tau_J(M),
\qquad
t_J=\tau_{J+1}(M).
$$

RFP-03 定義 nonlinear tail increment：

$$
W_J
=
U_{J+1}(t_J)
-
\mathsf H_{t_J-s_J}
U_{J+1}(s_J),
$$

以及：

$$
R_J
=
\|W_J\|_{X_{J+1}}
\ge
d_J.
$$

寫：

$$
W_J=(w_k)_{k>J+1},
$$

$$
b_k=\|w_k\|_3.
$$

則：

$$
R_J^2
=
\sum_{k>J+1}b_k^2.
$$

---

# 3. RFP-03 dual witness

RFP-03 構造：

$$
\Phi_J
=
(\phi_k)_{k>J+1}
\in
X_{J+1}^*,
$$

使：

$$
\|\Phi_J\|_{X_{J+1}^*}=1,
$$

以及：

$$
\boxed{
\langle W_J,\Phi_J\rangle=R_J.
}
$$

而且：

$$
\|\phi_k\|_{3/2}
=
\frac{b_k}{R_J}.
$$

此 identity是本文所有 spatial refinement 的線性入口。

---

# 4. Exact parent ledger input

令：

$$
\mathcal T_k
=
\Delta_k\mathbb P\nabla\cdot.
$$

對 dyadic parent pair：

$$
(p,q),
$$

令：

$$
F_{p,q}
=
u_p\otimes u_q.
$$

RFP-03 的 exact parent ledger 可寫為：

$$
\boxed{
\Lambda^{(J)}_{k;p,q}
=
-
\int_{s_J}^{t_J}
\left\langle
\mathcal T_kF_{p,q}(r),
\varphi_{J,k}(r)
\right\rangle dr,
}
$$

其中：

$$
\boxed{
\varphi_{J,k}(r)
=
e^{\nu(t_J-r)\Delta}\phi_k.
}
$$

因 heat semigroup self-adjoint，

這與 RFP-03 原本將 heat semigroup留在 source side 的定義等價。

---

# 5. Backward dual contraction

對：

$$
s_J\le r\le t_J,
$$

有：

$$
\boxed{
\|\varphi_{J,k}(r)\|_{3/2}
\le
\|\phi_k\|_{3/2}
=
\frac{b_k}{R_J}.
}
$$

所以 backward heat propagation不增加 dual norm。

---

# 6. Parent-gap escape input

RFP-03 定義：

$$
g(k;p,q)
=
\max\{p,q\}-k.
$$

並證存在固定：

$$
C_1<\infty
$$

只依賴 LP cutoff，使：

$$
g(k;p,q)>C_1
$$

且：

$$
\mathcal T_k(u_p\otimes u_q)\neq0
$$

時必有：

$$
\boxed{
|p-q|\le C_1.
}
$$

因此 far parent-gap contribution只能走 near-resonant high--high downshift。

---

# 7. Positive parent-tail ratio

令：

$$
P_J
=
\sum_{k,p,q}
[\Lambda^{(J)}_{k;p,q}]_+.
$$

對：

$$
L>C_1,
$$

定義：

$$
P_J^{down}(L)
=
\sum_{g(k;p,q)>L}
[\Lambda^{(J)}_{k;p,q}]_+.
$$

則：

$$
\boxed{
1-C_J^{par}(L)
=
\frac{P_J^{down}(L)}{P_J}.
}
$$

RFP-03 只證：

$$
C_J^{par}(L)\to1
$$

對每個 fixed $J$。

本文尋找 uniform-in-$J$ estimate。

---

# 8. Interval dyadic dissipation ledger

對每個 parent shell：

$$
p\ge-1,
$$

定義：

$$
\boxed{
D_{p,J}
=
\int_{s_J}^{t_J}
2^{2p}
\|u_p(r)\|_2^2\,dr.
}
$$

並令：

$$
\boxed{
D_J
=
\sum_{p\ge-1}D_{p,J}.
}
$$

由 standard energy inequality與 LP equivalence：

$$
D_J
$$

在任何單一 smooth interval有限。

若使用完整 solution energy inequality，

還有：

$$
D_J
\le
C\nu^{-1}\|u_0\|_2^2.
$$

但本文真正需要的是其和：

$$
R_J,
\quad
2^J
$$

形成的 scale-normalized ratio。

---

# 9. Output-depth first moment

定義：

$$
\boxed{
\mathfrak O_J
=
\frac1{R_J}
\sum_{k>J+1}
2^{k-J}b_k.
}
$$

smooth finite-window hypotheses保證此 quantity有限。

$\mathfrak O_J$ 測量 nonlinear tail increment：

$$
W_J
$$

相對 base first-passage scale：

$$
J
$$

向 deeper output shells 的 weighted depth。

---

# 10. Scale-normalized dissipation/debt ratio

定義：

$$
\boxed{
\mathfrak E_J
=
\frac{
2^J D_J
}{
R_J
}.
}
$$

此量把 interval viscous activity與 actual nonlinear increment debt：

$$
R_J
$$

比較。

---

# 11. Viscous downshift budget

定義：

$$
\boxed{
\mathfrak V_J
=
\mathfrak E_J\mathfrak O_J.
}
$$

等價地：

$$
\boxed{
\mathfrak V_J
=
\frac{
D_J
}{
R_J^2
}
\sum_{k>J+1}
2^k b_k.
}
$$

此 quantity將成為 parent escape 的第一個 quantitative obstruction variable。

---

# 12. Scaling audit

考慮 dyadic Navier--Stokes scaling：

$$
u^{(m)}(x,t)
=
2^m
u(2^mx,2^{2m}t).
$$

則：

$$
J\mapsto J+m,
\qquad
k\mapsto k+m.
$$

因 $L^3$ critical：

$$
b_k
$$

與：

$$
R_J
$$

保持數值尺度。

另一方面：

$$
D_J
\mapsto
2^{-m}D_J.
$$

因此：

$$
2^JD_J
$$

scale invariant。

又：

$$
2^{k-J}
$$

不變。

故：

$$
\boxed{
\mathfrak E_J,
\quad
\mathfrak O_J,
\quad
\mathfrak V_J
}
$$

皆為 dyadic scale invariant diagnostics。

---

# 13. Band-passed source estimate

標準 Bernstein與 smooth Fourier multiplier estimates給：

$$
\boxed{
\|
\mathcal T_kF
\|_3
\le
C2^{2k}
\|F\|_{3/2}.
}
$$

原因是：

- $\nabla\cdot$ 提供一個 factor $2^k$；
- output frequency localization使：
  $$
  L^{3/2}\to L^3
  $$
  再提供一個 factor $2^k$。

因此對 parent tensor：

$$
F_{p,q}=u_p\otimes u_q,
$$

有：

$$
\boxed{
\|
\mathcal T_k(u_p\otimes u_q)
\|_3
\le
C2^{2k}
\|u_p\|_3
\|u_q\|_3.
}
$$

---

# 14. Bernstein parent estimate

對 dyadic shell：

$$
p,
$$

有：

$$
\boxed{
\|u_p\|_3
\le
C2^{p/2}
\|u_p\|_2.
}
$$

所以：

$$
\|u_p\|_3\|u_q\|_3
\le
C2^{(p+q)/2}
\|u_p\|_2
\|u_q\|_2.
$$

---

# 15. Dissipation insertion

對：

$$
[s_J,t_J],
$$

Cauchy--Schwarz 給：

$$
\begin{aligned}
\int_{s_J}^{t_J}
\|u_p\|_2\|u_q\|_2\,dr
&=
2^{-p-q}
\int_{s_J}^{t_J}
(2^p\|u_p\|_2)
(2^q\|u_q\|_2)\,dr
\\
&\le
2^{-p-q}
D_{p,J}^{1/2}
D_{q,J}^{1/2}.
\end{aligned}
$$

因此：

$$
\boxed{
\int_{s_J}^{t_J}
\|u_p\|_3\|u_q\|_3\,dr
\le
C
2^{-(p+q)/2}
D_{p,J}^{1/2}
D_{q,J}^{1/2}.
}
$$

---

# 16. Single triad downshift estimate

由 dual contraction：

$$
\|\varphi_{J,k}(r)\|_{3/2}
\le
\frac{b_k}{R_J},
$$

所以：

$$
\begin{aligned}
|\Lambda^{(J)}_{k;p,q}|
&\le
C
\frac{b_k}{R_J}
2^{2k}
\int_{s_J}^{t_J}
\|u_p\|_3\|u_q\|_3\,dr
\\
&\le
C
\frac{b_k}{R_J}
2^{2k-(p+q)/2}
D_{p,J}^{1/2}D_{q,J}^{1/2}.
\end{aligned}
$$

---

# 17. C4.1 — Resonant Downshift Tail Estimate

## Theorem 17.1

存在常數：

$$
C<\infty
$$

只依賴 LP partition，使對所有：

$$
L>C_1,
$$

有：

$$
\boxed{
P_J^{down}(L)
\le
C
2^{-L}
D_J
\sum_{k>J+1}
2^k\frac{b_k}{R_J}.
}
$$

### Proof

在：

$$
g(k;p,q)>L
$$

的 support 上，

RFP-03 Resonant Downshift Lemma給：

$$
|p-q|\le C_1.
$$

且：

$$
\max\{p,q\}>k+L.
$$

所以：

$$
\frac{p+q}{2}
\ge
k+L-C
$$

for a fixed cutoff-dependent constant。

因此：

$$
2^{2k-(p+q)/2}
\le
C2^{k-L}.
$$

故固定 output shell：

$$
k,
$$

有：

$$
\sum_{g>L}
|\Lambda^{(J)}_{k;p,q}|
\le
C
\frac{b_k}{R_J}
2^{k-L}
\sum_{|p-q|\le C_1}
D_{p,J}^{1/2}D_{q,J}^{1/2}.
$$

finite-shift Cauchy estimate給：

$$
\sum_{|p-q|\le C_1}
D_{p,J}^{1/2}D_{q,J}^{1/2}
\le
CD_J.
$$

再對 $k$ 求和：

$$
P_J^{down}(L)
\le
\sum_{g>L}|\Lambda|
\le
C2^{-L}
D_J
\sum_{k>J+1}
2^k\frac{b_k}{R_J}.
$$

$\square$

---

# 18. C4.2 — Quantitative Uniform Parent-Tightness Bound

## Theorem 18.1

對所有：

$$
L>C_1,
$$

有：

$$
\boxed{
1-C_J^{par}(L)
\le
C2^{-L}\mathfrak V_J.
}
$$

### Proof

由：

$$
P_J\ge R_J,
$$

得：

$$
\frac{P_J^{down}(L)}{P_J}
\le
\frac{P_J^{down}(L)}{R_J}.
$$

套入 Theorem 17.1：

$$
\frac{P_J^{down}(L)}{R_J}
\le
C2^{-L}
\frac{D_J}{R_J^2}
\sum_{k>J+1}2^kb_k
=
C2^{-L}\mathfrak V_J.
$$

$\square$

---

# 19. 第一個 Uniform Parent Tightness criterion

## Corollary 19.1

若沿某 PF-A edge family：

$$
\boxed{
\sup_J\mathfrak V_J
\le
K<\infty,
}
$$

則：

$$
\boxed{
\sup_J
\left(
1-C_J^{par}(L)
\right)
\le
CK2^{-L}.
}
$$

因此 parent-gap ledger uniformly tight。

特別：

$$
\boxed{
\sup_J\mathfrak V_J<\infty
\Longrightarrow
PT
}
$$

不再只是 subsequential classification，

而具有 quantitative exponential tail。

---

# 20. Parent escape 必付 budget divergence

## Corollary 20.1

若 RFP-03 的 classified subsequence落入：

$$
PS
$$

或：

$$
PE,
$$

則沿該 subsequence：

$$
\boxed{
\mathfrak V_J\to\infty.
}
$$

### Proof

若存在 bounded subsubsequence：

$$
\mathfrak V_J\le K,
$$

Theorem 18.1 對所有 $L$ 給 uniform：

$$
1-C_J^{par}(L)
\le
CK2^{-L}.
$$

先取 subsequential limit，

再令：

$$
L\to\infty,
$$

得到：

$$
\alpha_{par}=1,
$$

與：

$$
PS
\quad\text{或}\quad
PE
$$

矛盾。$\square$

---

# 21. Parent escape 的二重 debt

因：

$$
\mathfrak V_J
=
\mathfrak E_J\mathfrak O_J,
$$

若：

$$
PS
$$

或：

$$
PE
$$

持續，

必有：

$$
\boxed{
\mathfrak E_J\to\infty
\quad\vee\quad
\mathfrak O_J\to\infty
}
$$

至少沿 further subsequence。

亦即：

$$
\boxed{
\text{parent-gap escape}
\Longrightarrow
\text{dissipation/debt escape}
\vee
\text{output-depth escape}.
}
$$

這將一個 frequency-geometry escape再壓成兩個 scale-invariant budget escape。

---

# 22. Output-depth probability

定義：

$$
\boxed{
\pi_{J,k}
=
\frac{b_k^2}{R_J^2},
\qquad
k>J+1.
}
$$

則：

$$
\sum_{k>J+1}\pi_{J,k}=1.
$$

定義 cumulative output-depth mass：

$$
\boxed{
C_J^{out}(L)
=
\sum_{J+1<k\le J+L}
\pi_{J,k}.
}
$$

---

# 23. C4.3 — Output-Depth Tail Bound

## Theorem 23.1

對：

$$
L\ge2,
$$

有：

$$
\boxed{
1-C_J^{out}(L)
\le
2^{-2L}
\mathfrak O_J^2
}
$$

up to a harmless index-shift constant。

### Proof

對：

$$
k>J+L,
$$

有：

$$
b_k
\le
2^{-L}
2^{k-J}b_k.
$$

所以：

$$
\begin{aligned}
\left(
\sum_{k>J+L}b_k^2
\right)^{1/2}
&\le
\sum_{k>J+L}b_k
\\
&\le
2^{-L}
\sum_{k>J+L}
2^{k-J}b_k
\\
&\le
2^{-L}
R_J\mathfrak O_J.
\end{aligned}
$$

平方並除以：

$$
R_J^2
$$

即得。$\square$

---

# 24. Output escape 也必付 $\mathfrak O_J$

若：

$$
\sup_J\mathfrak O_J<\infty,
$$

則 output-depth distribution uniformly tight。

因此任何 complete output-depth escape都必迫使：

$$
\boxed{
\mathfrak O_J\to\infty.
}
$$

這解釋為何：

$$
\mathfrak O_J
$$

自然出現在 parent tightness criterion中。

---

# 25. 從 frequency 到 spacetime：不要先硬切 primal equation

若直接令：

$$
v=\chi u,
$$

localized field一般不再 divergence-free，

而方程會產生：

- cutoff forcing；
- diffusion commutators；
- advection boundary terms；
- pressure terms；
- divergence correction。

2026 年 quantitative forced N--S localization工作再次顯示：

$$
\boxed{
\text{localization is not a free operation}.
}
$$

因此本文採另一個順序：

$$
\boxed{
\text{first localize the dual certificate},
}
$$

而不是先宣稱得到一個新的 homogeneous local N--S equation。

---

# 26. Terminal partition of unity

固定：

$$
A\ge1.
$$

令 base core length：

$$
\boxed{
\ell_J
=
A2^{-J}.
}
$$

取 terminal smooth partition：

$$
\left\{
\chi^1_{J,a}
\right\}_{a\in\mathbb Z^3}
$$

使：

$$
0\le
\chi^1_{J,a}
\le1,
$$

$$
\boxed{
\sum_a
\chi^1_{J,a}(x)
=
1,
}
$$

且每個 terminal cell localized at diameter：

$$
O(\ell_J),
$$

並滿足：

$$
\|\nabla\chi^1_{J,a}\|_\infty
\le
CA^{-1}2^J.
$$

---

# 27. Backward adjoint partition

對每個：

$$
a,
$$

令：

$$
\chi_{J,a}(t,x)
$$

解：

$$
\boxed{
\partial_t\chi_{J,a}
+
u\cdot\nabla\chi_{J,a}
+
\nu\Delta\chi_{J,a}
=
0,
}
$$

for：

$$
s_J<t<t_J,
$$

以及：

$$
\chi_{J,a}(t_J,x)
=
\chi^1_{J,a}(x).
$$

這正是 C3-O 的 adjoint ancestry cutoff。

---

# 28. C4.4 — Adjoint Partition Preservation

## Theorem 28.1

對所有：

$$
s_J\le t\le t_J,
$$

有：

$$
\boxed{
0\le\chi_{J,a}(t,x)\le1,
}
$$

以及：

$$
\boxed{
\sum_a\chi_{J,a}(t,x)=1.
}
$$

### Proof

nonnegativity與 upper bound由 parabolic maximum principle。

令：

$$
\Xi_J
=
\sum_a\chi_{J,a}.
$$

線性方程使：

$$
\partial_t\Xi_J
+
u\cdot\nabla\Xi_J
+
\nu\Delta\Xi_J
=
0.
$$

terminal condition：

$$
\Xi_J(t_J)=1.
$$

常數 function $1$ 亦為同方程解。

由 uniqueness：

$$
\Xi_J\equiv1.
$$

$\square$

---

# 29. Soft ancestry tube

每個：

$$
\chi_{J,a}
$$

定義一條：

$$
\boxed{
\textbf{soft adjoint spacetime tube}.
}
$$

它：

- backward follow drift；
- backward diffuse；
- earlier times一般具有 tails；
- 不保持 compact support。

所以本文不使用：

$$
\text{hard material tube}
$$

這個語義。

---

# 30. Adjoint gradient distortion

令：

$$
\boxed{
\mathfrak D_J^{adj}
=
\exp
\left(
\int_{s_J}^{t_J}
\|\nabla u(r)\|_\infty\,dr
\right).
}
$$

smooth pre-singular interval上此量有限。

標準 gradient maximum estimate給：

$$
\boxed{
\|\nabla\chi_{J,a}(r)\|_\infty
\le
CA^{-1}2^J
\mathfrak D_J^{adj}.
}
$$

因此 terminal wavelength-sized cell向 earlier time回推時，

其 boundary steepness可能支付：

$$
\mathfrak D_J^{adj}
$$

distortion debt。

---

# 31. Exact spacetime-tube parent ledger

定義：

$$
\boxed{
\Lambda^{tube,(J)}_{a;k;p,q}
=
-
\int_{s_J}^{t_J}
\left\langle
\mathcal T_kF_{p,q}(r),
\chi_{J,a}(r)
\varphi_{J,k}(r)
\right\rangle dr.
}
$$

這個 ledger 同時保存：

$$
\boxed{
a,
\quad
k,
\quad
p,
\quad
q.
}
$$

其中：

- $a$：soft spacetime tube；
- $k$：output shell；
- $(p,q)$：ordered dyadic parents。

---

# 32. C4.5 — Exact Tube Refinement Identity

## Theorem 32.1

對所有：

$$
k,p,q,
$$

有：

$$
\boxed{
\sum_a
\Lambda^{tube,(J)}_{a;k;p,q}
=
\Lambda^{(J)}_{k;p,q}.
}
$$

因此：

$$
\boxed{
\sum_{a,k,p,q}
\Lambda^{tube,(J)}_{a;k;p,q}
=
R_J.
}
$$

### Proof

由 Theorem 28.1：

$$
\sum_a\chi_{J,a}(r,x)=1.
$$

代入 pairing 並使用 absolute convergence：

$$
\begin{aligned}
\sum_a
\Lambda^{tube}_{a;k;p,q}
&=
-
\int
\left\langle
\mathcal T_kF_{p,q},
\left(
\sum_a\chi_{J,a}
\right)
\varphi_{J,k}
\right\rangle dr
\\
&=
-
\int
\left\langle
\mathcal T_kF_{p,q},
\varphi_{J,k}
\right\rangle dr
\\
&=
\Lambda_{k;p,q}.
\end{aligned}
$$

再對：

$$
k,p,q
$$

求和。$\square$

---

# 33. 這一步沒有 localization forcing

Theorem 32.1 只是把：

$$
\text{dual test certificate}
$$

做 partition。

它沒有宣稱：

$$
\chi_{J,a}u
$$

滿足 homogeneous N--S。

因此目前：

$$
\boxed{
\text{no primal localization forcing has been hidden}.
}
$$

這是本文的重要 proof-order choice。

---

# 34. Tube positive / negative ledger

定義：

$$
P_J^{tube}
=
\sum_{a,k,p,q}
[\Lambda^{tube,(J)}_{a;k;p,q}]_+,
$$

$$
N_J^{tube}
=
\sum_{a,k,p,q}
[\Lambda^{tube,(J)}_{a;k;p,q}]_-.
$$

則：

$$
\boxed{
P_J^{tube}
-
N_J^{tube}
=
R_J.
}
$$

令：

$$
\boxed{
\zeta_J^{tube}
=
\frac{N_J^{tube}}{P_J^{tube}}.
}
$$

有：

$$
0\le\zeta_J^{tube}<1.
$$

---

# 35. C4.6 — Tube Witness / Multiplicity Dichotomy

## Theorem 35.1

固定：

$$
0<\theta<1.
$$

每個 PF-A edge滿足以下之一：

### TW — Strong spacetime parent witness

存在：

$$
(a;k;p,q)
$$

使：

$$
\boxed{
[\Lambda^{tube,(J)}_{a;k;p,q}]_+
\ge
\theta R_J.
}
$$

### TM — Spacetime-parent multiplicity debt

若無此 witness，

則 positive tube ledger至少含：

$$
\boxed{
\left\lceil
\frac{
1
}{
\theta
\left(
1-\zeta_J^{tube}
\right)
}
\right\rceil
}
$$

個 nonzero：

$$
(a;k;p,q)
$$

entries。

### Proof

與 RFP-03 Parent Witness / Multiplicity theorem相同，

只將 parent-output index：

$$
(k;p,q)
$$

升級為：

$$
(a;k;p,q).
$$

$\square$

---

# 36. Interpretation

現在：

$$
\text{no strong spacetime witness}
$$

不再只是 unresolved。

它必支付：

$$
\boxed{
\text{spatial-parent multiplicity debt}.
}
$$

因此 physical dispersion 本身開始成為可量化 escape mechanism。

---

# 37. 為何不能單獨把 $\mathbb P$ 當局部算子？

Leray projector：

$$
\mathbb P
$$

是 nonlocal order-zero Fourier multiplier。

raw pressure亦由：

$$
-\Delta p
=
\partial_i\partial_j
(u_i u_j)
$$

決定。

所以：

$$
\boxed{
[\chi,\mathbb P]
}
$$

不能被無條件視為小 local error。

本文的 canonical pressure-compatible operator不是：

$$
\mathbb P
$$

單獨，

而是：

$$
\boxed{
\mathcal T_k
=
\Delta_k\mathbb P\nabla\cdot.
}
$$

output band-pass恢復了 strong kernel localization。

---

# 38. Band-passed Leray kernel

$\mathcal T_k$ 的 Fourier symbol為：

$$
m_k(\xi)
=
\varphi(2^{-k}\xi)
\mathbb P(\xi)
(i\xi)\cdot.
$$

因：

$$
\varphi
$$

smooth 且 compactly supported away from：

$$
\xi=0,
$$

scaled symbol smooth。

故：

$$
\mathcal T_k
$$

具有 Schwartz kernel：

$$
\boxed{
K_k(x)
=
2^{4k}K(2^kx),
}
$$

其中：

$$
K
$$

為 Schwartz tensor kernel。

---

# 39. C4.7 — Pressure-Compatible Pseudolocality

## Theorem 39.1

對任意：

$$
N>0,
$$

存在：

$$
C_N<\infty
$$

使：

$$
\boxed{
\left\|
\mathbf 1_{\{|x|\ge R2^{-k}\}}
K_k
\right\|_{L^{3/2}}
\le
C_N
2^{2k}
(1+R)^{-N}.
}
$$

因此若 sets：

$$
E,
\quad
F
$$

滿足：

$$
\operatorname{dist}(E,F)
\ge
R2^{-k},
$$

則：

$$
\boxed{
\|
\mathbf 1_E
\mathcal T_k
(\mathbf 1_F G)
\|_3
\le
C_N
2^{2k}
(1+R)^{-N}
\|G\|_{3/2}.
}
$$

### Proof

由：

$$
K_k(x)=2^{4k}K(2^kx)
$$

與 Schwartz decay，

change variables：

$$
y=2^kx
$$

即得 kernel-tail bound。

再用 Young inequality：

$$
L^{3/2}*L^{3/2}
\to
L^3.
$$

$\square$

---

# 40. Pressure nonlocality 沒有消失

Theorem 39.1 不是說：

$$
p
$$

是 local。

它說：

$$
\boxed{
\text{after exact output band-pass, the full Leray nonlinear source is pseudolocal at wavelength }2^{-k}.
}
$$

raw pressure仍 nonlocal。

但：

$$
\Delta_k
\mathbb P\nabla\cdot
$$

保留 pressure與 incompressibility cancellation後，

其 annular kernel rapidly decays。

---

# 41. Raw pressure near/far split

對任意 smooth spatial cutoff：

$$
\eta
$$

定義 pair pressure：

$$
p_{p,q}
=
R_iR_j
\left(
u_{p,i}u_{q,j}
\right).
$$

拆：

$$
p_{p,q}
=
p_{p,q}^{near}
+
p_{p,q}^{far},
$$

其中：

$$
p_{p,q}^{near}
=
R_iR_j
\left(
\eta
u_{p,i}u_{q,j}
\right),
$$

$$
p_{p,q}^{far}
=
R_iR_j
\left(
(1-\eta)
u_{p,i}u_{q,j}
\right).
$$

在：

$$
\eta\equiv1
$$

的 interior region，

有：

$$
\boxed{
\Delta p_{p,q}^{far}=0.
}
$$

亦即 far pressure在 core中 harmonic。

---

# 42. Local pressure expansion 的角色

raw local pressure decomposition需要保存：

- Calderon--Zygmund near part；
- far-field harmonic / renormalized contribution；
- additive time-dependent pressure gauge。

因此：

$$
\boxed{
\text{pressure near/far split}
}
$$

與：

$$
\boxed{
\text{band-passed Leray pseudolocality}
}
$$

是互補 descriptions。

本文 parent ledger優先使用後者，

因為它和 exact frequency provenance：

$$
(k;p,q)
$$

直接相容。

---

# 43. Combined commutator

對 Lipschitz cutoff：

$$
\chi,
$$

有 exact identity：

$$
\boxed{
\chi\mathcal T_kF
=
\mathcal T_k(\chi F)
+
[\chi,\mathcal T_k]F.
}
$$

這裡：

$$
[\chi,\mathcal T_k]
=
\chi\mathcal T_k
-
\mathcal T_k\chi.
$$

---

# 44. C4.8 — Band-Passed Leray Commutator Estimate

## Theorem 44.1

對：

$$
F\in L^{3/2},
$$

有：

$$
\boxed{
\|
[\chi,\mathcal T_k]F
\|_3
\le
C
2^k
\|\nabla\chi\|_\infty
\|F\|_{3/2}.
}
$$

### Proof

由 kernel representation：

$$
[\chi,\mathcal T_k]F(x)
=
\int
K_k(x-y)
\left(
\chi(x)-\chi(y)
\right)
F(y)\,dy.
$$

Lipschitz bound：

$$
|\chi(x)-\chi(y)|
\le
\|\nabla\chi\|_\infty
|x-y|.
$$

而：

$$
\|
|x|K_k(x)
\|_{L^{3/2}}
\le
C2^k.
$$

Young inequality給結論。$\square$

---

# 45. Relative commutator scale

主 operator estimate：

$$
\|
\mathcal T_kF
\|_3
\lesssim
2^{2k}
\|F\|_{3/2},
$$

而 commutator：

$$
\|
[\chi,\mathcal T_k]F
\|_3
\lesssim
2^k
\|\nabla\chi\|_\infty
\|F\|_{3/2}.
$$

所以相對 tax為：

$$
\boxed{
2^{-k}
\|\nabla\chi\|_\infty.
}
$$

若 cutoff physical scale：

$$
\ell,
$$

則：

$$
\|\nabla\chi\|_\infty
\sim
\ell^{-1}.
$$

因此 tax約：

$$
\boxed{
(2^k\ell)^{-1}.
}
$$

也就是 inverse number of output wavelengths across cutoff width。

---

# 46. Adjoint tube commutator factor

對：

$$
\chi=\chi_{J,a}(r),
$$

由 Section 30：

$$
\|\nabla\chi_{J,a}(r)\|_\infty
\le
CA^{-1}2^J
\mathfrak D_J^{adj}.
$$

因此：

$$
\boxed{
2^{-k}
\|\nabla\chi_{J,a}(r)\|_\infty
\le
CA^{-1}
2^{J-k}
\mathfrak D_J^{adj}.
}
$$

因 ledger outputs滿足：

$$
k>J+1,
$$

得到：

$$
\boxed{
2^{-k}
\|\nabla\chi_{J,a}(r)\|_\infty
\le
CA^{-1}
\mathfrak D_J^{adj}.
}
$$

所以只要：

$$
A
$$

相對 adjoint distortion足夠大，

commutator可作 scale-compatible small tax。

---

# 47. Tube-local source ledger

定義：

$$
\boxed{
\Lambda^{loc,(J)}_{a;k;p,q}
=
-
\int_{s_J}^{t_J}
\left\langle
\mathcal T_k
\left(
\chi_{J,a}
F_{p,q}
\right),
\varphi_{J,k}
\right\rangle dr.
}
$$

此量明確要求 parent tensor source由 soft tube：

$$
\chi_{J,a}
$$

加權。

---

# 48. Commutator ledger

定義：

$$
\boxed{
\Lambda^{com,(J)}_{a;k;p,q}
=
-
\int_{s_J}^{t_J}
\left\langle
[\chi_{J,a},\mathcal T_k]
F_{p,q},
\varphi_{J,k}
\right\rangle dr.
}
$$

---

# 49. C4.9 — Exact Local-Source / Leakage Split

## Theorem 49.1

對每個：

$$
(a;k;p,q),
$$

有 exact identity：

$$
\boxed{
\Lambda^{tube,(J)}_{a;k;p,q}
=
\Lambda^{loc,(J)}_{a;k;p,q}
+
\Lambda^{com,(J)}_{a;k;p,q}.
}
$$

### Proof

由：

$$
\langle
\mathcal T_kF,
\chi\varphi
\rangle
=
\langle
\chi\mathcal T_kF,
\varphi
\rangle
$$

以及：

$$
\chi\mathcal T_kF
=
\mathcal T_k(\chi F)
+
[\chi,\mathcal T_k]F.
$$

積分即得。$\square$

---

# 50. Commutator tax estimate

由 Theorem 44.1 與 dual contraction：

$$
\boxed{
\begin{aligned}
\left|
\Lambda^{com,(J)}_{a;k;p,q}
\right|
\le
C
\frac{b_k}{R_J}
\int_{s_J}^{t_J}
2^k
\|\nabla\chi_{J,a}(r)\|_\infty
\|u_p(r)\|_3
\|u_q(r)\|_3
\,dr.
\end{aligned}
}
$$

這是完全 explicit 的 localization leakage tax。

---

# 51. C4.10 — Spacetime Parent Attachment Certificate

## Theorem 51.1

若某 tube-parent-output entry滿足：

$$
\Lambda^{tube,(J)}_{a;k;p,q}
\ge
\theta R_J
$$

for：

$$
\theta>0,
$$

且其 commutator tax滿足：

$$
\left|
\Lambda^{com,(J)}_{a;k;p,q}
\right|
\le
\varepsilon R_J
$$

with：

$$
0\le\varepsilon<\theta,
$$

則：

$$
\boxed{
\Lambda^{loc,(J)}_{a;k;p,q}
\ge
(\theta-\varepsilon)R_J.
}
$$

### Proof

由 exact split：

$$
\Lambda^{loc}
=
\Lambda^{tube}
-
\Lambda^{com}.
$$

所以：

$$
\Lambda^{loc}
\ge
\theta R_J
-
|\Lambda^{com}|
\ge
(\theta-\varepsilon)R_J.
$$

$\square$

---

# 52. 這是真正的 spatial attachment 到哪一步？

Theorem 51.1 證明：

$$
\boxed{
\text{a definite portion of the exact parent contribution is generated by the parent tensor inside one soft adjoint tube}.
}
$$

它比：

$$
\text{global-frequency parent}
$$

更強。

但還沒有證：

$$
u_p
$$

與：

$$
u_q
$$

各自具有唯一 nested physical core。

目前 attached object是：

$$
\boxed{
\chi_{J,a}
(u_p\otimes u_q).
}
$$

所以它是：

$$
\boxed{
\text{source-core attachment},
}
$$

不是完整：

$$
\boxed{
\text{individual-parent-core identity}.
}
$$

---

# 53. Parent co-location debt

由 Holder：

$$
\|
\chi_{J,a}
u_p\otimes u_q
\|_{3/2}
\le
\|
\chi_{J,a}^{1/2}u_p
\|_3
\|
\chi_{J,a}^{1/2}u_q
\|_3.
$$

因此若：

$$
\Lambda^{loc}_{a;k;p,q}
$$

具有 nontrivial lower bound，

則對應 weighted parent product不可能在整個 edge interval上一致過小。

所以至少得到：

$$
\boxed{
\text{source-core attachment}
\Longrightarrow
\text{parent co-location burden}.
}
$$

但本文不將此直接升格為：

$$
\Omega_p,
\Omega_q
$$

的唯一 ancestry cores。

---

# 54. Pressure-compatible no-go

若先把：

$$
\mathbb P
$$

與：

$$
\Delta_k
$$

拆開，

再分別宣稱：

$$
[\chi,\mathbb P]
$$

與：

$$
[\chi,\Delta_k]
$$

都 small，

可能丟失 annular cancellation。

本文正式採：

$$
\boxed{
G_{\rm BP}:
\quad
\text{localize the combined band-passed Leray source }
\Delta_k\mathbb P\nabla\cdot
\text{ before declaring pressure leakage small}.
}
$$

這不否定 classical commutator theory。

它只是指定 NS-RFP ancestry 的 canonical operator unit。

---

# 55. Comparison：raw localization真的會產生 forcing

若直接令：

$$
v=\chi u,
$$

則 formal calculation產生：

$$
\partial_tv
-
\nu\Delta v
+
\nabla\cdot(\chi u\otimes u)
+
\nabla(\chi p)
=
f_\chi,
$$

其中：

$$
\boxed{
f_\chi
=
(\partial_t\chi)u
-
2\nu\nabla\chi\cdot\nabla u
-
\nu(\Delta\chi)u
+
(u\cdot\nabla\chi)u
+
p\nabla\chi.
}
$$

而：

$$
\nabla\cdot v
=
u\cdot\nabla\chi.
$$

所以：

$$
\boxed{
\text{primal localization}
\neq
\text{homogeneous local Navier--Stokes}.
}
$$

這正是本文先 localize dual certificate 的原因。

---

# 56. Adjoint cancellation只適用特定 balance layer

C3-O 的 adjoint cutoff：

$$
\partial_t\chi
+
u\cdot\nabla\chi
+
\nu\Delta\chi
=
0
$$

可以 exact消掉 localized strain-energy balance中的 scalar：

$$
\partial_t\chi
+
u\cdot\nabla\chi
+
\nu\Delta\chi
$$

package。

但這不表示：

$$
f_\chi=0
$$

在 velocity localized equation中。

因此：

$$
\boxed{
\text{adjoint balance cancellation}
\neq
\text{zero primal localization forcing}.
}
$$

---

# 57. Two adjoints must not be conflated

本文同時有：

### Duhamel dual witness

$$
\varphi_{J,k}(r)
=
e^{\nu(t_J-r)\Delta}\phi_k.
$$

### Strain-balance / ancestry cutoff

$$
\partial_t\chi
+
u\cdot\nabla\chi
+
\nu\Delta\chi
=
0.
$$

前者是：

$$
\text{backward heat dual}.
$$

後者是：

$$
\text{backward transport-diffusion adjoint}.
$$

它們角色不同。

本文只使用 product：

$$
\chi_{J,a}\varphi_{J,k}
$$

作 source-time test。

新增 guard：

$$
\boxed{
G_{\rm 2ADJ}:
\quad
\text{heat dual and transport-diffusion adjoint must not be identified}.
}
$$

---

# 58. Pressure near/far 與 tube split 的對接

在一條 selected tube：

$$
a,
$$

可另取 smooth spatial cutoff：

$$
\eta_{J,a,R}
$$

在 tube effective core附近為：

$$
1,
$$

在更大 buffer外為：

$$
0.
$$

parent pressure拆成：

$$
p_{p,q}^{near,R}
+
p_{p,q}^{far,R}.
$$

far part在 inner core harmonic。

而 band-passed source：

$$
\mathcal T_k
$$

對 buffer外 source又有 Theorem 39.1 的 rapid decay。

所以 pressure escape必須支付至少一種：

$$
\boxed{
\text{large far-source norm}
}
$$

或：

$$
\boxed{
\text{large tube distortion / commutator tax}.
}
$$

本文不宣稱這兩者已被 universal bound排除。

---

# 59. Certified buffer radius

若在某 selected entry上有 gross source budget：

$$
\mathfrak S_{J,a;k,p,q}
$$

使 far contribution被估為：

$$
C_N
R^{-N}
\mathfrak S_{J,a;k,p,q}R_J,
$$

則要 certify far leakage不超過：

$$
\varepsilon R_J,
$$

充分條件是：

$$
\boxed{
R
\ge
\left(
\frac{
C_N
\mathfrak S_{J,a;k,p,q}
}{
\varepsilon
}
\right)^{1/N}.
}
$$

因此：

$$
\boxed{
\text{large gross source budget}
\Longrightarrow
\text{larger certified spatial buffer}.
}
$$

這是 source cancellation與spatial localization之間的 quantitative coupling。

---

# 60. Uniform parent tightness + tube witness

目前最接近完整 spacetime ancestry的 branch升級成：

$$
\boxed{
\mathrm{PF\mbox{-}A}
+
\sup_J\mathfrak V_J<\infty
+
TW
+
\text{small commutator tax}.
}
$$

其中：

$$
\sup_J\mathfrak V_J<\infty
$$

給 uniform frequency-parent tightness，

而：

$$
TW
$$

加 small commutator tax給 source-core attachment。

---

# 61. Remaining escape branches

若上述最乾淨 branch失敗，

至少必進入以下之一：

### E-V

$$
\boxed{
\mathfrak V_J\to\infty
}
$$

dissipation-output budget escape。

### E-TM

spacetime-parent multiplicity：

$$
\boxed{
\#\text{positive tube-parent witnesses}\to\infty
}
$$

或至少無 uniform strong witness。

### E-COM

$$
\boxed{
\text{commutator/localization leakage is order-one}.
}
$$

### E-ADJ

$$
\boxed{
\mathfrak D_J^{adj}\to\infty
}
$$

導致 soft tube severe distortion。

### E-PRESS

far pressure / far source需要 growing buffer才能 certify。

### E-PERSIST

即使每 edge有 good tube witness，

跨 edge無法串成 consistent ancestry path。

---

# 62. C4.11 — RFP-04 Proof-Space Enclosure

## Theorem 62.1

對任意 infinite PF-A first-passage edge sequence，

若：

1. $\mathfrak V_J$ uniformly bounded；
2. 存在 uniform $\theta>0$ 的 TW witnesses；
3. selected witness commutator taxes uniformly小於 $\varepsilon R_J$，其中 $\varepsilon<\theta$；

則：

$$
\boxed{
\text{parent frequency gaps are uniformly tight}
}
$$

且每個 selected edge存在：

$$
\boxed{
\text{a positive tube-local parent source contribution}.
}
$$

若這組 conclusion 無法維持，

則至少一項假設失敗，

即必進入：

$$
\boxed{
E\mbox{-}V
\vee
E\mbox{-}TM
\vee
E\mbox{-}COM
}
$$

或後續 persistence / pressure / adjoint distortion escape。

### Proof

uniform parent tightness由 Corollary 19.1。

tube-local positive source由 Theorem 51.1。

其餘為 exhaustive failure of the stated hypotheses。$\square$

---

# 63. 這不是 Full Chain Necessity

Theorem 62.1 尚未證：

$$
\boxed{
X_J
\to
X_{J+1}
}
$$

可跨所有 $J$ 串成同一條 persistent ancestry。

目前每個 edge可以選到不同：

$$
a,
\quad
k,
\quad
p,
\quad
q.
$$

所以剩下最核心的問題變成：

$$
\boxed{
\textbf{Witness Persistence / Chain Stitching}.
}
$$

---

# 64. 為何下一篇變成 graph compactness 問題？

RFP-02：

$$
\text{first-passage levels}.
$$

RFP-03：

$$
\text{exact parent-output edges}.
$$

RFP-04：

$$
\text{spacetime tube-parent edges}.
$$

所以我們現在自然得到一個 layered directed graph：

$$
\boxed{
\mathcal G^{RFP}
=
(V,E),
}
$$

其 levels由：

$$
J
$$

排序。

Full Chain Necessity接下來要求：

> 從每一層存在 admissible witness，提升成存在一條跨任意多層一致的 infinite ancestry path。

這不是單一 PDE estimate。

它同時是：

$$
\boxed{
\text{PDE legality}
+
\text{graph compactness}
+
\text{persistence}.
}
$$

---

# 65. 下一篇

正式下一篇改為：

$$
\boxed{
\textbf{NS-RFP 05 — Witness Persistence、Finite Branching 與 Infinite Ancestry Path Extraction}.
}
$$

核心問題：

1. 定義 edge compatibility；
2. 將 parent/output/tube witness串成 layered ancestry graph；
3. 研究 bounded multiplicity是否給 finite branching；
4. 使用 compactness / Konig-type infinity principle抽 infinite path；
5. 判定 multiplicity blow-up是否成為新的 escape debt；
6. 將 first-passage time ordering與 tube overlap加入 compatibility；
7. 明確分離：
   $$
   \text{a witness at every level}
   $$
   與：
   $$
   \text{one persistent witness chain}.
   $$

---

# 66. New guards

新增：

### $G_{\rm VISC}$

parent-gap escape必須保存：

$$
\mathfrak V_J
=
\mathfrak E_J\mathfrak O_J.
$$

不得將 PS / PE 當成無代價 frequency jump。

### $G_{\rm OUT}$

output-depth distribution必須保存：

$$
\pi_{J,k}.
$$

### $G_{\rm TUBE}$

spatial label必須來自 exact partition / localization certificate，

不得由視覺 proximity直接宣稱 ancestry。

### $G_{\rm BP}$

pressure-compatible localization以：

$$
\Delta_k\mathbb P\nabla\cdot
$$

為 canonical operator unit。

### $G_{\rm COM}$

tube-local source claim必須保存 commutator ledger。

### $G_{\rm 2ADJ}$

backward heat dual與transport-diffusion adjoint不得混同。

### $G_{\rm FORCE}$

primal cutoff equation產生的 forcing不得被隱藏。

---

# 67. Guard Library v3

因此：

$$
\boxed{
\mathcal G_{NS}^{(3)}
=
\mathcal G_{NS}^{(2)}
\cup
\{
G_{\rm VISC},
G_{\rm OUT},
G_{\rm TUBE},
G_{\rm BP},
G_{\rm COM},
G_{\rm 2ADJ},
G_{\rm FORCE}
\}.
}
$$

---

# 68. Standard-literature calibration

本文 framework與以下 classical / recent facts對接：

1. local pressure不能被當作純 local algebraic function；local pressure expansion本身需要正確的 mild/distributional framework；
2. localized smoothing與critical concentration結果提供真正 singularity core在 parabolic scales上的標準 PDE interface；
3. 2026 forced N--S quantitative work再次明確顯示 spatial localization會引入 forcing，且此 forcing在 quantitative Carleman estimates中需要獨立控制。

本文只把這些作為：

$$
\boxed{
\text{standard PDE compatibility checks}.
}
$$

Theorems 17.1--62.1 的 algebraic / harmonic-analysis core不依賴任何未驗證 2026 global claim。

---

# 69. Formal status ledger

$$
\boxed{
\begin{aligned}
\text{scale-invariant }\mathfrak E_J,\mathfrak O_J,\mathfrak V_J
&:\ \mathrm{DEFINED/VERIFIED},\\
\text{resonant downshift tail estimate}
&:\ \mathrm{PROVED},\\
\text{quantitative parent-tightness bound}
&:\ \mathrm{PROVED},\\
\sup_J\mathfrak V_J<\infty
\Rightarrow
\text{uniform parent tightness}
&:\ \mathrm{PROVED},\\
PS/PE
\Rightarrow
\mathfrak V_J\to\infty
&:\ \mathrm{PROVED\ along\ classified\ subsequence},\\
\text{output-depth tail bound}
&:\ \mathrm{PROVED},\\
\text{adjoint partition preservation}
&:\ \mathrm{PROVED},\\
\text{exact spacetime-tube parent ledger}
&:\ \mathrm{PROVED},\\
\text{tube witness/multiplicity dichotomy}
&:\ \mathrm{PROVED},\\
\text{band-passed Leray pseudolocality}
&:\ \mathrm{PROVED},\\
\text{band-passed Leray commutator estimate}
&:\ \mathrm{PROVED},\\
\text{exact local-source/leakage split}
&:\ \mathrm{PROVED},\\
\text{spacetime parent attachment certificate}
&:\ \mathrm{PROVED\ conditionally\ on\ small\ commutator\ tax},\\
\text{universal bound on }\mathfrak V_J
&:\ \mathrm{OPEN},\\
\text{uniform adjoint distortion bound}
&:\ \mathrm{OPEN},\\
\text{uniform strong tube witness}
&:\ \mathrm{OPEN},\\
\text{individual parent-core identity}
&:\ \mathrm{OPEN},\\
\text{witness persistence across levels}
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

# 70. 結論

RFP-03 的 frontier是：

$$
\boxed{
\text{can exact frequency provenance be made uniformly tight, persistent, and spatially attached?}
}
$$

RFP-04 對前兩個詞中的第一個，以及第三個，取得實質進展。

首先：

$$
\boxed{
1-C_J^{par}(L)
\le
C2^{-L}
\mathfrak E_J\mathfrak O_J.
}
$$

所以：

$$
\boxed{
\sup_J
\mathfrak E_J\mathfrak O_J
<
\infty
\Longrightarrow
\text{quantitative uniform parent tightness}.
}
$$

而任何：

$$
PS
\quad\text{或}\quad
PE
$$

escape都必迫使：

$$
\boxed{
\mathfrak E_J\mathfrak O_J
\to\infty.
}
$$

這將 uniform-tightness量詞缺口轉成 scale-invariant budget obstruction。

其次，使用 C3-O backward adjoint cutoff作 partition of unity：

$$
\boxed{
\Lambda_{k;p,q}
=
\sum_a
\Lambda^{tube}_{a;k;p,q},
}
$$

因此 exact parent provenance第一次升級成：

$$
\boxed{
(a;k;p,q)
}
$$

spacetime soft-tube provenance。

再利用 canonical band-passed Leray operator：

$$
\mathcal T_k
=
\Delta_k\mathbb P\nabla\cdot,
$$

得到：

$$
\boxed{
\Lambda^{tube}
=
\Lambda^{loc}
+
\Lambda^{com}.
}
$$

所以 pressure/localization nonlocality不再被藏掉，

而被集中為 explicit commutator / leakage tax。

若一個 strong tube witness的 tax small，

則：

$$
\boxed{
\text{exact parent frequency witness}
\Longrightarrow
\text{positive tube-local parent source}.
}
$$

因此 Chain Necessity 現在真正剩下的核心已經從：

$$
\text{Where is the source?}
$$

轉成：

$$
\boxed{
\textbf{Can good witnesses at arbitrarily high levels be stitched into one persistent infinite ancestry path?}
}
$$

這就是下一篇：

$$
\boxed{
\textbf{NS-RFP 05 — Witness Persistence、Finite Branching 與 Infinite Ancestry Path Extraction}.
}
$$

---

# References

1. J.-M. Bony, *Calcul symbolique et propagation des singularités pour les équations aux dérivées partielles non linéaires*, Annales scientifiques de l'École Normale Supérieure 14 (1981), 209–246.
2. L. Escauriaza, G. Seregin, V. Sverak, *$L_{3,\infty}$-solutions of Navier–Stokes equations and backward uniqueness*, Russian Mathematical Surveys 58 (2003), 211–250.
3. A. Cheskidov, P. Constantin, S. Friedlander, R. Shvydkoy, *Energy conservation and Onsager's conjecture for the Euler equations*, Nonlinearity 21 (2008), 1233–1252; arXiv:0704.0759.
4. Z. Bradshaw, Z. Grujic, *Frequency localized regularity criteria for the 3D Navier–Stokes equations*, Archive for Rational Mechanics and Analysis 224 (2017), 125–133; arXiv:1501.01043.
5. T. Barker, C. Prange, *Localized smoothing for the Navier–Stokes equations and concentration of critical norms near singularities*, Archive for Rational Mechanics and Analysis 236 (2020), 1487–1541; arXiv:1812.09115.
6. Z. Bradshaw, T.-P. Tsai, *On the local pressure expansion for the Navier–Stokes equations*, Journal of Mathematical Fluid Mechanics 24 (2022); arXiv:2001.11526.
7. T. Barker, H. Popkin, *Quantitative estimates for the forced Navier–Stokes equations and applications*, arXiv:2602.09951 (2026). Used as contemporary localization/forcing calibration; no global conclusion is imported into the present theorems.

# Internal dependencies

- `NS_RFP_01_SingularityFormationAncestry_FiniteObstruction_v0.1.md`
- `NS_RFP_02_CriticalUV_FirstPassage_SourceDebt_v0.1.md`
- `NS_RFP_03_DualWitness_ParentLedger_CarrierEscape_v0.1.md`
- `NS_C3O_AdjointCore_BalanceDynamicsSeparation_v0.2.md`
- `NS_ETN_XIntegration_Multiscale_NonCollapse_v0.1.md`
- `True ETN / 無限維張力場`
- `X_Integral_Unified_Program_v0.2.md`

# Next

$$
\boxed{
\textbf{NS-RFP 05 — Witness Persistence、Finite Branching 與 Infinite Ancestry Path Extraction}
}
$$
