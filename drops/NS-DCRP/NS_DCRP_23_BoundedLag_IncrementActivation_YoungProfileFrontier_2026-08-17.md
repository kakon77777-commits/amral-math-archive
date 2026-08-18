# NS-DCRP-23 — Bounded-Lag Increment Activation, Descendant Coarse Decay, and the Young-Profile Frontier

- date: 2026-08-17
- status: research proof checkpoint
- canonical source: UTF-8 Markdown
- canonical math delimiters: `$...$` and `$$...$$`
- objective:
  1. audit whether DCRP-22's proposed "untaxed critical supply -> bounded-lag supplier" is actually the correct density bridge;
  2. separate absolute transition-supply bookkeeping from genuine small-scale roughness;
  3. prove a bounded-lag regularity theorem driven directly by a scale-critical velocity-increment defect;
  4. reduce a persistent bounded-reservoir non-CKN branch to a nonvanishing derivative-compatible increment profile at every sufficiently small scale.
- no full Navier--Stokes regularity claim is made.
- principal external primary sources:
  - Runlong Yu, *Finite-Window Singularity Audits and Local-to-Clean Defect Transfer for Navier-Stokes*, arXiv:2606.15086v1;
  - Runlong Yu, *Filtered Vortex Stretching and Subgrid Defects for the Three-Dimensional Navier--Stokes Equations*, arXiv:2606.27560v1.
- supporting primary source:
  - Cheskidov--Dai, arXiv:1507.06611v6.
- internal dependencies:
  - DCRP-19 through DCRP-22;
  - MORP compact normalized obstruction architecture.
- no novelty/priority claim is made without independent audit.

---

# 1. Executive result

DCRP-22 proposed the next bridge:

$$
\boxed{
\text{untaxed critical supply}
\Longrightarrow
\text{bounded-lag local supplier}.
}
\tag{1.1}
$$

A source audit shows that this is not the cleanest theorem to attack.

The unconditional finite-scale ledger defines:

$$
\boxed{
\Phi_k^{\rm flux}
=
r_k^{-1}
\iint_{Q_k}
|u|^2
|
u\cdot\nabla\phi_k
|
dxdt,
}
\tag{1.2}
$$

and:

$$
\boxed{
\Pi_k^{\rm press}
=
r_k^{-1}
\iint_{Q_k}
|
p-(p)_{B_{r_k}}
|
|
u\cdot\nabla\phi_k
|
dxdt.
}
\tag{1.3}
$$

These are **absolute transition magnitudes**.

They are intentionally robust for the one-sided local energy ledger, but they do not retain the sign/cancellation structure needed to identify a unique causal cascade mechanism.

Therefore:

$$
\boxed{
\textbf{
large }\mathrm{Sup}^{full}
\textbf{ is not, by definition alone, a frequency-local supplier statement}.
}
\tag{1.4}
$$

A bounded-lag supplier theorem cannot be deduced purely from the algebra of the full ledger.

The present round bypasses this issue.

Fix a parent cylinder:

$$
Q_r(z_0),
$$

a fixed relative smoothing length:

$$
\ell=\sigma r,
\qquad
0<\sigma<\sigma_0,
$$

and the spatially filtered field:

$$
\boxed{
U_\ell
=
S_\ell u.
}
\tag{1.5}
$$

Write:

$$
\boxed{
w_\ell
=
u-U_\ell.
}
\tag{1.6}
$$

The smooth coarse part and the unresolved increment part obey two opposite scaling laws on a descendant cylinder:

$$
r_m
=
\theta^m r.
$$

If the enlarged parent local energy is bounded:

$$
\boxed{
A_{r,\sigma}^{+}
\le
M,
}
\tag{1.7}
$$

then:

$$
\boxed{
C_{U_\ell}(r_m)
\le
C_\sigma
M^{3/2}
\theta^{3m}.
}
\tag{1.8}
$$

Thus the fixed parent coarse field becomes rapidly subcritical on sufficiently deep descendants.

The unresolved component is controlled by the scale-critical velocity-increment quantity:

$$
\boxed{
\mathcal I_{r,\ell}^{(3)}
=
r^{-2}
\iint_{Q_r^{+}}
\int
\varphi_\ell(z)
|
\delta_z u(x,t)
|^3
dzdxdt.
}
\tag{1.9}
$$

Jensen gives:

$$
\boxed{
C_{w_\ell}(r_m)
\le
\theta^{-2m}
\mathcal I_{r,\ell}^{(3)}.
}
\tag{1.10}
$$

Therefore:

$$
\boxed{
C(r_m)
\le
C_1
\sigma^{-9/2}
M^{3/2}
\theta^{3m}
+
C_2
\theta^{-2m}
\mathcal I_{r,\ell}^{(3)}.
}
\tag{1.11}
$$

This estimate is then inserted into the standard pressure-decay recurrence:

$$
\boxed{
D_{m+1}
\le
aD_m+bC_m,
\qquad
a=C_P\theta<1,
\qquad
b=C_P\theta^{-2}.
}
\tag{1.12}
$$

The result is the first main theorem.

For every normalized bound:

$$
M_0<\infty,
$$

there exist:

$$
\boxed{
L=L(M_0,\sigma,\theta,\varepsilon_{\rm CKN})<\infty,
}
\tag{1.13}
$$

and:

$$
\boxed{
\delta_{\rm inc}
=
\delta_{\rm inc}
(
M_0,\sigma,\theta,\varepsilon_{\rm CKN}
)
>0
}
\tag{1.14}
$$

such that:

> if
>
> $$
> A_{r,\sigma}^{+}
> +
> D(z_0,r)
> \le
> M_0
> $$
>
> and
>
> $$
> \mathcal I_{r,\sigma r}^{(3)}
> \le
> \delta_{\rm inc},
> $$
>
> then:
>
> $$
> \boxed{
> \Psi(z_L,r_L)
> =
> C(z_L,r_L)
> +
> D(z_L,r_L)
> \le
> \varepsilon_{\rm CKN},
> }
> \tag{1.15}
> $$
>
> for every admissible descendant:
>
> $$
> Q_{r_L}(z_L)
> \subset
> Q_r(z_0)
> $$
>
> in the fixed controlled-drift chain.

Hence the CKN criterion makes the descendant regular.

This is the **Bounded-Lag Increment-Regularity Theorem**.

The second main theorem connects:

$$
\mathcal I^{(3)}
$$

to the derivative-compatible increment defect already used by the filtered-vorticity paper:

$$
\boxed{
\widetilde{\mathcal S}_{r,\ell}^{(3)}
=
\frac{
r
}{
\ell^2
}
\iint
\chi_r
\mathfrak M_{\ell,3}^{4}
dxdt.
}
\tag{1.16}
$$

At fixed:

$$
\ell=\sigma r,
$$

Hölder gives:

$$
\boxed{
\mathcal I_{r,\ell}^{(3)}
\le
C
\sigma^{3/2}
\left(
\widetilde{\mathcal S}_{r,\ell}^{(3)}
\right)^{3/4}.
}
\tag{1.17}
$$

Therefore the bounded-lag theorem may be rewritten:

$$
\boxed{
\widetilde{\mathcal S}_{r,\sigma r}^{(3)}
<
s_\ast(M_0)
\Longrightarrow
\Psi(r_L)
<
\varepsilon_{\rm CKN}.
}
\tag{1.18}
$$

Consequently, on any persistent non-CKN chain satisfying the uniform normalized reservoir bound:

$$
\boxed{
A_{r_k,\sigma}^{+}
+
D_k
\le
M_0,
}
\tag{1.19}
$$

one must have:

$$
\boxed{
\widetilde{\mathcal S}_{k}^{(3)}
\ge
s_\ast(M_0)
>
0
}
\tag{1.20}
$$

for **every sufficiently late scale**.

This is stronger than a positive-density supplier subsequence.

The supplier-density bridge is therefore unnecessary on the bounded-reservoir branch.

The branch is forced directly into the derivative-compatible increment mechanism.

This conclusion lines up exactly with the terminal obstruction profile in arXiv:2606.27560:

a bounded nonvanishing:

$$
\widetilde{\mathcal S}^{(3)}
$$

generates a cylindrical generalized Young profile of normalized velocity increments.

Therefore the next exact frontier is not:

$$
\text{bounded-lag supplier activation}.
$$

It is:

$$
\boxed{
\textbf{
Increment Young-Profile / Reynolds-Covariance Rigidity Lemma}.
}
\tag{1.21}
$$

The remaining compact bounded-reservoir singular branch must carry a scale-uniform nontrivial increment profile at every late scale.

The problem is now to show that such a recurrent increment profile necessarily produces one of:

1. a nonzero Reynolds covariance / commutator stress with positive paid flux;
2. a nonzero oscillation or concentration defect;
3. a spatial/scale escape carrier;
4. a genuinely nontrivial recurrent limiting profile subject to a Liouville/rigidity theorem.

If all four fail, the increment defect must vanish, contradicting (1.20).

---

# 2. Why absolute full supply is not the correct bounded-lag object

The finite-scale survival theorem proves:

$$
\boxed{
\sum_{k<N}
\left(
\mathrm{Sup}^{full}_k
-
\mathrm{Tax}^{full}_k
\right)_+
\ge
\lambda\varepsilon N
-
B_0
-
\sum_{k<N}
\mathrm{Leak}^{full}_k.
}
\tag{2.1}
$$

This is a powerful survival theorem.

But its transition supply is deliberately built from absolute magnitudes.

The local energy inequality before absolute-value domination contains signed transport.

The ledger replaces those signed terms by:

$$
\Phi_k^{flux},
\qquad
\Pi_k^{press}
$$

to obtain an unconditional one-sided estimate.

Thus:

$$
\boxed{
\text{ledger supply}
}
$$

means:

$$
\boxed{
\text{amount sufficient to dominate the positive side of the transition}.
}
$$

It does not mean:

$$
\boxed{
\text{spectral energy flux through one dyadic boundary}.
}
$$

Status:

$$
\boxed{
\textbf{SOURCE-SEMANTICS AUDIT}.
}
$$

---

# 3. NO-GO — ledger algebra alone cannot produce a supplier

Consider an abstract recurrence:

$$
B_{k+1}
\le
(1-\lambda)B_k
+
S_k
$$

with:

$$
S_k\ge0.
$$

Suppose the analytic estimate generating:

$$
S_k
$$

was obtained by replacing a signed transport:

$$
Y_k
$$

with:

$$
|Y_k|.
$$

The fact that:

$$
S_k
$$

is large does not determine:

- the sign of:

  $$
  Y_k;
  $$

- its frequency support;
- whether it is low-frequency transport;
- whether it creates a new high-frequency dissipation boundary.

Therefore no theorem of the form:

$$
\boxed{
S_k\ge\eta
\Longrightarrow
\text{supplier within }L
}
\tag{3.1}
$$

can follow from the ledger inequality alone.

Additional PDE decomposition is mandatory.

Status:

$$
\boxed{
\textbf{LOGICAL NO-GO}.
}
$$

This does not say such a bounded-lag supplier theorem is false for Navier--Stokes.

It says it is not a consequence of the current full-supply bookkeeping by itself.

---

# 4. Parent-scale coarse graining

Fix:

$$
Q_r(z_0)
=
B_r(x_0)
\times
(t_0-r^2,t_0).
$$

Choose:

$$
0<\sigma<\sigma_0
$$

and:

$$
\boxed{
\ell
=
\sigma r.
}
\tag{4.1}
$$

Let:

$$
S_\ell
$$

be a nonnegative compactly supported spatial mollifier.

Define:

$$
\boxed{
U_\ell
=
S_\ell u,
}
\tag{4.2}
$$

and:

$$
\boxed{
w_\ell
=
u-U_\ell.
}
\tag{4.3}
$$

Choose an enlarged spatial cylinder:

$$
Q_r^{+}
$$

large enough to contain all filter shifts of the descendant windows used below.

---

# 5. Parent enlarged local-energy bound

Define:

$$
\boxed{
A_{r,\sigma}^{+}
=
r^{-1}
\operatorname*{ess\,sup}_{
t_0-r^2<t<t_0
}
\int_{
B_{(1+c_\varphi\sigma)r}(x_0)
}
|u(x,t)|^2dx.
}
\tag{5.1}
$$

Assume:

$$
\boxed{
A_{r,\sigma}^{+}
\le
M.
}
\tag{5.2}
$$

Then Young's inequality gives, on the interior filter region:

$$
\boxed{
\|U_\ell(t)\|_\infty
\le
C_\varphi
\ell^{-3/2}
\|u(t)\|_{
L^2(B_{(1+c_\varphi\sigma)r})
}.
}
\tag{5.3}
$$

Therefore:

$$
\boxed{
\|U_\ell(t)\|_\infty
\le
C_\varphi
\sigma^{-3/2}
M^{1/2}
r^{-1}.
}
\tag{5.4}
$$

---

# 6. Descendant scale

Let:

$$
0<\theta<1
$$

be the fixed CKN chain ratio.

Set:

$$
\boxed{
r_m
=
\theta^m r.
}
\tag{6.1}
$$

Let:

$$
Q_{r_m}(z_m)
\subset
Q_r(z_0)
$$

be any admissible controlled-drift descendant whose spatial portion remains inside the interior filter region.

Since the number of descendant steps used below is fixed, the standard controlled-drift condition only requires a fixed enlargement of:

$$
Q_r^{+}.
$$

---

# 7. NEW LEMMA — coarse smooth part loses cubic criticality

Define:

$$
\boxed{
C_U(r_m)
=
r_m^{-2}
\iint_{
Q_{r_m}(z_m)
}
|U_\ell|^3dxdt.
}
\tag{7.1}
$$

Then:

$$
\boxed{
C_U(r_m)
\le
C_\varphi
\sigma^{-9/2}
M^{3/2}
\theta^{3m}.
}
\tag{7.2}
$$

### Proof

The spacetime measure of:

$$
Q_{r_m}
$$

is:

$$
C r_m^5.
$$

Using (5.4):

$$
\begin{aligned}
C_U(r_m)
&\le
r_m^{-2}
|Q_{r_m}|
\|U_\ell\|_\infty^3\\
&\le
C
r_m^3
\left[
C_\varphi
\sigma^{-3/2}
M^{1/2}
r^{-1}
\right]^3\\
&=
C_\varphi
\sigma^{-9/2}
M^{3/2}
\left(
\frac{
r_m
}{
r
}
\right)^3.
\end{aligned}
$$

Since:

$$
r_m/r
=
\theta^m,
$$

the result follows.

$$
\square
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 8. Velocity-increment residual

For:

$$
z\in\mathbb R^3,
$$

define:

$$
\delta_z u(x,t)
=
u(x-z,t)-u(x,t).
$$

Define:

$$
\boxed{
\mathcal I_{r,\ell}^{(3)}
=
r^{-2}
\iint_{
Q_r^{+}
}
\int
\varphi_\ell(z)
|
\delta_z u(x,t)
|^3
dzdxdt.
}
\tag{8.1}
$$

This quantity is scale invariant when:

$$
\ell/r
$$

is fixed.

Because:

$$
U_\ell-u
=
\int
\varphi_\ell(z)
\delta_z u
\,dz,
$$

Jensen gives:

$$
\boxed{
|w_\ell(x,t)|^3
\le
\int
\varphi_\ell(z)
|
\delta_z u(x,t)
|^3dz.
}
\tag{8.2}
$$

---

# 9. NEW LEMMA — unresolved cubic descendant bound

Define:

$$
\boxed{
C_w(r_m)
=
r_m^{-2}
\iint_{
Q_{r_m}(z_m)
}
|w_\ell|^3dxdt.
}
\tag{9.1}
$$

Then:

$$
\boxed{
C_w(r_m)
\le
\theta^{-2m}
\mathcal I_{r,\ell}^{(3)}.
}
\tag{9.2}
$$

### Proof

Use:

$$
Q_{r_m}
\subset
Q_r^{+}
$$

and (8.2):

$$
\begin{aligned}
C_w(r_m)
&\le
r_m^{-2}
\iint_{
Q_r^{+}
}
\int
\varphi_\ell(z)
|
\delta_z u|^3
dzdxdt\\
&=
\frac{
r^2
}{
r_m^2
}
\mathcal I_{r,\ell}^{(3)}\\
&=
\theta^{-2m}
\mathcal I_{r,\ell}^{(3)}.
\end{aligned}
$$

$$
\square
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 10. Descendant cubic badness bound

Use:

$$
|a+b|^3
\le
4
\left(
|a|^3+|b|^3
\right).
$$

Since:

$$
u
=
U_\ell+w_\ell,
$$

Sections 7 and 9 give:

$$
\boxed{
C(z_m,r_m)
\le
K_1
\sigma^{-9/2}
M^{3/2}
\theta^{3m}
+
K_2
\theta^{-2m}
\mathcal I_{r,\ell}^{(3)}.
}
\tag{10.1}
$$

This is the basic bounded-lag velocity-decay estimate.

---

# 11. Pressure recurrence

The standard local pressure decay estimate on the chain is:

$$
\boxed{
D_{m+1}
\le
C_P
\theta
D_m
+
C_P
\theta^{-2}
C_m.
}
\tag{11.1}
$$

Choose:

$$
\theta
$$

so that:

$$
\boxed{
a
=
C_P\theta
<
1.
}
\tag{11.2}
$$

Set:

$$
b
=
C_P\theta^{-2}.
$$

Iteration gives:

$$
\boxed{
D_L
\le
a^L
D_0
+
b
\sum_{m=0}^{L-1}
a^{L-1-m}
C_m.
}
\tag{11.3}
$$

Insert (10.1).

---

# 12. Coarse contribution to pressure decays

The coarse contribution is:

$$
S_L^{coarse}
=
\sum_{m=0}^{L-1}
a^{L-1-m}
\theta^{3m}.
$$

Let:

$$
\boxed{
\rho
=
\max
\{
a,\theta^3
\}
<
1.
}
\tag{12.1}
$$

Then:

$$
\boxed{
S_L^{coarse}
\le
L
\rho^{L-1}.
}
\tag{12.2}
$$

Therefore:

$$
\boxed{
bK_1
\sigma^{-9/2}
M^{3/2}
S_L^{coarse}
\to0
}
\tag{12.3}
$$

as:

$$
L\to\infty.
$$

---

# 13. Increment contribution to pressure

The increment contribution is:

$$
S_L^{inc}
=
\sum_{m=0}^{L-1}
a^{L-1-m}
\theta^{-2m}.
$$

Let:

$$
n
=
L-1-m.
$$

Then:

$$
S_L^{inc}
=
\theta^{-2(L-1)}
\sum_{n=0}^{L-1}
(a\theta^2)^n.
$$

Since:

$$
a\theta^2
=
C_P\theta^3
<1
$$

after decreasing:

$$
\theta
$$

if necessary,

$$
\boxed{
S_L^{inc}
\le
\frac{
\theta^{-2(L-1)}
}{
1-a\theta^2
}.
}
\tag{13.1}
$$

Thus:

$$
\boxed{
D_L
\le
a^LD_0
+
K_3
\sigma^{-9/2}
M^{3/2}
L\rho^{L-1}
+
K_4
\theta^{-2L}
\mathcal I_{r,\ell}^{(3)}.
}
\tag{13.2}
$$

---

# 14. CKN descendant estimate

At the final descendant:

$$
r_L=\theta^Lr,
$$

Section 10 gives:

$$
\boxed{
C_L
\le
K_1
\sigma^{-9/2}
M^{3/2}
\theta^{3L}
+
K_2
\theta^{-2L}
\mathcal I_{r,\ell}^{(3)}.
}
\tag{14.1}
$$

Combining with (13.2):

$$
\boxed{
\Psi_L
=
C_L+D_L
\le
a^LD_0
+
K_5
\sigma^{-9/2}
M^{3/2}
L\rho^{L-1}
+
K_6
\theta^{-2L}
\mathcal I_{r,\ell}^{(3)}.
}
\tag{14.2}
$$

---

# 15. NEW THEOREM — Bounded-Lag Increment-Regularity Theorem

## Theorem 15.1

Fix:

$$
M_0<\infty,
$$

$$
0<\sigma<\sigma_0,
$$

and choose:

$$
\theta
$$

with:

$$
C_P\theta<1,
\qquad
C_P\theta^3<1.
$$

Then there exist:

$$
\boxed{
L_\ast
=
L_\ast
(
M_0,\sigma,\theta,\varepsilon_{\rm CKN}
)
<\infty
}
\tag{15.1}
$$

and:

$$
\boxed{
\delta_{\rm inc}
=
\delta_{\rm inc}
(
M_0,\sigma,\theta,\varepsilon_{\rm CKN}
)
>0
}
\tag{15.2}
$$

such that the following holds.

Assume:

$$
\boxed{
A_{r,\sigma}^{+}
+
D(z_0,r)
\le
M_0,
}
\tag{15.3}
$$

and:

$$
\boxed{
\mathcal I_{r,\sigma r}^{(3)}
\le
\delta_{\rm inc}.
}
\tag{15.4}
$$

Then every admissible descendant at:

$$
\boxed{
r_\ast
=
\theta^{L_\ast}r
}
\tag{15.5}
$$

satisfies:

$$
\boxed{
\Psi(z_\ast,r_\ast)
\le
\varepsilon_{\rm CKN}.
}
\tag{15.6}
$$

Hence the Navier--Stokes solution is regular in a smaller cylinder.

### Proof

Choose:

$$
L_\ast
$$

large enough that:

$$
a^{L_\ast}M_0
+
K_5
\sigma^{-9/2}
M_0^{3/2}
L_\ast
\rho^{L_\ast-1}
\le
\frac{
\varepsilon_{\rm CKN}
}{
2
}.
$$

Then choose:

$$
\delta_{\rm inc}
$$

small enough that:

$$
K_6
\theta^{-2L_\ast}
\delta_{\rm inc}
\le
\frac{
\varepsilon_{\rm CKN}
}{
2
}.
$$

Equation (14.2) gives:

$$
\Psi_{L_\ast}
\le
\varepsilon_{\rm CKN}.
$$

Apply CKN epsilon regularity.

$$
\square
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 16. Derivative-compatible increment defect

The filtered-vorticity paper defines:

$$
d\nu_\ell(z)
=
\varphi_\ell(z)dz,
$$

and:

$$
d\mu_\ell(z)
=
\frac{
\ell
|
\nabla\varphi_\ell(z)
|
}{
\|
\nabla\varphi
\|_1
}
dz.
$$

For:

$$
p=3,
$$

define:

$$
M_{\varphi,3}(x,t)
=
\left(
\int
|
\delta_z u
|^3
d\nu_\ell(z)
\right)^{1/3},
$$

and the derivative-compatible envelope:

$$
\boxed{
\mathfrak M_{\ell,3}
=
M_{\varphi,3}
+
M_{\nabla,3}.
}
\tag{16.1}
$$

The scale-critical defect is:

$$
\boxed{
\widetilde{\mathcal S}_{r,\ell}^{(3)}
=
\frac{
r
}{
\ell^2
}
\iint
\chi_r
\mathfrak M_{\ell,3}^4
dxdt.
}
\tag{16.2}
$$

---

# 17. NEW THEOREM — Cubic increment controlled by derivative-compatible defect

## Theorem 17.1

At fixed:

$$
\ell=\sigma r,
$$

and for a cutoff equal to one on the increment region,

$$
\boxed{
\mathcal I_{r,\ell}^{(3)}
\le
C_Q
\sigma^{3/2}
\left(
\widetilde{\mathcal S}_{r,\ell}^{(3)}
\right)^{3/4}.
}
\tag{17.1}
$$

### Proof

Since:

$$
M_{\varphi,3}
\le
\mathfrak M_{\ell,3},
$$

$$
\mathcal I_{r,\ell}^{(3)}
\le
r^{-2}
\iint
\mathfrak M_{\ell,3}^3
dxdt.
$$

Let:

$$
|Q_r^{+}|
\le
C_Qr^5.
$$

Hölder gives:

$$
\iint
\mathfrak M_{\ell,3}^3
\le
\left(
\iint
\mathfrak M_{\ell,3}^4
\right)^{3/4}
|Q_r^{+}|^{1/4}.
$$

By (16.2):

$$
\iint
\mathfrak M_{\ell,3}^4
\le
C
\frac{
\ell^2
}{
r
}
\widetilde{\mathcal S}_{r,\ell}^{(3)}.
$$

Therefore:

$$
\begin{aligned}
\mathcal I_{r,\ell}^{(3)}
&\le
C
r^{-2}
\left(
\frac{
\ell^2
}{
r
}
\widetilde{\mathcal S}^{(3)}
\right)^{3/4}
r^{5/4}\\
&=
C
r^{-2}
\ell^{3/2}
r^{-3/4}
r^{5/4}
\left(
\widetilde{\mathcal S}^{(3)}
\right)^{3/4}\\
&=
C
\left(
\frac{
\ell
}{
r
}
\right)^{3/2}
\left(
\widetilde{\mathcal S}^{(3)}
\right)^{3/4}.
\end{aligned}
$$

Since:

$$
\ell/r=\sigma,
$$

the result follows.

$$
\square
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 18. Bounded-lag criterion in the native defect variable

Let:

$$
\delta_{\rm inc}
$$

be the threshold from Theorem 15.1.

Choose:

$$
\boxed{
s_\ast
=
c
\sigma^{-2}
\delta_{\rm inc}^{4/3},
}
\tag{18.1}
$$

with the constant chosen so that:

$$
\widetilde{\mathcal S}^{(3)}
<
s_\ast
$$

implies:

$$
\mathcal I^{(3)}
<
\delta_{\rm inc}.
$$

Then:

$$
\boxed{
\widetilde{\mathcal S}_{r,\sigma r}^{(3)}
<
s_\ast
\Longrightarrow
\Psi(
\theta^{L_\ast}r
)
\le
\varepsilon_{\rm CKN}.
}
\tag{18.2}
$$

This is the desired scale-critical bounded-lag criterion.

---

# 19. NEW COROLLARY — Persistent non-CKN branch forces persistent increment defect

Let:

$$
r_k=\theta^kr_0
$$

be an admissible nested branch satisfying:

$$
\boxed{
\Psi_k
>
\varepsilon_{\rm CKN}
}
\tag{19.1}
$$

for every sufficiently large:

$$
k.
$$

Assume:

$$
\boxed{
A_{k,\sigma}^{+}
+
D_k
\le
M_0
}
\tag{19.2}
$$

uniformly.

Then:

$$
\boxed{
\widetilde{\mathcal S}_{k}^{(3)}
\ge
s_\ast(M_0)
}
\tag{19.3}
$$

for every sufficiently large:

$$
k.
$$

### Proof

Fix late:

$$
k.
$$

Since the branch remains non-CKN through:

$$
k+L_\ast,
$$

Theorem 18.2 cannot have:

$$
\widetilde{\mathcal S}_{k}^{(3)}
<
s_\ast.
$$

Therefore:

$$
\widetilde{\mathcal S}_{k}^{(3)}
\ge
s_\ast.
$$

Since:

$$
k
$$

was arbitrary late, the conclusion holds at every sufficiently late scale.

$$
\square
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

This is stronger than a positive-density conclusion.

---

# 20. Unbounded-reservoir branch

The bounded-lag theorem assumes:

$$
A_{k,\sigma}^{+}
+
D_k
\le
M_0.
$$

If no finite:

$$
M_0
$$

controls the branch, then:

$$
\boxed{
\limsup_{k\to\infty}
\left(
A_{k,\sigma}^{+}
+
D_k
\right)
=
+\infty.
}
\tag{20.1}
$$

This is a genuine critical-reservoir noncompactness branch.

It cannot be discarded.

Thus the new global alternative is:

$$
\boxed{
\textbf{
persistent non-CKN}
\Longrightarrow
\textbf{
critical reservoir blowup}
\ \vee\
\textbf{
persistent derivative-compatible increment defect}.
}
}
\tag{20.2}
$$

This is now the correct bounded-lag reduction.

---

# 21. Relation to the supplier route

DCRP-22 remains valid:

$$
\boxed{
\text{local supplier}
\Longrightarrow
\text{diffusion}
\vee
\text{commutator defect}
\vee
\text{localization}
\vee
\text{far spatial escape}.
}
\tag{21.1}
$$

DCRP-23 shows that supplier **density** is not required to continue the bounded-reservoir argument.

Even in scales where no supplier is selected, persistent non-CKN behavior forces:

$$
\boxed{
\widetilde{\mathcal S}^{(3)}
\ge
s_\ast.
}
\tag{21.2}
$$

Thus the supplier route and the increment route cover complementary regimes.

### supplier route

isolates high-amplitude pointwise critical events.

### increment route

detects persistent roughness even if no single shell reaches the supplier threshold at every scale.

This is a more complete mechanism split.

---

# 22. External Young-profile theorem

The filtered-vorticity paper proves:

if normalized states are bounded in:

$$
L^3(Q^+)
$$

and:

$$
\sup_n
\widetilde{\mathcal S}_n^{(3)}
<
\infty,
$$

then the derivative-compatible increment fields generate a cylindrical generalized Young profile.

The increment state is:

$$
\boxed{
V_n^\sharp(x,t)(z)
=
\left(
\delta_zu^{(n)}(x,t),
\delta_zu^{(n)}(x,t)
\right)
\in
E_\sigma^\sharp.
}
\tag{22.1}
$$

The defect controls:

$$
\boxed{
\sigma^{-2}
\iint
\chi
\|
V_n^\sharp
\|_{
E_\sigma^\sharp
}^{4}
dxdt.
}
\tag{22.2}
$$

Thus the bounded nonvanishing branch of Corollary 19.1 has a genuine conservative compactness object.

---

# 23. Increment-profile alternative

Assume:

$$
\boxed{
s_\ast
\le
\widetilde{\mathcal S}_n^{(3)}
\le
S_\ast
<
\infty.
}
\tag{23.1}
$$

After subsequence extraction, the normalized increment fields generate a generalized Young profile.

There are three broad possibilities.

### strong/profile branch

The increments converge strongly enough that a genuine nonzero limiting increment field remains.

### oscillation branch

The Young measure is non-Dirac on a set of positive measure.

### concentration branch

The DiPerna--Majda concentration measure is nonzero.

The external lower-semicontinuity result places oscillation/concentration excess into a nonnegative defect:

$$
\boxed{
\mathcal D_\sigma^{(3)}
\ge0.
}
\tag{23.2}
$$

Thus only the strong/profile branch can avoid an explicit Young defect.

---

# 24. Reynolds covariance map

The increment profile carries the covariance map:

$$
\boxed{
\mathcal C(\Xi)
=
\int
\varphi_\sigma(z)
\Xi_\nu(z)
\otimes
\Xi_\nu(z)
dz
-
\left(
\int
\varphi_\sigma(z)
\Xi_\nu(z)dz
\right)^{\otimes2}.
}
\tag{24.1}
$$

This is exactly the increment-space analogue of the coarse Reynolds covariance:

$$
R_\ell
=
\langle
\delta u\otimes\delta u
\rangle_\ell
-
\langle
\delta u
\rangle_\ell^{\otimes2}.
$$

It is positive semidefinite.

Therefore the next rigidity problem is not an abstract probability problem.

It is tied directly to the NS coarse stress.

---

# 25. New exact frontier

The next target is:

$$
\boxed{
\textbf{
Increment Young-Profile / Reynolds-Covariance Rigidity Lemma}.
}
$$

A useful sufficient statement is:

> Let a normalized persistent non-CKN sequence satisfy:
>
> $$
> s_\ast
> \le
> \widetilde{\mathcal S}_n^{(3)}
> \le
> S_\ast,
> $$
>
> with bounded normalized local reservoirs and all previously completed:
>
> - diffusion;
> - localization;
> - far-field spatial escape;
> - supplier trace/residual;
> - UV/IR scale escape
>
> channels asymptotically zero.
>
> Then its cylindrical increment Young profile must satisfy at least one of:
>
> 1. nonzero oscillation/concentration defect:
>
> $$
> \mathcal D_\sigma^{(3)}>0;
> $$
>
> 2. nonzero coarse Reynolds covariance producing a paid pressure/flux/commutator channel;
> 3. a nontrivial strong increment profile solving the corresponding normalized coarse/defect dynamics.
>
> Finally prove a Liouville/rigidity theorem excluding case 3 under zero-cost recurrence.

If all three fail:

$$
\widetilde{\mathcal S}^{(3)}
\to0,
$$

contradicting Corollary 19.1.

---

# 26. Why this is not a return to the original problem

The original problem allowed an arbitrary hypothetical singular branch.

The current bounded-reservoir survivor must satisfy simultaneously:

$$
\boxed{
\Psi_k>\varepsilon_{\rm CKN}
\quad
\forall k\gg1,
}
$$

$$
\boxed{
A_{k,\sigma}^{+}+D_k\le M_0,
}
$$

$$
\boxed{
\widetilde{\mathcal S}_k^{(3)}
\ge s_\ast>0
\quad
\forall k\gg1,
}
$$

plus the zero-cost assumptions already developed for:

- local supplier activation;
- filtered diffusion;
- near-field stretching;
- far-field spatial source escape;
- localization;
- scale escape;
- finite-window trace/residual.

Thus the survivor is now a **persistent scale-critical velocity-increment microstructure**.

This is far narrower than generic Navier--Stokes blowup.

---

# 27. Source audit

## Finite-Window Singularity Audits

Primary facts used:

- exact definitions of:

  $$
  \Phi_k^{flux},
  \qquad
  \Pi_k^{press},
  \qquad
  \Lambda_k;
  $$

- full critical ledger;
- finite-scale survival theorem;
- pressure decay:

  $$
  D_{k+1}
  \le
  C_P\theta D_k
  +
  C_P\theta^{-2}C_k.
  $$

The source explicitly states that uniform taxation/observable depletion of all critical supply is an open input.

DCRP-23 does not claim to derive a supplier from the absolute ledger supply.

## Filtered Vortex Stretching and Subgrid Defects

Primary facts used:

- exact increment identity:

  $$
  R_\ell
  =
  \langle
  \delta u\otimes\delta u
  \rangle_\ell
  -
  \langle
  \delta u
  \rangle_\ell^{\otimes2};
  $$

- derivative-compatible increment envelope:

  $$
  \mathfrak M_{\ell,p};
  $$

- scale-critical defect:

  $$
  \widetilde{\mathcal S}_{r,\ell}^{(p)}
  =
  \frac r{\ell^2}
  \iint
  \chi
  \mathfrak M_{\ell,p}^{4};
  $$

- cylindrical generalized Young-profile compactness for bounded:

  $$
  \widetilde{\mathcal S}^{(3)};
  $$

- oscillation/concentration defect and covariance map.

---

# 28. End state

The proposed supplier-density bridge has been replaced by a stronger bounded-lag increment theorem.

The core estimate is:

$$
\boxed{
C(r_m)
\le
C
\sigma^{-9/2}
M^{3/2}
\theta^{3m}
+
C
\theta^{-2m}
\mathcal I_{r,\sigma r}^{(3)}.
}
$$

Together with pressure decay:

$$
\boxed{
\mathcal I^{(3)}
\text{ small}
\Longrightarrow
\Psi(\theta^{L_\ast}r)
<
\varepsilon_{\rm CKN}.
}
$$

And:

$$
\boxed{
\mathcal I^{(3)}
\le
C
\sigma^{3/2}
\left(
\widetilde{\mathcal S}^{(3)}
\right)^{3/4}.
}
$$

Therefore every bounded-reservoir persistent non-CKN branch satisfies:

$$
\boxed{
\widetilde{\mathcal S}_k^{(3)}
\ge
s_\ast
>
0
\qquad
\forall k\gg1.
}
$$

The next single frontier is:

$$
\boxed{
\textbf{
Increment Young-Profile / Reynolds-Covariance Rigidity Lemma}.
}
$$

The final compact survivor is now a recurrent scale-critical increment microstructure, not an unidentified supply channel.
