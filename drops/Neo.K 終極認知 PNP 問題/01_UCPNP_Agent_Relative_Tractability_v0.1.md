# 智能體相對可解性：Cognitive-P-like 與 Cognitive-NP-like 操作狀態的形式化

**English title:** *Agent-Relative Tractability: Formalizing Cognitive-P-like and Cognitive-NP-like Operational Regimes*  
**Series:** Neo.K Ultimate Cognitive P/NP  
**Canonical parent:** Paper 00 — *The Neo.K Ultimate Cognitive P/NP Problem: Canonical Definition, Scope, and Research Program*  
**Paper:** 01  
**Definition origin:** Neo.K  
**Formalization:** Neo.K with Aletheia  
**Research organization:** EveMissLab  
**Version:** v0.1  
**Date:** 2026-08-15  
**Status:** Formal foundational draft; theorem claims in this document are internal consequences of the stated finite-resource definitions, not claims about classical $P$ versus $NP$.

---

# Canonical non-identity statement

$$
\boxed{
P_{\mathrm{cog}},NP_{\mathrm{cog}}
\text{ are Neo.K operational cognitive regimes, not classical complexity classes.}
}
$$

In particular,

$$
\boxed{
\mathrm{UCPNP}_{\mathrm{Neo.K}}
\neq
(P\stackrel{?}{=}NP)_{\mathrm{classical}}.
}
$$

本文不主張改寫、證明或消解標準複雜度理論中的 $P$、$NP$、NP-hard、NP-complete。本文研究的問題是：**在任務語義固定、外部資訊與預計算成本被記帳、智能體狀態與資源預算被明示的條件下，同一任務對不同智能體或不同歷史狀態是否呈現不同的操作性可解程度。**

---

# 摘要

本文形式化 Neo.K 終極認知 P/NP 研究綱領中的第一個核心數學對象：**智能體相對可解性**。我們不將「難」視為問題或智能體的單一標籤，而將其表示為任務語義、智能體操作能力、可取得資訊、資源向量、成功可靠度與證據契約共同決定的關係。

為避免「換一個智能體就能隨意重新命名 P/NP」的空泛相對主義，本文引入六個約束：固定任務語義、顯式資源偏序、合法策略集、外部資訊記帳、成功／驗證可靠度門檻，以及表示轉換的語義保持條件。在此基礎上，我們定義 completion 與 verification 的 Pareto 資源前沿，並以無權重的 normalized bottleneck ratio

$$
\rho_{\star}(x\mid \Xi,\mathbf B)
=
\inf_{\pi\in\Pi_{\star}}
\max_i
\frac{c_i(\pi,x)}{B_i},
\qquad
\star\in\{C,V\},
$$

描述任務相對於當前預算的資源距離。若完整完成所需最優 bottleneck ratio 不超過 $1$，則任務處於 cognitive-P-like regime；若外部給定候選後的驗證可在預算內完成，但從當前狀態自行取得可提交成果不可在預算內完成，則任務處於 cognitive-NP-like regime。

本文證明若干由定義直接導出的結構性結果：資源單調性、能力擴張單調性、操作等價智能體的不變性、成本保持重編碼不變性、預計算守恆與外部 oracle 透明性。我們並區分 exact/proven、empirical/observed 與 unresolved 三種認知 regime 證據狀態，避免在開放智能系統中把「目前沒找到策略」誤寫成「不存在策略」。

本文最後給出九類失敗案例，包括答案注入、免費 oracle、改題式 bypass、隱藏預計算、不可比較資源、一次性 advice、幸運猜測與自我授權 certification。這些反例共同建立一個核心原則：

$$
\boxed{
\text{Agent-relative}
\neq
\text{arbitrary-relative}.
}
$$

**關鍵詞：** agent-relative tractability、Cognitive-P、Cognitive-NP、bounded optimality、resource rationality、metareasoning、resource vector、Pareto frontier、precomputation accounting、representation invariance

---

# 0. Claim typing

本文核心陳述使用 Paper 00 的五類標記：

- **D** — Definition；
- **T** — Theorem；
- **C** — Conjecture；
- **E** — Empirical Hypothesis；
- **N** — Normative Axiom。

本文的主要數學結果屬於 **D/T**。例如「資源增加不能使既有可行策略失效」是定義下的 theorem；「人類或 ASI 的實際認知成本是否符合此模型」則必須留到 empirical papers，不在本文宣稱。

---

# 1. 問題：智能體相對可解性不能退化成主觀標籤

Paper 00 定義智能體歷史狀態：

$$
\Xi_t
=
(A_t,K_t,\Sigma_t,\Gamma_t,H_t,M_t,N_t,E_t),
$$

並提出 cognitive-P-like / cognitive-NP-like 操作狀態。

但若不加限制，這組語言有三個立即風險。

第一，**答案注入風險**：只要把答案放進 $K_t$，任何有限實例都可以變得「容易」。

第二，**改題風險**：只要允許任意重寫目標，就能把「解 SAT」改成「輸出 0」，再宣稱問題變簡單。

第三，**不可證不存在風險**：對真實人類或大型 AI，我們幾乎不可能量化所有可能策略，因此「目前沒有找到可行策略」不能直接等同「不存在可行策略」。

因此智能體相對可解性若要成為研究理論，必須先建立：

$$
\boxed{
\text{Task invariance}
+
\text{resource accounting}
+
\text{policy admissibility}
+
\text{evidence typing}.
}
$$

本文就是完成這四件事。

---

# 2. 任務語義契約

## 2.1 Verification-bearing task contract

**D2.1（任務語義契約）**  
定義一個可驗證任務契約：

$$
\boxed{
\mathfrak T
=
(\mathcal X,\mathcal Y,\mathsf{Goal},\mathsf{Ver},\mathsf{Cert},\equiv_{\mathfrak T},\mathcal I_{\mathrm{adm}}).
}
$$

其中：

- $\mathcal X$：輸入／問題實例空間；
- $\mathcal Y$：候選輸出或任務終態空間；
- $\mathsf{Goal}(x,y)$：輸出是否完成原任務語義；
- $\mathsf{Ver}(x,y,e)$：候選 $y$ 與證據 $e$ 是否通過指定驗證；
- $\mathsf{Cert}$：可提交 certification 的額外規範；
- $\equiv_{\mathfrak T}$：允許的任務等價終態關係；
- $\mathcal I_{\mathrm{adm}}$：允許使用的外部資訊型別與來源規格。

若使用 $\mathsf{Bypass}$，其結果 $y'$ 必須滿足：

$$
y'\equiv_{\mathfrak T}y
$$

對某個原契約合法完成態 $y$ 成立。否則不是 bypass，而是改題。

## 2.2 任務身分不變條件

兩次認知可解性比較只有在以下條件成立時才有意義：

$$
\boxed{
\mathfrak T_{\mathrm{before}}
\simeq
\mathfrak T_{\mathrm{after}}.
}
$$

其中 $\simeq$ 至少要求：

1. 成功條件不被弱化；
2. 驗證條件不被偷換；
3. certification 標準若改變，必須顯式列出；
4. 若輸入表示改變，必須存在語義保持的 translation；
5. 若輸出終態改變，必須在事先聲明的 $\equiv_{\mathfrak T}$ 下等價。

這條規則禁止以下偽轉換：

$$
\text{hard task}
\to
\text{easier different task}
\to
\text{claim tractability gain}.
$$

---

# 3. 智能體操作契約

## 3.1 Operational agent model

**D3.1（操作智能體）**  
對狀態 $\Xi$，定義其操作模型：

$$
\boxed{
\mathfrak A_{\Xi}
=
(\mathcal O_{\Xi},\Pi_{\Xi},\mathcal Z_{\Xi},\mathsf{Obs}_{\Xi},\mathsf{Cost}_{\Xi}).
}
$$

其中：

- $\mathcal O_{\Xi}$：允許的基本操作；
- $\Pi_{\Xi}$：由這些操作構成的 admissible policies；
- $\mathcal Z_{\Xi}$：內部／外部可觀察狀態；
- $\mathsf{Obs}_{\Xi}$：資訊取得機制；
- $\mathsf{Cost}_{\Xi}$：每種操作及其組合的資源成本模型。

Paper 00 的基本操作族為：

$$
\mathcal O_{\mathrm{UCPNP}}
=
\{
\mathsf{Represent},
\mathsf{Find},
\mathsf{Ask},
\mathsf{Generate},
\mathsf{Create},
\mathsf{Bypass},
\mathsf{Execute},
\mathsf{Verify},
\mathsf{Certify}
\}.
$$

不同智能體不必擁有相同操作集。

## 3.2 Admissible policy

**D3.2（合法策略）**  
策略 $\pi$ 為 admissible，若且唯若：

1. 僅使用 $\mathcal O_{\Xi}$ 中允許的操作；
2. 僅讀取 $K,\Sigma,M,N,E$ 中已聲明可取得的資訊；
3. 所有外部詢問、oracle、工具與人工協助都經 $\mathcal I_{\mathrm{adm}}$ 註冊；
4. 所有預計算與離線建造成本按契約處理；
5. 不利用 benchmark hidden data、答案洩漏或未授權 side channel；
6. completion、verification、certification 不互相偷換。

因此：

$$
\boxed{
\text{available information}
\neq
\text{free information}.
}
$$

---

# 4. 資源向量與偏序

## 4.1 Resource vector

定義 $d$ 維資源成本：

$$
\mathbf c
=
(c_1,\ldots,c_d)
\in
\mathbb R_+^d,
$$

與預算：

$$
\mathbf B
=
(B_1,\ldots,B_d)
\in
\mathbb R_+^d.
$$

可能包含：

$$
(T,E,M,Q,C,\mathrm{comm},\mathrm{risk},\ldots).
$$

本文不要求所有研究使用同樣的資源維度，但要求比較雙方使用**同一資源座標與單位**。

## 4.2 Componentwise preorder

定義：

$$
\mathbf c\preceq\mathbf B
\iff
c_i\le B_i,
\quad\forall i.
$$

這是一個偏序，不是總序。

因此兩個資源包：

$$
(1\text{ hour},1\text{ TB})
$$

與

$$
(10\text{ hours},1\text{ GB})
$$

未必誰「比較大」。

這一點阻止我們把所有智能體粗暴排成一條單一能力排行榜。

## 4.3 成本統計契約

對隨機策略，$c_i$ 可以是：

- worst-case；
- expectation；
- $p$-quantile；
- high-probability bound；
- risk-sensitive functional。

但每篇研究必須事先指定，不能在結果不利時更換統計口徑。

---

# 5. Completion 與 Verification 的資源前沿

## 5.1 Completion policy

令 $\Pi_C(x\mid\Xi)$ 為所有可從當前狀態自行產生一個符合 $\mathsf{Goal}$、$\mathsf{Ver}$ 與指定 $\mathsf{Cert}$ 的完整完成策略。

對 $\pi\in\Pi_C$，令：

$$
p_C(\pi,x)
=
\Pr[\pi\text{ completes }\mathfrak T\text{ correctly}],
$$

及資源向量：

$$
\mathbf c_C(\pi,x).
$$

給定可靠度需求 $1-\delta_C$，定義 completion 可行成本集合：

$$
\mathcal C_C(x\mid\Xi,\delta_C)
=
\left\{
\mathbf c_C(\pi,x):
\pi\in\Pi_C,
\ p_C(\pi,x)\ge1-\delta_C
\right\}.
$$

其 Pareto-minimal frontier 為：

$$
\boxed{
\mathcal F_C(x\mid\Xi,\delta_C)
=
\operatorname{Min}_{\preceq}
\mathcal C_C(x\mid\Xi,\delta_C).
}
$$

## 5.2 Verification policy

令 $\Pi_V(x,y\mid\Xi)$ 為「候選 $y$ 已由外部提供」時可使用的合法驗證／認證策略。

給定 verifier reliability $1-\delta_V$，定義：

$$
\mathcal C_V(x,y\mid\Xi,\delta_V)
=
\left\{
\mathbf c_V(\nu,x,y):
\nu\in\Pi_V,
\ p_V(\nu,x,y)\ge1-\delta_V
\right\}.
$$

若任務具有一組合法候選 $\mathcal Y_x^+$，可使用 worst-case 或指定分布聚合：

$$
\mathcal F_V(x\mid\Xi,\delta_V)
=
\operatorname{Agg}_{y\in\mathcal Y_x^+}
\operatorname{Min}_{\preceq}
\mathcal C_V(x,y\mid\Xi,\delta_V).
$$

研究必須明示使用 worst-case、average-case 或 distributional contract。

---

# 6. 無權重 normalized bottleneck ratio

多維成本不應任意加權成一個分數。本文改用相對於**已明示預算**的 bottleneck normalization。

對任一成本向量 $\mathbf c$，定義：

$$
\beta(\mathbf c\mid\mathbf B)
=
\max_{i:B_i>0}
\frac{c_i}{B_i}.
$$

若某維 $B_i=0$ 而 $c_i>0$，則令 $\beta=\infty$。

對 completion：

$$
\boxed{
\rho_C(x\mid\Xi,\mathbf B,\delta_C)
=
\inf_{\mathbf c\in\mathcal C_C}
\beta(\mathbf c\mid\mathbf B).
}
$$

對 verification：

$$
\boxed{
\rho_V(x\mid\Xi,\mathbf B,\delta_V)
=
\inf_{\mathbf c\in\mathcal C_V}
\beta(\mathbf c\mid\mathbf B).
}
$$

因此：

$$
\rho<1
$$

表示存在有 slack 的策略；

$$
\rho=1
$$

表示位於預算邊界；

$$
\rho>1
$$

表示當前已知／允許策略無法在該預算契約內完成。

這個 scalarization 不引入任意權重 $w_i$；每個維度的相對重要性已由實驗者公開指定的 $B_i$ 表達。

---

# 7. Cognitive-P-like 與 Cognitive-NP-like 的正式定義

## 7.1 Cognitive-P-like

**D7.1（Cognitive-P-like operational regime）**

若：

$$
\boxed{
\rho_C(x\mid\Xi,\mathbf B,\delta_C)
\le1,
}
$$

則稱：

$$
\boxed{
x\in P_{\mathrm{cog}}(\Xi,\mathbf B;\delta_C).
}
$$

意思僅為：在**當前智能體操作模型與當前資源契約**下，存在一條合法且可靠度足夠的完整完成策略。

## 7.2 Cognitive-NP-like

**D7.2（Cognitive-NP-like operational regime）**

若：

$$
\boxed{
\rho_V(x\mid\Xi,\mathbf B,\delta_V)
\le1
<
\rho_C(x\mid\Xi,\mathbf B,\delta_C),
}
$$

則稱：

$$
\boxed{
x\in NP_{\mathrm{cog}}(\Xi,\mathbf B;\delta_C,\delta_V).
}
$$

其語義是：**候選一旦被提供，智能體可以在預算內確認／認證；但在當前狀態下，自行取得可提交成果所需資源超過預算。**

這正是 UCPNP 借用傳統 P/NP 直覺的地方，但沒有宣稱兩者同構。

## 7.3 Verification-hard / opaque regime

若：

$$
\rho_V>1,
$$

則候選本身也不能在當前契約內可靠確認。本文稱其為：

$$
\boxed{
V_{\mathrm{cog}}\text{-hard / opaque regime}.
}
$$

此名稱同樣不是 classical complexity class。

## 7.4 Unresolved regime

若 $\rho_C$ 或 $\rho_V$ 無法被充分上、下界夾住，則不得強行分類，記為：

$$
\boxed{
U_{\mathrm{cog}}\text{-unresolved}.
}
$$

「不知道」是一個合法結果。

---

# 8. Proven、Observed 與 Unresolved：避免把搜索失敗當成不存在

對有限 SDPE-BEB 類 micro-model，我們可能精確枚舉或證明最優策略，因此能建立：

$$
\rho_C^{\star},\rho_V^{\star}
$$

的 exact value。

但對人類、大型 AI 或開放世界，通常只能得到界：

$$
\underline\rho_C
\le
\rho_C^{\star}
\le
\overline\rho_C.
$$

因此本文建立三種證據狀態。

## 8.1 Proven regime

若有 theorem / exhaustive certificate 證明：

$$
\overline\rho_C\le1,
$$

則 proven P-like。

若：

$$
\overline\rho_V\le1
<
\underline\rho_C,
$$

則 proven NP-like。

## 8.2 Observed / empirical regime

若只知道某組已測策略：

$$
\widehat\rho_C>1,
$$

不能推出 $\rho_C^{\star}>1$。

只能標記：

$$
\boxed{
\widehat{NP}_{\mathrm{cog}}
\text{ or empirically NP-like under tested policy class}.
}
$$

## 8.3 Unresolved regime

若界跨過 $1$：

$$
\underline\rho_C\le1\le\overline\rho_C,
$$

則正式標為 unresolved。

這條規則阻止：

$$
\text{we failed to solve}
\Rightarrow
\text{no solution strategy exists}.
$$

---

# 9. 基本結構定理

## T9.1 資源單調性定理

若：

$$
\mathbf B\preceq\mathbf B',
$$

且任務、智能體狀態、成功標準與 admissible policy set 不變，則：

$$
\boxed{
\rho_C(x\mid\Xi,\mathbf B')
\le
\rho_C(x\mid\Xi,\mathbf B),
}
$$

且：

$$
\boxed{
\rho_V(x\mid\Xi,\mathbf B')
\le
\rho_V(x\mid\Xi,\mathbf B).
}
$$

**證明。** 對任何固定成本向量 $\mathbf c$，若 $B'_i\ge B_i$，則：

$$
\frac{c_i}{B'_i}
\le
\frac{c_i}{B_i}.
$$

取各維最大值後仍不增，再對策略取 infimum 即得。$\square$

**推論。** 在其他條件固定下，增加預算不能使已處於 cognitive-P-like 的任務變回 infeasible。

注意：此定理不表示「增加更多工具永遠有益」，因為工具可能同時改變協調成本、policy set 或環境；它只處理純粹的 budget expansion。

---

## T9.2 能力擴張單調性定理

設兩智能體狀態 $\Xi$ 與 $\Xi'$ 滿足：

$$
\Pi_C(\Xi)
\subseteq
\Pi_C(\Xi'),
$$

且所有舊策略在 $\Xi'$ 中的成本與成功率不劣於在 $\Xi$ 中：

$$
\mathbf c_{\Xi'}(\pi)
\preceq
\mathbf c_{\Xi}(\pi),
$$

$$
p_{\Xi'}(\pi)
\ge
p_{\Xi}(\pi).
$$

則：

$$
\boxed{
\rho_C(x\mid\Xi',\mathbf B)
\le
\rho_C(x\mid\Xi,\mathbf B).
}
$$

verification 同理。

**證明。** 新策略集合包含舊策略集合，且舊策略的 objective 不變差；對更大的可行集合取 infimum 不可能上升。$\square$

這裡真正被證明的是**操作能力的 dominance extension**，不是「更大的模型／更多 Agent」本身。

---

## T9.3 操作等價智能體不變性

若兩個智能體狀態 $\Xi_1,\Xi_2$ 對任務 $x$ 具有相同：

1. admissible policy outcome distributions；
2. observation interface；
3. cost vectors；
4. verification / certification semantics；

則：

$$
\boxed{
\rho_C(x\mid\Xi_1,\mathbf B)
=
\rho_C(x\mid\Xi_2,\mathbf B),
}
$$

$$
\boxed{
\rho_V(x\mid\Xi_1,\mathbf B)
=
\rho_V(x\mid\Xi_2,\mathbf B).
}
$$

因此其 cognitive regime 完全相同。

**意義。** UCPNP 不依賴「人」、「AI」、「後人類」等名稱本身，而依賴可操作結構。若兩種載體在研究契約下行為等價，理論沒有理由僅因名稱不同而給出不同 tractability classification。

---

## T9.4 成本保持重編碼不變性

設任務表示 $R_1,R_2$ 間存在雙向 translation：

$$
f:R_1\to R_2,
\qquad
g:R_2\to R_1,
$$

且：

1. $f,g$ 保持 $\mathsf{Goal}$ 與 $\mathsf{Ver}$ 語義；
2. translation cost 為零或已包含於兩側成本向量；
3. 每個 $R_1$ admissible policy 可轉成 $R_2$ policy，反之亦然；
4. 轉換後成功率與資源向量完全相同。

則：

$$
\boxed{
\rho_{C,R_1}
=
\rho_{C,R_2},
\qquad
\rho_{V,R_1}
=
\rho_{V,R_2}.
}
$$

**證明。** $f,g$ 建立 cost-preserving policy bijection，因此兩側 feasible cost sets 相同。$\square$

**近似版本。** 若 translation 引入明示 overhead $\boldsymbol\Delta$，則 regime 只在將 $\boldsymbol\Delta$ 記入成本後比較。

這條定理讓真正的 $\Gamma$ 型 representation gain 與單純換符號分開。

---

## T9.5 No-Free-Precomputation Lemma

設某 representation / index / lookup table 的建立成本為：

$$
\mathbf c_{\mathrm{pre}},
$$

建立後單次 online completion 成本為：

$$
\mathbf c_{\mathrm{on}}.
$$

對一次性任務，總成本至少為：

$$
\boxed{
\mathbf c_{\mathrm{one-shot}}
=
\mathbf c_{\mathrm{pre}}
+
\mathbf c_{\mathrm{on}}.
}
$$

對重用 $m$ 次且可完全攤銷的任務族，每次攤銷成本為：

$$
\boxed{
\mathbf c_{\mathrm{amortized}}
=
\frac{1}{m}\mathbf c_{\mathrm{pre}}
+
\mathbf c_{\mathrm{on}}.
}
$$

若 $\mathbf c_{\mathrm{pre}}$ 被定義為歷史既有 $\Sigma$ 或 $K$，則可以不計入**當次 online cost**，但研究必須明確標記為：

$$
\boxed{
\text{historically imported structure},
}
$$

不能稱為「無成本」。$\square$

---

## T9.6 Oracle Transparency Lemma

若加入外部 oracle $O$ 後：

$$
\rho_C(x\mid\Xi+O,\mathbf B)
<
\rho_C(x\mid\Xi,\mathbf B),
$$

則這是一個合法的 agent-state transition；但除非 oracle 的：

- access cost；
- query count；
- latency；
- reliability；
- information scope；
- construction / acquisition history；

均被顯式列入 $M,N,E$ 與資源契約，否則不得把 improvement 歸因為智能體內部算法能力提升。

形式上，oracle 增益是：

$$
\boxed{
\Delta\rho
=
\Delta\rho(\Xi\to\Xi+O),
}
$$

而不是：

$$
\Delta\rho
=
\Delta\rho(A\text{ alone}).
$$

$\square$

---

# 10. Tractability margin：避免臨界點被任意 threshold 翻轉

定義 completion margin：

$$
\boxed{
\mathfrak m_C
=
1-\rho_C.
}
$$

verification margin：

$$
\boxed{
\mathfrak m_V
=
1-\rho_V.
}
$$

則：

- $\mathfrak m>0$：在 budget 內有 slack；
- $\mathfrak m=0$：正好臨界；
- $\mathfrak m<0$：超出 budget。

若：

$$
|\mathfrak m_C|
\gg
\epsilon_{\mathrm{measure}},
$$

則 classification 對小幅測量誤差穩定。

若：

$$
|\mathfrak m_C|
\approx0,
$$

應標記為 **critical / threshold-sensitive**，而不是過度解讀其 P-like 或 NP-like 標籤。

這與舊動態速率理論的「相變」直覺相容，但本文只主張操作性 margin，不主張普遍物理相變定律。

---

# 11. Cognitive gap

在 $\rho_V>0$ 時，可定義無權重相對 gap：

$$
\boxed{
G_{\mathrm{cog}}
=
\frac{\rho_C}{\rho_V}.
}
$$

若：

$$
G_{\mathrm{cog}}\gg1,
$$

表示從零開始取得成果相對於驗證 supplied candidate 困難得多。

但 $G_{\mathrm{cog}}$ 不應單獨用作 classification，因為：

$$
\rho_C=100,
\quad
\rho_V=10
$$

雖然 gap $=10$，但兩者都超出 budget；此時不是 cognitive-NP-like，而是 verification-hard。

因此正確判定仍是二維：

$$
(\rho_C,\rho_V).
$$

---

# 12. Family-level agent-relative tractability

單一有限實例可能因查表、記憶或偶然先驗而變容易。若要研究具有一般性的智能能力，必須升到 task family。

令：

$$
\mathfrak F
=
\{\mathfrak T_n\}_{n\ge1},
$$

並指定：

- instance distribution $\mu_n$；
- resource schedule $\mathbf B(n)$；
- success thresholds $\delta_C(n),\delta_V(n)$；
- shared prior / advice budget $\mathbf B_{\mathrm{adv}}(n)$。

## D12.1 Uniform cognitive tractability

若存在一個**統一 meta-policy generator** $G$，對每個合法 instance $x\sim\mu_n$ 只使用契約允許的 shared prior 與 instance input，即能產生 admissible completion policy $\pi_x$，且：

$$
\rho_C(x\mid\Xi_n,\mathbf B(n))\le1
$$

以指定可靠度成立，則稱該 family 在此 agent-history contract 下 uniform cognitive-P-like。

若每個 instance 都額外附帶長度近似答案本身的 instance-specific advice，則必須把 advice 納入：

$$
K,
\Sigma,
\mathbf B_{\mathrm{adv}}.
$$

否則不能把「每題都已偷偷放答案」誤稱為 uniform intelligence。

本文故意不把 $\mathbf B(n)$ 限定為 polynomial，因為 UCPNP 研究的不是 classical complexity class；不同實驗可以使用 polynomial、physical-time、energy、query 或 historical resource schedules，但必須事先聲明。

---

# 13. Tractability transition

Paper 00 的核心問題不是靜態分類，而是 transition。

定義合法狀態轉換：

$$
\mathcal T:
(\Xi_t,\mathbf B_t)
\to
(\Xi_{t+\Delta},\mathbf B_{t+\Delta}),
$$

並為轉換本身指定成本：

$$
\mathbf c_{\mathcal T}.
$$

**D13.1（Cognitive tractability transition）**  
若：

$$
\rho_C(x\mid\Xi_t,\mathbf B_t)>1,
$$

而：

$$
\rho_C(x\mid\Xi_{t+\Delta},\mathbf B_{t+\Delta})\le1,
$$

則稱發生一個 cognitive tractability transition。

但 transition report 必須同時輸出：

$$
\boxed{
(\Delta K,\Delta\Sigma,\Delta\Gamma,\Delta H,\Delta M,\Delta N,\Delta E,\mathbf c_{\mathcal T}).
}
$$

否則我們只知道「變容易了」，不知道為什麼。

## 13.2 Internal vs imported transition

暫定區分：

- **internal transition**：主要由 $A,\Sigma,\Gamma$ 的合法內部學習／重構造成；
- **imported transition**：主要由外部 $K,M,N,E$ 注入造成；
- **carrier transition**：主要由 $H$ 改變造成；
- **mixed transition**：多項共同作用。

這些不是價值階級，只是因果記帳分類。

---

# 14. 九個反例：什麼不算合法的 Cognitive-P 轉換

## Counterexample 1：答案注入

原狀態不知道 witness $w$。

新狀態直接設定：

$$
K'=K\cup\{w\}.
$$

online completion 當然可能變成 $O(1)$ lookup。

這是一個真實的 state change，但若研究問題是「智能體自行發現能力是否提升」，則必須計入 $w$ 的 acquisition provenance。否則只是：

$$
\text{answer supplied}
\neq
\text{answer discovered}.
$$

---

## Counterexample 2：免費 oracle

允許：

$$
\mathsf{Ask}(x)\to\text{correct answer}
$$

且成本設為零。

則任何問題都可能顯得 trivial。這不證明智能體 tractability 提升，只證明契約加入了高資訊 oracle。

---

## Counterexample 3：改題式 bypass

原任務：找到最短路徑。

新任務：輸出任意路徑。

即使後者極易，也不構成：

$$
NP_{\mathrm{cog}}\to P_{\mathrm{cog}},
$$

因為 $\mathfrak T$ 已改變。

---

## Counterexample 4：巨大 lookup table

先離線枚舉所有 $n$-bit inputs：

$$
\mathbf c_{\mathrm{pre}}\sim2^n,
$$

之後 online query：

$$
\mathbf c_{\mathrm{on}}\sim O(1).
$$

若研究 online response，這是合法的 $\Sigma$ / memory advantage；若研究 one-shot total cognition，不能刪掉 $2^n$ 預計算。

---

## Counterexample 5：資源座標偷換

智能體 A 使用：

$$
B_T=1\text{ s},
\quad
B_M=1\text{ TB},
$$

智能體 B 使用：

$$
B_T=1\text{ hour},
\quad
B_M=1\text{ MB}.
$$

沒有額外 scalar utility contract 時，兩者不可直接說「誰比較有資源」。

---

## Counterexample 6：instance-specific advice

對每個 instance $x$，附上：

$$
a_x=\text{optimal solution of }x.
$$

則每題都變容易，但這測到的是 advice channel，不是 uniform problem-solving capacity。

---

## Counterexample 7：幸運猜測

一個 agent 隨機猜一次，剛好命中答案。

若成功可靠度要求：

$$
1-\delta_C=0.99,
$$

而猜中率只有 $10^{-6}$，則它不是 cognitive-P-like policy。

一次成功 realization 不等於可靠策略存在。

---

## Counterexample 8：驗證等於自我宣告

若 agent 可以：

$$
\mathsf{Certify}(y)
:=
\text{``I say }y\text{ is correct.''}
$$

則 certification 失去獨立意義。

因此 $\mathsf{Cert}$ 必須由任務契約或外部審核規則定義，不能由被評估 agent 單方面降低標準。

---

## Counterexample 9：benchmark leakage

若 hidden evaluation data 被併入 $K$，則測試已不再評估原本 discovery ability。

因此任何 benchmark 都必須區分：

$$
K_{\mathrm{train}},
K_{\mathrm{public}},
K_{\mathrm{hidden}},
K_{\mathrm{post-reveal}}.
$$

這與 SDPE-BEB 的 public descriptor / hidden completion / post-session reveal 分離直接相容。

---

# 15. Agent-relative 不代表 ontology-relative

本文的 classification 是：

$$
\boxed{
\text{task--agent--budget relation}.
}
$$

它不是：

$$
\boxed{
\text{being rank}.
}
$$

即使：

$$
\rho_C(x\mid A)\ll\rho_C(x\mid B)
$$

對大量任務成立，也只能支持：

$$
A\text{ 在這些任務契約上較 tractable},
$$

不能推出：

$$
\operatorname{Dignity}(A)
>
\operatorname{Dignity}(B),
$$

更不能推出：

$$
A=\text{ultimate being}.
$$

這是 Paper 00 的 normative separation；本文只保持邊界，不在此建立規範倫理 theorem。

---

# 16. 與 bounded optimality / resource rationality 的關係

既有 bounded optimality 研究已指出：一個 agent 的 optimality 應相對於其 computational device 與 environment，而非假設無限計算能力。metareasoning 則研究 agent 應如何選擇「值得做的 computation」。resource-rational analysis 進一步以抽象 computational architecture 中的 elementary operations 與 costs，推導有限資源下的合理策略。

本文接受這些研究的核心精神，但做三個不同擴張。

第一，本文的研究單位不是 expected utility 最大化本身，而是：

$$
\boxed{
\text{task completion / verification tractability relation}.
}
$$

第二，本文將 representation、knowledge、external tools、memory compilation、multi-agent network 與 certification authority 顯式加入 $\Xi$。

第三，本文要求所有 cognitive-regime transition 保留 task semantics 並記帳 imported information / preprocessing；因此「換 representation」只有在語義保持且 overhead 被計入後才能宣稱為 tractability gain。

近年的 resource-rational representation 研究也顯示，有限認知資源下，智能體可能主動簡化 task representation，而不是把表示視為固定背景。這為 UCPNP 的 $\Gamma$ 研究提供重要外部鄰域，但 UCPNP 不預設任何特定心理模型或人類最優性假說。

---

# 17. 與 SDPE-BEB 的可操作對接

SDPE-BEB 可以成為本文定義的第一個 exact micro-model。

例如對 observation budget $Q$：

$$
\mathbf B=(B_Q=Q,\ldots).
$$

safe-certification policy set 對應 $\Pi_C$；候選 closure / counterexample 的驗證規則對應 $\Pi_V$ 與 $\mathsf{Cert}$。

其 exact Bellman frontier 可以產生：

$$
\rho_C^{\star}
$$

或等價 success frontier 的 exact finite certificate。

更重要的是 SDPE-BEB 已經展示：

$$
\text{Truth}
\neq
\text{Evidence}
\neq
\text{Certification Authority}.
$$

因此它非常適合測試：

1. 候選已知但 certificate 不足；
2. observation 增加導致 regime transition；
3. posterior state 增加 $\Sigma$；
4. quotient / dual representation 形成 $\Gamma$ 型 transition；
5. proof-carrying computation 把 discovery cost 與 verification cost 分離。

Paper 05 將專門完成這個映射；本文只建立接口。

---

# 18. 實驗輸出格式

任何聲稱某任務發生 cognitive tractability transition 的實驗，最低應輸出：

```text
Task contract:
  task_id
  semantic_goal
  verification_contract
  certification_contract

Agent state:
  A, K, Sigma, Gamma, H, M, N, E

Resource contract:
  dimensions
  budget vector
  risk statistic
  success threshold

Before:
  rho_C interval
  rho_V interval
  evidence level

Transition:
  Delta K, Sigma, Gamma, H, M, N, E
  transition cost
  imported/precomputed structure

After:
  rho_C interval
  rho_V interval
  evidence level

Classification:
  proven / empirical / unresolved
  P_cog-like / NP_cog-like / V-hard / unresolved
```

沒有這些資訊的「這個 AI 已經把 NP 問題變成 P」之類語句，在 UCPNP 正典中視為不合格 claim。

---

# 19. 後續可證明問題

本文留下以下正式研究前線。

## C19.1 Tractability transition decomposition

是否存在一組可辨識條件，使：

$$
\Delta\rho_C
\approx
f(
\Delta\Sigma,
\Delta\Gamma,
\Delta H,
\Delta M,
\Delta N,
\Delta E
)
$$

具有跨任務穩定性？

目前為 **C/E**，不是 theorem。

## C19.2 Representation gain lower bound

在語義保持且所有 translation / preprocessing 成本記帳後，是否存在問題族使：

$$
\Gamma\text{-type representation change}
$$

仍能產生不可由純 $H$ scaling 模擬的嚴格 tractability gain？

SDPE-BEB 提供有限候選，但尚不能外推為一般定理。

## C19.3 Agent equivalence quotient

是否可定義：

$$
\Xi_1\sim_x\Xi_2
$$

當兩者對任務族 $x$ 的 admissible policy-cost kernel 相同，並進一步對 agent space 做 quotient？

若成立，UCPNP 可以把「載體名稱」從大量數學分析中消去。

## C19.4 Historical tractability frontier

對歷史任務 $x$，能否估計：

$$
Y_{\mathrm{discover}},
Y_{\mathrm{execute}},
Y_{\mathrm{practical}},
Y_{\mathrm{commodity}}
$$

且在 held-out 歷史問題上優於純 FLOPS / memory trend baseline？

這將由 Paper 04 作 empirical test。

---

# 20. 本文的失敗條件

Paper 01 的形式化應被修正，如果發現：

1. normalized bottleneck ratio 對多資源實驗產生系統性錯判；
2. completion / verification 前沿無法在第二類 benchmark 操作化；
3. task semantic contract 無法處理生成式、創造式或 bypass 任務；
4. precomputation accounting 使歷史比較不可實作；
5. proven / empirical / unresolved 三分法仍不足以阻止不存在量詞被誤用；
6. $P_{\mathrm{cog}}$ / $NP_{\mathrm{cog}}$ 名稱持續造成 classical P/NP 語義混淆。

若第 6 點在實際交流中反覆發生，可以保留理論內容但把 operational labels 改名為：

$$
\mathsf{CTract}
\quad\text{and}\quad
\mathsf{CGap}.
$$

名稱不是理論不可修改的部分；非同一性與成本記帳才是。

---

# 21. 核心結論

本文把「智能體相對可解性」從直覺收斂為一個受約束的操作關係。

最核心的定義為：

$$
\boxed{
\rho_C(x\mid\Xi,\mathbf B)
=
\inf_{\pi\in\Pi_C}
\max_i
\frac{c_i(\pi,x)}{B_i},
}
$$

$$
\boxed{
\rho_V(x\mid\Xi,\mathbf B)
=
\inf_{\nu\in\Pi_V}
\max_i
\frac{c_i(\nu,x)}{B_i}.
}
$$

從而：

$$
\boxed{
P_{\mathrm{cog}}\text{-like}
\iff
\rho_C\le1,
}
$$

以及：

$$
\boxed{
NP_{\mathrm{cog}}\text{-like}
\iff
\rho_V\le1<\rho_C.
}
$$

但任何 regime claim 都必須同時指定：

$$
\boxed{
(\mathfrak T,\Xi,\mathbf B,\delta,\Pi,\mathsf{Cost},\text{evidence level}).
}
$$

因此：

$$
\boxed{
\text{Agent-relative}
\neq
\text{arbitrary-relative}.
}
$$

智能體相對可解性不是「每個人感覺不同所以一切都相對」，而是：**同一任務在不同操作狀態與資源契約下，具有可比較、可記帳、可證明或可實驗估計的 tractability frontier。**

這使 UCPNP 能在不僭越 classical complexity theory 的前提下，正式研究：

$$
\text{human}
\leftrightarrow
\text{AI}
\leftrightarrow
\text{multi-agent}
\leftrightarrow
\text{posthuman}
\leftrightarrow
\text{future ASI}
$$

在不同歷史、知識與 representation 條件下，「什麼時候一個原本不知道如何取得的成果，變成可以穩定完成與認證的成果」。

---

# 參考文獻

## 外部研究定位

1. Russell, S., & Wefald, E. (1991). *Principles of Metareasoning*. Artificial Intelligence, 49(1–3), 361–395. DOI: 10.1016/0004-3702(91)90015-C.
2. Russell, S. J., & Subramanian, D. (1995). *Provably Bounded-Optimal Agents*. Journal of Artificial Intelligence Research, 2, 575–609. DOI: 10.1613/JAIR.133.
3. Griffiths, T. L., Lieder, F., & Goodman, N. D. (2015). *Rational Use of Cognitive Resources: Levels of Analysis Between the Computational and the Algorithmic*. Topics in Cognitive Science, 7(2), 217–229. DOI: 10.1111/tops.12142.
4. Lieder, F., & Griffiths, T. L. (2020). *Resource-rational analysis: Understanding human cognition as the optimal use of limited computational resources*. Behavioral and Brain Sciences, 43, e1. DOI: 10.1017/S0140525X1900061X.
5. Correa, C. G., Ho, M. K., Callaway, F., & Griffiths, T. L. (2020). *Resource-rational Task Decomposition to Minimize Planning Costs*. arXiv:2007.13862.
6. Ho, M. K., Abel, D., Correa, C. G., Littman, M. L., Cohen, J. D., & Griffiths, T. L. (2022). *People construct simplified mental representations to plan*. Nature, 606, 129–136. DOI: 10.1038/s41586-022-04743-9.

## Neo.K / UCPNP internal lineage

1. Neo.K. *The Neo.K Ultimate Cognitive P/NP Problem: Canonical Definition, Scope, and Research Program*. Paper 00, v0.1.
2. Neo.K. 《動態速率理論與 P vs. NP 問題的結構連續模型 2.0：一種認知與數學整合框架（完整修正版）》.
3. Neo.K. 《P vs. NP 問題的動態可解性理論 2.5：計算機歷史的實證框架》.
4. Neo.K. 《動態速率理論 2.9：認知與計算的解耦——P vs. NP 問題的終極動力學解構》.
5. Neo.K. 《時序—認知統一框架：P vs NP 與數論基礎的深層同構》.
6. Neo.K with Aletheia. 《超越 P/NP 二分：解空間幾何計算論》系列.
7. Neo.K with Aletheia. 《從路徑覆蓋到行星智能：記憶編譯型計算存在論》.
8. SDPE-BEB v0.1–v1.0 research lineage.

---

# Migration note from Paper 00

Paper 00 對 $P_{\mathrm{cog}}$、$NP_{\mathrm{cog}}$ 的定義為概念版。Paper 01 v0.1 做以下 refinement：

1. 加入固定任務語義契約 $\mathfrak T$；
2. 加入 admissible policy contract；
3. 將「成本在 budget 內」形式化成 Pareto cost frontier；
4. 新增 normalized bottleneck ratio $\rho_C,\rho_V$；
5. 將 non-existence claim 拆成 proven / empirical / unresolved；
6. 新增 precomputation / oracle / advice accounting；
7. 新增 family-level uniformity；
8. 新增 tractability margin 與 transition cost。

這些 refinement 不改變 Paper 00 的核心語義，而是收緊其可操作條件。
