---
title: "Navier–Stokes C3-T：Pressure-Support Diversification、Cone-to-Eigenvalue Barrier 與 Hereditary-Ancestry Gap"
subtitle: "Quantitative Pressure Diversification, the Barrier from Five-Dimensional Mean-Strain Cones to Pointwise Middle-Eigenvalue Geometry, and the Missing Hereditary Lemma for Pressure-Poor Causal Rays"
version: "v0.1"
date: "2026-08-14"
author: "Neo.K / EveMissLab"
language: "zh-TW"
status: "Theorem-style structural reduction / no-go note"
epistemic_status: "Finite-dimensional matrix geometry + inherited pressure/enstrophy estimates + causal-tree selection no-go. Does NOT prove Navier–Stokes regularity."
---

# Navier–Stokes C3-T
# Pressure-Support Diversification、Cone-to-Eigenvalue Barrier 與 Hereditary-Ancestry Gap

## 0. 本輪定位

C3-S 已把 multi-core strain geometry壓成兩個 branch：

$$
\boxed{
\text{uniform strain cone}
\quad\vee\quad
\text{cone degeneration}.
}
$$

Uniform branch中，normalized local mean strains

$$
v_{n,i}
=
\frac{M_{n,i}}{|M_{n,i}|}
\in
S^4
\subset
\operatorname{Sym}_0(3)
$$

最終滿足

$$
K_\ast:v_{n,i}
\ge
\gamma_0>0.
$$

Degenerate branch中，

$$
\gamma_n
=
\operatorname{dist}
\left(
0,\operatorname{conv}V_n
\right)
\to0,
$$

並可抽至多六核 witness。

本輪處理兩個未閉合問題：

1. fixed 5D cone motif能否直接接 Miller 的 $\lambda_2^+$ geometry？
2. 每尺度都有 pressure-poor six-core witness，能否抽出一條 pressure-poor causal ancestry ray？

兩者答案都是：

$$
\boxed{
\textbf{不能直接。}
}
$$

但兩個 no-go 都能轉成精確的新 proof obligation。

---

# 1. 五維 matrix cone與 eigenvalue signature

令

$$
\mathbb S_0
=
\operatorname{Sym}_0(3).
$$

取任意

$$
K\in\mathbb S_0,
\qquad
|K|=1.
$$

令其 eigenvalues

$$
\kappa_1\le\kappa_2\le\kappa_3.
$$

因 trace-free 且 nonzero：

$$
\boxed{
\kappa_1<0<\kappa_3.
}
$$

---

# 2. Two-stretching test matrix

在 $K$ 的 eigenbasis中定義

$$
\boxed{
V^+
=
\frac1{\sqrt6}
\operatorname{diag}(-2,1,1).
}
$$

則

$$
|V^+|=1,
$$

且

$$
\boxed{
\lambda_2(V^+)
=
\frac1{\sqrt6}>0.
}
$$

同時

$$
K:V^+
=
-\frac{3\kappa_1}{\sqrt6}
>0.
$$

---

# 3. One-stretching test matrix

定義

$$
\boxed{
V^-
=
\frac1{\sqrt6}
\operatorname{diag}(-1,-1,2).
}
$$

則

$$
|V^-|=1,
$$

且

$$
\boxed{
\lambda_2(V^-)
=
-\frac1{\sqrt6}<0.
}
$$

同時

$$
K:V^-
=
\frac{3\kappa_3}{\sqrt6}
>0.
$$

---

# 4. C3-T.1：Half-Space Signature Non-Rigidity

## 定理 4.1

對任意 nonzero

$$
K\in\operatorname{Sym}_0(3),
$$

open half-space

$$
\mathcal H_K^+
=
\{
M:
K:M>0
\}
$$

同時包含：

$$
\lambda_2(M)>0
$$

與

$$
\lambda_2(M)<0
$$

的 trace-free symmetric matrices。

因此

$$
\boxed{
\text{fixed 5D strain half-space}
\not\Rightarrow
\text{middle-eigenvalue sign}.
}
$$

---

# 5. Narrow-cone eigenvalue inheritance

若

$$
K,V\in\mathbb S_0,
\qquad
|K|=|V|=1,
$$

且

$$
K:V\ge\gamma,
$$

則

$$
|V-K|_F^2
=
2-2K:V
\le
2(1-\gamma).
$$

所以

$$
\boxed{
|V-K|_F
\le
\sqrt{2(1-\gamma)}.
}
$$

Weyl inequality給

$$
|\lambda_2(V)-\lambda_2(K)|
\le
\|V-K\|_{\rm op}
\le
\|V-K\|_F.
$$

因此：

## 定理 5.1

$$
\boxed{
\lambda_2(V)
\ge
\lambda_2(K)
-
\sqrt{2(1-\gamma)}.
}
$$

以及

$$
\boxed{
\lambda_2(V)
\le
\lambda_2(K)
+
\sqrt{2(1-\gamma)}.
}
$$

若

$$
\boxed{
\lambda_2(K)
>
\sqrt{2(1-\gamma)},
}
$$

則

$$
\lambda_2(V)>0.
$$

若

$$
\boxed{
\lambda_2(K)
<
-\sqrt{2(1-\gamma)},
}
$$

則

$$
\lambda_2(V)<0.
$$

---

# 6. Uniform-cone branch的新分裂

因此 C3-S 的 uniform branch再分：

## T-A1 — Narrow nondegenerate cone

$$
\boxed{
|\lambda_2(K_\ast)|
>
\sqrt{2(1-\gamma_0)}.
}
$$

mean-strain directions的 $\lambda_2$ sign被鎖定。

## T-A2 — Wide / eigenvalue-degenerate cone

$$
\boxed{
|\lambda_2(K_\ast)|
\le
\sqrt{2(1-\gamma_0)}.
}
$$

cone coherence不足以決定 middle-eigenvalue sign。

---

# 7. 但這仍只是 mean strain

local mean strain：

$$
M_i
=
\int\chi_iS\,dx.
$$

若

$$
m_i
=
\int\chi_i\,dx>0,
$$

定義

$$
\overline S_i
=
\frac{M_i}{m_i}.
$$

它與 $M_i$ 有相同 normalized matrix direction與 eigenvalue sign。

但 Miller 的 criterion使用的是 pointwise/spatial norm：

$$
\lambda_2^+(S(x,t)),
$$

不是

$$
\lambda_2(\overline S_i).
$$

---

# 8. C3-T.2：Mean-to-Pointwise Middle-Eigenvalue No-Go

取

$$
A
=
\operatorname{diag}(2,-1,-1),
$$

$$
B
=
\operatorname{diag}(-1,2,-1).
$$

兩者都有

$$
\lambda_2(A)=\lambda_2(B)=-1<0.
$$

但

$$
\frac{A+B}{2}
=
\operatorname{diag}
\left(
\frac12,
\frac12,
-1
\right),
$$

所以

$$
\boxed{
\lambda_2
\left(
\frac{A+B}{2}
\right)
=
\frac12>0.
}
$$

因此：

$$
\boxed{
\text{mean }\lambda_2>0
\not\Rightarrow
\text{pointwise }\lambda_2>0.
}
$$

---

# 9. Mean-to-pointwise upgrade需要 fluctuation control

Weyl給：

$$
\lambda_2(S(x))
\ge
\lambda_2(\overline S_i)
-
\|S(x)-\overline S_i\|_{\rm op}.
$$

所以若

$$
\lambda_2(\overline S_i)>0
$$

且

$$
\boxed{
\|S-\overline S_i\|_{L^\infty(C_i),op}
<
\lambda_2(\overline S_i),
}
$$

則 pointwise：

$$
\boxed{
\lambda_2(S(x))>0
}
$$

on the core。

目前 ancestry route沒有這種 uniform fluctuation theorem。

---

# 10. Cone degeneration回顧

現在取

$$
\gamma_n\to0.
$$

每尺度有至多六核 witness

$$
v_{n,i_1},\ldots,v_{n,i_r},
\qquad
r\le6,
$$

與 weights

$$
\alpha_j\ge0,
\qquad
\sum_j\alpha_j=1,
$$

使

$$
\left|
\sum_{j=1}^{r}
\alpha_jv_{n,i_j}
\right|
=
\gamma_n.
$$

---

# 11. Common pressure efficiency bound

對任意 unit common far-pressure direction

$$
K_H,
$$

witness中至少一核

$$
i_\ast
$$

滿足

$$
\boxed{
K_H:v_{n,i_\ast}
\le
\gamma_n.
}
$$

因此若 actual common far matrix仍要對所有 cores有 uniform efficiency

$$
\eta_0>0,
$$

必須

$$
\boxed{
\gamma_n\ge\eta_0.
}
$$

所以

$$
\boxed{
\gamma_n\to0
}
$$

自動排除 uniform common-pressure efficiency。

---

# 12. Enstrophy補償 route

C3-S 已有：

若 witness全部要求 fixed normalized common far-pressure work

$$
b_0>0,
$$

則

$$
\boxed{
\mathfrak E_{R_n}
\gtrsim
b_0^{2/3}
\kappa_n^2
\gamma_n^{-2/3}.
}
$$

所以 cone degeneration的 pressure-side survivor只有：

## T-B1 — Enstrophy compensation

$$
\mathfrak E_{R_n}
$$

以至少上述 rate增長。

## T-B2 — Pressure-support diversification

至少一個 witness core不再由 common far matrix提供 fixed support。

---

# 13. Alternative-support lower bound

令某 witness core的 normalized required correction/growth demand：

$$
G_i^{req}>0.
$$

分解：

$$
G_i^{req}
=
P_i^{common}
+
A_i^{alt},
$$

其中

- $P_i^{common}$ = common far pressure；
- $A_i^{alt}$ = bulk SSA / near pressure / Betchov / projected operator / other channels。

對 weak-pressure core：

$$
P_i^{common}
\le
C
\gamma
\kappa^{-3}
\mathfrak E_R^{3/2}.
$$

所以：

## 定理 13.1

若

$$
G_i^{req}\ge g_0>0,
$$

則

$$
\boxed{
A_i^{alt}
\ge
g_0
-
C
\gamma
\kappa^{-3}
\mathfrak E_R^{3/2}.
}
$$

若右側 common-pressure bound不超過 $g_0/2$，則

$$
\boxed{
A_i^{alt}
\ge
\frac12g_0.
}
$$

這就是：

$$
\boxed{
\textbf{Pressure-Support Diversification Lower Bound}.
}
$$

---

# 14. Pressure-poor per-level witness

固定 threshold：

$$
\eta_0>0.
$$

稱 core 為 pressure-poor，若 common far-pressure efficiency：

$$
\eta_H\le\eta_0.
$$

當

$$
\gamma_n\to0,
$$

任意 fixed $\eta_0$ 下，

所有 sufficiently large scales都有至少一個 pressure-poor witness core。

---

# 15. 但 per-level witness ≠ causal ray

考慮 infinite rooted binary tree。

在 depth $n\ge1$ 只 mark：

$$
\boxed{
0^{n-1}1.
}
$$

則：

- 每一 depth都有 marked node；
- tree locally finite；
- 但沒有 infinite all-marked ray。

因此：

## No-Go 15.1

$$
\boxed{
\text{每尺度都有 pressure-poor core}
\not\Rightarrow
\text{存在 pressure-poor causal ancestry ray}.
}
$$

---

# 16. C3-T.3：Hereditary Pressure-Poor Ray Criterion

令 $\mathcal T$ 為 locally finite causal ancestry tree。

令 $\mathcal P$ 為 pressure-poor nodes。

若存在 $v_0\in\mathcal P$，且每個 $v\in\mathcal P$ 都有至少一個 pressure-poor child，

則存在 infinite pressure-poor causal ray：

$$
\boxed{
v_0\to v_1\to v_2\to\cdots,
\qquad
v_n\in\mathcal P.
}
$$

更一般地，若存在 fixed $L$，使每個 pressure-poor node都有一個 pressure-poor descendant在 $1,\ldots,L$ generations內，

則存在 bounded-generation-gap infinite pressure-poor ancestry subsequence。

---

# 17. 真正 missing lemma

因此 degenerate branch若要真正剝離 far-pressure channel，

需要：

$$
\boxed{
\textbf{Pressure-Poor Heredity Lemma}.
}
$$

候選形式：

$$
\boxed{
\eta_H(parent)\ll1
+
\text{local source dominance}
\Rightarrow
\exists child:
\eta_H(child)\lesssim
\eta_H(parent)+\varepsilon.
}
$$

或 bounded-generation版本。

目前：

$$
\boxed{\text{OPEN}.}
$$

---

# 18. 為何 pressure-poor 未必 hereditary？

child會改變：

- spatial center；
- pressure near/far split；
- far matrix orientation；
- local mean strain；
- merger status；
- local pressure source。

所以

$$
\eta_{H,parent}\ll1
$$

不自動推出

$$
\eta_{H,child}\ll1.
$$

這是 dynamical geometry gap。

---

# 19. Uniform cone motif與 Miller operator escape

uniform cone只控制：

$$
M_i
=
\int\chi_iS.
$$

這是五個 scalar first moments。

但 Miller operator：

$$
\mathcal Q_{SV}
$$

依賴：

- spatial derivatives；
- quadratic fluctuations；
- vorticity；
- advection；
- nonlocal projection。

因此 mean-strain cone無法一般地控制 operator escape。

---

# 20. C3-T.4：Mean-Motif / Operator-Fluctuation Separation No-Go

mean map

$$
S
\mapsto
M_\chi(S)
=
\int\chi S\,dx
$$

只有五個 scalar outputs。

其 kernel

$$
\left\{
W:
\int\chi W\,dx=0
\right\}
$$

是 infinite-dimensional。

因此可在保持 $M_\chi$ 不變的情況下加入 oscillatory zero-mean fluctuations。

這些 fluctuations可以改變：

- $\Delta S$；
- $S^2$；
- $\omega$；
- $\mathcal Q_{SV}$；

但不改 mean-strain cone data。

因此：

$$
\boxed{
\text{fixed mean-strain motif}
\not\Rightarrow
\text{small Miller operator defect}.
}
$$

此為 information-level no-go，不是 N–S counterexample construction。

---

# 21. Fixed cone與 operator escape可以共存

所以：

$$
\boxed{
\gamma_n\ge\gamma_0
}
$$

和：

$$
\boxed{
d_{SV}(t_n)\gtrsim1
}
$$

目前完全相容。

operator escape可藏在：

$$
\boxed{
\text{zero-mean/high-frequency fluctuations around a coherent mean motif}.
}
$$

---

# 22. Fixed pressure motif

若 actual common far-pressure directions

$$
K_n^H
$$

也有 uniform efficiency，

compactness of $S^4$給 subsequence：

$$
K_n^H\to K_H^\ast.
$$

所以 uniform branch可形成兩個 fixed matrix motifs：

$$
K_\ast^{cone},
\qquad
K_\ast^{pressure}.
$$

兩者不必相同。

定義 angle：

$$
\vartheta_\ast
=
\arccos
\left(
K_\ast^{pressure}
:
K_\ast^{cone}
\right).
$$

目前沒有 theorem固定此角度。

---

# 23. Uniform cone branch的新 subbranches

由 narrow-cone theorem：

## T-C1 — Positive-middle narrow mean motif

$$
\lambda_2(K_\ast)
>
\sqrt{2(1-\gamma_0)}.
$$

所有 normalized mean strains：

$$
\lambda_2(v_i)>0.
$$

## T-C2 — Negative-middle narrow mean motif

$$
\lambda_2(K_\ast)
<
-\sqrt{2(1-\gamma_0)}.
$$

所有 normalized mean strains：

$$
\lambda_2(v_i)<0.
$$

## T-C3 — Wide / degenerate motif

其餘。

三者都仍需 pointwise fluctuation control才能接 Miller criterion。

---

# 24. Mean fluctuation ratio

定義：

$$
\boxed{
\mathfrak F_i
=
\frac{
\|S-\overline S_i\|_{L^\infty(C_i),op}
}{
|\overline S_i|
}
}
$$

在 $\overline S_i\ne0$ 時。

若 normalized mean有：

$$
\lambda_2
\left(
\frac{\overline S_i}{|\overline S_i|}
\right)
\ge\delta>0
$$

且：

$$
\mathfrak F_i<\delta,
$$

則 Weyl給：

$$
\boxed{
\lambda_2(S(x))>0
}
$$

on the core。

目前沒有 uniform theorem給：

$$
\mathfrak F_i<\delta.
$$

---

# 25. C3-T survivor map

## Branch T-U — Uniform cone

$$
\gamma_n\ge\gamma_0.
$$

剩餘 debt：

$$
\boxed{
\text{mean-to-pointwise fluctuation}
+
\text{operator fluctuation}.
}
$$

## Branch T-D — Cone degeneration

$$
\gamma_n\to0.
$$

剩餘 debt：

$$
\boxed{
\text{enstrophy compensation}
\quad\vee\quad
\text{pressure-support diversification}.
}
$$

若要抽一條 pressure-poor ray，

還需：

$$
\boxed{
\text{pressure-poor heredity}.
}
$$

---

# 26. Major no-go

### NG-T1

$$
\text{fixed strain half-space}
\Rightarrow
\lambda_2\text{ fixed sign}.
$$

FALSE。

### NG-T2

$$
\text{mean }\lambda_2>0
\Rightarrow
\text{pointwise }\lambda_2>0.
$$

FALSE。

### NG-T3

$$
\text{pressure-poor node every scale}
\Rightarrow
\text{pressure-poor causal ray}.
$$

FALSE。

### NG-T4

$$
\text{fixed mean motif}
\Rightarrow
\text{small Miller operator escape}.
$$

FALSE / information insufficient。

### NG-T5

$$
\gamma\to0
\Rightarrow
\text{far pressure irrelevant}.
$$

FALSE。

enstrophy can compensate or support can diversify。

---

# 27. X-Integration guards

## G-MEAN/PT

$$
\boxed{
\text{mean strain}
\neq
\text{pointwise strain}.
}
$$

## G-EIGGAP

narrow cone若要推 eigenvalue sign，

需檢查：

$$
|\lambda_2(K_\ast)|
>
\sqrt{2(1-\gamma)}.
$$

## G-FLUCT

若要接 pointwise criterion，

保存：

$$
\mathfrak F_i.
$$

## G-PPOOR

six-core witness輸出 pressure-poor node，

但不得自動標成下一代 pressure-poor ancestor。

## G-HERED

pressure-poor causal ray需要 hereditary / bounded-gap inheritance。

## G-MEANOP

mean motif不得用來控制 operator fluctuation。

---

# 28. True ETN 更新

uniform branch：

$$
\Theta_n^{motif}
=
\left\langle
K_\ast,
\gamma_0,
\lambda_2(K_\ast),
\{\mathfrak F_i\},
d_{SV},
K_H^\ast,
\operatorname{Prov}
\right\rangle.
$$

degenerate branch：

$$
\Theta_n^{div}
=
\left\langle
\gamma_n,
\text{six-core witness},
\eta_{\min,n},
\mathfrak E_{R_n},
\text{alternative support},
\operatorname{HereditaryFlag}
\right\rangle.
$$

---

# 29. 新 frontier：C3-U

正式下一題：

$$
\boxed{
\textbf{C3-U — Hereditary Pressure-Poor Ancestry and Mean-to-Pointwise Strain Rigidity}.
}
$$

---

# 30. C3-U proof obligations

## U1 — Pressure-poor heredity

證或否證：

$$
\eta_H(parent)\ll1
+
\text{local source dominance}
\Rightarrow
\exists child:
\eta_H(child)\lesssim
\eta_H(parent)+\varepsilon.
$$

## U2 — Bounded-generation heredity

若 one-step太強，

測：

$$
\exists L<\infty:
\text{poor parent}
\Rightarrow
\text{poor descendant within }L\text{ generations}.
$$

## U3 — Far-pressure matrix transport

研究：

$$
H_n\to H_{n+1}
$$

的 scale-invariant variation。

## U4 — Mean-strain transport

研究：

$$
M_{parent}\to M_{child}
$$

的 local equation bound。

## U5 — Mean fluctuation control

尋找：

$$
\mathfrak F_i
$$

的 bound或證 no-go。

## U6 — Narrow-cone pointwise branch

cone eigen-gap + fluctuation smallness接 Miller middle-eigenvalue criterion。

## U7 — Operator fluctuation branch

若 fluctuation不能 small，

轉成 Miller operator escape / critical moment / extra core multiplicity。

## U8 — Pressure-poor ray closure

若 U1/U2成功，

從 cone-degeneration branch抽：

$$
\boxed{
\text{one causal ancestry ray
with asymptotically weak common far-pressure support}.
}
$$

---

# 31. 正式狀態

$$
\boxed{
\begin{aligned}
\text{half-space contains both middle-eigenvalue signatures}
&:\ \mathrm{PROVED},\\
\text{narrow-cone eigenvalue inheritance}
&:\ \mathrm{PROVED},\\
\text{fixed cone}\Rightarrow\lambda_2\text{ sign}
&:\ \mathrm{FALSE\ in\ general},\\
\text{mean }\lambda_2\Rightarrow\text{pointwise }\lambda_2
&:\ \mathrm{FALSE/NO\mbox{-}GO},\\
\text{mean-to-pointwise upgrade under fluctuation gap}
&:\ \mathrm{PROVED\ CONDITIONAL},\\
\gamma\to0\Rightarrow\text{no uniform common-pressure efficiency}
&:\ \mathrm{PROVED},\\
\text{pressure-support diversification lower bound}
&:\ \mathrm{PROVED},\\
\text{per-level pressure-poor witness}
&:\ \mathrm{PROVED},\\
\text{per-level witness}\Rightarrow\text{pressure-poor ray}
&:\ \mathrm{FALSE/NO\mbox{-}GO},\\
\text{hereditary pressure-poor ray criterion}
&:\ \mathrm{PROVED\ COMBINATORIAL},\\
\text{pressure-poor heredity for N--S dynamics}
&:\ \mathrm{OPEN},\\
\text{mean motif controls Miller operator escape}
&:\ \mathrm{FALSE/INFORMATION\ NO\mbox{-}GO},\\
\text{mean-to-pointwise / hereditary rigidity}
&:\ \mathrm{OPEN}.
\end{aligned}
}
$$

---

# 32. 結論

C3-S 留下：

$$
\text{uniform cone}
\quad\vee\quad
\text{cone degeneration}.
$$

C3-T 現在證明兩支各有一個更深 type gap。

Uniform cone中：

$$
\boxed{
\text{5D half-space coherence}
\not\Rightarrow
\lambda_2^+\text{ geometry}.
}
$$

只有窄 cone + eigenvalue gap才鎖 mean sign，

而 mean sign仍不等於 pointwise sign。

Degenerate branch中：

$$
\boxed{
\text{每尺度都有 common-pressure weak core}
}
$$

不等於：

$$
\boxed{
\text{存在 pressure-poor causal ray}.
}
$$

真正缺的是 heredity。

所以現在下一步不再是更多 convex geometry，

而是：

$$
\boxed{
\textbf{C3-U — Hereditary Pressure-Poor Ancestry and Mean-to-Pointwise Strain Rigidity}.
}
$$

---

# References

1. E. Miller, *A regularity criterion for the Navier–Stokes equation involving only the middle eigenvalue of the strain tensor*, arXiv:1710.05569; Arch. Rational Mech. Anal. 235 (2020).
2. E. Miller, *On the interaction of strain and vorticity for solutions of the Navier–Stokes equation*, arXiv:2407.02691; Pure and Applied Analysis 8 (2026).
3. Z. Bradshaw, T.-P. Tsai, *On the local pressure expansion for the Navier–Stokes equations*, arXiv:2001.11526.
4. T. Barker, C. Prange, *Quantitative regularity for the Navier–Stokes equations via spatial concentration*, arXiv:2003.06717.

# Internal dependencies

- `NS_C3S_StrainConeMargin_MergerRigidity_v0.1.md`
- `NS_C3R_MultiCore_PressureHorizon_StrainConvexity_v0.1.md`
- `NS_C3Q_PressureProjection_OperatorLocalization_v0.1.md`
- `NS_C3P_OperatorEscape_FarPressureMatrix_v0.1.md`
- `NS_C3O_AdjointCore_BalanceDynamicsSeparation_v0.1.md`
- `NS_C3M_VorticityStrain_Betchov_GeometryDebt_v0.1.md`
- `True ETN / 無限維張力場`
- `X_Integral_Unified_Program_v0.2.md`

Next:

$$
\boxed{
\textbf{C3-U — Hereditary Pressure-Poor Ancestry and Mean-to-Pointwise Strain Rigidity}
}
$$
