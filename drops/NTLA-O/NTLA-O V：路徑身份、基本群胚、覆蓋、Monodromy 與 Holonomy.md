# NTLA-O V：路徑身份、基本群胚、覆蓋、Monodromy 與 Holonomy
## 從同端點異路徑到歷史敏感的觀察者運輸

**英文題名：** *NTLA-O V: Path Identity, Fundamental Groupoids, Coverings, Monodromy, and Holonomy — Toward History-Sensitive Observer Transport*  
**系列：** NTLA-O Series, Paper 6  
**版本：** v0.1 Formal Draft  
**前置論文：**《NTLA-O IV：局部—全域觀察、Presheaf、Sheaf、Stalk 與 Descent》  
**作者：** Neo.K  
**理論整理與形式化協作：** Aletheia / GPT-5.6 Sol  
**日期：** 2026-08-17

---

## 摘要

前四篇 NTLA-O 已建立：

$$
\text{Set}
\rightarrow
\text{Distinction Family}
\rightarrow
\text{Observer Topology}
\rightarrow
\text{Local Sections}
\rightarrow
\text{Gluing}.
$$

然而，即使局部資料完全相容並能被黏合，仍存在另一類資訊尚未處理：

> **一個 observer state 如何從某位置被運輸到另一位置？**

以及：

> **若起點與終點相同，但所經路徑不同，最終 observation state 是否仍應視為相同？**

這正是原 NTLA「洞不只是多少，而是怎麼連」思想最自然的代數拓樸接口。

本文首先區分多種路徑身份：

$$
\boxed{
\text{Raw Path}
}
$$

$$
\rightarrow
$$

$$
\boxed{
\text{Reparameterization Class}
}
$$

$$
\rightarrow
$$

$$
\boxed{
\text{Thin-Homotopy Class}
}
$$

$$
\rightarrow
$$

$$
\boxed{
\text{Endpoint-Fixed Homotopy Class}
}
$$

$$
\rightarrow
$$

$$
\boxed{
\text{Homological Information}.
}
$$

不同 quotient level 保留不同程度的生成歷史。

對一般拓樸空間 $X$，本文使用基本群胚：

$$
\Pi_1(X),
$$

其 objects 為點，morphisms 為端點固定同倫類。Fundamental group 與 covering-space lifting 是標準代數拓樸核心結構。

對 covering：

$$
p:\widetilde X\rightarrow X,
$$

路徑提升產生 fiber transport：

$$
T_{[\gamma]}:
p^{-1}(x)
\rightarrow
p^{-1}(y),
$$

並形成：

$$
\boxed{
T:\Pi_1(X)\rightarrow\mathbf{Set}.
}
$$

對 loop 則得到 monodromy action。這給出一個完全標準的數學例子：

$$
\boxed{
\text{same base endpoint}
\not\Rightarrow
\text{same lifted state}.
}
$$

本文再將 covering monodromy 與 connection holonomy 嚴格分離。一般 smooth connection 的 parallel transport 更自然由 thin path groupoid 描述；Schreiber 與 Waldorf 將 bundle connection 的 parallel transport 表述為從 path groupoid 到 fiber category 的 functor。

因此，「路徑差異」本身也具有 resolution hierarchy。

Fundamental groupoid 已經將端點固定同倫路徑商掉；若 NTLA 身份規格要求保留更細的實際歷史，則：

$$
\Pi_1(X)
$$

仍然太粗。

反之，若只取：

$$
H_1(X),
$$

則第一同調還會進一步遺失基本群中的非交換順序資訊。

因此本文提出：

$$
\boxed{
\operatorname{PathRes}(\mathcal O)
}
$$

作為觀察者的路徑身份解析度，並正式建立：

$$
\boxed{
\text{Observer Position}
\times
\text{Local State}
\times
\text{Path Transport}
}
$$

三軸結構。

**關鍵詞：** NTLA-O、路徑身份、基本群胚、覆蓋空間、path lifting、monodromy、holonomy、thin homotopy、parallel transport、觀察者歷史

---

# 1. 為什麼 Sheaf 還不夠？

Paper 5 建立：

$$
s_i\in\mathscr F(U_i)
$$

並研究：

$$
s_i|_{U_i\cap U_j}
=
s_j|_{U_i\cap U_j}.
$$

這回答的是：

> 不同局部域中的 observation states 是否相容？

但它沒有完整回答：

> 一個 state 從 $x$ 移動到 $y$ 時，是沿什麼路徑到達？

假設：

$$
x,y\in X
$$

並存在兩條路徑：

$$
\gamma_1,\gamma_2:
x\rightarrow y.
$$

即使：

$$
\gamma_1(0)=\gamma_2(0)=x,
$$

以及：

$$
\gamma_1(1)=\gamma_2(1)=y,
$$

仍可能：

$$
\boxed{
\gamma_1\neq\gamma_2.
}
$$

因此：

$$
\boxed{
\text{endpoint data}
}
$$

不包含完整：

$$
\boxed{
\text{path data}.
}
$$

---

# 2. Raw Path

設：

$$
X
$$

為拓樸空間。

從 $x$ 至 $y$ 的 path 為連續映射：

$$
\boxed{
\gamma:[0,1]\rightarrow X
}
$$

滿足：

$$
\gamma(0)=x,
$$

$$
\gamma(1)=y.
$$

所有此類路徑記為：

$$
\boxed{
P(x,y).
}
$$

最細的身份可以直接使用函數身份：

$$
\boxed{
\gamma_1
\equiv_{\mathrm{raw}}
\gamma_2
\iff
\gamma_1=\gamma_2
}
$$

作為映射相等。

---

# 3. Raw Path 通常太細

若只是改變走路速度，例如存在嚴格遞增的合法重新參數化：

$$
\phi:[0,1]\rightarrow[0,1]
$$

而：

$$
\gamma_2
=
\gamma_1\circ\phi,
$$

幾何軌跡並未真正改變。

某些研究可以選擇將其視為同一。

因此定義：

$$
\boxed{
\equiv_{\mathrm{rep}}
}
$$

為適當 reparameterization equivalence。

於是：

$$
\boxed{
\equiv_{\mathrm{raw}}
\subseteq
\equiv_{\mathrm{rep}}.
}
$$

換句話說，reparameterization quotient 已經丟掉一部分時間參數資訊。

---

# 4. 身份規格再次出現

NTLA-O 不預設哪一層才是真正身份。

而要求指定：

$$
\boxed{
\mathfrak I_{\mathrm{path}}.
}
$$

例如某問題可能認為：

$$
\gamma
$$

與：

$$
\gamma\circ\phi
$$

相同。

另一問題可能認為速度歷史本身重要，因此兩者不同。

所以：

$$
\boxed{
\text{path equality}
}
$$

本身也是 representation-relative。

---

# 5. Endpoint-Fixed Homotopy

對：

$$
\gamma_0,\gamma_1:x\rightarrow y,
$$

若存在：

$$
H:[0,1]\times[0,1]\rightarrow X
$$

使：

$$
H(s,0)=\gamma_0(s),
$$

$$
H(s,1)=\gamma_1(s),
$$

並且：

$$
H(0,t)=x,
$$

$$
H(1,t)=y,
$$

則稱兩路徑端點固定同倫：

$$
\boxed{
\gamma_0
\simeq_{\partial}
\gamma_1.
}
$$

此關係把可以連續變形成彼此、且端點保持不動的路徑識別。

---

# 6. Fundamental Groupoid

對拓樸空間 $X$，定義：

$$
\boxed{
\Pi_1(X).
}
$$

其：

### Objects

$$
\operatorname{Ob}\Pi_1(X)=X.
$$

### Morphisms

$$
\operatorname{Hom}_{\Pi_1(X)}(x,y)
=
P(x,y)/{\simeq_\partial}.
$$

即：

$$
\boxed{
[\gamma]:
x\rightarrow y.
}
$$

Composition 由路徑串接給出。

Inverse 由反向路徑：

$$
\bar\gamma(t)=\gamma(1-t)
$$

給出。

Fundamental group 與 covering spaces 是傳統代數拓樸中最基本的路徑結構之一。

---

# 7. Fundamental Group 是單點 Endomorphism

固定：

$$
x\in X.
$$

則：

$$
\boxed{
\pi_1(X,x)
=
\operatorname{Aut}_{\Pi_1(X)}(x).
}
$$

亦即：

$$
x\rightarrow x
$$

的 loop homotopy classes。

因此：

$$
\boxed{
\Pi_1(X)
}
$$

比單一：

$$
\pi_1(X,x)
$$

更適合 NTLA-O 多位置 observer。

因為 observer 可以分布於多個：

$$
x,y,z,\ldots
$$

而不必強迫所有路徑先回到同一 basepoint。

---

# 8. 觀察者路徑解析度

定義一組路徑等價關係：

$$
R
$$

作用於：

$$
P(x,y).
$$

對 observer $\mathcal O$，令：

$$
R_{\mathcal O}^{\mathrm{path}}
$$

表示它判定哪些路徑為同一。

若：

$$
R_A
\subseteq
R_B,
$$

則：

$$
A
$$

保留至少不低於 $B$ 的路徑差異。

因此定義：

$$
\boxed{
A
\preceq_{\mathrm{path}}
B
}
$$

當且僅當：

$$
R_B
\subseteq
R_A,
$$

沿用前文「更細 observer 在右側」的方向。

---

# 9. 路徑 Quotient Monotonicity

若：

$$
R_1\subseteq R_2,
$$

則存在自然滿射：

$$
\boxed{
P/R_1
\rightarrow
P/R_2.
}
$$

因此每增加一個合法 path-identification rule，就會進一步丟失歷史資訊。

---

# 定理 1：Path Quotient Information Monotonicity

若：

$$
R_1\subseteq R_2,
$$

則：

$$
\boxed{
|\,[\gamma]_{R_1}\text{ distinctions}\,|
\geq
|\,[\gamma]_{R_2}\text{ distinctions}\,|
}
$$

在有限情況下為普通基數比較；一般情況則理解為存在上述自然商映射。

因此：

$$
\boxed{
\text{coarser path identity}
\Rightarrow
\text{no more historical distinction}.
}
$$

---

# 10. Fundamental Groupoid 已經是一種歷史壓縮

因：

$$
\gamma_1\simeq_\partial\gamma_2
$$

時：

$$
[\gamma_1]
=
[\gamma_2]
$$

在：

$$
\Pi_1(X)
$$

中成立。

所以：

$$
\boxed{
\Pi_1(X)
}
$$

不保存 raw path history。

它只保存：

$$
\boxed{
\text{path identity modulo endpoint-fixed homotopy}.
}
$$

因此如果 NTLA 身份規格要求：

> 實際走過的軌跡不同就必須不同，

那：

$$
\boxed{
\Pi_1(X)
\text{ 太粗。}
}
$$

---

# 11. Covering Space

令：

$$
\boxed{
p:\widetilde X\rightarrow X
}
$$

為 covering map。

對：

$$
x\in X,
$$

定義 fiber：

$$
\boxed{
F_x
=
p^{-1}(x).
}
$$

covering spaces 的關鍵特性之一是 path lifting：給定 base path 與 fiber 中的起始點，存在唯一 lifted path。Hatcher 的 covering-space 章節以 lifting properties 作為核心結構。

---

# 12. Path Lifting

令：

$$
\gamma:[0,1]\rightarrow X
$$

且：

$$
\gamma(0)=x.
$$

取：

$$
\tilde x\in F_x.
$$

則存在唯一：

$$
\tilde\gamma:[0,1]\rightarrow\widetilde X
$$

使：

$$
p\circ\tilde\gamma=\gamma,
$$

且：

$$
\tilde\gamma(0)=\tilde x.
$$

因此可以定義：

$$
\boxed{
T_\gamma(\tilde x)
=
\tilde\gamma(1).
}
$$

若：

$$
\gamma:x\rightarrow y,
$$

則：

$$
\boxed{
T_\gamma:
F_x\rightarrow F_y.
}
$$

---

# 13. Lift Transport 是雙射

反向 path：

$$
\bar\gamma:y\rightarrow x
$$

提供逆 transport。

因此：

$$
\boxed{
T_{\bar\gamma}
=
T_\gamma^{-1}.
}
$$

所以：

$$
T_\gamma
$$

為 bijection。

---

# 14. Homotopy Invariance of Covering Transport

若：

$$
\gamma_0
\simeq_\partial
\gamma_1,
$$

則 covering homotopy lifting 保證具有相同起始 lift 的兩條 lifted paths 有相同終點。這是 covering-space lifting theory 的標準結果。

因此：

$$
\boxed{
T_{\gamma_0}
=
T_{\gamma_1}.
}
$$

所以 transport 只依賴：

$$
[\gamma]\in\Pi_1(X).
$$

---

# 15. Covering Transport Functor

因此可以定義：

$$
\boxed{
T_p:
\Pi_1(X)
\rightarrow
\mathbf{Set}
}
$$

使：

$$
x
\mapsto
F_x
$$

且：

$$
[\gamma]
\mapsto
T_{[\gamma]}.
$$

串接滿足：

$$
\boxed{
T_{[\delta]\circ[\gamma]}
=
T_{[\delta]}
\circ
T_{[\gamma]}.
}
$$

identity path 對應 identity function。

因此 covering 不只是「很多層」。

它是一個：

$$
\boxed{
\text{path-dependent observer-state transport system}.
}
$$

---

# 16. Monodromy

如果：

$$
\gamma:x\rightarrow x
$$

為 loop，

則：

$$
T_{[\gamma]}:
F_x\rightarrow F_x
$$

為 permutation。

因此得到：

$$
\boxed{
\rho_p:
\pi_1(X,x)
\rightarrow
\operatorname{Sym}(F_x).
}
$$

稱為 covering monodromy action／representation（依 convention 可表述成左或右作用）。

其重要意義是：

$$
\boxed{
\text{loop 的 base endpoint 不變，
但 fiber state 可以改變。}
}
$$

---

# 17. 圓的二重覆蓋

考慮：

$$
p:S^1\rightarrow S^1
$$

定義：

$$
\boxed{
p(z)=z^2.
}
$$

在：

$$
x=1
$$

上：

$$
F_1
=
\{1,-1\}.
$$

考慮 base loop：

$$
\gamma(t)
=
e^{2\pi it}.
$$

它從：

$$
1
$$

出發，繞圓一次後回到：

$$
1.
$$

以：

$$
\tilde\gamma(0)=1
$$

開始的 lift 為：

$$
\boxed{
\tilde\gamma(t)=e^{\pi it}.
}
$$

因此：

$$
\tilde\gamma(1)=-1.
$$

即：

$$
\boxed{
T_\gamma(1)=-1.
}
$$

---

# 18. Same Endpoint ≠ Same Lifted State

在 base space：

$$
\gamma(0)=\gamma(1)=1.
$$

但在 covering space：

$$
\tilde\gamma(0)=1,
$$

$$
\tilde\gamma(1)=-1.
$$

所以：

$$
\boxed{
\text{same base endpoint}
\not\Rightarrow
\text{same transported lifted state}.
}
$$

這是原 NTLA「結果位置同一不代表連接歷史同一」的一個非常標準數學模型。

---

# 定理 2：Nontrivial Monodromy Implies Endpoint Insufficiency

若存在：

$$
[\gamma]\in\pi_1(X,x)
$$

以及：

$$
\tilde x\in F_x
$$

使：

$$
T_{[\gamma]}(\tilde x)\neq\tilde x,
$$

則 base endpoint：

$$
x
$$

不足以唯一決定 lifted final state。

### 證明

constant path：

$$
c_x
$$

滿足：

$$
T_{[c_x]}(\tilde x)=\tilde x.
$$

而 loop：

$$
\gamma
$$

滿足：

$$
T_{[\gamma]}(\tilde x)\neq\tilde x.
$$

兩條 path 具有相同起終點：

$$
x\rightarrow x,
$$

但輸出不同。

故 endpoint data 不完備。

證畢。

---

# 19. Base Observer 與 Lifted Observer

考慮：

$$
p:\widetilde X\rightarrow X.
$$

若 base-level observer 只能讀：

$$
p(\tilde x),
$$

則：

$$
\tilde x_1,\tilde x_2
$$

只要：

$$
p(\tilde x_1)=p(\tilde x_2)
$$

便被商為同一。

所以：

$$
\boxed{
K_B
=
\{
(\tilde x_1,\tilde x_2):
p(\tilde x_1)=p(\tilde x_2)
\}.
}
$$

如果 lifted observer 可以直接讀取：

$$
\tilde x
$$

本身，

則：

$$
\boxed{
K_L
=
\Delta_{\widetilde X}.
}
$$

若存在非平凡 fiber：

$$
|F_x|>1,
$$

則：

$$
\boxed{
K_L\subsetneq K_B.
}
$$

---

# 定理 3：Covering Observer Refinement

若 covering 存在 fiber：

$$
|p^{-1}(x)|>1,
$$

則 identity-level lifted observer 比只讀 projection 的 base observer 具有嚴格更細的點級區分能力：

$$
\boxed{
K_L\subsetneq K_B.
}
$$

證畢。

注意：

這並不自動表示：

$$
L=I
$$

或：

$$
B=M.
$$

M/I/E 角色仍必須相對另外指定的 reference domain 判斷。

所以此例再次說明：

$$
\boxed{
\text{geometric level}
\neq
\text{observer role}
\neq
\text{observer resolution}.
}
$$

---

# 20. Monodromy 與 Observer Memory

考慮：

$$
\tilde x
\xrightarrow{\gamma}
T_\gamma(\tilde x).
$$

若：

$$
T_\gamma
$$

依賴 loop class，

則 final state 可以保留部分 path-history information。

因此可以定義：

$$
\boxed{
\operatorname{Mem}_{p}([\gamma],\tilde x)
=
T_{[\gamma]}(\tilde x).
}
$$

這不是心理學記憶。

而是：

$$
\boxed{
\text{transport state retains information about path class}.
}
$$

---

# 21. Monodromy 並不保存 Raw Path

因：

$$
\gamma_1\simeq_\partial\gamma_2
$$

會得到：

$$
T_{\gamma_1}=T_{\gamma_2}.
$$

因此 covering monodromy 最多保留：

$$
\boxed{
\text{homotopy-class information}
}
$$

中的某個 representation。

甚至不同：

$$
[\gamma_1]\neq[\gamma_2]
$$

也可能仍有：

$$
T_{\gamma_1}=T_{\gamma_2}.
$$

若 representation：

$$
\rho_p
$$

有非平凡 kernel。

所以：

$$
\boxed{
\text{monodromy output}
}
$$

通常又比：

$$
\boxed{
\pi_1
}
$$

更粗。

---

# 22. Monodromy Kernel

定義：

$$
\boxed{
K_{\mathrm{mon}}
=
\ker\rho_p
}
$$

亦即：

$$
[\gamma]
$$

在 fiber 上作用為 identity 的 loop classes。

因此：

$$
\boxed{
\pi_1(X,x)/K_{\mathrm{mon}}
}
$$

才是該 covering 真正能區分的 loop-action 結構。

所以：

$$
\boxed{
\text{topological path difference exists}
}
$$

並不推出：

$$
\boxed{
\text{this covering observes it}.
}
$$

這與整個 NTLA-O 的 observer-relative principle 完全一致。

---

# 23. 基本群仍然可能太細或太粗

若 observer 只讀：

$$
\rho_p([\gamma]),
$$

則：

$$
\pi_1
$$

中落在同一 monodromy permutation 的 classes 被商掉。

所以：

$$
\boxed{
\text{fundamental-group distinction}
}
$$

與：

$$
\boxed{
\text{observer-effective distinction}
}
$$

仍然不同。

反過來，如果研究要求保留 raw path geometry，

則：

$$
\pi_1
$$

本身又太粗。

---

# 24. 第一同調再進一步商掉非交換資訊

對 path-connected space $X$，經典的一維 Hurewicz 結果給出：

$$
\boxed{
H_1(X;\mathbb Z)
\cong
\pi_1(X,x)_{\mathrm{ab}},
}
$$

即第一同調群是基本群的 abelianization。這是標準代數拓樸結果。

因此 commutator：

$$
aba^{-1}b^{-1}
$$

在：

$$
H_1
$$

中成為零。

這意味著：

$$
ab
$$

與：

$$
ba
$$

在 abelianized information 中不再保有完整順序差異。

---

# 25. NTLA 連接順序的代數拓樸版本

如果原 NTLA 身份要求：

$$
\boxed{
a\rightarrow b
\neq
b\rightarrow a,
}
$$

則只保留：

$$
H_1
$$

可能過度粗化。

因為：

$$
H_1
$$

天然交換化。

所以：

$$
\boxed{
\text{homology equality}
}
$$

不能推出：

$$
\boxed{
\text{path-order identity}.
}
$$

這直接支持 NTLA 2.0 中「粗拓樸摘要不是完整身份」的修訂。

---

# 26. Loop Identity Resolution Tower

對 loop 可以建立：

$$
\boxed{
\text{Raw Loops}
}
$$

$$
\Downarrow
$$

$$
\boxed{
\text{Reparameterization Classes}
}
$$

$$
\Downarrow
$$

$$
\boxed{
\text{Thin-Homotopy Classes}
}
$$

$$
\Downarrow
$$

$$
\boxed{
\pi_1(X,x)
}
$$

$$
\Downarrow
$$

$$
\boxed{
H_1(X;\mathbb Z)
}
$$

$$
\Downarrow
$$

$$
\boxed{
\text{Selected Numerical Invariants}.
}
$$

每往下一層，都可能再商掉差異。

因此：

$$
\boxed{
\text{same lower-level invariant}
}
$$

一般不能反推出：

$$
\boxed{
\text{same higher-resolution path identity}.
}
$$

---

# 27. Thin Homotopy

進入 differential geometry 後，需要比普通 homotopy 更細的 path quotient。

粗略而言，smooth paths：

$$
\gamma_0,
\gamma_1
$$

若可以由一個不掃出真正二維面積的 homotopy 連接，稱為 thin-homotopic。

技術定義通常以 homotopy differential rank 限制形式給出。Thin homotopy 是研究 connection holonomy 與 higher gauge transport 的標準工具；Caetano–Picken 與後續 higher-gauge 文獻都使用這種結構。

記：

$$
\boxed{
\gamma_0
\simeq_{\mathrm{thin}}
\gamma_1.
}
$$

有：

$$
\boxed{
\simeq_{\mathrm{thin}}
\subseteq
\simeq_{\partial}.
}
$$

因為 thin homotopy 特別是一種 homotopy。

所以 thin quotient 比普通 fundamental-groupoid quotient 保留更多 path geometry。

---

# 28. Thin Path Groupoid

對 smooth manifold $M$，可以構造 thin path groupoid：

$$
\boxed{
\Pi_1^{\mathrm{thin}}(M).
}
$$

其 morphisms 為適當 smooth paths 的 thin-homotopy classes。

Schreiber–Waldorf 的 parallel-transport framework 正是把連接的 transport 與 path-groupoid functor 聯繫起來。

因此：

$$
\boxed{
\Pi_1^{\mathrm{thin}}(M)
}
$$

通常比：

$$
\boxed{
\Pi_1(M)
}
$$

保留更細路徑資訊。

---

# 29. Connection 與 Parallel Transport

令：

$$
\pi:E\rightarrow M
$$

為適當 smooth bundle，並具有 connection：

$$
\nabla.
$$

對一條 path：

$$
\gamma:x\rightarrow y,
$$

parallel transport 給出 fiber map：

$$
\boxed{
P_\gamma:
E_x
\rightarrow
E_y.
}
$$

Schreiber 與 Waldorf證明並系統化了：bundle connection 的 parallel transport 可以用 path-groupoid 上的 functor 描述，並可透過局部 trivialization 與 smooth descent data 表徵。

---

# 30. Covering Monodromy 與 Connection Holonomy 不能混為一談

兩者形式相似：

$$
\text{path}
\rightarrow
\text{fiber transformation}.
$$

但數學結構不同。

### Covering monodromy

主要依：

$$
[\gamma]\in\Pi_1(X)
$$

即普通 endpoint-fixed homotopy class。

### General connection transport

自然保留到：

$$
[\gamma]_{\mathrm{thin}}
$$

的更細 path information。

因此：

$$
\boxed{
\text{monodromy}
\neq
\text{general connection holonomy}.
}
$$

即使它們都可以被理解為 transport。

---

# 31. Holonomy

固定：

$$
x\in M.
$$

對 loop：

$$
\gamma:x\rightarrow x,
$$

parallel transport：

$$
P_\gamma:
E_x
\rightarrow
E_x
$$

稱為沿該 loop 的 holonomy transformation。

在 principal $G$-bundle 的適當 trivialization 下，可以對應到：

$$
\boxed{
\operatorname{Hol}(\gamma)\in G.
}
$$

Holonomy 的 thin-homotopy formulation 是 differential geometry 與 gauge theory 中成熟的做法。

---

# 32. Holonomy 正好描述「回到原點但狀態改變」

base path：

$$
\gamma(0)=\gamma(1)=x.
$$

然而：

$$
\boxed{
P_\gamma(v)
\neq v
}
$$

可能成立。

因此又得到：

$$
\boxed{
\text{same geometric basepoint}
\not\Rightarrow
\text{same transported internal state}.
}
$$

和 covering monodromy 相似，但這次差異可能包含 connection／curvature information，而非單純 covering sheet permutation。

---

# 33. Holonomy-Sensitive Observer

定義 observer：

$$
\mathcal O_{\mathrm{hol}}
$$

能讀取：

$$
P_\gamma.
$$

則兩條 loops：

$$
\gamma_1,\gamma_2
$$

可定義為：

$$
\boxed{
\gamma_1
\sim_{\mathrm{hol},\mathcal O}
\gamma_2
}
$$

若：

$$
P_{\gamma_1}
=
P_{\gamma_2}.
$$

因此得到：

$$
\boxed{
K_{\mathrm{hol},\mathcal O}.
}
$$

這又是一個 observer-specific quotient。

---

# 34. Holonomy 也不是 Raw History

即使：

$$
\gamma_1\neq\gamma_2
$$

也可能：

$$
P_{\gamma_1}
=
P_{\gamma_2}.
$$

所以：

$$
\boxed{
\text{Holonomy identity}
}
$$

不等於：

$$
\boxed{
\text{Raw path identity}.
}
$$

反過來：

$$
\gamma_1\simeq_{\mathrm{thin}}\gamma_2
$$

時，適當 connection transport 無法利用這兩條 thin-equivalent paths 產生新的 distinction。

因此：

$$
\boxed{
\text{transport formalism 本身也帶有 path-resolution ceiling}.
}
$$

---

# 35. NTLA-O Path Resolution

因此正式定義：

$$
\boxed{
\operatorname{PathRes}(\mathcal O)
}
$$

為 observer 所保留的 path identity resolution。

本文不要求它一定是單一整數。

更一般地可令：

$$
\operatorname{PathRes}(\mathcal O)
$$

指定一個路徑等價關係：

$$
R_{\mathcal O}^{\mathrm{path}}.
$$

兩 observers：

$$
A,B
$$

若：

$$
R_A
\subsetneq
R_B,
$$

則：

$$
A
$$

保留比 $B$ 更細的路徑歷史差異。

---

# 36. Endpoint Observer 是最粗的一種

定義：

$$
E_{\mathrm{end}}(\gamma)
=
(\gamma(0),\gamma(1)).
$$

則：

$$
\gamma_1
\sim_{\mathrm{end}}
\gamma_2
$$

只需：

$$
\gamma_1(0)=\gamma_2(0)
$$

且：

$$
\gamma_1(1)=\gamma_2(1).
$$

這是一個非常粗的 path observer。

---

# 37. Homotopy Observer

定義：

$$
E_{\pi_1}(\gamma)
=
[\gamma]_{\simeq_\partial}.
$$

則：

$$
K_{\pi_1}
$$

比 endpoint kernel 更細。

因為不同 homotopy classes 可以具有相同 endpoints。

所以：

$$
\boxed{
K_{\pi_1}
\subseteq
K_{\mathrm{end}}.
}
$$

若存在相同端點但不同 homotopy class 的 paths，則為嚴格包含。

---

# 38. Raw Observer

若：

$$
E_{\mathrm{raw}}(\gamma)=\gamma,
$$

則：

$$
K_{\mathrm{raw}}
=
\Delta_P.
$$

所以：

$$
\boxed{
K_{\mathrm{raw}}
\subseteq
K_{\mathrm{thin}}
\subseteq
K_{\pi_1}
\subseteq
K_{\mathrm{end}}
}
$$

在相應 path class 與 regularity 條件下成立。

這就是：

# **Path Observer Kernel Tower**

---

# 39. 差異第一次在哪一階被消失？

前面 NTLA 定義：

$$
r(x,y)
$$

為差異首次被看見的解析階。

現在路徑可定義另一個量：

$$
\boxed{
q(\gamma_1,\gamma_2)
}
$$

表示：

> 兩路徑第一次在哪個 quotient level 被識別為同一？

例如：

若：

$$
\gamma_1\neq_{\mathrm{raw}}\gamma_2
$$

但：

$$
\gamma_1
\equiv_{\mathrm{rep}}
\gamma_2,
$$

則差異在 reparameterization quotient 消失。

若：

$$
\gamma_1
\not\simeq_{\mathrm{thin}}
\gamma_2
$$

但：

$$
\gamma_1\simeq_\partial\gamma_2,
$$

則差異直到 ordinary homotopy quotient 才消失。

---

# 40. Difference Emergence 與 Difference Collapse

因此 NTLA-O 現在有兩個互補概念：

$$
\boxed{
r(x,y)
}
$$

——差異第一次被 observer 看見；

以及：

$$
\boxed{
q(\gamma_1,\gamma_2)
}
$$

——差異第一次被 quotient 商掉。

二者共同描述：

$$
\boxed{
\text{difference lifecycle}.
}
$$

---

# 41. Path Transport 與 Sheaf Descent 的連接

Paper 5 研究：

$$
\varphi_{ij}
$$

如何在 overlap 上轉換局部 states。

Paper 6 則研究：

$$
T_\gamma
$$

如何沿 path 運輸 states。

這兩者不是無關結構。

Schreiber–Waldorf 的 transport-functor framework 正是將 parallel transport、local trivializations 與 smooth descent data 放在統一範疇結構中。

因此 NTLA-O 可將：

$$
\boxed{
\text{local transition}
}
$$

與：

$$
\boxed{
\text{path transport}
}
$$

接成同一條幾何主線。

---

# 42. Observer Transport Structure

因此定義：

$$
\boxed{
\mathfrak T_{\mathcal O}
=
\left(
X,
\mathscr F,
\mathcal P,
\mathcal T
\right)
}
$$

其中：

- $X$：observer topology domain；
- $\mathscr F$：local observation states；
- $\mathcal P$：允許的 path groupoid／path category；
- $\mathcal T$：transport functor。

例如：

$$
\boxed{
\mathcal T:
\mathcal P
\rightarrow
\mathbf C
}
$$

其中：

$$
\mathbf C
$$

可以是：

- $\mathbf{Set}$；
- vector spaces；
- groups；
- torsors；
- fibers；
- observer-state categories。

---

# 43. Transport Functoriality

若：

$$
\gamma:x\rightarrow y
$$

及：

$$
\delta:y\rightarrow z,
$$

則合理 transport 必須滿足：

$$
\boxed{
T_{\delta\circ\gamma}
=
T_\delta
\circ
T_\gamma.
}
$$

以及：

$$
\boxed{
T_{\operatorname{id}_x}
=
\operatorname{id}_{F_x}.
}
$$

因此：

$$
\boxed{
\text{history composition}
}
$$

對應：

$$
\boxed{
\text{state transformation composition}.
}
$$

這是一個非常自然的 category-theoretic interface。

---

# 44. 非交換歷史

若存在 loops：

$$
a,b
$$

使：

$$
[a][b]\neq[b][a]
$$

在：

$$
\pi_1(X,x)
$$

中，

則：

$$
\boxed{
\text{path order matters}.
}
$$

如果 transport representation 也能區分：

$$
T_aT_b
\neq
T_bT_a,
$$

則 observer state 直接保留非交換歷史。

---

# 45. Homology 可能把這個順序消掉

進入：

$$
H_1
$$

後，

group operation 被交換化。

因此：

$$
[a]+[b]
=
[b]+[a].
$$

所以：

$$
\boxed{
\text{noncommutative path history}
}
$$

在：

$$
H_1
$$

層可能不可恢復。

這給 NTLA 連接順序一個很清楚的數學警告：

$$
\boxed{
\text{若 order 是身份的一部分，
不要只保存 abelianized invariant。}
}
$$

---

# 46. History-Sensitive NTLA Identity

因此將 NTLA 2.0 的身份規格：

$$
\mathfrak I
$$

擴充為：

$$
\boxed{
\mathfrak I
=
(
\mathfrak I_{\mathrm{state}},
\mathfrak I_{\mathrm{top}},
\mathfrak I_{\mathrm{path}},
\mathfrak I_{\mathrm{transport}}
).
}
$$

其中：

### State identity

看最終 state。

### Topological identity

看空間／連接拓樸。

### Path identity

看路徑在哪一 quotient level 保留。

### Transport identity

看路徑對 fiber／observer state 產生什麼作用。

---

# 47. 四種相同不應混在一起

可能：

$$
x_{\mathrm{final}}
=
y_{\mathrm{final}},
$$

但：

$$
[\gamma_x]
\neq
[\gamma_y].
$$

也可能：

$$
[\gamma_x]
=
[\gamma_y]
$$

在普通 homotopy level，

但：

$$
\gamma_x
\not\simeq_{\mathrm{thin}}
\gamma_y.
$$

還可能兩條非同倫 loops：

$$
[\gamma_x]\neq[\gamma_y]
$$

但某 covering representation：

$$
T_{\gamma_x}
=
T_{\gamma_y}.
$$

所以：

$$
\boxed{
\text{State Identity}
}
$$

$$
\neq
$$

$$
\boxed{
\text{Path Identity}
}
$$

$$
\neq
$$

$$
\boxed{
\text{Transport Identity}.
}
$$

---

# 48. 主／內／外角色加入 Transport

Paper 2 有：

$$
\rho_X(\mathcal O).
$$

Paper 5 加：

$$
(U,s_U).
$$

本篇再加入：

$$
\gamma
$$

及：

$$
T_\gamma.
$$

因此 observer state 可提升為：

$$
\boxed{
\mathbf O_{\mathrm{path}}
=
\left(
\rho_X(\mathcal O),
U,
s_U,
R_{\mathcal O}^{\mathrm{path}},
T
\right).
}
$$

若保留前文全部資料，可寫：

$$
\boxed{
\mathbf O^\ast
=
\left(
S,
\rho,
\mathcal A,
\tau,
K,
\preceq,
\mathscr F,
R_{\mathrm{path}},
T
\right).
}
$$

---

# 49. 角色變化與路徑變化仍然不同

observer 可以：

$$
\rho_X(\mathcal O)=I
$$

始終不變，

但它沿內部 path：

$$
\gamma
$$

被 transport：

$$
s
\mapsto
T_\gamma(s).
$$

所以：

$$
\boxed{
\text{state transport}
\not\Rightarrow
\text{role transition}.
}
$$

同樣角色改變：

$$
I\rightarrow M
$$

也不自動表示：

$$
T_\gamma
$$

發生任何非平凡變換。

---

# 50. 高階路徑邊界

Fundamental groupoid 把 paths 作為 morphisms。

但若還要區分：

$$
H_1,H_2:
\gamma_1\Rightarrow\gamma_2
$$

這些不同 homotopies，

則 ordinary groupoid 又不夠。

需要進入：

$$
\boxed{
2\text{-groupoid}
}
$$

甚至：

$$
\boxed{
\infty\text{-groupoid}.
}
$$

Higher-gauge theory 已使用 path $2$-groupoids 與 $2$-functors描述曲線與曲面上的更高 parallel transport。

HoTT 亦將點、路徑、路徑之間的路徑等 iterated identity structure 視為高階群胚式結構的重要直覺。

---

# 51. NTLA-O 不預設必須保留到無限高階

這一點尤其重要。

NTLA-O 不宣稱：

$$
\boxed{
\text{任何應用都必須完整保存 }\infty\text{-groupoid}.
}
$$

而是要求：

$$
\boxed{
\text{身份規格必須說明在哪個 truncation level 停止。}
}
$$

例如某應用只需要：

$$
H_1.
$$

某應用需要：

$$
\pi_1.
$$

某 differential-geometric application 可能需要：

$$
\Pi_1^{\mathrm{thin}}.
$$

某 higher-gauge application 才需要：

$$
\Pi_2.
$$

---

# 52. Path Truncation Level

因此可以定義：

$$
\boxed{
\operatorname{TruncPath}(\mathcal O)
}
$$

描述 observer 把 path/higher-path structure 保留到哪一階。

但此量不應被簡單理解成：

$$
0<1<2<3
$$

就必然「越高越好」。

更高 resolution 具有更高資訊保留與計算成本。

所以：

$$
\boxed{
\text{resolution}
\neq
\text{utility}.
}
$$

---

# 53. 一個完整的 NTLA 路徑身份階梯

因此本文建議：

$$
\boxed{
\mathcal P_{\mathrm{raw}}
}
$$

$$
\Downarrow
$$

$$
\boxed{
\mathcal P_{\mathrm{rep}}
}
$$

$$
\Downarrow
$$

$$
\boxed{
\Pi_1^{\mathrm{thin}}
}
$$

$$
\Downarrow
$$

$$
\boxed{
\Pi_1
}
$$

$$
\Downarrow
$$

$$
\boxed{
H_1
}
$$

$$
\Downarrow
$$

$$
\boxed{
\text{application-specific summary}.
}
$$

其中每一箭頭都是：

$$
\boxed{
\text{information-losing quotient / functor}
}
$$

的候選。

---

# 54. 路徑觀察與 NTLA 原命題

原始 NTLA 的直覺：

> 洞數相同，連法不同，仍可能不同。

現在可以升級成：

> 節點、洞、起點、終點全部相同，若路徑 class、transport action 或高階 history 不同，仍可能依身份規格被判為不同。

因此：

$$
\boxed{
\text{same objects}
+
\text{same endpoints}
}
$$

仍然不推出：

$$
\boxed{
\text{same NTLA identity}.
}
$$

完整身份至少可能依賴：

$$
\boxed{
\text{objects}
+
\text{connections}
+
\text{nesting}
+
\text{path classes}
+
\text{transport}.
}
$$

---

# 55. 本篇核心定理群

本文得到：

### 定理 A：Path Quotient Information Monotonicity

若：

$$
R_1\subseteq R_2,
$$

則存在：

$$
P/R_1\rightarrow P/R_2
$$

自然滿射。

### 定理 B：Covering Transport Functor

covering path lifting 誘導：

$$
\boxed{
T_p:\Pi_1(X)\rightarrow\mathbf{Set}.
}
$$

### 定理 C：Nontrivial Monodromy Implies Endpoint Insufficiency

非平凡 monodromy 推出：

$$
\boxed{
\text{endpoint data cannot determine lifted state}.
}
$$

### 定理 D：Covering Observer Refinement

非平凡 fiber 下：

$$
\boxed{
K_L\subsetneq K_B.
}
$$

### 定理 E：Fundamental Groupoid History Loss

端點固定同倫的 paths 在：

$$
\Pi_1
$$

中無法區分。

### 定理 F：Homological Abelianization Loss

對 path-connected $X$：

$$
H_1(X;\mathbb Z)
\cong
\pi_1(X,x)_{\mathrm{ab}},
$$

因此非交換 path-order information 可能被消除。

### 結構 G：Connection Transport Functor

smooth bundle connection 的 parallel transport 可由 path-groupoid functor 表述。

---

# 56. 與傳統數學的界線

本文使用的：

- paths；
- homotopies；
- fundamental group；
- fundamental groupoid；
- covering spaces；
- path lifting；
- monodromy；
- $H_1$；
- parallel transport；
- holonomy；
- thin homotopy；
- higher path groupoid；

均有既有拓樸、微分幾何或 higher-categorical 理論背景。

NTLA-O 不宣稱發明這些結構。

本文自己的 candidate contribution 仍然位於耦合：

$$
\boxed{
\text{Observer Role}
}
$$

$$
+
$$

$$
\boxed{
\text{Observer Kernel}
}
$$

$$
+
$$

$$
\boxed{
\text{Path Identity Resolution}
}
$$

$$
+
$$

$$
\boxed{
\text{Transport Action}
}
$$

$$
+
$$

$$
\boxed{
\text{Explicit Identity Specification}.
}
$$

---

# 57. 理論強度聲明

本文不宣稱：

- 現實中的所有歷史都可由 fundamental groupoid 完整描述；
- 所有路徑差異都具有物理意義；
- raw path 永遠應被保存；
- homotopic paths 必然在所有系統中等效；
- holonomy 等價於記憶；
- monodromy 等價於認知；
- 高階群胚一定是 AI 的內部資料結構；
- 路徑解析度越高的 observer 就越聰明。

本文只提出：

> 當研究對象的身份依賴連接與運輸歷史時，path/groupoid/transport structures 提供比單純 endpoint、Betti number 或 homology summary 更適當的數學語言。

---

# 58. 本篇結論

NTLA-O 到這一階正式獲得第三條數學軸。

第一條是：

$$
\boxed{
\text{Locality Axis}
}
$$

$$
U\supseteq V
\rightarrow
\mathscr F(U)\rightarrow\mathscr F(V)
\rightarrow
\mathscr F_x.
$$

第二條是：

$$
\boxed{
\text{Resolution Axis}
}
$$

$$
K_0
\supseteq
K_1
\supseteq
K_2
\supseteq
\cdots.
$$

第三條則是本篇新增的：

$$
\boxed{
\text{Transport Axis}
}
$$

$$
x
\xrightarrow{\gamma}
y
$$

以及：

$$
\boxed{
F_x
\xrightarrow{T_\gamma}
F_y.
}
$$

因此 NTLA-O 已經不再只是「套娃 topology」。

而成為：

$$
\boxed{
\text{where}
\times
\text{what can be distinguished}
\times
\text{how states move}.
}
$$

更完整地：

$$
\boxed{
\text{Role}
\times
\text{Locality}
\times
\text{Resolution}
\times
\text{Transport}.
}
$$

其中最重要的結論是：

$$
\boxed{
\text{same endpoint}
\not\Rightarrow
\text{same path}
}
$$

$$
\boxed{
\text{same path homotopy class}
\not\Rightarrow
\text{same raw history}
}
$$

以及：

$$
\boxed{
\text{different path classes}
\not\Rightarrow
\text{a particular observer distinguishes them}.
}
$$

所以「不同」必須永遠指定：

$$
\boxed{
\text{在哪一個 path-resolution level，
由哪個 observer，
依哪一個 transport representation 判定。}
}
$$

這正是 NTLA 原本「每一次連接只要存在有效差異，就應保持不同身份」在代數拓樸中的正式版本。

---

# 59. 下一篇

目前我們已有：

$$
\boxed{
\text{local restrictions}
}
$$

的 direct-limit 方向，

以及：

$$
\boxed{
\text{path transport}
}
$$

的 groupoid 方向。

下一篇將正式處理第三種早已出現、但尚未完整封裝的結構：

$$
\boxed{
K_0
\supseteq
K_1
\supseteq
K_2
\supseteq
\cdots.
}
$$

由此形成：

$$
\boxed{
X/K_0
\leftarrow
X/K_1
\leftarrow
X/K_2
\leftarrow
\cdots.
}
$$

並進入：

# **NTLA-O VI：逆系統、Observer Tower、Inverse Limit 與 Pro-Observer Identity**

其核心問題將是：

> **如果兩個系統最後的 inverse limit 相同，但它們「差異在哪一階出現、又在哪一階被商掉」的整個歷史不同，它們是否仍應被 NTLA-O 判為同一？**

答案將導向：

$$
\boxed{
\text{Limit Identity}
\neq
\text{Tower Identity}.
}
$$

這會把 NTLA 的「結果相同不等於生成歷史相同」正式推進到 inverse-system 層級。

---

# 參考文獻

1. Hatcher, A. *Algebraic Topology*, Chapter 1: Fundamental Group and Covering Spaces.
2. Hatcher, A. *Algebraic Topology*, covering-space lifting properties and homotopy lifting.
3. Schreiber, U., & Waldorf, K. (2009). *Parallel Transport and Functors*. Journal of Homotopy and Related Structures 4(1), 187–244.
4. Caetano, A., & Picken, R. F. (1994). *An Axiomatic Definition of Holonomy*. International Journal of Mathematics 5, 835–848.
5. Baez, J., & Schreiber, U. *Higher Gauge Theory*. Thin homotopy and higher holonomy structures.
6. Schreiber, U., & Waldorf, K. *Local Theory for 2-Functors on Path 2-Groupoids*.
7. The Univalent Foundations Program. *Homotopy Type Theory: Univalent Foundations of Mathematics*.
8. Neo.K & Aletheia (2026). *NTLA-O IV：局部—全域觀察、Presheaf、Sheaf、Stalk 與 Descent*.

---

**文件狀態：** Formal Draft v0.1  
**系列位置：** NTLA-O Series Paper 6 / 9  
**下一篇：** NTLA-O VI — Inverse Systems, Observer Towers, Inverse Limits, and Pro-Observer Identity