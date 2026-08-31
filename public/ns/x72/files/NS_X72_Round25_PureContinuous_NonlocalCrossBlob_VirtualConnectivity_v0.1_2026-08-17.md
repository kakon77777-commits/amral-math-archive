# NS × X 積分 × 24/72 範式實戰
## Round 25 — Pure Continuous Nonlocal Cross-Blob Coupling / Virtual-Connectivity Route

- 日期：2026-08-17
- 版本：v0.1
- 狀態：Proof-Route Experiment / Continuous-Only Nonlocal Cross-Region Branch
- canonical source：UTF-8 Markdown
- canonical math delimiters：inline `$...$`；display `$$...$$`
- 前一輪：`NS_X72_Round24_PureContinuous_CriticalMass_ConductanceDynamics_v0.1_2026-08-17.md`
- 本輪目標：Round 24 顯示 local viscous neck communication可隨 blob separation變得極慢。本輪重新引入 Round 04 的 nonlocal pressure與 whole-space Biot–Savart / strain recovery，研究兩個 critical-mass blobs在幾乎沒有 mass neck時是否仍透過 algebraically decaying nonlocal kernels形成「virtual connection」。
- 非主張：本文沒有證明 nonlocal coupling必然同步兩 blobs，也沒有由 nonlocal interaction推出 positive Cheeger gap。恰恰相反，本輪證明 nonlocal coupling一般是 signed / anisotropic，故 dynamic coupling與 positive mixing conductance必須區分。

---

# 0. Round 24 handoff

critical mass：

$$
d\mu_Q
=
m_Qdx
$$

obeys：

$$
\boxed{
\partial_t m_Q
+
\operatorname{div}(b_Qm_Q)
=
\nu\Delta m_Q
+
3(G_Q-\bar G_Q)m_Q.
}
\tag{0.1}
$$

Round 24 continuous Cheeger conductance：

$$
\boxed{
h_Q
=
\inf_A
\frac{
\operatorname{Per}_{\mu_Q}(A)
}{
\min\{
\mu_Q(A),
1-\mu_Q(A)
\}
}.
}
\tag{0.2}
$$

material cut odds：

$$
\boxed{
\frac d{dt}
\log
\frac a{1-a}
=
\nu
\frac{
J_A
}{
a(1-a)
}
+
3\Delta_A G_Q.
}
\tag{0.3}
$$

而 two-Gaussian heat witness顯示：

$$
\boxed{
\text{strictly positive density}
\not\Rightarrow
\text{uniformly positive conductance}.
}
$$

Round 24 STOP：

$$
\boxed{
\text{STOP-C28}
=
\text{Conductance-Restoration / Neck-Selection Gap}.
}
$$

---

# 1. Two separated critical-mass regions

令：

$$
A,B\subset\mathbb R^3
$$

為兩個 measurable / smooth regions，滿足：

$$
\boxed{
\operatorname{dist}(A,B)
=
R>0.
}
\tag{1.1}
$$

允許中間存在 low-mass neck：

$$
N
=
\mathbb R^3\setminus(A\cup B).
$$

定義：

$$
a
=
\mu_Q(A),
\qquad
b
=
\mu_Q(B).
$$

本輪不把：

$$
A,B
$$

視為 discrete graph nodes。

它們只是 continuous field中的兩個 testing regions。

---

# 2. Pressure source and nonlocal pressure Hessian

whole-space incompressible NS pressure滿足：

$$
\boxed{
-\Delta p
=
f_p
=
|S|^2
-
\frac12|\omega|^2.
}
\tag{2.1}
$$

所以：

$$
\boxed{
H_p
=
\nabla^2(-\Delta)^{-1}f_p.
}
\tag{2.2}
$$

Newtonian potential kernel：

$$
\Phi(z)
=
\frac1{4\pi|z|}
$$

給：

$$
\boxed{
\partial_i\partial_j\Phi(z)
=
\frac{
3z_iz_j-|z|^2\delta_{ij}
}{
4\pi|z|^5
}.
}
\tag{2.3}
$$

因此 away from source：

$$
\boxed{
|K_H(z)|
\lesssim
|z|^{-3}.
}
\tag{2.4}
$$

這是 algebraic nonlocal coupling。

---

# 3. Exact source-region split for pressure

因 operator：

$$
\nabla^2(-\Delta)^{-1}
$$

對 source：

$$
f_p
$$

linear，

可定義：

$$
f_p^A
=
\mathbf1_Af_p,
$$

$$
f_p^B
=
\mathbf1_Bf_p,
$$

$$
f_p^N
=
\mathbf1_Nf_p.
$$

則：

$$
\boxed{
H_p
=
H_p^A
+
H_p^B
+
H_p^N,
}
\tag{3.1}
$$

其中：

$$
H_p^B
=
\nabla^2(-\Delta)^{-1}f_p^B.
$$

對：

$$
x\in A,
$$

有：

$$
\boxed{
|H_p^B(x)|
\le
\frac{
C
}{
R^3
}
\|f_p\|_{L^1(B)}.
}
\tag{3.2}
$$

更高 derivative：

$$
\boxed{
|\nabla^mH_p^B(x)|
\le
\frac{
C_m
}{
R^{3+m}
}
\|f_p\|_{L^1(B)}.
}
\tag{3.3}
$$

---

# 4. Whole-space Biot–Savart cross coupling

對適當 decay的 divergence-free velocity：

$$
\boxed{
u
=
\nabla\times(-\Delta)^{-1}\omega.
}
\tag{4.1}
$$

三維 Biot–Savart kernel magnitude：

$$
|K_{BS}(z)|
\sim
|z|^{-2}.
$$

因此把 vorticity按 region分：

$$
\omega
=
\omega^A+\omega^B+\omega^N,
$$

並定義：

$$
u^B
=
\mathcal B[\omega^B].
$$

對：

$$
x\in A,
$$

有：

$$
\boxed{
|u^B(x)|
\le
\frac{
C
}{
R^2
}
\|\omega\|_{L^1(B)}.
}
\tag{4.2}
$$

而 cross velocity gradient / strain：

$$
S^B
=
\operatorname{sym}\nabla u^B
$$

滿足：

$$
\boxed{
|S^B(x)|
\le
\frac{
C
}{
R^3
}
\|\omega\|_{L^1(B)}.
}
\tag{4.3}
$$

所以：

$$
\boxed{
\text{velocity cross influence}
\sim
R^{-2},
\qquad
\text{strain / pressure-Hessian cross influence}
\sim
R^{-3}
}
$$

在沒有更高 multipole cancellation時。

---

# 5. Cross strain enters critical-mass selection directly

Round 21 critical-mass growth field：

$$
\boxed{
G_Q
=
\gamma_Q-\nu K_D,
}
\tag{5.1}
$$

其中：

$$
\boxed{
\gamma_Q
=
-
n^\top Sn.
}
\tag{5.2}
$$

對 region：

$$
A,
$$

split：

$$
S
=
S^A+S^B+S^N.
$$

定義：

$$
\boxed{
\gamma_{A\leftarrow B}(x)
=
-
n(x)^\top
S^B(x)
n(x),
\qquad
x\in A.
}
\tag{5.3}
$$

則：

$$
\boxed{
|\gamma_{A\leftarrow B}(x)|
\le
\frac{
C
}{
R^3
}
\|\omega\|_{L^1(B)}.
}
\tag{5.4}
$$

定義 conditional average：

$$
\boxed{
\Gamma_{A\leftarrow B}
=
\frac1a
\int_A
\gamma_{A\leftarrow B}
\,d\mu_Q.
}
\tag{5.5}
$$

所以：

$$
\boxed{
|\Gamma_{A\leftarrow B}|
\le
\frac{
C
}{
R^3
}
\|\omega\|_{L^1(B)}.
}
\tag{5.6}
$$

這是真正直接進入 Round 24 cut-selection contrast的 nonlocal cross term。

---

# 6. Cross pressure enters intermittency selection, not the critical-mass equation directly

必須區分：

- critical-mass selection：
  $$
  G_Q
  $$
  直接含 strain：
  $$
  -n^\top Sn;
  $$
- strain-measure relative source：
  $$
  \mathcal R_S
  $$
  才直接含：
  $$
  H_p.
  $$

所以 pressure的 virtual connection主要進入 Round 22–23 的 intermittency / source-selection channel。

對 continuous tilt：

$$
p\ge0,
$$

raw moment weight：

$$
w_p
=
r^{3-p}|S|^{p-2}.
$$

cross-pressure contribution：

$$
\boxed{
\mathcal P_p(A\leftarrow B)
=
-2
\int_A
w_p
S:H_p^B\,dx.
}
\tag{6.1}
$$

由 (3.2)：

$$
\boxed{
|\mathcal P_p(A\leftarrow B)|
\le
\frac{
C
}{
R^3
}
\|f_p\|_{L^1(B)}
\int_A
r^{3-p}
|S|^{p-1}dx.
}
\tag{6.2}
$$

所以 pressure relative-source亦跨過低 mass neck algebraically作用。

---

# 7. Local neck communication versus nonlocal interaction

Round 24 heat-type thin-neck model給：

$$
\boxed{
\mathcal D_{\rm neck}(R,t)
\lesssim
C_D(t)
\exp
\left[
-\frac{
R^2
}{
C\nu t
}
\right]
}
\tag{7.1}
$$

的 cross-neck communication scale。

而 nonlocal strain / pressure coupling在 first nonvanishing far-field multipole order：

$$
m\ge0
$$

時一般為：

$$
\boxed{
\mathcal C_{\rm nl}(R)
\sim
R^{-(3+m)}.
}
\tag{7.2}
$$

因此若對某 interaction channel存在：

$$
\boxed{
|\mathcal C_{\rm nl}(R)|
\ge
c_\ast
R^{-(3+m)}
}
\tag{7.3}
$$

對 large：

$$
R,
$$

則固定：

$$
t>0
$$

時：

$$
\boxed{
\frac{
|\mathcal C_{\rm nl}(R)|
}{
\mathcal D_{\rm neck}(R,t)
}
\to
\infty
\qquad
R\to\infty.
}
\tag{7.4}
$$

命名：

$$
\boxed{
\textbf{Algebraic-over-Gaussian Virtual-Coupling Regime}.
}
$$

---

# 8. Important limitation — algebraic upper bound is not a lower bound

Sections 3–4 的：

$$
R^{-3}
$$

是 robust upper-envelope decay。

但 signed multipole moments可以 cancellation。

所以不能從：

$$
\|f_p\|_{L^1(B)}
$$

或：

$$
\|\omega\|_{L^1(B)}
$$

單獨推出 nonzero：

$$
R^{-3}
$$

lower bound。

真正的 far-field order取決於：

$$
\boxed{
\text{first nonvanishing signed multipole}.
}
$$

因此：

$$
\boxed{
\text{nonlocal dominance}
}
$$

是一個 conditional geometric regime，

不是 universal theorem for every blob pair。

---

# 9. Virtual Coupling Dominance Ratio

令 Round 24 cut-diffusion odds rate：

$$
\boxed{
\mathcal D_A
=
\nu
\left|
\frac{
J_A
}{
a(1-a)
}
\right|.
}
\tag{9.1}
$$

對兩個 dominant regions：

$$
A,B,
$$

定義 cross-strain contrast rate：

$$
\boxed{
\mathcal C_{AB}^{S}
=
\left|
\Gamma_{A\leftarrow B}
-
\Gamma_{B\leftarrow A}
\right|.
}
\tag{9.2}
$$

當：

$$
\mathcal D_A>0,
$$

定義：

$$
\boxed{
\mathfrak V_{AB}
=
\frac{
3\mathcal C_{AB}^{S}
}{
\mathcal D_A
}.
}
\tag{9.3}
$$

若：

$$
\boxed{
\mathfrak V_{AB}\gg1,
}
\tag{9.4}
$$

則兩 region的 relative growth可被 nonlocal strain coupling影響得比 direct neck diffusion更強。

注意：

$$
\mathfrak V_{AB}
$$

不代表 mixing。

它只代表：

$$
\boxed{
\text{dynamical coupling}
>
\text{mass-exchange coupling}.
}
$$

---

# 10. Cross coupling is signed

假設：

$$
S^B(x)
$$

在 region：

$$
A
$$

非零。

因：

$$
\operatorname{tr}S^B=0,
$$

非零 symmetric strain tensor必有不同 sign的 spectral directions。

而：

$$
\gamma_{A\leftarrow B}
=
-
n^\top S^Bn.
$$

所以依 local optimal quotient direction：

$$
n,
$$

有可能：

$$
\boxed{
\gamma_{A\leftarrow B}>0
}
$$

或：

$$
\boxed{
\gamma_{A\leftarrow B}<0.
}
$$

因此 cross strain可以：

- amplify local critical mass；
- suppress local critical mass。

沒有 universal synchronizing sign。

---

# 11. Pressure Hessian kernel is anisotropic and sign-indefinite

對 point-like scalar source：

$$
f_p^B
\approx
M\delta_y,
$$

且：

$$
e
=
\frac{x-y}{|x-y|},
$$

有 far-field model：

$$
\boxed{
H_p^B(x)
\approx
\frac{
M
}{
4\pi R^3
}
\left(
3e\otimes e-I
\right).
}
\tag{11.1}
$$

tensor：

$$
3e\otimes e-I
$$

的 eigenvalues為：

$$
2,-1,-1.
$$

所以同一 source amplitude會對不同 strain orientation產生 opposite-sign contraction。

例如：

$$
e=e_1,
$$

$$
S_1
=
\operatorname{diag}(-2a,a,a)
$$

給：

$$
S_1:
(3e_1\otimes e_1-I)
<0.
$$

而：

$$
S_2
=
\operatorname{diag}(a,-2a,a)
$$

給 opposite sign。

因此：

$$
\boxed{
\textbf{
nonlocal pressure coupling is not a positive synchronization kernel.
}
}
\tag{11.2}
$$

---

# 12. Virtual connection does not imply a Cheeger gap

Cheeger conductance：

$$
h_Q
$$

測量：

$$
\boxed{
\text{critical mass crossing weighted cuts}.
}
$$

nonlocal strain / pressure kernels測量：

$$
\boxed{
\text{field influence across geometric separation}.
}
$$

後者不需要：

$$
m_Q
$$

真的穿過 neck。

所以完全可以同時有：

$$
\boxed{
h_Q\ll1
}
$$

以及：

$$
\boxed{
\mathcal C_{\rm nl}\neq0.
}
$$

因此：

$$
\boxed{
\textbf{Virtual Dynamical Connectivity}
\neq
\textbf{Positive Mass Conductance}.
}
\tag{12.1}
$$

這是本輪最重要的 conceptual distinction。

---

# 13. Duplex connectivity state

Round 24 只追：

$$
h_Q.
$$

本輪顯示 NS connectivity至少需要兩層：

$$
\boxed{
X_{\rm duplex}
=
\left\langle
h_Q,
\mathscr I_Q(s),
\mathcal C_{AB}^{S},
\mathcal P_p(A\leftarrow B),
\mathfrak V_{AB}
\right\rangle.
}
\tag{13.1}
$$

其中：

## Layer M — mass connectivity

$$
\boxed{
h_Q,\quad
\mathscr I_Q(s).
}
$$

是 positive / metric mixing carrier。

## Layer N — nonlocal field connectivity

$$
\boxed{
\mathcal C_{AB}^{S},
\quad
\mathcal P_p.
}
$$

是 signed dynamical coupling carrier。

這兩層不能彼此取代。

---

# 14. Exact cross-selection split across a cut

令：

$$
A^c
$$

作為 source complement。

由 Biot–Savart linearity：

$$
S
=
S^A+S^{A^c}.
$$

在：

$$
A
$$

上：

$$
\gamma_Q
=
-
n^\top S^An
-
n^\top S^{A^c}n.
$$

定義：

$$
\boxed{
\langle\gamma^{\rm cross}\rangle_A
=
-\frac1a
\int_A
n^\top S^{A^c}n
\,d\mu_Q.
}
\tag{14.1}
$$

及：

$$
\boxed{
\langle\gamma^{\rm cross}\rangle_{A^c}
=
-\frac1{1-a}
\int_{A^c}
n^\top S^An
\,d\mu_Q.
}
\tag{14.2}
$$

所以 Round 24 selection contrast：

$$
\Delta_A G_Q
$$

含 exact nonlocal piece：

$$
\boxed{
\Delta_A G_Q^{\rm cross}
=
\langle\gamma^{\rm cross}\rangle_A
-
\langle\gamma^{\rm cross}\rangle_{A^c}.
}
\tag{14.3}
$$

因此 cut odds equation可寫：

$$
\boxed{
\ell_A'
=
\mathcal D_A^{\rm signed}
+
3\Delta_A G_Q^{\rm local}
+
3\Delta_A G_Q^{\rm cross}
+
3\Delta_A G_Q^{\rm gauge/diff}.
}
\tag{14.4}
$$

這是 virtual connection直接進入 critical-mass separation dynamics的位置。

---

# 15. Nonlocal coupling can synchronize or anti-synchronize

若：

$$
\Delta_A G_Q^{\rm cross}
$$

與：

$$
-\ell_A
$$

同號，

它傾向降低兩側 mass imbalance：

$$
\boxed{
\text{synchronizing virtual coupling}.
}
$$

若與：

$$
\ell_A
$$

同號，

它傾向增加 mass imbalance：

$$
\boxed{
\text{anti-synchronizing virtual coupling}.
}
$$

由 Sections 10–11：

$$
\boxed{
\text{兩種 sign皆被 local tensor geometry允許}.
}
$$

所以 nonlocality本身不是 regularity mechanism。

需要額外：

$$
\boxed{
\text{sign coherence / depletion geometry}.
}
$$

---

# 16. Pressure cross interaction returns Round 04 in a sharper form

Round 04 obstruction：

$$
\boxed{
\text{local geometry / nonlocal pressure closure gap}.
}
$$

Round 25 現在知道：

pressure nonlocality在 low-conductance regime並不是純障礙。

它還可能是：

$$
\boxed{
\text{cross-blob communication channel}.
}
$$

但因 kernel sign-indefinite，

它同時可能：

- synchronize；
- de-synchronize；
- rotate local strain geometry；
- bias high-$K$ relative source。

所以 Round 04 的 Boss被重新分類成：

$$
\boxed{
\textbf{nonlocal signed coupling rather than merely nonlocal nuisance}.
}
$$

---

# 17. Pressure self-adjoint reciprocity does not give positivity

operator：

$$
\nabla^2(-\Delta)^{-1}
$$

是 Fourier multiplier matrix：

$$
-\frac{
\xi\otimes\xi
}{
|\xi|^2
}
$$

up to sign convention。

它具有 self-adjoint / reciprocal structure。

但：

$$
3e\otimes e-I
$$

有 mixed signs。

因此：

$$
\boxed{
\text{reciprocity}
\neq
\text{positive coupling}.
}
\tag{17.1}
$$

所以不能從 pressure operator的 symmetric character直接推出：

$$
h_Q
$$

restoration。

---

# 18. Algebraic virtual connection versus exponential neck

把 Round 24 與本輪合併：

$$
\boxed{
\begin{array}{c|c}
\text{channel}
&
\text{large-separation scale}
\\
\hline
\text{local viscous neck}
&
\exp[-R^2/(C\nu t)]
\\
\text{cross velocity}
&
R^{-2}
\\
\text{cross strain}
&
R^{-3}
\\
\text{cross pressure Hessian}
&
R^{-3}
\end{array}
}
\tag{18.1}
$$

這個表不是 universal lower bound table。

它是：

- heat communication的 model scale；
- whole-space kernel的 far-field envelope / nonvanishing-multipole scale。

在 nonzero cross multipole branch，

large separation可形成：

$$
\boxed{
\text{weak mass conductance}
+
\text{comparatively stronger nonlocal field interaction}.
}
\tag{18.2}
$$

---

# 19. Translation-invariant norms miss both separation and cross sign

Round 24 已指出：

translation-invariant norms不記錄 blob separation：

$$
R.
$$

Round 25 再增加：

它們通常也不記錄：

$$
\boxed{
\text{relative orientation / signed kernel phase}.
}
$$

所以相同：

- $L^p$ amplitudes；
- energy；
- enstrophy；
- critical quotient norm；

可以對應不同：

$$
\mathcal C_{AB}^{S}
$$

sign與 magnitude。

因此 conductance/nonlocal coupling需要真正 relational observation：

$$
\boxed{
\mathsf O_{\mathsf X}.
}
$$

---

# 20. Nonlocal interaction-to-mixing transduction gap

要讓 virtual coupling真正修復 Round 24 的：

$$
h_Q\ll1,
$$

需要的不只是：

$$
\mathcal C_{\rm nl}\neq0.
$$

還要證：

$$
\boxed{
\text{signed nonlocal field interaction}
\Longrightarrow
\text{positive neck mass restoration}.
}
$$

也就是：

$$
\boxed{
\text{interaction}
\to
\text{selection synchronization}
\to
\text{mass redistribution}
\to
\text{conductance increase}.
}
\tag{20.1}
$$

目前第一箭頭本身就沒有 universal sign。

所以 virtual connection不是現成的 spectral-gap proof。

---

# 21. STOP-C29 — Virtual-Connectivity / Sign-Coherence Transduction Gap

定義：

$$
\boxed{
\bot_X^{\mathrm{C29}}
=
\left\langle
\begin{array}{l}
\text{layer}
=
\mathrm{nonlocal\ cross\text{-}blob\ coupling},
\\
\text{mass\ connectivity}
=
h_Q,\ \mathscr I_Q,
\\
\text{cross\ velocity}
\sim
R^{-2},
\\
\text{cross\ strain}
\sim
R^{-3},
\\
\text{cross\ pressure\ Hessian}
\sim
R^{-3},
\\
\text{neck\ diffusion}
\sim
\exp[-R^2/(C\nu t)]
\text{ in heat-type separation model},
\\
\text{virtual\ dominance}
=
\mathrm{possible\ under\ nonzero\ multipole},
\\
\text{coupling\ sign}
=
\mathrm{indefinite},
\\
\text{virtual\ connectivity}
\neq
\text{positive\ conductance},
\\
\text{missing}
=
\mathrm{sign\ coherence\ and\ interaction\text{-}to\text{-}mixing\ transduction},
\\
\text{essential\ discrete\ intrusion}
=
\mathrm{false}.
\end{array}
\right\rangle.
}
$$

命名：

$$
\boxed{
\textbf{STOP-C29:
Virtual-Connectivity / Sign-Coherence Transduction Gap}.
}
$$

---

# 22. 24/72 Ledger — Round 25

| Step | object | $B$ | $U$ | $O$ | $L$ | status |
|---|---|---|---|---|---|---|
| C324 | separated continuous regions $A,B$ | $\mathsf C$ | relational partition | $\mathsf X$ | $\mathsf F$ | FORM |
| C325 | pressure Hessian kernel | $\mathsf C$ | nonlocal integral | relational | $\mathsf F$ | EXACT |
| C326 | pressure source-region split | $\mathsf C$ | linear source split | $\mathsf X$ | $\mathsf F$ | EXACT |
| C327 | $R^{-3}$ cross-pressure bound | $\mathsf C$ | kernel estimate | scalar | $\mathsf F$ | PROVED |
| C328 | Biot–Savart cross velocity | $\mathsf C$ | nonlocal integral | relational | $\mathsf F$ | EXACT |
| C329 | $R^{-2}/R^{-3}$ cross bounds | $\mathsf C$ | kernel estimate | scalar | $\mathsf F$ | PROVED |
| C330 | cross strain in $G_Q$ | $\mathsf C$ | selection coupling | targeted | $\mathsf F$ | EXACT |
| C331 | cross pressure in $\mathcal R_S$ | $\mathsf C$ | tilt/source coupling | targeted | $\mathsf F$ | EXACT |
| C332 | algebraic-over-Gaussian regime | $\mathsf C$ | asymptotic comparison | scalar | $\mathsf F$ | CONDITIONAL PROVED |
| C333 | virtual dominance ratio | $\mathsf C$ | recognition | scalar | $\mathsf F$ | FORM |
| C334 | strain cross sign | $\mathsf C$ | tensor geometry | relational | $\mathsf F$ | INDEFINITE |
| C335 | pressure cross sign | $\mathsf C$ | Hessian kernel geometry | relational | $\mathsf F$ | INDEFINITE |
| C336 | virtual connectivity $\Rightarrow$ gap | $\mathsf C$ | mixing geometry | targeted | $\mathsf F$ | REFUTED as automatic implication |
| C337 | duplex connectivity state | $\mathsf C$ | coupled observation | $\mathsf X$ | $\mathsf F$ | FORM |
| C338 | exact cut cross-selection split | $\mathsf C$ | Biot–Savart/selection | targeted | $\mathsf F$ | EXACT |
| C339 | interaction-to-mixing transduction | $\mathsf C$ | global feedback | targeted | $\mathsf F$ | OPEN / STOP-C29 |

---

# 23. Continuous-versus-discrete status

本輪天然容易被畫成：

$$
\text{blob A}
\leftrightarrow
\text{blob B}.
$$

但這不代表我們已經需要 graph substrate。

所有 operations仍然是：

- continuous source partitions；
- continuous singular-integral kernels；
- continuous region averages；
- continuous weighted cuts；
- continuous separation parameter：
  $$
  R.
  $$

因此：

$$
\boxed{
T_{\mathsf C\to\mathsf D}
=
\text{NOT YET REACHED}.
}
\tag{23.1}
$$

如果未來把 blobs變成 graph vertices，

首先只是 coarse-grained representation。

除非可以證明 signed kernel interaction的 closure必須記錄離散 component identity，

否則還不能算 essential：

$$
\mathsf C\to\mathsf D.
$$

---

# 24. Strongest results of Round 25

## R25-A — nonlocal cross-field bounds

$$
\boxed{
|u^{B\to A}|
\lesssim
R^{-2}
\|\omega\|_{L^1(B)},
}
$$

$$
\boxed{
|S^{B\to A}|
\lesssim
R^{-3}
\|\omega\|_{L^1(B)},
}
$$

$$
\boxed{
|H_p^{B\to A}|
\lesssim
R^{-3}
\|f_p\|_{L^1(B)}.
}
$$

## R25-B — nonlocal interaction can outlive the neck

conditional nonzero-multipole branch：

$$
\boxed{
\frac{
\text{algebraic nonlocal coupling}
}{
\text{Gaussian neck communication}
}
\to\infty
}
$$

for fixed positive time and large separation。

## R25-C — cross coupling has no universal sign

$$
\boxed{
\text{strain kernel coupling}
\quad\text{and}\quad
\text{pressure-Hessian coupling}
}
$$

can both amplify or suppress depending geometry。

## R25-D — connectivity duplex

$$
\boxed{
\text{mass conductance}
\neq
\text{nonlocal dynamical connectivity}.
}
$$

---

# 25. Next round — signed-kernel coherence

現在真正剩下：

$$
\boxed{
\text{sign coherence}.
}
$$

下一輪不再問：

> nonlocal coupling存不存在？

而問：

$$
\boxed{
\textbf{
Can incompressibility, strain geometry, or critical-mass tilt
force the signed cross-kernel interaction to be predominantly synchronizing
on dangerous branches?
}
}
$$

具體：

1. 對 cross strain定義 continuous signed coherence：
   $$
   \mathfrak c_S(A,B);
   $$

2. 對 pressure Hessian定義：
   $$
   \mathfrak c_P^{(p)}(A,B);
   $$

3. 把 kernel orientation與：
   $$
   n,\quad
   \widehat S,\quad
   \omega
   $$
   對齊幾何納入；

4. 測 dangerous middle-strain branch：
   $$
   \lambda_2>0
   $$
   是否偏向某種 nonlocal sign；

5. 若 sign仍可完全自由，則 virtual connection只能是 signed transport network，不能閉合 conductance；

6. 若 sign在 high-$K$/high-$\lambda_2$ tilt下出現 bias，則可接回 Round 22 tilt-selection law。

---

# 26. External primary-source anchors

1. Borys Álvarez-Samaniego, Wilson P. Álvarez-Samaniego, Pedro G. Fernández-Dalgo, *On the use of the Riesz transforms to determine the pressure term in the incompressible Navier-Stokes equations on the whole space*, arXiv:2004.02588.
   - whole-space pressure由 Riesz transforms of $u_i u_j$決定的 primary-source背景。

2. Maurizio Carbone, Michele Iovieno, Andrew D. Bragg, *Gauge symmetry and dimensionality reduction of the anisotropic pressure Hessian*, arXiv:1911.08652.
   - anisotropic pressure Hessian作為 velocity-gradient dynamics中的 nonlocal functional之 primary-source背景。

本輪 pressure-kernel far-field bound、cross-region source split、virtual-dominance comparison、signed pressure witness與 duplex-connectivity distinction均為本文直接推導。

---

# 27. Commit state

$$
\boxed{
\begin{aligned}
\text{Route}
&=
\mathrm{Pure\ Continuous\ Nonlocal\ Cross\text{-}Blob\ Coupling},
\\
\text{Essential }\mathsf C\to\mathsf D
&=
\mathrm{Not\ reached},
\\
\text{Mass connectivity}
&=
h_Q,
\\
\text{Nonlocal connectivity}
&=
\mathcal C_{AB}^{S}
+
\mathcal P_p(A\leftarrow B),
\\
\text{Far-field coupling}
&=
\mathrm{algebraic},
\\
\text{Neck diffusion}
&=
\mathrm{Gaussian/exponential\ in\ separation\ model},
\\
\text{Virtual dominance}
&=
\mathrm{possible},
\\
\text{Universal synchronizing sign}
&=
\mathrm{false},
\\
\text{STOP-C29}
&=
\mathrm{Virtual\text{-}Connectivity/Sign\text{-}Coherence\ Transduction\ Gap},
\\
\text{Next}
&=
\mathrm{Signed\text{-}Kernel\ Coherence}.
\end{aligned}
}
$$
