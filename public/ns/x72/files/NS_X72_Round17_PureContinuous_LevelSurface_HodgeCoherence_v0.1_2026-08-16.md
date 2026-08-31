# NS × X 積分 × 24/72 範式實戰
## Round 17 — Pure Continuous Level-Surface Flux / Hodge-Coherence Route

- 日期：2026-08-16
- 版本：v0.1
- 狀態：Proof-Route Experiment / Continuous-Only Level-Surface Geometry Branch
- canonical source：UTF-8 Markdown
- canonical math delimiters：inline `$...$`；display `$$...$$`
- 前一輪：`NS_X72_Round16_PureContinuous_LayerCake_SuperlevelDistortion_v0.1_2026-08-16.md`
- 本輪目標：解剖 Round 16 的 level-surface boundary flux
  $$
  \mathcal B_Q(\lambda)
  $$
  ，以 nonlinear critical gauge
  $$
  \operatorname{div}(r^2n)=0
  $$
  將其分解成 incidence angle、direction turning、surface geometry與 optimal gauge slope；並檢驗 boundary flux是否是一個真正獨立 obstruction，或可重新吸收到 nonlinear-Hodge bulk geometry。
- 非主張：本文未證明 critical weighted physical-gradient budget必然有限。本文把 Round 16 的 boundary-flux obstruction部分解決後，將剩餘問題壓到一個 scale-critical weighted physical-gradient / Hodge-coherence frontier。

---

# 0. Round 16 handoff

令：

$$
Q
=
\mathfrak Q_3[u],
$$

optimal representative：

$$
v
=
u+\nabla q,
$$

以及：

$$
r=|v|,
\qquad
n=\frac v{|v|}
$$

於：

$$
r>0.
$$

nonlinear gauge：

$$
\boxed{
\operatorname{div}(r^2n)=0.
}
\tag{0.1}
$$

Round 16 定義：

$$
E_\lambda
=
\{r>\lambda\}
$$

及 regular level surface：

$$
\Sigma_\lambda
=
\{r=\lambda\}.
$$

global nonlinear-Hodge orthogonality localized to：

$$
E_\lambda
$$

後得到：

$$
\boxed{
E_M^u(\lambda)
=
D_M(\lambda)
+
H_M(\lambda)
-
2\mathcal B_Q(\lambda).
}
\tag{0.2}
$$

其中：

$$
\boxed{
\mathcal B_Q(\lambda)
=
\sum_{\ell=1}^3
\int_{\Sigma_\lambda}
q_\ell
\left(
M_v\partial_\ell v
\right)
\cdot\eta_\lambda
\,dS,
}
\tag{0.3}
$$

$$
q_\ell=\partial_\ell q,
$$

$$
M_v
=
r(I+n\otimes n),
$$

而：

$$
\eta_\lambda
$$

為：

$$
E_\lambda
$$

的 outward unit normal。

Round 16 STOP：

$$
\boxed{
\text{STOP-C20}
=
\text{Continuous Layer-Distortion / Boundary-Flux Gap}.
}
$$

---

# 1. Level-surface notation

在 regular level：

$$
\Sigma_\lambda,
$$

令：

$$
g
=
|\nabla r|.
$$

因：

$$
E_\lambda=\{r>\lambda\},
$$

outward normal 指向較小 $r$：

$$
\boxed{
\eta
=
-\frac{\nabla r}{g}.
}
\tag{1.1}
$$

定義 directional incidence：

$$
\boxed{
a
=
n\cdot\eta.
}
\tag{1.2}
$$

並分解：

$$
\boxed{
n
=
a\eta+n_T,
\qquad
n_T\cdot\eta=0.
}
\tag{1.3}
$$

---

# 2. Gauge incidence relation

由：

$$
\operatorname{div}(r^2n)=0,
$$

有：

$$
2r\,n\cdot\nabla r
+
r^2\operatorname{div}n
=
0.
$$

在：

$$
r=\lambda,
$$

且：

$$
n\cdot\nabla r
=
-ga,
$$

所以：

$$
\boxed{
\operatorname{div}n
=
\frac{
2ga
}{
\lambda
}.
}
\tag{2.1}
$$

這是 amplitude-level normal incidence與 direction-field divergence之間的 exact relation。

---

# 3. Zero net directional incidence

若：

$$
E_\lambda^{(j)}
$$

是一個 bounded regular connected superlevel component，則 divergence theorem：

$$
0
=
\int_{E_\lambda^{(j)}}
\operatorname{div}(r^2n)dx
=
\int_{\partial E_\lambda^{(j)}}
r^2
n\cdot\eta\,dS.
$$

在 boundary：

$$
r=\lambda,
$$

故：

$$
\boxed{
\int_{\partial E_\lambda^{(j)}}
n\cdot\eta\,dS
=
0.
}
\tag{3.1}
$$

命名：

$$
\boxed{
\textbf{Zero Net Incidence Law}.
}
$$

所以 optimal direction field不能在整個 closed amplitude surface上只單向向外或只單向向內穿越。

normal incidence必須整體平衡。

---

# 4. Mean-curvature / incidence balance

令 signed mean-curvature convention：

$$
\boxed{
\mathcal H_\Sigma
=
\operatorname{div}\eta.
}
\tag{4.1}
$$

在 surface上使用：

$$
n=a\eta+n_T.
$$

ambient divergence decomposition：

$$
\operatorname{div}n
=
\partial_\eta a
+
\operatorname{div}_\Sigma n_T
+
\mathcal H_\Sigma a.
$$

與 (2.1) 比較：

$$
\boxed{
\left(
\frac{2g}{\lambda}
-
\mathcal H_\Sigma
\right)a
=
\partial_\eta a
+
\operatorname{div}_\Sigma n_T.
}
\tag{4.2}
$$

因此 level-set curvature、amplitude slope、direction incidence與 tangential directional flux並非獨立。

---

# 5. Exact surface decomposition of quotient dissipation density

Round 16 unweighted dissipation density：

$$
A
=
|\nabla v|^2
+
|\nabla r|^2.
$$

由：

$$
v=rn
$$

及：

$$
n\cdot\partial_jn=0,
$$

有：

$$
\boxed{
|\nabla v|^2
=
|\nabla r|^2
+
r^2|\nabla n|^2.
}
\tag{5.1}
$$

所以：

$$
\boxed{
A
=
2g^2
+
r^2|\nabla n|^2.
}
\tag{5.2}
$$

Round 16 surface dissipation density：

$$
a_\Sigma(\lambda)
=
-d'(\lambda)
$$

因此：

$$
\boxed{
a_\Sigma(\lambda)
=
\int_{\Sigma_\lambda}
\left[
2g
+
\frac{
\lambda^2|\nabla n|^2
}{
g
}
\right]dS.
}
\tag{5.3}
$$

這個 exact decomposition說：

surface dissipation支付兩種 cost：

1. amplitude steepness：
   $$
   g;
   $$
2. directional turning：
   $$
   |\nabla n|.
   $$

---

# 6. Incidence-angle dissipation tax

由：

$$
|\operatorname{div}n|^2
\le
3|\nabla n|^2,
$$

以及 (2.1)：

$$
\frac{
\lambda^2|\nabla n|^2
}{
g
}
\ge
\frac{
4
}{
3
}
g a^2.
$$

故：

$$
\boxed{
a_\Sigma(\lambda)
\ge
\int_{\Sigma_\lambda}
g
\left(
2+\frac43a^2
\right)dS.
}
\tag{6.1}
$$

命名：

$$
\boxed{
\textbf{Incidence-Angle Dissipation Tax}.
}
$$

所以 direction field以較強 normal angle 穿越 amplitude surface時，surface dissipation必增加。

---

# 7. Area–distribution dissipation inequality

令：

$$
S(\lambda)
=
\operatorname{Area}(\Sigma_\lambda),
$$

且：

$$
-V'(\lambda)
=
\int_{\Sigma_\lambda}
\frac1g\,dS.
$$

由 Cauchy–Schwarz：

$$
S(\lambda)^2
\le
\left(
\int_{\Sigma_\lambda}g\,dS
\right)
\left(
-V'(\lambda)
\right).
$$

由 (5.3)：

$$
a_\Sigma
\ge
2\int_\Sigma g.
$$

因此：

$$
\boxed{
a_\Sigma(\lambda)
\left(
-V'(\lambda)
\right)
\ge
2S(\lambda)^2.
}
\tag{7.1}
$$

再由三維 isoperimetric inequality：

$$
S(\lambda)
\ge
C_{\rm iso}
V(\lambda)^{2/3},
$$

得到：

$$
\boxed{
a_\Sigma(\lambda)
\left(
-V'(\lambda)
\right)
\ge
c_{\rm iso}
V(\lambda)^{4/3}.
}
\tag{7.2}
$$

所以 superlevel volume若在 amplitude軸上不快速下降，surface dissipation必支付面積 cost。

---

# 8. Exact boundary-flux factorization

由：

$$
\partial_\ell v
=
(\partial_\ell r)n
+
r\partial_\ell n,
$$

及：

$$
M_v
=
r(I+n\otimes n),
$$

得到：

$$
\boxed{
M_v\partial_\ell v
=
2r
(\partial_\ell r)n
+
r^2\partial_\ell n.
}
\tag{8.1}
$$

代入 boundary flux。

在：

$$
r=\lambda,
$$

經 (2.1) 化簡：

$$
\boxed{
\begin{aligned}
\mathcal B_Q(\lambda)
={}&
\lambda^2
\int_{\Sigma_\lambda}
\left[
((\nabla q\cdot\nabla)n)\cdot\eta
-
(\operatorname{div}n)
(\nabla q\cdot\eta)
\right]dS.
\end{aligned}
}
\tag{8.2}
$$

等價 tensor form：

$$
\boxed{
\mathcal B_Q(\lambda)
=
\lambda^2
\int_{\Sigma_\lambda}
\eta\cdot
\left[
\nabla n
-
(\operatorname{div}n)I
\right]
\nabla q
\,dS.
}
\tag{8.3}
$$

這是本輪第一個核心 boundary-flux identity。

---

# 9. Meaning of the boundary-flux identity

(8.2) 顯示：

$$
\mathcal B_Q
$$

不是任意 boundary artifact。

它必須同時使用：

- direction-field gradient：
  $$
  \nabla n;
  $$
- normal incidence/divergence；
- optimal gauge slope：
  $$
  \nabla q;
  $$
- level-surface normal：
  $$
  \eta.
  $$

單獨 large surface area或 large amplitude並不足以產生 large boundary flux。

---

# 10. Surface gauge-slope bound

定義：

$$
\boxed{
P_q(\lambda)
=
\int_{\Sigma_\lambda}
g
|\nabla q|^2dS.
}
\tag{10.1}
$$

由：

$$
|\operatorname{div}n|
\le
\sqrt3|\nabla n|
$$

與 (8.2)：

$$
|\mathcal B_Q|
\le
C
\lambda^2
\int_\Sigma
|\nabla n|
|\nabla q|\,dS.
$$

以 weights：

$$
g^{-1},
\qquad
g
$$

做 Cauchy：

$$
|\mathcal B_Q|
\le
C
\lambda^2
\left(
\int_\Sigma
\frac{
|\nabla n|^2
}{
g
}dS
\right)^{1/2}
P_q(\lambda)^{1/2}.
$$

由 (5.3)：

$$
\boxed{
|\mathcal B_Q(\lambda)|
\le
C
\lambda
a_\Sigma(\lambda)^{1/2}
P_q(\lambda)^{1/2}.
}
\tag{10.2}
$$

所以 large pointwise boundary flux需要：

$$
\boxed{
\text{directional surface dissipation}
\times
\text{optimal gauge slope}
}
$$

共同增大。

---

# 11. Boundary flux is also a bulk Hodge cross term

由：

$$
\operatorname{div}
(M_v\partial_\ell v)=0
$$

及 divergence theorem：

$$
\boxed{
\mathcal B_Q(\lambda)
=
\sum_\ell
\int_{E_\lambda}
\nabla q_\ell
\cdot
M_v
\partial_\ell v\,dx.
}
\tag{11.1}
$$

所以 boundary flux同時是一個 bulk nonlinear-Hodge coherence。

定義：

$$
D_M(\lambda)
=
\sum_\ell
\int_{E_\lambda}
\partial_\ell v
\cdot
M_v
\partial_\ell v\,dx,
$$

$$
H_M(\lambda)
=
\sum_\ell
\int_{E_\lambda}
\nabla q_\ell
\cdot
M_v
\nabla q_\ell\,dx.
$$

則：

$$
\boxed{
|\mathcal B_Q(\lambda)|
\le
\sqrt{
D_M(\lambda)H_M(\lambda)
}.
}
\tag{11.2}
$$

因此 boundary flux的 magnitude不是一個額外無界 trace variable。

它被 bulk quotient/gauge energies控制。

---

# 12. Level Hodge-coherence coefficient

若：

$$
D_MH_M>0,
$$

定義：

$$
\boxed{
\rho_M(\lambda)
=
\frac{
\mathcal B_Q(\lambda)
}{
\sqrt{
D_M(\lambda)H_M(\lambda)
}
}.
}
\tag{12.1}
$$

則：

$$
\boxed{
-1\le\rho_M\le1.
}
$$

local Pythagorean：

$$
E_M^u
=
D_M+H_M-2\mathcal B_Q
$$

可寫成：

$$
\boxed{
\frac{
E_M^u
}{
D_M
}
=
1+R_M
-
2\rho_M\sqrt{R_M},
}
\tag{12.2}
$$

其中：

$$
\boxed{
R_M
=
\frac{
H_M
}{
D_M
}.
}
\tag{12.3}
$$

再重寫：

$$
\boxed{
\frac{
E_M^u
}{
D_M
}
=
\left(
\sqrt{R_M}-1
\right)^2
+
2\sqrt{R_M}
\left(
1-\rho_M
\right).
}
\tag{12.4}
$$

命名：

$$
\boxed{
\textbf{Level Hodge-Coherence Identity}.
}
$$

---

# 13. Consequence of the Hodge-coherence identity

(12.4) 表示 localized physical weighted gradient可以變小，必須同時滿足：

1. gauge distortion與 quotient dissipation接近：
   $$
   R_M\approx1;
   $$
2. nonlinear-Hodge cross term幾乎完全正對齊：
   $$
   \rho_M\approx1.
   $$

如果：

$$
R_M\gg1,
$$

則無論 boundary flux怎麼選，

$$
\boxed{
E_M^u
\ge
\left(
\sqrt{H_M}-\sqrt{D_M}
\right)^2.
}
\tag{13.1}
$$

所以 very large local gauge distortion無法被 boundary flux偷偷完全抵消。

它必轉化成 large physical weighted-gradient tail。

---

# 14. Relation to Round 16 continuous tails

Round 16：

$$
d(\lambda)
=
\int_{E_\lambda}
A\,dx,
$$

$$
h(\lambda)
=
\int_{E_\lambda}
B\,dx.
$$

而：

$$
D_M(\lambda)
=
\int_{E_\lambda}
rA\,dx,
$$

所以 layer-cake：

$$
\boxed{
D_M(\lambda)
=
\lambda d(\lambda)
+
\int_\lambda^\infty
d(\mu)d\mu.
}
\tag{14.1}
$$

同樣：

$$
\boxed{
H_M(\lambda)
=
\lambda h(\lambda)
+
\int_\lambda^\infty
h(\mu)d\mu.
}
\tag{14.2}
$$

所以 $R_M(\lambda)$ 不是新的離散 scale。

它是 Round 16 continuous tail profile的一個 smoothed amplitude-weighted transform。

---

# 15. Cumulative boundary-flux identity

定義：

$$
\boxed{
\overline{\mathcal B}_Q(\lambda)
=
\int_\lambda^\infty
\mathcal B_Q(\mu)d\mu.
}
\tag{15.1}
$$

由 coarea：

$$
\overline{\mathcal B}_Q(\lambda)
=
-
\sum_\ell
\int_{E_\lambda}
q_\ell
\left(
M_v\partial_\ell v
\right)
\cdot\nabla r\,dx.
$$

再使用：

$$
\operatorname{div}
(M_v\partial_\ell v)=0
$$

測試：

$$
q_\ell(r-\lambda)_+,
$$

得到：

$$
\boxed{
\overline{\mathcal B}_Q(\lambda)
=
\sum_\ell
\int_{E_\lambda}
(r-\lambda)
\nabla q_\ell
\cdot
M_v
\partial_\ell v\,dx.
}
\tag{15.2}
$$

所以 cumulative surface flux完全重積回 continuous bulk coherence。

---

# 16. Cumulative flux bound

定義：

$$
\overline D_M(\lambda)
=
\sum_\ell
\int_{E_\lambda}
(r-\lambda)
\partial_\ell v
\cdot
M_v
\partial_\ell v\,dx,
$$

$$
\overline H_M(\lambda)
=
\sum_\ell
\int_{E_\lambda}
(r-\lambda)
\nabla q_\ell
\cdot
M_v
\nabla q_\ell\,dx.
$$

則：

$$
\boxed{
|\overline{\mathcal B}_Q(\lambda)|
\le
\sqrt{
\overline D_M(\lambda)
\overline H_M(\lambda)
}.
}
\tag{16.1}
$$

所以如果 pointwise surface trace很難估，

continuous $\lambda$ integration可將它重新吸收到 bulk nonlinear-Hodge metric。

這是 Round 16 boundary-flux obstruction的一個 partial repair。

---

# 17. Physical weighted-gradient tail

由 definition：

$$
E_M^u(\lambda)
=
\sum_\ell
\int_{E_\lambda}
\partial_\ell u
\cdot
M_v
\partial_\ell u\,dx.
$$

展開：

$$
\boxed{
E_M^u(\lambda)
=
\int_{E_\lambda}
r
\left[
|\nabla u|^2
+
|(\nabla u)^\top n|^2
\right]dx.
}
\tag{17.1}
$$

因此：

$$
\boxed{
\int_{E_\lambda}
r|\nabla u|^2dx
\le
E_M^u(\lambda)
\le
2
\int_{E_\lambda}
r|\nabla u|^2dx.
}
\tag{17.2}
$$

所以 localized boundary-flux problem最後被推向一個 physical carrier：

$$
\boxed{
|v|
|\nabla u|^2.
}
$$

---

# 18. Global critical weighted-gradient budget

令：

$$
\boxed{
E_M(t)
=
E_M^u(0,t)
=
\int_{\mathbb R^3}
r
\left[
|\nabla u|^2
+
|(\nabla u)^\top n|^2
\right]dx.
}
\tag{18.1}
$$

Round 15 global Pythagorean：

$$
\boxed{
E_M
=
D+H.
}
\tag{18.2}
$$

在 NS scaling下：

$$
u_\lambda=\lambda u(\lambda x,\lambda^2t),
$$

optimal quotient representative同樣縮放：

$$
v_\lambda=\lambda v(\lambda x,\lambda^2t).
$$

因此：

$$
E_M
\mapsto
\lambda^2 E_M.
$$

所以：

$$
\boxed{
\int
E_M(t)\,dt
}
\tag{18.3}
$$

是 scale-invariant spacetime quantity。

這是一個新的 Pure-C critical budget。

---

# 19. Critical Weighted-Gradient Budget Criterion

Round 15 growth estimate：

$$
|I_Q|
\le
C
Q
H^{1/2}
D^{1/2}.
$$

因：

$$
E_M=D+H,
$$

AM–GM：

$$
H^{1/2}D^{1/2}
\le
\frac12E_M.
$$

所以：

$$
\boxed{
|I_Q|
\le
C
Q
E_M.
}
\tag{19.1}
$$

而 exact quotient equation：

$$
\frac13
(Q^3)'
+
\nu D
=
I_Q.
$$

即：

$$
Q^2Q'
+
\nu D
=
I_Q.
$$

若：

$$
Q>0,
$$

則：

$$
Q Q'
\le
C E_M.
$$

因此：

$$
\boxed{
\frac d{dt}
Q^2
\le
C
E_M(t).
}
\tag{19.2}
$$

積分：

$$
\boxed{
Q(T)^2
\le
Q(0)^2
+
C
\int_0^T
E_M(t)dt.
}
\tag{19.3}
$$

所以：

$$
\boxed{
\int_0^{T_\ast}
E_M(t)dt
<
\infty
}
\tag{19.4}
$$

足以保持：

$$
Q(t)
$$

有界。

由：

$$
Q\simeq\|u\|_3,
$$

及標準 endpoint $L^\infty_tL^3_x$ continuation theory，

得到 conditional regularity。

命名：

$$
\boxed{
\textbf{Critical Weighted-Gradient Budget Criterion}.
}
$$

本文不主張此 formulation 的學術新穎性；它是本路線 identities 的直接結果。

---

# 20. Why this is not yet closure

standard energy inequality提供：

$$
\int
\|\nabla u\|_2^2dt.
$$

但：

$$
E_M
$$

包含額外 critical amplitude weight：

$$
|v|.
$$

所以目前沒有由 ordinary energy直接得到：

$$
\boxed{
\int E_Mdt<\infty.
}
$$

因此：

$$
\boxed{
\text{boundary flux}
}
$$

不再是最深 obstruction。

它可以被 surface geometry、bulk Hodge coherence與 cumulative integration控制。

真正缺的是：

$$
\boxed{
\text{critical weighted physical-gradient budget}.
}
$$

---

# 21. Relation to strain / vorticity geometry

pointwise：

$$
|\nabla u|^2
=
|S_u|^2
+
\frac12|\omega|^2.
$$

所以：

$$
E_M
$$

至少包含 weighted：

$$
\boxed{
|v|
\left(
|S_u|^2
+
\frac12|\omega|^2
\right).
}
$$

第二項：

$$
|(\nabla u)^\top n|^2
$$

再加入 optimal-direction alignment information。

所以 Round 17 的 new frontier重新接回：

- Round 03 strain/vorticity geometry；
- Round 05 gradient-alignment；
- Round 08 frequency-transfer geometry；

但現在它們被一個 critical quotient amplitude：

$$
|v|
$$

加權。

---

# 22. STOP-C21 — Level Hodge-Coherence / Critical Weighted-Gradient Gap

定義：

$$
\boxed{
\bot_X^{\mathrm{C21}}
=
\left\langle
\begin{array}{l}
\text{layer}
=
\mathrm{continuous\ level\text{-}surface\ geometry},
\\
\text{zero\ net\ incidence}
=
\int_{\Sigma_\lambda}
n\cdot\eta
=
0,
\\
\text{surface\ dissipation}
=
2g+\lambda^2|\nabla n|^2/g,
\\
\text{boundary\ flux}
=
\lambda^2
\int
\eta\cdot
[\nabla n-(\operatorname{div}n)I]
\nabla q,
\\
\text{bulk\ coherence}
=
|\mathcal B_Q|
\le
\sqrt{D_MH_M},
\\
\text{localized\ identity}
=
E_M^u
=
D_M+H_M-2\mathcal B_Q,
\\
\text{cumulative\ surface\ flux}
=
\mathrm{resummed\ into\ bulk\ coherence},
\\
\text{new\ critical\ budget}
=
\int E_Mdt,
\\
\text{missing}
=
\mathrm{unconditional\ control\ of\ critical\ weighted\ physical\ gradient},
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
\textbf{STOP-C21:
Level Hodge-Coherence / Critical Weighted-Gradient Gap}.
}
$$

---

# 23. 24/72 Ledger — Round 17

| Step | object | $B$ | $U$ | $O$ | $L$ | status |
|---|---|---|---|---|---|---|
| C197 | level normal / incidence | $\mathsf C$ | surface geometry | relational | $\mathsf F$ | FORM |
| C198 | gauge incidence relation | $\mathsf C$ | constraint | scalar relation | $\mathsf F$ | EXACT |
| C199 | zero net incidence | $\mathsf C$ | global surface | scalar | $\mathsf F$ | PROVED |
| C200 | mean-curvature/incidence balance | $\mathsf C$ | surface differential | $\mathsf X$ | $\mathsf F$ | EXACT |
| C201 | surface dissipation decomposition | $\mathsf C$ | coarea | scalar profile | $\mathsf F$ | EXACT |
| C202 | incidence-angle dissipation tax | $\mathsf C$ | geometry | targeted | $\mathsf F$ | PROVED |
| C203 | area–distribution dissipation | $\mathsf C$ | isoperimetric/coarea | targeted | $\mathsf F$ | PROVED |
| C204 | boundary-flux factorization | $\mathsf C$ | surface geometry | $\mathsf X$ | $\mathsf F$ | EXACT |
| C205 | surface gauge-slope bound | $\mathsf C$ | surface estimate | scalar profile | $\mathsf F$ | PROVED |
| C206 | boundary flux as bulk cross term | $\mathsf C$ | nonlinear Hodge | relational | $\mathsf F$ | EXACT |
| C207 | Hodge coherence coefficient | $\mathsf C$ | recognition | scalar profile | $\mathsf F$ | FORM |
| C208 | level Hodge-coherence identity | $\mathsf C$ | geometric decomposition | targeted | $\mathsf F$ | EXACT |
| C209 | cumulative flux resummation | $\mathsf C$ | continuous $\lambda$ integration | relational | $\mathsf F$ | EXACT |
| C210 | physical weighted-gradient carrier | $\mathsf C$ | relational | $\mathsf X$ | $\mathsf F$ | FORM |
| C211 | scale-critical weighted-gradient budget | $\mathsf C$ | spacetime integration | scalar | $\mathsf F$ | CRITICAL |
| C212 | finite weighted-gradient budget $\Rightarrow$ bounded $Q$ | $\mathsf C$ | continuation | targeted | $\mathsf F$ | PROVED |
| C213 | unconditional weighted-gradient budget | $\mathsf C$ | — | targeted | $\mathsf F$ | OPEN / STOP-C21 |

---

# 24. Continuous-versus-discrete status

本輪甚至將：

$$
\mathcal B_Q(\lambda)
$$

先拆成 surface geometry，再用：

$$
\int_\lambda^\infty
\mathcal B_Q(\mu)d\mu
$$

重新積回 bulk continuous coherence。

沒有：

- discrete surface components作為必要 index；
- dyadic thresholds；
- atomic layer；
- shell graph；
- sequence extraction。

所以：

$$
\boxed{
T_{\mathsf C\to\mathsf D}
=
\text{NOT YET REACHED}.
}
\tag{24.1}
$$

---

# 25. Strongest results of Round 17

## R17-A — Zero Net Incidence

$$
\boxed{
\int_{\Sigma_\lambda}
n\cdot\eta\,dS=0.
}
$$

## R17-B — Incidence Dissipation Tax

$$
\boxed{
a_\Sigma
\ge
\int_\Sigma
g
\left(
2+\frac43(n\cdot\eta)^2
\right)dS.
}
$$

## R17-C — Exact surface flux

$$
\boxed{
\mathcal B_Q
=
\lambda^2
\int_\Sigma
\eta\cdot
[\nabla n-(\operatorname{div}n)I]
\nabla q\,dS.
}
$$

## R17-D — Level Hodge-Coherence Identity

$$
\boxed{
\frac{E_M^u}{D_M}
=
(\sqrt{R_M}-1)^2
+
2\sqrt{R_M}(1-\rho_M).
}
$$

## R17-E — Critical weighted-gradient budget

$$
\boxed{
Q(T)^2
\le
Q(0)^2
+
C
\int_0^T
E_M(t)dt.
}
$$

---

# 26. Next round — Weighted Physical-Gradient / Strain–Vorticity Return

下一輪不再把：

$$
\mathcal B_Q
$$

當 primary Boss。

直接攻：

$$
\boxed{
E_M
=
\int
|v|
\left[
|\nabla u|^2
+
|(\nabla u)^\top n|^2
\right]dx.
}
$$

問題：

1. 把 $E_M$ 精確拆成：
   $$
   S_u,
   \omega,
   n
   $$
   的 relational channels；

2. 是否有 pressure-free / vorticity orthogonality可消掉部分 weighted gradient；

3. $E_M$ 的 time integral是否可由 Round 05 的 strain-$H^1$ balance與 Round 03 geometric carriers共同約束；

4. 是否存在：
   $$
   \text{large weighted gradient}
   \Longrightarrow
   \text{alignment rigidity}
   \vee
   \text{viscous overpayment};
   $$

5. 若需要 amplitude layers，繼續用 continuous $\lambda$ profile，不進 dyadic。

---

# 27. External primary-source anchors

1. Alexis Vasseur, *Regularity criterion for 3D Navier-Stokes equations in terms of the direction of the velocity*, arXiv:0705.2446.
   - velocity-direction geometry可進入 3D NS regularity criteria；
   - 本輪的 $n$ 是 optimal quotient representative direction，不等同於 $u/|u|$，因此只作方向幾何的外部方法學錨點。

2. Dongho Chae, Jihoon Lee, *On the Geometric Regularity Conditions for the 3D Navier-Stokes Equations*, arXiv:1606.08126.
   - directional/alignment geometric regularity criteria的 primary-source背景。

3. Isabelle Gallagher, Gabriel S. Koch, Fabrice Planchon, *A profile decomposition approach to the $L^\infty_t(L^3_x)$ Navier-Stokes regularity criterion*, arXiv:1012.0145.
   - bounded $L^\infty_tL^3_x$ prevents finite-time singularity；
   - 本輪用於把 bounded quotient carrier $Q\simeq\|u\|_3$ 接到 endpoint continuation。

本輪 level-surface identities、incidence tax、Hodge-coherence identity、cumulative flux resummation與 weighted-gradient budget criterion均為本文直接推導。

---

# 28. Commit state

$$
\boxed{
\begin{aligned}
\text{Route}
&=
\mathrm{Pure\ Continuous\ Level\text{-}Surface/Hodge\ Coherence},
\\
\text{Essential }\mathsf C\to\mathsf D
&=
\mathrm{Not\ reached},
\\
\text{Boundary flux}
&=
\mathrm{surface\ geometric\ and\ bulk\ coherent},
\\
\text{Zero incidence}
&=
\mathrm{exact},
\\
\text{Direction crossing}
&=
\mathrm{pays\ dissipation},
\\
\text{Cumulative flux}
&=
\mathrm{continuously\ resumable},
\\
\text{New physical carrier}
&=
E_M,
\\
\text{Spacetime budget}
&=
\int E_Mdt
\text{ scale-critical},
\\
\text{Finite budget}
&=
\mathrm{controls\ }Q,
\\
\text{STOP-C21}
&=
\mathrm{Level\ Hodge\text{-}Coherence/Critical\ Weighted\text{-}Gradient\ Gap},
\\
\text{Next}
&=
\mathrm{Weighted\ Physical\text{-}Gradient/Strain\text{-}Vorticity\ Return}.
\end{aligned}
}
$$
