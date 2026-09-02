# NS-DCRP-19 — Critical-Supply Source Reduction, Visibility-vs-Taxation No-Go, and the Filtered Stretching–Diffusion Pivot

- date: 2026-08-16
- status: research proof checkpoint
- canonical source: UTF-8 Markdown
- canonical math delimiters: `$...$` and `$$...$$`
- objective:
  1. inspect the exact full-supply formula behind the persistent non-CKN survival theorem;
  2. reduce positive untaxed supply to a short list of quantitative source mechanisms;
  3. determine whether the DCRP detector/supplier modules actually tax those sources or merely observe them;
  4. pivot from bookkeeping geometry to a coercive filtered vorticity mechanism without discarding the existing DCRP infrastructure.
- no full Navier--Stokes regularity claim is made.
- principal external primary sources:
  - Runlong Yu, *Critical Ledgers and Scale-Defect Cascades for Navier-Stokes*, arXiv:2606.13887;
  - Runlong Yu, *Finite-Window Singularity Audits and Local-to-Clean Defect Transfer for Navier-Stokes*, arXiv:2606.15086;
  - Runlong Yu, *Coarse-Grained Resolution and Pressure-Flux Work Depletion for Navier-Stokes CKN Badness*, arXiv:2606.25322;
  - Runlong Yu, *A Structural Audit of Navier-Stokes Obstruction Calculus*, arXiv:2606.25341.
- internal dependencies:
  - DCRP-08 through DCRP-18;
  - MORP/FCBP finite-window observation and residual architecture.
- no novelty/priority claim is made without independent audit.

---

# 1. Executive result

DCRP-18 ended with the proposed target:

$$
\boxed{
\textbf{
Critical Supply Taxation / Untaxed-Supply Capture Lemma}.
}
$$

The exact full critical supply from the ledger theorem is:

$$
\boxed{
\mathrm{Sup}^{full}_k
=
\theta^{-1}X_k
+
C_{I,\theta}X_k^{3/2}
+
C_P\theta^{-2}C_k,
}
\tag{1.1}
$$

where:

$$
\boxed{
X_k
=
\Phi_k
+
2\Pi_k.
}
\tag{1.2}
$$

Here:

- $\Phi_k$ is nonlinear cutoff/window flux supply;
- $\Pi_k$ is pressure transport supply;
- $C_k$ is the scale-critical local velocity-cubic reservoir.

The tax is:

$$
\boxed{
\mathrm{Tax}^{full}_k
=
2E_{k+1}
+
(1-\alpha)A_k
+
(1-\alpha)C_k
+
\delta_DD_k.
}
\tag{1.3}
$$

The leakage is:

$$
\boxed{
\mathrm{Leak}^{full}_k
=
\theta^{-1}\Lambda_k
+
C_{I,\theta}\Lambda_k^{3/2}.
}
\tag{1.4}
$$

The first new theorem of this round is purely algebraic but closure-relevant.

If:

$$
\boxed{
\left(
\mathrm{Sup}^{full}_k
-
\mathrm{Tax}^{full}_k
\right)_+
\ge
\eta>0,
}
\tag{1.5}
$$

then in particular:

$$
\mathrm{Sup}^{full}_k\ge\eta.
$$

Consequently at least one of:

$$
\boxed{
X_k
\ge
\xi_\eta
}
\tag{1.6}
$$

or:

$$
\boxed{
C_k
\ge
\zeta_\eta
}
\tag{1.7}
$$

must hold, where:

$$
\boxed{
\xi_\eta
=
\min
\left\{
\frac{\theta\eta}{4},
\left(
\frac{\eta}{4C_{I,\theta}}
\right)^{2/3}
\right\},
}
\tag{1.8}
$$

and:

$$
\boxed{
\zeta_\eta
=
\frac{
\theta^2\eta
}{
2C_P
}.
}
\tag{1.9}
$$

Moreover:

$$
X_k\ge\xi_\eta
$$

implies:

$$
\boxed{
\Phi_k
\ge
\frac{\xi_\eta}{3}
}
\tag{1.10}
$$

or:

$$
\boxed{
\Pi_k
\ge
\frac{\xi_\eta}{3}.
}
\tag{1.11}
$$

Thus every fixed-size full supply event comes from one of only three quantitative source classes:

$$
\boxed{
\text{nonlinear transition influx}
\ \vee\
\text{pressure transition influx}
\ \vee\
\text{cubic reservoir regeneration}.
}
\tag{1.12}
$$

The interpolation term:

$$
C_{I,\theta}X_k^{3/2}
$$

is **not an independent source mechanism**.

It is generated algebraically from the same transition influx:

$$
X_k.
$$

Likewise:

$$
C_P\theta^{-2}C_k
$$

is not a new transition current.

It is pressure regeneration from the old cubic reservoir.

This reduces the full-supply taxonomy.

The second new theorem combines the cubic branch with the coarse resolution lemma.

Because:

$$
\Psi_k
=
C_k+D_k
\ge
C_k,
$$

the exact coarse resolution:

$$
\boxed{
\Psi_k
\le
4\Psi_k^\ell
+
4\Omega_k^\ell
}
\tag{1.13}
$$

gives:

$$
\boxed{
C_k\ge\zeta_\eta
\Longrightarrow
\Psi_k^\ell
\ge
\frac{
\zeta_\eta
}{
8
}
\quad
\vee
\quad
\Omega_k^\ell
\ge
\frac{
\zeta_\eta
}{
8
}.
}
\tag{1.14}
$$

Hence fixed untaxed supply reduces quantitatively to:

$$
\boxed{
\begin{aligned}
&\text{nonlinear boundary/transition influx}\\
&\vee
\text{pressure transport}\\
&\vee
\text{resolved coarse CKN mechanism}\\
&\vee
\text{subfilter residual}.
\end{aligned}
}
\tag{1.15}
$$

This is a genuine source reduction.

However the main audit result is a NO-GO:

$$
\boxed{
\textbf{
source visibility}
\not\Rightarrow
\textbf{
source taxation}.
}
\tag{1.16}
$$

A positive forward flux is precisely a mechanism that supplies the next scale.

Detecting it does not make it negative.

A positive coarse pressure/velocity observation is a certificate of activity, not automatically a depletion term.

Therefore the DCRP trace/PFET/defect machinery cannot close the ledger merely by proving:

$$
\boxed{
\text{every source is visible or retained}.
}
\tag{1.17}
$$

What is needed is a **coercive PDE mechanism** that converts persistent positive supply into:

- diffusion;
- backscatter/negative work;
- subgrid forcing cost;
- pressure-compatible loss;
- direction incoherence;
- or another genuinely nonnegative depletion.

This is exactly the distinction:

$$
\boxed{
\text{bookkeeping/interface}
\neq
\text{coercive PDE estimate}.
}
\tag{1.18}
$$

The present route therefore pivots to the filtered vorticity equation.

For a fixed relative spatial filter:

$$
\ell=\sigma r,
$$

write:

$$
U^\ell=S_\ell u,
$$

$$
\Omega^\ell
=
\nabla\times U^\ell,
$$

$$
S^\ell
=
\frac12
\left(
\nabla U^\ell
+
(\nabla U^\ell)^T
\right),
$$

and:

$$
\mathcal J^\ell
=
\nabla\times
(\nabla\cdot R^\ell).
$$

The exact filtered vorticity equation is:

$$
\boxed{
\partial_t\Omega^\ell
-
\nu\Delta\Omega^\ell
+
(U^\ell\cdot\nabla)\Omega^\ell
=
(\Omega^\ell\cdot\nabla)U^\ell
-
\mathcal J^\ell.
}
\tag{1.19}
$$

Dotting with:

$$
\Omega^\ell
$$

gives the exact filtered enstrophy identity:

$$
\boxed{
\partial_t
\frac{
|\Omega^\ell|^2
}{
2
}
-
\nu\Delta
\frac{
|\Omega^\ell|^2
}{
2
}
+
U^\ell\cdot\nabla
\frac{
|\Omega^\ell|^2
}{
2
}
+
\nu
|\nabla\Omega^\ell|^2
=
S^\ell\Omega^\ell\cdot\Omega^\ell
-
\Omega^\ell\cdot\mathcal J^\ell.
}
\tag{1.20}
$$

The third new theorem of this round is a fixed-relative-filter bound.

Suppose an enlarged local energy coordinate satisfies:

$$
A^+(z_0,r)
\le
M.
$$

For a compactly supported spatial mollifier and an interior cutoff, one has:

$$
\boxed{
\|S^\ell(t)\|_{L^\infty}
\le
C_\sigma
M^{1/2}
r^{-2}.
}
\tag{1.21}
$$

Therefore the positive filtered stretching quantity:

$$
\boxed{
V_{r,\ell}^+
=
r
\iint_{Q_r}
\chi
\left(
S^\ell\Omega^\ell\cdot\Omega^\ell
\right)_+
dxdt
}
\tag{1.22}
$$

obeys:

$$
\boxed{
V_{r,\ell}^+
\le
C_\sigma
M^{1/2}
O_{r,\ell},
}
\tag{1.23}
$$

where:

$$
\boxed{
O_{r,\ell}
=
r^{-1}
\iint_{Q_r}
\chi
|\Omega^\ell|^2
dxdt.
}
\tag{1.24}
$$

Thus fixed-relative filtered stretching cannot become an independent arbitrarily large source while filtered enstrophy remains small.

This is a genuine mechanism reduction.

But it is **not** a regularity theorem.

It says the remaining dangerous mechanism has moved into the persistence/regeneration of the coarse enstrophy reservoir:

$$
O_{r,\ell}.
$$

The final frontier of this round is therefore sharper than "tax all supply":

$$
\boxed{
\textbf{
Filtered Enstrophy Sustenance / Stretching–Diffusion Depletion Lemma}.
}
\tag{1.25}
$$

The next desired estimate must show that persistent scale-critical coarse vorticity cannot regenerate through arbitrarily many scales unless one of the already completed channels is non-negligible.

A model target is:

$$
\boxed{
V_{r,\ell}^+
\le
(1-\varepsilon_\ast)
P_{r,\ell}
+
C(M)
O_{r,\ell}
+
C\mathcal A_{r,\ell}
+
R_{r,\ell}
+
L_{r,\ell},
}
\tag{1.26}
$$

together with a **scale-transition estimate for $O_{r,\ell}$** strong enough that the $C(M)O$ term does not simply become a new untaxed reservoir.

This last clause is the essential new point.

The stretching estimate alone is not enough.

The closure-facing object is:

$$
\boxed{
\textbf{
coarse-enstrophy regeneration efficiency across scales}.
}
\tag{1.27}
$$

---

# 2. Exact full critical ledger audited

Let:

$$
B_k
=
A_k+C_k+D_k.
$$

The transition quantities are:

$$
\boxed{
\Phi_k
=
r_k^{-1}
\iint_{Q_k}
|u|^2
|u\cdot\nabla\phi_k|
dxdt,
}
\tag{2.1}
$$

$$
\boxed{
\Pi_k
=
r_k^{-1}
\iint_{Q_k}
\left|
p-(p)_{B_{r_k}}(t)
\right|
|u\cdot\nabla\phi_k|
dxdt,
}
\tag{2.2}
$$

and:

$$
\boxed{
\Lambda_k
=
r_k^{-1}
\iint_{Q_k}
|u|^2
\left(
|\partial_t\phi_k|
+
|\Delta\phi_k|
\right)
dxdt.
}
\tag{2.3}
$$

The local energy inequality gives:

$$
\boxed{
A_{k+1}
+
2E_{k+1}
\le
\theta^{-1}
\left(
\Lambda_k+\Phi_k+2\Pi_k
\right).
}
\tag{2.4}
$$

The cubic interpolation gives:

$$
\boxed{
C_{k+1}
\le
C_{I,\theta}
\left[
(\Phi_k+2\Pi_k)^{3/2}
+
\Lambda_k^{3/2}
\right].
}
\tag{2.5}
$$

The pressure decay gives:

$$
\boxed{
D_{k+1}
\le
C_P\theta D_k
+
C_P\theta^{-2}C_k.
}
\tag{2.6}
$$

Hence:

$$
\boxed{
\mathrm{Sup}^{full}_k
=
\theta^{-1}
(\Phi_k+2\Pi_k)
+
C_{I,\theta}
(\Phi_k+2\Pi_k)^{3/2}
+
C_P\theta^{-2}C_k,
}
\tag{2.7}
$$

$$
\boxed{
\mathrm{Tax}^{full}_k
=
2E_{k+1}
+
(1-\alpha)A_k
+
(1-\alpha)C_k
+
\delta_DD_k,
}
\tag{2.8}
$$

and:

$$
\boxed{
\mathrm{Leak}^{full}_k
=
\theta^{-1}\Lambda_k
+
C_{I,\theta}\Lambda_k^{3/2}.
}
\tag{2.9}
$$

The one-step ledger is:

$$
\boxed{
B_{k+1}
-
(1-\alpha)B_k
\le
\mathrm{Sup}^{full}_k
-
\mathrm{Tax}^{full}_k
+
\mathrm{Leak}^{full}_k.
}
\tag{2.10}
$$

---

# 3. Algebraic source reduction

Set:

$$
\boxed{
X
=
\Phi+2\Pi.
}
\tag{3.1}
$$

Let:

$$
a=\theta^{-1},
$$

$$
b=C_{I,\theta},
$$

and:

$$
c=C_P\theta^{-2}.
$$

Then:

$$
\boxed{
\mathrm{Sup}^{full}
=
aX+bX^{3/2}+cC.
}
\tag{3.2}
$$

---

# 4. NEW THEOREM — Full-Supply Source Reduction

## Theorem 4.1

Let:

$$
X,C\ge0
$$

and:

$$
S=aX+bX^{3/2}+cC,
$$

where:

$$
a,b,c>0.
$$

If:

$$
\boxed{
S\ge\eta>0,
}
\tag{4.1}
$$

then:

$$
\boxed{
X
\ge
\xi_\eta
}
\tag{4.2}
$$

or:

$$
\boxed{
C
\ge
\zeta_\eta,
}
\tag{4.3}
$$

where:

$$
\boxed{
\xi_\eta
=
\min
\left\{
\frac{\eta}{4a},
\left(
\frac{\eta}{4b}
\right)^{2/3}
\right\},
}
\tag{4.4}
$$

and:

$$
\boxed{
\zeta_\eta
=
\frac{\eta}{2c}.
}
\tag{4.5}
$$

### Proof

Assume:

$$
X<\xi_\eta.
$$

Then:

$$
aX<\frac{\eta}{4},
$$

and:

$$
bX^{3/2}<\frac{\eta}{4}.
$$

Therefore:

$$
cC
=
S-aX-bX^{3/2}
>
\frac{\eta}{2}.
$$

Hence:

$$
C>\frac{\eta}{2c}.
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

# 5. Corollary for untaxed supply

If:

$$
\boxed{
\left(
\mathrm{Sup}^{full}
-
\mathrm{Tax}^{full}
\right)_+
\ge
\eta,
}
\tag{5.1}
$$

then:

$$
\mathrm{Sup}^{full}\ge\eta.
$$

Apply Theorem 4.1.

With the ledger coefficients:

$$
a=\theta^{-1},
$$

$$
b=C_{I,\theta},
$$

$$
c=C_P\theta^{-2},
$$

one obtains:

$$
\boxed{
X
\ge
\min
\left\{
\frac{\theta\eta}{4},
\left(
\frac{\eta}{4C_{I,\theta}}
\right)^{2/3}
\right\}
}
\tag{5.2}
$$

or:

$$
\boxed{
C
\ge
\frac{
\theta^2\eta
}{
2C_P
}.
}
\tag{5.3}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 6. Splitting transition influx

Since:

$$
X=\Phi+2\Pi,
$$

if:

$$
X\ge\xi,
$$

then at least one of:

$$
\boxed{
\Phi\ge\frac{\xi}{3}
}
\tag{6.1}
$$

or:

$$
\boxed{
\Pi\ge\frac{\xi}{3}
}
\tag{6.2}
$$

holds.

Indeed if both were smaller than:

$$
\xi/3,
$$

then:

$$
X
=
\Phi+2\Pi
<
\xi.
$$

Therefore:

$$
\boxed{
\textbf{
fixed positive full supply}
\Longrightarrow
\textbf{
large nonlinear flux}
\ \vee\
\textbf{
large pressure transport}
\ \vee\
\textbf{
large cubic reservoir}.
}
\tag{6.3}
$$

---

# 7. The interpolation term is not an independent mechanism

The term:

$$
C_{I,\theta}X^{3/2}
$$

enters because:

$$
C_{k+1}
$$

is bounded through local interpolation by:

$$
(A_{k+1}+E_{k+1})^{3/2},
$$

while:

$$
A_{k+1}+E_{k+1}
$$

is itself supplied by:

$$
\Lambda_k+X_k.
$$

Thus:

$$
\boxed{
X^{3/2}
}
$$

is a nonlinear amplification of the same transition influx.

It should not be counted as a third physical input channel.

This matters because a taxation theorem need not separately capture:

$$
X
$$

and:

$$
X^{3/2}.
$$

A quantitative control of:

$$
X
$$

automatically controls its ledger amplification on any fixed bounded range.

---

# 8. Pressure regeneration is reservoir recycling

The term:

$$
C_P\theta^{-2}C_k
$$

comes from the local Calderon--Zygmund pressure generated by the velocity quadratic source at the previous scale.

It is not a flux through the spatial boundary.

It is a regeneration of:

$$
D_{k+1}
$$

from:

$$
C_k.
$$

Thus the full supply mechanism has two conceptual families:

$$
\boxed{
\textbf{
transition influx}
}
$$

and:

$$
\boxed{
\textbf{
reservoir regeneration}.
}
$$

The old four-label phrase:

- nonlinear flux;
- pressure transport;
- interpolation amplification;
- pressure regeneration;

contains only three quantitatively distinct source terms and two conceptual source types.

---

# 9. Coarse resolution of the cubic-regeneration branch

Let:

$$
\Psi
=
C+D.
$$

The exact coarse-resolution lemma gives, for every fixed spatial filter length:

$$
\ell>0,
$$

$$
\boxed{
\Psi
\le
4\Psi^\ell
+
4\Omega^\ell,
}
\tag{9.1}
$$

where:

- $\Psi^\ell$ is the resolved coarse velocity-pressure quantity;
- $\Omega^\ell$ is the explicit subfilter residual.

Because:

$$
\Psi\ge C,
$$

if:

$$
C\ge\zeta,
$$

then:

$$
4\Psi^\ell+4\Omega^\ell
\ge
\zeta.
$$

Therefore:

$$
\boxed{
\Psi^\ell
\ge
\frac{\zeta}{8}
}
\tag{9.2}
$$

or:

$$
\boxed{
\Omega^\ell
\ge
\frac{\zeta}{8}.
}
\tag{9.3}
$$

Status:

$$
\boxed{
\textbf{PROVED from the coarse-resolution lemma}.
}
$$

---

# 10. Critical-supply source theorem

Combining Sections 5--9:

## Theorem 10.1

Fix:

$$
\eta>0.
$$

If:

$$
\boxed{
\left(
\mathrm{Sup}^{full}_k
-
\mathrm{Tax}^{full}_k
\right)_+
\ge
\eta,
}
\tag{10.1}
$$

then there exists a constant:

$$
c_\eta>0
$$

depending only on the fixed ledger parameters such that at least one of:

$$
\boxed{
\Phi_k\ge c_\eta,
}
\tag{10.2}
$$

$$
\boxed{
\Pi_k\ge c_\eta,
}
\tag{10.3}
$$

$$
\boxed{
\Psi_k^\ell\ge c_\eta,
}
\tag{10.4}
$$

or:

$$
\boxed{
\Omega_k^\ell\ge c_\eta
}
\tag{10.5}
$$

holds.

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

This is the quantitative **Critical Supply Source Reduction**.

---

# 11. Why this still does not tax the supply

Suppose:

$$
\Phi_k\ge c_\eta.
$$

This means a large amount of nonlinear energy transport crosses the chosen local cutoff.

It does not say that the transport is negative.

It may be precisely the positive energy injection that sustains the next scale.

Likewise:

$$
\Pi_k\ge c_\eta
$$

is a magnitude of pressure transport.

It does not determine whether that pressure transport depletes or feeds the local reservoir.

Likewise:

$$
\Psi_k^\ell\ge c_\eta
$$

means the resolved coarse state is bad/active.

It is not a negative term in the energy ledger.

Thus:

$$
\boxed{
\textbf{
classification}
+
\textbf{
observation}
\neq
\textbf{
taxation}.
}
\tag{11.1}
$$

---

# 12. NO-GO — perfect observation does not imply depletion

Consider the scalar recurrence:

$$
\boxed{
B_{k+1}
=
(1-\alpha)B_k
+
S_k
}
\tag{12.1}
$$

with:

$$
0<\alpha<1,
$$

and:

$$
S_k=\alpha B_\ast>0.
$$

Then:

$$
B_k=B_\ast
$$

is a persistent orbit.

Define a perfect detector:

$$
\boxed{
O_k=S_k.
}
\tag{12.2}
$$

Then the supply is completely observed:

$$
O_k>0
$$

at every scale.

Nevertheless there is no tax:

$$
\boxed{
\mathrm{Tax}_k=0.
}
\tag{12.3}
$$

The persistent orbit survives exactly because the observed supply replenishes the expected decay.

Therefore:

$$
\boxed{
\textbf{
even perfect source observability does not imply regularity.
}
}
\tag{12.4}
$$

Status:

$$
\boxed{
\textbf{NO-GO PROVED}.
}
$$

This abstract countermodel is the ledger-level version of the PDE distinction between forward cascade and depletion.

---

# 13. Fixed-chain pressure-flux depletion does not remove the no-go

The coarse-grained work theorem proves on a fixed finite chain that:

- forward combined work;
- resolved dissipation;

are paid by:

- initial localized kinetic energy;
- explicit localization leakage;
- negative combined work/backscatter.

This is a genuine signed PDE telescope.

However it does not prove:

- moving-window constants are uniformly controlled;
- leakage is summable on an infinite singular chain;
- every positive transition supply entering the full critical ledger is the same signed combined-work quantity;
- a positive forward work event becomes a negative tax at the next step.

Therefore the theorem is a depletion/accounting mechanism, but not an automatic uniform taxation theorem for:

$$
\mathrm{Sup}^{full}_k.
$$

This is precisely why the finite-scale survival theorem lists uniform taxation of all critical supply as an open input.

---

# 14. Mechanism pivot

The current DCRP architecture has become very effective at the following tasks:

- local supplier capture;
- actual-history forcing;
- shell-energy first crossing;
- pressure-flux/backscatter splitting;
- finite-window localization;
- trace separation;
- projection/residual completion;
- UV/IR/spatial escape completion.

These are obstruction-calculus and interface modules.

The remaining question is not:

> where did the supply go?

It is:

> why can the physically dangerous mechanism not keep producing enough positive supply to offset diffusion?

For three-dimensional incompressible Navier--Stokes, the intrinsic smooth-level mechanism is vortex stretching.

Thus the next primary object is filtered vorticity.

---

# 15. Filtered Navier--Stokes package

Let:

$$
S_\ell
$$

be a smooth nonnegative spatial mollifier of scale:

$$
\ell.
$$

Define:

$$
\boxed{
U^\ell
=
S_\ell u,
}
\tag{15.1}
$$

$$
\boxed{
P^\ell
=
S_\ell p,
}
\tag{15.2}
$$

and Reynolds covariance:

$$
\boxed{
R^\ell
=
S_\ell(u\otimes u)
-
U^\ell\otimes U^\ell.
}
\tag{15.3}
$$

The coarse momentum equation is:

$$
\boxed{
\partial_tU^\ell
-
\nu\Delta U^\ell
+
(U^\ell\cdot\nabla)U^\ell
+
\nabla P^\ell
=
-\nabla\cdot R^\ell.
}
\tag{15.4}
$$

Define:

$$
\boxed{
\Omega^\ell
=
\nabla\times U^\ell,
}
\tag{15.5}
$$

$$
\boxed{
S^\ell
=
\frac12
\left(
\nabla U^\ell
+
(\nabla U^\ell)^T
\right),
}
\tag{15.6}
$$

and:

$$
\boxed{
\mathcal J^\ell
=
\nabla\times
(
\nabla\cdot R^\ell
).
}
\tag{15.7}
$$

---

# 16. Exact filtered vorticity identity

Take curl of (15.4).

Because:

$$
\nabla\cdot U^\ell=0,
$$

$$
\boxed{
\partial_t\Omega^\ell
-
\nu\Delta\Omega^\ell
+
(U^\ell\cdot\nabla)\Omega^\ell
=
(\Omega^\ell\cdot\nabla)U^\ell
-
\mathcal J^\ell.
}
\tag{16.1}
$$

The antisymmetric part of:

$$
\nabla U^\ell
$$

does not contribute to:

$$
\Omega^\ell\cdot
(
(\Omega^\ell\cdot\nabla)U^\ell
).
$$

Hence:

$$
\boxed{
\Omega^\ell\cdot
(
(\Omega^\ell\cdot\nabla)U^\ell
)
=
S^\ell
\Omega^\ell\cdot\Omega^\ell.
}
\tag{16.2}
$$

Dot (16.1) with:

$$
\Omega^\ell.
$$

Then:

$$
\boxed{
\partial_t
\frac{
|\Omega^\ell|^2
}{
2
}
-
\nu\Delta
\frac{
|\Omega^\ell|^2
}{
2
}
+
U^\ell\cdot\nabla
\frac{
|\Omega^\ell|^2
}{
2
}
+
\nu
|\nabla\Omega^\ell|^2
=
S^\ell
\Omega^\ell\cdot\Omega^\ell
-
\Omega^\ell\cdot\mathcal J^\ell.
}
\tag{16.3}
$$

Status:

$$
\boxed{
\textbf{PRIMARY-SOURCE IDENTITY}.
}
$$

---

# 17. Scale-invariant filtered mechanism coordinates

Let:

$$
\chi
$$

be a nonnegative cutoff supported in:

$$
Q_r(z_0)
$$

and equal to one on a slightly smaller cylinder.

Choose relative filter:

$$
\boxed{
\ell
=
\sigma r,
\qquad
0<\sigma<\sigma_0.
}
\tag{17.1}
$$

Define:

$$
\boxed{
O_{r,\ell}
=
r^{-1}
\iint
\chi
|\Omega^\ell|^2
dxdt,
}
\tag{17.2}
$$

$$
\boxed{
P_{r,\ell}
=
\nu r
\iint
\chi
|\nabla\Omega^\ell|^2
dxdt,
}
\tag{17.3}
$$

$$
\boxed{
V_{r,\ell}^+
=
r
\iint
\chi
\left(
S^\ell
\Omega^\ell\cdot\Omega^\ell
\right)_+
dxdt,
}
\tag{17.4}
$$

and:

$$
\boxed{
R_{r,\ell}
=
r
\iint
\chi
|\Omega^\ell|
|\mathcal J^\ell|
dxdt.
}
\tag{17.5}
$$

Let:

$$
L_{r,\ell}
$$

denote the scale-invariant cutoff/transport terms obtained by integrating (16.3) against:

$$
\chi.
$$

Every quantity above is scale invariant under:

$$
u_r(y,s)
=
r
u(x_0+ry,t_0+r^2s),
$$

with:

$$
\ell/r
=
\sigma
$$

fixed.

---

# 18. Enlarged local energy bound

Because the mollifier has spatial support of radius:

$$
O(\ell),
$$

the filtered field inside:

$$
\operatorname{supp}\chi
$$

depends only on velocity in a slightly enlarged ball.

Define:

$$
\boxed{
A^+_{r,\sigma}
=
r^{-1}
\operatorname*{ess\,sup}_{t\in I_r}
\int_{
B_{(1+c\sigma)r}(x_0)
}
|u(x,t)|^2dx.
}
\tag{18.1}
$$

Assume:

$$
\boxed{
A^+_{r,\sigma}
\le
M.
}
\tag{18.2}
$$

This is automatic if the standard local energy coordinate is bounded on a fixed slightly enlarged normalized cylinder.

---

# 19. NEW THEOREM — Fixed-Relative-Filter Stretching Bound

## Theorem 19.1

Let:

$$
\ell=\sigma r.
$$

Assume:

$$
A^+_{r,\sigma}\le M.
$$

Then:

$$
\boxed{
\|
S^\ell(t)
\|_{
L^\infty(\operatorname{supp}\chi)
}
\le
C
\sigma^{-5/2}
M^{1/2}
r^{-2}.
}
\tag{19.1}
$$

Consequently:

$$
\boxed{
V_{r,\ell}^+
\le
C
\sigma^{-5/2}
M^{1/2}
O_{r,\ell}.
}
\tag{19.2}
$$

### Proof

Let:

$$
\rho_\ell(x)
=
\ell^{-3}
\rho(x/\ell)
$$

be the spatial mollifier.

Then:

$$
\nabla U^\ell
=
(\nabla\rho_\ell)*u.
$$

For every point whose filter ball lies inside the enlarged spatial region:

$$
|\nabla U^\ell(x,t)|
\le
\|
\nabla\rho_\ell
\|_2
\|
u(t)
\|_{
L^2(B_{(1+c\sigma)r})
}.
$$

The kernel scaling gives:

$$
\boxed{
\|
\nabla\rho_\ell
\|_2
=
\ell^{-5/2}
\|
\nabla\rho
\|_2.
}
\tag{19.3}
$$

The local energy bound gives:

$$
\|
u(t)
\|_{
L^2(B_{(1+c\sigma)r})
}
\le
M^{1/2}
r^{1/2}.
$$

Therefore:

$$
|\nabla U^\ell|
\le
C
(\sigma r)^{-5/2}
M^{1/2}
r^{1/2}
=
C
\sigma^{-5/2}
M^{1/2}
r^{-2}.
$$

The strain is bounded by the full gradient, so (19.1) follows.

Now:

$$
\begin{aligned}
V_{r,\ell}^+
&\le
r
\|
S^\ell
\|_\infty
\iint
\chi
|\Omega^\ell|^2
dxdt\\
&\le
r
\left[
C
\sigma^{-5/2}
M^{1/2}
r^{-2}
\right]
\left[
r
O_{r,\ell}
\right].
\end{aligned}
$$

Hence (19.2).

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

# 20. Interpretation of the stretching bound

Theorem 19.1 says:

$$
\boxed{
\textbf{
at fixed relative filter scale,
positive filtered vortex stretching is linearly controlled by
the filtered enstrophy reservoir whenever local kinetic energy is bounded.
}
}
\tag{20.1}
$$

Thus a filtered stretching cascade cannot have:

$$
V_{r,\ell}^+\gg1
$$

while:

$$
O_{r,\ell}\ll1
$$

under:

$$
A^+\le M.
$$

This reduces the mechanism.

The remaining dangerous state is one with persistent nontrivial:

$$
O_{r,\ell}.
$$

---

# 21. Why Theorem 19.1 is not a regularity theorem

The estimate:

$$
V^+
\le
C(M,\sigma)
O
$$

does not compare stretching with diffusion using a coefficient smaller than one.

The coefficient:

$$
C(M,\sigma)
$$

can be arbitrarily large when:

- $M$ is large;
- the relative filter scale:

  $$
  \sigma
  $$

  is small.

Thus the filtered enstrophy identity may still have the schematic form:

$$
\boxed{
\text{next coarse enstrophy}
\lesssim
C(M,\sigma)
\text{ old coarse enstrophy}
+
\text{defects}.
}
\tag{21.1}
$$

There is no decay basin from this inequality alone.

Therefore:

$$
\boxed{
\text{stretching bounded by }O
\neq
\text{stretching depleted by diffusion}.
}
\tag{21.2}
$$

This is another visibility/taxation distinction at the mechanism level.

---

# 22. Local filtered enstrophy ledger

Integrate (16.3) against:

$$
\chi.
$$

The time derivative and diffusion yield:

- endpoint filtered enstrophy;
- positive diffusion:

  $$
  P_{r,\ell}.
  $$

The transport and cutoff Laplacian terms are collected in:

$$
L_{r,\ell}.
$$

The subgrid forcing is bounded by:

$$
R_{r,\ell}.
$$

Hence one obtains the schematic rigorous local inequality:

$$
\boxed{
\mathcal E^\ell_{\rm out}
+
P_{r,\ell}
\le
\mathcal E^\ell_{\rm in}
+
V_{r,\ell}^+
+
R_{r,\ell}
+
L_{r,\ell},
}
\tag{22.1}
$$

where the endpoint quantities carry the scale normalization appropriate to the chosen cutoff.

Insert Theorem 19.1:

$$
\boxed{
\mathcal E^\ell_{\rm out}
+
P_{r,\ell}
\le
\mathcal E^\ell_{\rm in}
+
C(M,\sigma)
O_{r,\ell}
+
R_{r,\ell}
+
L_{r,\ell}.
}
\tag{22.2}
$$

This is a genuine filtered mechanism ledger.

It does not yet close because:

$$
O_{r,\ell}
$$

is not itself taxed.

---

# 23. Connection to direction-incoherence

The structural audit proposes a stronger target:

$$
\boxed{
V_{r,\ell}^+
\le
(1-\varepsilon_\ast)
P_{r,\ell}
+
C(M)
O_{r,\ell}
+
C\mathcal A_{r,\ell}
+
R_{r,\ell}
+
L_{r,\ell}.
}
\tag{23.1}
$$

The direction-incoherence defect:

$$
\mathcal A_{r,\ell}
$$

is designed to separate coherent Euler-like stretching from geometrically depleted stretching.

Theorem 19.1 does not need:

$$
\mathcal A.
$$

It is weaker and more elementary.

Its value is to identify that the residual hard object is already contained in:

$$
O_{r,\ell}.
$$

A direction theorem becomes useful only if it helps obtain a **strict diffusion coefficient** or a **scale-transition decay law** for:

$$
O.
$$

---

# 24. Coarse resolved badness and filtered vorticity

The source reduction theorem produces the branch:

$$
\Psi^\ell
\ge
c_\eta.
$$

The resolved coarse velocity:

$$
U^\ell
$$

is smooth at the relative scale:

$$
\sigma r.
$$

A large resolved coarse velocity contribution is therefore naturally linked to:

- the coarse filtered vorticity reservoir;
- the coarse pressure field;
- the low-frequency/mean velocity component.

The DCRP finite-window package already has pressure/trace channels for the latter two.

Thus a useful next resolution theorem should separate:

$$
\boxed{
\Psi^\ell
\text{ large}
}
$$

into:

$$
\boxed{
O_{r,\ell}\text{ large}
}
$$

or:

$$
\boxed{
\text{coarse pressure/mean/trace channel large}.
}
$$

Such a result would connect the old full-supply ledger to the new filtered-vorticity mechanism without attempting to call observation a tax.

This component estimate has not yet been proved in the present round.

---

# 25. Correct closure question

The old question was:

$$
\boxed{
\text{Can every critical supply event be detected?}
}
$$

The answer is increasingly close to yes after DCRP-08 through DCRP-18.

But this is not enough.

The correct question is:

$$
\boxed{
\textbf{
Can filtered coarse enstrophy remain scale-critically profitable
after diffusion and all explicit defect channels are accounted for?
}
}
\tag{25.1}
$$

Equivalently:

$$
\boxed{
\textbf{
can the three-dimensional stretching mechanism repeatedly rebuild
the coarse vorticity reservoir faster than diffusion removes it,
without producing subgrid/leakage/pressure/geometric defects?
}
}
\tag{25.2}
$$

This is the mechanism-level closure problem.

---

# 26. New primary frontier

The next exact target is:

$$
\boxed{
\textbf{
Filtered Enstrophy Sustenance / Stretching–Diffusion Depletion Lemma}.
}
$$

A useful two-part form is:

### Part A — strict stretching-diffusion estimate

For bounded normalized local energy:

$$
\Phi(z_0,r)\le M,
$$

and relative filter:

$$
\ell=\sigma r,
$$

prove:

$$
\boxed{
V_{r,\ell}^+
\le
(1-\varepsilon_\ast)
P_{r,\ell}
+
C(M)
O_{r,\ell}
+
D_{r,\ell}^{silent},
}
\tag{26.1}
$$

where:

$$
D_{r,\ell}^{silent}
$$

is explicitly controlled by already completed:

- subgrid forcing;
- localization leakage;
- pressure/tail;
- direction-incoherence;
- spatial/scale escape.

### Part B — scale-transition control of the coarse reservoir

Prove that if:

$$
D_{r,\ell}^{silent}
$$

is small and:

$$
O_{r,\ell}
$$

remains above a fixed critical threshold through many shrinking scales, then either:

$$
\boxed{
\sum
P_{r_k,\ell_k}
}
$$

has non-summable normalized size,

or a fixed positive-density set of scales violates Part A through one of the declared silent defects.

This second part is essential.

Without it:

$$
C(M)O
$$

can simply replace the old untaxed supply reservoir.

---

# 27. Why this is closer to a true coercive estimate

The old ledger used:

$$
\Phi,\Pi,C,D
$$

and tracked how badness can survive.

The filtered enstrophy ledger contains the actual three-dimensional competition:

$$
\boxed{
\text{vortex stretching}
\quad\text{vs}\quad
\text{vorticity diffusion}.
}
$$

This is no longer merely:

- a detector coefficient;
- a quotient distance;
- a transition bookkeeping term.

A strict inequality:

$$
V^+
<
P
+
\text{controlled errors}
$$

would directly remove the mechanism that can create small-scale vorticity.

This is why the route is now genuinely PDE-coercive.

---

# 28. Relation to DCRP supplier modules

The DCRP supplier modules are not discarded.

They become downstream certification.

If the filtered stretching mechanism produces:

- a subgrid-forcing defect;
- a pressure/flux event;
- a local supplier;
- a spatial/scale carrier;
- a transition residual;

then DCRP already supplies:

- local capture;
- PFET/backscatter decomposition;
- finite-window localization;
- finite trace separation;
- quotient/residual realization;
- two-sided scale completion.

Thus the revised order is:

$$
\boxed{
\begin{aligned}
&\text{filtered vorticity mechanism}\\
&\Longrightarrow
\text{stretching--diffusion depletion}\\
&\Longrightarrow
\text{bad-scale mechanism classification}\\
&\Longrightarrow
\text{DCRP finite-window certification/tax ledger}.
\end{aligned}
}
\tag{28.1}
$$

This is a change of order, not a restart.

---

# 29. Current proof-space status

The route has compressed from generic Navier--Stokes blowup to:

$$
\boxed{
\textbf{
a local scale-critical filtered-vorticity reservoir
that can repeatedly regenerate despite diffusion,
while all explicit subgrid/leakage/pressure/geometric channels remain small.
}
}
\tag{29.1}
$$

That is a much more specific survivor than the original:

$$
\text{generic diffuse carrier}.
$$

But it is also recognizably close to the central three-dimensional difficulty.

Therefore the current state should be described as:

$$
\boxed{
\text{mechanism frontier reached}
}
$$

rather than:

$$
\boxed{
\text{QED nearly finished}.
}
$$

---

# 30. Source-status audit

## Critical Ledgers and Scale-Defect Cascades

Primary facts used:

$$
\mathrm{Sup}^{full}
=
\theta^{-1}(\Phi+2\Pi)
+
C_{I,\theta}(\Phi+2\Pi)^{3/2}
+
C_P\theta^{-2}C,
$$

$$
\mathrm{Tax}^{full}
=
2E_{k+1}
+
(1-\alpha)A
+
(1-\alpha)C
+
\delta_DD,
$$

and the finite-scale survival alternative.

## Coarse-Grained Resolution and Pressure-Flux Work Depletion

Primary facts used:

$$
\Psi
\le
4\Psi^\ell+4\Omega^\ell,
$$

and the fixed-chain signed pressure-flux work depletion theorem.

## Structural Audit

Primary facts used:

- the existing architecture is obstruction calculus rather than a coercive regularity mechanism;
- direct single-scale domination by a signed work detector is not available unconditionally;
- the next PDE target is a filtered stretching-diffusion estimate;
- the correct weak-level object is filtered vorticity;
- the filtered vorticity identity includes the subgrid vorticity forcing:

  $$
  \mathcal J^\ell.
  $$

DCRP-19 independently proves the elementary fixed-relative-filter stretching bound (19.2).

---

# 31. End state

This round proves the **Critical Supply Source Reduction**:

$$
\boxed{
\left(
\mathrm{Sup}^{full}
-
\mathrm{Tax}^{full}
\right)_+
\ge\eta
}
$$

forces at least one of:

$$
\boxed{
\Phi\ge c_\eta,
}
$$

$$
\boxed{
\Pi\ge c_\eta,
}
$$

$$
\boxed{
\Psi^\ell\ge c_\eta,
}
$$

or:

$$
\boxed{
\Omega^\ell\ge c_\eta.
}
$$

It also proves the key NO-GO:

$$
\boxed{
\textbf{
observing all supply is not the same as taxing all supply.
}
}
$$

The new mechanism theorem is:

$$
\boxed{
V_{r,\sigma r}^+
\le
C
\sigma^{-5/2}
M^{1/2}
O_{r,\sigma r}.
}
$$

Thus fixed-relative filtered stretching is controlled by the filtered enstrophy reservoir.

The remaining closure-facing object is not a hidden detector.

It is:

$$
\boxed{
\textbf{
persistent coarse enstrophy regeneration against diffusion.
}
}
$$

The next single frontier is therefore:

$$
\boxed{
\textbf{
Filtered Enstrophy Sustenance / Stretching–Diffusion Depletion Lemma}.
}
$$

That is the next exact attack.