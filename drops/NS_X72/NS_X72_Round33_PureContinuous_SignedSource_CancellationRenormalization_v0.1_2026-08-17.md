# NS × X 積分 × 24/72 範式實戰
## Round 33 — Pure Continuous Signed-Source / Cancellation-Preserving Renormalization Route

- 日期：2026-08-17
- 版本：v0.1
- 狀態：Proof-Route Experiment / Continuous-Only Signed-Source Branch
- canonical source：UTF-8 Markdown
- canonical math delimiters：inline `$...$`；display `$$...$$`
- 前一輪：`NS_X72_Round32_PureContinuous_SourceParticipation_Renormalization_v0.1_2026-08-17.md`
- 本輪目標：Round 32 顯示 smooth positive source participation具有 universal Fisher anti-concentration，但 determinant / $G_Q$ 有 sign interface，而 raw pressure / Biot–Savart pair kernel的 positive part會破壞 principal-value cancellation。本輪不再把 source強制正化，而直接追 signed net、total variation、Jordan balance、cancellation efficiency與 cancellation-preserving kernel renormalization。
- 非主張：本文沒有證明 signed total variation或 renormalized pair variation無條件有界。本文建立的是 lossless signed-source bookkeeping、local determinant Kato route，以及 smooth-branch even Calderón–Zygmund kernel的 second-difference renormalization。

---

# 0. Round 32 handoff

Round 32 對 smooth positive source：

$$
W>0
$$

建立：

$$
\boxed{
\mathfrak J_W
=
\frac{
\mathbb E_{\mu_Q}[W^2]
}{
\mathbb E_{\mu_Q}[W]^2
}
}
$$

及 universal participation dynamics：

$$
\boxed{
(\log\mathfrak J_W)'
=
-2\nu\langle|\nabla\log W|^2\rangle_2
+
\text{tilt selection}
+
\text{relative-source bias}.
}
$$

但三個 source classes有 representation leakage：

1. determinant：
   $$
   (-\det S)_+;
   $$
2. positive quotient growth：
   $$
   (G_Q)_+;
   $$
3. pair singular kernel：
   $$
   \mathcal C_+.
   $$

前兩者有 moving sign interface。

第三者甚至可能因：

$$
|x-y|^{-3}
$$

使 positive-part pair mass near diagonal diverge。

Round 32 STOP：

$$
\boxed{
\text{STOP-C36}
=
\text{Source-Participation Trapping / Singular-Source Renormalization Gap}.
}
$$

---

# 1. Signed source ledger

令：

$$
(\Omega,\mu)
$$

為 probability space，

且：

$$
W\in L^1(\mu)
$$

可正可負。

定義 signed net：

$$
\boxed{
M_W
=
\mathbb E_\mu[W].
}
\tag{1.1}
$$

定義 total variation magnitude：

$$
\boxed{
V_W
=
\mathbb E_\mu[|W|].
}
\tag{1.2}
$$

自然有：

$$
\boxed{
|M_W|
\le
V_W.
}
\tag{1.3}
$$

---

# 2. Jordan reconstruction

定義：

$$
W_+
=
\max\{W,0\},
$$

$$
W_-
=
\max\{-W,0\}.
$$

則：

$$
W=W_+-W_-,
$$

$$
|W|=W_++W_-.
$$

令：

$$
P_W
=
\mathbb E[W_+],
$$

$$
N_W
=
\mathbb E[W_-].
$$

所以：

$$
\boxed{
P_W
=
\frac{
V_W+M_W
}{2},
}
\tag{2.1}
$$

$$
\boxed{
N_W
=
\frac{
V_W-M_W
}{2}.
}
\tag{2.2}
$$

命名：

$$
\boxed{
\textbf{Signed-Source Jordan Reconstruction}.
}
$$

因此 local signed source不需要先對：

$$
W_+
$$

建立一條獨立微分方程，才能知道 positive mass。

只要：

$$
M_W,
\qquad
V_W
$$

可控，就能 losslessly reconstruction：

$$
P_W,
\qquad
N_W.
$$

---

# 3. Cancellation coefficient

若：

$$
V_W>0,
$$

定義 signed balance：

$$
\boxed{
c_W
=
\frac{
M_W
}{
V_W
}
\in[-1,1].
}
\tag{3.1}
$$

以及 unsigned cancellation efficiency：

$$
\boxed{
\kappa_W
=
1-|c_W|
\in[0,1].
}
\tag{3.2}
$$

interpretation：

$$
|c_W|=1
$$

表示幾乎沒有正負 cancellation；

$$
c_W=0
$$

表示 signed net完全由 equal positive / negative variation cancellation。

Jordan fractions：

$$
\boxed{
\frac{
P_W
}{
V_W
}
=
\frac{
1+c_W
}{2},
}
\tag{3.3}
$$

$$
\boxed{
\frac{
N_W
}{
V_W
}
=
\frac{
1-c_W
}{2}.
}
\tag{3.4}
$$

---

# 4. Magnitude participation

若：

$$
|W|\in L^2(\mu),
$$

定義 total-variation participation ratio：

$$
\boxed{
\mathfrak J_{|W|}
=
\frac{
\mathbb E[W^2]
}{
V_W^2
}.
}
\tag{4.1}
$$

因：

$$
|W|^2=W^2.
$$

這是 total variation measure：

$$
\boxed{
d\nu_{|W|}
=
\frac{
|W|
}{
V_W
}
d\mu
}
\tag{4.2}
$$

相對：

$$
\mu
$$

的：

$$
1+\chi^2.
$$

---

# 5. Jordan Occupancy Bound

若 measurable set：

$$
A
$$

承擔至少：

$$
\beta_+
$$

比例 positive source：

$$
\boxed{
\int_A
W_+
d\mu
\ge
\beta_+
P_W,
}
\tag{5.1}
$$

則：

$$
\int_A|W|d\mu
\ge
\beta_+
P_W
=
\beta_+
\frac{
1+c_W
}{2}
V_W.
$$

對：

$$
|W|
$$

使用 Source–Occupancy Lemma：

$$
\boxed{
\mu(A)
\ge
\frac{
\beta_+^2
(1+c_W)^2
}{
4
\mathfrak J_{|W|}
}.
}
\tag{5.2}
$$

同理，若 $A$ 承擔 $\beta_-$ fraction negative source：

$$
\boxed{
\mu(A)
\ge
\frac{
\beta_-^2
(1-c_W)^2
}{
4
\mathfrak J_{|W|}
}.
}
\tag{5.3}
$$

命名：

$$
\boxed{
\textbf{Jordan Occupancy Bound}.
}
$$

所以 signed source的 dangerous positive fraction仍可用：

$$
\text{total variation intermittency}
+
\text{signed cancellation balance}
$$

控制 occupancy。

---

# 6. Why this is better than differentiating $W_+$

若：

$$
W
$$

跨過：

$$
0,
$$

positive part：

$$
W_+
$$

的 derivative含 moving sign-interface結構。

但：

$$
M_W
=
\mathbb E[W]
$$

保持 signed smoothness，

而：

$$
V_W
=
\mathbb E[|W|]
$$

可用 Kato / convex renormalization處理。

因此：

$$
\boxed{
\text{signed net + total variation}
}
$$

通常比：

$$
\boxed{
\text{positive part alone}
}
$$

更適合作為 continuous renormalized carrier。

---

# 7. Signed determinant equation in convection–diffusion form

令：

$$
\boxed{
d
=
-\det S.
}
\tag{7.1}
$$

Round 32：

$$
\boxed{
D_td
=
-\nu
\operatorname{cof}S:\Delta S
+
\frac14
|S\omega|^2
+
\operatorname{cof}S:H_p.
}
\tag{7.2}
$$

對 scalar function：

$$
F(S)=\det S,
$$

chain rule：

$$
\Delta F(S)
=
DF(S):\Delta S
+
\sum_k
D^2F(S)
[
\partial_kS,
\partial_kS
].
$$

定義：

$$
\boxed{
\mathcal G_{\det}
=
\sum_k
D^2\det(S)
[
\partial_kS,
\partial_kS
].
}
\tag{7.3}
$$

因：

$$
d=-\det S,
$$

得到：

$$
\boxed{
D_td
-
\nu\Delta d
=
\nu\mathcal G_{\det}
+
\frac14
|S\omega|^2
+
\operatorname{cof}S:H_p.
}
\tag{7.4}
$$

令：

$$
\boxed{
F_d
=
\nu\mathcal G_{\det}
+
\frac14
|S\omega|^2
+
\operatorname{cof}S:H_p.
}
\tag{7.5}
$$

則：

$$
\boxed{
\partial_td
+
u\cdot\nabla d
-
\nu\Delta d
=
F_d.
}
\tag{7.6}
$$

---

# 8. Signed determinant net and total variation

因：

$$
\nabla\cdot u=0,
$$

若足夠 decay：

$$
\boxed{
M_D(t)
=
\int
d\,dx
}
\tag{8.1}
$$

滿足：

$$
\boxed{
M_D'
=
\int
F_d\,dx.
}
\tag{8.2}
$$

而：

$$
\boxed{
V_D(t)
=
\int
|d|dx
}
\tag{8.3}
$$

由 scalar parabolic Kato inequality得到：

$$
\boxed{
V_D'
\le
\int
\operatorname{sgn}(d)
F_d\,dx
}
\tag{8.4}
$$

在 classical / regularized sense。

更精確地，smooth convex approximation：

$$
\phi_\varepsilon(d)
=
\sqrt{
d^2+\varepsilon^2
}
$$

會產生一個 nonnegative diffusion defect：

$$
\nu
\phi_\varepsilon''(d)
|\nabla d|^2.
$$

取：

$$
\varepsilon\downarrow0
$$

得到 Kato-type total-variation dissipation。

---

# 9. Dangerous determinant positive mass without positive-part PDE

dangerous determinant production：

$$
\boxed{
P_D
=
\int
d_+dx
}
\tag{9.1}
$$

可 reconstruction：

$$
\boxed{
P_D
=
\frac{
V_D+M_D
}{2}.
}
\tag{9.2}
$$

negative determinant mass：

$$
\boxed{
N_D
=
\frac{
V_D-M_D
}{2}.
}
\tag{9.3}
$$

所以：

$$
\boxed{
\textbf{
determinant sign interface can be handled by signed net + Kato total variation,
without differentiating }d_+\textbf{ directly}.
}
}
\tag{9.4}
$$

這是 Round 32 determinant sign-interface leakage的一個 partial repair。

---

# 10. Net determinant returns to vortex stretching

whole-space identity：

$$
\boxed{
\int
\omega^\top S\omega\,dx
=
-4
\int
\det Sdx.
}
\tag{10.1}
$$

所以：

$$
\boxed{
M_D
=
\int
(-\det S)dx
=
\frac14
\int
\omega^\top S\omega\,dx.
}
\tag{10.2}
$$

因此 determinant cancellation coefficient：

$$
\boxed{
c_D
=
\frac{
\frac14
\int
\omega^\top S\omega dx
}{
\int
|\det S|dx
}.
}
\tag{10.3}
$$

它直接測量：

> total determinant variation中，有多少真正留下成 net vortex-stretching production。

---

# 11. Strong positive production can arise in two distinct ways

因：

$$
P_D
=
\frac{
V_D+M_D
}{2},
$$

large positive determinant production可來自：

## D1 — large variation, weak cancellation

$$
V_D\gg1,
\qquad
c_D\approx1.
$$

## D2 — large two-sided variation, strong cancellation

$$
V_D\gg1,
\qquad
|c_D|\ll1,
$$

但：

$$
P_D
\sim
V_D/2
$$

仍然很大。

所以：

$$
\boxed{
\text{small net vortex stretching}
}
$$

不代表：

$$
\boxed{
\text{small dangerous positive determinant activity}.
}
$$

它也可能只是：

$$
\boxed{
\text{large positive and negative determinant production cancel globally}.
}
$$

因此 total variation是一個不可省略的 relational carrier。

---

# 12. Signed source cancellation versus concentration

signed source需要兩個獨立 coordinates：

$$
\boxed{
\text{concentration}
=
\mathfrak J_{|W|}
}
$$

與：

$$
\boxed{
\text{cancellation}
=
c_W.
}
$$

高：

$$
\mathfrak J_{|W|}
$$

代表 magnitude集中在少量 carrier mass。

小：

$$
|c_W|
$$

代表 positive / negative magnitude高度平衡。

所以：

$$
\boxed{
\textbf{
magnitude concentration and sign cancellation are logically independent.
}
}
\tag{12.1}
$$

這正是 Round 32 positive-source representation無法表達的資訊。

---

# 13. Even homogeneous singular kernels

現在處理 pair singular source。

考慮：

$$
\boxed{
K(z)
=
\frac{
\Omega(e)
}{
|z|^3
},
\qquad
e=\frac z{|z|},
}
\tag{13.1}
$$

其中：

$$
\boxed{
\Omega(-e)=\Omega(e),
}
\tag{13.2}
$$

以及 spherical mean-zero：

$$
\boxed{
\int_{\mathbb S^2}
\Omega(e)d\Omega(e)
=
0.
}
\tag{13.3}
$$

pressure anisotropic Hessian kernel：

$$
3e\otimes e-I
$$

屬此類。

Round 26 exact Biot–Savart strain kernel作為 linear operator in remote vorticity也具有相同：

- degree $-3$；
- even angular kernel；
- spherical mean-zero；

結構。

---

# 14. Symmetric second-difference renormalization

令 scalar / vector source：

$$
f
$$

足夠 smooth。

考慮 truncated principal value：

$$
T_\delta f(x)
=
\int_{
\delta<|z|<R_0
}
K(z)
f(x-z)
\,dz.
$$

因：

$$
K(-z)=K(z),
$$

平均：

$$
z
\leftrightarrow
-z
$$

得：

$$
T_\delta f(x)
=
\frac12
\int_{
\delta<|z|<R_0
}
K(z)
[
f(x-z)+f(x+z)
]
dz.
$$

再用 mean-zero：

$$
\int_{\delta<|z|<R_0}
K(z)dz=0,
$$

得到 exact：

$$
\boxed{
T_\delta f(x)
=
\frac12
\int_{
\delta<|z|<R_0
}
K(z)
\left[
f(x-z)+f(x+z)-2f(x)
\right]
dz.
}
\tag{14.1}
$$

命名：

$$
\boxed{
\textbf{Cancellation-Preserving Second-Difference Renormalization}.
}
$$

---

# 15. Near-diagonal integrability after renormalization

若：

$$
f\in C^2,
$$

Taylor：

$$
\boxed{
|f(x+z)+f(x-z)-2f(x)|
\le
C
|z|^2
\sup_{|y-x|\le|z|}
|\nabla^2f(y)|.
}
\tag{15.1}
$$

而：

$$
|K(z)|
\lesssim
|z|^{-3}.
$$

三維 volume：

$$
dz
\sim
r^2drd\Omega.
$$

所以 renormalized absolute magnitude near：

$$
r=0
$$

至多：

$$
\boxed{
r^{-3}
\cdot
r^2
\cdot
r^2dr
=
r\,dr.
}
\tag{15.2}
$$

因此：

$$
\boxed{
\int_0^\delta
r\,dr
<
\infty.
}
$$

所以 smooth branch中，

signed principal-value cancellation可先編譯進：

$$
\boxed{
\Delta_z^2f(x)
=
f(x+z)+f(x-z)-2f(x)
}
$$

再談 absolute magnitude。

---

# 16. Why raw positive extraction diverges but renormalized magnitude need not

raw positive / absolute kernel：

$$
|K(z)f(x)|
$$

near diagonal：

$$
\sim
r^{-3}
$$

給：

$$
\int_0^\delta
r^{-3}r^2dr
=
\int_0^\delta
\frac{dr}{r}
=
\infty.
$$

但 cancellation-preserving source：

$$
K(z)\Delta_z^2f(x)
$$

給：

$$
\int_0^\delta
r\,dr
<
\infty.
$$

所以：

$$
\boxed{
\textbf{
the problem was not singularity alone;
it was taking magnitude before encoding the cancellation.
}
}
\tag{16.1}
$$

這直接修正 Round 32 Positive-Pair Cancellation-Destruction No-Go：

> positive extraction of the raw kernel is illegal；
> positive magnitude of a losslessly renormalized second-difference kernel can be legal in a smooth branch.

---

# 17. Log-shell cancellation profile

對：

$$
0<r<R_0,
$$

定義 signed shell：

$$
\boxed{
\Sigma_f(r;x)
=
\int_{\mathbb S^2}
\Omega(e)
f(x-re)
\,d\Omega(e).
}
\tag{17.1}
$$

則：

$$
\boxed{
T_\delta f(x)
=
\int_\delta^{R_0}
\frac{
\Sigma_f(r;x)
}{
r
}
dr.
}
\tag{17.2}
$$

mean-zero：

$$
\int\Omega=0
$$

移除 constant term。

evenness：

$$
\Omega(-e)=\Omega(e)
$$

移除 first-order odd term。

因此 smooth branch：

$$
\boxed{
\Sigma_f(r;x)
=
O(r^2).
}
\tag{17.3}
$$

所以：

$$
\boxed{
\frac{
\Sigma_f(r;x)
}{
r
}
=
O(r),
}
\tag{17.4}
$$

near：

$$
r=0.
$$

這把 principal-value cancellation變成一條 continuous log-radius profile。

---

# 18. Raw shell variation versus signed shell

定義 absolute shell envelope：

$$
\boxed{
A_f(r;x)
=
\int_{\mathbb S^2}
|\Omega(e)|
|f(x-re)|
d\Omega(e).
}
\tag{18.1}
$$

raw total variation：

$$
\int
A_f(r;x)
\frac{dr}{r}
$$

一般 logarithmically diverges。

但 signed shell：

$$
\Sigma_f(r;x)
$$

可以：

$$
O(r^2).
$$

因此定義 shell cancellation coefficient：

$$
\boxed{
c_{\rm shell}(r;x)
=
\frac{
\Sigma_f(r;x)
}{
A_f(r;x)
}
}
\tag{18.2}
$$

在 generic：

$$
A_f(r;x)\to A_0>0
$$

時：

$$
\boxed{
c_{\rm shell}(r;x)
=
O(r^2).
}
\tag{18.3}
$$

也就是 near diagonal：

$$
\boxed{
\text{raw magnitude巨大，
但 signed fraction趨近零}.
}
$$

這是 singular-integral cancellation的 continuous quantitative signature。

---

# 19. Renormalized pair variation

定義：

$$
\boxed{
\widetilde W_f(x,z)
=
\frac12
K(z)
[
f(x+z)+f(x-z)-2f(x)
].
}
\tag{19.1}
$$

其 renormalized total variation：

$$
\boxed{
\widetilde V_f
=
\iint_{
|z|<R_0
}
|
\widetilde W_f(x,z)
|
\,dz\,d\mu_Q(x)
}
\tag{19.2}
$$

在 smooth / sufficient second-difference regularity branch可有限。

此時可以再定義：

$$
\boxed{
\widetilde{\mathfrak J}_{\rm pair}
=
\frac{
\mathbb E[
|\widetilde W_f|^2
]
}{
\mathbb E[
|\widetilde W_f|
]^2
}
}
\tag{19.3}
$$

若 second moment亦 finite。

所以 pair occupancy可以在：

$$
\boxed{
\text{renormalized pair source}
}
$$

上重新合法化。

---

# 20. Regularity cost of cancellation-preserving renormalization

Section 15 用：

$$
C^2
$$

只為最直觀 sufficient condition。

真正需要的是 second-difference modulus：

$$
\boxed{
\omega_2(f,r)
=
\sup_x
\sup_{|z|\le r}
|
f(x+z)+f(x-z)-2f(x)
|.
}
\tag{20.1}
$$

只要：

$$
\boxed{
\int_0^{R_0}
\frac{
\omega_2(f,r)
}{
r
}
dr
<
\infty,
}
\tag{20.2}
$$

renormalized local singular integral具有 absolute convergence envelope。

所以 new proof obligation不是：

$$
f\in C^2
$$

本身，

而是某種 continuous Dini/Besov second-difference control。

---

# 21. Renormalization circularity warning

對 pressure：

$$
f_p
=
|S|^2-\frac12|\omega|^2.
$$

要控制：

$$
\omega_2(f_p,r)
$$

需要 strain / vorticity的 spatial regularity。

對 Biot–Savart strain：

$$
f=\omega.
$$

要控制：

$$
\omega_2(\omega,r)
$$

同樣需要 higher spatial regularity。

所以：

$$
\boxed{
\text{cancellation-preserving renormalization is structurally legal,
but its absolute-variation budget is not basic-energy free}.
}
\tag{21.1}
$$

這再次接回 Round 05/30 higher-derivative budget。

---

# 22. Signed source ledger for nonlocal kernels

對 separated / renormalized pair source：

$$
\widetilde W
$$

現在可同時追：

$$
\boxed{
M_{\widetilde W}
=
\mathbb E[\widetilde W],
}
$$

$$
\boxed{
V_{\widetilde W}
=
\mathbb E[|\widetilde W|],
}
$$

$$
\boxed{
c_{\widetilde W}
=
M_{\widetilde W}/V_{\widetilde W},
}
$$

以及：

$$
\boxed{
\mathfrak J_{|\widetilde W|}.
}
$$

因此 signed pair source也可被分成：

$$
\boxed{
\text{magnitude}
\times
\text{concentration}
\times
\text{cancellation}.
}
$$

這比 raw positive-source probability保留更多 original kernel information。

---

# 23. Cancellation-First Principle

本輪得到一個對 X-integral / representation routing很重要的原則：

$$
\boxed{
\textbf{
For a signed singular operator,
encode the exact cancellation before taking magnitude,
positive part, occupancy, or probability normalization.
}
}
\tag{23.1}
$$

否則：

$$
\boxed{
\text{representation may create a divergence
that the original operator does not possess}.
}
$$

命名：

$$
\boxed{
\textbf{Cancellation-First Principle}.
}
$$

這是 Round 32 positive-pair failure的正式修正。

---

# 24. STOP-C37 — Signed-Variation / Cancellation-Renormalization Budget Gap

$$
\boxed{
\begin{aligned}
\text{layer}
&=
\mathrm{signed\ source\ renormalization},
\\
\text{local signed source}
&=
M_W+V_W,
\\
\text{positive/negative reconstruction}
&=
(V_W\pm M_W)/2,
\\
\text{cancellation carrier}
&=
c_W=M_W/V_W,
\\
\text{concentration carrier}
&=
\mathfrak J_{|W|},
\\
\text{determinant sign interface}
&=
\text{partially repaired by Kato total variation},
\\
\text{raw pair positive extraction}
&=
\text{illegal near singular diagonal},
\\
\text{even mean-zero kernel}
&=
\text{second-difference renormalizable},
\\
\text{renormalized near-diagonal magnitude}
&=
O(r\,dr),
\\
\text{missing}
&=
\text{unconditional control of signed total variation,
second-difference regularity and renormalized pair participation},
\\
T_{\mathsf C\to\mathsf D}
&=
\text{NOT REACHED}.
\end{aligned}
}
$$

命名：

$$
\boxed{
\textbf{STOP-C37:
Signed-Variation / Cancellation-Renormalization Budget Gap}.
}
$$

---

# 25. 24/72 Ledger — Round 33

| Step | object | $B$ | $U$ | $O$ | $L$ | status |
|---|---|---|---|---|---|---|
| C473 | signed net $M_W$ | $\mathsf C$ | signed measure | scalar | $\mathsf F$ | FORM |
| C474 | total variation $V_W$ | $\mathsf C$ | magnitude measure | scalar | $\mathsf F$ | FORM |
| C475 | Jordan reconstruction | $\mathsf C$ | algebraic measure | targeted | $\mathsf F$ | EXACT |
| C476 | cancellation coefficient $c_W$ | $\mathsf C$ | recognition | scalar | $\mathsf F$ | FORM |
| C477 | magnitude participation $\mathfrak J_{|W|}$ | $\mathsf C$ | measure separation | scalar | $\mathsf F$ | FORM |
| C478 | Jordan Occupancy Bound | $\mathsf C$ | Cauchy / measure | targeted | $\mathsf F$ | PROVED |
| C479 | determinant convection–diffusion equation | $\mathsf C$ | PDE renormalization | relational | $\mathsf F$ | EXACT |
| C480 | determinant Kato variation bound | $\mathsf C$ | convex renormalization | scalar | $\mathsf F$ | CONDITIONAL EXACT/INEQUALITY |
| C481 | determinant positive-mass reconstruction | $\mathsf C$ | Jordan decomposition | targeted | $\mathsf F$ | EXACT |
| C482 | determinant cancellation / vortex stretching | $\mathsf C$ | strain-vorticity bridge | relational | $\mathsf F$ | EXACT |
| C483 | concentration-vs-cancellation split | $\mathsf C$ | signed measure | $\mathsf X$ | $\mathsf F$ | FORM |
| C484 | even mean-zero kernel class | $\mathsf C$ | singular integral | relational | $\mathsf F$ | FORM |
| C485 | second-difference renormalization | $\mathsf C$ | cancellation-preserving transform | targeted | $\mathsf F$ | EXACT |
| C486 | near-diagonal absolute integrability | $\mathsf C$ | second difference | scalar | $\mathsf F$ | PROVED in smooth branch |
| C487 | log-shell cancellation profile | $\mathsf C$ | continuous radius | profile | $\mathsf F$ | EXACT |
| C488 | shell cancellation coefficient | $\mathsf C$ | signed angular average | scalar profile | $\mathsf F$ | FORM |
| C489 | renormalized pair variation | $\mathsf C$ | product measure | scalar | $\mathsf F$ | FORM |
| C490 | Cancellation-First Principle | $\mathsf C$ | representation logic | $\mathsf X$ | $\mathsf F$ | ESTABLISHED |
| C491 | unconditional renormalized variation control | $\mathsf C$ | higher regularity | targeted | $\mathsf F$ | OPEN / STOP-C37 |

---

# 26. Continuous-versus-discrete status

本輪最核心的新 operation：

$$
f(x+z)+f(x-z)-2f(x)
$$

是 continuous symmetric second difference。

shell parameter：

$$
r\in(0,R_0)
$$

continuous。

angular variable：

$$
e\in\mathbb S^2
$$

continuous。

signed Jordan decomposition也屬 continuous measure theory。

沒有：

- atoms；
- shell index $j$；
- discrete cancellation pairs；
- graph singular-integral representation。

所以：

$$
\boxed{
T_{\mathsf C\to\mathsf D}
=
\text{NOT YET REACHED}.
}
$$

---

# 27. Strongest results of Round 33

## R33-A — Jordan reconstruction

$$
\boxed{
P_W=\frac{V_W+M_W}{2},
\qquad
N_W=\frac{V_W-M_W}{2}.
}
$$

## R33-B — Jordan occupancy

$$
\boxed{
\mu(A)
\ge
\frac{
\beta_+^2(1+c_W)^2
}{
4\mathfrak J_{|W|}
}
}
$$

for positive-source-dominant set。

## R33-C — determinant sign-interface repair

$$
\boxed{
P_D
=
\frac{
\int|-\det S|dx
+
\int(-\det S)dx
}{
2}.
}
$$

所以 positive determinant mass可由 signed net + Kato variation reconstruction。

## R33-D — cancellation-preserving singular-kernel renormalization

$$
\boxed{
T_\delta f(x)
=
\frac12
\int
K(z)
[
f(x-z)+f(x+z)-2f(x)
]dz.
}
$$

## R33-E — renormalized near-diagonal integrability

$$
\boxed{
|K(z)|\sim r^{-3},
\quad
|\Delta_z^2f|\sim r^2
\Rightarrow
|\widetilde W|\,dz
\sim
r\,dr.
}
$$

## R33-F — Cancellation-First Principle

$$
\boxed{
\text{encode cancellation first;
take magnitude / probability second}.
}
$$

---

# 28. Next round — Cancellation Budget Dynamics

Round 33 已把 source decomposition從：

$$
\text{positive only}
$$

升級成：

$$
\boxed{
\text{net}
+
\text{variation}
+
\text{concentration}
+
\text{cancellation}.
}
$$

下一輪直接研究：

$$
\boxed{
c_W(t)
=
\frac{
M_W(t)
}{
V_W(t)
}
}
$$

與 renormalized shell cancellation的 dynamics。

核心問題：

1. determinant：
   $$
   c_D(t)
   $$
   是否有 depletion / anti-cancellation law；

2. large positive and negative determinant activity能否長期互相 cancel；

3. shell cancellation coefficient：
   $$
   c_{\rm shell}(r,t)
   $$
   如何被 advection / strain / diffusion改變；

4. second-difference renormalized source的 total variation是否有 Kato-like dynamics；

5. signed cancellation若 rapid oscillate，是否再次接 Round 10 / 27 phase cancellation；

6. 若 cancellation弱化，positive source occupancy直接增大；

7. 若 cancellation強化，必支付 spatial/angular oscillation budget；

8. 仍保持 continuous radius與 signed measures。

---

# 29. External primary-source anchors

1. Borys Álvarez-Samaniego, Wilson P. Álvarez-Samaniego, Pedro G. Fernández-Dalgo, *On the use of the Riesz transforms to determine the pressure term in the incompressible Navier-Stokes equations on the whole space*, arXiv:2004.02588.
   - whole-space pressure的 Riesz-transform singular-integral representation背景。

2. Benjamin Jaye, Tomás Merchán, *On the problem of existence in principal value of a Calderón-Zygmund operator on a space of non-homogeneous type*, arXiv:1810.13299.
   - principal-value existence依賴 cancellation與 underlying measure geometry的 harmonic-analysis背景。

3. Evan Miller, *On the interaction of strain and vorticity for solutions of the Navier--Stokes equation*, arXiv:2407.02691.
   - strain–vorticity interaction與 determinant / nonlinear depletion背景。

本輪 Jordan source reconstruction、Jordan Occupancy Bound、determinant Kato route、second-difference singular-kernel renormalization、shell cancellation profile與 Cancellation-First Principle均為本文直接推導。

---

# 30. Commit state

$$
\boxed{
\begin{aligned}
\text{Route}
&=
\mathrm{Pure\ Continuous\ Signed\text{-}Source/Cancellation\ Renormalization},
\\
\text{Essential }\mathsf C\to\mathsf D
&=
\mathrm{Not\ reached},
\\
\text{Signed source carrier}
&=
(M_W,V_W,c_W,\mathfrak J_{|W|}),
\\
\text{Positive source}
&=
\mathrm{Jordan\ reconstructable},
\\
\text{Determinant interface}
&=
\mathrm{Kato\text{-}renormalizable},
\\
\text{Raw pair positive source}
&=
\mathrm{not\ lossless},
\\
\text{Signed even kernel}
&=
\mathrm{second\text{-}difference\ renormalizable},
\\
\text{Renormalized pair magnitude}
&=
\mathrm{locally\ finite\ under\ second\text{-}difference\ regularity},
\\
\text{STOP-C37}
&=
\mathrm{Signed\text{-}Variation/Cancellation\text{-}Renormalization\ Budget\ Gap},
\\
\text{Next}
&=
\mathrm{Cancellation\ Budget\ Dynamics}.
\end{aligned}
}
$$
