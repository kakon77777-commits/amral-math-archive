# NS × X 積分 × 24/72 範式實戰
## Round 02 — Pure Critical Continuous Carrier Route

- 日期：2026-08-16
- 版本：v0.1
- 狀態：Proof-Route Experiment / Continuous-Only Critical Branch
- canonical source：UTF-8 Markdown
- canonical math delimiters：inline `$...$`；display `$$...$$`
- 前一輪：`NS_X72_Round01_PureContinuous_EnergyRoute_v0.1_2026-08-16.md`
- 本輪目標：在不引入本質離散工具的前提下，改用尺度臨界 carrier，測試是否可以穿過 Round 01 的 `STOP-C01` 與 `STOP-C02`，形成無條件 global regularity closure。
- 非主張：本輪只判定本文測試的純連續 critical-carrier architectures；不宣稱排除所有可能的純連續證明。

---

# 0. Round 01 handoff

Round 01 得到：

$$
\boxed{
u\in
L_t^\infty L_x^2
\cap
L_t^2\dot H_x^1
}
$$

以及 energy interpolation family：

$$
\boxed{
\frac2q+\frac3p=\frac32.
}
$$

而 Serrin critical line 為：

$$
\boxed{
\frac2q+\frac3p=1.
}
$$

因此：

$$
\boxed{
\text{STOP-C01}
=
\text{Energy-to-Critical Scaling Gap}.
}
$$

vorticity/enstrophy route則得到：

$$
Y(t)
=
\|\omega(t)\|_2^2,
$$

$$
Y'
\lesssim
\nu^{-3}Y^3,
$$

無法給 arbitrary-data global a priori bound，因此：

$$
\boxed{
\text{STOP-C02}
=
\text{Vortex-Stretching Coercivity Gap}.
}
$$

最重要的是：

$$
\boxed{
T_{\mathsf C\to\mathsf D}
=
\text{NOT YET REACHED}.
}
$$

本輪因此仍保持：

$$
\boxed{
B=\mathsf C.
}
$$

---

# 1. NS scaling 與 critical carrier

Navier–Stokes scaling：

$$
u_\lambda(x,t)
=
\lambda
u(\lambda x,\lambda^2 t),
$$

$$
p_\lambda(x,t)
=
\lambda^2
p(\lambda x,\lambda^2t).
$$

此 scaling 保持 viscosity $\nu$ 不變。

對 Lebesgue norm：

$$
\|u_\lambda(t)\|_{L^p}
=
\lambda^{1-\frac3p}
\|u(\lambda^2t)\|_{L^p}.
$$

因此：

$$
\boxed{
p=3
}
$$

是 velocity Lebesgue critical exponent：

$$
\boxed{
\|u_\lambda(t)\|_3
=
\|u(\lambda^2t)\|_3.
}
\tag{1.1}
$$

對 homogeneous Sobolev norm：

$$
\|u_\lambda(t)\|_{\dot H^s}
=
\lambda^{s-\frac12}
\|u(\lambda^2t)\|_{\dot H^s}.
$$

故：

$$
\boxed{
s=\frac12
}
$$

為 critical Sobolev index：

$$
\boxed{
\|u_\lambda(t)\|_{\dot H^{1/2}}
=
\|u(\lambda^2t)\|_{\dot H^{1/2}}.
}
\tag{1.2}
$$

對 mixed norm：

$$
\|u_\lambda\|_{L_t^qL_x^p}
=
\lambda^{1-\frac3p-\frac2q}
\|u\|_{L_t^qL_x^p}.
$$

因此：

$$
\boxed{
\frac2q+\frac3p=1
}
\tag{1.3}
$$

即為 scale-critical Serrin line。

本輪的策略是：

$$
\boxed{
\text{不再從 subcritical energy carrier 硬推 criticality；
直接在 critical layer 建立 X 積分鏈。}
}
$$

---

# 2. X 積分圖：critical formation 與 global control 必須分離

定義：

$$
X_{\rm crit}
=
\int_{\rm scaling}
X_{\rm NS}.
$$

可選的 continuous critical observations 包括：

$$
\mathcal A_{H}(u)
=
\|u\|_{\dot H^{1/2}},
$$

$$
\mathcal A_{3}(u)
=
\|u\|_{L^3},
$$

以及 critical Kato heat-flow norm。

本輪強制區分四個不同 X 積分步驟：

$$
\boxed{
\begin{aligned}
&\mathsf I_{\rm form}:
X_{\rm NS}
\rightsquigarrow
X_{\rm crit},
\\
&\mathsf I_{\rm local}:
X_{\rm crit}
\rightsquigarrow
\text{local strong solution},
\\
&\mathsf I_{\rm criterion}:
\text{bounded critical carrier}
\rightsquigarrow
\text{regularity},
\\
&\mathsf I_{\rm global}:
X_{\rm NS}
\rightsquigarrow
\text{global bounded critical carrier}.
\end{aligned}
}
\tag{2.1}
$$

前面三種能否成立，不能被偷換成第四種成立。

Navier–Stokes Millennium closure 真正缺的是：

$$
\boxed{
\mathsf I_{\rm global}.
}
\tag{2.2}
$$

---

# 3. Pure-Critical Route A — $\dot H^{1/2}$

令：

$$
\Lambda
=
(-\Delta)^{1/2}.
$$

定義：

$$
Y(t)
=
\|u(t)\|_{\dot H^{1/2}}^2
=
\|\Lambda^{1/2}u(t)\|_2^2,
$$

以及：

$$
Z(t)
=
\|u(t)\|_{\dot H^{3/2}}^2
=
\|\Lambda^{3/2}u(t)\|_2^2.
$$

對 Leray-projected NS：

$$
\partial_tu
-
\nu\Delta u
+
\mathbb P(u\cdot\nabla u)
=
0
$$

與 $\Lambda u$ 做 $L^2$ pairing：

$$
\boxed{
\frac12Y'(t)
+
\nu Z(t)
=
-
\langle
\mathbb P(u\cdot\nabla u),
\Lambda u
\rangle.
}
\tag{3.1}
$$

---

# 4. 不使用 dyadic decomposition 的連續 product estimate

本輪禁止以 Littlewood–Paley dyadic shell 作核心工具。

使用三維 Sobolev embedding：

$$
\dot H^{1/2}
\hookrightarrow
L^3,
$$

以及：

$$
\dot H^{3/2}
\ni u
\Longrightarrow
\nabla u\in\dot H^{1/2}
\hookrightarrow
L^3.
$$

因此：

$$
\|u\cdot\nabla u\|_{L^{3/2}}
\le
\|u\|_3
\|\nabla u\|_3
\le
C
\|u\|_{\dot H^{1/2}}
\|u\|_{\dot H^{3/2}}.
$$

由 dual Sobolev embedding：

$$
L^{3/2}
\hookrightarrow
\dot H^{-1/2},
$$

得到：

$$
\boxed{
\|
\mathbb P(u\cdot\nabla u)
\|_{\dot H^{-1/2}}
\le
C
\|u\|_{\dot H^{1/2}}
\|u\|_{\dot H^{3/2}}.
}
\tag{4.1}
$$

另一方面：

$$
\|\Lambda u\|_{\dot H^{1/2}}
=
\|u\|_{\dot H^{3/2}}.
$$

所以由 $\dot H^{-1/2}$–$\dot H^{1/2}$ dual pairing：

$$
\boxed{
\left|
\langle
\mathbb P(u\cdot\nabla u),
\Lambda u
\rangle
\right|
\le
C
\|u\|_{\dot H^{1/2}}
\|u\|_{\dot H^{3/2}}^2.
}
\tag{4.2}
$$

代入 (3.1)：

$$
\boxed{
\frac12Y'
+
\left(
\nu
-
C\sqrt{Y}
\right)
Z
\le
0.
}
\tag{4.3}
$$

這是本輪第一個 critical equality-interface。

---

# 5. Small-data closure

若：

$$
\|u_0\|_{\dot H^{1/2}}
\le
\delta_\nu
$$

且取：

$$
C\delta_\nu
\le
\frac{\nu}{2},
$$

則 bootstrap 區域內：

$$
\nu
-
C\|u(t)\|_{\dot H^{1/2}}
\ge
\frac{\nu}{2}.
$$

因此：

$$
\boxed{
\frac12Y'
+
\frac{\nu}{2}Z
\le
0.
}
\tag{5.1}
$$

故 critical norm 不增加，bootstrap 自閉合。

這恢復 Fujita–Kato 型 small-critical-data global mechanism 的核心 energy geometry：

$$
\boxed{
\text{critical carrier}
+
\text{small amplitude}
\Longrightarrow
\text{viscous absorption}.
}
\tag{5.2}
$$

---

# 6. Large-data barrier

若：

$$
C\|u(t)\|_{\dot H^{1/2}}
>
\nu,
$$

則 (4.3) 中的 coercive coefficient：

$$
\nu
-
C\|u(t)\|_{\dot H^{1/2}}
$$

失去正號。

所以 standard critical energy estimate 本身只能給：

$$
\boxed{
\text{smallness-conditioned coercivity}.
}
$$

它不能給：

$$
\boxed{
\text{arbitrary-amplitude coercivity}.
}
$$

因此：

$$
\boxed{
\Gamma_{\mathsf C,\dot H^{1/2}}
\not\vdash
\int_{\rm global\ coercivity}
X_{\dot H^{1/2}}
\;\operatorname{form}
}
\tag{6.1}
$$

在目前這套單 carrier estimate 下。

定義：

$$
\boxed{
\textbf{STOP-C03:
Critical-Amplitude Absorption Gap}.
}
\tag{6.2}
$$

注意：

$$
\boxed{
\text{STOP-C03}
\neq
\text{no large-data critical-space proof can exist}.
}
$$

它只排除目前的單一 $\dot H^{1/2}$ absorption architecture 作為無條件 closure。

---

# 7. Critical Scaling Fixed-Point Lemma

這裡出現一個比「estimate 不夠強」更結構性的事實。

由 (1.2)：

$$
\mathcal A_H(u)
=
\|u\|_{\dot H^{1/2}}
$$

滿足：

$$
\boxed{
\mathcal A_H(u_\lambda)
=
\mathcal A_H(u).
}
\tag{7.1}
$$

同樣：

$$
\boxed{
\mathcal A_3(u_\lambda)
=
\mathcal A_3(u).
}
\tag{7.2}
$$

因此若 critical absorption 要求：

$$
\mathcal A(u)
<
\delta,
$$

而原 state 滿足：

$$
\mathcal A(u)
\ge
\delta,
$$

則任何 NS symmetry scaling：

$$
u
\mapsto
u_\lambda
$$

都不能改變這件事。

所以：

$$
\boxed{
\textbf{
critical scaling cannot turn large critical data into small critical data.
}
}
\tag{7.3}
$$

這可以寫成 X 積分固定點：

$$
\boxed{
\mathsf I_{\rm scale}
\left(
\mathcal A_{\rm crit}
\right)
=
\mathcal A_{\rm crit}.
}
\tag{7.4}
$$

因此：

$$
\boxed{
\text{Scale}
}
$$

在 critical layer 不再是 amplitude-repair operator。

它只改變：

- spatial location of detail；
- temporal scale；
- physical amplitude and wavelength jointly；

但不改變 critical carrier 的大小。

這是本輪重要的 structural no-go。

---

# 8. Pure-Critical Route B — $L^\infty_tL^3_x$

$L^3$ 為 scaling-critical space。

已知 endpoint regularity theorem 表明：

對適當 Navier–Stokes strong / suitable weak solution，如果在有限時間窗保持：

$$
\boxed{
u\in L^\infty(0,T;L^3(\mathbb R^3)),
}
\tag{8.1}
$$

則不會在 $T$ 發生有限時間奇異。

因此，若我們能無條件證：

$$
\boxed{
\sup_{0<t<T_\ast}
\|u(t)\|_3
<
\infty
}
\tag{8.2}
$$

對每個有限 $T_\ast$ 成立，則 regularity closure 成立。

所以：

$$
\boxed{
\mathsf I_{\rm criterion}^{L^3}
}
$$

是合法的。

真正缺的是：

$$
\boxed{
\mathsf I_{\rm global}^{L^3}.
}
$$

---

# 9. Energy closure 到 $L^3$ 只能得到 $L_t^4$

Round 01 energy bounds：

$$
u\in
L_t^\infty L_x^2
\cap
L_t^2L_x^6.
$$

對每個時間：

$$
\|u(t)\|_3
\le
\|u(t)\|_2^{1/2}
\|u(t)\|_6^{1/2}.
$$

四次方：

$$
\|u(t)\|_3^4
\le
\|u(t)\|_2^2
\|u(t)\|_6^2.
$$

積分時間：

$$
\int_0^T
\|u(t)\|_3^4dt
\le
\left(
\sup_{0<t<T}
\|u(t)\|_2^2
\right)
\int_0^T
\|u(t)\|_6^2dt.
$$

所以：

$$
\boxed{
u\in L_t^4L_x^3.
}
\tag{9.1}
$$

但是：

$$
L^4(0,T)
\not\hookrightarrow
L^\infty(0,T).
$$

例如：

$$
f(t)
=
(T-t)^{-\alpha}
$$

對：

$$
0<\alpha<\frac14
$$

滿足：

$$
f\in L^4(0,T)
$$

但：

$$
\sup_{0<t<T}f(t)
=
\infty.
$$

因此，僅從 energy bounds：

$$
\boxed{
L_t^4L_x^3
\not\Rightarrow
L_t^\infty L_x^3.
}
\tag{9.2}
$$

這是 functional-space non-implication；它不主張 NS solution 必然真的產生該 spike。

所以：

$$
\boxed{
\Gamma_{\rm energy}
\not\vdash
\int_{L_t^\infty L_x^3}
X_{\rm energy}
\;\operatorname{form}.
}
\tag{9.3}
$$

定義：

$$
\boxed{
\textbf{STOP-C04:
Endpoint-in-Time Critical Control Gap}.
}
\tag{9.4}
$$

---

# 10. $\dot H^{1/2}$ 與 $L^3$ 的關係

Sobolev embedding：

$$
\boxed{
\dot H^{1/2}
\hookrightarrow
L^3.
}
\tag{10.1}
$$

所以若可以建立 uniform：

$$
\sup_{t<T}
\|u(t)\|_{\dot H^{1/2}}
<
\infty,
$$

則至少得到：

$$
\sup_{t<T}
\|u(t)\|_3
<
\infty.
$$

但是 Route A 已顯示 standard $\dot H^{1/2}$ energy architecture 只有 smallness-conditioned absorption。

因此 Route A 與 Route B 在目前架構下合流為：

$$
\boxed{
\text{unconditional global critical-amplitude control is missing}.
}
\tag{10.2}
$$

---

# 11. Pure-Critical Route C — Kato / Duhamel continuous route

寫 mild formulation：

$$
\boxed{
u(t)
=
e^{\nu t\Delta}u_0
-
\int_0^t
e^{\nu(t-s)\Delta}
\mathbb P\nabla\cdot
(u\otimes u)(s)
\,ds.
}
\tag{11.1}
$$

整條式子完全由：

- continuous time integral；
- continuous heat semigroup；
- continuous convolution；
- deterministic transition；

構成。

所以：

$$
\boxed{
B=\mathsf C,
\qquad
L=\mathsf F.
}
$$

仍未引入本質離散概念。

---

# 12. 以 $L^3\to L^6$ Kato norm 為例

定義：

$$
\boxed{
\|u\|_{\mathcal K_6(T)}
=
\sup_{0<t<T}
t^{1/4}
\|u(t)\|_6.
}
\tag{12.1}
$$

這個 norm 在 NS scaling 下保持不變。

Heat estimate：

$$
\|e^{\nu t\Delta}f\|_6
\le
C
(\nu t)^{-1/4}
\|f\|_3.
$$

因此：

$$
\boxed{
\|e^{\nu t\Delta}u_0\|_{\mathcal K_6(T)}
\le
C\nu^{-1/4}
\|u_0\|_3.
}
\tag{12.2}
$$

對 bilinear term：

$$
B(u,v)(t)
=
-
\int_0^t
e^{\nu(t-s)\Delta}
\mathbb P\nabla\cdot
(u\otimes v)(s)
\,ds.
$$

heat-kernel derivative estimate：

$$
\|
e^{\nu(t-s)\Delta}
\mathbb P\nabla\cdot F
\|_6
\le
C
(\nu(t-s))^{-3/4}
\|F\|_3.
$$

而：

$$
\|u\otimes v\|_3
\le
\|u\|_6
\|v\|_6.
$$

若：

$$
M_u
=
\|u\|_{\mathcal K_6(T)},
$$

$$
M_v
=
\|v\|_{\mathcal K_6(T)},
$$

則：

$$
\|u(s)\|_6
\le
M_us^{-1/4},
$$

$$
\|v(s)\|_6
\le
M_vs^{-1/4}.
$$

因此：

$$
\|B(u,v)(t)\|_6
\le
C\nu^{-3/4}
M_uM_v
\int_0^t
(t-s)^{-3/4}
s^{-1/2}
\,ds.
$$

Beta scaling：

$$
\int_0^t
(t-s)^{-3/4}
s^{-1/2}
ds
=
C_\beta
t^{-1/4}.
$$

故：

$$
\boxed{
\|B(u,v)\|_{\mathcal K_6(T)}
\le
C_\ast
\nu^{-3/4}
\|u\|_{\mathcal K_6(T)}
\|v\|_{\mathcal K_6(T)}.
}
\tag{12.3}
$$

這是一個完全連續的 scale-critical quadratic fixed-point estimate。

---

# 13. Local large-data formation 與 global small-data closure

對：

$$
u_0\in L^3,
$$

heat flow 的短時間 Kato norm 可藉由 approximation + heat smoothing 使：

$$
\boxed{
\|e^{\nu t\Delta}u_0\|_{\mathcal K_6(T)}
\to0
\qquad
(T\downarrow0).
}
\tag{13.1}
$$

因此 arbitrary $L^3$ data 可以形成 local mild solution。

也就是：

$$
\boxed{
\mathsf I_{\rm local}^{L^3}
\;\operatorname{form}.
}
\tag{13.2}
$$

但若要直接在：

$$
T=\infty
$$

做單次 contraction，(12.2)–(12.3) 要求 linear critical size sufficiently small。

因此 small $L^3$ data：

$$
\|u_0\|_3
\ll
\nu
$$

可使 global contraction closure 成立。

對 arbitrary large data，這組 scale-critical bilinear estimate 不提供單次 global contraction。

所以：

$$
\boxed{
\textbf{STOP-C05:
Global Critical Fixed-Point Gap}.
}
\tag{13.3}
$$

---

# 14. 為什麼縮短時間可以 local，但不能直接 global

這裡要區分兩件事。

critical spatial norm：

$$
\|u_0\|_3
$$

對 NS scaling 不變。

但 local Kato profile：

$$
\sup_{0<t<T}
t^{1/4}
\|e^{\nu t\Delta}u_0\|_6
$$

對固定 $u_0\in L^3$ 可隨：

$$
T\downarrow0
$$

而趨近零。

這就是 arbitrary large critical data 仍有 local well-posedness 的原因。

然而若 maximal existence time：

$$
T_\ast<\infty,
$$

要一路 restart 到 $T_\ast$，就需要控制每個 restart state：

$$
u(t_0)
$$

的 critical profile。

如果 critical concentration 持續加劇，local lifespan 可以連續縮短。

目前沒有由 energy identity 單獨推出：

$$
\inf_{t_0<T_\ast}
T_{\rm local}(u(t_0))
>
0.
$$

因此 local formation 不等於 global closure。

---

# 15. 三條 critical route 的共同結構

目前測試：

## Route A

$$
\dot H^{1/2}
$$

得到：

$$
\frac12Y'
+
\left(
\nu-C\sqrt{Y}
\right)Z
\le0.
$$

障礙：

$$
\boxed{
\text{large critical amplitude destroys direct absorption}.
}
$$

## Route B

$$
L_t^\infty L_x^3
$$

是足夠 regularity interface，但 energy 只給：

$$
L_t^4L_x^3.
$$

障礙：

$$
\boxed{
\text{critical endpoint-in-time bound lacks an a priori bridge}.
}
$$

## Route C

critical Duhamel / Kato contraction。

障礙：

$$
\boxed{
\text{quadratic fixed point is globally contractive only in a small critical regime}.
}
$$

三者合流：

$$
\boxed{
\textbf{
Critical-Carrier Formation
\neq
Critical-Carrier Global Control.
}
}
\tag{15.1}
$$

---

# 16. Critical Amplitude Barrier Principle

本輪可抽出一個方法論級 no-go。

假設一個 pure-continuous critical energy architecture 具有：

$$
\boxed{
\frac d{dt}
\mathcal A(u)^2
+
\left(
\nu
-
C\mathcal A(u)
\right)
\mathcal D(u)^2
\le0,
}
\tag{16.1}
$$

其中：

$$
\mathcal A(u_\lambda)
=
\mathcal A(u).
$$

則：

1. 若：

$$
C\mathcal A(u_0)<\nu,
$$

可由 absorption 建立 small-data coercivity；

2. 若：

$$
C\mathcal A(u_0)\ge\nu,
$$

該 inequality 本身不提供正的 dissipation coefficient；

3. 由 critical scaling invariance：

$$
\mathcal A(u_\lambda)
=
\mathcal A(u),
$$

不能透過 NS rescaling 把 large-amplitude branch 送回 small regime。

因此：

$$
\boxed{
\textbf{
a single scale-invariant amplitude carrier with only
smallness-based viscous absorption cannot by itself close arbitrary-data global regularity.
}
}
\tag{16.2}
$$

這是對此 architecture 的 no-go，不是對所有 continuous proofs 的 no-go。

---

# 17. 24 範式的新訊號：可能不是 $B$ 軸先轉，而是 $O$ 軸先轉

Round 01 到 Round 02 都還沒有必要令：

$$
B=\mathsf D.
$$

所以：

$$
\boxed{
T_{\mathsf C\to\mathsf D}
=
\text{NOT YET REACHED}.
}
$$

但目前三條 critical route 都把複雜 state 壓成單一 critical amplitude：

$$
\|u\|_{\dot H^{1/2}},
$$

$$
\|u\|_3,
$$

或：

$$
\|u\|_{\mathcal K_6}.
$$

這些 carrier 可以：

- 偵測 criticality；
- 形成 local theory；
- 在 smallness 下 closure；
- 在 bounded endpoint 條件下作 regularity recognition；

但不能單獨產生 arbitrary-data global coercivity。

因此出現一個候選觀察模式轉換：

$$
\boxed{
\mathsf O_{\mathsf C}
\longrightarrow
\mathsf O_{\mathsf X}.
}
\tag{17.1}
$$

這裡的 $\mathsf X$ 不是「不可測」。

它表示下一輪應檢驗：

> 是否不存在一個單一 scalar critical carrier，同時保留 nonlinear geometry、alignment、sign、transport、pressure coupling 與 dissipation 所需的 closure information？

目前尚未證明：

$$
\boxed{
O=\mathsf X
}
$$

是 NS 的必要 observation mode。

所以 (17.1) 只標：

$$
\boxed{
\text{CANDIDATE TRANSITION}.
}
$$

它是下一輪需要測試的命題。

---

# 18. 72 第四軸：本輪仍完全停留在 $\mathsf F$

本輪沒有引入：

$$
\mathsf K
$$

古典機率核，

也沒有引入：

$$
\mathsf Q
$$

量子通道。

所有 route 都是 deterministic：

$$
\boxed{
L=\mathsf F.
}
$$

因此目前障礙不是：

$$
\mathsf F
\to
\mathsf K
$$

或：

$$
\mathsf F
\to
\mathsf Q.
$$

目前更精確的 72 診斷是：

$$
\boxed{
\langle
\mathsf C;
\mathsf S;
\mathsf C;
\mathsf F
\rangle
}
$$

已經可以形成 critical local theory 和 conditional regularity theory，但無條件 global coercivity 沒有閉合。

---

# 19. Round 02 24/72 Ledger

| Step | Carrier / X 積分 | $B$ | $U$ | $O$ | $L$ | 狀態 |
|---|---|---|---|---|---|---|
| C08 | $\int_{\rm scaling}$ | $\mathsf C$ | $\mathsf S$ | $\mathsf C$ | $\mathsf F$ | FORM |
| C09 | $\int_{\dot H^{1/2}}$ | $\mathsf C$ | $\mathsf S$ | $\mathsf C$ | $\mathsf F$ | FORM |
| C10 | $\int_{\rm critical\ energy}$ | $\mathsf C$ | $\mathsf S$ | $\mathsf C$ | $\mathsf F$ | FORM |
| C11 | $\int_{\rm arbitrary\ amplitude\ coercivity}$ | $\mathsf C$ | $\mathsf S$ | $\mathsf C$ | $\mathsf F$ | NOT CERTIFIED |
| C12 | $\int_{L^3}$ | $\mathsf C$ | $\mathsf S$ | $\mathsf C$ | $\mathsf F$ | FORM |
| C13 | bounded $L^\infty_tL^3_x\to$ regularity | $\mathsf C$ | $\mathsf R$ meta-step | $\mathsf C$ | $\mathsf F$ | FORM / known criterion |
| C14 | energy $\to L^\infty_tL^3_x$ | $\mathsf C$ | $\mathsf S$ | $\mathsf C$ | $\mathsf F$ | NOT CERTIFIED |
| C15 | $\int_{\rm Duhamel/Kato}$ | $\mathsf C$ | $\mathsf S$ | $\mathsf C$ | $\mathsf F$ | FORM |
| C16 | local arbitrary $L^3$ fixed point | $\mathsf C$ | $\mathsf S$ | $\mathsf C$ | $\mathsf F$ | FORM |
| C17 | global arbitrary $L^3$ contraction | $\mathsf C$ | $\mathsf S$ | $\mathsf C$ | $\mathsf F$ | NOT CERTIFIED |
| C18 | $\mathsf C\to\mathsf X$ observation transition | $\mathsf C$ | — | $\mathsf X$ candidate | $\mathsf F$ | OPEN |

其中 C13 的：

$$
\mathsf R
$$

只表示「proof meta-layer 使用既知 regularity criterion 作 recognition」。

它不表示 NS 物理演化本身從：

$$
\mathsf S
$$

變成：

$$
\mathsf R.
$$

---

# 20. X 失敗診斷物件

## STOP-C03

$$
\boxed{
\bot_X^{\mathrm{C03}}
=
\left\langle
\begin{array}{l}
\text{layer}=\dot H^{1/2}\text{ critical coercivity},\\
\text{reason}=\text{critical amplitude enters dissipation coefficient},\\
\text{available}=
\nu-C\|u\|_{\dot H^{1/2}},\\
\text{closure}=\text{smallness only},\\
\text{scale repair}=\text{impossible by NS symmetry},\\
\text{discrete intrusion}=\mathrm{false}
\end{array}
\right\rangle.
}
$$

## STOP-C04

$$
\boxed{
\bot_X^{\mathrm{C04}}
=
\left\langle
\begin{array}{l}
\text{layer}=L^\infty_tL^3_x,\\
\text{reason}=\text{endpoint-in-time control missing},\\
\text{available}=L^4_tL^3_x,\\
\text{needed}=L^\infty_tL^3_x,\\
\text{discrete intrusion}=\mathrm{false}
\end{array}
\right\rangle.
}
$$

## STOP-C05

$$
\boxed{
\bot_X^{\mathrm{C05}}
=
\left\langle
\begin{array}{l}
\text{layer}=\text{critical Kato fixed point},\\
\text{reason}=\text{quadratic global contraction requires small critical profile},\\
\text{local formation}=\mathrm{true},\\
\text{global arbitrary amplitude}=\mathrm{not\ certified},\\
\text{discrete intrusion}=\mathrm{false}
\end{array}
\right\rangle.
}
$$

---

# 21. 本輪真正的新結論

Round 01 顯示：

$$
\boxed{
\text{energy carrier is too subcritical}.
}
$$

Round 02 顯示：

$$
\boxed{
\text{moving directly to a critical scalar carrier fixes the scaling mismatch,
but exposes an amplitude/geometry closure gap}.
}
$$

所以 obstruction 由：

$$
\boxed{
\text{ScaleMismatch}
}
$$

推進成：

$$
\boxed{
\text{CriticalAmplitude/StructureMismatch}.
}
$$

這是嚴格的 frontier reduction。

---

# 22. Pure-C route 的目前狀態

目前純連續路徑：

$$
\boxed{
\begin{aligned}
\mathsf C
&\xrightarrow{\rm energy}
\mathsf C
\\
&\xrightarrow{\rm critical\ carrier}
\mathsf C
\\
&\xrightarrow{\rm local\ theory}
\mathsf C
\\
&\xrightarrow{\rm global\ control}
\operatorname{STOP}.
\end{aligned}
}
$$

而不是：

$$
\mathsf C
\to
\mathsf D.
$$

所以第二輪仍然沒有找到 essential discrete intrusion。

但是第一次出現一個新的候選：

$$
\boxed{
\text{底空間仍為 }\mathsf C,
\quad
\text{觀察模式可能需要 }\mathsf X.
}
$$

換言之：

$$
\boxed{
\text{下一個 transition 可能先發生在 observation axis，
而不是 substrate axis。}
}
$$

---

# 23. 下一輪：Pure Continuous Relational / Geometric Route

下一輪仍禁止本質離散化。

目標：

$$
\boxed{
\text{不用單一 critical amplitude；
改保留 nonlinear geometry itself。}
}
$$

候選 continuous relational carriers：

$$
S
=
\nabla_{\rm sym}u,
$$

$$
\omega
=
\nabla\times u,
$$

$$
\lambda_2(S),
$$

$$
\omega^\top S\omega,
$$

$$
\text{vorticity direction field},
$$

$$
\text{strain-vorticity alignment},
$$

$$
\text{helicity / local flux / pressure-strain coupling}.
$$

下一輪要測：

1. 是否能建立一個完全連續的 multi-carrier X state：

$$
X_{\rm geom}
=
\int_{\rm relation}
(u,S,\omega,p,\text{alignment},\text{flux});
$$

2. 是否真的需要：

$$
O=\mathsf X
$$

而不是單一 scalar observation；

3. 是否 geometric depletion 可以讓 nonlinear term 取得 sign 或 subcritical gain；

4. 若失敗，失敗是：

$$
\text{geometry not coercive},
$$

還是：

$$
\text{geometry requires discrete scale extraction}.
$$

只有後者才宣告真正的：

$$
T_{\mathsf C\to\mathsf D}.
$$

---

# 24. External source anchors

1. H. Fujita and T. Kato, *On the Navier-Stokes initial value problem. I*, Archive for Rational Mechanics and Analysis 16 (1964), 269–315. DOI: `10.1007/BF00276188`.

2. L. Escauriaza, G. A. Seregin, V. Šverák, *$L_{3,\infty}$-solutions of the Navier-Stokes equations and backward uniqueness*, Russian Mathematical Surveys 58(2) (2003), 211–250. DOI: `10.1070/RM2003v058n02ABEH000609`.

3. I. Gallagher, G. S. Koch, F. Planchon, *A profile decomposition approach to the $L^\infty_t(L^3_x)$ Navier-Stokes regularity criterion*, Math. Ann. 355 (2013), 1527–1559. arXiv: `1012.0145`.

4. J.-Y. Chemin and P. Zhang, *On the critical one component regularity for 3-D Navier-Stokes system*, arXiv: `1310.6442`.

---

# 25. Commit state

$$
\boxed{
\begin{aligned}
\text{Route} &: \mathrm{Pure\ Continuous\ Critical},\\
\text{First\ essential\ D\ intrusion} &: \mathrm{Not\ reached},\\
\text{STOP-C03} &: \mathrm{Critical\ amplitude\ absorption\ gap},\\
\text{STOP-C04} &: \mathrm{Endpoint\ }L^\infty_tL^3_x\mathrm{\ control\ gap},\\
\text{STOP-C05} &: \mathrm{Global\ critical\ fixed\ point\ gap},\\
\text{Scaling repair} &: \mathrm{No,\ critical\ carrier\ is\ invariant},\\
\text{Candidate transition} &: \mathsf O_{\mathsf C}\to\mathsf O_{\mathsf X},\\
\text{Next} &: \mathrm{Pure\ Continuous\ Relational/Geometric\ Route}.
\end{aligned}
}
$$
