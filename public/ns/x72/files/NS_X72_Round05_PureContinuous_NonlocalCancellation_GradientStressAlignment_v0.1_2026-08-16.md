# NS × X 積分 × 24/72 範式實戰
## Round 05 — Pure Continuous Nonlocal Cancellation / Gradient-Stress Alignment Route

- 日期：2026-08-16
- 版本：v0.1
- 狀態：Proof-Route Experiment / Continuous-Only Projection–Cancellation Branch
- canonical source：UTF-8 Markdown
- canonical math delimiters：inline `$...$`；display `$$...$$`
- 前一輪：`NS_X72_Round04_PureContinuous_GeometryEvolution_PressureConstraint_v0.1_2026-08-16.md`
- 本輪目標：反轉 Round 04 的順序。先利用 incompressibility、strain projection 與全域正交性消去 pressure / null channels，再檢查是否仍可保留足夠的幾何資訊形成 exact coercive carrier。
- 非主張：本文若得到新的等式或條件式判準，只聲稱本文中的直接推導；不聲稱其學術新穎性，除非另有獨立文獻稽核。

---

# 0. Round 04 handoff

Round 04 顯示 local strain spectrum 的 exact evolution需要：

$$
H_p
=
\nabla^2p
=
\nabla^2(-\Delta)^{-1}
\left(
|S|^2-\frac12|\omega|^2
\right).
$$

因此 finite local differential state：

$$
J^k(S,\omega)
$$

不能精確重建 anisotropic pressure Hessian。

得到：

$$
\boxed{
\text{STOP-C07}
=
\text{Local-Geometry / Nonlocal-Pressure Closure Gap}.
}
$$

同時 global pairing 中：

$$
\int S:H_p\,dx
=
0,
$$

但：

$$
e_2^\top H_pe_2
$$

仍保留於 local eigenvalue evolution。

得到：

$$
\boxed{
\text{STOP-C08}
=
\text{Global-Cancellation / Local-Feedback Gap}.
}
$$

本輪因此不再要求 pointwise eigenvalue closure。

改問：

$$
\boxed{
\text{若先做 global projection/cancellation，
能否重新構造一個恰好保存 H¹ strain growth 的 relational carrier？}
}
$$

---

# 1. Strain equation in projected form

考慮 smooth rapidly decaying incompressible Navier–Stokes：

$$
\partial_tu
+
(u\cdot\nabla)u
+
\nabla p
=
\nu\Delta u,
$$

$$
\nabla\cdot u=0.
$$

令：

$$
S
=
\nabla_{\rm sym}u,
$$

$$
\omega
=
\nabla\times u.
$$

使用 strain-space orthogonal projection：

$$
P_{st}.
$$

可將 strain equation 寫成：

$$
\boxed{
\partial_tS
-
\nu\Delta S
-
\frac12
P_{st}(\omega\otimes\omega)
+
\mathcal R
=
0,
}
\tag{1.1}
$$

其中定義 full NS residual：

$$
\boxed{
\mathcal R
=
P_{st}
\left(
(u\cdot\nabla)S
+
S^2
+
\frac34
\omega\otimes\omega
\right).
}
\tag{1.2}
$$

這個 decomposition 的用途不是 model replacement。

它保留完整 NS strain dynamics。

---

# 2. The key strain–vorticity orthogonality

對足夠光滑的 strain field，有 exact identity：

$$
\boxed{
\left\langle
-\Delta S,
\omega\otimes\omega
\right\rangle
=
0.
}
\tag{2.1}
$$

此外：

$$
-\Delta S
$$

仍屬 strain constraint space，因此對任意 admissible tensor $F$：

$$
\boxed{
\left\langle
P_{st}F,
-\Delta S
\right\rangle
=
\left\langle
F,
-\Delta S
\right\rangle.
}
\tag{2.2}
$$

令：

$$
B
=
-\Delta S.
$$

與 (1.1) 做 $L^2$ pairing。

得到：

$$
\boxed{
\frac12
\frac d{dt}
\|S\|_{\dot H^1}^2
+
\nu
\|B\|_2^2
=
-
\langle
\mathcal R,B
\rangle.
}
\tag{2.3}
$$

這就是 full NS 的 exact strain-$\dot H^1$ balance。

---

# 3. Pressure has disappeared without deleting the full NS dynamics

注意 (2.3) 不含：

$$
H_p.
$$

這不是忽略 pressure。

而是：

1. pressure Hessian 位於 strain-space 的 orthogonal null direction；
2. $P_{st}$ 將 full strain dynamics投影到 compatible strain subspace；
3. 對 growth observable：

$$
\|S\|_{\dot H^1}^2,
$$

該 projection 保留 exact pairing。

因此 Round 04 的：

$$
\boxed{
\text{Local-C}
\to
\text{Global/Nonlocal-C}
}
$$

並非死路。

至少對：

$$
\dot H^1
$$

strain growth，global projection 可以合法消去 pressure。

---

# 4. Amplitude–alignment decomposition

令：

$$
D(t)
=
\|B(t)\|_2.
$$

在：

$$
D(t)>0
$$

時定義 residual amplitude ratio：

$$
\boxed{
\chi_\nu(t)
=
\frac{
\|\mathcal R(t)\|_2
}{
\nu D(t)
}.
}
\tag{4.1}
$$

若：

$$
\mathcal R(t)\neq0,
$$

再定義 dangerous alignment cosine：

$$
\boxed{
c(t)
=
-
\frac{
\langle\mathcal R,B\rangle
}{
\|\mathcal R\|_2D
}.
}
\tag{4.2}
$$

故：

$$
-1\le c(t)\le1.
$$

定義 exact growth coefficient：

$$
\boxed{
\alpha_\nu(t)
=
\chi_\nu(t)c(t)
=
-
\frac{
\langle\mathcal R,B\rangle
}{
\nu D^2
}.
}
\tag{4.3}
$$

若：

$$
D=0,
$$

則在 finite-energy whole-space class 中已進入 spatially affine / trivial branch；以下只討論 $D>0$。

代入 (2.3)：

$$
\boxed{
\frac12
\frac d{dt}
\|S\|_{\dot H^1}^2
+
\nu
\left(
1-\alpha_\nu(t)
\right)
D(t)^2
=
0.
}
\tag{4.4}
$$

這是一個 exact scalar reduction。

---

# 5. Interpretation of $\alpha_\nu$

若：

$$
\alpha_\nu<1,
$$

則當下：

$$
\frac d{dt}
\|S\|_{\dot H^1}^2<0.
$$

若：

$$
\alpha_\nu=1,
$$

則：

$$
\frac d{dt}
\|S\|_{\dot H^1}^2=0.
$$

若：

$$
\alpha_\nu>1,
$$

則：

$$
\frac d{dt}
\|S\|_{\dot H^1}^2>0.
$$

所以：

$$
\boxed{
\alpha_\nu
}
$$

不是普通 norm amplitude。

它是：

$$
\boxed{
\text{nonlinearity amplitude}
\times
\text{dangerous alignment}.
}
$$

因此 Round 03 的結論：

$$
\text{amplitude-only observation is insufficient}
$$

在這裡得到更精確的 replacement：

$$
\boxed{
\text{growth is controlled by amplitude–alignment product, not amplitude alone}.
}
\tag{5.1}
$$

---

# 6. Exact logarithmic growth integral

定義：

$$
A(t)
=
\|S(t)\|_{\dot H^1}^2.
$$

對非平凡 whole-space solution，若：

$$
A(t)>0,
$$

由 (4.4)：

$$
\boxed{
A'
=
2\nu
(\alpha_\nu-1)
D^2.
}
\tag{6.1}
$$

因此：

$$
\boxed{
\frac d{dt}\log A
=
2\nu
(\alpha_\nu-1)
\frac{D^2}{A}.
}
\tag{6.2}
$$

積分：

$$
\boxed{
A(T)
=
A(0)
\exp
\left[
2\nu
\int_0^T
(\alpha_\nu(t)-1)
\frac{D(t)^2}{A(t)}
\,dt
\right].
}
\tag{6.3}
$$

定義 continuous growth integral：

$$
\boxed{
\mathfrak G(T)
=
\int_0^T
(\alpha_\nu(t)-1)
\frac{
\|-\Delta S(t)\|_2^2
}{
\|S(t)\|_{\dot H^1}^2
}
\,dt.
}
\tag{6.4}
$$

則：

$$
\boxed{
\|S(T)\|_{\dot H^1}^2
=
\|S(0)\|_{\dot H^1}^2
e^{2\nu\mathfrak G(T)}.
}
\tag{6.5}
$$

所以在本 smooth strong-solution class 中：

$$
\boxed{
\mathfrak G(T)
}
$$

是 strain-$\dot H^1$ growth 的 exact continuous accumulator。

---

# 7. Necessary growth condition for finite-time singularity

若 maximal strong solution 在：

$$
T_\ast<\infty
$$

失去 regularity，且 continuation theory要求：

$$
\|S(t)\|_{\dot H^1}
\to\infty
$$

沿 approaching times，則由 (6.5) 必有：

$$
\boxed{
\mathfrak G(T)
\to+\infty
\qquad
(T\uparrow T_\ast).
}
\tag{7.1}
$$

一個較保守的 sufficient regularity condition 是：

$$
\boxed{
\int_0^{T_\ast}
(\alpha_\nu-1)_+
\frac{D^2}{A}
\,dt
<
\infty.
}
\tag{7.2}
$$

因為：

$$
\mathfrak G(T)
\le
\int_0^T
(\alpha_\nu-1)_+
\frac{D^2}{A}
\,dt.
$$

所以該 positive danger integral 有界時：

$$
A(T)
$$

保持有界。

這仍是 conditional criterion，不是 unconditional NS estimate。

---

# 8. Recovering the MORP / model-cone threshold

由 Cauchy–Schwarz：

$$
c(t)\le1.
$$

所以：

$$
\boxed{
\alpha_\nu(t)
\le
\chi_\nu(t).
}
\tag{8.1}
$$

因此若：

$$
\boxed{
\chi_\nu(t)\le1
}
\tag{8.2}
$$

於一段時間成立，則：

$$
\alpha_\nu(t)\le1
$$

且：

$$
\boxed{
\|S(t)\|_{\dot H^1}
\text{ is nonincreasing}.
}
\tag{8.3}
$$

這恢復 Miller-type model-cone regularity geometry。

但 (4.3) 顯示真正控制 growth 的是：

$$
\alpha_\nu,
$$

而：

$$
\chi_\nu
$$

只是 Cauchy upper envelope。

因此：

$$
\boxed{
\text{amplitude ratio } \chi_\nu
}
$$

不是最小 growth carrier。

更尖的是：

$$
\boxed{
\alpha_\nu
=
\chi_\nu c.
}
$$

---

# 9. Equality rigidity inside the closed cone

假設在 interval：

$$
[a,b]
$$

上：

$$
\chi_\nu\le1
$$

a.e.，且：

$$
\|S(b)\|_{\dot H^1}
=
\|S(a)\|_{\dot H^1}.
$$

由 (4.4)：

$$
0
=
\int_a^b
\nu(1-\alpha_\nu)D^2dt.
$$

因：

$$
\alpha_\nu
\le
\chi_\nu
\le1,
$$

得到在：

$$
D>0
$$

處：

$$
\boxed{
\alpha_\nu=1.
}
$$

因此：

$$
\boxed{
\chi_\nu=1,
\qquad
c=1.
}
\tag{9.1}
$$

Cauchy equality 逼迫：

$$
\boxed{
\mathcal R
=
-\nu B
=
\nu\Delta S.
}
\tag{9.2}
$$

也就是 general-viscosity model-cone equality。

代回 (1.1)：

$$
\partial_tS
-
\nu\Delta S
-
\frac12P_{st}(\omega\otimes\omega)
+
\nu\Delta S
=
0,
$$

故：

$$
\boxed{
\partial_tS
=
\frac12
P_{st}(\omega\otimes\omega).
}
\tag{9.3}
$$

---

# 10. Equality-collapse theorem

對 (9.3) 與 $S$ pairing：

$$
\frac12
\frac d{dt}
\|S\|_2^2
=
\frac12
\langle
S,\omega\otimes\omega
\rangle.
$$

使用 exact identity：

$$
\boxed{
\langle
S,\omega\otimes\omega
\rangle
=
-4
\int\det S\,dx,
}
\tag{10.1}
$$

得到：

$$
\boxed{
\frac d{dt}
\|S\|_2^2
=
-4
\int\det S\,dx.
}
\tag{10.2}
$$

但 full Navier–Stokes 同時滿足：

$$
\boxed{
\frac d{dt}
\|S\|_2^2
=
-2\nu
\|S\|_{\dot H^1}^2
-
4
\int\det S\,dx.
}
\tag{10.3}
$$

比較 (10.2) 與 (10.3)：

$$
\boxed{
\|S\|_{\dot H^1}=0.
}
\tag{10.4}
$$

因此 $S$ spatially constant。

在：

$$
S\in L^2(\mathbb R^3)
$$

class：

$$
\boxed{
S\equiv0.
}
\tag{10.5}
$$

所以：

$$
\boxed{
\textbf{
a nontrivial finite-energy Navier–Stokes state cannot execute
an exact equal-$\dot H^1$ return inside }\chi_\nu\le1.
}
}
\tag{10.6}
$$

這重新連接前面 MORP/DCRP 的 model-cone equality collapse，但本輪直接由 Pure-C projection/cancellation route 得到。

---

# 11. Strict Lyapunov corollary

對 nontrivial finite-energy whole-space solution，如果：

$$
\chi_\nu(t)\le1
$$

於 interval：

$$
[a,b],
$$

則：

$$
\|S(t)\|_{\dot H^1}
$$

不能在非零 interval 上先不增後精確返回原值。

否則 Section 9–10 逼迫：

$$
S\equiv0.
$$

因此在 closed cone 中：

$$
\boxed{
\|S\|_{\dot H^1}^2
}
$$

是 nontrivial branch 的 strict Lyapunov quantity in the endpoint-return sense。

---

# 12. Remove the explicit vorticity tensor from the H¹ growth driver

由 (1.2)：

$$
\mathcal R
=
P_{st}
\left(
(u\cdot\nabla)S
+
S^2
+
\frac34
\omega\otimes\omega
\right).
$$

由：

$$
B\in L^2_{st},
$$

projection 可從 pairing 移除：

$$
\langle\mathcal R,B\rangle
=
\left\langle
(u\cdot\nabla)S
+
S^2
+
\frac34\omega\otimes\omega,
B
\right\rangle.
$$

再由：

$$
\langle
\omega\otimes\omega,
B
\rangle
=
0,
$$

得到：

$$
\boxed{
\langle\mathcal R,B\rangle
=
\left\langle
(u\cdot\nabla)S
+
S^2,
B
\right\rangle.
}
\tag{12.1}
$$

所以 full NS strain-$\dot H^1$ growth 的 exact dangerous projection只依賴：

$$
\boxed{
(u\cdot\nabla)S
+
S^2
}
$$

在：

$$
-\Delta S
$$

方向上的分量。

pressure 與 explicit $\omega\otimes\omega$ 均已從該 growth observable 中精確消失。

---

# 13. Localize the advection pairing without discrete decomposition

考慮：

$$
I_{\rm adv}
=
\left\langle
(u\cdot\nabla)S,
-\Delta S
\right\rangle.
$$

寫 component：

$$
I_{\rm adv}
=
\int
u_j
\partial_jS_{ab}
(-\partial_{kk}S_{ab})
\,dx.
$$

對 $x_k$ integration by parts：

$$
I_{\rm adv}
=
\int
\partial_k u_j
\,
\partial_jS_{ab}
\,
\partial_kS_{ab}
\,dx
+
\frac12
\int
u_j
\partial_j
|\partial_kS|^2
\,dx.
$$

第二項由：

$$
\nabla\cdot u=0
$$

消失。

定義 Gram tensor：

$$
\boxed{
M_{jk}
=
\partial_jS:\partial_kS.
}
\tag{13.1}
$$

則：

$$
M^\top=M,
$$

且對任意：

$$
v\in\mathbb R^3,
$$

$$
v^\top Mv
=
\left|
\sum_jv_j\partial_jS
\right|^2
\ge0.
$$

所以：

$$
\boxed{
M\succeq0.
}
\tag{13.2}
$$

又：

$$
\partial_ku_j
=
S_{jk}
+
\Omega_{jk}.
$$

因：

$$
M
$$

symmetric，

$$
\Omega:M=0.
$$

因此：

$$
\boxed{
I_{\rm adv}
=
\int
S:M
\,dx.
}
\tag{13.3}
$$

這是一個完全 local continuous identity。

---

# 14. Localize the strain self-amplification pairing

令：

$$
H_k
=
\partial_kS.
$$

因 $S$ symmetric：

$$
H_k^\top=H_k.
$$

考慮：

$$
I_{\rm self}
=
\langle
S^2,
-\Delta S
\rangle.
$$

integration by parts：

$$
I_{\rm self}
=
\sum_k
\int
\partial_k(S^2):\partial_kS
\,dx.
$$

而：

$$
\partial_k(S^2)
=
H_kS
+
SH_k.
$$

因此：

$$
\partial_k(S^2):H_k
=
2
\operatorname{tr}
(SH_k^2).
$$

故：

$$
\boxed{
I_{\rm self}
=
2
\int
S:
\left(
\sum_kH_k^2
\right)
dx.
}
\tag{14.1}
$$

每個：

$$
H_k^2
$$

均 positive semidefinite。

---

# 15. NEW exact carrier — gradient-stress tensor

定義：

$$
\boxed{
G[S]
=
M
+
2
\sum_{k=1}^3
H_k^2.
}
\tag{15.1}
$$

由 Sections 13–14：

$$
M\succeq0,
$$

且：

$$
H_k^2\succeq0.
$$

故：

$$
\boxed{
G[S]\succeq0.
}
\tag{15.2}
$$

此外：

$$
\operatorname{tr}M
=
|\nabla S|^2,
$$

以及：

$$
\operatorname{tr}
\left(
\sum_kH_k^2
\right)
=
|\nabla S|^2.
$$

所以：

$$
\boxed{
\operatorname{tr}G
=
3|\nabla S|^2.
}
\tag{15.3}
$$

由 (12.1)、(13.3)、(14.1)：

$$
\boxed{
\langle
\mathcal R,B
\rangle
=
\int
S:G[S]
\,dx.
}
\tag{15.4}
$$

代回 exact H¹ balance：

$$
\boxed{
\frac12
\frac d{dt}
\|S\|_{\dot H^1}^2
+
\nu
\|-\Delta S\|_2^2
=
-
\int
S:G[S]
\,dx.
}
\tag{15.5}
$$

這是本輪最重要的 exact identity。

---

# 16. Gradient-weighted strain scalar

在：

$$
|\nabla S|>0
$$

處，定義 normalized gradient-stress state：

$$
\boxed{
W
=
\frac{
G[S]
}{
\operatorname{tr}G[S]
}.
}
\tag{16.1}
$$

則：

$$
W\succeq0,
$$

$$
\operatorname{tr}W=1.
$$

定義：

$$
\boxed{
\Lambda_G
=
-
S:W.
}
\tag{16.2}
$$

若：

$$
|\nabla S|=0,
$$

令：

$$
\Lambda_G=0.
$$

由：

$$
G=3|\nabla S|^2W,
$$

得到：

$$
\boxed{
-
S:G
=
3
\Lambda_G
|\nabla S|^2.
}
\tag{16.3}
$$

所以 (15.5) 變成：

$$
\boxed{
\frac12
\frac d{dt}
\|S\|_{\dot H^1}^2
+
\nu
\|-\Delta S\|_2^2
=
3
\int
\Lambda_G
|\nabla S|^2
\,dx.
}
\tag{16.4}
$$

這把 full NS 的 strain-$\dot H^1$ nonlinear growth重新表示成：

$$
\boxed{
\text{gradient energy}
\times
\text{gradient-weighted strain geometry}.
}
$$

---

# 17. Spectral meaning of $\Lambda_G$

在 $S$ 的 eigenbasis：

$$
Se_i
=
\lambda_ie_i,
$$

定義：

$$
w_i
=
e_i^\top We_i.
$$

因：

$$
W\succeq0,
$$

$$
\operatorname{tr}W=1,
$$

有：

$$
w_i\ge0,
$$

$$
w_1+w_2+w_3=1.
$$

因此：

$$
\boxed{
\Lambda_G
=
-
\sum_{i=1}^3
w_i\lambda_i.
}
\tag{17.1}
$$

所以：

$$
\boxed{
-\lambda_3
\le
\Lambda_G
\le
-\lambda_1.
}
\tag{17.2}
$$

Dangerous positive：

$$
\Lambda_G>0
$$

表示 gradient-stress tensor：

$$
W
$$

在平均意義上更偏向 strain 的 compressive eigendirections。

Regularizing negative：

$$
\Lambda_G<0
$$

表示 gradient stress 更偏向 extensional eigendirections。

因此本輪得到一個新的 geometric interpretation：

$$
\boxed{
\textbf{
H¹ strain growth is driven by alignment of strain-gradient stress
with compressive strain directions.
}
}
\tag{17.3}
$$

---

# 18. Exact relation between $\alpha_\nu$ and $\Lambda_G$

由 (4.3) 與 (15.4)：

$$
\alpha_\nu
=
-
\frac{
\int S:G\,dx
}{
\nu
\|-\Delta S\|_2^2
}.
$$

再用 (16.3)：

$$
\boxed{
\alpha_\nu(t)
=
\frac{
3
\int
\Lambda_G
|\nabla S|^2dx
}{
\nu
\|-\Delta S\|_2^2
}.
}
\tag{18.1}
$$

所以 residual amplitude/alignment scalar：

$$
\alpha_\nu
$$

具有一個完全 local continuous integral representation。

這表示：

> global projection 並沒有把 H¹ growth 所需的 relational geometry 永久抹掉。

相反地：

$$
\boxed{
\text{projection/cancellation}
\longrightarrow
\text{new local relational carrier } \Lambda_G.
}
\tag{18.2}
$$

---

# 19. X-integral observation resolution cycle

Round 03 在：

$$
\Gamma_{\rm amp}
$$

中證明：

$$
\boxed{
\mathsf X_{\Gamma_{\rm amp}}
}
$$

因為單一 amplitude：

$$
|S|
$$

不能保存 nonlinear sign。

但本輪先做：

$$
\int_{\rm projection}
\int_{\rm cancellation}
\int_{\rm gradient\ relation}
X_{\rm geom},
$$

再觀察：

$$
\Lambda_G
$$

及：

$$
\alpha_\nu.
$$

對 target observable：

$$
\frac d{dt}
\|S\|_{\dot H^1}^2,
$$

單一 scalar：

$$
\boxed{
\alpha_\nu
}
$$

已是 sufficient。

因此 24 observation state 可以發生：

$$
\boxed{
\mathsf C_{\rm amplitude}
\to
\mathsf X_{\Gamma_{\rm amp}}
\to
\mathsf C_{\rm growth}
}
\tag{19.1}
$$

但前後兩個：

$$
\mathsf C
$$

不是同一 observation。

第一個只讀 amplitude。

第二個是在 X 積分更多 relational structure 之後才形成的 targeted sufficient scalar。

這正好展示：

$$
\boxed{
\textbf{
Refusal of a single measure can be resolved by structural integration
before re-observation.
}
}
\tag{19.2}
$$

---

# 20. Critical smallness criterion for the new carrier

由：

$$
\Lambda_G
\le
(-\lambda_1)^+
$$

以及 (16.4)：

$$
\frac12A'
+
\nu D^2
\le
3
\int
\Lambda_G^+
|\nabla S|^2dx.
$$

Hölder：

$$
\int
\Lambda_G^+
|\nabla S|^2
\le
\|\Lambda_G^+\|_{L^{3/2}}
\|\nabla S\|_{L^6}^2.
$$

Sobolev：

$$
\|\nabla S\|_{L^6}
\le
C
\|\Delta S\|_2.
$$

故：

$$
\boxed{
\frac12A'
+
\left(
\nu
-
C
\|\Lambda_G^+\|_{L^{3/2}}
\right)
D^2
\le0.
}
\tag{20.1}
$$

因此若：

$$
\boxed{
\sup_{t<T}
\|\Lambda_G^+(t)\|_{L^{3/2}}
<
\frac{\nu}{C},
}
\tag{20.2}
$$

則：

$$
A(t)
$$

nonincreasing。

$L^{3/2}$ 是 strain 的 scale-critical Lebesgue exponent，因：

$$
S_\lambda(x,t)
=
\lambda^2
S(\lambda x,\lambda^2t)
$$

而：

$$
\|S_\lambda\|_{L^{3/2}}
=
\|S\|_{L^{3/2}}.
$$

因此 (20.2) 是 critical geometric smallness condition。

本文不主張此 criterion 在文獻上新穎；它只是由新 carrier representation 的直接結果。

---

# 21. What has actually been eliminated

Round 04 的主要 suspicion：

> pressure Hessian 可能是純連續 geometry route 的不可消除 obstruction。

Round 05 顯示，對：

$$
\boxed{
\dot H^1\text{ strain growth}
}
$$

這個 specific target，該 suspicion 是錯的。

pressure 可以被 exact projection/cancellation 移除。

explicit：

$$
\omega\otimes\omega
$$

也由 orthogonality 移除。

因此：

$$
\boxed{
\text{STOP-C07}
}
$$

不是 H¹ growth route 的最終 barrier。

它仍對 pointwise spectrum evolution 成立，但可被另一個 continuous X route 繞過。

這就是本實驗要求的：

$$
\boxed{
\text{一條路不通}
\neq
\text{同一 substrate 下所有路不通}.
}
$$

---

# 22. New STOP — gradient-alignment coercivity

即使有 exact identity：

$$
\frac12A'
+
\nu D^2
=
3
\int
\Lambda_G
|\nabla S|^2,
$$

目前仍沒有從 standard NS constraints 無條件推出：

$$
3
\int
\Lambda_G
|\nabla S|^2
\le
\nu D^2.
$$

亦即尚未證：

$$
\boxed{
\alpha_\nu\le1.
}
$$

對所有 smooth NS states 成立。

而若：

$$
\|\Lambda_G^+\|_{3/2}
$$

只得到 finite-but-large control，smallness absorption 再次失效。

因此本輪的新主要 STOP：

$$
\boxed{
\textbf{STOP-C09:
Gradient-Stress / Compressive-Alignment Coercivity Gap}.
}
\tag{22.1}
$$

它比 STOP-C07 更尖：

不是 pressure 本身，

不是單一 amplitude，

不是 local eigenvalue。

而是：

$$
\boxed{
\text{strain gradients 對 compressive eigendirections 的 weighted alignment
能否被 NS dynamics 無條件限制？}
}
$$

---

# 23. No essential discrete intrusion yet

本輪所有物件：

$$
P_{st},
$$

$$
S,
$$

$$
\omega,
$$

$$
-\Delta S,
$$

$$
M,
$$

$$
G,
$$

$$
W,
$$

$$
\Lambda_G,
$$

$$
\alpha_\nu,
$$

$$
\mathfrak G(T)
$$

都可在 continuous deterministic framework 中定義。

因此：

$$
\boxed{
T_{\mathsf C\to\mathsf D}
=
\text{NOT YET REACHED}.
}
\tag{23.1}
$$

反而 Pure-C 路線目前已走過：

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
\mathsf C_{\rm gradient\ geometry}.
\end{aligned}
}
\tag{23.2}
$$

---

# 24. 24/72 Ledger — Round 05

| Step | X object / operation | $B$ | $U$ | $O$ | $L$ | status |
|---|---|---|---|---|---|---|
| C41 | $P_{st}$ full strain equation | $\mathsf C$ | $\mathsf P$ constraint | $\mathsf X$ | $\mathsf F$ | FORM |
| C42 | $\langle-\Delta S,\omega\otimes\omega\rangle=0$ | $\mathsf C$ | projection | targeted | $\mathsf F$ | EXACT |
| C43 | H¹ strain balance | $\mathsf C$ | $\mathsf S/\mathsf P$ | targeted | $\mathsf F$ | EXACT |
| C44 | residual amplitude $\chi_\nu$ | $\mathsf C$ | $\mathsf R$ meta-observation | scalar | $\mathsf F$ | FORM |
| C45 | dangerous alignment $c$ | $\mathsf C$ | relational | scalar | $\mathsf F$ | FORM |
| C46 | $\alpha_\nu=\chi_\nu c$ | $\mathsf C$ | relational | scalar sufficient for H¹ growth | $\mathsf F$ | EXACT |
| C47 | model-cone equality collapse | $\mathsf C$ | recurrent/equality | scalar + relation | $\mathsf F$ | CLOSED branch |
| C48 | advection localization $I_{\rm adv}=S:M$ | $\mathsf C$ | $\mathsf S$ | relational | $\mathsf F$ | EXACT |
| C49 | self-interaction localization | $\mathsf C$ | $\mathsf S$ | relational | $\mathsf F$ | EXACT |
| C50 | gradient-stress tensor $G$ | $\mathsf C$ | $\mathsf P$ local relation | $\mathsf X$ | $\mathsf F$ | FORM |
| C51 | normalized $W$ and $\Lambda_G$ | $\mathsf C$ | relational | targeted scalar | $\mathsf F$ | FORM |
| C52 | exact gradient-alignment law | $\mathsf C$ | hybrid | targeted scalar | $\mathsf F$ | EXACT |
| C53 | unconditional $\alpha_\nu\le1$ | $\mathsf C$ | — | targeted scalar | $\mathsf F$ | OPEN / STOP-C09 |

---

# 25. X diagnostic object

$$
\boxed{
\bot_X^{\mathrm{C09}}
=
\left\langle
\begin{array}{l}
\text{layer}
=
\mathrm{H^1\ strain\ geometric\ coercivity},
\\
\text{exact\ driver}
=
3\int\Lambda_G|\nabla S|^2,
\\
\text{dissipation}
=
\nu\|\Delta S\|_2^2,
\\
\text{required}
=
\alpha_\nu\le1
\text{ or integrable positive excess},
\\
\text{pressure}
=
\mathrm{eliminated},
\\
\text{explicit vorticity tensor}
=
\mathrm{eliminated},
\\
\text{remaining obstruction}
=
\mathrm{compressive\ gradient\ alignment},
\\
\text{discrete intrusion}
=
\mathrm{false}.
\end{array}
\right\rangle.
}
$$

---

# 26. Strongest result of Round 05

The strongest exact identity is:

$$
\boxed{
\frac12
\frac d{dt}
\|S\|_{\dot H^1}^2
+
\nu
\|-\Delta S\|_2^2
=
3
\int
\Lambda_G
|\nabla S|^2dx,
}
\tag{26.1}
$$

where：

$$
G
=
M
+
2
\sum_k(\partial_kS)^2
\succeq0,
$$

$$
M_{jk}
=
\partial_jS:\partial_kS,
$$

$$
W
=
\frac{G}{\operatorname{tr}G},
$$

$$
\Lambda_G
=
-S:W.
$$

Equivalently：

$$
\boxed{
\alpha_\nu
=
\frac{
3\int
\Lambda_G|\nabla S|^2dx
}{
\nu\|-\Delta S\|_2^2
}.
}
\tag{26.2}
$$

Thus the Pure-C proof frontier is now:

$$
\boxed{
\textbf{
Can Navier–Stokes dynamics prevent
gradient stress from becoming too strongly aligned
with compressive strain directions?
}
}
\tag{26.3}
$$

---

# 27. Next round — Dynamics of $\Lambda_G$ / $\alpha_\nu$

下一輪不再重新回 pressure。

直接攻新 carrier：

$$
\boxed{
\Lambda_G
}
$$

及：

$$
\boxed{
\alpha_\nu.
}
$$

需要判定：

1. $\Lambda_G$ 的 material evolution 是否存在 restoring term；
2. $W$ 的 evolution 是否具有 positivity / trace-one 結構可利用；
3. diffusion 是否迫使 gradient-stress orientation 混合；
4. $\alpha_\nu>1$ 是否能長時間維持；
5. 若微分 $\alpha_\nu$ 必須加入：

$$
\nabla^mS
$$

的無限 hierarchy，是否形成第一個真正的 continuous-infinite closure obstruction；
6. 若控制 hierarchy 必須改用 dyadic / countable scale extraction，才正式記錄：

$$
T_{\mathsf C\to\mathsf D}.
$$

---

# 28. External primary-source anchors

1. Evan Miller, *On the interaction of strain and vorticity for solutions of the Navier--Stokes equation*, arXiv:2407.02691.
   - projected strain equation；
   - identity
   $$
   \langle-\Delta S,\omega\otimes\omega\rangle=0;
   $$
   - strain-vorticity interaction model；
   - residual/model-cone regularity ratios。

2. Evan Miller, *A regularity criterion for the Navier-Stokes equation involving only the middle eigenvalue of the strain tensor*, arXiv:1710.05569.
   - strain equation；
   - exact enstrophy identity；
   - scale-critical middle-eigenvalue criterion。

3. Borys Álvarez-Samaniego, Wilson P. Álvarez-Samaniego, Pedro G. Fernández-Dalgo, *On the use of the Riesz transforms to determine the pressure term in the incompressible Navier-Stokes equations on the whole space*, arXiv:2004.02588.
   - whole-space pressure reconstruction by Riesz transforms。

---

# 29. Commit state

$$
\boxed{
\begin{aligned}
\text{Route}
&:
\mathrm{Pure\ Continuous\ Nonlocal\ Cancellation},
\\
\text{Essential } \mathsf C\to\mathsf D
&:
\mathrm{Not\ reached},
\\
\text{Pressure obstruction at H¹ growth}
&:
\mathrm{removed},
\\
\text{Explicit }\omega\otimes\omega\text{ obstruction}
&:
\mathrm{removed\ from\ H^1\ growth},
\\
\text{New exact scalar}
&:
\alpha_\nu,
\\
\text{New local relational carrier}
&:
\Lambda_G,
\\
\text{Model-cone equality branch}
&:
\mathrm{collapses\ to\ triviality},
\\
\text{STOP-C09}
&:
\mathrm{Gradient\text{-}Stress/Compressive\text{-}Alignment\ Coercivity},
\\
\text{Next}
&:
\mathrm{Dynamics\ of\ }\Lambda_G\mathrm{\ and\ }\alpha_\nu.
\end{aligned}
}
$$
