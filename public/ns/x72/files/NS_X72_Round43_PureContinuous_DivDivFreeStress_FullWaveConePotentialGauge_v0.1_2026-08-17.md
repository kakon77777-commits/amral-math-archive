# NS × X 積分 × 24/72 範式實戰
## Round 43 — Pure Continuous Double-Divergence-Free Stress / Full-Wave-Cone Potential-Gauge Route

- 日期：2026-08-17
- 版本：v0.1
- 狀態：Proof-Route Experiment / Continuous-Only Differential-Constraint Branch
- canonical source：UTF-8 Markdown
- canonical math delimiters：inline `$...$`；display `$$...$$`
- 前一輪：`NS_X72_Round42_PureContinuous_PiolaVorticity_VisibleInvisibleStress_v0.1_2026-08-17.md`
- 本輪目標：Round 42 已將 nonlocal Piola defect壓成 Riesz-invisible trace-free symmetric stress
  $$
  W_T,
  \qquad
  \partial_i\partial_j(W_T)_{ij}=0.
  $$
  本輪直接研究這個 differential constraint本身是否足以提供 compensated regularity。建立 divdiv constant-rank symbol、full wave cone、exact symcurl potential/gauge representation、quadratic null-Lagrangian no-go與 constrained transfer triad witness。
- 非主張：本文沒有證明 actual NS vorticity-generated $W_T$ 可以任意實現所有 divdiv-free tensor waves。相反地，本輪結論是：**divdiv constraint alone is too weak**；下一步必須使用
  $$
  W_L+W_T
  =
  \omega\otimes\omega-\frac13|\omega|^2I
  $$
  的 nonlinear realizability與
  $$
  \nabla\cdot\omega=0.
  $$

---

# 0. Round 42 handoff

Round 42 定義 trace-free vorticity stress：

$$
\boxed{
W
=
\omega\otimes\omega
-
\frac13|\omega|^2I.
}
\tag{0.1}
$$

Riesz visible/invisible decomposition：

$$
\boxed{
W
=
W_L+W_T,
}
\tag{0.2}
$$

其中：

$$
\boxed{
W_L
=
\mathbb P_LW,
\qquad
W_T
=
(I-\mathbb P_L)W.
}
\tag{0.3}
$$

and：

$$
\boxed{
\mathcal T_0^\ast W_T=0.
}
\tag{0.4}
$$

因 $W_T$ trace-free：

$$
\boxed{
\partial_i\partial_j(W_T)_{ij}=0.
}
\tag{0.5}
$$

Round 42 STOP：

$$
\boxed{
\text{STOP-C46}
=
\text{Visible–Invisible Vorticity-Stress Transfer / Double-Divergence Compensation Gap}.
}
$$

---

# 1. The trace-free divdiv operator

令：

$$
\mathbb S_0
=
\{
A\in\mathbb R^{3\times3}
:
A^\top=A,
\ \operatorname{tr}A=0
\}.
$$

dimension：

$$
\dim\mathbb S_0=5.
$$

定義：

$$
\boxed{
\mathcal A(D)
=
\operatorname{div}\operatorname{div}
:
\mathbb S_0
\to
\mathbb R.
}
\tag{1.1}
$$

Fourier symbol：

$$
\boxed{
\mathcal A(\xi)M
=
-\xi^\top M\xi.
}
\tag{1.2}
$$

sign convention對 kernel無影響。

---

# 2. Constant-rank property

對：

$$
\xi\ne0,
$$

令：

$$
n=\frac{\xi}{|\xi|}.
$$

取：

$$
\boxed{
M_\xi
=
n\otimes n
-
\frac13I
\in\mathbb S_0.
}
\tag{2.1}
$$

則：

$$
\boxed{
\xi^\top M_\xi\xi
=
\frac23|\xi|^2
\ne0.
}
\tag{2.2}
$$

因此：

$$
\boxed{
\operatorname{rank}
\mathcal A(\xi)
=
1
\qquad
\forall\xi\ne0.
}
\tag{2.3}
$$

所以：

$$
\boxed{
\operatorname{div}\operatorname{div}
\text{ on }\mathbb S_0
\text{ is a homogeneous constant-rank operator.}
}
$$

---

# 3. Frequency-wise invisible subspace

對 unit direction：

$$
n,
$$

定義：

$$
\boxed{
\mathcal K_n
=
\{
M\in\mathbb S_0
:
n^\top Mn=0
\}.
}
\tag{3.1}
$$

因：

$$
\mathcal A(\xi)
$$

rank one，

$$
\boxed{
\dim\mathcal K_n=4.
}
\tag{3.2}
$$

若：

$$
n=e_3,
$$

則：

$$
\boxed{
M
=
\begin{pmatrix}
a & b & c\\
b & -a & d\\
c & d & 0
\end{pmatrix}.
}
\tag{3.3}
$$

所以每個 frequency direction只有一個 scalar longitudinal stress component被 divdiv看到，

其餘四個 tensor polarizations都 invisible。

---

# 4. The wave cone is the entire trace-free tensor space

constant-rank operator的 wave cone：

$$
\boxed{
\Lambda_{\mathcal A}
=
\bigcup_{\xi\ne0}
\ker\mathcal A(\xi).
}
\tag{4.1}
$$

取任意：

$$
M\in\mathbb S_0,
\qquad
M\ne0.
$$

因：

$$
\operatorname{tr}M=0,
$$

$M$ 不可能 positive definite或 negative definite。

所以其 quadratic form：

$$
Q_M(n)
=
n^\top Mn
$$

在：

$$
\mathbb S^2
$$

上必取：

- positive value；
- negative value；

或已經有 zero eigenvalue。

由 continuity存在：

$$
n_\ast\in\mathbb S^2
$$

使：

$$
\boxed{
n_\ast^\top Mn_\ast=0.
}
\tag{4.2}
$$

因此：

$$
M\in\ker\mathcal A(n_\ast).
$$

所以：

$$
\boxed{
\Lambda_{\mathcal A}
=
\mathbb S_0.
}
\tag{4.3}
$$

命名：

$$
\boxed{
\textbf{Full-Wave-Cone Theorem for Trace-Free divdiv}.
}
$$

---

# 5. Every tensor amplitude admits an invisible plane wave

由 Section 4，

對任意：

$$
M\in\mathbb S_0,
$$

可選：

$$
\xi\ne0
$$

使：

$$
\xi^\top M\xi=0.
$$

則對任意 smooth scalar profile：

$$
h,
$$

$$
\boxed{
W(x)
=
M
h(\xi\cdot x)
}
\tag{5.1}
$$

滿足：

$$
\boxed{
\operatorname{div}\operatorname{div}W=0.
}
\tag{5.2}
$$

因此 divdiv-free condition本身不排除任何 pointwise tensor amplitude。

它只限制：

$$
\boxed{
\text{amplitude–frequency orientation}.
}
$$

---

# 6. No nontrivial quadratic null Lagrangian from divdiv alone

設：

$$
Q:\mathbb S_0\to\mathbb R
$$

為 homogeneous quadratic form，

並假設它是 $\mathcal A$-quasiaffine / quadratic null-Lagrangian-type compensated quantity。

對：

$$
M\in\Lambda_{\mathcal A},
$$

取 periodic mean-zero：

$$
h(s)=\cos s.
$$

則：

$$
W(x)=Mh(\xi\cdot x)
$$

為 $\mathcal A$-free，

且 mean：

$$
\overline W=0.
$$

quasiaffinity要求：

$$
\overline{Q(W)}
=
Q(\overline W)
=
0.
$$

但：

$$
\overline{Q(W)}
=
Q(M)
\overline{\cos^2}
=
\frac12Q(M).
$$

所以：

$$
Q(M)=0
$$

for every：

$$
M\in\Lambda_{\mathcal A}.
$$

由：

$$
\Lambda_{\mathcal A}
=
\mathbb S_0,
$$

得到：

$$
\boxed{
Q\equiv0.
}
\tag{6.1}
$$

命名：

$$
\boxed{
\textbf{Quadratic Compensation No-Go}.
}
$$

因此：

$$
\boxed{
|W_T|^2
}
$$

不能僅靠：

$$
\operatorname{div}\operatorname{div}W_T=0
$$

變成 nontrivial quadratic null Lagrangian。

---

# 7. Consequence for Hardy-type compensated energy

constant-rank compensated-compactness theory將 operator-specific Hardy integrability與 null-Lagrangian / quasiaffine quantities連接。

Section 6顯示：

$$
\boxed{
\text{there is no nonzero quadratic compensated scalar
available from the trace-free divdiv constraint alone.}
}
$$

所以不能期待 universal：

$$
\boxed{
|W_T|^2
\in
\mathcal H^1
}
\tag{7.1}
$$

只由：

$$
\operatorname{div}\operatorname{div}W_T=0
$$

推出。

這不排除：

- mixed bilinear quantities；
- higher-degree special invariants；
- additional vorticity realizability；

產生 compensation。

---

# 8. Cocanceling but not smoothing

另一方面，

若：

$$
M\in
\bigcap_{\xi\ne0}
\ker\mathcal A(\xi),
$$

則：

$$
\xi^\top M\xi=0
$$

for every：

$$
\xi.
$$

因此：

$$
M=0.
$$

所以：

$$
\boxed{
\operatorname{div}\operatorname{div}
\text{ on }\mathbb S_0
\text{ is cocanceling}.
}
\tag{8.1}
$$

endpoint cocanceling theory因此可對：

$$
L^1
$$

divdiv-free tensors給 negative-order dual/Sobolev compensation。

在：

$$
n=3,
$$

schematically：

$$
\boxed{
W_T\in L^1,
\quad
\operatorname{div}\operatorname{div}W_T=0
\Longrightarrow
W_T\in\dot W^{-1,3/2}.
}
\tag{8.2}
$$

但這是：

$$
\boxed{
\text{negative-order compensation},
}
$$

不是我們需要的 positive increment regularity。

因此：

$$
\boxed{
\textbf{cocancellation is real but insufficient for Round 42 endpoint transfer.}
}
$$

---

# 9. Exact divdiv differential complex

在 3D contractible domains，standard divdiv complex具有 exact sequence：

$$
\boxed{
RT
\longrightarrow
H^1(\mathbb R^3)
\xrightarrow{
\operatorname{dev}\nabla
}
H(\operatorname{symcurl};\mathbb T)
\xrightarrow{
\operatorname{symcurl}
}
H(\operatorname{divdiv};\mathbb S)
\xrightarrow{
\operatorname{divdiv}
}
L^2
\longrightarrow0.
}
\tag{9.1}
$$

其中：

- $\mathbb T$：trace-free matrices；
- $\mathbb S$：symmetric matrices。

所以在 compatible topology / boundary branch：

$$
\boxed{
\operatorname{div}\operatorname{div}W_T=0
}
$$

意味存在 trace-free tensor potential：

$$
\boxed{
\Psi
}
$$

使：

$$
\boxed{
W_T
=
\operatorname{symcurl}\Psi.
}
\tag{9.2}
$$

命名：

$$
\boxed{
\textbf{Invisible-Stress SymCurl Potential}.
}
$$

---

# 10. Potential gauge freedom

exact complex同時給：

$$
\boxed{
\operatorname{symcurl}
(
\operatorname{dev}\nabla v
)
=
0.
}
\tag{10.1}
$$

所以：

$$
\boxed{
\Psi
\sim
\Psi
+
\operatorname{dev}\nabla v.
}
\tag{10.2}
$$

命名：

$$
\boxed{
\textbf{Invisible-Stress Potential Gauge}.
}
$$

因此 $W_T$ 的 potential representation不是 discrete mode expansion，

而是 continuous gauge geometry。

---

# 11. Whole-space Fourier minimal potential

在：

$$
\xi\ne0
$$

令：

$$
\mathbb B(\xi)
$$

為：

$$
\operatorname{symcurl}
$$

symbol。

exactness給：

$$
\boxed{
\operatorname{im}\mathbb B(\xi)
=
\ker\mathcal A(\xi).
}
\tag{11.1}
$$

取 Moore–Penrose pseudoinverse：

$$
\mathbb B(\xi)^\dagger.
$$

對：

$$
\widehat W_T(\xi)
\in
\ker\mathcal A(\xi),
$$

定義：

$$
\boxed{
\widehat\Psi(\xi)
=
\mathbb B(\xi)^\dagger
\widehat W_T(\xi).
}
\tag{11.2}
$$

因：

$$
\mathbb B(\xi)
$$

homogeneous degree one且在 sphere上 constant rank，

有：

$$
\boxed{
|\xi|
|\widehat\Psi(\xi)|
\le
C
|\widehat W_T(\xi)|.
}
\tag{11.3}
$$

所以：

$$
\boxed{
\|\nabla\Psi\|_2
\le
C
\|W_T\|_2.
}
\tag{11.4}
$$

potential存在並且有自然 energy gauge。

---

# 12. Potential representation does not create a free derivative

因：

$$
W_T
=
\operatorname{symcurl}\Psi,
$$

若一個 high-frequency mode：

$$
W_T
\sim
B
e^{iN\xi\cdot x}
$$

保持 amplitude：

$$
O(1),
$$

其 minimal potential amplitude只有：

$$
O(N^{-1}).
$$

但：

$$
\operatorname{symcurl}
$$

再乘回：

$$
N.
$$

所以將 derivative轉移到 potential只重新分配 derivative，

不會降低 total critical derivative count。

因此：

$$
\boxed{
\textbf{
the potential complex solves representation,
not the endpoint regularity budget.
}
}
\tag{12.1}
$$

---

# 13. Frequency projection formula

Round 42 longitudinal projection symbol可寫成：

$$
\boxed{
P_L(n)F
=
\frac32
m(n)
[
m(n):F
],
}
\tag{13.1}
$$

where：

$$
\boxed{
m(n)
=
\frac13I
-
n\otimes n,
}
\tag{13.2}
$$

and：

$$
|m(n)|^2
=
\frac23.
$$

對 trace-free：

$$
F,
$$

$$
m(n):F
=
-
n^\top Fn.
$$

所以：

$$
\boxed{
P_L(n)F=0
\iff
n^\top Fn=0.
}
\tag{13.3}
$$

也就是：

$$
\boxed{
\ker P_L(n)
=
\mathcal K_n.
}
$$

Round 42 visible/invisible decomposition因此和 divdiv symbol kernel完全一致。

---

# 14. Constrained transfer triad witness

為測試：

$$
\operatorname{divdiv}W_T=0
$$

是否能自動殺掉 Round 42 transfer，

取 frequencies：

$$
\boxed{
k
=
Ne_1,
\qquad
\ell
=
Ne_2,
}
\tag{14.1}
$$

velocity amplitude：

$$
\boxed{
a=e_2.
}
\tag{14.2}
$$

則：

$$
k\cdot a=0,
$$

所以 velocity plane wave divergence-free，

且：

$$
a\cdot\ell=N\ne0.
$$

取 invisible stress amplitude：

$$
\boxed{
B
=
\operatorname{diag}(1,0,-1).
}
\tag{14.3}
$$

因：

$$
e_2^\top Be_2=0,
$$

有：

$$
\boxed{
P_L(e_2)B=0.
}
\tag{14.4}
$$

所以：

$$
B e^{i\ell\cdot x}
$$

是 frequency-wise invisible / divdiv-free stress wave。

---

# 15. Shifted frequency becomes visible

output frequency：

$$
m
=
k+\ell
=
N(e_1+e_2).
$$

令：

$$
n_m
=
\frac{
e_1+e_2
}{
\sqrt2
}.
$$

則：

$$
\boxed{
n_m^\top Bn_m
=
\frac12.
}
\tag{15.1}
$$

所以：

$$
\boxed{
P_L(n_m)B\ne0.
}
\tag{15.2}
$$

direct calculation：

$$
\boxed{
\|P_L(n_m)B\|_F^2
=
\frac38.
}
\tag{15.3}
$$

因此 transport frequency shift將原本 invisible at：

$$
\ell
$$

的 tensor搬到：

$$
k+\ell,
$$

而新方向下它變成 partially visible。

這正是 Round 42：

$$
W_T\to W_L
$$

transfer mechanism。

---

# 16. Nonzero constrained commutator symbol

對 complex plane waves：

$$
u
=
a
e^{ik\cdot x},
$$

$$
W_T
=
B
e^{i\ell\cdot x},
$$

projection commutator：

$$
[D_u,\mathbb P_L]W_T
$$

在：

$$
m=k+\ell
$$

frequency的 coefficient為：

$$
\boxed{
i(a\cdot\ell)
[
P_L(\ell)-P_L(m)
]B.
}
\tag{16.1}
$$

因：

$$
P_L(\ell)B=0,
$$

所以：

$$
\boxed{
[D_u,\mathbb P_L]W_T
=
-iN
P_L(m)B
\ e^{im\cdot x}.
}
\tag{16.2}
$$

與 matching visible mode pairing後，

symbol magnitude包含：

$$
\boxed{
N
\|P_L(m)B\|^2
=
\frac38N.
}
\tag{16.3}
$$

real sine/cosine phases可取出相同非零 real trilinear transfer。

命名：

$$
\boxed{
\textbf{Constrained Transfer Triad Witness}.
}
$$

---

# 17. The double-divergence constraint does not lower the derivative order

Section 16 顯示：

- velocity divergence-free；
- input stress divdiv-free；
- input stress exactly Riesz-invisible；

仍可產生：

$$
\boxed{
O(N)
}
$$

visible/invisible transfer coefficient。

所以：

$$
\boxed{
\textbf{
double-divergence-free compensation alone
does not remove the one transport derivative.
}
}
\tag{17.1}
$$

這在 operator-symbol level證明 Round 42 one-total-derivative endpoint不能只靠：

$$
\operatorname{divdiv}W_T=0
$$

下降。

---

# 18. Why potential gauge cannot kill the transfer witness

對 Section 14 stress wave，

symcurl potential可取 amplitude：

$$
\Psi_N
=
O(N^{-1})
e^{i\ell\cdot x}.
$$

但 transfer中：

$$
W_T
=
\operatorname{symcurl}\Psi_N
$$

恢復：

$$
O(1)
$$

stress amplitude。

任何 gauge shift：

$$
\Psi_N
\mapsto
\Psi_N+\operatorname{dev}\nabla v
$$

不改：

$$
W_T.
$$

所以 Section 16 transfer coefficient：

$$
\frac38N
$$

是 gauge invariant。

因此：

$$
\boxed{
\text{potential gauge fixes representation redundancy,
not the transfer endpoint}.
}
$$

---

# 19. What the divdiv constraint actually gives

本輪可精確分類：

## D1 — positive structure

- constant-rank；
- cocanceling；
- exact differential complex；
- symcurl potential；
- continuous gauge；
- negative-order endpoint compensation。

## D2 — negative structure

- full wave cone；
- no nontrivial quadratic null Lagrangian；
- arbitrary tensor amplitudes admit A-free plane waves；
- constrained transfer triads survive；
- one transport derivative remains sharp at symbol level。

所以：

$$
\boxed{
\textbf{
divdiv gives representation and weak compensation,
but not enough rigidity to close quartic stress transfer.
}
}
\tag{19.1}
$$

---

# 20. The missing structure is nonlinear vorticity realizability

actual NS stress不是 arbitrary：

$$
W\in\mathbb S_0.
$$

它 satisfies：

$$
\boxed{
W
=
\omega\otimes\omega
-
\frac13|\omega|^2I.
}
\tag{20.1}
$$

pointwise eigenvalues：

$$
\boxed{
\frac23|\omega|^2,
\qquad
-\frac13|\omega|^2,
\qquad
-\frac13|\omega|^2.
}
\tag{20.2}
$$

因此：

$$
W
$$

位於 axisymmetric rank-one-generated cone：

$$
\boxed{
\mathcal M_\omega
=
\left\{
a\otimes a
-
\frac13|a|^2I
:
a\in\mathbb R^3
\right\}.
}
\tag{20.3}
$$

---

# 21. Algebraic realizability identities

對：

$$
W\in\mathcal M_\omega,
$$

有：

$$
\boxed{
|W|^2
=
\frac23|\omega|^4,
}
\tag{21.1}
$$

$$
\boxed{
\det W
=
\frac2{27}
|\omega|^6,
}
\tag{21.2}
$$

以及 sharp axisymmetric relation：

$$
\boxed{
54
(\det W)^2
=
|W|^6.
}
\tag{21.3}
$$

所以：

$$
\mathcal M_\omega
$$

是 $\mathbb S_0$ 中一個低維 nonlinear cone。

away from zero其 dimension為：

$$
3
$$

而：

$$
\dim\mathbb S_0=5.
$$

所以 actual vorticity stress具有額外兩個 algebraic realizability constraints。

---

# 22. Visible and invisible stresses are not independent

雖然：

$$
W_L
$$

與：

$$
W_T
$$

分屬 orthogonal Fourier subspaces，

它們的 sum必滿足：

$$
\boxed{
W_L+W_T
\in
\mathcal M_\omega
}
\tag{22.1}
$$

pointwise。

因此：

$$
\boxed{
54
\left[
\det(W_L+W_T)
\right]^2
=
|W_L+W_T|^6.
}
\tag{22.2}
$$

此外：

$$
\boxed{
\nabla\cdot\omega=0.
}
\tag{22.3}
$$

所以 actual NS invisible stress還攜帶：

- nonlinear axisymmetric realizability；
- divergence-free generator；
- coupling to visible stress。

這些在 Section 16 arbitrary constrained triad witness中沒有使用。

---

# 23. Full-wave-cone no-go does not kill the NS-specific route

Section 4 wave cone full表示：

$$
\boxed{
\operatorname{divdiv}W_T=0
}
$$

單獨不夠。

但 actual：

$$
W_T
=
\mathbb P_T
\left(
\omega\otimes\omega-\frac13|\omega|^2I
\right)
$$

是一個 nonlocal projection of a rank-one-generated stress。

所以 remaining route不是：

$$
\boxed{
\text{generic constant-rank compensated compactness}.
}
$$

而是：

$$
\boxed{
\textbf{nonlinear realizability + differential constraint + projection transfer}.
}
$$

這比 Round 42 的 generic $W_T$ formulation更窄。

---

# 24. STOP-C47 — Full-Wave-Cone / Vorticity-Realizability Gap

$$
\boxed{
\begin{aligned}
\text{layer}
&=
\mathrm{double\text{-}divergence\text{-}free\ invisible\ stress},
\\
\mathcal A(D)
&=
\operatorname{divdiv}
\text{ on }\mathbb S_0,
\\
\operatorname{rank}\mathcal A(\xi)
&=
1,
\\
\text{wave cone}
&=
\mathbb S_0,
\\
\text{quadratic null Lagrangian}
&=
0
\text{ only},
\\
\text{cocanceling}
&=
\mathrm{true},
\\
\text{potential}
&=
W_T=\operatorname{symcurl}\Psi,
\\
\text{gauge}
&=
\Psi\sim\Psi+\operatorname{dev}\nabla v,
\\
\text{potential endpoint gain}
&=
\mathrm{none\ automatically},
\\
\text{constrained transfer triad}
&=
\mathrm{nonzero},
\\
\text{transfer derivative}
&=
\mathrm{one\ derivative\ survives},
\\
\text{actual NS extra structure}
&=
W_L+W_T\in\mathcal M_\omega,
\quad
\nabla\cdot\omega=0,
\\
\text{missing}
&=
\mathrm{use\ of\ nonlinear\ vorticity\text{-}stress\ realizability
to\ improve\ transfer/alignment\ endpoint},
\\
T_{\mathsf C\to\mathsf D}
&=
\mathrm{NOT\ REACHED}.
\end{aligned}
}
$$

命名：

$$
\boxed{
\textbf{STOP-C47:
Full-Wave-Cone / Vorticity-Realizability Gap}.
}
$$

---

# 25. 24/72 Ledger — Round 43

| Step | object | $B$ | $U$ | $O$ | $L$ | status |
|---|---|---|---|---|---|---|
| C659 | trace-free divdiv operator | $\mathsf C$ | differential constraint | relational | $\mathsf F$ | FORM |
| C660 | constant-rank symbol | $\mathsf C$ | Fourier geometry | scalar | $\mathsf F$ | PROVED |
| C661 | invisible frequency subspace | $\mathsf C$ | kernel geometry | profile | $\mathsf F$ | EXACT |
| C662 | full wave cone | $\mathsf C$ | compensated geometry | targeted | $\mathsf F$ | PROVED |
| C663 | arbitrary invisible plane wave | $\mathsf C$ | continuous wave | relational | $\mathsf F$ | CONSTRUCTED |
| C664 | quadratic compensation no-go | $\mathsf C$ | null-Lagrangian logic | targeted | $\mathsf F$ | PROVED |
| C665 | cocanceling property | $\mathsf C$ | endpoint operator geometry | scalar | $\mathsf F$ | PROVED |
| C666 | negative-order compensation | $\mathsf C$ | cocanceling theory | scalar | $\mathsf F$ | STANDARD |
| C667 | divdiv exact complex | $\mathsf C$ | differential complex | relational | $\mathsf F$ | STANDARD |
| C668 | symcurl potential | $\mathsf C$ | potential representation | tensor | $\mathsf F$ | EXACT under topology |
| C669 | potential gauge | $\mathsf C$ | gauge geometry | relational | $\mathsf F$ | EXACT |
| C670 | Fourier minimal potential | $\mathsf C$ | pseudoinverse | tensor | $\mathsf F$ | CONSTRUCTED |
| C671 | potential no-free-derivative | $\mathsf C$ | scaling | targeted | $\mathsf F$ | PROVED |
| C672 | projection/divdiv kernel equivalence | $\mathsf C$ | Fourier projection | relational | $\mathsf F$ | EXACT |
| C673 | constrained transfer triad | $\mathsf C$ | Fourier symbol test | targeted | $\mathsf F$ | CONSTRUCTED |
| C674 | one-derivative transfer survival | $\mathsf C$ | high-frequency scaling | scalar | $\mathsf F$ | PROVED at symbol level |
| C675 | vorticity-stress realizability cone | $\mathsf C$ | nonlinear algebra | relational | $\mathsf F$ | EXACT |
| C676 | visible/invisible realizability coupling | $\mathsf C$ | nonlinear projection | $\mathsf X$ | $\mathsf F$ | IDENTIFIED |
| C677 | generic divdiv-only endpoint closure | $\mathsf C$ | compensated compactness | targeted | $\mathsf F$ | REFUTED |
| C678 | NS-specific realizability closure | $\mathsf C$ | nonlinear constrained stress | targeted | $\mathsf F$ | OPEN / STOP-C47 |

---

# 26. Continuous-versus-discrete status

本輪出現：

- differential complex；
- potential；
- gauge；
- Fourier symbol；
- plane waves；
- wave cone。

但全部使用 continuous：

$$
\xi\in\mathbb R^3\setminus\{0\},
$$

continuous tensor amplitudes與 continuous gauge fields。

沒有：

- mode lattice；
- finite element discretization作 proof substrate；
- discrete wave labels；
- graph potential。

finite-element divdiv complex只作 exact continuous complex的外部數學錨點，

本輪實際理論仍以 continuous operator symbol與 whole-space Fourier pseudoinverse表示。

因此：

$$
\boxed{
T_{\mathsf C\to\mathsf D}
=
\text{NOT YET REACHED}.
}
$$

---

# 27. Strongest results of Round 43

## R43-A — constant rank

$$
\boxed{
\operatorname{rank}
[
M\mapsto\xi^\top M\xi
]
=
1
}
$$

for every：

$$
\xi\ne0.
$$

## R43-B — full wave cone

$$
\boxed{
\Lambda_{\operatorname{divdiv}}
=
\mathbb S_0.
}
$$

## R43-C — quadratic compensated-energy no-go

$$
\boxed{
\text{the only quadratic divdiv-null-Lagrangian on }\mathbb S_0
\text{ is zero}.
}
$$

## R43-D — continuous potential/gauge

$$
\boxed{
W_T
=
\operatorname{symcurl}\Psi,
\qquad
\Psi
\sim
\Psi+\operatorname{dev}\nabla v.
}
$$

## R43-E — constrained transfer survives

there are divergence-free velocity / divdiv-free invisible stress plane-wave triads with：

$$
\boxed{
|\text{transfer symbol}|
=
\frac38N.
}
$$

所以 one transport derivative survives at high frequency。

## R43-F — actual NS stress lies on a nonlinear realizability cone

$$
\boxed{
W
=
\omega\otimes\omega-\frac13|\omega|^2I,
}
$$

with：

$$
\boxed{
54(\det W)^2
=
|W|^6.
}
$$

所以 remaining hope must use vorticity origin rather than divdiv alone。

---

# 28. Next round — Vorticity-Stress Realizability / Axisymmetric Cone Coupling

Round 43 已經把 generic double-divergence compensation route封頂。

下一輪直接使用 actual NS-specific relation：

$$
\boxed{
W
=
W_L+W_T
=
\omega\otimes\omega
-
\frac13|\omega|^2I.
}
$$

核心問題：

1. axisymmetric stress cone：
   $$
   54(\det W)^2=|W|^6
   $$
   如何約束 visible/invisible energy split；

2. $\eta_\omega$ 是否能任意接近 $0$ 或 $1$ under realizability；

3. given $W_L$，axisymmetric cone是否限制 $W_T$ 的 orientation / amplitude；

4. divergence-free：
   $$
   \nabla\cdot\omega=0
   $$
   是否進一步限制 rapid invisible stress waves；

5. Round 43 constrained triad witness是否可由 actual quadratic vorticity stress實現；

6. 若不能，transfer endpoint可能因 nonlinear realizability真正下降；

7. 若能構造 actual vorticity triads，則 STOP-C47 會被證成 sharp；

8. 全程保持 continuous Fourier/physical-space stress manifold，不做 discrete mode enumeration。

---

# 29. External primary-source anchors

1. Jun Hu, Yizhou Liang, Rui Ma, *Conforming finite element DIVDIV complexes and the application for the linearized Einstein-Bianchi system*, arXiv:2103.00088.
   - 3D exact divdiv complex：
     $$
     \operatorname{dev}\nabla
     \to
     \operatorname{symcurl}
     \to
     \operatorname{divdiv}.
     $$
   - used as the external anchor for the continuous symcurl potential / gauge structure.

2. Long Chen, Xuehai Huang, *Finite elements for divdiv-conforming symmetric tensors in three dimensions*, arXiv:2007.12399.
   - divdiv Hilbert/polynomial complexes and trace structure for symmetric tensors.

3. André Guerra, Bogdan Raiţă, *Quasiconvexity, null Lagrangians, and Hardy space integrability under constant rank constraints*, arXiv:1909.03923.
   - constant-rank compensated compactness；
   - identifies null Lagrangians with Hardy-integrable compensated quantities.

4. André Guerra, Bogdan Raiţă, Matthew R. I. Schrecker, *Compensated compactness: continuity in optimal weak topologies*, arXiv:2007.00564.
   - sharp constant-rank $\mathcal A$-free / Hardy-type compensated compactness framework.

5. Jean Van Schaftingen, *Limiting Sobolev inequalities for vector fields and canceling linear differential operators*, arXiv:1104.0192.
   - cocanceling operators and negative-order endpoint estimates for $L^1$ constrained fields.

本輪 constant-rank proof、full-wave-cone theorem、quadratic compensation no-go、whole-space pseudoinverse potential、constrained transfer triad與 vorticity-stress realizability identities均為本文直接推導。

---

# 30. Commit state

$$
\boxed{
\begin{aligned}
\text{Route}
&=
\mathrm{Pure\ Continuous\ Double\text{-}Divergence\text{-}Free\ Stress\ Compensation},
\\
\text{Essential }\mathsf C\to\mathsf D
&=
\mathrm{Not\ reached},
\\
\text{divdiv constraint}
&=
\mathrm{constant\ rank\ and\ cocanceling},
\\
\text{wave cone}
&=
\mathrm{full},
\\
\text{quadratic Hardy/null-Lagrangian gain}
&=
\mathrm{none\ nontrivial},
\\
\text{potential representation}
&=
\mathrm{symcurl\ +\ devgrad\ gauge},
\\
\text{potential endpoint gain}
&=
\mathrm{none\ automatically},
\\
\text{generic constrained transfer}
&=
\mathrm{nonzero\ and\ one\text{-}derivative},
\\
\text{remaining special structure}
&=
\mathrm{vorticity\text{-}stress\ realizability\ cone},
\\
\text{STOP-C47}
&=
\mathrm{Full\text{-}Wave\text{-}Cone/Vorticity\text{-}Realizability\ Gap},
\\
\text{Next}
&=
\mathrm{Vorticity\text{-}Stress\ Realizability/Axisymmetric\ Cone\ Coupling}.
\end{aligned}
}
$$
