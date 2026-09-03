工程紀錄 · 第三弧線起點 v1.1 · 2026-09-02 · CONDITIONAL_TRANSFER_CLOSED · GLOBAL_WEIL_ISOLATION_OPEN

# 條件式偏軸 Cell 轉移、Weil 局部負慣性與 Li 全域壓縮

**RH-ConditionalOffAxisCell-ZetaTransfer v1.1**

本節點承接 AMRAL 黎曼猜想半自主研究第二弧線 v1.0。v1.0 已把抽象 Green 模型中的 $58$ 維局部位置盒證書，從 v0.9 的統一半徑 $2\times10^{-15}$ 嚴格提升到 $1.78\times10^{-6}$，並明確停止「繼續放大 local radius」作為主要研究方向。本節點不重新做局部覆蓋，而處理交接文件指定的下一個接口：

$$
\text{hypothetical off-axis zeta zero}
\Longrightarrow
\text{legal occupancy cell}.
$$

本輪得到的核心結果是：**偏軸零點到有理 cell 的存在性 transfer 可以閉合；但原有只記錄 ordinate 的 occupancy representation 對實際 zeta 偏軸語義不足，必須顯式加入水平偏移自由度。** 在修正後的表示中，一個偏軸水平對稱 pair 對 Weil 零點側二次型天然誘導一個不定的 $2\times2$ block；使用兩個 multiplicative translates 即可在局部子空間中嚴格產生負慣性。然而這個局部負方向尚不能直接推出完整 Weil quadratic form 為負，真正未閉合的 GAP 已被壓縮為 **global isolation / dominance**。

**RH_CLAIM = False.** 本節點不宣稱證明或否證黎曼猜想。

---

## 連接 · Connections

上一節點：

- AMRAL v0.9：佔用算子族與覆蓋式 Green 證書  
  https://amral.evemisslab.com/riemann/semi-autonomous/p/proto-occupancy-operatorfamily-v0.9/
- AMRAL v1.0：局部區間 Green 位置覆蓋  
  https://amral.evemisslab.com/riemann/semi-autonomous/p/proto-localintervalgreen-cellcover-v1.0/
- AMRAL v0.1–v1.0：完整研究報告與 AI 交接  
  https://amral.evemisslab.com/riemann/semi-autonomous/p/proto-v0.1-v1.0-final-report-ai-handoff-v1.0/

v1.0 的正式研究邊界為：

$$
\texttt{actual\_zeta\_occupancy\_family=false},
$$

$$
\texttt{global\_rh\_certificate=false}.
$$

交接文件指定下一節點：

`RH-ConditionalOffAxisCell-ZetaTransfer-v1.1`

並要求下一步不要再以擴大 local radius 為主要目標。

本文件即為該節點的第一份續推稿。

---

## 0. Claim register

本輪狀態：

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE

OFFAXIS_TO_RATIONAL_CELL = TRUE
ORDINATE_ONLY_TRANSFER_REPRESENTATION_SUFFICIENT = FALSE
QUARTET_SYMMETRY_BLOCK_IDENTIFIED = TRUE
LOCAL_NEGATIVE_INERTIA = TRUE

ACTUAL_ZETA_OCCUPANCY_FAMILY = FALSE
GLOBAL_WEIL_ISOLATION = FALSE
GLOBAL_RH_CERTIFICATE = FALSE
```

其中：

- `OFFAXIS_TO_RATIONAL_CELL = TRUE` 是條件命題：若存在偏軸零點，則可把它放入一個有理的 off-axis cell。
- `LOCAL_NEGATIVE_INERTIA = TRUE` 是局部 Weil 零點 block 的結果，不等於完整 Weil quadratic form 已出現負證人。
- `GLOBAL_WEIL_ISOLATION = FALSE` 是目前真正的主要未閉合點。
- `RH_PROVED = FALSE` 與 `RH_DISPROVED = FALSE` 必須保留。

---

# 1. Representation correction：ordinate-only occupancy 不足

設一個非平凡零點為

$$
\rho=\beta+i\gamma.
$$

相對於臨界線，定義水平偏移

$$
\delta=\beta-\frac12.
$$

RH 的幾何內容是

$$
\delta=0
$$

對所有非平凡零點成立。

因此，只記錄 ordinate

$$
\gamma
$$

不能區分

$$
\rho_0=\frac12+i\gamma
$$

與

$$
\rho_1=\frac12+\delta+i\gamma,
\qquad
\delta\neq0.
$$

兩者具有相同 ordinate，但只有第一個位於臨界線。

所以若 occupancy cell 要承載「實際 zeta 偏軸零點」的語義，最小表示至少必須包含

$$
C=I_\delta\times I_\gamma,
$$

而不能只使用

$$
C=I_\gamma.
$$

這裡的結論不是宣稱任何只使用 ordinate 的數學方法都不可能工作，而是：

> 對目前 v0.9–v1.0 所需的「hypothetical off-axis zeta zero 到合法 occupancy cell」接口而言，ordinate-only representation 缺少直接表示 RH 違反量 $\delta$ 的自由度。

因此，本節點把 occupancy semantic state 從一維位置資料提升為至少二維：

$$
(\delta,\gamma).
$$

若後續還要記錄 multiplicity、局部零點分離、證書半徑或 symmetry orbit，可再擴張成

$$
(\delta,\gamma,m,\text{cell metadata},\ldots),
$$

但 $\delta$ 與 $\gamma$ 是本接口不可丟失的核心座標。

---

# 2. 已知嚴格高度與偏軸 cell 的存在性 transfer

Platt 與 Trudgian 已用 interval arithmetic 嚴格驗證：

$$
0<\gamma\le 3\times10^{12}
\Longrightarrow
\beta=\frac12,
$$

且該高度範圍內所有非平凡零點皆為 simple。

令

$$
H_0=3\times10^{12}.
$$

若 RH 為假，則存在非平凡零點

$$
\rho=\beta+i\gamma
$$

使得

$$
\beta\neq\frac12.
$$

由上述已驗證高度可知，可取

$$
|\gamma|>H_0.
$$

利用共軛對稱，可以選擇

$$
\gamma>H_0.
$$

再利用 functional-equation symmetry

$$
\rho\longmapsto1-\rho,
$$

若必要，可選右半側代表，使

$$
\delta=\beta-\frac12>0.
$$

由非平凡零點位於臨界帶內，

$$
0<\beta<1,
$$

所以

$$
0<\delta<\frac12.
$$

因此偏軸零點可以寫成

$$
\rho_+
=
\frac12+\delta+i\gamma,
$$

其水平對稱點為

$$
\rho_-
=
\frac12-\delta+i\gamma.
$$

連同共軛對稱，形成 quartet

$$
\frac12\pm\delta\pm i\gamma.
$$

---

## 2.1 有理 cell

因為有理數在實數中稠密，所以可選有理端點

$$
0<\delta_-<\delta<\delta_+<\frac12
$$

以及

$$
H_0<\gamma_-<\gamma<\gamma_+.
$$

定義

$$
C=
[\delta_-,\delta_+]
\times
[\gamma_-,\gamma_+].
$$

令 $N_\zeta(C)$ 表示右半側非平凡零點中，座標

$$
(\beta-\tfrac12,\gamma)
$$

落在 $C$ 內的零點數，計 multiplicity。

則有：

### Proposition 2.1 · Conditional off-axis rational-cell transfer

若 RH 為假，則存在有理 compact off-axis cell

$$
C
\subset
\left(0,\frac12\right)\times(H_0,\infty)
$$

使

$$
N_\zeta(C)\ge1.
$$

也就是

$$
\boxed{
\neg RH
\Longrightarrow
\exists C\in\mathcal C_{\mathbb Q}^{\mathrm{off}}
:
N_\zeta(C)\ge1.
}
$$

這一步的存在性 transfer 不需要再擴大 v1.0 的 local Green radius。

若後續需要「cell 中只含指定有限 orbit」之類更強的 isolation 性質，才需要使用 zeta 零點離散性與進一步的局部零點分離證書。

因此，本輪可把原 handoff 中最弱版本的

$$
\text{off-axis zero}
\Longrightarrow
\text{legal rational off-axis cell}
$$

標記為條件式 CLOSED。

---

# 3. Weil 零點側：偏軸 pair 產生不定 block

Weil criterion 的核心之一，是 Riemann Hypothesis 等價於相應 Weil quadratic functional 的正半定性。對適當 test function $g$，令 Mellin transform 為

$$
G(s)=\int_0^\infty g(x)x^{s-1}\,dx.
$$

考慮上半平面的水平對稱 pair

$$
s_+
=
\frac12+\delta+i\gamma,
$$

$$
s_-
=
\frac12-\delta+i\gamma.
$$

在標準 Weil spectral pairing 下，

$$
1-\overline{s_+}=s_-,
$$

$$
1-\overline{s_-}=s_+.
$$

因此，這一水平 pair 對零點側的局部貢獻，在所採 normalization 下可寫成

$$
q_{\delta,\gamma}^{+}(g)
=
2m\,
\operatorname{Re}
\left(
G(s_+)\overline{G(s_-)}
\right),
$$

其中 $m$ 為 multiplicity。

若計入完整 quartet，可能依 normalization 多一個正的整體常數因子；以下 inertia 結論不受這個正因子影響。

令

$$
z=
\begin{pmatrix}
G(s_+)\\
G(s_-)
\end{pmatrix},
$$

以及

$$
J=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix}.
$$

則

$$
q_{\delta,\gamma}^{+}(g)
=
m z^\ast Jz.
$$

而

$$
\operatorname{spec}(J)=\{-1,+1\}.
$$

所以，只要 $s_+$ 與 $s_-$ 真正是兩個不同 evaluation state，也就是

$$
\delta\neq0,
$$

局部 symmetry block 天然是不定的。

---

## 3.1 臨界線退化

若

$$
\delta=0,
$$

則

$$
s_+=s_-=
\frac12+i\gamma,
$$

局部貢獻退化為 modulus square：

$$
q_{0,\gamma}^{+}(g)
=
2m
\left|
G\left(\frac12+i\gamma\right)
\right|^2
\ge0.
$$

所以局部結構呈現非常乾淨的分岔：

$$
\boxed{
\delta=0
\Longrightarrow
\text{positive square}.
}
$$

而

$$
\boxed{
\delta\neq0
\Longrightarrow
\text{two-state indefinite symmetry block}.
}
$$

這個結構與 Bombieri 對 Weil quadratic functional 的有限截斷與負 eigenvalue 分析方向一致，但本節點只使用局部 pair block，不宣稱已重建 Bombieri 的完整全域 eigenvalue theorem。

---

# 4. 兩個 multiplicative translates 足以暴露局部負方向

定義 multiplicative translation

$$
(\tau_a g)(x)
=
a^{-1/2}g(x/a),
\qquad
a>1.
$$

其 Mellin transform 滿足

$$
\widehat{\tau_a g}(s)
=
a^{s-\frac12}G(s).
$$

取兩個 test functions：

$$
g_0=g,
$$

$$
g_1=\tau_a g.
$$

在 $s_+$ 與 $s_-$ 上建立 evaluation matrix：

$$
V=
\begin{pmatrix}
G(s_+) &
a^{\delta+i\gamma}G(s_+)
\\
G(s_-) &
a^{-\delta+i\gamma}G(s_-)
\end{pmatrix}.
$$

直接計算得

$$
\det V
=
G(s_+)G(s_-)
a^{i\gamma}
\left(
a^{-\delta}-a^\delta
\right),
$$

亦即

$$
\det V
=
-2a^{i\gamma}
G(s_+)G(s_-)
\sinh(\delta\log a).
$$

因此只要

$$
a>1,
$$

$$
\delta>0,
$$

以及

$$
G(s_+)G(s_-)\neq0,
$$

就有

$$
\boxed{
\det V\neq0.
}
$$

這表示 $\{g,\tau_ag\}$ 可以在 evaluation level 分辨水平 mirror pair。

---

## 4.1 拉回 coefficient space

把局部 pair block 拉回由

$$
\{g,\tau_ag\}
$$

張成的二維 coefficient space，得到 Hermitian matrix

$$
B
=
mV^\ast JV.
$$

行列式為

$$
\det B
=
m^2
\det(V^\ast)
\det(J)
\det(V).
$$

因為

$$
\det(J)=-1,
$$

所以

$$
\det B
=
-m^2|\det V|^2<0.
$$

Hermitian $2\times2$ matrix 的 determinant 為負，故兩個實 eigenvalues 一正一負。

因此：

### Proposition 4.1 · Local negative inertia from two translates

若

$$
\delta>0,
\qquad
a>1,
\qquad
G(s_+)G(s_-)\neq0,
$$

則在

$$
\operatorname{span}\{g,\tau_ag\}
$$

中，偏軸水平 pair 所誘導的局部 Weil block 滿足

$$
\boxed{
\operatorname{inertia}(B)=(1,1).
}
$$

因此存在 coefficient vector

$$
c\neq0
$$

使局部 pair contribution 為負。

這是一個純代數結論，不依賴浮點近似。

---

# 5. Cell 上非消失 seed function 的建構

上節需要

$$
G(s_+)G(s_-)\neq0.
$$

這不必被當成 lucky assumption。

令

$$
x=e^u.
$$

選

$$
\eta\in C_c^\infty(\mathbb R),
$$

滿足

$$
\eta(u)\ge0,
$$

$$
\eta\not\equiv0,
$$

且

$$
\operatorname{supp}(\eta)\subset[-\varepsilon,\varepsilon].
$$

定義

$$
g(e^u)=e^{-u/2}\eta(u).
$$

則

$$
G(s)
=
\int_{\mathbb R}
\eta(u)e^{(s-\frac12)u}\,du.
$$

對

$$
s=\frac12+\delta+i\gamma,
$$

有

$$
G(s)
=
\int_{\mathbb R}
\eta(u)e^{\delta u}e^{i\gamma u}\,du.
$$

其實部為

$$
\operatorname{Re}G(s)
=
\int_{\mathbb R}
\eta(u)e^{\delta u}\cos(\gamma u)\,du.
$$

對一個 bounded cell

$$
C=
[\delta_-,\delta_+]
\times
[\gamma_-,\gamma_+],
$$

令

$$
\Gamma_C=\gamma_+.
$$

若選

$$
\Gamma_C\varepsilon<\frac{\pi}{4},
$$

則對所有

$$
|u|\le\varepsilon
$$

與

$$
|\gamma|\le\Gamma_C
$$

都有

$$
\cos(\gamma u)>0.
$$

又因為

$$
\eta(u)e^{\delta u}\ge0,
$$

且不恆為零，所以整個 cell 上可得

$$
\operatorname{Re}G(s)>0.
$$

因此

$$
G(s)\neq0
$$

在該 compact cell 上成立。

相同論證亦可作用於 $-\delta$ 的 mirror side。

---

## 5.1 可驗證化

對 AMRAL 工程而言，可把這個 analytic construction 轉成：

1. rational cell input；
2. rational 或可嚴格包絡的 $\varepsilon$；
3. 明確 bump function；
4. interval arithmetic 計算；
5. 證明

$$
\inf_{s\in C}|G(s)|>0.
$$

這與 v0.9–v1.0 已採用的 interval-certificate 路線相容。

因此，局部 nonvanishing 不需要依賴數值猜測。

---

# 6. v1.1 的條件式主命題

把前面結果合在一起，可得到本節點的主要條件式敘述。

### Theorem 6.1 · Conditional Off-Axis Quartet-Cell Transfer

若 RH 為假，則存在：

- 一個有理 compact off-axis cell

$$
C
\subset
\left(0,\frac12\right)\times(H_0,\infty),
$$

- 一個 smooth compactly supported test function $g$，
- 一個 rational parameter

$$
a>1,
$$

使得：

$$
N_\zeta(C)\ge1,
$$

且對 cell 中某一個 off-axis horizontal zero pair，其由

$$
\{g,\tau_ag\}
$$

生成的局部 Weil zero block 滿足

$$
\det B<0.
$$

因此

$$
\operatorname{inertia}(B)=(1,1).
$$

亦即：

$$
\boxed{
\neg RH
\Longrightarrow
\exists
\text{ rational off-axis cell carrying a local negative Weil direction}.
}
$$

此處「local negative Weil direction」只指目標偏軸 symmetry block 在所構造二維 test-function subspace 的 restriction。

**它不等於完整 Weil quadratic form 已為負。**

---

# 7. 真正未閉合的全域問題

完整 Weil quadratic form 不能只保留一個 target quartet。

把它示意拆成

$$
Q(g)
=
q_{\mathrm{target}}(g)
+
Q_{\mathrm{rest}}(g).
$$

本輪建立的是：

$$
\exists g:
q_{\mathrm{target}}(g)<0
$$

在適當局部二維子空間中可以成立。

但這不能直接推出

$$
Q(g)<0,
$$

因為

$$
Q_{\mathrm{rest}}(g)
$$

包含其他全部零點與完整 explicit-formula 結構，其貢獻可能抵消 target block 的局部負值。

因此真正剩餘的 GAP 是：

$$
\boxed{
\text{local quartet negative inertia}
\Longrightarrow
\text{global Weil negative witness}.
}
$$

我們把它記為

$$
G_{\mathrm{global}}.
$$

更具體地，它至少包含以下幾個可能方向：

1. **Isolation**：建構 test function，使 target quartet 的 sampling 遠強於其他零點。
2. **Dominance**：證明 target negative contribution 在某個 canonical family 中最終壓過 rest。
3. **Frame / lower-bound control**：建立可控的 spectral decomposition，使局部負 block 不會在全域投影後消失。
4. **Arithmetic-side certificate**：不直接逐零點隔離，而在 explicit formula 的 prime side 建立等價負證人。
5. **Discrete criterion compression**：改用 Li / Keiper-Li sequence，把連續零點位置量詞轉成離散 index。

所以 v1.1 的真正進展不是 RH closure，而是把之前模糊的「實際 zeta 零點位置量詞」進一步壓縮為一個明確的 global isolation / dominance problem。

---

# 8. Li criterion：把連續全域量詞壓縮成離散序列

令

$$
w_\rho
=
1-\frac1\rho.
$$

若

$$
\rho=\beta+i\gamma,
$$

則

$$
|w_\rho|^2
=
\frac{|\rho-1|^2}{|\rho|^2}.
$$

直接展開：

$$
|w_\rho|^2
=
1+\frac{1-2\beta}{|\rho|^2}.
$$

因此若

$$
\beta<\frac12,
$$

則

$$
\boxed{
|w_\rho|>1.
}
$$

若 RH 為假，由 functional-equation symmetry 必有左半側偏軸零點，所以至少存在某個 transformed zero 滿足上述嚴格不等式。

另一方面，當

$$
|\gamma|\to\infty,
$$

由

$$
0<\beta<1
$$

可得

$$
|w_\rho|\to1.
$$

因此只要存在偏軸零點，就可以考慮一個有限的 extremal set，使

$$
R=
\max_\rho |w_\rho|>1
$$

在該 set 上達到。

對其餘零點可取得 gap

$$
|w_\rho|\le R-\eta
$$

於非 extremal 部分成立，適當理解並配合 Bombieri–Lagarias 對零點 multiset 與收斂性的處理。

再利用 simultaneous Diophantine approximation，可選出無限多個整數 $n$，使 extremal phases 近乎同步。

於是 extremal contribution 以

$$
R^n
$$

尺度增長，而非 extremal 部分受

$$
(R-\eta)^n
$$

控制。

這是 Bombieri–Lagarias 對 Li criterion 反向方向的核心 amplification mechanism 之一。

---

## 8.1 Li coefficients

Li coefficients 可寫成

$$
\lambda_n
=
\sum_\rho
\left[
1-
\left(
1-\frac1\rho
\right)^n
\right],
\qquad
n=1,2,3,\ldots
$$

並以標準的對稱與極限方式理解該零點和。

Li 的 theorem 給出：

$$
\boxed{
RH
\Longleftrightarrow
\lambda_n\ge0
\quad
\forall n\ge1.
}
$$

因此若 RH 為假，Bombieri–Lagarias 的 amplification 證明會迫使相應 Li-type sums 在某些 $n$ 出現負值；在其 theorem 的對稱 multiset 設定下，這種負值可無限多次出現。

因此原本的連續零點位置問題

$$
(\beta,\gamma)
\in
(0,1)\times\mathbb R
$$

可以轉成 canonical discrete family：

$$
n\in\mathbb N.
$$

也就是：

$$
\neg RH
\Longrightarrow
\exists n:
\lambda_n<0.
$$

更強的 Bombieri–Lagarias 分析在適當設定下給出無限多次 negativity。

這個轉換並沒有降低 RH 本身的數學難度，因為證明

$$
\lambda_n\ge0
\quad
\forall n
$$

仍然與 RH 等價。

但它對 AMRAL 的工程化研究很重要，因為 global quantifier 的研究介面可以從「無界連續位置空間」改成「canonical countable sequence」。

---

# 9. 對 v0.9–v1.0 路線的含義

v0.9–v1.0 的主要技術成果是在抽象 Green 模型中建立可重播的局部 position certificate。

本輪顯示：

1. 單純繼續放大 local radius 不會自動補上 actual-zeta semantics。
2. 實際偏軸零點需要顯式水平偏移座標 $\delta$。
3. 偏軸 symmetry 本身已提供局部不定性。
4. 真正難點不是「局部能否出現負方向」，而是「如何讓局部負方向成為全域 Weil 負證人」。
5. Li / Bombieri–Lagarias criterion 提供另一條離散化 global quantifier 的自然接口。

因此下一輪不應把主要算力繼續投入：

$$
h
\longmapsto
\text{larger certified local radius}.
$$

而應投入：

$$
\text{global isolation},
$$

$$
\text{spectral dominance},
$$

或

$$
\text{Li-sequence arithmetic certification}.
$$

---

# 10. 外部一致性：compact-window positivity 的新障礙訊號

2026-08-25，Marcus Chuk 在 arXiv 上發布預印本 *Weil positivity in compact windows: certified two-sided bounds and a Landau--Widom decay law*。

該工作研究 support window

$$
[-L,L]
$$

上的 Weil positivity profile，並在

$$
L=0.8
$$

給出無條件嚴格下界

$$
Q(f)
\ge
8.9\times10^{-18}\|f\|_2^2
$$

對 support 長度 $1.6$ 的複值 test functions 成立。

同一工作亦指出某類 pointwise-envelope certificate 若隨 $L$ 擴張，必須處理的頻率尺度可達

$$
T_1
=
2\pi e^{A_L},
$$

其中

$$
A_L\sim4e^L,
$$

形成 double-exponential barrier。

這份工作截至本文件日期仍是近期預印本，不能作為本研究自己的 proof step；但它提供了一個外部一致性訊號：

> 單純把 compact window / local support 持續放大，未必是走向全域 RH closure 的有效工程策略。

這與 AMRAL v1.0 handoff 的「不要再以放大 local radius 為主要目標」方向相容。

---

# 11. GAP ledger

## CLOSED / CONDITIONAL-CLOSED

### G1. Off-axis zero to rational cell

狀態：

```text
CONDITIONAL_CLOSED
```

若 RH 為假，可把一個偏軸零點放入有理 compact off-axis cell。

---

### G2. Missing horizontal coordinate

狀態：

```text
MODEL_CORRECTION_IDENTIFIED
```

對本 transfer interface，ordinate-only occupancy 不足；需保留

$$
\delta=\beta-\frac12.
$$

---

### G3. Local off-axis symmetry block

狀態：

```text
CLOSED
```

偏軸 horizontal pair 在 Weil spectral pairing 中形成不定的二狀態 block。

---

### G4. Two-translate local negative inertia

狀態：

```text
CONDITIONAL_CLOSED
```

在 cell 上建構 nonvanishing Mellin seed，並取

$$
a>1,
$$

可使二維 restriction matrix 滿足

$$
\det B<0.
$$

---

## OPEN

### G5. Actual-zeta occupancy semantics

狀態：

```text
OPEN
```

需把 AMRAL 目前抽象 occupancy operator family 與實際 zeta zero orbit、multiplicity、cell semantics 完整接合。

---

### G6. Global Weil isolation / dominance

狀態：

```text
OPEN
```

需證明局部 target quartet 的負方向可提升成完整 Weil quadratic form 的負 witness，或找到等價的 global arithmetic contradiction。

---

### G7. Universal Li positivity certificate

狀態：

```text
OPEN
```

Li criterion 把問題壓成

$$
\lambda_n\ge0
\quad
\forall n\ge1,
$$

但仍缺 universal all-$n$ proof。

---

### G8. Global RH certificate

狀態：

```text
OPEN
```

目前沒有：

$$
RH
$$

的完整 proof，也沒有反例。

---

# 12. 建議下一節點

原本 v1.0 交接指定的

`RH-ConditionalOffAxisCell-ZetaTransfer-v1.1`

可以視為已取得第一階段條件式閉合。

下一節點建議命名：

`RH-LiExtremal-GlobalCompression-v1.2`

主要任務不是重新證明 Li criterion，而是建立 AMRAL 自己可驗證、可重播的 global-compression ledger：

1. 固定 Li coefficient normalization 與 zero-sum convention。
2. 把 Bombieri–Lagarias extremal-modulus argument 形式化成 dependency graph。
3. 明確分離：
   - known theorem；
   - AMRAL 新推導；
   - computational certificate；
   - still-open universal step。
4. 尋找是否存在比直接 all-$n$ positivity 更適合 AMRAL 目前 Green / PSD 架構的 arithmetic surrogate。
5. 對有限 $n$ 做嚴格 interval / exact arithmetic certificate，但明確禁止把有限驗證誤寫成全域 RH 證明。
6. 若要回到 Weil 路線，主攻 target isolation / dominance，不再主攻 local-radius expansion。

---

# 13. Trust boundary

本文件必須維持以下邊界：

```text
RH_CLAIM = FALSE
GLOBAL_RH_CERTIFICATE = FALSE
GLOBAL_WEIL_ISOLATION = FALSE
ACTUAL_ZETA_OCCUPANCY_FAMILY = FALSE
```

本輪真正建立或整理的是：

```text
OFFAXIS_TO_RATIONAL_CELL = TRUE
REPRESENTATION_REQUIRES_HORIZONTAL_OFFSET = TRUE
LOCAL_OFFAXIS_BLOCK_IS_INDEFINITE = TRUE
TWO_TRANSLATES_CAN_EXPOSE_LOCAL_NEGATIVE_INERTIA = TRUE
```

但以下推論目前**禁止**：

$$
\text{local negative block}
\not\Longrightarrow
\text{full Weil form negative}
$$

在沒有額外 isolation / dominance theorem 前，不能把局部負慣性提升成全域 RH conclusion。

同樣地：

$$
\text{finite Li verification}
\not\Longrightarrow
RH.
$$

任何有限高度、有限 $n$、有限 cell、有限 matrix 的計算，都只能按其實際量詞範圍登錄。

---

# 14. 目前一句話狀態

> v1.1 已把「假設存在偏軸 zeta 零點」嚴格轉移到帶有水平偏移座標的有理 off-axis cell，並證明該偏軸 symmetry pair 可由兩個 multiplicative translates 在局部 Weil restriction 中產生負慣性；但從局部負 block 到完整 Weil quadratic form 的全域 isolation / dominance 仍未閉合。下一步應轉向 Li-extremal 或其他 global-compression 架構，而不是繼續放大 local Green radius。

---

# 15. References

1. AMRAL, **佔用算子族與覆蓋式 Green 證書 · v0.9**.  
   https://amral.evemisslab.com/riemann/semi-autonomous/p/proto-occupancy-operatorfamily-v0.9/

2. AMRAL, **局部區間 Green 位置覆蓋 · v1.0**.  
   https://amral.evemisslab.com/riemann/semi-autonomous/p/proto-localintervalgreen-cellcover-v1.0/

3. AMRAL, **v0.1–v1.0 完整研究報告與 AI 交接**.  
   https://amral.evemisslab.com/riemann/semi-autonomous/p/proto-v0.1-v1.0-final-report-ai-handoff-v1.0/

4. Dave Platt and Tim Trudgian, **The Riemann hypothesis is true up to $3\cdot10^{12}$**, *Bulletin of the London Mathematical Society* 53 (2021), 792–797.  
   DOI: https://doi.org/10.1112/blms.12460  
   arXiv: https://arxiv.org/abs/2004.09765

5. Enrico Bombieri, **Remarks on Weil's quadratic functional in the theory of prime numbers, I**, *Rendiconti Lincei - Matematica e Applicazioni* 11 (2000), 183–233.  
   EUDML: https://eudml.org/doc/252338  
   BDM: https://www.bdim.eu/item?id=RLIN_2000_9_11_3_183_0

6. Xian-Jin Li, **The Positivity of a Sequence of Numbers and the Riemann Hypothesis**, *Journal of Number Theory* 65 (1997), 325–333.  
   DOI: https://doi.org/10.1006/jnth.1997.2137

7. Enrico Bombieri and Jeffrey C. Lagarias, **Complements to Li's Criterion for the Riemann Hypothesis**, *Journal of Number Theory* 77 (1999), 274–287.  
   DOI: https://doi.org/10.1006/jnth.1999.2392

8. Marcus Chuk, **Weil positivity in compact windows: certified two-sided bounds and a Landau--Widom decay law**, arXiv:2608.24827, submitted 2026-08-25.  
   https://arxiv.org/abs/2608.24827

---

# 16. Provenance

研究主導：Neo.K

本節點續推與整理：ChatGPT / GPT-5.6 Sol

日期：2026-09-02

研究定位：AMRAL 黎曼猜想半自主研究線之續接工程稿。

本文件是研究 source artifact，不是 peer-reviewed publication；所有 claim 應依 Claim register 與 Trust boundary 解讀。
