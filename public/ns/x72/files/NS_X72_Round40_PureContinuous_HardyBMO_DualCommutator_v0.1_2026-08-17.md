# NS × X 積分 × 24/72 範式實戰
## Round 40 — Pure Continuous Hardy–BMO Dual Commutator / Critical Campanato-Transfer Route

- 日期：2026-08-17
- 版本：v0.1
- 狀態：Proof-Route Experiment / Continuous-Only Hardy–BMO Endpoint Branch
- canonical source：UTF-8 Markdown
- canonical math delimiters：inline `$...$`；display `$$...$$`
- 前一輪：`NS_X72_Round39_PureContinuous_CriticalEndpoint_DiniHardyCompensation_v0.1_2026-08-17.md`
- 本輪目標：Round 39 已確認 incompressibility提供 pressure source的 Hardy-space compensation，但不自動提供 radial Dini summability。本輪改走 dual route：
  $$
  q\in\mathcal H^1,
  \qquad
  [u\cdot\nabla,\mathcal T_0^\ast]E_p
  \stackrel{?}{\in}
  \mathrm{BMO}.
  $$
  利用 Round 38 pressure self-commutator null identity，將 BMO partner進一步降為 local cofactor $C_S^0$，建立 exact two-increment commutator representation、Hardy–BMO energy charging law與 critical Campanato/Dini threshold。
- 非主張：本文沒有證明 dual commutator無條件屬於 BMO。本文證明的是：Hardy side可由 incompressible enstrophy支付，但 BMO side完整承接 one-total-derivative criticality；standard Coifman–Rochberg–Weiss $L^p$ commutator estimate本身不提供所需的 BMO target。

---

# 0. Round 39 handoff

Round 39 得到 incompressible pressure source：

$$
\boxed{
q
=
|S|^2-\frac12|\omega|^2
=
\sum_j
\nabla u_j\cdot\partial_j u,
}
\tag{0.1}
$$

其中每一項是 curl-free / divergence-free product。

因此 classical div–curl / incompressibility compensation給：

$$
\boxed{
\|q\|_{\mathcal H^1}
\lesssim
\|\nabla u\|_2^2.
}
\tag{0.2}
$$

Round 38–39 defect commutator pairing：

$$
\boxed{
\mathcal J_{\rm TR}
=
\left\langle
E,
[D_u,\mathcal T_0]q
\right\rangle,
\qquad
D_u=u\cdot\nabla.
}
\tag{0.3}
$$

Round 39 dual identity：

$$
\boxed{
\mathcal J_{\rm TR}
=
\left\langle
[D_u,\mathcal T_0^\ast]E,
q
\right\rangle.
}
\tag{0.4}
$$

Round 39 STOP：

$$
\boxed{
\text{STOP-C43}
=
\text{Critical Dini / Hardy–Increment Mismatch Gap}.
}
$$

---

# 1. Pressure component disappears from the dual pairing

Round 38 Pressure Self-Commutator Null：

$$
\boxed{
\left\langle
H,
[D_u,\mathcal T_0]q
\right\rangle
=
0,
}
\tag{1.1}
$$

where：

$$
H=\mathcal T_0q.
$$

因：

$$
E=H+C,
$$

得到：

$$
\boxed{
\mathcal J_{\rm TR}
=
\left\langle
C,
[D_u,\mathcal T_0]q
\right\rangle.
}
\tag{1.2}
$$

dualizing：

$$
\boxed{
\mathcal J_{\rm TR}
=
\left\langle
[D_u,\mathcal T_0^\ast]C,
q
\right\rangle.
}
\tag{1.3}
$$

定義：

$$
\boxed{
\mathcal A_C
=
[D_u,\mathcal T_0^\ast]C.
}
\tag{1.4}
$$

所以真正的 Hardy–BMO target不是：

$$
[D_u,\mathcal T_0^\ast]E,
$$

而是：

$$
\boxed{
\mathcal A_C
}
$$

built only from velocity transport and local cofactor geometry。

---

# 2. Hardy–BMO charging law

由 real Hardy–BMO duality：

$$
\boxed{
|\mathcal J_{\rm TR}|
\le
C
\|q\|_{\mathcal H^1}
\|\mathcal A_C\|_{\mathrm{BMO}}.
}
\tag{2.1}
$$

使用 (0.2)：

$$
\boxed{
|\mathcal J_{\rm TR}|
\le
C
\|\nabla u\|_2^2
\|\mathcal A_C\|_{\mathrm{BMO}}.
}
\tag{2.2}
$$

命名：

$$
\boxed{
\textbf{Hardy–BMO Commutator Charging Law}.
}
$$

這是本輪第一個核心 route reduction。

---

# 3. Energy-dissipation weighted spacetime closure

NS kinetic-energy inequality：

$$
\boxed{
\frac12
\|u(t)\|_2^2
+
\nu
\int_0^t
\|\nabla u(s)\|_2^2ds
\le
\frac12
\|u_0\|_2^2.
}
\tag{3.1}
$$

所以若：

$$
\boxed{
\|\mathcal A_C\|_{L_t^\infty\mathrm{BMO}_x}
\le
B_\ast
}
\tag{3.2}
$$

on：

$$
[0,T],
$$

則：

$$
\boxed{
\int_0^T
|\mathcal J_{\rm TR}(t)|dt
\le
\frac{
C
}{
\nu
}
\|u_0\|_2^2
B_\ast.
}
\tag{3.3}
$$

更一般地，只要：

$$
\boxed{
\int_0^T
\|\nabla u\|_2^2
\|\mathcal A_C\|_{\mathrm{BMO}}
dt
<
\infty,
}
\tag{3.4}
$$

transport–Riesz contribution可直接加入 defect-energy ledger。

所以 Hardy side本身已接到 basic energy dissipation。

真正問題全部轉移到：

$$
\boxed{
\mathcal A_C\in\mathrm{BMO}.
}
$$

---

# 4. Exact operator factorization

因：

$$
\mathcal T_0^\ast
$$

commutes with spatial derivatives，

$$
\boxed{
\begin{aligned}
\mathcal A_C
&=
[D_u,\mathcal T_0^\ast]C
\\
&=
\sum_{k=1}^3
[u_k,\mathcal T_0^\ast]
(
\partial_kC
).
\end{aligned}
}
\tag{4.1}
$$

命名：

$$
\boxed{
\textbf{CRW Factorization of the Transport Commutator}.
}
$$

這將 transport commutator連接到 classical Coifman–Rochberg–Weiss type commutators。

---

# 5. What standard CRW theory actually gives

對 Calderón–Zygmund operator：

$$
T,
$$

classical CRW theory的自然 strong estimate是：

$$
\boxed{
\|[b,T]f\|_{L^p}
\le
C_p
\|b\|_{\mathrm{BMO}}
\|f\|_{L^p},
\qquad
1<p<\infty.
}
\tag{5.1}
$$

因此 (4.1) 給：

$$
\boxed{
\|\mathcal A_C\|_{L^p}
\le
C_p
\|u\|_{\mathrm{BMO}}
\|\nabla C\|_{L^p}.
}
\tag{5.2}
$$

但 Hardy–BMO dual route需要：

$$
\boxed{
\mathcal A_C\in\mathrm{BMO},
}
$$

不是：

$$
L^p.
$$

所以：

$$
\boxed{
\textbf{
standard CRW boundedness does not by itself close the Hardy–BMO route.
}
}
\tag{5.3}
$$

這是一個 target-space mismatch，不是 commutator不存在。

---

# 6. Exact double-increment kernel

令：

$$
K_0(z)
$$

為：

$$
\mathcal T_0
$$

的 even trace-free kernel。

直接 kernel calculation：

$$
\boxed{
\mathcal A_C(x)
=
\operatorname{p.v.}
\int
[
u(x)-u(y)
]
\cdot
\nabla K_0(x-y)
:
C(y)
\,dy.
}
\tag{6.1}
$$

若：

$$
C
$$

為 constant tensor，

commutator必為零。

利用：

$$
\nabla\cdot u=0
$$

可驗證：

$$
\operatorname{p.v.}
\int
[
u(x)-u(y)
]
\cdot
\nabla K_0(x-y)
dy
=
0.
$$

因此可 losslessly 改寫：

$$
\boxed{
\mathcal A_C(x)
=
\operatorname{p.v.}
\int
[
u(x)-u(y)
]
\cdot
\nabla K_0(x-y)
:
[
C(y)-C(x)
]
dy.
}
\tag{6.2}
$$

命名：

$$
\boxed{
\textbf{Dual Two-Increment Commutator Identity}.
}
$$

---

# 7. Hardy cancellation replaces the third increment

Round 38 primal pairing：

$$
\delta u
\times
\delta E
\times
\delta q.
$$

Round 40 dual representation：

$$
q\in\mathcal H^1
$$

將 source cancellation吸收到 Hardy test structure，

而 BMO partner只剩：

$$
\boxed{
\delta u
\times
\delta C.
}
$$

因此：

$$
\boxed{
\textbf{
Hardy compensation removes the explicit }q\textbf{ increment,
but does not remove the total derivative threshold.
}
}
\tag{7.1}
$$

它把 critical regularity burden從 three-field simplex移到 two-field edge。

---

# 8. Local two-increment modulus

定義 uniform translation moduli：

$$
\boxed{
\omega_{u,\infty}(r)
=
\sup_{|z|\le r}
\|\delta_zu\|_\infty,
}
\tag{8.1}
$$

$$
\boxed{
\omega_{C,\infty}(r)
=
\sup_{|z|\le r}
\|\delta_zC\|_\infty.
}
\tag{8.2}
$$

由：

$$
|\nabla K_0(z)|
\lesssim
|z|^{-4},
$$

near-diagonal absolute envelope：

$$
\boxed{
\|\mathcal A_C^{<\ell}\|_\infty
\lesssim
\int_0^\ell
\frac{
\omega_{u,\infty}(r)
\omega_{C,\infty}(r)
}{
r^2
}
dr.
}
\tag{8.3}
$$

所以 near part亦受同一 quantity控制其 BMO norm。

定義：

$$
\boxed{
\mathfrak D_{u,C}^{\mathrm{BMO}}(\ell)
=
\int_0^\ell
\frac{
\omega_{u,\infty}(r)
\omega_{C,\infty}(r)
}{
r^2
}
dr.
}
\tag{8.4}
$$

---

# 9. Two-field one-total-derivative threshold

若：

$$
\omega_{u,\infty}(r)
\lesssim
r^{s_u},
$$

$$
\omega_{C,\infty}(r)
\lesssim
r^{s_C},
$$

則：

$$
\mathfrak D_{u,C}^{\mathrm{BMO}}
$$

near zero behaves：

$$
\boxed{
\int_0
r^{s_u+s_C-2}dr.
}
\tag{9.1}
$$

所以 absolute local closure要求：

$$
\boxed{
s_u+s_C>1.
}
\tag{9.2}
$$

critical endpoint：

$$
\boxed{
s_u+s_C=1
}
\tag{9.3}
$$

再次只剩：

$$
\int_0
\frac{dr}{r}
$$

型 Dini/log barrier。

命名：

$$
\boxed{
\textbf{Hardy-Absorbed One-Derivative Threshold}.
}
$$

---

# 10. Exact scaling of the two-field endpoint

NS scaling：

$$
u_\Lambda
=
\Lambda
u(\Lambda x,\Lambda^2t),
$$

$$
C_\Lambda
=
\Lambda^4
C(\Lambda x,\Lambda^2t).
$$

Hölder/Campanato seminorm scales：

$$
[u_\Lambda]_{C^{s_u}}
=
\Lambda^{1+s_u}
[u]_{C^{s_u}},
$$

$$
[C_\Lambda]_{C^{s_C}}
=
\Lambda^{4+s_C}
[C]_{C^{s_C}}.
$$

product scales：

$$
\boxed{
\Lambda^{5+s_u+s_C}.
}
\tag{10.1}
$$

而：

$$
\mathcal A_C
=
[D_u,\mathcal T_0^\ast]C
$$

scales：

$$
\boxed{
\Lambda^6.
}
\tag{10.2}
$$

所以 exact criticality要求：

$$
\boxed{
s_u+s_C=1.
}
\tag{10.3}
$$

因此 Hardy–BMO route沒有改變 total critical derivative count。

它只重新分配了哪一側攜帶 cancellation。

---

# 11. Cofactor modulus is strain modulus with amplitude

Round 38：

$$
C
=
S^2-\frac13|S|^2I.
$$

exact increment：

$$
\boxed{
\begin{aligned}
\delta C
={}&
\frac12
[
(S_x+S_y)\delta S
+
\delta S(S_x+S_y)
]
\\
&-
\frac13
[
(S_x+S_y):\delta S
]
I.
\end{aligned}
}
\tag{11.1}
$$

所以：

$$
\boxed{
|\delta C|
\le
C
(
|S_x|+|S_y|
)
|\delta S|.
}
\tag{11.2}
$$

因此：

$$
\boxed{
\text{BMO commutator endpoint}
\to
\text{velocity increment}
\times
\text{strain amplitude}
\times
\text{strain increment}.
}
\tag{11.3}
$$

它仍然回到 strain regularity，而不是新 pressure reservoir。

---

# 12. Energy-level Hardy gain is real

由 NS energy：

$$
\nu
\int_0^T
\|\nabla u\|_2^2dt
\le
\frac12\|u_0\|_2^2,
$$

及：

$$
\|q\|_{\mathcal H^1}
\lesssim
\|\nabla u\|_2^2,
$$

有：

$$
\boxed{
\int_0^T
\|q(t)\|_{\mathcal H^1}dt
\lesssim
\frac{
\|u_0\|_2^2
}{
\nu
}.
}
\tag{12.1}
$$

所以 Hardy pressure-source norm在 spacetime $L_t^1$ 意義下確實是 energy-level budget。

這是 Round 39 incompressibility gain最強的 usable consequence。

---

# 13. But the BMO partner is not energy-level free

若希望僅靠：

$$
\|\nabla u\|_2,
\qquad
\|\nabla S\|_2
$$

等 low $L^2$ Sobolev quantities直接控制：

$$
\|\mathcal A_C\|_{\mathrm{BMO}},
$$

scaling / concentration立即顯示這不可能是簡單 energy-level estimate。

$\mathrm{BMO}$ 對：

$$
\mathcal A_C
$$

保留 amplitude scaling：

$$
\Lambda^6.
$$

而 ordinary $L^2$ derivative norms會因 spatial integrability損失 powers。

因此：

$$
\boxed{
\textbf{
Hardy energy control does not automatically imply a matching BMO commutator control.
}
}
\tag{13.1}
$$

---

# 14. Standard CRW fallback returns to higher gradients

若放棄 Hardy–BMO duality，

改以：

$$
q\in L^{p'},
\qquad
\mathcal A_C\in L^p,
$$

then CRW factorization可用。

取：

$$
p=\frac32,
\qquad
p'=3.
$$

有：

$$
\boxed{
|\mathcal J_{\rm TR}|
\le
\|q\|_3
\|\mathcal A_C\|_{3/2}
}
\tag{14.1}
$$

及：

$$
\boxed{
\|\mathcal A_C\|_{3/2}
\lesssim
\|u\|_{\mathrm{BMO}}
\|\nabla C\|_{3/2}.
}
\tag{14.2}
$$

---

# 15. CRW fallback quantitative return to Round 05

Sobolev / Hodge：

$$
\boxed{
\|u\|_{\mathrm{BMO}}
\lesssim
\|\nabla u\|_3
\lesssim
\|S\|_2^{1/2}
\|\nabla S\|_2^{1/2}.
}
\tag{15.1}
$$

cofactor gradient：

$$
|\nabla C|
\lesssim
|S||\nabla S|,
$$

所以：

$$
\boxed{
\|\nabla C\|_{3/2}
\lesssim
\|S\|_6
\|\nabla S\|_2
\lesssim
\|\nabla S\|_2^2.
}
\tag{15.2}
$$

pressure source：

$$
\boxed{
\|q\|_3
\lesssim
\|S\|_6^2
+
\|\omega\|_6^2
\lesssim
\|\nabla S\|_2^2.
}
\tag{15.3}
$$

因此：

$$
\boxed{
|\mathcal J_{\rm TR}|
\lesssim
\|S\|_2^{1/2}
\|\nabla S\|_2^{9/2}.
}
\tag{15.4}
$$

這遠高於 basic energy/enstrophy budget。

所以：

$$
\boxed{
\textbf{
the standard CRW }L^p\textbf{ fallback closes legality
but returns directly to the old higher-gradient obstruction.}
}
\tag{15.5}
$$

---

# 16. Why recent generic BMO relaxation no-go matters

transport–Riesz commutator literature顯示：

對 broad Riesz interaction classes，

常見：

$$
\|\nabla u\|_\infty
$$

transport regularity不能一般性直接降成：

$$
\|\nabla u\|_{\mathrm{BMO}}.
$$

因此不能因為本輪出現 Hardy–BMO duality，就自動宣稱：

$$
\boxed{
\text{BMO is enough for every part of the transport commutator}.
}
$$

我們的 special NS pairing確實比 generic norm estimate多了：

- pressure self-null；
- cofactor reduction；
- two-increment cancellation；

但 BMO endpoint仍需用這些 special structures重新證，而不能套 generic wishful bound。

---

# 17. Hardy cancellation and two-increment BMO are equivalent route views

Round 38 primal：

$$
\boxed{
\delta u
\,
\delta E
\,
\delta q.
}
$$

Round 40 dual：

$$
\boxed{
q\in\mathcal H^1
}
$$

加：

$$
\boxed{
\delta u
\,
\delta C.
}
$$

可理解為：

$$
\boxed{
\text{the Hardy atom cancellation replaces the explicit source increment}.
}
\tag{17.1}
$$

但 critical derivative count仍為一。

所以 Hardy–BMO並非一條完全不同的物理 mechanism。

它是同一 commutator cancellation的 dual representation。

---

# 18. Conditional Hardy–BMO closure theorem

假設 smooth NS on：

$$
[0,T],
$$

且：

$$
\boxed{
\mathcal A_C
=
[u\cdot\nabla,\mathcal T_0^\ast]C
\in
L_t^\infty\mathrm{BMO}_x,
}
\tag{18.1}
$$

with：

$$
\|\mathcal A_C\|_{L_t^\infty\mathrm{BMO}}
\le
B_\ast.
$$

則：

$$
\boxed{
\int_0^T
|
\langle
E,
[u\cdot\nabla,\mathcal T_0]q
\rangle
|
dt
\le
C
\nu^{-1}
\|u_0\|_2^2
B_\ast.
}
\tag{18.2}
$$

因此 transport–Riesz contribution to affine-defect energy is globally finite on the interval。

這是 genuine conditional closure。

但 hypothesis (18.1) 尚未由 NS basic energy導出。

---

# 19. Continuous Campanato formulation

BMO可由 mean oscillation定義：

$$
\boxed{
\|f\|_{\mathrm{BMO}}
=
\sup_{x_0,r>0}
\frac1{|B_r|}
\int_{B_r(x_0)}
|f-f_{B_r}|dx.
}
\tag{19.1}
$$

因此本輪 endpoint可完全以 continuous radius：

$$
r>0
$$

研究。

對 near field，

sufficient carrier：

$$
\boxed{
\mathfrak D_{u,C}^{\mathrm{BMO}}(\ell)
=
\int_0^\ell
\frac{
\omega_{u,\infty}(r)
\omega_{C,\infty}(r)
}{
r^2
}
dr.
}
\tag{19.2}
$$

far field則是 nonsingular Campanato oscillation problem。

不需要 Littlewood–Paley dyadic shell。

---

# 20. Critical endpoint remains logarithmic

若：

$$
\omega_u(r)\omega_C(r)
=
O(r),
$$

then：

$$
\boxed{
\mathfrak D_{u,C}^{\mathrm{BMO}}
\sim
\int_0^\ell
\frac{dr}{r}
}
\tag{20.1}
$$

仍 logarithmically divergent。

所以 Hardy–BMO route沒有奇蹟般移除 Round 39 的 endpoint log。

它把：

$$
\boxed{
\text{Pair-Dini }(u,q)
}
$$

換成：

$$
\boxed{
\text{Campanato-Dini }(u,C).
}
$$

---

# 21. Route comparison

目前 transport–Riesz endpoint有三種 Pure-C representations：

## R38 — primal triple increment

$$
\boxed{
\delta u
\,
\delta E
\,
\delta q,
\qquad
s_u+s_E+s_q=1.
}
$$

## R39 — defect-viscosity Pair-Dini

$$
\boxed{
\nabla E
\quad+\quad
\int
\omega_u\omega_q
\,dr/r.
}
$$

## R40 — Hardy–BMO dual

$$
\boxed{
q\in\mathcal H^1
\quad+\quad
[u\cdot\nabla,\mathcal T_0^\ast]C
\in\mathrm{BMO}.
}
$$

and local BMO commutator has：

$$
\boxed{
s_u+s_C=1
}
$$

critical endpoint。

所以三種 representation都停在同一 total-derivative criticality。

---

# 22. Representation-stable endpoint core

Round 39 曾判斷：

$$
\text{Hardy cancellation}
\neq
\text{automatic Dini}.
$$

Round 40 現在更精確：

$$
\boxed{
\text{Hardy cancellation}
\Rightarrow
\text{source side energy-level closure},
}
$$

但：

$$
\boxed{
\text{the missing critical derivative is transferred intact to the BMO partner}.
}
$$

所以 endpoint obstruction再次 representation-stable。

---

# 23. STOP-C44 — Hardy–BMO Transfer / Two-Increment BMO Endpoint Gap

$$
\boxed{
\begin{aligned}
\text{layer}
&=
\mathrm{Hardy\text{-}BMO\ dual\ commutator},
\\
q
&\in
\mathcal H^1,
\\
\|q\|_{\mathcal H^1}
&\lesssim
\|\nabla u\|_2^2,
\\
\text{pressure self component}
&=
0,
\\
\text{dual target}
&=
\mathcal A_C
=
[D_u,\mathcal T_0^\ast]C,
\\
\text{exact kernel}
&=
\delta u
\times
\delta C
\times
\nabla K_0,
\\
\text{Hardy side}
&=
\mathrm{energy\text{-}chargeable},
\\
\text{standard CRW}
&=
L^p\to L^p
\text{ target, not BMO target},
\\
\text{two-field criticality}
&=
s_u+s_C=1,
\\
\text{endpoint}
&=
\mathrm{Campanato/Dini\ logarithmic\ barrier},
\\
\text{CRW fallback}
&\to
\mathrm{higher\text{-}gradient\ Round\ 05},
\\
\text{missing}
&=
\mathrm{unconditional\ BMO/Campanato\ control
of\ the\ special\ cofactor\ transport\ commutator},
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
\textbf{STOP-C44:
Hardy–BMO Transfer / Two-Increment BMO Endpoint Gap}.
}
$$

---

# 24. 24/72 Ledger — Round 40

| Step | object | $B$ | $U$ | $O$ | $L$ | status |
|---|---|---|---|---|---|---|
| C606 | Hardy pressure source | $\mathsf C$ | div–curl compensation | scalar | $\mathsf F$ | STANDARD |
| C607 | cofactor dual reduction | $\mathsf C$ | self-null duality | targeted | $\mathsf F$ | EXACT |
| C608 | Hardy–BMO charging law | $\mathsf C$ | functional duality | scalar | $\mathsf F$ | PROVED conditionally |
| C609 | energy-weighted spacetime charge | $\mathsf C$ | NS energy | targeted | $\mathsf F$ | PROVED conditionally |
| C610 | CRW factorization | $\mathsf C$ | commutator algebra | relational | $\mathsf F$ | EXACT |
| C611 | standard CRW target mismatch | $\mathsf C$ | function-space map | targeted | $\mathsf F$ | IDENTIFIED |
| C612 | dual two-increment identity | $\mathsf C$ | singular integral | relational | $\mathsf F$ | EXACT |
| C613 | Hardy absorbs source increment | $\mathsf C$ | dual representation | $\mathsf X$ | $\mathsf F$ | IDENTIFIED |
| C614 | local BMO Dini carrier | $\mathsf C$ | continuous modulus | scalar | $\mathsf F$ | FORM |
| C615 | two-field derivative threshold | $\mathsf C$ | Hölder/Campanato | targeted | $\mathsf F$ | PROVED |
| C616 | exact critical scaling | $\mathsf C$ | scaling | scalar | $\mathsf F$ | PROVED |
| C617 | cofactor-to-strain modulus return | $\mathsf C$ | tensor algebra | relational | $\mathsf F$ | EXACT |
| C618 | Hardy spacetime energy budget | $\mathsf C$ | energy dissipation | scalar | $\mathsf F$ | PROVED |
| C619 | standard CRW $L^{3/2}$ fallback | $\mathsf C$ | harmonic analysis | targeted | $\mathsf F$ | CONDITIONAL |
| C620 | higher-gradient fallback estimate | $\mathsf C$ | Sobolev/Hodge | scalar | $\mathsf F$ | PROVED |
| C621 | conditional Hardy–BMO closure | $\mathsf C$ | defect energy | targeted | $\mathsf F$ | CONDITIONAL |
| C622 | unconditional special BMO commutator control | $\mathsf C$ | coupled NS | targeted | $\mathsf F$ | OPEN / STOP-C44 |

---

# 25. Continuous-versus-discrete status

本輪使用：

- real Hardy space；
- BMO / Campanato mean oscillation；
- continuous balls：
  $$
  B_r(x_0);
  $$
- continuous translation modulus；
- continuous singular-integral kernel。

沒有：

- atoms作為 proof substrate necessity；
- dyadic BMO grid；
- frequency shell index；
- discrete commutator states。

Hardy atomic language即使可用，也不是本輪 essential representation；

所有核心條件已寫成 continuous div–curl / Campanato形式。

因此：

$$
\boxed{
T_{\mathsf C\to\mathsf D}
=
\text{NOT YET REACHED}.
}
$$

---

# 26. Strongest results of Round 40

## R40-A — dual cofactor reduction

$$
\boxed{
\langle
E,
[D_u,\mathcal T_0]q
\rangle
=
\langle
[D_u,\mathcal T_0^\ast]C,
q
\rangle.
}
$$

## R40-B — energy-level Hardy charging

$$
\boxed{
|\mathcal J_{\rm TR}|
\lesssim
\|\nabla u\|_2^2
\|
[D_u,\mathcal T_0^\ast]C
\|_{\mathrm{BMO}}.
}
$$

## R40-C — exact two-increment dual commutator

$$
\boxed{
\mathcal A_C(x)
=
\operatorname{p.v.}
\int
[
u(x)-u(y)
]
\cdot
\nabla K_0(x-y)
:
[
C(y)-C(x)
]
dy.
}
$$

## R40-D — Hardy-absorbed critical endpoint

$$
\boxed{
s_u+s_C=1.
}
$$

Hardy compensation removes the explicit $q$ increment but transfers the critical derivative to the BMO partner.

## R40-E — standard CRW fallback does not solve the target problem

$$
\boxed{
\|\mathcal A_C\|_p
\lesssim
\|u\|_{\mathrm{BMO}}
\|\nabla C\|_p
}
$$

is useful, but it is not the required：

$$
\mathcal A_C\in\mathrm{BMO}.
$$

---

# 27. Next round — Special Cofactor Commutator / Campanato Cancellation

Round 40 顯示 generic CRW theory不直接給我們要的 BMO target。

但：

$$
C
=
S^2-\frac13|S|^2I
$$

不是 arbitrary tensor。

下一輪直接研究這個 special structure：

1. 將：
   $$
   \delta C
   $$
   完整展開成：
   $$
   (S_x+S_y)\delta S;
   $$

2. 將：
   $$
   \delta u
   $$
   分成 longitudinal / transverse increments；

3. 利用：
   $$
   \nabla\cdot u=0,
   \qquad
   \operatorname{tr}S=0;
   $$

4. 檢查 angular mean-zero kernel和 cofactor trace-free structure是否再消掉 leading affine increment；

5. 若 leading affine term cancellation，critical threshold可能從：
   $$
   s_u+s_C=1
   $$
   得到額外 modulus gain；

6. 若 affine term不消失，構造 divergence-free affine/quadratic witness正式證明 endpoint sharp；

7. 研究 Campanato mean oscillation，而不要求 pointwise $L^\infty$ modulus；

8. 保持 continuous balls / radii，不使用 dyadic BMO grids。

---

# 28. External primary-source anchors

1. Dong Li, Xiaoyi Zhang, *A regularity upgrade of pressure*, arXiv:2106.11852.
   - incompressibility與 div–curl structure給 pressure/pressure source Hardy-space regularity提升，並展示若干 endpoint regularity failure。

2. Elias Hess-Childs, Matthew Rosenzweig, Sylvia Serfaty, *Another look at regularity in transport-commutator estimates*, arXiv:2601.02326.
   - 對 broad Riesz transport commutators，常用 Lipschitz-gradient control一般不能直接降成 BMO；說明 generic BMO wishful estimate並不成立。

3. Enno Lenzmann, Armin Schikorra, *Sharp commutator estimates via harmonic extensions*, arXiv:1609.08547.
   - Coifman–Rochberg–Weiss、Riesz與其他 commutator estimates可由 cancellation / integration-by-parts structure推導，提供本輪 CRW factorization與 special-structure search的 harmonic-analysis背景。

4. Irina Holmes, Michael T. Lacey, Brett D. Wick, *Commutators in the Two-Weight Setting*, arXiv:1506.05747.
   - classical Coifman–Rochberg–Weiss result的現代 primary-source extension：BMO symbol控制 Riesz commutator的 $L^p$ boundedness。

本輪 dual cofactor reduction、Hardy–BMO charging law、dual two-increment identity、two-field critical scaling與 higher-gradient CRW fallback均為本文直接推導。

---

# 29. Commit state

$$
\boxed{
\begin{aligned}
\text{Route}
&=
\mathrm{Pure\ Continuous\ Hardy\text{-}BMO\ Dual\ Commutator},
\\
\text{Essential }\mathsf C\to\mathsf D
&=
\mathrm{Not\ reached},
\\
\text{Pressure source}
&=
\mathcal H^1\text{ at energy/enstrophy level},
\\
\text{Pressure self commutator}
&=
0,
\\
\text{Dual target}
&=
[D_u,\mathcal T_0^\ast]C_S^0,
\\
\text{Hardy side}
&=
\mathrm{energy\text{-}chargeable},
\\
\text{BMO side}
&=
\mathrm{critical\ two\text{-}increment\ problem},
\\
\text{Standard CRW}
&=
\mathrm{wrong\ target\ space\ for\ direct\ closure},
\\
\text{Critical threshold}
&=
s_u+s_C=1,
\\
\text{STOP-C44}
&=
\mathrm{Hardy\text{-}BMO\ Transfer/Two\text{-}Increment\ BMO\ Endpoint\ Gap},
\\
\text{Next}
&=
\mathrm{Special\ Cofactor\ Commutator/Campanato\ Cancellation}.
\end{aligned}
}
$$
