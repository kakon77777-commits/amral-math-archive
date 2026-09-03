工程紀錄 · 第三弧線 v1.6 · 2026-09-02 · FIXED_APERTURE_LOCAL_PRIME_CRITERION · FINITE_MEMORY_EVENT_SYSTEM · RH_CLAIM_FALSE

# 固定孔徑局部質數偏差判準與有限記憶三脈衝系統

**RH-FixedAperture-LocalPrimeDiscrepancy v1.6**

本節點承接：

- `RH-ConditionalOffAxisCell-ZetaTransfer-v1.1`
- `RH-GlobalQuantifier-PrimePowerConvexCompression-v1.2`
- `RH-OffAxisCell-LiWitnessCompiler-v1.3`
- `RH-WeilCheckpoint-GreenDiagonalBridge-v1.4`
- `RH-AnchoredInterval-WeilToeplitzBridge-v1.5`

v1.5 建立 canonical box Toeplitz coefficient：

$$
a_k(h)
=
\frac12
\Delta_h^2\Psi(kh),
$$

以及 prime-power tent localization。

本節點不再把固定孔徑只看成一個 matrix discretization，而直接研究連續變數：

$$
\boxed{
D_h(t)
:=
\frac12
\left[
\Psi(t+h)+\Psi(t-h)-2\Psi(t)
\right].
}
$$

對任意固定：

$$
h>0,
$$

本輪得到一個新的 AMRAL reduction：

$$
\boxed{
RH
\Longleftrightarrow
D_h(t)=O_h(1).
}
$$

更強地，反方向不需要 boundedness；只要存在任一有限 $A$ 使：

$$
D_h(t)
=
O_h(t^A),
$$

甚至只要：

$$
D_h(t)=e^{o(t)},
$$

就已足以推出 RH。

更重要的是，$D_h(t)$ 可以完全改寫成一個**固定 logarithmic aperture 內的 von Mangoldt 局部偏差**。對每一個 prime power $q=p^k$，其 arithmetic contribution 只在：

$$
[\log q-h,\log q+h]
$$

存在；超出此區間後 contribution 精確歸零。

因此：

```text
SCALAR CHECKPOINT MEMORY = INFINITE
FIXED-APERTURE SECOND-DIFFERENCE MEMORY = FINITE
```

每個 prime power 對 workload 只產生三個脈衝：

$$
+\frac{w_q}{2},
\qquad
-w_q,
\qquad
+\frac{w_q}{2},
$$

且三者淨和為：

$$
0.
$$

這建立了一個 **RH-equivalent fixed-aperture finite-memory prime process**。

**RH_CLAIM = False.**

本節點沒有證明所需的全域 boundedness / subexponential bound。

---

# 0. Claim register

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE

FIXED_APERTURE_SECOND_DIFFERENCE_CRITERION = CLOSED_AS_REDUCTION
LOCAL_PRIME_TENT_IDENTITY = CLOSED
DYADIC_WINDOW_COROLLARY = CLOSED_AS_REDUCTION

PRIME_MEMORY_LENGTH = 2h
PRIME_EVENT_NET_IMPULSE = ZERO

EVENTUAL_SERVICE_CURVATURE_POSITIVE = CLOSED_WITH_EXPLICIT_THRESHOLD
FINITE_MEMORY_CHECKPOINT_REDUCTION = CLOSED_AS_REDUCTION

GLOBAL_LOCAL_DISCREPANCY_BOUND = OPEN
SUBEXPONENTIAL_LOCAL_DISCREPANCY = OPEN
GLOBAL_RH_CERTIFICATE = FALSE
```

---

# 1. Suzuki 基線

Suzuki 定義：

$$
\Psi(t)
$$

並證明 one-sided Fourier/Laplace transform：

$$
\boxed{
\int_0^\infty
\Psi(t)e^{izt}\,dt
=
-\frac1{z^2}
\frac{\xi'}{\xi}
\left(
\frac12-iz
\right)
}
$$

最初對：

$$
\Im z>\frac12
$$

成立。

Suzuki 同時證明：

$$
\boxed{
RH
\Longleftrightarrow
\Psi(t)=O(1)
\quad
(t\to\infty).
}
$$

以及：

$$
\boxed{
RH
\Longleftrightarrow
\Psi(t)\ge0
\quad
\forall t.
}
$$

本節點使用的是 transform 與 boundedness structure，不重新證明 Suzuki theorem。

---

# 2. Fixed-aperture second difference

固定：

$$
h>0.
$$

定義 centered second difference：

$$
\Delta_h^2\Psi(t)
=
\Psi(t+h)+\Psi(t-h)-2\Psi(t).
$$

並定義：

$$
\boxed{
D_h(t)
=
\frac12
\Delta_h^2\Psi(t).
}
$$

對：

$$
t\ge h
$$

所有 arguments 皆非負，因此可直接使用 Suzuki 的 arithmetic formula。

v1.5 的 uniform box Toeplitz coefficient 正是 lattice restriction：

$$
\boxed{
a_k(h)
=
D_h(kh).
}
$$

所以：

```text
v1.5 Toeplitz sequence
=
v1.6 continuous local observable sampled on one lattice.
```

---

# 3. Fixed-Aperture Growth Criterion

## Theorem 3.1

對任意固定：

$$
h>0,
$$

下列敘述等價：

1. RH 成立；
2.

$$
D_h(t)=O_h(1);
$$

3. 存在有限：

$$
A\ge0
$$

使：

$$
D_h(t)=O_h(t^A);
$$

4.

$$
D_h(t)=e^{o(t)}.
$$

---

# 4. RH 推出 bounded local observable

若 RH 成立，Suzuki Theorem 1.6 給：

$$
\Psi(t)=O(1).
$$

因此：

$$
|D_h(t)|
\le
\frac12
\left(
|\Psi(t+h)|
+
|\Psi(t-h)|
+
2|\Psi(t)|
\right),
$$

所以：

$$
\boxed{
D_h(t)=O_h(1).
}
$$

因此：

$$
(1)\Longrightarrow(2)\Longrightarrow(3)\Longrightarrow(4).
$$

---

# 5. 二階差分多項式成長會迫使 $\Psi$ 多項式成長

現在假設存在：

$$
A<\infty
$$

使：

$$
D_h(t)=O(t^A).
$$

對每個：

$$
r\in[0,h)
$$

定義 lattice sequence：

$$
y_n(r)
=
\Psi(r+nh).
$$

則：

$$
y_{n+1}(r)
-
2y_n(r)
+
y_{n-1}(r)
=
2D_h(r+nh).
$$

因此：

$$
y_{n+1}-2y_n+y_{n-1}
=
O(n^A)
$$

uniformly in：

$$
r\in[0,h),
$$

因為初始 compact interval 上 $\Psi$ 連續有界。

一次求和得到：

$$
y_{n+1}-y_n
=
O(n^{A+1}),
$$

再求和得到：

$$
y_n
=
O(n^{A+2}).
$$

所以：

$$
\boxed{
\Psi(t)
=
O(t^{A+2}).
}
$$

---

# 6. Polynomial growth 排除偏軸零點

若：

$$
\Psi(t)=O(t^B)
$$

對某個有限 $B$，則：

$$
F(z)
=
\int_0^\infty
\Psi(t)e^{izt}\,dt
$$

對整個：

$$
\Im z>0
$$

絕對收斂並定義 holomorphic function。

而在：

$$
\Im z>\frac12
$$

已有：

$$
F(z)
=
-\frac1{z^2}
\frac{\xi'}{\xi}
\left(
\frac12-iz
\right).
$$

由 analytic / meromorphic continuation 的唯一性，右側不能在：

$$
\Im z>0
$$

具有 pole。

如果存在 nontrivial zero：

$$
\rho
=
\beta+i\gamma
$$

滿足：

$$
\beta>\frac12,
$$

令：

$$
z_\rho
=
-\gamma+i
\left(
\beta-\frac12
\right).
$$

則：

$$
\Im z_\rho>0
$$

且：

$$
\frac12-iz_\rho
=
\rho.
$$

因此：

$$
\frac{\xi'}{\xi}
\left(
\frac12-iz
\right)
$$

會在 $z_\rho$ 產生 pole，矛盾。

所以：

$$
\Re\rho\le\frac12
$$

對所有 zeros 成立。

利用 functional equation：

$$
\rho\longmapsto1-\rho,
$$

得到：

$$
\Re\rho\ge\frac12.
$$

故：

$$
\boxed{
\Re\rho=\frac12
}
$$

對所有 nontrivial zeros。

因此：

$$
(3)\Longrightarrow RH.
$$

---

# 7. Subexponential growth 也足夠

假設：

$$
D_h(t)=e^{o(t)}.
$$

固定任意：

$$
\varepsilon>0.
$$

則對充分大 $t$：

$$
|D_h(t)|
\le
e^{\varepsilon t}.
$$

對每個 residue lattice 二次求和不改變 exponential rate，因此：

$$
\Psi(t)
=
e^{o(t)}.
$$

所以對任意：

$$
y>0,
$$

最終：

$$
|\Psi(t)|
\le
e^{yt/2}.
$$

因此：

$$
\int_0^\infty
\Psi(t)e^{i(x+iy)t}\,dt
$$

仍絕對收斂。

同 Section 6，Laplace transform 延伸到整個 upper half-plane，故 RH。

所以：

$$
\boxed{
RH
\Longleftrightarrow
D_h(t)=e^{o(t)}
}
$$

對任意 fixed $h>0$。

---

# 8. Smooth / arithmetic split

對：

$$
t>0
$$

把 Suzuki arithmetic formula寫成：

$$
\Psi(t)
=
\mathcal A(t)
-
\sum_{n=p^k}
\frac{\Lambda(n)}{\sqrt n}
(t-\log n)_+.
$$

其中：

$$
\begin{aligned}
\mathcal A(t)
&=
4(e^{t/2}+e^{-t/2}-2)
\\
&\quad
+
ct
+
\frac C4
-
\sum_{m=0}^{\infty}
\frac{
e^{-(2m+\frac12)t}
}{
(2m+\frac12)^2
},
\end{aligned}
$$

且：

$$
c
=
\frac12
\left[
\frac{\Gamma'}{\Gamma}
\left(
\frac14
\right)
-\log\pi
\right].
$$

注意 $m=0$ term：

$$
\frac{
e^{-t/2}
}{
(1/2)^2
}
=
4e^{-t/2}
$$

與前面的：

$$
4e^{-t/2}
$$

精確抵消。

所以亦可寫成：

$$
\boxed{
\mathcal A(t)
=
4e^{t/2}
-8
+
ct
+
\frac C4
-
\sum_{m=1}^{\infty}
\frac{
e^{-(2m+\frac12)t}
}{
(2m+\frac12)^2
}.
}
$$

這個 cancellation 對 local criterion 很重要。

---

# 9. Prime ramp 的二階差分是 tent

定義：

$$
T_h(x)
=
(h-|x|)_+.
$$

對：

$$
a>0
$$

及：

$$
t\ge h,
$$

有：

$$
\Delta_h^2(t-a)_+
=
T_h(t-a).
$$

因此：

$$
\boxed{
D_h(t)
=
R_h(t)
-
\frac12
\sum_{n=p^k}
\frac{\Lambda(n)}{\sqrt n}
T_h(t-\log n),
}
$$

其中：

$$
R_h(t)
=
\frac12
\Delta_h^2\mathcal A(t).
$$

因為：

$$
T_h(t-\log n)=0
$$

除非：

$$
|t-\log n|<h,
$$

所以 sum 實際只包含：

$$
e^{t-h}<n<e^{t+h}.
$$

因此：

## Theorem 9.1 · Exact finite-memory arithmetic identity

$$
\boxed{
D_h(t)
=
R_h(t)
-
\frac12
\sum_{
\substack{
n=p^k\\
e^{t-h}<n<e^{t+h}
}
}
\frac{\Lambda(n)}{\sqrt n}
\left(
h-|t-\log n|
\right).
}
$$

任一 fixed $t$ 只需要 finite local prime-power data。

---

# 10. Long-memory erasure

scalar $\Psi(t)$ 中，一旦：

$$
t>\log n,
$$

prime power $n$ 的 contribution：

$$
-\frac{\Lambda(n)}{\sqrt n}
(t-\log n)
$$

會永久留在 state 中。

但 $D_h$ 中：

$$
-\frac12
\frac{\Lambda(n)}{\sqrt n}
T_h(t-\log n)
$$

只在：

$$
\log n-h<t<\log n+h
$$

存在。

所以單一 prime power 的 memory lifetime 精確為：

$$
\boxed{
2h.
}
$$

因此 fixed aperture 把：

```text
PERMANENT RAMP MEMORY
```

改成：

```text
COMPACT TENT MEMORY.
```

---

# 11. Exact local weighted prime discrepancy

定義 local weighted prime sum：

$$
\boxed{
L_h(t)
=
\sum_{
\substack{
n=p^k\\
e^{t-h}<n<e^{t+h}
}
}
\frac{\Lambda(n)}{\sqrt n}
\left(
h-|t-\log n|
\right).
}
$$

連續 PNT main density 對應：

$$
e^{u/2}\,du.
$$

而：

$$
\int_{t-h}^{t+h}
e^{u/2}
\left(
h-|t-u|
\right)
du
=
8e^{t/2}
\left(
\cosh\frac h2-1
\right).
$$

定義 local discrepancy：

$$
\boxed{
\mathcal E_h(t)
=
L_h(t)
-
8e^{t/2}
\left(
\cosh\frac h2-1
\right).
}
$$

---

# 12. Trivial / archimedean correction 完全顯式且快速衰減

由 Section 8 的 cancellation：

$$
R_h(t)
=
4e^{t/2}
\left(
\cosh\frac h2-1
\right)
-
\sum_{m=1}^{\infty}
\frac{
e^{-(2m+\frac12)t}
}{
(2m+\frac12)^2
}
\left[
\cosh
\left(
(2m+\tfrac12)h
\right)
-1
\right].
$$

因此：

$$
\boxed{
D_h(t)
=
-\frac12
\mathcal E_h(t)
-
\mathcal R_h(t),
}
$$

其中：

$$
\boxed{
\mathcal R_h(t)
=
\sum_{m=1}^{\infty}
\frac{
e^{-(2m+\frac12)t}
}{
(2m+\frac12)^2
}
\left[
\cosh
\left(
(2m+\tfrac12)h
\right)
-1
\right].
}
$$

對 fixed $h$：

$$
\boxed{
\mathcal R_h(t)
=
O_h(e^{-5t/2}).
}
$$

因此 local prime discrepancy 與 fixed-aperture second difference 的 asymptotic growth 完全等價。

---

# 13. Local Prime Discrepancy Criterion

由 Theorem 3.1 與 Section 12：

## Theorem 13.1

對任何 fixed：

$$
h>0,
$$

RH 等價於：

$$
\boxed{
L_h(t)
=
8e^{t/2}
\left(
\cosh\frac h2-1
\right)
+
O_h(1).
}
$$

更弱但仍等價的反向條件：

若存在某個有限：

$$
A
$$

使：

$$
\boxed{
L_h(t)
=
8e^{t/2}
\left(
\cosh\frac h2-1
\right)
+
O_h(t^A),
}
$$

則 RH 成立。

同樣：

$$
\boxed{
L_h(t)
-
8e^{t/2}
\left(
\cosh\frac h2-1
\right)
=
e^{o(t)}
}
$$

也足以推出 RH。

這是 fixed multiplicative window 的 purely local prime-power criterion。

---

# 14. $x$-variable version

令：

$$
x=e^t.
$$

則：

$$
e^{t-h}<n<e^{t+h}
$$

等價於：

$$
xe^{-h}<n<xe^h.
$$

所以：

## Corollary 14.1 · Fixed multiplicative window criterion

對任意 fixed：

$$
h>0,
$$

RH 等價於：

$$
\boxed{
\begin{aligned}
&
\sum_{
xe^{-h}<n<xe^h
}
\frac{\Lambda(n)}{\sqrt n}
\left(
h-\left|\log\frac nx\right|
\right)
\\
&\qquad=
8\sqrt x
\left(
\cosh\frac h2-1
\right)
+
O_h(1).
\end{aligned}
}
$$

其中 $\Lambda(n)$ 自動只在 prime powers 非零。

反方向甚至只需要 error：

$$
O_h((\log x)^A)
$$

for some finite $A$，或：

$$
x^{o(1)}.
$$

---

# 15. Dyadic window：固定看 $[x/2,2x]$

取：

$$
h=\log2.
$$

則：

$$
e^{-h}=\frac12,
$$

$$
e^h=2.
$$

而：

$$
\cosh
\left(
\frac{\log2}{2}
\right)
=
\frac{3}{2\sqrt2}.
$$

所以：

$$
8
\left[
\cosh
\left(
\frac{\log2}{2}
\right)
-1
\right]
=
6\sqrt2-8.
$$

因此：

## Corollary 15.1 · Dyadic Local Prime Criterion

RH 等價於：

$$
\boxed{
\begin{aligned}
&
\sum_{x/2<n<2x}
\frac{\Lambda(n)}{\sqrt n}
\left(
\log2
-
\left|
\log\frac nx
\right|
\right)
\\
&\qquad=
(6\sqrt2-8)\sqrt x
+
O(1).
\end{aligned}
}
$$

更弱的：

$$
O((\log x)^A)
$$

for any one finite $A$，若能無條件證明，也足以推出 RH。

這是一個非常具體的 closure target：

> 不需要控制 $[1,x]$ 的所有歷史 prime memory；只需對每個 $x$ 控制固定 multiplicative annulus $[x/2,2x]$ 中的一個 triangularly weighted discrepancy。

---

# 16. 與 Arias de Reyna tempered-measure criterion 的關係

Arias de Reyna 證明 RH 等價於 measure：

$$
\mu
=
-
\sum_{n=1}^{\infty}
\frac{\Lambda(n)}{\sqrt n}
\left(
\delta_{\log n}
+
\delta_{-\log n}
\right)
+
2\cosh(x/2)\,dx
$$

是 tempered distribution。

本節點的 local tent observable 與該 measure 的 compactly supported tent convolution 高度對齊。

這提供外部一致性：

```text
ARIAS DE REYNA:
GLOBAL PRIME-ARCH MEASURE TEMPEREDNESS

AMRAL v1.6:
ONE FIXED-APERTURE LOCAL TENT DISCREPANCY GROWTH
```

本節點沒有宣稱 Arias de Reyna theorem 等同於本文件所有細節，也沒有在 targeted search 之外建立完整 priority claim。

正確定位：

```text
RELATED TEMPERED-DISTRIBUTION FRAMEWORK = KNOWN
FIXED-APERTURE TENT COROLLARY = DERIVED HERE FROM SUZUKI FORMULA
NOVELTY_PRIORITY = NOT ESTABLISHED
```

---

# 17. Prime event triplet

令：

$$
q=p^k
$$

且：

$$
a_q=\log q,
$$

$$
w_q
=
\frac{\Lambda(q)}{\sqrt q}.
$$

其 contribution：

$$
-\frac{w_q}{2}
T_h(t-a_q).
$$

定義 local workload：

$$
Y_h(t)
=
-D_h'(t).
$$

當 $t$ 穿越：

$$
a_q-h,
$$

tent 開始，$Y_h$ jump：

$$
\boxed{
+\frac{w_q}{2}.
}
$$

當穿越 center：

$$
a_q,
$$

jump：

$$
\boxed{
-w_q.
}
$$

當穿越：

$$
a_q+h,
$$

jump：

$$
\boxed{
+\frac{w_q}{2}.
}
$$

總 impulse：

$$
\boxed{
\frac{w_q}{2}
-w_q
+\frac{w_q}{2}
=
0.
}
$$

所以單一 prime power 不產生永久 workload memory。

---

# 18. Local workload in sliding-window form

令：

$$
W_-(t)
=
\sum_{
t-h<\log q<t
}
w_q,
$$

以及：

$$
W_+(t)
=
\sum_{
t<\log q<t+h
}
w_q.
$$

在非 event point：

$$
D_h'(t)
=
R_h'(t)
+
\frac12W_-(t)
-
\frac12W_+(t).
$$

所以：

$$
\boxed{
Y_h(t)
=
-R_h'(t)
-
\frac12W_-(t)
+
\frac12W_+(t).
}
$$

也就是：

> workload 只看當前 logarithmic window 中「左半窗與右半窗」的 weighted prime-power imbalance。

不存在從 $0$ 累積到 $t$ 的永久 Chebyshev memory。

---

# 19. Smooth service curvature

prime tent 在 event points 之外皆為 linear。

因此在任意相鄰 event points 間：

$$
\boxed{
D_h''(t)
=
R_h''(t).
}
$$

由：

$$
\mathcal A''(t)
=
e^{t/2}
-
\frac{
e^{-5t/2}
}{
1-e^{-2t}
}
$$

以及：

$$
\frac{
e^{-5t/2}
}{
1-e^{-2t}
}
=
\sum_{m=1}^{\infty}
e^{-(2m+\frac12)t},
$$

得到：

$$
\boxed{
\begin{aligned}
R_h''(t)
&=
e^{t/2}
\left(
\cosh\frac h2-1
\right)
\\
&\quad
-
\sum_{m=1}^{\infty}
e^{-(2m+\frac12)t}
\left[
\cosh
\left(
(2m+\tfrac12)h
\right)
-1
\right].
\end{aligned}
}
$$

因此：

$$
R_h''(t)>0
$$

對充分大 $t$ 必成立。

---

# 20. 一個顯式 service-curvature threshold

令：

$$
c_h
=
\cosh\frac h2-1>0.
$$

對：

$$
t>h
$$

使用：

$$
\cosh x-1<\frac12e^x
$$

得到 tail upper bound：

$$
\sum_{m=1}^{\infty}
e^{-(2m+\frac12)t}
\left[
\cosh
\left(
(2m+\tfrac12)h
\right)
-1
\right]
<
\frac12
\frac{
e^{-\frac52(t-h)}
}{
1-e^{-2(t-h)}
}.
$$

若：

$$
t-h
\ge
\frac{\log2}{2},
$$

則 denominator 至少為：

$$
\frac12,
$$

故 tail：

$$
\le
e^{-\frac52(t-h)}.
$$

因此充分條件：

$$
e^{t/2}c_h
>
e^{-\frac52(t-h)}.
$$

也就是：

$$
t
>
\frac{
\frac52h-\log c_h
}{
3}.
$$

所以可取：

$$
\boxed{
T_{\rm svc}(h)
=
\max
\left\{
h+\frac{\log2}{2},
\,
\frac{
\frac52h-\log(\cosh(h/2)-1)
}{
3}
\right\}.
}
$$

則：

$$
\boxed{
t>T_{\rm svc}(h)
\Longrightarrow
R_h''(t)>0.
}
$$

這個 threshold 是保守的，不是 sharp threshold。

---

# 21. Local service clock

在：

$$
t>T_{\rm svc}(h)
$$

定義：

$$
\tau_h(t)
=
R_h'(t).
$$

因為：

$$
R_h''(t)>0,
$$

$\tau_h$ 嚴格遞增。

在 prime triplet events 之外：

$$
Y_h=-D_h',
$$

所以：

$$
\frac{dY_h}{dt}
=
-R_h''(t).
$$

而：

$$
\frac{d\tau_h}{dt}
=
R_h''(t).
$$

因此：

$$
\boxed{
\frac{dY_h}{d\tau_h}
=
-1.
}
$$

這與 Mittermeier service-clock geometry 形式相同，但 arithmetic event law 不同：

Mittermeier scalar $\Psi$：

```text
one prime event -> permanent positive workload jump
```

AMRAL fixed-aperture $D_h$：

```text
one prime event -> enter / center / exit neutral triplet
```

---

# 22. Finite-memory checkpoint intervals

定義 event set：

$$
\boxed{
\mathcal T_h
=
\{
\log q-h,\,
\log q,\,
\log q+h
:
q=p^k
\}.
}
$$

把：

$$
\mathcal T_h\cap(T_{\rm svc}(h),\infty)
$$

排序成：

$$
s_1<s_2<s_3<\cdots
$$

並合併 coincident events。

在每個 open event interval：

$$
(s_j,s_{j+1}),
$$

有：

$$
D_h''(t)>0.
$$

因此：

$$
\boxed{
D_h
\text{ is strictly convex on every late event interval}.
}
$$

所以每個 interval：

- maximum 只可能出現在 endpoints；
- interior minimum 至多一個；
- interior minimum 若存在，由：

$$
Y_h(t)=0
$$

唯一決定。

因此 continuous global boundedness 可壓成 countable checkpoint family：

```text
event endpoints
+
at most one interior constrained minimum per event interval.
```

與 scalar prime-power checkpoint 不同，這裡每個 checkpoint 只需 sliding window 中的 finite active prime set。

---

# 23. Finite-Memory Checkpoint Criterion

## Theorem 23.1

固定 $h>0$。

忽略有限初始區間：

$$
[0,T_{\rm svc}(h)].
$$

則：

$$
D_h(t)=O(1)
$$

等價於：

1. 所有 late event endpoint values：

$$
D_h(s_j)
$$

uniformly bounded；

2. 所有存在的 interior constrained minima：

$$
D_h(t_j^\ast)
$$

uniformly bounded below。

因為每個 event interval strictly convex，這兩組資料控制整個 interval 的上、下界。

結合 Theorem 3.1：

$$
\boxed{
RH
\Longleftrightarrow
\text{all fixed-aperture event checkpoints remain uniformly bounded}.
}
$$

這仍然是 infinite checkpoint problem。

但每個 checkpoint 的 arithmetic memory 是 finite sliding window，而不是 full history。

---

# 24. v1.5 Toeplitz interpretation

在 lattice：

$$
t=kh,
$$

有：

$$
a_k(h)=D_h(kh).
$$

因此 local discrepancy criterion 的 lattice samples正是 canonical Toeplitz lags。

v1.5 prime tent formula：

$$
a_k^{\rm fin}(h)
=
-\frac12
\sum_{p^r}
\frac{\Lambda(p^r)}{p^{r/2}}
T_h(kh-\log p^r)
$$

對：

$$
k\ge1
$$

只需要 annulus：

$$
\boxed{
e^{(k-1)h}
<
p^r
<
e^{(k+1)h}.
}
$$

所以從 Toeplitz prefix order $k$ 擴到 $k+1$ 時，新 arithmetic coefficient只需要下一個 local annulus。

---

# 25. Prime event matrix update 是不定的

令：

$$
\frac{\log q}{h}
=
r+\theta,
$$

其中：

$$
r=\left\lfloor\frac{\log q}{h}\right\rfloor,
$$

$$
0\le\theta<1.
$$

令：

$$
J_r
$$

為 finite unilateral shift matrix：

$$
(J_r)_{i,i+r}=1.
$$

則單一 prime power $q$ 對 $m\times m$ box matrix 的 update 精確為：

$$
\boxed{
U_q
=
-\frac{w_qh}{2}
\left[
(1-\theta)
(J_r+J_r^\ast)
+
\theta
(J_{r+1}+J_{r+1}^\ast)
\right].
}
$$

對：

$$
r\ge1
$$

且 update 非零時，$U_q$ 的 diagonal 為零，所以：

$$
\operatorname{tr}U_q=0.
$$

但：

$$
U_q\neq0.
$$

Hermitian nonzero matrix 若 semidefinite 且 trace 為零，只能是零矩陣。

因此：

$$
\boxed{
r\ge1
\Longrightarrow
U_q
\text{ is indefinite}.
}
$$

所以：

> prime powers 在 matrix route 中不是一個個 negative-semidefinite cost。

這排除一條錯誤 proof strategy：

```text
positive arch matrix
minus a monotone sequence of PSD prime costs.
```

實際上 prime update 具有 direction-dependent sign。

---

# 26. Memory–Inertia Tradeoff

現在可以明確描述兩條 route 的 tradeoff。

## Scalar $\Psi$ route

優點：

- 一維；
- convex checkpoint；
- scalar capacity-cost。

代價：

- 每個 prime ramp 永久存在；
- arithmetic memory 從 $0$ 累積到 $t$；
- tail 變成 smoothed Chebyshev memory。

## Fixed-aperture / Toeplitz route

優點：

- 每個 prime power 只有 lifetime $2h$；
- coefficient只依賴 local annulus；
- prime history 精確被 second difference erase。

代價：

- matrix prime update indefinite；
- sign information 轉移到 cross-correlation / inertia；
- scalar monotonicity消失。

因此：

$$
\boxed{
\text{erase long arithmetic memory}
\Longleftrightarrow
\text{introduce directional inertia complexity}.
}
$$

這是本節點的核心結構觀察之一。

---

# 27. Levinson / Verblunsky state compression

固定 $h$，定義 real symmetric Toeplitz coefficients：

$$
a_0,a_1,a_2,\ldots
$$

其中：

$$
a_k=D_h(kh).
$$

假設目前 prefix：

$$
T_m
=
[a_{i-j}]_{i,j=0}^{m-1}
$$

positive definite。

從：

$$
T_m
$$

擴張到：

$$
T_{m+1}
$$

只需要新增：

$$
a_m.
$$

block form：

$$
T_{m+1}
=
\begin{pmatrix}
T_m & b_m\\
b_m^\ast & a_0
\end{pmatrix},
$$

其中：

$$
b_m
=
(a_m,a_{m-1},\ldots,a_1)^\top.
$$

Schur innovation：

$$
\boxed{
E_m
=
a_0
-
b_m^\ast
T_m^{-1}
b_m.
}
$$

則：

$$
\boxed{
T_{m+1}\succ0
\Longleftrightarrow
T_m\succ0
\text{ and }
E_m>0.
}
$$

而：

$$
E_m
=
\frac{
\det T_{m+1}
}{
\det T_m
}.
$$

---

# 28. Reflection coefficient recursion

classical Levinson / Szegő recursion 可把：

$$
E_m
$$

寫成：

$$
\boxed{
E_m
=
E_{m-1}
\left(
1-|\alpha_{m-1}|^2
\right),
}
$$

其中：

$$
\alpha_j
$$

是 Verblunsky / Schur / reflection coefficients。

因此 prefix strict positivity 等價於：

$$
\boxed{
|\alpha_j|<1
}
$$

逐步成立。

這建立一個 exact state machine：

```text
INPUT:
    new local coefficient a_m
    <- only local prime annulus + arch term

STATE:
    previous Levinson / prediction coefficients
    previous innovation E_{m-1}

UPDATE:
    reflection coefficient alpha_{m-1}

GATE:
    |alpha_{m-1}| < 1
```

這把 high-dimensional PSD extension 壓成一個 scalar gate per matrix dimension。

但：

```text
FIXED h ALL REFLECTION GATES
!=
KNOWN RH EQUIVALENCE
```

除非再處理 fixed-lattice completeness / all-h quantifier。

---

# 29. RH 下 reflection energy 不會收斂成固定 margin

v1.5 已指出，在 RH 下 fixed-$h$ spectral measure 是 pure atomic。

Szegő theorem：

$$
\prod_{j=0}^{\infty}
\left(
1-|\alpha_j|^2
\right)
=
\exp
\left[
\int
\log w
\right].
$$

pure singular / atomic spectral measure 的 absolutely continuous density $w$ 幾乎處處為零，所以右側為：

$$
0.
$$

因此 RH 下：

$$
\boxed{
\prod_{j=0}^{\infty}
\left(
1-|\alpha_j|^2
\right)
=
0.
}
$$

以及：

$$
\boxed{
\sum_{j=0}^{\infty}
|\alpha_j|^2
=
\infty
}
$$

在標準 Szegő dichotomy 下。

所以：

> reflection coefficients 的任務不是最終衰減到一個 uniformly safe zero-state。

系統在 RH 真時仍然具有無限累積的 prediction structure。

這再次排除 uniform-margin proof strategy。

---

# 30. 目前真正的新 closure target

v1.6 之後，正向問題可以改寫成：

$$
\boxed{
\text{Can one prove that the fixed-aperture local discrepancy is subexponential?}
}
$$

也就是，對某一個 fixed $h$：

$$
\boxed{
\mathcal E_h(t)=e^{o(t)}.
}
$$

由本節點 theorem，這已足以閉合 RH。

取：

$$
h=\log2
$$

時，目標尤其具體：

$$
\boxed{
\begin{aligned}
&
\sum_{x/2<n<2x}
\frac{\Lambda(n)}{\sqrt n}
\left(
\log2
-
\left|\log\frac nx\right|
\right)
\\
&\qquad
-
(6\sqrt2-8)\sqrt x
=
x^{o(1)}.
\end{aligned}
}
$$

若能提高到：

$$
O((\log x)^A),
$$

任一 finite $A$ 都足夠。

RH 真時更應有：

$$
O(1).
$$

---

# 31. 為何這可能比 cumulative memory 更適合 AMRAL

這個 target 仍然具有 RH 的完整難度。

但它有工程優勢：

1. 固定 window；
2. finite prime data per $x$；
3. no ancient prime memory；
4. exact compact kernel；
5. event dynamics finite-state in arithmetic window；
6. smooth service curvature eventual positive；
7. 可做 streaming interval certificate；
8. 可與 Toeplitz / Levinson state cross-check；
9. 若出現超出 bound 的事件，可精確定位到一個 multiplicative annulus；
10. 可直接做 independent prime-side reproduction。

因此下一步不必再追新的 RH-equivalent function。

可以直接研究：

```text
LOCAL PRIME DISCREPANCY DYNAMICS.
```

---

# 32. 下一節點

建議：

`RH-LocalPrime-SubexponentialBridge-v1.7`

主要研究：

### A. Analytic side

能否從：

- zero-density；
- zero-free region；
- weighted short-interval PNT；
- Mellin transform；
- local smoothing；

推出比目前：

$$
e^{t/2-c\sqrt t}
$$

更接近 subexponential 的 bound？

---

### B. Event-dynamics side

利用 neutral triplet：

$$
+\frac12w,\,-w,\,+\frac12w
$$

尋找：

- cancellation invariant；
- local conservation law；
- paired-event domination；
- left-right prime mass balance；
- event-cluster compensation。

---

### C. Matrix side

把 local discrepancy coefficient：

$$
a_m
$$

送入 Levinson recursion，研究：

$$
|\alpha_m|<1
$$

是否可由 local annulus data + previous finite state 維持。

---

### D. Formalization

優先形式化 Theorem 3.1：

```text
subexponential fixed second difference
=> polynomial/subexponential Psi
=> upper-half-plane Laplace holomorphy
=> no off-axis zeros
=> RH.
```

這是一個 dependency graph 很短的 formal target。

---

# 33. GAP ledger

## CLOSED / REDUCED

### G1. Fixed-aperture RH reduction

```text
CLOSED_AS_REDUCTION
```

$$
RH
\Longleftrightarrow
D_h=O(1).
$$

---

### G2. Polynomial / subexponential sufficiency

```text
CLOSED_AS_REDUCTION
```

任一 fixed $h$：

$$
D_h=O(t^A)
$$

或：

$$
D_h=e^{o(t)}
$$

都足以推出 RH。

---

### G3. Local prime identity

```text
CLOSED
```

只使用：

$$
e^{t-h}<p^k<e^{t+h}.
$$

---

### G4. Dyadic local criterion

```text
CLOSED_AS_REDUCTION
```

只看：

$$
[x/2,2x].
$$

---

### G5. Prime memory lifetime

```text
CLOSED
```

每個 prime power：

$$
2h.
$$

---

### G6. Neutral triplet event law

```text
CLOSED
```

net impulse：

$$
0.
$$

---

### G7. Eventual service curvature

```text
CLOSED_WITH_CONSERVATIVE_THRESHOLD
```

$$
t>T_{\rm svc}(h)
\Longrightarrow
R_h''(t)>0.
$$

---

### G8. Prime matrix update monotonicity

```text
NO_GO
```

late prime update generally indefinite。

---

## OPEN

### G9. Uniform local discrepancy bound

```text
OPEN
```

---

### G10. Subexponential local discrepancy

```text
OPEN
```

這一項若關閉，即關閉 RH。

---

### G11. Event-cluster invariant

```text
OPEN
```

---

### G12. Reflection-state invariant

```text
OPEN
```

---

### G13. RH

```text
OPEN
```

---

# 34. Trust boundary

必須保留：

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE

FIXED_APERTURE_EQUIVALENCE = REDUCTION_ONLY
LOCAL_PRIME_CRITERION = REDUCTION_ONLY

NO SUBEXPONENTIAL BOUND HAS BEEN PROVED
NO O(1) LOCAL ERROR HAS BEEN PROVED UNCONDITIONALLY

NOVELTY_PRIORITY = NOT ESTABLISHED
GLOBAL_RH_CERTIFICATE = FALSE
```

禁止：

$$
\text{finite-memory formulation}
\Longrightarrow
\text{problem solved}.
$$

禁止：

$$
\text{finite prime data per checkpoint}
\Longrightarrow
\text{finite global proof}.
$$

真正剩餘的 all-scale condition 仍然是：

$$
t\to\infty.
$$

---

# 35. 一句話狀態

> v1.6 把 v1.5 的 box second difference 從 matrix discretization 升級成一條固定孔徑 RH-equivalent local prime criterion。對任意固定 $h>0$，$D_h(t)=\frac12\Delta_h^2\Psi(t)$ bounded、任意有限多項式成長、甚至 subexponential growth 都足以推出 RH；而 $D_h$ 的 arithmetic side只依賴 $[e^{t-h},e^{t+h}]$ 中的 prime powers，每個 prime power 只留下長度 $2h$ 的 tent memory，對 workload 造成 $+\frac12w,-w,+\frac12w$ 的淨零三脈衝。取 $h=\log2$，RH 等價於固定 dyadic annulus $[x/2,2x]$ 中 triangularly weighted von Mangoldt sum具有 $(6\sqrt2-8)\sqrt x+O(1)$ 的局部漸近；反方向甚至任何 polylog 或 $x^{o(1)}$ error 都足以閉合 RH。這把 cumulative Chebyshev memory 換成 finite-memory local discrepancy，但代價是 matrix prime updates變成 indefinite、全域困難轉移到 local cancellation / inertia preservation。下一節點應直接攻 local discrepancy 的 subexponential bridge，而不是再創造新的 RH equivalent criterion。

---

# 36. References

1. Masatoshi Suzuki, **Aspects of the screw function corresponding to the Riemann zeta-function**, *Journal of the London Mathematical Society* 108 (2023), 1448–1487.  
   DOI: https://doi.org/10.1112/jlms.12785

2. Masatoshi Suzuki, **Weil's quadratic form via the screw function**, arXiv:2606.09096, 2026.  
   https://arxiv.org/abs/2606.09096

3. Juan Arias de Reyna, **Explicit formula and quasicrystal definition**, arXiv:2402.10604, current source dated 2026-03-22.  
   https://arxiv.org/abs/2402.10604

4. Rainer Andreas Mittermeier, **Recovery Witnesses in the Prime-Power Checkpoint Program: Service-Clock Geometry and an Exact Quantifier Reduction for the Riemann-Hypothesis Tail -- Part 4**, 2026.  
   https://zenodo.org/records/22076079

5. Rainer Andreas Mittermeier, **Deep Episodes in the Prime-Power Checkpoint Program: An Unconditional Terminal-Episode Theorem, an Exact Chebyshev Bridge, and Sharp Recovery Recurrence -- Part 5**, 2026.  
   https://zenodo.org/records/22076088

6. NIST Digital Library of Mathematical Functions, **§18.33 Polynomials Orthogonal on the Unit Circle**, Verblunsky and Szegő recurrences.  
   https://dlmf.nist.gov/18.33

7. Barry Simon, **Orthogonal Polynomials on the Unit Circle, Part 1: Classical Theory**, AMS Colloquium Publications 54.1, 2005.

8. AMRAL, **算術矩陣與半正定證書原型 · v0.1**.  
   https://amral.evemisslab.com/riemann/autonomous/p/proto-arithmetic-matrix-psd-v0.1/

9. AMRAL, **等變算術障礙整合總論 · v1.0**.  
   https://amral.evemisslab.com/riemann/semi-autonomous/p/proto-equivariant-arithmetic-obstruction-integration-v1.0/

10. AMRAL, **局部區間 Green 位置覆蓋 · v1.0**.  
    https://amral.evemisslab.com/riemann/semi-autonomous/p/proto-localintervalgreen-cellcover-v1.0/

---

# 37. Provenance

研究主導：Neo.K

v1.6 數學續推、fixed-aperture reduction、finite-memory event formulation、local-prime criterion 與 canonical source 整理：ChatGPT / GPT-5.6 Sol

日期：2026-09-02

研究定位：AMRAL 黎曼猜想半自主研究線，第三弧線 fixed-aperture local-prime / finite-memory 節點。

本文件是 research source artifact，不是 peer-reviewed publication。

所有 claim 必須依 Claim register、GAP ledger 與 Trust boundary 解讀。
