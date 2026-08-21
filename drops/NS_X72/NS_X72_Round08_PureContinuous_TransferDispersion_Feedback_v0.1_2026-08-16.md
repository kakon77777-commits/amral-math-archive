# NS × X 積分 × 24/72 範式實戰
## Round 08 — Pure Continuous Transfer–Dispersion Feedback Route

- 日期：2026-08-16
- 版本：v0.1
- 狀態：Proof-Route Experiment / Continuous-Only Spectral-Feedback Branch
- canonical source：UTF-8 Markdown
- canonical math delimiters：inline `$...$`；display `$$...$$`
- 前一輪：`NS_X72_Round07_PureContinuous_Gevrey_AnalyticRadiusBudget_v0.1_2026-08-16.md`
- 本輪目標：檢驗 Round 07 提出的「spectral variance 是否自動形成 analytic-radius 負回饋」假說。建立 analytic-weighted spectral measure 的 exact moment evolution，區分 mean-frequency damping、variance dynamics 與 nonlinear transfer-frequency covariance。
- 非主張：本文沒有證明 Navier–Stokes nonlinear transfer covariance 的無條件上界。本文的 strongest result 是把該缺口壓成一個精確 continuous covariance inequality。

---

# 0. Round 07 handoff

Round 07 定義 Gevrey carrier：

$$
\mathcal G_{\tau,s}
=
\left\|
e^{\tau\Lambda}
\Lambda^sS
\right\|_2^2
$$

及 analytic spectral probability measure：

$$
d\mu_{\tau,s}(\xi)
=
\frac{
e^{2\tau|\xi|}
|\xi|^{2s}
|\widehat S(\xi)|^2
}{
\mathcal G_{\tau,s}
}
d\xi.
$$

令：

$$
r=|\xi|.
$$

定義：

$$
m
=
\mathbb E_\mu[r],
$$

$$
\kappa
=
\mathbb E_\mu[r^2],
$$

$$
V
=
\operatorname{Var}_\mu(r)
=
\kappa-m^2.
$$

weighted nonlinear growth rate：

$$
g
=
\frac{
T_{\tau,s}
}{
\mathcal G_{\tau,s}
},
$$

以及：

$$
\alpha
=
\frac{
g
}{
\nu\kappa
}.
$$

Round 07 exact norm law：

$$
\boxed{
\frac12
\frac d{dt}
\log\mathcal G_{\tau,s}
=
\nu(\alpha-1)\kappa
+
\tau'm.
}
\tag{0.1}
$$

並提出 analytic-radius tax：

$$
\rho
=
\nu
(\alpha-1)_+
\frac{\kappa}{m}.
$$

選：

$$
\tau'=-\rho
$$

可使：

$$
\mathcal G_{\tau(t),s}
$$

不增加。

Round 07 STOP：

$$
\boxed{
\text{STOP-C11}
=
\text{Analytic-Radius Budget Exhaustion Gap}.
}
$$

本輪問：

> spectral variance 是否會自動壓低 high-frequency drift，從而阻止 radius budget 被吃光？

---

# 1. Exact weighted spectral replicator identity

projected strain equation：

$$
\partial_tS
+
\nu\Lambda^2S
=
F.
$$

在 Fourier space，令：

$$
e(\xi,t)
=
|\widehat S(\xi,t)|^2,
$$

$$
h(\xi,t)
=
\operatorname{Re}
\left(
\widehat F(\xi,t):
\overline{\widehat S(\xi,t)}
\right).
$$

在：

$$
e>0
$$

處定義 local nonlinear transfer rate：

$$
\boxed{
\vartheta(\xi,t)
=
\frac{h(\xi,t)}{e(\xi,t)}.
}
\tag{1.1}
$$

在：

$$
e=0
$$

處令：

$$
\vartheta=0.
$$

因：

$$
\partial_te
=
-2\nu r^2e
+
2h,
$$

而 analytic weight：

$$
w_{\tau,s}
=
e^{2\tau r}r^{2s}
$$

滿足：

$$
\partial_tw_{\tau,s}
=
2\tau' r w_{\tau,s},
$$

所以：

$$
\partial_t(w_{\tau,s}e)
=
2
\left(
\vartheta
-
\nu r^2
+
\tau'r
\right)
w_{\tau,s}e.
$$

定義：

$$
\boxed{
\Psi
=
\vartheta
-
\nu r^2
+
\tau'r.
}
\tag{1.2}
$$

則對任何足夠可積分、只依賴 $r$ 的 test observable：

$$
\phi(r),
$$

有 exact probability-measure evolution：

$$
\boxed{
\frac d{dt}
\mathbb E_\mu[\phi]
=
2
\operatorname{Cov}_\mu
\left(
\phi,
\Psi
\right).
}
\tag{1.3}
$$

這是本輪所有 moment equations 的母式。

---

# 2. Exact mean-frequency equation

取：

$$
\phi(r)=r.
$$

得到：

$$
\boxed{
m'
=
2
\operatorname{Cov}(r,\vartheta)
-
2\nu
\operatorname{Cov}(r,r^2)
+
2\tau'V.
}
\tag{2.1}
$$

此式把 mean-frequency drift 精確拆成三個 channel：

1. nonlinear transfer-frequency covariance：

$$
\operatorname{Cov}(r,\vartheta);
$$

2. viscous frequency damping：

$$
-\nu\operatorname{Cov}(r,r^2);
$$

3. analytic-radius reweighting：

$$
\tau'V.
$$

若：

$$
\tau'\le0,
$$

第三項永遠非正。

---

# 3. Universal viscous covariance lower bound

## Lemma 3.1

對任意 probability measure on：

$$
r\ge0,
$$

有：

$$
\boxed{
\operatorname{Cov}(r,r^2)
=
\mathbb E
\left[
(r-m)^2(r+m)
\right].
}
\tag{3.1}
$$

### Proof

展開右側：

$$
(r-m)^2(r+m)
=
r^3
-
mr^2
-
m^2r
+
m^3.
$$

取期望：

$$
\mathbb E[r^3]
-
m\mathbb E[r^2]
-
m^3
+
m^3
$$

即：

$$
\operatorname{Cov}(r,r^2).
$$

證畢。

因：

$$
r+m\ge m,
$$

得到：

$$
\boxed{
\operatorname{Cov}(r,r^2)
\ge
mV.
}
\tag{3.2}
$$

因此 pure diffusion 對 mean frequency 的 damping 至少為：

$$
\boxed{
2\nu mV.
}
\tag{3.3}
$$

---

# 4. Strict positivity in the nontrivial $L^2$ spectral class

在目前 smooth finite-energy whole-space class，

$$
\widehat S
$$

是普通 $L^2$ function。

若：

$$
V=0,
$$

則：

$$
r=m
$$

對 $\mu$-almost every frequency 成立。

因此 spectral mass 必完全支撐於 sphere：

$$
|\xi|=m.
$$

但該 sphere 在：

$$
\mathbb R^3
$$

中具有 Lebesgue measure zero。

由於：

$$
\mu
$$

對 Lebesgue measure absolutely continuous，

非零 $L^2$ state 不可能把全部 mass 支撐於一個 sphere。

故對 nontrivial state：

$$
\boxed{
V>0.
}
\tag{4.1}
$$

同理：

$$
m>0.
$$

因此：

$$
\boxed{
\operatorname{Cov}(r,r^2)>0
}
\tag{4.2}
$$

對 nontrivial analytic-weighted strain state 成立。

這表示 pure viscosity 嚴格把 mean frequency 往下推。

---

# 5. Mean-Frequency Feedback Theorem

若：

$$
\tau'\le0,
$$

由 (2.1)、(3.2)：

$$
m'
\le
2
\operatorname{Cov}(r,\vartheta)
-
2\nu mV.
$$

因此：

$$
\boxed{
\operatorname{Cov}(r,\vartheta)
\le
\nu mV
\quad
\Longrightarrow
\quad
m'\le0.
}
\tag{5.1}
$$

反過來：

$$
\boxed{
m'>0
\quad
\Longrightarrow
\quad
\operatorname{Cov}(r,\vartheta)
>
\nu
\operatorname{Cov}(r,r^2)
\ge
\nu mV
}
\tag{5.2}
$$

若：

$$
\tau'\le0.
$$

命名：

$$
\boxed{
\textbf{Mean-Frequency Feedback Theorem}.
}
$$

直觀：

> 要把 analytic-weighted spectral mean 往高頻推，非線性不能只「平均變強」；它必須 preferentially 把更大的 normalized growth rate 給更高的 frequency，而且這個 covariance 必須壓過 viscosity 的 universal monotone covariance。

---

# 6. Transfer–Dispersion Ratio

定義：

$$
\boxed{
\zeta_{\tau,s}
=
\frac{
\operatorname{Cov}(r,\vartheta)
}{
\nu
\operatorname{Cov}(r,r^2)
}.
}
\tag{6.1}
$$

對 nontrivial state denominator 嚴格正。

則 mean-frequency law 可寫成：

$$
\boxed{
m'
=
2\nu
\operatorname{Cov}(r,r^2)
(\zeta_{\tau,s}-1)
+
2\tau'V.
}
\tag{6.2}
$$

所以：

$$
\boxed{
\zeta_{\tau,s}\le1
\quad\text{且}\quad
\tau'\le0
\Longrightarrow
m'\le0.
}
\tag{6.3}
$$

因此：

$$
\boxed{
\zeta=1
}
$$

是 mean-frequency cascade 的 exact continuous threshold。

---

# 7. $\alpha$ and $\zeta$ measure different information

Recall：

$$
\alpha
=
\frac{
\mathbb E[\vartheta]
}{
\nu\mathbb E[r^2]
}.
$$

所以：

$$
\alpha
$$

只看 average nonlinear growth。

而：

$$
\zeta
$$

看：

$$
\operatorname{Cov}(r,\vartheta),
$$

也就是 nonlinear growth 是否 preferentially 偏向 higher frequency。

因此：

$$
\boxed{
\alpha
\neq
\zeta
}
$$

在 information content 上是根本不同的。

---

# 8. Observation-level no-go: $\alpha$ alone cannot determine spectral drift

固定任意 nondegenerate spectral probability measure：

$$
\mu
$$

with：

$$
V>0.
$$

固定 desired mean transfer：

$$
c.
$$

考慮兩個 abstract transfer profiles：

$$
\vartheta_+(r)
=
c
+
a(r-m),
$$

$$
\vartheta_-(r)
=
c
-
a(r-m),
$$

其中：

$$
a>0.
$$

兩者具有相同 mean：

$$
\boxed{
\mathbb E[\vartheta_+]
=
\mathbb E[\vartheta_-]
=
c.
}
\tag{8.1}
$$

因此對同一：

$$
\kappa
$$

有相同：

$$
\boxed{
\alpha_+
=
\alpha_-.
}
\tag{8.2}
$$

但：

$$
\operatorname{Cov}(r,\vartheta_+)
=
aV,
$$

$$
\operatorname{Cov}(r,\vartheta_-)
=
-aV.
$$

所以 mean-frequency nonlinear contribution方向相反。

因此在「只知道 $\alpha$、不保留 transfer-frequency relation」的 observation class 中：

$$
\boxed{
\alpha
\text{ is insufficient to determine spectral drift}.
}
\tag{8.3}
$$

重要限制：

這是一個 **observation architecture no-go**。

本文不主張：

$$
\vartheta_\pm
$$

都一定可由 actual Navier–Stokes convolution dynamics realize。

真正的 NS proof obligation 正是利用其 convolution / incompressibility structure 限制可實現的：

$$
\vartheta.
$$

---

# 9. A restricted $\mathsf X$ result appears again

令 observation context：

$$
\Gamma_{\alpha}
$$

要求同時保留：

$$
\mathbb E[\vartheta]
$$

與：

$$
\operatorname{sign}
\operatorname{Cov}(r,\vartheta).
$$

若容許 scalar observation class 只有：

$$
q=q(\alpha),
$$

則 Section 8 顯示：

同一：

$$
\alpha
$$

可以對應相反 covariance sign。

故：

$$
\boxed{
\mathsf X_{\Gamma_\alpha}
}
\tag{9.1}
$$

在此 restricted observation class 中成立。

repair 是把：

$$
\boxed{
(\alpha,\zeta)
}
$$

至少作為二維 targeted state。

---

# 10. Radial conditional transfer profile

因：

$$
r=|\xi|
$$

只依賴 radial frequency，

定義 transfer 的 conditional radial mean：

$$
\boxed{
\bar\vartheta(r)
=
\mathbb E[
\vartheta
\mid
|\xi|=r
].
}
\tag{10.1}
$$

形式上：

$$
\boxed{
\operatorname{Cov}(r,\vartheta)
=
\operatorname{Cov}
(r,\bar\vartheta(r)).
}
\tag{10.2}
$$

所以 angular complexity 對 mean-frequency drift 的作用，可以先壓成 radial conditional transfer profile。

這不表示 angular geometry 不重要。

它只表示對 observable：

$$
m'
$$

而言，angular information只透過：

$$
\bar\vartheta(r)
$$

進入。

---

# 11. Radial-slope sufficient condition

假設：

$$
\bar\vartheta(r)
$$

在 relevant spectral support 上 Lipschitz：

$$
|
\bar\vartheta(r_1)
-
\bar\vartheta(r_2)
|
\le
L
|r_1-r_2|.
$$

對 independent copies：

$$
R,R'\sim\mu,
$$

有 covariance identity：

$$
\operatorname{Cov}
(R,\bar\vartheta(R))
=
\frac12
\mathbb E
\left[
(R-R')
(
\bar\vartheta(R)
-
\bar\vartheta(R')
)
\right].
$$

故：

$$
\boxed{
\operatorname{Cov}(r,\vartheta)
\le
LV.
}
\tag{11.1}
$$

若：

$$
\boxed{
L\le\nu m,
}
\tag{11.2}
$$

則：

$$
\operatorname{Cov}(r,\vartheta)
\le
\nu mV
\le
\nu
\operatorname{Cov}(r,r^2).
$$

因此：

$$
\boxed{
L\le\nu m,
\quad
\tau'\le0
\Longrightarrow
m'\le0.
}
\tag{11.3}
$$

所以一個足夠的 continuous anti-cascade condition 是：

$$
\boxed{
\operatorname{Lip}_r
\bar\vartheta
\le
\nu m.
}
\tag{11.4}
$$

本輪沒有證明 actual NS transfer profile 無條件滿足此 bound。

---

# 12. Variance evolution

由母式 (1.3)：

$$
V
=
\mathbb E[(r-m)^2].
$$

直接得到：

$$
\boxed{
V'
=
2
\operatorname{Cov}
\left(
(r-m)^2,
\vartheta
\right)
-
2\nu
\operatorname{Cov}
\left(
(r-m)^2,
r^2
\right)
+
2\tau'
\operatorname{Cov}
\left(
(r-m)^2,
r
\right).
}
\tag{12.1}
$$

這三個 covariance 一般都沒有固定 sign。

因此：

$$
\boxed{
V
}
$$

本身不是由形式結構保證的 monotone Lyapunov quantity。

---

# 13. Counterexample: pure diffusion need not monotonically decrease variance

考慮 abstract radial probability measure supported on：

$$
r\in\{0,1\}
$$

with：

$$
\mathbb P(r=1)=p,
$$

$$
\mathbb P(r=0)=1-p.
$$

則：

$$
m=p,
$$

$$
V=p(1-p).
$$

並可直接計算：

$$
\operatorname{Cov}
\left(
(r-m)^2,
r^2
\right)
=
p(1-p)(1-2p).
$$

若：

$$
p>\frac12,
$$

則：

$$
\operatorname{Cov}
\left(
(r-m)^2,
r^2
\right)
<0.
$$

在 pure diffusion：

$$
\vartheta=0,
\qquad
\tau'=0
$$

下：

$$
V'
=
-2\nu
\operatorname{Cov}
\left(
(r-m)^2,
r^2
\right)
>0.
$$

所以：

$$
\boxed{
\textbf{
spectral variance itself can initially increase even under pure diffusion.
}
}
\tag{13.1}
$$

此 two-point measure 不是 smooth $L^2$ Fourier density。

但可用兩個非常窄的 smooth radial annuli approximation，使該 initial sign persistence 成立。

因此本輪修正 Round 07 的直觀猜想：

> viscosity 不是透過「讓 variance 必然下降」形成 feedback。

真正 guaranteed 的是：

$$
\boxed{
\text{viscosity makes the spectral mean drift downward},
}
$$

因：

$$
\operatorname{Cov}(r,r^2)>0.
$$

---

# 14. Two distinct continuous danger coordinates

定義 analytic weighted log-amplitude：

$$
\boxed{
L_G
=
\frac12
\log
\mathcal G_{\tau,s}.
}
$$

由 Round 07：

$$
\boxed{
L_G'
=
D_{\rm amp}
+
\tau'm,
}
\tag{14.1}
$$

其中：

$$
\boxed{
D_{\rm amp}
=
\mathbb E[\vartheta]
-
\nu
\mathbb E[r^2]
=
\nu
(\alpha-1)\kappa.
}
\tag{14.2}
$$

另一方面：

$$
\boxed{
\frac12m'
=
D_{\rm shift}
+
\tau'V,
}
\tag{14.3}
$$

其中：

$$
\boxed{
D_{\rm shift}
=
\operatorname{Cov}(r,\vartheta)
-
\nu
\operatorname{Cov}(r,r^2).
}
\tag{14.4}
$$

所以 analytic danger 其實至少有兩個不同座標：

$$
\boxed{
D_{\rm amp}
}
$$

與：

$$
\boxed{
D_{\rm shift}.
}
$$

第一個問：

> analytic weighted mass 是否增長？

第二個問：

> analytic weighted mean frequency 是否往高頻移動？

它們不能被單一：

$$
\alpha
$$

無損取代。

---

# 15. Radius control acts on both channels

radius change：

$$
\tau'
$$

對兩個 observables 的作用是：

$$
\boxed{
\begin{pmatrix}
L_G'
\\[0.3em]
\frac12m'
\end{pmatrix}
=
\begin{pmatrix}
D_{\rm amp}
\\[0.3em]
D_{\rm shift}
\end{pmatrix}
+
\tau'
\begin{pmatrix}
m
\\[0.3em]
V
\end{pmatrix}.
}
\tag{15.1}
$$

若：

$$
\tau'<0,
$$

則 shrinking analytic radius 同時：

1. 降低 analytic weighted norm growth；
2. 降低 weighted mean-frequency drift。

這提供一個二維 continuous feedback picture。

---

# 16. Joint compensation tax

因 nontrivial state 有：

$$
m>0,
\qquad
V>0,
$$

定義：

$$
\boxed{
\rho_{\rm joint}
=
\max
\left\{
\frac{
(D_{\rm amp})_+
}{
m
},
\;
\frac{
(D_{\rm shift})_+
}{
V
}
\right\}.
}
\tag{16.1}
$$

選：

$$
\boxed{
\tau'
=
-\rho_{\rm joint}.
}
\tag{16.2}
$$

則由 (15.1)：

$$
\boxed{
L_G'\le0,
}
\tag{16.3}
$$

並且：

$$
\boxed{
m'\le0.
}
\tag{16.4}
$$

命名：

$$
\boxed{
\textbf{Joint Analytic-Amplitude / Mean-Frequency Compensation Law}.
}
$$

注意：

此 joint tax 比 Round 07 只控制：

$$
L_G
$$

的 minimal amplitude tax 更保守。

它的用途是同時固定兩個 observables，而不是宣稱它是最佳 continuation control。

---

# 17. Joint radius budget

沿：

$$
\tau'=-\rho_{\rm joint},
$$

有：

$$
\boxed{
\tau(t)
=
\tau_0
-
\int_{t_0}^t
\rho_{\rm joint}(\sigma)
d\sigma.
}
\tag{17.1}
$$

且：

$$
\boxed{
\mathcal G_{\tau(t),s}(t)
\le
\mathcal G_{\tau_0,s}(t_0),
}
\tag{17.2}
$$

$$
\boxed{
m(t)\le m(t_0).
}
\tag{17.3}
$$

若：

$$
\inf_{t<T_\ast}\tau(t)>0,
$$

則 Round 07 resummation theorem仍然給所有 finite Sobolev levels uniform control。

因此在這個 joint-control path 上，potential finite-time singularity 必要求：

$$
\boxed{
\int_{t_0}^{T_\ast}
\rho_{\rm joint}(t)dt
\ge
\tau_0.
}
\tag{17.4}
$$

這不是 contradiction。

但它把 danger budget拆成：

$$
\boxed{
\text{amplitude excess}
\vee
\text{frequency-shift excess}.
}
$$

---

# 18. What variance feedback actually proves

本輪原始希望是：

$$
\boxed{
V\text{ large}
\Longrightarrow
\text{automatic nonlinear suppression}.
}
$$

這個命題沒有被證明。

真正得到的是：

$$
\boxed{
V>0
}
$$

提供一個 viscous restoring scale：

$$
\nu mV.
$$

但 nonlinear term也有：

$$
\operatorname{Cov}(r,\vartheta).
$$

因此 negative feedback 的真正比較式是：

$$
\boxed{
\operatorname{Cov}(r,\vartheta)
\stackrel{?}{\le}
\nu
\operatorname{Cov}(r,r^2).
}
\tag{18.1}
$$

也就是：

$$
\boxed{
\zeta_{\tau,s}
\stackrel{?}{\le}
1.
}
\tag{18.2}
$$

所以 variance 不是答案。

variance 是 denominator / restoring resource。

真正的 Boss 是 nonlinear transfer 如何依賴 frequency。

---

# 19. STOP-C12 — Nonlinear Transfer–Dispersion Covariance Gap

定義：

$$
\boxed{
\bot_X^{\mathrm{C12}}
=
\left\langle
\begin{array}{l}
\text{layer}
=
\mathrm{analytic\ spectral\ feedback},
\\
\text{exact\ mean\ law}
=
m'
=
2\operatorname{Cov}(r,\vartheta)
-
2\nu\operatorname{Cov}(r,r^2)
+
2\tau'V,
\\
\text{viscous\ lower\ bound}
=
\operatorname{Cov}(r,r^2)
\ge
mV,
\\
\text{exact\ threshold}
=
\zeta_{\tau,s}=1,
\\
\text{missing}
=
\mathrm{unconditional\ NS\ bound\ on\ }
\operatorname{Cov}(r,\vartheta),
\\
\text{variance\ monotonicity}
=
\mathrm{false\ in\ general},
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
\textbf{STOP-C12:
Nonlinear Transfer–Dispersion Covariance Gap}.
}
$$

---

# 20. The Pure-C frontier is now extremely specific

Round 01：

$$
\mathrm{energy\ scale\ mismatch}.
$$

Round 02：

$$
\mathrm{critical\ amplitude\ gap}.
$$

Round 03：

$$
\mathrm{geometry\ feedback\ gap}.
$$

Round 04：

$$
\mathrm{nonlocal\ pressure\ gap}.
$$

Round 05：

$$
\mathrm{compressive\ gradient\ alignment}.
$$

Round 06：

$$
\mathrm{continuous\ hierarchy\ slope}.
$$

Round 07：

$$
\mathrm{analytic\ radius\ budget}.
$$

Round 08：

$$
\boxed{
\mathrm{transfer\text{-}frequency\ covariance}.
}
$$

所以目前 Pure-C 不再是一個模糊的：

> 能不能用 continuous method 證 NS？

而是：

$$
\boxed{
\textbf{
Can actual Navier–Stokes convolution geometry enforce
a transfer-frequency covariance bound strong enough
to keep }\zeta_{\tau,s}\le1
\textbf{ or make its positive excess integrable?}
}
\tag{20.1}
$$

---

# 21. No essential discrete intrusion

本輪使用：

$$
r\in[0,\infty),
$$

$$
\xi\in\mathbb R^3,
$$

continuous probability measure：

$$
\mu_{\tau,s},
$$

及 continuous covariance。

沒有：

- dyadic shell；
- discrete triad graph；
- countable scale sequence；
- Galerkin modes；
- profile extraction。

因此：

$$
\boxed{
T_{\mathsf C\to\mathsf D}
=
\text{NOT YET REACHED}.
}
\tag{21.1}
$$

Pure-C route 目前為：

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
\mathsf C_{\rm transfer\ covariance}.
\end{aligned}
}
$$

---

# 22. 24/72 Ledger — Round 08

| Step | X object / operation | $B$ | $U$ | $O$ | $L$ | status |
|---|---|---|---|---|---|---|
| C74 | spectral replicator identity | $\mathsf C$ | $\mathsf P$ spectral | $\mathsf X$ | $\mathsf F$ | EXACT |
| C75 | mean frequency $m$ | $\mathsf C$ | relational | targeted scalar | $\mathsf F$ | FORM |
| C76 | viscous covariance lower bound | $\mathsf C$ | — | targeted | $\mathsf F$ | PROVED |
| C77 | transfer–dispersion ratio $\zeta$ | $\mathsf C$ | relational | targeted scalar | $\mathsf F$ | FORM |
| C78 | $\zeta\le1\Rightarrow m'\le0$ | $\mathsf C$ | feedback | scalar | $\mathsf F$ | PROVED |
| C79 | $\alpha$ determines cascade sign | $\mathsf C$ | — | scalar | $\mathsf F$ | REFUTED as observation architecture |
| C80 | radial transfer slope condition | $\mathsf C$ | radial conditional | targeted | $\mathsf F$ | CONDITIONAL |
| C81 | variance monotone under viscosity | $\mathsf C$ | — | scalar | $\mathsf F$ | REFUTED in general spectral-measure class |
| C82 | two-danger state $(D_{\rm amp},D_{\rm shift})$ | $\mathsf C$ | relational | $\mathsf X$→2D targeted | $\mathsf F$ | FORM |
| C83 | joint compensation law | $\mathsf C$ | adaptive | targeted | $\mathsf F$ | PROVED |
| C84 | unconditional NS covariance bound | $\mathsf C$ | convolution | targeted | $\mathsf F$ | OPEN / STOP-C12 |

---

# 23. Next round — continuous Fourier triad geometry

下一輪不再研究 abstract：

$$
\vartheta.
$$

直接代回 actual Navier–Stokes Fourier nonlinearity。

Fourier velocity equation：

$$
\partial_t\widehat u(\xi)
+
\nu|\xi|^2\widehat u(\xi)
=
-
i
\mathbb P_\xi
\int_{\mathbb R^3}
(\xi\cdot\widehat u(\eta))
\widehat u(\xi-\eta)
\,d\eta
$$

可採等價 divergence-form convention重新整理。

下一輪目標：

$$
\boxed{
\textbf{Continuous Triad Geometry}.
}
$$

不使用 discrete triad graph。

直接在：

$$
(\xi,\eta,\xi-\eta)
\in
\mathbb R^3\times\mathbb R^3\times\mathbb R^3
$$

上問：

1. incompressibility projection：

$$
\mathbb P_\xi
$$

是否對 high-frequency transfer covariance 提供 cancellation；

2. triad geometry：

$$
\xi=\eta+(\xi-\eta)
$$

是否使 transfer to high $|\xi|$ 必須支付 angular / amplitude cost；

3. convolution symmetry 是否讓：

$$
\operatorname{Cov}(r,\vartheta)
$$

可改寫成 signed triad integral；

4. 是否存在 continuous antisymmetry，使 forward transfer 必伴隨某個 lower-frequency loss；

5. 能否把：

$$
\zeta>1
$$

推成另一個 rigid triad geometry；

6. 若所有有用估計最後必須把 frequency space切成 shells，才記錄真正：

$$
T_{\mathsf C\to\mathsf D}.
$$

---

# 24. External primary-source anchors

1. Dong Li, Ping Zhang, *On the refined analyticity radius of 3-D generalized Navier-Stokes equations*, arXiv:2406.10865.
   - Gevrey exponential Fourier weights；
   - critical/subcritical analyticity-radius lower bounds；
   - high-frequency-tail-sensitive analyticity analysis.

2. Ira Herbst, Erik Skibsted, *Analyticity estimates for the Navier-Stokes equations*, arXiv:0907.4351.
   - classical spatial analyticity-radius estimates for Navier–Stokes.

3. Cong Wang, *Space-time analyticity and refined analyticity radius of the Navier-Stokes equations in the critical Besov spaces*, arXiv:2503.03658.
   - modern critical-space Gevrey/analyticity-radius framework.

These sources anchor the use of analytic/Gevrey Fourier weights. The covariance identities and transfer–dispersion ratio in this checkpoint are direct derivations within the present route and are not attributed to those papers.

---

# 25. Commit state

$$
\boxed{
\begin{aligned}
\text{Route}
&:
\mathrm{Pure\ Continuous\ Transfer\text{-}Dispersion\ Feedback},
\\
\text{Essential }\mathsf C\to\mathsf D
&:
\mathrm{Not\ reached},
\\
\text{Variance}
&:
\mathrm{not\ monotone\ in\ general},
\\
\text{Guaranteed\ viscous\ feedback}
&:
\operatorname{Cov}(r,r^2)\ge mV,
\\
\text{Exact\ cascade\ ratio}
&:
\zeta_{\tau,s},
\\
\text{Mean-frequency threshold}
&:
\zeta=1,
\\
\text{Single }\alpha\text{ observation}
&:
\mathrm{insufficient\ for\ spectral\ drift},
\\
\text{Joint danger coordinates}
&:
(D_{\rm amp},D_{\rm shift}),
\\
\text{STOP-C12}
&:
\mathrm{Nonlinear\ Transfer\text{-}Dispersion\ Covariance\ Gap},
\\
\text{Next}
&:
\mathrm{Continuous\ Fourier\ Triad\ Geometry}.
\end{aligned}
}
$$
