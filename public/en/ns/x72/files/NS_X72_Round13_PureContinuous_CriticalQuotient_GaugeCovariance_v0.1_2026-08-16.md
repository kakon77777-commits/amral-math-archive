# NS × X Integral × 24/72 Paradigm Practice
## Round 13 — Pure Continuous Critical Quotient Geometry / Gauge-Covariance Route

- Date:  2026-08-16
- Version:  v0.1
- Status:  Proof-Route Experiment / Continuous-Only Quotient-Dual Branch
- canonical source: UTF-8 Markdown
- canonical math delimiters: inline `$...$`; display `$$...$$`
- Previous round:  `NS_X72_Round12_PureContinuous_CriticalDual_CancellationTradeoff_v0.1_2026-08-16.md`
- This round's objective:  Correct the representation of the $L^{3/2}$ critical dual from Round 12. The true dual object is the quotient dual of the solenoidal $L^3$, namely $L^{3/2}$ modulo gradient fields. Verify whether the projected entropy gradient can be integrated back to a scalar functional, and determine whether the quotient geometry can eliminate the Leray defect.
- Non-claims:  The derivation of the quotient minimizer in this text is written under the standard whole-space Helmholtz decomposition and sufficient smooth/minimizer regularity; the general Banach-space version can be handled using a closed gradient subspace and subdifferential formulation.

---

# 0. Round 12 handoff

Round 12 tested two natural critical dual representatives:

$$
L^{3/2}
$$

and:

$$
\dot H^{-1/2}.
$$

yielding:

$$
\boxed{
\begin{array}{c|cc}
&\text{Transport cancellation}&\text{Leray compatibility}
\\
\hline
L^2&\checkmark&\checkmark
\\
L^{3/2}&\checkmark&\times
\\
\dot H^{-1/2}&\times&\checkmark
\end{array}
}
\tag{0.1}
$$

where the defect of the $L^{3/2}$ representative is:

$$
\mathfrak P_{3/2}
=
\left\langle
T_U\psi,
(P-I)J_{3/2}(\psi)
\right\rangle.
$$

The next question from Round 12:

$$
\boxed{
P J_{3/2}(\psi)
\text{ is truly the gradient of some scalar functional?}
}
$$

The first result of this round:

$$
\boxed{
\textbf{Yes.}
}
$$

But this is not a closure.

It reveals a deeper quotient/gauge defect.

---

# 1. The exact critical dual is a quotient space

Let:

$$
L^3_\sigma
=
\left\{
u\in L^3(\mathbb R^3;\mathbb R^3):
\nabla\cdot u=0
\right\}.
$$

Set:

$$
\mathcal G_p
=
\overline{
\{
\nabla q:
q\in C_c^\infty(\mathbb R^3)
\}
}^{L^p}.
$$

In the standard whole-space Helmholtz decomposition:

$$
L^p
=
L^p_\sigma
\oplus
\mathcal G_p,
\qquad
1<p<\infty.
$$

Therefore:

$$
\boxed{
(L^3_\sigma)^\ast
\simeq
L^{3/2}/\mathcal G_{3/2}.
}
\tag{1.1}
$$

Thus, the true critical dual state is not a single divergence-free representative:

$$
\psi,
$$

but rather an equivalence class:

$$
\boxed{
[\psi]
=
\psi+\mathcal G_{3/2}.
}
\tag{1.2}
$$

---

# 2. Quotient norm

For:

$$
1<p<\infty,
$$

define:

$$
\boxed{
\|[f]\|_{Q_p}
=
\inf_{g\in\mathcal G_p}
\|f+g\|_{L^p}.
}
\tag{2.1}
$$

For:

$$
p=\frac32,
$$

this norm possesses the dual critical scaling.

If:

$$
\psi=P f
$$

is the canonical solenoidal representative, then:

$$
[f]=[\psi].
$$

and:

$$
\|[f]\|_{Q_p}
\le
\|\psi\|_p.
$$

On the other hand, since the Helmholtz projector:

$$
P:L^p\to L^p_\sigma
$$

is bounded,

for any:

$$
v\in[f],
$$

$$
\psi=Pv.
$$

hence:

$$
\|\psi\|_p
\le
C_p
\|v\|_p.
$$

Taking the infimum:

$$
\boxed{
\|[f]\|_{Q_p}
\le
\|Pf\|_p
\le
C_p
\|[f]\|_{Q_p}.
}
\tag{2.2}
$$

Therefore, the quotient norm is not a weakened norm that loses critical information.

It is equivalent to the canonical solenoidal representative norm.

---

# 3. Exact dual norm detection

For:

$$
u\in L^3_\sigma,
$$

gradient fields annihilate the pairing:

$$
\langle
\nabla q,u
\rangle
=
0.
$$

Thus, the pairing depends only on the quotient class:

$$
\langle
[f],u
\rangle
:=
\langle
f,u
\rangle.
$$

Banach duality gives:

$$
\boxed{
\|u\|_{L^3}
=
\sup_{
\|[f]\|_{Q_{3/2}}\le1
}
|\langle
[f],u
\rangle|.
}
\tag{3.1}
$$

Therefore:

$$
\boxed{
Q_{3/2}
=
L^{3/2}/\mathcal G_{3/2}
}
$$

is the true critical dual geometry perfectly aligned with the primal $L^3_\sigma$.

---

# 4. Unique minimum representative

Since:

$$
1<p<\infty,
$$

$L^p$ is reflexive and strictly/uniformly convex.

For the closed affine class:

$$
[f]
$$

there exists a unique minimum-norm representative:

$$
\boxed{
v_\ast
=
f+g_\ast,
\qquad
g_\ast\in\mathcal G_p,
}
\tag{4.1}
$$

such that:

$$
\boxed{
\|v_\ast\|_p
=
\|[f]\|_{Q_p}.
}
\tag{4.2}
$$

Written under a smooth gradient representation:

$$
\boxed{
v_\ast
=
\psi+\nabla q_\ast,
}
\tag{4.3}
$$

where:

$$
P\psi=\psi.
$$

---

# 5. Nonlinear entropy gauge condition

The minimum representative is equivalent to minimizing:

$$
\mathcal E_p(v)
=
\frac1p
\int
|v|^pdx
$$

over the class:

$$
v=\psi+\nabla q.
$$

For:

$$
q\mapsto q+\varepsilon h
$$

the variation is:

$$
0
=
\left.
\frac d{d\varepsilon}
\right|_{\varepsilon=0}
\mathcal E_p
(
v_\ast+\varepsilon\nabla h
).
$$

Let:

$$
J_p(v)
=
|v|^{p-2}v.
$$

Then:

$$
0
=
\int
J_p(v_\ast)\cdot\nabla hdx
=
-
\int
\operatorname{div}
J_p(v_\ast)
h\,dx.
$$

Therefore:

$$
\boxed{
\operatorname{div}
J_p(v_\ast)
=
0.
}
\tag{5.1}
$$

For the critical:

$$
p=\frac32,
$$

we obtain the nonlinear gauge:

$$
\boxed{
\operatorname{div}
\left(
|v_\ast|^{-1/2}v_\ast
\right)
=
0.
}
\tag{5.2}
$$

This is the first new carrier of this round.

---

# 6. Projected entropy gradient is integrable

The candidate from Round 12:

$$
P J_p(\psi)
$$

might not appear to be a scalar functional gradient.

But on the divergence-free subspace:

$$
H_\sigma
$$

considering the ordinary entropy:

$$
\mathcal E_p[\psi]
=
\frac1p
\int
|\psi|^pdx.
$$

For any divergence-free tangent:

$$
h,
$$

we have:

$$
D\mathcal E_p[\psi](h)
=
\langle
J_p(\psi),h
\rangle.
$$

Also, since:

$$
Ph=h,
$$

$$
\langle
J_p,h
\rangle
=
\langle
P J_p,h
\rangle.
$$

Therefore, the constrained $L^2$ gradient is exactly:

$$
\boxed{
\nabla_{\sigma,L^2}
\mathcal E_p
=
P J_p(\psi).
}
\tag{6.1}
$$

Thus:

$$
\boxed{
\textbf{
there is no variational integrability obstruction here.
}
}
\tag{6.2}
$$

The next hurdle from Round 12 is legitimately bypassed.

---

# 7. The projected entropy defect is intrinsic

Although:

$$
P J_p
$$

is indeed a constrained gradient,

the critical entropy derivative remains:

$$
\frac1p
\frac d{d\sigma}
\|\psi\|_p^p
+
\nu
\mathfrak D_p(\psi)
=
\langle
P T_U\psi,
P J_p(\psi)
\rangle.
$$

So the defect is not:

> $PJ_p$ is not a gradient.

but rather:

$$
\boxed{
\text{projected transport vector field is not tangent to entropy level sets}.
}
$$

That is, after the integrability is repaired, the coercivity problem persists.

---

# 8. Quotient evolution

The Round 12 backward-time dual equation:

$$
\partial_\sigma\psi
=
\nu\Delta\psi
+
P T_U\psi.
$$

In the quotient:

$$
[P T_U\psi]
=
[T_U\psi].
$$

And if:

$$
v_\ast
=
\psi+\nabla q_\ast,
$$

then:

$$
[\Delta v_\ast]
=
[\Delta\psi].
$$

Therefore, the quotient class evolution can be represented by the representative:

$$
\boxed{
\nu\Delta v_\ast
+
T_U\psi
}
\tag{8.1}
$$

By the minimum-envelope / stationarity condition,

the gauge derivative of $q_\ast$ with respect to time does not directly contribute to the first-order norm variation, because:

$$
\operatorname{div}J_p(v_\ast)=0.
$$

Thus:

$$
\boxed{
\frac1p
\frac d{d\sigma}
\|[\psi]\|_{Q_p}^p
+
\nu
\mathfrak D_p(v_\ast)
=
\langle
J_p(v_\ast),
T_U\psi
\rangle.
}
\tag{8.2}
$$

---

# 9. Gauge noncovariance identity

Since:

$$
\psi
=
v_\ast-\nabla q_\ast,
$$

we have:

$$
T_U\psi
=
T_Uv_\ast
-
T_U\nabla q_\ast.
$$

The raw transport entropy cancellation gives:

$$
\langle
J_p(v_\ast),
T_Uv_\ast
\rangle
=
0.
$$

while:

$$
\boxed{
T_U\nabla q
=
\nabla(T_Uq)
-
(\nabla U)^\top\nabla q.
}
\tag{9.1}
$$

Since:

$$
\operatorname{div}J_p(v_\ast)=0,
$$

the gradient part vanishes.

Therefore:

$$
\boxed{
\langle
J_p(v_\ast),
T_U\psi
\rangle
=
\left\langle
J_p(v_\ast),
(\nabla U)^\top
\nabla q_\ast
\right\rangle.
}
\tag{9.2}
$$

Thus, the exact quotient entropy law is:

$$
\boxed{
\frac1p
\frac d{d\sigma}
\|[\psi]\|_{Q_p}^p
+
\nu
\mathfrak D_p(v_\ast)
=
\mathfrak G_p[U,\psi],
}
\tag{9.3}
$$

where:

$$
\boxed{
\mathfrak G_p
=
\int
J_p(v_\ast)\cdot
(\nabla U)^\top
\nabla q_\ast
\,dx.
}
\tag{9.4}
$$

Named:

$$
\boxed{
\textbf{Gauge-Deformation Defect}.
}
$$

---

# 10. Defect transmutation

The Round 12 canonical representative saw:

$$
\boxed{
\mathfrak P_p
=
\text{Leray projection defect}.
}
$$

The Round 13 exact quotient geometry eliminates the explicit projection defect,

but yields:

$$
\boxed{
\mathfrak G_p
=
\text{gauge-deformation / velocity-gradient defect}.
}
$$

Therefore:

$$
\boxed{
\textbf{
quotient geometry removes the representation-level Leray defect,
but does not remove the physical transport–constraint mismatch.
}
}
\tag{10.1}
$$

It merely rewrites the obstruction in a more intrinsic way.

---

# 11. Why componentwise transport fails on gradient classes

For two representatives in the same quotient class:

$$
v
$$

and:

$$
v+\nabla q,
$$

the componentwise transport difference is:

$$
T_U(v+\nabla q)-T_Uv
=
T_U\nabla q.
$$

From (9.1):

$$
T_U\nabla q
=
\nabla(T_Uq)
-
(\nabla U)^\top\nabla q.
$$

The second term is generally not a gradient.

Therefore:

$$
\boxed{
[T_U(v+\nabla q)]
\neq
[T_Uv]
}
\tag{11.1}
$$

holds in general.

Thus:

$$
\boxed{
\textbf{
componentwise transport does not descend naturally
to the quotient by gradient fields.
}
}
\tag{11.2}
$$

This is the geometric origin of $\mathfrak G_p$.

---

# 12. Lie derivative repairs gauge covariance

Treat the vector field as a Euclidean 1-form.

Define the 1-form Lie transport:

$$
\boxed{
\mathcal L_U^{(1)}v
=
T_Uv
+
(\nabla U)^\top v.
}
\tag{12.1}
$$

Then for an exact 1-form:

$$
\nabla q,
$$

we have:

$$
\boxed{
\mathcal L_U^{(1)}
(\nabla q)
=
\nabla(T_Uq).
}
\tag{12.2}
$$

Therefore:

$$
\boxed{
\mathcal L_U^{(1)}
}
$$

truly preserves gradient gauge classes.

So if we only look at the quotient geometry,

the Lie derivative is the natural transport operator.

---

# 13. But Lie transport loses local entropy conservation

For:

$$
v,
$$

we have:

$$
\langle
J_p(v),
T_Uv
\rangle
=
0.
$$

But:

$$
\boxed{
\langle
J_p(v),
\mathcal L_U^{(1)}v
\rangle
=
\int
|v|^{p-2}
v\cdot
(\nabla U)^\top v
\,dx.
}
\tag{13.1}
$$

Since the same vector appears on both sides,

the antisymmetric rotation part vanishes.

Let:

$$
S_U
=
\frac12
\left(
\nabla U+\nabla U^\top
\right).
$$

Then:

$$
\boxed{
\langle
J_p(v),
\mathcal L_U^{(1)}v
\rangle
=
\int
|v|^{p-2}
v^\top
S_U
v
\,dx.
}
\tag{13.2}
$$

Therefore:

$$
\boxed{
\text{Lie transport preserves gradient gauge
but introduces strain stretching}.
}
$$

---

# 14. Transport–Gauge Covariance Tradeoff

Now another cancellation square emerges.

## Componentwise transport

$$
T_U
=
U\cdot\nabla.
$$

It preserves:

$$
\boxed{
L^p\text{ entropy chain-rule cancellation}
}
$$

but loses:

$$
\boxed{
\text{gradient-gauge covariance}.
}
$$

## One-form Lie transport

$$
\mathcal L_U^{(1)}
=
T_U
+
(\nabla U)^\top.
$$

It preserves:

$$
\boxed{
\text{gradient-gauge covariance}
}
$$

but loses:

$$
\boxed{
L^p\text{ entropy conservation}
}
$$

due to strain stretching.

Therefore:

$$
\boxed{
\textbf{Transport–Gauge Covariance Tradeoff}.
}
\tag{14.1}
$$

---

# 15. Why $p=2$ is again special

If:

$$
p=2,
$$

the quotient minimum representative of a divergence-free:

$$
\psi
$$

is simply:

$$
v_\ast=\psi
$$

because the standard Helmholtz decomposition is orthogonal in $L^2$.

So:

$$
q_\ast=0.
$$

Therefore:

$$
\boxed{
\mathfrak G_2=0.
}
$$

This restores the:

$$
L^2
$$

exact dual contraction.

For:

$$
p\neq2,
$$

the metric projection onto gradient classes is not a linear orthogonal projection,

and:

$$
q_\ast
$$

is generally non-zero.

So the critical:

$$
p=\frac32
$$

once again loses the special $L^2 geometry.

---

# 16. The exact critical quotient law

Let:

$$
p=\frac32.
$$

Define:

$$
N_Q
=
\|[\psi]\|_{Q_{3/2}}
=
\|v_\ast\|_{3/2}.
$$

Then:

$$
J_{3/2}(v_\ast)
=
|v_\ast|^{-1/2}v_\ast.
$$

nonlinear gauge:

$$
\boxed{
\operatorname{div}
\left(
|v_\ast|^{-1/2}v_\ast
\right)
=
0.
}
\tag{16.1}
$$

exact evolution:

$$
\boxed{
\frac23
\frac d{d\sigma}
N_Q^{3/2}
+
\nu
\mathfrak D_{3/2}(v_\ast)
=
\int
|v_\ast|^{-1/2}
v_\ast
\cdot
(\nabla U)^\top
\nabla q_\ast
\,dx.
}
\tag{16.2}
$$

This is currently the most precise $L^3$ critical dual quotient balance.

---

# 17. Gauge-stress tensor

Define:

$$
\boxed{
\mathbb K_p
=
\nabla q_\ast
\otimes
J_p(v_\ast).
}
\tag{17.1}
$$

Then:

$$
\boxed{
\mathfrak G_p
=
\int
\nabla U:
\mathbb K_p
\,dx
}
\tag{17.2}
$$

with the corresponding transpose depending on the adopted matrix-index convention.

Decompose:

$$
\mathbb K_p
$$

into symmetric / antisymmetric parts:

$$
\mathbb K_p
=
\mathbb K_p^{\rm sym}
+
\mathbb K_p^{\rm skew}.
$$

Then:

$$
\boxed{
\mathfrak G_p
=
\int
S_U:
\mathbb K_p^{\rm sym}
+
\Omega_U:
\mathbb K_p^{\rm skew}
\,dx.
}
\tag{17.3}
$$

Therefore, the quotient defect is a truly relational carrier:

$$
\boxed{
\text{velocity-gradient geometry}
\times
\text{optimal-gauge stress}.
}
$$

---

# 18. Crude control returns to Lipschitz/BKM-type information

By Hölder's inequality:

$$
|\mathfrak G_p|
\le
\|\nabla U\|_\infty
\|J_p(v_\ast)\|_{p'}
\|\nabla q_\ast\|_p.
$$

And:

$$
\|J_p(v_\ast)\|_{p'}
=
\|v_\ast\|_p^{p-1}.
$$

Also:

$$
\psi=Pv_\ast,
$$

so:

$$
\|\psi\|_p
\le
C_p\|v_\ast\|_p.
$$

And:

$$
\nabla q_\ast
=
v_\ast-\psi.
$$

hence:

$$
\|\nabla q_\ast\|_p
\le
(1+C_p)
\|v_\ast\|_p.
$$

Therefore:

$$
\boxed{
|\mathfrak G_p|
\le
C_p^\ast
\|\nabla U\|_\infty
\|[\,\psi\,]\|_{Q_p}^p.
}
\tag{18.1}
$$

For:

$$
p=\frac32,
$$

this gives:

$$
\boxed{
\frac d{d\sigma}
N_Q^{3/2}
\lesssim
\|\nabla U\|_\infty
N_Q^{3/2}.
}
\tag{18.2}
$$

So if:

$$
\int
\|\nabla U\|_\infty
d\sigma
<\infty,
$$

the critical quotient norm can be controlled via Gronwall's inequality.

But this merely sends the problem back to Lipschitz/BKM-type continuation information.

It is not an energy-level unconditional closure.

---

# 19. A restricted local correction no-go

Consider an affine incompressible drift:

$$
U(x)=Ax,
$$

where:

$$
\operatorname{tr}A=0.
$$

Attempt to modify the component transport:

$$
D_Uv
=
T_Uv
+
Bv
$$

where:

$$
B
$$

is a constant matrix depending on $A$.

Require two things to hold simultaneously.

## G1. Gradient covariance

For all smooth scalars:

$$
q,
$$

$$
D_U(\nabla q)
$$

remains a gradient.

Since:

$$
T_U\nabla q
=
\nabla(T_Uq)-A^\top\nabla q,
$$

this requires:

$$
(B-A^\top)\nabla q
$$

to be a gradient for all $q$.

A constant matrix:

$$
M
$$

if it makes:

$$
M\nabla q
$$

a gradient for all $q$,

then:

$$
M
$$

must be a scalar multiple of the identity:

$$
M=cI.
$$

Therefore:

$$
\boxed{
B
=
A^\top+cI.
}
\tag{19.1}
$$

## G2. Universal isotropic entropy neutrality

Require that for all vectors:

$$
v
$$

we have:

$$
v^\top Bv=0.
$$

This forces:

$$
\operatorname{sym}B=0.
$$

From:

$$
B=A^\top+cI
$$

and:

$$
\operatorname{tr}A=0,
$$

taking the trace yields:

$$
c=0.
$$

Therefore:

$$
\operatorname{sym}A=0.
$$

That is:

$$
\boxed{
A
\text{ must be a pure rigid rotation}.
}
\tag{19.2}
$$

So as long as the drift has non-zero strain,

there does not exist such a constant zeroth-order matrix correction that universally preserves both:

- gradient gauge covariance;
- isotropic entropy neutrality.

Named:

$$
\boxed{
\textbf{Affine Gauge–Entropy No-Go}.
}
$$

This is a restricted local no-go, which does not rule out nonlocal/dynamic corrections.

---

# 20. What the quotient route repaired and what it did not

Successfully repaired:

$$
\boxed{
\text{ordinary divergence-free }L^{3/2}
\text{ representative is not the exact dual geometry}.
}
$$

The more precise dual:

$$
\boxed{
Q_{3/2}
=
L^{3/2}/\mathcal G_{3/2}.
}
$$

It:

- is critical;
- is lossless for $L^3_\sigma$ duality;
- has a unique minimal representative;
- generates a nonlinear divergence-free entropy gauge;
- makes the variational integrability of $P J_{3/2}$ no longer an issue.

But did not repair:

$$
\boxed{
\text{transport–constraint compatibility}.
}
$$

The obstruction is compressed into:

$$
\boxed{
\mathfrak G_{3/2}
=
\text{gauge stress}
\times
\nabla U.
}
$$

---

# 21. STOP-C17 — Critical Quotient Gauge-Covariance / Stretching Gap

Define:

$$
\boxed{
\bot_X^{\mathrm{C17}}
=
\left\langle
\begin{array}{l}
\text{layer}
=
\mathrm{exact\ }L^3\mathrm{\ critical\ dual\ quotient},
\\
\text{dual}
=
L^{3/2}/\mathcal G_{3/2},
\\
\text{minimal\ representative}
=
v_\ast,
\\
\text{entropy\ gauge}
=
\operatorname{div}(|v_\ast|^{-1/2}v_\ast)=0,
\\
\text{projected-gradient\ integrability}
=
\mathrm{true},
\\
\text{explicit\ Leray\ defect}
=
\mathrm{removed},
\\
\text{remaining\ defect}
=
\mathfrak G_{3/2},
\\
\text{geometric\ source}
=
T_U\nabla q
-
\nabla(T_Uq)
=
-(\nabla U)^\top\nabla q,
\\
\text{Lie\ derivative}
=
\mathrm{gauge\ covariant\ but\ stretching},
\\
\text{missing}
=
\mathrm{critical\ control\ of\ gauge\text{-}stretching\ coupling},
\\
\text{discrete\ intrusion}
=
\mathrm{false}.
\end{array}
\right\rangle.
}
$$

Named:

$$
\boxed{
\textbf{STOP-C17:
Critical Quotient Gauge-Covariance / Stretching Gap}.
}
$$

---

# 22. 24/72 Ledger — Round 13

| Step | X object / operation | $B$ | $U$ | $O$ | $L$ | status |
|---|---|---|---|---|---|---|
| C136 | quotient dual $Q_{3/2}$ | $\mathsf C$ | quotient/global | $\mathsf X$ | $\mathsf F$ | FORM |
| C137 | quotient–solenoidal norm equivalence | $\mathsf C$ | retrieval | targeted | $\mathsf F$ | PROVED under Helmholtz setting |
| C138 | minimum representative $v_\ast$ | $\mathsf C$ | variational | relational | $\mathsf F$ | FORM |
| C139 | nonlinear entropy gauge | $\mathsf C$ | variational | targeted relation | $\mathsf F$ | EXACT |
| C140 | $PJ_p$ integrability | $\mathsf C$ | constrained variational | gradient | $\mathsf F$ | PROVED |
| C141 | quotient entropy law | $\mathsf C$ | quotient evolution | scalar + relation | $\mathsf F$ | EXACT |
| C142 | gauge noncovariance identity | $\mathsf C$ | transport | relational | $\mathsf F$ | EXACT |
| C143 | Lie derivative gauge repair | $\mathsf C$ | geometric transport | quotient | $\mathsf F$ | EXACT |
| C144 | Lie-transport entropy stretching | $\mathsf C$ | geometric transport | scalar | $\mathsf F$ | EXACT |
| C145 | gauge-stress tensor $\mathbb K_p$ | $\mathsf C$ | relational | $\mathsf X$ | $\mathsf F$ | FORM |
| C146 | Lipschitz control of defect | $\mathsf C$ | estimate | scalar | $\mathsf F$ | CONDITIONAL |
| C147 | affine local gauge–entropy repair | $\mathsf C$ | local correction | relational | $\mathsf F$ | NO-GO except rigid rotation |
| C148 | unconditional critical gauge-stretching control | $\mathsf C$ | — | targeted | $\mathsf F$ | OPEN / STOP-C17 |

---

# 23. Continuous-versus-discrete status

The quotient in this round:

$$
L^{3/2}/\mathcal G_{3/2}
$$

is an infinite-dimensional continuous Banach geometry.

The minimum representative is formed by a continuous convex variational problem.

The nonlinear gauge:

$$
\operatorname{div}
(
|v|^{-1/2}v
)=0
$$

is also a continuous PDE condition.

No introduction of:

- atoms;
- dyadic blocks;
- wavelet packets;
- sequence extraction;
- countable basis closure.

Therefore:

$$
\boxed{
T_{\mathsf C\to\mathsf D}
=
\text{NOT YET REACHED}.
}
\tag{23.1}
$$

---

# 24. New structural interpretation

Round 12 appeared to be:

$$
\boxed{
\text{Leray projection ruins critical entropy}.
}
$$

Round 13 corrects this to:

$$
\boxed{
\textbf{
the deeper obstruction is that componentwise transport
does not preserve the gradient gauge underlying the exact critical dual quotient.
}
}
\tag{24.1}
$$

If changed to a gauge-covariant one-form Lie transport,

the gradient quotient naturally closes,

but strain stretching reappears.

So the problem has advanced from:

$$
\text{projection}
$$

to:

$$
\boxed{
\text{gauge covariance}
\leftrightarrow
\text{stretching}.
}
$$

---

# 25. An unexpected primal bridge

For the velocity one-form,

using the identity:

$$
\mathcal L_u^{(1)}u
=
(u\cdot\nabla)u
+
\nabla
\left(
\frac12|u|^2
\right).
$$

Navier–Stokes can be written as:

$$
\boxed{
\partial_tu
+
\mathcal L_u^{(1)}u
=
\nu\Delta u
-
\nabla
\left(
p-\frac12|u|^2
\right).
}
\tag{25.1}
$$

Therefore, modulo gradients:

$$
\boxed{
\partial_t[u]
+
[\mathcal L_u^{(1)}u]
=
\nu[\Delta u].
}
\tag{25.2}
$$

And:

$$
\mathcal L_u^{(1)}
$$

is exactly the natural transport preserving the gradient quotient.

So the critical quotient geometry is not just a dual trick.

It actually connects to the geometric formulation of the Navier–Stokes velocity 1-form itself.

This provides a new route for the next round.

---

# 26. Next round — critical one-form / circulation quotient

The next round will test the primal critical quotient instead:

$$
\boxed{
\mathfrak Q_3[u]
=
\inf_q
\|u+\nabla q\|_{L^3}.
}
$$

By Helmholtz boundedness:

$$
\mathfrak Q_3[u]
$$

and:

$$
\|u\|_3
$$

are equivalent for divergence-free $u$,

so it remains a true $L^3$ critical continuation carrier.

But it has an advantage that the Round 13 dual route lacks:

$$
\boxed{
\text{NS modulo gradients is inherently a Lie-transport equation}.
}
$$

Questions for the next round:

1. What nonlinear gauge does the quotient-minimal velocity 1-form:

$$
v_\ast=u+\nabla q_\ast
$$

satisfy?

2. Does Lie transport completely eliminate the pressure in the quotient?

3. Does the critical quotient norm evolution leave only the strain-stretching term?

4. Can this stretching be coupled with the $\lambda_2$ carrier from Round 03 / the gradient-alignment carriers from Round 05?

5. Does a new circulation / Kelvin-type invariant emerge?

6. If it still cannot be closed, test the differential-form hierarchy further, rather than discretizing prematurely.

---

# 27. External primary-source anchors

1. Tuoc Phan, *Well-posedness for the Navier-Stokes equations in critical mixed-norm Lebesgue spaces*, arXiv:1903.08319.
   - critical Lebesgue-space NS framework;
   - Helmholtz–Leray projection boundedness and Riesz-transform machinery.

2. Pascal Hobus, Jürgen Saal, *Stokes and Navier-Stokes equations subject to partial slip on uniform $C^{2,1}$-domains in $L_q$-spaces*, arXiv:2003.05801.
   - The importance of the $L_q$ Helmholtz decomposition as a functional framework for Stokes/Navier–Stokes;
   - The whole-space quotient in this round uses the standard Helmholtz case.

3. Standard Cartan/Lie-derivative identity for exact one-forms:
   $$
   \mathcal L_U(dq)=d(Uq).
   $$
   All gauge-covariance, quotient evolution, entropy-gauge, and affine no-go formulas in this round are directly derived in this text.

---

# 28. Commit state

$$
\boxed{
\begin{aligned}
\text{Route}
&:
\mathrm{Pure\ Continuous\ Critical\ Quotient\ Geometry},
\\
\text{Essential }\mathsf C\to\mathsf D
&:
\mathrm{Not\ reached},
\\
\text{Exact critical dual}
&:
L^{3/2}/\mathcal G_{3/2},
\\
\text{Projected entropy gradient}
&:
\mathrm{integrable},
\\
\text{Minimum representative}
&:
v_\ast,
\\
\text{Nonlinear gauge}
&:
\operatorname{div}(|v_\ast|^{-1/2}v_\ast)=0,
\\
\text{Round12 Leray defect}
&:
\mathrm{transmuted},
\\
\text{New exact defect}
&:
\mathfrak G_{3/2},
\\
\text{Underlying obstruction}
&:
\mathrm{transport\ gauge\ noncovariance},
\\
\text{Gauge-covariant repair}
&:
\mathrm{one\text{-}form\ Lie\ transport},
\\
\text{Repair cost}
&:
\mathrm{strain\ stretching},
\\
\text{STOP-C17}
&:
\mathrm{Critical\ Quotient\ Gauge\text{-}Covariance/Stretching\ Gap},
\\
\text{Next}
&:
\mathrm{Critical\ One\text{-}Form/Circulation\ Quotient}.
\end{aligned}
}
$$