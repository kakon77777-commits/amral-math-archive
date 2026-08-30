# NS-DCRP-46 — Canonical Label Measure, Log-Radius Transport, Exponential Intake Cones, and Intermittent Super-DSS Sheet Exhaust

- date: 2026-08-17
- status: research proof checkpoint / material-transport correction-and-rigidity round
- canonical source: UTF-8 Markdown
- canonical math delimiters: `$...$` and `$$...$$`
- objective:
  1. correct the tempting but invalid identification of the DCRP-45 incoming-source radius with the outgoing amplified-sheet radius;
  2. identify the canonical similarity-material label measure;
  3. derive an exact weighted continuity identity for transported material sets;
  4. prove an exponential upper bound on the radius of positive-volume incoming ancestor sets under the strict critical-tail portal estimate;
  5. prove a global weighted-velocity integrability theorem from the strict tail-energy envelope;
  6. derive a positive-volume Lagrangian log-radius growth theorem;
  7. prove that any fixed positive fraction of a material cohort can escape only at ordinary exponential radius;
  8. combine this with DCRP-45 double-exponential capacity escape to prove that any super-DSS coherent sheet exhaust must occupy an exponentially vanishing material fraction;
  9. reinterpret the final rank-two survivor as a two-sided conveyor: exponential-scale low-amplitude intake and vanishing-volume super-DSS high-amplitude exhaust;
  10. identify weighted carrier concentration on vanishing material fractions as the next frontier.
- no full Navier--Stokes regularity claim is made.
- external primary calibration:
  - P. Constantin, M. Ignatova, V. Vicol, *On putative self-similarity for incompressible 3D Euler*, arXiv:2602.17570v3;
  - A. Enciso, A. J. Fernández, D. Meyer, *Vortex-sheet desingularization for three-dimensional ideal fluids*, arXiv:2607.19233;
  - H. Huang, *Exact Lagrangian Realization and Robust Strain Sensing in Incompressible Flow*, arXiv:2607.26895.
- internal dependencies:
  - DCRP-30/31 strict critical tail envelope;
  - DCRP-43 anchored shear Poincaré cocycle;
  - DCRP-45 logarithmic capacity and inward portal estimates.
- no novelty/priority claim is made without independent audit.

---

# 1. Executive correction

DCRP-45 produced two strong but logically distinct facts.

### outgoing amplified-sheet fact

On a coherent pure pancake contrast lineage, bounded planar enstrophy forces:

$$
\boxed{
\frac{R_m}{r_m}
\ge
\exp
\left[
c
\mu_r^{2m}
\right],
}
\tag{1.1}
$$

where:

$$
\boxed{
\mu_r
=
e^{(1-2\gamma)S_0}
>
1.
}
\tag{1.2}
$$

Thus the amplified high-shear interface can require double-exponential scale escape.

### incoming tail-portal fact

At suitable large radii:

$$
\boxed{
\mathcal F_{\rm in}(\rho)
\lesssim
\rho^{\kappa-2},
\qquad
0<\kappa<1.
}
\tag{1.3}
$$

DCRP-45 informally juxtaposed these two scales.

DCRP-46 records the necessary correction:

$$
\boxed{
\textbf{
the outgoing high-amplitude labels and incoming low-amplitude replacement labels need not be the same material cohort.
}
}
\tag{1.4}
$$

The canonical pancake conveyor may have:

$$
\boxed{
\text{low-amplitude intake}
\to
\text{core amplification}
\to
\text{high-amplitude exhaust}.
}
\tag{1.5}
$$

Therefore a direct contradiction between the incoming and outgoing radii is invalid without an additional recycling theorem.

Status:

$$
\boxed{
\textbf{CORRECTION}.
}
$$

The correct connection is through the geometry of **material volume and radial transport**.

---

# 2. Similarity-material flow

Let:

$$
\boxed{
W(y,s)
=
\gamma y+V(y,s).
}
\tag{2.1}
$$

The similarity material flow is:

$$
\boxed{
\partial_sY(a,s)
=
W(Y(a,s),s).
}
\tag{2.2}
$$

Since:

$$
\nabla\cdot V=0,
$$

$$
\boxed{
\nabla\cdot W
=
3\gamma.
}
\tag{2.3}
$$

Therefore:

$$
\boxed{
\det D_aY(a,s)
=
e^{3\gamma s}.
}
\tag{2.4}
$$

For one DSS period:

$$
\boxed{
J_\Phi
=
e^{3\gamma S_0}.
}
\tag{2.5}
$$

---

# 3. Canonical label measure

The spatial density:

$$
\boxed{
\rho_{\rm lab}(s)
=
e^{-3\gamma s}
}
\tag{3.1}
$$

satisfies:

$$
\boxed{
\partial_s\rho_{\rm lab}
+
\nabla\cdot
(
\rho_{\rm lab}W
)
=
0.
}
\tag{3.2}
$$

Thus:

$$
\boxed{
d\mu_{\rm lab}(s)
=
e^{-3\gamma s}dy
}
\tag{3.3}
$$

is the canonical similarity-material label measure.

Equivalently, for any transported material set:

$$
A_s=Y(A_0,s),
$$

$$
\boxed{
e^{-3\gamma s}
|A_s|
=
|A_0|.
}
\tag{3.4}
$$

This is simply the Jacobian law rewritten as an invariant measure.

---

# 4. Transported indicator continuity

Let:

$$
\chi(y,s)
$$

be the indicator of a smooth transported material set:

$$
A_s.
$$

Then:

$$
\boxed{
\partial_s\chi
+
W\cdot\nabla\chi
=
0.
}
\tag{4.1}
$$

Therefore:

$$
\boxed{
\partial_s
\left(
e^{-3\gamma s}\chi
\right)
+
\nabla\cdot
\left(
e^{-3\gamma s}\chi W
\right)
=
0.
}
\tag{4.2}
$$

This identity gives the correct material-volume ledger across a fixed sphere.

---

# 5. Incoming ancestor setup

Let:

$$
A_0
\subset
B_{R_0}
$$

be a measurable material set at phase:

$$
s=0,
$$

with:

$$
\boxed{
|A_0|
=
v_0>0.
}
\tag{5.1}
$$

For an integer:

$$
m\ge1,
$$

let:

$$
\boxed{
A_{-m}
=
Y(A_0,-mS_0).
}
\tag{5.2}
$$

Then:

$$
\boxed{
|A_{-m}|
=
J_\Phi^{-m}
v_0.
}
\tag{5.3}
$$

Suppose:

$$
A_{-m}
\subset
\mathbb R^3\setminus B_\rho,
$$

while:

$$
A_0
\subset B_\rho.
$$

Every material label in:

$$
A_{-m}
$$

must cross:

$$
\partial B_\rho
$$

inward at least once during:

$$
[-mS_0,0].
$$

---

# 6. Weighted inward flux identity

Integrate (4.2) over:

$$
B_\rho\times[-mS_0,0].
$$

The initial weighted mass inside:

$$
B_\rho
$$

is zero.

The final weighted mass is:

$$
v_0.
$$

Therefore:

$$
\boxed{
v_0
=
-\int_{-mS_0}^{0}
e^{-3\gamma s}
\int_{\partial B_\rho}
\chi
W\cdot n
\,dSds.
}
\tag{6.1}
$$

The signed flux may contain multiple crossings.

Taking the gross inward part gives:

$$
\boxed{
v_0
\le
\int_{-mS_0}^{0}
e^{-3\gamma s}
\int_{\partial B_\rho}
(-W\cdot n)_+
\,dSds.
}
\tag{6.2}
$$

---

# 7. Periodic reduction of weighted flux

Because:

$$
W(y,s+S_0)=W(y,s),
$$

the ordinary one-period inward flux:

$$
\boxed{
\mathcal F_{\rm in}(\rho)
=
\int_0^{S_0}
\int_{\partial B_\rho}
(-W\cdot n)_+
dSds
}
\tag{7.1}
$$

is the same on every period.

On the:

$$
j
$$

th backward period, the weight:

$$
e^{-3\gamma s}
$$

is at most:

$$
J_\Phi^j.
$$

Hence:

$$
v_0
\le
\mathcal F_{\rm in}(\rho)
\sum_{j=1}^{m}
J_\Phi^j.
$$

Therefore:

$$
\boxed{
\mathcal F_{\rm in}(\rho)
\ge
c_J
J_\Phi^{-m}
v_0,
}
\tag{7.2}
$$

where:

$$
\boxed{
c_J
=
\frac{
J_\Phi-1
}{
J_\Phi
}
}
\tag{7.3}
$$

up to the harmless finite:

$$
(1-J_\Phi^{-m})^{-1}
$$

factor.

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

This is the correct **canonical shrinking-volume replenishment demand**.

---

# 8. Correction to fixed-positive-volume replenishment

DCRP-45 proved that a fixed positive ordinary material volume cannot be transported inward from arbitrarily large radii each period.

DCRP-46 shows the canonical requirement is weaker:

$$
\boxed{
\text{required ancestor volume at generation }m
\sim
J_\Phi^{-m}.
}
\tag{8.1}
$$

Thus the final branch does not require a generation-independent material volume.

The correct portal comparison must use:

$$
J_\Phi^{-m},
$$

not a fixed positive constant.

---

# 9. Portal-limited incoming source radius

At the good radii of DCRP-45:

$$
\boxed{
\mathcal F_{\rm in}(\rho)
\le
C
\rho^{\kappa-2}.
}
\tag{9.1}
$$

Combine with (7.2):

$$
c_J
v_0
J_\Phi^{-m}
\le
C
\rho^{\kappa-2}.
$$

Since:

$$
2-\kappa>0,
$$

$$
\boxed{
\rho^{2-\kappa}
\le
C
v_0^{-1}
J_\Phi^m.
}
\tag{9.2}
$$

Therefore:

$$
\boxed{
\rho
\le
C(v_0)
J_\Phi^{
m/(2-\kappa)
}.
}
\tag{9.3}
$$

Thus a positive-volume ancestor set which actually enters the recurrent core through a good-radius tail portal can originate only at an **ordinary exponential radius** in the backward generation index.

Status:

$$
\boxed{
\textbf{PROVED UNDER THE DECLARED OUTSIDE-TO-INSIDE MATERIAL-TUBE HYPOTHESIS}.
}
$$

---

# 10. Incoming source-cone exponent

Define:

$$
\boxed{
\chi_{\rm in}
=
\frac{
\log J_\Phi
}{
2-\kappa
}.
}
\tag{10.1}
$$

Then:

$$
\boxed{
\limsup_{m\to\infty}
\frac1m
\log\rho_m
\le
\chi_{\rm in}.
}
\tag{10.2}
$$

Using:

$$
J_\Phi=e^{3\gamma S_0},
$$

$$
\boxed{
\chi_{\rm in}
=
\frac{
3\gamma S_0
}{
2-\kappa
}.
}
\tag{10.3}
$$

Since:

$$
\kappa
=
5-\frac2\gamma,
$$

$$
\boxed{
2-\kappa
=
\frac{
2-3\gamma
}{
\gamma
},
}
\tag{10.4}
$$

and therefore:

$$
\boxed{
\chi_{\rm in}
=
\frac{
3\gamma^2
}{
2-3\gamma
}
S_0.
}
\tag{10.5}
$$

The incoming positive-volume source cone is exponentially bounded.

---

# 11. Weighted velocity integrability from the critical tail

Assume the strict period-integrated tail envelope:

$$
\boxed{
\int_0^{S_0}
\int_{B_R}
|V(y,s)|^2dyds
\le
C_E
R^\kappa,
\qquad
0<\kappa<1.
}
\tag{11.1}
$$

Then:

$$
\boxed{
\int_0^{S_0}
\int_{\mathbb R^3}
\frac{
|V(y,s)|^2
}{
(1+|y|)^2
}
dyds
<
\infty.
}
\tag{11.2}
$$

### Proof

Decompose:

$$
\mathbb R^3
=
B_2
\cup
\bigcup_{j\ge1}
\left(
B_{2^{j+1}}
\setminus
B_{2^j}
\right).
$$

On the:

$$
j
$$

th shell:

$$
(1+|y|)^{-2}
\lesssim
2^{-2j}.
$$

Therefore the shell contribution is bounded by:

$$
C
2^{-2j}
2^{\kappa(j+1)}
=
C
2^{(\kappa-2)j}.
$$

The series converges because:

$$
\kappa<2.
$$

The inner region is finite by smoothness.

$$
\square
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

The strict branch gives the stronger:

$$
\kappa<1.
$$

---

# 12. Positive-volume material cohort

Let:

$$
A_0
$$

be any measurable label set with:

$$
\boxed{
0<v_0=|A_0|<\infty.
}
\tag{12.1}
$$

Let:

$$
A_s=Y(A_0,s).
$$

Then:

$$
\boxed{
|A_s|
=
e^{3\gamma s}
v_0.
}
\tag{12.2}
$$

Define the label-average logarithmic radius:

$$
\boxed{
L_{A_0}(s)
=
\frac1{v_0}
\int_{A_0}
\log
\left(
1+|Y(a,s)|
\right)
da.
}
\tag{12.3}
$$

---

# 13. Pointwise radial-log inequality

Along one trajectory:

$$
\frac d{ds}
|Y|
\le
\gamma|Y|
+
|V(Y,s)|.
$$

Therefore:

$$
\boxed{
\frac d{ds}
\log
\left(
1+|Y|
\right)
\le
\gamma
+
\frac{
|V(Y,s)|
}{
1+|Y|
}.
}
\tag{13.1}
$$

---

# 14. Lagrangian change of variables

By the Jacobian law:

$$
\boxed{
\int_{A_0}
f(Y(a,s),s)da
=
e^{-3\gamma s}
\int_{A_s}
f(y,s)dy.
}
\tag{14.1}
$$

Hence:

$$
\begin{aligned}
L_{A_0}'(s)
&\le
\gamma
+
\frac{
e^{-3\gamma s}
}{
v_0
}
\int_{A_s}
\frac{
|V(y,s)|
}{
1+|y|
}
dy
\\
&\le
\gamma
+
v_0^{-1/2}
e^{-3\gamma s/2}
H(s),
\end{aligned}
\tag{14.2}
$$

where:

$$
\boxed{
H(s)
=
\left[
\int_{\mathbb R^3}
\frac{
|V(y,s)|^2
}{
(1+|y|)^2
}
dy
\right]^{1/2}.
}
\tag{14.3}
$$

---

# 15. Periodic weighted-velocity summation

The DSS profile is periodic in:

$$
s,
$$

so:

$$
H(s+S_0)=H(s).
$$

By Section 11:

$$
H\in L^2(0,S_0).
$$

Therefore:

$$
\boxed{
\int_0^\infty
e^{-3\gamma s/2}
H(s)ds
<
\infty.
}
\tag{15.1}
$$

Indeed the integral is a geometric sum of period copies.

---

# 16. NEW THEOREM — Material Log-Radius Growth Bound

## Theorem 16.1

For every finite positive-volume material cohort:

$$
A_0,
$$

there is a finite constant:

$$
C_{A_0}
$$

such that:

$$
\boxed{
L_{A_0}(s)
\le
L_{A_0}(0)
+
\gamma s
+
C_{A_0}
}
\tag{16.1}
$$

for all:

$$
s\ge0.
$$

One may take:

$$
\boxed{
C_{A_0}
=
v_0^{-1/2}
\int_0^\infty
e^{-3\gamma s/2}
H(s)ds.
}
\tag{16.2}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

This is a strict-tail Lagrangian travel theorem.

---

# 17. Positive-fraction radial escape

For:

$$
R>0,
$$

define the label fraction:

$$
\boxed{
\theta_{A_0}(R,s)
=
\frac1{v_0}
\left|
\left\{
a\in A_0:
|Y(a,s)|\ge R
\right\}
\right|.
}
\tag{17.1}
$$

Since:

$$
\log(1+|Y|)
\ge
\log(1+R)
$$

on this set:

$$
\boxed{
\theta_{A_0}(R,s)
\log(1+R)
\le
L_{A_0}(s).
}
\tag{17.2}
$$

Use Theorem 16.1:

$$
\boxed{
\theta_{A_0}(R,s)
\le
\frac{
L_{A_0}(0)
+
\gamma s
+
C_{A_0}
}{
\log(1+R)
}.
}
\tag{17.3}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 18. NEW THEOREM — No Positive-Fraction Super-DSS Escape

## Theorem 18.1

Fix:

$$
\theta_0>0.
$$

If for a sequence:

$$
s_m=mS_0
$$

one has:

$$
\boxed{
\theta_{A_0}(R_m,s_m)
\ge
\theta_0,
}
\tag{18.1}
$$

then:

$$
\boxed{
\log(1+R_m)
\le
C_{\theta_0,A_0}
(1+m).
}
\tag{18.2}
$$

Hence:

$$
\boxed{
R_m
\le
C
e^{Cm}.
}
\tag{18.3}
$$

A fixed positive material fraction cannot travel to a double-exponential radius in the DSS generation index.

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 19. Double-exponential sheet escape implies material intermittency

DCRP-45's bounded-planar-enstrophy coherent branch requires:

$$
\boxed{
\log R_m
\ge
c
\mu_r^{2m}
}
\tag{19.1}
$$

up to a fixed inner scale.

Insert this into (17.3):

$$
\boxed{
\theta_{A_0}(R_m,mS_0)
\le
C
(1+m)
\mu_r^{-2m}.
}
\tag{19.2}
$$

Therefore any material cohort which reaches the double-exponential sheet scale occupies an exponentially vanishing fraction of the original positive-volume cohort.

This is the **super-DSS material intermittency theorem**.

Status:

$$
\boxed{
\textbf{PROVED ON THE COHERENT BOUNDED-ENSTROPHY ESCAPE BRANCH}.
}
$$

---

# 20. Intermittency exponent

Define:

$$
\boxed{
\iota_{\rm mat}
=
\liminf_{m\to\infty}
-\frac1m
\log
\theta_m.
}
\tag{20.1}
$$

For the DCRP-45 bounded-enstrophy double-exponential exhaust:

$$
\boxed{
\iota_{\rm mat}
\ge
2
\log\mu_r
=
2(1-2\gamma)S_0.
}
\tag{20.2}
$$

Thus the material support of the super-DSS exhaust becomes exponentially sparse in label measure.

---

# 21. Why incoming and outgoing scales can coexist

The incoming ancestor scale obeys an ordinary exponential bound:

$$
\boxed{
\rho_m^{in}
\lesssim
e^{\chi_{\rm in}m}.
}
\tag{21.1}
$$

The bounded-enstrophy outgoing sheet interface may obey:

$$
\boxed{
\log
\rho_m^{out}
\gtrsim
\mu_r^{2m}.
}
\tag{21.2}
$$

These are not contradictory because the cohorts are different.

The correct conveyor geometry is:

$$
\boxed{
\textbf{
moderately remote low-amplitude intake}
}
\to
\boxed{
\textbf{
core amplification}
}
\to
\boxed{
\textbf{
extremely remote high-amplitude intermittent exhaust}.
}
}
\tag{21.3}
$$

This is the corrected two-sided material architecture.

---

# 22. Positive-volume traffic cone

Theorems 9.3 and 18.1 have a common interpretation.

### backward positive-volume traffic

A positive-volume ancestor set feeding the core through the strict tail cannot originate beyond an ordinary exponential radius.

### forward positive-fraction traffic

A positive fraction of a finite-volume core cohort cannot travel beyond an ordinary exponential radius.

Thus:

$$
\boxed{
\textbf{
all positive-volume material traffic is confined to an ordinary exponential similarity cone.
}
}
\tag{22.1}
$$

Any super-DSS material motion must be supported on a vanishing label fraction.

This is a much more precise statement than "tail escape."

---

# 23. Relation to DCRP-43 finite residence

DCRP-43 proved that nonzero pure-cocycle shear labels cannot return infinitely often to a fixed compact core.

DCRP-46 adds:

$$
\boxed{
\textbf{
they also cannot leave the core in a positive-volume double-exponential front.
}
}
\tag{23.1}
$$

Therefore the outgoing shear exhaust has two broad components:

1. a positive-volume ordinary-exponential material cloud;

2. a super-DSS high-contrast sheet component whose label measure vanishes exponentially.

The second is the branch relevant to bounded planar enstrophy.

---

# 24. Critical amplitude--intermittency pairing

On the pure scalar cocycle:

$$
|\widetilde r|
$$

along one material label grows like:

$$
\mu_r^m.
$$

On the bounded-enstrophy super-DSS exhaust, the material fraction obeys:

$$
\theta_m
\lesssim
(1+m)
\mu_r^{-2m}.
$$

Therefore the product:

$$
\boxed{
\mu_r^{2m}\theta_m
}
\tag{24.1}
$$

is at most polynomially large under the current upper bound.

This is a new critical pairing:

$$
\boxed{
\textbf{
amplitude squared}
\times
\textbf{
material intermittency}
}
\tag{24.2}
$$

can remain at a borderline scale.

No contradiction follows from this pairing alone.

A lower-bound or reproduction theorem for the weighted carrier mass is needed.

---

# 25. Why material intermittency itself is not impossible

Thin vortex sheets and strongly concentrated vorticity layers are legitimate exact Euler mechanisms in suitable settings.

Likewise large Lagrangian deformation can occur in smooth incompressible flows.

Therefore:

$$
\boxed{
\textbf{
vanishing material fraction}
}
$$

or:

$$
\boxed{
\textbf{
strong geometric concentration}
}
$$

is not a contradiction by itself.

The remaining DCRP question must use a **weighted physical carrier**.

---

# 26. Candidate weighted cohort measures

Let:

$$
A_0^{(m)}
\subset
A_0
$$

be the labels entering the super-DSS exhaust at generation:

$$
m.
$$

Natural weighted label masses include:

$$
\boxed{
\mathcal M_{r,p}^{(m)}
=
\int_{A_0^{(m)}}
|\widetilde r(Y(a,mS_0),mS_0)|^p
da,
}
\tag{26.1}
$$

and the physical:

$$
\boxed{
\mathcal M_{\omega}^{(m)}
=
\int_{A_0^{(m)}}
|\Omega_h(Y(a,mS_0),mS_0)|^2
da.
}
\tag{26.2}
$$

The first is gauge-completed only after the declared anchored chart.

The second is fully physical.

The next theorem must show that recurrence demands a nonvanishing amount of one such weighted mass.

---

# 27. Weighted concentration consequence

Suppose for some nonnegative physical carrier:

$$
g_m(a)
$$

one has:

$$
\boxed{
\int_{A_0^{(m)}}
g_m(a)da
\ge
c_0>0
}
\tag{27.1}
$$

while:

$$
\boxed{
|A_0^{(m)}|
\le
C
(1+m)
\mu_r^{-2m}.
}
\tag{27.2}
$$

Then:

$$
\boxed{
\fint_{A_0^{(m)}}
g_m(a)da
\ge
c
\frac{
\mu_r^{2m}
}{
1+m
}.
}
\tag{27.3}
$$

Thus any fixed weighted physical throughput carried by the super-DSS exhaust forces exponential carrier concentration.

Status:

$$
\boxed{
\textbf{PROVED AS AN ELEMENTARY CONDITIONAL CONSEQUENCE}.
}
$$

This is the correct form of the v45 intuition.

---

# 28. Candidate physical choices

If:

$$
g_m
=
|\Omega_h|^2,
$$

then fixed weighted mass implies an exponentially large material-average planar enstrophy on the exhaust cohort.

If:

$$
g_m
=
|\nabla\Omega_h|^2,
$$

the result becomes a second-order concentration channel.

If:

$$
g_m
$$

is a PFET or strain supplier density, the concentration becomes a scale/transition carrier.

Which weighted mass is genuinely required by same-parent recurrence is not yet proved.

---

# 29. A local peak-versus-gradient refinement

Suppose a physical carrier is:

$$
g=|\Omega_h|^2
$$

and the weighted concentration produces a point:

$$
(y_m,s_m)
$$

with:

$$
\boxed{
|\Omega_h(y_m,s_m)|
=
M_m
\to\infty.
}
\tag{29.1}
$$

Let:

$$
L_m
=
\|\nabla\Omega_h(\cdot,s_m)\|_{L^\infty(B_1(y_m))}.
$$

Then either:

$$
\boxed{
\int_{B_1(y_m)}
|\Omega_h|^2
\ge
c
M_m^2,
}
\tag{29.2}
$$

or:

$$
\boxed{
L_m
\ge
c
M_m^{5/3}
\left[
\int_{B_1(y_m)}
|\Omega_h|^2
\right]^{-1/3}.
}
\tag{29.3}
$$

### Proof

If:

$$
L_m\le M_m/2,
$$

the unit-scale enstrophy lower bound follows immediately.

Otherwise choose:

$$
r_m
=
\min
\left(
1,
\frac{
M_m
}{
2L_m
}
\right).
$$

On:

$$
B_{r_m}(y_m),
$$

$$
|\Omega_h|
\ge
M_m/2.
$$

Hence:

$$
E_m
\ge
c
M_m^2r_m^3.
$$

Rearrange.

$$
\square
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

Thus pointwise portal/exhaust vorticity concentration converts into either bulk enstrophy or second-order vorticity-gradient concentration.

---

# 30. Connection to filtered-vorticity defect architecture

The existing filtered-vorticity theory treats positive stretching surplus through:

- near-field directional/increment defects;
- far-field strain;
- commutator forcing;
- localization.

DCRP-46's final concentration branches are compatible with that architecture:

- large:

  $$
  |\Omega_h|
  $$

  is an enstrophy reservoir;

- large:

  $$
  |\nabla\Omega_h|
  $$

  is a higher-order/difference-quotient supplier;

- loss of coherent material fraction is a transition/localization carrier.

No claim is made that the external filtered theorem automatically closes the branch.

---

# 31. Exact sheet calibration

Recent exact Euler theory constructs smooth vorticities concentrated in thin neighborhoods of analytic vortex sheets for a time interval uniform in the thickness parameter.

Therefore the exponentially small material fraction found here is not locally impossible by geometry alone.

The novelty of the DCRP constraint is its simultaneous coupling to:

- DSS amplitude amplification;
- strict sublinear tail energy;
- same-parent recurrence;
- PFET;
- finite residence;
- and the rank-two potential--shear structure.

---

# 32. Lagrangian flexibility calibration

Smooth incompressible flows can realize very large classes of one-particle volume-preserving deformation gradients.

Thus the log-radius theorem is intentionally a **positive-volume averaged** result.

It does not claim to bound exceptional one-particle trajectories.

The super-DSS branch survives precisely by becoming exceptional in material measure.

This quotient is necessary.

---

# 33. Corrected DCRP-46 branch tree

The strict coherent pure pancake conveyor now has:

### intake side

$$
\boxed{
\text{positive-volume incoming ancestors}
\subset
\text{ordinary exponential source cone}.
}
$$

### core

$$
\boxed{
\text{material amplification}
+
\text{finite residence}.
}
$$

### exhaust side

Either:

$$
\boxed{
\text{ordinary-exponential positive-volume exhaust}
}
$$

or, if planar enstrophy remains bounded while coherent contrast amplifies:

$$
\boxed{
\text{super-DSS exhaust}
+
\text{exponentially vanishing material fraction}.
}
$$

Thus the strongest survivor is a **highly intermittent sheet conveyor**, not an ordinary remote sheet.

---

# 34. What DCRP-46 closes

The following overstrong idea is removed:

> double-exponential outgoing interface radius contradicts exponential incoming source radius.

False without a recycling identification.

The following stronger and correct statements are proved:

1. the canonical incoming ancestor volume is:

   $$
   J_\Phi^{-m};
   $$

2. positive-volume incoming source radius is at most exponential;

3. every positive-volume material cohort has average log-radius growth at most:

   $$
   \gamma s+O(1);
   $$

4. any fixed positive fraction of a cohort has at most exponential radial escape;

5. double-exponential coherent sheet escape must therefore occur on an exponentially vanishing material fraction.

This replaces the invalid direct radius clash by a rigorous intermittency theorem.

---

# 35. Correct next frontier

The next target is:

$$
\boxed{
\textbf{
Intermittent Sheet Exhaust /
Weighted Physical Carrier Concentration.
}
}
$$

A useful theorem would prove that same-parent rank-two recurrence requires a fixed nonzero weighted amount of at least one physical carrier on the super-DSS exhaust cohort, for example:

$$
\boxed{
|\Omega_h|^2,
\qquad
|\nabla\Omega_h|^2,
\qquad
\text{strain/PFET density}.
}
$$

Then the material-fraction estimate:

$$
\theta_m
\lesssim
(1+m)\mu_r^{-2m}
$$

would force exponential concentration of that carrier.

A second theorem should convert that concentration into:

- filtered increment defects;
- second-order viscous residues;
- rank lifting;
- or a non-summable same-parent transition coordinate.

This is now the sharpest rank-two sheet-concentration frontier.

---

# 36. End state

The canonical similarity label measure is:

$$
\boxed{
d\mu_{\rm lab}
=
e^{-3\gamma s}dy.
}
$$

A positive-volume ancestor set feeding the core from:

$$
m
$$

periods in the past obeys:

$$
\boxed{
\mathcal F_{\rm in}(\rho)
\gtrsim
J_\Phi^{-m}|A_0|.
}
$$

The strict tail then forces:

$$
\boxed{
\rho_m^{in}
\lesssim
J_\Phi^{m/(2-\kappa)}.
}
$$

Thus positive-volume intake is only exponentially remote.

The strict tail also gives:

$$
\boxed{
\int_0^{S_0}
\int
\frac{
|V|^2
}{
(1+|y|)^2
}
<\infty.
}
$$

Consequently every positive-volume material cohort satisfies:

$$
\boxed{
\frac1{|A_0|}
\int_{A_0}
\log
\left(
1+|Y(a,s)|
\right)
da
\le
\gamma s+O(1).
}
$$

Hence a fixed positive material fraction can travel only to ordinary exponential radius.

If bounded planar enstrophy nevertheless forces:

$$
\log R_m
\gtrsim
\mu_r^{2m},
$$

then the material fraction at that super-DSS radius satisfies:

$$
\boxed{
\theta_m
\lesssim
(1+m)
\mu_r^{-2m}.
}
$$

Therefore the final coherent rank-two survivor is:

$$
\boxed{
\textbf{
an exponentially intermittent high-amplitude sheet exhaust fed by an ordinary-exponential low-amplitude intake.
}
}
$$

The next frontier is:

$$
\boxed{
\textbf{
Intermittent Sheet Exhaust /
Weighted Physical Carrier Concentration.
}
}
$$
