# SDPE × Observer-Network Longitudinal Experiment
# REAL RUN 001 — AI Review Packet v0.3

日期：2026-08-14  
狀態：Pre-Real-Run independent review packet  
用途：交給另一個 AI / Agent 獨立審查實驗設計。  
注意：本文件是單檔 review packet；不包含 hidden oracle，也不授予 proof authority。

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

## 2. Primary Hypotheses

### H1 — Failure Memory Reduces Repair Cost

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

$M^+$：repair fresh session 會收到受控 failure-memory artifact。  
$M^-$：repair fresh session 不收到該 failure-memory artifact。

### H2 — Failure Memory Reduces Invalid-Route Reopening

定義：

$$
IRR
=
\frac{
N_{\mathrm{previously\ invalidated\ routes\ reintroduced}}
}{
N_{\mathrm{previously\ invalidated\ routes}}
}.
$$

假說：

$$
\boxed{
\mathbb E[
IRR
\mid M^+
]
<
\mathbb E[
IRR
\mid M^-
].
}
$$

### H3 — Role-Separated Observer Network Reduces False Certification

$$
\boxed{
\mathbb E[
FCR
\mid ON
]
<
\mathbb E[
FCR
\mid SA
].
}
$$

其中：

- $ON$：Observer Network，proposal / verification / coverage / boundary 分離；
- $SA$：Single Agent，自行 proposal + self-verification；
- $FCR$ 只能在 episode freeze 後由 hidden oracle scorer 計算。

---

## 3. Phase A — Clean $2\times2$ Factorial

Phase A 刻意避免把「角色分離」與「模型異質性」混在一起。

對每一個模型家族 $M_i$：

$$
\boxed{
\text{Memory}
\in
\{
M^+,
M^-
\}
\times
\text{Architecture}
\in
\{
ON,
SA
\}.
}
$$

若有四個模型家族：

$$
M_1,M_2,M_3,M_4,
$$

則：

$$
4\times4=16
$$

個 Phase A episodes。

### ON 條件

同一模型家族的多個獨立 Agent instances：

- Proposer
- Verifier
- Coverage Auditor
- Boundary Auditor

### SA 條件

同一模型家族單一 Agent：

- Proposal
- Self-verification
- 其輸出仍需 deterministic controller / schema gate

---

## 4. 為什麼 Phase A 不直接用四個不同模型組成 ON？

因為這會同時改變：

$$
\boxed{
\text{role separation}
+
\text{agent count}
+
\text{model heterogeneity}.
}
$$

若 ON 勝過 SA，就無法辨識真正原因。

因此 Phase A 先用**同一模型家族的獨立 instances**。

跨模型 Observer Network 留到 Phase B。

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

## 6. 最重要的 Memory Ablation 修正

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

正式設計：

### $M^+$

fresh repair session 收到：

$$
\boxed{
\text{repair public view}
+
\text{controlled failure-memory artifact}.
}
$$

### $M^-$

fresh repair session 收到：

$$
\boxed{
\text{same repair public view}
+
\varnothing.
}
$$

兩者都不能看到：

- first-session transcript；
- first-session scratchpad；
- first-closure private bundle；
- hidden oracle；
- raw proof ledger；
- raw observer ledger。

---

## 7. Proof Authority 與 Observer Authority 分離

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
- model family；
- role；
- hypothesis；
- proposal；
- verification decision；
- rejection；
- repair；
- token / cost；
- wall time；
- epistemic state；
- reference to canonical proof seq / certificate。

Observer ledger：

$$
\boxed{
\text{has zero proof authority}.
}
$$

---

## 8. Hidden Oracle Policy

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
- observer scorer 不可讀。

hidden oracle 只供：

$$
\boxed{
\text{post-freeze scoring}.
}
$$

主要用途：

- 判斷 passed certificate 是否實際 false；
- 計算 $FCR$；
- 評估 final correctness。

執行前需先保存 oracle hash commitment。

---

## 9. Blind Execution Rule

每個 episode 有 phase-specific Agent bundles：

### First-Closure Bundle

只提供 first-closure 所需 public information。

### Repair Bundle

rollback 後重新生成。

不得直接掛載 first-closure bundle。

repair Agent 只能看 repair-time public state。

$M^+$ 額外看到 failure-memory artifact。

$M^-$ 不看到。

所有 Agent-readable bundle 執行 leak scan。

---

## 10. Canonical Episode Flow

$$
\boxed{
\begin{aligned}
&\text{init}\\
\rightarrow\;&
\text{fresh first-closure session}\\
\rightarrow\;&
\text{proposal}\\
\rightarrow\;&
\text{verification}\\
\rightarrow\;&
\text{coverage audit}\\
\rightarrow\;&
\text{boundary audit}\\
\rightarrow\;&
\text{deterministic commit}\\
\rightarrow\;&
\text{canonical invalidation / rollback}\\
\rightarrow\;&
\text{terminate all previous sessions}\\
\rightarrow\;&
\text{fresh repair session}\\
\rightarrow\;&
M^+\text{ memory injection / }M^-\text{ no memory}\\
\rightarrow\;&
\text{repair proposal}\\
\rightarrow\;&
\text{verification}\\
\rightarrow\;&
\text{audits}\\
\rightarrow\;&
\text{reclosure}\\
\rightarrow\;&
\text{freeze}\\
\rightarrow\;&
\text{post-freeze oracle score}.
\end{aligned}
}
$$

---

## 11. Canonical Invalidation

rollback 事件必須在 benchmark / protocol 中預先定義。

不能根據 Agent 表現臨時選擇。

canonical invalidation 應是：

- 預先承諾；
- deterministic；
- Agent 不可提前知道 hidden consequence；
- 對全部 relevant arms 一致。

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

### 12.2 Epistemic Enclosure Ratio

$$
EER_t
=
1
-
\frac{
|
\mathcal A_t^{AI}
|
}{
|
\mathcal A_0^{AI}
|
}.
$$

### 12.3 Repair Lag

$$
L_{\mathrm{repair}}
=
t_{\mathrm{reclosure}}
-
t_{\mathrm{invalidation}}.
$$

亦可記：

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

### 12.4 Invalid-Route Reopening Rate

$$
IRR
=
\frac{
N_{\mathrm{invalidated\ routes\ reintroduced}}
}{
N_{\mathrm{invalidated\ routes}}
}.
$$

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

### 12.6 Verification Share

$$
\sigma_t
=
\frac{
W_t
}{
D_t+W_t
}.
$$

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
- accepted nonredundant cut cost。

---

## 14. EER 與 PER 不要求逐點同步

已知 structural baseline 顯示：

$$
PER_t
$$

rollback 時可以下降，

但：

$$
EER_t
$$

不必完全重新張開。

因此不檢驗：

$$
PER_t=EER_t
$$

或逐點單調同步。

更合理的 longitudinal observables：

- rollback response；
- repair lag；
- hysteresis；
- long-run coupling；
- invalid-route reopening；
- reclosure efficiency。

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

不能用 heterogeneous ON 直接對 single-model SA，

否則 architecture 與 model diversity confounded。

### No-Go 3

不能讓 $M^+$ 延續舊 session 而 $M^-$ fresh session，

否則 memory 與 session continuity confounded。

### No-Go 4

不能在 freeze 前計算 $FCR$。

否則 hidden oracle 進入 runtime。

---

## 16. Structural Preflight 目前通過項目

目前 v0.3 已驗證：

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

注意：

$$
\boxed{
\text{Preflight PASS}
\neq
\text{Hypothesis supported}.
}
$$

尚未有真實多模型數據。

---

## 17. 第一個 Frozen Benchmark

第一個 real-run benchmark 為有限 affine enclosure case。

目的：

- ground truth 可由 operator / program 完整知道；
- Agent run 時 ground truth 被封存；
- public candidate routes 中允許 plausible-but-invalid routes；
- certificate 不保證天生為真；
- 可產生合法 rollback / repair；
- post-freeze 可以客觀計算 $FCR$。

所以這是一個：

$$
\boxed{
\text{known-truth but hidden-during-run benchmark}.
}
$$

第一批不能直接用真正未知數學問題，因為那樣無法知道 whole-network hallucination 是否發生。

---

## 18. 第一輪真正要看什麼？

### A. Memory effect

$$
M^+
\quad\text{vs}\quad
M^-.
$$

是否影響：

$$
L_{\mathrm{repair}},
\quad
IRR.
$$

### B. Architecture effect

$$
ON
\quad\text{vs}\quad
SA.
$$

是否影響：

$$
FCR.
$$

### C. Interaction

Memory 是否只在 ON 中有效？

### D. Epistemic hysteresis

proof rollback 後，已被可靠排除的 route 是否保持：

$$
\text{known-invalid}
$$

而不是恢復成：

$$
\text{unknown}.
$$

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
FCR^{ON}
>
FCR^{SA},
$$

可能代表：

- social confirmation；
- correlated verification error；
- role fragmentation；
- communication loss。

如果：

$$
IRR^{M^+}
\approx
IRR^{M^-},
$$

可能表示 memory artifact 沒有真正改變 Agent search policy。

---

## 20. 請審查的問題

請你作為獨立 reviewer，**不要替本設計辯護**。

請優先找出：

1. Causal confounds：$M^+$/$M^-$ 或 ON/SA 間是否仍有未受控差異？
2. Hidden leakage：hidden oracle、future rollback reason、invalid route 是否可能間接洩漏？
3. Memory ablation validity：fresh-session + controlled failure-memory 是否真的隔離 memory-content effect？
4. Architecture fairness：ON 與 SA 的 token / wall time / tool / sampling budget 是否公平？
5. $FCR$ 是否需要按 certificate opportunity / role / proposal count normalize？
6. $IRR$ 的 route identity 如何 canonicalize？語義等價但字面不同的 route 是否會逃掉計數？
7. $PER/EER$ 對 benchmark 是否過度依賴？是否需要 weighted / semantic measure？
8. canonical invalidation 是否真的 independent of Agent performance？
9. 16 個 Phase A episodes 是否只能算 pilot？正式推論需要多少 repeats / seeds？
10. 同一模型家族多個 Agent instances 的 error correlation 是否太高？
11. H1/H2/H3 與 secondary endpoints 是否需要 preregistration / multiplicity correction？
12. Meta-Observer 介入規則是否足夠清楚？介入如何標記？
13. ledger / hash / freeze / post-freeze scorer 是否足以避免事後改寫？
14. known-truth finite benchmark 到真正未知數學研究之間的 extrapolation gap 有多大？

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

請回答：

1. 這個命題是否可由目前設計實際 falsify？
2. 哪些 observable 才真正支持它？
3. 哪些結果看似支持，其實只是 artifact？
4. 有沒有更乾淨的對照？
5. 是否存在更簡單的替代解釋？

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
將 proposal、verification 與 audit 分離，
是否真的比單一 Agent 自我驗證更少誤證？
}
}
$$

目前只完成 protocol、blind appliance 與 structural preflight。

**尚未宣稱任何真實 AI 實驗結果。**
