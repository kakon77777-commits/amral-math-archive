工程紀錄 · 第三弧線 v1.2 · 2026-09-02 · GLOBAL_QUANTIFIER_COMPRESSION · RH_CLAIM_FALSE

# 全域量詞壓縮：有限高度 Li 極值與質數冪凸最小值判準

**RH-GlobalQuantifier-PrimePowerConvexCompression v1.2**

本節點承接：

`RH-ConditionalOffAxisCell-ZetaTransfer-v1.1`

上一節點已把 hypothetical off-axis zero 的最弱存在性接口壓成有理 off-axis cell，並辨識出水平偏移

$$
\delta=\Re\rho-\frac12
$$

不能從 occupancy representation 中刪除。

本節點不再擴大 local Green radius，而集中處理真正的全域量詞：

$$
\text{How can an unbounded zero/location quantifier be compressed into auditable finite or countable objects?}
$$

本輪得到兩條互補壓縮：

1. **zero side**：任一已知 off-axis cell 都會給出一個顯式有限高度，保證 Li transform 的全域 extremal modulus 必在該有限高度以下出現；
2. **prime side**：利用 Suzuki 的顯式算術函數 $\Psi(t)$，把連續條件

$$
\Psi(t)\ge0
\quad
\forall t\ge0
$$

進一步壓成「每一對相鄰 prime powers 之間只需檢查一個 convex minimum」的離散序列。

第二條尤其貼近 AMRAL 既有的 Green / arithmetic matrix / interval-certificate 路線，因為它完全在已知的 prime-power 位置上工作，不需要先知道 zeta zeros。

**RH_CLAIM = False.**

本文件不宣稱證明或否證黎曼猜想。本文的主要新內容是 AMRAL 內部的 reduction / synthesis；未主張其 exact formulation 在外部文獻中從未出現。

---

# 0. 先修正 v1.1 的一個 GAP 標記

v1.1 把

```text
GLOBAL_WEIL_ISOLATION = FALSE
```

整體標成 OPEN。

這個標記過粗。

AMRAL 自己先前的 `RH-W-03` 已經引用 Weil / Yoshida / Suzuki 類 compact-support positivity criterion，登錄：

```text
RH-W-03-FULL-COMPACT-SEPARATION = CLOSED_BY_KNOWN_CRITERION
RH-W-03-SPECTRAL-ISOLATION = REFERENCE_CLOSED
RH-W-03-CONSTRUCTIVE-WITNESS = OPEN_ENGINEERING
```

Suzuki 的結果亦給出：

$$
RH
\Longleftrightarrow
W(\psi\ast\widetilde\psi)\ge0
\quad
\forall\psi\in C_c^\infty(\mathbb R),
$$

以及等價的 compact-support Hermitian-form positivity family。

因此，若 RH 為假，**某個 compactly supported global negative witness 的存在性**已由既有判準關閉。

正確拆分應為：

```text
GLOBAL_WEIL_NEGATIVE_WITNESS_EXISTENCE = CLOSED_BY_KNOWN_CRITERION
OFFAXIS_CELL_TO_EXPLICIT_WITNESS_MAP = OPEN
FINITE_INTERVAL_CERTIFIED_WITNESS_GENERATOR = OPEN_ENGINEERING
```

所以 v1.2 不再把「是否存在 global negative witness」當成新的數學 GAP。

真正值得研究的是：

$$
\boxed{
\text{hypothetical / localized off-axis data}
\Longrightarrow
\text{constructive, certified, replayable witness}.
}
$$

---

# 1. Zero-side：一個 off-axis cell 已足以把 extremal search 壓到有限高度

令

$$
\rho=\beta+i\gamma
$$

為非平凡零點，並定義 Li / Möbius transform

$$
w_\rho
=
1-\frac1\rho.
$$

直接計算：

$$
|w_\rho|^2
=
\frac{(\beta-1)^2+\gamma^2}{\beta^2+\gamma^2}
=
1+\frac{1-2\beta}{\beta^2+\gamma^2}.
$$

如果

$$
\beta<\frac12,
$$

則

$$
|w_\rho|>1.
$$

同時因為

$$
0<\beta<1,
$$

所以

$$
1-2\beta<1,
$$

並且

$$
\beta^2+\gamma^2\ge\gamma^2.
$$

因此得到 uniform bound：

$$
\boxed{
|w_\rho|^2
<
1+\frac1{\gamma^2}
}
$$

對每一個左半側 off-axis zero 都成立。

注意這個估計：

- 不依賴 zero-free region；
- 不依賴 RH；
- 不依賴 zero density；
- 只用臨界帶

$$
0<\beta<1.
$$

這正是有限高度壓縮的核心。

---

# 2. Cell lower bound

沿用 v1.1 的右半側 off-axis cell：

$$
C=
[\delta_-,\delta_+]
\times
[\gamma_-,\gamma_+]
$$

其中

$$
0<\delta_-<\delta_+<\frac12,
$$

$$
H_0<\gamma_-<\gamma_+,
$$

且右半側 zero 寫成

$$
\rho_+
=
\frac12+\delta+i\gamma.
$$

由 functional-equation symmetry，其左半側 mirror 為

$$
\rho_-
=
\frac12-\delta+i\gamma.
$$

對左側 mirror：

$$
\beta=\frac12-\delta.
$$

因此

$$
1-2\beta=2\delta.
$$

所以

$$
|w_{\rho_-}|^2
=
1+
\frac{2\delta}
{(\frac12-\delta)^2+\gamma^2}.
$$

對整個 cell，可取嚴格下界

$$
r_C^2
:=
1+
\frac{2\delta_-}
{(\frac12-\delta_-)^2+\gamma_+^2}.
$$

於是：

$$
\boxed{
|w_{\rho_-}|
\ge r_C>1.
}
$$

---

# 3. Finite-height extremal compression theorem

定義

$$
T_C
:=
\frac1{\sqrt{r_C^2-1}}.
$$

把上一節的 $r_C$ 展開：

$$
\boxed{
T_C
=
\sqrt{
\frac{
(\frac12-\delta_-)^2+\gamma_+^2
}{
2\delta_-
}
}.
}
$$

現在考慮任何左半側 nontrivial zero

$$
\rho=\beta+i\gamma
$$

滿足

$$
|\gamma|>T_C.
$$

由 uniform bound：

$$
|w_\rho|^2
<
1+\frac1{\gamma^2}
<
1+\frac1{T_C^2}
=
r_C^2.
$$

所以：

$$
|w_\rho|<r_C.
$$

而 cell 中至少一個 mirror zero 滿足

$$
|w_{\rho_-}|\ge r_C.
$$

因此得到：

## Theorem 3.1 · Conditional finite-height extremal compression

若

$$
N_\zeta(C)\ge1,
$$

則 Li transform 的全域最大模

$$
R
=
\sup_{\rho:\Re\rho<1/2}
\left|
1-\frac1\rho
\right|
$$

必在有限高度

$$
|\Im\rho|\le T_C
$$

內達到。

亦即：

$$
\boxed{
N_\zeta(C)\ge1
\Longrightarrow
R
=
\max_{
\substack{
\Re\rho<1/2\\
|\Im\rho|\le T_C
}
}
\left|
1-\frac1\rho
\right|.
}
$$

因為任一 bounded height strip 內只有有限多個 zeta zeros，extremal set 也是有限集合。

這裡第一次把：

$$
|\gamma|\in[0,\infty)
$$

的 extremal search 變成：

$$
|\gamma|\le T_C.
$$

這個 $T_C$ 完全由 rational cell bounds 算出。

---

# 4. 對 Bombieri–Lagarias extremal argument 的意義

Bombieri–Lagarias 證明 Li criterion 時，若某個 zero 落在錯誤半平面，會選出 transformed modulus 的有限 extremal set，並利用 simultaneous Diophantine approximation 讓 extremal phases 同時靠近相位 $0$，使其 exponential contribution 壓過其餘部分。

原證明的重要結構是：

$$
R>R_2
$$

其中：

- $R$ 是 extremal modulus；
- $R_2$ 是 non-extremal 部分的嚴格較小基底。

本節點增加的工程資訊是：

> 若已經有一個 rational off-axis cell，則「extremal set 在哪個高度內」不必只以抽象存在性處理；可以用 $T_C$ 顯式界定。

所以後續 certificate 可以要求：

```text
off_axis_cell
extremal_search_height = T_C
finite_zero_isolation_below_T_C
extremal_set
second_modulus_bound
phase_alignment_integer_n
```

這仍然是 conditional architecture，不是 RH proof。

---

# 5. Fixed-$n$ 的高零點 tail 也可以顯式控制

這一節不是 RH closure，而是提供可驗證器使用的 tail contract。

令一個 symmetry orbit 的 Li contribution 記為

$$
Q_n(\rho).
$$

對 off-axis quartet，若

$$
w_\rho=e^z,
$$

則可寫成

$$
Q_n(\rho)
=
4
-
2\operatorname{Re}
\left(
w_\rho^n+w_\rho^{-n}
\right)
=
-4\operatorname{Re}
\left(
\cosh(nz)-1
\right).
$$

若

$$
|\rho|\ge2
$$

則

$$
\left|
\log\left(1-\frac1\rho\right)
\right|
\le
\frac{1/|\rho|}{1-1/|\rho|}
\le
\frac2{|\rho|}.
$$

若再要求

$$
|\rho|\ge2n,
$$

則

$$
|nz|\le1.
$$

利用

$$
|\cosh u-1|
\le
\frac{|u|^2}{2}e^{|u|},
$$

得到保守 bound：

$$
|Q_n(\rho)|
\le
8e\,
\frac{n^2}{|\rho|^2}.
$$

臨界線上的退化二元 orbit 也滿足更強的同階 bound，所以可以統一使用上述常數。

因此，對

$$
T\ge2n,
$$

高零點尾端滿足：

$$
\left|
\sum_{\gamma>T}Q_n(\rho)
\right|
\le
8e\,n^2
\sum_{\gamma>T}\frac1{\gamma^2}.
$$

---

# 6. 用顯式 $N(T)$ bound 封住 tail

Hasanalizade–Shen–Wong 給出，對

$$
T\ge e,
$$

$$
\left|
N(T)
-
\frac{T}{2\pi}
\log\frac{T}{2\pi e}
\right|
\le
A\log T
+
B\log\log T
+
C
$$

其中可取

$$
A=0.1038,
$$

$$
B=0.2573,
$$

$$
C=9.3675.
$$

令

$$
S_2(T)
=
\sum_{\gamma>T}\frac1{\gamma^2}.
$$

Stieltjes integration by parts 給：

$$
S_2(T)
=
-\frac{N(T)}{T^2}
+
2\int_T^\infty
\frac{N(t)}{t^3}\,dt.
$$

丟掉第一個非正項，並用

$$
\log\log t\le\log t
$$

對

$$
t\ge e
$$

做保守估計，可得：

$$
\boxed{
S_2(T)
\le
\frac{\log(T/2\pi)}{\pi T}
+
\frac{
(A+B)(\log T+\frac12)+C
}{T^2}.
}
$$

因此，若

$$
T\ge\max(e,2n),
$$

可得 explicit tail contract：

$$
\boxed{
\left|
\sum_{\gamma>T}Q_n(\rho)
\right|
\le
8e\,n^2
\left[
\frac{\log(T/2\pi)}{\pi T}
+
\frac{
(A+B)(\log T+\frac12)+C
}{T^2}
\right].
}
$$

這表示任一固定 Li index $n$ 的 zero-side sign certificate 可以被拆成：

$$
\text{finite low-zero interval sum}
+
\text{explicit analytic tail}.
$$

再次強調：

$$
\text{finite verification of }\lambda_n
\not\Longrightarrow
RH.
$$

---

# 7. Prime-side pivot：Suzuki 的 $\Psi(t)$

Li 路線把 global quantifier 壓成：

$$
n\in\mathbb N.
$$

但 AMRAL 既有工程更接近 compact-support / Green / arithmetic side。

Suzuki 定義一個完全顯式的 real-valued continuous function：

$$
\begin{aligned}
\Psi(t)
&=
4(e^{t/2}+e^{-t/2}-2)
\\
&\quad
-
\sum_{n\le e^t}
\frac{\Lambda(n)}{\sqrt n}
(t-\log n)
\\
&\quad
+
\frac t2
\left[
\frac{\Gamma'}{\Gamma}
\left(\frac14\right)
-\log\pi
\right]
\\
&\quad
+
\frac14
\left[
C
-
e^{-t/2}
\Phi(e^{-2t},2,\tfrac14)
\right],
\end{aligned}
$$

其中

$$
C=\pi^2+8G
$$

而 $G$ 是 Catalan constant。

Suzuki 證明：

$$
\boxed{
RH
\Longleftrightarrow
\Psi(t)\ge0
\quad
\forall t\in\mathbb R.
}
$$

並且無條件證明存在

$$
t_0>\log2
$$

使

$$
\Psi(t)>0
$$

對

$$
0<t<t_0
$$

成立。

所以真正需要處理的 global interval 可以從

$$
t\ge\log2
$$

開始。

---

# 8. 把 prime side 拆成「smooth backbone − prime-power ramps」

定義 smooth archimedean backbone：

$$
\begin{aligned}
\mathcal A(t)
&:=
4(e^{t/2}+e^{-t/2}-2)
\\
&\quad
+
\frac t2
\left[
\frac{\Gamma'}{\Gamma}
\left(\frac14\right)
-\log\pi
\right]
\\
&\quad
+
\frac14
\left[
C
-
e^{-t/2}
\Phi(e^{-2t},2,\tfrac14)
\right].
\end{aligned}
$$

則

$$
\boxed{
\Psi(t)
=
\mathcal A(t)
-
\sum_{n\le e^t}
\frac{\Lambda(n)}{\sqrt n}
(t-\log n).
}
$$

因為 $\Lambda(n)$ 只在 prime powers

$$
n=p^k
$$

時非零，所以 $\Psi$ 是：

> 一條 smooth backbone，減去一族在已知 prime-power 位置啟動的 linear ramps。

這跟 AMRAL 先前的 Green / point-source engineering 語言非常接近。

---

# 9. Hurwitz–Lerch 項其實可以展成非常簡單的指數族

由

$$
\Phi(z,2,\tfrac14)
=
\sum_{m=0}^{\infty}
\frac{z^m}{(m+\frac14)^2},
$$

令

$$
a_m
=
2m+\frac12.
$$

注意

$$
a_m
=
2(m+\tfrac14).
$$

因此：

$$
\frac14
e^{-t/2}
\Phi(e^{-2t},2,\tfrac14)
=
\sum_{m=0}^{\infty}
\frac{e^{-a_mt}}{a_m^2}.
$$

所以：

$$
\boxed{
\mathcal A(t)
=
4(e^{t/2}+e^{-t/2}-2)
+
ct
+
\frac C4
-
\sum_{m=0}^{\infty}
\frac{e^{-a_mt}}{a_m^2},
}
$$

其中

$$
c
=
\frac12
\left[
\frac{\Gamma'}{\Gamma}
\left(\frac14\right)
-\log\pi
\right].
$$

這個表示對 interval arithmetic 特別友善。

對

$$
t\ge\log2,
$$

級數相鄰項的 exponential ratio 至多

$$
e^{-2t}\le\frac14,
$$

所以 truncation tail 很容易嚴格包絡。

---

# 10. 關鍵新結構：每個 prime-power interval 都是嚴格凸的

微分：

$$
\mathcal A'(t)
=
2(e^{t/2}-e^{-t/2})
+
c
+
\sum_{m=0}^{\infty}
\frac{e^{-a_mt}}{a_m}.
$$

再微分：

$$
\mathcal A''(t)
=
e^{t/2}
+
e^{-t/2}
-
\sum_{m=0}^{\infty}e^{-a_mt}.
$$

而

$$
\sum_{m=0}^{\infty}e^{-a_mt}
=
\frac{e^{-t/2}}{1-e^{-2t}}.
$$

因此：

$$
\boxed{
\mathcal A''(t)
=
e^{t/2}
+
e^{-t/2}
-
\frac{e^{-t/2}}{1-e^{-2t}}.
}
$$

令

$$
q=e^{-t}.
$$

則其符號等同於：

$$
1+q-\frac{q}{1-q^2}.
$$

乘上正數

$$
1-q^2
$$

後，符號等同於：

$$
1-q^2-q^3.
$$

令 $q_c$ 為

$$
q_c^3+q_c^2=1
$$

在 $(0,1)$ 的唯一根。

數值上：

$$
q_c
\approx
0.7548776662466928,
$$

所以：

$$
t_c
=
-\log q_c
\approx
0.2811995743229619.
$$

因此：

$$
\boxed{
\mathcal A''(t)>0
\quad
\forall t>t_c.
}
$$

又因為

$$
\log2
\approx
0.6931471805599453
>
t_c,
$$

所以：

$$
\boxed{
\mathcal A''(t)>0
\quad
\forall t\ge\log2.
}
$$

這是本節點 prime-side reduction 的核心。

---

# 11. Prime-power intervals

令所有 distinct prime powers 按大小排列：

$$
2=q_1<q_2<q_3<\cdots.
$$

令

$$
\ell_j=\log q_j.
$$

定義 weight：

$$
a(q)
=
\frac{\Lambda(q)}{\sqrt q}.
$$

以及 cumulative sums：

$$
A_j
=
\sum_{q\le q_j}a(q),
$$

$$
B_j
=
\sum_{q\le q_j}a(q)\log q.
$$

在 interval

$$
I_j
=
[\ell_j,\ell_{j+1}],
$$

沒有新的 prime-power ramp 在內部啟動。

因此，對

$$
t\in I_j,
$$

有精確公式：

$$
\boxed{
\Psi(t)
=
\mathcal A(t)
-
A_j t
+
B_j.
}
$$

所以：

$$
\Psi'(t)
=
\mathcal A'(t)-A_j,
$$

以及

$$
\boxed{
\Psi''(t)
=
\mathcal A''(t)>0
}
$$

在 interval interior 成立。

因此每一個 prime-power interval 上：

$$
\boxed{
\Psi
\text{ is strictly convex}.
}
$$

---

# 12. Prime-power 啟動點本身不會產生新的局部最小值

在

$$
t=\log q
$$

處，新 ramp

$$
a(q)(t-\log q)_+
$$

開始。

$\Psi(t)$ 本身保持連續。

但是其 derivative 發生 downward jump：

$$
\boxed{
\Psi'(\log q^+)
=
\Psi'(\log q^-)
-
a(q).
}
$$

其中

$$
a(q)>0.
$$

一個 cusp 若要成為 local minimum，需要：

$$
\Psi'(\log q^-)\le0
$$

且

$$
\Psi'(\log q^+)\ge0.
$$

但因為：

$$
\Psi'(\log q^+)
<
\Psi'(\log q^-),
$$

這種符號排列不可能發生。

所以：

$$
\boxed{
\text{prime-power activation points cannot create a new local minimum.}
}
$$

它們可能產生 local maximum：

$$
\Psi'(\log q^-)>0>
\Psi'(\log q^+),
$$

但不會產生 local minimum。

---

# 13. 每個 interval 只剩一個 scalar minimum candidate

因為

$$
\mathcal A'(t)
$$

在

$$
t\ge\log2
$$

嚴格遞增，所以方程

$$
\mathcal A'(t)=A_j
$$

在每個 $I_j$ 內最多有一個解。

定義：

$$
t_j^\ast
=
\operatorname{argmin}_{t\in I_j}
\left[
\mathcal A(t)-A_jt+B_j
\right].
$$

它可以完全由以下三種情況決定：

### Case L

若

$$
\mathcal A'(\ell_j)\ge A_j,
$$

則

$$
t_j^\ast=\ell_j.
$$

### Case R

若

$$
\mathcal A'(\ell_{j+1})\le A_j,
$$

則

$$
t_j^\ast=\ell_{j+1}.
$$

### Case I

否則存在唯一 interior root：

$$
\mathcal A'(t_j^\ast)=A_j.
$$

因為 $\mathcal A'$ 單調，這個 root 可用：

- bisection；
- interval Newton；
- rational enclosure；

嚴格隔離。

定義 prime-power minimum sequence：

$$
\boxed{
M_j
:=
\Psi(t_j^\ast)
=
\mathcal A(t_j^\ast)
-
A_j t_j^\ast
+
B_j.
}
$$

---

# 14. Prime-Power Convex-Minimum Criterion

現在使用 Suzuki 的兩個既有結果：

1. 存在

$$
t_0>\log2
$$

使

$$
\Psi(t)>0
$$

對

$$
0<t<t_0
$$

無條件成立；

2.

$$
RH
\Longleftrightarrow
\Psi(t)\ge0
\quad
\forall t\in\mathbb R.
$$

而

$$
[\log2,\infty)
=
\bigcup_{j=1}^{\infty}I_j.
$$

每個 $I_j$ 上的全域最小值正是 $M_j$。

所以得到：

## Theorem 14.1 · Prime-Power Convex-Minimum Reduction

$$
\boxed{
RH
\Longleftrightarrow
M_j\ge0
\quad
\forall j\ge1.
}
$$

其中每個 $M_j$ 只需要：

- 枚舉到 $q_j$ 為止的 prime powers；
- 計算 $A_j,B_j$；
- 解一個單調 scalar equation；
- 評估一個 scalar minimum。

這把：

$$
\Psi(t)\ge0
\quad
\forall t\in[\log2,\infty)
$$

壓成：

$$
M_1,M_2,M_3,\ldots
$$

的一維離散 positivity sequence。

這仍然有：

$$
\forall j\in\mathbb N
$$

的 global quantifier。

所以它是 reduction，不是 RH proof。

---

# 15. Convex-dual / Legendre form

對 interval $I_j$ 定義 restricted convex conjugate：

$$
\mathcal A_{I_j}^\ast(y)
:=
\sup_{t\in I_j}
\left[
yt-\mathcal A(t)
\right].
$$

則：

$$
M_j
=
B_j
-
\mathcal A_{I_j}^\ast(A_j).
$$

因此 Theorem 14.1 亦可寫成：

$$
\boxed{
RH
\Longleftrightarrow
B_j
\ge
\mathcal A_{I_j}^\ast(A_j)
\quad
\forall j\ge1.
}
$$

這個形式非常接近 AMRAL 原本的：

- arithmetic separation；
- positive cone；
- convex budget；
- dual certificate；

語言。

每個 prime-power interval 只產生一個 convex-dual inequality。

---

# 16. 這與 Li criterion 是兩種不同的 countable compression

Li：

$$
RH
\Longleftrightarrow
\lambda_n\ge0
\quad
\forall n\ge1.
$$

本節點的 prime-power convex reduction：

$$
RH
\Longleftrightarrow
M_j\ge0
\quad
\forall j\ge1.
$$

兩者的索引語義不同：

$$
n
=
\text{analytic / Möbius-transform order},
$$

而

$$
j
=
\text{prime-power activation interval}.
$$

所以可以把它們視為兩個不同的離散化：

$$
\text{zero-side spectral amplification}
\longrightarrow
\{\lambda_n\},
$$

以及

$$
\text{prime-side piecewise-convex arithmetic flow}
\longrightarrow
\{M_j\}.
$$

對 AMRAL 而言，第二種更適合既有 interval-certificate infrastructure。

---

# 17. 與 Suzuki Hankel / moment criterion 的第三條接口

Suzuki 另外定義 moments：

$$
\mu_n
=
\int_0^\infty
\frac14
e^{-t/2}
\Psi(t)t^n\,dt.
$$

建立兩族 Hankel matrices：

$$
\Delta_n
=
(\mu_{i+j})_{0\le i,j\le n},
$$

以及

$$
\Delta_n^{(1)}
=
(\mu_{i+j+1})_{0\le i,j\le n}.
$$

其 theorem 給：

$$
RH
\Longleftrightarrow
\det\Delta_n\ge0
\ \text{and}\
\det\Delta_n^{(1)}\ge0
\quad
\forall n\ge1.
$$

因此現在得到三個可互相 cross-check 的接口：

$$
\boxed{
\{M_j\}
\leftrightarrow
\Psi(t)
\leftrightarrow
\{\mu_n\}
\leftrightarrow
\{\Delta_n,\Delta_n^{(1)}\}
\leftrightarrow
\{\lambda_n\}.
}
$$

Suzuki 還給出 $\mu_n$ 與 Li coefficients $\lambda_n$ 的顯式有限線性轉換。

這對 AMRAL 的 arithmetic-matrix 路線很重要。

但必須加一條強警告：

```text
AMRAL existing M_arith(R)
IS NOT AUTOMATICALLY
Suzuki's Hankel Delta_n.
```

除非日後嚴格證明兩者間的 congruence / compression / limit relation，不得把兩個 PSD family 混成同一個 theorem。

---

# 18. 為何 prime-power convex criterion 很適合 interval certificate

每個 $M_j$ 的 certificate 只需有限資料。

## 18.1 Exact combinatorial data

prime powers：

$$
q\le q_{j+1}
$$

可以用 exact integer arithmetic 枚舉。

## 18.2 Elementary weights

$$
a(q)
=
\frac{\log p}{p^{k/2}}
$$

可以用 directed interval arithmetic 嚴格包絡。

## 18.3 Smooth backbone tail

在

$$
t\ge\log2
$$

時：

$$
\sum_{m=0}^{\infty}
\frac{e^{-a_mt}}{a_m^2}
$$

的 exponential ratio 至多 $1/4$，所以可給簡單幾何 tail enclosure。

## 18.4 Unique minimizer

因為

$$
\mathcal A''(t)>0,
$$

interval Newton 不會遇到多根 ambiguity。

## 18.5 Certificate target

對每個 $j$，只需證明：

$$
M_j^{\rm lower}>0.
$$

若某個 interval certificate 得到：

$$
M_j^{\rm upper}<0,
$$

則由 Suzuki criterion 直接形成 RH refutation candidate，必須立刻進入 independent adversarial verification。

但：

$$
M_j>0
\quad
\text{for finitely many }j
$$

永遠不能升格為 RH proof。

---

# 19. 一個自然的 certificate schema

下一輪可以把每個 interval certificate 做成：

```text
certificate_id
prime_power_left
prime_power_right
log_interval
A_j_interval
B_j_interval

arch_series_cutoff
arch_series_tail_bound

derivative_left_interval
derivative_right_interval
minimizer_mode = LEFT | RIGHT | INTERIOR

t_star_interval
M_j_interval

rounding_mode
precision_bits
implementation_hash
source_hash
```

成功狀態只有：

```text
FINITE_INTERVAL_POSITIVE
FINITE_INTERVAL_NEGATIVE
INCONCLUSIVE
```

禁止輸出：

```text
RH_PROVED
```

除非未來真的另外關閉 all-$j$ universal step。

---

# 20. Global quantifier 現在被拆成三層

原本問題看起來像：

$$
\forall\rho
\quad
\Re\rho=\frac12.
$$

現在至少有三個不同 compression interface。

## Layer Z · rational zero cells

$$
RH
\Longleftrightarrow
N_\zeta(C)=0
$$

對所有 rational off-axis cells $C$。

這把 continuum coordinate 壓成 countable rational basis。

## Layer L · Li sequence

$$
RH
\Longleftrightarrow
\lambda_n\ge0
\quad
\forall n.
$$

這把 zero geometry 壓成 countable analytic sequence。

## Layer P · prime-power convex minima

$$
RH
\Longleftrightarrow
M_j\ge0
\quad
\forall j.
$$

這把 prime-side continuous positivity 壓成 countable prime-power sequence。

真正沒有消失的是：

$$
\boxed{
\forall j\in\mathbb N
}
$$

或等價的 countable universal quantifier。

所以目前可以說：

```text
CONTINUOUS_GLOBAL_QUANTIFIER = COMPRESSED
COUNTABLE_GLOBAL_QUANTIFIER = STILL_OPEN
```

這個區分很重要。

---

# 21. 本節點 GAP ledger

## CLOSED / CORRECTED

### G1. Global compact negative witness existence

```text
CLOSED_BY_KNOWN_CRITERION
```

不是本輪新 theorem。

來源：Weil / Yoshida / Suzuki 與 AMRAL RH-W-03。

---

### G2. Off-axis cell to finite Li-extremal height

```text
CONDITIONAL_CLOSED
```

若 cell occupied：

$$
N_\zeta(C)\ge1,
$$

則 extremal modulus search 可限制到：

$$
|\gamma|\le T_C.
$$

---

### G3. Fixed-$n$ zero tail reduction

```text
CLOSED_AS_BOUND
```

對

$$
T\ge\max(e,2n)
$$

可用 $N(T)$ 顯式 bound 得到 high-zero tail enclosure。

---

### G4. Prime-side interval convexity

```text
CLOSED
```

對

$$
t\ge\log2,
$$

$$
\mathcal A''(t)>0.
$$

---

### G5. Continuous $\Psi$ positivity to prime-power minima

```text
CLOSED_AS_REDUCTION
```

利用 Suzuki criterion：

$$
RH
\Longleftrightarrow
M_j\ge0
\quad
\forall j.
$$

---

## OPEN

### G6. Universal prime-power minimum positivity

```text
OPEN
```

尚未證明：

$$
M_j\ge0
\quad
\forall j.
$$

這一項若完整關閉，即關閉 RH。

---

### G7. Asymptotic / inductive control of $M_j$

```text
OPEN
```

需要尋找不是逐項 brute-force 的結構，例如：

- recurrence；
- convex dual monotonicity；
- prime-power jump compensation；
- block positivity；
- moment/Hankel domination；
- renormalized asymptotic invariant。

---

### G8. Constructive off-axis cell to compact negative witness

```text
OPEN_ENGINEERING
```

存在性已知，但 explicit certified witness generator 尚未建成。

---

### G9. Relation between AMRAL arithmetic matrix and Suzuki Hankel matrices

```text
OPEN
```

不得假設兩者相同。

可以研究：

$$
M_{\rm arith}(R)
\stackrel{?}{\longleftrightarrow}
\Delta_n
$$

是否存在：

- congruence；
- Galerkin projection；
- moment map；
- Schur complement；
- scaling limit。

---

# 22. 下一個主研究節點

建議：

`RH-PrimePowerConvex-Certificate-v1.3`

第一階段不要再新增理論層。

直接實作並驗證：

1. exact prime-power enumerator；
2. directed interval evaluation of $A_j,B_j$；
3. interval-certified $\mathcal A,\mathcal A',\mathcal A''$；
4. geometric tail bound for the archimedean exponential series；
5. monotone interval-Newton minimizer；
6. per-interval certificate；
7. finite batch scan；
8. independent implementation cross-check。

同時建第二個 validator：

`RH-Suzuki-Hankel-CrossCheck-v0.1`

用 Suzuki 的：

$$
\mu_n
\leftrightarrow
\lambda_n
$$

轉換，建立 canonical Hankel matrices。

目的不是「兩個都算正就宣稱 RH」，而是：

$$
\boxed{
\text{local prime-power certificate}
\quad\text{vs.}\quad
\text{global moment certificate}
}
$$

做雙重 consistency testing。

---

# 23. 目前最值得攻的真正數學問題

v1.2 之後，問題已經不是：

> 如何覆蓋所有 hypothetical zero positions？

而可以改成：

> 能否找到一個對 prime-power indexed convex minima $M_j$ 的結構性控制，使 all-$j$ positivity 不必靠逐項驗證？

更精確：

$$
\boxed{
\text{Find a global invariant or recurrence forcing }
M_j\ge0
\text{ for all }j.
}
$$

或稍弱：

$$
\boxed{
M_j\ge0
\text{ for all sufficiently large }j
}
$$

再配合有限 prefix certificate。

若能得到：

$$
\exists J_0:
M_j\ge0
\quad
\forall j\ge J_0,
$$

且有限驗證：

$$
M_j\ge0
\quad
1\le j<J_0,
$$

才會真正把 countable universal quantifier 收束成有限 proof object。

這是下一個真正的 closure target。

---

# 24. Trust boundary

必須保留：

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE

GLOBAL_COMPACT_NEGATIVE_WITNESS_EXISTENCE = CLOSED_BY_KNOWN_CRITERION

OFFAXIS_CELL_TO_FINITE_EXTREMAL_HEIGHT = TRUE
PRIME_SIDE_INTERVAL_CONVEXITY = TRUE
PRIMEPOWER_MINIMUM_REDUCTION = TRUE

ALL_PRIMEPOWER_MINIMA_POSITIVE = FALSE
GLOBAL_RH_CERTIFICATE = FALSE
```

禁止：

$$
\text{finite number of positive }M_j
\Longrightarrow
RH.
$$

禁止：

$$
\text{finite Hankel PSD}
\Longrightarrow
RH.
$$

禁止：

$$
\text{AMRAL arithmetic matrix numerically PSD}
\Longrightarrow
\text{Suzuki Hankel PSD}.
$$

---

# 25. 一句話狀態

> v1.2 把上一輪模糊的 global-isolation GAP 拆開：compact global negative witness 的存在性其實已由既有 Weil/Suzuki 判準關閉，constructive witness 才仍開放；zero side 上，一個 occupied off-axis rational cell 已足以顯式給出有限 Li-extremal 搜尋高度；prime side 上，Suzuki 的 RH-equivalent arithmetic function $\Psi(t)$ 在每兩個相鄰 prime powers 之間可嚴格化成「strictly convex smooth backbone − linear prime ramp」，因此整個 continuous positivity problem 可壓成一個 prime-power indexed scalar minimum sequence $M_j$。真正剩餘的核心不再是連續位置覆蓋，而是如何消滅最後的 countable universal quantifier $M_j\ge0$ for all $j$。

---

# 26. References

1. AMRAL, **RH-W-03 · 緊支撐分離與雙核心架構**.  
   https://amral.evemisslab.com/riemann/autonomous/p/w03-v0.1/

2. AMRAL, **算術矩陣與半正定證書原型 · v0.1**.  
   https://amral.evemisslab.com/riemann/autonomous/p/proto-arithmetic-matrix-psd-v0.1/

3. AMRAL, **等變算術障礙整合總論 · v1.0**.  
   https://amral.evemisslab.com/riemann/semi-autonomous/p/proto-equivariant-arithmetic-obstruction-integration-v1.0/

4. Enrico Bombieri and Jeffrey C. Lagarias, **Complements to Li's Criterion for the Riemann Hypothesis**, *Journal of Number Theory* 77 (1999), 274–287.  
   DOI: https://doi.org/10.1006/jnth.1999.2392  
   Author-hosted PDF: https://websites.umich.edu/~lagarias/doc/bombieri.pdf

5. Masatoshi Suzuki, **Aspects of the screw function corresponding to the Riemann zeta-function**, *Journal of the London Mathematical Society* 108 (2023), 1448–1487.  
   DOI: https://doi.org/10.1112/jlms.12785  
   arXiv: https://arxiv.org/abs/2206.03682

6. Masatoshi Suzuki, **On the Hilbert space derived from the Weil distribution**, *Canadian Journal of Mathematics*, online 2025.  
   DOI: https://doi.org/10.4153/S0008414X25101739  
   arXiv: https://arxiv.org/abs/2301.00421

7. Masatoshi Suzuki, **Weil's quadratic form via the screw function**, arXiv:2606.09096, 2026.  
   https://arxiv.org/abs/2606.09096

8. Elchin Hasanalizade, Quanli Shen, and Peng-Jie Wong, **Counting zeros of the Riemann zeta function**, *Journal of Number Theory* 235 (2022), 219–241.  
   DOI: https://doi.org/10.1016/j.jnt.2021.06.032  
   arXiv: https://arxiv.org/abs/2107.06506

9. Dave Platt and Tim Trudgian, **The Riemann hypothesis is true up to $3\cdot10^{12}$**, *Bulletin of the London Mathematical Society* 53 (2021), 792–797.  
   DOI: https://doi.org/10.1112/blms.12460  
   arXiv: https://arxiv.org/abs/2004.09765

---

# 27. Provenance

研究主導：Neo.K

v1.2 數學續推、外部文獻對齊與 canonical source 整理：ChatGPT / GPT-5.6 Sol

日期：2026-09-02

研究定位：AMRAL 黎曼猜想半自主研究線，第三弧線 global-quantifier compression 節點。

本文件是 research source artifact，不是 peer-reviewed publication。

所有 claim 必須依 GAP ledger 與 Trust boundary 解讀。
