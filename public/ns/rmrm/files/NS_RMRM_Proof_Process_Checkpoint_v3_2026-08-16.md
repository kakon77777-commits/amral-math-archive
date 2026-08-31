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
