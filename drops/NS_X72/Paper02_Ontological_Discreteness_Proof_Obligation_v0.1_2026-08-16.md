# 離散本體證明責任原則
## 「宇宙是一台數位計算機」命題的形式化證明義務

- 英文題名：**The Proof-Obligation Principle for Ontological Discreteness: Formal Requirements for the Claim that the Universe Is a Digital Computer**
- 版本：v0.1
- 日期：2026-08-16
- 類型：計算本體論／科學哲學／數學邏輯方法論
- 核心立場：本文不主張世界必然連續，也不主張世界必然離散；本文只規定強離散本體論的證明責任。

---

## 摘要

「宇宙是一台計算機」、「萬物皆 bit」、「世界底層是離散資訊」等命題常在數位物理、計算宇宙論與資訊本體論中出現。然而，能被數位電腦模擬、能被離散化描述、能以 bit 編碼，均不足以推出世界的底層構成本身是離散的。

本文提出**離散本體證明責任原則**：若主張世界在本體上等價於一個離散計算系統，則必須證明其離散性不是測量、表示、近似、座標、量子化譜、計算介面或觀察限制所產生，而是在所有無損等價表示中都無法消除的結構不變量。世界若可能具有連續底層、前時空結構、混合結構或未知結構，均不能被未證明地排除。

---

# 1. 四個不能混同的命題

首先區分：

$$
\boxed{
\text{Computationally describable}
}
$$

$$
\boxed{
\text{Digitally representable}
}
$$

$$
\boxed{
\text{Exactly digitally simulable}
}
$$

$$
\boxed{
\text{Digitally constituted}
}
$$

它們並不等價。

特別是：

$$
\boxed{
\text{可被離散計算}
\neq
\text{世界本體離散}.
}
\tag{1.1}
$$

---

# 2. 數值近似不推出本體離散

考慮 continuous system：

$$
\frac{dx}{dt}
=
f(x).
$$

它可由數位計算機使用：

- finite differences；
- Runge–Kutta；
- spectral methods；
- finite elements；

任意精細近似。

但：

$$
\boxed{
\text{arbitrarily accurate discrete approximation}
\not\Rightarrow
\text{exact discrete ontology}.
}
\tag{2.1}
$$

數值方法證明的是：

$$
\boxed{
\text{digital computability / approximability},
}
$$

而不是：

$$
\boxed{
\text{digital constitution}.
}
$$

---

# 3. 世界狀態與離散模型

令世界完整狀態空間為：

$$
\mathcal W.
$$

某強離散本體論主張存在離散狀態空間：

$$
\mathcal D
$$

以及離散計算演化：

$$
F_t:
\mathcal D
\to
\mathcal D
$$

使：

$$
\boxed{
\mathcal W
\simeq
\mathcal D.
}
$$

這個主張至少需要下列證明。

---

# 4. Exact Encoding Obligation

必須存在 encoding：

$$
E:
\mathcal W
\to
\mathcal D
$$

以及 reconstruction：

$$
R:
\mathcal D
\to
\mathcal W
$$

使：

$$
\boxed{
R\circ E
=
\operatorname{id}_{\mathcal W}.
}
\tag{4.1}
$$

也就是：

$$
\boxed{
\text{lossless exact reconstruction}.
}
$$

若只能：

$$
R(E(w))
\approx
w,
$$

則只證明近似模型。

---

# 5. Dynamical Conjugacy Obligation

令世界真正演化為：

$$
\Phi_t:
\mathcal W
\to
\mathcal W.
$$

強 digital ontology 至少需：

$$
\boxed{
E\circ\Phi_t
=
F_t\circ E.
}
\tag{5.1}
$$

也就是：

$$
\boxed{
\text{world dynamics}
\cong
\text{discrete computational dynamics}.
}
$$

單純能模擬 observational outputs 不足以建立這個 conjugacy。

---

# 6. Invariant Preservation Obligation

所有 relevant physical / logical / mathematical invariants：

$$
I_\alpha
$$

都必須滿足：

$$
\boxed{
I_\alpha(w)
=
\widetilde I_\alpha(E(w)).
}
\tag{6.1}
$$

若離散 representation 丟失任何本體必要 invariant，

則：

$$
\boxed{
\mathcal W\not\simeq\mathcal D
}
$$

至少對該候選模型成立。

---

# 7. Essential Discreteness Obligation

最關鍵的要求不是：

> 找到一個離散模型。

而是證明：

$$
\boxed{
\textbf{
discreteness itself is representation-independent.
}
}
$$

即不存在另一個 lossless equivalent carrier：

$$
\mathcal C
$$

為 continuous、hybrid 或其他非離散形式，而同樣保留：

$$
\text{state}
+
\text{dynamics}
+
\text{invariants}.
$$

否則：

$$
\boxed{
\text{離散性可能只是表示選擇}.
}
$$

---

# 8. 離散本體證明責任原則

正式提出：

$$
\boxed{
\textbf{
Claiming ontological discreteness requires proving
that discreteness is invariant under lossless equivalent representations.
}
}
\tag{8.1}
$$

中文：

> 若主張世界在本體上是離散的，必須證明離散性不是座標、觀察、測量、近似、分割、計算介面或表示方法所產生，而是在所有無損等價表示中都不可消除的結構不變量。

---

# 9. 最小長度不等於離散世界

即使未來某理論證明存在：

$$
\ell_{\min}>0,
$$

仍不能直接推出：

$$
\boxed{
\text{world is discrete}.
}
$$

因為：

$$
\ell_{\min}
$$

可能代表：

- operational measurement cutoff；
- spectral gap；
- effective theory boundary；
- continuous substrate上的 quantized excitation；
- noncommutative geometry；
- pre-spacetime constraint；
- mixed continuous/discrete structure；
- 尚未知的底層形式。

所以：

$$
\boxed{
\text{minimum observable scale}
\neq
\text{discrete ontology}.
}
\tag{9.1}
$$

---

# 10. Quantization 不等於離散本體

觀察到 discrete spectrum：

$$
E_n
$$

也不能推出：

$$
\boxed{
\text{entire substrate is discrete}.
}
$$

一個 continuous operator：

$$
H
$$

完全可以具有 discrete spectrum。

所以：

$$
\boxed{
\text{discrete eigenvalues}
\neq
\text{discrete state-space ontology}.
}
\tag{10.1}
$$

---

# 11. Bit 不等於 ontological atom

一個 physical system能被映射成：

$$
0/1
$$

符號，不代表：

$$
0,1
$$

就是世界的 ontological atom。

bit 可能只是：

$$
\boxed{
\text{observation alphabet}
}
$$

或：

$$
\boxed{
\text{encoding alphabet}.
}
$$

因此：

$$
\boxed{
\text{information encoded in bits}
\not\Rightarrow
\text{reality made of bits}.
}
\tag{11.1}
$$

---

# 12. Computable 不等於 computer

令某現象：

$$
x(t)
$$

可由 algorithm：

$$
A
$$

計算。

這只支持：

$$
\boxed{
x(t)
\text{ is computationally representable}.
}
$$

不能推出：

$$
\boxed{
x(t)
\text{ is literally an algorithm}.
}
$$

同樣：

$$
\boxed{
\text{Universe is computable}
\not\Rightarrow
\text{Universe is a computer}.
}
\tag{12.1}
$$

---

# 13. 弱計算宇宙論與強計算宇宙論

## 13.1 Weak computational thesis

$$
\boxed{
\text{The universe admits computational descriptions.}
}
$$

這與科學建模相容，證明負擔相對低。

## 13.2 Strong digital ontology

$$
\boxed{
\text{The universe is literally a discrete computational system.}
}
$$

這需要 Sections 4–8 的完整證明義務。

兩者不可混同。

---

# 14. 不能反向偷渡連續世界

本文同樣拒絕：

$$
\boxed{
\text{找不到 essential discreteness}
\Longrightarrow
\text{世界必然連續}.
}
$$

合法 epistemic states 至少應包括：

$$
\boxed{
\mathsf C,
\quad
\mathsf D,
\quad
\mathsf H,
\quad
\mathsf U,
}
$$

其中：

- $\mathsf C$：essential continuous；
- $\mathsf D$：essential discrete；
- $\mathsf H$：hybrid / mixed；
- $\mathsf U$：unknown，包括前時空、尚無分類或無法由現有概念判定。

在證據不足時：

$$
\boxed{
\mathsf U
\not\Rightarrow
\mathsf D.
}
$$

同樣：

$$
\boxed{
\mathsf U
\not\Rightarrow
\mathsf C.
}
$$

---

# 15. 前時空與未知形式

若底層不是：

$$
\text{space}
+
\text{time}
$$

的普通結構，

而是：

- pre-spacetime；
- relational substrate；
- categorical structure；
- algebraic constraint network；
- continuous/discrete mixed object；
- unknown mathematical ontology；

則不能未經證明地把它重新命名為：

$$
\boxed{
\text{digital computer}.
}
$$

「可被電腦描述」與「它就是電腦」仍是不同命題。

---

# 16. 與廣義結構連續統假設的關係

若某離散模型：

$$
\mathcal D
$$

可以被 losslessly continuumized：

$$
\mathcal D
\rightsquigarrow
\mathcal C,
$$

且：

$$
\mathcal C
$$

完整保留：

$$
\text{state}
+
\text{dynamics}
+
\text{invariants},
$$

則：

$$
\boxed{
\mathcal D
}
$$

的離散性至少不能單獨作為 world ontology 的證據。

因此：

$$
\boxed{
\text{digital ontology}
}
$$

需要找到：

$$
\boxed{
\text{essential discreteness witness}.
}
$$

---

# 17. 一個正式反駁模板

對任何命題：

> 世界底層是一個離散計算機。

可以要求證明以下五步：

$$
\boxed{
\begin{aligned}
\mathrm{P1}:&
\quad
\text{Exact encoding};
\\
\mathrm{P2}:&
\quad
\text{Exact reconstruction};
\\
\mathrm{P3}:&
\quad
\text{Dynamical conjugacy};
\\
\mathrm{P4}:&
\quad
\text{Invariant preservation};
\\
\mathrm{P5}:&
\quad
\text{Essential discreteness}.
\end{aligned}
}
\tag{17.1}
$$

任何一步缺失：

$$
\boxed{
\text{digital model}
\neq
\text{proven digital ontology}.
}
$$

---

# 18. 最小論證標準

因此至少應區分：

$$
\boxed{
\text{Simulation}
}
$$

$$
\boxed{
\text{Representation}
}
$$

$$
\boxed{
\text{Equivalence}
}
$$

$$
\boxed{
\text{Ontology}.
}
$$

推理鏈：

$$
\text{Simulation}
\to
\text{Representation}
\to
\text{Equivalence}
\to
\text{Ontology}
$$

中的每一條箭頭都必須獨立證明。

不能把第一步直接跳成最後一步。

---

# 19. 核心定理式命題

本文核心可壓成：

$$
\boxed{
\textbf{
A discrete computational representation of reality
is not evidence of discrete computational constitution
unless discreteness itself is shown to be invariant under
all relevant lossless equivalent representations.
}
}
\tag{19.1}
$$

---

# 20. 結論

「宇宙是一台數位計算機」如果只是比喻，可以作為研究直覺。

如果要升格為本體論命題，就必須接受完整證明責任：

$$
\boxed{
R\circ E
=
\operatorname{id}_{\mathcal W},
}
$$

$$
\boxed{
E\circ\Phi_t
=
F_t\circ E,
}
$$

以及：

$$
\boxed{
\text{discreteness is an invariant,
not a representation artifact}.
}
$$

因此本文的最低結論不是：

$$
\boxed{
\text{世界是連續的}.
}
$$

而是：

$$
\boxed{
\textbf{
在 essential discreteness 被證明以前，
不得從離散描述、bit 編碼、量子化譜或數位模擬
偷渡出「世界底層就是離散計算機」。
}
}
$$

最短版本：

> **The universe may compute. That does not prove that the universe is a digital computer.**

以及：

$$
\boxed{
\textbf{請先證明。}
}
$$
