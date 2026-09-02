# NS-DCRP-20 — Filtered-Enstrophy Diffusion/IR Dichotomy and Far-Field-Only Survivor Reduction

- date: 2026-08-17
- status: research proof checkpoint
- canonical source: UTF-8 Markdown
- canonical math delimiters: `$...$` and `$$...$$`
- objective:
  1. audit DCRP-19 against the newer filtered-vorticity coercivity theorem;
  2. remove the lower-order filtered-enstrophy reservoir as a silent zero-cost mechanism by a spectral diffusion-versus-infrared dichotomy;
  3. combine near-field coercivity, commutator insertion, localization completion, and the new reservoir dichotomy;
  4. identify the final surviving filtered-vorticity mechanism.
- no full Navier--Stokes regularity claim is made.
- principal external primary source:
  - Runlong Yu, *Filtered Vortex Stretching and Subgrid Defects for the Three-Dimensional Navier--Stokes Equations*, arXiv:2606.27560v1.
- internal dependencies:
  - DCRP-18 two-sided relative-frequency completion;
  - DCRP-19 supply-source reduction and filtered-vorticity pivot;
  - MORP native-residual / paid-channel completion.
- no novelty / priority claim is made for results already contained in arXiv:2606.27560.

---

# 1. Executive result

DCRP-19 ended by proposing the filtered stretching--diffusion estimate

$$
V_{r,\ell}^{+}
\lesssim
(1-\varepsilon)P_{r,\ell}
+
C(M)O_{r,\ell}
+
\text{defects}.
$$

A source audit now shows that the near-field part of this target has already been proved in stronger form in arXiv:2606.27560.

For fixed relative filter length

$$
\ell=\sigma r,
$$

the paper proves

$$
\boxed{
V_{r,\ell}^{+,\mathrm{near}}
\le
(1-\varepsilon)
P_{r,\ell}^{\rho}
+
C_{\varepsilon,\sigma,\rho}
M_{r,\rho}(u)
O_{r,\ell}.
}
\tag{1.1}
$$

It also proves a derivative-compatible commutator insertion

$$
\boxed{
F_{r,\ell}^{\mathrm{com}}
\le
\eta P_{r,\ell}
+
C_{\eta,\varphi}
\widetilde{\mathcal S}_{r,\ell}^{(3)}
+
L_{r,\ell}^{\mathrm{com}}.
}
\tag{1.2}
$$

Thus DCRP-19's elementary estimate

$$
V^+\lesssim M^{1/2}O
$$

is retained only as a coarse fallback.

The stronger external theorem should be used for the proof program.

The unresolved lower-order term in (1.1) is the filtered-enstrophy reservoir

$$
O_{r,\ell}.
$$

The main new result of DCRP-20 is:

$$
\boxed{
\textbf{
positive filtered enstrophy}
\Longrightarrow
\textbf{
positive filtered diffusion/localization}
\ \vee\
\textbf{
relative infrared concentration}.
}
}
\tag{1.3}
$$

More precisely, let

$$
\eta_r(x)
=
\eta
\left(
\frac{x-x_0}{r}
\right)
$$

be a fixed smooth spatial cutoff and define

$$
f_{r,\ell}(x,t)
=
\eta_r(x)
\Omega_\ell(x,t).
$$

Let

$$
\boxed{
O_{r,\ell}^{\eta}
=
r^{-1}
\int_{I_r}
\|f_{r,\ell}(t)\|_2^2dt.
}
\tag{1.4}
$$

Whenever

$$
O_{r,\ell}^{\eta}>0,
$$

define the spacetime relative-frequency probability measure

$$
\boxed{
\mu_{r,\ell}(B)
=
\frac{
r^{-1}
\int_{I_r}
\int_{
\{\,\xi:\ r\xi\in B\,\}
}
|
\widehat{
f_{r,\ell}
}
(\xi,t)
|^2
d\xi dt
}{
O_{r,\ell}^{\eta}
}.
}
\tag{1.5}
$$

Then:

$$
\boxed{
\int_{\mathbb R^3}
|\zeta|^2
\,d\mu_{r,\ell}(\zeta)
\le
C
\frac{
\nu^{-1}P_{r,\ell}^{\eta}
+
L_{r,\ell}^{\omega}
}{
O_{r,\ell}^{\eta}
}.
}
\tag{1.6}
$$

Here:

$$
P_{r,\ell}^{\eta}
=
\nu r
\int_{I_r}
\int
\eta_r^2
|
\nabla\Omega_\ell
|^2
dxdt,
$$

and

$$
L_{r,\ell}^{\omega}
$$

is the normalized enstrophy mass on the fixed cutoff shell.

Consequently, if a sequence satisfies

$$
O_n^\eta\ge o_0>0,
$$

$$
P_n^\eta\to0,
$$

and:

$$
L_n^\omega\to0,
$$

then:

$$
\boxed{
\mu_n
\Longrightarrow
\delta_0.
}
\tag{1.7}
$$

In dyadic logarithmic relative-frequency coordinates:

$$
m
=
\log_2
(
r|\xi|
),
$$

this is exactly:

$$
\boxed{
m\to-\infty.
}
\tag{1.8}
$$

Therefore persistent coarse enstrophy with vanishing diffusion/localization is an **infrared relative-scale carrier**.

DCRP-18 already showed that transition-complete scale compactness must retain the

$$
-\infty
$$

direction.

Thus the lower-order reservoir is no longer a silent mechanism.

Quantitatively, if a sequence is uniformly non-infrared in the sense that there exist:

$$
\kappa>0,
\qquad
\delta>0
$$

with:

$$
\boxed{
\mu_n
(
\{
|\zeta|\ge\kappa
\}
)
\ge
\delta,
}
\tag{1.9}
$$

then:

$$
\boxed{
O_n^\eta
\le
\frac{
C
}{
\delta\kappa^2
}
\left(
\nu^{-1}P_n^\eta
+
L_n^\omega
\right).
}
\tag{1.10}
$$

Hence:

$$
\boxed{
\textbf{
no IR escape}
+
\textbf{
vanishing diffusion}
+
\textbf{
vanishing localization}
\Longrightarrow
O_n^\eta\to0.
}
\tag{1.11}
$$

This gives a zero-cost mechanism reduction.

Assume a normalized filtered-vorticity sequence satisfies:

$$
P_n\to0,
$$

$$
\widetilde{\mathcal S}_n^{(3)}\to0,
$$

$$
L_n\to0,
$$

$$
L_n^{\mathrm{com}}\to0,
$$

and has no infrared relative-scale defect.

Then:

$$
\boxed{
O_n\to0.
}
\tag{1.12}
$$

The external near-field theorem yields:

$$
\boxed{
V_n^{+,\mathrm{near}}\to0.
}
\tag{1.13}
$$

The external commutator insertion yields:

$$
\boxed{
F_n^{\mathrm{com}}\to0.
}
\tag{1.14}
$$

The principal localization residual may be canceled by the backward adjoint drift-diffusion cutoff, while the remaining shell localization terms are already included in:

$$
L_n,
\qquad
L_n^{\mathrm{com}}.
$$

Therefore every persistent positive filtered-enstrophy surplus must satisfy:

$$
\boxed{
\liminf_{n\to\infty}
V_n^{+,\mathrm{far}}
>
0.
}
\tag{1.15}
$$

Thus:

$$
\boxed{
\textbf{
zero-cost / no-IR filtered obstruction}
\Longrightarrow
\textbf{
far-field-strain-only survivor}.
}
}
\tag{1.16}
$$

This is the central reduction of DCRP-20.

The remaining mechanism is no longer generic vortex stretching.

The singular near-field stretching is diffusion-coercive.

The commutator term is increment-defect controlled.

The localization term is explicit.

The coarse-enstrophy reservoir is diffusion- or IR-controlled.

The only surviving positive mechanism is:

$$
\boxed{
\textbf{
external/far-field strain acting on the local filtered-vorticity core.
}
}
\tag{1.17}
$$

The next exact frontier is therefore:

$$
\boxed{
\textbf{
Far-Field Harmonic-Jet / Infrared-Strain Rigidity Lemma}.
}
\tag{1.18}
$$

The target is to show that persistent normalized far-field work must produce at least one of:

1. a nonzero two-sided infrared vorticity/strain carrier;
2. an unbounded or nontrivial finite-dimensional harmonic affine-strain jet;
3. a summable annular packing contribution;
4. a paid pressure/transition/localization residual.

If all four channels vanish, then:

$$
V_n^{+,\mathrm{far}}\to0,
$$

contradicting (1.15).

---

# 2. Source audit — DCRP-19 near-field target is already stronger externally

The main filtered-vorticity paper proves the exact near-field geometric depletion theorem:

$$
\boxed{
V_{r,\ell}^{+,\mathrm{near}}
\le
\frac{
3
}{
8\pi
}
\mathcal A_{r,\ell}^{\mathrm{pair}}.
}
\tag{2.1}
$$

The pairwise direction defect satisfies, for every:

$$
\eta>0,
$$

$$
\boxed{
\mathcal A_{r,\ell}^{\mathrm{pair}}
\le
\eta
P_{r,\ell}^{\rho}
+
C_\eta
M_{r,\rho}(u)
\left(
\frac r\ell
\right)^5
O_{r,\ell}.
}
\tag{2.2}
$$

Hence for:

$$
\ell=\sigma r,
$$

$$
\boxed{
V_{r,\sigma r}^{+,\mathrm{near}}
\le
(1-\varepsilon)
P_{r,\sigma r}^{\rho}
+
C_{\varepsilon}
M
\sigma^{-5}
O_{r,\sigma r}.
}
\tag{2.3}
$$

This is strictly stronger and more mechanism-specific than DCRP-19 Theorem 19.1.

Accordingly:

$$
\boxed{
\textbf{
DCRP-19's elementary stretching estimate is superseded for the near-field route.
}
}
\tag{2.4}
$$

It remains a simple independent fallback and scaling check.

---

# 3. Source audit — commutator forcing is already explicitly controlled

Let:

$$
R_\ell
=
S_\ell(u\otimes u)
-
U_\ell\otimes U_\ell.
$$

The filtered-vorticity commutator forcing is:

$$
-\nabla\times\nabla\cdot R_\ell.
$$

The external theorem proves, for:

$$
p\in[2,4],
$$

$$
\boxed{
F_k^{\mathrm{com}}
\le
\eta P_k
+
\frac{
C_{\mathrm{com}}^\sharp
}{
\eta
}
\widetilde{\mathcal S}_k^{(p)}
+
L_{k,\mathrm{inc}}^{\mathrm{com}}.
}
\tag{3.1}
$$

For the critical choice:

$$
p=3,
$$

$$
\boxed{
\widetilde{\mathcal S}^{(3)}
}
$$

is scale invariant.

This observable is already present in the MORP/DCRP extended cost architecture.

Therefore the commutator forcing does not need a new detector.

A zero-cost branch with:

$$
P_k\to0,
$$

$$
\widetilde{\mathcal S}_k^{(3)}\to0,
$$

and:

$$
L_{k,\mathrm{inc}}^{\mathrm{com}}\to0
$$

has:

$$
\boxed{
F_k^{\mathrm{com}}\to0.
}
\tag{3.2}
$$

---

# 4. The lower-order reservoir problem

After the singular near-field stretching is absorbed, the local filtered-enstrophy balance contains:

$$
\boxed{
C(M,\sigma)
O_{r,\ell}.
}
\tag{4.1}
$$

This term is not sign-indefinite work.

It is a lower-order reservoir.

It cannot be called:

- tax;
- leakage;
- backscatter.

If it persists while:

$$
P\to0,
$$

one must understand how its spectral mass avoids diffusion.

This is the new problem solved below.

---

# 5. Localized filtered-vorticity field

Fix a reference cutoff:

$$
\eta
\in
C_c^\infty(B_{1+\rho}),
$$

with:

$$
0\le\eta\le1,
$$

and:

$$
\eta\equiv1
$$

on:

$$
B_1.
$$

At scale:

$$
r,
$$

define:

$$
\boxed{
\eta_r(x)
=
\eta
\left(
\frac{
x-x_0
}{
r
}
\right).
}
\tag{5.1}
$$

Let:

$$
\Omega_\ell
=
\nabla\times S_\ell u,
$$

and define:

$$
\boxed{
f_{r,\ell}(x,t)
=
\eta_r(x)
\Omega_\ell(x,t).
}
\tag{5.2}
$$

Define:

$$
\boxed{
O_{r,\ell}^{\eta}
=
r^{-1}
\int_{I_r}
\|f_{r,\ell}(t)\|_2^2dt.
}
\tag{5.3}
$$

This is scale invariant.

---

# 6. Localized filtered diffusion and shell cost

Define:

$$
\boxed{
P_{r,\ell}^{\eta}
=
\nu r
\int_{I_r}
\int
\eta_r^2
|
\nabla\Omega_\ell
|^2
dxdt.
}
\tag{6.1}
$$

Let:

$$
A_\eta
=
\operatorname{supp}
\nabla\eta
$$

and define the physical shell:

$$
A_{\eta,r}
=
x_0+rA_\eta.
$$

Define the normalized filtered-enstrophy localization shell cost:

$$
\boxed{
L_{r,\ell}^{\omega}
=
r^{-1}
\int_{I_r}
\int_{A_{\eta,r}}
|
\Omega_\ell
|^2
dxdt.
}
\tag{6.2}
$$

Because:

$$
|\nabla\eta_r|
\le
C_\eta r^{-1},
$$

the cutoff-gradient term in:

$$
\nabla f_{r,\ell}
$$

is controlled by:

$$
L_{r,\ell}^{\omega}.
$$

---

# 7. Relative-frequency probability measure

Assume:

$$
O_{r,\ell}^{\eta}>0.
$$

For a Borel set:

$$
B\subset\mathbb R^3,
$$

define:

$$
\boxed{
\mu_{r,\ell}(B)
=
\frac{
r^{-1}
\int_{I_r}
\int_{\{
\xi:
r\xi\in B
\}}
|
\widehat f_{r,\ell}(\xi,t)
|^2
d\xi dt
}{
O_{r,\ell}^{\eta}
}.
}
\tag{7.1}
$$

By Plancherel:

$$
\boxed{
\mu_{r,\ell}
(
\mathbb R^3
)
=
1.
}
\tag{7.2}
$$

Thus:

$$
\mu_{r,\ell}
$$

is a probability measure on normalized relative-frequency space.

The normalized Fourier coordinate is:

$$
\boxed{
\zeta
=
r\xi.
}
\tag{7.3}
$$

---

# 8. NEW THEOREM — Relative-Frequency Second-Moment Bound

## Theorem 8.1

For every:

$$
O_{r,\ell}^{\eta}>0,
$$

$$
\boxed{
\int
|\zeta|^2
d\mu_{r,\ell}(\zeta)
\le
C_\eta
\frac{
\nu^{-1}
P_{r,\ell}^{\eta}
+
L_{r,\ell}^{\omega}
}{
O_{r,\ell}^{\eta}
}.
}
\tag{8.1}
$$

### Proof

By definition and Plancherel:

$$
\begin{aligned}
\int
|\zeta|^2
d\mu_{r,\ell}
&=
\frac{
r^{-1}
\int_{I_r}
\int
r^2
|\xi|^2
|
\widehat f_{r,\ell}
|^2
d\xi dt
}{
O_{r,\ell}^{\eta}
}\\
&=
\frac{
r
\int_{I_r}
\|
\nabla f_{r,\ell}(t)
\|_2^2dt
}{
O_{r,\ell}^{\eta}
}.
\end{aligned}
$$

Now:

$$
\nabla f_{r,\ell}
=
\eta_r
\nabla\Omega_\ell
+
(
\nabla\eta_r
)
\otimes
\Omega_\ell.
$$

Hence:

$$
|
\nabla f_{r,\ell}
|^2
\le
2
\eta_r^2
|
\nabla\Omega_\ell
|^2
+
2
|
\nabla\eta_r
|^2
|
\Omega_\ell
|^2.
$$

Multiply by:

$$
r
$$

and integrate.

The first term is:

$$
\le
2\nu^{-1}
P_{r,\ell}^{\eta}.
$$

The second term is:

$$
\le
2C_\eta
r^{-1}
\int_{I_r}
\int_{A_{\eta,r}}
|
\Omega_\ell
|^2
dxdt
=
2C_\eta
L_{r,\ell}^{\omega}.
$$

Absorb constants.

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

# 9. NEW THEOREM — Diffusion-or-Infrared Dichotomy

## Theorem 9.1

Let:

$$
(
u_n,
r_n,
\ell_n
)
$$

be a normalized sequence with fixed relative filter ratio:

$$
\ell_n
=
\sigma r_n.
$$

Assume:

$$
\boxed{
O_n^\eta
\ge
o_0
>
0.
}
\tag{9.1}
$$

Then either:

### positive diffusion/localization

there is:

$$
c_0>0
$$

such that along a subsequence:

$$
\boxed{
\nu^{-1}
P_n^\eta
+
L_n^\omega
\ge
c_0,
}
\tag{9.2}
$$

or:

### infrared concentration

$$
\boxed{
\mu_n
\Longrightarrow
\delta_0.
}
\tag{9.3}
$$

More quantitatively, if:

$$
\nu^{-1}
P_n^\eta
+
L_n^\omega
\to0,
$$

then for every:

$$
\kappa>0,
$$

$$
\boxed{
\mu_n
(
\{
|\zeta|\ge\kappa
\}
)
\to0.
}
\tag{9.4}
$$

### Proof

If (9.2) fails after subsequence extraction, then:

$$
\nu^{-1}
P_n^\eta
+
L_n^\omega
\to0.
$$

By Theorem 8.1 and:

$$
O_n^\eta\ge o_0,
$$

$$
\int
|\zeta|^2
d\mu_n
\to0.
$$

Markov's inequality gives:

$$
\mu_n
(
|\zeta|\ge\kappa
)
\le
\kappa^{-2}
\int
|\zeta|^2d\mu_n
\to0.
$$

Therefore:

$$
\mu_n
\Longrightarrow
\delta_0.
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

# 10. Dyadic interpretation — infrared escape

Let:

$$
m
=
\lfloor
\log_2
|\zeta|
\rfloor.
$$

For every fixed:

$$
M>0,
$$

the region:

$$
m\ge-M
$$

corresponds to:

$$
|\zeta|
\ge
2^{-M}.
$$

Under infrared concentration:

$$
\mu_n
\Longrightarrow
\delta_0,
$$

one has:

$$
\boxed{
\mu_n
(
m\ge-M
)
\to0
}
\tag{10.1}
$$

for every fixed:

$$
M.
$$

Equivalently:

$$
\boxed{
\text{all relative-frequency mass escapes through }
m\to-\infty.
}
\tag{10.2}
$$

This is exactly the missing infrared direction introduced in DCRP-18.

Thus:

$$
\boxed{
\textbf{
diffusion-silent filtered enstrophy is an IR scale carrier.
}
}
\tag{10.3}
$$

---

# 11. Quantitative non-IR coercivity

Suppose there exist:

$$
\kappa>0,
\qquad
\delta>0
$$

such that:

$$
\boxed{
\mu_{r,\ell}
(
|\zeta|\ge\kappa
)
\ge
\delta.
}
\tag{11.1}
$$

Then:

$$
\int
|\zeta|^2d\mu
\ge
\delta\kappa^2.
$$

Combine with Theorem 8.1:

$$
\delta\kappa^2
\le
C_\eta
\frac{
\nu^{-1}P^\eta
+
L^\omega
}{
O^\eta
}.
$$

Therefore:

$$
\boxed{
O^\eta
\le
\frac{
C_\eta
}{
\delta\kappa^2
}
\left(
\nu^{-1}P^\eta
+
L^\omega
\right).
}
\tag{11.2}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

This is a local scale-critical Poincare-type statement with the infrared sector made explicit rather than hidden in an uncontrolled mean mode.

---

# 12. Zero-cost reservoir elimination

Consider a normalized mechanism sequence satisfying:

$$
\boxed{
P_n^\eta\to0,
}
\tag{12.1}
$$

$$
\boxed{
L_n^\omega\to0,
}
\tag{12.2}
$$

and assume that the two-sided scale completion has no infrared defect.

The absence of an infrared defect means that the normalized relative-frequency measures cannot converge to:

$$
\delta_0
$$

while carrying a fixed positive absolute reservoir.

Therefore:

$$
\boxed{
O_n^\eta\to0.
}
\tag{12.3}
$$

Otherwise a subsequence with:

$$
O_n^\eta\ge o_0
$$

would trigger Theorem 9.1 and produce the prohibited IR carrier.

Status:

$$
\boxed{
\textbf{PROVED conditional only on explicit inclusion of the DCRP-18 infrared carrier in the native zero-cost package}.
}
$$

This is a package-completion condition already motivated independently by the scale-re-root audit.

---

# 13. Near-field stretching vanishes on a zero-cost/no-IR branch

The external near-field theorem gives:

$$
\boxed{
V_n^{+,\mathrm{near}}
\le
(1-\varepsilon)
P_n^\rho
+
C_{\varepsilon,\sigma,\rho}
M_n
O_n.
}
\tag{13.1}
$$

Assume:

$$
\sup_nM_n<\infty.
$$

If:

$$
P_n^\rho\to0
$$

and:

$$
O_n\to0,
$$

then:

$$
\boxed{
V_n^{+,\mathrm{near}}
\to0.
}
\tag{13.2}
$$

Thus the singular near-field stretching term cannot survive a zero-diffusion, zero-IR obstruction.

Status:

$$
\boxed{
\textbf{PROVED using arXiv:2606.27560}.
}
$$

---

# 14. Commutator forcing vanishes on the same branch

The external commutator insertion gives:

$$
F_n^{\mathrm{com}}
\le
\eta P_n
+
C_\eta
\widetilde{\mathcal S}_n^{(3)}
+
L_n^{\mathrm{com}}.
$$

If:

$$
P_n\to0,
$$

$$
\widetilde{\mathcal S}_n^{(3)}\to0,
$$

and:

$$
L_n^{\mathrm{com}}\to0,
$$

then:

$$
\boxed{
F_n^{\mathrm{com}}
\to0.
}
\tag{14.1}
$$

Status:

$$
\boxed{
\textbf{PROVED using arXiv:2606.27560}.
}
$$

---

# 15. Localization module

The filtered-enstrophy identity contains the cutoff residual:

$$
L_n.
$$

The external theorem proves that the principal cutoff residual vanishes identically if the cutoff solves the backward adjoint drift-diffusion equation:

$$
\boxed{
\partial_t\chi
+
\Delta\chi
+
U_\ell\cdot\nabla\chi
=
0.
}
\tag{15.1}
$$

The remaining shell costs generated by enlarged diffusion and commutator integration by parts are explicit nonnegative localization budgets.

Therefore the zero-localization branch satisfies:

$$
\boxed{
L_n
+
L_n^{\mathrm{com}}
\to0.
}
\tag{15.2}
$$

No hidden principal localization term remains.

---

# 16. Filtered enstrophy surplus

Let:

$$
E_{n,\mathrm{in}}^\omega,
\qquad
E_{n,\mathrm{out}}^\omega
$$

be the normalized endpoint filtered-enstrophy terms.

Let:

$$
P_n
$$

be filtered diffusion.

The external localized balance yields:

$$
\boxed{
E_{n,\mathrm{out}}^\omega
+
P_n
\le
E_{n,\mathrm{in}}^\omega
+
V_n^{+,\mathrm{near}}
+
V_n^{+,\mathrm{far}}
+
F_n^{\mathrm{com}}
+
L_n.
}
\tag{16.1}
$$

After choosing the near-field and commutator diffusion fractions, define the post-coercive positive surplus:

$$
\boxed{
\mathfrak B_n
=
\left[
E_{n,\mathrm{out}}^\omega
+
(1-\eta_{\mathrm{near}}-\eta_{\mathrm{com}})
P_n
-
E_{n,\mathrm{in}}^\omega
-
C_{\eta,\sigma}M_nO_n
-
L_n
-
L_n^{\mathrm{com}}
\right]_+.
}
\tag{16.2}
$$

The external theorem shows:

$$
\boxed{
\mathfrak B_n
\le
V_n^{+,\mathrm{far}}
+
C_{\eta}
\widetilde{\mathcal S}_n^{(3)}.
}
\tag{16.3}
$$

up to the explicit shell/localization terms already displayed.

---

# 17. NEW THEOREM — Far-Field-Only Survivor Reduction

## Theorem 17.1

Let a normalized filtered-vorticity sequence satisfy:

$$
\boxed{
\inf_n
\mathfrak B_n
\ge
b_0>0.
}
\tag{17.1}
$$

Assume:

$$
\boxed{
P_n\to0,
}
\tag{17.2}
$$

$$
\boxed{
\widetilde{\mathcal S}_n^{(3)}
\to0,
}
\tag{17.3}
$$

$$
\boxed{
L_n
+
L_n^{\mathrm{com}}
+
L_n^\omega
\to0,
}
\tag{17.4}
$$

$$
\boxed{
\sup_nM_n<\infty,
}
\tag{17.5}
$$

and the two-sided relative-frequency package has no infrared filtered-enstrophy defect.

Then:

$$
\boxed{
O_n\to0,
}
\tag{17.6}
$$

$$
\boxed{
V_n^{+,\mathrm{near}}\to0,
}
\tag{17.7}
$$

$$
\boxed{
F_n^{\mathrm{com}}\to0,
}
\tag{17.8}
$$

and necessarily:

$$
\boxed{
\liminf_{n\to\infty}
V_n^{+,\mathrm{far}}
\ge
b_0.
}
\tag{17.9}
$$

### Proof

The reservoir elimination theorem gives:

$$
O_n\to0.
$$

The external near-field coercivity then gives:

$$
V_n^{+,\mathrm{near}}\to0.
$$

The external commutator insertion gives:

$$
F_n^{\mathrm{com}}\to0.
$$

The localization terms vanish by assumption.

The balance inequality defining:

$$
\mathfrak B_n
$$

therefore leaves only:

$$
V_n^{+,\mathrm{far}}
$$

as a nonvanishing positive source.

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

# 18. Interpretation

The zero-cost survivor has now lost the following mechanisms.

### singular near-field stretching

Closed by geometric depletion plus diffusion.

### filtered-enstrophy reservoir

Closed by:

$$
\text{diffusion}
\ \vee\
\text{IR scale carrier}.
$$

### commutator forcing

Closed by:

$$
P
+
\widetilde{\mathcal S}^{(3)}
+
L^{\mathrm{com}}.
$$

### principal localization

Closed by the backward adjoint drift-diffusion cutoff.

### shell localization

Explicitly retained as:

$$
L^\omega,
\qquad
L^{\mathrm{com}}.
$$

Therefore the only remaining positive filtered mechanism is:

$$
\boxed{
\textbf{
far-field strain}.
}
$$

This is a substantial reduction.

---

# 19. Why far-field strain is structurally different

The singular near-field strain depends on vorticity at relative distance:

$$
O(r)
$$

and carries the Calderon--Zygmund singularity.

The far-field strain is generated by vorticity outside the core.

On the core it acts as a slowly varying external deformation.

The external filtered-vorticity paper gives two descriptions.

### annular packing

The contribution of larger spatial annuli is reassigned to coarser scales with geometric weights.

### fixed-source harmonic route

After replacing moving shells by fixed annular source partitions centered at the singular point, each exterior-source strain field is harmonic in the smaller core.

After subtracting its affine Taylor jet, higher-order terms gain powers of scale separation.

Thus the unresolved far-field object is essentially:

$$
\boxed{
\text{recurrent low-order harmonic strain jets across nested scales}.
}
\tag{19.1}
$$

---

# 20. Elementary far-field amplitude test

Define the scale-normalized far-field strain amplitude:

$$
\boxed{
J_{r,\ell}^{\mathrm{far}}
=
r^2
\left\|
S_\ell^{\mathrm{far}}
\right\|_{
L^\infty(Q_r)
}.
}
\tag{20.1}
$$

Then directly:

$$
\begin{aligned}
V_{r,\ell}^{+,\mathrm{far}}
&=
r
\iint
\chi
(
S_\ell^{\mathrm{far}}
\Omega_\ell\cdot\Omega_\ell
)_+
\\
&\le
r
\|
S_\ell^{\mathrm{far}}
\|_\infty
\iint
\chi
|
\Omega_\ell
|^2
\\
&=
J_{r,\ell}^{\mathrm{far}}
O_{r,\ell}.
\end{aligned}
$$

Hence:

$$
\boxed{
V_{r,\ell}^{+,\mathrm{far}}
\le
J_{r,\ell}^{\mathrm{far}}
O_{r,\ell}.
}
\tag{20.2}
$$

Therefore a far-field-only survivor with:

$$
O_n\to0
$$

and:

$$
V_n^{+,\mathrm{far}}\ge b_0
$$

must satisfy:

$$
\boxed{
J_n^{\mathrm{far}}
\to\infty.
}
\tag{20.3}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

Thus the far-field-only survivor is not merely "some external strain."

It is an **unbounded normalized far-field strain amplification**.

This is a new concrete obstruction coordinate.

---

# 21. Native meaning of the far-field amplification

The quantity:

$$
J_{r,\ell}^{\mathrm{far}}
$$

is:

- generated directly from filtered Navier--Stokes vorticity;
- scale normalized;
- independent of a copied singularity label;
- spatially external to the core;
- naturally associated with the harmonic exterior-source strain jet.

Therefore:

$$
\boxed{
J^{\mathrm{far}}\to\infty
}
$$

is a legitimate native noncompactness defect.

It should be retained in a transition-complete package as:

$$
\boxed{
\mathsf R_{\rm farjet}.
}
\tag{21.1}
$$

This does not yet eliminate the branch.

A hypothetical singular solution may genuinely generate diverging normalized external strain.

The point is that the survivor is now explicit.

---

# 22. Why the external weighted far-field estimate is not enough

The existing energy-level theorem yields:

$$
V_k^{+,\mathrm{far}}
\lesssim
M_E^{3/2}
2^{3k/2}.
$$

This is only summable against strongly decaying weights.

The annular reassignment improves the structure to:

$$
\boxed{
\mu_k^{\mathrm{far,ann}}
\lesssim
\sum_{j=0}^{k}
2^{-(k-j)}
\mathfrak A_j
\mathcal Q_k.
}
\tag{22.1}
$$

But bounded:

$$
\mathfrak A_j,
\qquad
\mathcal Q_k
$$

still allows:

$$
\mu_k\sim1
$$

at every scale.

Thus no unconditional unweighted Carleson summability follows from the current shell estimate.

This is a genuine remaining issue.

---

# 23. Two possible closure routes for far-field strain

The reduction suggests two distinct attacks.

## Route A — annular IR coupling

Show that:

$$
J_n^{\mathrm{far}}\to\infty
$$

or persistent:

$$
V_n^{+,\mathrm{far}}
$$

forces a nonzero two-sided infrared vorticity/strain carrier on outer relative scales.

Then DCRP-18's IR completion would absorb the far-field survivor into the already existing scale-defect channel.

## Route B — harmonic affine-jet rigidity

Use a fixed exterior annular partition.

For each outer source scale:

$$
j<k,
$$

the induced strain field on the smaller core is harmonic.

Write:

$$
\boxed{
H_{j,k}(x,t)
=
A_{j,k}(t)
+
B_{j,k}(t)
(
x-x_0
)
+
R_{j,k}^{(2)}(x,t).
}
\tag{23.1}
$$

Harmonic interior estimates give extra powers of:

$$
r_k/r_j
$$

for:

$$
R_{j,k}^{(2)}.
$$

Thus only the finite-dimensional low-order jet:

$$
\boxed{
(
A_{j,k},
B_{j,k}
)
}
\tag{23.2}
$$

can recur without geometric scale gain.

The target is to show that a persistent positive affine-strain jet must:

- be visible in a finite-dimensional native trace;
- generate a positive deformation/depletion tax;
- or correspond to a nonzero IR carrier.

This is the more geometric route.

---

# 24. New exact frontier

The next target is:

$$
\boxed{
\textbf{
Far-Field Harmonic-Jet / Infrared-Strain Rigidity Lemma}.
}
$$

A useful statement is:

> Let:
>
> $$
> \mathfrak B_n\ge b_0>0
> $$
>
> be a persistent post-near-field filtered-enstrophy surplus.
>
> Assume:
>
> $$
> P_n,
> \widetilde{\mathcal S}_n^{(3)},
> L_n,
> L_n^{\mathrm{com}},
> L_n^\omega
> \to0,
> $$
>
> and assume there is no UV/IR/spatial native carrier defect except possibly the exterior harmonic strain.
>
> Then prove that the fixed-source far-field harmonic jets satisfy:
>
> $$
> \boxed{
> \mathsf J_n^{aff}
> \ge
> c>0
> }
> $$
>
> on a positive-density set of scales.
>
> Next prove:
>
> $$
> \boxed{
> \text{persistent affine jet}
> \Longrightarrow
> \text{IR strain carrier}
> \ \vee\
> \text{paid deformation}
> \ \vee\
> \text{rigid removable mode}.
> }
> $$

If all three right-hand channels are zero, the far-field survivor vanishes.

This is now the single mechanism frontier.

---

# 25. Relation to the earlier supplier route

The supplier route remains useful.

If the far-field affine strain genuinely amplifies the local vorticity core until a local shell crosses the dissipation threshold, DCRP-16 produces a local supplier.

Then DCRP-14/15 attach:

$$
\text{finite trace}
\ \vee\
\text{finite-window residual}.
$$

DCRP-18 tracks re-root IR escape.

Thus the far-field mechanism cannot generate supplier events and then disappear from the audit.

The remaining issue is the **pre-supplier sustaining regime**:

can an external harmonic strain keep feeding the core across infinitely many scales without itself becoming an IR/native defect or paying a deformation tax?

That is exactly the next question.

---

# 26. Corrected proof-state diagram

The current filtered-vorticity route is:

$$
\boxed{
\begin{aligned}
\text{persistent local badness}
&\Longrightarrow
\text{positive filtered-enstrophy surplus}\\
&\Longrightarrow
\text{near-field}
\vee
\text{far-field}
\vee
\text{commutator}
\vee
\text{localization}\\
&\Longrightarrow
\text{diffusion/IR}
\vee
\text{far-field}
\vee
\widetilde{\mathcal S}^{(3)}
\vee
\text{local residual}.
\end{aligned}
}
\tag{26.1}
$$

On a zero-cost/no-IR branch:

$$
\boxed{
\text{only far-field strain survives}.
}
\tag{26.2}
$$

If the local filtered-enstrophy reservoir itself remains positive while diffusion vanishes, it is no longer a separate mechanism.

It is an IR defect.

This closes the reservoir loophole identified in DCRP-19.

---

# 27. Source-status map

## Already proved externally

From arXiv:2606.27560:

- near-field geometric depletion;
- pairwise direction-defect coercivity;
- strict diffusion insertion for near-field stretching;
- exact localized filtered-enstrophy identity;
- adjoint cancellation of the principal localization residual;
- far-field weighted packing;
- annular reassignment;
- conditional unweighted Carleson closure;
- derivative-compatible commutator estimate;
- commutator insertion into diffusion plus:

  $$
  \widetilde{\mathcal S}^{(p)};
  $$

- cylindrical Young-profile extraction for bounded critical commutator defects.

## Proved in DCRP-20

- localized relative-frequency probability measure for filtered enstrophy;
- second-moment diffusion/localization bound;
- diffusion-or-IR dichotomy;
- quantitative non-IR coercivity;
- zero-cost filtered-enstrophy reservoir elimination;
- far-field-only survivor reduction;
- normalized far-field strain amplification consequence:

  $$
  O_n\to0,
  \quad
  V_n^{far}\ge b_0
  \Longrightarrow
  J_n^{far}\to\infty.
  $$

## Still open

- unconditional far-field harmonic/annular closure;
- affine-jet rigidity;
- persistent commutator Young-profile recurrence if:

  $$
  \widetilde{\mathcal S}^{(3)}
  $$

  is allowed nonzero rather than assigned positive cost;
- full integration back into the singularity-to-MORP contradiction.

---

# 28. End state

The main new theorem is:

$$
\boxed{
\int
|\zeta|^2d\mu_{r,\ell}
\le
C
\frac{
\nu^{-1}P_{r,\ell}^{\eta}
+
L_{r,\ell}^{\omega}
}{
O_{r,\ell}^{\eta}
}.
}
$$

Therefore:

$$
\boxed{
O\ge o_0,
\quad
P\to0,
\quad
L^\omega\to0
\Longrightarrow
\text{IR relative-frequency escape}.
}
$$

If IR escape is prohibited by the completed native package:

$$
\boxed{
P\to0,
\quad
L^\omega\to0
\Longrightarrow
O\to0.
}
$$

Using the stronger external near-field and commutator theorems:

$$
\boxed{
\textbf{
zero-cost/no-IR filtered mechanism}
\Longrightarrow
\textbf{
far-field-strain-only survivor}.
}
$$

Moreover, if a positive far-field surplus persists while:

$$
O\to0,
$$

then:

$$
\boxed{
r^2
\|
S^{far}
\|_\infty
\to\infty.
}
$$

Thus the next single frontier is:

$$
\boxed{
\textbf{
Far-Field Harmonic-Jet / Infrared-Strain Rigidity Lemma}.
}
$$

The proof space has now reached a very specific external-strain obstruction.