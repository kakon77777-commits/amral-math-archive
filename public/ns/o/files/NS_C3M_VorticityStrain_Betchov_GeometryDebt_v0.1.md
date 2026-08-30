---
title: "Navier–Stokes C3-M：Vorticity–Strain 耦合、Betchov 全域坍縮與方向幾何債"
subtitle: "Vorticity–Strain Coupling, Global Betchov Collapse of Orientation, and the Geometric Debts Required by Critical Stretching"
version: "v0.1"
date: "2026-08-14"
author: "Neo.K / EveMissLab"
language: "zh-TW"
status: "Theorem-style structural reduction / no-go note"
epistemic_status: "Exact eigenframe algebra + Betchov identity consequences + external strain/vorticity-direction regularity inputs. Does NOT prove Navier–Stokes regularity."
---

# Navier–Stokes C3-M
# Vorticity–Strain 耦合、Betchov 全域坍縮與方向幾何債

## 0. 本輪定位

C3-L 已建立兩個獨立的 blow-up 必要 channel：

### Spectral channel

$$
\boxed{
\int_{T_\ast/2}^{T_\ast}
\sum_{q\le Q(t)}
\lambda_q\|u_q(t)\|_\infty\,dt
=
\infty.
}
$$

等價於 critical frequency-localized vorticity moment escape。

### Strain channel

hypothetical finite blow-up 必須逃出 middle-strain 的 scale-critical regularity classes，例如：

$$
\boxed{
\lambda_2^+
\notin
L_t^2L_x^3.
}
$$

本輪原問題：

> 這兩個必須同時失控的 channel，是否能由 exact vortex stretching geometry 強迫耦合？

本輪答案不是簡單的「vorticity 必須 align 某個 strain eigenvector」。

相反地，我們得到：

1. pointwise stretching 有 exact eigenframe decomposition；
2. 若 middle eigenvalue 不承擔 stretching，則 excess stretching 必須支付 principal-eigenvector alignment debt；
3. 但全空間積分有 Betchov identity：
   $$
   \int\omega\cdot S\omega=-4\int\det S,
   $$
   orientation information在 global stretching integral中完全坍縮；
4. 因此「global enstrophy growth $\Rightarrow$ principal alignment」是 no-go；
5. 真正 global carrier 是 two-positive-eigenvalue strain geometry；
6. vorticity direction coherence仍可在 localized/nonlocal stretching kernel中產生 geometric depletion；
7. 2026 最新結果進一步顯示，在指定 critical point-concentration scenario下，即使非常弱的 logarithmic-BMO direction control也足以 depletion vortex stretching；
8. 所以 hypothetical singularity 必須同時處理：
   - spectral moment escape；
   - positive middle-strain escape；
   - localized vorticity-direction roughness / non-depletion；
9. 下一個真正 frontier 是 localized Betchov compensation，而非另一個 global scalar identity。

---

# 1. Vorticity 與 strain

定義：

$$
\omega
=
\nabla\times u,
$$

$$
S
=
\frac12
\left(
\nabla u+\nabla u^\top
\right).
$$

vorticity equation：

$$
\partial_t\omega
+
(u\cdot\nabla)\omega
=
S\omega
+
\nu\Delta\omega.
$$

enstrophy identity：

$$
\boxed{
\frac12
\frac d{dt}
\|\omega\|_2^2
+
\nu
\|\nabla\omega\|_2^2
=
\int
\omega\cdot S\omega\,dx.
}
$$

stretching density：

$$
\boxed{
\mathcal S_\omega(x,t)
=
\omega\cdot S\omega.
}
$$

---

# 2. Vorticity direction

在：

$$
\omega(x,t)\ne0
$$

處，定義：

$$
\boxed{
\xi
=
\frac{\omega}{|\omega|}.
}
$$

則：

$$
\mathcal S_\omega
=
|\omega|^2
\alpha,
$$

其中：

$$
\boxed{
\alpha
=
\xi\cdot S\xi.
}
$$

$\alpha$ 是沿 vorticity direction 的 instantaneous stretching rate。

---

# 3. Strain eigenframe

令：

$$
\lambda_1
\le
\lambda_2
\le
\lambda_3
$$

為 $S$ 的 eigenvalues。

incompressibility給：

$$
\boxed{
\lambda_1+\lambda_2+\lambda_3=0.
}
$$

令：

$$
e_1,e_2,e_3
$$

為對應 orthonormal eigenvectors。

定義 orientation weights：

$$
\boxed{
c_i
=
|\xi\cdot e_i|^2.
}
$$

則：

$$
c_i\ge0,
$$

$$
c_1+c_2+c_3=1.
$$

在 eigenvalue degeneracy處，可改用 eigenspace projectors；以下 formulas在任一 orthonormal eigenbasis中成立。

---

# 4. C3-M.1：Exact Stretching-Orientation Identity

## 定理 4.1

$$
\boxed{
\alpha
=
\lambda_1c_1
+
\lambda_2c_2
+
\lambda_3c_3.
}
$$

等價地：

$$
\boxed{
\alpha
=
\lambda_2
+
(\lambda_3-\lambda_2)c_3
-
(\lambda_2-\lambda_1)c_1.
}
$$

### 證明

第一式為 Rayleigh quotient在 eigenbasis中的 expansion。

第二式使用：

$$
c_2=1-c_1-c_3.
$$

$\square$

---

# 5. 三個 stretching components

因此：

$$
\boxed{
\alpha
=
\underbrace{\lambda_2}_{\text{middle baseline}}
+
\underbrace{
(\lambda_3-\lambda_2)c_3
}_{\text{principal stretching surplus}}
-
\underbrace{
(\lambda_2-\lambda_1)c_1
}_{\text{compressive alignment depletion}}.
}
$$

這是一個 exact pointwise decomposition。

所以 vorticity direction relative to strain eigenframe不能只用「aligned / not aligned」二分。

真正有三個 typed contributions：

1. middle-eigenvalue baseline；
2. most-stretching eigenvector surplus；
3. most-compressive eigenvector depletion。

---

# 6. Positive stretching upper bound

由：

$$
-(\lambda_2-\lambda_1)c_1\le0,
$$

得：

$$
\alpha
\le
\lambda_2
+
(\lambda_3-\lambda_2)c_3.
$$

因此：

$$
\boxed{
\alpha_+
\le
\lambda_2^+
+
(\lambda_3-\lambda_2)c_3.
}
$$

其中：

$$
[x]_+=\max\{x,0\}.
$$

又：

$$
|\lambda_3-\lambda_2|
\le
\sqrt2\,|S|,
$$

故：

$$
\boxed{
\alpha_+
\le
\lambda_2^+
+
\sqrt2
|S|c_3.
}
$$

---

# 7. C3-M.2：Excess-Stretching Alignment Debt

## 定理 7.1

固定：

$$
0<\theta<1.
$$

在：

$$
\alpha_+>0
$$

且：

$$
\lambda_2^+
<
\theta\alpha_+
$$

的點上，

必有：

$$
\boxed{
c_3
\ge
\frac{
(1-\theta)\alpha_+
}{
\lambda_3-\lambda_2
}.
}
$$

特別：

$$
\boxed{
c_3
\ge
\frac{
(1-\theta)\alpha_+
}{
\sqrt2|S|
}.
}
$$

### 證明

由：

$$
\alpha_+
\le
\lambda_2^+
+
(\lambda_3-\lambda_2)c_3
$$

及：

$$
\lambda_2^+<\theta\alpha_+,
$$

得：

$$
(1-\theta)\alpha_+
<
(\lambda_3-\lambda_2)c_3.
$$

$\square$

---

# 8. 點態 carrier dichotomy

因此每一個 strong positive stretching point都必須選：

## Carrier M — Middle-strain carrier

$$
\boxed{
\lambda_2^+
\gtrsim
\alpha_+.
}
$$

或者：

## Carrier P — Principal-alignment carrier

$$
\boxed{
c_3
\gtrsim
\frac{\alpha_+}{|S|}.
}
$$

所以「vorticity是否對齊最伸長方向」只在 middle strain不足以解釋 stretching時成為必要債務。

---

# 9. Blow-up requires divergent positive stretching budget

對 maximal smooth solution，

若：

$$
T_\ast<\infty,
$$

則 bounded：

$$
\|\omega(t)\|_2
$$

near $T_\ast$ would give an $H^1$ continuation route。

因此：

$$
\limsup_{t\uparrow T_\ast}
\|\omega(t)\|_2
=
\infty.
$$

由 enstrophy identity：

$$
\frac12\|\omega(t)\|_2^2
\le
\frac12\|\omega_0\|_2^2
+
\int_0^t
\int
[\omega\cdot S\omega]_+
\,dxds.
$$

故：

$$
\boxed{
\int_0^{T_\ast}
\int
[\omega\cdot S\omega]_+
\,dxdt
=
\infty.
}
$$

---

# 10. C3-M.3：Stretching-Carrier Integral Dichotomy

由：

$$
[\omega\cdot S\omega]_+
=
|\omega|^2\alpha_+
$$

及 §6：

$$
[\omega\cdot S\omega]_+
\le
\lambda_2^+|\omega|^2
+
\sqrt2
|S|c_3|\omega|^2.
$$

因此 hypothetical blow-up implies至少一個：

$$
\boxed{
\int_0^{T_\ast}
\int
\lambda_2^+
|\omega|^2
\,dxdt
=
\infty,
}
$$

或：

$$
\boxed{
\int_0^{T_\ast}
\int
|S|
|\xi\cdot e_3|^2
|\omega|^2
\,dxdt
=
\infty.
}
$$

本文稱：

$$
\boxed{
\textbf{Middle-Strain / Principal-Alignment Carrier Dichotomy}.
}
$$

---

# 11. 重要限制

此 dichotomy 不等於：

$$
\boxed{
\text{blow-up forces vorticity to align with }e_3.
}
$$

因第一 branch：

$$
\lambda_2^+|\omega|^2
$$

本身就可承擔 divergent positive stretching。

所以任何「singularity 必然需要最大 stretching eigenvector alignment」的 universal statement在目前證據下都不合法。

---

# 12. Betchov identity

對 sufficiently decaying smooth divergence-free vector field，

有 global Betchov relation：

$$
\boxed{
\int_{\mathbb R^3}
\omega\cdot S\omega
\,dx
=
-4
\int_{\mathbb R^3}
\det S
\,dx.
}
$$

另有：

$$
\boxed{
\int|\omega|^2dx
=
2\int|S|^2dx.
}
$$

這是 exact global integral identity。

---

# 13. C3-M.4：Global Orientation Collapse

pointwise：

$$
\omega\cdot S\omega
=
|\omega|^2
\sum_i
\lambda_i c_i
$$

明確含 orientation weights：

$$
c_i.
$$

但全空間積分：

$$
\boxed{
\int
|\omega|^2
\sum_i\lambda_ic_i
\,dx
=
-4
\int
\lambda_1\lambda_2\lambda_3
\,dx.
}
$$

右側完全不含：

$$
\xi.
$$

因此：

## 定理/No-Go 13.1

global enstrophy-production identity不能單獨恢復 vorticity–strain eigenvector alignment information。

$$
\boxed{
\text{local orientation}
\overset{\int dx}{\longrightarrow}
\text{global strain determinant}
}
$$

是一個 genuine information collapse。

---

# 14. X-Integration 意義

因此下列 proof move非法：

$$
\boxed{
\int\omega\cdot S\omega\text{ large}
\Rightarrow
\text{vorticity aligns with }e_3.
}
$$

global integral已把 orientation資訊消掉。

若要研究 alignment，

必須保留：

- spatial localization；
- sign；
- eigenvalue gaps；
- vorticity direction field；
- cancellation across space。

新增：

$$
\boxed{
G_{\rm BETCHOV}
}
$$

任何 global stretching integral若被用來推出 local orientation，必須先通過 Betchov non-collapse audit。

---

# 15. Strain determinant 的 sign geometry

由：

$$
\lambda_1+\lambda_2+\lambda_3=0.
$$

若：

$$
\lambda_2\le0,
$$

則：

$$
\lambda_1\le\lambda_2\le0\le\lambda_3,
$$

所以：

$$
\det S
=
\lambda_1\lambda_2\lambda_3
\ge0.
$$

因此：

$$
\boxed{
-4\det S
\le0.
}
$$

positive global enstrophy production的 strain-only carrier必須來自：

$$
\boxed{
\lambda_2>0
}
$$

regions，亦即兩個 positive strain eigenvalues、一個 negative eigenvalue的 geometry。

---

# 16. Middle-eigenvalue upper bound

若：

$$
\lambda_2>0,
$$

令：

$$
a=-\lambda_1>0,
\quad
b=\lambda_2>0,
\quad
c=\lambda_3>0.
$$

trace-free給：

$$
a=b+c.
$$

則：

$$
-\det S
=
abc
=
bc(b+c).
$$

而：

$$
|S|^2
=
a^2+b^2+c^2
=
2(b^2+bc+c^2).
$$

因此：

$$
\boxed{
-\det S
\le
\frac12
\lambda_2^+
|S|^2.
}
$$

所以：

$$
\boxed{
-4\det S
\le
2
\lambda_2^+
|S|^2.
}
$$

這給 global middle-strain carrier一個直接 algebraic來源。

---

# 17. C3-M.5：Global Stretching is a Two-Positive-Eigenvalue Phenomenon

Betchov + §15–16 表示：

$$
\boxed{
\int\omega\cdot S\omega
=
-4\int\det S
}
$$

的 positive contribution在 global strain representation中只能由：

$$
\boxed{
\lambda_2>0
}
$$

的 two-stretching-directions geometry承擔。

所以 middle eigenvalue criterion並非任意 analytic artefact；

它直接對應 global enstrophy-production sign geometry。

---

# 18. Middle-eigenvector alignment不是 zero stretching

若：

$$
\xi=e_2,
$$

則：

$$
\boxed{
\alpha=\lambda_2.
}
$$

因此：

- 若 $\lambda_2<0$：depletion；
- 若 $\lambda_2=0$：no stretching；
- 若 $\lambda_2>0$：仍有 positive stretching。

所以：

$$
\boxed{
\text{vorticity aligns with middle eigenvector}
\not\Rightarrow
\text{stretching vanishes}.
}
$$

它只移除：

$$
e_3
$$

surplus與：

$$
e_1
$$

depletion，留下 middle baseline。

---

# 19. Alignment folklore no-go

numerical literature常觀察：

$$
\omega
$$

傾向 align：

$$
e_2.
$$

但從 exact algebra不能推出：

$$
\boxed{
e_2\text{-alignment alone regularizes N--S}.
}
$$

真正 relevant quantity仍包括：

$$
\lambda_2^+.
$$

這與 middle-eigenvalue regularity theory相容：

即使 alignment fixed，

若：

$$
\lambda_2^+
$$

進入 critical divergence，

stretching仍可持續。

---

# 20. Vorticity-direction coherence是另一種 geometry

必須區分：

## Local eigenframe alignment

$$
\boxed{
\xi(x,t)\cdot e_i(x,t)
}
$$

描述同一點上 vorticity 相對 strain eigenframe。

## Spatial direction coherence

$$
\boxed{
\xi(x,t)-\xi(y,t)
}
$$

描述不同空間點上的 vorticity direction variation。

Constantin–Fefferman 型 geometric depletion主要作用於第二種。

兩者不是同一資訊。

---

# 21. External geometric depletion：direction coherence

Constantin–Fefferman 的經典結果表明：

若 high-vorticity regions中的 vorticity direction具有 sufficiently strong spatial coherence，例如 Lipschitz-type control，

則 vortex stretching的 nonlocal singular kernel會被 geometric depletion，

從而得到 regularity。

後續 Beirão da Veiga–Berselli 等工作弱化所需方向正則性。

因此 hypothetical singularity必須避免所有適用的 direction-coherence regularity hypotheses。

---

# 22. 2026 最新 geometric depletion input

Zoran Grujić 2026 的 primary preprint研究一類：

$$
\boxed{
\text{critical point singularities}
}
$$

其中 vorticity magnitude呈：

$$
L^{3/2,\infty}
$$

critical concentration。

其結果指出：

若 local vorticity direction屬於 logarithmically weighted：

$$
\boxed{
\mathrm{bmo}_{1/|\log r|}
}
$$

則 vortex stretching可取得 logarithmic depletion，

最終排除該類 finite-time singularity scenario。

此 theorem：

- 很新；
- 很弱的 direction control仍可有效；
- 但具有特定 critical point-concentration hypotheses。

所以本文只作：

$$
\boxed{
\text{conditional latest geometric interface}.
}
$$

---

# 23. C3-M.6：Directional-Roughness Debt（conditional）

在 Grujić 2026 所處理的 critical point-concentration scenario中，

hypothetical blow-up必須：

$$
\boxed{
\xi
\notin
\mathrm{bmo}_{1/|\log r|}
}
$$

在其 theorem所要求的 localized sense。

因此：

$$
\boxed{
\text{critical concentration}
+
\text{too much direction coherence}
\Rightarrow
\text{singularity evasion}.
}
$$

所以該 branch若要存活，必須支付：

$$
\boxed{
\textbf{Directional Roughness Debt}.
}
$$

---

# 24. 這和 e3 alignment完全不同

vorticity可以：

$$
\xi(x)
\approx e_3(x)
$$

在每一點成立，

但：

$$
e_3(x)
$$

本身在空間上劇烈 oscillate。

反之，

$\xi$ 可以 spatially smooth，

但相對 local $e_3$ 完全不 aligned。

所以：

$$
\boxed{
\text{principal-eigenvector alignment}
\neq
\text{vorticity-direction coherence}.
}
$$

X-Integration 必須保存兩個不同 type。

---

# 25. Miller 2024/2026 新 identity

Evan Miller 的工作：

*On the interaction of strain and vorticity for solutions of the Navier–Stokes equation*

在 2026 revised/published version中證明：

$$
\boxed{
\left\langle
-\Delta S,
\omega\otimes\omega
\right\rangle
=
0.
}
$$

對 divergence-free vector fields成立。

這是一個很強的 reverse-coupling orthogonality。

---

# 26. C3-M.7：Reverse Vorticity-to-Strain Driver No-Go

strain equation含有：

$$
P_{st}(\omega\otimes\omega)
$$

型 vorticity-to-strain coupling。

但：

$$
\boxed{
\langle-\Delta S,\omega\otimes\omega\rangle=0
}
$$

表示在 strain：

$$
\dot H^1
$$

energy level，

這個 component不直接驅動 higher strain norm growth。

Miller進一步證明 isolating 此 strain–vorticity interaction的 model equation具有 global regularity。

因此：

$$
\boxed{
\text{「vorticity作用到strain」
本身不是足以解釋 N--S blow-up 的 driver}.
}
$$

full equation的：

- strain self-amplification；
- advection；
- their alignment/cancellation；

不能被刪掉。

---

# 27. 重要最新結構訊號

Miller 2024/2026 結果使我們的 C3-L：

$$
\text{moment raising}
\to
\text{vortex stretching debt}
$$

再細分。

不是所有 strain–vorticity nonlinear coupling都 equally dangerous。

至少有一個 reverse channel：

$$
\omega\otimes\omega
\to S
$$

在：

$$
\dot H^1(S)
$$

pairing中 exact orthogonal。

所以真正 dangerous geometry更接近：

$$
\boxed{
\text{strain self-amplification}
+
\text{advection / depletion balance}
}
$$

而非單純「vorticity很大」。

---

# 28. Spectral–strain coupling目前能證到哪？

目前有：

$$
\boxed{
\mathrm{Blowup}
\Rightarrow
\mathfrak T_{\rm spec}=\infty
}
$$

與：

$$
\boxed{
\mathrm{Blowup}
\Rightarrow
\mathfrak T_{\lambda_2}=\infty
}
$$

類型的平行 necessary conditions。

pointwise stretching又有：

$$
\boxed{
\alpha_+
\le
\lambda_2^+
+
\sqrt2|S|c_3.
}
$$

但 Betchov identity告訴我們：

$$
\boxed{
\int
|\omega|^2\alpha
=
-4\int\det S.
}
$$

所以 global integrated stretching不保留：

$$
c_3.
$$

因此目前不能證：

$$
\boxed{
\text{spectral moment escape}
\Rightarrow
\text{principal alignment divergence}.
}
$$

---

# 29. 真正新的 coupling target

要把 spectral vorticity moment與 strain geometry真正耦合，

必須做**localized** quantity。

例如 ancestry core：

$$
\chi_n(x)
$$

上研究：

$$
\boxed{
\int
\chi_n
\omega\cdot S\omega\,dx
}
$$

與：

$$
\boxed{
-4\int
\chi_n
\det S\,dx.
}
$$

兩者不再相等；

差：

$$
\boxed{
\mathfrak B_{\chi_n}
=
\int
\chi_n
\left(
\omega\cdot S\omega
+
4\det S
\right)
dx
}
$$

記錄被 global Betchov integration抹掉的 local orientation/cancellation information。

---

# 30. Localized Betchov defect

定義：

$$
\boxed{
b(x,t)
=
\omega\cdot S\omega
+
4\det S.
}
$$

global：

$$
\boxed{
\int b(x,t)\,dx=0.
}
$$

但局部：

$$
\boxed{
\int\chi b
}
$$

一般非零。

因此任何 core內 positive：

$$
\mathfrak B_\chi
$$

都必須在 complementary region由 negative contribution補償：

$$
\boxed{
\int\chi b
=
-
\int(1-\chi)b.
}
$$

這是 exact spatial compensation identity。

它尚不是 transport theorem。

---

# 31. C3-M.8：Localized Orientation-Compensation Debt

如果 ancestry core中：

$$
\boxed{
\int
\chi
\left(
\omega\cdot S\omega+4\det S
\right)
dx
\gg0,
}
$$

則 outside core必有完全相反的：

$$
\boxed{
-\int(1-\chi)b
}
$$

compensation。

所以：

$$
\boxed{
\text{local orientation surplus}
}
$$

不能作為孤立 scalar source存在；

它伴隨一個：

$$
\boxed{
\textbf{Spatial Betchov Compensation Debt}.
}
$$

目前未知此 compensation是否可轉成：

- boundary flux；
- spatial transport；
- frequency transfer；
- pressure-mediated nonlocality。

這正是下一 frontier。

---

# 32. X-Integration guards 更新

## G-EIG

保存：

$$
(\lambda_1,\lambda_2,\lambda_3).
$$

## G-ORI

保存：

$$
(c_1,c_2,c_3).
$$

## G-DIR

保存 spatial vorticity direction regularity：

$$
\xi(x)-\xi(y).
$$

不得與 G-ORI混同。

## G-BETCHOV

global integration會消掉 orientation資訊；

任何 local geometry claim不得由 global stretching integral逆推。

## G-REV

保存 Miller reverse-coupling orthogonality：

$$
\langle-\Delta S,\omega\otimes\omega\rangle=0.
$$

## G-COMP

localized Betchov surplus必須保存其 global compensation來源。

---

# 33. True ETN 更新

目前 stretching tension不能只寫：

$$
\Theta_{\rm stretch}
=
\omega\cdot S\omega.
$$

應拆成：

$$
\boxed{
\Theta_{\rm stretch}
=
\left\langle
|\omega|,
\lambda_2,
\lambda_3-\lambda_2,
c_1,c_3,
\xi\text{-coherence},
b_{\rm Betchov}
\right\rangle.
}
$$

其中：

- $|\omega|$ = magnitude；
- $\lambda_2$ = middle baseline；
- $\lambda_3-\lambda_2$ = principal gap；
- $c_3$ = principal alignment；
- $c_1$ = compressive depletion；
- spatial $\xi$ coherence = nonlocal geometric depletion；
- $b_{\rm Betchov}$ = local/global cancellation defect。

這是一個真正 typed geometry state。

---

# 34. Survivor geometry v3

hypothetical singular route現在至少要通過：

## S1 — Critical spectral moment escape

$$
\boxed{
\int
\sum_{q\le Q}
\|\omega_q\|_\infty dt
=
\infty.
}
$$

## S2 — Positive middle-strain critical escape

必須逃出：

$$
\lambda_2^+
$$

的 critical regularity classes。

## S3 — Stretching carrier

local positive stretching由：

- middle-strain；
- principal alignment；

之一承擔。

## S4 — Global Betchov consistency

orientation contribution不能違反：

$$
\int\omega\cdot S\omega
=
-4\int\det S.
$$

## S5 — Directional non-depletion

在適用 concentration scenario下，

vorticity direction不能太 coherent，否則 known geometric depletion theorem排除 singularity。

## S6 — Reverse-coupling orthogonality

不能把：

$$
\omega\otimes\omega\to S
$$

當成 unrestricted higher-strain driver。

---

# 35. 這是否得到 contradiction？

沒有。

目前完全可能：

1. spectral vorticity moment diverges；
2. $\lambda_2^+$ critical norm diverges；
3. local vorticity direction rough；
4. Betchov compensation在 shrinking ancestry core外完成；
5. full strain self-amplification / advection維持 singular route。

所以 full N–S proof尚未關閉。

---

# 36. C3-M 的主要 no-go

### NG-M1

$$
\text{large global stretching}
\Rightarrow
e_3\text{-alignment}.
$$

FALSE / unsupported because Betchov global collapse。

### NG-M2

$$
e_2\text{-alignment}
\Rightarrow
\text{zero stretching}.
$$

FALSE：

$$
\alpha=\lambda_2.
$$

### NG-M3

$$
\text{vorticity-direction coherence}
=
\text{strain-eigenvector alignment}.
$$

FALSE：different geometric types。

### NG-M4

$$
\omega\otimes\omega\text{ reverse coupling}
\Rightarrow
\text{strain higher-norm growth}.
$$

FALSE at the Miller:

$$
\langle-\Delta S,\omega\otimes\omega\rangle
$$

pairing level。

### NG-M5

$$
\text{spectral moment divergence}
\Rightarrow
\text{alignment divergence}.
$$

NOT PROVED。

---

# 37. 新 frontier：C3-N

本輪的核心修正：

$$
\boxed{
\text{global orientation information collapses under Betchov identity}.
}
$$

所以真正值得攻的不是另一個 global alignment norm。

正式下一題：

$$
\boxed{
\textbf{C3-N — Localized Betchov Compensation and Strain Self-Amplification Rigidity}.
}
$$

---

# 38. C3-N proof obligations

## N1 — Localized Betchov formula

對 smooth cutoff：

$$
\chi_{x_0,R},
$$

推導：

$$
\int\chi
\left(
\omega\cdot S\omega
+
4\det S
\right)
$$

的 exact boundary/commutator representation。

目標：

$$
\boxed{
\mathfrak B_\chi
=
\text{boundary derivative terms}.
}
$$

## N2 — Scaling of compensation

若：

$$
R\sim\lambda^{-1},
$$

量化：

$$
\mathfrak B_\chi
$$

在 ancestry parabolic core中的 critical scaling。

## N3 — Compensation locality

研究 positive core Betchov defect是否必須由：

- nearby shell；
- nearby space；
- or pressure/nonlocal tail

補償。

## N4 — Strain determinant ancestry

把：

$$
-\det S
$$

按 absolute shells / packets分解。

研究：

$$
\lambda_2>0
$$

two-stretching geometry是否沿 causal ancestry持續。

## N5 — Miller 2026 advection-depletion interface

使用：

$$
\langle-\Delta S,\omega\otimes\omega\rangle=0
$$

與其 regularity criteria，

判定 full N–S survivor中：

$$
\boxed{
\text{strain self-amplification}
}
$$

與：

$$
\boxed{
\text{advection depletion}
}
$$

必須維持什麼 imbalance。

## N6 — Directional roughness branch

在 critical point-concentration branch，

加入 Grujić 2026：

$$
\xi\notin \mathrm{bmo}_{1/|\log r|}
$$

failure certificate。

研究此 directional roughness是否增加 Betchov compensation cost。

## N7 — Localized strain/vorticity closure

若 ancestry core外 compensation可 decouple，

嘗試得到 closed localized strain-production model。

若不能，formalize nonlocal compensation frontier。

---

# 39. 正式狀態

$$
\boxed{
\begin{aligned}
\text{eigenframe stretching identity}
&:\ \mathrm{PROVED},\\
\text{middle/principal pointwise carrier bound}
&:\ \mathrm{PROVED},\\
\text{excess-stretching alignment debt}
&:\ \mathrm{PROVED},\\
\text{positive stretching integral divergence under blow-up}
&:\ \mathrm{PROVED/STANDARD},\\
\text{stretching-carrier integral dichotomy}
&:\ \mathrm{PROVED},\\
\text{Betchov identity}
&:\ \mathrm{STANDARD/EXTERNAL},\\
\text{global orientation collapse}
&:\ \mathrm{PROVED/DERIVED},\\
-\det S\le\frac12\lambda_2^+|S|^2
&:\ \mathrm{PROVED},\\
\text{middle-eigenvector alignment implies zero stretching}
&:\ \mathrm{FALSE/NO\mbox{-}GO},\\
\text{vorticity direction coherence regularizes under known hypotheses}
&:\ \mathrm{EXTERNAL},\\
\text{2026 logarithmic depletion interface}
&:\ \mathrm{EXTERNAL/CONDITIONAL},\\
\langle-\Delta S,\omega\otimes\omega\rangle=0
&:\ \mathrm{EXTERNAL\ THEOREM},\\
\text{reverse vorticity--strain coupling as sole driver}
&:\ \mathrm{NO\mbox{-}GO},\\
\text{localized Betchov compensation rigidity}
&:\ \mathrm{OPEN}.
\end{aligned}
}
$$

---

# 40. 結論

C3-L 把 missing frequency moment轉成：

$$
\boxed{
\text{critical vorticity moment}
+
\text{strain geometry debt}.
}
$$

C3-M 現在把這個 geometry debt拆清楚。

pointwise：

$$
\boxed{
\alpha
=
\lambda_2
+
(\lambda_3-\lambda_2)c_3
-
(\lambda_2-\lambda_1)c_1.
}
$$

所以 strong stretching若不是由：

$$
\lambda_2^+
$$

承擔，

就必須支付：

$$
\boxed{
e_3\text{-alignment debt}.
}
$$

但 global integration後：

$$
\boxed{
\int\omega\cdot S\omega
=
-4\int\det S,
}
$$

orientation全部消失。

因此：

$$
\boxed{
\text{local alignment}
\neq
\text{global stretching driver}.
}
$$

global net enstrophy production實際壓回：

$$
\boxed{
\lambda_2>0
}
$$

的 two-positive-eigenvalue strain geometry。

而 vorticity direction真正有已知 regularizing力量的位置，是：

$$
\boxed{
\text{spatial coherence / nonlocal geometric depletion}.
}
$$

最新 2026 工作甚至顯示，在特定 critical point-concentration scenario下，非常弱的 logarithmic-BMO direction regularity已足以避免 singularity。

最後，Miller 2026 的：

$$
\boxed{
\langle-\Delta S,\omega\otimes\omega\rangle=0
}
$$

又告訴我們：

$$
\boxed{
\text{not every vorticity--strain coupling drives higher strain growth}.
}
$$

所以 survivor進一步被壓向：

$$
\boxed{
\textbf{localized strain self-amplification}
+
\textbf{failure of advection/directional depletion}
+
\textbf{Betchov compensation across the ancestry core}.
}
$$

下一輪：

$$
\boxed{
\textbf{C3-N — Localized Betchov Compensation and Strain Self-Amplification Rigidity}.
}
$$
