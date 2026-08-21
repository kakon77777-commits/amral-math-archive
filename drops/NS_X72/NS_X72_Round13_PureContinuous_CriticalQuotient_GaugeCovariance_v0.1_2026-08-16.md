# NS × X 積分 × 24/72 範式實戰
## Round 13 — Pure Continuous Critical Quotient Geometry / Gauge-Covariance Route

- 日期：2026-08-16
- 版本：v0.1
- 狀態：Proof-Route Experiment / Continuous-Only Quotient-Dual Branch
- canonical source：UTF-8 Markdown
- canonical math delimiters：inline `$...$`；display `$$...$$`
- 前一輪：`NS_X72_Round12_PureContinuous_CriticalDual_CancellationTradeoff_v0.1_2026-08-16.md`
- 本輪目標：修正 Round 12 對 $L^{3/2}$ critical dual 的 representation。真正 dual object 是 solenoidal $L^3$ 的 quotient dual，即 $L^{3/2}$ modulo gradient fields。檢驗 projected entropy gradient 是否可積回 scalar functional，並判定 quotient geometry 是否能消除 Leray defect。
- 非主張：本文的 quotient minimizer推導在 standard whole-space Helmholtz decomposition 與足夠 smooth/minimizer regularity下書寫；一般 Banach-space版本可用 closed gradient subspace與 subdifferential formulation處理。

---

# 0. Round 12 handoff

Round 12 測試兩個自然 critical dual representatives：

$$
L^{3/2}
$$

與：

$$
\dot H^{-1/2}.
$$

得到：

$$
\boxed{
\begin{array}{c|cc}
&\text{Transport cancellation}&\text{Leray compatibility}
\\
\hline
L^2&\checkmark&\checkmark
\\
L^{3/2}&\checkmark&\times
\\
\dot H^{-1/2}&\times&\checkmark
\end{array}
}
\tag{0.1}
$$

其中 $L^{3/2}$ representative 的 defect：

$$
\mathfrak P_{3/2}
=
\left\langle
T_U\psi,
(P-I)J_{3/2}(\psi)
\right\rangle.
$$

Round 12 下一問：

$$
\boxed{
P J_{3/2}(\psi)
\text{ 是否真的是某 scalar functional 的 gradient？}
}
$$

本輪第一個結果：

$$
\boxed{
\textbf{是。}
}
$$

但這不是 closure。

它揭露出更深的 quotient/gauge defect。

---

# 1. The exact critical dual is a quotient space

令：

$$
L^3_\sigma
=
\left\{
u\in L^3(\mathbb R^3;\mathbb R^3):
\nabla\cdot u=0
\right\}.
$$

設：

$$
\mathcal G_p
=
\overline{
\{
\nabla q:
q\in C_c^\infty(\mathbb R^3)
\}
}^{L^p}.
$$

在 standard whole-space Helmholtz decomposition中：

$$
L^p
=
L^p_\sigma
\oplus
\mathcal G_p,
\qquad
1<p<\infty.
$$

因此：

$$
\boxed{
(L^3_\sigma)^\ast
\simeq
L^{3/2}/\mathcal G_{3/2}.
}
\tag{1.1}
$$

所以真正 critical dual state不是單一 divergence-free representative：

$$
\psi,
$$

而是 equivalence class：

$$
\boxed{
[\psi]
=
\psi+\mathcal G_{3/2}.
}
\tag{1.2}
$$

---

# 2. Quotient norm

對：

$$
1<p<\infty,
$$

定義：

$$
\boxed{
\|[f]\|_{Q_p}
=
\inf_{g\in\mathcal G_p}
\|f+g\|_{L^p}.
}
\tag{2.1}
$$

對：

$$
p=\frac32,
$$

此 norm具有 dual critical scaling。

如果：

$$
\psi=P f
$$

是 canonical solenoidal representative，則：

$$
[f]=[\psi].
$$

而：

$$
\|[f]\|_{Q_p}
\le
\|\psi\|_p.
$$

另一方面，因 Helmholtz projector：

$$
P:L^p\to L^p_\sigma
$$

bounded，

對任意：

$$
v\in[f],
$$

$$
\psi=Pv.
$$

故：

$$
\|\psi\|_p
\le
C_p
\|v\|_p.
$$

取 inf：

$$
\boxed{
\|[f]\|_{Q_p}
\le
\|Pf\|_p
\le
C_p
\|[f]\|_{Q_p}.
}
\tag{2.2}
$$

所以 quotient norm不是一個失去 critical information 的弱化 norm。

它與 canonical solenoidal representative norm等價。

---

# 3. Exact dual norm detection

對：

$$
u\in L^3_\sigma,
$$

gradient fields annihilate pairing：

$$
\langle
\nabla q,u
\rangle
=
0.
$$

因此 pairing只依賴 quotient class：

$$
\langle
[f],u
\rangle
:=
\langle
f,u
\rangle.
$$

Banach duality給：

$$
\boxed{
\|u\|_{L^3}
=
\sup_{
\|[f]\|_{Q_{3/2}}\le1
}
|\langle
[f],u
\rangle|.
}
\tag{3.1}
$$

所以：

$$
\boxed{
Q_{3/2}
=
L^{3/2}/\mathcal G_{3/2}
}
$$

才是與 primal $L^3_\sigma$ 完全對齊的 critical dual geometry。

---

# 4. Unique minimum representative

因：

$$
1<p<\infty,
$$

$L^p$ reflexive且 strictly/uniformly convex。

對 closed affine class：

$$
[f]
$$

存在唯一 minimum-norm representative：

$$
\boxed{
v_\ast
=
f+g_\ast,
\qquad
g_\ast\in\mathcal G_p,
}
\tag{4.1}
$$

使：

$$
\boxed{
\|v_\ast\|_p
=
\|[f]\|_{Q_p}.
}
\tag{4.2}
$$

在 smooth gradient representation下寫：

$$
\boxed{
v_\ast
=
\psi+\nabla q_\ast,
}
\tag{4.3}
$$

其中：

$$
P\psi=\psi.
$$

---

# 5. Nonlinear entropy gauge condition

minimum representative等價於最小化：

$$
\mathcal E_p(v)
=
\frac1p
\int
|v|^pdx
$$

於 class：

$$
v=\psi+\nabla q.
$$

對：

$$
q\mapsto q+\varepsilon h
$$

變分：

$$
0
=
\left.
\frac d{d\varepsilon}
\right|_{\varepsilon=0}
\mathcal E_p
(
v_\ast+\varepsilon\nabla h
).
$$

令：

$$
J_p(v)
=
|v|^{p-2}v.
$$

則：

$$
0
=
\int
J_p(v_\ast)\cdot\nabla hdx
=
-
\int
\operatorname{div}
J_p(v_\ast)
h\,dx.
$$

所以：

$$
\boxed{
\operatorname{div}
J_p(v_\ast)
=
0.
}
\tag{5.1}
$$

對 critical：

$$
p=\frac32,
$$

得到 nonlinear gauge：

$$
\boxed{
\operatorname{div}
\left(
|v_\ast|^{-1/2}v_\ast
\right)
=
0.
}
\tag{5.2}
$$

這是本輪第一個新 carrier。

---

# 6. Projected entropy gradient is integrable

Round 12 的 candidate：

$$
P J_p(\psi)
$$

看起來可能不是 scalar functional gradient。

但在 divergence-free subspace：

$$
H_\sigma
$$

上考慮 ordinary entropy：

$$
\mathcal E_p[\psi]
=
\frac1p
\int
|\psi|^pdx.
$$

對任意 divergence-free tangent：

$$
h,
$$

有：

$$
D\mathcal E_p[\psi](h)
=
\langle
J_p(\psi),h
\rangle.
$$

又因：

$$
Ph=h,
$$

$$
\langle
J_p,h
\rangle
=
\langle
P J_p,h
\rangle.
$$

因此 constrained $L^2$ gradient正是：

$$
\boxed{
\nabla_{\sigma,L^2}
\mathcal E_p
=
P J_p(\psi).
}
\tag{6.1}
$$

所以：

$$
\boxed{
\textbf{
there is no variational integrability obstruction here.
}
}
\tag{6.2}
$$

Round 12 的下一刀被合法繞過。

---

# 7. The projected entropy defect is intrinsic

雖然：

$$
P J_p
$$

真的是 constrained gradient，

critical entropy derivative仍然是：

$$
\frac1p
\frac d{d\sigma}
\|\psi\|_p^p
+
\nu
\mathfrak D_p(\psi)
=
\langle
P T_U\psi,
P J_p(\psi)
\rangle.
$$

所以 defect不是：

> $PJ_p$ 不是 gradient。

而是：

$$
\boxed{
\text{projected transport vector field is not tangent to entropy level sets}.
}
$$

也就是 integrability修復之後，coercivity問題仍在。

---

# 8. Quotient evolution

Round 12 backward-time dual equation：

$$
\partial_\sigma\psi
=
\nu\Delta\psi
+
P T_U\psi.
$$

在 quotient中：

$$
[P T_U\psi]
=
[T_U\psi].
$$

又若：

$$
v_\ast
=
\psi+\nabla q_\ast,
$$

則：

$$
[\Delta v_\ast]
=
[\Delta\psi].
$$

所以 quotient class evolution可用 representative：

$$
\boxed{
\nu\Delta v_\ast
+
T_U\psi
}
\tag{8.1}
$$

表示。

由 minimum-envelope / stationarity condition，

$q_\ast$ 隨時間的 gauge derivative不直接貢獻一階 norm variation，因：

$$
\operatorname{div}J_p(v_\ast)=0.
$$

因此：

$$
\boxed{
\frac1p
\frac d{d\sigma}
\|[\psi]\|_{Q_p}^p
+
\nu
\mathfrak D_p(v_\ast)
=
\langle
J_p(v_\ast),
T_U\psi
\rangle.
}
\tag{8.2}
$$

---

# 9. Gauge noncovariance identity

因：

$$
\psi
=
v_\ast-\nabla q_\ast,
$$

有：

$$
T_U\psi
=
T_Uv_\ast
-
T_U\nabla q_\ast.
$$

raw transport entropy cancellation：

$$
\langle
J_p(v_\ast),
T_Uv_\ast
\rangle
=
0.
$$

而：

$$
\boxed{
T_U\nabla q
=
\nabla(T_Uq)
-
(\nabla U)^\top\nabla q.
}
\tag{9.1}
$$

因：

$$
\operatorname{div}J_p(v_\ast)=0,
$$

gradient part消失。

所以：

$$
\boxed{
\langle
J_p(v_\ast),
T_U\psi
\rangle
=
\left\langle
J_p(v_\ast),
(\nabla U)^\top
\nabla q_\ast
\right\rangle.
}
\tag{9.2}
$$

因此 exact quotient entropy law：

$$
\boxed{
\frac1p
\frac d{d\sigma}
\|[\psi]\|_{Q_p}^p
+
\nu
\mathfrak D_p(v_\ast)
=
\mathfrak G_p[U,\psi],
}
\tag{9.3}
$$

其中：

$$
\boxed{
\mathfrak G_p
=
\int
J_p(v_\ast)\cdot
(\nabla U)^\top
\nabla q_\ast
\,dx.
}
\tag{9.4}
$$

命名：

$$
\boxed{
\textbf{Gauge-Deformation Defect}.
}
$$

---

# 10. Defect transmutation

Round 12 canonical representative看到：

$$
\boxed{
\mathfrak P_p
=
\text{Leray projection defect}.
}
$$

Round 13 exact quotient geometry把顯式 projection defect消掉，

但得到：

$$
\boxed{
\mathfrak G_p
=
\text{gauge-deformation / velocity-gradient defect}.
}
$$

因此：

$$
\boxed{
\textbf{
quotient geometry removes the representation-level Leray defect,
but does not remove the physical transport–constraint mismatch.
}
}
\tag{10.1}
$$

它只把 obstruction轉寫得更 intrinsic。

---

# 11. Why componentwise transport fails on gradient classes

對兩個同 quotient class 的 representatives：

$$
v
$$

與：

$$
v+\nabla q,
$$

componentwise transport difference：

$$
T_U(v+\nabla q)-T_Uv
=
T_U\nabla q.
$$

由 (9.1)：

$$
T_U\nabla q
=
\nabla(T_Uq)
-
(\nabla U)^\top\nabla q.
$$

第二項一般不是 gradient。

因此：

$$
\boxed{
[T_U(v+\nabla q)]
\neq
[T_Uv]
}
\tag{11.1}
$$

一般成立。

所以：

$$
\boxed{
\textbf{
componentwise transport does not descend naturally
to the quotient by gradient fields.
}
}
\tag{11.2}
$$

這就是 $\mathfrak G_p$ 的幾何來源。

---

# 12. Lie derivative repairs gauge covariance

把 vector field視為 Euclidean 1-form。

定義 1-form Lie transport：

$$
\boxed{
\mathcal L_U^{(1)}v
=
T_Uv
+
(\nabla U)^\top v.
}
\tag{12.1}
$$

則對 exact 1-form：

$$
\nabla q,
$$

有：

$$
\boxed{
\mathcal L_U^{(1)}
(\nabla q)
=
\nabla(T_Uq).
}
\tag{12.2}
$$

因此：

$$
\boxed{
\mathcal L_U^{(1)}
}
$$

真正 preservation gradient gauge classes。

所以若只看 quotient geometry，

Lie derivative才是自然 transport operator。

---

# 13. But Lie transport loses local entropy conservation

對：

$$
v,
$$

有：

$$
\langle
J_p(v),
T_Uv
\rangle
=
0.
$$

但：

$$
\boxed{
\langle
J_p(v),
\mathcal L_U^{(1)}v
\rangle
=
\int
|v|^{p-2}
v\cdot
(\nabla U)^\top v
\,dx.
}
\tag{13.1}
$$

因同一向量出現在兩側，

antisymmetric rotation part消失。

令：

$$
S_U
=
\frac12
\left(
\nabla U+\nabla U^\top
\right).
$$

則：

$$
\boxed{
\langle
J_p(v),
\mathcal L_U^{(1)}v
\rangle
=
\int
|v|^{p-2}
v^\top
S_U
v
\,dx.
}
\tag{13.2}
$$

所以：

$$
\boxed{
\text{Lie transport preserves gradient gauge
but introduces strain stretching}.
}
$$

---

# 14. Transport–Gauge Covariance Tradeoff

現在出現另一個 cancellation square。

## Componentwise transport

$$
T_U
=
U\cdot\nabla.
$$

它保留：

$$
\boxed{
L^p\text{ entropy chain-rule cancellation}
}
$$

但失去：

$$
\boxed{
\text{gradient-gauge covariance}.
}
$$

## One-form Lie transport

$$
\mathcal L_U^{(1)}
=
T_U
+
(\nabla U)^\top.
$$

它保留：

$$
\boxed{
\text{gradient-gauge covariance}
}
$$

但失去：

$$
\boxed{
L^p\text{ entropy conservation}
}
$$

因 strain stretching。

所以：

$$
\boxed{
\textbf{Transport–Gauge Covariance Tradeoff}.
}
\tag{14.1}
$$

---

# 15. Why $p=2$ is again special

若：

$$
p=2,
$$

quotient minimum representative of a divergence-free：

$$
\psi
$$

就是：

$$
v_\ast=\psi
$$

因 standard Helmholtz decomposition在 $L^2$ orthogonal。

所以：

$$
q_\ast=0.
$$

因此：

$$
\boxed{
\mathfrak G_2=0.
}
$$

這重新恢復：

$$
L^2
$$

exact dual contraction。

對：

$$
p\neq2,
$$

metric projection onto gradient classes不是 linear orthogonal projection，

且：

$$
q_\ast
$$

一般非零。

所以 critical：

$$
p=\frac32
$$

再次失去 $L^2$ 特殊幾何。

---

# 16. The exact critical quotient law

令：

$$
p=\frac32.
$$

定義：

$$
N_Q
=
\|[\psi]\|_{Q_{3/2}}
=
\|v_\ast\|_{3/2}.
$$

則：

$$
J_{3/2}(v_\ast)
=
|v_\ast|^{-1/2}v_\ast.
$$

nonlinear gauge：

$$
\boxed{
\operatorname{div}
\left(
|v_\ast|^{-1/2}v_\ast
\right)
=
0.
}
\tag{16.1}
$$

exact evolution：

$$
\boxed{
\frac23
\frac d{d\sigma}
N_Q^{3/2}
+
\nu
\mathfrak D_{3/2}(v_\ast)
=
\int
|v_\ast|^{-1/2}
v_\ast
\cdot
(\nabla U)^\top
\nabla q_\ast
\,dx.
}
\tag{16.2}
$$

這是目前最精確的 $L^3$ critical dual quotient balance。

---

# 17. Gauge-stress tensor

定義：

$$
\boxed{
\mathbb K_p
=
\nabla q_\ast
\otimes
J_p(v_\ast).
}
\tag{17.1}
$$

則：

$$
\boxed{
\mathfrak G_p
=
\int
\nabla U:
\mathbb K_p
\,dx
}
\tag{17.2}
$$

依採用的 matrix-index convention作對應 transpose。

將：

$$
\mathbb K_p
$$

分成 symmetric / antisymmetric：

$$
\mathbb K_p
=
\mathbb K_p^{\rm sym}
+
\mathbb K_p^{\rm skew}.
$$

則：

$$
\boxed{
\mathfrak G_p
=
\int
S_U:
\mathbb K_p^{\rm sym}
+
\Omega_U:
\mathbb K_p^{\rm skew}
\,dx.
}
\tag{17.3}
$$

所以 quotient defect是一個真正 relational carrier：

$$
\boxed{
\text{velocity-gradient geometry}
\times
\text{optimal-gauge stress}.
}
$$

---

# 18. Crude control returns to Lipschitz/BKM-type information

由 Hölder：

$$
|\mathfrak G_p|
\le
\|\nabla U\|_\infty
\|J_p(v_\ast)\|_{p'}
\|\nabla q_\ast\|_p.
$$

而：

$$
\|J_p(v_\ast)\|_{p'}
=
\|v_\ast\|_p^{p-1}.
$$

又：

$$
\psi=Pv_\ast,
$$

所以：

$$
\|\psi\|_p
\le
C_p\|v_\ast\|_p.
$$

且：

$$
\nabla q_\ast
=
v_\ast-\psi.
$$

故：

$$
\|\nabla q_\ast\|_p
\le
(1+C_p)
\|v_\ast\|_p.
$$

因此：

$$
\boxed{
|\mathfrak G_p|
\le
C_p^\ast
\|\nabla U\|_\infty
\|[\,\psi\,]\|_{Q_p}^p.
}
\tag{18.1}
$$

對：

$$
p=\frac32,
$$

這給：

$$
\boxed{
\frac d{d\sigma}
N_Q^{3/2}
\lesssim
\|\nabla U\|_\infty
N_Q^{3/2}.
}
\tag{18.2}
$$

所以如果：

$$
\int
\|\nabla U\|_\infty
d\sigma
<\infty,
$$

critical quotient norm可 Gronwall 控制。

但這只是把問題送回 Lipschitz/BKM-type continuation information。

它不是 energy-level unconditional closure。

---

# 19. A restricted local correction no-go

考慮 affine incompressible drift：

$$
U(x)=Ax,
$$

其中：

$$
\operatorname{tr}A=0.
$$

試圖修改 component transport：

$$
D_Uv
=
T_Uv
+
Bv
$$

其中：

$$
B
$$

為 constant matrix depending on $A$。

要求兩件事同時成立。

## G1. Gradient covariance

對所有 smooth scalar：

$$
q,
$$

$$
D_U(\nabla q)
$$

仍為 gradient。

因：

$$
T_U\nabla q
=
\nabla(T_Uq)-A^\top\nabla q,
$$

這要求：

$$
(B-A^\top)\nabla q
$$

對所有 $q$ 都是 gradient。

一個 constant matrix：

$$
M
$$

若對所有 $q$ 都使：

$$
M\nabla q
$$

為 gradient，

則：

$$
M
$$

必為 scalar multiple of identity：

$$
M=cI.
$$

所以：

$$
\boxed{
B
=
A^\top+cI.
}
\tag{19.1}
$$

## G2. Universal isotropic entropy neutrality

要求對所有 vectors：

$$
v
$$

都有：

$$
v^\top Bv=0.
$$

這迫使：

$$
\operatorname{sym}B=0.
$$

由：

$$
B=A^\top+cI
$$

及：

$$
\operatorname{tr}A=0,
$$

取 trace得：

$$
c=0.
$$

因此：

$$
\operatorname{sym}A=0.
$$

也就是：

$$
\boxed{
A
\text{ 必須是純 rigid rotation}.
}
\tag{19.2}
$$

所以只要 drift具有非零 strain，

不存在這種 constant zeroth-order matrix correction同時 universally 保持：

- gradient gauge covariance；
- isotropic entropy neutrality。

命名：

$$
\boxed{
\textbf{Affine Gauge–Entropy No-Go}.
}
$$

這是 restricted local no-go，不排除 nonlocal/dynamic corrections。

---

# 20. What the quotient route repaired and what it did not

成功修復：

$$
\boxed{
\text{ordinary divergence-free }L^{3/2}
\text{ representative is not the exact dual geometry}.
}
$$

更精確的 dual：

$$
\boxed{
Q_{3/2}
=
L^{3/2}/\mathcal G_{3/2}.
}
$$

它：

- critical；
- lossless for $L^3_\sigma$ duality；
- 有 unique minimal representative；
- 產生 nonlinear divergence-free entropy gauge；
- 使 $P J_{3/2}$ 的 variational integrability不再是問題。

但沒有修復：

$$
\boxed{
\text{transport–constraint compatibility}.
}
$$

obstruction被壓成：

$$
\boxed{
\mathfrak G_{3/2}
=
\text{gauge stress}
\times
\nabla U.
}
$$

---

# 21. STOP-C17 — Critical Quotient Gauge-Covariance / Stretching Gap

定義：

$$
\boxed{
\bot_X^{\mathrm{C17}}
=
\left\langle
\begin{array}{l}
\text{layer}
=
\mathrm{exact\ }L^3\mathrm{\ critical\ dual\ quotient},
\\
\text{dual}
=
L^{3/2}/\mathcal G_{3/2},
\\
\text{minimal\ representative}
=
v_\ast,
\\
\text{entropy\ gauge}
=
\operatorname{div}(|v_\ast|^{-1/2}v_\ast)=0,
\\
\text{projected-gradient\ integrability}
=
\mathrm{true},
\\
\text{explicit\ Leray\ defect}
=
\mathrm{removed},
\\
\text{remaining\ defect}
=
\mathfrak G_{3/2},
\\
\text{geometric\ source}
=
T_U\nabla q
-
\nabla(T_Uq)
=
-(\nabla U)^\top\nabla q,
\\
\text{Lie\ derivative}
=
\mathrm{gauge\ covariant\ but\ stretching},
\\
\text{missing}
=
\mathrm{critical\ control\ of\ gauge\text{-}stretching\ coupling},
\\
\text{discrete\ intrusion}
=
\mathrm{false}.
\end{array}
\right\rangle.
}
$$

命名：

$$
\boxed{
\textbf{STOP-C17:
Critical Quotient Gauge-Covariance / Stretching Gap}.
}
$$

---

# 22. 24/72 Ledger — Round 13

| Step | X object / operation | $B$ | $U$ | $O$ | $L$ | status |
|---|---|---|---|---|---|---|
| C136 | quotient dual $Q_{3/2}$ | $\mathsf C$ | quotient/global | $\mathsf X$ | $\mathsf F$ | FORM |
| C137 | quotient–solenoidal norm equivalence | $\mathsf C$ | retrieval | targeted | $\mathsf F$ | PROVED under Helmholtz setting |
| C138 | minimum representative $v_\ast$ | $\mathsf C$ | variational | relational | $\mathsf F$ | FORM |
| C139 | nonlinear entropy gauge | $\mathsf C$ | variational | targeted relation | $\mathsf F$ | EXACT |
| C140 | $PJ_p$ integrability | $\mathsf C$ | constrained variational | gradient | $\mathsf F$ | PROVED |
| C141 | quotient entropy law | $\mathsf C$ | quotient evolution | scalar + relation | $\mathsf F$ | EXACT |
| C142 | gauge noncovariance identity | $\mathsf C$ | transport | relational | $\mathsf F$ | EXACT |
| C143 | Lie derivative gauge repair | $\mathsf C$ | geometric transport | quotient | $\mathsf F$ | EXACT |
| C144 | Lie-transport entropy stretching | $\mathsf C$ | geometric transport | scalar | $\mathsf F$ | EXACT |
| C145 | gauge-stress tensor $\mathbb K_p$ | $\mathsf C$ | relational | $\mathsf X$ | $\mathsf F$ | FORM |
| C146 | Lipschitz control of defect | $\mathsf C$ | estimate | scalar | $\mathsf F$ | CONDITIONAL |
| C147 | affine local gauge–entropy repair | $\mathsf C$ | local correction | relational | $\mathsf F$ | NO-GO except rigid rotation |
| C148 | unconditional critical gauge-stretching control | $\mathsf C$ | — | targeted | $\mathsf F$ | OPEN / STOP-C17 |

---

# 23. Continuous-versus-discrete status

本輪 quotient：

$$
L^{3/2}/\mathcal G_{3/2}
$$

是 infinite-dimensional continuous Banach geometry。

minimum representative由 continuous convex variational problem形成。

nonlinear gauge：

$$
\operatorname{div}
(
|v|^{-1/2}v
)=0
$$

亦為 continuous PDE condition。

沒有引入：

- atoms；
- dyadic blocks；
- wavelet packets；
- sequence extraction；
- countable basis closure。

所以：

$$
\boxed{
T_{\mathsf C\to\mathsf D}
=
\text{NOT YET REACHED}.
}
\tag{23.1}
$$

---

# 24. New structural interpretation

Round 12 看起來是：

$$
\boxed{
\text{Leray projection ruins critical entropy}.
}
$$

Round 13 修正為：

$$
\boxed{
\textbf{
the deeper obstruction is that componentwise transport
does not preserve the gradient gauge underlying the exact critical dual quotient.
}
}
\tag{24.1}
$$

如果改成 gauge-covariant one-form Lie transport，

gradient quotient自然閉合，

但 strain stretching重新出現。

所以問題已從：

$$
\text{projection}
$$

推進為：

$$
\boxed{
\text{gauge covariance}
\leftrightarrow
\text{stretching}.
}
$$

---

# 25. An unexpected primal bridge

對 velocity one-form，

使用 identity：

$$
\mathcal L_u^{(1)}u
=
(u\cdot\nabla)u
+
\nabla
\left(
\frac12|u|^2
\right).
$$

Navier–Stokes可寫成：

$$
\boxed{
\partial_tu
+
\mathcal L_u^{(1)}u
=
\nu\Delta u
-
\nabla
\left(
p-\frac12|u|^2
\right).
}
\tag{25.1}
$$

因此 modulo gradients：

$$
\boxed{
\partial_t[u]
+
[\mathcal L_u^{(1)}u]
=
\nu[\Delta u].
}
\tag{25.2}
$$

而：

$$
\mathcal L_u^{(1)}
$$

正好是 preservation gradient quotient 的自然 transport。

所以 critical quotient geometry不只是一個 dual trick。

它其實接到 Navier–Stokes velocity 1-form本身的 geometric formulation。

這提供下一輪新路線。

---

# 26. Next round — critical one-form / circulation quotient

下一輪改測 primal critical quotient：

$$
\boxed{
\mathfrak Q_3[u]
=
\inf_q
\|u+\nabla q\|_{L^3}.
}
$$

由 Helmholtz boundedness：

$$
\mathfrak Q_3[u]
$$

與：

$$
\|u\|_3
$$

對 divergence-free $u$ 等價，

所以它仍是真正的 $L^3$ critical continuation carrier。

但它有一個 Round 13 dual route沒有的優勢：

$$
\boxed{
\text{NS modulo gradients本身就是 Lie-transport equation}.
}
$$

下一輪問題：

1. quotient-minimal velocity 1-form：

$$
v_\ast=u+\nabla q_\ast
$$

滿足什麼 nonlinear gauge；

2. Lie transport在 quotient中是否使 pressure完全消失；

3. critical quotient norm evolution是否只剩 strain-stretching term；

4. 該 stretching是否可與 Round 03 的 $\lambda_2$ / Round 05 的 gradient-alignment carriers接合；

5. 是否出現新的 circulation / Kelvin-type invariant；

6. 若仍不能閉合，再測 differential-form hierarchy，而非提前離散化。

---

# 27. External primary-source anchors

1. Tuoc Phan, *Well-posedness for the Navier-Stokes equations in critical mixed-norm Lebesgue spaces*, arXiv:1903.08319.
   - critical Lebesgue-space NS framework；
   - Helmholtz–Leray projection boundedness與 Riesz-transform machinery。

2. Pascal Hobus, Jürgen Saal, *Stokes and Navier-Stokes equations subject to partial slip on uniform $C^{2,1}$-domains in $L_q$-spaces*, arXiv:2003.05801.
   - $L_q$ Helmholtz decomposition作為 Stokes/Navier–Stokes functional framework的重要性；
   - 本輪 whole-space quotient使用的是標準 Helmholtz情形。

3. Standard Cartan/Lie-derivative identity for exact one-forms:
   $$
   \mathcal L_U(dq)=d(Uq).
   $$
   本輪所有 gauge-covariance、quotient evolution、entropy-gauge與 affine no-go formulas均為本文直接推導。

---

# 28. Commit state

$$
\boxed{
\begin{aligned}
\text{Route}
&:
\mathrm{Pure\ Continuous\ Critical\ Quotient\ Geometry},
\\
\text{Essential }\mathsf C\to\mathsf D
&:
\mathrm{Not\ reached},
\\
\text{Exact critical dual}
&:
L^{3/2}/\mathcal G_{3/2},
\\
\text{Projected entropy gradient}
&:
\mathrm{integrable},
\\
\text{Minimum representative}
&:
v_\ast,
\\
\text{Nonlinear gauge}
&:
\operatorname{div}(|v_\ast|^{-1/2}v_\ast)=0,
\\
\text{Round12 Leray defect}
&:
\mathrm{transmuted},
\\
\text{New exact defect}
&:
\mathfrak G_{3/2},
\\
\text{Underlying obstruction}
&:
\mathrm{transport\ gauge\ noncovariance},
\\
\text{Gauge-covariant repair}
&:
\mathrm{one\text{-}form\ Lie\ transport},
\\
\text{Repair cost}
&:
\mathrm{strain\ stretching},
\\
\text{STOP-C17}
&:
\mathrm{Critical\ Quotient\ Gauge\text{-}Covariance/Stretching\ Gap},
\\
\text{Next}
&:
\mathrm{Critical\ One\text{-}Form/Circulation\ Quotient}.
\end{aligned}
}
$$
