# NS × X 積分 × 24/72 範式實戰
## Round 01 — Pure Continuous Energy-First Route

- 日期：2026-08-16
- 版本：v0.1
- 狀態：Proof-Route Experiment / Continuous-Only Branch
- canonical source：UTF-8 Markdown
- canonical math delimiters：inline `$...$`；display `$$...$$`
- 本輪目標：在禁止本質離散工具的條件下，從三維不可壓縮 Navier–Stokes 原方程沿純連續 X 積分鏈向正則性推進，直到第一個嚴格可定位的 STOP / TRANSITION / ILLEGAL 節點。
- 非主張：本輪不宣稱已排除所有純連續證明；只判定本輪「energy-first continuous closure」能走到哪裡。

---

# 0. 實驗規則

本輪設定 proof-route constraint：

$$
\boxed{
B_k=\mathsf C
\qquad
\text{for every admitted step }k.
}
$$

禁止把下列物件當作必要證明工具：

- dyadic shell index；
- Galerkin mode index；
- discrete time step；
- finite partition 作為不可消除的核心步驟；
- subsequence 作為 closure 的必要核心；
- profile number；
- tree / forest index；
- scale sequence $r_n$；
- countable induction 作為本輪的主要結構。

允許：

- 連續時間 $t$；
- 連續空間 $x$；
- 連續尺度 $r>0$；
- PDE / distribution；
- Lebesgue / Sobolev / Lorentz 類連續函數空間；
- 積分恆等式；
- 微分不等式；
- 連續縮放；
- 連續參數插值；
- 連續局部化；
- 連續型 compactness statement，但若其證明或使用必須依賴 subsequence 才能形成下一步，必須標記離散入侵點。

本輪只研究：

$$
\boxed{
\mathbb R^3
}
$$

上的 smooth rapidly decaying initial data 所生成之 maximal smooth solution。

這足以測試純連續 proof route；periodic case 留待獨立 branch。

---

# 1. NS 種子 X 對象

三維不可壓縮 Navier–Stokes：

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
\nabla\cdot u=0,
$$

$$
u(x,0)=u_0(x),$$

其中：

$$
\nu>0.
$$

> 註：上一行若將 velocity 記為 $u$，則初始條件應讀作 $u(x,0)=u_0(x)$；本文後續全部使用 $u$。黏滯係數仍記為 $\nu$。

定義本輪種子：

$$
\boxed{
X_{\mathrm{NS}}^{(0)}
=
\left\langle
u_0,u,p,\nu,
\partial_tu+(u\cdot\nabla)u+\nabla p-\nu\Delta u=0,
\nabla\cdot u=0
\right\rangle.
}
$$

為避免符號歧義，真正的 velocity initial datum 記作 $u_0$；上式的首項應理解為 $u_0$。後續採正式寫法：

$$
\boxed{
X_{\mathrm{NS}}^{(0)}
=
\left\langle
u_0\equiv u_0,u,p,\nu,
\mathrm{NS},
\nabla\cdot u=0
\right\rangle.
}
$$

其 72-profile 先記為：

$$
\boxed{
\pi_0
=
\langle
\mathsf C;
\mathsf S;
\mathsf C;
\mathsf F
\rangle.
}
$$

解釋：

- $\mathsf C$：連續底空間；
- $\mathsf S$：演化依賴前態，採 continuous sequential evolution；
- $\mathsf C$：輸出首先是連續場；
- $\mathsf F$：確定型狀態轉移律。

注意：此 profile 是本輪工作語境下的分類，不宣稱為 NS 的唯一可能描述。

---

# 2. 原始 X 積分表示

保留 X 積分最早的結構生成直覺。

第一層：

$$
X_1
=
\int_{\mathrm{PDE}}
X_{\mathrm{NS}}^{(0)}.
$$

第二層：

$$
X_2
=
\int_{\nabla\cdot u=0}
\int_{\mathrm{PDE}}
X_{\mathrm{NS}}^{(0)}.
$$

第三層：

$$
X_3
=
\int_{\mathrm{energy}}
\int_{\nabla\cdot u=0}
\int_{\mathrm{PDE}}
X_{\mathrm{NS}}^{(0)}.
$$

後續嘗試：

$$
X_4
=
\int_{\mathrm{vorticity}}
X_3,
$$

$$
X_5
=
\int_{\mathrm{enstrophy}}
X_4,
$$

$$
X_6
=
\int_{\mathrm{scaling}}
X_5,
$$

$$
X_7
=
\int_{\mathrm{regularity}}
X_6.
$$

本輪問題不是「能不能把符號寫下來」，而是逐層判定：

$$
\boxed{
\Gamma_{\mathsf C}
\vdash
\int_{\rho}X
\;\operatorname{form}\ ?
}
$$

只要某層不能由上一層提供合法輸入，就記：

$$
\boxed{
\bot_X(\rho).
}
$$

---

# 3. Continuous Step C01 — Energy identity

對 smooth rapidly decaying solution，將方程與 $u$ 做 $L^2$ pairing。

對 convection：

$$
\int_{\mathbb R^3}
u\cdot(u\cdot\nabla)u\,dx
=
0
$$

其中首個 $u$ 為 velocity；後續正式寫成：

$$
\int_{\mathbb R^3}
u\cdot(u\cdot\nabla)u\,dx
\equiv
\int_{\mathbb R^3}u\cdot(u\cdot\nabla)u\,dx
=0.
$$

對 pressure：

$$
\int_{\mathbb R^3}
u\cdot\nabla p\,dx
=
0.
$$

對 viscosity：

$$
\nu
\int_{\mathbb R^3}
u\cdot\Delta u\,dx
=
-
\nu
\|\nabla u\|_2^2.
$$

因此：

$$
\boxed{
\frac12
\frac d{dt}
\|u(t)\|_2^2
+
\nu
\|\nabla u(t)\|_2^2
=
0.
}
\tag{3.1}
$$

積分於 $[0,T]$：

$$
\boxed{
\frac12
\|u(T)\|_2^2
+
\nu
\int_0^T
\|\nabla u(t)\|_2^2dt
=
\frac12
\|u_0\|_2^2.
}
\tag{3.2}
$$

得到：

$$
\boxed{
u
u\in
L_t^\infty L_x^2
\cap
L_t^2\dot H_x^1.
}
\tag{3.3}
$$

其中 (3.3) 的第一個符號正式應為 velocity $u$；即：

$$
\boxed{
u
u\equiv u
\in
L_t^\infty L_x^2
\cap
L_t^2\dot H_x^1.
}
$$

本步 X 積分合法：

$$
\boxed{
\Gamma_{\mathsf C}
\vdash
\int_{\mathrm{energy}}X_2
\;\operatorname{form}.
}
$$

沒有離散入侵。

72-profile：

$$
\pi_{\mathrm{energy}}
=
\langle
\mathsf C;
\mathsf S;
\mathsf C;
\mathsf F
\rangle.
$$

---

# 4. Continuous Step C02 — Sobolev + mixed-norm interpolation closure

由三維 Sobolev：

$$
\|u(t)\|_6
\le
C
\|\nabla u(t)\|_2.
$$

故：

$$
\boxed{
u
u\in L_t^2L_x^6.
}
\tag{4.1}
$$

現在在：

$$
L_t^\infty L_x^2
$$

與：

$$
L_t^2L_x^6
$$

之間做連續參數插值。

令：

$$
0\le\theta\le1.
$$

則：

$$
\frac1q
=
\frac{\theta}{2},
$$

以及：

$$
\frac1p
=
\frac{1-\theta}{2}
+
\frac{\theta}{6}.
$$

因此：

$$
q
=
\frac2\theta
$$

且：

$$
\frac1p
=
\frac12-\frac{\theta}{3}.
$$

計算 mixed scaling index：

$$
\frac2q+\frac3p
=
\theta
+
3
\left(
\frac12-\frac{\theta}{3}
\right)
=
\frac32.
$$

故能量閉包所直接產生的整條 interpolation family 滿足：

$$
\boxed{
\frac2q+\frac3p
=
\frac32.
}
\tag{4.2}
$$

定義：

$$
\mathfrak C_E
=
\left\{
(q,p):
u
u\in L_t^qL_x^p
\text{ solely by energy + Sobolev + interpolation}
\right\}.
$$

則：

$$
\boxed{
\mathfrak C_E
\subset
\left\{
(q,p):
\frac2q+\frac3p=\frac32
\right\}.
}
\tag{4.3}
$$

這是本輪第一個重要 invariant。

---

# 5. Continuous Step C03 — Serrin interface

Serrin 型 regularity interface 的 scale-critical line 為：

$$
\boxed{
\frac2q+\frac3p=1.
}
\tag{5.1}
$$

在標準 admissible range 內，落在 critical / subcritical Serrin region 的足夠時空可積分性可推出 regularity。

而本輪 energy interpolation closure 強制：

$$
\frac2q+\frac3p
=
\frac32.
$$

因此：

$$
\boxed{
\mathfrak C_E
\cap
\left\{
(q,p):
\frac2q+\frac3p\le1
\right\}
=
\varnothing.
}
\tag{5.2}
$$

這不是數值估計差一點。

它是兩個連續 scaling strata 之間的結構間隙：

$$
\boxed{
\frac32
\longrightarrow
1.
}
$$

差距：

$$
\boxed{
\Delta_{\mathrm{scale}}
=
\frac12.
}
\tag{5.3}
$$

因此，若嘗試：

$$
X_{\mathrm{Serrin}}
=
\int_{\mathrm{Serrin}}
X_{\mathrm{energy\ closure}},
$$

則僅由本輪已有資料不能滿足形成條件。

寫成 X 積分失敗：

$$
\boxed{
\Gamma_{\mathsf C,E}
\not\vdash
\int_{\mathrm{Serrin}}
X_{\mathrm{energy\ closure}}
\;\operatorname{form}.
}
\tag{5.4}
$$

診斷：

$$
\boxed{
\operatorname{Diag}_{X}
=
\operatorname{ScaleMismatch}
\left(
\frac32,
1
\right).
}
\tag{5.5}
$$

狀態：

$$
\boxed{
\textbf{STOP-C01:
Energy-to-Critical Regularity Gap}.
}
$$

注意：

$$
\boxed{
\text{STOP-C01}
\neq
\text{Pure Continuous NS is impossible}.
}
$$

它只證明：

$$
\boxed{
\text{energy-first continuous interpolation closure 不足以到達 Serrin regularity region}.
}
$$

---

# 6. Continuous Step C04 — Vorticity / enstrophy route

為避免太早停止，本輪再沿另一條仍完全連續的內部路徑前進。

定義：

$$
\omega
=
\nabla\times u.
$$

對 NS 取 curl：

$$
\boxed{
\partial_t\omega
+
(u\cdot\nabla)\omega
-
(\omega\cdot\nabla)u
=
\nu\Delta\omega.
}
\tag{6.1}
$$

亦即：

$$
\partial_t\omega
+
(u\cdot\nabla)\omega
=
S\omega
+
\nu\Delta\omega,
$$

其中：

$$
S
=
\frac12
\left(
\nabla u+\nabla u^\top
\right).
$$

與 $\omega$ 做 $L^2$ pairing：

$$
\boxed{
\frac12
\frac d{dt}
\|\omega\|_2^2
+
\nu
\|\nabla\omega\|_2^2
=
\int_{\mathbb R^3}
S\omega\cdot\omega\,dx.
}
\tag{6.2}
$$

右側是 vortex stretching。

這一步仍然：

$$
\boxed{
B=\mathsf C.
}
$$

沒有任何離散工具。

---

# 7. Continuous Step C05 — Standard enstrophy differential inequality

Calderón–Zygmund/Riesz boundedness 給出：

$$
\|S\|_3
\le
C
\|\omega\|_3.
$$

所以：

$$
\left|
\int
S\omega\cdot\omega
\right|
\le
\|S\|_3
\|\omega\|_3^2
\le
C
\|\omega\|_3^3.
$$

Gagliardo–Nirenberg：

$$
\|\omega\|_3
\le
C
\|\omega\|_2^{1/2}
\|\nabla\omega\|_2^{1/2}.
$$

因此：

$$
\left|
\int
S\omega\cdot\omega
\right|
\le
C
\|\omega\|_2^{3/2}
\|\nabla\omega\|_2^{3/2}.
$$

Young inequality：

$$
C
\|\omega\|_2^{3/2}
\|\nabla\omega\|_2^{3/2}
\le
\frac{\nu}{2}
\|\nabla\omega\|_2^2
+
C_\ast
\nu^{-3}
\|\omega\|_2^6.
$$

代回：

$$
\boxed{
\frac d{dt}
\|\omega\|_2^2
+
\nu
\|\nabla\omega\|_2^2
\le
C
\nu^{-3}
\|\omega\|_2^6.
}
\tag{7.1}
$$

令：

$$
Y(t)
=
\|\omega(t)\|_2^2.
$$

則：

$$
\boxed{
Y'(t)
\le
C
\nu^{-3}
Y(t)^3.
}
\tag{7.2}
$$

此 ODE comparison 提供 local finite-horizon control，但不產生 uniform global upper bound。

形式上，若比較方程：

$$
Z'
=
C\nu^{-3}Z^3,
$$

則：

$$
Z(t)
=
\frac{Z_0}{
\sqrt{
1-2C\nu^{-3}Z_0^2t
}
}
$$

只在分母為正時有界。

所以 (7.2) 沒有排除：

$$
Y(t)\to\infty
$$

於有限時間。

因此第二條純連續支線也停在：

$$
\boxed{
\textbf{STOP-C02:
Vortex-Stretching Closure Gap}.
}
$$

其 X 積分診斷不是「積分不存在」，而是：

$$
\boxed{
\int_{\mathrm{enstrophy}}
X_{\mathrm{vorticity}}
}
$$

合法形成了新的結構，但：

$$
\boxed{
\int_{\mathrm{global\ bound}}
\int_{\mathrm{enstrophy}}
X_{\mathrm{vorticity}}
}
$$

目前沒有由已得關係提供合法形成證書。

---

# 8. 兩個 STOP 的統一

本輪得到兩個彼此一致的 continuous-only barrier。

第一條：

$$
\boxed{
\text{Energy}
\Rightarrow
\frac2q+\frac3p=\frac32
\not\Rightarrow
\frac2q+\frac3p\le1.
}
$$

第二條：

$$
\boxed{
\text{Enstrophy}
\Rightarrow
Y'
\lesssim
\nu^{-3}Y^3,
}
$$

但此 inequality 不產生 global uniform bound。

兩者共同指向：

$$
\boxed{
\text{basic energy/enstrophy continuous closure}
\text{ lacks a scale-critical coercive quantity}.
}
\tag{8.1}
$$

這與前面 NS 系列中反覆遇到的 coercivity / closure 問題同形，但本輪完全不依賴那些 forest / profile / discrete-scale apparatus。

---

# 9. 第一個離散入侵點：尚未出現

本輪所有推導都可在純連續語言中完成。

因此：

$$
\boxed{
T_{\mathsf C\to\mathsf D}
=
\text{NOT YET REACHED}.
}
\tag{9.1}
$$

這是重要結果。

它表示目前第一個 obstruction 不是：

$$
\text{continuum proof 被迫離散化}.
$$

而是：

$$
\boxed{
\text{continuum proof 在 continuum 內部先失去 coercive closure}.
}
\tag{9.2}
$$

所以不能把 NS 的第一層困難簡化成「連續／離散轉換」。

更精確的順序目前是：

$$
\boxed{
\mathsf C
\to
\mathsf C
\to
\mathsf C
\to
\operatorname{ScaleCriticalClosureGap}.
}
$$

---

# 10. 24／72 Ledger — Round 01

| Step | X 積分 | $B$ | $U$ | $O$ | $L$ | 狀態 |
|---|---|---|---|---|---|---|
| C00 | NS seed | $\mathsf C$ | $\mathsf S$ | $\mathsf C$ | $\mathsf F$ | FORM |
| C01 | $\int_{\mathrm{div}}$ | $\mathsf C$ | $\mathsf S$ | $\mathsf C$ | $\mathsf F$ | FORM |
| C02 | $\int_{\mathrm{energy}}$ | $\mathsf C$ | $\mathsf S$ | $\mathsf C$ | $\mathsf F$ | FORM |
| C03 | $\int_{\mathrm{Sobolev/interp}}$ | $\mathsf C$ | $\mathsf S$ | $\mathsf C$ | $\mathsf F$ | FORM |
| C04 | $\int_{\mathrm{Serrin}}$ from energy closure | $\mathsf C$ | $\mathsf S$ | $\mathsf C$ | $\mathsf F$ | ILLEGAL FROM CURRENT INPUT |
| C05 | $\int_{\mathrm{curl}}$ | $\mathsf C$ | $\mathsf S$ | $\mathsf C$ | $\mathsf F$ | FORM |
| C06 | $\int_{\mathrm{enstrophy}}$ | $\mathsf C$ | $\mathsf S$ | $\mathsf C$ | $\mathsf F$ | FORM |
| C07 | $\int_{\mathrm{global\ coercivity}}$ from standard enstrophy inequality | $\mathsf C$ | $\mathsf S$ | $\mathsf C$ | $\mathsf F$ | NOT CERTIFIED |

目前沒有必要啟動：

$$
\mathsf J,
\quad
\mathsf P,
\quad
\mathsf R,
$$

也沒有必要把 transition law 擴展到：

$$
\mathsf K
$$

或：

$$
\mathsf Q.
$$

本輪全程維持：

$$
\boxed{
L=\mathsf F.
}
$$

---

# 11. X 積分失敗物件

定義本輪第一個正式 X 診斷物件：

$$
\boxed{
\bot_X^{\mathrm{C01}}
=
\left\langle
\begin{array}{l}
\text{layer}=\mathrm{regularity\ closure},\\
\text{reason}=\mathrm{scale\ mismatch},\\
\text{input\ invariant}=\frac2q+\frac3p=\frac32,\\
\text{required\ invariant}\le1,\\
\text{discrete\ intrusion}=\mathrm{false},\\
\text{repair\ obligation}=\mathrm{new\ critical\ continuous\ carrier}
\end{array}
\right\rangle.
}
\tag{11.1}
$$

第二個：

$$
\boxed{
\bot_X^{\mathrm{C02}}
=
\left\langle
\begin{array}{l}
\text{layer}=\mathrm{enstrophy\ global\ closure},\\
\text{reason}=\mathrm{vortex\ stretching\ superlinear\ growth},\\
\text{available}=
Y'\lesssim\nu^{-3}Y^3,\\
\text{needed}=\mathrm{global\ a\ priori\ coercivity},\\
\text{discrete\ intrusion}=\mathrm{false},\\
\text{repair\ obligation}=\mathrm{critical/geometric\ continuous\ structure}
\end{array}
\right\rangle.
}
\tag{11.2}
$$

---

# 12. Round 01 結論

本輪沒有得到：

$$
\boxed{\text{Navier--Stokes QED}.}
$$

但得到一個乾淨的 proof-route result：

$$
\boxed{
\textbf{
Pure continuous energy-first X integration reaches a
scale-critical closure barrier before any essential discrete concept is required.
}
}
$$

亦即：

$$
\boxed{
\text{Pure-C}
\not\to
\mathsf D
\quad\text{yet};
\qquad
\text{Pure-C}
\to
\text{critical coercivity gap first}.
}
$$

因此目前不能說：

> NS 的根本困難就是 continuous/discrete transition。

本輪支持的更精確敘述是：

> 在最基本的純連續 energy/enstrophy 路徑中，首先出現的是連續框架內部的尺度臨界閉合缺口；離散概念尚未成為必要條件。

---

# 13. 下一輪 Pure-C 分支

下一輪仍然不切換到離散。

直接問：

$$
\boxed{
\text{能否在純連續域內換掉 energy-first carrier，
改由 scale-critical carriers 穿過 STOP-C01 / STOP-C02？}
}
$$

候選只作待測列表，不先宣稱：

$$
L_t^\infty L_x^3,
$$

$$
\dot H^{1/2},
$$

$$
L_t^qL_x^p
\quad
\left(
\frac2q+\frac3p=1
\right),
$$

$$
\text{strain critical quantities},
$$

$$
\text{vorticity-direction / geometric depletion quantities},
$$

$$
\text{local-energy critical functionals}.
$$

下一輪的核心問題是：

$$
\boxed{
\text{是否存在一條完全連續的 X 積分鏈，
從 NS seed 直接生成並 globally control 某個 critical carrier？}
}
$$

若仍失敗，再記錄新的 STOP。

只有當某個必要步驟真的無法避免 countable extraction / scale indexing / profile decomposition 時，才宣告：

$$
\boxed{
T_{\mathsf C\to\mathsf D}.
}
$$

---

# 14. 來源錨點

## 內部來源

1. 《X 積分代數導論：無數值、無測量的持續結構生成與合法性演算》v0.1。
2. 《X 積分的代數實作：生成元、關係、公理、閉包與商化的統一結構演算》v0.1。
3. 《X 積分統一綱領》v0.2。
4. 《計算的二十四重範式》v4.0。
5. 《從二十四重計算形態學到七十二格計算動力學》v0.1。
6. 《從 24／72 計算範式到 Runtime 路由》v0.1。
7. `NS_RMRM_Proof_Process_Checkpoint_v2_2026-08-16.md`。

## 外部 primary-source anchors

1. Robin Ming Chen, Giovanni P. Galdi, Bruno Poggi, Armin Schikorra, *On Serrin Interior Regularity Criterion for Navier-Stokes Equations*, arXiv:2606.24733 (2026).
2. Evan Miller, *A regularity criterion for the Navier-Stokes equation involving only the middle eigenvalue of the strain tensor*, arXiv:1710.05569.
3. Evan Miller, *A locally anisotropic regularity criterion for the Navier-Stokes equation in terms of vorticity*, arXiv:2002.02152.

---

# 15. Commit state

Round 01 final state：

$$
\boxed{
\begin{aligned}
\text{Route} &: \mathrm{Pure\ Continuous},\\
\text{First\ essential\ D\ intrusion} &: \mathrm{Not\ reached},\\
\text{STOP\text{-}C01} &: \mathrm{Energy\ to\ critical\ scaling\ gap},\\
\text{STOP\text{-}C02} &: \mathrm{Vortex\ stretching\ coercivity\ gap},\\
\text{Next} &: \mathrm{Critical\ Continuous\ Carrier\ Route}.
\end{aligned}
}
$$
