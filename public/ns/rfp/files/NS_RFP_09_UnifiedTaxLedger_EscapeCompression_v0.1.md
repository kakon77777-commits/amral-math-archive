---
title: "Navier–Stokes Reverse Formation Program 09：Pressure/Far-Field、Adjoint Distortion、Interaction Efficiency 與 Unified Tax Ledger"
short_title: "NS-RFP 09"
version: "v0.1"
date: "2026-08-15"
author: "Neo.K / EveMissLab"
language: "zh-TW"
status: "Theorem-style escape compression / tax-compactness architecture"
epistemic_status: "Defines a finite scale-invariant core tax vector for the surviving RFP escape mechanisms; proves uniform selector bounds, collapses commutator and band-passed far-field escape into adjoint-distortion/interaction-efficiency taxes, derives parent-gap and plateau-gap bounds from earlier RFP estimates, and proves a bounded-tax certificate-compactness/path-closure theorem conditional on representation completeness and arbitrarily deep finite realizability. Does NOT prove that the core taxes are universally bounded, that every tax divergence is dynamically dangerous, Finite Obstruction, or Navier–Stokes regularity."
canonical_source: "UTF-8 Markdown"
---

# Navier–Stokes Reverse Formation Program 09

# Pressure/Far-Field、Adjoint Distortion、Interaction Efficiency 與 Unified Tax Ledger

## 0. 本文定位

RFP-01 到 RFP-08 已經把可能的 singularity-formation escape 從模糊的：

$$
\text{high-frequency blow-up}
$$

逐步拆成：

- first-passage source debt；
- exact parent provenance；
- parent-gap escape；
- spacetime tube leakage；
- witness atomization；
- persistence bottleneck；
- packet amplification；
- packet output-depth escape；
- memory-depth escape；
- temporal congestion；
- pressure/far-field leakage；
- adjoint distortion；
- interaction inefficiency。

到 RFP-08 為止，主要問題已經不再是：

> 還有哪些 escape 名稱？

而是：

> 這些 escape 是否其實只是少數幾個 scale-compatible loss-of-control variables 的不同投影？

本文回答：

$$
\boxed{
\textbf{YES, at the level of the current RFP certificate architecture.}
}
$$

我們建立一個 finite core tax vector：

$$
\boxed{
\mathbf T_n^{core}
}
$$

並證明目前大量 secondary escape coordinates可以由它統一控制或重新分類。

---

# 1. Tax 不是 blow-up driver 的同義詞

本文稱：

$$
\mathfrak T
$$

為 tax，

只表示：

$$
\boxed{
\text{某一 ancestry closure step 為了保持 uniform legality 必須付出的 quantitative cost}.
}
$$

因此：

$$
\mathfrak T_n\to\infty
$$

首先表示：

$$
\boxed{
\text{the corresponding closure mechanism loses uniform control}.
}
$$

它不自動表示：

$$
\boxed{
\text{this mechanism causes singularity}.
}
$$

特別：

- interaction inefficiency可能來自 nonlinear depletion；
- large omitted operator activity可能有 regularizing作用；
- pressure / localization tax可能只是 representation或certificate degradation。

新增 theorem-safety原則：

$$
\boxed{
\text{tax divergence}
\neq
\text{blow-up mechanism}.
}
$$

---

# 2. Typed tax classes

本文將 taxes分四型。

## Geometry taxes

控制 scale / carrier / parent geometry：

$$
\mathfrak T^{par},
\qquad
\mathfrak T^{depth}.
$$

## Provenance taxes

控制 witness / bridge / packet attribution：

$$
\mathfrak T^{atom},
\quad
\mathfrak T^{bridge},
\quad
\mathfrak T^{amp},
\quad
\mathfrak T^{int}.
$$

## Localization taxes

控制 moving tubes與 spatial leakage：

$$
\mathfrak T^{adj},
$$

以及由它衍生的：

$$
\mathfrak T^{com},
\quad
\mathfrak T^{far}.
$$

## History taxes

控制 old / fresh source history：

$$
\mathfrak T^{mem},
\qquad
\mathfrak T^{time}.
$$

---

# 3. Macro-edge convention

沿用 RFP-07 / 08 plateau-compressed PF-A macro skeleton：

$$
I_n=[T_n,T_{n+1}],
$$

以及 plateau-end base scale：

$$
K_n.
$$

每個 macro edge都有：

- positive local-source witness ledger；
- field packet family；
- packet bridge scores；
- age ledger；
- fresh-source lag ledger；
- adjoint spacetime tubes。

---

# 4. Strong-node atom

令 RFP-05 positive local-source probability為：

$$
\pi_n(w),
$$

且：

$$
\sum_w\pi_n(w)=1.
$$

定義 maximal node atom：

$$
\boxed{
a_n
=
\max_w
\pi_n(w).
}
$$

---

# 5. Core Tax 1 — Atomization tax

定義：

$$
\boxed{
\mathfrak T_n^{atom}
=
\frac1{a_n}.
}
$$

因：

$$
0<a_n\le1,
$$

有：

$$
\boxed{
1\le
\mathfrak T_n^{atom}
<
\infty
}
$$

on each finite smooth edge。

而：

$$
\mathfrak T_n^{atom}\to\infty
$$

正是 RFP-05 node atomization escape。

---

# 6. Canonical strong-node class

定義：

$$
\boxed{
\mathcal W_n^\star
=
\left\{
w:
\pi_n(w)\ge\frac{a_n}{2}
\right\}.
}
$$

此集合非空。

---

# 7. C9.1 — Strong-Node Cardinality Bound

## Theorem 7.1

有：

$$
\boxed{
|\mathcal W_n^\star|
\le
2\mathfrak T_n^{atom}.
}
$$

### Proof

每個：

$$
w\in\mathcal W_n^\star
$$

至少有 probability：

$$
a_n/2.
$$

而總和為：

$$
1.
$$

$\square$

---

# 8. Best predecessor bridge floor

對：

$$
w\in\mathcal W_{n+1}^\star,
$$

令：

$$
\boxed{
\beta_n(w)
=
\sup_v
\mathfrak b_n(v,w),
}
$$

其中 supremum遍歷 RFP-08 field packets。

再定義：

$$
\boxed{
\beta_n^\star
=
\inf_{w\in\mathcal W_{n+1}^\star}
\beta_n(w).
}
$$

---

# 9. Core Tax 2 — Bridge bottleneck tax

定義：

$$
\boxed{
\mathfrak T_n^{bridge}
=
\begin{cases}
1/\beta_n^\star,
&
\beta_n^\star>0,
\\
+\infty,
&
\beta_n^\star=0.
\end{cases}
}
$$

所以 bounded：

$$
\mathfrak T_n^{bridge}
$$

等價於：

> 每個 canonical strong child都有一個 field packet predecessor with uniform positive bridge floor。

---

# 10. Active bridge class

若：

$$
\beta_n^\star>0,
$$

定義：

$$
\boxed{
\mathscr B_n^\star
=
\left\{
(v,w):
w\in\mathcal W_{n+1}^\star,
\quad
\mathfrak b_n(v,w)
\ge
\frac{\beta_n^\star}{2}
\right\}.
}
$$

對每個：

$$
w\in\mathcal W_{n+1}^\star
$$

至少存在一個 active predecessor。

---

# 11. Packet amplification input

RFP-08 定義：

$$
\mathfrak A_n(v,w)
=
\frac{
\mathfrak b_n(v,w)
}{
q_n(v)
}.
$$

---

# 12. Core Tax 3 — Packet amplification tax

定義：

$$
\boxed{
\mathfrak T_n^{amp}
=
1+
\sup_{(v,w)\in\mathscr B_n^\star}
\mathfrak A_n(v,w).
}
$$

若：

$$
\mathscr B_n^\star=\varnothing,
$$

令：

$$
\mathfrak T_n^{amp}=+\infty.
$$

---

# 13. C9.2 — Active Packet Strength

## Theorem 13.1

對：

$$
(v,w)\in\mathscr B_n^\star,
$$

有：

$$
\boxed{
q_n(v)
\ge
\frac{
1
}{
2
\mathfrak T_n^{bridge}
\mathfrak T_n^{amp}
}.
}
$$

### Proof

active bridge給：

$$
\mathfrak b_n(v,w)
\ge
\frac1{
2\mathfrak T_n^{bridge}
}.
$$

而：

$$
\mathfrak A_n(v,w)
\le
\mathfrak T_n^{amp}.
$$

由：

$$
q_n(v)
=
\mathfrak b_n(v,w)
/\mathfrak A_n(v,w).
$$

$\square$

---

# 14. C9.3 — Uniform Predecessor Packet Count

## Theorem 14.1

所有 active predecessor packets都落在：

$$
\boxed{
\mathcal V_n^{pkt}
\left(
\frac1{
2
\mathfrak T_n^{bridge}
\mathfrak T_n^{amp}
}
\right).
}
$$

因此 distinct active predecessor packet數至多：

$$
\boxed{
2
\mathfrak T_n^{bridge}
\mathfrak T_n^{amp}.
}
$$

### Proof

套 RFP-08 packet-level finite cardinality theorem。$\square$

---

# 15. Core Tax 4 — Parent-tightness tax

沿用 RFP-04：

$$
\mathfrak V_n
$$

以及：

$$
1-C_n^{par}(L)
\le
C2^{-L}\mathfrak V_n.
$$

定義：

$$
\boxed{
\mathfrak T_n^{par}
=
1+\mathfrak V_n.
}
$$

---

# 16. C9.4 — Uniform Parent-Gap Selector

## Theorem 16.1

若：

$$
\mathfrak T_n^{par}\le K,
$$

則對任意：

$$
0<\varepsilon<1
$$

取：

$$
\boxed{
L_\varepsilon(K)
=
\left\lceil
\log_2
\left(
\frac{CK}{\varepsilon}
\right)
\right\rceil,
}
$$

即可保證：

$$
\boxed{
C_n^{par}
\left(
L_\varepsilon(K)
\right)
\ge
1-\varepsilon.
}
$$

$\square$

---

# 17. Core Tax 5 — Packet output-depth tax

沿用 RFP-08：

$$
\mathfrak O_n^{pkt}.
$$

定義：

$$
\boxed{
\mathfrak T_n^{depth}
=
1+\mathfrak O_n^{pkt}.
}
$$

---

# 18. C9.5 — Plateau Gap Bound from Taxes

## Theorem 18.1

假設：

$$
\mathfrak T_n^{bridge}
\le
K_B,
$$

$$
\mathfrak T_n^{amp}
\le
K_A,
$$

以及：

$$
\mathfrak T_n^{depth}
\le
K_O.
$$

若：

$$
w\in\mathcal W_{n+1}^\star
$$

由一個 active direct packet bridge跨越 macro plateau gap：

$$
G_n,
$$

則：

$$
\boxed{
G_n
\le
C_\ast
+
\log_2
\left(
2K_BK_AK_O
\right).
}
$$

### Proof

RFP-08 strong direct plateau bridge theorem給：

$$
\mathfrak O_n^{pkt}
\ge
\frac{\gamma}{A_0}
2^{G_n-C_\ast}.
$$

active bridge可取：

$$
\gamma
=
\frac1{2K_B},
$$

且：

$$
A_0\le K_A,
$$

$$
\mathfrak O_n^{pkt}\le K_O.
$$

移項即得。$\square$

---

# 19. Consequence：plateau depth 不是獨立 primitive tax

若：

$$
G_n\to\infty
$$

沿 strong direct-bridge branch，

則至少一個：

$$
\boxed{
\mathfrak T_n^{bridge},
\quad
\mathfrak T_n^{amp},
\quad
\mathfrak T_n^{depth}
}
$$

必 diverge。

因此 unbounded plateau crossing不需要另立第十個 primitive tax。

---

# 20. Core Tax 6 — Adjoint distortion

沿用 RFP-04：

$$
\mathfrak D_n^{adj}
=
\exp
\left(
\int_{I_n}
\|\nabla u(t)\|_\infty
dt
\right).
$$

定義：

$$
\boxed{
\mathfrak T_n^{adj}
=
\mathfrak D_n^{adj}.
}
$$

有：

$$
\mathfrak T_n^{adj}\ge1.
$$

---

# 21. Scaling audit of adjoint tax

Navier--Stokes scaling：

$$
u_\lambda(x,t)
=
\lambda
u(\lambda x,\lambda^2t)
$$

給：

$$
\nabla u_\lambda
=
\lambda^2
\nabla u(\lambda x,\lambda^2t),
$$

而：

$$
dt_\lambda
=
\lambda^{-2}dt.
$$

所以：

$$
\boxed{
\int
\|\nabla u\|_\infty dt
}
$$

scale invariant。

故：

$$
\boxed{
\mathfrak T^{adj}
}
$$

scale invariant。

---

# 22. Interaction efficiency

RFP-06 對 selected bridge entry定義 interaction envelope：

$$
\mathcal Q_n(v,w)
$$

與 positive bridge：

$$
[B_n(v\to w)]_+.
$$

定義：

$$
\boxed{
\mathfrak e_n(v,w)
=
\frac{
[B_n(v\to w)]_+
}{
\mathcal Q_n(v,w)
}
}
$$

when：

$$
\mathcal Q_n(v,w)>0.
$$

有：

$$
0\le
\mathfrak e_n(v,w)
\le1.
$$

---

# 23. Core Tax 7 — Interaction-inefficiency tax

對 active bridge class定義：

$$
\boxed{
\mathfrak T_n^{int}
=
\sup_{(v,w)\in\mathscr B_n^\star}
\frac1{
\mathfrak e_n(v,w)
}.
}
$$

若某 active bridge：

$$
\mathfrak e_n=0,
$$

令：

$$
\mathfrak T_n^{int}=+\infty.
$$

bounded：

$$
\mathfrak T^{int}
$$

表示：

> canonical interaction envelope中有 fixed fraction真正進入 selected positive bridge direction。

---

# 24. Tax type warning

$$
\mathfrak T_n^{int}\to\infty
$$

可以表示：

- cancellation；
- dual misalignment；
- transport depletion；
- interaction geometry不利於 selected source direction。

它未必是 singularity-danger tax。

所以：

$$
\boxed{
\mathfrak T^{int}
\text{ is a provenance-efficiency tax, not a monotone danger index}.
}
$$

---

# 25. Commutator envelope

沿用 RFP-04 canonical operator：

$$
\mathcal T_k
=
\Delta_k
\mathbb P\nabla\cdot.
$$

對 tube width parameter：

$$
A_{tube}\ge1,
$$

RFP-04 commutator estimate與 adjoint gradient bound給：

$$
\boxed{
\mathcal Q_n^{com}
\le
C
A_{tube}^{-1}
\mathfrak T_n^{adj}
\mathcal Q_n.
}
$$

這裡：

$$
\mathcal Q_n
$$

是 selected source的 canonical main interaction envelope。

---

# 26. C9.6 — Derived Commutator Share Bound

## Theorem 26.1

對 active bridge：

$$
(v,w),
$$

有：

$$
\boxed{
\frac{
\mathcal Q_n^{com}
}{
[B_n(v\to w)]_+
}
\le
C
A_{tube}^{-1}
\mathfrak T_n^{adj}
\mathfrak T_n^{int}.
}
$$

### Proof

由：

$$
[B]_+
=
\mathfrak e_n\mathcal Q_n
$$

與 Section 25：

$$
\frac{
\mathcal Q^{com}
}{
[B]_+
}
\le
C
A_{tube}^{-1}
\mathfrak T^{adj}
\frac1{\mathfrak e_n}.
$$

再用：

$$
1/\mathfrak e_n
\le
\mathfrak T^{int}.
$$

$\square$

---

# 27. Corollary：commutator escape不是獨立 primitive branch

若：

$$
\mathfrak T_n^{adj}
\le K_D,
$$

且：

$$
\mathfrak T_n^{int}
\le K_I,
$$

則任意：

$$
\varepsilon>0
$$

只需固定：

$$
\boxed{
A_{tube}
\ge
\frac{
CK_DK_I
}{
\varepsilon
}
}
$$

即可使 commutator envelope不超過 selected positive bridge的：

$$
\varepsilon
$$

fraction。

所以：

$$
\boxed{
\text{persistent order-one commutator escape}
}
$$

必迫使：

$$
\boxed{
\mathfrak T^{adj}
\to\infty
\quad\vee\quad
\mathfrak T^{int}
\to\infty
}
$$

若允許一次性選定 sufficiently wide tube。

---

# 28. Band-passed far-field envelope

RFP-04 pseudolocality給：

對任意：

$$
N_{dec}>0,
$$

若 source region距 output tube至少：

$$
R
$$

個 output wavelengths，

則：

$$
\boxed{
\mathcal Q_n^{far}(R)
\le
C_{N_{dec}}
(1+R)^{-N_{dec}}
\mathcal Q_n.
}
$$

---

# 29. C9.7 — Derived Far-Field Share Bound

## Theorem 29.1

對 active bridge：

$$
(v,w),
$$

有：

$$
\boxed{
\frac{
\mathcal Q_n^{far}(R)
}{
[B_n(v\to w)]_+
}
\le
C_{N_{dec}}
(1+R)^{-N_{dec}}
\mathfrak T_n^{int}.
}
$$

$\square$

---

# 30. Corollary：band-passed pressure/far escape被壓回 interaction tax

若：

$$
\mathfrak T_n^{int}\le K_I,
$$

則對任意：

$$
\varepsilon>0
$$

取 fixed dimensionless buffer：

$$
\boxed{
R_\varepsilon
\ge
\left(
\frac{
C_{N_{dec}}K_I
}{
\varepsilon
}
\right)^{1/N_{dec}}
}
$$

即可使 canonical band-passed far-source envelope低於 selected positive bridge的：

$$
\varepsilon
$$

share。

所以在：

$$
\Delta_k\mathbb P\nabla\cdot
$$

packet ledger中，

far pressure/source escape不是獨立 primitive tax。

---

# 31. Raw pressure warning

Section 30不表示：

$$
\boxed{
\text{raw pressure is local}.
}
$$

raw pressure由：

$$
-\Delta p
=
\partial_i\partial_j(u_iu_j)
$$

非局部決定，

far pressure在 local core中可保留 harmonic component。

本文結論只適用於：

$$
\boxed{
\text{canonical output-band-passed Leray source ledger}.
}
$$

因此 local pressure legality仍需 Bradshaw--Tsai 型 local pressure framework。

---

# 32. Full memory tail

固定：

$$
0<\varepsilon_{mem}<1/4.
$$

對 child：

$$
w
$$

定義 complete old-history tail：

$$
\boxed{
\operatorname{Tail}_{n,w}^{mem}(m)
=
\chi_n^{init}
+
\sum_{h\ge m}
\chi_{n,h}^{age}.
}
$$

---

# 33. Memory depth selector

定義：

$$
\boxed{
m_{n,w}(\varepsilon_{mem})
=
\inf
\left\{
m\ge1:
\operatorname{Tail}_{n,w}^{mem}(m)
\le
\varepsilon_{mem}
\right\}.
}
$$

若不存在，

令：

$$
m_{n,w}=+\infty.
$$

---

# 34. Core Tax 8 — Memory-depth tax

對 canonical strong child class：

$$
\mathcal W_n^\star
$$

定義：

$$
\boxed{
\mathfrak T_n^{mem}
=
1+
\sup_{w\in\mathcal W_n^\star}
m_{n,w}(\varepsilon_{mem}).
}
$$

---

# 35. Relation to RFP-08 viscous-age criterion

RFP-08 已證：

若：

$$
\sum_{h\ge m}
e^{-c\mathfrak a_{n,h}^{vis}}
\mathfrak G_{n,h}
$$

uniformly趨：

$$
0,
$$

則：

$$
\mathfrak T_n^{mem}
$$

uniformly bounded。

所以：

$$
\boxed{
\mathfrak T^{mem}\to\infty
}
$$

壓縮：

- viscous-age congestion；
- old-generation envelope growth；
- persistent initial reservoir contribution。

---

# 36. Normalized time-diagonal rate

固定：

$$
0<\delta_{fresh}<1/4.
$$

對 fresh-dominant child slot：

$$
\chi_n^{fresh}\ge\delta_{fresh},
$$

RFP-08定義：

$$
\mathcal S_{n,r},
\qquad
\mathcal C_{n,w}.
$$

令：

$$
\boxed{
\mathfrak R_{n,w}^{time}
=
\frac{
\|
\mathcal S_{n,r}
\|_{L^\infty(I_n)}
\|
\mathcal C_{n,w}
\|_{L^1(I_n)}
}{
\nu
2^{2r}
P_n^{age}(w)
}.
}
$$

若 fresh share低於：

$$
\delta_{fresh},
$$

本文令：

$$
\mathfrak R_{n,w}^{time}=0
$$

for tax purposes。

---

# 37. Core Tax 9 — Temporal-resolution tax

定義：

$$
\boxed{
\mathfrak T_n^{time}
=
1+
\sup_{w\in\mathcal W_n^\star}
\mathfrak R_{n,w}^{time}.
}
$$

---

# 38. Scaling audit of temporal tax

RFP-08 near-diagonal estimate：

$$
\frac{
|B_n^{near,\ell}|
}{
P_n^{age}
}
\le
\ell
\frac{
\|\mathcal S\|_\infty
\|\mathcal C\|_1
}{
P_n^{age}
}.
$$

令 normalized lag：

$$
\boxed{
\lambda
=
\nu2^{2r}\ell.
}
$$

則：

$$
\boxed{
\frac{
|B_n^{near,\ell}|
}{
P_n^{age}
}
\le
\lambda
\mathfrak R_{n,w}^{time}.
}
$$

因此：

$$
\mathfrak R^{time}
$$

dimensionless且 scale invariant。

---

# 39. C9.8 — Uniform Positive-Lag Selector

## Theorem 39.1

若：

$$
\chi_n^{fresh}\ge\delta_{fresh},
$$

且：

$$
\mathfrak T_n^{time}\le K_T,
$$

取：

$$
\boxed{
\lambda_0
=
\frac{
\delta_{fresh}
}{
2K_T
}.
}
$$

令：

$$
\ell_0
=
\frac{
\lambda_0
}{
\nu2^{2r}
}.
$$

則：

$$
\boxed{
[B_n^{sep,\ell_0}]_+
\ge
\frac{
\delta_{fresh}
}{2}
P_n^{age}.
}
$$

### Proof

near-diagonal absolute contribution至多：

$$
\lambda_0K_T
P_n^{age}
=
\frac{
\delta_{fresh}
}{2}
P_n^{age}.
$$

而：

$$
[B_n^{fresh}]_+
\ge
\delta_{fresh}P_n^{age}.
$$

所以 separated term保留至少一半。$\square$

---

# 40. Temporal congestion不再是獨立 name

若 fresh share保持：

$$
\ge\delta_{fresh},
$$

但不存在 fixed positive normalized lag的 separated source bridge，

則：

$$
\boxed{
\mathfrak T_n^{time}\to\infty.
}
$$

所以 near-diagonal temporal congestion被完全吸收到：

$$
\boxed{
\mathfrak T^{time}.
}
$$

---

# 41. Unified core tax vector

本文核心定義：

$$
\boxed{
\mathbf T_n^{core}
=
\left(
\mathfrak T_n^{atom},
\mathfrak T_n^{bridge},
\mathfrak T_n^{amp},
\mathfrak T_n^{par},
\mathfrak T_n^{depth},
\mathfrak T_n^{adj},
\mathfrak T_n^{int},
\mathfrak T_n^{mem},
\mathfrak T_n^{time}
\right).
}
$$

定義 max tax：

$$
\boxed{
\mathfrak T_n^{max}
=
\max_i
\mathfrak T_{n,i}^{core}.
}
$$

---

# 42. Scaling audit summary

九個 core taxes：

$$
\boxed{
\text{全部為 dimensionless scale-compatible quantities or dimensionless finite-depth counts}.
}
$$

具體：

- atomization：probability inverse；
- bridge：probability inverse；
- amplification：ratio；
- parent tax：RFP-04 scale invariant；
- packet depth：relative dyadic moment；
- adjoint：scale-invariant exponential strain integral；
- interaction：efficiency inverse；
- memory：macro-edge count；
- time：normalized parabolic lag-rate ratio。

---

# 43. Bounded-tax corridor

稱 macro ancestry落在：

$$
\boxed{
\textbf{bounded-tax corridor}
}
$$

若存在：

$$
K<\infty
$$

使所有 sufficiently large：

$$
n
$$

滿足：

$$
\boxed{
\mathfrak T_n^{max}
\le
K.
}
$$

---

# 44. C9.9 — Tax-to-Selector Compiler

## Theorem 44.1

假設：

$$
\mathfrak T_n^{max}\le K
$$

對所有 sufficiently large：

$$
n.
$$

則對任意 fixed：

$$
0<\varepsilon<1/4
$$

可以選擇以下 parameters independent of $n$：

### Strong-node count

$$
\boxed{
B_{node}
=
2K.
}
$$

### Active predecessor packet count

$$
\boxed{
B_{pkt}
=
2K^2.
}
$$

### Parent-gap radius

$$
\boxed{
L_\varepsilon
=
\left\lceil
\log_2
\left(
\frac{CK}{\varepsilon}
\right)
\right\rceil.
}
$$

### Direct plateau-gap bound

$$
\boxed{
G_{\max}
=
C_\ast
+
\left\lceil
\log_2(2K^3)
\right\rceil.
}
$$

### Tube width

$$
\boxed{
A_{tube,\varepsilon}
=
\left\lceil
\frac{
CK^2
}{
\varepsilon
}
\right\rceil.
}
$$

### Far-source buffer

for any chosen：

$$
N_{dec}>0,
$$

$$
\boxed{
R_{\varepsilon,N_{dec}}
=
\left(
\frac{
C_{N_{dec}}K
}{
\varepsilon
}
\right)^{1/N_{dec}}.
}
$$

### Memory depth

$$
\boxed{
m_{\max}
\le
K.
}
$$

up to the additive convention in：

$$
\mathfrak T^{mem}=1+m.
$$

### Fresh-source normalized lag

$$
\boxed{
\lambda_{\min}
=
\frac{
\delta_{fresh}
}{
2K
}.
}
$$

### Proof

各項依次來自 Theorems：

7.1、14.1、16.1、18.1、26.1、29.1，以及 tax definitions 34、37 與 Theorem 39.1。$\square$

---

# 45. 意義：bounded taxes給 uniform finite selectors

Theorem 44.1 將：

$$
\boxed{
\text{nine a priori moving escape parameters}
}
$$

編譯成：

$$
\boxed{
\text{one fixed finite collection of scale-independent selectors}.
}
$$

所以 bounded-tax corridor中：

- parent gap不能漂走；
- direct plateau gap不能漂走；
- tube width不必無限增加；
- far buffer不必無限增加；
- memory depth不必增加；
- fresh-source lag不必 collapse；
- strong node / packet branching不會爆炸。

---

# 46. Certificate compactness，不是 solution compactness

本文稱上述結果：

$$
\boxed{
\textbf{uniform certificate compactness}.
}
$$

它不表示：

$$
u_n
$$

在某 Banach space自動 precompact。

它只表示：

$$
\boxed{
\text{ancestry certificate所需的 discrete/relative localization parameters可以 uniform選定}.
}
$$

所以不得偷換成 PDE compactness theorem。

---

# 47. Derived tax dependency graph

目前 secondary escape可以壓成：

$$
\boxed{
\text{parent-gap escape}
\Rightarrow
\mathfrak T^{par}\to\infty,
}
$$

$$
\boxed{
\text{node atomization}
\Rightarrow
\mathfrak T^{atom}\to\infty,
}
$$

$$
\boxed{
\text{bridge bottleneck collapse}
\Rightarrow
\mathfrak T^{bridge}\to\infty,
}
$$

$$
\boxed{
\text{packet amplification escape}
\Rightarrow
\mathfrak T^{amp}\to\infty,
}
$$

$$
\boxed{
\text{packet / plateau depth escape}
\Rightarrow
\mathfrak T^{depth}
\to\infty
\vee
\mathfrak T^{amp}
\to\infty
\vee
\mathfrak T^{bridge}
\to\infty,
}
$$

$$
\boxed{
\text{commutator escape}
\Rightarrow
\mathfrak T^{adj}
\to\infty
\vee
\mathfrak T^{int}
\to\infty,
}
$$

$$
\boxed{
\text{band-passed far-source escape}
\Rightarrow
\mathfrak T^{int}\to\infty
}
$$

for fixed adjustable buffer semantics，

$$
\boxed{
\text{memory-depth escape}
\Rightarrow
\mathfrak T^{mem}\to\infty,
}
$$

以及：

$$
\boxed{
\text{temporal congestion}
\Rightarrow
\mathfrak T^{time}\to\infty.
}
$$

---

# 48. C9.10 — Escape-Name Compression Theorem

## Theorem 48.1

在 RFP-01--08 目前建立的 certificate semantics下，

若所有九個 core taxes uniformly bounded，

則以下 secondary escape labels不能作為 independent unbounded mechanisms持續：

- parent-gap escape；
- strong-node atomization；
- bridge bottleneck collapse；
- packet amplification escape；
- strong direct plateau-depth escape；
- commutator leakage escape；
- canonical band-passed far-source escape；
- infinite memory-depth escape；
- near-diagonal temporal congestion。

任何這些 escape若 persistence-level持續，

至少一個 core tax必 diverge。

$\square$

---

# 49. 但 converse 一般不成立

例如：

$$
\mathfrak T^{int}\to\infty
$$

可能代表 nonlinear depletion。

所以：

$$
\boxed{
\text{core tax divergence}
\not\Rightarrow
\text{dangerous singularity ancestry}.
}
$$

RFP-10 必須再區分：

$$
\boxed{
\text{dangerous dynamical escape}
}
$$

與：

$$
\boxed{
\text{certificate / depletion escape}.
}
$$

---

# 50. Bounded-tax graph

在 bounded-tax corridor，

取 canonical strong nodes：

$$
\mathcal W_n^\star.
$$

對每個 strong child，

有 predecessor bridge floor：

$$
\boxed{
\mathfrak b_n(v,w)
\ge
\frac1{2K}.
}
$$

而 active predecessor packet share：

$$
q_n(v)
\ge
\frac1{2K^2}.
$$

所以每層 candidate graph uniformly finite。

若 old/fresh channels存在，

Theorem 44.1 又將其編譯成：

- at most $K$ macro-edge memory；
- or fixed normalized positive time lag。

因此可建立 bounded-memory augmented graph。

---

# 51. Augmented node state

定義 augmented ancestry node：

$$
\boxed{
\widehat v_n
=
\left(
v_n,
m_n,
\lambda_n
\right),
}
$$

其中：

$$
0\le m_n\le K
$$

記 finite memory offset，

而：

$$
\lambda_n=0
$$

表示 completed-edge packet，

或：

$$
\lambda_n\ge\lambda_{\min}
$$

表示 hidden positive-lag subedge。

由 bounded-tax selectors，

每一 level 的 effective discrete ancestry choices仍 finite up to the declared tube/source packet indexing rules。

---

# 52. C9.11 — Bounded-Tax Path Closure Theorem

## Theorem 52.1

假設：

1. macro first-passage ancestry進入 bounded-tax corridor：
   $$
   \mathfrak T_n^{max}\le K;
   $$
2. RFP packet/tube representation對考慮的 singularity ancestry class complete；
3. 對任意：
   $$
   N<\infty,
   $$
   存在一條 depth-$N$ 的 tax-admissible finite realized ancestry；
4. pressure / localization使用本文 canonical band-passed Leray semantics。

則存在：

$$
\boxed{
\text{one infinite tax-admissible realized ancestry path}.
}
$$

### Proof

Theorem 44.1給 uniform：

- finite node count；
- finite predecessor packet count；
- finite parent / plateau gap；
- finite memory depth；
- positive time-lag floor；
- fixed localization buffer與 tube width。

所以 augmented certificate graph finitely branching。

由 assumption 3 有 arbitrarily deep finite paths。

套 RFP-05 finite-branching infinite-path extraction theorem。$\square$

---

# 53. 本 theorem 的真正地位

Theorem 52.1不是：

$$
\boxed{
\text{Navier--Stokes Chain Necessity proved}.
}
$$

因為：

- bounded-tax corridor尚未證 universal；
- representation completeness仍 open；
- arbitrarily deep tax-admissible finite realized paths需要由 actual blow-up hypothesis完整推出。

它完成的是：

$$
\boxed{
\text{if the nine taxes do not escape, the remaining quantifier/selector problem closes}.
}
$$

---

# 54. C9.12 — Finite Core-Tax Escape Alternative

## Theorem 54.1

假設：

- representation completeness成立；
- blow-up hypothesis已提供 arbitrarily deep finite RFP formation candidates；
- 但不存在 infinite realized ancestry path。

則至少一個 core tax不能保持 uniformly bounded：

$$
\boxed{
\limsup_{n\to\infty}
\mathfrak T_n^{max}
=
\infty.
}
$$

### Proof

反設：

$$
\sup_n
\mathfrak T_n^{max}<\infty.
$$

則由 Theorem 52.1 得 infinite path，

矛盾。$\square$

---

# 55. 這是有限 escape census，不是 Finite Obstruction

Theorem 54.1 只得到：

$$
\boxed{
\text{no infinite path}
\Longrightarrow
\text{some tax diverges}.
}
$$

真正 Finite Obstruction還需要：

$$
\boxed{
\text{每一種 tax divergence都被證明 dynamically impossible}
}
$$

或至少：

$$
\boxed{
\text{每一種 surviving divergence都可進一步導向 contradiction / regularity}.
}
$$

目前完全沒有做到這一步。

---

# 56. Tax vector as a dynamic state

因此 True ETN / X-Integration中的 ancestry state可新增：

$$
\boxed{
\Theta_n^{tax}
=
\mathbf T_n^{core}.
}
$$

完整 local formation state現在至少有：

$$
\boxed{
\Theta_n
=
\left(
\Theta_n^{bal},
\Theta_n^{op},
\Theta_n^{geo},
\Theta_n^{src},
\Theta_n^{prov},
\Theta_n^{tax}
\right).
}
$$

---

# 57. Tax provenance

每一個 tax必保存：

$$
\boxed{
\operatorname{Prov}
\left(
\mathfrak T_{n,i}
\right)
=
\left\langle
\text{definition},
\text{source ledger},
\text{normalization},
\text{scale audit},
\text{thresholds},
\text{status}
\right\rangle.
}
$$

不得只保存最後 scalar。

---

# 58. Threshold dependence

本文：

$$
\mathfrak T^{mem}
$$

依賴：

$$
\varepsilon_{mem},
$$

而：

$$
\mathfrak T^{time}
$$

依賴：

$$
\delta_{fresh}.
$$

這些 threshold必屬 certificate metadata，

不能在不同 edges間 silent change。

新增：

$$
\boxed{
G_{\rm TAXTHRESH}.
}
$$

---

# 59. Tax vector不可任意 scalarize

一般不能假設：

$$
\boxed{
\mathfrak T^{total}
=
\sum_i
\mathfrak T_i
}
$$

具有 intrinsic PDE meaning。

不同 taxes：

- type不同；
- monotonicity不同；
- 一些 divergence可能 regularizing；
- 一些只是 certificate loss。

所以第一版只保存：

$$
\boxed{
\mathbf T_n^{core}
}
$$

vector。

若需要 aggregate，

只能使用 task-specific monotone operator：

$$
\mathcal A_{\rm task}
\left(
\mathbf T_n^{core}
\right).
$$

---

# 60. Tax partial order

定義 componentwise order：

$$
\boxed{
\mathbf T
\preceq
\mathbf S
}
$$

若每一 core coordinate：

$$
T_i\le S_i.
$$

若一個 certificate theorem對 taxes monotone，

則：

$$
\mathbf S
$$

可 certify 的 parameter choice也適用於：

$$
\mathbf T.
$$

這使 tax space形成自然的 upward-danger / loss-of-control partial order，

但不是 blow-up probability order。

---

# 61. Tax fixed corridor

對：

$$
K<\infty,
$$

定義：

$$
\boxed{
\mathfrak C_K
=
\left\{
\mathbf T:
\mathfrak T^{max}\le K
\right\}.
}
$$

Theorem 44.1 對每個：

$$
\mathfrak C_K
$$

產生一套 fixed selectors。

因此：

$$
\boxed{
\mathfrak C_K
}
$$

是 certificate-level compact corridor。

---

# 62. Escape to the boundary

若：

$$
\mathfrak T_n^{max}\to\infty,
$$

稱：

$$
\boxed{
\mathbf T_n
\to
\partial_\infty
\mathfrak T
}
$$

即 tax state逃向 noncompact boundary。

RFP-10 的任務就是研究：

$$
\boxed{
\text{which boundary faces are dynamically realizable?}
}
$$

---

# 63. Boundary faces

第一版 boundary faces：

$$
\boxed{
F_{atom},
F_{bridge},
F_{amp},
F_{par},
F_{depth},
F_{adj},
F_{int},
F_{mem},
F_{time}.
}
$$

多個 coordinate可同時 diverge，

所以真正 escape可能落在 face intersections：

$$
F_i\cap F_j,
$$

甚至 higher-codimension corners。

---

# 64. 為何這比一長串 branches好？

舊 branch language：

$$
\text{pressure escape},
\quad
\text{commutator escape},
\quad
\text{plateau escape},
\quad
\text{memory escape},
\ldots
$$

容易重複計算同一現象。

例如本文已證：

$$
\text{commutator escape}
$$

在 canonical semantics下其實落在：

$$
F_{adj}
\cup
F_{int}.
$$

而：

$$
\text{far-source escape}
$$

落在：

$$
F_{int}
$$

或 raw-pressure representation outside the canonical packet ledger。

因此 tax boundary geometry能避免 branch duplication。

---

# 65. Standard PDE calibration I：pressure locality

Bradshaw--Tsai 的 local pressure expansion theorem說明：

whole-space distributional N--S solution的 local pressure expansion與 mildness之間存在精確關係。

這支持本文的 hard rule：

$$
\boxed{
\text{raw pressure localization需要獨立合法性，
不能被 band-passed pseudolocality取代。}
}
$$

---

# 66. Standard PDE calibration II：localization forcing

2026 Barker--Popkin 的 forced Navier--Stokes quantitative theory中，

localization誘導 forcing，

且 forcing在 Carleman estimates的大尺度上會被放大，

需要 additional Caccioppoli-type control。

這支持：

$$
\boxed{
\mathfrak T^{adj}
}
$$

與 localization / commutator tax必獨立記帳，

而不能因 cutoff smooth就自動宣稱 harmless。

---

# 67. Standard PDE calibration III：interaction depletion

Miller 的 strain--vorticity interaction工作證：

某些對 enstrophy growth pairing看似 orthogonal的 nonlinearity components仍可強烈改變 dynamics，

而 advection在特定 criteria下可以 depletion nonlinearity。

所以：

$$
\boxed{
\mathfrak T^{int}\to\infty
}
$$

可能是：

$$
\boxed{
\text{certificate inefficiency}
}
$$

甚至：

$$
\boxed{
\text{regularizing depletion},
}
$$

而不是 dangerous escape。

---

# 68. Standard PDE calibration IV：frequency window

Bradshaw--Grujic frequency-localized regularity criteria顯示：

possible singularity formation涉及一個 lower endpoint向：

$$
+\infty
$$

漂移的 relevant frequency window。

這與：

$$
\mathfrak T^{par},
\quad
\mathfrak T^{depth}
$$

作為 scale-relative tax相容，

但該 criterion不提供 ancestry genealogy。

---

# 69. 2026 finite-ledger calibration

2026 finite-scale critical-ledger與 structural-audit工作已將 persistent badness寫成：

$$
\boxed{
\text{supply}
+
\text{tax}
+
\text{leakage}
}
$$

並明確指出目前 obstruction calculus仍缺 coercive estimate排除 surviving obstruction。

RFP-09 與此相容：

本文統一的是：

$$
\boxed{
\text{formation certificate taxes},
}
$$

不是宣稱已經得到 coercive regularity inequality。

---

# 70. New guards

新增：

### $G_{\rm TAXTYPE}$

tax divergence不得自動稱為 dangerous mechanism。

### $G_{\rm TAXTHRESH}$

memory / time等 tax threshold metadata不可 silent change。

### $G_{\rm TAXVEC}$

tax vector不得無理由 scalarize成一個 total score。

### $G_{\rm RAWPRESS}$

band-passed far-field control不得偷換成 raw pressure locality。

### $G_{\rm DERIVED}$

commutator / far-field等 derived taxes若已由 primitive tax控制，

不得重複算成獨立 escape dimension。

---

# 71. Guard Library v8

因此：

$$
\boxed{
\mathcal G_{NS}^{(8)}
=
\mathcal G_{NS}^{(7)}
\cup
\{
G_{\rm TAXTYPE},
G_{\rm TAXTHRESH},
G_{\rm TAXVEC},
G_{\rm RAWPRESS},
G_{\rm DERIVED}
\}.
}
$$

---

# 72. RFP-09 對 Chain Necessity 的裁決

到本文為止，

若 formation ancestry一直留在 finite tax corridor：

$$
\boxed{
\sup_n
\mathfrak T_n^{max}
<
\infty,
}
$$

則：

- scale gaps uniform；
- packet branching uniform finite；
- localization buffers uniform；
- memory depth finite；
- fresh time lag positive；
- pressure/far packet leakage可 uniform控制；
- quantifier closure可交給 RFP-05。

因此：

$$
\boxed{
\text{bounded taxes}
\Longrightarrow
\text{certificate-level ancestry compactness}.
}
$$

如果完整 ancestry仍無法形成，

在 completeness assumptions下必有：

$$
\boxed{
\text{at least one core tax divergence}.
}
$$

---

# 73. 真正下一步

所以 RFP-10 不再需要重新推進 ancestry syntax。

它應該做：

$$
\boxed{
\textbf{Guard Library Consolidation}
+
\textbf{Tax-Boundary Escape Census}
+
\textbf{Finite Obstruction Candidates}.
}
$$

真正問題變成：

> 九個 boundary faces中，哪些已知可 regularize？
> 哪些可能 dangerous？
> 哪些可以由 energy / strain / pressure / viscosity inequality排除？
> 是否存在一個 finite family of dynamically complete obstructions hitting every tax-boundary escape？

---

# 74. Formal status ledger

$$
\boxed{
\begin{aligned}
\text{typed core tax vector}
&:\ \mathrm{DEFINED},\\
\text{strong-node finite bound}
&:\ \mathrm{PROVED},\\
\text{active packet strength / count}
&:\ \mathrm{PROVED},\\
\text{uniform parent-gap selector}
&:\ \mathrm{PROVED},\\
\text{plateau-gap tax bound}
&:\ \mathrm{PROVED},\\
\text{adjoint tax scaling}
&:\ \mathrm{PROVED},\\
\text{commutator share from adjoint + efficiency taxes}
&:\ \mathrm{PROVED\ within\ RFP\ envelope\ semantics},\\
\text{band-passed far-source share from efficiency tax}
&:\ \mathrm{PROVED},\\
\text{full memory-depth tax}
&:\ \mathrm{DEFINED},\\
\text{temporal-resolution tax}
&:\ \mathrm{DEFINED/SCALE\ AUDITED},\\
\text{uniform positive-lag selector}
&:\ \mathrm{PROVED},\\
\text{tax-to-selector compiler}
&:\ \mathrm{PROVED},\\
\text{escape-name compression}
&:\ \mathrm{PROVED\ relative\ to\ current\ RFP\ semantics},\\
\text{bounded-tax path closure}
&:\ \mathrm{PROVED\ CONDITIONALLY},\\
\text{finite core-tax escape alternative}
&:\ \mathrm{PROVED\ CONDITIONALLY},\\
\text{universal boundedness of core taxes}
&:\ \mathrm{OPEN},\\
\text{dynamic meaning of each divergent tax face}
&:\ \mathrm{OPEN},\\
\text{representation completeness}
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

# 75. 結論

RFP-09 將 RFP-01--08 累積的大量 escape branch壓縮成九個 core taxes：

$$
\boxed{
\mathbf T_n^{core}
=
\left(
\mathfrak T^{atom},
\mathfrak T^{bridge},
\mathfrak T^{amp},
\mathfrak T^{par},
\mathfrak T^{depth},
\mathfrak T^{adj},
\mathfrak T^{int},
\mathfrak T^{mem},
\mathfrak T^{time}
\right).
}
$$

其中：

$$
\boxed{
\text{commutator}
}
$$

不再是獨立 primitive escape，

因 bounded：

$$
\mathfrak T^{adj},
\quad
\mathfrak T^{int}
$$

允許 fixed tube width使其 uniformly small。

同樣，

canonical band-passed：

$$
\boxed{
\text{pressure / far-source leakage}
}
$$

在 bounded：

$$
\mathfrak T^{int}
$$

下可用 fixed wavelength buffer uniformly壓小。

bounded：

$$
\mathfrak T^{par}
$$

給 uniform parent tightness；

bounded：

$$
\mathfrak T^{bridge},
\quad
\mathfrak T^{amp},
\quad
\mathfrak T^{depth}
$$

給 finite packet branching與 bounded direct plateau gap；

bounded：

$$
\mathfrak T^{mem}
$$

給 finite generation memory；

bounded：

$$
\mathfrak T^{time}
$$

把 fresh source轉成 fixed normalized positive-lag ancestry。

因此：

$$
\boxed{
\sup_n
\mathfrak T_n^{max}
<
\infty
}
$$

會產生一個 uniform certificate corridor。

在 representation complete且 arbitrarily deep finite realization成立時，

RFP-05 compactness engine抽出：

$$
\boxed{
\text{one infinite realized ancestry path}.
}
$$

所以若 infinite ancestry仍失敗，

至少一個 core tax必逃向：

$$
+\infty.
$$

這不是 Finite Obstruction。

但它第一次把：

$$
\boxed{
\text{「奇點 formation 還可以往哪裡逃？」}
}
$$

壓成一個 finite-dimensional tax-boundary census：

$$
\boxed{
F_{atom},
F_{bridge},
F_{amp},
F_{par},
F_{depth},
F_{adj},
F_{int},
F_{mem},
F_{time}.
}
$$

下一篇真正開始研究：

$$
\boxed{
\text{which boundary faces are dynamically realizable, regularizing, or excludable?}
}
$$

這就是 RFP-10。

---

# References

1. Z. Bradshaw, T.-P. Tsai, *On the local pressure expansion for the Navier–Stokes equations*, Journal of Mathematical Fluid Mechanics 24 (2022); arXiv:2001.11526.
2. T. Barker, H. Popkin, *Quantitative estimates for the forced Navier–Stokes equations and applications*, arXiv:2602.09951 (2026).
3. E. Miller, *On the interaction of strain and vorticity for solutions of the Navier–Stokes equation*, Pure and Applied Analysis 8 (2026), 247–270; arXiv:2407.02691.
4. Z. Bradshaw, Z. Grujic, *Frequency localized regularity criteria for the 3D Navier–Stokes equations*, Archive for Rational Mechanics and Analysis 224 (2017), 125–133; arXiv:1501.01043.
5. A. Cheskidov, R. Shvydkoy, *A unified approach to regularity problems for the 3D Navier–Stokes and Euler equations: the use of Kolmogorov's dissipation range*, Journal of Mathematical Fluid Mechanics 16 (2014), 263–273; arXiv:1102.1944.
6. R. Yu, *Critical Ledgers and Scale-Defect Cascades for Navier–Stokes*, arXiv:2606.13887 (2026).
7. R. Yu, *Finite-Window Recursive Audit Chains for Navier–Stokes Generated Packages*, arXiv:2606.20899 (2026).
8. R. Yu, *A Structural Audit of Navier–Stokes Obstruction Calculus*, arXiv:2606.25341 (2026).

# Internal dependencies

- `NS_RFP_01_SingularityFormationAncestry_FiniteObstruction_v0.1.md`
- `NS_RFP_02_CriticalUV_FirstPassage_SourceDebt_v0.1.md`
- `NS_RFP_03_DualWitness_ParentLedger_CarrierEscape_v0.1.md`
- `NS_RFP_04_SpatialTube_PressureCompatible_UniformParentTightness_v0.1.md`
- `NS_RFP_05_WitnessPersistence_FiniteBranching_InfinitePath_v0.1.md`
- `NS_RFP_06_InterEdgeBridge_SourceStock_Bottleneck_v0.1.md`
- `NS_RFP_07_SynchronousPlateau_CarrierDepth_FastFront_v0.1.md`
- `NS_RFP_08_MemoryDepth_TimeResolution_PacketClosure_PlateauBridge_v0.1.md`
- `NS_C3O_AdjointCore_BalanceDynamicsSeparation_v0.2.md`

# Next

$$
\boxed{
\textbf{NS-RFP 10 — Guard Library Consolidation、Tax-Boundary Escape Census 與 Finite Obstruction Candidates}
}
$$
