---
title: "Navier–Stokes C3-O：Adjoint Core Balance、Cancellation Corridor 與 Balance–Dynamics Separation"
subtitle: "Gauge-Clean Local Strain Balance, Asymptotic Boundary/Self-Amplification Regimes, and Why Energy-Balance Closeness Is Not Dynamical Closeness"
version: "v0.2"
date: "2026-08-14"
author: "Neo.K / EveMissLab"
language: "zh-TW"
status: "Theorem-style structural reduction / audited no-go note"
epistemic_status: "Exact adjoint-localized strain balance + pointwise current identities + asymptotic ratio classification + balance-versus-operator non-identifiability. Does NOT prove Navier–Stokes regularity or singularity."
---

# Navier–Stokes C3-O
# Adjoint Core Balance、Cancellation Corridor 與 Balance–Dynamics Separation

## v0.2 audit delta

本版相對 v0.1 的核心修正不是文句潤飾，而是 theorem-safety 強化：

- 消除 velocity-gradient $G=\nabla u$ 與 integrated amplification $A_I$ 的符號碰撞；
- 把 C3-N 所依賴的 Betchov current 與 pressure current 寫成 pointwise divergence lemmas，使 C3-O 的主 balance 可在本文內直接核對；
- 對 adjoint cutoff 補上 regularity、maximum-principle 與 stochastic/transition-kernel interpretation，並明確指出 earlier-time cutoff 是具有 tails 的 soft ancestry tube，而不是 compactly supported hard tube；
- 將 cancellation-precision debt 改成 exact residual trichotomy，避免「沒有同比例趨零」這類不足以推出 divergence 的語句；
- 將 $\rho\to0$ 的結論改成 **non-identifiability/no-go**：scalar balance information 單獨不足以控制 omitted operator，而不是把未構造 explicit counterexample 的敘述標成 unconditional false theorem；
- 將 $\mathfrak P_I$ 明確標記為 whole-space/window diagnostic，另提出 cutoff-weighted multiplicative candidate；
- 修正 cancellation component debt 的漸近記號：需要的是 lower bound $\Omega(A_I)$，不是 upper-bound 記號 $O(A_I)$；
- 對 Miller 的 conditional blow-up theorem 改成 current paper numbering 與實際 perturbative ratio 的精確描述，並明確區分它與本文提出的 $\dot H^{-1}$ diagnostic。

---

## 0. 本輪定位

C3-N 已建立 exact localized strain balance：

$$
\frac12\frac d{dt}\int\chi|S|^2
+
\nu\int\chi|\nabla S|^2
=
-2\int\chi\det S
+
\mathcal C_\chi,
$$

其中：

$$
\begin{aligned}
\mathcal C_\chi
={}&
\frac12\int
|S|^2
(
\partial_t\chi
+
u\cdot\nabla\chi
+
\nu\Delta\chi
)
\\
&+
\frac13\int\nabla\chi\cdot F_B
+
\int\nabla\chi\cdot F_p.
\end{aligned}
$$

並且：

$$
F_B
=
\left(
G^2
-\frac12\operatorname{tr}(G^2)I
\right)u,
\qquad
G=\nabla u,
$$

以及：

$$
F_p
=
(\nabla^2p-\Delta p\,I)u.
$$

本輪的第一個問題：

> 能否把 cutoff 自己造成的 gauge/advection/diffusion terms完全剝除？

答案：

$$
\boxed{\textbf{YES}.}
$$

使用 strain transport-diffusion operator的 backward adjoint cutoff即可。

第二個問題：

> 若只剩 bulk strain self-amplification與真正的 boundary current，三種 asymptotic ratio regime能排除哪一些？

答案：

- boundary過度負向：
  $$
  \boxed{\rho\le-1}
  $$
  不能支援 positive local strain-energy growth；
- $\rho\to-1^+$：
  不被排除，但必須支付 increasingly precise gross cancellation；
- $\rho\to0$：
  也不能排除，而且**不能**解讀成 full dynamics接近 strain self-amplification model；
- $\rho\to+\infty$：
  boundary/pressure current成為主要 growth carrier。

最重要的結論：

$$
\boxed{
\text{balance closeness}
\neq
\text{dynamical/operator closeness}.
}
$$

---

# 1. Full strain equation

對 smooth incompressible Navier–Stokes：

$$
\partial_tu
-\nu\Delta u
+
(u\cdot\nabla)u
+
\nabla p
=
0,
$$

$$
\nabla\cdot u=0,
$$

strain：

$$
S
=
\frac12
(\nabla u+\nabla u^\top)
$$

滿足：

$$
\boxed{
\partial_tS
-
\nu\Delta S
+
(u\cdot\nabla)S
+
S^2
+
\frac14\omega\otimes\omega
-
\frac14|\omega|^2I
+
\nabla^2p
=
0.
}
$$

---

# 1A. Scope, convention, and regularity assumptions

除非另行聲明，本文工作於 $\mathbb R^3$，令

$$
G_{ij}=\partial_j u_i,
\qquad
S=\frac12(G+G^\top),
\qquad
\omega=\nabla\times u.
$$

為了讓所有 integration by parts、homogeneous Sobolev norm 與 terminal-value adjoint construction 都不帶技術性歧義，可先在 smooth rapidly decaying solution class 中理解各 identity；其後若要推到 standard strong/mild solution class，需逐項以 density/approximation 延拓。

對 terminal cutoff，本文取

$$
\chi_1\in C_c^\infty(\mathbb R^3),
\qquad
0\le\chi_1\le1.
$$

這個 compact support 只在 terminal time 成立；只要 $\nu>0$，earlier-time adjoint cutoff 一般會立即產生 noncompact tails。

---

# 1B. Pointwise current identities behind C3-N

## Lemma 1B.1 — Betchov current identity

定義

$$
F_B
=
\left(
G^2-\frac12\operatorname{tr}(G^2)I
\right)u.
$$

由 $\nabla\cdot u=0$、mixed derivatives commute，可得

$$
\partial_i
\left(
(G^2)_{ij}
-\frac12\operatorname{tr}(G^2)\delta_{ij}
\right)
=0.
$$

因此

$$
\nabla\cdot F_B
=
\operatorname{tr}(G^3).
$$

令 $W=(G-G^\top)/2$。在三維 incompressible case，

$$
\operatorname{tr}(G^3)
=
3\det S
+
\frac34\,\omega\cdot S\omega.
$$

故有 pointwise identity

$$
\boxed{
\frac14\,\omega\cdot S\omega
=
\frac13\nabla\cdot F_B
-
\det S.
}
$$

這是本文 localized Betchov conversion 的精確來源；其全空間平均版本與 classical Betchov relation 相容 [3,5]。

## Lemma 1B.2 — Pressure current identity

定義

$$
F_p
=
(\nabla^2p-\Delta p\,I)u.
$$

因

$$
\partial_i
(\partial_i\partial_jp-\Delta p\,\delta_{ij})
=0,
$$

且 $\operatorname{tr}G=0$，所以

$$
\boxed{
\nabla\cdot F_p
=
S:\nabla^2p.
}
$$

此外 pressure Poisson equation 為

$$
\boxed{
-\Delta p
=
\operatorname{tr}(G^2)
=
|S|^2-\frac12|\omega|^2.
}
$$

因此 pressure current 雖以 divergence 形式進入 local balance，其 source 仍經由 elliptic inversion 對全域速度梯度場敏感。

## Corollary 1B.3 — Direct localized strain balance

將 full strain equation 與 $\chi S$ contraction。利用 $\operatorname{tr}S=0$、

$$
S:S^2=\operatorname{tr}(S^3)=3\det S,
$$

再使用 Lemma 1B.1 與 Lemma 1B.2，得到

$$
\boxed{
\frac12\frac d{dt}\int\chi|S|^2
+
\nu\int\chi|\nabla S|^2
=
-2\int\chi\det S
+
\frac12\int|S|^2
(\partial_t\chi+u\cdot\nabla\chi+\nu\Delta\chi)
+
\frac13\int\nabla\chi\cdot F_B
+
\int\nabla\chi\cdot F_p.
}
$$

所以 C3-O 的 starting identity 不必只作為 C3-N 的黑箱輸入；其 pointwise current mechanism 可在本文內直接核對。

---

# 2. Adjoint cutoff

固定 ancestry window：

$$
I=[t_0,t_1].
$$

取 terminal cutoff：

$$
\chi_1(x)
$$

滿足：

$$
0\le\chi_1\le1,
$$

並 localized near child ancestry core。

令：

$$
\boxed{
\partial_t\chi
+
u\cdot\nabla\chi
+
\nu\Delta\chi
=
0
}
$$

在：

$$
t_0<t<t_1,
$$

以及 terminal condition：

$$
\boxed{
\chi(t_1,x)=\chi_1(x).
}
$$

在上述 smooth setting，terminal-value problem 經 time reversal 成為 forward uniformly parabolic problem，因此有唯一 smooth solution。Maximum principle 給出

$$
\boxed{
0\le\chi(t,x)\le1.
}
$$

更具體地，若 $X_s^{t,x}$ 解

$$
dX_s
=
u(s,X_s)\,ds
+
\sqrt{2\nu}\,dW_s,
\qquad
X_t=x,
$$

則 backward Kolmogorov representation 為

$$
\boxed{
\chi(t,x)
=
\mathbb E
\left[
\chi_1(X_{t_1}^{t,x})
\right].
}
$$

因此 $\chi$ 可以被理解成「從 $(t,x)$ 出發，在 terminal time 落入 child core 的 diffusive ancestry weight」。

令：

$$
\tau=t_1-t.
$$

則其變成 forward parabolic equation：

$$
\partial_\tau\chi
=
u(t_1-\tau)\cdot\nabla\chi
+
\nu\Delta\chi.
$$

所以在 smooth pre-singular window中，這是標準 parabolic adjoint construction。

---

# 3. Adjoint ancestry tube

此 cutoff不是固定 ball。

它會：

- backward follow velocity drift；
- backward diffuse over parabolic distance；
- 自動吸收 moving-core gauge和 advection cutoff terms。

本文稱：

$$
\boxed{
\textbf{Adjoint Ancestry Tube}.
}
$$

但這裡的 ``tube'' 是 **soft weighted tube**。若 $\nu>0$ 且 $\chi_1$ 非零，通常對任何 $t<t_1$ 都不能期待 $\chi(t,\cdot)$ 保持 compact support。因而本文後續的 ``boundary current'' 更精確應理解成

$$
\boxed{
\text{adjoint cutoff-interface current},
}
$$

不是一個固定幾何邊界上的 classical flux。

---

# 4. C3-O.1：Adjoint Core Balance Theorem

## 定理 4.1

若：

$$
\chi
$$

解 adjoint cutoff equation：

$$
\partial_t\chi
+
u\cdot\nabla\chi
+
\nu\Delta\chi
=
0,
$$

則：

$$
\boxed{
\frac12
\frac d{dt}
\int
\chi|S|^2
+
\nu
\int
\chi|\nabla S|^2
=
-2
\int
\chi\det S
+
\int
\nabla\chi\cdot J_{\rm corr},
}
$$

其中：

$$
\boxed{
J_{\rm corr}
=
\frac13F_B+F_p.
}
$$

### 證明

直接代入 C3-N 的 localized strain balance。

因：

$$
\partial_t\chi
+
u\cdot\nabla\chi
+
\nu\Delta\chi
=
0,
$$

第一整組 scalar cutoff terms exactly vanish。$\square$

---

# 5. Gauge-clean variables

定義：

$$
E_\chi(t)
=
\frac12
\int
\chi|S|^2dx,
$$

$$
D_\chi(t)
=
\nu
\int
\chi|\nabla S|^2dx,
$$

$$
A_\chi(t)
=
-2
\int
\chi\det S\,dx,
$$

以及：

$$
B_\chi(t)
=
\int
\nabla\chi\cdot J_{\rm corr}\,dx.
$$

則：

$$
\boxed{
E_\chi'
+
D_\chi
=
A_\chi+B_\chi.
}
$$

---

# 6. Window-integrated balance

對：

$$
I=[t_0,t_1],
$$

定義：

$$
\Delta E_I
=
E_\chi(t_1)-E_\chi(t_0),
$$

$$
D_I
=
\int_I
D_\chi(t)\,dt,
$$

$$
A_I
=
\int_I
A_\chi(t)\,dt,
$$

$$
B_I
=
\int_I
B_\chi(t)\,dt.
$$

則：

$$
\boxed{
\Delta E_I+D_I
=
A_I+B_I.
}
$$

且：

$$
D_I\ge0.
$$

---

# 7. Growth window

稱：

$$
I
$$

為 positive local strain-growth window，若：

$$
\Delta E_I>0.
$$

則：

$$
A_I+B_I
=
\Delta E_I+D_I
>
0.
$$

---

# 8. C3-O.2：Growth-Carrier Dichotomy

## 定理 8.1

對任何 positive local strain-growth window，必有以下之一：

### Branch A — Positive SSA-supported

$$
A_I>0
$$

而：

$$
B_I>-A_I.
$$

### Branch B — Boundary-current-driven

$$
A_I\le0
$$

且必然：

$$
\boxed{
B_I>
|A_I|+D_I.
}
$$

更精確：

$$
B_I
=
\Delta E_I+D_I-A_I.
$$

$\square$

---

# 9. Boundary ratio

在：

$$
A_I>0
$$

的 window定義：

$$
\boxed{
\rho_I
=
\frac{B_I}{A_I}.
}
$$

由 growth：

$$
A_I+B_I>0,
$$

得到：

$$
\boxed{
\rho_I>-1.
}
$$

---

# 10. C3-O.3：Hard Depletion Barrier

## 定理 10.1

若：

$$
A_I>0
$$

且：

$$
\rho_I\le-1,
$$

則：

$$
\boxed{
\Delta E_I\le-D_I\le0.
}
$$

所以此 window不可能是 positive strain-growth window。$\square$

---

# 11. Cancellation corridor

對：

$$
A_I>0,
$$

定義：

$$
\boxed{
\kappa_I
=
1+\rho_I
=
\frac{\Delta E_I+D_I}{A_I}.
}
$$

growth window有：

$$
\kappa_I>0.
$$

---

# 12. C3-O.4：Cancellation-Precision Debt

令一列 positive growth windows $I_n$ 滿足

$$
A_n>0,
\qquad
\rho_n\to-1^+.
$$

定義 exact residual

$$
R_n
:=
\Delta E_n+D_n
=
A_n+B_n
>0,
$$

以及

$$
\kappa_n
:=
1+\rho_n
=
\frac{R_n}{A_n}.
$$

則

$$
\boxed{
A_n=\frac{R_n}{\kappa_n},
\qquad
B_n=-A_n+R_n.
}
$$

因此有三個精確 consequences：

1. 若存在 $c>0$ 使 $R_n\ge c$，則
   $$
   A_n\to\infty,
   \qquad
   |B_n|\sim A_n.
   $$
2. 更一般地，
   $$
   A_n\to\infty
   \iff
   \frac{R_n}{\kappa_n}\to\infty.
   $$
3. 若 $A_n$ 保持 bounded，則必須支付
   $$
   \boxed{
   R_n=O(\kappa_n).
   }
   $$

所以 cancellation corridor 本身不強迫 gross amplification diverge；它強迫的是：**若 residual growth 不跟 $\kappa_n$ 一起縮小，gross terms 就必須放大。**

在 non-vanishing residual regime，確實得到

$$
\boxed{
\text{large SSA}
+
\text{large opposite interface current}
+
\text{small relative residual}.
}
$$

---

# 13. Fixed fractional growth版本

若 $E_\chi(t_0)>0$ 且

$$
\Delta E_I
\ge
\gamma E_\chi(t_0)
$$

for fixed：

$$
\gamma>0,
$$

則：

$$
\boxed{
A_I
\ge
\frac{
\gamma E_\chi(t_0)
}{
\kappa_I
}.
}
$$

所以：

$$
\kappa_I\to0
$$

時，

$$
\boxed{
\frac{A_I}{E_\chi(t_0)}
\ge
\frac{\gamma}{\kappa_I}.
}
$$

因此 gross self-amplification 相對 local stock 的 lower bound 發散。

---

# 14. Ratio subsequence classification

考慮 infinitely many positive growth windows：

$$
I_n
$$

且：

$$
A_{I_n}>0.
$$

因：

$$
\rho_n>-1,
$$

可抽 subsequence落入：

## O-A — Cancellation corridor

$$
\rho_n\to-1^+.
$$

## O-B — Finite balance regime

存在：

$$
-1+\delta
\le
\rho_n
\le
M
$$

for some：

$$
\delta>0,
\quad
M<\infty.
$$

## O-C — Boundary-driven regime

$$
\rho_n\to+\infty.
$$

若有 infinitely many：

$$
A_{I_n}\le0
$$

growth windows，

它們自動屬於 boundary-current-driven branch。

---

# 15. Miller operator decomposition

令 $L^2_{st}$ 表示由 divergence-free velocity fields 的 symmetric gradients 所形成的 closed strain subspace，$P_{st}$ 表示 $L^2$ 到 $L^2_{st}$ 的 orthogonal projection。

恢復一般 viscosity $\nu>0$ 後，Miller [1] 的 decomposition 可寫成：

$$
\boxed{
\partial_tS
-
\nu\Delta S
+
\frac23P_{st}(S^2)
+
\mathcal P_{NS}
=
0,
}
$$

其中：

$$
\boxed{
\mathcal P_{NS}
=
P_{st}
\left(
(u\cdot\nabla)S
+
\frac13S^2
+
\frac14\omega\otimes\omega
\right).
}
$$

strain self-amplification model則是：

$$
\boxed{
\partial_tS
-
\nu\Delta S
+
\frac23P_{st}(S^2)
=
0.
}
$$

---

# 16. Orthogonality

對 smooth rapidly decaying full-space strain $S\in L^2_{st}$，有

$$
\boxed{
\langle
\mathcal P_{NS},
S
\rangle
=
0.
}
$$

這件事在本文的 current language 中可以直接驗證。因 $P_{st}$ 是 orthogonal projection 且 $S\in L^2_{st}$，

$$
\langle P_{st}Q,S\rangle
=
\langle Q,S\rangle.
$$

首先 incompressibility 給出

$$
\left\langle
(u\cdot\nabla)S,S
\right\rangle
=0.
$$

其次

$$
\left\langle
\frac13S^2,S
\right\rangle
=
\int\det S.
$$

而 Lemma 1B.1 在全空間積分後給出 global Betchov cancellation

$$
0
=
\int\nabla\cdot F_B
=
3\int\det S
+
\frac34\int\omega\cdot S\omega,
$$

即

$$
\frac14\int\omega\cdot S\omega
=
-\int\det S.
$$

所以

$$
\left\langle
P_{st}
\left(
(u\cdot\nabla)S
+\frac13S^2
+\frac14\omega\otimes\omega
\right),
S
\right\rangle
=0.
$$

因此 full Navier--Stokes 與 SSA model 具有同一 global strain-enstrophy growth identity：

$$
\boxed{
\frac d{dt}
\|S\|_2^2
=
-2\nu\|S\|_{\dot H^1}^2
-
4\int\det S.
}
$$

在本稿的 smooth/decay assumptions 下，這個 orthogonality 因而不是額外假設。

---

# 17. C3-O.5：Balance–Dynamics Separation No-Go

## 命題 17.1 — Orthogonality is not operator control

$$
\langle\mathcal P_{NS},S\rangle=0
$$

只給出一個 scalar pairing constraint；它不推出

$$
\mathcal P_{NS}=0,
$$

也不推出任何 standalone norm smallness，例如

$$
\|\mathcal P_{NS}\|_X\ll1.
$$

因此更精確的結論是

$$
\boxed{
\text{energy orthogonality imposes no operator-size bound by itself}.
}
$$

特別地，whole-space constant choice $\chi\equiv1$ 是 adjoint equation 的 nonlocalized global solution（不是前述 compact terminal cutoff class），並給出

$$
B_{\chi\equiv1}=0
$$

identically；但 full Navier--Stokes strain equation 仍含 $\mathcal P_{NS}$。因此在任何 $A_I>0$ 的 whole-space window，ratio 都是

$$
\rho_I=0,
$$

卻不含任何足以恢復 $\mathcal P_{NS}$ 的資訊。

所以本文得到的是 information-theoretic / structural no-go：

$$
\boxed{
\rho\to0
\quad\text{alone cannot imply}\quad
\mathcal P_{NS}\to0.
}
$$

這不是聲稱已經用某一個 explicit singular/full-NS counterexample 反證所有可能附加假設下的 approximation theorem；它只排除 **由 $\rho$ 單獨決定 operator closeness** 的路線。 $\square$

---

# 18. 為何這個 no-go重要？

Miller [1] 的 SSA model：

- 位於同一 strain constraint space；
- 具有同一 enstrophy-growth identity；
- 具有相近的 middle-eigenvalue regularity structure；
- 對一類 initial data可 finite-time blow up。

所以：

$$
\boxed{
\text{strain-energy balance本身不足以區分
full N--S 與可 blow-up 的 SSA model}.
}
$$

---

# 19. Conditional full-N–S warning

Miller [1] 的 SSA-model 論文確實證明一個 conditional full Navier--Stokes blow-up theorem，但 v0.2 必須把它與本文 diagnostic 分開。

在該文採用的 $\nu=1$ normalization 中，令

$$
\mathcal P_{NS}
=
P_{st}
\left(
(u\cdot\nabla)S
+\frac13S^2
+\frac14\omega\otimes\omega
\right).
$$

該 theorem 的 perturbative hypothesis 不是本文的 $\mathfrak P_I$；它要求一個 pointwise-in-time $L^2$ ratio 保持受控，分母同時含 $-\Delta S$ 與 nonlinear terms。以該文記號，其核心 ratio 形如

$$
\frac{
\|\mathcal P_{NS}(t)\|_{L^2}
}{
\left\|
-\Delta S
+
P_{st}
\left(
\frac12(u\cdot\nabla)S
+\frac56S^2
+\frac18\omega\otimes\omega
\right)
\right\|_{L^2}
}
\le2,
$$

再配合該文指定的 initial-data sign condition，推出 finite-time blow-up。

所以 C3-O 應保存的不是「small perturbation automatically means danger」這種粗略句子，而是：

$$
\boxed{
\text{operator smallness is direction-dependent and theorem-dependent}.
}
$$

某種 specific relative closeness to the SSA dynamics 可以出現在 conditional blow-up theorem 中；另一方面，其他 interaction/depletion structure 又可能支援 regularity。故不能把 ``small omitted term'' 或 ``large omitted term'' 本身當成單調 regularity parameter。

---

# 20. Operator-level defect

因此真正需要和 $\rho_I$ 平行追蹤的是 $\mathcal P_{NS}$ 本身。

先定義 whole-space/window diagnostic：

$$
\boxed{
\mathfrak P_I^{\rm glob}
=
\frac{
\int_I
\|\mathcal P_{NS}(t)\|_{\dot H^{-1}}^2dt
}{
\nu^2
\int_I
\|S(t)\|_{\dot H^1}^2dt
}.
}
$$

這裡 denominator 非零，且 numerator/denominator 皆有限。

選 $\dot H^{-1}$ 的原因是

$$
\|\nu\Delta S\|_{\dot H^{-1}}
=
\nu\|S\|_{\dot H^1},
$$

所以 $\mathfrak P_I^{\rm glob}$ 可理解成 omitted operator 相對 viscous operator 的 time-integrated squared ratio。

但它 **不是 spatially localized diagnostic**。因此 v0.1 把 $(\rho_I,\mathfrak P_I)$ 直接稱為 ``true local state'' 太強。

一個 cutoff-weighted multiplicative candidate 是

$$
\boxed{
\mathfrak P_{I,\chi}^{\rm mult}
=
\frac{
\int_I
\|\chi\mathcal P_{NS}\|_{\dot H^{-1}}^2dt
}{
\nu^2
\int_I\int
\chi|\nabla S|^2\,dxdt
}.
}
$$

若 cutoff 按 Navier--Stokes scaling 協變縮放，這個 ratio 仍 scale invariant。

但 $\dot H^{-1}$ 本身是 nonlocal norm，所以 ``cutoff-weighted'' 仍不等於真正 geometric locality。再者，multiplication by $\chi$ 並不自動產生一個 closed localized evolution equation。因此它仍只是 C3-P 的 candidate；真正 stability theorem 可能需要 weighted dual norm、commutator terms 或 localized projected operator。

---

# 21. Scaling audit

N–S scaling：

$$
S_\lambda
=
\lambda^2S(\lambda x,\lambda^2t).
$$

equation-level perturbation：

$$
(\mathcal P_{NS})_\lambda
=
\lambda^4
\mathcal P_{NS}(\lambda x,\lambda^2t).
$$

因此：

$$
\|\mathcal P_\lambda\|_{\dot H^{-1}}
=
\lambda^{3/2}
\|\mathcal P\|_{\dot H^{-1}},
$$

所以：

$$
\int
\|\mathcal P_\lambda\|_{\dot H^{-1}}^2dt
=
\lambda
\int
\|\mathcal P\|_{\dot H^{-1}}^2dt.
$$

同時：

$$
\int
\|S_\lambda\|_{\dot H^1}^2dt
=
\lambda
\int
\|S\|_{\dot H^1}^2dt.
$$

故：

$$
\boxed{
\mathfrak P_I^{\rm glob}
}
$$

scale invariant。

---

# 22. 注意：operator diagnostics 仍只是 candidate

目前未證：

$$
\mathfrak P_I^{\rm glob}<\varepsilon
\Rightarrow
\text{SSA approximation theorem},
$$

也未證：

$$
\mathfrak P_I^{\rm glob}\gg1
\Rightarrow
\text{regularity}.
$$

它的作用是避免：

$$
\boxed{
\text{zero energy pairing}
}
$$

被偷換成：

$$
\boxed{
\text{small operator}.
}
$$

---

# 23. Balance–Dynamics diagnostic plane

若先做 whole-space/window diagnostic，至少要同時保存 balance 與 operator coordinates：

$$
\boxed{
(\rho_I,\mathfrak P_I^{\rm glob}).
}
$$

可區分：

## BD-1 — Balance-SSA / Operator-small

$$
|\rho_I|\ll1,
\qquad
\mathfrak P_I^{\rm glob}\ll1.
$$

這才是值得測試的 model-like candidate regime。

## BD-2 — Balance-SSA / Operator-large

$$
|\rho_I|\ll1,
\qquad
\mathfrak P_I^{\rm glob}\gtrsim1.
$$

energy balance看似 SSA，

但 hidden orthogonal dynamics很大。

## BD-3 — Cancellation corridor

$$
\rho_I\to-1^+.
$$

gross SSA與 boundary current大幅 cancellation。

## BD-4 — Boundary driven

$$
\rho_I\gg1
$$

或：

$$
A_I\le0,\quad B_I>0.
$$

---

# 24. Miller 2024/2026 對 operator-large regime 的警告

Miller [2] 的 strain–vorticity interaction 工作證：

$$
\boxed{
\langle-\Delta S,\omega\otimes\omega\rangle=0,
}
$$

並對 isolating reverse strain–vorticity interaction的 model equation建立 global regularity。

該工作也給出 regularity criteria，用來分析 advection何時 depletion nonlinearity。

所以：

$$
\boxed{
\text{large omitted/operator terms不必然是 blow-up driver；
它們可能是 depletion mechanism}.
}
$$

因此：

$$
\mathfrak P_I^{\rm glob}
$$

即使作為 magnitude diagnostic，也必須再拆 interaction type，而不能只看總量。

---

# 25. Adjoint cutoff 的 X-Integration 意義

原 moving cutoff有：

- gauge；
- advection；
- diffusion；
- Betchov；
- pressure。

adjoint cutoff將前三者吸收到 cutoff evolution。

所以：

$$
\boxed{
B_\chi
=
\int\nabla\chi\cdot
\left(
\frac13F_B+F_p
\right)
}
$$

是更乾淨的 correction current。

新增：

$$
\boxed{
G_{\rm ADJ}
}
$$

bulk/boundary ratio應優先使用 adjoint cutoff，或明確扣除非-adjoint gauge terms。

---

# 26. Gauge-clean 不等於 boundary-small

即使：

$$
\partial_t\chi
+
u\cdot\nabla\chi
+
\nu\Delta\chi=0,
$$

仍可能：

$$
|B_\chi|
$$

很大。

尤其 $F_p$ 含 pressure Hessian，而

$$
-\Delta p
=
|S|^2-\frac12|\omega|^2
$$

使 $\nabla^2p$ 在 whole space 中可由 Riesz-type elliptic operators 表示，因此具有 nonlocal source sensitivity。

所以：

$$
\boxed{
\text{gauge-clean}
\neq
\text{boundary-small}.
}
$$

---

# 27. Pressure/Betchov correction split

定義：

$$
B_I
=
B_I^B+B_I^p,
$$

其中：

$$
B_I^B
=
\frac13
\int_I
\int
\nabla\chi\cdot F_B,
$$

$$
B_I^p
=
\int_I
\int
\nabla\chi\cdot F_p.
$$

若：

$$
|B_I|
$$

很大，

至少：

$$
|B_I^B|
\ge
\frac12|B_I|
$$

或：

$$
|B_I^p|
\ge
\frac12|B_I|.
$$

因此 boundary-dominated branch再分：

$$
\boxed{
\text{Betchov-current dominated}
\quad\vee\quad
\text{pressure-current dominated}.
}
$$

---

# 28. Cancellation corridor 的 component debt

若：

$$
\rho_I\to-1^+
$$

且：

$$
A_I>0,
$$

則：

$$
B_I\sim-A_I.
$$

所以至少一個：

$$
B_I^B,
\quad
B_I^p
$$

至少滿足：

$$
\boxed{
\max
\left\{
|B_I^B|,|B_I^p|
\right\}
\ge
\frac12|B_I|
\sim
\frac12A_I.
}
$$

因此至少一個 component 具有 $\Omega(A_I)$ 的 lower-bound magnitude，而不是僅僅 $O(A_I)$。

near-perfect depletion不能靠所有 correction components都小完成。

---

# 29. Ratio route的最終裁決

### $\rho<-1$

positive growth不可能。

### $\rho\to-1^+$

survives，但付 cancellation-precision debt。

### $\rho\to0$

survives，且不能解讀為 dynamical SSA closeness。

### $\rho\to+\infty$

survives，boundary/pressure current成主要 carrier。

所以：

$$
\boxed{
\rho
}
$$

只能作：

$$
\boxed{
\text{local strain-energy growth carrier classifier}.
}
$$

不能作 standalone regularity parameter。

---

# 30. Balance Fixed Point / Dynamics Fixed Point Separation

即使：

$$
\rho_n\to0
$$

而：

$$
\frac{
\Delta E_n+D_n
}{
A_n
}
\to1,
$$

只代表：

$$
\boxed{
\text{strain-energy balance becomes SSA-like}.
}
$$

不代表：

$$
\boxed{
S_n
\text{ approaches an SSA-model solution}.
}
$$

本文稱：

$$
\boxed{
\textbf{Balance Fixed Point / Dynamics Fixed Point Separation}.
}
$$

這對 True ETN 非常重要：

relation-level balance convergence不能自動提升成 operator-level dynamical convergence。

---

# 31. True ETN 更新

local strain state應分兩層。

## Balance layer

$$
\boxed{
\Theta^{bal}
=
(E,D,A,B,\rho,\kappa).
}
$$

## Operator layer

$$
\boxed{
\Theta^{op}
=
\left(
\mathcal N_{SSA},
\mathcal P_{NS},
\mathfrak P^{\rm glob},
\mathfrak P_{\chi}^{\rm mult},
\operatorname{Prov}
\right),
}
$$

其中：

$$
\mathcal N_{SSA}
=
\frac23P_{st}(S^2).
$$

因此：

$$
\boxed{
\Theta^{bal}\text{ convergence}
\not\Rightarrow
\Theta^{op}\text{ convergence}.
}
$$

---

# 32. X-Integration hard guards

## G-ADJ

ratio使用 adjoint cutoff或完整 gauge subtraction。

## G-GROW

ratio只在：

$$
\Delta E>0
$$

growth windows中作 growth-carrier判斷。

## G-RATIO

若：

$$
A>0,
$$

positive growth要求：

$$
\rho>-1.
$$

## G-CANCEL

若：

$$
\rho\to-1,
$$

必須保存 gross：

$$
A,\ B
$$

不能只保存 residual：

$$
A+B.
$$

## G-OP

$$
B/A\to0
$$

不得推出：

$$
\mathcal P_{NS}\to0.
$$

## G-PROJ

global：

$$
\langle\mathcal P_{NS},S\rangle=0
$$

只是 orthogonality，不是 smallness。

## G-PRESS

pressure與 Betchov correction必須分開保存。

---

# 33. 新 frontier：C3-P

C3-O 已回答：

> bulk/boundary ratio本身能不能成為 rigidity theorem？

答案：

$$
\boxed{
\textbf{不能。}
}
$$

missing information是：

$$
\boxed{
\text{orthogonal perturbation operator本身的 dynamical effect}.
}
$$

正式下一題：

$$
\boxed{
\textbf{C3-P — Operator-Level Depletion and Pressure/Betchov Current Rigidity}.
}
$$

---

# 34. C3-P proof obligations

## P1 — Local operator defect

為

$$
\mathcal P_{NS}
=
P_{st}
\left(
(u\cdot\nabla)S
+\frac13S^2
+\frac14\omega\otimes\omega
\right)
$$

建立真正 ancestry-localized scale-critical dual norm，並比較 $\mathfrak P_{I,\chi}^{\rm mult}$、weighted $\dot H^{-1}$ norm 與 projection/cutoff commutator。

## P2 — Small-operator regime

若某個 **localized** operator defect $\mathfrak P_n^{\rm loc}\to0$，能否 rigorously 證 rescaled ancestry dynamics 接近 SSA model？

需要 stability theorem，不是 balance identity。

## P3 — Large-operator depletion split

把：

$$
\mathcal P_{NS}
$$

拆成：

- advection；
- residual strain self-interaction；
- vorticity-to-strain coupling。

## P4 — Pressure current near/far split

對：

$$
F_p
=
(\nabla^2p-\Delta pI)u
$$

用 pressure Poisson equation做 core/far source decomposition。

## P5 — Betchov-current spectral/helical split

研究 $F_B$ 與其 source $\operatorname{tr}(G^3)$ 在 Fourier/helical decomposition 下的 homochiral / heterochiral contributions。

必須保留 guard：helical decomposition 本質上是 spectral/nonlocal representation，不能直接稱為 physical-space ``local helical split''。

## P6 — Cancellation corridor operator test

若：

$$
\rho_n\to-1^+,
$$

判定 cancellation corridor 是否能推出任何 localized operator-defect lower bound；目前不能從 scalar balance identity 自動推出

$$
\mathfrak P_n^{\rm loc}\to\infty.
$$

## P7 — Balance/operator phase diagram

建立：

$$
(\rho_n,\mathfrak P_n^{\rm loc})
$$

各 branch的 possible / known-regular / model-like-dangerous / open 區域。

## P8 — Adjoint cutoff propagation

分析 terminal ancestry cutoff 向 earlier times 的 effective radius、Gaussian/Aronson-type tails、drift distortion 與 pressure sensitivity；不得假設 compact support backward persistence。

---

# 35. 正式狀態

$$
\boxed{
\begin{aligned}
\text{adjoint cutoff cancellation}
&:\ \mathrm{PROVED},\\
\text{gauge-clean strain balance}
&:\ \mathrm{PROVED},\\
\text{growth-carrier dichotomy}
&:\ \mathrm{PROVED},\\
\rho>-1\text{ necessary for }A>0\text{ growth}
&:\ \mathrm{PROVED},\\
\rho_I\le-1\text{ with }A_I>0\text{ growth sector}
&:\ \mathrm{EXCLUDED},\\
\text{cancellation-precision debt}
&:\ \mathrm{PROVED},\\
\rho\to0\Rightarrow\text{SSA operator closeness from }\rho\text{ alone}
&:\ \mathrm{NON\mbox{-}IDENTIFIABLE/NO\mbox{-}GO},\\
\langle\mathcal P_{NS},S\rangle=0
&:\ \mathrm{PROVED\ HERE\ UNDER\ DECAY},\\
\text{SSA model finite-time blowup}
&:\ \mathrm{EXTERNAL\ THEOREM},\\
\text{conditional full-NS blowup under perturbative condition}
&:\ \mathrm{EXTERNAL\ THEOREM},\\
\mathfrak P_I^{\rm glob}\text{ scale invariance}
&:\ \mathrm{PROVED},\\
\mathfrak P_I^{\rm glob}\text{ as stability criterion}
&:\ \mathrm{OPEN},\\
\text{balance/operator rigidity}
&:\ \mathrm{OPEN}.
\end{aligned}
}
$$

---

# 36. 結論

C3-N 把 local strain dynamics寫成：

$$
\text{bulk SSA}
+
\text{boundary/gauge package}.
$$

C3-O 使用 adjoint cutoff把 gauge/advection/diffusion cutoff terms exact消掉：

$$
\boxed{
E_\chi'
+
D_\chi
=
A_\chi+B_\chi.
}
$$

對 positive strain-growth window：

若：

$$
A>0,
$$

必須：

$$
\boxed{
\rho=\frac BA>-1.
}
$$

因此：

$$
\boxed{
\rho\le-1
}
$$

是真正 hard depletion sector。

但：

$$
\rho\to-1^+,
\qquad
\rho\to0,
\qquad
\rho\to+\infty
$$

全部仍存活。

更重要的是：

$$
\boxed{
\text{SSA-like balance}
\not\Rightarrow
\text{SSA-like dynamics}.
}
$$

full N–S 被 SSA model丟掉的 perturbation對 global strain energy恰好正交，

所以它對當下 enstrophy derivative 的 pairing 可以恰好為零，

但這個 scalar zero 並不排除它對未來 dynamics 產生顯著作用。

因此 scalar ratio route 作為 **standalone rigidity route** 已經走到極限；它仍可保留為 growth-carrier classifier，並與 operator diagnostics 聯合使用。

下一輪必須升級到：

$$
\boxed{
\textbf{C3-P — Operator-Level Depletion and Pressure/Betchov Current Rigidity}.
}
$$

---

# 37. v0.2 theorem-safety guards

## T-SCOPE

所有 C3-O ratio theorem 都是 smooth/pre-singular window identities 或其 algebraic consequences；本文沒有把它們提升成 weak-solution singularity theorem。

## T-RATIO-DOMAIN

$\rho_I=B_I/A_I$ 只在 $A_I>0$ 的 ratio branch 使用。$A_I\le0$ 的 positive-growth windows 單獨歸入 boundary-current-driven branch。

## T-ADJOINT-TAIL

Adjoint cutoff 消除的是 scalar cutoff transport/diffusion package，不是把 spatial communication 或 pressure nonlocality 消掉。

## T-ORTHO

$\langle\mathcal P_{NS},S\rangle=0$ 是 scalar orthogonality；不得轉譯成 $\mathcal P_{NS}$ norm smallness。

## T-MILLER

Miller 的 conditional blow-up theorem 使用特定 $L^2$ relative perturbation hypothesis；不得與本文 $\dot H^{-1}$ diagnostic 混同。

## T-LOCALITY

$\mathfrak P_I^{\rm glob}$ 是 whole-space/window diagnostic；$\mathfrak P_{I,\chi}^{\rm mult}$ 只是 cutoff-weighted candidate，因 $\dot H^{-1}$ 仍然 nonlocal。真正 C3-P local stability route 仍需建立 $\mathfrak P^{\rm loc}$ 與 cutoff/projection commutator control。

---

# References

1. E. Miller, *Finite-time blowup for a Navier–Stokes model equation for the self-amplification of strain*, Analysis & PDE 16 (2023), 997–1032; arXiv:1910.05415v6. The conditional full Navier–Stokes blow-up statement used here is Theorem 1.14 / Section 6 in the arXiv v6 numbering.
2. E. Miller, *On the interaction of strain and vorticity for solutions of the Navier–Stokes equation*, Pure and Applied Analysis 8 (2026), 247–270; arXiv:2407.02691v2.
3. M. Carbone, M. Wilczek, *Only two Betchov homogeneity constraints exist for isotropic turbulence*, Journal of Fluid Mechanics 948 (2022), R2; arXiv:2112.12820.
4. E. Miller, *A regularity criterion for the Navier–Stokes equation involving only the middle eigenvalue of the strain tensor*, Arch. Rational Mech. Anal. 235 (2020).
5. R. Betchov, *An inequality concerning the production of vorticity in isotropic turbulence*, Journal of Fluid Mechanics 1 (1956), 497–504.

# Internal dependencies

- `NS_C3M_VorticityStrain_Betchov_GeometryDebt_v0.1.md`
- `NS_C3N_LocalizedBetchov_StrainBoundaryBalance_v0.1.md`
- `NS_C3K_AbsoluteOccupancy_OneMomentGap_v0.1.md`
- `NS_C3L_CriticalMomentEscape_StrainGeometryDebt_v0.1.md`
- `NS_C3J_GaugeCorrected_Reentry_Hysteresis_NoGo_v0.1.md`
- `True ETN / 無限維張力場`
- `X_Integral_Unified_Program_v0.2.md`

Next:

$$
\boxed{
\textbf{C3-P — Operator-Level Depletion and Pressure/Betchov Current Rigidity}
}
$$
