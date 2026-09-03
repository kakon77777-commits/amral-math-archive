工程紀錄 · 第三弧線 v1.4 · 2026-09-02 · EXACT_DIAGONAL_BRIDGE · UNIFORM_GAP_NO_GO · RH_CLAIM_FALSE

# Weil 正錐、Suzuki 對角脊線與 Recovery-Witness Schur Reserve

**RH-WeilCheckpoint-GreenDiagonalBridge v1.4**

本節點承接：

- `RH-ConditionalOffAxisCell-ZetaTransfer-v1.1`
- `RH-GlobalQuantifier-PrimePowerConvexCompression-v1.2`
- `RH-OffAxisCell-LiWitnessCompiler-v1.3`

v1.2–v1.3 已辨識 Suzuki / Mittermeier prime-power checkpoint 路線與 AMRAL 原有 arithmetic PSD / Green 路線之間存在結構重疊，但尚未把兩者放入同一個 canonical operator picture。

本節點完成第一個精確橋接：

$$
\boxed{
\text{Suzuki checkpoint}
=
\text{Weil quadratic form 沿一個一參數 rectangular ray 的取值}
=
\frac12\text{ screw Green kernel 的對角值}.
}
$$

因此，checkpoint 並不是另一套與 AMRAL 平行的 RH criterion；它是 Weil / Green 正錐中的一條特殊一參數脊線，而且 Suzuki 證明這條脊線本身已經 **RH-complete**。

本節點同時得到一個重要的 no-go 結論：

> 若 RH 成立，最新 recovery-witness frontier 所引用的 asymptotic 行為給出 $\liminf_{t\to\infty}\Psi(t)=0$。因此任何忠實包含 screw-kernel 對角接觸的矩陣族，都不可能具有支撐尺度無關的固定正 spectral gap。AMRAL 若把「全域固定正裕量」當成 proof target，方向本身就過強。

最後，本節點定義一個新的 **Recovery-Witness Gram / Schur Reserve** 接口，把 AMRAL 的 matrix PSD 語言與 Mittermeier 的 capacity–cost 語言放入同一個有限維擴張公式。

**RH_CLAIM = False.**

---

# 0. Claim register

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE

WEIL_RECTANGULAR_RAY_IDENTITY = TRUE
SCREW_DIAGONAL_IDENTITY = TRUE
RECTANGULAR_RAY_RH_COMPLETENESS = REFERENCE_CLOSED

CHECKPOINT_IS_WEIL_CONE_SLICE = TRUE
CHECKPOINT_IS_GREEN_DIAGONAL = TRUE

UNIFORM_ABSOLUTE_GREEN_GAP = IMPOSSIBLE_UNDER_RH
UNIFORM_ABSOLUTE_SCHUR_RESERVE = IMPOSSIBLE_FOR_CONTACTING_FAMILIES

RECOVERY_WITNESS_SCHUR_RESERVE = NEW_ENGINEERING_BRIDGE
MITTERMEIER_CJ_EQUALS_SCHUR_RESERVE = NOT_CLAIMED

AMRAL_M_ARITH_EQUALS_SUZUKI_KERNEL_MATRIX = NOT_PROVED
GLOBAL_RH_CERTIFICATE = FALSE
```

---

# 1. Canonical Weil quadratic form

令 $W$ 為 Riemann zeta 對應的 Weil distribution。

對合法 test function $\psi$，定義：

$$
Q_W(\psi)
:=
W(\psi\ast\widetilde\psi),
$$

其中：

$$
\widetilde\psi(x)
=
\overline{\psi(-x)}.
$$

Weil positivity criterion 給出：

$$
\boxed{
RH
\Longleftrightarrow
Q_W(\psi)\ge0
\quad
\forall\psi\in C_c^\infty(\mathbb R).
}
$$

Suzuki 的 screw-function framework 把這個 distributional quadratic form 改寫成 continuous kernel / operator 語言。

AMRAL 的 arithmetic matrix / PSD 原型本質上亦在有限 test-function basis 上計算同類型的 quadratic form：

$$
M_{ij}
=
W(\psi_i\ast\widetilde{\psi_j}),
$$

使：

$$
c^\ast Mc
=
Q_W
\left(
\sum_i c_i\psi_i
\right).
$$

所以 finite-dimensional PSD matrix 是 Weil positive cone 的有限維 Galerkin slice。

AMRAL 目前的 `$M_{\rm arith}$` 有自己的 normalization、archimedean / finite-position 分解與 basis；在未做逐項 normalization identification 前，不能把它直接等同於後面定義的 Suzuki screw-kernel matrix。

---

# 2. Suzuki 的 $\Psi(t)$ 是一條 Weil rectangular ray

Suzuki 定義：

$$
\Delta_t(x)
=
\begin{cases}
\frac12(t-|x|), & |x|\le t,\\
0, & |x|>t,
\end{cases}
$$

並選 rectangular function：

$$
R_t(x)
=
\begin{cases}
\frac1{\sqrt2}, & |x|<t/2,\\
\frac1{2\sqrt2}, & |x|=t/2,\\
0, & |x|>t/2.
\end{cases}
$$

則：

$$
\boxed{
\Delta_t
=
R_t\ast\widetilde R_t.
}
$$

Suzuki 證明：

$$
\boxed{
W(\Delta_t)=\Psi(t).
}
$$

因此：

$$
\boxed{
\Psi(t)
=
Q_W(R_t).
}
$$

定義 rectangular ray：

$$
\mathfrak R
=
\{R_t:t>0\}.
$$

則 Suzuki 的 pointwise theorem 可以重新寫成：

## Theorem 2.1 · Rectangular-ray completeness

$$
\boxed{
RH
\Longleftrightarrow
Q_W(R_t)\ge0
\quad
\forall t>0.
}
$$

也就是：

$$
\boxed{
RH
\Longleftrightarrow
\mathfrak R
\subset
\mathcal C_W,
}
$$

其中：

$$
\mathcal C_W
=
\{\psi:Q_W(\psi)\ge0\}
$$

表示 Weil positivity cone。

這是一個非常強的 compression：

一般 Weil criterion 要求所有 compact test functions；

Suzuki 告訴我們，對 Riemann zeta 的特殊結構而言，一條一參數 rectangular ray 已經 RH-complete。

---

# 3. Screw Green kernel 的精確對角橋

Suzuki 的 screw function 記為：

$$
g(t)=-\Psi(t).
$$

因為 $\Psi$ 為實偶函數且：

$$
\Psi(0)=0,
$$

定義 screw kernel：

$$
G_g(t,u)
=
g(t-u)-g(t)-g(-u)+g(0).
$$

代入：

$$
g=-\Psi
$$

得到：

$$
\boxed{
G_g(t,u)
=
\Psi(t)+\Psi(u)-\Psi(t-u).
}
$$

特別地：

$$
G_g(t,t)
=
2\Psi(t)-\Psi(0).
$$

所以：

$$
\boxed{
G_g(t,t)=2\Psi(t).
}
$$

因此三個物件其實是同一個 scalar state：

$$
\boxed{
Q_W(R_t)
=
\Psi(t)
=
\frac12G_g(t,t).
}
$$

---

# 4. 三種研究語言其實在看同一個 positivity object

現在可以把三條語言精確對齊。

## 4.1 Weil / arithmetic language

$$
Q_W(\psi)\ge0.
$$

## 4.2 Green / screw-kernel language

$$
G_g
\succeq0.
$$

## 4.3 Suzuki checkpoint language

$$
\Psi(t)\ge0.
$$

對一般 positive kernel：

$$
G_g(t,t)\ge0
$$

只是一個必要條件，通常遠弱於：

$$
G_g\succeq0.
$$

但 zeta screw function 是特殊情況。

Suzuki 證明：

$$
\boxed{
G_g(t,t)\ge0
\quad
\forall t
\Longleftrightarrow
RH.
}
$$

而 RH 又推出整個 screw kernel nonnegative definite。

因此這裡存在一個特殊的：

```text
DIAGONAL SUFFICIENCY
```

亦即：

$$
\boxed{
\text{all diagonal checkpoints positive}
\Longrightarrow
\text{full RH}
\Longrightarrow
\text{full screw-kernel PSD}.
}
$$

這不是一般 kernel theory 的代數事實，而是 Riemann zeta / Suzuki theorem 的特殊解析結果。

---

# 5. AMRAL arithmetic matrix 與 checkpoint 的正確關係

令有限 basis：

$$
\mathcal B_m
=
\{\psi_1,\ldots,\psi_m\}.
$$

定義：

$$
M^{(m)}_{ij}
=
W(\psi_i\ast\widetilde{\psi_j}).
$$

若某個 $R_t$ 可以在 basis 中精確表示：

$$
R_t
=
\sum_{i=1}^m c_i(t)\psi_i,
$$

則：

$$
\boxed{
\Psi(t)
=
c(t)^\ast
M^{(m)}
c(t).
}
$$

所以 checkpoint 是 finite matrix Rayleigh evaluation。

若只做近似：

$$
R_t\approx
\sum_i c_i(t)\psi_i,
$$

則不能僅靠近似 norm 宣稱：

$$
\Psi(t)
\approx
c^\ast Mc
$$

已足以證明符號。

必須額外給：

- explicit-formula truncation bound；
- test-function approximation error；
- archimedean error；
- prime-side directed rounding；
- convolution / endpoint normalization error。

因此：

```text
FINITE_BASIS_APPROXIMATION
!=
RIGOROUS_CHECKPOINT_CERTIFICATE
```

除非誤差被完整封住。

---

# 6. Recovery workload 是 Weil ray energy 的導數

Mittermeier Part 4 使用：

$$
Y(t)
=
-\Psi'(t)
$$

作為 workload。

由 Section 2：

$$
\Psi(t)=Q_W(R_t).
$$

所以：

$$
\boxed{
Y(t)
=
-\frac d{dt}
Q_W(R_t).
}
$$

這表示 workload 不是外加的新變數。

它是 Weil quadratic energy 沿 rectangular ray 的負導數。

Mittermeier 再定義 service clock：

$$
\tau
=
\mathcal A'(t),
$$

並得到 prime-power events 之間：

$$
\boxed{
\frac{dY}{d\tau}
=
-1.
}
$$

每當 $q=p^k$ 的 prime-power event 啟動：

$$
\boxed{
Y^+
=
Y^-
+
\frac{\Lambda(q)}{\sqrt q}.
}
$$

所以 recovery-witness picture 可以重新理解為：

> rectangular Weil ray 沿 support parameter $t$ 演化；archimedean curvature 提供 continuous service，prime powers 以離散 jump 注入 arithmetic workload；RH positivity 問題是在這條 ray 上，energy 是否永遠不穿過零。

---

# 7. Green diagonal dynamics

因為：

$$
G_g(t,t)=2\Psi(t),
$$

所以：

$$
\frac d{dt}
G_g(t,t)
=
2\Psi'(t).
$$

因此：

$$
\boxed{
Y(t)
=
-\frac12
\frac d{dt}
G_g(t,t).
}
$$

Mittermeier 的 active episode：

$$
Y>0
$$

對應：

$$
\frac d{dt}G_g(t,t)<0.
$$

也就是 screw Green diagonal 正在下降。

recovery：

$$
Y=0
$$

則是 diagonal energy 的局部極小候選點。

所以 recovery-witness architecture 可以直接翻譯成：

```text
GREEN-DIAGONAL DRAWDOWN / RECOVERY PROCESS
```

而不是另一個不相關的 prime-number model。

---

# 8. Exact finite recovery-segment area identity

假設某個 recovery witness $q$ 是一個 recovered episode 的最後 active event。

令：

$$
t_q=\log q,
$$

並假設在下一個 prime-power event 前 workload 已恢復到：

$$
Y(t_\ast)=0.
$$

在：

$$
[t_q,t_\ast]
$$

內沒有新的 jump。

因為：

$$
Y=-\Psi',
$$

所以：

$$
\Psi(t_\ast)
=
\Psi(t_q)
-
\int_{t_q}^{t_\ast}
Y(s)\,ds.
$$

等價地：

$$
\boxed{
\frac12G_g(t_\ast,t_\ast)
=
\frac12G_g(t_q,t_q)
-
\int_{t_q}^{t_\ast}Y(s)\,ds.
}
$$

這是一個 exact level–area identity。

用 service clock：

$$
\tau=\mathcal A'(t)
$$

且：

$$
\frac{dY}{d\tau}=-1,
$$

令：

$$
\tau_q=\mathcal A'(t_q).
$$

若：

$$
Y_q=Y(t_q^+)>0,
$$

則 recovery 發生在：

$$
\tau_\ast=\tau_q+Y_q.
$$

因此：

$$
Y(\tau)
=
Y_q-(\tau-\tau_q).
$$

又：

$$
dt
=
\frac{d\tau}{\mathcal A''(t(\tau))}.
$$

所以最後 recovery segment 的 drawdown 精確為：

$$
\boxed{
D_q
=
\int_{\tau_q}^{\tau_q+Y_q}
\frac{
Y_q-(\tau-\tau_q)
}{
\mathcal A''(t(\tau))
}
\,d\tau.
}
$$

並且：

$$
\boxed{
\Psi(t_\ast)
=
\Psi(t_q)-D_q.
}
$$

這提供一個直接的 Green-diagonal capacity / debit picture。

本文件不宣稱：

$$
D_q=\mathcal J_q
$$

或：

$$
\Psi(t_q)=\mathcal C_q
$$

等同於 Mittermeier Part 3–5 的 exact normalization。

要建立該 equality 必須逐式對齊其 $\mathcal C_q,\mathcal J_q$ 定義。

目前合法結論是：

> recovery-witness 的 level–area inequality 與 Green diagonal 的 energy reserve 具有精確的同一條 pathwise calculus；Mittermeier 的 $\mathcal C_q-\mathcal J_q$ 是該全局 episode accounting 的一個具體算術化版本。

---

# 9. Curvature-only recovery drawdown bound

在 final recovery segment 上，令：

$$
m_q
=
\inf_{t\in[t_q,t_\ast]}
\mathcal A''(t),
$$

$$
M_q
=
\sup_{t\in[t_q,t_\ast]}
\mathcal A''(t).
$$

兩者皆正。

則：

$$
\frac1{M_q}
\le
\frac1{\mathcal A''(t(\tau))}
\le
\frac1{m_q}.
$$

而：

$$
\int_{\tau_q}^{\tau_q+Y_q}
\left[
Y_q-(\tau-\tau_q)
\right]d\tau
=
\frac{Y_q^2}{2}.
$$

所以：

$$
\boxed{
\frac{Y_q^2}{2M_q}
\le
D_q
\le
\frac{Y_q^2}{2m_q}.
}
$$

因此一個充分的 local recovery safety condition 是：

$$
\boxed{
\Psi(t_q)
\ge
\frac{Y_q^2}{2m_q}
\Longrightarrow
\Psi(t_\ast)\ge0.
}
$$

這只是最後無 jump recovery segment 的局部 bound。

它不包含較早 episode 所累積的全部 arithmetic memory，因此不能直接取代 Mittermeier 的 all-event $\mathcal J_q\le\mathcal C_q$ frontier。

但它給 AMRAL 一個非常乾淨、可 interval-certify 的 local Green budget。

---

# 10. 最新 frontier 告訴我們：固定正 reserve floor 不存在

Mittermeier Part 5 的最新公開結果登錄：

在 RH 下：

$$
\Psi
$$

為 uniformly almost periodic，且：

$$
\boxed{
\liminf_{t\to\infty}\Psi(t)=0.
}
$$

其摘要亦指出：

> no positive uniform reserve floor can close the tail.

由：

$$
G_g(t,t)=2\Psi(t),
$$

立刻得到：

$$
\boxed{
\liminf_{t\to\infty}
G_g(t,t)=0
}
$$

在 RH 下成立。

這對 matrix strategy 有直接後果。

---

# 11. No-Uniform-Spectral-Gap Theorem

取任意序列：

$$
t_n\to\infty
$$

使：

$$
\Psi(t_n)\to0^+.
$$

對任何 finite screw-kernel Gram matrix：

$$
K_n
=
\left[
G_g(s_i,s_j)
\right]_{i,j=1}^{m_n}
$$

只要其 point set 包含 $t_n$。

若 RH 成立，則：

$$
K_n\succeq0.
$$

Rayleigh quotient 使用對應 coordinate vector $e_{t_n}$：

$$
\lambda_{\min}(K_n)
\le
e_{t_n}^\ast K_n e_{t_n}.
$$

而：

$$
e_{t_n}^\ast K_n e_{t_n}
=
G_g(t_n,t_n)
=
2\Psi(t_n).
$$

所以：

$$
\boxed{
0\le
\lambda_{\min}(K_n)
\le
2\Psi(t_n)
\to0.
}
$$

因此：

## Theorem 11.1 · No uniform absolute spectral gap

在 RH 成立的情況下，任何包含 arbitrarily late near-contact diagonal points 的忠實 screw-kernel Gram family，都不可能存在：

$$
\varepsilon>0
$$

使：

$$
\lambda_{\min}(K_n)\ge\varepsilon
$$

對所有 $n$ 成立。

也就是：

$$
\boxed{
\text{PSD can remain true while the absolute certificate margin must approach zero.}
}
$$

---

# 12. 對 AMRAL Green / PSD 工程的含義

AMRAL v0.1–v1.0 曾大量追蹤：

- smallest eigenvalue；
- Sylvester determinant lower bound；
- local radius；
- leakage budget；
- positive safety margin。

對**抽象 Green model** 而言，這些仍是合法工程量。

但若未來把 model 真正 canonicalize 到 actual Suzuki screw kernel / Weil operator，則 Section 11 告訴我們：

> 不能期待支撐尺度增加後仍維持一個固定的 absolute positive margin。

因此下面這類 proof target 太強：

$$
\exists\varepsilon>0:
M(R)\succeq\varepsilon I
\quad
\forall R.
$$

對 actual contacting screw-kernel family，它在 RH 真時反而不可能成立。

所以研究目標應改成：

$$
M(R)\succeq0
$$

配合：

- scale-adaptive interval precision；
- normalized reserve；
- relative conditioning；
- event-conditioned proof；
- zero-margin contact geometry。

這可能也解釋為什麼 AMRAL 第二弧線中單純擴大 local radius / absolute budget 很快遭遇證書惡化。

這裡是結構上的解釋，不表示 v1.0 的 abstract Green matrix 已證明就是 Suzuki matrix。

---

# 13. Canonical Checkpoint Gram Matrix

選任意 finite times：

$$
T
=
\{t_1,\ldots,t_m\}.
$$

定義：

$$
\boxed{
K_T
=
\left[
\Psi(t_i)
+
\Psi(t_j)
-
\Psi(t_i-t_j)
\right]_{i,j=1}^m.
}
$$

由 screw identity：

$$
K_T
=
\left[
G_g(t_i,t_j)
\right].
$$

在 RH 下：

$$
\boxed{
K_T\succeq0.
}
$$

其 diagonal：

$$
(K_T)_{ii}
=
2\Psi(t_i).
$$

因此這個 matrix 只需要 scalar $\Psi$ evaluator，即可建立完整有限 Green Gram matrix。

它提供一個 canonical AMRAL / Suzuki bridge matrix。

---

# 14. Finite negative-eigenvalue refutation channel

如果對某個 finite $T$ 可以嚴格證明：

$$
\lambda_{\min}(K_T)<0,
$$

則 screw kernel 不是 nonnegative definite。

由 Suzuki / Weil criterion：

$$
\boxed{
\lambda_{\min}(K_T)<0
\Longrightarrow
\neg RH.
}
$$

這是一條合法的 finite refutation certificate。

但反方向：

$$
K_T\succeq0
$$

對任意有限 $T$ 都只能證明該 finite set 的 positivity。

所以：

$$
\boxed{
\text{finite PSD}
\not\Longrightarrow
RH.
}
$$

除非另外完成 all-$T$ / RH-complete parameter reduction。

Mittermeier recovery witnesses 正是在 scalar checkpoint side 處理這個 remaining quantifier。

---

# 15. One-point extension 與 Schur reserve

假設已有 certified positive-definite anchor matrix：

$$
K_T\succ0.
$$

加入新 checkpoint $t$。

定義 cross vector：

$$
k_T(t)
=
\begin{pmatrix}
G_g(t_1,t)\\
\vdots\\
G_g(t_m,t)
\end{pmatrix}.
$$

以及 diagonal capacity：

$$
d(t)
=
G_g(t,t)
=
2\Psi(t).
$$

augmented matrix：

$$
K_{T\cup\{t\}}
=
\begin{pmatrix}
K_T & k_T(t)\\
k_T(t)^\ast & d(t)
\end{pmatrix}.
$$

Schur complement theorem 給：

$$
K_{T\cup\{t\}}\succeq0
$$

若且唯若：

$$
\boxed{
S_T(t)
:=
d(t)
-
k_T(t)^\ast
K_T^{-1}
k_T(t)
\ge0.
}
$$

定義：

$$
\boxed{
S_T(t)
=
\text{Recovery-Witness Schur Reserve}.
}
$$

這個量有 exact capacity–cost form：

$$
\boxed{
S_T(t)
=
C_T(t)-J_T(t),
}
$$

其中：

$$
C_T(t)
=
2\Psi(t),
$$

$$
J_T(t)
=
k_T(t)^\ast K_T^{-1}k_T(t)
\ge0.
$$

這是一個真正的 matrix-theoretic reserve identity。

---

# 16. 與 Mittermeier $\mathcal C_q-\mathcal J_q$ 的關係

Mittermeier Part 3–5 使用：

$$
\mathcal V_q
=
\mathcal C_q-\mathcal J_q
$$

表示 active-event / recovery-witness reserve。

本節點的 Schur reserve：

$$
S_T(t)
=
C_T(t)-J_T(t)
$$

具有同樣的「capacity minus cost」代數形態。

但目前：

$$
\boxed{
\mathcal C_q
\stackrel{?}{=}
C_T(t_q)
}
$$

與：

$$
\boxed{
\mathcal J_q
\stackrel{?}{=}
J_T(t_q)
}
$$

**尚未證明。**

所以本節點只登錄：

```text
SHARED_CAPACITY_COST_GEOMETRY = TRUE

EXACT_CJ_IDENTIFICATION = OPEN
```

若未來能找到一個 canonical anchor set / basis，使：

$$
\mathcal V_q
=
\alpha_q
S_T(t_q)
$$

對某個明確正 normalization：

$$
\alpha_q>0,
$$

那才是真正把 Mittermeier frontier 改寫成 Schur-complement positivity。

這是值得攻的新 GAP。

---

# 17. Schur reserve 比 diagonal checkpoint 更強

因為：

$$
J_T(t)\ge0,
$$

所以：

$$
\boxed{
S_T(t)\le2\Psi(t).
}
$$

因此：

$$
S_T(t)\ge0
\Longrightarrow
\Psi(t)\ge0.
$$

所以在一個 fixed finite anchor set 上，Schur reserve positivity 是比單一 diagonal checkpoint positivity 更強的條件。

反過來：

$$
\Psi(t)>0
$$

不保證：

$$
S_T(t)\ge0.
$$

因此 Schur reserve 可以作為：

- 更敏感的 finite refutation detector；
- matrix PSD extension certificate；
- AMRAL 與 checkpoint 之間的 joint validator。

但它不自動讓 RH proof 變容易。

---

# 18. Absolute Schur reserve 也不能有固定正 floor

若：

$$
K_T\succ0,
$$

且在 RH 下：

$$
S_T(t)\ge0,
$$

則：

$$
0
\le
S_T(t)
\le
2\Psi(t).
$$

沿：

$$
\Psi(t_n)\to0^+
$$

的 contact sequence：

$$
\boxed{
S_T(t_n)\to0
}
$$

只要同一 anchor family 的 extension 保持可定義與 PSD。

所以：

$$
\boxed{
\text{absolute Schur reserve 也不能被要求有 uniform positive floor}.
}
$$

這再次指出，下一步應該研究 dimensionless reserve。

---

# 19. Normalized Schur reserve

令：

$$
D_T
=
\operatorname{diag}(K_T).
$$

在 diagonal 全嚴格正時，定義 correlation-normalized matrix：

$$
\widehat K_T
=
D_T^{-1/2}
K_T
D_T^{-1/2}.
$$

這是正 congruence，所以：

$$
K_T\succeq0
\Longleftrightarrow
\widehat K_T\succeq0.
$$

對新 point $t$，若：

$$
d(t)>0,
$$

定義 normalized cross vector：

$$
r_T(t)
=
\frac{
D_T^{-1/2}k_T(t)
}{
\sqrt{d(t)}
}.
$$

則：

$$
\boxed{
\frac{S_T(t)}{d(t)}
=
1-
r_T(t)^\ast
\widehat K_T^{-1}
r_T(t).
}
$$

定義 dimensionless reserve ratio：

$$
\boxed{
\eta_T(t)
:=
\frac{S_T(t)}{2\Psi(t)}
=
1-
r_T(t)^\ast
\widehat K_T^{-1}
r_T(t).
}
$$

在 PSD extension 下：

$$
0\le\eta_T(t)\le1.
$$

這個 $\eta_T$ 不再直接承受：

$$
\Psi(t)\to0
$$

造成的 absolute scale collapse。

它因此比：

- raw smallest eigenvalue；
- raw determinant；
- raw positive margin；

更適合做 late-tail numerical conditioning 指標。

但目前沒有 theorem 保證：

$$
\eta_T(t)
$$

具有正的 uniform lower bound。

所以：

```text
NORMALIZATION_SOLVES_SCALE
!=
NORMALIZATION_SOLVES_RH
```

---

# 20. Recovery-witness block certificate architecture

下一版 AMRAL 可以把每個 recovery witness / constrained minimum point 做成：

```text
checkpoint_id
t_interval
Psi_interval

anchor_set
difference_intervals

K_anchor_interval
cross_vector_interval

schur_capacity_interval
schur_cost_interval
schur_reserve_interval
normalized_reserve_interval

local_workload_interval
service_clock_interval
recovery_drawdown_interval

prime_power_reference
source_hash
precision_bits
rounding_mode
```

輸出狀態：

```text
CHECKPOINT_DIAGONAL_POSITIVE
SCHUR_EXTENSION_POSITIVE
NEGATIVE_GREEN_WITNESS
INCONCLUSIVE
```

若：

```text
NEGATIVE_GREEN_WITNESS
```

必須經第二實作獨立重算。

任何 finite positive batch 都不得輸出：

```text
RH_PROVED
```

---

# 21. 新的 canonical bridge map

本輪後可以把研究圖寫成：

$$
\boxed{
\begin{array}{ccc}
\text{Weil quadratic cone}
&
\longrightarrow
&
\text{finite AMRAL Gram / PSD slices}
\\
\downarrow
&&
\downarrow
\\
Q_W(R_t)=\Psi(t)
&
\longrightarrow
&
G_g(t,t)=2\Psi(t)
\\
\downarrow
&&
\downarrow
\\
\text{prime-power checkpoints}
&
\longrightarrow
&
\text{recovery-witness reserves}
\end{array}
}
$$

其中：

- 上排：一般 test-function direction；
- 中排：RH-complete rectangular diagonal spine；
- 下排：對 $t$ 的 arithmetic event compression。

所以 AMRAL 與 Mittermeier 並不是兩個平行 proof attempts。

更準確地說：

> 它們是同一個 Weil positivity object 的不同 coordinate systems 與不同 quantifier compression。

---

# 22. 對後續研究策略的改寫

不再優先問：

> 如何把 abstract Green matrix 的 absolute PSD margin 撐得更大？

改問：

### Q1

能否把 AMRAL `$M_{\rm arith}$` 的 normalization 精確對齊：

$$
W(\psi_i\ast\widetilde{\psi_j})?
$$

### Q2

能否建立 canonical rectangular / interval-indicator basis，使 checkpoint：

$$
\Psi(t)
$$

成為 matrix 中可精確抽取的 Rayleigh / diagonal quantity？

### Q3

Mittermeier recovery reserve：

$$
\mathcal V_q
=
\mathcal C_q-\mathcal J_q
$$

是否可以對某個 natural anchor basis 表成：

$$
\alpha_q
S_T(t_q)?
$$

### Q4

若 exact equality 不成立，是否至少存在：

$$
\mathcal V_q
\ge
\alpha_q
S_T(t_q)
$$

或反向 domination？

### Q5

能否用 normalized Schur reserve：

$$
\eta_T(t)
$$

找到比 raw $\Psi(t)$ 更穩定的 all-event inequality？

這幾個問題比再建立一個新的 RH equivalent criterion 更直接。

---

# 23. GAP ledger

## CLOSED / REFERENCE-CLOSED

### G1. Checkpoint to Weil ray

```text
CLOSED
```

$$
\Psi(t)
=
Q_W(R_t).
$$

---

### G2. Checkpoint to Green diagonal

```text
CLOSED
```

$$
G_g(t,t)=2\Psi(t).
$$

---

### G3. Rectangular-ray RH completeness

```text
REFERENCE_CLOSED
```

Suzuki：

$$
RH
\Longleftrightarrow
\Psi(t)\ge0
\quad
\forall t.
$$

---

### G4. Uniform absolute spectral gap

```text
NO_GO_UNDER_RH
```

沿 near-contact sequence：

$$
\lambda_{\min}\to0.
$$

---

### G5. Schur reserve formula

```text
CLOSED_FINITE_DIMENSIONAL
```

$$
S_T(t)
=
2\Psi(t)
-
k^\ast K_T^{-1}k.
$$

---

## OPEN

### G6. Exact AMRAL $M_{\rm arith}$ normalization to Weil Gram matrix

```text
OPEN
```

---

### G7. Exact Mittermeier reserve to Schur reserve identification

```text
OPEN
```

$$
\mathcal V_q
\stackrel{?}{=}
\alpha_qS_T(t_q).
$$

---

### G8. Relative reserve theorem

```text
OPEN
```

是否可對：

$$
\eta_T(t)
$$

建立 recovery-conditioned lower bound？

---

### G9. Actual all-event tail

```text
OPEN
```

Mittermeier current frontier：

$$
\mathcal J_q\le\mathcal C_q
$$

at every recovery witness。

---

### G10. RH

```text
OPEN
```

---

# 24. 下一節點

建議：

`RH-RecoveryWitness-SchurBridge-v1.5`

不要先做更大的理論。

直接做 exact normalization audit：

1. 從 AMRAL `M_arith` 原始公式抽取：

$$
M_{ij}
=
M_{\infty,ij}
+
M_{{\rm fin},ij}.
$$

2. 對齊 Suzuki / Weil：

$$
W(\psi_i\ast\widetilde{\psi_j}).
$$

3. 建立 interval-indicator / rectangular canonical basis。

4. 驗證：

$$
Q_W(R_t)=\Psi(t)
$$

在程式層的 normalization 完全一致。

5. 建立 finite：

$$
K_T
$$

與：

$$
S_T(t).
$$

6. 在已嚴格 verified finite range 做雙軌 comparison：

```text
scalar checkpoint reserve
vs.
matrix Schur reserve
```

7. 再嘗試對照 Mittermeier：

$$
\mathcal V_q,\mathcal C_q,\mathcal J_q.
$$

只有當 symbolic identity 真成立時，才升格成：

```text
EXACT_FRONTIER_IDENTIFICATION
```

否則維持：

```text
STRUCTURAL_BRIDGE_ONLY
```

---

# 25. Trust boundary

必須保留：

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE

SUZUKI_CHECKPOINT_BRIDGE = EXACT
GREEN_DIAGONAL_BRIDGE = EXACT

MITTERMEIER_CJ_TO_SCHUR_EQUALITY = NOT_PROVED
AMRAL_M_ARITH_TO_SUZUKI_MATRIX_EQUALITY = NOT_PROVED

UNIFORM_POSITIVE_MARGIN_STRATEGY = REJECTED_FOR_ACTUAL_CONTACTING_KERNEL
GLOBAL_RH_CERTIFICATE = FALSE
```

禁止：

$$
\text{same capacity-cost form}
\Longrightarrow
\text{same mathematical quantity}.
$$

禁止：

$$
\text{finite Schur-positive batch}
\Longrightarrow
RH.
$$

禁止：

$$
\text{abstract AMRAL Green no-gap behavior}
=
\text{actual zeta screw-kernel no-gap theorem}
$$

除非 canonical identification 已完成。

---

# 26. 一句話狀態

> v1.4 首次把 AMRAL Weil/PSD、Suzuki screw Green kernel 與 Mittermeier recovery checkpoints 放進同一個 canonical positivity picture：$\Psi(t)=Q_W(R_t)=\frac12G_g(t,t)$，所以 checkpoint 是 Weil positive cone 的 RH-complete rectangular diagonal spine，而 recovery workload 是這條 spine 上的能量導數。最新 tail 結果又顯示在 RH 下 $\liminf\Psi(t)=0$，因此 actual screw-kernel matrix 不可能擁有支撐無關的固定正 spectral gap，AMRAL 應從 absolute margin 轉向 normalized / event-conditioned reserve。本節點進一步定義 Schur reserve $S_T(t)=2\Psi(t)-k^\ast K_T^{-1}k$，得到一個與 recovery-witness `capacity − cost` 同型的精確有限維 bridge；但尚未宣稱它等於 Mittermeier 的 $\mathcal C_q-\mathcal J_q$。下一步是 exact normalization audit，而不是再造新的 RH equivalent criterion。

---

# 27. References

1. Masatoshi Suzuki, **Aspects of the screw function corresponding to the Riemann zeta-function**, *Journal of the London Mathematical Society* 108 (2023), 1448–1487.  
   DOI: https://doi.org/10.1112/jlms.12785  
   arXiv: https://arxiv.org/abs/2206.03682

2. Masatoshi Suzuki, **Weil's quadratic form via the screw function**, arXiv:2606.09096, 2026.  
   https://arxiv.org/abs/2606.09096

3. Rainer Andreas Mittermeier, **Recovery Witnesses in the Prime-Power Checkpoint Program: Service-Clock Geometry and an Exact Quantifier Reduction for the Riemann-Hypothesis Tail -- Part 4**, 2026.  
   https://zenodo.org/records/22076079

4. Rainer Andreas Mittermeier, **Deep Episodes in the Prime-Power Checkpoint Program: An Unconditional Terminal-Episode Theorem, an Exact Chebyshev Bridge, and Sharp Recovery Recurrence -- Part 5**, 2026.  
   https://zenodo.org/records/22076088

5. AMRAL, **算術矩陣與半正定證書原型 · v0.1**.  
   https://amral.evemisslab.com/riemann/autonomous/p/proto-arithmetic-matrix-psd-v0.1/

6. AMRAL, **RH-W-03 · 緊支撐分離與雙核心架構**.  
   https://amral.evemisslab.com/riemann/autonomous/p/w03-v0.1/

7. AMRAL, **嚴格交集證書 · v0.2**.  
   https://amral.evemisslab.com/riemann/semi-autonomous/p/proto-validated-intersection-certificate-v0.2/

8. AMRAL, **零點側洩漏預算 · v0.1**.  
   https://amral.evemisslab.com/riemann/semi-autonomous/p/proto-zero-side-leakage-budget-v0.1/

9. AMRAL, **等變算術障礙整合總論 · v1.0**.  
   https://amral.evemisslab.com/riemann/semi-autonomous/p/proto-equivariant-arithmetic-obstruction-integration-v1.0/

10. AMRAL, **局部區間 Green 位置覆蓋 · v1.0**.  
    https://amral.evemisslab.com/riemann/semi-autonomous/p/proto-localintervalgreen-cellcover-v1.0/

---

# 28. Provenance

研究主導：Neo.K

v1.4 數學續推、Suzuki / Mittermeier frontier 對齊與 canonical source 整理：ChatGPT / GPT-5.6 Sol

日期：2026-09-02

研究定位：AMRAL 黎曼猜想半自主研究線，第三弧線 exact Weil–checkpoint–Green bridge 節點。

本文件是 research source artifact，不是 peer-reviewed publication。

所有 claim 必須依 Claim register、GAP ledger 與 Trust boundary 解讀。
