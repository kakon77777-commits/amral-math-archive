---
title: "Navier–Stokes C3-D：Cutoff-Flux 符號定理、Helical Kernel 非局部指數與 Class-II 對數反轉"
subtitle: "Cutoff-Flux Signatures, Helical-Kernel Nonlocality Exponents, and Logarithmic Flux Reversal of Strongly Nonlocal Class-II Triads"
version: "v0.1"
date: "2026-08-14"
author: "Neo.K / EveMissLab"
language: "zh-TW"
status: "Theorem-style structural reduction note"
epistemic_status: "Exact single-triad algebra + standard Waleffe helical coefficient + conditional external scale-locality comparison. Does NOT prove Navier–Stokes global regularity."
---

# Navier–Stokes C3-D
# Cutoff-Flux 符號定理、Helical Kernel 非局部指數與 Class-II 對數反轉

## 0. 本輪定位

C3-C 已把 hypothetical singular production core 壓到：

$$
\boxed{
\text{high--high heterochiral UV pair-production}.
}
$$

並證明對 Class II：

$$
(+--),\qquad 0<k\le p\le q,
$$

strong nonlocality

$$
\chi=\frac{k}{p}\ll1
$$

會造成：

$$
\boxed{
\text{quadratic pair-production tax}
+
\text{radial-drift congestion}.
}
$$

本輪進一步問：

> 這些巨大、近乎互相抵消的 high--high exchanges，對真正穿過 spectral cutoff 的能量 flux 到底留下什麼？

答案分成三層：

1. Class II 的 large high--high turnover 多數只在同一 cutoff side 內部循環；
2. positive Class-II pair production 對 cutoff flux 具有 **reverse-then-forward sign change**；
3. positive Classes III/IV 則對 triad 全尺度區間具有 **uniform forward sign**。

此外，Waleffe helical coefficient 本身給出新的 strong-nonlocal kernel tax：

$$
\boxed{
\mathrm{Class\ II}:O(\chi^2),
\qquad
\mathrm{Class\ III/IV}:O(\chi)
}
$$

相對於 raw cubic amplitude scale。

---

# 1. 設定與符號

考慮一個 helical Fourier triad：

$$
\mathbf k+\mathbf p+\mathbf q=0,
$$

其模長排序：

$$
0<k\le p\le q.
$$

modal energies：

$$
e_k,\qquad e_p,\qquad e_q.
$$

triadwise exact conservation：

$$
\dot e_k+\dot e_p+\dot e_q=0,
$$

$$
s_k k\dot e_k+s_p p\dot e_p+s_q q\dot e_q=0.
$$

四類獨立 sign configurations：

$$
\mathrm I:(+++),
$$

$$
\mathrm{II}:(+--),
$$

$$
\mathrm{III}:(+-+),
$$

$$
\mathrm{IV}:(++-).
$$

global sign reversal視為同一 class。

---

# 2. Transfer vector 回顧

存在 scalar transfer parameter $\Theta_\tau$：

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

因此：

## Class II

$$
\dot e_k=(q-p)\Theta_\tau,
$$

$$
\dot e_p=-(q+k)\Theta_\tau,
$$

$$
\dot e_q=(p+k)\Theta_\tau.
$$

critical pair production：

$$
\mathcal R_{II}
=
k(q-p)\Theta_\tau.
$$

若：

$$
\mathcal R_{II}>0
$$

且 $q>p$，則：

$$
\Theta_\tau>0.
$$

---

## Class III

$$
\dot e_k=-(p+q)\Theta_\tau,
$$

$$
\dot e_p=(q-k)\Theta_\tau,
$$

$$
\dot e_q=(p+k)\Theta_\tau.
$$

$$
\mathcal R_{III}
=
p(q-k)\Theta_\tau.
$$

positive pair production implies：

$$
\Theta_\tau>0.
$$

---

## Class IV

$$
\dot e_k=(p+q)\Theta_\tau,
$$

$$
\dot e_p=-(q+k)\Theta_\tau,
$$

$$
\dot e_q=(k-p)\Theta_\tau.
$$

$$
\mathcal R_{IV}
=
q(k-p)\Theta_\tau.
$$

positive pair production implies：

$$
\Theta_\tau<0.
$$

令：

$$
\Psi_\tau=-\Theta_\tau>0.
$$

則：

$$
\dot e_k=-(p+q)\Psi_\tau,
$$

$$
\dot e_p=(q+k)\Psi_\tau,
$$

$$
\dot e_q=(p-k)\Psi_\tau.
$$

---

# 3. Sharp cutoff triad flux

對 cutoff：

$$
K>0,
$$

定義單 triad 的 high-side energy：

$$
E_{>K}^{(\tau)}
=
\sum_{r\in\{k,p,q\},\,r>K}
e_r.
$$

定義 triad cutoff flux：

$$
\boxed{
\Phi_\tau(K)
=
\left(
\frac{d}{dt}
E_{>K}^{(\tau)}
\right)_{\mathrm{nonlinear}}.
}
$$

本文採 sign convention：

$$
\Phi_\tau(K)>0
$$

表示 energy 經該 triad **向 cutoff 上方的更高 wavenumber side 流動**。

---

# 4. C3-D.1：Class-II Cutoff-Flux Signature

## 定理 4.1

考慮 positive-pair-producing Class-II triad：

$$
(+--),
$$

$$
q>p,
$$

$$
\Theta_\tau>0.
$$

則：

$$
\boxed{
\Phi_{II}(K)
=
\begin{cases}
0,
&
0<K<k,
\\[1mm]
-(q-p)\Theta_\tau,
&
k<K<p,
\\[1mm]
(p+k)\Theta_\tau,
&
p<K<q,
\\[1mm]
0,
&
K>q.
\end{cases}
}
$$

### 證明

- $K<k$：三個 modes 均在 high side；由 energy conservation總導數為零。
- $k<K<p$：high side包含 $p,q$：

$$
\Phi
=
\dot e_p+\dot e_q
=
-\dot e_k
=
-(q-p)\Theta_\tau.
$$

- $p<K<q$：high side只包含 $q$：

$$
\Phi
=
\dot e_q
=
(p+k)\Theta_\tau.
$$

- $K>q$：high side無此 triad modes。

$\square$

---

# 5. Class-II 的 sign reversal

因此：

$$
\boxed{
k<K<p
\quad\Rightarrow\quad
\Phi_{II}(K)<0,
}
$$

但：

$$
\boxed{
p<K<q
\quad\Rightarrow\quad
\Phi_{II}(K)>0.
}
$$

所以 positive critical pair production 的 Class II 並不是「整體 forward」。

它具有：

$$
\boxed{
\text{broad reverse interval}
+
\text{narrow forward window}.
}
$$

---

# 6. Forward window 的幾何厚度

Class II triangle geometry：

$$
q-p\le k.
$$

因此 large positive high--high transfer only crosses cutoffs：

$$
K\in(p,q),
$$

其 linear width：

$$
\boxed{
q-p\le k.
}
$$

若：

$$
k\ll p\sim q,
$$

則 large forward-flux window 只佔 high scale 的相對厚度：

$$
\boxed{
\frac{q-p}{p}
\le
\frac{k}{p}
=
\chi.
}
$$

---

# 7. Boundary-layer localization

固定 high cutoff：

$$
K.
$$

若 Class-II positive triad 的 large $p\to q$ transfer對 $\Phi_{II}(K)$ 為正，必有：

$$
p<K<q.
$$

又：

$$
q-p\le k.
$$

因此：

$$
\boxed{
K-k<p<K<q<K+k.
}
$$

所以：

$$
\boxed{
\text{strongly nonlocal Class-II large forward transfer
只能由 high pair 落在 cutoff 的 }O(k)\text{ boundary layer 內產生}.
}
$$

這是 pure Fourier geometry，不使用 turbulence scaling assumption。

---

# 8. C3-D.2：Classes III/IV Uniform Forward Signature

## 定理 8.1

若 Class III 或 Class IV triad 正在產生 positive critical pair production，則：

$$
\boxed{
\Phi_\tau(K)>0
\qquad
\forall K\in(k,q).
}
$$

### Class III

positive pair production意味：

$$
\Theta_\tau>0.
$$

當：

$$
k<K<p,
$$

$$
\Phi_{III}
=
\dot e_p+\dot e_q
=
-\dot e_k
=
(p+q)\Theta_\tau>0.
$$

當：

$$
p<K<q,
$$

$$
\Phi_{III}
=
\dot e_q
=
(p+k)\Theta_\tau>0.
$$

---

### Class IV

令：

$$
\Psi_\tau=-\Theta_\tau>0.
$$

當：

$$
k<K<p,
$$

$$
\Phi_{IV}
=
\dot e_p+\dot e_q
=
-\dot e_k
=
(p+q)\Psi_\tau>0.
$$

當：

$$
p<K<q,
$$

$$
\Phi_{IV}
=
\dot e_q
=
(p-k)\Psi_\tau\ge0.
$$

nondegenerate $p>k$ 時 strictly positive。

$\square$

---

# 9. Forward-sign classification

因此 positive pair-production triads具有：

$$
\boxed{
\begin{array}{c|c}
\text{Class}&\text{cutoff-flux signature}\\
\hline
II&\text{reverse on }(k,p),\ \text{forward on }(p,q)\\
III&\text{forward on all }(k,q)\\
IV&\text{forward on all }(k,q)
\end{array}
}
$$

這比上一輪「最低 mode是不是 donor」更強。

Classes III/IV 不只是 donor orientation forward-compatible，而是：

$$
\boxed{
\textbf{uniformly forward across every intermediate spectral cutoff}.
}
$$

---

# 10. Log-cutoff integrated flux

定義：

$$
\boxed{
\mathfrak F_\tau
=
\int_0^\infty
\Phi_\tau(K)\,
\frac{dK}{K}.
}
$$

$dK/K$ 是 logarithmic scale measure。

對 Class II：

$$
\boxed{
\mathfrak F_{II}
=
-(q-p)\Theta_\tau
\log\frac{p}{k}
+
(p+k)\Theta_\tau
\log\frac{q}{p}.
}
$$

---

# 11. Nonlocal variables

定義：

$$
\chi
=
\frac{k}{p},
$$

$$
\delta
=
\frac{q-p}{p}.
$$

triangle geometry給：

$$
\boxed{
0<\delta\le\chi\le1
}
$$

對 nonzero positive Class-II pair production。

上式改寫：

$$
\frac{
\mathfrak F_{II}
}{
p\delta\Theta_\tau
}
=
-
\log\frac1\chi
+
\frac{1+\chi}{\delta}
\log(1+\delta).
$$

---

# 12. C3-D.3：Log-Cutoff Reversal Threshold

對：

$$
\delta>0,
$$

有 elementary bound：

$$
\frac{\log(1+\delta)}{\delta}
\le1.
$$

故：

$$
\frac{
\mathfrak F_{II}
}{
p\delta\Theta_\tau
}
\le
-
\log\frac1\chi
+
1+\chi.
$$

令：

$$
\chi_\ast
$$

為方程：

$$
\log\frac1{\chi_\ast}
=
1+\chi_\ast
$$

的唯一正根。

等價：

$$
\boxed{
\chi_\ast
=
W(e^{-1})
\approx
0.278464542761.
}
$$

其中 $W$ 為 Lambert $W$ function。

## 定理 12.1

若 positive Class-II triad滿足：

$$
\boxed{
\frac{k}{p}
<
\chi_\ast
\approx0.27846,
}
$$

則：

$$
\boxed{
\mathfrak F_{II}<0.
}
$$

$\square$

---

# 13. 意義：strongly nonlocal Class II 的 scale-averaged方向是 reverse

因此一個足夠 nonlocal 的 positive-pair-producing Class II event 即使具有：

$$
p\to q
$$

的局部 high-end forward transfer，

當我們把所有 intermediate cutoffs 以 logarithmic scale measure 一起計帳時：

$$
\boxed{
\text{reverse contribution dominates}.
}
$$

這是 Waleffe「nonlocal R-class 大 local transfer 近似 cancellation、net effect 具有 reverse character」的一個 exact single-triad cutoff formulation。

---

# 14. Classes III/IV 的 log-cutoff flux

由定理 8.1：

$$
\Phi_{III}(K)>0,
$$

$$
\Phi_{IV}(K)>0
$$

對所有：

$$
K\in(k,q).
$$

故：

$$
\boxed{
\mathfrak F_{III}>0,
\qquad
\mathfrak F_{IV}>0.
}
$$

所以 positive pair-production 下：

$$
\boxed{
\text{III/IV 是 log-scale uniformly forward},
}
$$

而 sufficiently nonlocal II：

$$
\boxed{
\text{log-scale net reverse}.
}
$$

---

# 15. Compensation obligation

若某 hypothetical mechanism 同時要求：

1. 大量 positive critical pair production；
2. 大尺度區間內 net forward energy delivery；

則 strongly nonlocal positive Class-II triads不能單獨同時提供兩者。

它們的：

$$
\mathfrak F_{II}<0.
$$

因此必須由：

- Classes III/IV；
- 或較 local 的 Class II；
- 或其他 forward channels

提供 compensation。

本文稱：

$$
\boxed{
\textbf{Forward-Flux Compensation Obligation}.
}
$$

**重要：**

本文尚未證 finite-time singularity 必然需要 positive：

$$
\mathfrak F
$$

的 log-integrated energy flux。

因此 Compensation Obligation 是針對「需要 forward energy ancestry」的 conditional structural rule，不是 global regularity theorem。

---

# 16. Waleffe helical coupling coefficient

在標準 Waleffe helical normalization 下，單 triad geometric coefficient 的 magnitude 可寫成：

$$
\boxed{
|g_{s_ks_ps_q}(k,p,q)|
=
\frac{Q}{4kpq}
\left|
s_kk+s_pp+s_qq
\right|,
}
$$

忽略純 phase / basis normalization conventions。

其中：

$$
Q^2
=
2(k^2p^2+p^2q^2+q^2k^2)
-k^4-p^4-q^4.
$$

$Q$ 等於 wave-number triangle area 的固定倍數。

因此：

$$
Q
\le
2kp.
$$

---

# 17. C3-D.4：Helical Geometry Nonlocality Bounds

## Class II

$$
(+--):
$$

$$
|k-p-q|
=
p+q-k
\le
2q.
$$

所以：

$$
\boxed{
|g_{II}|
\le
C.
}
$$

在上述 normalization 可取 universal $C$。

---

## Class III

$$
(+-+):
$$

$$
|k-p+q|
=
k+(q-p)
\le
2k.
$$

因此：

$$
\boxed{
|g_{III}|
\le
C\frac{k}{q}
\le
C\frac{k}{p}.
}
$$

---

## Class IV

$$
(++-):
$$

$$
|k+p-q|
=
k-(q-p)
\le
k.
$$

因此：

$$
\boxed{
|g_{IV}|
\le
C\frac{k}{q}
\le
C\frac{k}{p}.
}
$$

---

# 18. Geometric interpretation

所以 strong nonlocality：

$$
\chi=\frac{k}{p}\to0
$$

時：

$$
\boxed{
g_{II}=O(1),
}
$$

但：

$$
\boxed{
g_{III},g_{IV}=O(\chi).
}
$$

這正是為什麼 individual nonlocal R/Class-II triads 可以具有非常大的 raw high-mode turnover：

它們的 geometric coupling沒有自動消失。

相反地，forward Classes III/IV 的 helical geometry 本身帶一個 linear nonlocality suppression。

---

# 19. Pair-production kernel bound

令：

$$
a_k
=
|u^{s_k}(\mathbf k)|,
\qquad
a_p
=
|u^{s_p}(\mathbf p)|,
\qquad
a_q
=
|u^{s_q}(\mathbf q)|.
$$

由 helical amplitude equation，transfer scalar滿足：

$$
|\Theta_\tau|
\le
C
|g_\tau|
a_ka_pa_q.
$$

因此：

## Class II

$$
|\mathcal R_{II}|
=
k(q-p)|\Theta_\tau|.
$$

由：

$$
q-p\le k,
$$

以及：

$$
|g_{II}|\le C,
$$

得：

$$
\boxed{
|\mathcal R_{II}|
\le
C
k^2
a_ka_pa_q.
}
$$

---

## Class III

$$
|\mathcal R_{III}|
=
p(q-k)|\Theta_\tau|.
$$

利用：

$$
q-k\le q,
$$

以及：

$$
|g_{III}|
\le
C\frac{k}{q},
$$

得：

$$
\boxed{
|\mathcal R_{III}|
\le
C
kp
a_ka_pa_q.
}
$$

---

## Class IV

$$
|\mathcal R_{IV}|
=
q(p-k)|\Theta_\tau|.
$$

利用：

$$
p-k\le p,
$$

與：

$$
|g_{IV}|
\le
C\frac{k}{q},
$$

得：

$$
\boxed{
|\mathcal R_{IV}|
\le
C
kp
a_ka_pa_q.
}
$$

---

# 20. C3-D.5：Nonlocality Exponent Classification

令：

$$
\chi=\frac{k}{p}.
$$

因 strong nonlocal triad 有：

$$
q\sim p.
$$

所以 relative to raw cubic high-frequency scale：

$$
p^2a_ka_pa_q,
$$

有：

$$
\boxed{
\frac{
|\mathcal R_{II}|
}{
p^2a_ka_pa_q
}
\lesssim
\chi^2,
}
$$

而：

$$
\boxed{
\frac{
|\mathcal R_{III}|
}{
p^2a_ka_pa_q
}
\lesssim
\chi,
}
$$

$$
\boxed{
\frac{
|\mathcal R_{IV}|
}{
p^2a_ka_pa_q
}
\lesssim
\chi.
}
$$

因此：

$$
\boxed{
\mathrm{II}:\text{ quadratic nonlocality exponent},
}
$$

$$
\boxed{
\mathrm{III/IV}:\text{ linear nonlocality exponent}.
}
$$

---

# 21. Amplitude compensation debt

若一列 increasingly nonlocal triads：

$$
\chi_n\to0
$$

仍要維持 non-vanishing normalized pair production，則 cubic amplitude product必須至少補償：

### Class II

$$
\boxed{
a_{k_n}a_{p_n}a_{q_n}
\gtrsim
\chi_n^{-2}
}
$$

相對固定 normalized production scale。

### Classes III/IV

至少：

$$
\boxed{
a_{k_n}a_{p_n}a_{q_n}
\gtrsim
\chi_n^{-1}.
}
$$

這是 schematic normalized statement；真正 dimensional version必須保留 $p_n^2$。

本文稱：

$$
\boxed{
\textbf{Amplitude Compensation Debt}.
}
$$

它尚未被有限 global norm budget關閉。

---

# 22. 與 Aluie–Eyink scale-locality theorem 的關係

Aluie–Eyink 對 sharp spectral filter 的研究證明：

在具有正的 inertial-range velocity scaling exponent：

$$
0<\sigma_p<1
$$

的假設下，SGS energy flux 與 logarithmic inter-band transfer 由 scale-local triads主導。

特別地，對 $P\gg K$ 的 nonlocal band contribution，其 rigorous bounds 含有衰減 factor，例如：

$$
\left(\frac{K}{P}\right)^{2\sigma_3}.
$$

他們也明確指出：

$$
\boxed{
\text{scale-locality不是任意 Navier--Stokes solution 的無條件性質};
}
$$

證明依賴 turbulent scaling assumptions。

---

# 23. 不能偷用 locality theorem 解 Clay 問題

因此我們不得寫：

$$
\text{Aluie--Eyink}
\Rightarrow
\text{all nonlocal blow-up routes impossible}.
$$

正確使用方式是：

## Conditional locality dichotomy

假設 hypothetical near-singular solution 在某 high-frequency window 仍滿足一組 uniform inertial-type scaling bounds。

則 strongly nonlocal SGS flux contribution asymptotically negligible。

所以若 blow-up route **必須依賴 strong nonlocality**，它至少需要：

$$
\boxed{
\text{breakdown of those scale-locality hypotheses}.
}
$$

因此：

$$
\boxed{
\text{nonlocal singular route}
\Rightarrow
\text{either amplitude compensation or scaling-law breakdown}.
}
$$

這是一個 research dichotomy，不是 regularity theorem。

---

# 24. X-Integration guards 更新

對 heterochiral event新增：

### G-FSIG — cutoff-flux signature

保存：

$$
K\mapsto\Phi_\tau(K).
$$

不能只保存單一 transfer amplitude。

### G-FWIN — forward-window width

Class II：

$$
\operatorname{width}_{\log}
(p,q)
=
\log(q/p)
\le
\chi.
$$

### G-LOG — log-cutoff sign

若：

$$
\chi<\chi_\ast,
$$

positive Class II 必須標記：

$$
\boxed{
\mathfrak F_{II}<0.
}
$$

### G-KERNEL — helical geometry suppression

保存：

$$
g_{II}=O(1),
$$

$$
g_{III/IV}=O(\chi).
$$

### G-AMP — amplitude compensation

若：

$$
\chi\to0
$$

但 production不消失，必須顯式記錄 amplitude growth的來源。

---

# 25. Survivor map v2

## Homochiral

$$
\mathcal R=0.
$$

production source淘汰。

## Strongly nonlocal Class II

具有：

- quadratic pair-production tax；
- radial-drift congestion；
- broad reverse cutoff interval；
- narrow forward window；
- sufficiently nonlocal時 $\mathfrak F_{II}<0$。

因此：

$$
\boxed{
\text{不能單獨擔任 broad-band forward energy ancestry}.
}
$$

但仍可能貢獻 critical pair production。

## Strongly nonlocal Class III

具有：

- uniform forward cutoff sign；
- geometric $O(\chi)$ suppression；
- amplitude compensation debt。

仍存活。

## Strongly nonlocal Class IV

具有：

- uniform forward cutoff sign；
- unique sign在最高 mode；
- geometric $O(\chi)$ suppression；
- amplitude compensation debt。

仍是 primary frontier survivor。

## Local / moderately nonlocal III/IV

不受 small-$\chi$ suppression。

$$
\boxed{
\textbf{CURRENT PRIMARY SURVIVOR CORE}.
}
$$

---

# 26. 新核心縮減

經 C3-D：

$$
\boxed{
\text{singular production route}
}
$$

若存在，愈來愈像：

$$
\boxed{
\textbf{moderately local / local heterochiral forward frontier}
}
$$

或者必須支付：

$$
\boxed{
\text{extreme amplitude compensation}
+
\text{scale-locality breakdown}
}
$$

才能持續 strong nonlocal route。

---

# 27. 下一主題：C3-E

本輪之後最值得研究的已不是「nonlocal Class II」。

定義：

$$
\boxed{
\textbf{C3-E — Local Heterochiral Frontier Coherence}.
}
$$

問題：

> 當 survivor 被迫進入 $k\sim p\sim q$ 或至少 bounded scale ratio 的 heterochiral triads 後，能否在有限時間形成一條相位、空間、helicity 與 lineage 都持續相容的無限 UV genealogy？

這裡 strong-nonlocal cancellation不再救我們。

真正要攻：

- triad phase coherence；
- spatial concentration；
- vorticity alignment；
- branching multiplicity；
- local shell residence time；
- viscosity at comparable scale；
- X-Integration 的 repeated legality。

---

# 28. C3-E proof obligations

## E1 — Local pair-production packing

限制：

$$
c\le\frac{k}{p}\le1
$$

對 fixed：

$$
c>0.
$$

建立 dyadic shell pair-production：

$$
\mathcal R_q^{\rm loc}.
$$

研究 blow-up 是否要求：

$$
\sum_q
\int
[\mathcal R_q^{\rm loc}]_+dt
=
\infty.
$$

## E2 — Phase coherence duration

helical transfer包含：

$$
\Re
\left(
g_\tau
u_k u_p u_q
\right).
$$

amplitude 大不代表 positive production。

需要 phase alignment在 enough time intervals持續。

## E3 — Local residence-time bound

若：

$$
k\sim p\sim q\sim\lambda,
$$

viscous time：

$$
\tau_\nu
\sim
(\nu\lambda^2)^{-1}.
$$

研究 positive pair-production coherence是否必須在：

$$
O(\lambda^{-2})
$$

window內完成。

## E4 — Branching congestion

local triads數量龐大。

但若要形成 source-preserving singular genealogy，不能只靠「triads很多」。

需要：

$$
\boxed{
\text{parent identity}
+
\text{child identity}
+
\text{sign}
+
\text{phase}
+
\text{space overlap}
}
$$

逐代同時可黏合。

## E5 — X non-collapse

研究局部大量 triads 聚合成一個 scalar flux時是否把 genealogy差異坍縮。

X 積分要求：

$$
\boxed{
\text{aggregate flux}
\neq
\text{source-certified persistent chain}.
}
$$

這可能成為新的證明障礙，也可能是找到 obstruction 的位置。

---

# 29. 正式狀態

$$
\boxed{
\begin{aligned}
\text{Class-II cutoff-flux signature}
&:\ \mathrm{PROVED},\\
\text{III/IV uniform forward signature}
&:\ \mathrm{PROVED},\\
\text{Class-II boundary-layer forward window}
&:\ \mathrm{PROVED},\\
\text{Class-II log-cutoff reversal threshold}
&:\ \mathrm{PROVED},\\
\chi_\ast=W(e^{-1})
&:\ \mathrm{PROVED},\\
\text{Waleffe geometry nonlocal bounds}
&:\ \mathrm{PROVED\ from\ standard\ coefficient},\\
\text{II quadratic kernel exponent}
&:\ \mathrm{PROVED},\\
\text{III/IV linear kernel exponent}
&:\ \mathrm{PROVED},\\
\text{amplitude compensation debt}
&:\ \mathrm{DERIVED},\\
\text{unconditional aggregate nonlocal suppression}
&:\ \mathrm{OPEN},\\
\text{local heterochiral frontier obstruction}
&:\ \mathrm{OPEN}.
\end{aligned}
}
$$

---

# 30. 結論

C3-C 已指出 Class II strong nonlocal route非常昂貴。

C3-D 再證明：

$$
\boxed{
\text{positive Class II
在 }k<K<p\text{ 對 cutoff flux 是 reverse},
}
$$

而：

$$
\boxed{
\text{只有 }p<K<q\text{ 的窄 window 是 forward}.
}
$$

甚至當：

$$
\frac{k}{p}
<
W(e^{-1})
\approx0.27846,
$$

其 logarithmically scale-integrated energy flux必為：

$$
\boxed{
\mathfrak F_{II}<0.
}
$$

與此相對，positive Classes III/IV：

$$
\boxed{
\Phi(K)>0
\quad
\forall K\in(k,q).
}
$$

所以 III/IV 才是真正 broad-band forward-compatible pair-production classes。

另一方面，Waleffe helical geometry又告訴我們：

$$
\boxed{
\text{所有 strong-nonlocal forward classes仍支付至少 }O(k/p)\text{ kernel tax}.
}
$$

因此 survivor被再次壓向：

$$
\boxed{
\textbf{local / moderately local heterochiral forward frontier}.
}
$$

下一輪正式轉入：

$$
\boxed{
\textbf{C3-E — Local Heterochiral Frontier Coherence}.
}
$$

---

# References

1. F. Waleffe, *The nature of triad interactions in homogeneous turbulence*, Physics of Fluids A 4 (1992), 350–363.
2. F. Waleffe, *Inertial transfers in the helical decomposition*, Physics of Fluids A 5 (1993).
3. H. Aluie, G. L. Eyink, *Localness of energy cascade in hydrodynamic turbulence, I. Smooth coarse-graining*, arXiv:0909.2386.
4. H. Aluie, G. L. Eyink, *Localness of energy cascade in hydrodynamic turbulence, II. Sharp spectral filter*, arXiv:0909.2451.
5. L. Biferale, E. S. Titi, *On the Global Regularity of a Helical-decimated Version of the 3D Navier–Stokes Equations*, arXiv:1303.1215.
6. G. Sahoo, L. Biferale, *Disentangling the triadic interactions in Navier-Stokes equations*, arXiv:1510.09006.

# Internal dependencies

- `NS_C1_UV_Replenishment_Chain_v0.2.md`
- `NS_C2_Critical_Toll_Spike_Packing_v0.3.md`
- `NS_C3A_Conservation_Criticality_Helical_Pair_Production_v0.1.md`
- `NS_C3B_BiHelical_Equalization_UniqueSign_UV_Escape_v0.1.md`
- `NS_C3C_ClassII_Nonlocality_Tax_Radial_Congestion_v0.1.md`
- `True ETN / 無限維張力場`
- `X_Integral_Unified_Program_v0.2.md`

Next:

$$
\boxed{
\textbf{C3-E — Local Heterochiral Frontier Coherence}
}
$$
