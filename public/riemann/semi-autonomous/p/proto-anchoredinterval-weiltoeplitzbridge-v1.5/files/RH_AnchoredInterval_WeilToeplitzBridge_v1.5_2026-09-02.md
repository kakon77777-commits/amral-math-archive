工程紀錄 · 第三弧線 v1.5 · 2026-09-02 · EXACT_FULL_MATRIX_BRIDGE · TOEPLITZ_PRIME_LOCALIZATION · RH_CLAIM_FALSE

# Anchored Interval Weil Gram、Box Toeplitz 二階差分與 Prime-Power Tent Localization

**RH-AnchoredInterval-WeilToeplitzBridge v1.5**

本節點承接：

- `RH-ConditionalOffAxisCell-ZetaTransfer-v1.1`
- `RH-GlobalQuantifier-PrimePowerConvexCompression-v1.2`
- `RH-OffAxisCell-LiWitnessCompiler-v1.3`
- `RH-WeilCheckpoint-GreenDiagonalBridge-v1.4`

v1.4 已建立精確對角關係：

$$
\Psi(t)
=
W(R_t\ast\widetilde R_t)
=
\frac12G_g(t,t),
$$

其中 Suzuki 的 $R_t$ 是中心對稱矩形。

本節點進行 normalization audit 後發現：

> 對角公式完全正確；但若要把 **full screw kernel** 直接解讀成矩形 basis 的 Weil Gram，必須區分「中心對稱矩形」與「共同左端點的一側 interval indicator」。

這個區分反而導出一個更精確、更適合 AMRAL arithmetic matrix 的 full-matrix bridge。

本輪核心結果：

1. 定義 anchored interval

$$
H_t=\mathbf 1_{[0,t]}.
$$

則在 Suzuki spectral / distributional extension 的自然意義下：

$$
\boxed{
W(H_t\ast\widetilde H_u)
=
G_g(t,u)
=
\Psi(t)+\Psi(u)-\Psi(t-u).
}
$$

2. 對 cumulative interval basis 做一次差分，得到局部 box basis。

3. 均勻網格下，box Gram matrix 是一個精確 Toeplitz matrix：

$$
\boxed{
M^{\rm box}_{ij}(h)
=
\frac12
\Delta_h^2
\Psi((i-j)h).
}
$$

4. Suzuki prime-side ramp 在二階差分後變成 compact tent kernel：

$$
\boxed{
M^{\rm fin}_{ij}(h)
=
-\frac12
\sum_{n=p^k}
\frac{\Lambda(n)}{\sqrt n}
\left[
T_h((i-j)h-\log n)
+
T_h((i-j)h+\log n)
\right],
}
$$

其中：

$$
T_h(x)=(h-|x|)_+.
$$

因此每個 prime power 只作用在其 logarithmic location 鄰近的 Toeplitz lag。

5. 這給出一個 canonical exact target：

```text
M_box = M_infty_box + M_fin_box
```

它與 AMRAL 舊 `M_arith = M_infty + M_fin` 的設計語言高度一致，但**尚未宣稱舊實作逐項完全相等**；舊封包使用實偶緊支撐 basis 與額外 constraints，需另做 basis / normalization audit。

6. 固定 box width $h$ 時，在 RH 下此 Toeplitz covariance 的 spectral measure 是純原子測度；Szegő–Kolmogorov prediction theorem 因而暗示其無限過去 one-step innovation variance 為 $0$。所以即使改用 box-normalized Schur innovation，也不應期待 uniform positive floor。

**RH_CLAIM = False.**

---

# 0. Claim register

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE

SUZUKI_CENTERED_RECTANGLE_DIAGONAL = TRUE
ANCHORED_INTERVAL_FULL_GREEN_GRAM = TRUE
CUMULATIVE_TO_INCREMENT_CONGRUENCE = TRUE
UNIFORM_GRID_TOEPLITZ_IDENTITY = TRUE

PRIMEPOWER_TENT_LOCALIZATION = TRUE
FINITE_PRIME_ACTIVATION_FOR_FINITE_BOX_MATRIX = TRUE

M_BOX_RH_EQUIVALENCE = TRUE_AS_REFORMULATION
OLD_AMRAL_M_ARITH_EQUALS_M_BOX = NOT_PROVED

MITTERMEIER_CJ_EQUALS_SCHUR = REJECTED_AS_DEFAULT_EXPECTATION
NESTED_ARITHMETIC_PLUS_PROJECTION_DEBIT = IDENTIFIED

FIXED_H_INNOVATION_UNIFORM_FLOOR = NO_GO_UNDER_RH
GLOBAL_RH_CERTIFICATE = FALSE
```

---

# 1. v1.4 normalization correction

Suzuki 定義中心對稱矩形：

$$
R_t(x)
=
\frac1{\sqrt2}
\mathbf 1_{[-t/2,t/2]}(x)
$$

忽略端點 measure-zero convention。

其自相關為：

$$
R_t\ast\widetilde R_t
=
\Delta_t,
$$

其中：

$$
\Delta_t(x)
=
\frac12(t-|x|)_+.
$$

Suzuki 證明：

$$
\boxed{
W(\Delta_t)=\Psi(t).
}
$$

所以：

$$
\boxed{
W(R_t\ast\widetilde R_t)=\Psi(t).
}
$$

這是 exact diagonal identity。

但對不同 $t,u$：

$$
W(R_t\ast\widetilde R_u)
$$

不是自動等於：

$$
\frac12
\left[
\Psi(t)+\Psi(u)-\Psi(t-u)
\right].
$$

原因是 $R_t,R_u$ 分別以自己的中心對齊；full screw kernel 則自然來自共同 anchor 的 interval increments。

所以 v1.4 應精確化為：

```text
CENTERED_RECTANGLE = EXACT DIAGONAL WEIL RAY
ANCHORED_INTERVAL = EXACT FULL SCREW GRAM
```

---

# 2. Anchored intervals

對：

$$
t\ge0
$$

定義：

$$
H_t(x)
=
\mathbf 1_{[0,t]}(x).
$$

使用 Suzuki 的 Fourier convention：

$$
\widehat f(z)
=
\int_{\mathbb R}
f(x)e^{izx}\,dx.
$$

則：

$$
\widehat H_t(z)
=
\frac{e^{izt}-1}{iz}.
$$

而：

$$
\widetilde H_u(x)
=
H_u(-x)
=
\mathbf 1_{[-u,0]}(x),
$$

所以：

$$
\widehat{\widetilde H_u}(z)
=
\frac{1-e^{-izu}}{iz}.
$$

因此：

$$
\widehat H_t(z)
\widehat{\widetilde H_u}(z)
=
\frac{
(e^{izt}-1)(e^{-izu}-1)
}{
z^2
}.
$$

Suzuki 的 screw-kernel spectral representation 是：

$$
G_g(t,u)
=
\sum_\gamma
\frac{
(e^{i\gamma t}-1)
(e^{-i\gamma u}-1)
}{
\gamma^2
}.
$$

所以在 Weil distribution 對此 piecewise-linear correlation 的自然 extension / approximation 意義下：

## Theorem 2.1 · Anchored Interval Full-Gram Identity

$$
\boxed{
W(H_t\ast\widetilde H_u)
=
G_g(t,u).
}
$$

而：

$$
G_g(t,u)
=
\Psi(t)+\Psi(u)-\Psi(t-u).
$$

所以：

$$
\boxed{
W(H_t\ast\widetilde H_u)
=
\Psi(t)+\Psi(u)-\Psi(t-u).
}
$$

---

# 3. Diagonal consistency

取：

$$
u=t.
$$

則：

$$
H_t\ast\widetilde H_t
=
(t-|x|)_+
=
2\Delta_t.
$$

所以：

$$
W(H_t\ast\widetilde H_t)
=
2W(\Delta_t)
=
2\Psi(t).
$$

另一方面：

$$
G_g(t,t)
=
2\Psi(t).
$$

完全一致。

而 Suzuki centered rectangle：

$$
R_t
=
\frac1{\sqrt2}
\tau_{-t/2}H_t
$$

在 self-correlation 上 translation phase 消失，因此：

$$
W(R_t\ast\widetilde R_t)
=
\frac12
W(H_t\ast\widetilde H_t)
=
\Psi(t).
$$

所以 centered 與 anchored conventions 的差異只在 full cross-Gram，而非 diagonal。

---

# 4. Finite cumulative Green matrix

取：

$$
0=t_0<t_1<\cdots<t_m.
$$

定義 cumulative anchored basis：

$$
\mathcal H_T
=
\{H_{t_1},\ldots,H_{t_m}\}.
$$

其 Gram matrix：

$$
K_T
=
\left[
G_g(t_i,t_j)
\right]_{i,j=1}^{m}.
$$

也就是：

$$
\boxed{
(K_T)_{ij}
=
\Psi(t_i)
+
\Psi(t_j)
-
\Psi(t_i-t_j).
}
$$

這是 v1.4 `Canonical Checkpoint Gram Matrix` 的 exact Weil-basis interpretation。

---

# 5. 從 cumulative intervals 到 local increments

定義 disjoint interval increments：

$$
E_j
=
H_{t_j}
-
H_{t_{j-1}}
=
\mathbf 1_{(t_{j-1},t_j]}.
$$

令：

$$
A_T
=
\left[
W(E_i\ast\widetilde E_j)
\right]_{i,j=1}^{m}.
$$

因為：

$$
H_{t_k}
=
\sum_{j=1}^{k}E_j,
$$

存在 unit lower-triangular matrix：

$$
L_{kj}
=
\mathbf 1_{j\le k}
$$

使：

$$
\boxed{
K_T
=
LA_TL^\ast.
}
$$

由：

$$
\det L=1,
$$

得到：

$$
\boxed{
\det K_T
=
\det A_T.
}
$$

而 congruence 保持 inertia：

$$
\boxed{
K_T\succeq0
\Longleftrightarrow
A_T\succeq0.
}
$$

這是 full Green checkpoint matrix 到 local arithmetic box matrix 的 exact basis bridge。

---

# 6. Nonuniform mixed second difference

直接展開：

$$
(A_T)_{ij}
=
K(t_i,t_j)
-
K(t_{i-1},t_j)
-
K(t_i,t_{j-1})
+
K(t_{i-1},t_{j-1}).
$$

代入：

$$
K(t,u)
=
\Psi(t)+\Psi(u)-\Psi(t-u),
$$

所有單變數 terms 消掉，得到：

$$
\boxed{
\begin{aligned}
(A_T)_{ij}
&=
-\Psi(t_i-t_j)
+
\Psi(t_{i-1}-t_j)
\\
&\quad
+
\Psi(t_i-t_{j-1})
-
\Psi(t_{i-1}-t_{j-1}).
\end{aligned}
}
$$

因此 local interval Gram 完全由 $\Psi$ 的 mixed finite difference 決定。

---

# 7. Uniform-grid Toeplitz theorem

令：

$$
t_j=jh,
\qquad
h>0.
$$

則：

$$
E_j
=
\mathbf 1_{((j-1)h,jh]}.
$$

所有 $E_j$ 都是同一個 length-$h$ box 的平移。

令：

$$
d_{ij}
=
(i-j)h.
$$

則：

$$
\boxed{
(A_h^{(m)})_{ij}
=
\Psi(d_{ij}+h)
+
\Psi(d_{ij}-h)
-
2\Psi(d_{ij}).
}
$$

定義 centered second difference：

$$
\Delta_h^2\Psi(x)
=
\Psi(x+h)+\Psi(x-h)-2\Psi(x).
$$

因此：

$$
\boxed{
(A_h^{(m)})_{ij}
=
\Delta_h^2\Psi((i-j)h).
}
$$

只依賴 $i-j$，所以：

$$
\boxed{
A_h^{(m)}
\text{ is Toeplitz}.
}
$$

---

# 8. Canonically normalized box basis

為了讓 diagonal 與 Suzuki $\Psi(h)$ 對齊，定義：

$$
B_j^{(h)}
=
\frac1{\sqrt2}
E_j.
$$

令：

$$
M_{\rm box}^{(m)}(h)
=
\left[
W(B_i^{(h)}\ast\widetilde B_j^{(h)})
\right].
$$

則：

$$
\boxed{
M_{\rm box}^{(m)}(h)
=
\frac12
A_h^{(m)}.
}
$$

所以：

$$
\boxed{
(M_{\rm box})_{ij}
=
\frac12
\Delta_h^2
\Psi((i-j)h).
}
$$

其 diagonal：

$$
(M_{\rm box})_{ii}
=
\frac12
[
\Psi(h)+\Psi(-h)-2\Psi(0)
].
$$

因為 $\Psi$ 偶且：

$$
\Psi(0)=0,
$$

得到：

$$
\boxed{
(M_{\rm box})_{ii}
=
\Psi(h).
}
$$

---

# 9. RH equivalence of the canonical box family

若 RH 成立，Weil positivity 給：

$$
M_{\rm box}^{(m)}(h)\succeq0
$$

對所有：

$$
h>0,
\qquad
m\ge1.
$$

反過來，若：

$$
M_{\rm box}^{(1)}(h)\ge0
$$

對所有 $h>0$，則：

$$
\Psi(h)\ge0
$$

對所有 $h>0$。

由 Suzuki Theorem 1.7：

$$
RH.
$$

因此：

## Theorem 9.1 · Box-Toeplitz RH reformulation

$$
\boxed{
RH
\Longleftrightarrow
M_{\rm box}^{(m)}(h)\succeq0
\quad
\forall h>0,\ \forall m\ge1.
}
$$

甚至：

$$
m=1
$$

已足以恢復 Suzuki pointwise criterion。

因此高維矩陣不是新的 quantifier reduction；其價值是：

- cross-correlation witness；
- basis compatibility；
- PSD / Schur engineering；
- 與 AMRAL arithmetic matrix 對齊。

---

# 10. Prime-side exact decomposition

對：

$$
t\in\mathbb R
$$

把 Suzuki $\Psi$ 寫成：

$$
\Psi(t)
=
\mathcal A_e(t)
-
\sum_{n=p^k}
\frac{\Lambda(n)}{\sqrt n}
\left(
|t|-\log n
\right)_+,
$$

其中：

$$
\mathcal A_e(t)
$$

是 archimedean / elementary terms 的 even extension。

所以：

$$
M_{\rm box}
=
M_{\infty}^{\rm box}
+
M_{\rm fin}^{\rm box},
$$

其中：

$$
\boxed{
(M_{\infty}^{\rm box})_{ij}
=
\frac12
\Delta_h^2
\mathcal A_e((i-j)h).
}
$$

以及：

$$
\boxed{
(M_{\rm fin}^{\rm box})_{ij}
=
-\frac12
\sum_{n=p^k}
\frac{\Lambda(n)}{\sqrt n}
\Delta_h^2
\left(
|x|-\log n
\right)_+
\Big|_{x=(i-j)h}.
}
$$

這正好形成：

```text
archimedean matrix + finite-position prime-power matrix
```

---

# 11. Ramp second difference is a tent

定義：

$$
r_a(x)
=
(|x|-a)_+.
$$

又定義：

$$
T_h(x)
=
(h-|x|)_+.
$$

因為：

$$
(|x|-a)_+
=
(x-a)_+
+
(-x-a)_+,
$$

而：

$$
\Delta_h^2
(x-a)_+
=
T_h(x-a),
$$

所以：

$$
\boxed{
\Delta_h^2r_a(x)
=
T_h(x-a)
+
T_h(x+a).
}
$$

因此：

## Theorem 11.1 · Prime-Power Tent Localization

$$
\boxed{
\begin{aligned}
(M_{\rm fin}^{\rm box})_{ij}
&=
-\frac12
\sum_{n=p^k}
\frac{\Lambda(n)}{\sqrt n}
\\
&\quad\times
\left[
T_h((i-j)h-\log n)
+
T_h((i-j)h+\log n)
\right].
\end{aligned}
}
$$

這是完全 local 的 finite-position formula。

---

# 12. Prime-power activation locality

因為：

$$
T_h(y)>0
$$

若且唯若：

$$
|y|<h,
$$

所以 prime power $n$ 對 lag：

$$
d=(i-j)h
$$

產生貢獻，只可能在：

$$
\boxed{
\left|
|d|-\log n
\right|
<h
}
$$

附近。

對：

$$
|i-j|\le m-1,
$$

有：

$$
|d|\le(m-1)h.
$$

所以若：

$$
\log n\ge mh,
$$

則：

$$
\left|
|d|-\log n
\right|
\ge h.
$$

因此不貢獻。

所以 finite $m\times m$ box matrix 的 prime side 只需要：

$$
\boxed{
n<e^{mh}.
}
$$

換言之：

```text
NO PRIME TAIL EXISTS
FOR A FIXED FINITE BOX MATRIX.
```

prime side 是真正有限和。

---

# 13. 每個 prime power 只落到鄰近 Toeplitz diagonals

令：

$$
x_n
=
\frac{\log n}{h}.
$$

考慮非負 lag index：

$$
k=|i-j|.
$$

主要 tent：

$$
T_h(kh-\log n)
$$

非零只在：

$$
|k-x_n|<1.
$$

因此 $k$ 最多只可能是：

$$
\lfloor x_n\rfloor
$$

與：

$$
\lceil x_n\rceil.
$$

若：

$$
x_n
=
r+\theta,
\qquad
0\le\theta<1,
$$

則：

$$
T_h(rh-\log n)
=
h(1-\theta),
$$

以及：

$$
T_h((r+1)h-\log n)
=
h\theta.
$$

所以一個 prime power 的 logarithmic position 被**線性插值**到最近的兩條 Toeplitz diagonals。

這給出非常清楚的 geometric interpretation：

$$
\boxed{
\log p^k
\longmapsto
\text{two-neighbour diagonal deposition}.
}
$$

---

# 14. 與 AMRAL 舊 $M_{\rm arith}$ 的關係

AMRAL 目前公開頁面說明舊 prototype：

$$
M_{\rm arith}(R)
=
M_\infty(R)
+
M_{\rm fin}(R)
$$

使用：

- real-even compact-support basis；
- archimedean 主計算；
- finite-position activation；
- constraints

$$
G(i/2)=G(0)=0;
$$

- 支撐半徑掃描；
- numerical minimum eigenvalue。

這與本節點 canonical box matrix 的 structural decomposition 高度一致。

但目前不能寫：

$$
\boxed{
M_{\rm arith}
=
M_{\rm box}.
}
$$

原因：

1. basis 不同；
2. constraints 不同；
3. Fourier / Mellin normalization 尚未逐項核對；
4. 舊 implementation 的 raw METHOD / source 在本輪 web surface 中無法直接取得完整公式。

所以正確狀態：

```text
SAME_WEIL_ENGINEERING_TARGET = STRONGLY_SUPPORTED
EXACT_MATRIX_EQUALITY = NOT_YET_AUDITED
```

---

# 15. Canonical normalization audit contract

舊 implementation 若要證明與 Weil / Suzuki normalization 一致，可增加一個專門的 box-basis test mode。

要求：

### N1 · Diagonal

對每個 $h$：

$$
M_{ii}
=
\Psi(h).
$$

### N2 · Toeplitz

$$
M_{ij}
=
M_{i+r,j+r}
$$

只要 indices 合法。

### N3 · Second difference

$$
2M_{ij}
=
\Psi((i-j+1)h)
+
\Psi((i-j-1)h)
-
2\Psi((i-j)h).
$$

### N4 · Prime tent

finite part 必須符合：

$$
M_{\rm fin}
=
-\frac12
\sum_{p^k}
\frac{\log p}{p^{k/2}}
\left[
T_h(d-\log p^k)
+
T_h(d+\log p^k)
\right].
$$

### N5 · Exact prime cutoff

$m\times m$ matrix 不得需要：

$$
p^k\ge e^{mh}
$$

的 prime data。

若 N1–N5 全部以 outward interval arithmetic 通過，就可以把：

```text
BOX_BASIS_NORMALIZATION = VERIFIED
```

登錄。

再從 box basis 到舊 smooth basis 做 congruence / projection audit。

---

# 16. Cumulative / increment determinant invariance

由：

$$
K_m
=
L_mA_mL_m^\ast
$$

以及：

$$
\det L_m=1,
$$

有：

$$
\det K_m
=
\det A_m.
$$

因此對 nested prefix：

$$
\frac{\det K_{m+1}}{\det K_m}
=
\frac{\det A_{m+1}}{\det A_m}.
$$

若 matrices positive definite，兩邊都是 one-step Schur complement。

所以：

$$
\boxed{
\text{cumulative checkpoint Schur reserve}
=
\text{increment-basis innovation variance}
}
$$

對同一 nested partition 而言，這不是類比，而是 determinant-ratio identity。

---

# 17. Uniform grid and stationary prediction picture

固定：

$$
h>0.
$$

在 RH 下，Suzuki spectral representation：

$$
\Psi(t)
=
\sum_\gamma
\frac{
1-\cos(\gamma t)
}{
\gamma^2
}
$$

其中 $\gamma$ 全為 real。

令 Toeplitz coefficient：

$$
a_k(h)
=
(M_{\rm box})_{i,i+k}.
$$

由二階差分：

$$
\boxed{
a_k(h)
=
\sum_\gamma
\frac{
1-\cos(\gamma h)
}{
\gamma^2
}
\cos(k\gamma h)
}
$$

以對稱 zero sum 的方式理解。

因此可定義單位圓 positive spectral measure：

$$
\boxed{
\mu_h
=
\sum_\gamma
\frac{
1-\cos(\gamma h)
}{
\gamma^2
}
\delta_{e^{i\gamma h}}.
}
$$

則：

$$
a_k(h)
=
\int_{\mathbb T}
z^k\,d\mu_h(z)
$$

以 real-symmetric moment convention 解讀。

所以：

$$
M_{\rm box}^{(m)}(h)
$$

就是一個 stationary Toeplitz covariance matrix。

---

# 18. Pure-point spectral measure

對固定 $h$，$\mu_h$ 是 countable atomic measure。

其 total mass：

$$
\mu_h(\mathbb T)
=
a_0(h)
=
\Psi(h).
$$

RH 下 Suzuki 證：

$$
\Psi(h)>0
$$

對所有：

$$
h>0.
$$

因此可 normalize：

$$
\nu_h
=
\frac{\mu_h}{\Psi(h)}
$$

成 probability spectral measure。

此 measure 沒有 absolutely continuous density；它是 pure point / singular。

---

# 19. Szegő–Kolmogorov no-floor theorem

令：

$$
\sigma_m^2(h)
$$

為用前 $m$ 個 box increments 預測下一個 increment 的 optimal linear prediction error。

對 Toeplitz Gram：

$$
\sigma_m^2(h)
=
\frac{
\det M_{\rm box}^{(m+1)}(h)
}{
\det M_{\rm box}^{(m)}(h)
}
$$

在 finite positive-definite 情況下成立。

Szegő–Kolmogorov prediction theorem 給出 infinite-past innovation variance：

$$
\sigma_\infty^2
=
\exp
\left[
\frac1{2\pi}
\int_{-\pi}^{\pi}
\log f(\theta)\,d\theta
\right]
$$

當 absolutely continuous spectral density $f$ 的 logarithm integrable；若：

$$
\int\log f=-\infty,
$$

則：

$$
\sigma_\infty^2=0.
$$

對 pure singular / atomic $\nu_h$：

$$
f(\theta)=0
$$

幾乎處處。

所以：

$$
\boxed{
\sigma_m^2(h)
\longrightarrow0
}
$$

在 RH 下。

因此：

## Theorem 19.1 · Fixed-width innovation no-floor

對任何 fixed：

$$
h>0,
$$

若 RH 成立，canonical uniform-box nested Schur innovation 不可能存在：

$$
\varepsilon_h>0
$$

使：

$$
\sigma_m^2(h)\ge\varepsilon_h
$$

對所有 $m$ 成立。

甚至以 fixed box variance：

$$
\Psi(h)
$$

正規化後：

$$
\boxed{
\frac{
\sigma_m^2(h)
}{
\Psi(h)
}
\to0.
}
$$

這比 v1.4 的 absolute-gap no-go 更進一步：

> 即使把單一 box variance 固定成常數尺度，隨著 history dimension 增加，prediction / Schur innovation reserve 仍必須允許 collapse 到 $0$。

---

# 20. 這對 determinant strategy 的警告

因為：

$$
\det M_m
=
\prod_{j=0}^{m-1}
\sigma_j^2,
$$

而：

$$
\sigma_j^2\to0,
$$

所以高維 determinant certificate 將不可避免地變得極度 ill-conditioned。

因此下列工程策略不可作為 global proof target：

```text
uniform determinant lower bound
uniform smallest-eigenvalue lower bound
uniform Schur-innovation lower bound
```

真正合理的是：

```text
SIGN-CORRECT PSD
WITH SCALE-ADAPTIVE PRECISION
```

而不是固定 margin。

---

# 21. Recovery reserve 與 Schur reserve：不是同一個 cost

Mittermeier Part 3–5 的 current frontier：

$$
\mathcal V_q
=
\mathcal C_q-\mathcal J_q
$$

其中：

- $\mathcal C_q$ 是 scalar arithmetic capacity；
- $\mathcal J_q\ge0$ 是 logarithmically smoothed von Mangoldt cost；
- after verified finite base：

$$
RH
\Longleftrightarrow
\mathcal V_q\ge0
$$

at every recovery witness。

若採其 recovery-minimum convention：

$$
\mathcal V_q
=
\Psi(t_q^\ast),
$$

則 Green diagonal：

$$
G_g(t_q^\ast,t_q^\ast)
=
2\mathcal V_q
=
2\mathcal C_q-2\mathcal J_q.
$$

現在加入 anchor set $T$。

Schur reserve：

$$
S_T(t_q^\ast)
=
2\Psi(t_q^\ast)
-
k^\ast K_T^{-1}k.
$$

所以：

$$
\boxed{
S_T(t_q^\ast)
=
2\mathcal C_q
-
\left[
2\mathcal J_q
+
P_T(q)
\right],
}
$$

其中：

$$
P_T(q)
=
k^\ast K_T^{-1}k
\ge0.
$$

因此：

```text
Mittermeier J_q = scalar arithmetic debit
Schur P_T(q)    = correlation / projection debit
```

兩者不是預設應相等的 quantity。

正確 bridge 是：

$$
\boxed{
\text{capacity}
-
\text{arithmetic debit}
-
\text{projection debit}.
}
$$

這是 v1.4 direct-equality expectation 的修正。

---

# 22. Consequence：Schur positivity 是更強的 finite condition

因為：

$$
P_T(q)\ge0,
$$

有：

$$
S_T(t_q^\ast)
\le
2\mathcal V_q.
$$

所以：

$$
S_T(t_q^\ast)\ge0
\Longrightarrow
\mathcal V_q\ge0.
$$

但：

$$
\mathcal V_q\ge0
$$

不必然推出：

$$
S_T(t_q^\ast)\ge0
$$

除非整個 kernel 已 PSD。

所以 Schur condition 是更敏感的 finite matrix test。

在 RH 假時，理論上可能在 scalar checkpoint 尚未穿零以前，就由 off-diagonal correlation 產生 negative finite eigenvalue。

這提供一條更早的 refutation detection channel。

但對證 RH 而言，它是更強條件，不應假定比 scalar frontier 更容易。

---

# 23. Generalized Schur reserve

v1.4 使用：

$$
K_T^{-1}.
$$

由 no-floor 結果可知，late matrices 可能非常 ill-conditioned。

更 robust 的 exact PSD block criterion 使用 Moore–Penrose pseudoinverse。

對：

$$
\begin{pmatrix}
K & k\\
k^\ast & d
\end{pmatrix},
$$

有：

$$
\succeq0
$$

若且唯若：

1.

$$
K\succeq0;
$$

2.

$$
k\in\operatorname{Range}(K);
$$

3.

$$
\boxed{
d-k^\ast K^\dagger k\ge0.
}
$$

所以 production certificate 應支援：

```text
GENERALIZED_SCHUR_RESERVE
```

而不能依賴 numerically unstable inverse。

RH 下 Suzuki 的 positive-definite theorem 對有限非零 test functions 通常使 exact finite Gram nonsingular；但驗證器仍應以 range-safe formulation 設計。

---

# 24. Canonical arithmetic matrix target

本節點建議正式新增 AMRAL canonical matrix：

$$
\boxed{
M_{\rm box}^{(m)}(h)
=
\frac12
\left[
\Delta_h^2
\Psi((i-j)h)
\right]_{i,j=1}^{m}.
}
$$

其優點：

1. exact RH-compatible；
2. exact prime-side finite sum；
3. exact arch / finite decomposition；
4. Toeplitz；
5. finite-position localization；
6. Schur / determinant recursion；
7. 可直接與 Suzuki scalar checkpoint cross-check；
8. 不需要未知 zeta zeros；
9. 可完全使用 prime powers + archimedean terms 計算。

它可以成為舊 `$M_{\rm arith}$` 的 canonical reference implementation。

---

# 25. Reference implementation contract

本節點附：

`box_toeplitz_reference.py`

其作用：

- 生成 prime powers；
- 計算 prime tent matrix；
- 從任意 $\Psi$ evaluator 建 second-difference Toeplitz matrix；
- 比較 split matrix 與 direct second-difference matrix；
- 計算 ordinary Schur reserve。

它是 reference code，不是 rigorous proof engine。

production 版本仍需：

- MPFR / Arb outward intervals；
- exact prime-power enumeration；
- directed logs / square roots；
- archimedean Lerch tail enclosure；
- generalized Schur certificate；
- independent implementation。

---

# 26. 下一個真正值得攻的方向

v1.5 之後，有兩條路。

## Route A · Engineering canonicalization

`RH-CanonicalBoxArithmeticMatrix-v1.6`

直接實作 rigorous：

$$
M_{\rm box}
=
M_\infty^{\rm box}
+
M_{\rm fin}^{\rm box}.
$$

目標：

- exact interval matrix；
- exact prime cutoff；
- independent split-vs-direct equality check；
- generalized Schur；
- finite negative-eigenvalue witness channel。

這一條工程成功率高。

---

## Route B · Mathematical closure

真正剩餘的是：

> 能否利用 prime-power tent locality 與 Toeplitz structure，得到一個不是 fixed-margin 的 all-scale sign theorem？

也就是尋找：

$$
M_{\rm box}^{(m)}(h)\succeq0
$$

的結構性證明，而不是 eigenvalue lower bound。

可研究：

- total positivity / conditional positive definiteness；
- Toeplitz symbol in a non-absolutely-continuous setting；
- Verblunsky coefficient constraints；
- exact prime-update recursion；
- event-conditioned inertia preservation；
- prime-power two-diagonal update 的 global sign invariant。

這可能比直接攻：

$$
\mathcal J_q\le\mathcal C_q
$$

更符合 AMRAL 原始 matrix 路線。

---

# 27. GAP ledger

## CLOSED

### G1. Full Green Gram basis

```text
CLOSED
```

anchored interval basis 給 exact full kernel。

---

### G2. Cumulative-to-local congruence

```text
CLOSED
```

$$
K=LAL^\ast.
$$

---

### G3. Uniform Toeplitz matrix

```text
CLOSED
```

$$
M_{ij}
=
\frac12
\Delta_h^2\Psi((i-j)h).
$$

---

### G4. Prime-power tent localization

```text
CLOSED
```

finite-position kernel 為 compact tents。

---

### G5. Fixed finite prime cutoff

```text
CLOSED
```

$m\times m$ box matrix只需：

$$
n<e^{mh}.
$$

---

### G6. Fixed-$h$ innovation floor

```text
NO_GO_UNDER_RH
```

Szegő–Kolmogorov：

$$
\sigma_m^2(h)\to0.
$$

---

## OPEN

### G7. Old AMRAL $M_{\rm arith}$ exact normalization

```text
OPEN_AUDIT
```

---

### G8. Rigorous box matrix implementation

```text
OPEN_ENGINEERING
```

---

### G9. Prime-update inertia invariant

```text
OPEN
```

---

### G10. All-scale Toeplitz PSD proof

```text
OPEN
```

等價 RH，不能偷降級。

---

### G11. RH

```text
OPEN
```

---

# 28. Trust boundary

必須保留：

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE

BOX_TOEPLITZ_IDENTITY = EXACT
PRIME_TENT_LOCALIZATION = EXACT

OLD_AMRAL_MATRIX_EQUALITY = NOT_PROVED
MITTERMEIER_COST_EQUALS_SCHUR_COST = FALSE_AS_DEFAULT_ASSUMPTION

FINITE_PSD_BATCH != RH_PROOF
FINITE_PRIME_CUTOFF != GLOBAL_QUANTIFIER_CLOSURE

GLOBAL_RH_CERTIFICATE = FALSE
```

---

# 29. 一句話狀態

> v1.5 把 v1.4 的 diagonal bridge 升級成 exact full-matrix bridge：Suzuki 的 centered rectangle 仍負責 $\Psi(t)=W(R_t\ast\widetilde R_t)$ 的對角 identity，而共同左端點 anchored intervals $H_t=\mathbf1_{[0,t]}$ 則精確生成整個 screw kernel $G_g(t,u)$. 對 cumulative intervals 做差分後得到 local box basis；均勻網格下形成 canonical Toeplitz matrix $M_{\rm box}=\frac12[\Delta_h^2\Psi((i-j)h)]$. 更重要的是，prime-power ramp 在二階差分後精確局部化成 tent kernels，每個 $\log p^k$ 只沉積到最近的 Toeplitz diagonals，且任一 finite matrix 的 prime side 只需 $p^k<e^{mh}$ 的有限資料。這給 AMRAL 舊 `M_arith=M_\infty+M_{\rm fin}` 一個可直接 audit 的 canonical normalization target。另一方面，RH 下 fixed-$h$ Toeplitz spectral measure 為 pure atomic，Szegő–Kolmogorov theorem 迫使 nested Schur innovation variance 趨近 $0$，所以連 box-normalized reserve 也不能期待 uniform positive floor；真正的 proof target 必須是 sign/inertia preservation，而不是固定 margin。

---

# 30. References

1. Masatoshi Suzuki, **Aspects of the screw function corresponding to the Riemann zeta-function**, *Journal of the London Mathematical Society* 108 (2023), 1448–1487.  
   DOI: https://doi.org/10.1112/jlms.12785

2. Masatoshi Suzuki, **On the Hilbert space derived from the Weil distribution**, arXiv:2301.00421.  
   https://arxiv.org/abs/2301.00421

3. Masatoshi Suzuki, **Weil's quadratic form via the screw function**, arXiv:2606.09096, 2026.  
   https://arxiv.org/abs/2606.09096

4. Rainer Andreas Mittermeier, **The Remaining Riemann-Hypothesis Tail: From Prime-Power Checkpoints to Smoothed von Mangoldt Bounds**, 2026.  
   https://zenodo.org/records/21979513

5. Rainer Andreas Mittermeier, **Recovery Witnesses in the Prime-Power Checkpoint Program: Service-Clock Geometry and an Exact Quantifier Reduction for the Riemann-Hypothesis Tail -- Part 4**, 2026.  
   https://zenodo.org/records/22076079

6. Rainer Andreas Mittermeier, **Deep Episodes in the Prime-Power Checkpoint Program: An Unconditional Terminal-Episode Theorem, an Exact Chebyshev Bridge, and Sharp Recovery Recurrence -- Part 5**, 2026.  
   https://zenodo.org/records/22076088

7. AMRAL, **算術矩陣與半正定證書原型 · v0.1**.  
   https://amral.evemisslab.com/riemann/autonomous/p/proto-arithmetic-matrix-psd-v0.1/

8. AMRAL, **區域相位塑形原型 · v0.1**.  
   https://amral.evemisslab.com/riemann/autonomous/p/proto-regional-phase-shaping-v0.1/

9. AMRAL, **等變算術障礙整合總論 · v1.0**.  
   https://amral.evemisslab.com/riemann/semi-autonomous/p/proto-equivariant-arithmetic-obstruction-integration-v1.0/

10. Classical Szegő–Kolmogorov prediction theorem; one accessible statement is summarized in the literature as the one-step prediction error being the exponential of the integral of the logarithm of the absolutely continuous spectral density, and zero when that logarithmic integral is $-\infty$.

---

# 31. Provenance

研究主導：Neo.K

v1.5 數學續推、Suzuki normalization audit、Toeplitz / prediction bridge 與 canonical source 整理：ChatGPT / GPT-5.6 Sol

日期：2026-09-02

研究定位：AMRAL 黎曼猜想半自主研究線，第三弧線 exact full-matrix / arithmetic canonicalization 節點。

本文件是 research source artifact，不是 peer-reviewed publication。

所有 claim 必須依 Claim register、GAP ledger 與 Trust boundary 解讀。
