# NS-DCRP-12 — Local PFET Localization, Work-Carrier Completion, and the Quantitative Anti-Diffusion Frontier

- date: 2026-08-16
- status: research proof checkpoint
- canonical source: UTF-8 Markdown
- canonical math delimiters: `$...$` and `$$...$$`
- objective: close the DCRP-11 global-to-local heat-work localization gap and determine exactly what remains if a fixed critical amount of work diffuses over an unbounded number of normalized parabolic cells.
- no full Navier--Stokes regularity claim is made.
- principal internal dependencies:
  - FCBP-04 heat-semigroup coarse pressure--flux ledger;
  - FCBP-05 combined pressure / resolved-flux / positive-energy / adjoint-trace observation map;
  - MORP-01 native residual channel;
  - MORP-02 spatial / relative-scale defect completion;
  - DCRP-08 through DCRP-11.
- external primary calibration:
  - Runlong Yu, arXiv:2606.25322v1;
  - Cheskidov--Dai, arXiv:1507.06611v6.

---

# 1. Executive result

DCRP-11 proved that every sufficiently high heat-band first-crossing event satisfies one of:

$$
\boxed{
\lambda_n
\int_{I_n}
(F_{b,n})_+
\,dt
\ge
c_{HB}\nu^2
}
\tag{1.1}
$$

or:

$$
\boxed{
\lambda_n
\int_{I_n}
(F_{a,n})_-
\,dt
\ge
c_{HB}\nu^2,
}
\tag{1.2}
$$

where:

$$
F_{*,n}(t)
=
\int_{\mathbb R^3}
\Pi_{*,n}(x,t)
\,dx
$$

is the whole-space heat-filter interscale work.

The remaining problem was to convert this global work into a local MORP / PFET / paid coordinate.

The localization part is now elementary once the internal FCBP-05 observation architecture is used correctly.

FCBP-05 does not retain only the single combined scalar work.

Its combined observation map contains separate channels:

$$
\boxed{
O_W^{comb}
=
(
O_W^P,
O_W^F,
O_W^E,
O_W^T
),
}
\tag{1.3}
$$

with active pressure, resolved flux, positive energy, and adjoint-trace components.

Therefore a nonzero local flux pairing is already a valid PFET-visible event even if a pressure term would cancel it in the scalar combined work.

The first new theorem is:

$$
\boxed{
\textbf{
nonzero whole-space heat flux}
\Longrightarrow
\textbf{
nonzero finite-window heat-flux pairing}.
}
}
\tag{1.4}
$$

The proof uses only a fixed-shape parabolic partition of unity.

No solution-dependent detector shape is needed.

The second new result is a compactness alternative for a sequence of fixed-total critical work events.

After normalizing every event to the filter scale, one has:

$$
\boxed{
\textbf{
local PFET atom}
\ \vee\
\textbf{
local paid backscatter}
\ \vee\
\textbf{
space/time work escape}.
}
}
\tag{1.5}
$$

The third alternative is a genuine PDE-generated work carrier.

It is compatible with the MORP-02 defect-completion philosophy:

- spatial non-tightness is represented by a compactified spatial defect;
- transition / temporal non-tightness is retained in the native residual side.

Thus the qualitative package-completion gap of DCRP-11 is closed **provided the heat-work escape coordinate is admitted as the concrete native residual already reserved abstractly by MORP-01**.

What is not yet closed is the quantitative coercive version.

A fixed global critical work amount can be divided among:

$$
N_n\to\infty
$$

normalized cells so that every single local coefficient tends to zero.

Therefore:

$$
\boxed{
\text{global critical work}
\not\Rightarrow
\text{uniform local detector gap}
}
\tag{1.6}
$$

without an anti-diffusion / bounded-multiplicity theorem.

The next frontier is therefore:

$$
\boxed{
\textbf{
Quantitative Work Anti-Diffusion / Critical Lift Lemma}.
}
$$

---

# 2. Source audit — what the existing PFET detector actually sees

The external coarse-grained work theorem defines the combined distribution:

$$
G^\ell
=
\Pi^\ell
+
\nabla\cdot(P^\ell U^\ell).
$$

Its active work detector is finite-dimensional and tests:

$$
\langle
G^\ell,
\phi
\rangle.
$$

It explicitly warns that pressure and flux may cancel in the scalar combined work.

However the same paper also records the signed component ledger:

$$
\boxed{
\mathcal F_{I,r}[\phi]
=
r^{-1}
\int_I
\int
\phi\Pi^\ell
\,dxdt,
}
\tag{2.1}
$$

and:

$$
\boxed{
\mathcal P_{I,r}[\phi]
=
-
r^{-1}
\int_I
\int
P^\ell U^\ell\cdot\nabla\phi
\,dxdt.
}
\tag{2.2}
$$

with:

$$
\mathcal W
=
\mathcal F
+
\mathcal P.
$$

The internal FCBP-05 architecture goes further and declares the combined observation vector:

$$
\boxed{
O_W^{comb}
=
(
O_W^P,
O_W^F,
O_W^E,
O_W^T
).
}
\tag{2.3}
$$

Therefore, for the present internal MORP program:

$$
\boxed{
O_W^F\ne0
\Longrightarrow
\mathsf O_{\rm PFET}>0.
}
\tag{2.4}
$$

Pressure--flux cancellation does not erase a nonzero **separate flux channel**.

This distinction is essential for the theorem below.

---

# 3. Fixed-shape spatial partition

Choose one nonnegative smooth function:

$$
\chi\in C_c^\infty(\mathbb R^3),
$$

and a lattice:

$$
\{y_j\}_{j\in\mathbb Z^3}
$$

such that:

$$
\boxed{
\sum_{j\in\mathbb Z^3}
\chi(y-y_j)
=
1
}
\tag{3.1}
$$

for all:

$$
y\in\mathbb R^3.
$$

Assume:

$$
\chi
$$

has support in a fixed ball:

$$
B_R(0),
$$

and the family has uniformly bounded overlap.

At physical scale:

$$
r>0,
$$

define:

$$
\boxed{
\chi_{j,r}(x)
=
\chi
\left(
\frac{x}{r}-y_j
\right).
}
\tag{3.2}
$$

Then:

$$
\sum_j
\chi_{j,r}(x)
=
1.
$$

Every:

$$
\chi_{j,r}
$$

is the translation / parabolic-scale pullback of one fixed reference profile.

Thus adaptive choice of:

$$
j
$$

is only a re-centering choice.

It does not change the detector shape.

---

# 4. Local integrability of heat-filter flux

Fix:

$$
s>0.
$$

For a smooth pre-singularity finite-energy solution:

$$
U^s
=
e^{s\Delta}u
$$

is spatially smooth.

The heat covariance:

$$
R^s
=
e^{s\Delta}(u\otimes u)
-
U^s\otimes U^s
$$

belongs to:

$$
L^1_x
$$

for each fixed time.

Also:

$$
\nabla U^s
$$

is bounded for positive:

$$
s.
$$

Therefore:

$$
\Pi^s
=
-
R^s:\nabla U^s
$$

belongs to:

$$
L^1_x.
$$

On every finite pre-singularity time interval:

$$
\Pi^s
$$

is locally integrable in spacetime, and the spatial partition can be summed by dominated convergence / absolute integrability.

Thus:

$$
\boxed{
F_s(t)
=
\sum_j
\int
\chi_{j,r}(x)
\Pi^s(x,t)
\,dx
}
\tag{4.1}
$$

for almost every time.

---

# 5. NEW THEOREM — spatial localization of signed heat flux

## Theorem 5.1

Let:

$$
J
$$

be a finite time interval and suppose:

$$
\boxed{
\int_J
F_s(t)
\,dt
>
0.
}
\tag{5.1}
$$

Then for every:

$$
r>0,
$$

there exists:

$$
j\in\mathbb Z^3
$$

such that:

$$
\boxed{
\int_J
\int
\chi_{j,r}(x)
\Pi^s(x,t)
\,dxdt
>
0.
}
\tag{5.2}
$$

Similarly, if:

$$
\int_J
F_s(t)
\,dt
<
0,
$$

then there exists:

$$
j
$$

with the corresponding local flux pairing negative.

### Proof

Using the partition of unity:

$$
\begin{aligned}
\int_J
F_s(t)
dt
&=
\int_J
\int
\Pi^s(x,t)
\,dxdt\\
&=
\sum_j
\int_J
\int
\chi_{j,r}(x)
\Pi^s(x,t)
\,dxdt.
\end{aligned}
$$

The sum is absolutely convergent after the standard locally finite partition / exhaustion argument.

If every summand were nonpositive, the total could not be positive.

Therefore at least one summand is positive.

The negative case is identical.

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

# 6. Temporal localization does not require a new test shape

DCRP-11 gives:

$$
\int_I
(F_s)_+
dt
>
0
$$

or:

$$
\int_I
(F_s)_-
dt
>
0.
$$

Suppose the forward case holds.

Then the measurable set:

$$
A
=
\{
t\in I:
F_s(t)>0
\}
$$

has positive measure.

For almost every:

$$
t\in A,
$$

equation (4.1) implies that at least one spatial cell satisfies:

$$
\int
\chi_{j,r}\Pi^s
>
0.
$$

Because the index set is countable, there exists at least one:

$$
j_\ast
$$

for which:

$$
\boxed{
A_{j_\ast}
=
\left\{
t\in A:
\int
\chi_{j_\ast,r}\Pi^s
>
0
\right\}
}
\tag{6.1}
$$

has positive measure.

Let:

$$
h(t)
=
\int
\chi_{j_\ast,r}\Pi^s(x,t)
\,dx.
$$

Then:

$$
h>0
$$

on a set of positive measure.

By the Lebesgue differentiation theorem, there exists a Lebesgue point:

$$
t_\ast
$$

with:

$$
h(t_\ast)>0.
$$

Therefore there are arbitrarily small intervals:

$$
J_\ast
\ni
t_\ast
$$

such that:

$$
\boxed{
\int_{J_\ast}
h(t)
\,dt
>
0.
}
\tag{6.2}
$$

Choose a fixed nonnegative reference bump:

$$
\eta\in C_c^\infty((-1,1))
$$

with:

$$
\eta(0)>0.
$$

By choosing a sufficiently small interval around:

$$
t_\ast,
$$

the rescaled pullback of:

$$
\eta
$$

also has positive pairing.

Hence the local spacetime detector can use one fixed reference profile:

$$
\boxed{
\phi_{j_\ast}(x,t)
=
\chi_{j_\ast,r}(x)
\eta
\left(
\frac{
t-t_\ast
}{
\delta
}
\right).
}
\tag{6.3}
$$

The only adaptive data are:

- spatial center;
- temporal center;
- temporal thickness.

These are already standard moving-window / re-root variables.

No solution-dependent detector **shape** is required.

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 7. NEW THEOREM — exact global-to-local heat-PFET bridge

## Theorem 7.1

Assume:

$$
\lambda
\int_I
(F_s)_+
dt
>
0.
$$

Let:

$$
r
=
\lambda^{-1}.
$$

Then there exists a finite parabolic window:

$$
W
=
B_{Cr}(x_\ast)
\times
J_\ast
$$

and a fixed-shape nonnegative local test:

$$
\phi
$$

such that:

$$
\boxed{
r^{-1}
\int_W
\phi(x,t)
\Pi^s(x,t)
\,dxdt
>
0.
}
\tag{7.1}
$$

If instead:

$$
\lambda
\int_I
(F_s)_-
dt
>
0,
$$

then there exists a finite window and test with:

$$
\boxed{
r^{-1}
\int_W
\phi\Pi^s
\,dxdt
<
0.
}
\tag{7.2}
$$

### Proof

Apply Section 6 with:

$$
r=\lambda^{-1}.
$$

Multiply the nonzero local pairing by:

$$
r^{-1}=\lambda.
$$

The sign is unchanged.

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

# 8. Corollary — exact PFET-zero kernel cannot contain a heat-work event

Assume the internal heat-filter branch is included in the resolved-flux channel:

$$
O_W^F.
$$

If:

$$
O_W^F=0
$$

for every admissible re-rooted local heat-filter window, then:

$$
\boxed{
F_s(t)=0
}
\tag{8.1}
$$

almost everywhere for that filter scale along the corresponding physical interval.

Indeed any positive or negative whole-space work event would produce a nonzero local flux detector by Theorem 7.1.

Therefore:

$$
\boxed{
\textbf{
exact heat-PFET invisibility}
\Longrightarrow
\textbf{
no nonzero whole-space heat-filter work event}.
}
}
\tag{8.2}
$$

Combining with DCRP-11:

$$
\boxed{
\textbf{
supplier heat-band first crossing}
\notin
\ker O_W^F.
}
}
\tag{8.3}
$$

Consequently, under the internal MORP meaning:

$$
\mathsf O_{\rm PFET}=0
$$

which includes the heat-resolved flux channel,

$$
\boxed{
\textbf{
a supplier heat-band first-crossing event is excluded from the exact PFET-zero kernel.
}
}
\tag{8.4}
$$

Status:

$$
\boxed{
\textbf{PROVED conditional only on compiler inclusion of the already-established FCBP-04 heat-flux channel in }O_W^F.
}
$$

This is a compiler-membership condition, not a new PDE estimate.

---

# 9. Why pressure cancellation no longer blocks exact localization

The external local scalar work is:

$$
\mathcal W
=
\mathcal F
+
\mathcal P.
$$

A nonzero:

$$
\mathcal F
$$

may be canceled by:

$$
\mathcal P
$$

inside:

$$
\mathcal W.
$$

But FCBP-05's internal observation vector contains:

$$
O_W^F
$$

and:

$$
O_W^P
$$

separately.

Therefore:

$$
\boxed{
\mathcal F\ne0
\Longrightarrow
O_W^{comb}\ne0
}
\tag{9.1}
$$

for the internal combined observation norm, regardless of scalar combined-work cancellation.

This is exactly why DCRP-12 uses the FCBP-05 combined **observation map**, not only the external scalar work detector.

---

# 10. Quantitative localization is harder than exact localization

Theorem 7.1 gives:

$$
\text{global nonzero}
\Longrightarrow
\text{local nonzero}.
$$

It does **not** give a universal constant:

$$
c_\ast>0
$$

such that:

$$
\left|
r^{-1}
\int_W
\phi\Pi^s
\right|
\ge
c_\ast.
$$

A fixed global work amount may be spread over many disjoint normalized cells.

This is not a technicality.

It is the exact quantitative anti-phantom problem.

---

# 11. NO-GO — fixed total work does not imply fixed local share

Let:

$$
N\in\mathbb N.
$$

Consider a model nonnegative normalized work density consisting of:

$$
N
$$

mutually disjoint, congruent normalized parabolic packets:

$$
w_N
=
\frac1N
\sum_{j=1}^N
w^{(j)},
$$

with:

$$
\int
w^{(j)}
=
1.
$$

Then:

$$
\int
w_N
=
1,
$$

but every packet carries only:

$$
\frac1N.
$$

Thus:

$$
\boxed{
\sup_{\text{unit normalized cell}}
\int_{\text{cell}}
w_N
\to0.
}
\tag{11.1}
$$

while total work remains fixed.

Therefore:

$$
\boxed{
\textbf{
global critical work}
\not\Rightarrow
\textbf{
uniform local critical work}
}
\tag{11.2}
$$

at the level of measure theory.

This model is not asserted to be generated by a Navier--Stokes solution.

Its role is to prove that a quantitative local lower bound requires additional PDE structure.

Status:

$$
\boxed{
\textbf{NO-GO PROVED at the measure-theoretic level}.
}
$$

---

# 12. Critical normalized work measures

For the forward heat-work branch define:

$$
\boxed{
d\mu_n^+
=
\lambda_n
(\Pi_n)_+
\,dxdt.
}
\tag{12.1}
$$

DCRP-11 implies:

$$
\boxed{
\mu_n^+
(
I_n\times\mathbb R^3
)
\ge
c_{HB}\nu^2.
}
\tag{12.2}
$$

Likewise, on the backscatter branch:

$$
\boxed{
d\mu_n^-
=
\lambda_n
(\Pi_n)_-
\,dxdt
}
\tag{12.3}
$$

has total mass bounded below.

Normalize:

$$
\boxed{
\widehat\mu_n^\pm
=
\frac{
\mu_n^\pm
}{
\mu_n^\pm(
I_n\times\mathbb R^3
)
}.
}
\tag{12.4}
$$

These are probability measures.

Introduce parabolic coordinates:

$$
y
=
\lambda_n
(
x-x_n
),
$$

$$
\tau
=
\lambda_n^2
(
t-t_n
),
$$

where:

$$
x_n,t_n
$$

are allowed package re-root coordinates.

The normalized measures live on a parabolic scale-one spacetime.

---

# 13. Cell concentration function

Fix a reference normalized parabolic cell:

$$
\mathcal Q_R
=
B_R(0)
\times
(-R^2,0).
$$

Define the concentration function:

$$
\boxed{
\mathfrak C_n(R)
=
\sup_{(y_0,\tau_0)}
\widehat\mu_n^\pm
\left(
B_R(y_0)
\times
(\tau_0-R^2,\tau_0)
\right).
}
\tag{13.1}
$$

There are two possibilities after subsequence extraction.

### Tight / concentrated work

For some:

$$
R<\infty,
$$

$$
\boxed{
\limsup_n
\mathfrak C_n(R)
>
0.
}
\tag{13.2}
$$

### Vanishing / diffuse work

For every fixed:

$$
R<\infty,
$$

$$
\boxed{
\mathfrak C_n(R)
\to0.
}
\tag{13.3}
$$

This is the standard concentration-versus-vanishing alternative at fixed parabolic scale.

---

# 14. NEW THEOREM — local flux / backscatter / escape trichotomy

## Theorem 14.1

Let:

$$
\mu_n
$$

be one of the positive critical work measures:

$$
\mu_n^+
$$

or:

$$
\mu_n^-,
$$

with:

$$
\mu_n(\mathbb R^3\times I_n)
\ge
m_0>0.
$$

After subsequence extraction, at least one of the following occurs.

### A. Local work concentration

There exist:

$$
R<\infty,
$$

$$
\eta>0,
$$

and normalized parabolic cells:

$$
Q_n
$$

such that:

$$
\boxed{
\mu_n(Q_n)
\ge
\eta m_0.
}
\tag{14.1}
$$

### B. Spatial / temporal work vanishing

For every fixed:

$$
R,
$$

$$
\boxed{
\sup_{Q_R}
\mu_n(Q_R)
\to0.
}
\tag{14.2}
$$

In branch B, after recentering at any sequence of scale-one cells, the normalized work measures converge locally to zero.

Equivalently, their mass leaves every bounded normalized spacetime region.

### Proof

Apply the concentration function of Section 13.

If:

$$
\limsup_n
\mathfrak C_n(R)>0
$$

for some:

$$
R,
$$

take:

$$
\eta
$$

below that positive limit and select maximizing cells.

Otherwise:

$$
\mathfrak C_n(R)\to0
$$

for every:

$$
R,
$$

which is exactly B.

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

# 15. Concentrated positive work gives visibility or paid cancellation

Suppose branch A of Theorem 14.1 occurs for the positive flux measure:

$$
\mu_n^+.
$$

Let:

$$
Q_n
$$

be a cell with:

$$
\boxed{
\lambda_n
\int_{Q_n}
(\Pi_n)_+
\,dxdt
\ge
\eta m_0.
}
\tag{15.1}
$$

Let:

$$
N_n
=
\lambda_n
\int_{Q_n}
(\Pi_n)_-
\,dxdt.
$$

There are two cases.

### Visible signed flux

If:

$$
N_n
\le
\frac12
\eta m_0,
$$

then:

$$
\boxed{
\lambda_n
\int_{Q_n}
\Pi_n
\,dxdt
\ge
\frac12
\eta m_0.
}
\tag{15.2}
$$

A fixed nonnegative cutoff supported slightly larger than:

$$
Q_n
$$

therefore gives a nonzero resolved-flux observation.

### Local backscatter payment

If:

$$
N_n
>
\frac12
\eta m_0,
$$

then:

$$
\boxed{
\lambda_n
\int_{Q_n}
(\Pi_n)_-
\,dxdt
\ge
\frac12
\eta m_0.
}
\tag{15.3}
$$

Thus a fixed positive amount of local backscatter is present.

Therefore:

$$
\boxed{
\textbf{
local positive-work concentration}
\Longrightarrow
\textbf{
local resolved-flux visibility}
\ \vee\
\textbf{
local paid backscatter}.
}
}
\tag{15.4}
$$

The same conclusion, with signs reversed, applies when the original DCRP-11 branch is already backscatter-dominated.

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 16. Work-escape as a native PDE residual

Branch B of Theorem 14.1 is not a zero object.

The total normalized work mass remains:

$$
\ge m_0,
$$

but every bounded normalized spacetime cell sees asymptotically zero mass.

This is exactly a non-tight native carrier.

MORP-02 already implements the same compactness principle for:

- relative-frequency carrier mass;
- normalized spatial carrier mass;
- selected trace mass.

In particular it explicitly distinguishes:

$$
\boxed{
\text{finite spatial carrier}
}
$$

from:

$$
\boxed{
\text{spatial defect at }\infty_x.
}
$$

MORP-01 reserves:

$$
\boxed{
\mathsf R_{\rm nat}
}
$$

for:

> any retained native residual not already included above.

The heat-work measure:

$$
\mu_n^\pm
$$

is generated directly from:

$$
u
$$

through the Navier--Stokes heat coarse-graining:

$$
\Pi^s
=
-
R^s:\nabla U^s.
$$

It contains no copied dangerous label.

Therefore a compactified space/time escape coordinate for:

$$
\mu_n^\pm
$$

is a legitimate **native PDE residual candidate**.

This is a package completion, not a new danger detector.

Status:

$$
\boxed{
\textbf{ARCHITECTURALLY ADMISSIBLE under the existing MORP native-residual definition}.
}
$$

The scalar lower-semicontinuous cost realization of this coordinate is not yet fixed.

---

# 17. Work-completed package theorem

Define a **work-completed MORP package** to retain:

1. the existing state / pressure / trace / scale coordinates;
2. the local heat-resolved flux / backscatter channel;
3. if the normalized heat-work carrier is non-tight, its compactified spatial / temporal escape coordinate.

## Theorem 17.1

Every DCRP-11 supplier heat-band first-crossing sequence has, after subsequence extraction, at least one of:

$$
\boxed{
O_W^F>0,
}
\tag{17.1}
$$

$$
\boxed{
\mathsf{Paid}>0,
}
\tag{17.2}
$$

or:

$$
\boxed{
\mathsf R_{\rm work}>0,
}
\tag{17.3}
$$

where:

$$
\mathsf R_{\rm work}
$$

is the retained compactified work-escape coordinate.

### Proof

Use Theorem 14.1.

If work concentrates, apply Section 15.

If it vanishes locally, retain the non-tight work carrier as:

$$
\mathsf R_{\rm work}.
$$

$$
\square
$$

Status:

$$
\boxed{
\textbf{PROVED at the package-alternative level}.
}
$$

---

# 18. Consequence for the MORP exact zero kernel

Suppose the concrete native-residual implementation includes:

$$
\mathsf R_{\rm work}
$$

as an instance of:

$$
\mathsf R_{\rm nat}.
$$

Then a supplier first-crossing sequence cannot satisfy simultaneously:

$$
\boxed{
O_W^F=0,
}
$$

$$
\boxed{
\mathsf{Paid}=0,
}
$$

and:

$$
\boxed{
\mathsf R_{\rm nat}=0.
}
$$

Therefore:

$$
\boxed{
\textbf{
the supplier first-crossing mechanism is absent from the
work-completed exact zero-cost PFET/Paid/native kernel.
}
}
\tag{18.1}
$$

Status:

$$
\boxed{
\textbf{PROVED conditional on the explicit work-residual package completion}.
}
$$

This does not yet imply Navier--Stokes regularity.

A positive but arbitrarily small local observation cost may remain.

---

# 19. Why this does not yet give a positive coercive gap

The trichotomy proves:

$$
\text{nonzero}
\vee
\text{defect}.
$$

It does not prove a universal quantitative constant for the local visible channel.

A sequence may satisfy:

$$
\boxed{
\max_{\text{unit cells}}
\lambda_n
\left|
\int_{\text{cell}}
\Pi_n
\right|
\to0
}
\tag{19.1}
$$

while total positive / negative critical work remains bounded below, provided the number of active normalized cells diverges.

If that divergence appears as work escape, the completed residual detects it.

But to turn the entire mechanism into a uniform positive scalar cost one must prove a quantitative relationship between:

- local detector norm;
- backscatter tax;
- work-escape residual norm.

That is an additional coercivity theorem.

---

# 20. Connection with FCBP-05's half-exponent barrier

FCBP-05 already identifies the moving-window observability problem as quantitative.

Its sharp temporal theorem shows that the threshold:

$$
\gamma q
=
\frac12
$$

separates window-growth laws that can or cannot be made effective on finite-time horizon schedules.

DCRP-12 explains how that older temporal barrier appears in the present supplier route.

The **qualitative** statement:

$$
\text{global work}
\Longrightarrow
\text{some local work}
$$

is easy.

The difficult statement is:

$$
\boxed{
\text{global critical work}
\Longrightarrow
\text{uniformly nonvanishing normalized local detector}
}
\tag{20.1}
$$

on windows whose centers / thicknesses / multiplicities may change with scale.

Thus the frontier has returned to a sharp quantitative Critical Lift problem, but now for a highly specific NS-generated work carrier rather than an abstract dangerous package.

---

# 21. A stronger quantitative target

Let:

$$
\mu_n
$$

be the normalized forward/backscatter work carrier.

Define its effective parabolic multiplicity:

$$
\boxed{
\mathfrak M_{\rm work}(n)
=
\left[
\sup_{z}
\widehat\mu_n
(
Q_1(z)
)
\right]^{-1}.
}
\tag{21.1}
$$

If:

$$
\mathfrak M_{\rm work}
$$

is uniformly bounded, then:

$$
\boxed{
\sup_z
\widehat\mu_n(Q_1(z))
\ge
c>0,
}
\tag{21.2}
$$

and Section 15 gives a uniform local PFET / backscatter gap.

Therefore only:

$$
\boxed{
\mathfrak M_{\rm work}\to\infty
}
\tag{21.3}
$$

can defeat uniform local observability.

This is now the exact quantitative diffuse-work branch.

The next question is whether Navier--Stokes can sustain:

$$
\mathfrak M_{\rm work}\to\infty
$$

while simultaneously satisfying the supplier / first-crossing / minimal-return constraints.

---

# 22. Candidate finite-energy multiplicity control and why it is not immediate

One might hope that finite kinetic energy bounds the number of active work cells.

This is not automatic.

At physical scale:

$$
r_n
=
\lambda_n^{-1},
$$

a scale-critical kinetic packet has raw energy:

$$
O(r_n).
$$

Therefore the finite total energy budget can still accommodate:

$$
O(r_n^{-1})
$$

such packets at one scale.

As:

$$
r_n\to0,
$$

this number diverges.

Thus:

$$
\boxed{
\text{finite kinetic energy alone}
\not\Rightarrow
\text{bounded work multiplicity}.
}
\tag{22.1}
$$

This is the same critical-summability geometry encountered earlier in CFOP / FCBP.

A new PDE interaction or recurrence constraint is required.

---

# 23. New exact frontier

The Heat-Flux Localization / Package-Completion Lemma is now closed at the qualitative level.

The remaining closure-facing target is:

$$
\boxed{
\textbf{
Quantitative Work Anti-Diffusion / Critical Lift Lemma}.
}
$$

A useful sufficient form would be:

> For every supplier heat-band first-crossing sequence generated by a hypothetical singular branch, one has either:
>
> $$
> \sup_n
> \mathfrak M_{\rm work}(n)
> <
> \infty,
> $$
>
> or a strictly positive native diffuse-work cost survives with a lower-semicontinuous scalar normalization.

If the first alternative holds, the local PFET / paid gap is uniformly positive.

If the second holds, exact minimal invisibility is impossible in the completed package.

The unresolved part is to obtain a **uniform scalar coercive gap**, not merely a nonzero coordinate.

---

# 24. Possible next attack — use the supplier center and first-crossing persistence

DCRP-08 gives a genuine localized supplier atom after critical rescaling.

DCRP-10 gives a first-crossing interval on which the supplier shell stays between two fixed critical levels.

This extra structure is not present in the abstract measure-theoretic no-go of Section 11.

A promising next attack is:

1. anchor normalized work cells at the supplier center;
2. use the localized shell energy identity to show that work lying far from the supplier must enter through boundary transport / pressure / nonlocal interaction;
3. charge that transport to existing leakage / native residual channels;
4. conclude that either a fixed fraction of the work remains within a bounded normalized distance from the supplier, or the paid/native transport cost is positive.

This would turn the supplier's endpoint localization into a quantitative work-tightness theorem.

The next round should attack exactly this anchored form rather than arbitrary work measures.

---

# 25. Source ledger

## Internal FCBP-05

Relevant internal statement:

$$
O_W^{comb}
=
(
O_W^P,
O_W^F,
O_W^E,
O_W^T
),
$$

with active pressure, resolved flux, positive energy, and adjoint-trace channels.

Thus:

$$
O_W^F
$$

is a separate observation coordinate.

## Internal MORP-01

Defines:

$$
\mathsf R_{\rm nat}
$$

for:

> any retained native residual not already included above.

## Internal MORP-02

Already develops defect completion by:

- one-point compactification of relative-frequency carrier distributions;
- analogous compactification for normalized spatial carrier measures;
- retention of trace / scale / spatial escape rather than silent loss.

DCRP-12 applies the same compactness pattern to the PDE-generated heat-work carrier.

## External Yu coarse-grained work theorem

The external theorem confirms:

- local resolved flux:

  $$
  \mathcal F_{I,r}[\phi]
  =
  r^{-1}
  \int
  \phi\Pi;
  $$

- local pressure work;
- combined distribution:

  $$
  G
  =
  \Pi+\nabla\cdot(PU);
  $$

- explicit pressure--flux cancellation ledger;
- finite-dimensional active work coefficients;
- the fact that coarse observability is a separate problem and is not automatic from resolved badness.

The external active detector itself is a detector for:

$$
G,
$$

not for the sum of absolute pressure and flux channels.

DCRP-12's separate-flux conclusion uses the **internal FCBP-05 observation map**, not an attribution to the external scalar detector theorem.

---

# 26. End state

The DCRP-11 localization gap has been reduced to a quantitative issue.

The exact qualitative theorem is:

$$
\boxed{
\text{nonzero global heat-filter work}
\Longrightarrow
\text{nonzero local heat-flux pairing}.
}
$$

For a sequence with fixed total critical work:

$$
\boxed{
\text{local PFET visibility}
\ \vee\
\text{local paid backscatter}
\ \vee\
\text{space/time work escape}.
}
$$

When work escape is explicitly retained as the native residual already allowed by MORP:

$$
\boxed{
\text{supplier first crossing}
\notin
\ker
\left(
O_W^F,
\mathsf{Paid},
\mathsf R_{\rm nat}
\right).
}
$$

The remaining problem is not qualitative invisibility.

It is quantitative diffusion:

$$
\boxed{
\mathfrak M_{\rm work}\to\infty.
}
$$

Therefore the next single frontier is:

$$
\boxed{
\textbf{
Quantitative Work Anti-Diffusion / Critical Lift Lemma,
anchored at the supplier center.
}
}
$$

This is now the next exact attack.
