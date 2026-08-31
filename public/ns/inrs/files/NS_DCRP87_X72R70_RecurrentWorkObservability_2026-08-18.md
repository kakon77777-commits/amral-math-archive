# DCRP87 / X72-R70 — Recurrent Work-Silent Rigidity and Compact Coarse Observability

**Series:** Independent Navier–Stokes Research Series / X72 Bridge  
**Date:** 2026-08-18  
**Status:** Proof-development checkpoint / resolved-badness-to-work observability round  
**Immediate predecessor:** `NS_DCRP86_X72R69_HardyAnnularization_OneComponentWorkGap_2026-08-18.md`

**Primary internal dependencies**
- DCRP31 — native inward PFET / native bounded-reservoir geometry
- DCRP62–79 — recurrent pressure/tilt equality closures
- DCRP86 — disjoint one-component shell debt / work-observability bottleneck

**Fresh primary-source calibration**
- Runlong Yu, *Coarse-Grained Resolution and Pressure-Flux Work Depletion for Navier-Stokes CKN Badness*, arXiv:2606.25322v1.
- Runlong Yu, *Finite-Chain CKN-Bad Scale Counting for Navier-Stokes: Standard PDE Closure and Canonical Detector Realization*, arXiv:2606.21783.
- Runlong Yu, *A Structural Audit of Navier-Stokes Obstruction Calculus*, arXiv:2606.25341.

The first source proves:

\[
\Psi(r)
\le
4\Psi^\ell(r)+4\Omega^\ell(r),
\]

and an exact finite-chain signed work-depletion theorem for:

\[
\boxed{
G^\ell
=
\Pi^\ell+\nabla\cdot(P^\ell U^\ell),
\qquad
\Pi^\ell=-R^\ell:\nabla U^\ell.
}
\]

It explicitly leaves open the implication:

\[
\Psi^\ell\ge c_0
\Longrightarrow
\text{nonzero finite signed-work detector},
\]

because of possible:

- pressure–flux cancellation;
- harmonic pressure tails;
- coherent low-frequency resolved profiles;
- leakage;
- backscatter;
- subfilter residual concentration.

DCRP87 does **not** prove this implication on the full class of suitable weak solutions.

It proves it on the much narrower **same-parent recurrent compact class** produced by the present Type-II/X72 program after the previously declared escape coordinates are removed.

No full Navier–Stokes regularity theorem is claimed.

---

# 0. Executive result

DCRP86 reduced the late forest problem to:

\[
\boxed{
\text{resolved CKN badness}
\stackrel{?}{\Longrightarrow}
\text{signed pressure–flux work}
}
\]

after:

- subfilter residuals;
- critical-reservoir escape;
- material noncompactness;
- relative-scale escape;
- Kelvin/trace defects

have been explicitly retained.

DCRP87 proves a compact recurrent observability theorem.

The core exact identity is elementary but decisive.

For the coarse Navier–Stokes package:

\[
\boxed{
\partial_tU
-
\Delta U
+
\nabla\cdot(U\otimes U)
+
\nabla P
=
-\nabla\cdot R,
\qquad
\nabla\cdot U=0,
}
\tag{0.1}
\]

define:

\[
\boxed{
K=\frac12|U|^2,
}
\]

\[
\boxed{
\Pi=-R:\nabla U,
}
\]

and:

\[
\boxed{
G=\Pi+\nabla\cdot(PU).
}
\]

Then:

## Exact resolved energy equation

\[
\boxed{
\partial_tK
-
\Delta K
+
|\nabla U|^2
+
\nabla\cdot(KU+RU)
+
G
=
0.
}
\tag{0.2}
\]

Thus if:

1. \(G\) is distributionally silent;
2. the same-parent localized kinetic energy returns;
3. localization leakage vanishes;

then:

\[
\boxed{
\int\phi|\nabla U|^2=0.
}
\]

Hence:

\[
\boxed{
\nabla U=0
}
\]

on the active interior.

So every work-silent recurrent resolved limit is spatially constant:

\[
\boxed{
U(x,t)=a(t).
}
\]

If the subfilter residual also vanishes, then the fine velocity collapses to the same constant resolved velocity and:

\[
R=0.
\]

The momentum equation gives:

\[
\boxed{
P(x,t)
=
-a'(t)\cdot x+c(t).
}
\]

Thus the only compact recurrent work-silent profile is the exact bulk-translation / affine-harmonic-pressure mode already encountered in D75.

But the native global profile branch satisfies the Morrey law:

\[
\boxed{
\int_{B_R}|U(y,t)|^2dy
\le
CM_0R.
}
\tag{0.3}
\]

For:

\[
U=a(t),
\]

the left side is:

\[
\asymp
|a(t)|^2R^3.
\]

Therefore:

\[
\boxed{
a(t)=0.
}
\]

Then:

\[
\nabla P=0.
\]

Hence:

\[
\boxed{
\Psi^\ell=0.
}
\]

This contradicts any persistent positive resolved-badness floor.

Therefore:

# Main theorem — compact recurrent work observability

On a sequentially compact same-parent resolved class satisfying:

- native Morrey control;
- same-parent endpoint return;
- vanishing localization leakage;
- vanishing subfilter residual;

one has:

\[
\boxed{
\Psi^\ell\ge b_0>0
\Longrightarrow
A^\infty(G)\ge c_{\rm obs}>0.
}
\tag{0.4}
\]

Here \(A^\infty\) is any sufficiently rich normalized distributional test seminorm that separates nonzero \(G\).

By compactness this infinite test family can be reduced to a **finite** active test family.

Thus the missing coarse observability implication is closed on this recurrent compact subclass.

---

# 1. Exact resolved-energy identity

Start from:

\[
\partial_tU
-
\Delta U
+
(U\cdot\nabla)U
+
\nabla P
=
-\nabla\cdot R.
\]

Dot with \(U\).

Use:

\[
U\cdot\partial_tU
=
\partial_tK,
\]

\[
-U\cdot\Delta U
=
-\Delta K+|\nabla U|^2,
\]

\[
U\cdot(U\cdot\nabla U)
=
\nabla\cdot(KU),
\]

\[
U\cdot\nabla P
=
\nabla\cdot(PU),
\]

and:

\[
-U\cdot\nabla\cdot R
=
-\nabla\cdot(RU)+R:\nabla U.
\]

Since:

\[
R:\nabla U=-\Pi,
\]

we obtain:

## Theorem D87.1 — Exact Coarse Energy Equation

\[
\boxed{
\partial_tK
-
\Delta K
+
|\nabla U|^2
+
\nabla\cdot(KU+RU)
+
G
=
0.
}
\tag{1.1}
\]

No sign approximation is involved.

---

# 2. Localized identity

Let:

\[
\phi\ge0
\]

be a smooth cutoff supported in an interior coarse cylinder.

Integrate (1.1) over:

\[
I=[t_-,t_+].
\]

Define:

\[
\boxed{
E_\phi(t)
=
\int\phi(x,t)K(x,t)\,dx.
}
\]

Define:

\[
\boxed{
D_\phi
=
\int_I\int\phi|\nabla U|^2dxdt.
}
\]

Define combined work:

\[
\boxed{
W_\phi
=
\langle G,\phi\rangle.
}
\]

Define localization leakage:

\[
\boxed{
\begin{aligned}
L_\phi
={}&
\int_I\int
K(\partial_t\phi+\Delta\phi)
\\
&+
(KU+RU)\cdot\nabla\phi
\,dxdt.
\end{aligned}
}
\tag{2.1}
\]

Then:

## Theorem D87.2 — Exact Recurrent Work Ledger

\[
\boxed{
E_\phi(t_+)
-
E_\phi(t_-)
+
D_\phi
+
W_\phi
=
L_\phi.
}
\tag{2.2}
\]

This is the exact resolved-energy identity in the sign convention used here.

---

# 3. Work-silent recurrence forces zero resolved dissipation

Assume:

\[
\boxed{
E_\phi(t_+)=E_\phi(t_-),
}
\tag{3.1}
\]

\[
\boxed{
L_\phi=0,
}
\tag{3.2}
\]

and:

\[
\boxed{
G=0
}
\]

distributionally on the support of \(\phi\).

Then:

\[
W_\phi=0.
\]

Equation (2.2) becomes:

\[
D_\phi=0.
\]

Hence:

## Theorem D87.3 — Work-Silent Recurrent Rigidity

\[
\boxed{
\nabla U=0
}
\]

almost everywhere wherever:

\[
\phi>0.
\]

Therefore on each connected active interior region:

\[
\boxed{
U(x,t)=a(t).
}
\tag{3.3}
\]

Pressure–flux cancellation cannot support a nontrivial recurrent resolved gradient if the total combined work, leakage, and endpoint defect are all silent.

---

# 4. Why individual pressure/flux cancellation does not rescue recurrence

The coarse-work source defines:

\[
\mathcal F[\phi]
=
\int\phi\Pi,
\]

and:

\[
\mathcal P[\phi]
=
-\int PU\cdot\nabla\phi,
\]

so:

\[
W_\phi
=
\mathcal F[\phi]
+
\mathcal P[\phi].
\]

It also defines the nonnegative cancellation ledger:

\[
\boxed{
\mathcal C^{PF}[\phi]
=
|\mathcal F[\phi]|
+
|\mathcal P[\phi]|
-
|W_\phi|.
}
\]

Large individual channels may cancel.

But if the **combined** distribution \(G\) is actually silent on a recurrent leakage-free limit, D87.3 still forces:

\[
\nabla U=0.
\]

Therefore:

## Corollary D87.4 — Cancellation Is Not a Recurrent Strong Equality Mode

\[
\boxed{
G=0
+
\text{return}
+
\text{zero leakage}
\Longrightarrow
\nabla U=0.
}
\]

Pressure–flux cancellation may be large as a ledger coordinate, but it cannot hide a nontrivial recurrent resolved strain field at zero total work.

---

# 5. Insert the vanishing subfilter residual

Let:

\[
u_n,
\quad
U_n^\ell
\]

be a same-parent sequence with:

\[
\Omega_n^\ell\to0.
\]

The velocity part of the coarse residual implies:

\[
u_n-U_n^\ell\to0
\]

locally in the critical \(L^3\) topology.

Suppose the compact limit satisfies:

\[
\nabla U=0.
\]

Then:

\[
U=a(t).
\]

Hence:

\[
u_n\to a(t)
\]

locally in \(L^3\).

The Reynolds stress satisfies the standard bound:

\[
\|R_n^\ell\|_{L^{3/2}}
\le
2
\|u_n\|_{L^3}^2.
\]

More importantly, after subtracting the common spatial constant \(a(t)\), the fluctuation converges to zero.

Thus:

## Theorem D87.5 — Residual-Silent Constant Limit Has Zero SGS Stress

\[
\boxed{
R_n^\ell\to0
}
\]

locally in \(L^{3/2}\).

Therefore in the limit:

\[
\boxed{
R=0.
}
\tag{5.1}
\]

---

# 6. The only work-silent residual-free coarse profile

With:

\[
U=a(t),
\qquad
R=0,
\]

the coarse momentum equation becomes:

\[
a'(t)+\nabla P=0.
\]

Therefore:

## Theorem D87.6 — Affine-Pressure Translation Normal Form

\[
\boxed{
P(x,t)
=
-a'(t)\cdot x+c(t).
}
\tag{6.1}
\]

The pressure is harmonic and affine in space.

This is exactly the coarse analogue of the bulk-translation / affine-pressure mode already isolated in the material-packet analysis.

---

# 7. Native Morrey kills the nonzero translation mode

The native strict Type-II profile branch satisfies:

\[
\boxed{
\int_{B_R}
|U(y,t)|^2dy
\le
CM_0R
}
\]

for all large \(R\) in the relevant similarity/global profile variables.

If:

\[
U=a(t),
\]

then:

\[
\int_{B_R}|U|^2
=
|a(t)|^2|B_1|R^3.
\]

Thus:

\[
|a(t)|^2R^3
\lesssim
R.
\]

Let:

\[
R\to\infty.
\]

Therefore:

## Theorem D87.7 — Native Elimination of Work-Silent Bulk Translation

\[
\boxed{
a(t)=0.
}
\tag{7.1}
\]

Then:

\[
\nabla P=0.
\]

So the projected pressure badness vanishes.

Therefore:

\[
\boxed{
\Psi^\ell=0.
}
\tag{7.2}
\]

---

# 8. Contradiction theorem

Assume a sequence of normalized same-parent resolved packages satisfies:

\[
\boxed{
\Psi_n^\ell\ge b_0>0,
}
\tag{8.1}
\]

and:

\[
\boxed{
\Omega_n^\ell\to0,
}
\tag{8.2}
\]

\[
\boxed{
E_{n,\phi}(t_+)-E_{n,\phi}(t_-)\to0,
}
\tag{8.3}
\]

\[
\boxed{
L_{n,\phi}\to0,
}
\tag{8.4}
\]

and:

\[
\boxed{
G_n^\ell\to0
}
\]

distributionally on every compactly supported active test.

Assume also:

- sequential compactness of the normalized package;
- the native global Morrey bound passes to the limit.

Take a convergent subsequence.

The limit satisfies:

\[
G=0.
\]

D87.3 gives:

\[
\nabla U=0.
\]

D87.5–7 give:

\[
U=0,
\qquad
\nabla P=0.
\]

Hence:

\[
\Psi^\ell=0,
\]

contradicting:

\[
\Psi^\ell\ge b_0.
\]

Therefore:

## Theorem D87.8 — No Recurrent Work-Invisible Resolved-Bad Limit

The above collection of properties is impossible.

---

# 9. Infinite-test observability gap

Let:

\[
\mathfrak X
\]

be a bounded test class in:

\[
C_c^\infty(Q_1)
\]

that separates distributions.

Define:

\[
\boxed{
A^\infty(G)
=
\sup_{
\psi\in\mathfrak X
}
|\langle G,\psi\rangle|.
}
\tag{9.1}
\]

On a compact normalized recurrent class satisfying:

- \(\Psi^\ell\ge b_0\);
- native Morrey;
- residual bound:
  \[
  \Omega^\ell\le\delta;
  \]
- endpoint return defect:
  \[
  \mathcal R_{\rm ret}\le\delta;
  \]
- localization leakage:
  \[
  \mathcal R_{\rm leak}\le\delta;
  \]

the contradiction theorem gives:

## Theorem D87.9 — Compact Recurrent Coarse Observability

For sufficiently small:

\[
\delta=\delta(b_0,M_0),
\]

there exists:

\[
\boxed{
c_{\rm obs}
=
c_{\rm obs}(b_0,M_0,\mathcal K)
>0
}
\]

such that:

\[
\boxed{
A^\infty(G)
\ge
c_{\rm obs}.
}
\tag{9.2}
\]

This is the desired resolved-badness-to-work observability implication on the recurrent compact subclass.

It is an existence theorem, not an explicit numerical constant.

---

# 10. Finite-dimensional reduction by compactness

The source depletion theorem requires a **finite** active family.

D87 can supply one.

For every package:

\[
X\in\mathcal K
\]

with:

\[
A^\infty(G_X)\ge c_{\rm obs},
\]

choose:

\[
\psi_X\in\mathfrak X
\]

such that:

\[
|\langle G_X,\psi_X\rangle|
\ge
\frac34c_{\rm obs}.
\]

Continuity of the pairing gives an open neighborhood:

\[
\mathcal U_X
\]

where:

\[
|\langle G_Y,\psi_X\rangle|
\ge
\frac12c_{\rm obs}.
\]

Compactness yields a finite subcover:

\[
\mathcal U_{X_1},
\ldots,
\mathcal U_{X_m}.
\]

Therefore:

## Theorem D87.10 — Finite Active Test Compiler

There exist finitely many test profiles:

\[
\boxed{
\psi_1,\ldots,\psi_m
}
\]

such that every package in the compact recurrent resolved-bad class satisfies:

\[
\boxed{
\max_{1\le j\le m}
|\langle G,\psi_j\rangle|
\ge
\frac12c_{\rm obs}.
}
\tag{10.1}
\]

Equivalently the finite coefficient norm obeys:

\[
\boxed{
\mathfrak A_m(G)
\ge
\frac12c_{\rm obs}.
}
\tag{10.2}
\]

This directly matches the finite-dimensional active-work architecture of the coarse depletion theorem.

---

# 11. Active extraction now applies

The coarse work source proves that for a fixed finite family there is a nonnegative active weight:

\[
\widehat\phi_k
\]

such that:

\[
\boxed{
|\mathcal W_k[\widehat\phi_k]|
\ge
c_{\rm act}
\mathfrak A_k(G).
}
\]

On the D87 compact recurrent class:

\[
\boxed{
|\mathcal W_k|
\ge
c_{\rm act}
\frac12c_{\rm obs}
=:
c_W>0.
}
\tag{11.1}
\]

Therefore every resolved-bad recurrent scale has one of:

\[
\boxed{
\mathcal W_k^+
\ge
c_W
}
\]

or:

\[
\boxed{
\mathcal W_k^-
\ge
c_W.
}
\]

The second is explicit backscatter.

The first is forward signed combined work.

Thus:

## Theorem D87.11 — Recurrent Work Visibility Dichotomy

\[
\boxed{
\text{resolved recurrent badness}
\Longrightarrow
W_+
\vee
W_-
}
\]

after the already-declared residual/leakage/return/tail/compactness escapes are removed.

---

# 12. Pressure–flux cancellation is now explicitly classified

Suppose the individual channels satisfy:

\[
|\mathcal F|
+
|\mathcal P|
\gg
|\mathcal W|.
\]

Then:

\[
\mathcal C^{PF}
\]

is large.

There are two possibilities.

### combined work remains observable

Then D87.11 applies.

### combined work tends to zero

Then, on the recurrent compact residual/leakage-silent branch, D87.3–8 force the bulk-translation affine-pressure limit, which native Morrey excludes.

Therefore:

## Theorem D87.12 — No Compact Recurrent Cancellation Kernel

A persistent pressure–flux cancellation cannot produce a nontrivial compact recurrent resolved-bad zero-work limit.

It must instead coincide with at least one of:

- active combined work;
- subfilter residual;
- leakage;
- endpoint nonreturn;
- material/profile noncompactness;
- tail/Morrey escape.

---

# 13. Harmonic pressure tail classification

A harmonic pressure is not gauge.

The coarse-work source gives the exact example:

\[
U=a(t),
\qquad
P=-a'(t)\cdot x.
\]

It can perform real local work when:

\[
|a(t)|^2
\]

changes.

D87 shows:

- if the recurrent endpoint kinetic energy returns;
- and total combined work is silent;
- and leakage is silent;

then:

\[
\nabla U=0.
\]

So the harmonic-pressure branch reduces exactly to the affine-pressure translation normal form.

Native Morrey then kills the nonzero translation.

Thus:

## Theorem D87.13 — Harmonic Pressure Is Active or Trivial on the Recurrent Native Class

\[
\boxed{
\text{harmonic pressure}
\Longrightarrow
\text{observable work / return change}
\vee
\text{native-trivial affine translation}.
}
\]

No separate compact recurrent harmonic-pressure equality mode survives.

---

# 14. Coherent low-frequency resolved profiles

The external source lists coherent low-frequency resolved flow as a possible work-invisible mechanism.

D87 shows that on the recurrent leakage-silent class, **exact work silence** collapses the entire low-frequency family to:

\[
\nabla U=0.
\]

Therefore any genuinely nonconstant coherent low-frequency profile must pay at least one of:

\[
\boxed{
G\neq0,
\quad
L\neq0,
\quad
E^+\neq E^-.
}
\]

Or the sequence fails compactness/residual closure.

So the coherent low-frequency endpoint is no longer broad in the same-parent recurrent program.

---

# 15. What happens to X72?

D87 does not require a direct implication:

\[
C_3
\Longrightarrow
X.
\]

That would be too strong.

Instead the architecture is now:

\[
\boxed{
C_3\text{-badness}
}
\]

\[
\Downarrow
\]

coarse resolution:

\[
\boxed{
\Omega^\ell
\vee
\Psi^\ell
}
\]

\[
\Downarrow
\]

on the recurrent compact branch:

\[
\boxed{
\Omega^\ell
\vee
W_+
\vee
W_-
\vee
\text{explicit transition defect}.
}
\]

X72 remains available to classify any coherent pressure-perfect residual state that appears before the work-silent rigidity assumptions close.

This avoids a false scalar identification between one-component mass and pressure response.

---

# 16. Important limitation — observability is not yet global depletion

The coarse work theorem uses finite-chain weights:

\[
\boxed{
w_k=\frac{r_k}{r_0}.
}
\]

Its exact depletion inequality is:

\[
\boxed{
\sum_k
w_k
(
\mathcal W_k^+
+
\mathcal D_k
)
\le
\mathcal E_0^-
+
\sum_kw_k|\mathcal L_k|
+
\sum_kw_k\mathcal W_k^-.
}
\tag{16.1}
\]

For a geometric scale chain:

\[
r_k=\lambda^kr_0,
\]

\[
\sum_kw_k
=
\sum_k\lambda^k
<
\infty.
\]

Therefore even a uniform normalized forward work floor:

\[
\mathcal W_k^+\ge c_W
\]

does **not** by itself contradict an infinite geometric scale chain.

This is the same critical summability phenomenon encountered repeatedly in the project.

Thus:

## Theorem D87.14 — Observability/Depletion Separation

D87 closes the **visibility** gap on the recurrent compact class.

It does not yet close the **global weighted depletion** gap.

This distinction is essential.

---

# 17. Updated forest normal form

D86 had:

\[
\text{long bad-scale forest}
\Longrightarrow
R_{\rm subfilter}
\vee
R_{\rm OW}.
\]

D87 resolves \(R_{\rm OW}\) on the recurrent compact same-parent class.

Therefore:

## Theorem D87.15 — Recurrent Forest Visibility Compiler

\[
\boxed{
\text{resolved bad forest}
\Longrightarrow
R_{\rm subfilter}
\vee
W_+
\vee
W_-
\vee
R_{\rm leak}
\vee
R_{\rm ret}
\vee
R_{\rm tail}
\vee
R_{\rm comp}.
}
\tag{17.1}
\]

There is no additional compact pressure–flux cancellation or coherent-low-frequency zero-work branch.

---

# 18. What remains after D87

The remaining late problem is now genuinely signed and global.

A singular same-parent scale forest may survive if normalized active work is visible at every scale but the physical/telescoping weights are geometrically summable.

Thus the next question is no longer:

> “is resolved badness visible?”

It is:

> “can same-parent recurrence convert the geometrically weighted signed-work budget into an unweighted or regeneration-sensitive debt?”

Possible ingredients:

- mandatory inward PFET;
- D74 material counterflow;
- one-period same-parent recurrence;
- pressure–flux/backscatter sign statistics;
- parent-to-child regeneration;
- branch-world/forest multiplicity.

This is a new level of the endgame.

---

# 19. Candidate regeneration quotient

The weighted work law pays:

\[
w_k\mathcal W_k
\sim
\frac{r_k}{r_0}\mathcal W_k.
\]

But same-parent recurrence regenerates a normalized state of comparable badness after each reroot.

Define schematically the regeneration quotient:

\[
\boxed{
\mathfrak Q_{\rm reg}
=
\frac{
\text{normalized next-generation badness}
}{
\text{physical signed work paid to create it}
}.
}
\]

If:

\[
\mathcal W_k\ge c_W
\]

but:

\[
w_k\sim r_k/r_0,
\]

then:

\[
\mathfrak Q_{\rm reg}
\sim
r_k^{-1}.
\]

So the cost per normalized regenerated state becomes smaller at smaller physical scales.

A closure theorem must therefore exploit **same-parent ancestry / recurrence structure**, not raw energy depletion alone.

This is the natural next target.

---

# 20. Status ledger

## PROVED this round

### D87-P1 — exact coarse resolved energy equation

\[
\partial_tK-\Delta K+|\nabla U|^2+\nabla\cdot(KU+RU)+G=0.
\]

### D87-P2 — exact localized recurrent work ledger.

### D87-P3 — zero combined work + endpoint return + zero leakage forces zero resolved dissipation.

### D87-P4 — work-silent recurrent resolved profile is spatially constant.

### D87-P5 — residual-silent constant limit has vanishing SGS stress.

### D87-P6 — only residual-free work-silent coarse profile is bulk translation + affine harmonic pressure.

### D87-P7 — native Morrey excludes nonzero bulk translation.

### D87-P8 — no recurrent compact resolved-bad work-invisible limit.

### D87-P9 — positive infinite-test coarse observability gap on the recurrent compact class.

### D87-P10 — compactness reduces the infinite detector to finitely many active test profiles.

### D87-P11 — source active-work extraction gives a uniform forward/backscatter work dichotomy on this class.

### D87-P12 — pressure–flux cancellation and harmonic-pressure low-frequency modes do not yield an additional compact recurrent zero-work endpoint.

### D87-P13 — observability is closed but global weighted depletion remains critical/summable.

---

# 21. What is not proved

D87 does not prove:

- unconditional coarse observability for all suitable weak solutions;
- the compact recurrent hypotheses from first principles in every prelimit branch;
- backscatter is small;
- localization leakage is summable;
- endpoint mismatch vanishes in every forest;
- a uniform normalized work floor contradicts an infinite geometric chain;
- global Navier–Stokes regularity.

The remaining late gap is now a **same-parent regeneration versus geometrically weighted signed-work depletion** problem.

---

# 22. New STOP

\[
\boxed{
\textbf{
STOP-D87:
On the same-parent recurrent compact class, the coarse observability gap can be closed. The exact resolved-energy identity shows that a distributionally work-silent package with returning localized kinetic energy and vanishing leakage has zero resolved dissipation, hence spatially constant resolved velocity. If the subfilter residual also vanishes, the only limit is a bulk translation with affine harmonic pressure; the native global Morrey law excludes every nonzero such translation, so positive resolved CKN badness cannot coexist with zero combined-work detector. Compactness then yields a finite active test family with a uniform work gap, after which the existing pressure--flux work theorem gives an explicit forward-work/backscatter alternative. Thus pressure--flux cancellation, harmonic pressure, and coherent low-frequency flow no longer provide a compact recurrent zero-work endpoint in this branch. However the depletion theorem weights scale }k\textbf{ by }r_k/r_0\textbf{, whose geometric sum is finite; observability is therefore closed, but global depletion is still critically summable. The remaining endgame is same-parent regeneration versus weighted signed-work cost, not another visibility classification.}
}
\]

---

# 23. Next autonomous step

## DCRP88 / X72-R71 — Same-Parent Regeneration versus Weighted Signed-Work Summability

**Working title**

> **Can a DSS/Same-Parent Branch Regenerate Order-One Normalized Badness at Infinitely Many Scales while Paying Only a Geometrically Summable Signed-Work Cost?**

Primary tasks:

1. assume D87 observability:
   \[
   |W_k|\ge c_W;
   \]
2. retain:
   \[
   w_k=r_k/r_0;
   \]
3. distinguish:
   - forward-work generations;
   - backscatter-funded generations;
4. define a parent-to-child regeneration map for normalized badness;
5. compare normalized recurrence with physical work:
   \[
   w_kW_k;
   \]
6. seek an exact same-parent identity that charges **regeneration**, not raw energy;
7. combine:
   - D31 inward PFET;
   - D74 material counterflow;
   - D76 material amplification;
   - D85 bad-scale gap debt;
8. determine whether each regenerated child must also export a signed material pressure-work / circulation quantity whose normalization cancels the geometric \(w_k\);
9. if not, isolate one exact “critical regeneration conveyor” normal form.

Desired endpoint:

\[
\boxed{
\text{same-parent recurrent work visibility}
\Longrightarrow
\text{non-summable regeneration debt}
\vee
\text{one explicit critical conveyor}.
}
\]

---

# 24. One-line checkpoint

The resolved-badness-to-signed-work observability gap is closed on the same-parent recurrent compact branch; the only reason this still does not finish the forest is that the exact work-depletion theorem carries geometrically summable physical scale weights, so the remaining question is now regeneration cost rather than visibility.

---

**End checkpoint:** DCRP87 / X72-R70  
**Next:** DCRP88 / X72-R71 — Same-Parent Regeneration / Weighted Work Summability.
