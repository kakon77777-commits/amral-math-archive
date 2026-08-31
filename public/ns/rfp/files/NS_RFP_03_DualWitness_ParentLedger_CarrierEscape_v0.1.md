---
title: "Navier–Stokes Reverse Formation Program 03：Dual-Witness Parent Ledger、Exact Triadic Provenance 與 Carrier-Depth Escape"
short_title: "NS-RFP 03"
version: "v0.1"
date: "2026-08-14"
author: "Neo.K / EveMissLab"
language: "zh-TW"
status: "Theorem-style structural advance / partial Exact Parent Resolution"
epistemic_status: "Constructs an exact signed dyadic parent-output ledger for every source-paid first-passage edge using a dual norming witness; proves parent cancellation and multiplicity debts, Fourier-support ancestry guards, and subsequential parent-gap/carrier-depth concentration-escape classifications. Does NOT prove uniform parent tightness, spatial-core ancestry, full Chain Necessity, Finite Obstruction, or Navier–Stokes regularity."
canonical_source: "UTF-8 Markdown"
---

# Navier–Stokes Reverse Formation Program 03

# Dual-Witness Parent Ledger、Exact Triadic Provenance 與 Carrier-Depth Escape

## 0. 本文定位

NS-RFP 02 已將

$$
\operatorname{Blowup}(T_\ast)
\Longrightarrow
\text{critical UV escape}
$$

提升為

$$
\boxed{
\operatorname{Blowup}(T_\ast)
\Longrightarrow
\text{canonical adjacent-scale first-passage skeleton}.
}
$$

對每個 fixed threshold

$$
M>0,
$$

存在

$$
\tau_J(M)\uparrow T_\ast,
$$

而且

$$
\tau_J(M)\le\tau_{J+1}(M).
$$

每個 edge

$$
J\to J+1
$$

有 first-passage deficit

$$
d_J=M-\mathcal B_{J+1}(\tau_J)\ge0.
$$

RFP-02 得到

$$
d_J>0
\Longrightarrow
\text{positive aggregate nonlinear Duhamel source debt}.
$$

但仍存在兩個主要缺口：

$$
\boxed{\textbf{PF-A: Exact Parent Resolution}}
$$

以及

$$
\boxed{\textbf{PF-B: Synchronous / Deep-Tail Bypass}}.
$$

本文的核心進展是：

1. 把 PF-A 的 aggregate source debt 線性化成 exact signed dyadic parent-output ledger；
2. 證明 exact parent witness / parent multiplicity debt；
3. 證明 far upward generation 在單一 quadratic interaction 中不可能；
4. 證明 large parent-to-output downshift 只能來自 near-resonant high--high parents；
5. 把 PF-A remaining gap 壓成 parent-gap tightness vs resonant downshift escape；
6. 把 PF-B 壓成 carrier-depth tight / split / escape profile。

本文仍不是完整 Chain Necessity。

---

# 1. Setting

考慮

$$
\partial_tu-\nu\Delta u+\mathbb P\nabla\cdot(u\otimes u)=0,
$$

$$
\nabla\cdot u=0,
$$

在

$$
0\le t<T_\ast
$$

上 smooth。

為使 parent ledger 的 dyadic sums 可逐項交換，本文在 theorem-level parent decomposition 採 compact pre-singular windows 上的 smooth rapid-decay hypothesis。等價地，可使用足夠高 Sobolev regularity 加 spatial decay 來保證下述 series 與 Bochner integrals 的 absolute convergence。

---

# 2. Littlewood–Paley convention

取標準 inhomogeneous decomposition

$$
u=\sum_{j\ge-1}u_j,
$$

其中

$$
u_j=\Delta_j u.
$$

RFP-02 的 UV first-passage construction只使用充分大的 $J$，所以 finite low-frequency convention 不改變

$$
\mathcal B_J(t)
=
\left(
\sum_{j>J}\|u_j(t)\|_3^2
\right)^{1/2}.
$$

---

# 3. RFP-02 input

固定

$$
M>0.
$$

令

$$
s_J=\tau_J(M),
\qquad
t_J=\tau_{J+1}(M).
$$

並令

$$
\eta_J
=
\frac{\mathcal B_{J+1}(s_J)}{M},
$$

$$
d_J=M(1-\eta_J).
$$

RFP-02 已證：若

$$
d_J>0,
$$

則

$$
s_J<t_J,
$$

且 deeper-tail burden 從 $\mathcal B_{J+1}(s_J)$ 增加到

$$
\mathcal B_{J+1}(t_J)=M
$$

必支付 positive nonlinear Duhamel source debt。

---

# 4. Tail Banach space

定義

$$
\boxed{
X_J
=
\ell^2_{k>J}
\left(L^3(\mathbb R^3;\mathbb R^3)\right).
}
$$

其 norm 為

$$
\|(f_k)_{k>J}\|_{X_J}
=
\left(
\sum_{k>J}\|f_k\|_3^2
\right)^{1/2}.
$$

因此

$$
\mathcal B_J(t)=\|U_J(t)\|_{X_J},
$$

其中

$$
U_J(t)=(u_k(t))_{k>J}.
$$

其 dual 為

$$
\boxed{
X_J^*
=
\ell^2_{k>J}
\left(L^{3/2}(\mathbb R^3;\mathbb R^3)\right).
}
$$

pairing 使用

$$
\langle F,\Phi\rangle
=
\sum_{k>J}\int_{\mathbb R^3}f_k(x)\cdot\phi_k(x)\,dx.
$$

---

# 5. Tail heat operator

定義 diagonal heat operator

$$
\mathsf H_\sigma(f_k)_{k>J}
=
\left(e^{\nu\sigma\Delta}f_k\right)_{k>J}.
$$

因 heat semigroup 在 $L^3$ contractive，

$$
\boxed{
\|\mathsf H_\sigma F\|_{X_J}
\le
\|F\|_{X_J}.
}
$$

---

# 6. Nonlinear tail increment

對 PF-A edge $d_J>0$，使用 tail space $X_{J+1}$。

定義

$$
\boxed{
W_J
=
U_{J+1}(t_J)
-
\mathsf H_{t_J-s_J}U_{J+1}(s_J).
}
$$

由 Duhamel formula，

$$
W_J
=
-
\int_{s_J}^{t_J}
\mathsf H_{t_J-r}F_J^{tail}(r)\,dr,
$$

其中

$$
F_J^{tail}(r)
=
\left(
\Delta_k\mathbb P\nabla\cdot(u\otimes u)(r)
\right)_{k>J+1}.
$$

---

# 7. C3.1 — Tail Increment Debt

## Theorem 7.1

對每個 PF-A edge，令

$$
R_J:=\|W_J\|_{X_{J+1}}.
$$

則

$$
\boxed{R_J\ge d_J>0.}
$$

### Proof

由 reverse triangle inequality 與 heat contraction，

$$
\begin{aligned}
R_J
&\ge
\|U_{J+1}(t_J)\|_{X_{J+1}}
-
\|\mathsf H_{t_J-s_J}U_{J+1}(s_J)\|_{X_{J+1}}
\\
&\ge
M-\mathcal B_{J+1}(s_J)
\\
&=d_J.
\end{aligned}
$$

$\square$

---

# 8. 為何改追 $W_J$？

RFP-02 使用 positive quantity

$$
\int\mathcal N_{J+1}
$$

足以證明 nonlinear source 必須存在，但它先取 magnitude，因而不保存 sign、cancellation 與 exact parent contribution。

本文改追

$$
\boxed{W_J}
$$

本身，因為 $W_J$ 對 Duhamel source 是線性的。

---

# 9. Constructive norming witness

寫

$$
W_J=(w_k)_{k>J+1},
$$

$$
b_k=\|w_k\|_3,
\qquad
R_J=\left(\sum_{k>J+1}b_k^2\right)^{1/2}.
$$

若 $w_k\neq0$，定義

$$
\psi_k(x)
=
\frac{|w_k(x)|w_k(x)}{\|w_k\|_3^2},
$$

則

$$
\|\psi_k\|_{3/2}=1,
\qquad
\langle w_k,\psi_k\rangle=\|w_k\|_3.
$$

令

$$
\boxed{
\phi_k
=
\frac{b_k}{R_J}\psi_k
}
$$

且 $w_k=0$ 時令 $\phi_k=0$。

記

$$
\Phi_J=(\phi_k)_{k>J+1}.
$$

---

# 10. C3.2 — Dual-Witness Theorem

## Theorem 10.1

有

$$
\boxed{\|\Phi_J\|_{X_{J+1}^*}=1,}
$$

以及

$$
\boxed{\langle W_J,\Phi_J\rangle=R_J.}
$$

### Proof

由定義，

$$
\|\phi_k\|_{3/2}=\frac{b_k}{R_J},
$$

故

$$
\|\Phi_J\|_{X_{J+1}^*}^2
=
\sum_{k>J+1}\frac{b_k^2}{R_J^2}=1.
$$

且

$$
\begin{aligned}
\langle W_J,\Phi_J\rangle
&=
\sum_{k>J+1}
\frac{b_k}{R_J}
\langle w_k,\psi_k\rangle
\\
&=
\frac1{R_J}\sum_{k>J+1}b_k^2
\\
&=R_J.
\end{aligned}
$$

$\square$

---

# 11. Dual witness 的角色

$\Phi_J$ 不是 physical field，也不是新的 invariant。

它是

$$
\boxed{
\text{a norm-attaining linear certificate for the actual nonlinear tail increment}.
}
$$

因此可把 norm-level fact

$$
\|W_J\|_{X_{J+1}}
$$

重新翻成對 exact N--S source 的 linear pairing。

---

# 12. Dyadic parent-output source

對 $p,q\ge-1$ 及 output $k>J+1$ 定義 ordered dyadic parent-output source

$$
\boxed{
F_{k;p,q}(r)
=
\Delta_k\mathbb P\nabla\cdot(u_p\otimes u_q)(r).
}
$$

在本文 smooth/rapid-decay hypotheses 下，

$$
\Delta_k\mathbb P\nabla\cdot(u\otimes u)
=
\sum_{p,q\ge-1}F_{k;p,q}
$$

在所需 finite-window topology 中 absolutely convergent。

---

# 13. Exact signed triad ledger

定義

$$
\boxed{
\Lambda^{(J)}_{k;p,q}
=
-
\int_{s_J}^{t_J}
\left\langle
 e^{\nu(t_J-r)\Delta}F_{k;p,q}(r),
 \phi_k
\right\rangle dr.
}
$$

這是一個 signed quantity；它可以為正、零或負。

---

# 14. C3.3 — Exact Parent Ledger Identity

## Theorem 14.1

對每個 PF-A edge，

$$
\boxed{
\sum_{k>J+1}\sum_{p,q\ge-1}
\Lambda^{(J)}_{k;p,q}
=R_J.
}
$$

因此

$$
\boxed{
\sum_{k,p,q}\Lambda^{(J)}_{k;p,q}
\ge d_J.
}
$$

### Proof

由 Duhamel、dyadic source decomposition與 Theorem 10.1，

$$
\begin{aligned}
R_J
&=\langle W_J,\Phi_J\rangle
\\
&=-\int_{s_J}^{t_J}
\sum_{k>J+1}
\left\langle
 e^{\nu(t_J-r)\Delta}F_k(r),
 \phi_k
\right\rangle dr
\\
&=\sum_{k>J+1}\sum_{p,q\ge-1}
\Lambda^{(J)}_{k;p,q}.
\end{aligned}
$$

absolute convergence 保證交換合法。再用 $R_J\ge d_J$。$\square$

---

# 15. Exact ledger 不等於唯一 causal parent

本文得到的是 exact label

$$
(k;p,q),
$$

但 $\Lambda^{(J)}_{k;p,q}$ 的語義是：該 ordered dyadic parent pair 對 $\Phi_J$ 所識別的 actual nonlinear increment direction 的 signed contribution。

所以

$$
\boxed{
\text{exact ledger entry}
\neq
\text{unique causal parent}.
}
$$

---

# 16. Positive / negative parent ledgers

令

$$
[\lambda]_+=\max\{\lambda,0\},
\qquad
[\lambda]_- =\max\{-\lambda,0\}.
$$

定義

$$
\boxed{
P_J
=
\sum_{k,p,q}[\Lambda^{(J)}_{k;p,q}]_+,
}
$$

$$
\boxed{
N_J
=
\sum_{k,p,q}[\Lambda^{(J)}_{k;p,q}]_-.
}
$$

由 absolute convergence，

$$
P_J<\infty,
\qquad
N_J<\infty.
$$

---

# 17. C3.4 — Parent Cancellation Debt

## Theorem 17.1

有

$$
\boxed{P_J-N_J=R_J\ge d_J.}
$$

所以

$$
\boxed{P_J\ge d_J+N_J.}
$$

$\square$

定義 parent cancellation ratio

$$
\boxed{
\zeta_J=\frac{N_J}{P_J}.
}
$$

則

$$
0\le\zeta_J<1,
$$

以及

$$
\boxed{
P_J=\frac{R_J}{1-\zeta_J},
\qquad
N_J=\frac{\zeta_JR_J}{1-\zeta_J}.
}
$$

若 $\zeta_J\to1^-$，gross positive/negative parent activity 相對 net increment 必發散。

---

# 18. Exact parent witness

固定

$$
0<\theta<1.
$$

稱 triple $(k;p,q)$ 為 $\theta$-debt-paying parent witness，若

$$
\boxed{
[\Lambda^{(J)}_{k;p,q}]_+
\ge
\theta R_J.
}
$$

因 $R_J\ge d_J$，它至少支付 $\theta d_J$ 的 first-passage debt。

---

# 19. C3.5 — Parent Witness / Multiplicity Dichotomy

## Theorem 19.1

對每個 PF-A edge與任意 $0<\theta<1$，以下至少一個成立：

### Branch W — Exact parent witness

存在 $(k;p,q)$ 使

$$
[\Lambda^{(J)}_{k;p,q}]_+
\ge\theta R_J.
$$

### Branch M — Parent multiplicity debt

若不存在此 witness，positive ledger 至少有

$$
\boxed{
\left\lceil
\frac1{\theta(1-\zeta_J)}
\right\rceil
}
$$

個 nonzero parent-output triples。

### Proof

若 positive support有限且共有 $m$ 項，而每一項皆小於 $\theta R_J$，則

$$
P_J<m\theta R_J.
$$

使用

$$
P_J=\frac{R_J}{1-\zeta_J}
$$

得到

$$
m>\frac1{\theta(1-\zeta_J)}.
$$

若 support infinite，結論自動成立。$\square$

---

# 20. Multiplicity debt 的意義

Exact Parent Resolution 不再是二值的

$$
\text{found}
\vee
\text{not found}.
$$

它現在變成

$$
\boxed{
\text{single strong witness}
\vee
\text{quantified parent multiplicity}.
}
$$

並且 cancellation corridor 越嚴重，若沒有單一 strong witness，required multiplicity lower bound 越大。

---

# 21. Fourier-support guard

Littlewood--Paley parent labels不是任意 graph labels。存在 constants $C_0,C_1<\infty$，只依賴選定 LP partition，使 nonzero parent-output interactions obey固定 support geometry。

---

# 22. C3.6 — No Far Up-Jump Lemma

## Lemma 22.1

若

$$
F_{k;p,q}\neq0,
$$

則

$$
\boxed{
k\le\max\{p,q\}+C_0.
}
$$

等價地

$$
\boxed{
\max\{p,q\}\ge k-C_0.
}
$$

### Proof

在 Fourier space，存在 parent frequencies $\eta,\zeta$ 與 output frequency $\xi$ 滿足

$$
\xi=\eta+\zeta,
$$

以及

$$
|\eta|\sim2^p,
\qquad
|\zeta|\sim2^q,
\qquad
|\xi|\sim2^k.
$$

triangle inequality給

$$
|\xi|
\le
|\eta|+|\zeta|
\lesssim
2^{\max\{p,q\}}.
$$

轉成 dyadic index 即得。Leray projection、derivative與 heat multiplier均不擴大 Fourier support。$\square$

---

# 23. No spontaneous distant UV jump

Lemma 22.1 排除：

$$
p,q\ll k
$$

兩個遠低於 child 的 parent shells 在單一 quadratic interaction 中直接生成 $k$。

所以每個 high-frequency source event 都必含：

$$
\boxed{
\text{at least one parent within bounded distance below the output, or a parent already above it}.
}
$$

這是 equation-level ancestry restriction。

---

# 24. C3.7 — Resonant Downshift Lemma

## Lemma 24.1

存在 $C_1<\infty$，使若

$$
F_{k;p,q}\neq0
$$

且

$$
\max\{p,q\}-k>C_1,
$$

則

$$
\boxed{|p-q|\le C_1.}
$$

### Proof

若例如 $p\gg q$，則 low parent $q$ 無法抵銷 high parent $p$ 的 Fourier magnitude，因此

$$
|\eta+\zeta|\sim2^p,
$$

迫使

$$
k=p+O(1).
$$

故 large downward separation只能由 comparable high--high frequencies產生。$\square$

---

# 25. Parent-output gap

對 nonzero candidate triple 定義

$$
\boxed{
g(k;p,q)=\max\{p,q\}-k.}
$$

Lemma 22.1 給

$$
g(k;p,q)\ge-C_0.
$$

若

$$
g(k;p,q)\gg1,
$$

則 Lemma 24.1 強迫

$$
|p-q|=O(1).
$$

所以

$$
\boxed{
\text{large positive parent-output gap}
\Longrightarrow
\text{near-resonant high--high downshift}.
}
$$

---

# 26. Positive parent-gap ledger

固定

$$
L>C_1.
$$

定義

$$
P_J^{near}(L)
=
\sum_{g(k;p,q)\le L}
[\Lambda^{(J)}_{k;p,q}]_+,
$$

以及

$$
P_J^{down}(L)
=
\sum_{g(k;p,q)>L}
[\Lambda^{(J)}_{k;p,q}]_+.
$$

則

$$
P_J^{near}(L)+P_J^{down}(L)=P_J.
$$

---

# 27. C3.8 — Near-Parent / Resonant-Downshift Gross Dichotomy

## Theorem 27.1

對任意 $L>C_1$，至少有

$$
\boxed{P_J^{near}(L)\ge\frac{P_J}{2}}
$$

或

$$
\boxed{P_J^{down}(L)\ge\frac{P_J}{2}}.
$$

第二 branch 中所有 contributing triples皆屬 near-resonant high--high downshift。

又因

$$
P_J\ge d_J+N_J,
$$

dominant branch至少具有

$$
\frac{d_J+N_J}{2}
$$

的 positive gross activity。$\square$

---

# 28. Per-edge tightness 不等於 chain tightness

對每個固定 PF-A edge，由 absolute convergence，

$$
P_J^{down}(L)\to0
\qquad
(L\to\infty).
$$

所以每個單一 edge 的 positive parent-gap ledger 都 tight。

但所需 $L$ 可以依賴 $J$，因此

$$
\boxed{
\text{per-edge tightness}
\not\Rightarrow
\text{uniform ancestry tightness}.
}
$$

這是 full Chain Necessity 新的量詞缺口。

---

# 29. Normalized parent-gap profile

定義 positive probability ledger

$$
\mu_J(k,p,q)
=
\frac{[\Lambda^{(J)}_{k;p,q}]_+}{P_J}.
$$

則

$$
\sum_{k,p,q}\mu_J(k,p,q)=1.
$$

定義 cumulative parent tightness

$$
\boxed{
C_J^{par}(L)
=
\frac{P_J^{near}(L)}{P_J}.
}
$$

對每個 fixed $J$，

$$
C_J^{par}(L)\uparrow1
\qquad
(L\to\infty).
$$

---

# 30. C3.9 — Parent-Gap Concentration--Escape Theorem

## Theorem 30.1

取任意 infinite PF-A edge sequence

$$
J_n\to\infty.
$$

存在 subsequence，仍記為 $J_n$，使對每個 integer $L>C_1$，

$$
c^{par}(L)
=
\lim_{n\to\infty}C_{J_n}^{par}(L)
$$

存在。

且 $c^{par}(L)$ 對 $L$ 單調不減，因此

$$
\boxed{
\alpha_{par}
=
\lim_{L\to\infty}c^{par}(L)
\in[0,1].
}
$$

### Proof

對 $L=C_1+1,C_1+2,\ldots$ 逐次抽 subsequence，再做 diagonal extraction。各 $C_J^{par}(L)$ 落在 $[0,1]$，而 monotonicity 在 limit 中保留。故 $c^{par}(L)$ 作為 bounded monotone sequence 有 $L\to\infty$ 極限。$\square$

---

# 31. Parent-gap 三 regime

### PT — Parent-tight

$$
\boxed{\alpha_{par}=1.}
$$

所有 positive ledger mass 在 subsequential limit 中最終可由 finite parent-output gap 捕捉。

### PS — Parent-split

$$
\boxed{0<\alpha_{par}<1.}
$$

部分 source activity 保持 bounded-gap，部分向 arbitrarily large positive parent-output gap 逃逸。

### PE — Parent-escape

$$
\boxed{\alpha_{par}=0.}
$$

任何 fixed parent-output gap window 在 limit 中都捕捉不到 positive ledger mass。

由 Lemma 24.1，PS / PE 的 escaped mass 若沿 $g\to+\infty$ 逃逸，只能由 near-resonant high--high parents 支付。

因此

$$
\boxed{
\text{parent-gap escape}
\Longrightarrow
\text{resonant high--high downshift escape}.
}
$$

---

# 32. PF-A 現在真正剩下的 gap

RFP-03 已把 Exact Parent Resolution 從模糊的「找 parent」改寫為：

$$
\boxed{
\text{strong exact witness}
\vee
\text{quantified parent multiplicity}
}
$$

再乘上

$$
\boxed{PT\vee PS\vee PE.}
$$

因此 missing information已經轉成 uniform tightness、witness persistence 與 resonant-downshift control。

---

# 33. PF-B：synchronous bypass

現在考慮

$$
d_J=0.
$$

由 RFP-02，

$$
\mathcal B_{J+1}(s_J)=M,
\qquad
\mathcal B_J(s_J)=M,
$$

所以

$$
\boxed{\|u_{J+1}(s_J)\|_3=0,}
$$

且

$$
s_J=t_J.
$$

因此 PF-A 的 positive-time Duhamel increment不能直接使用。

---

# 34. Zero interval debt is not zero history

由 $s_J=t_J$ 只能推出：所選 first-passage edge沒有 positive time interval。

不能推出 deeper tail沒有 earlier nonlinear formation history。

所以 PF-B 要追的不是 interval source debt，而是

$$
\boxed{
\text{where the threshold burden already resides at the synchronous crossing time}.
}
$$

---

# 35. Carrier weights

在

$$
t=s_J=\tau_J(M)
$$

定義

$$
\boxed{
\omega_{J,r}
=
\frac{\|u_{J+r}(s_J)\|_3^2}{M^2},
\qquad r\ge1.
}
$$

由 $\mathcal B_J(s_J)=M$，

$$
\sum_{r\ge1}\omega_{J,r}=1.
$$

PF-B 另有

$$
\boxed{\omega_{J,1}=0.}
$$

定義 cumulative carrier profile

$$
\boxed{
C_J^{car}(L)
=
\sum_{r=1}^{L}\omega_{J,r}.
}
$$

對 fixed $J$，

$$
C_J^{car}(L)\uparrow1
\qquad
(L\to\infty).
$$

---

# 36. C3.10 — Carrier-Depth Concentration--Escape Theorem

## Theorem 36.1

取任意 infinite PF-B subsequence

$$
J_n\to\infty.
$$

存在 further subsequence，使每個 fixed $L$ 皆有

$$
c^{car}(L)
=
\lim_{n\to\infty}C_{J_n}^{car}(L).
$$

令

$$
\boxed{
\alpha_{car}
=
\lim_{L\to\infty}c^{car}(L)
\in[0,1].
}
$$

### Proof

同 Theorem 30.1，使用 diagonal extraction 與 monotonicity。$\square$

---

# 37. Carrier-depth 三 regime

### CT — Carrier-tight

$$
\boxed{\alpha_{car}=1.}
$$

synchronous threshold burden在 subsequential limit中可由 finite offset shells 捕捉。

### CS — Carrier-split

$$
\boxed{0<\alpha_{car}<1.}
$$

部分 burden 留在 bounded offset，部分向 arbitrarily deep shells逃逸。

### CE — Carrier-escape

$$
\boxed{\alpha_{car}=0.}
$$

對任意 fixed $L$，

$$
C_{J_n}^{car}(L)\to0.
$$

所以任何 fixed number of shells above $J_n$ 都無法承載 nontrivial fraction of threshold burden。

---

# 38. PF-A 與 PF-B 的 escape 不同

$\alpha_{par}$ 描述

$$
\text{source provenance geometry},
$$

而 $\alpha_{car}$ 描述

$$
\text{state occupancy geometry}.
$$

因此

$$
\boxed{\alpha_{par}\neq\alpha_{car}}
$$

不是數值不等式，而是提醒兩者根本屬於不同 typed layer，不能互相替代。

---

# 39. C3.11 — Infinite Edge Subsequence Classification

## Theorem 39.1

考慮任意 infinite first-passage edge sequence

$$
J_n\to\infty.
$$

存在 subsequence落入以下之一：

### A — PF-A source-paid subsequence

$$
d_{J_n}>0
$$

對所有 $n$，且 parent-gap profile 再分

$$
PT\vee PS\vee PE.
$$

### B — PF-B synchronous subsequence

$$
d_{J_n}=0
$$

對所有 $n$，且 carrier-depth profile 再分

$$
CT\vee CS\vee CE.
$$

### Proof

binary partition $d_J>0$ 與 $d_J=0$ 至少一支含 infinite subsequence，再套 Theorem 30.1 或 36.1。$\square$

---

# 40. 最接近 full ancestry 的 branch

目前最接近完整 source-traceable ancestry的是

$$
\boxed{\mathrm{PF\mbox{-}A}+PT.}
$$

但仍需要：

1. 將 subsequential parent tightness升級成 uniform / quantitative tightness；
2. 將 strong witnesses跨 edge 串成 persistent parent-child history；
3. 將 global frequency labels附著到 physical-space cores；
4. 控制 pressure/localization commutators；
5. 保存時間方向與 source stock/supply separation。

---

# 41. PE / CE 的研究意義

若 PE 或 CE 可持續實現，bounded-gap local-cascade proof strategy 將失敗。

但這不等於 RFP 失敗；escape route已被壓縮為

$$
\boxed{
\text{resonant high--high downshift}
}
$$

或

$$
\boxed{
\text{deep carrier escape}.
}
$$

未來可專門對這兩種 geometry 建立 tax / obstruction。

---

# 42. 與 classical dyadic flux analysis 的關係

經典 Littlewood--Paley energy-flux analysis表明 nonlinear flux 可按 dyadic shells 組織，且 frequency localization 對 transfer structure提供實質限制。

本文不把 energy-flux identity直接當成 $L^3$ first-passage parent theorem；本文的主要新操作是

$$
\boxed{X_J-X_J^*\text{ dual norming witness},}
$$

其目的在於解析 actual Duhamel increment direction，而不是只追 scalar energy flux。

---

# 43. 與 recent triadic / ledger work 的關係

2026 年已有 preprint以 explicit triadic Fourier decomposition建立 deterministic scale-resolved energy-transfer representation，也有 finite-scale critical-ledger work強調 defect、positive cone與 anti-phantom tests 必須分開。

本文把這些視為 contemporary comparison，不把其任何 global claim當作本文 theorem input。

Theorems 7.1--39.1 所需核心只有：

- Duhamel formula；
- standard LP decomposition；
- $L^3$ heat contraction；
- explicit Banach dual witness；
- Fourier support geometry；
- smooth finite-window absolute convergence。

---

# 44. New guards

新增以下 hard guards：

### $G_{\rm DUAL}$

從 norm magnitude升級 parent contribution時，必須有 linear witness / dual certificate 或等價 bridge。

### $G_{\rm SIGN}$

必須保存 signed ledger，不能只保存 $|\Lambda_{k;p,q}|$。

### $G_{\rm PMULT}$

沒有 single strong witness時，必須保存 parent multiplicity debt。

### $G_{\rm DOWN}$

large parent-output downshift 必須滿足 near-resonant high--high support condition。

### $G_{\rm PTIGHT}$

per-edge tightness不得偷換成 uniform chain tightness。

### $G_{\rm CARRIER}$

PF-B 的 zero interval debt 不得偷換成 zero historical source；必須保存 carrier-depth profile。

---

# 45. Guard Library v2

因此

$$
\boxed{
\mathcal G_{NS}^{(2)}
=
\mathcal G_{NS}^{(1)}
\cup
\{
G_{\rm DUAL},
G_{\rm SIGN},
G_{\rm PMULT},
G_{\rm DOWN},
G_{\rm PTIGHT},
G_{\rm CARRIER}
\}.
}
$$

---

# 46. Chain Necessity 更新

RFP-02 將 full CN gap壓成

$$
\text{Synchronous-Bypass Resolution}
+
\text{Exact Parent Resolution}
+
\text{Spatial-Core Attachment}.
$$

RFP-03 後，Exact Parent Resolution進一步拆成

$$
\boxed{
\text{Dual Parent Ledger}
+
\text{Witness/Multiplicity}
+
\text{Parent-Gap Tightness}.
}
$$

前兩項本文完成；第三項只完成 subsequential PT / PS / PE classification。

---

# 47. Remaining obligations

## O1 — Uniform Parent Tightness

能否排除 PS / PE，或至少證 PT 含 sufficient ancestry subsequence？

## O2 — Witness Persistence

每個 edge 的 strong $(k;p,q)$ witness 能否跨 edge 串成 consistent parent-child history？

## O3 — Parent Cancellation Control

能否由 exact N--S structure限制

$$
\zeta_J\to1^-?
$$

## O4 — Resonant Downshift Control

能否控制

$$
g\to+\infty,
\qquad
|p-q|=O(1)
$$

的 high--high downshift source？

## O5 — Carrier Escape Control

能否排除或 rigidify CE？

## O6 — Spatial Core Attachment

如何將 global-frequency dual witness $\Phi_J$ 連到 $\Omega_J$ 與 C3-O adjoint ancestry tube？

---

# 48. 為何下一篇必須 spatialize？

目前 exact parent ledger仍是

$$
\boxed{\text{global-frequency provenance}.}
$$

真正 singularity formation 必須同時保存

$$
(x,t,\lambda).
$$

所以還需要

$$
\boxed{
(k;p,q)
\longrightarrow
(\Omega_k;\Omega_p,\Omega_q)
}
$$

的 localization bridge。

但 localization會引入 cutoff commutators、pressure nonlocality、forced N--S terms 與 moving-core geometry。

---

# 49. 下一篇

正式下一篇：

$$
\boxed{
\textbf{NS-RFP 04 — Spatial Core Attachment、Pressure-Compatible Localization 與 Uniform Parent Tightness}.
}
$$

核心任務：

1. 對 $\Phi_J$ 建立 physical-space localization；
2. 控制 $[\chi,\Delta_k]$ 與 $[\chi,\mathbb P]$；
3. 將 pressure做 near/far provenance split；
4. 接入 C3-O adjoint ancestry tube；
5. 判定 PT 能否升級成 spacetime ancestry；
6. 對 PE / CE 建立 nonlocal escape taxes。

---

# 50. Formal status ledger

$$
\boxed{
\begin{aligned}
\text{tail Banach-space reformulation}
&:\ \mathrm{PROVED},\\
\text{constructive dual norming witness}
&:\ \mathrm{PROVED},\\
\text{exact signed dyadic parent ledger}
&:\ \mathrm{PROVED\ under\ smooth/decay\ hypotheses},\\
\text{parent cancellation debt}
&:\ \mathrm{PROVED},\\
\text{parent witness/multiplicity dichotomy}
&:\ \mathrm{PROVED},\\
\text{no far upward quadratic jump}
&:\ \mathrm{PROVED},\\
\text{far downshift implies resonant high--high parents}
&:\ \mathrm{PROVED},\\
\text{parent-gap subsequential concentration--escape}
&:\ \mathrm{PROVED},\\
\text{carrier-depth subsequential concentration--escape}
&:\ \mathrm{PROVED},\\
\text{uniform parent tightness}
&:\ \mathrm{OPEN},\\
\text{witness persistence across edges}
&:\ \mathrm{OPEN},\\
\text{resonant downshift exclusion}
&:\ \mathrm{OPEN},\\
\text{carrier escape exclusion}
&:\ \mathrm{OPEN},\\
\text{spatial-core ancestry}
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

# 51. 結論

RFP-02 得到

$$
\boxed{
\text{time order}
+
\text{scale order}
+
\text{aggregate nonlinear source debt}.
}
$$

RFP-03 再往前一步：

$$
\boxed{
\text{aggregate source debt}
\longrightarrow
\text{exact signed parent-output ledger}.
}
$$

對每個 PF-A edge，存在 dual witness $\Phi_J$ 使

$$
\boxed{
R_J
=
\sum_{k,p,q}\Lambda^{(J)}_{k;p,q}
\ge d_J.
}
$$

若沒有 single strong witness，就必須支付 quantified parent multiplicity debt；若 cancellation接近 perfect，multiplicity lower bound更強。

同時 Fourier support排除 two far-lower parents 在一步 quadratic interaction 中生成 far-higher child，而 large downward parent-output gap只能走 near-resonant high--high route。

因此 PF-A remaining route被壓成

$$
\boxed{PT\vee PS\vee PE,}
$$

PF-B 則被壓成

$$
\boxed{CT\vee CS\vee CE.}
$$

新的 frontier 不再只是「source 在哪裡」，而是：

$$
\boxed{
\text{can exact frequency provenance be made uniformly tight, persistent, and spatially attached?}
}
$$

這就是 NS-RFP 04。

---

# References

1. J.-M. Bony, *Calcul symbolique et propagation des singularités pour les équations aux dérivées partielles non linéaires*, Annales scientifiques de l'École Normale Supérieure 14 (1981), 209–246.
2. A. Cheskidov, P. Constantin, S. Friedlander, R. Shvydkoy, *Energy conservation and Onsager's conjecture for the Euler equations*, Nonlinearity 21 (2008), 1233–1252; arXiv:0704.0759.
3. Z. Bradshaw, Z. Grujić, *Frequency localized regularity criteria for the 3D Navier–Stokes equations*, Archive for Rational Mechanics and Analysis 224 (2017), 125–133; arXiv:1501.01043.
4. A. Cheskidov, R. Shvydkoy, *A unified approach to regularity problems for the 3D Navier–Stokes and Euler equations: the use of Kolmogorov's dissipation range*, Journal of Mathematical Fluid Mechanics 16 (2014), 263–273.
5. Z. Bradshaw, T.-P. Tsai, *On the local pressure expansion for the Navier–Stokes equations*, Journal of Mathematical Fluid Mechanics 24 (2022); arXiv:2001.11526.
6. T. Barker, C. Prange, *Localized smoothing for the Navier–Stokes equations and concentration of critical norms near singularities*, Archive for Rational Mechanics and Analysis 236 (2020), 1487–1541; arXiv:1812.09115.
7. R. Yu, *Critical Ledgers and Scale-Defect Cascades for Navier–Stokes*, arXiv:2606.13887 (2026). Contemporary comparison only; no global conclusion from this preprint is used as an input theorem here.
8. E. Bertram, *From Triadic Interactions to Kolmogorov Scaling: A Deterministic, Scale-Resolved Formulation of Energy Flux*, arXiv:2607.16381 (2026). Contemporary comparison only; no global conclusion from this preprint is used as an input theorem here.

# Internal dependencies

- `NS_RFP_01_SingularityFormationAncestry_FiniteObstruction_v0.1.md`
- `NS_RFP_02_CriticalUV_FirstPassage_SourceDebt_v0.1.md`
- `NS_C3O_AdjointCore_BalanceDynamicsSeparation_v0.2.md`
- `NS_ETN_XIntegration_Multiscale_NonCollapse_v0.1.md`
- `True ETN / 無限維張力場`
- `X_Integral_Unified_Program_v0.2.md`

# Next

$$
\boxed{
\textbf{NS-RFP 04 — Spatial Core Attachment、Pressure-Compatible Localization 與 Uniform Parent Tightness}
}
$$
