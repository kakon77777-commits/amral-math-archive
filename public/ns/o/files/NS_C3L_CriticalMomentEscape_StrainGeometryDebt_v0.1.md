---
title: "Navier–Stokes C3-L：Critical Vorticity Moment Escape、Active-Occupancy Dichotomy 與 Strain-Geometry Debt"
subtitle: "Critical Vorticity-Moment Divergence, Active-Shell Moment Escape, and the Geometric Debt of Raising One Frequency Moment"
version: "v0.1"
date: "2026-08-14"
author: "Neo.K / EveMissLab"
language: "zh-TW"
status: "Theorem-style structural reduction / no-go note"
epistemic_status: "Uses external frequency-localized regularity and strain-eigenvalue criteria, plus self-contained dyadic consequences. Does NOT prove Navier–Stokes regularity."
---

# Navier–Stokes C3-L
# Critical Vorticity Moment Escape、Active-Occupancy Dichotomy 與 Strain-Geometry Debt

## 0. 本輪定位

C3-K 已經把一路以來的 energy-budget gap 壓成：

$$
\boxed{
\textbf{One-Frequency-Moment Gap}.
}
$$

對 local heterochiral interaction：

$$
\mathcal R_\tau
\sim
\lambda_\tau
\dot e_\tau,
$$

所以 ordinary energy turnover 即使可加總：

$$
\sum_\tau
\int
|\dot e_\tau|dt
<
\infty,
$$

也不控制：

$$
\sum_\tau
\int
\lambda_\tau
|\dot e_\tau|dt.
$$

另一方面，absolute active-shell worldvolume滿足：

$$
\boxed{
M_1(\beta)
=
\sum_{q,\sigma}
\lambda_q
|A_{q,\sigma}(\beta)|
<
\infty.
}
$$

本輪原問題是：

> hypothetical blow-up 是否真的必須把下一個 frequency moment推到 infinity？

答案：

$$
\boxed{
\textbf{YES，已有 frequency-localized regularity theorem 的 contrapositive 可直接證。}
}
$$

所以 C3-L 不再猜 Critical Moment Escape 是否存在。

真正工作改成：

1. 把 Cheskidov–Dai criterion轉成 exact divergent critical vorticity moment；
2. 和 C3-K 的 finite absolute occupancy帳本合併；
3. 得到一個 sharp moment-escape dichotomy；
4. 測試 enstrophy是否能免費補上 missing moment；
5. 證明不能：升矩必須支付 vortex-stretching geometry debt；
6. 接到 middle strain eigenvalue 的 scale-critical regularity criteria；
7. 得到 spectral moment escape + geometric strain escape 的雙重必要條件。

---

# 1. 設定

考慮三維不可壓 Navier–Stokes：

$$
\partial_tu
+
(u\cdot\nabla)u
+
\nabla p
=
\nu\Delta u,
$$

$$
\nabla\cdot u=0,
$$

在：

$$
\mathbb R^3\times[0,T_\ast).
$$

假設：

$$
0<T_\ast<\infty
$$

為 hypothetical maximal singular time。

使用 Littlewood–Paley shells：

$$
u_q=\Delta_qu,
$$

$$
\lambda_q=2^q.
$$

定義：

$$
\boxed{
a_q(t)
=
\frac{
\|u_q(t)\|_\infty
}{
\nu\lambda_q
}.
}
$$

若需要 helicity refinement：

$$
a_q^\sigma(t)
=
\frac{
\|u_q^\sigma(t)\|_\infty
}{
\nu\lambda_q
}.
$$

---

# 2. Dissipation wavenumber

令：

$$
\Lambda(t)
=
\lambda_{Q(t)}
$$

為 Cheskidov–Shvydkoy / Cheskidov–Dai 型 dissipation wavenumber。

其基本語意：

在：

$$
q>Q(t)
$$

的 sufficiently high shells，nonlinear shell amplitude已落入 viscosity-dominated smallness threshold。

C2 已經使用外部結果：

$$
\boxed{
\Lambda\in L^1(0,T_\ast)
}
$$

對 Leray–Hopf solutions成立，

且 hypothetical blow-up要求：

$$
\boxed{
\Lambda\notin L^{5/2}(0,T_\ast).
}
$$

---

# 3. External theorem：frequency-localized critical toll

Cheskidov–Dai 的 3D NSE criterion有以下形式：

若：

$$
\limsup_{q\to\infty}
\int_{T/2}^{T}
1_{\{q\le Q(t)\}}
\lambda_q
\|u_q(t)\|_\infty
\,dt
$$

小於 sufficiently small universal/viscosity-normalized threshold，

則 solution regular through：

$$
T.
$$

因此若：

$$
T=T_\ast
$$

真是 singular time，

其 contrapositive給：

$$
\boxed{
\limsup_{q\to\infty}
J_q
>
c_\ast
}
$$

其中：

$$
\boxed{
J_q
=
\int_{T_\ast/2}^{T_\ast}
1_{\{q\le Q(t)\}}
\lambda_q
\|u_q(t)\|_\infty
\,dt.
}
$$

---

# 4. C3-L.1：Critical Vorticity-Moment Divergence

## 定理 4.1

hypothetical finite blow-up implies：

$$
\boxed{
\sum_q
J_q
=
\infty.
}
$$

等價地：

$$
\boxed{
\nu
\int_{T_\ast/2}^{T_\ast}
\sum_{q\le Q(t)}
\lambda_q^2
a_q(t)
\,dt
=
\infty.
}
$$

### 證明

由：

$$
\limsup_{q\to\infty}J_q>c_\ast,
$$

存在：

$$
c_1>0
$$

及 infinitely many：

$$
q
$$

使：

$$
J_q\ge c_1.
$$

故：

$$
\sum_qJ_q=\infty.
$$

所有 terms nonnegative，所以 Tonelli 給：

$$
\sum_qJ_q
=
\int
\sum_{q\le Q(t)}
\lambda_q\|u_q(t)\|_\infty
dt.
$$

再用：

$$
\lambda_q\|u_q\|_\infty
=
\nu\lambda_q^2a_q.
$$

證畢。$\square$

---

# 5. Vorticity interpretation

令：

$$
\omega
=
\nabla\times u.
$$

在一個 fixed annulus：

$$
|\xi|\sim\lambda_q,
$$

curl 與 Biot–Savart inverse都是 smooth annular multipliers。

因此：

$$
\boxed{
\|\omega_q\|_\infty
\asymp
\lambda_q
\|u_q\|_\infty.
}
$$

所以定理 4.1 可讀成：

$$
\boxed{
\int_{T_\ast/2}^{T_\ast}
\sum_{q\le Q(t)}
\|\omega_q(t)\|_\infty
\,dt
=
\infty
}
$$

up to universal annular constants。

本文稱：

$$
\boxed{
\textbf{Critical Vorticity-Moment Escape}.
}
$$

---

# 6. 和 C3-K 的 moment notation 對齊

定義 amplitude-weighted second moment：

$$
\boxed{
\mathfrak M_2^{amp}
=
\int_{T_\ast/2}^{T_\ast}
\sum_{q\le Q(t)}
\lambda_q^2
a_q(t)
\,dt.
}
$$

則：

$$
\boxed{
\mathrm{Blowup}
\Rightarrow
\mathfrak M_2^{amp}
=
\infty.
}
$$

而 C3-K 的 threshold occupancy控制：

$$
\boxed{
M_1(\beta)
=
\sum_q
\lambda_q
|A_q(\beta)|
<
\infty,
}
$$

其中：

$$
A_q(\beta)
=
\{
t:
a_q(t)\ge\beta
\}.
$$

因此 low-order finite / next critical amplitude moment infinite 已經是 theorem-level reduction。

---

# 7. Threshold split

固定任意：

$$
\beta>0.
$$

將：

$$
a_q
=
a_q1_{\{a_q<\beta\}}
+
a_q1_{\{a_q\ge\beta\}}.
$$

因此：

$$
\mathfrak M_2^{amp}
=
\mathfrak M_{2,<\beta}
+
\mathfrak M_{2,\ge\beta}.
$$

---

# 8. Subthreshold contribution由 $\Lambda^2$ 控制

當：

$$
q\le Q(t),
$$

有 geometric sum：

$$
\sum_{q\le Q(t)}
\lambda_q^2
\le
C
\Lambda(t)^2.
$$

所以：

$$
\boxed{
\mathfrak M_{2,<\beta}
\le
C\beta
\int_{T_\ast/2}^{T_\ast}
\Lambda(t)^2\,dt.
}
$$

因此若：

$$
\Lambda\in L^2(T_\ast/2,T_\ast),
$$

subthreshold part必 finite。

---

# 9. C3-L.2：Critical-Moment Carrier Dichotomy

## 定理 9.1

若 $T_\ast$ 為 finite singular time，則：

$$
\boxed{
\int_{T_\ast/2}^{T_\ast}
\Lambda(t)^2dt
=
\infty
}
$$

或者，若：

$$
\Lambda\in L^2,
$$

則對每一個 fixed：

$$
\beta>0,
$$

都有：

$$
\boxed{
\mathfrak M_{2,\ge\beta}
=
\infty.
}
$$

### 證明

總：

$$
\mathfrak M_2^{amp}
=
\infty.
$$

若：

$$
\int\Lambda^2<\infty,
$$

由上一節：

$$
\mathfrak M_{2,<\beta}<\infty.
$$

所以 active part必發散。$\square$

---

# 10. Branch A：frontier second-moment spike

第一 branch：

$$
\boxed{
\Lambda\notin L^2.
}
$$

注意：

N–S scaling下：

$$
\Lambda_\lambda(t)
=
\lambda
\Lambda(\lambda^2t).
$$

因此：

$$
\boxed{
\int
\Lambda(t)^2dt
}
$$

是 scale-invariant。

所以：

$$
\boxed{
\Lambda\notin L^2
}
$$

是一個真正 critical frontier-spike mechanism。

這比 C2 的：

$$
\Lambda\in L^1
$$

finite帳本正好高一個 scaling level。

---

# 11. Branch B：active amplitude carries all critical escape

若：

$$
\Lambda\in L^2,
$$

則對任意：

$$
\beta>0,
$$

critical moment divergence必須集中到：

$$
\boxed{
a_q\ge\beta
}
$$

的 absolute active sets。

這把：

$$
\text{many tiny subthreshold modes}
$$

route排除。

但 active amplitude本身仍可能非常大。

---

# 12. Energy-level upper bound on $a_q$

由 Bernstein與 global energy：

$$
\|u_q(t)\|_\infty
\le
C
\lambda_q^{3/2}
\|u_q(t)\|_2
\le
C
\lambda_q^{3/2}
\|u_0\|_2.
$$

所以：

$$
\boxed{
a_q(t)
\le
C
\frac{
\|u_0\|_2
}{
\nu
}
\lambda_q^{1/2}.
}
$$

---

# 13. C3-L.3：Active $5/2$-Moment Escape

## 定理 13.1

假設：

$$
T_\ast
$$

singular且：

$$
\Lambda\in L^2(T_\ast/2,T_\ast).
$$

則對每個：

$$
\beta>0,
$$

有：

$$
\boxed{
\sum_q
\lambda_q^{5/2}
\left|
A_q(\beta)
\cap
(T_\ast/2,T_\ast)
\right|
=
\infty.
}
$$

### 證明

由定理 9.1：

$$
\int
\sum_{q\le Q}
\lambda_q^2
a_q
1_{\{a_q\ge\beta\}}
dt
=
\infty.
$$

而：

$$
\lambda_q^2a_q
\le
C
\frac{\|u_0\|_2}{\nu}
\lambda_q^{5/2}.
$$

因此若：

$$
\sum_q
\lambda_q^{5/2}
|A_q(\beta)|
<
\infty,
$$

上式 active amplitude integral必 finite，矛盾。$\square$

---

# 14. 和 C3-K 結合

C3-K 已證：

$$
\boxed{
\sum_q
\lambda_q
|A_q(\beta)|
<
\infty.
}
$$

所以 Branch B 同時具有：

$$
\boxed{
M_1(\beta)<\infty
}
$$

與：

$$
\boxed{
M_{5/2}(\beta)=\infty.
}
$$

這是一個非常清楚的 moment-escape signature：

$$
\boxed{
\text{finite first occupation moment}
+
\text{divergent }5/2\text{-moment}.
}
$$

---

# 15. 和 C2 spike packing 完全接起來

C2 已得到 dissipation-wavenumber：

$$
\boxed{
\Lambda\in L^1
\setminus
L^{5/2}.
}
$$

C3-L 再細分：

## Branch A

$$
\boxed{
\Lambda\in L^1\setminus L^2.
}
$$

critical divergence直接由 frontier spike承擔。

## Branch B

$$
\boxed{
\Lambda\in L^2\setminus L^{5/2}
}
$$

時，

對任意 fixed threshold：

$$
\beta>0,
$$

absolute active shell occupancy必有：

$$
\boxed{
M_{5/2}(\beta)=\infty.
}
$$

所以：

$$
\boxed{
\text{frontier尖峰}
\quad\text{vs}\quad
\text{active-shell高矩 multiplicity}
}
$$

成為 exact dichotomy。

---

# 16. 這是否已經 contradiction？

沒有。

抽象例子：

$$
|A_q|
\sim
\lambda_q^{-2}.
$$

則：

$$
M_1
\sim
\sum_q\lambda_q^{-1}
<
\infty,
$$

而：

$$
M_{5/2}
\sim
\sum_q\lambda_q^{1/2}
=
\infty.
$$

同時 total physical time：

$$
\sum_q|A_q|
<
\infty.
$$

所以 Branch B 完全可以 Zeno-pack。

這仍不是 N–S construction，只是 moment bookkeeping compatibility。

---

# 17. 最自然的 moment-raising候選：enstrophy

令：

$$
\omega
=
\nabla\times u,
$$

strain tensor：

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
\boxed{
\partial_t\omega
+
(u\cdot\nabla)\omega
=
S\omega
+
\nu\Delta\omega.
}
$$

因 antisymmetric rotation part不貢獻：

$$
\omega\cdot\nabla u\,\omega
=
\omega\cdot S\omega.
$$

---

# 18. Exact enstrophy identity

對 smooth solution：

$$
\boxed{
\frac12
\frac d{dt}
\|\omega(t)\|_2^2
+
\nu
\|\nabla\omega(t)\|_2^2
=
\int_{\mathbb R^3}
\omega\cdot S\omega\,dx.
}
$$

左側 dissipation：

$$
\|\nabla\omega\|_2^2
\asymp
\|u\|_{\dot H^2}^2
$$

確實比 energy dissipation：

$$
\|u\|_{\dot H^1}^2
$$

多一個 derivative。

看起來像我們一直找的：

$$
\boxed{
\text{moment-raising identity}.
}
$$

---

# 19. 但 higher moment不是免費的

積分 enstrophy identity：

$$
\boxed{
\nu
\int_0^T
\|\nabla\omega\|_2^2dt
=
\frac12
\|\omega_0\|_2^2
-
\frac12
\|\omega(T)\|_2^2
+
\int_0^T
\int
\omega\cdot S\omega
\,dxdt.
}
$$

所以若要 control higher derivative dissipation，

必須 control：

$$
\boxed{
\mathcal V_S
=
\int
\omega\cdot S\omega.
}
$$

這是 vortex stretching。

---

# 20. C3-L.4：Moment-Raising Geometry Debt No-Go

## 命題 20.1

energy inequality本身不能把：

$$
\int
\|u\|_{\dot H^1}^2dt
$$

免費提升成：

$$
\int
\|u\|_{\dot H^2}^2dt.
$$

任何透過 enstrophy identity完成此提升的 argument，都必須另外控制：

$$
\boxed{
\int
\omega\cdot S\omega.
}
$$

因此：

$$
\boxed{
\text{raising one differential/frequency moment
creates a vortex-stretching geometry debt}.
}
$$

這不是 heuristic，而是 exact identity的直接邏輯後果。

---

# 21. Scaling audit

N–S scaling：

$$
u_\lambda(x,t)
=
\lambda
u(\lambda x,\lambda^2t).
$$

則：

$$
\omega_\lambda
=
\lambda^2
\omega(\lambda x,\lambda^2t).
$$

所以：

$$
\|\omega_\lambda\|_2^2
=
\lambda
\|\omega\|_2^2.
$$

且：

$$
\int
\|\nabla\omega_\lambda\|_2^2dt
=
\lambda
\int
\|\nabla\omega\|_2^2dt.
$$

stretching integral同樣 scale：

$$
\lambda.
$$

因此：

$$
\boxed{
\text{enstrophy-level identity本身位於 energy之上的同一 supercritical balance level}.
}
$$

沒有隱藏 scale advantage。

---

# 22. Enstrophy no-go 的真正意義

所以「用 vorticity / enstrophy補一個 moment」並不是錯。

錯的是假設：

$$
\boxed{
\text{higher moment會自動帶來 finite budget}.
}
$$

實際上：

$$
\boxed{
\text{higher dissipation}
=
\text{higher stock change}
+
\text{vortex stretching}.
}
$$

真正剩下的就是 geometry。

---

# 23. External geometry theorem：middle strain eigenvalue

令 strain eigenvalues排序：

$$
\lambda_1(x,t)
\le
\lambda_2(x,t)
\le
\lambda_3(x,t),
$$

並定義：

$$
\boxed{
\lambda_2^+
=
\max\{\lambda_2,0\}.
}
$$

因 incompressibility：

$$
\operatorname{tr}S=0.
$$

所以：

$$
\lambda_2>0
$$

意味至少兩個 strain directions是 stretching-type，另一方向必 compression。

Evan Miller 的 theorem證：

若：

$$
\boxed{
\lambda_2^+
\in
L_t^rL_x^p
}
$$

且：

$$
\boxed{
\frac2r+\frac3p=2,
\qquad
\frac32<p\le\infty,
}
$$

則 solution可延拓 / regular。

---

# 24. C3-L.5：Critical Middle-Strain Divergence

取：

$$
p=3,
\qquad
r=2.
$$

hypothetical finite blow-up必須：

$$
\boxed{
\int_0^{T_\ast}
\|\lambda_2^+(t)\|_3^2dt
=
\infty.
}
$$

這是一個 scaling-critical geometric necessity。

所以 singular route不只要：

$$
\boxed{
\text{frequency moment escape},
}
$$

還必須：

$$
\boxed{
\text{positive middle-strain geometry escape}.
}
$$

---

# 25. 最新 endpoint Besov geometry guard

Guo–O 的 2025 Applied Mathematics Letters result進一步證：

若：

$$
\boxed{
\lambda_2^+
\in
L^2
\left(
0,T;
\dot B^{-1}_{\infty,\infty}
\right),
}
$$

則 local strong solution可 smooth extend。

因此 hypothetical singularity還必須失敗於：

$$
\boxed{
L_t^2\dot B^{-1}_{\infty,\infty}
}
$$

這個 critical endpoint strain-geometry control。

此結果是 Miller 所提出 Besov extension問題的 endpoint版本之一。

---

# 26. C3-L.6：Spectral–Geometric Double Escape

綜合定理 4.1 與 middle-strain criterion：

## 定理 26.1

若：

$$
T_\ast<\infty
$$

為 hypothetical singular time，

則必須同時：

$$
\boxed{
\int_{T_\ast/2}^{T_\ast}
\sum_{q\le Q(t)}
\lambda_q
\|u_q(t)\|_\infty
dt
=
\infty
}
$$

以及：

$$
\boxed{
\int_0^{T_\ast}
\|\lambda_2^+(t)\|_3^2dt
=
\infty.
}
$$

並且依 2025 endpoint result：

$$
\boxed{
\lambda_2^+
\notin
L^2_t
\dot B^{-1}_{\infty,\infty}.
}
$$

這是兩組**平行必要條件**。

目前尚未證：

$$
\boxed{
\text{spectral moment divergence}
\Rightarrow
\text{middle-strain divergence}
}
$$

或反向 implication。

不得偷寫成因果等價。

---

# 27. ETN interpretation

True ETN 現在可以把 N–S singular survivor寫成兩個必須同步失控的 typed tension channels：

## Spectral channel

$$
\boxed{
\mathfrak T_{\rm spec}
=
\int
\sum_{q\le Q(t)}
\lambda_q^2a_q(t)dt
=
\infty.
}
$$

## Geometric channel

$$
\boxed{
\mathfrak T_{\rm strain}
=
\int
\|\lambda_2^+(t)\|_3^2dt
=
\infty.
}
$$

這兩個不能壓成同一 scalar。

X-Integration必須保存：

$$
\boxed{
\text{spectral provenance}
\neq
\text{strain-eigenvalue provenance}.
}
$$

---

# 28. 新 X-Guard：Moment Raising

新增：

$$
\boxed{
G_{\rm RAISE}
}
$$

任何 proof若從 low frequency moment：

$$
M_s
$$

推出：

$$
M_{s+1}
$$

finite，

必須指出：

1. 哪個 exact equation提高 derivative；
2. 新 source term是什麼；
3. source term由哪個 independent bound控制；
4. 是否只是把 missing moment藏進 nonlinear geometry。

對 enstrophy：

$$
\boxed{
G_{\rm RAISE}
\text{輸出 debt}
=
\omega\cdot S\omega.
}
$$

---

# 29. 新 X-Guard：Geometry Non-Collapse

不得從：

$$
\|\nabla u\|
\text{ large}
$$

直接推：

$$
\lambda_2^+
\text{ large}.
$$

因：

- strain eigenvalue signs；
- vorticity orientation；
- shell cancellation；
- spatial localization；

都會被 scalar gradient norm抹掉。

所以：

$$
\boxed{
G_{\rm GEOM}
}
$$

要求 middle-eigenvalue information獨立保存。

---

# 30. Moment escape 的兩條 carrier branch

C3-L 最終把 spectral branch拆成：

## Branch A — Frontier critical spike

$$
\boxed{
\Lambda\notin L^2.
}
$$

此時 critical moment主要可由 moving dissipation frontier的 spike packing承擔。

## Branch B — Active occupancy escape

$$
\boxed{
\Lambda\in L^2
}
$$

但對所有：

$$
\beta>0,
$$

$$
\boxed{
M_{5/2}(\beta)=\infty,
}
$$

而：

$$
M_1(\beta)<\infty.
$$

此時 singularity需要 active absolute shells的 higher-moment congestion。

---

# 31. 兩 branch 都還必須通過 strain geometry

不論 A 或 B，

hypothetical blow-up仍需：

$$
\boxed{
\lambda_2^+
\notin
L_t^2L_x^3
}
$$

以及 endpoint Besov failure。

所以 survivor map：

$$
\boxed{
\begin{array}{c}
\text{Branch A：frontier }L^2\text{ spike}\\
\text{or}\\
\text{Branch B：active }5/2\text{-moment escape}
\end{array}
}
$$

必須再和：

$$
\boxed{
\text{middle-strain positive stretching divergence}
}
$$

取交集。

---

# 32. 這是不是已經等於 alignment theorem？

不是。

$\lambda_2^+$ regularity criteria限制的是 strain eigenvalue geometry。

它不等於：

$$
\boxed{
\omega
\text{ 必須精確 align with middle eigenvector}.
}
$$

Miller 的工作提供 analytic evidence / geometric interpretation，但本文不把 alignment heuristic升格成 exact necessary theorem。

若下一輪要用 alignment，必須另外找：

- Constantin–Fefferman vorticity direction coherence；
- Beirão da Veiga–Berselli 類 criteria；
- exact strain–vorticity angle identities；

重新證或引用。

---

# 33. C3-L 的 no-go 裁決

以下路線現在正式淘汰：

### NG-L1

$$
M_1<\infty
\Rightarrow
M_2<\infty.
$$

FALSE。

### NG-L2

$$
\text{energy dissipation finite}
\Rightarrow
\text{enstrophy dissipation finite}.
$$

FALSE without stretching control。

### NG-L3

$$
\text{large vorticity}
\Rightarrow
\lambda_2^+\text{ automatically large pointwise}.
$$

NOT ESTABLISHED。

### NG-L4

$$
\text{spectral moment escape}
\Rightarrow
\text{strain geometry escape}
$$

not yet proved as an implication；目前只有兩者都是 blow-up必要條件。

---

# 34. 下一個真正 frontier：C3-M

C3-L 已經回答：

> 缺的 moment 在哪裡？

它在：

$$
\boxed{
\text{frequency-localized vorticity toll}.
}
$$

也回答：

> 為什麼 enstrophy不能免費補？

因為：

$$
\boxed{
\text{vortex stretching debt}.
}
$$

而已知 strain criterion又告訴我們：

$$
\boxed{
\text{blow-up的 stretching geometry必須進入 }\lambda_2^+\text{ critical divergence}.
}
$$

因此下一步正式定義：

$$
\boxed{
\textbf{C3-M — Critical Vorticity–Strain Coupling Rigidity}.
}
$$

---

# 35. C3-M proof obligations

## M1 — Shell vorticity toll localization

Cheskidov–Dai給：

$$
\sum_q
\int
1_{q\le Q}
\|\omega_q\|_\infty
dt
=
\infty.
$$

研究能否分解成：

$$
\boxed{
\text{local heterochiral ancestry contribution}
+
\text{background defect contribution}.
}
$$

## M2 — Strain eigenvalue shell/interface

建立：

$$
\lambda_2^+
$$

與 dyadic strain：

$$
S_q
$$

之間不丟 eigenvalue sign information的 observation interface。

不得直接 frequency-decompose eigenvalues後當 linear field。

## M3 — Vortex-stretching source certificate

對：

$$
\omega\cdot S\omega
$$

建立：

$$
\boxed{
\text{amplitude}
+
\text{eigenvalue}
+
\text{orientation}
}
$$

三分 certificate。

## M4 — Geometry–moment coupling

尋找 inequality / dichotomy：

$$
\boxed{
\text{large critical vorticity moment}
\Rightarrow
\text{large }\lambda_2^+
\text{ contribution}
}
$$

或證 no-go。

## M5 — Alignment/depletion audit

重查 vorticity-direction coherence regularity literature。

測試：

$$
\boxed{
\text{moment escape}
+
\text{local heterochiral genealogy}
}
$$

是否迫使 vorticity directions失去 depletion geometry。

## M6 — Branch A/B geometry

分別對：

- $\Lambda\notin L^2$；
- $\Lambda\in L^2,\ M_{5/2}=\infty$；

判斷 middle-strain divergence是如何被實現。

## M7 — Endpoint Besov audit

將 2025：

$$
\lambda_2^+
\in
L_t^2\dot B^{-1}_{\infty,\infty}
$$

criterion與 first-frontier UV cap比較。

研究是否可在 ancestry core上取得 local endpoint strain smallness。

---

# 36. 正式狀態

$$
\boxed{
\begin{aligned}
\text{critical vorticity-moment divergence}
&:\ \mathrm{EXTERNAL+DERIVED},\\
\mathfrak M_2^{amp}=\infty
&:\ \mathrm{PROVED},\\
\text{subthreshold moment }\le C\beta\int\Lambda^2
&:\ \mathrm{PROVED},\\
\text{frontier }L^2\text{ vs active-moment dichotomy}
&:\ \mathrm{PROVED},\\
\Lambda\in L^2\Rightarrow M_{5/2}(\beta)=\infty
&:\ \mathrm{PROVED},\\
M_1(\beta)<\infty
&:\ \mathrm{PROVED\ from\ C3-K},\\
\text{enstrophy identity}
&:\ \mathrm{STANDARD/PROVED},\\
\text{free moment raising by enstrophy}
&:\ \mathrm{NO\mbox{-}GO},\\
\text{vortex-stretching geometry debt}
&:\ \mathrm{PROVED/STRUCTURAL},\\
\lambda_2^+\notin L_t^2L_x^3\text{ under blow-up}
&:\ \mathrm{EXTERNAL+CONTRAPOSITIVE},\\
\lambda_2^+\notin L_t^2\dot B^{-1}_{\infty,\infty}
&:\ \mathrm{EXTERNAL+CONTRAPOSITIVE},\\
\text{spectral moment}\Rightarrow\text{strain geometry}
&:\ \mathrm{OPEN},\\
\text{critical vorticity--strain rigidity}
&:\ \mathrm{OPEN}.
\end{aligned}
}
$$

---

# 37. 結論

C3-K 把 singularity縮成：

$$
\boxed{
\text{finite low-order occupancy}
+
\text{possible higher-moment escape}.
}
$$

C3-L 現在證明：

$$
\boxed{
\text{higher critical moment真的必須逃逸}.
}
$$

不是猜想。

hypothetical blow-up直接要求：

$$
\boxed{
\nu
\int
\sum_{q\le Q(t)}
\lambda_q^2a_q(t)dt
=
\infty.
}
$$

而這個 divergence只有兩種 carrier：

$$
\boxed{
\Lambda\notin L^2
}
$$

或者：

$$
\boxed{
\Lambda\in L^2
\quad\text{且}\quad
M_{5/2}(\beta)=\infty
\ \forall\beta>0.
}
$$

同時：

$$
\boxed{
M_1(\beta)<\infty.
}
$$

所以我們真正得到：

$$
\boxed{
\text{finite low moment}
+
\text{divergent critical/high moment}.
}
$$

嘗試用 enstrophy把缺的一階補回去時，

exact equation立即產生：

$$
\boxed{
\omega\cdot S\omega
}
$$

的 vortex-stretching debt。

而獨立的 strain regularity theory又要求 hypothetical singularity同時有：

$$
\boxed{
\lambda_2^+
\text{ 的 scale-critical divergence}.
}
$$

所以 N–S survivor現在不只是：

$$
\text{UV cascade}.
$$

而是：

$$
\boxed{
\textbf{critical vorticity moment escape}
+
\textbf{positive middle-strain geometric escape}.
}
$$

下一輪：

$$
\boxed{
\textbf{C3-M — Critical Vorticity–Strain Coupling Rigidity}.
}
$$

真正開始問：

$$
\boxed{
\text{這兩個已知必須同時發散的 channel，
能不能被 exact N--S geometry 強制耦合到一個不可能的狀態？}
}
$$

---

# References

1. A. Cheskidov, M. Dai, *Regularity criteria for the 3D Navier–Stokes and MHD equations*, arXiv:1507.06611.
2. A. Cheskidov, R. Shvydkoy, *A unified approach to regularity problems for the 3D Navier–Stokes and Euler equations: the use of Kolmogorov's dissipation range*, arXiv:1102.1944.
3. E. Miller, *A regularity criterion for the Navier–Stokes equation involving only the middle eigenvalue of the strain tensor*, arXiv:1710.05569; Arch. Rational Mech. Anal. 235 (2020).
4. Z. Guo, C.-J. O, *Extension criterion involving the middle eigenvalue of the strain tensor on local strong solutions to the 3D Navier–Stokes equations*, Applied Mathematics Letters 160 (2025), 109354.
5. Z. Lei, F.-H. Lin, Y. Zhou, *Structure of Helicity and Global Solutions of Incompressible Navier–Stokes Equation*, arXiv:1505.00142.
6. G. Seregin, *A certain necessary condition of potential blow up for Navier–Stokes equations*, arXiv:1104.3615.
7. H. Aluie, G. L. Eyink, *Localness of energy cascade in hydrodynamic turbulence, II. Sharp spectral filter*, arXiv:0909.2451.

# Internal dependencies

- `NS_C1_UV_Replenishment_Chain_v0.2.md`
- `NS_C2_Critical_Toll_Spike_Packing_v0.3.md`
- `NS_C3A_Conservation_Criticality_Helical_Pair_Production_v0.1.md`
- `NS_C3B_BiHelical_Equalization_UniqueSign_UV_Escape_v0.1.md`
- `NS_C3C_ClassII_Nonlocality_Tax_Radial_Congestion_v0.1.md`
- `NS_C3D_CutoffFlux_HelicalKernel_Nonlocality_v0.1.md`
- `NS_C3E_ViscousWindow_PhaseEfficiency_Zeno_v0.1.md`
- `NS_C3F_PhaseSpace_Ancestry_Cone_v0.1.md`
- `NS_C3G_FirstCrossing_CausalAncestry_DepletionNoGo_v0.1.md`
- `NS_C3H_Ancestry_Renormalization_CriticalCompactnessBarrier_v0.1.md`
- `NS_C3I_FrontierUVCap_DefectTrichotomy_v0.1.md`
- `NS_C3J_GaugeCorrected_Reentry_Hysteresis_NoGo_v0.1.md`
- `NS_C3K_AbsoluteOccupancy_OneMomentGap_v0.1.md`
- `True ETN / 無限維張力場`
- `X_Integral_Unified_Program_v0.2.md`

Next:

$$
\boxed{
\textbf{C3-M — Critical Vorticity–Strain Coupling Rigidity}
}
$$
