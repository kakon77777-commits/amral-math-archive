---
title: "Navier–Stokes C5-E：Strain-Direction Defect Measures、Middle-Gap Degeneration 與 Derivative-Intermittency Closure"
subtitle: "From Quadratic Cancellation to Middle-Gap Concentration, Strain/Vorticity Leakage, Cubic Active-Volume Intermittency, and the Remaining Grujić–Xu Interface"
version: "v0.1"
date: "2026-08-15"
author: "Neo.K / EveMissLab"
language: "zh-TW"
status: "Theorem-style spatial defect-measure reduction / intermittency interface"
epistemic_status: "Exact trace-free eigenvalue algebra + Q-weighted defect measures + Poincaré fluctuation routing + effective-volume intermittency lemmas + conditional interface to published derivative-sparseness regularity criteria. Does NOT prove Navier–Stokes regularity."
---

# Navier–Stokes C5-E
# Strain-Direction Defect Measures、Middle-Gap Degeneration 與 Derivative-Intermittency Closure

## 0. 本輪定位

C5-D 得到 C5 第一個 finite-dimensional recurrent-limit incompatibility：

$$
\boxed{
\text{Strong-Middle Pointwise Cone}
\cap
\text{Seven-Point Zero-Barycenter Cancellation}
=
\varnothing.
}
$$

因此 recurrent quadratic-cancellation motif：

$$
Q
$$

若要繼續存在，只能逃向：

$$
\boxed{
\text{Middle-Gap Degeneration}
\vee
\text{Strain-Direction Dispersion}.
}
$$

C5-E 的任務不是把這兩個名字保留下來，

而是問：

> 它們實際上代表哪一種 measurable / derivative / intermittency debt？

本輪主要結果：

1. normalized middle-gap variable：
   $$
   \vartheta(S)
   =
   \frac{
   \lambda_2^+(S)\lambda_3(S)
   }{
   |S|^2
   }
   $$
   與：
   $$
   \lambda_2^+(S)/|S|
   $$
   quantitatively equivalent；
2. 若：
   $$
   \vartheta\ge\delta>0,
   $$
   則 pointwise：
   $$
   \boxed{
   |Q|
   \gtrsim
   \delta
   (
   |S|^2+|\omega|^2
   );
   }
   $$
3. 因此 Q-weighted middle-gap concentration是真正 physical quadratic activity concentration，
   不是 matrix-normalization artefact；
4. 建立：
   $$
   \boxed{
   \text{Q-weighted strain-direction/middle-gap defect measure};
   }
   $$
5. zero quadratic barycenter若 limit沒有 middle-gap mass，
   則 strain-direction marginal不可能收斂到單一 strong-middle direction；
6. quantitative Q-cancellation forcing fixed cone leakage；
7. cone leakage再 exact分成：
   $$
   \boxed{
   \text{strain-carrying directional leakage}
   \vee
   \text{vorticity-dominant leakage};
   }
   $$
8. strain-carrying leakage利用 weighted Poincaré給：
   $$
   \boxed{
   \text{higher-derivative strain fluctuation stock};
   }
   $$
9. vorticity-dominant leakage給：
   $$
   \boxed{
   \text{local critical vorticity/enstrophy stock};
   }
   $$
10. middle-gap degeneration若承擔 fixed fraction middle amplification，
    必使：
    $$
    \boxed{
    \|S\|_3^3
    \gtrsim
    \delta^{-1}
    \times
    \text{middle load};
    }
    $$
11. large cubic strain相對 $L^2$ stock產生：
    $$
    \boxed{
    \text{small effective active volume};
    }
    $$
12. 一個 explicit effective-amplitude superlevel set可同時：
    - 承載 fixed fraction cubic activity；
    - 具有 small volume；
13. 因此 middle-gap route被轉成真正 spatial intermittency；
14. 但 published Grujić–Xu theorem仍要求：
    - $D^ku$ 或 $D^k\omega$ component/sign superlevel sparseness；
    - escape/later analytic time；
    - derivative-chain hypotheses；
15. strain amplitude / $\nabla S$ intermittency目前不能直接偷換成該 theorem hypotheses；
16. 因此 C5-E 得到的是：
    $$
    \boxed{
    \textbf{Derivative-Intermittency Pre-Gate},
    }
    $$
    不是 full regularity gate；
17. C5-D 的 free Q-cancellation motif至此被消除：
    $$
    \boxed{
    Q
    \Rightarrow
    \text{Gap Concentration}
    \vee
    \text{Derivative Fluctuation}
    \vee
    \text{Vorticity Leakage}.
    }
    $$

---

# 1. Fresh primary-source audit

## 1.1 Miller — middle eigenvalue

Miller 的 middle-eigenvalue work把：

$$
\lambda_2^+
$$

確立為 scale-critical regularity channel。

因此 C5-E 對 normalized：

$$
\lambda_2^+/|S|
$$

的 degeneration並非任意 eigenvalue statistic；

它是 middle-strain regularity geometry中的 shape degeneration。

## 1.2 Grujić–Xu 2024 journal version

正式 version of record：

$$
\boxed{
\text{J. Math. Fluid Mech. 26, Article 53 (2024)}.
}
$$

其框架以：

$$
\boxed{
\text{higher derivative component/sign superlevel-set sparseness}
}
$$

為核心。

Theorem 3.5 是 fixed derivative direct geometric regularity criterion。

Theorem 3.7 給 energy-level a-priori volumetric sparseness。

Theorem 3.14 使用：

- higher-order derivative chains；
- spatial analyticity；
- component/sign superlevel sets；

得到 asymptotically critical regularity route。

### C5-E guard

本文不把：

$$
S,
\quad
\nabla S
$$

的 magnitude geometry直接當成：

$$
D^ku
$$

component/sign theorem hypothesis。

---

# 2. Positive-middle normalized shape

對：

$$
S\in\operatorname{Sym}_0(3),
\qquad
S\ne0,
$$

ordered eigenvalues：

$$
\lambda_1\le\lambda_2\le\lambda_3.
$$

定義：

$$
\boxed{
\xi_2(S)
=
\frac{
\lambda_2^+(S)
}{
|S|_F
}.
}
$$

以及 C5-D shape variable：

$$
\boxed{
\vartheta(S)
=
\frac{
\lambda_2^+(S)\lambda_3(S)
}{
|S|_F^2
}.
}
$$

若：

$$
\lambda_2\le0,
$$

令：

$$
\vartheta=0.
$$

---

# 3. C5-E.1：Middle-Gap Equivalence

若：

$$
\lambda_2>0,
$$

normalized eigenvalues滿足：

$$
\boxed{
\frac1{\sqrt6}
\le
\frac{\lambda_3}{|S|}
\le
\frac1{\sqrt2}.
}
$$

所以：

$$
\boxed{
\frac1{\sqrt6}
\xi_2
\le
\vartheta
\le
\frac1{\sqrt2}
\xi_2.
}
$$

等價：

$$
\boxed{
\sqrt2\,\vartheta
\le
\xi_2
\le
\sqrt6\,\vartheta.
}
$$

### 結論

$$
\boxed{
\vartheta\to0
\quad\Longleftrightarrow\quad
\lambda_2^+/|S|\to0
}
$$

within the positive-middle sector。

所以：

$$
\boxed{
\textbf{Middle-Gap Degeneration}
}
$$

就是 normalized middle eigenvalue真正退化。

---

# 4. Pointwise quadratic coercivity away from the middle gap

C5-D 對每一個 normalized positive-middle direction：

$$
K=S/|S|
$$

構造：

$$
H_K
$$

並證：

$$
H_K:Q
\ge
\frac{
\vartheta(S)
}{
4
}
(
|S|^2+|\omega|^2
).
$$

又：

$$
|H_K|_F
$$

在 normalized trace-free sphere上 uniformly bounded。

因此存在 universal：

$$
c_Q>0
$$

使：

## C5-E.2

若：

$$
\boxed{
\vartheta(S)\ge\delta>0,
}
$$

則：

$$
\boxed{
|Q(S,\omega)|
\ge
c_Q
\delta
(
|S|^2+|\omega|^2
).
}
$$

另一方面：

$$
\boxed{
|Q|
\le
|S|^2
+
\frac{\sqrt2}{4}
|\omega|^2
\le
|S|^2+|\omega|^2.
}
$$

所以在：

$$
\vartheta\ge\delta
$$

region：

$$
\boxed{
|Q|
\asymp_\delta
|S|^2+|\omega|^2.
}
$$

---

# 5. Meaning

如果 Q-weighted mass集中在：

$$
\vartheta\to0,
$$

那是在把真正：

$$
|S|^2+|\omega|^2
$$

quadratic activity推向 middle-degenerate boundary。

它不是因：

$$
Q/|Q|
$$

normalization造成的假 defect。

---

# 6. Q-weighted spatial probability measure

取 selected adjoint/local core cutoff：

$$
\chi_j\ge0.
$$

定義：

$$
\boxed{
A_j^Q
=
\int
\chi_j|Q_j|dx.
}
$$

在 active Q motif：

$$
A_j^Q>0.
$$

定義：

$$
\boxed{
d\nu_j^Q(x)
=
\frac{
\chi_j(x)|Q_j(x)|
}{
A_j^Q
}
dx.
}
$$

所以：

$$
\boxed{
\nu_j^Q
}
$$

是 probability measure。

---

# 7. Joint strain-direction / gap state

若：

$$
S_j(x)\ne0,
$$

定義：

$$
\boxed{
V_j(x)
=
\frac{
S_j(x)
}{
|S_j(x)|
}
\in
S^4
\subset
\operatorname{Sym}_0(3).
}
$$

若：

$$
S_j=0,
$$

加入 cemetery：

$$
\partial_S.
$$

定義：

$$
\boxed{
\theta_j(x)
=
\vartheta(S_j(x))
\in
\left[
0,\frac16
\right].
}
$$

push-forward：

$$
\boxed{
\Xi_j^{S\theta}
=
(V_j,\theta_j)_\#
\nu_j^Q.
}
$$

state space：

$$
\boxed{
\mathcal K_{S\theta}
=
(S^4\cup\{\partial_S\})
\times
[0,1/6]
}
$$

compact。

---

# 8. Middle-gap distribution function

定義：

$$
\boxed{
\mathfrak g_j(\delta)
=
\nu_j^Q
\{
\theta_j\le\delta
\}
}
$$

for：

$$
0<\delta<1/6.
$$

抽 subsequence：

$$
\Xi_j^{S\theta}
\rightharpoonup
\Xi_\ast^{S\theta}.
$$

define limit gap mass：

$$
\boxed{
\mathfrak g_\ast(\delta)
=
\Xi_\ast^{S\theta}
\{
\theta\le\delta
\}.
}
$$

---

# 9. Middle-gap defect mass

定義：

$$
\boxed{
\mathfrak G_\ast
=
\Xi_\ast^{S\theta}
\{
\theta=0
\}.
}
$$

equivalently：

$$
\boxed{
\mathfrak G_\ast
=
\lim_{\delta\downarrow0}
\mathfrak g_\ast(\delta).
}
$$

如果：

$$
\mathfrak G_\ast>0,
$$

稱：

$$
\boxed{
\textbf{Middle-Gap Defect Measure}
}
$$

active。

---

# 10. Quadratic-direction barycenter

另定義：

$$
\boxed{
U_j(x)
=
\frac{
Q_j(x)
}{
|Q_j(x)|
}
\in
S^5
}
$$

on：

$$
Q_j\ne0.
$$

則：

$$
\boxed{
\int
U_j
d\nu_j^Q
=
\frac{
B_j^Q
}{
A_j^Q
}.
}
$$

Seven-Point cancellation extreme branch：

$$
\boxed{
\left|
\int
U_jd\nu_j^Q
\right|
=
\kappa_j^Q
\to0.
}
$$

---

# 11. C5-E.3：Zero-Barycenter Limit Cannot Have a Single Strong-Middle Direction

假設：

$$
\boxed{
\kappa_j^Q\to0.
}
$$

若：

$$
\Xi_\ast^{S\theta}
=
\delta_{(K,\theta_K)}
$$

with：

$$
\boxed{
\theta_K>0,
}
$$

則不可能。

### 證明

取：

$$
0<\delta<\theta_K.
$$

由 weak concentration，

large $j$ 時幾乎全部 Q mass落在：

- $\theta\ge\delta$；
- $V$ sufficiently close to $K$。

C5-D strong-middle cone theorem因此給：

$$
\kappa_j^Q
\ge
\gamma_K/2
$$

for large $j$，

和：

$$
\kappa_j^Q\to0
$$

矛盾。$\square$

### 結論

zero quadratic barycenter若存活，

strain-direction/gap limit必：

$$
\boxed{
\text{hit }\theta=0
}
$$

或：

$$
\boxed{
\text{remain directionally nontrivial}.
}
$$

---

# 12. Uniform strong-middle subset

固定：

$$
\delta>0.
$$

定義：

$$
\boxed{
\mathcal S_\delta
=
\{
V\in S^4:
\vartheta(V)\ge\delta
\}.
}
$$

$\mathcal S_\delta$ compact。

C5-D cone radius與 half-space margin在此可取 uniform constants：

$$
\boxed{
r_\delta>0,
\qquad
\gamma_\delta>0.
}
$$

schematically：

$$
r_\delta\gtrsim\delta,
$$

$$
\gamma_\delta\gtrsim\delta.
$$

---

# 13. C5-E.4：Quantitative Direction Anti-Concentration

假設：

$$
\kappa_j^Q\le\kappa_0
<
\gamma_\delta.
$$

對任意：

$$
K\in\mathcal S_\delta,
$$

定義：

$$
B_{r_\delta}(K)
\subset S^4.
$$

若 middle-gap mass：

$$
\mathfrak g_j(\delta/2)
$$

已另行剔除，

C5-D cone-leakage theorem給：

$$
\boxed{
\nu_j^Q
\left(
\{
\theta\ge\delta/2
\}
\setminus
B_{r_\delta}(K)
\right)
\ge
c_\delta
-
\mathfrak g_j(\delta/2)
}
$$

for a constant：

$$
c_\delta>0.
$$

### 解讀

若 middle-gap mass很小，

Q cancellation就強迫：

$$
\boxed{
\text{strain-direction probability不能集中在任何單一 strong-middle cone}.
}
$$

---

# 14. Directional variance lower bound

同條件下，

若：

$$
\mathfrak g_j(\delta/2)
\le
c_\delta/2,
$$

則對任意：

$$
K\in\mathcal S_\delta,
$$

$$
\boxed{
\int
|V_j-K|^2
d\nu_j^Q
\ge
\frac{
c_\delta
}{2}
r_\delta^2.
}
$$

所以：

$$
\boxed{
\textbf{Q cancellation + no middle-gap defect}
\Rightarrow
\textbf{nondegenerate directional dispersion}.
}
$$

---

# 15. From direction leakage to physical PDE stock

要把 direction dispersion轉成 derivative stock，

不能直接把 Q-weight等同 strain-energy weight。

所以 C5-E 再做一次 exact split。

固定：

$$
0<\eta<1.
$$

定義：

$$
\boxed{
E_S(\eta)
=
\{
|S|^2
\ge
\eta|Q|
\},
}
$$

以及：

$$
\boxed{
E_\omega(\eta)
=
\{
|S|^2
<
\eta|Q|
\}.
}
$$

---

# 16. Vorticity dominance on $E_\omega$

因：

$$
|Q|
\le
|S|^2
+
c_\omega
|\omega|^2,
$$

其中：

$$
\boxed{
c_\omega
=
\frac{\sqrt2}{4},
}
$$

在：

$$
E_\omega(\eta)
$$

有：

$$
(1-\eta)|Q|
\le
c_\omega
|\omega|^2.
$$

所以：

$$
\boxed{
|\omega|^2
\ge
\frac{
1-\eta
}{
c_\omega
}
|Q|.
}
$$

---

# 17. Direction-to-ray distance

固定 unit：

$$
K\in S^4.
$$

若：

$$
|V-K|
\ge r,
$$

則存在：

$$
c_r>0
$$

使：

$$
\boxed{
\operatorname{dist}
(
V,
\{aK:a\ge0\}
)
\ge
c_r.
}
$$

例如對：

$$
0<r\le1,
$$

可取：

$$
\boxed{
c_r\ge r/2.
}
$$

因此若 local mean：

$$
\bar S=mK,
\qquad
m\ge0,
$$

則：

$$
\boxed{
|S-\bar S|
\ge
c_r|S|
}
$$

on：

$$
|S/|S|-K|\ge r.
$$

---

# 18. Standard weighted core Poincaré

取 standard radius-$R$ core cutoff：

$$
\chi_R,
$$

令：

$$
\boxed{
\bar S_{\chi}
=
\frac{
\int\chi_RS
}{
\int\chi_R
}.
}
$$

假設 standard weighted Poincaré constant：

$$
C_P
$$

使：

$$
\boxed{
\int
\chi_R
|S-\bar S_\chi|^2
\le
C_P
R^2
\int_{B_{CR}}
|\nabla S|^2.
}
$$

---

# 19. Leakage mass

假設某 cone center：

$$
K
=
\bar S_\chi/|\bar S_\chi|
$$

具有 nondegenerate strong-middle margin，

且 Q cancellation forcing：

$$
\boxed{
\int_{E_{\rm leak}}
\chi|Q|
\ge
\varepsilon_0
A_\chi^Q,
}
$$

where：

$$
E_{\rm leak}
=
\{
|S/|S|-K|
\ge r_0
\}.
$$

---

# 20. C5-E.5：Leakage → Derivative or Vorticity Dichotomy

將：

$$
E_{\rm leak}
$$

分：

$$
E_{\rm leak}\cap E_S(\eta)
$$

與：

$$
E_{\rm leak}\cap E_\omega(\eta).
$$

至少一支承擔：

$$
\varepsilon_0A_\chi^Q/2.
$$

---

## Branch E-DER

若：

$$
\int_{E_{\rm leak}\cap E_S(\eta)}
\chi|Q|
\ge
\frac{
\varepsilon_0
}{2}
A_\chi^Q,
$$

則：

$$
\int
\chi
|S-\bar S_\chi|^2
\ge
c_{r_0}^2
\eta
\frac{
\varepsilon_0
}{2}
A_\chi^Q.
$$

weighted Poincaré給：

$$
\boxed{
R^2
\int_{B_{CR}}
|\nabla S|^2
\ge
c
\eta
\varepsilon_0
A_\chi^Q.
}
$$

定義：

$$
\boxed{
\mathfrak H_R
=
\frac{
R^3
}{
\nu^2
}
\int_{B_{CR}}
|\nabla S|^2,
}
$$

$$
\boxed{
a_R^Q
=
\frac{
R
}{
\nu^2
}
A_\chi^Q.
}
$$

則：

$$
\boxed{
\mathfrak H_R
\ge
c
\eta
\varepsilon_0
a_R^Q.
}
$$

---

## Branch E-VORT

若：

$$
\int_{E_{\rm leak}\cap E_\omega(\eta)}
\chi|Q|
\ge
\frac{
\varepsilon_0
}{2}
A_\chi^Q,
$$

則由 §16：

$$
\boxed{
\int
\chi|\omega|^2
\ge
c_\eta
\varepsilon_0
A_\chi^Q.
}
$$

定義 local critical vorticity stock：

$$
\boxed{
\mathfrak W_R
=
\frac{
R
}{
\nu^2
}
\int
\chi|\omega|^2.
}
$$

則：

$$
\boxed{
\mathfrak W_R
\ge
c_\eta
\varepsilon_0
a_R^Q.
}
$$

---

# 21. C5-E.6：Q-Cancellation Spatial Debt Trichotomy

在 nondegenerate local Q-intensity：

$$
a_R^Q\ge a_0>0
$$

下，

recurrent small quadratic mean：

$$
\kappa_Q\ll1
$$

必至少走：

$$
\boxed{
\text{Middle-Gap Defect}
}
$$

或：

$$
\boxed{
\mathfrak H_R
\gtrsim1
}
$$

或：

$$
\boxed{
\mathfrak W_R
\gtrsim1.
}
$$

也就是：

$$
\boxed{
\textbf{Q Cancellation}
\Rightarrow
\textbf{Gap Concentration}
\vee
\textbf{Strain-Derivative Fluctuation}
\vee
\textbf{Vorticity-Dominant Leakage}.
}
$$

### 這是本輪第一個主要 compression。

---

# 22. Middle-gap degeneration is not a free escape

現在處理：

$$
\vartheta\le\delta.
$$

middle source density：

$$
\boxed{
\lambda_2^+|S|^2
=
\xi_2(S)|S|^3.
}
$$

由 C5-E.1：

$$
\xi_2
\le
\sqrt6\vartheta.
$$

所以在：

$$
\vartheta\le\delta,
$$

$$
\boxed{
\lambda_2^+|S|^2
\le
\sqrt6
\delta
|S|^3.
}
$$

---

# 23. C5-E.7：Middle-Gap Load Forces Cubic Strain

若 measurable set：

$$
G_\delta
=
\{
\vartheta\le\delta
\}
$$

承擔 middle load：

$$
\boxed{
M_{\delta}
=
\int_{G_\delta}
\lambda_2^+
|S|^2dx,
}
$$

則：

$$
\boxed{
\int_{G_\delta}
|S|^3dx
\ge
\frac{
M_\delta
}{
\sqrt6\,\delta
}.
}
$$

### 結論

如果：

$$
M_\delta
$$

不退化，

而：

$$
\delta\downarrow0,
$$

則：

$$
\boxed{
\|S\|_3^3
\to\infty
}
$$

at least at：

$$
\delta^{-1}
$$

rate。

---

# 24. Global derivative lower bound from cubic strain

whole-space Sobolev / interpolation：

$$
\boxed{
\|S\|_3
\le
C
\|S\|_2^{1/2}
\|\nabla S\|_2^{1/2}.
}
$$

所以：

$$
\boxed{
\|S\|_3^3
\le
C
\|S\|_2^{3/2}
\|\nabla S\|_2^{3/2}.
}
$$

結合 C5-E.7：

$$
\boxed{
\|\nabla S\|_2
\ge
c
\frac{
M_\delta^{2/3}
}{
\delta^{2/3}
\|S\|_2
}.
}
$$

### 意義

middle-gap degeneration若要維持 middle amplification，

也會直接推高：

$$
\boxed{
D^2u\text{-level }L^2\text{ stock}
}
$$

unless enstrophy itself compensates。

---

# 25. Effective cubic amplitude

對任意：

$$
f\in L^2\cap L^3,
\qquad
f\not\equiv0,
$$

定義：

$$
\boxed{
A_{\rm eff}(f)
=
\frac{
\|f\|_3^3
}{
\|f\|_2^2
}.
}
$$

因：

$$
\|f\|_3^3
\le
\|f\|_\infty
\|f\|_2^2,
$$

有：

$$
\boxed{
A_{\rm eff}(f)
\le
\|f\|_\infty.
}
$$

---

# 26. Effective active volume

定義：

$$
\boxed{
V_{\rm eff}(f)
=
\frac{
\|f\|_2^6
}{
\|f\|_3^6
}.
}
$$

dimension為 volume。

若：

$$
f
$$

roughly constant on a set of volume：

$$
V,
$$

則：

$$
V_{\rm eff}\sim V.
$$

---

# 27. C5-E.8：Effective Active-Set Lemma

固定：

$$
0<c<1.
$$

定義：

$$
\boxed{
E_c(f)
=
\{
x:
|f(x)|
\ge
cA_{\rm eff}(f)
\}.
}
$$

則：

## Volume bound

$$
\boxed{
|E_c(f)|
\le
c^{-2}
V_{\rm eff}(f).
}
$$

### 證明

Chebyshev：

$$
|E_c|
\le
\frac{
\|f\|_2^2
}{
c^2A_{\rm eff}^2
}
=
c^{-2}
\frac{
\|f\|_2^6
}{
\|f\|_3^6
}.
$$

## Cubic activity bound

$$
\boxed{
\int_{E_c(f)}
|f|^3dx
\ge
(1-c)
\|f\|_3^3.
}
$$

### 證明

在 complement：

$$
|f|<cA_{\rm eff}.
$$

所以：

$$
\int_{E_c^c}
|f|^3
\le
cA_{\rm eff}
\|f\|_2^2
=
c\|f\|_3^3.
$$

$\square$

---

# 28. Meaning

large：

$$
\|S\|_3^3/\|S\|_2^2
$$

不只是高 amplitude。

它保證存在一個：

$$
\boxed{
\text{small effective-volume set}
}
$$

承載至少：

$$
1-c
$$

比例的 cubic strain activity。

這是：

$$
\boxed{
\textbf{Strain-Amplitude Intermittency}.
}
$$

---

# 29. Normalized effective volume on an ancestry scale

取：

$$
R>0.
$$

定義：

$$
\boxed{
\phi_{S,3}(R)
=
\frac{
V_{\rm eff}(S)
}{
R^3
}.
}
$$

若 local middle-gap load normalized為：

$$
\boxed{
b_R^{mid}
=
\frac{
R^3
}{
\nu^3
}
M_\delta,
}
$$

而 global/local strain enstrophy stock：

$$
\boxed{
e_R^S
=
\frac{
R
}{
\nu^2
}
\|S\|_2^2,
}
$$

則 C5-E.7給：

$$
\|S\|_3^3
\ge
\frac{
\nu^3
}{
R^3
}
\frac{
b_R^{mid}
}{
\sqrt6\delta
}.
$$

所以：

$$
\boxed{
\phi_{S,3}(R)
\le
6
\delta^2
\frac{
(e_R^S)^3
}{
(b_R^{mid})^2
}.
}
$$

---

# 30. C5-E.9：Middle-Gap → Effective-Volume Collapse

若沿 subsequence：

$$
\boxed{
b_R^{mid}\ge b_0>0,
}
$$

且：

$$
\boxed{
e_R^S\le E_0<\infty,
}
$$

同時：

$$
\delta\to0,
$$

則：

$$
\boxed{
\phi_{S,3}(R)
\lesssim
\delta^2
\to0.
}
$$

### 結論

middle-gap degeneration若持續承擔 nondegenerate middle load，

在 bounded strain-stock regime中必轉成：

$$
\boxed{
\textbf{vanishing effective active volume}.
}
$$

若：

$$
e_R^S
$$

不 bounded，

則已進：

$$
\boxed{
\textbf{strain-enstrophy escape}.
}
$$

---

# 31. Volume-to-line sparseness pre-gate

C3-W pure geometric lemma：

若 set：

$$
A
$$

在：

$$
B_r(x_0)
$$

的 volume fraction：

$$
<\delta_{sp}^3,
$$

則存在 through：

$$
x_0
$$

的 line方向使 one-dimensional occupancy：

$$
\le\delta_{sp}.
$$

對 global effective set：

$$
E_c(S),
$$

因：

$$
|E_c(S)|
\le
c^{-2}
V_{\rm eff}(S),
$$

取：

$$
\boxed{
r_{sp}
\asymp
\delta_{sp}^{-1}
c^{-2/3}
V_{\rm eff}(S)^{1/3}.
}
$$

則：

$$
E_c(S)
$$

在任意 base point都有一個 line方向呈：

$$
\boxed{
1D\ \delta_{sp}\text{-sparseness}.
}
$$

---

# 32. Middle-gap sparseness scale

用 C5-E.9：

$$
\boxed{
\frac{
r_{sp}
}{
R
}
\lesssim
\delta^{2/3}
\frac{
e_R^S
}{
(b_R^{mid})^{2/3}
}
}
$$

up to fixed constants。

所以：

$$
\boxed{
\delta\downarrow0
}
$$

會把 strain cubic active set推到更細的 sparse scale，

除非：

$$
e_R^S
$$

同步膨脹。

---

# 33. Relation to fixed-fraction $L^\infty$ strain superlevel sets

因：

$$
A_{\rm eff}(S)
\le
\|S\|_\infty,
$$

若：

$$
0<c\le\lambda<1,
$$

則：

$$
\boxed{
\{
|S|
>
\lambda
\|S\|_\infty
\}
\subset
E_c(S).
}
$$

所以 E-c sparseness也適用於 fixed-fraction：

$$
|S|
$$

magnitude high set。

### 但：

published Grujić–Xu theorem追蹤的是：

$$
D^ku
$$

或：

$$
D^k\omega
$$

的 component/sign superlevel sets。

所以仍有 field-interface gap。

---

# 34. C5-E derivative-intermittency pre-gate

目前 C5-E 已能產生：

## From direction leakage

$$
\boxed{
\mathfrak H_R
=
\frac{
R^3
}{
\nu^2
}
\|\nabla S\|_2^2
\gtrsim1
}
$$

or：

$$
\boxed{
\mathfrak W_R
=
\frac{
R
}{
\nu^2
}
\|\omega\|_2^2
\gtrsim1.
}
$$

## From middle-gap degeneration

$$
\boxed{
\phi_{S,3}\ll1
}
$$

or：

$$
\boxed{
e_R^S\text{ large}.
}
$$

這些都是真正：

$$
\boxed{
\textbf{derivative / intermittency pre-gates}.
}
$$

---

# 35. Published Grujić–Xu gate

Theorem 3.5 的 antecedent：

在：

$$
D^ku
$$

或：

$$
D^k\omega
$$

escape time之後的適當 later time，

對任意 spatial point：

$$
x_0,
$$

存在 scale：

$$
\rho
$$

使 selected：

$$
\boxed{
\text{component/sign superlevel set}
}
$$

在該 scale上 1D sparse。

Theorem 3.14 更要求 derivative-chain / analytic-time structure，

並在：

$$
\|D^ku\|_\infty^{-1/(k+1)}
$$

scale上形成 asymptotically critical route。

---

# 36. C5-E.10：Derivative-Gate Interface

C5-E 所得 strain intermittency若要合法進 published theorem，

仍需：

## E-G1 — Field conversion

由：

$$
S
$$

或：

$$
\nabla S
$$

geometry轉成某：

$$
D^ku
$$

或：

$$
D^k\omega
$$

component/sign superlevel geometry。

## E-G2 — Threshold conversion

C5-E effective amplitude：

$$
A_{\rm eff}
$$

與 theorem的：

$$
\lambda
\|D^ku\|_\infty
$$

threshold要對齊。

## E-G3 — Uniform-local / global set

C5-E sparse set需真正控制 theorem所用 full-space component/sign superlevel set，

不能只控制 ancestry core內 subset。

## E-G4 — Time gate

geometry需出現在 theorem admissible later analytic time：

$$
s=s(t).
$$

## E-G5 — Chain gate

若使用 Theorem 3.14，

需 ascending/descending derivative-chain hypotheses。

### 狀態

$$
\boxed{
\mathrm{OPEN\ INTERFACE}.
}
$$

---

# 37. Why we do not silently identify strain with $D u$

雖然：

$$
S
=
\frac12
(
\nabla u+\nabla u^T
),
$$

pointwise：

$$
|S|
$$

large會強迫某些 linear derivative combinations large。

但 published theorem的 norm / component / sign reference是：

$$
D^\zeta u
$$

自身。

而：

$$
\nabla u
$$

還包含 antisymmetric vorticity part。

因此：

$$
\boxed{
\text{strain high-set sparse}
}
$$

不自動給：

$$
\boxed{
\text{all relevant raw derivative component/sign high-sets sparse}.
}
$$

這個 distinction必保留。

---

# 38. Vorticity leakage branch and theorem interface

C5-E.5 的 E-VORT給：

$$
\boxed{
\mathfrak W_R
\gtrsim1.
}
$$

但 vorticity $L^2$ stock同樣不是：

$$
\boxed{
\text{vorticity superlevel sparseness}.
}
$$

若後續能再證：

- vorticity active volume shrinkage；
- fixed-fraction vorticity high-set geometry；

則可直接對接 Grujić–Xu 的 vorticity版 Theorem 3.5 / 3.14。

目前仍：

$$
\boxed{
\mathrm{OPEN}.
}
$$

---

# 39. C5-E limit taxonomy

對 recurrent Q-cancellation limit，

現在只有：

## E-L1 — Middle-gap defect

$$
\boxed{
\mathfrak G_\ast>0.
}
$$

## E-L2 — Direction-dispersion defect

strong-middle mass不退化，

但 strain direction measure無法集中於單 cone。

## E-L3 — Strain-derivative fluctuation

$$
\boxed{
\mathfrak H_R
\gtrsim1.
}
$$

## E-L4 — Vorticity-dominant leakage

$$
\boxed{
\mathfrak W_R
\gtrsim1.
}
$$

其中：

E-L1 若承擔 middle amplification，

再轉成：

$$
\boxed{
\text{cubic strain intermittency}.
}
$$

---

# 40. Q motif is no longer free

C4-J：

$$
Q
=
\text{Seven-Point Quadratic Cancellation}
$$

曾是一個 compact compensator。

C5-D：

$$
Q
\Rightarrow
\text{Gap}
\vee
\text{Direction Leakage}.
$$

C5-E：

$$
\boxed{
Q
\Rightarrow
\text{Middle-Gap/Cubic Intermittency}
\vee
\text{Strain-Derivative Fluctuation}
\vee
\text{Vorticity Leakage}.
}
$$

所以：

$$
\boxed{
\textbf{Q motif has been fully converted into PDE field defects}.
}
$$

---

# 41. Middle-gap concentration measure

對 gap limit：

$$
\mathfrak G_\ast>0,
$$

可進一步看：

$$
\boxed{
\theta^{-1}
}
$$

weighted middle activity。

定義 truncated gap severity：

$$
\boxed{
\mathfrak J_j(\delta)
=
\int_{\{
0<\theta_j\le\delta
\}}
\frac{
1
}{
\theta_j
}
\,d\mu_j^{mid,Q}
}
$$

where：

$$
\mu_j^{mid,Q}
$$

是適當 normalized middle/Q joint measure。

若：

$$
\mathfrak G_\ast>0
$$

且 middle load在 gap層不退化，

則：

$$
\boxed{
\mathfrak J_j(\delta)
}
$$

必在：

$$
\delta\downarrow0
$$

時失去 uniform integrability。

### 本輪不再展開此 severity measure，

留作 C5-F 可用 metadata。

---

# 42. X-Integration guards 更新

## G-GAPVAR

保存：

$$
\vartheta
=
\lambda_2^+\lambda_3/|S|^2
$$

而非只記 $\lambda_2^+$。

## G-QPHYS

在：

$$
\vartheta\ge\delta
$$

時 Q-weight可和 strain/vorticity quadratic activity比較。

## G-QWEIGHT

direction leakage量必說明是 Q-weighted、strain-weighted或 volume-weighted。

## G-SVLEAK

Q leakage轉 derivative前先分：

$$
\text{strain-carrying}
\vee
\text{vorticity-dominant}.
$$

## G-CUBIC

middle-gap承載 middle load時保存 cubic strain concentration。

## G-EFFVOL

effective-volume sparseness是 strain-amplitude pre-gate，

不得直接標成 Grujić–Xu theorem hypothesis。

## G-GXFIELD

published derivative theorem要求 $D^ku$ / $D^k\omega$ component/sign geometry。

---

# 43. True ETN 更新

C5-E defect state：

$$
\boxed{
\Theta_\ast^{SDef}
=
\left\langle
\Xi_\ast^{S\theta},
\mathfrak G_\ast,
\mathfrak D_\ast^{dir},
\mathfrak H_\ast,
\mathfrak W_\ast,
\phi_{S,3}^\ast,
r_{sp}^\ast,
\mathsf G_{\rm der}
\right\rangle.
}
$$

其中：

- $\Xi^{S\theta}$ = Q-weighted strain-direction/gap measure；
- $\mathfrak G$ = middle-gap mass；
- $\mathfrak D^{dir}$ = direction-dispersion defect；
- $\mathfrak H$ = strain derivative stock；
- $\mathfrak W$ = vorticity stock；
- $\phi_{S,3}$ = cubic effective-volume ratio；
- $\mathsf G_{\rm der}$ = derivative theorem-interface status。

---

# 44. C5 strategic status

C5-A：

$$
\text{motif compactness}.
$$

C5-B：

$$
\text{temporal oscillation/concentration}.
$$

C5-C：

$$
\text{transition curvature constraints}.
$$

C5-D：

$$
\text{Strong-Middle vs Q-cancellation incompatibility}.
$$

C5-E：

$$
\boxed{
\textbf{Q-cancellation residual}
\to
\textbf{middle-gap / derivative / vorticity / intermittency defects}.
}
$$

因此 C5 spatial–matrix route已不再留下 free Seven-Point motif。

---

# 45. What remains unresolved

## 1. Middle-gap route

middle-gap → cubic strain intermittency已證，

但還沒對接 raw：

$$
D^ku
$$

component/sign theorem gate。

## 2. Direction-leak route

已轉：

$$
\mathfrak H_R
\vee
\mathfrak W_R,
$$

但 stock ≠ geometric regularity。

## 3. Common far-pressure axis locking

C5-D 的 compressive-axis constraint尚未和 gap/dispersion defects聯立。

## 4. Derivative order escalation

也尚未判定：

$$
k_j\to\infty
$$

是否能系統性吸收 C5-E defects。

---

# 46. 新 frontier：C5-F

正式下一題：

$$
\boxed{
\textbf{C5-F — Strain/Vorticity Defect Coupling,
Axis Locking, and Derivative-Gate Escalation}.
}
$$

---

# 47. C5-F proof obligations

## F1 — Middle-gap × compressive-axis limit

當：

$$
\vartheta\to0,
$$

研究：

$$
e_1\otimes e_1-I/3
$$

是否仍保持 nontrivial pressure-axis information。

## F2 — Gap degeneration × axis locking

若 common far pressure要求 compressive axes鎖定，

middle-gap degeneration是否可同時維持 Q zero-barycenter geometry？

## F3 — Direction dispersion × axis locking

Q cancellation要求 strain directions spread，

而 pressure compensation要求 compressive axes落 common cone；

兩者是否形成第二 finite-dimensional incompatibility？

## F4 — Vorticity leakage × Miller orthogonality

E-VORT recurrent時，

接：

$$
P_{st}(\omega\otimes\omega)
$$

operator orthogonal congestion。

## F5 — Strain derivative stock × derivative amplitudes

由：

$$
\mathfrak H_R
$$

建立：

$$
D^2u
$$

amplitude / multiplicity dichotomy。

## F6 — Cubic strain intermittency × derivative component sets

測是否存在 safe finite-component transfer：

$$
S\text{-magnitude sparse}
\to
D u\text{ component/sign sparse}
$$

或必付 vorticity defect。

## F7 — Derivative order escalation

若 k=1/2 interfaces反覆失敗，

研究 defect是否迫使：

$$
k_j\to\infty.
$$

## F8 — Grujić–Xu gate audit

嚴格使用 2024 Theorem 3.5 / 3.14 hypotheses，

判定哪個 C5 defect branch真的已接 theorem-ready closure。

---

# 48. 正式狀態

$$
\boxed{
\begin{aligned}
\vartheta\leftrightarrow\lambda_2^+/|S|
&:\ \mathrm{PROVED},\\
\vartheta\ge\delta\Rightarrow |Q|\gtrsim_\delta |S|^2+|\omega|^2
&:\ \mathrm{PROVED},\\
\text{Q-weighted gap measure compactification}
&:\ \mathrm{DEFINED/COMPACT},\\
\text{zero Q barycenter excludes single strong-middle limit}
&:\ \mathrm{PROVED},\\
\text{quantitative direction anti-concentration}
&:\ \mathrm{PROVED},\\
\text{direction leakage}\Rightarrow
\text{strain derivative or vorticity stock}
&:\ \mathrm{PROVED},\\
\text{middle-gap load}\Rightarrow\text{cubic strain}
&:\ \mathrm{PROVED},\\
\text{cubic strain}\Rightarrow\text{small effective active volume}
&:\ \mathrm{PROVED},\\
\text{effective active-set lemma}
&:\ \mathrm{PROVED},\\
\text{middle-gap}\Rightarrow\text{strain intermittency}
&:\ \mathrm{PROVED\ UNDER\ BOUNDED\ STRAIN\ STOCK},\\
\text{strain intermittency}\Rightarrow
\text{published Grujić--Xu gate}
&:\ \mathrm{NOT\ YET},\\
Q\text{ motif free compensation}
&:\ \mathrm{NO},\\
\text{global regularity}
&:\ \mathrm{OPEN}.
\end{aligned}
}
$$

---

# 49. 結論

C5-D 把 Seven-Point Q-cancellation從 free finite-dimensional motif壓成：

$$
\boxed{
\text{Middle-Gap Degeneration}
\vee
\text{Direction Leakage}.
}
$$

C5-E現在把這兩支都翻譯回 PDE field quantities。

第一，

middle-gap variable：

$$
\vartheta(S)
=
\frac{
\lambda_2^+\lambda_3
}{
|S|^2
}
$$

和 normalized：

$$
\lambda_2^+/|S|
$$

quantitatively等價。

若：

$$
\vartheta\ge\delta,
$$

則：

$$
\boxed{
|Q|
\gtrsim
\delta
(
|S|^2+|\omega|^2
).
}
$$

所以 Q-weighted gap concentration是真正 physical quadratic-activity concentration。

第二，

若 Q cancellation在 nondegenerate gap regime逼固定 cone leakage，

leakage只有兩種支付方式：

$$
\boxed{
\text{strain-carrying leakage}
}
$$

或：

$$
\boxed{
\text{vorticity-dominant leakage}.
}
$$

前者經 Poincaré：

$$
\boxed{
\mathfrak H_R
=
\frac{
R^3
}{
\nu^2
}
\|\nabla S\|_2^2
\gtrsim
a_R^Q.
}
$$

後者：

$$
\boxed{
\mathfrak W_R
=
\frac{
R
}{
\nu^2
}
\|\omega\|_2^2
\gtrsim
a_R^Q.
}
$$

因此：

$$
\boxed{
Q\text{-cancellation}
\Rightarrow
\text{Gap}
\vee
\text{Derivative}
\vee
\text{Vorticity}.
}
$$

第三，

gap branch也不是 free。

因：

$$
\lambda_2^+|S|^2
=
\xi_2|S|^3,
$$

在：

$$
\vartheta\le\delta
$$

上：

$$
\xi_2\lesssim\delta.
$$

所以 fixed middle amplification必要求：

$$
\boxed{
\|S\|_3^3
\gtrsim
\delta^{-1}.
}
$$

相對固定 $L^2$ strain stock，

這強迫 effective volume：

$$
\boxed{
V_{\rm eff}
=
\frac{
\|S\|_2^6
}{
\|S\|_3^6
}
}
$$

collapse。

而 explicit set：

$$
E_c
=
\{
|S|\ge
c\|S\|_3^3/\|S\|_2^2
\}
$$

承載：

$$
\boxed{
\ge1-c
}
$$

比例 cubic strain activity，

同時：

$$
\boxed{
|E_c|
\le
c^{-2}V_{\rm eff}.
}
$$

所以 middle-gap degeneration真的變成：

$$
\boxed{
\textbf{spatial intermittency}.
}
$$

但最後的 guard非常重要：

Grujić–Xu 2024 Theorem 3.5 / 3.14要求的是：

$$
\boxed{
D^ku
\text{ 或 }
D^k\omega
}
$$

component/sign superlevel-set sparseness，

還有 theorem-specific later-time與 derivative-chain gates。

我們現在的：

$$
S,\quad\nabla S
$$

geometry還不能直接偷換。

所以 C5-E 到達的是：

$$
\boxed{
\textbf{Derivative-Intermittency Pre-Gate},
}
$$

不是 regularity proof。

正式下一篇：

$$
\boxed{
\textbf{C5-F — Strain/Vorticity Defect Coupling,
Axis Locking, and Derivative-Gate Escalation}.
}
$$

---

# References

1. E. Miller, *A regularity criterion for the Navier–Stokes equation involving only the middle eigenvalue of the strain tensor*, arXiv:1710.05569; Arch. Rational Mech. Anal. 235 (2020).
2. E. Miller, *On the interaction of strain and vorticity for solutions of the Navier–Stokes equation*, arXiv:2407.02691v2; Pure and Applied Analysis 8 (2026).
3. Z. Grujić, L. Xu, *Asymptotic Criticality of the Navier–Stokes Regularity Problem*, Journal of Mathematical Fluid Mechanics 26, Article 53 (2024), DOI: 10.1007/s00021-024-00888-x; arXiv:1911.00974.
4. Z. Bradshaw, T.-P. Tsai, *On the local pressure expansion for the Navier–Stokes equations*, arXiv:2001.11526.
5. P. Constantin, *Pressure, Intermittency, Singularity*, arXiv:2301.04489.

# Internal dependencies

- `NS_C5D_SpatialMatrix_StrongMiddleQuadraticPressureObstruction_v0.1.md`
- `NS_C5C_TemporalCorrelation_CrossCurvatureOrdering_v0.1.md`
- `NS_C5B_TemporalYoung_PulsePhaseCompatibility_v0.1.md`
- `NS_C5A_RecordWindow_MotifCompactness_v0.1.md`
- `NS_C4J_CompensationRigidity_FinalSynchronizationAudit_v0.1.md`
- `NS_C3V_TurnoverPacking_StrainFluctuationEscape_v0.1.md`
- `NS_C3W_PressureRotation_StrainSparseness_v0.1.md`
- `NS_C3X_JointPressureStrain_AnalyticityGap_v0.1.md`
- `NS_C3Y_DerivativeChain_IntermittencyTradeoff_v0.1.md`
- `True ETN / 無限維張力場`
- `X_Integral_Unified_Program_v0.2.md`

Next:

$$
\boxed{
\textbf{C5-F — Strain/Vorticity Defect Coupling,
Axis Locking, and Derivative-Gate Escalation}
}
$$
