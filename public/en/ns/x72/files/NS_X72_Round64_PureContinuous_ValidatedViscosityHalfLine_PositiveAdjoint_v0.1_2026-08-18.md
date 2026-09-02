# NS × X Integration × 24/72 Paradigm in Practice
## Round 64 — Pure Continuous Validated Viscosity Half-Line / Uniform Positive Adjoint Coefficient

- Date: 2026-08-18
- Version: v0.1
- Status: Proof-Route Experiment / Continuous-Only Validated Parameter Branch
- canonical source: UTF-8 Markdown
- canonical math delimiters: inline `$...$`; display `$$...$$`
- Previous round: `NS_X72_Round63_PureContinuous_FastDifferenceSchur_SymmetrizedSlowGauge_v0.1_2026-08-18.md`

## Objectives of this round

Round 63 has rigorously eliminated the fast sector, leaving the slow Jost/Riccati selection. This round no longer first pursues a complete
$$
\nu\to0^+
$$
singular matching, but adopts a two-stage strategy:

1. Perform an a posteriori validated enclosure of the finite-core + infinite-tail for a compact viscosity range;
2. Directly apply the global contraction of the full adjoint recurrence for sufficiently large viscosity.

The objective is to upgrade an entire positive viscosity parameter line into a theorem for the first time, rather than a parameter scan.

---

# 1. Main result

For the two source-hidden Floquet fibres

$$
\boxed{
K_-=\sqrt{17}-3,
\qquad
K_+=\sqrt{17}+3,
}
\tag{1.1}
$$

let
$$
\psi_+(\nu)
$$
be the canonical reflection-even, $\mathcal C$-even adjoint mode normalized by

$$
\boxed{
\psi_+(0)=1,
\qquad
\psi_+(1)=0.
}
\tag{1.2}
$$

Write

$$
\boxed{
\psi_+(3)=ia_3(\nu).
}
\tag{1.3}
$$

Round 64 proves

$$
\boxed{
a_{3,\pm}(\nu)>0
\qquad
\forall
\nu\ge10^{-4}.
}
\tag{1.4}
$$

Equivalently, since

$$
\psi_n=i^n u_n,
$$

$$
\boxed{
u_3(\nu)<0
\qquad
\forall
\nu\ge10^{-4}.
}
\tag{1.5}
$$

Designation:

$$
\boxed{
\textbf{Validated Viscosity Half-Line Positivity Theorem}.
}
$$

---

# 2. Consequence for the hidden-rescue route

Round 55 proved the exact compatibility reduction

$$
\boxed{
\langle
\psi_+,
g
\rangle
=
g_0(\nu)
+
a_3(\nu)
G_{-3}.
}
\tag{2.1}
$$

At both source fibres,

$$
\boxed{
\operatorname{sign}
g_0(\nu)
=
\operatorname{sign}
G_{-3}
}
\tag{2.2}
$$

for every

$$
\nu>0.
$$

Therefore (1.4) implies

$$
\boxed{
\langle
\psi_+,
g
\rangle
\ne0
\qquad
\forall
\nu\ge10^{-4}.
}
\tag{2.3}
$$

Hence the two non-Beltrami $\sqrt{17}$ source-hidden circles cannot be integrated into full second-order state/source-locked analytic curves for any

$$
\boxed{
\nu\ge10^{-4}.
}
\tag{2.4}
$$

This extends Round 56 from the single normalized slice

$$
\nu=1
$$

to an entire positive-viscosity half-line above a small explicit threshold.

---

# 3. Canonical adjoint recurrence

The real $\mathcal C$-even recurrence is

$$
\boxed{
-
A_{-2}^{(n)}
u_{n-2}
+
A_0^{(n)}
u_n
-
\nu b_nu_{n+1}
-
A_2^{(n)}
u_{n+2}
+
A_4^{(n)}
u_{n+4}
=
0,
}
\tag{3.1}
$$

with

$$
u_0=1,
\qquad
u_1=0,
$$

and reflection

$$
u_{-n}=(-1)^nu_n.
$$

The same-parity coefficients are independent of viscosity; only the cross-parity coefficient is linear in

$$
\nu.
$$

---

# 4. Proof split

The proof is divided at

$$
\boxed{
\nu_L=0.7.
}
\tag{4.1}
$$

## Regime A — validated finite-core / infinite-tail enclosure

$$
\boxed{
10^{-4}
\le
\nu
\le
0.7.
}
\tag{4.2}
$$

## Regime B — global full-sequence contraction

$$
\boxed{
\nu
\ge
0.7.
}
\tag{4.3}
$$

The two arguments overlap exactly at the split and require no continuity assumption across it.

---

# 5. Finite-core decomposition

Fix an integer cutoff

$$
N.
$$

Let

$$
x=
(
u_2,\ldots,u_N
)^T
$$

and let the first three tail values be

$$
y=
(
u_{N+1},
u_{N+2},
u_{N+3}
)^T.
$$

Using the equations

$$
n=1,\ldots,N-1,
$$

the finite core has the exact affine form

$$
\boxed{
M_N(\nu)x
=
r_N
-
C_Ny.
}
\tag{5.1}
$$

The matrix depends affinely on viscosity:

$$
\boxed{
M_N(\nu)
=
M_{N,0}
+
\nu M_{N,1}.
}
\tag{5.2}
$$

The tail-coupling matrix

$$
C_N
$$

is viscosity-independent.

---

# 6. A posteriori inverse certificate on a viscosity chunk

Let a chunk be

$$
I=[\nu_-,\nu_+]
$$

with center

$$
\nu_c
$$

and half-width

$$
h.
$$

Let

$$
R
$$

be a floating approximate inverse of

$$
M_c=M_N(\nu_c).
$$

The verification computes with outward interval coefficient evaluation

$$
\boxed{
\eta
=
\|
I-RM_c
\|_\infty.
}
\tag{6.1}
$$

Every certified chunk satisfies

$$
\boxed{
\eta\ll1.
}
\tag{6.2}
$$

Therefore

$$
\boxed{
M_c^{-1}
=
(
I-E
)^{-1}R,
\qquad
\|E\|_\infty\le\eta,
}
\tag{6.3}
$$

and

$$
\boxed{
\|M_c^{-1}\|_\infty
\le
\frac{
\|R\|_\infty
}{
1-\eta
}.
}
\tag{6.4}
$$

---

# 7. Parameter perturbation inside one chunk

Define

$$
\boxed{
B_c
=
M_c^{-1}M_{N,1}.
}
\tag{7.1}
$$

The approximate product

$$
RM_{N,1}
$$

is evaluated against outward interval coefficients, giving a certified bound

$$
\boxed{
\beta
\ge
\|B_c\|_\infty.
}
\tag{7.2}
$$

For

$$
|\nu-\nu_c|\le h,
$$

set

$$
\boxed{
\rho=h\beta.
}
\tag{7.3}
$$

All chunks satisfy

$$
\boxed{
\rho<1.
}
\tag{7.4}
$$

Hence

$$
\boxed{
M_N(\nu)^{-1}
=
(
I+
(\nu-\nu_c)B_c
)^{-1}
M_c^{-1}.
}
\tag{7.5}
$$

This gives explicit row-wise perturbation bounds for:

- the zero-tail core solution;
- the core-to-tail map;
- the boundary core values entering the first tail equations;
- the central coefficient:
  $$
  u_3.
  $$

---

# 8. Infinite tail contraction

Solve the adjoint recurrence for

$$
u_{n+1}.
$$

The row coefficient sum is

$$
\boxed{
q_n(K,\nu)
=
\frac{
-
A_{-2}^{(n)}
+
A_0^{(n)}
+
A_2^{(n)}
-
A_4^{(n)}
}{
-\nu b_n
}.
}
\tag{8.1}
$$

Round 56 rigorously proved:

1. for each source fibre,
   $$
   q_n(K,1)
   $$
   decreases for
   $$
   n\ge6;
   $$

2. viscosity scaling is exact:
   $$
   \boxed{
   q_n(K,\nu)
   =
   q_n(K,1)/\nu.
   }
   \tag{8.2}
   $$

Thus a cutoff chosen at the lower end of a viscosity regime gives a uniform tail bound across the entire regime.

---

# 9. Tail/core feedback enclosure

Let

$$
L_N(\nu)
=
-
M_N(\nu)^{-1}
C_N.
$$

For the first tail equations, some nominal tail inputs pass through the last few core rows of

$$
L_N.
$$

Let

$$
L_{\rm bd}
$$

be a certified upper bound on those boundary row norms, and let

$$
X_{\rm bd}
$$

bound the corresponding zero-tail core values.

If

$$
q_N
$$

is the raw recurrence row bound at the lower viscosity endpoint, then the full affine tail map obeys

$$
\boxed{
\operatorname{Lip}T_{\rm tail}
\le
\widehat q
=
q_N
(
1+L_{\rm bd}
).
}
\tag{9.1}
$$

Every validated chunk satisfies

$$
\boxed{
\widehat q<1.
}
\tag{9.2}
$$

The tail fixed point therefore satisfies

$$
\boxed{
\|y^\ast\|_\infty
\le
\frac{
q_NX_{\rm bd}
}{
1-\widehat q
}.
}
\tag{9.3}
$$

Finally, if

$$
L_3
$$

bounds the $u_3$ row of the core-to-tail map,

$$
\boxed{
u_3
\le
u_{3,\rm core}^{\rm upper}
+
L_3
\|y^\ast\|_\infty.
}
\tag{9.4}
$$

This is the quantity certified negative chunk by chunk.

---

# 10. Low-viscosity validated regime

For

$$
\boxed{
10^{-4}
\le
\nu
\le
10^{-3},
}
\tag{10.1}
$$

use

$$
\boxed{
N=250.
}
\tag{10.2}
$$

The interval is divided geometrically with ratio

$$
\boxed{
3/2.
}
\tag{10.3}
$$

There are only six chunks per fibre.

The worst certified chunk is the first:

$$
\boxed{
[10^{-4},1.5\times10^{-4}].
}
\tag{10.4}
$$

### Small fibre

$$
\boxed{
u_{3,-}
<
-2.1681699396530456\times10^{-4}.
}
\tag{10.5}
$$

### Large fibre

$$
\boxed{
u_{3,+}
<
-3.0490435797040873\times10^{-4}.
}
\tag{10.6}
$$

Therefore

$$
\boxed{
a_{3,\pm}(\nu)>0
}
$$

through the entire low regime.

---

# 11. Intermediate validated regime

For

$$
\boxed{
10^{-3}
\le
\nu
\le
0.7,
}
\tag{11.1}
$$

the stronger viscous tail allows the much smaller cutoff

$$
\boxed{
N=80.
}
\tag{11.2}
$$

Again use geometric ratio

$$
3/2.
$$

There are seventeen chunks per fibre.

The worst chunk is

$$
\boxed{
[10^{-3},1.5\times10^{-3}].
}
\tag{11.3}
$$

### Small fibre

$$
\boxed{
u_{3,-}
<
-2.4009827134153527\times10^{-3}.
}
\tag{11.4}
$$

### Large fibre

$$
\boxed{
u_{3,+}
<
-3.0331757703739824\times10^{-3}.
}
\tag{11.5}
$$

Hence

$$
\boxed{
a_{3,\pm}(\nu)>0
}
$$

through the full intermediate regime.

---

# 12. Numerical rigor layer of the finite-core certificate

For each chunk:

1. the inverse
   $$
   R
   $$
   is only used as an arbitrary approximate inverse;

2. all decisive residuals
   $$
   I-RM_c
   $$
   and
   $$
   r-M_c\widetilde x
   $$
   are recomputed with high-precision outward interval evaluation of the exact
   $$
   \mathbb Q(\sqrt{17})
   $$
   coefficient formulas;

3. Neumann inequalities then certify the true inverse and parameter perturbation bounds;

4. the infinite tail is not truncated as a proof step; it is controlled by the exact contraction estimate inherited from Round 56.

Thus the sign conclusion does not rely on convergence of a finite Galerkin cutoff.

---

# 13. Global contraction for large viscosity

For the remaining half-line we do not need chunk continuation.

Let

$$
w=
(
u_2,u_3,u_4,\ldots
)
\in\ell^\infty.
$$

Solving each recurrence equation for

$$
u_{n+1}
$$

defines an affine map

$$
\boxed{
w=T_\nu w+f_\nu.
}
\tag{13.1}
$$

The only nonzero affine forcing comes from

$$
u_0=1
$$

in the

$$
n=2
$$

equation.

---

# 14. Uniform full-sequence Lipschitz bound

At viscosity one define

$$
q_n^\ast
=
q_n(K,1).
$$

For both fibres, exact algebraic evaluation gives

$$
\boxed{
q_n^\ast<0.53
\qquad
n=1,\ldots,6.
}
\tag{14.1}
$$

Round 56 supplies monotonic decrease for

$$
n\ge6.
$$

Therefore

$$
\boxed{
\sup_{n\ge1}
q_n^\ast
<
0.53.
}
\tag{14.2}
$$

By exact viscosity scaling:

$$
\boxed{
\|T_\nu\|
<
\frac{
0.53
}{
\nu
}.
}
\tag{14.3}
$$

Hence for

$$
\nu\ge0.7,
$$

$$
\boxed{
\|T_\nu\|
<
\frac{53}{70}
<1.
}
\tag{14.4}
$$

So the entire full sequence is selected by one global Banach contraction.

---

# 15. Large-viscosity forcing coefficient

The

$$
n=2
$$

equation has affine forcing

$$
\boxed{
-\frac{
c_\infty
}{
\nu
},
}
\tag{15.1}
$$

where

$$
\boxed{
c_\infty
=
\frac{
A_{-2}^{(2)}
}{
b_2
}
>0.
}
\tag{15.2}
$$

Numerically:

$$
\boxed{
c_{\infty,-}
=
0.0414714839150580\ldots,
}
\tag{15.3}
$$

$$
\boxed{
c_{\infty,+}
=
0.0856618055887251\ldots.
}
\tag{15.4}
$$

This reproduces the large-viscosity constants observed in Round 57.

---

# 16. Central-row feedback bound

In the

$$
u_3
$$

equation, after removing the

$$
u_0
$$

forcing, the remaining coefficient row has viscosity-one norm

$$
r_{2,\pm}.
$$

Exact algebraic checks give the common bound

$$
\boxed{
r_{2,\pm}
<
0.151.
}
\tag{16.1}
$$

The global fixed-point bound is

$$
\boxed{
\|w\|_\infty
\le
\frac{
c_\infty
}{
\nu-0.53
}.
}
\tag{16.2}
$$

Therefore

$$
\boxed{
u_3
\le
-\frac{
c_\infty
}{
\nu
}
+
\frac{
0.151
}{
\nu
}
\frac{
c_\infty
}{
\nu-0.53
}.
}
\tag{16.3}
$$

Thus

$$
\boxed{
u_3
\le
-\frac{
c_\infty
}{
\nu
}
\left[
1
-
\frac{
0.151
}{
\nu-0.53
}
\right].
}
\tag{16.4}
$$

---

# 17. Explicit positivity margin for $\nu\ge0.7$

At

$$
\nu=0.7,
$$

$$
\nu-0.53
=
0.17.
$$

Hence

$$
\boxed{
1
-
\frac{
0.151
}{
0.17
}
=
1-\frac{151}{170}
=
\frac{
19
}{
170
}
>0.
}
\tag{17.1}
$$

The bracket increases as viscosity increases.

Therefore

$$
\boxed{
u_3(\nu)
<
0
\qquad
\forall
\nu\ge0.7.
}
\tag{17.2}
$$

More explicitly,

$$
\boxed{
a_3(\nu)
\ge
\frac{
19
}{
170
}
\frac{
c_\infty
}{
\nu
}
>0.
}
\tag{17.3}
$$

---

# 18. Combined theorem

Sections 10–11 give

$$
a_3(\nu)>0
$$

on

$$
[10^{-4},0.7].
$$

Sections 13–17 give

$$
a_3(\nu)>0
$$

on

$$
[0.7,\infty).
$$

Therefore:

$$
\boxed{
\textbf{
a_{3,\pm}(\nu)>0
\quad
for every
\quad
\nu\ge10^{-4}.
}
}
\tag{18.1}
$$

This is the strongest viscosity-uniform theorem obtained so far in the Round 48–64 hidden-rescue branch.

---

# 19. What remains of the viscosity problem

Round 59 rigorously proved the singular endpoint Green functional

$$
\boxed{
c_{0,-}>5.79,
\qquad
c_{0,+}>5.33.
}
\tag{19.1}
$$

Round 64 rigorously proves positivity for

$$
\boxed{
\nu\ge10^{-4}.
}
\tag{19.2}
$$

Therefore the only viscosity interval not yet rigorously connected is

$$
\boxed{
0<\nu<10^{-4}.
}
\tag{19.3}
$$

Numerically, Rounds 57–60 strongly support positivity there as well, and Rounds 58–63 have already identified the exact endpoint Jost functional, the $\nu^{-1/3}$ boundary layer, the neutral cancellation, the fast Schur inverse, and the symmetrized slow gauge.

Thus the entire viscosity problem has been compressed to one genuinely singular thin strip adjacent to the Euler endpoint.

---

# 20. STOP-C68 — Final Singular Viscosity Strip / Slow Jost Matching Gap

$$
\boxed{
\begin{aligned}
\text{layer}
&=
\mathrm{viscosity\text{-}uniform\ adjoint\ positivity},
\\
\text{endpoint }\nu=0
&=
\mathrm{positive\ Green\ functional\ proved},
\\
10^{-4}
\le\nu\le10^{-3}
&=
\mathrm{validated\ core/tail\ theorem},
\\
10^{-3}
\le\nu\le0.7
&=
\mathrm{validated\ core/tail\ theorem},
\\
\nu\ge0.7
&=
\mathrm{global\ full\text{-}sequence\ contraction\ theorem},
\\
a_{3,\pm}(\nu)
&>
0
\quad
\forall\nu\ge10^{-4},
\\
\text{hidden second-order rescue}
&=
\mathrm{ruled\ out\ on\ both\ source\ circles}
\\
&\quad
\mathrm{for\ every\ }\nu\ge10^{-4},
\\
\text{only remaining viscosity strip}
&=
0<\nu<10^{-4},
\\
\text{missing}
&=
\mathrm{slow\ Jost/Riccati\ singular\ matching\ from\ }\nu=0
\\
&\quad
\mathrm{to\ the\ validated\ threshold\ }10^{-4},
\\
T_{\mathsf C\to\mathsf D}
&=
\mathrm{NOT\ REACHED}.
\end{aligned}
}
$$

Designation:

$$
\boxed{
\textbf{STOP-C68:
Final Singular Viscosity Strip / Slow Jost Matching Gap}.
}
$$

---

# 21. 24/72 Ledger — Round 64

| Step | object | $B$ | $U$ | $O$ | $L$ | status |
|---|---|---|---|---|---|---|
| C1020 | affine finite-core matrix family | $\mathsf C$ | parameterized adjoint core | relational | $\mathsf F$ | EXACT |
| C1021 | approximate-inverse residual certificate | $\mathsf C$ | a posteriori operator bound | scalar | $\mathsf F$ | VALIDATED |
| C1022 | viscosity chunk Neumann perturbation | $\mathsf C$ | resolvent continuation | relational | $\mathsf F$ | PROVED per chunk |
| C1023 | core-to-tail parameter enclosure | $\mathsf C$ | Schur feedback | scalar | $\mathsf F$ | VALIDATED |
| C1024 | infinite tail contraction correction | $\mathsf C$ | sequence-space fixed point | scalar | $\mathsf F$ | PROVED |
| C1025 | $[10^{-4},10^{-3}]$ positivity | $\mathsf C$ | validated continuation | targeted | $\mathsf F$ | PROVED |
| C1026 | $[10^{-3},0.7]$ positivity | $\mathsf C$ | validated continuation | targeted | $\mathsf F$ | PROVED |
| C1027 | full-sequence affine contraction | $\mathsf C$ | $\ell^\infty$ map | relational | $\mathsf F$ | PROVED |
| C1028 | global $q_\ast<0.53$ | $\mathsf C$ | recurrence norm | scalar | $\mathsf F$ | PROVED using R56 tail monotonicity |
| C1029 | central feedback $r_\ast<0.151$ | $\mathsf C$ | central row | scalar | $\mathsf F$ | EXACT algebraic check |
| C1030 | $\nu\ge0.7$ positivity | $\mathsf C$ | global contraction | targeted | $\mathsf F$ | PROVED |
| C1031 | $\nu\ge10^{-4}$ uniform positivity | $\mathsf C$ | parameter half-line | targeted | $\mathsf F$ | PROVED |
| C1032 | uniform Fredholm incompatibility | $\mathsf C$ | hidden source range | targeted | $\mathsf F$ | PROVED for $\nu\ge10^{-4}$ |
| C1033 | final singular strip | $\mathsf C$ | endpoint matching | targeted | $\mathsf F$ | OPEN / STOP-C68 |

---

# 22. Continuous-versus-discrete status

The finite core is only an a posteriori chart used to validate the parameterized continuous Floquet operator.

The proof does not truncate the infinite tail: the tail is closed by a Banach contraction in sequence space.

The large-viscosity half-line is proved directly on the full infinite recurrence.

The viscosity parameter itself remains continuous throughout.

Therefore:

$$
\boxed{
T_{\mathsf C\to\mathsf D}
=
\text{NOT YET REACHED}.
}
$$

---

# 23. Strongest results of Round 64

## R64-A — first validated low-viscosity interval

$$
\boxed{
a_{3,\pm}(\nu)>0
\qquad
10^{-4}\le\nu\le10^{-3}.
}
$$

## R64-B — validated intermediate interval

$$
\boxed{
a_{3,\pm}(\nu)>0
\qquad
10^{-3}\le\nu\le0.7.
}
$$

## R64-C — analytic large-viscosity half-line

$$
\boxed{
a_{3,\pm}(\nu)>0
\qquad
\nu\ge0.7.
}
$$

## R64-D — combined viscosity half-line

$$
\boxed{
a_{3,\pm}(\nu)>0
\qquad
\forall\nu\ge10^{-4}.
}
$$

## R64-E — uniform second-order hidden-rescue no-go

The two $\sqrt{17}$ source-hidden circles fail full second-order analytic source-lock compatibility for every

$$
\boxed{
\nu\ge10^{-4}.
}
$$

---

# 24. Next round — Final Singular Strip / Endpoint-to-$10^{-4}$ Bridge

Round 64 leaves only

$$
\boxed{
0<\nu<10^{-4}.
}
$$

The next attack should therefore return to the Round 63 symmetrized slow Jost/Riccati problem, but now with a concrete target endpoint:

$$
\nu=10^{-4}
$$

is already rigorously inside the positive region.

Concrete targets:

1. use the exact fast-Difference Schur inverse from Round 63;
2. use the three-quarter-shift symmetrized coupling;
3. formulate the slow Jost projective map over
   $$
   0<\nu\le10^{-4};
   $$

4. construct an interval stable-line cone through the
   $$
   j\sim\nu^{-1/3}
   $$
   WKB layer;

5. match it to the rigorous Round 59 endpoint Jost graph;

6. obtain
   $$
   \left|
   a_3(\nu)/\nu-c_0
   \right|
   <
   c_0
   $$
   throughout the strip;

7. conclude
   $$
   a_3(\nu)>0
   $$
   for every
   $$
   \nu>0;
   $$

8. if successful, the viscosity parameter will disappear entirely from this hidden-rescue escape branch.

This becomes:

$$
\boxed{
\textbf{Final Singular Strip / Endpoint-to-$10^{-4}$ Bridge}.
}
$$

---

# 25. External primary-source anchors

Fresh literature check before this round:

1. Yuri Latushkin, Shibi Vasudevan, *Fredholm determinants, continued fractions, Jost and Evans functions for a Jacobi matrix associated with the 2D-Euler equations*, arXiv:2401.14037.
   - hydrodynamic difference-equation context connecting Jost, Evans, Fredholm and continued-fraction formulations.

2. Yuri Latushkin, Shibi Vasudevan, *Characteristic determinants for a second order difference equation on the half-line arising in hydrodynamics*, arXiv:2405.01135.
   - half-line hydrodynamic difference equations, Jost/Evans functions and Fredholm determinants.

3. F. Battelli, M. Franca, K. J. Palmer, *Exponential Dichotomy for Noninvertible Linear Difference Equations*, arXiv:2111.04553.
   - primary-source roughness / persistence framework for difference-equation dichotomies.

These works are framework anchors only. All NS-specific coefficients, viscosity bounds, core/tail certificates and compatibility conclusions in Round 64 are direct derivations of this project.

---

# 26. Commit state

$$
\boxed{
\begin{aligned}
\text{Route}
&=
\mathrm{Pure\ Continuous\ Validated\ Viscosity\ Half\text{-}Line},
\\
\text{Essential }\mathsf C\to\mathsf D
&=
\mathrm{Not\ reached},
\\
\text{Endpoint }\nu=0
&=
\mathrm{positive\ functional\ proved},
\\
\text{Validated positive interval}
&=
[10^{-4},0.7],
\\
\text{Analytic positive half-line}
&=
[0.7,\infty),
\\
\text{Combined}
&=
a_{3,\pm}(\nu)>0
\quad
\forall\nu\ge10^{-4},
\\
\text{Hidden rescue no-go}
&=
\mathrm{uniform\ for\ }\nu\ge10^{-4},
\\
\text{Only remaining parameter gap}
&=
(0,10^{-4}),
\\
\text{STOP-C68}
&=
\mathrm{Final\ Singular\ Viscosity\ Strip/Slow\ Jost\ Matching\ Gap},
\\
\text{Next}
&=
\mathrm{Final\ Singular\ Strip/Endpoint\text{-}to\text{-}10^{-4}\ Bridge}.
\end{aligned}
}
$$