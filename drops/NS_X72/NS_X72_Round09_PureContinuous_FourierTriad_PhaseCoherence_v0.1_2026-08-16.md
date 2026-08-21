# NS × X 積分 × 24/72 範式實戰
## Round 09 — Pure Continuous Fourier-Triad Geometry / Phase-Coherence Route

- 日期：2026-08-16
- 版本：v0.1
- 狀態：Proof-Route Experiment / Continuous-Only Fourier-Triad Branch
- canonical source：UTF-8 Markdown
- canonical math delimiters：inline `$...$`；display `$$...$$`
- 前一輪：`NS_X72_Round08_PureContinuous_TransferDispersion_Feedback_v0.1_2026-08-16.md`
- 本輪目標：把 Round 08 的 abstract transfer rate $\vartheta$ 代回 actual incompressible Navier–Stokes Fourier convolution，建立 continuous triad transfer kernel、commutator weight-gap identity、angular null structure與 phase-sign structure，並將 $\zeta_{\tau,s}$ 的 missing covariance bound改寫成一條明確 signed triad inequality。
- 非主張：本輪不證明該 signed triad inequality無條件成立；相反地，本輪精確辨識出 radial geometry + amplitude 本身不足以決定 transfer sign，relative triad phase 是不可丟失 carrier。

---

# 0. Round 08 handoff

Round 08 對 analytic-weighted strain spectrum定義：

$$
r=|\xi|,
$$

$$
m
=
\mathbb E_\mu[r],
$$

$$
V
=
\operatorname{Var}_\mu(r),
$$

以及 local nonlinear transfer rate：

$$
\vartheta(\xi,t).
$$

得到 exact mean-frequency law：

$$
\boxed{
m'
=
2
\operatorname{Cov}_\mu(r,\vartheta)
-
2\nu
\operatorname{Cov}_\mu(r,r^2)
+
2\tau'V.
}
\tag{0.1}
$$

並證明：

$$
\boxed{
\operatorname{Cov}_\mu(r,r^2)
\ge
mV>0
}
\tag{0.2}
$$

對 nontrivial smooth $L^2$ spectral state成立。

定義：

$$
\boxed{
\zeta_{\tau,s}
=
\frac{
\operatorname{Cov}_\mu(r,\vartheta)
}{
\nu
\operatorname{Cov}_\mu(r,r^2)
}.
}
\tag{0.3}
$$

若：

$$
\tau'\le0,
$$

則：

$$
\boxed{
\zeta_{\tau,s}\le1
\Longrightarrow
m'\le0.
}
\tag{0.4}
$$

Round 08 STOP：

$$
\boxed{
\text{STOP-C12}
=
\text{Nonlinear Transfer–Dispersion Covariance Gap}.
}
$$

本輪直接問：

$$
\boxed{
\operatorname{Cov}(r,\vartheta)
}
$$

在 actual NS convolution 中到底是什麼。

---

# 1. Fourier Navier–Stokes equation

採 Fourier convention：

$$
\widehat f(k)
=
\int_{\mathbb R^3}
e^{-ik\cdot x}
f(x)\,dx.
$$

令：

$$
P_k
=
I
-
\frac{k\otimes k}{|k|^2}
$$

為 Leray projector symbol。

對 incompressible velocity：

$$
k\cdot\widehat u(k)=0.
$$

Navier–Stokes Fourier equation：

$$
\boxed{
\partial_t\widehat u(k)
+
\nu|k|^2\widehat u(k)
=
-i
P_k
\int_{\mathbb R^3}
\left(
k\cdot\widehat u(p)
\right)
\widehat u(q)
\,dp,
}
\tag{1.1}
$$

其中：

$$
\boxed{
q=k-p,
\qquad
k=p+q.
}
\tag{1.2}
$$

由：

$$
p\cdot\widehat u(p)=0,
$$

有：

$$
\boxed{
k\cdot\widehat u(p)
=
q\cdot\widehat u(p).
}
\tag{1.3}
$$

這個 identity 將 triad coupling與 triad geometry直接連接。

---

# 2. Continuous triad transfer density

與：

$$
\overline{\widehat u(k)}
$$

pair。

因：

$$
P_k\widehat u(k)=\widehat u(k),
$$

projector 在 modal energy pairing中消失。

定義 ordered continuous triad transfer kernel：

$$
\boxed{
\mathcal T(k;p,q)
=
\operatorname{Im}
\left[
\left(
k\cdot\widehat u(p)
\right)
\left(
\widehat u(q)\cdot
\overline{\widehat u(k)}
\right)
\right],
}
\tag{2.1}
$$

其中：

$$
k=p+q.
$$

則：

$$
\boxed{
\frac12
\partial_t
|\widehat u(k)|^2
+
\nu|k|^2|\widehat u(k)|^2
=
\int_{\mathbb R^3}
\mathcal T(k;p,k-p)
\,dp.
}
\tag{2.2}
$$

令：

$$
\boxed{
\Theta(k)
=
\int
\mathcal T(k;p,k-p)
\,dp.
}
\tag{2.3}
$$

則：

$$
\Theta(k)
$$

就是 mode $k$ 的 nonlinear energy-transfer density。

---

# 3. Global energy conservation is a zero-weight-gap statement

對 smooth decaying incompressible field：

$$
\int_{\mathbb R^3}
u\cdot(u\cdot\nabla u)\,dx
=
0.
$$

在 Fourier space：

$$
\boxed{
\int_{\mathbb R^3}
\Theta(k)\,dk
=
0.
}
\tag{3.1}
$$

因此 nonlinear term：

- 可以把 energy 從某些 frequencies搬到另一些 frequencies；
- 但不創造總 kinetic energy。

這是 triad redistribution，而不是 net creation。

---

# 4. Weighted Fourier multiplier energy

令：

$$
A=a(\Lambda)
$$

為 real radial Fourier multiplier：

$$
\widehat{Af}(k)
=
a(|k|)\widehat f(k),
$$

其中：

$$
a(r)>0.
$$

定義：

$$
E_a
=
\frac12
\|Au\|_2^2.
$$

則：

$$
\boxed{
\frac d{dt}E_a
+
\nu
\|\Lambda Au\|_2^2
=
\mathcal N_a,
}
\tag{4.1}
$$

其中 direct weighted transfer：

$$
\boxed{
\mathcal N_a
=
\iint
a_k^2
\mathcal T(k;p,q)
\,dp\,dk,
}
\tag{4.2}
$$

記：

$$
a_k=a(|k|).
$$

---

# 5. Exact commutator representation

由 incompressibility：

$$
\langle
Au,
u\cdot\nabla Au
\rangle
=
0.
$$

因此：

$$
\langle
Au,
A(u\cdot\nabla u)
\rangle
=
\langle
Au,
[A,u\cdot\nabla]u
\rangle.
$$

Fourier space 中：

$$
[A,u\cdot\nabla]u
$$

的 triad kernel帶有：

$$
a_k-a_q.
$$

所以：

$$
\boxed{
\mathcal N_a
=
\iint
a_k
(a_k-a_q)
\mathcal T(k;p,q)
\,dp\,dk.
}
\tag{5.1}
$$

這個 identity 非常重要。

若：

$$
a\equiv1,
$$

則：

$$
a_k-a_q=0
$$

pointwise，

所以：

$$
\mathcal N_1=0.
$$

因此：

$$
\boxed{
\textbf{
weighted nonlinear growth exists only because
the spectral observation weight does not commute with advection.
}
}
\tag{5.2}
$$

換言之：

$$
\boxed{
\text{cascade signal}
=
\text{transport–observation commutator}.
}
$$

---

# 6. No-free-radial-jump lemma

對 radial：

$$
a=a(r),
$$

由 mean-value theorem：

$$
|a_k-a_q|
\le
\sup_{\rho\in I_{kq}}
|a'(\rho)|
\,
\bigl|
|k|-|q|
\bigr|,
$$

其中：

$$
I_{kq}
$$

是：

$$
|k|
$$

與：

$$
|q|
$$

之間區間。

由 triangle inequality：

$$
\boxed{
\bigl|
|k|-|q|
\bigr|
\le
|k-q|
=
|p|.
}
\tag{6.1}
$$

因此：

$$
\boxed{
|a_k-a_q|
\le
|p|
\sup_{\rho\in I_{kq}}
|a'(\rho)|.
}
\tag{6.2}
$$

命名：

$$
\boxed{
\textbf{No-Free-Radial-Jump Lemma}.
}
$$

意義：

> 如果一次 triad interaction 想讓 observation weight在 $q\to k$ 之間跨越很大的 radial gap，mediator mode $p$ 的 wavenumber 必須至少承擔該 gap 的幾何大小。

這不是能量成本下界。

它是 exact frequency-triangle constraint。

---

# 7. Incompressibility angular null

由：

$$
k\cdot\widehat u(p)
=
q\cdot\widehat u(p)
$$

且：

$$
\widehat u(p)\perp p,
$$

得到：

$$
\boxed{
\left|
k\cdot\widehat u(p)
\right|
\le
|q|
\sin\theta_{pq}
|\widehat u(p)|,
}
\tag{7.1}
$$

其中：

$$
\theta_{pq}
$$

為 $p,q$ 之間夾角。

因此：

$$
\boxed{
|\mathcal T(k;p,q)|
\le
|q|
\sin\theta_{pq}
|\widehat u(p)|
|\widehat u(q)|
|\widehat u(k)|.
}
\tag{7.2}
$$

特別：

$$
\boxed{
\theta_{pq}=0
\text{ or }\pi
\Longrightarrow
\mathcal T(k;p,q)=0.
}
\tag{7.3}
$$

所以 exact collinear triad 對此 ordered transfer channel不貢獻。

命名：

$$
\boxed{
\textbf{Collinear Triad Null}.
}
$$

---

# 8. Weight-gap × angle upper envelope

合併 (5.1)、(6.2)、(7.2)：

$$
\boxed{
\begin{aligned}
&
\left|
a_k(a_k-a_q)
\mathcal T(k;p,q)
\right|
\\
&\qquad
\le
a_k
|p|
|q|
\sin\theta_{pq}
\sup_{\rho\in I_{kq}}|a'(\rho)|
|\widehat u(p)|
|\widehat u(q)|
|\widehat u(k)|.
\end{aligned}
}
\tag{8.1}
$$

所以 large weighted transfer需要共同滿足：

1. nontrivial mediator frequency：

$$
|p|>0;
$$

2. non-collinear geometry：

$$
\sin\theta_{pq}>0;
$$

3. modal amplitude overlap；

4. observation-weight gap；

5. 尚未顯式寫出的 relative phase coherence。

前四項仍然不能決定 sign。

---

# 9. Triad phase carrier

定義 complex interaction product：

$$
\boxed{
Z(k;p,q)
=
\left(
k\cdot\widehat u(p)
\right)
\left(
\widehat u(q)\cdot
\overline{\widehat u(k)}
\right).
}
\tag{9.1}
$$

在：

$$
Z\neq0
$$

時寫：

$$
\boxed{
Z
=
\mathcal A
e^{i\Phi},
}
\tag{9.2}
$$

其中：

$$
\mathcal A=|Z|\ge0,
$$

$$
\Phi\in\mathbb S^1.
$$

則：

$$
\boxed{
\mathcal T
=
\mathcal A
\sin\Phi.
}
\tag{9.3}
$$

因此 transfer kernel 被精確分成：

$$
\boxed{
\text{amplitude}
\times
\text{phase coherence}.
}
$$

角度：

$$
\theta_{pq}
$$

控制：

$$
\mathcal A
$$

的幾何上界，

但：

$$
\Phi
$$

決定 signed transfer。

---

# 10. Phase-Sign Flexibility Lemma

固定一個非退化 triad geometry：

$$
(k,p,q),
\qquad
k=p+q,
$$

以及 divergence-free modal directions與 magnitudes，使：

$$
\mathcal A>0.
$$

則：

$$
\mathcal T
=
\mathcal A\sin\Phi.
$$

若只改 relative complex phase，使：

$$
\Phi
\mapsto
-\Phi,
$$

則：

$$
\mathcal A
$$

不變，

frequency triangle不變，

modal magnitudes不變，

angle geometry不變，

但：

$$
\boxed{
\mathcal T
\mapsto
-\mathcal T.
}
\tag{10.1}
$$

因此：

$$
\boxed{
\textbf{
frequency geometry + modal magnitudes do not determine
the sign of an individual triad transfer kernel.
}
}
\tag{10.2}
$$

這是一個 algebraic Fourier-kernel statement。

若要把它提升成特定 whole-space solution class 的 global realizability statement，還需控制全部 conjugate modes與其他 simultaneous triads；本文不做該過強宣稱。

---

# 11. Restricted observation no-go

定義觀察語境：

$$
\Gamma_{\rm triad,amp}
$$

要求保存：

- $|k|,|p|,|q|$；
- triad angles；
- modal magnitudes；
- signed energy transfer。

限制 observation class：

$$
\mathcal Q_{\rm amp/geom}
$$

只能讀：

- radial geometry；
- angle geometry；
- modal amplitudes；

但不讀 relative complex phase。

由 Phase-Sign Flexibility：

存在相同 amplitude/geometry observation 對應：

$$
\mathcal T>0
$$

及：

$$
\mathcal T<0.
$$

所以：

$$
\boxed{
\mathsf X_{\Gamma_{\rm triad,amp}}
}
\tag{11.1}
$$

在此 restricted class 中成立。

repair 至少需要加入：

$$
\boxed{
\Phi
}
$$

或與：

$$
\sin\Phi
$$

等價的 signed phase-coherence carrier。

---

# 12. Connection back to strain spectral measure

Fourier strain：

$$
\boxed{
\widehat S_{ij}(k)
=
\frac{i}{2}
\left(
k_j\widehat u_i(k)
+
k_i\widehat u_j(k)
\right).
}
\tag{12.1}
$$

由：

$$
k\cdot\widehat u(k)=0,
$$

可算得：

$$
\boxed{
|\widehat S(k)|^2
=
\frac12
|k|^2
|\widehat u(k)|^2.
}
\tag{12.2}
$$

若：

$$
N_u(k)
$$

為 velocity nonlinear Fourier RHS，

則 strain nonlinear RHS 是：

$$
N_S
=
\operatorname{sym}
(ik\otimes N_u).
$$

同樣計算得到：

$$
\boxed{
\operatorname{Re}
\left(
N_S:
\overline{\widehat S}
\right)
=
\frac12
|k|^2
\operatorname{Re}
\left(
N_u\cdot
\overline{\widehat u}
\right).
}
\tag{12.3}
$$

因此在：

$$
\widehat u(k)\neq0
$$

處，normalized local nonlinear growth rate相同：

$$
\boxed{
\vartheta_S(k)
=
\vartheta_u(k).
}
\tag{12.4}
$$

所以 Round 08 的：

$$
\vartheta
$$

可以直接用本輪 velocity triad kernel表示。

---

# 13. Round 08 analytic strain weight as a velocity weight

Round 08/07 strain spectral measure權重：

$$
e^{2\tau r}
r^{2s}
|\widehat S|^2.
$$

由 (12.2)：

$$
e^{2\tau r}
r^{2s}
|\widehat S|^2
=
\frac12
e^{2\tau r}
r^{2s+2}
|\widehat u|^2.
$$

所以定義 velocity-side positive weight：

$$
\boxed{
w_{\tau,s}(r)
=
\frac12
e^{2\tau r}
r^{2s+2}.
}
\tag{13.1}
$$

則 analytic strain normalization：

$$
G
=
\int
w_{\tau,s}(r_k)
|\widehat u(k)|^2
dk.
$$

---

# 14. Exact triad representation of the covariance numerator

由：

$$
\vartheta(k)
=
\frac{
\Theta(k)
}{
|\widehat u(k)|^2
}
$$

在非零 mode 上，

有：

$$
\boxed{
G
\operatorname{Cov}_\mu(r,\vartheta)
=
\int
w_k
(r_k-m)
\Theta(k)
\,dk.
}
\tag{14.1}
$$

再代入：

$$
\Theta(k)
=
\int
\mathcal T(k;p,q)dp,
$$

得到：

$$
\boxed{
G
\operatorname{Cov}_\mu(r,\vartheta)
=
\iint
w_k
(r_k-m)
\mathcal A(k;p,q)
\sin\Phi(k;p,q)
\,dp\,dk.
}
\tag{14.2}
$$

這就是 Round 08 抽象 covariance 的 actual NS continuous-triad form。

---

# 15. Exact continuous triad threshold for $\zeta$

Round 08：

$$
\zeta
=
\frac{
\operatorname{Cov}_\mu(r,\vartheta)
}{
\nu
\operatorname{Cov}_\mu(r,r^2)
}.
$$

利用 (14.2)：

$$
\boxed{
\zeta_{\tau,s}
=
\frac{
\displaystyle
\iint
w_k(r_k-m)
\mathcal A
\sin\Phi
\,dp\,dk
}{
\displaystyle
\nu G
\operatorname{Cov}_\mu(r,r^2)
}.
}
\tag{15.1}
$$

所以：

$$
\boxed{
\zeta\le1
}
$$

等價於：

$$
\boxed{
\iint
w_k(r_k-m)
\mathcal A
\sin\Phi
\,dp\,dk
\le
\nu G
\operatorname{Cov}_\mu(r,r^2).
}
\tag{15.2}
$$

這就是目前 Pure-C route 真正缺的 signed triad inequality。

它不再含 abstract：

$$
\vartheta.
$$

---

# 16. What incompressibility and triad geometry already give

由 Sections 6–9，

triad amplitude滿足：

$$
\boxed{
\mathcal A
\le
|q|
\sin\theta_{pq}
|\widehat u(p)|
|\widehat u(q)|
|\widehat u(k)|.
}
\tag{16.1}
$$

且 spectral weight difference只能跨：

$$
\boxed{
||k|-|q||
\le
|p|.
}
\tag{16.2}
$$

所以 dangerous positive covariance需要：

$$
\boxed{
\text{radial displacement}
+
\text{non-collinearity}
+
\text{amplitude overlap}
+
\text{positive phase coherence}.
}
\tag{16.3}
$$

如果任一項持續退化：

- radial displacement $\to0$；
- angle $\to0$；
- amplitude overlap $\to0$；
- $\sin\Phi$ phase cancellation；

則其 triad contribution被抑制。

---

# 17. But these geometric factors do not give a uniform positive tax

No-Free-Radial-Jump 與 Collinear Null提供：

$$
\boxed{
\text{upper-envelope suppression}.
}
$$

但它們不提供：

$$
\boxed{
\text{forward transfer必支付某個 strictly positive universal lower cost}.
}
$$

因為：

$$
\sin\theta_{pq}
$$

可以任意小，

而：

$$
\sin\Phi
$$

可正、可負、可接近零。

所以目前不能由 purely pointwise triad geometry推出：

$$
\zeta\le1.
$$

這是重要 no-go：

$$
\boxed{
\text{triad geometry constrains magnitude but not signed global covariance}.
}
\tag{17.1}
$$

---

# 18. Energy conservation alone does not select cascade direction

Global nonlinear energy conservation只給：

$$
\int\Theta(k)dk=0.
$$

它表示 gain 與 loss必平衡。

但對 increasing spectral observation weight：

$$
w(r),
$$

仍可能有：

$$
\int
w(r)\Theta(k)dk
>0
$$

或：

$$
<0,
$$

取決於 energy 被搬往較高或較低 frequency。

因此：

$$
\boxed{
\text{energy conservation}
\not\Rightarrow
\text{forward suppression}.
}
\tag{18.1}
$$

這與已知 triadic-interaction研究中不同 interaction classes可支持不同 transfer direction的現象一致。

所以 invariant conservation 本身不是足夠 coercive sign。

---

# 19. Continuous phase-coherence functional

定義 centered analytic triad weight：

$$
\boxed{
\mathcal W_m(k)
=
w_{\tau,s}(r_k)
(r_k-m).
}
\tag{19.1}
$$

定義 positive-amplitude measure：

$$
d\Gamma
=
\mathcal A(k;p,q)
\,dp\,dk.
$$

則 covariance numerator：

$$
\boxed{
\mathfrak C_{\rm triad}
=
\int
\mathcal W_m(k)
\sin\Phi
\,d\Gamma.
}
\tag{19.2}
$$

亦即：

$$
\boxed{
G
\operatorname{Cov}(r,\vartheta)
=
\mathfrak C_{\rm triad}.
}
\tag{19.3}
$$

因此真正的 high-frequency danger不是：

$$
\mathcal A
$$

大本身。

而是：

$$
\boxed{
\mathcal W_m
\text{ 與 }
\sin\Phi
\text{ 在 amplitude measure 下產生 sustained positive correlation}.
}
\tag{19.4}
$$

---

# 20. Phase-neutral cancellation criterion

若在 amplitude-weighted triad ensemble 中：

$$
\boxed{
\int
\mathcal W_m
\sin\Phi
\,d\Gamma
\le0,
}
\tag{20.1}
$$

則：

$$
\operatorname{Cov}(r,\vartheta)\le0,
$$

故：

$$
\zeta\le0<1.
$$

於：

$$
\tau'\le0
$$

時：

$$
m'<0
$$

對 nontrivial state。

更一般，

若：

$$
\boxed{
\int
\mathcal W_m
\sin\Phi
\,d\Gamma
\le
\nu G
\operatorname{Cov}(r,r^2),
}
\tag{20.2}
$$

則：

$$
m'\le0.
$$

所以 Pure-C closure已經被壓成：

$$
\boxed{
\text{continuous triad phase-coherence versus viscous dispersion}.
}
$$

---

# 21. A normalized dangerous coherence ratio

定義：

$$
\boxed{
\mathfrak Z_{\tau,s}
=
\frac{
\displaystyle
\int
\mathcal W_m
\sin\Phi
\,d\Gamma
}{
\displaystyle
\nu G
\operatorname{Cov}(r,r^2)
}.
}
\tag{21.1}
$$

由 (19.3)：

$$
\boxed{
\mathfrak Z_{\tau,s}
=
\zeta_{\tau,s}.
}
\tag{21.2}
$$

但新表示揭露了 $\zeta$ 原本隱藏的內容：

$$
\boxed{
\zeta
=
\text{signed phase-coherent triad transfer}
/\text{viscous spectral dispersion}.
}
$$

所以 Round 08 的 abstract ratio現在已具有 explicit NS geometry。

---

# 22. STOP-C13 — Triad Phase-Coherence / Commutator-Sign Gap

定義：

$$
\boxed{
\bot_X^{\mathrm{C13}}
=
\left\langle
\begin{array}{l}
\text{layer}
=
\mathrm{continuous\ Fourier\ triad\ transfer},
\\
\text{exact\ kernel}
=
\mathcal T
=
\mathcal A\sin\Phi,
\\
\text{weight\ mechanism}
=
a_k(a_k-a_q),
\\
\text{radial\ constraint}
=
||k|-|q||\le|p|,
\\
\text{angular\ null}
=
\theta_{pq}=0,\pi
\Rightarrow
\mathcal T=0,
\\
\text{conservation}
=
\int\Theta(k)dk=0,
\\
\text{missing}
=
\mathrm{unconditional\ bound\ on\ signed\ phase\text{-}coherent\ weighted\ triad\ integral},
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
\textbf{STOP-C13:
Triad Phase-Coherence / Commutator-Sign Gap}.
}
$$

---

# 23. Observation-axis update

Round 03：

$$
\mathsf X_{\Gamma_{\rm amp}}
$$

顯示 strain amplitude不足以保存 nonlinear sign。

Round 08：

$$
\mathsf X_{\Gamma_\alpha}
$$

顯示 mean nonlinear growth不足以保存 spectral drift。

Round 09：

$$
\boxed{
\mathsf X_{\Gamma_{\rm triad,amp}}
}
$$

顯示 frequency geometry + modal amplitude仍不足以保存 signed triad transfer。

所以 observation state 必須至少包含：

$$
\boxed{
\text{relative phase/coherence}.
}
$$

目前信息鏈：

$$
\boxed{
\text{amplitude}
\to
\text{geometry}
\to
\text{frequency distribution}
\to
\text{phase coherence}.
}
\tag{23.1}
$$

這是 Pure-C 路線的重要信息層級。

---

# 24. Still no essential discrete intrusion

本輪所有 triads 直接由：

$$
p\in\mathbb R^3
$$

連續積分。

沒有：

- shell index；
- mode graph；
- dyadic decomposition；
- discrete helical class作為證明必要步；
- finite triad enumeration。

因此：

$$
\boxed{
T_{\mathsf C\to\mathsf D}
=
\text{NOT YET REACHED}.
}
\tag{24.1}
$$

Pure-C route目前：

$$
\boxed{
\begin{aligned}
\mathsf C_{\rm energy}
&\to
\mathsf C_{\rm critical}
\\
&\to
\mathsf C_{\rm relational}
\\
&\to
\mathsf C_{\rm nonlocal}
\\
&\to
\mathsf C_{\rm projected}
\\
&\to
\mathsf C_{\rm gradient\ geometry}
\\
&\to
\mathsf C_{\rm hierarchy}
\\
&\to
\mathsf C_{\rm Gevrey}
\\
&\to
\mathsf C_{\rm covariance}
\\
&\to
\mathsf C_{\rm triad\ phase}.
\end{aligned}
}
\tag{24.2}
$$

---

# 25. 24/72 Ledger — Round 09

| Step | X object / operation | $B$ | $U$ | $O$ | $L$ | status |
|---|---|---|---|---|---|---|
| C85 | Fourier NS convolution | $\mathsf C$ | $\mathsf P$ continuous convolution | relational | $\mathsf F$ | EXACT |
| C86 | triad transfer $\mathcal T$ | $\mathsf C$ | triadic | targeted | $\mathsf F$ | EXACT |
| C87 | total nonlinear energy conservation | $\mathsf C$ | global | scalar | $\mathsf F$ | EXACT |
| C88 | multiplier commutator identity | $\mathsf C$ | weighted | relational | $\mathsf F$ | EXACT |
| C89 | no-free-radial-jump | $\mathsf C$ | geometry | scalar | $\mathsf F$ | PROVED |
| C90 | collinear triad null | $\mathsf C$ | geometry | scalar | $\mathsf F$ | PROVED |
| C91 | phase decomposition $\mathcal T=\mathcal A\sin\Phi$ | $\mathsf C$ | relational | $\mathsf X$ | $\mathsf F$ | EXACT |
| C92 | geometry/amplitude determines transfer sign | $\mathsf C$ | — | amplitude/geometry only | $\mathsf F$ | REFUTED as observation architecture |
| C93 | strain/velocity transfer equivalence | $\mathsf C$ | linear relation | targeted | $\mathsf F$ | PROVED |
| C94 | covariance triad representation | $\mathsf C$ | global continuous triads | $\mathsf X$ | $\mathsf F$ | EXACT |
| C95 | phase-coherent triad threshold | $\mathsf C$ | feedback | targeted | $\mathsf F$ | EXACT reformulation |
| C96 | unconditional signed triad inequality | $\mathsf C$ | continuous triads | targeted | $\mathsf F$ | OPEN / STOP-C13 |

---

# 26. What has actually been learned

Round 08 的問題：

$$
\operatorname{Cov}(r,\vartheta)
\stackrel{?}{\le}
\nu\operatorname{Cov}(r,r^2).
$$

Round 09 已經把左側完全展開：

$$
\boxed{
G
\operatorname{Cov}(r,\vartheta)
=
\iint
w_k(r_k-m)
\mathcal A
\sin\Phi
\,dp\,dk.
}
$$

所以 missing theorem不再是：

> 控制某個抽象 covariance。

而是：

$$
\boxed{
\textbf{
control the signed phase-coherent continuous triad integral.
}
}
$$

此外：

- radial jumps不是免費的；
- collinear triads不傳輸；
- total energy只重分配不創造；
- 但 relative phase可以翻轉 transfer sign。

因此現在最小 unresolved information已從 amplitude / geometry 推進到：

$$
\boxed{
\textbf{phase organization across the continuous triad field}.
}
$$

---

# 27. Next round — continuous triad phase dynamics

下一輪直接研究：

$$
\boxed{
\Phi(k;p,q,t)
}
$$

的 dynamics。

不能只對單一 triad做 isolated ODE，因 full NS 中每個 mode同時參與 continuum many triads。

下一輪目標：

1. 定義 modal amplitude–phase：

$$
\widehat u(k)
=
R_k
e^{i\phi_k}
e_k
$$

的 gauge-safe版本；

2. 將：

$$
\Phi
$$

寫成 mode phases + polarization geometry；

3. 推導：

$$
\partial_t\Phi
$$

的 exact / admissible form；

4. 判定 phase coherence是否有 self-dephasing mechanism；

5. 若 differentiation of triad phase引入 quadruple interaction / nested convolution，檢查是否可以再做 continuous resummation；

6. 若 phase dynamics最終只能以離散 helical sign class或 shell graph closure，才記：

$$
T_{\mathsf C\to\mathsf D}.
$$

目前仍不允許因「文獻常用 shell」就提前離散化。

---

# 28. External primary-source anchors

1. Ganapati Sahoo, Luca Biferale, *Disentangling the triadic interactions in Navier-Stokes equations*, arXiv:1510.09006.
   - Fourier/helical triad structure；
   - different triad classes can contribute to different transfer directions；
   - competition of triadic interaction types.

2. Nicholas M. Rathmann, Peter D. Ditlevsen, *The role of helicity in triad interactions in 3D turbulence investigated in a new shell model*, arXiv:1602.02553.
   - Fourier/helical triads；
   - energy and helicity conservation within nonlinear triadic interactions as the structural starting point.

3. Fabian Waleffe, *The nature of triad interactions in homogeneous turbulence*, Physics of Fluids A 4, 350 (1992).
   - classical exact helical decomposition and triad-instability analysis.
   - 本輪不使用 helical sign classification 作證明必要工具；僅作 triad-structure external anchor.

The commutator, angular-null, phase-flexibility, and covariance-triad formulas in this checkpoint are direct derivations in the present route.

---

# 29. Commit state

$$
\boxed{
\begin{aligned}
\text{Route}
&:
\mathrm{Pure\ Continuous\ Fourier\ Triad\ Geometry},
\\
\text{Essential }\mathsf C\to\mathsf D
&:
\mathrm{Not\ reached},
\\
\text{Abstract transfer rate}
&:
\mathrm{expanded\ into\ actual\ NS\ triads},
\\
\text{Exact weighted mechanism}
&:
\mathrm{transport\text{-}multiplier\ commutator},
\\
\text{Radial jump}
&:
\mathrm{mediator\text{-}limited},
\\
\text{Collinear triad}
&:
\mathrm{null},
\\
\text{Signed transfer}
&:
\mathcal A\sin\Phi,
\\
\text{Geometry + amplitude}
&:
\mathrm{insufficient\ for\ sign},
\\
\text{Round08 }\zeta
&:
\mathrm{signed\ phase\text{-}coherent\ triad\ ratio},
\\
\text{STOP-C13}
&:
\mathrm{Triad\ Phase\text{-}Coherence/Commutator\text{-}Sign\ Gap},
\\
\text{Next}
&:
\mathrm{Continuous\ Triad\ Phase\ Dynamics}.
\end{aligned}
}
$$
