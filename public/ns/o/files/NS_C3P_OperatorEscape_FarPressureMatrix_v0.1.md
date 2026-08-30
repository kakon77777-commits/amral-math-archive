---
title: "Navier–Stokes C3-P：Operator Escape、Far-Pressure Harmonic Matrix 與 Finite-Dimensionalization No-Go"
subtitle: "Operator-Level Escape from a Regular Strain Model, Near/Far Pressure Hessian Decomposition, and Why Finite-Dimensional Far Pressure Is Not Automatically Small"
version: "v0.1"
date: "2026-08-14"
author: "Neo.K / EveMissLab"
language: "zh-TW"
status: "Theorem-style structural reduction / no-go note"
epistemic_status: "Uses external Miller operator criteria and standard pressure/Riesz representation; proves exact two-model and far-pressure structural lemmas. Does NOT prove Navier–Stokes regularity."
---

# Navier–Stokes C3-P
# Operator Escape、Far-Pressure Harmonic Matrix 與 Finite-Dimensionalization No-Go

## 0. 本輪定位

C3-O 已證：

$$
\boxed{
\text{SSA-like strain-energy balance}
\not\Rightarrow
\text{SSA-like dynamics}.
}
$$

使用 adjoint cutoff：

$$
\partial_t\chi+u\cdot\nabla\chi+\nu\Delta\chi=0,
$$

local strain balance可整理成：

$$
E_\chi'+D_\chi=A_\chi+B_\chi,
$$

其中：

$$
A_\chi=-2\int\chi\det S,
$$

而：

$$
B_\chi
=
\int\nabla\chi\cdot
\left(
\frac13F_B+F_p
\right).
$$

因此 scalar ratio：

$$
\rho=B/A
$$

只能分類 local strain-energy growth carrier，

不能判斷 full operator 是否接近某 model。

本輪正式升級到 operator level。

核心結果：

1. Miller 2026 已提供一個 theorem-backed operator blow-up necessity；
2. hypothetical blow-up不能一直留在 globally-regular strain–vorticity model的小擾動管道；
3. strain self-amplification model與 strain–vorticity model之間有 exact operator gap；
4. smallness to SSA model不是 regularity方向，在 Miller 的指定 initial-data / perturbative hypothesis下甚至與 blow-up兼容；
5. pressure Hessian可做 exact near/far source decomposition；
6. far pressure在 ancestry core中是 harmonic；
7. far pressure Hessian可 finite-dimensionalize成：
   $$
   \boxed{
   \text{constant symmetric trace-free matrix}
   +
   \text{spatially smaller remainder};
   }
   $$
8. 但 finite-dimensionalization不等於 smallness；
9. far-pressure decoupling需要額外控制一個 scale-invariant rescaled enstrophy number；
10. 因此 singular survivor必須同時支付：
   - operator escape debt；
   - 或 far-pressure harmonic-matrix debt；
   - 或 rescaled enstrophy blow-up debt。

---

# 1. 為方便引用 Miller theorem，先取 $\nu=1$

Miller 的 strain-model papers使用：

$$
\nu=1.
$$

本輪 operator-theorem subsections先採此 normalization。

一般：

$$
\nu>0
$$

可由標準 parabolic nondimensionalization恢復。

pressure near/far subsections則保留一般：

$$
\nu.
$$

---

# 2. Full strain equation

full strain equation：

$$
\partial_tS
-
\Delta S
+
P_{st}\left((u\cdot\nabla)S\right)
+
P_{st}\left(
S^2+\frac14\omega\otimes\omega
\right)
=
0.
$$

它可以相對兩個不同 model重新分組。

---

# 3. Strain self-amplification model

定義：

$$
\boxed{
\mathcal N_{SSA}
=
\frac23P_{st}(S^2).
}
$$

SSA model：

$$
\boxed{
\partial_tS
-
\Delta S
+
\mathcal N_{SSA}
=
0.
}
$$

full N–S relative to SSA model：

$$
\boxed{
\partial_tS
-
\Delta S
+
\mathcal N_{SSA}
+
\mathcal P_{SSA}
=
0,
}
$$

其中：

$$
\boxed{
\mathcal P_{SSA}
=
P_{st}
\left(
(u\cdot\nabla)S
+
\frac13S^2
+
\frac14\omega\otimes\omega
\right).
}
$$

---

# 4. Strain–vorticity interaction model

Miller 2026定義：

$$
\boxed{
\mathcal N_{SV}
=
-\frac12P_{st}(\omega\otimes\omega).
}
$$

SV interaction model：

$$
\boxed{
\partial_tS
-
\Delta S
+
\mathcal N_{SV}
=
0.
}
$$

Miller證此 model對：

$$
S^0\in L^2_{st}
$$

具有 global smooth solution。

full N–S relative to此 model：

$$
\boxed{
\partial_tS
-
\Delta S
+
\mathcal N_{SV}
+
\mathcal Q_{SV}
=
0,
}
$$

其中：

$$
\boxed{
\mathcal Q_{SV}
=
P_{st}
\left(
(u\cdot\nabla)S
+
S^2
+
\frac34\omega\otimes\omega
\right).
}
$$

---

# 5. C3-P.1：Exact Two-Model Gap

## 定理 5.1

$$
\boxed{
\mathcal Q_{SV}
-
\mathcal P_{SSA}
=
\mathcal N_{SSA}
-
\mathcal N_{SV}.
}
$$

更明確：

$$
\boxed{
\mathcal Q_{SV}
-
\mathcal P_{SSA}
=
P_{st}
\left(
\frac23S^2
+
\frac12\omega\otimes\omega
\right).
}
$$

### 證明

逐項相減。$\square$

---

# 6. Two-model triangle barrier

定義 model-gap operator：

$$
\boxed{
\mathcal G
=
P_{st}
\left(
\frac23S^2
+
\frac12\omega\otimes\omega
\right).
}
$$

則：

$$
\mathcal G
=
\mathcal Q_{SV}-\mathcal P_{SSA}.
$$

所以：

## 推論 6.1

對任意 Banach norm：

$$
\boxed{
\|\mathcal Q_{SV}\|
+
\|\mathcal P_{SSA}\|
\ge
\|\mathcal G\|.
}
$$

因此 full strain dynamics除非：

$$
\mathcal G
$$

本身很小，

否則不可能同時接近：

- SSA model；
- SV interaction model。

---

# 7. External theorem：operator-level regularity debt

Miller 2026 Theorem 1.8在：

$$
\alpha=0
$$

時給出：

若：

$$
T_\ast<\infty
$$

為 finite blow-up time，則：

$$
\boxed{
\int_0^{T_\ast}
\frac{
\|\mathcal Q_{SV}(t)\|_2^2
}{
\|S(t)\|_{\dot H^1}^2
}
\,dt
=
\infty.
}
$$

這是一個 scale-invariant integrated operator debt。

---

# 8. Scaling audit

under：

$$
u_\lambda(x,t)
=
\lambda u(\lambda x,\lambda^2t),
$$

有：

$$
S_\lambda
=
\lambda^2S(\lambda x,\lambda^2t),
$$

以及 equation-level quadratic operator：

$$
(\mathcal Q_{SV})_\lambda
=
\lambda^4
\mathcal Q_{SV}(\lambda x,\lambda^2t).
$$

所以：

$$
\|\mathcal Q_{SV,\lambda}\|_2
=
\lambda^{5/2}
\|\mathcal Q_{SV}\|_2,
$$

$$
\|S_\lambda\|_{\dot H^1}
=
\lambda^{3/2}
\|S\|_{\dot H^1}.
$$

故 ratio平方 scale：

$$
\lambda^2,
$$

配：

$$
dt\mapsto\lambda^{-2}dt,
$$

總 integral invariant。

---

# 9. C3-P.2：Regular-Model Operator Escape

Miller 2026 Theorem 1.9給：

hypothetical finite blow-up必須：

$$
\boxed{
\limsup_{t\uparrow T_\ast}
\frac{
\|\mathcal Q_{SV}(t)\|_2
}{
\|-\Delta S(t)\|_2
}
\ge
1.
}
$$

因此：

## 推論 9.1

若存在：

$$
\delta>0
$$

與：

$$
t_0<T_\ast
$$

使：

$$
\boxed{
\|\mathcal Q_{SV}(t)\|_2
\le
(1-\delta)
\|-\Delta S(t)\|_2
}
$$

對所有：

$$
t_0<t<T_\ast
$$

成立，

則：

$$
T_\ast
$$

不能是 singular time。

---

# 10. Operator escape 的意義

所以 full N–S hypothetical blow-up不能 asymptotically永久待在：

$$
\boxed{
\text{globally regular SV-model 的 dissipation-small perturbation tube}.
}
$$

它必須 infinitely near blow-up滿足：

$$
\boxed{
\mathcal Q_{SV}
\text{ 達到 }-\Delta S
\text{ 同階}.
}
$$

這是真正 operator-level necessity，

不是 scalar energy balance inference。

---

# 11. SSA-small 不是 regularity方向

另一方面，SSA model本身可 finite-time blow up。

Miller 的 SSA model paper還證：

對指定 initial-data sign condition，

若 full N–S中：

$$
\mathcal P_{SSA}
$$

相對 paper所指定的 evolution norm保持 perturbatively controlled，

則 full N–S也有 conditional finite-time blow-up conclusion。

所以：

$$
\boxed{
\mathcal P_{SSA}\text{ small}
}
$$

不能被當作通用 regularity criterion。

---

# 12. Operator phase map

因此有兩個完全不同的 operator distances：

## Distance to regular SV model

$$
\boxed{
d_{SV}(t)
=
\frac{
\|\mathcal Q_{SV}(t)\|_2
}{
\|-\Delta S(t)\|_2
}.
}
$$

blow-up必要：

$$
\boxed{
\limsup d_{SV}\ge1.
}
$$

## Distance to blow-up-capable SSA model

以：

$$
\mathcal P_{SSA}
$$

為核心。

其 smallness不是 regularity保證；

在特定 hypotheses下甚至是 blow-up-compatible。

---

# 13. Balance ratio 與 operator ratio必須分開

C3-O 的：

$$
\rho=B/A
$$

只看：

$$
\boxed{
\text{localized strain-energy balance}.
}
$$

而：

$$
d_{SV}
$$

看：

$$
\boxed{
\text{full operator size relative to strain dissipation}.
}
$$

因此：

$$
\boxed{
\rho\to0
}
$$

完全可以和：

$$
\boxed{
d_{SV}\gtrsim1
}
$$

同時成立。

這正是：

$$
\boxed{
\text{Balance-SSA / Operator-large}
}
$$

regime。

---

# 14. Pressure Poisson equation

回到一般：

$$
\nu>0.
$$

取：

$$
A=\nabla u.
$$

divergence-free N–S給：

$$
\boxed{
-\Delta p
=
\partial_i u_j
\partial_j u_i
=
\operatorname{tr}(A^2).
}
$$

定義：

$$
\boxed{
f
=
\operatorname{tr}(A^2).
}
$$

則：

$$
p
=
(-\Delta)^{-1}f
$$

up to time-dependent additive constant。

因此：

$$
\boxed{
\partial_a\partial_b p
=
R_aR_b f.
}
$$

pressure Hessian是 $f$ 的 zero-order Calderón–Zygmund transform。

---

# 15. Source size

pointwise：

$$
|f|
=
|\operatorname{tr}(A^2)|
\le
|A|^2.
$$

所以：

$$
\boxed{
\|f(t)\|_1
\le
\|\nabla u(t)\|_2^2.
}
$$

---

# 16. Near/far source decomposition

固定：

$$
x_0\in\mathbb R^3,
$$

core radius：

$$
R>0,
$$

以及：

$$
\kappa\ge4.
$$

取 smooth cutoff：

$$
\eta_{\kappa R}
$$

滿足：

$$
\eta_{\kappa R}=1
$$

on：

$$
B_{\kappa R}(x_0),
$$

并 supported in：

$$
B_{2\kappa R}(x_0).
$$

定義：

$$
f_{\rm near}
=
\eta_{\kappa R}f,
$$

$$
f_{\rm far}
=
(1-\eta_{\kappa R})f.
$$

以及：

$$
p_{\rm near}
=
(-\Delta)^{-1}f_{\rm near},
$$

$$
p_{\rm far}
=
(-\Delta)^{-1}f_{\rm far}.
$$

---

# 17. Far pressure is harmonic in the core

因：

$$
f_{\rm far}=0
$$

on：

$$
B_{\kappa R}(x_0),
$$

所以：

$$
\boxed{
\Delta p_{\rm far}=0
}
$$

在：

$$
B_{\kappa R}(x_0).
$$

因此：

$$
\boxed{
H_{\rm far}
=
\nabla^2p_{\rm far}
}
$$

在 ancestry core中是 harmonic symmetric tensor field，

並且：

$$
\boxed{
\operatorname{tr}H_{\rm far}=0.
}
$$

---

# 18. Riesz kernel bound

Riesz-pair kernel在遠離 singularity時滿足：

$$
|\nabla^mK_{ab}(z)|
\le
C_m
|z|^{-3-m}.
$$

對：

$$
x\in B_R(x_0),
$$

與：

$$
y\in\operatorname{supp}f_{\rm far},
$$

有：

$$
|x-y|
\ge
(\kappa-1)R.
$$

因此：

## 定理 18.1

對任意：

$$
m\ge0,
$$

$$
\boxed{
\|\nabla^mH_{\rm far}\|_{L^\infty(B_R)}
\le
C_m
(\kappa R)^{-3-m}
\|f\|_1.
}
$$

up to harmless constants depending on cutoff geometry。

由：

$$
\|f\|_1\le\|\nabla u\|_2^2,
$$

得到：

$$
\boxed{
\|\nabla^mH_{\rm far}\|_{L^\infty(B_R)}
\le
C_m
\kappa^{-3-m}
R^{-3-m}
\|\nabla u\|_2^2.
}
$$

---

# 19. C3-P.3：Far-Pressure Finite-Dimensionalization Lemma

令：

$$
\boxed{
H_0(t)
=
H_{\rm far}(x_0,t).
}
$$

則：

$$
H_0
$$

是 symmetric trace-free matrix。

此外：

$$
\boxed{
|H_0|
\le
C
\kappa^{-3}
R^{-3}
\|\nabla u\|_2^2.
}
$$

由 mean value theorem與 $m=1$ estimate：

$$
\boxed{
\sup_{x\in B_R}
|H_{\rm far}(x)-H_0|
\le
C
\kappa^{-4}
R^{-3}
\|\nabla u\|_2^2.
}
$$

因此：

$$
\boxed{
H_{\rm far}(x)
=
H_0
+
E_{\rm far}(x),
}
$$

其中：

$$
\boxed{
\|E_{\rm far}\|_{L^\infty(B_R)}
\le
C
\kappa^{-4}
R^{-3}
\|\nabla u\|_2^2.
}
$$

---

# 20. 5-dimensional far-pressure channel

symmetric：

$$
3\times3
$$

trace-free matrices空間維度：

$$
\boxed{
5.
}
$$

所以 far pressure在 small ancestry core的 leading effect不是 arbitrary field，

而是：

$$
\boxed{
\textbf{a five-dimensional harmonic pressure-Hessian channel}
}
$$

加上一個多一個 factor：

$$
\kappa^{-1}
$$

的 spatially varying remainder。

---

# 21. Finite-dimensionalization ≠ smallness

定義 scale-invariant rescaled enstrophy number：

$$
\boxed{
\mathfrak E_R(t)
=
\frac{
R
\|\nabla u(t)\|_2^2
}{
\nu^2
}.
}
$$

under N–S scaling：

$$
R\mapsto\lambda^{-1}R,
$$

$$
\|\nabla u\|_2^2\mapsto\lambda\|\nabla u\|_2^2,
$$

所以：

$$
\mathfrak E_R
$$

invariant。

---

# 22. Normalized far-pressure Hessian

pressure Hessian scale：

$$
\nu^2R^{-4}.
$$

定義：

$$
\boxed{
\widehat H_{\rm far}
=
\frac{
R^4
}{
\nu^2
}
H_{\rm far}.
}
$$

則：

$$
\boxed{
|\widehat H_0|
\le
C
\kappa^{-3}
\mathfrak E_R.
}
$$

以及：

$$
\boxed{
\sup_{B_R}
|\widehat H_{\rm far}-\widehat H_0|
\le
C
\kappa^{-4}
\mathfrak E_R.
}
$$

---

# 23. C3-P.4：Conditional Far-Pressure Decoupling

## 定理 23.1

若一列 ancestry scales：

$$
R_n\to0
$$

滿足 uniform rescaled-enstrophy bound：

$$
\boxed{
\sup_n
\mathfrak E_{R_n}(t_n)
<\infty,
}
$$

則先取：

$$
\kappa\to\infty
$$

時：

$$
\boxed{
\widehat H_{{\rm far},n}
\to0
}
$$

uniformly on unit rescaled core，

至少以：

$$
O(\kappa^{-3})
$$

衰減。

$\square$

---

# 24. Far-pressure decoupling No-Go

energy inequality只給：

$$
\nu
\int_0^{T_\ast}
\|\nabla u(t)\|_2^2dt
<
\infty.
$$

它不給：

$$
\boxed{
\sup_n
R_n
\|\nabla u(t_n)\|_2^2
<\infty.
}
$$

所以：

$$
\boxed{
\text{far pressure cannot be unconditionally discarded in a singular ancestry zoom}.
}
$$

若：

$$
\mathfrak E_{R_n}\to\infty,
$$

它可以補償：

$$
\kappa^{-3}
$$

spatial distance decay。

---

# 25. Far pressure dichotomy

因此 far pressure在 ancestry core有：

## P-FAR-A — Decoupled branch

$$
\boxed{
\mathfrak E_R=O(1)
}
$$

則 far pressure可由大：

$$
\kappa
$$

decouple。

## P-FAR-B — Critical enstrophy branch

$$
\boxed{
\mathfrak E_R\to\infty
}
$$

則 far pressure可能維持 order-one甚至更大 normalized influence。

這把 pressure nonlocality轉成另一個 critical moment debt。

---

# 26. Pressure current decomposition

C3-N 定義：

$$
F_p
=
(\nabla^2p-\Delta p\,I)u.
$$

在 core中 far pressure harmonic：

$$
\Delta p_{\rm far}=0.
$$

所以：

$$
\boxed{
F_{p,{\rm far}}
=
H_{\rm far}u.
}
$$

用：

$$
H_{\rm far}=H_0+E_{\rm far},
$$

得到：

$$
\boxed{
F_{p,{\rm far}}
=
H_0u
+
E_{\rm far}u.
}
$$

---

# 27. Leading harmonic-matrix pressure current

對 localization：

$$
\chi,
$$

far-pressure boundary current：

$$
B_p^{far}
=
\int
\nabla\chi\cdot
H_{\rm far}u.
$$

leading constant-matrix part：

$$
B_p^{H_0}
=
\int
\nabla\chi\cdot
H_0u.
$$

因：

$$
H_0
$$

spatially constant，

integration by parts給：

$$
\boxed{
B_p^{H_0}
=
-
\int
\chi
H_0:S\,dx.
}
$$

所以 far pressure的 leading-order core作用可被看成：

$$
\boxed{
\text{a constant trace-free external strain matrix coupled to local }S.
}
$$

---

# 28. 這個 matrix不能 gauge away

pressure只允許加：

$$
c(t)
$$

而不改：

$$
\nabla p.
$$

constant Hessian：

$$
H_0\ne0
$$

對應 quadratic harmonic pressure component，

其 gradient是 affine force。

所以：

$$
\boxed{
H_0
}
$$

不是 pressure additive gauge。

它是真正 dynamical far-field channel。

---

# 29. Spatially varying far-pressure remainder

remainder current：

$$
B_p^{rem}
=
\int
\nabla\chi\cdot
E_{\rm far}u.
$$

若：

$$
|\nabla\chi|
\lesssim
R^{-1}
$$

於 shell：

$$
\mathcal A_R,
$$

則：

$$
\boxed{
|B_p^{rem}|
\le
C
\kappa^{-4}
R^{-4}
\|\nabla u\|_2^2
\int_{\mathcal A_R}
|u|dx.
}
$$

相比 leading pressure-Hessian bound，

spatial variation多一個：

$$
\boxed{
\kappa^{-1}.
}
$$

---

# 30. Pressure finite-dimensionalization theorem 的真正含義

far pressure不是：

$$
\boxed{
\text{automatically negligible}.
}
$$

而是：

$$
\boxed{
\text{large-scale infinite-dimensional source}
\to
\text{5D harmonic matrix}
+
\text{small spatial variation}
}
$$

在 local core中的 leading asymptotic representation。

所以它是一個：

$$
\boxed{
\textbf{complexity compression theorem},
}
$$

不是 smallness theorem。

---

# 31. 與 Bradshaw–Tsai local pressure expansion 的關係

local pressure expansion literature本來就把 pressure分成：

- local source contribution；
- nonlocal/harmonic contribution；

來處理 whole-space Navier–Stokes pressure。

本輪的 far-pressure matrix lemma是 smooth ancestry-core條件下，

對：

$$
\nabla^2p
$$

再做一階 Taylor / multipole compression。

因此它和 local pressure expansion framework相容，

但本文的 5D matrix statement是本 project此 route所用的特定 derivative-level consequence。

---

# 32. Betchov current與 pressure current不可混同

adjoint balance：

$$
B_\chi
=
B_\chi^B+B_\chi^p.
$$

其中：

$$
B_\chi^B
=
\frac13
\int\nabla\chi\cdot F_B,
$$

$$
B_\chi^p
=
\int\nabla\chi\cdot F_p.
$$

差別：

### Betchov current

$$
F_B
$$

是 local algebraic current：

$$
u(\nabla u)^2.
$$

### Pressure current

$$
F_p
$$

含：

$$
\nabla^2p,
$$

而：

$$
\nabla^2p
$$

是 Calderón–Zygmund nonlocal transform。

所以：

$$
\boxed{
\text{boundary current}
}
$$

這個共同名稱不能抹掉：

$$
\boxed{
\text{local algebraic provenance}
\neq
\text{nonlocal pressure provenance}.
}
$$

---

# 33. Operator theorem與 boundary theorem是不同 observation interfaces

Miller operator criterion：

$$
d_{SV}(t)
=
\frac{
\|\mathcal Q_{SV}(t)\|_2
}{
\|-\Delta S(t)\|_2
}
$$

是：

$$
\boxed{
\text{bulk operator norm interface}.
}
$$

C3-O：

$$
\rho=B/A
$$

是：

$$
\boxed{
\text{adjoint-localized balance interface}.
}
$$

pressure matrix：

$$
H_0
$$

是：

$$
\boxed{
\text{far-field harmonic forcing interface}.
}
$$

三者不能互相偷換。

---

# 34. C3-P.5：Three-Interface Survivor Constraint

hypothetical singular ancestry必須同時尊重：

## Interface P1 — Operator escape

$$
\boxed{
\limsup
d_{SV}\ge1.
}
$$

## Interface P2 — Local growth

對 positive SSA-supported adjoint windows：

$$
\boxed{
\rho>-1.
}
$$

## Interface P3 — Far pressure

若 far-pressure effect在 rescaled core仍 non-negligible，

則至少：

$$
\boxed{
\mathfrak E_R
}
$$

不能太小，

或者其 5D harmonic matrix：

$$
\boxed{
H_0
}
$$

必須持續具有 critical-size coupling。

目前這是**平行必要 constraints**，

不是已證 mutual contradiction。

---

# 35. Blow-up operator debt比原候選 $\mathfrak P$ 更好

C3-O 提出的：

$$
\mathfrak P
=
\frac{
\int
\|\mathcal P_{SSA}\|_{\dot H^{-1}}^2
}{
\nu^2\int
\|S\|_{\dot H^1}^2
}
$$

仍是合理 diagnostic，

但未有 direct theorem支援。

C3-P 應優先加入 Miller theorem-backed：

$$
\boxed{
\mathfrak Q_{SV}
=
\int
\frac{
\|\mathcal Q_{SV}\|_2^2
}{
\|S\|_{\dot H^1}^2
}dt.
}
$$

hypothetical blow-up要求：

$$
\boxed{
\mathfrak Q_{SV}
=
\infty.
}
$$

---

# 36. Two-operator X-certificate

定義：

$$
\boxed{
\operatorname{XOp}_n
=
\left\langle
\mathcal P_{SSA,n},
\mathcal Q_{SV,n},
\mathcal G_n,
d_{SSA,n},
d_{SV,n},
\operatorname{Prov}_n
\right\rangle.
}
$$

其中：

$$
\mathcal G_n
=
\mathcal Q_{SV,n}
-
\mathcal P_{SSA,n}.
$$

守衛：

## G-MODEL

明確指出正在比較哪一個 model。

## G-REGMODEL

SV model有 global regularity theorem。

## G-BLOWMODEL

SSA model有 finite-time blowup theorem。

## G-GAP

兩個 model distance不能混成單一「perturbation size」。

## G-ORTH

zero pairing不等於 zero operator。

---

# 37. Pressure X-certificate

定義：

$$
\boxed{
\operatorname{XPressure}_n
=
\left\langle
p_{\rm near},
H_{0,n},
E_{{\rm far},n},
\kappa,
\mathfrak E_{R_n},
\operatorname{ProvFar}
\right\rangle.
}
$$

守衛：

## G-PNEAR

near pressure由 core/source neighborhood生成。

## G-PFAR

far pressure在 core harmonic。

## G-H0

保存 constant trace-free matrix：

$$
H_0.
$$

## G-PREM

保存 remainder：

$$
E_{\rm far}.
$$

## G-PENST

不能因：

$$
\kappa^{-3}
$$

就宣布 far pressure small；

必須檢查：

$$
\mathfrak E_R.
$$

---

# 38. Pressure decoupling 的真正 threshold

normalized：

$$
|\widehat H_0|
\lesssim
\kappa^{-3}
\mathfrak E_R.
$$

所以 far pressure要 decouple，

真正需要的是：

$$
\boxed{
\kappa^{-3}
\mathfrak E_R
\to0.
}
$$

不是單純：

$$
\kappa\to\infty.
$$

若 ancestry中：

$$
\mathfrak E_R
$$

以：

$$
\kappa^3
$$

或更快增長，

far pressure可保持 non-negligible。

---

# 39. 新 No-Go：spatial separation alone cannot kill pressure

$$
\boxed{
\operatorname{dist}(\text{defect},\text{core})/R
\to\infty
}
$$

不自動推出：

$$
\boxed{
\text{pressure influence}\to0.
}
$$

因 pressure source amplitude / rescaled enstrophy可同步增長。

所以 C3-F 的 off-diagonal decay對 band-limited Leray nonlinearity很強，

但 pressure Hessian的 far source需要另外的 critical source norm控制。

---

# 40. 新 frontier：C3-Q

C3-P 已回答兩個問題。

### Operator-small 是否能代表 full singular dynamics？

對 globally regular SV model：

$$
\boxed{
\text{NO：blow-up必須 operator-escape}.
}
$$

### Far pressure是否可直接 spatial-decouple？

$$
\boxed{
\text{NO：只能 finite-dimensionalize；
smallness還需 rescaled-enstrophy control}.
}
$$

因此下一主題：

$$
\boxed{
\textbf{C3-Q — Harmonic Pressure-Matrix / Operator-Escape Coupling Rigidity}.
}
$$

---

# 41. C3-Q proof obligations

## Q1 — Normalize harmonic matrix

在 ancestry scale：

$$
R_n,
$$

定義：

$$
\boxed{
\mathsf H_n
=
\frac{
R_n^4
}{
\nu^2
}
H_{0,n}.
}
$$

抽 subsequence分析：

- $\mathsf H_n\to0$；
- $\mathsf H_n\to\mathsf H_\ast\ne0$；
- $|\mathsf H_n|\to\infty$。

## Q2 — Harmonic-matrix eigengeometry

$\mathsf H_n$ 是 symmetric trace-free 5D object。

研究其 eigenframe與 local strain：

$$
S_n
$$

及 vorticity direction：

$$
\xi_n
$$

的 coupling。

## Q3 — Pressure-current ratio

比較：

$$
B_I^p/A_I
$$

與：

$$
\mathsf H_n:S_n.
$$

判定 cancellation corridor是否可主要由 far harmonic matrix支援。

## Q4 — Operator escape localization

Miller criterion是 global：

$$
\|\mathcal Q_{SV}\|_2.
$$

研究能否在 ancestry core抽出 localized operator debt。

避免：

$$
\text{global operator large}
$$

其實只來自 far defect。

## Q5 — Integrated operator debt partition

將：

$$
\int
\frac{
\|\mathcal Q_{SV}\|_2^2
}{
\|S\|_{\dot H^1}^2
}
dt
=
\infty
$$

分配到：

- ancestry core；
- spatial defect；
- frequency defect。

接 C3-I defect trichotomy。

## Q6 — Two-model gap rigidity

研究：

$$
\mathcal G
=
P_{st}
\left(
\frac23S^2+\frac12\omega\otimes\omega
\right)
$$

在 ancestry core是否可 small。

若不 small，full dynamics不能同時靠近兩個 model。

## Q7 — Pressure/enstrophy dichotomy

若：

$$
\mathsf H_n
$$

不 decouple，

使用：

$$
|\mathsf H_n|
\lesssim
\kappa^{-3}\mathfrak E_{R_n}
$$

把 far-pressure survivor轉成 rescaled-enstrophy blow-up condition。

## Q8 — Far-pressure Taylor hierarchy

若 constant matrix channel可被某 rigidity排除，

下一階 far-pressure term為：

$$
\nabla H_{\rm far}(x_0)
$$

並多付：

$$
\kappa^{-1}.
$$

建立 multipole hierarchy。

---

# 42. 正式狀態

$$
\boxed{
\begin{aligned}
\text{SSA/SV two-model operator decomposition}
&:\ \mathrm{PROVED},\\
\text{exact two-model gap}
&:\ \mathrm{PROVED},\\
\text{Miller integrated SV-operator debt}
&:\ \mathrm{EXTERNAL\ THEOREM},\\
\limsup\|\mathcal Q_{SV}\|_2/\|-\Delta S\|_2\ge1
&:\ \mathrm{EXTERNAL\ THEOREM},\\
\text{eventual SV-small perturbation under blow-up}
&:\ \mathrm{EXCLUDED},\\
\text{SSA perturbation smallness as regularity}
&:\ \mathrm{FALSE/NO\mbox{-}GO},\\
-\Delta p=\operatorname{tr}(A^2)
&:\ \mathrm{STANDARD},\\
\nabla^2p=R_iR_j\operatorname{tr}(A^2)
&:\ \mathrm{STANDARD},\\
\text{far pressure harmonic in core}
&:\ \mathrm{PROVED},\\
\text{far-pressure derivative decay}
&:\ \mathrm{PROVED},\\
\text{5D harmonic-matrix finite-dimensionalization}
&:\ \mathrm{PROVED},\\
\text{spatially varying far remainder gains }\kappa^{-1}
&:\ \mathrm{PROVED},\\
\text{finite-dimensionalization}\Rightarrow\text{smallness}
&:\ \mathrm{FALSE/NO\mbox{-}GO},\\
\text{far pressure decoupling under bounded }\mathfrak E_R
&:\ \mathrm{PROVED\ CONDITIONAL},\\
\text{unconditional far-pressure decoupling}
&:\ \mathrm{OPEN/NO\mbox{-}GO\ from\ energy},\\
\text{harmonic pressure-matrix/operator coupling rigidity}
&:\ \mathrm{OPEN}.
\end{aligned}
}
$$

---

# 43. 結論

C3-O 告訴我們：

$$
\boxed{
\text{balance ratio不夠；
必須看 operator}.
}
$$

C3-P 現在得到現成的 theorem-backed operator necessity：

$$
\boxed{
\mathrm{Blowup}
\Rightarrow
\int_0^{T_\ast}
\frac{
\|\mathcal Q_{SV}\|_2^2
}{
\|S\|_{\dot H^1}^2
}dt
=
\infty,
}
$$

以及：

$$
\boxed{
\limsup_{t\uparrow T_\ast}
\frac{
\|\mathcal Q_{SV}\|_2
}{
\|-\Delta S\|_2
}
\ge1.
}
$$

所以 singular dynamics必須 escape globally-regular SV model的 perturbative tube。

另一方面，

SSA model本身可 blow up，

所以：

$$
\boxed{
\text{small distance to SSA model}
}
$$

不能作 regularity方向。

pressure route也被壓清楚：

$$
\boxed{
\nabla^2p_{\rm far}
=
H_0
+
E_{\rm far},
}
$$

其中：

$$
H_0
$$

是一個：

$$
\boxed{
5\text{-dimensional constant symmetric trace-free matrix},
}
$$

而：

$$
E_{\rm far}
$$

多一個：

$$
\kappa^{-1}
$$

的 spatial-variation suppression。

但：

$$
\boxed{
\text{finite-dimensionalization}
\neq
\text{smallness}.
}
$$

normalized far-pressure strength obeys：

$$
\boxed{
|\widehat H_0|
\lesssim
\kappa^{-3}
\mathfrak E_R.
}
$$

所以真正 decoupling condition是：

$$
\boxed{
\kappa^{-3}\mathfrak E_R\to0.
}
$$

若 rescaled enstrophy爆得夠快，

遠場 pressure仍可保持 critical-size作用。

因此下一輪正式進入：

$$
\boxed{
\textbf{C3-Q — Harmonic Pressure-Matrix / Operator-Escape Coupling Rigidity}.
}
$$

真正要測：

> singular ancestry如果既要讓 regular-model operator defect變成 dissipation-scale，
> 又要讓 far pressure透過一個 5D harmonic matrix持續支援 local strain geometry，
> 這兩個 channel能不能被同一套 exact N–S constraints同時維持到無限尺度？

---

# References

1. E. Miller, *On the interaction of strain and vorticity for solutions of the Navier–Stokes equation*, arXiv:2407.02691; Pure and Applied Analysis 8 (2026).
2. E. Miller, *Finite-time blowup for a Navier–Stokes model equation for the self-amplification of strain*, arXiv:1910.05415; Analysis & PDE 16 (2023).
3. B. Álvarez-Samaniego, W. P. Álvarez-Samaniego, P. G. Fernández-Dalgo, *On the use of the Riesz transforms to determine the pressure term in the incompressible Navier–Stokes equations on the whole space*, arXiv:2004.02588; Acta Applicandae Mathematicae 176 (2021).
4. Z. Bradshaw, T.-P. Tsai, *On the local pressure expansion for the Navier–Stokes equations*, arXiv:2001.11526.
5. M. Carbone, M. Wilczek, *Only two Betchov homogeneity constraints exist for isotropic turbulence*, arXiv:2112.12820; Journal of Fluid Mechanics 948 (2022), R2.

# Internal dependencies

- `NS_C3N_LocalizedBetchov_StrainBoundaryBalance_v0.1.md`
- `NS_C3O_AdjointCore_BalanceDynamicsSeparation_v0.1.md`
- `NS_C3M_VorticityStrain_Betchov_GeometryDebt_v0.1.md`
- `NS_C3L_CriticalMomentEscape_StrainGeometryDebt_v0.1.md`
- `NS_C3K_AbsoluteOccupancy_OneMomentGap_v0.1.md`
- `NS_C3I_FrontierUVCap_DefectTrichotomy_v0.1.md`
- `NS_C3G_FirstCrossing_CausalAncestry_DepletionNoGo_v0.1.md`
- `True ETN / 無限維張力場`
- `X_Integral_Unified_Program_v0.2.md`

Next:

$$
\boxed{
\textbf{C3-Q — Harmonic Pressure-Matrix / Operator-Escape Coupling Rigidity}
}
$$
