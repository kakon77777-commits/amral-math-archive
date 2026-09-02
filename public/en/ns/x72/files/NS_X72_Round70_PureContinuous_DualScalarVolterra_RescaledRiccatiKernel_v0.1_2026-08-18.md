# NS × X Integral × 24/72 Paradigm Practice
## Round 70 — Pure Continuous Dual Scalar Volterra Kernel / Parity-Rescaled Riccati Sensitivity

- Date: 2026-08-18
- Version: v0.1
- Status: Proof-Route Experiment / Continuous-Only Dual Scalar Jost-Kernel Branch
- Previous Round: Round 69 — Rank-One Scattering Tangent / Affine Endpoint Repair
- canonical math delimiters: inline `$...$`; display `$$...$$`

## 0. Core Conclusions

Round 69 compressed the endpoint first-order Grassmann motion into a rank-one scattering freedom.

Round 70 goes one layer deeper: in the parity-rescaled consecutive Riccati chart, **each local viscosity tangent source itself is exactly rank-one, and the dual weight of each central scalar observable also exactly preserves rank-one**.

Therefore, the final sensitivity is no longer "a scalar hidden inside a $3\times3$ tangent matrix", but directly becomes:

$$
\boxed{
\text{scalar Jost kernel sum}
+
\text{one terminal pairing}.
}
$$

---

# 1. Parity-rescaled consecutive variable

Definition:

$$
\boxed{
r_n=
\begin{cases}
u_n,&n\ {\rm even},\\
u_n/\nu,&n\ {\rm odd}.
\end{cases}
}
$$

and:

$$
\boxed{
Z_n=
(r_{n+3},r_{n+2},r_{n+1},r_n,r_{n-1},r_{n-2})^T.
}
$$

This is the diagonal parity rescaling of the consecutive state from Round 66.

---

# 2. Local viscosity dependence collapses

Under the $r_n$ variables:

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

It is completely independent of $\nu$.

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

Therefore:

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

At $n=1$:

$$
Z_1^-=(0,1,0)^T.
$$

If:

$$
Z_1^+=R_1Z_1^-,
$$

then:

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

and:

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

The central-cone quantities from Round 68 are thus all $O(1)$ graph readouts.

---

# 4. Riccati tangent

Block the transfer matrix as:

$$
T_n=
\begin{pmatrix}
A_n&B_n\\
C_n&D_n
\end{pmatrix}.
$$

Let:

$$
X_n=R_{n+1}C_n-A_n,
$$

$$
Y_n=C_nR_n+D_n.
$$

Then:

$$
R_n=X_n^{-1}(B_n-R_{n+1}D_n).
$$

The ordinary viscosity tangent:

$$
H_n:=\partial_\nu R_n
$$

satisfies:

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

For odd layers:

$$
\boxed{S_n=0.}
$$

For even layers, only one transfer entry has a non-zero derivative:

$$
\dot\beta_n
=
2\nu
\frac{b_n}{A_4^{(n)}}.
$$

Therefore:

$$
A_n'=\dot\beta_n e_1e_3^T,
$$

and:

$$
\boxed{
S_n
=
\dot\beta_n
\left(X_n^{-1}e_1\right)
\left(e_3^TR_n\right).
}
$$

Thus:

$$
\boxed{
\operatorname{rank}S_n\le1.
}
$$

This is exact for every $\nu>0$.

---

# 6. Dual scalar Volterra identity

For the central scalar functional:

$$
\ell(H_1)=\langle W_1,H_1\rangle_F,
$$

define:

$$
\boxed{
W_{n+1}
=
-X_n^{-T}W_nY_n^T.
}
$$

We obtain the finite-$J$ exact identity:

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

The last term is the unique terminal Jost sensitivity.

---

# 7. Dual rank preservation

If:

$$
W_1=p_1q_1^T,
$$

then:

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

Therefore:

$$
\boxed{
W_n=p_nq_n^T.
}
$$

The central entry derivative only requires two 3-vectors plus a scalar accumulator.

---

# 8. Dual Rank-One Scattering Kernel

Write:

$$
S_n=\dot\beta_nx_nr_n^T,
$$

where:

$$
x_n=X_n^{-1}e_1,
$$

$$
r_n^T=e_3^TR_n.
$$

Then:

$$
\boxed{
\langle W_n,S_n\rangle_F
=
\dot\beta_n
(p_n^Tx_n)
(q_n^Tr_n).
}
$$

This is the exact scalar Jost kernel.

Named:

$$
\boxed{
\textbf{Dual Rank-One Scattering Kernel}.
}
$$

---

# 9. Central scalar channels

### $e_1'$

Take:

$$
W_1^{(e)}=E_{32}.
$$

### $f'$

Take:

$$
W_1^{(f)}=-E_{22}.
$$

### $o_2'$

From:

$$
o_2'
=
\frac{
b_1e_1'-A_2^{(1)}f'
}{
A_4^{(1)}
},
$$

thus it only requires a linear combination of the first two rank-one channels.

---

# 10. Scalar-kernel diagnostics

The verifier computes the finite-$J$ local source sums in:

$$
10^{-8}\le\nu\le10^{-6}
$$

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

These remain numerical diagnostics and do not masquerade as a uniform theorem.

The finite-$J$ terminal eigenspace derivative at the minimum viscosity still leaves a visible remainder in the $f/o_2$ channel; the CSV explicitly records this using `source_residual_*`, so the source-only sum is not masquerading as the full derivative.

What Round 68 actually requires is merely:

$$
|e_1'|<10^5,
$$

$$
|o_2'|<10^6.
$$

There are still three to five orders of magnitude of proof slack.

---

# 11. Sign concentration

The scalar decomposition shows:

- the resolved kernel for $o_2'$ in the small fibre exhibits an almost uniform negative sign;
- the large fibre, apart from very few early defects, exhibits a uniform positive sign in the later stages;
- $e_1'$ similarly possesses a high degree of sign concentration.

Therefore, the next step, in addition to absolute summability, may also pursue a stronger monotonicity route.

This round does not claim a uniform sign theorem.

---

# 12. Terminal pairing

The only term not absorbed by the local source sum is:

$$
\boxed{
\langle W_{J+1},H_{J+1}\rangle_F.
}
$$

Round 69 already has a deep-tail jet bound to control $H_{J+1}$.

What is currently missing is the uniform decay of:

$$
W_{J+1}
$$

Thus, the final gap is cleanly split into:

$$
\boxed{
\text{scalar kernel summability}
+
\text{dual terminal-weight decay}.
}
$$

---

# 13. Final sufficient inequalities

Round 68 has proved that as long as:

$$
|e_1'|<10^5,
$$

$$
|o_2'|<10^6
$$

the final viscosity strip can be closed.

Now, equivalently, we only need:

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

and:

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

The actual local source sums are $O(1)$ to $O(10^2)$.

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

The next round only remains to establish a majorant for the scalar kernel:

1. Use the exact factorization:
   $$
   \kappa_n
   =
   \dot\beta_n
   (p_n^TX_n^{-1}e_1)
   (q_n^TR_n^Te_3);
   $$
2. Partition into three regions: center / transition / deep-tail;
3. Use a fixed finite interval bound for the center;
4. Use the Round 63 fast-Schur and Round 60 WKB scale for the transition;
5. Use the Round 69 jet contraction for the deep-tail;
6. Prove the geometric decay of the terminal dual weight;
7. Only require:
   $$
   \sum|\kappa^{(e)}|<10^5,
   $$
   $$
   \sum|\kappa^{(o)}|<10^6;
   $$
8. Upon success, apply the Round 68 Central Sign-Cone Lemma:
   $$
   a_{3,\pm}(\nu)>0
   \quad
   \forall\nu>0.
   $$

---

# 17. External primary-source anchors

Fresh primary-source check:

1. Pierre Del Moral, Emma Horton, *A note on Riccati matrix difference equations*, arXiv:2107.12918.
2. F. Battelli, M. Franca, K. J. Palmer, *Exponential Dichotomy for Noninvertible Linear Difference Equations*, arXiv:2111.04553.
3. Yuri Latushkin, Shibi Vasudevan, *Fredholm determinants, continued fractions, Jost and Evans functions for a Jacobi matrix associated with the 2D-Euler equations*, arXiv:2401.14037.

These serve only as anchors for the Riccati / dichotomy / hydrodynamic-Jost framework; the parity rescaling, rank-one source, and dual scalar kernel in Round 70 are all directly derived within this series.