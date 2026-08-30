# NS-DCRP-21 — Far-Field Annular Escape, Core-Profile Collapse, and Harmonic-Jet Reduction to Spatial Infinity

- date: 2026-08-17
- status: research proof checkpoint
- canonical source: UTF-8 Markdown
- canonical math delimiters: `$...$` and `$$...$$`
- objective:
  1. attack the DCRP-20 far-field-only survivor without assuming an unproved affine-jet cancellation;
  2. combine the exact annular reassignment formula with the already-proved collapse of the core filtered-enstrophy reservoir;
  3. prove that a persistent far-field stretching surplus forces the source annulus to escape to infinite relative spatial radius with diverging normalized annular vorticity amplitude;
  4. show that bounded-relative harmonic affine jets cannot be the final zero-cost survivor.
- no full Navier--Stokes regularity claim is made.
- principal external primary source:
  - Runlong Yu, *Filtered Vortex Stretching and Subgrid Defects for the Three-Dimensional Navier--Stokes Equations*, arXiv:2606.27560v1.
- internal dependencies:
  - DCRP-18 two-sided scale/spatial completion;
  - DCRP-20 filtered-enstrophy diffusion/IR dichotomy and far-field-only survivor reduction.
- no novelty/priority claim is made without independent audit.

---

# 1. Executive result

DCRP-20 reduced the zero-cost/no-IR filtered-vorticity branch to a far-field-only survivor:

$$
\boxed{
O_k\to0,
\qquad
V_k^{+,\mathrm{far}}
\ge b_0>0.
}
\tag{1.1}
$$

The external far-field paper gives the annular reassignment bound

$$
\boxed{
\mu_k^{\mathrm{far,ann}}
\le
C_0
\sum_{j=0}^{k}
2^{-(k-j)}
\mathfrak A_{j,k}
\mathcal Q_k,
}
\tag{1.2}
$$

where

$$
\boxed{
\mathfrak A_{j,k}
=
\left(
r_j^{-1}
\iint_{I_k\times\widetilde A_j}
|\Omega_k|^2
\right)^{1/2},
}
\tag{1.3}
$$

and

$$
\boxed{
\mathcal Q_k
=
\left[
\int_{I_k}
\left(
\int_{B_{2r_k}}
\chi_k|\Omega_k|^2dx
\right)^2dt
\right]^{1/2}.
}
\tag{1.4}
$$

The first new theorem of this round is the core time-profile estimate

$$
\boxed{
\mathcal Q_k
\le
C_{\sigma}
M_k^{1/2}
O_k^{1/2},
}
\tag{1.5}
$$

where

$$
M_k
$$

is the fixed-relative local kinetic-energy bound used in the filtered-vorticity theorem.

Therefore

$$
\boxed{
O_k\to0
\Longrightarrow
\mathcal Q_k\to0.
}
\tag{1.6}
$$

This is stronger than the observation in DCRP-20 that only the time-integrated core reservoir vanishes.

The second new theorem is the far-field annular amplification theorem.

Assume:

$$
V_k^{+,\mathrm{far}}
\ge
b_0>0,
$$

the exterior tail beyond a fixed physical base radius is separated as in the external far-field decomposition, and

$$
O_k\to0.
$$

The exterior tail satisfies

$$
\boxed{
V_k^{+,\mathrm{ext}}
\le
C
r_k
O_k
\to0.
}
\tag{1.7}
$$

Hence for sufficiently large:

$$
k,
$$

$$
\boxed{
\mu_k^{\mathrm{far,ann}}
\ge
\frac{b_0}{2}.
}
\tag{1.8}
$$

Using (1.2) and (1.5),

$$
\boxed{
\sum_{j=0}^{k}
2^{-(k-j)}
\mathfrak A_{j,k}
\ge
\frac{
c\,b_0
}{
M_k^{1/2}
O_k^{1/2}
}.
}
\tag{1.9}
$$

Since:

$$
\sum_{m=0}^{\infty}2^{-m}=2,
$$

there exists:

$$
j_k\le k
$$

such that:

$$
\boxed{
\mathfrak A_{j_k,k}
\ge
\frac{
c\,b_0
}{
M_k^{1/2}
O_k^{1/2}
}.
}
\tag{1.10}
$$

Thus if:

$$
\sup_k M_k<\infty,
$$

$$
\boxed{
\mathfrak A_{j_k,k}
\to\infty.
}
\tag{1.11}
$$

The third new theorem shows that this amplified annulus cannot remain at bounded relative spatial distance from the core.

Let:

$$
m=k-j.
$$

For every fixed:

$$
M<\infty,
$$

assume the local energy on the fixed enlarged normalized ball is uniformly bounded:

$$
\boxed{
\sup_k
M_k^{(M)}
<
\infty.
}
\tag{1.12}
$$

Then for:

$$
0\le m\le M,
$$

the local filter smoothing bound gives:

$$
\boxed{
\mathfrak A_{k-m,k}
\le
C_{\sigma,M}
\left(
M_k^{(M)}
\right)^{1/2}.
}
\tag{1.13}
$$

Consequently the annuli selected in (1.10) must satisfy:

$$
\boxed{
m_k
=
k-j_k
\to\infty.
}
\tag{1.14}
$$

Equivalently:

$$
\boxed{
\frac{
r_{j_k}
}{
r_k
}
=
2^{m_k}
\to\infty.
}
\tag{1.15}
$$

Hence:

$$
\boxed{
\textbf{
persistent far-field work with a collapsing core enstrophy profile
forces the source vorticity reservoir to escape to normalized spatial infinity.
}
}
\tag{1.16}
$$

Moreover its normalized annular amplitude diverges.

This result changes the interpretation of the harmonic-jet frontier.

The external paper correctly notes that fixed exterior annular sources generate harmonic strain fields in the core and that low-order affine jets are the modes that can recur across nested scales.

DCRP-21 proves:

$$
\boxed{
\textbf{
an affine jet sourced at bounded relative spatial radius cannot sustain
the DCRP-20 far-field-only survivor.
}
}
\tag{1.17}
$$

If a fixed-relative source annulus remains inside:

$$
|y-x_0|
\lesssim
2^M r_k,
$$

its normalized annular reservoir is uniformly bounded by local energy and filter smoothing, while the core profile:

$$
\mathcal Q_k
$$

tends to zero.

Its work therefore tends to zero.

Thus any recurrent affine harmonic jet capable of paying:

$$
V_k^{+,\mathrm{far}}
\ge b_0
$$

must be sourced at:

$$
\boxed{
\frac{
|y-x_0|
}{
r_k
}
\to\infty.
}
\tag{1.18}
$$

This is not a mysterious finite-dimensional jet recurrence.

It is an exterior-source spatial-escape branch.

Therefore the DCRP-20 far-field-only survivor reduces further to:

$$
\boxed{
\textbf{
spatial-infinity annular vorticity amplification.
}
}
\tag{1.19}
$$

In a transition-complete package that retains:

- absolute annular filtered-vorticity amplitude;
- normalized spatial source position;
- the point at spatial infinity;

one has:

$$
\boxed{
\textbf{
zero spatial-defect branch}
\Longrightarrow
V_k^{+,\mathrm{far}}\to0.
}
\tag{1.20}
$$

Combining with DCRP-20:

$$
\boxed{
\textbf{
zero diffusion}
+
\textbf{
zero IR-frequency defect}
+
\textbf{
zero commutator defect}
+
\textbf{
zero localization}
+
\textbf{
zero spatial-source escape}
\Longrightarrow
\textbf{
no positive filtered-enstrophy surplus}.
}
}
\tag{1.21}
$$

Thus the far-field harmonic-jet obstruction is closed **at the level of compactness alternatives**.

The remaining major bridge is no longer a stretching decomposition.

It is:

$$
\boxed{
\textbf{
Singular/CKN Badness}
\Longrightarrow
\textbf{
Persistent Filtered-Enstrophy Surplus or an Already-Paid Defect}.
}
}
\tag{1.22}
$$

Equivalently, the next question is whether every singular local branch must actually activate the filtered-vorticity mechanism strongly enough for the now-closed mechanism decomposition to apply.

A useful next target is:

$$
\boxed{
\textbf{
Local Supplier / Filtered-Enstrophy Activation Lemma}.
}
\tag{1.23}
$$

The DCRP-16 supplier theorem is a natural starting point.

---

# 2. External annular reassignment audited

The external paper defines:

$$
I_k
=
(t_0-r_k^2,t_0),
$$

and for:

$$
j\le k,
$$

$$
\boxed{
\widetilde A_j
=
\left\{
y:
(\Gamma-1)r_j
<
|y-x_0|
\le
(2\Gamma+1)r_j
\right\}.
}
\tag{2.1}
$$

The reassigned annular reservoir is:

$$
\boxed{
\mathfrak A_{j,k}
=
\left(
r_j^{-1}
\iint_{I_k\times\widetilde A_j}
|\Omega_k|^2
\right)^{1/2}.
}
\tag{2.2}
$$

The core time profile is:

$$
\boxed{
\mathcal Q_k
=
\left[
\int_{I_k}
\left(
\int_{B_{2r_k}}
\chi_k|\Omega_k|^2dx
\right)^2
dt
\right]^{1/2}.
}
\tag{2.3}
$$

The exact moving-shell reassignment estimate is:

$$
\boxed{
\mu_k^{\mathrm{far,ann}}
\le
C_0
\sum_{j=0}^{k}
2^{-(k-j)}
\mathfrak A_{j,k}
\mathcal Q_k.
}
\tag{2.4}
$$

The dyadic weight is summable:

$$
\boxed{
\sum_{j=0}^{k}
2^{-(k-j)}
<
2.
}
\tag{2.5}
$$

This summability is the key new leverage once:

$$
\mathcal Q_k
$$

is shown to vanish.

---

# 3. Core filtered-vorticity profile

Let:

$$
\boxed{
F_k(t)
=
\int_{B_{2r_k}}
\chi_k(x,t)
|\Omega_k(x,t)|^2dx.
}
\tag{3.1}
$$

Then:

$$
\boxed{
O_k
=
r_k^{-1}
\int_{I_k}
F_k(t)dt.
}
\tag{3.2}
$$

Also:

$$
\boxed{
\mathcal Q_k
=
\|F_k\|_{L_t^2(I_k)}.
}
\tag{3.3}
$$

The problem is that in general:

$$
L_t^1\to0
$$

does not imply:

$$
L_t^2\to0.
$$

The filtered-vorticity smoothing bound supplies the missing:

$$
L_t^\infty
$$

control.

---

# 4. NEW THEOREM — Core Time-Profile Collapse

## Theorem 4.1

Assume:

$$
\ell_k
=
\sigma r_k
$$

with fixed:

$$
\sigma>0.
$$

Assume the fixed-relative local kinetic-energy coordinate satisfies:

$$
\boxed{
M_k
\le
M_\ast.
}
\tag{4.1}
$$

Then:

$$
\boxed{
\mathcal Q_k
\le
C_{\sigma}
M_\ast^{1/2}
O_k^{1/2}.
}
\tag{4.2}
$$

In particular:

$$
\boxed{
O_k\to0
\Longrightarrow
\mathcal Q_k\to0.
}
\tag{4.3}
$$

### Proof

The local filtered-vorticity bound gives:

$$
\boxed{
\|\Omega_k(t)\|_{L^\infty(B_{2r_k})}
\le
C_\sigma
M_\ast^{1/2}
r_k^{-2}.
}
\tag{4.4}
$$

Therefore:

$$
F_k(t)
\le
C
r_k^3
\|\Omega_k(t)\|_\infty^2
\le
C_\sigma
M_\ast
r_k^{-1}.
$$

Hence:

$$
\boxed{
\|F_k\|_{L^\infty_t}
\le
C_\sigma
M_\ast
r_k^{-1}.
}
\tag{4.5}
$$

Now:

$$
\mathcal Q_k^2
=
\int
F_k^2dt
\le
\|F_k\|_\infty
\int
F_kdt.
$$

But:

$$
\int
F_kdt
=
r_kO_k.
$$

Therefore:

$$
\mathcal Q_k^2
\le
C_\sigma
M_\ast
O_k.
$$

Take square roots.

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

# 5. Exterior tail beyond the fixed base radius

The annular reassignment of the external paper treats the source shells:

$$
0\le m\le k.
$$

The more distant shells:

$$
m>k
$$

lie beyond a fixed physical base radius comparable to:

$$
r_0.
$$

Let:

$$
S_k^{\mathrm{ext}}
$$

be the filtered strain generated from source points separated from the core by at least:

$$
c r_0.
$$

The strain-kernel:

$$
L^2
$$

tail gives:

$$
\boxed{
\|
K\mathbf1_{|z|>cr_0}
\|_2
\le
C
r_0^{-3/2}.
}
\tag{5.1}
$$

The global filtered-vorticity bound gives:

$$
\boxed{
\|\Omega_k(t)\|_2
\le
C
\ell_k^{-1}
\|u(t)\|_2
\le
C_\sigma
r_k^{-1}
M_E^{1/2}.
}
\tag{5.2}
$$

Therefore:

$$
\boxed{
\|S_k^{\mathrm{ext}}(t)\|_\infty
\le
C_\sigma
r_0^{-3/2}
r_k^{-1}
M_E^{1/2}.
}
\tag{5.3}
$$

The normalized exterior positive work obeys:

$$
\begin{aligned}
V_k^{+,\mathrm{ext}}
&\le
r_k
\|S_k^{\mathrm{ext}}\|_\infty
\iint_{Q_k}
\chi_k|\Omega_k|^2
\\
&=
r_k
\|S_k^{\mathrm{ext}}\|_\infty
(r_kO_k).
\end{aligned}
$$

Hence:

$$
\boxed{
V_k^{+,\mathrm{ext}}
\le
C_\sigma
r_0^{-3/2}
M_E^{1/2}
r_k
O_k.
}
\tag{5.4}
$$

Thus if:

$$
O_k
$$

is bounded, and in particular if:

$$
O_k\to0,
$$

$$
\boxed{
V_k^{+,\mathrm{ext}}\to0.
}
\tag{5.5}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 6. NEW THEOREM — Annular Source Amplification

## Theorem 6.1

Assume:

$$
\boxed{
V_k^{+,\mathrm{far}}
\ge
b_0>0,
}
\tag{6.1}
$$

$$
\boxed{
O_k\to0,
}
\tag{6.2}
$$

and:

$$
\boxed{
M_k\le M_\ast.
}
\tag{6.3}
$$

Then, after discarding finitely many:

$$
k,
$$

there exists:

$$
j_k\le k
$$

such that:

$$
\boxed{
\mathfrak A_{j_k,k}
\ge
\frac{
c\,b_0
}{
M_\ast^{1/2}
O_k^{1/2}
}.
}
\tag{6.4}
$$

Consequently:

$$
\boxed{
\mathfrak A_{j_k,k}
\to\infty.
}
\tag{6.5}
$$

### Proof

By Theorem 5.1:

$$
V_k^{+,\mathrm{ext}}\to0.
$$

The far-field positive work is bounded above by the annular absolute contribution plus the exterior tail budget.

Therefore for sufficiently large:

$$
k,
$$

$$
\mu_k^{\mathrm{far,ann}}
\ge
\frac{b_0}{2}.
$$

Apply the external annular reassignment estimate:

$$
\frac{b_0}{2}
\le
C_0
\mathcal Q_k
\sum_{j=0}^{k}
2^{-(k-j)}
\mathfrak A_{j,k}.
$$

By Theorem 4.1:

$$
\mathcal Q_k
\le
C_\sigma
M_\ast^{1/2}
O_k^{1/2}.
$$

Thus:

$$
\sum_{j=0}^{k}
2^{-(k-j)}
\mathfrak A_{j,k}
\ge
\frac{
c\,b_0
}{
M_\ast^{1/2}
O_k^{1/2}
}.
$$

Since the weights sum to less than two:

$$
\max_{0\le j\le k}
\mathfrak A_{j,k}
\ge
\frac12
\sum_{j=0}^{k}
2^{-(k-j)}
\mathfrak A_{j,k}.
$$

Choose:

$$
j_k
$$

realizing the maximum.

This proves (6.4).

$$
\square
$$

Status:

$$
\boxed{
\textbf{PROVED using Proposition 8.6 of arXiv:2606.27560 plus Theorems 4.1 and 5.1 above}.
}
$$

---

# 7. Fixed-relative annuli cannot amplify without bound

Let:

$$
m=k-j.
$$

Then:

$$
r_j
=
2^m
r_k.
$$

Fix:

$$
M<\infty.
$$

For:

$$
0\le m\le M,
$$

the annulus:

$$
\widetilde A_{k-m}
$$

lies inside a fixed enlarged normalized ball:

$$
B_{R_Mr_k}(x_0),
$$

where:

$$
R_M
$$

depends only on:

$$
M
$$

and:

$$
\Gamma.
$$

Assume:

$$
\boxed{
M_k^{(M)}
:=
r_k^{-1}
\operatorname*{ess\,sup}_{t\in I_k}
\int_{
B_{R_Mr_k}(x_0)
}
|u(x,t)|^2dx
\le
M_M.
}
\tag{7.1}
$$

The local filter smoothing estimate gives:

$$
\boxed{
\|\Omega_k(t)\|_{
L^\infty(B_{R_Mr_k})
}
\le
C_{\sigma,M}
M_M^{1/2}
r_k^{-2}.
}
\tag{7.2}
$$

---

# 8. NEW THEOREM — Bounded-Relative Annular Reservoir Bound

## Theorem 8.1

Under (7.1), for every:

$$
0\le m\le M,
$$

$$
\boxed{
\mathfrak A_{k-m,k}
\le
C_{\sigma,\Gamma,M}
M_M^{1/2}
2^m.
}
\tag{8.1}
$$

In particular:

$$
\boxed{
\sup_k
\max_{0\le m\le M}
\mathfrak A_{k-m,k}
<
\infty.
}
\tag{8.2}
$$

### Proof

The annulus:

$$
\widetilde A_{k-m}
$$

has volume:

$$
\boxed{
|\widetilde A_{k-m}|
\le
C_\Gamma
r_{k-m}^3
=
C_\Gamma
2^{3m}
r_k^3.
}
\tag{8.3}
$$

The time interval has length:

$$
|I_k|
=
r_k^2.
$$

Therefore:

$$
\begin{aligned}
\mathfrak A_{k-m,k}^2
&=
r_{k-m}^{-1}
\iint_{
I_k\times\widetilde A_{k-m}
}
|\Omega_k|^2
\\
&\le
r_{k-m}^{-1}
r_k^2
C_\Gamma
r_{k-m}^3
\|\Omega_k\|_\infty^2
\\
&\le
C
r_k^2
r_{k-m}^2
\left[
M_M
r_k^{-4}
\right]
\\
&=
C
M_M
\left(
\frac{
r_{k-m}
}{
r_k
}
\right)^2
\\
&=
C
M_M
2^{2m}.
\end{aligned}
$$

Take square roots.

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

# 9. NEW THEOREM — Far-Field Source Spatial Escape

## Theorem 9.1

Assume the hypotheses of Theorem 6.1.

Assume in addition that for every fixed:

$$
M<\infty,
$$

the enlarged local-energy bound:

$$
\sup_kM_k^{(M)}<\infty
$$

holds.

Let:

$$
j_k
$$

be the amplified annulus supplied by Theorem 6.1 and define:

$$
\boxed{
m_k
=
k-j_k.
}
\tag{9.1}
$$

Then:

$$
\boxed{
m_k\to\infty.
}
\tag{9.2}
$$

Equivalently:

$$
\boxed{
\frac{
r_{j_k}
}{
r_k
}
\to\infty.
}
\tag{9.3}
$$

### Proof

Suppose not.

Then after a subsequence:

$$
m_k\le M
$$

for some fixed:

$$
M.
$$

Theorem 8.1 gives:

$$
\sup_k
\mathfrak A_{j_k,k}
<
\infty.
$$

But Theorem 6.1 gives:

$$
\mathfrak A_{j_k,k}\to\infty.
$$

Contradiction.

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

# 10. Quantitative spatial-escape strength

Theorem 6.1 actually gives more than:

$$
m_k\to\infty.
$$

The selected annular reservoir satisfies:

$$
\boxed{
\mathfrak A_{j_k,k}
\gtrsim
O_k^{-1/2}.
}
\tag{10.1}
$$

up to the fixed local-energy and far-surplus constants.

Thus the source does not merely move outward.

Its normalized annular filtered-vorticity amplitude diverges while its relative radius diverges.

Therefore the survivor is:

$$
\boxed{
\textbf{
spatial escape}
+
\textbf{
annular critical-amplitude blowup}.
}
\tag{10.2}
$$

This is substantially more rigid than a bounded external harmonic background.

---

# 11. Harmonic affine-jet interpretation

The external paper replaces moving shells by a fixed smooth annular partition:

$$
\psi_j(y)
$$

supported where:

$$
|y-x_0|
\simeq
r_j,
$$

and defines:

$$
\boxed{
H_{j,k}(x,t)
=
\int
K(x-y)
\psi_j(y)
\Omega_k(y,t)dy.
}
\tag{11.1}
$$

For:

$$
j<k,
$$

$$
H_{j,k}
$$

is a smooth exterior-source strain field in the core.

In the exterior-source formulation it is harmonic there.

Write its Taylor expansion:

$$
\boxed{
H_{j,k}(x,t)
=
A_{j,k}(t)
+
B_{j,k}(t)(x-x_0)
+
R_{j,k}^{(2)}(x,t).
}
\tag{11.2}
$$

The paper notes that the affine jet:

$$
(A_{j,k},B_{j,k})
$$

is the low-order mode that may recur across nested cores.

DCRP-21 gives a new restriction on such recurrence.

---

# 12. NEW COROLLARY — bounded-relative harmonic jets cannot sustain the survivor

Fix:

$$
M<\infty.
$$

Consider only source annuli satisfying:

$$
0\le k-j\le M.
$$

Under the fixed-relative local-energy bounds of Theorem 8.1, their annular source reservoirs are uniformly bounded.

The external annular work formula then gives:

$$
\boxed{
\mu_k^{\mathrm{far},\,m\le M}
\le
C_M
\mathcal Q_k.
}
\tag{12.1}
$$

By Theorem 4.1:

$$
\mathcal Q_k\to0.
$$

Therefore:

$$
\boxed{
\mu_k^{\mathrm{far},\,m\le M}
\to0.
}
\tag{12.2}
$$

Hence no fixed finite collection of bounded-relative exterior harmonic jets can support:

$$
V_k^{+,\mathrm{far}}\ge b_0.
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

The low-order affine jet can survive only if its source scale itself recedes to:

$$
m\to\infty.
$$

---

# 13. Why no affine cancellation theorem is needed on the zero-spatial-defect branch

The external paper leaves affine-jet cancellation as a conditional route because an affine harmonic mode may remain visible across nested cores.

DCRP-21 does not prove algebraic cancellation of an arbitrary affine strain.

Instead it proves a different statement:

> If the core filtered-enstrophy time profile collapses, then any affine jet sourced at bounded relative radius has vanishing work.

Thus the only affine jets relevant to the DCRP-20 far-field survivor are sourced at unbounded relative distance.

Those are already a spatial noncompactness phenomenon.

Therefore, on a transition-complete branch satisfying:

$$
\boxed{
\text{no spatial-source escape},
}
\tag{13.1}
$$

one does not need a separate universal affine-cancellation theorem.

The far-field source is forced into the near/finite-relative compact sector, where its work vanishes because:

$$
\mathcal Q_k\to0.
$$

This is an alternative closure route to the paper's proposed affine-jet cancellation module.

---

# 14. Spatial carrier completion

For the far-field source, a natural native carrier is the family:

$$
\boxed{
\left(
m,
\mathfrak A_{k-m,k}
\right),
\qquad
m\in\mathbb N_0.
}
\tag{14.1}
$$

Compactify relative source radius by:

$$
\boxed{
\overline{\mathbb N}_0^{sp}
=
\mathbb N_0
\cup
\{
+\infty_{sp}
\}.
}
\tag{14.2}
$$

Retain separately:

1. normalized source-position distribution;
2. absolute annular amplitude.

Theorem 9.1 says that a far-field-only survivor produces:

$$
\boxed{
+\infty_{sp}
}
$$

with divergent absolute amplitude.

This is a native PDE-generated spatial carrier.

It does not copy a singularity label.

---

# 15. Transition-complete zero-spatial-defect implication

Suppose a normalized filtered mechanism sequence satisfies the DCRP-20 zero-cost conditions:

$$
P_k\to0,
$$

$$
\widetilde{\mathcal S}^{(3)}_k\to0,
$$

$$
L_k+L_k^{\mathrm{com}}+L_k^\omega\to0,
$$

no IR-frequency defect, and fixed-relative local-energy bounds.

DCRP-20 gives:

$$
O_k\to0.
$$

If the completed spatial-source carrier also has no defect at:

$$
+\infty_{sp},
$$

then Theorem 9.1 rules out:

$$
V_k^{+,\mathrm{far}}\ge b_0.
$$

Therefore:

$$
\boxed{
V_k^{+,\mathrm{far}}\to0.
}
\tag{15.1}
$$

Together with DCRP-20:

$$
\boxed{
V_k^{+,\mathrm{near}}\to0,
}
\tag{15.2}
$$

$$
\boxed{
F_k^{\mathrm{com}}\to0,
}
\tag{15.3}
$$

and:

$$
\boxed{
L_k\to0.
}
\tag{15.4}
$$

Hence:

$$
\boxed{
\textbf{
all positive filtered-vorticity mechanism channels vanish.
}
}
\tag{15.5}
$$

Status:

$$
\boxed{
\textbf{PROVED at the mechanism-package level under the stated zero-defect compactness assumptions}.
}
$$

---

# 16. Filtered-surplus consequence

Let:

$$
\mathfrak B_k
$$

be the post-near-field filtered-enstrophy surplus used in DCRP-20 and in the external filtered-vorticity theorem.

Under the zero-cost/no-IR/no-spatial-defect hypotheses above:

$$
V_k^{+,\mathrm{far}}
\to0,
$$

$$
\widetilde{\mathcal S}^{(3)}_k
\to0,
$$

and all localization terms vanish.

Therefore:

$$
\boxed{
\mathfrak B_k\to0.
}
\tag{16.1}
$$

Thus:

$$
\boxed{
\textbf{
a persistent positive filtered-enstrophy surplus cannot be an exact zero-cost compact obstruction.
}
}
\tag{16.2}
$$

This substantially closes the mechanism decomposition.

---

# 17. What this does not yet prove

A singular suitable weak solution is known to remain CKN-bad at every sufficiently small scale around a singular point.

But the current chain has not yet proved the implication:

$$
\boxed{
\text{persistent CKN badness}
\Longrightarrow
\inf_k
\mathfrak B_k
>
0.
}
\tag{17.1}
$$

Nor has it proved that every local supplier event forces a fixed positive:

$$
\mathfrak B_k
$$

at a comparable filtered scale.

Therefore eliminating a hypothetical persistent positive filtered-vorticity surplus does not yet eliminate every possible singular branch.

This is now the principal interface gap.

---

# 18. Why this is the correct next gap

The external structural program already separates:

- full CKN badness;
- coarse resolved badness;
- subfilter residual badness.

DCRP-19 reduced full critical supply to:

- transition influx;
- coarse resolved mechanism;
- subfilter residual.

DCRP-20/21 now substantially close the **filtered-vorticity mechanism** whenever it is activated.

The remaining question is whether singularity must activate that mechanism at a fixed critical strength.

This is a detector-to-mechanism lower-bound problem, not another decomposition problem.

---

# 19. Supplier route as the activation candidate

DCRP-16 proves that every first singular point admits:

$$
t_n\uparrow T,
$$

$$
x_n\to x_\ast,
$$

$$
\lambda_n\to\infty,
$$

with:

$$
\boxed{
\lambda_n^{-1}
|
\Delta_{\lambda_n}u(x_n,t_n)
|
\ge
c_{\rm loc}\nu.
}
\tag{19.1}
$$

DCRP-09/14 then produce an actual same-history nonlinear increment at the same scale.

A band-limited divergence-free supplier also has the global Fourier identity:

$$
\boxed{
\|
\nabla\times u_q
\|_2^2
\asymp
\lambda_q^2
\|u_q\|_2^2.
}
\tag{19.2}
$$

Together with:

$$
\lambda_q
\|u_q\|_2^2
\gtrsim
\nu^2,
$$

this gives a critical instantaneous vorticity-shell lower bound.

The unresolved part is to convert this instantaneous bandpass vorticity atom into a **fixed spacetime filtered-enstrophy surplus**:

$$
\mathfrak B_k\ge b_0.
$$

This is where possible ultrashort temporal spikes and low-pass/bandpass cancellation still matter.

---

# 20. New exact frontier

The next target is:

$$
\boxed{
\textbf{
Local Supplier / Filtered-Enstrophy Activation Lemma}.
}
$$

A useful sufficient statement is:

> Let:
>
> $$
> (x_n,t_n,\lambda_n)
> $$
>
> be the local supplier sequence of DCRP-16.
>
> Then after passing to:
>
> $$
> r_n\asymp\lambda_n^{-1},
> \qquad
> \ell_n=\sigma r_n,
> $$
>
> at least one of:
>
> 1. a fixed positive post-near-field filtered-enstrophy surplus:
>
> $$
> \mathfrak B_n\ge b_0;
> $$
>
> 2. a fixed positive filtered diffusion cost;
> 3. a derivative-compatible commutator defect;
> 4. a localization/pressure residual;
> 5. a temporal concentration defect;
>
> occurs.

If alternative 1 occurs, DCRP-20/21 eliminate the zero-cost compact branch.

Alternatives 2--5 are already paid/native defect channels after completion.

This would finally connect local singular supplier capture to the now-closed filtered-vorticity mechanism calculus.

---

# 21. Possible temporal concentration coordinate

The main technical difference between a supplier endpoint and the filtered-enstrophy surplus is time.

A supplier may, a priori, be a short spike.

Define the normalized bandpass enstrophy profile:

$$
\boxed{
e_n(\tau)
=
\int_{B_R}
|
\omega_{q_n}^{(n)}(y,\tau)
|^2dy.
}
\tag{21.1}
$$

At the supplier endpoint:

$$
\boxed{
e_n(0)\ge c\nu^2.
}
\tag{21.2}
$$

There are two possibilities.

### positive normalized residence

For some fixed:

$$
\tau_0>0,
$$

$$
\boxed{
\int_{-\tau_0}^{0}
e_n(\tau)d\tau
\ge
c_0>0.
}
\tag{21.3}
$$

Then a fixed filtered/bandpass enstrophy spacetime reservoir is activated.

### temporal concentration

For every fixed:

$$
\tau_0>0,
$$

the profile mass collapses toward:

$$
\tau=0.
$$

Then the supplier produces a nontrivial temporal concentration defect.

A transition-complete package should retain this concentration rather than silently lose it.

Thus even before a quantitative residence-time theorem, the activation problem admits a compactness alternative.

---

# 22. Why the harmonic-jet frontier has changed

The external paper states that a complete harmonic-rigidity theorem should control affine jets from a fixed annular source decomposition directly.

DCRP-21 does not prove that general theorem.

Instead, in the specific DCRP zero-core-reservoir regime, it proves:

$$
\boxed{
\text{bounded-relative source}
\Longrightarrow
\text{bounded annular amplitude}
\Longrightarrow
\text{vanishing far work}.
}
\tag{22.1}
$$

Therefore the only harmonic jets still relevant to the DCRP survivor are those whose **source annuli themselves escape to normalized spatial infinity**.

This is a stronger classification in the specific zero-cost branch, but it does not supersede the external paper's general harmonic-jet problem for arbitrary filtered flows.

---

# 23. Source ledger

## Filtered Vortex Stretching and Subgrid Defects

The following primary results are used:

### far-field moving-shell decomposition

$$
\mathbb S_k^{far}
=
\sum_m
\mathbb S_{k,m}.
$$

### bounded-overlap annular reassignment

The moving shell at relative separation:

$$
m
$$

is contained in a fixed annulus at scale:

$$
r_{k-m},
$$

and the fixed annuli have uniformly bounded overlap.

### exact reassigned bound

$$
\mu_k^{far,ann}
\le
C
\sum_{j=0}^k
2^{-(k-j)}
\mathfrak A_{j,k}
\mathcal Q_k.
$$

### fixed-annulus harmonic route

A fixed exterior annular source generates a smooth harmonic strain in the smaller core, and after subtraction of its affine Taylor jet the higher-order remainder gains powers of scale separation.

The paper explicitly does not prove unconditional affine-jet cancellation.

DCRP-21 uses the exact annular bound, not an assumed cancellation theorem.

---

# 24. End state

The far-field-only survivor from DCRP-20 has been reduced to a spatial-escape object.

The key new estimates are:

$$
\boxed{
\mathcal Q_k
\le
C_\sigma
M_\ast^{1/2}
O_k^{1/2},
}
$$

and, if:

$$
V_k^{+,\mathrm{far}}
\ge b_0,
\qquad
O_k\to0,
$$

then there exists:

$$
j_k\le k
$$

such that:

$$
\boxed{
\mathfrak A_{j_k,k}
\gtrsim
O_k^{-1/2}
\to\infty,
}
$$

and:

$$
\boxed{
k-j_k\to\infty.
}
$$

Thus:

$$
\boxed{
\textbf{
far-field survivor}
\Longrightarrow
\textbf{
spatial-infinity annular vorticity amplification}.
}
$$

Consequently a zero-spatial-defect, zero-IR, zero-diffusion, zero-commutator, zero-localization branch has:

$$
\boxed{
\mathfrak B_k\to0.
}
$$

The next single frontier is:

$$
\boxed{
\textbf{
Local Supplier / Filtered-Enstrophy Activation Lemma}.
}
$$

The mechanism decomposition is now substantially closed.

The remaining question is whether a singular branch must activate it at a fixed critical strength, or else leave a temporal/paid defect.
