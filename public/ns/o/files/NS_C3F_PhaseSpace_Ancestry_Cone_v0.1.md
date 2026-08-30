---
title: "Navier–Stokes C3-F：Phase-Space 準局部性、Ancestry Cone 與有限分枝反轉"
subtitle: "Quasi-Local Phase-Space Interactions, Parabolic Ancestry Cones, and Why Finite Branching Does Not Obstruct an Infinite Cascade"
version: "v0.1"
date: "2026-08-14"
author: "Neo.K / EveMissLab"
language: "zh-TW"
status: "Theorem-style structural reduction note"
epistemic_status: "Self-contained annular-kernel and ancestry lemmas + external regularity/concentration interfaces. Does NOT prove Navier–Stokes global regularity."
---

# Navier–Stokes C3-F
# Phase-Space 準局部性、Ancestry Cone 與有限分枝反轉

## 0. 本輪定位

C3-E 已將 local heterochiral survivor 壓成三個同時必要的結構：

$$
\boxed{
\text{fast viscous renewal}
+
\text{phase/amplitude efficiency}
+
\text{source-preserving genealogy}.
}
$$

其中每個高頻 renewal window具有：

$$
|I_q|
\lesssim
(\nu\lambda_q^2)^{-1},
$$

而 local production若要與 critical viscous scale競爭，必須：

$$
\eta_q A_q^{\rm crit}
\gtrsim
\nu.
$$

本輪第一次把 physical space 直接放進 proof route。

核心結果：

1. annular Leray nonlinearity 在 physical space具有 rapid off-diagonal decay；
2. local heterochiral production可分成有限半徑 core + 快速衰減 tail；
3. phase efficiency $\eta_q$ 決定需要保留多大的 spatial ancestry radius；
4. coherent local genealogy若尺度幾何增長，centers 必然收斂到單一空間點；
5. viscous windows 同時迫使 times 進入同一 parabolic spacetime cone；
6. finite branching本身**不是** obstruction；反而在 source-selection成立時有利於抽出 infinite ancestry ray；
7. 真正未閉合的是 **causal/time-oriented parenthood** 與 parent reuse/depletion。

---

# 1. Annular Leray critical operator

令：

$$
\Delta_q
$$

為標準 smooth Littlewood–Paley annular projector：

$$
|\xi|
\sim
\lambda_q,
\qquad
\lambda_q=2^q.
$$

令：

$$
D=\sqrt{-\Delta},
$$

以及 Leray projector：

$$
\mathbb P(\xi)
=
I-\frac{\xi\otimes\xi}{|\xi|^2}.
$$

考察作用在 tensor field $F$ 上的 operator：

$$
\boxed{
\mathcal T_qF
=
D\Delta_q
\mathbb P\nabla\cdot F.
}
$$

其 Fourier multiplier：

$$
m_q(\xi)
$$

支撐在 annulus：

$$
|\xi|\sim\lambda_q.
$$

因 annulus 遠離：

$$
\xi=0,
$$

Leray symbol 在此為 smooth。

operator總 differential order為：

$$
2.
$$

---

# 2. Kernel scaling

令：

$$
K_q
=
\mathcal F^{-1}m_q.
$$

由 dyadic scaling：

$$
\boxed{
K_q(x)
=
\lambda_q^5
K(\lambda_qx),
}
$$

其中：

$$
K\in\mathcal S(\mathbb R^3)
$$

為 Schwartz kernel。

因此：

$$
\boxed{
\|K_q\|_2
=
\lambda_q^{7/2}\|K\|_2.
}
$$

更重要地，對任意：

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
1_{\{|x|\ge R/\lambda_q\}}
K_q
\right\|_2
\le
C_N
\lambda_q^{7/2}
(1+R)^{-N}.
}
$$

這是 physical-space quasi-locality 的來源。

---

# 3. C3-F.1：Off-Diagonal Critical Interaction Lemma

令：

$$
f,g,h\in L^2(\mathbb R^3).
$$

假設：

$$
f\otimes g
$$

支撐於：

$$
A\subset\mathbb R^3,
$$

而：

$$
h
$$

支撐於：

$$
B\subset\mathbb R^3.
$$

令：

$$
d=\operatorname{dist}(A,B).
$$

則：

## 定理 3.1

對任意 $N$：

$$
\boxed{
\left|
\left\langle
h,
\mathcal T_q(f\otimes g)
\right\rangle
\right|
\le
C_N
\lambda_q^{7/2}
(1+\lambda_qd)^{-N}
\|f\|_2
\|g\|_2
\|h\|_2.
}
$$

### 證明

對：

$$
x\in B,
\qquad
y\in A,
$$

有：

$$
|x-y|\ge d.
$$

所以：

$$
\mathcal T_q(f\otimes g)(x)
=
\int_A
K_q(x-y)
(f\otimes g)(y)\,dy.
$$

由 Young / Cauchy–Schwarz：

$$
\|
1_B\mathcal T_q(f\otimes g)
\|_2
\le
\left\|
1_{\{|z|\ge d\}}K_q(z)
\right\|_2
\|f\otimes g\|_1.
$$

而：

$$
\|f\otimes g\|_1
\le
\|f\|_2\|g\|_2.
$$

再使用 kernel tail estimate即得。$\square$

---

# 4. Parent-overlap guard

如果 parents 使用 compactly-supported physical partition：

$$
f_Q=\chi_Qf,
$$

$$
g_{Q'}=\chi_{Q'}g,
$$

且：

$$
\operatorname{supp}\chi_Q
\cap
\operatorname{supp}\chi_{Q'}
=
\varnothing,
$$

則：

$$
\boxed{
f_Q\otimes g_{Q'}=0.
}
$$

所以 local quadratic interaction至少需要：

$$
\boxed{
\text{parent spatial supports overlap}.
}
$$

對 Schwartz / frame molecules而非 compact packets，exact zero改成 rapid decay。

---

# 5. Spatial packet grid

對 scale：

$$
\lambda_q,
$$

取 cubes：

$$
Q_{q,m},
\qquad
m\in\mathbb Z^3,
$$

side length：

$$
\ell_q
=
c\lambda_q^{-1}.
$$

取 smooth bounded-overlap partition：

$$
\sum_m\chi_{q,m}=1.
$$

定義 spatially localized shell pieces：

$$
u_{q,m}
=
\chi_{q,m}u_q.
$$

若要恢復 strict annular localization，可再施 slightly enlarged projector：

$$
\widetilde\Delta_q.
$$

本文稱此類 objects 為：

$$
\boxed{
\text{admissible dyadic packets}.
}
$$

---

# 6. Core radius

固定 dimensionless：

$$
R\ge1.
$$

對 output cube：

$$
Q_{q,m_3},
$$

稱 parent pair：

$$
(Q_{q,m_1},Q_{q,m_2})
$$

屬於 $R$-core，若：

1. parent supports overlap；
2. parent overlap region距 output cube不超過：

$$
R\lambda_q^{-1}.
$$

其餘 interaction稱：

$$
R\text{-tail}.
$$

---

# 7. Effective finite branching

因每個 cube side：

$$
O(\lambda_q^{-1}),
$$

固定半徑：

$$
R\lambda_q^{-1}
$$

內只有：

$$
O(R^3)
$$

個 spatial cubes。

又因 parent supports必須 overlap，每個 candidate parent cube只有：

$$
O(1)
$$

個 overlapping partners。

再乘：

- finite helicity signs；
- finite local dyadic offsets；
- 若需要，fixed finite angular-sector partition。

因此：

## 命題 7.1

對 fixed：

$$
R,
$$

以及 bounded scale-ratio local interactions，每個 output packet只有：

$$
\boxed{
M_R<\infty
}
$$

個 effective core parent tuples，其中：

$$
M_R
$$

與：

$$
q
$$

無關。

schematically：

$$
\boxed{
M_R=O(R^3)
}
$$

乘上一個固定的 frequency/helicity combinatorial factor。

---

# 8. Aggregate tail bound

令：

$$
U_q^2
=
\sum_m
\|u_{q,m}\|_2^2.
$$

由 bounded overlap：

$$
U_q
\asymp
\|u_q\|_2.
$$

把所有距離 output 超過：

$$
R\lambda_q^{-1}
$$

的 packet interactions相加。

由定理 3.1、bounded overlap與 discrete Young convolution，得到：

## 定理 8.1（Packet tail bound）

對任意：

$$
N>0,
$$

$$
\boxed{
|\mathcal R_q^{\rm tail}(R)|
\le
C_N
R^{-N}
\lambda_q^{7/2}
U_q^3.
}
$$

此量與 C3-E 的 maximal local amplitude capacity：

$$
\mathcal M_q
\lesssim
\lambda_q^{7/2}U_q^3
$$

具有相同 scaling。

所以：

$$
\boxed{
|\mathcal R_q^{\rm tail}(R)|
\le
C_N
R^{-N}
\mathcal M_q^{\rm scale}
}
$$

其中：

$$
\mathcal M_q^{\rm scale}
=
\lambda_q^{7/2}U_q^3.
$$

---

# 9. Phase efficiency回顧

C3-E 定義 actual positive local pair production：

$$
\mathcal P_q
$$

以及 amplitude capacity：

$$
\mathcal M_q.
$$

phase efficiency：

$$
\boxed{
\eta_q
=
\frac{\mathcal P_q}{\mathcal M_q}
\in[0,1].
}
$$

schematically：

$$
\mathcal M_q
\le
C_0
\mathcal M_q^{\rm scale}.
$$

---

# 10. C3-F.2：Locality–Coherence Tradeoff

若：

$$
\mathcal P_q>0,
$$

選：

$$
R_q
$$

使：

$$
C_NR_q^{-N}
\mathcal M_q^{\rm scale}
\le
\frac12\mathcal P_q.
$$

充分條件為：

$$
\boxed{
R_q
\ge
C_{N}'
\eta_q^{-1/N}.
}
$$

因此：

## 定理 10.1

對任意 $N$，存在常數 $C_N'$，使只要：

$$
R_q
\ge
C_N'\eta_q^{-1/N},
$$

則：

$$
\boxed{
\left[
\mathcal P_q
-
|\mathcal R_q^{\rm tail}(R_q)|
\right]
\ge
\frac12\mathcal P_q.
}
$$

亦即至少一半 actual positive local production 可以歸因到距離：

$$
\boxed{
O
\left(
\eta_q^{-1/N}
\lambda_q^{-1}
\right)
}
$$

內的 spatial parent core。

---

# 11. 意義

若 coherent route：

$$
\boxed{
\eta_q\ge\eta_0>0,
}
$$

則可固定：

$$
R_q=R_\ast
$$

與：

$$
q
$$

無關。

所以 positive production必須主要由：

$$
\boxed{
O(\lambda_q^{-1})
}
$$

physical neighborhood內的 parents形成。

如果：

$$
\eta_q\to0,
$$

所需 ancestry radius會擴張。

但因 kernel tail為 Schwartz：

$$
R^{-N}
$$

對所有 $N$ 都成立，

只要 $\eta_q$ 不以極端超多項式速度坍縮，spatial radius仍遠小於 macroscopic scale。

---

# 12. Core source-selection lemma

考慮一個 output packet $v$，其 signed/positive production magnitude：

$$
B_v>0.
$$

假設：

1. tail magnitude：

$$
|T_v^{\rm tail}|
\le
\varepsilon B_v,
\qquad
0\le\varepsilon<1;
$$

2. core parent tuple數：

$$
\#\mathcal A(v)\le M.
$$

3. core decomposition：

$$
B_v
\le
\left|
\sum_{\alpha\in\mathcal A(v)}
T_{v,\alpha}
+
T_v^{\rm tail}
\right|.
$$

則：

## 引理 12.1

存在：

$$
\alpha_\ast\in\mathcal A(v)
$$

使：

$$
\boxed{
|T_{v,\alpha_\ast}|
\ge
\frac{1-\varepsilon}{M}
B_v.
}
$$

### 證明

若所有：

$$
|T_{v,\alpha}|
<
\frac{1-\varepsilon}{M}B_v,
$$

則：

$$
\sum_\alpha
|T_{v,\alpha}|
<
(1-\varepsilon)B_v.
$$

加 tail：

$$
< B_v,
$$

與 output magnitude假設矛盾。$\square$

---

# 13. X-Integration 意義

若：

- local core dominance成立；
- phase efficiency足夠使 tail可吸收；
- output packet production有 threshold；

則：

$$
\boxed{
\text{每個 significant child
至少有一個 significant local parent tuple}.
}
$$

這把「scalar shell flux大」第一次提升成：

$$
\boxed{
\text{packet-level source certificate}.
}
$$

但仍需注意：

> tuple存在不等於已建立 time-oriented causal parenthood。

這是本輪後半的核心。

---

# 14. Local ancestry chain

假設我們已有一條 source-certified packet genealogy：

$$
v_0
\rightsquigarrow
v_1
\rightsquigarrow
v_2
\rightsquigarrow
\cdots
$$

其 characteristic scales：

$$
\lambda_0<\lambda_1<\lambda_2<\cdots,
$$

centers：

$$
x_0,x_1,x_2,\ldots
$$

以及 times：

$$
t_0<t_1<t_2<\cdots.
$$

假設 bounded local scale jump：

$$
\boxed{
r_-\lambda_n
\le
\lambda_{n+1}
\le
r_+\lambda_n
}
$$

for fixed：

$$
1<r_-\le r_+<\infty.
$$

---

# 15. Spatial ancestry displacement

由 local core：

$$
\boxed{
|x_{n+1}-x_n|
\le
C
\frac{R_n}{\lambda_n},
}
$$

其中：

$$
R_n
\sim
\eta_n^{-1/N}
$$

可由 locality–coherence tradeoff選取。

---

# 16. C3-F.3：Ancestry Center Convergence

## 定理 16.1

若：

$$
\sum_{n=0}^{\infty}
\frac{R_n}{\lambda_n}
<
\infty,
$$

則存在：

$$
x_\ast\in\mathbb R^3
$$

使：

$$
\boxed{
x_n\to x_\ast.
}
$$

且：

$$
\boxed{
|x_n-x_\ast|
\le
C
\sum_{m=n}^{\infty}
\frac{R_m}{\lambda_m}.
}
$$

### 證明

對：

$$
m>n,
$$

triangle inequality：

$$
|x_m-x_n|
\le
\sum_{j=n}^{m-1}
|x_{j+1}-x_j|
\le
C
\sum_{j=n}^{m-1}
\frac{R_j}{\lambda_j}.
$$

tail sum趨零，故 $(x_n)$ Cauchy。$\square$

---

# 17. Coherent route 的 sharp spatial cone

若：

$$
\eta_n\ge\eta_0>0,
$$

可取：

$$
R_n\le R_\ast.
$$

又：

$$
\lambda_n\ge\lambda_0r_-^n.
$$

所以：

$$
\sum_{m=n}^\infty
\lambda_m^{-1}
\le
C
\lambda_n^{-1}.
$$

因此：

## 推論 17.1

$$
\boxed{
|x_n-x_\ast|
\le
C'
\lambda_n^{-1}.
}
$$

也就是 packet ancestry自動壓進：

$$
\boxed{
B(x_\ast,C'\lambda_n^{-1}).
}
$$

---

# 18. Time ancestry

C3-E 的 viscous-window renewal給：

$$
\boxed{
0<t_{n+1}-t_n
\le
C_t
(\nu\lambda_n^2)^{-1}.
}
$$

由：

$$
\lambda_n\ge\lambda_0r_-^n
$$

可加總：

$$
\sum_n
(\nu\lambda_n^2)^{-1}
<
\infty.
$$

所以：

$$
t_n
$$

收斂到 finite：

$$
T_\infty.
$$

若此 chain代表 hypothetical terminal singular cascade，則：

$$
T_\infty=T_\ast.
$$

---

# 19. C3-F.4：Parabolic Ancestry Cone Theorem

## 定理 19.1

假設：

1. coherent route：
   $$
   \eta_n\ge\eta_0>0;
   $$
2. bounded local scale ratios；
3. local core ancestry；
4. viscous-window renewal。

則存在 spacetime endpoint：

$$
(x_\ast,T_\ast)
$$

使：

$$
\boxed{
|x_n-x_\ast|
\le
C_x\lambda_n^{-1},
}
$$

以及：

$$
\boxed{
0<T_\ast-t_n
\le
\frac{C_t'}{\nu\lambda_n^2}.
}
$$

因此：

$$
\boxed{
\lambda_n|x_n-x_\ast|
\le
C_x,
}
$$

$$
\boxed{
\nu\lambda_n^2(T_\ast-t_n)
\le
C_t'.
}
$$

hypothetical coherent genealogy 被迫進入一個 parabolic phase-space cone。

$\square$

---

# 20. 與 known spatial concentration 的關係

Barker–Prange 的 localized smoothing / concentration結果證明，在 Type-I 型 potential singularity 假設下，critical norms 必須在：

$$
R(t)
=
O(\sqrt{T_\ast-t})
$$

量級的 shrinking spatial balls內集中。

本文的 ancestry cone：

$$
|x_n-x_\ast|
\lesssim
\lambda_n^{-1},
$$

$$
T_\ast-t_n
\lesssim
(\nu\lambda_n^2)^{-1}
$$

形式上給：

$$
\lambda_n^{-1}
\sim
\sqrt{\nu(T_\ast-t_n)}.
$$

兩者幾何完全相容。

但：

$$
\boxed{
\text{本文 ancestry cone theorem 是 conditional genealogy theorem；
Barker--Prange concentration theorem有自己的 Type-I hypotheses。}
}
$$

兩者不能互相偷換。

---

# 21. CKN / $\varepsilon$-regularity interface

suitable weak solution在真正 singular spacetime point附近，不能在所有 sufficiently small parabolic cylinders中同時滿足任意給定的 $\varepsilon$-regularity smallness criterion。

因此 singular point可被理解成：

$$
\boxed{
\text{scale-invariant local regularity certificate
在所有小尺度持續失敗}.
}
$$

這與 X-Integration 的 language非常直接：

$$
\boxed{
\text{singularity}
=
\text{nested failure of local regularity guards}.
}
$$

本文不需要選唯一一個 $\varepsilon$-criterion；不同 known criteria可以作為不同 observation interfaces。

---

# 22. Finite branching 的直覺陷阱

我們可能希望：

> 每個 parent只有有限 children，因此無限 cascade不可能。

這是錯的。

考慮 rooted tree：

$$
\mathcal T.
$$

若：

1. root set有限；
2. 每個 node只有有限 children；
3. tree有 arbitrarily large depth；

則 Kőnig infinity lemma反而給出：

$$
\boxed{
\text{存在 infinite ray}.
}
$$

所以：

$$
\boxed{
\text{finite branching}
\not\Rightarrow
\text{finite genealogy}.
}
$$

---

# 23. C3-F.5：Finite-Branching Reversal

## 命題 23.1

若 packet-level source graph已滿足：

- finite root set；
- locally finite branching；
- every level contains a source-connected significant node；

則至少存在一條 infinite packet ancestry path。

所以 physical quasi-locality 的作用不是：

$$
\boxed{
\text{直接消滅 infinite path}.
}
$$

而是：

$$
\boxed{
\text{把模糊 aggregate cascade
壓成可抽取的 concrete genealogy}.
}
$$

這是非常重要的方向修正。

---

# 24. C1c 的新狀態

C1c 原本是：

$$
\boxed{
\mathrm{Blowup}
\stackrel{?}{\Rightarrow}
\text{persistent source-preserving genealogy}.
}
$$

現在可拆成：

### C1c-a — Static packet source selection

在 local-core dominance與tail absorption下：

$$
\boxed{
\text{significant child}
\Rightarrow
\text{significant local parent tuple}.
}
$$

本輪已給出 finite-core selection lemma。

### C1c-b — Infinite path extraction

若 source graph time-oriented且 locally finite：

$$
\boxed{
\text{arbitrarily deep source graph}
\Rightarrow
\text{infinite ancestry ray}.
}
$$

這是 discrete combinatorial theorem。

### C1c-c — Causal orientation

仍缺：

$$
\boxed{
\text{static nonlinear interaction tuple}
\Rightarrow
\text{genuine earlier-time parenthood}.
}
$$

這是目前最關鍵 gap。

---

# 25. 為什麼 static graph 可能 circular？

Navier–Stokes nonlinearity在同一時刻：

$$
t
$$

使用：

$$
u(t)\otimes u(t).
$$

若只畫：

$$
A\leftrightarrow B\to C
$$

的 instantaneous interaction graph，

可能出現：

$$
A\to B,
\qquad
B\to A
$$

等 simultaneous cycles。

這種 graph不是 causal DAG。

所以：

$$
\boxed{
\text{interaction}
\neq
\text{causal ancestry}.
}
$$

要真正建立 parenthood，必須使用：

$$
\boxed{
\text{Duhamel time ordering}.
}
$$

---

# 26. Duhamel causal source

對 output packet $v(t)$：

$$
v(t)
=
\text{linear inheritance}
+
\int_s^t
\operatorname{Source}[u(r),u(r)]\,dr.
$$

若 nonlinear integral很大，則：

$$
\int_s^t
\|\operatorname{Source}(r)\|\,dr
$$

必須很大。

因此至少存在：

$$
r<t
$$

使 instantaneous source non-negligible。

這給：

$$
\boxed{
\text{strictly earlier source time}.
}
$$

但 source at time $r$ 使用的 parent packets：

$$
u(r)
$$

本身可能在同一 short window中剛被 co-generated。

所以還必須追蹤：

$$
\boxed{
\text{first significant crossing times}
}
$$

或其他 monotone provenance marker，才能排除 circular parent reuse。

---

# 27. First-crossing strategy

對 packet amplitude functional：

$$
A_v(t)
$$

與 threshold：

$$
a_v>0,
$$

定義：

$$
\boxed{
\tau_v
=
\inf
\{
t:
A_v(t)\ge a_v
\}.
}
$$

若 child：

$$
v_c
$$

第一次跨 threshold於：

$$
\tau_c,
$$

真正 parent若要有 causal meaning，應要求：

$$
\boxed{
\tau_p<\tau_c.
}
$$

若所有 candidate high parents都只有：

$$
\tau_p\ge\tau_c,
$$

則 child crossing不能被這些 parents作為既有 source解釋。

此策略目前只是 proof program。

尚未建立 packet-amplitude differential inequality足以完成它。

---

# 28. Parent reuse problem

即使：

$$
\tau_p<\tau_c,
$$

同一 parent packet可能被 many children引用。

若 proof中把它每次都當成「全新可用 source」，可能產生 double counting。

X-Integration 要求保存：

$$
\boxed{
\text{source use history}.
}
$$

因此下一個真正 quantity不是單純 branching degree，而是：

$$
\boxed{
\operatorname{Reuse}(v_p)
=
\text{一個 parent packet可支持多少 cumulative child production}.
}
$$

如果能證：

$$
\operatorname{Reuse}(v_p)
$$

受 local energy / helicity / strain budget控制，就可能第一次得到不可重複的 ancestry resource。

---

# 29. Nested packet Zeno no-go

即使已經有 perfect parabolic ancestry：

$$
|x_n-x_\ast|
\sim
\lambda_n^{-1},
$$

$$
T_\ast-t_n
\sim
\lambda_n^{-2},
$$

它仍不和 global energy budget矛盾。

取 critical packet：

$$
A_n^{\rm crit}
=
\lambda_n^{1/2}U_n
\sim1.
$$

則：

$$
U_n^2
\sim
\lambda_n^{-1}.
$$

每代 ordinary energy dissipation over one viscous window：

$$
D_n
\sim
\nu
\lambda_n^2
U_n^2
\cdot
(\nu\lambda_n^2)^{-1}
\sim
\lambda_n^{-1}.
$$

若：

$$
\lambda_n
$$

幾何增長：

$$
\boxed{
\sum_nD_n<\infty.
}
$$

所以：

## No-Go 29.1

$$
\boxed{
\text{perfect space-frequency localization}
+
\text{parabolic Zeno timing}
+
\text{critical packet amplitude}
}
$$

仍可與 finite energy dissipation bookkeeping相容。

因此：

$$
\boxed{
\text{spatial concentration本身不是 regularity proof}.
}
$$

---

# 30. External frequency-localized interface

Bradshaw–Grujić 的 frequency-localized regularity criteria 顯示，在若干 function-space hypotheses下，possible singularity formation可以被壓到一個隨時間往高頻移動的有限 Littlewood–Paley window；若該關鍵 window在適當 times保持受控，solution可延拓。

本文不把這類 theorem直接用成 Clay proof。

它支持的只是研究定位：

$$
\boxed{
\text{追蹤一個 moving high-frequency frontier是標準 PDE 上合理的 reduction}.
}
$$

---

# 31. X-Integration：Phase-Space ancestry certificate

現在一個候選 parent-child edge 至少需要：

$$
\boxed{
\operatorname{XEdge}
=
\left\langle
q_p,m_p,s_p,t_p;
q_c,m_c,s_c,t_c;
\mathcal T;
\eta;
R;
\operatorname{Prov}
\right\rangle.
}
$$

守衛：

### G-FREQ

bounded scale ratio：

$$
q_c-q_p=O(1)
$$

對 local route。

### G-SPACE

$$
|x_c-x_p|
\lesssim
R\lambda_p^{-1}.
$$

### G-TIME

$$
t_p<t_c.
$$

### G-TAIL

far-field contribution已由：

$$
R^{-N}
$$

bound控制。

### G-CORE

至少一個 core parent tuple攜帶 fixed fraction source。

### G-HEL

helicity class合法。

### G-PHASE

actual signed production方向正確。

### G-REUSE

parent contribution不能無限制重複計數。

目前最未閉合的是：

$$
\boxed{
G\text{-TIME}
+
G\text{-REUSE}.
}
$$

---

# 32. True ETN 更新

N–S 的 ETN state अब不應只記：

$$
\Theta_q(t).
$$

更完整應記：

$$
\boxed{
\Theta_{q,m,s}(t)
}
$$

以及 relation：

$$
\boxed{
\Theta_{q_1,m_1,s_1}
\bowtie
\Theta_{q_2,m_2,s_2}
\longrightarrow
\Theta_{q_3,m_3,s_3}.
}
$$

每條 edge含：

- amplitude；
- phase；
- physical location；
- frequency；
- helicity；
- time；
- source debt；
- reuse history。

因此 True ETN 的「無限維張力場」在 N–S 這裡自然升級成：

$$
\boxed{
\textbf{a time-oriented phase-space tension hypergraph}.
}
$$

---

# 33. 新 frontier：C3-G

C3-F 的裁決不是：

> 找到 spatial locality，所以 regularity成立。

而是：

$$
\boxed{
\text{spatial quasi-locality使 genealogy可形式化；
但 genealogy存在本身不構成 contradiction}.
}
$$

真正下一關：

$$
\boxed{
\textbf{C3-G — Causal Packet Reuse and Depletion Rigidity}.
}
$$

---

# 34. C3-G proof obligations

## G1 — First-crossing causal lemma

建立 packet threshold crossing：

$$
\tau_v.
$$

證 significant child crossing必須有：

$$
\boxed{
\exists\text{ parent }p:
\tau_p<\tau_c.
}
$$

若不能，精確定位 simultaneous co-generation obstruction。

## G2 — Parent-use ledger

對 packet $p$ 定義：

$$
\operatorname{Use}_p
=
\sum_{c}
\text{source contribution }p\to c.
$$

找：

$$
\boxed{
\operatorname{Use}_p
\le
\text{depletion / strain / helicity budget of }p.
}
$$

## G3 — No-double-counting theorem

把 aggregate trilinear estimate改成 source-disjoint / orthogonal packet estimate，防止同一 parent energy被無限複製。

## G4 — Time-oriented finite-branching tree

若 G1–G3 成功，packet graph成真正 DAG/tree-like structure。

再使用 finite branching + arbitrary depth抽出：

$$
\boxed{
\text{one genuine infinite causal ancestry ray}.
}
$$

## G5 — Depletion along ray

最後研究：

$$
\boxed{
\text{one parent}
\to
\text{child}
}
$$

是否必須留下不可回收 depletion。

若每代有正的 normalized depletion，才可能形成真正 obstruction。

---

# 35. 正式狀態

$$
\boxed{
\begin{aligned}
\text{annular Leray kernel Schwartz localization}
&:\ \mathrm{PROVED/STANDARD},\\
\text{off-diagonal critical interaction decay}
&:\ \mathrm{PROVED},\\
\text{finite effective core branching}
&:\ \mathrm{PROVED\ for\ admissible\ packetization},\\
\text{packet tail }R^{-N}\text{ bound}
&:\ \mathrm{PROVED},\\
\text{locality--coherence tradeoff}
&:\ \mathrm{PROVED},\\
\text{core source-selection lemma}
&:\ \mathrm{PROVED},\\
\text{ancestry center convergence}
&:\ \mathrm{PROVED\ CONDITIONAL},\\
\text{parabolic ancestry cone}
&:\ \mathrm{PROVED\ CONDITIONAL},\\
\text{finite branching as obstruction}
&:\ \mathrm{FALSE/NO\mbox{-}GO},\\
\text{finite branching helps infinite-ray extraction}
&:\ \mathrm{PROVED\ COMBINATORIAL},\\
\text{static packet parenthood}
&:\ \mathrm{PARTIALLY\ CLOSED},\\
\text{causal time-oriented parenthood}
&:\ \mathrm{OPEN},\\
\text{parent reuse/depletion rigidity}
&:\ \mathrm{OPEN}.
\end{aligned}
}
$$

---

# 36. 結論

本輪第一次把：

$$
\text{frequency}
$$

與：

$$
\text{physical space}
$$

在 exact N–S nonlinear operator level接起來。

band-limited Leray nonlinearity的 kernel滿足：

$$
\boxed{
\text{off-diagonal decay faster than any power of }
\lambda\,d.
}
$$

因此 coherent local pair production不能依賴任意遙遠的 physical parents。

若：

$$
\eta_q\gtrsim1,
$$

真正 production core被壓在：

$$
\boxed{
O(\lambda_q^{-1})
}
$$

的 spatial neighborhood。

搭配：

$$
O((\nu\lambda_q^2)^{-1})
$$

viscous time，

任何 geometric-scale coherent ancestry都被迫收斂到：

$$
\boxed{
(x_\ast,T_\ast)
}
$$

的 parabolic cone。

但這仍不是 contradiction。

甚至 finite branching也不能救我們：

$$
\boxed{
\text{若 arbitrarily deep合法 nodes已存在，
finite branching反而有利於抽出 infinite ray}.
}
$$

所以真正未解之處已經變得極精確：

$$
\boxed{
\text{instantaneous interaction graph
如何升級成
strictly time-oriented, non-double-counted causal genealogy？}
}
$$

下一輪：

$$
\boxed{
\textbf{C3-G — Causal Packet Reuse and Depletion Rigidity}
}
$$

正式攻：

$$
\boxed{
\text{first crossing}
+
\text{parent reuse}
+
\text{depletion}
+
\text{no double counting}.
}
$$

---

# References

1. H. Aluie, G. L. Eyink, *Localness of energy cascade in hydrodynamic turbulence, I. Smooth coarse-graining*, arXiv:0909.2386.
2. H. Aluie, G. L. Eyink, *Localness of energy cascade in hydrodynamic turbulence, II. Sharp spectral filter*, arXiv:0909.2451.
3. T. Barker, C. Prange, *Localized smoothing for the Navier–Stokes equations and concentration of critical norms near singularities*, arXiv:1812.09115.
4. T. Barker, C. Prange, *Quantitative regularity for the Navier–Stokes equations via spatial concentration*, arXiv:2003.06717.
5. Z. Bradshaw, Z. Grujić, *Frequency localized regularity criteria for the 3D Navier–Stokes equations*, arXiv:1501.01043.
6. I. Gallagher, G. S. Koch, F. Planchon, *A profile decomposition approach to the $L^\infty_t(L^3_x)$ Navier–Stokes regularity criterion*, arXiv:1012.0145.
7. C. E. Kenig, G. S. Koch, *An alternative approach to regularity for the Navier–Stokes equations in critical spaces*, arXiv:0908.3349.

# Internal dependencies

- `NS_C1_UV_Replenishment_Chain_v0.2.md`
- `NS_C2_Critical_Toll_Spike_Packing_v0.3.md`
- `NS_C3A_Conservation_Criticality_Helical_Pair_Production_v0.1.md`
- `NS_C3B_BiHelical_Equalization_UniqueSign_UV_Escape_v0.1.md`
- `NS_C3C_ClassII_Nonlocality_Tax_Radial_Congestion_v0.1.md`
- `NS_C3D_CutoffFlux_HelicalKernel_Nonlocality_v0.1.md`
- `NS_C3E_ViscousWindow_PhaseEfficiency_Zeno_v0.1.md`
- `True ETN / 無限維張力場`
- `X_Integral_Unified_Program_v0.2.md`

Next:

$$
\boxed{
\textbf{C3-G — Causal Packet Reuse and Depletion Rigidity}
}
$$
