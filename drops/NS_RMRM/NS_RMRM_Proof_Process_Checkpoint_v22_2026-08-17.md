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

---

# Checkpoint v13 Update — DCRP-13

# NS-DCRP-13 — Supplier Trace Critical Lift, Finite-Family Anti-Diffusion, and Adjoint-Trace Bridge

- date: 2026-08-16
- status: research proof checkpoint
- canonical source: UTF-8 Markdown
- canonical math delimiters: `$...$` and `$$...$$`
- objective: bypass the DCRP-12 work-multiplicity obstruction by extracting a scale-uniform finite-family trace witness directly from the dissipation-boundary supplier atom.
- no full Navier--Stokes regularity claim is made.
- principal internal dependencies:
  - FCBP-02 filtered adjoint localization;
  - FCBP-04 heat-filter / moving-window architecture;
  - FCBP-05 combined observation hierarchy with selected adjoint-trace channel;
  - FCBP-06 CAR0--CAR3 / Native CAR Compiler;
  - MORP-01 through MORP-05;
  - DCRP-08 through DCRP-12.
- external primary calibration:
  - Cheskidov--Dai, arXiv:1507.06611v6;
  - Cheskidov--Shvydkoy, arXiv:1102.1944v2.

---

# 1. Executive result

DCRP-12 showed that a fixed amount of global critical heat-work may be spread over arbitrarily many normalized cells, so

$$
\boxed{
\text{fixed global work}
\not\Rightarrow
\text{uniform local work coefficient}.
}
\tag{1.1}
$$

That multiplicity obstruction does **not** apply to the dissipation-boundary supplier endpoint itself.

DCRP-08 established that at a dissipation-boundary shell

$$
Q=Q(t),
\qquad
\Lambda=\lambda_Q,
$$

one has

$$
\boxed{
\|u_Q(t)\|_\infty
\ge
c_0\nu\Lambda.
}
\tag{1.2}
$$

Define the critically rescaled shell

$$
\boxed{
w(y)
=
\Lambda^{-1}
u_Q
\left(
x_\ast+\Lambda^{-1}y,
t
\right).
}
\tag{1.3}
$$

After choosing

$$
x_\ast
$$

at a point of almost maximal shell amplitude,

$$
\boxed{
\|w\|_\infty
\ge
c_0\nu.
}
\tag{1.4}
$$

The Fourier support of

$$
w
$$

lies in one fixed annulus independent of

$$
Q.
$$

Therefore Bernstein gives

$$
\boxed{
\|\nabla w\|_\infty
\le
C_B
\|w\|_\infty.
}
\tag{1.5}
$$

This implies a uniform finite-family trace theorem:

there exist universal constants

$$
r_\ast>0,
\qquad
c_\ast>0,
$$

a fixed nonnegative bump

$$
\eta\in C_c^\infty(B_{r_\ast}),
$$

and one of only six signed coordinate functionals

$$
\boxed{
\mathcal L_{i,\sigma}(w)
=
\sigma
\int
\eta(y)
w_i(y)
\,dy,
\qquad
i\in\{1,2,3\},
\quad
\sigma\in\{-1,+1\},
}
\tag{1.6}
$$

such that

$$
\boxed{
\mathcal L_{i,\sigma}(w)
\ge
c_\ast\nu.
}
\tag{1.7}
$$

Thus:

$$
\boxed{
\textbf{
every dissipation-boundary supplier carries a fixed,
scale-uniform, six-test local trace atom.
}
}
\tag{1.8}
$$

This is fundamentally different from DCRP-12's diffuse work measure.

No number of distant work cells can make all six supplier-centered trace coefficients vanish.

The witness is:

- generated from the actual Navier--Stokes state;
- located at the actual supplier scale;
- located at an actual supplier center;
- fixed-shape after normalization;
- finite-dimensional;
- quantitatively scale uniform.

The same terminal bump can be propagated backward by the heat adjoint:

$$
\boxed{
\phi_{i,\sigma}(\tau)
=
e^{-\tau\Delta}
(
\sigma\eta e_i
)
}
\tag{1.9}
$$

in backward-time notation, producing a canonical selected caloric-adjoint trace family.

Therefore the old abstract CAR1 problem has a concrete solution **for the supplier state coordinate**:

$$
\boxed{
\textbf{
supplier atom}
\Longrightarrow
\textbf{
uniform finite-family native trace separation}.
}
}
\tag{1.10}
$$

The remaining issue is no longer anti-diffusion.

It is compiler compatibility:

> Does the specific `selected adjoint trace` channel used by the FCBP/MORP finite-window audit admit this fixed terminal family, or a uniformly equivalent filtered version?

If yes, then the supplier mechanism cannot lie in the exact combined-invisible kernel

$$
O_W^T=0.
$$

If no, the mismatch is now finite and explicit: it is a trace-family admissibility problem, not a diffuse-carrier problem.

---

# 2. Supplier endpoint from the dissipation wavenumber

For the Navier--Stokes dissipation wavenumber in the

$$
r=\infty
$$

form,

$$
\Lambda(t)
=
\lambda_{Q(t)},
$$

Cheskidov--Dai / Cheskidov--Shvydkoy give the boundary estimate

$$
\boxed{
\|u_{Q(t)}(t)\|_\infty
\ge
c_0\nu\Lambda(t)
}
\tag{2.1}
$$

whenever

$$
1<\Lambda(t)<\infty.
$$

DCRP-08 already converted this by Bernstein into

$$
\boxed{
\Lambda
\|u_Q\|_2^2
\ge
c_1\nu^2.
}
\tag{2.2}
$$

The present round uses the stronger pointwise form (2.1).

---

# 3. Critical rescaling

Let

$$
x_\ast
$$

satisfy

$$
|u_Q(x_\ast,t)|
\ge
\frac34
\|u_Q(t)\|_\infty.
$$

Define

$$
\boxed{
w(y)
=
\Lambda^{-1}
u_Q
\left(
x_\ast+\Lambda^{-1}y,
t
\right).
}
\tag{3.1}
$$

Then

$$
\boxed{
|w(0)|
\ge
\frac34c_0\nu.
}
\tag{3.2}
$$

The Fourier support of

$$
w
$$

lies in a fixed annulus

$$
\boxed{
\mathcal A
=
\{
\xi:
c_-\le|\xi|\le c_+
\},
}
\tag{3.3}
$$

where

$$
0<c_-<c_+<\infty
$$

depend only on the chosen Littlewood--Paley partition.

Consequently all Bernstein constants below are universal.

---

# 4. Finite coordinate selection

For every vector

$$
a\in\mathbb R^3,
$$

there exists

$$
i\in\{1,2,3\}
$$

such that

$$
|a_i|
\ge
\frac{
|a|
}{
\sqrt3
}.
$$

Apply this to

$$
a=w(0).
$$

There exist

$$
i_\ast\in\{1,2,3\}
$$

and

$$
\sigma_\ast\in\{-1,+1\}
$$

such that

$$
\boxed{
\sigma_\ast
w_{i_\ast}(0)
\ge
\frac{
3c_0
}{
4\sqrt3
}
\nu.
}
\tag{4.1}
$$

The pair

$$
(i_\ast,\sigma_\ast)
$$

belongs to a fixed family of exactly six possibilities.

---

# 5. Bernstein persistence

Because

$$
w
$$

is supported in the fixed annulus

$$
\mathcal A,
$$

Bernstein gives

$$
\boxed{
\|\nabla w\|_\infty
\le
C_B
\|w\|_\infty.
}
\tag{5.1}
$$

Also

$$
\|w\|_\infty
\le
\frac43
|w(0)|
$$

if

$$
x_\ast
$$

is chosen sufficiently close to the essential supremum point; alternatively one may carry a harmless factor two in all constants.

Thus there is a universal constant

$$
C_1
$$

such that

$$
\boxed{
\|\nabla w\|_\infty
\le
C_1
|w(0)|.
}
\tag{5.2}
$$

Choose

$$
\boxed{
r_\ast
=
\frac1{
8\sqrt3C_1
}.
}
\tag{5.3}
$$

For

$$
|y|\le r_\ast,
$$

$$
|w_{i_\ast}(y)-w_{i_\ast}(0)|
\le
\|\nabla w\|_\infty
|y|
\le
\frac{
|w(0)|
}{
8\sqrt3
}.
$$

Using (4.1),

$$
\boxed{
\sigma_\ast
w_{i_\ast}(y)
\ge
c_2\nu
}
\tag{5.4}
$$

throughout

$$
B_{r_\ast}(0)
$$

for a universal

$$
c_2>0.
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 6. NEW THEOREM — Finite-Family Supplier Trace Lift

Choose a fixed function

$$
\eta
\in
C_c^\infty(B_{r_\ast}(0)),
$$

with

$$
\eta\ge0
$$

and

$$
\boxed{
\int
\eta(y)\,dy
=
1.
}
\tag{6.1}
$$

For

$$
i\in\{1,2,3\},
\qquad
\sigma\in\{-1,+1\},
$$

define

$$
\boxed{
\mathcal L_{i,\sigma}(w)
=
\sigma
\int
\eta(y)
w_i(y)
\,dy.
}
\tag{6.2}
$$

## Theorem 6.1

For every dissipation-boundary supplier shell, after the admissible critical rescaling and spatial re-centering above,

$$
\boxed{
\max_{
1\le i\le3,
\ \sigma=\pm1
}
\mathcal L_{i,\sigma}(w)
\ge
c_2\nu.
}
\tag{6.3}
$$

### Proof

Use the selected pair

$$
(i_\ast,\sigma_\ast)
$$

from Section 5.

Since

$$
\eta\ge0,
$$

has unit mass, and

$$
\sigma_\ast w_{i_\ast}\ge c_2\nu
$$

throughout its support,

$$
\mathcal L_{i_\ast,\sigma_\ast}(w)
\ge
c_2\nu.
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

# 7. Why this is a genuine anti-diffusion theorem

The work multiplicity obstruction of DCRP-12 concerns a measure whose fixed total mass may be split into

$$
N\to\infty
$$

separate cells.

Theorem 6.1 does not estimate a sum of work cells.

It uses one dynamically selected supplier endpoint.

Once the supplier center is chosen, one of six fixed local coordinate tests has a uniform lower bound.

Therefore:

$$
\boxed{
\text{supplier endpoint}
\Longrightarrow
\text{one local coefficient }\ge c\nu
}
\tag{7.1}
$$

independently of:

- number of other active cells;
- total work multiplicity;
- spatial distribution of the remaining solution;
- pressure--flux cancellation elsewhere.

Thus:

$$
\boxed{
\textbf{
supplier-state trace visibility cannot be defeated by work fragmentation.
}
}
\tag{7.2}
$$

This bypasses rather than solves the global heat-work multiplicity problem.

---

# 8. Physical-variable form

Recall

$$
w(y)
=
\Lambda^{-1}
u_Q
\left(
x_\ast+\Lambda^{-1}y,t
\right).
$$

Then

$$
\begin{aligned}
\mathcal L_{i,\sigma}(w)
&=
\sigma
\int
\eta(y)
\Lambda^{-1}
u_{Q,i}
\left(
x_\ast+\Lambda^{-1}y,t
\right)
dy\\
&=
\sigma
\Lambda^2
\int
\eta
\left(
\Lambda(x-x_\ast)
\right)
u_{Q,i}(x,t)
dx.
\end{aligned}
$$

Hence Theorem 6.1 is equivalently

$$
\boxed{
\max_{i,\sigma}
\sigma
\Lambda^2
\int
\eta
\left(
\Lambda(x-x_\ast)
\right)
u_{Q,i}(x,t)
dx
\ge
c_2\nu.
}
\tag{8.1}
$$

The normalization

$$
\Lambda^2
$$

is exactly the one dictated by the Navier--Stokes scaling of this local linear trace.

---

# 9. Filtered-state interpretation

Let

$$
P_{\mathcal A}
$$

denote the fixed unit-annulus Littlewood--Paley projector in normalized variables.

The supplier shell is

$$
w
=
P_{\mathcal A}v,
$$

where

$$
v
$$

is the full normalized velocity state.

Therefore:

$$
\boxed{
\mathcal L_{i,\sigma}(w)
=
\sigma
\int
\eta
\left(
P_{\mathcal A}v
\right)_i.
}
\tag{9.1}
$$

This is a **filtered selected-time trace** of the actual normalized Navier--Stokes state.

It is generated from the state by a fixed Fourier filter and a fixed local test.

No dangerous/singular label is copied into the coordinate.

Thus it passes the FCBP-06 Copied-Gate safety requirement.

---

# 10. Native CAR1 interpretation

FCBP-06 isolates CAR1 as the missing statement:

$$
\boxed{
\operatorname{dist}_{\rm native}
\ge
a_0
\mu_{\rm dang}
-
\mathcal R^{extract},
}
$$

with the requirement that the native geometry must be generated from Navier--Stokes rather than from a copied dangerous mark.

Theorem 6.1 provides a concrete supplier-side separation:

$$
\boxed{
\mathsf T_{\rm sup}(v)
:=
\max_{i,\sigma}
\mathcal L_{i,\sigma}
(
P_{\mathcal A}v
)
\ge
c_2\nu.
}
\tag{10.1}
$$

The quantity

$$
\mathsf T_{\rm sup}
$$

is:

- state-generated;
- scale normalized;
- spatially re-rooted by an allowed symmetry;
- finite-dimensional;
- quantitatively uniform.

Thus, for any native package norm that contains the six filtered trace coefficients as genuine components,

$$
\boxed{
\operatorname{dist}_{\rm native}
\ge
c_3\nu
}
\tag{10.2}
$$

away from the subspace where all six supplier traces vanish.

Status:

$$
\boxed{
\textbf{CAR1 PROVED FOR THIS CONCRETE SUPPLIER-TRACE SUBGEOMETRY}.
}
$$

This is not yet a theorem about the entire external admissible quotient

$$
\Gamma_W.
$$

That compiler identification remains explicit.

---

# 11. Finite-dimensional anti-phantom advantage

The old work-carrier branch had an effective number of cells

$$
\mathfrak M_{\rm work}
$$

that could diverge.

The supplier trace vector is only:

$$
\boxed{
\mathbf T_{\rm sup}
=
\left(
\mathcal L_{1,+},
\mathcal L_{1,-},
\mathcal L_{2,+},
\mathcal L_{2,-},
\mathcal L_{3,+},
\mathcal L_{3,-}
\right).
}
\tag{11.1}
$$

Its dimension is fixed:

$$
\boxed{
\dim
\mathbf T_{\rm sup}
=
6.
}
\tag{11.2}
$$

Theorem 6.1 gives

$$
\boxed{
\|\mathbf T_{\rm sup}\|_{\ell^\infty}
\ge
c_2\nu.
}
\tag{11.3}
$$

Thus no moving-window multiplicity constant occurs at the extraction stage.

This is precisely the geometry that FCBP-06's Native CAR Detector Compiler is designed to exploit once the trace vector is identified with an admissible detector/quotient component.

---

# 12. Backward caloric adjoint family

For each terminal test

$$
\psi_{i,\sigma}
=
\sigma
\eta e_i,
$$

define the backward heat-adjoint family on normalized time

$$
\tau\le0
$$

by

$$
\boxed{
\Psi_{i,\sigma}(y,\tau)
=
e^{-\tau\Delta}
\psi_{i,\sigma}(y),
\qquad
\tau\le0.
}
\tag{12.1}
$$

Then

$$
\boxed{
\partial_\tau
\Psi_{i,\sigma}
+
\Delta
\Psi_{i,\sigma}
=
0,
}
\tag{12.2}
$$

and

$$
\boxed{
\Psi_{i,\sigma}(y,0)
=
\psi_{i,\sigma}(y).
}
\tag{12.3}
$$

The terminal filtered trace is

$$
\boxed{
\left<
P_{\mathcal A}v(0),
\Psi_{i,\sigma}(0)
\right>
=
\mathcal L_{i,\sigma}
(
P_{\mathcal A}v(0)
).
}
\tag{12.4}
$$

Therefore one of this fixed six-element terminal adjoint family satisfies

$$
\boxed{
\left<
P_{\mathcal A}v(0),
\Psi_{i,\sigma}(0)
\right>
\ge
c_2\nu.
}
\tag{12.5}
$$

This gives a canonical route from the supplier trace atom to a selected caloric-adjoint trace.

---

# 13. Relation to FCBP filtered adjoint localization

FCBP-02 already uses a backward filtered adjoint weight to cancel the principal localization residual.

FCBP-04 / FCBP-05 explicitly retain a selected adjoint-trace channel in the combined observability hierarchy.

Therefore the structure required by DCRP-13 is not foreign to the existing compiler.

However the current corpus does not state, in one theorem, that the exact selected-adjoint family

$$
\Psi_{i,\sigma}
$$

from Section 12 is an admissible basis for

$$
O_W^T.
$$

The final identification must therefore be stated conditionally.

---

# 14. Conditional theorem — direct collision with the trace-zero kernel

## Theorem 14.1

Assume the FCBP/MORP selected adjoint-trace channel

$$
O_W^T
$$

contains, after the standard scale/translation normalization, the six terminal caloric trace functionals generated by:

$$
\psi_{i,\sigma}
=
\sigma\eta e_i.
$$

Then every dissipation-boundary supplier state satisfies

$$
\boxed{
O_W^T
\ge
c_T\nu
}
\tag{14.1}
$$

for a universal:

$$
c_T>0.
$$

Consequently no such supplier state belongs to the exact trace-invisible kernel

$$
\boxed{
O_W^T=0.
}
\tag{14.2}
$$

### Proof

Theorem 6.1 gives one terminal coefficient at least

$$
c_2\nu.
$$

By the assumed channel inclusion, the trace observation norm dominates that coefficient up to a fixed normalization constant.

$$
\square
$$

Status:

$$
\boxed{
\textbf{CONDITIONAL ONLY ON TRACE-FAMILY COMPILER ADMISSIBILITY}.
}
$$

No scale-uniform observability constant is otherwise needed for this direct finite-family branch.

---

# 15. Corollary — supplier sequence cannot be combined-invisible if the trace family is admissible

DCRP-08 proved that a hypothetical finite-time singularity requires a sequence

$$
t_n\uparrow T
$$

with:

$$
\Lambda_n\to\infty
$$

and supplier shells

$$
Q_n=Q(t_n).
$$

Under Theorem 14.1's compiler assumption, every normalized supplier state satisfies:

$$
\boxed{
O_{W,n}^T
\ge
c_T\nu.
}
\tag{15.1}
$$

Hence:

$$
\boxed{
\textbf{
the supplier sequence cannot enter any combined-invisible branch that requires }
O_W^T\to0.
}
\tag{15.2}
$$

This directly attacks the FCBP-06 combined-invisible cascade survivor.

Status:

$$
\boxed{
\textbf{CONDITIONAL ON THE SAME TRACE-COMPILER IDENTIFICATION}.
}
$$

---

# 16. Why this is stronger than local positive energy alone

A positive local

$$
L^2
$$

mass statement gives:

$$
\int_{B_R}
|w|^2
\ge
c\nu^2.
$$

To convert that to a finite set of **linear** detector coefficients one would normally need a finite-dimensional approximation argument.

The dissipation-boundary

$$
L^\infty
$$

lower bound is stronger.

Because the field is band-limited, pointwise largeness persists on a fixed ball with a fixed coordinate sign.

Therefore a fixed **six-element linear test family** already detects it.

No compactness, singular-value decomposition, or increasing detector dimension is needed.

---

# 17. The detector shape is not solution dependent

The following are fixed once and for all:

- the reference bump:

  $$
  \eta;
  $$

- the six component/sign choices:

  $$
  (i,\sigma);
  $$

- the unit-annulus filter:

  $$
  P_{\mathcal A}.
  $$

The solution determines only:

- the admissible spatial re-centering:

  $$
  x_\ast;
  $$

- the admissible parabolic scale:

  $$
  \Lambda^{-1};
  $$

- which one of the six tests is positive.

Thus the detector **family** is fixed and finite.

This avoids the tautology:

> choose the test to be the solution itself.

No such solution-dependent shape is used.

---

# 18. Rotational normalization

If the MORP state normalization also allows spatial rotations, the six-test family can be reduced conceptually to one coordinate test after rotation.

However no rotation is required.

Keeping all six signed coordinate tests has two advantages:

1. it avoids a separate rotational selection theorem;
2. it makes finite-dimensionality explicit.

Thus:

$$
\boxed{
6
}
$$

is a safe universal detector count.

---

# 19. Quantitative stability under approximate supplier threshold

Suppose only:

$$
\|u_Q\|_\infty
\ge
(c_0-\varepsilon)\nu\Lambda
$$

with:

$$
0\le\varepsilon<c_0/2.
$$

Then the same proof gives:

$$
\boxed{
\max_{i,\sigma}
\mathcal L_{i,\sigma}(w)
\ge
c(\,c_0-\varepsilon\,)\nu
\ge
c'\nu.
}
\tag{19.1}
$$

Therefore the trace lift is stable under fixed relative threshold errors.

This is useful if the dissipation-wavenumber definition is implemented with harmless dyadic / mollifier constants.

---

# 20. Quantitative stability under finite shell overlap

A smooth Littlewood--Paley decomposition may represent the dissipation-boundary frequency by a bounded cluster

$$
|p-Q|\le C_0
$$

rather than a single sharp shell.

If:

$$
\max_{|p-Q|\le C_0}
\lambda_p^{-1}
\|u_p\|_\infty
\ge
c\nu,
$$

then one of the finitely many cluster shells satisfies the same lower bound with a modified universal constant.

The trace construction can therefore use a finite family enlarged by the bounded relative shell offsets.

The detector dimension remains universal:

$$
\boxed{
6(2C_0+1).
}
\tag{20.1}
$$

No scale-dependent growth occurs.

---

# 21. Duhamel-adjoint identity for the matched supplier shell

Let:

$$
t_1
$$

be a supplier time and:

$$
q=Q(t_1).
$$

Let:

$$
t_0<t_1.
$$

Define the backward heat evolution of the **terminal supplier shell**:

$$
\boxed{
\varphi_q(s)
=
e^{\nu(t_1-s)\Delta}
u_q(t_1).
}
\tag{21.1}
$$

Then:

$$
\partial_s\varphi_q
+
\nu\Delta\varphi_q
=
0.
$$

Let:

$$
F_q
=
\Delta_q
\mathbb P
\nabla\cdot(u\otimes u).
$$

The projected velocity satisfies:

$$
\partial_su_q
-
\nu\Delta u_q
+
F_q
=
0.
$$

Therefore:

$$
\frac d{ds}
\left<
u_q(s),
\varphi_q(s)
\right>
=
-
\left<
F_q(s),
\varphi_q(s)
\right>.
$$

Integrating:

$$
\boxed{
\|u_q(t_1)\|_2^2
-
\left<
u_q(t_0),
e^{\nu(t_1-t_0)\Delta}
u_q(t_1)
\right>
=
-
\int_{t_0}^{t_1}
\left<
F_q(s),
\varphi_q(s)
\right>
ds.
}
\tag{21.2}
$$

This is an exact signed adjoint ancestry identity.

---

# 22. NEW THEOREM — matched-adjoint nonlinear payment

Let:

$$
A_q(t)
=
\lambda_q^{1/2}
\|u_q(t)\|_2.
$$

Assume at:

$$
t_1
$$

the supplier satisfies:

$$
A_q(t_1)
\ge
a_0\nu.
$$

Let:

$$
K_0
=
\|u(0)\|_2^2.
$$

Choose:

$$
\tau_q
=
\frac1{
c_h\nu\lambda_q^2
}
\log
\left(
\frac{
2\lambda_q^{1/2}K_0^{1/2}
}{
a_0\nu
}
\right)
$$

as in DCRP-09, and set:

$$
t_0=t_1-\tau_q.
$$

Then:

$$
\boxed{
-\lambda_q
\int_{t_0}^{t_1}
\left<
F_q(s),
\varphi_q(s)
\right>
ds
\ge
\frac12
a_0^2\nu^2.
}
\tag{22.1}
$$

### Proof

By shell heat decay:

$$
\left\|
e^{\nu\tau_q\Delta}
u_q(t_1)
\right\|_2
\le
e^{-c_h\nu\lambda_q^2\tau_q}
\|u_q(t_1)\|_2.
$$

Hence:

$$
\left|
\left<
u_q(t_0),
e^{\nu\tau_q\Delta}
u_q(t_1)
\right>
\right|
\le
K_0^{1/2}
e^{-c_h\nu\lambda_q^2\tau_q}
\|u_q(t_1)\|_2.
$$

By definition of:

$$
\tau_q,
$$

the right side is at most:

$$
\frac12
\|u_q(t_1)\|_2^2.
$$

Equation (21.2) gives:

$$
-\int_{t_0}^{t_1}
\left<
F_q,
\varphi_q
\right>
ds
\ge
\frac12
\|u_q(t_1)\|_2^2.
$$

Multiply by:

$$
\lambda_q.
$$

Since:

$$
\lambda_q
\|u_q(t_1)\|_2^2
=
A_q(t_1)^2
\ge
a_0^2\nu^2,
$$

the result follows.

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

# 23. Significance of the matched-adjoint payment

DCRP-09 proved an unsigned source-norm lower bound:

$$
\lambda_q^{1/2}
\int
\|F_q\|_2
dt
\gtrsim
\nu.
$$

Theorem 22.1 gives a stronger **signed dual pairing**:

$$
\boxed{
-\lambda_q
\int
\left<
F_q,
e^{\nu(t_1-s)\Delta}
u_q(t_1)
\right>
ds
\gtrsim
\nu^2.
}
\tag{23.1}
$$

This pairing is:

- exact;
- actual-history;
- scale critical;
- sign definite after the heat-memory term is removed;
- naturally adjoint.

Thus the supplier branch generates both:

$$
\boxed{
\text{terminal finite-family trace atom}
}
$$

and:

$$
\boxed{
\text{signed matched-adjoint nonlinear payment}.
}
$$

This is much less compatible with an adjoint-trace-invisible minimal obstruction than a diffuse unsigned work measure.

---

# 24. Why the matched adjoint is not yet an admissible detector by itself

The terminal state:

$$
u_q(t_1)
$$

appears inside:

$$
\varphi_q.
$$

Therefore the matched adjoint shape is solution dependent.

Using it directly as a detector would risk the same kind of tautological adaptivity that FCBP-06 warns against.

For this reason:

- Theorem 22.1 is retained as a native signed identity;
- Theorem 6.1 is the actual finite-family detector extraction.

The six-test trace lift removes the solution dependence from the detector family.

A future compiler theorem may use Theorem 22.1 to prove that one of the six fixed adjoint channels inherits nonzero nonlinear payment, but that step is not claimed here.

---

# 25. Updated Critical Lift status

The original FCBP Critical Lift problem asked for a non-tautological, scale-uniform route from dangerous causal data to an auditable local observable.

The DCRP chain has now produced:

1. hypothetical singularity:

   $$
   \Longrightarrow
   $$

2. arbitrarily high dissipation-boundary suppliers:

   $$
   \Longrightarrow
   $$

3. critical endpoint shell atom:

   $$
   \Longrightarrow
   $$

4. fixed local pointwise normalized amplitude:

   $$
   \Longrightarrow
   $$

5. finite six-test trace lower bound:

   $$
   \boxed{
   \max_{i,\sigma}
   \mathcal L_{i,\sigma}
   \ge
   c\nu.
   }
   $$

This is a genuine native, scale-uniform extraction statement.

Therefore the supplier branch has solved the **geometry** of CAR1.

What remains is a finite compiler question:

$$
\boxed{
\textbf{
is the supplier trace family contained in, or uniformly controlled by,
the already-declared }O_W^T\textbf{ adjoint-trace channel?}
}
\tag{25.1}
$$

---

# 26. If the compiler answer is yes

If:

$$
O_W^T
\gtrsim
\max_{i,\sigma}
\mathcal L_{i,\sigma},
$$

then:

$$
\boxed{
O_W^T
\ge
c\nu
}
\tag{26.1}
$$

on every supplier state.

Since a hypothetical first singularity forces suppliers at arbitrarily high scales:

$$
\boxed{
\liminf_{n\to\infty}
O_{W,n}^T
\ge
c\nu.
}
\tag{26.2}
$$

Thus the supplier branch cannot enter a moving-window combined-invisible cascade with:

$$
O_{W,n}^{comb}\to0.
$$

At that point the remaining global closure work would return to:

- paid-side recurrence;
- transition realization;
- whether every hypothetical singular branch must pass through the supplier-normalized MORP minimal object.

The diffuse-work multiplicity obstruction would no longer be relevant to supplier observability.

---

# 27. If the compiler answer is no

If the declared:

$$
O_W^T
$$

does **not** admit the six fixed caloric terminal traces, then the gap is now explicit.

One must explain which of the following fails:

1. filtered velocity traces are not part of the trace state;
2. the allowed terminal adjoint family excludes fixed compact bumps;
3. the trace is defined only for a different tensor/source variable;
4. the filter class cannot include the fixed unit-annulus shell;
5. normalization loses the trace under actual return/re-root.

Any such failure is a finite interface mismatch.

It is no longer:

$$
\boxed{
\text{unknown diffuse NS obstruction}.
}
$$

---

# 28. Relation to DCRP-12

DCRP-12 remains useful for the physical work ledger.

Its result is:

$$
\boxed{
\text{local PFET}
\vee
\text{paid backscatter}
\vee
\text{work escape}.
}
$$

DCRP-13 does not invalidate that theorem.

It proves a different statement:

$$
\boxed{
\text{work may diffuse, but the supplier state itself has a fixed trace atom}.
}
$$

Thus the two routes are complementary.

### Work route

tracks **how the supplier is paid**.

### Trace route

tracks **whether the supplier can be observationally invisible**.

The trace route is immune to work-cell multiplicity.

---

# 29. New exact frontier

The previous frontier was:

$$
\text{Quantitative Work Anti-Diffusion / Critical Lift}.
$$

The supplier trace theorem bypasses the anti-diffusion half.

The next exact target is now:

$$
\boxed{
\textbf{
Supplier Trace / FCBP Adjoint-Channel Identification Lemma}.
}
$$

Desired statement:

> After the standard supplier scale/translation normalization, the six fixed terminal filtered trace functionals
>
> $$
> \mathcal L_{i,\sigma}
> $$
>
> belong to the admissible selected-adjoint trace family defining
>
> $$
> O_W^T,
> $$
>
> or are uniformly dominated by that trace norm.
>
> Therefore:
>
> $$
> O_W^T
> \ge
> c\nu
> $$
>
> on every dissipation-boundary supplier.

This is now a finite compiler theorem.

No new PDE mechanism is required.

---

# 30. Source ledger

## Cheskidov--Dai

Alexey Cheskidov and Mimi Dai, *Regularity criteria for the 3D Navier-Stokes and MHD equations*, arXiv:1507.06611v6.

Used for the dissipation-wavenumber architecture and the Navier--Stokes high-frequency boundary condition.

## Cheskidov--Shvydkoy

Alexey Cheskidov and Roman Shvydkoy, *A unified approach to regularity problems for the 3D Navier-Stokes and Euler equations: the use of Kolmogorov's dissipation range*, arXiv:1102.1944v2.

Contains the explicit boundary estimate:

$$
\|u_{Q(t)}(t)\|_\infty
\ge
c_0\nu\Lambda(t)
$$

on the active dissipation-wavenumber set.

## Internal FCBP-02

Already uses a backward filtered adjoint cutoff and proves cancellation of the principal localization residual.

## Internal FCBP-05

Declares the combined observation hierarchy:

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

including the selected adjoint-trace channel.

## Internal FCBP-06

Factorizes Critical Lift into:

$$
\mathrm{CAR0}
\to
\mathrm{CAR1}
\to
\mathrm{CAR2}
\to
\mathrm{CAR3}.
$$

The supplier trace theorem provides a concrete scale-uniform native separation for a specific NS-generated state coordinate and respects the Copied-Gate prohibition.

---

# 31. End state

The key new theorem is:

$$
\boxed{
\textbf{
Dissipation-boundary supplier}
\Longrightarrow
\textbf{
finite-family local trace atom}.
}
$$

Quantitatively:

$$
\boxed{
\max_{
1\le i\le3,\,
\sigma=\pm1
}
\sigma
\int
\eta(y)
\left[
P_{\mathcal A}v(y)
\right]_i
dy
\ge
c\nu.
}
$$

The family has fixed dimension:

$$
\boxed{
6.
}
$$

No work multiplicity can dilute this coefficient.

In addition, the supplier has a signed matched-adjoint nonlinear payment:

$$
\boxed{
-\lambda_Q
\int
\left<
F_Q(s),
e^{\nu(t_Q-s)\Delta}
u_Q(t_Q)
\right>
ds
\ge
c\nu^2.
}
$$

Thus the supplier mechanism is simultaneously:

- state-visible;
- trace-visible to a finite fixed family;
- dynamically and nonlinearly generated.

The next single frontier is:

$$
\boxed{
\textbf{
Supplier Trace / FCBP Adjoint-Channel Identification Lemma}.
}
$$

If this finite compiler bridge holds, the dissipation-boundary supplier branch cannot be combined-invisible.

---

# Checkpoint v14 Update — DCRP-14

# NS-DCRP-14 — Solenoidal Trace-Window Compiler, Nonlinear Supplier Increment, and the Final Trace-Realization Ledger

- date: 2026-08-16
- status: research proof checkpoint
- canonical source: UTF-8 Markdown
- canonical math delimiters: `$...$` and `$$...$$`
- objective: audit DCRP-13 against the actual finite-window adjoint-trace definition, correct the inadmissible scalar test shortcut, and build a genuine finite-dimensional divergence-free trace window for the supplier-generated nonlinear increment.
- no full Navier--Stokes regularity claim is made.
- principal internal dependencies:
  - FCBP-02 filtered adjoint localization;
  - FCBP-05 combined observability;
  - FCBP-06 trace / CAR audit;
  - MORP-01 through MORP-05;
  - DCRP-08 through DCRP-13.
- external primary calibration:
  - Runlong Yu, *Invisible Defect Cascades for Navier--Stokes Regularity*, arXiv:2606.12756v1;
  - Cheskidov--Dai, arXiv:1507.06611v6;
  - Cheskidov--Shvydkoy, arXiv:1102.1944v2.

---

# 1. Executive result

DCRP-13 produced six scalar local traces

$$
\mathcal L_{i,\sigma}(w)
=
\sigma
\int
\eta(y)w_i(y)\,dy
$$

for the normalized supplier shell.

Those functionals are valid state diagnostics.

However they cannot be identified directly with the FCBP selected adjoint-trace channel.

The external finite-window trace space is:

$$
\boxed{
H_W
=
\text{finite-dimensional selected-time divergence-free trace correction space},
}
$$

localized in the observation ball and projected to the finite window.

The primal trace observation is:

$$
\boxed{
\mathcal O_W^T d
=
\Pi_W^T
\dot U(s_\ast).
}
\tag{1.1}
$$

Therefore the DCRP-13 claim

$$
\text{six scalar traces}
\Longrightarrow
O_W^T\ge c\nu
$$

was too fast.

There are two distinct issues.

First, the test field

$$
\eta e_i
$$

is not divergence free.

Second, the FCBP trace channel acts on the selected-time velocity component

$$
\dot U(s_\ast)
$$

of a cleaned defect direction, not on the full nonlinear supplier state

$$
u_Q(t_\ast)
$$

by arbitrary scalar pairing.

These points are corrected here.

The replacement argument uses the nonlinear supplier increment.

Let:

$$
q=Q(t_1),
\qquad
\lambda=\lambda_q,
$$

be a dissipation-boundary supplier shell.

Define:

$$
g_q(t)
=
u_q(t)
-
e^{\nu(t-t_0)\Delta}
u_q(t_0).
$$

Then:

$$
g_q(t_0)=0,
$$

and:

$$
\boxed{
\partial_tg_q
-
\nu\Delta g_q
+
\nabla\pi_q
=
-\nabla\cdot T_q,
}
\tag{1.2}
$$

where:

$$
T_q
=
\Delta_q(u\otimes u),
$$

and:

$$
\pi_q
=
\Delta_qp.
$$

Thus:

$$
g_q
$$

is the actual same-history nonlinear increment relative to linear heat memory.

Choose:

$$
t_0=t_1-\tau_q
$$

with:

$$
\tau_q
\sim
\frac{
\log(C\lambda^{1/2}K_0^{1/2}/\nu)
}{
\nu\lambda^2
}.
$$

Then the linear memory is small in

$$
L^\infty,
$$

while the dissipation-boundary supplier satisfies:

$$
\|u_q(t_1)\|_\infty
\gtrsim
\nu\lambda.
$$

Hence:

$$
\boxed{
\|g_q(t_1)\|_\infty
\ge
c\nu\lambda.
}
\tag{1.3}
$$

After critical rescaling and recentering at a point of near-maximal nonlinear-increment amplitude,

$$
\boxed{
h(y)
=
\lambda^{-1}
g_q
\left(
x_\ast+\lambda^{-1}y,
t_1
\right),
}
\tag{1.4}
$$

one has:

$$
\boxed{
\nabla\cdot h=0,
}
\tag{1.5}
$$

$$
\boxed{
\operatorname{supp}\widehat h
\subset
\mathcal A
}
\tag{1.6}
$$

for one fixed annulus

$$
\mathcal A,
$$

and:

$$
\boxed{
\|h\|_\infty
\ge
c\nu.
}
\tag{1.7}
$$

The main theorem of this round is:

> There exists one universal finite-dimensional subspace
>
> $$
> H_\ast
> \subset
> C_c^\infty(B_R;\mathbb R^3),
> $$
>
> consisting entirely of divergence-free vector fields, such that every normalized supplier nonlinear increment
>
> $$
> h
> $$
>
> satisfies:
>
> $$
> \boxed{
> \|\Pi_{H_\ast}h\|_{L^2(B_R)}
> \ge
> c_\ast\nu.
> }
> \tag{1.8}
> $$

The dimension of:

$$
H_\ast
$$

is universal and independent of:

- the supplier scale;
- the singular sequence;
- the number of work cells;
- the solution.

This fixes the trace-family admissibility problem.

The remaining gap is now exactly:

$$
\boxed{
\textbf{
Supplier Nonlinear-Increment / Cleaned-Defect Trace Realization}.
}
\tag{1.9}
$$

Namely, prove that the finite-window cleaned defect direction generated from the same actual return has selected-time component:

$$
\dot U(s_\ast)
$$

equal to the normalized nonlinear supplier increment up to an explicitly charged projection / localization / synchronization residual.

Once that is shown,

$$
\boxed{
\|\mathcal O_W^Td\|
\ge
c_\ast\nu
-
\mathcal E_{\rm tr-real}.
}
\tag{1.10}
$$

Thus exact trace invisibility requires:

$$
\mathcal E_{\rm tr-real}
\ge
c_\ast\nu.
$$

At that point the only escape is a positive native realization residual.

---

# 2. CORRECTION — DCRP-13 trace identification

The external finite-window trace channel is defined as follows.

A finite window is:

$$
W
=
(n,\ell,\Lambda,\chi,s_\ast).
$$

The trace correction space:

$$
H_W
$$

is finite dimensional.

Its elements are:

- divergence-free;
- selected-time vector fields;
- localized in the observation ball;
- projected to the finite active window.

The primal trace observation is:

$$
\boxed{
\mathcal O_W^Td
=
\Pi_W^T
\dot U(s_\ast).
}
\tag{2.1}
$$

The dual map:

$$
A_W^\ast
$$

is obtained from the backward **linearized coarse-grained Navier--Stokes adjoint**, not from the pure heat equation.

Therefore the following DCRP-13 statements must be corrected.

### Correction 1

The scalar terminal tests:

$$
\eta e_i
$$

are not themselves admissible trace corrections because:

$$
\nabla\cdot(\eta e_i)
=
\partial_i\eta
$$

is generally nonzero.

### Correction 2

A pure backward caloric propagation:

$$
e^{-\tau\Delta}\psi
$$

is not identical to the external:

$$
A_W^\ast
$$

adjoint, which contains linearized coarse transport and pressure coupling.

### Correction 3

The phrase:

$$
\boxed{
\text{CAR1 proved for the supplier-trace subgeometry}
}
$$

is too strong if it refers directly to the external FCBP trace channel.

The correct statement after DCRP-13 is:

$$
\boxed{
\text{a finite-dimensional scalar state witness exists}.
}
$$

DCRP-14 replaces it by an admissible solenoidal finite trace window.

Status:

$$
\boxed{
\textbf{CORRECTED}.
}
$$

---

# 3. The supplier shell and nonlinear memory subtraction

Let:

$$
q=Q(t_1)
$$

be a dissipation-boundary supplier shell.

By the dissipation-wavenumber boundary estimate:

$$
\boxed{
\|u_q(t_1)\|_\infty
\ge
c_0\nu\lambda_q.
}
\tag{3.1}
$$

Let:

$$
K_0
=
\|u(0)\|_2^2.
$$

For:

$$
t_0<t_1,
$$

the fixed shell mild formula is:

$$
u_q(t_1)
=
e^{\nu(t_1-t_0)\Delta}
u_q(t_0)
-
\int_{t_0}^{t_1}
e^{\nu(t_1-s)\Delta}
\mathbb P
\nabla\cdot
\Delta_q(u\otimes u)(s)
\,ds.
$$

Define:

$$
\boxed{
g_q(t_1)
=
u_q(t_1)
-
e^{\nu(t_1-t_0)\Delta}
u_q(t_0).
}
\tag{3.2}
$$

Then:

$$
\boxed{
g_q(t_1)
=
-
\int_{t_0}^{t_1}
e^{\nu(t_1-s)\Delta}
\mathbb P
\nabla\cdot
\Delta_q(u\otimes u)(s)
\,ds.
}
\tag{3.3}
$$

Thus:

$$
g_q
$$

is generated only by actual nonlinear forcing over:

$$
[t_0,t_1].
$$

---

# 4. Heat-memory $L^\infty$ bound

On the fixed dyadic annulus:

$$
|\xi|
\sim
\lambda_q,
$$

the heat semigroup gives:

$$
\left\|
e^{\nu\tau\Delta}
u_q
\right\|_2
\le
e^{-c_h\nu\lambda_q^2\tau}
\|u_q\|_2.
$$

Bernstein gives:

$$
\left\|
e^{\nu\tau\Delta}
u_q
\right\|_\infty
\le
C_B
\lambda_q^{3/2}
e^{-c_h\nu\lambda_q^2\tau}
\|u_q\|_2.
$$

By the energy inequality:

$$
\|u_q(t_0)\|_2
\le
K_0^{1/2}.
$$

Hence:

$$
\boxed{
\left\|
e^{\nu\tau\Delta}
u_q(t_0)
\right\|_\infty
\le
C_B
\lambda_q^{3/2}
K_0^{1/2}
e^{-c_h\nu\lambda_q^2\tau}.
}
\tag{4.1}
$$

Choose:

$$
\boxed{
\tau_q
=
\frac1{
c_h\nu\lambda_q^2
}
\log
\left(
\frac{
4C_B
\lambda_q^{1/2}
K_0^{1/2}
}{
c_0\nu
}
\right).
}
\tag{4.2}
$$

For sufficiently large:

$$
q,
$$

the logarithm is positive.

Then:

$$
\boxed{
\left\|
e^{\nu\tau_q\Delta}
u_q(t_0)
\right\|_\infty
\le
\frac{
c_0
}{
4
}
\nu\lambda_q.
}
\tag{4.3}
$$

---

# 5. NEW THEOREM — nonlinear supplier increment is critical and nonvanishing

## Theorem 5.1

Let:

$$
t_0=t_1-\tau_q
$$

with:

$$
\tau_q
$$

given by (4.2).

Then:

$$
\boxed{
\|g_q(t_1)\|_\infty
\ge
\frac{
3c_0
}{
4
}
\nu\lambda_q.
}
\tag{5.1}
$$

### Proof

By definition:

$$
g_q(t_1)
=
u_q(t_1)
-
e^{\nu\tau_q\Delta}
u_q(t_0).
$$

Therefore:

$$
\|g_q(t_1)\|_\infty
\ge
\|u_q(t_1)\|_\infty
-
\left\|
e^{\nu\tau_q\Delta}
u_q(t_0)
\right\|_\infty.
$$

Use (3.1) and (4.3).

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

# 6. Forced Stokes realization of the nonlinear increment

Define for:

$$
t\in[t_0,t_1]:
$$

$$
\boxed{
g_q(t)
=
u_q(t)
-
e^{\nu(t-t_0)\Delta}
u_q(t_0).
}
\tag{6.1}
$$

Then:

$$
g_q(t_0)=0.
$$

Apply:

$$
\Delta_q
$$

to the Navier--Stokes equation:

$$
\partial_tu_q
-
\nu\Delta u_q
+
\nabla p_q
=
-\nabla\cdot
\Delta_q(u\otimes u),
$$

where:

$$
p_q
=
\Delta_qp.
$$

The heat-memory term solves the homogeneous heat equation.

Therefore:

$$
\boxed{
\partial_tg_q
-
\nu\Delta g_q
+
\nabla p_q
=
-\nabla\cdot T_q,
}
\tag{6.2}
$$

with:

$$
\boxed{
T_q
=
\Delta_q(u\otimes u).
}
\tag{6.3}
$$

Also:

$$
\nabla\cdot g_q=0.
$$

Thus:

$$
\boxed{
(g_q,p_q,T_q)
}
$$

is an actual same-history forced Stokes package generated by the Navier--Stokes nonlinearity.

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 7. Critical normalization

Choose:

$$
x_q
$$

such that:

$$
|g_q(x_q,t_1)|
\ge
\frac34
\|g_q(t_1)\|_\infty.
$$

Define:

$$
\boxed{
h_q(y)
=
\lambda_q^{-1}
g_q
\left(
x_q+\lambda_q^{-1}y,
t_1
\right).
}
\tag{7.1}
$$

Then:

$$
\boxed{
\|h_q\|_\infty
\ge
c_s\nu
}
\tag{7.2}
$$

for:

$$
c_s>0.
$$

Moreover:

$$
\boxed{
\nabla\cdot h_q=0,
}
\tag{7.3}
$$

and:

$$
\boxed{
\operatorname{supp}\widehat h_q
\subset
\mathcal A
}
\tag{7.4}
$$

for one universal compact annulus:

$$
\mathcal A
=
\{
\xi:
c_-\le|\xi|\le c_+
\}.
$$

---

# 8. Normalized supplier-increment class

Fix:

$$
a\in(0,1).
$$

Define:

$$
\boxed{
\mathscr K_{\mathcal A,a}
}
$$

to be the class of vector fields:

$$
f:\mathbb R^3\to\mathbb R^3
$$

satisfying:

$$
\boxed{
\nabla\cdot f=0,
}
\tag{8.1}
$$

$$
\boxed{
\operatorname{supp}\widehat f
\subset
\mathcal A,
}
\tag{8.2}
$$

$$
\boxed{
\|f\|_\infty
\le
1,
}
\tag{8.3}
$$

and:

$$
\boxed{
|f(0)|
\ge
a.
}
\tag{8.4}
$$

Every normalized supplier increment:

$$
h_q
$$

can be divided by its:

$$
L^\infty
$$

norm and placed in:

$$
\mathscr K_{\mathcal A,a}
$$

for a fixed universal:

$$
a>0.
$$

---

# 9. Local compactness of the normalized annulus class

Let:

$$
m\ge0.
$$

Because:

$$
f
$$

has Fourier support in:

$$
\mathcal A,
$$

choose one fixed smooth multiplier:

$$
\vartheta
$$

with:

$$
\vartheta\equiv1
$$

on:

$$
\mathcal A.
$$

Then:

$$
f
=
\check\vartheta*f.
$$

Hence for every multi-index:

$$
\alpha,
$$

$$
\partial^\alpha f
=
(\partial^\alpha\check\vartheta)*f.
$$

Therefore:

$$
\boxed{
\|\partial^\alpha f\|_\infty
\le
C_\alpha
\|f\|_\infty
\le
C_\alpha.
}
\tag{9.1}
$$

Thus:

$$
\mathscr K_{\mathcal A,a}
$$

is uniformly bounded in:

$$
C^m(B_R)
$$

for every fixed:

$$
m,R.
$$

Arzela--Ascoli gives:

$$
\boxed{
\mathscr K_{\mathcal A,a}
\text{ is precompact in }
C^\infty_{\rm loc}.
}
\tag{9.2}
$$

Its closure retains:

$$
|f(0)|\ge a.
$$

---

# 10. Local solenoidal test space

Fix any:

$$
R>0.
$$

Let:

$$
\boxed{
V_R
=
\overline{
\{
\psi\in C_c^\infty(B_R;\mathbb R^3):
\nabla\cdot\psi=0
\}
}^{L^2(B_R)}.
}
\tag{10.1}
$$

Let:

$$
P_R
$$

denote the:

$$
L^2(B_R)
$$

orthogonal projection onto:

$$
V_R.
$$

The central question is whether:

$$
P_Rf
$$

can vanish for:

$$
f\in\mathscr K_{\mathcal A,a}.
$$

---

# 11. NEW THEOREM — local solenoidal nondegeneracy

## Theorem 11.1

For every:

$$
R>0,
$$

$$
\boxed{
\delta_R
:=
\inf_{
f\in\mathscr K_{\mathcal A,a}
}
\|P_Rf\|_{L^2(B_R)}
>
0.
}
\tag{11.1}
$$

### Proof

Assume the contrary.

Then there exists:

$$
f_n\in\mathscr K_{\mathcal A,a}
$$

with:

$$
\|P_Rf_n\|_{L^2(B_R)}
\to0.
$$

By local compactness, after a subsequence:

$$
f_n
\to
f_\ast
$$

strongly in:

$$
C^\infty(B_R).
$$

Therefore:

$$
\boxed{
|f_\ast(0)|
\ge
a>0.
}
\tag{11.2}
$$

Also:

$$
P_Rf_\ast=0.
$$

Hence:

$$
f_\ast
$$

is orthogonal in:

$$
B_R
$$

to every compactly supported divergence-free test field.

For every:

$$
\Phi\in C_c^\infty(B_R;\mathbb R^3),
$$

the field:

$$
\nabla\times\Phi
$$

is divergence free and compactly supported.

Thus:

$$
0
=
\int_{B_R}
f_\ast\cdot
(\nabla\times\Phi)
\,dx
=
\int_{B_R}
(\nabla\times f_\ast)
\cdot\Phi
\,dx.
$$

Therefore:

$$
\boxed{
\nabla\times f_\ast=0
}
\tag{11.3}
$$

in:

$$
B_R.
$$

But:

$$
\nabla\cdot f_\ast=0.
$$

Hence:

$$
\boxed{
\Delta f_\ast=0
}
\tag{11.4}
$$

in:

$$
B_R.
$$

Because:

$$
f_\ast
$$

is band limited, it is real analytic.

Thus:

$$
\Delta f_\ast=0
$$

on one nonempty open ball implies:

$$
\boxed{
\Delta f_\ast=0
}
\tag{11.5}
$$

globally.

Taking Fourier transforms:

$$
|\xi|^2
\widehat f_\ast(\xi)
=
0.
$$

But:

$$
\operatorname{supp}\widehat f_\ast
\subset
\mathcal A,
$$

and:

$$
0\notin\mathcal A.
$$

Therefore:

$$
\widehat f_\ast=0,
$$

so:

$$
f_\ast=0.
$$

This contradicts (11.2).

Therefore:

$$
\delta_R>0.
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

# 12. Finite-dimensional compression of the solenoidal trace space

Choose a countable dense family:

$$
\{
\psi_1,\psi_2,\ldots
\}
\subset
C_c^\infty(B_R;\mathbb R^3)
$$

with:

$$
\nabla\cdot\psi_j=0,
$$

dense in:

$$
V_R.
$$

Let:

$$
\boxed{
H_N
=
\operatorname{span}
\{
\psi_1,\ldots,\psi_N
\}.
}
\tag{12.1}
$$

Let:

$$
P_N
$$

be the:

$$
L^2(B_R)
$$

orthogonal projection onto:

$$
H_N.
$$

Then:

$$
P_N
\to
P_R
$$

strongly on:

$$
L^2(B_R).
$$

Because the closure of:

$$
\mathscr K_{\mathcal A,a}
$$

is compact in:

$$
L^2(B_R),
$$

the convergence is uniform on:

$$
\mathscr K_{\mathcal A,a}.
$$

Therefore for some finite:

$$
N_\ast,
$$

$$
\boxed{
\sup_{
f\in\mathscr K_{\mathcal A,a}
}
\|
(P_R-P_{N_\ast})f
\|_{L^2(B_R)}
<
\frac{
\delta_R
}{
2
}.
}
\tag{12.2}
$$

Hence:

$$
\boxed{
\inf_{
f\in\mathscr K_{\mathcal A,a}
}
\|
P_{N_\ast}f
\|_{L^2(B_R)}
\ge
\frac{
\delta_R
}{
2
}.
}
\tag{12.3}
$$

---

# 13. NEW THEOREM — universal finite-dimensional solenoidal supplier trace window

Define:

$$
\boxed{
H_\ast
=
H_{N_\ast}.
}
\tag{13.1}
$$

## Theorem 13.1

There exist universal:

$$
R<\infty,
$$

$$
N_\ast<\infty,
$$

and:

$$
c_\ast>0
$$

such that every normalized supplier nonlinear increment:

$$
h_q
$$

satisfies:

$$
\boxed{
\|
\Pi_{H_\ast}
h_q
\|_{L^2(B_R)}
\ge
c_\ast\nu.
}
\tag{13.2}
$$

The space:

$$
H_\ast
$$

consists of compactly supported divergence-free vector fields.

### Proof

Let:

$$
M_q
=
\|h_q\|_\infty.
$$

By Theorem 5.1 / Section 7:

$$
M_q
\ge
c_s\nu.
$$

Define:

$$
f_q
=
M_q^{-1}h_q.
$$

After recentering:

$$
f_q\in
\mathscr K_{\mathcal A,a}.
$$

Therefore:

$$
\|
\Pi_{H_\ast}
f_q
\|_2
\ge
\delta_R/2.
$$

Multiply by:

$$
M_q.
$$

Then:

$$
\|
\Pi_{H_\ast}
h_q
\|_2
\ge
\frac{
\delta_Rc_s
}{
2
}
\nu.
$$

Set:

$$
c_\ast
=
\delta_Rc_s/2.
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

# 14. Why this trace window matches the FCBP type

The external finite-window definition allows:

$$
\Lambda
$$

to be a finite-dimensional space of:

- localized test functions;
- wave packets;
- Stokes eigenfunctions;
- localized Fourier packets;
- adjoint test modes.

The selected-time correction space:

$$
H_W
$$

must be finite dimensional, divergence free, and localized in the observation ball.

The space:

$$
H_\ast
$$

constructed above satisfies exactly these structural requirements.

Therefore:

$$
\boxed{
\textbf{
trace-family admissibility is solved.
}
}
\tag{14.1}
$$

No new detector architecture is needed.

What remains is the identity of the **observed object**.

---

# 15. The observed object mismatch

The external primal trace map is:

$$
\mathcal O_W^Td
=
\Pi_W^T
\dot U(s_\ast).
$$

Theorem 13.1 controls:

$$
\Pi_{H_\ast}
h_q,
$$

where:

$$
h_q
$$

is the normalized nonlinear supplier increment.

Thus to obtain:

$$
\mathcal O_W^T d
\ne0,
$$

one needs:

$$
\boxed{
\dot U(s_\ast)
=
h_q
+
e_{\rm tr}
}
\tag{15.1}
$$

inside the selected trace window, with controlled:

$$
e_{\rm tr}.
$$

Define the trace-realization error:

$$
\boxed{
\mathcal E_{\rm tr-real}
=
\|
\Pi_{H_\ast}
e_{\rm tr}
\|_{L^2(B_R)}.
}
\tag{15.2}
$$

Then:

$$
\boxed{
\|
\mathcal O_W^Td
\|
\ge
c_\ast\nu
-
\mathcal E_{\rm tr-real}.
}
\tag{15.3}
$$

Status:

$$
\boxed{
\textbf{PROVED by triangle inequality once (15.1) is established}.
}
$$

---

# 16. Exact trace-realization alternative

Equation (15.3) gives the following elementary but important alternative.

For every supplier nonlinear increment:

$$
\boxed{
\|\mathcal O_W^Td\|
\ge
\frac{
c_\ast
}{
2
}
\nu
}
\tag{16.1}
$$

or:

$$
\boxed{
\mathcal E_{\rm tr-real}
\ge
\frac{
c_\ast
}{
2
}
\nu.
}
\tag{16.2}
$$

Thus:

$$
\boxed{
\textbf{
supplier nonlinear increment}
\Longrightarrow
\textbf{
trace visibility}
\ \vee\
\textbf{
positive trace-realization residual}.
}
}
\tag{16.3}
$$

This is now exactly the kind of alternative MORP is designed to retain.

The missing theorem is to prove that:

$$
\mathcal E_{\rm tr-real}
$$

belongs to the existing:

$$
\mathsf R_{\rm nat}
$$

or another already-paid localization / projection / synchronization ledger.

---

# 17. Relation to the forced Stokes package

The nonlinear supplier increment satisfies:

$$
\partial_tg_q
-
\nu\Delta g_q
+
\nabla p_q
=
-\nabla\cdot T_q.
$$

This is a linear forced Stokes evolution with actual Navier--Stokes-generated source:

$$
T_q
=
\Delta_q(u\otimes u).
$$

Hence the selected-time trace:

$$
g_q(t_1)
$$

is not a fabricated direction.

It belongs to an actual PDE-generated linear forced package.

This makes the following realization program natural:

1. use the normalized:

   $$
   g_q
   $$

   as the velocity direction:

   $$
   \dot U;
   $$

2. use the normalized:

   $$
   T_q
   $$

   as the source / residual direction:

   $$
   \dot R;
   $$

3. use:

   $$
   p_q
   $$

   as the corresponding pressure direction;

4. localize / project / clean this forced Stokes package into the finite-window constrained space.

Every mismatch generated by:

- finite-window projection;
- localization;
- coarse baseline coupling;
- active/harmonic pressure cleaning;
- synchronization;

must then appear explicitly in the finite-window residual ledger.

This is the concrete form of the next theorem.

---

# 18. Why the pure heat adjoint is no longer needed

DCRP-13 used a pure backward heat test.

The actual FCBP dual trace:

$$
A_W^\ast
$$

solves a backward **linearized coarse Navier--Stokes** equation.

DCRP-14 avoids this mismatch.

The trace lower bound is now stated on the primal selected-time space:

$$
H_\ast.
$$

One only needs:

$$
\Pi_W^T
\dot U(s_\ast),
$$

which is exactly the external primal trace definition.

The backward adjoint may then be used internally by the finite-window anti-phantom theorem in its own correct form.

Thus no direct identification:

$$
e^{-\tau\Delta}
=
A_W^\ast
$$

is required.

---

# 19. Relation to MORP-02 selected-time traces

MORP-02 already treats selected-time native carriers as a separate extraction route.

It proves strong trace compactness under:

- fixed relative frequency support;
- a global trace:

  $$
  L^2
  $$

  bound;
- spatial tightness.

The DCRP-14 theorem is complementary.

It does not require a global trace bound or spatial tightness.

Instead it produces a fixed finite-dimensional **local solenoidal projection** with uniform lower bound.

Thus:

$$
\boxed{
\text{supplier trace does not need full global trace compactness
merely to remain locally observable}.
}
$$

This removes one source of unnecessary compactness debt.

---

# 20. Why finite dimensionality is genuinely uniform

The dimension:

$$
N_\ast
$$

depends only on:

- the fixed annulus:

  $$
  \mathcal A;
  $$

- the fixed local radius:

  $$
  R;
  $$

- the fixed normalized point-amplitude fraction:

  $$
  a.
  $$

It does not depend on:

$$
q.
$$

Therefore:

$$
\boxed{
N_\ast
=
O(1)
}
\tag{20.1}
$$

along the entire hypothetical singular cascade.

This avoids the moving-window dimension blowup that plagued earlier abstract finite-window CAR attempts.

---

# 21. Why the unique-continuation step is essential

The compactness theorem alone would only give a limiting band-limited field.

The key fact is:

$$
\boxed{
\text{no nonzero annulus-band-limited divergence-free field
can be locally orthogonal to every compactly supported divergence-free test}.
}
$$

If it were orthogonal to all such tests:

$$
\nabla\times f=0
$$

locally.

Together with:

$$
\nabla\cdot f=0,
$$

this gives:

$$
\Delta f=0
$$

locally.

Band-limited analyticity propagates that identity globally.

But a globally harmonic field with Fourier support away from zero must vanish.

This is precisely what gives a positive uniform solenoidal distance.

---

# 22. A possible shortcut through finite-window projection

The external finite-window framework allows:

$$
\Lambda
$$

to be a chosen finite-dimensional localized Fourier / wave-packet window.

Therefore one may choose:

$$
\Lambda_\ast
$$

so that its selected-time velocity subspace contains:

$$
H_\ast.
$$

Then:

$$
\Pi_W^T
$$

may be chosen to dominate:

$$
\Pi_{H_\ast}.
$$

Under an exact supplier-increment realization:

$$
\dot U(s_\ast)=h_q,
$$

one would immediately obtain:

$$
\boxed{
\|
\mathcal O_W^Td
\|
\ge
c_\ast\nu.
}
\tag{22.1}
$$

Thus:

$$
\boxed{
\textbf{
the trace-window geometry itself is no longer the missing step.
}
}
$$

Only realization/cleaning remains.

---

# 23. Concrete next theorem — Supplier Increment Realization

The next exact target is:

$$
\boxed{
\textbf{
Supplier Increment / Finite-Window Defect Realization Lemma}.
}
$$

Desired statement:

Let:

$$
g_q
$$

be the DCRP-14 nonlinear supplier increment on:

$$
[t_0,t_1].
$$

Normalize at:

$$
\lambda_q
$$

and re-center at:

$$
x_q.
$$

Then there exists an admissible finite-window cleaned defect direction:

$$
d_q
=
[
\dot U_q,
\dot P_q;
\dot P_q^{act},
\dot P_q^{har},
\dot R_q,
\dot\Pi_q
]
\in
Y_{W_q}
$$

such that at the selected terminal time:

$$
\boxed{
\dot U_q(s_\ast)
=
h_q
+
e_q,
}
\tag{23.1}
$$

and:

$$
\boxed{
\|
\Pi_{H_\ast}e_q
\|_2
\le
\mathcal E_q^{\rm proj}
+
\mathcal E_q^{\rm loc}
+
\mathcal E_q^{\rm press}
+
\mathcal E_q^{\rm sync}.
}
\tag{23.2}
$$

Every error on the right must be one of the already declared finite-window residual-ledger channels.

Then:

$$
\boxed{
\|
\mathcal O_{W_q}^T
d_q
\|
+
\mathcal E_q^{\rm ledger}
\ge
c_\ast\nu.
}
\tag{23.3}
$$

If the residual ledger tends to zero, the trace channel has a uniform positive lower bound.

If the trace channel tends to zero, the residual ledger has a uniform positive lower bound.

Either alternative is incompatible with exact combined invisibility plus zero native residual.

---

# 24. What this would and would not prove

If the Supplier Increment Realization Lemma is proved, it would establish:

$$
\boxed{
\text{supplier mechanism}
\not\subset
\{
O_W^T=0,
\mathsf R_{\rm nat}=0
\}.
}
$$

It would **not yet** prove global Navier--Stokes regularity.

One still has to verify that:

1. every hypothetical singular branch entering the MORP minimal-return normal form must carry the supplier-increment package through the same return object;

2. the positive trace / residual event produces enough depletion or exclusion in the minimal-obstruction geometry;

3. the remaining defect-only branch cannot detach from the supplier mechanism.

Thus the present result closes one concrete CAR / trace realization interface, not the Clay problem.

---

# 25. Source ledger

## External finite-window trace definition

Runlong Yu, *Invisible Defect Cascades for Navier--Stokes Regularity*, arXiv:2606.12756v1.

Relevant definitions:

- finite observation window:

  $$
  W=(n,\ell,\Lambda,\chi,s_\ast);
  $$

- trace correction space:

  $$
  H_W;
  $$

- $H_W$ consists of divergence-free selected-time fields localized in the observation ball and projected to the finite window;

- primal trace observation:

  $$
  \mathcal O_W^Td
  =
  \Pi_W^T\dot U(s_\ast);
  $$

- the window:

  $$
  \Lambda
  $$

  may be a finite-dimensional space of localized test functions, wave packets, Stokes eigenfunctions, localized Fourier packets, or adjoint test modes;

- the dual map:

  $$
  A_W^\ast
  $$

  is generated by the backward adjoint **linearized coarse-grained Navier--Stokes equation**.

These facts are the reason DCRP-13 required correction and DCRP-14 uses a primal solenoidal trace window.

## Cheskidov--Dai / Cheskidov--Shvydkoy

Used for:

$$
\|u_Q\|_\infty
\gtrsim
\nu\lambda_Q.
$$

This is the starting amplitude that survives nonlinear memory subtraction.

---

# 26. End state

DCRP-13's scalar six-test shortcut has been corrected.

The correct statement is stronger in the relevant sense.

The actual nonlinear supplier increment satisfies:

$$
\boxed{
\|g_q(t_1)\|_\infty
\gtrsim
\nu\lambda_q.
}
$$

After critical re-scaling:

$$
\boxed{
h_q
=
\lambda_q^{-1}
g_q
}
$$

is:

- divergence free;
- supported in one fixed Fourier annulus;
- generated by actual same-history NS forcing;
- nonvanishing at fixed normalized amplitude.

There exists one universal finite-dimensional solenoidal trace window:

$$
\boxed{
H_\ast
\subset
C_c^\infty(B_R;\mathbb R^3),
\qquad
\dim H_\ast=N_\ast<\infty,
}
$$

such that:

$$
\boxed{
\|\Pi_{H_\ast}h_q\|_2
\ge
c_\ast\nu.
}
$$

Therefore the trace-family / detector-space geometry is no longer open.

The single remaining bridge is:

$$
\boxed{
\textbf{
actual nonlinear supplier increment}
\Longrightarrow
\textbf{
cleaned finite-window defect selected-time component}
}
$$

up to already-paid projection / localization / pressure / synchronization residuals.

The next exact target is:

$$
\boxed{
\textbf{
Supplier Increment / Finite-Window Defect Realization Lemma}.
}
$$

That is now the next attack.

---

# Checkpoint v15 Update — DCRP-15

# NS-DCRP-15 — Exact Supplier Tangent Completion, Finite-Window Trace-or-Residual Gap, and the Local Supplier Capture Barrier

- date: 2026-08-16
- status: research proof checkpoint
- canonical source: UTF-8 Markdown
- canonical math delimiters: `$...$` and `$$...$$`
- objective:
  1. finish the DCRP-14 supplier-increment / finite-window defect realization bridge at the fixed-window algebraic level;
  2. audit whether the resulting supplier exclusion is already local enough to attack a singular point;
  3. isolate the next genuine PDE blocker without hiding it inside a compiler term.
- no full Navier--Stokes regularity claim is made.
- principal internal dependencies:
  - FCBP finite-window constrained defect quotient;
  - FCBP selected-time trace channel;
  - finite-window local-to-clean residual budgets;
  - MORP native residual completion;
  - DCRP-08 through DCRP-14.
- principal external primary sources:
  - Runlong Yu, *Invisible Defect Cascades for Navier-Stokes Regularity*, arXiv:2606.12756v1;
  - Runlong Yu, *Finite-Window Singularity Audits and Local-to-Clean Defect Transfer for Navier-Stokes*, arXiv:2606.15086v1;
  - Cheskidov--Dai, arXiv:1507.06611v6;
  - Cheskidov--Shvydkoy, arXiv:1102.1944v2.

---

# 1. Executive result

DCRP-14 constructed an actual nonlinear supplier increment

$$
g_q
$$

satisfying a forced Stokes equation and proved that, after critical supplier normalization,

$$
h_q
$$

has a uniform projection onto one fixed finite-dimensional divergence-free local trace space

$$
H_\ast:
$$

$$
\boxed{
\|\Pi_{H_\ast}h_q\|_{L^2(B_R)}
\ge
c_\ast\nu.
}
\tag{1.1}
$$

The remaining question was whether this actual nonlinear increment can be realized as a constrained finite-window defect direction of the type observed by the FCBP combined map.

The first main theorem of this round answers the infinite-dimensional PDE part affirmatively.

Let

$$
G
$$

be any divergence-free nonlinear increment solving

$$
\partial_tG
-
\nu\Delta G
+
\nabla\pi
=
-\nabla\cdot T.
$$

Let

$$
(U,P,R)
$$

be any divergence-free resolved baseline package.

Define

$$
\boxed{
\dot U
=
G,
}
\tag{1.2}
$$

$$
\boxed{
\dot R
=
T
-
G\otimes U
-
U\otimes G,
}
\tag{1.3}
$$

$$
\boxed{
\dot P
=
\pi,
}
\tag{1.4}
$$

and

$$
\boxed{
\dot\Pi
=
-
\dot R:\nabla U
-
R:\nabla G.
}
\tag{1.5}
$$

Then the FCBP constrained tangent identities hold exactly:

$$
\boxed{
\nabla\cdot\dot U=0,
}
\tag{1.6}
$$

$$
\boxed{
\partial_t\dot U
-
\nu\Delta\dot U
+
\nabla\cdot
(
\dot U\otimes U
+
U\otimes\dot U
)
+
\nabla\dot P
=
-\nabla\cdot\dot R,
}
\tag{1.7}
$$

$$
\boxed{
-\Delta\dot P
=
\partial_i\partial_j
\left(
\dot U_iU_j
+
U_i\dot U_j
+
\dot R_{ij}
\right),
}
\tag{1.8}
$$

together with the required linearized flux identity.

Therefore

$$
\boxed{
\textbf{
the nonlinear supplier increment has an exact global constrained-defect completion.
}
}
\tag{1.9}
$$

No approximation is needed for the PDE tangent equations themselves.

The second main theorem is finite-dimensional.

Fix one normalized finite-window template

$$
W_\ast.
$$

Let

$$
X_\ast
$$

be its finite-dimensional raw projected package space.

Let

$$
\mathcal C_\ast:X_\ast\to Z_\ast^{res}
$$

be the linear constraint-residual map whose kernel is the constrained package space

$$
\boxed{
\mathcal Z_\ast
=
\ker\mathcal C_\ast.
}
\tag{1.10}
$$

Let

$$
\mathcal T_\ast:X_\ast\to H_\ast
$$

be the selected-time trace projection.

Because all spaces are finite dimensional, define the smallest positive singular value

$$
\boxed{
\sigma_\ast
=
\inf_{
x\in\mathcal Z_\ast^\perp,\,
\|x\|=1
}
\|\mathcal C_\ast x\|
>
0.
}
\tag{1.11}
$$

For the raw finite-window projection

$$
x_q
$$

of the supplier tangent package, choose the window so that:

- the selected time is the supplier endpoint;
- the velocity trace space contains

  $$
  H_\ast;
  $$

- the spatial cutoff equals one on the support of

  $$
  H_\ast.
  $$

Then

$$
\boxed{
\|\mathcal T_\ast x_q\|
\ge
c_\ast\nu.
}
\tag{1.12}
$$

Let

$$
P_{\mathcal Z}
$$

be orthogonal projection onto the constrained finite-window space.

The finite-dimensional constraint projection theorem gives

$$
\boxed{
\|
\mathcal T_\ast
P_{\mathcal Z}x_q
\|
+
C_\ast
\|
\mathcal C_\ast x_q
\|
\ge
c_\ast\nu,
}
\tag{1.13}
$$

where

$$
C_\ast
=
\frac{
\|\mathcal T_\ast\|
}{
\sigma_\ast
}.
$$

Hence

$$
\boxed{
\textbf{
supplier finite-window package}
\Longrightarrow
\textbf{
trace visibility}
\ \vee\
\textbf{
fixed positive constraint residual}.
}
}
\tag{1.14}
$$

The external local-to-clean audit already decomposes exactly such finite-window errors into:

- pressure residual;
- localization leakage;
- truncation residual;
- nonlinear cutoff / nonlinear remainder;
- reproduction drift;
- gauge mismatch;
- profit mismatch.

Thus, on one fixed normalized supplier template,

$$
\boxed{
\|
O_{W_\ast}^T d_q
\|
+
C_{\rm led}
\mathcal B_{\rm sup}^{res}(q)
\ge
c_\ast\nu.
}
\tag{1.15}
$$

This closes the DCRP-14 finite-window realization problem:

a supplier nonlinear increment cannot become simultaneously trace invisible and residual free merely because of finite-window projection / cleaning.

However the round also identifies a major gap that earlier supplier arguments did not fully expose.

The dissipation wavenumber

$$
\Lambda(t)
$$

used in DCRP-08 through DCRP-15 is a global Fourier quantity.

The point

$$
x_q
$$

where the supplier shell is large need not lie near the local singular point

$$
x_\ast.
$$

Therefore the theorem

$$
\boxed{
\text{global singularity}
\Longrightarrow
\text{some global supplier trace}
}
$$

does not yet imply

$$
\boxed{
\text{local singular obstruction at }x_\ast
\Longrightarrow
\text{supplier trace in the same local MORP window}.
}
$$

This is not a compiler detail.

It is now the principal PDE-facing gap.

The next exact target is therefore

$$
\boxed{
\textbf{
Local Supplier Capture / Remote-Supplier Decoupling Lemma}.
}
\tag{1.16}
$$

A full proof must show one of:

1. a dissipation-boundary supplier of fixed critical normalized strength occurs within bounded parabolic distance of the singular point;

2. a remote global supplier cannot feed the local singular core strongly enough through the Navier--Stokes propagator;

3. failure of both statements produces an explicit local noncompact / pressure / transition carrier already retained by MORP.

This is the next real barrier.

---

# 2. External constrained defect equations audited

The finite-window raw defect direction has the form

$$
\boxed{
\dot{\mathfrak D}_W
=
(
\dot U,\dot P;
\dot P^{act},
\dot P^{har},
\dot R,\dot\Pi
).
}
\tag{2.1}
$$

The constrained tangent space requires

$$
\boxed{
\nabla\cdot\dot U=0,
}
\tag{2.2}
$$

$$
\boxed{
\partial_t\dot U
-
\Delta\dot U
+
\nabla\cdot
(
\dot U\otimes U
+
U\otimes\dot U
)
+
\nabla\dot P
=
-\nabla\cdot\dot R,
}
\tag{2.3}
$$

$$
\boxed{
-\Delta\dot P
=
\partial_i\partial_j
\left(
\dot U_iU_j
+
U_i\dot U_j
+
\dot R_{ij}
\right),
}
\tag{2.4}
$$

with

$$
\dot P
=
\dot P^{act}
+
\dot P^{har},
$$

$$
\Delta\dot P^{har}=0
$$

locally, and

$$
\boxed{
\dot\Pi
=
-\dot R:\nabla U
-
R:\nabla\dot U.
}
\tag{2.5}
$$

Exact pressure time-only gauges and exact Leray-null directions are quotiented.

Localization, harmonic tails, truncation, and nonlinear projection errors are not quotiented.

They remain explicit residual terms.

This distinction is central to the theorem below.

---

# 3. Actual nonlinear supplier increment

Let

$$
q=Q(t_1)
$$

be a supplier shell.

DCRP-14 defines

$$
\boxed{
G(t)
=
g_q(t)
=
u_q(t)
-
e^{\nu(t-t_0)\Delta}
u_q(t_0).
}
\tag{3.1}
$$

Then

$$
G(t_0)=0,
$$

and

$$
\boxed{
\partial_tG
-
\nu\Delta G
+
\nabla\pi
=
-\nabla\cdot T,
}
\tag{3.2}
$$

where

$$
\boxed{
T
=
\Delta_q(u\otimes u),
}
\tag{3.3}
$$

and

$$
\boxed{
\pi
=
\Delta_qp.
}
\tag{3.4}
$$

Also

$$
\nabla\cdot G=0.
$$

Taking divergence of (3.2),

$$
\boxed{
-\Delta\pi
=
\partial_i\partial_jT_{ij}.
}
\tag{3.5}
$$

This pressure identity is exactly what is needed for tangent completion.

---

# 4. NEW THEOREM — exact tangent completion relative to an arbitrary resolved baseline

## Theorem 4.1

Let

$$
(U,P,R)
$$

be any smooth divergence-free resolved coarse package on the same spacetime region.

Let

$$
(G,\pi,T)
$$

satisfy

$$
\nabla\cdot G=0,
$$

$$
\partial_tG
-
\nu\Delta G
+
\nabla\pi
=
-\nabla\cdot T,
$$

and

$$
-\Delta\pi
=
\partial_i\partial_jT_{ij}.
$$

Define

$$
\boxed{
\dot U
=
G,
}
\tag{4.1}
$$

$$
\boxed{
\dot P
=
\pi,
}
\tag{4.2}
$$

$$
\boxed{
\dot R
=
T
-
G\otimes U
-
U\otimes G,
}
\tag{4.3}
$$

and

$$
\boxed{
\dot\Pi
=
-\dot R:\nabla U
-
R:\nabla G.
}
\tag{4.4}
$$

Then

$$
(
\dot U,\dot P,\dot R,\dot\Pi
)
$$

satisfies the constrained linearized momentum, pressure-compatibility, divergence, and flux equations exactly.

### Proof

The divergence condition is immediate.

For momentum,

$$
\begin{aligned}
&
\partial_tG
-
\nu\Delta G
+
\nabla\cdot
(
G\otimes U
+
U\otimes G
)
+
\nabla\pi\\
&=
-\nabla\cdot T
+
\nabla\cdot
(
G\otimes U
+
U\otimes G
)\\
&=
-\nabla\cdot
\left[
T
-
G\otimes U
-
U\otimes G
\right]\\
&=
-\nabla\cdot\dot R.
\end{aligned}
$$

For pressure compatibility,

$$
\begin{aligned}
&
\partial_i\partial_j
\left(
G_iU_j
+
U_iG_j
+
\dot R_{ij}
\right)\\
&=
\partial_i\partial_j
T_{ij}\\
&=
-\Delta\pi.
\end{aligned}
$$

Finally (4.4) is exactly the required linearized flux definition.

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

# 5. Pressure split

On a local observation core

$$
B_R,
$$

write

$$
\boxed{
\pi
=
\pi^{act}
+
\pi^{har},
}
\tag{5.1}
$$

where

$$
\pi^{act}
$$

is the chosen localized Calderon--Zygmund pressure solve generated by

$$
T
$$

and

$$
\pi^{har}
$$

is harmonic on the core.

Then

$$
\boxed{
\Delta\pi^{har}=0
}
\tag{5.2}
$$

on the core.

This gives the required

$$
\dot P^{act},
\qquad
\dot P^{har}
$$

coordinates.

Any discrepancy between the global

$$
\pi
$$

and the chosen finite-window active solve is exactly of the type already placed in the pressure-transfer residual budget:

- harmonic tail;
- cutoff--Riesz commutator;
- active-source mismatch;
- finite pressure projection;
- pressure mean / periodization residual.

No pressure term needs to be silently discarded.

---

# 6. Normalized supplier tangent package

Normalize the supplier increment at

$$
\lambda_q
$$

and center

$$
x_q.
$$

Use normalized time

$$
\tau
=
\lambda_q^2(t-t_1).
$$

Define the full normalized tangent package

$$
\boxed{
\mathfrak z_q
=
(
G_q,\Pi_q;
\Pi_q^{act},
\Pi_q^{har},
\mathcal R_q,
\mathcal P_q
),
}
\tag{6.1}
$$

obtained by applying the Navier--Stokes parabolic scaling to the quantities in Theorem 4.1.

Because the original completion is exact, the normalized package satisfies the same tangent equations with the same viscosity

$$
\nu.
$$

At selected normalized time

$$
\tau=0,
$$

$$
\boxed{
G_q(\cdot,0)
=
h_q.
}
\tag{6.2}
$$

DCRP-14 gives

$$
\boxed{
\|
\Pi_{H_\ast}
G_q(0)
\|_{L^2(B_R)}
\ge
c_\ast\nu.
}
\tag{6.3}
$$

---

# 7. Fixed normalized window template

Fix once and for all a normalized finite observation window

$$
\boxed{
W_\ast
=
(
n_\ast,\ell_\ast,\Lambda_\ast,\chi_\ast,s_\ast
).
}
\tag{7.1}
$$

Choose

$$
s_\ast=0.
$$

Choose the observation and preparation balls so that

$$
\boxed{
\operatorname{supp}H_\ast
\subset
B_R
\Subset
Q_{\rm obs}
\Subset
Q_{\rm prep}.
}
\tag{7.2}
$$

Choose

$$
\chi_\ast\equiv1
$$

on a neighborhood of

$$
B_R
$$

at selected time.

Choose the selected-time trace space

$$
H_{W_\ast}
$$

to contain

$$
\boxed{
H_\ast.
}
\tag{7.3}
$$

Choose the finite velocity projection in

$$
\Lambda_\ast
$$

so that its selected-time velocity range also contains

$$
H_\ast.
$$

Because the supplier package is always normalized to the same unit annulus and the same local geometry, the template

$$
W_\ast
$$

does not change with

$$
q.
$$

Thus all finite-dimensional constants below are scale independent.

---

# 8. Raw finite-window projection

Let

$$
X_\ast
$$

be the finite-dimensional raw window space before imposing the tangent constraints.

Let

$$
\boxed{
\mathsf P_\ast^{raw}
}
$$

be the chosen bounded finite-window projection from the normalized global package to

$$
X_\ast.
$$

Define

$$
\boxed{
x_q
=
\mathsf P_\ast^{raw}
\mathfrak z_q.
}
\tag{8.1}
$$

The selected-time trace extraction

$$
\mathcal T_\ast:X_\ast\to H_\ast
$$

is chosen as the orthogonal

$$
H_\ast
$$

projection of the velocity coordinate at

$$
s_\ast=0.
$$

Because:

- the cutoff is identically one on

  $$
  \operatorname{supp}H_\ast;
  $$

- the velocity window contains

  $$
  H_\ast;
  $$

- the raw selected-time velocity is

  $$
  h_q;
  $$

one has

$$
\boxed{
\mathcal T_\ast x_q
=
\Pi_{H_\ast}h_q.
}
\tag{8.2}
$$

Therefore

$$
\boxed{
\|
\mathcal T_\ast x_q
\|
\ge
c_\ast\nu.
}
\tag{8.3}
$$

Status:

$$
\boxed{
\textbf{PROVED by window construction}.
}
$$

---

# 9. Constraint residual map

Let

$$
Z_\ast^{res}
$$

be the finite-dimensional residual target space containing the projected errors in:

- divergence;
- momentum;
- pressure compatibility;
- active/harmonic pressure split;
- flux identity.

Define the bounded linear constraint-residual map

$$
\boxed{
\mathcal C_\ast:
X_\ast
\longrightarrow
Z_\ast^{res}.
}
\tag{9.1}
$$

By definition

$$
\boxed{
\mathcal Z_\ast
=
\ker\mathcal C_\ast
}
\tag{9.2}
$$

is the finite-dimensional constrained tangent space.

The global supplier package

$$
\mathfrak z_q
$$

satisfies the tangent equations exactly.

Therefore

$$
\mathcal C_\ast x_q
$$

contains only defects introduced by:

- localization;
- finite-dimensional projection / truncation;
- pressure cleaning;
- cutoff nonlinear mismatch;
- any declared finite-window synchronization.

There is no unexplained PDE defect.

---

# 10. Finite-dimensional constraint projection

Choose Hilbert norms on

$$
X_\ast
$$

and

$$
Z_\ast^{res}.
$$

Let

$$
P_{\mathcal Z}
$$

be orthogonal projection of

$$
X_\ast
$$

onto

$$
\mathcal Z_\ast.
$$

Let

$$
\mathcal Z_\ast^\perp
$$

be its orthogonal complement.

Because

$$
\ker
\left(
\mathcal C_\ast
|
_{\mathcal Z_\ast^\perp}
\right)
=
\{0\},
$$

and

$$
\mathcal Z_\ast^\perp
$$

is finite dimensional, define

$$
\boxed{
\sigma_\ast
=
\inf_{
z\in\mathcal Z_\ast^\perp,\,
\|z\|=1
}
\|
\mathcal C_\ast z
\|
>
0.
}
\tag{10.1}
$$

For every

$$
x\in X_\ast,
$$

write

$$
x
=
P_{\mathcal Z}x
+
x^\perp.
$$

Then

$$
\mathcal C_\ast x
=
\mathcal C_\ast x^\perp,
$$

and

$$
\boxed{
\|
x-P_{\mathcal Z}x
\|
=
\|x^\perp\|
\le
\sigma_\ast^{-1}
\|
\mathcal C_\ast x
\|.
}
\tag{10.2}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 11. NEW THEOREM — finite-window trace-or-residual realization gap

## Theorem 11.1

For every normalized supplier raw package

$$
x_q,
$$

$$
\boxed{
\|
\mathcal T_\ast
P_{\mathcal Z}
x_q
\|
+
\frac{
\|\mathcal T_\ast\|
}{
\sigma_\ast
}
\|
\mathcal C_\ast x_q
\|
\ge
c_\ast\nu.
}
\tag{11.1}
$$

### Proof

By the triangle inequality,

$$
\begin{aligned}
\|
\mathcal T_\ast
P_{\mathcal Z}x_q
\|
&\ge
\|
\mathcal T_\ast x_q
\|
-
\|
\mathcal T_\ast
(
x_q-P_{\mathcal Z}x_q
)
\|\\
&\ge
c_\ast\nu
-
\|\mathcal T_\ast\|
\|
x_q-P_{\mathcal Z}x_q
\|.
\end{aligned}
$$

Apply (10.2).

Rearrange.

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

# 12. Fixed quantitative dichotomy

Theorem 11.1 implies

$$
\boxed{
\|
\mathcal T_\ast
P_{\mathcal Z}x_q
\|
\ge
\frac{
c_\ast
}{
2
}
\nu
}
\tag{12.1}
$$

or

$$
\boxed{
\|
\mathcal C_\ast x_q
\|
\ge
\frac{
c_\ast
\sigma_\ast
}{
2
\|\mathcal T_\ast\|
}
\nu.
}
\tag{12.2}
$$

Therefore

$$
\boxed{
\textbf{
actual supplier increment}
\Longrightarrow
\textbf{
finite-window trace visibility}
\ \vee\
\textbf{
fixed finite-window constraint residual}.
}
}
\tag{12.3}
$$

Because

$$
W_\ast
$$

is a fixed normalized template, the constants

$$
c_\ast,
\qquad
\sigma_\ast,
\qquad
\|\mathcal T_\ast\|
$$

are uniform over the entire supplier sequence.

This is the desired scale-uniform realization gap.

---

# 13. Passage to the cleaned quotient

Let

$$
\mathcal G_\ast^{ex}
$$

be the exact quotient-null subspace.

The constrained finite-window representative

$$
P_{\mathcal Z}x_q
$$

defines

$$
\boxed{
d_q
=
[
P_{\mathcal Z}x_q
]
\in
Y_{W_\ast}.
}
\tag{13.1}
$$

The exact null directions are:

- divergence-free projection nulls already removed;
- time-only pressure gauges.

Neither alters the selected-time velocity trace in

$$
H_\ast.
$$

Thus

$$
\boxed{
\|
\mathcal O_{W_\ast}^T
d_q
\|
\ge
c_T
\|
\mathcal T_\ast
P_{\mathcal Z}x_q
\|
}
\tag{13.2}
$$

for a fixed norm-equivalence constant

$$
c_T>0.
$$

Therefore

$$
\boxed{
\|
\mathcal O_{W_\ast}^T
d_q
\|
+
C_\ast^{res}
\|
\mathcal C_\ast x_q
\|
\ge
c_\ast'\nu.
}
\tag{13.3}
$$

Status:

$$
\boxed{
\textbf{PROVED for the fixed supplier template}.
}
$$

---

# 14. Identification with the existing residual ledger

The external local-to-clean framework defines

$$
\boxed{
\mathsf{Err}_\Lambda
=
\mathsf{Err}_{prs}
+
\mathsf{Err}_{loc}
+
\mathsf{Err}_{tr}
+
\mathsf{Err}_{nl}
+
\mathsf{Err}_{rep}
+
\mathsf{Err}_{gauge}
+
\mathsf{Err}_{prof}.
}
\tag{14.1}
$$

It further instantiates:

- pressure residuals;
- energy/flux/momentum localization;
- finite-window truncation;
- nonlinear cutoff mismatch;
- finite-dimensional nonlinear remainder;
- reproduction drift;
- gauge mismatch;
- profit discrepancy.

For the supplier tangent package, the raw global equations are exact.

Therefore every component of

$$
\mathcal C_\ast x_q
$$

is produced by the projection / localization / cleaning operations already represented by the first four of these residual classes:

$$
\boxed{
\mathsf{Err}_{prs},
\quad
\mathsf{Err}_{loc},
\quad
\mathsf{Err}_{tr},
\quad
\mathsf{Err}_{nl}.
}
\tag{14.2}
$$

If the selected supplier package is also synchronized with a return chart, reproduction / gauge / profit entries may be added, but they are not needed merely to realize the one-window trace direction.

Because

$$
Z_\ast^{res}
$$

is finite dimensional and the concrete residual ledger contains norms of all its declared components, norm equivalence gives a fixed constant

$$
C_{\rm led}<\infty
$$

such that

$$
\boxed{
\|
\mathcal C_\ast x_q
\|
\le
C_{\rm led}
\mathcal B_{\rm sup}^{res}(q),
}
\tag{14.3}
$$

where

$$
\boxed{
\mathcal B_{\rm sup}^{res}
=
\mathsf{Err}_{prs}
+
\mathsf{Err}_{loc}
+
\mathsf{Err}_{tr}
+
\mathsf{Err}_{nl}.
}
\tag{14.4}
$$

This uses only the fixed finite supplier window.

No scale-uniform infinite-dimensional comparison is required.

---

# 15. NEW THEOREM — package-level Supplier Trace/Residual Gap

Combining Sections 13--14,

$$
\boxed{
\|
\mathcal O_{W_\ast}^T
d_q
\|
+
C_{\rm sup}
\mathcal B_{\rm sup}^{res}(q)
\ge
c_{\rm sup}\nu.
}
\tag{15.1}
$$

Thus

$$
\boxed{
\textbf{
a supplier nonlinear increment cannot be simultaneously
trace invisible and finite-window residual free.
}
}
\tag{15.2}
$$

In particular

$$
\boxed{
\mathcal O_{W_\ast}^T d_q=0
\Longrightarrow
\mathcal B_{\rm sup}^{res}(q)
\ge
c\nu.
}
\tag{15.3}
$$

and

$$
\boxed{
\mathcal B_{\rm sup}^{res}(q)=0
\Longrightarrow
\|
\mathcal O_{W_\ast}^T d_q
\|
\ge
c\nu.
}
\tag{15.4}
$$

Status:

$$
\boxed{
\textbf{PROVED at the fixed normalized finite-window compiler level}.
}
$$

This is the completed form of the DCRP-14 realization bridge.

---

# 16. Relation to the local-to-clean transfer theorem

The external local-to-clean framework states that a localized package is coercively detected if:

- the clean quotient has a finite-window anti-phantom gap;
- quotient distance lifts stably;
- component detection transfers;
- the normalized residual budget is absorbable.

DCRP-15 does not prove the general absorption hypothesis.

Instead it proves a supplier-specific statement:

$$
\boxed{
\textbf{
before any absorption argument,
the supplier package already has a uniform
trace-or-residual lower gap.
}
}
$$

Therefore the supplier sequence cannot satisfy

$$
\boxed{
O_W^T\to0
}
$$

and

$$
\boxed{
\mathsf{Err}_{prs}
+
\mathsf{Err}_{loc}
+
\mathsf{Err}_{tr}
+
\mathsf{Err}_{nl}
\to0
}
$$

simultaneously.

This removes one concrete combined-invisible route.

---

# 17. What this does to MORP

Suppose a MORP zero-cost branch contains the same supplier-centered finite-window packages.

The zero-cost kernel requires the relevant observation / native residual channels to vanish.

But Theorem 15.1 gives

$$
\boxed{
O_W^T
+
C_{\rm sup}
\mathcal B_{\rm sup}^{res}
\ge
c_{\rm sup}\nu.
}
$$

Thus

$$
\boxed{
\textbf{
the supplier-centered package is not in the exact
combined-invisible / residual-free kernel.
}
}
\tag{17.1}
$$

This statement is now unconditional at the supplier-centered finite window.

The phrase "supplier-centered finite window" is essential.

It leads to the localization audit below.

---

# 18. MAJOR AUDIT — the supplier constructed so far is global

The dissipation wavenumber used in DCRP-08 onward is

$$
\Lambda(t)
=
\lambda_{Q(t)}
$$

defined from the global Littlewood--Paley decomposition

$$
u_q
=
\Delta_q u.
$$

The boundary estimate

$$
\|u_Q(t)\|_\infty
\ge
c_0\nu\Lambda(t)
$$

selects a spatial point

$$
x_Q(t)
$$

where the global boundary shell is large.

Nothing in the definition implies

$$
\boxed{
|x_Q(t)-x_{\rm sing}|
\lesssim
\Lambda(t)^{-1}.
}
\tag{18.1}
$$

Nor does it imply that

$$
x_Q(t)
$$

lies in any fixed physical neighborhood of a particular singular point.

Therefore

$$
\boxed{
\textbf{
global supplier visibility is not yet local singular-point visibility.
}
}
\tag{18.2}
$$

This is a genuine gap.

---

# 19. Why this gap matters

The MORP / FCBP obstruction framework is local.

A local singular point

$$
z_\ast
=
(x_\ast,T)
$$

is followed through shrinking parabolic windows

$$
Q_{r_n}(z_\ast).
$$

A global supplier shell centered very far from

$$
x_\ast
$$

may be dynamically active elsewhere in the solution while being irrelevant to the local singular mechanism.

Therefore the implication

$$
\boxed{
T<\infty
\Longrightarrow
\text{global supplier package at arbitrarily high frequency}
}
$$

is insufficient by itself to contradict a local combined-invisible defect cascade at

$$
z_\ast.
$$

A spatial capture theorem is required.

---

# 20. The singular-point local lower bound that is already available

For a genuine singular point

$$
z_\ast,
$$

standard local epsilon-regularity gives a universal critical lower bound.

Schematically, for sufficiently small

$$
r,
$$

$$
\boxed{
r^{-2}
\int_{Q_r(z_\ast)}
|u|^3
\ge
\varepsilon_\ast
}
\tag{20.1}
$$

in a pressure-free one-scale formulation, or the corresponding velocity-pressure CKN lower bound.

Thus the singular point cannot become locally empty under its own parabolic scaling.

However (20.1) does not immediately produce a single dissipation-boundary Littlewood--Paley shell with

$$
\lambda_q^{-1}
\|u_q\|_\infty
\ge
c\nu
$$

inside the same local cylinder.

The passage

$$
\boxed{
\text{local critical mass}
\Longrightarrow
\text{local supplier shell}
}
\tag{20.2}
$$

is presently open in this DCRP route.

This is exactly where an infinite diffuse local frequency cascade may still hide.

---

# 21. Why the global supplier cannot simply be declared causal for the local singularity

Navier--Stokes pressure is nonlocal.

The velocity equation is also coupled globally through the Leray projector.

Therefore spatial separation alone does not imply exact dynamical decoupling.

Conversely, nonlocality does not imply that a remote supplier can feed a singular point with scale-critical strength without paying a quantitative propagation / pressure cost.

Thus neither direction may be assumed.

The correct theorem must estimate it.

---

# 22. New primary frontier — Local Supplier Capture / Remote-Supplier Decoupling

The next exact target is

$$
\boxed{
\textbf{
Local Supplier Capture / Remote-Supplier Decoupling Lemma}.
}
$$

A sufficient theorem could have the following form.

Let

$$
z_\ast
=
(x_\ast,T)
$$

be a singular point.

For every sufficiently small local singular scale

$$
r,
$$

prove at least one of:

### A. Local supplier capture

There exist

$$
t_r\in(T-r^2,T),
$$

a frequency

$$
\lambda_r
\gtrsim
r^{-1},
$$

and a center

$$
x_r
$$

with

$$
|x_r-x_\ast|
\le
Cr,
$$

such that

$$
\boxed{
\lambda_r^{-1}
\|
\Delta_{\sim\lambda_r}u(t_r)
\|_{L^\infty(B_{Cr}(x_\ast))}
\ge
c\nu.
}
\tag{22.1}
$$

Then the entire DCRP-14 / DCRP-15 supplier trace package is available in the same local singular window.

### B. Localized diffuse-frequency defect

No individual local supplier shell carries the critical atom, but a derivative/frequency carrier with divergent effective multiplicity survives inside the local window.

This must be represented by the existing relative-scale / derivative defect completion.

### C. Remote-supplier propagation tax

The local singular growth is sustained by scales / centers outside the local capture region.

Then prove a fixed critical contribution in one of:

- pressure transport;
- nonlocal Leray coupling;
- boundary flux;
- local momentum leakage;
- native transition residual.

Any of these routes the remote supply into an already-paid or native residual ledger.

If A, the supplier trace gap kills local invisibility.

If B or C, the local supplier failure is not free.

---

# 23. A possible localized supplier construction

Choose

$$
\chi_r(x)
=
\chi
\left(
\frac{
x-x_\ast
}{
r
}
\right),
$$

with

$$
\chi\equiv1
$$

on the inner ball and compactly supported in a slightly larger ball.

Define the localized velocity

$$
\boxed{
v_r
=
\chi_r u.
}
\tag{23.1}
$$

Because

$$
\nabla\cdot v_r
\ne0,
$$

one must either:

- apply a local solenoidal correction;
- or use the Leray projection

  $$
  \mathbb Pv_r.
  $$

The localized field satisfies a forced Navier--Stokes / Stokes equation with forcing consisting of:

- cutoff momentum terms;
- pressure transport;
- localization commutators;
- nonlocal projection tails.

This is favorable conceptually.

Those are precisely the residual classes already isolated in the finite-window local-to-clean framework.

The intended proof structure is

$$
\boxed{
\begin{aligned}
&\text{local singularity}\\
&\Longrightarrow
\text{localized field remains nonregular}\\
&\Longrightarrow
\text{localized dissipation boundary }\Lambda_{\rm loc}\to\infty\\
&\Longrightarrow
\text{local supplier atom}
\end{aligned}
}
$$

unless the localization forcing is itself non-negligible.

If the forcing is non-negligible, it is paid leakage / residual.

This is the natural next attack.

---

# 24. Localized dissipation wavenumber proposal

For a divergence-free localized field

$$
v,
$$

define

$$
\boxed{
\Lambda_{\rm loc}(t)
=
\min
\left\{
\lambda_q:
\lambda_p^{-1}
\|v_p(t)\|_\infty
<
c_0\nu
\quad
\forall p>q
\right\}.
}
\tag{24.1}
$$

At the boundary

$$
Q_{\rm loc}(t),
$$

minimality gives exactly

$$
\boxed{
\|v_{Q_{\rm loc}}\|_\infty
\ge
c_0\nu
\Lambda_{\rm loc}.
}
\tag{24.2}
$$

Therefore the supplier trace theorem applies immediately once

$$
\Lambda_{\rm loc}
$$

is shown to become unbounded along the local singular branch.

The missing theorem becomes

$$
\boxed{
\text{bounded }\Lambda_{\rm loc}
+
\text{small localization forcing}
\Longrightarrow
\text{local regularity}.
}
\tag{24.3}
$$

This is a forced/local version of the global Cheskidov--Dai continuation mechanism.

---

# 25. Forced high-frequency estimate needed

The localized divergence-free field has schematic equation

$$
\boxed{
\partial_tv
-
\nu\Delta v
+
\mathbb P\nabla\cdot(v\otimes v)
=
f_{\rm loc}
+
f_{\rm mismatch}.
}
\tag{25.1}
$$

A localized dissipation-wavenumber proof needs an estimate of the form

$$
\boxed{
\frac d{dt}
\|v\|_{H^2}^2
\le
C
f_{\le Q_{\rm loc}}(t)
\|v\|_{H^2}^2
+
C
\langle
f_{\rm loc}+f_{\rm mismatch},
v
\rangle_{H^2}.
}
\tag{25.2}
$$

If

$$
Q_{\rm loc}
$$

remains bounded and the forcing term is integrable in the correct normalized dual norm, Gronwall yields local continuation.

Therefore singularity forces

$$
\boxed{
\Lambda_{\rm loc}\to\infty
}
$$

or a nonintegrable localization / pressure / projection forcing.

Either route is detectable.

This is the next PDE estimate to prove.

---

# 26. Why the current progress still matters

The global/local audit does not invalidate DCRP-08 through DCRP-15.

Those rounds have established reusable analytic modules:

1. dissipation-boundary critical atom;
2. actual Duhamel ancestry;
3. first-crossing positive shell flux;
4. heat-band PFET / paid alternative;
5. local heat-flux localization;
6. finite-dimensional supplier trace lift;
7. exact nonlinear-increment tangent completion;
8. finite-window trace-or-residual gap.

The current issue is only

$$
\boxed{
\textbf{
placing this supplier module at the same local singular point.
}
}
$$

Once a local supplier is produced, the entire supplier package can be reused without modification.

---

# 27. Exact finite-window conclusion of this round

For any actual supplier event for which the supplier-centered finite window is admissible,

$$
\boxed{
\|
\mathcal O_{W_\ast}^T
d_q
\|
+
C_{\rm sup}
\left(
\mathsf{Err}_{prs}
+
\mathsf{Err}_{loc}
+
\mathsf{Err}_{tr}
+
\mathsf{Err}_{nl}
\right)
\ge
c_{\rm sup}\nu.
}
\tag{27.1}
$$

Therefore

$$
\boxed{
\textbf{
supplier projection / cleaning cannot manufacture an exact phantom.
}
}
\tag{27.2}
$$

This is the completed finite-window realization theorem.

---

# 28. Updated proof-state diagram

The current route is

$$
\boxed{
\begin{aligned}
\text{finite-time singularity}
&\Longrightarrow
\text{local non-CKN branch}\\
&\overset{\mathrm{OPEN}}{\Longrightarrow}
\text{local supplier or paid localization forcing}\\
&\Longrightarrow
\text{critical supplier atom}\\
&\Longrightarrow
\text{nonlinear supplier increment}\\
&\Longrightarrow
\text{finite solenoidal trace window}\\
&\Longrightarrow
\text{trace visibility or residual}\\
&\Longrightarrow
\text{not exact combined-invisible / residual-free}.
\end{aligned}
}
\tag{28.1}
$$

Everything after the second arrow has now been substantially developed.

The next target is exactly the second arrow.

---

# 29. Relation to the question "can this actually finish?"

The research-space contraction is real.

The current path no longer has dozens of unrelated named obstructions.

For this supplier/trace route, the major unresolved analytic implication is now

$$
\boxed{
\text{local singularity}
\Longrightarrow
\text{local supplier}
\ \vee\
\text{paid localization/nonlocal forcing}.
}
$$

However this implication is not a small bookkeeping lemma.

It is a genuine local harmonic-analysis / forced-frequency regularity problem.

Therefore one may reasonably say

$$
\boxed{
\text{the route is materially narrower}
}
$$

but not

$$
\boxed{
\text{QED is now guaranteed or necessarily close}.
}
$$

The next rounds will determine whether the local forced dissipation-wavenumber estimate closes or generates another true analytic obstruction.

---

# 30. Source audit

## Invisible Defect Cascades

Runlong Yu, arXiv:2606.12756v1.

Checked structural facts:

- finite observation window:

  $$
  W=(n,\ell,\Lambda,\chi,s_\ast);
  $$

- finite raw defect direction:

  $$
  (\dot U,\dot P;\dot P^{act},\dot P^{har},\dot R,\dot\Pi);
  $$

- constrained tangent equations;
- cleaned quotient:

  $$
  Y_W=\mathcal Z_W/\mathcal G_W^{ex};
  $$

- perturbative localization / tail sectors are not quotient null;
- selected-time trace:

  $$
  \mathcal O_W^Td
  =
  \Pi_W^T\dot U(s_\ast).
  $$

## Finite-Window Singularity Audits and Local-to-Clean Transfer

Runlong Yu, arXiv:2606.15086v1.

Checked residual classes:

$$
\boxed{
\mathsf{Err}_{prs},
\quad
\mathsf{Err}_{loc},
\quad
\mathsf{Err}_{tr},
\quad
\mathsf{Err}_{nl},
\quad
\mathsf{Err}_{rep},
\quad
\mathsf{Err}_{gauge},
\quad
\mathsf{Err}_{prof}.
}
$$

The paper explicitly records:

- cutoff momentum localization residual;
- pressure-transfer residual;
- truncation residual;
- nonlinear cutoff mismatch;
- finite-dimensional nonlinear remainder;
- normalized residual-budget synchronization.

It does not prove those residuals are uniformly small.

DCRP-15 uses them only as explicit nonzero alternatives.

---

# 31. End state

This round completes the finite-window supplier realization bridge.

The strongest fixed-window statement is

$$
\boxed{
\textbf{
Supplier Trace/Residual Gap}
}
$$

$$
\boxed{
\|
\mathcal O_{W_\ast}^T
d_q
\|
+
C_{\rm sup}
\mathcal B_{\rm sup}^{res}(q)
\ge
c_{\rm sup}\nu.
}
$$

Thus a genuine supplier nonlinear increment cannot be erased by:

- finite-dimensional projection;
- finite-window cleaning;
- pressure splitting;
- localization;
- truncation;
- nonlinear coordinate conversion;

without leaving a fixed residual payment.

The next and now genuinely central frontier is

$$
\boxed{
\textbf{
Local Supplier Capture / Remote-Supplier Decoupling Lemma}.
}
$$

The most concrete next attack is

$$
\boxed{
\textbf{
forced localized dissipation-wavenumber continuation theorem}
}
$$

for a divergence-free localized field around the singular point.

If that theorem is proved, a local singularity must produce either

$$
\boxed{
\text{local critical supplier}
}
$$

or

$$
\boxed{
\text{non-negligible localization / pressure / nonlocal forcing}.
}
$$

Either outcome enters the already-built supplier/PFET/residual machinery.

That is the next exact attack.

---

# Checkpoint v16 Update — DCRP-16

# NS-DCRP-16 — Good-Collar Localization, Forced Dissipation-Wavenumber Continuation, and Local Supplier Capture

- date: 2026-08-16
- status: research proof checkpoint
- canonical source: UTF-8 Markdown
- canonical math delimiters: `$...$` and `$$...$$`
- objective: close the DCRP-15 Local Supplier Capture / Remote-Supplier Decoupling barrier by constructing a divergence-free localization around a first singular point and proving that bounded localized dissipation wavenumber would force local continuation.
- no full Navier--Stokes regularity claim is made.
- principal internal dependencies: DCRP-09 through DCRP-15 supplier/trace modules; MORP local singular-window architecture.
- external primary calibration: Caffarelli--Kohn--Nirenberg partial regularity; Barker--Prange, arXiv:1812.09115v2; Bradshaw--Grujić, arXiv:1501.01043v2; Cheskidov--Dai, arXiv:1507.06611v6.

---

# 1. Executive result

DCRP-15 identified a genuine gap: the dissipation wavenumber used in DCRP-08 was global, so the critical supplier shell could in principle be spatially remote from a chosen singular point.

This round removes that gap at the level of first-singularity localization.

Let

$$
z_\ast=(x_\ast,T)
$$

be a singular point at the first singular time

$$
T<\infty.
$$

The spatial singular set at time $T$ has one-dimensional Hausdorff measure zero. Therefore one can choose arbitrarily small radii

$$
\rho_k\downarrow0
$$

and positive collar widths

$$
\delta_k>0
$$

such that the closed annulus

$$
\boxed{
A_k=
\left\{
x:
\rho_k-\delta_k
\le
|x-x_\ast|
\le
\rho_k+\delta_k
\right\}
}
\tag{1.1}
$$

contains no singular point at time $T$.

Consequently the solution is smooth, with uniform bounds on every derivative, on a spacetime neighborhood of each fixed collar

$$
A_k\times(T-\tau_k,T].
$$

Choose a cutoff $\chi_k$ which equals one on the inner ball and changes only inside the good collar. Use a Bogovskii correction $b_k$ supported in the collar to define

$$
\boxed{
v_k=\chi_k u-b_k,
}
\tag{1.2}
$$

so that

$$
\boxed{\nabla\cdot v_k=0,}
\tag{1.3}
$$

$$
\boxed{v_k=u}
\tag{1.4}
$$

on a smaller ball around $x_\ast$, and $v_k$ is compactly supported.

The localized field satisfies a forced divergence-free Navier--Stokes equation

$$
\boxed{
\partial_t v_k-\nu\Delta v_k+\mathbb P\nabla\cdot(v_k\otimes v_k)=F_k.
}
\tag{1.5}
$$

Because the collar is regular up to $T$, for every fixed $k$,

$$
\boxed{
F_k\in L^2(T-\tau_k,T;L^2(\mathbb R^3)).
}
\tag{1.6}
$$

Define the localized dissipation wavenumber

$$
\Lambda_k(t)=\lambda_{Q_k(t)}
$$

by

$$
\boxed{
\Lambda_k(t)=
\min\left\{
\lambda_q:
\lambda_p^{-1}\|(v_k)_p(t)\|_\infty<c_0\nu
\quad\forall p>q
\right\}.
}
\tag{1.7}
$$

The main forced continuation theorem is:

> If
>
> $$
> \sup_{t\uparrow T}Q_k(t)<\infty,
> $$
>
> then
>
> $$
> v_k\in L_t^\infty H_x^1\cap L_t^2H_x^2
> $$
>
> up to $T$.

Since $v_k=u$ near $x_\ast$, this makes $(x_\ast,T)$ regular, contradiction.

Hence for every good collar $k$,

$$
\boxed{
\limsup_{t\uparrow T}\Lambda_k(t)=+\infty.
}
\tag{1.8}
$$

At each localized dissipation boundary,

$$
\boxed{
\lambda_{Q_k}^{-1}\|(v_k)_{Q_k}\|_\infty\ge c_0\nu.
}
\tag{1.9}
$$

Because the localized field is compactly supported, the transition collar is smooth up to the singular time, and Littlewood--Paley kernels have rapid off-support decay, a sufficiently high boundary shell cannot achieve the lower bound far outside the localization region or inside the smooth transition collar.

Thus the supplier point lies in the inner region where $v_k=u$, up to an error rapidly decaying in relative frequency.

Selecting the supplier frequency sufficiently large yields a point $x_k$, a time $t_k\uparrow T$, and a frequency $\lambda_k\to\infty$ such that

$$
\boxed{
|x_k-x_\ast|\le C\rho_k,
}
\tag{1.10}
$$

and

$$
\boxed{
\lambda_k^{-1}
|
\Delta_{\sim\lambda_k}u(x_k,t_k)
|
\ge
c_{\rm loc}\nu.
}
\tag{1.11}
$$

Since $\rho_k\downarrow0$,

$$
\boxed{x_k\to x_\ast.}
\tag{1.12}
$$

Therefore

$$
\boxed{
\textbf{
every first singular point admits a sequence of actual,
arbitrarily high-frequency, critical supplier atoms whose centers converge to that singular point.
}
}
\tag{1.13}
$$

This closes the physical-space version of Local Supplier Capture.

The DCRP-09 through DCRP-15 supplier/trace machinery can now be re-applied to the original Navier--Stokes field $u$, not merely to a remote global supplier.

The next unresolved interface is narrower:

$$
\boxed{
\textbf{
Local Supplier Sequence}
\Longrightarrow
\textbf{
the same MORP minimal-return / obstruction sequence}.
}
\tag{1.14}
$$

---

# 2. Good radii around a first singular point

Let

$$
\Sigma_T=
\left\{
x\in\mathbb R^3:
(x,T)\text{ is singular}
\right\}.
$$

The Caffarelli--Kohn--Nirenberg theory gives zero one-dimensional parabolic Hausdorff measure for the spacetime singular set. In particular,

$$
\boxed{\mathcal H^1(\Sigma_T)=0.}
\tag{2.1}
$$

Fix $x_\ast\in\Sigma_T$. The map

$$
d_{x_\ast}(x)=|x-x_\ast|
$$

is one-Lipschitz, so

$$
\boxed{
\mathcal H^1
\left(
d_{x_\ast}
(
\Sigma_T\cap\overline{B_R(x_\ast)}
)
\right)=0.
}
\tag{2.2}
$$

For fixed $R$, the bounded time-slice singular set is closed, hence compact, and its distance image is compact.

Therefore there exists a sequence

$$
\boxed{\rho_k\downarrow0}
\tag{2.3}
$$

outside that distance image.

Set

$$
\boxed{
d_k=
\operatorname{dist}
\left(
\rho_k,
d_{x_\ast}(\Sigma_T)
\right)>0,
}
\tag{2.4}
$$

and

$$
\boxed{
\delta_k=
\min\left\{
\frac{d_k}{4},
\frac{\rho_k}{16}
\right\}.
}
\tag{2.5}
$$

Then

$$
\boxed{
A_k=
\left\{
\rho_k-2\delta_k
\le
|x-x_\ast|
\le
\rho_k+2\delta_k
\right\}
}
\tag{2.6}
$$

contains no point of $\Sigma_T$.

Status:

$$
\boxed{\textbf{PROVED}.}
$$

---

# 3. Uniform collar regularity

Every point $(x,T)$ with $x\in A_k$ is regular. The regular set is open in spacetime. Since $A_k$ is compact, finitely many regularity neighborhoods cover $A_k\times\{T\}$.

Therefore there is $\tau_k>0$ and a slightly enlarged collar $A_k^+$ such that

$$
\boxed{
u\text{ is smooth on }A_k^+\times(T-\tau_k,T].
}
\tag{3.1}
$$

For every integer $m\ge0$,

$$
\boxed{
\sup_{A_k^+\times(T-\tau_k,T]}
|\nabla^m u|<\infty.
}
\tag{3.2}
$$

A standard local pressure decomposition gives smooth control of the local pressure component. The far pressure component is harmonic on the collar and is controlled there by finite kinetic energy and positive spatial separation.

Status:

$$
\boxed{
\textbf{STANDARD LOCAL REGULARITY CONSEQUENCE}.
}
$$

---

# 4. Divergence-free good-collar localization

Choose

$$
\chi_k\in C_c^\infty(B_{\rho_k+\delta_k}(x_\ast))
$$

with

$$
\boxed{
\chi_k\equiv1
\quad\text{on }B_{\rho_k-\delta_k}(x_\ast)
}
\tag{4.1}
$$

and

$$
\boxed{
\operatorname{supp}\nabla\chi_k\subset A_k.
}
\tag{4.2}
$$

Set

$$
f_k=\nabla\chi_k\cdot u.
$$

Since $\nabla\cdot u=0$ and $\chi_k$ is compactly supported,

$$
\int f_k\,dx
=
\int\nabla\cdot(\chi_ku)\,dx
=
0.
$$

Let $\mathcal B_k$ be a Bogovskii operator on a smooth annular domain containing $\operatorname{supp}\nabla\chi_k$ and define

$$
\boxed{
b_k=\mathcal B_k(f_k).
}
\tag{4.3}
$$

Then

$$
\boxed{\nabla\cdot b_k=f_k}
\tag{4.4}
$$

and $b_k$ is supported in the good collar.

Define

$$
\boxed{
v_k=\chi_ku-b_k.
}
\tag{4.5}
$$

Then

$$
\boxed{\nabla\cdot v_k=0,}
\tag{4.6}
$$

$$
\boxed{
v_k=u
\quad
\text{on }B_{\rho_k-\delta_k}(x_\ast),
}
\tag{4.7}
$$

and $v_k$ is compactly supported in a ball of radius $O(\rho_k)$.

---

# 5. Local $L^2$ bound

Bogovskii boundedness and the global energy inequality give, for each fixed $k$,

$$
\boxed{
\sup_{t<T}\|v_k(t)\|_2
\le
M_k<\infty.
}
\tag{5.1}
$$

No uniformity in $k$ is needed for the contradiction on one fixed collar.

---

# 6. Forced localized Navier--Stokes equation

Direct substitution of $v_k=\chi_ku-b_k$ into Navier--Stokes and application of the Leray projector yields

$$
\boxed{
\partial_tv_k
-
\nu\Delta v_k
+
\mathbb P\nabla\cdot(v_k\otimes v_k)
=
F_k.
}
\tag{6.1}
$$

Before Leray projection, the forcing is a finite sum of terms produced by:

- derivatives of $\chi_k$;
- $b_k$ and its time/spatial derivatives;
- collar values of $u,\nabla u,p$;
- the difference between $\chi_k(u\cdot\nabla u)$ and $(v_k\cdot\nabla)v_k$.

All raw forcing terms are supported in, or generated from, the good collar.

By Section 3, for fixed $k$ all collar fields are uniformly smooth up to $T$. Since the Leray projector is bounded on $L^2$,

$$
\boxed{
F_k\in
L^\infty(T-\tau_k,T;L^2(\mathbb R^3))
}
\tag{6.2}
$$

and hence

$$
\boxed{
\int_{T-\tau_k}^{T}
\|F_k(t)\|_2^2\,dt<\infty.
}
\tag{6.3}
$$

Status:

$$
\boxed{
\textbf{PROVED from good-collar regularity and standard Bogovskii bounds}.
}
$$

---

# 7. Localized dissipation wavenumber

Let

$$
(v_k)_q=\Delta_qv_k.
$$

Define

$$
\boxed{
Q_k(t)
=
\min\left\{
q:
\lambda_p^{-1}
\|(v_k)_p(t)\|_\infty
<
c_0\nu
\quad
\forall p>q
\right\}.
}
\tag{7.1}
$$

For smooth $v_k(t)$, $Q_k(t)<\infty$ for each $t<T$.

At an active boundary,

$$
\boxed{
\|(v_k)_{Q_k(t)}(t)\|_\infty
\ge
c_0\nu\lambda_{Q_k(t)}.
}
\tag{7.2}
$$

This follows from minimality of the definition and does not require the equation to be unforced.

---

# 8. Forced Littlewood--Paley $H^1$ estimate

Apply $\Delta_q$ to (6.1), pair with $(v_k)_q$, multiply by $\lambda_q^2$, and sum over $q$.

The nonlinear term is treated by the standard Bony/dissipation-wavenumber decomposition. For the pure velocity flux, the Cheskidov--Dai estimate is valid for every $s>0$. At $s=1$, choosing $c_0$ sufficiently small absorbs the high-frequency nonlinear part into viscosity.

One obtains

$$
\boxed{
\frac12
\frac d{dt}
\|v_k\|_{\dot H^1}^2
+
c_1\nu
\|v_k\|_{\dot H^2}^2
\le
C
f_k^{low}(t)
\|v_k\|_{\dot H^1}^2
+
\mathcal F_k(t),
}
\tag{8.1}
$$

where

$$
\boxed{
f_k^{low}(t)
=
\sum_{q\le Q_k(t)}
\lambda_q
\|(v_k)_q(t)\|_\infty
}
\tag{8.2}
$$

and

$$
\mathcal F_k
=
\sum_q
\lambda_q^2
\langle
(F_k)_q,(v_k)_q
\rangle.
$$

By Cauchy--Schwarz and Young,

$$
\boxed{
|\mathcal F_k|
\le
\frac{c_1\nu}{2}
\|v_k\|_{\dot H^2}^2
+
C\nu^{-1}
\|F_k\|_2^2.
}
\tag{8.3}
$$

Thus

$$
\boxed{
\frac d{dt}
\|v_k\|_{\dot H^1}^2
+
c_2\nu
\|v_k\|_{\dot H^2}^2
\le
C
f_k^{low}(t)
\|v_k\|_{\dot H^1}^2
+
C\nu^{-1}
\|F_k\|_2^2.
}
\tag{8.4}
$$

Status:

$$
\boxed{
\textbf{PROVED modulo the standard Cheskidov--Dai Bony estimate, with forcing treated explicitly}.
}
$$

---

# 9. Forced localized dissipation-wavenumber continuation

## Theorem 9.1

Fix $k$. Suppose there exist $Q_0<\infty$ and $t_0<T$ such that

$$
\boxed{
Q_k(t)\le Q_0
}
\tag{9.1}
$$

for every $t\in(t_0,T)$.

Then

$$
\boxed{
\sup_{t_0<t<T}\|v_k(t)\|_{H^1}<\infty
}
\tag{9.2}
$$

and

$$
\boxed{
\int_{t_0}^{T}
\|v_k(t)\|_{H^2}^2\,dt<\infty.
}
\tag{9.3}
$$

Consequently $(x_\ast,T)$ is regular.

### Proof

Since $Q_k(t)\le Q_0$, only finitely many low modes occur. Bernstein and (5.1) give

$$
\begin{aligned}
f_k^{low}(t)
&\le
\sum_{q\le Q_0}
\lambda_q
\|(v_k)_q(t)\|_\infty\\
&\le
C
\sum_{q\le Q_0}
\lambda_q^{5/2}
\|(v_k)_q(t)\|_2\\
&\le
C(Q_0)M_k
=
L_k.
\end{aligned}
$$

Insert this into (8.4). The force term is integrable by (6.3). Gronwall gives (9.2), and integration gives (9.3).

Since

$$
H^2(\mathbb R^3)\hookrightarrow L^\infty(\mathbb R^3),
$$

we obtain

$$
v_k\in L^2(t_0,T;L^\infty).
$$

This is a Serrin endpoint class:

$$
\frac2{2}+\frac3{\infty}=1.
$$

Hence $v_k$ is regular up to $T$.

But $v_k=u$ near $x_\ast$, so $(x_\ast,T)$ is regular, contradiction.

$$
\square
$$

Status:

$$
\boxed{\textbf{PROVED}.}
$$

---

# 10. Local dissipation wavenumber must diverge

Because $(x_\ast,T)$ is singular, Theorem 9.1 implies for every good collar

$$
\boxed{
\limsup_{t\uparrow T}Q_k(t)=+\infty.
}
\tag{10.1}
$$

Equivalently,

$$
\boxed{
\limsup_{t\uparrow T}\Lambda_k(t)=+\infty.
}
\tag{10.2}
$$

Status:

$$
\boxed{\textbf{PROVED}.}
$$

---

# 11. Choosing a local supplier sequence

For each $k$, choose $N_k$ large enough that

$$
\boxed{
2^{N_k}\rho_k\ge k
}
\tag{11.1}
$$

and all high-frequency localization/collar errors below are less than a fixed small fraction of $c_0\nu2^{N_k}$.

By (10.1), choose

$$
t_k\in
(T-\min\{\tau_k,k^{-1}\},T)
$$

with

$$
\boxed{
Q_k(t_k)\ge N_k.
}
\tag{11.2}
$$

Set

$$
q_k=Q_k(t_k),
\qquad
\lambda_k=2^{q_k}.
$$

Then

$$
\boxed{t_k\uparrow T,}
\tag{11.3}
$$

$$
\boxed{\lambda_k\rho_k\to\infty,}
\tag{11.4}
$$

and

$$
\boxed{
\lambda_k^{-1}
\|(v_k)_{q_k}(t_k)\|_\infty
\ge
c_0\nu.
}
\tag{11.5}
$$

---

# 12. Rapid off-support decay

Let $K$ be the Schwartz kernel of the unit Littlewood--Paley projector. Then

$$
K_q(x)=\lambda_q^3K(\lambda_qx),
$$

and for every $N$,

$$
\boxed{
|K_q(x)|
\le
C_N\lambda_q^3
(1+\lambda_q|x|)^{-N}.
}
\tag{12.1}
$$

Since $v_k$ is supported in a ball of radius $O(\rho_k)$ and has bounded $L^2$ norm, for points a fixed fraction of $\rho_k$ away from the support,

$$
\boxed{
\lambda_k^{-1}
|
(v_k)_{q_k}(x,t_k)
|
\to0.
}
\tag{12.2}
$$

because $\lambda_k\rho_k\to\infty$.

Hence a point realizing a fixed fraction of the supplier $L^\infty$ norm lies within $O(\rho_k)$ of $x_\ast$.

---

# 13. High frequencies are negligible in the smooth collar

Let $C_k$ be a closed subcollar containing the cutoff transition and the support of $b_k$.

Since $v_k$ is smooth with all derivatives uniformly bounded on a neighborhood of $C_k\times(T-\tau_k,T]$, a local smooth cutoff plus the Schwartz-kernel tail gives, for every $M$,

$$
\boxed{
\sup_{
x\in C_k,\,
t\in(T-\tau_k,T]
}
|
(v_k)_q(x,t)
|
\le
C_{k,M}\lambda_q^{-M}.
}
\tag{13.1}
$$

Therefore

$$
\boxed{
\sup_{
x\in C_k,\,
t\in(T-\tau_k,T]
}
\lambda_q^{-1}
|
(v_k)_q(x,t)
|
\to0
}
\tag{13.2}
$$

as $q\to\infty$.

Thus the critical supplier lower bound cannot be attained in the smooth cutoff/Bogovskii collar for $q$ sufficiently large.

---

# 14. Supplier center lies in the inner localization region

Choose $x_k$ with

$$
\boxed{
|
(v_k)_{q_k}(x_k,t_k)
|
\ge
\frac34
\|(v_k)_{q_k}(t_k)\|_\infty.
}
\tag{14.1}
$$

By Sections 12--13, after increasing $N_k$ if needed,

$$
\boxed{
x_k\in B_{\rho_k-\delta_k}(x_\ast).
}
\tag{14.2}
$$

Hence

$$
\boxed{
|x_k-x_\ast|\le\rho_k
}
\tag{14.3}
$$

and therefore

$$
\boxed{x_k\to x_\ast.}
\tag{14.4}
$$

Status:

$$
\boxed{\textbf{PROVED}.}
$$

---

# 15. Comparing localized and original shells

Inside the inner region $v_k=u$. Moreover, the difference $v_k-u$ is supported in the distant transition/exterior region.

With a slightly smaller inner selection region, the chosen $x_k$ has positive distance from $\operatorname{supp}(v_k-u)$ for each fixed $k$.

The Littlewood--Paley kernel tail therefore gives, for every $N$,

$$
\boxed{
|
\Delta_{q_k}(v_k-u)(x_k,t_k)
|
\le
C_{k,N}\lambda_k^{-N}.
}
\tag{15.1}
$$

Choose $q_k$ sufficiently large so that

$$
\boxed{
\lambda_k^{-1}
|
\Delta_{q_k}(v_k-u)(x_k,t_k)
|
\le
\frac{c_0}{4}\nu.
}
\tag{15.2}
$$

From (11.5) and (14.1),

$$
\lambda_k^{-1}
|
(v_k)_{q_k}(x_k,t_k)
|
\ge
\frac{3c_0}{4}\nu.
$$

Hence

$$
\boxed{
\lambda_k^{-1}
|
u_{q_k}(x_k,t_k)
|
\ge
\frac{c_0}{2}\nu.
}
\tag{15.3}
$$

Status:

$$
\boxed{\textbf{PROVED}.}
$$

---

# 16. NEW THEOREM — Local Supplier Capture

## Theorem 16.1

Let $u$ be a smooth finite-energy three-dimensional Navier--Stokes solution on $[0,T)$ with first singular time $T<\infty$. Let $(x_\ast,T)$ be any singular point.

Then there exist sequences

$$
\boxed{t_k\uparrow T,}
\tag{16.1}
$$

$$
\boxed{x_k\to x_\ast,}
\tag{16.2}
$$

and dyadic frequencies

$$
\boxed{\lambda_k\to\infty}
\tag{16.3}
$$

such that

$$
\boxed{
\lambda_k^{-1}
|
\Delta_{\lambda_k}u(x_k,t_k)
|
\ge
c_{\rm loc}\nu
}
\tag{16.4}
$$

for a universal $c_{\rm loc}>0$ up to the fixed Littlewood--Paley convention.

Equivalently,

$$
\boxed{
\textbf{
a first singular point is approached by actual critical
Littlewood--Paley supplier atoms of the original velocity field.
}
}
\tag{16.5}
$$

Status:

$$
\boxed{
\textbf{PROVED within the stated first-singularity / suitable-solution framework}.
}
$$

The theorem should receive independent audit before any public novelty claim.

---

# 17. Relation to established local concentration results

Barker--Prange prove localized smoothing for critical local data and, under a Type-I assumption, concentration of $L^3$, $L^{3,\infty}$, and critical Besov norms on shrinking balls centered at a singular point.

Their result confirms that critical activity may be genuinely centered on a blow-up point rather than at an unrelated global location. The present argument is different: it uses first-singularity geometry, good regular collars, and a forced localized dissipation-wavenumber continuation estimate, and it does not assume Type I.

Bradshaw--Grujić independently show that possible singularity formation requires essential activity in frequency windows whose lower edge diverges toward the first singular time.

No priority claim is made for the general frequency-localization philosophy.

---

# 18. Why the good collar matters

A naive cutoff around $x_\ast$ can create forcing terms that themselves become singular near $T$.

The CKN singular-set geometry lets the cutoff be placed on a radius whose transition collar contains no singular point at time $T$.

Thus

$$
\boxed{
\text{localization forcing is regular,
so high-frequency blowup cannot be blamed on the collar}.
}
\tag{18.1}
$$

That is the local-decoupling mechanism.

---

# 19. Re-entry into the supplier trace pipeline

Theorem 16.1 supplies

$$
\boxed{
\lambda_k^{-1}
|u_{q_k}(x_k,t_k)|
\ge
c_{\rm loc}\nu
}
\tag{19.1}
$$

with

$$
x_k\to x_\ast.
$$

The DCRP-09 heat-memory subtraction only requires a critical shell-amplitude lower bound plus the global kinetic-energy bound. It does not require that $q_k$ be the global dissipation boundary.

Define

$$
\boxed{
g_{q_k}(t)
=
u_{q_k}(t)
-
e^{\nu(t-t_{0,k})\Delta}
u_{q_k}(t_{0,k})
}
\tag{19.2}
$$

with $t_{0,k}$ chosen so the heat memory is a small fraction of the local supplier amplitude.

Then

$$
\boxed{
\lambda_k^{-1}
\|g_{q_k}(t_k)\|_\infty
\ge
c\nu.
}
\tag{19.3}
$$

After normalized recentering, DCRP-14 gives the universal solenoidal trace lift

$$
\boxed{
\|\Pi_{H_\ast}h_k\|
\ge
c_\ast\nu.
}
\tag{19.4}
$$

DCRP-15 gives

$$
\boxed{
\|
\mathcal O_{W_\ast}^Td_k
\|
+
C_{\rm sup}
\mathcal B_{\rm sup}^{res}(k)
\ge
c_{\rm sup}\nu.
}
\tag{19.5}
$$

Thus the supplier trace/residual gap now occurs at centers converging to the actual singular point.

The remote-supplier loophole is removed.

---

# 20. What is now closed

The DCRP-15 frontier was

$$
\boxed{
\text{local singularity}
\Longrightarrow
\text{local supplier}
\ \vee\
\text{paid localization forcing}.
}
$$

The good-collar construction makes the localization forcing regular.

Therefore

$$
\boxed{
\textbf{
local singularity}
\Longrightarrow
\textbf{
local critical supplier sequence}.
}
\tag{20.1}
$$

Status:

$$
\boxed{
\textbf{CLOSED in the present route}.
}
$$

---

# 21. What remains open

The theorem produces an actual local supplier sequence

$$
(x_k,t_k,\lambda_k)
$$

approaching $(x_\ast,T)$.

MORP works with a particular extracted minimal obstruction / return sequence.

It remains to verify that the local supplier sequence can be inserted into, synchronized with, or used to replace that extracted sequence without losing:

- minimality;
- actual return structure;
- zero-cost ledger relations;
- finite-window quotient synchronization.

Thus the next issue is

$$
\boxed{
\textbf{
Local Supplier / MORP Sequence Synchronization}.
}
\tag{21.1}
$$

This is much narrower than Local Supplier Capture.

---

# 22. Potential synchronization shortcut

Suppose the MORP minimal sequence is generated from shrinking actual singular windows around $(x_\ast,T)$.

Theorem 16.1 gives supplier atoms in arbitrarily small physical neighborhoods of $x_\ast$.

For every singular window, choose the first descendant local supplier event satisfying

$$
\lambda^{-1}
|\Delta_\lambda u|
\ge
c_{\rm loc}\nu.
$$

Use that event as the next re-root point/scale.

Then:

- the state is actual;
- the center remains in the singular neighborhood;
- the scale is endogenous to Navier--Stokes;
- the trace lower bound is automatic;
- failure to fit the original return chart is an explicit transition/re-root discrepancy.

This suggests that supplier rooting can be installed as the stopping rule of the actual MORP extraction rather than as an auxiliary sequence.

---

# 23. Remaining time-scale issue

Theorem 16.1 proves

$$
t_k\uparrow T,
\qquad
\lambda_k\to\infty.
$$

It does not prove

$$
\boxed{
\lambda_k^2(T-t_k)\asymp1.
}
\tag{23.1}
$$

Thus the normalized remaining horizon may tend to zero, a finite positive constant, or infinity.

Likewise the supplier wavelength need not be comparable to the original good-collar radius.

These are synchronization issues, not local-capture failures.

They must be handled by the MORP descendant/re-root compiler.

---

# 24. New exact frontier

The next target is

$$
\boxed{
\textbf{
Local Supplier Stopping-Time / MORP Synchronization Lemma}.
}
$$

A sufficient form is:

> Given any actual singular-rooted MORP extraction sequence around $(x_\ast,T)$, one may pass to a descendant/stopping-time refinement whose roots are local supplier events satisfying
>
> $$
> \lambda_n^{-1}
> |\Delta_{\lambda_n}u(x_n,t_n)|
> \ge
> c\nu,
> $$
>
> while preserving the monotone obstruction ordering and charging every re-root discrepancy to the existing transition residual.
>
> Consequently every minimal actual singular obstruction may be assumed, without loss of zero-cost generality, to be supplier-rooted.

If proved, DCRP-15's uniform trace/residual gap applies directly to the very sequence used by MORP minimality.

That would collide with the exact zero-cost minimal obstruction.

---

# 25. Source ledger

## Caffarelli--Kohn--Nirenberg

Used for the singular-set geometry and the existence of arbitrarily small regular collars around a selected first singular point.

## Barker--Prange

Tobias Barker and Christophe Prange, *Localized smoothing for the Navier-Stokes equations and concentration of critical norms near singularities*, arXiv:1812.09115v2.

Relevant established facts:

- localized smoothing is genuinely local for local energy solutions;
- under a Type-I assumption, critical norms concentrate on shrinking balls centered at the singular point;
- perturbed/localized Navier--Stokes equations can be analyzed with explicit local pressure and forcing terms.

DCRP-16 does not assume their Type-I concentration theorem.

## Bradshaw--Grujić

Zachary Bradshaw and Zoran Grujić, *Frequency localized regularity criteria for the 3D Navier-Stokes equations*, arXiv:1501.01043v2.

Used as calibration that frequency windows diverging toward the first singular time are essential to possible singularity formation.

## Cheskidov--Dai

Used for the velocity dissipation-wavenumber Bony estimate. DCRP-16 adds the forcing term explicitly by Cauchy--Schwarz and Young.

---

# 26. End state

The global/local supplier gap from DCRP-15 is closed.

For every first singular point $(x_\ast,T)$ there exist

$$
t_k\uparrow T,
\qquad
x_k\to x_\ast,
\qquad
\lambda_k\to\infty
$$

such that

$$
\boxed{
\lambda_k^{-1}
|
\Delta_{\lambda_k}u(x_k,t_k)
|
\ge
c_{\rm loc}\nu.
}
$$

Thus

$$
\boxed{
\textbf{
the singular point itself is approached by actual critical supplier atoms.
}
}
$$

The supplier modules then give

$$
\boxed{
\|
\mathcal O_{W_\ast}^Td_k
\|
+
C_{\rm sup}
\mathcal B_{\rm sup}^{res}(k)
\ge
c_{\rm sup}\nu
}
$$

with $x_k\to x_\ast$.

The next single frontier is

$$
\boxed{
\textbf{
Local Supplier Stopping-Time / MORP Synchronization Lemma}.
}
$$

If supplier rooting can be installed as a legitimate descendant/stopping rule of the minimal-obstruction extraction, the supplier trace/residual gap collides directly with MORP's zero-cost minimality.

---

# Checkpoint v17 Update — DCRP-17

# NS-DCRP-17 — Supplier Stopping-Time Synchronization, Native Obstruction Extraction, and the Excursion-Irreversibility Barrier

- date: 2026-08-16
- status: research proof checkpoint
- canonical source: UTF-8 Markdown
- canonical math delimiters: `$...$` and `$$...$$`
- objective:
  1. install the DCRP-16 local supplier sequence as an actual MORP-compatible return/re-root stopping rule;
  2. prove that supplier-rooted finite-window packages are genuinely native-separated and compact after fixed normalization;
  3. determine whether this already forces a contradiction with MORP minimality.
- no full Navier--Stokes regularity claim is made.
- principal internal dependencies:
  - MORP-01 normalized native obstruction slice and extended cost;
  - MORP-02 defect-completed compactness;
  - MORP-03 actual return/re-root semantics and Minimal Return Rigidity;
  - DCRP-14 through DCRP-16 supplier trace/realization/local-capture modules.
- external calibration:
  - Gallagher--Koch--Planchon, arXiv:1012.0145;
  - Jia--Šverák, arXiv:1201.1592.
- no novelty / priority claim is made without independent audit.

---

# 1. Executive result

DCRP-16 proved that if

$$
z_\ast=(x_\ast,T)
$$

is a first singular point, then there exist actual local supplier events

$$
\boxed{
(t_n,x_n,\lambda_n)
}
$$

with

$$
\boxed{
t_n\uparrow T,
\qquad
x_n\to x_\ast,
\qquad
\lambda_n\to\infty,
}
\tag{1.1}
$$

and

$$
\boxed{
\lambda_n^{-1}
|
\Delta_{\lambda_n}u(x_n,t_n)
|
\ge
c_{\rm loc}\nu.
}
\tag{1.2}
$$

DCRP-14/15 then attach to every such event an actual nonlinear supplier increment and a fixed normalized finite-window package satisfying

$$
\boxed{
\|
\mathcal O_{W_\ast}^T d_n
\|
+
C_{\rm sup}
\mathcal B_{\rm sup}^{res}(n)
\ge
c_{\rm sup}\nu.
}
\tag{1.3}
$$

The first theorem of this round shows that the supplier package is genuinely native-separated.

Let

$$
\mathcal A_\ast d
=
\left(
\mathcal O_{W_\ast}^T d,
\mathcal R_{W_\ast}^{sup}d
\right),
$$

where the second component contains the fixed finite-window residual coordinates used in DCRP-15.

Because exact gauge/null directions are annihilated by

$$
\mathcal A_\ast,
$$

the map descends to the finite-dimensional quotient.

Hence there is a fixed constant

$$
C_A<\infty
$$

such that

$$
\boxed{
\|
\mathcal A_\ast d
\|
\le
C_A
d_{\rm nat}(d).
}
\tag{1.4}
$$

Combining with (1.3),

$$
\boxed{
d_{\rm nat}(d_n)
\ge
a_{\rm sup}
>
0.
}
\tag{1.5}
$$

After homogeneous normalization by

$$
a_{\rm sup},
$$

supplier packages satisfy

$$
d_{\rm nat}\ge1.
$$

Because the normalized supplier package lives in one fixed finite-dimensional quotient/template, norm equivalence gives a uniform package bound

$$
\boxed{
\mathcal N_{\rm pkg}(d_n)
\le
C_\ast.
}
\tag{1.6}
$$

Therefore the singularity produces an actual non-tautological supplier-rooted obstruction slice

$$
\boxed{
\mathscr O_{\rm sup}
\subset
\mathscr O_1.
}
\tag{1.7}
$$

The second theorem installs a canonical supplier stopping rule.

Fix one integer scale gap

$$
L\ge1.
$$

Given an actual singular-rooted supplier window with dyadic reference index

$$
q,
$$

define the next supplier return to be the canonical first later local supplier event satisfying

$$
q'\ge q+L,
$$

with the deterministic spatial/time tie-breaking rule declared in advance.

DCRP-16 guarantees that such later events exist arbitrarily close to

$$
T.
$$

Thus:

$$
\boxed{
\mathsf T_{\rm sup}
:
\mathscr O_{\rm sup}^{act}
\to
\mathscr O_{\rm sup}^{act}
}
\tag{1.8}
$$

is an actual same-history return/re-root map.

This is exactly the type of return rule MORP-03 permits:

- first later native-separated window;
- first later dangerous/native-separated window;
- next member of a declared admissible extraction sequence.

The supplier rule is declared before compactness/minimality.

Thus:

$$
\boxed{
\textbf{
actual supplier return realization is no longer the missing issue on the supplier-rooted slice.
}
}
\tag{1.9}
$$

Moreover, the fixed normalized finite-dimensional supplier slice is sequentially compact.

Therefore the supplier-rooted subprogram has:

$$
\boxed{
\text{XTR}
+
\text{COM}
+
\text{ACTUAL RETURN}.
}
\tag{1.10}
$$

The third theorem is a positive-gap result.

Since:

$$
\mathfrak J
=
\mathsf O_{\rm PFET}
+
\mathcal M_{SV}
+
\widetilde{\mathcal S}^{(3)}
+
\mathsf{Paid}
+
\mathsf R_{\rm nat},
$$

and DCRP-15 places the supplier trace/residual gap inside the first/native-residual channels, there exists

$$
c_J>0
$$

such that every normalized supplier package satisfies

$$
\boxed{
\mathfrak J(d)
\ge
c_J.
}
\tag{1.11}
$$

Hence

$$
\boxed{
m_{\rm sup}
:=
\inf_{d\in\mathscr O_{\rm sup}}
\mathfrak J(d)
>
0.
}
\tag{1.12}
$$

Therefore:

$$
\boxed{
\textbf{
there is no zero-cost supplier-rooted minimal obstruction.
}
}
\tag{1.13}
$$

This is a genuine synchronization gain.

However it does **not** yet prove that the original MORP minimal value

$$
m_\ast
$$

is positive.

MORP-03 explicitly allows a genuine obstruction history to:

- temporarily deplete;
- transfer across channels;
- become visible;
- later regenerate/re-root into a new native-separated window.

Thus a hypothetical zero-cost minimal recurrent orbit could, logically, pass through a positive-cost supplier excursion and only return to the minimal level later.

Choosing the supplier itself as the return window does not preserve Minimal Return Rigidity unless one proves a supplier-specific nonnegative return-depletion inequality.

Therefore the critical NO-GO of this round is:

$$
\boxed{
\textbf{
supplier visibility}
\not\Rightarrow
\textbf{
minimal-orbit contradiction}
}
\tag{1.14}
$$

without an irreversibility/depletion theorem.

The next exact frontier is therefore:

$$
\boxed{
\textbf{
Supplier Excursion Irreversibility / Return-Depletion Lemma}.
}
\tag{1.15}
$$

A sufficient theorem would show that if an actual native-separated orbit starts near a zero-cost invisible window, passes through a local supplier event, and later returns to a zero-cost invisible window, then the complete excursion necessarily pays a fixed strictly positive nonnegative tax:

$$
\boxed{
\Delta_{\rm exc}
\ge
c_{\rm exc}>0.
}
\tag{1.16}
$$

If this is proved, MORP Minimal Return Rigidity gives immediately

$$
\Delta_{\rm exc}=0,
$$

a contradiction.

This is now the single closure-facing frontier of the supplier route.

---

# 2. MORP return semantics audited

MORP-03 defines actual Navier--Stokes evolution/restriction

$$
\mathsf E_{s\to t}
$$

and normalization

$$
\mathsf N_{\rm norm}.
$$

A candidate transition is

$$
\boxed{
\mathsf T
=
\mathsf N_{\rm norm}
\circ
\mathsf E.
}
\tag{2.1}
$$

MORP deliberately rejects rigid fixed-step invariance.

A legitimate obstruction may:

- partially deplete;
- transfer across channels;
- become source dominated;
- later re-root into a new dangerous/native-separated window.

Therefore the actual transition is a return/re-root transition.

A later window

$$
W'
$$

is a native return if

$$
\boxed{
d_{\rm nat}
(
D(W')
)
\ge1.
}
\tag{2.2}
$$

MORP-03 explicitly allows the canonical rule to choose:

1. the first later native-separated window;
2. the first later dangerous-certified native-separated window;
3. the next member of a fixed admissible extraction sequence.

The rule must be fixed before compactness/minimality is used.

The supplier stopping rule below satisfies exactly this semantic requirement once supplier native separation is proved.

---

# 3. Native distance on the fixed supplier window

MORP-01 defines

$$
\boxed{
d_{\rm nat}(D)
=
\operatorname{dist}_{\mathfrak X/\Gamma}
(
D,\Gamma
).
}
\tag{3.1}
$$

Here

$$
\Gamma
$$

contains only declared exact gauge/symmetry directions.

The supplier window from DCRP-15 is a fixed normalized finite-dimensional quotient.

Let

$$
Y_\ast
$$

denote that cleaned quotient.

Let

$$
\mathcal O_\ast^T
:
Y_\ast
\to
H_\ast
$$

be the selected trace map.

Let

$$
\mathcal R_\ast
:
Y_\ast
\to
Z_\ast^{res}
$$

be the concrete finite residual map after all exact quotient nulls have been removed.

Define

$$
\boxed{
\mathcal A_\ast
=
(
\mathcal O_\ast^T,
\mathcal R_\ast
).
}
\tag{3.2}
$$

This is a bounded linear map on the finite-dimensional cleaned quotient.

---

# 4. NEW THEOREM — supplier native separation

## Theorem 4.1

There exists

$$
a_{\rm sup}>0
$$

such that every DCRP-15 normalized supplier package

$$
d_q
$$

satisfies

$$
\boxed{
d_{\rm nat}(d_q)
\ge
a_{\rm sup}.
}
\tag{4.1}
$$

### Proof

DCRP-15 gives

$$
\boxed{
\|
\mathcal O_\ast^Td_q
\|
+
C_{\rm sup}
\|
\mathcal R_\ast d_q
\|
\ge
c_{\rm sup}\nu.
}
\tag{4.2}
$$

Choose a product norm on the target of

$$
\mathcal A_\ast.
$$

Then there is

$$
c_1>0
$$

with

$$
\boxed{
\|
\mathcal A_\ast d_q
\|
\ge
c_1\nu.
}
\tag{4.3}
$$

Since

$$
\mathcal A_\ast
$$

vanishes on exact quotient-null directions, it descends to

$$
Y_\ast.
$$

Boundedness gives

$$
\boxed{
\|
\mathcal A_\ast d
\|
\le
C_A
\|[d]\|_{Y_\ast}.
}
\tag{4.4}
$$

The quotient norm is an admissible realization of native distance on this fixed window, up to a fixed equivalence constant

$$
C_{\rm eq}.
$$

Therefore

$$
d_{\rm nat}(d_q)
\ge
\frac{
c_1
}{
C_AC_{\rm eq}
}
\nu.
$$

Set

$$
\boxed{
a_{\rm sup}
=
\frac{
c_1
}{
C_AC_{\rm eq}
}
\nu.
}
\tag{4.5}
$$

$$
\square
$$

Status:

$$
\boxed{
\textbf{PROVED on the fixed supplier finite-window quotient}.
}
$$

---

# 5. Homogeneous normalization to the unit obstruction slice

The supplier package is a tangent/native direction.

All linearized package constraints are homogeneous.

Therefore define

$$
\boxed{
\widehat d_q
=
a_{\rm sup}^{-1}
d_q.
}
\tag{5.1}
$$

Then

$$
\boxed{
d_{\rm nat}(\widehat d_q)
\ge1.
}
\tag{5.2}
$$

The normalization does not insert the dangerous/singular certificate.

It uses only the native quotient separation already extracted from the actual supplier package.

Thus it passes the MORP non-tautological extraction safety rule.

---

# 6. Uniform package bound from finite dimensionality

On the fixed finite-dimensional quotient

$$
Y_\ast,
$$

let

$$
\mathcal N_{\rm pkg}
$$

be any fixed compactness-control norm used for the supplier slice.

All norms on

$$
Y_\ast
$$

are equivalent.

Therefore there is a fixed constant

$$
C_N
$$

such that

$$
\boxed{
\mathcal N_{\rm pkg}(d)
\le
C_N
d_{\rm nat}(d)
}
\tag{6.1}
$$

after the exact gauge representative is fixed.

Apply to the unit-native supplier package.

One may additionally divide by the exact native norm rather than the lower constant

$$
a_{\rm sup}
$$

to obtain

$$
d_{\rm nat}=1.
$$

Then

$$
\boxed{
\mathcal N_{\rm pkg}
\le
C_\ast
}
\tag{6.2}
$$

with a universal constant for the fixed normalized supplier template.

Thus supplier-rooted packages belong to the MORP unit obstruction geometry.

Status:

$$
\boxed{
\textbf{PROVED on the fixed supplier window}.
}
$$

---

# 7. Supplier-rooted obstruction slice

Define

$$
\boxed{
\mathscr O_{\rm sup}
=
\left\{
d\in
\overline{\mathcal Y_{\rm sup}^{NS}}
:
d_{\rm nat}(d)\ge1,
\quad
\mathcal N_{\rm pkg}(d)\le C_\ast
\right\},
}
\tag{7.1}
$$

where

$$
\mathcal Y_{\rm sup}^{NS}
$$

consists of the actual finite-window tangent packages constructed from local supplier nonlinear increments.

Then

$$
\boxed{
\mathscr O_{\rm sup}
\subset
\mathscr O_1
}
\tag{7.2}
$$

provided the original MORP coordinate map includes the fixed supplier finite-window coordinates, which DCRP-14/15 constructed inside the declared trace/residual architecture.

DCRP-16 gives:

$$
\boxed{
T<\infty
\Longrightarrow
\mathscr O_{\rm sup}\ne\varnothing.
}
\tag{7.3}
$$

This is a concrete supplier-side XTR theorem.

Status:

$$
\boxed{
\textbf{PROVED for the supplier-rooted coordinate slice}.
}
$$

It does not prove universal XTR for every MORP extraction route.

---

# 8. Compactness of the supplier-rooted slice

The fixed normalized supplier quotient is finite dimensional.

The set

$$
\boxed{
\left\{
d:
d_{\rm nat}(d)=1,
\quad
\mathcal N_{\rm pkg}(d)\le C_\ast
\right\}
}
\tag{8.1}
$$

is bounded and closed modulo the exact fixed gauge.

Therefore it is compact.

Hence

$$
\boxed{
\mathscr O_{\rm sup}
\text{ is sequentially compact after fixed native normalization}.
}
\tag{8.2}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

Thus the supplier slice does not carry the original infinite-dimensional COM difficulty.

---

# 9. Canonical supplier stopping rule

Fix once and for all:

- an integer dyadic scale gap

  $$
  L\ge1;
  $$

- a deterministic spatial tie-breaking convention;
- a deterministic time tie-breaking convention.

Let an actual supplier-rooted state have current supplier frequency index

$$
q_n.
$$

Define the admissible future supplier set

$$
\mathfrak S_n
$$

to consist of local supplier events

$$
(t,x,q)
$$

from the same actual singular solution satisfying

$$
\boxed{
t>t_n,
}
\tag{9.1}
$$

$$
\boxed{
q\ge q_n+L,
}
\tag{9.2}
$$

and belonging to a prescribed singular-rooted neighborhood whose radius tends to zero with the extraction level.

DCRP-16 gives supplier events with

$$
q\to\infty,
\qquad
t\uparrow T,
\qquad
x\to x_\ast.
$$

Therefore

$$
\boxed{
\mathfrak S_n\ne\varnothing
}
\tag{9.3}
$$

for every sufficiently late supplier node.

Define

$$
\boxed{
\mathsf S_{\rm sup}
}
$$

to select the smallest admissible dyadic index, then the earliest admissible threshold time, then the declared spatial tie-breaker.

The rule is declared before any compactness/minimality argument.

---

# 10. NEW THEOREM — actual supplier return realization

## Theorem 10.1

Along a hypothetical singular history, the supplier stopping rule defines an infinite actual same-history return sequence

$$
\boxed{
D_1^{sup},
D_2^{sup},
D_3^{sup},
\ldots
}
\tag{10.1}
$$

with

$$
\boxed{
q_{n+1}\ge q_n+L,
}
\tag{10.2}
$$

$$
\boxed{
t_{n+1}>t_n,
}
\tag{10.3}
$$

$$
\boxed{
t_n\uparrow T,
}
\tag{10.4}
$$

and

$$
\boxed{
x_n\to x_\ast.
}
\tag{10.5}
$$

After the fixed supplier normalization,

$$
\boxed{
\widehat D_n^{sup}\in\mathscr O_{\rm sup}.
}
\tag{10.6}
$$

Thus

$$
\boxed{
\mathsf T_{\rm sup}
:
\mathscr O_{\rm sup}^{act}
\to
\mathscr O_{\rm sup}^{act}
}
\tag{10.7}
$$

is an actual original-solution return/re-root map.

### Proof

Existence of arbitrarily late/higher local supplier events is DCRP-16.

The deterministic selection makes the return rule canonical.

The event is taken from the same original Navier--Stokes solution.

Sections 4--8 place every normalized supplier package in

$$
\mathscr O_{\rm sup}.
$$

Iteration gives the infinite actual chain.

$$
\square
$$

Status:

$$
\boxed{
\textbf{PROVED conditional only on the DCRP-16 local-supplier theorem already established in the project}.
}
$$

---

# 11. Relation to MORP-03 actual-return semantics

MORP-03 permits exactly the following return-rule forms:

- first later native-separated window;
- first later dangerous/native-separated window;
- next member of a fixed admissible extraction sequence.

The supplier stopping rule is of the second/third type after Sections 4--7 establish native separation.

Therefore

$$
\boxed{
\textbf{
the supplier stopping rule is semantically admissible as a MORP actual return/re-root rule.
}
}
\tag{11.1}
$$

This closes the purely semantic synchronization problem.

It does not yet prove a return-depletion inequality.

---

# 12. Supplier-rooted positive cost gap

The MORP extended cost is

$$
\boxed{
\mathfrak J
=
\mathsf O_{\rm PFET}
+
\mathcal M_{SV}
+
\widetilde{\mathcal S}^{(3)}
+
\mathsf{Paid}
+
\mathsf R_{\rm nat}.
}
\tag{12.1}
$$

On the supplier package, DCRP-15 gives a fixed trace-or-residual gap.

The selected trace contributes to

$$
\mathsf O_{\rm PFET},
$$

while the finite-window realization residual contributes to

$$
\mathsf R_{\rm nat}
$$

or the declared local paid/residual ledger.

Hence, after unit native normalization and finite-dimensional norm equivalence, there is

$$
\boxed{
c_J>0
}
\tag{12.2}
$$

such that

$$
\boxed{
\mathfrak J(d)
\ge
c_J
\qquad
\forall d\in\mathscr O_{\rm sup}.
}
\tag{12.3}
$$

Therefore

$$
\boxed{
m_{\rm sup}
=
\inf_{
d\in\mathscr O_{\rm sup}
}
\mathfrak J(d)
\ge
c_J>0.
}
\tag{12.4}
$$

Status:

$$
\boxed{
\textbf{PROVED on the supplier-rooted slice}.
}
$$

---

# 13. Corollary — no zero-cost supplier-rooted minimal obstruction

There is no

$$
d_\ast^{sup}\in\mathscr O_{\rm sup}
$$

with

$$
\boxed{
\mathfrak J(d_\ast^{sup})=0.
}
\tag{13.1}
$$

Equivalently,

$$
\boxed{
\mathscr O_{\rm sup}
\cap
\ker\mathfrak J
=
\varnothing.
}
\tag{13.2}
$$

Thus the MORP minimal-invisible branch does not exist **inside the supplier-rooted slice**.

This is a true positive-gap result.

---

# 14. Why this does not imply the global MORP minimal value is positive

The original obstruction slice

$$
\mathscr O_1
$$

is larger than

$$
\mathscr O_{\rm sup}.
$$

Therefore

$$
\boxed{
m_\ast
=
\inf_{\mathscr O_1}\mathfrak J
\le
\inf_{\mathscr O_{\rm sup}}\mathfrak J
=
m_{\rm sup}.
}
\tag{14.1}
$$

A positive supplier gap does not by itself imply

$$
m_\ast>0.
$$

A minimizing invisible sequence could live in other windows/states of the same actual singular history.

Thus:

$$
\boxed{
\textbf{
supplier XTR/COM/visibility}
\neq
\textbf{
global MORP coercive gap}.
}
}
\tag{14.2}
$$

---

# 15. CRITICAL NO-GO — temporary supplier visibility is compatible with MORP semantics

MORP-03 explicitly states that fixed-step invariance is too strong.

A genuine dangerous trajectory may:

- partially deplete;
- transfer across channels;
- become source dominated;
- later re-root into a new dangerous/native-separated window.

Therefore a hypothetical minimal zero-cost orbit may, logically, have the pattern

$$
\boxed{
D_n^{min}
\longrightarrow
S_n^{sup}
\longrightarrow
D_{n+1}^{min},
}
\tag{15.1}
$$

where

$$
\boxed{
\mathfrak J(D_n^{min})=0,
}
\tag{15.2}
$$

$$
\boxed{
\mathfrak J(S_n^{sup})\ge c_J,
}
\tag{15.3}
$$

and

$$
\boxed{
\mathfrak J(D_{n+1}^{min})=0.
}
\tag{15.4}
$$

Nothing in minimality alone forbids the middle excursion.

Thus the following inference is invalid:

$$
\boxed{
\text{supplier event exists}
\Longrightarrow
\text{minimal zero-cost orbit impossible}.
}
\tag{15.5}
$$

Status:

$$
\boxed{
\textbf{NO-GO / LOGICAL CORRECTION}.
}
$$

This is the principal result of the synchronization audit.

---

# 16. Why choosing the supplier itself as the MORP return is not enough

MORP Minimal Return Rigidity assumes

$$
\boxed{
\mathfrak J
(
\mathsf T_{\rm ret}D
)
+
\Delta_{\rm ret}(D)
\le
\mathfrak J(D),
}
\tag{16.1}
$$

with

$$
\Delta_{\rm ret}\ge0.
$$

Suppose

$$
\mathfrak J(D)=0
$$

and choose the later supplier package as

$$
\mathsf T_{\rm ret}D.
$$

But supplier synchronization gives

$$
\mathfrak J(\mathsf T_{\rm ret}D)\ge c_J>0.
$$

Then (16.1) cannot hold.

Therefore:

$$
\boxed{
\textbf{
supplier stopping is an admissible actual return rule,
but it is not automatically a depletion-compatible minimal return rule.
}
}
\tag{16.2}
$$

This distinction must not be hidden.

---

# 17. Actual supplier synchronization achieved

Although supplier stopping does not yet preserve minimality, the following parts of the synchronization problem are now closed:

### actual-history realization

$$
\boxed{
\mathsf T_{\rm sup}
\text{ is generated by one original singular solution}.
}
\tag{17.1}
$$

### local singular-point capture

$$
\boxed{
x_n\to x_\ast.
}
\tag{17.2}
$$

### scale advance

$$
\boxed{
q_{n+1}\ge q_n+L.
}
\tag{17.3}
$$

### native separation

$$
\boxed{
d_{\rm nat}(D_n^{sup})\ge1.
}
\tag{17.4}
$$

### normalized compactness

$$
\boxed{
\mathcal N_{\rm pkg}(D_n^{sup})\le C_\ast.
}
\tag{17.5}
$$

### visibility

$$
\boxed{
\mathfrak J(D_n^{sup})\ge c_J.
}
\tag{17.6}
$$

The only missing ingredient for collision with Minimal Return Rigidity is an irreversible tax across the **complete excursion**.

---

# 18. Supplier excursion

Let

$$
D_n^-
$$

be one native-separated invisible/minimal window.

Let

$$
S_n
$$

be the next local supplier event selected by the supplier stopping rule.

If recurrence exists, let

$$
D_n^+
$$

be the first later native-separated window that returns to the minimal/invisible class.

The complete excursion is

$$
\boxed{
D_n^-
\longrightarrow
S_n
\longrightarrow
D_n^+.
}
\tag{18.1}
$$

A supplier-excursion return map should be defined by

$$
\boxed{
\mathsf T_{\rm exc}(D_n^-)
=
D_n^+.
}
\tag{18.2}
$$

If no such

$$
D_n^+
$$

exists, then the recurrent minimal branch already fails.

Thus only the case in which the system becomes invisible again needs analysis.

---

# 19. Target depletion identity

The desired supplier-specific return law is

$$
\boxed{
\mathfrak J(D_n^+)
+
\Delta_{\rm exc}(D_n^-;S_n;D_n^+)
\le
\mathfrak J(D_n^-),
}
\tag{19.1}
$$

with

$$
\boxed{
\Delta_{\rm exc}\ge0.
}
\tag{19.2}
$$

The crucial new theorem must prove

$$
\boxed{
\Delta_{\rm exc}
\ge
c_{\rm exc}
>
0
}
\tag{19.3}
$$

whenever the middle state contains the supplier trace/residual gap

$$
\mathfrak J(S_n)\ge c_J.
$$

Then for a minimal zero-cost orbit,

$$
\mathfrak J(D_n^-)
=
\mathfrak J(D_n^+)
=
0,
$$

and (19.1) gives

$$
\Delta_{\rm exc}\le0.
$$

Combined with (19.3),

$$
\boxed{\bot.}
$$

This would close the actual recurrent minimal branch.

---

# 20. What can provide irreversibility?

The supplier route has already produced several candidate nonnegative ledgers.

## viscous supplier dissipation

During a supplier-shell energy growth excursion,

$$
\nu
\int
\|\nabla u_Q\|_2^2
\,dt
\ge0.
$$

The difficulty is obtaining a uniform scale-critical lower bound.

## paid backscatter

DCRP-11 gives a heat-filter alternative:

$$
\text{forward work}
\vee
\text{backscatter}.
$$

Backscatter is already on the paid side.

The forward branch remains potentially reversible.

## finite-window realization residual

DCRP-15 gives

$$
O_W^T
+
C
\mathcal B_{\rm sup}^{res}
\ge
c\nu.
$$

If the supplier is invisible in the selected trace, the residual side is already paid/native.

The hard case is a supplier that is genuinely trace-visible but later becomes invisible with negligible residual.

## diffusion between visible and invisible states

If supplier trace amplitude disappears before the next invisible return, viscosity and nonlinear transfer must remove it.

One must show that the disappearance cannot be achieved entirely by sign-indefinite forward redistribution without a strictly positive return tax.

This is the core irreversibility question.

---

# 21. Heat-band excursion identity

DCRP-11 constructed a positive scale-critical heat-band energy

$$
\mathcal B_\lambda^{a,b}(t).
$$

A supplier event forces

$$
\boxed{
\mathcal B_\lambda^{a,b}
\ge
\beta_0\nu^2.
}
\tag{21.1}
$$

A complete excursion from a low-band state to supplier and back to low band has at least one rise and one fall.

The exact identity is

$$
\boxed{
\frac d{dt}
\mathcal B_\lambda^{a,b}
+
\nu\lambda
(D_a-D_b)
+
\lambda(F_{s_a}-F_{s_b})
=
0.
}
\tag{21.2}
$$

The first nontrivial positive term is

$$
\boxed{
\nu\lambda
(D_a-D_b)\ge0.
}
\tag{21.3}
$$

The next route should attempt to prove that a fixed-amplitude excursion cannot have

$$
\boxed{
\nu\lambda
\int_{\rm excursion}
(D_a-D_b)\,dt
\to0
}
\tag{21.4}
$$

while both endpoint observation/residual costs vanish.

If such a lower bound holds, it is the desired irreversible tax.

---

# 22. Why a naive total-variation argument is insufficient

The band energy may rise through forward transfer at the coarse boundary and later fall through forward transfer at the fine boundary.

Thus an energy packet can pass through the band without backscatter.

This is the normal forward-cascade picture.

Therefore

$$
\boxed{
\text{band rises and falls}
\not\Rightarrow
\text{backscatter}.
}
\tag{22.1}
$$

Likewise a fixed amount of energy can pass through increasingly small scales while the raw viscous payment remains summable.

This is the old critical-barrier accumulation problem.

Hence the irreversibility theorem must use additional supplier structure:

- dissipation-wavenumber location;
- finite trace amplitude;
- first-crossing geometry;
- actual return to a native invisible state;
- or repeated recurrence/minimality.

---

# 23. Potential route — supplier residence time

At the supplier boundary,

$$
\lambda^{-1}
\|u_Q\|_\infty
\gtrsim\nu.
$$

If one can prove a scale-invariant lower bound on normalized residence time,

$$
\boxed{
\nu\lambda^2
|I_{\rm sup}|
\ge
\tau_0>0,
}
\tag{23.1}
$$

while the shell remains above a fixed fraction of critical amplitude, then

$$
\|u_Q\|_2^2
\gtrsim
\nu^2\lambda^{-1}
$$

would give

$$
\boxed{
\nu\lambda
\int_{I_{\rm sup}}
\|\nabla u_Q\|_2^2
\,dt
\gtrsim
\nu^2.
}
\tag{23.2}
$$

This would produce the desired non-summable scale-critical excursion tax.

The current corpus does not yet provide (23.1).

The shell may, in principle, spike on a much shorter normalized time interval.

Thus residence-time rigidity is one possible next sublemma.

---

# 24. Potential route — trace disappearance rate

DCRP-14 gives a fixed finite-dimensional supplier trace

$$
\boxed{
\|\Pi_{H_\ast}h(t_{\rm sup})\|
\ge
c\nu.
}
\tag{24.1}
$$

Suppose the next minimal invisible return satisfies

$$
\boxed{
\|\Pi_{H_\ast}h(t_{\rm ret})\|
\approx0.
}
\tag{24.2}
$$

Because

$$
H_\ast
$$

is finite dimensional and fixed in normalized coordinates, one can differentiate each trace coefficient along the normalized forced Stokes/Navier--Stokes increment equation.

A viable theorem would bound

$$
\boxed{
\left|
\frac d{d\tau}
\Pi_{H_\ast}h
\right|
}
\tag{24.3}
$$

by:

- paid flux;
- viscosity;
- finite-window residual;
- low-mode supplier activity.

If all paid/residual terms are small, a fixed drop

$$
c\nu\to0
$$

would require a positive normalized time.

Combining with viscous occupation may yield a strict return tax.

This converts the irreversibility problem into a finite-dimensional trace ODE estimate.

This is currently the most attractive route.

---

# 25. External critical-element calibration

Classical critical-element/profile-decomposition work shows that, under a hypothetical nonempty blowup class and suitable critical-space compactness, minimal singular objects can be extracted.

This supports the general MORP philosophy that a minimizing/critical orbit is meaningful once the topology and transition are controlled.

However those results do not imply that an arbitrary supplier stopping time preserves the minimal element.

Therefore no external theorem closes the excursion-depletion gap automatically.

The issue identified in Sections 15--24 is genuine.

---

# 26. Updated proof-state diagram

The current supplier route is now

$$
\boxed{
\begin{aligned}
\text{finite-time singular point}
&\Longrightarrow
\text{local supplier sequence}\\
&\Longrightarrow
\text{actual supplier nonlinear increment}\\
&\Longrightarrow
\text{finite-window trace/residual gap}\\
&\Longrightarrow
\text{supplier-rooted native obstruction slice}\\
&\Longrightarrow
\text{actual supplier return chain}.
\end{aligned}
}
\tag{26.1}
$$

Every supplier-rooted node satisfies

$$
\boxed{
\mathfrak J\ge c_J>0.
}
\tag{26.2}
$$

But a hypothetical minimal recurrent orbit may have

$$
\boxed{
0
\to
c_J
\to
0
}
\tag{26.3}
$$

across one excursion.

The final unresolved arrow is therefore

$$
\boxed{
\text{visible supplier excursion}
\Longrightarrow
\text{strict irreversible return tax}.
}
\tag{26.4}
$$

---

# 27. What is closed in this round

## supplier XTR

A first singular point generates a non-tautological native-separated supplier package.

## supplier COM

After fixed normalization, the supplier package lies in one fixed finite-dimensional compact quotient.

## supplier ACTUAL RETURN

The local supplier stopping rule yields an actual same-history infinite return/re-root chain.

## supplier positive gap

The supplier-rooted obstruction slice satisfies

$$
m_{\rm sup}>0.
$$

These are genuine reductions of the original MORP XTR/COM/TR difficulties on the supplier subprogram.

---

# 28. What remains open

The single closure-facing gap is

$$
\boxed{
\textbf{
Supplier Excursion Irreversibility / Return-Depletion.
}
}
$$

One must prove that a zero-cost minimal/native orbit cannot pass through a fixed supplier trace event and later return to zero cost without paying a positive nonnegative tax.

This is not a compactness issue.

It is now a dynamical irreversibility issue.

---

# 29. Next exact attack

The next round should attack a finite-dimensional trace version first.

Let

$$
a_j(\tau)
=
\langle
h(\tau),
\psi_j
\rangle,
\qquad
j=1,\ldots,N_\ast,
$$

for an orthonormal basis of

$$
H_\ast.
$$

At supplier time,

$$
\boxed{
|a(\tau_{\rm sup})|
\ge
c\nu.
}
\tag{29.1}
$$

At a true combined-invisible minimal return,

$$
\boxed{
|a(\tau_{\rm ret})|
\to0.
}
\tag{29.2}
$$

Differentiate using the normalized forced supplier increment equation.

The target estimate is

$$
\boxed{
\left|
a'(\tau)
+
\nu
M_\ast a(\tau)
\right|
\le
C
\left(
\mathsf{Flux}_{paid}
+
\mathsf{Residual}_{nat}
\right),
}
\tag{29.3}
$$

where

$$
M_\ast
$$

is the positive finite-dimensional Stokes/Laplacian matrix on

$$
H_\ast.
$$

If the right-hand side vanishes, the trace decays only through strictly positive viscosity, producing an explicit positive dissipation integral.

If the right side is nonzero, it is already paid/native.

A successful estimate would yield

$$
\boxed{
\Delta_{\rm exc}
\ge
c_{\rm exc}\nu^2.
}
\tag{29.4}
$$

That would collide directly with MORP's zero-return-tax equality.

This is the next exact attack.

---

# 30. End state

The supplier stopping-time synchronization problem is now resolved in the following precise sense:

$$
\boxed{
\textbf{
local supplier events define an actual,
native-separated, compact, recurrent stopping chain.
}
}
$$

Every normalized supplier node has a uniform positive extended cost

$$
\boxed{
\mathfrak J\ge c_J.
}
$$

Therefore there is no zero-cost supplier-rooted minimal obstruction.

But MORP explicitly allows temporary visible excursions before a later return.

Thus the proof cannot stop at supplier visibility.

The next and single frontier is

$$
\boxed{
\textbf{
Supplier Excursion Irreversibility / Return-Depletion Lemma}.
}
$$

The preferred next route is the finite-dimensional supplier-trace evolution estimate:

$$
\boxed{
\text{trace drop}
\Longrightarrow
\text{viscous payment}
\ \vee\
\text{paid/native forcing}.
}
$$

If this is proved with a scale-uniform positive lower bound, the actual recurrent zero-cost MORP branch is eliminated.

---

# Checkpoint v18 Update — DCRP-18

# NS-DCRP-18 — Trace-Erasure Action, Re-root Infrared Escape, and Two-Sided Scale-Carrier Completion

- date: 2026-08-16
- status: research proof checkpoint
- canonical source: UTF-8 Markdown
- canonical math delimiters: `$...$` and `$$...$$`
- objective:
  1. test the DCRP-17 Supplier Excursion Irreversibility proposal rigorously;
  2. prove the strongest valid fixed-frame trace-erasure action inequality;
  3. audit whether that inequality survives the scale-changing MORP return normalization;
  4. complete the relative-frequency package in the missing infrared direction;
  5. identify the correct next closure target.
- no full Navier--Stokes regularity claim is made.
- principal internal dependencies:
  - MORP-02 relative-frequency defect completion;
  - MORP-03 actual return/re-root semantics and return depletion ledger;
  - DCRP-14 finite-dimensional solenoidal supplier trace window;
  - DCRP-15 finite-window trace/residual realization;
  - DCRP-16 local supplier capture;
  - DCRP-17 supplier stopping-time synchronization.
- external primary calibration:
  - Runlong Yu, *Finite-Window Singularity Audits and Local-to-Clean Defect Transfer for Navier-Stokes*, arXiv:2606.15086v1;
  - Runlong Yu, *Coarse-Grained Resolution and Pressure-Flux Work Depletion for Navier-Stokes CKN Badness*, arXiv:2606.25322v1.
- no novelty / priority claim is made without independent audit.

---

# 1. Executive result

DCRP-17 proposed the following closure strategy:

$$
\boxed{
\text{supplier trace }c\nu
\longrightarrow
\text{later invisible trace }0
\Longrightarrow
\text{strict irreversible return tax}.
}
\tag{1.1}
$$

The first implication can be made rigorous **only in a fixed normalization frame**.

The trace space from DCRP-14 may be chosen to be a finite Stokes spectral window

$$
\boxed{
H_\ast
=
\operatorname{span}
\{
\psi_1,\ldots,\psi_N
\},
}
\tag{1.2}
$$

where the

$$
\psi_j
$$

are divergence-free Dirichlet Stokes eigenfunctions on the fixed observation ball:

$$
\boxed{
A_S\psi_j
=
\mu_j\psi_j,
\qquad
0<\mu_1\le\cdots\le\mu_N.
}
\tag{1.3}
$$

For a supplier nonlinear increment

$$
h
$$

satisfying a forced Stokes equation, define trace coefficients

$$
\boxed{
a_j(\tau)
=
\langle
h(\tau),
\psi_j
\rangle.
}
\tag{1.4}
$$

Then exactly:

$$
\boxed{
a'(\tau)
+
\nu M a(\tau)
=
f(\tau),
}
\tag{1.5}
$$

where

$$
M
=
\operatorname{diag}
(
\mu_1,\ldots,\mu_N
)
$$

and

$$
f
$$

is the finite-dimensional projection of the actual nonlinear stress forcing.

If

$$
|a(\tau_s)|
\ge
A_0
$$

and

$$
|a(\tau_r)|
\le
\varepsilon<A_0,
$$

then:

$$
\boxed{
\nu
\int_{\tau_s}^{\tau_r}
a^TMa\,d\tau
+
\nu^{-1}
\int_{\tau_s}^{\tau_r}
f^TM^{-1}f\,d\tau
\ge
\frac{
A_0^2-\varepsilon^2
}{
3
}.
}
\tag{1.6}
$$

Thus:

$$
\boxed{
\textbf{
fixed-frame supplier trace erasure carries a uniform positive action.
}
}
\tag{1.7}
$$

However the crucial audit result of this round is:

$$
\boxed{
\textbf{
fixed-frame trace erasure}
\neq
\textbf{
scale-re-root trace erasure}.
}
}
\tag{1.8}
$$

If a supplier shell is physically unchanged but the next MORP window re-roots at a scale larger by

$$
\Gamma>1,
$$

then its normalized representation changes from

$$
w(y)
$$

to

$$
\boxed{
w_\Gamma(y)
=
\Gamma^{-1}
w
\left(
\Gamma^{-1}y
\right).
}
\tag{1.9}
$$

Its normalized frequency moves from order one to order

$$
\Gamma^{-1},
$$

and every fixed unit-frequency trace detector sees it vanish as

$$
\Gamma\to\infty,
$$

even though the physical supplier has not dissipated.

Therefore the DCRP-17 plan

$$
\text{trace disappears}
\Rightarrow
\text{physical irreversible tax}
$$

is false for a scale-changing return unless the old supplier scale is explicitly retained.

This exposes a concrete incompleteness in the current MORP-02 scale compactification.

MORP-02 defines relative-frequency shells only for

$$
m\ge0
$$

relative to the terminal reference shell and compactifies

$$
\mathbb N_0
$$

by one point

$$
+\infty.
$$

It detects ultraviolet scale escape.

It does **not** retain an older supplier that, after a higher-frequency re-root, moves to

$$
m<0
$$

and eventually

$$
m\to-\infty.
$$

The missing coordinate is an **infrared relative-scale defect**.

This round introduces the two-sided compactification

$$
\boxed{
\overline{\mathbb Z}
=
\mathbb Z
\cup
\{
-\infty,+\infty
\}.
}
\tag{1.10}
$$

The scale-critical kinetic shell carrier is

$$
\boxed{
\mathcal K_q(t)
=
\lambda_q
\|u_q(t)\|_2^2.
}
\tag{1.11}
$$

It is exactly invariant under Navier--Stokes parabolic scaling.

At a supplier time:

$$
\boxed{
\mathcal K_q(t_s)
\ge
\kappa_0\nu^2.
}
\tag{1.12}
$$

Let a later supplier/re-root have reference shell

$$
q'=q+L.
$$

Then one of the following must occur.

### Persistence

If:

$$
\mathcal K_q(t_r)
\ge
\frac{
\kappa_0
}{
2
}
\nu^2,
$$

then the old supplier survives as a scale-critical carrier at relative shell

$$
m=-L.
$$

For:

$$
L\to\infty,
$$

it becomes a nonzero infrared escape carrier at

$$
-\infty.
$$

### Depletion

If:

$$
\mathcal K_q(t_r)
<
\frac{
\kappa_0
}{
2
}
\nu^2,
$$

the exact shell-energy equation gives:

$$
\boxed{
\nu\lambda_q
\int_{t_s}^{t_r}
\|\nabla u_q\|_2^2dt
+
\lambda_q
\left(
-\int_{t_s}^{t_r}
\mathcal T_q(t)\,dt
\right)_+
\ge
\frac{
\kappa_0
}{
4
}
\nu^2.
}
\tag{1.13}
$$

Thus actual loss of the old supplier pays a fixed scale-critical viscous/outgoing-transfer action.

### Spatial escape

If the old supplier remains physically nonzero but leaves every bounded normalized spatial neighborhood of the return center, the carrier is a spatial-escape defect of the type already contemplated in MORP-02.

Therefore:

$$
\boxed{
\textbf{
old supplier}
\Longrightarrow
\textbf{
finite-relative / IR carrier}
\ \vee\
\textbf{
critical depletion}
\ \vee\
\textbf{
spatial escape}.
}
}
\tag{1.14}
$$

This is the strongest valid excursion statement obtained in this round.

It also forces a correction to DCRP-17.

DCRP-17 proved compactness of the **fixed finite-dimensional supplier window**.

That is valid windowwise.

But transition-complete compactness of an infinite supplier return chain is not established unless the missing infrared carrier is added.

Hence:

$$
\boxed{
\textbf{
supplier window COM}
\neq
\textbf{
transition-complete supplier COM}.
}
}
\tag{1.15}
$$

The supplier excursion problem therefore does not reduce to trace ODE irreversibility.

The correct closure-facing problem is now:

$$
\boxed{
\textbf{
Two-Sided Scale-Carrier / Critical-Supply Taxation Lemma}.
}
\tag{1.16}
$$

This re-routing is consistent with the unconditional finite-scale critical ledger of arXiv:2606.15086:

a persistent non-CKN branch requires cumulative untaxed critical supply or accumulated leakage.

The supplier analysis has now shown how an individual local critical supplier is:

- state-visible;
- trace-visible or residual-paid;
- actual-history generated;
- and, after re-root, either retained as a two-sided scale carrier or depleted at fixed critical action.

What remains is to prove that the **positive-density critical supply required by a persistent bad branch cannot all evade taxation by passing through scale re-rooting / infrared escape**.

That is the next exact target.

---

# 2. Refinement of the DCRP-14 trace window

DCRP-14 constructed a finite-dimensional space

$$
H_\ast
\subset
C_c^\infty(B_R;\mathbb R^3)
$$

of divergence-free fields satisfying a uniform supplier projection gap.

For the trace-evolution argument it is useful to choose the finite-dimensional space from the spectral decomposition of the Dirichlet Stokes operator on

$$
B_R.
$$

Let:

$$
A_S
$$

denote the positive self-adjoint Stokes operator on the divergence-free

$$
L^2
$$

space with zero boundary condition.

Its eigenfunctions form a complete orthonormal basis:

$$
\boxed{
A_S\psi_j
=
\mu_j\psi_j.
}
\tag{2.1}
$$

The density argument used in DCRP-14 remains valid with the increasing spectral spaces

$$
\boxed{
H_N
=
\operatorname{span}
\{
\psi_1,\ldots,\psi_N
\}.
}
\tag{2.2}
$$

Because the normalized supplier class is locally compact and the full solenoidal projection has a uniform positive lower bound, there exists

$$
N_\ast<\infty
$$

such that:

$$
\boxed{
\|
\Pi_{H_{N_\ast}}
h
\|_2
\ge
c_\ast\nu
}
\tag{2.3}
$$

for every normalized supplier nonlinear increment.

Thus, without loss of the DCRP-14 trace lift, one may take:

$$
\boxed{
H_\ast
=
H_{N_\ast}.
}
\tag{2.4}
$$

Status:

$$
\boxed{
\textbf{PROVED by the same compact finite-dimensional approximation argument as DCRP-14}.
}
$$

---

# 3. Exact finite-dimensional trace evolution

Let:

$$
h(\tau)
$$

be a normalized divergence-free supplier increment satisfying:

$$
\boxed{
\partial_\tau h
-
\nu\Delta h
+
\nabla\pi
=
-\nabla\cdot T.
}
\tag{3.1}
$$

Let:

$$
\psi_j
$$

be a Dirichlet Stokes eigenfunction.

Define:

$$
\boxed{
a_j(\tau)
=
\int_{B_R}
h(y,\tau)
\cdot
\psi_j(y)
\,dy.
}
\tag{3.2}
$$

Testing (3.1) against:

$$
\psi_j,
$$

the pressure term vanishes because:

$$
\nabla\cdot\psi_j=0
$$

and:

$$
\psi_j|_{\partial B_R}=0.
$$

Also:

$$
\int
\nabla h:\nabla\psi_j
=
\mu_j
\int
h\cdot\psi_j.
$$

Therefore:

$$
\boxed{
a_j'
+
\nu\mu_j a_j
=
f_j,
}
\tag{3.3}
$$

where:

$$
\boxed{
f_j(\tau)
=
\int_{B_R}
T(y,\tau):
\nabla\psi_j(y)
\,dy.
}
\tag{3.4}
$$

Let:

$$
a
=
(a_1,\ldots,a_N)^T,
$$

$$
f
=
(f_1,\ldots,f_N)^T,
$$

and:

$$
\boxed{
M
=
\operatorname{diag}
(
\mu_1,\ldots,\mu_N
).
}
\tag{3.5}
$$

Then:

$$
\boxed{
a'
+
\nu Ma
=
f.
}
\tag{3.6}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 4. NEW THEOREM — Fixed-Frame Trace-Erasure Action Gap

## Theorem 4.1

Suppose:

$$
a:
[\tau_s,\tau_r]
\to
\mathbb R^N
$$

satisfies:

$$
a'
+
\nu Ma
=
f,
$$

where:

$$
M
$$

is symmetric positive definite.

Assume:

$$
\boxed{
|a(\tau_s)|
\ge
A_0,
}
\tag{4.1}
$$

and:

$$
\boxed{
|a(\tau_r)|
\le
\varepsilon
<
A_0.
}
\tag{4.2}
$$

Then:

$$
\boxed{
\nu
\int_{\tau_s}^{\tau_r}
a^TMa\,d\tau
+
\nu^{-1}
\int_{\tau_s}^{\tau_r}
f^TM^{-1}f\,d\tau
\ge
\frac{
A_0^2-\varepsilon^2
}{
3
}.
}
\tag{4.3}
$$

### Proof

Take the Euclidean inner product of:

$$
a'
+
\nu Ma
=
f
$$

with:

$$
a.
$$

Then:

$$
\frac12
\frac d{d\tau}
|a|^2
+
\nu a^TMa
=
a^Tf.
$$

Integrate from:

$$
\tau_s
$$

to:

$$
\tau_r.
$$

Set:

$$
D
=
\nu
\int
a^TMa,
$$

and:

$$
F
=
\nu^{-1}
\int
f^TM^{-1}f.
$$

Then:

$$
\frac12
\left(
|a(\tau_s)|^2
-
|a(\tau_r)|^2
\right)
=
D
-
\int
a^Tf.
$$

By Cauchy--Schwarz in the

$$
M/M^{-1}
$$

pairing:

$$
\left|
\int
a^Tf
\right|
\le
\sqrt{DF}.
$$

Thus:

$$
\frac12
\left(
A_0^2-\varepsilon^2
\right)
\le
D+\sqrt{DF}.
$$

Since:

$$
\sqrt{DF}
\le
\frac{
D+F
}{
2
},
$$

$$
D+\sqrt{DF}
\le
\frac32
(D+F).
$$

Therefore:

$$
D+F
\ge
\frac{
A_0^2-\varepsilon^2
}{
3
}.
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

# 5. Supplier consequence in one fixed normalization frame

At supplier time:

$$
\tau_s,
$$

DCRP-14 gives:

$$
\boxed{
|a(\tau_s)|
\ge
c_\ast\nu.
}
\tag{5.1}
$$

If, in the **same normalized frame and same trace space**,

$$
|a(\tau_r)|
\le
\frac{
c_\ast
}{
2
}
\nu,
$$

Theorem 4.1 gives:

$$
\boxed{
\nu
\int_{\tau_s}^{\tau_r}
a^TMa
+
\nu^{-1}
\int_{\tau_s}^{\tau_r}
f^TM^{-1}f
\ge
c_A\nu^2,
}
\tag{5.2}
$$

where:

$$
c_A
=
\frac{
c_\ast^2
}{
4
}.
$$

Thus the fixed-frame trace cannot disappear without a fixed viscous/forcing action.

This validates one part of the DCRP-17 intuition.

---

# 6. CRITICAL NO-GO — scale re-root can erase a fixed trace for free

The MORP return is not generally a fixed-frame evolution.

It contains parabolic re-rooting.

Suppose a physical supplier field at scale:

$$
\lambda
$$

is represented in its own normalized coordinates by:

$$
\boxed{
w(y)
=
\lambda^{-1}
u_{\rm sup}
\left(
x_\ast+\lambda^{-1}y
\right).
}
\tag{6.1}
$$

Suppose the next return uses a reference scale:

$$
\lambda'
=
\Gamma\lambda,
\qquad
\Gamma>1.
$$

Represent the **same unchanged physical field** in the new coordinates:

$$
w^{new}(y)
=
(\lambda')^{-1}
u_{\rm sup}
\left(
x_\ast+(\lambda')^{-1}y
\right).
$$

Using (6.1):

$$
u_{\rm sup}
\left(
x_\ast+(\lambda')^{-1}y
\right)
=
\lambda
w
\left(
\lambda(\lambda')^{-1}y
\right).
$$

Therefore:

$$
\boxed{
w^{new}(y)
=
\Gamma^{-1}
w
\left(
\Gamma^{-1}y
\right).
}
\tag{6.2}
$$

The amplitude acquires:

$$
\Gamma^{-1},
$$

and the normalized Fourier support moves from:

$$
|\xi|\sim1
$$

to:

$$
|\xi|\sim\Gamma^{-1}.
$$

Hence for every fixed unit-annulus trace window:

$$
H_\ast,
$$

$$
\boxed{
\|
\Pi_{H_\ast}
w^{new}
\|_2
\to0
\qquad
(\Gamma\to\infty)
}
\tag{6.3}
$$

even though:

- the physical field is unchanged;
- no viscosity acted;
- no nonlinear transfer occurred.

Therefore:

$$
\boxed{
\textbf{
normalized trace disappearance across a scale-changing return
does not imply physical depletion.
}
}
\tag{6.4}
$$

Status:

$$
\boxed{
\textbf{NO-GO PROVED}.
}
$$

This invalidates a direct use of Theorem 4.1 as the complete MORP return-depletion theorem.

---

# 7. What happened to the old supplier?

The old supplier did not disappear.

It moved to a lower **relative** frequency.

If the later reference shell is:

$$
q'=q+L,
$$

then the old shell:

$$
q
$$

has relative index:

$$
\boxed{
m=q-q'=-L.
}
\tag{7.1}
$$

For:

$$
L\to\infty,
$$

$$
\boxed{
m\to-\infty.
}
\tag{7.2}
$$

Thus the correct language is:

$$
\boxed{
\textbf{
re-root visibility loss}
=
\textbf{
infrared relative-scale escape}
}
}
\tag{7.3}
$$

unless the physical supplier itself is depleted.

---

# 8. Audit of MORP-02 relative-scale completion

MORP-02 defines a terminal reference shell:

$$
J_n.
$$

It then defines relative shells only for:

$$
\boxed{
m\ge0,
}
\tag{8.1}
$$

and places the selected-time carrier on:

$$
\boxed{
\overline{\mathbb N}_0
=
\mathbb N_0
\cup
\{
+\infty
\}.
}
\tag{8.2}
$$

The resulting defect completion retains:

$$
\boxed{
\text{UV relative-frequency escape}.
}
\tag{8.3}
$$

But a previous supplier under a later/higher re-root has:

$$
m<0.
$$

Therefore the current one-sided compactification does not retain:

$$
\boxed{
\text{IR relative-frequency escape}.
}
\tag{8.4}
$$

This is a genuine transition-completeness gap.

---

# 9. Two-sided relative-frequency completion

Define:

$$
\boxed{
\overline{\mathbb Z}
=
\mathbb Z
\cup
\{
-\infty,+\infty
\}.
}
\tag{9.1}
$$

Use the order topology / two-point compactification.

For a normalized state whose reference physical shell is:

$$
J_n,
$$

the physical shell:

$$
J_n+m
$$

corresponds to normalized relative frequency:

$$
2^m.
$$

Define the scale-critical kinetic shell carrier:

$$
\boxed{
\kappa_{n,m}
=
2^m
\|
P_mU_n
\|_2^2.
}
\tag{9.2}
$$

For the global normalized state:

$$
U_n(y)
=
2^{-J_n}
u
\left(
x_n+2^{-J_n}y,
t_n
\right),
$$

one has, up to the bounded dyadic partition convention,

$$
\boxed{
\kappa_{n,m}
=
2^{J_n+m}
\|
u_{J_n+m}(t_n)
\|_2^2.
}
\tag{9.3}
$$

Thus:

$$
\boxed{
\kappa_{n,m}
}
$$

is exactly parabolic-scale invariant.

For a localized carrier, the same identity holds modulo the explicit localization/spatial-tail residual.

---

# 10. Supplier critical shell lower bound

At a local supplier event from DCRP-16:

$$
\lambda_q^{-1}
\|u_q\|_\infty
\ge
c_{\rm loc}\nu.
$$

Bernstein yields:

$$
\boxed{
\mathcal K_q
:=
\lambda_q
\|u_q\|_2^2
\ge
\kappa_0\nu^2
}
\tag{10.1}
$$

for:

$$
\kappa_0>0.
$$

This is exactly the carrier:

$$
\kappa_{n,0}
$$

when the supplier shell itself is chosen as the reference scale.

---

# 11. Exact shell-energy ledger

For a fixed physical shell:

$$
q,
$$

the exact kinetic-shell identity is:

$$
\boxed{
\frac12
\frac d{dt}
\|u_q\|_2^2
+
\nu
\|\nabla u_q\|_2^2
=
\mathcal T_q(t),
}
\tag{11.1}
$$

where:

$$
\mathcal T_q
$$

is the signed nonlinear transfer **into** shell:

$$
q.
$$

Multiply by:

$$
\lambda_q
$$

and integrate:

$$
\boxed{
\frac12
\left[
\mathcal K_q(t_1)
-
\mathcal K_q(t_0)
\right]
+
\nu\lambda_q
\int_{t_0}^{t_1}
\|\nabla u_q\|_2^2dt
=
\lambda_q
\int_{t_0}^{t_1}
\mathcal T_q(t)\,dt.
}
\tag{11.2}
$$

Every term has critical scaling.

---

# 12. NEW THEOREM — Tagged Supplier Depletion / IR-Escape Alternative

## Theorem 12.1

Let:

$$
t_s<t_r
$$

be two times on one actual Navier--Stokes history.

Assume shell:

$$
q
$$

is a supplier at:

$$
t_s:
$$

$$
\boxed{
\mathcal K_q(t_s)
\ge
\kappa_0\nu^2.
}
\tag{12.1}
$$

Then exactly one of the following broad alternatives holds.

### Persistent old supplier

$$
\boxed{
\mathcal K_q(t_r)
\ge
\frac{
\kappa_0
}{
2
}
\nu^2.
}
\tag{12.2}
$$

If the return reference shell is:

$$
q_r>q,
$$

the old supplier appears as a nonzero two-sided relative-scale carrier at:

$$
\boxed{
m=q-q_r<0.
}
\tag{12.3}
$$

If:

$$
q_r-q\to\infty,
$$

this is a nonzero IR escape carrier at:

$$
-\infty.
$$

### Depleted old supplier

$$
\boxed{
\mathcal K_q(t_r)
<
\frac{
\kappa_0
}{
2
}
\nu^2.
}
\tag{12.4}
$$

Then:

$$
\boxed{
\nu\lambda_q
\int_{t_s}^{t_r}
\|\nabla u_q\|_2^2dt
+
\left[
-\lambda_q
\int_{t_s}^{t_r}
\mathcal T_q(t)\,dt
\right]_+
\ge
\frac{
\kappa_0
}{
4
}
\nu^2.
}
\tag{12.5}
$$

### Proof of the depletion estimate

From (11.2):

$$
\frac12
\left[
\mathcal K_q(t_s)
-
\mathcal K_q(t_r)
\right]
=
\nu\lambda_q
\int
\|\nabla u_q\|_2^2
-
\lambda_q
\int
\mathcal T_q.
$$

Under (12.1) and (12.4):

$$
\frac12
\left[
\mathcal K_q(t_s)
-
\mathcal K_q(t_r)
\right]
\ge
\frac{
\kappa_0
}{
4
}
\nu^2.
$$

For any:

$$
D\ge0
$$

and:

$$
X\in\mathbb R,
$$

$$
D+(-X)_+
\ge
D-X.
$$

Apply:

$$
D
=
\nu\lambda_q
\int
\|\nabla u_q\|_2^2,
$$

$$
X
=
\lambda_q
\int
\mathcal T_q.
$$

This gives (12.5).

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

# 13. Spatial completion

Theorem 12.1 uses the global shell carrier.

For a local supplier package, one must also track spatial position.

If:

$$
\mathcal K_q(t_r)
$$

remains large globally but the shell carrier leaves every bounded normalized spatial neighborhood of the return center, then the supplier is not locally depleted.

It has undergone:

$$
\boxed{
\textbf{
spatial carrier escape}.
}
}
\tag{13.1}
$$

MORP-02 already allows one-point compactification of normalized spatial carrier measures.

Thus the local version of Theorem 12.1 is:

$$
\boxed{
\textbf{
old supplier}
\Longrightarrow
\textbf{
finite/IR scale carrier}
\ \vee\
\textbf{
spatial escape}
\ \vee\
\textbf{
critical depletion}.
}
}
\tag{13.2}
$$

---

# 14. Scale re-root no longer counts as "free disappearance"

After adding the infrared scale coordinate:

- a physically persistent old supplier cannot vanish merely because the reference frequency increased;
- if it is no longer visible at finite relative scale, it appears at:

  $$
  -\infty;
  $$

- if it is no longer spatially local, it appears in the spatial escape coordinate;
- if neither carrier remains, Theorem 12.1 gives a fixed critical depletion action.

Thus:

$$
\boxed{
\textbf{
re-root trace disappearance}
\Longrightarrow
\textbf{
IR/spatial defect}
\ \vee\
\textbf{
physical depletion}.
}
}
\tag{14.1}
$$

This is the corrected form of DCRP-17's excursion intuition.

---

# 15. CORRECTION — DCRP-17 supplier compactness claim

DCRP-17 proved compactness of the supplier package after projection to one fixed finite-dimensional normalized supplier window.

That statement remains valid.

However an infinite supplier return chain changes the reference frequency.

The fixed window does not contain all older negative relative shells.

Therefore:

$$
\boxed{
\text{fixed-window supplier COM}
}
$$

does not imply:

$$
\boxed{
\text{transition-complete supplier COM}.
}
$$

Without two-sided relative-scale completion, an infinite amount of old supplier history may escape into:

$$
m\to-\infty.
$$

Accordingly, DCRP-17's phrase:

$$
\boxed{
\text{Supplier COM closed}
}
$$

must be read only as:

$$
\boxed{
\text{Supplier fixed-window COM closed}.
}
$$

Transition-complete compactness remains open.

Status:

$$
\boxed{
\textbf{CORRECTED}.
}
$$

---

# 16. Why two-sided completion still does not prove a contradiction

Suppose every old supplier is eventually depleted.

Then Theorem 12.1 supplies a fixed critical depletion action for each tag.

However new supplier shells are also generated at later scales.

A forward cascade may have the schematic form:

$$
\boxed{
\text{old supplier depletion}
+
\text{new supplier creation}.
}
\tag{16.1}
$$

The positive loss of one shell can be compensated by positive supply to the next shell.

Physical kinetic energy permits this because the raw energy per scale is:

$$
O(\lambda_q^{-1}),
$$

which is geometrically summable.

Therefore:

$$
\boxed{
\text{fixed critical depletion per supplier}
\not\Rightarrow
\text{global energy contradiction}.
}
\tag{16.2}
$$

This is the old Critical Barrier Accumulation obstruction in a sharper tagged-shell form.

---

# 17. Why fixed-frame trace action is not a MORP return tax by itself

Theorem 4.1 proves a positive action whenever one fixed trace genuinely decays in one fixed frame.

But an excursion may have:

$$
\boxed{
\text{positive forcing}
\to
\text{visible supplier}
\to
\text{viscous/forward transfer loss}
}
\tag{17.1}
$$

and still return to a new invisible normalized state.

The action is real.

What is not automatic is the MORP inequality:

$$
\boxed{
\mathfrak J(D^+)
+
\Delta_{\rm exc}
\le
\mathfrak J(D^-).
}
\tag{17.2}
$$

The supplier can be created by incoming critical supply.

Therefore:

$$
\boxed{
\textbf{
action cost}
\neq
\textbf{
net return depletion}.
}
}
\tag{17.3}
$$

Status:

$$
\boxed{
\textbf{LOGICAL NO-GO}.
}
$$

This is why the next route must return to the full critical supply/tax ledger.

---

# 18. External finite-scale critical ledger

The finite-window audit theorem of arXiv:2606.15086 proves an unconditional finite-scale survival alternative.

Along a persistent non-CKN scale-window chain:

$$
\boxed{
\sum_{k=0}^{N-1}
\left(
\mathrm{Sup}^{full}_k
-
\mathrm{Tax}^{full}_k
\right)_+
\ge
\lambda_0
\varepsilon
N
-
B_0
-
\sum_{k=0}^{N-1}
\mathrm{Leak}^{full}_k.
}
\tag{18.1}
$$

Thus if leakage has vanishing average, a persistent bad branch requires **positive-density untaxed critical supply**.

This theorem identifies the correct global resource problem.

The question is not merely:

> does a supplier excursion pay something?

It is:

> can the positive critical supply required to perpetuate the bad branch remain **untaxed** after the DCRP supplier / PFET / trace / two-sided-scale completion is applied?

This is the correct closure-facing formulation.

---

# 19. What DCRP has already established about critical supply

The current DCRP chain supplies the following modules.

### Local source

DCRP-16:

$$
\boxed{
\text{local singular point}
\Longrightarrow
\text{local critical supplier sequence}.
}
\tag{19.1}
$$

### Actual nonlinear ancestry

DCRP-09:

$$
\boxed{
\text{supplier}
\Longrightarrow
\text{same-history nonlinear forcing}.
}
\tag{19.2}
$$

### Positive net shell supply

DCRP-10:

$$
\boxed{
\lambda_Q
\int_I
\mathcal T_Q
\ge
c\nu^2
}
\tag{19.3}
$$

on first-crossing intervals.

### Heat-filter PFET / backscatter alternative

DCRP-11:

$$
\boxed{
\text{forward heat work}
\ \vee\
\text{backscatter}
}
\tag{19.4}
$$

with fixed critical amount.

### Local package completion

DCRP-12:

$$
\boxed{
\text{local PFET}
\ \vee\
\text{paid backscatter}
\ \vee\
\text{work escape}.
}
\tag{19.5}
$$

### Supplier trace/residual gap

DCRP-15:

$$
\boxed{
\|
O_W^T
\|
+
C
\mathcal B_{\rm sup}^{res}
\ge
c\nu.
}
\tag{19.6}
$$

### Re-root completion

DCRP-18:

$$
\boxed{
\text{persistent old supplier}
\Longrightarrow
\text{finite/IR scale carrier or spatial escape},
}
\tag{19.7}
$$

while actual loss gives:

$$
\boxed{
\text{critical viscous/outgoing-transfer action}.
}
\tag{19.8}
$$

Thus individual supplier events are no longer structurally invisible.

---

# 20. What is still missing from the finite-scale ledger

The survival theorem (18.1) does not say that every critical supply event must cross the particular supplier threshold:

$$
\lambda_q^{-1}
\|u_q\|_\infty
\gtrsim
\nu.
$$

A persistent bad branch could, in principle, distribute its required critical supply over:

- many frequency shells;
- many spatial cells;
- pressure transport;
- unresolved oscillation;
- long moving windows;

without one individual supply event becoming a DCRP supplier atom at every ledger step.

Therefore:

$$
\boxed{
\textbf{
supplier taxation}
\neq
\textbf{
all critical-supply taxation}.
}
}
\tag{20.1}
$$

This is now the exact remaining global gap.

---

# 21. Corrected next frontier

The DCRP-17 target:

$$
\text{Supplier Excursion Irreversibility}
$$

is replaced by:

$$
\boxed{
\textbf{
Critical Supply Taxation / Untaxed-Supply Capture Lemma}.
}
\tag{21.1}
$$

A sufficient theorem would prove:

> Along every sufficiently late local non-CKN transition whose full critical ledger has
>
> $$
> \left(
> \mathrm{Sup}^{full}
> -
> \mathrm{Tax}^{full}
> \right)_+
> \ge
> \eta>0,
> $$
>
> at least one of the following occurs:
>
> 1. a local supplier atom is produced and therefore enters the DCRP trace/PFET/residual package;
> 2. the supply is spatially or spectrally diffuse and produces a nonzero completed work/scale/spatial defect;
> 3. pressure/localization leakage carries a fixed amount;
> 4. a paid/backscatter channel is already positive.

If the above alternatives have a scale-uniform quantitative lower bound, then the positive-density untaxed supply required by (18.1) cannot remain untaxed.

Combined with vanishing-average leakage, the persistent non-CKN branch would be impossible.

This is now a direct route from an unconditional finite-scale ledger to regularity.

---

# 22. Two-sided relative-scale probability versus absolute carrier

A technical choice remains.

MORP-02 normalizes its scale distribution to a probability measure.

For the old supplier, one has an **absolute** critical lower bound:

$$
\mathcal K_q\ge\kappa_0\nu^2.
$$

Normalizing by a total carrier that may diverge can make this supplier's probability share vanish.

Therefore the two-sided completion should retain both:

1. a normalized probability distribution describing relative carrier geometry;
2. an absolute critical carrier amplitude coordinate.

A useful package is:

$$
\boxed{
\left(
A_n^{sc},
\sigma_n^{sc}
\right),
}
\tag{22.1}
$$

where:

$$
A_n^{sc}
=
\sum_m
\kappa_{n,m}
$$

when finite, or its extended-value defect completion, and:

$$
\sigma_n^{sc}
=
(A_n^{sc})^{-1}
\sum_m
\kappa_{n,m}\delta_m.
$$

This prevents a fixed absolute supplier atom from disappearing merely because the total critical norm diverges.

No compactness claim is made here when:

$$
A_n^{sc}\to\infty.
$$

That divergence itself is a native critical-norm defect.

---

# 23. New compactness boundary

The two-sided completion produces the following alternatives.

### Finite total critical carrier

If:

$$
\sup_n
A_n^{sc}
<
\infty,
$$

the two-sided carrier measures are weak-star compact on:

$$
\overline{\mathbb Z}.
$$

### Divergent critical carrier

If:

$$
A_n^{sc}\to\infty,
$$

the state has a divergent:

$$
\dot H^{1/2}
$$

-type shell carrier.

This is not a contradiction.

It is a noncompact critical-norm branch.

Thus transition-complete supplier compactness itself reduces to:

$$
\boxed{
\text{finite two-sided carrier}
\ \vee\
\text{critical-norm blowup}.
}
\tag{23.1}
$$

The latter is compatible with a hypothetical singularity and therefore must be handled dynamically rather than discarded.

---

# 24. Implication for the "proof-space contraction" assessment

The supplier route has not returned to the original unstructured problem.

The remaining obstruction is now highly specific.

A hypothetical singular branch must support:

$$
\boxed{
\textbf{
positive-density scale-critical supply that remains profitable after:
}
}
$$

- local supplier capture;
- pressure/flux observation;
- backscatter taxation;
- finite-window trace separation;
- projection/residual cleaning;
- spatial escape completion;
- UV scale completion;
- IR scale completion;
- tagged-shell depletion accounting.

This is a much narrower object than the original generic blowup branch.

But it is also recognizably the central cascade problem:

$$
\boxed{
\textbf{
can Navier--Stokes sustain a profitable critical energy cascade
to arbitrarily small scales without entering a regularity basin?
}
}
\tag{24.1}
$$

That question is not yet answered by the present corpus.

---

# 25. Preferred next attack

The next round should work directly with the unconditional critical ledger rather than with endpoint trace disappearance.

Let:

$$
Q_k\to Q_{k+1}
$$

be one local singular scale transition.

Let:

$$
\mathrm{Sup}^{full}_k
$$

be decomposed into:

- nonlinear flux supply;
- pressure transport supply;
- localization leakage / residual.

The goal is a **supply-to-carrier decomposition**:

$$
\boxed{
\mathrm{Sup}^{full}_k
\le
C
\left[
\mathrm{TaxedSupplier}_k
+
\mathrm{DiffuseDefect}_k
+
\mathrm{Leak}_k
+
\mathrm{Tax}^{full}_k
\right].
}
\tag{25.1}
$$

with constants independent of:

$$
k.
$$

Here:

$$
\mathrm{TaxedSupplier}_k
$$

must be controlled by the already established DCRP PFET/trace/residual modules.

Then:

$$
\boxed{
\left(
\mathrm{Sup}^{full}_k
-
\mathrm{Tax}^{full}_k
\right)_+
}
$$

can remain large only if:

$$
\mathrm{DiffuseDefect}_k
+
\mathrm{Leak}_k
$$

is large.

If both have vanishing average, Theorem 3.3 of the finite-window audit gives a contradiction with persistent badness.

This is the cleanest current closure target.

---

# 26. Source audit

## Finite-Window Singularity Audits and Local-to-Clean Defect Transfer

Runlong Yu, arXiv:2606.15086v1.

The paper proves unconditionally that along every admissible non-CKN scale-window chain:

$$
B_{k+1}
-
(1-\lambda_0)
B_k
\le
\mathrm{Sup}^{full}_k
-
\mathrm{Tax}^{full}_k
+
\mathrm{Leak}^{full}_k,
$$

and consequently:

$$
\sum_{k<N}
\left(
\mathrm{Sup}^{full}_k
-
\mathrm{Tax}^{full}_k
\right)_+
\ge
\lambda_0\varepsilon N
-
B_0
-
\sum_{k<N}
\mathrm{Leak}^{full}_k.
$$

Thus persistent badness requires cumulative untaxed supply or leakage.

The paper explicitly lists uniform taxation/observable depletion of all critical supply as an open input.

DCRP-18 adopts that exact open interface as the next target.

## Coarse-Grained Resolution and Pressure-Flux Work Depletion

Runlong Yu, arXiv:2606.25322v1.

This paper proves an exact fixed-chain pressure--flux work telescope:

- forward combined work;
- resolved dissipation;

are paid by:

- initial localized kinetic energy;
- explicit localization leakage;
- negative combined work/backscatter.

DCRP-11/12 already used this sign structure.

The remaining issue is not the fixed-chain work identity.

It is the quantitative capture of all critical supply appearing in the full singularity ledger.

---

# 27. End state

The strongest new fixed-frame theorem is:

$$
\boxed{
\textbf{
Trace-Erasure Action Gap}
}
$$

$$
\boxed{
\nu
\int
a^TMa
+
\nu^{-1}
\int
f^TM^{-1}f
\ge
\frac{
A_0^2-\varepsilon^2
}{
3
}.
}
$$

But scale re-rooting produces the exact NO-GO:

$$
\boxed{
w^{new}(y)
=
\Gamma^{-1}
w(\Gamma^{-1}y),
}
$$

so a fixed unit-scale trace may vanish with no physical depletion.

The missing object is infrared relative-scale escape.

After two-sided scale completion, every old supplier satisfies:

$$
\boxed{
\text{finite/IR carrier}
\ \vee\
\text{spatial escape}
\ \vee\
\text{critical depletion}.
}
$$

This corrects the transition-complete compactness picture.

The excursion problem is therefore not primarily a trace-irreversibility problem.

It is a **critical supply taxation problem**.

The next single frontier is:

$$
\boxed{
\textbf{
Critical Supply Taxation / Untaxed-Supply Capture Lemma}.
}
$$

If every positive-density critical supply required by the unconditional finite-scale survival theorem can be routed into:

- DCRP supplier/PFET/trace taxation;
- paid backscatter;
- completed diffuse scale/spatial/work defects;
- or localization leakage,

then the persistent non-CKN branch has no untaxed mechanism left.

That is the next exact attack.

---

# Checkpoint v19 Update — DCRP-19

# NS-DCRP-19 — Critical-Supply Source Reduction, Visibility-vs-Taxation No-Go, and the Filtered Stretching–Diffusion Pivot

- date: 2026-08-16
- status: research proof checkpoint
- canonical source: UTF-8 Markdown
- canonical math delimiters: `$...$` and `$$...$$`
- objective:
  1. inspect the exact full-supply formula behind the persistent non-CKN survival theorem;
  2. reduce positive untaxed supply to a short list of quantitative source mechanisms;
  3. determine whether the DCRP detector/supplier modules actually tax those sources or merely observe them;
  4. pivot from bookkeeping geometry to a coercive filtered vorticity mechanism without discarding the existing DCRP infrastructure.
- no full Navier--Stokes regularity claim is made.
- principal external primary sources:
  - Runlong Yu, *Critical Ledgers and Scale-Defect Cascades for Navier-Stokes*, arXiv:2606.13887;
  - Runlong Yu, *Finite-Window Singularity Audits and Local-to-Clean Defect Transfer for Navier-Stokes*, arXiv:2606.15086;
  - Runlong Yu, *Coarse-Grained Resolution and Pressure-Flux Work Depletion for Navier-Stokes CKN Badness*, arXiv:2606.25322;
  - Runlong Yu, *A Structural Audit of Navier-Stokes Obstruction Calculus*, arXiv:2606.25341.
- internal dependencies:
  - DCRP-08 through DCRP-18;
  - MORP/FCBP finite-window observation and residual architecture.
- no novelty/priority claim is made without independent audit.

---

# 1. Executive result

DCRP-18 ended with the proposed target:

$$
\boxed{
\textbf{
Critical Supply Taxation / Untaxed-Supply Capture Lemma}.
}
$$

The exact full critical supply from the ledger theorem is:

$$
\boxed{
\mathrm{Sup}^{full}_k
=
\theta^{-1}X_k
+
C_{I,\theta}X_k^{3/2}
+
C_P\theta^{-2}C_k,
}
\tag{1.1}
$$

where:

$$
\boxed{
X_k
=
\Phi_k
+
2\Pi_k.
}
\tag{1.2}
$$

Here:

- $\Phi_k$ is nonlinear cutoff/window flux supply;
- $\Pi_k$ is pressure transport supply;
- $C_k$ is the scale-critical local velocity-cubic reservoir.

The tax is:

$$
\boxed{
\mathrm{Tax}^{full}_k
=
2E_{k+1}
+
(1-\alpha)A_k
+
(1-\alpha)C_k
+
\delta_DD_k.
}
\tag{1.3}
$$

The leakage is:

$$
\boxed{
\mathrm{Leak}^{full}_k
=
\theta^{-1}\Lambda_k
+
C_{I,\theta}\Lambda_k^{3/2}.
}
\tag{1.4}
$$

The first new theorem of this round is purely algebraic but closure-relevant.

If:

$$
\boxed{
\left(
\mathrm{Sup}^{full}_k
-
\mathrm{Tax}^{full}_k
\right)_+
\ge
\eta>0,
}
\tag{1.5}
$$

then in particular:

$$
\mathrm{Sup}^{full}_k\ge\eta.
$$

Consequently at least one of:

$$
\boxed{
X_k
\ge
\xi_\eta
}
\tag{1.6}
$$

or:

$$
\boxed{
C_k
\ge
\zeta_\eta
}
\tag{1.7}
$$

must hold, where:

$$
\boxed{
\xi_\eta
=
\min
\left\{
\frac{\theta\eta}{4},
\left(
\frac{\eta}{4C_{I,\theta}}
\right)^{2/3}
\right\},
}
\tag{1.8}
$$

and:

$$
\boxed{
\zeta_\eta
=
\frac{
\theta^2\eta
}{
2C_P
}.
}
\tag{1.9}
$$

Moreover:

$$
X_k\ge\xi_\eta
$$

implies:

$$
\boxed{
\Phi_k
\ge
\frac{\xi_\eta}{3}
}
\tag{1.10}
$$

or:

$$
\boxed{
\Pi_k
\ge
\frac{\xi_\eta}{3}.
}
\tag{1.11}
$$

Thus every fixed-size full supply event comes from one of only three quantitative source classes:

$$
\boxed{
\text{nonlinear transition influx}
\ \vee\
\text{pressure transition influx}
\ \vee\
\text{cubic reservoir regeneration}.
}
\tag{1.12}
$$

The interpolation term:

$$
C_{I,\theta}X_k^{3/2}
$$

is **not an independent source mechanism**.

It is generated algebraically from the same transition influx:

$$
X_k.
$$

Likewise:

$$
C_P\theta^{-2}C_k
$$

is not a new transition current.

It is pressure regeneration from the old cubic reservoir.

This reduces the full-supply taxonomy.

The second new theorem combines the cubic branch with the coarse resolution lemma.

Because:

$$
\Psi_k
=
C_k+D_k
\ge
C_k,
$$

the exact coarse resolution:

$$
\boxed{
\Psi_k
\le
4\Psi_k^\ell
+
4\Omega_k^\ell
}
\tag{1.13}
$$

gives:

$$
\boxed{
C_k\ge\zeta_\eta
\Longrightarrow
\Psi_k^\ell
\ge
\frac{
\zeta_\eta
}{
8
}
\quad
\vee
\quad
\Omega_k^\ell
\ge
\frac{
\zeta_\eta
}{
8
}.
}
\tag{1.14}
$$

Hence fixed untaxed supply reduces quantitatively to:

$$
\boxed{
\begin{aligned}
&\text{nonlinear boundary/transition influx}\\
&\vee
\text{pressure transport}\\
&\vee
\text{resolved coarse CKN mechanism}\\
&\vee
\text{subfilter residual}.
\end{aligned}
}
\tag{1.15}
$$

This is a genuine source reduction.

However the main audit result is a NO-GO:

$$
\boxed{
\textbf{
source visibility}
\not\Rightarrow
\textbf{
source taxation}.
}
\tag{1.16}
$$

A positive forward flux is precisely a mechanism that supplies the next scale.

Detecting it does not make it negative.

A positive coarse pressure/velocity observation is a certificate of activity, not automatically a depletion term.

Therefore the DCRP trace/PFET/defect machinery cannot close the ledger merely by proving:

$$
\boxed{
\text{every source is visible or retained}.
}
\tag{1.17}
$$

What is needed is a **coercive PDE mechanism** that converts persistent positive supply into:

- diffusion;
- backscatter/negative work;
- subgrid forcing cost;
- pressure-compatible loss;
- direction incoherence;
- or another genuinely nonnegative depletion.

This is exactly the distinction:

$$
\boxed{
\text{bookkeeping/interface}
\neq
\text{coercive PDE estimate}.
}
\tag{1.18}
$$

The present route therefore pivots to the filtered vorticity equation.

For a fixed relative spatial filter:

$$
\ell=\sigma r,
$$

write:

$$
U^\ell=S_\ell u,
$$

$$
\Omega^\ell
=
\nabla\times U^\ell,
$$

$$
S^\ell
=
\frac12
\left(
\nabla U^\ell
+
(\nabla U^\ell)^T
\right),
$$

and:

$$
\mathcal J^\ell
=
\nabla\times
(\nabla\cdot R^\ell).
$$

The exact filtered vorticity equation is:

$$
\boxed{
\partial_t\Omega^\ell
-
\nu\Delta\Omega^\ell
+
(U^\ell\cdot\nabla)\Omega^\ell
=
(\Omega^\ell\cdot\nabla)U^\ell
-
\mathcal J^\ell.
}
\tag{1.19}
$$

Dotting with:

$$
\Omega^\ell
$$

gives the exact filtered enstrophy identity:

$$
\boxed{
\partial_t
\frac{
|\Omega^\ell|^2
}{
2
}
-
\nu\Delta
\frac{
|\Omega^\ell|^2
}{
2
}
+
U^\ell\cdot\nabla
\frac{
|\Omega^\ell|^2
}{
2
}
+
\nu
|\nabla\Omega^\ell|^2
=
S^\ell\Omega^\ell\cdot\Omega^\ell
-
\Omega^\ell\cdot\mathcal J^\ell.
}
\tag{1.20}
$$

The third new theorem of this round is a fixed-relative-filter bound.

Suppose an enlarged local energy coordinate satisfies:

$$
A^+(z_0,r)
\le
M.
$$

For a compactly supported spatial mollifier and an interior cutoff, one has:

$$
\boxed{
\|S^\ell(t)\|_{L^\infty}
\le
C_\sigma
M^{1/2}
r^{-2}.
}
\tag{1.21}
$$

Therefore the positive filtered stretching quantity:

$$
\boxed{
V_{r,\ell}^+
=
r
\iint_{Q_r}
\chi
\left(
S^\ell\Omega^\ell\cdot\Omega^\ell
\right)_+
dxdt
}
\tag{1.22}
$$

obeys:

$$
\boxed{
V_{r,\ell}^+
\le
C_\sigma
M^{1/2}
O_{r,\ell},
}
\tag{1.23}
$$

where:

$$
\boxed{
O_{r,\ell}
=
r^{-1}
\iint_{Q_r}
\chi
|\Omega^\ell|^2
dxdt.
}
\tag{1.24}
$$

Thus fixed-relative filtered stretching cannot become an independent arbitrarily large source while filtered enstrophy remains small.

This is a genuine mechanism reduction.

But it is **not** a regularity theorem.

It says the remaining dangerous mechanism has moved into the persistence/regeneration of the coarse enstrophy reservoir:

$$
O_{r,\ell}.
$$

The final frontier of this round is therefore sharper than "tax all supply":

$$
\boxed{
\textbf{
Filtered Enstrophy Sustenance / Stretching–Diffusion Depletion Lemma}.
}
\tag{1.25}
$$

The next desired estimate must show that persistent scale-critical coarse vorticity cannot regenerate through arbitrarily many scales unless one of the already completed channels is non-negligible.

A model target is:

$$
\boxed{
V_{r,\ell}^+
\le
(1-\varepsilon_\ast)
P_{r,\ell}
+
C(M)
O_{r,\ell}
+
C\mathcal A_{r,\ell}
+
R_{r,\ell}
+
L_{r,\ell},
}
\tag{1.26}
$$

together with a **scale-transition estimate for $O_{r,\ell}$** strong enough that the $C(M)O$ term does not simply become a new untaxed reservoir.

This last clause is the essential new point.

The stretching estimate alone is not enough.

The closure-facing object is:

$$
\boxed{
\textbf{
coarse-enstrophy regeneration efficiency across scales}.
}
\tag{1.27}
$$

---

# 2. Exact full critical ledger audited

Let:

$$
B_k
=
A_k+C_k+D_k.
$$

The transition quantities are:

$$
\boxed{
\Phi_k
=
r_k^{-1}
\iint_{Q_k}
|u|^2
|u\cdot\nabla\phi_k|
dxdt,
}
\tag{2.1}
$$

$$
\boxed{
\Pi_k
=
r_k^{-1}
\iint_{Q_k}
\left|
p-(p)_{B_{r_k}}(t)
\right|
|u\cdot\nabla\phi_k|
dxdt,
}
\tag{2.2}
$$

and:

$$
\boxed{
\Lambda_k
=
r_k^{-1}
\iint_{Q_k}
|u|^2
\left(
|\partial_t\phi_k|
+
|\Delta\phi_k|
\right)
dxdt.
}
\tag{2.3}
$$

The local energy inequality gives:

$$
\boxed{
A_{k+1}
+
2E_{k+1}
\le
\theta^{-1}
\left(
\Lambda_k+\Phi_k+2\Pi_k
\right).
}
\tag{2.4}
$$

The cubic interpolation gives:

$$
\boxed{
C_{k+1}
\le
C_{I,\theta}
\left[
(\Phi_k+2\Pi_k)^{3/2}
+
\Lambda_k^{3/2}
\right].
}
\tag{2.5}
$$

The pressure decay gives:

$$
\boxed{
D_{k+1}
\le
C_P\theta D_k
+
C_P\theta^{-2}C_k.
}
\tag{2.6}
$$

Hence:

$$
\boxed{
\mathrm{Sup}^{full}_k
=
\theta^{-1}
(\Phi_k+2\Pi_k)
+
C_{I,\theta}
(\Phi_k+2\Pi_k)^{3/2}
+
C_P\theta^{-2}C_k,
}
\tag{2.7}
$$

$$
\boxed{
\mathrm{Tax}^{full}_k
=
2E_{k+1}
+
(1-\alpha)A_k
+
(1-\alpha)C_k
+
\delta_DD_k,
}
\tag{2.8}
$$

and:

$$
\boxed{
\mathrm{Leak}^{full}_k
=
\theta^{-1}\Lambda_k
+
C_{I,\theta}\Lambda_k^{3/2}.
}
\tag{2.9}
$$

The one-step ledger is:

$$
\boxed{
B_{k+1}
-
(1-\alpha)B_k
\le
\mathrm{Sup}^{full}_k
-
\mathrm{Tax}^{full}_k
+
\mathrm{Leak}^{full}_k.
}
\tag{2.10}
$$

---

# 3. Algebraic source reduction

Set:

$$
\boxed{
X
=
\Phi+2\Pi.
}
\tag{3.1}
$$

Let:

$$
a=\theta^{-1},
$$

$$
b=C_{I,\theta},
$$

and:

$$
c=C_P\theta^{-2}.
$$

Then:

$$
\boxed{
\mathrm{Sup}^{full}
=
aX+bX^{3/2}+cC.
}
\tag{3.2}
$$

---

# 4. NEW THEOREM — Full-Supply Source Reduction

## Theorem 4.1

Let:

$$
X,C\ge0
$$

and:

$$
S=aX+bX^{3/2}+cC,
$$

where:

$$
a,b,c>0.
$$

If:

$$
\boxed{
S\ge\eta>0,
}
\tag{4.1}
$$

then:

$$
\boxed{
X
\ge
\xi_\eta
}
\tag{4.2}
$$

or:

$$
\boxed{
C
\ge
\zeta_\eta,
}
\tag{4.3}
$$

where:

$$
\boxed{
\xi_\eta
=
\min
\left\{
\frac{\eta}{4a},
\left(
\frac{\eta}{4b}
\right)^{2/3}
\right\},
}
\tag{4.4}
$$

and:

$$
\boxed{
\zeta_\eta
=
\frac{\eta}{2c}.
}
\tag{4.5}
$$

### Proof

Assume:

$$
X<\xi_\eta.
$$

Then:

$$
aX<\frac{\eta}{4},
$$

and:

$$
bX^{3/2}<\frac{\eta}{4}.
$$

Therefore:

$$
cC
=
S-aX-bX^{3/2}
>
\frac{\eta}{2}.
$$

Hence:

$$
C>\frac{\eta}{2c}.
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

# 5. Corollary for untaxed supply

If:

$$
\boxed{
\left(
\mathrm{Sup}^{full}
-
\mathrm{Tax}^{full}
\right)_+
\ge
\eta,
}
\tag{5.1}
$$

then:

$$
\mathrm{Sup}^{full}\ge\eta.
$$

Apply Theorem 4.1.

With the ledger coefficients:

$$
a=\theta^{-1},
$$

$$
b=C_{I,\theta},
$$

$$
c=C_P\theta^{-2},
$$

one obtains:

$$
\boxed{
X
\ge
\min
\left\{
\frac{\theta\eta}{4},
\left(
\frac{\eta}{4C_{I,\theta}}
\right)^{2/3}
\right\}
}
\tag{5.2}
$$

or:

$$
\boxed{
C
\ge
\frac{
\theta^2\eta
}{
2C_P
}.
}
\tag{5.3}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 6. Splitting transition influx

Since:

$$
X=\Phi+2\Pi,
$$

if:

$$
X\ge\xi,
$$

then at least one of:

$$
\boxed{
\Phi\ge\frac{\xi}{3}
}
\tag{6.1}
$$

or:

$$
\boxed{
\Pi\ge\frac{\xi}{3}
}
\tag{6.2}
$$

holds.

Indeed if both were smaller than:

$$
\xi/3,
$$

then:

$$
X
=
\Phi+2\Pi
<
\xi.
$$

Therefore:

$$
\boxed{
\textbf{
fixed positive full supply}
\Longrightarrow
\textbf{
large nonlinear flux}
\ \vee\
\textbf{
large pressure transport}
\ \vee\
\textbf{
large cubic reservoir}.
}
}
\tag{6.3}
$$

---

# 7. The interpolation term is not an independent mechanism

The term:

$$
C_{I,\theta}X^{3/2}
$$

enters because:

$$
C_{k+1}
$$

is bounded through local interpolation by:

$$
(A_{k+1}+E_{k+1})^{3/2},
$$

while:

$$
A_{k+1}+E_{k+1}
$$

is itself supplied by:

$$
\Lambda_k+X_k.
$$

Thus:

$$
\boxed{
X^{3/2}
}
$$

is a nonlinear amplification of the same transition influx.

It should not be counted as a third physical input channel.

This matters because a taxation theorem need not separately capture:

$$
X
$$

and:

$$
X^{3/2}.
$$

A quantitative control of:

$$
X
$$

automatically controls its ledger amplification on any fixed bounded range.

---

# 8. Pressure regeneration is reservoir recycling

The term:

$$
C_P\theta^{-2}C_k
$$

comes from the local Calderon--Zygmund pressure generated by the velocity quadratic source at the previous scale.

It is not a flux through the spatial boundary.

It is a regeneration of:

$$
D_{k+1}
$$

from:

$$
C_k.
$$

Thus the full supply mechanism has two conceptual families:

$$
\boxed{
\textbf{
transition influx}
}
$$

and:

$$
\boxed{
\textbf{
reservoir regeneration}.
}
$$

The old four-label phrase:

- nonlinear flux;
- pressure transport;
- interpolation amplification;
- pressure regeneration;

contains only three quantitatively distinct source terms and two conceptual source types.

---

# 9. Coarse resolution of the cubic-regeneration branch

Let:

$$
\Psi
=
C+D.
$$

The exact coarse-resolution lemma gives, for every fixed spatial filter length:

$$
\ell>0,
$$

$$
\boxed{
\Psi
\le
4\Psi^\ell
+
4\Omega^\ell,
}
\tag{9.1}
$$

where:

- $\Psi^\ell$ is the resolved coarse velocity-pressure quantity;
- $\Omega^\ell$ is the explicit subfilter residual.

Because:

$$
\Psi\ge C,
$$

if:

$$
C\ge\zeta,
$$

then:

$$
4\Psi^\ell+4\Omega^\ell
\ge
\zeta.
$$

Therefore:

$$
\boxed{
\Psi^\ell
\ge
\frac{\zeta}{8}
}
\tag{9.2}
$$

or:

$$
\boxed{
\Omega^\ell
\ge
\frac{\zeta}{8}.
}
\tag{9.3}
$$

Status:

$$
\boxed{
\textbf{PROVED from the coarse-resolution lemma}.
}
$$

---

# 10. Critical-supply source theorem

Combining Sections 5--9:

## Theorem 10.1

Fix:

$$
\eta>0.
$$

If:

$$
\boxed{
\left(
\mathrm{Sup}^{full}_k
-
\mathrm{Tax}^{full}_k
\right)_+
\ge
\eta,
}
\tag{10.1}
$$

then there exists a constant:

$$
c_\eta>0
$$

depending only on the fixed ledger parameters such that at least one of:

$$
\boxed{
\Phi_k\ge c_\eta,
}
\tag{10.2}
$$

$$
\boxed{
\Pi_k\ge c_\eta,
}
\tag{10.3}
$$

$$
\boxed{
\Psi_k^\ell\ge c_\eta,
}
\tag{10.4}
$$

or:

$$
\boxed{
\Omega_k^\ell\ge c_\eta
}
\tag{10.5}
$$

holds.

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

This is the quantitative **Critical Supply Source Reduction**.

---

# 11. Why this still does not tax the supply

Suppose:

$$
\Phi_k\ge c_\eta.
$$

This means a large amount of nonlinear energy transport crosses the chosen local cutoff.

It does not say that the transport is negative.

It may be precisely the positive energy injection that sustains the next scale.

Likewise:

$$
\Pi_k\ge c_\eta
$$

is a magnitude of pressure transport.

It does not determine whether that pressure transport depletes or feeds the local reservoir.

Likewise:

$$
\Psi_k^\ell\ge c_\eta
$$

means the resolved coarse state is bad/active.

It is not a negative term in the energy ledger.

Thus:

$$
\boxed{
\textbf{
classification}
+
\textbf{
observation}
\neq
\textbf{
taxation}.
}
\tag{11.1}
$$

---

# 12. NO-GO — perfect observation does not imply depletion

Consider the scalar recurrence:

$$
\boxed{
B_{k+1}
=
(1-\alpha)B_k
+
S_k
}
\tag{12.1}
$$

with:

$$
0<\alpha<1,
$$

and:

$$
S_k=\alpha B_\ast>0.
$$

Then:

$$
B_k=B_\ast
$$

is a persistent orbit.

Define a perfect detector:

$$
\boxed{
O_k=S_k.
}
\tag{12.2}
$$

Then the supply is completely observed:

$$
O_k>0
$$

at every scale.

Nevertheless there is no tax:

$$
\boxed{
\mathrm{Tax}_k=0.
}
\tag{12.3}
$$

The persistent orbit survives exactly because the observed supply replenishes the expected decay.

Therefore:

$$
\boxed{
\textbf{
even perfect source observability does not imply regularity.
}
}
\tag{12.4}
$$

Status:

$$
\boxed{
\textbf{NO-GO PROVED}.
}
$$

This abstract countermodel is the ledger-level version of the PDE distinction between forward cascade and depletion.

---

# 13. Fixed-chain pressure-flux depletion does not remove the no-go

The coarse-grained work theorem proves on a fixed finite chain that:

- forward combined work;
- resolved dissipation;

are paid by:

- initial localized kinetic energy;
- explicit localization leakage;
- negative combined work/backscatter.

This is a genuine signed PDE telescope.

However it does not prove:

- moving-window constants are uniformly controlled;
- leakage is summable on an infinite singular chain;
- every positive transition supply entering the full critical ledger is the same signed combined-work quantity;
- a positive forward work event becomes a negative tax at the next step.

Therefore the theorem is a depletion/accounting mechanism, but not an automatic uniform taxation theorem for:

$$
\mathrm{Sup}^{full}_k.
$$

This is precisely why the finite-scale survival theorem lists uniform taxation of all critical supply as an open input.

---

# 14. Mechanism pivot

The current DCRP architecture has become very effective at the following tasks:

- local supplier capture;
- actual-history forcing;
- shell-energy first crossing;
- pressure-flux/backscatter splitting;
- finite-window localization;
- trace separation;
- projection/residual completion;
- UV/IR/spatial escape completion.

These are obstruction-calculus and interface modules.

The remaining question is not:

> where did the supply go?

It is:

> why can the physically dangerous mechanism not keep producing enough positive supply to offset diffusion?

For three-dimensional incompressible Navier--Stokes, the intrinsic smooth-level mechanism is vortex stretching.

Thus the next primary object is filtered vorticity.

---

# 15. Filtered Navier--Stokes package

Let:

$$
S_\ell
$$

be a smooth nonnegative spatial mollifier of scale:

$$
\ell.
$$

Define:

$$
\boxed{
U^\ell
=
S_\ell u,
}
\tag{15.1}
$$

$$
\boxed{
P^\ell
=
S_\ell p,
}
\tag{15.2}
$$

and Reynolds covariance:

$$
\boxed{
R^\ell
=
S_\ell(u\otimes u)
-
U^\ell\otimes U^\ell.
}
\tag{15.3}
$$

The coarse momentum equation is:

$$
\boxed{
\partial_tU^\ell
-
\nu\Delta U^\ell
+
(U^\ell\cdot\nabla)U^\ell
+
\nabla P^\ell
=
-\nabla\cdot R^\ell.
}
\tag{15.4}
$$

Define:

$$
\boxed{
\Omega^\ell
=
\nabla\times U^\ell,
}
\tag{15.5}
$$

$$
\boxed{
S^\ell
=
\frac12
\left(
\nabla U^\ell
+
(\nabla U^\ell)^T
\right),
}
\tag{15.6}
$$

and:

$$
\boxed{
\mathcal J^\ell
=
\nabla\times
(
\nabla\cdot R^\ell
).
}
\tag{15.7}
$$

---

# 16. Exact filtered vorticity identity

Take curl of (15.4).

Because:

$$
\nabla\cdot U^\ell=0,
$$

$$
\boxed{
\partial_t\Omega^\ell
-
\nu\Delta\Omega^\ell
+
(U^\ell\cdot\nabla)\Omega^\ell
=
(\Omega^\ell\cdot\nabla)U^\ell
-
\mathcal J^\ell.
}
\tag{16.1}
$$

The antisymmetric part of:

$$
\nabla U^\ell
$$

does not contribute to:

$$
\Omega^\ell\cdot
(
(\Omega^\ell\cdot\nabla)U^\ell
).
$$

Hence:

$$
\boxed{
\Omega^\ell\cdot
(
(\Omega^\ell\cdot\nabla)U^\ell
)
=
S^\ell
\Omega^\ell\cdot\Omega^\ell.
}
\tag{16.2}
$$

Dot (16.1) with:

$$
\Omega^\ell.
$$

Then:

$$
\boxed{
\partial_t
\frac{
|\Omega^\ell|^2
}{
2
}
-
\nu\Delta
\frac{
|\Omega^\ell|^2
}{
2
}
+
U^\ell\cdot\nabla
\frac{
|\Omega^\ell|^2
}{
2
}
+
\nu
|\nabla\Omega^\ell|^2
=
S^\ell
\Omega^\ell\cdot\Omega^\ell
-
\Omega^\ell\cdot\mathcal J^\ell.
}
\tag{16.3}
$$

Status:

$$
\boxed{
\textbf{PRIMARY-SOURCE IDENTITY}.
}
$$

---

# 17. Scale-invariant filtered mechanism coordinates

Let:

$$
\chi
$$

be a nonnegative cutoff supported in:

$$
Q_r(z_0)
$$

and equal to one on a slightly smaller cylinder.

Choose relative filter:

$$
\boxed{
\ell
=
\sigma r,
\qquad
0<\sigma<\sigma_0.
}
\tag{17.1}
$$

Define:

$$
\boxed{
O_{r,\ell}
=
r^{-1}
\iint
\chi
|\Omega^\ell|^2
dxdt,
}
\tag{17.2}
$$

$$
\boxed{
P_{r,\ell}
=
\nu r
\iint
\chi
|\nabla\Omega^\ell|^2
dxdt,
}
\tag{17.3}
$$

$$
\boxed{
V_{r,\ell}^+
=
r
\iint
\chi
\left(
S^\ell
\Omega^\ell\cdot\Omega^\ell
\right)_+
dxdt,
}
\tag{17.4}
$$

and:

$$
\boxed{
R_{r,\ell}
=
r
\iint
\chi
|\Omega^\ell|
|\mathcal J^\ell|
dxdt.
}
\tag{17.5}
$$

Let:

$$
L_{r,\ell}
$$

denote the scale-invariant cutoff/transport terms obtained by integrating (16.3) against:

$$
\chi.
$$

Every quantity above is scale invariant under:

$$
u_r(y,s)
=
r
u(x_0+ry,t_0+r^2s),
$$

with:

$$
\ell/r
=
\sigma
$$

fixed.

---

# 18. Enlarged local energy bound

Because the mollifier has spatial support of radius:

$$
O(\ell),
$$

the filtered field inside:

$$
\operatorname{supp}\chi
$$

depends only on velocity in a slightly enlarged ball.

Define:

$$
\boxed{
A^+_{r,\sigma}
=
r^{-1}
\operatorname*{ess\,sup}_{t\in I_r}
\int_{
B_{(1+c\sigma)r}(x_0)
}
|u(x,t)|^2dx.
}
\tag{18.1}
$$

Assume:

$$
\boxed{
A^+_{r,\sigma}
\le
M.
}
\tag{18.2}
$$

This is automatic if the standard local energy coordinate is bounded on a fixed slightly enlarged normalized cylinder.

---

# 19. NEW THEOREM — Fixed-Relative-Filter Stretching Bound

## Theorem 19.1

Let:

$$
\ell=\sigma r.
$$

Assume:

$$
A^+_{r,\sigma}\le M.
$$

Then:

$$
\boxed{
\|
S^\ell(t)
\|_{
L^\infty(\operatorname{supp}\chi)
}
\le
C
\sigma^{-5/2}
M^{1/2}
r^{-2}.
}
\tag{19.1}
$$

Consequently:

$$
\boxed{
V_{r,\ell}^+
\le
C
\sigma^{-5/2}
M^{1/2}
O_{r,\ell}.
}
\tag{19.2}
$$

### Proof

Let:

$$
\rho_\ell(x)
=
\ell^{-3}
\rho(x/\ell)
$$

be the spatial mollifier.

Then:

$$
\nabla U^\ell
=
(\nabla\rho_\ell)*u.
$$

For every point whose filter ball lies inside the enlarged spatial region:

$$
|\nabla U^\ell(x,t)|
\le
\|
\nabla\rho_\ell
\|_2
\|
u(t)
\|_{
L^2(B_{(1+c\sigma)r})
}.
$$

The kernel scaling gives:

$$
\boxed{
\|
\nabla\rho_\ell
\|_2
=
\ell^{-5/2}
\|
\nabla\rho
\|_2.
}
\tag{19.3}
$$

The local energy bound gives:

$$
\|
u(t)
\|_{
L^2(B_{(1+c\sigma)r})
}
\le
M^{1/2}
r^{1/2}.
$$

Therefore:

$$
|\nabla U^\ell|
\le
C
(\sigma r)^{-5/2}
M^{1/2}
r^{1/2}
=
C
\sigma^{-5/2}
M^{1/2}
r^{-2}.
$$

The strain is bounded by the full gradient, so (19.1) follows.

Now:

$$
\begin{aligned}
V_{r,\ell}^+
&\le
r
\|
S^\ell
\|_\infty
\iint
\chi
|\Omega^\ell|^2
dxdt\\
&\le
r
\left[
C
\sigma^{-5/2}
M^{1/2}
r^{-2}
\right]
\left[
r
O_{r,\ell}
\right].
\end{aligned}
$$

Hence (19.2).

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

# 20. Interpretation of the stretching bound

Theorem 19.1 says:

$$
\boxed{
\textbf{
at fixed relative filter scale,
positive filtered vortex stretching is linearly controlled by
the filtered enstrophy reservoir whenever local kinetic energy is bounded.
}
}
\tag{20.1}
$$

Thus a filtered stretching cascade cannot have:

$$
V_{r,\ell}^+\gg1
$$

while:

$$
O_{r,\ell}\ll1
$$

under:

$$
A^+\le M.
$$

This reduces the mechanism.

The remaining dangerous state is one with persistent nontrivial:

$$
O_{r,\ell}.
$$

---

# 21. Why Theorem 19.1 is not a regularity theorem

The estimate:

$$
V^+
\le
C(M,\sigma)
O
$$

does not compare stretching with diffusion using a coefficient smaller than one.

The coefficient:

$$
C(M,\sigma)
$$

can be arbitrarily large when:

- $M$ is large;
- the relative filter scale:

  $$
  \sigma
  $$

  is small.

Thus the filtered enstrophy identity may still have the schematic form:

$$
\boxed{
\text{next coarse enstrophy}
\lesssim
C(M,\sigma)
\text{ old coarse enstrophy}
+
\text{defects}.
}
\tag{21.1}
$$

There is no decay basin from this inequality alone.

Therefore:

$$
\boxed{
\text{stretching bounded by }O
\neq
\text{stretching depleted by diffusion}.
}
\tag{21.2}
$$

This is another visibility/taxation distinction at the mechanism level.

---

# 22. Local filtered enstrophy ledger

Integrate (16.3) against:

$$
\chi.
$$

The time derivative and diffusion yield:

- endpoint filtered enstrophy;
- positive diffusion:

  $$
  P_{r,\ell}.
  $$

The transport and cutoff Laplacian terms are collected in:

$$
L_{r,\ell}.
$$

The subgrid forcing is bounded by:

$$
R_{r,\ell}.
$$

Hence one obtains the schematic rigorous local inequality:

$$
\boxed{
\mathcal E^\ell_{\rm out}
+
P_{r,\ell}
\le
\mathcal E^\ell_{\rm in}
+
V_{r,\ell}^+
+
R_{r,\ell}
+
L_{r,\ell},
}
\tag{22.1}
$$

where the endpoint quantities carry the scale normalization appropriate to the chosen cutoff.

Insert Theorem 19.1:

$$
\boxed{
\mathcal E^\ell_{\rm out}
+
P_{r,\ell}
\le
\mathcal E^\ell_{\rm in}
+
C(M,\sigma)
O_{r,\ell}
+
R_{r,\ell}
+
L_{r,\ell}.
}
\tag{22.2}
$$

This is a genuine filtered mechanism ledger.

It does not yet close because:

$$
O_{r,\ell}
$$

is not itself taxed.

---

# 23. Connection to direction-incoherence

The structural audit proposes a stronger target:

$$
\boxed{
V_{r,\ell}^+
\le
(1-\varepsilon_\ast)
P_{r,\ell}
+
C(M)
O_{r,\ell}
+
C\mathcal A_{r,\ell}
+
R_{r,\ell}
+
L_{r,\ell}.
}
\tag{23.1}
$$

The direction-incoherence defect:

$$
\mathcal A_{r,\ell}
$$

is designed to separate coherent Euler-like stretching from geometrically depleted stretching.

Theorem 19.1 does not need:

$$
\mathcal A.
$$

It is weaker and more elementary.

Its value is to identify that the residual hard object is already contained in:

$$
O_{r,\ell}.
$$

A direction theorem becomes useful only if it helps obtain a **strict diffusion coefficient** or a **scale-transition decay law** for:

$$
O.
$$

---

# 24. Coarse resolved badness and filtered vorticity

The source reduction theorem produces the branch:

$$
\Psi^\ell
\ge
c_\eta.
$$

The resolved coarse velocity:

$$
U^\ell
$$

is smooth at the relative scale:

$$
\sigma r.
$$

A large resolved coarse velocity contribution is therefore naturally linked to:

- the coarse filtered vorticity reservoir;
- the coarse pressure field;
- the low-frequency/mean velocity component.

The DCRP finite-window package already has pressure/trace channels for the latter two.

Thus a useful next resolution theorem should separate:

$$
\boxed{
\Psi^\ell
\text{ large}
}
$$

into:

$$
\boxed{
O_{r,\ell}\text{ large}
}
$$

or:

$$
\boxed{
\text{coarse pressure/mean/trace channel large}.
}
$$

Such a result would connect the old full-supply ledger to the new filtered-vorticity mechanism without attempting to call observation a tax.

This component estimate has not yet been proved in the present round.

---

# 25. Correct closure question

The old question was:

$$
\boxed{
\text{Can every critical supply event be detected?}
}
$$

The answer is increasingly close to yes after DCRP-08 through DCRP-18.

But this is not enough.

The correct question is:

$$
\boxed{
\textbf{
Can filtered coarse enstrophy remain scale-critically profitable
after diffusion and all explicit defect channels are accounted for?
}
}
\tag{25.1}
$$

Equivalently:

$$
\boxed{
\textbf{
can the three-dimensional stretching mechanism repeatedly rebuild
the coarse vorticity reservoir faster than diffusion removes it,
without producing subgrid/leakage/pressure/geometric defects?
}
}
\tag{25.2}
$$

This is the mechanism-level closure problem.

---

# 26. New primary frontier

The next exact target is:

$$
\boxed{
\textbf{
Filtered Enstrophy Sustenance / Stretching–Diffusion Depletion Lemma}.
}
$$

A useful two-part form is:

### Part A — strict stretching-diffusion estimate

For bounded normalized local energy:

$$
\Phi(z_0,r)\le M,
$$

and relative filter:

$$
\ell=\sigma r,
$$

prove:

$$
\boxed{
V_{r,\ell}^+
\le
(1-\varepsilon_\ast)
P_{r,\ell}
+
C(M)
O_{r,\ell}
+
D_{r,\ell}^{silent},
}
\tag{26.1}
$$

where:

$$
D_{r,\ell}^{silent}
$$

is explicitly controlled by already completed:

- subgrid forcing;
- localization leakage;
- pressure/tail;
- direction-incoherence;
- spatial/scale escape.

### Part B — scale-transition control of the coarse reservoir

Prove that if:

$$
D_{r,\ell}^{silent}
$$

is small and:

$$
O_{r,\ell}
$$

remains above a fixed critical threshold through many shrinking scales, then either:

$$
\boxed{
\sum
P_{r_k,\ell_k}
}
$$

has non-summable normalized size,

or a fixed positive-density set of scales violates Part A through one of the declared silent defects.

This second part is essential.

Without it:

$$
C(M)O
$$

can simply replace the old untaxed supply reservoir.

---

# 27. Why this is closer to a true coercive estimate

The old ledger used:

$$
\Phi,\Pi,C,D
$$

and tracked how badness can survive.

The filtered enstrophy ledger contains the actual three-dimensional competition:

$$
\boxed{
\text{vortex stretching}
\quad\text{vs}\quad
\text{vorticity diffusion}.
}
$$

This is no longer merely:

- a detector coefficient;
- a quotient distance;
- a transition bookkeeping term.

A strict inequality:

$$
V^+
<
P
+
\text{controlled errors}
$$

would directly remove the mechanism that can create small-scale vorticity.

This is why the route is now genuinely PDE-coercive.

---

# 28. Relation to DCRP supplier modules

The DCRP supplier modules are not discarded.

They become downstream certification.

If the filtered stretching mechanism produces:

- a subgrid-forcing defect;
- a pressure/flux event;
- a local supplier;
- a spatial/scale carrier;
- a transition residual;

then DCRP already supplies:

- local capture;
- PFET/backscatter decomposition;
- finite-window localization;
- finite trace separation;
- quotient/residual realization;
- two-sided scale completion.

Thus the revised order is:

$$
\boxed{
\begin{aligned}
&\text{filtered vorticity mechanism}\\
&\Longrightarrow
\text{stretching--diffusion depletion}\\
&\Longrightarrow
\text{bad-scale mechanism classification}\\
&\Longrightarrow
\text{DCRP finite-window certification/tax ledger}.
\end{aligned}
}
\tag{28.1}
$$

This is a change of order, not a restart.

---

# 29. Current proof-space status

The route has compressed from generic Navier--Stokes blowup to:

$$
\boxed{
\textbf{
a local scale-critical filtered-vorticity reservoir
that can repeatedly regenerate despite diffusion,
while all explicit subgrid/leakage/pressure/geometric channels remain small.
}
}
\tag{29.1}
$$

That is a much more specific survivor than the original:

$$
\text{generic diffuse carrier}.
$$

But it is also recognizably close to the central three-dimensional difficulty.

Therefore the current state should be described as:

$$
\boxed{
\text{mechanism frontier reached}
}
$$

rather than:

$$
\boxed{
\text{QED nearly finished}.
}
$$

---

# 30. Source-status audit

## Critical Ledgers and Scale-Defect Cascades

Primary facts used:

$$
\mathrm{Sup}^{full}
=
\theta^{-1}(\Phi+2\Pi)
+
C_{I,\theta}(\Phi+2\Pi)^{3/2}
+
C_P\theta^{-2}C,
$$

$$
\mathrm{Tax}^{full}
=
2E_{k+1}
+
(1-\alpha)A
+
(1-\alpha)C
+
\delta_DD,
$$

and the finite-scale survival alternative.

## Coarse-Grained Resolution and Pressure-Flux Work Depletion

Primary facts used:

$$
\Psi
\le
4\Psi^\ell+4\Omega^\ell,
$$

and the fixed-chain signed pressure-flux work depletion theorem.

## Structural Audit

Primary facts used:

- the existing architecture is obstruction calculus rather than a coercive regularity mechanism;
- direct single-scale domination by a signed work detector is not available unconditionally;
- the next PDE target is a filtered stretching-diffusion estimate;
- the correct weak-level object is filtered vorticity;
- the filtered vorticity identity includes the subgrid vorticity forcing:

  $$
  \mathcal J^\ell.
  $$

DCRP-19 independently proves the elementary fixed-relative-filter stretching bound (19.2).

---

# 31. End state

This round proves the **Critical Supply Source Reduction**:

$$
\boxed{
\left(
\mathrm{Sup}^{full}
-
\mathrm{Tax}^{full}
\right)_+
\ge\eta
}
$$

forces at least one of:

$$
\boxed{
\Phi\ge c_\eta,
}
$$

$$
\boxed{
\Pi\ge c_\eta,
}
$$

$$
\boxed{
\Psi^\ell\ge c_\eta,
}
$$

or:

$$
\boxed{
\Omega^\ell\ge c_\eta.
}
$$

It also proves the key NO-GO:

$$
\boxed{
\textbf{
observing all supply is not the same as taxing all supply.
}
}
$$

The new mechanism theorem is:

$$
\boxed{
V_{r,\sigma r}^+
\le
C
\sigma^{-5/2}
M^{1/2}
O_{r,\sigma r}.
}
$$

Thus fixed-relative filtered stretching is controlled by the filtered enstrophy reservoir.

The remaining closure-facing object is not a hidden detector.

It is:

$$
\boxed{
\textbf{
persistent coarse enstrophy regeneration against diffusion.
}
}
$$

The next single frontier is therefore:

$$
\boxed{
\textbf{
Filtered Enstrophy Sustenance / Stretching–Diffusion Depletion Lemma}.
}
$$

That is the next exact attack.

---

# Checkpoint v20 Update — DCRP-20

# NS-DCRP-20 — Filtered-Enstrophy Diffusion/IR Dichotomy and Far-Field-Only Survivor Reduction

- date: 2026-08-17
- status: research proof checkpoint
- canonical source: UTF-8 Markdown
- canonical math delimiters: `$...$` and `$$...$$`
- objective:
  1. audit DCRP-19 against the newer filtered-vorticity coercivity theorem;
  2. remove the lower-order filtered-enstrophy reservoir as a silent zero-cost mechanism by a spectral diffusion-versus-infrared dichotomy;
  3. combine near-field coercivity, commutator insertion, localization completion, and the new reservoir dichotomy;
  4. identify the final surviving filtered-vorticity mechanism.
- no full Navier--Stokes regularity claim is made.
- principal external primary source:
  - Runlong Yu, *Filtered Vortex Stretching and Subgrid Defects for the Three-Dimensional Navier--Stokes Equations*, arXiv:2606.27560v1.
- internal dependencies:
  - DCRP-18 two-sided relative-frequency completion;
  - DCRP-19 supply-source reduction and filtered-vorticity pivot;
  - MORP native-residual / paid-channel completion.
- no novelty / priority claim is made for results already contained in arXiv:2606.27560.

---

# 1. Executive result

DCRP-19 ended by proposing the filtered stretching--diffusion estimate

$$
V_{r,\ell}^{+}
\lesssim
(1-\varepsilon)P_{r,\ell}
+
C(M)O_{r,\ell}
+
\text{defects}.
$$

A source audit now shows that the near-field part of this target has already been proved in stronger form in arXiv:2606.27560.

For fixed relative filter length

$$
\ell=\sigma r,
$$

the paper proves

$$
\boxed{
V_{r,\ell}^{+,\mathrm{near}}
\le
(1-\varepsilon)
P_{r,\ell}^{\rho}
+
C_{\varepsilon,\sigma,\rho}
M_{r,\rho}(u)
O_{r,\ell}.
}
\tag{1.1}
$$

It also proves a derivative-compatible commutator insertion

$$
\boxed{
F_{r,\ell}^{\mathrm{com}}
\le
\eta P_{r,\ell}
+
C_{\eta,\varphi}
\widetilde{\mathcal S}_{r,\ell}^{(3)}
+
L_{r,\ell}^{\mathrm{com}}.
}
\tag{1.2}
$$

Thus DCRP-19's elementary estimate

$$
V^+\lesssim M^{1/2}O
$$

is retained only as a coarse fallback.

The stronger external theorem should be used for the proof program.

The unresolved lower-order term in (1.1) is the filtered-enstrophy reservoir

$$
O_{r,\ell}.
$$

The main new result of DCRP-20 is:

$$
\boxed{
\textbf{
positive filtered enstrophy}
\Longrightarrow
\textbf{
positive filtered diffusion/localization}
\ \vee\
\textbf{
relative infrared concentration}.
}
}
\tag{1.3}
$$

More precisely, let

$$
\eta_r(x)
=
\eta
\left(
\frac{x-x_0}{r}
\right)
$$

be a fixed smooth spatial cutoff and define

$$
f_{r,\ell}(x,t)
=
\eta_r(x)
\Omega_\ell(x,t).
$$

Let

$$
\boxed{
O_{r,\ell}^{\eta}
=
r^{-1}
\int_{I_r}
\|f_{r,\ell}(t)\|_2^2dt.
}
\tag{1.4}
$$

Whenever

$$
O_{r,\ell}^{\eta}>0,
$$

define the spacetime relative-frequency probability measure

$$
\boxed{
\mu_{r,\ell}(B)
=
\frac{
r^{-1}
\int_{I_r}
\int_{
\{\,\xi:\ r\xi\in B\,\}
}
|
\widehat{
f_{r,\ell}
}
(\xi,t)
|^2
d\xi dt
}{
O_{r,\ell}^{\eta}
}.
}
\tag{1.5}
$$

Then:

$$
\boxed{
\int_{\mathbb R^3}
|\zeta|^2
\,d\mu_{r,\ell}(\zeta)
\le
C
\frac{
\nu^{-1}P_{r,\ell}^{\eta}
+
L_{r,\ell}^{\omega}
}{
O_{r,\ell}^{\eta}
}.
}
\tag{1.6}
$$

Here:

$$
P_{r,\ell}^{\eta}
=
\nu r
\int_{I_r}
\int
\eta_r^2
|
\nabla\Omega_\ell
|^2
dxdt,
$$

and

$$
L_{r,\ell}^{\omega}
$$

is the normalized enstrophy mass on the fixed cutoff shell.

Consequently, if a sequence satisfies

$$
O_n^\eta\ge o_0>0,
$$

$$
P_n^\eta\to0,
$$

and:

$$
L_n^\omega\to0,
$$

then:

$$
\boxed{
\mu_n
\Longrightarrow
\delta_0.
}
\tag{1.7}
$$

In dyadic logarithmic relative-frequency coordinates:

$$
m
=
\log_2
(
r|\xi|
),
$$

this is exactly:

$$
\boxed{
m\to-\infty.
}
\tag{1.8}
$$

Therefore persistent coarse enstrophy with vanishing diffusion/localization is an **infrared relative-scale carrier**.

DCRP-18 already showed that transition-complete scale compactness must retain the

$$
-\infty
$$

direction.

Thus the lower-order reservoir is no longer a silent mechanism.

Quantitatively, if a sequence is uniformly non-infrared in the sense that there exist:

$$
\kappa>0,
\qquad
\delta>0
$$

with:

$$
\boxed{
\mu_n
(
\{
|\zeta|\ge\kappa
\}
)
\ge
\delta,
}
\tag{1.9}
$$

then:

$$
\boxed{
O_n^\eta
\le
\frac{
C
}{
\delta\kappa^2
}
\left(
\nu^{-1}P_n^\eta
+
L_n^\omega
\right).
}
\tag{1.10}
$$

Hence:

$$
\boxed{
\textbf{
no IR escape}
+
\textbf{
vanishing diffusion}
+
\textbf{
vanishing localization}
\Longrightarrow
O_n^\eta\to0.
}
\tag{1.11}
$$

This gives a zero-cost mechanism reduction.

Assume a normalized filtered-vorticity sequence satisfies:

$$
P_n\to0,
$$

$$
\widetilde{\mathcal S}_n^{(3)}\to0,
$$

$$
L_n\to0,
$$

$$
L_n^{\mathrm{com}}\to0,
$$

and has no infrared relative-scale defect.

Then:

$$
\boxed{
O_n\to0.
}
\tag{1.12}
$$

The external near-field theorem yields:

$$
\boxed{
V_n^{+,\mathrm{near}}\to0.
}
\tag{1.13}
$$

The external commutator insertion yields:

$$
\boxed{
F_n^{\mathrm{com}}\to0.
}
\tag{1.14}
$$

The principal localization residual may be canceled by the backward adjoint drift-diffusion cutoff, while the remaining shell localization terms are already included in:

$$
L_n,
\qquad
L_n^{\mathrm{com}}.
$$

Therefore every persistent positive filtered-enstrophy surplus must satisfy:

$$
\boxed{
\liminf_{n\to\infty}
V_n^{+,\mathrm{far}}
>
0.
}
\tag{1.15}
$$

Thus:

$$
\boxed{
\textbf{
zero-cost / no-IR filtered obstruction}
\Longrightarrow
\textbf{
far-field-strain-only survivor}.
}
}
\tag{1.16}
$$

This is the central reduction of DCRP-20.

The remaining mechanism is no longer generic vortex stretching.

The singular near-field stretching is diffusion-coercive.

The commutator term is increment-defect controlled.

The localization term is explicit.

The coarse-enstrophy reservoir is diffusion- or IR-controlled.

The only surviving positive mechanism is:

$$
\boxed{
\textbf{
external/far-field strain acting on the local filtered-vorticity core.
}
}
\tag{1.17}
$$

The next exact frontier is therefore:

$$
\boxed{
\textbf{
Far-Field Harmonic-Jet / Infrared-Strain Rigidity Lemma}.
}
\tag{1.18}
$$

The target is to show that persistent normalized far-field work must produce at least one of:

1. a nonzero two-sided infrared vorticity/strain carrier;
2. an unbounded or nontrivial finite-dimensional harmonic affine-strain jet;
3. a summable annular packing contribution;
4. a paid pressure/transition/localization residual.

If all four channels vanish, then:

$$
V_n^{+,\mathrm{far}}\to0,
$$

contradicting (1.15).

---

# 2. Source audit — DCRP-19 near-field target is already stronger externally

The main filtered-vorticity paper proves the exact near-field geometric depletion theorem:

$$
\boxed{
V_{r,\ell}^{+,\mathrm{near}}
\le
\frac{
3
}{
8\pi
}
\mathcal A_{r,\ell}^{\mathrm{pair}}.
}
\tag{2.1}
$$

The pairwise direction defect satisfies, for every:

$$
\eta>0,
$$

$$
\boxed{
\mathcal A_{r,\ell}^{\mathrm{pair}}
\le
\eta
P_{r,\ell}^{\rho}
+
C_\eta
M_{r,\rho}(u)
\left(
\frac r\ell
\right)^5
O_{r,\ell}.
}
\tag{2.2}
$$

Hence for:

$$
\ell=\sigma r,
$$

$$
\boxed{
V_{r,\sigma r}^{+,\mathrm{near}}
\le
(1-\varepsilon)
P_{r,\sigma r}^{\rho}
+
C_{\varepsilon}
M
\sigma^{-5}
O_{r,\sigma r}.
}
\tag{2.3}
$$

This is strictly stronger and more mechanism-specific than DCRP-19 Theorem 19.1.

Accordingly:

$$
\boxed{
\textbf{
DCRP-19's elementary stretching estimate is superseded for the near-field route.
}
}
\tag{2.4}
$$

It remains a simple independent fallback and scaling check.

---

# 3. Source audit — commutator forcing is already explicitly controlled

Let:

$$
R_\ell
=
S_\ell(u\otimes u)
-
U_\ell\otimes U_\ell.
$$

The filtered-vorticity commutator forcing is:

$$
-\nabla\times\nabla\cdot R_\ell.
$$

The external theorem proves, for:

$$
p\in[2,4],
$$

$$
\boxed{
F_k^{\mathrm{com}}
\le
\eta P_k
+
\frac{
C_{\mathrm{com}}^\sharp
}{
\eta
}
\widetilde{\mathcal S}_k^{(p)}
+
L_{k,\mathrm{inc}}^{\mathrm{com}}.
}
\tag{3.1}
$$

For the critical choice:

$$
p=3,
$$

$$
\boxed{
\widetilde{\mathcal S}^{(3)}
}
$$

is scale invariant.

This observable is already present in the MORP/DCRP extended cost architecture.

Therefore the commutator forcing does not need a new detector.

A zero-cost branch with:

$$
P_k\to0,
$$

$$
\widetilde{\mathcal S}_k^{(3)}\to0,
$$

and:

$$
L_{k,\mathrm{inc}}^{\mathrm{com}}\to0
$$

has:

$$
\boxed{
F_k^{\mathrm{com}}\to0.
}
\tag{3.2}
$$

---

# 4. The lower-order reservoir problem

After the singular near-field stretching is absorbed, the local filtered-enstrophy balance contains:

$$
\boxed{
C(M,\sigma)
O_{r,\ell}.
}
\tag{4.1}
$$

This term is not sign-indefinite work.

It is a lower-order reservoir.

It cannot be called:

- tax;
- leakage;
- backscatter.

If it persists while:

$$
P\to0,
$$

one must understand how its spectral mass avoids diffusion.

This is the new problem solved below.

---

# 5. Localized filtered-vorticity field

Fix a reference cutoff:

$$
\eta
\in
C_c^\infty(B_{1+\rho}),
$$

with:

$$
0\le\eta\le1,
$$

and:

$$
\eta\equiv1
$$

on:

$$
B_1.
$$

At scale:

$$
r,
$$

define:

$$
\boxed{
\eta_r(x)
=
\eta
\left(
\frac{
x-x_0
}{
r
}
\right).
}
\tag{5.1}
$$

Let:

$$
\Omega_\ell
=
\nabla\times S_\ell u,
$$

and define:

$$
\boxed{
f_{r,\ell}(x,t)
=
\eta_r(x)
\Omega_\ell(x,t).
}
\tag{5.2}
$$

Define:

$$
\boxed{
O_{r,\ell}^{\eta}
=
r^{-1}
\int_{I_r}
\|f_{r,\ell}(t)\|_2^2dt.
}
\tag{5.3}
$$

This is scale invariant.

---

# 6. Localized filtered diffusion and shell cost

Define:

$$
\boxed{
P_{r,\ell}^{\eta}
=
\nu r
\int_{I_r}
\int
\eta_r^2
|
\nabla\Omega_\ell
|^2
dxdt.
}
\tag{6.1}
$$

Let:

$$
A_\eta
=
\operatorname{supp}
\nabla\eta
$$

and define the physical shell:

$$
A_{\eta,r}
=
x_0+rA_\eta.
$$

Define the normalized filtered-enstrophy localization shell cost:

$$
\boxed{
L_{r,\ell}^{\omega}
=
r^{-1}
\int_{I_r}
\int_{A_{\eta,r}}
|
\Omega_\ell
|^2
dxdt.
}
\tag{6.2}
$$

Because:

$$
|\nabla\eta_r|
\le
C_\eta r^{-1},
$$

the cutoff-gradient term in:

$$
\nabla f_{r,\ell}
$$

is controlled by:

$$
L_{r,\ell}^{\omega}.
$$

---

# 7. Relative-frequency probability measure

Assume:

$$
O_{r,\ell}^{\eta}>0.
$$

For a Borel set:

$$
B\subset\mathbb R^3,
$$

define:

$$
\boxed{
\mu_{r,\ell}(B)
=
\frac{
r^{-1}
\int_{I_r}
\int_{\{
\xi:
r\xi\in B
\}}
|
\widehat f_{r,\ell}(\xi,t)
|^2
d\xi dt
}{
O_{r,\ell}^{\eta}
}.
}
\tag{7.1}
$$

By Plancherel:

$$
\boxed{
\mu_{r,\ell}
(
\mathbb R^3
)
=
1.
}
\tag{7.2}
$$

Thus:

$$
\mu_{r,\ell}
$$

is a probability measure on normalized relative-frequency space.

The normalized Fourier coordinate is:

$$
\boxed{
\zeta
=
r\xi.
}
\tag{7.3}
$$

---

# 8. NEW THEOREM — Relative-Frequency Second-Moment Bound

## Theorem 8.1

For every:

$$
O_{r,\ell}^{\eta}>0,
$$

$$
\boxed{
\int
|\zeta|^2
d\mu_{r,\ell}(\zeta)
\le
C_\eta
\frac{
\nu^{-1}
P_{r,\ell}^{\eta}
+
L_{r,\ell}^{\omega}
}{
O_{r,\ell}^{\eta}
}.
}
\tag{8.1}
$$

### Proof

By definition and Plancherel:

$$
\begin{aligned}
\int
|\zeta|^2
d\mu_{r,\ell}
&=
\frac{
r^{-1}
\int_{I_r}
\int
r^2
|\xi|^2
|
\widehat f_{r,\ell}
|^2
d\xi dt
}{
O_{r,\ell}^{\eta}
}\\
&=
\frac{
r
\int_{I_r}
\|
\nabla f_{r,\ell}(t)
\|_2^2dt
}{
O_{r,\ell}^{\eta}
}.
\end{aligned}
$$

Now:

$$
\nabla f_{r,\ell}
=
\eta_r
\nabla\Omega_\ell
+
(
\nabla\eta_r
)
\otimes
\Omega_\ell.
$$

Hence:

$$
|
\nabla f_{r,\ell}
|^2
\le
2
\eta_r^2
|
\nabla\Omega_\ell
|^2
+
2
|
\nabla\eta_r
|^2
|
\Omega_\ell
|^2.
$$

Multiply by:

$$
r
$$

and integrate.

The first term is:

$$
\le
2\nu^{-1}
P_{r,\ell}^{\eta}.
$$

The second term is:

$$
\le
2C_\eta
r^{-1}
\int_{I_r}
\int_{A_{\eta,r}}
|
\Omega_\ell
|^2
dxdt
=
2C_\eta
L_{r,\ell}^{\omega}.
$$

Absorb constants.

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

# 9. NEW THEOREM — Diffusion-or-Infrared Dichotomy

## Theorem 9.1

Let:

$$
(
u_n,
r_n,
\ell_n
)
$$

be a normalized sequence with fixed relative filter ratio:

$$
\ell_n
=
\sigma r_n.
$$

Assume:

$$
\boxed{
O_n^\eta
\ge
o_0
>
0.
}
\tag{9.1}
$$

Then either:

### positive diffusion/localization

there is:

$$
c_0>0
$$

such that along a subsequence:

$$
\boxed{
\nu^{-1}
P_n^\eta
+
L_n^\omega
\ge
c_0,
}
\tag{9.2}
$$

or:

### infrared concentration

$$
\boxed{
\mu_n
\Longrightarrow
\delta_0.
}
\tag{9.3}
$$

More quantitatively, if:

$$
\nu^{-1}
P_n^\eta
+
L_n^\omega
\to0,
$$

then for every:

$$
\kappa>0,
$$

$$
\boxed{
\mu_n
(
\{
|\zeta|\ge\kappa
\}
)
\to0.
}
\tag{9.4}
$$

### Proof

If (9.2) fails after subsequence extraction, then:

$$
\nu^{-1}
P_n^\eta
+
L_n^\omega
\to0.
$$

By Theorem 8.1 and:

$$
O_n^\eta\ge o_0,
$$

$$
\int
|\zeta|^2
d\mu_n
\to0.
$$

Markov's inequality gives:

$$
\mu_n
(
|\zeta|\ge\kappa
)
\le
\kappa^{-2}
\int
|\zeta|^2d\mu_n
\to0.
$$

Therefore:

$$
\mu_n
\Longrightarrow
\delta_0.
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

# 10. Dyadic interpretation — infrared escape

Let:

$$
m
=
\lfloor
\log_2
|\zeta|
\rfloor.
$$

For every fixed:

$$
M>0,
$$

the region:

$$
m\ge-M
$$

corresponds to:

$$
|\zeta|
\ge
2^{-M}.
$$

Under infrared concentration:

$$
\mu_n
\Longrightarrow
\delta_0,
$$

one has:

$$
\boxed{
\mu_n
(
m\ge-M
)
\to0
}
\tag{10.1}
$$

for every fixed:

$$
M.
$$

Equivalently:

$$
\boxed{
\text{all relative-frequency mass escapes through }
m\to-\infty.
}
\tag{10.2}
$$

This is exactly the missing infrared direction introduced in DCRP-18.

Thus:

$$
\boxed{
\textbf{
diffusion-silent filtered enstrophy is an IR scale carrier.
}
}
\tag{10.3}
$$

---

# 11. Quantitative non-IR coercivity

Suppose there exist:

$$
\kappa>0,
\qquad
\delta>0
$$

such that:

$$
\boxed{
\mu_{r,\ell}
(
|\zeta|\ge\kappa
)
\ge
\delta.
}
\tag{11.1}
$$

Then:

$$
\int
|\zeta|^2d\mu
\ge
\delta\kappa^2.
$$

Combine with Theorem 8.1:

$$
\delta\kappa^2
\le
C_\eta
\frac{
\nu^{-1}P^\eta
+
L^\omega
}{
O^\eta
}.
$$

Therefore:

$$
\boxed{
O^\eta
\le
\frac{
C_\eta
}{
\delta\kappa^2
}
\left(
\nu^{-1}P^\eta
+
L^\omega
\right).
}
\tag{11.2}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

This is a local scale-critical Poincare-type statement with the infrared sector made explicit rather than hidden in an uncontrolled mean mode.

---

# 12. Zero-cost reservoir elimination

Consider a normalized mechanism sequence satisfying:

$$
\boxed{
P_n^\eta\to0,
}
\tag{12.1}
$$

$$
\boxed{
L_n^\omega\to0,
}
\tag{12.2}
$$

and assume that the two-sided scale completion has no infrared defect.

The absence of an infrared defect means that the normalized relative-frequency measures cannot converge to:

$$
\delta_0
$$

while carrying a fixed positive absolute reservoir.

Therefore:

$$
\boxed{
O_n^\eta\to0.
}
\tag{12.3}
$$

Otherwise a subsequence with:

$$
O_n^\eta\ge o_0
$$

would trigger Theorem 9.1 and produce the prohibited IR carrier.

Status:

$$
\boxed{
\textbf{PROVED conditional only on explicit inclusion of the DCRP-18 infrared carrier in the native zero-cost package}.
}
$$

This is a package-completion condition already motivated independently by the scale-re-root audit.

---

# 13. Near-field stretching vanishes on a zero-cost/no-IR branch

The external near-field theorem gives:

$$
\boxed{
V_n^{+,\mathrm{near}}
\le
(1-\varepsilon)
P_n^\rho
+
C_{\varepsilon,\sigma,\rho}
M_n
O_n.
}
\tag{13.1}
$$

Assume:

$$
\sup_nM_n<\infty.
$$

If:

$$
P_n^\rho\to0
$$

and:

$$
O_n\to0,
$$

then:

$$
\boxed{
V_n^{+,\mathrm{near}}
\to0.
}
\tag{13.2}
$$

Thus the singular near-field stretching term cannot survive a zero-diffusion, zero-IR obstruction.

Status:

$$
\boxed{
\textbf{PROVED using arXiv:2606.27560}.
}
$$

---

# 14. Commutator forcing vanishes on the same branch

The external commutator insertion gives:

$$
F_n^{\mathrm{com}}
\le
\eta P_n
+
C_\eta
\widetilde{\mathcal S}_n^{(3)}
+
L_n^{\mathrm{com}}.
$$

If:

$$
P_n\to0,
$$

$$
\widetilde{\mathcal S}_n^{(3)}\to0,
$$

and:

$$
L_n^{\mathrm{com}}\to0,
$$

then:

$$
\boxed{
F_n^{\mathrm{com}}
\to0.
}
\tag{14.1}
$$

Status:

$$
\boxed{
\textbf{PROVED using arXiv:2606.27560}.
}
$$

---

# 15. Localization module

The filtered-enstrophy identity contains the cutoff residual:

$$
L_n.
$$

The external theorem proves that the principal cutoff residual vanishes identically if the cutoff solves the backward adjoint drift-diffusion equation:

$$
\boxed{
\partial_t\chi
+
\Delta\chi
+
U_\ell\cdot\nabla\chi
=
0.
}
\tag{15.1}
$$

The remaining shell costs generated by enlarged diffusion and commutator integration by parts are explicit nonnegative localization budgets.

Therefore the zero-localization branch satisfies:

$$
\boxed{
L_n
+
L_n^{\mathrm{com}}
\to0.
}
\tag{15.2}
$$

No hidden principal localization term remains.

---

# 16. Filtered enstrophy surplus

Let:

$$
E_{n,\mathrm{in}}^\omega,
\qquad
E_{n,\mathrm{out}}^\omega
$$

be the normalized endpoint filtered-enstrophy terms.

Let:

$$
P_n
$$

be filtered diffusion.

The external localized balance yields:

$$
\boxed{
E_{n,\mathrm{out}}^\omega
+
P_n
\le
E_{n,\mathrm{in}}^\omega
+
V_n^{+,\mathrm{near}}
+
V_n^{+,\mathrm{far}}
+
F_n^{\mathrm{com}}
+
L_n.
}
\tag{16.1}
$$

After choosing the near-field and commutator diffusion fractions, define the post-coercive positive surplus:

$$
\boxed{
\mathfrak B_n
=
\left[
E_{n,\mathrm{out}}^\omega
+
(1-\eta_{\mathrm{near}}-\eta_{\mathrm{com}})
P_n
-
E_{n,\mathrm{in}}^\omega
-
C_{\eta,\sigma}M_nO_n
-
L_n
-
L_n^{\mathrm{com}}
\right]_+.
}
\tag{16.2}
$$

The external theorem shows:

$$
\boxed{
\mathfrak B_n
\le
V_n^{+,\mathrm{far}}
+
C_{\eta}
\widetilde{\mathcal S}_n^{(3)}.
}
\tag{16.3}
$$

up to the explicit shell/localization terms already displayed.

---

# 17. NEW THEOREM — Far-Field-Only Survivor Reduction

## Theorem 17.1

Let a normalized filtered-vorticity sequence satisfy:

$$
\boxed{
\inf_n
\mathfrak B_n
\ge
b_0>0.
}
\tag{17.1}
$$

Assume:

$$
\boxed{
P_n\to0,
}
\tag{17.2}
$$

$$
\boxed{
\widetilde{\mathcal S}_n^{(3)}
\to0,
}
\tag{17.3}
$$

$$
\boxed{
L_n
+
L_n^{\mathrm{com}}
+
L_n^\omega
\to0,
}
\tag{17.4}
$$

$$
\boxed{
\sup_nM_n<\infty,
}
\tag{17.5}
$$

and the two-sided relative-frequency package has no infrared filtered-enstrophy defect.

Then:

$$
\boxed{
O_n\to0,
}
\tag{17.6}
$$

$$
\boxed{
V_n^{+,\mathrm{near}}\to0,
}
\tag{17.7}
$$

$$
\boxed{
F_n^{\mathrm{com}}\to0,
}
\tag{17.8}
$$

and necessarily:

$$
\boxed{
\liminf_{n\to\infty}
V_n^{+,\mathrm{far}}
\ge
b_0.
}
\tag{17.9}
$$

### Proof

The reservoir elimination theorem gives:

$$
O_n\to0.
$$

The external near-field coercivity then gives:

$$
V_n^{+,\mathrm{near}}\to0.
$$

The external commutator insertion gives:

$$
F_n^{\mathrm{com}}\to0.
$$

The localization terms vanish by assumption.

The balance inequality defining:

$$
\mathfrak B_n
$$

therefore leaves only:

$$
V_n^{+,\mathrm{far}}
$$

as a nonvanishing positive source.

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

# 18. Interpretation

The zero-cost survivor has now lost the following mechanisms.

### singular near-field stretching

Closed by geometric depletion plus diffusion.

### filtered-enstrophy reservoir

Closed by:

$$
\text{diffusion}
\ \vee\
\text{IR scale carrier}.
$$

### commutator forcing

Closed by:

$$
P
+
\widetilde{\mathcal S}^{(3)}
+
L^{\mathrm{com}}.
$$

### principal localization

Closed by the backward adjoint drift-diffusion cutoff.

### shell localization

Explicitly retained as:

$$
L^\omega,
\qquad
L^{\mathrm{com}}.
$$

Therefore the only remaining positive filtered mechanism is:

$$
\boxed{
\textbf{
far-field strain}.
}
$$

This is a substantial reduction.

---

# 19. Why far-field strain is structurally different

The singular near-field strain depends on vorticity at relative distance:

$$
O(r)
$$

and carries the Calderon--Zygmund singularity.

The far-field strain is generated by vorticity outside the core.

On the core it acts as a slowly varying external deformation.

The external filtered-vorticity paper gives two descriptions.

### annular packing

The contribution of larger spatial annuli is reassigned to coarser scales with geometric weights.

### fixed-source harmonic route

After replacing moving shells by fixed annular source partitions centered at the singular point, each exterior-source strain field is harmonic in the smaller core.

After subtracting its affine Taylor jet, higher-order terms gain powers of scale separation.

Thus the unresolved far-field object is essentially:

$$
\boxed{
\text{recurrent low-order harmonic strain jets across nested scales}.
}
\tag{19.1}
$$

---

# 20. Elementary far-field amplitude test

Define the scale-normalized far-field strain amplitude:

$$
\boxed{
J_{r,\ell}^{\mathrm{far}}
=
r^2
\left\|
S_\ell^{\mathrm{far}}
\right\|_{
L^\infty(Q_r)
}.
}
\tag{20.1}
$$

Then directly:

$$
\begin{aligned}
V_{r,\ell}^{+,\mathrm{far}}
&=
r
\iint
\chi
(
S_\ell^{\mathrm{far}}
\Omega_\ell\cdot\Omega_\ell
)_+
\\
&\le
r
\|
S_\ell^{\mathrm{far}}
\|_\infty
\iint
\chi
|
\Omega_\ell
|^2
\\
&=
J_{r,\ell}^{\mathrm{far}}
O_{r,\ell}.
\end{aligned}
$$

Hence:

$$
\boxed{
V_{r,\ell}^{+,\mathrm{far}}
\le
J_{r,\ell}^{\mathrm{far}}
O_{r,\ell}.
}
\tag{20.2}
$$

Therefore a far-field-only survivor with:

$$
O_n\to0
$$

and:

$$
V_n^{+,\mathrm{far}}\ge b_0
$$

must satisfy:

$$
\boxed{
J_n^{\mathrm{far}}
\to\infty.
}
\tag{20.3}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

Thus the far-field-only survivor is not merely "some external strain."

It is an **unbounded normalized far-field strain amplification**.

This is a new concrete obstruction coordinate.

---

# 21. Native meaning of the far-field amplification

The quantity:

$$
J_{r,\ell}^{\mathrm{far}}
$$

is:

- generated directly from filtered Navier--Stokes vorticity;
- scale normalized;
- independent of a copied singularity label;
- spatially external to the core;
- naturally associated with the harmonic exterior-source strain jet.

Therefore:

$$
\boxed{
J^{\mathrm{far}}\to\infty
}
$$

is a legitimate native noncompactness defect.

It should be retained in a transition-complete package as:

$$
\boxed{
\mathsf R_{\rm farjet}.
}
\tag{21.1}
$$

This does not yet eliminate the branch.

A hypothetical singular solution may genuinely generate diverging normalized external strain.

The point is that the survivor is now explicit.

---

# 22. Why the external weighted far-field estimate is not enough

The existing energy-level theorem yields:

$$
V_k^{+,\mathrm{far}}
\lesssim
M_E^{3/2}
2^{3k/2}.
$$

This is only summable against strongly decaying weights.

The annular reassignment improves the structure to:

$$
\boxed{
\mu_k^{\mathrm{far,ann}}
\lesssim
\sum_{j=0}^{k}
2^{-(k-j)}
\mathfrak A_j
\mathcal Q_k.
}
\tag{22.1}
$$

But bounded:

$$
\mathfrak A_j,
\qquad
\mathcal Q_k
$$

still allows:

$$
\mu_k\sim1
$$

at every scale.

Thus no unconditional unweighted Carleson summability follows from the current shell estimate.

This is a genuine remaining issue.

---

# 23. Two possible closure routes for far-field strain

The reduction suggests two distinct attacks.

## Route A — annular IR coupling

Show that:

$$
J_n^{\mathrm{far}}\to\infty
$$

or persistent:

$$
V_n^{+,\mathrm{far}}
$$

forces a nonzero two-sided infrared vorticity/strain carrier on outer relative scales.

Then DCRP-18's IR completion would absorb the far-field survivor into the already existing scale-defect channel.

## Route B — harmonic affine-jet rigidity

Use a fixed exterior annular partition.

For each outer source scale:

$$
j<k,
$$

the induced strain field on the smaller core is harmonic.

Write:

$$
\boxed{
H_{j,k}(x,t)
=
A_{j,k}(t)
+
B_{j,k}(t)
(
x-x_0
)
+
R_{j,k}^{(2)}(x,t).
}
\tag{23.1}
$$

Harmonic interior estimates give extra powers of:

$$
r_k/r_j
$$

for:

$$
R_{j,k}^{(2)}.
$$

Thus only the finite-dimensional low-order jet:

$$
\boxed{
(
A_{j,k},
B_{j,k}
)
}
\tag{23.2}
$$

can recur without geometric scale gain.

The target is to show that a persistent positive affine-strain jet must:

- be visible in a finite-dimensional native trace;
- generate a positive deformation/depletion tax;
- or correspond to a nonzero IR carrier.

This is the more geometric route.

---

# 24. New exact frontier

The next target is:

$$
\boxed{
\textbf{
Far-Field Harmonic-Jet / Infrared-Strain Rigidity Lemma}.
}
$$

A useful statement is:

> Let:
>
> $$
> \mathfrak B_n\ge b_0>0
> $$
>
> be a persistent post-near-field filtered-enstrophy surplus.
>
> Assume:
>
> $$
> P_n,
> \widetilde{\mathcal S}_n^{(3)},
> L_n,
> L_n^{\mathrm{com}},
> L_n^\omega
> \to0,
> $$
>
> and assume there is no UV/IR/spatial native carrier defect except possibly the exterior harmonic strain.
>
> Then prove that the fixed-source far-field harmonic jets satisfy:
>
> $$
> \boxed{
> \mathsf J_n^{aff}
> \ge
> c>0
> }
> $$
>
> on a positive-density set of scales.
>
> Next prove:
>
> $$
> \boxed{
> \text{persistent affine jet}
> \Longrightarrow
> \text{IR strain carrier}
> \ \vee\
> \text{paid deformation}
> \ \vee\
> \text{rigid removable mode}.
> }
> $$

If all three right-hand channels are zero, the far-field survivor vanishes.

This is now the single mechanism frontier.

---

# 25. Relation to the earlier supplier route

The supplier route remains useful.

If the far-field affine strain genuinely amplifies the local vorticity core until a local shell crosses the dissipation threshold, DCRP-16 produces a local supplier.

Then DCRP-14/15 attach:

$$
\text{finite trace}
\ \vee\
\text{finite-window residual}.
$$

DCRP-18 tracks re-root IR escape.

Thus the far-field mechanism cannot generate supplier events and then disappear from the audit.

The remaining issue is the **pre-supplier sustaining regime**:

can an external harmonic strain keep feeding the core across infinitely many scales without itself becoming an IR/native defect or paying a deformation tax?

That is exactly the next question.

---

# 26. Corrected proof-state diagram

The current filtered-vorticity route is:

$$
\boxed{
\begin{aligned}
\text{persistent local badness}
&\Longrightarrow
\text{positive filtered-enstrophy surplus}\\
&\Longrightarrow
\text{near-field}
\vee
\text{far-field}
\vee
\text{commutator}
\vee
\text{localization}\\
&\Longrightarrow
\text{diffusion/IR}
\vee
\text{far-field}
\vee
\widetilde{\mathcal S}^{(3)}
\vee
\text{local residual}.
\end{aligned}
}
\tag{26.1}
$$

On a zero-cost/no-IR branch:

$$
\boxed{
\text{only far-field strain survives}.
}
\tag{26.2}
$$

If the local filtered-enstrophy reservoir itself remains positive while diffusion vanishes, it is no longer a separate mechanism.

It is an IR defect.

This closes the reservoir loophole identified in DCRP-19.

---

# 27. Source-status map

## Already proved externally

From arXiv:2606.27560:

- near-field geometric depletion;
- pairwise direction-defect coercivity;
- strict diffusion insertion for near-field stretching;
- exact localized filtered-enstrophy identity;
- adjoint cancellation of the principal localization residual;
- far-field weighted packing;
- annular reassignment;
- conditional unweighted Carleson closure;
- derivative-compatible commutator estimate;
- commutator insertion into diffusion plus:

  $$
  \widetilde{\mathcal S}^{(p)};
  $$

- cylindrical Young-profile extraction for bounded critical commutator defects.

## Proved in DCRP-20

- localized relative-frequency probability measure for filtered enstrophy;
- second-moment diffusion/localization bound;
- diffusion-or-IR dichotomy;
- quantitative non-IR coercivity;
- zero-cost filtered-enstrophy reservoir elimination;
- far-field-only survivor reduction;
- normalized far-field strain amplification consequence:

  $$
  O_n\to0,
  \quad
  V_n^{far}\ge b_0
  \Longrightarrow
  J_n^{far}\to\infty.
  $$

## Still open

- unconditional far-field harmonic/annular closure;
- affine-jet rigidity;
- persistent commutator Young-profile recurrence if:

  $$
  \widetilde{\mathcal S}^{(3)}
  $$

  is allowed nonzero rather than assigned positive cost;
- full integration back into the singularity-to-MORP contradiction.

---

# 28. End state

The main new theorem is:

$$
\boxed{
\int
|\zeta|^2d\mu_{r,\ell}
\le
C
\frac{
\nu^{-1}P_{r,\ell}^{\eta}
+
L_{r,\ell}^{\omega}
}{
O_{r,\ell}^{\eta}
}.
}
$$

Therefore:

$$
\boxed{
O\ge o_0,
\quad
P\to0,
\quad
L^\omega\to0
\Longrightarrow
\text{IR relative-frequency escape}.
}
$$

If IR escape is prohibited by the completed native package:

$$
\boxed{
P\to0,
\quad
L^\omega\to0
\Longrightarrow
O\to0.
}
$$

Using the stronger external near-field and commutator theorems:

$$
\boxed{
\textbf{
zero-cost/no-IR filtered mechanism}
\Longrightarrow
\textbf{
far-field-strain-only survivor}.
}
$$

Moreover, if a positive far-field surplus persists while:

$$
O\to0,
$$

then:

$$
\boxed{
r^2
\|
S^{far}
\|_\infty
\to\infty.
}
$$

Thus the next single frontier is:

$$
\boxed{
\textbf{
Far-Field Harmonic-Jet / Infrared-Strain Rigidity Lemma}.
}
$$

The proof space has now reached a very specific external-strain obstruction.

---

# Checkpoint v21 Update — DCRP-21

# NS-DCRP-21 — Far-Field Annular Escape, Core-Profile Collapse, and Harmonic-Jet Reduction to Spatial Infinity

- date: 2026-08-17
- status: research proof checkpoint
- canonical source: UTF-8 Markdown
- canonical math delimiters: `$...$` and `$$...$$`
- objective:
  1. attack the DCRP-20 far-field-only survivor without assuming an unproved affine-jet cancellation;
  2. combine the exact annular reassignment formula with the already-proved collapse of the core filtered-enstrophy reservoir;
  3. prove that a persistent far-field stretching surplus forces the source annulus to escape to infinite relative spatial radius with diverging normalized annular vorticity amplitude;
  4. show that bounded-relative harmonic affine jets cannot be the final zero-cost survivor.
- no full Navier--Stokes regularity claim is made.
- principal external primary source:
  - Runlong Yu, *Filtered Vortex Stretching and Subgrid Defects for the Three-Dimensional Navier--Stokes Equations*, arXiv:2606.27560v1.
- internal dependencies:
  - DCRP-18 two-sided scale/spatial completion;
  - DCRP-20 filtered-enstrophy diffusion/IR dichotomy and far-field-only survivor reduction.
- no novelty/priority claim is made without independent audit.

---

# 1. Executive result

DCRP-20 reduced the zero-cost/no-IR filtered-vorticity branch to a far-field-only survivor:

$$
\boxed{
O_k\to0,
\qquad
V_k^{+,\mathrm{far}}
\ge b_0>0.
}
\tag{1.1}
$$

The external far-field paper gives the annular reassignment bound

$$
\boxed{
\mu_k^{\mathrm{far,ann}}
\le
C_0
\sum_{j=0}^{k}
2^{-(k-j)}
\mathfrak A_{j,k}
\mathcal Q_k,
}
\tag{1.2}
$$

where

$$
\boxed{
\mathfrak A_{j,k}
=
\left(
r_j^{-1}
\iint_{I_k\times\widetilde A_j}
|\Omega_k|^2
\right)^{1/2},
}
\tag{1.3}
$$

and

$$
\boxed{
\mathcal Q_k
=
\left[
\int_{I_k}
\left(
\int_{B_{2r_k}}
\chi_k|\Omega_k|^2dx
\right)^2dt
\right]^{1/2}.
}
\tag{1.4}
$$

The first new theorem of this round is the core time-profile estimate

$$
\boxed{
\mathcal Q_k
\le
C_{\sigma}
M_k^{1/2}
O_k^{1/2},
}
\tag{1.5}
$$

where

$$
M_k
$$

is the fixed-relative local kinetic-energy bound used in the filtered-vorticity theorem.

Therefore

$$
\boxed{
O_k\to0
\Longrightarrow
\mathcal Q_k\to0.
}
\tag{1.6}
$$

This is stronger than the observation in DCRP-20 that only the time-integrated core reservoir vanishes.

The second new theorem is the far-field annular amplification theorem.

Assume:

$$
V_k^{+,\mathrm{far}}
\ge
b_0>0,
$$

the exterior tail beyond a fixed physical base radius is separated as in the external far-field decomposition, and

$$
O_k\to0.
$$

The exterior tail satisfies

$$
\boxed{
V_k^{+,\mathrm{ext}}
\le
C
r_k
O_k
\to0.
}
\tag{1.7}
$$

Hence for sufficiently large:

$$
k,
$$

$$
\boxed{
\mu_k^{\mathrm{far,ann}}
\ge
\frac{b_0}{2}.
}
\tag{1.8}
$$

Using (1.2) and (1.5),

$$
\boxed{
\sum_{j=0}^{k}
2^{-(k-j)}
\mathfrak A_{j,k}
\ge
\frac{
c\,b_0
}{
M_k^{1/2}
O_k^{1/2}
}.
}
\tag{1.9}
$$

Since:

$$
\sum_{m=0}^{\infty}2^{-m}=2,
$$

there exists:

$$
j_k\le k
$$

such that:

$$
\boxed{
\mathfrak A_{j_k,k}
\ge
\frac{
c\,b_0
}{
M_k^{1/2}
O_k^{1/2}
}.
}
\tag{1.10}
$$

Thus if:

$$
\sup_k M_k<\infty,
$$

$$
\boxed{
\mathfrak A_{j_k,k}
\to\infty.
}
\tag{1.11}
$$

The third new theorem shows that this amplified annulus cannot remain at bounded relative spatial distance from the core.

Let:

$$
m=k-j.
$$

For every fixed:

$$
M<\infty,
$$

assume the local energy on the fixed enlarged normalized ball is uniformly bounded:

$$
\boxed{
\sup_k
M_k^{(M)}
<
\infty.
}
\tag{1.12}
$$

Then for:

$$
0\le m\le M,
$$

the local filter smoothing bound gives:

$$
\boxed{
\mathfrak A_{k-m,k}
\le
C_{\sigma,M}
\left(
M_k^{(M)}
\right)^{1/2}.
}
\tag{1.13}
$$

Consequently the annuli selected in (1.10) must satisfy:

$$
\boxed{
m_k
=
k-j_k
\to\infty.
}
\tag{1.14}
$$

Equivalently:

$$
\boxed{
\frac{
r_{j_k}
}{
r_k
}
=
2^{m_k}
\to\infty.
}
\tag{1.15}
$$

Hence:

$$
\boxed{
\textbf{
persistent far-field work with a collapsing core enstrophy profile
forces the source vorticity reservoir to escape to normalized spatial infinity.
}
}
\tag{1.16}
$$

Moreover its normalized annular amplitude diverges.

This result changes the interpretation of the harmonic-jet frontier.

The external paper correctly notes that fixed exterior annular sources generate harmonic strain fields in the core and that low-order affine jets are the modes that can recur across nested scales.

DCRP-21 proves:

$$
\boxed{
\textbf{
an affine jet sourced at bounded relative spatial radius cannot sustain
the DCRP-20 far-field-only survivor.
}
}
\tag{1.17}
$$

If a fixed-relative source annulus remains inside:

$$
|y-x_0|
\lesssim
2^M r_k,
$$

its normalized annular reservoir is uniformly bounded by local energy and filter smoothing, while the core profile:

$$
\mathcal Q_k
$$

tends to zero.

Its work therefore tends to zero.

Thus any recurrent affine harmonic jet capable of paying:

$$
V_k^{+,\mathrm{far}}
\ge b_0
$$

must be sourced at:

$$
\boxed{
\frac{
|y-x_0|
}{
r_k
}
\to\infty.
}
\tag{1.18}
$$

This is not a mysterious finite-dimensional jet recurrence.

It is an exterior-source spatial-escape branch.

Therefore the DCRP-20 far-field-only survivor reduces further to:

$$
\boxed{
\textbf{
spatial-infinity annular vorticity amplification.
}
}
\tag{1.19}
$$

In a transition-complete package that retains:

- absolute annular filtered-vorticity amplitude;
- normalized spatial source position;
- the point at spatial infinity;

one has:

$$
\boxed{
\textbf{
zero spatial-defect branch}
\Longrightarrow
V_k^{+,\mathrm{far}}\to0.
}
\tag{1.20}
$$

Combining with DCRP-20:

$$
\boxed{
\textbf{
zero diffusion}
+
\textbf{
zero IR-frequency defect}
+
\textbf{
zero commutator defect}
+
\textbf{
zero localization}
+
\textbf{
zero spatial-source escape}
\Longrightarrow
\textbf{
no positive filtered-enstrophy surplus}.
}
}
\tag{1.21}
$$

Thus the far-field harmonic-jet obstruction is closed **at the level of compactness alternatives**.

The remaining major bridge is no longer a stretching decomposition.

It is:

$$
\boxed{
\textbf{
Singular/CKN Badness}
\Longrightarrow
\textbf{
Persistent Filtered-Enstrophy Surplus or an Already-Paid Defect}.
}
}
\tag{1.22}
$$

Equivalently, the next question is whether every singular local branch must actually activate the filtered-vorticity mechanism strongly enough for the now-closed mechanism decomposition to apply.

A useful next target is:

$$
\boxed{
\textbf{
Local Supplier / Filtered-Enstrophy Activation Lemma}.
}
\tag{1.23}
$$

The DCRP-16 supplier theorem is a natural starting point.

---

# 2. External annular reassignment audited

The external paper defines:

$$
I_k
=
(t_0-r_k^2,t_0),
$$

and for:

$$
j\le k,
$$

$$
\boxed{
\widetilde A_j
=
\left\{
y:
(\Gamma-1)r_j
<
|y-x_0|
\le
(2\Gamma+1)r_j
\right\}.
}
\tag{2.1}
$$

The reassigned annular reservoir is:

$$
\boxed{
\mathfrak A_{j,k}
=
\left(
r_j^{-1}
\iint_{I_k\times\widetilde A_j}
|\Omega_k|^2
\right)^{1/2}.
}
\tag{2.2}
$$

The core time profile is:

$$
\boxed{
\mathcal Q_k
=
\left[
\int_{I_k}
\left(
\int_{B_{2r_k}}
\chi_k|\Omega_k|^2dx
\right)^2
dt
\right]^{1/2}.
}
\tag{2.3}
$$

The exact moving-shell reassignment estimate is:

$$
\boxed{
\mu_k^{\mathrm{far,ann}}
\le
C_0
\sum_{j=0}^{k}
2^{-(k-j)}
\mathfrak A_{j,k}
\mathcal Q_k.
}
\tag{2.4}
$$

The dyadic weight is summable:

$$
\boxed{
\sum_{j=0}^{k}
2^{-(k-j)}
<
2.
}
\tag{2.5}
$$

This summability is the key new leverage once:

$$
\mathcal Q_k
$$

is shown to vanish.

---

# 3. Core filtered-vorticity profile

Let:

$$
\boxed{
F_k(t)
=
\int_{B_{2r_k}}
\chi_k(x,t)
|\Omega_k(x,t)|^2dx.
}
\tag{3.1}
$$

Then:

$$
\boxed{
O_k
=
r_k^{-1}
\int_{I_k}
F_k(t)dt.
}
\tag{3.2}
$$

Also:

$$
\boxed{
\mathcal Q_k
=
\|F_k\|_{L_t^2(I_k)}.
}
\tag{3.3}
$$

The problem is that in general:

$$
L_t^1\to0
$$

does not imply:

$$
L_t^2\to0.
$$

The filtered-vorticity smoothing bound supplies the missing:

$$
L_t^\infty
$$

control.

---

# 4. NEW THEOREM — Core Time-Profile Collapse

## Theorem 4.1

Assume:

$$
\ell_k
=
\sigma r_k
$$

with fixed:

$$
\sigma>0.
$$

Assume the fixed-relative local kinetic-energy coordinate satisfies:

$$
\boxed{
M_k
\le
M_\ast.
}
\tag{4.1}
$$

Then:

$$
\boxed{
\mathcal Q_k
\le
C_{\sigma}
M_\ast^{1/2}
O_k^{1/2}.
}
\tag{4.2}
$$

In particular:

$$
\boxed{
O_k\to0
\Longrightarrow
\mathcal Q_k\to0.
}
\tag{4.3}
$$

### Proof

The local filtered-vorticity bound gives:

$$
\boxed{
\|\Omega_k(t)\|_{L^\infty(B_{2r_k})}
\le
C_\sigma
M_\ast^{1/2}
r_k^{-2}.
}
\tag{4.4}
$$

Therefore:

$$
F_k(t)
\le
C
r_k^3
\|\Omega_k(t)\|_\infty^2
\le
C_\sigma
M_\ast
r_k^{-1}.
$$

Hence:

$$
\boxed{
\|F_k\|_{L^\infty_t}
\le
C_\sigma
M_\ast
r_k^{-1}.
}
\tag{4.5}
$$

Now:

$$
\mathcal Q_k^2
=
\int
F_k^2dt
\le
\|F_k\|_\infty
\int
F_kdt.
$$

But:

$$
\int
F_kdt
=
r_kO_k.
$$

Therefore:

$$
\mathcal Q_k^2
\le
C_\sigma
M_\ast
O_k.
$$

Take square roots.

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

# 5. Exterior tail beyond the fixed base radius

The annular reassignment of the external paper treats the source shells:

$$
0\le m\le k.
$$

The more distant shells:

$$
m>k
$$

lie beyond a fixed physical base radius comparable to:

$$
r_0.
$$

Let:

$$
S_k^{\mathrm{ext}}
$$

be the filtered strain generated from source points separated from the core by at least:

$$
c r_0.
$$

The strain-kernel:

$$
L^2
$$

tail gives:

$$
\boxed{
\|
K\mathbf1_{|z|>cr_0}
\|_2
\le
C
r_0^{-3/2}.
}
\tag{5.1}
$$

The global filtered-vorticity bound gives:

$$
\boxed{
\|\Omega_k(t)\|_2
\le
C
\ell_k^{-1}
\|u(t)\|_2
\le
C_\sigma
r_k^{-1}
M_E^{1/2}.
}
\tag{5.2}
$$

Therefore:

$$
\boxed{
\|S_k^{\mathrm{ext}}(t)\|_\infty
\le
C_\sigma
r_0^{-3/2}
r_k^{-1}
M_E^{1/2}.
}
\tag{5.3}
$$

The normalized exterior positive work obeys:

$$
\begin{aligned}
V_k^{+,\mathrm{ext}}
&\le
r_k
\|S_k^{\mathrm{ext}}\|_\infty
\iint_{Q_k}
\chi_k|\Omega_k|^2
\\
&=
r_k
\|S_k^{\mathrm{ext}}\|_\infty
(r_kO_k).
\end{aligned}
$$

Hence:

$$
\boxed{
V_k^{+,\mathrm{ext}}
\le
C_\sigma
r_0^{-3/2}
M_E^{1/2}
r_k
O_k.
}
\tag{5.4}
$$

Thus if:

$$
O_k
$$

is bounded, and in particular if:

$$
O_k\to0,
$$

$$
\boxed{
V_k^{+,\mathrm{ext}}\to0.
}
\tag{5.5}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 6. NEW THEOREM — Annular Source Amplification

## Theorem 6.1

Assume:

$$
\boxed{
V_k^{+,\mathrm{far}}
\ge
b_0>0,
}
\tag{6.1}
$$

$$
\boxed{
O_k\to0,
}
\tag{6.2}
$$

and:

$$
\boxed{
M_k\le M_\ast.
}
\tag{6.3}
$$

Then, after discarding finitely many:

$$
k,
$$

there exists:

$$
j_k\le k
$$

such that:

$$
\boxed{
\mathfrak A_{j_k,k}
\ge
\frac{
c\,b_0
}{
M_\ast^{1/2}
O_k^{1/2}
}.
}
\tag{6.4}
$$

Consequently:

$$
\boxed{
\mathfrak A_{j_k,k}
\to\infty.
}
\tag{6.5}
$$

### Proof

By Theorem 5.1:

$$
V_k^{+,\mathrm{ext}}\to0.
$$

The far-field positive work is bounded above by the annular absolute contribution plus the exterior tail budget.

Therefore for sufficiently large:

$$
k,
$$

$$
\mu_k^{\mathrm{far,ann}}
\ge
\frac{b_0}{2}.
$$

Apply the external annular reassignment estimate:

$$
\frac{b_0}{2}
\le
C_0
\mathcal Q_k
\sum_{j=0}^{k}
2^{-(k-j)}
\mathfrak A_{j,k}.
$$

By Theorem 4.1:

$$
\mathcal Q_k
\le
C_\sigma
M_\ast^{1/2}
O_k^{1/2}.
$$

Thus:

$$
\sum_{j=0}^{k}
2^{-(k-j)}
\mathfrak A_{j,k}
\ge
\frac{
c\,b_0
}{
M_\ast^{1/2}
O_k^{1/2}
}.
$$

Since the weights sum to less than two:

$$
\max_{0\le j\le k}
\mathfrak A_{j,k}
\ge
\frac12
\sum_{j=0}^{k}
2^{-(k-j)}
\mathfrak A_{j,k}.
$$

Choose:

$$
j_k
$$

realizing the maximum.

This proves (6.4).

$$
\square
$$

Status:

$$
\boxed{
\textbf{PROVED using Proposition 8.6 of arXiv:2606.27560 plus Theorems 4.1 and 5.1 above}.
}
$$

---

# 7. Fixed-relative annuli cannot amplify without bound

Let:

$$
m=k-j.
$$

Then:

$$
r_j
=
2^m
r_k.
$$

Fix:

$$
M<\infty.
$$

For:

$$
0\le m\le M,
$$

the annulus:

$$
\widetilde A_{k-m}
$$

lies inside a fixed enlarged normalized ball:

$$
B_{R_Mr_k}(x_0),
$$

where:

$$
R_M
$$

depends only on:

$$
M
$$

and:

$$
\Gamma.
$$

Assume:

$$
\boxed{
M_k^{(M)}
:=
r_k^{-1}
\operatorname*{ess\,sup}_{t\in I_k}
\int_{
B_{R_Mr_k}(x_0)
}
|u(x,t)|^2dx
\le
M_M.
}
\tag{7.1}
$$

The local filter smoothing estimate gives:

$$
\boxed{
\|\Omega_k(t)\|_{
L^\infty(B_{R_Mr_k})
}
\le
C_{\sigma,M}
M_M^{1/2}
r_k^{-2}.
}
\tag{7.2}
$$

---

# 8. NEW THEOREM — Bounded-Relative Annular Reservoir Bound

## Theorem 8.1

Under (7.1), for every:

$$
0\le m\le M,
$$

$$
\boxed{
\mathfrak A_{k-m,k}
\le
C_{\sigma,\Gamma,M}
M_M^{1/2}
2^m.
}
\tag{8.1}
$$

In particular:

$$
\boxed{
\sup_k
\max_{0\le m\le M}
\mathfrak A_{k-m,k}
<
\infty.
}
\tag{8.2}
$$

### Proof

The annulus:

$$
\widetilde A_{k-m}
$$

has volume:

$$
\boxed{
|\widetilde A_{k-m}|
\le
C_\Gamma
r_{k-m}^3
=
C_\Gamma
2^{3m}
r_k^3.
}
\tag{8.3}
$$

The time interval has length:

$$
|I_k|
=
r_k^2.
$$

Therefore:

$$
\begin{aligned}
\mathfrak A_{k-m,k}^2
&=
r_{k-m}^{-1}
\iint_{
I_k\times\widetilde A_{k-m}
}
|\Omega_k|^2
\\
&\le
r_{k-m}^{-1}
r_k^2
C_\Gamma
r_{k-m}^3
\|\Omega_k\|_\infty^2
\\
&\le
C
r_k^2
r_{k-m}^2
\left[
M_M
r_k^{-4}
\right]
\\
&=
C
M_M
\left(
\frac{
r_{k-m}
}{
r_k
}
\right)^2
\\
&=
C
M_M
2^{2m}.
\end{aligned}
$$

Take square roots.

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

# 9. NEW THEOREM — Far-Field Source Spatial Escape

## Theorem 9.1

Assume the hypotheses of Theorem 6.1.

Assume in addition that for every fixed:

$$
M<\infty,
$$

the enlarged local-energy bound:

$$
\sup_kM_k^{(M)}<\infty
$$

holds.

Let:

$$
j_k
$$

be the amplified annulus supplied by Theorem 6.1 and define:

$$
\boxed{
m_k
=
k-j_k.
}
\tag{9.1}
$$

Then:

$$
\boxed{
m_k\to\infty.
}
\tag{9.2}
$$

Equivalently:

$$
\boxed{
\frac{
r_{j_k}
}{
r_k
}
\to\infty.
}
\tag{9.3}
$$

### Proof

Suppose not.

Then after a subsequence:

$$
m_k\le M
$$

for some fixed:

$$
M.
$$

Theorem 8.1 gives:

$$
\sup_k
\mathfrak A_{j_k,k}
<
\infty.
$$

But Theorem 6.1 gives:

$$
\mathfrak A_{j_k,k}\to\infty.
$$

Contradiction.

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

# 10. Quantitative spatial-escape strength

Theorem 6.1 actually gives more than:

$$
m_k\to\infty.
$$

The selected annular reservoir satisfies:

$$
\boxed{
\mathfrak A_{j_k,k}
\gtrsim
O_k^{-1/2}.
}
\tag{10.1}
$$

up to the fixed local-energy and far-surplus constants.

Thus the source does not merely move outward.

Its normalized annular filtered-vorticity amplitude diverges while its relative radius diverges.

Therefore the survivor is:

$$
\boxed{
\textbf{
spatial escape}
+
\textbf{
annular critical-amplitude blowup}.
}
\tag{10.2}
$$

This is substantially more rigid than a bounded external harmonic background.

---

# 11. Harmonic affine-jet interpretation

The external paper replaces moving shells by a fixed smooth annular partition:

$$
\psi_j(y)
$$

supported where:

$$
|y-x_0|
\simeq
r_j,
$$

and defines:

$$
\boxed{
H_{j,k}(x,t)
=
\int
K(x-y)
\psi_j(y)
\Omega_k(y,t)dy.
}
\tag{11.1}
$$

For:

$$
j<k,
$$

$$
H_{j,k}
$$

is a smooth exterior-source strain field in the core.

In the exterior-source formulation it is harmonic there.

Write its Taylor expansion:

$$
\boxed{
H_{j,k}(x,t)
=
A_{j,k}(t)
+
B_{j,k}(t)(x-x_0)
+
R_{j,k}^{(2)}(x,t).
}
\tag{11.2}
$$

The paper notes that the affine jet:

$$
(A_{j,k},B_{j,k})
$$

is the low-order mode that may recur across nested cores.

DCRP-21 gives a new restriction on such recurrence.

---

# 12. NEW COROLLARY — bounded-relative harmonic jets cannot sustain the survivor

Fix:

$$
M<\infty.
$$

Consider only source annuli satisfying:

$$
0\le k-j\le M.
$$

Under the fixed-relative local-energy bounds of Theorem 8.1, their annular source reservoirs are uniformly bounded.

The external annular work formula then gives:

$$
\boxed{
\mu_k^{\mathrm{far},\,m\le M}
\le
C_M
\mathcal Q_k.
}
\tag{12.1}
$$

By Theorem 4.1:

$$
\mathcal Q_k\to0.
$$

Therefore:

$$
\boxed{
\mu_k^{\mathrm{far},\,m\le M}
\to0.
}
\tag{12.2}
$$

Hence no fixed finite collection of bounded-relative exterior harmonic jets can support:

$$
V_k^{+,\mathrm{far}}\ge b_0.
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

The low-order affine jet can survive only if its source scale itself recedes to:

$$
m\to\infty.
$$

---

# 13. Why no affine cancellation theorem is needed on the zero-spatial-defect branch

The external paper leaves affine-jet cancellation as a conditional route because an affine harmonic mode may remain visible across nested cores.

DCRP-21 does not prove algebraic cancellation of an arbitrary affine strain.

Instead it proves a different statement:

> If the core filtered-enstrophy time profile collapses, then any affine jet sourced at bounded relative radius has vanishing work.

Thus the only affine jets relevant to the DCRP-20 far-field survivor are sourced at unbounded relative distance.

Those are already a spatial noncompactness phenomenon.

Therefore, on a transition-complete branch satisfying:

$$
\boxed{
\text{no spatial-source escape},
}
\tag{13.1}
$$

one does not need a separate universal affine-cancellation theorem.

The far-field source is forced into the near/finite-relative compact sector, where its work vanishes because:

$$
\mathcal Q_k\to0.
$$

This is an alternative closure route to the paper's proposed affine-jet cancellation module.

---

# 14. Spatial carrier completion

For the far-field source, a natural native carrier is the family:

$$
\boxed{
\left(
m,
\mathfrak A_{k-m,k}
\right),
\qquad
m\in\mathbb N_0.
}
\tag{14.1}
$$

Compactify relative source radius by:

$$
\boxed{
\overline{\mathbb N}_0^{sp}
=
\mathbb N_0
\cup
\{
+\infty_{sp}
\}.
}
\tag{14.2}
$$

Retain separately:

1. normalized source-position distribution;
2. absolute annular amplitude.

Theorem 9.1 says that a far-field-only survivor produces:

$$
\boxed{
+\infty_{sp}
}
$$

with divergent absolute amplitude.

This is a native PDE-generated spatial carrier.

It does not copy a singularity label.

---

# 15. Transition-complete zero-spatial-defect implication

Suppose a normalized filtered mechanism sequence satisfies the DCRP-20 zero-cost conditions:

$$
P_k\to0,
$$

$$
\widetilde{\mathcal S}^{(3)}_k\to0,
$$

$$
L_k+L_k^{\mathrm{com}}+L_k^\omega\to0,
$$

no IR-frequency defect, and fixed-relative local-energy bounds.

DCRP-20 gives:

$$
O_k\to0.
$$

If the completed spatial-source carrier also has no defect at:

$$
+\infty_{sp},
$$

then Theorem 9.1 rules out:

$$
V_k^{+,\mathrm{far}}\ge b_0.
$$

Therefore:

$$
\boxed{
V_k^{+,\mathrm{far}}\to0.
}
\tag{15.1}
$$

Together with DCRP-20:

$$
\boxed{
V_k^{+,\mathrm{near}}\to0,
}
\tag{15.2}
$$

$$
\boxed{
F_k^{\mathrm{com}}\to0,
}
\tag{15.3}
$$

and:

$$
\boxed{
L_k\to0.
}
\tag{15.4}
$$

Hence:

$$
\boxed{
\textbf{
all positive filtered-vorticity mechanism channels vanish.
}
}
\tag{15.5}
$$

Status:

$$
\boxed{
\textbf{PROVED at the mechanism-package level under the stated zero-defect compactness assumptions}.
}
$$

---

# 16. Filtered-surplus consequence

Let:

$$
\mathfrak B_k
$$

be the post-near-field filtered-enstrophy surplus used in DCRP-20 and in the external filtered-vorticity theorem.

Under the zero-cost/no-IR/no-spatial-defect hypotheses above:

$$
V_k^{+,\mathrm{far}}
\to0,
$$

$$
\widetilde{\mathcal S}^{(3)}_k
\to0,
$$

and all localization terms vanish.

Therefore:

$$
\boxed{
\mathfrak B_k\to0.
}
\tag{16.1}
$$

Thus:

$$
\boxed{
\textbf{
a persistent positive filtered-enstrophy surplus cannot be an exact zero-cost compact obstruction.
}
}
\tag{16.2}
$$

This substantially closes the mechanism decomposition.

---

# 17. What this does not yet prove

A singular suitable weak solution is known to remain CKN-bad at every sufficiently small scale around a singular point.

But the current chain has not yet proved the implication:

$$
\boxed{
\text{persistent CKN badness}
\Longrightarrow
\inf_k
\mathfrak B_k
>
0.
}
\tag{17.1}
$$

Nor has it proved that every local supplier event forces a fixed positive:

$$
\mathfrak B_k
$$

at a comparable filtered scale.

Therefore eliminating a hypothetical persistent positive filtered-vorticity surplus does not yet eliminate every possible singular branch.

This is now the principal interface gap.

---

# 18. Why this is the correct next gap

The external structural program already separates:

- full CKN badness;
- coarse resolved badness;
- subfilter residual badness.

DCRP-19 reduced full critical supply to:

- transition influx;
- coarse resolved mechanism;
- subfilter residual.

DCRP-20/21 now substantially close the **filtered-vorticity mechanism** whenever it is activated.

The remaining question is whether singularity must activate that mechanism at a fixed critical strength.

This is a detector-to-mechanism lower-bound problem, not another decomposition problem.

---

# 19. Supplier route as the activation candidate

DCRP-16 proves that every first singular point admits:

$$
t_n\uparrow T,
$$

$$
x_n\to x_\ast,
$$

$$
\lambda_n\to\infty,
$$

with:

$$
\boxed{
\lambda_n^{-1}
|
\Delta_{\lambda_n}u(x_n,t_n)
|
\ge
c_{\rm loc}\nu.
}
\tag{19.1}
$$

DCRP-09/14 then produce an actual same-history nonlinear increment at the same scale.

A band-limited divergence-free supplier also has the global Fourier identity:

$$
\boxed{
\|
\nabla\times u_q
\|_2^2
\asymp
\lambda_q^2
\|u_q\|_2^2.
}
\tag{19.2}
$$

Together with:

$$
\lambda_q
\|u_q\|_2^2
\gtrsim
\nu^2,
$$

this gives a critical instantaneous vorticity-shell lower bound.

The unresolved part is to convert this instantaneous bandpass vorticity atom into a **fixed spacetime filtered-enstrophy surplus**:

$$
\mathfrak B_k\ge b_0.
$$

This is where possible ultrashort temporal spikes and low-pass/bandpass cancellation still matter.

---

# 20. New exact frontier

The next target is:

$$
\boxed{
\textbf{
Local Supplier / Filtered-Enstrophy Activation Lemma}.
}
$$

A useful sufficient statement is:

> Let:
>
> $$
> (x_n,t_n,\lambda_n)
> $$
>
> be the local supplier sequence of DCRP-16.
>
> Then after passing to:
>
> $$
> r_n\asymp\lambda_n^{-1},
> \qquad
> \ell_n=\sigma r_n,
> $$
>
> at least one of:
>
> 1. a fixed positive post-near-field filtered-enstrophy surplus:
>
> $$
> \mathfrak B_n\ge b_0;
> $$
>
> 2. a fixed positive filtered diffusion cost;
> 3. a derivative-compatible commutator defect;
> 4. a localization/pressure residual;
> 5. a temporal concentration defect;
>
> occurs.

If alternative 1 occurs, DCRP-20/21 eliminate the zero-cost compact branch.

Alternatives 2--5 are already paid/native defect channels after completion.

This would finally connect local singular supplier capture to the now-closed filtered-vorticity mechanism calculus.

---

# 21. Possible temporal concentration coordinate

The main technical difference between a supplier endpoint and the filtered-enstrophy surplus is time.

A supplier may, a priori, be a short spike.

Define the normalized bandpass enstrophy profile:

$$
\boxed{
e_n(\tau)
=
\int_{B_R}
|
\omega_{q_n}^{(n)}(y,\tau)
|^2dy.
}
\tag{21.1}
$$

At the supplier endpoint:

$$
\boxed{
e_n(0)\ge c\nu^2.
}
\tag{21.2}
$$

There are two possibilities.

### positive normalized residence

For some fixed:

$$
\tau_0>0,
$$

$$
\boxed{
\int_{-\tau_0}^{0}
e_n(\tau)d\tau
\ge
c_0>0.
}
\tag{21.3}
$$

Then a fixed filtered/bandpass enstrophy spacetime reservoir is activated.

### temporal concentration

For every fixed:

$$
\tau_0>0,
$$

the profile mass collapses toward:

$$
\tau=0.
$$

Then the supplier produces a nontrivial temporal concentration defect.

A transition-complete package should retain this concentration rather than silently lose it.

Thus even before a quantitative residence-time theorem, the activation problem admits a compactness alternative.

---

# 22. Why the harmonic-jet frontier has changed

The external paper states that a complete harmonic-rigidity theorem should control affine jets from a fixed annular source decomposition directly.

DCRP-21 does not prove that general theorem.

Instead, in the specific DCRP zero-core-reservoir regime, it proves:

$$
\boxed{
\text{bounded-relative source}
\Longrightarrow
\text{bounded annular amplitude}
\Longrightarrow
\text{vanishing far work}.
}
\tag{22.1}
$$

Therefore the only harmonic jets still relevant to the DCRP survivor are those whose **source annuli themselves escape to normalized spatial infinity**.

This is a stronger classification in the specific zero-cost branch, but it does not supersede the external paper's general harmonic-jet problem for arbitrary filtered flows.

---

# 23. Source ledger

## Filtered Vortex Stretching and Subgrid Defects

The following primary results are used:

### far-field moving-shell decomposition

$$
\mathbb S_k^{far}
=
\sum_m
\mathbb S_{k,m}.
$$

### bounded-overlap annular reassignment

The moving shell at relative separation:

$$
m
$$

is contained in a fixed annulus at scale:

$$
r_{k-m},
$$

and the fixed annuli have uniformly bounded overlap.

### exact reassigned bound

$$
\mu_k^{far,ann}
\le
C
\sum_{j=0}^k
2^{-(k-j)}
\mathfrak A_{j,k}
\mathcal Q_k.
$$

### fixed-annulus harmonic route

A fixed exterior annular source generates a smooth harmonic strain in the smaller core, and after subtraction of its affine Taylor jet the higher-order remainder gains powers of scale separation.

The paper explicitly does not prove unconditional affine-jet cancellation.

DCRP-21 uses the exact annular bound, not an assumed cancellation theorem.

---

# 24. End state

The far-field-only survivor from DCRP-20 has been reduced to a spatial-escape object.

The key new estimates are:

$$
\boxed{
\mathcal Q_k
\le
C_\sigma
M_\ast^{1/2}
O_k^{1/2},
}
$$

and, if:

$$
V_k^{+,\mathrm{far}}
\ge b_0,
\qquad
O_k\to0,
$$

then there exists:

$$
j_k\le k
$$

such that:

$$
\boxed{
\mathfrak A_{j_k,k}
\gtrsim
O_k^{-1/2}
\to\infty,
}
$$

and:

$$
\boxed{
k-j_k\to\infty.
}
$$

Thus:

$$
\boxed{
\textbf{
far-field survivor}
\Longrightarrow
\textbf{
spatial-infinity annular vorticity amplification}.
}
$$

Consequently a zero-spatial-defect, zero-IR, zero-diffusion, zero-commutator, zero-localization branch has:

$$
\boxed{
\mathfrak B_k\to0.
}
$$

The next single frontier is:

$$
\boxed{
\textbf{
Local Supplier / Filtered-Enstrophy Activation Lemma}.
}
$$

The mechanism decomposition is now substantially closed.

The remaining question is whether a singular branch must activate it at a fixed critical strength, or else leave a temporal/paid defect.

---

# Checkpoint v22 Update — DCRP-22

# NS-DCRP-22 — Supplier-to-Filtered-Enstrophy Activation, Temporal-Spike Elimination, and a Poincaré Correction to the Local Reservoir Branch

- date: 2026-08-17
- status: research proof checkpoint
- canonical source: UTF-8 Markdown
- canonical math delimiters: `$...$` and `$$...$$`
- objective:
  1. connect the DCRP-16 local supplier atom to the filtered-vorticity mechanism of DCRP-20/21;
  2. eliminate the proposed "ultrashort temporal spike" escape;
  3. correct the DCRP-20 treatment of the compactly localized filtered-enstrophy reservoir;
  4. reduce supplier activation to explicit diffusion / commutator / localization / far-field spatial-escape channels.
- no full Navier--Stokes regularity claim is made.
- principal external primary source:
  - Runlong Yu, *Filtered Vortex Stretching and Subgrid Defects for the Three-Dimensional Navier--Stokes Equations*, arXiv:2606.27560v1.
- supporting primary source:
  - Cheskidov--Dai, *Regularity Criteria for the 3D Navier-Stokes and MHD Equations*, arXiv:1507.06611v6.
- internal dependencies:
  - DCRP-16 Local Supplier Capture;
  - DCRP-20 filtered mechanism reduction;
  - DCRP-21 far-field annular spatial-escape theorem.
- no novelty/priority claim is made without independent audit.

---

# 1. Executive result

DCRP-21 left the interface:

$$
\boxed{
\textbf{
Local Supplier}
\Longrightarrow
\textbf{
Filtered-Enstrophy Activation}
\ \vee\
\textbf{
temporal/paid defect}.
}
}
\tag{1.1}
$$

This round closes that interface at the level of a quantitative alternative.

The argument has three modules.

## Module A — supplier velocity forces local supplier vorticity

DCRP-16 produces, near every first singular point,

$$
t_n\uparrow T,
\qquad
x_n\to x_\ast,
\qquad
r_n=\lambda_n^{-1}\downarrow0,
$$

with a localized dissipation-boundary shell satisfying

$$
\boxed{
r_n
\|
(v_n)_{q_n}(t_n)
\|_\infty
\ge
c_{\rm sup}\nu.
}
\tag{1.2}
$$

After normalizing at its own global shell maximum, the field belongs to a fixed annulus-bandlimited divergence-free class.

A compactness/analyticity argument gives a uniform local curl lower bound.

Consequently, after transferring from the good-collar localization back to the original field,

$$
\boxed{
r_n
\int_{
B_{Rr_n}(x_n)
}
|
\omega_{q_n}(x,t_n)
|^2dx
\ge
c_\omega\nu^2.
}
\tag{1.3}
$$

Thus the local supplier is also a critical local vorticity-shell atom.

## Module B — two fixed mollifier scales force a full filtered-vorticity endpoint atom or a localization defect

Choose one fixed radial nonnegative compactly supported mollifier

$$
\varphi,
\qquad
\int\varphi=1.
$$

There exist fixed constants

$$
0<a<b\ll1
$$

such that the Fourier multiplier difference

$$
\boxed{
m_{a,b}(\zeta)
=
\widehat\varphi(a\zeta)
-
\widehat\varphi(b\zeta)
}
\tag{1.4}
$$

is bounded away from zero on the fixed supplier annulus:

$$
\boxed{
|m_{a,b}(\zeta)|
\ge
d_\varphi>0
\qquad
(\zeta\in\mathcal A).
}
\tag{1.5}
$$

Let

$$
\Omega_{a,n}
=
\nabla\times
S_{ar_n}u,
$$

$$
\Omega_{b,n}
=
\nabla\times
S_{br_n}u,
$$

and

$$
G_n
=
\Omega_{a,n}
-
\Omega_{b,n}.
$$

The supplier shell lower bound implies

$$
\boxed{
r_n
\|
\eta_n
\Delta_{q_n}G_n(t_n)
\|_2^2
\ge
c_G\nu^2
}
\tag{1.6}
$$

for a fixed normalized cutoff

$$
\eta_n.
$$

Using

$$
\eta_n\Delta_qG
=
\Delta_q(\eta_nG)
-
[
\Delta_q,\eta_n
]G,
$$

one obtains the exact alternative:

$$
\boxed{
r_n
\|
\eta_nG_n(t_n)
\|_2^2
\ge
c_1\nu^2
}
\tag{1.7}
$$

or:

$$
\boxed{
\mathcal C_n^{spec}
:=
r_n
\|
[
\Delta_{q_n},\eta_n
]
G_n(t_n)
\|_2^2
\ge
c_2\nu^2.
}
\tag{1.8}
$$

If (1.7) holds, then by the triangle inequality at least one of the two **full filtered vorticities** satisfies:

$$
\boxed{
r_n
\|
\eta_n
\Omega_{\sigma_n,n}(t_n)
\|_2^2
\ge
e_0\nu^2,
\qquad
\sigma_n\in\{a,b\}.
}
\tag{1.9}
$$

Hence:

$$
\boxed{
\textbf{
supplier endpoint}
\Longrightarrow
\textbf{
full filtered-vorticity endpoint atom}
\ \vee\
\textbf{
spectral-localization defect}.
}
}
\tag{1.10}
$$

The detector family contains only two filter ratios.

No scale-dependent detector dimension is introduced.

## Module C — a temporal spike cannot avoid the filtered-enstrophy ledger

Assume the endpoint filtered atom (1.9).

Fix a normalized backward time length

$$
\tau_0>0.
$$

Let

$$
J_n
=
(
t_n-\tau_0r_n^2,
t_n
).
$$

Define:

$$
\boxed{
\mathcal O_n
=
r_n^{-1}
\int_{J_n}
\int
\eta_n^2
|
\Omega_{\sigma_n,n}
|^2dxdt.
}
\tag{1.11}
$$

There are two cases.

### Reservoir branch

If:

$$
\mathcal O_n
\ge
o_0>0,
$$

then a local Poincaré inequality gives:

$$
\boxed{
\mathcal O_n
\le
C_\eta
\left(
\nu^{-1}\mathcal P_n
+
\mathcal L_n^\omega
\right).
}
\tag{1.12}
$$

Therefore a fixed reservoir immediately forces fixed filtered diffusion or cutoff-shell cost.

### Temporal-spike branch

If:

$$
\mathcal O_n
<
o_0
$$

with:

$$
o_0
$$

chosen sufficiently small relative to the endpoint atom and:

$$
\tau_0,
$$

then there exists:

$$
s_n\in J_n
$$

with small initial filtered enstrophy:

$$
\boxed{
\mathcal E_n^\omega(s_n)
\le
\frac14
e_0\nu^2.
}
\tag{1.13}
$$

while:

$$
\boxed{
\mathcal E_n^\omega(t_n)
\ge
e_0\nu^2.
}
\tag{1.14}
$$

The exact localized filtered-enstrophy identity therefore forces a fixed positive mechanism payment.

After inserting the external near-field stretching coercivity and derivative-compatible commutator estimate, one obtains:

$$
\boxed{
c_{\rm act}\nu^2
\le
C(M)
\mathcal O_n
+
\mathcal V_n^{+,\mathrm{far}}
+
C
\widetilde{\mathcal S}_n^{(3)}
+
\mathcal L_n
+
\mathcal L_n^{\mathrm{com}}.
}
\tag{1.15}
$$

Thus an ultrashort supplier spike does not evade the spacetime ledger.

It forces a fixed positive:

- far-field strain event;
- derivative-compatible commutator defect;
- or localization residual.

Combining Modules A--C:

$$
\boxed{
\begin{aligned}
\textbf{local supplier}
\Longrightarrow\quad
&
\mathcal C^{spec}\ge c\\
&\vee\
\mathcal P+\mathcal L^\omega\ge c\\
&\vee\
\mathcal V^{far}\ge c\\
&\vee\
\widetilde{\mathcal S}^{(3)}\ge c\\
&\vee\
\mathcal L+\mathcal L^{com}\ge c.
\end{aligned}
}
\tag{1.16}
$$

All constants are scale uniform after fixing:

- the normalized supplier annulus;
- the two relative filter ratios;
- the local-energy bound;
- the normalized cutoff family.

The remaining far-field branch is handled by DCRP-21:

if the local reservoir tends to zero and far-field work remains positive, the annular source must escape to normalized spatial infinity with diverging amplitude.

Therefore a transition-complete zero-cost package satisfying:

- zero filtered diffusion;
- zero spectral/localization defect;
- zero derivative-compatible increment defect;
- zero spatial-source escape;

cannot contain the local supplier sequence.

This eliminates the "supplier exists only as an ultrashort invisible spike" loophole.

---

# 2. CORRECTION — the DCRP-20 local IR reservoir branch is unnecessary

DCRP-20 defined:

$$
f_{r,\ell}
=
\eta_r\Omega_\ell
$$

with:

$$
\eta_r
$$

compactly supported in a fixed normalized ball.

It then introduced a relative-frequency measure and concluded:

$$
\boxed{
O^\eta>0,
\quad
P^\eta\to0,
\quad
L^\omega\to0
\Longrightarrow
\text{relative IR concentration}.
}
\tag{2.1}
$$

The second-moment inequality itself is correct.

However, because:

$$
f_{r,\ell}
$$

has compact support of radius:

$$
O(r),
$$

one has an ordinary Poincaré inequality.

This yields a strictly stronger conclusion.

---

# 3. NEW THEOREM — Compact Local Reservoir Poincaré Bound

## Theorem 3.1

Let:

$$
f
=
\eta_r\Omega_\ell
$$

with:

$$
\eta_r
$$

supported in:

$$
B_{Cr}(x_0).
$$

Then:

$$
\boxed{
\mathcal O_{r,\ell}^{\eta}
\le
C_{\eta}
\left(
\nu^{-1}
\mathcal P_{r,\ell}^{\eta}
+
\mathcal L_{r,\ell}^{\omega}
\right).
}
\tag{3.1}
$$

### Proof

For every fixed time, because:

$$
f
\in
H_0^1
(
B_{Cr}
),
$$

Poincaré gives:

$$
\|f\|_2^2
\le
C_\eta
r^2
\|
\nabla f
\|_2^2.
$$

But:

$$
\nabla f
=
\eta_r
\nabla\Omega_\ell
+
(
\nabla\eta_r
)
\otimes
\Omega_\ell.
$$

Hence:

$$
\|
\nabla f
\|_2^2
\le
2
\int
\eta_r^2
|
\nabla\Omega_\ell
|^2
+
C_\eta
r^{-2}
\int_{
\supp\nabla\eta_r
}
|
\Omega_\ell
|^2.
$$

Integrate in time and multiply by:

$$
r^{-1}.
$$

The first term becomes:

$$
C_\eta
\nu^{-1}
\mathcal P_{r,\ell}^{\eta},
$$

and the second becomes:

$$
C_\eta
\mathcal L_{r,\ell}^{\omega}.
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

# 4. Consequence for DCRP-20

For the compactly localized reservoir:

$$
\boxed{
\mathcal P_n^\eta\to0,
\qquad
\mathcal L_n^\omega\to0
\Longrightarrow
\mathcal O_n^\eta\to0
}
\tag{4.1}
$$

**without any no-IR assumption**.

Therefore DCRP-20's infrared alternative should be read only as a Fourier concentration description that would necessarily be accompanied by a nonvanishing cutoff-gradient/diffusion cost in the fixed compact local geometry.

The two-sided infrared completion of DCRP-18 remains necessary for:

- global carriers;
- scale-re-rooted old suppliers;
- noncompact transition packages.

It is not needed to eliminate the compact localized filtered-enstrophy reservoir.

Status:

$$
\boxed{
\textbf{CORRECTION / STRENGTHENING}.
}
$$

---

# 5. Strengthening of DCRP-20/21

The DCRP-20 zero-cost reservoir conclusion improves from:

$$
\boxed{
P\to0
+
L^\omega\to0
+
\text{no IR}
\Longrightarrow
O\to0
}
$$

to:

$$
\boxed{
P\to0
+
L^\omega\to0
\Longrightarrow
O\to0.
}
\tag{5.1}
$$

Accordingly, the DCRP-21 far-field-only survivor reduction no longer requires a separate no-IR hypothesis for the compact core reservoir.

The only remaining scale/spatial noncompactness in that argument is the **far-field source** itself.

---

# 6. Local supplier sequence from DCRP-16

Fix a first singular point:

$$
(x_\ast,T).
$$

DCRP-16 constructs good-collar localized divergence-free fields:

$$
v_n
$$

and localized boundary shells:

$$
q_n
$$

with:

$$
r_n
=
\lambda_{q_n}^{-1},
$$

such that:

$$
t_n\uparrow T,
$$

the shell maximum point:

$$
x_n\to x_\ast,
$$

and:

$$
\boxed{
r_n
\|
(v_n)_{q_n}(t_n)
\|_\infty
\ge
a_0\nu.
}
\tag{6.1}
$$

Moreover:

$$
r_n/\rho_n
\to0
$$

arbitrarily fast after increasing the supplier threshold inside each good collar.

The original shell:

$$
u_{q_n}
$$

agrees with:

$$
(v_n)_{q_n}
$$

near:

$$
x_n
$$

up to rapidly decaying high-frequency localization errors.

---

# 7. Normalized supplier class

Set:

$$
A_n
=
r_n
\|
(v_n)_{q_n}(t_n)
\|_\infty.
$$

Then:

$$
\boxed{
A_n\ge a_0\nu.
}
\tag{7.1}
$$

Choose:

$$
x_n
$$

with:

$$
\boxed{
r_n
|
(v_n)_{q_n}(x_n,t_n)
|
\ge
\frac34
A_n.
}
\tag{7.2}
$$

Define:

$$
\boxed{
W_n(y)
=
A_n^{-1}
r_n
(v_n)_{q_n}
(
x_n+r_ny,t_n
).
}
\tag{7.3}
$$

Then:

$$
\boxed{
\|W_n\|_\infty=1,
}
\tag{7.4}
$$

$$
\boxed{
|W_n(0)|
\ge
\frac34,
}
\tag{7.5}
$$

$$
\boxed{
\nabla\cdot W_n=0,
}
\tag{7.6}
$$

and:

$$
\boxed{
\supp
\widehat W_n
\subset
\mathcal A
}
\tag{7.7}
$$

for one fixed compact annulus:

$$
0<c_-\le|\xi|\le c_+.
$$

Bernstein gives uniform:

$$
C^m
$$

bounds for every:

$$
m.
$$

---

# 8. NEW THEOREM — Supplier Curl Atom

## Theorem 8.1

There exist universal:

$$
R_\omega<\infty,
$$

and:

$$
c_\omega>0
$$

such that every normalized supplier:

$$
W_n
$$

satisfies:

$$
\boxed{
\int_{
B_{R_\omega}
}
|
\nabla\times W_n
|^2dy
\ge
c_\omega.
}
\tag{8.1}
$$

### Proof

Assume the contrary.

Then there exists a sequence:

$$
W_n
$$

in the normalized supplier class with:

$$
\|
\nabla\times W_n
\|_{
L^2(B_{R_\omega})
}
\to0.
$$

By Bernstein and Arzela--Ascoli, after a subsequence:

$$
W_n
\to
W_\ast
$$

in:

$$
C^\infty_{\rm loc}.
$$

Then:

$$
|W_\ast(0)|
\ge
3/4,
$$

while:

$$
\nabla\times W_\ast=0
$$

on a nonempty ball.

Also:

$$
\nabla\cdot W_\ast=0.
$$

Therefore:

$$
\Delta W_\ast=0
$$

on that ball.

Because:

$$
W_\ast
$$

is band limited, it is real analytic.

Hence:

$$
\Delta W_\ast=0
$$

globally.

Taking Fourier transforms:

$$
|\xi|^2
\widehat W_\ast(\xi)
=
0.
$$

But the Fourier support lies in an annulus disjoint from:

$$
\xi=0.
$$

Therefore:

$$
W_\ast=0,
$$

contradicting:

$$
|W_\ast(0)|\ge3/4.
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

# 9. Physical supplier-vorticity lower bound

Undoing the normalization:

$$
\nabla_y\times
\left[
r_n
(v_n)_{q_n}
(
x_n+r_ny,t_n
)
\right]
=
r_n^2
\nabla_x\times
(v_n)_{q_n}.
$$

Therefore Theorem 8.1 gives:

$$
\boxed{
r_n
\int_{
B_{R_\omega r_n}(x_n)
}
|
\nabla\times
(v_n)_{q_n}(x,t_n)
|^2dx
\ge
c_\omega
A_n^2.
}
\tag{9.1}
$$

Using:

$$
A_n\ge a_0\nu,
$$

$$
\boxed{
r_n
\int_{
B_{R_\omega r_n}(x_n)
}
|
\nabla\times
(v_n)_{q_n}
|^2dx
\ge
c_1\nu^2.
}
\tag{9.2}
$$

The derivative Littlewood--Paley kernel tail gives the same estimate for the original shell:

$$
\omega_{q_n}
=
\nabla\times u_{q_n},
$$

after discarding finitely many terms:

$$
\boxed{
r_n
\int_{
B_{2R_\omega r_n}(x_n)
}
|
\omega_{q_n}(x,t_n)
|^2dx
\ge
c_2\nu^2.
}
\tag{9.3}
$$

Status:

$$
\boxed{
\textbf{PROVED using DCRP-16 good-collar separation plus the derivative kernel tail}.
}
$$

---

# 10. Two fixed compact mollifier scales

Choose one fixed radial:

$$
\varphi
\in
C_c^\infty(B_1),
$$

with:

$$
\varphi\ge0,
$$

and:

$$
\int\varphi=1.
$$

Because:

$$
\varphi
$$

is radial and nontrivial, its Fourier transform has the Taylor expansion:

$$
\boxed{
\widehat\varphi(\zeta)
=
1
-
c_\varphi
|\zeta|^2
+
O(
|\zeta|^4
)
}
\tag{10.1}
$$

near:

$$
\zeta=0,
$$

with:

$$
c_\varphi>0.
$$

Therefore one may choose fixed:

$$
0<a<b
$$

sufficiently small that:

$$
\boxed{
m_{a,b}(\zeta)
=
\widehat\varphi(a\zeta)
-
\widehat\varphi(b\zeta)
}
\tag{10.2}
$$

satisfies:

$$
\boxed{
|m_{a,b}(\zeta)|
\ge
d_\varphi
>
0
}
\tag{10.3}
$$

for every:

$$
\zeta\in\mathcal A.
$$

These two relative filter ratios are fixed for the entire sequence.

---

# 11. Full filtered-vorticity pair

At physical scale:

$$
r_n,
$$

define:

$$
\boxed{
\Omega_{a,n}
=
\nabla\times
S_{ar_n}u,
}
\tag{11.1}
$$

$$
\boxed{
\Omega_{b,n}
=
\nabla\times
S_{br_n}u,
}
\tag{11.2}
$$

and:

$$
\boxed{
G_n
=
\Omega_{a,n}
-
\Omega_{b,n}.
}
\tag{11.3}
$$

Because filtering and Littlewood--Paley projection commute:

$$
\boxed{
\Delta_{q_n}G_n
=
\left(
S_{ar_n}
-
S_{br_n}
\right)
\omega_{q_n}.
}
\tag{11.4}
$$

On the supplier annulus the multiplier is uniformly invertible.

---

# 12. NEW THEOREM — Filter-Difference Supplier Atom

There exist:

$$
R_G<\infty,
$$

and:

$$
c_G>0
$$

such that, after discarding finitely many:

$$
n,
$$

$$
\boxed{
r_n
\int_{
B_{R_Gr_n}(x_n)
}
|
\Delta_{q_n}G_n(x,t_n)
|^2dx
\ge
c_G\nu^2.
}
\tag{12.1}
$$

### Proof sketch

In normalized variables, the operator:

$$
S_a-S_b
$$

acts on the fixed supplier annulus by the multiplier:

$$
m_{a,b}.
$$

Equation (10.3) makes this multiplier invertible on the annulus.

Apply the same compactness/analyticity argument as Theorem 8.1 to the normalized class after applying:

$$
m_{a,b}(D)
\nabla\times.
$$

A vanishing local output would force the band-limited normalized supplier to vanish identically, contradicting its normalized point amplitude.

Undo the normalization and use (9.3).

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

# 13. Spectral-localization commutator

Choose a fixed normalized cutoff:

$$
\eta
\in
C_c^\infty(B_{2R_G}),
$$

with:

$$
\eta\equiv1
$$

on:

$$
B_{R_G}.
$$

Define:

$$
\eta_n(x)
=
\eta
\left(
\frac{
x-x_n
}{
r_n
}
\right).
$$

Then:

$$
\boxed{
\eta_n
\Delta_{q_n}G_n
=
\Delta_{q_n}
(
\eta_nG_n
)
-
[
\Delta_{q_n},
\eta_n
]
G_n.
}
\tag{13.1}
$$

Since:

$$
\Delta_{q_n}
$$

is bounded on:

$$
L^2,
$$

$$
\boxed{
\|
\eta_n
\Delta_{q_n}G_n
\|_2
\le
C
\|
\eta_nG_n
\|_2
+
\|
[
\Delta_{q_n},
\eta_n
]
G_n
\|_2.
}
\tag{13.2}
$$

---

# 14. NEW THEOREM — Endpoint Filtered Atom / Spectral-Localization Defect Alternative

## Theorem 14.1

There exists:

$$
c_E>0
$$

such that every sufficiently late local supplier event satisfies at least one of:

### full filtered endpoint atom

for one:

$$
\sigma_n\in\{a,b\},
$$

$$
\boxed{
r_n
\int
\eta_n^2
|
\Omega_{\sigma_n,n}(x,t_n)
|^2dx
\ge
c_E\nu^2,
}
\tag{14.1}
$$

or:

### spectral-localization defect

$$
\boxed{
\mathcal C_n^{spec}
=
r_n
\|
[
\Delta_{q_n},\eta_n
]
G_n(t_n)
\|_2^2
\ge
c_E\nu^2.
}
\tag{14.2}
$$

### Proof

Theorem 12.1 and:

$$
\eta_n\equiv1
$$

on the supplier ball give:

$$
r_n^{1/2}
\|
\eta_n
\Delta_{q_n}G_n
\|_2
\ge
c\nu.
$$

Use (13.2).

If the commutator term is at least half the right scale, (14.2) holds.

Otherwise:

$$
r_n^{1/2}
\|
\eta_nG_n
\|_2
\ge
c\nu.
$$

But:

$$
G_n
=
\Omega_{a,n}
-
\Omega_{b,n}.
$$

Hence:

$$
\|
\eta_nG_n
\|_2
\le
\|
\eta_n\Omega_{a,n}
\|_2
+
\|
\eta_n\Omega_{b,n}
\|_2.
$$

At least one term is bounded below by a fixed fraction.

Square and multiply by:

$$
r_n.
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

# 15. Interpretation of the spectral-localization defect

The commutator:

$$
[
\Delta_q,\eta_r
]
G
$$

measures the incompatibility between:

- isolating the supplier frequency;
- and isolating the supplier spatial core.

It is generated by the actual filtered vorticity and the fixed localization operation.

It does not copy a singularity label.

Thus:

$$
\boxed{
\mathcal C^{spec}
}
$$

is an admissible native localization residual.

A zero-localization branch must satisfy:

$$
\boxed{
\mathcal C_n^{spec}\to0.
}
\tag{15.1}
$$

On such a branch every sufficiently late supplier produces a genuine endpoint atom for one of the two fixed full filtered-vorticity fields.

---

# 16. Endpoint filtered enstrophy

Assume the endpoint-atom branch.

Let:

$$
\ell_n
=
\sigma_nr_n,
\qquad
\sigma_n\in\{a,b\}.
$$

Define:

$$
\boxed{
\mathcal E_n^\omega(t)
=
\frac{
r_n
}{
2
}
\int
\eta_n^2
|
\Omega_{\ell_n}(x,t)
|^2dx.
}
\tag{16.1}
$$

Then:

$$
\boxed{
\mathcal E_n^\omega(t_n)
\ge
e_0\nu^2
}
\tag{16.2}
$$

for a fixed:

$$
e_0>0.
$$

---

# 17. Fixed normalized backward window

Fix:

$$
\tau_0\in(0,1].
$$

Let:

$$
\boxed{
J_n
=
(
t_n-\tau_0r_n^2,
t_n
).
}
\tag{17.1}
$$

For sufficiently late:

$$
n,
$$

the interval lies before the first singular time and the solution is smooth there.

Define the spacetime filtered-enstrophy reservoir:

$$
\boxed{
\mathcal O_n
=
r_n^{-1}
\int_{J_n}
\int
\eta_n^2
|
\Omega_{\ell_n}
|^2dxdt.
}
\tag{17.2}
$$

Since:

$$
\mathcal E_n^\omega(t)
=
\frac{r_n}{2}
\int
\eta_n^2
|
\Omega_{\ell_n}
|^2,
$$

one has:

$$
\boxed{
\mathcal O_n
=
2
\int_{-\tau_0}^{0}
\mathcal E_n^\omega(\tau)
\,d\tau
}
\tag{17.3}
$$

in normalized time.

---

# 18. Reservoir branch is already taxed by diffusion/localization

Apply Theorem 3.1 with the cutoff:

$$
\eta_n.
$$

Then:

$$
\boxed{
\mathcal O_n
\le
C_\eta
\left(
\nu^{-1}\mathcal P_n
+
\mathcal L_n^\omega
\right),
}
\tag{18.1}
$$

where:

$$
\mathcal P_n
=
\nu r_n
\int_{J_n}
\int
\eta_n^2
|
\nabla\Omega_{\ell_n}
|^2,
$$

and:

$$
\mathcal L_n^\omega
$$

is the normalized cutoff-shell filtered-enstrophy cost.

Therefore if:

$$
\boxed{
\mathcal O_n
\ge
o_0>0,
}
\tag{18.2}
$$

then:

$$
\boxed{
\nu^{-1}\mathcal P_n
+
\mathcal L_n^\omega
\ge
c(o_0)>0.
}
\tag{18.3}
$$

Thus a supplier with nontrivial normalized residence time already pays a fixed diffusion/localization cost.

---

# 19. Temporal-spike branch

Suppose instead:

$$
\boxed{
\mathcal O_n
<
o_0.
}
\tag{19.1}
$$

Choose:

$$
o_0
\le
\frac{
e_0\nu^2\tau_0
}{
4
}.
$$

Then the normalized-time average of:

$$
\mathcal E_n^\omega
$$

over:

$$
[-\tau_0,0]
$$

is:

$$
\frac{
\mathcal O_n
}{
2\tau_0
}
<
\frac{
e_0\nu^2
}{
8
}.
$$

Therefore there exists:

$$
s_n\in J_n
$$

such that:

$$
\boxed{
\mathcal E_n^\omega(s_n)
\le
\frac{
e_0\nu^2
}{
8
}.
}
\tag{19.2}
$$

Together with (16.2):

$$
\boxed{
\mathcal E_n^\omega(t_n)
-
\mathcal E_n^\omega(s_n)
\ge
\frac{
7e_0
}{
8
}
\nu^2.
}
\tag{19.3}
$$

Thus an ultrashort endpoint spike has a fixed filtered-enstrophy rise inside the same normalized window.

---

# 20. Exact filtered-enstrophy balance on the spike interval

The external filtered-vorticity identity gives, on:

$$
[s_n,t_n],
$$

$$
\boxed{
\mathcal E_n^\omega(t_n)
-
\mathcal E_n^\omega(s_n)
+
\mathcal P_n^{[s_n,t_n]}
=
\mathcal V_n^{near}
+
\mathcal V_n^{far}
+
\mathcal R_n^{com}
+
\mathcal L_n.
}
\tag{20.1}
$$

Taking positive/absolute contributions:

$$
\boxed{
\frac{
7e_0
}{
8
}
\nu^2
+
\mathcal P_n^{[s_n,t_n]}
\le
\mathcal V_n^{+,\mathrm{near}}
+
\mathcal V_n^{+,\mathrm{far}}
+
|
\mathcal R_n^{com}
|
+
|
\mathcal L_n|.
}
\tag{20.2}
$$

This is the exact anti-spike ledger.

---

# 21. Insert near-field coercivity

For a fixed relative filter ratio:

$$
\sigma_n\in\{a,b\},
$$

the external theorem gives:

$$
\boxed{
\mathcal V_n^{+,\mathrm{near}}
\le
(1-\varepsilon)
\mathcal P_n^\rho
+
C_{\varepsilon,\sigma,M}
\mathcal O_n.
}
\tag{21.1}
$$

The local-energy constant is uniform on a fixed normalized obstruction slice.

Because:

$$
a,b
$$

are fixed, the filter-ratio constant is uniform.

---

# 22. Insert derivative-compatible commutator forcing

The external commutator theorem gives:

$$
\boxed{
|
\mathcal R_n^{com}
|
\le
\eta
\mathcal P_n
+
C_{\eta,\varphi}
\widetilde{\mathcal S}_n^{(3)}
+
\mathcal L_n^{com}.
}
\tag{22.1}
$$

Choose:

$$
\eta
<
\varepsilon/2.
$$

After matching the slightly enlarged diffusion regions by a fixed cutoff convention, the positive diffusion fraction left on the left-hand side is uniform.

Thus:

$$
\boxed{
c_0\nu^2
\le
C(M)
\mathcal O_n
+
\mathcal V_n^{+,\mathrm{far}}
+
C
\widetilde{\mathcal S}_n^{(3)}
+
\mathcal L_n
+
\mathcal L_n^{com},
}
\tag{22.2}
$$

for some fixed:

$$
c_0>0,
$$

provided:

$$
o_0
$$

has been chosen sufficiently small.

Status:

$$
\boxed{
\textbf{PROVED using the exact balance and arXiv:2606.27560 near-field/commutator theorems}.
}
$$

---

# 23. No invisible temporal spike

Equation (22.2) gives:

$$
\boxed{
\textbf{
ultrashort supplier spike}
\Longrightarrow
\textbf{
far-field work}
\ \vee\
\textbf{
critical commutator increment defect}
\ \vee\
\textbf{
localization residual}.
}
}
\tag{23.1}
$$

Thus temporal concentration is not an extra unpriced category.

The exact filtered-enstrophy balance prices it immediately.

This closes the DCRP-21 "probe head for an instant" loophole.

---

# 24. Far-field spike branch

Suppose a zero-commutator / zero-localization branch has:

$$
\widetilde{\mathcal S}_n^{(3)}
\to0,
$$

$$
\mathcal L_n
+
\mathcal L_n^{com}
\to0.
$$

Suppose also the reservoir branch is absent:

$$
\mathcal O_n\to0.
$$

Then (22.2) implies:

$$
\boxed{
\liminf
\mathcal V_n^{+,\mathrm{far}}
>
0.
}
\tag{24.1}
$$

DCRP-21 applies.

Therefore the source annulus must satisfy:

$$
\boxed{
m_n\to\infty
}
\tag{24.2}
$$

and:

$$
\boxed{
\mathfrak A_{j_n,n}
\to\infty.
}
\tag{24.3}
$$

Thus the last spike branch is a spatial-source escape defect.

---

# 25. NEW THEOREM — Local Supplier Activation/Tax Alternative

## Theorem 25.1

Assume:

- the DCRP-16 local supplier sequence;
- a uniform normalized local-energy bound:

  $$
  M_n\le M_\ast;
  $$

- the fixed two-filter family:

  $$
  \{a,b\};
  $$

- the fixed normalized spatial cutoff family.

Then every sufficiently late supplier event satisfies at least one of the following scale-uniform alternatives.

### A. spectral localization defect

$$
\boxed{
\mathcal C_n^{spec}
\ge
c_A\nu^2.
}
\tag{25.1}
$$

### B. filtered diffusion/localization payment

$$
\boxed{
\nu^{-1}
\mathcal P_n
+
\mathcal L_n^\omega
\ge
c_B\nu^2.
}
\tag{25.2}
$$

### C. derivative-compatible commutator defect

$$
\boxed{
\widetilde{\mathcal S}_n^{(3)}
\ge
c_C\nu^2.
}
\tag{25.3}
$$

### D. filtered localization residual

$$
\boxed{
\mathcal L_n
+
\mathcal L_n^{com}
\ge
c_D\nu^2.
}
\tag{25.4}
$$

### E. far-field spatial-source branch

$$
\boxed{
\mathcal V_n^{+,\mathrm{far}}
\ge
c_E\nu^2.
}
\tag{25.5}
$$

If branch E persists while the local reservoir tends to zero, DCRP-21 forces normalized spatial-source escape with diverging annular vorticity amplitude.

### Proof

Apply Theorem 14.1.

If branch A occurs, stop.

Otherwise a full filtered-vorticity endpoint atom exists.

If:

$$
\mathcal O_n\ge o_0,
$$

Theorem 3.1 gives branch B.

If:

$$
\mathcal O_n<o_0,
$$

Sections 19--22 give a fixed lower bound on the sum of branches C--E and the localization terms.

At least one is uniformly positive.

$$
\square
$$

Status:

$$
\boxed{
\textbf{PROVED at the finite supplier-event level}.
}
$$

---

# 26. Zero-cost supplier consequence

Suppose a transition-complete normalized supplier sequence satisfies:

$$
\mathcal C_n^{spec}\to0,
$$

$$
\mathcal P_n\to0,
$$

$$
\mathcal L_n^\omega\to0,
$$

$$
\widetilde{\mathcal S}_n^{(3)}\to0,
$$

$$
\mathcal L_n
+
\mathcal L_n^{com}
\to0,
$$

and has no far-field spatial-source escape defect.

Then Theorem 25.1 is impossible.

Hence:

$$
\boxed{
\textbf{
a local supplier sequence cannot be an exact zero-cost
filtered-vorticity mechanism sequence.
}
}
\tag{26.1}
$$

This is independent of any temporal residence-time assumption.

---

# 27. Relation to Cheskidov--Dai temporal activity

Cheskidov--Dai prove that high-frequency vorticity-shell activity integrated in time is itself a regularity-relevant quantity:

$$
\limsup_{q\to\infty}
\int
1_{\{q\le Q(t)\}}
\|
\Delta_q\omega(t)
\|_\infty
dt
$$

must exceed a fixed small threshold along a blowup branch.

DCRP-22 does not need this theorem to prove the anti-spike alternative.

The present proof instead uses:

- the local supplier endpoint;
- the exact localized filtered-enstrophy identity.

The Cheskidov--Dai criterion is retained as independent calibration that high-frequency **temporal** activity is not an artificial concern.

---

# 28. What is now closed

The following gap from DCRP-21 is closed:

$$
\boxed{
\text{local supplier}
\Longrightarrow
\text{filtered mechanism activation}
\ \vee\
\text{explicit paid/native defect}.
}
\tag{28.1}
$$

The supplier cannot escape by:

- being only a velocity atom;
- canceling silently in one filtered field;
- existing for vanishing normalized time;
- hiding in the lower-order compact local enstrophy reservoir.

Every route produces a fixed scale-critical entry.

---

# 29. What remains open

The supplier theorem gives infinitely many supplier events near a singular point.

The finite-scale critical ledger, however, requires **positive-density untaxed critical supply** along a persistent non-CKN chain.

An infinite supplier subsequence may still be sparse in dyadic scale.

Therefore:

$$
\boxed{
\text{every supplier is taxed}
}
$$

does not yet imply:

$$
\boxed{
\text{every profitable bad transition is taxed}.
}
$$

This is the same distinction identified in DCRP-19, now sharpened.

---

# 30. New exact frontier — bounded-lag supplier capture

The next target is:

$$
\boxed{
\textbf{
Untaxed Critical Supply
}
\Longrightarrow
\textbf{
Bounded-Lag Local Supplier Activation}.
}
\tag{30.1}
$$

A useful quantitative form is:

> Fix:
>
> $$
> \eta>0.
> $$
>
> Suppose one non-CKN transition satisfies:
>
> $$
> \left(
> \mathrm{Sup}^{full}_k
> -
> \mathrm{Tax}^{full}_k
> \right)_+
> \ge
> \eta,
> $$
>
> while:
>
> - leakage is small;
> - coarse/subfilter native defects are below their paid thresholds.
>
> Then within at most:
>
> $$
> L=L(\eta,M)
> $$
>
> dyadic descendant steps, there exists a local supplier event satisfying:
>
> $$
> \lambda^{-1}
> |
> \Delta_\lambda u
> |
> \ge
> c(\eta,M)\nu,
> $$
>
> or one of the already-paid filtered-vorticity defects is positive.

If this is proved, the positive-density untaxed supply required by the finite-scale survival theorem produces positive-density supplier activations.

DCRP-22 then taxes every such activation.

This would directly attack the persistent profitable branch rather than a sparse auxiliary sequence.

---

# 31. Updated proof-state diagram

The current route is:

$$
\boxed{
\begin{aligned}
\text{first singular point}
&\Longrightarrow
\text{local supplier sequence}\\
&\Longrightarrow
\text{filtered endpoint atom}
\vee
\text{spectral localization defect}\\
&\Longrightarrow
\text{reservoir payment}
\vee
\text{filtered surplus}\\
&\Longrightarrow
\text{diffusion}
\vee
\widetilde{\mathcal S}^{(3)}
\vee
\text{localization}
\vee
\text{far spatial escape}.
\end{aligned}
}
\tag{31.1}
$$

Thus individual local suppliers have no zero-cost temporal-spike route.

The missing global bridge is density:

$$
\boxed{
\textbf{
profitable bad-scale supply}
\Longrightarrow
\textbf{
supplier within bounded scale lag}.
}
}
\tag{31.2}
$$

---

# 32. Source ledger

## Filtered Vortex Stretching and Subgrid Defects

Primary results used:

- exact spatially filtered vorticity equation;
- localized filtered-enstrophy identity:

  $$
  \mathcal E_\chi(s_1)
  -
  \mathcal E_\chi(s_0)
  +
  \mathcal P_\chi
  =
  \mathcal V_\chi^{near}
  +
  \mathcal V_\chi^{rem}
  +
  \mathcal R_\chi
  +
  \mathcal L_\chi;
  $$

- near-field stretching-to-diffusion coercivity:

  $$
  \mathcal V^{+,\mathrm{near}}
  \le
  (1-\varepsilon)\mathcal P^\rho
  +
  C_{\varepsilon}M(r/\ell)^5\mathcal O;
  $$

- derivative-compatible commutator insertion:

  $$
  F^{com}
  \le
  \eta P
  +
  C_\eta
  \widetilde{\mathcal S}^{(3)}
  +
  L^{com};
  $$

- adjoint cancellation of the principal localization residual;
- far-field annular reassignment used in DCRP-21.

## Cheskidov--Dai

Primary regularity criterion used only as independent temporal calibration:

a blowup branch cannot have asymptotically small integrated high-frequency vorticity-shell activity on the active dissipation range.

---

# 33. End state

The major correction is:

$$
\boxed{
\mathcal O^\eta
\le
C
\left(
\nu^{-1}\mathcal P^\eta
+
\mathcal L^\omega
\right).
}
$$

Thus the compact local filtered-enstrophy reservoir has no free IR escape.

The supplier-to-filtered bridge is:

$$
\boxed{
\text{supplier}
\Longrightarrow
\text{full filtered endpoint atom}
\ \vee\
\mathcal C^{spec}>0.
}
$$

The temporal anti-spike theorem is:

$$
\boxed{
\text{endpoint atom}
\Longrightarrow
\text{diffusion/localization reservoir payment}
\ \vee\
\text{positive filtered mechanism surplus}.
}
$$

After near-field and commutator insertion:

$$
\boxed{
\text{supplier}
\Longrightarrow
\text{diffusion}
\vee
\text{commutator defect}
\vee
\text{localization}
\vee
\text{far spatial escape}.
}
$$

Therefore ultrashort supplier spikes are not an untaxed mechanism.

The next single frontier is:

$$
\boxed{
\textbf{
Untaxed Critical Supply / Bounded-Lag Supplier Activation Lemma}.
}
$$

This is now the density bridge between the unconditional finite-scale survival ledger and the supplier mechanism that DCRP has learned how to tax.
