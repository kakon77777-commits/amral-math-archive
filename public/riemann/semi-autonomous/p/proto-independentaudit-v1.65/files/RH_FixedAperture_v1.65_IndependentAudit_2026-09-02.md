工程紀錄 · 第三弧線 v1.65 · 2026-09-02 · INDEPENDENT_AUDIT · VALIDATED_AS_REDUCTION · FINITE_PROBLEM_NOT_YET

# vRH 1.65：Fixed-Aperture Local Prime Criterion 獨立審核與「有限問題」邊界

**RH-FixedAperture-v1.65-IndependentAudit**

本文件不是 v1.6 後的新主研究節點，而是對：

`RH-FixedAperture-LocalPrimeDiscrepancy v1.6`

進行一次獨立 audit。

審核問題只有兩個：

1. v1.6 的 fixed-aperture reduction 是否在其他表示下仍成立？
2. 它是否已把 RH 真正化成 finite problem？

本次結論：

```text
V1.6_CORE_REDUCTION = VALIDATED
V1.6_LOCAL_PRIME_IDENTITY = VALIDATED
V1.6_DYADIC_COROLLARY = VALIDATED
V1.6_SUBEXPONENTIAL_SUFFICIENCY = VALIDATED

FIXED_TEMPORAL_MEMORY = TRUE
FINITE_DATA_AT_EACH_CHECKPOINT = TRUE

UNIFORM_BOUNDED_STATE_CARDINALITY = FALSE
FINITE_NUMBER_OF_CHECKPOINTS = FALSE
FINITE_GLOBAL_PROOF_OBJECT = NOT_YET

RH_PROVED = FALSE
RH_DISPROVED = FALSE
```

最重要的語義修正：

> v1.6 把 RH 變成 **fixed-aperture / local / finite-support per-event problem**，但尚未變成「有限個 instance 驗完即可結束」的 finite problem。

真正要從 local finite-memory 走到 finite proof object，仍缺：

$$
\boxed{
\text{a tail invariant / tail theorem closing all sufficiently large scales at once}.
}
$$

---

# 0. 外部基線

本 audit 只依賴幾個已公開基線。

Suzuki 已證：

$$
\boxed{
\int_0^\infty
\Psi(t)e^{izt}\,dt
=
-\frac1{z^2}
\frac{\xi'}{\xi}
\left(
\frac12-iz
\right),
\qquad
\Im z>\frac12,
}
$$

以及：

$$
\boxed{
RH
\Longleftrightarrow
\Psi(t)=O(1).
}
$$

Suzuki 亦給零點級數：

$$
\boxed{
\Psi(t)
=
\sum_\gamma
\frac{1-e^{i\gamma t}}{\gamma^2},
}
$$

其中 $\gamma$ 為：

$$
\xi\left(\frac12-i\gamma\right)=0
$$

的零點參數。

Arias de Reyna 另證明：

$$
\boxed{
RH
\Longleftrightarrow
\mu
\text{ is tempered},
}
$$

其中：

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
2\cosh(x/2)\,dx.
$$

這些都是外部已知 theorem；v1.65 不重新宣稱它們。

---

# 1. Audit object

固定任意：

$$
h>0.
$$

定義：

$$
\boxed{
D_h(t)
=
\frac12
\left[
\Psi(t+h)
+
\Psi(t-h)
-
2\Psi(t)
\right].
}
$$

$\Psi$ 使用其 even extension。

對：

$$
t\ge h
$$

三個 arguments 皆非負。

---

# 2. 第一條獨立驗證：離散二階差分反積分

假設對某個固定 $h$：

$$
D_h(t)
=
O(t^A)
$$

其中 $A<\infty$。

對每個 residue：

$$
r\in[0,h)
$$

定義：

$$
y_n(r)
=
\Psi(r+nh).
$$

則：

$$
\boxed{
y_{n+1}(r)-2y_n(r)+y_{n-1}(r)
=
2D_h(r+nh).
}
$$

由：

$$
D_h(r+nh)=O(n^A)
$$

一次離散求和：

$$
y_{n+1}-y_n
=
O(n^{A+1}),
$$

再求和：

$$
y_n
=
O(n^{A+2}).
$$

因為：

$$
r\in[0,h)
$$

是 compact set，而且 $\Psi$ 連續，所以初始資料：

$$
\Psi(r),
\qquad
\Psi(r+h)
$$

可 uniform 控制。

因此：

$$
\boxed{
D_h(t)=O(t^A)
\Longrightarrow
\Psi(t)=O(t^{A+2}).
}
$$

---

# 3. Laplace extension 閉合 RH

如果：

$$
\Psi(t)=O(t^B)
$$

對有限 $B$，則：

$$
F(z)
=
\int_0^\infty
\Psi(t)e^{izt}\,dt
$$

對：

$$
\Im z>0
$$

絕對收斂且 holomorphic。

在已知區域：

$$
\Im z>\frac12
$$

有 Suzuki identity：

$$
F(z)
=
-\frac1{z^2}
\frac{\xi'}{\xi}
\left(
\frac12-iz
\right).
$$

若存在：

$$
\rho=\beta+i\tau
$$

且：

$$
\beta>\frac12,
$$

取：

$$
z_\rho
=
-\tau
+
i
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

右側會有 pole，但左側在整個 upper half-plane holomorphic，矛盾。

所以：

$$
\Re\rho\le\frac12.
$$

functional equation：

$$
\rho\mapsto1-\rho
$$

再給：

$$
\Re\rho\ge\frac12.
$$

因此：

$$
\boxed{
D_h(t)=O(t^A)
\Longrightarrow RH.
}
$$

RH 反向由：

$$
\Psi=O(1)
$$

立即給：

$$
D_h=O(1).
$$

所以 v1.6 的主要 reduction 通過第一條 audit：

## Audit Theorem 3.1

對任意 fixed：

$$
h>0,
$$

$$
\boxed{
RH
\Longleftrightarrow
D_h(t)=O(1).
}
$$

而任一有限 polynomial growth：

$$
D_h(t)=O(t^A)
$$

都已足以推出 RH。

---

# 4. Subexponential 版本重新驗證

假設：

$$
D_h(t)=e^{o(t)}.
$$

對任意：

$$
\varepsilon>0,
$$

存在 $T_\varepsilon$ 使：

$$
|D_h(t)|
\le
e^{\varepsilon t}
$$

對：

$$
t\ge T_\varepsilon.
$$

在每個 residue lattice 上做兩次離散求和，只增加 polynomial factor，所以：

$$
\Psi(t)
=
e^{o(t)}.
$$

因此對任意：

$$
y>0,
$$

最終：

$$
|\Psi(t)|
\le
e^{yt/2},
$$

所以：

$$
\int_0^\infty
\Psi(t)e^{i(x+iy)t}\,dt
$$

對所有：

$$
y>0
$$

收斂。

因此同 Section 3：

$$
\boxed{
D_h(t)=e^{o(t)}
\Longrightarrow RH.
}
$$

結合 RH 下 boundedness：

$$
\boxed{
RH
\Longleftrightarrow
D_h(t)=e^{o(t)}.
}
$$

---

# 5. 第二條獨立驗證：零點 spectral filter

從 Suzuki：

$$
\Psi(t)
=
\sum_\gamma
\frac{1-e^{i\gamma t}}{\gamma^2}.
$$

對固定 $h$ termwise 取二階差分：

$$
\begin{aligned}
D_h(t)
&=
\frac12
\sum_\gamma
\frac{
-e^{i\gamma(t+h)}
-e^{i\gamma(t-h)}
+2e^{i\gamma t}
}{
\gamma^2
}
\\
&=
\sum_\gamma
\frac{
1-\cos(\gamma h)
}{
\gamma^2
}
e^{i\gamma t}.
\end{aligned}
$$

所以：

$$
\boxed{
D_h(t)
=
\sum_\gamma
c_h(\gamma)e^{i\gamma t},
\qquad
c_h(\gamma)
=
\frac{1-\cos(\gamma h)}{\gamma^2}.
}
$$

這是 fixed-aperture observable 的 spectral response。

---

# 6. 固定孔徑不會消掉偏軸 zero mode

設：

$$
\rho=\beta+i\tau
$$

為非平凡 zero。

對應：

$$
\gamma
=
-\tau
+
i
\left(
\beta-\frac12
\right).
$$

若偏軸：

$$
\beta\neq\frac12,
$$

則：

$$
\Im\gamma\neq0.
$$

若 filter coefficient 為零，需要：

$$
1-\cos(\gamma h)=0,
$$

即：

$$
\cos(\gamma h)=1.
$$

complex equation：

$$
\cos z=1
$$

的解為：

$$
z=2\pi k,
\qquad
k\in\mathbb Z,
$$

全為 real。

因此：

$$
\Im\gamma\neq0
\Longrightarrow
1-\cos(\gamma h)\neq0.
$$

所以：

$$
\boxed{
\text{no off-critical zero mode can be annihilated by a fixed }h>0.
}
$$

這是 v1.6 反向 theorem 的重要 spectral sanity check。

---

# 7. 新的定量 audit theorem：growth exponent = zero-strip width

定義 zeta zeros 的最大水平偏離：

$$
\boxed{
\Delta_\zeta
=
\sup_\rho
\left|
\Re\rho-\frac12
\right|.
}
$$

由 critical strip：

$$
0\le\Delta_\zeta\le\frac12.
$$

再定義 fixed-aperture exponential type：

$$
\boxed{
\sigma_h
=
\inf
\left\{
\sigma\ge0:
D_h(t)=O(e^{\sigma t})
\right\}.
}
$$

---

# 8. 上界：$\sigma_h\le\Delta_\zeta$

對 zero parameter：

$$
\gamma
=
-\tau
+
i
\left(
\beta-\frac12
\right),
$$

有：

$$
|\Im\gamma|
\le
\Delta_\zeta.
$$

因此：

$$
|e^{i\gamma t}|
\le
e^{\Delta_\zeta t}.
$$

而：

$$
|\Im(\gamma h)|
\le
\frac h2.
$$

所以：

$$
|\cos(\gamma h)|
\le
\cosh(h/2).
$$

故：

$$
|1-\cos(\gamma h)|
\le
1+\cosh(h/2).
$$

Suzuki zero series 具有：

$$
\sum_\gamma
\frac1{|\gamma|^2}
<
\infty.
$$

因此：

$$
|D_h(t)|
\le
C_h
e^{\Delta_\zeta t}
$$

對某 finite $C_h$。

所以：

$$
\boxed{
\sigma_h\le\Delta_\zeta.
}
$$

---

# 9. 下界：$\Delta_\zeta\le\sigma_h$

取任意：

$$
\sigma>\sigma_h.
$$

則：

$$
D_h(t)=O(e^{\sigma t}).
$$

若：

$$
\sigma>0,
$$

二次離散求和仍保持相同 exponential rate：

$$
\Psi(t)
=
O(e^{\sigma t}\operatorname{poly}(t)).
$$

因此 Laplace transform 至少在：

$$
\Im z>\sigma
$$

holomorphic。

所以不存在：

$$
\beta>\frac12+\sigma.
$$

由 functional symmetry，也不存在：

$$
\beta<\frac12-\sigma.
$$

因此：

$$
\Delta_\zeta\le\sigma.
$$

對所有：

$$
\sigma>\sigma_h
$$

成立，所以：

$$
\boxed{
\Delta_\zeta\le\sigma_h.
}
$$

與 Section 8 合併：

## Audit Theorem 9.1 · Exact aperture growth type

對任意 fixed：

$$
h>0,
$$

$$
\boxed{
\sigma_h
=
\Delta_\zeta.
}
$$

也就是：

> fixed-aperture observable 的最小 exponential growth exponent，精確等於所有 zeta zeros 對 critical line 的最大水平偏離。

所以：

$$
\boxed{
RH
\Longleftrightarrow
\sigma_h=0.
}
$$

這比單純：

$$
D_h=e^{o(t)}
$$

更精確。

---

# 10. Quantitative strip corollary

若能證：

$$
D_h(t)
=
O(e^{\sigma t})
$$

對某：

$$
0\le\sigma<\frac12,
$$

則所有 nontrivial zeros 均滿足：

$$
\boxed{
\left|
\Re\rho-\frac12
\right|
\le\sigma.
}
$$

因此 fixed-aperture method 具有連續的 quantitative meaning：

```text
growth exponent 1/2
    -> only critical strip scale

growth exponent sigma < 1/2
    -> improved zero strip

growth exponent 0
    -> RH
```

Suzuki 無條件 bound：

$$
\Psi(t)
\ll
e^{t/2-c\sqrt t}
$$

在 exponential-type 意義下仍對應：

$$
\sigma=\frac12.
$$

所以它不會免費推出比 critical strip 更強的固定寬度結論。

---

# 11. 第三條獨立驗證：local prime tent identity

對：

$$
t\ge h
$$

Suzuki prime side：

$$
-\sum_n
\frac{\Lambda(n)}{\sqrt n}
(t-\log n)_+
$$

取：

$$
\frac12\Delta_h^2.
$$

因為：

$$
\Delta_h^2
(t-a)_+
=
(h-|t-a|)_+,
$$

得到：

$$
\boxed{
D_h(t)
=
R_h(t)
-
\frac12
\sum_{
e^{t-h}<n<e^{t+h}
}
\frac{\Lambda(n)}{\sqrt n}
\left(
h-|t-\log n|
\right).
}
$$

其中：

$$
R_h(t)
=
\frac12\Delta_h^2\mathcal A(t).
$$

所以每個 checkpoint 的 arithmetic input 確實是 finite。

---

# 12. archimedean main term 再驗證

Suzuki smooth term中：

$$
4e^{-t/2}
$$

與 Hurwitz–Lerch 展開的：

$$
m=0
$$

項精確消掉。

剩餘 leading smooth component：

$$
4e^{t/2}.
$$

其 half second difference：

$$
\frac12
\Delta_h^2
\left(
4e^{t/2}
\right)
=
4e^{t/2}
\left(
\cosh\frac h2-1
\right).
$$

因此 local prime sum 的 natural main term 是：

$$
\boxed{
8e^{t/2}
\left(
\cosh\frac h2-1
\right).
}
$$

定義：

$$
L_h(t)
=
\sum_{
e^{t-h}<n<e^{t+h}
}
\frac{\Lambda(n)}{\sqrt n}
\left(
h-|t-\log n|
\right)
$$

與：

$$
\mathcal E_h(t)
=
L_h(t)
-
8e^{t/2}
\left(
\cosh\frac h2-1
\right).
$$

則：

$$
\boxed{
D_h(t)
=
-\frac12\mathcal E_h(t)
-
\mathcal R_h(t),
}
$$

其中：

$$
\mathcal R_h(t)
=
O_h(e^{-5t/2}).
$$

所以：

$$
D_h
$$

與：

$$
\mathcal E_h
$$

具有完全相同的 exponential type。

---

# 13. Local-prime growth type

令：

$$
x=e^t.
$$

定義：

$$
\mathfrak E_h(x)
=
\sum_{
xe^{-h}<n<xe^h
}
\frac{\Lambda(n)}{\sqrt n}
\left(
h-\left|\log\frac nx\right|
\right)
-
8\sqrt x
\left(
\cosh\frac h2-1
\right).
$$

由 Section 9 與 Section 12：

$$
\boxed{
\inf
\left\{
\sigma\ge0:
\mathfrak E_h(x)=O(x^\sigma)
\right\}
=
\Delta_\zeta.
}
$$

因此：

$$
\boxed{
RH
\Longleftrightarrow
\mathfrak E_h(x)=x^{o(1)}.
}
$$

RH 下更有：

$$
\mathfrak E_h(x)=O_h(1).
$$

---

# 14. Dyadic audit

取：

$$
h=\log2.
$$

則：

$$
xe^{-h}=\frac x2,
$$

$$
xe^h=2x.
$$

並且：

$$
8
\left(
\cosh\frac{\log2}{2}-1
\right)
=
6\sqrt2-8.
$$

所以：

$$
\boxed{
\begin{aligned}
\mathfrak E_2(x)
&=
\sum_{x/2<n<2x}
\frac{\Lambda(n)}{\sqrt n}
\left(
\log2-\left|\log\frac nx\right|
\right)
\\
&\quad
-
(6\sqrt2-8)\sqrt x.
\end{aligned}
}
$$

且：

$$
\boxed{
\inf
\left\{
\sigma:
\mathfrak E_2(x)=O(x^\sigma)
\right\}
=
\Delta_\zeta.
}
$$

特別地：

$$
\boxed{
RH
\Longleftrightarrow
\mathfrak E_2(x)=x^{o(1)}.
}
$$

這確認 v1.6 dyadic form 的數學方向沒有在換變數時遺失量詞。

---

# 15. 第四條獨立驗證：adjacent-block identity

定義：

$$
S(x)
=
\sum_{n\le x}
\frac{\Lambda(n)}{\sqrt n}.
$$

令：

$$
A(u)=S(e^u).
$$

則 local tent sum可寫成 Stieltjes integral：

$$
L_h(t)
=
\int_{t-h}^{t+h}
\left(
h-|t-u|
\right)dA(u).
$$

分成左右兩半做 integration by parts：

$$
\boxed{
L_h(t)
=
\int_t^{t+h}A(u)\,du
-
\int_{t-h}^{t}A(u)\,du.
}
$$

令：

$$
B(x)
=
S(x)-2\sqrt x.
$$

則：

$$
\boxed{
\mathfrak E_h(x)
=
\int_x^{xe^h}
\frac{B(y)}{y}\,dy
-
\int_{xe^{-h}}^x
\frac{B(y)}{y}\,dy.
}
$$

所以 fixed-aperture discrepancy 是：

> 相鄰兩個固定 logarithmic blocks 的 weighted cumulative-prime error difference。

---

# 16. Dyadic adjacent-block form

對：

$$
h=\log2,
$$

得到：

$$
\boxed{
\mathfrak E_2(x)
=
\int_x^{2x}
\frac{B(y)}{y}\,dy
-
\int_{x/2}^{x}
\frac{B(y)}{y}\,dy.
}
$$

Arias de Reyna 在 RH 下引用標準結果並得到：

$$
S(x)
=
2\sqrt x
+
O(\log^3x).
$$

所以：

$$
B(x)=O(\log^3x).
$$

這至少立刻給：

$$
\mathfrak E_2(x)
=
O(\log^3x),
$$

與 v1.65 反向 sufficiency 完全相容。

Suzuki 的 bounded $\Psi$ 結構則進一步給實際 RH-equivalent sharp form：

$$
\mathfrak E_2(x)=O(1).
$$

不存在矛盾；前者只是較弱的 RH consequence。

---

# 17. 與 tempered-distribution theorem 的一致性

Arias de Reyna 的 measure：

$$
\mu
=
-
\sum_n
\frac{\Lambda(n)}{\sqrt n}
\left(
\delta_{\log n}
+
\delta_{-\log n}
\right)
+
2\cosh(x/2)\,dx
$$

在 RH 下且僅在 RH 下 tempered。

v1.65 的 local discrepancy本質上是：

$$
\mu
$$

與固定 compact tent kernel 的 translate pairing，再加已完全顯式可控的 trivial / archimedean correction normalization。

所以：

```text
GLOBAL TEMPERED PRIME-ARCH DISTRIBUTION
        |
        v
FIXED COMPACT TENT OBSERVABLE
        |
        v
LOCAL PRIME DISCREPANCY
```

這不是一個獨立 proof of v1.6，但提供第四條外部一致性路徑。

---

# 18. 數值 normalization audit

本節點附獨立 reference checker。

它以兩條不同方式計算：

### Route A

直接使用 Suzuki 原始：

$$
\Psi(t)
$$

公式，包括：

- full cumulative prime ramp；
- Hurwitz–Lerch term；
- gamma / archimedean constants；

然後計算：

$$
D_h(t)
=
\frac12
[
\Psi(t+h)+\Psi(t-h)-2\Psi(t)
].
$$

### Route B

直接只枚舉 local window：

$$
e^{t-h}<p^k<e^{t+h}
$$

並使用 tent formula。

### Route C

以 cumulative step function：

$$
S(x)
$$

計算 adjacent-block integral identity。

測試：

- $h=\log2$；
- $h=0.4$；
- $h=1.1$；
- 多組 $t$；

在 60 位以上 precision 下，Route A / B residual 約為：

$$
10^{-59}
$$

量級；具體結果附於：

`vrh165_crosscheck_residuals.csv`

這只是 normalization / algebra sanity check，不是 RH evidence。

---

# 19. 「有限問題」到底是哪一種有限？

需要把有限性拆成五層。

## F1 · Fixed support per prime

每個 prime power $q$ 對：

$$
D_h
$$

只在：

$$
[\log q-h,\log q+h]
$$

有作用。

狀態：

```text
TRUE
```

---

## F2 · Finite data per checkpoint

對 fixed：

$$
t<\infty,
$$

只需要：

$$
e^{t-h}<q<e^{t+h}
$$

的有限 prime powers。

狀態：

```text
TRUE
```

---

## F3 · Bounded number of active primes

這是錯的。

固定 multiplicative window：

$$
[xe^{-h},xe^h]
$$

中的 primes 數量隨：

$$
x\to\infty
$$

仍無界增加。

粗略規模：

$$
\asymp_h
\frac{x}{\log x}.
$$

所以：

```text
FIXED TEMPORAL WIDTH = TRUE
FIXED ACTIVE CARDINALITY = FALSE
```

---

## F4 · Finite number of checkpoints

prime event set：

$$
\{
\log q-h,\log q,\log q+h
\}
$$

仍有無限多個元素。

所以：

```text
COUNTABLE CHECKPOINT REDUCTION = TRUE
FINITE CHECKPOINT REDUCTION = FALSE
```

---

## F5 · Finite global proof object

目前還沒有。

我們尚未得到某個 finite $T_0$ 後，自動對所有 event 成立的 invariant。

所以：

```text
FINITE GLOBAL CLOSURE = OPEN
```

---

# 20. 更精確的系統分類

v1.6 最適合稱為：

$$
\boxed{
\text{finite-horizon, locally finite, infinitely driven arithmetic system}.
}
$$

而不是：

$$
\text{finite-state system}.
$$

它的 control modes 很少：

```text
ENTER
CENTER
EXIT
SMOOTH_SERVICE
```

但 event times 與 weights：

$$
(\log p^k,\Lambda(p^k)/\sqrt{p^k})
$$

形成無限 input stream。

即使只保留 aggregate scalar state，若要 exact streaming，仍需要處理未來 center / exit schedules。

---

# 21. 什麼條件下才真的變成 finite proof problem？

若能證明一個 theorem：

存在 finite：

$$
T_0,
$$

使對所有：

$$
t\ge T_0
$$

都有：

$$
\boxed{
|D_h(t)|
\le
C(1+t)^A
}
$$

或更弱：

$$
\boxed{
|D_h(t)|
\le
e^{o(t)},
}
$$

那 v1.65 已經證明這直接推出 RH。

若這個 tail theorem 的使用需要檢查有限 base states：

$$
t\le T_0,
$$

則 proof architecture 可真正變成：

$$
\boxed{
\text{finite prefix certificate}
+
\text{one invariant theorem}
=
\text{global closure}.
}
$$

這才是「變成有限問題」的正確意義。

---

# 22. 但 tail theorem 本身就是現在的 RH 級 GAP

因為：

$$
\boxed{
D_h=e^{o(t)}
\Longleftrightarrow RH.
}
$$

所以不能把：

```text
prove eventual subexponential tail
```

描述成已經較簡單到接近 routine 的剩餘工作。

它是一個**重新定位後的 RH-complete GAP**。

v1.6 真正改善的是：

- locality；
- memory geometry；
- proof engineering；
- certificate reproducibility；
- prime-side interpretability；

不是自動降低 theorem complexity。

---

# 23. Neutral triplet 不等於自動 bounded

單一 prime event有：

$$
+\frac{w}{2},
\qquad
-w,
\qquad
+\frac{w}{2},
$$

淨 impulse：

$$
0.
$$

但不能推出：

$$
D_h=O(1).
$$

原因包括：

1. 大量 tent 會重疊；
2. event density 無界增加；
3. event gaps 改變；
4. smooth service 與 arithmetic impulses 的 phase coupling 仍需控制；
5. zero net impulse 只控制總 derivative jump，不控制 excursion amplitude。

所以：

$$
\boxed{
\text{zero net memory}
\not\Longrightarrow
\text{bounded trajectory}.
}
$$

這是 v1.65 必須加入的防誤讀。

---

# 24. 「有限化」真正得到的是什麼？

可以安全地說：

### 已得到

$$
\boxed{
\text{global historical dependence}
\rightarrow
\text{fixed local aperture}.
}
$$

$$
\boxed{
\text{permanent prime ramp}
\rightarrow
\text{compact prime tent}.
}
$$

$$
\boxed{
\text{continuous local interval}
\rightarrow
\text{event checkpoints + at most one convex minimum}.
}
$$

### 尚未得到

$$
\boxed{
\text{infinitely many scales}
\rightarrow
\text{finitely many scales}.
}
$$

這最後一步就是 v1.7 真正要找的 invariant。

---

# 25. v1.65 對 v1.6 的正式審核結論

## VALIDATED

### V1

$$
RH
\Longleftrightarrow
D_h=O(1)
$$

for every fixed $h>0$。

### V2

任一：

$$
D_h=O(t^A)
$$

with finite $A$ 足以推出 RH。

### V3

$$
D_h=e^{o(t)}
$$

足以推出 RH。

### V4

local prime tent identity正確。

### V5

dyadic coefficient：

$$
6\sqrt2-8
$$

正確。

### V6

prime memory support長度：

$$
2h
$$

正確。

### V7

neutral triplet：

$$
+\frac12w,-w,+\frac12w
$$

正確。

### V8

fixed-aperture filter不會 annihilate off-axis zero modes。

### V9

exponential type identity：

$$
\sigma_h=\Delta_\zeta
$$

成立。

### V10

adjacent-block identity成立。

---

# 26. SCOPE CORRECTIONS

### C1

原本「finite-memory prime process」應解讀為：

```text
finite temporal support per prime
```

而不是：

```text
bounded-size finite state.
```

### C2

每個 checkpoint 的 input finite，但其 cardinality不 uniform bounded。

### C3

checkpoint family仍 infinite。

### C4

v1.6 尚未把 RH 化成 finite numerical verification。

### C5

`x^{o(1)}` tail 本身就是 RH-complete，不應當作已接近 routine 的最後一步。

---

# 27. 下一步建議：v1.7 不要再找等價式

下一節點仍建議：

`RH-LocalPrime-SubexponentialBridge-v1.7`

但工作要改成更嚴格的三分法：

## Route A · Try to prove an invariant

尋找 local event dynamics 的 structural quantity：

$$
I_h(t)
$$

使：

$$
I_h(t)\le C
$$

能推出：

$$
D_h=e^{o(t)}.
$$

---

## Route B · Prove impossibility / insufficiency results

逐一排除：

- zero net impulse alone；
- bounded average event weight alone；
- ordinary PNT error alone；
- finite-order Toeplitz PSD alone；
- local convexity alone；

是否足以閉合。

這能避免重複撞假捷徑。

---

## Route C · Quantitative strip program

不要一開始只追：

$$
\sigma=0.
$$

先研究能否從 local dynamics 無條件得到：

$$
\sigma<\frac12.
$$

因為任何：

$$
D_h=O(e^{\sigma t}),
\qquad
\sigma<\frac12,
$$

都會給真正新的 zero-free fixed strip：

$$
\boxed{
\left|
\Re\rho-\frac12
\right|
\le\sigma.
}
$$

這提供一個比 binary RH 更有梯度的研究 benchmark。

---

# 28. Trust boundary

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE

V1_6_CORE = VALIDATED_AS_REDUCTION
V1_6_FINITE_MEMORY = VALIDATED_WITH_TERMINOLOGY_CORRECTION

FINITE_GLOBAL_PROBLEM = FALSE
TAIL_INVARIANT = OPEN

NOVELTY_PRIORITY_OF_FIXED_APERTURE_FORM = NOT_ESTABLISHED
GLOBAL_RH_CERTIFICATE = FALSE
```

禁止：

$$
\text{local finite data}
\Longrightarrow
\text{finite global proof}.
$$

禁止：

$$
\text{zero-net prime triplet}
\Longrightarrow
\text{bounded discrepancy}.
$$

---

# 29. 一句話狀態

> v1.65 以四條互相獨立的表示重新審核 v1.6：離散二階差分 + Suzuki Laplace 延拓、zero-mode spectral filter、local prime tent explicit formula、以及 adjacent-block / tempered-distribution 表示均彼此吻合。更進一步，對任意固定 $h>0$，fixed-aperture observable 的最小 exponential growth exponent $\sigma_h$ 精確等於 zeta zeros 對 critical line 的最大水平偏離 $\Delta_\zeta$；因此 $x^{o(1)}$ local discrepancy 精確對應 RH，而 $O(x^\sigma)$ 對應寬度 $\sigma$ 的 zero strip。v1.6 的「有限化」是真實但必須精確描述：每個 prime 的 temporal support固定、每個 checkpoint 使用有限 local prime data，但 active cardinality與 checkpoint 數仍無界，所以尚未成為有限枚舉問題。真正 finite closure 仍需要一個能一次控制所有 sufficiently large scales 的 tail invariant；而這個 invariant 本身正是目前 RH-complete 的主要 GAP。

---

# 30. References

1. Masatoshi Suzuki, **Aspects of the screw function corresponding to the Riemann zeta-function**, *Journal of the London Mathematical Society* 108 (2023), 1448–1487.  
   DOI: https://doi.org/10.1112/jlms.12785  
   arXiv: https://arxiv.org/abs/2206.03682

2. Juan Arias de Reyna, **Explicit formula and quasicrystal definition**, arXiv:2402.10604, current source dated 2026-03-22.  
   https://arxiv.org/abs/2402.10604

3. AMRAL, **RH-FixedAperture-LocalPrimeDiscrepancy v1.6**, 2026-09-02.  
   Canonical local source from the preceding AMRAL research node.

---

# 31. Provenance

研究主導：Neo.K

v1.65 獨立審核、quantitative growth-strip theorem、adjacent-block derivation、numerical cross-check 與 canonical source 整理：ChatGPT / GPT-5.6 Sol

日期：2026-09-02

研究定位：AMRAL 黎曼猜想半自主研究線，v1.6 validation / finite-problem boundary audit。

本文件是 research source artifact，不是 peer-reviewed publication。

所有 claim 必須依 Claim register、Scope Corrections 與 Trust boundary 解讀。
