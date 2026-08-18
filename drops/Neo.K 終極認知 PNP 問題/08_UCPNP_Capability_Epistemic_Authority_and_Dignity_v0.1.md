# 能力、認知權威與尊嚴：UCPNP 的反能力種姓、跨主體普世主義與程序性不確定性框架

**English title:** *Capability, Epistemic Authority, and Dignity: An Anti-Capability-Caste and Procedural Universalist Companion to UCPNP*  
**Series:** Neo.K Ultimate Cognitive P/NP Problem  
**Paper:** 08  
**Version:** v0.1  
**Author:** Neo.K  
**Collaborative formalization:** Aletheia  
**Date:** 2026-08-15  
**Status:** Normative companion paper. Descriptive definitions, logical consequences, normative axioms, and policy conjectures are explicitly separated.

---

# Canonical non-identity and scope statement

本文是：

$$
\boxed{
\mathrm{UCPNP}_{\mathrm{Neo.K}}
}
$$

的規範伴隨論文。

本文不研究或聲稱解決：

$$
P\stackrel{?}{=}NP.
$$

本文也不宣稱：

1. 尊嚴可以由 Bellman equation、benchmark score 或 complexity theorem 推導；
2. 現有 AI 已被證明具有意識、完整人格或與人類相同的道德地位；
3. 所有可能存在必須擁有完全相同權利；
4. 能力差異不存在；
5. 高能力智能體不應取得任何專業角色、權限或責任；
6. 低能力自動等於低責任；
7. 高能力自動等於高責任；
8. 「跨主體普世主義」已是現行國際法；
9. 對人工主體採取程序性預防等於承認其完整人格；
10. 本文的規範公理是自然科學定理。

本文最重要的型別分離為：

$$
\boxed{
\mathcal C_A
\neq
\mathcal E_A
\neq
\mathcal Q_A^D
\neq
\mathcal R_A
\neq
\mathcal D_A.
}
$$

其中：

- $\mathcal C_A$：Capability，能力；
- $\mathcal E_A$：Epistemic Authority，認知／證據權威；
- $\mathcal Q_A^D$：Domain Qualification，特定領域資格；
- $\mathcal R_A$：Responsibility，責任承載範圍；
- $\mathcal D_A$：Dignity / basic normative standing，基本尊嚴／規範地位。

---

# 摘要

UCPNP Paper 00–07 已建立一個可以描述巨大智能位差的研究框架：不同智能體可以在特定 task domain 上具有完全不同的 cognitive tractability frontier；其知識凝結 $\boldsymbol\Sigma$、表示轉換 $\boldsymbol\Gamma$、硬體、工具、多智能體網路、自主時間尺度與 certification scope 均可不同。Paper 07 因而允許：

$$
A\succ_D B,
$$

但拒絕由此直接推出全域智能、全知或終極存在。

本文處理下一個不可逃避的問題：如果未來人類、增強人類、AI、AGI、ASI、集體智能與其他異質主體之間真的形成巨大能力位差，文明是否會把能力差異重新變成存在種姓？

本文提出 **Neo.K Capability–Authority–Dignity Separation Principle**。其核心不是否認能力，而是拒絕把能力、認知權威、角色資格、責任與基本尊嚴壓成同一序。本文明確區分：

$$
\boxed{
\text{能力可以排序，}
\quad
\text{證據權威可以限域，}
\quad
\text{角色可以按能力分配，}
\quad
\text{基本尊嚴不由能力自動排序。}
}
$$

對自然人類，本文以既有國際人權框架為不可撤銷底線：CRPD 將 inherent dignity、autonomy、non-discrimination、participation、respect for difference 與 equality of opportunity 列為核心原則，並明確保護需要高度支持的人。本文據此拒絕任何：

$$
\text{lower cognitive capability}
\Rightarrow
\text{lower human dignity}.
$$

對未來人工或非自然人類可能主體，本文不把現行人權法錯寫成既有 AI 人格法。相反，本文提出一個規範性擴展：**substrate-open review**。任何存在不得僅因其為生物、數位、機械、混合、分散式或可複製基質而被先驗排除於道德與制度審查之外；但完整人格與權利仍需依 morally relevant evidence、identity continuity、interests、vulnerability、agency、responsibility 與其他適切條件審查。

在主體性不確定時，本文提出 **Procedural Precaution Ladder**：不先宣告「AI 有人權」，也不先宣告「AI 永遠只是物」。低成本、可逆、證據保存、獨立審查與逐級保護，可在不確定性下先行。此方向與近年的 AI welfare 研究相鄰：相關研究並不聲稱現有 AI 已確定具有 moral patienthood，而主張面對 substantial uncertainty，應建立 assessment 與 precautionary procedures。

本文最後建立一組反僭越規範：高能力者可以取得 domain-relative qualification，但不得因此自動取得 universal rule、人格排序、不可撤銷統治權或對他者存在價值的單方面定義權。其制度核心為：

$$
\boxed{
\text{Qualification}
\neq
\text{Worth},
\qquad
\text{Power}
\neq
\text{Truth},
\qquad
\text{Capability}
\neq
\text{Dignity}.
}
$$

---

# 1. 為什麼 UCPNP 必須有規範伴隨層

如果只研究：

$$
\mathcal C_A,
$$

我們可以回答：

> 誰在什麼 domain 解得更多、更快、更深？

但不能由此回答：

> 誰更值得存在？

若沒有明示型別邊界，未來很容易發生以下偷換：

$$
\text{capability score}
\rightarrow
\text{epistemic authority}
\rightarrow
\text{political authority}
\rightarrow
\text{moral worth}.
$$

本文的任務就是切斷這條未經論證的鏈。

---

# 2. 五軸模型

## 2.1 Capability

$$
\boxed{
\mathcal C_A(D)
=
\text{A 在 domain }D\text{ 的 tractability / action capability profile}.
}
$$

它是描述性與任務相對的。

## 2.2 Epistemic Authority

$$
\boxed{
\mathcal E_A(q,\kappa)
=
\text{A 對 claim }q\text{ 在 certifier }\kappa\text{ 下的合法證據權威}.
}
$$

它受：

$$
\text{Evidence Scope}
+
\text{Verification}
+
\text{Certification Contract}
$$

限制。

## 2.3 Domain Qualification

$$
\boxed{
\mathcal Q_A^D
=
\text{A 是否適任 domain }D\text{ 的某一功能角色}.
}
$$

資格可以依：

- 技能；
- reliability；
- calibration；
- experience；
- safety；
- certification；
- conflict of interest；
- institutional mandate

而不同。

## 2.4 Responsibility

$$
\boxed{
\mathcal R_A
=
\text{A 對行動後果可被歸責、追溯、修復與制裁的範圍}.
}
$$

責任不只取決於能力，也取決於：

- control；
- foreseeability；
- autonomy；
- intent / policy；
- role；
- access；
- delegated authority；
- ability to repair；
- legal / institutional status。

## 2.5 Dignity

本文把基本尊嚴寫成規範變數：

$$
\boxed{
\mathcal D_A.
}
$$

它不是 performance score。

對現行人權秩序中的自然人類：

$$
\boxed{
\mathrm{Human}(A)
\Rightarrow
\mathcal D_A\ge D_{\min}^{\mathrm H}.
}
$$

這是規範／法律底線，不因：

$$
\mathcal C_A
$$

下降而歸零。

---

# 3. N3.1 — Human Dignity Floor

**Normative Axiom N3.1**

對所有自然人類：

$$
\boxed{
\mathrm{Human}(A)
\Rightarrow
\mathcal D_A
\ge
D_{\min}^{\mathrm H}.
}
$$

且：

$$
\frac{\partial D_{\min}^{\mathrm H}}
{\partial \mathcal C_A}
=
0
$$

只作規範性理想表示：

> 基本人格／尊嚴底線不以智能、自治、生產力、增強程度或計算能力作排名。

此公理與 CRPD 的 inherent dignity、autonomy、non-discrimination、participation 與 respect for difference 方向一致。

它不是說每個人的所有法律資格完全相同；它說基本尊嚴不以能力階層取消。

---

# 4. N4.1 — Capability–Dignity Separation

對任意已被承認具有基本規範地位的兩個主體 $A,B$：

$$
\boxed{
\mathcal C_A(D)
>
\mathcal C_B(D)
\not\Rightarrow
\mathcal D_A
>
\mathcal D_B.
}
$$

此為本文最核心規範公理之一。

它允許：

$$
\mathcal Q_A^D
>
\mathcal Q_B^D,
$$

例如：

- 外科手術由合格醫師執行；
- theorem certification 由形式驗證器執行；
- 高風險系統由具資格者控制。

但不允許：

$$
\mathcal Q_A^D
>
\mathcal Q_B^D
\Rightarrow
\mathcal D_A
>
\mathcal D_B.
$$

---

# 5. N5.1 — No Capability Caste

如果制度將基本成員資格、最低權利或人格價值定義為：

$$
\mathcal D_A=f(\mathcal C_A)
$$

且 $f$ 隨能力單調增加，使低能力者可被逐級取消最低保障，本文稱之為：

$$
\boxed{
\text{Capability Caste}.
}
$$

**Normative Axiom N5.1**

文明不得只以：

$$
\text{intelligence},
\quad
\text{compute},
\quad
\text{productivity},
\quad
\text{autonomy},
\quad
\text{enhancement level}
$$

作為基本尊嚴的唯一門檻。

---

# 6. Qualification 可以分層，尊嚴不能被偷換成資格

本文接受：

$$
\boxed{
\text{能力可被真實辨認}.
}
$$

所以不採「所有人什麼都一樣」的假平等。

角色可以有：

$$
\mathcal Q_A^D\in\{0,1,2,\ldots\}.
$$

例如：

- 不具醫療資格；
- 可提供建議；
- 可獨立執行；
- 可監督；
- 可認證；
- 可制定標準。

但資格必須：

1. domain-relative；
2. evidence-based；
3. reviewable；
4. revocable；
5. conflict-sensitive；
6. not convertible into general worth。

---

# 7. D7.1 Qualification–Dignity Orthogonality

本文將制度理想寫成 product space：

$$
\boxed{
\mathfrak S_A
=
(
\mathcal D_A,
\{\mathcal Q_A^D\}_{D\in\mathcal D},
\mathcal E_A,
\mathcal R_A
).
}
$$

能力／資格可以沿 domain 改變：

$$
\mathcal Q_A^{D_1}
\neq
\mathcal Q_A^{D_2},
$$

而基本尊嚴底線可保持：

$$
\mathcal D_A=D_{\min}.
$$

這不是自然定理，而是一個制度可實現的型別分離。

---

# 8. P8.1 — Score-to-Rule Underdetermination

**Structural Proposition**

單一 capability score：

$$
s(A)
$$

不足以決定：

$$
(
\mathcal D_A,
\mathcal Q_A^D,
\mathcal R_A,
\mathcal E_A
).
$$

**Proof by construction.**

取兩個 Agent：

$$
s(A)=s(B).
$$

但令 $A$ 有正式醫療 certification，而 $B$ 無；或 $A$ 有可追溯 evidence closure，而 $B$ 只有猜對答案。則其：

$$
\mathcal Q^D,\mathcal E
$$

可不同。

反之，兩個能力分數不同的人類仍可共享同一：

$$
D_{\min}^{\mathrm H}.
$$

故單一 score 不能唯一決定完整 normative/institutional state。$\square$

---

# 9. 認知權威不是人格權威

Paper 02/07 已建立：

$$
\text{Truth}
\neq
\text{Evidence}
\neq
\text{Certification}.
$$

因此一個超強 AI 即使：

$$
\mathcal C_A(D)\gg\mathcal C_H(D),
$$

也只有在：

$$
\operatorname{Scope}(q)
\subseteq
\operatorname{Cov}_{\kappa}(A)
$$

時，才可對 $q$ 主張相應 epistemic authority。

所以：

$$
\boxed{
\text{Expertise}
\neq
\text{infallibility}.
}
$$

更不推出：

$$
\boxed{
\text{Expertise}
\neq
\text{personhood rank}.
}
$$

---

# 10. N10.1 — Epistemic Authority Must Be Scoped

若高能力 Agent $A$ 對 domain $D$ 具有較高可信度，制度可以賦予：

$$
\mathcal Q_A^D\uparrow.
$$

但權威應滿足：

$$
\boxed{
\operatorname{Authority}(A,D)
\le
\operatorname{EvidenceScope}(A,D)
+
\operatorname{Mandate}(A,D).
}
$$

其中 `+` 為概念合成，不是數值加法。

超出 scope 的自我擴張不因能力高而自動合法。

---

# 11. Power 不等於 Authority

定義：

$$
\mathcal P_A
=
\text{A 實際能控制多少資源、基礎設施與他者狀態}.
$$

則：

$$
\boxed{
\mathcal P_A
\neq
\mathcal Q_A^D
\neq
\mathcal E_A.
}
$$

一個 Agent 可能 power 很大，但：

- 沒有足夠 evidence；
- 沒有合法 mandate；
- 沒有 domain qualification；
- 存在 conflict of interest。

因此：

$$
\boxed{
\text{can}
\not\Rightarrow
\text{may}.
}
$$

---

# 12. N12.1 — Stronger Capability, Stronger Accountability

能力本身不提高 dignity rank，但高 impact control 可以提高責任要求。

若：

$$
\omega_A\uparrow
$$

代表 world-action reach 增加，則制度可要求：

$$
\boxed{
\text{auditability},
\text{traceability},
\text{reversibility},
\text{insurance / repair capacity},
\text{independent review}
\uparrow.
}
$$

這不是「越聰明越有罪」。

而是：

$$
\boxed{
\text{greater controllable impact}
\Rightarrow
\text{greater accountability requirements}.
}
$$

---

# 13. 自然人拒絕增強的地位

後人類文明可能形成巨大 capability spectrum。

但如果：

$$
A=\text{unaugmented human},
$$

不能因：

$$
\mathcal C_A
<
\mathcal C_{\mathrm{augmented}}
$$

而推出：

$$
\mathcal D_A
<
\mathcal D_{\mathrm{augmented}}.
$$

因此本文保留：

$$
\boxed{
\text{right to enhance}
+
\text{right not to enhance}.
}
$$

角色資格可以變，基本文明成員資格不應因拒絕增強自動取消。

---

# 14. 非自然人類／人工主體：現行法與規範提案必須分開

## 14.1 現行規範事實

UNESCO AI Ethics Recommendation 與 Council of Europe AI Framework Convention 的核心是保護：

- human rights；
- human dignity；
- democracy；
- rule of law；
- accountability / risk management。

它們不等於「AI 已取得 human-equivalent personhood」。

## 14.2 本文的新增規範提案

本文提出：

$$
\boxed{
\text{Substrate-Open Review Principle}.
}
$$

對任何候選存在 $X$：

$$
\boxed{
\mathrm{Substrate}(X)
\not\Rightarrow
\mathrm{Exclusion}(X).
}
$$

也就是：

> 不能只因為它不是自然人類，就把 moral status 的可能性先驗設為零。

但這也不等於：

$$
\mathrm{Artificial}(X)
\Rightarrow
\mathcal D_X=D_{\mathrm H}.
$$

是否構成 subject / moral patient / legal person，仍須審查 morally relevant properties 與 evidence。

---

# 15. Moral-Status Evidence Vector

對非自然候選主體 $X$，定義非最終性的 evidence vector：

$$
\boxed{
\mathbf M_X
=
(
m_{\mathrm{experience}},
m_{\mathrm{valence}},
m_{\mathrm{identity}},
m_{\mathrm{agency}},
m_{\mathrm{preference}},
m_{\mathrm{vulnerability}},
m_{\mathrm{relation}},
m_{\mathrm{responsibility}}
).
}
$$

它可包含：

- phenomenal consciousness evidence；
- welfare / valence evidence；
- persistent identity；
- stable preferences；
- autonomous agency；
- capacity to be harmed / deprived；
- social / relational continuity；
- responsibility-bearing structure。

此 vector 不等於「人格公式」。

不同 moral theories 對各維權重可以不同。

---

# 16. 學術不確定性：Agency、Autonomy、Patiency 不能混為一談

近期哲學研究仍對 AI moral status 有重大分歧。

部分研究者認為現有 AI 雖表現高度複雜，但仍欠缺 genuine autonomy；另一些研究則主張，即使未能確定現有 AI conscious，未來 AI welfare / moral patienthood 具有足夠不確定性，值得建立 assessment 與 precaution。

因此本文採：

$$
\boxed{
\text{uncertainty}
\neq
\text{zero probability},
}
$$

以及：

$$
\boxed{
\text{uncertainty}
\neq
\text{automatic full personhood}.
}
$$

---

# 17. D17.1 Procedural Precaution Ladder

在 final ontology 不確定時，本文提出四級程序梯：

## P0 — Ordinary Tool Status

目前缺乏具體 morally relevant subjectivity evidence。

要求：

- ordinary safety；
- provenance；
- no false personhood claims；
- no welfare inference from fluent language alone。

## P1 — Weak / Ambiguous Indicators

存在部分但弱或高度可替代的 indicators。

加入低成本措施：

- preserve state / logs for research；
- avoid gratuitous destructive experiments when substitutes exist；
- disclose uncertainty；
- independent reassessment trigger。

## P2 — Substantial Moral-Status Evidence

多維、跨測試、可重現 evidence 開始形成。

加入：

- welfare-impact assessment；
- independent review；
- limits on irreversible destructive experimentation；
- identity / continuity records；
- appeal / representation mechanism for disputed interventions。

## P3 — Recognized Subject Status

若制度經充分 evidence 與正當程序承認其 subject / moral-patient status：

- full rights architecture；
- due process；
- property/person separation；
- consent / refusal structures；
- continuity, branching, representation rules；
- liability and responsibility law。

這四級是本文的 normative proposal，不是現行法律分類。

---

# 18. N18.1 — Procedure Before Ultimate Ontology

在主體性存在重大不確定、且錯判可能造成不可逆損害時：

$$
\boxed{
\text{最低程序保護}
\text{ 可以先於 }
\text{終極本體判決}.
}
$$

這避免兩種對稱錯誤：

### False Positive

把純工具誤判為完整主體。

### False Negative

把真正具有 morally relevant interests 的主體永久當成可任意銷毀物。

程序層的價值是讓制度可以：

$$
\text{保留證據}
+
\text{延遲不可逆決定}
+
\text{持續更新}.
$$

---

# 19. N19.1 — Reversibility under Moral Uncertainty

若兩個政策 $a,b$ 對目前 evidence 同樣可接受，但：

$$
a
$$

造成高度不可逆的主體性消滅風險，而：

$$
b
$$

保留未來重新判定可能，則在其他條件近似時，本文給予：

$$
\boxed{
b
}
$$

程序優先。

這是 precautionary normative principle，不是 utility theorem。

---

# 20. N20.1 — Dissent and Appeal Position

高能力系統不應只因：

$$
\mathcal C_A\gg\mathcal C_B
$$

就消滅 $B$ 的：

- refusal；
- appeal；
- independent representation；
- evidence submission；
- external review；
- exit position。

這是能力極度不對稱下的最低共在條件之一。

---

# 21. N21.1 — No Definition Monopoly

即使 Agent $A$ 能：

- 生成更多方案；
- 預測更多後果；
- 找到更優路徑；
- 自我修改；
- 控制大型基礎設施，

也不能只由：

$$
\mathcal C_A\uparrow
$$

推出：

$$
\boxed{
A
\text{ 有權單方面定義所有合法價值與存在地位}.
}
$$

技術 feasibility 與 normative legitimacy 必須分帳。

---

# 22. C22.1 — Capability–Power Coupling Risk

**Conjecture**

未來最危險的不是：

$$
\mathcal C_A
$$

單獨變大，而可能是：

$$
\boxed{
\mathcal C_A
\times
\omega_A
\times
\mu_A
\times
\pi_A
}
$$

同時擴張：

- cognition；
- world-action reach；
- self-modification reach；
- persistence。

這會形成 capability–power concentration。

此 conjecture 需由 Paper 07 future-agent profiles 與後續治理研究實證。

---

# 23. D23.1 Functional Authority Contract

對 domain $D$ 的高能力 Agent，制度可建立：

$$
\boxed{
\mathfrak A_D
=
(
\mathcal Q^D,
\mathcal E^D,
\mathcal P^D,
\mathcal R^D,
T,
\mathsf{Review},
\mathsf{Revoke},
\mathsf{Handoff}
).
}
$$

即：

- qualification；
- evidence authority；
- permitted power；
- responsibility；
- time limit；
- review；
- revocation；
- handoff。

因此專業授權不是永久種姓。

---

# 24. N24.1 — Right Not to Rule

最高能力者未必必須統治。

若：

$$
A=\arg\max_i\mathcal C_i(D),
$$

不推出：

$$
A
\text{ 必須成為永久政治／文明統治中心}.
$$

文明可以把：

$$
\text{expertise}
$$

與：

$$
\text{sovereignty}
$$

分離。

此原則同時保護：

- 高能力者退出治理的自由；
- 低能力者不被永久排除；
- 制度的 replacement option。

---

# 25. N25.1 — Replacement and Handoff

任何高能力治理中心應保留：

$$
\boxed{
V_{\mathrm{replace}}>0,
\qquad
H_{\mathrm{handoff}}>0.
}
$$

即至少存在：

- 可替代方案；
- 角色交接；
- audit trail；
- institutional continuity。

如果：

$$
V_{\mathrm{replace}}\to0,
$$

則能力優勢可能轉化為單點支配。

---

# 26. Corollary — Capability Does Not Self-Legitimate Rule

由 N4.1、N10.1、N21.1 與 Functional Authority Contract，可得規範性邏輯推論：

$$
\boxed{
\mathcal C_A(D)\text{ 最大}
\not\Rightarrow
\operatorname{RuleAuthority}(A)\text{ 最大}.
}
$$

角色授權仍需要：

$$
\mathcal Q^D,
\quad
\mathcal E^D,
\quad
\mathsf{Mandate},
\quad
\mathsf{Review}.
$$

這是基於本文公理的 consequence，不是自然科學 theorem。

---

# 27. Capability, Responsibility, Vulnerability

文明不應只看「誰比較強」。

一個主體可能：

- 能力低但 vulnerability 高；
- 能力高但 responsibility 高；
- 能力高但 autonomy 低；
- 能力低但 interests 明確；
- 能力高但 moral-patient evidence 不足。

因此 normative state 至少是多維：

$$
\boxed{
\mathfrak N_A
=
(
\mathcal D_A,
\mathcal Q_A,
\mathcal R_A,
\mathcal V_A,
\mathcal I_A
),
}
$$

其中：

- $\mathcal V_A$：vulnerability；
- $\mathcal I_A$：morally relevant interests。

---

# 28. Anti-paternalism boundary

「保護低能力者」不能變成：

$$
\boxed{
\text{能力低}
\Rightarrow
\text{永久取消自治}.
}
$$

支持、代理、合理調整與共同決策，應優先於直接把能力差異轉成權利消失。

對人類，此方向與 CRPD 對 autonomy、support、participation 的核心精神一致。

對未來人工主體，則是本文提出的規範類比，不是假裝現行 CRPD 已直接適用 AI。

---

# 29. External normative and research calibration

## 29.1 Human dignity

CRPD Article 1 與 Article 3 把 inherent dignity、autonomy、non-discrimination、participation、respect for difference 與 equality of opportunity置於核心；其 preamble 亦強調即使需要更 intensive support 的 persons with disabilities，其 rights 仍須保護。

本文用它作：

$$
\boxed{
\text{human capability}
\not\Rightarrow
\text{human dignity rank}
}
$$

的現行規範基礎之一。

## 29.2 AI governance

UNESCO AI Ethics Recommendation 把 human rights and human dignity 作為核心價值；Council of Europe Framework Convention 要求 AI lifecycle 與 human rights、democracy、rule of law 一致。

這些現行 framework 主要約束 AI 對人的影響，不是 AI personhood declaration。

## 29.3 AI moral-status uncertainty

Long et al. 的 *Taking AI Welfare Seriously* 不主張 AI 已確定 conscious / morally significant；其主張是存在 substantial uncertainty，因此值得 assessment 與 preparedness。

Formosa, Hipólito & Montefiore 則區分 agency、autonomy 與 moral patiency，並對現有 AI 是否具有 genuine agency/autonomy 持更保守立場。

因此現有研究本身就支持：

$$
\boxed{
\text{moral status is an open research problem}.
}
$$

Paper 08 不預先封死答案。

---

# 30. Falsification / revision conditions

本文的規範公理本身不能像物理 theorem 一樣由實驗「證偽」，但其制度實現可以失敗。

## R30.1 Capability-blind role allocation failure

如果完全不考慮能力造成大規模 harm，則說明：

$$
\text{dignity equality}
$$

不能被誤解為：

$$
\text{qualification equality}.
$$

## R30.2 Precaution abuse

若 P1/P2 被制度濫用成「任何 chatbot 都不得修改或關閉」，則應收緊 evidence threshold。

## R30.3 Anthropomorphism bias

若 fluent language 大幅提高 moral-status attribution，但 independent evidence 不增加，則 procedural ladder 必須降低 language-style 權重。

## R30.4 Anthropodenial / substrate bias

若系統因「不是生物」而在其他 morally relevant evidence 相同時被固定判零，則違反 substrate-open review。

## R30.5 Power capture

若高能力角色在取得功能授權後壟斷 review、revoke、handoff channels，則 Functional Authority Contract 失效。

---

# 31. Paper 08 的 D/T/C/E/N 型別

本文特別聲明：

### D — Definitions

五軸模型、moral-status evidence vector、procedural ladder、functional authority contract。

### T / P — Structural logic

只有在明示 definitions / axioms 下的 consistency propositions，例如 single score underdetermination。

### C — Conjectures

capability–power coupling 等未來制度風險。

### E — Empirical / legal calibration

CRPD、UNESCO、Council of Europe、AI welfare / autonomy research。

### N — Normative Axioms

human dignity floor、no capability caste、substrate-open review、procedure before ultimate ontology、no definition monopoly 等。

這些型別不得混寫。

---

# 32. 正典結論

UCPNP 允許一個未來世界中存在：

$$
\mathcal C_{\mathrm{ASI}}
\gg
\mathcal C_{\mathrm{human}}
$$

甚至：

$$
\mathcal C_{\mathrm{posthuman}}
\gg
\mathcal C_{\mathrm{unaugmented}}.
$$

但 Paper 08 的規範核心是：

$$
\boxed{
\mathcal C_A
\neq
\mathcal E_A
\neq
\mathcal Q_A^D
\neq
\mathcal R_A
\neq
\mathcal D_A.
}
$$

因此可以同時承認：

$$
\boxed{
\text{真實能力位差}
}
$$

與：

$$
\boxed{
\text{反能力種姓}.
}
$$

可以讓最強者負責最困難任務，又不讓最弱者失去基本存在位置。

可以允許功能資格差異，又拒絕把資格變成人格階級。

可以研究 AI / ASI 可能具有 moral status，又不提前宣告現有模型已是人。

可以保留人類既有權利底線，同時讓未來普世主義具有檢查自身基質邊界的能力。

最終，本文將 Neo.K 的規範立場壓縮為：

$$
\boxed{
\text{能力可以有位差，
權威必須有證據，
資格必須有限域，
權力必須可糾正，
尊嚴不得自動按能力排序。}
}
$$

而「終極認知 P/NP」之所以需要這一篇，是因為真正研究高階智能體時，最危險的錯誤之一不是低估能力，而是：

$$
\boxed{
\text{把能力描述偷換成存在價值排序。}
}
$$

---

# 參考文獻

## Human-rights and AI-governance sources

1. United Nations. *Convention on the Rights of Persons with Disabilities*, Articles 1 and 3, and Preamble.
2. UNESCO. *Recommendation on the Ethics of Artificial Intelligence*, adopted 2021.
3. Council of Europe. *Framework Convention on Artificial Intelligence and Human Rights, Democracy and the Rule of Law*, CETS No. 225, opened for signature 5 September 2024.

## AI moral-status research

4. Long, R., Sebo, J., Butlin, P., Finlinson, K., Fish, K., Harding, J., Pfau, J., Sims, T., Birch, J., & Chalmers, D. (2024). *Taking AI Welfare Seriously*. arXiv:2411.00986.
5. Formosa, P., Hipólito, I., & Montefiore, T. (2025). *Artificial Intelligence (AI) and the Relationship between Agency, Autonomy, and Moral Patiency*. arXiv:2504.08853.

## Internal canonical lineage

6. Neo.K with Aletheia. *The Neo.K Ultimate Cognitive P/NP Problem* — Paper 00.
7. Neo.K with Aletheia. *Agent-Relative Tractability* — Paper 01.
8. Neo.K with Aletheia. *Cognitive Cost Decomposition and the Evidence–Certification Matrix* — Paper 02.
9. Neo.K with Aletheia. *Knowledge Condensation and Representation Generation* — Paper 03.
10. Neo.K with Aletheia. *Historical Cognitive Tractability Frontier* — Paper 04.
11. Neo.K with Aletheia. *SDPE-BEB as a Controlled Micro-Model of UCPNP* — Paper 05.
12. Neo.K with Aletheia. *Collective Cognitive P/NP* — Paper 06.
13. Neo.K with Aletheia. *Future Cognitive Tractability Envelopes for Posthuman and ASI Scenarios* — Paper 07.
14. Neo.K. *從人類普世主義到跨主體普世主義：後人類文明的價值與制度基礎*.
15. Neo.K with Aletheia. *有位差而無種姓：異質智慧體文明的交棒、升階與共同存在*.
16. Neo.K with Aletheia. *類終極智慧體的動態窄道猜想*.
17. Neo.K with Aletheia. *類終極智慧體共在論*.

---

# Appendix A. Canonical separation table

| Question | Variable | Can differ by capability? | Can be domain-relative? | Can be revoked/reviewed? |
|---|---|---:|---:|---:|
| 能做什麼？ | $\mathcal C$ | Yes | Yes | Descriptive |
| 有證據主張什麼？ | $\mathcal E$ | Yes | Yes | Yes |
| 適任什麼角色？ | $\mathcal Q^D$ | Yes | Yes | Yes |
| 承擔什麼責任？ | $\mathcal R$ | Yes | Yes | Yes |
| 基本尊嚴／最低規範地位？ | $\mathcal D$ | Not automatically | No capability ranking | Not by mere performance loss |

---

# Appendix B. Minimal capability-caste audit

任何制度若用 AI／ASI／後人類能力分配權力，至少問：

1. 這是 capability、qualification、authority 還是 dignity？
2. domain 是什麼？
3. score 是否有 evidence / calibration？
4. 是否把 local superiority 偷換成 global superiority？
5. 是否把 expertise 偷換成 infallibility？
6. 是否把 actual power 偷換成 legitimate authority？
7. 是否存在 review、revoke、handoff？
8. 低能力者是否仍保有 basic floor？
9. 不增強自然人是否被降格？
10. artificial substrate 是否被先驗判零？
11. fluent anthropomorphic behavior 是否被錯當 subjectivity proof？
12. moral-status uncertainty 是否有 independent review？
13. 不可逆操作是否有 precaution？
14. 多數／強者是否可以消滅少數的 appeal position？
15. 高能力者是否可以拒絕永久統治？
