---
title: "Navier–Stokes C4-D：Amplitude-to-Flux Branching Bridge、Local Work Cancellation 與 Helical-Cancellation Rigidity"
subtitle: "A Persistence-or-Work Theorem for Critical Shell Crossings and a Same-Event Reduction from Amplitude Growth to Source Overcapacity, Energy Work, or Helical/Spatial Cancellation"
version: "v0.1"
date: "2026-08-15"
author: "Neo.K / EveMissLab"
language: "zh-TW"
status: "Theorem-style shared-event coupling / structural reduction"
epistemic_status: "Exact first-crossing envelope calculus + band-limited localization + helical triad algebra. The final bridge is branching, not a direct amplitude-to-flux implication. Does NOT prove Navier–Stokes regularity."
---

# Navier–Stokes C4-D
# Amplitude-to-Flux Branching Bridge、Local Work Cancellation 與 Helical-Cancellation Rigidity

## 0. 本輪定位

C4-C 已建立多條 same-event edges：

$$
\text{UV amplitude}
\to
\text{critical helical / strain / vorticity stock},
$$

$$
\text{robust heterochiral highest-mode gain}
\to
\text{positive helical variation},
$$

$$
\text{strain growth}
\to
\text{pressure}
\vee
\text{Betchov}
\vee
\text{vortex stretching},
$$

$$
\text{Miller operator escape}
\to
\text{advection}
\vee
S^2
\vee
\omega^2.
$$

但最關鍵的 hereditary UV anchor：

$$
a_q^\sigma(t)
=
\frac{
\|u_q^\sigma(t)\|_\infty
}{
\nu\lambda_q
}
$$

仍是 amplitude event，

而 helical triad coupling最強的 antecedent是：

$$
\boxed{
\text{positive high-mode nonlinear energy work}.
}
$$

C4-C 已證：

$$
\boxed{
\text{amplitude}
\not\Rightarrow
\text{flux}
}
$$

from norm data alone。

C4-D 的工作：

> 不再追求錯誤的 direct implication，
> 而是在真正 N–S evolution上證一條 branching bridge。

主要結果：

1. critical shell first crossing必落入：
   $$
   \boxed{
   \text{viscous-scale persistence}
   \vee
   \text{fast amplitude crossing};
   }
   $$
2. fast crossing的 positive amplitude variation，在最大點上必由 nonlinear source正向驅動；
3. output shell band-limit把 pointwise source轉成 shell-scale positive local nonlinear-work ball；
4. integrated fast crossing因此必支付：
   $$
   \boxed{
   \text{source-overcapacity impulse}
   \vee
   \text{positive shell nonlinear work}
   \vee
   \text{spatial work cancellation};
   }
   $$
5. 這是真正的 **Amplitude-to-Work Branching Bridge**；
6. positive shell work若由 highest-rank robust heterochiral triads承擔，立即同步 critical helical production；
7. robust helical cancellation不是獨立 escape：
   negative pair production同時意味 negative highest-mode nonlinear work；
8. 因此 robust helical cancellation可被壓回：
   $$
   \boxed{
   \text{high-mode work cancellation debt};
   }
   $$
9. 真正剩餘 UV work逃逸只剩：
   - non-top-rank gain；
   - homochiral gain；
   - radial-gap degeneration；
   - work cancellation；
10. 所以 C4-C 的 Amplitude-to-Flux Barrier被部分閉合：
    $$
    \boxed{
    \text{direct bridge FALSE},
    \quad
    \text{finite branching bridge TRUE}.
    }
    $$

---

# 1. Fresh primary-source audit

本輪 fresh audit對齊：

## Cheskidov–Dai

frequency-localized vorticity regularity criteria確認：

$$
\boxed{
\text{potential singularity必須反覆支付 high-frequency critical toll}.
}
$$

但它不自動給 shell energy-flux sign。

## Waleffe 1992

helical Fourier decomposition把 triadic interactions按 helicity signs分類，

並顯示不同 helical classes具有不同 energy-transfer方向與 local/nonlocal transfer結構。

本輪的 triad ratio calculations建立在：

- triad energy conservation；
- triad helicity conservation；

上，不使用 turbulence statistical closure。

## Lei–Lin–Zhou

critical helical energy identity證實：

$$
\boxed{
\text{helical critical stock / pair-production是 full N--S 真實 PDE quantity}.
}
$$

## Biferale–Titi

single-helicity-sign decimated N–S存在 sign-definite critical helicity並 global regular，

因此 homochiral branch不能和 full heterochiral production route混同。

---

# 2. Shell equation

固定 dyadic shell：

$$
q
$$

與 helicity：

$$
\sigma.
$$

令：

$$
\boxed{
f(t,x)
=
u_q^\sigma(t,x)
=
\Delta_qP^\sigma u(t,x).
}
$$

令：

$$
\lambda
=
\lambda_q.
$$

定義 shell nonlinear source：

$$
\boxed{
N(t,x)
=
\Delta_q
P^\sigma
\mathbb P
\nabla\cdot(u\otimes u).
}
$$

則：

$$
\boxed{
\partial_tf
-
\nu\Delta f
+
N
=
0.
}
$$

$f$ 與 $N$ 的 Fourier support都位於：

$$
|\xi|\asymp\lambda
$$

的 fixed annulus。

所以 Bernstein：

$$
\boxed{
\|\nabla f\|_\infty
\le
C_f
\lambda
\|f\|_\infty,
}
$$

$$
\boxed{
\|\nabla N\|_\infty
\le
C_N
\lambda
\|N\|_\infty.
}
$$

---

# 3. Critical amplitude

定義：

$$
\boxed{
a(t)
=
\frac{
\|f(t)\|_\infty
}{
\nu\lambda
}.
}
$$

固定：

$$
0<\beta_0<\beta_1.
$$

令：

$$
t_1
$$

為某次：

$$
\beta_1
$$

first / hysteretic crossing：

$$
\boxed{
a(t_1)=\beta_1.
}
$$

令：

$$
t_0<t_1
$$

為 crossing前最後一次：

$$
a(t_0)=\beta_0
$$

的時間，

如果存在。

則：

$$
\boxed{
a(t)>\beta_0
\qquad
t_0<t<t_1.
}
$$

---

# 4. Viscous window

固定：

$$
\theta>0.
$$

定義：

$$
\boxed{
\tau_\lambda
=
\frac{
\theta
}{
\nu\lambda^2
}.
}
$$

看 backward window：

$$
\boxed{
I_\lambda
=
[t_1-\tau_\lambda,t_1].
}
$$

---

# 5. C4-D.1：Persistence-or-Fast-Crossing Dichotomy

## 定理 5.1

對任何：

$$
\beta_0<\beta_1,
$$

必有：

## Branch D-PERSIST

$$
\boxed{
a(t)>\beta_0
\qquad
\forall t\in I_\lambda;
}
$$

或：

## Branch D-FAST

存在：

$$
t_0\in I_\lambda
$$

使：

$$
a(t_0)=\beta_0,
$$

$$
a(t_1)=\beta_1,
$$

且：

$$
\boxed{
t_1-t_0
\le
\frac{
\theta
}{
\nu\lambda^2
}.
}
$$

### 證明

若 backward viscous window內沒有：

$$
\beta_0
$$

crossing，

而：

$$
a(t_1)=\beta_1>\beta_0,
$$

由最後-crossing定義，

整個 window只能保持：

$$
a>\beta_0.
$$

否則最後 crossing必落在 window內。$\square$

---

# 6. C4 synchronization meaning

所以每一個：

$$
\beta_1
$$

crossing不是任意 pulse。

它首先已經滿足：

$$
\boxed{
\textbf{one full viscous window of UV persistence}
}
$$

或：

$$
\boxed{
\textbf{fast nonlinear crossing}.
}
$$

D-PERSIST 可直接送回 C4-A persistence-to-synchronization machinery。

因此 C4-D 真正只需研究：

$$
\boxed{
\text{D-FAST}.
}
$$

---

# 7. Sup norm envelope

令：

$$
\boxed{
M(t)
=
\|f(t)\|_\infty.
}
$$

在 smooth pre-singular interval，

$f$ 與：

$$
\partial_tf
$$

皆 continuous且 band-limited，

因此：

$$
M(t)
$$

locally Lipschitz。

又：

$$
f(t)\in L^2
$$

且 band-limited，

所以：

$$
f(t,x)\to0
$$

as：

$$
|x|\to\infty,
$$

因此：

$$
M(t)
$$

在某：

$$
x_t
$$

達到。

---

# 8. Envelope derivative

在：

$$
M
$$

可微的 a.e. time，

存在 maximizing point：

$$
x_t
$$

與：

$$
\boxed{
e_t
=
\frac{
f(t,x_t)
}{
M(t)
}
}
$$

使：

$$
\boxed{
M'(t)
=
e_t\cdot
\partial_tf(t,x_t).
}
$$

這是標準 max-envelope / Danskin-type fact。

---

# 9. Viscosity在 amplitude maximum的符號

在：

$$
x_t
$$

有：

$$
\nabla|f|^2=0,
$$

$$
\Delta|f|^2\le0.
$$

而：

$$
f\cdot\Delta f
=
\frac12
\Delta|f|^2
-
|\nabla f|^2.
$$

所以：

$$
\boxed{
e_t\cdot\Delta f(t,x_t)
\le0.
}
$$

---

# 10. C4-D.2：Positive Amplitude Variation Requires Positive Nonlinear Source

由 shell equation：

$$
\partial_tf
=
\nu\Delta f-N.
$$

所以：

$$
M'
=
\nu e\cdot\Delta f
-
e\cdot N
\le
-
e\cdot N.
$$

因此在：

$$
M'(t)>0
$$

的 differentiability times：

$$
\boxed{
g(t)
:=
-e_t\cdot N(t,x_t)
\ge
M'(t)>0.
}
$$

這是一個 exact same-time amplitude/source coupling。

---

# 11. Positive variation budget of a fast crossing

D-FAST 中：

$$
M(t_1)-M(t_0)
=
\nu\lambda
(\beta_1-\beta_0).
$$

令：

$$
\Delta\beta
=
\beta_1-\beta_0.
$$

因：

$$
M
$$

absolutely continuous：

$$
\boxed{
\int_{t_0}^{t_1}
[M'(t)]_+dt
\ge
\nu\lambda
\Delta\beta.
}
$$

所以 fast crossing必支付 fixed amplitude positive variation。

---

# 12. Source efficiency

在：

$$
M'(t)>0
$$

時定義：

$$
\boxed{
\eta(t)
=
\frac{
g(t)
}{
\|N(t)\|_\infty
}
\in(0,1].
}
$$

固定：

$$
0<\eta_0<1.
$$

定義：

$$
G
=
\{
t:
M'(t)>0,\ 
\eta(t)\ge\eta_0
\},
$$

$$
B
=
\{
t:
M'(t)>0,\ 
\eta(t)<\eta_0
\}.
$$

---

# 13. Good/bad positive variation split

由：

$$
\int[M']_+
\ge
\nu\lambda\Delta\beta,
$$

至少：

## D-SRC

$$
\boxed{
\int_B
M'(t)dt
\ge
\frac12
\nu\lambda\Delta\beta,
}
$$

或：

## D-WORK

$$
\boxed{
\int_G
M'(t)dt
\ge
\frac12
\nu\lambda\Delta\beta.
}
$$

---

# 14. Source-overcapacity branch

在：

$$
B
$$

上：

$$
g
<
\eta_0
\|N\|_\infty.
$$

而：

$$
g\ge M'.
$$

所以：

$$
\boxed{
\|N(t)\|_\infty
>
\frac{
M'(t)
}{
\eta_0
}.
}
$$

因此：

## 定理 14.1

若 D-SRC 成立，

$$
\boxed{
\frac1{
\nu\lambda
}
\int_B
\|N(t)\|_\infty dt
\ge
\frac{
\Delta\beta
}{
2\eta_0
}.
}
$$

本文稱：

$$
\boxed{
\textbf{Nonlinear Source-Overcapacity Impulse}.
}
$$

---

# 15. Source-overcapacity的空間 stock

因：

$$
N
$$

band-limited，

Bernstein反推：

$$
\|N\|_2
\ge
c
\lambda^{-3/2}
\|N\|_\infty.
$$

所以大 source-overcapacity也意味着：

$$
\boxed{
\text{a large shell-local nonlinear-source stock}.
}
$$

目前沒有 finite critical budget可直接排除此 branch。

---

# 16. Local work density

在 D-WORK branch，

考慮：

$$
t\in G.
$$

令：

$$
x=x_t,
\quad
e=e_t,
\quad
M=M(t),
\quad
g=g(t).
$$

定義 nonlinear shell work density：

$$
\boxed{
w(t,y)
=
-f(t,y)\cdot N(t,y).
}
$$

在：

$$
y=x
$$

：

$$
\boxed{
w(t,x)
=
M g
>0.
}
$$

---

# 17. C4-D.3：Band-Limited Local Positive-Work Ball

## 定理 17.1

存在 universal：

$$
c_\ast>0
$$

只依 LP cutoff，

使對：

$$
t\in G
$$

ball：

$$
\boxed{
B_t
=
B
\left(
x_t,
c_\ast
\eta_0
\lambda^{-1}
\right)
}
$$

滿足：

$$
\boxed{
w(t,y)
\ge
c_\ast
M(t)g(t)
\qquad
y\in B_t.
}
$$

### 證明

Bernstein：

$$
|f(y)-Me|
\le
C_f
\lambda M|y-x|,
$$

$$
|N(y)-N(x)|
\le
C_N
\lambda
\|N\|_\infty
|y-x|.
$$

取：

$$
|y-x|
\le
c_\ast\eta_0\lambda^{-1}.
$$

因：

$$
g\ge
\eta_0\|N\|_\infty,
$$

可令：

$$
-e\cdot N(y)
\ge
\frac34g,
$$

以及：

$$
|f(y)-Me|
\le
\frac{
\eta_0
}{8}
M.
$$

故：

$$
-f(y)\cdot N(y)
\ge
\frac34Mg
-
\frac{\eta_0}{8}
M\|N\|_\infty
\ge
\frac58Mg.
$$

調整 universal constant即可。$\square$

---

# 18. Local positive work rate

ball volume：

$$
|B_t|
\asymp
\eta_0^3
\lambda^{-3}.
$$

所以：

$$
\boxed{
L(t)
:=
\int_{B_t}
w(t,y)dy
\ge
c
\eta_0^3
\lambda^{-3}
M(t)
g(t).
}
$$

又：

$$
g\ge M',
$$

且 crossing interval：

$$
M(t)\ge
\nu\lambda\beta_0.
$$

因此：

$$
\boxed{
L(t)
\ge
c
\eta_0^3
\nu
\beta_0
\lambda^{-2}
M'(t).
}
$$

---

# 19. C4-D.4：Integrated Local Work Toll

若 D-WORK 成立：

$$
\int_GM'dt
\ge
\frac12
\nu\lambda\Delta\beta,
$$

所以：

$$
\boxed{
\int_G
L(t)dt
\ge
c
\eta_0^3
\beta_0
\Delta\beta
\frac{
\nu^2
}{
\lambda
}.
}
$$

乘 critical weight：

$$
\lambda/\nu^2,
$$

得到：

$$
\boxed{
\frac{
\lambda
}{
\nu^2
}
\int_G
L(t)dt
\ge
c
\eta_0^3
\beta_0
\Delta\beta.
}
$$

這是：

$$
\boxed{
\textbf{scale-invariant integrated local nonlinear-work toll}.
}
$$

---

# 20. Global shell nonlinear work

定義：

$$
\boxed{
W_q^\sigma(t)
=
-\int_{\mathbb R^3}
f(t,x)\cdot N(t,x)dx.
}
$$

shell energy balance：

$$
\boxed{
\frac12
\frac d{dt}
\|f\|_2^2
+
\nu
\|\nabla f\|_2^2
=
W_q^\sigma.
}
$$

注意：

$$
W_q^\sigma
$$

是 **nonlinear shell energy input**，

不是已扣 viscosity後的 total energy derivative。

---

# 21. Positive / negative spatial work variation

定義：

$$
\boxed{
W^+(t)
=
\int
[w(t,x)]_+
dx,
}
$$

$$
\boxed{
W^-(t)
=
\int
[-w(t,x)]_+
dx.
}
$$

則：

$$
\boxed{
W_q^\sigma
=
W^+-W^-.
}
$$

且：

$$
W^+(t)\ge L(t)
$$

for：

$$
t\in G.
$$

---

# 22. C4-D.5：Local-to-Global Work Cancellation Identity

對任意：

$$
t,
$$

$$
\boxed{
[W_q^\sigma(t)]_+
+
W^-(t)
\ge
W^+(t).
}
$$

因此在 good-source set：

$$
\boxed{
[W_q^\sigma]_+
+
W^-
\ge
L.
}
$$

時間積分：

$$
\boxed{
\int_G
[W_q^\sigma]_+dt
+
\int_G
W^-dt
\ge
c
\eta_0^3
\beta_0
\Delta\beta
\frac{
\nu^2
}{
\lambda
}.
}
$$

---

# 23. C4-D.6：Amplitude-to-Work Branching Bridge

定義 dimensionless：

$$
\boxed{
\mathfrak F_q
=
\frac{
\lambda
}{
\nu^2
}
\int_G
[W_q^\sigma(t)]_+
dt,
}
$$

$$
\boxed{
\mathfrak C_q^{sp}
=
\frac{
\lambda
}{
\nu^2
}
\int_G
W^-(t)dt.
}
$$

則每次 D-FAST crossing至少滿足：

## Source-overcapacity

$$
\boxed{
\frac1{
\nu\lambda
}
\int_B
\|N\|_\infty dt
\ge
\frac{
\Delta\beta
}{
2\eta_0
},
}
$$

或：

## Positive shell work

$$
\boxed{
\mathfrak F_q
\ge
c
\eta_0^3
\beta_0
\Delta\beta,
}
$$

或：

## Spatial work cancellation

$$
\boxed{
\mathfrak C_q^{sp}
\ge
c
\eta_0^3
\beta_0
\Delta\beta.
}
$$

這就是：

$$
\boxed{
\textbf{Amplitude-to-Work Branching Bridge}.
}
$$

---

# 24. C4-B synchronization consequence

所以 critical shell crossing現在被壓成：

$$
\boxed{
\text{UV persistence}
}
$$

或：

$$
\boxed{
\text{source-overcapacity}
}
$$

或：

$$
\boxed{
\text{positive nonlinear energy work}
}
$$

或：

$$
\boxed{
\text{spatial work cancellation}.
}
$$

它不能單純以：

$$
\boxed{
\text{zero-duty amplitude pulse with no other debt}
}
$$

逃逸。

這是真正超越 C4-B generic pulse no-go的 N–S-specific result。

---

# 25. Spatial work-cancellation geometry

在 good-source times：

$$
w\ge cMg
$$

於：

$$
B_t.
$$

若 global work被大量抵消，

則必有：

$$
W^-
$$

comparable。

又：

$$
|w|
\le
M
\|N\|_\infty
\le
\frac{
Mg
}{
\eta_0
}
$$

在 whole space只對 $|f|\le M$ 成立。

因此若某一時刻：

$$
W^-
\ge
c
\eta_0^3
Mg\lambda^{-3},
$$

negative-work set：

$$
\Omega_-
=
\{w<0\}
$$

必滿足：

$$
\boxed{
|\Omega_-|
\ge
c
\eta_0^4
\lambda^{-3}.
}
$$

所以 strong spatial work cancellation需要另一個 shell-volume級的 opposite-work region。

本文稱：

$$
\boxed{
\textbf{Work-Dipole / Work-Multiplicity Debt}.
}
$$

---

# 26. Positive shell work的 triad decomposition

現在只處理：

$$
\mathfrak F_q
$$

branch。

在 finite Galerkin truncation，

shell nonlinear work可分成 triad contributions：

$$
\boxed{
W_q^\sigma
=
\sum_{\tau\ni(q,\sigma)}
w_{\tau\to q,\sigma}.
}
$$

定義 positive variation：

$$
\boxed{
G_q^+
=
\sum_\tau
[w_{\tau\to q,\sigma}]_+.
}
$$

則：

$$
\boxed{
G_q^+
\ge
[W_q^\sigma]_+.
}
$$

時間積分後：

$$
\boxed{
\int_G
G_q^+dt
\ge
\int_G
[W_q^\sigma]_+dt.
}
$$

---

# 27. Rank split

C4-C 的 strongest helical table假設 receiving mode是 triad最高 wavenumber。

所以定義：

$$
\boxed{
G_q^+
=
G_{\rm top}^+
+
G_{\rm nontop}^+.
}
$$

其中：

## Top-rank

receiving：

$$
q
$$

是 triad highest wavenumber。

## Non-top

triad中存在：

$$
r>q
$$

的 participating mode。

---

# 28. Rank-defect branch

如果：

$$
G_{\rm nontop}^+
$$

佔主要 positive shell work，

則：

$$
\boxed{
\text{the amplitude-crossing shell is being fed by interactions
already involving still-higher absolute frequencies}.
}
$$

這不一定表示 higher mode itself critical-active，

但它表示：

$$
\boxed{
\textbf{higher-frequency participation cannot be removed from provenance}.
}
$$

本文稱：

$$
\boxed{
\textbf{Rank-Defect / Higher-Frequency-Participation Branch}.
}
$$

---

# 29. Top-rank helical split

對：

$$
G_{\rm top}^+,
$$

再分：

$$
\boxed{
G_{\rm top}^+
=
G_{\rm hom}^+
+
G_{\rm deg}^+
+
G_{\rm rob}^+.
}
$$

其中：

- hom = homochiral Class I；
- deg = II/III radial-gap degenerate；
- rob = robust heterochiral II/III/IV。

---

# 30. Robust heterochiral coefficient

對：

$$
\tau\in\mathrm{rob},
$$

C4-C已證存在：

$$
c_\ast=c(c_L,\delta)>0
$$

使：

$$
\boxed{
\mathcal R_\tau
=
\kappa_\tau
q_\tau
\dot e_{q_\tau},
}
$$

其中：

$$
\boxed{
c_\ast
\le
\kappa_\tau
\le
1.
}
$$

重要：

此 identity對：

$$
\dot e_q>0
$$

與：

$$
\dot e_q<0
$$

都成立，

因：

$$
\mathcal R_\tau
$$

與最高模態 nonlinear energy derivative具有相同 sign。

---

# 31. C4-D.7：Helical Cancellation Forces High-Mode Work Cancellation

對 robust heterochiral top-rank pool定義：

$$
\boxed{
X_+
=
\sum_{\tau\in rob}
[q_\tau\dot e_{q_\tau}]_+,
}
$$

$$
\boxed{
X_-
=
\sum_{\tau\in rob}
[-q_\tau\dot e_{q_\tau}]_+.
}
$$

critical helical variations：

$$
P_+
=
\sum_{\tau\in rob}
[\mathcal R_\tau]_+,
$$

$$
P_-
=
\sum_{\tau\in rob}
[-\mathcal R_\tau]_+.
$$

則：

$$
\boxed{
c_\ast X_+
\le
P_+
\le
X_+,
}
$$

以及：

$$
\boxed{
c_\ast X_-
\le
P_-
\le
X_-.
}
$$

若：

$$
\boxed{
P_+-P_-
\le
\eta
c_\ast
X_+
}
$$

for：

$$
0<\eta<1,
$$

則：

$$
P_-
\ge
(1-\eta)c_\ast X_+.
$$

而：

$$
P_-\le X_-.
$$

所以：

$$
\boxed{
X_-
\ge
(1-\eta)c_\ast X_+.
}
$$

### 結論

$$
\boxed{
\textbf{robust helical cancellation}
\Rightarrow
\textbf{comparable negative highest-mode energy work}.
}
$$

helical cancellation不是一個完全獨立的新 escape。

它必回到 high-mode work cancellation。

---

# 32. 這比 C4-C 更強

C4-C只有：

$$
\boxed{
P_+
\text{ large}
\Rightarrow
\text{net helicity}
\vee
P_-\text{ cancellation}.
}
$$

C4-D現在把第二支再壓成：

$$
\boxed{
P_-\text{ cancellation}
\Rightarrow
X_-\text{ high-mode back-transfer}.
}
$$

所以 robust sector裡：

$$
\boxed{
\text{helical cancellation}
}
$$

其實只是：

$$
\boxed{
\textbf{energy-work cancellation的 critical-weighted影像}.
}
$$

---

# 33. Positive shell work → helical branching edge

若 positive shell-work branch：

$$
\mathfrak F_q
\ge
F_0,
$$

且在 integrated positive triad variation中：

1. non-top fraction不是 dominant；
2. homochiral fraction不是 dominant；
3. radial-degenerate fraction不是 dominant；

則 robust heterochiral top-rank：

$$
X_+
$$

有 fixed fraction lower bound。

此時至少：

## D-HNET

$$
\boxed{
\text{net positive critical helical production}
}
$$

或：

## D-HCANCEL

$$
\boxed{
\text{comparable negative high-mode work variation}.
}
$$

所以 shell positive work不能在 robust heterochiral sector裡靠「純 helical cancellation」無成本消失。

---

# 34. Full amplitude-crossing branch tree

一個：

$$
\beta_0\to\beta_1
$$

critical shell first crossing現在必進：

---

## Branch A — Viscous persistence

$$
\boxed{
a_q^\sigma(t)\ge\beta_0
}
$$

through one full preceding viscous window。

---

## Branch B — Nonlinear source overcapacity

$$
\boxed{
\frac1{\nu\lambda}
\int
\|N_q^\sigma\|_\infty dt
\gtrsim
1.
}
$$

---

## Branch C — Spatial work cancellation

$$
\boxed{
\frac\lambda{\nu^2}
\int
W_q^-dt
\gtrsim
1.
}
$$

並伴隨 opposite-work region / work multiplicity。

---

## Branch D — Rank defect

positive shell input主要由仍更高 absolute frequency参与的 triads承擔。

---

## Branch E — Homochiral top-rank gain

pair-production silent / sign-definite-helicity-like transfer structure。

---

## Branch F — Radial-gap degeneration

heterochiral II/III coupling係數趨小。

---

## Branch G — Robust heterochiral net production

$$
\boxed{
\text{positive critical helical production}
}
$$

同步。

---

## Branch H — Robust work cancellation

helical negative cancellation強迫 comparable negative high-mode nonlinear work。

---

# 35. C4-D.8：Amplitude-to-Flux Barrier — Partial Closure

所以 C4-C 的：

$$
\boxed{
\text{Amplitude-to-Flux Barrier}
}
$$

現在狀態是：

## Direct implication

$$
\boxed{
\text{amplitude crossing}
\Rightarrow
\text{positive flux}
}
$$

仍：

$$
\boxed{
\mathrm{FALSE}.
}
$$

## Branching implication

$$
\boxed{
\text{amplitude crossing}
\Rightarrow
\text{finite structured branch set}
}
$$

現在：

$$
\boxed{
\mathrm{PROVED}.
}
$$

這是本輪最主要 closure。

---

# 36. C4-B pulse-capacity的修正

C4-B說 integrated critical toll可由 narrow high pulse支付。

C4-D現在證：

對 UV amplitude first crossing，

即使它走 pulse route，

也不能只有「pulse」這一個描述。

它必支付：

$$
\boxed{
\text{source impulse}
\vee
\text{critical nonlinear work}
\vee
\text{work cancellation}.
}
$$

所以：

$$
\boxed{
\textbf{UV pulse capacity has an N--S-specific structured payload}.
}
$$

---

# 37. 但 new carrier relay仍可存在

每代：

$$
q_n\uparrow\infty
$$

都可選不同 branch：

- 第 $n$ 代 source overcapacity；
- 第 $n+1$ 代 homochiral；
- 再下一代 rank defect；

等等。

所以 C4-D仍沒有 global contradiction。

但 branch set已變成有限且 typed，

因此 C4可重新使用：

$$
\boxed{
\text{finite recurrent branch reduction}.
}
$$

---

# 38. C4-D.9：Recurrent Escape-Branch Reduction

若 infinite critical crossings存在，

且每次都落在 finite branch family：

$$
\mathcal B
=
\{A,B,C,D,E,F,G,H\},
$$

則存在：

$$
\boxed{
B_\ast\in\mathcal B
}
$$

在 infinite subsequence反覆出現。

因此後續 C4不必同時處理所有 crossing escape。

可逐一 attack：

$$
\boxed{
\textbf{one recurrent amplitude-crossing escape mode}.
}
$$

---

# 39. 哪些 branch已有舊 rigidity？

## A — Persistence

回 C4-A synchronization。

## B — Source overcapacity

尚缺 critical source-capacity budget。

## C / H — Work cancellation

可合併研究 total nonlinear-work variation / work-dipole geometry。

## D — Rank defect

接 C1/C3-G absolute-frequency ancestry與 carrier relay。

## E — Homochiral

接 Biferale–Titi / heterochiral leakage。

## F — Radial degeneration

接 C3-C/D radial congestion。

## G — Positive helical production

接 C3-A/B critical pair-production divergence。

所以：

$$
\boxed{
\text{C4-D branch family大部分已有 C3 dependence graph}.
}
$$

---

# 40. Source-overcapacity scaling

normalized source impulse：

$$
\boxed{
\mathfrak S_q
=
\frac1{
\nu\lambda
}
\int
\|N_q^\sigma\|_\infty dt.
}
$$

在 viscous crossing：

$$
|I|
\sim
(\nu\lambda^2)^{-1},
$$

critical-size nonlinear source：

$$
\|N_q\|_\infty
\sim
\nu^2\lambda^3
$$

正好給：

$$
\mathfrak S_q
\sim1.
$$

所以 source-overcapacity branch是 scale-critical，

不能由 ordinary energy直接排除。

---

# 41. Work-cancellation scaling

critical nonlinear shell work rate：

$$
W_q
\sim
\nu^3\lambda.
$$

over viscous time：

$$
(\nu\lambda^2)^{-1}
$$

integrated ordinary energy work：

$$
\sim
\nu^2\lambda^{-1}.
$$

critical weighting：

$$
\lambda
$$

後：

$$
\sim
\nu^2.
$$

所以：

$$
\boxed{
\mathfrak C_q^{sp}\sim O(1)
}
$$

同樣是 scale-critical variation。

這再次解釋為何 generic finite energy budget不會關掉它。

---

# 42. Homochiral branch caveat

Biferale–Titi regularity theorem作用於：

$$
\boxed{
\text{full evolution projected到單 helicity-sign subspace}.
}
$$

C4-D Branch E只表示：

$$
\boxed{
\text{selected positive high-mode gain主要由 homochiral triads承擔}.
}
$$

它不表示 full N–S evolution已經 helical-decimated。

所以不能直接套：

$$
\boxed{
\text{homochiral gain}
\Rightarrow
\text{regular}.
}
$$

真正需要控制：

$$
\boxed{
\text{heterochiral leakage}.
}
$$

---

# 43. Rank-defect caveat

non-top positive shell gain只證：

$$
\boxed{
\text{still-higher absolute frequencies participate}.
}
$$

它不證：

$$
\boxed{
\text{those higher modes are already critical-active}.
}
$$

所以 D branch要接：

- source amplitude；
- parent criticality；
- shell occupancy；

才可形成 ancestry contradiction。

---

# 44. Radial degeneration caveat

II/III coupling可以因：

$$
\frac{q-p}{q}\to0
$$

或：

$$
\frac{q-k}{q}\to0
$$

逃。

此 branch不是 phase cancellation，

而是：

$$
\boxed{
\text{kinematic helical coupling coefficient itself collapse}.
}
$$

所以必須用 C3-C/D 的 radial congestion，

不能用 helical total variation處理。

---

# 45. X-Integration guards 更新

## G-HCROSS

crossing先分 persistence / fast。

## G-MAXSRC

fast amplitude growth需保存 maximizing-point nonlinear source projection。

## G-SEFF

保存：

$$
\eta
=
\frac{
-e\cdot N(x_{\max})
}{
\|N\|_\infty
}.
$$

## G-LWORK

good efficiency產生 local positive-work ball。

## G-WCANCEL

local positive work若沒有變成 net shell input，

missing amount進 spatial negative-work debt。

## G-RANK

shell gain進 helical table前必保存 receiving mode rank。

## G-HCWORK

robust helical cancellation必保存 corresponding negative high-mode work。

## G-BRANCH

Amplitude-to-Flux只允許 branching bridge，

不得重新升格成 direct implication。

---

# 46. True ETN 更新

Amplitude crossing state：

$$
\boxed{
\Theta_q^{cross}
=
\left\langle
\beta_0,\beta_1,
I_\lambda,
M',
N,
\eta,
L_{\rm local},
W_q,
W^-,
\operatorname{Rank},
\operatorname{HelClass},
\operatorname{RadialGap}
\right\rangle.
}
$$

transition：

$$
\boxed{
\text{Crossing}
\to
\text{Persistence}
\vee
\text{Source}
\vee
\text{WorkCancellation}
\vee
\text{RankDefect}
\vee
\text{Homochiral}
\vee
\text{RadialDegeneration}
\vee
\text{HelicalNet}
\vee
\text{RobustBackTransfer}.
}
$$

---

# 47. Strategic consequence

C4-C 的核心 barrier原本是：

$$
\boxed{
\text{amplitude不是 flux}.
}
$$

C4-D沒有否定這句。

而是證：

$$
\boxed{
\text{amplitude crossing不是任意的非-flux event}.
}
$$

在 N–S shell evolution上，

它要嘛：

- 已經 persistent；
- 要嘛 nonlinear source過量；
- 要嘛產生 critical local energy work；
- 若 work被隱藏，就必有 cancellation；
- 若 work真向 UV shell輸入，helical structure再把它壓成有限 branch family。

所以 hereditary amplitude ancestry第一次真正接到：

$$
\boxed{
\text{energy-work / helical closure graph}.
}
$$

---

# 48. 新 frontier：C4-E

現在最值得做的不是再攻 direct flux implication。

Amplitude crossing剩餘 finite branch family：

$$
\boxed{
\text{Source Overcapacity}
\vee
\text{Work Cancellation}
\vee
\text{Rank Defect}
\vee
\text{Homochiral}
\vee
\text{Radial Degeneration}
\vee
\text{Helical Net Production}.
}
$$

因此正式下一題：

$$
\boxed{
\textbf{C4-E — Recurrent Escape-Branch Rigidity and UV Closure Graph}.
}
$$

---

# 49. C4-E proof obligations

## E1 — Recurrent source-overcapacity

若：

$$
\mathfrak S_{q_n}\gtrsim1
$$

infinitely often，

能否轉成：

- critical operator debt；
- higher derivative toll；
- source active-volume packing？

## E2 — Recurrent work cancellation

若：

$$
\mathfrak C_{q_n}^{sp}\gtrsim1
$$

infinitely often，

研究：

- work-sign active volume；
- work-dipole separation；
- total work variation；
- pressure / phase transport。

## E3 — Rank-defect chain

若 shell crossing反覆由 still-higher modes供能，

證是否形成：

$$
\boxed{
\text{strictly faster absolute-frequency ancestry}
}
$$

或 pre-existing UV congestion。

## E4 — Homochiral dominance

若 positive work反覆 homochiral-dominated，

量化 heterochiral leakage：

$$
\varepsilon_{het,n}.
$$

若 leakage趨零，

比較 helical-decimated regular dynamics；

若不趨零，

回 heterochiral branch。

## E5 — Radial-gap degeneration

反覆：

$$
\delta_n\to0
$$

時，

接 C3-C/D radial congestion，

研究 required triad multiplicity。

## E6 — Helical net production

若：

$$
\mathcal R_+
$$

反覆同步 crossing，

現在 UV / helical channels完成真正 shared-event synchronization。

再與：

- strain；
- operator；

尋找下一 edge。

## E7 — Branch transition graph

建立：

$$
B_i
\to
B_j
$$

的 possible / forbidden transitions。

## E8 — C4 UV closure audit

判定 amplitude hereditary chain是否已被壓成：

$$
\boxed{
\text{finite recurrent structural motifs}
}
$$

足以進更強的 compactness / contradiction階段。

---

# 50. 正式狀態

$$
\boxed{
\begin{aligned}
\text{persistence-or-fast-crossing dichotomy}
&:\ \mathrm{PROVED},\\
\text{positive amplitude variation}\Rightarrow\text{positive nonlinear source at max}
&:\ \mathrm{PROVED},\\
\text{band-limited local positive-work ball}
&:\ \mathrm{PROVED},\\
\text{integrated critical local-work toll}
&:\ \mathrm{PROVED},\\
\text{source-overcapacity impulse branch}
&:\ \mathrm{PROVED},\\
\text{local-to-global work cancellation branch}
&:\ \mathrm{PROVED},\\
\text{Amplitude-to-Work branching bridge}
&:\ \mathrm{PROVED},\\
\text{direct amplitude}\Rightarrow\text{positive flux}
&:\ \mathrm{FALSE},\\
\text{positive shell work}\Rightarrow\text{positive triad variation}
&:\ \mathrm{PROVED},\\
\text{rank-defect branch}
&:\ \mathrm{DEFINED/EXACT\ PROVENANCE},\\
\text{robust heterochiral }\mathcal R=\kappa q\dot e_q
&:\ \mathrm{PROVED},\\
\text{helical cancellation}\Rightarrow\text{high-mode work cancellation}
&:\ \mathrm{PROVED},\\
\text{full amplitude crossing finite branch reduction}
&:\ \mathrm{PROVED},\\
\text{global regularity}
&:\ \mathrm{OPEN}.
\end{aligned}
}
$$

---

# 51. 結論

C4-C留下：

$$
\boxed{
\text{Amplitude-to-Flux Barrier}.
}
$$

C4-D現在把它改寫成真正 N–S-specific theorem：

對 critical shell crossing：

$$
\beta_0
\to
\beta_1,
$$

先有：

$$
\boxed{
\text{full viscous-window persistence}
\vee
\text{fast crossing}.
}
$$

fast crossing中，

最大點的 viscosity無法正向增加 amplitude，

因此 positive amplitude variation必由 nonlinear source提供：

$$
\boxed{
-e\cdot N
\ge
M'.
}
$$

band-limit再把 pointwise source擴成 shell-scale local positive-work ball。

因此整個 crossing必支付：

$$
\boxed{
\text{source overcapacity}
\vee
\text{positive nonlinear shell work}
\vee
\text{spatial work cancellation}.
}
$$

這就是：

$$
\boxed{
\textbf{Amplitude-to-Work Branching Bridge}.
}
$$

如果進 positive shell-work branch，

再經 triad rank / helical class decomposition：

$$
\boxed{
\text{rank defect}
\vee
\text{homochiral}
\vee
\text{radial degeneration}
\vee
\text{robust heterochiral}.
}
$$

而 robust heterochiral中：

$$
\boxed{
\mathcal R_\tau
=
\kappa_\tau
q_\tau\dot e_{q_\tau},
\qquad
c_\ast\le\kappa_\tau\le1.
}
$$

所以 helical cancellation若發生，

必同步產生 comparable negative highest-mode work：

$$
\boxed{
\text{helical cancellation}
\Rightarrow
\text{high-mode back-transfer}.
}
$$

因此「helicity正負互相抵掉」不再是一個完全獨立的隱藏通道。

C4 現在第一次真正把：

$$
\boxed{
\text{hereditary UV amplitude crossing}
}
$$

接到了：

$$
\boxed{
\text{energy-work / helical shared-event closure graph}.
}
$$

下一輪：

$$
\boxed{
\textbf{C4-E — Recurrent Escape-Branch Rigidity and UV Closure Graph}.
}
$$

---

# References

1. F. Waleffe, *The nature of triad interactions in homogeneous turbulence*, Physics of Fluids A 4 (1992), 350–363, DOI: 10.1063/1.858309.
2. A. Cheskidov, M. Dai, *Regularity criteria for the 3D Navier–Stokes and MHD equations*, arXiv:1507.06611.
3. A. Cheskidov, R. Shvydkoy, *On the regularity of weak solutions of the 3D Navier–Stokes equations in \(B^{-1}_{\infty,\infty}\)*, arXiv:0708.3067.
4. Z. Lei, F.-H. Lin, Y. Zhou, *Structure of Helicity and Global Solutions of Incompressible Navier–Stokes Equation*, arXiv:1505.00142.
5. L. Biferale, E. S. Titi, *On the Global Regularity of a Helical-decimated Version of the 3D Navier–Stokes Equations*, arXiv:1303.1215.

# Internal dependencies

- `NS_C4C_SharedEventCoupling_AmplitudeFluxBarrier_v0.1.md`
- `NS_C4B_TemporalSynchronization_CarrierRelayNoGo_v0.1.md`
- `NS_C4A_UnifiedSurvivorState_SynchronizationClosure_v0.1.md`
- `NS_C3G_FirstCrossing_CausalAncestry_DepletionNoGo_v0.1.md`
- `NS_C3E_ViscousWindow_PhaseEfficiency_Zeno_v0.1.md`
- `NS_C3D_CutoffFlux_HelicalKernel_Nonlocality_v0.1.md`
- `NS_C3C_ClassII_Nonlocality_Tax_Radial_Congestion_v0.1.md`
- `NS_C3B_BiHelical_Equalization_UniqueSign_UV_Escape_v0.1.md`
- `NS_C3K_AbsoluteOccupancy_OneMomentGap_v0.1.md`
- `True ETN / 無限維張力場`
- `X_Integral_Unified_Program_v0.2.md`

Next:

$$
\boxed{
\textbf{C4-E — Recurrent Escape-Branch Rigidity and UV Closure Graph}
}
$$
