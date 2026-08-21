# NTLA-O IV：局部—全域觀察、Presheaf、Sheaf、Stalk 與 Descent
## 從內部觀察者的局部狀態、相容黏合到全域重建障礙

**英文題名：** *NTLA-O IV: Local-to-Global Observation — Presheaves, Sheaves, Stalks, Germs, and Descent*  
**系列：** NTLA-O Series, Paper 5  
**版本：** v0.1 Formal Draft  
**前置論文：**《NTLA-O III：觀察拓樸、不可區分核與商空間》  
**作者：** Neo.K  
**理論整理與形式化協作：** Aletheia / GPT-5.6 Sol  
**日期：** 2026-08-17

---

## 摘要

前文已將 NTLA-O 觀察者的集合論區分族：

$$
\mathcal A_{\mathcal O}
\subseteq
\mathcal P(X)
$$

拓樸閉包化為：

$$
\tau_{\mathcal O},
$$

並建立 observer kernel：

$$
K_{\mathcal O},
$$

specialization preorder：

$$
\preceq_{\mathcal O},
$$

與 observer-relative quotient：

$$
X/K_{\mathcal O}.
$$

然而，拓樸只告訴我們：

> **哪些局部區域可以作為合法的開觀察域？**

它尚未說明：

> **一個內部觀察者在這些局部域中究竟持有哪些資料，以及不同局部觀察者的資料何時能夠共同形成全域狀態？**

本文因此將 NTLA-O 的內部觀察者進一步表示為開集上的局部 section。

對 observer topology：

$$
(X,\tau_{\mathcal O}),
$$

定義：

$$
\mathscr F(U)
$$

為開集：

$$
U\in\tau_{\mathcal O}
$$

上的合法局部觀察狀態集合。

若：

$$
V\subseteq U,
$$

存在 restriction map：

$$
\rho^U_V:
\mathscr F(U)
\rightarrow
\mathscr F(V),
$$

且滿足單位與複合一致性，便得到一個 presheaf。

本文強調：

$$
\boxed{
\text{presheaf}
\not\Rightarrow
\text{local data can always be globally glued}.
}
$$

Sheaf condition 正是額外要求：若一組局部 sections 在所有 overlap 上彼此一致，則存在唯一的全域 section 黏合它們。標準 sheaf 理論可把此條件寫成覆蓋上的 equalizer；Stacks Project 明確以此作為 sheaf condition 的範疇表達。

本文進一步利用 stalk：

$$
\mathscr F_x
=
\varinjlim_{x\in U}
\mathscr F(U)
$$

建立「點級內部觀察狀態」。Stalk 中的元素是 germ：兩個局部 section 只要在某個更小的共同鄰域上一致，就代表同一局部 germ。這是標準 stalk construction。

由此，NTLA-O 的觀察身份得到新的層級：

$$
\boxed{
\text{global identity}
\Rightarrow
\text{local-section identity}
\Rightarrow
\text{germ identity},
}
$$

而反方向一般不成立。

本文亦引入 descent 語言。當不同局部觀察資料不是字面相同，而是透過 transition isomorphisms：

$$
\varphi_{ij}
$$

互相對應時，三重 overlap 上的 cocycle condition 成為全域相容性的基本約束；這正是標準 descent data 的核心形式。

因此 NTLA-O 的局部—全域問題被精確拆分為：

$$
\boxed{
\text{Local Validity}
}
$$

$$
+
$$

$$
\boxed{
\text{Pairwise Compatibility}
}
$$

$$
+
$$

$$
\boxed{
\text{Higher Coherence}
}
$$

$$
+
$$

$$
\boxed{
\text{Effective Gluing}.
}
$$

局部觀察者很多、甚至每個局部都正確，皆不足以單獨推出全域主觀察狀態存在。

**關鍵詞：** NTLA-O、presheaf、sheaf、stalk、germ、descent、局部—全域、內部觀察者、黏合、cocycle、observer reconstruction

---

# 1. 從 Observer Topology 到局部 Observer State

前文建立：

$$
\boxed{
(X,\tau_{\mathcal O}).
}
$$

其中：

$$
U\in\tau_{\mathcal O}
$$

表示：

> $U$ 是相對於觀察者制度允許作為局部觀察區域的 open domain。

但：

$$
U
$$

本身不是 observation state。

因此本文增加：

$$
\boxed{
\mathscr F(U).
}
$$

$\mathscr F(U)$ 表示：

> 在局部域 $U$ 上可以合法存在的 observation states。

例如它可以是：

- 局部測量值；
- 局部拓樸資料；
- 局部結構標籤；
- 局部函數；
- 局部模型；
- 局部判定；
- 局部連接資料；
- 局部 Agent state。

本文暫不限制其具體內容。

---

# 2. Restriction

若：

$$
V\subseteq U,
$$

則一個在 $U$ 上合法的 observation state 應該可以被限制到更小的區域 $V$。

因此定義：

$$
\boxed{
\rho^U_V:
\mathscr F(U)
\rightarrow
\mathscr F(V).
}
$$

亦記：

$$
s
\mapsto
s|_V.
$$

這回答：

> 一個較大局部域中的 observation，當視野縮小時留下什麼？

---

# 3. Presheaf Observer

## 定義 3.1

若對所有開集：

$$
U\in\tau_{\mathcal O}
$$

皆給定：

$$
\mathscr F(U),
$$

並對所有：

$$
W\subseteq V\subseteq U
$$

給定 restriction maps，使：

$$
\rho^U_U
=
\operatorname{id}_{\mathscr F(U)}
$$

以及：

$$
\boxed{
\rho^V_W
\circ
\rho^U_V
=
\rho^U_W,
}
$$

則：

$$
\boxed{
\mathscr F
}
$$

稱為 NTLA-O observer presheaf。

這就是標準 presheaf 在開集包含範疇上的反變結構；Stacks Project 的 sheaf framework 也是從此類 presheaf 開始。

---

# 4. Presheaf 的觀察者解釋

在 NTLA-O 中：

$$
\mathscr F(U)
$$

可以理解為：

$$
\boxed{
\text{all admissible internal-observer states supported on }U.
}
$$

而：

$$
\rho^U_V
$$

表示：

$$
\boxed{
\text{observer state under domain restriction}.
}
$$

所以內部觀察者不再只有：

$$
S_I\subsetneq X.
$$

還可以攜帶：

$$
\boxed{
s_I\in\mathscr F(S_I).
}
$$

完整寫為：

$$
\boxed{
I=(S_I,s_I).
}
$$

---

# 5. 主觀察者的 Sheaf 模型

若：

$$
X
$$

本身為整個參考域，

則：

$$
\mathscr F(X)
$$

表示全域 observation states。

因此在本篇採用的 sheaf model 中，一個主域全域狀態可以寫為：

$$
\boxed{
s_M\in\mathscr F(X).
}
$$

注意：

這不是說：

$$
\boxed{
\text{所有主觀察者本體上等於 global section}.
}
$$

而只是：

> 在本文的 local-to-global 模型中，global section 為主域完整 observation state 的自然數學表示。

角色定義：

$$
S_M=X
$$

仍由前篇保留。

---

# 6. 局部 Restrictions 必須來自同一 Global State 嗎？

若已知：

$$
s\in\mathscr F(X),
$$

則對任何：

$$
U\subseteq X
$$

自然得到：

$$
s|_U.
$$

因此：

$$
\boxed{
\text{Global}
\rightarrow
\text{Local}
}
$$

通常沒有問題。

真正困難的是反方向：

$$
\boxed{
\text{Local}
\rightarrow
\text{Global}?
}
$$

---

# 7. 開覆蓋

令：

$$
\mathcal U
=
\{U_i\}_{i\in I}
$$

為：

$$
X
$$

的一個開覆蓋：

$$
\boxed{
X
=
\bigcup_{i\in I}U_i.
}
$$

每一個局部 observer 提供：

$$
s_i
\in
\mathscr F(U_i).
$$

問題是：

> 是否存在某：

$$
s\in\mathscr F(X)
$$

使：

$$
s|_{U_i}=s_i
$$

對所有 $i$ 成立？

---

# 8. Pairwise Compatibility

一個最低必要條件是：

$$
\boxed{
s_i|_{U_i\cap U_j}
=
s_j|_{U_i\cap U_j}
}
$$

對所有：

$$
i,j.
$$

如果不成立，兩個局部 observation 在共同可觀察域中直接衝突。

因此定義：

$$
\boxed{
\operatorname{Compat}(s_i,s_j)=1
}
$$

當且僅當：

$$
s_i|_{U_i\cap U_j}
=
s_j|_{U_i\cap U_j}.
$$

---

# 9. Local Compatibility 是必要條件

如果：

$$
s\in\mathscr F(X)
$$

確實存在，且：

$$
s_i=s|_{U_i},
$$

則：

$$
s_i|_{U_i\cap U_j}
=
s|_{U_i\cap U_j}
=
s_j|_{U_i\cap U_j}.
$$

因此：

---

# 定理 1：Global State Implies Local Compatibility

若一組局部 states：

$$
\{s_i\}
$$

來自同一：

$$
s\in\mathscr F(X),
$$

則：

$$
\boxed{
\forall i,j,
\quad
s_i|_{U_i\cap U_j}
=
s_j|_{U_i\cap U_j}.
}
$$

證畢。

---

# 10. 但 Compatibility 不足以保證 Global State

這正是 presheaf 與 sheaf 的分界。

---

# 11. 一個 NTLA-O Presheaf 反例

令：

$$
X=\mathbb R
$$

取通常拓樸。

定義：

$$
\mathscr B(U)
=
\{
f:U\rightarrow\mathbb R
\mid
f
\text{ 連續且有界}
\}.
$$

限制函數就是普通函數 restriction。

這形成 presheaf。

現在取開覆蓋：

$$
U_n
=
(n-1,n+1),
\qquad
n\in\mathbb Z.
$$

定義：

$$
f_n:
U_n
\rightarrow
\mathbb R
$$

為：

$$
\boxed{
f_n(x)=x.
}
$$

因每個：

$$
U_n
$$

有界，

所以：

$$
f_n
$$

在：

$$
U_n
$$

上有界。

因此：

$$
f_n\in\mathscr B(U_n).
$$

在所有 overlap：

$$
U_n\cap U_m
$$

上，

兩者都只是：

$$
x\mapsto x.
$$

因此完全相容：

$$
f_n|_{U_n\cap U_m}
=
f_m|_{U_n\cap U_m}.
$$

然而若存在：

$$
f\in\mathscr B(\mathbb R)
$$

黏合所有 $f_n$，

則必須：

$$
f(x)=x
$$

對所有：

$$
x\in\mathbb R.
$$

但：

$$
x\mapsto x
$$

在：

$$
\mathbb R
$$

上無界。

所以：

$$
f\notin\mathscr B(\mathbb R).
$$

因此不存在符合此 presheaf 定義的 global section。

所以：

$$
\boxed{
\text{pairwise compatible local data}
\not\Rightarrow
\text{global section in an arbitrary presheaf}.
}
$$

---

# 12. Sheaf Condition

因此需要額外公理。

標準 sheaf condition 要求：對任意開覆蓋，一族相容 local sections 必須存在唯一 global section 黏合它們；在範疇語言中，此條件可寫成一個 equalizer diagram。

---

## 定義 12.1：NTLA-O Observer Sheaf

若 observer presheaf：

$$
\mathscr F
$$

滿足以下兩條：

### Locality / Uniqueness

若：

$$
s,t\in\mathscr F(U)
$$

且：

$$
s|_{U_i}
=
t|_{U_i}
$$

對某個開覆蓋：

$$
U=\bigcup_iU_i
$$

的所有 $i$ 成立，

則：

$$
\boxed{
s=t.
}
$$

### Gluing / Existence

若：

$$
s_i\in\mathscr F(U_i)
$$

滿足：

$$
s_i|_{U_i\cap U_j}
=
s_j|_{U_i\cap U_j}
$$

對所有 $i,j$ 成立，

則存在：

$$
s\in\mathscr F(U)
$$

使：

$$
s|_{U_i}=s_i.
$$

則稱：

$$
\boxed{
\mathscr F
}
$$

為 NTLA-O observer sheaf。

---

# 定理 2：Internal Observer Gluing 定理

設：

$$
X=\bigcup_iU_i,
$$

且：

$$
\mathscr F
$$

為 observer sheaf。

若：

$$
s_i\in\mathscr F(U_i)
$$

滿足：

$$
\boxed{
s_i|_{U_i\cap U_j}
=
s_j|_{U_i\cap U_j}
}
$$

對所有：

$$
i,j,
$$

則存在唯一：

$$
\boxed{
s\in\mathscr F(X)
}
$$

使：

$$
s|_{U_i}=s_i
$$

對所有 $i$。

### 證明

這正是 sheaf existence 與 uniqueness 公理。

證畢。

這是標準 sheaf gluing principle；Stacks Project 對 sections 的存在與唯一黏合有直接表述。

---

# 13. NTLA-O 的局部—全域閉合式

因此在 sheaf 模型中：

$$
\boxed{
\text{Covering}
}
$$

$$
+
$$

$$
\boxed{
\text{Local States}
}
$$

$$
+
$$

$$
\boxed{
\text{Overlap Compatibility}
}
$$

$$
+
$$

$$
\boxed{
\text{Sheaf Property}
}
$$

推出：

$$
\boxed{
\text{Unique Global State}.
}
$$

可以壓成：

$$
\boxed{
\{
s_i
\}_{i\in I}
\xrightarrow{\mathrm{compatible}}
s.
}
$$

---

# 14. 「所有內部觀察者都對」仍不夠

現在可以很清楚地分出三種情況。

### 情況 A：局部 observer 本身錯誤

某：

$$
s_i
$$

甚至不屬於：

$$
\mathscr F(U_i).
$$

即：

$$
\boxed{
\text{local invalidity}.
}
$$

### 情況 B：每個局部都合法，但 overlap 衝突

$$
s_i|_{U_i\cap U_j}
\neq
s_j|_{U_i\cap U_j}.
$$

即：

$$
\boxed{
\text{compatibility failure}.
}
$$

### 情況 C：全部局部合法且 pairwise compatible，但 presheaf 不具 sheaf property

可能仍然沒有 global section。

即：

$$
\boxed{
\text{global realization failure}.
}
$$

所以：

$$
\boxed{
\text{local correctness}
\neq
\text{global reconstructibility}.
}
$$

---

# 15. Equalizer 形式

對開覆蓋：

$$
U=\bigcup_iU_i,
$$

sheaf condition 可以寫成：

$$
\boxed{
\mathscr F(U)
\longrightarrow
\prod_i
\mathscr F(U_i)
\rightrightarrows
\prod_{i,j}
\mathscr F(U_i\cap U_j).
}
$$

其中兩個右箭頭分別是：

$$
(s_i)_i
\mapsto
(s_i|_{U_i\cap U_j})_{i,j},
$$

與：

$$
(s_i)_i
\mapsto
(s_j|_{U_i\cap U_j})_{i,j}.
$$

Sheaf condition 要求：

$$
\mathscr F(U)
$$

正好是這兩個箭頭的 equalizer。這是標準範疇形式。

---

# 16. Observer Globalization Operator

在相容 local data 上，可以抽象記：

$$
\boxed{
\operatorname{Glue}_{\mathscr F}
:
\operatorname{Compat}
\left(
\prod_i\mathscr F(U_i)
\right)
\rightarrow
\mathscr F(U).
}
$$

若：

$$
\mathscr F
$$

為 sheaf，

則：

$$
\operatorname{Glue}_{\mathscr F}
$$

在每一組 compatible family 上唯一有定義。

因此：

$$
\boxed{
\text{global observer reconstruction}
}
$$

可以被理解為：

$$
\boxed{
\text{sheaf gluing}.
}
$$

---

# 17. Stalk：把內部觀察者縮到一個點附近

若我們不關心固定大小的局部域，而只問：

> 在點 $x$ 附近，observer 最終保留了什麼局部資訊？

則考慮所有包含：

$$
x
$$

的開鄰域：

$$
U\ni x.
$$

Stalk 定義為 directed colimit：

$$
\boxed{
\mathscr F_x
=
\varinjlim_{x\in U}
\mathscr F(U).
}
$$

Stacks Project 將 stalk 定義為這種鄰域系統下的 colimit，並將 section 在 stalk 中的像稱為 germ。

---

# 18. Germ

取：

$$
s\in\mathscr F(U),
\qquad
x\in U.
$$

其在：

$$
x
$$

處的 germ 記為：

$$
\boxed{
s_x\in\mathscr F_x.
}
$$

兩個局部 sections：

$$
s\in\mathscr F(U),
$$

$$
t\in\mathscr F(V)
$$

在 $x$ 處具有相同 germ，當且僅當存在：

$$
W\subseteq U\cap V,
\qquad
x\in W,
$$

使：

$$
\boxed{
s|_W=t|_W.
}
$$

---

# 19. Germ Observer Identity

因此定義：

$$
\boxed{
s
\equiv_{\mathrm{germ},x}
t
}
$$

當且僅當：

$$
s_x=t_x.
$$

這是一種比 section identity 更局部的 observer identity。

可能：

$$
s\neq t
$$

作為 $U$ 上的 sections，

但：

$$
\boxed{
s_x=t_x.
}
$$

因為它們只在遠離 $x$ 的地方不同。

---

# 20. Identity Hierarchy

因此 NTLA-O 至少得到：

$$
\boxed{
\text{Global Section Identity}
}
$$

$$
\Downarrow
$$

$$
\boxed{
\text{Restriction Identity on }U
}
$$

$$
\Downarrow
$$

$$
\boxed{
\text{Germ Identity at }x.
}
$$

若：

$$
s=t
$$

全域成立，

則其所有 restrictions 與 germs 當然相同。

但：

$$
s_x=t_x
$$

通常不能推出：

$$
s=t.
$$

因此：

$$
\boxed{
\text{germ identity}
}
$$

是更粗粒度的局部身份。

---

# 21. Germ Difference Emergence

對兩個局部 observation states：

$$
s,t,
$$

可以定義其差異支撐：

$$
\boxed{
\operatorname{Diff}(s,t)
=
\{
x:
s_x\neq t_x
\}.
}
$$

若：

$$
x\notin\operatorname{Diff}(s,t),
$$

代表兩個 observations 在 $x$ 附近局部一致。

因此 NTLA 原本的：

> 差異到底在哪裡發生？

現在可以變成：

$$
\boxed{
\text{差異首次在那些 stalks 上分裂？}
}
$$

---

# 22. Sheaf Sections 可由 Stalks 檢查相等

Sheaf 的局部性意味著，如果兩個 sections 在每一點的 germ 都相同，則它們本身相同。Stacks Project 明確指出，對 sheaf，section 到所有 stalks 的自然映射是 injective。

---

# 定理 3：Stalkwise Identity Determines Section Identity

若：

$$
\mathscr F
$$

為 sheaf，

且：

$$
s,t\in\mathscr F(U),
$$

並滿足：

$$
\boxed{
\forall x\in U,
\quad
s_x=t_x,
}
$$

則：

$$
\boxed{
s=t.
}
$$

### 證明

對每個：

$$
x\in U,
$$

由：

$$
s_x=t_x
$$

存在開鄰域：

$$
V_x\ni x
$$

使：

$$
s|_{V_x}
=
t|_{V_x}.
$$

而：

$$
U
=
\bigcup_{x\in U}V_x.
$$

由 sheaf uniqueness：

$$
s=t.
$$

證畢。

---

# 23. Stalkwise 完整並不代表單一 Stalk 全知

定理 3 使用的是：

$$
\boxed{
\forall x\in U.
}
$$

不是：

$$
\boxed{
\exists x.
}
$$

所以單一 stalk：

$$
\mathscr F_x
$$

通常不足以恢復整個 global section。

因此：

$$
\boxed{
\text{perfectly detailed local observer}
\not\Rightarrow
\text{global observer}.
}
$$

這再次支持：

$$
\boxed{
\text{Internal}
\neq
\text{Incomplete by definition},
}
$$

但也：

$$
\boxed{
\text{Internal local completeness}
\neq
\text{global completeness}.
}
$$

---

# 24. Observer Cover

現在可以把一組內部觀察者正式寫成：

$$
\boxed{
\mathfrak I
=
\{
(U_i,s_i)
\}_{i\in I}
}
$$

其中：

$$
X=\bigcup_iU_i.
$$

稱為：

# **Internal Observer Cover**

其完整性至少需要兩個不同條件：

### Spatial Coverage

$$
\boxed{
X=\bigcup_iU_i.
}
$$

### State Compatibility

$$
\boxed{
s_i|_{U_i\cap U_j}
=
s_j|_{U_i\cap U_j}.
}
$$

所以：

$$
\boxed{
\text{coverage}
\neq
\text{coherence}.
}
$$

---

# 25. Coverage 不足的反例

若：

$$
\bigcup_iU_i
\neq
X,
$$

則即使所有局部 states 完全相容，

仍存在：

$$
x\in
X\setminus
\bigcup_iU_i
$$

沒有任何 local observation。

因此不能僅靠這些 sections 唯一決定 $X$ 上全部資料。

所以：

$$
\boxed{
\text{observer multiplicity}
\neq
\text{domain coverage}.
}
$$

再多 observer，如果全部擠在同一區域，仍然可能完全看不到其他區域。

---

# 26. Sheafification：把可局部黏合的資訊補成 Sheaf

標準 sheaf theory 對任意 presheaf：

$$
\mathscr F
$$

可以構造 sheafification：

$$
\boxed{
\mathscr F
\rightarrow
\mathscr F^\#.
}
$$

Stacks Project 明確給出此 canonical morphism 以及 sheafification construction。

在 NTLA-O 中，可以將：

$$
\mathscr F^\#
$$

理解為：

> 將原 presheaf 中局部可表示、但全域 closure 不足的 observation data，送入其標準 sheaf completion。

---

# 27. 但 Sheafification 不是「修正真理」

這一點必須非常小心。

$$
\boxed{
\mathscr F
\rightarrow
\mathscr F^\#
}
$$

是數學上的 universal sheafification。

它不代表：

$$
\boxed{
\text{原 observer 錯，而 sheafified observer 真。}
}
$$

例如前述「有界連續函數」presheaf 被 sheafification 後，可能允許局部有界但全域不必有界的 continuous functions。

這是在改變 admissible global-state class。

因此：

$$
\boxed{
\text{sheafification}
=
\text{closure/completion operation},
}
$$

不是認識論上的 truth correction。

---

# 28. Local Equality 與 Transition Equivalence

到目前為止，compatibility 使用：

$$
s_i=s_j
$$

在 overlap 上成立。

但更一般的情況是：

局部 observer 使用不同座標、不同表示、不同 gauge 或不同合法語言。

這時不要求：

$$
s_i|_{U_{ij}}
=
s_j|_{U_{ij}},
$$

而可以只要求存在 transition isomorphism：

$$
\boxed{
\varphi_{ij}
:
\mathscr F_i|_{U_{ij}}
\overset{\sim}{\longrightarrow}
\mathscr F_j|_{U_{ij}}.
}
$$

其中：

$$
U_{ij}=U_i\cap U_j.
$$

---

# 29. 三重 Overlap

只要求 pairwise transitions 還不夠。

對：

$$
U_{ijk}
=
U_i\cap U_j\cap U_k,
$$

從 $i$ 轉到 $k$ 可以有兩條路：

$$
i\rightarrow k
$$

或：

$$
i\rightarrow j\rightarrow k.
$$

一致性要求：

$$
\boxed{
\varphi_{ik}
=
\varphi_{jk}
\circ
\varphi_{ij}
}
$$

在三重 overlap 上成立。

更嚴格地，在 pullback/descent 語言中需使用相應 projections 的 pullbacks；這正是標準 descent datum 的 cocycle condition。

---

# 30. NTLA-O Cocycle Coherence

因此定義局部 observer transition family：

$$
\Phi
=
\{
\varphi_{ij}
\}.
$$

若：

$$
\boxed{
\varphi_{ii}
=
\operatorname{id},
}
$$

$$
\boxed{
\varphi_{ji}
=
\varphi_{ij}^{-1},
}
$$

以及：

$$
\boxed{
\varphi_{ik}
=
\varphi_{jk}\circ\varphi_{ij}
}
$$

在所有適當 overlap 上成立，

則稱：

$$
\Phi
$$

為 observer cocycle-coherent。

---

# 31. Pairwise Agreement 與 Higher Coherence 再次分離

即使：

$$
\varphi_{ij}
$$

對每一對 observer 都存在，

仍可能：

$$
\varphi_{ik}
\neq
\varphi_{jk}\circ\varphi_{ij}.
$$

此時 pairwise translation 全部存在，

但整個三者關係無法形成一致 global identification system。

所以：

$$
\boxed{
\text{pairwise translatability}
\not\Rightarrow
\text{global coherence}.
}
$$

這對多觀察者與多 Agent 系統尤其重要。

---

# 32. Descent Data

更一般地，標準 descent theory 研究：

> 局部對象及其 overlap isomorphisms，何時來自某個 global object？

Stacks Project 對 quasi-coherent sheaves 的 descent datum 就是以每個局部對象、pairwise isomorphisms 與 triple-overlap cocycle condition 定義。

因此 NTLA-O 可以抽象寫：

$$
\boxed{
\mathfrak D
=
\left(
\{F_i\},
\{\varphi_{ij}\}
\right)
}
$$

作為 observer descent datum。

---

# 33. Effective Descent

一組 descent data 若真正來自某個 global object：

$$
F,
$$

並且 local objects 可以由：

$$
F|_{U_i}
$$

恢復，

則稱該 descent datum effective。

標準 descent theory 正式區分「具有 descent datum」與「descent datum 是否 effective」。

NTLA-O 因此增加第四層：

$$
\boxed{
\text{Cocycle Coherence}
\not\Rightarrow
\text{Effective Global Realization}
}
$$

在一般 descent problem 中不能任意省略 effectiveness。

---

# 34. 四階局部—全域條件

因此一組內部 observers 要達到全域重建，至少需區分：

### 第一階：Local Legality

$$
s_i\in\mathscr F_i(U_i).
$$

### 第二階：Coverage

$$
X=\bigcup_iU_i.
$$

### 第三階：Overlap Coherence

字面 sheaf 模型：

$$
s_i|_{U_{ij}}
=
s_j|_{U_{ij}},
$$

或更一般：

$$
\varphi_{ij}.
$$

### 第四階：Effective Descent / Gluing

存在：

$$
s
$$

或 global object：

$$
F
$$

真正產生全部局部資料。

因此：

$$
\boxed{
\text{Local}
\rightarrow
\text{Compatible}
\rightarrow
\text{Coherent}
\rightarrow
\text{Effective Global}.
}
$$

---

# 35. 主觀察狀態的兩種生成方式

現在主域：

$$
X
$$

的 global observer state 可以有兩種來源。

### 原生全域

直接已有：

$$
s_M\in\mathscr F(X).
$$

### 局部重建

由：

$$
\{
s_i
\}
$$

透過：

$$
\operatorname{Glue}
$$

得到：

$$
s_M.
$$

所以：

$$
\boxed{
\text{Main State}
}
$$

不必在所有模型裡被視為 primitive。

它可以在 sheaf model 中由 compatible internal observer states 重建。

---

# 36. 但「主體等於內部的總和」仍然不是一般定理

即使 sheaf gluing 成立，也不能寫：

$$
\boxed{
M
=
\sum_iI_i.
}
$$

因為：

- observer role 與 section data 不同；
- cover 本身需要選擇；
- restriction structure 是額外資料；
- gluing 是範疇／sheaf 構造，不是普通加法；
- local observers 可能重疊；
- global section 不是 local section 的集合聯集。

所以更準確寫成：

$$
\boxed{
\text{compatible local data}
\xrightarrow{\operatorname{Glue}}
\text{global data}.
}
$$

---

# 37. Observer Redundancy

假設某：

$$
U_k
$$

完全被其他開集覆蓋：

$$
U_k
\subseteq
\bigcup_{i\neq k}U_i,
$$

且：

$$
s_k
$$

由其 overlap restrictions 唯一決定。

則：

$$
I_k
$$

在 global reconstruction 上可能是冗餘 observer。

因此可以定義：

$$
\boxed{
\operatorname{Redundant}(I_k|\mathfrak I)=1
}
$$

若移除 $I_k$ 後，仍能唯一恢復同一 global section。

這給多觀察者系統一個新的最小化問題。

---

# 38. Minimal Observer Cover

定義：

$$
\boxed{
\mathfrak I_{\min}
}
$$

為滿足：

1. 覆蓋 $X$；
2. 局部資料足以唯一重建 global section；
3. 移除任一 observer 後至少破壞 coverage 或 uniqueness；

的 observer cover。

這可以稱為：

# **Minimal Reconstructive Observer Cover**

它與拓樸中的 minimal open cover 並不完全相同，因為還取決於 section information。

---

# 39. 多 Observer 的局部信任問題

如果每一個：

$$
I_i
$$

具有自己的：

$$
K_{I_i},
$$

則同一 overlap：

$$
U_{ij}
$$

上的資料可能在不同 observer resolution 下被不同程度商化。

因此真正 comparison 之前可能需要：

$$
\boxed{
C_{ij}
:
\mathscr F_i(U_{ij})
\rightarrow
\mathscr G_{ij}(U_{ij})
}
$$

與：

$$
C_{ji}
:
\mathscr F_j(U_{ij})
\rightarrow
\mathscr G_{ij}(U_{ij}),
$$

映射到共同 comparison domain。

此時 compatibility 改為：

$$
\boxed{
C_{ij}(s_i)
=
C_{ji}(s_j).
}
$$

這是 NTLA-O 相較最簡 sheaf model 的重要擴張候選。

---

# 40. 判定域依賴的 Sheaf

更一般地：

$$
\mathscr F
$$

本身可能依賴 observer judgment domain：

$$
\mathcal J.
$$

寫成：

$$
\boxed{
\mathscr F_{\mathcal J}.
}
$$

改變：

$$
\mathcal J
$$

可能同時改變：

- 可用 sections；
- compatibility；
- restriction maps；
- gluing 結果。

因此：

$$
\boxed{
\mathcal J_1\neq\mathcal J_2
}
$$

可能導致：

$$
\boxed{
\mathscr F_{\mathcal J_1}
\neq
\mathscr F_{\mathcal J_2}.
}
$$

這將為後續 observer transition 提供接口。

---

# 41. Observer Stalk 與 NTLA 嵌套

考慮：

$$
U_0
\supseteq
U_1
\supseteq
U_2
\supseteq
\cdots
\ni x.
$$

局部 observer states：

$$
s_n\in\mathscr F(U_n)
$$

透過 restrictions：

$$
s_n|_{U_{n+1}}
$$

逐步向更小鄰域傳遞。

Stalk：

$$
\mathscr F_x
$$

將所有這類局部描述按「在足夠小鄰域相同」商化。

所以 stalk 可以理解為：

$$
\boxed{
\text{nested local observer limit under germ equivalence}.
}
$$

但技術上它是：

$$
\boxed{
\text{direct limit / colimit},
}
$$

不是前文 quotient tower 的 inverse limit。

這一方向差異必須保留。

---

# 42. Direct 與 Inverse 兩種觀察塔

因此 NTLA-O 現在第一次同時存在：

### 向局部縮小

$$
U_0
\supseteq
U_1
\supseteq
U_2
\supseteq
\cdots
$$

sections 經 restriction 形成 directed system，最終進入：

$$
\boxed{
\mathscr F_x
=
\varinjlim
\mathscr F(U).
}
$$

### 向解析精化

$$
K_0
\supseteq
K_1
\supseteq
K_2
\supseteq
\cdots
$$

quotients 形成：

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

後者在 Paper 7 將進入 inverse limit。

所以：

$$
\boxed{
\text{localization}
\neq
\text{resolution refinement}.
}
$$

---

# 43. Locality–Resolution 二維網格

可以因此建立：

$$
\boxed{
\mathscr F_{n}(U)
}
$$

其中：

$$
n
$$

代表 observation resolution，

$$
U
$$

代表 spatial/local domain。

於是：

$$
\mathscr F_n(U)
$$

形成二維結構：

$$
\boxed{
\text{resolution axis}
\times
\text{locality axis}.
}
$$

沿：

$$
V\subseteq U
$$

做 restriction。

沿：

$$
n\rightarrow n+1
$$

做 refinement。

這將是 NTLA-O 後面非常重要的統一結構。

---

# 44. Main／Internal 角色的新座標

前文：

$$
\mathbf O_{\mathrm{top}}
=
(\rho,\tau,K,\preceq).
$$

本文加入 section state：

$$
\boxed{
\mathbf O_{\mathrm{local}}
=
\left(
\rho,
U,
s_U,
\tau,
K,
\preceq
\right).
}
$$

其中：

$$
U=X
$$

時可作為 global/main-state model；

$$
U\subsetneq X
$$

時為 internal/local-state model。

若再縮到 germ：

$$
\boxed{
\mathbf O_{x}
=
\left(
\rho,
x,
s_x,
K,
\ldots
\right).
}
$$

---

# 45. Local Observer Difference

對：

$$
s,t\in\mathscr F(U),
$$

定義：

$$
\boxed{
\Delta_{\mathrm{loc}}(s,t)
=
\{
x\in U:
s_x\neq t_x
\}.
}
$$

則由定理 3：

$$
\boxed{
\Delta_{\mathrm{loc}}(s,t)
=
\varnothing
\iff
s=t.
}
$$

前提是：

$$
\mathscr F
$$

為 sheaf。

因此 global section difference 可以完全被 stalkwise difference support 偵測。

---

# 定理 4：Stalk Separation of Sheaf Sections

對 sheaf：

$$
\mathscr F,
$$

映射：

$$
\boxed{
\eta_U:
\mathscr F(U)
\rightarrow
\prod_{x\in U}\mathscr F_x
}
$$

定義為：

$$
s
\mapsto
(s_x)_{x\in U}.
$$

則：

$$
\boxed{
\eta_U
\text{ 為單射}.
}
$$

### 證明

若：

$$
\eta_U(s)=\eta_U(t),
$$

則：

$$
s_x=t_x
$$

對全部：

$$
x\in U.
$$

由定理 3：

$$
s=t.
$$

故單射。

證畢。

此性質亦為標準 sheaf/stalk 結果。

---

# 46. 但不是所有 Stalk Family 都來自 Global Section

雖然：

$$
\mathscr F(U)
\hookrightarrow
\prod_{x\in U}\mathscr F_x,
$$

一般不能反過來寫：

$$
\prod_{x\in U}\mathscr F_x
\rightarrow
\mathscr F(U)
$$

為任意滿射。

任意選一個 germ：

$$
g_x\in\mathscr F_x
$$

對每個點 $x$，

不代表它們具有局部相容性。

所以：

$$
\boxed{
\text{pointwise local possibility}
\not\Rightarrow
\text{global realizability}.
}
$$

---

# 47. 這形成 NTLA-O 的第二個局部—全域障礙

第一個障礙：

$$
\boxed{
\text{local sections fail overlap compatibility}.
}
$$

第二個障礙：

$$
\boxed{
\text{arbitrary stalk assignments fail local realizability}.
}
$$

所以 observer system 若要從「所有點各自的可能狀態」恢復真正 global observation，仍然需要 coherence structure。

---

# 48. 本篇主要定理群

本文建立或重新表述：

### 定理 A：Global State Implies Local Compatibility

$$
s
\mapsto
\{s|_{U_i}\}
$$

必然滿足 overlap compatibility。

### 定理 B：Internal Observer Gluing

對 sheaf：

$$
\boxed{
\text{compatible local sections}
\iff
\text{unique global glued section}
}
$$

在給定覆蓋與局部 family 的意義下成立。

### 定理 C：Stalkwise Identity Determines Section Identity

$$
\forall x,\;
s_x=t_x
\Longrightarrow
s=t.
$$

### 定理 D：Stalk Embedding

$$
\mathscr F(U)
\hookrightarrow
\prod_{x\in U}\mathscr F_x.
$$

### 反例 E：Presheaf Compatibility 不保證原 Presheaf Global Section

有界連續函數 presheaf 提供明確反例。

### 結構 F：Descent Cocycle

局部 transition maps 需要三重 overlap coherence。

---

# 49. 與傳統數學的界線

本文使用的：

- presheaf；
- sheaf；
- restriction；
- open cover；
- stalk；
- germ；
- sheafification；
- gluing；
- descent datum；
- cocycle condition；

均屬成熟的 sheaf/descent theory。Stacks Project 對 sheaf condition、stalk、sheafification、gluing 與 descent 均提供標準定義與構造。

NTLA-O 不宣稱發明這些數學對象。

本文自身的 candidate contribution 在於把它們組織成：

$$
\boxed{
\text{observer role}
+
\text{observer topology}
+
\text{observer kernel}
+
\text{local section}
+
\text{judgment/legality indexing}
}
$$

的同一框架。

---

# 50. 理論強度聲明

本文不宣稱：

- 現實世界本身必然是一個 sheaf；
- 所有內部觀察者都能黏成主觀察者；
- 所有 local truths 都能形成 global truth；
- global section 等於意識；
- stalk 等於主觀感受；
- sheafification 等於修正錯誤認知；
- descent obstruction 自動具有物理意義；
- 所有 multi-agent disagreement 都是 sheaf cohomology 問題。

本文只提出：

> 若某觀察系統具備 topology、local restriction 與 sheaf/descent 型結構，則傳統局部—全域數學可精確描述其 observation compatibility 與 reconstruction conditions。

---

# 51. 本篇核心結論

NTLA-O 到目前最大的變化，是正式把：

$$
\boxed{
\text{Internal Observer}
}
$$

從一個「位於主域內部的點或子域」，

提升成：

$$
\boxed{
(U,s_U).
}
$$

亦即：

> **一個內部位置，加上一個在該位置合法存在的局部觀察狀態。**

因此一群內部 observers：

$$
\{
(U_i,s_i)
\}
$$

能否形成 global state，不由它們的數量決定。

而由：

$$
\boxed{
\text{coverage}
}
$$

$$
+
$$

$$
\boxed{
\text{restriction consistency}
}
$$

$$
+
$$

$$
\boxed{
\text{overlap compatibility}
}
$$

$$
+
$$

$$
\boxed{
\text{higher coherence}
}
$$

$$
+
$$

$$
\boxed{
\text{effective gluing}
}
$$

共同決定。

所以：

$$
\boxed{
\text{Many Internal Observers}
\not\Rightarrow
\text{Global Observer}.
}
$$

而：

$$
\boxed{
\text{Compatible Internal Observer Cover}
+
\text{Sheaf Property}
}
$$

才推出：

$$
\boxed{
\text{Unique Global Observation State}.
}
$$

同時 stalk 給出另一個重要方向：

$$
\boxed{
\text{local domains}
\rightarrow
\text{germs}
}
$$

使 observation identity 第一次具有真正局部化版本。

因此目前 NTLA-O 已形成：

$$
\boxed{
\text{Set}
}
$$

$$
\rightarrow
$$

$$
\boxed{
\text{Distinction Family}
}
$$

$$
\rightarrow
$$

$$
\boxed{
\text{Observer Topology}
}
$$

$$
\rightarrow
$$

$$
\boxed{
\text{Local Sections}
}
$$

$$
\rightarrow
$$

$$
\boxed{
\text{Stalks / Germs}
}
$$

$$
\rightarrow
$$

$$
\boxed{
\text{Gluing / Descent}
}
$$

$$
\rightarrow
$$

$$
\boxed{
\text{Global State}.
}
$$

---

# 52. 下一篇

下一篇將處理一個 sheaf identity 還不能完整保存的問題：

> **即使起點與終點相同，觀察者經過不同路徑後，是否仍應被判定為同一狀態？**

因此將正式進入：

# **NTLA-O V：路徑身份、Fundamental Groupoid、Covering、Monodromy 與 Holonomy**

核心將是：

$$
\boxed{
\text{same endpoint}
\not\Rightarrow
\text{same transported state},
}
$$

並進一步區分：

$$
\boxed{
\text{raw path},
}
$$

$$
\boxed{
\text{path modulo reparameterization},
}
$$

$$
\boxed{
\text{homotopy class},
}
$$

$$
\boxed{
\text{fundamental-groupoid identity},
}
$$

以及：

$$
\boxed{
\text{history-sensitive NTLA identity}.
}
$$

這將正式回到原始 NTLA 最關鍵的直覺：

> **洞不只在於存在幾個；洞與洞怎麼連、怎麼走、沿什麼歷史連接，也可能本身就是不能被丟掉的結構。**

---

# 參考文獻

1. The Stacks Project, *Sheaves on Spaces*, Sections 6.7–6.13. Sheaf condition, algebraic-structure sheaves, stalks and germs.
2. The Stacks Project, Section 6.17, *Sheafification*.
3. The Stacks Project, Section 6.33, *Glueing Sheaves*.
4. The Stacks Project, Chapter *Descent*, and Section 35.2, *Descent Data for Quasi-Coherent Sheaves*.
5. Neo.K & Aletheia (2026). *NTLA-O III：觀察拓樸、不可區分核與商空間*.

---

**文件狀態：** Formal Draft v0.1  
**系列位置：** NTLA-O Series Paper 5 / 9  
**下一篇：** NTLA-O V — Path Identity, Fundamental Groupoids, Coverings, Monodromy, and Holonomy