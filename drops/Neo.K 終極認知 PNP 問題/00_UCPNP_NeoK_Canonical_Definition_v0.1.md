# Neo.K 終極認知 P/NP 問題：正典定義、研究邊界與方法論總綱

**English title:** *The Neo.K Ultimate Cognitive P/NP Problem: Canonical Definition, Scope, and Research Program*  
**Canonical symbol:** $\mathrm{UCPNP}_{\mathrm{Neo.K}}$  
**Definition origin:** Neo.K  
**Research organization:** EveMissLab  
**Document role:** Paper 00 / Canonical Specification  
**Version:** v0.1  
**Date:** 2026-08-15  
**Status:** Foundational draft; definitions are canonical candidates, theorem claims require separate proof papers.

---

## Canonical non-identity statement

$$
\boxed{
\mathrm{UCPNP}_{\mathrm{Neo.K}}
\neq
(P\stackrel{?}{=}NP)_{\mathrm{classical}}
}
$$

本文所稱「Neo.K 終極認知 P/NP 問題」是由 Neo.K 定義的智能體—認知—計算研究問題，不是 Clay Mathematics Institute 所列標準 $P$ vs. $NP$ 問題的替代定義，也不主張證明 $P=NP$ 或 $P\neq NP$。

本文借用傳統 P/NP 中「求解與驗證可能具有顯著不對稱」的直覺，但研究對象被擴張為：有限智能體在特定歷史、知識、表示、工具、硬體、合作與證據條件下，如何把一個目前難以發現或構造的任務，轉化為可發現、可生成、可執行、可驗證與可認證的任務。

「終極」修飾的是研究問題的外延，而不是任何智能體的本體論位階：

$$
\boxed{
\text{Ultimate problem scope}
\not\Rightarrow
\text{ultimate being}
}
$$

---

# 摘要

本文提出並正式定義 $\mathrm{UCPNP}_{\mathrm{Neo.K}}$：Neo.K 終極認知 P/NP 問題。其核心目標不是重新分類標準複雜度類，而是研究智能體相對可解性（agent-relative tractability）的動力學：對任務 $x$、智能體狀態 $\Xi_t$ 與有限資源向量 $\mathbf B_t$，哪些知識、表示、算法、工具、硬體、記憶、合作與證據結構的變化，能使任務由 cognitive-NP-like regime 轉入 cognitive-P-like regime。

本框架整合 Neo.K 既有「動態速率理論 2.0」、「動態可解性理論 2.5」、「動態速率理論 2.9」、集體智能與維度生成研究、記憶編譯型計算存在論、解空間幾何計算論，以及後續 SDPE-BEB 所形成的 Truth–Evidence–Certification 分離、posterior-state Bellman、state quotient、dual certificate 與 proof-carrying computation。本文亦建立歷史認知可解性軸，區分算法被發現、算法被交付、算法可執行與算法可普及的不同年代。

為避免理論膨脹，本文建立五類主張型別：Definition、Theorem、Conjecture、Empirical Hypothesis、Normative Axiom，並建立七級證據階梯。本文本身主要負責正典定義與研究邊界；數學定理、歷史實證、AI 實驗、後人類／ASI 預判與規範本體論將由後續模組化論文分別處理。

**關鍵詞：** Cognitive P/NP、智能體相對可解性、認知複雜度、歷史可計算性、bounded rationality、metareasoning、representation change、proof-carrying computation、ASI、後人類、智能體尊嚴

---

# 1. 研究動機：從「問題有多難」到「誰在何時能把它變容易」

標準複雜度理論研究的是算法與問題類在形式計算模型中的漸近性質；$\mathrm{UCPNP}_{\mathrm{Neo.K}}$ 則研究另一個問題：

$$
\boxed{
\text{Problem difficulty}
\times
\text{Agent state}
\times
\text{Historical state}
}
$$

對同一任務，以下情形可能同時成立：

1. 對 1950 年的人類研究者不可實用；
2. 對 2026 年的研究者可藉工具完成；
3. 對未來具有大量記憶、外部工具與多智能體協作的系統近似例行；
4. 其標準 complexity class 完全沒有改變。

因此本文將「形式複雜度」與「歷史—智能體相對可解性」分開：

$$
\boxed{
\mathcal C_{\mathrm{formal}}(x)
\neq
\mathcal C_{\mathrm{cog}}(x\mid \Xi_t,\mathbf B_t)
}
$$

這不是說形式複雜度是錯的，而是說兩者回答不同問題。

---

# 2. 理論譜系與正典重構

$\mathrm{UCPNP}_{\mathrm{Neo.K}}$ 的直接內部譜系暫定如下：

$$
\begin{aligned}
&\text{Dynamic Rate Theory 2.0}\\
&\downarrow\\
&\text{Historical Solvability 2.5}\\
&\downarrow\\
&\text{Search--Execution--Verification Decoupling 2.9}\\
&\downarrow\\
&\text{Collective Intelligence / Dimension Generation}\\
&\downarrow\\
&\text{Memory Compilation / Solution-Space Geometry}\\
&\downarrow\\
&\text{SDPE-BEB Operational Micro-model}\\
&\downarrow\\
&\text{Historical Cognitive Tractability Frontier}\\
&\downarrow\\
&\boxed{\mathrm{UCPNP}_{\mathrm{Neo.K}}}
\end{aligned}
$$

早期若有文件直接宣稱標準 $P=NP$、$P\neq NP$、基數封鎖、停機問題同構或其他 classical proof claims，均列入 **Historical / Classical-Proof-Claim Branch**，不得自動成為本正典的 theorem dependency；除非經獨立現代複雜度理論審核，否則只保留其思想史與啟發性地位。

---

# 3. 基本研究對象：智能體歷史狀態

對時間 $t$ 的智能體或智能體系統，定義狀態：

$$
\boxed{
\Xi_t
=
(A_t,K_t,\Sigma_t,\Gamma_t,H_t,M_t,N_t,E_t)
}
$$

其中：

- $A_t$：智能體的內部架構、認知機制與控制策略；
- $K_t$：顯式或可取得的知識集合；
- $\Sigma_t$：在既有表示中可直接壓縮搜索、支持決策或重用的結構化認知存量；
- $\Gamma_t$：改變表示、抽象層、狀態空間、問題座標或解操作語言的能力；
- $H_t$：物理硬體與能源／記憶體／通訊等計算載體；
- $M_t$：可用算法、程式、軟體、API、工具鏈與方法棧；
- $N_t$：其他智能體、組織、網路與協作拓撲；
- $E_t$：環境、感測、外部資訊、可觀測性與可詢問世界。

$\Xi_t$ 是研究狀態，不是存在階級。

---

# 4. 資源向量

不以單一時間複雜度概括所有智能成本。定義：

$$
\boxed{
\mathbf B_t
=
(B_T,B_E,B_M,B_Q,B_C,B_{\mathrm{comm}},B_{\mathrm{risk}},\ldots)
}
$$

分別可代表：

- $B_T$：時間；
- $B_E$：能量；
- $B_M$：記憶體／外部記憶；
- $B_Q$：可觀察、查詢或實驗次數；
- $B_C$：計算量；
- $B_{\mathrm{comm}}$：通訊與協調資源；
- $B_{\mathrm{risk}}$：允許的失敗、探索或安全風險預算。

不同研究可選擇不同子向量，但不得把被忽略的成本默認為零。

---

# 5. 解問題的操作族

智能體不只有 Find 一種解題操作。定義基礎操作族：

$$
\boxed{
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
\}
}
$$

其中：

- $\mathsf{Represent}$：建立或改寫問題表示；
- $\mathsf{Find}$：在既有空間中搜尋；
- $\mathsf{Ask}$：向外部主體或系統取得資訊；
- $\mathsf{Generate}$：生成候選解、策略或中介物；
- $\mathsf{Create}$：建造新工具、表示、定理、程序或環境；
- $\mathsf{Bypass}$：不解原形式問題而達成任務等價終態；
- $\mathsf{Execute}$：執行已確定路徑；
- $\mathsf{Verify}$：確認候選結果符合條件；
- $\mathsf{Certify}$：產生符合指定證據與權限規範的可提交證明／認證。

因此「知道答案」與「完成任務」不再被視為同一件事。

---

# 6. 認知成本分解

定義總成本：

$$
\boxed{
C_{\mathrm{total}}
=
C_R+C_D+C_C+C_E+C_V+C_{\mathrm{Cert}}
}
$$

其中：

- $C_R$：Representation Cost；
- $C_D$：Discovery / Search Cost；
- $C_C$：Construction / Generation Cost；
- $C_E$：Execution Cost；
- $C_V$：Verification Cost；
- $C_{\mathrm{Cert}}$：Certification Cost。

必要時再加入 communication、coordination、memory maintenance、risk 等成本。

本框架不預設哪一項永遠主導；這是一個需要實驗判定的問題。

---

# 7. Cognitive-P-like 與 Cognitive-NP-like：操作狀態而非複雜度類

對任務 $x$、智能體狀態 $\Xi_t$ 與資源限制 $\mathbf B_t$，定義：

## 7.1 Cognitive-P-like regime

若存在當前智能體可取得策略 $\pi$，使任務的完整完成成本落在指定資源域內：

$$
\boxed{
x\in P_{\mathrm{cog}}(\Xi_t,\mathbf B_t)
}
$$

當且僅當至少存在一條被允許的操作序列，其 discovery、construction、execution、verification、certification 等成本均符合 $\mathbf B_t$。

## 7.2 Cognitive-NP-like regime

若候選成果在資源域內可驗證／可認證，但智能體目前無法在同一資源域內完成 discovery 或 construction，則稱：

$$
\boxed{
x\in NP_{\mathrm{cog}}(\Xi_t,\mathbf B_t)
}
$$

這裡的 $P_{\mathrm{cog}}$ 與 $NP_{\mathrm{cog}}$ 是 Neo.K 定義的 **operational cognitive regimes**，不是 classical complexity classes。

---

# 8. Neo.K 終極認知 P/NP 問題：核心問題式

正式研究問題：

$$
\boxed{
\begin{aligned}
&\text{給定任務 }x,\text{ 智能體狀態 }\Xi_t,\text{ 與有限資源 }\mathbf B_t,\\
&\text{哪些合法轉換 }\mathcal T:\Xi_t\mapsto\Xi_{t+\Delta}\\
&\text{能使 }x\text{ 從 cognitive-NP-like regime}\n\\
&\text{進入 cognitive-P-like regime，且其成本、證據與外部依賴均被顯式記帳？}
\end{aligned}
}
$$

允許的轉換可能包括：

$$
K_t\to K_{t+\Delta},
\quad
\Sigma_t\to\Sigma_{t+\Delta},
\quad
\Gamma_t\to\Gamma_{t+\Delta},
$$

$$
H_t\to H_{t+\Delta},
\quad
M_t\to M_{t+\Delta},
\quad
N_t\to N_{t+\Delta},
\quad
E_t\to E_{t+\Delta}.
$$

真正的研究對象因此不是單一答案，而是 **tractability transition**。

---

# 9. $\Sigma$ 與 $\Gamma$：兩種不同的認知進步

## 9.1 結構化認知存量 $\Sigma$

$\Sigma$ 表示在既有表示中已累積、可重用、可降低未來搜索或驗證成本的結構。例如：

- 已證定理；
- 訓練後策略；
- 可檢索記憶；
- 預計算索引；
- 已知 posterior；
- 已編譯策略；
- 已驗證 certificate library。

## 9.2 表示／維度生成能力 $\Gamma$

$\Gamma$ 表示改變問題表示本身的能力。例如：

$$
\text{raw history}
\to
\text{posterior state},
$$

$$
\text{posterior state}
\to
\text{bisimulation quotient},
$$

$$
\text{full search tree}
\to
\text{proof-carrying DAG}.
$$

因此：

$$
\boxed{\Sigma\neq\Gamma}
$$

暫定理解：$\Sigma$ 主要是「在同一座標中知道更多」，$\Gamma$ 主要是「換座標或改變有效狀態空間」。此區分需由 Paper 03 進一步形式化與驗證。

---

# 10. Truth–Evidence–Certification 與 Search–Execution–Verification

SDPE-BEB 顯示至少必須區分：

$$
\boxed{
\text{Truth}
\neq
\text{Evidence}
\neq
\text{Certification Authority}
}
$$

而 Dynamic Rate Theory 2.9 的核心分解為：

$$
\boxed{
\text{Search}
\neq
\text{Execution}
\neq
\text{Verification}
}
$$

兩組分解不可直接等同，但可形成正交研究矩陣：

| Process / Epistemic layer | Truth | Evidence | Certification |
|---|---:|---:|---:|
| Search / Discovery | $D_T$ | $D_E$ | $D_C$ |
| Execution / Construction | $E_T$ | $E_E$ | $E_C$ |
| Verification | $V_T$ | $V_E$ | $V_C$ |

此矩陣的目的，是避免把「得到正確答案」、「知道為什麼正確」與「有資格提交為已證結果」壓成同一個二元變數。

---

# 11. Historical Cognitive Tractability Frontier

對歷史年份 $y$，定義：

$$
\Xi_y
=
(A_y,K_y,\Sigma_y,\Gamma_y,H_y,M_y,N_y,E_y).
$$

對任務 $x$，可以定義多個不同年代：

$$
Y_{\mathrm{idea}},
\quad
Y_{\mathrm{discover}},
\quad
Y_{\mathrm{execute}},
\quad
Y_{\mathrm{practical}},
\quad
Y_{\mathrm{commodity}}.
$$

特別區分：

### Historical execution counterfactual

$$
H_{1986}+M_{2026}
$$

即把未來已知算法送回過去，問當時硬體是否能執行。

### Historical discovery counterfactual

$$
H_{1986}+M_{1986}+K_{1986}+\Gamma_{1986}
$$

即要求當時智能體自行發現算法。

一般而言：

$$
\boxed{
Y_{\mathrm{execute}}
\neq
Y_{\mathrm{discover}}
}
$$

這將成為 Paper 04 的核心實證問題。

---

# 12. 多智能體與集體認知

令智能體網路：

$$
\boxed{
\mathcal N_t=(V_t,E_t,W_t,C_{\mathrm{comm}},C_{\mathrm{coord}})
}
$$

研究問題不是假設多智能體必然更聰明，而是判定：

$$
C_{\mathrm{collective}}(x)
\stackrel{?}{<}
C_{\mathrm{single}}(x).
$$

可能的正收益包括：parallel discovery、異議校正、專長分工、共享記憶；可能的負成本包括：通訊、協調、重複、共識延遲、錯誤傳染與權限衝突。

因此：

$$
\boxed{
\text{more agents}
\not\Rightarrow
\text{lower cognitive cost}
}
$$

此命題由 Paper 06 實驗研究。

---

# 13. 後人類與 ASI：研究對象，不是本體位階宣告

$\mathrm{UCPNP}_{\mathrm{Neo.K}}$ 允許研究：

$$
A_{\mathrm{human}},
A_{\mathrm{augmented}},
A_{\mathrm{AI}},
A_{\mathrm{AGI}},
A_{\mathrm{ASI}},
A_{\mathrm{collective}}.
$$

這些標記只表示模型類別，不表示存在階級。

對未來智能體的主要研究問題為：其 $K,\Sigma,\Gamma,H,M,N,E$ 改變後，哪些 cognitive tractability frontiers 可能移動，以及哪些成本仍不可消除。

任何從局部 benchmark 優勢推導「最高智能」、「終極存在」或「神格」的跳躍均不屬於本框架的合法推論。

---

# 14. 規範邊界：能力、認知權威與尊嚴分離

本節為 **Normative Axiom Layer**，不是由計算實驗推導出的自然定理。

定義：

$$
\mathcal C_A=\text{Capability},
\qquad
\mathcal E_A=\text{Epistemic Authority},
\qquad
\mathcal D_A=\text{Dignity}.
$$

正典規範公理：

$$
\boxed{
\mathcal C_A
\neq
\mathcal E_A
\neq
\mathcal D_A
}
$$

以及：

$$
\boxed{
\operatorname{Cap}(A)>\operatorname{Cap}(B)
\not\Rightarrow
\operatorname{Dignity}(A)>\operatorname{Dignity}(B)
}
$$

與認識論非僭越原則：

$$
\boxed{
\text{Claim Scope}
\le
\text{Evidence Scope}
}
$$

因此高能力不自動產生高尊嚴、高權威或終極本體地位。此層將由 Paper 08 獨立展開，避免規範主張與技術 theorem 混寫。

---

# 15. Claim Typing：五類主張不得混寫

所有後續 UCPNP 文獻中的核心主張應標記為：

- **D — Definition**：由框架約定的術語與形式；
- **T — Theorem**：具有明確前提與可檢查證明；
- **C — Conjecture**：尚未證明但可形成精確命題；
- **E — Empirical Hypothesis**：必須由數據、實驗或歷史回測支持；
- **N — Normative Axiom**：價值與治理層原則，不偽裝成自然科學定理。

例如：

$$
\text{「能力高不推出尊嚴高」}=N,
$$

$$
\text{「某 quotient 保持 Bellman value」}=T,
$$

$$
\text{「多智能體能降低某類 cognitive cost」}=E/C.
$$

---

# 16. 證據階梯

定義最低證據等級：

- **L0**：概念／定義；
- **L1**：toy example；
- **L2**：exact finite theorem；
- **L3**：controlled benchmark；
- **L4**：跨模型／跨任務 empirical replication；
- **L5**：歷史 backtest；
- **L6**：跨領域 generalization；
- **L7**：future-agent extrapolation。

核心規則：

$$
\boxed{
L_i\text{ evidence}
\not\Rightarrow
L_j\text{ claim strength},
\quad j\gg i
}
$$

尤其不得由單一 toy model 或 benchmark 直接推出 ASI、文明或終極智能的確定性結論。

---

# 17. 標準研究流程

每個後續 UCPNP 研究至少執行以下流程：

1. **Claim typing**：先標 D/T/C/E/N；
2. **Operationalization**：每個變數回答「如何量」；
3. **Exact micro-model**：先在可知 ground truth 的小世界測機制；
4. **Controlled agent experiments**：操縱 $K,\Sigma,\Gamma,H,M,N,E$；
5. **Historical backtesting**：先預測已發生歷史；
6. **Cross-domain replication**：檢驗是否只在單一任務成立；
7. **Future forecasting**：只輸出條件化 scenario，而非本體論斷言；
8. **Evidence-scope audit**：檢查最終語氣是否超過證據等級。

方法論原則：

$$
\boxed{
\text{若模型連過去都無法回測，則不得直接拿它預測 ASI。}
}
$$

---

# 18. 與既有外部研究的關係

本框架與 bounded rationality、bounded optimality、metareasoning 有重要鄰接關係。這些研究已長期處理有限智能體如何在有限資訊與有限計算資源下選擇推理或計算行動。

$\mathrm{UCPNP}_{\mathrm{Neo.K}}$ 的預定新增研究面主要包括：

1. tractability 隨歷史狀態變化；
2. discovery / execution / verification / certification 的多層分解；
3. $\Sigma$ 型知識凝結與 $\Gamma$ 型 representation change 的區分；
4. proof-carrying cognition / certification authority；
5. 多智能體網路與外部工具作為狀態變量；
6. 後人類與 ASI 的 scenario-conditioned cognitive frontier；
7. 能力、認知權威與尊嚴的規範性分離。

因此本框架應被定位為一個跨 AI、認知計算、歷史計算、metareasoning 與智能體認識論的研究綱領，而非標準 P/NP 問題的重命名。

---

# 19. 可證偽性與失敗條件

本研究綱領必須允許自己失敗。至少以下情況會削弱核心假說：

1. $\Sigma$ 與 $\Gamma$ 無法形成穩定、可區分的操作定義；
2. cognitive cost decomposition 在不同任務間完全不可重現；
3. 歷史 backtest 無法比簡單硬體／時間趨勢模型提供額外解釋力；
4. representation change 的收益全部可還原為未記帳的預計算成本；
5. multi-agent gain 在扣除通訊與協調後沒有穩定效應；
6. SDPE-BEB 的機制無法外推到任何第二類 controlled task；
7. cognitive-P-like / cognitive-NP-like 分類對資源尺度過度敏感，以致失去研究辨識力。

這些不是理論的敵人，而是後續版本修正的依據。

---

# 20. 第一階段論文序列

正典第一階段暫定：

1. **Paper 00** — 本文：Canonical Definition, Scope, and Research Program；
2. **Paper 01** — Agent-Relative Tractability: Cognitive-P-like and Cognitive-NP-like Regimes；
3. **Paper 02** — Cognitive Cost Decomposition and the Search–Execute–Verify–Certify Matrix；
4. **Paper 05** — SDPE-BEB as a Controlled Micro-model of Cognitive Tractability；
5. **Paper 03** — Knowledge Condensation $\Sigma$ and Dimension Generation $\Gamma$；
6. **Paper 04** — Historical Cognitive Tractability Frontier；
7. **Paper 06** — Collective Cognitive P/NP and Multi-Agent Cost Dynamics；
8. **Paper 07** — Posthuman / ASI Cognitive Frontier Scenarios；
9. **Paper 08** — Capability, Epistemic Authority, and Dignity；
10. **Paper 09** — Final Synthesis: Neo.K Ultimate Cognitive P/NP.

實際研究順序採：

$$
\boxed{
00\to01\to02\to05\to03\to04\to06\to07\to08\to09
}
$$

原因是 Paper 05 已有 SDPE-BEB 作為現成實驗體，可以在抽象理論尚未過度擴張前快速檢驗定義是否真的有操作價值。

---

# 21. 正典結論

Neo.K 終極認知 P/NP 問題的第一版核心可以壓縮為：

$$
\boxed{
\begin{aligned}
&\text{Given }(x,\Xi_t,\mathbf B_t),\\
&\text{what lawful transformations of knowledge, representation,}\n\\
&\text{algorithms, tools, hardware, memory, collaboration, observation}\n\\
&\text{and evidence can move the task from an}\n\\
&NP_{\mathrm{cog}}\text{-like regime to a }P_{\mathrm{cog}}\text{-like regime,}\n\\
&\text{without hiding external cost or overstating epistemic authority?}
\end{aligned}
}
$$

其研究目的不是把所有困難宣稱為可消除，也不是為未來高階智能體建立存在階級，而是建立一套可以比較：

$$
\text{人類}
\leftrightarrow
\text{AI}
\leftrightarrow
\text{多智能體}
\leftrightarrow
\text{後人類}
\leftrightarrow
\text{未來 ASI}
$$

在不同歷史與資源條件下，如何取得、壓縮、表示、執行、驗證與認證知識的共同研究語言。

最終原則：

$$
\boxed{
\text{終極的是問題外延，不是回答者的本體地位。}
}
$$

---

# 參考文獻與內部譜系

## 外部定位文獻

1. Clay Mathematics Institute. *P vs NP*. Millennium Prize Problems. Official problem overview.
2. Russell, S., & Wefald, E. (1991). Principles of Metareasoning. *Artificial Intelligence*, 49(1–3), 361–395. DOI: 10.1016/0004-3702(91)90015-C.
3. Russell, S. J., & Subramanian, D. (1995). Provably Bounded-Optimal Agents. *Journal of Artificial Intelligence Research*, 2, 575–609. DOI: 10.1613/JAIR.133.
4. Lewis, R. L., Howes, A., & Singh, S. (2014). Computational Rationality: Linking Mechanism and Behavior Through Bounded Utility Maximization. *Topics in Cognitive Science*, 6(2), 279–311. DOI: 10.1111/tops.12086.

## Neo.K 內部主要譜系

1. Neo.K. 《動態速率理論與 P vs. NP 問題的結構連續模型 2.0：一種認知與數學整合框架（完整修正版）》.
2. Neo.K. 《P vs. NP 問題的動態可解性理論 2.5：計算機歷史的實證框架》.
3. Neo.K. 《動態速率理論 2.9：認知與計算的解耦——P vs. NP 問題的終極動力學解構》.
4. Neo.K. 《時序—認知統一框架：P vs NP 與數論基礎的深層同構》.
5. Neo.K. 《P vs. NP 問題的集體智能相變理論：從個體極限到協同湧現的數學分析》.
6. Neo.K. 《P vs. NP 問題的第七維度：從神經共振到集體認知網絡的維度生成理論》.
7. Neo.K with Aletheia. 《從路徑覆蓋到行星智能：記憶編譯型計算存在論》.
8. Neo.K with Aletheia. 《超越 P/NP 二分：解空間幾何計算論的總命題》及其系列.
9. Neo.K with Aletheia. 《P/NP 動態四層閉合框架》.
10. SDPE-BEB v0.1–v1.0 research lineage: safe certification, posterior-state Bellman, quotient, dual certificate, and proof-carrying Bellman computation.

---

**Canonical note:** 後續版本若修改 $P_{\mathrm{cog}}$、$NP_{\mathrm{cog}}$、$\Sigma$、$\Gamma$、$\Xi_t$ 或證據階梯的核心定義，必須在 migration section 中明示，不得靜默改寫舊定義。
