---
title: "Navier–Stokes C5-I：Derivative Sign-Geometry Defects、Chain Sections 與 Harmonic-Measure Compatibility"
subtitle: "A Harmonic-or-Descent Dichotomy: Chain-Scale Sign-Sparseness Failure Forces Lower-Order Root Amplitude, While Recurrent Bad Cores Compactify as Isotropically Sign-Thick Motifs"
version: "v0.1"
date: "2026-08-15"
author: "Neo.K / EveMissLab"
language: "zh-TW"
status: "Theorem-style sign-microgeometry / derivative-chain compatibility refinement"
epistemic_status: "Exact 1D occupancy-to-lower-derivative estimate + compact sign-core metadata + direct interface to the published Grujić–Xu harmonic-measure and Type-A/Type-B chain framework. Does NOT prove Navier–Stokes regularity."
---

# Navier–Stokes C5-I
# Derivative Sign-Geometry Defects、Chain Sections 與 Harmonic-Measure Compatibility

## 0. 本輪定位

C5-H 正式封掉：

$$
\boxed{
\textbf{All-Order Static Effective-Volume Closure Program}.
}
$$

原因：

1. fixed-$k$ direct Theorem 3.5 是合法 kill switch；
2. 但其：
   $$
   2^{-k},
   \qquad
   4^{-k}
   $$
   order factors阻止把 direct criteria視為 monotone all-order ladder；
3. $L^2$ derivative log-convexity只控制 spectral ladder：
   $$
   \Lambda_k,
   $$
   不控制 physical multiplicity：
   $$
   \mathfrak N_k;
   $$
4. even Theorem 3.14 chain scale也不能一般性由 global-volume alone certify；
5. high-order asymptotic mechanism真正依賴：
   $$
   \boxed{
   \text{component/sign 1D geometry}
   +
   \text{derivative-chain dynamics}
   +
   \text{harmonic measure}.
   }
   $$

C5-I 因此第一次直接把：

$$
\boxed{
\textbf{sign microgeometry}
}
$$

當成主要 object，

而不是 volume geometry的附屬品。

本輪主要結果：

1. 重新 faithful encoding Grujić–Xu Definition 3.15：
   - exponentially separated derivative sections；
   - section maximizer $m_i$；
   - Type-$\mathcal A$ / Type-$\mathcal B$ strings；
2. 對每個 derivative level定義 chain-scale selected sign high set；
3. 定義 exact：
   $$
   \boxed{
   \text{best-direction chord occupancy};
   }
   $$
4. Theorem 3.14 spatial pass等價於：
   在每個 dangerous basepoint可找到 occupancy $\le\delta$ 的 direction/scale；
5. spatial failure則產生一個：
   $$
   \boxed{
   \textbf{isotropically sign-thick bad core};
   }
   $$
6. bad core的 angular occupancy profile可 weak-* compactify於：
   $$
   L^\infty(\mathbb{RP}^2);
   $$
7. harmonic-measure pass的 geometric reserve由：
   $$
   h(\beta)
   =
   \frac2\pi
   \arcsin
   \frac{1-\beta^2}{1+\beta^2}
   $$
   measure；
8. 若 chain-scale spatial condition失敗，
   selected $k$-th derivative同-sign chord厚度反而強迫：
   $$
   \boxed{
   A_{k-1}
   \ge
   ((1+\lambda)\delta-1)
   r_kA_k;
   }
   $$
9. 在 Theorem 3.14 chain scale：
   $$
   r_k
   =
   \frac1{
   2\widetilde{\mathcal C}_k
   A_k^{1/(k+1)}
   },
   $$
   因而：
   $$
   \boxed{
   A_{k-1}^{1/k}
   \gtrsim
   \widetilde{\mathcal C}_k^{-1/k}
   A_k^{1/(k+1)};
   }
   $$
10. 轉成 Grujić–Xu normalized chain amplitudes：
    $$
    \boxed{
    \mathcal R(k-1,c,s)
    \ge
    d_k(c)
    \mathcal R(k,c,s);
    }
    $$
11. 因此得到：
    $$
    \boxed{
    \textbf{Harmonic-Measure Pass}
    \vee
    \textbf{Descending-Root Toll};
    }
    $$
12. contrapositive：
    若 adjacent normalized derivative ascent比 $d_k^{-1}$ 更陡，
    level $k$ sign geometry必 pass；
13. consecutive same-time sign failures會限制一整段 derivative ascent gain；
14. 所以 persistent Type-$\mathcal A$ strong ascent不能完全由 sign-thick levels組成；
15. Type-$\mathcal B$ / descending behavior與 sign-thick defect相容，
    但 published Theorem 3.9 / Corollary 3.12正是處理 descending chains；
16. bad sign core另有 fixed chain-scale local $L^2$ toll；
17. 多個 disjoint bad cores數量由 spectral-cell/effective-volume multiplicity控制；
18. weak limit若：
    $$
    \beta_\ast=\delta,
    $$
    形成：
    $$
    \boxed{
    \textbf{Harmonic Critical-Saturation Defect};
    }
    $$
19. 本輪也找到一個 hard guard：
    不同 derivative levels的 theorem-admissible times一般不同；
    same-time descent inequalities不能無條件跨 levels相乘；
20. 這個 timing-stitching precisely 是 dynamic interpolation需要保留的部分。

---

# 1. Fresh primary-source audit

## 1.1 Grujić–Xu 2024 — Definition 3.15

正式 version of record把 derivative orders分 sections：

$$
\boxed{
\ell_0<\ell_1<\cdots,
\qquad
\ell_{i+1}
=
\phi(\ell_i),
\qquad
\phi(x)\ge2x.
}
$$

在每 section：

$$
[\ell_i,\ell_{i+1}],
$$

選：

$$
\boxed{
m_i
}
$$

使：

$$
\boxed{
\mathcal R(m_i,c(\ell_i),t)
=
\max_{\ell_i\le j\le\ell_{i+1}}
\mathcal R(j,c(\ell_i),t),
}
$$

其中：

$$
\boxed{
\mathcal R(k,c,t)
=
\frac{
\|D^ku(t)\|_\infty^{1/(k+1)}
}{
c^{k/(k+1)}
(k!)^{1/(k+1)}
}.
}
$$

---

# 2. Type-$\mathcal A$ / Type-$\mathcal B$

section：

$$
[\ell_i,\ell_{i+1}]
$$

為 Type-$\mathcal A$，

若存在：

$$
k_i>\ell_{i+1}
$$

使：

$$
\boxed{
\mathcal R(k_i,c(\ell_i),t)
\ge
\max_{m_i\le j\le k_i}
\mathcal R(j,c(\ell_i),t).
}
$$

即 higher order eventually catches/overtakes current section maximum。

Type-$\mathcal B$ 若：

$$
\boxed{
\mathcal R(m_i,c(\ell_i),t)
>
\max_{j>m_i}
\mathcal R(j,c(\ell_i),t).
}
$$

即 current section maximum dominates the entire higher-order tail。

published proof再處理 Type-A / Type-B strings及其 switches。

---

# 3. Theorem 3.14 spatial condition

對 velocity derivative order：

$$
k\ge\ell,
$$

在 theorem-admissible later time：

$$
s=s(t),
$$

Theorem 3.14要求：

對 every spatial point：

$$
x_0,
$$

存在：

$$
\boxed{
\rho
\le
r_k(s)
:=
\frac1{
2\widetilde{\mathcal C}(\|u_0\|,\ell,k)
\|D^ku(s)\|_\infty^{1/(k+1)}
}
}
$$

及 line direction：

$$
\nu,
$$

使 selected component/sign superlevel set：

$$
\boxed{
V_{\lambda,k}^{j,\pm}(s)
=
\left\{
x:
(D^ku)_j^\pm(x,s)
>
\lambda
A_k(s)
\right\}
}
$$

1D $\delta$-sparse around：

$$
x_0.
$$

其中：

$$
A_k(s)
=
\|D^ku(s)\|_\infty.
$$

---

# 4. Theorem tuning

published parameter pair：

$$
(\lambda,\delta)
$$

is chosen consistently with harmonic-measure condition。

In particular：

$$
\boxed{
\frac1{1+\lambda}
<
\delta
<
1.
}
$$

因此：

$$
\boxed{
\kappa_{\lambda,\delta}
:=
(1+\lambda)\delta-1
>0.
}
$$

這個 positive margin會在 C5-I 的 sign-defect descent theorem中直接出現。

---

# 5. One-dimensional chord occupancy

對 measurable：

$$
E\subset\mathbb R^3,
$$

point：

$$
x_0,
$$

radius：

$$
r,
$$

projective direction：

$$
[\nu]\in\mathbb{RP}^2,
$$

定義：

$$
\boxed{
b_E(x_0,r,[\nu])
=
\frac1{2r}
\mathcal H^1
\left(
E\cap
(x_0-r\nu,x_0+r\nu)
\right).
}
$$

所以：

$$
\boxed{
0\le b_E\le1.
}
$$

1D $\delta$-sparseness正是：

$$
\boxed{
\exists[\nu]:
\quad
b_E(x_0,r,[\nu])
\le\delta.
}
$$

---

# 6. Best directional occupancy

定義：

$$
\boxed{
\beta_E(x_0,r)
=
\inf_{[\nu]\in\mathbb{RP}^2}
b_E(x_0,r,[\nu]).
}
$$

則：

$$
\boxed{
\beta_E(x_0,r)\le\delta
}
$$

等價於在 radius $r$ 存在 theorem-usable sparse direction。

---

# 7. Exact spatial-pass state

對 level $k$、time $s$，

定義：

$$
\boxed{
\mathsf{SG}_k(s)=1
}
$$

若對所有：

$$
x_0
$$

存在：

$$
0<\rho\le r_k(s)
$$

使：

$$
\beta_{V_{\lambda,k}^{j(x_0),\pm(x_0)}}(x_0,\rho)
\le\delta.
$$

否則：

$$
\boxed{
\mathsf{SG}_k(s)=0.
}
$$

### Important

$\mathsf{SG}=1$ 是 Theorem 3.14真正的 spatial geometry pass。

---

# 8. Bad basepoint

若：

$$
\mathsf{SG}_k(s)=0,
$$

則存在：

$$
x_k
$$

使對所有：

$$
0<\rho\le r_k(s),
$$

及所有 projective directions：

$$
[\nu],
$$

selected sign high set都滿足：

$$
\boxed{
b_k(x_k,\rho,[\nu])
>
\delta.
}
$$

特別在 maximal chain radius：

$$
r_k=r_k(s),
$$

有：

$$
\boxed{
b_k(x_k,r_k,[\nu])
>
\delta
\qquad
\forall[\nu].
}
$$

---

# 9. Chain-scale angular sign profile

對 bad witness：

$$
x_k,
$$

定義：

$$
\boxed{
b_k([\nu])
=
b_{V_{\lambda,k}^{j,\pm}}
(x_k,r_k,[\nu]).
}
$$

則：

$$
\boxed{
b_k
\in
L^\infty
(
\mathbb{RP}^2;
[0,1]
),
}
$$

且：

$$
\boxed{
b_k([\nu])>\delta
}
$$

for all directions。

---

# 10. C5-I.1：Angular Sign-Core Compactness

任意 recurrent bad-core sequence：

$$
b_n
$$

有 subsequence：

$$
\boxed{
b_n
\stackrel{*}{\rightharpoonup}
b_\ast
}
$$

in：

$$
L^\infty(\mathbb{RP}^2).
$$

因：

$$
b_n-\delta\ge0,
$$

positive cone weak-* closed，

所以：

$$
\boxed{
b_\ast([\nu])
\ge
\delta
}
$$

for almost every：

$$
[\nu].
$$

### Interpretation

recurrent spatial geometry failure compactifies成：

$$
\boxed{
\textbf{Isotropically Sign-Thick Derivative Core}.
}
$$

---

# 11. Strong vs boundary sign-core limits

定義：

$$
\boxed{
\beta_n
=
\inf_{[\nu]}
b_n([\nu])
\in[\delta,1].
}
$$

抽：

$$
\beta_n\to\beta_\ast.
$$

兩種 limit：

## I-SGSTRONG

$$
\boxed{
\beta_\ast>\delta.
}
$$

strictly sign-thick。

## I-SGCRIT

$$
\boxed{
\beta_\ast=\delta.
}
$$

finite-level failures逼近 theorem threshold。

本文稱：

$$
\boxed{
\textbf{Harmonic Critical-Saturation Defect}.
}
$$

---

# 12. Harmonic-measure map

對 line active-set occupancy：

$$
0\le\beta<1,
$$

complement measure fraction：

$$
1-\beta.
$$

Solynin extremal estimate給 harmonic-measure lower bound：

$$
\boxed{
h(\beta)
=
\frac2\pi
\arcsin
\frac{
1-\beta^2
}{
1+\beta^2
}.
}
$$

$h$ strictly decreasing。

因此：

$$
\boxed{
\beta\le\delta
\Rightarrow
h(\beta)\ge h(\delta).
}
$$

---

# 13. Harmonic pass

當某 point/scale/direction：

$$
\beta\le\delta,
$$

line complement提供 harmonic-measure lower bound：

$$
h_\delta
=
h(\delta).
$$

再結合：

- complex spatial analyticity；
- chain-level complex derivative bound；
- two-constants theorem；

published Grujić–Xu argument把：

$$
D^ku(x_0,s)
$$

壓回 norm threshold。

### External status

這個 contraction mechanism屬 published theorem。

C5-I不重新證其完整 analytic constants。

---

# 14. Why a bad point must be sign-thick

如果 selected derivative at：

$$
x_0
$$

已不在：

$$
V_{\lambda,k}^{j,\pm},
$$

harmonic argument在 complement case直接安全。

所以 genuine geometry obstruction必由 selected high-sign set局部 thick behavior支撐。

這使 bad-core witness具有實際 amplitude provenance。

---

# 15. Bad core → volumetric thickness

若：

$$
b_k([\nu])>\delta
$$

for every direction，

則 contrapositive of the standard:

$$
\text{3D }\delta^3\text{-sparseness}
\Rightarrow
\text{1D }\delta\text{-sparseness}
$$

給：

$$
\boxed{
\left|
V_{\lambda,k}^{j,\pm}
\cap
B_{r_k}(x_k)
\right|
>
\delta^3
|B_{r_k}|.
}
$$

---

# 16. C5-I.2：Bad Sign-Core Local $L^2$ Toll

在：

$$
V_{\lambda,k}^{j,\pm},
$$

selected component magnitude：

$$
>
\lambda A_k.
$$

所以：

$$
\boxed{
\int_{B_{r_k}(x_k)}
|D^ku|^2dx
\ge
c_3
\lambda^2
\delta^3
A_k^2
r_k^3.
}
$$

其中：

$$
c_3=|B_1|.
$$

在 chain radius：

$$
r_k
=
\frac1{
2\widetilde{\mathcal C}_k
A_k^{1/(k+1)}
},
$$

得到：

$$
\boxed{
\int_{B_{r_k}(x_k)}
|D^ku|^2dx
\ge
c
\lambda^2\delta^3
\widetilde{\mathcal C}_k^{-3}
A_k^{2-\frac3{k+1}}.
}
$$

---

# 17. Bad-core local fraction

令：

$$
L_k
=
\|D^ku\|_2.
$$

define：

$$
\boxed{
\Phi_k^{bad}
=
\frac{
\int_{B_{r_k}(x_k)}
|D^ku|^2
}{
L_k^2
}.
}
$$

則：

$$
\boxed{
\Phi_k^{bad}
\ge
c
\lambda^2\delta^3
\frac{
A_k^2r_k^3
}{
L_k^2
}.
}
$$

用：

$$
V_k^{eff}
=
L_k^2/A_k^2,
$$

$$
\boxed{
\Phi_k^{bad}
\ge
c
\lambda^2\delta^3
\frac{
r_k^3
}{
V_k^{eff}
}.
}
$$

---

# 18. Relation to C5-H multiplicity

C5-H：

$$
V_k^{eff}
=
\mathfrak N_k
\Lambda_k^{-3}.
$$

所以 bad-core fraction：

$$
\boxed{
\Phi_k^{bad}
\gtrsim
\lambda^2\delta^3
\frac{
(r_k\Lambda_k)^3
}{
\mathfrak N_k
}.
}
$$

### Meaning

sign-geometry failure產生一個 genuine local dense cell。

若：

$$
\mathfrak N_k
$$

巨大，

它可以只承擔很小 global derivative mass fraction。

因此：

$$
\boxed{
\textbf{Sign-thick core}
}
$$

與：

$$
\boxed{
\textbf{Spectral-cell multiplicity}
}
$$

是 compatible but coupled motifs。

---

# 19. Disjoint bad-core count

若同一 level/time有：

$$
N_k
$$

個 pairwise disjoint bad balls：

$$
B_{r_k}(x_{k,a}),
$$

則：

$$
N_k
c\lambda^2\delta^3A_k^2r_k^3
\le
L_k^2.
$$

因此：

$$
\boxed{
N_k
\le
C_{\lambda,\delta}
\frac{
V_k^{eff}
}{
r_k^3
}.
}
$$

所以：

$$
\boxed{
\textbf{bad-core multiplicity}
}
$$

被 C5-H effective-volume multiplicity直接控制。

---

# 20. Main new bridge：geometry failure → lower derivative

現在固定：

$$
k\ge1.
$$

在 bad witness：

$$
x_k,
$$

selected component/sign可寫：

$$
\boxed{
f
=
D^\zeta u_a,
\qquad
|\zeta|=k.
}
$$

choose：

$$
q
$$

such that：

$$
\zeta_q\ge1.
$$

定義 lower derivative：

$$
\boxed{
g
=
D^{\zeta-e_q}u_a.
}
$$

沿 coordinate line：

$$
x=x_k+se_q,
$$

有：

$$
\boxed{
g'(s)=f(x_k+se_q).
}
$$

---

# 21. Positive selected sign

先假設 selected sign為：

$$
+.
$$

bad-core property在：

$$
e_q
$$

direction給：

$$
\boxed{
\left|
\left\{
s\in[-r_k,r_k]:
f(x_k+se_q)
>
\lambda A_k
\right\}
\right|
>
2\delta r_k.
}
$$

而 everywhere：

$$
f\ge-A_k.
$$

---

# 22. C5-I.3：Sign-Thick Chord Descent Lemma

integration：

$$
g(r_k)-g(-r_k)
=
\int_{-r_k}^{r_k}
f(x_k+se_q)ds.
$$

所以：

$$
\begin{aligned}
g(r_k)-g(-r_k)
&>
\lambda A_k(2\delta r_k)
-
A_k(2r_k-2\delta r_k)
\\
&=
2r_kA_k
\left(
(1+\lambda)\delta-1
\right).
\end{aligned}
$$

定義：

$$
\boxed{
\kappa_{\lambda,\delta}
=
(1+\lambda)\delta-1
>0.
}
$$

則：

$$
\boxed{
|g(r_k)-g(-r_k)|
>
2
\kappa_{\lambda,\delta}
r_kA_k.
}
$$

所以至少一端：

$$
|g|
\ge
\kappa_{\lambda,\delta}r_kA_k.
$$

因此：

$$
\boxed{
A_{k-1}
\ge
\kappa_{\lambda,\delta}
r_kA_k.
}
$$

---

# 23. Negative selected sign

若 selected sign為：

$$
-,
$$

apply same argument to：

$$
-f.
$$

得到相同：

$$
\boxed{
A_{k-1}
\ge
\kappa_{\lambda,\delta}
r_kA_k.
}
$$

所以 lemma與 sign無關。

---

# 24. Chain-scale form

代入：

$$
r_k
=
\frac1{
2\widetilde{\mathcal C}_k
A_k^{1/(k+1)}
},
$$

得到：

$$
\boxed{
A_{k-1}
\ge
\frac{
\kappa_{\lambda,\delta}
}{
2\widetilde{\mathcal C}_k
}
A_k^{k/(k+1)}.
}
$$

taking $k$-th root：

$$
\boxed{
A_{k-1}^{1/k}
\ge
\left(
\frac{
\kappa_{\lambda,\delta}
}{
2\widetilde{\mathcal C}_k
}
\right)^{1/k}
A_k^{1/(k+1)}.
}
$$

---

# 25. Grujić–Xu normalized root form

固定 section normalization：

$$
c=c(\ell_i).
$$

recall：

$$
\mathcal R(k,c,s)
=
\frac{
A_k^{1/(k+1)}
}{
c^{k/(k+1)}
(k!)^{1/(k+1)}
}.
$$

因此：

$$
\boxed{
\mathcal R(k-1,c,s)
\ge
d_k(c)
\mathcal R(k,c,s),
}
$$

其中：

$$
\boxed{
d_k(c)
=
\left(
\frac{
\kappa_{\lambda,\delta}
}{
2\widetilde{\mathcal C}_k
}
\right)^{1/k}
c^{1/[k(k+1)]}
\frac{
(k!)^{1/(k+1)}
}{
((k-1)!)^{1/k}
}.
}
$$

---

# 26. Equivalent explicit factorial factor

因：

$$
k!
=
k(k-1)!,
$$

可寫：

$$
\boxed{
d_k(c)
=
\left(
\frac{
\kappa_{\lambda,\delta}
}{
2\widetilde{\mathcal C}_k
}
\right)^{1/k}
c^{1/[k(k+1)]}
k^{1/(k+1)}
((k-1)!)^{-1/[k(k+1)]}.
}
$$

### Guard

C5-I不假設：

$$
d_k\to1.
$$

這需要額外 control on：

$$
\widetilde{\mathcal C}_k
$$

growth。

---

# 27. C5-I.4：Harmonic-or-Descent Dichotomy

在 theorem-admissible time：

$$
s,
$$

對任意：

$$
k\ge1,
$$

至少一個成立：

## I-HARM

Theorem 3.14 chain-scale spatial condition passes at level $k$：

$$
\boxed{
\mathsf{SG}_k(s)=1.
}
$$

或：

## I-DESC

$$
\boxed{
\mathcal R(k-1,c,s)
\ge
d_k(c)
\mathcal R(k,c,s).
}
$$

### Proof

若 I-HARM false，

spatial condition fails，

C5-I.3–25 apply。$\square$

---

# 28. Contrapositive：strong adjacent ascent forces geometry pass

如果：

$$
\boxed{
\mathcal R(k,c,s)
>
d_k(c)^{-1}
\mathcal R(k-1,c,s),
}
$$

則 I-DESC impossible，

hence：

$$
\boxed{
\mathsf{SG}_k(s)=1.
}
$$

### Interpretation

$$
\boxed{
\textbf{a sufficiently steep derivative-root ascent
forces chain-scale sign sparseness}.
}
$$

這是 C5 第一次由 amplitude-chain shape直接逼 sign geometry。

---

# 29. Same-time consecutive failure

若在同一 time：

$$
s
$$

levels：

$$
J+1,\ldots,K
$$

全部 spatially fail，

則 iteration：

$$
\boxed{
\mathcal R(J,c,s)
\ge
\left(
\prod_{n=J+1}^{K}
d_n(c)
\right)
\mathcal R(K,c,s).
}
$$

equivalently：

$$
\boxed{
\frac{
\mathcal R(K,c,s)
}{
\mathcal R(J,c,s)
}
\le
\prod_{n=J+1}^{K}
d_n(c)^{-1}.
}
$$

---

# 30. C5-I.5：Type-A Puncture Criterion

suppose at one time：

$$
s,
$$

a derivative interval：

$$
[J,K]
$$

has ascent gain：

$$
\boxed{
\frac{
\mathcal R(K,c,s)
}{
\mathcal R(J,c,s)
}
>
\prod_{n=J+1}^{K}
d_n(c)^{-1}.
}
$$

Then not every level：

$$
J+1,\ldots,K
$$

can be spatially bad。

Therefore at least one：

$$
n\in(J,K]
$$

has：

$$
\boxed{
\mathsf{SG}_n(s)=1.
}
$$

### Meaning

a strong Type-A-like takeover must puncture a completely sign-thick order interval。

---

# 31. Relation to Definition 3.15

Type-$\mathcal A$ sections express eventual higher-order takeover。

C5-I does NOT prove：

$$
\boxed{
\text{Type-A}\Rightarrow
\text{all levels spatially good}.
}
$$

It proves only：

$$
\boxed{
\text{large enough same-time ascent gain}
\Rightarrow
\text{at least one harmonic-pass level}.
}
$$

This distinction is essential because Theorem 3.14 requires the spatial geometry hypotheses across the full required derivative range。

---

# 32. Type-B compatibility

Type-$\mathcal B$ means current section maximum dominates all higher orders。

C5-I descending-root toll：

$$
\mathcal R(k-1)
\gtrsim
\mathcal R(k)
$$

is geometrically compatible with such descending behavior。

### But

published Theorem 3.9 / Corollary 3.12 were designed precisely to stabilize descending chains under condition (3.14)。

Therefore：

$$
\boxed{
\textbf{Type-B is not a free singularity survivor}.
}
$$

C5-I only identifies that sign-thick geometry naturally pushes chain shape toward the descending side。

---

# 33. Harmonic-measure compatibility

For a good level：

$$
\mathsf{SG}_k=1,
$$

choose theorem line where occupancy：

$$
\beta\le\delta.
$$

then：

$$
\boxed{
h(\beta)
\ge
h_\delta
:=
\frac2\pi
\arcsin
\frac{
1-\delta^2
}{
1+\delta^2
}.
}
$$

Grujić–Xu combine this harmonic lower bound with:

- spatial analyticity radius；
- complex derivative upper bounds from the chain；
- two-constants theorem；

and parameter condition (3.14) to obtain contraction / stabilization。

---

# 34. Harmonic critical saturation

If recurrent failures have：

$$
\beta_n\downarrow\delta,
$$

then:

$$
\boxed{
h(\beta_n)\uparrow h_\delta
}
$$

from below。

So the spatial defect approaches the exact harmonic-measure threshold。

This is：

$$
\boxed{
\textbf{Harmonic Critical-Saturation}.
}
$$

It is analogous to C5-H asymptotic a-priori saturation：

the survivor lives increasingly close to the sufficient regularity boundary rather than violating it by a fixed margin。

---

# 35. Strong sign-thickness

If instead：

$$
\beta_\ast
\ge
\delta+\varepsilon_0,
$$

then:

$$
\boxed{
h(\beta_\ast)
\le
h(\delta+\varepsilon_0)
<
h_\delta.
}
$$

There is a fixed harmonic-measure deficit。

But C5-I.3 simultaneously gives a fixed lower-order root toll：

$$
\kappa_{\lambda,\delta+\varepsilon_0}
>
\kappa_{\lambda,\delta}.
$$

Thus:

$$
\boxed{
\text{stronger harmonic defect}
\Rightarrow
\text{stronger descending-root coupling}.
}
$$

---

# 36. Continuous occupancy–descent relation

If maximal-radius best occupancy is：

$$
\beta_k>\frac1{1+\lambda},
$$

repeat C5-I.3 with：

$$
\beta_k
$$

rather than theorem threshold：

$$
\delta.
$$

Then：

$$
\boxed{
A_{k-1}
\ge
\left(
(1+\lambda)\beta_k-1
\right)
r_kA_k.
}
$$

So sign-core thickness has an exact quantitative chain cost。

---

# 37. Geometry failure as an order-space state

For a derivative section：

$$
[\ell_i,\ell_{i+1}],
$$

define binary geometry indicators：

$$
\boxed{
g_{i,k}
=
1-\mathsf{SG}_k
\in\{0,1\}.
}
$$

normalized order coordinate：

$$
\boxed{
\theta_{i,k}
=
\frac{
k-\ell_i
}{
\ell_{i+1}-\ell_i
}
\in[0,1].
}
$$

define defect counting measure：

$$
\boxed{
\mu_i^{SG}
=
\frac1{
\ell_{i+1}-\ell_i+1
}
\sum_{k=\ell_i}^{\ell_{i+1}}
g_{i,k}
\delta_{\theta_{i,k}}.
}
$$

This is a subprobability measure on：

$$
[0,1].
$$

---

# 38. Sectionwise sign-defect compactness

Any sequence of sections has a subsequence：

$$
\boxed{
\mu_i^{SG}
\rightharpoonup
\mu_\ast^{SG}
}
$$

on：

$$
[0,1].
$$

Interpretation：

- zero measure = geometry good at asymptotically full fraction of levels；
- diffuse nonzero measure = distributed sign defects；
- atoms = defect orders concentrate at preferred normalized positions。

### Guard

Even:

$$
\mu_\ast^{SG}=0
$$

does NOT imply Theorem 3.14 closure。

A single bad level per ever-larger section has vanishing density but still blocks an all-order hypothesis。

---

# 39. Witness bad-order state

To preserve rare defects，

if section $i$ contains any geometry failure，

select deterministic first bad order：

$$
k_i^{bad}.
$$

define：

$$
\boxed{
\theta_i^{bad}
=
\frac{
k_i^{bad}-\ell_i
}{
\ell_{i+1}-\ell_i
}
\in[0,1].
}
$$

Along recurrent defective sections：

$$
\boxed{
\theta_i^{bad}
\to
\theta_\ast^{bad}
}
$$

after subsequence。

So vanishing defect density does not erase the recurrent bad-order carrier。

---

# 40. Type / geometry joint alphabet

For each section：

$$
i,
$$

define：

$$
\boxed{
\mathsf T_i
\in
\{\mathcal A,\mathcal B\},
}
$$

and：

$$
\boxed{
\mathsf G_i
\in
\{
\mathrm{GOOD},
\mathrm{BAD}
\},
}
$$

where BAD means the selected theorem-relevant evaluation contains a spatial geometry defect。

finite alphabet：

$$
\boxed{
\{
A_G,
A_B,
B_G,
B_B
\}.
}
$$

With a separate：

$$
\boxed{
\mathrm{TIME}
}
$$

cemetery/state when no theorem-admissible evaluation can be aligned。

---

# 41. Joint section compactness

Because the alphabet is finite，

any infinite section sequence has a subsequence with eventually constant joint type：

$$
\boxed{
\mathsf Z_\ast
\in
\{
A_G,A_B,B_G,B_B,\mathrm{TIME}
\}.
}
$$

This is the simplest C5 compactification of Type-A/Type-B with sign geometry。

---

# 42. But Type-A/B can switch in time

Grujić–Xu proof explicitly tracks strings switching：

$$
\mathcal A
\leftrightarrow
\mathcal B.
$$

So a static section label is insufficient for full dynamic interpolation。

C5-I therefore adds a normalized switch-time coordinate。

---

# 43. Chain time normalization

At level：

$$
k,
$$

Theorem 3.14 later window：

$$
s-t
\in
\left[
\frac1{
4\widetilde{\mathcal C}_kA_k(t)^{2/(k+1)}
},
\frac1{
\widetilde{\mathcal C}_kA_k(t)^{2/(k+1)}
}
\right].
$$

define：

$$
\boxed{
\tau_k
=
\widetilde{\mathcal C}_k
A_k(t)^{2/(k+1)}
(s-t)
\in
[1/4,1].
}
$$

If no aligned theorem time is available：

$$
\boxed{
\tau_k=\partial_T.
}
$$

---

# 44. Timing compactness

space：

$$
\boxed{
[1/4,1]\cup\{\partial_T\}
}
$$

compact after isolated cemetery point。

Thus chain geometry/time events can be compactified jointly：

$$
\boxed{
(\mathsf T_i,\mathsf G_i,\tau_i,\theta_i^{bad}).
}
$$

---

# 45. Critical hard guard：different orders use different times

C5-I.3 gives same-time inequality：

$$
\boxed{
\mathcal R(k-1,c,s)
\ge
d_k
\mathcal R(k,c,s).
}
$$

But Theorem 3.14 may test level：

$$
k
$$

at：

$$
s_k
$$

and level：

$$
k-1
$$

at：

$$
s_{k-1}
\ne s_k.
$$

Therefore：

$$
\boxed{
\text{per-level descent inequalities at theorem times}
}
$$

cannot be blindly multiplied across $k$。

This is exactly where the published dynamic interpolation machinery is necessary。

---

# 46. C5-I temporal-order defect

Define：

$$
\boxed{
\Delta\tau_{k,k-1}
=
\text{normalized separation between admissible chain evaluation times}.
}
$$

If these cannot be synchronized into common chain windows，

the all-order geometry state carries：

$$
\boxed{
\textbf{Order-Dependent Timing Defect}.
}
$$

C5-I does not claim this defect impossible。

---

# 47. The published proof handles Type switches dynamically

Grujić–Xu Lemma 3.16 treats Type-$\mathcal A$ strings until switch to Type-$\mathcal B$。

Lemma 3.17 controls Type-$\mathcal B$ strings until switch to Type-$\mathcal A$。

The proof of Theorem 3.14 then groups blocks and tracks maxima：

$$
\widehat m_i
$$

through switching times。

Thus:

$$
\boxed{
\textbf{Type switching itself is not a loophole
once theorem geometry hypothesis is available}.
}
$$

---

# 48. What a hypothetical survivor must do

Under the published chain setup，

if from some sufficiently high:

$$
\ell
$$

onward all required levels/times satisfy：

$$
\boxed{
D^ku(s)
\in
Z_{1/(k+1)}
}
$$

with theorem constants，

Theorem 3.14 excludes：

$$
T^\ast
$$

as blow-up time。

Therefore any hypothetical survivor must recurrently produce：

$$
\boxed{
\text{Sign-Geometry Defect}
\vee
\text{Timing/Chain-Hypothesis Defect}.
}
$$

---

# 49. C5-I sharpened survivor implication

If sign geometry is the recurring defect，

then every such bad event also pays：

$$
\boxed{
\text{Descending-Root Toll}
}
$$

and：

$$
\boxed{
\text{Dense Sign-Core }L^2\text{ Toll}.
}
$$

Therefore sign geometry is not an independent Boolean failure。

It is coupled to：

- derivative chain shape；
- derivative effective volume；
- spatial multiplicity。

---

# 50. Sign-core vs multiplicity trilemma

A bad event can be:

## I-C1 — Single/few dense cores

$$
\Phi_k^{bad}
\not\ll1.
$$

A nonnegligible fraction of derivative $L^2$ mass sits in a chain-scale sign-thick region。

## I-C2 — Many-core multiplicity

many disjoint bad cores，

paid by：

$$
V_k^{eff}/r_k^3.
$$

## I-C3 — Small-core fraction with diffuse remainder

one bad core exists but：

$$
\Phi_k^{bad}\to0,
$$

while most $L^2$ derivative mass remains elsewhere。

All are compatible with theorem failure，

but they are distinct recurrent motifs。

---

# 51. Harmonic-or-Descent network

C5-H had:

$$
\boxed{
\text{Spectral}
+
\text{Multiplicity}
+
\text{Sign}
+
\text{Time}
+
\text{Chain}.
}
$$

C5-I now routes the Sign coordinate：

$$
\boxed{
\text{Sign Defect}
\Rightarrow
\text{Dense Core}
+
\text{Descending Root Toll}.
}
$$

Thus:

$$
\boxed{
\begin{aligned}
\text{level }k
&\Rightarrow
\text{Harmonic Pass}
\\
&\quad\vee
\left(
\text{Dense Sign Core}
+
\text{Descending Root Toll}
\right).
\end{aligned}
}
$$

---

# 52. A new order-space tension

Type-A geometry wants high derivative levels to overtake lower ones。

Sign-thick failure pushes:

$$
\mathcal R(k-1)
$$

back up relative to:

$$
\mathcal R(k).
$$

Hence:

$$
\boxed{
\textbf{Type-A ascent}
}
$$

and:

$$
\boxed{
\textbf{persistent sign-thick defects}
}
$$

are antagonistic order-space effects。

C5-I.5 quantifies this antagonism on same-time order intervals。

---

# 53. Why this is not yet a contradiction

Three reasons：

1. descent coefficient：
   $$
   d_k
   $$
   may be small due theorem constants；
2. bad levels can be sparse in order；
3. theorem geometry is evaluated at order-dependent later times。

So:

$$
\boxed{
\text{Sign Defect}
\Rightarrow
\text{Type-B}
}
$$

is NOT proved。

Only a quantitative adjacent descent pressure is proved。

---

# 54. Potential high-order favorable regime

If future analysis establishes：

$$
\boxed{
-\log d_k=o(1)
}
$$

or at least summably small across relevant section scales，

then a long run of sign defects would force:

$$
\boxed{
\mathcal R(k-1)
\approx
\mathcal R(k)
}
$$

and make strong Type-A takeover increasingly difficult。

### Current status

$$
\boxed{
\mathrm{CONDITIONAL}.
}
$$

No such theorem-constant upper growth estimate is assumed in C5-I。

---

# 55. Harmonic microgeometry is weaker than volume sparsity

A component/sign high set may have large 3D volume，

yet at every dangerous point admit one sparse line direction。

Then:

$$
\boxed{
\mathsf{SG}_k=1
}
$$

even though:

$$
V_k^{eff}
$$

is large。

This is exactly why C5-H volume-only route was too coarse。

C5-I restores the genuinely anisotropic geometry used by the published theorem。

---

# 56. Bad-core geometry is stronger than volume failure

Conversely，

if a theorem spatial condition truly fails at：

$$
x_k,
$$

the high set is not merely globally large。

At maximal chain scale it is thick in：

$$
\boxed{
\textbf{every line direction through }x_k.
}
$$

This is a much stronger local statement than：

$$
\mathfrak G_k^{dir}>1
$$

or：

$$
V_k^{eff}\text{ large}.
$$

---

# 57. Compact C5-I state

Define block/level state：

$$
\boxed{
\Theta^{I}
=
\left\langle
\mathcal R_k,
\mathsf T_i,
\mathsf{SG}_k,
\tau_k,
\beta_k,
b_k(\cdot),
\Phi_k^{bad},
\mathfrak N_k,
\theta_i^{bad}
\right\rangle.
}
$$

with：

- $\mathcal R_k$ = chain-normalized derivative root；
- $\mathsf T_i$ = Type-A/B；
- $\mathsf{SG}$ = spatial harmonic pass/fail；
- $\tau$ = normalized theorem time；
- $\beta$ = best chain-scale occupancy；
- $b(\cdot)$ = angular sign profile；
- $\Phi^{bad}$ = local derivative mass fraction；
- $\mathfrak N$ = spectral-cell multiplicity；
- $\theta^{bad}$ = bad-order location in section。

---

# 58. Compactness status

after bounded-coordinate compactifications：

- Type finite；
- SG binary；
- $\tau$ compact；
- $\beta\in[0,1]$；
- $b\in L^\infty(\mathbb{RP}^2)$ weak-* compact；
- $\Phi^{bad}\in[0,1]$；
- multiplicity compactified by:
  $$
  \widehat{\mathfrak N}
  =
  \mathfrak N/(1+\mathfrak N);
  $$
- bad-order coordinate in $[0,1]$。

Therefore recurrent C5-I motifs admit subsequential compactification。

---

# 59. C5-I principal theorem bundle

The main new C5-I results can be summarized：

## I-A — Sign-Core Compactness

$$
\boxed{
\text{spatial failure}
\Rightarrow
b_\ast\ge\delta.
}
$$

## I-B — Dense-Core Toll

$$
\boxed{
\text{spatial failure}
\Rightarrow
\int_{B_{r_k}}
|D^ku|^2
\gtrsim
A_k^2r_k^3.
}
$$

## I-C — Sign-Descent Bridge

$$
\boxed{
\text{spatial failure}
\Rightarrow
A_{k-1}
\gtrsim
r_kA_k.
}
$$

## I-D — Harmonic-or-Descent Dichotomy

$$
\boxed{
\text{Harmonic Pass}
\vee
\mathcal R_{k-1}
\ge
d_k\mathcal R_k.
}
$$

## I-E — Strong Ascent Forces Sparseness

$$
\boxed{
\mathcal R_k
>
d_k^{-1}
\mathcal R_{k-1}
\Rightarrow
\text{Harmonic Pass}.
}
$$

---

# 60. Relation to C5-H all-order no-go

C5-H concluded：

static all-order volumes cannot close the high-order route。

C5-I shows the missing information is not arbitrary。

Actual sign-geometry failure leaves:

$$
\boxed{
\text{an isotropically thick same-sign core}
}
$$

and simultaneously modifies the derivative-root chain。

So the correct next all-order question is no longer：

> Are high sets small enough?

It is：

> Can recurrent chain sections continually alternate between
> harmonic-pass levels and sign-thick descending-toll levels,
> while respecting Type-A/Type-B dynamics and theorem timing?

---

# 61. Remaining geometry gap

C5-I angular occupancy：

$$
b_k([\nu])
$$

records total chord occupancy，

which is enough for Solynin's extremal lower bound。

But it does NOT record:

- radial placement of active intervals；
- number of sign intervals；
- sign alternation outside selected high set；
- correlations between nearby basepoints。

Those are finer microgeometry defects。

---

# 62. Next frontier

The natural next object is not another volume measure。

It is a:

$$
\boxed{
\textbf{line-section sign process}.
}
$$

For selected bad/pass cores，

on normalized chord：

$$
s\in[-1,1],
$$

track:

$$
\boxed{
\chi_k([\nu],s)
=
1_{
V_{\lambda,k}^{j,\pm}
}
(x_k+r_ks\nu).
}
$$

This lives on:

$$
\mathbb{RP}^2\times[-1,1].
$$

Its:

- occupancy marginal；
- interval fragmentation；
- neighboring-order correlations；

can be compactified as a two-scale sign measure。

---

# 63. New frontier：C5-J

正式下一題：

$$
\boxed{
\textbf{C5-J — Line-Section Sign Processes,
Order-to-Order Descent Coupling, and Harmonic Critical Saturation}.
}
$$

---

# 64. C5-J proof obligations

## J1 — Chord sign-process measure

建立：

$$
\Gamma_k(d[\nu],ds)
$$

記錄 selected component/sign active intervals at chain scale。

## J2 — Fragmentation statistic

同 occupancy下區分：

- one long thick interval；
- many rapidly alternating intervals。

## J3 — Harmonic invariance audit

Solynin only sees total complement length；

判斷 fragmentation是否能提供 stronger harmonic measure than the extremal lower bound。

## J4 — Order-to-order chord coupling

把：

$$
D^ku
=
\nabla D^{k-1}u
$$

沿 selected coordinate的 integral relation加入 joint $k/k-1$ line process。

## J5 — Descent coefficient limit

研究：

$$
d_k(c)
$$

在 published chain constants下能否取得 usable high-order lower envelope。

## J6 — Type-A puncture density

若 Type-A string具有 persistent high-order takeover，

量化 harmonic-pass levels最低 density / placement。

## J7 — Critical saturation

若：

$$
\beta_k\downarrow\delta,
$$

研究 harmonic-measure margin與 derivative descent margin是否同時趨某 critical boundary。

## J8 — Chain-time stitching

把 different order theorem times：

$$
\tau_k
$$

和 chord processes一起放入 dynamic-interpolation state。

---

# 65. Major no-go audit

### NG-I1

$$
\text{large global high-set volume}
\Rightarrow
\text{harmonic geometry failure}.
$$

FALSE。

### NG-I2

$$
\text{geometry failure}
\Rightarrow
\text{just another Boolean defect}.
$$

FALSE；它 forces dense core + descent toll。

### NG-I3

$$
\text{Type-A}
\Rightarrow
\text{all levels geometry pass}.
$$

FALSE / not proved。

### NG-I4

$$
\text{geometry failure}
\Rightarrow
\text{Type-B theorem hypothesis}.
$$

FALSE；only adjacent descent pressure。

### NG-I5

$$
\text{same-time descent inequalities}
\Rightarrow
\text{all-order theorem-time chain inequality}.
$$

FALSE without time stitching。

### NG-I6

$$
b_\ast=\delta
\Rightarrow
\text{regularity}.
$$

FALSE；it is a boundary limit of finite-level failures。

---

# 66. X-Integration guards 更新

## G-SIGNJOINT

component and sign must stay attached to the selected derivative carrier。

## G-CHORD

harmonic geometry tracks 1D chord occupancy, not global volume。

## G-BADMAX

complete theorem spatial failure implies badness at maximal chain scale; maximal-scale badness alone does not imply complete failure。

## G-DESCLOCAL

sign-descent lemma is same-time。

## G-TIMESTITCH

cross-order iteration requires actual dynamic time control。

## G-HSAT

$\beta\to\delta$ is harmonic critical saturation, not theorem pass at finite level。

## G-TYPE

Type-A/B labels follow published Definition 3.15; do not redefine them as good/bad states。

---

# 67. True ETN 更新

C5-I state：

$$
\boxed{
\mathfrak T^{C5I}
=
\left(
\text{section type},
\text{chain root},
\text{sign geometry},
\text{harmonic occupancy},
\text{bad-core mass},
\text{multiplicity},
\text{order location},
\text{chain time}
\right).
}
$$

new transition edge：

$$
\boxed{
\text{SIGN-FAIL}_k
\longrightarrow
\text{ROOT-DESCENT}_{k\to k-1}.
}
$$

---

# 68. C5 strategic status

C5-A：

$$
\text{motif compactness}.
$$

C5-B：

$$
\text{temporal Young defects}.
$$

C5-C：

$$
\text{cross-curvature ordering}.
$$

C5-D：

$$
\text{spatial–matrix incompatibility}.
$$

C5-E：

$$
Q\to\text{gap/derivative/vorticity}.
$$

C5-F：

$$
\text{axis-pressure / derivative escalation}.
$$

C5-G：

$$
\text{fixed-order theorem-ready gate}.
$$

C5-H：

$$
\text{static all-order volume no-go}.
$$

C5-I：

$$
\boxed{
\textbf{sign geometry is now dynamically coupled to derivative-chain shape}.
}
$$

This is the first direct bridge between:

$$
\boxed{
\text{Grujić--Xu harmonic-measure geometry}
}
$$

and:

$$
\boxed{
\text{C5 recurrent derivative-chain metadata}.
}
$$

---

# 69. 正式狀態

$$
\boxed{
\begin{aligned}
\text{Definition 3.15 Type-A/B audit}
&:\ \mathrm{VERIFIED},\\
\text{Theorem 3.14 1D sign geometry audit}
&:\ \mathrm{VERIFIED},\\
\text{angular sign-core compactification}
&:\ \mathrm{PROVED},\\
\text{bad core}\Rightarrow\text{3D chain-scale thickness}
&:\ \mathrm{PROVED},\\
\text{bad core}\Rightarrow\text{local derivative }L^2\text{ toll}
&:\ \mathrm{PROVED},\\
\text{bad core count}\le\text{effective-volume multiplicity}
&:\ \mathrm{PROVED},\\
\text{sign-thick chord}\Rightarrow A_{k-1}\gtrsim r_kA_k
&:\ \mathrm{PROVED},\\
\text{normalized root descent}
&:\ \mathrm{PROVED},\\
\text{harmonic-or-descent dichotomy}
&:\ \mathrm{PROVED},\\
\text{strong adjacent ascent}\Rightarrow\text{spatial pass}
&:\ \mathrm{PROVED},\\
\text{same-time Type-A puncture criterion}
&:\ \mathrm{PROVED},\\
\text{Type-A/B full dynamic closure}
&:\ \mathrm{EXTERNAL\ THEOREM\ FRAMEWORK},\\
\text{cross-order theorem-time stitching}
&:\ \mathrm{OPEN/NEXT},\\
\text{global regularity}
&:\ \mathrm{OPEN}.
\end{aligned}
}
$$

---

# 70. 結論

C5-H告訴我們：

$$
\boxed{
\text{high-order asymptotic criticality不能靠 volume-only route恢復}.
}
$$

C5-I現在真正進入 published mechanism使用的：

$$
\boxed{
\textbf{component/sign 1D microgeometry}.
}
$$

如果 level $k$ spatial condition pass，

某 line上的 active occupancy：

$$
\le\delta,
$$

Solynin harmonic-measure lower bound和 analytic extension提供 theorem contraction。

如果 spatial condition fail，

則存在 chain-scale bad core：

$$
\boxed{
b_k([\nu])>\delta
\quad
\forall[\nu].
}
$$

這個 bad core不是免費 escape。

它先產生：

$$
\boxed{
\int_{B_{r_k}}
|D^ku|^2
\gtrsim
A_k^2r_k^3,
}
$$

再利用：

$$
D^\zeta u
=
\partial_q
D^{\zeta-e_q}u
$$

和 theorem threshold：

$$
\delta>
\frac1{1+\lambda},
$$

強迫：

$$
\boxed{
A_{k-1}
\ge
((1+\lambda)\delta-1)
r_kA_k.
}
$$

於 chain scale：

$$
\boxed{
\mathcal R(k-1,c,s)
\ge
d_k(c)
\mathcal R(k,c,s).
}
$$

所以每個 high-order level都有：

$$
\boxed{
\textbf{Harmonic Pass}
\vee
\textbf{Descending-Root Toll}.
}
$$

反過來：

$$
\boxed{
\text{strong adjacent root ascent}
\Rightarrow
\text{sign-sparseness pass}.
}
$$

這使 C5 第一次真正把：

$$
\boxed{
\text{harmonic-measure geometry}
}
$$

與：

$$
\boxed{
\text{ascending/descending chain}
}
$$

接成同一個 causal compatibility network。

但不同 derivative orders的 theorem-admissible later times一般不同。

所以不能把 same-time inequalities偷偷乘成 all-order contradiction。

這個剩餘 timing/line-process問題正是下一輪：

$$
\boxed{
\textbf{C5-J — Line-Section Sign Processes,
Order-to-Order Descent Coupling,
and Harmonic Critical Saturation}.
}
$$

---

# References

1. Z. Grujić, L. Xu, *Asymptotic Criticality of the Navier–Stokes Regularity Problem*, Journal of Mathematical Fluid Mechanics 26, Article 53 (2024), DOI: 10.1007/s00021-024-00888-x; arXiv:1911.00974.
2. Z. Grujić, *A geometric measure-type regularity criterion for solutions to the 3D Navier–Stokes equations*, Nonlinearity 26 (2013), 289–296; arXiv:1111.0217.
3. T. Ransford, *Potential Theory in the Complex Plane*, London Mathematical Society Student Texts 28, Cambridge University Press (1995).
4. A. Y. Solynin, *Ordering of sets, hyperbolic metrics, and harmonic measure*, Journal of Mathematical Sciences 95 (1999), 2256.
5. R. Guberović, *Smoothness of Koch–Tataru solutions to the Navier–Stokes equations revisited*, Discrete and Continuous Dynamical Systems 27 (2010), 231–236.

# Internal dependencies

- `NS_C5H_AllOrder_EffectiveVolume_AsymptoticCriticality_v0.1.md`
- `NS_C5G_PressureSignature_VorticityComplement_FixedOrderGate_v0.1.md`
- `NS_C5F_AxisPressureSignature_DerivativeGateEscalation_v0.1.md`
- `NS_C5E_StrainDirection_MiddleGap_DerivativeIntermittency_v0.1.md`
- `NS_C5D_SpatialMatrix_StrongMiddleQuadraticPressureObstruction_v0.1.md`
- `NS_C5C_TemporalCorrelation_CrossCurvatureOrdering_v0.1.md`
- `NS_C5B_TemporalYoung_PulsePhaseCompatibility_v0.1.md`
- `NS_C5A_RecordWindow_MotifCompactness_v0.1.md`
- `NS_C4J_CompensationRigidity_FinalSynchronizationAudit_v0.1.md`
- `True ETN / 無限維張力場`
- `X_Integral_Unified_Program_v0.2.md`

Next:

$$
\boxed{
\textbf{C5-J — Line-Section Sign Processes,
Order-to-Order Descent Coupling,
and Harmonic Critical Saturation}
}
$$
