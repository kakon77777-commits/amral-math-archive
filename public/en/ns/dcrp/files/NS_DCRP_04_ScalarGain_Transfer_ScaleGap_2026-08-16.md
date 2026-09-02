# NS-DCRP-04 — Scalar Gain Transfer, Relaxed Return Debt, and the Scale-Gap Boundary

- date: 2026-08-16
- status: research proof checkpoint
- canonical source: UTF-8 Markdown
- canonical math delimiters: `$...$` and `$$...$$`
- objective: continue DCRP-03 by removing the unnecessary high-derivative transfer requirement from the logarithmic cone-debt route.
- no new detector taxonomy is introduced.
- principal internal dependencies: MORP-02, MORP-03, MORP-04, DCRP-03.
- principal external calibration: Evan Miller, arXiv:2407.02691v2; Pineau--Vicol, arXiv:2607.09619v1.

---

# 1. Executive result

DCRP-03 introduced the scale-invariant logarithmic model-cone debt

$$
\mathfrak D_{SV}[a,b]
=
\int_a^b
\tau_{SV}(t)\,dt,
$$

where

$$
\tau_{SV}(t)
=
\frac{
(\chi_{SV}(t)-1)_+
\|-\Delta S(t)\|_2^2
}{
\|S(t)\|_{\dot H^1}^2
},
$$

and proved

$$
\boxed{
\frac12
\log
\frac{
\|S(b)\|_{\dot H^1}^2
}{
\|S(a)\|_{\dot H^1}^2
}
\le
\mathfrak D_{SV}[a,b].
}
\tag{1.1}
$$

The previous checkpoint then formulated a Log-Cone Transfer Lemma involving strong convergence of the high-derivative objects

$$
\Delta S_n
$$

and

$$
Q_n.
$$

That transfer requirement is stronger than necessary.

The key observation is that the right side of the desired scale-return contradiction can be accessed through the scalar endpoint gain

$$
\boxed{
g_{SV}[a,b]
=
\frac{
\|S(b)\|_{\dot H^1}^2
}{
\|S(a)\|_{\dot H^1}^2
}.
}
\tag{1.2}
$$

Equation (1.1) immediately gives

$$
\boxed{
\mathfrak D_{SV}[a,b]
\ge
\frac12
\log g_{SV}[a,b].
}
\tag{1.3}
$$

whenever

$$
g_{SV}\ge1.
$$

For an exact scale return with factor

$$
\lambda>1,
$$

the scaling law gives

$$
g_{SV}=\lambda^3.
$$

Therefore

$$
\boxed{
\mathfrak D_{SV}
\ge
\frac32\log\lambda.
}
\tag{1.4}
$$

The important new point is:

> to transfer this lower bound through a MORP return limit, it is enough to retain the two scalar transition coordinates
>
> $$
> \lambda_n
> $$
>
> and
>
> $$
> g_{SV,n}.
> $$

No strong convergence of

$$
Q_n
$$

or

$$
\Delta S_n
$$

is required.

This reduces the former Log-Cone Transfer Lemma to a scalar compatibility problem.

---

# 2. Exact strain-growth inequality recalled

Let

$$
S=\nabla_{\rm sym}u
$$

and

$$
Q
=
P_{st}
\left(
(u\cdot\nabla)S
+
S^2
+
\frac34\omega\otimes\omega
\right).
$$

Miller's exact identity is

$$
\boxed{
\frac12
\frac d{dt}
\|S\|_{\dot H^1}^2
+
\|-\Delta S\|_2^2
=
-
\langle
-\Delta S,Q
\rangle.
}
\tag{2.1}
$$

Set

$$
H(t)
=
\|S(t)\|_{\dot H^1}^2
$$

and

$$
Z(t)
=
\|-\Delta S(t)\|_2.
$$

Define

$$
\chi_{SV}(t)
=
\frac{\|Q(t)\|_2}{Z(t)}
$$

when

$$
Z(t)>0,
$$

and

$$
\tau_{SV}(t)
=
\frac{
(\chi_{SV}(t)-1)_+Z(t)^2
}{
H(t)
}.
$$

DCRP-03 proved

$$
\boxed{
\frac12
\frac d{dt}
\log H(t)
\le
\tau_{SV}(t)
}
\tag{2.2}
$$

whenever

$$
H(t)>0.
$$

Integrating:

$$
\boxed{
\frac12
\log
\frac{H(b)}{H(a)}
\le
\mathfrak D_{SV}[a,b].
}
\tag{2.3}
$$

This is the only PDE estimate needed for the transfer theorem below.

---

# 3. Definition — scalar strain gain coordinate

For any actual return interval

$$
R=[a,b]
$$

with

$$
0<H(a),H(b)<\infty,
$$

define

$$
\boxed{
g_{SV}(R)
=
\frac{H(b)}{H(a)}.
}
\tag{3.1}
$$

Define the positive logarithmic gain

$$
\boxed{
\Gamma_{SV}(R)
=
\frac12
\left[
\log g_{SV}(R)
\right]_+.
}
\tag{3.2}
$$

Then (2.3) implies

$$
\boxed{
\Gamma_{SV}(R)
\le
\mathfrak D_{SV}(R).
}
\tag{3.3}
$$

Hence

$$
\Gamma_{SV}
$$

is a scalar lower certificate for the full log-cone debt.

It is not a dangerous mark.

It is generated only from the actual endpoint strain norms of one return interval.

---

# 4. Scaling law for the scalar gain

Under Navier--Stokes parabolic scaling,

$$
u_\lambda(x,t)
=
\lambda
u(\lambda x,\lambda^2t),
$$

the strain satisfies

$$
S_\lambda(x,t)
=
\lambda^2
S(\lambda x,\lambda^2t).
$$

Therefore

$$
\|S_\lambda\|_{\dot H^1}^2
=
\lambda^3
\|S\|_{\dot H^1}^2.
$$

Thus if a return interval is exactly related by a scale factor

$$
\lambda>1
$$

up to translations and orthogonal rotations, then

$$
\boxed{
g_{SV}
=
\lambda^3.
}
\tag{4.1}
$$

Consequently

$$
\boxed{
\Gamma_{SV}
=
\frac32\log\lambda.
}
\tag{4.2}
$$

and by (3.3),

$$
\boxed{
\mathfrak D_{SV}
\ge
\frac32\log\lambda.
}
\tag{4.3}
$$

---

# 5. Theorem — Scalar Gain Transfer

## Theorem 5.1

Let

$$
R_n
$$

be a sequence of actual finite-$\dot H^1$ Navier--Stokes return intervals.

Let

$$
\lambda_n>1
$$

be their declared parabolic re-root / return scale factors.

Assume

$$
\lambda_n\to\lambda_\ast
$$

with

$$
\lambda_\ast>1.
$$

Assume only the scalar gain compatibility

$$
\boxed{
g_{SV}(R_n)
\to
\lambda_\ast^3.
}
\tag{5.1}
$$

Then

$$
\boxed{
\liminf_{n\to\infty}
\mathfrak D_{SV}(R_n)
\ge
\frac32
\log\lambda_\ast
>
0.
}
\tag{5.2}
$$

### Proof

For every

$$
n,
$$

equation (3.3) gives

$$
\mathfrak D_{SV}(R_n)
\ge
\frac12
\left[
\log g_{SV}(R_n)
\right]_+.
$$

By (5.1),

$$
g_{SV}(R_n)
\to
\lambda_\ast^3>1.
$$

Therefore for sufficiently large

$$
n,
$$

$$
g_{SV}(R_n)>1,
$$

and hence

$$
\liminf_{n\to\infty}
\mathfrak D_{SV}(R_n)
\ge
\frac12
\lim_{n\to\infty}
\log g_{SV}(R_n).
$$

Thus

$$
\liminf_{n\to\infty}
\mathfrak D_{SV}(R_n)
\ge
\frac12
\log(\lambda_\ast^3)
=
\frac32
\log\lambda_\ast.
$$

Since

$$
\lambda_\ast>1,
$$

the lower bound is strictly positive.

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

# 6. Why this removes the old high-derivative transfer requirement

DCRP-03 considered proving directly that

$$
\mathcal M_{SV}^{\log}(D_\ast)
\le
\liminf_n
\mathcal M_{SV}^{\log}(D_n)
$$

from convergence of

$$
Q_n
$$

and

$$
\Delta S_n.
$$

Theorem 5.1 shows that this is unnecessary for the fixed-scale return contradiction.

It is enough that the return compactification retain:

$$
\boxed{
(\lambda_n,g_{SV,n})
}
$$

and that at the fixed-point limit,

$$
\boxed{
g_{SV,n}
\to
\lambda_\ast^3.
}
$$

Thus the difficult infinite-dimensional transfer problem

$$
(Q_n,\Delta S_n)
\longrightarrow
(Q_\ast,\Delta S_\ast)
$$

is replaced by the scalar compatibility problem

$$
\boxed{
g_{SV,n}
\longrightarrow
\lambda_\ast^3.
}
$$

This is a strict frontier reduction.

---

# 7. Defect-completed return package

MORP-02 already uses defect completion rather than discarding noncompact coordinates.

Apply the same principle to the return transition.

Augment a normalized return package by the scalar transition metadata

$$
\boxed{
\mathfrak r
=
(
\lambda,
g_{SV}
).
}
\tag{7.1}
$$

More explicitly:

$$
\boxed{
D^{ret}
=
\left(
D_{\rm in},
D_{\rm out},
\lambda,
g_{SV},
\mathcal R^{tr}
\right).
}
\tag{7.2}
$$

The new coordinates are not observation detectors.

They record:

- the geometric re-root factor;
- the actual strain-$\dot H^1$ endpoint gain.

A compactification may retain

$$
\lambda
$$

and

$$
g_{SV}
$$

as extended nonnegative scalars.

If

$$
g_{SV}
$$

does not converge to the scaling-compatible value

$$
\lambda^3,
$$

the mismatch is not hidden.

Define the scale-gain compatibility defect

$$
\boxed{
\delta_{SG}
=
\left|
\log g_{SV}
-
3\log\lambda
\right|
}
\tag{7.3}
$$

whenever both quantities are finite and positive.

For an exact parabolic scale return,

$$
\boxed{
\delta_{SG}=0.
}
\tag{7.4}
$$

---

# 8. Theorem — Relaxed log-debt lower bound

The previous theorem can be expressed without any high-derivative topology.

Let

$$
\mathscr A
$$

denote the set of actual finite-$\dot H^1$ return packages.

Let

$$
\mathfrak T
$$

be any sequential package topology for which the scale coordinate

$$
\lambda
$$

and scalar gain coordinate

$$
g_{SV}
$$

are continuous.

Define the sequential relaxed log-debt by

$$
\boxed{
\overline{\mathfrak D}_{SV}(D)
=
\inf
\left\{
\liminf_{n\to\infty}
\mathfrak D_{SV}(R_n)
:
R_n\in\mathscr A,
\ 
R_n\to D
\right\},
}
\tag{8.1}
$$

with the convention that the infimum over an empty approximation class is

$$
+\infty.
$$

## Theorem 8.1

Suppose

$$
D
$$

belongs to the sequential closure of

$$
\mathscr A
$$

and satisfies

$$
\boxed{
g_{SV}(D)=\lambda(D)^3
}
\tag{8.2}
$$

with

$$
\lambda(D)>1.
$$

Then

$$
\boxed{
\overline{\mathfrak D}_{SV}(D)
\ge
\frac32
\log\lambda(D)
>
0.
}
\tag{8.3}
$$

### Proof

Take any approximating actual-return sequence

$$
R_n\to D.
$$

Continuity of the scalar coordinates gives

$$
\lambda(R_n)\to\lambda(D)
$$

and

$$
g_{SV}(R_n)\to g_{SV}(D)=\lambda(D)^3.
$$

Theorem 5.1 therefore gives

$$
\liminf_n
\mathfrak D_{SV}(R_n)
\ge
\frac32\log\lambda(D).
$$

This lower bound holds for every admissible approximating sequence.

Taking the infimum over all such sequences proves (8.3).

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

# 9. Kernel-on-the-scale-boundary theorem

Theorem 8.1 immediately gives:

## Corollary 9.1

On the scale-compatible finite-$\dot H^1$ return closure,

$$
\boxed{
\ker
\overline{\mathfrak D}_{SV}
\subseteq
\{
\lambda=1
\}.
}
\tag{9.1}
$$

More precisely, if

$$
\delta_{SG}=0
$$

and

$$
\lambda>1,
$$

then

$$
\overline{\mathfrak D}_{SV}>0.
$$

Therefore a zero relaxed log-debt recurrent profile can survive only by at least one of:

$$
\boxed{
\begin{aligned}
&\lambda\to1,\\
&\delta_{SG}>0,\\
&\text{finite-}\dot H^1\text{ failure},\\
&\text{failure of approximation by actual returns}.
\end{aligned}
}
\tag{9.2}
$$

This is not a new obstruction taxonomy.

It is the exact boundary of the theorem.

---

# 10. Uniform scale-gap corollary

Assume the return rule has a fixed logarithmic scale separation:

$$
\boxed{
\lambda
\ge
\lambda_0
>
1.
}
\tag{10.1}
$$

Then every scale-compatible element of the actual-return closure satisfies

$$
\boxed{
\overline{\mathfrak D}_{SV}
\ge
\frac32
\log\lambda_0
=
c_0
>
0.
}
\tag{10.2}
$$

Thus the zero-cost kernel is empty on that return class.

Schematically:

$$
\boxed{
\text{fixed scale gap}
+
\text{actual-return closure}
+
\text{gain compatibility}
\Longrightarrow
\text{positive model-cone gap}.
}
\tag{10.3}
$$

This is stronger than a non-summability statement.

It is a one-return coercive gap.

---

# 11. Consequence for MORP minimal return rigidity

MORP-03 proves abstractly:

if

$$
D_\ast
$$

is a minimal recurrent obstruction and the nonnegative return depletion ledger holds, then

$$
\boxed{
\Delta_{\rm ret}(D_\ast)=0.
}
\tag{11.1}
$$

MORP-01 also places a zero-cost minimizer in the model-cone kernel.

The present round provides a canonical scalar-completed realization of the state-visible scale-return part of that kernel.

If the recurrent minimizer is approximable by actual finite-$\dot H^1$ returns and satisfies

$$
\delta_{SG}=0,
$$

then any fixed scale factor

$$
\lambda_\ast>1
$$

forces

$$
\boxed{
\overline{\mathfrak D}_{SV}(D_\ast)
\ge
\frac32\log\lambda_\ast
>
0.
}
\tag{11.2}
$$

Therefore:

$$
\boxed{
\textbf{
a zero-cost minimal recurrent state-visible obstruction cannot be a
scale-compatible finite-$\dot H^1$ fixed return with }\lambda_\ast>1.
}
}
\tag{11.3}
$$

This closes the fixed-factor state-visible return branch subject only to the already explicit actual-return / gain-compatibility hypotheses.

---

# 12. What remains of the former Log-Cone Transfer Lemma

The old target required:

$$
Q_n\to Q_\ast
$$

and

$$
\Delta S_n\to\Delta S_\ast
$$

strongly enough to pass the full integral debt.

That target is now demoted.

For fixed-point exclusion it is enough to prove:

$$
\boxed{
\textbf{Scalar Gain Compatibility Lemma}.
}
$$

Desired form:

Let

$$
D_n^{ret}\to D_\ast^{ret}
$$

be a MORP recurrent return sequence converging to a state-visible fixed point with scale factor

$$
\lambda_\ast>1.
$$

Prove either

$$
\boxed{
g_{SV,n}\to\lambda_\ast^3
}
\tag{12.1}
$$

or else retain a nonzero transition defect

$$
\boxed{
\liminf_n
\delta_{SG,n}
>
0.
}
\tag{12.2}
$$

The second alternative is already a failure of exact transition closure and should remain visible in

$$
\mathsf R_{\rm nat}.
$$

Thus the bridge has become scalar.

---

# 13. A compatibility residual that cannot silently disappear

Define

$$
\boxed{
\mathsf R_{SG}(D^{ret})
=
\min
\left\{
1,
\left|
\log g_{SV}
-
3\log\lambda
\right|
\right\}.
}
\tag{13.1}
$$

Then:

$$
\mathsf R_{SG}\ge0,
$$

and exact scale compatibility implies

$$
\mathsf R_{SG}=0.
$$

If the return package topology retains

$$
(\lambda,g_{SV}),
$$

then

$$
\mathsf R_{SG}
$$

is continuous wherever both scalars stay in a compact positive interval.

Therefore a zero-native-residual minimizer satisfying

$$
\mathsf R_{\rm nat}=0
$$

may be refined so that

$$
\boxed{
\mathsf R_{SG}=0.
}
\tag{13.2}
$$

Under this refinement,

$$
\boxed{
g_{SV}=\lambda^3.
}
\tag{13.3}
$$

Thus the exact high-derivative state relation need not be used merely to recover the scalar scaling law.

The cost of losing that law is itself retained as transition residual.

This is consistent with the existing MORP defect-completion principle.

Status:

$$
\boxed{
\textbf{ARCHITECTURAL REFINEMENT; not yet an unconditional NS theorem}.
}
$$

---

# 14. Infinitesimal-return boundary

Corollary 9.1 shows that if a zero-cost recurrent minimizing sequence survives while the scalar gain defect vanishes, then necessarily

$$
\boxed{
\lambda_n\to1.
}
\tag{14.1}
$$

Write the self-similar time period

$$
\boxed{
\mathcal T_n
=
2\log\lambda_n.
}
\tag{14.2}
$$

Then

$$
\lambda_n\to1
$$

is equivalent to

$$
\boxed{
\mathcal T_n\to0.
}
\tag{14.3}
$$

Therefore the only scale-compatible zero-debt boundary is an infinitesimal-period renormalization regime.

This is a substantially sharper normal form than generic diffuse recurrence.

---

# 15. External Liouville cut for small-period DSS

A 2026 primary source by Pineau and Vicol records the following existing result of Chae--Wolf for backwards globally discretely self-similar Navier--Stokes solutions.

For every Type-I constant

$$
C_{U,0}>0,
$$

there exists

$$
\lambda_\ast(C_{U,0})>1
$$

such that a smooth backwards globally

$$
\lambda\text{-DSS}
$$

solution satisfying the corresponding Type-I upper bound is trivial whenever

$$
\boxed{
1<\lambda<\lambda_\ast(C_{U,0}).
}
\tag{15.1}
$$

Thus an actual non-rotated Type-I DSS realization cannot survive the infinitesimal-return boundary

$$
\lambda\to1.
$$

In the rotated discretely self-similar setting, Pineau--Vicol prove analogous triviality when the angular speed is sufficiently small or sufficiently large and the discrete period is sufficiently small relative to the stated parameter regime.

These external theorems do not exclude the full MORP branch because:

- the MORP recurrent object need not yet be an actual global DSS/RDSS solution;
- Type-I control must be established;
- rotated intermediate-angular-speed regimes are not all covered.

Nevertheless, the small-period boundary is not an unconstrained new object.

Large parts of it are already externally Liouville-excluded once actual Type-I DSS/RDSS realization is obtained.

---

# 16. Fixed scale gap versus infinitesimal period

The state-visible recurrent branch is now divided by a theorem, not by a new detector.

### Case A — nondegenerate scale gap

There exists

$$
\lambda_0>1
$$

such that along the recurrent subsequence

$$
\lambda_n\ge\lambda_0.
$$

If scalar gain compatibility holds, then

$$
\boxed{
\overline{\mathfrak D}_{SV}
\ge
\frac32
\log\lambda_0>0.
}
$$

Hence zero model-cone cost is impossible.

### Case B — vanishing scale gap

$$
\lambda_n\to1.
$$

Then

$$
\mathcal T_n=2\log\lambda_n\to0.
$$

Any exact Type-I DSS realization is eventually inside the known small-period Liouville regime and hence trivial.

Thus a surviving zero-cost minimal obstruction in Case B must still fail at least one of:

$$
\boxed{
\text{actual DSS realization},
\qquad
\text{Type-I transfer},
\qquad
\text{unrotated/extreme-rotation Liouville hypotheses}.
}
\tag{16.1}
$$

The scale variable itself is no longer a free escape route.

---

# 17. A conditional closure theorem for the Type-I non-rotated recurrent branch

## Theorem 17.1

Assume a hypothetical singular MORP minimal obstruction produces a sequence of state-visible recurrent return packages

$$
R_n
$$

satisfying:

1. each return is approximable by an actual finite-$\dot H^1$ return;

2. the scale-gain residual vanishes:

$$
\delta_{SG,n}\to0;
$$

3. the model-cone channel is the relaxed log-debt channel, or dominates it on the recurrent class;

4. the limiting recurrent branch is Type-I and non-rotated;

5. profile recurrence upgrades to an actual backwards globally DSS state whenever

$$
\lambda_n\to1.
$$

Then the branch is impossible.

### Proof

There are two cases.

#### Case A

There exists

$$
\lambda_0>1
$$

and a subsequence with

$$
\lambda_n\ge\lambda_0.
$$

By Theorem 8.1 / Corollary 10.1,

$$
\overline{\mathfrak D}_{SV}
\ge
\frac32\log\lambda_0>0,
$$

contradicting zero model-cone cost.

#### Case B

No such scale gap exists.

Then after a subsequence,

$$
\lambda_n\to1.
$$

By assumption 5, the recurrent branch upgrades to an actual Type-I DSS state with a sufficiently small discrete similarity factor.

The Chae--Wolf small-factor Liouville theorem, as restated in Pineau--Vicol Theorem 1.6, gives

$$
U\equiv0.
$$

This contradicts the nontrivial singular obstruction.

Hence both cases are impossible.

$$
\square
$$

Status:

$$
\boxed{
\textbf{CONDITIONAL on the stated actual-realization / Type-I hypotheses}.
}
$$

The importance is that once those pre-existing MORP bridges are supplied, there is no residual scale-factor loophole in the non-rotated Type-I branch.

---

# 18. New strongest internal conclusion

The scalar gain construction gives the following robust statement:

$$
\boxed{
\begin{aligned}
&\text{zero model-cone recurrent cost}\\
&+
\text{actual-return approximability}\\
&+
\text{scale-gain compatibility}
\end{aligned}
}
$$

forces the recurrent scale factor onto the boundary

$$
\boxed{
\lambda=1.
}
\tag{18.1}
$$

Equivalently:

$$
\boxed{
\textbf{
every nontrivial scale-changing recurrent return with }\lambda>1
\textbf{ carries strictly positive relaxed logarithmic cone debt.}
}
\tag{18.2}
$$

This conclusion survives compactification using only two scalar return coordinates.

The full high-derivative cone functional need not pass strongly through the compactness limit.

---

# 19. Updated frontier

The former target

$$
\text{Log-Cone Transfer Lemma}
$$

has been reduced to two sharply separated obligations.

## Frontier A — Scalar Gain Compatibility

Prove from the existing MORP actual-return / residual package that

$$
\boxed{
\mathsf R_{\rm nat}=0
\Longrightarrow
\delta_{SG}=0.
}
\tag{19.1}
$$

Because

$$
\delta_{SG}
$$

is scalar and can be retained explicitly, this is substantially easier than high-derivative functional convergence.

## Frontier B — Infinitesimal Return Realization

If a zero-cost minimizing sequence has

$$
\lambda_n\to1,
$$

prove that the recurrent profile either:

$$
\boxed{
\text{upgrades to an actual small-period DSS/RDSS object}
}
\tag{19.2}
$$

or pays a nonzero shadowing / transition residual.

The non-rotated Type-I actual DSS subcase is already externally excluded for sufficiently small

$$
\lambda-1.
$$

---

# 20. Next exact attack

The next proof round should not return to

$$
Q_n,\Delta S_n
$$

strong convergence.

Instead attack:

$$
\boxed{
\textbf{
Zero Residual}
\Longrightarrow
\textbf{
Scalar Scale-Gain Compatibility}.
}
$$

More concretely:

Given an actual return / re-root package with normalization

$$
\mathsf N_{\rm norm},
$$

write the exact transformation law of

$$
H=\|S\|_{\dot H^1}^2
$$

under every declared normalization component:

- translation;
- rotation;
- parabolic scaling;
- time re-root;
- any amplitude/reference-shell normalization.

Translation and rotation preserve

$$
H.
$$

Parabolic scaling contributes exactly

$$
3\log\lambda
$$

to

$$
\log H.
$$

Therefore any discrepancy

$$
\boxed{
\log g_{SV}-3\log\lambda
}
$$

must come from a declared non-symmetry normalization or from failure of actual return realization.

If the current MORP normalization contains no additional amplitude renormalization acting on the physical state component, then

$$
\boxed{
\delta_{SG}=0
}
$$

is automatic for an exact actual fixed return.

If such an extra normalization is present, its contribution must be explicitly isolated as a transition residual.

This is the next point to audit in the original normalization compiler.

---

# 21. Source ledger

## Internal

- `NS_MORP_02_NativeExtraction_Compactness_v0.1.md`
  - defect-completed package principle;
  - selected trace and scale-escape completion.

- `NS_MORP_03_Transition_Profile_RigidityEntry_v0.1.md`
  - actual versus profile return distinction;
  - return/re-root normalization;
  - minimal return rigidity;
  - conditional fixed-factor discrete renormalization state.

- `NS_MORP_04_EqualityManifold_RigidityAudit_v0.1.md`
  - Miller model-cone equality branch.

- `NS_DCRP_03_LogCone_Debt_ScaleReturn_2026-08-16.md`
  - exact logarithmic cone-growth inequality;
  - scale-invariant log-cone debt;
  - scale-return lower bound.

## External primary sources

### Evan Miller

Evan Miller, *On the interaction of strain and vorticity for solutions of the Navier--Stokes equation*, arXiv:2407.02691v2, revised 2026-04-13.

Used for:

$$
\left<
-\Delta S,
\omega\otimes\omega
\right>
=
0,
$$

the exact strain equation, the exact strain-$\dot H^1$ balance, and model-cone regularity calibration.

### Pineau--Vicol

Ben Pineau and Vlad Vicol, *On rotated backwards self-similar solutions of the incompressible 3D Navier-Stokes equations*, arXiv:2607.09619v1, 2026-07-10.

Used only as external calibration for:

- the relation
  $$
  \mathcal T=2\log\lambda
  $$
  between self-similar period and DSS factor;
- the restatement of the Chae--Wolf small-factor Type-I DSS Liouville theorem;
- the 2026 Type-I RDSS exclusions in small/large angular-speed regimes with sufficiently small period.

No unconditional general DSS/RDSS exclusion is claimed.

---

# 22. End state

The main transfer obstacle has changed.

We no longer need to prove lower semicontinuity of the entire nonlinear high-derivative integral

$$
\mathfrak D_{SV}.
$$

It is enough to retain the scalar endpoint gain

$$
g_{SV}
$$

and scale factor

$$
\lambda.
$$

The rigorous transfer statement is

$$
\boxed{
g_{SV,n}\to\lambda_\ast^3,
\quad
\lambda_\ast>1
\Longrightarrow
\liminf_n
\mathfrak D_{SV}(R_n)
\ge
\frac32\log\lambda_\ast.
}
$$

The relaxed zero-debt kernel therefore lies on

$$
\boxed{
\lambda=1
}
$$

unless scale-gain compatibility or actual-return realization fails.

The next exact target is:

$$
\boxed{
\textbf{
audit the MORP normalization compiler and prove
Zero Native Residual}
\Longrightarrow
\textbf{
Scale-Gain Compatibility}.
}
$$

That is now a finite transformation-law problem rather than an infinite-dimensional compactness problem.