# 崁套拓樸代數學習架構 2.0
## 從拓樸匹配、差異敏感連接到觀察者相對結構學習

**英文題名：** *Nested Topological Learning Architecture 2.0: From Topological Matching and Difference-Sensitive Connections to Observer-Relative Structural Learning*  
**縮寫：** NTLA 2.0  
**系列：** NTLA-O Series, Paper 1  
**版本：** v0.1 Formal Draft  
**作者：** Neo.K  
**理論整理與形式化協作：** Aletheia / GPT-5.6 Sol  
**日期：** 2026-08-17

---

## 摘要

早期「崁套拓樸代數學習架構」（Nested Topological Learning Architecture, NTLA）提出一個核心直覺：複雜理論、概念或知識結構不宜只被表示為單一向量或固定字串，而可以被表示為多層嵌套的拓樸結構，學習則可被部分理解為模型結構與目標結構之間的逐層匹配。舊版本進一步使用持續同調與 bottleneck distance 作為拓樸比較工具，並以生成—近似—恢復流程描述多階學習。

NTLA 2.0 保留上述核心，但對其數學強度進行系統修訂。

第一，本文不再宣稱「一般學習等同於拓樸匹配」。拓樸匹配被重新定位為一種結構學習表示框架；是否適用取決於研究對象、表示函子與選定的不變量。

第二，bottleneck distance 不再被定義為 NTLA 的普遍或唯一損失函數。它只在已建立 filtration、persistent homology 與 persistence-diagram 表示的分量上作為合法距離之一。經典持續同調穩定性理論保證，在適當條件下輸入函數的小擾動會導致 persistence diagram 的受控擾動，但這不等於 persistence diagram 是任意結構的完整不變量。

第三，本文加入「差異敏感連接結構」。兩個對象即使具有相同 Betti 數、相同部分同調資料甚至相同粗粒度拓樸摘要，也不因此被 NTLA 2.0 自動判為同一。洞、區域或概念節點之間的連接、嵌套、方向、路徑與歷史可以被選擇為身份結構的一部分。

第四，本文為後續 NTLA-O 建立 observer-ready interface。結構身份不再只有一個絕對比較函數，而明確依賴「哪些差異被允許觀察、哪些差異被判定為有效、哪些差異被等價關係商掉」。

因此，NTLA 2.0 從早期的「拓樸學習架構」修訂為：

$$
\boxed{
\text{Nested Structural Representation}
+
\text{Topological Invariants}
+
\text{Difference-Sensitive Relations}
+
\text{Explicit Identity Criterion}.
}
$$

本文只提出一個數學表示與學習框架，不主張所有認知、AI 學習或理論形成必然服從 NTLA。

**關鍵詞：** 崁套拓樸、嵌套學習、持續同調、結構學習、瓶頸距離、逆系統、連接差異、理論表示、觀察者相對性

---

# 1. 修訂動機

## 1.1 舊 NTLA 的核心

舊 NTLA 的核心結構可概括為：

$$
T^\infty
=
T_0
\leftarrow
T_1
\leftarrow
T_2
\leftarrow
\cdots.
$$

其中不同 $T_n$ 表示不同深度或解析度下的理論／知識結構。

若存在投影：

$$
p_{n+1,n}:
T_{n+1}
\rightarrow
T_n,
$$

則高階表示可以被投影到較粗表示。

舊版本的重要直覺是：

$$
\boxed{
\text{learning}
\approx
\text{nested structural alignment}.
}
$$

這個直覺本文保留。

但「$\approx$」不能被偷換成普遍數學等號。

---

# 2. 第一項修正：學習不等於拓樸匹配

設一般學習系統為：

$$
\mathfrak L
=
(\mathcal X,\mathcal Y,\Theta,\mathcal A,\mathcal E),
$$

其中：

- $\mathcal X$ 為輸入域；
- $\mathcal Y$ 為輸出或目標域；
- $\Theta$ 為模型狀態／參數空間；
- $\mathcal A$ 為更新機制；
- $\mathcal E$ 為評估條件。

NTLA 額外選擇一個表示映射：

$$
\Phi:
\mathfrak L
\rightarrow
\mathfrak T,
$$

其中：

$$
\mathfrak T
$$

是某個嵌套結構空間。

因此 NTLA 的正式主張只應寫成：

$$
\boxed{
\text{某些學習問題可以經由 }
\Phi
\text{ 被轉譯為嵌套結構匹配問題。}
}
$$

而不是：

$$
\boxed{
\text{所有學習本體上就是拓樸匹配。}
}
$$

這兩個命題強度完全不同。

---

# 3. NTLA 2.0 的基本結構

定義第 $n$ 層 NTLA 狀態：

$$
\boxed{
\mathcal T_n
=
\left(
X_n,
\tau_n,
\mathcal H_n,
\mathcal C_n,
\Lambda_n
\right).
}
$$

其中：

- $X_n$：第 $n$ 層底集合；
- $\tau_n$：該層選定的拓樸；
- $\mathcal H_n$：嵌套／包含結構；
- $\mathcal C_n$：差異敏感連接結構；
- $\Lambda_n$：標籤、型別或其他研究中必須保持的資料。

舊 NTLA 的主要資訊集中於：

$$
(X_n,\tau_n).
$$

新版則明確提升為：

$$
\boxed{
(X_n,\tau_n,\mathcal H_n,\mathcal C_n,\Lambda_n).
}
$$

因此：

$$
\boxed{
\text{topological type}
\neq
\text{full NTLA identity}.
}
$$

---

# 4. 差異敏感連接結構

令：

$$
H_n
$$

表示第 $n$ 層選定的結構單元，可為洞、區域、概念節點、部件或其他研究對象。

定義：

$$
\mathcal C_n
=
\left(
E_n,
N_n,
D_n,
P_n,
G_n
\right),
$$

其中：

$$
E_n
$$

記錄直接連接，

$$
N_n
$$

記錄嵌套，

$$
D_n
$$

記錄有向關係，

$$
P_n
$$

記錄選定的路徑資料，

$$
G_n
$$

記錄在研究目的下必須保存的生成／歷史資料。

不是所有應用都必須保留全部五類資料。

因此定義一個身份規格：

$$
\boxed{
\mathfrak I
\subseteq
\{
\tau,\mathcal H,E,N,D,P,G,\Lambda,\ldots
\}.
}
$$

只有被：

$$
\mathfrak I
$$

指定為身份必要結構的差異，才禁止被商掉。

---

# 5. 有效差異原則

NTLA 2.0 不採用：

$$
\boxed{
\text{任何字面差異都代表新對象。}
}
$$

而採用：

$$
\boxed{
\text{任何被身份規格 }
\mathfrak I
\text{ 指定為有效的差異，都必須保留。}
}
$$

因此重新命名：

$$
h_1\mapsto h_a,
\qquad
h_2\mapsto h_b
$$

若保持全部 $\mathfrak I$ 結構，可以仍然屬於同一結構同構類。

但如果：

$$
E_A\neq E_B
$$

或：

$$
N_A\neq N_B
$$

而 $E,N\in\mathfrak I$，則不能僅因兩者具有相同 Betti 數就宣稱：

$$
A\equiv B.
$$

---

# 6. 第二項修正：Betti 數不是完整身份

對拓樸空間 $X$，Betti 數：

$$
\beta_k(X)
=
\operatorname{rank}H_k(X)
$$

可以描述某些同調資訊。

但：

$$
\beta_k(X)=\beta_k(Y)
$$

一般不推出：

$$
X\cong Y.
$$

同樣：

$$
H_\ast(X)\cong H_\ast(Y)
$$

也不能在一般情形下視為 homeomorphism 的完整分類。

因此 NTLA 2.0 把拓樸資料分為：

$$
\boxed{
\text{coarse invariants}
}
$$

與：

$$
\boxed{
\text{identity-complete data relative to a chosen class}.
}
$$

前者適合快速比較。

後者才足以支持強身份主張。

---

# 7. 持續同調的位置

若 NTLA 層具有 filtration：

$$
K_a
\subseteq
K_b,
\qquad
a\leq b,
$$

則可建立 persistent homology：

$$
H_k(K_a)
\rightarrow
H_k(K_b).
$$

由此可以得到 persistence module 與 persistence diagram。

持續同調提供的是：

$$
\boxed{
\text{跨尺度持續存在的拓樸特徵摘要}.
}
$$

它特別適合 NTLA 的多解析度表示。

但 persistence diagram 不應被自動理解為原結構的完整身份證。

事實上，在一般 q-tame persistence modules 中，普通 persistence diagram 本身未必是完整不變量；文獻甚至需要引入 observable category 才能在相應局部化設定下恢復完整分類性。

因此：

$$
\boxed{
\text{persistence summary}
\neq
\text{full NTLA structure}.
}
$$

---

# 8. 第三項修正：bottleneck distance 的合法位置

舊 NTLA 曾將 bottleneck distance 放在過於核心的位置。

新版改為：

若：

$$
D_X,
D_Y
$$

是同一規格下得到的 persistence diagrams，

則可以使用：

$$
d_B(D_X,D_Y)
$$

衡量該 persistence representation 的差異。

經典穩定性定理在適當條件下給出類似：

$$
d_B
\left(
\operatorname{Dgm}(f),
\operatorname{Dgm}(g)
\right)
\leq
\|f-g\|_\infty.
$$

其意義是 persistence diagram 對一定類型的小輸入擾動具有穩定性。

但此結果不推出：

$$
\boxed{
d_B
=
\text{universal learning loss}.
}
$$

也不推出：

$$
\boxed{
d_B=0
\Rightarrow
\text{原始理論／結構完全相同}
}
$$

在任何未指定表示條件的情況下都成立。

---

# 9. NTLA 2.0 多分量損失

因此新版定義：

$$
\boxed{
\mathcal L_{\mathrm{NTLA}}
=
\lambda_{\mathrm{task}}
\mathcal L_{\mathrm{task}}
+
\lambda_{\mathrm{top}}
\mathcal L_{\mathrm{top}}
+
\lambda_{\mathrm{conn}}
\mathcal L_{\mathrm{conn}}
+
\lambda_{\mathrm{nest}}
\mathcal L_{\mathrm{nest}}
+
\lambda_{\mathrm{id}}
\mathcal L_{\mathrm{id}}.
}
$$

其中：

$$
\mathcal L_{\mathrm{task}}
$$

評估原始任務表現；

$$
\mathcal L_{\mathrm{top}}
$$

評估選定的拓樸表示；

$$
\mathcal L_{\mathrm{conn}}
$$

評估連接結構；

$$
\mathcal L_{\mathrm{nest}}
$$

評估嵌套結構；

$$
\mathcal L_{\mathrm{id}}
$$

評估身份規格中不得遺失的資料。

若使用持續同調，則可以令：

$$
\mathcal L_{\mathrm{top}}
=
\sum_k
w_k
d_B
\left(
D_k^{\mathrm{model}},
D_k^{\mathrm{target}}
\right).
$$

但這只是：

$$
\mathcal L_{\mathrm{top}}
$$

的一個可能實例。

---

# 10. 多層 NTLA 系統

令：

$$
\mathcal T_0,
\mathcal T_1,
\mathcal T_2,
\ldots
$$

為不同解析階。

定義 bonding maps：

$$
p_{n+1,n}:
\mathcal T_{n+1}
\rightarrow
\mathcal T_n.
$$

若滿足：

$$
p_{n,n}
=
\operatorname{id},
$$

以及：

$$
p_{k,i}
=
p_{j,i}
\circ
p_{k,j}
\qquad
(i<j<k),
$$

則：

$$
\boxed{
\left(
\mathcal T_n,
p_{n+1,n}
\right)
}
$$

形成 inverse system。

這提供舊 NTLA：

$$
T_0
\leftarrow
T_1
\leftarrow
T_2
\leftarrow
\cdots
$$

更標準的數學解讀。

---

# 11. NTLA 的「崁套」不只表示集合包含

新版區分三種嵌套。

## 11.1 集合嵌套

$$
X_{n+1}\subseteq X_n.
$$

## 11.2 結構解析嵌套

高階結構保留低階結構，並增加新的可區分資料：

$$
F_n
=
q_n\circ F_{n+1}.
$$

## 11.3 容器嵌套

一個結構存在於另一個結構的合法容器內：

$$
\mathcal H(A,B)=1.
$$

三者可以重合，但不必然相同。

因此：

$$
\boxed{
\text{nested}
}
$$

在 NTLA 2.0 中永遠需要標明是哪種嵌套。

---

# 12. 結構解析函數

令研究對象全集為：

$$
\Omega.
$$

第 $n$ 階結構讀取為：

$$
F_n:
\Omega
\rightarrow
Y_n.
$$

定義：

$$
x\sim_ny
\iff
F_n(x)=F_n(y).
$$

並記：

$$
K_n
=
\{
(x,y):
F_n(x)=F_n(y)
\}.
$$

如果：

$$
F_n
=
q_n\circ F_{n+1},
$$

則高一階至少保留低階所有可辨識資訊。

---

# 定理 1：NTLA 結構精化單調定理

若：

$$
F_n
=
q_n\circ F_{n+1},
$$

則：

$$
\boxed{
K_{n+1}
\subseteq
K_n.
}
$$

### 證明

若：

$$
(x,y)\in K_{n+1},
$$

則：

$$
F_{n+1}(x)
=
F_{n+1}(y).
$$

因此：

$$
F_n(x)
=
q_n(F_{n+1}(x))
=
q_n(F_{n+1}(y))
=
F_n(y).
$$

故：

$$
(x,y)\in K_n.
$$

所以：

$$
K_{n+1}\subseteq K_n.
$$

證畢。

---

# 13. 真正的結構增益

若：

$$
K_{n+1}=K_n,
$$

則第 $n+1$ 層即使資料格式更複雜，也沒有增加新的可區分能力。

只有：

$$
\boxed{
K_{n+1}\subsetneq K_n
}
$$

時，才稱：

$$
\boxed{
\mathcal T_{n+1}
}
$$

對：

$$
\mathcal T_n
$$

形成**嚴格結構精化**。

因此：

$$
\boxed{
\text{更多參數}
\not\Rightarrow
\text{更多結構資訊}.
}
$$

以及：

$$
\boxed{
\text{更多嵌套層}
\not\Rightarrow
\text{更多可區分性}.
}
$$

---

# 14. 差異首次顯現階

對：

$$
x,y\in\Omega,
$$

定義：

$$
\boxed{
r(x,y)
=
\min
\{
n:
F_n(x)\neq F_n(y)
\}.
}
$$

若沒有有限 $n$ 可分離，記：

$$
r(x,y)=\infty.
$$

$r(x,y)$ 稱為：

# **Difference Emergence Rank**

即：

# **差異顯現階**

它描述：

> 一個真實保留的結構差異，需要到哪個解析層才第一次能被表示。

---

# 15. 洞與連接的例子

考慮兩個結構：

$$
A,
B.
$$

假設：

$$
\beta_1(A)
=
\beta_1(B)
=
3.
$$

第零階只讀：

$$
F_0(X)=\beta_1(X).
$$

因此：

$$
F_0(A)=F_0(B).
$$

若第一階加入洞鄰接：

$$
F_1(X)
=
\left(
\beta_1(X),
E_H(X)
\right),
$$

而：

$$
E_H(A)\neq E_H(B),
$$

則：

$$
F_1(A)\neq F_1(B).
$$

因此：

$$
\boxed{
r(A,B)=1.
}
$$

所以：

$$
\boxed{
\text{相同洞數}
}
$$

從來不等於：

$$
\boxed{
\text{相同洞連接結構}.
}
$$

---

# 16. 生成—近似—恢復流程的修訂

舊 NTLA 使用 GAR：

$$
\boxed{
G
\rightarrow
A
\rightarrow
R.
}
$$

新版保留，但重新定位為 architecture template，而不是普遍學習定律。

## 16.1 Generate

由目前狀態產生候選高階結構：

$$
G:
\mathcal T_n
\rightarrow
\mathcal P(\mathcal T_{n+1}).
$$

## 16.2 Approximate

依選定 loss 與身份規格評估候選：

$$
A:
\mathcal P(\mathcal T_{n+1})
\rightarrow
\mathcal T_{n+1}^{\ast}.
$$

## 16.3 Recover

檢查新結構投影回較低階後是否保持必要資訊：

$$
R:
\mathcal T_{n+1}^{\ast}
\rightarrow
\mathcal T_n.
$$

理想一致性條件為：

$$
\boxed{
p_{n+1,n}
\left(
\mathcal T_{n+1}^{\ast}
\right)
\approx_{\mathfrak I}
\mathcal T_n.
}
$$

其中：

$$
\approx_{\mathfrak I}
$$

表示只要求保持身份規格所指定的結構。

---

# 17. 恢復不等於完全逆映射

若：

$$
p_{n+1,n}
$$

不是單射，

則一般不存在唯一：

$$
p_{n+1,n}^{-1}.
$$

因此 Recover 的數學意義不是：

$$
\boxed{
\text{精確逆轉所有粗粒化}.
}
$$

而是：

$$
\boxed{
\text{驗證新高階表示投影後仍滿足必要一致性}.
}
$$

這修正舊版中容易把 recovery 理解得過強的問題。

---

# 18. 理論學習的新版定義

定義模型的嵌套表示：

$$
\mathbf T^{\mathrm{model}}
=
\{
\mathcal T_n^{\mathrm{model}}
\}_{n\in I}.
$$

定義目標表示：

$$
\mathbf T^{\mathrm{target}}
=
\{
\mathcal T_n^{\mathrm{target}}
\}_{n\in I}.
$$

NTLA learning objective 是尋找模型狀態 $\theta$，使指定解析範圍：

$$
J\subseteq I
$$

上的綜合差異：

$$
\boxed{
\mathcal D_J
\left(
\mathbf T^{\mathrm{model}}_\theta,
\mathbf T^{\mathrm{target}}
\right)
}
$$

被降低。

但：

$$
\mathcal D_J=0
$$

只代表在：

$$
J
$$

及指定身份規格下不可區分。

除非另外證明 representation complete，否則不能推出：

$$
\boxed{
\text{模型已取得目標理論的全部結構}.
}
$$

---

# 19. 「理論形狀同構」主張的修正

舊 NTLA 可以被解讀成目標：

$$
T_{\mathrm{model}}
\cong
T_{\mathrm{target}}.
$$

NTLA 2.0 將其降為條件性目標。

只有先指定：

1. 理論如何被映射為數學結構；
2. 哪些結構必須保持；
3. 採用哪一類同構；
4. 表示是否丟失資訊；

之後，才可以討論：

$$
\boxed{
\Phi(T_{\mathrm{model}})
\cong_{\mathfrak I}
\Phi(T_{\mathrm{target}}).
}
$$

因此：

$$
\boxed{
\text{theory isomorphism}
}
$$

不是原始自然語言理論之間自動存在的關係。

它是 representation-relative statement。

---

# 20. NTLA 與現有 Nested Learning 的名稱區分

「Nested Learning」在既有機器學習文獻中已有其他用法。

例如一類工作把 nested learning 用於多粒度預測與 nested information bottlenecks；另一類較新的工作把模型描述為多層／平行的嵌套 optimization problems，並研究多時間尺度更新與 continual learning。

本文的：

# **Nested Topological Learning Architecture**

與上述工作不等同。

NTLA 的「Nested」主要指：

$$
\boxed{
\text{nested structural/topological resolution}
}
$$

以及：

$$
\boxed{
\text{bonded hierarchy of representations}.
}
$$

它不預設：

$$
\boxed{
\text{nested optimization problems}.
}
$$

因此後續文獻中應始終使用完整名稱或縮寫：

$$
\boxed{
\mathrm{NTLA}
}
$$

而不單獨稱為 Nested Learning。

---

# 21. NTLA 2.0 與 NTLA-O 的接口

到這裡，我們尚未指定：

> 誰決定哪些差異算差異？

因此加入 observer interface。

對每一個觀察者：

$$
\mathcal O,
$$

後續 NTLA-O 將定義：

$$
\mathcal L_{\mathcal O}
$$

為合法觀察域，

$$
\mathcal J_{\mathcal O}
$$

為判定域，

以及：

$$
K_{\mathcal O}
$$

為觀察不可區分核。

於是 NTLA 2.0 的：

$$
K_n
$$

可以進一步升級為：

$$
\boxed{
K_{n,\mathcal O}.
}
$$

這意味著：

$$
\boxed{
\text{同一個結構解析層}
}
$$

在不同觀察者下，

仍可能具有不同的有效可區分性。

---

# 22. 主、內、外觀察者的預留接口

對參考域：

$$
X,
$$

後續系列將定義：

$$
\rho_X(\mathcal O)
\in
\{M,I,E\}.
$$

其中：

$$
M
$$

為主觀察角色，

$$
I
$$

為內部角色，

$$
E
$$

為外部角色。

NTLA 2.0 此處只保留接口：

$$
\boxed{
\mathcal T_n
\longrightarrow
\mathcal T_{n,\mathcal O}.
}
$$

不在本文提前假定：

$$
M,
I,
E
$$

之間存在任何知識能力高低關係。

---

# 23. NTLA 2.0 的最小公理組

## 公理 N1：結構表示公理

研究對象可以在指定研究域內被映射為：

$$
\mathcal T
=
(X,\tau,\mathcal H,\mathcal C,\Lambda).
$$

這是建模選擇，不是所有存在的本體論斷言。

---

## 公理 N2：身份規格公理

任何「同一」主張都必須指定：

$$
\mathfrak I.
$$

---

## 公理 N3：投影一致性公理

若兩解析層存在 projection：

$$
p_{n+1,n},
$$

則其定義域、值域與保持結構必須明示。

---

## 公理 N4：有效差異保存公理

若：

$$
\Delta_{\mathfrak I}(A,B)\neq0,
$$

則禁止在未聲明 quotient rule 的情況下直接寫：

$$
A\equiv_{\mathfrak I}B.
$$

---

## 公理 N5：拓樸摘要非完備公理

任何 Betti、homology、persistence 或其他選定不變量，除非已對研究類別證明完整性，不得自動視為完整結構身份。

---

## 公理 N6：損失函數域限定公理

任何：

$$
\mathcal L
$$

都必須說明它比較的是哪個 representation component。

---

## 公理 N7：觀察者可延伸公理

NTLA identity 可以進一步依賴：

$$
\mathcal O.
$$

因此允許：

$$
K_{n,\mathcal O_1}
\neq
K_{n,\mathcal O_2}.
$$

---

# 24. 主要定理與非定理

目前 NTLA 2.0 中真正由定義直接推出的核心結果包括：

$$
F_n=q_n\circ F_{n+1}
\Longrightarrow
K_{n+1}\subseteq K_n.
$$

以及：

$$
K_{n+1}\subsetneq K_n
$$

代表第 $n+1$ 層確實產生新的可區分能力。

而以下內容**不是本文已證普遍定理**：

$$
\boxed{
\text{所有學習都是拓樸學習};
}
$$

$$
\boxed{
\text{所有理論都有唯一拓樸表示};
}
$$

$$
\boxed{
\text{bottleneck distance 是最佳或唯一 loss};
}
$$

$$
\boxed{
\text{persistence diagram 完整決定所有結構};
}
$$

$$
\boxed{
\text{AI 理論空間必然可與人類理論空間同構}.
}
$$

它們若未來需要成立，都必須增加額外假設或實證證據。

---

# 25. NTLA 2.0 的新版核心式

舊版本可被概括為：

$$
\text{Theory}
\rightarrow
\text{Topology}
\rightarrow
\text{Matching}.
$$

新版改成：

$$
\boxed{
\text{Object / Theory}
}
$$

$$
\Downarrow
$$

$$
\boxed{
\text{Explicit Representation Choice}
}
$$

$$
\Downarrow
$$

$$
\boxed{
(X,\tau,\mathcal H,\mathcal C,\Lambda)
}
$$

$$
\Downarrow
$$

$$
\boxed{
\text{Nested Resolution Tower}
}
$$

$$
\Downarrow
$$

$$
\boxed{
\text{Selected Invariants}
+
\text{Connection Data}
}
$$

$$
\Downarrow
$$

$$
\boxed{
\text{Identity Criterion}
}
$$

$$
\Downarrow
$$

$$
\boxed{
\text{Structure-Sensitive Learning / Matching}.
}
$$

---

# 26. 與傳統拓樸資料分析的關係

拓樸資料分析的成熟成果證明，拓樸與持續性結構確實可以用來分析高維資料；持續同調的 stability theory 也為噪聲下的多尺度特徵比較提供嚴格基礎。

NTLA 2.0 不重新發明這些結果。

本文的工作位置是：

$$
\boxed{
\text{將這些既有拓樸工具放進一個
嵌套、差異敏感、身份條件顯式化的學習表示框架。}
}
$$

因此其潛在新意應從：

$$
\boxed{
\text{framework composition}
}
$$

與後續：

$$
\boxed{
\text{observer-indexed refinement}
}
$$

中評估，而不是從單一 persistence technique 中尋找。

---

# 27. 修訂對照表

### 舊主張：理論學習等於拓樸空間匹配

新版：

$$
\boxed{
\text{拓樸匹配是可選的結構學習表示。}
}
$$

---

### 舊主張：損失函數為 bottleneck distance

新版：

$$
\boxed{
d_B
\text{ 僅為 persistence component 的合法候選 loss。}
}
$$

---

### 舊主張：模型與目標理論形狀同構

新版：

$$
\boxed{
\Phi(T_{\mathrm{model}})
\cong_{\mathfrak I}
\Phi(T_{\mathrm{target}})
}
$$

只能在明確 representation 與 identity criterion 下提出。

---

### 舊結構：只突出 topology

新版：

$$
\boxed{
\text{topology}
+
\text{nesting}
+
\text{connection}
+
\text{path/history}
+
\text{identity specification}.
}
$$

---

### 舊 NTLA：觀察者未正式進入核心

新版：

$$
\boxed{
K_n
\rightarrow
K_{n,\mathcal O}
}
$$

預留完整 NTLA-O 接口。

---

# 28. 理論強度聲明

本文的核心數學工作主要屬於：

- 結構定義；
- 等價關係與 kernel；
- 逆系統；
- 多解析度表示；
- 拓樸不變量的條件性使用；
- 差異敏感身份規格。

本文不宣稱：

- 創造持續同調；
- 創造 bottleneck distance；
- 創造 inverse systems；
- 已證明新的 persistence stability theorem；
- 已建立一般機器學習的完備理論；
- 已證明所有知識具有唯一拓樸；
- 已證明 NTLA 優於現有學習架構。

NTLA 2.0 的正式地位為：

$$
\boxed{
\text{formal structural framework}
+
\text{research program}.
}
$$

---

# 29. 系列接口

本文是 NTLA-O 九篇系列的基礎篇。

後續將依序處理：

$$
\boxed{
\text{Observer Roles}
}
$$

$$
\Downarrow
$$

$$
\boxed{
\text{Set-Theoretic Foundations}
}
$$

$$
\Downarrow
$$

$$
\boxed{
\text{Observer-Induced Topology}
}
$$

$$
\Downarrow
$$

$$
\boxed{
\text{Local--Global Gluing}
}
$$

$$
\Downarrow
$$

$$
\boxed{
\text{Path / Groupoid Identity}
}
$$

$$
\Downarrow
$$

$$
\boxed{
\text{Inverse Observer Towers}
}
$$

$$
\Downarrow
$$

$$
\boxed{
\text{Complete Separation}
}
$$

$$
\Downarrow
$$

$$
\boxed{
\text{Unified NTLA-O}.
}
$$

---

# 30. 結論

NTLA 2.0 保留原 NTLA 最重要的思想：

$$
\boxed{
\text{複雜知識不必被壓縮成單層表示；
它可以具有可逐層展開的結構形狀。}
}
$$

但新版拒絕三種過度簡化：

$$
\boxed{
\text{拓樸摘要}
=
\text{完整身份},
}
$$

$$
\boxed{
\text{單一距離}
=
\text{完整學習},
}
$$

以及：

$$
\boxed{
\text{同一最終結果}
=
\text{同一結構歷史}.
}
$$

因此新版的真正核心變成：

$$
\boxed{
\text{Nested Structure}
+
\text{Difference Preservation}
+
\text{Explicit Quotient Rules}.
}
$$

而當觀察者進入後，還要再增加：

$$
\boxed{
\text{Who is allowed to distinguish what?}
}
$$

即：

$$
\boxed{
\text{誰能合法區分哪些差異？}
}
$$

這正是 NTLA-O 的起點。

---

# 參考文獻

1. Carlsson, G. (2009). *Topology and Data*. Bulletin of the American Mathematical Society, 46(2), 255–308.
2. Cohen-Steiner, D., Edelsbrunner, H., & Harer, J. (2007). *Stability of Persistence Diagrams*. Discrete & Computational Geometry, 37, 103–120.
3. Chazal, F., de Silva, V., Glisse, M., & Oudot, S. (2016). *The Structure and Stability of Persistence Modules*. Springer.
4. Chazal, F., Crawley-Boevey, W., & de Silva, V. (2016). *The Observable Structure of Persistence Modules*. Homology, Homotopy and Applications.
5. Edelsbrunner, H., & Harer, J. (2010). *Computational Topology: An Introduction*. American Mathematical Society.
6. Achddou, R., di Martino, J. M., & Sapiro, G. (2020). *Nested Learning for Multi-Granular Tasks*.
7. Behrouz, A., Razaviyayn, M., Zhong, P., & Mirrokni, V. (2025). *Nested Learning: The Illusion of Deep Learning Architectures*.
8. Neo.K & Theia (2026). *崁套拓樸代數學習架構*, EML-NTLA-2026-v1.0. Historical predecessor.
9. Neo.K et al. (2026). *拓撲相位計算論：萬物形狀的計算本體論*. Internal theoretical integration reference.

---

**文件狀態：** Formal Draft v0.1  
**修訂地位：** 建議作為 EML-NTLA-2026-v1.0 的後繼 canonical draft；舊版保留為 historical version，不直接覆寫。