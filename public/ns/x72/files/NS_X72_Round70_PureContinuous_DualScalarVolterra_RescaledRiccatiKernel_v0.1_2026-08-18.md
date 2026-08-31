# NS × X 積分 × 24/72 範式實戰
## Round 70 — Pure Continuous Dual Scalar Volterra Kernel / Parity-Rescaled Riccati Sensitivity

- 日期：2026-08-18
- 版本：v0.1
- 狀態：Proof-Route Experiment / Continuous-Only Dual Scalar Jost-Kernel Branch
- 前一輪：Round 69 — Rank-One Scattering Tangent / Affine Endpoint Repair
- canonical math delimiters：inline `$...$`；display `$$...$$`

## 0. 核心結論

Round 69 將 endpoint first-order Grassmann motion壓成一個 rank-one scattering freedom。

Round 70 再往下做一層：在 parity-rescaled consecutive Riccati chart 中，**每一個 local viscosity tangent source本身精確 rank-one，而每一個中央 scalar observable 的 dual weight也精確保持 rank-one**。

所以最終 sensitivity 已不是「$3\times3$ tangent matrix 裡藏著一個 scalar」，而是直接成為：

$$
\boxed{
\text{scalar Jost kernel sum}
+
\text{one terminal pairing}.
}
$$

---

# 1. Parity-rescaled consecutive variable

定義：

$$
\boxed{
r_n=
\begin{cases}
u_n,&n\ {\rm even},\\
u_n/\nu,&n\ {\rm odd}.
\end{cases}
}
$$

以及：

$$
\boxed{
Z_n=
(r_{n+3},r_{n+2},r_{n+1},r_n,r_{n-1},r_{n-2})^T.
}
$$

這是 Round 66 consecutive state 的 diagonal parity rescaling。

---

# 2. Local viscosity dependence collapses

在 $r_n$ 變數下：

### odd $n$

$$
\boxed{
r_{n+4}
=
\frac{
A_{-2}r_{n-2}
-
A_0r_n
+
b_nr_{n+1}
+
A_2r_{n+2}
}{
A_4
}.
}
$$

完全不含 $\nu$。

### even $n$

$$
\boxed{
r_{n+4}
=
\frac{
A_{-2}r_{n-2}
-
A_0r_n
+
\nu^2b_nr_{n+1}
+
A_2r_{n+2}
}{
A_4
}.
}
$$

因此：

$$
\boxed{
T_n(\nu)=T_n(0)+\nu^2E_n
\quad(n\ {\rm even}),
}
$$

$$
\boxed{
T_n(\nu)=T_n(0)
\quad(n\ {\rm odd}).
}
$$

---

# 3. Central observables are order one

在 $n=1$：

$$
Z_1^-=(0,1,0)^T.
$$

若：

$$
Z_1^+=R_1Z_1^-,
$$

則：

$$
\boxed{
e_1=u_2=(R_1)_{32},
}
$$

$$
\boxed{
f(\nu)=\frac{a_3(\nu)}{\nu}=-(R_1)_{22}.
}
$$

以及：

$$
\boxed{
o_2=\frac{u_5}{\nu}
=
\frac{
b_1e_1-A_2^{(1)}f
}{
A_4^{(1)}
}.
}
$$

Round 68 的 central-cone quantities 因而全是 $O(1)$ graph readouts。

---

# 4. Riccati tangent

將 transfer block 成：

$$
T_n=
\begin{pmatrix}
A_n&B_n\\
C_n&D_n
\end{pmatrix}.
$$

令：

$$
X_n=R_{n+1}C_n-A_n,
$$

$$
Y_n=C_nR_n+D_n.
$$

則：

$$
R_n=X_n^{-1}(B_n-R_{n+1}D_n).
$$

ordinary viscosity tangent：

$$
H_n:=\partial_\nu R_n
$$

滿足：

$$
\boxed{
H_n
=
S_n
-
X_n^{-1}H_{n+1}Y_n.
}
$$

---

# 5. Rank-One Local Viscosity Source Theorem

odd layer：

$$
\boxed{S_n=0.}
$$

even layer只有一個 transfer entry 微分非零：

$$
\dot\beta_n
=
2\nu
\frac{b_n}{A_4^{(n)}}.
$$

因此：

$$
A_n'=\dot\beta_n e_1e_3^T,
$$

並且：

$$
\boxed{
S_n
=
\dot\beta_n
\left(X_n^{-1}e_1\right)
\left(e_3^TR_n\right).
}
$$

所以：

$$
\boxed{
\operatorname{rank}S_n\le1.
}
$$

對每個 $\nu>0$ 都是 exact。

---

# 6. Dual scalar Volterra identity

對中央 scalar functional：

$$
\ell(H_1)=\langle W_1,H_1\rangle_F,
$$

定義：

$$
\boxed{
W_{n+1}
=
-X_n^{-T}W_nY_n^T.
}
$$

得到 finite-$J$ exact identity：

$$
\boxed{
\ell(H_1)
=
\sum_{n=1}^{J}
\langle W_n,S_n\rangle_F
+
\langle W_{J+1},H_{J+1}\rangle_F.
}
$$

最後一項就是唯一的 terminal Jost sensitivity。

---

# 7. Dual rank preservation

若：

$$
W_1=p_1q_1^T,
$$

則：

$$
\boxed{
p_{n+1}=-X_n^{-T}p_n,
}
$$

$$
\boxed{
q_{n+1}=Y_nq_n,
}
$$

因此：

$$
\boxed{
W_n=p_nq_n^T.
}
$$

中央 entry derivative只需兩個三向量加一個 scalar accumulator。

---

# 8. Dual Rank-One Scattering Kernel

寫：

$$
S_n=\dot\beta_nx_nr_n^T,
$$

其中：

$$
x_n=X_n^{-1}e_1,
$$

$$
r_n^T=e_3^TR_n.
$$

則：

$$
\boxed{
\langle W_n,S_n\rangle_F
=
\dot\beta_n
(p_n^Tx_n)
(q_n^Tr_n).
}
$$

這就是 exact scalar Jost kernel。

命名：

$$
\boxed{
\textbf{Dual Rank-One Scattering Kernel}.
}
$$

---

# 9. Central scalar channels

### $e_1'$

取：

$$
W_1^{(e)}=E_{32}.
$$

### $f'$

取：

$$
W_1^{(f)}=-E_{22}.
$$

### $o_2'$

由：

$$
o_2'
=
\frac{
b_1e_1'-A_2^{(1)}f'
}{
A_4^{(1)}
},
$$

所以只需前兩條 rank-one channel 的線性組合。

---

# 10. Scalar-kernel diagnostics

verifier 在：

$$
10^{-8}\le\nu\le10^{-6}
$$

計算 finite-$J$ local source sums。

### Small fibre

$$
\boxed{
\sum|\kappa_n^{(e)}|<1.50,
}
$$

$$
\boxed{
\sum|\kappa_n^{(f)}|<10.20,
}
$$

$$
\boxed{
\sum|\kappa_n^{(o)}|<144.
}
$$

### Large fibre

$$
\boxed{
\sum|\kappa_n^{(e)}|<1.00,
}
$$

$$
\boxed{
\sum|\kappa_n^{(f)}|<3.60,
}
$$

$$
\boxed{
\sum|\kappa_n^{(o)}|<21.
}
$$

這些仍是 numerical diagnostics，不冒充 uniform theorem。

最小 viscosity 的 finite-$J$ terminal eigenspace derivative在 $f/o_2$ channel仍留下可見 remainder；CSV 用 `source_residual_*` 明確記錄，所以沒有把 source-only sum冒充 full derivative。

Round 68 真正需要的卻只是：

$$
|e_1'|<10^5,
$$

$$
|o_2'|<10^6.
$$

proof slack 仍有三至五個數量級。

---

# 11. Sign concentration

scalar decomposition顯示：

- small fibre 的 $o_2'$ resolved kernel幾乎呈單一負號；
- large fibre 除極少 early defects外，後段呈單一正號；
- $e_1'$ 同樣具有高度 sign concentration。

因此下一步除了 absolute summability，還可能走更強的 monotonicity route。

本輪不宣稱 uniform sign theorem。

---

# 12. Terminal pairing

唯一未被 local source sum吸收的是：

$$
\boxed{
\langle W_{J+1},H_{J+1}\rangle_F.
}
$$

Round 69 已有 deep-tail jet bound控制 $H_{J+1}$。

現在缺的是：

$$
W_{J+1}
$$

的 uniform decay。

所以最後 gap乾淨拆成：

$$
\boxed{
\text{scalar kernel summability}
+
\text{dual terminal-weight decay}.
}
$$

---

# 13. Final sufficient inequalities

Round 68 已證，只要：

$$
|e_1'|<10^5,
$$

$$
|o_2'|<10^6
$$

即可封閉最後 viscosity strip。

現在等價地只需：

$$
\boxed{
\sum_{n\ge1}
|\kappa_n^{(e)}|
+
|\mathrm{terminal}_e|
<
10^5,
}
$$

以及：

$$
\boxed{
\sum_{n\ge1}
|\kappa_n^{(o)}|
+
|\mathrm{terminal}_o|
<
10^6.
}
$$

實際 local source sums是 $O(1)$ 至 $O(10^2)$。

---

# 14. STOP-C74

$$
\boxed{
\textbf{
STOP-C74:
Dual Scalar Kernel Summability / Terminal-Weight Gap
}.
}
$$

$$
\boxed{
\begin{aligned}
\text{local tangent source rank}&\le1,\\
\text{dual channel rank}&=1,\\
\text{central derivative}
&=
\sum\text{ scalar kernel}
+
\text{terminal pairing},\\
\text{observed }e_1'\text{ local kernel}&=O(1),\\
\text{observed }o_2'\text{ local kernel}&=O(10^2),\\
\text{sufficient bounds}&=10^5,\ 10^6,\\
\text{remaining}
&=
\text{uniform scalar majorant + terminal dual decay},\\
T_{\mathsf C\to\mathsf D}&=\mathrm{NOT\ REACHED}.
\end{aligned}
}
$$

---

# 15. 24/72 Ledger — Round 70

| Step | object | $B$ | $U$ | $O$ | $L$ | status |
|---|---|---|---|---|---|---|
| C1099 | parity-rescaled consecutive state | $\mathsf C$ | Floquet coordinate | relational | $\mathsf F$ | EXACT |
| C1100 | odd-layer viscosity removal | $\mathsf C$ | local transfer | scalar | $\mathsf F$ | EXACT |
| C1101 | even-layer $\nu^2$ transfer | $\mathsf C$ | local transfer | scalar | $\mathsf F$ | EXACT |
| C1102 | order-one central readout | $\mathsf C$ | canonical observable | scalar | $\mathsf F$ | EXACT |
| C1103 | ordinary-viscosity Riccati tangent | $\mathsf C$ | graph flow | relational | $\mathsf F$ | EXACT |
| C1104 | rank-one local source | $\mathsf C$ | parameter injection | matrix | $\mathsf F$ | PROVED |
| C1105 | dual Volterra identity | $\mathsf C$ | adjoint graph flow | scalar | $\mathsf F$ | EXACT |
| C1106 | dual rank preservation | $\mathsf C$ | adjoint factorization | relational | $\mathsf F$ | PROVED |
| C1107 | scalar kernel factorization | $\mathsf C$ | Jost sensitivity | scalar | $\mathsf F$ | EXACT |
| C1108 | $e_1'$ scalar channel | $\mathsf C$ | central response | scalar | $\mathsf F$ | EXACT |
| C1109 | $f'$ scalar channel | $\mathsf C$ | central response | scalar | $\mathsf F$ | EXACT |
| C1110 | $o_2'$ two-channel reduction | $\mathsf C$ | central response | scalar | $\mathsf F$ | EXACT |
| C1111 | microscopic local-kernel diagnostics | $\mathsf C$ | kernel profile | profile | $\mathsf F$ | VERIFIED |
| C1112 | terminal dual decay | $\mathsf C$ | Jost tail | targeted | $\mathsf F$ | OPEN |
| C1113 | uniform scalar majorant | $\mathsf C$ | final viscosity bridge | targeted | $\mathsf F$ | OPEN / STOP-C74 |

---

# 16. Next round — Dual Kernel Majorant / Final Central-Cone Closure

下一輪只剩把 scalar kernel做 majorant：

1. 使用 exact factorization：
   $$
   \kappa_n
   =
   \dot\beta_n
   (p_n^TX_n^{-1}e_1)
   (q_n^TR_n^Te_3);
   $$
2. center / transition / deep-tail 三區分割；
3. center 用固定有限 interval bound；
4. transition 用 Round 63 fast-Schur 與 Round 60 WKB scale；
5. deep-tail 用 Round 69 jet contraction；
6. 證 terminal dual weight幾何衰減；
7. 只求：
   $$
   \sum|\kappa^{(e)}|<10^5,
   $$
   $$
   \sum|\kappa^{(o)}|<10^6;
   $$
8. 成功後套 Round 68 Central Sign-Cone Lemma：
   $$
   a_{3,\pm}(\nu)>0
   \quad
   \forall\nu>0.
   $$

---

# 17. External primary-source anchors

Fresh primary-source check：

1. Pierre Del Moral，Emma Horton，*A note on Riccati matrix difference equations*，arXiv:2107.12918.
2. F. Battelli，M. Franca，K. J. Palmer，*Exponential Dichotomy for Noninvertible Linear Difference Equations*，arXiv:2111.04553.
3. Yuri Latushkin，Shibi Vasudevan，*Fredholm determinants, continued fractions, Jost and Evans functions for a Jacobi matrix associated with the 2D-Euler equations*，arXiv:2401.14037.

這些只作 Riccati / dichotomy / hydrodynamic-Jost framework anchors；Round 70 的 parity rescaling、rank-one source與 dual scalar kernel均為本系列直接推導。
