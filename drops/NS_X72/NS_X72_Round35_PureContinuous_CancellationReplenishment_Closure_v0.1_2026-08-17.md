# NS × X 積分 × 24/72 範式實戰
## Round 35 — Pure Continuous Cancellation-Replenishment Budget Closure / Cofactor–Pressure Coherence Route

- 日期：2026-08-17
- 版本：v0.1
- 狀態：Proof-Route Experiment / Continuous-Only Replenishment-Audit Branch
- canonical source：UTF-8 Markdown
- canonical math delimiters：inline `$...$`；display `$$...$$`
- 前一輪：`NS_X72_Round34_PureContinuous_CancellationBudget_Dynamics_v0.1_2026-08-17.md`
- 本輪目標：Round 34 已證 persistent signed cancellation需要 minority-sign replenishment。本輪專門 audit determinant net-positive branch的兩條 replenishment供電線：
  $$
  -\nu\int_{d<0}\mathcal G_{\det},
  \qquad
  -\int_{d<0}\operatorname{cof}S:H_p.
  $$
  將 pressure拆成 isotropic / anisotropic cofactor coherence，將 tensor-diffusion curvature接回 higher-gradient budget，並檢驗 Kato interface dissipation能否吸收 bulk curvature。
- 非主張：本文沒有證明 cancellation reserve必在有限時間耗盡。本文證明的是：兩條 replenishment都不是 free reservoir；pressure需要 quartic amplitude與 signed tensor coherence，tensor curvature需要 higher-gradient budget且不能一般性被 Kato defect吸收。

---

# 0. Round 34 handoff

令：

$$
d=-\det S.
$$

在 net-positive dangerous branch：

$$
M_D=\int d\,dx>0,
$$

negative-sign cancellation reserve：

$$
\boxed{
R_D
=
2\int_{\{d<0\}}d_-\,dx.
}
$$

Round 34 exact law：

$$
\boxed{
\begin{aligned}
R_D'
={}&
-2\nu
\int_{\{d<0\}}
\mathcal G_{\det}dx
\\
&-
\frac12
\int_{\{d<0\}}
|S\omega|^2dx
\\
&-
2
\int_{\{d<0\}}
\operatorname{cof}S:H_pdx
\\
&-
\mathcal D_D,
\end{aligned}
}
\tag{0.1}
$$

其中：

$$
\mathcal D_D\ge0
$$

為 determinant Kato defect。

Round 34 STOP：

$$
\boxed{
\text{STOP-C38}
=
\text{Cancellation-Reserve / Sign-Selective Replenishment Gap}.
}
$$

---

# 1. Trace-free cofactor algebra

對 trace-free symmetric：

$$
S\in\mathbb R^{3\times3},
$$

Cayley–Hamilton 給：

$$
\boxed{
\operatorname{cof}S
=
S^2
-
\frac12|S|^2I.
}
\tag{1.1}
$$

因此：

$$
\boxed{
\operatorname{tr}(\operatorname{cof}S)
=
-\frac12|S|^2.
}
\tag{1.2}
$$

定義 trace-free cofactor：

$$
\boxed{
C_S^0
=
(\operatorname{cof}S)^0
=
S^2
-
\frac13|S|^2I.
}
\tag{1.3}
$$

三維 trace-free identity：

$$
\operatorname{tr}(S^4)
=
\frac12|S|^4
$$

給：

$$
\boxed{
|C_S^0|^2
=
\frac16|S|^4,
}
\tag{1.4}
$$

所以：

$$
\boxed{
|C_S^0|
=
\frac{
|S|^2
}{
\sqrt6
}.
}
\tag{1.5}
$$

此外：

$$
\boxed{
|\operatorname{cof}S|
=
\frac12|S|^2.
}
\tag{1.6}
$$

---

# 2. Pressure Hessian decomposition

令：

$$
\boxed{
H_p^0
=
H_p
-
\frac{
\Delta p
}{3}
I.
}
\tag{2.1}
$$

則：

$$
\boxed{
H_p
=
H_p^0
+
\frac{
\Delta p
}{3}I.
}
$$

whole-space incompressible NS：

$$
\boxed{
-\Delta p
=
|S|^2
-
\frac12|\omega|^2.
}
\tag{2.2}
$$

由 tensor orthogonality：

$$
\boxed{
\operatorname{cof}S:H_p
=
C_S^0:H_p^0
+
\frac13
\operatorname{tr}(\operatorname{cof}S)
\Delta p.
}
\tag{2.3}
$$

代入 (1.2)、(2.2)：

$$
\boxed{
\operatorname{cof}S:H_p
=
C_S^0:H_p^0
+
\frac16|S|^4
-
\frac1{12}
|S|^2|\omega|^2.
}
\tag{2.4}
$$

---

# 3. Exact pressure-replenishment split

所以 determinant reserve中的 pressure contribution：

$$
\boxed{
\begin{aligned}
-2\operatorname{cof}S:H_p
={}&
-2C_S^0:H_p^0
\\
&-
\frac13|S|^4
+
\frac16|S|^2|\omega|^2.
\end{aligned}
}
\tag{3.1}
$$

這把 pressure replenishment分成：

## P-aniso

$$
\boxed{
-2C_S^0:H_p^0.
}
\tag{3.2}
$$

## P-iso

$$
\boxed{
\frac16|S|^2
\left(
|\omega|^2
-
2|S|^2
\right).
}
\tag{3.3}
$$

所以 isotropic pressure本身要 replenishing，必要：

$$
\boxed{
|\omega|^2
>
2|S|^2.
}
\tag{3.4}
$$

否則：

$$
P_{\rm iso}\le0.
$$

---

# 4. Cofactor–pressure coherence

在 negative-reserve region：

$$
A_-(t)
=
\{x:d(x,t)<0\},
$$

定義：

$$
\boxed{
U_p
=
\|C_S^0\|_{L^2(A_-)},
}
\tag{4.1}
$$

$$
\boxed{
V_p
=
\|H_p^0\|_{L^2(A_-)}.
}
\tag{4.2}
$$

若：

$$
U_pV_p>0,
$$

定義 replenishing coherence：

$$
\boxed{
\rho_p^-
=
-
\frac{
\int_{A_-}
C_S^0:H_p^0dx
}{
U_pV_p
}
\in[-1,1].
}
\tag{4.3}
$$

則 anisotropic pressure replenishment精確為：

$$
\boxed{
\mathcal P_{\rm aniso}
=
2
\rho_p^-
U_pV_p.
}
\tag{4.4}
$$

所以：

$$
\boxed{
\rho_p^->0
}
$$

才是 replenishing alignment。

若：

$$
\rho_p^-<0,
$$

anisotropic pressure反而侵蝕 cancellation reserve。

---

# 5. Pressure replenishment requires coherence, not amplitude alone

由：

$$
|C_S^0|
=
|S|^2/\sqrt6,
$$

有：

$$
\boxed{
U_p
=
\frac1{\sqrt6}
\|S\|_{L^4(A_-)}^2.
}
\tag{5.1}
$$

所以：

$$
\boxed{
\mathcal P_{\rm aniso}
=
\frac{
2
}{
\sqrt6
}
\rho_p^-
\|S\|_{L^4(A_-)}^2
V_p.
}
\tag{5.2}
$$

即使：

$$
V_p
$$

很大，

若：

$$
\rho_p^-\approx0,
$$

anisotropic replenishment仍然很弱。

因此 pressure供電是：

$$
\boxed{
\text{amplitude}
\times
\text{cofactor–pressure coherence}.
}
$$

這重新接回 Round 26–29 angular/coherence-locking obstruction。

---

# 6. Hilbert-angle pressure phase

若：

$$
|\rho_p^-|<1,
$$

定義：

$$
\boxed{
\theta_p^-
=
\arccos
\rho_p^-.
}
\tag{6.1}
$$

則：

$$
\boxed{
\mathcal P_{\rm aniso}
=
2U_pV_p
\cos\theta_p^-.
}
\tag{6.2}
$$

因此 Round 27 Nonstationary Angular-Cancellation Lemma可直接套到 time integral：

$$
\int
\mathcal P_{\rm aniso}(t)dt.
$$

若：

$$
|\dot\theta_p^-|
\ge
\Omega>0
$$

且 amplitude modulation受控，

則 cumulative anisotropic replenishment被：

$$
O(\Omega^{-1})
$$

抑制。

所以：

$$
\boxed{
\textbf{
persistent anisotropic pressure replenishment
requires Hilbert-space coherence locking or strong modulation.
}
}
\tag{6.3}
$$

---

# 7. Pressure replenishment envelope

由：

$$
|\operatorname{cof}S|
=
\frac12|S|^2,
$$

有：

$$
\boxed{
\begin{aligned}
\left|
2
\int_{A_-}
\operatorname{cof}S:H_pdx
\right|
&\le
\int_{A_-}
|S|^2|H_p|dx
\\
&\le
\|S\|_4^2
\|H_p\|_2.
\end{aligned}
}
\tag{7.1}
$$

whole-space pressure Hessian是 Riesz-transform matrix applied to：

$$
|S|^2-\frac12|\omega|^2.
$$

所以：

$$
\boxed{
\|H_p\|_2
\le
C
\left(
\|S\|_4^2
+
\|\omega\|_4^2
\right).
}
\tag{7.2}
$$

因此：

$$
\boxed{
\mathcal B_p
:=
\left[
-2
\int_{A_-}
\operatorname{cof}S:H_pdx
\right]_+
\le
C
\left(
\|S\|_4^4
+
\|\omega\|_4^4
\right).
}
\tag{7.3}
$$

所以 pressure replenishment沒有 independent reservoir。

它仍燒 Round 30 quartic budget。

---

# 8. Vorticity + isotropic-pressure gate

Round 34 reserve equation已有 vorticity erosion：

$$
-\frac12|S\omega|^2.
$$

和 P-iso合併：

$$
\boxed{
\begin{aligned}
\mathcal E_{\omega,\rm iso}
={}&
-\frac12|S\omega|^2
+
\frac16|S|^2|\omega|^2
-
\frac13|S|^4.
\end{aligned}
}
\tag{8.1}
$$

若：

$$
|S||\omega|>0,
$$

定義：

$$
\boxed{
\alpha_\omega
=
\frac{
3|S\omega|^2
}{
|S|^2|\omega|^2
}.
}
\tag{8.2}
$$

則：

$$
\boxed{
\mathcal E_{\omega,\rm iso}
=
\frac16
|S|^2|\omega|^2
(1-\alpha_\omega)
-
\frac13|S|^4.
}
\tag{8.3}
$$

因此 combined vorticity + isotropic pressure要 replenishing，必要：

$$
\boxed{
\alpha_\omega<1
}
\tag{8.4}
$$

以及：

$$
\boxed{
|\omega|^2
>
\frac{
2|S|^2
}{
1-\alpha_\omega
}.
}
\tag{8.5}
$$

所以它需要：

- strong vorticity amplitude；
- alignment with a below-RMS strain direction。

不是 generic positive supply。

---

# 9. Exact tensor-diffusion curvature

Round 33 定義：

$$
\mathcal G_{\det}
=
\sum_k
D^2\det(S)
[
\partial_kS,
\partial_kS
].
$$

因：

$$
\det S
=
\frac13
\operatorname{tr}(S^3)
$$

on trace-free $3\times3$ matrices，

且：

$$
\partial_kS
$$

亦 trace-free，

得到：

$$
\boxed{
\mathcal G_{\det}
=
2
\sum_k
\operatorname{tr}
\left[
S(\partial_kS)^2
\right].
}
\tag{9.1}
$$

因此：

$$
\boxed{
|\mathcal G_{\det}|
\le
2
|S|
|\nabla S|^2.
}
\tag{9.2}
$$

---

# 10. Tensor-curvature replenishment envelope

定義：

$$
\boxed{
\mathcal B_{\rm curv}
=
\left[
-2\nu
\int_{A_-}
\mathcal G_{\det}dx
\right]_+.
}
\tag{10.1}
$$

由 (9.2)：

$$
\boxed{
\mathcal B_{\rm curv}
\le
4\nu
\int
|S|
|\nabla S|^2dx.
}
\tag{10.2}
$$

Hölder + Sobolev：

$$
\|S\|_3
\lesssim
\|S\|_2^{1/2}
\|\nabla S\|_2^{1/2},
$$

$$
\|\nabla S\|_3
\lesssim
\|\nabla S\|_2^{1/2}
\|\Delta S\|_2^{1/2},
$$

所以：

$$
\boxed{
\int
|S|
|\nabla S|^2
\lesssim
\|S\|_2^{1/2}
\|\nabla S\|_2^{3/2}
\|\Delta S\|_2.
}
\tag{10.3}
$$

Young：

$$
\boxed{
\mathcal B_{\rm curv}
\le
\frac{\nu}{2}
\|\Delta S\|_2^2
+
C\nu
\|S\|_2
\|\nabla S\|_2^3.
}
\tag{10.4}
$$

所以 tensor-curvature replenishment也回到 Round 05 higher-gradient budget。

---

# 11. Can Kato defect absorb tensor curvature?

Round 34 determinant Kato defect：

$$
\mathcal D_D
$$

來自：

$$
\nu
\phi_\varepsilon''(d)
|\nabla d|^2
$$

在：

$$
d=0
$$

sign interface附近的極限。

但：

$$
\mathcal G_{\det}
=
2
\sum_k
\operatorname{tr}
[
S(\partial_kS)^2
]
$$

是一個 bulk negative-region quantity。

所以兩者支撐幾何不同。

下面給 explicit structural witness。

---

# 12. Bulk–Interface Mismatch Witness

令 divergence-free polynomial velocity：

$$
\boxed{
\begin{aligned}
u_1
&=
-x_1
+
\frac12x_1^2
+
\frac12x_2^2,
\\
u_2
&=
-(1+x_1)x_2,
\\
u_3
&=
2x_3.
\end{aligned}
}
\tag{12.1}
$$

可驗證：

$$
\nabla\cdot u=0.
$$

其 strain：

$$
\boxed{
S
=
\operatorname{diag}
(
-1+x_1,
-1-x_1,
2
).
}
\tag{12.2}
$$

對：

$$
|x_1|<1,
$$

$$
\det S
=
2(1-x_1^2)>0,
$$

所以：

$$
\boxed{
d=-\det S<0.
}
\tag{12.3}
$$

此 region遠離 sign interface時 determinant Kato defect sharp limit為零。

但：

$$
\partial_1S
=
\operatorname{diag}(1,-1,0),
$$

其餘 derivative為零。

因此：

$$
\boxed{
\mathcal G_{\det}
=
2
\operatorname{tr}
\left[
S(\partial_1S)^2
\right]
=
-4.
}
\tag{12.4}
$$

所以：

$$
\boxed{
-2\nu\mathcal G_{\det}
=
8\nu>0
}
\tag{12.5}
$$

在 entire local negative-reserve region提供 replenishment，

即使沒有任何 sign-interface Kato defect。

因此不存在 purely local universal：

$$
\boxed{
[-\mathcal G_{\det}]_+
\le
C
\times
\text{Kato-interface defect density}.
}
\tag{12.6}
$$

此 witness是 local divergence-free structural field，不宣稱為 whole-space finite-energy NS solution。

---

# 13. Tensor-curvature coherence

由：

$$
|\mathcal G_{\det}|
\le
2|S||\nabla S|^2,
$$

在：

$$
|S||\nabla S|>0
$$

處定義：

$$
\boxed{
\rho_{\rm curv}
=
-
\frac{
\mathcal G_{\det}
}{
2|S||\nabla S|^2
}
\in[-1,1].
}
\tag{13.1}
$$

則 tensor-curvature replenishment density：

$$
\boxed{
-2\nu\mathcal G_{\det}
=
4\nu
|S|
|\nabla S|^2
\rho_{\rm curv}.
}
\tag{13.2}
$$

所以它也具有：

$$
\boxed{
\text{amplitude}
\times
\text{signed geometric coherence}.
}
$$

並不是所有 higher-gradient activity都補 cancellation。

---

# 14. Total replenishment envelope

定義：

$$
\boxed{
\mathcal E_D
=
\frac12
\int_{A_-}
|S\omega|^2dx
+
\mathcal D_D
}
\tag{14.1}
$$

作為 mandatory erosion。

由 Round 34 exact equation與 Sections 7、10：

$$
\boxed{
R_D'
\le
\mathcal B_{\rm curv}
+
\mathcal B_p
-
\mathcal E_D.
}
\tag{14.2}
$$

其中：

$$
\boxed{
\mathcal B_p
\lesssim
\|S\|_4^4
+
\|\omega\|_4^4,
}
\tag{14.3}
$$

以及：

$$
\boxed{
\mathcal B_{\rm curv}
\le
\frac{\nu}{2}
\|\Delta S\|_2^2
+
C\nu
\|S\|_2
\|\nabla S\|_2^3.
}
\tag{14.4}
$$

---

# 15. Cancellation-Replenishment Budget Inequality

integrate (14.2)：

$$
\boxed{
\begin{aligned}
R_D(t_1)
+
\int_{t_0}^{t_1}
\mathcal E_Ddt
\le{}&
R_D(t_0)
\\
&+
\int_{t_0}^{t_1}
\left(
\mathcal B_{\rm curv}
+
\mathcal B_p
\right)dt.
\end{aligned}
}
\tag{15.1}
$$

命名：

$$
\boxed{
\textbf{Cancellation-Replenishment Budget Inequality}.
}
$$

因此 persistent determinant cancellation沒有新 free energy source。

所有 replenishment都由：

$$
\boxed{
\text{higher derivative}
+
\text{quartic amplitude}
+
\text{coherence}
}
$$

支付。

---

# 16. Cancellation Exhaustion Criterion

若在：

$$
[t_0,T)
$$

net-positive branch：

$$
M_D>0
$$

持續成立，且：

$$
\boxed{
\int_{t_0}^{T}
\left(
\mathcal B_{\rm curv}
+
\mathcal B_p
\right)dt
<
\infty,
}
\tag{16.1}
$$

但：

$$
\boxed{
\int_{t_0}^{T}
\mathcal E_Ddt
=
\infty,
}
\tag{16.2}
$$

則 (15.1) 與：

$$
R_D\ge0
$$

矛盾。

所以：

$$
\boxed{
\textbf{
divergent cancellation erosion forces divergent replenishment supply
or termination of the persistent net-positive cancellation branch.
}
}
\tag{16.3}
$$

這是一個 conditional exhaustion criterion，不是 global regularity theorem。

---

# 17. Replenishment efficiency ratio

定義 interval budget：

$$
\boxed{
\mathfrak R_{\rm rep}(I)
=
\frac{
\int_I
\mathcal E_Ddt
}{
R_D(t_0)
+
\int_I
(
\mathcal B_{\rm curv}
+
\mathcal B_p
)dt
}.
}
\tag{17.1}
$$

若：

$$
\boxed{
\mathfrak R_{\rm rep}(I)>1,
}
\tag{17.2}
$$

則 persistent cancellation reserve到 interval終點前必失效／branch假設必改變。

這是一個 continuous budget diagnostic。

---

# 18. Pressure replenishment returns to phase locking

anisotropic supply：

$$
\mathcal P_{\rm aniso}
=
2U_pV_p
\rho_p^-.
$$

若：

$$
\rho_p^-
=
\cos\theta_p^-,
$$

則它和 Round 27：

$$
A\cos\theta
$$

完全同型。

所以 long-lived pressure replenishment需：

$$
\boxed{
\text{cofactor–pressure phase locking}
\vee
\text{strong amplitude modulation}
\vee
\text{phase-speed modulation}.
}
\tag{18.1}
$$

因此：

$$
\boxed{
\textbf{
cancellation replenishment and angular phase locking are not separate bosses.
}
}
\tag{18.2}
$$

pressure若想長期隱藏 determinant danger，

必須同時支付：

- quartic amplitude；
- nonlocal tensor coherence persistence。

---

# 19. Pressure amplitude budget remains old quartic obstruction

三維 interpolation：

$$
\|S\|_4^4
\lesssim
\|S\|_2
\|\nabla S\|_2^3.
$$

Hodge identities給：

$$
\|\omega\|_4^4
\lesssim
\|\omega\|_2
\|\nabla\omega\|_2^3
\asymp
\|S\|_2
\|\nabla S\|_2^3.
$$

因此：

$$
\boxed{
\mathcal B_p
\lesssim
\|S\|_2
\|\nabla S\|_2^3.
}
\tag{19.1}
$$

所以 pressure replenishment的 amplitude supply仍回到 Round 05 / 30 higher-gradient nonlinearity。

---

# 20. No-free-replenishment synthesis

到 Round 35：

## tensor-diffusion curvature

需要：

$$
\boxed{
\nu
\int
|S||\nabla S|^2
}
$$

higher-gradient budget，

且不能由 Kato interface defect普遍吸收。

## isotropic pressure

只有在：

$$
|\omega|^2>2|S|^2
$$

等 amplitude gate下才可能補貨。

## anisotropic pressure

需要：

$$
\boxed{
\rho_p^->0
}
$$

cofactor–pressure coherence，

並且 amplitude受 quartic budget控制。

## vorticity term

在 net-positive branch：

$$
\boxed{
-\frac12|S\omega|^2
}
$$

直接侵蝕 reserve。

所以：

$$
\boxed{
\textbf{No Free Cancellation-Replenishment Principle}.
}
\tag{20.1}
$$

---

# 21. Representation-stable obstruction confluence

Round 04：

$$
\text{nonlocal pressure}
$$

Round 05：

$$
\text{higher-gradient strain}
$$

Round 18：

$$
\text{vorticity interaction}
$$

Round 26–29：

$$
\text{nonlocal coherence / phase lock}
$$

Round 34：

$$
\text{cancellation replenishment}
$$

Round 35把它們重新壓成：

$$
\boxed{
\text{replenishment}
=
\text{higher-gradient amplitude}
+
\text{pressure coherence}
-
\text{vorticity erosion}.
}
\tag{21.1}
$$

所以 obstruction core再次 representation-stable。

---

# 22. STOP-C39 — Replenishment-Closure / Cofactor–Pressure Coherence Gap

$$
\boxed{
\begin{aligned}
\text{layer}
&=
\mathrm{cancellation\ replenishment\ closure},
\\
\text{tensor curvature}
&=
2\sum_k\operatorname{tr}[S(\partial_kS)^2],
\\
\text{tensor-curvature supply}
&\to
\mathrm{higher\text{-}gradient\ budget},
\\
\text{Kato absorption}
&=
\mathrm{false\ as\ universal\ mechanism},
\\
\text{pressure split}
&=
\mathrm{isotropic}
+
\mathrm{anisotropic},
\\
\text{isotropic replenishment}
&=
\mathrm{amplitude/alignment\ gated},
\\
\text{anisotropic replenishment}
&=
\mathrm{cofactor\text{-}pressure\ coherence},
\\
\text{pressure amplitude}
&\to
\mathrm{quartic\ strain/vorticity},
\\
\text{persistent pressure supply}
&\to
\mathrm{phase/coherence\ locking},
\\
\text{mandatory erosion}
&=
\mathcal D_D
+
\frac12\int_{d<0}|S\omega|^2,
\\
\text{missing}
&=
\mathrm{unconditional\ control\ of\ cofactor\text{-}pressure\ coherence
and\ tensor\text{-}curvature\ replenishment},
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
\textbf{STOP-C39:
Replenishment-Closure / Cofactor–Pressure Coherence Gap}.
}
$$

---

# 23. 24/72 Ledger — Round 35

| Step | object | $B$ | $U$ | $O$ | $L$ | status |
|---|---|---|---|---|---|---|
| C512 | trace-free cofactor $C_S^0$ | $\mathsf C$ | tensor algebra | relational | $\mathsf F$ | EXACT |
| C513 | cofactor norm identities | $\mathsf C$ | algebraic | scalar | $\mathsf F$ | PROVED |
| C514 | pressure Hessian trace split | $\mathsf C$ | tensor decomposition | relational | $\mathsf F$ | EXACT |
| C515 | exact pressure replenishment split | $\mathsf C$ | sign decomposition | targeted | $\mathsf F$ | EXACT |
| C516 | cofactor–pressure coherence $\rho_p^-$ | $\mathsf C$ | Hilbert geometry | scalar | $\mathsf F$ | FORM |
| C517 | anisotropic pressure factorization | $\mathsf C$ | amplitude/coherence | targeted | $\mathsf F$ | EXACT |
| C518 | Hilbert-angle phase lock | $\mathsf C$ | angular dynamics | scalar | $\mathsf F$ | CONNECTION |
| C519 | pressure quartic envelope | $\mathsf C$ | Riesz / Hölder | targeted | $\mathsf F$ | PROVED |
| C520 | isotropic-vorticity gate | $\mathsf C$ | alignment/amplitude | targeted | $\mathsf F$ | PROVED |
| C521 | exact determinant curvature $\mathcal G_{\det}$ | $\mathsf C$ | second derivative | relational | $\mathsf F$ | EXACT |
| C522 | curvature pointwise envelope | $\mathsf C$ | tensor inequality | scalar | $\mathsf F$ | PROVED |
| C523 | higher-gradient curvature budget | $\mathsf C$ | Sobolev / Young | targeted | $\mathsf F$ | PROVED |
| C524 | Bulk–Interface Mismatch Witness | $\mathsf C$ | local structural field | targeted | $\mathsf F$ | CONSTRUCTED |
| C525 | Kato absorbs curvature | $\mathsf C$ | interface/bulk comparison | targeted | $\mathsf F$ | REFUTED universally |
| C526 | curvature coherence $\rho_{\rm curv}$ | $\mathsf C$ | geometric alignment | scalar | $\mathsf F$ | FORM |
| C527 | total replenishment envelope | $\mathsf C$ | budget synthesis | $\mathsf X$ | $\mathsf F$ | PROVED |
| C528 | cancellation-replenishment inequality | $\mathsf C$ | spacetime budget | targeted | $\mathsf F$ | PROVED |
| C529 | cancellation exhaustion criterion | $\mathsf C$ | continuation logic | targeted | $\mathsf F$ | CONDITIONAL |
| C530 | no-free-replenishment synthesis | $\mathsf C$ | route compression | $\mathsf X$ | $\mathsf F$ | ESTABLISHED |
| C531 | unconditional cofactor-pressure control | $\mathsf C$ | coupled NS | targeted | $\mathsf F$ | OPEN / STOP-C39 |

---

# 24. Continuous-versus-discrete status

本輪新 objects：

- trace-free cofactor tensor；
- pressure Hessian trace/deviatoric split；
- Hilbert-space coherence angle；
- tensor-curvature coherence；
- continuous spacetime replenishment budget；
- continuous sign region：
  $$
  \{d<0\}.
  $$

全部是 continuous tensor / measure / PDE objects。

沒有：

- sign cell enumeration；
- discrete pressure modes；
- discrete curvature events；
- graph replenishment network。

因此：

$$
\boxed{
T_{\mathsf C\to\mathsf D}
=
\text{NOT YET REACHED}.
}
$$

---

# 25. Strongest results of Round 35

## R35-A — exact pressure split

$$
\boxed{
-2\operatorname{cof}S:H_p
=
-2C_S^0:H_p^0
-\frac13|S|^4
+\frac16|S|^2|\omega|^2.
}
$$

## R35-B — exact cofactor anisotropy size

$$
\boxed{
|C_S^0|
=
|S|^2/\sqrt6.
}
$$

## R35-C — pressure replenishment coherence

$$
\boxed{
\mathcal P_{\rm aniso}
=
2\rho_p^-U_pV_p.
}
$$

large nonlocal pressure amplitude without positive $\rho_p^-$ does not replenish cancellation.

## R35-D — exact tensor-diffusion curvature

$$
\boxed{
\mathcal G_{\det}
=
2
\sum_k
\operatorname{tr}
[
S(\partial_kS)^2
].
}
$$

## R35-E — Kato absorption no-go

there exist local divergence-free strain fields with：

$$
d<0,
\qquad
\mathcal D_D=0,
\qquad
-\mathcal G_{\det}>0.
$$

所以 tensor-curvature replenishment can live in the bulk away from sign interface.

## R35-F — replenishment budget

$$
\boxed{
R_D(t_1)
+
\int_I\mathcal E_D
\le
R_D(t_0)
+
\int_I
(
\mathcal B_{\rm curv}
+
\mathcal B_p
).
}
$$

---

# 26. Next round — Cofactor–Pressure Coherence Dynamics

Round 35 將真正 nonlocal replenishment壓成：

$$
\boxed{
\rho_p^-(t)
=
-
\frac{
\langle C_S^0,H_p^0\rangle_{A_-}
}{
\|C_S^0\|_{2,A_-}
\|H_p^0\|_{2,A_-}
}.
}
$$

下一輪直接研究：

1. $\rho_p^-$ 如何隨 moving negative-determinant region演化；
2. $C_S^0$ 的 material derivative；
3. $H_p^0$ 的 time derivative / pressure Poisson differentiation；
4. moving sign-region boundary flux；
5. pressure replenishment coherence是否可 phase-lock；
6. 若 rapid dephasing，Round 27 cancellation lemma是否壓低 cumulative replenishment；
7. 若 stable replenishing coherence存在，它需要什麼 pressure/source organization；
8. 保持 continuous tensor與 moving-domain transport，不做 discrete sign-state switching。

---

# 27. External primary-source anchors

1. Maurizio Carbone, Michele Iovieno, Andrew D. Bragg, *Gauge symmetry and dimensionality reduction of the anisotropic pressure Hessian*, arXiv:1911.08652.
   - anisotropic pressure Hessian是 velocity-gradient dynamics中的 nonlocal functional，並與 strain eigenframe / vorticity geometry有強 alignment structure。

2. Josin Tom, Maurizio Carbone, Andrew D. Bragg, *Exploring the turbulent velocity gradients at different scales from the perspective of the strain-rate eigenframe*, arXiv:2005.04300.
   - strain eigenframe rotation中 anisotropic pressure Hessian具有關鍵作用的 DNS / eigenframe-dynamics背景。

3. Borys Álvarez-Samaniego, Wilson P. Álvarez-Samaniego, Pedro G. Fernández-Dalgo, *On the use of the Riesz transforms to determine the pressure term in the incompressible Navier-Stokes equations on the whole space*, arXiv:2004.02588.
   - whole-space pressure的 Riesz-transform representation背景。

4. Evan Miller, *On the interaction of strain and vorticity for solutions of the Navier--Stokes equation*, arXiv:2407.02691.
   - strain–vorticity interaction、higher-gradient identity與 nonlinear depletion背景。

本輪 cofactor norm identities、pressure replenishment decomposition、tensor-diffusion curvature identity、Bulk–Interface Mismatch Witness與 Cancellation-Replenishment Budget Inequality均為本文直接推導。

---

# 28. Commit state

$$
\boxed{
\begin{aligned}
\text{Route}
&=
\mathrm{Pure\ Continuous\ Cancellation\text{-}Replenishment\ Closure},
\\
\text{Essential }\mathsf C\to\mathsf D
&=
\mathrm{Not\ reached},
\\
\text{Tensor-curvature supply}
&=
\mathrm{higher\text{-}gradient\ budget},
\\
\text{Universal Kato absorption}
&=
\mathrm{false},
\\
\text{Pressure amplitude supply}
&=
\mathrm{quartic\ budget},
\\
\text{Anisotropic pressure supply}
&=
\mathrm{cofactor\text{-}pressure\ coherence},
\\
\text{Persistent pressure replenishment}
&=
\mathrm{phase\ locking/modulation},
\\
\text{No free replenishment}
&=
\mathrm{established\ as\ route\ map},
\\
\text{STOP-C39}
&=
\mathrm{Replenishment\text{-}Closure/Cofactor\text{-}Pressure\ Coherence\ Gap},
\\
\text{Next}
&=
\mathrm{Cofactor\text{-}Pressure\ Coherence\ Dynamics}.
\end{aligned}
}
$$
