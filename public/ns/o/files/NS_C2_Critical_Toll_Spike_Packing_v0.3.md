---
title: "Navier–Stokes C2：臨界通行費、耗散波數尖峰打包與尺度盲預算 No-Go"
subtitle: "Critical Tolls, Dissipation-Wavenumber Spike Packing, and Why Additive Energy Budgets Do Not Yet Close Blow-up"
version: "v0.3"
date: "2026-08-14"
author: "Neo.K / EveMissLab"
language: "zh-TW"
status: "Theorem-style reduction / no-go research note"
epistemic_status: "External theorems + self-contained scaling lemmas + abstract scalar-ledger no-go. Does NOT prove Navier–Stokes regularity."
---

# Navier–Stokes C2：臨界通行費、耗散波數尖峰打包與尺度盲預算 No-Go

## 0. 本輪目標

上一輪已閉合：

$$
\mathrm{C1a}:
\quad
\mathrm{Blowup}(T_\ast)
\Rightarrow
\forall J,\
\limsup_{t\uparrow T_\ast}
\|P_{>J}u(t)\|_{L^3}
=
\infty,
$$

以及：

$$
\mathrm{C1b}:
\quad
\mathrm{Blowup}(T_\ast)
\Rightarrow
\exists
(J_n,t_n,\mathcal N_n)
$$

滿足：

$$
J_n\uparrow\infty,
\qquad
t_n\uparrow T_\ast,
\qquad
\|\mathcal N_n\|_3\to\infty.
$$

因此 hypothetical blow-up 必須在愈來愈高頻率上反覆取得 nonlinear UV replenishment。

原先 C2 的直覺是：

> 每一次 replenishment 是否都必須支付一個正的 cost，而 total budget 有限，從而導致矛盾？

本輪的結論是：

$$
\boxed{
\text{有 critical per-scale toll，但最自然的 additive energy budget 不足以關閉。}
}
$$

更精確地，本輪建立：

1. dissipation-wavenumber 的 $L^1/L^{5/2}$ squeeze；
2. dyadic spike-packing law；
3. high-shell critical toll 的必要性；
4. quadratic Sobolev cost 的 scaling no-go；
5. 一個抽象 geometric cascade ledger，證明目前 scalar budgets 彼此相容；
6. 因此主線必須從「scalar additive cost」升級為「cross-scale structural rigidity」。

---

# 1. 問題設定

考慮：

$$
\partial_tu-\nu\Delta u+(u\cdot\nabla)u+\nabla p=0,
$$

$$
\nabla\cdot u=0
$$

於：

$$
\mathbb R^3\times[0,T_\ast).
$$

假設 $u$ 是由光滑、快速衰減 initial data 產生的 maximal classical solution。

整篇仍採反證式研究：

$$
0<T_\ast<\infty
$$

是假想 finite singular time。

使用 dyadic shells：

$$
u_q=\Delta_qu,
\qquad
\lambda_q=2^q.
$$

---

# 2. 外部輸入 A：dissipation wavenumber

Cheskidov–Shvydkoy 對 3D Navier–Stokes 定義 time-dependent dissipation wavenumber：

$$
\boxed{
\Lambda(t)
=
\min
\left\{
\lambda_q:
\lambda_p^{-1}
\|u_p(t)\|_\infty
<
c_0\nu,
\quad
\forall p>q
\right\}.
}
$$

令：

$$
\Lambda(t)=\lambda_{Q(t)}.
$$

其直觀意義為：

- $q\le Q(t)$：可能仍有 nonlinear/inertial dynamics；
- $q>Q(t)$：shell amplitude 已小到 viscosity 可吸收 nonlinear term。

對本文最重要的兩個外部結果是：

### External-A1

對 Leray–Hopf solution：

$$
\boxed{
\Lambda\in L^1(0,T)
}
$$

對任意 finite $T$ 成立。

### External-A2

若：

$$
\boxed{
\Lambda\in L^{5/2}(0,T),
}
$$

則 solution regular up to $T$。

因此若真的在 $T_\ast$ blow up：

$$
\boxed{
\Lambda
\in
L^1(0,T_\ast)
\setminus
L^{5/2}(0,T_\ast).
}
$$

這是一個嚴格的必要條件。

---

# 3. C2a：Dissipation-Wavenumber Squeeze

## 定理 3.1（Conditional blow-up envelope squeeze）

假設 $T_\ast<\infty$ 是 maximal finite singular time。

則：

$$
\boxed{
\int_0^{T_\ast}\Lambda(t)\,dt<\infty,
}
$$

但：

$$
\boxed{
\int_0^{T_\ast}\Lambda(t)^{5/2}\,dt=\infty.
}
$$

### 證明

第一式由 External-A1。

若第二式有限，則：

$$
\Lambda\in L^{5/2}(0,T_\ast),
$$

由 External-A2，solution regular through $T_\ast$，與 maximal blow-up 假設矛盾。

故第二式必發散。$\square$

---

# 4. ETN 解讀：尖峰而非單調爆炸

定理 3.1 不要求：

$$
\Lambda(t)
$$

單調增加。

它只要求假想 blow-up 的 envelope 同時滿足：

$$
\Lambda\in L^1
$$

與：

$$
\Lambda\notin L^{5/2}.
$$

所以一條可疑 trajectory 必須具有：

$$
\boxed{
\text{high-amplitude + short-duration + increasingly concentrated spikes}.
}
$$

這非常符合 True ETN 的語言：

> tension amplitude 可以極高，但若 persistence window 同時縮短，低階總帳仍可能有限。

所以「最大張力高」與「總張力預算耗盡」不是同一命題。

---

# 5. C2b：Dyadic Spike-Packing Law

定義：

$$
E_q
=
\left\{
t\in(0,T_\ast):
2^q
\le
\Lambda(t)
<
2^{q+1}
\right\},
$$

以及 occupancy：

$$
m_q
=
|E_q|.
$$

則對任意 $a>0$：

$$
\int_0^{T_\ast}\Lambda(t)^a\,dt
\asymp
\sum_q
2^{aq}m_q,
$$

忽略有限 low-frequency shells。

因此定理 3.1 等價給出：

$$
\boxed{
\sum_q2^qm_q<\infty,
}
$$

但是：

$$
\boxed{
\sum_q2^{5q/2}m_q=\infty.
}
$$

## 定理 5.1（Blow-up spike-packing law）

任何 hypothetical finite blow-up 的 dissipation-wavenumber occupancy 必須滿足：

$$
\boxed{
\left(m_q\right)
\in
\ell^1(2^q)
\setminus
\ell^1(2^{5q/2}).
}
$$

$\square$

這是一個真正的 multiscale packing restriction。

---

# 6. 粗略 power-law window

若只作 asymptotic diagnostic，假設：

$$
m_q
\sim
2^{-\alpha q},
$$

則：

$$
\sum_q2^qm_q
\sim
\sum_q2^{(1-\alpha)q}
$$

有限要求：

$$
\alpha>1.
$$

而：

$$
\sum_q2^{5q/2}m_q
\sim
\sum_q2^{(5/2-\alpha)q}
$$

發散允許：

$$
\alpha\le\frac52.
$$

因此 hypothetical blow-up 的純 occupancy 指數區域為：

$$
\boxed{
1<\alpha\le\frac52.
}
$$

注意：

$$
\alpha=2
$$

——也就是自然 parabolic window：

$$
\tau_q\sim\lambda_q^{-2}
$$

——完全落在允許域內。

這已是一個關鍵 no-go 訊號。

---

# 7. 外部輸入 B：High-shell critical toll

Cheskidov–Dai 的 frequency-localized regularity criterion給出一類 dimensionless high-shell quantity。

對 NSE，可考察：

$$
K_q
=
\int_{T/2}^{T}
1_{\{q\le Q(t)\}}
\lambda_q
\|u_q(t)\|_\infty\,dt.
$$

其 theorem 說：若

$$
\limsup_{q\to\infty}K_q
$$

小於一個足夠小的 universal/viscosity-normalized threshold，則 solution regular through $T$。

因此 contrapositive 給：

## 定理 7.1（Critical shell toll necessity；external contrapositive）

若 $T_\ast$ 為 singular time，則：

$$
\boxed{
\limsup_{q\to\infty}
K_q
>
c_\ast
}
$$

其中 $c_\ast>0$ 為 theorem 所允許的 regularity threshold。

因此沿 infinitely many high shells：

$$
\boxed{
K_q
\gtrsim 1
}
$$

在 dimensionless scaling 意義下不可消失。

這是我們原來尋找的「每個高尺度需要支付 critical toll」的嚴格版本之一。

---

# 8. 為什麼這個 toll 還不能直接求和？

因為：

$$
K_q
$$

具有三個困難：

1. 不同 $q$ 的 time support 高度重疊；
2. interval approaching $T_\ast$ 可 nested；
3. 沒有由 energy inequality 給出的：

$$
\sum_qK_q<\infty.
$$

所以：

$$
K_q\gtrsim c_\ast
\quad
\text{infinitely often}
$$

雖然意味：

$$
\sum_qK_q=\infty
$$

若直接逐 shell 相加，

但我們並沒有一個 theorem 說這個 sum 必須由：

$$
\|u_0\|_2^2
$$

或總 energy dissipation 上界。

也就是：

$$
\boxed{
\text{critical toll exists}
\neq
\text{critical toll has an additive finite global ledger}.
}
$$

---

# 9. N–S scaling

標準縮放：

$$
u_\lambda(x,t)
=
\lambda
u(\lambda x,\lambda^2t).
$$

若 $u$ 解 N–S，則 $u_\lambda$ 仍解同 viscosity-normalized form。

$L^3$ norm 為 critical：

$$
\|u_\lambda(t)\|_3
=
\|u(\lambda^2t)\|_3.
$$

因此上一輪 C1 的 $L^3$ replenishment 是 scale-invariant event type。

---

# 10. Quadratic Sobolev cost scaling

定義：

$$
\mathcal D_s[u;I]
=
\int_I
\|u(t)\|_{\dot H^s}^2\,dt.
$$

N–S scaling 下：

$$
\|u_\lambda(t)\|_{\dot H^s}
=
\lambda^{s-\frac12}
\|u(\lambda^2t)\|_{\dot H^s}.
$$

若：

$$
I_\lambda
=
\lambda^{-2}I,
$$

則：

$$
\boxed{
\mathcal D_s[u_\lambda;I_\lambda]
=
\lambda^{2s-3}
\mathcal D_s[u;I].
}
$$

---

# 11. C2c：Scale-Blind Quadratic Toll No-Go

## 定理 11.1

考慮任何對 N–S scaling invariant 的事件類 $\mathcal E$。

若候選 cost 為：

$$
\mathcal D_s
=
\int\|u\|_{\dot H^s}^2dt
$$

且：

$$
s<\frac32,
$$

則不存在只由事件類 $\mathcal E$ 本身推出的 scale-independent constant：

$$
c>0
$$

使所有該類事件都滿足：

$$
\mathcal D_s\ge c.
$$

### 證明

取任一具有：

$$
0<\mathcal D_s[u;I]<\infty
$$

的 event representative。

由 scaling invariance，$u_\lambda$ 仍屬同一 event class。

但：

$$
\mathcal D_s[u_\lambda;I_\lambda]
=
\lambda^{2s-3}
\mathcal D_s[u;I].
$$

因：

$$
2s-3<0,
$$

所以：

$$
\lambda\to\infty
$$

時：

$$
\mathcal D_s[u_\lambda;I_\lambda]\to0.
$$

因此不存在 uniform positive lower bound。$\square$

---

# 12. Energy dissipation route 正式 no-go

standard energy dissipation：

$$
\mathcal D_{\mathrm{energy}}
=
\nu
\int_I
\|\nabla u(t)\|_2^2dt
$$

對應：

$$
s=1.
$$

故：

$$
\boxed{
\mathcal D_{\mathrm{energy}}[u_\lambda;I_\lambda]
=
\lambda^{-1}
\mathcal D_{\mathrm{energy}}[u;I].
}
$$

所以：

$$
\boxed{
\text{高頻 critical replenishment}
\not\Rightarrow
\text{固定正數的 energy-dissipation cost}.
}
$$

這正式淘汰上一輪最自然的：

$$
\sum_n\operatorname{Cost}_n
\le
\frac12\|u_0\|_2^2
$$

加上：

$$
\operatorname{Cost}_n\ge c>0
$$

的策略。

在高頻：

$$
\operatorname{Cost}_n
$$

完全可以像：

$$
2^{-J_n}
$$

一樣縮小。

---

# 13. 臨界 quadratic level

當：

$$
s=\frac32,
$$

有：

$$
\boxed{
\mathcal D_{3/2}[u_\lambda;I_\lambda]
=
\mathcal D_{3/2}[u;I].
}
$$

所以：

$$
\int
\|u\|_{\dot H^{3/2}}^2dt
$$

才具有 scale-independent toll 的 dimensional qualification。

但 standard energy inequality只控制：

$$
s=1,
$$

不控制：

$$
s=\frac32.
$$

所以目前出現一個極清楚的 criticality wall：

$$
\boxed{
\text{finite unconditional budget lives below the critical toll exponent}.
}
$$

這不是偶然。

這正是 N–S global regularity 的尺度困難之一。

---

# 14. Abstract Geometric Cascade Ledger

為證明「目前 scalar constraints 邏輯上彼此相容」，建立一個純 scalar model。

**警告：此模型不是 N–S solution。**

令：

$$
\lambda_n=2^n.
$$

令每一個 hypothetical critical-scale event duration：

$$
\tau_n
=
\lambda_n^{-2}
=
2^{-2n}.
$$

令 characteristic velocity amplitude：

$$
U_n
\sim
\lambda_n.
$$

這符合 N–S critical scaling。

---

# 15. Ledger A：finite total time

$$
\sum_n\tau_n
=
\sum_n2^{-2n}
<
\infty.
$$

所以 infinite cascade 可以塞進 finite time。

---

# 16. Ledger B：finite $L^1$ dissipation-wavenumber occupancy

$$
\sum_n
\lambda_n\tau_n
=
\sum_n
2^n2^{-2n}
=
\sum_n2^{-n}
<
\infty.
$$

所以：

$$
\Lambda\in L^1
$$

與 infinite parabolic cascade 相容。

---

# 17. Ledger C：divergent $L^{5/2}$ dissipation-wavenumber moment

$$
\sum_n
\lambda_n^{5/2}\tau_n
=
\sum_n
2^{5n/2}2^{-2n}
=
\sum_n
2^{n/2}
=
\infty.
$$

所以：

$$
\Lambda\notin L^{5/2}
$$

同樣與此 cascade 相容。

---

# 18. Ledger D：critical shell toll remains order one

取：

$$
K_n
\sim
\lambda_nU_n\tau_n.
$$

則：

$$
K_n
\sim
\lambda_n^2\lambda_n^{-2}
=
1.
$$

所以每個 scale 都可以支付：

$$
\boxed{
K_n\asymp1
}
$$

的 critical toll。

---

# 19. Ledger E：energy dissipation still summable

由 scaling theorem，critical-shaped event 在 scale $\lambda_n$ 的 ordinary energy-dissipation cost 應為：

$$
D_n
\sim
\lambda_n^{-1}.
$$

故：

$$
\sum_nD_n
\sim
\sum_n2^{-n}
<
\infty.
$$

因此以下五件事同時相容：

$$
\boxed{
\begin{aligned}
&\sum_n\tau_n<\infty,\\
&\Lambda\in L^1,\\
&\Lambda\notin L^{5/2},\\
&K_n\asymp1\text{ at every scale},\\
&\sum_nD_n<\infty.
\end{aligned}
}
$$

---

# 20. C2d：Scalar-Ledger Compatibility No-Go

## 命題 20.1

僅使用下列 scalar constraints：

1. finite total time；
2. finite energy dissipation；
3. $\Lambda\in L^1$；
4. blow-up requires $\Lambda\notin L^{5/2}$；
5. nonvanishing critical shell toll；

不能產生形式矛盾。

### 證明

§14–19 的 geometric cascade ledger 是同時滿足全部條件的抽象 sequence model。$\square$

再次強調：

$$
\boxed{
\text{這不是 blow-up construction}.
}
$$

它只證明：

$$
\boxed{
\text{這些 scalar inequalities 本身不足以排除 blow-up-shaped bookkeeping}.
}
$$

---

# 21. 這與 Tao averaged N–S no-go 的一致性

Tao 已構造 averaged bilinear operator：

$$
\widetilde B(u,u)
$$

仍滿足：

$$
\langle
\widetilde B(u,u),u
\rangle
=
0
$$

即保持 usual energy cancellation，

但對 corresponding averaged 3D Navier–Stokes equation 可產生 finite-time blow-up。

因此已有一個更強的外部 no-go：

$$
\boxed{
\text{energy identity + generic harmonic-analysis structure}
\text{不足以證 true N--S regularity}.
}
$$

本文的 C2 no-go 與此完全同向：

> 若想排除 geometric critical cascade，必須使用 true Navier–Stokes bilinear symbol 的更細結構。

---

# 22. X 積分重新定位：不是「費用相加」，而是「跨尺度形成資格」

上一輪想像：

$$
\text{每次事件付費}
\Rightarrow
\text{總預算耗盡}
$$

現在證明太弱。

X 積分真正應該作用在：

$$
\boxed{
\text{事件 }n
\text{ 是否有資格把來源結構傳給事件 }n+1.
}
$$

也就是：

$$
\mathsf G_n
\left(
X_n,
\rho_{n\to n+1},
X_{n+1}
\right).
$$

要檢查的不只是 scalar amplitude，而是：

- parent provenance；
- frequency support；
- spatial overlap；
- incompressibility；
- pressure-mediated nonlocal coupling；
- vorticity direction；
- triad sign/geometry；
- source depletion；
- backreaction；
- cancellation；
- branch multiplicity；
- persistence across scales。

這些才可能破壞 geometric self-similar ledger。

---

# 23. True ETN 更新：scalar tension 改成 typed tension relation

ETN 若只記：

$$
\Theta_q
=
(T_q,D_q),
$$

仍太粗。

下一版至少應記：

$$
\boxed{
\Theta_q
=
\left\langle
A_q,
D_q,
R_q,
\mathcal P_q,
\mathcal G_q,
\mathcal S_q
\right\rangle,
}
$$

其中：

- $A_q$：amplitude state；
- $D_q$：viscous dissipation；
- $R_q$：nonlinear replenishment；
- $\mathcal P_q$：provenance / parent structure；
- $\mathcal G_q$：triad geometry；
- $\mathcal S_q$：spatial concentration / support state。

真正的 tension 不再是一個 scalar。

而是一個 typed multiscale relation。

---

# 24. 新 frontier：C3 Cross-Scale Coupling Rigidity

C2 的 scalar additive route 正式降級。

下一主題定義：

$$
\boxed{
\mathrm{C3}
=
\textbf{Cross-Scale Coupling Rigidity}.
}
$$

目標不是證：

$$
\sum_n\text{cost}_n=\infty.
$$

而是證任意 hypothetical blow-up chain 必須滿足某種 incompatible cross-scale constraints。

候選 C3 branches：

## C3-A — Parent Depletion

高頻 child 的生成是否必然對 comparable-frequency parent 造成可量化 depletion？

若：

$$
\text{child gain}
\Rightarrow
\text{parent loss}
$$

可建立不可重複使用的來源帳本，才可能產生真正 additive structure。

## C3-B — Branching Congestion

若每個 high-frequency event 必須有 comparable-high parent，而 parent 數量不能無限自由複製，是否會形成：

$$
\text{genealogical congestion}
$$

或 multiplicity explosion？

## C3-C — Triad Geometry Rigidity

true N–S symbol：

$$
\mathbb P\nabla\cdot(u\otimes u)
$$

的 incompressibility / Leray projection 是否禁止 averaged-model 那類 perfect cascade wiring？

## C3-D — Spatial–Frequency Coherence

高頻 Fourier generation 是否同時必須在 physical space 形成足夠 concentration？

若 spatial center / direction / scale 無法持續對齊，genealogy 可能失效。

## C3-E — Vorticity Direction / Stretching Constraint

研究：

$$
(\omega\cdot\nabla)u
$$

的 amplification 是否需要 increasingly rigid directional coherence，而 viscosity / Biot–Savart geometry 對此形成 obstruction。

---

# 25. 本輪正式裁決

$$
\boxed{
\begin{aligned}
\mathrm{C2a}:&
\ \Lambda\in L^1\setminus L^{5/2}
\text{ under blow-up}
&&\mathrm{CLOSED/EXTERNAL},\\[2mm]
\mathrm{C2b}:&
\ \text{dyadic spike-packing law}
&&\mathrm{CLOSED/DERIVED},\\[2mm]
\mathrm{C2c}:&
\ \text{high-shell critical toll}
&&\mathrm{CLOSED/EXTERNAL\ CONTRAPOSITIVE},\\[2mm]
\mathrm{C2d}:&
\ \text{fixed energy toll strategy}
&&\mathrm{NO\mbox{-}GO},\\[2mm]
\mathrm{C2e}:&
\ \text{scalar-ledger contradiction}
&&\mathrm{NO\mbox{-}GO},\\[2mm]
\mathrm{C3}:&
\ \text{cross-scale structural rigidity}
&&\mathrm{OPEN}.
\end{aligned}
}
$$

---

# 26. 結論

本輪沒有得到 Navier–Stokes regularity proof。

但它把「有限預算能否阻止無限 cascade」這條路壓到一個非常清楚的極限：

$$
\boxed{
\text{critical geometric cascade 可以同時具有：}
}
$$

$$
\boxed{
\text{finite time}
+
\text{finite energy dissipation}
+
\Lambda\in L^1
+
\Lambda\notin L^{5/2}
+
\text{nonzero critical toll at every scale}.
}
$$

因此：

$$
\boxed{
\text{單純 scalar accounting 不足。}
}
$$

若要跨過這個 frontier，下一步必須使用 true N–S nonlinear operator 的**跨尺度關係結構**：

$$
\boxed{
\text{parent}
\to
\text{child}
\to
\text{depletion/backreaction}
\to
\text{next child}.
}
$$

這正好是 True ETN 與 X 積分真正能提供新研究語言的位置：

- ETN：保存 infinite-dimensional tension network；
- X Integration：逐尺度審核 relation 是否合法形成；
- N–S：提供不可任意修改的 exact bilinear dynamics；
- C3：尋找 geometric cascade ledger 無法滿足的第一個 genuine cross-scale obstruction。

---

# References

1. A. Cheskidov, R. Shvydkoy, *A unified approach to regularity problems for the 3D Navier–Stokes and Euler equations: the use of Kolmogorov's dissipation range*, arXiv:1102.1944.
2. A. Cheskidov, M. Dai, *Regularity criteria for the 3D Navier–Stokes and MHD equations*, arXiv:1507.06611.
3. T. Tao, *Finite time blowup for an averaged three-dimensional Navier–Stokes equation*, arXiv:1402.0290.
4. L. Escauriaza, G. Seregin, V. Šverák, *$L_{3,\infty}$-solutions of Navier–Stokes equations and backward uniqueness*, 2003.
5. T. Tao, *Quantitative bounds for critically bounded solutions to the Navier–Stokes equations*, arXiv:1908.04958.

# Internal dependencies

- `NS_ETN_XIntegration_Multiscale_NonCollapse_v0.1.md`
- `NS_C1_UV_Replenishment_Chain_v0.2.md`
- `X_Integral_Unified_Program_v0.2.md`
- `X_Integral_Kakeya_PreMeasure_Reinterpretation_v0.1.md`
- `X_Singularity_Theory_Foundations_v0.1.md`
- `True ETN / 無限維張力場`

Next target:

$$
\boxed{
\textbf{C3 — Cross-Scale Coupling Rigidity}
}
$$

Priority order:

1. parent depletion / backreaction；
2. exact triad geometry audit；
3. spatial-frequency coherence；
4. vorticity-direction stretching；
5. branching-congestion theorem.
