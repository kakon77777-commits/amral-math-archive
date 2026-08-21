# NS × X 積分 × 24/72 範式實戰
## Round 28 — Pure Continuous Lock-Manifold Stability / Dual-Strain Saddle Route

- 日期：2026-08-17
- 版本：v0.1
- 狀態：Proof-Route Experiment / Continuous-Only Lock-Stability Branch
- canonical source：UTF-8 Markdown
- canonical math delimiters：inline `$...$`；display `$$...$$`
- 前一輪：`NS_X72_Round27_PureContinuous_CoherenceDynamics_AngularPhaseLocking_v0.1_2026-08-17.md`
- 本輪目標：Round 27 已證 sustained signed nonlocal coupling需要 angular phase locking或強 modulation。本輪對 lock manifold做真正線性化，首先抽出 frozen-strain principal dynamics，再加入 moving eigenframe、viscosity、vorticity、pressure與 quotient gauge forcing。檢驗 amplification-sign lock是否 attracting、repelling、saddle或 forced-neutral。
- 非主張：本文沒有證明 actual Navier–Stokes dangerous trajectories的 lock manifold必 unstable，也沒有證明 intermediate-eigenvector alignment不可穩定。本文證明的是 frozen-strain leading subsystem具有 exact dual stability與 common-lock saddle結構；actual stability完全取決於額外 frame/gauge/nonlocal forcing是否能改寫這個 leading saddle。

---

# 0. Round 27 handoff

Round 27 建立：

$$
\boxed{
\mathcal C(t)=A(t)\cos\theta(t)
}
$$

型 signed coupling，以及 nonstationary angular cancellation：

$$
|\theta'|\ge\Omega>0
\Longrightarrow
\text{cumulative signed coupling被 }O(\Omega^{-1})\text{ 抑制},
$$

除非 amplitude或 phase-speed modulation很強。

同時 strain eigenframe rotation：

$$
\boxed{
D_te_i
=
\sum_{j\ne i}
\frac{
\nu e_j^\top\Delta S e_i
-\frac14(\omega\cdot e_j)(\omega\cdot e_i)
-e_j^\top H_pe_i
}{
\lambda_i-\lambda_j
}
e_j.
}
\tag{0.1}
$$

其中：

$$
-S^2
$$

沒有 direct off-diagonal frame rotation。

Round 27 STOP：

$$
\boxed{
\text{STOP-C31}
=
\text{Angular Phase-Locking / Coherence-Persistence Gap}.
}
$$

---

# 1. Frozen-strain vorticity-direction subsystem

先取一個 fixed symmetric trace-free strain：

$$
S=S^\top,
$$

eigenpairs：

$$
Se_i=\lambda_ie_i,
\qquad
\lambda_1<\lambda_2<\lambda_3.
$$

忽略：

- eigenframe rotation；
- viscosity；
- pressure forcing through frame motion。

vorticity direction：

$$
\xi=\frac{\omega}{|\omega|}
$$

的 leading dynamics：

$$
\boxed{
\dot\xi
=
P_\xi^\perp S\xi
=
S\xi
-
(\xi^\top S\xi)\xi.
}
\tag{1.1}
$$

令：

$$
\sigma
=
\xi^\top S\xi.
$$

---

# 2. Vorticity direction is a Rayleigh-quotient ascent

由 (1.1)：

$$
\boxed{
\dot\sigma
=
2
\left(
|S\xi|^2-\sigma^2
\right)
\ge0.
}
\tag{2.1}
$$

等號恰在：

$$
S\xi\parallel\xi,
$$

即 strain eigenvector方向。

所以 frozen-strain vorticity direction是 sphere上 Rayleigh quotient：

$$
\xi^\top S\xi
$$

的 gradient-ascent flow。

---

# 3. Linear stability near a strain eigenvector

令：

$$
\xi
=
e_i
+
\sum_{j\ne i}
\varepsilon_j e_j
+
O(|\varepsilon|^2).
$$

由 (1.1)：

$$
\boxed{
\dot\varepsilon_j
=
(\lambda_j-\lambda_i)
\varepsilon_j
+
O(|\varepsilon|^2).
}
\tag{3.1}
$$

因此：

## alignment with $e_3$

$$
\lambda_j-\lambda_3<0
\qquad
(j=1,2),
$$

所以：

$$
\boxed{
e_3
\text{ is locally attracting for frozen-strain vorticity direction}.
}
\tag{3.2}
$$

## alignment with $e_1$

$$
\lambda_j-\lambda_1>0
\qquad
(j=2,3),
$$

所以：

$$
\boxed{
e_1
\text{ is repelling}.
}
\tag{3.3}
$$

## alignment with $e_2$

一個 transverse exponent為負、一個為正：

$$
\boxed{
e_2
\text{ is a saddle}.
}
\tag{3.4}
$$

---

# 4. Why observed intermediate alignment is genuinely dynamical

Section 3只描述：

$$
\boxed{
\text{frozen eigenframe + leading strain action}.
}
$$

actual NS：

- eigenframe rotates；
- pressure Hessian進入 eigenframe dynamics；
- viscosity進入 vorticity direction；
- strain itself evolves；
- material stretching history matters。

因此：

$$
\boxed{
\text{instantaneous }e_2\text{ alignment}
}
$$

不等同於 frozen-$S$ attracting fixed point。

若 actual dynamics偏向：

$$
e_2,
$$

它必使用 frozen-strain subsystem之外的 structure。

---

# 5. Frozen-strain optimal-quotient-direction subsystem

Round 27 quotient direction equation：

$$
D_tn
=
\nu P_n^\perp[\cdots]
-
P_n^\perp Sn
+
\frac12\omega\times n
+
r^{-1}P_n^\perp\nabla\chi_g.
$$

只保留 frozen strain principal term：

$$
\boxed{
\dot n
=
-
P_n^\perp Sn
=
-
Sn
+
(n^\top Sn)n.
}
\tag{5.1}
$$

令：

$$
\tau
=
n^\top Sn.
$$

---

# 6. Quotient direction is a Rayleigh-quotient descent

由 (5.1)：

$$
\boxed{
\dot\tau
=
-2
\left(
|Sn|^2-\tau^2
\right)
\le0.
}
\tag{6.1}
$$

所以 quotient direction的 strain-only dynamics是同一 Rayleigh quotient的 gradient-descent flow。

因此：

$$
\boxed{
\xi
\text{ climbs strain Rayleigh quotient},
\qquad
n
\text{ descends it}.
}
\tag{6.2}
$$

命名：

$$
\boxed{
\textbf{Dual Strain Gradient-Flow Structure}.
}
$$

---

# 7. Quotient-direction eigenvector stability

令：

$$
n
=
e_i
+
\sum_{j\ne i}
\eta_j e_j
+
O(|\eta|^2).
$$

由 (5.1)：

$$
\boxed{
\dot\eta_j
=
(\lambda_i-\lambda_j)
\eta_j
+
O(|\eta|^2).
}
\tag{7.1}
$$

所以：

$$
\boxed{
e_1
\text{ attracts }n,
}
\tag{7.2}
$$

$$
\boxed{
e_3
\text{ repels }n,
}
\tag{7.3}
$$

而：

$$
\boxed{
e_2
\text{ is again a saddle}.
}
\tag{7.4}
$$

這與 vorticity-direction stability完全對偶。

---

# 8. Exact strain-only alignment equation between $\xi$ and $n$

定義：

$$
\boxed{
q
=
\xi\cdot n.
}
\tag{8.1}
$$

使用：

$$
\dot\xi
=
S\xi-\sigma\xi,
$$

及：

$$
\dot n
=
-Sn+\tau n,
$$

由 $S$ symmetric：

$$
n\cdot S\xi
=
\xi\cdot Sn.
$$

所以 cross terms cancel：

$$
\boxed{
\dot q
=
(\tau-\sigma)q.
}
\tag{8.2}
$$

因此：

- $q=0$ 為 invariant；
- $q=\pm1$ 若同時位於同一 eigenvector則固定；
- alignment growth由兩個方向看到的 strain Rayleigh quotient差決定。

---

# 9. Common eigenvector lock has paired opposite exponents

考慮 common lock：

$$
\xi=n=e_i.
$$

對某 transverse direction：

$$
e_j,
\qquad
j\ne i,
$$

vorticity perturbation：

$$
\boxed{
\dot\varepsilon_j
=
(\lambda_j-\lambda_i)\varepsilon_j.
}
$$

quotient-direction perturbation：

$$
\boxed{
\dot\eta_j
=
-(\lambda_j-\lambda_i)\eta_j.
}
$$

所以每個 transverse strain gap：

$$
\Delta_{ji}
=
\lambda_j-\lambda_i
$$

產生一對：

$$
\boxed{
+\Delta_{ji},
\qquad
-\Delta_{ji}.
}
\tag{9.1}
$$

若 spectrum simple：

$$
\Delta_{ji}\ne0.
$$

因此 common lock transverse subsystem必有一個 growing mode與一個 decaying mode。

---

# 10. Dual-Strain Common-Lock Saddle Theorem

由 Section 9：

$$
\boxed{
\textbf{
in the frozen-strain principal subsystem,
a common lock }\xi=n=e_i
\textbf{ is never asymptotically attracting for simple strain spectrum.}
}
\tag{10.1}
$$

更精確：

$$
\boxed{
\text{transverse Lyapunov exponents occur in }\pm|\lambda_j-\lambda_i|\text{ pairs}.
}
\tag{10.2}
$$

所以 common vorticity–quotient-direction lock需要額外 dynamics才可能 stabilise。

---

# 11. Middle-eigenvector common lock is doubly saddle-like

對：

$$
i=2,
$$

vorticity：

$$
\lambda_1-\lambda_2<0,
\qquad
\lambda_3-\lambda_2>0.
$$

quotient direction剛好反號：

$$
\lambda_2-\lambda_1>0,
\qquad
\lambda_2-\lambda_3<0.
$$

所以在：

$$
e_2
$$

附近：

- $\xi$ 有一穩一不穩；
- $n$ 也有一穩一不穩；
- unstable transverse directions互補。

因此：

$$
\boxed{
\textbf{
simultaneous }\xi\approx n\approx e_2
\textbf{ requires genuine multi-frame balancing}.
}
}
\tag{11.1}
$$

---

# 12. Moving-eigenframe coefficient equations

回到 actual NS。

定義：

$$
a_i
=
\xi\cdot e_i,
$$

$$
b_i
=
n\cdot e_i.
$$

令 eigenframe angular-velocity coefficients：

$$
\boxed{
\Omega_{ji}
=
e_j\cdot D_te_i,
}
\tag{12.1}
$$

則：

$$
\Omega_{ji}
=
-\Omega_{ij}.
$$

由 Round 27：

$$
\boxed{
\Omega_{ji}
=
\frac{
\nu e_j^\top\Delta S e_i
-\frac14(\omega\cdot e_j)(\omega\cdot e_i)
-e_j^\top H_pe_i
}{
\lambda_i-\lambda_j
}
}
\tag{12.2}
$$

for：

$$
j\ne i.
$$

---

# 13. Exact vorticity coefficients in the moving eigenframe

令：

$$
\mathcal V_\omega
=
\nu
P_\xi^\perp
\frac{\Delta\omega}{|\omega|}.
$$

則：

$$
\boxed{
D_ta_i
=
(\lambda_i-\sigma)a_i
+
e_i\cdot\mathcal V_\omega
+
\sum_j
a_j\Omega_{ji}.
}
\tag{13.1}
$$

所以 frozen-strain stability exponent：

$$
\lambda_i-\sigma
$$

現在被：

- viscous angular forcing；
- eigenframe rotation；

持續驅動。

---

# 14. Exact quotient coefficients in the moving eigenframe

定義非-strain quotient angular forcing：

$$
\boxed{
\begin{aligned}
\mathcal F_n
={}&
\nu
P_n^\perp
[
\Delta n+2\nabla\log r\cdot\nabla n]
\\
&+
\frac12\omega\times n
+
\frac1r
P_n^\perp\nabla\chi_g.
\end{aligned}
}
\tag{14.1}
$$

則：

$$
D_tn
=
-P_n^\perp Sn
+
\mathcal F_n.
$$

因此：

$$
\boxed{
D_tb_i
=
-(\lambda_i-\tau)b_i
+
e_i\cdot\mathcal F_n
+
\sum_j
b_j\Omega_{ji}.
}
\tag{14.2}
$$

actual quotient-direction lock可被：

- viscosity；
- vorticity rotation；
- gauge feedback；
- eigenframe rotation；

重新穩定或重新 destabilize。

---

# 15. Linearized forced common-lock system

在：

$$
\xi\approx n\approx e_i
$$

附近，對：

$$
j\ne i,
$$

令 transverse variables：

$$
z_j
=
\begin{pmatrix}
a_j\\
b_j
\end{pmatrix}.
$$

leading linear part：

$$
\boxed{
D_tz_j
=
\begin{pmatrix}
\lambda_j-\lambda_i & 0\\
0 & \lambda_i-\lambda_j
\end{pmatrix}
z_j
+
F_j
+
\mathcal C_jz
+
O(|z|^2).
}
\tag{15.1}
$$

其中：

$$
F_j
$$

收集 lock-point上的：

- viscous vorticity-direction forcing；
- quotient gauge/vorticity/viscous forcing；
- eigenframe forcing；

而：

$$
\mathcal C_j
$$

收集其一階變分與 mode coupling。

principal matrix trace：

$$
0,
$$

determinant：

$$
\boxed{
-(\lambda_j-\lambda_i)^2<0.
}
\tag{15.2}
$$

所以額外 forcing / coupling若要讓 common lock stable，必須真正改寫 principal saddle。

---

# 16. Spectral collision is a separate degeneracy channel

當：

$$
|\lambda_i-\lambda_j|
\to0,
$$

frozen-strain saddle exponent：

$$
|\lambda_i-\lambda_j|
$$

變小。

但 Round 27 eigenframe rotation係數：

$$
\Omega_{ji}
$$

同時含：

$$
\frac1{\lambda_i-\lambda_j}.
$$

所以 near spectral collision：

$$
\boxed{
\text{principal alignment attraction/repulsion weakens,
while frame sensitivity can strengthen}.
}
\tag{16.1}
$$

因此 simple-spectrum linearization不能 uniform延伸到 eigenvalue collision。

這是 continuous spectral-degeneracy branch，不是離散 intrusion。

---

# 17. Pressure-coherence lock needs a tangent error, not only $c$

Round 27 pressure tensor coherence：

$$
c_P
=
\widehat S:\widehat{\mathbb Q}_P.
$$

在 perfect lock：

$$
c_P=1.
$$

但若：

$$
\widehat S=\widehat{\mathbb Q}_P,
$$

因兩者 tangent velocities都 orthogonal於自身，

立即有：

$$
\boxed{
\dot c_P=0
}
\tag{17.1}
$$

不論 lock是否 stable。

所以 scalar：

$$
c_P
$$

在 perfect lock處沒有一階 stability資訊。

真正需要 tangent-space error：

$$
\boxed{
\delta_P
=
\widehat{\mathbb Q}_P-\widehat S.
}
\tag{17.2}
$$

且：

$$
\boxed{
1-c_P
=
\frac12|\delta_P|^2.
}
\tag{17.3}
$$

---

# 18. Generic tangent lock-error equation

令：

$$
U=\widehat S,
\qquad
V=\widehat{\mathbb Q}_P,
$$

且：

$$
\delta=V-U.
$$

則 exact：

$$
\boxed{
\frac12
\frac d{dt}
|\delta|^2
=
\delta:
(\dot V-\dot U).
}
\tag{18.1}
$$

在 lock manifold：

$$
U=V,
$$

若：

$$
\boxed{
\dot V-\dot U\ne0,
}
\tag{18.2}
$$

則 tangent vector error立即被 forced離開 lock。

若：

$$
\dot V-\dot U=0
$$

on the manifold，

才需要研究 linearized relative angular operator：

$$
\boxed{
\dot\delta
=
\mathcal J_{\rm rel}\delta
+
O(|\delta|^2).
}
\tag{18.3}
$$

lock locally attracting的必要條件是：

$$
\boxed{
\lambda_{\max}
\left(
\operatorname{sym}\mathcal J_{\rm rel}
\right)
<0.
}
\tag{18.4}
$$

---

# 19. No universal sign for the relative angular Jacobian

Round 27 已知：

$$
D_t\widehat S
$$

含：

- pressure Hessian；
- vorticity dyad；
- viscosity；
- self-amplification shape term。

remote quadrupole dynamics又含：

- source motion；
- line-of-sight motion；
- remote source reorientation；
- amplitude normalization。

這些 terms沒有 universal sign relation。

因此沒有只由：

$$
\lambda_2>0,
\quad
Q,
\quad
|S|,
\quad
|\omega|
$$

就推出：

$$
\boxed{
\operatorname{sym}\mathcal J_{\rm rel}
\le
-\kappa I
}
\tag{19.1}
$$

的 purely algebraic universal statement。

---

# 20. Neutral-lock structural witness

考慮 local structural model：

- $S$ constant；
- eigenframe fixed；
- line of sight：
  $$
  e
  $$
  fixed；
- remote quadrupole fixed。

則：

$$
\widehat S,
\qquad
\widehat{\mathbb Q}_P
$$

皆 constant。

因此：

$$
\boxed{
\dot c_P=0
}
$$

對所有 initial coherence。

所以可以有：

$$
\boxed{
\text{neutral persistent amplification-sign coherence}
}
$$

而沒有 restoring或dephasing。

此 witness不是 whole-space finite-energy NS solution。

它排除的是：

$$
\boxed{
\text{all nontrivial locks are automatically unstable}
}
$$

這種純幾何推論。

---

# 21. Conditional lock-stability lemma

考慮 tangent lock error：

$$
z(t)
$$

滿足：

$$
\boxed{
z'
=
A(t)z+f(t).
}
\tag{21.1}
$$

若：

$$
\boxed{
\lambda_{\max}
\left(
\frac{
A+A^\top
}{2}
\right)
\le
-\kappa(t)
}
\tag{21.2}
$$

且：

$$
\kappa(t)\ge0,
$$

則：

$$
\boxed{
\frac d{dt}|z|
\le
-\kappa(t)|z|
+
|f(t)|.
}
\tag{21.3}
$$

因此：

$$
\boxed{
|z(t)|
\le
e^{-\int_{t_0}^t\kappa}
|z(t_0)|
+
\int_{t_0}^t
e^{-\int_s^t\kappa}
|f(s)|ds.
}
\tag{21.4}
$$

所以 stable phase lock需要兩件事：

1. negative transverse angular Jacobian；
2. small off-manifold forcing。

---

# 22. Lock-attraction margin

定義：

$$
\boxed{
\kappa_{\rm lock}(t)
=
-
\lambda_{\max}
\left(
\operatorname{sym}\mathcal J_{\rm rel}(t)
\right).
}
\tag{22.1}
$$

interpretation：

$$
\kappa_{\rm lock}>0
$$

代表 instantaneous attraction；

$$
\kappa_{\rm lock}<0
$$

代表 instantaneous transverse instability；

$$
\kappa_{\rm lock}=0
$$

代表 neutral/center direction。

再定義 forcing ratio：

$$
\boxed{
\mathfrak F_{\rm lock}
=
\frac{
|f|
}{
\kappa_{\rm lock}|z|
}
}
\tag{22.2}
$$

於：

$$
\kappa_{\rm lock}>0,\quad z\ne0.
$$

若：

$$
\mathfrak F_{\rm lock}\ll1,
$$

lock attraction主導。

---

# 23. Frozen-strain common lock has negative attraction margin

Section 10 的 common lock principal matrix：

$$
A_j
=
\begin{pmatrix}
\Delta_{ji} & 0\\
0 & -\Delta_{ji}
\end{pmatrix}.
$$

其 symmetric part就是自身。

所以：

$$
\lambda_{\max}
=
|\Delta_{ji}|.
$$

因此：

$$
\boxed{
\kappa_{\rm lock}^{\rm frozen}
=
-|\lambda_j-\lambda_i|
<0.
}
\tag{23.1}
$$

對 simple spectrum。

也就是 frozen-strain common lock不是 marginal：

$$
\boxed{
\textbf{它是 genuine saddle instability.}
}
$$

---

# 24. Stabilization burden

若 actual NS 要把：

$$
\xi\approx n\approx e_i
$$

的 common lock變成 attracting，

additional angular dynamics必須至少提供 transverse correction超過：

$$
\boxed{
|\lambda_j-\lambda_i|
}
$$

的 unstable gap rate。

所以 stabilizing burden可寫成：

$$
\boxed{
\mathcal D_{\rm extra}
\gtrsim
|\lambda_j-\lambda_i|.
}
\tag{24.1}
$$

其中：

$$
\mathcal D_{\rm extra}
$$

必來自：

- pressure-driven eigenframe rotation；
- viscous direction diffusion；
- vorticity/gauge rotation；
- correlated multi-frame coupling。

這是一個真正的 rate competition。

---

# 25. Vorticity strongest-direction lock versus quotient weakest-direction lock

frozen-strain leading dynamics各自有 stable branch：

$$
\boxed{
\xi\to e_3,
}
\tag{25.1}
$$

$$
\boxed{
n\to e_1.
}
\tag{25.2}
$$

所以 generic strain-only tendency是：

$$
\boxed{
\text{vorticity and quotient direction separate toward opposite strain extremes}.
}
\tag{25.3}
$$

這表示 Round 26 transverse depletion factor：

$$
|\xi\times n|
$$

在此 simplified asymptotic picture不趨近零，

而傾向：

$$
\boxed{
|\xi\times n|\to1
}
$$

若：

$$
e_1\perp e_3.
$$

所以 strain-only dynamics本身不會用：

$$
\xi\parallel n
$$

去關掉 cross-strain amplitude。

---

# 26. But amplitude persistence still does not fix signed phase

即使：

$$
|\xi\times n|
$$

保持 order-one，

Round 27 pair coupling仍有：

$$
\psi_{BS}
=
2(n\cdot e)(m\cdot e)
$$

signed phase。

所以：

$$
\boxed{
\text{transverse amplitude persistence}
\neq
\text{signed coherence persistence}.
}
$$

仍需：

$$
e,
\quad
n,
\quad
\xi
$$

多框架 lock。

---

# 27. Stability classification after Round 28

目前 angular lock可分：

## Type A — strain-only individual attractors

$$
\xi\to e_3,
\qquad
n\to e_1.
$$

## Type B — common-direction lock

frozen-strain：

$$
\boxed{
\text{saddle}.
}
$$

## Type C — pressure/tensor coherence lock

需要 relative angular Jacobian：

$$
\mathcal J_{\rm rel}.
$$

沒有 universal sign。

## Type D — forced lock

即使 principal dynamics unstable，

外部 pressure/gauge/viscous feedback可持續把系統壓在 lock manifold附近。

因此 persistent danger可來自：

$$
\boxed{
\text{stable lock}
\vee
\text{forced lock}
\vee
\text{neutral persistence}.
}
$$

---

# 28. STOP-C32 — Dual-Strain Saddle / Lock-Stability Forcing Gap

$$
\boxed{
\begin{aligned}
\text{layer}
&=
\mathrm{lock\text{-}manifold\ stability},
\\
\text{vorticity frozen-strain flow}
&=
\mathrm{Rayleigh\ ascent},
\\
\text{quotient-direction frozen-strain flow}
&=
\mathrm{Rayleigh\ descent},
\\
\text{vorticity stable direction}
&=
e_3,
\\
\text{quotient stable direction}
&=
e_1,
\\
\text{common eigenvector lock}
&=
\mathrm{saddle\ for\ simple\ spectrum},
\\
\text{middle-eigenvector common lock}
&=
\mathrm{multi\text{-}frame\ saddle},
\\
\text{actual stabilization}
&=
\mathrm{pressure}
+
\mathrm{viscosity}
+
\mathrm{vorticity}
+
\mathrm{gauge}
+
\mathrm{frame\ dynamics},
\\
\text{missing}
&=
\mathrm{unconditional\ sign/control\ of\ relative\ angular\ Jacobian
and\ lock\ forcing},
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
\textbf{STOP-C32:
Dual-Strain Saddle / Lock-Stability Forcing Gap}.
}
$$

---

# 29. 24/72 Ledger — Round 28

| Step | object | $B$ | $U$ | $O$ | $L$ | status |
|---|---|---|---|---|---|---|
| C380 | frozen vorticity direction flow | $\mathsf C$ | angular ODE | relational | $\mathsf F$ | EXACT |
| C381 | vorticity Rayleigh ascent | $\mathsf C$ | gradient flow | scalar | $\mathsf F$ | PROVED |
| C382 | vorticity eigenvector stability | $\mathsf C$ | linearization | targeted | $\mathsf F$ | PROVED |
| C383 | frozen quotient direction flow | $\mathsf C$ | angular ODE | relational | $\mathsf F$ | EXACT |
| C384 | quotient Rayleigh descent | $\mathsf C$ | gradient flow | scalar | $\mathsf F$ | PROVED |
| C385 | quotient eigenvector stability | $\mathsf C$ | linearization | targeted | $\mathsf F$ | PROVED |
| C386 | $\xi\cdot n$ exact strain-only law | $\mathsf C$ | relational | scalar | $\mathsf F$ | EXACT |
| C387 | common-lock paired exponents | $\mathsf C$ | linearization | relational | $\mathsf F$ | PROVED |
| C388 | common-lock saddle theorem | $\mathsf C$ | stability | targeted | $\mathsf F$ | PROVED |
| C389 | moving eigenframe coefficients | $\mathsf C$ | frame transport | relational | $\mathsf F$ | EXACT |
| C390 | vorticity moving-frame equation | $\mathsf C$ | coupled angular PDE | relational | $\mathsf F$ | EXACT |
| C391 | quotient moving-frame equation | $\mathsf C$ | gauge/angular PDE | relational | $\mathsf F$ | EXACT |
| C392 | forced common-lock linearization | $\mathsf C$ | stability | $\mathsf X$ | $\mathsf F$ | FORM |
| C393 | spectral-collision branch | $\mathsf C$ | degeneracy | relational | $\mathsf F$ | IDENTIFIED |
| C394 | tensor tangent lock error | $\mathsf C$ | manifold stability | $\mathsf X$ | $\mathsf F$ | EXACT |
| C395 | relative angular Jacobian criterion | $\mathsf C$ | linearization | targeted | $\mathsf F$ | CONDITIONAL |
| C396 | neutral-lock witness | $\mathsf C$ | structural model | targeted | $\mathsf F$ | CONSTRUCTED |
| C397 | conditional lock-stability lemma | $\mathsf C$ | Gronwall | scalar | $\mathsf F$ | PROVED |
| C398 | frozen common-lock attraction | $\mathsf C$ | stability | scalar | $\mathsf F$ | REFUTED |
| C399 | unconditional actual lock stability sign | $\mathsf C$ | coupled NS | targeted | $\mathsf F$ | OPEN / STOP-C32 |

---

# 30. Continuous-versus-discrete status

本輪使用：

- continuous sphere dynamics；
- continuous eigenframe transport；
- tangent-space linearization；
- continuous Lyapunov / attraction rates；
- continuous spectral gaps：
  $$
  \lambda_i-\lambda_j.
  $$

有限 eigenvalue label：

$$
i=1,2,3
$$

只是 $3\times3$ symmetric tensor的 finite spectral notation。

整個結果可用 spectral projectors重寫。

因此：

$$
\boxed{
T_{\mathsf C\to\mathsf D}
=
\text{NOT YET REACHED}.
}
$$

---

# 31. Strongest results of Round 28

## R28-A — Dual Strain Gradient Flow

$$
\boxed{
\xi'=
P_\xi^\perp S\xi
}
$$

是 Rayleigh ascent；

$$
\boxed{
n'=
-P_n^\perp Sn
}
$$

是 Rayleigh descent。

## R28-B — Opposite individual attractors

$$
\boxed{
\xi\to e_3,
\qquad
n\to e_1
}
$$

在 frozen simple strain中。

## R28-C — Common-lock saddle theorem

$$
\boxed{
\xi=n=e_i
}
$$

的 transverse exponents成：

$$
\boxed{
\pm|\lambda_j-\lambda_i|
}
$$

pair，所以 common lock不可能由 strain-only principal dynamics asymptotically attract。

## R28-D — Moving-frame forcing requirement

actual stable common lock必須靠 pressure / viscosity / vorticity / gauge / frame dynamics真正克服 unstable strain-gap rate。

## R28-E — Scalar coherence is insufficient at perfect lock

$$
c=1
$$

時：

$$
c'=0
$$

自動成立。

lock stability必須看 tangent-space error與 relative angular Jacobian。

---

# 32. Next round — Lock-Stability Energy / Frame-Forcing Budget

下一輪不再只寫：

$$
\mathcal J_{\rm rel}.
$$

直接攻：

$$
\boxed{
\text{額外 frame/gauge forcing是否有足夠 budget 長時間維持 unstable lock？}
}
$$

問題：

1. stable/forced common lock需要克服：
   $$
   |\lambda_j-\lambda_i|;
   $$
2. pressure-Hessian off-diagonal forcing是否有可積分 budget；
3. viscosity frame forcing：
   $$
   \nu\Delta S
   $$
   是否會形成 damping而非 persistent forcing；
4. gauge-direction forcing：
   $$
   r^{-1}P_n^\perp\nabla\chi_g
   $$
   在 low-amplitude區是否能長時間維持 lock；
5. 定義 cumulative lock-work：
   $$
   \mathcal W_{\rm lock};
   $$
6. 若 persistent amplification lock需要 infinite / critical forcing budget，可能形成新的 continuation criterion；
7. 若 budget本身可由既有 energy提供，才有機會真正關閉 phase-locking route；
8. 仍不離散 frame states。

---

# 33. External primary-source anchors

1. Alex Encinas-Bartos, George Haller, *Vorticity Alignment with Lyapunov Vectors and Rate-of-Strain Eigenvectors*, arXiv:2310.17267.
   - material stretching、vorticity alignment與 viscous-flow intermediate strain-eigenvector estimates的 primary-source背景。

2. Alain Pumir, Eberhard Bodenschatz, Haitao Xu, *Tetrahedron deformation and alignment of perceived vorticity and strain in a turbulent flow*, arXiv:1204.5857.
   - instantaneous intermediate alignment與 fixed strain eigenframe下 vorticity朝 strongest eigendirection演化之 DNS/experimental primary-source背景。

3. B. Galanti, J. D. Gibbon, M. Heritage, *Vorticity alignment results for the three-dimensional Euler and Navier-Stokes equations*, arXiv:chao-dyn/9709003.
   - vorticity–strain alignment variables、pressure-Hessian-driven alignment dynamics與 attracting alignment states under additional assumptions的 primary-source背景。

本輪 dual Rayleigh-flow identities、common-lock saddle theorem、moving-eigenframe coefficient equations、tangent lock-error criterion與 conditional stability lemma均為本文直接推導。

---

# 34. Commit state

$$
\boxed{
\begin{aligned}
\text{Route}
&=
\mathrm{Pure\ Continuous\ Lock\text{-}Manifold\ Stability},
\\
\text{Essential }\mathsf C\to\mathsf D
&=
\mathrm{Not\ reached},
\\
\text{Vorticity principal flow}
&=
\mathrm{strain\ Rayleigh\ ascent},
\\
\text{Quotient principal flow}
&=
\mathrm{strain\ Rayleigh\ descent},
\\
\text{Common lock}
&=
\mathrm{frozen\text{-}strain\ saddle},
\\
\text{Stable actual lock}
&=
\mathrm{requires\ extra\ angular\ stabilization},
\\
\text{Middle alignment}
&=
\mathrm{requires\ moving\text{-}frame/nonlocal/viscous\ organization},
\\
\text{STOP-C32}
&=
\mathrm{Dual\text{-}Strain\ Saddle/Lock\text{-}Stability\ Forcing\ Gap},
\\
\text{Next}
&=
\mathrm{Lock\text{-}Stability\ Energy/Frame\text{-}Forcing\ Budget}.
\end{aligned}
}
$$
