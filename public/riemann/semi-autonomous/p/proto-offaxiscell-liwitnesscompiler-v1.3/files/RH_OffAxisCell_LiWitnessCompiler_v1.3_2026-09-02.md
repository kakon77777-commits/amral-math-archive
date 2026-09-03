工程紀錄 · 第三弧線 v1.3 · 2026-09-02 · CONDITIONAL_EFFECTIVE_WITNESS_COMPILER · RH_CLAIM_FALSE

# 偏軸 Cell 到有限 Li 負證人的條件式有效編譯器

**RH-OffAxisCell-LiWitnessCompiler v1.3**

本節點承接：

- `RH-ConditionalOffAxisCell-ZetaTransfer-v1.1`
- `RH-GlobalQuantifier-PrimePowerConvexCompression-v1.2`

v1.1 把 hypothetical off-axis zero 的最弱存在性接口壓成 rational off-axis cell，並辨識出水平偏移

$$
\delta=\Re\rho-\frac12
$$

必須保留。

v1.2 則把 Li extremal search 壓到由 cell 顯式決定的有限高度，並探索 Suzuki $\Psi$ 的 prime-power convex compression。

本節點首先校正 v1.2 與 2026 年 8 月最新外部工作的重疊；接著不再沿 prime-power checkpoint tail 重複推導，而回到 Li / Bombieri–Lagarias 路線，建立一個新的 AMRAL 工程接口：

$$
\boxed{
\text{certified off-axis cell}
\Longrightarrow
\text{finite extremal package}
\Longrightarrow
\text{finite negative Li witness}.
}
$$

這是一個**條件式有效化結果**。

它不提供 off-axis zero，也不證明 RH；它說明：一旦 off-axis occupancy 被嚴格證實，則可以把該反例資料編譯成一個有限、可重播、可獨立驗證的 Li negativity certificate。

**RH_CLAIM = False.**

---

# 0. Claim register

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE

OFFAXIS_CELL_TO_FINITE_EXTREMAL_HEIGHT = TRUE
GLOBAL_LI_EXTREMAL_SET_FINITE = TRUE_CONDITIONAL_ON_OCCUPIED_CELL
GLOBAL_SECOND_MODULUS_GAP = EFFECTIVELY_ISOLATABLE
NEGATIVE_LI_INDEX_EXISTENCE = CLOSED_BY_BOMBIERI_LAGARIAS
OFFAXIS_CELL_TO_FINITE_LI_WITNESS = CONDITIONAL_EFFECTIVE

ACTUAL_OFFAXIS_CELL = NOT_KNOWN
ACTUAL_NEGATIVE_LI_COEFFICIENT = NOT_KNOWN
GLOBAL_RH_CERTIFICATE = FALSE
```

---

# 1. 外部基線校正：v1.2 的 prime-power convexity 不是可主張的新發現

在 v1.2 完成後進行 2026-09-02 外部搜尋，發現 Rainer Andreas Mittermeier 於 2026 年 8 月已公開一套以 Suzuki screw function 為核心的 `Prime-Power Checkpoint` 系列。

其中至少包括：

1. **Part 1**：prime-power interval convexity、plastic constant transition、restricted Legendre–Mangoldt representation，並嚴格驗證到

$$
q\le10^8.
$$

2. **Part 2**：directed MPFR certificate 擴展到

$$
q\le10^{10},
$$

並建立 Chebyshev-memory barrier。

3. **Part 3**：把剩餘 tail 寫成 active-event reserve

$$
\mathcal V_q
=
\mathcal C_q-\mathcal J_q,
$$

真正剩餘的是 all-event inequality

$$
\mathcal J_q\le\mathcal C_q.
$$

4. **Part 4**：以 workload

$$
Y=-\Psi'
$$

與 service clock

$$
\tau=\mathcal A'(t)
$$

把 recovered episode 壓成 recovery witness。

5. **Part 5**：排除 terminal active episode，並把剩餘 RH tail 更精確地收斂到 recovery-witness inequality；RH 仍 OPEN。

因此，AMRAL v1.2 的 prime-power convex minimum reduction 應視為：

```text
INDEPENDENT_REDERIVATION / EXTERNAL_ALIGNMENT
```

而不能在未做完整 priority / novelty study 前標成原創 theorem。

本節點因此主動避開重做該系列的 current frontier。

外部基線：

- https://zenodo.org/records/21859280
- https://zenodo.org/records/22076060
- https://zenodo.org/records/21979513
- https://zenodo.org/records/22076079
- https://zenodo.org/records/22076088

---

# 2. 回到 Li transform

對非平凡零點

$$
\rho=\beta+i\gamma
$$

定義

$$
u_\rho
:=
\left(
1-\frac1\rho
\right)^{-1}
=
\frac{\rho}{\rho-1}.
$$

直接計算：

$$
|u_\rho|^2
=
\frac{\beta^2+\gamma^2}
{(\beta-1)^2+\gamma^2}
=
1+
\frac{2\beta-1}
{(1-\beta)^2+\gamma^2}.
$$

因此：

$$
\beta>\frac12
\Longrightarrow
|u_\rho|>1,
$$

$$
\beta=\frac12
\Longrightarrow
|u_\rho|=1,
$$

$$
\beta<\frac12
\Longrightarrow
|u_\rho|<1.
$$

Bombieri–Lagarias 的 Li criterion proof 正是使用這個 transformed modulus。

---

# 3. 從 rational off-axis cell 得到嚴格 modulus lower bound

令 v1.1 的右半側 rational cell 為

$$
C
=
[\delta_-,\delta_+]
\times
[\gamma_-,\gamma_+],
$$

其中

$$
0<\delta_-<\delta_+<\frac12,
$$

且 cell 中 zero 的座標寫成

$$
\rho
=
\frac12+\delta+i\gamma.
$$

因此

$$
\beta=\frac12+\delta.
$$

代入：

$$
|u_\rho|^2
=
1+
\frac{2\delta}
{(\frac12-\delta)^2+\gamma^2}.
$$

對整個 cell 可取嚴格 lower enclosure：

$$
\boxed{
r_C^2
=
1+
\frac{2\delta_-}
{(\frac12-\delta_-)^2+\gamma_+^2}.
}
$$

若 cell 真正 occupied，則：

$$
\boxed{
|u_\rho|\ge r_C>1.
}
$$

若 cell 端點是對實際 zero 的嚴格 rational enclosure，則可把端點進一步細化，使實際 target modulus 嚴格大於 $r_C$。

---

# 4. 有限高度 extremal reduction

對任何右半側非平凡零點：

$$
\frac12<\beta<1.
$$

因為

$$
0<2\beta-1<1
$$

且

$$
(1-\beta)^2+\gamma^2\ge\gamma^2,
$$

所以：

$$
|u_\rho|^2
<
1+\frac1{\gamma^2}.
$$

若

$$
\beta\le\frac12,
$$

則

$$
|u_\rho|\le1<r_C.
$$

定義：

$$
\boxed{
T_C
=
\frac1{\sqrt{r_C^2-1}}
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

則對任何

$$
|\gamma|>T_C
$$

的 zero：

- 若 $\beta>1/2$，則

$$
|u_\rho|<r_C;
$$

- 若 $\beta\le1/2$，則

$$
|u_\rho|\le1<r_C.
$$

因此，只要 cell occupied，global transformed modulus maximum

$$
R
:=
\max_\rho |u_\rho|
$$

一定在：

$$
\boxed{
|\Im\rho|\le T_C
}
$$

的有限高度內達到。

這是 v1.2 finite-height reduction 的 Li-oriented formulation。

---

# 5. Finite extremal package

固定一個 occupied cell $C$。

在有限高度：

$$
|\gamma|\le T_C
$$

內，可原則上用標準 rigorous zero isolation：

- argument principle；
- Turing-type zero counting；
- interval arithmetic；
- validated complex root isolation；

取得全部 nontrivial zeros 的 finite spectral package。

定義 extremal set：

$$
E
=
\left\{
\rho:
|u_\rho|=R
\right\}.
$$

因為 bounded height 中零點有限，所以：

$$
K:=|E|<\infty
$$

計 multiplicity。

令：

$$
R_2
=
\sup_{\rho\notin E}|u_\rho|.
$$

由：

1. bounded region 的有限性；
2. $E$ 包含所有 ties；
3. 高度 $>T_C$ 的統一 bound；
4. $R>r_C>1$；

可得：

$$
\boxed{
1\le R_2<R.
}
$$

在實際 certificate 中，不需要知道 $R,R_2$ 的 exact value，只需得到 directed enclosures：

$$
1<R_-,
$$

$$
R_2^+<R_-,
$$

並驗證：

$$
|u_\rho|\ge R_-
$$

對所有 extremal boxes，

以及：

$$
|u_\rho|\le R_2^+
$$

對所有 non-extremal boxes與 high tail。

---

# 6. Extremal phase decomposition

對

$$
\rho_k\in E
$$

寫：

$$
u_{\rho_k}
=
R e^{i\phi_k}.
$$

Bombieri–Lagarias 考察 negative-index form：

$$
L_{-n}
:=
\sum_\rho
\operatorname{Re}
\left[
1-u_\rho^n
\right].
$$

extremal set 的 contribution 為：

$$
K
-
R^n
\sum_{k=1}^{K}
\cos(n\phi_k).
$$

定義：

$$
C_n
:=
\sum_{k=1}^{K}
\cos(n\phi_k).
$$

則：

$$
L_{-n}^{(E)}
=
K-R^n C_n.
$$

Bombieri–Lagarias 使用 simultaneous Diophantine approximation 證明：

$$
C_n
$$

可以對無限多個 $n$ 任意接近 $K$。

因此若 RH 為假，extremal exponential term 最終會在某些 phase-aligned indices 主導其他部分，並使相應 Li quantity 為負。

本節點的工作是把這個 existence argument 改成 finite certificate contract。

---

# 7. Non-extremal finite / mid-range bound

固定一個正整數 $n$。

選：

$$
H_n
\ge
\max(T_C,2n).
$$

對：

$$
|\gamma|\le H_n
$$

且

$$
\rho\notin E,
$$

有：

$$
|u_\rho|\le R_2.
$$

因此：

$$
\left|
\operatorname{Re}
\left[
1-u_\rho^n
\right]
\right|
\le
1+R_2^n.
$$

若：

$$
M(H_n)
$$

表示

$$
|\Im\rho|\le H_n
$$

內的 zero 總數，計 multiplicity，則 finite/mid non-extremal contribution 可用：

$$
\boxed{
B_{\mathrm{mid}}(n)
\le
(M(H_n)-K)
\left(
1+R_2^n
\right).
}
$$

certificate 實作只需：

$$
M(H_n)\le M_n^+
$$

以及：

$$
R_2\le R_2^+.
$$

故：

$$
\boxed{
B_{\mathrm{mid}}(n)
\le
(M_n^+-K)
\left(
1+(R_2^+)^n
\right).
}
$$

---

# 8. High-zero tail 的 explicit real-part bound

對：

$$
|\gamma|>H_n\ge2n,
$$

寫：

$$
u_\rho
=
1+v_\rho,
$$

其中：

$$
v_\rho
=
\frac1{\rho-1}.
$$

因為：

$$
|\rho-1|\ge|\gamma|,
$$

所以：

$$
|v_\rho|
\le
\frac1{|\gamma|}
<
\frac1{2n}.
$$

展開：

$$
(1+v)^n
=
1+nv
+
\sum_{m=2}^{n}
\binom{n}{m}v^m.
$$

第一階：

$$
\left|
\operatorname{Re}v_\rho
\right|
=
\frac{|1-\beta|}
{(1-\beta)^2+\gamma^2}
\le
\frac1{\gamma^2}.
$$

而 higher-order remainder 滿足：

$$
\left|
\sum_{m=2}^{n}
\binom{n}{m}v^m
\right|
\le
e^{n|v|}-1-n|v|.
$$

由：

$$
n|v|\le\frac12
$$

與：

$$
e^x-1-x
\le
\frac{x^2}{2}e^x,
$$

得到：

$$
\left|
\sum_{m=2}^{n}
\binom{n}{m}v^m
\right|
\le
\frac{e^{1/2}}{2}
\frac{n^2}{\gamma^2}.
$$

所以：

$$
\left|
\operatorname{Re}
\left[
1-u_\rho^n
\right]
\right|
\le
\frac{n}{\gamma^2}
+
\frac{e^{1/2}}{2}
\frac{n^2}{\gamma^2}.
$$

對

$$
n\ge1
$$

可統一寫成：

$$
\boxed{
\left|
\operatorname{Re}
\left[
1-u_\rho^n
\right]
\right|
\le
c_0
\frac{n^2}{\gamma^2},
}
$$

其中：

$$
\boxed{
c_0
=
1+\frac{e^{1/2}}2.
}
$$

定義：

$$
Z_2(H)
=
\sum_{|\gamma|>H}
\frac1{\gamma^2}.
$$

則：

$$
\boxed{
B_{\mathrm{tail}}(n)
\le
c_0 n^2 Z_2(H_n).
}
$$

$Z_2(H_n)$ 可由 explicit $N(T)$ upper bound 配合 Stieltjes integration 得到 rigorously directed upper enclosure；v1.2 已建立同類 tail contract。

---

# 9. Finite negativity certificate

假設 finite spectral package 已給出：

$$
R_->R_2^+\ge1.
$$

對選定 $n$，再用 interval phase evaluation 證明：

$$
C_n
=
\sum_{k=1}^{K}
\cos(n\phi_k)
\ge
C_n^-,
$$

其中：

$$
C_n^->0.
$$

extremal contribution 有 upper bound：

$$
L_{-n}^{(E)}
\le
K
-
R_-^n C_n^-.
$$

全部 non-extremal contribution則有：

$$
L_{-n}^{(\mathrm{rest})}
\le
(M_n^+-K)
\left(
1+(R_2^+)^n
\right)
+
c_0n^2Z_{2,n}^+.
$$

因此若：

$$
\boxed{
R_-^n C_n^-
>
K
+
(M_n^+-K)
\left(
1+(R_2^+)^n
\right)
+
c_0n^2Z_{2,n}^+,
}
$$

則：

$$
\boxed{
L_{-n}<0.
}
$$

對 Riemann zeta zero multiset，functional-equation 與 conjugation symmetry 給 Bombieri–Lagarias Corollary 1 的：

$$
\lambda_n=\lambda_{-n}.
$$

所以：

$$
\boxed{
L_{-n}<0
\Longrightarrow
\lambda_n<0.
}
$$

這就是本節點的 finite witness inequality。

---

# 10. Conditional Effective Li-Witness Theorem

## Theorem 10.1

假設存在一個 certified rational off-axis cell $C$，且其 occupancy certificate 證明：

$$
N_\zeta(C)\ge1.
$$

則存在一個有限演算法流程，可產生：

- finite height $T_C$；
- finite rigorous zero-isolation package；
- extremal set $E$；
- certified modulus gap

$$
1\le R_2^+<R_-;
$$

- 某個有限 positive integer $n$；
- extremal phase enclosure；
- finite zero-count bound $M_n^+$；
- high-zero tail bound $Z_{2,n}^+$；

使 finite negativity inequality

$$
R_-^n C_n^-
>
K
+
(M_n^+-K)
\left(
1+(R_2^+)^n
\right)
+
c_0n^2Z_{2,n}^+
$$

成立。

因此輸出：

$$
\boxed{
\lambda_n<0.
}
$$

---

# 11. 為何此 compiler 會終止

termination 有三層。

## 11.1 Global extremal set finite

occupied cell 給：

$$
r_C>1
$$

與：

$$
T_C<\infty.
$$

所以所有 global maximizers 都在 finite height。

---

## 11.2 Strict global second-modulus gap

有限 extremal set 把所有 ties 收進 $E$ 後：

$$
R_2<R.
$$

rigorous zero boxes可任意細化，所以最後可得到：

$$
R_2^+<R_-.
$$

---

## 11.3 Phase alignment

Bombieri–Lagarias 使用 Dirichlet simultaneous Diophantine approximation，使：

$$
C_n
=
\sum_{k=1}^{K}\cos(n\phi_k)
$$

對無限多個 $n$ 任意接近：

$$
K.
$$

因此存在無限多個 phase-aligned indices 使：

$$
C_n^->c
$$

對某固定：

$$
c>0.
$$

在這些 indices 上：

$$
R_-^n
$$

是主 exponential scale。

另一方面：

$$
(R_2^+)^n
$$

具有嚴格較小 exponential base，而：

$$
M_n^+
$$

最多是 polynomial / quasi-linear-log scale；

$$
n^2Z_{2,n}^+
$$

也是 subexponential。

故：

$$
\frac{
(M_n^+-K)(1+(R_2^+)^n)
+
c_0n^2Z_{2,n}^+
}{
R_-^n
}
\to0
$$

沿適當 alignment subsequence。

所以有限 negativity inequality 最終必通過。

這不是給一個漂亮的小 universal upper bound for $n$。

它給的是更適合 AMRAL 的結論：

> **enumerate candidate $n$, refine finite phase boxes, verify the finite inequality；在 off-axis certificate 為真時，該 semidecision process 保證停機並輸出一個有限 negative Li witness。**

---

# 12. 這與直接找到 off-axis zero 有什麼不同？

如果已經 rigorous 地找到 off-axis zero，本身當然已經否證 RH。

因此這個 compiler 的價值不在「比反例更早否證 RH」。

它的價值在 proof engineering：

$$
\text{geometric counterexample}
\longrightarrow
\text{canonical arithmetic witness}.
$$

也就是把：

$$
\rho\notin\Re s=\frac12
$$

轉成：

$$
\lambda_n<0
$$

的有限標量證書。

如此可得到彼此獨立的 evidence channels：

```text
CHANNEL A = complex zero isolation
CHANNEL B = transformed extremal geometry
CHANNEL C = Li coefficient negativity
CHANNEL D = prime-side / explicit-formula recomputation
```

若未來真的出現 counterexample candidate，可以要求四個 channel 互相驗證，降低單一 numerical pipeline 的風險。

---

# 13. 與 v1.1 global witness GAP 的關係

v1.1 留下：

```text
OFFAXIS_CELL_TO_EXPLICIT_WITNESS_MAP = OPEN
```

當時主要討論 Weil compact witness。

v1.3 現在可以拆成：

```text
OFFAXIS_CELL_TO_EXPLICIT_COMPACT_WEIL_WITNESS = OPEN_ENGINEERING

OFFAXIS_CELL_TO_EXPLICIT_LI_WITNESS =
    CONDITIONAL_EFFECTIVE
```

所以不能把 Weil witness map 本身宣稱 CLOSED。

但「global arithmetic witness」已有一條不同出口：

$$
\boxed{
\text{off-axis cell}
\to
\text{negative Li coefficient}.
}
$$

---

# 14. Certificate schema

建議 canonical certificate：

```text
certificate_type = RH_LI_NEGATIVE_WITNESS

source_offaxis_cell:
  delta_lower
  delta_upper
  gamma_lower
  gamma_upper
  occupancy_proof_reference

finite_height:
  r_cell_lower
  T_cell_upper

spectral_isolation:
  zero_isolation_method
  zero_count_below_T
  extremal_boxes
  K
  R_lower
  R2_upper

li_index:
  n
  phase_boxes
  cosine_sum_lower

mid_bound:
  H_n
  zero_count_upper

tail_bound:
  Z2_upper
  c0

negativity_margin:
  lhs_lower
  rhs_upper
  margin_lower

result:
  lambda_n_upper
  verdict = NEGATIVE
```

核心 machine-checkable condition：

$$
\texttt{margin\_lower}>0.
$$

---

# 15. Reference checker 的邊界

本節點附一個 Python reference checker：

`li_witness_certificate_checker.py`

它只驗證最後的 scalar sufficient inequality。

它**不**：

- 找 zeta zeros；
- 證明 cell occupied；
- 自動建立 Turing certificate；
- 自動證明 $R_2^+<R_-$；
- 自動計算 rigorous phase intervals；
- 宣稱 RH false。

因此：

```text
REFERENCE_CHECKER = FINAL_INEQUALITY_ONLY
```

真正 production verifier 應使用：

- MPFR / Arb；
- outward rounding；
- signed certificate manifest；
- independent implementation；
- formalized scalar theorem。

---

# 16. Formalization target

本節點很適合先形式化有限核心。

Lean / Coq 可先證：

### F1

若：

$$
R_->R_2^+\ge1,
$$

$$
C_n^->0,
$$

且 finite negativity inequality 成立，則：

$$
L_{-n}<0.
$$

### F2

zeta symmetry assumptions下：

$$
L_{-n}=\lambda_n.
$$

### F3

high-tail elementary inequality：

$$
\left|
\operatorname{Re}
\left[
1-
\left(
1+\frac1{\rho-1}
\right)^n
\right]
\right|
\le
c_0
\frac{n^2}{\gamma^2}
$$

在：

$$
|\gamma|\ge2n
$$

及：

$$
0<\Re\rho<1
$$

下成立。

較重的 analytical dependencies：

- zero counting；
- finite zero isolation；
- simultaneous Diophantine approximation；

可先作 theorem dependency，不必第一版全部 formalize。

---

# 17. GAP ledger

## CLOSED / CONDITIONAL-CLOSED

### G1. Occupied cell to finite extremal height

```text
CONDITIONAL_CLOSED
```

$$
N_\zeta(C)\ge1
\Longrightarrow
T_C<\infty.
$$

---

### G2. Finite extremal set

```text
CONDITIONAL_CLOSED
```

global transformed modulus maximizers 被限制在 finite height。

---

### G3. Strict second-modulus gap

```text
EFFECTIVELY_ISOLATABLE
```

有限 spectral package 完整隔離後：

$$
R_2<R.
$$

---

### G4. Phase-aligned negative Li existence

```text
REFERENCE_CLOSED
```

Bombieri–Lagarias 已證，若 critical-line condition fail，Li quantities 出現負值；extremal proof 使用 simultaneous Diophantine approximation。

---

### G5. Finite witness compiler

```text
CONDITIONAL_EFFECTIVE
```

本節點把 existence proof 改寫成可驗證的 finite-certificate pipeline。

---

## OPEN

### G6. Actual off-axis occupancy

```text
OPEN
```

目前沒有已知：

$$
N_\zeta(C)\ge1.
$$

---

### G7. Production rigorous zero-isolation adapter

```text
OPEN_ENGINEERING
```

需要把 Turing / interval zero verification 接到本 certificate schema。

---

### G8. Formal proof of scalar certificate theorem

```text
OPEN_FORMALIZATION
```

適合作為下一個 Lean / Coq 小節點。

---

### G9. RH

```text
OPEN
```

本節點不縮短：

$$
\forall\rho:\Re\rho=\frac12
$$

的 proof obligation 本身。

它改善的是：

$$
\neg RH
\Longrightarrow
\text{finite auditable witness}
$$

的工程結構。

---

# 18. 下一節點建議

若繼續此支線：

`RH-LiWitness-FormalCertificate-v1.4`

工作：

1. 把 Section 8 high-tail bound 做 exact theorem；
2. 用 explicit $N(T)$ bound 產生 $Z_2(H)$ closed formula；
3. 建 synthetic spectral package tests；
4. 寫 Lean 4 finite inequality theorem；
5. 寫 independent Python / Rust checker；
6. 建 certificate JSON schema；
7. adversarially test interval-overlap / multiplicity / phase-wrap corner cases。

若回到真正 RH closure：

`RH-GlobalTail-Bridge-v2.0`

則應在兩條 current frontiers之間選：

- Suzuki/Mittermeier recovery-witness inequality

$$
\mathcal J_q\le\mathcal C_q;
$$

或

- AMRAL 原本 arithmetic PSD / Green bridge。

不建議再把主要時間投入已被外部 Part 1–5 完整開發的基本 prime-power convexity。

---

# 19. Trust boundary

必須保留：

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE

ACTUAL_OFFAXIS_ZERO = NOT_KNOWN
ACTUAL_NEGATIVE_LI_COEFFICIENT = NOT_KNOWN

OFFAXIS_TO_LI_WITNESS_COMPILER = CONDITIONAL_EFFECTIVE
GLOBAL_RH_CERTIFICATE = FALSE
```

禁止：

$$
\text{compiler exists}
\Longrightarrow
\text{counterexample exists}.
$$

禁止：

$$
\text{finite spectral architecture}
\Longrightarrow
\neg RH.
$$

本節點只建立：

$$
\boxed{
\text{IF an off-axis zero is rigorously certified, THEN a finite negative Li witness can be effectively compiled and independently checked.}
}
$$

---

# 20. 一句話狀態

> v1.3 校正了 v1.2 與 2026 年 8 月 Mittermeier prime-power checkpoint 系列的外部重疊，停止在該已高度開發路線上重複推導；轉而利用 v1.2 的 finite-height Li extremal reduction 與 Bombieri–Lagarias 的 extremal-gap / simultaneous-Diophantine argument，把 hypothetical certified off-axis cell 有效編譯成有限 negative Li coefficient certificate。此結果不證 RH，但把「偏軸幾何反例」到「全域算術負證人」的其中一條接口從 existence 升級為 conditional effective finite proof object。

---

# 21. References

1. Enrico Bombieri and Jeffrey C. Lagarias, **Complements to Li's Criterion for the Riemann Hypothesis**, *Journal of Number Theory* 77 (1999), 274–287.  
   DOI: https://doi.org/10.1006/jnth.1999.2392  
   PDF: https://websites.umich.edu/~lagarias/doc/bombieri.pdf

2. Xian-Jin Li, **The Positivity of a Sequence of Numbers and the Riemann Hypothesis**, *Journal of Number Theory* 65 (1997), 325–333.  
   DOI: https://doi.org/10.1006/jnth.1997.2137

3. Masatoshi Suzuki, **Aspects of the screw function corresponding to the Riemann zeta-function**, *Journal of the London Mathematical Society* 108 (2023), 1448–1487.  
   DOI: https://doi.org/10.1112/jlms.12785  
   arXiv: https://arxiv.org/abs/2206.03682

4. Rainer Andreas Mittermeier, **Prime-power checkpoints for the Riemann zeta screw function: Plastic-Constant Convexity and a Restricted Legendre--Mangoldt Representation**, 2026.  
   https://zenodo.org/records/21859280

5. Rainer Andreas Mittermeier, **Prime-Power Checkpoints for Suzuki's Riemann Zeta Screw Function: Rigorous Positivity Certificate through q = 10^10 and an Explicit Chebyshev-Memory Barrier -- Part 2**, 2026.  
   https://zenodo.org/records/22076060

6. Rainer Andreas Mittermeier, **The Remaining Riemann-Hypothesis Tail: From Prime-Power Checkpoints to Smoothed von Mangoldt Bounds**, 2026.  
   https://zenodo.org/records/21979513

7. Rainer Andreas Mittermeier, **Recovery Witnesses in the Prime-Power Checkpoint Program: Service-Clock Geometry and an Exact Quantifier Reduction for the Riemann-Hypothesis Tail -- Part 4**, 2026.  
   https://zenodo.org/records/22076079

8. Rainer Andreas Mittermeier, **Deep Episodes in the Prime-Power Checkpoint Program: An Unconditional Terminal-Episode Theorem, an Exact Chebyshev Bridge, and Sharp Recovery Recurrence -- Part 5**, 2026.  
   https://zenodo.org/records/22076088

9. Elchin Hasanalizade, Quanli Shen, and Peng-Jie Wong, **Counting zeros of the Riemann zeta function**, *Journal of Number Theory* 235 (2022), 219–241.  
   DOI: https://doi.org/10.1016/j.jnt.2021.06.032  
   arXiv: https://arxiv.org/abs/2107.06506

---

# 22. Provenance

研究主導：Neo.K

v1.3 數學續推、外部 frontier 校正與 canonical source 整理：ChatGPT / GPT-5.6 Sol

日期：2026-09-02

研究定位：AMRAL 黎曼猜想半自主研究線，第三弧線 conditional effective witness 節點。

本文件是 research source artifact，不是 peer-reviewed publication。

所有 claim 必須依 Claim register、GAP ledger 與 Trust boundary 解讀。
