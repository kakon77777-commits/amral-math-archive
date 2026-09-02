# NS × X Integral × 24/72 Paradigm Practice
## Round 57 — Pure Continuous Viscosity Continuation / Adjoint Positivity Bifurcation Map

- Date: 2026-08-17
- Version: v0.1
- Status: Proof-Route Experiment / Continuous-Only Parameter-Continuation Branch
- Canonical source: UTF-8 Markdown
- Canonical math delimiters: inline `$...$`; display `$$...$$`
- Previous round: `NS_X72_Round56_PureContinuous_RigorousAdjointTail_PositiveCentralCoefficient_v0.1_2026-08-17.md`
- Objective of this round: Round 56 has strictly closed the full second-order analytic rescue of the two $\sqrt{17}$ source-hidden circles on the normalized
  $$
  \nu=1
  $$
  slice. This round restores the viscosity / Reynolds-like ratio as a continuous parameter and investigates whether the canonical adjoint coefficient
  $$
  a_3(\nu)
  =
  \operatorname{Im}\psi_+(3;\nu)
  $$
  could cross zero.
- Main results:
  1. The tail contraction coefficient possesses the exact factorization
     $$
     q_n(K,\nu)
     =
     \frac{q_n(K,1)}{\nu};
     $$
  2. For large $n$,
     $$
     q_n(K,\nu)
     \sim
     \frac{K}{2\nu n^2};
     $$
     therefore, for any fixed $\nu>0$, the rigorous contraction cutoff can be moved to a sufficiently high Floquet depth;
  3. Thus, the only places where parameter continuation could genuinely fail are not at tail infinity, but at the finite-core / global minimal matching or the
     $$
     a_3(\nu)=0
     $$
     bifurcation;
  4. In a logarithmic scan of raw physical finite sections over
     $$
     10^{-5}\le\nu\le10^3,
     $$
     both source fibres strictly yield
     $$
     a_3(\nu)>0;
     $$
  5. $a_3$ is not a monotonic function: it rises from a small positive value as $\nu\to0^+$ to a broad positive peak, and then decays with a positive $1/\nu$ tail;
  6. Endpoint diagnostics stably support
     $$
     a_3(\nu)
     \sim
     c_0\nu
     \qquad
     (\nu\to0^+),
     $$
     and
     $$
     a_3(\nu)
     \sim
     c_\infty/\nu
     \qquad
     (\nu\to\infty),
     $$
     with all four coefficients being positive;
  7. Because the Round 55 exact target sign geometry maintains
     $$
     \operatorname{sign}g_0
     =
     \operatorname{sign}G_{-3},
     $$
     for all $\nu>0$, if it can be proven that
     $$
     a_3(\nu)>0
     \quad
     \forall\nu>0,
     $$
     then the local second-order no-go of Round 56 can be upgraded to a viscosity-uniform theorem.
- Non-claims: The all-parameter positivity in this round remains a **continuation theorem candidate**, not a proven all-$\nu$ theorem. The rigorous parts are the tail contraction scaling and the "movable cutoff for any fixed $\nu>0$"; the absence of zeros over the entire interval is currently supported by a high-resolution physical finite-section map. The next round should perform interval / validated continuation, rather than treating the scan as a proof.

---

# 0. Round 56 handoff

The two source fibres are:

$$
\boxed{
K_-
=
\sqrt{17}-3,
}
\tag{0.1}
$$

and:

$$
\boxed{
K_+
=
\sqrt{17}+3.
}
\tag{0.2}
$$

Round 56 constructed, at:

$$
\nu=1,
$$

the unique bounded reflection-even, $\mathcal C$-even canonical adjoint:

$$
\boxed{
\psi_+(0)=1,
\qquad
\psi_+(1)=0.
}
\tag{0.3}
$$

with:

$$
\boxed{
a_3(1)
=
\operatorname{Im}\psi_+(3)>0.
}
\tag{0.4}
$$

Rigorous bounds:

$$
\boxed{
a_{3,-}(1)
>
0.040999,
}
\tag{0.5}
$$

$$
\boxed{
a_{3,+}(1)
>
0.0839.
}
\tag{0.6}
$$

Therefore the exact Fredholm compatibility pairing is nonzero at:

$$
\nu=1.
$$

Round 56 STOP:

$$
\boxed{
\text{STOP-C60}
=
\text{Viscosity-Parameter Continuation / Global Hidden-Manifold Gap}.
}
$$

---

# 1. Where viscosity enters the adjoint recurrence

In the $\mathcal C$-even real representation:

$$
\psi_n
=
i^n u_n,
$$

Round 56 recurrence is:

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
\tag{1.1}
$$

The same-parity Euler coefficients:

$$
A_{-2}^{(n)},
\quad
A_0^{(n)},
\quad
A_2^{(n)},
\quad
A_4^{(n)}
$$

are independent of:

$$
\nu.
$$

The cross-parity coefficient is exactly:

$$
\boxed{
B_1^{(n)}(K,\nu)
=
\nu
B_1^{(n)}(K,1).
}
\tag{1.2}
$$

This simple parameter dependence is the structural starting point of the continuation problem.

---

# 2. Exact viscosity scaling of the tail contraction

Round 56 defined:

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
-
B_1^{(n)}(K,\nu)
}.
}
\tag{2.1}
$$

Using (1.2):

$$
\boxed{
q_n(K,\nu)
=
\frac{
q_n(K,1)
}{
\nu
}.
}
\tag{2.2}
$$

Nomenclature:

$$
\boxed{
\textbf{Viscosity Tail-Scaling Identity}.
}
$$

No approximation is involved.

---

# 3. Large-depth contraction asymptotic

Rounds 53–56 give:

$$
\boxed{
A_0^{(n)}
+
A_2^{(n)}
=
8K
+
O(n^{-1}),
}
\tag{3.1}
$$

while:

$$
\boxed{
-
B_1^{(n)}
=
16\nu n^2
\left[
1+O(n^{-1})
\right].
}
\tag{3.2}
$$

The lower / far-upper coefficients are only:

$$
O(K^3n^{-2}).
$$

Therefore:

$$
\boxed{
q_n(K,\nu)
=
\frac{
K
}{
2\nu n^2
}
\left[
1+O(n^{-1})
\right].
}
\tag{3.3}
$$

So:

$$
\boxed{
q_n(K,\nu)\to0
}
$$

for every fixed:

$$
K>0,
\qquad
\nu>0.
$$

---

# 4. Movable-cutoff contraction principle

Fix:

$$
0<\theta<1.
$$

For every:

$$
\nu>0,
$$

there exists:

$$
N_{\rm tail}(K,\nu,\theta)
$$

such that:

$$
\boxed{
q_n(K,\nu)
\le
\theta
\qquad
\forall n\ge N_{\rm tail}.
}
\tag{4.1}
$$

At leading order:

$$
\boxed{
N_{\rm tail}
\sim
\sqrt{
\frac{
K
}{
2\theta\nu
}
}.
}
\tag{4.2}
$$

Thus small viscosity does **not** destroy the existence of a contractive Floquet tail.

It pushes the start of the rigorous tail farther outward.

Nomenclature:

$$
\boxed{
\textbf{Movable-Cutoff Tail Principle}.
}
$$

---

# 5. What can actually bifurcate

Because the tail can be made contractive for every fixed:

$$
\nu>0,
$$

a continuation failure must occur through the finite/global matching part.

There are two natural mechanisms:

## P1 — normalization / matching degeneracy

The canonical conditions:

$$
\psi_0=1,
\qquad
\psi_1=0
$$

could cease to select a unique minimal global mode if a Fredholm/Evans-type matching determinant vanishes.

## P2 — positivity crossing

The canonical mode can continue smoothly but:

$$
\boxed{
a_3(\nu)
=
\operatorname{Im}\psi_+(3;\nu)
}
$$

could cross:

$$
0.
$$

Round 57 numerically looks for both phenomena.

---

# 6. Physical finite-section continuation map

To avoid compact-block coordinate redundancies, the verification script uses the raw divergence-free physical Fourier basis:

$$
B_n\in(K,0,n)^\perp.
$$

For each viscosity:

$$
\nu,
$$

it computes:

1. the physical state-normal matrix;
2. an orthonormal basis:
   $$
   Q_N
   $$
   of:
   $$
   \ker\mathscr N_N;
   $$
3. the physical source map:
   $$
   A_N
   =
   \mathscr S_NQ_N;
   $$
4. the two localized adjoint cokernel modes;
5. the canonical central normalization:
   $$
   \psi_+(0)=1,
   \qquad
   \psi_+(1)=0;
   $$
6. the continuation diagnostic:
   $$
   a_{3,N}(\nu)
   =
   \operatorname{Im}\psi_{+,N}(3).
   $$

No compact-block quotient is used.

---

# 7. Logarithmic scan

The attached CSV / verification script scans:

$$
\boxed{
10^{-5}
\le
\nu
\le
10^3
}
\tag{7.1}
$$

on a logarithmic grid, with deeper truncation at smaller:

$$
\nu.
$$

For every tested parameter value and both fibres:

$$
\boxed{
a_{3,N}(\nu)>0.
}
\tag{7.2}
$$

No normalization singularity or sign flip is observed.

This is numerical continuation evidence, not an interval proof.

---

# 8. Shape of the small-fibre map

For:

$$
K_-
=
\sqrt{17}-3,
$$

representative values are:

$$
\boxed{
\begin{array}{c|c}
\nu
&
a_{3,-}(\nu)
\\
\hline
10^{-4}
&
5.7915\times10^{-4}
\\
10^{-3}
&
5.8001\times10^{-3}
\\
10^{-2}
&
5.8204\times10^{-2}
\\
10^{-1}
&
2.4662\times10^{-1}
\\
1
&
4.1191\times10^{-2}
\\
10
&
4.1469\times10^{-3}
\\
100
&
4.1471\times10^{-4}
\end{array}
}
\tag{8.1}
$$

The map rises from zero, reaches a broad maximum near:

$$
\nu\sim10^{-1},
$$

and returns to zero from above.

---

# 9. Shape of the large-fibre map

For:

$$
K_+
=
\sqrt{17}+3,
$$

$$
\boxed{
\begin{array}{c|c}
\nu
&
a_{3,+}(\nu)
\\
\hline
10^{-4}
&
5.3314\times10^{-4}
\\
10^{-3}
&
5.3280\times10^{-3}
\\
10^{-2}
&
5.2656\times10^{-2}
\\
10^{-1}
&
3.2400\times10^{-1}
\\
1
&
8.4277\times10^{-2}
\\
10
&
8.5648\times10^{-3}
\\
100
&
8.5662\times10^{-4}
\end{array}
}
\tag{9.1}
$$

Again:

$$
\boxed{
a_{3,+}(\nu)>0
}
$$

throughout the scan.

---

# 10. Small-viscosity diagnostic

Deep finite sections at:

$$
\nu
=
10^{-6},
10^{-5},
10^{-4}
$$

show:

$$
\boxed{
\frac{
a_{3,-}(\nu)
}{
\nu
}
\to
5.7905\ldots
}
\tag{10.1}
$$

and:

$$
\boxed{
\frac{
a_{3,+}(\nu)
}{
\nu
}
\to
5.3317\ldots
}
\tag{10.2}
$$

as:

$$
\nu\to0^+.
$$

Thus the data support:

$$
\boxed{
a_{3,\pm}(\nu)
=
c_{0,\pm}
\nu
+
o(\nu),
}
\tag{10.3}
$$

with:

$$
\boxed{
c_{0,-}
\approx
5.7905>0,
}
\tag{10.4}
$$

$$
\boxed{
c_{0,+}
\approx
5.3317>0.
}
\tag{10.5}
$$

This is a numerical endpoint asymptotic, not yet a singular-perturbation theorem.

---

# 11. Large-viscosity diagnostic

For:

$$
\nu
=
10^2,
10^3,
10^4,
$$

finite sections show:

$$
\boxed{
\nu
a_{3,-}(\nu)
\to
0.04147148\ldots
}
\tag{11.1}
$$

and:

$$
\boxed{
\nu
a_{3,+}(\nu)
\to
0.08566181\ldots
}
\tag{11.2}
$$

Therefore:

$$
\boxed{
a_{3,\pm}(\nu)
=
\frac{
c_{\infty,\pm}
}{
\nu
}
+
o(\nu^{-1}),
}
\tag{11.3}
$$

numerically, with both endpoint constants positive.

---

# 12. Bifurcation topology suggested by the map

The combined picture is:

$$
\boxed{
\begin{aligned}
a_3(\nu)
&\to0^+
&&
\nu\to0^+,
\\
a_3(\nu)
&>0
&&
\text{on the scanned interior},
\\
a_3(\nu)
&\to0^+
&&
\nu\to\infty.
\end{aligned}
}
\tag{12.1}
$$

No interior crossing is observed.

Hence the natural theorem candidate is:

$$
\boxed{
\textbf{Adjoint Positivity Conjecture: }
a_{3,\pm}(\nu)>0
\quad
\forall\nu>0.
}
\tag{12.2}
$$

---

# 13. Exact target pairing remains same-sign for all positive viscosity

Round 55 pairing:

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
\tag{13.1}
$$

Here:

$$
\boxed{
g_0(\nu)
=
12\nu
(
3r^2-1
).
}
\tag{13.2}
$$

The coefficient:

$$
G_{-3}
$$

is independent of:

$$
\nu.
$$

For the small fibre:

$$
\boxed{
3r_-^2-1<0,
\qquad
G_{-3}<0.
}
\tag{13.3}
$$

For the large fibre:

$$
\boxed{
3r_+^2-1>0,
\qquad
G_{-3}>0.
}
\tag{13.4}
$$

Therefore for every:

$$
\nu>0,
$$

$$
\boxed{
\operatorname{sign}g_0(\nu)
=
\operatorname{sign}G_{-3}.
}
\tag{13.5}
$$

Consequently:

$$
\boxed{
a_3(\nu)>0
\Longrightarrow
\langle
\psi_+,
g
\rangle
\ne0.
}
\tag{13.6}
$$

There is no second cancellation mechanism inside the pairing once positivity is established.

---

# 14. Endpoint pairing scales

If the numerical small-viscosity asymptotic is promoted to a theorem:

$$
a_3(\nu)
\sim
c_0\nu,
$$

then:

$$
\boxed{
\langle
\psi_+,
g
\rangle
\sim
\nu
\left[
12(3r^2-1)
+
c_0G_{-3}
\right].
}
\tag{14.1}
$$

Because both terms have the same sign, the Euler limit approaches the obstruction only linearly in:

$$
\nu,
$$

but does not suggest an interior sign reversal.

At large:

$$
\nu,
$$

$$
g_0
=
O(\nu),
$$

while:

$$
a_3G_{-3}
=
O(\nu^{-1}).
$$

So the pairing is dominated by:

$$
g_0
$$

and is automatically far from zero once positivity of the canonical mode is retained.

---

# 15. Why the small-viscosity end is the real continuation problem

For:

$$
\nu\gg1,
$$

the tail contraction starts extremely early:

$$
q_6(K,\nu)
\ll1,
$$

and the exact target pairing is dominated by:

$$
g_0=O(\nu).
$$

For:

$$
\nu\ll1,
$$

the tail cutoff scales approximately as:

$$
N_{\rm tail}
\sim
\nu^{-1/2}.
$$

The limit:

$$
\nu\to0^+
$$

is singular because the cross-parity viscous coupling disappears and the Round 53 Euler-like recurrence regains a neutral branch.

Thus the hardest endpoint is:

$$
\boxed{
\nu\to0^+.
}
\tag{15.1}
$$

A full uniform theorem should treat this limit by parity-rescaled singular perturbation rather than by letting the validated cutoff diverge indefinitely.

---

# 16. Natural parity rescaling near $\nu=0$

The numerical canonical modes show:

$$
u_{2j}
=
O(1),
$$

while:

$$
u_{2j+1}
=
O(\nu)
$$

as:

$$
\nu\to0^+.
$$

Define:

$$
\boxed{
u_{2j}
=
e_j,
}
\tag{16.1}
$$

$$
\boxed{
u_{2j+1}
=
\nu o_j.
}
\tag{16.2}
$$

Then:

- the even equations have viscous coupling only at:
  $$
  O(\nu^2);
  $$
- the odd equations, after dividing by:
  $$
  \nu,
  $$
  retain a finite forced limit.

So the small-viscosity positivity constant:

$$
c_0
=
\lim_{\nu\to0^+}
a_3(\nu)/\nu
$$

should be obtainable from a coupled **Euler minimal even mode + forced odd corrector** problem.

This is the natural analytic route to the singular endpoint.

---

# 17. Large-viscosity rescaling

The numerical data show:

$$
u_{2j+1}
=
O(\nu^{-1}),
$$

and for nonzero even levels:

$$
u_{2j}
=
O(\nu^{-2})
$$

as:

$$
\nu\to\infty.
$$

Thus define:

$$
\boxed{
u_{2j+1}
=
\nu^{-1}o_j,
}
\tag{17.1}
$$

$$
\boxed{
u_{2j}
=
\nu^{-2}e_j
\qquad
(j\ne0),
}
\tag{17.2}
$$

with:

$$
u_0=1.
$$

This produces a regular strong-viscosity hierarchy and explains:

$$
a_3(\nu)
=
O(\nu^{-1}).
$$

The large-viscosity end therefore appears analytically easier than:

$$
\nu\to0^+.
$$

---

# 18. Parameter-continuation strategy

A rigorous all-viscosity theorem can now be divided into three regimes:

## V-A — small viscosity

Use the parity-rescaled singular perturbation of Section 16 to prove:

$$
\boxed{
a_3(\nu)>0
\qquad
0<\nu\le\nu_{\rm s}.
}
$$

## V-B — compact middle interval

For:

$$
\nu\in
[
\nu_{\rm s},
\nu_{\rm l}
],
$$

use validated interval continuation:

- interval arithmetic in:
  $$
  \nu;
  $$
- a uniform movable tail cutoff;
- a radii-polynomial / Newton–Kantorovich or Banach enclosure of the canonical adjoint branch;
- direct interval lower bound on:
  $$
  a_3(\nu).
  $$

## V-C — large viscosity

Use the strong-viscosity rescaling of Section 17 to prove:

$$
\boxed{
a_3(\nu)>0
\qquad
\nu\ge\nu_{\rm l}.
}
$$

This is substantially more efficient than attempting one enormous interval proof over:

$$
(0,\infty).
$$

---

# 19. Current numerical safety margins

On the log scan:

$$
10^{-5}
\le\nu\le10^3,
$$

the coefficient never approaches a spurious interior zero.

The only small values occur near the expected endpoints:

$$
\nu\to0^+,
\qquad
\nu\to\infty.
$$

Representative peak diagnostics:

- small fibre:
  $$
  a_{3,-}
  \approx
  0.25
  $$
  near:
  $$
  \nu\approx8\times10^{-2};
  $$
- large fibre:
  $$
  a_{3,+}
  \approx
  0.33
  $$
  near:
  $$
  \nu\approx1.3\times10^{-1}.
  $$

Thus the compact-middle interval should have a large positivity margin.

The hard work is endpoint certification, not the middle.

---

# 20. STOP-C61 — Viscosity-Uniform Positivity / Endpoint-Continuation Gap

$$
\boxed{
\begin{aligned}
\text{layer}
&=
\mathrm{viscosity\ continuation\ of\ adjoint\ positivity},
\\
q_n(K,\nu)
&=
q_n(K,1)/\nu,
\\
q_n
&\sim
K/(2\nu n^2),
\\
\text{fixed }\nu>0\text{ tail contraction}
&=
\mathrm{available\ after\ movable\ cutoff},
\\
\text{possible bifurcation}
&=
\mathrm{finite\text{-}core\ matching}
\vee
a_3(\nu)=0,
\\
\text{scan range}
&=
10^{-5}\le\nu\le10^3,
\\
\text{observed sign}
&=
a_{3,\pm}(\nu)>0
\text{ everywhere scanned},
\\
\nu\to0^+
&:
a_3\sim c_0\nu,
\quad
c_0>0
\text{ numerically},
\\
\nu\to\infty
&:
a_3\sim c_\infty/\nu,
\quad
c_\infty>0
\text{ numerically},
\\
\text{interior zero}
&=
\mathrm{not\ observed},
\\
\text{uniform theorem}
&=
\mathrm{not\ yet\ proved},
\\
\text{missing}
&=
\mathrm{small\text{-}\nu\ singular\ perturbation}
+
\mathrm{validated\ middle\ continuation}
+
\mathrm{large\text{-}\nu\ enclosure},
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
\textbf{STOP-C61:
Viscosity-Uniform Positivity / Endpoint-Continuation Gap}.
}
$$

---

# 21. 24/72 Ledger — Round 57

| Step | object | $B$ | $U$ | $O$ | $L$ | status |
|---|---|---|---|---|---|---|
| C917 | viscosity entry in adjoint recurrence | $\mathsf C$ | parameterized Floquet operator | relational | $\mathsf F$ | EXACT |
| C918 | tail scaling $q_n(K,\nu)=q_n(K,1)/\nu$ | $\mathsf C$ | contraction geometry | scalar | $\mathsf F$ | EXACT |
| C919 | large-$n$ movable-cutoff law | $\mathsf C$ | asymptotic analysis | scalar | $\mathsf F$ | PROVED asymptotically |
| C920 | fixed-$\nu$ tail availability | $\mathsf C$ | Banach-tail route | targeted | $\mathsf F$ | IDENTIFIED |
| C921 | physical viscosity scan | $\mathsf C$ | raw Fourier finite section | profile | $\mathsf F$ | NUMERICALLY VERIFIED |
| C922 | small-fibre positivity map | $\mathsf C$ | parameter continuation | scalar | $\mathsf F$ | NUMERICAL |
| C923 | large-fibre positivity map | $\mathsf C$ | parameter continuation | scalar | $\mathsf F$ | NUMERICAL |
| C924 | small-$\nu$ linear asymptotic | $\mathsf C$ | singular endpoint | scalar | $\mathsf F$ | NUMERICAL / STRUCTURAL |
| C925 | large-$\nu$ inverse asymptotic | $\mathsf C$ | strong viscosity | scalar | $\mathsf F$ | NUMERICAL / STRUCTURAL |
| C926 | exact all-$\nu$ target sign geometry | $\mathsf C$ | Fredholm pairing | targeted | $\mathsf F$ | EXACT |
| C927 | small-$\nu$ parity rescaling | $\mathsf C$ | singular perturbation | relational | $\mathsf F$ | IDENTIFIED |
| C928 | large-$\nu$ parity rescaling | $\mathsf C$ | asymptotic hierarchy | relational | $\mathsf F$ | IDENTIFIED |
| C929 | interval continuation decomposition | $\mathsf C$ | validated parameter proof | targeted | $\mathsf F$ | ROUTE DESIGNED |
| C930 | viscosity-uniform positivity | $\mathsf C$ | global parameter branch | targeted | $\mathsf F$ | OPEN / STOP-C61 |

---

# 22. Continuous-versus-discrete status

The viscosity parameter:

$$
\nu\in(0,\infty)
$$

is continuous.

The continuation question is a continuous operator-family problem.

The log-grid and finite sections are diagnostic representations only; they do not constitute the intended proof closure.

The next rigorous route uses:

- parameter intervals;
- analytic endpoint rescaling;
- infinite-tail contraction;

all on continuous parameter families.

Therefore:

$$
\boxed{
T_{\mathsf C\to\mathsf D}
=
\text{NOT YET REACHED}.
}
$$

---

# 23. Strongest results of Round 57

## R57-A — exact viscosity tail scaling

$$
\boxed{
q_n(K,\nu)
=
q_n(K,1)/\nu.
}
$$

## R57-B — no fixed positive viscosity loses tail contractivity at infinity

$$
\boxed{
q_n(K,\nu)
\sim
K/(2\nu n^2)
\to0.
}
$$

## R57-C — the bifurcation problem is finite/global, not an infinity-loss problem

Any positivity failure must arise through finite-core matching or:

$$
\boxed{
a_3(\nu)=0.
}
$$

## R57-D — broad numerical positivity

For both source fibres, raw physical finite sections show:

$$
\boxed{
a_3(\nu)>0
}
$$

through:

$$
10^{-5}\le\nu\le10^3.
$$

## R57-E — positive endpoint diagnostics

$$
\boxed{
a_3(\nu)
\sim
c_0\nu
\quad
(\nu\to0^+),
}
$$

and:

$$
\boxed{
a_3(\nu)
\sim
c_\infty/\nu
\quad
(\nu\to\infty),
}
$$

with positive numerical constants at both fibres.

## R57-F — all-$\nu$ no-go reduces to all-$\nu$ positivity

Because target coefficients are same-sign:

$$
\boxed{
a_3(\nu)>0
\quad
\forall\nu>0
}
$$

would immediately extend Round 56's Fredholm obstruction through the entire positive-viscosity parameter line.

---

# 24. Next round — Small-Viscosity Singular Adjoint Limit / Positive Slope

The numerics indicate the most delicate endpoint is:

$$
\nu\to0^+.
$$

So the next round should not start with interval gridding.

It should first derive the endpoint theorem:

$$
\boxed{
\lim_{\nu\to0^+}
\frac{
a_3(\nu)
}{
\nu
}
=
c_0>0.
}
$$

Concrete targets:

1. split:
   $$
   u_{2j}=e_j,
   \qquad
   u_{2j+1}=\nu o_j;
   $$

2. derive the exact:
   $$
   \nu=0
   $$
   even minimal adjoint problem;

3. derive the forced odd corrector equation;

4. construct both with minimal/analytic tails;

5. evaluate:
   $$
   c_0=-o_1
   $$
   in the indexing where:
   $$
   u_3=\nu o_1;
   $$

6. prove:
   $$
   c_0>0
   $$
   for both source fibres;

7. obtain a quantitative:
   $$
   a_3(\nu)\ge
   \frac12c_0\nu
   $$
   on:
   $$
   (0,\nu_{\rm s}];
   $$

8. only then perform validated continuation over the compact middle interval.

This becomes:

$$
\boxed{
\textbf{Small-Viscosity Singular Adjoint Limit / Positive Slope}.
}
$$

---

# 25. External primary-source anchors

1. Christian Pötzsche, Robert Skiba, *Evans function, parity and nonautonomous bifurcations*, arXiv:2503.07221.
   - relates Evans functions to parity, dichotomy spectrum and hyperbolicity in parameter-dependent Fredholm/bifurcation problems;
   - relevant structural context for treating a possible zero of the matching functional as a parameter bifurcation rather than as a tail-loss event.

2. Yuri Latushkin, Shibi Vasudevan, *Fredholm determinants, continued fractions, Jost and Evans functions for a Jacobi matrix associated with the 2D-Euler equations*, arXiv:2401.14037.
   - connects difference-equation Fredholm determinants, Jost/Evans functions and continued fractions in a fluid-stability problem;
   - relevant to future analytic representations of the viscosity-dependent matching functional.

3. Matthieu Cadiot, Jean-Philippe Lessard, *Recent advances about the rigorous integration of parabolic PDEs via fully spectral Fourier-Chebyshev expansions*, arXiv:2502.20644.
   - develops explicit rigorous spectral error bounds and Newton–Kantorovich validation, including a 2D Navier–Stokes application;
   - relevant methodological context for the planned interval continuation over a compact viscosity range.

4. Jacek Cyranka, Jean-Philippe Lessard, *Validated forward integration scheme for parabolic PDEs via Chebyshev series*, arXiv:2101.00684.
   - provides a Banach-space Fourier/Chebyshev validated-numerics framework with computable inverse bounds;
   - relevant methodological context only, not a source for the NS-specific Round 57 formulas.

The viscosity tail-scaling identity, movable-cutoff principle and all NS-specific continuation quantities are direct derivations / computations of this round.

---

# 26. Commit state

$$
\boxed{
\begin{aligned}
\text{Route}
&=
\mathrm{Pure\ Continuous\ Viscosity\ Continuation},
\\
\text{Essential }\mathsf C\to\mathsf D
&=
\mathrm{Not\ reached},
\\
\text{Round 56 }\nu=1\text{ closure}
&=
\mathrm{rigorous},
\\
\text{Tail contraction for fixed }\nu>0
&=
\mathrm{available\ after\ movable\ cutoff},
\\
\text{Observed }a_3(\nu)
&=
\mathrm{positive\ on\ }[10^{-5},10^3],
\\
\text{Small-viscosity endpoint}
&=
\mathrm{positive\ linear\ slope\ suggested},
\\
\text{Large-viscosity endpoint}
&=
\mathrm{positive\ inverse\ tail\ suggested},
\\
\text{Interior bifurcation}
&=
\mathrm{not\ observed},
\\
\text{Uniform theorem}
&=
\mathrm{not\ yet\ claimed},
\\
\text{STOP-C61}
&=
\mathrm{Viscosity\text{-}Uniform\ Positivity/Endpoint\text{-}Continuation\ Gap},
\\
\text{Next}
&=
\mathrm{Small\text{-}Viscosity\ Singular\ Adjoint\ Limit/Positive\ Slope}.
\end{aligned}
}
$$