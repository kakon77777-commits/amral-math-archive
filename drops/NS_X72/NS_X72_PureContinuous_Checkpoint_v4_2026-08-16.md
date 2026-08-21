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

---

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

---

# NS × X 積分 × 24/72 範式實戰
## Round 03 — Pure Continuous Relational / Geometric Route

- 日期：2026-08-16
- 版本：v0.1
- 狀態：Proof-Route Experiment / Continuous-Only Relational Geometry Branch
- canonical source：UTF-8 Markdown
- canonical math delimiters：inline `$...$`；display `$$...$$`
- 前一輪：`NS_X72_Round02_PureCriticalContinuous_CarrierBarrier_v0.1_2026-08-16.md`
- 本輪目標：不再依賴單一 critical amplitude，而保留 strain、vorticity、eigenvalue、alignment 與 nonlinear sign 等連續關係資料，檢驗幾何 depletion 是否能在純連續域中產生無條件 global coercivity。
- 非主張：本文導出的 regularity criteria 不宣稱新穎；其用途是把既有/可直接導出的幾何判準放入 X 積分與 24/72 proof-route ledger，判定它們是否能成為無條件閉合鏈。

---

# 0. Round 02 handoff

Round 02 測試三條 scale-critical continuous route：

$$
\dot H^{1/2},
$$

$$
L_t^\infty L_x^3,
$$

以及 Kato/Duhamel critical fixed point。

共同結果：

$$
\boxed{
\text{Critical-Carrier Formation}
\neq
\text{Critical-Carrier Global Control}.
}
$$

主要 STOP：

$$
\boxed{
\text{STOP-C03}
=
\text{Critical-Amplitude Absorption Gap},
}
$$

$$
\boxed{
\text{STOP-C04}
=
\text{Endpoint-in-Time Critical Control Gap},
}
$$

$$
\boxed{
\text{STOP-C05}
=
\text{Global Critical Fixed-Point Gap}.
}
$$

同時得到 critical scaling fixed-point fact：

$$
\boxed{
\mathcal A_{\rm crit}(u_\lambda)
=
\mathcal A_{\rm crit}(u),
}
$$

所以 NS scaling 無法把 large critical data 修復成 small critical data。

本輪因此改問：

$$
\boxed{
\text{是否是單一 amplitude observation 丟掉了真正的 closure information？}
}
$$

---

# 1. Pure continuous relational state

保持底空間：

$$
\boxed{
B=\mathsf C.
}
$$

令：

$$
S
=
\nabla_{\rm sym}u
=
\frac12
\left(
\nabla u+\nabla u^\top
\right),
$$

$$
\omega
=
\nabla\times u.
$$

由 incompressibility：

$$
\boxed{
\operatorname{tr}S=0.
}
\tag{1.1}
$$

設 strain eigenvalues：

$$
\lambda_1
\le
\lambda_2
\le
\lambda_3,
$$

故：

$$
\boxed{
\lambda_1+\lambda_2+\lambda_3=0.
}
\tag{1.2}
$$

在 $\omega\neq0$ 處定義 vorticity direction：

$$
\xi
=
\frac{\omega}{|\omega|}.
$$

定義 relational stretching scalar：

$$
\boxed{
\sigma
=
\xi^\top S\xi.
}
\tag{1.3}
$$

則：

$$
\boxed{
\omega^\top S\omega
=
|\omega|^2\sigma.
}
\tag{1.4}
$$

本輪 relational X state 設為：

$$
\boxed{
X_{\rm geom}
=
\left\langle
u,p,S,\omega,
\lambda_1,\lambda_2,\lambda_3,
\xi,\sigma,
\det S,
\nabla S
\right\rangle.
}
\tag{1.5}
$$

其形成鏈：

$$
X_{\rm geom}
=
\int_{\rm spectrum}
\int_{\rm alignment}
\int_{\omega=\nabla\times u}
\int_{S=\nabla_{\rm sym}u}
X_{\rm NS}.
$$

這些都是 continuous deterministic operations。

因此目前仍：

$$
\boxed{
\pi_{\rm geom}
=
\langle
\mathsf C;
\mathsf S;
\mathsf X_{\Gamma_{\rm geom}}\text{ candidate};
\mathsf F
\rangle.
}
$$

---

# 2. Exact vorticity-enstrophy relation

Vorticity equation：

$$
\partial_t\omega
+
(u\cdot\nabla)\omega
-
S\omega
=
\nu\Delta\omega.
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
\omega^\top S\omega\,dx.
}
\tag{2.1}
$$

使用 (1.4)：

$$
\boxed{
\frac12
\frac d{dt}
\|\omega\|_2^2
+
\nu
\|\nabla\omega\|_2^2
=
\int
|\omega|^2\sigma\,dx.
}
\tag{2.2}
$$

所以 vortex stretching 不是只有 amplitude。

真正 pointwise relational carrier 是：

$$
\boxed{
(|\omega|,\sigma).
}
$$

若只保留：

$$
|\omega|
$$

或：

$$
\|\omega\|_2,
$$

則 stretching 的 sign 與 geometry 已被投影掉。

---

# 3. Exact strain-enstrophy identity

對足夠光滑、衰減良好的三維 incompressible NS solution，有：

$$
\boxed{
\frac d{dt}
\|S\|_2^2
=
-2\nu
\|\nabla S\|_2^2
-
4
\int_{\mathbb R^3}
\det S\,dx.
}
\tag{3.1}
$$

又因：

$$
\|S\|_2^2
=
\frac12
\|\omega\|_2^2,
$$

strain 與 vorticity enstrophy 是同一 physical derivative scale 的兩種 relational representation。

(3.1) 的重要性是：

$$
\boxed{
\text{nonlinear enstrophy production}
=
-4\int\det S.
}
\tag{3.2}
$$

pressure 與 vorticity nonlocality 在這個 global identity 中不再顯式出現。

這不是解掉 NS，而是成功把「非線性危險」壓成 strain spectrum 的 sign structure。

---

# 4. Algebraic Lemma — middle eigenvalue controls the dangerous determinant sign

## Lemma 4.1

對任意 real symmetric trace-free $3\times3$ matrix：

$$
S,
$$

令：

$$
\lambda_1\le\lambda_2\le\lambda_3.
$$

則 pointwise：

$$
\boxed{
-\det S
\le
\frac12
\lambda_2^+
|S|^2,
}
\tag{4.1}
$$

其中：

$$
\lambda_2^+
=
\max\{\lambda_2,0\}.
$$

### Proof

若：

$$
\lambda_2\le0,
$$

則：

$$
\lambda_1\le\lambda_2\le0
$$

且 trace-free 強迫：

$$
\lambda_3\ge0.
$$

故：

$$
\det S
=
\lambda_1\lambda_2\lambda_3
\ge0.
$$

所以：

$$
-\det S
\le0
=
\frac12\lambda_2^+|S|^2.
$$

現在考慮：

$$
\lambda_2>0.
$$

令：

$$
a=-\lambda_1>0,
\qquad
b=\lambda_2>0,
\qquad
c=\lambda_3>0.
$$

trace-free 給：

$$
a=b+c.
$$

因此：

$$
-\det S
=
abc.
$$

另一方面：

$$
|S|^2
=
a^2+b^2+c^2
$$

$$
=
(b+c)^2+b^2+c^2
$$

$$
=
2(b^2+bc+c^2).
$$

而：

$$
ac
=
c(b+c)
=
bc+c^2
\le
b^2+bc+c^2
=
\frac12|S|^2.
$$

故：

$$
abc
\le
\frac12b|S|^2.
$$

即：

$$
-\det S
\le
\frac12
\lambda_2
|S|^2.
$$

證畢。

$$
\square
$$

---

# 5. Immediate geometric consequence

由 (3.1) 和 (4.1)：

$$
\frac d{dt}
\|S\|_2^2
+
2\nu
\|\nabla S\|_2^2
\le
2
\int
\lambda_2^+
|S|^2dx.
\tag{5.1}
$$

特別地，如果：

$$
\boxed{
\lambda_2(x,t)\le0
}
$$

對所有 relevant $(x,t)$ 成立，則：

$$
\boxed{
\frac d{dt}
\|S\|_2^2
+
2\nu
\|\nabla S\|_2^2
\le0.
}
\tag{5.2}
$$

所以在這個 geometric branch 中，enstrophy 單調不增。

因此：

$$
\boxed{
\lambda_2\le0
\quad\Longrightarrow\quad
\text{no enstrophy blow-up through this branch}.
}
\tag{5.3}
$$

對 smooth maximal solution，這提供 global continuation。

狀態：

$$
\boxed{
\textbf{CONDITIONAL CLOSED BRANCH}.
}
$$

---

# 6. Middle-eigenvalue critical criterion — continuous derivation

令：

$$
q>\frac32.
$$

由 Hölder：

$$
\int
\lambda_2^+
|S|^2
\le
\|\lambda_2^+\|_q
\|S\|_{\frac{2q}{q-1}}^2.
$$

設：

$$
r
=
\frac{2q}{q-1}.
$$

在：

$$
L^2
\quad\text{與}\quad
L^6
$$

之間插值。

令：

$$
\theta
=
\frac{3}{2q}.
$$

則：

$$
\frac1r
=
\frac{1-\theta}{2}
+
\frac{\theta}{6}.
$$

故：

$$
\|S\|_r^2
\le
C
\|S\|_2^{2(1-\theta)}
\|\nabla S\|_2^{2\theta}.
$$

代入 (5.1)：

$$
\frac d{dt}
\|S\|_2^2
+
2\nu
\|\nabla S\|_2^2
\le
C
\|\lambda_2^+\|_q
\|S\|_2^{2(1-\theta)}
\|\nabla S\|_2^{2\theta}.
$$

Young inequality給：

$$
C
\|\lambda_2^+\|_q
\|S\|_2^{2(1-\theta)}
\|\nabla S\|_2^{2\theta}
$$

$$
\le
\nu
\|\nabla S\|_2^2
+
C_{\nu,q}
\|\lambda_2^+\|_q^{p}
\|S\|_2^2,
$$

其中：

$$
p
=
\frac1{1-\theta}
=
\frac{2q}{2q-3}.
$$

因此：

$$
\boxed{
\frac2p+\frac3q=2.
}
\tag{6.1}
$$

最後：

$$
\boxed{
\frac d{dt}
\|S\|_2^2
+
\nu
\|\nabla S\|_2^2
\le
C_{\nu,q}
\|\lambda_2^+\|_q^p
\|S\|_2^2.
}
\tag{6.2}
$$

Gronwall：

$$
\boxed{
\|S(T)\|_2^2
\le
\|S(0)\|_2^2
\exp
\left(
C_{\nu,q}
\int_0^T
\|\lambda_2^+(t)\|_q^pdt
\right).
}
\tag{6.3}
$$

所以：

$$
\boxed{
\lambda_2^+
\in
L_t^pL_x^q,
\qquad
\frac2p+\frac3q=2,
\qquad
q>\frac32
}
\tag{6.4}
$$

是 scale-critical geometric regularity interface。

這與既有 middle-eigenvalue regularity theory 一致。

---

# 7. Relational Stretching Criterion

在 $\omega\neq0$ 處：

$$
\sigma
=
\xi^\top S\xi.
$$

在 $\omega=0$ 處令：

$$
\sigma=0.
$$

由 (2.2)：

$$
\frac12
\frac d{dt}
\|\omega\|_2^2
+
\nu
\|\nabla\omega\|_2^2
\le
\int
\sigma^+
|\omega|^2dx.
$$

完全重複 Section 6 的 Hölder–Sobolev–Young 推導，得到：

若：

$$
\sigma^+
\in
L_t^pL_x^q,
$$

且：

$$
\boxed{
\frac2p+\frac3q=2,
\qquad
q>\frac32,
}
\tag{7.1}
$$

則 enstrophy 保持有界。

所以：

$$
\boxed{
\text{critical control of actual stretching rate }\sigma^+
\Longrightarrow
\text{regularity}.
}
\tag{7.2}
$$

這個 criterion 在本文件只作直接推導使用，不主張其學術新穎性。

---

# 8. Exact alignment decomposition

在 $S$ 的 orthonormal eigenbasis：

$$
e_1,e_2,e_3,
$$

寫：

$$
\xi
=
a_1e_1+a_2e_2+a_3e_3,
$$

其中：

$$
a_1^2+a_2^2+a_3^2=1.
$$

則：

$$
\sigma
=
\lambda_1a_1^2
+
\lambda_2a_2^2
+
\lambda_3a_3^2.
$$

利用：

$$
a_2^2
=
1-a_1^2-a_3^2,
$$

得到：

$$
\boxed{
\sigma
=
\lambda_2
+
(\lambda_1-\lambda_2)a_1^2
+
(\lambda_3-\lambda_2)a_3^2.
}
\tag{8.1}
$$

由：

$$
\lambda_1-\lambda_2\le0
$$

可得：

$$
\sigma
\le
\lambda_2
+
(\lambda_3-\lambda_2)a_3^2.
$$

因此：

$$
\boxed{
\sigma^+
\le
\lambda_2^+
+
(\lambda_3-\lambda_2)
|\xi\cdot e_3|^2.
}
\tag{8.2}
$$

定義 extensional-alignment carrier：

$$
\boxed{
\mathcal A_3
=
(\lambda_3-\lambda_2)
|\xi\cdot e_3|^2.
}
\tag{8.3}
$$

所以 dangerous stretching 可由兩個 continuous relational channels 上界：

$$
\boxed{
\sigma^+
\le
\lambda_2^+
+
\mathcal A_3.
}
\tag{8.4}
$$

這給出一個明確的 multi-carrier picture：

$$
\boxed{
\text{danger}
=
\text{planar strain positivity}
+
\text{alignment toward strongest extension}
}
$$

作為上界結構。

若兩者皆有適當 critical spacetime control，則 $\sigma^+$ 亦被控制。

但 NS dynamics 目前沒有提供兩者的無條件 critical upper bound。

---

# 9. PROVED OBSERVATION FAILURE — amplitude-only scalar cannot preserve nonlinear sign

這是本輪 24 範式最重要的測試。

定義兩個 pointwise trace-free symmetric strain states：

$$
S_{\rm grow}
=
\operatorname{diag}(-2a,a,a),
$$

以及：

$$
S_{\rm decay}
=
\operatorname{diag}(-a,-a,2a),
$$

其中：

$$
a>0.
$$

兩者皆滿足：

$$
\operatorname{tr}S=0.
$$

且：

$$
|S_{\rm grow}|^2
=
4a^2+a^2+a^2
=
6a^2,
$$

$$
|S_{\rm decay}|^2
=
a^2+a^2+4a^2
=
6a^2.
$$

所以：

$$
\boxed{
|S_{\rm grow}|
=
|S_{\rm decay}|.
}
\tag{9.1}
$$

但是：

$$
\det S_{\rm grow}
=
-2a^3,
$$

$$
\det S_{\rm decay}
=
2a^3.
$$

因此 strain-enstrophy identity 中的 nonlinear production：

$$
-4\det S
$$

分別為：

$$
\boxed{
-4\det S_{\rm grow}
=
8a^3>0,
}
$$

以及：

$$
\boxed{
-4\det S_{\rm decay}
=
-8a^3<0.
}
$$

也就是：

$$
\boxed{
\text{same amplitude}
\quad
\text{but opposite nonlinear enstrophy sign}.
}
\tag{9.2}
$$

---

# 10. Restricted $\mathsf X$ theorem for norm-only observation

建立明確語境：

$$
\Gamma_{\rm amp}
=
\left(
\mathcal M_{\rm geom},
\mathcal Q_{\rm amp}
\right),
$$

其中 relevant observables 至少包括：

$$
\mathcal M_{\rm geom}
=
\{
|S|,
\operatorname{sign}(\det S),
\lambda_2^+
\},
$$

而容許的單一表示類限制為 amplitude-only scalar：

$$
\mathcal Q_{\rm amp}
=
\{
q:
q(S)=f(|S|)
\}.
$$

則由 Section 9，任何：

$$
q\in\mathcal Q_{\rm amp}
$$

都有：

$$
q(S_{\rm grow})
=
q(S_{\rm decay}),
$$

但：

$$
\operatorname{sign}
\det S_{\rm grow}
\neq
\operatorname{sign}
\det S_{\rm decay}.
$$

所以不存在由 $q$ 重建 nonlinear sign 的函數。

因此：

$$
\boxed{
\nexists q\in\mathcal Q_{\rm amp}
\text{ 對 }
\mathcal M_{\rm geom}
\text{ 為 }\Gamma_{\rm amp}\text{-充分}.
}
\tag{10.1}
$$

按照二十四重範式的拒單測定義：

$$
\boxed{
\mathsf X_{\Gamma_{\rm amp}}(S).
}
\tag{10.2}
$$

這是一個真正已證的、**語境相對** observation result。

注意：

$$
\boxed{
\mathsf X_{\Gamma_{\rm amp}}
}
$$

不代表「strain 不可能被單一數學對象編碼」。

它只代表：

> 在 amplitude-only norm observation class 中，單一 scalar amplitude 無法保存本輪要求的 nonlinear geometric invariants。

因此我們首次得到一個合法的 24-axis transition：

$$
\boxed{
\text{single amplitude observation}
\longrightarrow
\mathsf X_{\Gamma_{\rm amp}}.
}
\tag{10.3}
$$

這個 transition 發生在 observation axis，而不是 substrate axis。

---

# 11. Determinant geometry normalization

對任何 symmetric trace-free $3\times3$ matrix，有 sharp algebraic bound：

$$
\boxed{
|\det S|
\le
\frac{1}{3\sqrt6}
|S|^3.
}
\tag{11.1}
$$

等號在 eigenvalue ratio：

$$
(-2,1,1)
$$

或其 sign reversal / scaling 上達到。

定義 normalized dangerous geometry factor：

$$
\boxed{
\chi_S
=
\begin{cases}
\displaystyle
3\sqrt6
\frac{(-\det S)_+}{|S|^3},
&
|S|>0,
\\[1em]
0,
&
|S|=0.
\end{cases}
}
\tag{11.2}
$$

則：

$$
\boxed{
0\le\chi_S\le1.
}
\tag{11.3}
$$

而：

$$
(-\det S)_+
=
\frac{\chi_S}{3\sqrt6}
|S|^3.
$$

因此 exact strain identity 給：

$$
\frac d{dt}
\|S\|_2^2
+
2\nu
\|\nabla S\|_2^2
\le
\frac{4}{3\sqrt6}
\int
\chi_S
|S|^3dx.
\tag{11.4}
$$

這把 amplitude 與 geometry 明確拆開：

$$
\boxed{
\text{nonlinear danger}
=
\text{amplitude}^3
\times
\text{geometry factor}.
}
\tag{11.5}
$$

---

# 12. Constant-factor geometric depletion no-go

現在測試一個自然希望：

> 如果 geometry 永遠不是最危險形態，也許一個 uniform depletion factor 就足以 global control。

假設：

$$
\boxed{
\|\chi_S(t)\|_\infty
\le
\delta
<1
}
\tag{12.1}
$$

對所有時間成立。

則：

$$
\frac d{dt}
\|S\|_2^2
+
2\nu
\|\nabla S\|_2^2
\le
C
\delta
\|S\|_3^3.
$$

Gagliardo–Nirenberg：

$$
\|S\|_3^3
\le
C
\|S\|_2^{3/2}
\|\nabla S\|_2^{3/2}.
$$

令：

$$
E
=
\|S\|_2^2,
$$

$$
D
=
\|\nabla S\|_2^2.
$$

則：

$$
E'
+
2\nu D
\le
C
\delta
E^{3/4}
D^{3/4}.
$$

Young：

$$
C
\delta
E^{3/4}
D^{3/4}
\le
\nu D
+
C_\ast
\delta^4
\nu^{-3}
E^3.
$$

因此：

$$
\boxed{
E'
+
\nu D
\le
C_\ast
\delta^4
\nu^{-3}
E^3.
}
\tag{12.2}
$$

重要的是：

$$
\boxed{
E^3
}
$$

的超線性 exponent 沒有改變。

$\delta<1$ 只改善常數：

$$
C
\mapsto
C\delta^4.
$$

所以對任何固定：

$$
0<\delta\le1,
$$

(12.2) 本身仍不能排除 finite-time blow-up of the comparison ODE。

只有 extreme case：

$$
\delta=0
$$

直接消除 dangerous determinant。

因此：

$$
\boxed{
\textbf{
a fixed nonzero geometric depletion factor does not by itself change
the superlinear enstrophy closure class.
}
}
\tag{12.3}
$$

狀態：

$$
\boxed{
\textbf{PROVED NO-GO for this constant-factor depletion architecture}.
}
$$

這不排除更強的：

- scale-dependent depletion；
- amplitude-dependent depletion；
- spacetime-critical depletion；
- nonlocal cancellation；
- dynamic alignment feedback。

---

# 13. What geometry successfully accomplished

Round 02 的單 critical carrier 問題是：

$$
\boxed{
\text{amplitude known}
\quad
\text{but nonlinear sign unknown}.
}
$$

Round 03 透過 strain spectrum 得到：

$$
\boxed{
\text{nonlinear sign}
\longleftrightarrow
\det S
}
$$

以及：

$$
\boxed{
\text{dangerous determinant}
\lesssim
\lambda_2^+|S|^2.
}
$$

透過 vorticity direction 又得到：

$$
\boxed{
\text{actual stretching}
=
|\omega|^2
\xi^\top S\xi.
}
$$

所以 relational geometry 確實保留了單 scalar amplitude 丟失的資訊。

也就是：

$$
\boxed{
\text{Round 03 repairs an observation-loss defect from Round 02}.
}
$$

但 repair observation loss：

$$
\not\Rightarrow
$$

global coercivity。

---

# 14. Where the continuous relational route stops

現在有多個完全連續的 conditional regularity branches：

$$
\lambda_2\le0
\Longrightarrow
\text{closure},
$$

$$
\lambda_2^+
\in
L_t^pL_x^q,
\qquad
\frac2p+\frac3q=2
\Longrightarrow
\text{closure},
$$

$$
\sigma^+
\in
L_t^pL_x^q,
\qquad
\frac2p+\frac3q=2
\Longrightarrow
\text{closure}.
$$

但 NS energy/enstrophy identities 目前沒有無條件推出：

$$
\lambda_2^+
\in
L_t^pL_x^q,
$$

也沒有無條件推出：

$$
\sigma^+
\in
L_t^pL_x^q
$$

於 critical exponent。

因此：

$$
\boxed{
\Gamma_{\mathsf C,\rm geom}
\not\vdash
\int_{\rm unconditional\ geometric\ control}
X_{\rm geom}
\;\operatorname{form}.
}
\tag{14.1}
$$

定義：

$$
\boxed{
\textbf{STOP-C06:
Relational Geometry-to-Coercivity Gap}.
}
\tag{14.2}
$$

---

# 15. STOP-C06 的精確含義

它不是：

> geometry 沒用。

相反，geometry 已做到：

1. 恢復 nonlinear sign；
2. 分離 dangerous / safe strain topology；
3. 給出 scale-critical regularity interfaces；
4. 排除 $\lambda_2\le0$ branch；
5. 將 actual vortex stretching 分解為 eigenvalue + alignment channels。

缺的是：

$$
\boxed{
\text{NS dynamics itself forces one of these good geometric regimes}.
}
$$

也就是：

$$
\boxed{
\text{Criterion}
\neq
\text{A priori Dynamics}.
}
$$

這與 Round 02 的：

$$
\boxed{
\text{Critical Carrier Formation}
\neq
\text{Critical Carrier Global Control}
}
$$

同構，但這次 obstruction 已從「amplitude」推進成「geometry evolution」。

---

# 16. 第一個真正的 observation-axis transition

目前三輪都沒有出現：

$$
B:\mathsf C\to\mathsf D.
$$

所以：

$$
\boxed{
T_{\mathsf C\to\mathsf D}
=
\text{NOT YET REACHED}.
}
$$

但是本輪在限定語境：

$$
\Gamma_{\rm amp}
$$

下已經真正證明：

$$
\boxed{
\mathsf X_{\Gamma_{\rm amp}}.
}
$$

所以 proof route 目前更像：

$$
\boxed{
\langle
\mathsf C,\mathsf S,\mathsf C,\mathsf F
\rangle
}
$$

在單 amplitude observation 失效後，提升為：

$$
\boxed{
\langle
\mathsf C,\mathsf S,\mathsf X_{\Gamma_{\rm amp}},\mathsf F
\rangle.
}
\tag{16.1}
$$

這是目前 24/72 實戰第一個真正由數學反例支撐的 axis transition。

---

# 17. 72 第四軸仍未轉移

strain spectrum、vorticity alignment、pressure coupling 全部仍是原 deterministic NS law 的結果。

因此：

$$
\boxed{
L=\mathsf F
}
$$

仍然足夠描述本輪 dynamics。

沒有任何證據要求：

$$
\mathsf K
$$

或：

$$
\mathsf Q.
$$

所以目前的困難不是 transition-law 類型不夠。

目前困難是：

$$
\boxed{
\text{deterministic continuous dynamics 中的 relational geometry 無 coercive feedback theorem}.
}
$$

---

# 18. Round 03 24/72 Ledger

| Step | X 積分 / carrier | $B$ | $U$ | $O$ | $L$ | 狀態 |
|---|---|---|---|---|---|---|
| C19 | $\int_{S=\mathrm{sym}\nabla u}$ | $\mathsf C$ | $\mathsf S$ | $\mathsf C$ | $\mathsf F$ | FORM |
| C20 | $\int_{\omega=\nabla\times u}$ | $\mathsf C$ | $\mathsf S$ | $\mathsf C$ | $\mathsf F$ | FORM |
| C21 | $\int_{\rm spectrum}$ | $\mathsf C$ | $\mathsf S$ | multi-observable | $\mathsf F$ | FORM |
| C22 | exact strain-enstrophy identity | $\mathsf C$ | $\mathsf S$ | multi-observable | $\mathsf F$ | FORM |
| C23 | $\lambda_2^+$ critical criterion | $\mathsf C$ | $\mathsf R$ meta-step | multi-observable | $\mathsf F$ | CONDITIONAL CLOSED |
| C24 | $\sigma^+$ stretching criterion | $\mathsf C$ | $\mathsf R$ meta-step | multi-observable | $\mathsf F$ | CONDITIONAL CLOSED |
| C25 | norm-only observation sufficiency | $\mathsf C$ | — | $\mathsf C$ scalar | $\mathsf F$ | REFUTED |
| C26 | $\mathsf X_{\Gamma_{\rm amp}}$ | $\mathsf C$ | — | $\mathsf X$ | $\mathsf F$ | PROVED IN RESTRICTED CONTEXT |
| C27 | constant geometric depletion $\delta<1$ | $\mathsf C$ | $\mathsf S$ | $\mathsf X$ | $\mathsf F$ | INSUFFICIENT |
| C28 | unconditional geometric feedback | $\mathsf C$ | $\mathsf S$ | $\mathsf X$ | $\mathsf F$ | OPEN / STOP-C06 |

---

# 19. New X diagnostic objects

## Observation failure

$$
\boxed{
\bot_X^{\mathrm{O01}}
=
\left\langle
\begin{array}{l}
\text{layer}=\mathrm{observation},\\
\text{context}=\Gamma_{\rm amp},\\
\text{candidate}=q(S)=f(|S|),\\
\text{collision}=S_{\rm grow},S_{\rm decay},\\
\text{preserved}=|S|,\\
\text{lost}=\operatorname{sign}(\det S),\lambda_2^+,\\
\text{repair}=\mathsf X_{\Gamma_{\rm amp}}\text{ / multi-carrier geometry}
\end{array}
\right\rangle.
}
$$

## Geometry closure failure

$$
\boxed{
\bot_X^{\mathrm{C06}}
=
\left\langle
\begin{array}{l}
\text{layer}=\mathrm{geometric\ coercivity},\\
\text{available}=\lambda_2^+,\sigma^+,\chi_S,\det S,\\
\text{known}=\mathrm{critical\ conditional\ criteria},\\
\text{missing}=\mathrm{unconditional\ dynamic\ control},\\
\text{constant\ depletion}=\mathrm{insufficient},\\
\text{discrete\ intrusion}=\mathrm{false}
\end{array}
\right\rangle.
}
$$

---

# 20. Round 03 strongest result

本輪最重要的 proof-route statement：

$$
\boxed{
\textbf{
Pure continuous relational geometry repairs scalar observation loss
but still does not provide unconditional geometric coercivity.
}
}
$$

更精確：

$$
\boxed{
\text{Amplitude-only}
\to
\mathsf X_{\Gamma_{\rm amp}}
\to
\text{Relational Geometry}
\to
\text{Conditional Critical Criteria}
\to
\operatorname{STOP-C06}.
}
$$

因此前三輪的 obstruction evolution 是：

$$
\boxed{
\begin{aligned}
\text{Round 01: }&
\mathrm{ScaleMismatch},
\\
\text{Round 02: }&
\mathrm{CriticalAmplitude/StructureMismatch},
\\
\text{Round 03: }&
\mathrm{GeometryEvolution/CoercivityMismatch}.
\end{aligned}
}
$$

每一輪都在縮小「純連續方法真正缺的是什麼」。

---

# 21. 下一輪：Pure Continuous Geometry Evolution Route

下一輪仍不使用本質離散化。

不再只把：

$$
\lambda_2^+,
\qquad
\sigma^+,
\qquad
\chi_S
$$

當作 regularity condition。

直接研究它們的 dynamics。

核心問題：

$$
\boxed{
\text{NS evolution 是否會自行抑制 dangerous geometry？}
}
$$

第一主線：

$$
\boxed{
D_tS
=
\nu\Delta S
-
S^2
+
\text{vorticity terms}
-
\nabla^2p
}
$$

並追蹤：

$$
D_t\lambda_2,
$$

$$
D_t\det S,
$$

$$
D_t(\xi^\top S\xi).
$$

第二主線：

pressure Hessian 是否是：

$$
\boxed{
\text{geometry feedback 的必要非局部 carrier}
}
$$

而不是可被消掉的 nuisance term。

第三主線：

如果為了控制 spectrum evolution 必須持續加入：

$$
\nabla^2p,
\quad
\nabla S,
\quad
\nabla\omega,
\quad
\text{higher relational derivatives},
$$

則檢驗是否出現真正的：

$$
\boxed{
\text{continuous infinite hierarchy obstruction}.
}
$$

這會開始直接碰到使用者提出的：

$$
\boxed{
\text{約束與無限}
}
$$

而仍然不預設：

$$
\mathsf C\to\mathsf D.
$$

---

# 22. External primary-source anchors

1. Evan Miller, *A regularity criterion for the Navier-Stokes equation involving only the middle eigenvalue of the strain tensor*, Archive for Rational Mechanics and Analysis 235 (2020); arXiv:1710.05569.
   - exact strain evolution；
   - enstrophy identity；
   - middle-eigenvalue critical regularity criterion。

2. Evan Miller, *A locally anisotropic regularity criterion for the Navier--Stokes equation in terms of vorticity*, arXiv:2002.02152.
   - anisotropic / vorticity-direction-sensitive critical criteria。

3. Siran Li, *On Vortex Alignment and Boundedness of $L^q$ Norm of Vorticity*, arXiv:1712.00551.
   - vorticity direction coherence and bounded-vorticity consequences；
   - discusses the Constantin–Fefferman vortex-direction program.

4. Alexis Vasseur, *Regularity criterion for 3D Navier-Stokes equations in terms of the direction of the velocity*, arXiv:0705.2446.
   - direction-based geometric regularity as a distinct continuous relational route.

---

# 23. Commit state

$$
\boxed{
\begin{aligned}
\text{Route} &: \mathrm{Pure\ Continuous\ Relational/Geometric},\\
\text{First\ essential\ D\ intrusion} &: \mathrm{Not\ reached},\\
\text{Observation transition} &: \mathsf X_{\Gamma_{\rm amp}}\ \mathrm{proved},\\
\text{Safe branch} &: \lambda_2\le0,\\
\text{Critical criteria} &: \lambda_2^+,\sigma^+,\\
\text{Constant geometry depletion} &: \mathrm{insufficient},\\
\text{STOP-C06} &: \mathrm{Geometry\ Evolution/Coercivity\ Gap},\\
\text{Next} &: \mathrm{Pure\ Continuous\ Geometry\ Evolution}.
\end{aligned}
}
$$

---

# NS × X 積分 × 24/72 範式實戰
## Round 04 — Pure Continuous Geometry Evolution / Pressure-Constraint Route

- 日期：2026-08-16
- 版本：v0.1
- 狀態：Proof-Route Experiment / Continuous-Only Geometry-Evolution Branch
- canonical source：UTF-8 Markdown
- canonical math delimiters：inline `$...$`；display `$$...$$`
- 前一輪：`NS_X72_Round03_PureContinuous_RelationalGeometry_v0.1_2026-08-16.md`
- 本輪目標：不再把 $\lambda_2^+$、$\det S$、$\sigma^+$ 當外加 regularity criterion，而直接推導它們的連續演化，判定 Navier–Stokes dynamics 是否自身產生 geometric feedback；並檢驗 pressure Hessian 是否形成第一個不可由純局部幾何消去的 global continuous constraint carrier。
- 非主張：本輪不宣稱排除所有純連續證明，也不宣稱 pressure nonlocality 等於 blow-up。本文只判定指定 local-geometric closure architecture 的形成資格與停止點。

---

# 0. Round 03 handoff

Round 03 建立 relational state：

$$
X_{\rm geom}
=
\left\langle
u,p,S,\omega,
\lambda_1,\lambda_2,\lambda_3,
\xi,\sigma,
\det S,
\nabla S
\right\rangle,
$$

其中：

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
\xi
=
\frac{\omega}{|\omega|},
$$

$$
\sigma
=
\xi^\top S\xi.
$$

並證明 amplitude-only observation 在指定語境：

$$
\Gamma_{\rm amp}
$$

下不充分。

具體地，兩個 trace-free strain tensors：

$$
S_{\rm grow}
=
\operatorname{diag}(-2a,a,a),
$$

$$
S_{\rm decay}
=
\operatorname{diag}(-a,-a,2a)
$$

具有相同：

$$
|S|^2=6a^2,
$$

但：

$$
\det S_{\rm grow}
=
-2a^3,
$$

$$
\det S_{\rm decay}
=
2a^3.
$$

所以相同 amplitude 可對應相反 enstrophy-production sign。

因此：

$$
\boxed{
\mathsf X_{\Gamma_{\rm amp}}
}
$$

已在 restricted observation class 中成立。

Round 03 的主要 STOP：

$$
\boxed{
\text{STOP-C06}
=
\text{Geometry-Evolution / Coercivity Gap}.
}
$$

本輪直接攻：

$$
\boxed{
D_tS,
\quad
D_t\lambda_2,
\quad
D_t\det S,
\quad
D_t(\xi^\top S\xi).
}
$$

---

# 1. Velocity-gradient equation

令：

$$
A
=
\nabla u
$$

採 convention：

$$
A_{ij}
=
\partial_j u_i.
$$

Navier–Stokes：

$$
\partial_tu
+
u\cdot\nabla u
+
\nabla p
=
\nu\Delta u.
$$

取梯度。

令 material derivative：

$$
D_t
=
\partial_t+u\cdot\nabla.
$$

則：

$$
\boxed{
D_tA
+
A^2
+
\nabla^2p
=
\nu\Delta A.
}
\tag{1.1}
$$

分解：

$$
A=S+\Omega,
$$

其中：

$$
S^\top=S,
$$

$$
\Omega^\top=-\Omega.
$$

取 symmetric part：

$$
\operatorname{sym}(A^2)
=
S^2+\Omega^2.
$$

在三維：

$$
\Omega
=
\frac12[\omega]_\times,
$$

故：

$$
\boxed{
\Omega^2
=
\frac14
\left(
\omega\otimes\omega
-
|\omega|^2I
\right).
}
\tag{1.2}
$$

因此 exact strain equation：

$$
\boxed{
D_tS
-
\nu\Delta S
=
-
S^2
-
\frac14\omega\otimes\omega
+
\frac14|\omega|^2I
-
H_p,
}
\tag{1.3}
$$

其中：

$$
\boxed{
H_p
=
\nabla^2p.
}
\tag{1.4}
$$

本輪第一個重要結果：

> strain geometry 的 evolution 在 pointwise level 不是只由 $S$ 與 $\omega$ 的局部代數決定；pressure Hessian 與 viscosity-induced spatial geometry 同時進入。

---

# 2. Pressure Poisson constraint

對 momentum equation 取 divergence。

由：

$$
\nabla\cdot u=0
$$

得到：

$$
\boxed{
-\Delta p
=
\partial_i u_j\,
\partial_j u_i.
}
\tag{2.1}
$$

又：

$$
\operatorname{tr}(A^2)
=
\operatorname{tr}(S^2)
+
\operatorname{tr}(\Omega^2).
$$

且：

$$
\operatorname{tr}(S^2)
=
|S|^2,
$$

$$
\operatorname{tr}(\Omega^2)
=
-\frac12|\omega|^2.
$$

所以：

$$
\boxed{
-\Delta p
=
|S|^2
-
\frac12|\omega|^2.
}
\tag{2.2}
$$

定義 pressure source：

$$
\boxed{
f_p
=
|S|^2
-
\frac12|\omega|^2.
}
\tag{2.3}
$$

則：

$$
-\Delta p=f_p.
$$

在 $\mathbb R^3$、適當衰減條件下：

$$
p
=
(-\Delta)^{-1}f_p
$$

至多差一個時間函數。

因此：

$$
\boxed{
(H_p)_{ij}
=
\partial_i\partial_j(-\Delta)^{-1}f_p.
}
\tag{2.4}
$$

若使用 Riesz transform：

$$
\mathcal R_i
=
\partial_i(-\Delta)^{-1/2},
$$

則：

$$
\boxed{
(H_p)_{ij}
=
\mathcal R_i\mathcal R_j f_p.
}
\tag{2.5}
$$

這是一個 order-zero singular integral operator。

---

# 3. Isotropic / anisotropic pressure-Hessian split

由：

$$
\Delta p=-f_p
$$

可寫：

$$
\boxed{
H_p
=
-\frac13 f_p I
+
H_p^{\rm dev},
}
\tag{3.1}
$$

其中：

$$
\operatorname{tr}
H_p^{\rm dev}
=
0.
$$

所以 pressure Hessian 有兩部分：

1. isotropic trace part：

$$
-\frac13f_pI,
$$

其 scalar source 由 local：

$$
S,\omega
$$

直接決定；

2. deviatoric part：

$$
H_p^{\rm dev},
$$

它由 Poisson/Riesz global reconstruction 決定。

因此：

$$
\boxed{
\text{pressure trace is locally sourced, but pressure anisotropy is nonlocal}.
}
\tag{3.2}
$$

這個區分將直接控制 eigenvalue evolution。

---

# 4. PROVED — pressure Hessian is not a finite local differential operator of its source

考慮 operator：

$$
T_{ij}
=
\partial_i\partial_j(-\Delta)^{-1}.
$$

在 Fourier space：

$$
\widehat{T_{ij}f}(\xi)
=
-
\frac{\xi_i\xi_j}{|\xi|^2}
\widehat f(\xi).
$$

若 $T_{ij}$ 可以由某個 finite-order constant-coefficient local differential operator：

$$
P(D)
$$

在所有 smooth compactly supported source 上表示，則 Fourier symbol 必為一個 polynomial：

$$
P(i\xi).
$$

但是：

$$
-\frac{\xi_i\xi_j}{|\xi|^2}
$$

不是 polynomial。

因此：

$$
\boxed{
\partial_i\partial_j(-\Delta)^{-1}
}
$$

不是 finite-order local differential operator。

也就是：

$$
\boxed{
H_p(x)
}
$$

不能由：

$$
f_p(x),
\nabla f_p(x),
\ldots,
\nabla^k f_p(x)
$$

的某個 universal finite-order local differential rule 在所有 admissible source functions 上重建。

狀態：

$$
\boxed{
\textbf{PROVED operator-level nonlocality}.
}
\tag{4.1}
$$

注意：

這裡證明的是 pressure reconstruction operator 的非局部性。

它不宣稱：

> 每一個 NS solution 的 pressure Hessian 都無法利用額外 global invariants 被有效控制。

---

# 5. 72 / X interpretation of the incompressibility constraint

NS 時間演化是 deterministic：

$$
L=\mathsf F.
$$

但每一個時間 slice 的 pressure 並不是一個只靠 pointwise local state 更新的 scalar。

它由 global elliptic constraint：

$$
-\Delta p=f_p
$$

重建。

因此若 24-update axis 要描述「如何組織當前 state 的更新」，更精確的 NS profile 不是純：

$$
\mathsf S.
$$

而是 hybrid：

$$
\boxed{
\mathsf S_{\rm time}
+
\mathsf P_{\rm constraint}.
}
\tag{5.1}
$$

其中：

- $\mathsf S_{\rm time}$：時間演化依賴前一時刻 state；
- $\mathsf P_{\rm constraint}$：同一時間 slice 上，pressure constraint global coupling 同時作用於整個 spatial state。

因此本輪第一次出現一個有實際 PDE 結構支持的 update-axis refinement：

$$
\boxed{
\langle
\mathsf C;
\mathsf S;
\mathsf X;
\mathsf F
\rangle
}
$$

提升為：

$$
\boxed{
\langle
\mathsf C;
\{\mathsf S,\mathsf P\};
\mathsf X;
\mathsf F
\rangle.
}
\tag{5.2}
$$

這不是 substrate transition。

所以：

$$
\boxed{
B=\mathsf C
}
$$

仍保持不變。

---

# 6. Exact eigenvalue evolution

假設某點 strain spectrum simple：

$$
\lambda_1<\lambda_2<\lambda_3.
$$

令：

$$
e_i
$$

為 normalized eigenvector：

$$
Se_i
=
\lambda_ie_i.
$$

對 material derivative：

$$
\boxed{
D_t\lambda_i
=
e_i^\top(D_tS)e_i.
}
\tag{6.1}
$$

對 spatial derivative，standard symmetric-matrix eigenvalue perturbation formula 給：

$$
\partial_k^2\lambda_i
=
e_i^\top(\partial_k^2S)e_i
+
2
\sum_{j\ne i}
\frac{
|e_j^\top(\partial_kS)e_i|^2
}{
\lambda_i-\lambda_j
}.
$$

對 $k$ 求和：

$$
\Delta\lambda_i
=
e_i^\top(\Delta S)e_i
+
2
\sum_{k=1}^3
\sum_{j\ne i}
\frac{
|e_j^\top(\partial_kS)e_i|^2
}{
\lambda_i-\lambda_j
}.
$$

故：

$$
e_i^\top(\Delta S)e_i
=
\Delta\lambda_i
-
2
\sum_{k=1}^3
\sum_{j\ne i}
\frac{
|e_j^\top(\partial_kS)e_i|^2
}{
\lambda_i-\lambda_j
}.
$$

代入 strain equation (1.3)：

$$
\boxed{
\begin{aligned}
(D_t-\nu\Delta)\lambda_i
={}&
-\lambda_i^2
-\frac14(\omega\cdot e_i)^2
+\frac14|\omega|^2
\\
&-
e_i^\top H_pe_i
\\
&-
2\nu
\sum_{k=1}^3
\sum_{j\ne i}
\frac{
|e_j^\top(\partial_kS)e_i|^2
}{
\lambda_i-\lambda_j
}.
\end{aligned}
}
\tag{6.2}
$$

此式只在 simple spectrum region 直接使用。

eigenvalue collision 需要 spectral projection / generalized eigenvalue treatment，不能把 (6.2) 無條件穿過 collision set。

---

# 7. Middle eigenvalue equation has two independent sign-indefinite channels

對：

$$
i=2,
$$

定義：

$$
\mathcal G_2
=
-
2\nu
\sum_{k=1}^3
\left[
\frac{
|e_1^\top(\partial_kS)e_2|^2
}{
\lambda_2-\lambda_1
}
+
\frac{
|e_3^\top(\partial_kS)e_2|^2
}{
\lambda_2-\lambda_3
}
\right].
$$

因：

$$
\lambda_2-\lambda_1>0,
$$

但：

$$
\lambda_2-\lambda_3<0,
$$

所以第一部分非正，第二部分非負。

故：

$$
\boxed{
\mathcal G_2
\text{ has no fixed sign}.
}
\tag{7.1}
$$

另一方面 pressure channel：

$$
\boxed{
\mathcal P_2
=
-
e_2^\top H_pe_2
}
\tag{7.2}
$$

亦沒有 universal pointwise sign。

所以：

$$
\boxed{
(D_t-\nu\Delta)\lambda_2
}
$$

不是由：

$$
\lambda_2
$$

自身的一個 scalar sign-definite reaction-diffusion law控制。

這直接表示：

$$
\boxed{
\lambda_2\le0
}
$$

雖然是 Round 03 的 safe conditional branch，

但沒有由 (6.2) 得到一個 simple scalar maximum principle 證明此 region 對 arbitrary NS data 不變。

狀態：

$$
\boxed{
\textbf{PROVED failure of the naive scalar maximum-principle architecture}.
}
\tag{7.3}
$$

這不等於證明 safe region 一定會被離開；只表示該 invariance 不能由只看 $\lambda_2$ 的 pointwise scalar sign argument建立。

---

# 8. Pressure trace does not solve the eigenvalue problem

使用 (3.1)：

$$
e_2^\top H_pe_2
=
-\frac13f_p
+
e_2^\top H_p^{\rm dev}e_2.
$$

所以：

$$
\mathcal P_2
=
\frac13f_p
-
e_2^\top H_p^{\rm dev}e_2.
$$

第一項：

$$
\frac13
\left(
|S|^2-\frac12|\omega|^2
\right)
$$

是 local scalar。

但：

$$
e_2^\top H_p^{\rm dev}e_2
$$

仍是 global anisotropic constraint channel。

因此即使把 pressure trace 完全代回 local strain/vorticity amplitude：

$$
\boxed{
\text{anisotropic pressure feedback remains}.
}
\tag{8.1}
$$

---

# 9. Calderón–Zygmund control gives no criticality gain

Riesz transforms 在：

$$
1<q<\infty
$$

上有：

$$
\|H_p\|_{L^q}
\le
C_q
\|f_p\|_{L^q}.
$$

由：

$$
f_p
=
|S|^2-\frac12|\omega|^2
$$

得到：

$$
\boxed{
\|H_p\|_{L^q}
\le
C_q
\left(
\|S\|_{L^{2q}}^2
+
\|\omega\|_{L^{2q}}^2
\right).
}
\tag{9.1}
$$

Riesz operator 是 order zero。

所以：

$$
\boxed{
\text{pressure reconstruction does not create derivative gain}.
}
\tag{9.2}
$$

也不提供 pointwise sign。

換句話說，把：

$$
H_p
$$

正式 X 積分進 state 是合法的：

$$
\boxed{
X_{\rm geom+p}
=
\int_{\rm pressure\ Poisson}
X_{\rm geom}.
}
\tag{9.3}
$$

但是：

$$
\boxed{
\text{legal formation}
\neq
\text{coercive improvement}.
}
$$

---

# 10. Global pressure cancellation

現在出現一個很重要的對照。

對 smooth decaying incompressible field：

$$
\boxed{
\int_{\mathbb R^3}
S:H_p\,dx
=
0.
}
\tag{10.1}
$$

Proof：

因 Hessian symmetric：

$$
S:H_p
=
\partial_j u_i\,
\partial_{ij}p
$$

在 integral 下等價。

積分 by parts：

$$
\int
\partial_j u_i\,
\partial_{ij}p\,dx
=
-
\int
u_i
\partial_i\Delta p\,dx.
$$

再積分：

$$
-
\int
u_i
\partial_i\Delta p\,dx
=
\int
(\nabla\cdot u)
\Delta p\,dx
=
0.
$$

所以 pressure Hessian 在 global $L^2$ strain pairing 中消失。

這解釋了為什麼 global strain-enstrophy identity 可以寫成：

$$
\boxed{
\frac d{dt}
\|S\|_2^2
=
-2\nu
\|\nabla S\|_2^2
-
4
\int
\det S\,dx
}
\tag{10.2}
$$

而沒有顯式 pressure term。

---

# 11. But local spectral projection keeps the pressure channel

對 $\lambda_2$：

$$
e_2^\top H_pe_2
$$

一般不等於零。

所以：

$$
\boxed{
\int S:H_p=0
}
$$

不能推出：

$$
\boxed{
e_2^\top H_pe_2=0.
}
$$

因此 global constraint cancellation 與 local spectral observation 不交換。

用 X 積分語言：

$$
\boxed{
\mathsf I_{\rm global\ pairing}
\circ
\mathsf I_{\rm pressure}
\neq
\mathsf O_{\rm local\ spectrum}
\circ
\mathsf I_{\rm pressure}.
}
\tag{11.1}
$$

更直觀：

- 若先做 global pairing，pressure 被 incompressibility constraint annihilate；
- 若先觀察 local eigenvalue evolution，anisotropic pressure Hessian 保留下來。

這是本輪真正的 **X-order noncommutativity**。

---

# 12. Constraint–Observation Tradeoff

Round 03 的 geometric route 要的是：

$$
\lambda_2,
\quad
\sigma,
\quad
\det S
$$

等 local relational information。

Round 04 顯示：

若保留 local spectrum：

$$
\boxed{
\text{pressure anisotropy survives}.
}
$$

若做 global energy/enstrophy pairing：

$$
\boxed{
\text{pressure disappears},
}
$$

但 local spectral feedback 被壓縮成 global integrated quantities。

因此出現：

$$
\boxed{
\textbf{Constraint–Observation Tradeoff}.
}
\tag{12.1}
$$

其形式為：

$$
\boxed{
\begin{array}{c}
\text{local geometric resolution}
\\
\Downarrow
\\
\text{nonlocal pressure coupling retained}
\end{array}
}
$$

而：

$$
\boxed{
\begin{array}{c}
\text{global incompressible pairing}
\\
\Downarrow
\\
\text{pressure cancellation}
\\
\Downarrow
\\
\text{loss of pointwise spectral feedback}
\end{array}
}
$$

這不是邏輯矛盾。

它表示兩種 observation route 保存不同 invariants。

---

# 13. Evolution of determinant does not close the hierarchy

對 trace-free $3\times3$ matrix：

$$
\operatorname{adj}S
=
S^2
-
\frac12|S|^2I.
$$

因此：

$$
D_t(\det S)
=
\operatorname{adj}S:D_tS.
$$

另一方面：

$$
\Delta(\det S)
=
\operatorname{adj}S:\Delta S
+
\sum_{k=1}^3
D^2(\det)_S
[
\partial_kS,
\partial_kS
].
$$

所以由 (1.3)：

$$
\boxed{
\begin{aligned}
(D_t-\nu\Delta)\det S
={}&
-
\operatorname{adj}S:
\left(
S^2
+
\frac14\omega\otimes\omega
-
\frac14|\omega|^2I
+
H_p
\right)
\\
&-
\nu
\sum_{k=1}^3
D^2(\det)_S
[
\partial_kS,
\partial_kS
].
\end{aligned}
}
\tag{13.1}
$$

因此 determinant evolution 引入：

- pressure Hessian contraction；
- strain-gradient quadratic term；
- vorticity-strain coupling。

沒有 scalar sign closure。

所以從：

$$
\lambda_2
$$

切換到：

$$
\det S
$$

不會消除 pressure/nonlocality problem。

---

# 14. Evolution of vorticity direction

vorticity equation：

$$
D_t\omega
=
S\omega
+
\nu\Delta\omega.
$$

在：

$$
|\omega|>0
$$

區域，令：

$$
\xi
=
\frac{\omega}{|\omega|}.
$$

則：

$$
\boxed{
D_t\xi
=
(I-\xi\otimes\xi)S\xi
+
\frac{\nu}{|\omega|}
(I-\xi\otimes\xi)\Delta\omega.
}
\tag{14.1}
$$

所以 vorticity direction evolution 已依賴：

$$
S\xi
$$

及：

$$
\Delta\omega.
$$

對：

$$
\sigma
=
\xi^\top S\xi
$$

有：

$$
\boxed{
D_t\sigma
=
\xi^\top(D_tS)\xi
+
2(D_t\xi)^\top S\xi.
}
\tag{14.2}
$$

代入 (1.3) 與 (14.1)，必然出現：

$$
\boxed{
-\xi^\top H_p\xi
}
\tag{14.3}
$$

以及 diffusion / higher-gradient terms。

所以：

$$
\boxed{
\sigma
}
$$

同樣不是一個 local finite-dimensional closed scalar state。

---

# 15. Finite local geometry closure fails in the tested class

本輪測試 finite relational local state：

$$
\mathcal G_k(x,t)
=
J^k
\left(
S,\omega
\right)(x,t),
$$

即 strain / vorticity 的某個 finite spatial jet。

對 local spectrum：

$$
\lambda_2,
$$

determinant：

$$
\det S,
$$

alignment：

$$
\sigma,
$$

它們的 exact evolution都會透過：

$$
H_p
=
\nabla^2(-\Delta)^{-1}f_p
$$

接回 global field。

而 Section 4 已證明這個 operator 不是 finite-order local differential operator of $f_p$。

因此，若 closure class 被限制為：

$$
\boxed{
\text{finite local differential functions of }
J^k(S,\omega),
}
$$

則它不能精確包含 pressure Hessian feedback。

所以：

$$
\boxed{
\textbf{
Finite Local Geometry Closure fails for exact NS strain-spectrum evolution.
}
}
\tag{15.1}
$$

這是一個 restricted architecture no-go。

它不排除：

- global integral carriers；
- pseudodifferential carriers；
- nonlocal functionals；
- semigroup formulations；
- Lagrangian global geometry；
- infinite-but-continuous state descriptions。

---

# 16. First continuous constraint barrier

因此 Pure-C route 目前沒有遇到：

$$
\mathsf C\to\mathsf D.
$$

反而先遇到：

$$
\boxed{
\mathsf C_{\rm local}
\to
\mathsf C_{\rm global/nonlocal}.
}
\tag{16.1}
$$

即：

$$
\boxed{
\text{continuous local geometry}
\Longrightarrow
\text{continuous global elliptic constraint}.
}
$$

這是比「連續或離散」更細的 transition：

$$
\boxed{
\textbf{
Local-C}
\to
\textbf{Nonlocal-C}.
}
\tag{16.2}
$$

這個 transition 由 incompressibility pressure constraint 強迫。

---

# 17. STOP-C07 — Local Geometry / Nonlocal Pressure Closure Gap

本輪的主要 X diagnostic：

$$
\boxed{
\bot_X^{\mathrm{C07}}
=
\left\langle
\begin{array}{l}
\text{layer}=\mathrm{geometry\ evolution},\\
\text{local\ state}=
(\lambda_2,\det S,\sigma,J^kS,J^k\omega),\\
\text{required\ carrier}=H_p^{\rm dev},\\
\text{operator}=
\nabla^2(-\Delta)^{-1},\\
\text{local\ finite\ closure}=\mathrm{impossible\ in\ tested\ class},\\
\text{global\ continuous\ closure}=\mathrm{legal},\\
\text{coercivity\ gain}=\mathrm{not\ obtained},\\
\text{discrete\ intrusion}=\mathrm{false}
\end{array}
\right\rangle.
}
\tag{17.1}
$$

命名：

$$
\boxed{
\textbf{STOP-C07:
Local-Geometry / Nonlocal-Pressure Closure Gap}.
}
$$

---

# 18. STOP-C08 — Global cancellation does not imply local feedback control

另一個 diagnostic：

$$
\boxed{
\bot_X^{\mathrm{C08}}
=
\left\langle
\begin{array}{l}
\text{layer}=\mathrm{constraint/observation\ ordering},\\
\text{global\ fact}=
\int S:H_p=0,\\
\text{local\ need}=
e_2^\top H_pe_2,\\
\text{failure}=
\mathrm{global\ cancellation}
\not\Rightarrow
\mathrm{local\ spectral\ sign},\\
\text{repair}=
\mathrm{nonlocal\ relational\ functional\ or\ new\ cancellation},\\
\text{discrete\ intrusion}=\mathrm{false}
\end{array}
\right\rangle.
}
\tag{18.1}
$$

命名：

$$
\boxed{
\textbf{STOP-C08:
Global-Cancellation / Local-Feedback Gap}.
}
$$

---

# 19. 24/72 Ledger — Round 04

| Step | X 積分 / object | $B$ | $U$ | $O$ | $L$ | 狀態 |
|---|---|---|---|---|---|---|
| C29 | $\int_{\nabla u}$ | $\mathsf C$ | $\mathsf S$ | relational | $\mathsf F$ | FORM |
| C30 | $\int_{D_tS}$ | $\mathsf C$ | $\mathsf S$ | relational | $\mathsf F$ | FORM |
| C31 | pressure Poisson | $\mathsf C$ | $\mathsf P$ constraint | $\mathsf X$ | $\mathsf F$ | FORM |
| C32 | $H_p=\nabla^2(-\Delta)^{-1}f_p$ | $\mathsf C$ | global/nonlocal | $\mathsf X$ | $\mathsf F$ | FORM |
| C33 | finite local reconstruction of $H_p$ | $\mathsf C$ | local | local scalar/vector | $\mathsf F$ | REFUTED in finite differential class |
| C34 | exact $\lambda_2$ evolution | $\mathsf C$ | hybrid $\mathsf S/\mathsf P$ | $\mathsf X$ | $\mathsf F$ | FORM on simple spectrum |
| C35 | scalar maximum principle for $\lambda_2$ | $\mathsf C$ | local | scalar | $\mathsf F$ | NOT AVAILABLE |
| C36 | determinant evolution | $\mathsf C$ | hybrid | $\mathsf X$ | $\mathsf F$ | FORM but not closed |
| C37 | alignment evolution | $\mathsf C$ | hybrid | $\mathsf X$ | $\mathsf F$ | FORM but not closed |
| C38 | global $S:H_p$ cancellation | $\mathsf C$ | global pairing | compressed | $\mathsf F$ | FORM |
| C39 | global cancellation $\to$ local pressure sign | $\mathsf C$ | — | local spectrum | $\mathsf F$ | ILLEGAL |
| C40 | unconditional geometry feedback | $\mathsf C$ | hybrid | $\mathsf X$ | $\mathsf F$ | OPEN |

---

# 20. What happened to the original continuous-vs-discrete question?

After four rounds:

$$
\boxed{
T_{\mathsf C\to\mathsf D}
=
\text{NOT YET REACHED}.
}
$$

Instead the route has produced:

$$
\boxed{
\mathsf C_{\rm local}
\to
\mathsf C_{\rm critical}
\to
\mathsf C_{\rm relational}
\to
\mathsf C_{\rm global/nonlocal}.
}
\tag{20.1}
$$

So the continuous route is not exhausted.

It has internally changed its required information architecture.

The actual first hard transition so far is:

$$
\boxed{
\text{local continuum}
\to
\text{globally constrained continuum}.
}
\tag{20.2}
$$

This is directly caused by incompressibility.

---

# 21. Constraint and infinity

The user hypothesis motivating this program emphasized:

$$
\boxed{
\text{constraint}
+
\text{infinity}
+
\text{continuous/discrete}.
}
$$

Round 04 supplies the first precise connection.

The incompressibility constraint:

$$
\nabla\cdot u=0
$$

forces pressure to solve:

$$
-\Delta p=f_p.
$$

The inverse Laplacian:

$$
(-\Delta)^{-1}
$$

couples each point to an unbounded continuum of spatial points.

Thus the constraint does not merely remove one degree of freedom.

It introduces:

$$
\boxed{
\text{a global continuous dependency graph of infinite spatial extent}.
}
\tag{21.1}
$$

This is not a discrete infinity.

It is a continuum nonlocal constraint.

Therefore:

$$
\boxed{
\text{constraint}
\Longrightarrow
\text{nonlocal continuous infinity}
}
\tag{21.2}
$$

already appears before any essential discrete decomposition.

---

# 22. Why this still does not prove blow-up or regularity

Nonlocality alone does not imply failure.

In fact pressure can act as a regularizing redistribution mechanism.

The obstruction is narrower:

$$
\boxed{
\text{we do not yet have a sign/coercivity theorem
for the anisotropic pressure feedback
strong enough to force safe geometry globally}.
}
$$

So the current frontier is not:

> pressure is bad.

It is:

$$
\boxed{
\text{pressure constraint is exact and legal,
but its anisotropic feedback has not yet been converted into a global coercive invariant}.
}
\tag{22.1}
$$

---

# 23. Next round — Pure Continuous Nonlocal Cancellation / Projection Route

Round 04 shows that following local eigenvalues directly keeps the hard pressure channel.

The next continuous route should therefore reverse the order:

instead of trying to control:

$$
e_2^\top H_pe_2
$$

pointwise,

search for global/nonlocal functionals in which pressure or other dangerous terms cancel exactly.

Candidates:

$$
\langle S,H_p\rangle=0,
$$

Miller-type strain/vorticity orthogonality,

Leray projection identities,

nonlocal commutator structures,

Biot–Savart/Riesz cancellations,

global strain–vorticity interaction functionals.

The next X question:

$$
\boxed{
\text{Can a nonlocal continuous X integral preserve enough geometry
while retaining the exact global cancellations?}
}
$$

This is designed to attack the tradeoff:

$$
\boxed{
\text{local geometry}
\leftrightarrow
\text{global cancellation}.
}
$$

If yes, Pure-C continues.

If every such closure eventually requires countable scale extraction / profile decomposition / dyadic localization, that point will finally be recorded as:

$$
\boxed{
T_{\mathsf C\to\mathsf D}.
}
$$

---

# 24. External primary-source anchors

1. Evan Miller, *A regularity criterion for the Navier-Stokes equation involving only the middle eigenvalue of the strain tensor*, arXiv:1710.05569.
   - strain evolution;
   - exact enstrophy/strain identity;
   - middle-eigenvalue regularity criteria.

2. Evan Miller, *On the interaction of strain and vorticity for solutions of the Navier--Stokes equation*, arXiv:2407.02691.
   - strain-vorticity interaction;
   - exact structural identities;
   - global regularity for a related interaction model;
   - advection/depletion analysis.

3. Borys Álvarez-Samaniego, Wilson P. Álvarez-Samaniego, Pedro G. Fernández-Dalgo, *On the use of the Riesz transforms to determine the pressure term in the incompressible Navier-Stokes equations on the whole space*, arXiv:2004.02588.
   - pressure reconstruction by Riesz transforms on the whole space.

4. Laurent Chevillard, Emmanuel Lévêque, Francesco Taddia, Charles Meneveau, Huidan Yu, Carlos Rosales, *Local and nonlocal pressure Hessian effects in real and synthetic fluid turbulence*, arXiv:1106.1046.
   - pressure-Hessian local/nonlocal roles in velocity-gradient dynamics.

---

# 25. Commit state

$$
\boxed{
\begin{aligned}
\text{Route}
&:
\mathrm{Pure\ Continuous\ Geometry\ Evolution},
\\
\text{Essential } \mathsf C\to\mathsf D
&:
\mathrm{Not\ reached},
\\
\text{New transition}
&:
\mathsf C_{\rm local}
\to
\mathsf C_{\rm global/nonlocal},
\\
\text{Update profile}
&:
\mathsf S_{\rm time}
+
\mathsf P_{\rm constraint},
\\
\text{Pressure reconstruction}
&:
\mathrm{exact\ continuous\ nonlocal},
\\
\text{Finite local pressure closure}
&:
\mathrm{refuted\ in\ differential\ class},
\\
\text{Naive }\lambda_2\text{ max principle}
&:
\mathrm{fails\ structurally},
\\
\text{STOP-C07}
&:
\mathrm{Local\ Geometry/Nonlocal\ Pressure\ Gap},
\\
\text{STOP-C08}
&:
\mathrm{Global\ Cancellation/Local\ Feedback\ Gap},
\\
\text{Next}
&:
\mathrm{Pure\ Continuous\ Nonlocal\ Cancellation/Projection}.
\end{aligned}
}
$$
