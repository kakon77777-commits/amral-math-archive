---
title: "Navier–Stokes C5-F：Compressive-Axis Robustness、Pressure-Signature Locking 與 Derivative-Gate Escalation"
subtitle: "Middle-Gap Limits Preserve the Compressive Axis; Nondegenerate Q-Cancellation Forces Axis Dispersion; Strong Common Far Pressure Can Conflict with It"
version: "v0.1"
date: "2026-08-15"
author: "Neo.K / EveMissLab"
language: "zh-TW"
status: "Theorem-style strain/vorticity defect coupling / axis-pressure incompatibility / derivative-gate audit"
epistemic_status: "Exact trace-free spectral algebra + finite-dimensional axis-cap half-space theorem + pressure-signature geometry + vorticity projection/complement dichotomy + conditional scaling interface to published derivative-sparseness criteria. Does NOT prove Navier–Stokes regularity."
---

# Navier–Stokes C5-F
# Compressive-Axis Robustness、Pressure-Signature Locking 與 Derivative-Gate Escalation

## 0. 本輪定位

C5-E 已把 recurrent Seven-Point quadratic cancellation完全翻譯成 PDE field defects：

$$
\boxed{
Q\text{-Cancellation}
\Rightarrow
\text{Middle-Gap/Cubic Intermittency}
\vee
\text{Strain-Derivative Fluctuation}
\vee
\text{Vorticity-Dominant Leakage}.
}
$$

同時 C5-D 有 common far-pressure convex geometry：

$$
\boxed{
G(e_1)
=
e_1\otimes e_1-\frac13I,
}
$$

以及：

$$
\boxed{
0\in\operatorname{conv}\{G(e_i)\}
\Rightarrow
\text{one common far-pressure matrix cannot compensate all cores}.
}
$$

C5-F 的問題：

1. middle-gap degeneration：
   $$
   \lambda_2/|S|\to0
   $$
   是否會讓 compressive-axis pressure geometry消失？
2. Q-cancellation 所需 strain-direction dispersion，
   是否真的需要最壓縮 eigenvector分散？
3. common far-pressure compensation是否能強迫 axis locking，
   並和 Q-cancellation形成第二個 finite-dimensional incompatibility？
4. vorticity leakage究竟會回到 Miller operator還是 constraint complement？
5. strain-derivative / cubic-intermittency pre-gates能否真正靠近 Grujić–Xu published theorem尺度？
6. 若 fixed derivative levels一直失敗，是否真的被迫：
   $$
   k_j\to\infty?
   $$

本輪主要結果：

1. positive-middle normalized strain的 most-compressive eigenvalue具有 uniform spectral gap：
   $$
   \boxed{
   \lambda_2-\lambda_1\ge1/\sqrt2;
   }
   $$
2. 因此 compressive-axis projector在整個 positive-middle sector，
   包括 middle-gap boundary，
   都是穩定 metadata；
3. middle-gap degeneration只把 eigenvalue shape推向：
   $$
   (-1/\sqrt2,0,1/\sqrt2),
   $$
   不會 erase $e_1$；
4. 若：
   $$
   \vartheta\ge\delta>0
   $$
   且 compressive axes都在 sufficiently narrow common cap，
   所有 local quadratic directions仍落在一個 common strict half-space；
5. 因此：
   $$
   \boxed{
   Q\text{-cancellation}
   +
   \text{nondegenerate middle gap}
   \Rightarrow
   \textbf{compressive-axis dispersion};
   }
   $$
6. 只轉動 $e_2/e_3$、保持 $e_1$ fixed，
   不能支撐 Q zero barycenter；
7. common far-pressure matrix若 signature為：
   $$
   (-,+,+)
   $$
   且 negative compensation margin夠強，
   會把 compressive axes鎖進一個 projective cap；
8. 若該 cap窄於 Q-cancellation要求的 axis-dispersion scale，
   二者 incompatibility；
9. 所以 nondegenerate-gap Q-cancellation若仍和 common far pressure共存，
   必逃向：
   - weak pressure margin；
   - two-negative-eigenvalue far matrix；
   - pressure-source fragmentation；
   - mean rotation；
10. middle-gap degeneration仍保留 common pressure-axis constraint；
11. vorticity-dominant leakage強迫：
    $$
    \boxed{
    P_{st}(\omega\otimes\omega)
    \text{ congestion}
    \vee
    P_{st}^{\perp}(\omega\otimes\omega)
    \text{ constraint-complement congestion};
    }
    $$
12. strain-derivative stock直接產生 scale-critical $D^2u$ pointwise amplitude somewhere；
13. middle-gap cubic intermittency在 NS-rescaled variables中的 sparse-scale exponent：
    $$
    2/3
    $$
    比 fixed-$k=1$ direct velocity regularity scale exponent：
    $$
    3/5
    $$
    更 favorable；
14. 但 raw $Du$ component/sign theorem interface仍可能被 vorticity geometry阻塞；
15. derivative-order escalation不是自動 theorem：
    任意 best-order sequence只有：
    $$
    \boxed{
    \text{fixed-order recurrent defect}
    \vee
    k_j\to\infty;
    }
    $$
16. $k_j\to\infty$使 Grujić–Xu scaling burden asymptotically vanish，
    但不自動滿足 component/sign、analytic-time與 chain hypotheses；
17. 因此 C5-F 把 residual壓成：
    $$
    \boxed{
    \text{Axis/Pressure Signature Defect}
    \vee
    \text{Vorticity Projection Defect}
    \vee
    \text{Fixed-Order Gate Defect}
    \vee
    \text{Derivative-Order Escape}.
    }
    $$

---

# 1. Fresh primary-source audit

本輪重新核對三個 theorem-level anchors。

## 1.1 Miller 2026

Miller 定義：

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
\right),
}
$$

並證若 finite-time blow-up：

$$
\boxed{
\limsup_{t\uparrow T_\ast}
\frac{
\|\mathcal Q_{SV}(t)\|_2
}{
\|-\Delta S(t)\|_2
}
\ge1.
}
$$

其新 identity：

$$
\boxed{
\langle-\Delta S,\omega\otimes\omega\rangle=0
}
$$

繼續提供 vorticity-quadratic operator channel與 growth direction的 orthogonality anchor。

## 1.2 Grujić–Xu 2024

正式：

$$
\boxed{
\text{J. Math. Fluid Mech. 26, 53 (2024)}.
}
$$

Theorem 3.5：

對 fixed derivative order $k$，

若在 escape time後 appropriate later time，

selected：

$$
D^ku
$$

或：

$$
D^k\omega
$$

component/sign superlevel set在 scale：

$$
\boxed{
\rho
\lesssim
\|D^ku\|_\infty^{-3/(2k+3)}
}
$$

for velocity in $d=3$，

或 corresponding vorticity scale，

呈 1D sparse，

則 regularity延伸過 potential blow-up time。

Theorem 3.14：

在 derivative-chain / analyticity framework中，

regularity scale提升到：

$$
\boxed{
\rho
\lesssim
\|D^ku\|_\infty^{-1/(k+1)}
}
$$

velocity route，

且 scaling gap asymptotically vanishes as：

$$
k\to\infty.
$$

### Guard

C5-F只作 theorem-interface audit，

不把 strain/vorticity pre-gates直接宣稱成 published theorem hypotheses。

## 1.3 Bradshaw–Tsai

whole-space pressure local expansion提供：

- local pressure；
- far contribution；
- harmonic far-field provenance；

的 rigorous foundation。

所以 C5-D/F 的 common far-pressure matrix只在：

$$
\boxed{
\text{common far-field dominance已另外證明}
}
$$

時使用。

---

# 2. Positive-middle normalized eigenvalue algebra

取：

$$
K\in\operatorname{Sym}_0(3),
\qquad
|K|_F=1.
$$

ordered eigenvalues：

$$
k_1\le k_2\le k_3.
$$

假設：

$$
\boxed{
k_2\ge0.
}
$$

定義：

$$
\boxed{
\vartheta(K)
=
k_2k_3.
}
$$

C5-D：

$$
\boxed{
k_1^2
=
\frac12+\vartheta.
}
$$

---

# 3. C5-F.1：Uniform Compressive Spectral Gap

因：

$$
\vartheta\ge0,
$$

$$
|k_1|
\ge
\frac1{\sqrt2}.
$$

且：

$$
k_1<0,
\qquad
k_2\ge0.
$$

所以：

$$
\boxed{
k_2-k_1
\ge
\frac1{\sqrt2}.
}
$$

### 結論

most-compressive eigenvalue：

$$
k_1
$$

在整個 positive-middle closed sector：

$$
k_2\ge0
$$

都是 uniformly simple。

---

# 4. Compressive-axis projector

令：

$$
\boxed{
P_1(K)
=
e_1(K)\otimes e_1(K)
}
$$

為 $k_1$ spectral projector。

因 uniform gap：

$$
\ge1/\sqrt2,
$$

標準 finite-dimensional spectral perturbation estimate給：

$$
\boxed{
\|P_1(K)-P_1(L)\|_F
\le
C
\|K-L\|_F
}
$$

對 positive-middle normalized sector中的 sufficiently close：

$$
K,L,
$$

其中 $C$ 可取 universal。

### 意義

$$
\boxed{
\textbf{compressive axis is robust even when the middle gap degenerates}.
}
$$

---

# 5. Middle-gap boundary shape

若：

$$
K_j
$$

normalized positive-middle，

且：

$$
\vartheta(K_j)\to0,
$$

則：

$$
k_{1,j}^2
=
\frac12+\vartheta_j
\to
\frac12.
$$

因：

$$
k_{1,j}<0,
$$

$$
\boxed{
k_{1,j}\to
-\frac1{\sqrt2}.
}
$$

由：

$$
k_1+k_2+k_3=0
$$

與：

$$
k_2k_3\to0,
$$

positive sector給：

$$
\boxed{
k_{2,j}\to0,
}
$$

$$
\boxed{
k_{3,j}\to
\frac1{\sqrt2}.
}
$$

---

# 6. C5-F.2：Middle-Gap Limit Preserves the Compressive Axis

沿 subsequence：

$$
P_1(K_j)\to P_\ast
$$

in compact rank-one projector space。

limit strain shape為：

$$
\boxed{
K_\ast
=
R_\ast
\operatorname{diag}
\left(
-\frac1{\sqrt2},
0,
\frac1{\sqrt2}
\right)
R_\ast^T,
}
$$

with：

$$
\boxed{
P_\ast
=
R_\ast
e_1\otimes e_1
R_\ast^T.
}
$$

### 結論

$$
\boxed{
\text{Middle-Gap Degeneration}
\not\Rightarrow
\text{Pressure-Axis Decoherence}.
}
$$

gap degeneration只殺：

$$
\theta_K
$$

half-space margin，

不殺：

$$
\boxed{
G(e_1)
=
e_1\otimes e_1-\frac13I.
}
$$

---

# 7. Exact common-axis quadratic half-space

現在假設：

$$
\boxed{
\vartheta(S/|S|)
\ge
\delta>0.
}
$$

且 most-compressive axis exact：

$$
\boxed{
e_1=e
}
$$

固定。

定義：

$$
\boxed{
H_{e,\delta}
=
e\otimes e
-
\frac{
1+\delta
}{
2
}
I.
}
$$

---

# 8. Strain contribution with fixed axis

因：

$$
e^TS^2e
=
\lambda_1^2
=
|S|^2
\left(
\frac12+\vartheta
\right),
$$

所以：

$$
H_{e,\delta}:S^2
=
|S|^2
\left[
\frac12+\vartheta
-
\frac{
1+\delta
}{2}
\right].
$$

因此：

$$
\boxed{
H_{e,\delta}:S^2
\ge
\frac{
\delta
}{2}
|S|^2.
}
$$

---

# 9. Vorticity contribution with fixed axis

計算：

$$
\operatorname{tr}H_{e,\delta}
=
-\frac{
1+3\delta
}{2}.
$$

所以：

$$
\boxed{
H_{e,\delta}
-
(\operatorname{tr}H_{e,\delta})I
=
e\otimes e
+
\delta I.
}
$$

因此：

$$
\boxed{
H_{e,\delta}:
\frac14
(
\omega\otimes\omega
-
|\omega|^2I
)
\ge
\frac{
\delta
}{4}
|\omega|^2.
}
$$

---

# 10. C5-F.3：Fixed Compressive Axis Excludes Q Cancellation

結合 §§8–9：

$$
\boxed{
H_{e,\delta}:Q
\ge
\frac{
\delta
}{4}
(
|S|^2+|\omega|^2
)
\ge
\frac{
\delta
}{4}
|Q|.
}
$$

所以所有：

$$
Q/|Q|
$$

落同一 strict half-space。

因此：

$$
\boxed{
\vartheta\ge\delta
+
e_1\equiv e
\Rightarrow
0\notin\operatorname{conv}\{Q/|Q|\}.
}
$$

### 結論

只讓：

$$
e_2,e_3
$$

在 $e^\perp$ 裡旋轉，

不能產生 Seven-Point zero barycenter。

---

# 11. Axis-cap version

現在不要求：

$$
e_1=e
$$

exact。

假設：

$$
\boxed{
\angle(e_1,e)
\le
\alpha.
}
$$

固定：

$$
\sigma
=
\delta/2.
$$

定義：

$$
\boxed{
H_{e,\sigma}
=
e\otimes e
-
\frac{
1+\sigma
}{2}
I.
}
$$

---

# 12. Strain lower bound in an axis cap

令：

$$
\alpha
=
\angle(e_1,e).
$$

因：

$$
S^2
$$

positive semidefinite，

$$
e^TS^2e
\ge
\lambda_1^2
\cos^2\alpha.
$$

且：

$$
\lambda_1^2
\ge
|S|^2
\left(
\frac12+\delta
\right).
$$

所以：

$$
H_{e,\sigma}:S^2
\ge
|S|^2
\left[
\left(
\frac12+\delta
\right)
\cos^2\alpha
-
\frac12
-
\frac{\delta}{4}
\right].
$$

即：

$$
\boxed{
H_{e,\sigma}:S^2
\ge
|S|^2
\left[
\frac{3\delta}{4}
-
\left(
\frac12+\delta
\right)
\sin^2\alpha
\right].
}
$$

---

# 13. Axis-cap radius

若：

$$
\boxed{
\sin^2\alpha
\le
\frac{
\delta
}{
2+4\delta
},
}
$$

則：

$$
\left(
\frac12+\delta
\right)
\sin^2\alpha
\le
\frac{\delta}{4}.
$$

因此：

$$
\boxed{
H_{e,\sigma}:S^2
\ge
\frac{
\delta
}{2}
|S|^2.
}
$$

定義：

$$
\boxed{
\alpha_\delta
=
\arcsin
\sqrt{
\frac{
\delta
}{
2+4\delta
}
}.
}
$$

---

# 14. Vorticity in the axis-cap test

對：

$$
\sigma=\delta/2,
$$

$$
H_{e,\sigma}
-
(\operatorname{tr}H_{e,\sigma})I
=
e\otimes e
+
\frac{\delta}{2}I.
$$

所以：

$$
\boxed{
H_{e,\sigma}:
\frac14
(
\omega\otimes\omega
-
|\omega|^2I
)
\ge
\frac{
\delta
}{8}
|\omega|^2.
}
$$

---

# 15. C5-F.4：Axis-Cap Quadratic Half-Space Theorem

若：

$$
\boxed{
\vartheta\ge\delta>0
}
$$

且：

$$
\boxed{
\angle(e_1,e)
\le
\alpha_\delta,
}
$$

則：

$$
\boxed{
H_{e,\delta/2}:Q
\ge
\frac{
\delta
}{8}
(
|S|^2+|\omega|^2
)
\ge
\frac{
\delta
}{8}
|Q|.
}
$$

因此：

$$
\boxed{
\textbf{all Q directions in one narrow compressive-axis cap
lie in a common strict half-space}.
}
$$

---

# 16. Projective compressive-axis space

因：

$$
e
$$

與：

$$
-e
$$

產生相同 projector，

真正 axis state是：

$$
\boxed{
[e]\in\mathbb{RP}^2.
}
$$

等價用：

$$
\boxed{
P=e\otimes e
}
$$

rank-one projector。

其 space compact。

---

# 17. Q-weighted axis measure

在 active Q core，

定義：

$$
\boxed{
\nu_j^{axis}
=
P_1(S_j)_\#
\nu_j^Q
}
$$

on：

$$
\mathbb{RP}^2.
$$

若：

$$
S=0
$$

on nonzero Q points，

使用 cemetery state；

但 C5-E away from gap physical coercivity可控制此 branch。

---

# 18. C5-F.5：Nondegenerate Q Cancellation Forces Axis Anti-Concentration

固定：

$$
\delta>0.
$$

假設：

1. gap mass：
   $$
   \nu_j^Q\{\vartheta<\delta\}
   \to0;
   $$

2. quadratic coherence：
   $$
   \kappa_j^Q\to0.
   $$

則對任意 projective axis：

$$
[e],
$$

不可能：

$$
\nu_j^{axis}
\left(
B_{\alpha_\delta}([e])
\right)
\to1.
$$

更定量，

存在：

$$
c_\delta>0
$$

使 large $j$：

$$
\boxed{
\sup_{[e]}
\nu_j^{axis}
\left(
B_{\alpha_\delta}([e])
\right)
\le
1-c_\delta
}
$$

after absorbing the small gap mass。

### 結論

$$
\boxed{
Q\text{-cancellation}
+
\text{nondegenerate gap}
\Rightarrow
\textbf{compressive-axis dispersion}.
}
$$

這比 C5-E 的 full strain-direction dispersion更強。

---

# 19. Common far-pressure axis condition

C5-D：

harmonic far-pressure leading matrix：

$$
\boxed{
F\in\operatorname{Sym}_0(3).
}
$$

對 strong-middle coherent core，

若 mean rotation depleted，

required oriented compensation是：

$$
\boxed{
G(e_1):F
=
e_1^TFe_1
\le
-c
}
$$

for：

$$
c>0.
$$

所以 compressive axis必落：

$$
\boxed{
\Omega_F^-(c)
=
\{
[e]\in\mathbb{RP}^2:
e^TFe\le-c
\}.
}
$$

---

# 20. Far-pressure signature dichotomy

nonzero trace-free symmetric：

$$
F
$$

只有兩種 nondegenerate inertia types：

## Signature I

$$
\boxed{
(-,+,+).
}
$$

one negative eigenvalue。

## Signature II

$$
\boxed{
(-,-,+).
}
$$

two negative eigenvalues。

zero eigenvalue是 boundary degeneration。

這兩種 pressure-axis geometries本質不同。

---

# 21. Signature $(-,+,+)$ gives projective cap locking

令：

$$
f_1<0<f_2\le f_3
$$

為 eigenvalues，

$$
v_1
$$

是 unique negative eigenvector。

對 unit：

$$
e,
$$

令：

$$
\alpha
=
\angle(e,v_1)
$$

projectively。

因：

$$
e^TFe
\ge
f_1\cos^2\alpha
+
f_2\sin^2\alpha,
$$

若：

$$
e^TFe
\le
-c,
$$

其中：

$$
0<c<|f_1|,
$$

則：

$$
\boxed{
\sin^2\alpha
\le
\frac{
|f_1|-c
}{
|f_1|+f_2
}.
}
$$

---

# 22. Pressure cap radius

定義：

$$
\boxed{
\alpha_F(c)
=
\arcsin
\sqrt{
\frac{
|f_1|-c
}{
|f_1|+f_2
}
}.
}
$$

則：

$$
\boxed{
\Omega_F^-(c)
\subset
B_{\alpha_F(c)}
([v_1]).
}
$$

所以 strong negative pressure margin：

$$
c\uparrow|f_1|
$$

強迫 compressive axes鎖到 arbitrarily narrow projective cap。

---

# 23. C5-F.6：Strong One-Negative Far Pressure vs Q-Cancellation Incompatibility

假設：

1. Q-cancellation：
   $$
   \kappa_Q\to0;
   $$

2. nondegenerate middle gap：
   $$
   \vartheta\ge\delta>0
   $$
   on asymptotically full Q mass；

3. same common far matrix：
   $$
   F
   $$
   with signature：
   $$
   (-,+,+);
   $$

4. every active core requires：
   $$
   e_1^TFe_1\le-c<0;
   $$

5. pressure cap satisfies：
   $$
   \boxed{
   \alpha_F(c)
   <
   \alpha_\delta.
   }
   $$

則 impossible。

### 證明

pressure condition把 all compressive axes鎖進：

$$
B_{\alpha_F(c)}([v_1])
\subset
B_{\alpha_\delta}([v_1]).
$$

C5-F.4把 all Q directions放入同一 strict half-space。

所以 Q barycenter不能趨零。$\square$

---

# 24. Explicit margin criterion

condition：

$$
\alpha_F(c)
<
\alpha_\delta
$$

equivalent to：

$$
\boxed{
\frac{
|f_1|-c
}{
|f_1|+f_2
}
<
\frac{
\delta
}{
2+4\delta
}.
}
$$

即：

$$
\boxed{
c
>
|f_1|
-
(
|f_1|+f_2
)
\frac{
\delta
}{
2+4\delta
}.
}
$$

所以有 explicit：

$$
\boxed{
\textbf{pressure-margin vs middle-gap incompatibility threshold}.
}
$$

---

# 25. Signature $(-,-,+)$ does not force a cap

若：

$$
f_1\le f_2<0<f_3,
$$

negative quadratic region包含 whole negative eigenspace附近的一個 projective belt。

即使：

$$
e^TFe\le-c,
$$

axes仍可在 two-dimensional negative subspace中顯著 spread。

所以：

$$
\boxed{
\text{common pressure sign}
}
$$

本身不推出：

$$
\boxed{
\text{single-axis cap locking}.
}
$$

---

# 26. Pressure-signature escape

因此 nondegenerate-gap Q-cancellation若要和 common far pressure共存，

至少走：

## F-P1 — Weak pressure alignment

$$
c
$$

不足以形成 narrow cap。

## F-P2 — Two-negative-eigenvalue pressure

$$
\boxed{
\operatorname{sig}F=(-,-,+).
}
$$

## F-P3 — Far-pressure spectral degeneration

one eigenvalue：

$$
\to0,
$$

signature接近 boundary。

## F-P4 — Pressure-source fragmentation

different cores沒有共同 dominant：

$$
F.
$$

## F-P5 — Mean rotation

pressure不需承擔 coherent quadratic forcing。

## F-P6 — Middle-gap degeneration

$$
\delta\to0
$$

使 Q half-space margin消失。

---

# 27. Middle-gap does not remove F-axis condition

即使：

$$
\delta\to0,
$$

C5-F.2證：

$$
P_1=e_1\otimes e_1
$$

仍穩定。

而 far pressure pairing仍：

$$
\boxed{
G(e_1):F
=
e_1^TFe_1.
}
$$

所以：

$$
\boxed{
\text{middle-gap route}
}
$$

只能逃掉：

$$
Q\text{-half-space margin},
$$

不能自動逃掉：

$$
\boxed{
\text{pressure-axis constraint}.
}
$$

這使 middle-gap / pressure motifs仍保持耦合。

---

# 28. Axis measure compactness through the gap

因：

$$
\mathbb{RP}^2
$$

compact，

任意 recurrent gap-degenerate sequence仍可抽：

$$
\boxed{
\nu_j^{axis}
\rightharpoonup
\nu_\ast^{axis}.
}
$$

所以 C5 limit可以同時記錄：

- gap defect：
  $$
  \vartheta=0;
  $$
- compressive-axis distribution：
  $$
  \nu_\ast^{axis}.
  $$

這兩個 coordinates不可合併成單一「strain degeneracy」。

---

# 29. Vorticity-dominant leakage

C5-E 給 local core：

$$
B_R
$$

上的 critical vorticity stock：

$$
\boxed{
\mathfrak W_R
=
\frac{
R
}{
\nu^2
}
\int_{B_R}
|\omega|^2dx
\ge
w_0>0.
}
$$

所以：

$$
\boxed{
\int_{B_R}
|\omega|^2dx
\ge
w_0
\frac{
\nu^2
}{
R
}.
}
$$

---

# 30. C5-F.7：Vorticity Stock Forces Quadratic $L^2$ Congestion

Hölder：

$$
\left(
\int_{B_R}
|\omega|^2
\right)^2
\le
|B_R|
\int_{B_R}
|\omega|^4.
$$

所以：

$$
\boxed{
\|\omega\|_{L^4(\mathbb R^3)}^2
\ge
c
w_0
\nu^2
R^{-5/2}.
}
$$

即：

$$
\boxed{
\|\omega\otimes\omega\|_2
\ge
c
w_0
\nu^2
R^{-5/2}.
}
$$

---

# 31. Strain-space / complement split

因：

$$
P_{st}
$$

是 $L^2$ orthogonal projection，

$$
\boxed{
\|\omega\otimes\omega\|_2^2
=
\|P_{st}(\omega\otimes\omega)\|_2^2
+
\|P_{st}^{\perp}(\omega\otimes\omega)\|_2^2.
}
$$

所以至少：

## F-VOP

$$
\boxed{
\frac{
R^{5/2}
}{
\nu^2
}
\|
P_{st}(\omega\otimes\omega)
\|_2
\ge
c w_0,
}
$$

或：

## F-VCOMP

$$
\boxed{
\frac{
R^{5/2}
}{
\nu^2
}
\|
P_{st}^{\perp}(\omega\otimes\omega)
\|_2
\ge
c w_0.
}
$$

---

# 32. Meaning of F-VOP

$$
P_{st}(\omega\otimes\omega)
$$

正是 Miller operator architecture中的 growth-orthogonal vorticity-quadratic source。

所以：

$$
\boxed{
\text{Vorticity Leakage}
\Rightarrow
\text{Miller Orthogonal Operator Congestion}
}
$$

在 F-VOP branch。

---

# 33. Meaning of F-VCOMP

$$
P_{st}^{\perp}(\omega\otimes\omega)
$$

是 constraint-space complement。

### Hard guard

它不是：

$$
\boxed{
\text{actual pressure Hessian}
}
$$

本身。

actual pressure是 full raw N–S nonlinearity projection complement，

而不是單獨：

$$
\omega\otimes\omega
$$

complement。

所以 F-VCOMP只能記為：

$$
\boxed{
\textbf{Constraint-Complement Congestion}.
}
$$

未來需和：

- $S^2$；
- advection；
- pressure current；

聯立。

---

# 34. Strain-derivative leakage

C5-E E-DER：

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
|\nabla S|^2dx
\ge
h_0>0.
}
$$

所以：

$$
\boxed{
\int_{B_{CR}}
|\nabla S|^2
\ge
h_0
\frac{
\nu^2
}{
R^3
}.
}
$$

---

# 35. C5-F.8：Derivative Stock Forces Critical $D^2u$ Amplitude

由 volume average，

存在：

$$
x_R\in B_{CR}
$$

使：

$$
|\nabla S(x_R)|
\ge
c
h_0^{1/2}
\frac{
\nu
}{
R^3
}.
$$

因 pointwise：

$$
|\nabla S|
\le
C
|D^2u|,
$$

有：

$$
\boxed{
\|D^2u\|_{L^\infty(B_{CR})}
\ge
c
h_0^{1/2}
\frac{
\nu
}{
R^3
}.
}
$$

所以：

$$
\boxed{
\frac{
R^3
}{
\nu
}
\|D^2u\|_\infty
\gtrsim1.
}
$$

這是 scale-critical second-derivative amplitude。

---

# 36. Stock still does not give derivative geometry

C5-F.8只給：

$$
\boxed{
D^2u\text{ amplitude}
}
$$

不給：

$$
\boxed{
D^2u\text{ component/sign superlevel sparseness}.
}
$$

所以仍不能直接套：

$$
\boxed{
\text{Grujić--Xu Theorem 3.5}.
}
$$

這個 hard guard保持。

---

# 37. Middle-gap cubic amplitude in NS-scaled coordinates

C5-E：

$$
\|S\|_3^3
\ge
\frac{
M_\delta
}{
\sqrt6\,\delta
}.
$$

若 on ancestry scale $R$：

$$
b_R^{mid}
=
\frac{
R^3
}{
\nu^3
}
M_\delta
\ge
b_0,
$$

且：

$$
e_R^S
=
\frac{
R
}{
\nu^2
}
\|S\|_2^2
\le
E_0,
$$

則 effective amplitude：

$$
A_{\rm eff}
=
\frac{
\|S\|_3^3
}{
\|S\|_2^2
}
$$

滿足：

$$
\boxed{
\widehat A_S
:=
\frac{
R^2
}{
\nu
}
A_{\rm eff}
\ge
c
\frac{
b_0
}{
E_0
}
\delta^{-1}.
}
$$

因此：

$$
\boxed{
\frac{
R^2
}{
\nu
}
\|S\|_\infty
\gtrsim
\delta^{-1}.
}
$$

---

# 38. Middle-gap sparse scale

C5-E：

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
E_0
}{
b_0^{2/3}
}
}
$$

under fixed stock/load bounds。

所以 middle-gap route產生：

$$
\boxed{
\text{amplitude}\sim\delta^{-1},
\qquad
\text{sparse scale}\sim\delta^{2/3}.
}
$$

---

# 39. Fixed-$k=1$ direct regularity scale comparison

Grujić–Xu Theorem 3.5，

velocity route：

$$
d=3,
\qquad
k=1,
$$

geometric scale exponent：

$$
\boxed{
\frac{
d
}{
2k+d
}
=
\frac35.
}
$$

在 NS-rescaled coordinates，

若 raw gradient amplitude與 strain amplitude comparable：

$$
\boxed{
\frac{
R^2
}{
\nu
}
\|\nabla u\|_\infty
\lesssim
C
\widehat A_S
\sim
\delta^{-1},
}
$$

則 theorem target normalized scale behaves：

$$
\boxed{
\frac{
\rho_{\rm dir}
}{
R
}
\sim
\delta^{3/5}.
}
$$

而 C5-E strain sparse scale：

$$
\boxed{
\frac{
r_{sp}
}{
R
}
\lesssim
\delta^{2/3}.
}
$$

因：

$$
\boxed{
\frac23>\frac35,
}
$$

對：

$$
0<\delta\ll1,
$$

$$
\boxed{
\delta^{2/3}
<
\delta^{3/5}.
}
$$

所以：

$$
\boxed{
\textbf{middle-gap intermittency has a formally favorable spatial exponent
relative to the fixed-}k=1\textbf{ direct scale}.
}
$$

---

# 40. The raw-gradient/vorticity interface

但是：

$$
\nabla u
=
S
+
A(\omega),
$$

所以：

$$
\|\nabla u\|_\infty
$$

可遠大於：

$$
\|S\|_\infty
$$

因 vorticity。

若 raw derivative component：

$$
(\nabla u)_\ell^\pm
>
\lambda
\|\nabla u\|_\infty
$$

而：

$$
|\omega|
\le
\eta
\|\nabla u\|_\infty
$$

at that point，

則：

$$
|S|
\ge
c
(\lambda-C\eta)
\|\nabla u\|_\infty.
$$

因此 selected raw derivative high set可被包含於：

$$
\boxed{
\text{strain high set}
\cup
\text{vorticity-high defect set}.
}
$$

---

# 41. C5-F.9：Field-Conversion Dichotomy

schematically，

對 suitable thresholds：

$$
\boxed{
V_\lambda(Du)
\subset
E_{\lambda_S}(S)
\cup
E_{\eta}(\omega).
}
$$

所以要把 strain sparseness合法轉成：

$$
D^1u
$$

component/sign sparseness，

只需額外控制 vorticity high set。

### 結論

C5-E 的 field-conversion gap可重寫為：

$$
\boxed{
\text{raw-velocity derivative gate}
\vee
\textbf{vorticity-geometry defect}.
}
$$

這正和 E-VORT branch接上。

---

# 42. Direct-gate pre-closure

因此 middle-gap branch若同時滿足：

1. bounded normalized strain stock；
2. nondegenerate middle load；
3. sufficiently small gap：
   $$
   \delta\ll1;
   $$
4. vorticity high set在 same scale沒有破壞 union sparsity；
5. full-space / component-sign conversion成立；
6. geometry出現在 Theorem 3.5 admissible later time；

則 C5-E sparse scale在 exponent上已不比：

$$
k=1
$$

direct target差。

### 狀態

$$
\boxed{
\mathrm{SCALING\mbox{-}FAVORABLE\ CONDITIONAL\ INTERFACE}.
}
$$

不是 theorem application。

---

# 43. Chain-assisted scale

Grujić–Xu Theorem 3.14 velocity scale：

$$
\boxed{
\rho_{\rm chain}^{(k)}
\sim
\|D^ku\|_\infty^{-1/(k+1)}.
}
$$

對 formal：

$$
k=1
$$

amplitude：

$$
\sim\delta^{-1},
$$

normalized target：

$$
\sim
\delta^{1/2}.
$$

C5-E：

$$
r_{sp}/R
\sim
\delta^{2/3}
<
\delta^{1/2}.
$$

所以 spatial exponent亦 favorable。

### Hard guard

Theorem 3.14不是單獨的 $k=1$ sparseness theorem。

它包含：

- sufficiently high derivative hierarchy；
- ascending/descending chains；
- later analytic time；
- all stated constants/hypotheses。

因此这里只能稱：

$$
\boxed{
\textbf{formal chain-scale compatibility}.
}
$$

---

# 44. Derivative-order selection

對每個 recurrent event：

$$
j,
$$

令：

$$
\boxed{
k_j^{best}
}
$$

是我們依：

- available amplitude；
- available sparseness；
- field conversion；
- theorem time gate；
- chain status；

選出的最有利 derivative order。

不假設：

$$
k_j^{best}
$$

一定唯一。

固定 deterministic tie-break。

---

# 45. C5-F.10：Fixed-Order Recurrence or Derivative-Order Escape

任意：

$$
k_j^{best}\in\mathbb N
$$

sequence都有 subsequence滿足：

## F-KFIX

$$
\boxed{
k_j^{best}
=
k_\ast
}
$$

eventually，

或：

## F-KINF

$$
\boxed{
k_j^{best}
\to\infty.
}
$$

### Proof

$\mathbb N$ 的 elementary subsequence dichotomy。$\square$

### 意義

$$
\boxed{
\text{repeated low-order failure}
}
$$

本身不自動推出：

$$
\boxed{
k\to\infty.
}
$$

除非所有 fixed-order recurrent defect motifs被另外排除。

---

# 46. Fixed-order defect stabilization

若：

$$
k_j^{best}=k_\ast
$$

along subsequence，

C5-A derivative defect vector：

$$
d_j^{der}
\in
\{0,1\}^{4}
$$

再抽 subsequence可 eventual constant。

所以得到：

$$
\boxed{
\textbf{Fixed-Order Recurrent Gate Defect}.
}
$$

例如永久：

- MULT；
- SHELLFULL；
- TIMECHAIN；
- COMPSIGN。

這是 C5下一階可直接攻的 compact motif。

---

# 47. Derivative-order escape

若：

$$
k_j^{best}\to\infty,
$$

Grujić–Xu direct exponent：

$$
\boxed{
\alpha_k^{dir}
=
\frac{
3
}{
2k+3
}
\to0,
}
$$

而 chain exponent：

$$
\boxed{
\alpha_k^{chain}
=
\frac1{k+1}
\to0.
}
$$

其 framework正是證：

$$
\boxed{
\text{regularity/a-priori scaling gap asymptotically vanishes}
}
$$

as：

$$
k\to\infty.
$$

---

# 48. But derivative-order escape is not regularity

即使：

$$
k_j\to\infty,
$$

仍可能每代失敗於：

- component/sign conversion；
- later analytic time；
- derivative chain；
- spatial carrier mismatch；
- effective multiplicity。

所以：

$$
\boxed{
k_j\to\infty
}
$$

只是：

$$
\boxed{
\textbf{Asymptotically-Critical Boundary Motif}.
}
$$

不是 contradiction。

---

# 49. C5-F residual network

C5-E residual：

$$
\text{Gap}
\vee
\text{Derivative}
\vee
\text{Vorticity}.
$$

C5-F後：

## Gap branch

$$
\boxed{
\text{Gap Intermittency}
+
\text{persistent compressive-axis metadata}.
}
$$

若 common far pressure one-negative strongly locks axes，

與 nondegenerate-gap Q cancellation incompatible。

## Vorticity branch

$$
\boxed{
\text{Miller Orthogonal Operator}
\vee
\text{Constraint-Complement Congestion}.
}
$$

## Derivative branch

$$
\boxed{
\text{critical }D^2u\text{ amplitude}
+
\text{fixed-order defect}
\vee
\text{order escape}.
}
$$

---

# 50. Second finite-dimensional incompatibility

C5-D 第一個：

$$
\boxed{
\text{Strong-Middle Full Strain Cone}
\cap
\text{Q Zero-Barycenter}
=
\varnothing.
}
$$

C5-F 第二個：

$$
\boxed{
\text{Nondegenerate Middle Gap}
+
\text{Strong One-Negative Common Far-Pressure Axis Lock}
+
\text{Q Zero-Barycenter}
=
\varnothing.
}
$$

此處不再要求 full strain direction鎖在單 cone；

只需：

$$
\boxed{
\textbf{compressive axis itself被鎖定}.
}
$$

這是更強的 motif incompatibility。

---

# 51. Why this matters

Q cancellation原本可以想像：

> 固定最壓縮軸，
> 只讓另外兩個 eigenvectors / eigenvalues亂轉，
> 應該足以把 quadratic directions抵消吧？

C5-F 證：

$$
\boxed{
\textbf{不行，只要 middle gap有 fixed positive margin。}
}
$$

Q cancellation真的需要：

$$
\boxed{
\textbf{compressive-axis dispersion}
}
$$

或：

$$
\boxed{
\textbf{middle-gap collapse}.
}
$$

而 pressure compensation恰好也看：

$$
\boxed{
\textbf{同一個 compressive axis}.
}
$$

所以 Q / Pressure兩個 residual motifs現在共用真正有限維 order parameter：

$$
\boxed{
[e_1]\in\mathbb{RP}^2.
}
$$

---

# 52. New C5 shared state

定義：

$$
\boxed{
\Theta_\ast^{Axis}
=
\left\langle
\nu_\ast^{axis},
\mathfrak G_\ast,
F_\ast,
\operatorname{sig}F_\ast,
c_\ast^P,
\mathfrak C_\ast^{axis}
\right\rangle.
}
$$

其中：

- $\nu_\ast^{axis}$ = compressive-axis probability；
- $\mathfrak G_\ast$ = middle-gap defect mass；
- $F_\ast$ = normalized common far-pressure matrix metadata；
- signature = pressure inertia type；
- $c_\ast^P$ = pressure alignment margin；
- $\mathfrak C_\ast^{axis}$ = cap / convex-hull concentration statistic。

---

# 53. Axis concentration statistic

定義：

$$
\boxed{
\mathfrak C_{\rm axis}(\alpha)
=
\sup_{[e]\in\mathbb{RP}^2}
\nu_\ast^{axis}
(
B_\alpha([e])
).
}
$$

若：

$$
\mathfrak C_{\rm axis}(\alpha_\delta)=1,
$$

且 gap：

$$
\ge\delta,
$$

Q zero barycenter impossible。

如果 Q cancellation active：

$$
\boxed{
\mathfrak C_{\rm axis}(\alpha_\delta)
\le
1-c_\delta.
}
$$

unless middle-gap mass intervenes。

---

# 54. Pressure axis-locking statistic

signature：

$$
(-,+,+)
$$

common far matrix with margin：

$$
c
$$

forces：

$$
\boxed{
\mathfrak C_{\rm axis}
(
\alpha_F(c)
)
=
1.
}
$$

所以如果：

$$
\alpha_F(c)<\alpha_\delta,
$$

與 Q cancellation limit直接衝突。

---

# 55. X-Integration guards 更新

## G-AXROB

middle-gap degeneration不得刪除 compressive-axis metadata。

## G-AXCAP

Q cancellation在 nondegenerate gap下必保存 axis anti-concentration。

## G-PSIG

common far-pressure matrix需保存 eigenvalue signature。

## G-PCAP

signature $(-,+,+)$ + strong negative margin才能升成 single projective cap。

## G-PBELT

signature $(-,-,+)$只給 negative-plane/belt geometry，

不得偷稱 axis locking。

## G-VPROJ

vorticity L2 stock先轉 raw $\omega\otimes\omega$ L2，

再分 $P_{st}$ / complement。

## G-PCOMPNEQ

$P_{st}^{\perp}(\omega\otimes\omega)$不得稱 actual pressure。

## G-KESC

repeated derivative gate failure不得直接推出 $k\to\infty$。

## G-GXSCALE

scaling-favorable不等於 theorem-ready。

---

# 56. True ETN 更新

C5-F state：

$$
\boxed{
\Theta_\ast^{F}
=
\left\langle
\nu_\ast^{axis},
\mathfrak G_\ast,
F_\ast,
\operatorname{sig}F_\ast,
c_\ast^P,
\mathfrak V_\ast^{op,\omega},
\mathfrak V_\ast^{\perp,\omega},
k_\ast^{best},
d_\ast^{der}
\right\rangle.
}
$$

---

# 57. C5 strategic status

C5-A：

$$
\text{motif compactness}.
$$

C5-B：

$$
\text{temporal Young oscillation/concentration}.
$$

C5-C：

$$
\text{temporal cross-curvature constraints}.
$$

C5-D：

$$
\text{Strong-Middle vs Q-cancellation incompatibility}.
$$

C5-E：

$$
Q
\to
\text{Gap/Derivative/Vorticity field defects}.
$$

C5-F：

$$
\boxed{
\textbf{Gap preserves pressure axis;
Q cancellation forces axis dispersion;
strong one-negative far pressure can force the opposite.}
}
$$

同時 derivative route被整理成：

$$
\boxed{
\text{fixed-order recurrent defect}
\vee
\text{asymptotically-critical order escape}.
}
$$

---

# 58. What remains unresolved

## 1. Pressure signature $(-,-,+)$

negative-plane geometry仍可能容納 axis dispersion與 Q cancellation。

## 2. Middle-gap + one-negative pressure

gap collapse會讓 Q half-space margin消失，

所以 strong axis lock可和 gap intermittency共存。

## 3. Vorticity complement

constraint-complement congestion尚未和 actual pressure / advection聯立。

## 4. Derivative theorem gate

scaling開始 favorable，

但 field/component/sign/time/chain interfaces仍在。

---

# 59. 新 frontier：C5-G

正式下一題：

$$
\boxed{
\textbf{C5-G — Pressure-Signature Defects,
Vorticity Constraint Complements,
and Fixed-Order Derivative-Gate Closure}.
}
$$

---

# 60. C5-G proof obligations

## G1 — Two-negative pressure geometry

對：

$$
\operatorname{sig}F=(-,-,+),
$$

研究 negative-plane axis distribution與 Q cancellation是否仍可無限制共存。

## G2 — Pressure signature transitions

若 recurrent common pressure在：

$$
(-,+,+)
\leftrightarrow
(-,-,+)
$$

之間切換，

必 crossing：

$$
\det F=0.
$$

研究 signature-transition defect / eigenvalue-zero congestion。

## G3 — Gap × pressure signature

middle-gap defect與 pressure signature boundary是否同步形成 compact recurrent motif。

## G4 — Vorticity constraint complement

把：

$$
P_{st}^{\perp}(\omega\otimes\omega)
$$

與：

- $S^2$ complement；
- advection complement；
- actual pressure Hessian；

放入同一 orthogonal ledger。

## G5 — Fixed $k=1$ gate

在 vorticity-high-set不 dominant時，

嚴格測：

$$
\text{strain sparse}
\to
D u\text{ component/sign sparse}
$$

的 union-sparseness constants。

## G6 — Fixed $k=2$ gate

從：

$$
\mathfrak H_R
$$

與 additional active-volume data，

測 Theorem 3.5 $k=2$ scale。

## G7 — Fixed-order defect elimination

逐一處理：

- SHELLFULL；
- COMPSIGN；
- TIMECHAIN；
- MULT。

若某 fixed order全部閉合，

hypothetical survivor排除。

## G8 — Escalation audit

只有 fixed-order defects全部無法 recurrently承擔時，

才合法把研究 route送：

$$
k_j\to\infty.
$$

---

# 61. 正式狀態

$$
\boxed{
\begin{aligned}
\text{uniform compressive spectral gap}
&:\ \mathrm{PROVED},\\
\text{middle-gap preserves compressive axis}
&:\ \mathrm{PROVED},\\
\text{fixed-axis + gap}\Rightarrow Q\text{ half-space}
&:\ \mathrm{PROVED},\\
\text{axis-cap + gap}\Rightarrow Q\text{ half-space}
&:\ \mathrm{PROVED},\\
Q\text{-cancellation + gap}\Rightarrow\text{axis dispersion}
&:\ \mathrm{PROVED},\\
(-,+,+)\text{ far pressure}\Rightarrow\text{axis cap}
&:\ \mathrm{PROVED},\\
\text{strong cap pressure + gap + Q cancellation}
&:\ \mathrm{INCOMPATIBLE},\\
(-,-,+)\text{ far pressure}\Rightarrow\text{single cap}
&:\ \mathrm{FALSE},\\
\text{vorticity stock}\Rightarrow\omega\otimes\omega\ L^2\text{ congestion}
&:\ \mathrm{PROVED},\\
\text{vorticity congestion}\Rightarrow
P_{st}\text{ or complement}
&:\ \mathrm{PROVED},\\
\text{strain derivative stock}\Rightarrow D^2u\text{ critical amplitude}
&:\ \mathrm{PROVED},\\
\text{middle-gap sparse exponent vs fixed }k=1\text{ scale}
&:\ \mathrm{FAVORABLE\ CONDITIONAL},\\
\text{raw }Du\text{ gate}\vee\text{vorticity geometry defect}
&:\ \mathrm{PROVED\ STRUCTURAL},\\
\text{fixed order or }k\to\infty\text{ subsequence}
&:\ \mathrm{PROVED},\\
k\to\infty\Rightarrow\text{regularity}
&:\ \mathrm{FALSE/NOT\ PROVED},\\
\text{global regularity}
&:\ \mathrm{OPEN}.
\end{aligned}
}
$$

---

# 62. 結論

C5-E把 Q cancellation翻成：

$$
\text{Gap}
\vee
\text{Derivative}
\vee
\text{Vorticity}.
$$

C5-F現在把這三支再和 pressure / derivative theorem geometry耦合。

第一，

middle gap並不破壞最壓縮 axis。

對 normalized positive-middle strain：

$$
\boxed{
\lambda_2-\lambda_1
\ge
1/\sqrt2.
}
$$

所以：

$$
e_1\otimes e_1
$$

甚至在：

$$
\lambda_2/|S|\to0
$$

時仍穩定。

第二，

如果 gap：

$$
\vartheta\ge\delta
$$

不退化，

只要 compressive axes待在 cap：

$$
\boxed{
\sin^2\angle(e_1,e)
\le
\frac{
\delta
}{
2+4\delta
},
}
$$

就存在 common matrix functional使：

$$
\boxed{
H:Q
\gtrsim
\delta|Q|.
}
$$

所以：

$$
\boxed{
Q\text{-cancellation}
+
\text{nondegenerate gap}
\Rightarrow
\textbf{compressive-axis dispersion}.
}
$$

第三，

common harmonic far pressure如果 signature：

$$
(-,+,+)
$$

且負向補償 margin夠強，

它反而強迫 compressive axes落入單一 projective cap。

若 cap窄過上面的 Q-cancellation threshold，

得到第二個 finite-dimensional incompatibility：

$$
\boxed{
\text{Strong One-Negative Pressure Axis Lock}
+
\text{Nondegenerate Gap}
+
\text{Q Zero Barycenter}
=
\varnothing.
}
$$

所以 pressure survivor必走：

$$
\boxed{
\text{weak margin}
\vee
(-,-,+)\text{ signature}
\vee
\text{signature degeneration}
\vee
\text{source fragmentation}
\vee
\text{mean rotation}
\vee
\text{middle-gap collapse}.
}
$$

第四，

vorticity leakage現在也被送回 operator architecture：

$$
\boxed{
\text{Vorticity Leakage}
\Rightarrow
P_{st}(\omega\otimes\omega)
\vee
P_{st}^{\perp}(\omega\otimes\omega).
}
$$

第五，

strain-derivative leakage給：

$$
\boxed{
R^3\|D^2u\|_\infty/\nu
\gtrsim1.
}
$$

而 middle-gap cubic intermittency在 normalized spatial exponent上已對 fixed-$k=1$ direct sparseness scale呈 favorable relation。

但 published Grujić–Xu theorem仍要求真正：

$$
D^ku
\text{ / }
D^k\omega
$$

component/sign、later time、chain條件，因此仍不能越級。

最後，

derivative escalation真正正確的邏輯只有：

$$
\boxed{
\textbf{Fixed-Order Recurrent Defect}
\vee
\textbf{Derivative Order }k_j\to\infty.
}
$$

只有把所有 fixed-order defects逐步殺掉後，

才有資格把 survivor route真正送到：

$$
k\to\infty
$$

的 asymptotically-critical boundary。

正式下一篇：

$$
\boxed{
\textbf{C5-G — Pressure-Signature Defects,
Vorticity Constraint Complements,
and Fixed-Order Derivative-Gate Closure}.
}
$$

---

# References

1. E. Miller, *On the interaction of strain and vorticity for solutions of the Navier–Stokes equation*, arXiv:2407.02691v2; Pure and Applied Analysis 8 (2026).
2. Z. Grujić, L. Xu, *Asymptotic Criticality of the Navier–Stokes Regularity Problem*, Journal of Mathematical Fluid Mechanics 26, Article 53 (2024), DOI: 10.1007/s00021-024-00888-x; arXiv:1911.00974.
3. Z. Bradshaw, T.-P. Tsai, *On the local pressure expansion for the Navier–Stokes equations*, arXiv:2001.11526.
4. E. Miller, *A regularity criterion for the Navier–Stokes equation involving only the middle eigenvalue of the strain tensor*, arXiv:1710.05569.

# Internal dependencies

- `NS_C5E_StrainDirection_MiddleGap_DerivativeIntermittency_v0.1.md`
- `NS_C5D_SpatialMatrix_StrongMiddleQuadraticPressureObstruction_v0.1.md`
- `NS_C5C_TemporalCorrelation_CrossCurvatureOrdering_v0.1.md`
- `NS_C5B_TemporalYoung_PulsePhaseCompatibility_v0.1.md`
- `NS_C5A_RecordWindow_MotifCompactness_v0.1.md`
- `NS_C4J_CompensationRigidity_FinalSynchronizationAudit_v0.1.md`
- `NS_C3S_StrainConeMargin_MergerRigidity_v0.1.md`
- `NS_C3V_TurnoverPacking_StrainFluctuationEscape_v0.1.md`
- `NS_C3W_PressureRotation_StrainSparseness_v0.1.md`
- `NS_C3X_JointPressureStrain_AnalyticityGap_v0.1.md`
- `NS_C3Y_DerivativeChain_IntermittencyTradeoff_v0.1.md`
- `True ETN / 無限維張力場`
- `X_Integral_Unified_Program_v0.2.md`

Next:

$$
\boxed{
\textbf{C5-G — Pressure-Signature Defects,
Vorticity Constraint Complements,
and Fixed-Order Derivative-Gate Closure}
}
$$
