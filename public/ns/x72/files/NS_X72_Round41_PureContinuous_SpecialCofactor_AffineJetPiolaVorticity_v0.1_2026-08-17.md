# NS × X 積分 × 24/72 範式實戰
## Round 41 — Pure Continuous Special-Cofactor Commutator / Affine-Jet Cancellation and Piola–Vorticity Route

- 日期：2026-08-17
- 版本：v0.1
- 狀態：Proof-Route Experiment / Continuous-Only Special-Cofactor Branch
- canonical source：UTF-8 Markdown
- canonical math delimiters：inline `$...$`；display `$$...$$`
- 前一輪：`NS_X72_Round40_PureContinuous_HardyBMO_DualCommutator_v0.1_2026-08-17.md`
- 本輪目標：Round 40 將 Hardy–BMO dual route壓成 special cofactor commutator
  $$
  \mathcal A_C
  =
  [u\cdot\nabla,\mathcal T_0^\ast]C,
  \qquad
  C=S^2-\frac13|S|^2I.
  $$
  本輪不再視 $C$ 為 arbitrary tensor，而利用：
  - centered parity；
  - incompressibility；
  - cofactor quadratic algebra；
  - Piola null-Lagrangian identity；
  尋找 generic CRW/BMO estimate看不到的額外 cancellation。
- 非主張：本文沒有證明 Hardy–BMO endpoint閉合。本文證明的是：
  1. leading affine first-increment interaction exact cancellation；
  2. generic rotational branch的 second-jet curvature contribution可以非零，所以不存在 universal third-order cancellation；
  3. special cofactor的 nonlocal scalar projection可精確分解為 local pressure-source part + vorticity-stress Piola defect；
  4. fractional critical endpoint仍需 Zygmund/Campanato gain。

---

# 0. Round 40 handoff

Round 40 將 transport–Riesz defect pairing化為：

$$
\boxed{
\langle
E,
[D_u,\mathcal T_0]q
\rangle
=
\langle
\mathcal A_C,
q
\rangle,
}
\tag{0.1}
$$

其中：

$$
\boxed{
\mathcal A_C
=
[D_u,\mathcal T_0^\ast]C,
}
\tag{0.2}
$$

$$
\boxed{
C
=
S^2-\frac13|S|^2I.
}
\tag{0.3}
$$

且：

$$
\boxed{
\|q\|_{\mathcal H^1}
\lesssim
\|\nabla u\|_2^2.
}
\tag{0.4}
$$

所以 Hardy side可被 energy/enstrophy level支付。

剩餘：

$$
\boxed{
\mathcal A_C
\stackrel{?}{\in}
\mathrm{BMO}.
}
$$

Round 40 的 generic two-increment kernel：

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
\tag{0.5}
$$

naive fractional threshold：

$$
\boxed{
s_u+s_C=1.
}
$$

Round 40 STOP：

$$
\boxed{
\text{STOP-C44}
=
\text{Hardy–BMO Transfer / Two-Increment BMO Endpoint Gap}.
}
$$

---

# 1. Centered first and second differences

令：

$$
z\in\mathbb R^3.
$$

定義 centered first difference：

$$
\boxed{
D_zf(x)
=
\frac{
f(x+z)-f(x-z)
}{2}.
}
\tag{1.1}
$$

定義 centered second difference：

$$
\boxed{
\Delta_z^2f(x)
=
f(x+z)-2f(x)+f(x-z).
}
\tag{1.2}
$$

此外：

$$
\Delta_z^+f
=
f(x+z)-f(x),
$$

$$
\Delta_z^-f
=
f(x)-f(x-z).
$$

則：

$$
\boxed{
\Delta_z^+f+\Delta_z^-f
=
2D_zf,
}
\tag{1.3}
$$

$$
\boxed{
\Delta_z^+f-\Delta_z^-f
=
\Delta_z^2f.
}
\tag{1.4}
$$

---

# 2. Exact centered symmetrization of the cofactor commutator

由：

$$
K_0(-z)=K_0(z),
$$

所以：

$$
\nabla K_0(-z)
=
-\nabla K_0(z).
$$

將 (0.5) 以：

$$
y=x-z
$$

表示，並平均：

$$
z
\leftrightarrow
-z,
$$

得到 exact：

$$
\boxed{
\begin{aligned}
\mathcal A_C(x)
=
\frac12
\operatorname{p.v.}
\int
&
\left[
D_zu(x)
\cdot
\nabla K_0(z)
\right]
:
\Delta_z^2C(x)
\,dz
\\
+
\frac12
\operatorname{p.v.}
\int
&
\left[
\Delta_z^2u(x)
\cdot
\nabla K_0(z)
\right]
:
D_zC(x)
\,dz.
\end{aligned}
}
\tag{2.1}
$$

命名：

$$
\boxed{
\textbf{Centered Cofactor-Commutator Identity}.
}
$$

---

# 3. Affine-jet cancellation

若：

$$
u
$$

與：

$$
C
$$

在 neighborhood內皆 affine，

則：

$$
\Delta_z^2u=0,
$$

$$
\Delta_z^2C=0.
$$

所以：

$$
\boxed{
\mathcal A_C^{\rm local}=0.
}
\tag{3.1}
$$

對 actual NS cofactor更強：

若：

$$
u(x)=Ax+b
$$

affine，

則：

$$
S=\operatorname{sym}A
$$

constant，

因此：

$$
C
$$

constant，

所以 commutator local contribution exact vanish。

因此 Round 40 的 naive：

$$
\delta u
\times
\delta C
$$

first-first interaction其 leading affine jet並不真正存在。

---

# 4. Smooth local order gains one radial power

若：

$$
u,C\in C^2
$$

near：

$$
x,
$$

則：

$$
\boxed{
|D_zu|
\lesssim
|z|
\|\nabla u\|_{\infty,\rm loc},
}
\tag{4.1}
$$

$$
\boxed{
|\Delta_z^2u|
\lesssim
|z|^2
\|\nabla^2u\|_{\infty,\rm loc},
}
\tag{4.2}
$$

以及相同 estimates對：

$$
C.
$$

由：

$$
|\nabla K_0(z)|
\lesssim
|z|^{-4},
$$

三維 volume：

$$
dz
\sim
r^2drd\Omega,
$$

得到：

$$
\boxed{
\begin{aligned}
|\mathcal A_C^{<\ell}(x)|
\lesssim{}&
\int_0^\ell
r
\Big[
\|\nabla u\|_{\infty,\rm loc}
\|\nabla^2C\|_{\infty,\rm loc}
\\
&+
\|\nabla^2u\|_{\infty,\rm loc}
\|\nabla C\|_{\infty,\rm loc}
\Big]dr.
\end{aligned}
}
\tag{4.3}
$$

所以：

$$
\boxed{
|\mathcal A_C^{<\ell}(x)|
=
O(\ell^2)
}
\tag{4.4}
$$

at smooth points。

這比 raw：

$$
\delta u\delta C|z|^{-4}
$$

picture的 logarithmic first-jet counting更好。

---

# 5. Affine cancellation is not automatically fractional gain

定義 first modulus：

$$
\boxed{
\omega_f^{(1)}(r)
=
\sup_{|z|\le r}
\|D_zf\|.
}
\tag{5.1}
$$

以及 second modulus：

$$
\boxed{
\omega_f^{(2)}(r)
=
\sup_{|z|\le r}
\|\Delta_z^2f\|.
}
\tag{5.2}
$$

由 (2.1) near field受：

$$
\boxed{
\mathfrak Z_{u,C}(\ell)
=
\int_0^\ell
\frac{
\omega_u^{(1)}(r)
\omega_C^{(2)}(r)
+
\omega_u^{(2)}(r)
\omega_C^{(1)}(r)
}{
r^2
}
dr.
}
\tag{5.3}
$$

控制。

若：

$$
0<s<1,
$$

一般 Hölder/Besov regularity下：

$$
\omega_f^{(1)}(r)
\sim
r^s,
$$

且 second difference仍只有：

$$
\omega_f^{(2)}(r)
\sim
r^s.
$$

所以：

$$
\boxed{
s_u+s_C>1
}
\tag{5.4}
$$

仍是 generic fractional absolute-convergence threshold。

因此：

$$
\boxed{
\textbf{
affine-jet cancellation improves smooth-jet order,
but does not automatically move the fractional critical line.
}
}
\tag{5.5}
$$

---

# 6. Zygmund/little-Campanato interpretation

當某 field具有 one full derivative但 endpoint仍 critical，

second difference比 first difference更能看見：

$$
\boxed{
\text{departure from affine behavior}.
}
$$

例如若：

$$
\nabla f
$$

uniformly continuous，

則：

$$
\boxed{
|\Delta_z^2f(x)|
\le
|z|
\omega_{\nabla f}(2|z|).
}
\tag{6.1}
$$

所以 (5.3) 的 endpoint gain可由：

- little-Zygmund；
- VMO-gradient；
- Campanato affine-defect；
- Dini gradient modulus；

提供。

因此 Round 40 的 BMO endpoint更精確地應改寫為：

$$
\boxed{
\textbf{critical affine-defect / Zygmund endpoint},
}
$$

而不是單純 first-difference Hölder endpoint。

---

# 7. Exact centered cofactor algebra

令：

$$
S_0=S(x),
$$

$$
A_z
=
D_zS(x),
$$

$$
B_z
=
\frac12
\Delta_z^2S(x).
$$

定義 linearized cofactor map：

$$
\boxed{
L_S(H)
=
SH+HS
-
\frac23
(S:H)I.
}
\tag{7.1}
$$

以及 quadratic trace-free map：

$$
\boxed{
Q(H)
=
H^2
-
\frac13|H|^2I.
}
\tag{7.2}
$$

因：

$$
C(S)=Q(S),
$$

有 exact：

$$
\boxed{
D_zC
=
L_{S_0}(A_z)
+
A_zB_z
+
B_zA_z
-
\frac23
(A_z:B_z)I.
}
\tag{7.3}
$$

以及：

$$
\boxed{
\Delta_z^2C
=
L_{S_0}(\Delta_z^2S)
+
2Q(A_z)
+
\frac12
Q(\Delta_z^2S).
}
\tag{7.4}
$$

這是本輪第二個核心 identity。

---

# 8. What the cofactor special structure actually buys

Equation (7.4) 顯示：

$$
\Delta_z^2C
$$

不是 generic second difference。

它由：

1. strain affine-defect：
   $$
   L_S(\Delta_z^2S);
   $$

2. quadratic first-strain increment：
   $$
   2Q(D_zS);
   $$

3. quadratic second-strain increment：
   $$
   \frac12Q(\Delta_z^2S);
   $$

組成。

所以 near-affine strain：

$$
\Delta_z^2S\approx0
$$

時，

主要 cofactor curvature是：

$$
\boxed{
\Delta_z^2C
\approx
2Q(D_zS).
}
\tag{8.1}
$$

即：

$$
\boxed{
\text{cofactor curvature}
\sim
(\text{strain increment})^2.
}
$$

這是 generic tensor沒有的特殊 quadratic gain。

---

# 9. But the first centered cofactor still contains one strain increment

Equation (7.3) leading term：

$$
\boxed{
D_zC
=
L_S(D_zS)
+
\text{higher order}.
}
\tag{9.1}
$$

因此 (2.1) 第二項：

$$
\Delta_z^2u
\cdot
\nabla K_0
:
D_zC
$$

仍可攜帶：

$$
\boxed{
\text{velocity affine-defect}
\times
\text{one strain increment}.
}
$$

所以 cofactor quadraticity沒有自動把整個 commutator提升到 two-strain-increment order。

---

# 10. Piola decomposition of the cofactor

令 full velocity gradient：

$$
A
=
\nabla u.
$$

分解：

$$
\boxed{
A
=
S+\Omega,
}
\tag{10.1}
$$

其中：

$$
S^\top=S,
$$

$$
\Omega^\top=-\Omega.
$$

incompressibility：

$$
\operatorname{tr}A=0.
$$

對 general trace-free：

$$
A,
$$

cofactor公式：

$$
\boxed{
\operatorname{cof}A
=
(A^\top)^2
-
\frac12
\operatorname{tr}(A^2)I.
}
\tag{10.2}
$$

因此：

$$
\boxed{
\operatorname{cof}S
-
\operatorname{cof}A
=
S\Omega
+
\Omega S
-
\Omega^2
+
\frac12
\operatorname{tr}(\Omega^2)I.
}
\tag{10.3}
$$

---

# 11. Vorticity simplification

對：

$$
\Omega_{ij}
=
-\frac12
\varepsilon_{ijk}\omega_k,
$$

有：

$$
\boxed{
\Omega^2
=
\frac14
(
\omega\otimes\omega
-
|\omega|^2I
),
}
\tag{11.1}
$$

以及：

$$
\boxed{
\operatorname{tr}(\Omega^2)
=
-\frac12|\omega|^2.
}
\tag{11.2}
$$

所以：

$$
\boxed{
-\Omega^2
+
\frac12
\operatorname{tr}(\Omega^2)I
=
-\frac14
\omega\otimes\omega.
}
\tag{11.3}
$$

因此 trace-free cofactor：

$$
C
=
\operatorname{cof}S
+
\frac16|S|^2I
$$

可寫成：

$$
\boxed{
C
=
\operatorname{cof}\nabla u
+
S\Omega
+
\Omega S
-
\frac14
\omega\otimes\omega
+
\frac16
|S|^2I.
}
\tag{11.4}
$$

命名：

$$
\boxed{
\textbf{Piola–Vorticity Cofactor Decomposition}.
}
$$

---

# 12. Piola null-Lagrangian cancellation

classical Piola identity：

$$
\boxed{
\operatorname{div}
\operatorname{cof}\nabla u
=
0
}
\tag{12.1}
$$

for smooth maps。

此外：

$$
S\Omega+\Omega S
$$

是 skew-symmetric，

所以：

$$
\boxed{
\partial_i\partial_j
(S\Omega+\Omega S)_{ij}
=
0.
}
\tag{12.2}
$$

因此 double divergence of：

$$
C
$$

只剩：

$$
\boxed{
\partial_i\partial_jC_{ij}
=
-\frac14
\partial_i\partial_j
(
\omega_i\omega_j
)
+
\frac16
\Delta|S|^2.
}
\tag{12.3}
$$

這是 cofactor special structure最強的 exact null-Lagrangian reduction。

---

# 13. Scalar Riesz projection of the cofactor

因：

$$
C
$$

trace-free，

$$
\mathcal T_0^\ast C
=
\partial_i\partial_j
(-\Delta)^{-1}
C_{ij}.
$$

由 (12.3)：

$$
\boxed{
\mathcal T_0^\ast C
=
-\frac16
|S|^2
-
\frac14
\mathcal R_i\mathcal R_j
(
\omega_i\omega_j
).
}
\tag{13.1}
$$

其中：

$$
\mathcal R_i\mathcal R_j
=
\partial_i\partial_j(-\Delta)^{-1}.
$$

又：

$$
q
=
|S|^2-\frac12|\omega|^2,
$$

所以：

$$
\boxed{
\mathcal T_0^\ast C
=
-\frac16q
-
\frac1{12}
|\omega|^2
-
\frac14
\mathcal R_i\mathcal R_j
(
\omega_i\omega_j
).
}
\tag{13.2}
$$

命名：

$$
\boxed{
\textbf{Piola–Vorticity Projection Identity}.
}
$$

---

# 14. Irrotational branch

若：

$$
\omega=0,
$$

則：

$$
A=S=\nabla u.
$$

Piola–Vorticity Projection Identity退化為：

$$
\boxed{
\mathcal T_0^\ast C
=
-\frac16
q
=
-\frac16|S|^2.
}
\tag{14.1}
$$

所以 irrotational incompressible branch中，

cofactor的 nonlocal scalar projection其實降成 local scalar。

這是真正的 null-Lagrangian depletion。

但 full 3D NS一般具有：

$$
\omega\ne0.
$$

所以：

$$
\boxed{
\text{vorticity stress is the obstruction to exact Piola locality}.
}
\tag{14.2}
$$

---

# 15. Irrotational harmonic second-jet depletion witness

取 harmonic potential：

$$
\boxed{
\begin{aligned}
\phi(x)
={}&
-\frac12x_1^2
-\frac12x_2^2
+
x_3^2
\\
&+
x_1^3
-
3x_1x_2^2.
\end{aligned}
}
\tag{15.1}
$$

令：

$$
u=\nabla\phi.
$$

則：

$$
\nabla\cdot u
=
\Delta\phi
=
0,
$$

且：

$$
\omega=0.
$$

在：

$$
x=0,
$$

$$
S_0
=
\operatorname{diag}
(-1,-1,2).
$$

直接 spherical jet calculation顯示：

$$
\boxed{
\text{the leading centered second-jet shell coefficient of }
\mathcal A_C
\text{ vanishes}.
}
\tag{15.2}
$$

這和 Piola null-Lagrangian depletion一致。

此 witness不宣稱所有 irrotational higher jets全部 vanish。

---

# 16. Generic rotational second-jet sharpness witness

現在取 Round 35 divergence-free polynomial field：

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
\tag{16.1}
$$

則：

$$
\nabla\cdot u=0,
$$

以及：

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
\tag{16.2}
$$

於：

$$
x=0,
$$

$$
S_0
=
\operatorname{diag}
(-1,-1,2),
$$

$$
\boxed{
C_0
=
\operatorname{diag}
(-1,-1,2).
}
\tag{16.3}
$$

並：

$$
\boxed{
\partial_1C
=
\operatorname{diag}
(-2,2,0),
}
\tag{16.4}
$$

$$
\boxed{
\partial_{11}C
=
\operatorname{diag}
\left(
\frac23,
\frac23,
-\frac43
\right).
}
\tag{16.5}
$$

此 field有：

$$
\boxed{
\omega
=
(0,0,-2x_2),
}
\tag{16.6}
$$

所以：

$$
\nabla\omega\ne0.
$$

---

# 17. Exact nonzero curvature shell coefficient

採 standard Newtonian trace-free kernel：

$$
\boxed{
K_{0,ij}(z)
=
\frac{
3e_ie_j-\delta_{ij}
}{
4\pi r^3
},
\qquad
e=z/r.
}
\tag{17.1}
$$

則：

$$
\boxed{
\partial_kK_{0,ij}
=
\frac3{
4\pi r^4
}
\left[
\delta_{ki}e_j
+
\delta_{kj}e_i
+
\delta_{ij}e_k
-
5e_ie_je_k
\right].
}
\tag{17.2}
$$

將 (16.1)–(16.5) 代入 Centered Cofactor-Commutator Identity。

對 unit sphere的 cubic jet angular average精確為：

$$
\boxed{
-\frac4{15}
}
\tag{17.3}
$$

after removing the kernel normalization factor。

所以 full radial shell coefficient為：

$$
\boxed{
-\frac45
r\,dr.
}
\tag{17.4}
$$

因此：

$$
\boxed{
\mathcal A_C^{\varepsilon<|z|<\ell}(0)
=
-\frac25
\left(
\ell^2-\varepsilon^2
\right)
}
\tag{17.5}
$$

under this kernel sign convention。

最重要的不是 sign，而是：

$$
\boxed{
\mathcal A_C^{\rm second\ jet}
\ne0.
}
$$

命名：

$$
\boxed{
\textbf{Second-Jet Sharpness Witness}.
}
$$

---

# 18. No universal third-order cancellation

Sections 3–4證：

$$
\boxed{
\text{affine first jet cancels exactly}.
}
$$

但 Section 17證：

$$
\boxed{
\text{generic divergence-free rotational second jet can survive}.
}
$$

所以不存在 purely algebraic universal：

$$
\boxed{
\mathcal A_C^{<\ell}
=
O(\ell^{2+\alpha})
}
\tag{18.1}
$$

for some fixed：

$$
\alpha>0
$$

based only on：

- incompressibility；
- trace-free strain；
- cofactor structure；
- kernel parity。

也就是：

$$
\boxed{
\textbf{special cofactor buys exactly an affine-jet cancellation,
not a universal extra fractional derivative.}
}
\tag{18.2}
$$

---

# 19. Fractional endpoint remains sharp in the rotational branch

在 rough critical branch：

$$
0<s_u,s_C<1,
$$

centered second differences與 first differences仍同 order：

$$
r^{s_u},
\qquad
r^{s_C}.
$$

所以：

$$
\mathfrak Z_{u,C}
$$

仍要求：

$$
\boxed{
s_u+s_C>1
}
$$

for absolute local convergence。

critical：

$$
\boxed{
s_u+s_C=1
}
$$

仍需：

- little-Zygmund；
- Campanato affine-defect；
- Dini gain；
- 或另外的 vorticity/Piola depletion。

所以 Round 40 critical line在 generic rotational branch仍是 sharp route obstruction。

---

# 20. Piola–Vorticity commutator resolution

定義 vorticity projection defect：

$$
\boxed{
\mathfrak V_\omega
=
\frac1{12}
|\omega|^2
+
\frac14
\mathcal R_i\mathcal R_j
(
\omega_i\omega_j
).
}
\tag{20.1}
$$

由 (13.2)：

$$
\boxed{
\mathcal T_0^\ast C
=
-\frac16q
-
\mathfrak V_\omega.
}
\tag{20.2}
$$

Round 37 cofactor equation：

$$
\boxed{
D_tC-\nu\Delta C
=
-
L_S(E)
-
2\nu Q_C
+
V_C.
}
\tag{20.3}
$$

所以：

$$
\boxed{
\begin{aligned}
\mathcal A_C
&=
[D_u,\mathcal T_0^\ast]C
\\
&=
(D_u-\nu\Delta)
(
\mathcal T_0^\ast C
)
+
\mathcal T_0^\ast L_S(E)
+
2\nu
\mathcal T_0^\ast Q_C
-
\mathcal T_0^\ast V_C.
\end{aligned}
}
\tag{20.4}
$$

Round 37 pressure-source equation：

$$
\boxed{
(D_u-\nu\Delta)q
=
N_0
-
2S:E.
}
\tag{20.5}
$$

因此：

$$
\boxed{
\begin{aligned}
\mathcal A_C
={}&
-\frac16
(
N_0-2S:E
)
\\
&-
(D_u-\nu\Delta)
\mathfrak V_\omega
\\
&+
\mathcal T_0^\ast L_S(E)
+
2\nu
\mathcal T_0^\ast Q_C
-
\mathcal T_0^\ast V_C.
\end{aligned}
}
\tag{20.6}
$$

命名：

$$
\boxed{
\textbf{Piola–Vorticity Commutator Resolution}.
}
$$

---

# 21. What the Piola resolution changes

Round 40 將：

$$
\mathcal A_C
$$

視為 generic transport commutator。

Round 41 現在顯示：

$$
\boxed{
\text{its genuinely nonlocal special-cofactor defect
can be pushed into }
\mathfrak V_\omega,
}
$$

plus already-known：

- defect-linear terms；
- viscous cofactor gradients；
- vorticity forcing。

所以：

$$
\boxed{
\textbf{
the special cofactor commutator is not arbitrary:
its failure to be Piola-local is vorticity-generated.
}
}
\tag{21.1}
$$

這是本輪最重要的新 route compression。

---

# 22. Why Piola resolution still does not close the problem

$\mathfrak V_\omega$ 包含：

$$
\mathcal R_i\mathcal R_j
(
\omega_i\omega_j
).
$$

因此：

$$
(D_u-\nu\Delta)
\mathfrak V_\omega
$$

仍會產生：

- vorticity stretching；
- vorticity diffusion；
- transport–Riesz commutator of vorticity stress。

所以 nonlocality沒有消失。

但它現在不再由：

$$
\boxed{
\text{arbitrary }C
}
$$

承擔，

而是由：

$$
\boxed{
\text{vorticity stress}
}
$$

承擔。

這直接接回 Round 18、26、28 的 strain–vorticity geometry。

---

# 23. Endpoint route map after special-cofactor reduction

現在 Hardy–BMO route有三個 branches：

## B1 — generic rotational fractional branch

$$
\boxed{
s_u+s_C=1
}
$$

remains critical。

## B2 — near-affine smooth branch

Centered symmetrization gives：

$$
\boxed{
O(\ell^2)
}
$$

local commutator。

## B3 — Piola/low-vorticity branch

cofactor projection becomes approximately：

$$
\boxed{
\mathcal T_0^\ast C
\approx
-\frac16q,
}
$$

and remaining nonlocality is vorticity stress。

所以 next proof obligation naturally becomes：

$$
\boxed{
\text{control the Piola–vorticity defect rather than generic }C\text{ BMO}.
}
$$

---

# 24. STOP-C45 — Affine-Jet Cancellation / Piola–Vorticity Endpoint Gap

$$
\boxed{
\begin{aligned}
\text{layer}
&=
\mathrm{special\ cofactor\ commutator},
\\
\text{raw dual kernel}
&=
\delta u
\times
\delta C
\times
\nabla K_0,
\\
\text{centered form}
&=
D_zu\,\Delta_z^2C
+
\Delta_z^2u\,D_zC,
\\
\text{affine first jet}
&=
0,
\\
\text{smooth local order}
&=
O(\ell^2),
\\
\text{generic second jet}
&\ne
0,
\\
\text{universal third-order cancellation}
&=
\mathrm{false},
\\
\text{fractional critical line}
&=
s_u+s_C=1
\text{ remains},
\\
\text{special cofactor projection}
&=
-\frac16q
-
\mathfrak V_\omega,
\\
\text{Piola-local branch}
&=
\omega=0,
\\
\text{nonlocal defect}
&=
\mathrm{vorticity\ stress},
\\
\text{missing}
&=
\mathrm{critical\ control\ of\ Piola\text{-}vorticity\ stress
or\ little\text{-}Zygmund/Campanato\ affine\ defect},
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
\textbf{STOP-C45:
Affine-Jet Cancellation / Piola–Vorticity Endpoint Gap}.
}
$$

---

# 25. 24/72 Ledger — Round 41

| Step | object | $B$ | $U$ | $O$ | $L$ | status |
|---|---|---|---|---|---|---|
| C623 | centered first/second differences | $\mathsf C$ | continuous translation | profile | $\mathsf F$ | FORM |
| C624 | centered cofactor-commutator identity | $\mathsf C$ | parity cancellation | targeted | $\mathsf F$ | EXACT |
| C625 | affine-jet cancellation | $\mathsf C$ | local jet | targeted | $\mathsf F$ | PROVED |
| C626 | smooth $O(\ell^2)$ local order | $\mathsf C$ | Taylor / kernel | scalar | $\mathsf F$ | PROVED |
| C627 | Zygmund/Campanato endpoint | $\mathsf C$ | affine defect | profile | $\mathsf F$ | IDENTIFIED |
| C628 | exact centered cofactor algebra | $\mathsf C$ | quadratic tensor | relational | $\mathsf F$ | EXACT |
| C629 | cofactor curvature decomposition | $\mathsf C$ | strain increments | relational | $\mathsf F$ | EXACT |
| C630 | Piola–vorticity cofactor decomposition | $\mathsf C$ | null Lagrangian | relational | $\mathsf F$ | EXACT |
| C631 | Piola double-divergence reduction | $\mathsf C$ | compensated structure | scalar | $\mathsf F$ | EXACT |
| C632 | cofactor scalar projection identity | $\mathsf C$ | Riesz projection | scalar | $\mathsf F$ | EXACT |
| C633 | irrotational Piola-local branch | $\mathsf C$ | vorticity-zero | targeted | $\mathsf F$ | PROVED |
| C634 | harmonic potential depletion witness | $\mathsf C$ | local jet | targeted | $\mathsf F$ | CONSTRUCTED |
| C635 | rotational second-jet witness | $\mathsf C$ | local polynomial | targeted | $\mathsf F$ | CONSTRUCTED |
| C636 | universal third-jet gain | $\mathsf C$ | special algebra | targeted | $\mathsf F$ | REFUTED |
| C637 | Piola–vorticity commutator resolution | $\mathsf C$ | operator/PDE | relational | $\mathsf F$ | EXACT |
| C638 | generic BMO endpoint closure | $\mathsf C$ | Campanato | targeted | $\mathsf F$ | OPEN / STOP-C45 |

---

# 26. Continuous-versus-discrete status

本輪所有核心 objects：

- continuous centered translations；
- continuous second differences；
- continuous Taylor/Campanato affine defect；
- continuous cofactor tensor；
- continuous Piola/null-Lagrangian identity；
- continuous vorticity stress；
- continuous Riesz projection。

沒有：

- discrete jets；
- dyadic Zygmund shells；
- vorticity cells；
- graph null-Lagrangian representation。

即使 endpoint以 Zygmund / Campanato描述，

全部可由：

$$
r\in(0,\ell)
$$

continuous moduli表示。

因此：

$$
\boxed{
T_{\mathsf C\to\mathsf D}
=
\text{NOT YET REACHED}.
}
$$

---

# 27. Strongest results of Round 41

## R41-A — Centered Cofactor-Commutator Identity

$$
\boxed{
\mathcal A_C
=
\frac12
\int
(D_zu\cdot\nabla K_0):\Delta_z^2C
+
\frac12
\int
(\Delta_z^2u\cdot\nabla K_0):D_zC.
}
$$

## R41-B — affine first-jet cancellation

$$
\boxed{
\text{leading affine first-first interaction vanishes exactly}.
}
$$

## R41-C — special cofactor centered algebra

$$
\boxed{
\Delta_z^2C
=
L_S(\Delta_z^2S)
+
2Q(D_zS)
+
\frac12Q(\Delta_z^2S).
}
$$

## R41-D — Piola–Vorticity Projection Identity

$$
\boxed{
\mathcal T_0^\ast C
=
-\frac16q
-
\frac1{12}|\omega|^2
-
\frac14
\mathcal R_i\mathcal R_j
(
\omega_i\omega_j
).
}
$$

## R41-E — second-jet sharpness

for the explicit divergence-free rotational polynomial witness：

$$
\boxed{
\mathcal A_C^{\varepsilon<|z|<\ell}(0)
=
-\frac25
(
\ell^2-\varepsilon^2
)
}
$$

under the standard kernel sign convention。

所以 no universal higher jet cancellation。

## R41-F — special cofactor nonlocality is vorticity-generated

Piola resolution rewrites generic cofactor transport commutator as：

$$
\boxed{
\text{vorticity-stress evolution}
+
\text{already-known defect/higher-gradient terms}.
}
$$

---

# 28. Next round — Piola–Vorticity Stress Defect Dynamics

Round 41 讓下一個 target非常明確：

$$
\boxed{
\mathfrak V_\omega
=
\frac1{12}|\omega|^2
+
\frac14
\mathcal R_i\mathcal R_j
(
\omega_i\omega_j
).
}
$$

下一輪直接研究：

1. exact：
   $$
   (D_t-\nu\Delta)\mathfrak V_\omega;
   $$

2. vorticity equation：
   $$
   D_t\omega=S\omega+\nu\Delta\omega;
   $$

3. Riesz transport commutator of：
   $$
   \omega\otimes\omega;
   $$

4. incompressibility：
   $$
   \nabla\cdot\omega=0
   $$
   是否再次提供 Hardy/div–curl compensation；

5. $\mathfrak V_\omega$ 是否能用 Round 18 weighted enstrophy / alignment budget控制；

6. 若 vorticity stress的 nonlocal commutator又可被 pairing-level cancellation降階，可能進一步縮小 STOP-C45；

7. 若不能，Piola–vorticity defect就成為目前最穩定的 nonlocal obstruction core；

8. 仍使用 continuous Riesz / stress / increment representation。

---

# 29. External primary-source anchors

1. Raz Kupferman, Asaf Shachar, *A geometric perspective on the Piola identity in Riemannian settings*, arXiv:1805.12365.
   - reviews and proves the classical Euclidean Piola identity
     $$
     \operatorname{div}\operatorname{cof}\nabla f=0,
     $$
     and interprets it through null-Lagrangians.

2. André Guerra, Bogdan Raiţă, *Quasiconvexity, null Lagrangians, and Hardy space integrability under constant rank constraints*, arXiv:1909.03923.
   - null-Lagrangians and Hardy-space compensated integrability under differential constraints.

3. Elias Hess-Childs, Matthew Rosenzweig, Sylvia Serfaty, *Another look at regularity in transport-commutator estimates*, arXiv:2601.02326.
   - generic Riesz transport commutators retain delicate endpoint velocity-regularity constraints.

4. Maurizio Carbone, Michele Iovieno, Andrew D. Bragg, *Gauge symmetry and dimensionality reduction of the anisotropic pressure Hessian*, arXiv:1911.08652.
   - anisotropic pressure Hessian is a genuinely nonlocal velocity-gradient functional with strong geometric alignment structure.

本輪 Centered Cofactor-Commutator Identity、special centered cofactor algebra、Piola–Vorticity Projection Identity、second-jet sharpness witness與 Piola–Vorticity Commutator Resolution均為本文直接推導。

---

# 30. Commit state

$$
\boxed{
\begin{aligned}
\text{Route}
&=
\mathrm{Pure\ Continuous\ Special\ Cofactor/Affine\text{-}Jet\ Cancellation},
\\
\text{Essential }\mathsf C\to\mathsf D
&=
\mathrm{Not\ reached},
\\
\text{Affine first jet}
&=
\mathrm{exactly\ cancelled},
\\
\text{Smooth local commutator}
&=
O(\ell^2),
\\
\text{Generic second jet}
&=
\mathrm{nonzero},
\\
\text{Universal extra fractional gain}
&=
\mathrm{false},
\\
\text{Cofactor null structure}
&=
\mathrm{Piola},
\\
\text{Piola defect}
&=
\mathrm{vorticity\ stress},
\\
\text{Critical endpoint}
&=
\mathrm{Zygmund/Campanato\ or\ vorticity\text{-}stress\ control},
\\
\text{STOP-C45}
&=
\mathrm{Affine\text{-}Jet\ Cancellation/Piola\text{-}Vorticity\ Endpoint\ Gap},
\\
\text{Next}
&=
\mathrm{Piola\text{-}Vorticity\ Stress\ Defect\ Dynamics}.
\end{aligned}
}
$$
