---
title: "Navier–Stokes C3-B：雙手性臨界能量等化、異手性三元組分解與 Unique-Sign UV Escape"
subtitle: "Bi-Helical Critical-Energy Equalization, Exact Heterochiral Triad Algebra, and High-Frequency Escape of the Unique-Helicity Source"
version: "v0.1"
date: "2026-08-14"
author: "Neo.K / EveMissLab"
language: "zh-TW"
status: "Theorem-style structural reduction note"
epistemic_status: "Uses established critical-helicity identity and triadwise energy/helicity conservation; derives new-to-this-project corollaries and reductions. Does NOT prove Navier–Stokes global regularity."
---

# Navier–Stokes C3-B：
# 雙手性臨界能量等化、異手性三元組分解與 Unique-Sign UV Escape

## 0. 認識論修正

上一輪 C3-A 由 helical decomposition 得到：

$$
u=u^++u^-,
$$

並定義：

$$
H_\pm(t)
=
\|D^{1/2}u^\pm(t)\|_2^2,
$$

$$
D_\pm(t)
=
\|D^{3/2}u^\pm(t)\|_2^2.
$$

其中：

$$
D=\sqrt{-\Delta}.
$$

我們寫出 sector balance：

$$
\frac12H_\pm'(t)
+
\nu D_\pm(t)
=
\mathcal R_\pm(t),
$$

並由 nonlinear helicity cancellation得到：

$$
\mathcal R_+(t)
=
\mathcal R_-(t).
$$

本輪 literature audit 發現：

> Lei–Lin–Zhou 已建立與此等價的 critical-helicity energy identity。

因此：

$$
\boxed{
\mathcal E_+(t)-\mathcal E_-(t)=c_0
}
$$

不是本文新定理。

本文新增的工作是把此 identity 接到：

1. hypothetical blow-up 的 critical $L^3$ / $\dot H^{1/2}$ escape；
2. Waleffe helical triad algebra；
3. unique-sign mode provenance；
4. fixed-low-frequency unique-sign contribution的 integrability；
5. X Integration 的 multiscale legality chain。

---

# 1. Helical projector

對 divergence-free $u$，定義：

$$
u^\pm
=
\frac12
\left(
u
\pm
D^{-1}\nabla\times u
\right).
$$

則：

$$
u=u^++u^-,
$$

$$
\nabla\times u^+
=
Du^+,
$$

$$
\nabla\times u^-
=
-Du^-.
$$

並且 $u^+$ 與 $u^-$ 在所有由 $D$ 生成的 Sobolev inner products 中正交。

因此：

$$
\|D^s u\|_2^2
=
\|D^s u^+\|_2^2
+
\|D^s u^-\|_2^2.
$$

---

# 2. External theorem：critical helical energy identity

定義：

$$
\boxed{
\mathcal E_\pm(t)
=
\frac12
\|D^{1/2}u^\pm(t)\|_2^2
+
\nu
\int_0^t
\|D^{3/2}u^\pm(s)\|_2^2\,ds.
}
$$

Lei–Lin–Zhou 的 Structure of Helicity theorem 給：

$$
\boxed{
\mathcal E_+(t)
=
\mathcal E_-(t)
+
c_0,
}
$$

其中：

$$
\boxed{
c_0
=
\frac12
\left(
\|D^{1/2}u_0^+\|_2^2
-
\|D^{1/2}u_0^-\|_2^2
\right).
}
$$

所以：

$$
\boxed{
\mathcal E_+(t)-\mathcal E_-(t)=c_0
}
$$

對所有 smooth existence times成立。

這是一個 scaling-critical identity。

---

# 3. Common production primitive

令：

$$
\mathcal R(t)
=
\mathcal E_+'(t)
=
\mathcal E_-'(t).
$$

則：

$$
\boxed{
\mathcal E_\pm(t)
=
\mathcal E_\pm(0)
+
\int_0^t
\mathcal R(s)\,ds.
}
$$

因此 positive / negative helical sector 的 cumulative critical energy，除初始常數外，具有**完全相同的增量歷史**。

此處：

$$
\mathcal R
$$

就是前一輪稱為 critical helical pair-production rate 的 quantity。

---

# 4. Hypothetical blow-up implies unbounded critical size

由 endpoint $L^3$ regularity theorem，若：

$$
T_\ast<\infty
$$

為 maximal classical singular time，則：

$$
\limsup_{t\uparrow T_\ast}
\|u(t)\|_3
=
\infty.
$$

又：

$$
\dot H^{1/2}(\mathbb R^3)
\hookrightarrow
L^3(\mathbb R^3),
$$

所以：

$$
\boxed{
\limsup_{t\uparrow T_\ast}
\|D^{1/2}u(t)\|_2
=
\infty.
}
$$

由 helical orthogonality：

$$
\|D^{1/2}u\|_2^2
=
H_++H_-.
$$

---

# 5. C3-B.1：Bi-Helical Critical-Energy Escalation

## 定理 5.1

假設 $T_\ast<\infty$ 為 finite singular time。

則存在：

$$
t_n\uparrow T_\ast
$$

使：

$$
\boxed{
\mathcal E_+(t_n)\to\infty,
\qquad
\mathcal E_-(t_n)\to\infty.
}
$$

### 證明

選：

$$
t_n\uparrow T_\ast
$$

使：

$$
H_+(t_n)+H_-(t_n)
\to\infty.
$$

因：

$$
\mathcal E_+(t)+\mathcal E_-(t)
\ge
\frac12
\left(
H_+(t)+H_-(t)
\right),
$$

故：

$$
S_n
:=
\mathcal E_+(t_n)+\mathcal E_-(t_n)
\to\infty.
$$

又：

$$
\mathcal E_+(t_n)-\mathcal E_-(t_n)
=
c_0.
$$

所以：

$$
\mathcal E_+(t_n)
=
\frac{S_n+c_0}{2},
$$

$$
\mathcal E_-(t_n)
=
\frac{S_n-c_0}{2}.
$$

因此兩者同時趨於無窮。$\square$

---

# 6. C3-B.2：Asymptotic Critical-Energy Equalization

## 推論 6.1

在定理 5.1 的 sequence 上：

$$
\boxed{
\frac{\mathcal E_+(t_n)}
{\mathcal E_-(t_n)}
\to1.
}
$$

### 證明

$$
\frac{\mathcal E_+(t_n)}
{\mathcal E_-(t_n)}
=
\frac{S_n+c_0}{S_n-c_0}.
$$

因：

$$
S_n\to\infty,
$$

故比值趨於 $1$。$\square$

---

# 7. 物理／ETN 解讀

因此 hypothetical blow-up 不能在 cumulative critical-energy level 永遠保持：

$$
\mathcal E_+\gg\mathcal E_-
$$

或：

$$
\mathcal E_-\gg\mathcal E_+.
$$

不論初始 helicity bias：

$$
c_0
$$

多大，只要 critical energy 真的逃向無窮，固定初始差最終都會變成 negligible。

故：

$$
\boxed{
\mathrm{Blowup}
\Rightarrow
\text{asymptotic bi-helical critical-energy equalization}.
}
$$

注意：

這不是說 instantaneous：

$$
H_+(t_n)/H_-(t_n)\to1.
$$

因為 cumulative dissipation 也包含在：

$$
\mathcal E_\pm.
$$

正確命題只作用於：

$$
\boxed{
\text{state critical energy + accumulated critical dissipation}.
}
$$

---

# 8. Pair-production primitive must diverge

由：

$$
\mathcal E_\pm(t)
=
\mathcal E_\pm(0)
+
\int_0^t
\mathcal R(s)\,ds,
$$

以及定理 5.1：

$$
\boxed{
\limsup_{t\uparrow T_\ast}
\int_0^t
\mathcal R(s)\,ds
=
\infty.
}
$$

因此：

$$
\boxed{
\int_0^{T_\ast}
[\mathcal R(s)]_+\,ds
=
\infty.
}
$$

這重新得到 C3-A 的 pair-production divergence，但現在被嵌入已知 critical-energy identity 中。

---

# 9. External input：triad-by-triad conservation

對一個 Fourier triad：

$$
\mathbf k+\mathbf p+\mathbf q=0,
$$

令：

$$
k=|\mathbf k|,
\qquad
p=|\mathbf p|,
\qquad
q=|\mathbf q|,
$$

並排序：

$$
0<k\le p\le q.
$$

helical signs：

$$
s_k,s_p,s_q\in\{+1,-1\}.
$$

令：

$$
e_k
=
\frac12|u^{s_k}(\mathbf k)|^2,
$$

其餘類同。

Waleffe helical decomposition以及後續 work 的基本性質是：

每一個 closed nonlinear triad 分別保存 energy 與 signed helicity：

$$
\boxed{
\dot e_k+\dot e_p+\dot e_q=0,
}
$$

$$
\boxed{
s_k k\dot e_k
+
s_p p\dot e_p
+
s_q q\dot e_q
=
0.
}
$$

---

# 10. Transfer-nullspace lemma

## 引理 10.1

對 nondegenerate triad transfer，存在 scalar：

$$
\Theta_\tau(t)
$$

使：

$$
\boxed{
\begin{pmatrix}
\dot e_k\\
\dot e_p\\
\dot e_q
\end{pmatrix}
=
\Theta_\tau
\begin{pmatrix}
s_p p-s_q q\\
s_q q-s_k k\\
s_k k-s_p p
\end{pmatrix}.
}
$$

### 證明

transfer vector：

$$
(\dot e_k,\dot e_p,\dot e_q)
$$

同時 orthogonal to：

$$
(1,1,1)
$$

與：

$$
(s_k k,s_p p,s_q q).
$$

在 nondegenerate case，其共同 orthogonal complement 是一維。

兩向量的 cross product 正比於：

$$
(s_p p-s_q q,\,
s_q q-s_k k,\,
s_k k-s_p p).
$$

故得。$\square$

此 lemma 只使用 triadwise invariants，不依賴 instability assumption。

---

# 11. Absolute critical content of a triad

定義：

$$
\boxed{
\mathscr A_\tau
=
k e_k
+
p e_p
+
q e_q.
}
$$

它等於該 triad 對：

$$
\frac12
\|D^{1/2}u\|_2^2
$$

的 contribution。

signed helicity half-density為：

$$
\mathscr H_\tau
=
s_k k e_k
+
s_p p e_p
+
s_q q e_q.
$$

nonlinear dynamics保：

$$
\dot{\mathscr H}_\tau=0.
$$

但：

$$
\dot{\mathscr A}_\tau
$$

一般不為零。

---

# 12. 四類 independent helicity configurations

global sign reversal不改變 interaction class，因此固定最小波數 sign 為 $+$。

四類：

$$
\mathrm{I}: (+++),
$$

$$
\mathrm{II}: (+--),
$$

$$
\mathrm{III}: (+-+),
$$

$$
\mathrm{IV}: (++-).
$$

其中：

- I = homochiral；
- II–IV = heterochiral。

---

# 13. Class I：homochiral pair production exactly zero

對：

$$
(s_k,s_p,s_q)=(+,+,+),
$$

signed helicity等於 absolute critical content：

$$
\mathscr H_\tau
=
\mathscr A_\tau.
$$

因此：

$$
\boxed{
\dot{\mathscr A}_\tau=0.
}
$$

global sign reversal：

$$
(---)
$$

同樣：

$$
\dot{\mathscr A}_\tau=0.
$$

所以：

$$
\boxed{
\text{homochiral triads do not produce positive critical absolute helicity}.
}
$$

它們可以 redistribute energy，但不能改變該 triad 的：

$$
k e_k+p e_p+q e_q.
$$

---

# 14. Heterochiral unique-sign identity

每個 heterochiral triad 都有一個 **unique-helicity-sign mode**。

若其 wavenumber 為：

$$
r_\tau,
$$

energy 為：

$$
e_{\rm uniq},
$$

則由 signed helicity conservation：

$$
\boxed{
\dot{\mathscr A}_\tau
=
2r_\tau
\dot e_{\rm uniq}.
}
$$

因此定義該 triad 對 common sector-production rate 的 contribution：

$$
\boxed{
\mathcal R_\tau
=
r_\tau
\dot e_{\rm uniq}.
}
$$

則：

$$
\dot{\mathscr A}_\tau
=
2\mathcal R_\tau.
$$

所以「critical pair production」可以完全重新解讀成：

$$
\boxed{
\text{wavenumber-weighted energy transfer into the unique-helicity-sign mode}.
}
$$

---

# 15. Exact triad table

由引理 10.1：

## Class II

$$
(+--).
$$

unique sign 在最小 wavenumber：

$$
r_\tau=k.
$$

有：

$$
\dot e_k
=
(q-p)\Theta_\tau.
$$

因此：

$$
\boxed{
\mathcal R_{\mathrm{II}}
=
k(q-p)\Theta_\tau.
}
$$

---

## Class III

$$
(+-+).
$$

unique sign 在中間 wavenumber：

$$
r_\tau=p.
$$

有：

$$
\dot e_p
=
(q-k)\Theta_\tau.
$$

因此：

$$
\boxed{
\mathcal R_{\mathrm{III}}
=
p(q-k)\Theta_\tau.
}
$$

---

## Class IV

$$
(++-).
$$

unique sign 在最大 wavenumber：

$$
r_\tau=q.
$$

有：

$$
\dot e_q
=
(k-p)\Theta_\tau.
$$

因此：

$$
\boxed{
\mathcal R_{\mathrm{IV}}
=
q(k-p)\Theta_\tau.
}
$$

正負號由：

$$
\Theta_\tau
$$

與 class orientation共同決定；本文不使用 Waleffe instability assumption 來宣告 instantaneous transfer sign。

---

# 16. Same-sign radial-gap factorization

對 heterochiral triad，另兩個 mode 有相同 helicity sign。

令其 radial wavenumber gap：

$$
\Delta_\tau
=
\left|
a_\tau-b_\tau
\right|.
$$

則上節三式統一寫成：

$$
\boxed{
|\mathcal R_\tau|
=
r_\tau
\Delta_\tau
|\Theta_\tau|.
}
$$

因此 pair production 具有兩個必要 structural factors：

$$
\boxed{
\text{unique-sign scale}
\times
\text{same-sign radial separation}.
}
$$

若：

$$
\Delta_\tau=0,
$$

則：

$$
\boxed{
\mathcal R_\tau=0.
}
$$

即使該 triad 是 heterochiral。

---

# 17. Triangle-gap bound

由 triad triangle inequalities：

### Class II

$$
q-p\le k.
$$

### Class III

$$
q-k\le p.
$$

### Class IV

$$
p-k\le q.
$$

所以統一有：

$$
\boxed{
0\le
\Delta_\tau
\le
r_\tau.
}
$$

因此：

$$
\boxed{
|\mathcal R_\tau|
\le
r_\tau^2
|\Theta_\tau|.
}
$$

此 inequality 不是 global regularity estimate；它只是 exact class factorization 的 geometric consequence。

---

# 18. X-Guard：pair production 的最低形成資格

一個 triad 要對：

$$
\mathcal R
$$

產生非零 contribution，至少必須同時通過：

### G-H — Heterochiral guard

$$
\text{not all }s_k,s_p,s_q\text{ equal}.
$$

### G-U — Unique-sign participation

unique-helicity mode amplitude / transfer不能退化。

### G-$\Delta$ — Radial-gap guard

$$
\Delta_\tau>0.
$$

### G-GEO — geometric coupling guard

helical triple-product / Leray-projected interaction coefficient不能為零。

### G-PHASE — phase-transfer guard

instantaneous triad phase必須給：

$$
\Theta_\tau\ne0.
$$

因此：

$$
\boxed{
\text{heterochiral}
\not\Rightarrow
\text{pair-producing}.
}
$$

X Integration 在這裡不是增加方程，而是防止把「mixed sign」直接偷換成「危險 transfer」。

---

# 19. Global unique-sign representation of common production

所有 heterochiral triads可按 unique sign 分成兩族：

1. unique $+$；
2. unique $-$。

因此 global common production可寫成 unique-sign transfer sum。

在 physical-space bilinear notation下，對應為：

$$
\boxed{
\mathcal R
=
\mathcal R_{\mathrm{uniq}+}
+
\mathcal R_{\mathrm{uniq}-},
}
$$

其中：

$$
\mathcal R_{\mathrm{uniq}+}
=
-
\left\langle
D u^+,
\mathbb P^+
\big(
(u^-\cdot\nabla)u^-
\big)
\right\rangle,
$$

$$
\mathcal R_{\mathrm{uniq}-}
=
-
\left\langle
D u^-,
\mathbb P^-
\big(
(u^+\cdot\nabla)u^+
\big)
\right\rangle.
$$

這是「每個 heterochiral triad只由它的 unique-sign mode 計帳一次」的 representation。

---

# 20. Fixed-low unique-sign cutoff

令：

$$
P_{\le K}
$$

為 smooth Fourier low-pass。

定義：

$$
\mathcal R_{\le K}^{\mathrm{uniq}}
=
-
\left\langle
D P_{\le K}u^+,
(u^-\cdot\nabla)u^-
\right\rangle
-
\left\langle
D P_{\le K}u^-,
(u^+\cdot\nabla)u^+
\right\rangle.
$$

Leray / helical projectors可在 pairing 中省略，因 test field 已 divergence-free 且位於指定 helical sector。

---

# 21. C3-B.3：Fixed-Low Unique-Sign Production Bound

## 定理 21.1

對任意 fixed：

$$
K<\infty,
$$

有：

$$
\boxed{
\left|
\mathcal R_{\le K}^{\mathrm{uniq}}(t)
\right|
\le
C
K^{7/2}
\|u(t)\|_2^3.
}
$$

因此由 energy inequality：

$$
\boxed{
\left|
\mathcal R_{\le K}^{\mathrm{uniq}}(t)
\right|
\le
C
K^{7/2}
\|u_0\|_2^3.
}
$$

### 證明

考察第一項。

因：

$$
\nabla\cdot u^-=0,
$$

integration by parts：

$$
\left\langle
D P_{\le K}u^+,
(u^-\cdot\nabla)u^-
\right\rangle
=
-
\int
(u^-\otimes u^-):
\nabla D P_{\le K}u^+
\,dx.
$$

故：

$$
\left|
\left\langle
D P_{\le K}u^+,
(u^-\cdot\nabla)u^-
\right\rangle
\right|
\le
\|\nabla D P_{\le K}u^+\|_\infty
\|u^-\|_2^2.
$$

Bernstein inequality給：

$$
\|\nabla D P_{\le K}u^+\|_\infty
\le
C
K^{7/2}
\|u^+\|_2.
$$

所以：

$$
\le
C
K^{7/2}
\|u^+\|_2
\|u^-\|_2^2.
$$

第二項同理：

$$
\le
C
K^{7/2}
\|u^-\|_2
\|u^+\|_2^2.
$$

相加並使用：

$$
\|u^\pm\|_2\le\|u\|_2
$$

得：

$$
|\mathcal R_{\le K}^{\mathrm{uniq}}|
\le
C
K^{7/2}
\|u\|_2^3.
$$

再由 Leray energy inequality：

$$
\|u(t)\|_2\le\|u_0\|_2.
$$

證畢。$\square$

---

# 22. Fixed-low contribution is time-integrable

若：

$$
T_\ast<\infty,
$$

則：

$$
\boxed{
\int_0^{T_\ast}
\left|
\mathcal R_{\le K}^{\mathrm{uniq}}(t)
\right|
dt
\le
C
T_\ast
K^{7/2}
\|u_0\|_2^3
<
\infty.
}
$$

所以：

$$
\boxed{
\text{固定低頻 unique-helicity modes
不能承擔 divergent cumulative pair production}.
}
$$

---

# 23. C3-B.4：Unique-Sign UV Escape Theorem

令：

$$
\mathcal R_{>K}^{\mathrm{uniq}}
=
\mathcal R
-
\mathcal R_{\le K}^{\mathrm{uniq}}.
$$

## 定理 23.1

若：

$$
T_\ast<\infty
$$

為 finite singular time，則對每個 fixed：

$$
K<\infty,
$$

都有：

$$
\boxed{
\int_0^{T_\ast}
\left[
\mathcal R_{>K}^{\mathrm{uniq}}(t)
\right]_+
dt
=
\infty.
}
$$

### 證明

已知：

$$
\int_0^{T_\ast}
[\mathcal R(t)]_+dt
=
\infty.
$$

又：

$$
\mathcal R
=
\mathcal R_{\le K}^{\mathrm{uniq}}
+
\mathcal R_{>K}^{\mathrm{uniq}}.
$$

所以：

$$
[\mathcal R]_+
\le
\left|
\mathcal R_{\le K}^{\mathrm{uniq}}
\right|
+
\left[
\mathcal R_{>K}^{\mathrm{uniq}}
\right]_+.
$$

第一項 time integral finite。

因此第二項的 positive-part integral 必須發散。$\square$

---

# 24. 這比 C1 的 UV escape 更細

C1a：

$$
\text{velocity critical tail must escape every fixed frequency}.
$$

C3-B.4：

$$
\boxed{
\text{the unique-helicity source responsible for critical pair production
must also escape every fixed frequency}.
}
$$

所以不能只靠：

> 一個固定低頻 opposite-helicity catalyst

反覆驅動無限 critical growth。

若 blow-up 存在，真正負責 pair-production 的 unique-sign participant 本身必須不斷進入更高頻率。

---

# 25. High–High necessity

考慮 heterochiral triad，unique-sign wavenumber：

$$
r_\tau>K.
$$

由 triangle inequality，至少一個其他 wavenumber：

$$
a_\tau
$$

滿足：

$$
\boxed{
a_\tau
\ge
\frac12r_\tau
>
\frac12K.
}
$$

因此：

## 推論 25.1

C3-B.4 的 UV pair-production tail 必然由至少 two-high-frequency interaction 支援：

$$
\boxed{
\text{unique high}
+
\text{at least one comparable-high partner}.
}
$$

所以 hypothetical singular pair-production 不能是：

$$
\boxed{
\text{high} \leftarrow \text{low}+\text{low}.
}
$$

而必須包含真正的 high–high geometry。

---

# 26. Class-specific interpretation

### Class II：$(+--)$

unique sign在最小 wavenumber：

$$
r=k.
$$

若：

$$
k>K,
$$

則：

$$
p,q>K.
$$

所以 Class II 的 UV contribution必然是 three-high-frequency triad。

### Class III：$(+-+)$

unique sign在 medium：

$$
r=p>K,
$$

故：

$$
q\ge p>K.
$$

至少 medium + high兩個 mode都 high。

### Class IV：$(++-)$

unique sign在 largest：

$$
r=q>K.
$$

triangle inequality：

$$
q\le k+p\le2p
$$

給：

$$
p\ge q/2>K/2.
$$

所以也必有第二個 comparable-high mode。

---

# 27. C3-A minority-factor candidate 的正式降級

上一輪提出候選：

$$
|\mathcal R|
\stackrel{?}{\le}
C
\min
\left\{
\|u^+\|_{\dot H^{1/2}},
\|u^-\|_{\dot H^{1/2}}
\right\}
\|u\|_{\dot H^{3/2}}^2.
$$

本輪 exact triad audit顯示：

- 每個 pair-producing triad確實包含兩種 helicity signs；
- 但 unique-sign mode可以作為 **output/test mode**；
- 因此「每個 monomial 含 minority sign」本身不足以把 global minority factor放在 $\dot H^{1/2}$。

所以目前裁決：

$$
\boxed{
\text{Minority-}\dot H^{1/2}\text{ estimate = OPEN, not established.}
}
$$

不得使用它推出 regularity。

---

# 28. 一個可安全使用的 weaker estimate

由 standard critical bilinear estimate：

$$
\|
\mathbb P(u\cdot\nabla u)
\|_{\dot H^{-1/2}}
\le
C
\|u\|_{\dot H^{1/2}}
\|u\|_{\dot H^{3/2}},
$$

以及：

$$
\mathcal R
=
\mathcal R_+
=
\mathcal R_-,
$$

可分別得到：

$$
|\mathcal R|
\le
C
\|u\|_{\dot H^{1/2}}
\|u\|_{\dot H^{3/2}}
\|u^+\|_{\dot H^{3/2}},
$$

及：

$$
|\mathcal R|
\le
C
\|u\|_{\dot H^{1/2}}
\|u\|_{\dot H^{3/2}}
\|u^-\|_{\dot H^{3/2}}.
$$

故：

$$
\boxed{
|\mathcal R|
\le
C
\|u\|_{\dot H^{1/2}}
\|u\|_{\dot H^{3/2}}
\min
\left\{
\|u^+\|_{\dot H^{3/2}},
\|u^-\|_{\dot H^{3/2}}
\right\}.
}
$$

這是 **minority-dissipation factor**，而不是原本更強的 minority-critical-size factor。

它本身尚不足以關閉 global regularity。

---

# 29. X-Integration：新版 singular-chain certificate

hypothetical blow-up 的 pair-production chain 現在至少必須保存：

$$
\boxed{
\operatorname{XHelUV}_n
=
\left\langle
r_n,
\Delta_n,
s_n,
\Theta_n,
\mathcal R_n,
\mathcal E_n^+,
\mathcal E_n^-,
\operatorname{Prov}_n
\right\rangle.
}
$$

守衛：

1. **heterochiral**；
2. **unique-sign mode存在**；
3. **same-sign radial gap非零**；
4. **helical geometry非退化**；
5. **phase transfer非零**；
6. **unique-sign scale必須逃出任意 fixed cutoff**；
7. **至少一個 partner與 unique scale comparable-high**；
8. **兩 sector cumulative critical energy最終 equalize**；
9. 每次尺度轉換重新審核，不由前一步合法自動推出下一步合法。

---

# 30. 新 frontier：C3-C

現在真正的 hypothetical singular route被壓成：

$$
\boxed{
\text{heterochiral}
+
\text{high unique-sign source}
+
\text{high partner}
+
\text{nonzero radial gap}
+
\text{nondegenerate geometry}
+
\text{positive cumulative phase transfer}.
}
$$

因此下一步不再是「所有 helical triads」。

只需要攻這個 narrow survivor set。

C3-C 候選名稱：

$$
\boxed{
\textbf{High–High Heterochiral Congestion Rigidity}.
}
$$

研究問題：

> 當 unique-sign mode與至少一個 partner都被迫走向無限高頻時，exact N–S triad geometry、radial-gap factor、phase alignment與 viscosity 是否允許這些合法 pair-production events 在 finite time 無限串接？

---

# 31. 下一步 proof obligations

## C3-C.1 — Dyadic unique-sign decomposition

定義：

$$
\mathcal R_q^{\mathrm{uniq}}
$$

為 unique-sign mode位於 shell $q$ 的 pair production。

由 C3-B.4 推導 tail law：

$$
\forall Q,
\qquad
\int
\left[
\sum_{q>Q}
\mathcal R_q^{\mathrm{uniq}}
\right]_+
dt
=
\infty.
$$

再研究是否能得到 shellwise packing constraints。

## C3-C.2 — Relative-gap split

定義：

$$
\eta_\tau
=
\frac{\Delta_\tau}{r_\tau}
\in[0,1].
$$

研究：

$$
\eta_\tau\ll1
$$

的 near-radially-degenerate triads 是否可被 perturbatively absorbed。

## C3-C.3 — Class II nonlocal suppression

Class II：

$$
\mathcal R_{\mathrm{II}}
=
k(q-p)\Theta.
$$

當：

$$
k\ll p\sim q,
$$

有：

$$
q-p\le k,
$$

所以：

$$
|\mathcal R_{\mathrm{II}}|
\lesssim
k^2|\Theta|.
$$

研究 strongly nonlocal Class II 是否可由 low-frequency energy bounds完全積分控制。

## C3-C.4 — Classes III/IV core

若 C3-C.3 成立，主要 survivor將進一步集中至：

$$
\boxed{
\mathrm{Class\ III/IV}
}
$$

或 fully high local Class II。

這將更靠近 forward small-scale transfer channels。

## C3-C.5 — Phase persistence

$\Theta_\tau$ 包含 triad phase / amplitude / geometric coefficient。

即使所有 amplitude guard通過，仍需：

$$
\mathcal R_\tau>0
$$

在足夠長的跨尺度 sequence 上持續。

研究 phase-sign persistence是否能形成新的 finite obstruction。

---

# 32. 正式狀態

$$
\boxed{
\begin{aligned}
\text{Lei--Lin--Zhou critical energy difference}
&:\ \mathrm{EXTERNAL\ THEOREM},\\
\mathrm{Blowup}\Rightarrow
\mathcal E_\pm\to\infty\text{ along a sequence}
&:\ \mathrm{PROVED\ DERIVED},\\
\mathcal E_+/\mathcal E_-\to1
&:\ \mathrm{PROVED\ DERIVED},\\
\text{homochiral }\mathcal R_\tau=0
&:\ \mathrm{PROVED},\\
\text{heterochiral unique-sign factorization}
&:\ \mathrm{PROVED},\\
\Delta_\tau\le r_\tau
&:\ \mathrm{PROVED},\\
\text{fixed-low unique-sign production integrable}
&:\ \mathrm{PROVED},\\
\mathrm{Blowup}\Rightarrow
\text{unique-sign UV escape}
&:\ \mathrm{PROVED\ DERIVED},\\
\text{high--high necessity}
&:\ \mathrm{PROVED},\\
\text{minority-}\dot H^{1/2}\text{ estimate}
&:\ \mathrm{OPEN},\\
\text{High--High Heterochiral Congestion Rigidity}
&:\ \mathrm{OPEN}.
\end{aligned}
}
$$

---

# 33. 結論

本輪將 C3 的 survivor geometry 從：

$$
\text{all nonlinear interactions}
$$

壓成：

$$
\boxed{
\text{heterochiral pair-producing interactions}.
}
$$

再由 fixed-low unique-sign bound 壓成：

$$
\boxed{
\text{heterochiral pair production whose unique-sign mode escapes to UV}.
}
$$

triangle geometry 再迫使：

$$
\boxed{
\text{at least one comparable-high partner}.
}
$$

因此 hypothetical singularity 的 critical production core 現在是：

$$
\boxed{
\textbf{High--High Heterochiral UV Pair-Production Chain}.
}
$$

同時，Lei–Lin–Zhou identity 給出另一個獨立必要條件：

$$
\boxed{
\textbf{the two helical critical-energy histories must asymptotically equalize}.
}
$$

所以任何 blow-up scenario都必須同時做到：

1. 向無限高頻推進；
2. 保持 heterochiral interaction；
3. 讓 unique-sign source 本身升頻；
4. 保持至少 two-high-frequency coupling；
5. 持續通過 radial-gap / geometry / phase guards；
6. 將正負 sector 的 cumulative critical energy拉向 asymptotic parity。

這已比單純「energy cascade beats viscosity」窄得多。

下一輪：

$$
\boxed{
\textbf{C3-C — High–High Heterochiral Congestion Rigidity}
}
$$

優先攻：

$$
\boxed{
\text{Class II nonlocal suppression}
\to
\text{III/IV survivor reduction}
\to
\text{dyadic pair-production packing}.
}
$$

---

# References

1. Z. Lei, F.-H. Lin, Y. Zhou, *Structure of Helicity and Global Solutions of Incompressible Navier–Stokes Equation*, Archive for Rational Mechanics and Analysis; arXiv:1505.00142.
2. F. Waleffe, *The nature of triad interactions in homogeneous turbulence*, Physics of Fluids A 4 (1992), 350–363.
3. L. Biferale, E. S. Titi, *On the Global Regularity of a Helical-decimated Version of the 3D Navier–Stokes Equations*, Journal of Statistical Physics; arXiv:1303.1215.
4. G. Sahoo, L. Biferale, *Disentangling the triadic interactions in Navier-Stokes equations*, European Physical Journal E; arXiv:1510.09006.
5. G. Sahoo, L. Biferale, *Energy Cascade and Intermittency in Helically Decomposed Navier-Stokes Equations*, Fluid Dynamics Research; arXiv:1709.03713.
6. L. Escauriaza, G. Seregin, V. Šverák, endpoint $L^3$ regularity theorem for 3D Navier–Stokes.

# Internal dependencies

- `NS_ETN_XIntegration_Multiscale_NonCollapse_v0.1.md`
- `NS_C1_UV_Replenishment_Chain_v0.2.md`
- `NS_C2_Critical_Toll_Spike_Packing_v0.3.md`
- `NS_C3A_Conservation_Criticality_Helical_Pair_Production_v0.1.md`
- `True ETN / 無限維張力場`
- `X_Integral_Unified_Program_v0.2.md`

Next:

$$
\boxed{
\textbf{C3-C — High–High Heterochiral Congestion Rigidity}
}
$$
