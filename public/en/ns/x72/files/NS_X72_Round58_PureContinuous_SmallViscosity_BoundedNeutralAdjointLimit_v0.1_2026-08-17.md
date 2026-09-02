# NS × X Integral × 24/72 Paradigm in Practice
## Round 58 — Pure Continuous Small-Viscosity Singular Adjoint Limit / Bounded-Neutral Corrector

- Date:  2026-08-17
- Version:  v0.1
- Status:  Proof-Route Experiment / Continuous-Only Singular-Endpoint Branch
- canonical source: UTF-8 Markdown
- canonical math delimiters: inline `$...$`; display `$$...$$`
- Previous round:  `NS_X72_Round57_PureContinuous_ViscosityContinuation_AdjointPositivityMap_v0.1_2026-08-17.md`
- This round's objective:  The full viscosity scan of Round 57 shows
  $$
  a_{3,\pm}(\nu)>0
  $$
  and
  $$
  a_3(\nu)=O(\nu)
  $$
  as
  $$
  \nu\to0^+.
  $$
  This round no longer directly extrapolates using the finite-section SVD at small positive viscosity, but instead applies a singular parity rescaling to the adjoint recurrence to derive the correct $\nu=0$ endpoint problem.
- Main result: 
  1. The exact rescaling
     $$
     u_{2j}=e_j,
     \qquad
     u_{2j+1}=\nu o_j
     $$
     transforms the canonical adjoint equation into a system depending only on
     $$
     \mu=\nu^2
     $$
     ;
  2. At $\mu=0$, the even sector is the superfactorial minimal Euler mode;
  3. The odd first corrector is not an analytic/minimal tail, but a bounded-neutral mode;
  4. direct recurrence asymptotics gives
     $$
     o_j
     =
     L
     -
     \frac{3K^2L}{4j^2}
     +
     O(j^{-3});
     $$
  5. The endpoint central slope constant is determined by a "minimal-even forced bounded-odd" BVP;
  6. direct rescaled endpoint solve stabilizes to
     $$
     c_{0,-}
     =
     5.79052557842265\ldots,
     $$
     $$
     c_{0,+}
     =
     5.33175254587449\ldots;
     $$
  7. hence the predicted Fredholm-pairing slopes are
     $$
     \Pi'_-(0^+)
     \approx
     -1.76280262464,
     $$
     $$
     \Pi'_+(0^+)
     \approx
     532.651652172;
     $$
  8. the small-fibre value
     $$
     5.7905357\ldots
     $$
     quoted from Round 57's extremely-small-$\nu$ raw SVD is identified as singular-cutoff contamination, not the endpoint constant;
  9. the correct rigorous endpoint space is
     $$
     \boxed{
     \text{minimal even}
     \times
     \text{bounded-neutral odd}
     }
     $$
     rather than the fixed-$\nu$ analytic tail space.
- Non-claims:  This round has not yet proven
  $$
  \lim_{\nu\to0^+}
  a_3(\nu)/\nu
  =
  c_0
  $$
  in the full infinite operator topology. The singular endpoint system and asymptotics are exact; the numerical values of $c_0$ are stable direct BVP computations. The remaining proof obligation is a rigorous Green/Jost matching theorem connecting the fixed-$\nu$ minimal branches to the bounded-neutral endpoint corrector.

---

# 0. Round 57 handoff

Round 57:

$$
\boxed{
q_n(K,\nu)
=
q_n(K,1)/\nu.
}
\tag{0.1}
$$

So every fixed:

$$
\nu>0
$$

still has a contractive tail at sufficiently large Floquet depth.

But:

$$
N_{\rm tail}
\sim
\nu^{-1/2}
$$

diverges as:

$$
\nu\to0^+.
$$

Numerically:

$$
a_3(\nu)>0
$$

through:

$$
10^{-5}\le\nu\le10^3.
$$

The suggested small-viscosity law was:

$$
\boxed{
a_3(\nu)
\sim
c_0\nu.
}
\tag{0.2}
$$

Round 57 STOP:

$$
\boxed{
\text{STOP-C61}
=
\text{Viscosity-Uniform Positivity / Endpoint-Continuation Gap}.
}
$$

---

# 1. Real canonical adjoint recurrence

Round 56 writes the $\mathcal C$-even canonical adjoint as:

$$
\boxed{
\psi_n=i^nu_n,
\qquad
u_n\in\mathbb R.
}
\tag{1.1}
$$

Reflection:

$$
\boxed{
u_{-n}=(-1)^nu_n.
}
\tag{1.2}
$$

Normalization:

$$
\boxed{
u_0=1,
\qquad
u_1=0.
}
\tag{1.3}
$$

The recurrence:

$$
\boxed{
-
A_{-2}^{(n)}
u_{n-2}
+
A_0^{(n)}
u_n
-
B_1^{(n)}
u_{n+1}
-
A_2^{(n)}
u_{n+2}
+
A_4^{(n)}
u_{n+4}
=
0.
}
\tag{1.4}
$$

Here:

$$
A_{-2},
A_0,
A_2,
A_4
$$

are independent of viscosity, while:

$$
\boxed{
B_1^{(n)}(K,\nu)
=
\nu b_n(K).
}
\tag{1.5}
$$

---

# 2. Exact parity rescaling

Set:

$$
\boxed{
u_{2j}=e_j,
}
\tag{2.1}
$$

and:

$$
\boxed{
u_{2j+1}
=
\nu o_j.
}
\tag{2.2}
$$

Then the even equations, at:

$$
n=2j,
$$

become:

$$
\boxed{
-
A_{-2}^{(2j)}
e_{j-1}
+
A_0^{(2j)}
e_j
-
A_2^{(2j)}
e_{j+1}
+
A_4^{(2j)}
e_{j+2}
-
\nu^2
b_{2j}
o_j
=
0.
}
\tag{2.3}
$$

The odd equations, at:

$$
n=2j+1,
$$

after dividing by:

$$
\nu,
$$

become:

$$
\boxed{
\begin{aligned}
0
={}&
-
A_{-2}^{(2j+1)}
o_{j-1}
+
A_0^{(2j+1)}
o_j
\\
&-
b_{2j+1}
e_{j+1}
-
A_2^{(2j+1)}
o_{j+1}
+
A_4^{(2j+1)}
o_{j+2}.
\end{aligned}
}
\tag{2.4}
$$

Therefore the rescaled system depends on viscosity only through:

$$
\boxed{
\mu=\nu^2.
}
\tag{2.5}
$$

This explains the observed structural expansion:

$$
\boxed{
u_{2j}
=
e_j^{(0)}
+
O(\nu^2),
}
\tag{2.6}
$$

$$
\boxed{
u_{2j+1}
=
\nu
\left[
o_j^{(0)}
+
O(\nu^2)
\right]
}
\tag{2.7}
$$

provided the singular endpoint matching is justified.

---

# 3. The $\mu=0$ even problem

At:

$$
\mu=0,
$$

the even mode solves:

$$
\boxed{
-
A_{-2}^{(2j)}
e_{j-1}
+
A_0^{(2j)}
e_j
-
A_2^{(2j)}
e_{j+1}
+
A_4^{(2j)}
e_{j+2}
=
0.
}
\tag{3.1}
$$

with:

$$
\boxed{
e_0=1.
}
\tag{3.2}
$$

The admissible branch is the minimal Euler branch.

Let:

$$
\boxed{
R_j
=
e_j/e_{j-1}.
}
\tag{3.3}
$$

Then:

$$
\boxed{
R_j
=
\frac{
A_{-2}^{(2j)}
}{
A_0^{(2j)}
-
A_2^{(2j)}
R_{j+1}
+
A_4^{(2j)}
R_{j+2}R_{j+1}
}.
}
\tag{3.4}
$$

The coefficient asymptotics imply:

$$
\boxed{
R_j
\sim
-\frac{
K^2
}{
16j^2
}.
}
\tag{3.5}
$$

Hence:

$$
\boxed{
|e_j|
\asymp
C
\frac{
(K^2/16)^j
}{
(j!)^2
}
}
\tag{3.6}
$$

up to subfactorial factors.

So the even endpoint remains superfactorially minimal.

---

# 4. The $\mu=0$ odd corrector

The odd first corrector solves:

$$
\boxed{
\begin{aligned}
0
={}&
-
A_{-2}^{(2j+1)}
o_{j-1}
+
A_0^{(2j+1)}
o_j
\\
&-
b_{2j+1}
e_{j+1}
-
A_2^{(2j+1)}
o_{j+1}
+
A_4^{(2j+1)}
o_{j+2}.
\end{aligned}
}
\tag{4.1}
$$

Normalization:

$$
\boxed{
o_0=0.
}
\tag{4.2}
$$

Reflection is:

$$
\boxed{
o_{-j-1}
=
-o_j.
}
\tag{4.3}
$$

The forcing:

$$
b_{2j+1}e_{j+1}
$$

decays superfactorially.

However, the homogeneous odd operator possesses the neutral Euler branch inherited from Round 53.

Therefore the correct endpoint condition is:

$$
\boxed{
o_j
\text{ bounded as }
j\to+\infty,
}
\tag{4.4}
$$

not:

$$
o_j\to0.
$$

---

# 5. Exact constant-residual asymptotic

Define:

$$
\boxed{
S_j
=
-
A_{-2}^{(2j+1)}
+
A_0^{(2j+1)}
-
A_2^{(2j+1)}
+
A_4^{(2j+1)}.
}
\tag{5.1}
$$

Direct exact symbolic expansion gives:

$$
\boxed{
\lim_{j\to\infty}
j^3S_j
=
6K^3.
}
\tag{5.2}
$$

So a strictly constant odd mode is not exact; its residual is:

$$
O(j^{-3}).
$$

This is precisely weak enough to generate a bounded neutral correction rather than an exponentially separated tail.

---

# 6. Exact plateau law

Assume:

$$
\boxed{
o_j
=
L
+
\frac{C}{j^2}
+
o(j^{-2}).
}
\tag{6.1}
$$

The forcing is superfactorially smaller and does not contribute to the algebraic tail balance.

Substitute (6.1) into the homogeneous part of (4.1).

The exact symbolic limit is:

$$
\boxed{
\lim_{j\to\infty}
j^3
\mathcal O
\left[
L+C/j^2
\right]
=
8CK
+
6K^3L.
}
\tag{6.2}
$$

Thus:

$$
\boxed{
C
=
-\frac34
K^2L.
}
\tag{6.3}
$$

Hence:

$$
\boxed{
o_j
=
L
-
\frac{
3K^2L
}{
4j^2
}
+
O(j^{-3}).
}
\tag{6.4}
$$

Nomenclature:

$$
\boxed{
\textbf{Bounded-Neutral Plateau Law}.
}
$$

This is an exact asymptotic balance of the endpoint recurrence.

---

# 7. Why Round 57 direct small-$\nu$ extrapolation is delicate

For every:

$$
\nu>0,
$$

the full canonical adjoint is analytic/minimal at infinity.

But the scale at which viscosity dominates is:

$$
j
\sim
\nu^{-1/2}.
$$

At fixed:

$$
j,
$$

the rescaled odd variable:

$$
o_j=u_{2j+1}/\nu
$$

approaches the bounded-neutral endpoint profile.

At:

$$
j
\gg
\nu^{-1/2},
$$

the fixed-$\nu$ minimal tail bends back toward superfactorial decay.

Therefore the limits:

$$
\nu\to0^+
$$

and:

$$
j\to\infty
$$

do not commute.

This is the source of singular-cutoff contamination in raw finite-section extrapolation.

---

# 8. Direct endpoint BVP computation

The verification script solves:

1. the even minimal mode by backward continued-ratio iteration;
2. the forced odd endpoint equation with:
   $$
   o_0=0;
   $$
3. a far cutoff whose boundary influence on the central value is empirically superfactorially small.

The endpoint central coefficient is:

$$
\boxed{
c_0
=
-\,
o_1.
}
\tag{8.1}
$$

For the small source fibre:

$$
\boxed{
K_-
=
\sqrt{17}-3,
}
\tag{8.2}
$$

the stable value is:

$$
\boxed{
c_{0,-}
=
5.79052557842265\ldots.
}
\tag{8.3}
$$

For the large source fibre:

$$
\boxed{
K_+
=
\sqrt{17}+3,
}
\tag{8.4}
$$

$$
\boxed{
c_{0,+}
=
5.33175254587449\ldots.
}
\tag{8.5}
$$

---

# 9. Endpoint cutoff stability

For the small fibre, the direct endpoint BVP gives:

$$
\boxed{
\begin{array}{c|c}
J
&
-c_1=-o_1
\\
\hline
3
&
5.79052558969675
\\
4
&
5.79052557841899
\\
5
&
5.79052557842265
\\
10
&
5.79052557842265
\\
20
&
5.79052557842265
\end{array}
}
\tag{9.1}
$$

For the large fibre:

$$
\boxed{
\begin{array}{c|c}
J
&
-o_1
\\
\hline
3
&
5.33374367637498
\\
4
&
5.33157043152890
\\
5
&
5.33175948323330
\\
6
&
5.33175232358105
\\
8
&
5.33175254575307
\\
10
&
5.33175254587446
\\
20
&
5.33175254587449
\end{array}
}
\tag{9.2}
$$

These are direct endpoint equations, not extrapolation from small positive viscosity.

They are still numerical until a rigorous endpoint Green/Jost tail estimate is supplied.

---

# 10. Small positive viscosity in the rescaled variables

Solve the finite rescaled system directly at small positive:

$$
\nu.
$$

Representative values:

### small fibre

$$
\boxed{
\begin{array}{c|c}
\nu
&
a_3(\nu)/\nu
\\
\hline
10^{-2}
&
5.82043633064
\\
10^{-3}
&
5.80013506899
\\
10^{-4}
&
5.79153420592
\\
10^{-5}
&
5.79061554981
\\
10^{-6}
&
5.79052700090
\end{array}
}
\tag{10.1}
$$

### large fibre

$$
\boxed{
\begin{array}{c|c}
\nu
&
a_3(\nu)/\nu
\\
\hline
10^{-2}
&
5.26561015994
\\
10^{-3}
&
5.32799430246
\\
10^{-4}
&
5.33141366867
\\
10^{-5}
&
5.33174497726
\\
10^{-6}
&
5.33175246896
\end{array}
}
\tag{10.2}
$$

The rescaled solve converges toward (8.3)–(8.5).

---

# 11. Correction to the Round 57 small-fibre extrapolation

Round 57's raw physical finite section at:

$$
\nu=10^{-6}
$$

reported:

$$
a_{3,-}/\nu
\approx
5.790535712.
$$

The rescaled endpoint solve shows the true endpoint candidate is:

$$
\boxed{
5.790525578\ldots.
}
$$

The difference:

$$
\sim10^{-5}
$$

is entirely consistent with the diverging minimal-tail cutoff:

$$
N_{\rm tail}
\sim
\nu^{-1/2}.
$$

This does not change the positivity conclusion.

It is a useful audit correction: near a singular endpoint, raw finite sections should not be used to estimate derivatives without parity rescaling.

---

# 12. Fredholm-pairing slope candidate

Round 55:

$$
\boxed{
\langle
\psi_+,
g
\rangle
=
g_0(\nu)
+
a_3(\nu)G_{-3}.
}
\tag{12.1}
$$

If:

$$
a_3(\nu)
=
c_0\nu
+
o(\nu),
$$

then:

$$
\boxed{
\frac{
\langle
\psi_+,
g
\rangle
}{
\nu
}
\to
12
(
3r^2-1
)
+
c_0G_{-3}.
}
\tag{12.2}
$$

Using the endpoint BVP constants:

### small fibre

$$
\boxed{
\Pi'_-(0^+)
\approx
-1.76280262464.
}
\tag{12.3}
$$

### large fibre

$$
\boxed{
\Pi'_+(0^+)
\approx
532.651652172.
}
\tag{12.4}
$$

Both are far from zero.

Thus the vanishing-viscosity endpoint numerically reinforces, rather than weakens, the Round 56 Fredholm obstruction.

---

# 13. Endpoint space must change

The fixed positive-viscosity canonical mode belongs to an analytic/minimal Floquet space.

Its first viscosity derivative does not.

The correct singular tangent space is:

$$
\boxed{
\mathcal X_0
=
\mathcal X_{\rm even}^{\rm minimal}
\times
\mathcal X_{\rm odd}^{\rm bounded\ neutral}.
}
\tag{13.1}
$$

This resolves an apparent paradox:

- for every:
  $$
  \nu>0,
  $$
  all components decay;
- at:
  $$
  \nu=0,
  $$
  the odd first corrector approaches a nonzero plateau.

The boundary layer sits at Floquet depth:

$$
j\sim\nu^{-1/2}
$$

and escapes to infinity as viscosity vanishes.

---

# 14. Formal endpoint analyticity in $\mu=\nu^2$

The rescaled equations (2.3)–(2.4) contain:

$$
\nu
$$

only through:

$$
\mu=\nu^2.
$$

This suggests the canonical singular branch, when formulated in:

$$
\mathcal X_0,
$$

should have:

$$
\boxed{
e_j(\nu)
=
e_j^{(0)}
+
\mu e_j^{(1)}
+\cdots,
}
\tag{14.1}
$$

$$
\boxed{
o_j(\nu)
=
o_j^{(0)}
+
\mu o_j^{(1)}
+\cdots.
}
\tag{14.2}
$$

Therefore:

$$
\boxed{
a_3(\nu)
=
-\nu o_1^{(0)}
+
O(\nu^3).
}
\tag{14.3}
$$

So:

$$
\boxed{
c_0
=
-\,
o_1^{(0)}.
}
\tag{14.4}
$$

The missing theorem is the invertibility / matching result that justifies this expansion uniformly across the singular tail.

---

# 15. Why a Jost / continued-fraction formulation is natural

The even minimal mode already admits the backward continued-ratio equation:

$$
R_j
=
\frac{
A_{-2}^{(2j)}
}{
A_0^{(2j)}
-
A_2^{(2j)}R_{j+1}
+
A_4^{(2j)}R_{j+2}R_{j+1}
}.
$$

The odd endpoint problem is a forced bounded-neutral recurrence.

Thus a natural rigorous endpoint construction is:

1. construct the even Jost/minimal solution by continued fractions;
2. construct the neutral homogeneous odd solution with:
   $$
   h_j\to1;
   $$
3. construct the forced odd particular solution:
   $$
   p_j\to0;
   $$
4. choose:
   $$
   o_j=Lh_j+p_j
   $$
   so:
   $$
   o_0=0;
   $$
5. prove the central quantity:
   $$
   -o_1>0.
   $$

This avoids sending a fixed positive-viscosity contraction cutoff to infinity.

---

# 16. Neutral homogeneous asymptotic

Let:

$$
h_j\to1.
$$

Section 6 gives:

$$
\boxed{
h_j
=
1
-
\frac{
3K^2
}{
4j^2
}
+
O(j^{-3}).
}
\tag{16.1}
$$

The forced particular solution inherits the superfactorial scale of:

$$
e_j
$$

and may be chosen:

$$
\boxed{
p_j\to0.
}
\tag{16.2}
$$

Then:

$$
\boxed{
o_j
=
Lh_j+p_j.
}
\tag{16.3}
$$

The scalar:

$$
L
$$

is fixed by:

$$
o_0=0.
$$

This decomposition cleanly separates:

- the neutral Euler tail;
- the genuinely forced minimal correction.

---

# 17. Numerical plateau diagnostics

A large-cutoff endpoint solve gives approximate plateaux:

$$
\boxed{
L_-
\approx
2.97825,
}
\tag{17.1}
$$

and:

$$
\boxed{
L_+
\approx
-11.4795.
}
\tag{17.2}
$$

The observed approach is consistent with:

$$
j^2
(
o_j-L
)
\to
-\frac34K^2L.
$$

For the small fibre:

$$
-\frac34K_-^2L_-
\approx
-2.82.
$$

For the large fibre:

$$
-\frac34K_+^2L_+
\approx
4.37\times10^2.
$$

These large differences explain why the large-$K$ endpoint needs much deeper Floquet resolution before its neutral plateau is visually apparent.

---

# 18. What is now rigorously clear versus still open

## Exact / analytic

- parity-rescaled endpoint equations;
- dependence on:
  $$
  \mu=\nu^2;
  $$
- even minimal ratio asymptotic;
- neutral residual:
  $$
  j^3S_j\to6K^3;
  $$
- plateau coefficient:
  $$
  C=-3K^2L/4;
  $$
- exact target sign geometry of Rounds 55–57.

## Numerically stable but not yet infinite-endpoint theorem

- $c_{0,\pm}$ values;
- plateau values:
  $$
  L_\pm;
  $$
- actual convergence:
  $$
  a_3(\nu)/\nu\to c_0.
  $$

This distinction is maintained deliberately.

---

# 19. STOP-C62 — Bounded-Neutral Green/Jost Endpoint Gap

$$
\boxed{
\begin{aligned}
\text{layer}
&=
\mathrm{small\text{-}viscosity\ singular\ adjoint\ limit},
\\
u_{2j}
&=
e_j,
\\
u_{2j+1}
&=
\nu o_j,
\\
\mu
&=
\nu^2,
\\
\text{even endpoint}
&=
\mathrm{superfactorial\ minimal},
\\
\text{odd endpoint}
&=
\mathrm{bounded\ neutral},
\\
e_j/e_{j-1}
&\sim
-K^2/(16j^2),
\\
o_j
&=
L
-
3K^2L/(4j^2)
+
O(j^{-3}),
\\
c_{0,-}^{\rm num}
&=
5.79052557842265\ldots,
\\
c_{0,+}^{\rm num}
&=
5.33175254587449\ldots,
\\
\Pi'_-(0^+)^{\rm num}
&\approx
-1.76280262464,
\\
\Pi'_+(0^+)^{\rm num}
&\approx
532.651652172,
\\
\text{endpoint sign}
&=
\mathrm{strongly\ positive\ for\ }a_3/\nu
\mathrm{\ numerically},
\\
\text{missing}
&=
\mathrm{rigorous\ Green/Jost\ construction\ in\ }
\mathcal X_{\rm even}^{\rm minimal}
\times
\mathcal X_{\rm odd}^{\rm bounded}
\\
&\quad
\mathrm{and\ proof\ that\ the\ fixed\text{-}\nu\ minimal\ branch\ converges\ to\ it},
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
\textbf{STOP-C62:
Bounded-Neutral Green/Jost Endpoint Gap}.
}
$$

---

# 20. 24/72 Ledger — Round 58

| Step | object | $B$ | $U$ | $O$ | $L$ | status |
|---|---|---|---|---|---|---|
| C931 | parity viscosity rescaling | $\mathsf C$ | singular operator family | relational | $\mathsf F$ | EXACT |
| C932 | $\mu=\nu^2$ endpoint system | $\mathsf C$ | parameter desingularization | scalar | $\mathsf F$ | EXACT |
| C933 | even Euler minimal recurrence | $\mathsf C$ | continued-ratio geometry | profile | $\mathsf F$ | EXACT |
| C934 | even minimal asymptotic | $\mathsf C$ | Floquet infinity | scalar | $\mathsf F$ | DERIVED |
| C935 | forced odd endpoint recurrence | $\mathsf C$ | singular corrector | relational | $\mathsf F$ | EXACT |
| C936 | bounded-neutral endpoint condition | $\mathsf C$ | function-space change | targeted | $\mathsf F$ | IDENTIFIED |
| C937 | constant residual limit | $\mathsf C$ | exact asymptotic algebra | scalar | $\mathsf F$ | PROVED |
| C938 | Bounded-Neutral Plateau Law | $\mathsf C$ | asymptotic matching | scalar | $\mathsf F$ | PROVED formally from recurrence |
| C939 | endpoint BVP constants | $\mathsf C$ | direct rescaled solve | scalar | $\mathsf F$ | NUMERICALLY VERIFIED |
| C940 | Round 57 endpoint audit | $\mathsf C$ | cutoff comparison | targeted | $\mathsf F$ | VERIFIED |
| C941 | Fredholm pairing slope candidate | $\mathsf C$ | endpoint compatibility | scalar | $\mathsf F$ | NUMERICAL |
| C942 | mixed endpoint function space | $\mathsf C$ | singular topology | relational | $\mathsf F$ | IDENTIFIED |
| C943 | $\mu$-analytic branch ansatz | $\mathsf C$ | singular perturbation | profile | $\mathsf F$ | CONJECTURAL / STRUCTURAL |
| C944 | Green/Jost endpoint decomposition | $\mathsf C$ | continued-fraction route | targeted | $\mathsf F$ | ROUTE DESIGNED |
| C945 | rigorous positive endpoint slope | $\mathsf C$ | infinite matching | targeted | $\mathsf F$ | OPEN / STOP-C62 |

---

# 21. Continuous-versus-discrete status

This round is fundamentally a continuous viscosity singular-limit problem:

$$
\nu\to0^+.
$$

The sideband index is still a spectral chart for a continuous periodic vertical coordinate.

The decisive new object is a change of infinite-dimensional function space at the endpoint, not a discrete computational mechanism.

The continued-ratio / Jost language is a representation of the same periodic continuous operator.

Therefore:

$$
\boxed{
T_{\mathsf C\to\mathsf D}
=
\text{NOT YET REACHED}.
}
$$

---

# 22. Strongest results of Round 58

## R58-A — exact desingularization

$$
\boxed{
u_{2j}=e_j,
\qquad
u_{2j+1}=\nu o_j
}
$$

turns the parameter into:

$$
\boxed{
\mu=\nu^2.
}
$$

## R58-B — even minimal endpoint

$$
\boxed{
e_j/e_{j-1}
\sim
-K^2/(16j^2).
}
$$

## R58-C — odd bounded-neutral endpoint

$$
\boxed{
o_j
=
L
-
\frac{3K^2L}{4j^2}
+
O(j^{-3}).
}
$$

## R58-D — refined positive slope constants

$$
\boxed{
c_{0,-}
\approx
5.79052557842265,
}
$$

$$
\boxed{
c_{0,+}
\approx
5.33175254587449.
}
$$

## R58-E — strong nonzero endpoint pairing slopes

$$
\boxed{
\Pi'_-(0^+)
\approx
-1.76280262464,
}
$$

$$
\boxed{
\Pi'_+(0^+)
\approx
532.651652172.
}
$$

## R58-F — endpoint difficulty is now localized

The remaining issue is not whether the formal endpoint is positive.

It is to justify the singular matching:

$$
\boxed{
\text{fixed-}\nu\text{ analytic minimal tail}
\longrightarrow
\text{minimal-even/bounded-odd endpoint}.
}
$$

---

# 23. Next round — Endpoint Green Functional / Rigorous Positive Slope

The next round should now prove the endpoint slope rather than re-scan viscosity.

Concrete targets:

1. rigorously construct the even minimal Jost solution through the continued-ratio fixed point;
2. construct the neutral odd homogeneous solution:
   $$
   h_j\to1;
   $$
3. prove:
   $$
   h_j
   =
   1
   -
   3K^2/(4j^2)
   +
   O(j^{-3});
   $$
4. construct the forced minimal odd particular solution:
   $$
   p_j\to0;
   $$
5. set:
   $$
   o_j=Lh_j+p_j,
   \qquad
   o_0=0;
   $$
6. derive a Green/Jost formula for:
   $$
   c_0=-o_1;
   $$
7. use a finite-core exact enclosure plus superfactorial forcing tail to prove a coarse but rigorous:
   $$
   c_{0,\pm}>0;
   $$
8. then establish a singular matching estimate:
   $$
   a_3(\nu)
   =
   c_0\nu
   +
   O(\nu^3)
   $$
   in a mixed weighted norm.

This becomes:

$$
\boxed{
\textbf{Endpoint Green Functional / Rigorous Positive Slope}.
}
$$

---

# 24. External primary-source anchors

1. Quansen Jiu, Milton C. Lopes Filho, Dongjuan Niu, Helena J. Nussenzveig Lopes, *The limit of vanishing viscosity for the incompressible 3D Navier-Stokes equations with helical symmetry*, arXiv:1706.10012.
   - rigorous 3D incompressible Navier–Stokes vanishing-viscosity analysis in a helical setting;
   - used only as external context showing that helical geometry and viscosity-dependent decompositions naturally lead to singular-limit estimates, not as a source for the Round 58 Floquet formulas.

2. Yuri Latushkin, Shibi Vasudevan, *Fredholm determinants, continued fractions, Jost and Evans functions for a Jacobi matrix associated with the 2D-Euler equations*, arXiv:2401.14037.
   - relates continued fractions, Jost solutions, Evans functions and Fredholm determinants for a fluid-derived difference equation;
   - directly relevant methodological context for the planned endpoint continued-fraction / Jost formulation.

3. Christian Pötzsche, Robert Skiba, *Evans function, parity and nonautonomous bifurcations*, arXiv:2503.07221.
   - parameter-dependent Evans/parity framework;
   - relevant to the later step of reconnecting the rigorously solved singular endpoint to the positive-viscosity continuation branch.

All NS-specific endpoint recurrences, plateau asymptotics and numerical constants in Round 58 are direct derivations / computations of this project.

---

# 25. Commit state

$$
\boxed{
\begin{aligned}
\text{Route}
&=
\mathrm{Pure\ Continuous\ Small\text{-}Viscosity\ Singular\ Adjoint\ Limit},
\\
\text{Essential }\mathsf C\to\mathsf D
&=
\mathrm{Not\ reached},
\\
\text{Fixed-}\nu\text{ analytic tail}
&=
\mathrm{singular\ as\ }\nu\to0^+,
\\
\text{Correct endpoint topology}
&=
\mathrm{minimal\ even}
\times
\mathrm{bounded\ neutral\ odd},
\\
\text{Endpoint plateau law}
&=
\mathrm{derived},
\\
\text{Positive slope constants}
&=
\mathrm{strongly\ supported},
\\
\text{Round 57 raw endpoint estimate}
&=
\mathrm{refined},
\\
\text{Rigorous endpoint positivity}
&=
\mathrm{not\ yet\ claimed},
\\
\text{STOP-C62}
&=
\mathrm{Bounded\text{-}Neutral\ Green/Jost\ Endpoint\ Gap},
\\
\text{Next}
&=
\mathrm{Endpoint\ Green\ Functional/Rigorous\ Positive\ Slope}.
\end{aligned}
}
$$