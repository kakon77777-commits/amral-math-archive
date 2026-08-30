# NS-DCRP-24 — Increment Young-Profile Fiber Completion, Actual-Increment Covariance Rigidity, and the Pressure-Compatible Kernel

- date: 2026-08-17
- status: research proof checkpoint
- canonical source: UTF-8 Markdown
- canonical math delimiters: `$...$` and `$$...$$`
- objective:
  1. audit the role of the derivative-compatible increment defect inside the MORP extended cost;
  2. correct the interpretation of the DCRP-23 Young-profile frontier;
  3. complete the external cylindrical Young-profile theorem by identifying the missing infinite-dimensional fiber-escape defect;
  4. prove a rigidity theorem for the covariance of an actual resolved velocity-increment field;
  5. identify the genuine strong-profile kernel that can remain dynamically silent at coarse vorticity level.
- no full Navier--Stokes regularity claim is made.
- principal external primary source:
  - Runlong Yu, *Filtered Vortex Stretching and Subgrid Defects for the Three-Dimensional Navier--Stokes Equations*, arXiv:2606.27560v1.
- principal internal source:
  - `NS_MORP_01_MinimalObstruction_Rigidity_v0.1.md`.
- internal dependencies:
  - DCRP-18 through DCRP-23.
- no novelty/priority claim is made without independent audit.

---

# 1. Executive result

The first result of this round is a **consistency correction**.

MORP-01 already defines the extended obstruction cost by:

$$
\boxed{
\mathfrak J(D)
=
\mathsf O_{\rm PFET}(D)
+
\mathcal M_{SV}(D)
+
\widetilde{\mathcal S}^{(3)}(D)
+
\mathsf{Paid}(D)
+
\mathsf R_{\rm nat}(D).
}
\tag{1.1}
$$

Thus the minimal-invisible branch:

$$
\mathfrak J(D_\ast)=0
$$

already requires:

$$
\boxed{
\widetilde{\mathcal S}^{(3)}(D_\ast)=0.
}
\tag{1.2}
$$

DCRP-23 proves, on a persistent non-CKN branch with fixed relative filter ratio and bounded normalized local reservoirs:

$$
\boxed{
\widetilde{\mathcal S}^{(3)}_k
\ge
s_\ast(M_0)
>
0
\qquad
\forall k\gg1.
}
\tag{1.3}
$$

Therefore, provided the DCRP-23 increment observable is identified with the same fixed-filter/cutoff coordinate used in MORP-01:

$$
\boxed{
\textbf{
bounded-reservoir persistent non-CKN}
\cap
\textbf{
exact MORP zero-cost}
=
\varnothing.
}
}
\tag{1.4}
$$

This means the Young-profile analysis is **not needed merely to exclude the exact zero-cost bounded-reservoir branch**.

However this does **not** prove regularity.

A positive scale-critical increment cost may persist at every scale without automatically becoming a positive depletion tax.

The global proof still has to understand whether such persistent roughness:

- performs positive recurrent commutator work;
- is dynamically pressure-compatible and harmless;
- escapes through a noncompact profile direction;
- or forces another paid/native mechanism.

The second major result concerns the compactness theorem used for this persistent positive-cost branch.

The external filtered-vorticity paper proves only a **cylindrical** generalized Young profile unconditionally.

It explicitly does **not** obtain a full generalized Young representation of:

$$
\|\Xi\|_{E_\sigma^\sharp}^{4}
$$

or the covariance map without an additional hypothesis.

DCRP-24 identifies the missing compactness coordinate.

Let:

$$
E_\sigma^\sharp
=
L^3(d\nu_\sigma;\mathbb R^3)
\times
L^3(d\mu_\sigma;\mathbb R^3).
$$

Choose finite-rank conditional-expectation projections:

$$
P_N:E_\sigma^\sharp\to E_\sigma^\sharp
$$

with:

$$
\boxed{
\sup_N\|P_N\|<\infty,
\qquad
P_N\Xi\to\Xi
\quad
\forall\Xi\in E_\sigma^\sharp.
}
\tag{1.5}
$$

For normalized increment fields:

$$
V_n^\sharp,
$$

define the fiber-tail cost:

$$
\boxed{
\mathfrak F_{\rm fib}
=
\inf_N
\limsup_{n\to\infty}
\sigma^{-2}
\iint
\chi
\|
(I-P_N)V_n^\sharp
\|_{E_\sigma^\sharp}^{4}
dxdt.
}
\tag{1.6}
$$

Then:

### fiber-escape branch

$$
\boxed{
\mathfrak F_{\rm fib}>0
}
\tag{1.7}
$$

is a genuine infinite-dimensional increment-fiber defect.

### fiber-tight branch

If:

$$
\boxed{
\mathfrak F_{\rm fib}=0,
}
\tag{1.8}
$$

then the cylindrical Young profile is sufficient to represent:

- the full quartic norm;
- the quadratic Reynolds covariance map;

because both are uniformly approximable by the finite-rank projected functionals.

Thus the external paper's additional **full-representation hypothesis** can be replaced, for the present program, by the explicit alternative:

$$
\boxed{
\textbf{
fiber escape}
\ \vee\
\textbf{
full increment representation}.
}
}
\tag{1.9}
$$

This turns a hidden compactness assumption into a native defect channel.

The third major result is an **actual-increment covariance rigidity theorem**.

Let:

$$
\varphi_\sigma>0
$$

almost everywhere on its open support ball and define the actual coarse covariance:

$$
\boxed{
R_\sigma[u]
=
\int
\varphi_\sigma(z)
\delta_zu\otimes\delta_zu\,dz
-
\left(
\int
\varphi_\sigma(z)
\delta_zu\,dz
\right)^{\otimes2}.
}
\tag{1.10}
$$

Then:

$$
\boxed{
R_\sigma[u]=0
\text{ a.e. on a connected interior region}
\Longrightarrow
\delta_zu=0
\text{ locally for a.e. }z.
}
\tag{1.11}
$$

Consequently:

$$
\boxed{
\widetilde{\mathcal S}^{(3)}[u]>0
\Longrightarrow
R_\sigma[u]\neq0
\text{ on a set of positive measure},
}
\tag{1.12}
$$

for every actual resolved increment field.

Thus a nonzero **strong/resolved** increment profile cannot hide behind zero actual covariance.

However one more important NO-GO remains.

A nonzero covariance need not create coarse vorticity forcing.

Define the pressure-compatible covariance kernel:

$$
\boxed{
\mathcal K_{\rm pc}
=
\left\{
R=R^T:
\nabla\times\nabla\cdot R=0
\right\}.
}
\tag{1.13}
$$

On a simply connected core:

$$
R\in\mathcal K_{\rm pc}
$$

implies:

$$
\boxed{
\nabla\cdot R=\nabla q
}
\tag{1.14}
$$

for some scalar:

$$
q.
$$

Hence:

- the filtered-vorticity commutator forcing vanishes;
- the momentum effect is absorbed into pressure;
- the coarse stress work is only a divergence:

$$
\boxed{
-R:\nabla U
=
\nabla\cdot
(
qU-RU
).
}
\tag{1.15}
$$

Therefore:

$$
\boxed{
\textbf{
nonzero increment covariance}
\not\Rightarrow
\textbf{
positive bulk commutator work}.
}
}
\tag{1.16}
$$

A concrete local affine example proves this is not merely formal.

Thus the correct next frontier is:

$$
\boxed{
\textbf{
Increment Work-Efficiency / Pressure-Compatible Covariance Rigidity Lemma}.
}
\tag{1.17}
$$

The remaining bounded-reservoir positive-cost survivor is no longer "an arbitrary Young profile."

It is one of:

1. infinite-dimensional fiber escape;
2. genuine Young oscillation/concentration;
3. a resolved nonzero covariance producing actual commutator work;
4. a pressure-compatible covariance profile whose coarse effect is only pressure/boundary transport.

The fourth branch is the genuinely new strong-profile kernel.

---

# 2. MORP cost consistency audit

MORP-01 defines the unit obstruction slice:

$$
\boxed{
\mathscr O_1
=
\left\{
D:
d_{\rm nat}(D)\ge1,
\quad
\mathcal N_{\rm pkg}(D)\le C_\ast
\right\}.
}
\tag{2.1}
$$

It then defines the nonnegative candidate channels:

$$
\mathsf O_{\rm PFET},
$$

$$
\mathcal M_{SV},
$$

$$
\widetilde{\mathcal S}^{(3)},
$$

$$
\mathsf{Paid},
$$

and:

$$
\mathsf R_{\rm nat}.
$$

The exact extended cost is (1.1).

Therefore:

$$
\boxed{
\mathfrak J(D)=0
\Longrightarrow
\widetilde{\mathcal S}^{(3)}(D)=0.
}
\tag{2.2}
$$

Status:

$$
\boxed{
\textbf{INTERNAL DEFINITION, AUDITED}.
}
$$

---

# 3. DCRP-23 versus the zero-cost bounded-reservoir branch

DCRP-23 proves:

if an admissible nested branch remains non-CKN and:

$$
\boxed{
A_{k,\sigma}^{+}
+
D_k
\le
M_0
}
\tag{3.1}
$$

uniformly, then:

$$
\boxed{
\widetilde{\mathcal S}_k^{(3)}
\ge
s_\ast(M_0)
>
0
}
\tag{3.2}
$$

for every sufficiently large:

$$
k.
$$

Suppose the MORP zero-cost sequence uses the same:

- fixed relative filter:

  $$
  \ell_k=\sigma r_k;
  $$

- derivative-compatible kernel pair:

  $$
  d\nu_\sigma,
  \qquad
  d\mu_\sigma;
  $$

- normalized cutoff family.

Then:

$$
\boxed{
\text{bounded reservoir}
+
\text{persistent non-CKN}
\Longrightarrow
\mathfrak J
\ge
s_\ast
}
\tag{3.3}
$$

on all sufficiently late actual windows.

Thus:

$$
\boxed{
\textbf{
the exact zero-cost bounded-reservoir branch is excluded.
}
}
\tag{3.4}
$$

Status:

$$
\boxed{
\textbf{PROVED conditional only on coordinate identification}.
}
$$

The coordinate identification is a finite compiler issue, not a new PDE estimate.

---

# 4. Why this does not finish regularity

The conclusion:

$$
\mathfrak J\ge s_\ast>0
$$

is a **normalized positive gap**.

It does not imply:

$$
\boxed{
\sum_k
\text{physical raw payment}_k
=
+\infty.
}
$$

The old critical-barrier issue remains:

a scale-invariant positive amount may correspond to geometrically shrinking physical energy.

Also:

$$
\widetilde{\mathcal S}^{(3)}
$$

controls the size of derivative-compatible velocity increments.

In the filtered-vorticity equation it appears as an upper bound for differentiated commutator forcing.

It is not itself a signed negative term.

Therefore:

$$
\boxed{
\textbf{
positive increment cost}
\neq
\textbf{
positive irreversible depletion}.
}
}
\tag{4.1}
$$

The profile analysis is needed to determine what persistent positive increment cost actually does dynamically.

---

# 5. External cylindrical Young theorem audited

At unit scale the external paper defines:

$$
\boxed{
E_\sigma^\sharp
=
L^3(B_{c_\varphi\sigma},d\nu_\sigma;\mathbb R^3)
\times
L^3(B_{c_\varphi\sigma},d\mu_\sigma;\mathbb R^3).
}
\tag{5.1}
$$

For normalized states:

$$
u^{(n)},
$$

the derivative-compatible increment field is:

$$
\boxed{
V_n^\sharp(x,t)(z)
=
\left(
\delta_zu^{(n)}(x,t),
\delta_zu^{(n)}(x,t)
\right).
}
\tag{5.2}
$$

The critical defect is:

$$
\boxed{
\widetilde{\mathcal S}_n^{(3)}
=
\sigma^{-2}
\iint
\chi
\|
V_n^\sharp
\|_{E_\sigma^\sharp}^{4}
dxdt.
}
\tag{5.3}
$$

A uniform bound yields a **cylindrical** generalized Young profile.

This means every finite collection of continuous linear functionals on:

$$
E_\sigma^\sharp
$$

has a consistent finite-dimensional generalized Young limit.

The theorem does **not** unconditionally represent:

$$
\|
\Xi
\|_{E_\sigma^\sharp}^{4}
$$

or the covariance map.

Status:

$$
\boxed{
\textbf{EXTERNAL PRIMARY THEOREM}.
}
$$

---

# 6. Why cylindrical compactness is insufficient

Let:

$$
E
$$

be an infinite-dimensional Banach space.

A sequence can satisfy:

$$
\|v_n\|_E=1
$$

while every fixed finite-dimensional projection converges to zero.

The model is an orthonormal/basis sequence.

Thus:

$$
\boxed{
\text{all cylindrical projections tight}
\not\Rightarrow
\text{norm-topology tightness}.
}
\tag{6.1}
$$

The external paper correctly states this as the reason full covariance/norm representation requires an additional assumption.

For the DCRP program this missing mass must not be silently ignored.

It becomes a defect coordinate.

---

# 7. Finite-rank approximation on the increment fiber

Both probability spaces:

$$
(B_{c_\varphi\sigma},\nu_\sigma),
\qquad
(B_{c_\varphi\sigma},\mu_\sigma)
$$

are finite measure spaces.

Choose increasing finite measurable partitions:

$$
\mathcal P_N^\nu,
\qquad
\mathcal P_N^\mu
$$

whose generated sigma-algebras are dense in the respective Borel sigma-algebras.

Let:

$$
P_N^\nu
$$

and:

$$
P_N^\mu
$$

be conditional expectation onto the corresponding partition.

Then:

$$
\boxed{
\|P_N^\nu\|_{L^3\to L^3}
\le1,
\qquad
\|P_N^\mu\|_{L^3\to L^3}
\le1.
}
\tag{7.1}
$$

Each operator has finite rank and:

$$
\boxed{
P_N^\nu f\to f
\quad
\text{in }L^3(d\nu_\sigma),
}
\tag{7.2}
$$

$$
\boxed{
P_N^\mu g\to g
\quad
\text{in }L^3(d\mu_\sigma).
}
\tag{7.3}
$$

Define:

$$
\boxed{
P_N
=
P_N^\nu
\oplus
P_N^\mu
:
E_\sigma^\sharp
\to
E_\sigma^\sharp.
}
\tag{7.4}
$$

Then:

$$
\boxed{
\sup_N
\|P_N\|
\le1,
\qquad
P_N\Xi\to\Xi
\quad
\forall\Xi\in E_\sigma^\sharp.
}
\tag{7.5}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 8. Fiber-tail defect

Define:

$$
\boxed{
\mathcal F_N
=
\limsup_{n\to\infty}
\sigma^{-2}
\iint
\chi
\|
(I-P_N)V_n^\sharp
\|_{E_\sigma^\sharp}^{4}
dxdt.
}
\tag{8.1}
$$

Define the infinite-dimensional fiber-escape amount:

$$
\boxed{
\mathfrak F_{\rm fib}
=
\inf_{N\ge1}
\mathcal F_N.
}
\tag{8.2}
$$

Then:

### fiber-tight

$$
\boxed{
\mathfrak F_{\rm fib}=0;
}
\tag{8.3}
$$

### fiber escape

$$
\boxed{
\mathfrak F_{\rm fib}>0.
}
\tag{8.4}
$$

The second case means a fixed portion of the critical increment mass escapes every finite-dimensional resolution of the increment variable:

$$
z.
$$

This is a native noncompactness defect.

It is independent of:

- physical-space escape;
- relative-frequency escape;
- temporal concentration.

---

# 9. NEW THEOREM — Fiber-Tight Upgrade of Cylindrical Representation

## Theorem 9.1

Assume:

$$
\boxed{
\sup_n
\widetilde{\mathcal S}_n^{(3)}
<
\infty,
}
\tag{9.1}
$$

and:

$$
\boxed{
\mathfrak F_{\rm fib}=0.
}
\tag{9.2}
$$

Then, after a subsequence, the cylindrical Young profile determines the limits of:

1. the full quartic increment functional:

   $$
   \boxed{
   G(\Xi)
   =
   \|
   \Xi
   \|_{E_\sigma^\sharp}^{4};
   }
   \tag{9.3}
   $$

2. the quadratic Reynolds covariance functional:

   $$
   \boxed{
   \mathcal C(\Xi).
   }
   \tag{9.4}
   $$

In particular, the "full representation" consequences used in the external paper become available on the fiber-tight branch.

### Proof

For the quartic functional, use:

$$
\left|
\|X\|^4-\|Y\|^4
\right|
\le
4
\left(
\|X\|+\|Y\|
\right)^3
\|X-Y\|.
$$

Set:

$$
Y=P_NX.
$$

Since:

$$
\|P_NX\|\le\|X\|,
$$

$$
\left|
\|X\|^4-\|P_NX\|^4
\right|
\le
32
\|X\|^3
\|
(I-P_N)X
\|.
$$

Integrating and applying Holder:

$$
\boxed{
\iint
\chi
\left|
\|V_n^\sharp\|^4
-
\|P_NV_n^\sharp\|^4
\right|
\le
C
\left(
\iint
\chi
\|V_n^\sharp\|^4
\right)^{3/4}
\left(
\iint
\chi
\|(I-P_N)V_n^\sharp\|^4
\right)^{1/4}.
}
\tag{9.5}
$$

The first factor is uniformly bounded.

Fiber tightness makes the second uniformly small after choosing:

$$
N
$$

large.

For fixed:

$$
N,
$$

the functional:

$$
\|P_N\Xi\|^4
$$

depends only on finitely many coordinates and is represented by the cylindrical generalized Young profile.

Pass:

$$
n\to\infty
$$

first and then:

$$
N\to\infty.
$$

For the covariance map, using the probability character of:

$$
d\nu_\sigma,
$$

one has:

$$
\boxed{
|
\mathcal C(X)
-
\mathcal C(Y)
|
\le
C
\left(
\|X\|_E+\|Y\|_E
\right)
\|X-Y\|_E.
}
\tag{9.6}
$$

Therefore:

$$
\boxed{
\|
\mathcal C(V_n^\sharp)
-
\mathcal C(P_NV_n^\sharp)
\|_{L^2(Q)}
\le
C
\|
V_n^\sharp
\|_{L^4(Q;E)}
\|
(I-P_N)V_n^\sharp
\|_{L^4(Q;E)}.
}
\tag{9.7}
$$

Again the right side is uniformly small on the fiber-tight branch.

For fixed:

$$
N,
$$

the projected covariance is a continuous finite-dimensional quadratic functional and is represented cylindrically.

Pass:

$$
n\to\infty
$$

and:

$$
N\to\infty.
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

# 10. Compactness alternative for the persistent increment branch

Combining the external cylindrical theorem with Theorem 9.1:

$$
\boxed{
\textbf{
bounded persistent increment defect}
\Longrightarrow
\textbf{
fiber escape}
\ \vee\
\textbf{
full Young/covariance representation}.
}
}
\tag{10.1}
$$

This replaces an external compactness assumption by a completed defect alternative.

The fiber-escape branch should be retained inside:

$$
\mathsf R_{\rm nat}.
$$

---

# 11. Full-profile alternatives

On the full-representation branch the generalized Young profile separates:

- barycentric resolved increments;
- non-Dirac oscillation;
- concentration.

Let:

$$
\mathcal D_\sigma^{(3)}
\ge0
$$

be the quartic Jensen/concentration excess.

Then:

$$
\boxed{
\liminf_n
\widetilde{\mathcal S}^{(3)}_n
\ge
\widetilde{\mathcal S}^{(3)}[u]
+
\mathcal D_\sigma^{(3)}.
}
\tag{11.1}
$$

If:

$$
\mathcal D_\sigma^{(3)}>0,
$$

the increment branch already contains a positive Young oscillation/concentration defect.

Thus the most rigid remaining branch is:

$$
\boxed{
\mathfrak F_{\rm fib}=0,
\qquad
\mathcal D_\sigma^{(3)}=0,
}
\tag{11.2}
$$

with nonzero resolved increment barycenter.

---

# 12. Actual Reynolds covariance identity

For an actual velocity:

$$
u,
$$

define:

$$
\boxed{
m_\sigma(x,t)
=
\int
\varphi_\sigma(z)
\delta_zu(x,t)dz.
}
\tag{12.1}
$$

Then:

$$
\boxed{
R_\sigma[u]
=
\int
\varphi_\sigma(z)
\left(
\delta_zu-m_\sigma
\right)
\otimes
\left(
\delta_zu-m_\sigma
\right)
dz.
}
\tag{12.2}
$$

Thus:

$$
\boxed{
R_\sigma[u]\ge0
}
\tag{12.3}
$$

as a symmetric matrix.

Also:

$$
\boxed{
\operatorname{tr}R_\sigma[u]
=
\int
\varphi_\sigma(z)
|
\delta_zu-m_\sigma
|^2dz.
}
\tag{12.4}
$$

Hence:

$$
\boxed{
R_\sigma[u]=0
\Longleftrightarrow
\delta_zu
=
m_\sigma
\quad
\varphi_\sigma\text{-a.e. }z.
}
\tag{12.5}
$$

---

# 13. NEW THEOREM — Actual-Increment Covariance Rigidity

## Theorem 13.1

Assume:

- the mollifier:

  $$
  \varphi_\sigma
  $$

  is strictly positive almost everywhere on:

  $$
  B_\sigma;
  $$

-:

  $$
  u(\cdot,t)\in L^3_{\rm loc}
  $$

  for almost every:

  $$
  t;
  $$

-:

  $$
  G\subset\mathbb R^3
  $$

  is connected and:

  $$
  \operatorname{dist}
  (
  G,\partial G^+
  )
  >
  \sigma.
  $$

If:

$$
\boxed{
R_\sigma[u](x,t)=0
}
\tag{13.1}
$$

for almost every:

$$
(x,t)\in G^+\times I,
$$

then for almost every:

$$
t\in I,
$$

$$
\boxed{
u(\cdot,t)
\text{ is spatially constant a.e. on }G.
}
\tag{13.2}
$$

Consequently:

$$
\boxed{
\delta_zu=0
}
\tag{13.3}
$$

for almost every admissible:

$$
(x,t,z)
$$

in the inner region, and:

$$
\boxed{
\widetilde{\mathcal S}^{(3)}[u;G]=0.
}
\tag{13.4}
$$

### Proof

If:

$$
R_\sigma[u](x,t)=0,
$$

then (12.4) gives:

$$
\delta_zu(x,t)
=
m_\sigma(x,t)
$$

for:

$$
\varphi_\sigma\text{-a.e. }z.
$$

Because:

$$
\varphi_\sigma>0
$$

a.e. on:

$$
B_\sigma,
$$

the value:

$$
u(x-z,t)
=
u(x,t)+m_\sigma(x,t)
$$

is independent of:

$$
z
$$

for almost every:

$$
z\in B_\sigma.
$$

Therefore:

$$
u(\cdot,t)
$$

is a.e. constant on:

$$
B_\sigma(x).
$$

For almost every pair of nearby points:

$$
x_1,x_2
$$

whose balls overlap, the two constants agree on the overlap.

A chain of overlapping balls connects any two points of:

$$
G,
$$

because:

$$
G
$$

is connected and lies a positive distance inside:

$$
G^+.
$$

Hence:

$$
u(\cdot,t)
$$

is constant a.e. on:

$$
G.
$$

All admissible increments in the inner region vanish.

The derivative-weighted increment component also vanishes because its:

$$
z
$$

support lies in the closure of the same filter ball.

Therefore:

$$
\widetilde{\mathcal S}^{(3)}[u;G]=0.
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

# 14. Corollary — nonzero resolved increment profile has nonzero covariance

Suppose a full/strong resolved profile satisfies:

$$
\boxed{
\widetilde{\mathcal S}^{(3)}[u;G]
>
0.
}
\tag{14.1}
$$

Then Theorem 13.1 implies:

$$
\boxed{
R_\sigma[u]
\neq0
}
\tag{14.2}
$$

on a set of positive spacetime measure.

Thus:

$$
\boxed{
\textbf{
a nonzero actual strong increment profile cannot have identically zero Reynolds covariance.
}
}
\tag{14.3}
$$

This is stronger than the one-way defect statement in the external paper because it uses the special **actual increment structure** of the barycentric profile.

It does **not** say that a zero **stress defect** forces a Dirac Young measure.

Those are different statements.

---

# 15. Covariance defect versus resolved covariance

The external full-profile theorem defines:

$$
\boxed{
D
=
R_\sigma^{YM}
-
R_\sigma[u].
}
\tag{15.1}
$$

It correctly states:

$$
D\neq0
\Longrightarrow
\text{nontrivial microstructure}.
$$

It also correctly warns:

$$
\boxed{
D=0
\not\Longrightarrow
\text{Young profile Dirac}.
}
\tag{15.2}
$$

DCRP-24 does not contradict this.

Theorem 13.1 concerns:

$$
\boxed{
R_\sigma[u]
}
$$

itself, the covariance of the resolved barycentric increment field.

Thus the strong-profile branch may have:

$$
D=0,
$$

while still:

$$
R_\sigma[u]\neq0.
$$

---

# 16. The commutator-force kernel

The coarse vorticity equation sees:

$$
\boxed{
-\nabla\times\nabla\cdot R_\sigma.
}
\tag{16.1}
$$

Therefore define:

$$
\boxed{
\mathcal K_{\rm pc}
=
\left\{
R:
R=R^T,
\quad
\nabla\times\nabla\cdot R=0
\right\}.
}
\tag{16.2}
$$

Call this the **pressure-compatible covariance kernel**.

On a simply connected region:

$$
\nabla\times\nabla\cdot R=0
$$

implies:

$$
\boxed{
\nabla\cdot R
=
\nabla q
}
\tag{16.3}
$$

for a scalar distribution:

$$
q.
$$

Hence the coarse momentum equation sees:

$$
-\nabla\cdot R
=
-\nabla q,
$$

which is absorbed by pressure.

---

# 17. NEW THEOREM — Pressure-Compatible Covariance is Bulk-Work Silent

## Theorem 17.1

Let:

$$
U
$$

be divergence free and let:

$$
R=R^T
$$

satisfy:

$$
\nabla\cdot R=\nabla q.
$$

Then:

$$
\boxed{
-R:\nabla U
=
\nabla\cdot
(
qU-RU
).
}
\tag{17.1}
$$

Consequently:

- on the whole space with sufficient decay:

  $$
  \boxed{
  \int
  R:\nabla U\,dx
  =
  0;
  }
  \tag{17.2}
  $$

- on a local window the stress work is entirely a pressure/boundary localization term.

### Proof

Because:

$$
R
$$

is symmetric,

$$
\nabla\cdot(RU)
=
(\nabla\cdot R)\cdot U
+
R:\nabla U.
$$

Use:

$$
\nabla\cdot R=\nabla q
$$

and:

$$
\nabla\cdot U=0.
$$

Then:

$$
(\nabla q)\cdot U
=
\nabla\cdot(qU).
$$

Therefore:

$$
R:\nabla U
=
\nabla\cdot(RU-qU).
$$

Multiply by:

$$
-1.
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

# 18. NO-GO — nonzero increment defect need not generate commutator work

Consider a local affine divergence-free field:

$$
\boxed{
u(x)
=
Ax,
\qquad
\operatorname{tr}A=0.
}
\tag{18.1}
$$

For a centered radial mollifier:

$$
U_\sigma=u,
$$

and:

$$
\boxed{
\delta_zu
=
-Az.
}
\tag{18.2}
$$

The mean increment is zero:

$$
m_\sigma=0.
$$

The covariance is:

$$
\boxed{
R_\sigma
=
\int
\varphi_\sigma(z)
Az\otimes Az\,dz
=
c_\varphi
\sigma^2
AA^T.
}
\tag{18.3}
$$

This matrix is constant.

Therefore:

$$
\boxed{
\nabla\cdot R_\sigma=0.
}
\tag{18.4}
$$

Hence:

$$
\boxed{
\nabla\times\nabla\cdot R_\sigma=0.
}
\tag{18.5}
$$

But if:

$$
A\neq0,
$$

the increment defect is nonzero.

If:

$$
A
$$

is skew-symmetric, then:

$$
R_\sigma
$$

is symmetric and:

$$
\boxed{
R_\sigma:A=0.
}
\tag{18.6}
$$

Thus the bulk coarse stress work also vanishes.

Therefore:

$$
\boxed{
\textbf{
nonzero derivative-compatible increment defect}
\not\Rightarrow
\textbf{
nonzero commutator forcing or positive stress work}.
}
}
\tag{18.7}
$$

Status:

$$
\boxed{
\textbf{EXACT LOCAL ALGEBRAIC NO-GO}.
}
$$

This affine field is not finite energy on:

$$
\mathbb R^3
$$

and is not presented as a Navier--Stokes blowup counterexample.

Its role is only to disprove an invalid local algebraic inference.

---

# 19. Updated profile classification

A bounded persistent increment branch:

$$
s_\ast
\le
\widetilde{\mathcal S}^{(3)}_n
\le
S_\ast
$$

now has the following completed alternatives.

### A. fiber escape

$$
\boxed{
\mathfrak F_{\rm fib}>0.
}
\tag{19.1}
$$

This is an infinite-dimensional native defect.

### B. full Young oscillation/concentration

On the fiber-tight branch, if:

$$
\boxed{
\mathcal D_\sigma^{(3)}>0,
}
\tag{19.2}
$$

there is a positive oscillation/concentration defect.

### C. covariance defect

If:

$$
\boxed{
R_\sigma^{YM}
-
R_\sigma[u]
\neq0,
}
\tag{19.3}
$$

the microstructure has a genuine commutator stress defect.

### D. resolved strong-profile covariance

If the profile is resolved/strong with:

$$
\widetilde{\mathcal S}^{(3)}[u]>0,
$$

then:

$$
\boxed{
R_\sigma[u]\neq0.
}
\tag{19.4}
$$

This final branch splits again into:

$$
\boxed{
R_\sigma[u]
\notin
\mathcal K_{\rm pc}
}
\tag{19.5}
$$

or:

$$
\boxed{
R_\sigma[u]
\in
\mathcal K_{\rm pc}.
}
\tag{19.6}
$$

The second is the pressure-compatible strong-profile kernel.

---

# 20. What has actually been closed

The hidden "full Young representation" assumption has been converted into:

$$
\boxed{
\text{fiber escape}
\ \vee\
\text{full representation}.
}
$$

The resolved strong-profile branch has been shown to satisfy:

$$
\boxed{
\widetilde{\mathcal S}^{(3)}[u]>0
\Longrightarrow
R_\sigma[u]\neq0.
}
$$

Thus a nonzero actual strong increment profile cannot be a covariance-free phantom.

These are genuine compactness/rigidity gains.

---

# 21. What remains open

The unresolved branch is not "Young measures" in general.

It is now:

$$
\boxed{
\textbf{
persistent nonzero covariance whose divergence is pressure-compatible,
or whose commutator work efficiency tends to zero.
}
}
\tag{21.1}
$$

The external paper already identifies the associated recurrence quantity:

$$
\boxed{
\mathfrak E_{\rm com}
=
\frac{
(W_{\rm com}^{def})_+
}{
S_{\rm def}^{(3)}+\varepsilon
}.
}
\tag{21.2}
$$

A persistent increment defect can be:

- dynamically active:

  $$
  \mathfrak E_{\rm com}\not\to0;
  $$

- dynamically inefficient:

  $$
  \mathfrak E_{\rm com}\to0.
  $$

The second branch requires rigidity.

---

# 22. The correct next frontier

The next target is:

$$
\boxed{
\textbf{
Increment Work-Efficiency / Pressure-Compatible Covariance Rigidity Lemma}.
}
$$

A useful theorem would state:

> Let:
>
> $$
> s_\ast
> \le
> \widetilde{\mathcal S}^{(3)}_n
> \le
> S_\ast
> $$
>
> on a persistent bounded-reservoir non-CKN chain.
>
> Assume:
>
> - no fiber escape;
> - no Young concentration/oscillation excess;
> - no covariance defect;
> - no UV/IR/spatial escape;
> - all localization budgets vanish.
>
> Then either:
>
> 1. the resolved covariance produces a fixed positive recurrent commutator/flux work;
>
> or:
>
> 2. the resolved covariance lies asymptotically in:
>
>    $$
>    \mathcal K_{\rm pc},
>    $$
>
>    and the corresponding pressure-compatible stress is reducible to:
>
>    - a removable pressure mode;
>    - a boundary/localization payment;
>    - or a finite-dimensional affine/rigid increment mode.
>
> Finally exclude persistent nonzero affine/rigid modes by finite energy, local recurrence, or the existing strain/pressure package.

This is now the strong-profile rigidity problem.

---

# 23. Relation to the MORP zero-cost branch

For the exact MORP zero-cost branch, DCRP-23 already gives a simpler conclusion on bounded reservoirs:

$$
\boxed{
\widetilde{\mathcal S}^{(3)}=0
}
$$

from MORP minimality,

but:

$$
\boxed{
\widetilde{\mathcal S}^{(3)}
\ge
s_\ast>0
}
$$

from persistent non-CKN.

Thus the exact zero-cost bounded-reservoir branch is already inconsistent.

The profile machinery in DCRP-24 is needed for the more difficult possibility:

$$
\boxed{
\textbf{
persistent positive-cost increment microstructure
that may continue to finance a singular cascade.
}
}
\tag{23.1}
$$

This distinction should be retained going forward.

---

# 24. Remaining global branch split

After DCRP-23/24, a persistent local singular branch satisfies one of:

### critical-reservoir blowup

$$
\boxed{
\limsup_k
\left(
A_{k,\sigma}^{+}
+
D_k
\right)
=
+\infty;
}
\tag{24.1}
$$

or:

### bounded-reservoir persistent increment microstructure

$$
\boxed{
s_\ast
\le
\widetilde{\mathcal S}^{(3)}_k
}
\tag{24.2}
$$

for all sufficiently late:

$$
k.
$$

If the second branch is additionally bounded above, DCRP-24 gives the Young/fiber/covariance classification.

Therefore the global proof has two hard fronts:

$$
\boxed{
\textbf{
critical-reservoir escape}
}
$$

and:

$$
\boxed{
\textbf{
pressure-compatible / low-efficiency increment recurrence}.
}
}
\tag{24.3}
$$

The second is currently more structured and should be attacked first.

---

# 25. Source-status audit

## MORP-01

The internal source explicitly defines:

$$
\widetilde{\mathcal S}^{(3)}
$$

as one of the nonnegative lower-semicontinuous candidate channels in:

$$
\mathfrak J.
$$

Thus a zero-cost minimizer has zero increment cost.

## arXiv:2606.27560

The primary source proves:

- derivative-compatible increment defect:

  $$
  \widetilde{\mathcal S}^{(3)};
  $$

- unconditional cylindrical generalized Young-profile extraction;
- the explicit warning that cylindrical control does not imply full norm-topology tightness;
- full norm/covariance consequences only under a full-representation hypothesis;
- nonzero covariance **defect** implies nontrivial microstructure;
- the converse is false because the covariance map is not injective;
- the defect-work ratio:

  $$
  \mathfrak E_{\rm com}
  $$

  is the proposed recurrence/rigidity test.

DCRP-24 does not contradict these cautions.

It completes the missing full-representation assumption only after adding the explicit fiber-tail alternative.

---

# 26. End state

The central new compactness theorem is:

$$
\boxed{
\mathfrak F_{\rm fib}=0
\Longrightarrow
\text{full quartic/covariance representation from the cylindrical profile}.
}
$$

The central new rigidity theorem is:

$$
\boxed{
R_\sigma[u]=0
\Longrightarrow
\text{actual resolved increments vanish locally}.
}
$$

Thus:

$$
\boxed{
\widetilde{\mathcal S}^{(3)}[u]>0
\Longrightarrow
R_\sigma[u]\neq0.
}
$$

But the exact NO-GO is:

$$
\boxed{
R_\sigma[u]\neq0
\not\Rightarrow
\text{positive bulk work}.
}
$$

A pressure-compatible covariance satisfies:

$$
\boxed{
\nabla\times\nabla\cdot R_\sigma=0
}
$$

and contributes only pressure/boundary transport.

Therefore the next single structured frontier on the bounded-reservoir positive-cost branch is:

$$
\boxed{
\textbf{
Increment Work-Efficiency / Pressure-Compatible Covariance Rigidity.
}
}
$$

The exact zero-cost bounded-reservoir branch itself is already incompatible with DCRP-23 once the MORP increment coordinate is identified.
