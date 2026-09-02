# NS-DCRP-37 — Affine-Jet / Vorticity-Covariance Phase Locking, Eigenframe Dynamics, and the Very-Non-Generic Alignment Frontier

- date: 2026-08-17
- status: research proof checkpoint / phase-rigidity entry
- canonical source: UTF-8 Markdown
- canonical math delimiters: `$...$` and `$$...$$`
- objective:
  1. convert the DCRP-36 affine-jet magnitude problem into a tensor phase/alignment problem;
  2. define a normalized strain--vorticity covariance phase parameter;
  3. distinguish persistent phase locking, phase slip, and intermittent relocking;
  4. derive the eigenframe evolution formula for the affine strain jet and the core vorticity covariance;
  5. identify the relative rotation dynamics on $SO(3)$;
  6. show that persistent positive stretching requires nontrivial scale-time coherence between the annular affine jet and the core vorticity covariance;
  7. isolate the next frontier as classification of phase-locked low-dimensional invariant modes versus phase-transition/concentration defects.
- no full Navier--Stokes regularity claim is made.
- internal dependencies:
  - DCRP-35 finite-annulus affine strain supplier;
  - DCRP-36 affine-jet reproduction equation and critical shell packing.
- no novelty/priority claim is made without independent audit.

---

# 1. Executive result

DCRP-36 showed that the finite-annulus affine strain supplier can remain scale-critical in magnitude:

$$
\widehat A_R
=
R^{\alpha+1}A_R,
$$

with

$$
\|\widehat A_R\|
\sim O(1)
$$

across geometric DSS-related scales without violating the critical tail-energy envelope.

Therefore:

$$
\boxed{
\textbf{
jet magnitude alone cannot close the strict Type-II branch.
}
}
\tag{1.1}
$$

The actual core stretching is not controlled by:

$$
|A|
$$

alone.

Let:

$$
\boxed{
B(s)
=
\int_{B_{r_0}}
\Omega(y,s)
\otimes
\Omega(y,s)\,dy.
}
\tag{1.2}
$$

Then:

$$
B(s)
$$

is symmetric positive semidefinite and the affine-jet core work is

$$
\boxed{
\mathcal W_{AB}
=
\int_0^{S_0}
\left(
A(s):B(s)
\right)_+ds.
}
\tag{1.3}
$$

Thus the dangerous quantity is the **relative tensor orientation** of:

- the external affine strain jet:

  $$
  A(s)\in\mathrm{Sym}_0(3);
  $$

- the core vorticity covariance:

  $$
  B(s)\in\mathrm{Sym}_+(3).
  $$

This is the phase/alignment frontier.

---

# 2. Normalized tensor phase

Define the Frobenius-normalized alignment parameter whenever:

$$
A\neq0,
\qquad
B\neq0:
$$

$$
\boxed{
\chi_{AB}(s)
=
\frac{
A(s):B(s)
}{
|A(s)|_F
|B(s)|_F
}.
}
\tag{2.1}
$$

Then:

$$
\boxed{
-1
\le
\chi_{AB}
\le
1.
}
\tag{2.2}
$$

Positive vortex stretching requires:

$$
\boxed{
\chi_{AB}>0
}
\tag{2.3}
$$

on a set of positive measure in similarity time.

A persistent positive core-work gap therefore requires persistent positive **phase coherence**, not merely large jet magnitude.

---

# 3. Eigenframe representation

Diagonalize:

$$
\boxed{
A
=
Q
\Lambda_A
Q^T,
}
\tag{3.1}
$$

where:

$$
Q\in SO(3),
$$

and:

$$
\boxed{
\Lambda_A
=
\operatorname{diag}
(
a_1,a_2,a_3
),
\qquad
a_1+a_2+a_3=0.
}
\tag{3.2}
$$

Likewise:

$$
\boxed{
B
=
R
\Lambda_B
R^T,
}
\tag{3.3}
$$

with:

$$
R\in SO(3),
$$

and:

$$
\boxed{
\Lambda_B
=
\operatorname{diag}
(
b_1,b_2,b_3
),
\qquad
b_j\ge0.
}
\tag{3.4}
$$

Define the relative eigenframe rotation:

$$
\boxed{
O
=
Q^TR
\in SO(3).
}
\tag{3.5}
$$

Then:

$$
\boxed{
A:B
=
\sum_{i,j}
a_i b_j
|O_{ij}|^2.
}
\tag{3.6}
$$

Thus the stretching work depends explicitly on the relative angular distribution:

$$
|O_{ij}|^2.
$$

The problem is genuinely finite-dimensional in the phase fiber once the eigenvalues are fixed.

---

# 4. Why magnitude is insufficient

Suppose:

$$
|A|_F
\sim1,
\qquad
|B|_F
\sim1.
$$

Then:

$$
A:B
$$

can still be:

- strongly positive;
- nearly zero;
- or negative;

depending entirely on:

$$
O.
$$

Therefore:

$$
\boxed{
\textbf{
critical magnitude recurrence}
\not\Rightarrow
\textbf{
critical stretching recurrence}.
}
}
\tag{4.1}
$$

A strict Type-II branch must preserve **orientation coherence** as well.

---

# 5. Phase-locking alternatives

The recurrent affine branch naturally splits into three phase regimes.

## persistent phase locking

There exists a recurrent relative orientation:

$$
O_\ast(s)
$$

such that after DSS quotienting:

$$
\boxed{
O_{n+1}(s)
\to
O_n(s+\theta)
}
\tag{5.1}
$$

or a fixed/periodic version thereof.

The positive stretching cone is visited recurrently with a fixed measure and a fixed positive work fraction.

## phase slip

There is:

$$
\delta_{\rm ph}>0
$$

such that infinitely often:

$$
\boxed{
d_{SO(3)}
\left(
O_{n+1},
O_n
\right)
\ge
\delta_{\rm ph}.
}
\tag{5.2}
$$

This is a genuine angular/phase transition residual.

## intermittent relocking

The phase is not globally recurrent, but positive stretching is concentrated on shrinking or moving subsets of similarity time where the eigendirections temporarily relock.

This produces a time-phase concentration defect.

Thus:

$$
\boxed{
\textbf{
phase locking}
\ \vee\
\textbf{
phase slip}
\ \vee\
\textbf{
phase concentration}.
}
\tag{5.3}
$$

---

# 6. Affine-jet derivative

Let:

$$
A
=
Q\Lambda_AQ^T.
$$

Define the skew-symmetric angular velocity:

$$
\boxed{
\Xi
=
Q^TQ'.
}
\tag{6.1}
$$

Then:

$$
\boxed{
\Xi^T
=
-\Xi.
}
\tag{6.2}
$$

Differentiate:

$$
A.
$$

Since:

$$
Q'
=
Q\Xi,
$$

one obtains:

$$
\boxed{
A'
=
Q
\left[
\Lambda_A'
+
[\Xi,\Lambda_A]
\right]
Q^T.
}
\tag{6.3}
$$

The commutator:

$$
\boxed{
[\Xi,\Lambda_A]
}
\tag{6.4}
$$

is the exact **eigenframe rotation / phase-velocity term**.

Thus the DCRP-36 reproduction equation:

$$
A'+A
=
J_{\rm tr}
+
J_{\rm str}
$$

contains both:

- eigenvalue reproduction;
- eigenframe rotation.

---

# 7. Core covariance derivative

Likewise write:

$$
B
=
R\Lambda_BR^T,
$$

and define:

$$
\boxed{
\Upsilon
=
R^TR'.
}
\tag{7.1}
$$

Then:

$$
\boxed{
B'
=
R
\left[
\Lambda_B'
+
[\Upsilon,\Lambda_B]
\right]
R^T.
}
\tag{7.2}
$$

Thus the core vorticity covariance has its own angular velocity:

$$
\Upsilon.
$$

---

# 8. Relative phase dynamics

Recall:

$$
O=Q^TR.
$$

Differentiate:

$$
O'
=
(Q^T)'R
+
Q^TR'.
$$

Since:

$$
(Q^T)'
=
-\Xi Q^T,
$$

and:

$$
R'
=
R\Upsilon,
$$

one obtains:

$$
\boxed{
O'
=
-\Xi O
+
O\Upsilon.
}
\tag{8.1}
$$

This is the exact relative eigenframe phase equation.

Thus the next obstruction question is:

$$
\boxed{
\textbf{
what dynamically keeps }O(s)
\textbf{ inside the positive stretching cone every DSS return?}
}
\tag{8.2}
$$

---

# 9. Positive stretching cone

For fixed eigenvalues:

$$
\Lambda_A,
\qquad
\Lambda_B,
$$

define the stretching cone:

$$
\boxed{
\mathcal C_+
=
\left\{
O\in SO(3):
\sum_{i,j}
a_i b_j
|O_{ij}|^2
>
0
\right\}.
}
\tag{9.1}
$$

The strict affine supplier branch requires:

$$
\boxed{
\operatorname{meas}
\left\{
s\in[0,S_0]:
O(s)\in\mathcal C_+
\right\}
>0.
}
\tag{9.2}
$$

A uniform positive work gap requires a quantitative version:

$$
\boxed{
\int_0^{S_0}
\left[
\sum_{i,j}
a_i b_j
|O_{ij}|^2
\right]_+
ds
\ge
w_0.
}
\tag{9.3}
$$

---

# 10. Phase-slip residual

Define a one-period phase mismatch after all declared DSS quotient symmetries:

$$
\boxed{
\mathcal R_{\rm ph}
=
d_{SO(3)}
\left(
O(S_0),
\mathcal Q_{\rm sym}
O(0)
\right),
}
\tag{10.1}
$$

where:

$$
\mathcal Q_{\rm sym}
$$

represents allowed discrete rotational/eigenvalue-permutation symmetries.

If:

$$
\boxed{
\mathcal R_{\rm ph}>0,
}
\tag{10.2}
$$

the branch has a genuine angular transition defect.

Only:

$$
\boxed{
\mathcal R_{\rm ph}=0
}
\tag{10.3}
$$

belongs to the exact phase-locked equality manifold.

---

# 11. Degenerate eigenvalue safety

If:

$$
A
$$

or:

$$
B
$$

has repeated eigenvalues, the eigenframe is not uniquely defined.

Therefore:

$$
O
$$

must be interpreted modulo the stabilizer groups of:

$$
\Lambda_A
$$

and:

$$
\Lambda_B.
$$

The correct phase space is a quotient of:

$$
SO(3)
$$

by the corresponding isotropy subgroups.

Thus phase residuals must not assign a cost to rotations inside degenerate eigenspaces.

This is the tensor-phase analogue of the earlier translation/scale quotient corrections.

---

# 12. Phase concentration measure

Suppose:

$$
O_n(s)
$$

does not converge strongly in time but the positive stretching work remains bounded below.

Define the positive phase-work measures:

$$
\boxed{
d\mu_n^{\rm ph}(s)
=
\frac{
\left(
A_n:B_n
\right)_+
}{
\int_0^{S_0}
\left(
A_n:B_n
\right)_+d\tau
}
ds.
}
\tag{12.1}
$$

These are probability measures on:

$$
[0,S_0].
$$

After subsequence extraction:

$$
\boxed{
\mu_n^{\rm ph}
\stackrel{\ast}{\rightharpoonup}
\mu_\ast^{\rm ph}.
}
\tag{12.2}
$$

If the limiting measure is singular or atomic, the stretching survives through temporal phase concentration rather than smooth phase locking.

This is an explicit defect coordinate.

---

# 13. Phase-locking equality manifold

The strongest compact affine branch therefore satisfies:

$$
\boxed{
\mathcal R_{\rm ph}=0
}
\tag{13.1}
$$

and no singular phase-work measure.

Then the relative orientation:

$$
O(s)
$$

is a recurrent/periodic trajectory in the finite-dimensional phase quotient.

The remaining state is a **phase-locked tensor eigenmode**.

This is the correct finite-dimensional equality manifold.

---

# 14. Reproduction equation in the eigenframe

DCRP-36 gives:

$$
\boxed{
A'+A
=
J_A,
}
\tag{14.1}
$$

where:

$$
J_A
=
J_{\rm tr}
+
J_{\rm str}.
$$

Conjugate by:

$$
Q^T
$$

and:

$$
Q.
$$

Using (6.3):

$$
\boxed{
\Lambda_A'
+
[\Xi,\Lambda_A]
+
\Lambda_A
=
Q^TJ_AQ.
}
\tag{14.2}
$$

Hence:

### diagonal part

controls eigenvalue reproduction:

$$
\boxed{
\Lambda_A'
+
\Lambda_A
=
\operatorname{diag}
(
Q^TJ_AQ
)
}
\tag{14.3}
$$

up to degenerate-block conventions.

### off-diagonal part

controls eigenframe rotation:

$$
\boxed{
[\Xi,\Lambda_A]
=
\operatorname{offdiag}
(
Q^TJ_AQ
).
}
\tag{14.4}
$$

Therefore the annular source dynamics must explicitly supply both:

- strain magnitude/eigenvalue reproduction;
- strain orientation rotation.

---

# 15. Angular-source necessity

If:

$$
\Lambda_A
$$

has separated eigenvalues, then:

$$
[\Xi,\Lambda_A]
$$

controls:

$$
\Xi
$$

quantitatively.

Indeed for:

$$
i\neq j,
$$

$$
\boxed{
[\Xi,\Lambda_A]_{ij}
=
\Xi_{ij}
(a_j-a_i).
}
\tag{15.1}
$$

Thus, away from eigenvalue degeneracy:

$$
\boxed{
|\Xi_{ij}|
\le
\frac{
|
(Q^TJ_AQ)_{ij}
|
}{
|a_i-a_j|
}.
}
\tag{15.2}
$$

Therefore any persistent jet-frame rotation requires a persistent **off-diagonal reproduction source**.

The phase cannot rotate for free.

---

# 16. Core angular velocity

An analogous decomposition of:

$$
B'
$$

gives:

$$
\boxed{
[\Upsilon,\Lambda_B]
=
\operatorname{offdiag}
(
R^TB'R
).
}
\tag{16.1}
$$

Thus the core vorticity covariance orientation rotates only if its own evolution supplies off-diagonal covariance production.

The relative phase dynamics:

$$
O'
=
-\Xi O+O\Upsilon
$$

therefore reflect a competition between:

- annular jet angular source;
- core covariance angular source.

Persistent locking requires a dynamical synchronization of these two independent source channels.

---

# 17. Very-non-generic alignment formulation

The strict branch now requires simultaneously:

1. critical jet magnitude:

   $$
   |\widehat A_R|
   \sim O(1);
   $$

2. nonzero core vorticity covariance:

   $$
   B\neq0;
   $$

3. positive relative alignment:

   $$
   A:B>0;
   $$

4. recurrent phase dynamics:

   $$
   O(s+S_0)
   \sim
   O(s)
   $$

   modulo allowed symmetries;

5. reproduction of the jet eigenvalues;

6. reproduction of the jet eigenframe orientation;

7. reproduction of the core covariance orientation.

Thus the surviving state must satisfy a multi-coordinate synchronization condition.

This is the precise mathematical meaning of the informal phrase:

> "why does the very non-generic phase keep lining up?"

---

# 18. Phase-locking NO-GO to scalar coercivity

A scalar observable depending only on:

$$
|A|,
\quad
|B|,
\quad
E(R)
$$

cannot distinguish:

- a strongly aligned dangerous state;
- a decorrelated harmless state.

Therefore:

$$
\boxed{
\textbf{
scalar magnitude-only coercivity cannot close the affine branch.
}
}
\tag{18.1}
$$

A valid detector must retain angular information.

---

# 19. Finite-dimensional compactness

After normalization and quotienting eigenvalue degeneracies, the relative phase variable belongs to a compact finite-dimensional space.

Therefore for a compact normalized class, phase-slip alternatives can be compressed to finitely many angular charts.

This is significantly simpler than the original infinite-dimensional Navier--Stokes state space.

The remaining infinite-dimensional content enters only through the source terms driving:

$$
\Xi
$$

and:

$$
\Upsilon.
$$

---

# 20. Candidate phase defect package

A minimal phase-aware obstruction package may contain:

$$
\boxed{
\mathfrak D_{\rm phase}
=
\left(
\mathcal R_{\rm ph},
\mu_{\rm ph},
\mathcal A_{\rm ang}^{A},
\mathcal A_{\rm ang}^{B}
\right),
}
\tag{20.1}
$$

where:

-:

  $$
  \mathcal R_{\rm ph}
  $$

  is one-period angular mismatch;

-:

  $$
  \mu_{\rm ph}
  $$

  is the temporal phase-concentration measure;

-:

  $$
  \mathcal A_{\rm ang}^{A}
  $$

  is the annular jet off-diagonal reproduction action;

-:

  $$
  \mathcal A_{\rm ang}^{B}
  $$

  is the core covariance angular-production action.

These coordinates are native to the state/source dynamics.

---

# 21. Phase-locked eigenmode branch

If all phase defects vanish, the surviving branch must approach a finite-dimensional recurrent eigenmode.

Schematically:

$$
\boxed{
O(s)
=
O_\ast(s),
}
\tag{21.1}
$$

with:

$$
O_\ast
$$

periodic or symmetry-fixed.

Then:

$$
\boxed{
A:B
}
$$

is a deterministic periodic function of:

- the three strain eigenvalues;
- the three covariance eigenvalues;
- the finite-dimensional relative orientation orbit.

The problem reduces to classifying this recurrent tensor mode.

---

# 22. Possible rigid subcases

Several special subcases are natural.

## fixed eigenframe locking

$$
\boxed{
O(s)\equiv O_\ast.
}
\tag{22.1}
$$

Then:

$$
\Xi O_\ast
=
O_\ast\Upsilon.
$$

The annular and core frames rotate synchronously.

## rotating-wave locking

$$
O(s)
$$

is nonconstant but periodic.

This is a tensor analogue of a rotating wave / relative periodic orbit.

## eigenvalue-degenerate locking

One tensor has a repeated eigenvalue and the relevant phase is reduced to an axis-direction alignment.

This may be the most robust surviving mode.

Each subcase is finite-dimensional.

---

# 23. Alignment with extensional eigendirections

Since:

$$
B
$$

is positive semidefinite, positive:

$$
A:B
$$

requires sufficient covariance weight on the positive eigenspaces of:

$$
A.
$$

If:

$$
a_1\ge a_2\ge a_3,
\qquad
a_1>0>a_3,
$$

then dangerous stretching requires a nontrivial part of:

$$
B
$$

to remain aligned with the extensional directions.

Thus the phase problem is equivalent to persistent vorticity-covariance occupancy of the extensional strain bundle.

---

# 24. Intermittent relocking route

A state may evade smooth phase locking by allowing:

$$
\chi_{AB}
$$

to be small most of the time but large on sparse intervals.

If the positive work remains fixed:

$$
\int
(A:B)_+
\ge
w_0,
$$

then the amplitude on those intervals must increase as their temporal measure decreases.

Therefore intermittent relocking creates a time-concentration tradeoff.

This should be treated as a phase analogue of DCRP's earlier temporal spike / trace-concentration defects.

A quantitative concentration theorem is not yet proved in this round.

---

# 25. Same-parent scale phase

The DSS return also links different spatial scales.

Thus there is a second phase coordinate across scale:

$$
\boxed{
O_j(s)
=
Q_j(s)^TR_j(s).
}
\tag{25.1}
$$

A strict scale-recurrent phase-locked branch requires:

$$
\boxed{
O_{j+1}(s)
\approx
\mathcal G
O_j(s+\theta)
}
\tag{25.2}
$$

for an allowed rotational/permutation symmetry:

$$
\mathcal G.
$$

Failure gives a scale-phase transition defect.

---

# 26. Scale-phase coherence requirement

The DCRP-36 critical packing theorem permits:

$$
|\widehat A_{R_j}|
\sim1
$$

for infinitely many scales.

But dangerous stretching at infinitely many scales further requires:

$$
\boxed{
A_j:B_j
\gtrsim
c>0
}
\tag{26.1}
$$

after normalization.

This requires the relative tensor phase to remain in a dangerous cone across scale.

Therefore the remaining branch is not merely a critical magnitude cascade.

It is a **critical phase-coherent affine-jet cascade**.

---

# 27. Why this may be more rigid than the magnitude cascade

Magnitude recurrence uses scalar critical scaling and is compatible with geometric shell packing.

Phase recurrence lives on a compact group quotient.

Repeated nontrivial phase drift cannot be hidden by increasing physical scale.

It either:

- converges to an invariant/periodic phase orbit;
- remains chaotic but recurrent;
- or generates a nonzero transition/concentration defect.

Thus phase coherence has a qualitatively different compactness structure from critical energy magnitude.

---

# 28. No theorem yet excluding chaotic phase recurrence

A compact finite-dimensional phase dynamics can in principle support:

- periodic orbits;
- quasiperiodic motion;
- chaotic recurrent sets.

Therefore:

$$
\boxed{
\textbf{
phase recurrence alone is not a contradiction.
}
}
\tag{28.1}
$$

The next step must exploit that:

$$
O'
=
-\Xi O+O\Upsilon
$$

is not an arbitrary $SO(3)$ ODE.

Its generators:

$$
\Xi,
\Upsilon
$$

are themselves produced by the annular Navier--Stokes/Euler source dynamics.

---

# 29. Correct next frontier

The next target is:

$$
\boxed{
\textbf{
Affine-Jet Phase/Angular Cancellation /
Same-Parent Reproduction Rigidity.
}
}
$$

A useful theorem would prove:

> Let a same-parent strict DSS branch have:
>
> $$
> \|\widehat A_{R_j}\|\ge a_0,
> $$
>
> and:
>
> $$
> \int
> (\widehat A_{R_j}:B_j)_+
> \ge
> w_0.
> $$
>
> Then at least one of:
>
> 1.:
>    
>    $$
>    \text{nonzero scale/time phase transition residual};
>    $$
>
> 2.:
>    
>    $$
>    \text{temporal phase concentration};
>    $$
>
> 3.:
>    
>    $$
>    \text{off-diagonal jet reproduction action};
>    $$
>
> 4.:
>    
>    $$
>    \text{off-diagonal covariance production};
>    $$
>
> 5. a finite-dimensional phase-locked eigenmode
>
> must survive.
>
> Then classify the final eigenmode branch.

This is now the narrowest non-scalar closure problem in the DCRP chain.

---

# 30. End state

DCRP-36 showed:

$$
\boxed{
\text{critical jet magnitude}
}
$$

can persist across infinitely many scales.

DCRP-37 identifies the missing variable:

$$
\boxed{
\textbf{
relative tensor phase}.
}
$$

The affine-core work is:

$$
\boxed{
A:B
=
\sum_{i,j}
a_i b_j
|O_{ij}|^2,
\qquad
O=Q^TR.
}
$$

The relative phase evolves by:

$$
\boxed{
O'
=
-\Xi O
+
O\Upsilon.
}
$$

Therefore persistent dangerous stretching requires recurrent synchronization of:

- annular jet eigenvalues;
- annular jet eigenframe;
- core covariance eigenvalues;
- core covariance eigenframe;
- DSS time phase;
- DSS scale phase.

The surviving strict branch is thus a:

$$
\boxed{
\textbf{
critical phase-coherent affine-jet cascade}.
}
$$

The next frontier is not magnitude.

It is:

$$
\boxed{
\textbf{
phase locking versus phase slip versus phase concentration.
}
}
$$