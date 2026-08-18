---
title: "Navier–Stokes C5-G：Pressure-Signature Defects、Vorticity Constraint Complements 與 Fixed-Order Derivative-Gate Closure"
subtitle: "A Theorem-Ready Fixed-k Direct Sparseness Gate, Pressure-Poisson Re-entry from Vorticity Leakage, and Signature-Boundary Compactification"
version: "v0.1"
date: "2026-08-15"
author: "Neo.K / EveMissLab"
language: "zh-TW"
status: "Theorem-style fixed-order gate closure / pressure-signature and constraint-complement reduction"
epistemic_status: "Exact component-volume geometry + direct interface to Grujić–Xu Theorem 3.5 + exact pressure Poisson/projection identities + conditional pressure-signature heredity. Does NOT prove Navier–Stokes regularity."
---

# Navier–Stokes C5-G
# Pressure-Signature Defects、Vorticity Constraint Complements 與 Fixed-Order Derivative-Gate Closure

## 0. 本輪定位

C5-F 把 residual network壓成：

$$
\boxed{
\text{Pressure-Signature Defect}
}
$$

$$
\boxed{
\text{Vorticity Constraint-Complement Defect}
}
$$

$$
\boxed{
\text{Fixed-Order Derivative-Gate Defect}
}
$$

$$
\boxed{
\text{Asymptotically-Critical Derivative-Order Escape}.
}
$$

其中最值得優先死扣的是 fixed-order direct gate。

原因是：

C5-E/F 已經發現：

- middle-gap cubic intermittency可以產生很小的 strain active volume；
- strain-derivative leakage可以產生 critical $D^2u$ amplitude；
- spatial exponent本身開始 favorable；

但之前仍保留：

- SHELLFULL；
- COMPSIGN；
- MULT；
- TIMECHAIN；

等 theorem-interface debts。

C5-G 現在做一個更乾淨的 move：

> **直接對 full $D^ku$ 的 component/sign superlevel sets做 global volume bound。**

這樣：

- 不需要 shell-to-full conversion；
- 不需要 strain-to-$Du$ conversion；
- 不需要先猜 selected component/sign；
- Theorem 3.5所要求的 component/sign high set本身直接被控制。

本輪主要結果：

1. 任意 fixed $k\ge1$，
   full derivative component/sign superlevel set的 global volume有：
   $$
   \boxed{
   |V_{\lambda,k}^{i,\pm}|
   \le
   \lambda^{-2}
   \|D^ku\|_2^2
   \|D^ku\|_\infty^{-2};
   }
   $$
2. volume-to-line把它變成 theorem-ready 1D sparseness尺度：
   $$
   \boxed{
   r_{vol,k}
   \lesssim
   \|D^ku\|_2^{2/3}
   \|D^ku\|_\infty^{-2/3};
   }
   $$
3. 與 Grujić–Xu 2024 Theorem 3.5 direct scale：
   $$
   \boxed{
   r_{GX,k}
   =
   \frac1{
   2^k c(M,\|u_0\|_2)
   \|D^ku(s)\|_\infty^{3/(2k+3)}
   }
   }
   $$
   比較；
4. 若 theorem-admissible later time：
   $$
   s=s(t)
   $$
   上：
   $$
   \boxed{
   r_{vol,k}(s)
   \le
   r_{GX,k}(s),
   }
   $$
   則 Theorem 3.5真正閉合；
5. 因此 fixed-order `COMPSIGN` 與 `SHELLFULL` defects可在此 direct-volume route中被旁路；
6. 真正 fixed-order direct survivor只剩：
   $$
   \boxed{
   \text{Derivative Effective-Volume / Multiplicity Defect}
   \vee
   \text{Theorem Later-Time Defect};
   }
   $$
7. 對 $k=1$：
   $$
   \|Du\|_2^2=2\|S\|_2^2,
   $$
   所以得到 explicit strain-enstrophy / raw-gradient gate；
8. pressure signature switching在 common hereditary far-matrix route下，
   必：
   $$
   \boxed{
   \text{Pressure Turnover/Fragmentation}
   \vee
   \det F\to0;
   }
   $$
9. middle-gap degeneration不會 erase compressive axis，
   所以 signature-boundary與 axis metadata可同時 compactify；
10. vorticity-dominant leakage利用 exact pressure Poisson identity：
    $$
    \Delta p=-|S|^2+\frac12|\omega|^2
    $$
    直接同步到：
    $$
    \boxed{
    (\Delta p)_+\text{ pressure-curvature activity};
    }
    $$
11. vorticity strain-space complement再由 exact orthogonal ledger壓成：
    $$
    \boxed{
    \text{Actual Pressure Hessian}
    \vee
    \text{Advection Complement}
    \vee
    \text{Strain-Square Complement};
    }
    $$
12. 因而 `Vorticity Constraint-Complement Defect`不再是 free motif；
13. fixed-$k$ direct gate若永久不閉，
    可以量化成一個：
    $$
    \boxed{
    \mathfrak G_k^{dir}>1
    }
    $$
    的 recurrent concentration defect；
14. derivative-order escalation的正確邏輯變成：
    - fixed $k$ recurrent concentration/time defect；
    - 或 eventually no fixed order survives，才送 $k\to\infty$；
15. C5-G 首次把 Grujić–Xu Theorem 3.5接成一個真正可測的 **theorem-ready fixed-order gate ratio**。

---

# 1. Fresh primary-source audit

## 1.1 Grujić–Xu 2024 — Theorem 3.5

正式 version of record：

$$
\boxed{
\text{J. Math. Fluid Mech. 26, Article 53 (2024)}.
}
$$

對 velocity：

令：

$$
t
$$

為：

$$
D^ku
$$

escape time。

Theorem 3.5要求存在 later time：

$$
\boxed{
s=s(t)
}
$$

位於明確 interval：

$$
t
+
C_1
\|D^ku(t)\|_\infty^{-6/(2k+3)}
\le
s
\le
t
+
C_2
\|D^ku(t)\|_\infty^{-6/(2k+3)}
$$

in $d=3$ notation，

使對任意：

$$
x_0,
$$

selected：

$$
D^ku
$$

component/sign superlevel set：

$$
\boxed{
V_{\lambda}^{i,\pm}
=
\{
x:
(D^ku)_i^\pm(x,s)
>
\lambda
\|D^ku(s)\|_\infty
\}
}
$$

在某 scale：

$$
\boxed{
\rho
\le
\frac1{
2^k c(M,\|u_0\|_2)
\|D^ku(s)\|_\infty^{3/(2k+3)}
}
}
$$

1D $\delta$-sparse around：

$$
x_0.
$$

則：

$$
T^\ast
$$

不是 blow-up time。

### C5-G status

我們把這個 theorem當作 external gate。

不修改 theorem hypotheses。

---

# 2. Grujić–Xu 2024 — Theorem 3.7

Theorem 3.7從 Leray energy bound得到 fixed-$k$ a-priori volumetric sparseness scale：

$$
\boxed{
r_{apr,k}
\sim
c(\|u_0\|_2)
\|D^ku\|_\infty^{-2/(2k+3)}
}
$$

for velocity in $d=3$。

而 Theorem 3.5 direct regularity scale exponent：

$$
\boxed{
\frac3{2k+3}
}
$$

更小。

這就是 fixed-order scaling gap。

C5-G不是重新證 Theorem 3.7。

我們加入的是：

$$
\boxed{
\text{actual }L^2\text{ derivative concentration}
}
$$

對 selected high-set的直接 volume estimate。

---

# 3. Grujić–Xu 2024 — Theorem 3.14

main asymptotic-critical theorem使用：

$$
\boxed{
\rho
\lesssim
\|D^ku\|_\infty^{-1/(k+1)}
}
$$

velocity chain scale，

並要求：

- derivative-chain hypotheses；
- later analytic time；
- theorem constants；
- all $k\ge\ell$ structure。

C5-G fixed-order direct route只使用：

$$
\boxed{
\textbf{Theorem 3.5}.
}
$$

不把 Theorem 3.14混進 fixed-order closure。

---

# 4. Fixed derivative quantities

固定：

$$
k\ge1.
$$

在 pre-singular smooth time：

$$
s<T^\ast,
$$

定義：

$$
\boxed{
A_k(s)
=
\|D^ku(s)\|_\infty,
}
$$

$$
\boxed{
L_k(s)
=
\|D^ku(s)\|_2.
}
$$

以下省略：

$$
s
$$

若不混淆。

---

# 5. Selected component/sign high set

對任一 multi-index：

$$
|\zeta|=k,
$$

component：

$$
i,
$$

sign：

$$
\pm,
$$

定義：

$$
\boxed{
V_{\lambda,k}^{\zeta,i,\pm}
=
\{
x:
(D^\zeta u_i)^\pm(x)
>
\lambda A_k
\}.
}
$$

Theorem 3.5 在每：

$$
x_0
$$

選一個：

$$
(\zeta,i,\pm)
$$

對應 local maximal component/sign。

C5-G 的 volume bound對：

$$
\boxed{
\textbf{所有 component/sign uniformly成立}.
}
$$

---

# 6. C5-G.1：Direct Component-Volume Bound

Chebyshev：

$$
\lambda^2
A_k^2
|
V_{\lambda,k}^{\zeta,i,\pm}
|
\le
\int
|D^\zeta u_i|^2dx.
$$

所以：

$$
\boxed{
|
V_{\lambda,k}^{\zeta,i,\pm}
|
\le
\lambda^{-2}
\frac{
L_k^2
}{
A_k^2
}.
}
$$

### 關鍵

沒有：

- strain/rotation decomposition；
- shell conversion；
- component selection問題。

---

# 7. Global-volume to 1D-line sparseness

沿用 C3-W pure geometric lemma。

若 measurable：

$$
E\subset\mathbb R^3
$$

滿足：

$$
|E|
<
c_3
\delta^3
r^3,
$$

則對任意 spatial base point：

$$
x_0,
$$

存在 line direction：

$$
d=d(x_0)
$$

使：

$$
E
$$

在：

$$
x_0-rd
\quad\text{到}\quad
x_0+rd
$$

的 one-dimensional occupancy：

$$
\le
\delta.
$$

---

# 8. Fixed-order effective-volume scale

定義：

$$
\boxed{
V_{k}^{eff}
=
\frac{
L_k^2
}{
A_k^2
}.
}
$$

dimension為 volume。

固定 theorem pair：

$$
(\lambda,\delta)
$$

後，

定義：

$$
\boxed{
r_{vol,k}
=
C_{\lambda,\delta}
\left(
V_k^{eff}
\right)^{1/3}
=
C_{\lambda,\delta}
L_k^{2/3}
A_k^{-2/3}.
}
$$

---

# 9. C5-G.2：Uniform Component/Sign 1D Sparseness

對任意：

$$
x_0,
$$

以及 Theorem 3.5所選：

$$
(\zeta,i,\pm),
$$

superlevel set：

$$
V_{\lambda,k}^{\zeta,i,\pm}
$$

在 scale：

$$
\boxed{
r_{vol,k}
}
$$

1D $\delta$-sparse around：

$$
x_0.
$$

### Proof

C5-G.1給 global volume bound。

選：

$$
r_{vol,k}
$$

使：

$$
|V|
\le
c_3\delta^3r_{vol,k}^3.
$$

套 volume-to-line lemma。$\square$

---

# 10. Published direct target scale

定義：

$$
\boxed{
r_{GX,k}
=
\frac1{
2^k
c_{GX,k}
A_k^{3/(2k+3)}
},
}
$$

其中：

$$
c_{GX,k}
=
c(M,\|u_0\|_2)
$$

表示 Theorem 3.5 的 fixed theorem constant。

---

# 11. Direct gate ratio

定義：

$$
\boxed{
\mathfrak G_k^{dir}
=
\frac{
r_{vol,k}
}{
r_{GX,k}
}.
}
$$

即：

$$
\boxed{
\mathfrak G_k^{dir}
=
C_{\lambda,\delta}
2^k
c_{GX,k}
L_k^{2/3}
A_k^{-\frac23+\frac3{2k+3}}.
}
$$

因：

$$
-\frac23
+
\frac3{2k+3}
=
-
\frac{
4k-3
}{
3(2k+3)
},
$$

所以：

$$
\boxed{
\mathfrak G_k^{dir}
=
C_{\lambda,\delta}
2^k
c_{GX,k}
L_k^{2/3}
A_k^{-\frac{4k-3}{3(2k+3)}}.
}
$$

---

# 12. C5-G.3：Fixed-Order Direct Gate Closure Theorem

## 定理 12.1

令：

$$
t
$$

為 Theorem 3.5意義下的：

$$
D^ku
$$

escape time。

若存在 theorem-admissible：

$$
s=s(t)
$$

使：

$$
\boxed{
\mathfrak G_k^{dir}(s)
\le1,
}
$$

則 Theorem 3.5 hypotheses中的 spatial condition成立，

因此：

$$
\boxed{
T^\ast
\text{ is not a blow-up time}.
}
$$

### 證明

C5-G.2：

selected component/sign superlevel set在：

$$
r_{vol,k}
$$

1D sparse。

若：

$$
r_{vol,k}\le r_{GX,k},
$$

取：

$$
\rho=r_{vol,k}
$$

即滿足 published theorem scale bound。$\square$

---

# 13. Equivalent effective-volume condition

cubing：

$$
r_{vol,k}
\le
r_{GX,k}
$$

等價於：

$$
\boxed{
V_k^{eff}
\le
C_{k,\lambda,\delta,GX}
A_k^{-9/(2k+3)}.
}
$$

因：

$$
V_k^{eff}=L_k^2/A_k^2,
$$

可寫：

$$
\boxed{
L_k^2
\le
C_{k,\lambda,\delta,GX}
A_k^{\frac{4k-3}{2k+3}}.
}
$$

### Important

常數保留 Theorem 3.5 的：

- $M$；
- $\|u_0\|_2$；
- $\lambda,\delta$；
- $k$；

依賴。

不把它們靜默設為 $1$。

---

# 14. k=1 exact form

對：

$$
k=1,
$$

$$
\boxed{
\frac{
4k-3
}{
2k+3
}
=
\frac15.
}
$$

所以 fixed-$k=1$ direct gate condition：

$$
\boxed{
\|Du(s)\|_2^2
\le
C_{GX,1}
\|Du(s)\|_\infty^{1/5}.
}
$$

equivalently：

$$
\boxed{
\|Du(s)\|_\infty
\ge
C'_{GX,1}
\|Du(s)\|_2^{10}.
}
$$

with theorem constants included。

---

# 15. Strain form of k=1 gate

對 whole-space divergence-free smooth：

$$
u,
$$

有：

$$
\boxed{
\|Du\|_2^2
=
\|\omega\|_2^2
=
2
\|S\|_2^2.
}
$$

所以：

$$
\boxed{
\|S(s)\|_2^2
\le
C
\|Du(s)\|_\infty^{1/5}
}
$$

at an admissible Theorem 3.5 later time，

足以閉 fixed-$k=1$ gate。

### 解讀

這是一個：

$$
\boxed{
\textbf{raw-gradient peak vs strain-enstrophy concentration gate}.
}
$$

---

# 16. What happened to COMPSIGN?

C5-A derivative defect：

$$
\mathrm{COMPSIGN}
$$

原本表示：

> 我們只有 magnitude geometry，
> 但 theorem要 component/sign geometry。

C5-G direct-volume route直接對：

$$
(D^\zeta u_i)^\pm
$$

superlevel set作 volume bound。

所以在：

$$
\boxed{
\text{C5-G direct-volume gate}
}
$$

中：

$$
\boxed{
\mathrm{COMPSIGN}
}
$$

不再是獨立 defect。

---

# 17. What happened to SHELLFULL?

C5-H 早期曾有 shell/full derivative conversion問題。

C5-G 現在完全不用：

$$
u_q.
$$

直接對：

$$
\boxed{
D^ku
}
$$

full field作 estimate。

所以：

$$
\boxed{
\mathrm{SHELLFULL}
}
$$

也不再是 fixed-$k$ direct route的獨立 defect。

---

# 18. What remains at fixed k?

因此 fixed Theorem 3.5 route真正 residual只剩：

## G-KMULT — Effective-volume / multiplicity defect

在所有 theorem-admissible later times：

$$
\boxed{
\mathfrak G_k^{dir}>1.
}
$$

也就是：

$$
D^ku
$$

$L^2$ mass相對 $L^\infty$ peak太 diffuse。

## G-KTIME — Later-time defect

escape-time後的 theorem interval與 favorable geometry/amplitude window始終無法對齊。

### Fixed-$k$ direct defect family

$$
\boxed{
\mathfrak D_k^{dir}
=
\{
\mathrm{MULT},
\mathrm{TIME}
\}.
}
$$

---

# 19. Relation to Theorem 3.7

Theorem 3.7用 only kinetic energy / negative Sobolev control，

得到：

$$
r_{apr,k}
\sim
A_k^{-2/(2k+3)}.
$$

C5-G使用 actual：

$$
L_k/A_k
$$

effective volume，

得到：

$$
r_{vol,k}
\sim
L_k^{2/3}A_k^{-2/3}.
$$

如果 derivative field高度 concentrated，

$$
r_{vol,k}
$$

可小於：

$$
r_{GX,k}
\sim
A_k^{-3/(2k+3)},
$$

直接關 gate。

所以 C5-G在測：

$$
\boxed{
\textbf{fixed-order derivative concentration是否足以跨過 scaling gap}.
}
$$

---

# 20. General fixed-order concentration index

定義：

$$
\boxed{
\mathfrak C_k^{eff}
=
\frac{
L_k^2
}{
A_k^{(4k-3)/(2k+3)}
}.
}
$$

在固定 theorem normalization下，

gate condition就是：

$$
\boxed{
\mathfrak C_k^{eff}
\le
C_{GX,k}.
}
$$

### Guard

$\mathfrak C_k^{eff}$單獨不是 universal scale-invariant scalar，

必連同：

$$
C_{GX,k}
$$

及 NS scaling metadata解讀。

真正 dimensionless object仍是：

$$
\boxed{
\mathfrak G_k^{dir}
=
r_{vol,k}/r_{GX,k}.
}
$$

---

# 21. Fixed-order recurrent survivor

若 hypothetical blow-up存在，

則對任意 recurrent fixed：

$$
k
$$

direct route，

每一個 relevant escape time：

$$
t
$$

都必滿足：

$$
\boxed{
\mathfrak G_k^{dir}(s)>1
}
$$

對所有 theorem-admissible：

$$
s
$$

或 favorable time不落在 theorem window。

否則 Theorem 3.5直接排除：

$$
T^\ast.
$$

---

# 22. Derivative-order escalation update

C5-F：

$$
k_j^{best}=k_\ast
$$

or：

$$
k_j^{best}\to\infty.
$$

C5-G現在進一步：

若固定：

$$
k_\ast
$$

recurrent，

its direct defect已壓成：

$$
\boxed{
\mathrm{MULT}
\vee
\mathrm{TIME}.
}
$$

所以若未來能對每 fixed：

$$
k
$$

排除：

- effective-volume diffuseness；
- later-time mismatch；

才合法把 survivor route真正逼向：

$$
\boxed{
k\to\infty.
}
$$

---

# 23. Pressure signature state

回到 C5-F common far-pressure matrix：

$$
\boxed{
F\in\operatorname{Sym}_0(3).
}
$$

若：

$$
F\ne0,
$$

normalize：

$$
\boxed{
\widehat F
=
\frac{
F
}{
|F|_F
}
\in
S^4\cap\operatorname{Sym}_0(3).
}
$$

---

# 24. Signature regions

定義：

$$
\boxed{
\mathcal S_{1-}
=
\{
\widehat F:
\operatorname{sig}F=(-,+,+)
\},
}
$$

$$
\boxed{
\mathcal S_{2-}
=
\{
\widehat F:
\operatorname{sig}F=(-,-,+)
\}.
}
$$

兩者是 open subsets。

共同 boundary：

$$
\boxed{
\Sigma_P
=
\{
\widehat F:
\det F=0
\}.
}
$$

---

# 25. Signature defect distance

定義：

$$
\boxed{
d_{\rm sig}(F)
=
\operatorname{dist}
\left(
\widehat F,
\Sigma_P
\right).
}
$$

若：

$$
F=0,
$$

令：

$$
d_{\rm sig}=0.
$$

所以：

$$
\boxed{
d_{\rm sig}\in[0,1]
}
$$

是一個 compact pressure-signature metadata。

---

# 26. C5-G.4：Opposite Signature Matrices Must Cross the Boundary

若：

$$
F_0,F_1\in\operatorname{Sym}_0(3)
$$

nonzero，

且 signatures：

$$
(-,+,+)
$$

與：

$$
(-,-,+)
$$

不同，

則 line segment：

$$
F(\theta)
=
(1-\theta)F_0+\theta F_1
$$

存在：

$$
\theta_\ast\in(0,1)
$$

使：

$$
\boxed{
\det F(\theta_\ast)=0.
}
$$

### Proof

$$
\det F_0<0,
$$

$$
\det F_1>0,
$$

determinant continuous。$\square$

---

# 27. Signature switching + heredity

C3-U 的 far-pressure heredity架構給：

$$
F_{j+1}-F_j
$$

可被：

- spatial motion；
- temporal turnover；
- source reclassification；

三類 defects控制。

若沿 selected recurrent branch：

$$
\boxed{
\frac{
\|F_{j+1}-F_j\|
}{
\|F_j\|
}
\to0,
}
$$

稱：

$$
\boxed{
\textbf{strong far-matrix heredity}.
}
$$

---

# 28. C5-G.5：Signature Switching Rigidity

假設：

1. strong far-matrix heredity；
2. signatures在：
   $$
   (-,+,+)
   $$
   與：
   $$
   (-,-,+)
   $$
   間 recurrently切換。

則沿 switching subsequence：

$$
\boxed{
d_{\rm sig}(F_j)\to0.
}
$$

### 證明

對每 opposite-signature pair：

$$
F_j,F_{j+1},
$$

segment內存在 singular：

$$
F_j^\ast.
$$

因此：

$$
\operatorname{dist}
(
F_j,
\{\det=0\}
)
\le
\|F_j-F_j^\ast\|
\le
\|F_{j+1}-F_j\|.
$$

除以：

$$
\|F_j\|
$$

並用 heredity。$\square$

---

# 29. Pressure-signature trichotomy

因此 recurrent common far-pressure branch只能：

## G-PFIX

$$
\boxed{
\text{signature eventually fixed};
}
$$

或：

## G-PBOUND

$$
\boxed{
d_{\rm sig}(F_j)\to0;
}
$$

或：

## G-PTURN

$$
\boxed{
\|F_{j+1}-F_j\|/\|F_j\|
\not\to0
}
$$

即：

- pressure turnover；
- source reclassification；
- spatial/far-field fragmentation。

---

# 30. Relation to C5-F axis locking

如果 signature fixed：

$$
(-,+,+),
$$

C5-F strong pressure margin可鎖：

$$
e_1
$$

into one projective cap，

並與 nondegenerate-gap Q cancellation衝突。

如果 signature fixed：

$$
(-,-,+),
$$

仍保留 negative-plane belt geometry。

如果：

$$
d_{\rm sig}\to0,
$$

pressure matrix接近 one-zero-eigenvalue boundary，

形成：

$$
\boxed{
\textbf{Pressure Spectral-Gap Defect}.
}
$$

所以 C5-F 的「signature degeneration」現在正式 compactify。

---

# 31. Middle-gap and pressure signature remain distinct

C5-F已證：

middle gap：

$$
\vartheta\to0
$$

不會 erase compressive axis。

C5-G現在：

pressure signature gap：

$$
d_{\rm sig}\to0
$$

是 far-pressure matrix eigenvalue退化。

兩者是不同 compact boundaries：

$$
\boxed{
\text{Strain Middle-Gap}
\neq
\text{Pressure Signature-Gap}.
}
$$

C5 state必同時保存。

---

# 32. Pressure Poisson identity

對 incompressible：

$$
u,
$$

$$
-\Delta p
=
\partial_i u_j
\partial_j u_i.
$$

以：

$$
\nabla u=S+\Omega,
$$

$$
|\Omega|^2
=
\frac12
|\omega|^2,
$$

有：

$$
\boxed{
-\Delta p
=
|S|^2
-
\frac12
|\omega|^2.
}
$$

所以：

$$
\boxed{
\Delta p
=
-|S|^2
+
\frac12
|\omega|^2.
}
$$

---

# 33. C5-E vorticity-dominant set

回顧：

$$
\boxed{
E_\omega(\eta)
=
\{
|S|^2
<
\eta|Q|
\}.
}
$$

且：

$$
\boxed{
|Q|
\le
|S|^2
+
c_\omega
|\omega|^2,
\qquad
c_\omega
=
\frac{\sqrt2}{4}.
}
$$

所以在：

$$
E_\omega(\eta),
$$

$$
(1-\eta)|S|^2
<
\eta c_\omega|\omega|^2.
$$

即：

$$
\boxed{
|S|^2
<
r_\eta
|\omega|^2,
\qquad
r_\eta
=
\frac{
\eta c_\omega
}{
1-\eta
}.
}
$$

---

# 34. C5-G.6：Vorticity-Dominant Leakage Forces Positive Pressure Laplacian

若：

$$
\boxed{
r_\eta<\frac12,
}
$$

例如：

$$
\eta\le\frac14,
$$

則在：

$$
E_\omega(\eta)
$$

pointwise：

$$
\boxed{
\Delta p
\ge
\left(
\frac12-r_\eta
\right)
|\omega|^2
>0.
}
$$

### 結論

$$
\boxed{
\textbf{Vorticity-Dominant Leakage}
\Rightarrow
\textbf{Positive Pressure-Poisson Curvature}
}
$$

on the same spatial set。

---

# 35. Critical pressure-Poisson stock

若 C5-E branch給：

$$
\boxed{
\frac{
R
}{
\nu^2
}
\int_{E_\omega}
\chi|\omega|^2dx
\ge
w_0,
}
$$

則：

$$
\boxed{
\frac{
R
}{
\nu^2
}
\int
\chi
(\Delta p)_+
dx
\ge
c_\eta
w_0.
}
$$

本文稱：

$$
\boxed{
\textbf{Pressure-Poisson Re-entry Certificate}.
}
$$

---

# 36. Why this is not yet $L^{3/2}$ pressure concentration

large：

$$
\int
(\Delta p)_+
$$

does not by itself lower-bound：

$$
\inf_{\ell\in\mathcal A_1}
\|p-\ell\|_{3/2}
$$

without controlling：

- negative $\Delta p$ outside the leakage set；
- spatial oscillation scale；
- sign-coherent cutoff geometry。

所以：

$$
\boxed{
\text{Pressure-Poisson Re-entry}
}
$$

是 pressure-curvature synchronization，

不是 C4-I pressure-oscillation theorem的 automatic replacement。

---

# 37. Strain-space orthogonal complement

令：

$$
P_{st}
$$

為：

$$
L^2
$$

symmetric-matrix fields到 strain constraint space的 orthogonal projection，

如 Miller–Sawyer Helmholtz-type decomposition。

定義：

$$
\boxed{
P_{st}^{\perp}
=
I-P_{st}.
}
$$

---

# 38. Raw strain nonlinearity

full strain equation：

$$
\partial_tS
+
(u\cdot\nabla)S
-
\nu\Delta S
+
S^2
+
\frac14
(
\omega\otimes\omega
-
|\omega|^2I
)
+
\nabla^2p
=
0.
$$

定義：

$$
\boxed{
\mathcal A
=
(u\cdot\nabla)S,
}
$$

$$
\boxed{
\mathcal S
=
S^2,
}
$$

$$
\boxed{
\mathcal W
=
\frac14
(
\omega\otimes\omega
-
|\omega|^2I
).
}
$$

---

# 39. Exact constraint-complement pressure ledger

因：

$$
\partial_tS-\nu\Delta S
$$

留在 strain constraint space，

apply：

$$
P_{st}^{\perp}.
$$

得到：

$$
\boxed{
\nabla^2p
=
-
P_{st}^{\perp}
(
\mathcal A+\mathcal S+\mathcal W
).
}
$$

定義：

$$
\boxed{
C_A
=
P_{st}^{\perp}\mathcal A,
}
$$

$$
\boxed{
C_S
=
P_{st}^{\perp}\mathcal S,
}
$$

$$
\boxed{
C_\omega
=
P_{st}^{\perp}\mathcal W.
}
$$

則：

$$
\boxed{
\nabla^2p
=
-
(
C_A+C_S+C_\omega
).
}
$$

---

# 40. C5-G.7：Vorticity-Complement Re-entry Trichotomy

若：

$$
\boxed{
\|C_\omega\|_2
\ge
c_0,
}
$$

則至少：

## G-CP

$$
\boxed{
\|\nabla^2p\|_2
\ge
c_0/3,
}
$$

或：

## G-CA

$$
\boxed{
\|C_A\|_2
\ge
c_0/3,
}
$$

或：

## G-CS

$$
\boxed{
\|C_S\|_2
\ge
c_0/3.
}
$$

up to harmless split constants。

### 結論

$$
\boxed{
\textbf{Vorticity Constraint-Complement Congestion}
}
$$

不能孤立存在。

它必同步：

$$
\boxed{
\text{Actual Pressure Hessian}
\vee
\text{Advection Constraint Complement}
\vee
\text{Strain-Square Constraint Complement}.
}
$$

---

# 41. Two pressure re-entry mechanisms

C5-G 現在有兩種 distinct pressure re-entry：

## Trace / Poisson channel

vorticity-dominant physical set：

$$
\boxed{
\Delta p>0.
}
$$

## Constraint-complement channel

large：

$$
C_\omega
$$

forces：

$$
\boxed{
\nabla^2p
\vee
C_A
\vee
C_S.
}
$$

兩者不能混成一個 scalar pressure quantity。

---

# 42. Fixed k=1 now bypasses vorticity field conversion

C5-F 曾把 raw：

$$
Du
$$

high set分成：

$$
S
$$

high set與：

$$
\omega
$$

high set。

這是 useful spatial provenance。

但 C5-G fixed-$k=1$ direct gate對：

$$
Du
$$

component/sign high set本身作 global volume bound。

所以：

$$
\boxed{
\textbf{Theorem 3.5 spatial gate不再需要 vorticity-field conversion}.
}
$$

vorticity geometry仍重要於：

- Q cancellation；
- pressure；
- operator；

但不再是 fixed-$k=1$ component/sign conversion的必要障礙。

---

# 43. k=1 direct gate ratio in strain variables

因：

$$
L_1^2
=
2\|S\|_2^2,
$$

$$
A_1
=
\|Du\|_\infty,
$$

所以：

$$
\boxed{
\mathfrak G_1^{dir}
=
C_{GX}
\|S\|_2^{2/3}
\|Du\|_\infty^{-1/15}.
}
$$

up to fixed theorem constants。

### Important

exponent：

$$
1/15
$$

很小。

所以 k=1 direct closure需要：

$$
\boxed{
\textbf{very strong peak concentration relative to enstrophy}.
}
$$

這說明為什麼 k=1雖 theorem-ready，

仍可能是難 gate。

---

# 44. k=2 direct gate ratio

$$
\boxed{
\mathfrak G_2^{dir}
=
C_{GX,2}
\|D^2u\|_2^{2/3}
\|D^2u\|_\infty^{-5/21}.
}
$$

因：

$$
\frac{
4k-3
}{
3(2k+3)
}
=
\frac5{21}
$$

at：

$$
k=2.
$$

C5-E/F 可提供：

- $D^2u$ amplitude lower bound；
- $\nabla S$ stock；

但 gate仍取決於 amplitude對 $L^2$ mass是否夠 concentrated。

---

# 45. General fixed-k behavior

amplitude exponent in：

$$
\mathfrak G_k^{dir}
$$

是：

$$
\boxed{
\frac{
4k-3
}{
3(2k+3)
}
}
$$

which increases：

$$
\frac1{15},
\frac5{21},
\ldots
\to
\frac23.
$$

所以 purely at this effective-volume formula level：

$$
\boxed{
\text{higher derivative peak concentration
has stronger leverage against fixed-}k\text{ direct gap}.
}
$$

但：

$$
L_k
$$

也可能 rapidly grow。

所以仍非 automatic escalation closure。

---

# 46. Fixed-order direct defect state

對每：

$$
k,
$$

定義：

$$
\boxed{
\Theta_k^{dir}
=
\left\langle
\mathfrak G_k^{dir},
\mathsf T_k
\right\rangle,
}
$$

其中：

$$
\mathsf T_k
\in\{0,1\}
$$

表示 theorem later-time gate是否對齊。

Hypothetical survivor at fixed：

$$
k
$$

must recurrently satisfy：

$$
\boxed{
\mathfrak G_k^{dir}>1
}
$$

或：

$$
\boxed{
\mathsf T_k=0.
}
$$

---

# 47. Direct gate removes two old labels

對 Theorem 3.5 route：

$$
\boxed{
\mathrm{SHELLFULL},
\mathrm{COMPSIGN}
}
$$

已被 full-field component-volume route bypass。

所以 C5-A derivative defect vector可對 fixed direct route更新：

$$
\boxed{
d_k^{dir}
=
(
\mathrm{MULT},
\mathrm{TIME}
).
}
$$

### Chain route separate

Theorem 3.14仍有：

- chain；
- all-order synchronization；
- later analytic timing；

額外 hypotheses。

所以：

$$
\boxed{
\text{TIMECHAIN}
}
$$

仍保留在 chain-assisted route。

---

# 48. Fixed-order closure audit

對任意 fixed：

$$
k,
$$

如果 recurrent escape time sequence中存在 subsequence，

每一代都有 admissible：

$$
s_j
$$

且：

$$
\boxed{
\limsup_j
\mathfrak G_k^{dir}(s_j)
\le1,
}
$$

則 sufficiently large：

$$
j
$$

Theorem 3.5 spatial gate關閉，

contradicting：

$$
T^\ast
$$

being first blow-up time。

所以 fixed-order survivor必保持：

$$
\boxed{
\liminf
\mathfrak G_k^{dir}>1
}
$$

along all admissible favorable subsequences，

或始終 time-mismatch。

---

# 49. Pressure-signature defect state

C5-F axis-pressure metadata更新為：

$$
\boxed{
\Theta_\ast^P
=
\left\langle
\widehat F_\ast,
\operatorname{sig}F_\ast,
d_{\rm sig,\ast},
c_\ast^P,
\nu_\ast^{axis},
\mathsf H_\ast^P
\right\rangle.
}
$$

其中：

- $d_{\rm sig}$ = distance to det-zero boundary；
- $c^P$ = pressure-axis margin；
- $\mathsf H^P$ = far-matrix heredity status。

---

# 50. Vorticity-pressure defect state

定義：

$$
\boxed{
\Theta_\ast^{V/P}
=
\left\langle
\mathfrak W_\ast,
\mathfrak P_{\Delta,+},
\|C_\omega\|,
\|\nabla^2p\|,
\|C_A\|,
\|C_S\|
\right\rangle.
}
$$

它保存：

- vorticity leakage stock；
- positive pressure-Poisson curvature；
- vorticity constraint complement；
- actual pressure Hessian；
- competing complement channels。

---

# 51. C5-G residual compression

C5-F residual：

$$
\text{Pressure Signature}
\vee
\text{Vorticity Complement}
\vee
\text{Fixed-Order Gate}
\vee
k\to\infty.
$$

C5-G後：

## Pressure signature

$$
\boxed{
\text{Fixed Signature}
\vee
\text{Signature-Boundary Defect}
\vee
\text{Pressure Turnover/Fragmentation}.
}
$$

## Vorticity complement

$$
\boxed{
\text{Pressure-Poisson Activity}
+
\left(
\text{Pressure Hessian}
\vee
\text{Advection Complement}
\vee
\text{Strain-Square Complement}
\right).
}
$$

## Fixed order

$$
\boxed{
\text{Effective-Volume Defect}
\vee
\text{Later-Time Defect}.
}
$$

---

# 52. What is now genuinely theorem-ready?

The following statement is no longer a pre-gate：

> At a Grujić–Xu Theorem 3.5 admissible later time $s$,
> if:
> $$
> \mathfrak G_k^{dir}(s)\le1,
> $$
> then regularity follows past $T^\ast$.

This uses exactly：

- full $D^ku$；
- selected component/sign superlevel sets；
- 1D sparseness；
- published theorem scale；
- theorem later-time window。

所以：

$$
\boxed{
\textbf{C5-G has a genuine theorem-ready fixed-order closure interface}.
}
$$

---

# 53. What remains non-theorem-ready?

Middle-gap strain active volume：

$$
E_c(S)
$$

itself仍不是 Theorem 3.5 superlevel set。

Vorticity pressure-Poisson stock也不是 Grujić–Xu gate。

Pressure axis geometry也不是 standalone regularity theorem。

所以 C5-G只宣稱：

$$
\boxed{
\textbf{one direct fixed-order route is theorem-ready}.
}
$$

---

# 54. Can k=1 now solve the route?

Not yet。

Hypothetical survivor can keep：

$$
\boxed{
\mathfrak G_1^{dir}>1
}
$$

by making：

$$
\|S\|_2
$$

grow sufficiently rapidly relative to：

$$
\|Du\|_\infty.
$$

This is：

$$
\boxed{
\textbf{Diffuse-Enstrophy / Insufficient-Peak-Concentration Defect}.
}
$$

No existing finite budget excludes this near hypothetical blow-up。

---

# 55. Can fixed k=2 solve the route?

Not yet。

C5-F gives critical：

$$
D^2u
$$

amplitude somewhere，

but the $L^2$ derivative stock can grow comparably or faster，

keeping：

$$
\mathfrak G_2^{dir}>1.
$$

所以：

$$
\boxed{
\text{amplitude stock}
\neq
\text{effective-volume concentration}.
}
$$

仍是核心 distinction。

---

# 56. Derivative escalation logic after C5-G

對 fixed：

$$
k,
$$

survivor defect只有：

$$
\mathrm{MULT}
\vee
\mathrm{TIME}.
$$

因此全 C5 derivative route可寫：

$$
\boxed{
\text{some fixed }k\text{ closes}
}
$$

or：

$$
\boxed{
\forall\text{ fixed }k,
\quad
\mathrm{MULT}_k
\vee
\mathrm{TIME}_k
\text{ recurrent}.
}
$$

只有第二情況下，

再研究：

$$
\boxed{
k\to\infty
}
$$

是否能將 these defects壓到 incompatibility。

---

# 57. Relation to asymptotic criticality

Grujić–Xu Theorem 3.14的 scale：

$$
\|D^ku\|_\infty^{-1/(k+1)}
$$

與 a-priori scale差隨：

$$
k\to\infty
$$

消失。

但 C5-G揭示另一個 dimension：

$$
\boxed{
\textbf{effective derivative volume}
}
$$

也必跟著 compatible。

所以 high-$k$ asymptotic criticality若要真正閉合 C5 survivor，

還要研究：

$$
\boxed{
\mathfrak G_k^{dir},
\quad
\mathrm{MULT}_k,
\quad
\mathrm{TIMECHAIN}_k
}
$$

是否可同時在：

$$
k\to\infty
$$

保持 failure。

---

# 58. Major no-go audit

### NG-G1

$$
\text{middle-gap strain sparseness}
\Rightarrow
\text{Theorem 3.5}.
$$

FALSE by itself。

### NG-G2

$$
\text{component/sign conversion remains an unavoidable fixed-}k\text{ defect}.
$$

FALSE for C5-G direct-volume route。

### NG-G3

$$
\text{shell/full conversion remains unavoidable}.
$$

FALSE for C5-G direct-volume route。

### NG-G4

$$
\text{vorticity-dominant leakage}
\Rightarrow
L^{3/2}\text{ pressure concentration}.
$$

NOT PROVED。

It gives pressure-Poisson curvature first。

### NG-G5

$$
P_{st}^{\perp}(\omega\otimes\omega)
=
\nabla^2p.
$$

FALSE。

### NG-G6

$$
\text{pressure signature switching}
\Rightarrow
\det F\to0.
$$

Only under strong hereditary closeness。

Otherwise pressure turnover/fragmentation is legal。

### NG-G7

$$
\text{fixed-order direct defect failure}
\Rightarrow
k\to\infty.
$$

FALSE unless all fixed-order recurrent defects are excluded。

---

# 59. X-Integration guards 更新

## G-DIRECTFULL

fixed-order direct gate優先使用 full：

$$
D^ku
$$

component/sign high set，

避免不必要 shell/strain conversion。

## G-EFFVOLK

保存：

$$
V_k^{eff}
=
\|D^ku\|_2^2/\|D^ku\|_\infty^2.
$$

## G-GXRATIO

theorem-ready gate保存：

$$
\mathfrak G_k^{dir}
=
r_{vol,k}/r_{GX,k}.
$$

## G-GXTIME

$\mathfrak G_k^{dir}\le1$只有在 Theorem 3.5 admissible later time才可閉 gate。

## G-PSIGBOUND

signature switching只有和 heredity closeness聯用才能推出 det-zero boundary。

## G-PPOIS

vorticity-dominant leakage先記：

$$
(\Delta p)_+
$$

而不是直接 $L^{3/2}$ pressure。

## G-PCOMPLEDGER

vorticity constraint complement必和 actual pressure / advection / $S^2$ complement聯帳。

---

# 60. True ETN 更新

C5-G derivative state：

$$
\boxed{
\Theta_\ast^{DG}
=
\left\langle
k,
A_k,
L_k,
V_k^{eff},
r_{vol,k},
r_{GX,k},
\mathfrak G_k^{dir},
\mathsf T_k
\right\rangle.
}
$$

pressure state：

$$
\boxed{
\Theta_\ast^{PS}
=
\left\langle
\widehat F,
\operatorname{sig}F,
d_{\rm sig},
\mathsf H^P,
\nu^{axis}
\right\rangle.
}
$$

vorticity-pressure state：

$$
\boxed{
\Theta_\ast^{VP}
=
\left\langle
\mathfrak W_R,
\mathfrak P_{\Delta,+},
C_\omega,
\nabla^2p,
C_A,
C_S
\right\rangle.
}
$$

---

# 61. C5 strategic status

C5-A：

$$
\text{motif compactness}.
$$

C5-B：

$$
\text{temporal oscillation/concentration}.
$$

C5-C：

$$
\text{temporal transition curvature}.
$$

C5-D：

$$
\text{first spatial–matrix incompatibility}.
$$

C5-E：

$$
Q\to\text{gap/derivative/vorticity defects}.
$$

C5-F：

$$
\text{axis/pressure signature + derivative escalation}.
$$

C5-G：

$$
\boxed{
\textbf{fixed-order direct derivative gate becomes theorem-ready};
}
$$

同時：

$$
\boxed{
\textbf{pressure signature and vorticity complement become compact,
routed defects rather than free escapes}.
}
$$

---

# 62. What remains most important

現在真正值得打的 fixed-order問題不再是 geometry怎麼轉：

而是：

$$
\boxed{
\textbf{Can a hypothetical blow-up keep }
\mathfrak G_k^{dir}>1
\textbf{ for every fixed }k
\textbf{ at every admissible later time?}
}
$$

這是：

$$
\boxed{
\textbf{All-Order Effective-Volume Defect Problem}.
}
$$

如果答案否，

某 fixed $k$ direct gate就關。

如果答案是，

則 survivor必在所有 derivative levels保持：

$$
\boxed{
\text{L}^2\text{ derivative mass sufficiently diffuse relative to peaks}.
}
$$

這已經是一個高度結構化的 all-order constraint。

---

# 63. 新 frontier：C5-H

正式下一題：

$$
\boxed{
\textbf{C5-H — All-Order Effective-Volume Defects,
Derivative Concentration Ladders, and Asymptotic-Critical Compatibility}.
}
$$

---

# 64. C5-H proof obligations

## H1 — All-order direct gate ratios

研究：

$$
\boxed{
\mathfrak G_k^{dir}
}
$$

隨：

$$
k
$$

的 relation，

能否所有 fixed $k$ simultaneously保持：

$$
>1.
$$

## H2 — Derivative interpolation

利用 Gagliardo–Nirenberg / log-convexity，

把：

$$
L_k,
\quad
A_k
$$

across derivative levels聯立。

## H3 — Effective-volume ladder

定義：

$$
\boxed{
V_k^{eff}
=
L_k^2/A_k^2
}
$$

並研究：

$$
V_{k+1}^{eff}/V_k^{eff}.
$$

## H4 — Fixed-order defect inheritance

若：

$$
\mathfrak G_k^{dir}>1
$$

and：

$$
\mathfrak G_{k+1}^{dir}>1,
$$

是否強迫某 derivative-chain monotonicity / multiplicity structure？

## H5 — Time-gate synchronization

不同：

$$
k
$$

的 Theorem 3.5 admissible later windows能否沿 C5 record ladder共同抽取？

## H6 — Link to Theorem 3.14

若 all fixed direct gates fail，

測是否這本身產生 Theorem 3.14 所需的 ascending/descending derivative chain。

## H7 — High-k compactification

對：

$$
k\to\infty,
$$

compactify：

$$
\mathfrak G_k^{dir},
\quad
V_k^{eff},
\quad
A_k^{1/(k+1)},
\quad
L_k^{1/k}.
$$

## H8 — Asymptotic compatibility contradiction

尋找：

$$
\boxed{
\text{all-order diffuse derivative mass}
}
$$

與：

$$
\boxed{
\text{asymptotically-critical chain geometry}
}
$$

是否 incompatibility。

---

# 65. 正式狀態

$$
\boxed{
\begin{aligned}
\text{component/sign global-volume bound}
&:\ \mathrm{PROVED},\\
\text{volume-to-line fixed-}k\text{ sparseness}
&:\ \mathrm{PROVED},\\
\mathfrak G_k^{dir}\le1
\text{ at admissible time}
\Rightarrow
\text{Theorem 3.5 closure}
&:\ \mathrm{PROVED},\\
\text{fixed-}k\ \mathrm{COMPSIGN}
&:\ \mathrm{BYPASSED},\\
\text{fixed-}k\ \mathrm{SHELLFULL}
&:\ \mathrm{BYPASSED},\\
\text{fixed-order residual}
&:\ \mathrm{MULT}\vee\mathrm{TIME},\\
\text{pressure signature boundary compactification}
&:\ \mathrm{DEFINED/PROVED},\\
\text{signature switching + heredity}
\Rightarrow
d_{\rm sig}\to0
&:\ \mathrm{PROVED},\\
\text{vorticity-dominant leakage}
\Rightarrow
(\Delta p)_+
&:\ \mathrm{PROVED},\\
\text{constraint-complement pressure ledger}
&:\ \mathrm{PROVED},\\
\text{vorticity complement trichotomy}
&:\ \mathrm{PROVED},\\
\text{all fixed }k\text{ direct gates cannot all fail}
&:\ \mathrm{OPEN},\\
\text{global regularity}
&:\ \mathrm{OPEN}.
\end{aligned}
}
$$

---

# 66. 結論

C5-F留下：

$$
\text{Pressure Signature}
\vee
\text{Vorticity Complement}
\vee
\text{Fixed-Order Gate}
\vee
k\to\infty.
$$

C5-G現在真正把 fixed-order route接到 published theorem。

對任意：

$$
k\ge1,
$$

selected：

$$
D^ku
$$

component/sign high set直接滿足：

$$
\boxed{
|V_{\lambda,k}|
\lesssim
\frac{
\|D^ku\|_2^2
}{
\|D^ku\|_\infty^2
}.
}
$$

所以：

$$
\boxed{
r_{vol,k}
\lesssim
\|D^ku\|_2^{2/3}
\|D^ku\|_\infty^{-2/3}.
}
$$

而 published Theorem 3.5 direct target：

$$
\boxed{
r_{GX,k}
=
\frac1{
2^kc(M)
\|D^ku\|_\infty^{3/(2k+3)}
}.
}
$$

因此在 theorem-admissible later time：

$$
\boxed{
\mathfrak G_k^{dir}
=
r_{vol,k}/r_{GX,k}
\le1
}
$$

就真正關 gate。

這不是 pre-gate。

它已經是：

$$
\boxed{
\textbf{theorem-ready fixed-order closure}.
}
$$

所以 fixed direct route的 old defects：

$$
\mathrm{SHELLFULL},
\quad
\mathrm{COMPSIGN}
$$

可以旁路。

真正只剩：

$$
\boxed{
\text{Effective-Volume Diffuseness}
\vee
\text{Later-Time Mismatch}.
}
$$

Pressure方面，

common far matrix signature若在 strong heredity下反覆切換，

就必逼：

$$
\boxed{
\det F\to0.
}
$$

否則必支付 pressure turnover / source fragmentation。

Vorticity方面，

dominant leakage直接給：

$$
\boxed{
\Delta p>0
}
$$

on the same leakage set，

而 strain-space complement又 exact滿足：

$$
\boxed{
\nabla^2p
=
-
(
C_A+C_S+C_\omega
).
}
$$

所以 vorticity complement必：

$$
\boxed{
\text{Pressure Hessian}
\vee
\text{Advection Complement}
\vee
\text{Strain-Square Complement}.
}
$$

因此 C5-G 後最硬的新問題已經非常清楚：

> **一個 hypothetical singular survivor，
> 能不能在所有 fixed derivative orders，
> 都讓 $D^ku$ 的 $L^2$ mass相對 $L^\infty$ peak保持足夠 diffuse，
> 使 $\mathfrak G_k^{dir}>1$，
> 同時又避開每個 Theorem 3.5 admissible later time？**

正式下一篇：

$$
\boxed{
\textbf{C5-H — All-Order Effective-Volume Defects,
Derivative Concentration Ladders, and Asymptotic-Critical Compatibility}.
}
$$

---

# References

1. Z. Grujić, L. Xu, *Asymptotic Criticality of the Navier–Stokes Regularity Problem*, Journal of Mathematical Fluid Mechanics 26, Article 53 (2024), DOI: 10.1007/s00021-024-00888-x; arXiv:1911.00974.
2. E. Miller, E. Sawyer, *A Helmholtz-type decomposition for the space of symmetric matrices*, arXiv:2111.12891.
3. E. Miller, *On the interaction of strain and vorticity for solutions of the Navier–Stokes equation*, arXiv:2407.02691v2; Pure and Applied Analysis 8 (2026).
4. Z. Bradshaw, T.-P. Tsai, *On the local pressure expansion for the Navier–Stokes equations*, arXiv:2001.11526.
5. E. Miller, *A regularity criterion for the Navier–Stokes equation involving only the middle eigenvalue of the strain tensor*, arXiv:1710.05569.

# Internal dependencies

- `NS_C5F_AxisPressureSignature_DerivativeGateEscalation_v0.1.md`
- `NS_C5E_StrainDirection_MiddleGap_DerivativeIntermittency_v0.1.md`
- `NS_C5D_SpatialMatrix_StrongMiddleQuadraticPressureObstruction_v0.1.md`
- `NS_C5C_TemporalCorrelation_CrossCurvatureOrdering_v0.1.md`
- `NS_C5B_TemporalYoung_PulsePhaseCompatibility_v0.1.md`
- `NS_C5A_RecordWindow_MotifCompactness_v0.1.md`
- `NS_C4J_CompensationRigidity_FinalSynchronizationAudit_v0.1.md`
- `NS_C3U_PressureHeredity_MeanPointwiseRigidity_v0.1.md`
- `NS_C3Y_DerivativeChain_IntermittencyTradeoff_v0.1.md`
- `True ETN / 無限維張力場`
- `X_Integral_Unified_Program_v0.2.md`

Next:

$$
\boxed{
\textbf{C5-H — All-Order Effective-Volume Defects,
Derivative Concentration Ladders, and Asymptotic-Critical Compatibility}
}
$$
