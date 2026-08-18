---
title: "Navier–Stokes C3-C：Class-II 非局部二次稅、徑向漂移擁塞與 III/IV 前向存活族"
subtitle: "Quadratic Nonlocality Tax, Radial-Drift Congestion, and the Forward-Surviving Heterochiral Classes"
version: "v0.1"
date: "2026-08-14"
author: "Neo.K / EveMissLab"
language: "zh-TW"
status: "Theorem-style structural reduction note"
epistemic_status: "Exact consequences of triadwise energy/helicity conservation plus Waleffe helical decomposition. No global regularity proof."
---

# Navier–Stokes C3-C
# Class-II 非局部二次稅、徑向漂移擁塞與 III/IV 前向存活族

## 0. 本輪定位

C3-B 已將 hypothetical singular pair-production core 壓成：

$$
\boxed{
\text{High--High Heterochiral UV Pair-Production Chain}.
}
$$

其中：

- homochiral triads 對 positive critical absolute helicity 的 production 為零；
- divergent pair production 的 unique-sign mode 必須逃出任意 fixed frequency cutoff；
- 每個 UV unique-sign mode 至少需要一個 comparable-high partner。

本輪優先處理 Class II：

$$
(s_k,s_p,s_q)=(+,-,-),
\qquad
0<k\le p\le q.
$$

目標是回答：

> 若 $k\ll p\sim q$，Class II 是否真的能作為高效率 UV pair-production mechanism？

答案：

$$
\boxed{
\text{Class II 可以存在，但強非局部時要同時支付}
}
$$

$$
\boxed{
\text{quadratic critical-production tax}
+
\text{radial-drift congestion}.
}
$$

---

# 1. Triad transfer algebra 回顧

對任意 helical triad：

$$
\mathbf k+\mathbf p+\mathbf q=0,
$$

排序：

$$
0<k\le p\le q,
$$

modal energies：

$$
e_k,\ e_p,\ e_q.
$$

triadwise energy 與 signed helicity conservation：

$$
\dot e_k+\dot e_p+\dot e_q=0,
$$

$$
s_k k\dot e_k+s_p p\dot e_p+s_q q\dot e_q=0.
$$

因此存在 scalar transfer parameter $\Theta_\tau$：

$$
\begin{pmatrix}
\dot e_k\\
\dot e_p\\
\dot e_q
\end{pmatrix}
=
\Theta_\tau
\begin{pmatrix}
s_pp-s_qq\\
s_qq-s_kk\\
s_kk-s_pp
\end{pmatrix}.
$$

此式只使用 exact triad invariants。

---

# 2. Class II exact equations

Class II：

$$
(+--).
$$

代入：

$$
s_k=+1,\quad s_p=-1,\quad s_q=-1.
$$

得到：

$$
\boxed{
\dot e_k
=
(q-p)\Theta_\tau,
}
$$

$$
\boxed{
\dot e_p
=
-(q+k)\Theta_\tau,
}
$$

$$
\boxed{
\dot e_q
=
(p+k)\Theta_\tau.
}
$$

unique-helicity-sign mode 是最小波數 $k$。

critical pair-production contribution：

$$
\boxed{
\mathcal R_{\mathrm{II}}
=
k(q-p)\Theta_\tau.
}
$$

---

# 3. Triangle geometry gives the first suppression

由：

$$
\mathbf k+\mathbf p+\mathbf q=0
$$

的 triangle inequality：

$$
q\le p+k.
$$

所以：

$$
\boxed{
0\le q-p\le k.
}
$$

因此：

$$
\boxed{
|\mathcal R_{\mathrm{II}}|
\le
k^2|\Theta_\tau|.
}
$$

這就是前一輪已看到的 radial-gap suppression。

但本輪要比較的不只是 absolute coefficient，而是它相對於 triad 內真正的 high-frequency exchange 有多小。

---

# 4. High critical exchange scale

定義兩個 high-mode critical exchange magnitudes：

$$
X_p
=
p|\dot e_p|,
$$

$$
X_q
=
q|\dot e_q|.
$$

Class II 中：

$$
X_p
=
p(q+k)|\Theta_\tau|,
$$

$$
X_q
=
q(p+k)|\Theta_\tau|.
$$

因：

$$
q\ge p,
$$

所以：

$$
\boxed{
X_p\ge p^2|\Theta_\tau|,
}
$$

以及：

$$
\boxed{
X_q\ge p^2|\Theta_\tau|.
}
$$

令：

$$
X_{\mathrm{hi}}
=
\min\{X_p,X_q\}.
$$

則：

$$
\boxed{
X_{\mathrm{hi}}
\ge
p^2|\Theta_\tau|.
}
$$

---

# 5. C3-C.1：Quadratic Nonlocality Tax

## 定理 5.1

Class II triad 滿足：

$$
\boxed{
|\mathcal R_{\mathrm{II}}|
\le
\left(\frac{k}{p}\right)^2
X_{\mathrm{hi}}.
}
$$

### 證明

由：

$$
|\mathcal R_{\mathrm{II}}|
\le
k^2|\Theta_\tau|
$$

與：

$$
X_{\mathrm{hi}}
\ge
p^2|\Theta_\tau|,
$$

直接得：

$$
|\mathcal R_{\mathrm{II}}|
\le
\frac{k^2}{p^2}
X_{\mathrm{hi}}.
$$

$\square$

---

# 6. Dyadic form

若：

$$
p\ge2^N k,
$$

則：

$$
\boxed{
|\mathcal R_{\mathrm{II}}|
\le
2^{-2N}
X_{\mathrm{hi}}.
}
$$

因此每增加一個 dyadic separation：

$$
N\mapsto N+1,
$$

Class II pair-production 相對 hidden high critical exchange 再下降 factor：

$$
4.
$$

本文稱：

$$
\boxed{
\textbf{Class-II Quadratic Nonlocality Tax}.
}
$$

---

# 7. Hidden-exchange debt

重寫定理 5.1：

若：

$$
\mathcal R_{\mathrm{II}}\ne0,
$$

則：

$$
\boxed{
X_{\mathrm{hi}}
\ge
\left(\frac{p}{k}\right)^2
|\mathcal R_{\mathrm{II}}|.
}
$$

所以若：

$$
\chi_\tau
=
\frac{k}{p}
\ll1,
$$

要產生固定大小的 critical pair production，就需要：

$$
\boxed{
\chi_\tau^{-2}
}
$$

倍量級的 hidden high-frequency critical exchange。

這不是新的有限 budget theorem。

它是一個 exact **congestion certificate**：

> pair production 越 nonlocal，背後必須有越大的 high-mode exchange circulation。

---

# 8. Energy-transfer cancellation ratio

Class II 有：

$$
\dot e_p+\dot e_q
=
-\dot e_k.
$$

而：

$$
|\dot e_k|
=
(q-p)|\Theta_\tau|
\le
k|\Theta_\tau|.
$$

同時：

$$
|\dot e_p|
=
(q+k)|\Theta_\tau|
\ge
p|\Theta_\tau|,
$$

$$
|\dot e_q|
=
(p+k)|\Theta_\tau|
\ge
p|\Theta_\tau|.
$$

所以：

## 定理 8.1（High-exchange cancellation）

$$
\boxed{
\frac{
|\dot e_p+\dot e_q|
}{
\min\{|\dot e_p|,|\dot e_q|\}
}
\le
\frac{k}{p}.
}
$$

當：

$$
k/p\to0,
$$

兩個 high-mode energy transfers 變成：

$$
\boxed{
\text{large opposite transfers + small residual}.
}
$$

這是 Waleffe 對 strongly nonlocal reverse-type interactions 所描述的 pair cancellation 的 exact algebraic version。

---

# 9. Positive pair production 的 donor/receiver orientation

假設 nondegenerate：

$$
q>p.
$$

Class II：

$$
\mathcal R_{\mathrm{II}}
=
k(q-p)\Theta_\tau.
$$

所以：

$$
\mathcal R_{\mathrm{II}}>0
\iff
\Theta_\tau>0.
$$

此時：

$$
\dot e_k>0,
$$

$$
\dot e_p<0,
$$

$$
\dot e_q>0.
$$

因此：

$$
\boxed{
\text{Class II positive pair production：}
p\text{ 是 donor，}
k,q\text{ 是 receivers}.
}
$$

也就是：

$$
\boxed{
p
\longrightarrow
\{k,q\}.
}
$$

---

# 10. Class II 不是純 forward transfer

對 strongly nonlocal：

$$
k\ll p\sim q,
$$

正 pair production 同時：

1. 把一小部分 transfer送到低模 $k$；
2. 把主要高端 transfer從 $p$ 搬到附近的 $q$。

它不是：

$$
k\to p\to q
$$

型由最低 mode 直接 feeding higher modes 的純 forward pattern。

這與 Waleffe 對 small-scale same-helicity nonlocal R-class 的結構描述一致：

- high-end local exchange 很大；
- 對 low mode feedback較小；
- large high transfers 成對接近 cancellation；
- net effect接近 wave-number-space advection。

---

# 11. Radial step bound

Class II high receiver 是：

$$
q.
$$

high donor 是：

$$
p.
$$

high-end radial advancement：

$$
\Delta_{\mathrm{rad}}
=
q-p.
$$

triangle inequality 已給：

$$
q-p\le k.
$$

除以 $p$：

$$
\boxed{
\frac{q-p}{p}
\le
\frac{k}{p}.
}
$$

定義：

$$
\delta_\tau
=
\frac{q-p}{p},
$$

$$
\chi_\tau
=
\frac{k}{p}.
$$

則：

$$
\boxed{
0\le\delta_\tau\le\chi_\tau\le1.
}
$$

所以 nonlocality：

$$
\chi_\tau\ll1
$$

自動意味：

$$
\delta_\tau\ll1.
$$

---

# 12. Class-II radial genealogy

考慮一條理想化 source-preserving Class-II high-end genealogy：

$$
p_0
\to
q_0=p_1
\to
q_1=p_2
\to
\cdots.
$$

令第 $n$ 步：

$$
q_n=p_n(1+\delta_n),
$$

其中：

$$
0\le\delta_n\le\chi_n.
$$

則：

$$
p_{n+1}
=
p_n(1+\delta_n).
$$

所以：

$$
\boxed{
p_n
=
p_0
\prod_{j=0}^{n-1}
(1+\delta_j).
}
$$

---

# 13. C3-C.2：Radial-Drift Congestion Lemma

## 定理 13.1

若一條 Class-II high-end genealogy 滿足：

$$
p_n\to\infty,
$$

則必有：

$$
\boxed{
\sum_{n=0}^{\infty}
\delta_n
=
\infty.
}
$$

因此也必有：

$$
\boxed{
\sum_{n=0}^{\infty}
\chi_n
=
\infty.
}
$$

### 證明

若：

$$
\sum_n\delta_n<\infty,
$$

則：

$$
\sum_n\log(1+\delta_n)
\le
\sum_n\delta_n
<
\infty.
$$

因此 product：

$$
\prod_n(1+\delta_n)
$$

收斂到 finite positive number。

所以：

$$
p_n
=
p_0
\prod_{j<n}(1+\delta_j)
$$

保持有界，與：

$$
p_n\to\infty
$$

矛盾。

故：

$$
\sum_n\delta_n=\infty.
$$

由：

$$
\delta_n\le\chi_n,
$$

得：

$$
\sum_n\chi_n=\infty.
$$

$\square$

---

# 14. Uniform nonlocality congestion

若整條 chain 都滿足：

$$
\chi_n\le\varepsilon<1,
$$

則每一步：

$$
p_{n+1}\le(1+\varepsilon)p_n.
$$

若要從：

$$
p_0
$$

跨到：

$$
2p_0,
$$

至少需要：

$$
m
\ge
\frac{\log2}{\log(1+\varepsilon)}.
$$

當：

$$
\varepsilon\ll1,
$$

有：

$$
\log(1+\varepsilon)\sim\varepsilon.
$$

所以：

$$
\boxed{
m
\gtrsim
\frac{1}{\varepsilon}.
}
$$

這是 **Class-II step congestion**。

---

# 15. Quadratic tax + linear congestion

strongly nonlocal Class II 同時具有：

### 每步 pair-production efficiency

$$
\boxed{
\frac{|\mathcal R_{\mathrm{II}}|}{X_{\mathrm{hi}}}
\le
\chi^2.
}
$$

### 每個 dyadic scale traversal 所需步數

$$
\boxed{
m
\gtrsim
\chi^{-1}
}
$$

若 $\chi$ approximately uniform。

因此越 nonlocal：

- 每一步越沒有 production efficiency；
- 要跨一個 dyadic scale又需要越多步。

本文稱：

$$
\boxed{
\textbf{Quadratic Tax + Linear Congestion}.
}
$$

這仍不是 contradiction，因我們尚未有：

$$
\sum X_{\mathrm{hi}}<\infty.
$$

但它把 strongly nonlocal Class II 變成一條非常昂貴的 genealogy。

---

# 16. Class III exact orientation

Class III：

$$
(+-+).
$$

transfer：

$$
\dot e_k
=
-(p+q)\Theta_\tau,
$$

$$
\dot e_p
=
(q-k)\Theta_\tau,
$$

$$
\dot e_q
=
(p+k)\Theta_\tau.
$$

unique sign 在 medium：

$$
p.
$$

pair production：

$$
\mathcal R_{\mathrm{III}}
=
p(q-k)\Theta_\tau.
$$

若：

$$
\mathcal R_{\mathrm{III}}>0,
$$

則：

$$
\Theta_\tau>0.
$$

所以：

$$
\boxed{
\dot e_k<0,
\qquad
\dot e_p>0,
\qquad
\dot e_q>0.
}
$$

即：

$$
\boxed{
k
\longrightarrow
\{p,q\}.
}
$$

最低 mode 是 donor。

這是直接 forward-compatible orientation。

---

# 17. Class III strongly nonlocal regime沒有 $k/p$ suppression

若：

$$
k\ll p\sim q,
$$

因：

$$
q\le p+k,
$$

有：

$$
q\sim p.
$$

並且：

$$
q-k
\sim p.
$$

所以：

$$
\boxed{
|\mathcal R_{\mathrm{III}}|
\sim
p^2|\Theta_\tau|
}
$$

在 radial algebra level沒有：

$$
(k/p)^2
$$

tax。

因此 Class III 是真正的 nonlocal survivor。

---

# 18. Class IV exact orientation

Class IV：

$$
(++-).
$$

transfer：

$$
\dot e_k
=
(p+q)\Theta_\tau,
$$

$$
\dot e_p
=
-(q+k)\Theta_\tau,
$$

$$
\dot e_q
=
(k-p)\Theta_\tau.
$$

unique sign 在 largest：

$$
q.
$$

pair production：

$$
\mathcal R_{\mathrm{IV}}
=
q(k-p)\Theta_\tau.
$$

因：

$$
k-p\le0,
$$

若：

$$
\mathcal R_{\mathrm{IV}}>0,
$$

則：

$$
\Theta_\tau<0.
$$

因此：

$$
\boxed{
\dot e_k<0,
\qquad
\dot e_p>0,
\qquad
\dot e_q>0.
}
$$

即同樣：

$$
\boxed{
k
\longrightarrow
\{p,q\}.
}
$$

最低 mode 是 donor。

---

# 19. Class IV 是唯一 top-unique class

三個 heterochiral classes 的 unique-sign mode位置：

| Class | signs | unique-sign wavenumber |
|---|---|---|
| II | $(+--)$ | $k$ smallest |
| III | $(+-+)$ | $p$ middle |
| IV | $(++-)$ | $q$ largest |

所以：

$$
\boxed{
\text{Class IV 是唯一把 unique-helicity mode 放在 triad 最大波數的 class}.
}
$$

因此若我們追蹤：

$$
\text{unique-sign critical pair-production frontier},
$$

Class IV 是唯一**直接 frontier-capable**的 pair-production class。

此句的精確含義是：

> 在單一 triad 內，只有 Class IV 的 positive pair-production target 是該 triad 的最大 wavenumber。

它不表示 global blow-up 必須只由 Class IV構成。

---

# 20. Class III 的 ancestry demand

Class III unique mode位於：

$$
p,
$$

但同一 positive pair-production event 還有：

$$
q\ge p
$$

的 high receiver。

因此 Class III 可以 forward transfer，但 unique-sign target不是 triad frontier。

若要把 unique-sign pair-production frontier持續推高，Class III event 需要：

- 更高 $q$ mode同時形成；
- 或下一代以 $q$ 作為 ancestry source；
- 或其他 class 負責 frontier extension。

所以它仍帶有 ancestry obligation。

---

# 21. C3-C.3：Forward-Compatible Survivor Classification

定義一個 positive pair-production event 為 **forward-compatible**，若最低 wave number $k$ 是 energy donor。

則由 exact transfer signs：

$$
\boxed{
\text{Class III and Class IV are forward-compatible}.
}
$$

而 Class II positive pair production中 donor是：

$$
p,
$$

不是 $k$。

因此：

$$
\boxed{
\text{Class II is not forward-compatible in this precise sense}.
}
$$

這是 algebraic classification，不依賴 Waleffe instability assumption。

---

# 22. 與 Waleffe R/F classification 的關係

Waleffe 將 elementary helical interactions依 small-scale modes 的 helicity signs分為 reverse-type與 forward-type families。

對本文排序：

- Class II 的兩個較高 modes $p,q$ 為同 sign；
- Classes III/IV 的 $p,q$ 為 opposite signs。

這與 Waleffe 對：

- nonlocal same-small-scale-sign interactions具有大型局部交換與強 cancellation；
- opposite-small-scale-sign interactions支援 forward transfer；

的分析結構一致。

本文不用其 statistical instability assumption來證 transfer sign。

本文所有 sign orientation均由條件：

$$
\mathcal R_\tau>0
$$

與 exact conservation algebra直接推出。

---

# 23. C3-C 的 X-Integration guards

對 Class-II chain，新增：

### G-$\chi$ — nonlocality ratio

$$
\chi_n=\frac{k_n}{p_n}.
$$

### G-$\delta$ — radial drift

$$
\delta_n=\frac{q_n-p_n}{p_n}.
$$

且：

$$
0\le\delta_n\le\chi_n.
$$

### G-tax — production efficiency

$$
\frac{|\mathcal R_n|}{X_{\mathrm{hi},n}}
\le
\chi_n^2.
$$

### G-drift — UV escape

若：

$$
p_n\to\infty,
$$

必須：

$$
\sum_n\delta_n=\infty.
$$

### G-congestion

若：

$$
\chi_n\le\varepsilon,
$$

每跨一個 dyadic scale至少：

$$
O(\varepsilon^{-1})
$$

steps。

所以一條 Class-II singular certificate不能只寫：

$$
\text{all interactions legal}.
$$

它還必須攜帶：

$$
\boxed{
\text{hidden exchange debt}
+
\text{radial drift debt}
+
\text{step congestion}.
}
$$

---

# 24. 一個重要 no-go

目前不能從：

$$
X_{\mathrm{hi}}
\ge
\chi^{-2}|\mathcal R|
$$

直接推出 contradiction。

因為沒有已證 global finite bound：

$$
\boxed{
\int
\sum_{\tau}
X_{\mathrm{hi},\tau}\,dt
<
\infty.
}
$$

這個 quantity 是 absolute high-frequency exchange variation，energy conservation只控制 signed net transfer，不控制 absolute turnover。

因此：

$$
\boxed{
\text{nonlocality tax}
\neq
\text{finite-budget proof}.
}
$$

這必須明確保留。

---

# 25. Conditional suppression theorem

## 定理 25.1

令：

$$
\mathfrak C_{II}^{(N)}
$$

表示所有 Class-II triads satisfying：

$$
p\ge2^N k.
$$

定義其 cumulative pair production：

$$
P_{II}^{(N)}
=
\int
\sum_{\tau\in\mathfrak C_{II}^{(N)}}
|\mathcal R_\tau(t)|
\,dt,
$$

以及 hidden high-exchange variation：

$$
V_{II}^{(N)}
=
\int
\sum_{\tau\in\mathfrak C_{II}^{(N)}}
X_{\mathrm{hi},\tau}(t)
\,dt.
$$

則：

$$
\boxed{
P_{II}^{(N)}
\le
2^{-2N}
V_{II}^{(N)}.
}
$$

### 證明

逐 triad使用：

$$
|\mathcal R_\tau|
\le
2^{-2N}X_{\mathrm{hi},\tau}
$$

後積分求和。$\square$

---

# 26. Conditional consequence

若未來能證某種：

$$
V_{II}^{(N)}
=
o(2^{2N})
$$

as：

$$
N\to\infty,
$$

則：

$$
\boxed{
P_{II}^{(N)}\to0.
}
$$

也就是 strongly nonlocal Class II 對 cumulative pair production asymptotically negligible。

因此新的具體 proof target是：

$$
\boxed{
\text{控制 }V_{II}^{(N)}\text{ 的 growth rate}.
}
$$

這比模糊地說「nonlocal Class II應該不重要」精確。

---

# 27. Survivor map

目前 critical pair-production classes：

## Homochiral

$$
\boxed{
\mathcal R=0.
}
$$

淘汰為 production source。

## Class II local / moderately nonlocal

仍存活。

## Class II strongly nonlocal

具有：

$$
\boxed{
\chi^2\text{ production tax}
+
\chi^{-1}\text{ traversal congestion}
}
$$

但尚未完全淘汰。

## Class III

forward-compatible，strongly nonlocal不受 radial-gap tax。

$$
\boxed{
\text{SURVIVOR}.
}
$$

## Class IV

forward-compatible，unique sign 位於 highest mode。

$$
\boxed{
\text{PRIMARY FRONTIER SURVIVOR}.
}
$$

---

# 28. 新主線：C3-D

經 C3-C 後，最值得直接攻的是：

$$
\boxed{
\textbf{C3-D — Forward Heterochiral Frontier Rigidity}.
}
$$

核心 survivor：

$$
\boxed{
\text{Classes III/IV}
+
\text{non-negligibly local Class II}.
}
$$

其中 Class IV 優先度最高，因它直接對最高 unique-helicity mode 作 positive pair production。

---

# 29. C3-D proof obligations

## D1 — Class-IV dyadic frontier production

定義：

$$
\mathcal R_{IV,q}
$$

為 unique-sign highest mode位於 shell $q$ 的 Class-IV positive production。

由 C3-B unique-sign UV escape，研究能否證：

$$
\boxed{
\sum_{q>Q}
\int
[\mathcal R_{IV,q}]_+dt
}
$$

在 blow-up scenario中必須有 nontrivial lower envelope。

## D2 — Separate III from IV ancestry

Class III unique mode不是 top mode。

建立 ancestry graph：

$$
p_{\rm unique}
\leftarrow
(k,q)
$$

並追蹤 $q$ 的來源。

判定 infinite III-only genealogy 是否必然：

- 轉成 IV step；
- 或需要 infinite pre-existing higher-frequency ancestry。

## D3 — Absolute exchange variation

嘗試控制：

$$
V_{II}^{(N)}.
$$

候選工具：

- dyadic commutators；
- local energy flux；
- scale-locality estimates；
- dissipation wavenumber；
- frequency-envelope variation；
- wave-space telescoping。

## D4 — Wave-space advection formulation

對 nonlocal Class II：

$$
q-p\le k\ll p.
$$

將高端 $p\to q$ 看成 small radial step。

研究能否把 aggregate Class-II high transfer重寫成 discrete/continuous divergence：

$$
\partial_\kappa
\mathcal J(\kappa)
$$

使大量 opposite high exchanges telescopically cancel，只留下 shell-boundary flux。

若成功，可能把：

$$
V_{II}
$$

從 absolute exchange降成 boundary variation。

這與 Waleffe 所描述的 wave-number-space advection結構最直接。

---

# 30. 正式狀態

$$
\boxed{
\begin{aligned}
\text{Class-II exact transfer equations}
&:\ \mathrm{PROVED},\\
\text{quadratic nonlocality tax}
&:\ \mathrm{PROVED},\\
\text{high-exchange cancellation ratio}
&:\ \mathrm{PROVED},\\
\text{radial step bound}
&:\ \mathrm{PROVED},\\
\text{radial-drift congestion lemma}
&:\ \mathrm{PROVED},\\
\text{Class III forward-compatible}
&:\ \mathrm{PROVED},\\
\text{Class IV forward-compatible}
&:\ \mathrm{PROVED},\\
\text{Class IV top-unique}
&:\ \mathrm{PROVED},\\
\text{strongly nonlocal Class II globally negligible}
&:\ \mathrm{OPEN},\\
V_{II}^{(N)}=o(2^{2N})
&:\ \mathrm{OPEN},\\
\text{Forward Heterochiral Frontier Rigidity}
&:\ \mathrm{OPEN}.
\end{aligned}
}
$$

---

# 31. 結論

本輪沒有證明 N–S regularity。

但把 Class-II strong-nonlocal route 壓出了兩個 exact costs：

$$
\boxed{
\frac{|\mathcal R_{II}|}{X_{\rm hi}}
\le
\left(\frac{k}{p}\right)^2
}
$$

以及：

$$
\boxed{
p_n\to\infty
\Rightarrow
\sum_n
\frac{q_n-p_n}{p_n}
=
\infty.
}
$$

所以 strongly nonlocal Class II 若要一路走向 UV，必須：

1. 在每一步接受 quadratic production inefficiency；
2. 用大量 small radial steps補回 scale growth；
3. 維持巨大、近乎互相抵消的 high-mode exchange circulation。

與此相對：

$$
\boxed{
\text{Classes III/IV positive pair production直接由最低 mode feeding higher modes}.
}
$$

而：

$$
\boxed{
\text{Class IV 是唯一 unique-helicity target 位於 triad最高頻的 class}.
}
$$

因此下一主戰場正式縮成：

$$
\boxed{
\textbf{C3-D — Forward Heterochiral Frontier Rigidity}
}
$$

優先：

$$
\boxed{
\text{Class IV frontier production}
+
\text{Class III ancestry}
+
\text{Class-II wave-space telescoping}.
}
$$

---

# References

1. F. Waleffe, *The nature of triad interactions in homogeneous turbulence*, Physics of Fluids A 4 (1992), 350–363.
2. F. Waleffe, *Inertial transfers in the helical decomposition*, Physics of Fluids A 5 (1993).
3. L. Biferale, E. S. Titi, *On the Global Regularity of a Helical-decimated Version of the 3D Navier–Stokes Equations*, arXiv:1303.1215.
4. G. Sahoo, L. Biferale, *Disentangling the triadic interactions in Navier-Stokes equations*, arXiv:1510.09006.
5. G. Sahoo, L. Biferale, *Energy Cascade and Intermittency in Helically Decomposed Navier-Stokes Equations*, arXiv:1709.03713.
6. Z. Lei, F.-H. Lin, Y. Zhou, *Structure of Helicity and Global Solutions of Incompressible Navier–Stokes Equation*, arXiv:1505.00142.

# Internal dependencies

- `NS_C1_UV_Replenishment_Chain_v0.2.md`
- `NS_C2_Critical_Toll_Spike_Packing_v0.3.md`
- `NS_C3A_Conservation_Criticality_Helical_Pair_Production_v0.1.md`
- `NS_C3B_BiHelical_Equalization_UniqueSign_UV_Escape_v0.1.md`
- `True ETN / 無限維張力場`
- `X_Integral_Unified_Program_v0.2.md`

Next:

$$
\boxed{
\textbf{C3-D — Forward Heterochiral Frontier Rigidity}
}
$$
