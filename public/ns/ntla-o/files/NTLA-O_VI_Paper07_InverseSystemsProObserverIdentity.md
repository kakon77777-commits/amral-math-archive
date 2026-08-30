# NTLA-O VI：逆系統、Observer Tower、Inverse Limit 與 Pro-Observer Identity
## 從解析精化歷史、理想極限狀態到「極限同一不等於塔同一」

**英文題名：** *NTLA-O VI: Inverse Systems, Observer Towers, Inverse Limits, and Pro-Observer Identity — Resolution Histories Beyond Limit Equivalence*  
**系列：** NTLA-O Series, Paper 7  
**版本：** v0.1 Formal Draft  
**前置論文：**《NTLA-O V：路徑身份、基本群胚、覆蓋、Monodromy 與 Holonomy》  
**作者：** Neo.K  
**理論整理與形式化協作：** Aletheia / GPT-5.6 Sol  
**日期：** 2026-08-17

---

## 摘要

前五篇 NTLA-O 已建立四個主要觀察維度：

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

其中 observation resolution 由一族逐步精化的不可區分核描述：

$$
K_0
\supseteq
K_1
\supseteq
K_2
\supseteq
\cdots.
$$

每一個 $K_n$ 產生觀察商：

$$
Q_n
=
D/K_n,
$$

而 kernel inclusion 自然給出滿射：

$$
\pi_{n+1,n}:
Q_{n+1}
\rightarrow
Q_n.
$$

因此形成：

$$
\boxed{
Q_0
\leftarrow
Q_1
\leftarrow
Q_2
\leftarrow
\cdots,
}
$$

即標準 inverse system。逆系統由對象與相容 transition morphisms 構成，而其 inverse limit 是所有跨層相容元素族；這是標準範疇論定義。

本文建立 NTLA-O 的 **Observer Tower Theory**。

第一個主要結果為：令

$$
K_\infty
=
\bigcap_{n\geq0}K_n.
$$

則存在自然單射：

$$
\boxed{
D/K_\infty
\hookrightarrow
\varprojlim_nD/K_n.
}
$$

但此映射一般**不必滿射**。

因此 inverse limit 可能包含一組在所有有限 observation levels 上皆相容、卻不存在任何原始 $x\in D$ 能同時實現的「理想極限狀態」。本文以 $\mathbb N$ 上逐步分離有限前綴的 observer tower 給出明確例子，其中 inverse limit 自然多出一個可記為 $\infty$ 的極限點。

第二個主要結果為：

$$
\boxed{
\text{same inverse limit}
\not\Rightarrow
\text{same inverse system}.
}
$$

甚至：

$$
\boxed{
\text{same inverse limit}
\not\Rightarrow
\text{same pro-object}.
}
$$

本文以：

$$
\{\mathbb Z/p^n\mathbb Z\}_n
$$

與其 inverse limit $\mathbb Z_p$ 的常值系統為例：二者具有同構 inverse limit，但在 $\operatorname{Pro}(\mathbf{Ab})$ 中並不同構。

因此本文將 NTLA-O 身份拆成至少三層：

$$
\boxed{
\text{Strict Tower Identity}
}
$$

$$
\Longrightarrow
$$

$$
\boxed{
\text{Pro-Observer Identity}
}
$$

$$
\Longrightarrow
$$

$$
\boxed{
\text{Limit Identity},
}
$$

反向一般皆不成立。

Pro-category 的標準定義正是保留 cofiltered diagrams 本身，而非只取其極限；其 morphism 集由

$$
\operatorname{Hom}_{\operatorname{Pro}(\mathcal C)}(F,G)
=
\varprojlim_j
\varinjlim_i
\operatorname{Hom}_{\mathcal C}(F(i),G(j))
$$

給出。

本文因此提出：

$$
\boxed{
\mathbf{ProObs}(D)
}
$$

作為 observer resolution history 的自然結構。

最後，對自然數索引的 decreasing equivalence kernels，本文由首次分離階構造 observer pseudoultrametric。這使 NTLA-O 的 resolution history 同時可被理解為：

$$
\boxed{
\text{inverse system}
}
$$

與：

$$
\boxed{
\text{hierarchical ultrametric geometry}.
}
$$

因此 NTLA-O 原本的命題：

> 結果相同，不代表生成或觀察歷史相同，

在本篇得到新的精確形式：

$$
\boxed{
\varprojlim\mathfrak T
\cong
\varprojlim\mathfrak T'
\not\Rightarrow
\mathfrak T
\cong_{\mathrm{Pro}}
\mathfrak T'.
}
$$

**關鍵詞：** NTLA-O、逆系統、inverse limit、pro-object、observer tower、不可區分核、completion、ultrametric、resolution history、pro-category

---

# 1. 從單一 Observer Kernel 到 Observer Tower

前文定義：

$$
K_{\mathcal O}
=
\{
(x,y):
x\sim_{\mathcal O}y
\}.
$$

若 observer resolution 逐步增加，可得到：

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

其中：

$$
K_{n+1}\subseteq K_n
$$

表示第 $n+1$ 層至少保留第 $n$ 層已能保留的全部差異。

若：

$$
K_{n+1}\subsetneq K_n,
$$

則存在至少一對：

$$
x,y
$$

在第 $n$ 層仍不可區分，而在第 $n+1$ 層被分離。

---

# 2. 每個 Kernel 產生一個 Quotient

定義：

$$
\boxed{
Q_n
=
D/K_n.
}
$$

元素：

$$
[x]_n
$$

代表：

> 第 $n$ 層 observer 所能區分到的 $x$ 的有效身份。

由：

$$
K_{n+1}\subseteq K_n
$$

可定義：

$$
\boxed{
\pi_{n+1,n}:
Q_{n+1}
\rightarrow
Q_n
}
$$

為：

$$
\pi_{n+1,n}([x]_{n+1})
=
[x]_n.
$$

此映射良定且滿射。

---

# 定理 1：Observer Quotient Bonding 定理

若：

$$
K_j\subseteq K_i
\qquad
(i\leq j),
$$

則存在唯一自然滿射：

$$
\boxed{
\pi_{j,i}:
Q_j
\rightarrow
Q_i
}
$$

滿足：

$$
\pi_{i,i}
=
\operatorname{id}_{Q_i},
$$

以及：

$$
\boxed{
\pi_{k,i}
=
\pi_{j,i}
\circ
\pi_{k,j}
}
$$

對：

$$
i\leq j\leq k
$$

成立。

### 證明

定義：

$$
\pi_{j,i}([x]_j)
=
[x]_i.
$$

良定性由：

$$
K_j\subseteq K_i
$$

得到。

其餘兩式直接由 equivalence class projection 得到。

證畢。

---

# 3. Observer Tower 是標準 Inverse System

因此：

$$
\boxed{
\mathfrak T_{\mathrm{obs}}
=
\left(
Q_n,
\pi_{m,n}
\right)_{m\geq n}
}
$$

形成 inverse system。

標準 inverse system 要求 transition maps 滿足 identity 與 composition consistency；在自然數索引時通常寫成：

$$
M_1
\leftarrow
M_2
\leftarrow
M_3
\leftarrow
\cdots.
$$



所以 NTLA 2.0 原來的：

$$
T_0
\leftarrow
T_1
\leftarrow
T_2
\leftarrow
\cdots
$$

現在得到一個更精確的 observer interpretation：

$$
\boxed{
\text{resolution refinement}
\Longrightarrow
\text{inverse system of observational quotients}.
}
$$

---

# 4. Inverse Limit

定義：

$$
\boxed{
L
=
\varprojlim_nQ_n.
}
$$

在 Sets 中，inverse limit 的元素就是所有層的 compatible tuples：

$$
\boxed{
L
=
\left\{
(q_0,q_1,q_2,\ldots)
\in
\prod_nQ_n:
\pi_{n+1,n}(q_{n+1})=q_n
\right\}.
}
$$

這是標準 set-theoretic limit 描述。

因此一個：

$$
\ell\in L
$$

表示：

> 一個在所有 observation resolutions 上都彼此一致的身份序列。

---

# 5. Limit State 不是「最高有限層」

如果：

$$
Q_0
\leftarrow
Q_1
\leftarrow
\cdots
$$

沒有最後一項，

則：

$$
L
$$

不是某：

$$
Q_N
$$

的另一個名字。

它由整個 compatible system 定義。

所以：

$$
\boxed{
\text{limit}
\neq
\text{last finite stage}.
}
$$

---

# 6. 極限不可區分核

定義：

$$
\boxed{
K_\infty
=
\bigcap_{n=0}^\infty K_n.
}
$$

因此：

$$
xK_\infty y
$$

當且僅當：

$$
\boxed{
\forall n,
\quad
xK_ny.
}
$$

也就是：

> 任意有限 observation resolution 都無法分開 $x,y$。

---

# 7. 自然極限映射

每個：

$$
x\in D
$$

都產生：

$$
\boxed{
\eta(x)
=
(
[x]_0,
[x]_1,
[x]_2,\ldots
).
}
$$

因：

$$
\pi_{n+1,n}([x]_{n+1})
=
[x]_n,
$$

所以：

$$
\eta(x)\in L.
$$

因此存在：

$$
\boxed{
\eta:
D
\rightarrow
L.
}
$$

---

# 定理 2：Natural Limit Map Kernel 定理

$$
\boxed{
\ker\eta
=
K_\infty.
}
$$

其中 kernel 理解為：

$$
\eta(x)=\eta(y).
$$

### 證明

$$
\eta(x)=\eta(y)
$$

當且僅當對所有 $n$：

$$
[x]_n=[y]_n.
$$

這又當且僅當：

$$
(x,y)\in K_n
$$

對所有 $n$ 成立。

即：

$$
(x,y)\in
\bigcap_nK_n
=
K_\infty.
$$

證畢。

---

# 定理 3：Residual Quotient Injection

自然映射 $\eta$ 唯一因子化為：

$$
\boxed{
\bar\eta:
D/K_\infty
\hookrightarrow
\varprojlim_nD/K_n.
}
$$

且：

$$
\bar\eta
$$

為單射。

### 證明

由定理 2：

$$
\ker\eta=K_\infty.
$$

所以 $\eta$ 在 $K_\infty$ 等價類上為常值，因而下降到：

$$
D/K_\infty.
$$

若：

$$
\bar\eta([x]_\infty)
=
\bar\eta([y]_\infty),
$$

則：

$$
\eta(x)=\eta(y),
$$

由定理 2：

$$
xK_\infty y.
$$

故：

$$
[x]_\infty=[y]_\infty.
$$

因此：

$$
\bar\eta
$$

單射。

證畢。

---

# 8. 這個單射不一定是滿射

這是 NTLA-O inverse-limit 結構第一個真正重要的非平凡現象。

存在：

$$
\ell\in L
$$

使：

$$
\ell
$$

在每一有限 observation level 都合法且 compatible，

但不存在：

$$
x\in D
$$

使：

$$
\eta(x)=\ell.
$$

這些 limit elements 不是某個原始 object 的 observation history。

---

# 9. 明確反例：自然數 Observer Completion

令：

$$
D=\mathbb N.
$$

對：

$$
n\geq0
$$

定義等價關係：

$$
xK_ny
$$

當且僅當：

1. $x=y<n$；

或：

2. $x\geq n$ 且 $y\geq n$。

所以：

$$
Q_n
$$

具有：

$$
0,1,\ldots,n-1
$$

這些已被單獨辨識的點，

以及一個尚未分解的 tail class：

$$
\boxed{
T_n
=
\{n,n+1,n+2,\ldots\}.
}
$$

因此：

$$
Q_n
=
\{
[0],[1],\ldots,[n-1],T_n
\}.
$$

---

# 10. 此 Tower 逐步分離每一自然數

有：

$$
K_{n+1}\subsetneq K_n.
$$

因第 $n+1$ 層把：

$$
n
$$

從原來的 tail：

$$
T_n
$$

中分離。

而：

$$
\boxed{
K_\infty=\Delta_{\mathbb N}.
}
$$

因任意：

$$
x\neq y
$$

最終都會在足夠高的有限階被分開。

因此：

$$
D/K_\infty
=
\mathbb N.
$$

---

# 11. 但 Inverse Limit 多出一個狀態

考慮 coherent sequence：

$$
\boxed{
\ell_\infty
=
(T_0,T_1,T_2,\ldots).
}
$$

因：

$$
\pi_{n+1,n}(T_{n+1})
=
T_n,
$$

所以：

$$
\ell_\infty
\in
\varprojlim_nQ_n.
$$

然而不存在：

$$
m\in\mathbb N
$$

同時滿足：

$$
m\in T_n
$$

對所有 $n$。

因：

$$
\bigcap_{n=0}^{\infty}T_n
=
\varnothing.
$$

所以：

$$
\boxed{
\ell_\infty
\notin
\eta(\mathbb N).
}
$$

---

# 定理 4：Inverse Limit Can Add Ideal Observer States

存在 decreasing observer-kernel tower 使：

$$
K_\infty=\Delta_D
$$

但：

$$
\boxed{
D
\subsetneq
\varprojlim_nD/K_n
}
$$

透過自然嵌入。

上述 $\mathbb N$ construction 即為例子。

證畢。

---

# 12. Observer Completion

因此定義：

$$
\boxed{
\widehat D_{\mathrm{obs}}
=
\varprojlim_nD/K_n.
}
$$

稱為：

# **Observer Completion**

這個名稱是 NTLA-O 的解釋性術語。

它表示：

> 將所有跨有限 resolution 相容的身份序列也納入之後得到的完成域。

因此可能：

$$
\boxed{
D/K_\infty
\subsetneq
\widehat D_{\mathrm{obs}}.
}
$$

---

# 13. Realized 與 Ideal States

定義：

$$
\boxed{
L_{\mathrm{real}}
=
\operatorname{Im}\bar\eta.
}
$$

而：

$$
\boxed{
L_{\mathrm{ideal}}
=
L\setminus L_{\mathrm{real}}.
}
$$

稱後者為：

# **Ideal Observer States**

它們不是「虛假」狀態。

其精確意思只有：

> 每個有限層投影都合法且 compatible，但此 compatible family 沒有原始 $D$ 中的共同 representative。

---

# 14. Realization Completeness

定義 observer tower 為：

# **Realization-Complete**

若：

$$
\boxed{
\bar\eta:
D/K_\infty
\rightarrow
L
}
$$

為滿射。

此時：

$$
\boxed{
D/K_\infty
\cong
L.
}
$$

---

# 定理 5：Nested-Class Intersection Criterion

設：

$$
\ell=(C_n)_n\in L
$$

其中每個：

$$
C_n
$$

被視為 $K_n$ 的 equivalence class，則：

$$
C_{n+1}\subseteq C_n.
$$

而：

$$
\ell
$$

來自某：

$$
x\in D
$$

當且僅當：

$$
\boxed{
\bigcap_nC_n\neq\varnothing.
}
$$

### 證明

若：

$$
\eta(x)=\ell,
$$

則：

$$
x\in C_n
$$

對所有 $n$，所以交非空。

反之若存在：

$$
x\in\bigcap_nC_n,
$$

則：

$$
[x]_n=C_n
$$

對所有 $n$。

故：

$$
\eta(x)=\ell.
$$

證畢。

---

# 15. 完成性真正需要額外條件

所以：

$$
\boxed{
K_\infty=\Delta_D
}
$$

只證明：

> 不同原始點最終可以被 observation tower 分離。

它**不證明**：

> 每個極限相容 observation state 都來自一個原始點。

因此必須區分：

$$
\boxed{
\text{Separation Completeness}
}
$$

與：

$$
\boxed{
\text{Realization Completeness}.
}
$$

第一個是 kernel intersection 問題。

第二個是 nested-class intersection 問題。

---

# 16. 一個極其重要的否定式

因此：

$$
\boxed{
K_\infty=\Delta_D
}
$$

不推出：

$$
\boxed{
D
=
\varprojlim D/K_n.
}
$$

這修正了任何把「所有有限差異最終都能辨識」直接等同於「原域就是完整 inverse limit」的過強說法。

---

# 17. Difference Separation Rank

由 decreasing kernels，可為：

$$
x,y\in D
$$

定義：

$$
\boxed{
r_{\mathrm{sep}}(x,y)
=
\min
\{
n:
(x,y)\notin K_n
\}.
}
$$

若：

$$
(x,y)\in K_n
$$

對所有 $n$ 成立，令：

$$
r_{\mathrm{sep}}(x,y)=\infty.
$$

它表示：

> $x,y$ 首次在哪個 observation resolution 被分離。

---

# 18. 嚴格 Nested Kernel 的單調性

因：

$$
K_{n+1}\subseteq K_n,
$$

一旦：

$$
(x,y)\notin K_n,
$$

則對所有：

$$
m\geq n
$$

亦有：

$$
(x,y)\notin K_m.
$$

所以：

$$
r_{\mathrm{sep}}(x,y)
$$

是一個 well-defined threshold。

這就是 NTLA 早期「差異顯現階」的正式 observer-kernel 版本。

---

# 19. Agreement Depth

亦可定義：

$$
\boxed{
a(x,y)
=
\sup
\{
n:
(x,y)\in K_n
\}.
}
$$

若：

$$
xK_ny
$$

對所有 $n$，令：

$$
a(x,y)=\infty.
$$

直觀上：

> $a(x,y)$ 越大，表示二者要到越深 resolution 才被分開。

---

# 20. Observer Pseudoultrametric

假設自然數索引，定義：

$$
d_{\mathrm{obs}}(x,y)
=
\begin{cases}
0,
&
xK_\infty y,
\\[4pt]
2^{-r_{\mathrm{sep}}(x,y)},
&
\text{otherwise}.
\end{cases}
$$

---

# 定理 6：Observer Pseudoultrametric 定理

$$
d_{\mathrm{obs}}
$$

滿足：

$$
\boxed{
d_{\mathrm{obs}}(x,z)
\leq
\max
\{
d_{\mathrm{obs}}(x,y),
d_{\mathrm{obs}}(y,z)
\}.
}
$$

因此：

$$
d_{\mathrm{obs}}
$$

為 pseudoultrametric。

### 證明

設：

$$
m
=
\min
\{
r_{\mathrm{sep}}(x,y),
r_{\mathrm{sep}}(y,z)
\}.
$$

則 $x,y$ 與 $y,z$ 在所有：

$$
n<m
$$

的 $K_n$ 中仍等價。

由 $K_n$ 的傳遞性：

$$
xK_nz
$$

亦對所有：

$$
n<m
$$

成立。

所以：

$$
r_{\mathrm{sep}}(x,z)
\geq
m.
$$

因此：

$$
2^{-r_{\mathrm{sep}}(x,z)}
\leq
2^{-m},
$$

即：

$$
d_{\mathrm{obs}}(x,z)
\leq
\max\{
d_{\mathrm{obs}}(x,y),
d_{\mathrm{obs}}(y,z)
\}.
$$

證畢。

---

# 21. 在 Residual Quotient 上得到真正 Ultrametric

如果：

$$
xK_\infty y
$$

可能對不同 $x,y$ 成立，

則：

$$
d_{\mathrm{obs}}(x,y)=0
$$

不一定推出：

$$
x=y.
$$

因此是 pseudometric。

但在：

$$
D/K_\infty
$$

上，它下降為：

$$
\boxed{
\bar d_{\mathrm{obs}}.
}
$$

---

# 定理 7：Residual Observer Ultrametric

$$
\bar d_{\mathrm{obs}}
$$

為：

$$
D/K_\infty
$$

上的 ultrametric。

因此 nested observer kernels 自然產生 hierarchical geometry。

證畢。

---

# 22. Observer Tower 不只是一串 Quotients

此時：

$$
K_0
\supseteq
K_1
\supseteq
\cdots
$$

同時可以理解成：

1. partitions 的逐步精化；
2. quotient spaces 的 inverse system；
3. pairwise difference emergence ranks；
4. pseudoultrametric hierarchy。

所以：

$$
\boxed{
\text{Observer Tower}
}
$$

已經同時具有：

$$
\boxed{
\text{categorical}
+
\text{order-theoretic}
+
\text{metric}
}
$$

三種表述。

---

# 23. 但 Inverse Limit 會忘掉什麼？

現在進入本篇第二個核心問題。

設：

$$
\mathfrak T
=
(Q_n,\pi_{m,n}),
$$

$$
\mathfrak T'
=
(Q_n',\pi_{m,n}').
$$

假設：

$$
\boxed{
\varprojlim\mathfrak T
\cong
\varprojlim\mathfrak T'.
}
$$

可以推出：

$$
\mathfrak T
$$

與：

$$
\mathfrak T'
$$

具有相同 resolution history 嗎？

一般答案是：

$$
\boxed{
\text{不能。}
}
$$

---

# 24. Limit 只保留 Compatible Total States

Inverse limit 的元素是跨所有 stages 的 compatible families。

但單一：

$$
L=\varprojlim Q_n
$$

本身並不記錄：

- 有多少 stages；
- 哪一階第一次分離某對象；
- 每一階 quotient 大小；
- transition map 的具體形狀；
- 是否重複某些 stages；
- 哪些中間層曾經存在。

因此：

$$
\boxed{
\text{limit object}
}
$$

通常比：

$$
\boxed{
\text{inverse system}
}
$$

更粗。

---

# 25. Strict Tower Identity

第一種最強身份定義為：

$$
\boxed{
\mathfrak T
\equiv_{\mathrm{strict}}
\mathfrak T'
}
$$

若：

- index system 相同；
- 每一階 object 相同或指定方式同構；
- 所有 bonding maps 相容。

如果要求保留絕對 stage labels：

$$
0,1,2,\ldots,
$$

則它是一種非常強的 history identity。

---

# 26. Strict Identity 的問題

假設：

$$
\mathfrak T'
$$

只是在：

$$
\mathfrak T
$$

中每一個 level 重複兩次：

$$
Q_0
\leftarrow
Q_0
\leftarrow
Q_1
\leftarrow
Q_1
\leftarrow
\cdots.
$$

其數學近似內容可能沒有增加任何東西。

但 strict identity 仍會把它判成不同 tower。

所以：

$$
\boxed{
\text{strict tower identity}
}
$$

可能對純粹重編號過度敏感。

---

# 27. Pro-Object

這正是 pro-category 的用途之一。

對 category：

$$
\mathcal C,
$$

一個 pro-object 可由：

$$
\boxed{
\text{a small cofiltered diagram in }\mathcal C
}
$$

表示。

它不是把 diagram 立刻壓縮成 limit。

Stacks Project 明確定義：

$$
\operatorname{Pro}(\mathcal C)
$$

並給出：

$$
\boxed{
\operatorname{Hom}_{\operatorname{Pro}(\mathcal C)}(F,G)
=
\varprojlim_j
\varinjlim_i
\operatorname{Hom}_{\mathcal C}(F(i),G(j)).
}
$$



---

# 28. Pro-Observer

因此定義：

$$
\boxed{
\mathbf{ProObs}(D)
=
\left[
D/K_i
\right]_{i\in I}
}
$$

作為：

$$
\operatorname{Pro}(\mathcal C)
$$

中的 pro-object。

其中：

$$
\mathcal C
$$

依問題可以是：

- Sets；
- Top；
- Groups；
- Abelian groups；
- structured observer states；
- 其他適當 category。

---

# 29. 為什麼 Pro-Observer 比單一 Limit 更符合 NTLA？

因為：

$$
\mathbf{ProObs}(D)
$$

保留：

$$
\boxed{
\text{整個逐層近似系統}.
}
$$

而不是只留下：

$$
\boxed{
\text{所有近似完成後的 compatible states}.
}
$$

這與 NTLA 原始的：

$$
T_0
\leftarrow
T_1
\leftarrow
T_2
\leftarrow
\cdots
$$

比單一：

$$
T_\infty
$$

更加接近。

---

# 30. Pro-Identity

定義：

$$
\boxed{
\mathfrak T
\equiv_{\mathrm{pro}}
\mathfrak T'
}
$$

若兩者在：

$$
\operatorname{Pro}(\mathcal C)
$$

中同構。

Pro-category 的 morphism 定義允許從來源足夠後面的 stage 映射到目標任意固定 stage，因此它天然比「逐 level 同構」更不依賴具體 index 表示。

---

# 31. Cofinal Reindexing 的意義

例如：

$$
Q_0
\leftarrow
Q_1
\leftarrow
Q_2
\leftarrow
Q_3
\leftarrow
\cdots
$$

與取 cofinal subsequence：

$$
Q_0
\leftarrow
Q_2
\leftarrow
Q_4
\leftarrow
Q_6
\leftarrow
\cdots
$$

在 pro-level 上可以表示相同漸進對象。

直觀上：

> 如果第二個系統永遠能走到第一個系統任意指定的解析深度，那些被跳過的純中間 index 不必自動構成新的 pro-identity。

這正是 Pro-Observer 很適合「漸進解析」的原因。

---

# 32. 但 Pro-Identity 也會忘掉一些歷史

假設：

$$
x,y
$$

在原 tower 中首次於：

$$
n=7
$$

被分離。

如果重新索引成：

$$
n\mapsto2n,
$$

那麼其數字 stage label 會改變。

但 pro-object 本身可能不把這種 index 改寫視為新身份。

因此：

$$
\boxed{
r_{\mathrm{sep}}(x,y)
}
$$

一般不是純 pro-isomorphism invariant。

---

# 33. Stage Label 若有物理／語義意義就必須保留

如果：

$$
n
$$

只表示任意解析編號，

cofinal reindexing 合理。

但如果：

$$
n
$$

代表：

- 真實時間；
- 物理尺度；
- 精確成本；
- 學習輪次；
- 特定語義層；
- 實驗階段；

則：

$$
n\mapsto2n
$$

不能被無條件商掉。

因此可定義：

$$
\boxed{
\text{Scale-Labeled Observer Tower}
}
$$

為：

$$
\boxed{
(I,s,\{Q_i\},\{\pi_{ji}\}),
}
$$

其中：

$$
s:I\rightarrow\Lambda
$$

保留有意義的 scale labels。

---

# 34. Pro-Object 是身份選項，不是唯一答案

因此 NTLA-O 不宣稱：

$$
\boxed{
\text{Tower Identity}
=
\text{Pro-Isomorphism}
}
$$

永遠成立。

而是提供：

$$
\boxed{
\text{Strict Identity}
}
$$

與：

$$
\boxed{
\text{Pro-Identity}
}
$$

兩種不同 history resolutions。

若 index 本身有身份意義，採 strict／labeled identity。

若只在意 cofinal approximation behavior，採 pro-identity。

---

# 35. Limit Identity

定義：

$$
\boxed{
\mathfrak T
\equiv_{\mathrm{lim}}
\mathfrak T'
}
$$

若：

$$
\boxed{
\varprojlim\mathfrak T
\cong
\varprojlim\mathfrak T'.
}
$$

這是三者中最粗的一種。

---

# 36. Identity Hierarchy

在 Sets、Ab 等所需 inverse limits 存在的情況下，可以得到概念上：

$$
\boxed{
\equiv_{\mathrm{strict}}
\Longrightarrow
\equiv_{\mathrm{pro}}
\Longrightarrow
\equiv_{\mathrm{lim}}.
}
$$

第一個箭頭把具體 stage representation 放寬成 pro-object。

第二個箭頭則只保留 limit object。

反方向一般不成立。

---

# 37. Strict 反方向失敗

兩個 cofinally reindexed towers 可以在 Pro-category 中同構，但不具有逐 index 相同的 strict diagram。

因此：

$$
\boxed{
\equiv_{\mathrm{pro}}
\not\Rightarrow
\equiv_{\mathrm{strict}}.
}
$$

這是 pro-object formalism 故意容許的表示彈性。Pro-category 本身就是將 cofiltered systems 組織成獨立 category，而非把具體 index presentation 當唯一身份。

---

# 38. Limit 反方向甚至對 Pro-Identity 也失敗

現在需要一個更強反例。

考慮 category：

$$
\mathbf{Ab}.
$$

固定 prime：

$$
p.
$$

定義 inverse system：

$$
\boxed{
A_n
=
\mathbb Z/p^n\mathbb Z
}
$$

以及自然 quotient maps：

$$
A_{n+1}\twoheadrightarrow A_n.
$$

定義：

$$
\boxed{
\mathbb Z_p
=
\varprojlim_n
\mathbb Z/p^n\mathbb Z.
}
$$

再考慮常值 inverse system：

$$
\boxed{
B_n=\mathbb Z_p
}
$$

所有 transition maps 為 identity。

則：

$$
\boxed{
\varprojlim A_n
\cong
\mathbb Z_p
\cong
\varprojlim B_n.
}
$$

所以：

$$
A
\equiv_{\mathrm{lim}}
B.
$$

---

# 39. 但兩者不是同一 Pro-Object

對 constant target：

$$
\mathbb Z_p,
$$

pro-category morphism formula 化為：

$$
\operatorname{Hom}_{\operatorname{Pro}(\mathbf{Ab})}
(A,\mathbb Z_p)
=
\varinjlim_n
\operatorname{Hom}_{\mathbf{Ab}}
(
\mathbb Z/p^n\mathbb Z,
\mathbb Z_p
).
$$

標準 pro-category morphism formula 見 Stacks Project。

而：

$$
\mathbb Z_p
$$

作為 additive group 沒有非零的有限 $p$-torsion 元素。

所以每個：

$$
\operatorname{Hom}
(
\mathbb Z/p^n\mathbb Z,
\mathbb Z_p
)
$$

都只有零映射。

因此：

$$
\boxed{
\operatorname{Hom}_{\operatorname{Pro}(\mathbf{Ab})}
(A,\mathbb Z_p)
=
0.
}
$$

故不可能存在：

$$
A\rightarrow B
$$

的 pro-isomorphism。

因此：

---

# 定理 8：Same Limit Does Not Imply Pro-Isomorphism

存在 inverse systems：

$$
A,B
$$

使：

$$
\boxed{
\varprojlim A
\cong
\varprojlim B
}
$$

但：

$$
\boxed{
A
\not\cong
B
\quad
\text{in }
\operatorname{Pro}(\mathbf{Ab}).
}
$$

證畢。

---

# 40. 這是本篇最重要的身份結果

因此：

$$
\boxed{
\text{same completed outcome}
\not\Rightarrow
\text{same approximation structure}.
}
$$

甚至在把純 index representation 差異商掉之後仍然成立。

所以：

$$
\boxed{
\text{Limit Identity}
}
$$

比：

$$
\boxed{
\text{Pro-Observer Identity}
}
$$

嚴格更粗。

---

# 41. NTLA 原始直覺因此得到第二種 History

Paper 6 的 history 是：

$$
\boxed{
\text{Path History}.
}
$$

本篇新增：

$$
\boxed{
\text{Resolution History}.
}
$$

兩者完全不同。

### Path History

回答：

> 同一 state 是沿哪條 path 到達？

### Resolution History

回答：

> 同一 object 是在哪些 observation stages 被逐步分離、投影與商化？

因此：

$$
\boxed{
\text{history}
}
$$

在 NTLA-O 中至少有兩個獨立維度。

---

# 42. Tower Signature

可以定義：

$$
\boxed{
\operatorname{TSig}(\mathfrak T)
=
\left(
I,
\{Q_i\},
\{\pi_{ji}\}
\right).
}
$$

若再保留 scale：

$$
\boxed{
\operatorname{TSig}^{\Lambda}(\mathfrak T)
=
\left(
I,
s,
\{Q_i\},
\{\pi_{ji}\}
\right).
}
$$

此資料比：

$$
\varprojlim Q_i
$$

完整。

---

# 43. Pairwise Separation Signature

對 fixed-domain tower，可進一步記錄：

$$
\boxed{
R_{\mathfrak T}(x,y)
=
r_{\mathrm{sep}}(x,y).
}
$$

整體：

$$
\boxed{
\mathbf R_{\mathfrak T}
=
\{
r_{\mathrm{sep}}(x,y)
\}_{x,y\in D}
}
$$

記錄每對 objects 的首次分離階。

若 exact scale labels 有意義，這本身就是 resolution-history invariant。

---

# 44. Kernel Tower 可由 Separation Signature 恢復

在自然數索引 decreasing tower 中：

$$
(x,y)\in K_n
$$

當且僅當：

$$
\boxed{
r_{\mathrm{sep}}(x,y)>n
}
$$

或：

$$
r_{\mathrm{sep}}(x,y)=\infty.
$$

所以 pairwise separation-rank matrix 在此條件下可以恢復整個：

$$
\{K_n\}.
$$

因此：

$$
\boxed{
\text{kernel tower}
}
$$

與：

$$
\boxed{
\text{pairwise separation hierarchy}
}
$$

攜帶等價資訊。

---

# 45. 但它仍不能恢復所有額外結構

若：

$$
Q_n
$$

不只是集合，而還帶：

- topology；
- group structure；
- sheaf data；
- transport；
- labels；

則單靠：

$$
K_n
$$

不能恢復所有這些額外結構。

所以：

$$
\boxed{
\text{Kernel Tower}
}
$$

仍然只是：

$$
\boxed{
\text{Observer Tower 的 point-identity skeleton}.
}
$$

完整 Pro-Observer 必須保留所選 category 中的 objects 與 morphisms。

---

# 46. Observer Tower 的類別必須指定

因此不能只寫：

$$
\mathbf{ProObs}.
$$

更完整應寫：

$$
\boxed{
\mathbf{ProObs}_{\mathcal C}.
}
$$

例如：

$$
\mathbf{ProObs}_{\mathbf{Set}},
$$

$$
\mathbf{ProObs}_{\mathbf{Top}},
$$

$$
\mathbf{ProObs}_{\mathbf{Grp}}.
$$

因不同 category 保留不同 morphism 與 identity notion。

---

# 47. Set-Theoretic Size Boundary 再次出現

標準 pro-object 使用 small cofiltered diagram。Stacks Project 亦把 pro-objects描述成 cofiltered diagrams，並將它們組成 $\operatorname{Pro}(\mathcal C)$。

所以如果 NTLA-O 要使用：

$$
\operatorname{Ord}
$$

整個 proper class 作 index，

就不能在普通 small-pro-object 設定中不加說明地直接操作。

必須回到 Paper 3 的 size profiles：

$$
\mathrm{NTLA\!-\!O}_{\mathrm{set}},
$$

$$
\mathrm{NTLA\!-\!O}_{U},
$$

或：

$$
\mathrm{NTLA\!-\!O}_{\mathrm{class}}.
$$

---

# 48. 無界不代表一定要 Class-Level

一個：

$$
\omega
$$

索引 tower：

$$
Q_0
\leftarrow
Q_1
\leftarrow
\cdots
$$

已經可以具有無限 observation depth，

但整個 index：

$$
\mathbb N
$$

仍然是一個集合。

因此普通 pro-object 完全足以處理大量 NTLA 無界解析問題。

只有真正對所有序數無界的 tower 才需要 class-level size treatment。

---

# 49. Limit Functor 本身也可能失去代數資訊

在 Abelian groups 等情況，inverse limit 並不對所有 short exact sequences 都保持右端 exactness；Mittag-Leffler 等條件正是經典 inverse-system 理論中控制此類問題的工具。

NTLA-O 不在本文展開 derived limits。

但這提供另一個重要警告：

$$
\boxed{
\text{taking inverse limit is not a universally information-neutral operation}.
}
$$

因此若未來把 observer towers 放進：

- modules；
- chain complexes；
- cohomology；
- derived categories；

不能把：

$$
\varprojlim
$$

當成無條件保持所有結構的操作。

---

# 50. Stabilization

若存在：

$$
N
$$

使對所有：

$$
n\geq N
$$

都有：

$$
K_n=K_N,
$$

則稱 kernel tower 在 $N$ 後 stabilization。

此時 point-distinction 層已不再增加。

---

# 51. 但 Kernel Stabilization 不等於 Full Tower Stabilization

即使：

$$
K_n=K_N
$$

對全部高階成立，

仍可能：

$$
\tau_n,
\mathscr F_n,
T_n
$$

繼續改變。

Paper 4 已證明相同 kernel 不決定相同 topology。

因此：

$$
\boxed{
\text{kernel stabilization}
\not\Rightarrow
\text{observer-structure stabilization}.
}
$$

---

# 52. Pro-Constant

在 pro-category 中，如果一個 inverse system 與某個 constant system 同構，就稱其在 pro-object 意義下 essentially constant。Stacks Project 明確指出，pro-system essentially constant 等價於它在 $\operatorname{Pro}(\mathcal C)$ 中與 constant system 同構。

因此 NTLA-O 可以區分：

$$
\boxed{
\text{levelwise eventual constancy}
}
$$

與：

$$
\boxed{
\text{pro-constancy}.
}
$$

後者更弱、更不依賴具體 presentation。

---

# 53. Observer Learning 的 Pro-Stabilization 候選

如果一個 learning system 的 observer tower：

$$
\mathfrak T_t
$$

隨訓練演化，

可以研究：

$$
\boxed{
\mathfrak T_t
\rightarrow
\mathfrak T_\infty
}
$$

是否在某種：

- strict；
- pro；
- limit；

意義下 stabilization。

三種「收斂」不是同一命題。

---

# 54. 三種收斂強度

可以暫時區分：

### Stage Stabilization

高階後所有：

$$
Q_n,\pi_n
$$

逐 level 固定。

### Pro-Stabilization

整體 approximation system 在 pro-category 中進入同一 isomorphism class。

### Limit Stabilization

只有：

$$
\varprojlim Q_n
$$

保持同構。

因此：

$$
\boxed{
\text{Limit Stabilization}
}
$$

是三者最弱的一種。

---

# 55. Resolution History 與 Path History 的交叉

現在 observer 不只可以沿 path：

$$
\gamma
$$

移動，

還可以在 resolution：

$$
n
$$

上變化。

所以更完整 state 應寫成：

$$
\boxed{
s_{n,x}.
}
$$

其中：

$$
x
$$

代表位置，

$$
n
$$

代表解析層。

存在兩種 maps：

### Spatial transport

$$
T_\gamma:
s_{n,x}
\rightarrow
s_{n,y}.
$$

### Resolution projection

$$
\pi_{m,n}:
s_{m,x}
\rightarrow
s_{n,x}.
$$

---

# 56. Transport–Resolution Commutation 問題

現在出現一個新問題：

先提升解析度再沿路徑 transport：

$$
s_{m,x}
\xrightarrow{T_\gamma^{(m)}}
s_{m,y}
\xrightarrow{\pi_{m,n}}
s_{n,y}
$$

是否等於：

先投影到粗 resolution：

$$
s_{m,x}
\xrightarrow{\pi_{m,n}}
s_{n,x}
\xrightarrow{T_\gamma^{(n)}}
s_{n,y}?
$$

也就是：

$$
\boxed{
\pi_{m,n}
\circ
T_\gamma^{(m)}
\stackrel{?}{=}
T_\gamma^{(n)}
\circ
\pi_{m,n}.
}
$$

---

# 57. Observer Transport–Resolution Coherence

若上式對所有：

$$
m\geq n
$$

與合法 paths $\gamma$ 成立，稱 transport 與 resolution projection coherent。

即：

$$
\boxed{
\pi
\circ
T
=
T
\circ
\pi.
}
$$

這是下一階統合理論的重要接口。

---

# 58. 如果不交換會發生什麼？

若：

$$
\pi_{m,n}
\circ
T_\gamma^{(m)}
\neq
T_\gamma^{(n)}
\circ
\pi_{m,n},
$$

則：

> 在高解析度下先經歷歷史再壓縮，與先壓縮再經歷歷史，會得到不同結果。

這正是一種：

$$
\boxed{
\text{resolution–history noncommutativity}.
}
$$

它與 NTLA 原始的 connection-order sensitivity 極為一致。

但本文只建立問題，不宣稱一般系統必然非交換。

---

# 59. Locality 軸也可以加入

Paper 5 有：

$$
V\subseteq U
$$

的 restriction：

$$
\rho^U_V.
$$

現在完整 state 可以寫：

$$
\boxed{
\mathscr F_n(U).
}
$$

因此至少具有三種 morphisms：

### Local restriction

$$
\rho^U_V:
\mathscr F_n(U)
\rightarrow
\mathscr F_n(V).
$$

### Resolution projection

$$
\pi_{m,n}:
\mathscr F_m(U)
\rightarrow
\mathscr F_n(U).
$$

### Path transport

$$
T_\gamma^{(n)}.
$$

NTLA-O 因而開始形成真正的多方向交換圖問題。

---

# 60. NTLA-O 三軸交換結構

可以暫時表示為：

$$
\boxed{
\text{Locality}
\times
\text{Resolution}
\times
\text{Transport}.
}
$$

而：

$$
\rho_X(\mathcal O)
$$

作為第四個 role index。

因此：

$$
\boxed{
\text{NTLA-O}
=
\text{Role-indexed multiaxial observer system}.
}
$$

這仍是研究綱領，不是既有單一標準數學對象的名稱。

---

# 61. 本篇核心身份層級

現在正式定義三種：

## 61.1 Strict Tower Identity

保存：

- stages；
- indices；
- bonding maps；
- chosen labels。

## 61.2 Pro-Observer Identity

保存：

- cofinal approximation behavior；
- pro-object isomorphism class。

但允許忽略純表示性的 cofinal reindexing。

## 61.3 Limit Identity

只保存：

$$
\boxed{
\varprojlim Q_i.
}
$$

因此：

$$
\boxed{
\text{Strict}
\succ
\text{Pro}
\succ
\text{Limit}
}
$$

代表逐步更粗的 history resolution。

---

# 62. NTLA 身份規格再擴充

現在 NTLA 2.0 的身份規格可更新為：

$$
\boxed{
\mathfrak I
=
\left(
\mathfrak I_{\mathrm{state}},
\mathfrak I_{\mathrm{top}},
\mathfrak I_{\mathrm{path}},
\mathfrak I_{\mathrm{transport}},
\mathfrak I_{\mathrm{tower}}
\right).
}
$$

其中：

$$
\mathfrak I_{\mathrm{tower}}
$$

決定：

> 解析歷史需要保存到 strict、pro，還是只保存 limit？

---

# 63. 「結果同一」現在至少有三層

假設：

$$
L_A
\cong
L_B.
$$

可能：

$$
\mathfrak T_A
\not\cong_{\mathrm{Pro}}
\mathfrak T_B.
$$

即：

$$
\boxed{
\text{same limit}
\not\Rightarrow
\text{same approximation history}.
}
$$

即使：

$$
\mathfrak T_A
\cong_{\mathrm{Pro}}
\mathfrak T_B,
$$

仍可能：

$$
\mathfrak T_A
\not\equiv_{\mathrm{strict}}
\mathfrak T_B.
$$

即：

$$
\boxed{
\text{same asymptotic approximation structure}
\not\Rightarrow
\text{same exact stage history}.
}
$$

---

# 64. 這就是 NTLA-O 的 Resolution-History Principle

本文提出：

$$
\boxed{
\textbf{Resolution-History Principle}
}
$$

其內容不是一條宇宙公理，而是一條身份設計原則：

> 若一個應用的身份依賴「差異在哪一階首次出現、哪些 intermediate quotients 曾存在、resolution maps 如何組成」，則不能只保存 inverse limit。

應至少保存：

$$
\boxed{
\text{inverse system}
}
$$

或其適當：

$$
\boxed{
\text{pro-object}.
}
$$

---

# 65. 與原始 NTLA 的重新連接

原始 NTLA：

$$
T^\infty
=
T_0
\leftarrow
T_1
\leftarrow
T_2
\leftarrow
\cdots
$$

早期主要被理解成：

> 不同理論解析層逐步逼近完整形狀。

現在 NTLA-O VI 給出更精確的版本：

$$
\boxed{
T^\infty
}
$$

不應自動只被理解為：

$$
\boxed{
\varprojlim T_n.
}
$$

還應考慮：

$$
\boxed{
\{T_n,p_{m,n}\}
}
$$

本身。

因此符號：

$$
T^\infty
$$

在新版正式文件中應避免未定義地同時指：

1. 整個 inverse system；
2. inverse limit；
3. pro-object。

三者應分別記號化。

---

# 66. 建議新記號

本文建議：

### Tower

$$
\boxed{
\mathbf T
=
\{T_i,p_{ji}\}.
}
$$

### Pro-object

$$
\boxed{
[\mathbf T]_{\mathrm{Pro}}.
}
$$

### Inverse limit

$$
\boxed{
T_\infty
=
\varprojlim_iT_i.
}
$$

如此避免舊式：

$$
T^\infty
$$

語意混亂。

---

# 67. 這也是對 NTLA 2.0 的第二次精修

因此第一篇中：

$$
T^\infty
=
T_0\leftarrow T_1\leftarrow\cdots
$$

後續正式版本應修正成：

$$
\boxed{
\mathbf T
:
T_0
\leftarrow
T_1
\leftarrow
T_2
\leftarrow
\cdots,
}
$$

而：

$$
\boxed{
T_\infty
=
\varprojlim\mathbf T
}
$$

僅在 limit 存在並需要時使用。

如果研究的是 approximation identity，則使用：

$$
\boxed{
[\mathbf T]_{\mathrm{Pro}}.
}
$$

這會比原記號乾淨很多。

---

# 68. 本篇核心定理群

本文建立：

### 定理 A：Observer Quotient Bonding

$$
K_j\subseteq K_i
$$

自然產生：

$$
D/K_j\rightarrow D/K_i.
$$

### 定理 B：Natural Limit Map Kernel

$$
\ker\eta=K_\infty.
$$

### 定理 C：Residual Quotient Injection

$$
\boxed{
D/K_\infty
\hookrightarrow
\varprojlim D/K_n.
}
$$

### 定理 D：Ideal Limit States Exist

上述單射一般不必滿射。

### 定理 E：Nested-Class Intersection Criterion

limit state 被原域實現，當且僅當其 nested equivalence classes 有非空交。

### 定理 F：Observer Pseudoultrametric

nested kernels 自然產生 pseudoultrametric。

### 定理 G：Residual Observer Ultrametric

在：

$$
D/K_\infty
$$

上得到真正 ultrametric。

### 定理 H：Same Limit Does Not Imply Pro-Isomorphism

$$
\{\mathbb Z/p^n\mathbb Z\}
$$

與 constant $\mathbb Z_p$ system 提供反例。

---

# 69. 傳統數學接口與新意邊界

本文使用的：

- inverse system；
- inverse limit；
- cofiltered diagram；
- pro-object；
- pro-category；
- essentially constant system；
- Mittag-Leffler condition；

均為既有標準範疇論／同調代數結構。Stacks Project 對 inverse systems 與 pro-objects 有直接正式定義。

本文不宣稱發明：

$$
\varprojlim,
\quad
\operatorname{Pro}(\mathcal C),
\quad
\text{ultrametric hierarchy}.
$$

NTLA-O 的 candidate contribution 仍然是耦合：

$$
\boxed{
\text{Observer Kernel Refinement}
}
$$

$$
+
$$

$$
\boxed{
\text{Resolution History}
}
$$

$$
+
$$

$$
\boxed{
\text{Role / Locality / Path Transport}
}
$$

$$
+
$$

$$
\boxed{
\text{Explicit Identity Resolution}.
}
$$

---

# 70. 理論強度聲明

本文不宣稱：

- 任意 observer tower 的 inverse limit 都存在於任意 category；
- inverse limit 必等於原始 domain；
- 所有 ideal limit states 都具有物理意義；
- pro-object 是所有歷史身份的唯一正確定義；
- cofinal reindexing 在所有應用中都應視為同一；
- ultrametric 距離等於真實心理距離；
- inverse limit 保持所有代數或幾何資訊；
- NTLA-O 已解決一般 inverse-limit completion 問題。

本文證明的是：

> 在 decreasing observer-kernel 系統中，可以自然形成 inverse quotient tower；此 tower 的 residual quotient、inverse limit 與 pro-object 是三種不同強度的數學對象，不能互相偷換。

---

# 71. NTLA-O 到目前的四軸結構

現在完整主線為：

## Role

$$
\boxed{
\rho_X(\mathcal O)
}
$$

回答：

> observer 相對 reference domain 在哪裡？

## Locality

$$
\boxed{
U,\mathscr F(U),\mathscr F_x
}
$$

回答：

> observation 在哪個局部域成立？

## Resolution

$$
\boxed{
K_0\supseteq K_1\supseteq\cdots
}
$$

回答：

> observation 可以分到多細？

## Transport

$$
\boxed{
T_\gamma
}
$$

回答：

> observation state 沿路徑如何改變？

因此：

$$
\boxed{
\mathrm{NTLA\!-\!O}
=
\text{Role}
\times
\text{Locality}
\times
\text{Resolution}
\times
\text{Transport}.
}
$$

而本篇額外指出：

$$
\boxed{
\text{Resolution}
}
$$

本身還存在：

$$
\boxed{
\text{stage history}
\rightarrow
\text{pro-history}
\rightarrow
\text{limit}.
}
$$

---

# 72. 下一篇

到這裡我們已經知道：

1. 如何建立 observer differences；
2. 如何把 differences 組織成 topology；
3. 如何從 local observers 黏合 global states；
4. 如何保存 path/transport history；
5. 如何保存 resolution history。

現在剩下一個最直接的數學問題：

> **這些觀察結構何時真的足以完整分離 NTLA 所宣稱不同的結構？**

也就是：

$$
\boxed{
\text{Observation}
\stackrel{?}{=}
\text{Complete Structural Classification}.
}
$$

下一篇因此進入：

# **NTLA-O VII：完備分離、Canonical Invariants、局部有限重建與 Continuous Separation Problem**

其核心將依次處理：

$$
\boxed{
\text{有限 NTLA 結構}
}
$$

$$
\rightarrow
$$

$$
\boxed{
\text{canonical complete separator}
}
$$

$$
\rightarrow
$$

$$
\boxed{
\text{局部有限可數結構}
}
$$

$$
\rightarrow
$$

$$
\boxed{
\text{all finite-radius observations}
}
$$

$$
\rightarrow
$$

$$
\boxed{
\text{global reconstruction}.
}
$$

最後再明確劃出目前真正沒有被解決的：

$$
\boxed{
\text{General Continuous Separation Problem}.
}
$$

那一篇完成後，八篇數學主體就會全部閉合；第九篇只需要做公理、定理依賴、傳統數學接口與整個 NTLA-O 的統一總篇。