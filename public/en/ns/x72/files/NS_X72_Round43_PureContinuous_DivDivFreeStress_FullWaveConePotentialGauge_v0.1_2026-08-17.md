# NS × X Integral × 24/72 Paradigm Practice
## Round 43 — Pure Continuous Double-Divergence-Free Stress / Full-Wave-Cone Potential-Gauge Route

- Date: 2026-08-17
- Version: v0.1
- Status: Proof-Route Experiment / Continuous-Only Differential-Constraint Branch
- canonical source: UTF-8 Markdown
- canonical math delimiters: inline `$...$`; display `$$...$$`
- Previous round: `NS_X72_Round42_PureContinuous_PiolaVorticity_VisibleInvisibleStress_v0.1_2026-08-17.md`
- Objective of this round: Round 42 has compressed the nonlocal Piola defect into a Riesz-invisible trace-free symmetric stress
  $$
  W_T,
  \qquad
  \partial_i\partial_j(W_T)_{ij}=0.
  $$
  This round directly investigates whether this differential constraint itself is sufficient to provide compensated regularity. It establishes the divdiv constant-rank symbol, full wave cone, exact symcurl potential/gauge representation, quadratic null-Lagrangian no-go, and constrained transfer triad witness.
- Non-assertion: This document does not prove that the actual NS vorticity-generated $W_T$ can arbitrarily realize all divdiv-free tensor waves. Conversely, the conclusion of this round is: **divdiv constraint alone is too weak**; the next step must utilize the nonlinear realizability of
  $$
  W_L+W_T
  =
  \omega\otimes\omega-\frac13|\omega|^2I
  $$
  and
  $$
  \nabla\cdot\omega=0.
  $$

---

# 0. Round 42 handoff

Round 42 defines the trace-free vorticity stress:

$$
\boxed{
W
=
\omega\otimes\omega
-
\frac13|\omega|^2I.
}
\tag{0.1}
$$

Riesz visible/invisible decomposition:

$$
\boxed{
W
=
W_L+W_T,
}
\tag{0.2}
$$

where:

$$
\boxed{
W_L
=
\mathbb P_LW,
\qquad
W_T
=
(I-\mathbb P_L)W.
}
\tag{0.3}
$$

and:

$$
\boxed{
\mathcal T_0^\ast W_T=0.
}
\tag{0.4}
$$

Since $W_T$ is trace-free:

$$
\boxed{
\partial_i\partial_j(W_T)_{ij}=0.
}
\tag{0.5}
$$

Round 42 STOP:

$$
\boxed{
\text{STOP-C46}
=
\text{Visible–Invisible Vorticity-Stress Transfer / Double-Divergence Compensation Gap}.
}
$$

---

# 1. The trace-free divdiv operator

Let:

$$
\mathbb S_0
=
\{
A\in\mathbb R^{3\times3}
:
A^\top=A,
\ \operatorname{tr}A=0
\}.
$$

dimension:

$$
\dim\mathbb S_0=5.
$$

Define:

$$
\boxed{
\mathcal A(D)
=
\operatorname{div}\operatorname{div}
:
\mathbb S_0
\to
\mathbb R.
}
\tag{1.1}
$$

Fourier symbol:

$$
\boxed{
\mathcal A(\xi)M
=
-\xi^\top M\xi.
}
\tag{1.2}
$$

The sign convention has no effect on the kernel.

---

# 2. Constant-rank property

For:

$$
\xi\ne0,
$$

let:

$$
n=\frac{\xi}{|\xi|}.
$$

Take:

$$
\boxed{
M_\xi
=
n\otimes n
-
\frac13I
\in\mathbb S_0.
}
\tag{2.1}
$$

Then:

$$
\boxed{
\xi^\top M_\xi\xi
=
\frac23|\xi|^2
\ne0.
}
\tag{2.2}
$$

Therefore:

$$
\boxed{
\operatorname{rank}
\mathcal A(\xi)
=
1
\qquad
\forall\xi\ne0.
}
\tag{2.3}
$$

Thus:

$$
\boxed{
\operatorname{div}\operatorname{div}
\text{ on }\mathbb S_0
\text{ is a homogeneous constant-rank operator.}
}
$$

---

# 3. Frequency-wise invisible subspace

For a unit direction:

$$
n,
$$

define:

$$
\boxed{
\mathcal K_n
=
\{
M\in\mathbb S_0
:
n^\top Mn=0
\}.
}
\tag{3.1}
$$

Since:

$$
\mathcal A(\xi)
$$

is rank one,

$$
\boxed{
\dim\mathcal K_n=4.
}
\tag{3.2}
$$

If:

$$
n=e_3,
$$

then:

$$
\boxed{
M
=
\begin{pmatrix}
a & b & c\\
b & -a & d\\
c & d & 0
\end{pmatrix}.
}
\tag{3.3}
$$

Therefore, for each frequency direction, only one scalar longitudinal stress component is seen by divdiv,

while the other four tensor polarizations are invisible.

---

# 4. The wave cone is the entire trace-free tensor space

The wave cone of a constant-rank operator is:

$$
\boxed{
\Lambda_{\mathcal A}
=
\bigcup_{\xi\ne0}
\ker\mathcal A(\xi).
}
\tag{4.1}
$$

Take any:

$$
M\in\mathbb S_0,
\qquad
M\ne0.
$$

Since:

$$
\operatorname{tr}M=0,
$$

$M$ cannot be positive definite or negative definite.

Thus, its quadratic form:

$$
Q_M(n)
=
n^\top Mn
$$

on:

$$
\mathbb S^2
$$

must take:

- positive values;
- negative values;

or already has a zero eigenvalue.

By continuity, there exists:

$$
n_\ast\in\mathbb S^2
$$

such that:

$$
\boxed{
n_\ast^\top Mn_\ast=0.
}
\tag{4.2}
$$

Therefore:

$$
M\in\ker\mathcal A(n_\ast).
$$

Thus:

$$
\boxed{
\Lambda_{\mathcal A}
=
\mathbb S_0.
}
\tag{4.3}
$$

Nomenclature:

$$
\boxed{
\textbf{Full-Wave-Cone Theorem for Trace-Free divdiv}.
}
$$

---

# 5. Every tensor amplitude admits an invisible plane wave

From Section 4,

for any:

$$
M\in\mathbb S_0,
$$

we can choose:

$$
\xi\ne0
$$

such that:

$$
\xi^\top M\xi=0.
$$

Then for any smooth scalar profile:

$$
h,
$$

$$
\boxed{
W(x)
=
M
h(\xi\cdot x)
}
\tag{5.1}
$$

satisfies:

$$
\boxed{
\operatorname{div}\operatorname{div}W=0.
}
\tag{5.2}
$$

Therefore, the divdiv-free condition itself does not exclude any pointwise tensor amplitude.

It only restricts:

$$
\boxed{
\text{amplitude–frequency orientation}.
}
$$

---

# 6. No nontrivial quadratic null Lagrangian from divdiv alone

Let:

$$
Q:\mathbb S_0\to\mathbb R
$$

be a homogeneous quadratic form,

and assume it is an $\mathcal A$-quasiaffine / quadratic null-Lagrangian-type compensated quantity.

For:

$$
M\in\Lambda_{\mathcal A},
$$

take the periodic mean-zero:

$$
h(s)=\cos s.
$$

Then:

$$
W(x)=Mh(\xi\cdot x)
$$

is $\mathcal A$-free,

and its mean is:

$$
\overline W=0.
$$

Quasiaffinity requires:

$$
\overline{Q(W)}
=
Q(\overline W)
=
0.
$$

But:

$$
\overline{Q(W)}
=
Q(M)
\overline{\cos^2}
=
\frac12Q(M).
$$

Thus:

$$
Q(M)=0
$$

for every:

$$
M\in\Lambda_{\mathcal A}.
$$

From:

$$
\Lambda_{\mathcal A}
=
\mathbb S_0,
$$

we obtain:

$$
\boxed{
Q\equiv0.
}
\tag{6.1}
$$

Nomenclature:

$$
\boxed{
\textbf{Quadratic Compensation No-Go}.
}
$$

Therefore:

$$
\boxed{
|W_T|^2
}
$$

cannot rely solely on:

$$
\operatorname{div}\operatorname{div}W_T=0
$$

to become a nontrivial quadratic null Lagrangian.

---

# 7. Consequence for Hardy-type compensated energy

Constant-rank compensated-compactness theory connects operator-specific Hardy integrability with null-Lagrangian / quasiaffine quantities.

Section 6 shows:

$$
\boxed{
\text{there is no nonzero quadratic compensated scalar
available from the trace-free divdiv constraint alone.}
}
$$

Thus, we cannot expect the universal:

$$
\boxed{
|W_T|^2
\in
\mathcal H^1
}
\tag{7.1}
$$

to be deduced solely from:

$$
\operatorname{div}\operatorname{div}W_T=0
$$

.

This does not exclude:

- mixed bilinear quantities;
- higher-degree special invariants;
- additional vorticity realizability;

from generating compensation.

---

# 8. Cocanceling but not smoothing

On the other hand,

if:

$$
M\in
\bigcap_{\xi\ne0}
\ker\mathcal A(\xi),
$$

then:

$$
\xi^\top M\xi=0
$$

for every:

$$
\xi.
$$

Therefore:

$$
M=0.
$$

Thus:

$$
\boxed{
\operatorname{div}\operatorname{div}
\text{ on }\mathbb S_0
\text{ is cocanceling}.
}
\tag{8.1}
$$

Endpoint cocanceling theory can therefore provide negative-order dual/Sobolev compensation for:

$$
L^1
$$

divdiv-free tensors.

In:

$$
n=3,
$$

schematically:

$$
\boxed{
W_T\in L^1,
\quad
\operatorname{div}\operatorname{div}W_T=0
\Longrightarrow
W_T\in\dot W^{-1,3/2}.
}
\tag{8.2}
$$

But this is:

$$
\boxed{
\text{negative-order compensation},
}
$$

not the positive increment regularity we need.

Therefore:

$$
\boxed{
\textbf{cocancellation is real but insufficient for Round 42 endpoint transfer.}
}
$$

---

# 9. Exact divdiv differential complex

In 3D contractible domains, the standard divdiv complex has the exact sequence:

$$
\boxed{
RT
\longrightarrow
H^1(\mathbb R^3)
\xrightarrow{
\operatorname{dev}\nabla
}
H(\operatorname{symcurl};\mathbb T)
\xrightarrow{
\operatorname{symcurl}
}
H(\operatorname{divdiv};\mathbb S)
\xrightarrow{
\operatorname{divdiv}
}
L^2
\longrightarrow0.
}
\tag{9.1}
$$

where:

- $\mathbb T$: trace-free matrices;
- $\mathbb S$: symmetric matrices.

Thus, in the compatible topology / boundary branch:

$$
\boxed{
\operatorname{div}\operatorname{div}W_T=0
}
$$

implies the existence of a trace-free tensor potential:

$$
\boxed{
\Psi
}
$$

such that:

$$
\boxed{
W_T
=
\operatorname{symcurl}\Psi.
}
\tag{9.2}
$$

Nomenclature:

$$
\boxed{
\textbf{Invisible-Stress SymCurl Potential}.
}
$$

---

# 10. Potential gauge freedom

The exact complex simultaneously gives:

$$
\boxed{
\operatorname{symcurl}
(
\operatorname{dev}\nabla v
)
=
0.
}
\tag{10.1}
$$

Thus:

$$
\boxed{
\Psi
\sim
\Psi
+
\operatorname{dev}\nabla v.
}
\tag{10.2}
$$

Nomenclature:

$$
\boxed{
\textbf{Invisible-Stress Potential Gauge}.
}
$$

Therefore, the potential representation of $W_T$ is not a discrete mode expansion,

but a continuous gauge geometry.

---

# 11. Whole-space Fourier minimal potential

For:

$$
\xi\ne0
$$

let:

$$
\mathbb B(\xi)
$$

be the:

$$
\operatorname{symcurl}
$$

symbol.

Exactness gives:

$$
\boxed{
\operatorname{im}\mathbb B(\xi)
=
\ker\mathcal A(\xi).
}
\tag{11.1}
$$

Take the Moore–Penrose pseudoinverse:

$$
\mathbb B(\xi)^\dagger.
$$

For:

$$
\widehat W_T(\xi)
\in
\ker\mathcal A(\xi),
$$

define:

$$
\boxed{
\widehat\Psi(\xi)
=
\mathbb B(\xi)^\dagger
\widehat W_T(\xi).
}
\tag{11.2}
$$

Since:

$$
\mathbb B(\xi)
$$

is homogeneous of degree one and has constant rank on the sphere,

we have:

$$
\boxed{
|\xi|
|\widehat\Psi(\xi)|
\le
C
|\widehat W_T(\xi)|.
}
\tag{11.3}
$$

Thus:

$$
\boxed{
\|\nabla\Psi\|_2
\le
C
\|W_T\|_2.
}
\tag{11.4}
$$

The potential exists and has a natural energy gauge.

---

# 12. Potential representation does not create a free derivative

Since:

$$
W_T
=
\operatorname{symcurl}\Psi,
$$

if a high-frequency mode:

$$
W_T
\sim
B
e^{iN\xi\cdot x}
$$

maintains an amplitude of:

$$
O(1),
$$

its minimal potential amplitude is only:

$$
O(N^{-1}).
$$

But:

$$
\operatorname{symcurl}
$$

multiplies back by:

$$
N.
$$

Thus, transferring the derivative to the potential only redistributes the derivative,

and does not lower the total critical derivative count.

Therefore:

$$
\boxed{
\textbf{
the potential complex solves representation,
not the endpoint regularity budget.
}
}
\tag{12.1}
$$

---

# 13. Frequency projection formula

The Round 42 longitudinal projection symbol can be written as:

$$
\boxed{
P_L(n)F
=
\frac32
m(n)
[
m(n):F
],
}
\tag{13.1}
$$

where:

$$
\boxed{
m(n)
=
\frac13I
-
n\otimes n,
}
\tag{13.2}
$$

and:

$$
|m(n)|^2
=
\frac23.
$$

For a trace-free:

$$
F,
$$

$$
m(n):F
=
-
n^\top Fn.
$$

Thus:

$$
\boxed{
P_L(n)F=0
\iff
n^\top Fn=0.
}
\tag{13.3}
$$

That is:

$$
\boxed{
\ker P_L(n)
=
\mathcal K_n.
}
$$

The Round 42 visible/invisible decomposition is therefore completely identical to the divdiv symbol kernel.

---

# 14. Constrained transfer triad witness

To test whether:

$$
\operatorname{divdiv}W_T=0
$$

can automatically kill the Round 42 transfer,

take the frequencies:

$$
\boxed{
k
=
Ne_1,
\qquad
\ell
=
Ne_2,
}
\tag{14.1}
$$

velocity amplitude:

$$
\boxed{
a=e_2.
}
\tag{14.2}
$$

Then:

$$
k\cdot a=0,
$$

so the velocity plane wave is divergence-free,

and:

$$
a\cdot\ell=N\ne0.
$$

Take the invisible stress amplitude:

$$
\boxed{
B
=
\operatorname{diag}(1,0,-1).
}
\tag{14.3}
$$

Since:

$$
e_2^\top Be_2=0,
$$

we have:

$$
\boxed{
P_L(e_2)B=0.
}
\tag{14.4}
$$

Thus:

$$
B e^{i\ell\cdot x}
$$

is a frequency-wise invisible / divdiv-free stress wave.

---

# 15. Shifted frequency becomes visible

Output frequency:

$$
m
=
k+\ell
=
N(e_1+e_2).
$$

Let:

$$
n_m
=
\frac{
e_1+e_2
}{
\sqrt2
}.
$$

Then:

$$
\boxed{
n_m^\top Bn_m
=
\frac12.
}
\tag{15.1}
$$

Thus:

$$
\boxed{
P_L(n_m)B\ne0.
}
\tag{15.2}
$$

Direct calculation:

$$
\boxed{
\|P_L(n_m)B\|_F^2
=
\frac38.
}
\tag{15.3}
$$

Therefore, the transport frequency shift moves the tensor originally invisible at:

$$
\ell
$$

to:

$$
k+\ell,
$$

and under the new direction it becomes partially visible.

This is exactly the Round 42:

$$
W_T\to W_L
$$

transfer mechanism.

---

# 16. Nonzero constrained commutator symbol

For the complex plane waves:

$$
u
=
a
e^{ik\cdot x},
$$

$$
W_T
=
B
e^{i\ell\cdot x},
$$

the projection commutator:

$$
[D_u,\mathbb P_L]W_T
$$

at the:

$$
m=k+\ell
$$

frequency has the coefficient:

$$
\boxed{
i(a\cdot\ell)
[
P_L(\ell)-P_L(m)
]B.
}
\tag{16.1}
$$

Since:

$$
P_L(\ell)B=0,
$$

Thus:

$$
\boxed{
[D_u,\mathbb P_L]W_T
=
-iN
P_L(m)B
\ e^{im\cdot x}.
}
\tag{16.2}
$$

After pairing with the matching visible mode,

the symbol magnitude contains:

$$
\boxed{
N
\|P_L(m)B\|^2
=
\frac38N.
}
\tag{16.3}
$$

Real sine/cosine phases can extract the same nonzero real trilinear transfer.

Nomenclature:

$$
\boxed{
\textbf{Constrained Transfer Triad Witness}.
}
$$

---

# 17. The double-divergence constraint does not lower the derivative order

Section 16 shows:

- velocity is divergence-free;
- input stress is divdiv-free;
- input stress is exactly Riesz-invisible;

can still produce an:

$$
\boxed{
O(N)
}
$$

visible/invisible transfer coefficient.

Thus:

$$
\boxed{
\textbf{
double-divergence-free compensation alone
does not remove the one transport derivative.
}
}
\tag{17.1}
$$

This proves at the operator-symbol level that the Round 42 one-total-derivative endpoint cannot be lowered solely by:

$$
\operatorname{divdiv}W_T=0
$$

.

---

# 18. Why potential gauge cannot kill the transfer witness

For the stress wave in Section 14,

the symcurl potential can take the amplitude:

$$
\Psi_N
=
O(N^{-1})
e^{i\ell\cdot x}.
$$

But in the transfer:

$$
W_T
=
\operatorname{symcurl}\Psi_N
$$

restores the:

$$
O(1)
$$

stress amplitude.

Any gauge shift:

$$
\Psi_N
\mapsto
\Psi_N+\operatorname{dev}\nabla v
$$

does not change:

$$
W_T.
$$

Thus, the Section 16 transfer coefficient:

$$
\frac38N
$$

is gauge invariant.

Therefore:

$$
\boxed{
\text{potential gauge fixes representation redundancy,
not the transfer endpoint}.
}
$$

---

# 19. What the divdiv constraint actually gives

This round can precisely classify:

## D1 — positive structure

- constant-rank;
- cocanceling;
- exact differential complex;
- symcurl potential;
- continuous gauge;
- negative-order endpoint compensation.

## D2 — negative structure

- full wave cone;
- no nontrivial quadratic null Lagrangian;
- arbitrary tensor amplitudes admit A-free plane waves;
- constrained transfer triads survive;
- one transport derivative remains sharp at symbol level.

Thus:

$$
\boxed{
\textbf{
divdiv gives representation and weak compensation,
but not enough rigidity to close quartic stress transfer.
}
}
\tag{19.1}
$$

---

# 20. The missing structure is nonlinear vorticity realizability

The actual NS stress is not an arbitrary:

$$
W\in\mathbb S_0.
$$

It satisfies:

$$
\boxed{
W
=
\omega\otimes\omega
-
\frac13|\omega|^2I.
}
\tag{20.1}
$$

pointwise eigenvalues:

$$
\boxed{
\frac23|\omega|^2,
\qquad
-\frac13|\omega|^2,
\qquad
-\frac13|\omega|^2.
}
\tag{20.2}
$$

Therefore:

$$
W
$$

lies on the axisymmetric rank-one-generated cone:

$$
\boxed{
\mathcal M_\omega
=
\left\{
a\otimes a
-
\frac13|a|^2I
:
a\in\mathbb R^3
\right\}.
}
\tag{20.3}
$$

---

# 21. Algebraic realizability identities

For:

$$
W\in\mathcal M_\omega,
$$

we have:

$$
\boxed{
|W|^2
=
\frac23|\omega|^4,
}
\tag{21.1}
$$

$$
\boxed{
\det W
=
\frac2{27}
|\omega|^6,
}
\tag{21.2}
$$

and the sharp axisymmetric relation:

$$
\boxed{
54
(\det W)^2
=
|W|^6.
}
\tag{21.3}
$$

Thus:

$$
\mathcal M_\omega
$$

is a low-dimensional nonlinear cone in $\mathbb S_0$.

Away from zero, its dimension is:

$$
3
$$

while:

$$
\dim\mathbb S_0=5.
$$

Thus, the actual vorticity stress possesses two additional algebraic realizability constraints.

---

# 22. Visible and invisible stresses are not independent

Although:

$$
W_L
$$

and:

$$
W_T
$$

belong to orthogonal Fourier subspaces,

their sum must satisfy:

$$
\boxed{
W_L+W_T
\in
\mathcal M_\omega
}
\tag{22.1}
$$

pointwise.

Therefore:

$$
\boxed{
54
\left[
\det(W_L+W_T)
\right]^2
=
|W_L+W_T|^6.
}
\tag{22.2}
$$

Furthermore:

$$
\boxed{
\nabla\cdot\omega=0.
}
\tag{22.3}
$$

Thus, the actual NS invisible stress also carries:

- nonlinear axisymmetric realizability;
- divergence-free generator;
- coupling to visible stress.

These were not used in the arbitrary constrained triad witness in Section 16.

---

# 23. Full-wave-cone no-go does not kill the NS-specific route

The full wave cone in Section 4 implies that:

$$
\boxed{
\operatorname{divdiv}W_T=0
}
$$

alone is insufficient.

But the actual:

$$
W_T
=
\mathbb P_T
\left(
\omega\otimes\omega-\frac13|\omega|^2I
\right)
$$

is a nonlocal projection of a rank-one-generated stress.

Thus, the remaining route is not:

$$
\boxed{
\text{generic constant-rank compensated compactness}.
}
$$

but rather:

$$
\boxed{
\textbf{nonlinear realizability + differential constraint + projection transfer}.
}
$$

This is narrower than the generic $W_T$ formulation of Round 42.

---

# 24. STOP-C47 — Full-Wave-Cone / Vorticity-Realizability Gap

$$
\boxed{
\begin{aligned}
\text{layer}
&=
\mathrm{double\text{-}divergence\text{-}free\ invisible\ stress},
\\
\mathcal A(D)
&=
\operatorname{divdiv}
\text{ on }\mathbb S_0,
\\
\operatorname{rank}\mathcal A(\xi)
&=
1,
\\
\text{wave cone}
&=
\mathbb S_0,
\\
\text{quadratic null Lagrangian}
&=
0
\text{ only},
\\
\text{cocanceling}
&=
\mathrm{true},
\\
\text{potential}
&=
W_T=\operatorname{symcurl}\Psi,
\\
\text{gauge}
&=
\Psi\sim\Psi+\operatorname{dev}\nabla v,
\\
\text{potential endpoint gain}
&=
\mathrm{none\ automatically},
\\
\text{constrained transfer triad}
&=
\mathrm{nonzero},
\\
\text{transfer derivative}
&=
\mathrm{one\ derivative\ survives},
\\
\text{actual NS extra structure}
&=
W_L+W_T\in\mathcal M_\omega,
\quad
\nabla\cdot\omega=0,
\\
\text{missing}
&=
\mathrm{use\ of\ nonlinear\ vorticity\text{-}stress\ realizability
to\ improve\ transfer/alignment\ endpoint},
\\
T_{\mathsf C\to\mathsf D}
&=
\mathrm{NOT\ REACHED}.
\end{aligned}
}
$$

Nomenclature:

$$
\boxed{
\textbf{STOP-C47:
Full-Wave-Cone / Vorticity-Realizability Gap}.
}
$$

---

# 25. 24/72 Ledger — Round 43

| Step | object | $B$ | $U$ | $O$ | $L$ | status |
|---|---|---|---|---|---|---|
| C659 | trace-free divdiv operator | $\mathsf C$ | differential constraint | relational | $\mathsf F$ | FORM |
| C660 | constant-rank symbol | $\mathsf C$ | Fourier geometry | scalar | $\mathsf F$ | PROVED |
| C661 | invisible frequency subspace | $\mathsf C$ | kernel geometry | profile | $\mathsf F$ | EXACT |
| C662 | full wave cone | $\mathsf C$ | compensated geometry | targeted | $\mathsf F$ | PROVED |
| C663 | arbitrary invisible plane wave | $\mathsf C$ | continuous wave | relational | $\mathsf F$ | CONSTRUCTED |
| C664 | quadratic compensation no-go | $\mathsf C$ | null-Lagrangian logic | targeted | $\mathsf F$ | PROVED |
| C665 | cocanceling property | $\mathsf C$ | endpoint operator geometry | scalar | $\mathsf F$ | PROVED |
| C666 | negative-order compensation | $\mathsf C$ | cocanceling theory | scalar | $\mathsf F$ | STANDARD |
| C667 | divdiv exact complex | $\mathsf C$ | differential complex | relational | $\mathsf F$ | STANDARD |
| C668 | symcurl potential | $\mathsf C$ | potential representation | tensor | $\mathsf F$ | EXACT under topology |
| C669 | potential gauge | $\mathsf C$ | gauge geometry | relational | $\mathsf F$ | EXACT |
| C670 | Fourier minimal potential | $\mathsf C$ | pseudoinverse | tensor | $\mathsf F$ | CONSTRUCTED |
| C671 | potential no-free-derivative | $\mathsf C$ | scaling | targeted | $\mathsf F$ | PROVED |
| C672 | projection/divdiv kernel equivalence | $\mathsf C$ | Fourier projection | relational | $\mathsf F$ | EXACT |
| C673 | constrained transfer triad | $\mathsf C$ | Fourier symbol test | targeted | $\mathsf F$ | CONSTRUCTED |
| C674 | one-derivative transfer survival | $\mathsf C$ | high-frequency scaling | scalar | $\mathsf F$ | PROVED at symbol level |
| C675 | vorticity-stress realizability cone | $\mathsf C$ | nonlinear algebra | relational | $\mathsf F$ | EXACT |
| C676 | visible/invisible realizability coupling | $\mathsf C$ | nonlinear projection | $\mathsf X$ | $\mathsf F$ | IDENTIFIED |
| C677 | generic divdiv-only endpoint closure | $\mathsf C$ | compensated compactness | targeted | $\mathsf F$ | REFUTED |
| C678 | NS-specific realizability closure | $\mathsf C$ | nonlinear constrained stress | targeted | $\mathsf F$ | OPEN / STOP-C47 |

---

# 26. Continuous-versus-discrete status

This round features:

- differential complex;
- potential;
- gauge;
- Fourier symbol;
- plane waves;
- wave cone.

But all utilize continuous:

$$
\xi\in\mathbb R^3\setminus\{0\},
$$

continuous tensor amplitudes and continuous gauge fields.

There are no:

- mode lattices;
- finite element discretizations as proof substrates;
- discrete wave labels;
- graph potentials.

The finite-element divdiv complex only serves as an external mathematical anchor for the exact continuous complex;

the actual theory in this round is still expressed using continuous operator symbols and whole-space Fourier pseudoinverses.

Therefore:

$$
\boxed{
T_{\mathsf C\to\mathsf D}
=
\text{NOT YET REACHED}.
}
$$

---

# 27. Strongest results of Round 43

## R43-A — constant rank

$$
\boxed{
\operatorname{rank}
[
M\mapsto\xi^\top M\xi
]
=
1
}
$$

for every:

$$
\xi\ne0.
$$

## R43-B — full wave cone

$$
\boxed{
\Lambda_{\operatorname{divdiv}}
=
\mathbb S_0.
}
$$

## R43-C — quadratic compensated-energy no-go

$$
\boxed{
\text{the only quadratic divdiv-null-Lagrangian on }\mathbb S_0
\text{ is zero}.
}
$$

## R43-D — continuous potential/gauge

$$
\boxed{
W_T
=
\operatorname{symcurl}\Psi,
\qquad
\Psi
\sim
\Psi+\operatorname{dev}\nabla v.
}
$$

## R43-E — constrained transfer survives

there are divergence-free velocity / divdiv-free invisible stress plane-wave triads with:

$$
\boxed{
|\text{transfer symbol}|
=
\frac38N.
}
$$

Thus, one transport derivative survives at high frequency.

## R43-F — actual NS stress lies on a nonlinear realizability cone

$$
\boxed{
W
=
\omega\otimes\omega-\frac13|\omega|^2I,
}
$$

with:

$$
\boxed{
54(\det W)^2
=
|W|^6.
}
$$

Thus, the remaining hope must use the vorticity origin rather than divdiv alone.

---

# 28. Next round — Vorticity-Stress Realizability / Axisymmetric Cone Coupling

Round 43 has capped off the generic double-divergence compensation route.

The next round will directly use the actual NS-specific relation:

$$
\boxed{
W
=
W_L+W_T
=
\omega\otimes\omega
-
\frac13|\omega|^2I.
}
$$

Core questions:

1. How does the axisymmetric stress cone:
   $$
   54(\det W)^2=|W|^6
   $$
   constrain the visible/invisible energy split?

2. Can $\eta_\omega$ arbitrarily approach $0$ or $1$ under realizability?

3. Given $W_L$, does the axisymmetric cone restrict the orientation / amplitude of $W_T$?

4. Does the divergence-free condition:
   $$
   \nabla\cdot\omega=0
   $$
   further restrict rapid invisible stress waves?

5. Can the Round 43 constrained triad witness be realized by the actual quadratic vorticity stress?

6. If not, the transfer endpoint might genuinely be lowered due to nonlinear realizability;

7. If actual vorticity triads can be constructed, then STOP-C47 will be proven sharp;

8. Maintain a continuous Fourier/physical-space stress manifold throughout, without performing discrete mode enumeration.

---

# 29. External primary-source anchors

1. Jun Hu, Yizhou Liang, Rui Ma, *Conforming finite element DIVDIV complexes and the application for the linearized Einstein-Bianchi system*, arXiv:2103.00088.
   - 3D exact divdiv complex:
     $$
     \operatorname{dev}\nabla
     \to
     \operatorname{symcurl}
     \to
     \operatorname{divdiv}.
     $$
   - used as the external anchor for the continuous symcurl potential / gauge structure.

2. Long Chen, Xuehai Huang, *Finite elements for divdiv-conforming symmetric tensors in three dimensions*, arXiv:2007.12399.
   - divdiv Hilbert/polynomial complexes and trace structure for symmetric tensors.

3. André Guerra, Bogdan Raiţă, *Quasiconvexity, null Lagrangians, and Hardy space integrability under constant rank constraints*, arXiv:1909.03923.
   - constant-rank compensated compactness;
   - identifies null Lagrangians with Hardy-integrable compensated quantities.

4. André Guerra, Bogdan Raiţă, Matthew R. I. Schrecker, *Compensated compactness: continuity in optimal weak topologies*, arXiv:2007.00564.
   - sharp constant-rank $\mathcal A$-free / Hardy-type compensated compactness framework.

5. Jean Van Schaftingen, *Limiting Sobolev inequalities for vector fields and canceling linear differential operators*, arXiv:1104.0192.
   - cocanceling operators and negative-order endpoint estimates for $L^1$ constrained fields.

The constant-rank proof, full-wave-cone theorem, quadratic compensation no-go, whole-space pseudoinverse potential, constrained transfer triad, and vorticity-stress realizability identities in this round are all directly derived in this document.

---

# 30. Commit state

$$
\boxed{
\begin{aligned}
\text{Route}
&=
\mathrm{Pure\ Continuous\ Double\text{-}Divergence\text{-}Free\ Stress\ Compensation},
\\
\text{Essential }\mathsf C\to\mathsf D
&=
\mathrm{Not\ reached},
\\
\text{divdiv constraint}
&=
\mathrm{constant\ rank\ and\ cocanceling},
\\
\text{wave cone}
&=
\mathrm{full},
\\
\text{quadratic Hardy/null-Lagrangian gain}
&=
\mathrm{none\ nontrivial},
\\
\text{potential representation}
&=
\mathrm{symcurl\ +\ devgrad\ gauge},
\\
\text{potential endpoint gain}
&=
\mathrm{none\ automatically},
\\
\text{generic constrained transfer}
&=
\mathrm{nonzero\ and\ one\text{-}derivative},
\\
\text{remaining special structure}
&=
\mathrm{vorticity\text{-}stress\ realizability\ cone},
\\
\text{STOP-C47}
&=
\mathrm{Full\text{-}Wave\text{-}Cone/Vorticity\text{-}Realizability\ Gap},
\\
\text{Next}
&=
\mathrm{Vorticity\text{-}Stress\ Realizability/Axisymmetric\ Cone\ Coupling}.
\end{aligned}
}
$$