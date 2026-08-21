# NTLA-O VII：完備分離、Canonical Invariants、局部有限重建與 Continuous Separation Problem
## 從有限結構的完整身份碼到無界局部觀察的全域完備性

**英文題名：** *NTLA-O VII: Complete Separation, Canonical Invariants, Locally Finite Reconstruction, and the Continuous Separation Problem*  
**系列：** NTLA-O Series, Paper 8  
**版本：** v0.1 Formal Draft  
**前置論文：**《NTLA-O VI：逆系統、Observer Tower、Inverse Limit 與 Pro-Observer Identity》  
**作者：** Neo.K  
**理論整理與形式化協作：** Aletheia / GPT-5.6 Sol  
**日期：** 2026-08-17

---

## 摘要

NTLA-O 前六篇已建立：

$$
\boxed{
\text{Role}
\times
\text{Locality}
\times
\text{Resolution}
\times
\text{Transport}
}
$$

並以 observer kernel：

$$
K_{\mathcal O}
$$

描述相對觀察不可區分性。

但整個理論仍缺少一個最核心的問題：

> **如果 NTLA 宣稱兩個結構不同，我們是否真的能構造某種觀察，使它們必然被分開？**

本文稱此問題為 **Complete Separation Problem**。

第一部分限制於有限 NTLA 關係結構。對固定有限關係 signature $\Sigma$，本文將所有合法重標號後的完整結構編碼取字典序最小值，定義：

$$
\operatorname{Can}_{\Sigma}(\mathbb C).
$$

並證明：

$$
\boxed{
\operatorname{Can}_{\Sigma}(\mathbb C_1)
=
\operatorname{Can}_{\Sigma}(\mathbb C_2)
\iff
\mathbb C_1\cong_{\Sigma}\mathbb C_2.
}
$$

因此在有限結構域，NTLA-O 確實存在 complete separator。

Complete invariant 與 canonical form 是圖同構／canonization 文獻中的標準概念；但 complete invariant 的存在或暴力構造不等於高效率 canonization，後者本身是一個非平凡算法問題。

第二部分處理連通、根化、局部有限、有限 signature 的可數 NTLA 結構。令：

$$
B_n(\mathbb C,o)
$$

為以根 $o$ 為中心的半徑 $n$ 有限觀察球。

若兩個結構對所有有限 $n$ 都有：

$$
\operatorname{Can}
\left(
B_n(\mathbb C,o)
\right)
=
\operatorname{Can}
\left(
B_n(\mathbb D,p)
\right),
$$

則本文利用有限部分同構所形成的有限分枝樹與 König 型緊緻性論證證明：

$$
\boxed{
(\mathbb C,o)
\cong
(\mathbb D,p).
}
$$

因此，在此限制類別中：

$$
\boxed{
\text{all finite-radius complete observations}
}
$$

足以決定：

$$
\boxed{
\text{global structural identity}.
}
$$

局部有限性不能無條件刪除。Martineau 構造了非局部有限的 Cayley graphs，使任意有限半徑的對應球皆同構，但整體圖仍不同構。

第三部分因此不宣稱得到一般連續拓樸分類定理，而提出：

# **NTLA-O Continuous Separation Problem**

給定一類拓樸／幾何結構 $\mathfrak C$ 與指定身份關係 $\equiv_\ast$，尋找一族合法、最好可計算且穩定的不變量：

$$
F_0,F_1,F_2,\ldots
$$

使：

$$
\boxed{
x\equiv_\ast y
\iff
\forall n,\;
F_n(x)=F_n(y).
}
$$

現有研究亦表明，單一 persistence diagram 遠非所有資料類別的完整描述；更豐富的 distributed-persistence families 在特定點雲模型上可以建立 inverse results。這支持本文採取「完整性必須相對指定對象類別證明」的立場。

**關鍵詞：** NTLA-O、complete invariant、canonical form、結構同構、局部有限、局部—全域重建、König lemma、observer completeness、continuous separation

---

# 1. 從「有差異」到「能完整證明差異」

NTLA 2.0 引入身份規格：

$$
\mathfrak I.
$$

因此可以說：

$$
x\not\equiv_{\mathfrak I}y.
$$

但這仍然只是身份定義。

NTLA-O 真正需要回答：

$$
\boxed{
x\not\equiv_{\mathfrak I}y
\Longrightarrow
\exists\mathcal O:
x\not\sim_{\mathcal O}y?
}
$$

若答案永遠成立，才可以稱 observer system 對指定身份關係為完備。

---

# 2. Complete Observer

令：

$$
\Omega
$$

為研究對象域。

令：

$$
\equiv_\ast
$$

為指定結構身份關係。

## 定義 2.1

觀察者：

$$
\mathcal O
$$

稱為相對：

$$
\equiv_\ast
$$

的 complete observer，若：

$$
\boxed{
K_{\mathcal O}
=
\equiv_\ast.
}
$$

也就是：

$$
E_{\mathcal O}(x)=E_{\mathcal O}(y)
$$

當且僅當：

$$
x\equiv_\ast y.
$$

---

# 3. Complete Separator

更一般地，函數：

$$
F:\Omega\rightarrow Y
$$

稱為：

# **Complete Separator**

若：

$$
\boxed{
F(x)=F(y)
\iff
x\equiv_\ast y.
}
$$

因此：

$$
\ker F
=
\equiv_\ast.
$$

一旦找到：

$$
F,
$$

便可令：

$$
E_{\mathcal O}=F
$$

構造 complete observer。

---

# 4. Separating Family

有時單一不變量難以直接構造。

令：

$$
\mathcal F
=
\{f_\alpha\}_{\alpha\in A}.
$$

定義聯合觀察：

$$
\boxed{
F_{\mathcal F}(x)
=
\left(
f_\alpha(x)
\right)_{\alpha\in A}.
}
$$

---

# 定理 1：Separating Family Criterion

如果：

$$
x\not\equiv_\ast y
$$

必存在：

$$
\alpha\in A
$$

使：

$$
f_\alpha(x)\neq f_\alpha(y),
$$

且每個：

$$
f_\alpha
$$

都在：

$$
\equiv_\ast
$$

等價類上保持不變，

則：

$$
\boxed{
\ker F_{\mathcal F}
=
\equiv_\ast.
}
$$

### 證明

若：

$$
x\equiv_\ast y,
$$

由 invariant 條件：

$$
f_\alpha(x)=f_\alpha(y)
$$

對所有 $\alpha$ 成立。

所以：

$$
F_{\mathcal F}(x)
=
F_{\mathcal F}(y).
$$

反之若：

$$
x\not\equiv_\ast y,
$$

由 separating property，存在 $\alpha$ 使：

$$
f_\alpha(x)\neq f_\alpha(y).
$$

因此：

$$
F_{\mathcal F}(x)
\neq
F_{\mathcal F}(y).
$$

證畢。

---

# 5. 完備性永遠是相對身份規格

若：

$$
\equiv_\ast
=
=
$$

表示 rigid literal identity，

所需 separator 與：

$$
\equiv_\ast
=
\cong
$$

表示結構同構，

完全不同。

同理：

$$
\equiv_{\mathrm{homeo}},
$$

$$
\equiv_{\mathrm{homotopy}},
$$

$$
\equiv_{\mathrm{path}},
$$

$$
\equiv_{\mathrm{tower}}
$$

各自需要不同 complete separator。

因此禁止寫：

$$
\boxed{
F
\text{ 是完整不變量}
}
$$

卻不說明：

$$
\boxed{
\text{complete for what equivalence?}
}
$$

---

# 6. 有限 NTLA 關係結構

固定有限 relational signature：

$$
\boxed{
\Sigma
=
\{
R_\alpha
\}_{\alpha\in A}
}
$$

其中每個：

$$
R_\alpha
$$

具有有限 arity：

$$
k_\alpha.
$$

定義有限 NTLA 結構：

$$
\boxed{
\mathbb C
=
\left(
H,
\{R_\alpha^{\mathbb C}\}_{\alpha\in A},
\Lambda
\right)
}
$$

其中：

$$
|H|=n<\infty.
$$

$\Lambda$ 可以透過：

- unary relations；
- distinguished constants；
- typed relation symbols；

等標準有限結構方式納入 signature。

---

# 7. 洞—連接—嵌套作為有限 Signature

例如可取：

$$
\Sigma_{\mathrm{NTLA}}
=
\{
E,N,D,L,\ldots
\}.
$$

其中：

$$
E(x,y)
$$

表示連接；

$$
N(x,y)
$$

表示嵌套；

$$
D(x,y)
$$

表示有向關係；

$$
L_i(x)
$$

表示型別或標籤。

如果 finite-history information 必須保留，也可以把所需歷史資料編碼進額外 relations。

因此：

$$
\boxed{
\text{finite NTLA identity}
}
$$

可以先被降成：

$$
\boxed{
\text{finite relational-structure identity}.
}
$$

---

# 8. 結構同構

兩個：

$$
\Sigma
$$

結構：

$$
\mathbb C,
\mathbb D
$$

稱為同構：

$$
\boxed{
\mathbb C
\cong_\Sigma
\mathbb D
}
$$

若存在雙射：

$$
f:H_{\mathbb C}
\rightarrow
H_{\mathbb D}
$$

使所有指定 relations、constants、types 均被保存。

這允許忽略純粹重新命名。

---

# 9. Rigidity 必須另外指定

若 node 名稱本身具有不可交換身份，

可以透過 distinguished labels 將其編碼進：

$$
\Sigma.
$$

此時合法同構必須保存這些 labels。

因此：

$$
\boxed{
\text{structural identity}
}
$$

與：

$$
\boxed{
\text{rigid named identity}
}
$$

不需要另造兩套數學。

只需改變：

$$
\boxed{
\Sigma
}
$$

所要求保存的資料。

---

# 10. 完整序列化

固定：

1. relation symbols 的總順序；
2. 每種 tuple 的字典序；
3. label encoding；
4. 一個有限 alphabet。

對任意雙射：

$$
\sigma:
H
\rightarrow
[n]
$$

將：

$$
\mathbb C
$$

重新標號到：

$$
[n]
=
\{1,\ldots,n\}.
$$

再依固定格式把全部 relation tables 寫成有限字串：

$$
\boxed{
\operatorname{Enc}_{\sigma}(\mathbb C).
}
$$

因結構有限，所以候選編碼只有有限個。

---

# 11. Canonical Structural Code

定義：

$$
\boxed{
\operatorname{Can}_{\Sigma}(\mathbb C)
=
\min_{\sigma:H\rightarrow[n]}
\operatorname{Enc}_{\sigma}(\mathbb C)
}
$$

其中 minimum 取字典序。

它表示：

> 在所有合法重新命名方式中，選擇唯一最小的完整結構表示。

Complete invariant 與 canonical form 正是有限結構／圖同構研究中的標準區分：complete invariant 在同構時且僅在同構時相等，而 canonical form 則提供同構類的規範代表。

---

# 定理 2：Finite NTLA Canonical Completeness

對兩個有限 $\Sigma$-NTLA 結構：

$$
\mathbb C,
\mathbb D,
$$

有：

$$
\boxed{
\operatorname{Can}_{\Sigma}(\mathbb C)
=
\operatorname{Can}_{\Sigma}(\mathbb D)
\iff
\mathbb C
\cong_\Sigma
\mathbb D.
}
$$

### 證明

先假設：

$$
\mathbb C
\cong_\Sigma
\mathbb D.
$$

令：

$$
f:
H_{\mathbb C}
\rightarrow
H_{\mathbb D}
$$

為同構。

每一個 $\mathbb C$ 的標號：

$$
\sigma
$$

對應到 $\mathbb D$ 的標號：

$$
\sigma\circ f^{-1}.
$$

由 $f$ 保存全部 $\Sigma$-structure：

$$
\operatorname{Enc}_\sigma(\mathbb C)
=
\operatorname{Enc}_{\sigma\circ f^{-1}}(\mathbb D).
$$

所以兩者全部可能編碼集合相同。

故其最小元素相同。

反方向，若：

$$
\operatorname{Can}_{\Sigma}(\mathbb C)
=
\operatorname{Can}_{\Sigma}(\mathbb D),
$$

則存在標號：

$$
\sigma,
\tau
$$

使：

$$
\operatorname{Enc}_{\sigma}(\mathbb C)
=
\operatorname{Enc}_{\tau}(\mathbb D).
$$

因 encoding 完整記錄全部 relations，

$$
\tau^{-1}\circ\sigma
$$

保存全部：

$$
\Sigma
$$

結構。

故：

$$
\mathbb C\cong_\Sigma\mathbb D.
$$

證畢。

---

# 12. 有限 Complete Observer 存在

定義：

$$
E_{\mathrm{can}}(\mathbb C)
=
\operatorname{Can}_{\Sigma}(\mathbb C).
$$

則由定理 2：

$$
\boxed{
K_{\mathrm{can}}
=
\cong_\Sigma.
}
$$

因此：

---

# 推論 2.1：Finite Complete Observer Existence

對固定有限 signature 下的有限 NTLA 結構：

$$
\boxed{
\text{存在相對結構同構的 complete observer}.
}
$$

---

# 13. 這第一次真正完成「有差異就能分」

如果：

$$
\mathbb C
\not\cong_\Sigma
\mathbb D,
$$

則：

$$
\boxed{
\operatorname{Can}_{\Sigma}(\mathbb C)
\neq
\operatorname{Can}_{\Sigma}(\mathbb D).
}
$$

因此只要某個：

- 洞；
- 連接；
- 嵌套；
- 方向；
- label；
- finite history relation；

已經被寫進：

$$
\Sigma,
$$

那麼其任何真正非同構差異都一定能被 canonical observer 分離。

這是有限 NTLA 上的完整版本。

---

# 14. 但是「沒被編碼的差異」仍然不存在於此身份規格

如果：

$$
\Sigma
$$

沒有保存實際 path history，

兩個不同 raw histories 可能仍產生相同有限 relational structure。

Canonical code 不可能恢復從未進入輸入的資訊。

因此：

$$
\boxed{
\text{complete relative to }\Sigma
}
$$

不能偷換成：

$$
\boxed{
\text{complete relative to every imaginable identity}.
}
$$

---

# 15. 完備不等於高效率

定理 2 的暴力實作可以枚舉：

$$
n!
$$

個標號。

因此它首先證明：

$$
\boxed{
\text{existence of a complete canonical separator}.
}
$$

不是：

$$
\boxed{
\text{efficient canonization}.
}
$$

一般圖同構已有遠比暴力搜尋高明的算法研究；例如 Babai 證明一般 graph isomorphism 可在 quasipolynomial time 解決，而 canonical forms／labeling 的效率亦有獨立文獻。

因此 NTLA-O 必須永久分開：

$$
\boxed{
\text{classification completeness}
}
$$

與：

$$
\boxed{
\text{classification complexity}.
}
$$

---

# 16. 快速但不完整的不變量仍有價值

可以先定義較便宜：

$$
F_0,
F_1,\ldots
$$

例如：

$$
F_0
=
\text{size/count information},
$$

$$
F_1
=
(F_0,\beta_\ast),
$$

$$
F_2
=
(F_1,H_\ast),
$$

$$
F_3
=
(F_2,\text{nesting summary}),
$$

$$
\cdots
$$

最終必要時才計算：

$$
F_\ast
=
\operatorname{Can}_{\Sigma}.
$$

這形成：

$$
\boxed{
\text{cheap coarse filtering}
\rightarrow
\text{expensive complete classification}.
}
$$

---

# 17. Cumulative Feature Tower

令：

$$
F_{n+1}
=
(F_n,g_{n+1}).
$$

則存在 projection：

$$
p_{n+1,n}
$$

使：

$$
F_n
=
p_{n+1,n}\circ F_{n+1}.
$$

因此 observer kernels：

$$
K_n
=
\ker F_n
$$

滿足：

$$
\boxed{
K_{n+1}\subseteq K_n.
}
$$

這重新接回 Paper 7 的 inverse observer tower。

---

# 18. 完整層

若存在：

$$
N
$$

使：

$$
F_N
$$

已是 complete separator，

則：

$$
\boxed{
K_N
=
\equiv_\ast.
}
$$

若之後 feature layers 只增加冗餘資訊：

$$
K_n=K_N
$$

對所有：

$$
n\geq N.
$$

此時 point-identity resolution 已 stabilization。

---

# 19. 無有限 Complete Layer 的情況

另一種可能是：

$$
K_n
supsetneq
K_{n+1}
$$

持續發生，

而：

$$
\boxed{
\bigcap_nK_n
=
\equiv_\ast.
}
$$

此時沒有單一有限 level 完整，

但整個無界 observer tower 完整。

這就是：

# **Asymptotic Observer Completeness**

---

# 20. 局部有限無限結構

現在進入可數無限情況。

令：

$$
(\mathbb C,o)
$$

為：

- 根化；
- 連通；
- 有限 relational signature；
- locally finite；

的 NTLA relational structure。

---

# 21. Gaifman Graph

對 relational structure：

$$
\mathbb C,
$$

構造 Gaifman graph：

$$
G_{\mathbb C}.
$$

兩個不同元素：

$$
x,y
$$

若共同出現在某個 relation tuple 中，就在 Gaifman graph 中相鄰。

因此 relational locality 可以被轉成 graph distance。

---

# 22. Local Finiteness

稱：

$$
\mathbb C
$$

locally finite，若其 Gaifman graph 每個 vertex 都具有有限 degree。

由此，對任意有限：

$$
n,
$$

以：

$$
o
$$

為根的閉球：

$$
\boxed{
B_n(\mathbb C,o)
}
$$

都是有限集合。

因為：

$$
B_0
$$

有限，

而每個有限球只有有限多個有限度鄰居。

---

# 23. 根化有限 Ball 的 Canonical Code

將 root：

$$
o
$$

作為 distinguished constant 寫入 signature。

於是每個：

$$
B_n(\mathbb C,o)
$$

皆為有限 rooted $\Sigma$-structure。

可以使用前面的 canonical code：

$$
\boxed{
c_n(\mathbb C,o)
=
\operatorname{Can}
\left(
B_n(\mathbb C,o)
\right).
}
$$

---

# 24. Local Observation Signature

定義：

$$
\boxed{
\mathbf C_{\mathrm{loc}}(\mathbb C,o)
=
(
c_0,
c_1,
c_2,
\ldots
).
}
$$

它表示：

> 從 root 出發，把 observation radius 無限向外擴張時看到的全部有限完整局部結構。

---

# 25. 問題

如果：

$$
\boxed{
c_n(\mathbb C,o)
=
c_n(\mathbb D,p)
}
$$

對所有：

$$
n
$$

成立，

是否推出：

$$
(\mathbb C,o)
\cong
(\mathbb D,p)?
$$

在本文限制條件下：

$$
\boxed{
\text{是。}
}
$$

---

# 定理 3：Locally Finite Rooted Reconstruction Theorem

設：

$$
(\mathbb C,o),
\quad
(\mathbb D,p)
$$

為連通、根化、局部有限、有限 signature 的 relational structures。

若：

$$
\boxed{
\forall n\in\mathbb N,
\quad
B_n(\mathbb C,o)
\cong
B_n(\mathbb D,p)
}
$$

以保根同構成立，

則：

$$
\boxed{
(\mathbb C,o)
\cong
(\mathbb D,p).
}
$$

### 證明

對每個：

$$
n,
$$

令：

$$
\mathcal I_n
$$

為所有保根同構：

$$
f:
B_n(\mathbb C,o)
\rightarrow
B_n(\mathbb D,p)
$$

所成的集合。

依假設：

$$
\mathcal I_n\neq\varnothing.
$$

因兩個 balls 都有限，

$$
\mathcal I_n
$$

亦有限。

建立一棵樹：

$$
\mathcal T.
$$

第 $n$ 層節點為：

$$
\mathcal I_n.
$$

若：

$$
g\in\mathcal I_{n+1}
$$

限制到：

$$
B_n(\mathbb C,o)
$$

後等於：

$$
f\in\mathcal I_n,
$$

則連一條：

$$
f\rightarrow g.
$$

因 rooted relational isomorphism 保存 Gaifman adjacency，因此保存距離，故 restriction 確實將半徑 $n+1$ ball 的 rooted isomorphism 降到半徑 $n$ ball。

此樹：

- 每一層非空；
- 每層有限；
- 因而有限分枝；
- 具有任意有限深度。

由 König infinity lemma，存在無限 branch：

$$
f_0
\subseteq
f_1
\subseteq
f_2
\subseteq
\cdots.
$$

定義：

$$
\boxed{
f
=
\bigcup_{n=0}^{\infty}f_n.
}
$$

因 $\mathbb C$ 連通：

$$
\mathbb C
=
\bigcup_n
B_n(\mathbb C,o).
$$

同理：

$$
\mathbb D
=
\bigcup_n
B_n(\mathbb D,p).
$$

所以：

$$
f:
\mathbb C
\rightarrow
\mathbb D
$$

為全域雙射。

任何有限 arity relation tuple 最終全部落在某個有限 ball 內，而對應：

$$
f_n
$$

保存該 relation。

因此：

$$
f
$$

保存全部：

$$
\Sigma
$$

結構。

故：

$$
(\mathbb C,o)
\cong
(\mathbb D,p).
$$

證畢。

---

# 26. Canonical-Code 版本

由有限 canonical completeness：

$$
c_n(\mathbb C,o)
=
c_n(\mathbb D,p)
$$

當且僅當：

$$
B_n(\mathbb C,o)
\cong
B_n(\mathbb D,p).
$$

因此定理 3 可立即改寫為：

---

# 推論 3.1：All-Radius Canonical Completeness

在上述結構類別中：

$$
\boxed{
(\mathbb C,o)
\cong
(\mathbb D,p)
}
$$

當且僅當：

$$
\boxed{
\forall n,
\quad
c_n(\mathbb C,o)
=
c_n(\mathbb D,p).
}
$$

---

# 27. 局部有限 Observer Tower

定義半徑 $n$ observer：

$$
\boxed{
E_n(\mathbb C,o)
=
c_n(\mathbb C,o).
}
$$

則：

$$
K_n
$$

表示：

> 兩個 rooted structures 在 radius $n$ 完全不可區分。

有：

$$
\boxed{
K_{n+1}\subseteq K_n.
}
$$

因 radius $n+1$ 完整結構自然包含 radius $n$。

---

# 定理 4：Locally Finite Observer-Tower Completeness

在定理 3 的結構類別上：

$$
\boxed{
\bigcap_{n=0}^{\infty}K_n
=
\cong_{\mathrm{root}}.
}
$$

### 證明

若兩結構全域 rooted-isomorphic，當然所有有限 balls 同構。

故：

$$
\cong_{\mathrm{root}}
\subseteq
\bigcap_nK_n.
$$

反之，若兩結構屬於：

$$
\bigcap_nK_n,
$$

則所有：

$$
c_n
$$

相同。

由推論 3.1：

$$
(\mathbb C,o)
\cong
(\mathbb D,p).
$$

因此：

$$
\bigcap_nK_n
\subseteq
\cong_{\mathrm{root}}.
$$

證畢。

---

# 28. 這是「無界觀察完成全域身份」的正式版本

在此類別中：

$$
\boxed{
\text{No single bounded radius}
}
$$

可能足以分類所有無限結構。

但：

$$
\boxed{
\text{all finite radii together}
}
$$

可以。

因此：

$$
\boxed{
\text{Unbounded Compatible Local Observation}
\Longrightarrow
\text{Global Structural Separation}
}
$$

在明確條件下成為定理。

---

# 29. 內部觀察者可以在極限上達到主域分類能力

假設 main observer：

$$
M
$$

直接使用完整結構 identity：

$$
K_M
=
\cong_{\mathrm{root}}.
$$

而內部／局部 observer tower：

$$
I_0,I_1,I_2,\ldots
$$

依序讀取：

$$
B_0,B_1,B_2,\ldots.
$$

由定理 4：

$$
\boxed{
K_{I_\infty}
=
\bigcap_nK_{I_n}
=
K_M.
}
$$

因此：

$$
\boxed{
I_\infty
\equiv_{\mathrm{wobs}}
M.
}
$$

但其角色仍可能：

$$
I\neq M.
$$

所以再次得到：

$$
\boxed{
\text{observational capacity identity}
\neq
\text{role identity}.
}
$$

---

# 30. 局部有限性為何重要？

定理 3 的 proof 使用：

$$
\mathcal I_n
$$

有限。

這保證部分同構樹有限分枝，從而能使用 König 型 compactness argument。

若 finite-radius balls 可以無限大，這個結構立即失去。

---

# 31. 不可刪除 Local Finiteness

這不是單純 proof technique 的方便條件。

Martineau 構造了具有無限 generating systems 的 Cayley graphs，使兩個圖在任意指定有限 radius 上的 balls 都同構，但整體 Cayley graphs 不同構。

因此：

$$
\boxed{
\forall R<\infty,
\quad
B_R(G)\cong B_R(H)
}
$$

在不具合適局部有限／緊緻條件的類別中，不能推出：

$$
\boxed{
G\cong H.
}
$$

---

# 32. Local Agreement ≠ Global Identity 是真的

所以 NTLA-O 必須永久保留：

$$
\boxed{
\text{all finite local observations agree}
}
$$

並不在任意 universe 中推出：

$$
\boxed{
\text{global structures agree}.
}
$$

局部—全域重建一定需要指定結構類別與 compactness／finiteness 條件。

---

# 33. Coverage、Compatibility、Compactness 三者缺一不可

Paper 5 強調：

$$
\boxed{
\text{coverage}
+
\text{compatibility}.
}
$$

本篇再加入第三種：

$$
\boxed{
\text{compactness / finite branching}.
}
$$

所以無界 local observer reconstruction 的典型結構是：

$$
\boxed{
\text{Coverage}
}
$$

$$
+
$$

$$
\boxed{
\text{Compatibility}
}
$$

$$
+
$$

$$
\boxed{
\text{Compactness}
}
$$

$$
\Longrightarrow
$$

$$
\boxed{
\text{Global Reconstruction}.
}
$$

---

# 34. 有限／局部有限結果的適用界線

目前本文真正得到完整分類的，是：

### 第一層

$$
\boxed{
\text{finite relational NTLA structures}.
}
$$

使用：

$$
\operatorname{Can}_{\Sigma}.
$$

### 第二層

$$
\boxed{
\text{connected rooted locally finite relational structures}.
}
$$

使用：

$$
\{
\operatorname{Can}(B_n)
\}_{n<\omega}.
$$

下一步不能直接跳成：

$$
\boxed{
\text{all topological spaces}.
}
$$

---

# 35. Continuous Separation Problem

令：

$$
\mathfrak C
$$

為指定拓樸／幾何結構類別。

令：

$$
\equiv_\ast
$$

為指定身份：

例如：

$$
\cong_{\mathrm{homeo}},
$$

$$
\simeq_{\mathrm{homotopy}},
$$

或其他 NTLA enriched identity。

---

## 問題 CSP-1：Existence

是否存在一族：

$$
\boxed{
\mathcal F
=
\{
F_\alpha
\}_{\alpha\in A}
}
$$

使：

$$
\boxed{
x\equiv_\ast y
\iff
\forall\alpha,\;
F_\alpha(x)=F_\alpha(y)?
}
$$

---

# 36. Countable Continuous Separation

更強地問：

是否存在：

$$
\boxed{
F_0,F_1,F_2,\ldots
}
$$

使：

$$
\boxed{
\bigcap_n
\ker F_n
=
\equiv_\ast?
}
$$

這會直接產生 NTLA-O countable observer tower。

---

# 37. Computable Continuous Separation

再進一步問：

$$
\boxed{
F_n
}
$$

是否：

- 可有限表示；
- 可算法計算；
- 計算成本可控制；
- 可以從實際資料估計。

Complete invariant 存在與 efficient canonization 本來就是不同問題；有限圖研究已充分顯示這兩個層級應分開。

所以 continuous theory 更不能偷把：

$$
\boxed{
\text{existence}
}
$$

與：

$$
\boxed{
\text{computability}
}
$$

混在一起。

---

# 38. Stable Continuous Separation

若研究輸入具有 noise，

還需要：

$$
\boxed{
\text{stability}.
}
$$

即存在適當輸入 metric：

$$
d_X
$$

與 invariant metric：

$$
d_F
$$

使：

$$
d_X(x,y)
\text{ 小}
$$

能控制：

$$
d_F(F(x),F(y)).
$$

但：

$$
\boxed{
\text{stable}
}
$$

與：

$$
\boxed{
\text{complete}
}
$$

是不同性質。

---

# 39. 四層 Separation 強度

因此對 invariants 可分成：

### S0：Invariant

$$
x\equiv_\ast y
\Rightarrow
F(x)=F(y).
$$

### S1：Separating

不同等價類至少被某 invariant 分離。

### S2：Computably Separating

存在可算法實現的 separating family。

### S3：Stable and Computably Separating

另外具有適當穩定性。

不能把 S0 直接宣稱成 S3。

---

# 40. Persistence 的合法位置

Persistent homology 很適合作為：

$$
F_n
$$

中的一部分。

但單一 persistence diagram 不應被預設為任意幾何結構的 complete invariant。

已有研究正是因單一全域 persistence diagram 信息不足，而研究由大量局部子集 persistence diagrams 組成的 distributed persistence；在其指定 point-cloud model 中，可以得到 inverse/quasi-isometry 類結果。

這提供 NTLA-O 很好的方法論示例：

$$
\boxed{
\text{one coarse invariant}
}
$$

可以提升成：

$$
\boxed{
\text{structured family of local invariants},
}
$$

而完整性必須在指定對象類別內真正證明。

---

# 41. NTLA-O 不尋找「宇宙萬用單一拓樸碼」

本文因此不把研究目標設定成：

$$
\boxed{
\exists F:
\text{所有數學結構}
\rightarrow
\text{單一有限碼}
}
$$

並要求：

$$
F
$$

有效分類一切。

更合理的是：

$$
\boxed{
(\mathfrak C,\equiv_\ast)
\mapsto
\mathcal F_{\mathfrak C,\equiv_\ast}.
}
$$

即：

> 指定對象類與身份關係後，再研究適合的 separator。

---

# 42. Observer Completeness Spectrum

因此定義：

$$
\boxed{
\operatorname{Comp}
(\mathfrak O;\equiv_\ast)
}
$$

表示 observer system：

$$
\mathfrak O
$$

對指定身份的完備程度。

至少可分：

### Incomplete

$$
\bigcap_{\mathcal O\in\mathfrak O}
K_{\mathcal O}
\supsetneq
\equiv_\ast.
$$

### Complete

$$
\boxed{
\bigcap_{\mathcal O\in\mathfrak O}
K_{\mathcal O}
=
\equiv_\ast.
}
$$

### Efficiently Complete

另外存在可接受的 evaluation/canonization algorithm。

---

# 43. Observer Redundancy 再次出現

若：

$$
\mathfrak O
$$

已 complete，

某：

$$
\mathcal O_i
$$

若移除後仍：

$$
\bigcap_{j\neq i}K_{\mathcal O_j}
=
\equiv_\ast,
$$

則：

$$
\mathcal O_i
$$

對 identity separation 冗餘。

因此可以問：

$$
\boxed{
\text{minimal complete observer family}.
}
$$

這比單純「observer 越多越好」更合理。

---

# 44. Minimal Separating Family

定義：

$$
\boxed{
\mathfrak O_{\min}
}
$$

為 complete observer family，且任何 proper subfamily 都不 complete。

這產生新的 optimisation 問題：

$$
\boxed{
\min
\left|
\mathfrak O
\right|
$$

subject to：

$$
\boxed{
\bigcap_{\mathcal O\in\mathfrak O}
K_{\mathcal O}
=
\equiv_\ast.
}
$$

若 observers 具有成本：

$$
c(\mathcal O),
$$

則可改成：

$$
\boxed{
\min
\sum_{\mathcal O\in\mathfrak O}
c(\mathcal O).
}
$$

---

# 45. 完備性與解析深度成本

越細的 observer 通常可能需要：

- 更多資料；
- 更多計算；
- 更高 path resolution；
- 更大的 local coverage；
- 更複雜 canonical comparison。

所以最實際的 NTLA-O 系統不一定總是使用：

$$
\operatorname{Can}
$$

直接比較。

而可以採：

$$
\boxed{
F_0
\rightarrow
F_1
\rightarrow
\cdots
\rightarrow
F_k
\rightarrow
\operatorname{Can}
}
$$

逐階增加成本。

---

# 46. Adaptive Observer Refinement

如果：

$$
F_n(x)\neq F_n(y),
$$

已經分離二者，

就不必計算：

$$
F_{n+1},
F_{n+2},\ldots
$$

因此可以定義 adaptive separation：

$$
\boxed{
n^\ast(x,y)
=
\min
\{
n:
F_n(x)\neq F_n(y)
\}.
}
$$

這正是：

$$
r_{\mathrm{sep}}(x,y).
$$

所以 Paper 7 的 separation rank 同時具有 algorithmic interpretation。

---

# 47. NTLA-O 完整觀察流程

完整比較可以寫成：

$$
\boxed{
x,y
}
$$

$$
\Downarrow
$$

$$
\boxed{
F_0
}
$$

若未分離：

$$
\Downarrow
$$

$$
\boxed{
F_1
}
$$

$$
\Downarrow
$$

$$
\cdots
$$

$$
\Downarrow
$$

$$
\boxed{
F_n
}
$$

$$
\Downarrow
$$

最終必要時：

$$
\boxed{
\operatorname{Can}.
}
$$

這與 NTLA 的 nested refinement 本身完全一致。

---

# 48. 物件拓樸與觀察拓樸真正形成對偶問題

到這裡可以區分：

$$
\boxed{
\text{Object Structure}
}
$$

與：

$$
\boxed{
\text{Observer Separation Structure}.
}
$$

前者：

$$
\mathbb C.
$$

後者：

$$
\{
K_{\mathcal O}
\}_{\mathcal O}.
$$

可以研究：

$$
\boxed{
\mathbb C
\mapsto
\operatorname{ObsSig}(\mathbb C).
}
$$

完整 observer system 的目標就是讓：

$$
\operatorname{ObsSig}
$$

在指定 quotient 上 injective。

---

# 49. Complete Observational Embedding

令：

$$
\mathfrak O
=
\{
\mathcal O_\alpha
\}_{\alpha\in A}.
$$

定義：

$$
\boxed{
\Psi_{\mathfrak O}(x)
=
\left(
E_{\mathcal O_\alpha}(x)
\right)_{\alpha\in A}.
}
$$

若：

$$
\mathfrak O
$$

complete，則：

$$
\Psi_{\mathfrak O}
$$

下降為：

$$
\boxed{
\bar\Psi:
\Omega/{\equiv_\ast}
\hookrightarrow
\prod_{\alpha\in A}Y_\alpha.
}
$$

因此 identity classes 可以嵌入 observer-output product。

---

# 定理 5：Complete Observer Embedding

若：

$$
\bigcap_{\alpha}K_{\mathcal O_\alpha}
=
\equiv_\ast,
$$

則：

$$
\boxed{
\bar\Psi
}
$$

為單射。

### 證明

若：

$$
\bar\Psi([x])
=
\bar\Psi([y]),
$$

則對所有：

$$
\alpha
$$

有：

$$
E_{\mathcal O_\alpha}(x)
=
E_{\mathcal O_\alpha}(y).
$$

故：

$$
(x,y)\in
\bigcap_\alpha K_{\mathcal O_\alpha}
=
\equiv_\ast.
$$

因此：

$$
[x]=[y].
$$

證畢。

---

# 50. NTLA-O 的 Complete-Separation Principle

因此提出一個研究原則：

# **Complete-Separation Principle**

任何強身份主張：

$$
x\equiv_\ast y
$$

若要被 observation framework 實際使用，都應盡量回答：

$$
\boxed{
\text{What separating family realizes }
\equiv_\ast
\text{ as an observer kernel intersection?}
}
$$

即：

$$
\boxed{
\equiv_\ast
=
\bigcap_\alpha
K_{\mathcal O_\alpha}.
}
$$

---

# 51. 這比「找一個萬能不變量」更一般

可能存在單一：

$$
F.
$$

也可能必須使用：

$$
F_0,F_1,\ldots.
$$

也可能需要：

- local observations；
- path transport；
- tower data；
- higher invariants。

所以 NTLA-O 完整性本身是一個**觀察系統性質**，不要求一定被單一數值解決。

---

# 52. 本篇與前六篇的閉合

Paper 2 問：

> 誰在觀察？

得到：

$$
\rho_X(\mathcal O).
$$

Paper 3 問：

> observer 最小怎麼區分？

得到：

$$
\mathcal A_{\mathcal O}.
$$

Paper 4 問：

> 區分如何形成局部拓樸？

得到：

$$
\tau_{\mathcal O}.
$$

Paper 5 問：

> 局部資料如何拼成全域？

得到：

$$
\mathscr F,
\quad
\operatorname{Glue}.
$$

Paper 6 問：

> 狀態沿歷史如何搬運？

得到：

$$
T_\gamma.
$$

Paper 7 問：

> 解析度如何逐層展開？

得到：

$$
\mathbf{ProObs},
\quad
\varprojlim.
$$

本篇最後問：

> 這整套 observation 到底夠不夠？

答案由：

$$
\boxed{
\bigcap_{\mathcal O}K_{\mathcal O}
\stackrel{?}{=}
\equiv_\ast
}
$$

判定。

---

# 53. 七篇數學主體的統一核心

因此 NTLA-O 的數學主體現在可以壓縮成：

$$
\boxed{
\mathfrak N
=
\left(
X,
\mathfrak I,
\mathbf{Obs},
\mathcal L,
\mathcal J,
\mathcal A,
\tau,
K,
\mathscr F,
T,
\mathbf{ProObs}
\right).
}
$$

其中：

$$
\mathfrak I
$$

指定要保留什麼身份；

$$
\mathbf{Obs}
$$

提供觀察者；

$$
\mathcal L
$$

控制合法性；

$$
\mathcal J
$$

控制判定；

$$
\mathcal A
$$

提供區分 predicates；

$$
\tau
$$

組織局部可觀察性；

$$
K
$$

描述不可區分；

$$
\mathscr F
$$

承載局部 observation states；

$$
T
$$

描述 path transport；

$$
\mathbf{ProObs}
$$

保存解析歷史。

而完整性條件則是：

$$
\boxed{
K_{\mathrm{total}}
=
\equiv_{\mathfrak I}.
}
$$

---

# 54. 本篇主要結果

本文得到：

### 定理 A：Finite Canonical Completeness

$$
\boxed{
\operatorname{Can}_{\Sigma}(\mathbb C)
=
\operatorname{Can}_{\Sigma}(\mathbb D)
\iff
\mathbb C\cong_\Sigma\mathbb D.
}
$$

### 定理 B：Finite Complete Observer Existence

有限 NTLA relational structures 存在 complete canonical observer。

### 定理 C：Locally Finite Rooted Reconstruction

所有 finite-radius rooted balls 同構推出全域 rooted isomorphism。

### 定理 D：Locally Finite Observer-Tower Completeness

$$
\boxed{
\bigcap_nK_n
=
\cong_{\mathrm{root}}.
}
$$

### 定理 E：Complete Observer Embedding

若 observer family complete，則 identity quotient 嵌入所有 observer outputs 的積。

### 邊界 F：Local Finiteness 不能無條件移除

非局部有限圖可具有所有有限半徑局部同構而全域不同構。

---

# 55. 理論強度聲明

本文已經證明：

- 有限 relational NTLA 結構存在 complete canonical separator；
- 指定局部有限 rooted relational structures 可由所有 finite-radius canonical observations 完整分類。

本文**沒有**證明：

- Betti numbers 是完整不變量；
- homology 是 homeomorphism complete invariant；
- persistence diagram 是一般 complete invariant；
- 任意無限圖由所有有限 balls 唯一決定；
- 任意 topological space 存在有限 complete code；
- Continuous Separation Problem 一般可解；
- complete canonical separator 一定能高效率計算。

因此本文的 strongest established region 為：

$$
\boxed{
\text{Finite}
\rightarrow
\text{Countable Locally Finite}.
}
$$

而下一個 frontier 為：

$$
\boxed{
\text{Restricted Continuous Classes}.
}
$$

---

# 56. 結論

NTLA-O 最初從一句非常直覺的命題出發：

> **如果洞、嵌套或連接存在有效差異，就不應因為粗摘要相同而自動判成同一。**

本篇第一次把這件事在一個明確數學域中做完。

對有限 NTLA 結構：

$$
\boxed{
\text{every preserved structural difference}
}
$$

都能由：

$$
\boxed{
\operatorname{Can}_{\Sigma}
}
$$

完整分離。

對局部有限可數 rooted NTLA 結構：

$$
\boxed{
\text{every finite radius}
}
$$

可能都只是局部資訊，

但：

$$
\boxed{
\text{all finite radii}
}
$$

在 compactness 條件下足以恢復全域身份。

因此得到：

$$
\boxed{
\text{Finite Complete Separation}
}
$$

$$
\Downarrow
$$

$$
\boxed{
\text{Unbounded Local Observation}
}
$$

$$
+
$$

$$
\boxed{
\text{Local Finiteness / Compactness}
}
$$

$$
\Downarrow
$$

$$
\boxed{
\text{Global Reconstruction}.
}
$$

但當我們離開這些限制條件後：

$$
\boxed{
\text{local agreement}
\not\Rightarrow
\text{global identity}.
}
$$

所以 NTLA-O 不再使用：

> 「只要一直觀察下去，最後必然知道全部。」

這種無條件主張。

正式版本改為：

$$
\boxed{
\text{Observer completeness is a theorem to be proved
for each specified structural class.}
}
$$

也就是：

> **觀察完備性不是信念，而是一個需要逐類證明的數學性質。**

---

# 57. 下一篇：統一總篇

至此，NTLA-O 九篇系列中的八篇數學主體已完成。

最後一篇將不再大幅新增新數學，而做完整閉合：

# **NTLA-O：廣義嵌套拓樸觀察者論——統一公理、定理依賴圖、傳統數學接口與研究邊界**

內容將包括：

1. NTLA 1.0 → NTLA 2.0 修訂史；
2. NTLA-O 最小公理組；
3. Role / Locality / Resolution / Transport 四軸統一；
4. Set / Topology / Sheaf / Groupoid / Pro-object / Canonization 六大傳統數學接口；
5. 所有主要定理依賴圖；
6. 身份層級：
   $$
   =
   \rightarrow
   \cong
   \rightarrow
   \sim_{\mathcal O}
   \rightarrow
   \equiv_{\mathrm{lim}};
   $$
7. 三種無界與三種完備性的正式區分；
8. novelty discipline；
9. 已證、條件成立、猜想、未解問題完整列表；
10. NTLA-O 1.0 的 canonical notation table；
11. Continuous Separation Problem 與後續研究綱領。

那篇完成後，這個系列就可以正式封頂為 **9 篇正式草稿版**。