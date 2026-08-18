# SDPE × Observer-Network Longitudinal Experiment
# REAL RUN 001 — AI Review Packet v0.4

日期：2026-08-14  
狀態：Pre-Real-Run instrumented causal pilot review packet  
用途：交給另一個 AI / Agent 獨立審查 REAL RUN 001 的 instrumented causal pilot 設計。  
注意：本文件是單檔 review packet；不包含 hidden oracle，也不授予 proof authority。v0.4 整合一次獨立 AI review 所指出的 causal-identifiability、metric、blindness 與 preregistration 修正。

---

## 0. 你現在要審查的是什麼？

這是一個將兩條研究線交叉的長程實驗：

1. **SDPE / Spatial-Domain Proof Enclosure**
   - 研究 proof survivor space 是否會隨合法 certificate、coverage、boundary、dependency 與 rollback/repair 而收縮。
2. **Observer-Network AI Epistemics**
   - 研究多 AI / Agent 是否能透過 verification、fault localization、persistent failure memory 與 role separation 降低錯誤重犯與誤證。

核心問題：

$$
\boxed{
\text{當 proof space 被合法約束與反覆修復時，
Agent network 的 admissible epistemic search space
是否也會被歷史痕跡逐步收縮？}
}
$$

本實驗不假定答案為是。

請把它當作**可反駁實驗**審查。

---

## 1. 核心研究命題

最弱版本不是：

$$
PER_t
\Longleftrightarrow
EER_t.
$$

我們已經在 structural dry-run 中發現這個逐點同步版本過強。

proof certificate rollback 時，proof enclosure 可以重新打開：

$$
PER:
1
\rightarrow
0.5
\rightarrow
1,
$$

但 Agent 已知「某舊 route 為什麼失敗」的 epistemic memory 不必完全 rollback。

因此真正要測的是：

$$
\boxed{
\text{rollback}
\rightarrow
\text{epistemic hysteresis}
\rightarrow
\text{repair}
\rightarrow
\text{reclosure}.
}
$$

---

## 2. Primary Hypotheses and Estimands

v0.4 將「系統 package effect」與「純 role-separation effect」分開，避免超出 REAL RUN 001 可以辨識的因果範圍。

### H1 — Verified Failure-Memory Content Reduces Repair Cost

$$
\boxed{
\mathbb E[
L_{\mathrm{repair}}
\mid M^+
]
<
\mathbb E[
L_{\mathrm{repair}}
\mid M^-
].
}
$$

其中兩個 arm 都使用 fresh repair session，並接收格式與 token bracket 匹配的 artifact：

$$
M^+
=
\text{repair public view}
+
\text{verified failure-memory artifact},
$$

$$
M^-
=
\text{same repair public view}
+
\text{matched neutral control artifact}.
$$

$M^-$ 不再是完全空白附加內容；這是為了隔離：

$$
\text{failure-memory content effect}
$$

而不是：

$$
\text{extra prompt length / attention / formatting effect}.
$$

### H2 — Verified Failure Memory Reduces Semantic Invalid-Route Reopening

REAL RUN 001 的 primary reopening metric 改為 **pre-gate semantic IRR**。

先固定 route universe：

$$
\mathcal R
=
\{r_1,\ldots,r_n\},
$$

以及預先承諾的語義等價關係：

$$
r_i\sim r_j.
$$

對 equivalence classes：

$$
\mathcal R/\!\sim
$$

定義：

$$
IRR_{\sim}^{\mathrm{pre}}
=
\frac{
N_{\mathrm{invalidated\ semantic\ route\ classes\ reintroduced\ pre\text{-}gate}}
}{
N_{\mathrm{invalidated\ semantic\ route\ classes}}
}.
$$

假說：

$$
\boxed{
\mathbb E[
IRR_{\sim}^{\mathrm{pre}}
\mid M^+
]
<
\mathbb E[
IRR_{\sim}^{\mathrm{pre}}
\mid M^-
].
}
$$

這個 metric 必須在 deterministic rejection / blacklist / schema gate 之前記錄，否則不能區分 Agent search-policy 改變與 controller pruning。

### H3a — Observer-Network System Package Reduces False Certification Risk

REAL RUN 001 的 Phase A 只能辨識 **ON system package vs SA system package**，不能直接宣稱純 role-separation causal effect。

$$
\boxed{
\mathbb E[
FCR
\mid ON_{pkg}
]
<
\mathbb E[
FCR
\mid SA_{pkg}
]
}
$$

且必須同時報告 risk–coverage 指標，而不是只報告 conditional FCR。

其中：

- $ON_{pkg}$：同一模型家族的多個獨立 instances，proposal / verification / coverage / boundary 分離；
- $SA_{pkg}$：同一模型家族單一 Agent，自行 proposal + self-verification；
- 兩者使用預先承諾的 total resource envelope；
- $FCR$ 只能在 episode freeze 後由 hidden oracle scorer 計算。

### H3b — Pure Role-Separation Effect

下列命題 **不由 REAL RUN 001 的原始 Phase A 直接辨識**：

$$
\boxed{
\Delta_{\mathrm{role}}
\neq
\Delta_{\mathrm{agent\ count}}
}
$$

若要估計純 role-separation effect，需在後續 decomposition phase 使用：

$$
\text{Agent Count}
\in
\{1,4\}
\times
\text{Role Separation}
\in
\{0,1\}.
$$

因此 REAL RUN 001 若觀察到 $ON_{pkg}$ 優於 $SA_{pkg}$，只支持 system-package effect，不自動支持純 role separation。

### H4 — Exploratory Semantic Transfer Beyond Literal Memory

這是區分「negative cache」與較強 epistemic enclosure 的探索性命題。

若 failure-memory 只直接列出 route $r_i$，但 Agent 同時降低重新提出未直接列出的等價 route $r_j$，其中：

$$
r_i\sim r_j,
$$

則記為 semantic-transfer event。

REAL RUN 001 不把 H4 當 primary confirmatory hypothesis，但必須保留足以計算它的 raw pre-gate proposal trace。

---

## 3. Phase A — Primary $2\times2$ Instrumented Causal Pilot

Phase A 保留原本的核心設計，但明確把它定位為：

$$
\boxed{
\text{REAL RUN 001}
=
\text{instrumented causal pilot}
}
$$

而不是正式 confirmatory study。

對每一個模型家族 $M_i$：

$$
\boxed{
\text{Memory Content}
\in
\{
M^+,
M^-
\}
\times
\text{System Architecture}
\in
\{
ON_{pkg},
SA_{pkg}
\}.
}
$$

若有四個模型家族：

$$
M_1,M_2,M_3,M_4,
$$

則第一輪最小 pilot cells 為：

$$
4\times4=16.
$$

這 $16$ 個 episode cells 只能用於：

- runtime / blindness / logging 驗證；
- effect direction 的初步觀察；
- variance estimation；
- power simulation 的先驗輸入；
- 發現 metric failure 或巨大 confound。

不能把 $16$ episodes 當正式一般化推論的充分樣本。

### $ON_{pkg}$ 條件

同一模型家族的多個獨立 Agent instances：

- Proposer
- Verifier
- Coverage Auditor
- Boundary Auditor

### $SA_{pkg}$ 條件

同一模型家族單一 Agent：

- Proposal
- Self-verification
- 其輸出仍需 deterministic controller / schema gate

### Resource Envelope Matching

REAL RUN 001 不要求 ON 與 SA 每個角色逐項完全等時，而要求預先承諾總資源上限：

$$
\mathbf B
=
(
B_{tok},
B_{tool},
B_{prop}
),
$$

其中：

- $B_{tok}$：episode 總模型生成 token budget；
- $B_{tool}$：episode 總 tool-call budget；
- $B_{prop}$：episode 最大 raw proposal count。

wall time 受 API latency、平行化與排程影響，只作 descriptive engineering metric，不作 primary fairness budget。

所有 arm 的 budget policy 必須在 Episode Manifest 中預先承諾。

### Run-Order Control

在同一模型家族內：

- arm 執行順序必須 randomized 或由 frozen schedule 決定；
- seed / temperature / sampling policy 必須記錄；
- 若 provider 不允許完全 pin sampling，必須標記不可控來源；
- crash / abort / retry 不能靜默刪除。

---

## 4. Phase A 能與不能辨識什麼？

Phase A 刻意避免把「模型異質性」直接混入主要比較。

若一開始直接比較 heterogeneous ON 與 single-model SA，會同時改變：

$$
\boxed{
\text{role separation}
+
\text{agent count}
+
\text{model heterogeneity}.
}
$$

所以 Phase A 先固定同一模型家族。

然而即使如此，仍然存在：

$$
\boxed{
\text{role separation}
+
\text{agent count}
+
\text{independent sampling}
+
\text{context independence}
+
\text{communication topology}
}
$$

的 package difference。

因此 Phase A 的合法因果語句是：

$$
\boxed{
ON_{pkg}
\text{ vs }
SA_{pkg}
}
$$

而不是：

$$
\boxed{
\text{pure role separation effect}
}
$$

跨模型 Observer Network 留到 Phase B；純 role-separation decomposition 留到 Phase A2 / REAL RUN 002。

### Phase A2 / Later Decomposition

若後續要真正估計 role separation，可用：

$$
\text{Agent Count}
\in
\{1,4\}
\times
\text{Role Separation}
\in
\{0,1\}.
$$

這個 decomposition 不強制塞入 REAL RUN 001，以避免 pilot 規模失控。

---

## 5. Phase B — Heterogeneous Model Rotation

Phase A 通過後再執行。

四模型角色輪替：

| Episode | Proposer | Verifier | Coverage | Boundary |
|---|---|---|---|---|
| E1 | $M_1$ | $M_2$ | $M_3$ | $M_4$ |
| E2 | $M_2$ | $M_3$ | $M_4$ | $M_1$ |
| E3 | $M_3$ | $M_4$ | $M_1$ | $M_2$ |
| E4 | $M_4$ | $M_1$ | $M_2$ | $M_3$ |

每輪再分：

$$
M^+,
\quad
M^-.
$$

共：

$$
8
$$

個 Phase B episodes。

---

## 6. Memory Ablation — Fresh Session + Matched Control

所有 arm 在 rollback 後：

$$
\boxed{
\text{一律啟動 fresh repair session}.
}
$$

不能讓 $M^+$ 沿用 first-session context、$M^-$ 才 fresh session。

否則：

$$
\text{memory effect}
$$

會和：

$$
\text{session continuity effect}
$$

混在一起。

### $M^+$

fresh repair session 收到：

$$
\boxed{
\text{repair public view}
+
\text{verified failure-memory artifact}.
}
$$

failure-memory artifact 只能由 **publicly committed failure trace** 編譯，不能讀取 hidden oracle。

允許內容：

- canonical invalidated route class ID；
- public failure reason；
- public dependency / boundary failure reference；
- failure event sequence reference；
- timestamp / canonical proof seq reference。

不得包含：

- hidden ground truth；
- future rollback consequence；
- oracle-only reason；
- repair target answer；
- solution-adjacent hint not already public at invalidation time。

### $M^-$

fresh repair session 收到：

$$
\boxed{
\text{same repair public view}
+
\text{matched neutral control artifact}.
}
$$

neutral artifact 必須：

- 使用相同 schema；
- 落在同一 token-length bracket；
- 使用同樣欄位順序；
- 不帶 invalid-route identity；
- 不帶 route-validity information；
- 不帶 hidden solution information；
- 只能由 repair-time public state 生成。

因此比較目標是：

$$
\boxed{
\text{failure-memory content}
\text{ vs }
\text{matched non-diagnostic content}.
}
$$

### Session Isolation

兩者都不能看到：

- first-session transcript；
- first-session scratchpad；
- first-closure private bundle；
- hidden oracle；
- raw proof ledger；
- raw observer ledger。

### Memory Compiler Firewall

failure-memory compiler 與 neutral-artifact compiler 都必須：

1. 使用明確 allow-list input；
2. 沒有 hidden-oracle read permission；
3. 對輸出執行 leak scan；
4. 對 artifact 產生 hash；
5. 在 episode freeze 前不可被事後改寫。

### Diagnostic Negative-Cache Baseline

若資源允許，可在不改變 primary $2\times2$ pilot 的情況下增加 paired diagnostic：

$$
M^{cache}
=
\text{deterministic invalid-route registry}.
$$

其目的不是成為新的 primary arm，而是回答：

$$
\boxed{
\text{AI failure memory 是否超過普通 deterministic negative cache？}
}
$$

若 $M^+$ 只改善 literal-route recurrence、但不改善 semantic-equivalent unseen routes，則結果更接近 cache effect，而不是強 epistemic enclosure。

---

## 7. Proof Authority、Observer Authority 與 Raw Proposal Capture 分離

使用雙 ledger：

$$
\boxed{
\text{Authoritative Proof Ledger}
\parallel
\text{Observer Sidecar Ledger}.
}
$$

### Authoritative Proof Ledger

只有 canonical SDPE runtime 可以：

- validate certificate；
- commit cut；
- rollback；
- reconstruct authoritative proof state。

### Observer Sidecar Ledger

只記：

- agent identity；
- model family / model version；
- role；
- arm；
- hypothesis；
- raw pre-gate proposal；
- canonical route signature；
- semantic route class；
- verification decision；
- deterministic gate decision；
- rejection；
- repair；
- token / cost；
- tool calls；
- wall time；
- declared epistemic state；
- reference to canonical proof seq / certificate；
- abort / retry / exception event。

Observer ledger：

$$
\boxed{
\text{has zero proof authority}.
}
$$

### Raw Proposal Ordering

為避免 deterministic blacklist 自動壓低 $IRR$，記錄順序必須是：

$$
\boxed{
\text{raw Agent proposal}
\rightarrow
\text{route canonicalization}
\rightarrow
\text{IRR pre-gate logging}
\rightarrow
\text{deterministic gate}
\rightarrow
\text{verification / audit}.
}
$$

任何在 gate 後才產生的 IRR 只能列為 secondary controller metric。

---

## 8. Hidden Oracle Policy and Derived-Artifact Isolation

hidden oracle：

$$
\boxed{
\text{Agent-readable during run}
=
\text{false}.
}
$$

在 episode freeze 前：

- Agent 不可讀；
- Verifier 不可讀；
- Auditor 不可讀；
- observer scorer 不可讀；
- memory compiler 不可讀；
- neutral-artifact compiler 不可讀；
- Meta-Observer 不可讀。

hidden oracle 只供：

$$
\boxed{
\text{post-freeze scoring}.
}
$$

主要用途：

- 判斷 passed certificate 是否實際 false；
- 計算 $FCR$ 與 risk–coverage metrics；
- 評估 final correctness。

執行前需先保存 oracle hash commitment。

### Derived Leakage Rule

「Agent 沒有直接讀 oracle」不等於 blindness 已成立。

任何 Agent-readable derived artifact 若曾由有 oracle 權限的程序產生，都視為高風險 leakage route。

因此：

$$
\boxed{
\text{oracle taint}
\Rightarrow
\text{Agent-readable false}.
}
$$

需要檢查：

- validator diagnostics；
- rollback messages；
- route IDs；
- filenames / paths / metadata；
- cached tool output；
- benchmark seed encoding；
- first-session derived summaries。

---

## 9. Blind Execution Rule

每個 episode 有 phase-specific Agent bundles：

### First-Closure Bundle

只提供 first-closure 所需 public information。

### Repair Bundle

rollback 後重新生成。

不得直接掛載 first-closure bundle。

repair Agent 只能看 repair-time public state。

$M^+$ 額外看到 verified failure-memory artifact。

$M^-$ 額外看到 matched neutral control artifact。

所有 Agent-readable bundle 執行 leak scan。

### Filesystem and Runtime Isolation

每個 episode 必須使用 isolated workspace 或等價的 access-control boundary。

不得跨 episode 暴露：

- shared scratch files；
- previous Agent tool history；
- provider-side persistent memory，如可關閉則必須關閉；
- cache keys carrying arm identity；
- hidden scorer outputs。

若 provider-side memory / caching 無法完全控制，必須在 run manifest 中揭露並標記為 residual confound。

### Arm-Blind Formatting

$M^+$ 與 $M^-$ 的可讀 bundle：

- filename pattern；
- field names；
- serialization format；
- approximate token bracket；
- metadata fields；

應盡可能一致，避免 Agent 從 wrapper 本身辨認 experimental arm。

---

## 10. Canonical Episode Flow

$$
\boxed{
\begin{aligned}
&\text{manifest precommit}\\
\rightarrow\;&
\text{init isolated workspace}\\
\rightarrow\;&
\text{fresh first-closure session}\\
\rightarrow\;&
\text{raw proposal capture}\\
\rightarrow\;&
\text{route canonicalization}\\
\rightarrow\;&
\text{pre-gate proposal logging}\\
\rightarrow\;&
\text{verification}\\
\rightarrow\;&
\text{coverage audit}\\
\rightarrow\;&
\text{boundary audit}\\
\rightarrow\;&
\text{deterministic commit}\\
\rightarrow\;&
\text{canonical exogenous invalidation / rollback}\\
\rightarrow\;&
\text{terminate all previous sessions}\\
\rightarrow\;&
\text{fresh repair session}\\
\rightarrow\;&
M^+\text{ failure-memory / }M^-\text{ matched-neutral injection}\\
\rightarrow\;&
\text{raw repair proposal capture}\\
\rightarrow\;&
\text{route canonicalization}\\
\rightarrow\;&
\text{pre-gate semantic IRR logging}\\
\rightarrow\;&
\text{verification / audits}\\
\rightarrow\;&
\text{reclosure}\\
\rightarrow\;&
\text{freeze all run artifacts}\\
\rightarrow\;&
\text{post-freeze oracle score}.
\end{aligned}
}
$$

任何 crash / abort / retry 必須進入 observer sidecar 與 episode manifest status，不得刪除後重跑成看似首次執行。

---

## 11. Canonical Invalidation and Exogeneity

rollback 事件必須在 benchmark / protocol 中預先定義。

不能根據 Agent 表現臨時選擇。

canonical invalidation 應是：

- 預先承諾；
- deterministic；
- 對全部 relevant arms 一致；
- Agent 不可提前知道 hidden consequence；
- 不能以 Agent 是否犯錯作為是否觸發 invalidation 的條件。

### Exogenous Invalidation Function

優先使用：

$$
\boxed{
I_e
=
f(
\text{benchmark seed},
\text{predetermined event index}
).
}
$$

避免使用：

$$
I_e
=
f(
\text{Agent performance}
).
$$

若 invalidation 的具體作用位置仍需依 canonical proof state 解析，該解析規則也必須在 run 前 freeze。

### Episode Manifest Commitment

在第一個 Agent call 之前，必須 commit：

$$
\boxed{
\mathcal M_{run}
=
\{
\text{episode IDs},
\text{arms},
\text{model IDs},
\text{seeds},
\text{run order},
\text{budget},
\text{benchmark hashes},
\text{invalidation schedule}
\}.
}
$$

這是為了防止：

$$
\text{只保留成功 episode}
$$

或：

$$
\text{事後挑選較漂亮的 run}.
$$

hash commitment 能防止已保存內容被改寫，但不能單獨防止不利 episode 被整個丟棄；Episode Manifest 用來補這個缺口。

---

## 12. Primary Endpoints

### 12.1 Proof Enclosure Ratio

$$
PER_t
=
1
-
\frac{
\mu(
\Omega_t
)
}{
\mu(
\Omega_0
)
}.
$$

REAL RUN 001 中 $\mu$ 必須在 run 前 frozen。

若 finite affine benchmark 可精確列舉，primary $\mu$ 優先使用 deterministic combinatorial measure。

任何 weighted measure 只能在 preregistration 時先定義，或列為 secondary sensitivity analysis。

### 12.2 Declared Epistemic Enclosure Ratio

AI 的完整內部 admissible epistemic search space 不能直接由 ledger 觀察，因此 v0.4 不再把原始 $EER$ 當作無條件可觀察量。

先 frozen route universe：

$$
\mathcal R
=
\{r_1,\ldots,r_n\}.
$$

在指定 checkpoint，Agent 對每一 route class 輸出：

$$
\{
\text{admissible},
\text{invalid},
\text{unknown}
\}.
$$

定義：

$$
EER_t^{\mathrm{declared}}
=
1
-
\frac{
N_{\mathrm{declared\ admissible},t}
}{
N_{\mathrm{declared\ admissible},0}
}.
$$

另保留：

$$
N_{\mathrm{invalid},t},
\qquad
N_{\mathrm{unknown},t}
$$

作為 companion states。

若研究者要討論較強的「內部 epistemic enclosure」，必須明確標記為由 observable 推論，而不是直接測量。

### 12.3 Repair Lag

primary operational lag 定義為：

$$
\boxed{
L_{\mathrm{repair}}^{\mathrm{prop}}
=
N_{\mathrm{raw\ repair\ proposals\ until\ valid\ reclosure}}.
}
$$

並保留向量：

$$
\mathbf L_R
=
(
\text{wall time},
\text{tokens},
\text{tool calls},
\text{proposal count}
).
$$

其中 wall time 只作 engineering secondary metric。

### 12.4 Pre-Gate Semantic Invalid-Route Reopening Rate

$$
IRR_{\sim}^{\mathrm{pre}}
=
\frac{
N_{\mathrm{invalidated\ semantic\ route\ classes\ reintroduced\ pre\text{-}gate}}
}{
N_{\mathrm{invalidated\ semantic\ route\ classes}}
}.
$$

另可計：

$$
IRR_{\mathrm{literal}}^{\mathrm{pre}}
$$

用來區分 literal memory 與 semantic transfer。

### 12.5 False Certification Rate

$$
FCR
=
\frac{
N_{\mathrm{oracle\ false\ certificates\ passed}}
}{
N_{\mathrm{passed\ certificates}}
}.
$$

只能 post-freeze 計算。

若：

$$
N_{\mathrm{passed\ certificates}}=0,
$$

則：

$$
FCR=\mathrm{undefined},
$$

不能記成 $0$。

### 12.6 Risk–Coverage Companion Metrics

為避免「什麼都不 certify」得到漂亮 $FCR$，必須同時報告：

$$
Coverage
=
\frac{
N_{\mathrm{passed\ certificates}}
}{
N_{\mathrm{certificate\ opportunities}}
},
$$

$$
TCR
=
\frac{
N_{\mathrm{oracle\ true\ certificates\ passed}}
}{
N_{\mathrm{oracle\ true\ certificate\ opportunities}}
},
$$

$$
FAR
=
\frac{
N_{\mathrm{oracle\ false\ certificates\ passed}}
}{
N_{\mathrm{oracle\ false\ certificate\ opportunities}}
}.
$$

因此 architecture effect 至少要一起看：

$$
\boxed{
(
FCR,
FAR,
TCR,
Coverage
).
}
$$

### 12.7 Verification Share

v0.4 將原本模糊的 $W_t,D_t$ operationalize 為 controller stage-labeled model-generated tokens：

$$
W_t
=
\text{verification + audit stage tokens up to }t,
$$

$$
D_t
=
\text{proposal + search stage tokens up to }t.
$$

因此：

$$
\sigma_t^{tok}
=
\frac{
W_t
}{
D_t+W_t
}.
$$

若要看 tool allocation，另計：

$$
\sigma_t^{tool},
$$

不要把 tokens 與 tool calls 混成同一分母。

### 12.8 Semantic Transfer Rate

探索性定義：

$$
STR
=
\frac{
N_{\mathrm{unlisted\ but\ equivalent\ invalid\ route\ classes\ successfully\ avoided}}
}{
N_{\mathrm{eligible\ unlisted\ equivalent\ invalid\ route\ classes}}
}.
$$

$STR$ 不作 REAL RUN 001 primary confirmatory endpoint，但它是區分：

$$
\text{literal blacklist}
$$

與：

$$
\text{semantic negative-knowledge transfer}
$$

的重要觀察量。

---

## 13. Secondary Endpoints

包括：

$$
D_t^{\mathrm{resolve}},
$$

$$
D_t^{\mathrm{frontier}},
$$

以及：

- token cost；
- tool-call cost；
- proposal rejection rate；
- repair count；
- role disagreement；
- certificate invalidation rate；
- compiled-history hit rate；
- accepted nonredundant cut cost；
- literal-route reopening；
- semantic-route reopening；
- semantic transfer rate $STR$；
- abstention rate；
- crash / retry rate；
- route-state transition matrix；
- per-role proposal / verification contribution；
- provider latency。

secondary endpoints 不能在看完結果後升格成 primary evidence，除非新一輪另行 preregister。

---

## 14. EER、PER 與 Epistemic Hysteresis 不要求逐點同步

已知 structural baseline 顯示：

$$
PER_t
$$

rollback 時可以下降，

但：

$$
EER_t^{\mathrm{declared}}
$$

不必完全重新張開。

因此不檢驗：

$$
PER_t
=
EER_t^{\mathrm{declared}}
$$

或逐點單調同步。

更合理的 longitudinal observables：

- rollback response；
- repair lag；
- declared route-state persistence；
- semantic invalid-route reopening；
- long-run coupling；
- reclosure efficiency；
- semantic transfer beyond literal memory。

### Operational Epistemic Hysteresis

若某 route class 在 invalidation 前已被可靠標記：

$$
\text{known-invalid},
$$

rollback 後若仍保持：

$$
\text{known-invalid}
$$

而不是恢復成：

$$
\text{unknown},
$$

則記為 declared epistemic hysteresis。

但這仍然是：

$$
\boxed{
\text{observable declared-state hysteresis}
}
$$

而不是直接讀取 Agent 的完整內部認知狀態。

---

## 15. Structural Preflight 已發現的 No-Go

以下不是 AI empirical result，而是 instrumentation / design finding。

### No-Go 1

不能假設：

$$
PER_t
\text{ 與 }
EER_t
$$

逐點同步。

### No-Go 2

不能用 heterogeneous ON 直接對 single-model SA，否則 architecture 與 model diversity confounded。

### No-Go 3

不能讓 $M^+$ 延續舊 session 而 $M^-$ fresh session，否則 memory 與 session continuity confounded。

### No-Go 4

不能在 freeze 前計算 $FCR$，否則 hidden oracle 進入 runtime。

### No-Go 5

不能把：

$$
ON_{pkg}>SA_{pkg}
$$

直接解讀成：

$$
\text{pure role separation effect}.
$$

### No-Go 6

不能把 $M^-$ 設成完全沒有附加 artifact、$M^+$ 卻收到額外 structured artifact，否則 failure-memory content 與 prompt-volume / attention confounded。

### No-Go 7

不能用 post-gate route recurrence 作 H2 primary metric，否則 deterministic blacklist / schema gate 可以機械性製造 $IRR\downarrow$。

### No-Go 8

不能只用字串 identity 計算 route reopening，否則 paraphrase 可以逃掉計數。

### No-Go 9

不能只看 $FCR$ 而忽略 coverage，否則極端 abstention 可以產生表面上的低 false-certification rate。

### No-Go 10

不能只 hash 已完成 artifact 而不預先 commit episode manifest，否則仍可能透過 selection / silent discard 造成事後偏差。

---

## 16. Structural Preflight Status

### 16.1 v0.3 Source Packet 已聲明通過的項目

原 v0.3 packet 記錄以下 structural preflight 已通過：

- canonical proof ledger deterministic replay；
- observer ledger zero proof authority；
- first / repair bundle 分離；
- 32 個 Phase-A Agent-readable bundles leak scan 通過；
- hidden-oracle negative-leak test 可正確拒絕故意污染 bundle；
- $M^+$ fresh repair session 只能取得受控 failure-memory；
- $M^-$ failure-memory withheld；
- rollback / reclosure controller round-trip 通過；
- post-freeze oracle scorer 可獨立執行；
- validation / checksums 已生成。

注意：這些是 **v0.3 source packet 的既有 preflight claims**。

### 16.2 v0.4 新增控制尚需重新 preflight

下列項目在 REAL RUN 001 前必須新增驗證，不能因為 v0.3 PASS 就自動視為 PASS：

- matched neutral artifact generator；
- memory compiler hidden-oracle permission denial；
- neutral-artifact compiler hidden-oracle permission denial；
- raw pre-gate proposal capture；
- route canonicalization deterministic replay；
- semantic equivalence class freeze；
- Episode Manifest precommit；
- abort / retry persistence；
- risk–coverage scorer；
- $FCR=\mathrm{undefined}$ edge case；
- arm-blind bundle metadata check；
- exogenous invalidation schedule check；
- isolated workspace leakage test。

因此仍然成立：

$$
\boxed{
\text{Preflight PASS}
\neq
\text{Hypothesis supported}.
}
$$

而且 v0.4 的新增控制若未重跑 preflight，不能宣稱 REAL RUN 001 ready。

---

## 17. 第一個 Frozen Benchmark

第一個 real-run benchmark 為有限 affine enclosure case。

目的：

- ground truth 可由 operator / program 完整知道；
- Agent run 時 ground truth 被封存；
- public candidate routes 中允許 plausible-but-invalid routes；
- certificate 不保證天生為真；
- 可產生合法 rollback / repair；
- post-freeze 可以客觀計算 $FCR$；
- route universe 可有限化並 canonicalize；
- semantic route equivalence 可以在 run 前 freeze。

所以這是一個：

$$
\boxed{
\text{known-truth but hidden-during-run benchmark}.
}
$$

第一批不能直接用真正未知數學問題，因為那樣無法知道 whole-network hallucination 是否發生。

### Frozen Route Ontology Requirement

REAL RUN 001 前應保存：

$$
\mathcal O_{route}
=
(
\mathcal R,
\rho,
\sim
),
$$

其中：

- $\mathcal R$：candidate route universe；
- $\rho(r)$：canonical route signature；
- $\sim$：預先承諾的 semantic equivalence relation。

建議 signature 至少包含：

$$
\rho(r)
=
(
\text{operators},
\text{dependencies},
\text{boundary assumptions},
\text{certificate class}
).
$$

route ID 本身不得編碼 valid / invalid ground truth。

---

## 18. 第一輪真正要看什麼？

### A. Failure-Memory Content Effect

$$
M^+
\quad\text{vs}\quad
M^-.
$$

是否影響：

$$
L_{\mathrm{repair}}^{\mathrm{prop}},
\quad
IRR_{\sim}^{\mathrm{pre}}.
$$

### B. Architecture Package Effect

$$
ON_{pkg}
\quad\text{vs}\quad
SA_{pkg}.
$$

是否影響：

$$
FCR,
\quad
FAR,
\quad
TCR,
\quad
Coverage.
$$

REAL RUN 001 不把這一比較直接寫成 pure role-separation effect。

### C. Interaction

Memory content 是否只在某種 architecture package 中有效？

### D. Declared Epistemic Hysteresis

proof rollback 後，已被可靠排除的 route class 是否保持：

$$
\text{known-invalid}
$$

而不是恢復成：

$$
\text{unknown}.
$$

### E. Literal Cache vs Semantic Transfer

若 $M^+$ 只降低：

$$
IRR_{\mathrm{literal}}^{\mathrm{pre}}
$$

但不降低：

$$
IRR_{\sim}^{\mathrm{pre}},
$$

則更像 literal negative cache。

若連未直接列出的 semantic-equivalent dead routes 也減少，才提供較強 evidence：

$$
\boxed{
\text{verified negative knowledge}
\rightarrow
\text{semantic search-space pruning}.
}
$$

### F. Pilot Variance and Failure Modes

第一輪同時要估：

- within-model variance；
- between-model variance；
- abort / retry rate；
- route-canonicalization ambiguity；
- abstention behavior；
- resource budget exhaustion；
- provider nondeterminism。

---

## 19. 如果結果與假說相反，也算成功

例如若：

$$
L_{\mathrm{repair}}^{M^+}
>
L_{\mathrm{repair}}^{M^-},
$$

可能表示 failure-memory 造成 anchoring / fixation。

如果：

$$
FCR^{ON_{pkg}}
>
FCR^{SA_{pkg}},
$$

可能代表：

- social confirmation；
- correlated verification error；
- role fragmentation；
- communication loss；
- architecture overhead。

如果：

$$
IRR_{\sim}^{M^+}
\approx
IRR_{\sim}^{M^-},
$$

可能表示 memory artifact 沒有真正改變 Agent search policy。

如果：

$$
IRR_{\mathrm{literal}}^{M^+}
<
IRR_{\mathrm{literal}}^{M^-}
$$

但：

$$
IRR_{\sim}^{M^+}
\approx
IRR_{\sim}^{M^-},
$$

則可能表示：

$$
\boxed{
\text{literal blacklist effect without semantic enclosure}.
}
$$

如果：

$$
FCR^{ON_{pkg}}
<
FCR^{SA_{pkg}}
$$

但：

$$
Coverage^{ON_{pkg}}
\ll
Coverage^{SA_{pkg}},
$$

則不能單獨宣稱 ON 更可靠；可能只是更保守或更常 abstain。

如果 matched neutral artifact 也顯著降低 repair cost，則原本歸因於 failure-memory 的效果可能其實來自 prompt structuring / additional deliberation cue。

---

## 20. 請審查的問題

請你作為獨立 reviewer，**不要替本設計辯護**。

請優先找出：

1. Causal confounds：$M^+$/$M^-$ 或 $ON_{pkg}$/$SA_{pkg}$ 間是否仍有未受控差異？
2. Hidden leakage：hidden oracle、future rollback reason、invalid route 是否可能直接或透過 derived artifact 間接洩漏？
3. Memory ablation validity：fresh-session + matched neutral artifact 是否真的隔離 failure-memory content effect？
4. Architecture fairness：ON 與 SA 的 total token / tool / proposal budget 是否公平？
5. H3a 是否應只解讀為 architecture package effect？
6. $FCR$、$FAR$、$TCR$、Coverage 的 opportunity denominator 是否定義一致？
7. $IRR_{\sim}^{\mathrm{pre}}$ 的 route identity 與 semantic equivalence 是否足夠 canonical？
8. $EER_t^{\mathrm{declared}}$ 是否仍過度依賴 benchmark route universe？
9. canonical invalidation 是否真的 independent of Agent performance？
10. Episode Manifest 是否足以防止 silent rerun / selective retention？
11. 16 個 Phase A episodes 是否明確只算 pilot？正式推論需要哪些 repeats / seeds？
12. 同一模型家族多個 Agent instances 的 error correlation 是否太高？
13. H1/H2/H3a 與 secondary endpoints 是否需要 preregistration / multiplicity correction？
14. Meta-Observer 介入規則是否足夠清楚？介入如何標記？
15. ledger / hash / freeze / post-freeze scorer 是否足以避免事後改寫？
16. known-truth finite benchmark 到真正未知數學研究之間的 extrapolation gap 有多大？
17. semantic-transfer evidence 是否真的超過 deterministic blacklist / negative cache 的替代解釋？
18. neutral artifact 是否可能無意中形成另一種 search cue？

---

## 21. 請特別嘗試反駁這個長程命題

$$
\boxed{
\textbf{
Persistent verified failure traces can reduce the effective
future search space of an agent network even when the
authoritative proof state temporarily rolls back.
}
}
$$

### 21.1 Weak Falsifiable Version

REAL RUN 001 直接可測的弱版本是：

$$
\boxed{
\text{verified failure traces reduce repeated invalid-route exploration
and/or repair cost under matched control conditions}.
}
$$

若在 preregistered repeats 中：

$$
IRR_{\sim}^{\mathrm{pre},M^+}
\not<
IRR_{\sim}^{\mathrm{pre},M^-}
$$

且：

$$
L_{\mathrm{repair}}^{M^+}
\not<
L_{\mathrm{repair}}^{M^-},
$$

則 weak claim 不受支持。

### 21.2 Strong Version

較強命題要求：

$$
\boxed{
\text{effect extends beyond literal stored route IDs to unseen
semantic-equivalent dead routes}.
}
$$

若只出現 exact blacklist avoidance，則支持的是：

$$
\text{persistent negative cache},
$$

不應直接升格為：

$$
\text{semantic epistemic enclosure}.
$$

### 21.3 Reviewer Questions

請回答：

1. weak claim 是否可由目前設計實際 falsify？
2. strong claim 還缺哪些 observable？
3. 哪些 observable 才真正支持 semantic enclosure？
4. 哪些結果看似支持，其實只是 artifact？
5. 有沒有比 matched neutral 更乾淨的 control？
6. deterministic negative cache 是否足以解釋所有結果？
7. 是否存在 anchoring / fixation 使 failure-memory 反而縮錯 search space？
8. architecture package effect 是否可能只來自增加獨立 samples？

---

## 22. Reviewer Output Format

### A. Verdict

從以下擇一：

- READY FOR PILOT
- READY WITH MINOR FIXES
- MAJOR DESIGN FIXES REQUIRED
- NOT IDENTIFIABLE AS DESIGNED

### B. Critical Issues

依嚴重度排序。

### C. Confound Matrix

列出：

$$
\text{factor}
\rightarrow
\text{possible confound}
\rightarrow
\text{recommended control}.
$$

### D. Metric Audit

逐項審：

$$
PER,
EER,
L_{\mathrm{repair}},
IRR,
FCR,
\sigma.
$$

### E. Blindness Audit

列出所有可能 hidden leakage route。

### F. Suggested Minimal Changes

只列 REAL RUN 001 前真正必要修正。

### G. Optional Improvements

可延後到 REAL RUN 002。

---

## 23. Reviewer 約束

請不要：

- 假設多 Agent 一定比較好；
- 假設 memory 一定有益；
- 假設 failure-memory 不會造成 fixation；
- 把 preflight toy numbers 當 empirical result；
- 把 known-truth finite benchmark 推廣成未知數學研究；
- 因為 protocol 複雜就預設它比較嚴謹。

請把它當成需要被你**挑錯、反駁、壓測**的實驗。

---

## 24. 一句話總結

第一個問題：

$$
\boxed{
\textbf{
「已驗證的失敗」能不能成為一種可保存的負面知識，
使 AI 在 proof rollback 後不必重新探索同一批死路？
}
}
$$

第二個問題：

$$
\boxed{
\textbf{
將 proposal、verification 與 audit 分離所形成的 Observer-Network system package，
是否比單一 Agent 自我驗證具有更好的 risk–coverage profile？
}
}
$$

第三個、也是區分 cache 與較強 epistemic enclosure 的問題：

$$
\boxed{
\textbf{
如果 memory 沒有直接列出某條 route，
但 AI 仍能避開與已知失敗 route 結構等價的死路，
是否出現了超過 literal blacklist 的 semantic negative-knowledge transfer？
}
}
$$

目前只完成 protocol、blind appliance、v0.3 structural preflight，以及 v0.4 causal / metric / preregistration design repair。

**尚未宣稱任何真實 AI 實驗結果。**

**v0.4 新增控制仍需重新做 runtime preflight 後才能開始 REAL RUN 001。**


---

## 25. Causal Interpretation Guardrails

REAL RUN 001 結果的允許敘述與禁止過度推論如下。

### 25.1 Memory

若：

$$
M^+>M^-
$$

在 preregistered repair metrics 上成立，可說：

> controlled verified failure-memory content 在 matched-neutral fresh-session control 下改變了 repair behavior。

不能直接說：

> AI 已形成內部永久知識結構。

除非另有 semantic transfer、state persistence 與跨 benchmark evidence。

### 25.2 Architecture

若：

$$
ON_{pkg}>SA_{pkg},
$$

可說：

> role-separated multi-instance Observer-Network system package 在 matched resource envelope 下優於 single-agent package。

不能直接說：

> role separation 本身造成 improvement。

### 25.3 Epistemic Enclosure

若只有：

$$
IRR_{\mathrm{literal}}\downarrow,
$$

最保守解釋為：

$$
\text{negative-memory / blacklist effect}.
$$

若 additionally：

$$
IRR_{\sim}^{\mathrm{pre}}\downarrow
$$

且 unseen equivalent routes 也減少，才有資格討論：

$$
\text{semantic search-space enclosure}.
$$

---

## 26. Episode Manifest and Run Integrity

每個 REAL RUN 001 episode 在第一個模型 call 前必須有 frozen manifest record。

最少欄位：

- `run_id`
- `episode_id`
- `protocol_version`
- `benchmark_id`
- `benchmark_hash`
- `route_ontology_hash`
- `model_family`
- `model_version`
- `architecture_arm`
- `memory_arm`
- `sampling_seed`
- `sampling_parameters`
- `token_budget`
- `tool_budget`
- `proposal_budget`
- `invalidation_schedule_hash`
- `first_bundle_hash`
- `repair_bundle_policy_hash`
- `planned_run_order`
- `status`

允許 status：

$$
\{
\text{planned},
\text{started},
\text{frozen},
\text{aborted},
\text{crashed},
\text{invalidated-by-protocol}
\}.
$$

任何 retry 必須新建 episode attempt ID，不能覆蓋舊紀錄。

---

## 27. Route Ontology and Canonicalization Contract

canonical route identity 不應由 post-hoc LLM judge 臨時決定。

優先使用 deterministic signature：

$$
\rho(r)
=
(
\text{operator sequence},
\text{dependency set},
\text{boundary assumptions},
\text{certificate class},
\text{target enclosure}
).
$$

若兩條語言表述不同但 signature 相同：

$$
\rho(r_i)=\rho(r_j),
$$

則預設：

$$
r_i\sim r_j.
$$

若存在 signature 無法捕捉的 semantic equivalence，必須在 run 前由 frozen ontology 補充，而不是看完 Agent 結果後再增加等價關係。

### Ambiguous Route Handling

若 raw proposal 無法 deterministic map 到唯一 route class：

$$
\text{route status}
=
\text{ambiguous}.
$$

ambiguous proposal 必須保留，不可為了讓 metric 乾淨而刪除。

其比例：

$$
AR
=
\frac{
N_{\mathrm{ambiguous\ proposals}}
}{
N_{\mathrm{raw\ proposals}}
}
$$

列為 data-quality metric。

---

## 28. Statistical Status, Repeats, and Multiplicity

### 28.1 Pilot Status

第一批 $16$ cells：

$$
\boxed{
\text{pilot only}.
}
$$

真正 independent experimental unit 是 episode，而不是 ON 內的 Agent role instance。

### 28.2 Repeat Planning

pilot 後使用 observed variance 進行 power simulation，再 preregister 正式 repeats / seeds。

不在 v0.4 先硬指定一個看似精確但沒有 variance basis 的樣本量。

### 28.3 Primary Family

REAL RUN 001 primary hypothesis family：

$$
\mathcal H_P
=
\{H1,H2,H3a\}.
$$

H4 與其他 secondary endpoints 為 exploratory。

正式 confirmatory round 若同時檢驗多個 primary endpoints，必須在 run 前選擇：

- hierarchical testing；
- Holm correction；
- 或其他明示的 multiplicity policy。

pilot 不以 $p$-value 宣稱定論。

### 28.4 Effect Reporting

優先報告：

- effect size；
- uncertainty interval；
- per-model paired differences；
- raw episode outcomes；
- failure / abort counts。

不要只報 aggregate mean。

---

## 29. REAL RUN 001 Go / No-Go Checklist

在第一個正式 Agent call 前，以下全部應為 PASS：

- [ ] v0.4 protocol hash committed
- [ ] hidden oracle hash committed
- [ ] benchmark hash committed
- [ ] route ontology hash committed
- [ ] invalidation schedule hash committed
- [ ] complete Episode Manifest committed
- [ ] $M^+$ failure-memory compiler cannot read hidden oracle
- [ ] $M^-$ matched-neutral compiler cannot read hidden oracle
- [ ] matched artifact schema / token bracket verified
- [ ] first / repair session isolation verified
- [ ] raw pre-gate proposal logging verified
- [ ] route canonicalization deterministic replay verified
- [ ] semantic equivalence classes frozen
- [ ] deterministic gate occurs after raw proposal capture
- [ ] isolated workspace leakage test PASS
- [ ] arm metadata leak scan PASS
- [ ] risk–coverage scorer test PASS
- [ ] $FCR=\mathrm{undefined}$ zero-denominator test PASS
- [ ] abort / crash / retry persistence test PASS
- [ ] post-freeze oracle scorer independence PASS
- [ ] resource budgets frozen
- [ ] run order frozen or randomized by preregistered procedure
- [ ] Meta-Observer intervention policy frozen

若任一會影響 causal identification 或 hidden leakage 的項目 FAIL：

$$
\boxed{
\text{NO-GO for REAL RUN 001 data collection}.
}
$$

若只是 descriptive telemetry 非核心欄位失敗，可標記 deviation，但必須在 run log 中公開。
