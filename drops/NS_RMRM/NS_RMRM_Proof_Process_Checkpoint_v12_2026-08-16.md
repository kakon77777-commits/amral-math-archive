# NS × RMRM 證明研究過程 Checkpoint

- 日期：2026-08-16
- 狀態：Research Process Checkpoint
- 格式：UTF-8 Markdown
- canonical math delimiter：inline 使用 `$...$`；display 使用 `$$...$$`
- 目的：保存目前 NS 證明研究的連續過程、已建立結果、條件式結果、已撤回／修正之跳躍，以及下一個唯一 frontier。
- 注意：本文件不是 Navier–Stokes Millennium Problem 的完成證明；任何尚未閉合之處均明確標記為 OPEN / CONDITIONAL / CORRECTED。

---

## 0. 研究狀態總覽

目前已提供並檢視的 NS 主研究系列包括：

- `NS_O`
- `NS_ANP`
- `NS_CSP`
- `NS_DRC`
- `NS_FCBP`
- `NS_CFOP`
- `NS_MORP`

截至 MORP：

$$
\boxed{102+5=107}
$$

即至少 107 份主研究稿。

前六個 Cycle 的整體研究型態，不是 107 個彼此獨立的「快完成證明」，而是持續把 blow-up 相容的合法逃逸機制分類、壓縮、排除，再把剩餘 obstruction 推入更小的 normal form。

概念上：

$$
\Omega_0
\supset
\Omega_1
\supset
\cdots
\supset
\Omega_{107}.
$$

真正的 Navier–Stokes regularity QED 仍要求：

$$
\boxed{
\Omega_\infty=\varnothing.
}
$$

而不能只要求：

$$
\mu(\Omega_t)\to0.
$$

這對應到目前研究中反覆出現的核心原則：

$$
\boxed{
\text{Proof-space contraction}
\neq
\text{Proof-space extinction}.
}
$$

---

# Part I. 前六 Cycle 的壓縮結果

## 1. CSP：殘餘危險機制分類

CSP 將主要 residual dangerous behavior 壓成：

$$
\boxed{
R_{\rm EXP}
\cup
R_{\rm DISS}
\cup
R_{\rm DIL}
\cup
R_{\rm SRC}.
}
$$

但當時仍未證明 residual core 為空。

因此：

$$
\boxed{
\text{分類完}
\neq
\text{排除完}.
}
$$

---

## 2. DRC：Reservoir classification closure 與 Chain Necessity 分離

DRC 得到：

$$
\boxed{
\text{no unexplained DRC reservoir class remains}
}
$$

但明確區分：

$$
\boxed{
\text{Reservoir classification closure}
\neq
\text{Chain Necessity}
}
$$

以及：

$$
\boxed{
\text{Chain Necessity}
\neq
\text{Finite Obstruction}.
}
$$

因此「怪物種類被命名完」並不等於「怪物不存在」。

---

## 3. ANP：Actual causal forest 與 infinite lineage 的量詞缺口

ANP 建立：

$$
\boxed{
CN_{\rm Forest}
}
$$

即在假設有限時間 singular formation 下，得到靠近 singular horizon、跨越無界 singular scales 的 actual causal forest。

但仍保留：

$$
\boxed{
CN3_{\rm Atomic}=\mathrm{OPEN}.
}
$$

這個缺口可抽象成：

$$
\forall n\;\exists P_n
\not\Rightarrow
\exists P_\infty.
$$

即任意深度的 causal forest 不自動推出一條所需的無限 compatible atomic lineage。

---

## 4. CFOP：有限 budget 的可求和問題

在 geometric scale：

$$
R_k\sim2^{-k},
$$

若危險 cascade 每層只支付：

$$
R_k
$$

或：

$$
R_k^{4/3},
$$

則：

$$
\sum_{k=1}^{\infty}2^{-k}<\infty
$$

以及：

$$
\sum_{k=1}^{\infty}2^{-4k/3}<\infty.
$$

因此 cascade 可以無限延伸，但總成本仍有限。

這就是原本 coercive contradiction 無法閉合的核心：

$$
\boxed{
\text{infinite cascade}
+
\text{summable tax}
\not\Rightarrow
\bot.
}
$$

CFOP 因而要求一個新的 forest functional 同時具有：

$$
\boxed{
\begin{aligned}
&\text{universal finite upper bound},\\
&\text{near-critical / non-summable dangerous-cut cost},\\
&\text{branching stability},\\
&\text{fragmentation stability}.
\end{aligned}
}
$$

此問題稱為：

$$
\boxed{
\text{Forest Coercive Budget Problem}.
}
$$

---

## 5. FCBP：四個未閉合模組

FCBP Cycle VI 未得到 unconditional Forest Coercive Budget。

最後被壓成：

$$
\boxed{
XTR\vee UNI\vee RIG\vee SIGN.
}
$$

其中：

$$
\begin{aligned}
XTR &: \text{non-tautological extraction},\\
UNI &: \text{moving-window uniformity},\\
RIG &: \text{invisible-cascade rigidity},\\
SIGN &: \text{paid-side sign/leakage coercivity}.
\end{aligned}
$$

這表示真正難點已從「再找一個 detector」轉成「如何處理極度隱形、仍然 NS-realizable 的 obstruction」。

---

# Part II. MORP：Minimal Obstruction Rigidity Program

MORP 是 Cycle VII，共五篇主稿。

它沒有繼續增加 detector list，而是改採：

$$
\boxed{
\text{coercivity failure}
\Rightarrow
\text{minimal obstruction}
\Rightarrow
\text{rigidity}.
}
$$

---

## 6. MORP-01：Minimal obstruction

從 FCBP 的四缺口轉成：

$$
\boxed{
M\!-\!XTR,\quad
M\!-\!COM,\quad
M\!-\!TR,\quad
M\!-\!RIG.
}
$$

核心思想：

如果最小 obstruction $D_\ast$ 存在，而 admissible transition 不增加 cost，minimality 逼迫：

$$
\Delta(D_\ast)=0.
$$

因此：

$$
\boxed{
\text{minimality}
\Longrightarrow
\text{equality-manifold dynamics}.
}
$$

---

## 7. MORP-02：Compactness carriers

局部 velocity sector：

$$
u_n\to u_\ast
\quad\text{strongly in }L^3_{\mathrm{loc}}.
$$

active pressure sector：

$$
p_n^{act}\to p_\ast^{act}
\quad\text{strongly in }L^{3/2}_{\mathrm{loc}}.
$$

harmonic pressure 以 quotient 保存：

$$
[p_n]_{\mathcal H}
\to
[p_\ast]_{\mathcal H}.
$$

dissipation weak-limit loss 則明確表示為：

$$
\mu_\ast^{diss}
=
|\nabla u_\ast|^2dxdt+\nu_{\rm diss}.
$$

所以 compactness failure 被拆成可被追蹤的 state、pressure、defect carriers，而不是用單一模糊缺口包住。

---

## 8. MORP-03：Return / profile saturation

若 minimal obstruction return，且 depletion 非負，則：

$$
\boxed{
\Delta_{\rm ret}(D_\ast)=0.
}
$$

profile splitting 下，每個 surviving profile 都必須飽和 minimal ratio：

$$
\frac{\mathfrak J(D^{(j)})}{a_j}
=
q_\ast.
$$

即：

$$
\boxed{
\text{arbitrary splitting}
\Longrightarrow
\text{minimal equality splitting}.
}
$$

對 defect-only fixed point，得到 degree-one parabolic homogeneity：

$$
\nu_\ast(\Phi_\lambda(E))
=
\lambda\nu_\ast(E).
$$

並排除 singular center point atom：

$$
\boxed{
\nu_\ast(\{(0,0)\})=0.
}
$$

---

## 9. MORP-04：LEI slack 排除 pure dissipation defect

利用 local energy inequality slack：

$$
\mathscr S_{\rm LEI},
$$

得到：

$$
2\nu\int\phi\,d\nu_{\rm diss}
\le
\mathscr S_{\rm LEI}(u_\ast,p_\ast;\phi).
$$

在 equality manifold 上，若：

$$
\mathscr S_{\rm LEI}=0,
$$

則：

$$
\boxed{
\nu_{\rm diss}=0.
}
$$

因此 pure degree-one dissipation defect branch 被排除。

剩餘：

$$
\boxed{
A\text{-KERNEL}
\vee
E\text{-KERNEL}
\vee
S\text{-KERNEL}.
}
$$

其中 splitting kernel 不再獨立：

$$
S\text{-KERNEL}
\subset
A\text{-KERNEL}\cup E\text{-KERNEL}.
$$

---

## 10. MORP-05：Atomic escape reprofile 與 diffuse carrier

若 space-scale carrier 中存在固定比例 atom：

$$
p_n^{\max}\ge\eta_0>0,
$$

則可重新中心化、重新縮放並再次抽出非零 profile：

$$
\boxed{
\text{atomic escape}
\Rightarrow
\text{reprofile}.
}
$$

因此真正能持續逃逸的 branch 必滿足：

$$
p_n^{\max}\to0.
$$

並推出 multiplicity：

$$
\mathfrak M_n
=
\left(\sum_\alpha e_{n,\alpha}^2\right)^{-1}
\to\infty,
$$

以及 entropy：

$$
\mathfrak H_n
=
-\sum_\alpha e_{n,\alpha}\log e_{n,\alpha}
\to\infty.
$$

ancient branch 若落在適用的 Liouville cut 內則消失；若要存活，必須透過 global spatial tail 失去 compactness。

因此 ancient 與 escape branch 被壓成：

$$
\boxed{
\mathcal K_{\rm diff}
}
$$

即：

$$
\boxed{
\textbf{minimal diffuse carrier}.
}
$$

下一 program：

$$
\boxed{
\text{NS-DCRP}
=
\text{Diffuse Carrier Rigidity Program}.
}
$$

---

# Part III. RMRM：數學家逆向研究矩陣作為研究 Router

RMRM 的目標不是模仿數學家人格，而是把卓越數學研究方法拆成可組合、可路由、可驗證的 research operators。

目前框架包含：

$$
\boxed{
11\text{ cognitive primitives}
+
38\text{ operators}
+
28\text{ dynamics}
}
$$

以及 10 個 phase-aware mathematician fingerprints。

靜態 fingerprint：

$$
m\mapsto\mathfrak F_m
$$

升級為：

$$
\boxed{
(m,t)\mapsto\mathfrak F_m(t).
}
$$

目前主要 transformed-object policies：

| Mode | 主要處理對象 |
|---|---|
| Tao | Obstruction |
| Grothendieck | Relational Structure |
| Ramanujan | Result Seed |
| Erdős | Problem / Obligation |
| Thurston | Manipulable Understanding |
| Mirzakhani | Global Law / Research Hub |
| Gowers | Diagnostic Research State |
| Bourgain | Quantitative Interface |
| Perelman | Closure-Bearing Structure |
| Noether | Structural Carrier / Theorem Architecture |

真正的 composite mathematician 不是：

$$
\text{Tao}+\text{Noether}+\text{Perelman},
$$

而是研究狀態相依的動態路由：

$$
\boxed{
\text{Problem State}
\rightarrow
\text{appropriate methodology}
\rightarrow
\text{new state}
\rightarrow
\text{re-route}.
}
$$

形式上：

$$
\mathcal S_0
\xrightarrow{\text{Noether}}
\mathcal S_1
\xrightarrow{\text{Tao}}
\mathcal S_2
\xrightarrow{\text{Gowers}}
\mathcal S_3
\xrightarrow{\text{Bourgain}}
\mathcal S_4
\xrightarrow{\text{Perelman}}
\mathcal S_5.
$$

並提出研究動作價值函數：

$$
\boxed{
J(a\mid\mathcal S_t)
=
\alpha G_{\mathrm{closure}}
+
\beta\Delta_{\mathrm{frontier}}
+
\gamma G_{\mathrm{transfer}}
-
\lambda\Delta V
-
\mu C_{\mathrm{correlation}}.
}
$$

其中：

$$
G_{\mathrm{closure}}
=
\text{真正靠近全域閉合的增益},
$$

$$
\Delta_{\mathrm{frontier}}
=
\text{合法逃逸空間下降量},
$$

$$
G_{\mathrm{transfer}}
=
\text{可重用的方法增益},
$$

$$
\Delta V
=
\text{新增 verification debt},
$$

$$
C_{\mathrm{correlation}}
=
\text{共同隱藏假設／自洽幻覺風險}.
$$

選擇律：

$$
\boxed{
a_t^\ast
=
\arg\max_a
J(a\mid\mathcal S_t).
}
$$

---

# Part IV. 第一輪 Composite-Mathematician NS 攻擊：UV route

## 11. 初始目標

曾將 MORP frontier 暫時鎖定成：

$$
\boxed{
\mathcal K_{\mathrm{diff}}=\varnothing.
}
$$

並嘗試把 diffuse carrier 直接連到 CKN / $L^3$ critical mass。

這一輪提出過：

$$
\mathcal C(r)
=
\frac1{r^2}
\int_{Q_r(z_\ast)}
\left(
|u|^3+
|p-(p)_{B_r}(t)|^{3/2}
\right)
\,dx\,dt.
$$

以及 singularity 所要求的 one-scale critical non-vanishing。

進一步曾嘗試定義 nested carrier share：

$$
\eta_n
=
\frac{M(r_{n+1})}{M(r_n)},
$$

並由：

$$
M(r)=r^2\mathcal C(r)
$$

推導：

$$
\eta_n
=
\theta^2
\frac{\mathcal C(r_{n+1})}{\mathcal C(r_n)}.
$$

若錯誤地把 MORP diffuse 直接識別成：

$$
\eta_n\to0,
$$

則形式上會得到：

$$
\mathcal C(r_n)\to\infty.
$$

並進一步嘗試推到：

$$
C_u(r_n)\to\infty
$$

以及 local $L^3$ inflation 和 unbounded relative-frequency span。

---

## 12. CORRECTION：MORP diffuse carrier 不可無條件等同於 CKN/$L^3$ carrier

上述 UV route 有一個關鍵識別跳躍：

$$
\boxed{
\text{MORP diffuse carrier}
\not\equiv
\text{CKN / }L^3\text{ critical mass carrier}
}
$$

MORP 的 diffuse carrier 可以位於：

- trace coordinates；
- relative-scale coordinates；
- transition coordinates；
- defect coordinates；
- other native carrier coordinates。

而且 MORP 本身刻意禁止把 dangerous certificate 直接複製成 carrier。

因此不能無條件寫：

$$
p_n^{\max}\to0
\Rightarrow
\eta_n\to0
$$

若 $\eta_n$ 是由 $L^3$ critical mass 定義。

所以「$\mathcal K_{\rm diff}$ 必然等於 UV critical-mass inflation」不保留為已證結果。

狀態：

$$
\boxed{\text{CORRECTED / NOT ESTABLISHED}.}
$$

這一修正非常重要，因為後續證明必須先在 MORP 原生 carrier 與 actual NS state-visible sector 之間建立合法橋接。

---

# Part V. DCRP-01：Singular-Rooted Compactness Rigidity

此後改採更乾淨的路線：

不假設 diffuse carrier 等於 $L^3$ carrier。

只證：

$$
\boxed{
\text{actual singular root}
+
\text{MORP-type compactness}
\Longrightarrow
\text{state-visible sector 不可能消失}.
}
$$

---

## 13. 基本設定

令：

$$
Q_r:=B_r(0)\times(-r^2,0).
$$

考慮 suitable weak solutions：

$$
(u_n,p_n)
$$

定義於 $Q_2$，且對每個 $n$：

$$
(0,0)
$$

皆為 singular point。

假設存在固定：

$$
M<\infty
$$

使：

$$
\sup_n
\left[
\|u_n\|_{L_t^\infty L_x^2(Q_2)}
+
\|\nabla u_n\|_{L^2(Q_2)}
+
\|p_n-(p_n)_{B_2}(t)\|_{L^{3/2}(Q_2)}
\right]
\le M.
\tag{13.1}
$$

這是 compact singular-rooted branch。

---

## 14. Lemma：pressure-free singular $L^3$ lower bound

使用 suitable weak solution 的 one-scale velocity $\varepsilon$-regularity criterion。

對 $p=q=3$：

$$
\frac2p+\frac3q
=
\frac23+1
=
\frac53<2.
$$

存在 universal：

$$
\varepsilon_0>0
$$

使若：

$$
\|u\|_{L^3(Q_1)}
\le\varepsilon_0,
$$

則原點 regular。

故 singularity 強迫：

$$
\|u\|_{L^3(Q_1)}>\varepsilon_0.
$$

縮放：

$$
u^{(r)}(y,s)
=
r\,u(ry,r^2s).
$$

則：

$$
\|u^{(r)}\|_{L^3(Q_1)}^3
=
r^{-2}
\int_{Q_r}|u(x,t)|^3\,dx\,dt.
$$

因此：

$$
\boxed{
r^{-2}\int_{Q_r}|u|^3\,dx\,dt
\ge
\varepsilon_0^3
\qquad
\forall\,0<r<1.
}
\tag{14.1}
$$

這一步完全不依賴 pressure carrier。

---

## 15. Lemma：MORP compactness bound 給 uniform $L^{10/3}$ bound

由：

$$
u_n\in
L_t^\infty L_x^2
\cap
L_t^2H_x^1
$$

以及三維 energy interpolation：

$$
\|u_n\|_{L^{10/3}(Q_{4/3})}
\le C(M).
\tag{15.1}
$$

所以在 $Q_1$：

$$
\boxed{
\int_{Q_1}|u_n|^3
\le C_M^3.
}
\tag{15.2}
$$

---

## 16. Theorem：Fixed-Share Singular Core

固定：

$$
0<\rho<1.
$$

由 singular lower bound：

$$
\int_{Q_\rho}|u_n|^3
\ge
\varepsilon_0^3\rho^2.
$$

而：

$$
\int_{Q_1}|u_n|^3
\le
C_M^3.
$$

故：

$$
\frac{
\int_{Q_\rho}|u_n|^3
}{
\int_{Q_1}|u_n|^3
}
\ge
\frac{\varepsilon_0^3\rho^2}{C_M^3}.
$$

定義：

$$
\eta(M,\rho)
:=
\frac{\varepsilon_0^3\rho^2}{C_M^3}>0.
$$

則：

$$
\boxed{
\frac{
\int_{Q_\rho}|u_n|^3
}{
\int_{Q_1}|u_n|^3
}
\ge
\eta(M,\rho)
>0.
}
\tag{16.1}
$$

意義：

$$
\boxed{
\text{actual singular root}
+
\text{compactness}
\Longrightarrow
\text{state-visible }L^3\text{ sector 永遠保留 fixed positive share}.
}
$$

注意：這不等於宣稱 MORP carrier 本身就是 $|u|^3$ carrier。

---

## 17. Theorem：Singularity survives compact limit

由 compactness 可取子列：

$$
u_n\to u_\ast
\qquad
\text{strongly in }L^3(Q_{4/3}).
\tag{17.1}
$$

對固定 $0<\rho<1$：

$$
\int_{Q_\rho}|u_n|^3
\longrightarrow
\int_{Q_\rho}|u_\ast|^3.
$$

所以：

$$
\boxed{
\rho^{-2}
\int_{Q_\rho}|u_\ast|^3
\ge
\varepsilon_0^3
\qquad
\forall 0<\rho<1.
}
\tag{17.2}
$$

若 $u_\ast$ 在 $(0,0)$ regular，則對某 $K<\infty$：

$$
|u_\ast|\le K
$$

於小 cylinder。

因此：

$$
\int_{Q_\rho}|u_\ast|^3
\le
CK^3\rho^5.
$$

所以：

$$
\rho^{-2}
\int_{Q_\rho}|u_\ast|^3
\le
CK^3\rho^3
\to0,
$$

與 (17.2) 矛盾。

故：

$$
\boxed{
(0,0)\text{ remains singular for }u_\ast.
}
\tag{17.3}
$$

即：

$$
\boxed{
\textbf{Singular-rooted compact limits remain singular.}
}
$$

---

# Part VI. Zero-Tax Actual Return Rigidity

## 18. Local energy setup

取：

$$
\chi\in C_c^\infty(B_1),
\qquad
0\le\chi\le1,
\qquad
\chi\equiv1\text{ on }B_{1/2}.
$$

令：

$$
t_0<t_1<0
$$

為 suitable weak solution 的 good times。

定義：

$$
E_\chi(t)
=
\int_{B_1}|u(x,t)|^2\chi(x)^2\,dx.
$$

local energy interval inequality：

$$
\begin{aligned}
E_\chi(t_1)
+
2\nu
\int_{t_0}^{t_1}
\int
|\nabla u|^2\chi^2
&\le
E_\chi(t_0)\\
&\quad+
\nu
\int_{t_0}^{t_1}\int
|u|^2\Delta(\chi^2)\\
&\quad+
\int_{t_0}^{t_1}\int
(|u|^2+2p)
u\cdot\nabla(\chi^2).
\end{aligned}
\tag{18.1}
$$

定義 nonnegative LEI slack：

$$
\begin{aligned}
\mathscr S_\chi[t_0,t_1]
:={}&
E_\chi(t_0)-E_\chi(t_1)\\
&+
\nu\int|u|^2\Delta(\chi^2)\\
&+
\int(|u|^2+2p)u\cdot\nabla(\chi^2)\\
&-
2\nu\int|\nabla u|^2\chi^2.
\end{aligned}
\tag{18.2}
$$

由 suitability：

$$
\boxed{
\mathscr S_\chi[t_0,t_1]\ge0.
}
\tag{18.3}
$$

---

## 19. Theorem：Zero-Tax Actual Return Rigidity

假設一個 actual same-branch return interval 同時滿足：

### kinetic trace exact return

$$
E_\chi(t_1)=E_\chi(t_0).
\tag{19.1}
$$

### zero localized diffusion leakage

$$
\int_{t_0}^{t_1}\int
|u|^2\Delta(\chi^2)
=0.
\tag{19.2}
$$

### zero nonlinear transport leakage

$$
\int_{t_0}^{t_1}\int
|u|^2u\cdot\nabla(\chi^2)
=0.
\tag{19.3}
$$

### zero pressure leakage

$$
\int_{t_0}^{t_1}\int
2p\,u\cdot\nabla(\chi^2)
=0.
\tag{19.4}
$$

### zero LEI slack

$$
\mathscr S_\chi[t_0,t_1]=0.
\tag{19.5}
$$

將 (19.1)–(19.5) 代入 (18.2)：

$$
0
=
-2\nu
\int_{t_0}^{t_1}\int
|\nabla u|^2\chi^2.
$$

因：

$$
\nu>0
$$

且 integrand 非負：

$$
\boxed{
\int_{t_0}^{t_1}\int
|\nabla u|^2\chi^2=0.
}
\tag{19.6}
$$

所以：

$$
\nabla u=0
$$

幾乎處處於：

$$
B_{1/2}\times(t_0,t_1).
$$

因此對幾乎每個 $t$：

$$
u(x,t)=a(t)
\qquad
x\in B_{1/2}.
$$

在 interior 內代回 Navier–Stokes：

$$
\partial_ta(t)+\nabla p=0,
$$

得到 spatially constant smooth interior flow。

故：

$$
\boxed{
\text{zero-tax exact actual return}
\Longrightarrow
\text{interior regularity}.
}
\tag{19.7}
$$

若此 return interval 同時屬於 singular-rooted recurrent profile，則與 (17.3) 矛盾。

因此：

$$
\boxed{
\textbf{
不存在 singular、compact、state-visible、
zero-leakage、zero-slack 的 exact recurrent return。
}
}
\tag{19.8}
$$

---

# Part VII. 目前最新 Frontier

由 singular-rooted compactness rigidity 與 zero-tax return rigidity：

$$
\boxed{
\begin{aligned}
\text{finite-time singularity}
\Longrightarrow{}&
\text{COMPACTNESS-FAIL}\\
&\vee\text{ACTUAL-RETURN-FAIL}\\
&\vee\text{POSITIVE-RETURN-TAX}.
\end{aligned}
}
\tag{20.1}
$$

其中 positive return tax 至少需要在某個可正確定義之 net / signed / slack accounting 中保留非零成本。

目前可追蹤的 local-energy coordinates 包括：

$$
\boxed{
\begin{aligned}
&|E_\chi(t_1)-E_\chi(t_0)|,\\
&\left|\int|u|^2\Delta\chi^2\right|,\\
&\left|\int|u|^2u\cdot\nabla\chi^2\right|,\\
&\left|\int2pu\cdot\nabla\chi^2\right|,\\
&\mathscr S_\chi[t_0,t_1].
\end{aligned}
}
\tag{20.2}
$$

因此現有 residual frontier 可記為：

$$
\boxed{
\mathcal K_{\rm rem}
=
\mathcal K_{\rm II}
\cup
\mathcal K_{\rm shadow}
\cup
\mathcal K_{\rm tax}.
}
\tag{20.3}
$$

其中：

$$
\mathcal K_{\rm II}
=
\{\text{scale-invariant compactness bound diverges}\},
$$

$$
\mathcal K_{\rm shadow}
=
\{\text{profile recurrence cannot be promoted to actual same-branch recurrence}\},
$$

$$
\mathcal K_{\rm tax}
=
\{\text{actual surviving return must retain nonzero local-energy / flux tax}\}.
$$

---

# Part VIII. 下一個唯一證明目標

下一個真正 closure-bearing 的候選不是新增 detector，而是：

$$
\boxed{
\textbf{Return-Tax Non-Summability Lemma}.
}
$$

理想閉合形式：

先證 infinite singular cascade 的總可用 budget 有有限上界：

$$
\boxed{
\sum_k \Delta_{\rm ret}^{(k)}
<\infty.
}
\tag{21.1}
$$

再證任何 surviving actual return 必支付不可求和下界：

$$
\boxed{
\Delta_{\rm ret}^{(k)}
\ge
c\,\Psi_k,
\qquad
\sum_k\Psi_k=\infty.
}
\tag{21.2}
$$

兩者合併：

$$
\infty
\le
\sum_k\Delta_{\rm ret}^{(k)}
<
\infty,
$$

故：

$$
\boxed{\bot}.
$$

如果此 lemma 對 compact recurrent branch 成立，則 compact recurrent singular mechanism 被完全排除。

---

# Part IX. 目前不得偷換的命題

以下各項目前不得視為已證：

1. 不得把：

$$
\mathcal K_{\rm diff}
$$

直接等同於 $L^3$ / CKN critical carrier。

2. 不得把：

$$
p_n^{\max}\to0
$$

直接翻譯成某個未建立橋接的 physical-space mass ratio：

$$
\eta_n\to0.
$$

3. 不得由：

$$
\text{frontier compression 很快}
$$

推出：

$$
\text{QED 很近}.
$$

4. 不得由：

$$
\forall n\;\exists P_n
$$

推出：

$$
\exists P_\infty.
$$

5. 不得把 profile recurrence 自動當成 actual same-history recurrence。

6. 不得只證「某一項 leakage 非零」就自動得到 positive coercive tax；signed cancellation、scale weight、summability 仍需處理。

7. 不得把 conditional minimal-obstruction argument 描述成 unconditional global regularity theorem。

---

# Part X. 當前研究策略鎖定

下一輪不新增：

- detector family；
- forest taxonomy；
- obstruction name；
- mathematician persona。

只允許攻擊：

$$
\boxed{
\text{Return-Tax Non-Summability}
}
$$

或其必要子引理。

RMRM Router 的優先順序：

$$
\boxed{
\text{Noether}
\rightarrow
\text{Tao}
\rightarrow
\text{Gowers}
\rightarrow
\text{Bourgain}
\rightarrow
\text{Perelman}.
}
$$

具體意義：

- Noether：建立 return-tax 的 intrinsic carrier 與 exact accounting identity。
- Tao：找出最小 surviving tax obstruction。
- Gowers：分解真正會導致 summability failure 的 regimes。
- Bourgain：尋找 scale-critical quantitative lower bound。
- Perelman：檢查 equality case 是否 closure-bearing，是否強迫 regularity / trivial carrier。

最終研究原則：

$$
\boxed{
\text{不要獎勵更多 lemma；
只獎勵 closure-weighted frontier reduction。}
}
$$

---

# End State

目前最新可安全提交給下一個 AI / 本地研究系統的 frontier 為：

$$
\boxed{
\textbf{
Prove or refute the Return-Tax Non-Summability Lemma
for actual singular-rooted recurrent Navier–Stokes branches.
}
}
$$

若失敗，必須精確指出：

$$
\boxed{
\text{finite upper budget}
\quad\text{或}\quad
\text{non-summable lower tax}
}
$$

哪一側無法建立，以及所需的最小額外 hypothesis。

不得以新的 taxonomy 取代此問題。

---

# Checkpoint v2 Update — DCRP-02

# NS-DCRP-02 — Model-Cone Equality Collapse and Return-Ledger Re-Routing

- date: 2026-08-16
- status: research proof checkpoint
- canonical source: UTF-8 Markdown
- math delimiters: `$...$` and `$$...$$`
- objective: continue the Navier–Stokes proof program from MORP/DCRP without adding a new detector taxonomy.
- epistemic policy: every statement below is marked as PROVED / CONDITIONAL / CORRECTED / OPEN where needed.

---

# 1. Executive state

This round changes the closure route.

The previous checkpoint ended with the proposed target

$$
\boxed{
\text{Return-Tax Non-Summability Lemma}.
}
$$

That is no longer the preferred primary target.

Two observations force a re-route.

First, an exact scale-normalized return does not imply equality of the raw physical kinetic energy at the two physical endpoints. Therefore the previous local-energy argument that combined

$$
E_\chi(t_1)=E_\chi(t_0)
$$

with zero leakage and zero slack to force

$$
\nabla u=0
$$

cannot be used for a general scale-normalized return without an additional bridge.

Second, an older internal result already identifies the critical accumulation obstruction: even a fixed positive scale-critical toll can correspond to a geometrically summable raw physical cost.

Therefore the better route is not

$$
\text{many positive tolls}
\Longrightarrow
\infty,
$$

but

$$
\boxed{
\text{minimal return}
\Longrightarrow
\text{exact equality}
\Longrightarrow
\text{rigidity}
\Longrightarrow
\text{triviality}.
}
$$

The main new result of this round is that the MORP-04 model-cone equality law is much more rigid than previously recorded.

Under the stated finite-enstrophy regularity assumptions,

$$
\boxed{
\mathcal R_{SV}=\Delta S
}
$$

does not merely reduce the strain equation.

It forces the strain-gradient energy to vanish, hence the state is spatially affine/rigid and therefore cannot represent a singular Navier–Stokes state.

This is recorded below as the **Model-Cone Equality Collapse Theorem**.

---

# 2. CORRECTION — raw energy return versus normalized return

The three-dimensional Navier–Stokes scaling is

$$
u_\lambda(x,t)
=
\lambda
u(\lambda x,\lambda^2 t).
$$

The raw kinetic energy scales as

$$
\|u_\lambda(t)\|_{L^2_x}^2
=
\lambda^{-1}
\|u(\lambda^2t)\|_{L^2_x}^2.
$$

Therefore equality of two states after canonical parabolic re-normalization does not imply

$$
\|u(t_1)\|_2^2
=
\|u(t_0)\|_2^2
$$

in the original physical variables.

Equivalently, in backward self-similar variables

$$
u(x,t)
=
(-t)^{-1/2}
U(y,s),
$$

$$
y
=
\frac{x}{\sqrt{-t}},
\qquad
s
=
-\log(-t),
$$

the equation acquires dilation terms:

$$
\partial_sU
+
\frac12U
+
\frac12(y\cdot\nabla)U
-
\Delta U
+
(U\cdot\nabla)U
+
\nabla P
=
0.
$$

For a sufficiently decaying global profile, the formal $L^2$ balance becomes

$$
\frac12
\frac d{ds}
\|U\|_2^2
+
\|\nabla U\|_2^2
-
\frac14
\|U\|_2^2
=
0.
$$

Thus a normalized recurrent/periodic orbit can in principle have nonzero viscous dissipation balanced by the dilation contribution.

Accordingly, the previous checkpoint statement

$$
\boxed{
\text{zero-tax exact actual return}
\Longrightarrow
\nabla u=0
}
$$

is retained only for a return for which the **raw physical endpoint local-energy equality** and the stated leakage equalities are independently justified.

It is not valid merely from scale-normalized recurrence.

Status:

$$
\boxed{
\textbf{CORRECTED}.
}
$$

The earlier fixed-share singular-core and compact-limit singularity arguments are not changed by this correction.

---

# 3. Existing no-go — critical toll accumulation does not close the proof

The earlier Cycle-VI internal analysis already contains the following scaling obstruction.

Let

$$
r_n
=
r_0a^{-n},
\qquad
a>1.
$$

Suppose a raw dissipation-type quantity satisfies a fixed critical lower bound

$$
D_n^{crit}
:=
r_n^{-1}D_n
\ge
d_0>0.
$$

Then only

$$
D_n
\ge
d_0r_n
$$

follows.

But

$$
\sum_{n=0}^{\infty}r_n
<
\infty.
$$

Hence

$$
\sum_{n=0}^{\infty}D_n
$$

need not diverge.

Therefore

$$
\boxed{
\text{fixed positive critical toll per geometric scale}
\not\Rightarrow
\text{infinite raw physical cost}.
}
$$

This is the already identified **Critical Barrier Accumulation** no-go.

Consequently, the proposed Return-Tax Non-Summability route is demoted unless one finds a genuinely non-summable quantity rather than merely a scale-critical one.

The stronger strategy is to exploit MORP minimality, because MORP gives an **exact zero-depletion condition at a minimal recurrent obstruction**.

---

# 4. Single-return principle from MORP minimality

MORP-03 uses a native return map

$$
\mathsf T_{\rm ret}
$$

and a nonnegative return depletion

$$
\Delta_{\rm ret}(D)
\ge
0
$$

with the ledger

$$
\mathfrak J(\mathsf T_{\rm ret}D)
+
\Delta_{\rm ret}(D)
\le
\mathfrak J(D).
$$

For a minimal recurrent obstruction

$$
D_\ast,
$$

minimality and recurrence force

$$
\boxed{
\Delta_{\rm ret}(D_\ast)=0.
}
$$

Therefore it is not necessary to prove that infinitely many return taxes have divergent sum if one can find a native nonnegative quantity

$$
\tau(D)
$$

such that

$$
\tau(D)
\le
\Delta_{\rm ret}(D)
$$

and

$$
\tau(D)>0
$$

for every nontrivial singular return.

Then a **single** minimal return yields

$$
0
=
\Delta_{\rm ret}(D_\ast)
\ge
\tau(D_\ast)
>
0,
$$

a contradiction.

This is structurally stronger than geometric-scale accumulation.

The task becomes:

$$
\boxed{
\text{identify a positive-definite equality-breaking coordinate already controlled by the MORP return ledger}.
}
$$

---

# 5. MORP-04 model-cone equality law

Set viscosity

$$
\nu=1.
$$

Let

$$
S
=
\nabla_{\rm sym}u
$$

be the strain tensor and

$$
\omega
=
\nabla\times u.
$$

Define the Miller residual

$$
\boxed{
\mathcal R_{SV}
=
P_{st}
\left(
(u\cdot\nabla)S
+
S^2
+
\frac34\omega\otimes\omega
\right).
}
$$

The exact strain equation can be written as

$$
\boxed{
\partial_tS
-
\Delta S
-
\frac12P_{st}(\omega\otimes\omega)
+
\mathcal R_{SV}
=
0.
}
\tag{5.1}
$$

Miller's $\dot H^1$ strain balance is

$$
\boxed{
\frac12
\frac d{dt}
\|S\|_{\dot H^1}^2
+
\|-\Delta S\|_2^2
=
-
\langle
\mathcal R_{SV},
-\Delta S
\rangle.
}
\tag{5.2}
$$

Define

$$
\chi_{SV}
=
\frac{
\|\mathcal R_{SV}\|_2
}{
\|-\Delta S\|_2
}
$$

when the denominator is nonzero.

MORP-04 Theorem 20.1 proves:

if on a finite interval

$$
[a,b]
$$

one has

$$
S\in L^\infty(a,b;\dot H^1),
$$

the balance is integrable,

$$
\chi_{SV}(t)\le1
$$

a.e., and

$$
\|S(b)\|_{\dot H^1}
=
\|S(a)\|_{\dot H^1},
$$

then a.e. on the nontrivial set

$$
\|-\Delta S\|_2>0
$$

one has

$$
\boxed{
\chi_{SV}=1
}
$$

and

$$
\boxed{
\mathcal R_{SV}
=
\Delta S.
}
\tag{5.3}
$$

Substituting into (5.1) gives

$$
\boxed{
\partial_tS
=
\frac12
P_{st}
(\omega\otimes\omega).
}
\tag{5.4}
$$

MORP-04 recorded (5.3)–(5.4) as an equality-manifold rigidity law.

The next section strengthens this branch to a collapse theorem.

---

# 6. External exact strain identities

For sufficiently regular finite-enstrophy Navier–Stokes solutions on

$$
\mathbb R^3,
$$

the following exact identities hold.

First,

$$
\boxed{
\langle
S,
\omega\otimes\omega
\rangle
=
-4
\int_{\mathbb R^3}
\det S
\,dx.
}
\tag{6.1}
$$

Second, the exact strain/enstrophy growth identity is

$$
\boxed{
\frac d{dt}
\|S\|_2^2
=
-2
\|S\|_{\dot H^1}^2
-
4
\int_{\mathbb R^3}
\det S
\,dx.
}
\tag{6.2}
$$

Because

$$
P_{st}
$$

is the orthogonal projection onto the strain space and

$$
S
$$

already belongs to that space,

$$
\boxed{
\langle
S,
P_{st}(\omega\otimes\omega)
\rangle
=
\langle
S,
\omega\otimes\omega
\rangle.
}
\tag{6.3}
$$

These identities are independently established in the strain formulation of Navier–Stokes and are not MORP-specific.

---

# 7. NEW THEOREM — Model-Cone Equality Collapse

## Theorem 7.1

Let

$$
u
$$

be a sufficiently regular incompressible Navier–Stokes solution on

$$
\mathbb R^3\times(a,b),
$$

with strain

$$
S
=
\nabla_{\rm sym}u.
$$

Assume the pairings below are legitimate; for example it suffices to work in the smooth finite-enstrophy regime with

$$
S(t)\in L^2\cap\dot H^1
$$

and the required higher regularity for almost every

$$
t\in(a,b).
$$

Assume further that on a set of times of full measure in

$$
(a,b)
$$

the MORP model-cone equality law holds:

$$
\boxed{
\mathcal R_{SV}
=
\Delta S.
}
\tag{7.1}
$$

Then

$$
\boxed{
\|S(t)\|_{\dot H^1}=0
}
\tag{7.2}
$$

for almost every

$$
t\in(a,b).
$$

Consequently

$$
S
$$

is spatially constant on each connected spatial component. Under the global finite-enstrophy condition

$$
S(t)\in L^2(\mathbb R^3),
$$

this constant must be zero:

$$
\boxed{
S\equiv0.
}
\tag{7.3}
$$

Even without using the final $L^2$ elimination of the constant, a spatially constant strain produces only an affine smooth velocity field and therefore cannot represent a singular Navier–Stokes state.

### Proof

From (7.1) and the exact strain equation (5.1),

$$
\partial_tS
-
\Delta S
-
\frac12P_{st}(\omega\otimes\omega)
+
\Delta S
=
0.
$$

Hence

$$
\boxed{
\partial_tS
=
\frac12
P_{st}(\omega\otimes\omega).
}
\tag{7.4}
$$

Pair (7.4) with

$$
S.
$$

Using (6.3),

$$
\frac12
\frac d{dt}
\|S\|_2^2
=
\frac12
\langle
S,
\omega\otimes\omega
\rangle.
$$

Therefore

$$
\boxed{
\frac d{dt}
\|S\|_2^2
=
\langle
S,
\omega\otimes\omega
\rangle.
}
\tag{7.5}
$$

Apply (6.1):

$$
\boxed{
\frac d{dt}
\|S\|_2^2
=
-4
\int_{\mathbb R^3}
\det S
\,dx.
}
\tag{7.6}
$$

But the same Navier–Stokes solution simultaneously satisfies the independent exact identity (6.2):

$$
\frac d{dt}
\|S\|_2^2
=
-2
\|S\|_{\dot H^1}^2
-
4
\int_{\mathbb R^3}
\det S
\,dx.
$$

Comparing with (7.6),

$$
-4
\int
\det S
=
-2
\|S\|_{\dot H^1}^2
-
4
\int
\det S.
$$

Hence

$$
2
\|S\|_{\dot H^1}^2
=
0.
$$

Thus

$$
\boxed{
\|S\|_{\dot H^1}=0.
}
$$

Therefore

$$
\nabla S=0
$$

a.e., so

$$
S
$$

is spatially constant.

If

$$
S\in L^2(\mathbb R^3),
$$

the only spatially constant possibility is

$$
S=0.
$$

This proves (7.3).

If additionally

$$
u\in L^2(\mathbb R^3),
$$

then

$$
\nabla_{\rm sym}u=0
$$

forces the global finite-energy rigid motion to vanish, so

$$
u\equiv0.
$$

In either case there is no singular state.

$$
\square
$$

Status:

$$
\boxed{
\textbf{PROVED under the stated regularity / pairing assumptions}.
}
$$

---

# 8. Corollary — finite-enstrophy model-cone return branch is empty

Combine MORP-04 Theorem 20.1 with Theorem 7.1.

Suppose a finite-enstrophy return interval satisfies:

1.

$$
S\in L^\infty(a,b;\dot H^1)
$$

with the exact Miller balance integrable;

2.

$$
\chi_{SV}\le1
$$

a.e.;

3.

$$
\|S(b)\|_{\dot H^1}
=
\|S(a)\|_{\dot H^1};
$$

4. the finite-enstrophy pairings needed in Theorem 7.1 are valid.

Then MORP-04 gives

$$
\mathcal R_{SV}
=
\Delta S,
$$

and Theorem 7.1 gives

$$
\boxed{
S\equiv0
}
$$

in the global finite-enstrophy class.

Therefore:

$$
\boxed{
\textbf{
there is no nontrivial finite-enstrophy Navier–Stokes return
inside the closed Miller model cone with exact endpoint strain-$\dot H^1$ equality.
}
}
\tag{8.1}
$$

For the singularity program this means:

$$
\boxed{
\text{a singular minimal recurrent obstruction cannot live in this branch}.
}
\tag{8.2}
$$

This is stronger than merely saying that the return lies on a rigid equality manifold.

The equality manifold itself collapses.

---

# 9. Consequence for the MORP survivor

MORP-01 minimality forces the minimal invisible obstruction into the common zero-cost kernel

$$
\mathsf O_{\rm PFET}=0,
$$

$$
\mathcal M_{SV}=0,
$$

$$
\widetilde{\mathcal S}^{(3)}=0,
$$

$$
\mathsf{Paid}=0,
$$

and

$$
\mathsf R_{\rm nat}=0.
$$

MORP-04/MORP-05 then reduce state-visible survivors to ancient / escape / transition / diffuse branches not already removed by known Liouville cuts.

Theorem 7.1 removes an additional piece:

$$
\boxed{
\mathcal K_{\rm MC}^{FE}
=
\left\{
\begin{array}{l}
\text{finite-enstrophy state-visible branch},\\
\mathcal R_{SV}=\Delta S
\end{array}
\right\}
}
$$

contains no nontrivial singular state.

Hence any surviving minimal obstruction must evade at least one of the following bridges:

$$
\boxed{
\begin{aligned}
\text{B1: }&
\text{the zero model-cone cost does not upgrade to }
\mathcal R_{SV}=\Delta S;\\
\text{B2: }&
\text{the relevant recurrent/profile state is not finite-enstrophy /
the global pairing is lost};\\
\text{B3: }&
\text{profile recurrence cannot be promoted to an actual return
with the endpoint equality needed by MORP-04};\\
\text{B4: }&
\text{mass escapes through noncompact tails / diffuse coordinates
before the state-visible equality theorem applies}.
\end{aligned}
}
\tag{9.1}
$$

This is a genuine frontier compression because the finite-enstrophy equality branch is no longer an open ancient kernel subclass.

It is empty.

---

# 10. Why the new theorem is closure-relevant

The proof did not introduce a new detector.

It intersected two exact identities that the same Navier–Stokes state must satisfy.

The first identity is produced by the MORP equality manifold:

$$
\mathcal R_{SV}
=
\Delta S
\Longrightarrow
\partial_tS
=
\frac12P_{st}(\omega\otimes\omega).
$$

The second is the exact Navier–Stokes enstrophy/strain law.

These two laws are individually compatible with nontrivial dynamics, but their simultaneous validity forces

$$
\|S\|_{\dot H^1}=0.
$$

Schematically:

$$
\boxed{
\text{MORP equality law}
\cap
\text{exact NS enstrophy law}
=
\text{trivial strain-gradient state}.
}
$$

This is precisely the type of cross-identity rigidity that the RMRM composite route was intended to search for.

---

# 11. New primary proof obligation

The previous primary target

$$
\text{Return-Tax Non-Summability}
$$

is replaced by the sharper bridge problem:

$$
\boxed{
\textbf{Model-Cone-to-Actual-Return Bridge Lemma}.
}
$$

A sufficient form would be:

> Let $D_\ast$ be a minimal singular recurrent MORP obstruction that retains a nontrivial state-visible finite-enstrophy component. If the model-cone excess and all native return depletion vanish, then on some actual return interval the associated strain satisfies
>
> $$
> \chi_{SV}\le1,
> $$
>
> $$
> \|S(b)\|_{\dot H^1}
> =
> \|S(a)\|_{\dot H^1}.
> $$
>
> Hence
>
> $$
> \mathcal R_{SV}
> =
> \Delta S,
> $$
>
> and Theorem 7.1 gives a contradiction.

Thus the next route is no longer:

$$
\text{find an infinite tax}.
$$

It is:

$$
\boxed{
\text{turn the existing zero-cost kernel into an exact equality interval}.
}
$$

If this bridge succeeds, the state-visible finite-enstrophy recurrent branch closes in one return.

If it fails, the failure itself must live in

$$
\boxed{
\text{shadowing}
\vee
\text{normalization mismatch}
\vee
\text{noncompact / infinite-enstrophy escape}.
}
$$

Those are substantially narrower targets than the former general diffuse-carrier problem.

---

# 12. Additional external 2026 cut

A recent 2026 result of Pineau and Vicol gives further independent evidence that self-similar/recurrent Type-I branches are strongly constrained.

Their work on rotated backward self-similar and rotated discretely self-similar solutions proves Liouville-type triviality in substantial Type-I parameter regimes and develops a quantitative weighted-$L^2$ framework.

This does not close the general MORP survivor and is not used in Theorem 7.1.

It is retained only as an external cut:

$$
\boxed{
\text{Type-I + sufficiently rigid self-similar/rotated recurrence}
\Longrightarrow
\text{additional Liouville exclusion in the proven parameter regimes}.
}
$$

The internal Model-Cone Equality Collapse theorem is logically separate.

---

# 13. Current frontier ledger

## Closed in this round

### C1. Previous raw-energy zero-tax return overclaim

Corrected.

### C2. Critical toll accumulation as the primary closure route

Demoted because geometric scaling can make the raw cost summable.

### C3. Finite-enstrophy model-cone equality branch

Closed:

$$
\boxed{
\mathcal R_{SV}=\Delta S
\Longrightarrow
\|S\|_{\dot H^1}=0.
}
$$

Therefore no nontrivial singular state exists in this equality branch.

---

## Still open

### O1. Model-cone equality bridge

Need to derive the exact hypotheses of MORP-04 Theorem 20.1 from the minimal obstruction / return ledger without inserting them by hand.

### O2. Actual-return realization

Need to upgrade profile recurrence to an actual same-history return or prove that failure of this upgrade itself carries a native positive cost.

### O3. Finite-enstrophy transfer

Need to determine whether every state-visible minimal return relevant to the singular branch has enough global or localized compactness to justify the $L^2$ strain pairing used in Theorem 7.1.

### O4. Diffuse noncompact tail

If the branch necessarily leaves finite enstrophy or loses global pairing, the remaining survivor is pushed toward a more precise tail/escape object rather than a generic diffuse carrier.

---

# 14. Next exact attack

The next proof round should attempt the implication

$$
\boxed{
\mathcal M_{SV}(D_\ast)=0
+
\Delta_{\rm ret}(D_\ast)=0
+
\text{state-visible recurrence}
\Longrightarrow
\text{MORP-04 equality hypotheses}.
}
\tag{14.1}
$$

If (14.1) is established with finite-enstrophy transfer, then:

$$
\mathcal M_{SV}=0
+
\Delta_{\rm ret}=0
\Longrightarrow
\mathcal R_{SV}=\Delta S
\Longrightarrow
\|S\|_{\dot H^1}=0
\Longrightarrow
\text{regular/trivial state},
$$

contradicting the nontrivial singular obstruction.

The desired closure chain is therefore now:

$$
\boxed{
\text{minimal singular return}
\Rightarrow
\text{closed model cone + exact return}
\Rightarrow
\mathcal R_{SV}=\Delta S
\Rightarrow
\|S\|_{\dot H^1}=0
\Rightarrow
\bot.
}
\tag{14.2}
$$

No new taxonomy is needed.

The next proof obligation is the first implication.

---

# 15. Source anchors

## Internal sources

1. `NS_MORP_01_MinimalObstruction_Rigidity_v0.1.md`
   - extended obstruction cost
   - zero-cost kernel
   - minimal obstruction setup

2. `NS_MORP_03_Transition_Profile_RigidityEntry_v0.1.md`
   - return map
   - nonnegative return depletion
   - minimal recurrent obstruction implies zero return depletion

3. `NS_MORP_04_EqualityManifold_RigidityAudit_v0.1.md`
   - Theorem 20.1
   - closed Miller model cone
   - equal endpoint strain-$\dot H^1$ norm
   - conclusion
   $$
   \mathcal R_{SV}=\Delta S.
   $$

4. `NS_C6I_CriticalDebt_CapacityInfinity_BarrierCycles_v0.1.md`
   - geometric-scale critical toll can remain raw-summable
   - Critical Barrier Accumulation alone is not enough

## External primary sources

1. Evan Miller, *On the interaction of strain and vorticity for solutions of the Navier--Stokes equation*, arXiv:2407.02691.
   Relevant identities include:
   - strain equation;
   - 
   $$
   \langle S,\omega\otimes\omega\rangle=-4\int\det S;
   $$
   - exact strain/enstrophy growth;
   - Miller residual $\dot H^1$ balance.

2. Ben Pineau and Vlad Vicol, *On rotated backwards self-similar solutions of the incompressible 3D Navier-Stokes equations*, arXiv:2607.09619.
   Used only as an external 2026 Liouville/self-similar comparison cut, not in the proof of Theorem 7.1.

---

# 16. End state

The strongest new statement produced in this round is

$$
\boxed{
\textbf{
Model-Cone Equality Collapse:
\quad
\mathcal R_{SV}=\Delta S
\ \Longrightarrow\
\|S\|_{\dot H^1}=0
}
}
$$

for the stated finite-enstrophy Navier–Stokes class.

The primary frontier is now

$$
\boxed{
\textbf{
prove that a minimal singular actual return is forced onto this equality manifold.
}
}
$$

If that bridge is proved, the finite-enstrophy state-visible recurrent survivor is eliminated without any infinite-scale accumulation argument.

---

# Checkpoint v3 Update — DCRP-03

# NS-DCRP-03 — Logarithmic Model-Cone Debt and Scale-Return Exclusion

- date: 2026-08-16
- status: research proof checkpoint
- canonical source: UTF-8 Markdown
- canonical math delimiters: `$...$` and `$$...$$`
- objective: replace the failed raw-tax accumulation route by a scale-invariant logarithmic cone-debt identity and test it directly against MORP recurrent returns.
- no new detector taxonomy is introduced.
- primary external source: Evan Miller, *On the interaction of strain and vorticity for solutions of the Navier--Stokes equation*, arXiv:2407.02691, v2.

---

# 1. Executive result

The previous checkpoint identified two difficulties:

1. scale-normalized recurrence does not imply raw endpoint kinetic-energy equality;
2. a fixed scale-critical raw toll can remain geometrically summable.

This round resolves both issues at once by using the exact strain balance at the logarithmic level.

Let

$$
S=\nabla_{\rm sym}u,
$$

$$
Q
=
P_{st}
\left(
(u\cdot\nabla)S
+
S^2
+
\frac34\omega\otimes\omega
\right),
$$

and define

$$
H(t)
=
\|S(t)\|_{\dot H^1}^2,
$$

$$
Z(t)
=
\|-\Delta S(t)\|_2.
$$

Miller's exact identity gives

$$
\frac12H'(t)
+
Z(t)^2
=
-
\langle
-\Delta S(t),
Q(t)
\rangle.
$$

Define

$$
\chi(t)
=
\frac{\|Q(t)\|_2}{Z(t)}
$$

when

$$
Z(t)>0.
$$

The new scale-invariant instantaneous cone debt is

$$
\boxed{
\tau_{SV}(t)
=
\frac{
(\chi(t)-1)_+
Z(t)^2
}{
H(t)
}.
}
$$

Equivalently,

$$
\boxed{
\tau_{SV}(t)
=
\frac{
(\|Q(t)\|_2-Z(t))_+
Z(t)
}{
H(t)
}.
}
$$

Then:

$$
\boxed{
\frac12
\frac d{dt}
\log H(t)
\le
\tau_{SV}(t).
}
$$

Consequently:

$$
\boxed{
H(t)
\le
H(t_0)
\exp
\left(
2
\int_{t_0}^{t}
\tau_{SV}(s)\,ds
\right).
}
$$

Therefore every finite-time blowup in the regularity class for which

$$
H(t)\to\infty
$$

must satisfy

$$
\boxed{
\int_{t_0}^{T_{\max}}
\tau_{SV}(t)\,dt
=
+\infty.
}
$$

This quantity is exactly invariant under Navier--Stokes parabolic scaling.

More strongly, if an actual return changes scale by a factor

$$
\lambda>1
$$

and the two endpoint states agree modulo the admissible scaling / translation / rotation symmetries, then

$$
\boxed{
\int_a^b
\tau_{SV}(t)\,dt
\ge
\frac32
\log\lambda.
}
$$

Hence:

$$
\boxed{
\textbf{
a nontrivial scale-changing return can never be a zero model-cone-debt return.
}
}
$$

This directly attacks the MORP discrete renormalization fixed-point branch without requiring raw endpoint equality.

---

# 2. Exact strain balance

For a sufficiently regular incompressible Navier--Stokes solution on

$$
\mathbb R^3,
$$

write

$$
S
=
\nabla_{\rm sym}u
$$

and

$$
\omega
=
\nabla\times u.
$$

Miller writes the exact strain equation as

$$
\boxed{
\partial_tS
-
\Delta S
-
\frac12
P_{st}
(
\omega\otimes\omega
)
+
Q
=
0,
}
\tag{2.1}
$$

where

$$
\boxed{
Q
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
\tag{2.2}
$$

The key orthogonality is

$$
\boxed{
\langle
-\Delta S,
\omega\otimes\omega
\rangle
=
0.
}
\tag{2.3}
$$

Pairing (2.1) with

$$
-\Delta S
$$

therefore yields

$$
\boxed{
\frac12
\frac d{dt}
\|S\|_{\dot H^1}^2
+
\|-\Delta S\|_2^2
=
-
\langle
-\Delta S,
Q
\rangle.
}
\tag{2.4}
$$

This identity is exact.

---

# 3. Definition of logarithmic model-cone debt

Define

$$
H(t)
=
\|S(t)\|_{\dot H^1}^2
$$

and

$$
Z(t)
=
\|-\Delta S(t)\|_2.
$$

On a nontrivial singular branch,

$$
H(t)>0
$$

on a sufficiently late interval; otherwise

$$
S=0
$$

in the corresponding finite-energy strain class and the branch is regular/trivial.

When

$$
Z(t)>0,
$$

define the Miller cone ratio

$$
\chi(t)
=
\frac{
\|Q(t)\|_2
}{
Z(t)
}.
$$

If

$$
Z(t)=0,
$$

set

$$
\tau_{SV}(t)=0.
$$

For

$$
Z(t)>0,
$$

define

$$
\boxed{
\tau_{SV}(t)
=
\frac{
(\chi(t)-1)_+
Z(t)^2
}{
H(t)
}.
}
\tag{3.1}
$$

Because

$$
(\chi-1)_+Z^2
=
(\|Q\|_2-Z)_+Z,
$$

one may equivalently write

$$
\boxed{
\tau_{SV}(t)
=
\frac{
(\|Q(t)\|_2-Z(t))_+
Z(t)
}{
H(t)
}.
}
\tag{3.2}
$$

This is nonnegative.

The associated interval debt is

$$
\boxed{
\mathfrak D_{SV}[a,b]
=
\int_a^b
\tau_{SV}(t)\,dt.
}
\tag{3.3}
$$

---

# 4. Theorem — Logarithmic cone-growth inequality

## Theorem 4.1

Let

$$
u
$$

be a sufficiently regular Navier--Stokes solution on

$$
[a,b]
$$

such that

$$
0<H(t)<\infty
$$

and the quantities in (2.4) are integrable.

Then

$$
\boxed{
\frac12
\frac d{dt}
\log H(t)
\le
\tau_{SV}(t)
}
\tag{4.1}
$$

for almost every

$$
t\in[a,b].
$$

Hence

$$
\boxed{
\frac12
\log
\frac{H(b)}{H(a)}
\le
\mathfrak D_{SV}[a,b].
}
\tag{4.2}
$$

Equivalently,

$$
\boxed{
H(b)
\le
H(a)
\exp
\left(
2\mathfrak D_{SV}[a,b]
\right).
}
\tag{4.3}
$$

### Proof

From (2.4),

$$
\frac12H'
=
-Z^2
-
\langle
-\Delta S,Q
\rangle.
$$

By Cauchy--Schwarz,

$$
-
\langle
-\Delta S,Q
\rangle
\le
Z\|Q\|_2.
$$

Therefore

$$
\frac12H'
\le
-Z^2
+
Z\|Q\|_2.
$$

Thus

$$
\frac12H'
\le
(\chi-1)Z^2.
$$

Since

$$
(\chi-1)Z^2
\le
(\chi-1)_+Z^2,
$$

we obtain

$$
\frac12H'
\le
(\chi-1)_+Z^2.
$$

Divide by

$$
H>0:
$$

$$
\frac12
\frac{H'}{H}
\le
\frac{
(\chi-1)_+Z^2
}{
H
}.
$$

Hence

$$
\frac12
\frac d{dt}
\log H
\le
\tau_{SV}.
$$

Integrating gives (4.2), and exponentiating gives (4.3).

$$
\square
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 5. Corollary — finite logarithmic cone debt is a regularity criterion

Miller records that for a maximal

$$
H^3_{df}
$$

mild Navier--Stokes solution, if

$$
T_{\max}<\infty,
$$

then the subcritical strain norm obeys

$$
\boxed{
\lim_{t\uparrow T_{\max}}
\|S(t)\|_{\dot H^1}
=
+\infty.
}
\tag{5.1}
$$

Therefore Theorem 4.1 immediately gives:

## Corollary 5.1

If for some

$$
t_0<T_{\max}
$$

one has

$$
\boxed{
\int_{t_0}^{T_{\max}}
\tau_{SV}(t)\,dt
<
\infty,
}
\tag{5.2}
$$

then

$$
T_{\max}
$$

cannot be a finite blowup time.

Equivalently, finite-time blowup forces

$$
\boxed{
\int_{t_0}^{T_{\max}}
\tau_{SV}(t)\,dt
=
+\infty
}
\tag{5.3}
$$

for every sufficiently late

$$
t_0<T_{\max}.
$$

### Proof

If (5.2) holds, (4.3) gives a uniform bound

$$
H(t)
\le
H(t_0)
\exp
\left(
2
\int_{t_0}^{T_{\max}}
\tau_{SV}
\right)
<
\infty.
$$

This contradicts (5.1).

$$
\square
$$

Status:

$$
\boxed{
\textbf{PROVED in the stated maximal mild-solution class}.
}
$$

---

# 6. Scale invariance

The Navier--Stokes scaling is

$$
u_\lambda(x,t)
=
\lambda
u(\lambda x,\lambda^2t).
$$

The strain scales as

$$
S_\lambda(x,t)
=
\lambda^2
S(\lambda x,\lambda^2t).
$$

Therefore

$$
H_\lambda(t)
=
\|S_\lambda(t)\|_{\dot H^1}^2
=
\lambda^3
H(\lambda^2t).
\tag{6.1}
$$

Also,

$$
-\Delta S_\lambda
=
\lambda^4
(-\Delta S)(\lambda x,\lambda^2t),
$$

so

$$
Z_\lambda(t)^2
=
\lambda^5
Z(\lambda^2t)^2.
\tag{6.2}
$$

Every term in

$$
Q
$$

has the same pointwise scaling degree as

$$
\Delta S,
$$

hence

$$
\|Q_\lambda(t)\|_2^2
=
\lambda^5
\|Q(\lambda^2t)\|_2^2.
\tag{6.3}
$$

Thus

$$
\boxed{
\chi_\lambda(t)
=
\chi(\lambda^2t).
}
\tag{6.4}
$$

Using (6.1) and (6.2),

$$
\tau_{SV,\lambda}(t)
=
\lambda^2
\tau_{SV}(\lambda^2t).
$$

Therefore

$$
\tau_{SV,\lambda}(t)\,dt
=
\tau_{SV}(s)\,ds,
\qquad
s=\lambda^2t.
$$

Hence:

$$
\boxed{
\mathfrak D_{SV}
\text{ is exactly parabolic-scale invariant}.
}
\tag{6.5}
$$

This is the key improvement over raw dissipation debt.

The earlier geometric-summability obstruction does not apply to

$$
\mathfrak D_{SV},
$$

because the normalization by

$$
H
$$

converts the growth estimate into a logarithmic, dimensionless quantity.

---

# 7. Theorem — Scale-Return Cone Debt

## Theorem 7.1

Let

$$
u
$$

be a sufficiently regular Navier--Stokes solution on an actual physical interval

$$
[a,b].
$$

Assume the endpoint strain states are related by a nontrivial Navier--Stokes parabolic scaling with factor

$$
\lambda>1,
$$

up to translations and orthogonal spatial rotations, which preserve the relevant homogeneous Sobolev norms.

Thus schematically,

$$
S(b)
=
\mathcal G
\mathcal S_\lambda
S(a),
$$

where

$$
\mathcal G
$$

is an allowed norm-preserving Euclidean symmetry and

$$
\mathcal S_\lambda S(x)
=
\lambda^2S(\lambda x).
$$

Then

$$
\boxed{
H(b)
=
\lambda^3H(a).
}
\tag{7.1}
$$

Consequently,

$$
\boxed{
\mathfrak D_{SV}[a,b]
\ge
\frac32
\log\lambda.
}
\tag{7.2}
$$

### Proof

By the scaling law (6.1) and norm preservation of translations/rotations,

$$
H(b)
=
\lambda^3H(a).
$$

Apply Theorem 4.1:

$$
\mathfrak D_{SV}[a,b]
\ge
\frac12
\log
\frac{H(b)}{H(a)}.
$$

Using (7.1),

$$
\mathfrak D_{SV}[a,b]
\ge
\frac12
\log(\lambda^3).
$$

Therefore

$$
\boxed{
\mathfrak D_{SV}[a,b]
\ge
\frac32\log\lambda.
}
$$

$$
\square
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 8. Immediate exclusion — zero-debt nontrivial scale return

If

$$
\lambda>1,
$$

then

$$
\frac32\log\lambda>0.
$$

Therefore Theorem 7.1 gives:

$$
\boxed{
\lambda>1
\Longrightarrow
\mathfrak D_{SV}[a,b]>0.
}
\tag{8.1}
$$

Hence:

$$
\boxed{
\textbf{
there is no nontrivial finite-$\dot H^1$ actual scale-changing return with zero logarithmic model-cone debt.
}
}
\tag{8.2}
$$

This conclusion does not require:

$$
\|S(a)\|_{\dot H^1}
=
\|S(b)\|_{\dot H^1}.
$$

It therefore removes the normalization mismatch that blocked the previous MORP-04 endpoint-equality route.

---

# 9. Variable-scale return orbit

Consider a sequence of actual return times

$$
t_0<t_1<t_2<\cdots<T
$$

with return scale factors

$$
\lambda_k>1
$$

such that

$$
S(t_{k+1})
=
\mathcal G_k
\mathcal S_{\lambda_k}
S(t_k).
$$

Then Theorem 7.1 gives

$$
\mathfrak D_{SV}[t_k,t_{k+1}]
\ge
\frac32
\log\lambda_k.
$$

Summing,

$$
\boxed{
\sum_{k=0}^{N-1}
\mathfrak D_{SV}[t_k,t_{k+1}]
\ge
\frac32
\sum_{k=0}^{N-1}
\log\lambda_k
=
\frac32
\log
\left(
\prod_{k=0}^{N-1}
\lambda_k
\right).
}
\tag{9.1}
$$

If the total renormalization scale diverges,

$$
\prod_{k=0}^{\infty}\lambda_k
=
+\infty,
$$

then

$$
\boxed{
\sum_{k=0}^{\infty}
\mathfrak D_{SV}[t_k,t_{k+1}]
=
+\infty.
}
\tag{9.2}
$$

Thus the non-summability sought in earlier cycles is available in a genuinely scale-invariant logarithmic coordinate.

This does not by itself contradict blowup.

Rather, it proves that a blowup-compatible scale-return orbit must carry infinite model-cone debt and therefore cannot belong to a true zero-debt equality kernel.

---

# 10. Canonical realization of the MORP model-cone excess

MORP-01 introduced

$$
\mathcal M_{SV}(D)
$$

abstractly as a nonnegative lower-semicontinuous candidate channel measuring model-cone excess.

MORP-04 then used the closed model cone

$$
\chi_{SV}\le1
$$

as the corresponding equality regime.

The natural concrete realization on a finite-$\dot H^1$ return cycle is therefore:

$$
\boxed{
\mathcal M_{SV}^{\log}(D;[a,b])
:=
\mathfrak D_{SV}[a,b]
=
\int_a^b
\frac{
(\chi_{SV}-1)_+
\|-\Delta S\|_2^2
}{
\|S\|_{\dot H^1}^2
}
\,dt.
}
\tag{10.1}
$$

It has the required structural features:

1. nonnegative:

$$
\mathcal M_{SV}^{\log}\ge0;
$$

2. vanishes throughout the closed cone:

$$
\chi_{SV}\le1
\quad\Longrightarrow\quad
\mathcal M_{SV}^{\log}=0;
$$

3. exact parabolic scale invariance;

4. detects the minimum excess necessary for scale growth;

5. on an exact scale return:

$$
\boxed{
\mathcal M_{SV}^{\log}
\ge
\frac32\log\lambda.
}
$$

The remaining technical issue is not the analytic inequality.

It is whether

$$
\mathcal M_{SV}^{\log}
$$

is admissible in the precise MORP compactness topology and return package:

- lower semicontinuity;
- passage to profile limits;
- compatibility with actual/profile return realization.

That is a bridge problem.

The return obstruction itself is already quantified.

---

# 11. Conditional MORP closure theorem for an actual recurrent minimizer

## Theorem 11.1

Assume there exists a minimal MORP obstruction

$$
D_\ast
$$

with a finite-$\dot H^1$ state-visible component satisfying all of the following.

### A. Actual return realization

There is an actual same-history return interval

$$
[a,b]
$$

with a scale factor

$$
\lambda>1.
$$

### B. Exact recurrent state relation

The endpoint strain states satisfy

$$
S(b)
=
\mathcal G
\mathcal S_\lambda
S(a).
$$

### C. Model-cone kernel realization

The MORP zero-cost condition

$$
\mathcal M_{SV}(D_\ast)=0
$$

passes to the concrete logarithmic realization:

$$
\mathcal M_{SV}^{\log}(D_\ast;[a,b])=0.
$$

Then no such

$$
D_\ast
$$

exists.

### Proof

By Theorem 7.1,

$$
\mathcal M_{SV}^{\log}(D_\ast;[a,b])
\ge
\frac32
\log\lambda.
$$

Since

$$
\lambda>1,
$$

the right-hand side is strictly positive.

But assumption C gives

$$
\mathcal M_{SV}^{\log}(D_\ast;[a,b])=0.
$$

Contradiction.

$$
\square
$$

Therefore:

$$
\boxed{
\textbf{
the finite-$\dot H^1$ exact scale-recurrent state-visible branch is empty
once the abstract MORP model-cone kernel is legitimately realized by the logarithmic cone debt.
}
}
\tag{11.1}
$$

Status:

$$
\boxed{
\textbf{CONDITIONAL only on the stated MORP bridge assumptions}.
}
$$

The analytic scale-return inequality itself is unconditional in the stated smooth class.

---

# 12. Relationship to the previous Model-Cone Equality Collapse theorem

DCRP-02 proved, under its finite-enstrophy pairing assumptions,

$$
\mathcal R_{SV}
=
\Delta S
\Longrightarrow
\|S\|_{\dot H^1}=0.
$$

That theorem remains useful.

However DCRP-03 is stronger for scale-normalized recurrence because it does not require raw endpoint equality.

The two mechanisms are:

### Equality-collapse route

$$
\chi\le1
+
H(a)=H(b)
\Longrightarrow
\mathcal R_{SV}=\Delta S
\Longrightarrow
\|S\|_{\dot H^1}=0.
$$

### Log-debt route

$$
H(b)=\lambda^3H(a),
\qquad
\lambda>1
$$

directly gives

$$
\mathfrak D_{SV}[a,b]
\ge
\frac32\log\lambda>0.
$$

Thus the second route is naturally adapted to renormalization returns.

---

# 13. What has actually been removed

Before this round, a putative survivor could be described schematically as

$$
\text{finite-$\dot H^1$}
+
\text{scale recurrent}
+
\text{closed / zero-tax model cone}.
$$

That combination is now inconsistent.

The exact excluded conjunction is:

$$
\boxed{
\begin{aligned}
&\text{finite-$\dot H^1$ state-visible return}\\
&+
\text{actual exact parabolic scale return with }\lambda>1\\
&+
\text{zero logarithmic model-cone debt}
\end{aligned}
\Longrightarrow
\bot.
}
\tag{13.1}
$$

Hence a surviving singular recurrent obstruction must fail at least one bridge:

$$
\boxed{
\begin{aligned}
\text{G1: }&
\text{no actual exact scale return is realized};\\
\text{G2: }&
\text{the state-visible return loses finite }\dot H^1;\\
\text{G3: }&
\text{the abstract model-cone kernel does not pass to }
\mathcal M_{SV}^{\log};\\
\text{G4: }&
\text{the recurrence is only profile/shadow recurrence, not same-history recurrence}.
\end{aligned}
}
\tag{13.2}
$$

This is not introduced as a new taxonomy.

It is the explicit list of hypotheses required to block Theorem 11.1.

---

# 14. Stronger global statement — blowup forces infinite logarithmic model-cone excess

For emphasis, the main analytic statement can be written independently of MORP:

## Theorem 14.1

Let

$$
u\in C([0,T_{\max});H^3_{df})
$$

be a maximal mild three-dimensional Navier--Stokes solution.

Define

$$
S=\nabla_{\rm sym}u,
$$

$$
Q
=
P_{st}
\left(
(u\cdot\nabla)S
+
S^2
+
\frac34\omega\otimes\omega
\right),
$$

and

$$
\tau_{SV}
=
\frac{
(\|Q\|_2-\|-\Delta S\|_2)_+
\|-\Delta S\|_2
}{
\|S\|_{\dot H^1}^2
}.
$$

If

$$
T_{\max}<\infty,
$$

then

$$
\boxed{
\int_0^{T_{\max}}
\tau_{SV}(t)\,dt
=
+\infty.
}
\tag{14.1}
$$

More precisely, for every

$$
0<t_0<T_{\max},
$$

$$
\boxed{
\int_{t_0}^{T_{\max}}
\tau_{SV}(t)\,dt
=
+\infty.
}
\tag{14.2}
$$

This is a one-sided refinement of the qualitative threshold

$$
\limsup_{t\uparrow T_{\max}}
\chi_{SV}(t)\ge1.
$$

It does not merely require that the cone ratio touch or exceed one.

It requires the scale-invariant positive excess above one, weighted by

$$
\frac{
\|-\Delta S\|_2^2
}{
\|S\|_{\dot H^1}^2
},
$$

to have infinite total logarithmic debt.

---

# 15. Comparison with Miller's existing perturbative criterion

Miller proves for

$$
0\le\alpha\le1,
\qquad
p=\frac2{1+\alpha},
$$

that finite-time blowup forces divergence of a perturbative integral involving

$$
\frac{
\|Q\|_{\dot H^\alpha}^p
}{
\|S\|_{\dot H^1}^p
}.
$$

For

$$
\alpha=0,
$$

this controls

$$
\int
\frac{
\|Q\|_2^2
}{
\|S\|_{\dot H^1}^2
}
\,dt.
$$

The present cone-debt quantity is different:

$$
\frac{
(\|Q\|_2-Z)_+Z
}{
H
}.
$$

It discards the entire closed-cone region

$$
\|Q\|_2\le Z
$$

and charges only the portion of the perturbation that exceeds the dissipative threshold.

The proof is nevertheless an immediate consequence of the same exact strain balance and Cauchy--Schwarz mechanism.

No priority or novelty claim is made here.

For this project, its value is structural:

$$
\boxed{
\text{it is precisely aligned with the MORP model-cone equality/zero-cost architecture.}
}
$$

---

# 16. Lower-semicontinuity issue

To turn Theorem 11.1 into an unconditional MORP exclusion theorem, one must still show that

$$
\mathcal M_{SV}^{\log}
$$

survives the compactness and profile limits used to produce a minimizer.

The current MORP-02 compactness gives strong local convergence at the state level in

$$
L^3_{\rm loc},
$$

but the logarithmic cone debt contains

$$
\Delta S
$$

and the projected nonlinear residual

$$
Q.
$$

Therefore strong

$$
L^3_{\rm loc}
$$

convergence alone is insufficient to pass (10.1).

A sufficient stronger convergence package would be, on each finite return interval,

$$
S_n\to S
\quad
\text{strongly in }
L^\infty_t\dot H^1_x,
$$

together with

$$
\Delta S_n\to\Delta S
\quad
\text{strongly in }L^2_{t,x},
$$

and

$$
Q_n\to Q
\quad
\text{strongly in }L^2_{t,x}.
$$

Under such a package,

$$
\mathcal M_{SV}^{\log}(D_n)
\to
\mathcal M_{SV}^{\log}(D)
$$

away from the trivial

$$
H=0
$$

branch.

This strong package is not currently proved for the general MORP minimizer.

Hence the next obstruction is no longer an analytic cone-rigidity problem.

It is a compactness / transfer problem for a specific scale-invariant functional.

---

# 17. Next exact proof target

The next proof target is now:

$$
\boxed{
\textbf{Log-Cone Transfer Lemma}.
}
$$

Desired statement:

Let

$$
D_n\to D_\ast
$$

be the MORP minimizing sequence / return-profile convergence in the state-visible finite-$\dot H^1$ branch.

Prove enough compactness or lower-semicontinuity to obtain

$$
\boxed{
\mathcal M_{SV}^{\log}(D_\ast)
\le
\liminf_{n\to\infty}
\mathcal M_{SV}^{\log}(D_n).
}
\tag{17.1}
$$

Then if the minimizing branch has

$$
m_\ast=0
$$

and model-cone kernel saturation,

$$
\mathcal M_{SV}^{\log}(D_\ast)=0.
$$

If the same object is an actual nontrivial scale return with

$$
\lambda>1,
$$

Theorem 7.1 gives

$$
\mathcal M_{SV}^{\log}(D_\ast)
\ge
\frac32\log\lambda>0,
$$

contradiction.

Thus the desired closure chain is:

$$
\boxed{
\begin{aligned}
m_\ast=0
&\Longrightarrow
\mathcal M_{SV}^{\log}(D_\ast)=0\\
&\Longrightarrow
\text{no exact }\lambda>1\text{ state return}\\
&\Longrightarrow
\text{recurrent state-visible minimizer excluded}.
\end{aligned}
}
\tag{17.2}
$$

The only remaining bridge in this chain is the transfer / realization step.

---

# 18. Source verification ledger

The following external facts used above were re-checked against the primary arXiv source:

### Miller strain equation

arXiv:2407.02691v2, equation corresponding to the full strain formulation:

$$
\partial_tS-\Delta S-\frac12P_{st}(\omega\otimes\omega)+Q=0.
$$

### Miller orthogonality identity

$$
\langle-\Delta S,\omega\otimes\omega\rangle=0.
$$

### Exact strain $\dot H^1$ balance

$$
\frac12
\frac d{dt}
\|S\|_{\dot H^1}^2
=
-\|-\Delta S\|_2^2
-
\langle-\Delta S,Q\rangle.
$$

### Blowup continuation fact used by Miller

For a maximal

$$
H^3_{df}
$$

mild solution with

$$
T_{\max}<\infty,
$$

$$
\|S(t)\|_{\dot H^1}\to\infty.
$$

### Miller qualitative model-cone threshold

Finite-time blowup requires

$$
\limsup_{t\uparrow T_{\max}}
\frac{\|Q(t)\|_2}{\|-\Delta S(t)\|_2}
\ge1.
$$

The logarithmic cone-debt theorem in this checkpoint is derived directly from the same exact balance.

---

# 19. End state

The previous frontier was:

$$
\text{Model-Cone-to-Actual-Return Bridge}.
$$

After correcting for scale normalization, the sharper statement is:

$$
\boxed{
\textbf{
Scale-changing recurrence itself forces positive logarithmic cone debt.
}
}
$$

For an exact return factor

$$
\lambda>1,
$$

the mandatory debt is

$$
\boxed{
\mathfrak D_{SV}
\ge
\frac32\log\lambda.
}
$$

For a finite-time blowup,

$$
\boxed{
\mathfrak D_{SV}[t_0,T_{\max})
=
+\infty.
}
$$

The quantity is parabolic-scale invariant.

Thus the old critical-barrier summability obstruction has been bypassed at the analytic level.

The next and only target is:

$$
\boxed{
\textbf{
prove the Log-Cone Transfer Lemma through the MORP compactness/return limit.
}
}
$$

No additional detector family is required.

---

# Checkpoint v4 Update — DCRP-04

# NS-DCRP-04 — Scalar Gain Transfer, Relaxed Return Debt, and the Scale-Gap Boundary

- date: 2026-08-16
- status: research proof checkpoint
- canonical source: UTF-8 Markdown
- canonical math delimiters: `$...$` and `$$...$$`
- objective: continue DCRP-03 by removing the unnecessary high-derivative transfer requirement from the logarithmic cone-debt route.
- no new detector taxonomy is introduced.
- principal internal dependencies: MORP-02, MORP-03, MORP-04, DCRP-03.
- principal external calibration: Evan Miller, arXiv:2407.02691v2; Pineau--Vicol, arXiv:2607.09619v1.

---

# 1. Executive result

DCRP-03 introduced the scale-invariant logarithmic model-cone debt

$$
\mathfrak D_{SV}[a,b]
=
\int_a^b
\tau_{SV}(t)\,dt,
$$

where

$$
\tau_{SV}(t)
=
\frac{
(\chi_{SV}(t)-1)_+
\|-\Delta S(t)\|_2^2
}{
\|S(t)\|_{\dot H^1}^2
},
$$

and proved

$$
\boxed{
\frac12
\log
\frac{
\|S(b)\|_{\dot H^1}^2
}{
\|S(a)\|_{\dot H^1}^2
}
\le
\mathfrak D_{SV}[a,b].
}
\tag{1.1}
$$

The previous checkpoint then formulated a Log-Cone Transfer Lemma involving strong convergence of the high-derivative objects

$$
\Delta S_n
$$

and

$$
Q_n.
$$

That transfer requirement is stronger than necessary.

The key observation is that the right side of the desired scale-return contradiction can be accessed through the scalar endpoint gain

$$
\boxed{
g_{SV}[a,b]
=
\frac{
\|S(b)\|_{\dot H^1}^2
}{
\|S(a)\|_{\dot H^1}^2
}.
}
\tag{1.2}
$$

Equation (1.1) immediately gives

$$
\boxed{
\mathfrak D_{SV}[a,b]
\ge
\frac12
\log g_{SV}[a,b].
}
\tag{1.3}
$$

whenever

$$
g_{SV}\ge1.
$$

For an exact scale return with factor

$$
\lambda>1,
$$

the scaling law gives

$$
g_{SV}=\lambda^3.
$$

Therefore

$$
\boxed{
\mathfrak D_{SV}
\ge
\frac32\log\lambda.
}
\tag{1.4}
$$

The important new point is:

> to transfer this lower bound through a MORP return limit, it is enough to retain the two scalar transition coordinates
>
> $$
> \lambda_n
> $$
>
> and
>
> $$
> g_{SV,n}.
> $$

No strong convergence of

$$
Q_n
$$

or

$$
\Delta S_n
$$

is required.

This reduces the former Log-Cone Transfer Lemma to a scalar compatibility problem.

---

# 2. Exact strain-growth inequality recalled

Let

$$
S=\nabla_{\rm sym}u
$$

and

$$
Q
=
P_{st}
\left(
(u\cdot\nabla)S
+
S^2
+
\frac34\omega\otimes\omega
\right).
$$

Miller's exact identity is

$$
\boxed{
\frac12
\frac d{dt}
\|S\|_{\dot H^1}^2
+
\|-\Delta S\|_2^2
=
-
\langle
-\Delta S,Q
\rangle.
}
\tag{2.1}
$$

Set

$$
H(t)
=
\|S(t)\|_{\dot H^1}^2
$$

and

$$
Z(t)
=
\|-\Delta S(t)\|_2.
$$

Define

$$
\chi_{SV}(t)
=
\frac{\|Q(t)\|_2}{Z(t)}
$$

when

$$
Z(t)>0,
$$

and

$$
\tau_{SV}(t)
=
\frac{
(\chi_{SV}(t)-1)_+Z(t)^2
}{
H(t)
}.
$$

DCRP-03 proved

$$
\boxed{
\frac12
\frac d{dt}
\log H(t)
\le
\tau_{SV}(t)
}
\tag{2.2}
$$

whenever

$$
H(t)>0.
$$

Integrating:

$$
\boxed{
\frac12
\log
\frac{H(b)}{H(a)}
\le
\mathfrak D_{SV}[a,b].
}
\tag{2.3}
$$

This is the only PDE estimate needed for the transfer theorem below.

---

# 3. Definition — scalar strain gain coordinate

For any actual return interval

$$
R=[a,b]
$$

with

$$
0<H(a),H(b)<\infty,
$$

define

$$
\boxed{
g_{SV}(R)
=
\frac{H(b)}{H(a)}.
}
\tag{3.1}
$$

Define the positive logarithmic gain

$$
\boxed{
\Gamma_{SV}(R)
=
\frac12
\left[
\log g_{SV}(R)
\right]_+.
}
\tag{3.2}
$$

Then (2.3) implies

$$
\boxed{
\Gamma_{SV}(R)
\le
\mathfrak D_{SV}(R).
}
\tag{3.3}
$$

Hence

$$
\Gamma_{SV}
$$

is a scalar lower certificate for the full log-cone debt.

It is not a dangerous mark.

It is generated only from the actual endpoint strain norms of one return interval.

---

# 4. Scaling law for the scalar gain

Under Navier--Stokes parabolic scaling,

$$
u_\lambda(x,t)
=
\lambda
u(\lambda x,\lambda^2t),
$$

the strain satisfies

$$
S_\lambda(x,t)
=
\lambda^2
S(\lambda x,\lambda^2t).
$$

Therefore

$$
\|S_\lambda\|_{\dot H^1}^2
=
\lambda^3
\|S\|_{\dot H^1}^2.
$$

Thus if a return interval is exactly related by a scale factor

$$
\lambda>1
$$

up to translations and orthogonal rotations, then

$$
\boxed{
g_{SV}
=
\lambda^3.
}
\tag{4.1}
$$

Consequently

$$
\boxed{
\Gamma_{SV}
=
\frac32\log\lambda.
}
\tag{4.2}
$$

and by (3.3),

$$
\boxed{
\mathfrak D_{SV}
\ge
\frac32\log\lambda.
}
\tag{4.3}
$$

---

# 5. Theorem — Scalar Gain Transfer

## Theorem 5.1

Let

$$
R_n
$$

be a sequence of actual finite-$\dot H^1$ Navier--Stokes return intervals.

Let

$$
\lambda_n>1
$$

be their declared parabolic re-root / return scale factors.

Assume

$$
\lambda_n\to\lambda_\ast
$$

with

$$
\lambda_\ast>1.
$$

Assume only the scalar gain compatibility

$$
\boxed{
g_{SV}(R_n)
\to
\lambda_\ast^3.
}
\tag{5.1}
$$

Then

$$
\boxed{
\liminf_{n\to\infty}
\mathfrak D_{SV}(R_n)
\ge
\frac32
\log\lambda_\ast
>
0.
}
\tag{5.2}
$$

### Proof

For every

$$
n,
$$

equation (3.3) gives

$$
\mathfrak D_{SV}(R_n)
\ge
\frac12
\left[
\log g_{SV}(R_n)
\right]_+.
$$

By (5.1),

$$
g_{SV}(R_n)
\to
\lambda_\ast^3>1.
$$

Therefore for sufficiently large

$$
n,
$$

$$
g_{SV}(R_n)>1,
$$

and hence

$$
\liminf_{n\to\infty}
\mathfrak D_{SV}(R_n)
\ge
\frac12
\lim_{n\to\infty}
\log g_{SV}(R_n).
$$

Thus

$$
\liminf_{n\to\infty}
\mathfrak D_{SV}(R_n)
\ge
\frac12
\log(\lambda_\ast^3)
=
\frac32
\log\lambda_\ast.
$$

Since

$$
\lambda_\ast>1,
$$

the lower bound is strictly positive.

$$
\square
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 6. Why this removes the old high-derivative transfer requirement

DCRP-03 considered proving directly that

$$
\mathcal M_{SV}^{\log}(D_\ast)
\le
\liminf_n
\mathcal M_{SV}^{\log}(D_n)
$$

from convergence of

$$
Q_n
$$

and

$$
\Delta S_n.
$$

Theorem 5.1 shows that this is unnecessary for the fixed-scale return contradiction.

It is enough that the return compactification retain:

$$
\boxed{
(\lambda_n,g_{SV,n})
}
$$

and that at the fixed-point limit,

$$
\boxed{
g_{SV,n}
\to
\lambda_\ast^3.
}
$$

Thus the difficult infinite-dimensional transfer problem

$$
(Q_n,\Delta S_n)
\longrightarrow
(Q_\ast,\Delta S_\ast)
$$

is replaced by the scalar compatibility problem

$$
\boxed{
g_{SV,n}
\longrightarrow
\lambda_\ast^3.
}
$$

This is a strict frontier reduction.

---

# 7. Defect-completed return package

MORP-02 already uses defect completion rather than discarding noncompact coordinates.

Apply the same principle to the return transition.

Augment a normalized return package by the scalar transition metadata

$$
\boxed{
\mathfrak r
=
(
\lambda,
g_{SV}
).
}
\tag{7.1}
$$

More explicitly:

$$
\boxed{
D^{ret}
=
\left(
D_{\rm in},
D_{\rm out},
\lambda,
g_{SV},
\mathcal R^{tr}
\right).
}
\tag{7.2}
$$

The new coordinates are not observation detectors.

They record:

- the geometric re-root factor;
- the actual strain-$\dot H^1$ endpoint gain.

A compactification may retain

$$
\lambda
$$

and

$$
g_{SV}
$$

as extended nonnegative scalars.

If

$$
g_{SV}
$$

does not converge to the scaling-compatible value

$$
\lambda^3,
$$

the mismatch is not hidden.

Define the scale-gain compatibility defect

$$
\boxed{
\delta_{SG}
=
\left|
\log g_{SV}
-
3\log\lambda
\right|
}
\tag{7.3}
$$

whenever both quantities are finite and positive.

For an exact parabolic scale return,

$$
\boxed{
\delta_{SG}=0.
}
\tag{7.4}
$$

---

# 8. Theorem — Relaxed log-debt lower bound

The previous theorem can be expressed without any high-derivative topology.

Let

$$
\mathscr A
$$

denote the set of actual finite-$\dot H^1$ return packages.

Let

$$
\mathfrak T
$$

be any sequential package topology for which the scale coordinate

$$
\lambda
$$

and scalar gain coordinate

$$
g_{SV}
$$

are continuous.

Define the sequential relaxed log-debt by

$$
\boxed{
\overline{\mathfrak D}_{SV}(D)
=
\inf
\left\{
\liminf_{n\to\infty}
\mathfrak D_{SV}(R_n)
:
R_n\in\mathscr A,
\ 
R_n\to D
\right\},
}
\tag{8.1}
$$

with the convention that the infimum over an empty approximation class is

$$
+\infty.
$$

## Theorem 8.1

Suppose

$$
D
$$

belongs to the sequential closure of

$$
\mathscr A
$$

and satisfies

$$
\boxed{
g_{SV}(D)=\lambda(D)^3
}
\tag{8.2}
$$

with

$$
\lambda(D)>1.
$$

Then

$$
\boxed{
\overline{\mathfrak D}_{SV}(D)
\ge
\frac32
\log\lambda(D)
>
0.
}
\tag{8.3}
$$

### Proof

Take any approximating actual-return sequence

$$
R_n\to D.
$$

Continuity of the scalar coordinates gives

$$
\lambda(R_n)\to\lambda(D)
$$

and

$$
g_{SV}(R_n)\to g_{SV}(D)=\lambda(D)^3.
$$

Theorem 5.1 therefore gives

$$
\liminf_n
\mathfrak D_{SV}(R_n)
\ge
\frac32\log\lambda(D).
$$

This lower bound holds for every admissible approximating sequence.

Taking the infimum over all such sequences proves (8.3).

$$
\square
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 9. Kernel-on-the-scale-boundary theorem

Theorem 8.1 immediately gives:

## Corollary 9.1

On the scale-compatible finite-$\dot H^1$ return closure,

$$
\boxed{
\ker
\overline{\mathfrak D}_{SV}
\subseteq
\{
\lambda=1
\}.
}
\tag{9.1}
$$

More precisely, if

$$
\delta_{SG}=0
$$

and

$$
\lambda>1,
$$

then

$$
\overline{\mathfrak D}_{SV}>0.
$$

Therefore a zero relaxed log-debt recurrent profile can survive only by at least one of:

$$
\boxed{
\begin{aligned}
&\lambda\to1,\\
&\delta_{SG}>0,\\
&\text{finite-}\dot H^1\text{ failure},\\
&\text{failure of approximation by actual returns}.
\end{aligned}
}
\tag{9.2}
$$

This is not a new obstruction taxonomy.

It is the exact boundary of the theorem.

---

# 10. Uniform scale-gap corollary

Assume the return rule has a fixed logarithmic scale separation:

$$
\boxed{
\lambda
\ge
\lambda_0
>
1.
}
\tag{10.1}
$$

Then every scale-compatible element of the actual-return closure satisfies

$$
\boxed{
\overline{\mathfrak D}_{SV}
\ge
\frac32
\log\lambda_0
=
c_0
>
0.
}
\tag{10.2}
$$

Thus the zero-cost kernel is empty on that return class.

Schematically:

$$
\boxed{
\text{fixed scale gap}
+
\text{actual-return closure}
+
\text{gain compatibility}
\Longrightarrow
\text{positive model-cone gap}.
}
\tag{10.3}
$$

This is stronger than a non-summability statement.

It is a one-return coercive gap.

---

# 11. Consequence for MORP minimal return rigidity

MORP-03 proves abstractly:

if

$$
D_\ast
$$

is a minimal recurrent obstruction and the nonnegative return depletion ledger holds, then

$$
\boxed{
\Delta_{\rm ret}(D_\ast)=0.
}
\tag{11.1}
$$

MORP-01 also places a zero-cost minimizer in the model-cone kernel.

The present round provides a canonical scalar-completed realization of the state-visible scale-return part of that kernel.

If the recurrent minimizer is approximable by actual finite-$\dot H^1$ returns and satisfies

$$
\delta_{SG}=0,
$$

then any fixed scale factor

$$
\lambda_\ast>1
$$

forces

$$
\boxed{
\overline{\mathfrak D}_{SV}(D_\ast)
\ge
\frac32\log\lambda_\ast
>
0.
}
\tag{11.2}
$$

Therefore:

$$
\boxed{
\textbf{
a zero-cost minimal recurrent state-visible obstruction cannot be a
scale-compatible finite-$\dot H^1$ fixed return with }\lambda_\ast>1.
}
}
\tag{11.3}
$$

This closes the fixed-factor state-visible return branch subject only to the already explicit actual-return / gain-compatibility hypotheses.

---

# 12. What remains of the former Log-Cone Transfer Lemma

The old target required:

$$
Q_n\to Q_\ast
$$

and

$$
\Delta S_n\to\Delta S_\ast
$$

strongly enough to pass the full integral debt.

That target is now demoted.

For fixed-point exclusion it is enough to prove:

$$
\boxed{
\textbf{Scalar Gain Compatibility Lemma}.
}
$$

Desired form:

Let

$$
D_n^{ret}\to D_\ast^{ret}
$$

be a MORP recurrent return sequence converging to a state-visible fixed point with scale factor

$$
\lambda_\ast>1.
$$

Prove either

$$
\boxed{
g_{SV,n}\to\lambda_\ast^3
}
\tag{12.1}
$$

or else retain a nonzero transition defect

$$
\boxed{
\liminf_n
\delta_{SG,n}
>
0.
}
\tag{12.2}
$$

The second alternative is already a failure of exact transition closure and should remain visible in

$$
\mathsf R_{\rm nat}.
$$

Thus the bridge has become scalar.

---

# 13. A compatibility residual that cannot silently disappear

Define

$$
\boxed{
\mathsf R_{SG}(D^{ret})
=
\min
\left\{
1,
\left|
\log g_{SV}
-
3\log\lambda
\right|
\right\}.
}
\tag{13.1}
$$

Then:

$$
\mathsf R_{SG}\ge0,
$$

and exact scale compatibility implies

$$
\mathsf R_{SG}=0.
$$

If the return package topology retains

$$
(\lambda,g_{SV}),
$$

then

$$
\mathsf R_{SG}
$$

is continuous wherever both scalars stay in a compact positive interval.

Therefore a zero-native-residual minimizer satisfying

$$
\mathsf R_{\rm nat}=0
$$

may be refined so that

$$
\boxed{
\mathsf R_{SG}=0.
}
\tag{13.2}
$$

Under this refinement,

$$
\boxed{
g_{SV}=\lambda^3.
}
\tag{13.3}
$$

Thus the exact high-derivative state relation need not be used merely to recover the scalar scaling law.

The cost of losing that law is itself retained as transition residual.

This is consistent with the existing MORP defect-completion principle.

Status:

$$
\boxed{
\textbf{ARCHITECTURAL REFINEMENT; not yet an unconditional NS theorem}.
}
$$

---

# 14. Infinitesimal-return boundary

Corollary 9.1 shows that if a zero-cost recurrent minimizing sequence survives while the scalar gain defect vanishes, then necessarily

$$
\boxed{
\lambda_n\to1.
}
\tag{14.1}
$$

Write the self-similar time period

$$
\boxed{
\mathcal T_n
=
2\log\lambda_n.
}
\tag{14.2}
$$

Then

$$
\lambda_n\to1
$$

is equivalent to

$$
\boxed{
\mathcal T_n\to0.
}
\tag{14.3}
$$

Therefore the only scale-compatible zero-debt boundary is an infinitesimal-period renormalization regime.

This is a substantially sharper normal form than generic diffuse recurrence.

---

# 15. External Liouville cut for small-period DSS

A 2026 primary source by Pineau and Vicol records the following existing result of Chae--Wolf for backwards globally discretely self-similar Navier--Stokes solutions.

For every Type-I constant

$$
C_{U,0}>0,
$$

there exists

$$
\lambda_\ast(C_{U,0})>1
$$

such that a smooth backwards globally

$$
\lambda\text{-DSS}
$$

solution satisfying the corresponding Type-I upper bound is trivial whenever

$$
\boxed{
1<\lambda<\lambda_\ast(C_{U,0}).
}
\tag{15.1}
$$

Thus an actual non-rotated Type-I DSS realization cannot survive the infinitesimal-return boundary

$$
\lambda\to1.
$$

In the rotated discretely self-similar setting, Pineau--Vicol prove analogous triviality when the angular speed is sufficiently small or sufficiently large and the discrete period is sufficiently small relative to the stated parameter regime.

These external theorems do not exclude the full MORP branch because:

- the MORP recurrent object need not yet be an actual global DSS/RDSS solution;
- Type-I control must be established;
- rotated intermediate-angular-speed regimes are not all covered.

Nevertheless, the small-period boundary is not an unconstrained new object.

Large parts of it are already externally Liouville-excluded once actual Type-I DSS/RDSS realization is obtained.

---

# 16. Fixed scale gap versus infinitesimal period

The state-visible recurrent branch is now divided by a theorem, not by a new detector.

### Case A — nondegenerate scale gap

There exists

$$
\lambda_0>1
$$

such that along the recurrent subsequence

$$
\lambda_n\ge\lambda_0.
$$

If scalar gain compatibility holds, then

$$
\boxed{
\overline{\mathfrak D}_{SV}
\ge
\frac32
\log\lambda_0>0.
}
$$

Hence zero model-cone cost is impossible.

### Case B — vanishing scale gap

$$
\lambda_n\to1.
$$

Then

$$
\mathcal T_n=2\log\lambda_n\to0.
$$

Any exact Type-I DSS realization is eventually inside the known small-period Liouville regime and hence trivial.

Thus a surviving zero-cost minimal obstruction in Case B must still fail at least one of:

$$
\boxed{
\text{actual DSS realization},
\qquad
\text{Type-I transfer},
\qquad
\text{unrotated/extreme-rotation Liouville hypotheses}.
}
\tag{16.1}
$$

The scale variable itself is no longer a free escape route.

---

# 17. A conditional closure theorem for the Type-I non-rotated recurrent branch

## Theorem 17.1

Assume a hypothetical singular MORP minimal obstruction produces a sequence of state-visible recurrent return packages

$$
R_n
$$

satisfying:

1. each return is approximable by an actual finite-$\dot H^1$ return;

2. the scale-gain residual vanishes:

$$
\delta_{SG,n}\to0;
$$

3. the model-cone channel is the relaxed log-debt channel, or dominates it on the recurrent class;

4. the limiting recurrent branch is Type-I and non-rotated;

5. profile recurrence upgrades to an actual backwards globally DSS state whenever

$$
\lambda_n\to1.
$$

Then the branch is impossible.

### Proof

There are two cases.

#### Case A

There exists

$$
\lambda_0>1
$$

and a subsequence with

$$
\lambda_n\ge\lambda_0.
$$

By Theorem 8.1 / Corollary 10.1,

$$
\overline{\mathfrak D}_{SV}
\ge
\frac32\log\lambda_0>0,
$$

contradicting zero model-cone cost.

#### Case B

No such scale gap exists.

Then after a subsequence,

$$
\lambda_n\to1.
$$

By assumption 5, the recurrent branch upgrades to an actual Type-I DSS state with a sufficiently small discrete similarity factor.

The Chae--Wolf small-factor Liouville theorem, as restated in Pineau--Vicol Theorem 1.6, gives

$$
U\equiv0.
$$

This contradicts the nontrivial singular obstruction.

Hence both cases are impossible.

$$
\square
$$

Status:

$$
\boxed{
\textbf{CONDITIONAL on the stated actual-realization / Type-I hypotheses}.
}
$$

The importance is that once those pre-existing MORP bridges are supplied, there is no residual scale-factor loophole in the non-rotated Type-I branch.

---

# 18. New strongest internal conclusion

The scalar gain construction gives the following robust statement:

$$
\boxed{
\begin{aligned}
&\text{zero model-cone recurrent cost}\\
&+
\text{actual-return approximability}\\
&+
\text{scale-gain compatibility}
\end{aligned}
}
$$

forces the recurrent scale factor onto the boundary

$$
\boxed{
\lambda=1.
}
\tag{18.1}
$$

Equivalently:

$$
\boxed{
\textbf{
every nontrivial scale-changing recurrent return with }\lambda>1
\textbf{ carries strictly positive relaxed logarithmic cone debt.}
}
\tag{18.2}
$$

This conclusion survives compactification using only two scalar return coordinates.

The full high-derivative cone functional need not pass strongly through the compactness limit.

---

# 19. Updated frontier

The former target

$$
\text{Log-Cone Transfer Lemma}
$$

has been reduced to two sharply separated obligations.

## Frontier A — Scalar Gain Compatibility

Prove from the existing MORP actual-return / residual package that

$$
\boxed{
\mathsf R_{\rm nat}=0
\Longrightarrow
\delta_{SG}=0.
}
\tag{19.1}
$$

Because

$$
\delta_{SG}
$$

is scalar and can be retained explicitly, this is substantially easier than high-derivative functional convergence.

## Frontier B — Infinitesimal Return Realization

If a zero-cost minimizing sequence has

$$
\lambda_n\to1,
$$

prove that the recurrent profile either:

$$
\boxed{
\text{upgrades to an actual small-period DSS/RDSS object}
}
\tag{19.2}
$$

or pays a nonzero shadowing / transition residual.

The non-rotated Type-I actual DSS subcase is already externally excluded for sufficiently small

$$
\lambda-1.
$$

---

# 20. Next exact attack

The next proof round should not return to

$$
Q_n,\Delta S_n
$$

strong convergence.

Instead attack:

$$
\boxed{
\textbf{
Zero Residual}
\Longrightarrow
\textbf{
Scalar Scale-Gain Compatibility}.
}
$$

More concretely:

Given an actual return / re-root package with normalization

$$
\mathsf N_{\rm norm},
$$

write the exact transformation law of

$$
H=\|S\|_{\dot H^1}^2
$$

under every declared normalization component:

- translation;
- rotation;
- parabolic scaling;
- time re-root;
- any amplitude/reference-shell normalization.

Translation and rotation preserve

$$
H.
$$

Parabolic scaling contributes exactly

$$
3\log\lambda
$$

to

$$
\log H.
$$

Therefore any discrepancy

$$
\boxed{
\log g_{SV}-3\log\lambda
}
$$

must come from a declared non-symmetry normalization or from failure of actual return realization.

If the current MORP normalization contains no additional amplitude renormalization acting on the physical state component, then

$$
\boxed{
\delta_{SG}=0
}
$$

is automatic for an exact actual fixed return.

If such an extra normalization is present, its contribution must be explicitly isolated as a transition residual.

This is the next point to audit in the original normalization compiler.

---

# 21. Source ledger

## Internal

- `NS_MORP_02_NativeExtraction_Compactness_v0.1.md`
  - defect-completed package principle;
  - selected trace and scale-escape completion.

- `NS_MORP_03_Transition_Profile_RigidityEntry_v0.1.md`
  - actual versus profile return distinction;
  - return/re-root normalization;
  - minimal return rigidity;
  - conditional fixed-factor discrete renormalization state.

- `NS_MORP_04_EqualityManifold_RigidityAudit_v0.1.md`
  - Miller model-cone equality branch.

- `NS_DCRP_03_LogCone_Debt_ScaleReturn_2026-08-16.md`
  - exact logarithmic cone-growth inequality;
  - scale-invariant log-cone debt;
  - scale-return lower bound.

## External primary sources

### Evan Miller

Evan Miller, *On the interaction of strain and vorticity for solutions of the Navier--Stokes equation*, arXiv:2407.02691v2, revised 2026-04-13.

Used for:

$$
\left<
-\Delta S,
\omega\otimes\omega
\right>
=
0,
$$

the exact strain equation, the exact strain-$\dot H^1$ balance, and model-cone regularity calibration.

### Pineau--Vicol

Ben Pineau and Vlad Vicol, *On rotated backwards self-similar solutions of the incompressible 3D Navier-Stokes equations*, arXiv:2607.09619v1, 2026-07-10.

Used only as external calibration for:

- the relation
  $$
  \mathcal T=2\log\lambda
  $$
  between self-similar period and DSS factor;
- the restatement of the Chae--Wolf small-factor Type-I DSS Liouville theorem;
- the 2026 Type-I RDSS exclusions in small/large angular-speed regimes with sufficiently small period.

No unconditional general DSS/RDSS exclusion is claimed.

---

# 22. End state

The main transfer obstacle has changed.

We no longer need to prove lower semicontinuity of the entire nonlinear high-derivative integral

$$
\mathfrak D_{SV}.
$$

It is enough to retain the scalar endpoint gain

$$
g_{SV}
$$

and scale factor

$$
\lambda.
$$

The rigorous transfer statement is

$$
\boxed{
g_{SV,n}\to\lambda_\ast^3,
\quad
\lambda_\ast>1
\Longrightarrow
\liminf_n
\mathfrak D_{SV}(R_n)
\ge
\frac32\log\lambda_\ast.
}
$$

The relaxed zero-debt kernel therefore lies on

$$
\boxed{
\lambda=1
}
$$

unless scale-gain compatibility or actual-return realization fails.

The next exact target is:

$$
\boxed{
\textbf{
audit the MORP normalization compiler and prove
Zero Native Residual}
\Longrightarrow
\textbf{
Scale-Gain Compatibility}.
}
$$

That is now a finite transformation-law problem rather than an infinite-dimensional compactness problem.

---

# Checkpoint v5 Update — DCRP-05

# NS-DCRP-05 — Transverse Model-Cone Rigidity, Normalization Orientation Audit, and Spectral-Dispersion Boundary

- date: 2026-08-16
- status: research proof checkpoint
- canonical source: UTF-8 Markdown
- canonical math delimiters: `$...$` and `$$...$$`
- objective: audit the MORP normalization compiler, correct scale-orientation ambiguities, and strengthen the Miller model-cone estimate using an exact orthogonality of the Navier--Stokes strain residual.
- no claim of full Navier--Stokes regularity is made.
- principal internal dependencies: MORP-01, MORP-02, MORP-03, MORP-04, DCRP-02, DCRP-03, DCRP-04.
- principal external primary source: Evan Miller, arXiv:2407.02691v2.

---

# 1. Executive result

This round produces three corrections and one new rigidity mechanism.

## Correction A — MORP-04 residual sign

The primary Miller residual is

$$
\boxed{
Q
=
P_{st}
\left(
(u\cdot\nabla)S
+
S^2
+
\frac34\omega\otimes\omega
\right).
}
\tag{1.1}
$$

The MORP-04 Markdown contains one displayed definition with a minus sign in front of

$$
(u\cdot\nabla)S.
$$

That sign is inconsistent with Miller's primary equation and with the exact balance subsequently used.

The canonical residual for all DCRP work is therefore (1.1), with the plus sign.

DCRP-02 and DCRP-03 already used the plus-sign residual.

Status:

$$
\boxed{
\textbf{CORRECTED}.
}
$$

## Correction B — scale orientation

DCRP-04 used the schematic law

$$
g_{SV}=\lambda^3
$$

without first distinguishing:

- the physical concentration factor;
- the scaling parameter actually applied by the normalization map.

That distinction is necessary.

For a forward singular cascade whose physical radius changes from

$$
r
$$

to

$$
r/\Lambda,
\qquad
\Lambda>1,
$$

the relative normalization that maps the smaller later window back to the old normalized chart uses the Navier--Stokes scaling parameter

$$
a=\Lambda^{-1}<1.
$$

Thus an exact normalized fixed return is naturally written

$$
U
\simeq
\mathcal G
\mathcal S_{\Lambda^{-1}}
\mathcal E_\tau U,
$$

not with

$$
\mathcal S_{\Lambda}
$$

if

$$
\Lambda>1
$$

denotes the physical concentration ratio.

The physical endpoint strain gain is then

$$
\boxed{
\frac{
H_{\rm phys,out}
}{
H_{\rm phys,in}
}
=
\Lambda^3.
}
\tag{1.2}
$$

The DCRP-04 positive log-debt formula remains correct when its

$$
\lambda
$$

is interpreted as the physical concentration factor

$$
\Lambda,
$$

rather than the normalization scaling parameter

$$
a.
$$

Status:

$$
\boxed{
\textbf{NOTATION / ORIENTATION CORRECTED}.
}
$$

## New rigidity mechanism

For the exact residual (1.1),

$$
\boxed{
\langle S,Q\rangle_{L^2}=0.
}
\tag{1.3}
$$

This is an exact Navier--Stokes structural identity.

It implies that the Cauchy--Schwarz growth direction used in the Miller cone estimate cannot be perfectly saturated by a nontrivial strain state.

The resulting sharpened cone ratio is

$$
\boxed{
\Theta_{SV}
=
\chi_{SV}
\sqrt{
1-
\beta_{SV}^2
},
}
\tag{1.4}
$$

where

$$
\chi_{SV}
=
\frac{
\|Q\|_2
}{
\|-\Delta S\|_2
}
$$

and

$$
\boxed{
\beta_{SV}
=
\frac{
\|S\|_{\dot H^1}^2
}{
\|S\|_2
\|-\Delta S\|_2
}.
}
\tag{1.5}
$$

The exact strain growth satisfies

$$
\boxed{
\frac12
\frac d{dt}
\|S\|_{\dot H^1}^2
\le
-
\left(
1-\Theta_{SV}
\right)
\|-\Delta S\|_2^2.
}
\tag{1.6}
$$

Hence finite-time blowup in the smooth class forces

$$
\boxed{
\limsup_{t\uparrow T_{\max}}
\Theta_{SV}(t)
\ge1.
}
\tag{1.7}
$$

Because

$$
\Theta_{SV}\le\chi_{SV},
$$

this is strictly stronger than the unrefined cone threshold whenever

$$
\beta_{SV}>0.
$$

The only way to asymptotically recover the old threshold

$$
\chi_{SV}\approx1
$$

is

$$
\boxed{
\beta_{SV}\to0,
}
\tag{1.8}
$$

which is exactly an unbounded spectral-dispersion regime.

Thus the state-visible near-equality branch is pushed directly into a frequency-diffuse normal form.

---

# 2. Normalization compiler audit

MORP-01 states that a general normalization may include:

- spatial translation / centering;
- parabolic scaling;
- pressure constants or harmonic quotient;
- terminal amplitude;
- footprint mass / centroid;
- finite-window time origin.

MORP-03 later defines the actual normalized return by

$$
\mathsf T_{\rm ret}
=
\mathsf N_{\rm norm}
\circ
\mathsf E
$$

and lists:

- recentering;
- parabolic rescaling;
- pressure / harmonic quotient normalization;
- terminal / reference-scale normalization;
- selected-trace normalization.

However, MORP-03 Section 25 gives a more restrictive statement for the **state component** of a fixed return.

It assumes the state relation is generated by:

1. actual Navier--Stokes evolution;
2. parabolic rescaling;
3. normalized time translation;
4. recentering by allowed symmetry.

No independent physical amplitude renormalization is present in that state relation.

This distinction is necessary.

---

# 3. Theorem — rigidity of state-preserving affine normalization

Consider a transformation of the form

$$
v(x,t)
=
A
u(Bx,Ct),
$$

$$
q(x,t)
=
D
p(Bx,Ct),
$$

with positive scalar parameters

$$
A,B,C,D.
$$

Assume that for every sufficiently regular solution

$$
(u,p)
$$

of the fixed-viscosity incompressible Navier--Stokes equation

$$
\partial_tu
-
\nu\Delta u
+
(u\cdot\nabla)u
+
\nabla p
=
0,
$$

the pair

$$
(v,q)
$$

is again a solution of the same equation with the same viscosity

$$
\nu.
$$

Then necessarily

$$
\boxed{
A=B,
\qquad
C=B^2,
\qquad
D=B^2.
}
\tag{3.1}
$$

Thus the only nontrivial scalar amplitude / coordinate renormalization preserving the equation is the standard parabolic Navier--Stokes scaling.

### Proof

Compute:

$$
\partial_tv
=
AC
(\partial_tu)(Bx,Ct),
$$

$$
\Delta v
=
AB^2
(\Delta u)(Bx,Ct),
$$

$$
(v\cdot\nabla)v
=
A^2B
((u\cdot\nabla)u)(Bx,Ct),
$$

and

$$
\nabla q
=
DB
(\nabla p)(Bx,Ct).
$$

For the transformed equation to be a common nonzero multiple of the original Navier--Stokes equation for arbitrary solutions, the four coefficients must agree:

$$
AC
=
AB^2
=
A^2B
=
DB.
$$

Since

$$
A,B>0,
$$

the first equality gives

$$
C=B^2.
$$

The second gives

$$
A=B.
$$

Finally,

$$
DB
=
AB^2
=
B^3,
$$

so

$$
D=B^2.
$$

Therefore the transformation is exactly

$$
v(x,t)
=
B
u(Bx,B^2t),
$$

$$
q(x,t)
=
B^2
p(Bx,B^2t).
$$

$$
\square
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 4. Consequence — terminal amplitude normalization cannot be hidden in the physical state

Suppose an independent terminal-amplitude normalization multiplies the state by

$$
c\ne1
$$

without the coordinated spatial/time transformation required by Theorem 3.1.

Then the transformed field is not, in general, another solution of the same fixed-viscosity Navier--Stokes equation.

Therefore:

$$
\boxed{
\textbf{
any terminal-amplitude normalization used by MORP must either}
}
$$

$$
\boxed{
\begin{aligned}
&\text{act only on diagnostic / carrier coordinates,}\\
&\text{or be absorbed into the unique parabolic NS scaling,}\\
&\text{or else destroy actual NS state realization.}
\end{aligned}
}
\tag{4.1}
$$

This closes the hidden-amplitude ambiguity for an **actual state-visible return**.

It does not prove that every MORP profile return is actually realized.

That shadowing problem remains separate.

---

# 5. Exact forward-window scaling orientation

Let a physical singular-horizon window have radius

$$
r_n
$$

and define the usual normalized state by

$$
u_n(y,s)
=
r_n
u
\left(
x_n+r_ny,
t_n+r_n^2s
\right).
\tag{5.1}
$$

Suppose the next physical window has radius

$$
r_{n+1}
=
\frac{
r_n
}{
\Lambda_n
},
\qquad
\Lambda_n>1.
\tag{5.2}
$$

Relative to the old normalized chart, the later normalization uses the parabolic scaling parameter

$$
\boxed{
a_n
=
\frac{
r_{n+1}
}{
r_n
}
=
\Lambda_n^{-1}.
}
\tag{5.3}
$$

Thus a scale-fixed normalized return has the schematic forward form

$$
\boxed{
U_{n+1}
\simeq
\mathcal G_n
\mathcal S_{\Lambda_n^{-1}}
\mathcal E_{\tau_n}
U_n.
}
\tag{5.4}
$$

If

$$
U_{n+1}\simeq U_n,
$$

then

$$
H(U_n)
=
\Lambda_n^{-3}
H(
\mathcal E_{\tau_n}U_n
),
$$

because

$$
H(
\mathcal S_aV
)
=
a^3H(V).
$$

Therefore the physical evolution segment satisfies

$$
\boxed{
\frac{
H(
\mathcal E_{\tau_n}U_n
)
}{
H(U_n)
}
=
\Lambda_n^3.
}
\tag{5.5}
$$

This is the orientation-safe form of the DCRP-04 scale-gain compatibility law.

---

# 6. Primary Miller residual

For the remainder of this checkpoint define

$$
\boxed{
Q
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
\tag{6.1}
$$

Miller's exact strain equation is

$$
\boxed{
\partial_tS
-
\Delta S
-
\frac12
P_{st}
(
\omega\otimes\omega
)
+
Q
=
0.
}
\tag{6.2}
$$

The primary orthogonality identity is

$$
\boxed{
\langle
-\Delta S,
\omega\otimes\omega
\rangle
=
0.
}
\tag{6.3}
$$

Therefore:

$$
\boxed{
\frac12
\frac d{dt}
\|S\|_{\dot H^1}^2
=
-
\|-\Delta S\|_2^2
-
\langle
-\Delta S,
Q
\rangle.
}
\tag{6.4}
$$

---

# 7. NEW THEOREM — residual-strain orthogonality

## Theorem 7.1

Let

$$
u
$$

be a sufficiently regular divergence-free vector field on

$$
\mathbb R^3
$$

with

$$
S=\nabla_{\rm sym}u
$$

and

$$
\omega=\nabla\times u,
$$

and assume all pairings below are integrable.

Let

$$
Q
$$

be defined by (6.1).

Then

$$
\boxed{
\langle
S,Q
\rangle
=
0.
}
\tag{7.1}
$$

### Proof

Because

$$
S
$$

lies in the strain space and

$$
P_{st}
$$

is the orthogonal projection onto that space,

$$
\langle
S,Q
\rangle
=
\left<
S,
(u\cdot\nabla)S
+
S^2
+
\frac34
\omega\otimes\omega
\right>.
$$

Since

$$
\nabla\cdot u=0,
$$

the transport contribution vanishes:

$$
\left<
S,
(u\cdot\nabla)S
\right>
=
\frac12
\int_{\mathbb R^3}
u\cdot\nabla
|S|^2
\,dx
=
0.
$$

For a trace-free

$$
3\times3
$$

matrix,

$$
\operatorname{tr}(S^3)
=
3\det S.
$$

Hence

$$
\langle
S,S^2
\rangle
=
3
\int
\det S.
$$

Miller's Proposition 1.1 gives

$$
\langle
S,
\omega\otimes\omega
\rangle
=
-4
\int
\det S.
$$

Therefore

$$
\left<
S,
S^2
+
\frac34
\omega\otimes\omega
\right>
=
3
\int\det S
-
3
\int\det S
=
0.
$$

Combining the transport and algebraic terms:

$$
\boxed{
\langle S,Q\rangle=0.
}
$$

$$
\square
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 8. Immediate repair / simplification of DCRP-02

DCRP-02 proved a Model-Cone Equality Collapse theorem under the equality relation

$$
Q=\Delta S.
$$

Theorem 7.1 gives a shorter proof.

If

$$
Q=\Delta S,
$$

then

$$
0
=
\langle S,Q\rangle
=
\langle S,\Delta S\rangle
=
-
\|S\|_{\dot H^1}^2.
$$

Hence

$$
\boxed{
\|S\|_{\dot H^1}=0.
}
\tag{8.1}
$$

Thus:

$$
\boxed{
Q=\Delta S
\Longrightarrow
\text{spatially constant strain}.
}
\tag{8.2}
$$

In the global finite-enstrophy class,

$$
S\in L^2(\mathbb R^3),
$$

this gives

$$
S=0.
$$

Therefore the DCRP-02 equality-collapse conclusion is retained, but the proof is simplified and no comparison of two enstrophy identities is required.

---

# 9. Orthogonal projection of the dissipation direction

Set

$$
z
=
-\Delta S.
$$

Define

$$
E
=
\|S\|_2^2,
$$

$$
H
=
\|S\|_{\dot H^1}^2
=
\langle
S,z
\rangle,
$$

and

$$
Z
=
\|z\|_2.
$$

Assume

$$
E>0.
$$

Decompose

$$
z
=
\frac{H}{E}S
+
z_\perp,
$$

with

$$
\langle
S,z_\perp
\rangle
=
0.
$$

Then

$$
\|z_\perp\|_2^2
=
Z^2
-
\frac{
H^2
}{
E
}.
$$

By Theorem 7.1,

$$
Q\perp S.
$$

Therefore

$$
\langle
z,Q
\rangle
=
\langle
z_\perp,Q
\rangle.
$$

Cauchy--Schwarz now gives the strictly improved estimate

$$
\boxed{
-
\langle
z,Q
\rangle
\le
\sqrt{
Z^2-\frac{H^2}{E}
}
\,
\|Q\|_2.
}
\tag{9.1}
$$

The usual Miller cone estimate replaces the square-root factor by

$$
Z.
$$

The improvement is exact and comes solely from

$$
Q\perp S.
$$

---

# 10. Definition — spectral transversality parameter

Define

$$
\boxed{
\beta_{SV}
=
\frac{
H
}{
\sqrt E\,Z
}.
}
\tag{10.1}
$$

By Cauchy--Schwarz,

$$
0\le
\beta_{SV}
\le1.
$$

When

$$
H>0,
$$

one has

$$
\beta_{SV}>0.
$$

Also define the ordinary Miller ratio

$$
\boxed{
\chi_{SV}
=
\frac{
\|Q\|_2
}{
Z
}.
}
\tag{10.2}
$$

Then (9.1) becomes

$$
\boxed{
-
\langle
z,Q
\rangle
\le
Z^2
\chi_{SV}
\sqrt{
1-\beta_{SV}^2
}.
}
\tag{10.3}
$$

Define the **transverse cone ratio**

$$
\boxed{
\Theta_{SV}
=
\chi_{SV}
\sqrt{
1-\beta_{SV}^2
}.
}
\tag{10.4}
$$

Since

$$
0\le
\sqrt{
1-\beta_{SV}^2
}
\le1,
$$

$$
\boxed{
\Theta_{SV}\le\chi_{SV}.
}
\tag{10.5}
$$

---

# 11. NEW THEOREM — transverse cone growth inequality

## Theorem 11.1

For every sufficiently regular nontrivial Navier--Stokes strain state for which the quantities above are finite,

$$
\boxed{
\frac12
H'
\le
-
\left(
1-\Theta_{SV}
\right)
Z^2.
}
\tag{11.1}
$$

### Proof

The exact strain balance (6.4) gives

$$
\frac12H'
=
-Z^2
-
\langle
z,Q
\rangle.
$$

Apply (10.3):

$$
\frac12H'
\le
-Z^2
+
Z^2
\Theta_{SV}.
$$

Hence

$$
\boxed{
\frac12H'
\le
-
(1-\Theta_{SV})Z^2.
}
$$

$$
\square
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 12. Corollary — strengthened blowup threshold

If

$$
\Theta_{SV}(t)\le1
$$

on a time interval, then

$$
H(t)
$$

is nonincreasing there.

For a maximal

$$
H^3_{df}
$$

mild solution, Miller uses the standard fact that finite-time blowup implies

$$
H(t)
=
\|S(t)\|_{\dot H^1}^2
\to\infty.
$$

Therefore:

$$
\boxed{
T_{\max}<\infty
\Longrightarrow
\limsup_{t\uparrow T_{\max}}
\Theta_{SV}(t)
\ge1.
}
\tag{12.1}
$$

Equivalently,

$$
\boxed{
\limsup_{t\uparrow T_{\max}}
\left[
\frac{
\|Q(t)\|_2
}{
\|-\Delta S(t)\|_2
}
\sqrt{
1-
\frac{
\|S(t)\|_{\dot H^1}^4
}{
\|S(t)\|_2^2
\|-\Delta S(t)\|_2^2
}
}
\right]
\ge1.
}
\tag{12.2}
$$

Because

$$
\Theta_{SV}\le\chi_{SV},
$$

this implies the older qualitative threshold

$$
\limsup\chi_{SV}\ge1,
$$

but is more restrictive whenever the spectral transversality factor does not vanish.

No priority / novelty claim is made here.

The inequality is a direct structural corollary of Miller's exact identities.

---

# 13. Quantitative gap away from spectral diffusion

Suppose for all sufficiently late times

$$
\boxed{
\beta_{SV}(t)
\ge
\beta_0
>
0.
}
\tag{13.1}
$$

Then finite-time blowup requires

$$
\Theta_{SV}\ge1
$$

along a sequence.

Therefore

$$
\chi_{SV}
\sqrt{
1-\beta_0^2
}
\ge1
$$

along that sequence, so

$$
\boxed{
\limsup_{t\uparrow T_{\max}}
\chi_{SV}(t)
\ge
\frac{
1
}{
\sqrt{
1-\beta_0^2
}
}
>
1.
}
\tag{13.2}
$$

Hence a blowup sequence satisfying

$$
\chi_{SV}\to1
$$

must obey

$$
\boxed{
\beta_{SV}\to0.
}
\tag{13.3}
$$

This is the first direct bridge from near model-cone equality to spectral diffusion.

---

# 14. NEW THEOREM — transverse logarithmic cone debt

Define

$$
\boxed{
\tau_{\perp}(t)
=
\frac{
(\Theta_{SV}(t)-1)_+
Z(t)^2
}{
H(t)
}.
}
\tag{14.1}
$$

Then Theorem 11.1 implies

$$
\boxed{
\frac12
\frac d{dt}
\log H(t)
\le
\tau_{\perp}(t).
}
\tag{14.2}
$$

Therefore

$$
\boxed{
H(t)
\le
H(t_0)
\exp
\left(
2
\int_{t_0}^{t}
\tau_{\perp}(s)\,ds
\right).
}
\tag{14.3}
$$

Consequently, finite-time blowup forces

$$
\boxed{
\int_{t_0}^{T_{\max}}
\tau_{\perp}(t)\,dt
=
+\infty.
}
\tag{14.4}
$$

for every sufficiently late

$$
t_0.
$$

Because

$$
\Theta_{SV}\le\chi_{SV},
$$

$$
\boxed{
\tau_{\perp}
\le
\tau_{SV}.
}
\tag{14.5}
$$

Thus (14.4) is a strictly sharper necessary divergence statement than DCRP-03 whenever

$$
\beta_{SV}
$$

is non-negligible.

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 15. Growth-time quantitative excess

Suppose at some time

$$
H'(t)\ge0.
$$

Then Theorem 11.1 gives

$$
\Theta_{SV}\ge1.
$$

Hence

$$
\chi_{SV}
\ge
\frac1{
\sqrt{
1-\beta_{SV}^2
}
}.
$$

Therefore

$$
\chi_{SV}-1
\ge
\frac1{
\sqrt{
1-\beta_{SV}^2
}
}
-
1.
$$

For

$$
0\le x<1,
$$

$$
\frac1{\sqrt{1-x}}-1
\ge
\frac x2.
$$

Taking

$$
x=\beta_{SV}^2,
$$

we obtain

$$
\boxed{
\chi_{SV}-1
\ge
\frac12
\beta_{SV}^2
}
\tag{15.1}
$$

at every nondecreasing-

$$
H
$$

time.

Since

$$
\beta_{SV}^2
=
\frac{
H^2
}{
EZ^2
},
$$

the DCRP-03 cone debt satisfies

$$
\tau_{SV}
=
\frac{
(\chi_{SV}-1)_+Z^2
}{
H
}
\ge
\frac12
\frac{
H
}{
E
}
$$

whenever

$$
H'\ge0.
$$

Thus:

$$
\boxed{
H'(t)\ge0
\Longrightarrow
\tau_{SV}(t)
\ge
\frac12
\frac{
\|S(t)\|_{\dot H^1}^2
}{
\|S(t)\|_2^2
}.
}
\tag{15.2}
$$

This gives an explicit positive model-cone excess at every nontrivial strain-growth time.

---

# 16. Spectral meaning of $\beta_{SV}$

Let

$$
\widehat S(\xi)
$$

be the Fourier transform of the strain.

Define the probability measure

$$
\boxed{
d\mu_S(\xi)
=
\frac{
|\widehat S(\xi)|^2
}{
E
}
\,d\xi.
}
\tag{16.1}
$$

Let the random variable

$$
X(\xi)=|\xi|^2.
$$

Then

$$
\mathbb E_{\mu_S}[X]
=
\frac HE,
$$

and

$$
\mathbb E_{\mu_S}[X^2]
=
\frac{
Z^2
}{
E
}.
$$

Therefore

$$
\boxed{
\beta_{SV}^2
=
\frac{
\left(
\mathbb E[X]
\right)^2
}{
\mathbb E[X^2]
}.
}
\tag{16.2}
$$

Equivalently,

$$
\boxed{
\frac{
\operatorname{Var}(X)
}{
\left(
\mathbb E[X]
\right)^2
}
=
\beta_{SV}^{-2}-1.
}
\tag{16.3}
$$

Hence:

$$
\boxed{
\beta_{SV}\to0
}
$$

if and only if the coefficient of variation of the strain frequency-squared distribution diverges.

This is not merely qualitative "high frequency".

It is a precise **spectral dispersion / moment-separation condition**.

---

# 17. Bounded-band lower bound

Suppose

$$
\widehat S
$$

is supported in a frequency annulus

$$
m
\le
|\xi|^2
\le
M
$$

with

$$
0<m\le M<\infty.
$$

Then

$$
X^2\le MX.
$$

Therefore

$$
\mathbb E[X^2]
\le
M\mathbb E[X].
$$

Also

$$
\mathbb E[X]\ge m.
$$

Hence

$$
\beta_{SV}^2
=
\frac{
(\mathbb E[X])^2
}{
\mathbb E[X^2]
}
\ge
\frac{
\mathbb E[X]
}{
M
}
\ge
\frac mM.
$$

Thus:

$$
\boxed{
\beta_{SV}
\ge
\sqrt{
\frac mM
}.
}
\tag{17.1}
$$

For a dyadic relative-frequency band

$$
2^{j-K}
\lesssim
|\xi|
\lesssim
2^{j+K},
$$

one obtains schematically

$$
\boxed{
\beta_{SV}
\gtrsim
2^{-2K}.
}
\tag{17.2}
$$

Therefore:

$$
\boxed{
\beta_{SV}\to0
\Longrightarrow
\text{no uniformly bounded relative-frequency band can carry the full strain spectrum}.
}
\tag{17.3}
$$

This is a rigorous state-visible route from cone near-saturation to unbounded relative-frequency span.

---

# 18. Connection to MORP-02 scale compactification

MORP-02 retains a relative-frequency probability measure

$$
\sigma_n^{sc}
$$

based on selected-time shell carrier mass.

Its weak-star compactification detects a positive amount of base carrier mass escaping to

$$
\infty.
$$

However, the parameter

$$
\beta_{SV}
$$

depends on the ratio of the first and second

$$
|\xi|^2
$$

moments.

Weak convergence of base probability measures does not by itself control those moments.

Example:

$$
\mu_n
=
\left(
1-\frac1n
\right)
\delta_1
+
\frac1n
\delta_{n^2}.
$$

Then

$$
\mu_n
\rightharpoonup
\delta_1,
$$

so no positive base mass remains at infinity in the weak limit.

But

$$
\mathbb E_{\mu_n}[X]
\sim
n,
$$

and

$$
\mathbb E_{\mu_n}[X^2]
\sim
n^3,
$$

so

$$
\beta_n^2
\sim
\frac1n
\to0.
$$

Thus:

$$
\boxed{
\textbf{
vanishing-mass ultraviolet tails can destroy transverse rigidity
without appearing as positive weak scale-defect mass.
}
}
\tag{18.1}
$$

This identifies a precise compactness issue:

$$
\boxed{
\text{moment uniform integrability}.
}
\tag{18.2}
$$

The remaining scale-diffuse survivor is therefore sharper than ordinary weak carrier escape.

It is a possible **high-moment UV defect**.

---

# 19. State-visible cone-kernel exclusion with bounded spectral dispersion

Suppose a hypothetical recurrent state-visible branch satisfies all of:

1.

$$
0<E,H,Z<\infty;
$$

2. the Miller closed cone:

$$
\chi_{SV}\le1;
$$

3. a nontrivial strain state:

$$
H>0.
$$

Then because

$$
\beta_{SV}>0,
$$

$$
\Theta_{SV}
=
\chi_{SV}
\sqrt{1-\beta_{SV}^2}
<
1.
$$

Theorem 11.1 gives

$$
\boxed{
H'<0
}
\tag{19.1}
$$

whenever

$$
Z>0.
$$

Therefore an actual forward concentrating return with physical endpoint gain

$$
H_{\rm out}
=
\Lambda^3H_{\rm in},
\qquad
\Lambda>1,
$$

cannot remain inside the closed Miller cone for the entire return interval.

Equivalently:

$$
\boxed{
\textbf{
every nontrivial forward scale-concentrating return must leave the closed Miller cone on a set of positive dynamical effect.
}
}
\tag{19.2}
$$

This conclusion is independent of the old equal-endpoint assumption.

---

# 20. Fixed-return consequence after normalization audit

Assume an actual same-history forward return shrinks physical scale by

$$
\Lambda>1.
$$

By Sections 3--5, if the state normalization preserves the fixed-viscosity Navier--Stokes equation, then its physical state action is symmetry-only plus the unique parabolic scaling

$$
\mathcal S_{\Lambda^{-1}}.
$$

If the normalized state returns to the same state modulo rotations/translations, then

$$
H_{\rm phys,out}
=
\Lambda^3H_{\rm phys,in}.
$$

Therefore:

$$
\boxed{
\frac12
\log
\frac{
H_{\rm phys,out}
}{
H_{\rm phys,in}
}
=
\frac32
\log\Lambda
>
0.
}
\tag{20.1}
$$

DCRP-03 then gives

$$
\boxed{
\mathfrak D_{SV}
\ge
\frac32
\log\Lambda.
}
\tag{20.2}
$$

The present transverse refinement gives the stronger necessary debt

$$
\boxed{
\int
\tau_{\perp}
\,dt
\ge
\frac32
\log\Lambda.
}
\tag{20.3}
$$

Thus any exact forward scale-return state must carry positive **transverse** cone debt.

If a MORP equality kernel is defined so that its actual return interval has zero transverse cone debt, the fixed-return branch is immediately impossible.

The remaining issue is whether the current abstract

$$
\mathcal M_{SV}=0
$$

and

$$
\Delta_{\rm ret}=0
$$

already imply zero interval transverse debt.

That implication is not yet present in the original corpus.

---

# 21. Exact status of the normalization frontier

The normalization audit gives:

$$
\boxed{
\text{independent state-amplitude normalization}
\Longrightarrow
\text{not an exact NS symmetry}.
}
$$

Therefore the state-visible actual-return compiler has only two legitimate possibilities.

### State-symmetry branch

The state normalization is:

$$
\boxed{
\text{translation}
+
\text{rotation}
+
\text{time re-root}
+
\text{parabolic NS scaling}.
}
$$

Then scale-gain compatibility is exact once the concentration/scaling orientation is declared.

### Diagnostic-normalization branch

Terminal amplitude, footprint mass, selected-trace normalization, etc. act only on non-state package coordinates.

They do not alter the physical state scaling law.

Thus the hidden-amplitude issue is closed for actual state realization.

What remains open is not amplitude compatibility.

It is:

$$
\boxed{
\text{profile return}
\Longrightarrow
\text{actual same-history return}.
}
$$

---

# 22. New frontier after transverse rigidity

The state-visible near-model-cone branch now has a sharp dichotomy.

If

$$
\beta_{SV}
\ge\beta_0>0,
$$

then the blowup cone threshold has a uniform strict gap:

$$
\chi_{SV}
\ge
\frac1{
\sqrt{1-\beta_0^2}
}
>
1
$$

along a blowup sequence.

If instead the model-cone ratio approaches the old boundary:

$$
\chi_{SV}\downarrow1,
$$

then necessarily

$$
\boxed{
\beta_{SV}\to0.
}
$$

By Section 16 this means:

$$
\boxed{
\frac{
\operatorname{Var}_{\mu_S}(|\xi|^2)
}{
\mathbb E_{\mu_S}[|\xi|^2]^2
}
\to\infty.
}
\tag{22.1}
$$

Thus the remaining equality-boundary survivor is no longer generic diffuse carrier.

It is specifically:

$$
\boxed{
\textbf{
unbounded strain spectral-moment dispersion.
}
}
\tag{22.2}
$$

---

# 23. Next exact proof target

The next attack should focus on the one remaining state-visible route:

$$
\boxed{
\beta_{SV}\to0.
}
$$

The most useful target is a **Moment-Reprofile Lemma**.

Desired form:

> If a normalized singular-return sequence has
>
> $$
> \beta_{SV,n}\to0,
> $$
>
> then either:
>
> 1. a positive fraction of an appropriate derivative-weighted carrier can be re-centered/re-scaled into a nonzero state-visible profile; or
> 2. the high-moment tail produces a strictly positive native transition / splitting tax.

The key difference from MORP-05 is that the relevant carrier should be weighted strongly enough to see the moment leakage hidden by

$$
\sigma_n^{sc}
\rightharpoonup
\sigma_\ast^{sc}.
$$

A natural derivative-weighted probability measure is

$$
\boxed{
d\nu_H(\xi)
=
\frac{
|\xi|^2
|\widehat S(\xi)|^2
}{
H
}
\,d\xi.
}
\tag{23.1}
$$

or, for the next moment,

$$
\boxed{
d\nu_Z(\xi)
=
\frac{
|\xi|^4
|\widehat S(\xi)|^2
}{
Z^2
}
\,d\xi.
}
\tag{23.2}
$$

These are not yet inserted into the MORP cost.

They are proposed as proof coordinates for the next reprofile argument.

The next theorem should first test whether

$$
\beta_{SV}\to0
$$

forces a nontrivial separation between

$$
\nu_H
$$

and

$$
\nu_Z
$$

that can be converted into an actual profile.

---

# 24. Source audit

## Internal source findings

### MORP-01

The general symmetry-normalization list includes a possible `terminal amplitude` normalization.

This is too broad to be treated automatically as a physical-state symmetry.

### MORP-03

The actual state component of a fixed return is separately described using:

- Navier--Stokes evolution;
- parabolic scaling;
- time translation;
- recentering.

This is compatible with Theorem 3.1.

Its displayed fixed-return relation is schematic and does not unambiguously distinguish physical concentration factor from normalization scaling parameter.

DCRP-05 resolves this by using:

$$
\Lambda>1
$$

for physical concentration and

$$
a=\Lambda^{-1}
$$

for the relative normalization scale.

### MORP-04

One displayed residual definition contains the wrong sign on the advection term relative to Miller's primary formula.

All canonical DCRP work now uses (6.1).

---

## External primary source

Evan Miller, *On the interaction of strain and vorticity for solutions of the Navier--Stokes equation*, arXiv:2407.02691v2.

Primary facts used:

$$
Q
=
P_{st}
\left(
(u\cdot\nabla)S
+
S^2
+
\frac34\omega\otimes\omega
\right),
$$

$$
\partial_tS
-
\Delta S
-
\frac12P_{st}(\omega\otimes\omega)
+
Q
=
0,
$$

$$
\langle
-\Delta S,
\omega\otimes\omega
\rangle
=
0,
$$

$$
\frac12
\frac d{dt}
\|S\|_{\dot H^1}^2
=
-
\|-\Delta S\|_2^2
-
\langle
-\Delta S,Q
\rangle,
$$

and Proposition 1.1:

$$
\langle
S,
\omega\otimes\omega
\rangle
=
-4
\int\det S
=
-\frac43
\langle
S^2,S
\rangle.
$$

The identity

$$
\langle S,Q\rangle=0
$$

is derived in this checkpoint from these exact primary identities plus incompressible transport cancellation.

No novelty / priority claim is made.

---

# 25. End state

This round closes the normalization-amplitude ambiguity for actual state-visible returns and strengthens the model-cone geometry.

The main exact new identities are:

$$
\boxed{
\langle S,Q\rangle=0,
}
$$

and

$$
\boxed{
\frac12
\frac d{dt}
\|S\|_{\dot H^1}^2
\le
-
\left[
1-
\chi_{SV}
\sqrt{
1-\beta_{SV}^2
}
\right]
\|-\Delta S\|_2^2.
}
$$

Finite-time blowup therefore requires:

$$
\boxed{
\limsup
\chi_{SV}
\sqrt{
1-\beta_{SV}^2
}
\ge1.
}
$$

Near the old Miller boundary

$$
\chi_{SV}\to1,
$$

one must have

$$
\boxed{
\beta_{SV}\to0,
}
$$

which is exactly unbounded spectral-moment dispersion.

The next proof target is no longer generic scale diffusion.

It is:

$$
\boxed{
\textbf{
Moment-Reprofile Lemma for }
\beta_{SV}\to0.
}
$$

That is the next single frontier.

---

# Checkpoint v6 Update — DCRP-06

# NS-DCRP-06 — Spectral-Moment Separation, Hellinger Rigidity, and the Derivative-Carrier Boundary

- date: 2026-08-16
- status: research proof checkpoint
- canonical source: UTF-8 Markdown
- canonical math delimiters: `$...$` and `$$...$$`
- objective: attack the DCRP-05 frontier $\beta_{SV}\to0$ and determine exactly what kind of frequency reprofile it forces.
- no full Navier--Stokes regularity claim is made.
- primary external source checked: Evan Miller, arXiv:2407.02691v2, especially Theorems 1.8, 1.9, 1.12, 1.13 and Proposition 1.1.

---

# 1. Executive result

DCRP-05 reduced near-saturation of the old Miller model cone to

$$
\boxed{
\beta_{SV}\to0,
}
$$

where

$$
\beta_{SV}
=
\frac{
\|S\|_{\dot H^1}^2
}{
\|S\|_2
\|-\Delta S\|_2
}.
$$

The initial goal was to prove:

> $\beta_{SV}\to0$ forces a fixed positive fraction of the original strain-energy carrier to move to a remote high-frequency profile.

That statement is false in general.

A two-scale counterexample shows that

$$
\beta_{SV}\to0
$$

may be produced by a high-frequency component whose **base $L^2$ strain mass tends to zero**.

However, the derivative-weighted carrier behaves in the opposite way.

The exact replacement theorem is:

$$
\boxed{
\beta_{SV}
=
\operatorname{Aff}
(
\mu_E,\mu_Z
),
}
$$

where

$$
\mu_E
$$

is the normalized strain-energy spectral measure and

$$
\mu_Z
$$

is the normalized Laplacian-energy spectral measure.

Thus

$$
\boxed{
\beta_{SV}\to0
}
$$

means that these two derivative-level spectral carriers become asymptotically mutually singular.

More quantitatively, define

$$
x_E
=
\frac HE,
$$

$$
x_Z
=
\frac{Z^2}{H},
$$

where

$$
E=\|S\|_2^2,
\qquad
H=\|S\|_{\dot H^1}^2,
\qquad
Z=\|-\Delta S\|_2.
$$

Then

$$
\boxed{
\frac{x_Z}{x_E}
=
\beta_{SV}^{-2}.
}
$$

For the choice

$$
L=\beta_{SV}^{-1/2},
$$

at least

$$
1-\sqrt{\beta_{SV}}
$$

of the $E$-carrier lies below

$$
Lx_E,
$$

while at least

$$
1-\sqrt{\beta_{SV}}
$$

of the $Z$-carrier lies above

$$
x_Z/L.
$$

These two frequency-squared thresholds differ by the factor

$$
\boxed{
\beta_{SV}^{-1}.
}
$$

Equivalently, the corresponding frequency radii differ by

$$
\boxed{
\beta_{SV}^{-1/2}.
}
$$

A second new estimate shows that during any time at which

$$
H'(t)\ge0,
$$

the high derivative scale cannot run arbitrarily faster than the enstrophy amplitude:

$$
\boxed{
\frac{Z^2}{H}
\le
C E^2.
}
$$

and

$$
\boxed{
\frac HE
\le
C\beta_{SV}^2E^2.
}
$$

Thus the $\beta_{SV}\to0$ escape is now confined to a precise configuration:

> a vanishing-$E$-mass ultraviolet tail must carry an asymptotically dominant fraction of the $Z$-mass, while nonlinear transfer must continually compensate its viscous high-frequency loss.

The next proof target is therefore a **Low--High Interaction Tax Lemma**, not another generic diffuse-carrier theorem.

---

# 2. External calibration: Miller's approximate-eigenfunction criterion

Miller's 2026 revision contains the $q=2$ specialization

$$
\boxed{
\int_0^{T_{\max}}
\left(
1-
\frac{
\|S\|_{\dot H^1}^4
}{
\|S\|_2^2
\|-\Delta S\|_2^2
}
\right)^2
\|S\|_2^4
\,dt
=
+\infty
}
\tag{2.1}
$$

for finite-time blowup in the stated mild-solution class.

Therefore the parameter used in DCRP-05 is exactly

$$
\boxed{
\beta_{SV}^2
=
\frac{
\|S\|_{\dot H^1}^4
}{
\|S\|_2^2
\|-\Delta S\|_2^2
}.
}
\tag{2.2}
$$

Miller also proves a regularity criterion based on

$$
\inf_{\rho\in\mathbb R}
\|-\rho\Delta S-S\|_{L^q}.
$$

For

$$
q=2,
$$

the minimization can be computed exactly:

$$
\boxed{
\inf_{\rho\in\mathbb R}
\|-\rho\Delta S-S\|_2^2
=
E
\left(
1-\beta_{SV}^2
\right).
}
\tag{2.3}
$$

Indeed,

$$
\|-\rho\Delta S-S\|_2^2
=
\rho^2Z^2
-
2\rho H
+
E,
$$

whose minimum occurs at

$$
\rho_\ast
=
\frac H{Z^2}.
$$

Hence:

- $\beta_{SV}\approx1$ means the strain is close, in this $L^2$ sense, to a Laplacian eigenfunction shell;
- $\beta_{SV}\to0$ is the opposite extreme.

No novelty claim is made for the appearance of $1-\beta_{SV}^2$; it is already explicit in Miller's Theorem 1.12.

The new task here is to resolve its spectral-measure meaning inside the MORP/DCRP route.

---

# 3. Three canonical spectral measures

Let

$$
X(\xi)
=
|\xi|^2.
$$

Assume

$$
0<E,H,Z<\infty.
$$

Define the strain-energy probability measure

$$
\boxed{
d\mu_E(\xi)
=
\frac{
|\widehat S(\xi)|^2
}{
E
}
\,d\xi.
}
\tag{3.1}
$$

Define the $\dot H^1$ probability measure

$$
\boxed{
d\mu_H(\xi)
=
\frac{
X(\xi)
|\widehat S(\xi)|^2
}{
H
}
\,d\xi.
}
\tag{3.2}
$$

Define the Laplacian-energy probability measure

$$
\boxed{
d\mu_Z(\xi)
=
\frac{
X(\xi)^2
|\widehat S(\xi)|^2
}{
Z^2
}
\,d\xi.
}
\tag{3.3}
$$

All three are generated directly by the same physical state.

No dangerous-certificate mark is inserted.

---

# 4. NEW THEOREM — Hellinger identity

## Theorem 4.1

The Hellinger / Bhattacharyya affinity of

$$
\mu_E
$$

and

$$
\mu_Z
$$

is exactly

$$
\boxed{
\operatorname{Aff}
(
\mu_E,\mu_Z
)
=
\beta_{SV}.
}
\tag{4.1}
$$

Moreover,

$$
\boxed{
d\mu_H
=
\frac1{\beta_{SV}}
\sqrt{
d\mu_E\,d\mu_Z
}.
}
\tag{4.2}
$$

### Proof

Using the common Lebesgue reference measure,

$$
\sqrt{
\frac{
|\widehat S|^2
}{
E
}
\frac{
X^2|\widehat S|^2
}{
Z^2
}
}
=
\frac{
X|\widehat S|^2
}{
\sqrt E\,Z
}.
$$

Integrating,

$$
\operatorname{Aff}
(
\mu_E,\mu_Z
)
=
\frac{
\int X|\widehat S|^2
}{
\sqrt E\,Z
}
=
\frac H{\sqrt E\,Z}
=
\beta_{SV}.
$$

Also,

$$
\frac1{\beta_{SV}}
\frac{
X|\widehat S|^2
}{
\sqrt E\,Z
}
=
\frac{
X|\widehat S|^2
}{
H
},
$$

which is exactly

$$
d\mu_H.
$$

$$
\square
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 5. Corollary — asymptotic derivative-level mutual singularity

Let

$$
d_{\rm TV}
(
\mu_E,\mu_Z
)
$$

denote total variation distance.

For probability measures,

$$
1-
\operatorname{Aff}(\mu_E,\mu_Z)
\le
d_{\rm TV}(\mu_E,\mu_Z).
$$

Hence Theorem 4.1 gives

$$
\boxed{
d_{\rm TV}
(
\mu_E,\mu_Z
)
\ge
1-\beta_{SV}.
}
\tag{5.1}
$$

Therefore:

$$
\boxed{
\beta_{SV}\to0
\Longrightarrow
d_{\rm TV}
(
\mu_E,\mu_Z
)
\to1.
}
\tag{5.2}
$$

Thus the two derivative-level carriers become asymptotically mutually singular.

This is stronger than saying that the variance of frequency grows.

It identifies two explicit state-generated probability measures that separate.

---

# 6. Adjacent Rayleigh frequency scales

Define

$$
\boxed{
x_E
=
\frac HE
=
\mathbb E_{\mu_E}[X],
}
\tag{6.1}
$$

and

$$
\boxed{
x_Z
=
\frac{Z^2}{H}.
}
\tag{6.2}
$$

Then

$$
\frac{x_Z}{x_E}
=
\frac{
EZ^2
}{
H^2
}
=
\beta_{SV}^{-2}.
$$

Hence:

$$
\boxed{
x_Z
=
\beta_{SV}^{-2}x_E.
}
\tag{6.3}
$$

If the corresponding frequency radii are

$$
\kappa_E
=
\sqrt{x_E},
$$

$$
\kappa_Z
=
\sqrt{x_Z},
$$

then

$$
\boxed{
\frac{
\kappa_Z
}{
\kappa_E
}
=
\beta_{SV}^{-1}.
}
\tag{6.4}
$$

Thus $\beta_{SV}$ itself is the inverse adjacent-Sobolev spectral scale ratio.

---

# 7. NEW THEOREM — quantitative two-carrier separation

## Theorem 7.1

Let

$$
L>1.
$$

Then

$$
\boxed{
\mu_E
\left(
X\ge Lx_E
\right)
\le
\frac1L.
}
\tag{7.1}
$$

and

$$
\boxed{
\mu_Z
\left(
X\le\frac{x_Z}{L}
\right)
\le
\frac1L.
}
\tag{7.2}
$$

### Proof of (7.1)

By Markov:

$$
\mu_E
(
X\ge Lx_E
)
\le
\frac{
\mathbb E_{\mu_E}[X]
}{
Lx_E
}
=
\frac1L.
$$

### Proof of (7.2)

On

$$
X\le\frac{x_Z}{L},
$$

one has

$$
X^2
\le
\frac{x_Z}{L}X.
$$

Therefore

$$
\mu_Z
\left(
X\le\frac{x_Z}{L}
\right)
=
\frac{
E
\int_{\{X\le x_Z/L\}}
X^2
|\widehat S|^2/E
}{
Z^2
}.
$$

Equivalently using

$$
\mathbb E_{\mu_E}[X^2]
=
\frac{Z^2}{E}
=
x_Ex_Z,
$$

$$
\mu_Z
\left(
X\le\frac{x_Z}{L}
\right)
\le
\frac{
(x_Z/L)x_E
}{
x_Ex_Z
}
=
\frac1L.
$$

$$
\square
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 8. Corollary — diverging empty spectral corridor

Choose

$$
\boxed{
L
=
\beta_{SV}^{-1/2}.
}
\tag{8.1}
$$

Then:

$$
\boxed{
\mu_E
\left(
X<
\frac{x_E}{\sqrt{\beta_{SV}}}
\right)
\ge
1-\sqrt{\beta_{SV}}.
}
\tag{8.2}
$$

and

$$
\boxed{
\mu_Z
\left(
X>
x_Z\sqrt{\beta_{SV}}
\right)
\ge
1-\sqrt{\beta_{SV}}.
}
\tag{8.3}
$$

The two threshold values satisfy

$$
\frac{
x_Z\sqrt{\beta_{SV}}
}{
x_E/\sqrt{\beta_{SV}}
}
=
\beta_{SV}
\frac{x_Z}{x_E}
=
\beta_{SV}^{-1}.
$$

Therefore the frequency-squared gap is

$$
\boxed{
\beta_{SV}^{-1},
}
\tag{8.4}
$$

and the ordinary frequency gap is

$$
\boxed{
\beta_{SV}^{-1/2}.
}
\tag{8.5}
$$

So as

$$
\beta_{SV}\to0,
$$

almost all of the $E$-carrier lies below one scale and almost all of the $Z$-carrier lies above a scale separated from it by an unbounded factor.

---

# 9. NO-GO — base-carrier fixed-share reprofile is false

The original proposed Moment-Reprofile Lemma would have required that

$$
\beta_n\to0
$$

forces a fixed positive fraction of

$$
\mu_{E,n}
$$

to occur at a remote high frequency.

This is false.

Let

$$
\epsilon_n\downarrow0
$$

and consider the model spectral probability measure

$$
\boxed{
\mu_{E,n}
=
(1-\epsilon_n)\delta_1
+
\epsilon_n\delta_{\epsilon_n^{-2}}.
}
\tag{9.1}
$$

Then:

$$
\mathbb E[X]
=
1-\epsilon_n
+
\epsilon_n^{-1}
\sim
\epsilon_n^{-1},
$$

and

$$
\mathbb E[X^2]
=
1-\epsilon_n
+
\epsilon_n^{-3}
\sim
\epsilon_n^{-3}.
$$

Thus

$$
\beta_n
=
\frac{
\mathbb E[X]
}{
\sqrt{
\mathbb E[X^2]
}
}
\sim
\sqrt{\epsilon_n}
\to0.
$$

But the high-frequency base mass is only

$$
\boxed{
\epsilon_n\to0.
}
$$

On the other hand the associated

$$
\mu_Z
$$

mass at the high point tends to one.

Thus:

$$
\boxed{
\beta_n\to0
\not\Rightarrow
\text{fixed positive remote share in }\mu_{E,n}.
}
\tag{9.2}
$$

Any proof route requiring this implication is invalid.

The correct carrier for the ultraviolet side is derivative-weighted.

Status:

$$
\boxed{
\textbf{NO-GO PROVED at the spectral-measure level}.
}
$$

The same two-scale pattern can be approximated by smooth Fourier packets supported on separated annuli, so this is not an artifact of atomic notation.

---

# 10. Derivative-shell atom/diffuse dichotomy

Let

$$
A_j
=
\{
2^j\le|\xi|<2^{j+1}
\}
$$

be dyadic shells.

Define the Laplacian-energy shell shares

$$
\boxed{
c_j^{(Z)}
=
\mu_Z(A_j).
}
\tag{10.1}
$$

Then

$$
c_j^{(Z)}\ge0,
$$

and

$$
\sum_j
c_j^{(Z)}
=
1.
$$

For any sequence of states there are only two possibilities after subsequence extraction.

### Atomic derivative carrier

There exists

$$
\eta_0>0
$$

and shells

$$
j_n
$$

such that

$$
\boxed{
c_{j_n}^{(Z)}
\ge
\eta_0.
}
\tag{10.2}
$$

### Diffuse derivative carrier

$$
\boxed{
\sup_j
c_{j}^{(Z)}
\to0.
}
\tag{10.3}
$$

In the diffuse case, define

$$
\mathfrak M_Z
=
\left(
\sum_j
(c_j^{(Z)})^2
\right)^{-1}.
$$

Because

$$
\sum_j(c_j^{(Z)})^2
\le
\sup_jc_j^{(Z)}
\sum_jc_j^{(Z)}
=
\sup_jc_j^{(Z)},
$$

one has

$$
\boxed{
\mathfrak M_Z\to\infty.
}
\tag{10.4}
$$

Similarly the Shannon entropy satisfies

$$
\mathfrak H_Z
\ge
-\log
\sum_j
(c_j^{(Z)})^2,
$$

so

$$
\boxed{
\mathfrak H_Z\to\infty.
}
\tag{10.5}
$$

This is a derivative-weighted analogue of the MORP-05 atomic/diffuse split.

No claim is yet made that a fixed $Z$-shell atom automatically yields a nonzero actual Navier--Stokes state profile under symmetry-only normalization.

That bridge remains to be proved.

---

# 11. Exact bridge measure

The middle measure

$$
\mu_H
$$

is not independent.

Theorem 4.1 gives

$$
\boxed{
d\mu_H
=
\frac1{\beta_{SV}}
\sqrt{
d\mu_Ed\mu_Z
}.
}
\tag{11.1}
$$

Thus the $\dot H^1$ carrier is precisely the normalized geometric overlap of the two increasingly separated endpoint derivative carriers.

Consequently:

$$
\boxed{
\beta_{SV}\to0
}
$$

means that the middle Sobolev carrier is supported by an asymptotically small overlap set after renormalization.

This provides a precise interpretation of why weak base-carrier compactness can miss the relevant ultraviolet defect.

---

# 12. Nonlinear compensation estimate

The previous sections are purely spectral.

Now use the Navier--Stokes dynamics.

Let

$$
Q
=
P_{st}
\left(
(u\cdot\nabla)S
+
S^2
+
\frac34\omega\otimes\omega
\right).
$$

For sufficiently regular solutions,

$$
\boxed{
\|Q\|_2
\le
C
\left[
E^{1/2}
H^{1/4}
Z^{1/2}
+
E^{1/4}
H^{3/4}
\right].
}
\tag{12.1}
$$

### Proof

Because

$$
P_{st}
$$

is an $L^2$ orthogonal projection,

$$
\|Q\|_2
\le
\|(u\cdot\nabla)S\|_2
+
\left\|
S^2+\frac34\omega\otimes\omega
\right\|_2.
$$

For the transport term,

$$
\|(u\cdot\nabla)S\|_2
\le
\|u\|_6
\|\nabla S\|_3.
$$

Sobolev and the strain--velocity isometry give

$$
\|u\|_6
\le
C\|\nabla u\|_2
\le
C E^{1/2}.
$$

Interpolation gives

$$
\|\nabla S\|_3
\le
C
\|\nabla S\|_2^{1/2}
\|\nabla S\|_6^{1/2}
\le
C
H^{1/4}
Z^{1/2}.
$$

Thus

$$
\|(u\cdot\nabla)S\|_2
\le
C
E^{1/2}
H^{1/4}
Z^{1/2}.
$$

For the algebraic terms,

$$
\|S^2\|_2
\le
\|S\|_4^2
\le
C
E^{1/4}
H^{3/4}.
$$

The same bound holds for

$$
\omega\otimes\omega
$$

using boundedness of the strain--vorticity zero-order singular integral on

$$
L^4.
$$

This proves (12.1).

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 13. NEW THEOREM — growth-time spectral pinning

Define the scale-invariant shape parameter

$$
\boxed{
\mathfrak R
=
\frac{
H
}{
E^3
}.
}
\tag{13.1}
$$

## Theorem 13.1

At every sufficiently regular time for which

$$
H'(t)\ge0,
$$

one has

$$
\boxed{
\mathfrak R
\le
C_0
\beta_{SV}^2
(1-\beta_{SV}^2)^2
(1+\sqrt{\beta_{SV}})^4.
}
\tag{13.2}
$$

In particular,

$$
\boxed{
\mathfrak R
\le
C_1\beta_{SV}^2.
}
\tag{13.3}
$$

Consequently,

$$
\boxed{
\frac{
Z^2
}{
H
}
\le
C_1E^2,
}
\tag{13.4}
$$

and

$$
\boxed{
\frac HE
\le
C_1
\beta_{SV}^2
E^2.
}
\tag{13.5}
$$

### Proof

DCRP-05 proved the transverse growth estimate

$$
\frac12H'
\le
-Z^2
+
\sqrt{
1-\beta_{SV}^2
}
Z\|Q\|_2.
$$

If

$$
H'\ge0,
$$

then

$$
Z
\le
\sqrt{
1-\beta_{SV}^2
}
\|Q\|_2.
$$

Use (12.1):

$$
1
\le
C
\sqrt{
1-\beta_{SV}^2
}
\left[
E^{1/2}
H^{1/4}
Z^{-1/2}
+
E^{1/4}
H^{3/4}
Z^{-1}
\right].
$$

Since

$$
\beta_{SV}
=
\frac H{\sqrt E\,Z},
$$

one obtains

$$
E^{1/2}
H^{1/4}
Z^{-1/2}
=
\beta_{SV}^{1/2}
\mathfrak R^{-1/4},
$$

and

$$
E^{1/4}
H^{3/4}
Z^{-1}
=
\beta_{SV}
\mathfrak R^{-1/4}.
$$

Therefore

$$
1
\le
C
\sqrt{
1-\beta_{SV}^2
}
\mathfrak R^{-1/4}
\left(
\sqrt{\beta_{SV}}
+
\beta_{SV}
\right).
$$

Raise to the fourth power:

$$
\mathfrak R
\le
C_0
(1-\beta_{SV}^2)^2
\left(
\sqrt{\beta_{SV}}
+
\beta_{SV}
\right)^4.
$$

Since

$$
\left(
\sqrt\beta+\beta
\right)^4
=
\beta^2
(1+\sqrt\beta)^4,
$$

(13.2) follows.

Now

$$
\beta_{SV}^2
=
\frac{
H^2
}{
EZ^2
}
$$

implies

$$
\frac{Z^2}{H}
=
\frac{
H
}{
E\beta_{SV}^2
}
=
\frac{
\mathfrak R
}{
\beta_{SV}^2
}
E^2.
$$

Apply (13.3) to obtain (13.4).

Also,

$$
\frac HE
=
\mathfrak R E^2,
$$

which gives (13.5).

$$
\square
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 14. Interpretation of growth-time pinning

Let

$$
\kappa_E
=
\sqrt{
H/E
},
$$

and

$$
\kappa_Z
=
\sqrt{
Z^2/H
}.
$$

At

$$
H'\ge0,
$$

Theorem 13.1 gives

$$
\boxed{
\kappa_Z
\le
C E,
}
\tag{14.1}
$$

and

$$
\boxed{
\kappa_E
\le
C\beta_{SV}E.
}
\tag{14.2}
$$

while the exact identity

$$
\kappa_Z/\kappa_E
=
\beta_{SV}^{-1}
$$

still holds.

Therefore the derivative-scale separation can grow only by pushing the lower characteristic strain scale downward relative to the enstrophy amplitude while the upper derivative scale remains bounded by the natural amplitude scale

$$
E.
$$

This is a dynamical restriction that is absent from the purely spectral counterexample of Section 9.

---

# 15. Finite kinetic-energy lower bound on $\beta$ during $H$ growth

Let

$$
K(t)
=
\|u(t)\|_2^2.
$$

Fourier Cauchy--Schwarz and the strain--velocity isometry give

$$
\boxed{
H
\ge
\frac{
2E^2
}{
K
}.
}
\tag{15.1}
$$

Indeed,

$$
\|\nabla u\|_2^4
\le
\|u\|_2^2
\|\Delta u\|_2^2,
$$

while

$$
\|\nabla u\|_2^2
=
2E,
$$

and

$$
\|\Delta u\|_2^2
=
2H.
$$

Combining (15.1) with (13.5) at a time with

$$
H'\ge0,
$$

$$
\frac{
2E
}{
K
}
\le
\frac HE
\le
C_1
\beta_{SV}^2
E^2.
$$

Hence:

$$
\boxed{
\beta_{SV}^2E
\ge
\frac{
c
}{
K
}.
}
\tag{15.2}
$$

Since kinetic energy is nonincreasing,

$$
K(t)\le K(0),
$$

one gets the uniform growth-time constraint

$$
\boxed{
H'(t)\ge0
\Longrightarrow
E(t)
\ge
\frac{
c
}{
K(0)\beta_{SV}(t)^2
}.
}
\tag{15.3}
$$

Thus extreme spectral-moment separation during actual $\dot H^1$ growth is possible only at correspondingly large enstrophy.

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 16. Temporal sparsity of extreme-dispersion growth times

For a smooth finite-energy Navier--Stokes solution,

$$
\frac12
\frac d{dt}
K(t)
+
\|\nabla u(t)\|_2^2
=
0.
$$

Since

$$
\|\nabla u\|_2^2
=
2E,
$$

$$
\int_0^T
E(t)\,dt
\le
\frac{
K(0)
}{
4
}.
$$

Define

$$
\boxed{
A_\epsilon
=
\left\{
t:
H'(t)\ge0,
\quad
\beta_{SV}(t)\le\epsilon
\right\}.
}
\tag{16.1}
$$

By (15.3), for

$$
t\in A_\epsilon,
$$

$$
E(t)
\ge
\frac{
c
}{
K(0)\epsilon^2
}.
$$

Therefore

$$
\frac{
c
}{
K(0)\epsilon^2
}
|A_\epsilon|
\le
\int_{A_\epsilon}
E(t)\,dt
\le
\frac{
K(0)
}{
4
}.
$$

Hence

$$
\boxed{
|A_\epsilon|
\le
C
K(0)^2
\epsilon^2.
}
\tag{16.2}
$$

So:

$$
\boxed{
\textbf{
times of simultaneous }\dot H^1\textbf{-growth and extreme spectral separation
have Lebesgue measure }O(\epsilon^2).
}
}
\tag{16.3}
$$

This does not by itself rule out accumulation at a finite singular time.

It is a quantitative sparsity statement.

---

# 17. Why this still does not close Navier--Stokes

The new results do **not** imply that

$$
\beta_{SV}\to0
$$

is impossible.

A singular cascade could in principle use:

- vanishing base $E$-mass at ultraviolet frequencies;
- almost all $Z$-mass in the same ultraviolet tail;
- increasingly large enstrophy;
- increasingly short time intervals;
- nonlinear transfer sufficient to regenerate the high derivative carrier.

The global kinetic-energy budget controls

$$
\int E\,dt,
$$

but not

$$
\int E^2\,dt.
$$

Indeed Miller's Theorem 1.12 is consistent with finite-time blowup requiring divergence of a critical quantity comparable to

$$
\int E^2\,dt
$$

when

$$
\beta_{SV}\to0.
$$

Therefore the present estimates do not yield a contradiction from time integration alone.

This prevents a false closure claim.

---

# 18. What the counterexample teaches about reprofile

The measure-theoretic no-go in Section 9 shows:

$$
\boxed{
\text{fixed high-frequency share of }\mu_E
}
$$

cannot be the required reprofile mechanism.

The correct object must see at least one derivative-weighted measure.

The natural ultraviolet carrier is

$$
\boxed{
\mu_Z.
}
$$

However a fixed positive shell share in

$$
\mu_Z
$$

still does not automatically imply a nonzero Navier--Stokes state profile after **symmetry-only** rescaling.

The shell can carry large derivative weight while its lower-order / critical amplitude vanishes.

Thus the next bridge must be dynamical:

$$
\boxed{
\text{high derivative carrier}
+
\text{required nonlinear compensation}
\Longrightarrow
\text{nonzero interaction cost or actual profile}.
}
$$

---

# 19. Candidate interaction identity

The exact strain balance is

$$
\frac12H'
+
Z^2
=
-
\langle
-\Delta S,Q
\rangle.
$$

On a growth interval,

$$
-\langle
-\Delta S,Q
\rangle
\ge
Z^2.
$$

When

$$
\beta_{SV}\ll1,
$$

Section 8 shows that the vector

$$
-\Delta S
$$

is spectrally concentrated, in derivative weight, far above the bulk of the base strain-energy carrier.

Therefore the right side must be generated by nonlinear interactions that place a comparable amount of

$$
Q
$$

into the ultraviolet region carrying

$$
-\Delta S.
$$

This is the exact location where low--high paraproduct structure should be used.

A viable next lemma must estimate the ultraviolet pairing

$$
\boxed{
-\left<
P_{>N}\Delta S,
P_{>N}Q
\right>
}
\tag{19.1}
$$

with

$$
N
$$

chosen inside the spectral corridor from Section 8.

The objective is to show that if:

- the base $E$-mass above $N$ is vanishing;
- the $Z$-mass above a much larger frequency is fixed;
- no derivative-shell atom can be reprofilied;

then the nonlinear term cannot compensate

$$
Z^2
$$

without paying a positive cross-scale flux / transition cost.

---

# 20. Next exact target — Low--High Interaction Tax Lemma

The next proof target is:

$$
\boxed{
\textbf{Low--High Interaction Tax Lemma}.
}
$$

A useful sufficient form is the following.

Let

$$
N_-(t)<N_+(t)
$$

be thresholds satisfying

$$
\frac{
N_+(t)
}{
N_-(t)
}
\to\infty,
$$

with

$$
\mu_E
(
|\xi|>N_-
)
\to0,
$$

and

$$
\mu_Z
(
|\xi|<N_+
)
\to0.
$$

Prove that one of the following must occur:

1. **derivative reprofile**

   a dyadic high-frequency shell carries a fixed positive fraction of the $Z$-carrier and produces a nonzero actual state/profile after admissible re-rooting;

2. **cross-scale tax**

   the high-frequency nonlinear pairing obeys a positive lower bound in a native scale-invariant flux coordinate;

3. **insufficient compensation**

   the nonlinear high-frequency term cannot satisfy

   $$
   -\langle
   -\Delta S,Q
   \rangle
   \ge
   Z^2,
   $$

   forcing

   $$
   H'<0.
   $$

Any of these closes one part of the $\beta_{SV}\to0$ escape:

- (1) returns to the MORP atomic reprofile mechanism;
- (2) contradicts a true zero-cost minimal return;
- (3) forbids the required strain-$\dot H^1$ growth.

This is now the single state-visible frontier.

---

# 21. Source ledger

## External primary source

Evan Miller, *On the interaction of strain and vorticity for solutions of the Navier--Stokes equation*, arXiv:2407.02691v2, revised 2026-04-13, journal reference Pure Appl. Analysis 8 (2026), 247--270.

Checked facts used in this checkpoint:

- Proposition 1.1:

  $$
  \langle
  S,\omega\otimes\omega
  \rangle
  =
  -\frac43
  \langle
  S^2,S
  \rangle;
  $$

- Theorem 1.8:

  perturbative strain regularity criterion;

- Theorem 1.9:

  finite-time blowup requires

  $$
  \limsup
  \frac{
  \|Q\|_2
  }{
  \|-\Delta S\|_2
  }
  \ge1;
  $$

- Theorem 1.12:

  approximate-Laplacian-eigenfunction regularity criterion;

- $q=2$ specialization:

  $$
  \int
  (1-\beta_{SV}^2)^2E^2
  \,dt
  =
  +\infty
  $$

  under finite-time blowup;

- Theorem 1.13:

  endpoint lower bound for distance from the Laplacian-eigenfunction family.

No novelty or priority claim is made for Miller's established criteria.

The Hellinger-carrier reformulation and the subsequent deductions are internal derivations for this research program and remain subject to independent mathematical audit.

---

# 22. End state

The original target

$$
\beta_{SV}\to0
\Longrightarrow
\text{fixed-share base reprofile}
$$

is false.

The correct exact structure is:

$$
\boxed{
\beta_{SV}
=
\operatorname{Aff}
(
\mu_E,\mu_Z
).
}
$$

Thus:

$$
\boxed{
\beta_{SV}\to0
\Longrightarrow
\mu_E
\text{ and }
\mu_Z
\text{ become asymptotically mutually singular}.
}
$$

Moreover:

$$
\boxed{
\frac{x_Z}{x_E}
=
\beta_{SV}^{-2},
}
$$

and almost all of the two carriers can be separated by an expanding spectral corridor.

During actual

$$
H'\ge0
$$

times, nonlinear compensation forces

$$
\boxed{
\frac{Z^2}{H}
\le
CE^2
}
$$

and

$$
\boxed{
\beta_{SV}^2E
\ge
\frac c{K(0)}.
}
$$

Therefore the only remaining $\beta_{SV}\to0$ mechanism is a vanishing-base-mass but derivative-dominant ultraviolet tail continually regenerated by nonlinear cross-scale transfer.

The next exact target is:

$$
\boxed{
\textbf{
Low--High Interaction Tax Lemma}.
}
$$

No broader diffuse-carrier taxonomy is required.

---

# Checkpoint v7 Update — DCRP-07

# NS-DCRP-07 — $H^2$ Interaction Tax, Derivative Visibility Gap, and Strengthened Spectral Pinning

- date: 2026-08-16
- status: research proof checkpoint
- canonical source: UTF-8 Markdown
- canonical math delimiters: `$...$` and `$$...$$`
- objective: attack the DCRP-06 Low--High Interaction Tax frontier and determine whether the ultraviolet derivative carrier can be charged by the existing lower-order energy/flux ledgers.
- no full Navier--Stokes regularity claim is made.
- principal internal dependencies: MORP-01 through MORP-05, DCRP-03 through DCRP-06.
- external primary calibration:
  - Evan Miller, arXiv:2407.02691v2;
  - Alexey Cheskidov and Mimi Dai, arXiv:1507.06611;
  - Xiaoyutao Luo, arXiv:1803.05569v4;
  - Runlong Yu, arXiv:2606.25322v1.

---

# 1. Executive result

DCRP-06 identified the remaining state-visible escape as

$$
\boxed{
\beta_{SV}\to0,
}
$$

where

$$
\beta_{SV}
=
\frac{
H
}{
\sqrt E\,Z
},
$$

with

$$
E
=
\|S\|_2^2,
$$

$$
H
=
\|S\|_{\dot H^1}^2,
$$

and

$$
Z
=
\|-\Delta S\|_2.
$$

The corresponding spectral carriers satisfy

$$
\beta_{SV}
=
\operatorname{Aff}
(
\mu_E,\mu_Z
),
$$

so the escape is a separation between low-order strain energy and high-order derivative energy.

The present round establishes four facts.

## Fact A — ordinary lower-order visibility is insufficient

There exist smooth two-scale divergence-free fields for which:

$$
\beta_{SV}\to0,
$$

the ultraviolet share of kinetic energy tends to zero,

$$
\frac{
K_{\rm UV}
}{
K
}
\to0,
$$

the ultraviolet share of strain energy tends to zero,

$$
\frac{
E_{\rm UV}
}{
E
}
\to0,
$$

and even the ultraviolet share of

$$
H
$$

tends to zero, while

$$
\frac{
Z_{\rm UV}^2
}{
Z^2
}
\to1.
$$

Therefore no proof may assume that a derivative-dominant ultraviolet tail must carry a fixed positive ordinary energy / dissipation share.

This is a structural explanation for why a pressure--flux--energy ledger can remain blind to the final derivative tail.

## Fact B — true Navier--Stokes $H$ growth has a mandatory interaction tax

For every smooth Navier--Stokes solution,

$$
\boxed{
H'
+
2\nu Z^2
\le
C
\|\nabla u\|_\infty
H.
}
\tag{1.1}
$$

Hence at every time with

$$
H'\ge0,
$$

$$
\boxed{
\nu
\frac{
Z^2
}{
H
}
\le
C
\|\nabla u\|_\infty.
}
\tag{1.2}
$$

Define the derivative characteristic frequency

$$
\lambda_Z^2
=
\frac{
Z^2
}{
H
}.
$$

Then

$$
\boxed{
H'\ge0
\Longrightarrow
\nu\lambda_Z^2
\lesssim
\|\nabla u\|_\infty.
}
\tag{1.3}
$$

Thus a derivative-dominant UV tail cannot grow while viscosity dominates its characteristic frequency.

The nonlinear shear rate must be at least comparable to the viscous rate.

## Fact C — $\beta$ pinning strengthens from $\beta^2$ to $\beta^5$

Using the valid three-dimensional Gagliardo--Nirenberg inequality

$$
\|\nabla u\|_\infty
\le
C
\|\nabla u\|_2^{1/4}
\|D^3u\|_2^{3/4},
$$

one obtains at every

$$
H'\ge0
$$

time:

$$
\boxed{
\frac{
H
}{
E^3
}
\le
C\nu^{-4}
\beta_{SV}^{5}.
}
\tag{1.4}
$$

This strictly improves the earlier DCRP-06 bound

$$
H/E^3
\lesssim
\beta_{SV}^2
$$

in the extreme-dispersion regime.

## Fact D — extreme spectral-separation growth times are even sparser

If

$$
K_0
=
\|u(0)\|_2^2,
$$

then

$$
\boxed{
H'\ge0
\Longrightarrow
E
\ge
c
\frac{
\nu^4
}{
K_0\beta_{SV}^{5}
}.
}
\tag{1.5}
$$

Hence

$$
A_\epsilon
=
\left\{
t:
H'(t)\ge0,
\quad
\beta_{SV}(t)\le\epsilon
\right\}
$$

satisfies

$$
\boxed{
|A_\epsilon|
\le
C
\frac{
K_0^2
}{
\nu^5
}
\epsilon^5.
}
\tag{1.6}
$$

The exponent improves from the earlier

$$
O(\epsilon^2)
$$

estimate to

$$
O(\epsilon^5).
$$

This still does not by itself exclude finite-time blowup, because arbitrarily large nonlinear activity may concentrate on arbitrarily short time sets.

The next closure target is therefore not a lower-order energy-flux tax.

It is a **derivative-level UV flux / commutator bridge**.

---

# 2. Exact Fourier norm relations

Let

$$
u
$$

be divergence free and

$$
S
=
\nabla_{\rm sym}u.
$$

In Fourier variables,

$$
\widehat S_{ij}
=
\frac i2
\left(
\xi_i\widehat u_j
+
\xi_j\widehat u_i
\right).
$$

Since

$$
\xi\cdot\widehat u=0,
$$

one obtains pointwise

$$
|\widehat S(\xi)|^2
=
\frac12
|\xi|^2
|\widehat u(\xi)|^2.
$$

Consequently,

$$
\boxed{
E
=
\|S\|_2^2
=
\frac12
\|\nabla u\|_2^2,
}
\tag{2.1}
$$

$$
\boxed{
H
=
\|S\|_{\dot H^1}^2
=
\frac12
\|D^2u\|_2^2,
}
\tag{2.2}
$$

and

$$
\boxed{
Z^2
=
\|-\Delta S\|_2^2
=
\frac12
\|D^3u\|_2^2.
}
\tag{2.3}
$$

These identities allow the strain spectral frontier to be tested directly by the standard differentiated Navier--Stokes energy estimate.

---

# 3. NEW THEOREM — $H^2$ interaction inequality

## Theorem 3.1

Let

$$
u
$$

be a smooth divergence-free solution of

$$
\partial_tu
-
\nu\Delta u
+
(u\cdot\nabla)u
+
\nabla p
=
0
$$

on

$$
\mathbb R^3.
$$

Then

$$
\boxed{
H'
+
2\nu Z^2
\le
C
\|\nabla u\|_\infty
H.
}
\tag{3.1}
$$

### Proof

Apply

$$
\Delta
$$

to the velocity equation and pair with

$$
\Delta u.
$$

The pressure contribution vanishes by incompressibility.

One gets

$$
\frac12
\frac d{dt}
\|\Delta u\|_2^2
+
\nu
\|\nabla\Delta u\|_2^2
=
-
\left<
\Delta
\left[
(u\cdot\nabla)u
\right],
\Delta u
\right>.
$$

Expand:

$$
\Delta
\left[
(u\cdot\nabla)u
\right]
=
(u\cdot\nabla)\Delta u
+
2
\sum_k
(\partial_ku\cdot\nabla)\partial_ku
+
(\Delta u\cdot\nabla)u.
$$

The leading transport term cancels:

$$
\left<
(u\cdot\nabla)\Delta u,
\Delta u
\right>
=
0.
$$

The remaining terms satisfy

$$
\left|
\left<
2
\sum_k
(\partial_ku\cdot\nabla)\partial_ku,
\Delta u
\right>
\right|
\le
C
\|\nabla u\|_\infty
\|D^2u\|_2^2,
$$

and

$$
\left|
\left<
(\Delta u\cdot\nabla)u,
\Delta u
\right>
\right|
\le
\|\nabla u\|_\infty
\|\Delta u\|_2^2.
$$

Therefore

$$
\frac12
\frac d{dt}
\|D^2u\|_2^2
+
\nu
\|D^3u\|_2^2
\le
C
\|\nabla u\|_\infty
\|D^2u\|_2^2.
$$

Use (2.2)--(2.3):

$$
\|D^2u\|_2^2
=
2H,
$$

$$
\|D^3u\|_2^2
=
2Z^2.
$$

After absorbing the harmless factor two into the universal constant:

$$
\boxed{
H'
+
2\nu Z^2
\le
C
\|\nabla u\|_\infty
H.
}
$$

$$
\square
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 4. NEW COROLLARY — instantaneous derivative interaction tax

If

$$
H'(t)\ge0,
$$

Theorem 3.1 gives

$$
2\nu Z^2
\le
C
\|\nabla u\|_\infty H.
$$

Therefore:

$$
\boxed{
\|\nabla u\|_\infty
\ge
c\nu
\frac{
Z^2
}{
H
}.
}
\tag{4.1}
$$

Define

$$
\boxed{
\lambda_Z^2
=
\frac{
Z^2
}{
H
}.
}
\tag{4.2}
$$

Then:

$$
\boxed{
H'\ge0
\Longrightarrow
\|\nabla u\|_\infty
\ge
c\nu\lambda_Z^2.
}
\tag{4.3}
$$

Define the dimensionless interaction ratio

$$
\boxed{
\mathfrak I_{H^2}(t)
=
\frac{
\|\nabla u(t)\|_\infty
H(t)
}{
\nu Z(t)^2
}.
}
\tag{4.4}
$$

Under Navier--Stokes parabolic scaling:

$$
\|\nabla u\|_\infty
\mapsto
a^2
\|\nabla u\|_\infty,
$$

$$
H
\mapsto
a^3H,
$$

$$
Z^2
\mapsto
a^5Z^2.
$$

Hence:

$$
\boxed{
\mathfrak I_{H^2}
\text{ is scale invariant}.
}
\tag{4.5}
$$

Moreover:

$$
\boxed{
H'\ge0
\Longrightarrow
\mathfrak I_{H^2}
\ge
c.
}
\tag{4.6}
$$

This is the first rigorous interaction-tax statement for the derivative-dominant branch.

---

# 5. Interpretation as a dissipation-scale obstruction

The viscous time rate at frequency

$$
\lambda_Z
$$

is

$$
\nu\lambda_Z^2.
$$

Equation (4.3) says that whenever the strain

$$
\dot H^1
$$

norm is growing, the nonlinear Lipschitz shear rate must satisfy

$$
\boxed{
\text{nonlinear shear rate}
\gtrsim
\text{viscous rate at }\lambda_Z.
}
\tag{5.1}
$$

Thus the ultraviolet derivative carrier can grow only while its characteristic frequency lies at or below an instantaneous nonlinear dissipation boundary.

This is consistent with the dissipation-wavenumber philosophy in the frequency-localized Navier--Stokes regularity literature.

It is not itself a global regularity theorem.

---

# 6. NEW THEOREM — strengthened $\beta$ shape pinning

The DCRP-06 shape variable was

$$
\mathfrak R
=
\frac{
H
}{
E^3
}.
$$

DCRP-06 obtained

$$
\mathfrak R
\lesssim
\beta_{SV}^2
$$

at

$$
H'\ge0
$$

times using a direct estimate for the Miller residual.

The $H^2$ interaction inequality yields a stronger exponent.

## Theorem 6.1

At every smooth time with

$$
H'\ge0,
$$

$$
\boxed{
\frac{
H
}{
E^3
}
\le
C
\nu^{-4}
\beta_{SV}^{5}.
}
\tag{6.1}
$$

### Proof

By (4.1),

$$
\nu
\frac{
Z^2
}{
H
}
\le
C
\|\nabla u\|_\infty.
$$

Use the three-dimensional Gagliardo--Nirenberg inequality

$$
\boxed{
\|\nabla u\|_\infty
\le
C
\|\nabla u\|_2^{1/4}
\|D^3u\|_2^{3/4}.
}
\tag{6.2}
$$

By (2.1) and (2.3),

$$
\|\nabla u\|_2
=
(2E)^{1/2},
$$

and

$$
\|D^3u\|_2
=
(2Z^2)^{1/2}
=
\sqrt2\,Z.
$$

Thus

$$
\|\nabla u\|_\infty
\le
C
E^{1/8}
Z^{3/4}.
$$

Therefore

$$
\nu
\frac{
Z^2
}{
H
}
\le
C
E^{1/8}
Z^{3/4}.
$$

Rearrange:

$$
\nu
Z^{5/4}
\le
C
E^{1/8}
H.
$$

Use

$$
\beta_{SV}
=
\frac{
H
}{
\sqrt E\,Z
},
$$

so

$$
Z
=
\frac{
H
}{
\beta_{SV}\sqrt E
}.
$$

Substitution gives

$$
\nu
H^{5/4}
\beta_{SV}^{-5/4}
E^{-5/8}
\le
C
E^{1/8}
H.
$$

Cancel

$$
H:
$$

$$
\nu
H^{1/4}
\le
C
\beta_{SV}^{5/4}
E^{3/4}.
$$

Raise to the fourth power:

$$
\boxed{
H
\le
C
\nu^{-4}
\beta_{SV}^{5}
E^3.
}
$$

$$
\square
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 7. Comparison with DCRP-06

For

$$
0<\beta_{SV}\ll1,
$$

the new estimate

$$
H/E^3
\lesssim
\beta_{SV}^{5}
$$

is substantially stronger than

$$
H/E^3
\lesssim
\beta_{SV}^{2}.
$$

Therefore DCRP-06 Theorem 13.1 is superseded, for the extreme-dispersion growth regime, by Theorem 6.1.

The older theorem remains algebraically valid under its stated assumptions.

The new estimate is preferred.

---

# 8. Finite-energy interpolation lower bound

Let

$$
K(t)
=
\|u(t)\|_2^2.
$$

Fourier Cauchy--Schwarz gives

$$
\|\nabla u\|_2^4
\le
\|u\|_2^2
\|D^2u\|_2^2.
$$

Using

$$
\|\nabla u\|_2^2
=
2E
$$

and

$$
\|D^2u\|_2^2
=
2H,
$$

one obtains

$$
4E^2
\le
2KH.
$$

Hence:

$$
\boxed{
H
\ge
\frac{
2E^2
}{
K
}.
}
\tag{8.1}
$$

Since kinetic energy is nonincreasing,

$$
K(t)\le K_0,
$$

where

$$
K_0=K(0).
$$

---

# 9. NEW COROLLARY — enstrophy floor at extreme-dispersion growth times

Combine (6.1) and (8.1):

$$
\frac{
2E^2
}{
K_0
}
\le
H
\le
C
\nu^{-4}
\beta_{SV}^{5}
E^3.
$$

Cancel

$$
E^2>0.
$$

Then:

$$
\boxed{
E
\ge
c
\frac{
\nu^4
}{
K_0
\beta_{SV}^{5}
}
}
\tag{9.1}
$$

at every

$$
H'\ge0
$$

time.

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

This improves the previous DCRP-06 lower bound proportional to

$$
\beta_{SV}^{-2}.
$$

---

# 10. NEW COROLLARY — stronger temporal sparsity

The global kinetic-energy equality gives

$$
\frac12
K'(t)
+
\nu
\|\nabla u(t)\|_2^2
=
0.
$$

Since

$$
\|\nabla u\|_2^2
=
2E,
$$

$$
\boxed{
\int_0^T
E(t)\,dt
\le
\frac{
K_0
}{
4\nu
}.
}
\tag{10.1}
$$

Define

$$
A_\epsilon
=
\left\{
t:
H'(t)\ge0,
\quad
\beta_{SV}(t)\le\epsilon
\right\}.
$$

For

$$
t\in A_\epsilon,
$$

(9.1) gives

$$
E(t)
\ge
c
\frac{
\nu^4
}{
K_0
\epsilon^5
}.
$$

Hence

$$
c
\frac{
\nu^4
}{
K_0
\epsilon^5
}
|A_\epsilon|
\le
\int_{A_\epsilon}
E(t)\,dt
\le
\frac{
K_0
}{
4\nu
}.
$$

Therefore:

$$
\boxed{
|A_\epsilon|
\le
C
\frac{
K_0^2
}{
\nu^5
}
\epsilon^5.
}
\tag{10.2}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

Thus simultaneous

$$
H\text{-growth}
+
\beta_{SV}\ll1
$$

occurs on an increasingly sparse set with fifth-order measure decay.

---

# 11. NEW COROLLARY — Lipschitz amplitude floor

Equation (4.1) gives

$$
\|\nabla u\|_\infty
\ge
c\nu
\frac{
H
}{
\beta_{SV}^2E
}.
$$

Using (8.1),

$$
H
\ge
\frac{
2E^2
}{
K_0
},
$$

so:

$$
\boxed{
\|\nabla u\|_\infty
\ge
c
\frac{
\nu E
}{
K_0
\beta_{SV}^2
}.
}
\tag{11.1}
$$

Now apply the enstrophy floor (9.1):

$$
\boxed{
\|\nabla u\|_\infty
\ge
c
\frac{
\nu^5
}{
K_0^2
\beta_{SV}^{7}
}
}
\tag{11.2}
$$

at every

$$
H'\ge0
$$

time.

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

Therefore extreme derivative-level spectral separation can support

$$
H
$$

growth only through correspondingly extreme instantaneous nonlinear shear.

---

# 12. Integrated interaction tax for a scale return

From Theorem 3.1,

$$
H'
\le
C
\|\nabla u\|_\infty
H.
$$

Therefore:

$$
\boxed{
\frac d{dt}
\log H
\le
C
\|\nabla u\|_\infty.
}
\tag{12.1}
$$

Suppose an actual forward physical return increases

$$
H
$$

by the scale factor dictated by concentration ratio

$$
\Lambda>1:
$$

$$
H(b)
=
\Lambda^3
H(a).
$$

Integrating (12.1):

$$
3\log\Lambda
=
\log
\frac{
H(b)
}{
H(a)
}
\le
C
\int_a^b
\|\nabla u(t)\|_\infty
\,dt.
$$

Hence:

$$
\boxed{
\int_a^b
\|\nabla u(t)\|_\infty
\,dt
\ge
c
\log\Lambda.
}
\tag{12.2}
$$

The quantity

$$
\int
\|\nabla u\|_\infty\,dt
$$

is parabolic-scale invariant.

Thus every genuine scale-changing return pays a nonzero integrated Lipschitz interaction debt.

This is compatible with classical BKM-type necessary blowup behavior and does not itself contradict finite-time singularity.

---

# 13. NO-GO — lower-order carrier visibility does not see the final UV tail

The DCRP-06 two-scale example can be sharpened to show a derivative visibility gap.

Let

$$
N\to\infty.
$$

Choose two smooth divergence-free Fourier packets with disjoint annular supports:

- a low packet near frequency
  $$
  |\xi|\sim1;
  $$

- a high packet near
  $$
  |\xi|\sim N.
  $$

Normalize the low packet so its strain energy is order one.

Choose the high packet so its strain-energy mass is

$$
\boxed{
E_{\rm hi}
\sim
N^{-3}.
}
\tag{13.1}
$$

Then its contributions scale as:

### kinetic energy

Since

$$
E_{\rm hi}
\sim
N^2K_{\rm hi},
$$

$$
\boxed{
K_{\rm hi}
\sim
N^{-5}.
}
\tag{13.2}
$$

### strain energy

$$
\boxed{
E_{\rm hi}
\sim
N^{-3}.
}
\tag{13.3}
$$

### strain $\dot H^1$ energy

$$
H_{\rm hi}
\sim
N^2E_{\rm hi}
\sim
N^{-1}.
$$

Thus:

$$
\boxed{
H_{\rm hi}
\to0.
}
\tag{13.4}
$$

### Laplacian-strain energy

$$
Z_{\rm hi}^2
\sim
N^4E_{\rm hi}
\sim
N.
$$

Hence:

$$
\boxed{
Z_{\rm hi}^2
\to\infty.
}
\tag{13.5}
$$

For the combined low + high field,

$$
E\sim1,
$$

$$
H\sim1,
$$

and

$$
Z^2\sim N.
$$

Therefore:

$$
\boxed{
\beta_{SV}
\sim
N^{-1/2}
\to0.
}
\tag{13.6}
$$

At the same time:

$$
\boxed{
\frac{
K_{\rm hi}
}{
K
}
\to0,
\qquad
\frac{
E_{\rm hi}
}{
E
}
\to0,
\qquad
\frac{
H_{\rm hi}
}{
H
}
\to0,
}
\tag{13.7}
$$

while

$$
\boxed{
\frac{
Z_{\rm hi}^2
}{
Z^2
}
\to1.
}
\tag{13.8}
$$

Thus an ultraviolet tail can be invisible to all three lower orders

$$
K,\ E,\ H
$$

while dominating the next derivative order

$$
Z^2.
$$

Status:

$$
\boxed{
\textbf{PROVED as a smooth spectral-family no-go}.
}
$$

This family is not claimed to be a blowup solution.

It proves only that lower-order carrier visibility cannot, by functional analysis alone, control the derivative-dominant tail.

---

# 14. Consequence for PFET / lower-order paid ledgers

The existing PFET-type channels are built from pressure, kinetic-energy flux, localized energy, trace, and related lower-order finite-window observables.

The spectral family of Section 13 shows that one cannot prove a universal implication of the form

$$
\boxed{
Z_{\rm UV}\text{ dominant}
\Longrightarrow
\text{fixed positive lower-order energy share}.
}
\tag{14.1}
$$

Therefore the remaining derivative-dominant branch cannot be closed merely by asserting that the UV tail must become visible in ordinary kinetic-energy mass.

A successful bridge must use one of:

1. derivative-level nonlinear transfer;
2. a commutator linking derivative growth to an already-paid lower-order flux;
3. a dynamical theorem showing that a derivative-only tail cannot remain lower-order invisible under actual Navier--Stokes evolution.

This is a genuine restriction on the next proof architecture.

---

# 15. Frequency-localized external calibration

Frequency-localized Navier--Stokes regularity theory already supports the general principle that possible singularity formation requires persistent activity at dynamically active high frequencies.

Cheskidov--Dai prove regularity under smallness of frequency-localized vorticity activity near the dissipation wavenumber.

Luo develops cutoff high-frequency energy/dissipation and flux inequalities on intervals of regularity.

In particular, a standard cutoff-energy structure has the schematic form

$$
\frac d{dt}
\|u_{\ge p}\|_2^2
+
2\nu
\|\nabla u_{\ge p}\|_2^2
\lesssim
|\Pi_{\ge p}|,
$$

with the nonlinear flux controlled by weighted high/near-frequency energy multiplied by a low-frequency Lipschitz factor.

These results do not directly close the present branch because Section 13 shows that the catastrophic carrier may be invisible at the kinetic-energy level.

They do, however, identify the correct mechanism:

$$
\boxed{
\text{a high derivative tail must be dynamically replenished through nonlinear frequency transfer}.
}
$$

---

# 16. Relation to the 2026 pressure--flux work framework

Yu's 2026 coarse-grained pressure--flux theorem gives a finite-scale resolved/unresolved decomposition and an exact combined pressure--flux work depletion law.

For the present program, the important calibration is:

- lower-order CKN badness can be split into resolved visibility and unresolved oscillation;
- forward combined work and resolved dissipation are paid by finite energy, leakage, and backscatter terms.

The derivative-visibility no-go of Section 13 explains why the final DCRP survivor may live entirely inside the unresolved / higher-derivative side without carrying a fixed lower-order resolved mass.

Thus the next bridge cannot merely re-use the PFET observable unchanged.

It must show that the **derivative-level interaction tax** from Theorem 3.1 necessarily induces either:

$$
\boxed{
\text{PFET-visible work}
}
$$

or

$$
\boxed{
\text{a retained unresolved derivative defect}.
}
$$

That is now the precise coupling problem.

---

# 17. The current Low--High Interaction Tax theorem

The strongest unconditional statement presently obtained is:

## Theorem 17.1

For every smooth finite-energy three-dimensional Navier--Stokes solution, at every time with

$$
H'(t)\ge0,
$$

the derivative UV characteristic scale

$$
\lambda_Z
=
\frac{
Z
}{
\sqrt H
}
$$

satisfies

$$
\boxed{
\nu\lambda_Z^2
\le
C
\|\nabla u\|_\infty.
}
\tag{17.1}
$$

Equivalently:

$$
\boxed{
\mathfrak I_{H^2}
=
\frac{
\|\nabla u\|_\infty
}{
\nu\lambda_Z^2
}
\ge
c.
}
\tag{17.2}
$$

Together with

$$
\beta_{SV}
=
\frac{
\lambda_E
}{
\lambda_Z
},
$$

where

$$
\lambda_E^2
=
H/E,
$$

this gives:

$$
\boxed{
\lambda_E
\le
C
\beta_{SV}
\sqrt{
\frac{
\|\nabla u\|_\infty
}{
\nu
}
}.
}
\tag{17.3}
$$

Thus the

$$
\beta_{SV}\to0
$$

escape cannot be a passive static tail.

At every time at which it contributes to increasing

$$
H,
$$

it must sit inside an actively nonlinear shear regime.

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 18. Why this is not yet the final contradiction

The integral

$$
\int_0^{T}
\|\nabla u\|_\infty\,dt
$$

is allowed to diverge at a hypothetical singular time.

Therefore:

$$
\boxed{
\text{positive interaction tax}
\not\Rightarrow
\bot
}
$$

unless that tax is connected to a globally finite ledger or to MORP minimal zero-cost recurrence.

Likewise, the estimate

$$
|A_\epsilon|
\lesssim
\epsilon^5
$$

does not exclude a singularity, because the nonlinear amplitude on those increasingly short sets may diverge faster.

The remaining issue is not finding a nonzero interaction quantity.

That has now been done.

The issue is **payment**.

---

# 19. Next exact target — UV Flux Bridge Lemma

The next proof target is:

$$
\boxed{
\textbf{UV Flux Bridge Lemma}.
}
$$

Desired form:

Let an actual singular-return interval contain a derivative-dominant state with

$$
\beta_{SV}\ll1
$$

and a period on which

$$
H
$$

achieves the growth required by the return scale.

Then prove that the mandatory interaction debt

$$
\int
\frac{
\|\nabla u\|_\infty H
}{
\nu Z^2
}
\,d\mu_{\rm growth}
$$

or an equivalent derivative-frequency flux quantity must produce at least one of:

1. a nonzero contribution to the existing paid / pressure--flux--energy ledger;

2. a nonzero native transition residual;

3. a derivative defect measure retained under MORP compactification.

The key requirement is:

$$
\boxed{
\text{no derivative-level transfer may disappear simultaneously from all three channels}.
}
\tag{19.1}
$$

A successful proof would bridge the new $H^2$ tax back into the old minimal-zero-cost framework.

---

# 20. More concrete dyadic target

Let

$$
P_{\ge p}
$$

be a smooth high-frequency projector and define

$$
H_{\ge p}
=
\|D^2P_{\ge p}u\|_2^2,
$$

$$
Z_{\ge p}^2
=
\|D^3P_{\ge p}u\|_2^2.
$$

The next local-frequency theorem should establish an inequality of the form

$$
\boxed{
\frac12
\frac d{dt}
H_{\ge p}
+
\nu
Z_{\ge p}^2
\le
\mathcal F_p^{LH}
+
\mathcal F_p^{HH},
}
\tag{20.1}
$$

where:

$$
\mathcal F_p^{LH}
$$

is a low--high commutator flux controlled by low-frequency strain / shear, and

$$
\mathcal F_p^{HH}
$$

is a high--high remainder.

The desired closure is then:

- if
  $$
  \mathcal F_p^{LH}
  $$
  is large, charge it to a scale-critical paid / flux channel;

- if
  $$
  \mathcal F_p^{HH}
  $$
  is large, extract a high-frequency derivative profile or retain a derivative defect;

- if both are small, viscosity gives
  $$
  \frac d{dt}H_{\ge p}<0.
  $$

This is now a concrete Littlewood--Paley / commutator proof problem.

---

# 21. Source ledger

## Evan Miller

Evan Miller, *On the interaction of strain and vorticity for solutions of the Navier--Stokes equation*, arXiv:2407.02691v2.

Used for the strain-side calibration and the $\beta_{SV}$ / approximate-Laplacian-eigenfunction framework already established in DCRP-05/06.

## Cheskidov--Dai

Alexey Cheskidov and Mimi Dai, *Regularity criteria for the 3D Navier-Stokes and MHD equations*, arXiv:1507.06611.

Used only as external frequency-localized calibration: high-frequency vorticity activity near a dissipation wavenumber is sufficient to formulate refined regularity criteria.

## Luo

Xiaoyutao Luo, arXiv:1803.05569v4.

Used as external calibration for:

- Littlewood--Paley cutoff energy;
- high-frequency dissipation;
- nonlinear energy flux through a wavenumber.

No claim is made that Luo's kinetic-energy cutoff flux directly controls the present $H^2$ derivative carrier.

## Yu

Runlong Yu, *Coarse-Grained Resolution and Pressure--Flux Work Depletion for Navier-Stokes CKN Badness*, arXiv:2606.25322v1.

Used only as external calibration for the existing lower-order resolved/unresolved pressure--flux work framework.

The derivative-level bridge required in Section 19 is not claimed to be proved there.

---

# 22. End state

This round answers the first Low--High Interaction Tax question.

The answer is:

$$
\boxed{
\textbf{
yes, derivative growth must pay a scale-invariant nonlinear interaction tax;
but no, that tax is not automatically visible in the old lower-order energy carrier.
}
}
$$

The exact interaction lower bound is

$$
\boxed{
H'\ge0
\Longrightarrow
\|\nabla u\|_\infty
\ge
c\nu
\frac{
Z^2
}{
H
}.
}
$$

The extreme-dispersion shape is sharpened to

$$
\boxed{
\frac{
H
}{
E^3
}
\lesssim
\nu^{-4}
\beta_{SV}^{5},
}
$$

and

$$
\boxed{
|A_\epsilon|
\lesssim
\frac{
K_0^2
}{
\nu^5
}
\epsilon^5.
}
$$

At the same time, a smooth spectral no-go shows that the ultraviolet tail may satisfy

$$
K_{\rm UV},
\ E_{\rm UV},
\ H_{\rm UV}
\to0
$$

while

$$
Z_{\rm UV}^2/Z^2
\to1.
$$

Therefore the next single frontier is:

$$
\boxed{
\textbf{
UV Flux Bridge Lemma:
convert mandatory derivative interaction into paid flux,
native residual, or retained derivative defect.
}
}
$$

That is the next exact attack.

---

# Checkpoint v8 Update — DCRP-08

# NS-DCRP-08 — Dissipation-Wavenumber Supplier Atom Recovery and the UV Supply Bridge

- date: 2026-08-16
- status: research proof checkpoint
- canonical source: UTF-8 Markdown
- canonical math delimiters: `$...$` and `$$...$$`
- objective: continue DCRP-07 by bridging a derivative-dominant ultraviolet tail back to a lower-order, scale-critical, state-visible supplier shell.
- no full Navier--Stokes regularity claim is made.
- principal internal dependencies: MORP-02 through MORP-05, DCRP-05 through DCRP-07.
- principal external primary source: Alexey Cheskidov and Mimi Dai, arXiv:1507.06611v6.
- secondary calibration: Cheskidov--Shvydkoy, arXiv:1102.1944.

---

# 1. Executive result

DCRP-07 proved that a derivative-dominant ultraviolet tail may satisfy

$$
K_{\rm UV}\to0,
\qquad
E_{\rm UV}\to0,
\qquad
H_{\rm UV}\to0,
$$

while

$$
\frac{Z_{\rm UV}^2}{Z^2}\to1.
$$

Thus lower-order raw mass alone cannot see the final tail.

The present round shows that this does **not** mean the ultraviolet derivative tail can be dynamically supplied without a lower-order critical atom.

Let

$$
u_q=\Delta_q u,
\qquad
\lambda_q=2^q,
$$

and define the Navier--Stokes dissipation wavenumber in the $r=\infty$ form

$$
\boxed{
\Lambda(t)
=
\lambda_{Q(t)}
=
\min
\left\{
\lambda_q:
\lambda_p^{-1}
\|u_p(t)\|_\infty
<
c_0\nu
\quad
\forall p>q
\right\}.
}
\tag{1.1}
$$

For every smooth nontrivial state with

$$
1<\Lambda(t)<\infty,
$$

minimality gives the exact boundary lower bound

$$
\boxed{
\|u_{Q(t)}(t)\|_\infty
\ge
c_0\nu\Lambda(t).
}
\tag{1.2}
$$

Bernstein therefore yields

$$
\boxed{
\Lambda(t)
\|u_{Q(t)}(t)\|_2^2
\ge
c_1\nu^2.
}
\tag{1.3}
$$

The quantity

$$
\lambda_q\|u_q\|_2^2
$$

is scale critical in three dimensions.

After rescaling the $Q$-shell to unit frequency,

$$
v_Q(y)
=
\Lambda^{-1}
u_Q
\left(
x_0+\Lambda^{-1}y
\right),
$$

one obtains

$$
\boxed{
\|v_Q\|_\infty
\ge
c_0\nu,
}
\tag{1.4}
$$

and

$$
\boxed{
\|v_Q\|_2^2
=
\Lambda
\|u_Q\|_2^2
\ge
c_1\nu^2.
}
\tag{1.5}
$$

After translating to a point of almost maximal amplitude, band limitation gives a fixed-radius local lower bound

$$
\boxed{
\int_{B_{r_0}}
|v_Q(y)|^2\,dy
\ge
c_2\nu^2.
}
\tag{1.6}
$$

Thus the dissipation-boundary supplier shell is a genuine nonvanishing state-visible object after its natural critical rescaling.

The second part of the result uses Cheskidov--Dai's Littlewood--Paley flux estimate. For the Navier--Stokes equation and any

$$
s>\frac12,
$$

in particular

$$
s=2,
$$

the nonlinear $H^s$ flux satisfies schematically

$$
\boxed{
|I_s|
\le
c_3\nu
\sum_{q>Q-3}
\lambda_q^{2s+2}
\|u_q\|_2^2
+
C f(t)
\sum_q
\lambda_q^{2s}
\|u_q\|_2^2,
}
\tag{1.7}
$$

where

$$
\boxed{
f(t)
=
\sum_{q\le Q(t)}
\lambda_q
\|u_q(t)\|_\infty.
}
\tag{1.8}
$$

The first term is absorbed by viscosity when the defining constant of the dissipation wavenumber is chosen sufficiently small.

Hence the high derivative norm is not self-funded above the dissipation boundary:

$$
\boxed{
\frac d{dt}
\|u\|_{H^2}^2
\le
C f(t)
\|u\|_{H^2}^2.
}
\tag{1.9}
$$

For an actual concentrating return with

$$
H_{\rm out}
=
\Gamma^3H_{\rm in},
\qquad
\Gamma>1,
$$

one therefore obtains the scale-invariant supplier-activity debt

$$
\boxed{
\int_a^b
f(t)\,dt
\ge
c_4\log\Gamma.
}
\tag{1.10}
$$

The main structural conclusion is:

$$
\boxed{
\textbf{
a derivative-dominant UV tail may lose raw lower-order mass,
but it cannot simultaneously lose its scale-critical supplier atom
and its low-mode supplier activity.
}
}
$$

The remaining bridge is now causal/compactness-based:

> show that the recovered dissipation-boundary supplier atom belongs to the same actual singular return chain and therefore either re-profiles under MORP or leaves a nonzero native transition/escape residual.

---

# 2. Dissipation wavenumber

For a smooth Navier--Stokes state define

$$
\Lambda(t)
=
\lambda_{Q(t)}
$$

by

$$
\boxed{
\Lambda(t)
=
\min
\left\{
\lambda_q:
\lambda_p^{-1}
\|u_p(t)\|_\infty
<
c_0\nu
\quad
\forall p>q
\right\}.
}
\tag{2.1}
$$

This is the

$$
r=\infty
$$

specialization of the Cheskidov--Dai dissipation wavenumber.

For a smooth state the dyadic amplitudes decay faster than every power at high frequency, so

$$
\Lambda(t)<\infty.
$$

The region

$$
p>Q(t)
$$

is the dissipation range in the sense that the high-frequency nonlinear contributions are small enough to be absorbed into the viscous term.

---

# 3. Boundary shell lower bound

Cheskidov--Dai record directly that if

$$
1<\Lambda(t)<\infty,
$$

then

$$
\boxed{
\|u_{Q(t)}(t)\|_\infty
\ge
c_0\nu
\Lambda(t)
}
\tag{3.1}
$$

for the Navier--Stokes

$$
r=\infty
$$

case.

This follows from minimality of

$$
Q(t).
$$

Indeed, if the boundary shell and every shell above it all satisfied the strict high-frequency smallness condition at the previous dyadic cutoff, then

$$
Q(t)
$$

would not be minimal.

Status:

$$
\boxed{
\textbf{PRIMARY-SOURCE ESTABLISHED}.
}
$$

---

# 4. NEW THEOREM — critical kinetic supplier atom

## Theorem 4.1

At every smooth time with

$$
1<\Lambda(t)<\infty,
$$

the dissipation-boundary shell satisfies

$$
\boxed{
\Lambda(t)
\|u_{Q(t)}(t)\|_2^2
\ge
c_1\nu^2.
}
\tag{4.1}
$$

### Proof

Bernstein gives

$$
\|u_Q\|_\infty
\le
C_B
\Lambda^{3/2}
\|u_Q\|_2.
$$

By (3.1),

$$
c_0\nu\Lambda
\le
C_B
\Lambda^{3/2}
\|u_Q\|_2.
$$

Hence

$$
\|u_Q\|_2
\ge
\frac{c_0}{C_B}
\nu
\Lambda^{-1/2}.
$$

Squaring and multiplying by

$$
\Lambda
$$

gives

$$
\Lambda
\|u_Q\|_2^2
\ge
\frac{c_0^2}{C_B^2}
\nu^2.
$$

Set

$$
c_1
=
\frac{c_0^2}{C_B^2}.
$$

$$
\square
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 5. Scale invariance of the supplier atom

Under Navier--Stokes scaling

$$
u_a(x,t)
=
a
u(ax,a^2t),
$$

a dyadic shell at frequency

$$
\lambda_q
$$

moves to frequency

$$
a\lambda_q.
$$

The shell

$$
L^2
$$

norm obeys

$$
\|(u_a)_{q+\log_2a}\|_2^2
=
a^{-1}
\|u_q\|_2^2
$$

up to the standard bounded dyadic-index ambiguity.

Therefore

$$
(a\lambda_q)
\left[
a^{-1}
\|u_q\|_2^2
\right]
=
\lambda_q
\|u_q\|_2^2.
$$

Thus

$$
\boxed{
\lambda_q\|u_q\|_2^2
}
\tag{5.1}
$$

is parabolic-scale invariant.

The lower bound (4.1) is therefore an intrinsic critical amplitude statement, not a raw-energy statement.

---

# 6. NEW THEOREM — unit-frequency supplier recovery

Let

$$
\Lambda
=
\lambda_Q.
$$

Define the critically rescaled boundary shell

$$
\boxed{
v_Q(y)
=
\Lambda^{-1}
u_Q
\left(
x_0+\Lambda^{-1}y
\right).
}
\tag{6.1}
$$

The Fourier support of

$$
v_Q
$$

lies in a fixed annulus

$$
c\le|\eta|\le C
$$

independent of

$$
Q.
$$

## Theorem 6.1

There exists a translation

$$
x_0
$$

such that

$$
\boxed{
\|v_Q\|_\infty
\ge
c_0\nu,
}
\tag{6.2}
$$

$$
\boxed{
\|v_Q\|_2^2
\ge
c_1\nu^2,
}
\tag{6.3}
$$

and for universal

$$
r_0,c_2>0,
$$

$$
\boxed{
\int_{B_{r_0}(0)}
|v_Q(y)|^2\,dy
\ge
c_2\nu^2.
}
\tag{6.4}
$$

### Proof

From (3.1),

$$
\|v_Q\|_\infty
=
\Lambda^{-1}
\|u_Q\|_\infty
\ge
c_0\nu.
$$

Also:

$$
\|v_Q\|_2^2
=
\Lambda
\|u_Q\|_2^2
\ge
c_1\nu^2.
$$

Let

$$
M
=
\|v_Q\|_\infty.
$$

Choose

$$
y_0
$$

with

$$
|v_Q(y_0)|
\ge
\frac34M.
$$

Translate so that

$$
y_0=0.
$$

Because

$$
v_Q
$$

is supported in a fixed Fourier annulus, Bernstein gives

$$
\|\nabla v_Q\|_\infty
\le
C_0M.
$$

Choose

$$
r_0
=
\frac1{4C_0}.
$$

Then for

$$
|y|\le r_0,
$$

$$
|v_Q(y)-v_Q(0)|
\le
C_0Mr_0
\le
\frac14M.
$$

Therefore

$$
|v_Q(y)|
\ge
\frac12M
\ge
\frac{c_0}{2}\nu
$$

throughout

$$
B_{r_0}.
$$

Hence

$$
\int_{B_{r_0}}
|v_Q|^2
\ge
|B_{r_0}|
\frac{c_0^2}{4}
\nu^2.
$$

Set

$$
c_2
=
|B_{r_0}|
\frac{c_0^2}{4}.
$$

$$
\square
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 7. Interpretation — the supplier is not a vanishing profile

DCRP-07 showed that the derivative-dominant tail itself can have

$$
K_{\rm UV},
E_{\rm UV},
H_{\rm UV}
\to0
$$

while carrying almost all of

$$
Z^2.
$$

Theorem 6.1 shows that the dynamically defined dissipation-boundary supplier behaves differently.

After scaling to its own natural frequency:

$$
\boxed{
\text{supplier shell}
\Longrightarrow
\text{fixed local }L^2\text{ amplitude}.
}
$$

Thus:

$$
\boxed{
\textbf{
derivative invisibility does not imply supplier invisibility.
}
}
\tag{7.1}
$$

The high derivative tail may be lower-order invisible **at its own UV location**, but the nonlinear/viscous interface that permits such a tail contains a scale-critical lower-order atom.

---

# 8. Compactness dichotomy at the supplier scale

Consider a sequence of times

$$
t_n\uparrow T
$$

with

$$
\Lambda_n
=
\Lambda(t_n)
\to\infty.
$$

Let

$$
v_n
$$

be the full state rescaled to the supplier scale

$$
\Lambda_n^{-1},
$$

translated according to Theorem 6.1.

Its unit shell component satisfies

$$
\boxed{
\int_{B_{r_0}}
|P_{\sim1}v_n|^2
\ge
c_2\nu^2.
}
\tag{8.1}
$$

There are now only two possibilities.

## Compact supplier branch

If the rescaled full states have a uniform local compactness bound strong enough to pass the fixed Littlewood--Paley shell, then after subsequence extraction

$$
v_n\to v_\ast
$$

locally in a topology for which

$$
P_{\sim1}v_n\to P_{\sim1}v_\ast
$$

strongly in

$$
L^2(B_{r_0}),
$$

and therefore

$$
\boxed{
P_{\sim1}v_\ast\ne0.
}
\tag{8.2}
$$

This gives a genuine nonzero state-visible reprofile.

## Noncompact supplier branch

If no such local compactness is available, then the supplier scale itself produces an explicit state compactness / amplitude / tail defect.

Therefore the supplier cannot disappear silently.

Status:

$$
\boxed{
\textbf{CONDITIONAL REPROFILE DICHOTOMY}.
}
$$

The missing condition is precisely the local compactness transfer for the full state at the supplier scale.

---

# 9. Cheskidov--Dai high-frequency flux estimate

For the Navier--Stokes equation, Cheskidov--Dai derive for any

$$
s>\frac12
$$

an

$$
H^s
$$

energy estimate based on the dissipation wavenumber.

Define

$$
\boxed{
f(t)
=
\sum_{q\le Q(t)}
\lambda_q
\|u_q(t)\|_\infty.
}
\tag{9.1}
$$

Their Bony/commutator estimate for the nonlinear velocity flux gives, schematically,

$$
\boxed{
|I_s|
\le
C_1c_0\nu
\sum_{q>Q-3}
\lambda_q^{2s+2}
\|u_q\|_2^2
+
C_2f(t)
\sum_q
\lambda_q^{2s}
\|u_q\|_2^2.
}
\tag{9.2}
$$

For the Navier--Stokes case they allow every

$$
s>\frac12.
$$

Choose

$$
s=2.
$$

Then:

$$
\boxed{
|I_2|
\le
C_1c_0\nu
\sum_{q>Q-3}
\lambda_q^{6}
\|u_q\|_2^2
+
C_2f(t)
\sum_q
\lambda_q^{4}
\|u_q\|_2^2.
}
\tag{9.3}
$$

If

$$
c_0
$$

is chosen sufficiently small, the first term is absorbed by the viscous

$$
H^3
$$

dissipation.

Thus:

$$
\boxed{
\frac d{dt}
\sum_q
\lambda_q^4
\|u_q\|_2^2
\le
C f(t)
\sum_q
\lambda_q^4
\|u_q\|_2^2.
}
\tag{9.4}
$$

This is the frequency-localized counterpart of the global

$$
H^2
$$

interaction estimate in DCRP-07.

Status:

$$
\boxed{
\textbf{PRIMARY-SOURCE ESTABLISHED modulo equivalent Littlewood--Paley norm constants}.
}
$$

---

# 10. Supplier interpretation of the flux estimate

Equation (9.3) has a structural meaning.

Above

$$
Q(t),
$$

the high-frequency self-interaction contribution is small enough to be absorbed by viscosity.

The remaining non-absorbable growth is controlled by

$$
f(t),
$$

which contains only modes

$$
q\le Q(t).
$$

Thus:

$$
\boxed{
\textbf{
the high derivative range is not self-sustaining above the dissipation wavenumber;
its non-absorbable growth is mediated by the supplier side }q\le Q(t).
}
}
\tag{10.1}
$$

This provides the desired qualitative low--high bridge.

It does not yet identify one unique triadic causal path from

$$
u_Q
$$

to the derivative tail.

That stronger causal assignment remains open.

---

# 11. NEW THEOREM — supplier activity debt for a scale return

Define the dyadic

$$
H^2
$$

energy

$$
\boxed{
\mathcal H_2(t)
=
\sum_q
\lambda_q^4
\|u_q(t)\|_2^2.
}
\tag{11.1}
$$

It is equivalent to

$$
\|u(t)\|_{\dot H^2}^2,
$$

and hence to the strain quantity

$$
H(t)
=
\|S(t)\|_{\dot H^1}^2
$$

up to universal constants.

Suppose an actual forward concentrating return satisfies an exact physical scale gain

$$
\boxed{
\mathcal H_2(b)
=
\Gamma^3
\mathcal H_2(a),
\qquad
\Gamma>1.
}
\tag{11.2}
$$

Then:

$$
\boxed{
\int_a^b
f(t)\,dt
\ge
c_4
\log\Gamma.
}
\tag{11.3}
$$

### Proof

Equation (9.4) gives

$$
\frac d{dt}
\log\mathcal H_2(t)
\le
Cf(t)
$$

whenever

$$
\mathcal H_2>0.
$$

Integrating:

$$
\log
\frac{
\mathcal H_2(b)
}{
\mathcal H_2(a)
}
\le
C
\int_a^b
f(t)\,dt.
$$

Using (11.2):

$$
3\log\Gamma
\le
C
\int_a^b
f(t)\,dt.
$$

Hence:

$$
\boxed{
\int_a^b
f(t)\,dt
\ge
\frac3C
\log\Gamma.
}
$$

$$
\square
$$

Status:

$$
\boxed{
\textbf{PROVED assuming the exact return gain and the Cheskidov--Dai }s=2\textbf{ estimate}.
}
$$

---

# 12. Scale invariance of supplier activity

Each summand

$$
\lambda_q
\|u_q\|_\infty
$$

has physical dimension

$$
{\rm time}^{-1}.
$$

Under Navier--Stokes scaling

$$
u_a(x,t)
=
a
u(ax,a^2t),
$$

it transforms as

$$
\lambda_q
\|u_q\|_\infty
\mapsto
a^2
\lambda_q
\|u_q\|_\infty
$$

after the corresponding dyadic index shift.

Since

$$
dt\mapsto a^{-2}dt,
$$

the integral

$$
\boxed{
\int
f(t)\,dt
}
\tag{12.1}
$$

is scale invariant up to bounded dyadic partition constants.

Thus (11.3) is a genuine critical return cost.

---

# 13. NEW THEOREM — hypothetical blowup forces unbounded supplier frequency

Let

$$
u
$$

be a maximal smooth / strong solution on

$$
[0,T_{\max}),
$$

and suppose

$$
T_{\max}<\infty.
$$

Then:

$$
\boxed{
\limsup_{t\uparrow T_{\max}}
\Lambda(t)
=
+\infty.
}
\tag{13.1}
$$

### Proof

Assume instead that

$$
\Lambda(t)
\le\Lambda_0
$$

for all sufficiently late

$$
t.
$$

Then

$$
Q(t)\le Q_0
$$

for a fixed integer

$$
Q_0.
$$

Using Bernstein and the global kinetic-energy bound

$$
\|u(t)\|_2
\le
\|u(0)\|_2,
$$

for every fixed

$$
q\le Q_0,
$$

$$
\lambda_q
\|u_q(t)\|_\infty
\le
C
\lambda_q^{5/2}
\|u(0)\|_2.
$$

Therefore

$$
f(t)
=
\sum_{q\le Q(t)}
\lambda_q
\|u_q(t)\|_\infty
\le
C(Q_0,\|u(0)\|_2)
$$

uniformly near

$$
T_{\max}.
$$

Apply the Cheskidov--Dai estimate with

$$
s=2:
$$

$$
\frac d{dt}
\|u(t)\|_{H^2}^2
\le
C f(t)
\|u(t)\|_{H^2}^2.
$$

Gronwall gives a uniform

$$
H^2
$$

bound up to

$$
T_{\max}.
$$

Such a bound continues the strong Navier--Stokes solution beyond

$$
T_{\max},
$$

contradiction.

Hence

$$
\Lambda(t)
$$

must be unbounded.

$$
\square
$$

Status:

$$
\boxed{
\textbf{PROVED in the standard strong-solution continuation class}.
}
$$

---

# 14. Corollary — arbitrarily high critical supplier atoms

From Theorem 13.1, any hypothetical finite-time singularity admits times

$$
t_n\uparrow T_{\max}
$$

with

$$
\Lambda_n
=
\Lambda(t_n)
\to\infty.
$$

At each such time, Theorem 4.1 gives

$$
\boxed{
\Lambda_n
\|u_{Q_n}(t_n)\|_2^2
\ge
c_1\nu^2.
}
\tag{14.1}
$$

and Theorem 6.1 gives a critically rescaled translated shell with

$$
\boxed{
\int_{B_{r_0}}
|v_{Q_n}|^2
\ge
c_2\nu^2.
}
\tag{14.2}
$$

Therefore:

$$
\boxed{
\textbf{
finite-time blowup would require an unbounded sequence of
nonvanishing scale-critical supplier atoms.
}
}
\tag{14.3}
$$

This is a lower-order state-visible object at arbitrarily small physical scales.

---

# 15. Relation to the DCRP-07 derivative visibility no-go

DCRP-07 proved that an ultraviolet tail can have raw shell kinetic energy as small as

$$
K_{\rm UV}
\sim
N^{-5}
$$

while dominating

$$
Z^2.
$$

The present theorem does not contradict that construction.

Instead it says:

if such a derivative-dominant tail is part of an actual Navier--Stokes singular mechanism, then somewhere at the dynamically selected dissipation boundary there must also be a supplier shell with

$$
\boxed{
K_Q
\gtrsim
\nu^2
\Lambda^{-1}.
}
\tag{15.1}
$$

The raw energy

$$
K_Q
$$

still tends to zero as

$$
\Lambda\to\infty.
$$

That is exactly critical scaling.

After renormalization:

$$
\boxed{
\Lambda K_Q
\gtrsim\nu^2.
}
\tag{15.2}
$$

Thus the old raw-summability obstruction remains true, but the reprofile obstruction is stronger:

$$
\boxed{
\text{critical supplier atom does not vanish under its own scale normalization}.
}
$$

---

# 16. Atomic supplier versus diffuse derivative tail

The final state-visible picture is now asymmetric.

The extreme derivative tail may be diffuse in

$$
\mu_Z
$$

or may carry only vanishing base mass.

But the dissipation boundary itself carries an atomic critical lower-order state:

$$
\boxed{
\lambda_Q\|u_Q\|_2^2
\gtrsim\nu^2.
}
$$

Hence a surviving singular mechanism has the form

$$
\boxed{
\text{critical supplier atom}
\longrightarrow
\text{possibly diffuse derivative UV tail}.
}
\tag{16.1}
$$

The remaining mathematical question is no longer whether a lower-order atom exists.

It does.

The question is whether that supplier atom can fail to enter the same compact / causal return object used by MORP.

---

# 17. Connection to MORP atomic reprofile

MORP-05 proves schematically:

$$
\text{fixed-share atom}
\Longrightarrow
\text{recenter}
+
\text{rescale}
+
\text{extract nonzero profile}.
$$

Theorem 6.1 supplies exactly the first two analytic ingredients for the dissipation-boundary shell:

- natural scale;
- natural spatial center;
- fixed local shell amplitude after critical rescaling.

Therefore a direct MORP-compatible closure would follow from:

$$
\boxed{
\textbf{Supplier Compactness Bridge}.
}
$$

Desired statement:

> Along an actual singular return chain, the full Navier--Stokes states normalized at the dissipation-boundary supplier scales satisfy the local compactness package required to pass the fixed unit shell.
>
> Then the uniform lower bound
>
> $$
> \int_{B_{r_0}}
> |P_{\sim1}v_n|^2
> \ge
> c\nu^2
> $$
>
> yields a nonzero actual state profile.

If the compactness package fails, that failure must be retained as a state/pressure/defect/escape coordinate.

This is a much narrower bridge than the previous generic UV Flux Bridge.

---

# 18. Supplier activity and the existing low-mode regularity criterion

The Cheskidov--Dai regularity criterion further shows that regularity is controlled by the time integral of low-mode vorticity activity below the dissipation wavenumber.

In the Navier--Stokes case, finite-time blowup requires the corresponding critical low-mode activity condition to fail.

Thus a hypothetical singularity has two simultaneous supplier signatures:

$$
\boxed{
\begin{aligned}
&\text{instantaneous critical atom at }Q(t),\\
&\text{nontrivial scale-invariant low-mode activity in time}.
\end{aligned}
}
\tag{18.1}
$$

This independently supports the conclusion that the UV derivative tail cannot be dynamically isolated from its lower-frequency supplier sector.

No claim is made that this regularity criterion alone proves global regularity.

---

# 19. What has been closed in this round

## Closed A — complete lower-order invisibility

It is false that an actual derivative-dominant singular mechanism may be invisible at **all** lower-order scales.

The dissipation boundary contains

$$
\boxed{
\Lambda\|u_Q\|_2^2
\ge
c\nu^2.
}
$$

## Closed B — vanishing supplier under critical re-scaling

After scaling the supplier shell to unit frequency and translating,

$$
\boxed{
\int_{B_{r_0}}
|v_Q|^2
\ge
c\nu^2.
}
$$

So the supplier shell cannot vanish as a normalized shell object.

## Closed C — purely self-funded UV derivative growth

Cheskidov--Dai's paraproduct estimate absorbs the high-frequency nonlinear contribution above the dissipation boundary and leaves growth controlled by the low-mode activity

$$
f(t).
$$

Therefore the non-absorbable derivative growth is supplier-mediated.

---

# 20. What remains open

The remaining gap is no longer a generic analytic flux inequality.

It is a **same-history compactness / causality bridge**.

One must prove that the recovered supplier shell belongs to the same actual singular mechanism that generated the derivative tail.

More specifically, at least one of the following must be established.

## Route A — actual supplier reprofile

The supplier-normalized full states have enough local compactness to extract a nonzero actual Navier--Stokes profile.

## Route B — supplier-to-UV causal edge

The low-mode activity

$$
f(t)
$$

that pays for derivative growth can be localized to an actual transition edge already represented in the MORP return/transition ledger.

## Route C — noncompactness is itself retained

Failure of Route A produces a nonzero native compactness / escape / pressure / derivative defect rather than disappearing.

The key point is:

$$
\boxed{
\text{the supplier cannot be both nonzero and absent from every completed package coordinate}.
}
$$

This last sentence is still a target, not yet a proved theorem.

---

# 21. Next exact target

The next proof target is:

$$
\boxed{
\textbf{Supplier Compactness--Causality Lemma}.
}
$$

A useful sufficient version is:

Let

$$
t_n\uparrow T_{\max}
$$

be singular-approach times with

$$
\Lambda_n\to\infty.
$$

Normalize and recenter the full state at the dissipation-boundary shell:

$$
v_n(y,s)
=
\Lambda_n^{-1}
u
\left(
x_n+\Lambda_n^{-1}y,
t_n+\Lambda_n^{-2}s
\right).
$$

The unit shell satisfies

$$
\int_{B_{r_0}}
|P_{\sim1}v_n(y,0)|^2\,dy
\ge
c\nu^2.
$$

Prove one of:

1. the full state sequence has a locally compact subsequence and the limit has

   $$
   P_{\sim1}v_\ast\ne0;
   $$

2. a specific MORP native defect coordinate is strictly positive;

3. the supplier scale cannot be causally connected to the derivative-growth return, in which case the Cheskidov--Dai low-mode flux estimate must be sharpened to identify the actual supplying shell/edge.

If (1) is proved on the minimal-return branch, MORP atomic reprofile applies.

If (2) is proved, zero-cost minimality fails.

Only (3) can continue to escape.

Thus the next frontier has been reduced to a causal localization problem.

---

# 22. Source ledger

## Cheskidov--Dai

Alexey Cheskidov and Mimi Dai, *Regularity criteria for the 3D Navier-Stokes and MHD equations*, arXiv:1507.06611v6.

Primary facts used:

- dissipation wavenumber

  $$
  \Lambda_r(t)
  =
  \min
  \left\{
  \lambda_q:
  \lambda_p^{-1+3/r}
  \|u_p\|_r
  <
  c_r\nu
  \quad
  \forall p>q
  \right\};
  $$

- for the Navier--Stokes case,

  $$
  r=\infty
  $$

  is allowed;

- boundary lower bound

  $$
  \|u_Q\|_\infty
  \ge
  c\nu\Lambda;
  $$

- low-mode activity

  $$
  f(t)
  =
  \sum_{q\le Q(t)}
  \lambda_q
  \|u_q(t)\|_\infty;
  $$

- for Navier--Stokes and any

  $$
  s>\frac12,
  $$

  the Littlewood--Paley nonlinear flux estimate absorbs the high-frequency contribution above the dissipation wavenumber and leaves an

  $$
  f(t)\|u\|_{H^s}^2
  $$

  growth term.

## Cheskidov--Shvydkoy

Alexey Cheskidov and Roman Shvydkoy, *A unified approach to regularity problems for the 3D Navier-Stokes and Euler equations: the use of Kolmogorov's dissipation range*, arXiv:1102.1944.

Used as conceptual calibration for the interpretation of the dissipation wavenumber as the boundary between Euler-dominated and viscosity-dominated frequency ranges.

No novelty / priority claim is made for the dissipation-wavenumber framework.

The supplier-atom and MORP bridge deductions are internal derivations and require independent audit.

---

# 23. End state

The UV Flux Bridge problem has been reduced.

The derivative-dominant tail itself can remain lower-order raw-mass invisible.

But the actual Navier--Stokes dissipation boundary necessarily satisfies

$$
\boxed{
\|u_Q\|_\infty
\gtrsim
\nu\Lambda,
}
$$

and

$$
\boxed{
\Lambda\|u_Q\|_2^2
\gtrsim
\nu^2.
}
$$

After critical rescaling and recentering,

$$
\boxed{
\int_{B_{r_0}}
|P_{\sim1}v|^2
\gtrsim
\nu^2.
}
$$

Furthermore, high derivative growth above the dissipation boundary is controlled by the low-mode supplier activity

$$
f(t).
$$

Therefore:

$$
\boxed{
\textbf{
the final UV escape has acquired a nonvanishing lower-order supplier atom.
}
}
$$

The next single frontier is:

$$
\boxed{
\textbf{
Supplier Compactness--Causality Lemma}.
}
$$

That is the next exact attack.

---

# Checkpoint v9 Update — DCRP-09

# NS-DCRP-09 — Duhamel Supplier Ancestry, Actual-History Causality, and Triadic Parent Reduction

- date: 2026-08-16
- status: research proof checkpoint
- canonical source: UTF-8 Markdown
- canonical math delimiters: `$...$` and `$$...$$`
- objective: continue DCRP-08 by proving that the nonvanishing dissipation-boundary supplier shell is not merely an instantaneous frequency marker but is necessarily connected to an actual same-history nonlinear Navier--Stokes ancestry.
- no full Navier--Stokes regularity claim is made.
- principal internal dependencies: MORP-02 through MORP-05, DCRP-07, DCRP-08.
- principal external primary source: Cheskidov--Dai, arXiv:1507.06611v6.
- secondary external calibration: Gallagher--Koch--Planchon, arXiv:1012.0145v3.

---

# 1. Executive result

DCRP-08 proved that the Navier--Stokes dissipation-boundary shell

$$
Q(t)
$$

satisfies the critical lower bound

$$
\boxed{
\lambda_{Q(t)}
\|u_{Q(t)}(t)\|_2^2
\ge
c_1\nu^2.
}
\tag{1.1}
$$

Equivalently, with

$$
A_q(t)
=
\lambda_q^{1/2}
\|u_q(t)\|_2,
$$

one has

$$
\boxed{
A_{Q(t)}(t)
\ge
a_0\nu
}
\tag{1.2}
$$

for a universal

$$
a_0>0.
$$

The remaining question was whether this supplier shell belongs to the actual same-history singular mechanism or could be only an instantaneous frequency artifact.

This round proves an actual-history Duhamel ancestry theorem.

For a fixed shell

$$
q
$$

define the nonlinear source

$$
\boxed{
F_q
=
\Delta_q
\mathbb P
\nabla\cdot
(u\otimes u),
}
\tag{1.3}
$$

where

$$
\mathbb P
$$

is the Leray projector.

Define the scale-critical integrated nonlinear input

$$
\boxed{
\mathfrak J_q[t_0,t_1]
=
\lambda_q^{1/2}
\int_{t_0}^{t_1}
\|F_q(s)\|_2
\,ds.
}
\tag{1.4}
$$

Then

$$
\mathfrak J_q
$$

is exactly invariant under Navier--Stokes parabolic scaling, up to the standard bounded dyadic-index shift.

For a boundary supplier shell

$$
Q=Q(t)
$$

with

$$
A_Q(t)\ge a_0\nu,
$$

let

$$
K_0
=
\|u(0)\|_2^2.
$$

Choose the backward interval

$$
\boxed{
\tau_Q
=
\frac{
1
}{
c_h\nu\lambda_Q^2
}
\log
\left(
\frac{
2\lambda_Q^{1/2}K_0^{1/2}
}{
a_0\nu
}
\right),
}
\tag{1.5}
$$

whenever the logarithm is positive and

$$
t-\tau_Q\ge0.
$$

Here

$$
c_h>0
$$

is the universal heat-decay constant on the fixed Littlewood--Paley annulus.

Then:

$$
\boxed{
\mathfrak J_Q[t-\tau_Q,t]
\ge
\frac{
a_0
}{
2
}
\nu.
}
\tag{1.6}
$$

Thus a sufficiently high supplier shell cannot be explained solely by linear heat persistence from the earlier state.

It must receive a fixed nonzero amount of nonlinear forcing on the same actual Navier--Stokes trajectory.

Bony decomposition then yields an exact triadic ancestry reduction:

$$
\boxed{
\mathfrak J_Q^{LH}
+
\mathfrak J_Q^{HL}
+
\mathfrak J_Q^{HH}
\ge
\frac{
a_0
}{
2
}
\nu,
}
\tag{1.7}
$$

so at least one of

$$
LH,
\qquad
HL,
\qquad
HH
$$

carries a fixed critical nonlinear input.

Consequently:

$$
\boxed{
\textbf{
the supplier atom has an actual same-history nonlinear parent class.
}
}
\tag{1.8}
$$

The causal part of the Supplier Compactness--Causality problem is therefore closed at the aggregate triadic level.

What remains is parent extraction:

> from the nonzero low--high / high--low / high--high forcing class, extract a nonvanishing parent profile under admissible re-rooting, or prove that failure of extraction leaves a retained transition / derivative defect.

---

# 2. Source precision check for DCRP-08

Cheskidov--Dai define for Navier--Stokes the dissipation wavenumber

$$
\Lambda_r(t)
=
\min
\left\{
\lambda_q:
\lambda_p^{-1+3/r}
\|u_p(t)\|_r
<
c_r\nu
\quad
\forall p>q
\right\}.
$$

For the pure Navier--Stokes equation,

$$
r=\infty
$$

is allowed.

The velocity nonlinear flux

$$
I
$$

obeys, in their Lemma 3.2, for **every**

$$
s>0
$$

and

$$
r\ge2,
$$

$$
\boxed{
|I|
\lesssim
c_r\nu
\sum_{q>Q-3}
\lambda_q^{2s+2}
\|u_q\|_2^2
+
f(t)
\sum_{q\ge-1}
\lambda_q^{2s}
\|u_q\|_2^2.
}
\tag{2.1}
$$

Therefore the DCRP-08 use of

$$
s=2
$$

for the pure Navier--Stokes velocity equation is valid.

The restriction

$$
\frac12<s<1
$$

appearing later in the paper is generated by the additional magnetic flux terms in MHD and is not a restriction on Lemma 3.2 for the pure Navier--Stokes velocity flux.

This source audit confirms the DCRP-08

$$
H^2
$$

supplier-activity estimate.

Status:

$$
\boxed{
\textbf{SOURCE AUDIT PASSED}.
}
$$

---

# 3. Fixed-shell mild equation

Let

$$
u
$$

be a smooth Navier--Stokes solution on

$$
[t_0,t_1].
$$

The mild equation is

$$
u(t_1)
=
e^{\nu(t_1-t_0)\Delta}
u(t_0)
-
\int_{t_0}^{t_1}
e^{\nu(t_1-s)\Delta}
\mathbb P
\nabla\cdot
(u\otimes u)(s)
\,ds.
$$

Since

$$
\Delta_q,
\qquad
e^{t\Delta},
\qquad
\mathbb P
$$

are Fourier multipliers, they commute.

Therefore:

$$
\boxed{
u_q(t_1)
=
e^{\nu(t_1-t_0)\Delta}
u_q(t_0)
-
\int_{t_0}^{t_1}
e^{\nu(t_1-s)\Delta}
F_q(s)
\,ds.
}
\tag{3.1}
$$

where

$$
F_q
=
\Delta_q
\mathbb P
\nabla\cdot
(u\otimes u).
$$

This is an exact same-history identity.

---

# 4. Heat decay on one Littlewood--Paley shell

For

$$
q\ge0,
$$

the Fourier support of

$$
u_q
$$

lies in a fixed annulus:

$$
c_-\lambda_q
\le
|\xi|
\le
c_+\lambda_q.
$$

Hence:

$$
\boxed{
\left\|
e^{\nu\tau\Delta}
u_q
\right\|_2
\le
e^{-c_h\nu\lambda_q^2\tau}
\|u_q\|_2
}
\tag{4.1}
$$

for a universal

$$
c_h>0.
$$

This follows directly from the Fourier multiplier

$$
e^{-\nu\tau|\xi|^2}.
$$

No nonlinear estimate is used.

---

# 5. Definition — critical shell amplitude and Duhamel forcing debt

Define:

$$
\boxed{
A_q(t)
=
\lambda_q^{1/2}
\|u_q(t)\|_2.
}
\tag{5.1}
$$

This quantity is critical under the three-dimensional Navier--Stokes scaling.

Define:

$$
\boxed{
\mathfrak J_q[t_0,t_1]
=
\lambda_q^{1/2}
\int_{t_0}^{t_1}
\|F_q(s)\|_2
\,ds.
}
\tag{5.2}
$$

From (3.1), heat contraction, and (4.1):

$$
\boxed{
A_q(t_1)
\le
e^{-c_h\nu\lambda_q^2(t_1-t_0)}
A_q(t_0)
+
\mathfrak J_q[t_0,t_1].
}
\tag{5.3}
$$

This is the basic ancestry inequality.

---

# 6. Scale invariance of the Duhamel forcing debt

Under

$$
u_a(x,t)
=
a
u(ax,a^2t),
$$

the nonlinear source scales as

$$
F_a(x,t)
=
a^3
F(ax,a^2t).
$$

Therefore:

$$
\|F_a(t)\|_2
=
a^{3/2}
\|F(a^2t)\|_2.
$$

The corresponding frequency scales as

$$
\lambda_q
\mapsto
a\lambda_q.
$$

Hence:

$$
(a\lambda_q)^{1/2}
\|F_a(t)\|_2
\,dt
=
a^{1/2}
\lambda_q^{1/2}
a^{3/2}
\|F(a^2t)\|_2
\,dt.
$$

Since

$$
ds
=
a^2dt,
$$

one obtains:

$$
\boxed{
\mathfrak J_q
\text{ is parabolic-scale invariant}.
}
\tag{6.1}
$$

The quantity

$$
\nu^{-1}\mathfrak J_q
$$

is therefore a dimensionless critical nonlinear input.

---

# 7. NEW THEOREM — Duhamel Supplier Ancestry

## Theorem 7.1

Let

$$
u
$$

be a smooth finite-energy Navier--Stokes solution.

Let

$$
q\ge0
$$

and

$$
t>0.
$$

Assume

$$
\boxed{
A_q(t)
\ge
a_0\nu.
}
\tag{7.1}
$$

Let

$$
K_0
=
\|u(0)\|_2^2.
$$

Assume

$$
\frac{
2\lambda_q^{1/2}K_0^{1/2}
}{
a_0\nu
}
>1.
$$

Define:

$$
\boxed{
\tau_q
=
\frac{
1
}{
c_h\nu\lambda_q^2
}
\log
\left(
\frac{
2\lambda_q^{1/2}K_0^{1/2}
}{
a_0\nu
}
\right).
}
\tag{7.2}
$$

If

$$
t-\tau_q\ge0,
$$

then:

$$
\boxed{
\mathfrak J_q[t-\tau_q,t]
\ge
\frac{
a_0
}{
2
}
\nu.
}
\tag{7.3}
$$

### Proof

By the global energy inequality,

$$
\|u_q(t-\tau_q)\|_2
\le
\|u(t-\tau_q)\|_2
\le
K_0^{1/2}.
$$

Therefore:

$$
A_q(t-\tau_q)
\le
\lambda_q^{1/2}
K_0^{1/2}.
$$

By definition of

$$
\tau_q,
$$

$$
e^{-c_h\nu\lambda_q^2\tau_q}
=
\frac{
a_0\nu
}{
2\lambda_q^{1/2}K_0^{1/2}
}.
$$

Hence:

$$
e^{-c_h\nu\lambda_q^2\tau_q}
A_q(t-\tau_q)
\le
\frac{
a_0
}{
2
}
\nu.
$$

Now use (5.3):

$$
a_0\nu
\le
A_q(t)
\le
\frac{
a_0
}{
2
}
\nu
+
\mathfrak J_q[t-\tau_q,t].
$$

Thus:

$$
\mathfrak J_q[t-\tau_q,t]
\ge
\frac{
a_0
}{
2
}
\nu.
$$

$$
\square
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 8. Application to the dissipation-boundary supplier

DCRP-08 gives:

$$
A_{Q(t)}(t)
\ge
a_0\nu.
$$

For any sequence

$$
t_n\uparrow T_{\max}
$$

such that

$$
\Lambda_n
=
\lambda_{Q(t_n)}
\to\infty,
$$

the associated

$$
\tau_{Q_n}
$$

satisfies:

$$
\boxed{
\tau_{Q_n}
\sim
\frac{
\log
\left(
C
K_0^{1/2}
\Lambda_n^{1/2}/\nu
\right)
}{
\nu\Lambda_n^2
}.
}
\tag{8.1}
$$

In particular:

$$
\boxed{
\tau_{Q_n}\to0.
}
\tag{8.2}
$$

For all sufficiently large

$$
n,
$$

one has

$$
t_n-\tau_{Q_n}>0.
$$

Theorem 7.1 yields:

$$
\boxed{
\mathfrak J_{Q_n}
[
t_n-\tau_{Q_n},
t_n
]
\ge
c\nu.
}
\tag{8.3}
$$

Thus every sufficiently high supplier atom near a hypothetical singular horizon has a fixed critical nonlinear ancestry on an actual physical interval shrinking to the singular time.

---

# 9. Normalized ancestry duration

The physical ancestry window is

$$
\tau_Q.
$$

In supplier-scale parabolic time, define

$$
\Theta_Q
=
\lambda_Q^2
\tau_Q.
$$

Then:

$$
\boxed{
\Theta_Q
=
\frac1{
c_h\nu
}
\log
\left(
\frac{
2\lambda_Q^{1/2}K_0^{1/2}
}{
a_0\nu
}
\right).
}
\tag{9.1}
$$

Therefore:

$$
\Theta_Q
\to\infty
$$

only logarithmically as

$$
Q\to\infty.
$$

Interpretation:

- the physical interval collapses like
  $$
  \lambda_Q^{-2}\log\lambda_Q;
  $$

- after scaling to the supplier frequency, the available ancestry interval becomes logarithmically long.

This creates room for an actual supplier-scale history, not merely a one-time slice.

---

# 10. Bony triadic decomposition of the supplier forcing

Using the sharp Bony decomposition,

$$
\Delta_Q
(u\cdot\nabla u)
$$

splits into three classes:

$$
\boxed{
F_Q
=
F_Q^{LH}
+
F_Q^{HL}
+
F_Q^{HH},
}
\tag{10.1}
$$

where schematically:

$$
\boxed{
F_Q^{LH}
=
\mathbb P
\sum_{|Q-p|\le2}
\Delta_Q
\left[
u_{\le p-2}
\cdot\nabla u_p
\right],
}
\tag{10.2}
$$

$$
\boxed{
F_Q^{HL}
=
\mathbb P
\sum_{|Q-p|\le2}
\Delta_Q
\left[
u_p
\cdot\nabla u_{\le p-2}
\right],
}
\tag{10.3}
$$

and

$$
\boxed{
F_Q^{HH}
=
\mathbb P
\sum_{p\ge Q-2}
\Delta_Q
\left[
u_p
\cdot\nabla\widetilde u_p
\right].
}
\tag{10.4}
$$

Define the three critical ancestry inputs:

$$
\boxed{
\mathfrak J_Q^{XY}[I]
=
\lambda_Q^{1/2}
\int_I
\|F_Q^{XY}(s)\|_2
\,ds,
}
\tag{10.5}
$$

for

$$
XY\in\{LH,HL,HH\}.
$$

By the triangle inequality:

$$
\boxed{
\mathfrak J_Q
\le
\mathfrak J_Q^{LH}
+
\mathfrak J_Q^{HL}
+
\mathfrak J_Q^{HH}.
}
\tag{10.6}
$$

Hence Theorem 7.1 gives:

$$
\boxed{
\max
\left\{
\mathfrak J_Q^{LH},
\mathfrak J_Q^{HL},
\mathfrak J_Q^{HH}
\right\}
\ge
\frac{
a_0
}{
6
}
\nu.
}
\tag{10.7}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 11. Causal meaning of the triadic lower bound

The three alternatives correspond to actual PDE ancestry classes.

## Low--high ancestry

A mode near

$$
Q
$$

is transported / deformed by lower frequencies.

## High--low ancestry

A near-

$$
Q
$$

mode acts on a lower-frequency field to create output at the supplier shell.

## High--high ancestry

Two frequencies at or above

$$
Q
$$

interact and feed the supplier shell.

Thus the supplier atom is not an isolated instantaneous feature.

At least one actual nonlinear triadic class contributes a fixed scale-critical amount on the same physical solution history.

Therefore the causal half of the former Supplier Compactness--Causality Lemma is closed at the aggregate paraproduct level:

$$
\boxed{
\textbf{
supplier atom}
\Longrightarrow
\textbf{
actual same-history nonlinear ancestry}.
}
\tag{11.1}
$$

No profile recurrence assumption is used for this implication.

---

# 12. External high-frequency activity persistence

Cheskidov--Dai prove the following regularity criterion for a Navier--Stokes solution regular on

$$
(0,T).
$$

In the

$$
r=\infty
$$

case, if the asymptotic high-shell vorticity activity while the shell lies below the dissipation wavenumber is sufficiently small, then the solution is regular at

$$
T.
$$

Therefore the contrapositive gives:

if

$$
T
$$

is a finite singular time, then

$$
\boxed{
\limsup_{q\to\infty}
\int_{T/2}^{T}
1_{\{q\le Q(t)\}}
\|\Delta_q\omega(t)\|_\infty
\,dt
>
c_\ast
}
\tag{12.1}
$$

for the theorem's small universal threshold

$$
c_\ast>0.
$$

On a fixed dyadic shell,

$$
\|\Delta_q\omega\|_\infty
\sim
\lambda_q
\|u_q\|_\infty
$$

up to bounded Littlewood--Paley constants.

Therefore a hypothetical singularity requires nontrivial time-integrated supplier-side activity at arbitrarily high fixed frequencies.

This independently rules out the picture in which the supplier atoms are isolated one-time spikes with no persistent actual-history activity.

Status:

$$
\boxed{
\textbf{PRIMARY-SOURCE CONSEQUENCE}.
}
$$

---

# 13. What has now been closed

The previous frontier asked whether the critical supplier shell is causally connected to the same actual Navier--Stokes history.

The answer is now yes in the following rigorous sense.

For arbitrarily high supplier scales in a hypothetical singular approach:

$$
\boxed{
A_Q(t)
\gtrsim\nu
}
$$

and the linear heat memory over a short backward interval can be made smaller than half this amount.

Therefore:

$$
\boxed{
\mathfrak J_Q
\gtrsim\nu.
}
$$

The supplier must be nonlinearly regenerated.

Moreover:

$$
\boxed{
\text{one of }
LH,\ HL,\ HH
\text{ supplies a fixed critical ancestry amount}.
}
$$

Thus:

$$
\boxed{
\textbf{
the supplier is an actual dynamically generated node,
not merely a normalization artifact.
}
}
$$

---

# 14. What has not yet been closed

The triadic ancestry lower bound is aggregate.

It does not yet imply that one individual parent shell carries a fixed share.

In particular the

$$
HH
$$

term contains

$$
p\ge Q-2
$$

and can, in principle, be generated by a diffuse sum over arbitrarily high parent shells.

Likewise a low-frequency aggregate in the

$$
LH
$$

or

$$
HL
$$

term may itself be distributed over many lower shells.

Therefore:

$$
\boxed{
\text{aggregate causal ancestry}
\not\Rightarrow
\text{single parent profile}.
}
\tag{14.1}
$$

This is now the exact remaining compactness/extraction issue.

---

# 15. Parent extraction problem

For a supplier interval

$$
I_Q
=
[t-\tau_Q,t],
$$

suppose:

$$
\mathfrak J_Q^{HH}[I_Q]
\ge
c\nu.
$$

Write:

$$
F_Q^{HH}
=
\sum_{p\ge Q-2}
F_{Q,p}^{HH}.
$$

Then:

$$
\mathfrak J_Q^{HH}
\le
\sum_{p\ge Q-2}
\mathfrak J_{Q,p}^{HH},
$$

where:

$$
\boxed{
\mathfrak J_{Q,p}^{HH}
=
\lambda_Q^{1/2}
\int_{I_Q}
\|F_{Q,p}^{HH}(s)\|_2
\,ds.
}
\tag{15.1}
$$

There are two possibilities.

### Atomic parent

There exists

$$
\eta_0>0
$$

and parent indices

$$
p_Q
$$

such that:

$$
\boxed{
\mathfrak J_{Q,p_Q}^{HH}
\ge
\eta_0\nu.
}
\tag{15.2}
$$

This gives a selected actual parent scale.

### Diffuse parent

$$
\boxed{
\sup_{p\ge Q-2}
\mathfrak J_{Q,p}^{HH}
\to0
}
\tag{15.3}
$$

while the total remains bounded below.

Then the number / entropy of active parent scales must diverge.

This is a parent-interaction analogue of MORP-05 diffuse multiplicity.

The difference is that the object is now an **actual Duhamel causal contribution**, not merely an abstract carrier coordinate.

---

# 16. Low--high parent localization

For

$$
LH
$$

and

$$
HL,
$$

the high parent index satisfies:

$$
|p-Q|\le2.
$$

Therefore one parent is automatically at the supplier scale.

The only possible diffusion occurs in the lower-frequency aggregate:

$$
u_{\le p-2}.
$$

Hence if either:

$$
\mathfrak J_Q^{LH}
\gtrsim\nu
$$

or:

$$
\mathfrak J_Q^{HL}
\gtrsim\nu,
$$

then:

$$
\boxed{
\textbf{
the actual causal edge contains a fixed near-supplier-scale parent.
}
}
\tag{16.1}
$$

The remaining issue is whether the low-frequency co-parent can be localized or whether a distributed low-mode shear is essential.

This is strictly narrower than the original full UV-tail problem.

---

# 17. Galilean invariance

The supplier-shell and Duhamel-source construction is insensitive to adding a spatially constant velocity.

For

$$
q\ge0,
$$

$$
\Delta_q c
=
0.
$$

Thus:

$$
u_q
$$

and the critical shell amplitude

$$
A_q
$$

are Galilean invariant at nonzero dyadic frequencies after the corresponding coordinate shift.

The nonlinear projected shell source

$$
F_q
$$

is likewise the physical high-frequency source in the transformed solution.

Therefore the supplier ancestry mechanism is not an artifact of an uncontrolled constant low-frequency background.

Large nonconstant low-mode shear remains possible and is precisely represented by the

$$
LH/HL
$$

ancestry classes.

---

# 18. Why full-state compactness is not automatic

At supplier scale:

$$
v_n(y)
=
\Lambda_n^{-1}
u
\left(
x_n+\Lambda_n^{-1}y,
t_n
\right),
$$

the selected shell has a fixed local lower bound.

However the full global kinetic energy scales as:

$$
\|v_n\|_2^2
=
\Lambda_n
\|u(t_n)\|_2^2,
$$

which need not be uniformly bounded.

Likewise the normalized enstrophy is:

$$
\|S(v_n)\|_2^2
=
\Lambda_n^{-1}
E(t_n),
$$

which has a universal lower bound at the supplier scale but no presently established universal upper bound.

Therefore one must **not** assume full-state local compactness from supplier-shell nonvanishing alone.

This is why DCRP-09 uses Duhamel causality before profile compactness.

Status:

$$
\boxed{
\textbf{COMPACTNESS OVERCLAIM AVOIDED}.
}
$$

---

# 19. Critical-element comparison

Gallagher--Koch--Planchon develop a profile-decomposition / critical-element method in critical Navier--Stokes spaces and show that, under bounded critical-norm hypotheses, minimal blowup data can be extracted.

That framework confirms that scale/translation profile extraction is mathematically viable when a uniform critical-space bound is available.

The present supplier-normalized sequence does **not** yet have such a global uniform critical bound.

Therefore their theorem cannot simply be imported to close the supplier profile.

It serves only as a calibration:

$$
\boxed{
\text{critical atom}
+
\text{uniform critical bound}
\Longrightarrow
\text{profile decomposition machinery is available}.
}
$$

The missing ingredient here is the uniform bound or a defect-completed substitute.

---

# 20. New single frontier — Triadic Parent Extraction Lemma

The former frontier

$$
\text{Supplier Compactness--Causality}
$$

has split asymmetrically:

- causality: established at aggregate Duhamel level;
- compact parent extraction: still open.

The next exact target is:

$$
\boxed{
\textbf{Triadic Parent Extraction Lemma}.
}
$$

A sufficient statement would be:

Let

$$
Q_n\to\infty
$$

be supplier shells approaching a hypothetical singular horizon and let

$$
I_n
$$

be their Duhamel ancestry windows.

Assume:

$$
\mathfrak J_{Q_n}[I_n]
\ge
c\nu.
$$

Then after subsequence extraction, prove at least one of:

1. **near-scale parent reprofile**

   a parent shell with

   $$
   |p_n-Q_n|\le C
   $$

   carries a nonzero critical state/profile after admissible scale/translation normalization;

2. **remote atomic parent**

   there exists

   $$
   p_n-Q_n\to\infty
   $$

   with a fixed positive share of

   $$
   \mathfrak J_{Q_n}^{HH};
   $$

   re-root at

   $$
   p_n
   $$

   and extract a new parent profile;

3. **diffuse parent forcing**

   no parent shell carries fixed share, in which case a completed interaction measure / entropy / defect survives and must be retained by the MORP transition package.

If the minimal obstruction has zero transition / splitting defect, alternative 3 must be excluded.

Then alternatives 1 or 2 produce an actual nonzero parent profile.

This is now a concrete causal-profile extraction problem.

---

# 21. Potential compact interaction measure

For the high--high ancestry define the normalized parent-interaction measure:

$$
\boxed{
\pi_Q^{HH}(p)
=
\frac{
\mathfrak J_{Q,p}^{HH}
}{
\sum_{r\ge Q-2}
\mathfrak J_{Q,r}^{HH}
}
}
\tag{21.1}
$$

whenever the denominator is nonzero.

Then:

$$
\pi_Q^{HH}(p)\ge0,
$$

and:

$$
\sum_{p\ge Q-2}
\pi_Q^{HH}(p)=1.
$$

Shift to relative parent index:

$$
k=p-Q.
$$

This produces a probability measure on:

$$
\{-2,-1,0,1,\ldots\}.
$$

After one-point compactification by:

$$
\infty,
$$

the measures are weak-star compact.

Hence every supplier sequence has a subsequence with:

$$
\boxed{
\pi_{Q_n}^{HH}
\rightharpoonup
\pi_\ast^{HH}
}
\tag{21.2}
$$

on the compact relative-parent space.

Three outcomes are visible in the limit:

- finite relative atom;
- mass at relative infinity;
- diffuse finite-relative distribution.

This probability measure is generated from actual nonlinear Duhamel contribution.

It is proposed as the canonical object for the next parent-extraction proof.

No new MORP cost is declared in this checkpoint.

---

# 22. End state

DCRP-08 proved:

$$
\boxed{
\text{a hypothetical singular mechanism has arbitrarily high critical supplier atoms}.
}
$$

DCRP-09 now proves:

$$
\boxed{
\textbf{
each sufficiently high supplier atom receives a fixed scale-critical nonlinear input
on the same actual Navier--Stokes history.
}
}
$$

Quantitatively:

$$
\boxed{
\mathfrak J_Q[t-\tau_Q,t]
\ge
c\nu,
}
$$

where:

$$
\tau_Q
\sim
\frac{
\log
\left(
C\lambda_Q^{1/2}K_0^{1/2}/\nu
\right)
}{
\nu\lambda_Q^2
}.
$$

Bony decomposition then forces:

$$
\boxed{
\max
\left\{
\mathfrak J_Q^{LH},
\mathfrak J_Q^{HL},
\mathfrak J_Q^{HH}
\right\}
\ge
c\nu.
}
$$

Therefore the causal half of the supplier problem is no longer open.

The remaining single frontier is:

$$
\boxed{
\textbf{
Triadic Parent Extraction Lemma}.
}
$$

The goal is to convert the nonzero actual nonlinear ancestry into:

$$
\boxed{
\text{parent profile}
\quad\text{or}\quad
\text{retained transition / interaction defect}.
}
$$

No broader obstruction taxonomy is required.

---

# Checkpoint v10 Update — DCRP-10

# NS-DCRP-10 — First-Crossing Shell Flux, Signed Triadic Ancestry, and Parent-or-Defect Localization

- date: 2026-08-16
- status: research proof checkpoint
- canonical source: UTF-8 Markdown
- canonical math delimiters: `$...$` and `$$...$$`
- objective: refine DCRP-09 from nonlinear-source ancestry to genuine positive kinetic-energy transfer into the dissipation-boundary supplier shell, and localize the signed triadic ancestry into a parent-or-defect alternative.
- no full Navier--Stokes regularity claim is made.
- principal internal dependencies: MORP-01 through MORP-05, DCRP-08, DCRP-09.
- external primary calibration: Cheskidov--Dai, arXiv:1507.06611v6.

---

# 1. Executive result

DCRP-09 proved that a sufficiently high dissipation-boundary supplier shell must receive a fixed amount of actual same-history nonlinear Duhamel forcing.

That result remains correct, but the source norm

$$
\left\|
\Delta_Q
\mathbb P
\nabla\cdot
(u\otimes u)
\right\|_2
$$

does not distinguish genuine shell-energy transfer from transport / phase deformation.

The present round replaces source-norm ancestry by a signed shell-energy statement.

For a fixed dyadic shell

$$
q,
$$

define

$$
e_q(t)
=
\|u_q(t)\|_2^2
$$

and the signed nonlinear shell transfer

$$
\boxed{
\mathcal T_q(t)
=
-
\left<
\Delta_q
\mathbb P
\nabla\cdot
(u\otimes u),
u_q
\right>.
}
\tag{1.1}
$$

The exact shell-energy identity is

$$
\boxed{
\frac12
\frac d{dt}
e_q(t)
+
\nu
\|\nabla u_q(t)\|_2^2
=
\mathcal T_q(t).
}
\tag{1.2}
$$

Define the critical shell energy

$$
\boxed{
\mathcal K_q(t)
=
\lambda_q
e_q(t)
=
\lambda_q
\|u_q(t)\|_2^2.
}
\tag{1.3}
$$

DCRP-08 gives, at every dissipation-boundary supplier time,

$$
\boxed{
\mathcal K_{Q(t)}(t)
\ge
\kappa_0\nu^2
}
\tag{1.4}
$$

for a universal

$$
\kappa_0>0.
$$

Suppose

$$
T
$$

is a hypothetical first singular time and choose supplier times

$$
t_n\uparrow T,
$$

with

$$
Q_n=Q(t_n)\to\infty.
$$

Because the solution is smooth on every compact subinterval

$$
[0,T-\varepsilon],
$$

the high-shell critical energy satisfies

$$
\sup_{t\le T-\varepsilon}
\mathcal K_{Q_n}(t)
\to0.
$$

Therefore each sufficiently large supplier shell must undergo a genuine first threshold crossing near

$$
T.
$$

Choose the fixed levels

$$
\alpha
=
\frac14
\kappa_0\nu^2,
$$

$$
\beta
=
\frac12
\kappa_0\nu^2.
$$

There exist times

$$
r_n<s_n<t_n,
$$

with

$$
r_n,s_n\uparrow T,
$$

such that

$$
\mathcal K_{Q_n}(r_n)=\alpha,
$$

$$
\mathcal K_{Q_n}(s_n)=\beta,
$$

and

$$
\alpha
<
\mathcal K_{Q_n}(t)
<
\beta
$$

for

$$
r_n<t<s_n.
$$

Integrating (1.2) gives the new lower bound

$$
\boxed{
\lambda_{Q_n}
\int_{r_n}^{s_n}
\mathcal T_{Q_n}(t)\,dt
\ge
\frac18
\kappa_0\nu^2.
}
\tag{1.5}
$$

Hence also

$$
\boxed{
\lambda_{Q_n}
\int_{r_n}^{s_n}
\left(
\mathcal T_{Q_n}(t)
\right)_+
\,dt
\ge
\frac18
\kappa_0\nu^2.
}
\tag{1.6}
$$

This is an actual positive, scale-critical kinetic-energy transfer event occurring arbitrarily close to the hypothetical singular horizon.

Thus the UV supplier does not merely have nonlinear ancestry.

It has a **paid net flux ancestry**.

A signed Bony decomposition yields

$$
\mathcal T_Q
=
\mathcal T_Q^{LH}
+
\mathcal T_Q^{HL}
+
\mathcal T_Q^{HH}.
$$

Therefore at least one of the three integrated signed classes carries a fixed positive critical amount.

The low--high / high--low classes are controlled by a genuine low-frequency shear commutator.

The remote high--high class obeys a new suppression estimate:

$$
\boxed{
\lambda_Q
\int_I
\left|
\mathcal T_Q^{HH,\ge Q+M}
\right|
\,dt
\le
C\nu
2^{-5M/2}
\mathfrak W_{Q,M}[I],
}
\tag{1.7}
$$

on a threshold-crossing interval, where

$$
\boxed{
\mathfrak W_{Q,M}[I]
=
\lambda_Q^{-1}
\int_I
\sum_{p\ge Q+M}
\lambda_p^4
\|u_p(t)\|_2^2
\,dt.
}
\tag{1.8}
$$

The quantity

$$
\mathfrak W_{Q,M}
$$

is scale critical.

Consequently, if a fixed positive portion of the supplier flux is carried by parent scales

$$
p-Q\to\infty,
$$

then

$$
\mathfrak W_{Q,M}
$$

must grow at least exponentially in the relative parent separation.

Thus:

$$
\boxed{
\textbf{
positive supplier flux}
\Longrightarrow
\textbf{
low-mode shear tax}
\ \vee\
\textbf{
bounded-relative parent}
\ \vee\
\textbf{
large derivative occupancy defect}.
}
}
\tag{1.9}
$$

This is the first parent-or-defect reduction using a **signed actual kinetic-energy transfer**, rather than an unsigned source norm.

---

# 2. Refinement of DCRP-09

DCRP-09 defined the critical Duhamel source input

$$
\mathfrak J_Q
=
\lambda_Q^{1/2}
\int
\left\|
\Delta_Q
\mathbb P
\nabla\cdot
(u\otimes u)
\right\|_2
dt.
$$

A lower bound on

$$
\mathfrak J_Q
$$

proves actual same-history nonlinear dependence.

However, a low-frequency velocity can advect a high-frequency packet and make the source norm large without producing comparable net kinetic-energy gain of that shell.

Therefore:

$$
\boxed{
\text{Duhamel source ancestry}
\not\equiv
\text{paid shell-energy ancestry}.
}
\tag{2.1}
$$

DCRP-09 remains a correct causal result.

DCRP-10 strengthens the paid-side statement by working with

$$
\mathcal T_Q.
$$

Status:

$$
\boxed{
\textbf{REFINEMENT, not retraction}.
}
$$

---

# 3. Exact shell-energy equation

Apply the Littlewood--Paley projector

$$
\Delta_q
$$

to

$$
\partial_tu
-
\nu\Delta u
+
\mathbb P\nabla\cdot(u\otimes u)
=
0.
$$

Because

$$
\Delta_q,
\qquad
\mathbb P,
\qquad
\Delta
$$

are Fourier multipliers,

$$
\partial_tu_q
-
\nu\Delta u_q
+
\Delta_q
\mathbb P
\nabla\cdot
(u\otimes u)
=
0.
$$

Pair with

$$
u_q.
$$

Then

$$
\boxed{
\frac12
\frac d{dt}
\|u_q\|_2^2
+
\nu
\|\nabla u_q\|_2^2
=
-
\left<
\Delta_q
\mathbb P
\nabla\cdot
(u\otimes u),
u_q
\right>.
}
\tag{3.1}
$$

Define the right side to be

$$
\mathcal T_q.
$$

Positive

$$
\mathcal T_q
$$

means net nonlinear energy transfer **into** shell

$$
q.
$$

This sign convention is fixed for the remainder of the checkpoint.

---

# 4. Scale-critical shell flux

Define

$$
\boxed{
\Phi_q[I]
=
\lambda_q
\int_I
\mathcal T_q(t)\,dt.
}
\tag{4.1}
$$

and the positive paid amount

$$
\boxed{
\Phi_q^+[I]
=
\lambda_q
\int_I
(\mathcal T_q(t))_+
\,dt.
}
\tag{4.2}
$$

Under a dyadic Navier--Stokes scaling

$$
u_a(x,t)
=
a
u(ax,a^2t),
\qquad
a=2^m,
$$

the corresponding shell index shifts by

$$
m.
$$

Shell energy scales as

$$
\|u_q\|_2^2
\mapsto
a^{-1}
\|u_q\|_2^2.
$$

Hence its time derivative and

$$
\mathcal T_q
$$

scale as

$$
a.
$$

Since

$$
\lambda_q\mapsto a\lambda_q
$$

and

$$
dt\mapsto a^{-2}dt,
$$

$$
\boxed{
\Phi_q
}
$$

is exactly invariant under dyadic parabolic rescaling.

For arbitrary scaling factors it is scale critical up to the bounded overlap constants of the fixed Littlewood--Paley partition.

---

# 5. Uniform high-shell smallness before the singular horizon

Let

$$
T
$$

be a hypothetical first singular time of a strong solution.

Fix

$$
\varepsilon>0.
$$

Since the solution is smooth on

$$
[0,T-\varepsilon],
$$

for any

$$
s>\frac12,
$$

$$
\sup_{0\le t\le T-\varepsilon}
\|u(t)\|_{H^s}
<
\infty.
$$

For every shell

$$
q,
$$

$$
\|u_q(t)\|_2
\le
C
\lambda_q^{-s}
\|u(t)\|_{H^s}.
$$

Therefore

$$
\mathcal K_q(t)
=
\lambda_q
\|u_q(t)\|_2^2
\le
C_\varepsilon
\lambda_q^{1-2s}.
$$

Since

$$
s>\frac12,
$$

$$
\boxed{
\sup_{0\le t\le T-\varepsilon}
\mathcal K_q(t)
\to0
\qquad
(q\to\infty).
}
\tag{5.1}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 6. NEW THEOREM — first-crossing supplier flux

## Theorem 6.1

Assume

$$
T<\infty
$$

is a hypothetical first singular time.

Let

$$
t_n\uparrow T
$$

be dissipation-boundary supplier times with

$$
Q_n=Q(t_n)\to\infty
$$

and

$$
\mathcal K_{Q_n}(t_n)
\ge
\kappa_0\nu^2.
$$

Set

$$
\alpha
=
\frac14
\kappa_0\nu^2,
$$

$$
\beta
=
\frac12
\kappa_0\nu^2.
$$

Then after discarding finitely many terms there exist

$$
r_n<s_n<t_n
$$

such that:

$$
\boxed{
r_n,s_n\to T,
}
\tag{6.1}
$$

$$
\boxed{
\mathcal K_{Q_n}(r_n)=\alpha,
\qquad
\mathcal K_{Q_n}(s_n)=\beta,
}
\tag{6.2}
$$

and

$$
\boxed{
\alpha
<
\mathcal K_{Q_n}(t)
<
\beta
\qquad
(r_n<t<s_n).
}
\tag{6.3}
$$

Moreover:

$$
\boxed{
\Phi_{Q_n}[r_n,s_n]
\ge
\frac18
\kappa_0\nu^2.
}
\tag{6.4}
$$

and hence:

$$
\boxed{
\Phi_{Q_n}^+[r_n,s_n]
\ge
\frac18
\kappa_0\nu^2.
}
\tag{6.5}
$$

### Proof

By (5.1), for every fixed

$$
\varepsilon>0,
$$

and all sufficiently large

$$
n,
$$

$$
\sup_{t\le T-\varepsilon}
\mathcal K_{Q_n}(t)
<
\alpha.
$$

But

$$
\mathcal K_{Q_n}(t_n)
\ge
2\beta.
$$

By continuity in time, the shell must cross the levels

$$
\alpha
$$

and

$$
\beta.
$$

Let

$$
s_n
$$

be the first time before

$$
t_n
$$

at which

$$
\mathcal K_{Q_n}=\beta.
$$

Let

$$
r_n
$$

be the last time before

$$
s_n
$$

at which

$$
\mathcal K_{Q_n}=\alpha.
$$

Then (6.2)--(6.3) hold.

Since for every fixed

$$
\varepsilon>0
$$

the level

$$
\alpha
$$

cannot be reached on

$$
[0,T-\varepsilon]
$$

for sufficiently large

$$
n,
$$

one has

$$
r_n\to T.
$$

Therefore also

$$
s_n\to T.
$$

Integrate the exact shell-energy identity (3.1):

$$
\frac12
\left[
e_{Q_n}(s_n)-e_{Q_n}(r_n)
\right]
+
\nu
\int_{r_n}^{s_n}
\|\nabla u_{Q_n}\|_2^2
dt
=
\int_{r_n}^{s_n}
\mathcal T_{Q_n}(t)
dt.
$$

Multiply by

$$
\lambda_{Q_n}.
$$

The first term is:

$$
\frac12
\left[
\mathcal K_{Q_n}(s_n)
-
\mathcal K_{Q_n}(r_n)
\right]
=
\frac12
(\beta-\alpha).
$$

The viscous term is nonnegative.

Thus:

$$
\Phi_{Q_n}[r_n,s_n]
\ge
\frac12
(\beta-\alpha)
=
\frac18
\kappa_0\nu^2.
$$

Finally:

$$
\int
\mathcal T
\le
\int
\mathcal T_+,
$$

which gives (6.5).

$$
\square
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 7. Meaning of the first-crossing theorem

The lower bound

$$
\Phi_{Q_n}
\ge
c\nu^2
$$

has four useful properties.

1. It is generated by the actual Navier--Stokes state.

2. It is signed: the shell has received **net positive energy**.

3. It is scale critical.

4. The interval on which the payment occurs satisfies

$$
r_n,s_n\to T.
$$

Therefore:

$$
\boxed{
\textbf{
a hypothetical singularity requires arbitrarily high-frequency,
near-horizon, positive critical kinetic-energy transfer events.
}
}
\tag{7.1}
$$

This is stronger for paid-side purposes than the unsigned Duhamel forcing bound of DCRP-09.

---

# 8. Signed Bony decomposition

Write the Bony decomposition of the shell nonlinear term as:

$$
\mathcal T_Q
=
\mathcal T_Q^{LH}
+
\mathcal T_Q^{HL}
+
\mathcal T_Q^{HH}.
$$

The precise finite index ranges depend on the chosen smooth Littlewood--Paley partition, but the structural classes are:

### Low--high

A low-frequency velocity transports / deforms a near-

$$
Q
$$

mode.

### High--low

A near-

$$
Q
$$

mode acts on a lower-frequency velocity.

### High--high

Two comparable high parents interact and output at shell

$$
Q.
$$

Define:

$$
\boxed{
\Phi_Q^{XY}[I]
=
\lambda_Q
\int_I
\mathcal T_Q^{XY}(t)\,dt,
}
\tag{8.1}
$$

for

$$
XY\in\{LH,HL,HH\}.
$$

Then:

$$
\boxed{
\Phi_Q
=
\Phi_Q^{LH}
+
\Phi_Q^{HL}
+
\Phi_Q^{HH}.
}
\tag{8.2}
$$

If:

$$
\Phi_Q\ge c_\ast\nu^2,
$$

then:

$$
\boxed{
\max
\left\{
\Phi_Q^{LH},
\Phi_Q^{HL},
\Phi_Q^{HH}
\right\}
\ge
\frac{
c_\ast
}{
3
}
\nu^2.
}
\tag{8.3}
$$

This is a signed statement.

No absolute-value overcount is used.

---

# 9. Low--high transport cancellation

The low--high energy contribution is not merely bounded by the size of the low velocity.

The divergence-free leading transport cancels.

For a representative term:

$$
\left<
\Delta_Q
(
u_{\le Q-2}\cdot\nabla u_Q
),
u_Q
\right>,
$$

insert:

$$
\Delta_Q
(
u_{\le Q-2}\cdot\nabla u_Q
)
=
u_{\le Q-2}\cdot\nabla\Delta_Qu_Q
+
[
\Delta_Q,
u_{\le Q-2}\cdot\nabla
]u_Q.
$$

The leading term satisfies:

$$
\left<
u_{\le Q-2}\cdot\nabla u_Q,
u_Q
\right>
=
0
$$

because:

$$
\nabla\cdot u_{\le Q-2}=0.
$$

Therefore the actual shell-energy transfer is governed by the commutator / shear:

$$
\boxed{
\left|
\mathcal T_Q^{LH}
\right|
\le
C
\|\nabla u_{\le Q+C}\|_\infty
\sum_{|p-Q|\le C}
\|u_p\|_2^2.
}
\tag{9.1}
$$

The same structural bound holds for the corresponding high--low class after the standard paraproduct rearrangement:

$$
\boxed{
\left|
\mathcal T_Q^{HL}
\right|
\le
C
\|\nabla u_{\le Q+C}\|_\infty
\sum_{|p-Q|\le C}
\|u_p\|_2^2.
}
\tag{9.2}
$$

These are standard Littlewood--Paley commutator consequences of incompressibility.

The important point is:

$$
\boxed{
\text{constant / Galilean low velocity does not pay the shell flux}.
}
$$

Only low-frequency deformation / shear does.

---

# 10. Low--high parent-or-shear dichotomy

Define the near-shell critical cluster:

$$
\boxed{
\mathcal C_Q(t)
=
\lambda_Q
\sum_{|p-Q|\le C}
\|u_p(t)\|_2^2.
}
\tag{10.1}
$$

Equations (9.1)--(9.2) imply:

$$
\boxed{
\lambda_Q
\left|
\mathcal T_Q^{LH}
+
\mathcal T_Q^{HL}
\right|
\le
C
\|\nabla u_{\le Q+C}\|_\infty
\mathcal C_Q(t).
}
\tag{10.2}
$$

Suppose on a first-crossing interval

$$
I=[r,s]
$$

the low--high / high--low class pays:

$$
\boxed{
\Phi_Q^{LH}
+
\Phi_Q^{HL}
\ge
\eta\nu^2.
}
\tag{10.3}
$$

Fix any

$$
M_0>0.
$$

Then one of the following holds.

### Near-scale parent amplification

There exists

$$
t\in I
$$

such that:

$$
\boxed{
\mathcal C_Q(t)
>
M_0\nu^2.
}
\tag{10.4}
$$

This is a nonvanishing, indeed large, near-scale critical state cluster.

### Low-mode shear tax

Otherwise:

$$
\mathcal C_Q(t)
\le
M_0\nu^2
$$

throughout

$$
I.
$$

Then (10.2)--(10.3) yield:

$$
\boxed{
\int_I
\|\nabla u_{\le Q+C}(t)\|_\infty
dt
\ge
\frac{
\eta
}{
CM_0
}.
}
\tag{10.5}
$$

The integral is scale invariant.

Therefore:

$$
\boxed{
\textbf{
positive LH/HL supplier flux}
\Longrightarrow
\textbf{
near-scale critical parent}
\ \vee\
\textbf{
positive low-mode shear debt}.
}
}
\tag{10.6}
$$

Status:

$$
\boxed{
\textbf{PROVED modulo the standard commutator bound (9.1)--(9.2)}.
}
$$

---

# 11. Remote high--high forcing estimate

Consider the high--high contribution from parent shells:

$$
p\ge Q+M.
$$

Write:

$$
F_Q^{HH,\ge Q+M}
=
\sum_{p\ge Q+M}
\Delta_Q
\mathbb P
\nabla\cdot
(
u_p\otimes\widetilde u_p
).
$$

By Bernstein:

$$
\left\|
F_Q^{HH,\ge Q+M}
\right\|_2
\le
C
\lambda_Q
\sum_{p\ge Q+M}
\|u_p\|_\infty
\|\widetilde u_p\|_2.
$$

Again by Bernstein:

$$
\|u_p\|_\infty
\le
C
\lambda_p^{3/2}
\|u_p\|_2.
$$

After absorbing the finite neighbor width in

$$
\widetilde u_p,
$$

$$
\boxed{
\left\|
F_Q^{HH,\ge Q+M}
\right\|_2
\le
C
\lambda_Q
\sum_{p\ge Q+M}
\lambda_p^{3/2}
\|u_p\|_2^2.
}
\tag{11.1}
$$

Since:

$$
\lambda_p^{3/2}
=
\lambda_p^{-5/2}
\lambda_p^4,
$$

and:

$$
\lambda_p^{-5/2}
\le
2^{-5M/2}
\lambda_Q^{-5/2},
$$

one gets:

$$
\boxed{
\left\|
F_Q^{HH,\ge Q+M}
\right\|_2
\le
C
2^{-5M/2}
\lambda_Q^{-3/2}
\mathcal H^{(2)}_{\ge Q+M},
}
\tag{11.2}
$$

where:

$$
\boxed{
\mathcal H^{(2)}_{\ge Q+M}(t)
=
\sum_{p\ge Q+M}
\lambda_p^4
\|u_p(t)\|_2^2.
}
\tag{11.3}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 12. NEW THEOREM — remote-parent $H^2$ occupancy barrier

On a first-crossing interval:

$$
I=[r,s],
$$

one has:

$$
\mathcal K_Q(t)
<
\beta
=
\frac12
\kappa_0\nu^2.
$$

Hence:

$$
\boxed{
\|u_Q(t)\|_2
\le
C_\kappa
\nu
\lambda_Q^{-1/2}.
}
\tag{12.1}
$$

The remote high--high shell transfer satisfies:

$$
\left|
\mathcal T_Q^{HH,\ge Q+M}
\right|
\le
\left\|
F_Q^{HH,\ge Q+M}
\right\|_2
\|u_Q\|_2.
$$

Using (11.2) and (12.1):

$$
\boxed{
\lambda_Q
\left|
\mathcal T_Q^{HH,\ge Q+M}
\right|
\le
C
\nu
2^{-5M/2}
\lambda_Q^{-1}
\mathcal H^{(2)}_{\ge Q+M}(t).
}
\tag{12.2}
$$

Define the scale-critical remote

$$
H^2
$$

occupancy:

$$
\boxed{
\mathfrak W_{Q,M}[I]
=
\lambda_Q^{-1}
\int_I
\mathcal H^{(2)}_{\ge Q+M}(t)
\,dt.
}
\tag{12.3}
$$

Then:

$$
\boxed{
\lambda_Q
\int_I
\left|
\mathcal T_Q^{HH,\ge Q+M}
\right|
dt
\le
C
\nu
2^{-5M/2}
\mathfrak W_{Q,M}[I].
}
\tag{12.4}
$$

Therefore if:

$$
\boxed{
\lambda_Q
\int_I
\mathcal T_Q^{HH,\ge Q+M}
dt
\ge
\eta\nu^2
}
\tag{12.5}
$$

for some

$$
\eta>0,
$$

then necessarily:

$$
\boxed{
\mathfrak W_{Q,M}[I]
\ge
c
\eta
\nu
2^{5M/2}.
}
\tag{12.6}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 13. Scale criticality of the remote occupancy

The homogeneous velocity

$$
\dot H^2
$$

square scales as:

$$
\|u\|_{\dot H^2}^2
\mapsto
a^3
\|u\|_{\dot H^2}^2.
$$

Also:

$$
dt\mapsto a^{-2}dt,
$$

and:

$$
\lambda_Q^{-1}
\mapsto
a^{-1}
\lambda_Q^{-1}.
$$

Therefore:

$$
\boxed{
\lambda_Q^{-1}
\int
\|u\|_{\dot H^2}^2
dt
}
\tag{13.1}
$$

is parabolic-scale invariant.

Hence:

$$
\boxed{
\mathfrak W_{Q,M}
}
$$

is a genuine scale-critical derivative occupancy coordinate.

Remote parent escape cannot be dismissed as a raw supercritical artifact.

---

# 14. Corollary — bounded occupancy localizes high--high parents

Suppose a family of first-crossing intervals satisfies:

$$
\boxed{
\sup_n
\mathfrak W_{Q_n,0}[I_n]
\le
W_\ast
<
\infty.
}
\tag{14.1}
$$

Suppose also that:

$$
\Phi_{Q_n}^{HH}[I_n]
\ge
\eta\nu^2.
$$

Choose

$$
M_\ast
$$

large enough that:

$$
C
\nu
2^{-5M_\ast/2}
W_\ast
<
\frac12
\eta\nu^2.
$$

Then the remote parents:

$$
p\ge Q_n+M_\ast
$$

cannot contribute more than half the required positive

$$
HH
$$

flux.

Therefore:

$$
\boxed{
\lambda_{Q_n}
\int_{I_n}
\mathcal T_{Q_n}^{HH,\,
Q_n-2\le p<Q_n+M_\ast}
dt
\ge
\frac12
\eta\nu^2.
}
\tag{14.2}
$$

Since there are only finitely many relative parent indices in this range, at least one bounded-relative parent class carries a fixed positive signed transfer share.

Thus:

$$
\boxed{
\textbf{
bounded scale-normalized }H^2\textbf{ occupancy}
\Longrightarrow
\textbf{
bounded-relative HH ancestry}.
}
}
\tag{14.3}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 15. Remote parent escape forces a derivative defect

Suppose instead that for every fixed

$$
M,
$$

the positive

$$
HH
$$

flux increasingly originates from:

$$
p-Q\ge M.
$$

Then for a sequence

$$
M_n\to\infty,
$$

one has:

$$
\lambda_{Q_n}
\int_{I_n}
\mathcal T_{Q_n}^{HH,\ge Q_n+M_n}
dt
\ge
\eta\nu^2.
$$

Theorem 12.1 gives:

$$
\boxed{
\mathfrak W_{Q_n,M_n}[I_n]
\ge
c
\eta\nu
2^{5M_n/2}
\to\infty.
}
\tag{15.1}
$$

Thus:

$$
\boxed{
\textbf{
unbounded relative HH ancestry}
\Longrightarrow
\textbf{
divergent scale-critical }H^2\textbf{ occupancy}.
}
}
\tag{15.2}
$$

This is a concrete derivative noncompactness defect.

It is substantially stronger than the purely probabilistic statement that parent mass escapes to relative infinity.

---

# 16. Normalized crossing duration

Define the normalized duration of a first-crossing interval:

$$
\boxed{
L_Q[I]
=
\nu
\lambda_Q^2
|I|.
}
\tag{16.1}
$$

This is scale invariant.

There are two possibilities.

### Bounded-duration branch

$$
\sup_n
L_{Q_n}[I_n]
<
\infty.
$$

Then any bounded-relative parent interaction that pays a fixed amount over the interval must achieve nontrivial critical amplitude at some actual time.

### Long-germ branch

$$
L_{Q_n}[I_n]
\to\infty.
$$

But by construction:

$$
\alpha
<
\mathcal K_{Q_n}(t)
<
\beta
$$

throughout the entire crossing interval.

After re-scaling to shell

$$
Q_n,
$$

the supplier shell therefore remains nonvanishing for a normalized time interval whose length tends to infinity.

Thus:

$$
\boxed{
\textbf{
long normalized crossing duration}
\Longrightarrow
\textbf{
an arbitrarily long nonvanishing supplier germ}.
}
}
\tag{16.2}
$$

This does not automatically give a full ancient Navier--Stokes profile because full-state local compactness is still required.

But temporal disappearance is no longer possible.

---

# 17. Bounded-duration bounded-relative parent atom

Assume:

$$
L_Q[I]
\le
L_\ast,
$$

and a fixed bounded-relative high--high parent index

$$
p
$$

with:

$$
|p-Q|\le M_\ast
$$

satisfies:

$$
\boxed{
\lambda_Q
\int_I
\mathcal T_{Q,p}^{HH}(t)
dt
\ge
\eta\nu^2.
}
\tag{17.1}
$$

A standard Bernstein estimate gives:

$$
\left|
\mathcal T_{Q,p}^{HH}
\right|
\le
C
\lambda_Q
\lambda_p^{3/2}
B_p(t)^2
\|u_Q(t)\|_2,
$$

where:

$$
B_p(t)^2
=
\sum_{|r-p|\le1}
\|u_r(t)\|_2^2.
$$

On the crossing interval:

$$
\|u_Q\|_2
\le
C\nu\lambda_Q^{-1/2}.
$$

Since:

$$
|p-Q|\le M_\ast,
$$

$$
\lambda_p
\asymp_{M_\ast}
\lambda_Q.
$$

Therefore:

$$
\lambda_Q
\left|
\mathcal T_{Q,p}^{HH}
\right|
\le
C(M_\ast)
\nu
\lambda_Q^3
B_p(t)^2.
$$

Integrating and using (17.1):

$$
\int_I
B_p(t)^2dt
\ge
c(M_\ast)
\eta
\nu
\lambda_Q^{-3}.
$$

But:

$$
|I|
\le
\frac{
L_\ast
}{
\nu\lambda_Q^2
}.
$$

Hence for some:

$$
t_\ast\in I,
$$

$$
B_p(t_\ast)^2
\ge
c(M_\ast)
\frac{
\eta\nu^2
}{
L_\ast
}
\lambda_Q^{-1}.
$$

Since the cluster contains finitely many shells, some:

$$
r
$$

with:

$$
|r-p|\le1
$$

satisfies:

$$
\boxed{
\lambda_r
\|u_r(t_\ast)\|_2^2
\ge
c(M_\ast,L_\ast)
\eta\nu^2.
}
\tag{17.2}
$$

Thus:

$$
\boxed{
\textbf{
bounded duration}
+
\textbf{
bounded-relative positive HH flux}
\Longrightarrow
\textbf{
a genuine critical parent shell atom}.
}
}
\tag{17.3}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 18. Combined parent-or-defect theorem

The previous sections can be assembled into the following structural result.

## Theorem 18.1

Let:

$$
I_n=[r_n,s_n]
$$

be the first-crossing intervals of Theorem 6.1.

Then after subsequence extraction, at least one of the following occurs.

### A. Positive low-mode shear debt

$$
\boxed{
\int_{I_n}
\|\nabla u_{\le Q_n+C}\|_\infty
dt
\ge
c>0.
}
\tag{18.1}
$$

### B. Near-scale critical cluster

There are times:

$$
t_n^\ast\in I_n
$$

with:

$$
\boxed{
\lambda_{Q_n}
\sum_{|p-Q_n|\le C}
\|u_p(t_n^\ast)\|_2^2
\ge
c\nu^2.
}
\tag{18.2}
$$

### C. Critical bounded-relative HH parent atom

There exist:

$$
p_n-Q_n=O(1)
$$

and:

$$
t_n^\ast\in I_n
$$

such that:

$$
\boxed{
\lambda_{p_n}
\|u_{p_n}(t_n^\ast)\|_2^2
\ge
c\nu^2.
}
\tag{18.3}
$$

### D. Divergent derivative occupancy defect

For some:

$$
M_n\to\infty,
$$

$$
\boxed{
\mathfrak W_{Q_n,M_n}[I_n]
\to\infty.
}
\tag{18.4}
$$

### E. Long normalized supplier germ

$$
\boxed{
\nu
\lambda_{Q_n}^2
|I_n|
\to\infty,
}
\tag{18.5}
$$

while:

$$
\boxed{
\alpha
<
\lambda_{Q_n}
\|u_{Q_n}(t)\|_2^2
<
\beta
}
\tag{18.6}
$$

throughout:

$$
I_n.
$$

### Proof status

The theorem is obtained by:

1. the first-crossing positive flux theorem;
2. the signed

$$
LH/HL/HH
$$

decomposition;
3. the low--high commutator dichotomy;
4. the remote

$$
HH
$$

occupancy barrier;
5. the bounded-duration bounded-relative parent estimate.

Status:

$$
\boxed{
\textbf{PROVED as a structural alternative under the standard LP/Bony estimates stated above}.
}
$$

---

# 19. What this means for MORP

MORP zero-cost minimality requires simultaneous saturation of:

$$
\mathsf O_{\rm PFET}=0,
$$

$$
\mathsf{Paid}=0,
$$

and:

$$
\mathsf R_{\rm nat}=0,
$$

together with the remaining mechanism kernels.

Theorem 6.1 now supplies an unavoidable actual near-horizon kinetic-energy transfer:

$$
\boxed{
\Phi_{Q_n}
\ge
c\nu^2.
}
\tag{19.1}
$$

This quantity is not a dangerous certificate.

It is a direct signed energy balance of the actual Navier--Stokes shell.

Therefore the remaining compatibility question is extremely concrete:

$$
\boxed{
\textbf{
does the existing PFET / paid / native-residual compiler retain
a positive scale-critical shell-energy transfer event?
}
}
\tag{19.2}
$$

One must not answer this by definition.

It has to be proved from the actual PFET observable / finite-window compiler.

If yes, the zero-cost minimal recurrent obstruction is immediately incompatible with Theorem 6.1.

If no, the exact visibility gap is now identified:

$$
\boxed{
\text{spectral shell transfer}
\longrightarrow
\text{PFET / paid visibility}.
}
$$

---

# 20. Why this is stronger than "there is a parent"

The parent-extraction approach alone risks an infinite regress:

$$
\text{supplier}
\leftarrow
\text{parent}
\leftarrow
\text{parent of parent}
\leftarrow
\cdots
$$

The first-crossing theorem changes the target.

Regardless of which individual parent pays, the shell itself must receive:

$$
\boxed{
\text{fixed positive net critical energy transfer}.
}
$$

So the closure problem can potentially terminate at the **flux event itself**, without identifying a unique parent profile.

Parent localization remains useful only if the existing paid ledger fails to see the flux directly.

This is a major proof-routing simplification.

---

# 21. External source calibration

Cheskidov--Dai's Littlewood--Paley argument explicitly uses:

- Bony paraproduct;
- commutator estimates;
- dissipation-wavenumber splitting;
- absorption of high-frequency nonlinear terms by viscosity;
- low-mode activity:

$$
f(t)
=
\sum_{q\le Q(t)}
\lambda_q
\|u_q(t)\|_\infty.
$$

Their Lemma 3.2 states for the pure velocity flux:

$$
|I|
\lesssim
c_r\nu
\sum_{q>Q-3}
\lambda_q^{2s+2}
\|u_q\|_2^2
+
f(t)
\sum_q
\lambda_q^{2s}
\|u_q\|_2^2
$$

for every:

$$
s>0
$$

and:

$$
r\ge2.
$$

This external result supports the low--high shear / high-frequency absorption geometry used in the present checkpoint.

DCRP-10's first-crossing flux theorem itself follows directly from the exact shell energy identity and does not depend on Cheskidov--Dai's theorem.

No novelty / priority claim is made for standard Littlewood--Paley commutator estimates.

---

# 22. End state

DCRP-09 established:

$$
\boxed{
\text{critical supplier atom}
\Longrightarrow
\text{actual same-history nonlinear source ancestry}.
}
$$

DCRP-10 strengthens this to:

$$
\boxed{
\textbf{
hypothetical singularity}
\Longrightarrow
\textbf{
arbitrarily high near-horizon positive scale-critical shell-energy transfer events}.
}
$$

Quantitatively:

$$
\boxed{
\lambda_{Q_n}
\int_{r_n}^{s_n}
\mathcal T_{Q_n}(t)
dt
\ge
c\nu^2.
}
$$

The signed triadic analysis further yields:

$$
\boxed{
\text{positive low-mode shear debt}
\vee
\text{critical parent atom}
\vee
\text{divergent derivative occupancy}
\vee
\text{long supplier germ}.
}
$$

The next proof target is no longer generic parent extraction.

It is:

$$
\boxed{
\textbf{
Spectral-Flux / PFET Compatibility Lemma}.
}
$$

Desired statement:

> Every first-crossing shell event satisfying
>
> $$
> \lambda_Q
> \int_I
> \mathcal T_Q\,dt
> \ge
> c\nu^2
> $$
>
> must produce either:
>
> $$
> \mathsf O_{\rm PFET}>0,
> $$
>
> $$
> \mathsf{Paid}>0,
> $$
>
> or:
>
> $$
> \mathsf R_{\rm nat}>0.
> $$

If this compatibility lemma is established for the existing MORP compiler, the zero-cost minimal obstruction cannot contain the supplier mechanism.

That is now the single closure-facing frontier.

---

# Checkpoint v11 Update — DCRP-11

# NS-DCRP-11 — Heat-Band PFET Compatibility, Forward/Backscatter Alternative, and the Final Localization Gap

- date: 2026-08-16
- status: research proof checkpoint
- canonical source: UTF-8 Markdown
- canonical math delimiters: `$...$` and `$$...$$`
- objective: bridge the positive first-crossing spectral shell flux from DCRP-10 to the already existing FCBP pressure--flux / paid-backscatter architecture without inventing a new physical detector.
- no full Navier--Stokes regularity claim is made.
- principal internal dependencies:
  - FCBP-03 signed pressure--flux telescope;
  - FCBP-04 heat-semigroup coarse graining and co-moving heat pressure--flux ledger;
  - FCBP-05 combined pressure/flux/energy/trace observability;
  - FCBP-06 paid-side and combined-invisible audit;
  - MORP-01 through MORP-05;
  - DCRP-08 through DCRP-10.
- external primary calibration:
  - Runlong Yu, arXiv:2606.25322v1;
  - Cheskidov--Dai, arXiv:1507.06611v6.

---

# 1. Executive result

DCRP-10 proved that a hypothetical finite-time singularity forces arbitrarily high dyadic first-crossing events with

$$
\boxed{
\lambda_{Q_n}
\int_{r_n}^{s_n}
\mathcal T_{Q_n}(t)\,dt
\ge
c\nu^2.
}
\tag{1.1}
$$

This is a positive, scale-critical, signed kinetic-energy transfer into a Littlewood--Paley supplier shell.

The remaining question was whether this transfer must be visible to the already existing pressure--flux / paid-side ledgers.

A direct comparison between a Littlewood--Paley shell flux and the compact-mollifier PFET observable is unnecessarily difficult and filter-dependent.

The present round bypasses that mismatch.

Use instead the heat-semigroup coarse graining already constructed internally in FCBP-04:

$$
S_s
=
e^{s\Delta}.
$$

For fixed constants

$$
0<a<b,
$$

and a frequency

$$
\lambda>0,
$$

define the two comparable smoothing parameters

$$
s_a
=
a\lambda^{-2},
$$

$$
s_b
=
b\lambda^{-2}.
$$

Define the scale-critical heat-band energy

$$
\boxed{
\mathcal B_{\lambda}^{a,b}(t)
=
\frac{\lambda}{2}
\left(
\|e^{s_a\Delta}u(t)\|_2^2
-
\|e^{s_b\Delta}u(t)\|_2^2
\right).
}
\tag{1.2}
$$

Because

$$
b>a,
$$

the Fourier multiplier

$$
e^{-2a|\xi|^2/\lambda^2}
-
e^{-2b|\xi|^2/\lambda^2}
$$

is nonnegative.

If the Littlewood--Paley supplier shell at frequency

$$
\lambda_Q
$$

satisfies

$$
\lambda_Q
\|u_Q\|_2^2
\ge
\kappa_0\nu^2,
$$

then:

$$
\boxed{
\mathcal B_{\lambda_Q}^{a,b}
\ge
\kappa_{HB}\nu^2
}
\tag{1.3}
$$

for a universal

$$
\kappa_{HB}>0
$$

depending only on the fixed LP annulus and the fixed pair

$$
a<b.
$$

On every compact regular time interval before a first singular time,

$$
\mathcal B_{\lambda}^{a,b}(t)
\to0
$$

uniformly as

$$
\lambda\to\infty.
$$

Hence the heat-band energy itself has arbitrarily high first-crossing intervals approaching the singular horizon.

For a fixed heat filter

$$
S_s,
$$

let

$$
U^s
=
S_su,
$$

$$
R^s
=
S_s(u\otimes u)
-
U^s\otimes U^s,
$$

and

$$
\Pi^s
=
-
R^s:\nabla U^s.
$$

Define the whole-space resolved interscale work

$$
\boxed{
F_s(t)
=
\int_{\mathbb R^3}
\Pi^s(x,t)\,dx.
}
\tag{1.4}
$$

The exact whole-space heat-filter energy identity is

$$
\boxed{
\frac d{dt}
\frac12
\|U^s\|_2^2
+
\nu
\|\nabla U^s\|_2^2
+
F_s
=
0.
}
\tag{1.5}
$$

Subtracting the two heat-filter identities produces an exact heat-band balance.

If

$$
\mathcal B_{\lambda}^{a,b}
$$

rises by

$$
\delta\nu^2
$$

on an interval

$$
I,
$$

then:

$$
\boxed{
\lambda
\int_I
\left(
F_{s_b}
-
F_{s_a}
\right)
dt
\ge
\delta\nu^2.
}
\tag{1.6}
$$

Therefore:

$$
\boxed{
\lambda
\int_I
(F_{s_b})_+
dt
+
\lambda
\int_I
(F_{s_a})_-
dt
\ge
\delta\nu^2.
}
\tag{1.7}
$$

Hence at least one of:

$$
\boxed{
\lambda
\int_I
(F_{s_b})_+
dt
\ge
\frac{\delta}{2}\nu^2
}
\tag{1.8}
$$

or:

$$
\boxed{
\lambda
\int_I
(F_{s_a})_-
dt
\ge
\frac{\delta}{2}\nu^2
}
\tag{1.9}
$$

must occur.

Interpretation:

- the coarser heat filter sees fixed positive **forward interscale work**;
- or the finer heat filter sees fixed positive **backscatter payment**.

These are precisely the two signs already present in the FCBP pressure--flux / paid-side architecture.

Thus:

$$
\boxed{
\textbf{
supplier first crossing}
\Longrightarrow
\textbf{
heat-PFET forward work}
\ \vee\
\textbf{
heat-Paid backscatter}.
}
}
\tag{1.10}
$$

No new physical mechanism is introduced.

The only remaining compatibility gap is spatial / window localization:

> the theorem above is a whole-space heat-filter work statement, whereas the MORP/finite-window PFET kernel is a local normalized package.

Thus the next target is now a single precise lemma:

$$
\boxed{
\textbf{Heat-Flux Localization / Package-Completion Lemma}.
}
$$

---

# 2. Internal PFET architecture audited

MORP-01 defines

$$
\mathsf O_{\rm PFET}(D)
$$

as combined pressure--flux--energy--trace visibility,

$$
\mathsf{Paid}(D)
$$

as normalized paid-side leakage/backscatter tax,

and:

$$
\mathsf R_{\rm nat}(D)
$$

as a retained native residual not already included in the previous channels.

The zero-cost minimal obstruction satisfies:

$$
\mathsf O_{\rm PFET}(D_\ast)=0,
$$

$$
\mathsf{Paid}(D_\ast)=0,
$$

and:

$$
\mathsf R_{\rm nat}(D_\ast)=0.
$$

FCBP-03 defines the signed coarse work distribution

$$
G^\ell
=
\Pi^\ell
+
\nabla\cdot(P^\ell U^\ell),
$$

with

$$
\Pi^\ell
=
-
R^\ell:\nabla U^\ell.
$$

Its signed telescope explicitly places negative work / backscatter on the paid side.

FCBP-04 separately develops heat-semigroup coarse graining:

$$
S_s=e^{s\Delta},
$$

and proves the corresponding exact coarse Navier--Stokes equation and heat pressure--flux ledger.

Therefore heat-filter interscale work is not an ad hoc DCRP observable.

It already belongs to the internal FCBP coarse-work architecture.

---

# 3. External PFET calibration

The external coarse-grained pressure--flux work theorem uses a nonnegative compactly supported smooth spatial mollifier.

For a spatial filter length

$$
\ell,
$$

it defines:

$$
U^\ell=S_\ell u,
$$

$$
P^\ell=S_\ell p,
$$

$$
R^\ell
=
S_\ell(u\otimes u)
-
U^\ell\otimes U^\ell,
$$

$$
\boxed{
\Pi^\ell
=
-
R^\ell:\nabla U^\ell,
}
\tag{3.1}
$$

and:

$$
\boxed{
G^\ell
=
\Pi^\ell
+
\nabla\cdot(P^\ell U^\ell).
}
\tag{3.2}
$$

Its localized normalized work is:

$$
\boxed{
\mathcal W_{I,r}[\phi]
=
r^{-1}
\int_I
\int
\left(
\phi\Pi^\ell
-
P^\ell U^\ell\cdot\nabla\phi
\right)
dxdt.
}
\tag{3.3}
$$

The external theorem proves an exact finite-chain energy/work telescope once a chosen local coarse-work signal is present.

It explicitly leaves the general coarse-observability implication open.

Thus the DCRP-11 result should not be described as a theorem that the external compact-mollifier active detector automatically sees the supplier event.

The current exact bridge is to the internal **heat-filter** pressure--flux / backscatter ledger.

---

# 4. Heat-band energy

Fix:

$$
0<a<b.
$$

Let:

$$
\lambda>0.
$$

Define:

$$
s_a
=
a\lambda^{-2},
$$

$$
s_b
=
b\lambda^{-2}.
$$

Set:

$$
U_a
=
e^{s_a\Delta}u,
$$

$$
U_b
=
e^{s_b\Delta}u.
$$

Define:

$$
\boxed{
\mathcal B_\lambda^{a,b}(t)
=
\frac{\lambda}{2}
\left(
\|U_a(t)\|_2^2
-
\|U_b(t)\|_2^2
\right).
}
\tag{4.1}
$$

By Plancherel:

$$
\mathcal B_\lambda^{a,b}
=
\frac{\lambda}{2}
\int_{\mathbb R^3}
m_{a,b}
\left(
\frac{
|\xi|
}{
\lambda
}
\right)
|\widehat u(\xi)|^2
d\xi,
$$

where:

$$
\boxed{
m_{a,b}(\rho)
=
e^{-2a\rho^2}
-
e^{-2b\rho^2}.
}
\tag{4.2}
$$

For:

$$
\rho>0,
$$

$$
m_{a,b}(\rho)>0.
$$

Thus:

$$
\boxed{
\mathcal B_\lambda^{a,b}\ge0.
}
\tag{4.3}
$$

---

# 5. Scale invariance

Under the Navier--Stokes scaling:

$$
u_c(x,t)
=
c
u(cx,c^2t),
$$

the frequency parameter transforms as:

$$
\lambda\mapsto c\lambda.
$$

The filtered

$$
L^2
$$

energy scales as:

$$
\|U\|_2^2
\mapsto
c^{-1}
\|U\|_2^2.
$$

Hence:

$$
(c\lambda)
\left(
c^{-1}
\|U\|_2^2
\right)
=
\lambda
\|U\|_2^2.
$$

Therefore:

$$
\boxed{
\mathcal B_\lambda^{a,b}
}
$$

is parabolic-scale invariant when the heat parameters are kept at fixed relative values:

$$
s_a=a\lambda^{-2},
\qquad
s_b=b\lambda^{-2}.
$$

---

# 6. NEW THEOREM — supplier shell forces nonzero heat-band energy

Let the Littlewood--Paley shell multiplier defining

$$
u_Q
$$

be supported in the fixed annulus:

$$
c_-\lambda_Q
\le
|\xi|
\le
c_+\lambda_Q,
$$

with:

$$
0<c_-<c_+<\infty.
$$

Let:

$$
|\varphi_Q(\xi)|\le1.
$$

Define:

$$
\boxed{
d_{a,b}
=
\min_{
c_-\le\rho\le c_+
}
m_{a,b}(\rho).
}
\tag{6.1}
$$

Because:

$$
m_{a,b}>0
$$

on:

$$
(0,\infty),
$$

$$
\boxed{
d_{a,b}>0.
}
\tag{6.2}
$$

## Theorem 6.1

If:

$$
\lambda_Q
\|u_Q(t)\|_2^2
\ge
\kappa_0\nu^2,
$$

then:

$$
\boxed{
\mathcal B_{\lambda_Q}^{a,b}(t)
\ge
\frac{
d_{a,b}\kappa_0
}{
2
}
\nu^2.
}
\tag{6.3}
$$

### Proof

On the support of:

$$
\varphi_Q,
$$

$$
m_{a,b}
\left(
\frac{|\xi|}{\lambda_Q}
\right)
\ge
d_{a,b}.
$$

Hence:

$$
\begin{aligned}
\mathcal B_{\lambda_Q}^{a,b}
&=
\frac{\lambda_Q}{2}
\int
m_{a,b}
\left(
\frac{|\xi|}{\lambda_Q}
\right)
|\widehat u|^2d\xi\\
&\ge
\frac{
d_{a,b}\lambda_Q
}{
2
}
\int_{\operatorname{supp}\varphi_Q}
|\widehat u|^2d\xi.
\end{aligned}
$$

Since:

$$
|\varphi_Q|\le1,
$$

$$
\int_{\operatorname{supp}\varphi_Q}
|\widehat u|^2
\ge
\int
|\varphi_Q\widehat u|^2
=
\|u_Q\|_2^2.
$$

Therefore:

$$
\mathcal B_{\lambda_Q}^{a,b}
\ge
\frac{
d_{a,b}
}{
2
}
\lambda_Q
\|u_Q\|_2^2.
$$

Apply the supplier lower bound.

$$
\square
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 7. High heat-band energy is absent on every regular compact time interval

The multiplier difference satisfies:

$$
0
\le
e^{-2ax}
-
e^{-2bx}
\le
2(b-a)x
$$

for:

$$
x\ge0.
$$

Therefore:

$$
m_{a,b}
\left(
\frac{|\xi|}{\lambda}
\right)
\le
2(b-a)
\frac{
|\xi|^2
}{
\lambda^2
}.
$$

Hence:

$$
\boxed{
\mathcal B_{\lambda}^{a,b}(t)
\le
(b-a)
\lambda^{-1}
\|\nabla u(t)\|_2^2.
}
\tag{7.1}
$$

If:

$$
T
$$

is a hypothetical first singular time, then for every:

$$
\varepsilon>0,
$$

the strong solution satisfies:

$$
\sup_{
0\le t\le T-\varepsilon
}
\|\nabla u(t)\|_2
<
\infty.
$$

Thus:

$$
\boxed{
\sup_{
0\le t\le T-\varepsilon
}
\mathcal B_{\lambda}^{a,b}(t)
\to0
\qquad
(\lambda\to\infty).
}
\tag{7.2}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 8. NEW THEOREM — heat-band first crossing

Let:

$$
t_n\uparrow T
$$

be the supplier times from DCRP-08 / DCRP-10, with:

$$
\lambda_n
=
\lambda_{Q_n}
\to\infty.
$$

By Theorem 6.1:

$$
\mathcal B_{\lambda_n}^{a,b}(t_n)
\ge
\kappa_{HB}\nu^2,
$$

where:

$$
\boxed{
\kappa_{HB}
=
\frac{
d_{a,b}\kappa_0
}{
2
}.
}
\tag{8.1}
$$

Choose:

$$
\alpha_{HB}
=
\frac14
\kappa_{HB}\nu^2,
$$

$$
\beta_{HB}
=
\frac12
\kappa_{HB}\nu^2.
$$

Then for all sufficiently large:

$$
n,
$$

there exist:

$$
\rho_n<\sigma_n<t_n
$$

such that:

$$
\boxed{
\rho_n,\sigma_n\to T,
}
\tag{8.2}
$$

$$
\boxed{
\mathcal B_{\lambda_n}^{a,b}(\rho_n)
=
\alpha_{HB},
}
\tag{8.3}
$$

$$
\boxed{
\mathcal B_{\lambda_n}^{a,b}(\sigma_n)
=
\beta_{HB},
}
\tag{8.4}
$$

and:

$$
\alpha_{HB}
<
\mathcal B_{\lambda_n}^{a,b}(t)
<
\beta_{HB}
$$

for:

$$
\rho_n<t<\sigma_n.
$$

### Proof

The proof is identical in structure to DCRP-10's shell first-crossing theorem.

Theorem 7.1 prevents level:

$$
\alpha_{HB}
$$

from being reached on any fixed compact subinterval before:

$$
T
$$

once:

$$
\lambda_n
$$

is sufficiently large.

The supplier lower bound places the endpoint above:

$$
2\beta_{HB}.
$$

Continuity gives the two crossing times.

$$
\square
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 9. Whole-space heat-filter energy identity

For fixed:

$$
s>0,
$$

define:

$$
U^s
=
e^{s\Delta}u,
$$

$$
P^s
=
e^{s\Delta}p,
$$

and:

$$
R^s
=
e^{s\Delta}(u\otimes u)
-
U^s\otimes U^s.
$$

The heat-filtered velocity satisfies:

$$
\partial_tU^s
-
\nu\Delta U^s
+
\nabla\cdot(U^s\otimes U^s)
+
\nabla P^s
=
-\nabla\cdot R^s.
$$

Define:

$$
\boxed{
\Pi^s
=
-
R^s:\nabla U^s.
}
\tag{9.1}
$$

For a smooth finite-energy whole-space solution, pair with:

$$
U^s
$$

and integrate over:

$$
\mathbb R^3.
$$

The resolved advection term vanishes by incompressibility.

The pressure term integrates to zero.

The Reynolds-stress term gives:

$$
\int
U^s\cdot
(-\nabla\cdot R^s)
dx
=
\int
R^s:\nabla U^s
dx
=
-
\int
\Pi^s dx.
$$

Therefore:

$$
\boxed{
\frac d{dt}
\frac12
\|U^s\|_2^2
+
\nu
\|\nabla U^s\|_2^2
+
F_s(t)
=
0,
}
\tag{9.2}
$$

where:

$$
\boxed{
F_s(t)
=
\int_{\mathbb R^3}
\Pi^s(x,t)\,dx.
}
\tag{9.3}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 10. Heat-band balance

For a fixed frequency:

$$
\lambda,
$$

set:

$$
s_a=a\lambda^{-2},
$$

$$
s_b=b\lambda^{-2}.
$$

Define:

$$
E_a(t)
=
\frac12
\|U^{s_a}(t)\|_2^2,
$$

$$
E_b(t)
=
\frac12
\|U^{s_b}(t)\|_2^2.
$$

Define:

$$
D_a(t)
=
\|\nabla U^{s_a}(t)\|_2^2,
$$

$$
D_b(t)
=
\|\nabla U^{s_b}(t)\|_2^2.
$$

Equation (9.2) gives:

$$
E_a'
+
\nu D_a
+
F_{s_a}
=
0,
$$

$$
E_b'
+
\nu D_b
+
F_{s_b}
=
0.
$$

Subtract:

$$
(E_a-E_b)'
+
\nu
(D_a-D_b)
+
F_{s_a}
-
F_{s_b}
=
0.
$$

Multiply by:

$$
\lambda:
$$

$$
\boxed{
\frac d{dt}
\mathcal B_\lambda^{a,b}
+
\nu\lambda
(D_a-D_b)
+
\lambda
(
F_{s_a}-F_{s_b}
)
=
0.
}
\tag{10.1}
$$

Because:

$$
s_a<s_b,
$$

the finer-filter dissipation is larger:

$$
\boxed{
D_a-D_b
\ge0.
}
\tag{10.2}
$$

This follows directly from the Fourier multipliers:

$$
|\xi|^2
e^{-2a|\xi|^2/\lambda^2}
\ge
|\xi|^2
e^{-2b|\xi|^2/\lambda^2}.
$$

---

# 11. NEW THEOREM — Heat-Band PFET / Paid Alternative

## Theorem 11.1

Suppose on an interval:

$$
I=[\rho,\sigma]
$$

the heat-band energy satisfies:

$$
\mathcal B_\lambda^{a,b}(\sigma)
-
\mathcal B_\lambda^{a,b}(\rho)
=
\delta\nu^2,
$$

with:

$$
\delta>0.
$$

Then:

$$
\boxed{
\lambda
\int_I
\left(
F_{s_b}
-
F_{s_a}
\right)
dt
\ge
\delta\nu^2.
}
\tag{11.1}
$$

Consequently:

$$
\boxed{
\lambda
\int_I
(F_{s_b})_+
dt
+
\lambda
\int_I
(F_{s_a})_-
dt
\ge
\delta\nu^2.
}
\tag{11.2}
$$

Hence at least one of:

$$
\boxed{
\lambda
\int_I
(F_{s_b})_+
dt
\ge
\frac{\delta}{2}\nu^2
}
\tag{11.3}
$$

or:

$$
\boxed{
\lambda
\int_I
(F_{s_a})_-
dt
\ge
\frac{\delta}{2}\nu^2
}
\tag{11.4}
$$

holds.

### Proof

Integrate (10.1):

$$
\delta\nu^2
+
\nu\lambda
\int_I
(D_a-D_b)
dt
+
\lambda
\int_I
(F_{s_a}-F_{s_b})
dt
=
0.
$$

Therefore:

$$
\lambda
\int_I
(F_{s_b}-F_{s_a})
dt
=
\delta\nu^2
+
\nu\lambda
\int_I
(D_a-D_b)
dt.
$$

By (10.2), the final term is nonnegative.

Thus (11.1) follows.

Next:

$$
F_{s_b}-F_{s_a}
\le
(F_{s_b})_+
+
(F_{s_a})_-.
$$

Integrate and multiply by:

$$
\lambda.
$$

This proves (11.2).

If both terms in (11.2) were less than:

$$
\frac{\delta}{2}\nu^2,
$$

their sum would be less than:

$$
\delta\nu^2,
$$

a contradiction.

$$
\square
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 12. Corollary — arbitrarily high heat-PFET / paid events

Apply Theorem 11.1 to the first-crossing intervals:

$$
I_n
=
[\rho_n,\sigma_n].
$$

Here:

$$
\delta
=
\frac{
\kappa_{HB}
}{
4
}.
$$

Therefore for every sufficiently large:

$$
n,
$$

either:

$$
\boxed{
\lambda_n
\int_{I_n}
(F_{b,n})_+
dt
\ge
c_{HB}\nu^2
}
\tag{12.1}
$$

or:

$$
\boxed{
\lambda_n
\int_{I_n}
(F_{a,n})_-
dt
\ge
c_{HB}\nu^2,
}
\tag{12.2}
$$

where:

$$
F_{a,n}
=
F_{
a\lambda_n^{-2}
},
$$

$$
F_{b,n}
=
F_{
b\lambda_n^{-2}
},
$$

and:

$$
c_{HB}>0
$$

is universal for the fixed filter parameters and LP decomposition.

Thus a hypothetical finite-time singularity produces arbitrarily high, near-horizon, scale-critical events of one of the two forms:

$$
\boxed{
\text{forward heat-filter interscale work}
}
$$

or:

$$
\boxed{
\text{heat-filter backscatter}.
}
$$

---

# 13. PFET / paid interpretation

For the coarser filter:

$$
s_b,
$$

positive:

$$
F_{s_b}
$$

means resolved kinetic energy is transferred forward into the unresolved scales.

This is the same physical sign as the forward coarse flux:

$$
\Pi^\ell>0
$$

in the FCBP / external pressure--flux ledger.

For the finer filter:

$$
s_a,
$$

negative:

$$
F_{s_a}
$$

is backscatter from unresolved to resolved scales.

FCBP-03 / FCBP-05 / FCBP-06 already place persistent negative combined work / backscatter on the explicitly paid side.

Therefore Theorem 11.1 is structurally aligned with the existing split:

$$
\boxed{
\text{visible forward work}
\ \vee\
\text{paid backscatter}.
}
\tag{13.1}
$$

This is not merely an analogy.

The heat-semigroup coarse equation in FCBP-04 uses exactly the same Reynolds-covariance flux definition:

$$
\Pi
=
-R:\nabla U.
$$

---

# 14. Why pressure does not obstruct the whole-space bridge

The FCBP / external local combined work is:

$$
G
=
\Pi
+
\nabla\cdot(PU).
$$

On the whole space, for the smooth finite-energy class used in the present argument, the pressure transport is a divergence and contributes zero to the global energy balance.

Therefore:

$$
\boxed{
\int_{\mathbb R^3}
G\,dx
=
\int_{\mathbb R^3}
\Pi\,dx
=
F_s.
}
\tag{14.1}
$$

Thus the whole-space heat-band bridge is already a pressure--flux work bridge.

The difficulty begins only when one restricts to a finite local window, where pressure transport is physical and must remain in the ledger.

---

# 15. Compatibility with FCBP-04 heat filtering

FCBP-04 proves internally that for:

$$
S_s=e^{s\Delta},
$$

the covariance:

$$
R
=
S_s(u\otimes u)
-
U\otimes U
$$

is nonnegative because the heat kernel is nonnegative.

It also proves the coarse Navier--Stokes equation for a time-dependent:

$$
s(t),
$$

and constructs a co-moving heat pressure--flux ledger.

DCRP-11 uses only **fixed** heat filters on each first-crossing interval.

Thus no filter-drift term is present.

Across the sequence:

$$
n\to\infty,
$$

the physical filter scale changes as:

$$
s_{a,n},
s_{b,n}
\sim
\lambda_n^{-2},
$$

but the relative heat parameters:

$$
a,
\qquad
b
$$

remain fixed.

Therefore the constants in Theorem 11.1 do not degenerate with:

$$
n.
$$

This bypasses the old moving-filter switching issue at the one-event level.

---

# 16. Why DCRP-11 does not yet close the MORP zero kernel

The theorem above is global in space.

MORP and the external finite-window PFET framework are built from normalized local windows and local test families.

The external PFET work is:

$$
\mathcal W_{I,r}[\phi]
=
r^{-1}
\int_I
\int
\left(
\phi\Pi
-
PU\cdot\nabla\phi
\right)
dxdt.
$$

The whole-space identity corresponds formally to:

$$
\phi\equiv1,
$$

for which the pressure term disappears.

But:

$$
\phi\equiv1
$$

is not a compact local normalized window.

Therefore one cannot yet write:

$$
\boxed{
F_s\ne0
\Longrightarrow
\mathsf O_{\rm PFET}(D_\ast)>0
}
$$

for a specific local MORP minimal obstruction.

A localization theorem is still required.

This is the only major compatibility gap introduced by the present bridge.

---

# 17. Measure-theoretic localization alternative

Consider the forward-work case.

Define the nonnegative work measure on:

$$
I_n\times\mathbb R^3
$$

by:

$$
\boxed{
d\mu_n^+
=
\frac{
\lambda_n
(\Pi^{s_{b,n}})_+
\,dxdt
}{
M_n^+
},
}
\tag{17.1}
$$

where:

$$
M_n^+
=
\lambda_n
\int_{I_n}
\int
(\Pi^{s_{b,n}})_+
dxdt.
$$

When the forward branch occurs:

$$
M_n^+
\ge
c_{HB}\nu^2.
$$

Thus:

$$
\mu_n^+
$$

is a probability measure.

Rescale parabolically at:

$$
\lambda_n:
$$

$$
y
=
\lambda_n(x-x_n),
$$

$$
\tau
=
\lambda_n^2(t-t_n).
$$

The normalized positive-work measures again have unit mass.

After one-point compactification in the spatial variable and compactification of bounded normalized-time windows, every sequence has a weak-star subsequence.

There are only two generic outcomes relevant to local visibility.

### Localized work

A fixed normalized parabolic cell captures a positive fraction:

$$
\boxed{
\limsup_n
\mu_n^+
(
Q_R(y_n,\tau_n)
)
>0
}
\tag{17.2}
$$

for some fixed:

$$
R<\infty.
$$

Then recentering at that cell produces nonzero local forward-flux visibility.

### Diffuse / escaping work

Every fixed normalized parabolic cell captures vanishing mass.

Then the positive heat-flux work itself is a diffuse / escaping native work carrier.

The same alternative applies to the negative/backscatter measure.

Status:

$$
\boxed{
\textbf{ELEMENTARY COMPACTNESS REDUCTION}.
}
$$

This does not yet prove that the diffuse alternative contradicts:

$$
\mathsf R_{\rm nat}=0.
$$

That package-completion statement is the next target.

---

# 18. Local work versus local combined work

Even if:

$$
\Pi
$$

has a positive localized pairing, the local combined work:

$$
G
=
\Pi+\nabla\cdot(PU)
$$

may suffer pressure--flux cancellation.

This is already an explicit FCBP warning.

However the combined PFET architecture does not consist only of the signed scalar:

$$
G.
$$

FCBP-05 / FCBP-06 retain separate pressure, flux, energy, and trace channels in the combined observation package.

Therefore a local nonzero flux event may be routed in one of two ways:

1. it is visible in the separate flux channel;

2. cancellation in the combined work requires a compensating pressure-work channel, which is itself retained.

The exact quantitative local lower bound still depends on the finite-window detector / quotient geometry.

No automatic universal constant is asserted here.

---

# 19. NEW CONDITIONAL THEOREM — local PFET/paid collision

## Theorem 19.1

Assume the first-crossing heat-band event of Theorem 12.1 is completed into a local MORP return package with the following property.

For every normalized heat-filter forward/backscatter work measure with total critical mass at least:

$$
c_{HB}\nu^2,
$$

either:

### local visibility

a fixed normalized finite window carries a detector amount:

$$
\mathsf O_{\rm PFET}
\ge
c_\ast>0;
$$

or:

### paid visibility

the negative-work / leakage realization satisfies:

$$
\mathsf{Paid}
\ge
c_\ast>0;
$$

or:

### noncompact work defect

the diffuse / escaping work measure is retained in:

$$
\mathsf R_{\rm nat}
$$

with:

$$
\mathsf R_{\rm nat}
\ge
c_\ast>0.
$$

Then no zero-cost MORP minimal obstruction can contain the supplier first-crossing mechanism.

### Proof

Theorem 12.1 gives a fixed positive heat-filter forward or backscatter event.

By the assumed package-completion property, at least one of:

$$
\mathsf O_{\rm PFET},
$$

$$
\mathsf{Paid},
$$

$$
\mathsf R_{\rm nat}
$$

is strictly positive.

But a zero-cost minimal obstruction satisfies:

$$
\mathsf O_{\rm PFET}
=
\mathsf{Paid}
=
\mathsf R_{\rm nat}
=
0.
$$

Contradiction.

$$
\square
$$

Status:

$$
\boxed{
\textbf{CONDITIONAL only on the stated localization/package-completion lemma}.
}
$$

---

# 20. What has been closed in this round

## Closed A — filter-physics mismatch at the global level

A supplier shell does not need to be compared directly with a compact-mollifier flux.

The same supplier forces a nonzero **heat-band** energy.

Heat filters are already part of the FCBP internal coarse-graining architecture.

## Closed B — unsigned ancestry versus paid work

The heat-band first crossing gives a signed alternative:

$$
\boxed{
\text{forward heat flux}
\vee
\text{heat backscatter}.
}
$$

Thus the supplier mechanism genuinely enters the visible-work / paid-backscatter split.

## Closed C — pressure ambiguity globally

Whole-space pressure transport integrates out.

The global heat-band bridge is an exact pressure--flux work statement.

---

# 21. What remains open

Only one closure-facing issue remains in this branch:

$$
\boxed{
\textbf{
whole-space critical heat-work event}
\Longrightarrow
\textbf{
local completed MORP PFET/paid/native coordinate}.
}
}
\tag{21.1}
$$

The failure modes are now very specific:

1. spatial diffusion of positive work;
2. temporal diffusion / long normalized crossing;
3. pressure--flux cancellation inside a selected local scalar work test;
4. mismatch between the local heat-filter package and the exact finite-window detector family;
5. failure to retain the diffuse work measure as a native residual.

No new Navier--Stokes mechanism remains hidden behind the term "spectral flux".

---

# 22. Next exact target — Heat-Flux Localization / Package-Completion Lemma

The next proof target is:

$$
\boxed{
\textbf{
Heat-Flux Localization / Package-Completion Lemma}.
}
$$

A useful sufficient version is:

Let:

$$
I_n
$$

be heat-band first-crossing intervals and let:

$$
\lambda_n\to\infty.
$$

Suppose:

$$
\lambda_n
\int_{I_n}
(F_{b,n})_+
dt
\ge
c\nu^2
$$

or:

$$
\lambda_n
\int_{I_n}
(F_{a,n})_-
dt
\ge
c\nu^2.
$$

Then after parabolic recentering and subsequence extraction, prove at least one of:

1. **local PFET atom**

   a fixed normalized finite window has nonzero separate pressure/flux/energy/trace detector norm;

2. **paid local backscatter/leakage**

   a fixed normalized finite window has nonzero paid-side tax;

3. **completed diffuse work defect**

   the normalized work measures have no local atom, but their noncompact / diffuse limit is retained as a nonzero native residual.

A proof of this lemma would combine with Theorem 19.1 to eliminate the entire supplier first-crossing mechanism from the MORP zero-cost kernel.

---

# 23. Stronger route suggested by the supplier endpoint atom

DCRP-08 already supplies a spatially localized critical shell atom at the supplier endpoint after recentering:

$$
\boxed{
\lambda_Q
\int_{
B_{r_0/\lambda_Q}(x_Q)
}
|u_Q(x,t_Q)|^2dx
\ge
c\nu^2.
}
\tag{23.1}
$$

This suggests a stronger version of the localization lemma:

> anchor the local heat-band / pressure--flux package to the supplier center:
>
> $$
> x_Q.
> $$
>
> If the positive heat-work is not visible in a bounded normalized neighborhood of that center, then the supplier energy must have entered through localization transport / leakage or the work must remain spatially nonlocal.
>
> Either alternative is a candidate paid/native residual.

The missing step is a local elliptic / commutator comparison between:

$$
u_Q
$$

and the heat-band resolved difference in a bounded normalized neighborhood.

This is a finite-scale harmonic-analysis problem, not a new global NS mechanism problem.

---

# 24. Source ledger

## Internal FCBP sources

### FCBP-03

`NS_FCBP_03_SignedWork_SlowScale_Telescoping_v0.1.md`

Relevant structures:

$$
G^\ell
=
\Pi^\ell+\nabla\cdot(P^\ell U^\ell),
$$

the signed forward/backscatter work split, and the paid-side backscatter ledger.

### FCBP-04

`NS_FCBP_04_MovingFilter_HorizonAlignment_v0.1.md`

Relevant established internal modules:

$$
S_s=e^{s\Delta},
$$

$$
R=S_s(u\otimes u)-U\otimes U,
$$

$$
R\ge0,
$$

the heat-filter coarse Navier--Stokes equation, and the co-moving heat pressure--flux ledger.

### FCBP-05 / FCBP-06

Relevant architecture:

- separate pressure / flux / energy / trace visibility;
- pressure--flux cancellation warning;
- backscatter / leakage on the paid side;
- combined-invisible residual branch;
- native residual completion.

### MORP-01

Relevant zero-cost kernel:

$$
\mathsf O_{\rm PFET}
=
0,
$$

$$
\mathsf{Paid}
=
0,
$$

$$
\mathsf R_{\rm nat}
=
0.
$$

---

## External primary source

Runlong Yu, *Coarse-Grained Resolution and Pressure--Flux Work Depletion for Navier--Stokes CKN Badness*, arXiv:2606.25322v1.

Primary facts independently checked:

- compact spatial coarse graining;
- Reynolds covariance:

  $$
  R^\ell
  =
  S_\ell(u\otimes u)
  -
  U^\ell\otimes U^\ell;
  $$

- resolved interscale work:

  $$
  \Pi^\ell
  =
  -
  R^\ell:\nabla U^\ell;
  $$

- combined pressure--flux work:

  $$
  G^\ell
  =
  \Pi^\ell
  +
  \nabla\cdot(P^\ell U^\ell);
  $$

- local normalized work:

  $$
  \mathcal W_{I,r}[\phi]
  =
  r^{-1}
  \int
  \left(
  \phi\Pi^\ell
  -
  P^\ell U^\ell\cdot\nabla\phi
  \right);
  $$

- exact finite-chain telescope;
- explicit statement that coarse observability is a separate open compactness/separation problem and is not automatic from the resolved-energy identity.

The present heat-filter bridge is an internal DCRP/FCBP derivation and is not attributed to Yu's compact-mollifier theorem.

---

## Cheskidov--Dai

Alexey Cheskidov and Mimi Dai, *Regularity criteria for the 3D Navier-Stokes and MHD equations*, arXiv:1507.06611v6.

Used through DCRP-08 for the dissipation-boundary supplier shell:

$$
\lambda_Q
\|u_Q\|_2^2
\gtrsim
\nu^2.
$$

---

# 25. End state

The Spectral-Flux / PFET compatibility problem has been substantially reduced.

The key new theorem is:

$$
\boxed{
\begin{aligned}
\text{supplier critical shell}
&\Longrightarrow
\text{critical heat-band first crossing}\\
&\Longrightarrow
\text{coarse heat-filter forward work}\\
&\qquad\vee
\text{fine heat-filter backscatter}.
\end{aligned}
}
$$

Quantitatively:

$$
\boxed{
\lambda
\int_I
(F_{s_b})_+
dt
+
\lambda
\int_I
(F_{s_a})_-
dt
\ge
c\nu^2.
}
$$

Thus the supplier mechanism already lands in the physical **PFET forward-work / paid-backscatter split** at the whole-space heat-filter level.

The sole closure-facing gap in this route is now:

$$
\boxed{
\textbf{
global heat-work}
\Longrightarrow
\textbf{
local completed PFET / paid / native package}.
}
$$

The next exact target is:

$$
\boxed{
\textbf{
Heat-Flux Localization / Package-Completion Lemma}.
}
$$

If that lemma is proved, the supplier first-crossing mechanism is incompatible with the MORP zero-cost kernel.

---

# Checkpoint v12 Update — DCRP-12

# NS-DCRP-12 — Local PFET Localization, Work-Carrier Completion, and the Quantitative Anti-Diffusion Frontier

- date: 2026-08-16
- status: research proof checkpoint
- canonical source: UTF-8 Markdown
- canonical math delimiters: `$...$` and `$$...$$`
- objective: close the DCRP-11 global-to-local heat-work localization gap and determine exactly what remains if a fixed critical amount of work diffuses over an unbounded number of normalized parabolic cells.
- no full Navier--Stokes regularity claim is made.
- principal internal dependencies:
  - FCBP-04 heat-semigroup coarse pressure--flux ledger;
  - FCBP-05 combined pressure / resolved-flux / positive-energy / adjoint-trace observation map;
  - MORP-01 native residual channel;
  - MORP-02 spatial / relative-scale defect completion;
  - DCRP-08 through DCRP-11.
- external primary calibration:
  - Runlong Yu, arXiv:2606.25322v1;
  - Cheskidov--Dai, arXiv:1507.06611v6.

---

# 1. Executive result

DCRP-11 proved that every sufficiently high heat-band first-crossing event satisfies one of:

$$
\boxed{
\lambda_n
\int_{I_n}
(F_{b,n})_+
\,dt
\ge
c_{HB}\nu^2
}
\tag{1.1}
$$

or:

$$
\boxed{
\lambda_n
\int_{I_n}
(F_{a,n})_-
\,dt
\ge
c_{HB}\nu^2,
}
\tag{1.2}
$$

where:

$$
F_{*,n}(t)
=
\int_{\mathbb R^3}
\Pi_{*,n}(x,t)
\,dx
$$

is the whole-space heat-filter interscale work.

The remaining problem was to convert this global work into a local MORP / PFET / paid coordinate.

The localization part is now elementary once the internal FCBP-05 observation architecture is used correctly.

FCBP-05 does not retain only the single combined scalar work.

Its combined observation map contains separate channels:

$$
\boxed{
O_W^{comb}
=
(
O_W^P,
O_W^F,
O_W^E,
O_W^T
),
}
\tag{1.3}
$$

with active pressure, resolved flux, positive energy, and adjoint-trace components.

Therefore a nonzero local flux pairing is already a valid PFET-visible event even if a pressure term would cancel it in the scalar combined work.

The first new theorem is:

$$
\boxed{
\textbf{
nonzero whole-space heat flux}
\Longrightarrow
\textbf{
nonzero finite-window heat-flux pairing}.
}
}
\tag{1.4}
$$

The proof uses only a fixed-shape parabolic partition of unity.

No solution-dependent detector shape is needed.

The second new result is a compactness alternative for a sequence of fixed-total critical work events.

After normalizing every event to the filter scale, one has:

$$
\boxed{
\textbf{
local PFET atom}
\ \vee\
\textbf{
local paid backscatter}
\ \vee\
\textbf{
space/time work escape}.
}
}
\tag{1.5}
$$

The third alternative is a genuine PDE-generated work carrier.

It is compatible with the MORP-02 defect-completion philosophy:

- spatial non-tightness is represented by a compactified spatial defect;
- transition / temporal non-tightness is retained in the native residual side.

Thus the qualitative package-completion gap of DCRP-11 is closed **provided the heat-work escape coordinate is admitted as the concrete native residual already reserved abstractly by MORP-01**.

What is not yet closed is the quantitative coercive version.

A fixed global critical work amount can be divided among:

$$
N_n\to\infty
$$

normalized cells so that every single local coefficient tends to zero.

Therefore:

$$
\boxed{
\text{global critical work}
\not\Rightarrow
\text{uniform local detector gap}
}
\tag{1.6}
$$

without an anti-diffusion / bounded-multiplicity theorem.

The next frontier is therefore:

$$
\boxed{
\textbf{
Quantitative Work Anti-Diffusion / Critical Lift Lemma}.
}
$$

---

# 2. Source audit — what the existing PFET detector actually sees

The external coarse-grained work theorem defines the combined distribution:

$$
G^\ell
=
\Pi^\ell
+
\nabla\cdot(P^\ell U^\ell).
$$

Its active work detector is finite-dimensional and tests:

$$
\langle
G^\ell,
\phi
\rangle.
$$

It explicitly warns that pressure and flux may cancel in the scalar combined work.

However the same paper also records the signed component ledger:

$$
\boxed{
\mathcal F_{I,r}[\phi]
=
r^{-1}
\int_I
\int
\phi\Pi^\ell
\,dxdt,
}
\tag{2.1}
$$

and:

$$
\boxed{
\mathcal P_{I,r}[\phi]
=
-
r^{-1}
\int_I
\int
P^\ell U^\ell\cdot\nabla\phi
\,dxdt.
}
\tag{2.2}
$$

with:

$$
\mathcal W
=
\mathcal F
+
\mathcal P.
$$

The internal FCBP-05 architecture goes further and declares the combined observation vector:

$$
\boxed{
O_W^{comb}
=
(
O_W^P,
O_W^F,
O_W^E,
O_W^T
).
}
\tag{2.3}
$$

Therefore, for the present internal MORP program:

$$
\boxed{
O_W^F\ne0
\Longrightarrow
\mathsf O_{\rm PFET}>0.
}
\tag{2.4}
$$

Pressure--flux cancellation does not erase a nonzero **separate flux channel**.

This distinction is essential for the theorem below.

---

# 3. Fixed-shape spatial partition

Choose one nonnegative smooth function:

$$
\chi\in C_c^\infty(\mathbb R^3),
$$

and a lattice:

$$
\{y_j\}_{j\in\mathbb Z^3}
$$

such that:

$$
\boxed{
\sum_{j\in\mathbb Z^3}
\chi(y-y_j)
=
1
}
\tag{3.1}
$$

for all:

$$
y\in\mathbb R^3.
$$

Assume:

$$
\chi
$$

has support in a fixed ball:

$$
B_R(0),
$$

and the family has uniformly bounded overlap.

At physical scale:

$$
r>0,
$$

define:

$$
\boxed{
\chi_{j,r}(x)
=
\chi
\left(
\frac{x}{r}-y_j
\right).
}
\tag{3.2}
$$

Then:

$$
\sum_j
\chi_{j,r}(x)
=
1.
$$

Every:

$$
\chi_{j,r}
$$

is the translation / parabolic-scale pullback of one fixed reference profile.

Thus adaptive choice of:

$$
j
$$

is only a re-centering choice.

It does not change the detector shape.

---

# 4. Local integrability of heat-filter flux

Fix:

$$
s>0.
$$

For a smooth pre-singularity finite-energy solution:

$$
U^s
=
e^{s\Delta}u
$$

is spatially smooth.

The heat covariance:

$$
R^s
=
e^{s\Delta}(u\otimes u)
-
U^s\otimes U^s
$$

belongs to:

$$
L^1_x
$$

for each fixed time.

Also:

$$
\nabla U^s
$$

is bounded for positive:

$$
s.
$$

Therefore:

$$
\Pi^s
=
-
R^s:\nabla U^s
$$

belongs to:

$$
L^1_x.
$$

On every finite pre-singularity time interval:

$$
\Pi^s
$$

is locally integrable in spacetime, and the spatial partition can be summed by dominated convergence / absolute integrability.

Thus:

$$
\boxed{
F_s(t)
=
\sum_j
\int
\chi_{j,r}(x)
\Pi^s(x,t)
\,dx
}
\tag{4.1}
$$

for almost every time.

---

# 5. NEW THEOREM — spatial localization of signed heat flux

## Theorem 5.1

Let:

$$
J
$$

be a finite time interval and suppose:

$$
\boxed{
\int_J
F_s(t)
\,dt
>
0.
}
\tag{5.1}
$$

Then for every:

$$
r>0,
$$

there exists:

$$
j\in\mathbb Z^3
$$

such that:

$$
\boxed{
\int_J
\int
\chi_{j,r}(x)
\Pi^s(x,t)
\,dxdt
>
0.
}
\tag{5.2}
$$

Similarly, if:

$$
\int_J
F_s(t)
\,dt
<
0,
$$

then there exists:

$$
j
$$

with the corresponding local flux pairing negative.

### Proof

Using the partition of unity:

$$
\begin{aligned}
\int_J
F_s(t)
dt
&=
\int_J
\int
\Pi^s(x,t)
\,dxdt\\
&=
\sum_j
\int_J
\int
\chi_{j,r}(x)
\Pi^s(x,t)
\,dxdt.
\end{aligned}
$$

The sum is absolutely convergent after the standard locally finite partition / exhaustion argument.

If every summand were nonpositive, the total could not be positive.

Therefore at least one summand is positive.

The negative case is identical.

$$
\square
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 6. Temporal localization does not require a new test shape

DCRP-11 gives:

$$
\int_I
(F_s)_+
dt
>
0
$$

or:

$$
\int_I
(F_s)_-
dt
>
0.
$$

Suppose the forward case holds.

Then the measurable set:

$$
A
=
\{
t\in I:
F_s(t)>0
\}
$$

has positive measure.

For almost every:

$$
t\in A,
$$

equation (4.1) implies that at least one spatial cell satisfies:

$$
\int
\chi_{j,r}\Pi^s
>
0.
$$

Because the index set is countable, there exists at least one:

$$
j_\ast
$$

for which:

$$
\boxed{
A_{j_\ast}
=
\left\{
t\in A:
\int
\chi_{j_\ast,r}\Pi^s
>
0
\right\}
}
\tag{6.1}
$$

has positive measure.

Let:

$$
h(t)
=
\int
\chi_{j_\ast,r}\Pi^s(x,t)
\,dx.
$$

Then:

$$
h>0
$$

on a set of positive measure.

By the Lebesgue differentiation theorem, there exists a Lebesgue point:

$$
t_\ast
$$

with:

$$
h(t_\ast)>0.
$$

Therefore there are arbitrarily small intervals:

$$
J_\ast
\ni
t_\ast
$$

such that:

$$
\boxed{
\int_{J_\ast}
h(t)
\,dt
>
0.
}
\tag{6.2}
$$

Choose a fixed nonnegative reference bump:

$$
\eta\in C_c^\infty((-1,1))
$$

with:

$$
\eta(0)>0.
$$

By choosing a sufficiently small interval around:

$$
t_\ast,
$$

the rescaled pullback of:

$$
\eta
$$

also has positive pairing.

Hence the local spacetime detector can use one fixed reference profile:

$$
\boxed{
\phi_{j_\ast}(x,t)
=
\chi_{j_\ast,r}(x)
\eta
\left(
\frac{
t-t_\ast
}{
\delta
}
\right).
}
\tag{6.3}
$$

The only adaptive data are:

- spatial center;
- temporal center;
- temporal thickness.

These are already standard moving-window / re-root variables.

No solution-dependent detector **shape** is required.

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 7. NEW THEOREM — exact global-to-local heat-PFET bridge

## Theorem 7.1

Assume:

$$
\lambda
\int_I
(F_s)_+
dt
>
0.
$$

Let:

$$
r
=
\lambda^{-1}.
$$

Then there exists a finite parabolic window:

$$
W
=
B_{Cr}(x_\ast)
\times
J_\ast
$$

and a fixed-shape nonnegative local test:

$$
\phi
$$

such that:

$$
\boxed{
r^{-1}
\int_W
\phi(x,t)
\Pi^s(x,t)
\,dxdt
>
0.
}
\tag{7.1}
$$

If instead:

$$
\lambda
\int_I
(F_s)_-
dt
>
0,
$$

then there exists a finite window and test with:

$$
\boxed{
r^{-1}
\int_W
\phi\Pi^s
\,dxdt
<
0.
}
\tag{7.2}
$$

### Proof

Apply Section 6 with:

$$
r=\lambda^{-1}.
$$

Multiply the nonzero local pairing by:

$$
r^{-1}=\lambda.
$$

The sign is unchanged.

$$
\square
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 8. Corollary — exact PFET-zero kernel cannot contain a heat-work event

Assume the internal heat-filter branch is included in the resolved-flux channel:

$$
O_W^F.
$$

If:

$$
O_W^F=0
$$

for every admissible re-rooted local heat-filter window, then:

$$
\boxed{
F_s(t)=0
}
\tag{8.1}
$$

almost everywhere for that filter scale along the corresponding physical interval.

Indeed any positive or negative whole-space work event would produce a nonzero local flux detector by Theorem 7.1.

Therefore:

$$
\boxed{
\textbf{
exact heat-PFET invisibility}
\Longrightarrow
\textbf{
no nonzero whole-space heat-filter work event}.
}
}
\tag{8.2}
$$

Combining with DCRP-11:

$$
\boxed{
\textbf{
supplier heat-band first crossing}
\notin
\ker O_W^F.
}
}
\tag{8.3}
$$

Consequently, under the internal MORP meaning:

$$
\mathsf O_{\rm PFET}=0
$$

which includes the heat-resolved flux channel,

$$
\boxed{
\textbf{
a supplier heat-band first-crossing event is excluded from the exact PFET-zero kernel.
}
}
\tag{8.4}
$$

Status:

$$
\boxed{
\textbf{PROVED conditional only on compiler inclusion of the already-established FCBP-04 heat-flux channel in }O_W^F.
}
$$

This is a compiler-membership condition, not a new PDE estimate.

---

# 9. Why pressure cancellation no longer blocks exact localization

The external local scalar work is:

$$
\mathcal W
=
\mathcal F
+
\mathcal P.
$$

A nonzero:

$$
\mathcal F
$$

may be canceled by:

$$
\mathcal P
$$

inside:

$$
\mathcal W.
$$

But FCBP-05's internal observation vector contains:

$$
O_W^F
$$

and:

$$
O_W^P
$$

separately.

Therefore:

$$
\boxed{
\mathcal F\ne0
\Longrightarrow
O_W^{comb}\ne0
}
\tag{9.1}
$$

for the internal combined observation norm, regardless of scalar combined-work cancellation.

This is exactly why DCRP-12 uses the FCBP-05 combined **observation map**, not only the external scalar work detector.

---

# 10. Quantitative localization is harder than exact localization

Theorem 7.1 gives:

$$
\text{global nonzero}
\Longrightarrow
\text{local nonzero}.
$$

It does **not** give a universal constant:

$$
c_\ast>0
$$

such that:

$$
\left|
r^{-1}
\int_W
\phi\Pi^s
\right|
\ge
c_\ast.
$$

A fixed global work amount may be spread over many disjoint normalized cells.

This is not a technicality.

It is the exact quantitative anti-phantom problem.

---

# 11. NO-GO — fixed total work does not imply fixed local share

Let:

$$
N\in\mathbb N.
$$

Consider a model nonnegative normalized work density consisting of:

$$
N
$$

mutually disjoint, congruent normalized parabolic packets:

$$
w_N
=
\frac1N
\sum_{j=1}^N
w^{(j)},
$$

with:

$$
\int
w^{(j)}
=
1.
$$

Then:

$$
\int
w_N
=
1,
$$

but every packet carries only:

$$
\frac1N.
$$

Thus:

$$
\boxed{
\sup_{\text{unit normalized cell}}
\int_{\text{cell}}
w_N
\to0.
}
\tag{11.1}
$$

while total work remains fixed.

Therefore:

$$
\boxed{
\textbf{
global critical work}
\not\Rightarrow
\textbf{
uniform local critical work}
}
\tag{11.2}
$$

at the level of measure theory.

This model is not asserted to be generated by a Navier--Stokes solution.

Its role is to prove that a quantitative local lower bound requires additional PDE structure.

Status:

$$
\boxed{
\textbf{NO-GO PROVED at the measure-theoretic level}.
}
$$

---

# 12. Critical normalized work measures

For the forward heat-work branch define:

$$
\boxed{
d\mu_n^+
=
\lambda_n
(\Pi_n)_+
\,dxdt.
}
\tag{12.1}
$$

DCRP-11 implies:

$$
\boxed{
\mu_n^+
(
I_n\times\mathbb R^3
)
\ge
c_{HB}\nu^2.
}
\tag{12.2}
$$

Likewise, on the backscatter branch:

$$
\boxed{
d\mu_n^-
=
\lambda_n
(\Pi_n)_-
\,dxdt
}
\tag{12.3}
$$

has total mass bounded below.

Normalize:

$$
\boxed{
\widehat\mu_n^\pm
=
\frac{
\mu_n^\pm
}{
\mu_n^\pm(
I_n\times\mathbb R^3
)
}.
}
\tag{12.4}
$$

These are probability measures.

Introduce parabolic coordinates:

$$
y
=
\lambda_n
(
x-x_n
),
$$

$$
\tau
=
\lambda_n^2
(
t-t_n
),
$$

where:

$$
x_n,t_n
$$

are allowed package re-root coordinates.

The normalized measures live on a parabolic scale-one spacetime.

---

# 13. Cell concentration function

Fix a reference normalized parabolic cell:

$$
\mathcal Q_R
=
B_R(0)
\times
(-R^2,0).
$$

Define the concentration function:

$$
\boxed{
\mathfrak C_n(R)
=
\sup_{(y_0,\tau_0)}
\widehat\mu_n^\pm
\left(
B_R(y_0)
\times
(\tau_0-R^2,\tau_0)
\right).
}
\tag{13.1}
$$

There are two possibilities after subsequence extraction.

### Tight / concentrated work

For some:

$$
R<\infty,
$$

$$
\boxed{
\limsup_n
\mathfrak C_n(R)
>
0.
}
\tag{13.2}
$$

### Vanishing / diffuse work

For every fixed:

$$
R<\infty,
$$

$$
\boxed{
\mathfrak C_n(R)
\to0.
}
\tag{13.3}
$$

This is the standard concentration-versus-vanishing alternative at fixed parabolic scale.

---

# 14. NEW THEOREM — local flux / backscatter / escape trichotomy

## Theorem 14.1

Let:

$$
\mu_n
$$

be one of the positive critical work measures:

$$
\mu_n^+
$$

or:

$$
\mu_n^-,
$$

with:

$$
\mu_n(\mathbb R^3\times I_n)
\ge
m_0>0.
$$

After subsequence extraction, at least one of the following occurs.

### A. Local work concentration

There exist:

$$
R<\infty,
$$

$$
\eta>0,
$$

and normalized parabolic cells:

$$
Q_n
$$

such that:

$$
\boxed{
\mu_n(Q_n)
\ge
\eta m_0.
}
\tag{14.1}
$$

### B. Spatial / temporal work vanishing

For every fixed:

$$
R,
$$

$$
\boxed{
\sup_{Q_R}
\mu_n(Q_R)
\to0.
}
\tag{14.2}
$$

In branch B, after recentering at any sequence of scale-one cells, the normalized work measures converge locally to zero.

Equivalently, their mass leaves every bounded normalized spacetime region.

### Proof

Apply the concentration function of Section 13.

If:

$$
\limsup_n
\mathfrak C_n(R)>0
$$

for some:

$$
R,
$$

take:

$$
\eta
$$

below that positive limit and select maximizing cells.

Otherwise:

$$
\mathfrak C_n(R)\to0
$$

for every:

$$
R,
$$

which is exactly B.

$$
\square
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 15. Concentrated positive work gives visibility or paid cancellation

Suppose branch A of Theorem 14.1 occurs for the positive flux measure:

$$
\mu_n^+.
$$

Let:

$$
Q_n
$$

be a cell with:

$$
\boxed{
\lambda_n
\int_{Q_n}
(\Pi_n)_+
\,dxdt
\ge
\eta m_0.
}
\tag{15.1}
$$

Let:

$$
N_n
=
\lambda_n
\int_{Q_n}
(\Pi_n)_-
\,dxdt.
$$

There are two cases.

### Visible signed flux

If:

$$
N_n
\le
\frac12
\eta m_0,
$$

then:

$$
\boxed{
\lambda_n
\int_{Q_n}
\Pi_n
\,dxdt
\ge
\frac12
\eta m_0.
}
\tag{15.2}
$$

A fixed nonnegative cutoff supported slightly larger than:

$$
Q_n
$$

therefore gives a nonzero resolved-flux observation.

### Local backscatter payment

If:

$$
N_n
>
\frac12
\eta m_0,
$$

then:

$$
\boxed{
\lambda_n
\int_{Q_n}
(\Pi_n)_-
\,dxdt
\ge
\frac12
\eta m_0.
}
\tag{15.3}
$$

Thus a fixed positive amount of local backscatter is present.

Therefore:

$$
\boxed{
\textbf{
local positive-work concentration}
\Longrightarrow
\textbf{
local resolved-flux visibility}
\ \vee\
\textbf{
local paid backscatter}.
}
}
\tag{15.4}
$$

The same conclusion, with signs reversed, applies when the original DCRP-11 branch is already backscatter-dominated.

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 16. Work-escape as a native PDE residual

Branch B of Theorem 14.1 is not a zero object.

The total normalized work mass remains:

$$
\ge m_0,
$$

but every bounded normalized spacetime cell sees asymptotically zero mass.

This is exactly a non-tight native carrier.

MORP-02 already implements the same compactness principle for:

- relative-frequency carrier mass;
- normalized spatial carrier mass;
- selected trace mass.

In particular it explicitly distinguishes:

$$
\boxed{
\text{finite spatial carrier}
}
$$

from:

$$
\boxed{
\text{spatial defect at }\infty_x.
}
$$

MORP-01 reserves:

$$
\boxed{
\mathsf R_{\rm nat}
}
$$

for:

> any retained native residual not already included above.

The heat-work measure:

$$
\mu_n^\pm
$$

is generated directly from:

$$
u
$$

through the Navier--Stokes heat coarse-graining:

$$
\Pi^s
=
-
R^s:\nabla U^s.
$$

It contains no copied dangerous label.

Therefore a compactified space/time escape coordinate for:

$$
\mu_n^\pm
$$

is a legitimate **native PDE residual candidate**.

This is a package completion, not a new danger detector.

Status:

$$
\boxed{
\textbf{ARCHITECTURALLY ADMISSIBLE under the existing MORP native-residual definition}.
}
$$

The scalar lower-semicontinuous cost realization of this coordinate is not yet fixed.

---

# 17. Work-completed package theorem

Define a **work-completed MORP package** to retain:

1. the existing state / pressure / trace / scale coordinates;
2. the local heat-resolved flux / backscatter channel;
3. if the normalized heat-work carrier is non-tight, its compactified spatial / temporal escape coordinate.

## Theorem 17.1

Every DCRP-11 supplier heat-band first-crossing sequence has, after subsequence extraction, at least one of:

$$
\boxed{
O_W^F>0,
}
\tag{17.1}
$$

$$
\boxed{
\mathsf{Paid}>0,
}
\tag{17.2}
$$

or:

$$
\boxed{
\mathsf R_{\rm work}>0,
}
\tag{17.3}
$$

where:

$$
\mathsf R_{\rm work}
$$

is the retained compactified work-escape coordinate.

### Proof

Use Theorem 14.1.

If work concentrates, apply Section 15.

If it vanishes locally, retain the non-tight work carrier as:

$$
\mathsf R_{\rm work}.
$$

$$
\square
$$

Status:

$$
\boxed{
\textbf{PROVED at the package-alternative level}.
}
$$

---

# 18. Consequence for the MORP exact zero kernel

Suppose the concrete native-residual implementation includes:

$$
\mathsf R_{\rm work}
$$

as an instance of:

$$
\mathsf R_{\rm nat}.
$$

Then a supplier first-crossing sequence cannot satisfy simultaneously:

$$
\boxed{
O_W^F=0,
}
$$

$$
\boxed{
\mathsf{Paid}=0,
}
$$

and:

$$
\boxed{
\mathsf R_{\rm nat}=0.
}
$$

Therefore:

$$
\boxed{
\textbf{
the supplier first-crossing mechanism is absent from the
work-completed exact zero-cost PFET/Paid/native kernel.
}
}
\tag{18.1}
$$

Status:

$$
\boxed{
\textbf{PROVED conditional on the explicit work-residual package completion}.
}
$$

This does not yet imply Navier--Stokes regularity.

A positive but arbitrarily small local observation cost may remain.

---

# 19. Why this does not yet give a positive coercive gap

The trichotomy proves:

$$
\text{nonzero}
\vee
\text{defect}.
$$

It does not prove a universal quantitative constant for the local visible channel.

A sequence may satisfy:

$$
\boxed{
\max_{\text{unit cells}}
\lambda_n
\left|
\int_{\text{cell}}
\Pi_n
\right|
\to0
}
\tag{19.1}
$$

while total positive / negative critical work remains bounded below, provided the number of active normalized cells diverges.

If that divergence appears as work escape, the completed residual detects it.

But to turn the entire mechanism into a uniform positive scalar cost one must prove a quantitative relationship between:

- local detector norm;
- backscatter tax;
- work-escape residual norm.

That is an additional coercivity theorem.

---

# 20. Connection with FCBP-05's half-exponent barrier

FCBP-05 already identifies the moving-window observability problem as quantitative.

Its sharp temporal theorem shows that the threshold:

$$
\gamma q
=
\frac12
$$

separates window-growth laws that can or cannot be made effective on finite-time horizon schedules.

DCRP-12 explains how that older temporal barrier appears in the present supplier route.

The **qualitative** statement:

$$
\text{global work}
\Longrightarrow
\text{some local work}
$$

is easy.

The difficult statement is:

$$
\boxed{
\text{global critical work}
\Longrightarrow
\text{uniformly nonvanishing normalized local detector}
}
\tag{20.1}
$$

on windows whose centers / thicknesses / multiplicities may change with scale.

Thus the frontier has returned to a sharp quantitative Critical Lift problem, but now for a highly specific NS-generated work carrier rather than an abstract dangerous package.

---

# 21. A stronger quantitative target

Let:

$$
\mu_n
$$

be the normalized forward/backscatter work carrier.

Define its effective parabolic multiplicity:

$$
\boxed{
\mathfrak M_{\rm work}(n)
=
\left[
\sup_{z}
\widehat\mu_n
(
Q_1(z)
)
\right]^{-1}.
}
\tag{21.1}
$$

If:

$$
\mathfrak M_{\rm work}
$$

is uniformly bounded, then:

$$
\boxed{
\sup_z
\widehat\mu_n(Q_1(z))
\ge
c>0,
}
\tag{21.2}
$$

and Section 15 gives a uniform local PFET / backscatter gap.

Therefore only:

$$
\boxed{
\mathfrak M_{\rm work}\to\infty
}
\tag{21.3}
$$

can defeat uniform local observability.

This is now the exact quantitative diffuse-work branch.

The next question is whether Navier--Stokes can sustain:

$$
\mathfrak M_{\rm work}\to\infty
$$

while simultaneously satisfying the supplier / first-crossing / minimal-return constraints.

---

# 22. Candidate finite-energy multiplicity control and why it is not immediate

One might hope that finite kinetic energy bounds the number of active work cells.

This is not automatic.

At physical scale:

$$
r_n
=
\lambda_n^{-1},
$$

a scale-critical kinetic packet has raw energy:

$$
O(r_n).
$$

Therefore the finite total energy budget can still accommodate:

$$
O(r_n^{-1})
$$

such packets at one scale.

As:

$$
r_n\to0,
$$

this number diverges.

Thus:

$$
\boxed{
\text{finite kinetic energy alone}
\not\Rightarrow
\text{bounded work multiplicity}.
}
\tag{22.1}
$$

This is the same critical-summability geometry encountered earlier in CFOP / FCBP.

A new PDE interaction or recurrence constraint is required.

---

# 23. New exact frontier

The Heat-Flux Localization / Package-Completion Lemma is now closed at the qualitative level.

The remaining closure-facing target is:

$$
\boxed{
\textbf{
Quantitative Work Anti-Diffusion / Critical Lift Lemma}.
}
$$

A useful sufficient form would be:

> For every supplier heat-band first-crossing sequence generated by a hypothetical singular branch, one has either:
>
> $$
> \sup_n
> \mathfrak M_{\rm work}(n)
> <
> \infty,
> $$
>
> or a strictly positive native diffuse-work cost survives with a lower-semicontinuous scalar normalization.

If the first alternative holds, the local PFET / paid gap is uniformly positive.

If the second holds, exact minimal invisibility is impossible in the completed package.

The unresolved part is to obtain a **uniform scalar coercive gap**, not merely a nonzero coordinate.

---

# 24. Possible next attack — use the supplier center and first-crossing persistence

DCRP-08 gives a genuine localized supplier atom after critical rescaling.

DCRP-10 gives a first-crossing interval on which the supplier shell stays between two fixed critical levels.

This extra structure is not present in the abstract measure-theoretic no-go of Section 11.

A promising next attack is:

1. anchor normalized work cells at the supplier center;
2. use the localized shell energy identity to show that work lying far from the supplier must enter through boundary transport / pressure / nonlocal interaction;
3. charge that transport to existing leakage / native residual channels;
4. conclude that either a fixed fraction of the work remains within a bounded normalized distance from the supplier, or the paid/native transport cost is positive.

This would turn the supplier's endpoint localization into a quantitative work-tightness theorem.

The next round should attack exactly this anchored form rather than arbitrary work measures.

---

# 25. Source ledger

## Internal FCBP-05

Relevant internal statement:

$$
O_W^{comb}
=
(
O_W^P,
O_W^F,
O_W^E,
O_W^T
),
$$

with active pressure, resolved flux, positive energy, and adjoint-trace channels.

Thus:

$$
O_W^F
$$

is a separate observation coordinate.

## Internal MORP-01

Defines:

$$
\mathsf R_{\rm nat}
$$

for:

> any retained native residual not already included above.

## Internal MORP-02

Already develops defect completion by:

- one-point compactification of relative-frequency carrier distributions;
- analogous compactification for normalized spatial carrier measures;
- retention of trace / scale / spatial escape rather than silent loss.

DCRP-12 applies the same compactness pattern to the PDE-generated heat-work carrier.

## External Yu coarse-grained work theorem

The external theorem confirms:

- local resolved flux:

  $$
  \mathcal F_{I,r}[\phi]
  =
  r^{-1}
  \int
  \phi\Pi;
  $$

- local pressure work;
- combined distribution:

  $$
  G
  =
  \Pi+\nabla\cdot(PU);
  $$

- explicit pressure--flux cancellation ledger;
- finite-dimensional active work coefficients;
- the fact that coarse observability is a separate problem and is not automatic from resolved badness.

The external active detector itself is a detector for:

$$
G,
$$

not for the sum of absolute pressure and flux channels.

DCRP-12's separate-flux conclusion uses the **internal FCBP-05 observation map**, not an attribution to the external scalar detector theorem.

---

# 26. End state

The DCRP-11 localization gap has been reduced to a quantitative issue.

The exact qualitative theorem is:

$$
\boxed{
\text{nonzero global heat-filter work}
\Longrightarrow
\text{nonzero local heat-flux pairing}.
}
$$

For a sequence with fixed total critical work:

$$
\boxed{
\text{local PFET visibility}
\ \vee\
\text{local paid backscatter}
\ \vee\
\text{space/time work escape}.
}
$$

When work escape is explicitly retained as the native residual already allowed by MORP:

$$
\boxed{
\text{supplier first crossing}
\notin
\ker
\left(
O_W^F,
\mathsf{Paid},
\mathsf R_{\rm nat}
\right).
}
$$

The remaining problem is not qualitative invisibility.

It is quantitative diffusion:

$$
\boxed{
\mathfrak M_{\rm work}\to\infty.
}
$$

Therefore the next single frontier is:

$$
\boxed{
\textbf{
Quantitative Work Anti-Diffusion / Critical Lift Lemma,
anchored at the supplier center.
}
}
$$

This is now the next exact attack.
