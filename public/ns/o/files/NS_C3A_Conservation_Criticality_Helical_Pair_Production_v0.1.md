---
title: "Navier–Stokes C3-A：守恆—臨界—正定三難與雙手性成對生成發散"
subtitle: "The Conservation–Criticality–Positivity Trilemma and Divergent Helical Pair Production at Hypothetical Blow-up"
version: "v0.1"
date: "2026-08-14"
author: "Neo.K / EveMissLab"
language: "zh-TW"
status: "Theorem-style structural reduction note"
epistemic_status: "Exact energy/helicity identities + standard Sobolev input + external helical-decimation comparison. Does NOT prove regularity."
---

# Navier–Stokes C3-A：守恆—臨界—正定三難與雙手性成對生成發散

## 0. 目的

C2 已證明：

$$
\boxed{
\text{scalar additive energy budget alone cannot rule out a critical geometric cascade}.
}
$$

因此下一步必須使用 true Navier–Stokes nonlinearity 的更細結構。

本輪從三個自然 quadratic quantities 出發：

1. kinetic energy；
2. helicity；
3. critical $\dot H^{1/2}$ size。

結果顯示它們形成一個結構三難：

$$
\boxed{
\text{positive}
+
\text{critical}
+
\text{nonlinearly conserved}
}
$$

在 full 3D Navier–Stokes 中不能由這三個最自然 scalar quantities 同時取得。

這迫使研究從 scalar invariant 轉向 **signed paired structure**。

---

# 1. Navier–Stokes scaling

標準 scaling：

$$
u_\lambda(x,t)
=
\lambda u(\lambda x,\lambda^2t).
$$

對 homogeneous Sobolev norm：

$$
\|u_\lambda\|_{\dot H^s}
=
\lambda^{s-\frac12}
\|u\|_{\dot H^s}.
$$

因此 state-level critical quadratic Sobolev exponent為：

$$
2s-1=0
\quad\Longleftrightarrow\quad
s=\frac12.
$$

所以：

$$
\boxed{
\|u\|_{\dot H^{1/2}}^2
}
$$

是 scaling-critical quadratic size。

---

# 2. Energy：正定 + 守恆結構，但次臨界

kinetic energy：

$$
E(t)
=
\frac12\|u(t)\|_2^2.
$$

對 smooth N–S：

$$
\boxed{
\frac{d}{dt}E(t)
+
\nu\|\nabla u(t)\|_2^2
=
0.
}
$$

nonlinear term obeys：

$$
\langle
(u\cdot\nabla)u,
u
\rangle
=
0.
$$

所以 energy 具有：

- positivity；
- exact nonlinear cancellation；
- global finite budget。

但 scaling：

$$
\|u_\lambda\|_2^2
=
\lambda^{-1}\|u\|_2^2.
$$

故 energy 是 subcritical relative to the blow-up scaling。

---

# 3. Exact low/high energy flux antisymmetry

令 $P_{\le K}$、$P_{>K}$ 為 $L^2$-orthogonal Fourier cutoff。

寫：

$$
u_L=P_{\le K}u,
\qquad
u_H=P_{>K}u.
$$

定義：

$$
E_L=\frac12\|u_L\|_2^2,
\qquad
E_H=\frac12\|u_H\|_2^2.
$$

令：

$$
N(u)=\mathbb P(u\cdot\nabla u).
$$

定義 flux into high frequencies：

$$
\Pi_K(t)
=
-
\langle N(u),u_H\rangle.
$$

則：

$$
\boxed{
\frac{dE_H}{dt}
+
\nu\|\nabla u_H\|_2^2
=
\Pi_K,
}
$$

而因：

$$
\langle N(u),u\rangle=0,
$$

有：

$$
\boxed{
\frac{dE_L}{dt}
+
\nu\|\nabla u_L\|_2^2
=
-\Pi_K.
}
$$

因此 nonlinear energy transfer across a cutoff 是 exact antisymmetric：

$$
\boxed{
\text{high-side gain}
=
\text{low-side nonlinear loss}
}
$$

在 $L^2$ energy level成立。

這是 C3 的第一個 exact parent-depletion identity。

---

# 4. 但 critical $L^3$ size 可以幾乎不花 $L^2$ energy

取固定 divergence-free Schwartz vector field $v$，Fourier support 位於 unit annulus。

定義：

$$
v_{\lambda,A}(x)
=
A\lambda v(\lambda x).
$$

則：

$$
\|v_{\lambda,A}\|_3
=
A\|v\|_3,
$$

但是：

$$
\|v_{\lambda,A}\|_2^2
=
A^2\lambda^{-1}\|v\|_2^2.
$$

因此對任意：

$$
M>0,
\qquad
\varepsilon>0,
$$

可以先取：

$$
A=\frac{M}{\|v\|_3},
$$

再取足夠大的 $\lambda$，使：

$$
\boxed{
\|v_{\lambda,A}\|_3=M,
}
$$

而同時：

$$
\boxed{
\|v_{\lambda,A}\|_2^2<\varepsilon.
}
$$

## 命題 4.1

不存在只由 high-frequency $L^3$ critical amplitude 推出的 universal positive lower bound：

$$
\|P_{>K}u\|_3\ge M
\quad\Longrightarrow\quad
\|P_{>K}u\|_2^2\ge c(M)>0
$$

uniformly over arbitrarily high frequencies。

因此 §3 的 exact energy depletion 雖然真實，仍不足以 charge C1 的 critical UV replenishment。

---

# 5. Critical positive quadratic size

定義：

$$
A(t)
=
\|u(t)\|_{\dot H^{1/2}}^2.
$$

由 Sobolev embedding：

$$
\dot H^{1/2}(\mathbb R^3)
\hookrightarrow
L^3(\mathbb R^3),
$$

有：

$$
\|u\|_3
\le
C\|u\|_{\dot H^{1/2}}.
$$

因此若 hypothetical blow-up 使：

$$
\limsup_{t\uparrow T_\ast}\|u(t)\|_3=\infty,
$$

則：

$$
\boxed{
\limsup_{t\uparrow T_\ast}A(t)=\infty.
}
$$

這把 C1 的 $L^3$ escape 轉成 critical quadratic escape。

---

# 6. 但 $\dot H^{1/2}$ size 不具有 energy cancellation

對 smooth solution：

$$
\frac12
\frac{d}{dt}
\|u\|_{\dot H^{1/2}}^2
+
\nu
\|u\|_{\dot H^{3/2}}^2
=
\mathcal P_{\mathrm{crit}}(t),
$$

其中：

$$
\boxed{
\mathcal P_{\mathrm{crit}}
=
-
\left\langle
|D|u,
\mathbb P(u\cdot\nabla u)
\right\rangle.
}
$$

一般而言：

$$
\mathcal P_{\mathrm{crit}}\ne0.
$$

所以：

$$
\boxed{
\dot H^{1/2}
=
\text{positive + critical}
}
$$

但失去：

$$
\boxed{
\text{exact nonlinear conservation}.
}
$$

---

# 7. Helicity：critical + nonlinear invariant，但 sign-indefinite

定義 vorticity：

$$
\omega=\nabla\times u.
$$

helicity：

$$
H(t)
=
\int_{\mathbb R^3}
u\cdot\omega\,dx.
$$

在 inviscid nonlinear dynamics 中 helicity conserved。

對 viscous N–S：

$$
\frac{dH}{dt}
=
-2\nu
\int
\omega\cdot(\nabla\times\omega)\,dx.
$$

最重要的是：

$$
\boxed{
\text{nonlinear contribution to }\frac{dH}{dt}=0.
}
$$

helicity scaling：

$$
H[u_\lambda]=H[u].
$$

所以 helicity 是 critical quadratic invariant of the nonlinear flow。

但：

$$
H
$$

不是 positive definite。

正負 helical content 可以 cancellation。

---

# 8. Conservation–Criticality–Positivity Trilemma

因此三個自然 quantity：

| Quantity | Positive | Scaling-critical | Nonlinear conservation |
|---|---:|---:|---:|
| $\|u\|_2^2$ | YES | NO | YES |
| helicity $H$ | NO | YES | YES |
| $\|u\|_{\dot H^{1/2}}^2$ | YES | YES | NO |

得到：

$$
\boxed{
\textbf{Conservation–Criticality–Positivity Trilemma}.
}
$$

這不是說不存在任何更高級 functional 同時取得三者。

它只說：

> N–S 最自然的 quadratic scalar structure 已經把三個需要的性質分散到不同 quantities 中。

所以單 scalar energy method 會自然失去 criticality；直接 critical norm method 則失去 nonlinear cancellation。

---

# 9. Helical decomposition

在 Fourier space，對 divergence-free modes使用 curl eigenbasis：

$$
i\xi\times h^\pm(\xi)
=
\pm|\xi|h^\pm(\xi).
$$

分解：

$$
u=u^++u^-.
$$

滿足：

$$
\nabla\times u^\pm
=
\pm|D|u^\pm.
$$

定義 positive sector helicities：

$$
H_+(t)
=
\|u^+(t)\|_{\dot H^{1/2}}^2,
$$

$$
H_-(t)
=
\|u^-(t)\|_{\dot H^{1/2}}^2.
$$

則：

$$
\boxed{
H
=
H_+-H_-,
}
$$

而：

$$
\boxed{
A
=
H_++H_-
=
\|u\|_{\dot H^{1/2}}^2.
}
$$

因此：

- signed difference = critical invariant channel；
- positive sum = critical size channel。

---

# 10. Sector evolution

令 $P^\pm$ 為 helical projectors。

對每一 sector：

$$
\frac12H_\pm'
+
\nu
D_\pm
=
\mathcal R_\pm,
$$

其中：

$$
D_\pm
=
\|u^\pm\|_{\dot H^{3/2}}^2,
$$

以及：

$$
\mathcal R_\pm
=
-
\left\langle
|D|u^\pm,
P^\pm\mathbb P(u\cdot\nabla u)
\right\rangle.
$$

因 nonlinear helicity conservation：

$$
\left(\frac{d}{dt}(H_+-H_-)\right)_{\rm nonlinear}
=
0.
$$

因此：

$$
\boxed{
\mathcal R_+
=
\mathcal R_-.
}
$$

令共同值：

$$
\boxed{
\mathcal R(t)
=
\mathcal R_+(t)
=
\mathcal R_-(t).
}
$$

---

# 11. Exact critical pair-production identity

將兩 sector equation 相加：

$$
\boxed{
\frac12A'(t)
+
\nu
\left(
D_+(t)+D_-(t)
\right)
=
2\mathcal R(t).
}
$$

這裡：

$$
A=H_++H_-.
$$

所以 full N–S critical positive size 的 nonlinear growth，不是 arbitrary scalar source，而是：

$$
\boxed{
\text{equal nonlinear production in the two signed helical sectors}.
}
$$

本文稱：

$$
\boxed{
\mathcal R
=
\textbf{critical helical pair-production rate}
}
$$

這是描述性名稱；其數學定義就是上式的 $\mathcal R$。

---

# 12. C3-A 主定理：blow-up forces divergent positive pair production

## 定理 12.1（Pair-Production Divergence）

若 $T_\ast<\infty$ 是 maximal finite blow-up time，則：

$$
\boxed{
\int_0^{T_\ast}
[\mathcal R(t)]_+
\,dt
=
\infty,
}
$$

其中：

$$
[x]_+=\max\{x,0\}.
$$

### 證明

由 $L^3$ endpoint regularity criterion 與：

$$
\dot H^{1/2}\hookrightarrow L^3,
$$

hypothetical blow-up implies：

$$
\limsup_{t\uparrow T_\ast}
A(t)
=
\infty.
$$

由 pair-production identity：

$$
\frac12A(t)
+
\nu
\int_0^t(D_++D_-)\,ds
=
\frac12A(0)
+
2
\int_0^t
\mathcal R(s)\,ds.
$$

因 dissipation term nonnegative：

$$
\frac12A(t)
\le
\frac12A(0)
+
2
\int_0^t
[\mathcal R(s)]_+\,ds.
$$

若：

$$
\int_0^{T_\ast}
[\mathcal R]_+dt
<
\infty,
$$

則 $A(t)$ uniform bounded，與 blow-up implication矛盾。

故：

$$
\int_0^{T_\ast}
[\mathcal R]_+dt
=
\infty.
$$

$\square$

---

# 13. 這比 C2 的 critical toll 更細

C2 說：

$$
\text{某些 high-frequency shell toll 必須 nonvanishing}.
$$

C3-A 說：

$$
\boxed{
\text{總 critical size 若逃向無限，
非線性必須累積無限量的 signed-sector pair production}.
}
$$

而且：

$$
\mathcal R
$$

不是 energy flux。

它是 full nonlinear operator 在 helical critical coordinates 下的特定 projection。

這開始真正使用 true $B(u,u)$ 的結構，而不只使用 energy identity。

---

# 14. 與 helical-decimated global regularity 的外部對照

Biferale–Titi 研究把 dynamics 投影到 single-sign helicity subspace 的 decimated 3D Navier–Stokes system。

在該模型中：

$$
H
$$

變成 sign-definite，

並等價於：

$$
\|u\|_{\dot H^{1/2}}^2.
$$

因此同一 quantity 同時得到：

$$
\boxed{
\text{positive + critical + inviscid conserved}.
}
$$

他們據此建立 arbitrary-data global regularity for the decimated system。

這不是 full N–S proof。

但它給我們一個非常重要的 structural control：

$$
\boxed{
\text{移除 opposite-helicity freedom 後，
trilemma 可被解除，global regularity 可證。}
}
$$

因此 full N–S 的 mixed-helicity freedom 不是可隨意忽略的 decoration。

---

# 15. X 積分翻譯

對每個 critical replenishment interval：

$$
I_n=[t_{n-1},t_n],
$$

除了上一輪的：

$$
\operatorname{XUVRepCert}_n,
$$

現在新增：

$$
\boxed{
\operatorname{XHelPairCert}_n
=
\left\langle
H_+,
H_-,
D_+,
D_-,
\mathcal R,
\operatorname{Prov}_{\rm hel}
\right\rangle_{I_n}.
}
$$

守衛至少檢查：

1. helical decomposition is from same $u$；
2. $P^++P^-$ reconstructs divergence-free field；
3. signed difference recovers helicity；
4. positive sum recovers $\dot H^{1/2}$ size；
5. nonlinear sector-production equality：
   $$
   \mathcal R_+=\mathcal R_-;
   $$
6. viscous terms kept separate；
7. pair-production cannot be replaced by energy flux；
8. individual triad genealogy仍未由 aggregate $\mathcal R$ 決定。

---

# 16. True ETN 更新

N–S ETN state 應至少加入 paired critical coordinates：

$$
\boxed{
\Theta_{\rm crit}(t)
=
\left\langle
H_+(t),
H_-(t),
H_+(t)-H_-(t),
H_+(t)+H_-(t),
\mathcal R(t),
D_+(t),
D_-(t)
\right\rangle.
}
$$

這比單一：

$$
E_j,T_j,D_j
$$

更接近真正的「張力」。

因為：

$$
\boxed{
\text{一個方向的 critical growth
被另一方向的 signed invariant 結構牽制}.
}
$$

---

# 17. 尚未閉合的關鍵

定理 12.1 仍沒有 contradiction。

因為目前沒有：

$$
\boxed{
\int_0^{T_\ast}[\mathcal R]_+dt<\infty
}
$$

的 unconditional theorem。

事實上：

$$
\mathcal R
$$

本身是 scaling-critical rate：

under $u_\lambda$，

$$
\mathcal R_\lambda(t)
=
\lambda^2
\mathcal R(\lambda^2t),
$$

所以：

$$
\int\mathcal R_\lambda dt
$$

scale invariant。

因此 infinite cascade 每一尺度支付 $O(1)$ pair-production toll 在 scaling 上完全可能。

這與 C2 的 critical toll no-go 一致。

---

# 18. 下一個真正 proof target

C3-A 已把問題壓成：

$$
\boxed{
\mathrm{Blowup}
\Rightarrow
\int_0^{T_\ast}[\mathcal R]_+dt=\infty.
}
$$

所以最有價值的下一步不是再找另一個 scalar norm，而是研究：

$$
\boxed{
\mathcal R
\text{ 的 exact mixed-helicity triad kernel}.
}
$$

具體目標：

## H1 — Minority-factor estimate

測試是否存在：

$$
|\mathcal R|
\le
C
\min
\left\{
\|u^+\|_{\dot H^{1/2}},
\|u^-\|_{\dot H^{1/2}}
\right\}
\|u\|_{\dot H^{3/2}}^2.
$$

目前標記：

$$
\boxed{\text{CANDIDATE LEMMA}}
$$

不得當 theorem。

若成立，則任何 blow-up 必須使兩個 helicity sectors 都無法永久保持小 critical size。

## H2 — Exact triad sign classification

將：

$$
(s_1,s_2,s_3)\in\{+,-\}^3
$$

八類 interaction 全展開，判定哪些：

- 對 $\mathcal R$ exact cancel；
- 只 redistribute；
- 真正 pair-produce critical size。

## H3 — Cross-scale pair-production congestion

研究同一 mixed-helicity parent structure 是否能無限次支援：

$$
q\to q+1\to q+2\to\cdots
$$

而不產生：

- depletion；
- alignment loss；
- back-transfer；
- viscous penalty；
- branch multiplicity explosion。

---

# 19. C3-A 正式狀態

$$
\boxed{
\begin{aligned}
\text{low/high }L^2\text{ flux antisymmetry}
&:\ \mathrm{PROVED},\\
L^3\text{ large with arbitrarily small }L^2\text{ energy}
&:\ \mathrm{PROVED},\\
\text{conservation-criticality-positivity trilemma}
&:\ \mathrm{PROVED/STRUCTURAL},\\
\mathcal R_+=\mathcal R_-
&:\ \mathrm{PROVED},\\
\mathrm{Blowup}\Rightarrow
\int[\mathcal R]_+=\infty
&:\ \mathrm{PROVED\ given\ standard\ endpoint\ regularity},\\
\text{minority-factor estimate}
&:\ \mathrm{OPEN},\\
\text{persistent triadic obstruction}
&:\ \mathrm{OPEN}.
\end{aligned}
}
$$

---

# 20. 結論

C2 告訴我們：

$$
\boxed{
\text{普通 scalar cost 可以在高頻縮小，
所以 finite energy budget 不排除 infinite critical cascade}.
}
$$

C3-A 則找到第一個真正使用 full N–S structure 的不可逃避條件：

$$
\boxed{
\text{finite-time blow-up}
\Rightarrow
\text{divergent cumulative critical helical pair production}.
}
$$

因此研究前線從：

$$
\text{energy cascade}
$$

進一步縮成：

$$
\boxed{
\text{mixed-helicity critical pair-production cascade}.
}
$$

這不等於已證明「helicity 是唯一問題」。

它只表示：在 positive critical $\dot H^{1/2}$ size 與 exact nonlinear helicity structure同時保留時，任何 blow-up 都必須穿過這個 pair-production channel。

下一輪最直接工作：

$$
\boxed{
\textbf{C3-B — Exact Helical Triad Kernel Audit}
}
$$

八類 helicity triads 全展開，優先驗證 minority-factor estimate 或找到其反例。

---

# References

1. L. Biferale, E. S. Titi, *On the Global Regularity of a Helical-decimated Version of the 3D Navier–Stokes Equations*, arXiv:1303.1215.
2. G. Sahoo, L. Biferale, *Disentangling the triadic interactions in Navier-Stokes equations*, arXiv:1510.09006.
3. G. Sahoo, L. Biferale, *Energy Cascade and Intermittency in Helically Decomposed Navier-Stokes Equations*, arXiv:1709.03713.
4. T. Tao, *Finite time blowup for an averaged three-dimensional Navier–Stokes equation*, arXiv:1402.0290.
5. L. Escauriaza, G. Seregin, V. Šverák, endpoint $L^3$ regularity theorem for 3D Navier–Stokes.

# Internal dependencies

- `NS_ETN_XIntegration_Multiscale_NonCollapse_v0.1.md`
- `NS_C1_UV_Replenishment_Chain_v0.2.md`
- `NS_C2_Critical_Toll_Spike_Packing_v0.3.md`
- `True ETN / 無限維張力場`
- `X_Integral_Unified_Program_v0.2.md`

Next:

$$
\boxed{
\textbf{C3-B — Exact Helical Triad Kernel Audit}
}
$$
