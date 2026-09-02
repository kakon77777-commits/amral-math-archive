# NS × X Integral × 24/72 Paradigm in Action
## Round 05 — Pure Continuous Nonlocal Cancellation / Gradient-Stress Alignment Route

- Date: 2026-08-16
- Version: v0.1
- Status: Proof-Route Experiment / Continuous-Only Projection–Cancellation Branch
- canonical source: UTF-8 Markdown
- canonical math delimiters: inline `$...$`; display `$$...$$`
- Previous round: `NS_X72_Round04_PureContinuous_GeometryEvolution_PressureConstraint_v0.1_2026-08-16.md`
- Objective of this round: Reverse the order of Round 04. First, utilize incompressibility, strain projection, and global orthogonality to eliminate pressure / null channels, and then check whether sufficient geometric information can still be preserved to form an exact coercive carrier.
- Non-claim: If this document derives new equations or conditional criteria, it only claims the direct derivations herein; it does not claim academic novelty unless audited by independent literature.

---

# 0. Round 04 handoff

Round 04 showed that the exact evolution of the local strain spectrum requires:

$$
H_p
=
\nabla^2p
=
\nabla^2(-\Delta)^{-1}
\left(
|S|^2-\frac12|\omega|^2
\right).
$$

Therefore, the finite local differential state:

$$
J^k(S,\omega)
$$

cannot exactly reconstruct the anisotropic pressure Hessian.

Yielding:

$$
\boxed{
\text{STOP-C07}
=
\text{Local-Geometry / Nonlocal-Pressure Closure Gap}.
}
$$

Meanwhile, in the global pairing:

$$
\int S:H_p\,dx
=
0,
$$

but:

$$
e_2^\top H_pe_2
$$

remains in the local eigenvalue evolution.

Yielding:

$$
\boxed{
\text{STOP-C08}
=
\text{Global-Cancellation / Local-Feedback Gap}.
}
$$

Therefore, this round no longer requires pointwise eigenvalue closure.

Instead, we ask:

$$
\boxed{
\text{If we first perform global projection/cancellation,
can we reconstruct a relational carrier that exactly preserves the H¹ strain growth?}
}
$$

---

# 1. Strain equation in projected form

Consider the smooth rapidly decaying incompressible Navier–Stokes equations:

$$
\partial_tu
+
(u\cdot\nabla)u
+
\nabla p
=
\nu\Delta u,
$$

$$
\nabla\cdot u=0.
$$

Let:

$$
S
=
\nabla_{\rm sym}u,
$$

$$
\omega
=
\nabla\times u.
$$

Using the strain-space orthogonal projection:

$$
P_{st}.
$$

the strain equation can be written as:

$$
\boxed{
\partial_tS
-
\nu\Delta S
-
\frac12
P_{st}(\omega\otimes\omega)
+
\mathcal R
=
0,
}
\tag{1.1}
$$

where the full NS residual is defined as:

$$
\boxed{
\mathcal R
=
P_{st}
\left(
(u\cdot\nabla)S
+
S^2
+
\frac34
\omega\otimes\omega
\right).
}
\tag{1.2}
$$

The purpose of this decomposition is not model replacement.

It preserves the full NS strain dynamics.

---

# 2. The key strain–vorticity orthogonality

For a sufficiently smooth strain field, we have the exact identity:

$$
\boxed{
\left\langle
-\Delta S,
\omega\otimes\omega
\right\rangle
=
0.
}
\tag{2.1}
$$

Furthermore:

$$
-\Delta S
$$

still belongs to the strain constraint space, so for any admissible tensor $F$:

$$
\boxed{
\left\langle
P_{st}F,
-\Delta S
\right\rangle
=
\left\langle
F,
-\Delta S
\right\rangle.
}
\tag{2.2}
$$

Let:

$$
B
=
-\Delta S.
$$

Taking the $L^2$ pairing with (1.1).

Yields:

$$
\boxed{
\frac12
\frac d{dt}
\|S\|_{\dot H^1}^2
+
\nu
\|B\|_2^2
=
-
\langle
\mathcal R,B
\rangle.
}
\tag{2.3}
$$

This is the exact strain-$\dot H^1$ balance of the full NS equations.

---

# 3. Pressure has disappeared without deleting the full NS dynamics

Note that (2.3) does not contain:

$$
H_p.
$$

This is not ignoring the pressure.

Rather:

1. The pressure Hessian lies in the orthogonal null direction of the strain-space;
2. $P_{st}$ projects the full strain dynamics onto the compatible strain subspace;
3. For the growth observable:

$$
\|S\|_{\dot H^1}^2,
$$

this projection preserves the exact pairing.

Therefore, Round 04's:

$$
\boxed{
\text{Local-C}
\to
\text{Global/Nonlocal-C}
}
$$

is not a dead end.

At least for the:

$$
\dot H^1
$$

strain growth, the global projection can legitimately eliminate the pressure.

---

# 4. Amplitude–alignment decomposition

Let:

$$
D(t)
=
\|B(t)\|_2.
$$

When:

$$
D(t)>0
$$

define the residual amplitude ratio:

$$
\boxed{
\chi_\nu(t)
=
\frac{
\|\mathcal R(t)\|_2
}{
\nu D(t)
}.
}
\tag{4.1}
$$

If:

$$
\mathcal R(t)\neq0,
$$

then define the dangerous alignment cosine:

$$
\boxed{
c(t)
=
-
\frac{
\langle\mathcal R,B\rangle
}{
\|\mathcal R\|_2D
}.
}
\tag{4.2}
$$

Thus:

$$
-1\le c(t)\le1.
$$

Define the exact growth coefficient:

$$
\boxed{
\alpha_\nu(t)
=
\chi_\nu(t)c(t)
=
-
\frac{
\langle\mathcal R,B\rangle
}{
\nu D^2
}.
}
\tag{4.3}
$$

If:

$$
D=0,
$$

then within the finite-energy whole-space class, it has entered a spatially affine / trivial branch; below we only discuss $D>0$.

Substituting into (2.3):

$$
\boxed{
\frac12
\frac d{dt}
\|S\|_{\dot H^1}^2
+
\nu
\left(
1-\alpha_\nu(t)
\right)
D(t)^2
=
0.
}
\tag{4.4}
$$

This is an exact scalar reduction.

---

# 5. Interpretation of $\alpha_\nu$

If:

$$
\alpha_\nu<1,
$$

then currently:

$$
\frac d{dt}
\|S\|_{\dot H^1}^2<0.
$$

If:

$$
\alpha_\nu=1,
$$

then:

$$
\frac d{dt}
\|S\|_{\dot H^1}^2=0.
$$

If:

$$
\alpha_\nu>1,
$$

then:

$$
\frac d{dt}
\|S\|_{\dot H^1}^2>0.
$$

Therefore:

$$
\boxed{
\alpha_\nu
}
$$

is not an ordinary norm amplitude.

It is:

$$
\boxed{
\text{nonlinearity amplitude}
\times
\text{dangerous alignment}.
}
$$

Thus, the conclusion of Round 03:

$$
\text{amplitude-only observation is insufficient}
$$

receives a more precise replacement here:

$$
\boxed{
\text{growth is controlled by amplitude–alignment product, not amplitude alone}.
}
\tag{5.1}
$$

---

# 6. Exact logarithmic growth integral

Define:

$$
A(t)
=
\|S(t)\|_{\dot H^1}^2.
$$

For a nontrivial whole-space solution, if:

$$
A(t)>0,
$$

From (4.4):

$$
\boxed{
A'
=
2\nu
(\alpha_\nu-1)
D^2.
}
\tag{6.1}
$$

Therefore:

$$
\boxed{
\frac d{dt}\log A
=
2\nu
(\alpha_\nu-1)
\frac{D^2}{A}.
}
\tag{6.2}
$$

Integrating:

$$
\boxed{
A(T)
=
A(0)
\exp
\left[
2\nu
\int_0^T
(\alpha_\nu(t)-1)
\frac{D(t)^2}{A(t)}
\,dt
\right].
}
\tag{6.3}
$$

Define the continuous growth integral:

$$
\boxed{
\mathfrak G(T)
=
\int_0^T
(\alpha_\nu(t)-1)
\frac{
\|-\Delta S(t)\|_2^2
}{
\|S(t)\|_{\dot H^1}^2
}
\,dt.
}
\tag{6.4}
$$

Then:

$$
\boxed{
\|S(T)\|_{\dot H^1}^2
=
\|S(0)\|_{\dot H^1}^2
e^{2\nu\mathfrak G(T)}.
}
\tag{6.5}
$$

So in this smooth strong-solution class:

$$
\boxed{
\mathfrak G(T)
}
$$

is the exact continuous accumulator for the strain-$\dot H^1$ growth.

---

# 7. Necessary growth condition for finite-time singularity

If the maximal strong solution loses regularity at:

$$
T_\ast<\infty
$$

and continuation theory requires:

$$
\|S(t)\|_{\dot H^1}
\to\infty
$$

along approaching times, then by (6.5) we must have:

$$
\boxed{
\mathfrak G(T)
\to+\infty
\qquad
(T\uparrow T_\ast).
}
\tag{7.1}
$$

A more conservative sufficient regularity condition is:

$$
\boxed{
\int_0^{T_\ast}
(\alpha_\nu-1)_+
\frac{D^2}{A}
\,dt
<
\infty.
}
\tag{7.2}
$$

Because:

$$
\mathfrak G(T)
\le
\int_0^T
(\alpha_\nu-1)_+
\frac{D^2}{A}
\,dt.
$$

So when this positive danger integral is bounded:

$$
A(T)
$$

remains bounded.

This is still a conditional criterion, not an unconditional NS estimate.

---

# 8. Recovering the MORP / model-cone threshold

By Cauchy–Schwarz:

$$
c(t)\le1.
$$

Therefore:

$$
\boxed{
\alpha_\nu(t)
\le
\chi_\nu(t).
}
\tag{8.1}
$$

Thus if:

$$
\boxed{
\chi_\nu(t)\le1
}
\tag{8.2}
$$

holds for a period of time, then:

$$
\alpha_\nu(t)\le1
$$

and:

$$
\boxed{
\|S(t)\|_{\dot H^1}
\text{ is nonincreasing}.
}
\tag{8.3}
$$

This recovers the Miller-type model-cone regularity geometry.

But (4.3) shows that what truly controls the growth is:

$$
\alpha_\nu,
$$

while:

$$
\chi_\nu
$$

is merely the Cauchy upper envelope.

Therefore:

$$
\boxed{
\text{amplitude ratio } \chi_\nu
}
$$

is not the minimal growth carrier.

What is sharper is:

$$
\boxed{
\alpha_\nu
=
\chi_\nu c.
}
$$

---

# 9. Equality rigidity inside the closed cone

Suppose on the interval:

$$
[a,b]
$$

:

$$
\chi_\nu\le1
$$

a.e., and:

$$
\|S(b)\|_{\dot H^1}
=
\|S(a)\|_{\dot H^1}.
$$

From (4.4):

$$
0
=
\int_a^b
\nu(1-\alpha_\nu)D^2dt.
$$

Since:

$$
\alpha_\nu
\le
\chi_\nu
\le1,
$$

we obtain that where:

$$
D>0
$$

:

$$
\boxed{
\alpha_\nu=1.
}
$$

Therefore:

$$
\boxed{
\chi_\nu=1,
\qquad
c=1.
}
\tag{9.1}
$$

Cauchy equality forces:

$$
\boxed{
\mathcal R
=
-\nu B
=
\nu\Delta S.
}
\tag{9.2}
$$

which is the general-viscosity model-cone equality.

Substituting back into (1.1):

$$
\partial_tS
-
\nu\Delta S
-
\frac12P_{st}(\omega\otimes\omega)
+
\nu\Delta S
=
0,
$$

Thus:

$$
\boxed{
\partial_tS
=
\frac12
P_{st}(\omega\otimes\omega).
}
\tag{9.3}
$$

---

# 10. Equality-collapse theorem

Pairing (9.3) with $S$:

$$
\frac12
\frac d{dt}
\|S\|_2^2
=
\frac12
\langle
S,\omega\otimes\omega
\rangle.
$$

Using the exact identity:

$$
\boxed{
\langle
S,\omega\otimes\omega
\rangle
=
-4
\int\det S\,dx,
}
\tag{10.1}
$$

Yields:

$$
\boxed{
\frac d{dt}
\|S\|_2^2
=
-4
\int\det S\,dx.
}
\tag{10.2}
$$

But the full Navier–Stokes equations simultaneously satisfy:

$$
\boxed{
\frac d{dt}
\|S\|_2^2
=
-2\nu
\|S\|_{\dot H^1}^2
-
4
\int\det S\,dx.
}
\tag{10.3}
$$

Comparing (10.2) and (10.3):

$$
\boxed{
\|S\|_{\dot H^1}=0.
}
\tag{10.4}
$$

Therefore $S$ is spatially constant.

In the:

$$
S\in L^2(\mathbb R^3)
$$

class:

$$
\boxed{
S\equiv0.
}
\tag{10.5}
$$

Therefore:

$$
\boxed{
\textbf{
a nontrivial finite-energy Navier–Stokes state cannot execute
an exact equal-$\dot H^1$ return inside }\chi_\nu\le1.
}
}
\tag{10.6}
$$

This reconnects with the previous model-cone equality collapse of MORP/DCRP, but in this round it is obtained directly via the Pure-C projection/cancellation route.

---

# 11. Strict Lyapunov corollary

For a nontrivial finite-energy whole-space solution, if:

$$
\chi_\nu(t)\le1
$$

on the interval:

$$
[a,b],
$$

then:

$$
\|S(t)\|_{\dot H^1}
$$

cannot be nonincreasing and then exactly return to its original value over a nonzero interval.

Otherwise, Sections 9–10 force:

$$
S\equiv0.
$$

Therefore, inside the closed cone:

$$
\boxed{
\|S\|_{\dot H^1}^2
}
$$

is a strict Lyapunov quantity for the nontrivial branch in the endpoint-return sense.

---

# 12. Remove the explicit vorticity tensor from the H¹ growth driver

From (1.2):

$$
\mathcal R
=
P_{st}
\left(
(u\cdot\nabla)S
+
S^2
+
\frac34
\omega\otimes\omega
\right).
$$

Since:

$$
B\in L^2_{st},
$$

the projection can be removed from the pairing:

$$
\langle\mathcal R,B\rangle
=
\left\langle
(u\cdot\nabla)S
+
S^2
+
\frac34\omega\otimes\omega,
B
\right\rangle.
$$

Then from:

$$
\langle
\omega\otimes\omega,
B
\rangle
=
0,
$$

we obtain:

$$
\boxed{
\langle\mathcal R,B\rangle
=
\left\langle
(u\cdot\nabla)S
+
S^2,
B
\right\rangle.
}
\tag{12.1}
$$

So the exact dangerous projection of the full NS strain-$\dot H^1$ growth depends only on:

$$
\boxed{
(u\cdot\nabla)S
+
S^2
}
$$

in the direction of:

$$
-\Delta S
$$

.

Both the pressure and the explicit $\omega\otimes\omega$ have exactly disappeared from this growth observable.

---

# 13. Localize the advection pairing without discrete decomposition

Consider:

$$
I_{\rm adv}
=
\left\langle
(u\cdot\nabla)S,
-\Delta S
\right\rangle.
$$

Writing in components:

$$
I_{\rm adv}
=
\int
u_j
\partial_jS_{ab}
(-\partial_{kk}S_{ab})
\,dx.
$$

Integration by parts with respect to $x_k$:

$$
I_{\rm adv}
=
\int
\partial_k u_j
\,
\partial_jS_{ab}
\,
\partial_kS_{ab}
\,dx
+
\frac12
\int
u_j
\partial_j
|\partial_kS|^2
\,dx.
$$

The second term vanishes due to:

$$
\nabla\cdot u=0
$$

.

Define the Gram tensor:

$$
\boxed{
M_{jk}
=
\partial_jS:\partial_kS.
}
\tag{13.1}
$$

Then:

$$
M^\top=M,
$$

and for any:

$$
v\in\mathbb R^3,
$$

$$
v^\top Mv
=
\left|
\sum_jv_j\partial_jS
\right|^2
\ge0.
$$

Therefore:

$$
\boxed{
M\succeq0.
}
\tag{13.2}
$$

Also:

$$
\partial_ku_j
=
S_{jk}
+
\Omega_{jk}.
$$

Since:

$$
M
$$

is symmetric,

$$
\Omega:M=0.
$$

Therefore:

$$
\boxed{
I_{\rm adv}
=
\int
S:M
\,dx.
}
\tag{13.3}
$$

This is a completely local continuous identity.

---

# 14. Localize the strain self-amplification pairing

Let:

$$
H_k
=
\partial_kS.
$$

Since $S$ is symmetric:

$$
H_k^\top=H_k.
$$

Consider:

$$
I_{\rm self}
=
\langle
S^2,
-\Delta S
\rangle.
$$

Integration by parts:

$$
I_{\rm self}
=
\sum_k
\int
\partial_k(S^2):\partial_kS
\,dx.
$$

And:

$$
\partial_k(S^2)
=
H_kS
+
SH_k.
$$

Therefore:

$$
\partial_k(S^2):H_k
=
2
\operatorname{tr}
(SH_k^2).
$$

Thus:

$$
\boxed{
I_{\rm self}
=
2
\int
S:
\left(
\sum_kH_k^2
\right)
dx.
}
\tag{14.1}
$$

Each:

$$
H_k^2
$$

is positive semidefinite.

---

# 15. NEW exact carrier — gradient-stress tensor

Define:

$$
\boxed{
G[S]
=
M
+
2
\sum_{k=1}^3
H_k^2.
}
\tag{15.1}
$$

From Sections 13–14:

$$
M\succeq0,
$$

and:

$$
H_k^2\succeq0.
$$

Thus:

$$
\boxed{
G[S]\succeq0.
}
\tag{15.2}
$$

Furthermore:

$$
\operatorname{tr}M
=
|\nabla S|^2,
$$

and:

$$
\operatorname{tr}
\left(
\sum_kH_k^2
\right)
=
|\nabla S|^2.
$$

Therefore:

$$
\boxed{
\operatorname{tr}G
=
3|\nabla S|^2.
}
\tag{15.3}
$$

From (12.1), (13.3), and (14.1):

$$
\boxed{
\langle
\mathcal R,B
\rangle
=
\int
S:G[S]
\,dx.
}
\tag{15.4}
$$

Substituting back into the exact H¹ balance:

$$
\boxed{
\frac12
\frac d{dt}
\|S\|_{\dot H^1}^2
+
\nu
\|-\Delta S\|_2^2
=
-
\int
S:G[S]
\,dx.
}
\tag{15.5}
$$

This is the most important exact identity of this round.

---

# 16. Gradient-weighted strain scalar

Where:

$$
|\nabla S|>0
$$

, define the normalized gradient-stress state:

$$
\boxed{
W
=
\frac{
G[S]
}{
\operatorname{tr}G[S]
}.
}
\tag{16.1}
$$

Then:

$$
W\succeq0,
$$

$$
\operatorname{tr}W=1.
$$

Define:

$$
\boxed{
\Lambda_G
=
-
S:W.
}
\tag{16.2}
$$

If:

$$
|\nabla S|=0,
$$

let:

$$
\Lambda_G=0.
$$

From:

$$
G=3|\nabla S|^2W,
$$

we obtain:

$$
\boxed{
-
S:G
=
3
\Lambda_G
|\nabla S|^2.
}
\tag{16.3}
$$

So (15.5) becomes:

$$
\boxed{
\frac12
\frac d{dt}
\|S\|_{\dot H^1}^2
+
\nu
\|-\Delta S\|_2^2
=
3
\int
\Lambda_G
|\nabla S|^2
\,dx.
}
\tag{16.4}
$$

This re-expresses the strain-$\dot H^1$ nonlinear growth of the full NS equations as:

$$
\boxed{
\text{gradient energy}
\times
\text{gradient-weighted strain geometry}.
}
$$

---

# 17. Spectral meaning of $\Lambda_G$

In the eigenbasis of $S$:

$$
Se_i
=
\lambda_ie_i,
$$

Define:

$$
w_i
=
e_i^\top We_i.
$$

Since:

$$
W\succeq0,
$$

$$
\operatorname{tr}W=1,
$$

we have:

$$
w_i\ge0,
$$

$$
w_1+w_2+w_3=1.
$$

Therefore:

$$
\boxed{
\Lambda_G
=
-
\sum_{i=1}^3
w_i\lambda_i.
}
\tag{17.1}
$$

So:

$$
\boxed{
-\lambda_3
\le
\Lambda_G
\le
-\lambda_1.
}
\tag{17.2}
$$

Dangerous positive:

$$
\Lambda_G>0
$$

indicates that the gradient-stress tensor:

$$
W
$$

is more biased towards the compressive eigendirections of the strain in an average sense.

Regularizing negative:

$$
\Lambda_G<0
$$

indicates that the gradient stress is more biased towards the extensional eigendirections.

Therefore, this round yields a new geometric interpretation:

$$
\boxed{
\textbf{
H¹ strain growth is driven by alignment of strain-gradient stress
with compressive strain directions.
}
}
\tag{17.3}
$$

---

# 18. Exact relation between $\alpha_\nu$ and $\Lambda_G$

From (4.3) and (15.4):

$$
\alpha_\nu
=
-
\frac{
\int S:G\,dx
}{
\nu
\|-\Delta S\|_2^2
}.
$$

Then using (16.3):

$$
\boxed{
\alpha_\nu(t)
=
\frac{
3
\int
\Lambda_G
|\nabla S|^2dx
}{
\nu
\|-\Delta S\|_2^2
}.
}
\tag{18.1}
$$

So the residual amplitude/alignment scalar:

$$
\alpha_\nu
$$

has a completely local continuous integral representation.

This means:

> the global projection did not permanently erase the relational geometry required for H¹ growth.

Conversely:

$$
\boxed{
\text{projection/cancellation}
\longrightarrow
\text{new local relational carrier } \Lambda_G.
}
\tag{18.2}
$$

---

# 19. X-integral observation resolution cycle

Round 03 proved in:

$$
\Gamma_{\rm amp}
$$

:

$$
\boxed{
\mathsf X_{\Gamma_{\rm amp}}
}
$$

because a single amplitude:

$$
|S|
$$

cannot preserve the nonlinear sign.

But this round first performs:

$$
\int_{\rm projection}
\int_{\rm cancellation}
\int_{\rm gradient\ relation}
X_{\rm geom},
$$

then observes:

$$
\Lambda_G
$$

and:

$$
\alpha_\nu.
$$

For the target observable:

$$
\frac d{dt}
\|S\|_{\dot H^1}^2,
$$

the single scalar:

$$
\boxed{
\alpha_\nu
}
$$

is already sufficient.

Therefore, the 24 observation state can occur as:

$$
\boxed{
\mathsf C_{\rm amplitude}
\to
\mathsf X_{\Gamma_{\rm amp}}
\to
\mathsf C_{\rm growth}
}
\tag{19.1}
$$

But the former and latter:

$$
\mathsf C
$$

are not the same observation.

The first only reads the amplitude.

The second is a targeted sufficient scalar formed only after X-integrating more relational structure.

This exactly demonstrates:

$$
\boxed{
\textbf{
Refusal of a single measure can be resolved by structural integration
before re-observation.
}
}
\tag{19.2}
$$

---

# 20. Critical smallness criterion for the new carrier

From:

$$
\Lambda_G
\le
(-\lambda_1)^+
$$

and (16.4):

$$
\frac12A'
+
\nu D^2
\le
3
\int
\Lambda_G^+
|\nabla S|^2dx.
$$

Hölder:

$$
\int
\Lambda_G^+
|\nabla S|^2
\le
\|\Lambda_G^+\|_{L^{3/2}}
\|\nabla S\|_{L^6}^2.
$$

Sobolev:

$$
\|\nabla S\|_{L^6}
\le
C
\|\Delta S\|_2.
$$

Thus:

$$
\boxed{
\frac12A'
+
\left(
\nu
-
C
\|\Lambda_G^+\|_{L^{3/2}}
\right)
D^2
\le0.
}
\tag{20.1}
$$

Therefore if:

$$
\boxed{
\sup_{t<T}
\|\Lambda_G^+(t)\|_{L^{3/2}}
<
\frac{\nu}{C},
}
\tag{20.2}
$$

then:

$$
A(t)
$$

is nonincreasing.

$L^{3/2}$ is the scale-critical Lebesgue exponent for the strain, because:

$$
S_\lambda(x,t)
=
\lambda^2
S(\lambda x,\lambda^2t)
$$

and:

$$
\|S_\lambda\|_{L^{3/2}}
=
\|S\|_{L^{3/2}}.
$$

Therefore (20.2) is a critical geometric smallness condition.

This document does not claim this criterion is novel in the literature; it is merely a direct consequence of the new carrier representation.

---

# 21. What has actually been eliminated

The main suspicion of Round 04:

> the pressure Hessian might be an ineliminable obstruction for the pure continuous geometry route.

Round 05 shows that, for:

$$
\boxed{
\dot H^1\text{ strain growth}
}
$$

this specific target, that suspicion is wrong.

The pressure can be removed by exact projection/cancellation.

The explicit:

$$
\omega\otimes\omega
$$

is also removed by orthogonality.

Therefore:

$$
\boxed{
\text{STOP-C07}
}
$$

is not the final barrier for the H¹ growth route.

It still holds for pointwise spectrum evolution, but can be bypassed by another continuous X route.

This is exactly what this experiment demands:

$$
\boxed{
\text{One blocked route}
\neq
\text{All routes blocked under the same substrate}.
}
$$

---

# 22. New STOP — gradient-alignment coercivity

Even with the exact identity:

$$
\frac12A'
+
\nu D^2
=
3
\int
\Lambda_G
|\nabla S|^2,
$$

we still cannot unconditionally deduce from standard NS constraints that:

$$
3
\int
\Lambda_G
|\nabla S|^2
\le
\nu D^2.
$$

That is, we have not yet proven:

$$
\boxed{
\alpha_\nu\le1.
}
$$

holds for all smooth NS states.

And if:

$$
\|\Lambda_G^+\|_{3/2}
$$

only obtains finite-but-large control, smallness absorption fails again.

Therefore, the new main STOP for this round is:

$$
\boxed{
\textbf{STOP-C09:
Gradient-Stress / Compressive-Alignment Coercivity Gap}.
}
\tag{22.1}
$$

It is sharper than STOP-C07:

Not the pressure itself,

Not a single amplitude,

Not a local eigenvalue.

Rather:

$$
\boxed{
\text{Can the weighted alignment of strain gradients with compressive eigendirections be unconditionally constrained by NS dynamics?}
}
$$

---

# 23. No essential discrete intrusion yet

All objects in this round:

$$
P_{st},
$$

$$
S,
$$

$$
\omega,
$$

$$
-\Delta S,
$$

$$
M,
$$

$$
G,
$$

$$
W,
$$

$$
\Lambda_G,
$$

$$
\alpha_\nu,
$$

$$
\mathfrak G(T)
$$

can all be defined within a continuous deterministic framework.

Therefore:

$$
\boxed{
T_{\mathsf C\to\mathsf D}
=
\text{NOT YET REACHED}.
}
\tag{23.1}
$$

Instead, the Pure-C route has currently traversed:

$$
\boxed{
\begin{aligned}
\mathsf C_{\rm energy}
&\to
\mathsf C_{\rm critical}
\\
&\to
\mathsf C_{\rm relational}
\\
&\to
\mathsf C_{\rm nonlocal}
\\
&\to
\mathsf C_{\rm projected}
\\
&\to
\mathsf C_{\rm gradient\ geometry}.
\end{aligned}
}
\tag{23.2}
$$

---

# 24. 24/72 Ledger — Round 05

| Step | X object / operation | $B$ | $U$ | $O$ | $L$ | status |
|---|---|---|---|---|---|---|
| C41 | $P_{st}$ full strain equation | $\mathsf C$ | $\mathsf P$ constraint | $\mathsf X$ | $\mathsf F$ | FORM |
| C42 | $\langle-\Delta S,\omega\otimes\omega\rangle=0$ | $\mathsf C$ | projection | targeted | $\mathsf F$ | EXACT |
| C43 | H¹ strain balance | $\mathsf C$ | $\mathsf S/\mathsf P$ | targeted | $\mathsf F$ | EXACT |
| C44 | residual amplitude $\chi_\nu$ | $\mathsf C$ | $\mathsf R$ meta-observation | scalar | $\mathsf F$ | FORM |
| C45 | dangerous alignment $c$ | $\mathsf C$ | relational | scalar | $\mathsf F$ | FORM |
| C46 | $\alpha_\nu=\chi_\nu c$ | $\mathsf C$ | relational | scalar sufficient for H¹ growth | $\mathsf F$ | EXACT |
| C47 | model-cone equality collapse | $\mathsf C$ | recurrent/equality | scalar + relation | $\mathsf F$ | CLOSED branch |
| C48 | advection localization $I_{\rm adv}=S:M$ | $\mathsf C$ | $\mathsf S$ | relational | $\mathsf F$ | EXACT |
| C49 | self-interaction localization | $\mathsf C$ | $\mathsf S$ | relational | $\mathsf F$ | EXACT |
| C50 | gradient-stress tensor $G$ | $\mathsf C$ | $\mathsf P$ local relation | $\mathsf X$ | $\mathsf F$ | FORM |
| C51 | normalized $W$ and $\Lambda_G$ | $\mathsf C$ | relational | targeted scalar | $\mathsf F$ | FORM |
| C52 | exact gradient-alignment law | $\mathsf C$ | hybrid | targeted scalar | $\mathsf F$ | EXACT |
| C53 | unconditional $\alpha_\nu\le1$ | $\mathsf C$ | — | targeted scalar | $\mathsf F$ | OPEN / STOP-C09 |

---

# 25. X diagnostic object

$$
\boxed{
\bot_X^{\mathrm{C09}}
=
\left\langle
\begin{array}{l}
\text{layer}
=
\mathrm{H^1\ strain\ geometric\ coercivity},
\\
\text{exact\ driver}
=
3\int\Lambda_G|\nabla S|^2,
\\
\text{dissipation}
=
\nu\|\Delta S\|_2^2,
\\
\text{required}
=
\alpha_\nu\le1
\text{ or integrable positive excess},
\\
\text{pressure}
=
\mathrm{eliminated},
\\
\text{explicit vorticity tensor}
=
\mathrm{eliminated},
\\
\text{remaining obstruction}
=
\mathrm{compressive\ gradient\ alignment},
\\
\text{discrete intrusion}
=
\mathrm{false}.
\end{array}
\right\rangle.
}
$$

---

# 26. Strongest result of Round 05

The strongest exact identity is:

$$
\boxed{
\frac12
\frac d{dt}
\|S\|_{\dot H^1}^2
+
\nu
\|-\Delta S\|_2^2
=
3
\int
\Lambda_G
|\nabla S|^2dx,
}
\tag{26.1}
$$

where:

$$
G
=
M
+
2
\sum_k(\partial_kS)^2
\succeq0,
$$

$$
M_{jk}
=
\partial_jS:\partial_kS,
$$

$$
W
=
\frac{G}{\operatorname{tr}G},
$$

$$
\Lambda_G
=
-S:W.
$$

Equivalently:

$$
\boxed{
\alpha_\nu
=
\frac{
3\int
\Lambda_G|\nabla S|^2dx
}{
\nu\|-\Delta S\|_2^2
}.
}
\tag{26.2}
$$

Thus the Pure-C proof frontier is now:

$$
\boxed{
\textbf{
Can Navier–Stokes dynamics prevent
gradient stress from becoming too strongly aligned
with compressive strain directions?
}
}
\tag{26.3}
$$

---

# 27. Next round — Dynamics of $\Lambda_G$ / $\alpha_\nu$

The next round will not return to pressure.

It will directly attack the new carrier:

$$
\boxed{
\Lambda_G
}
$$

and:

$$
\boxed{
\alpha_\nu.
}
$$

We need to determine:

1. Whether a restoring term exists in the material evolution of $\Lambda_G$;
2. Whether the evolution of $W$ possesses a positivity / trace-one structure that can be utilized;
3. Whether diffusion forces the gradient-stress orientation to mix;
4. Whether $\alpha_\nu>1$ can be sustained for a long time;
5. If differentiating $\alpha_\nu$ requires adding the infinite hierarchy of:

$$
\nabla^mS
$$

whether this forms the first true continuous-infinite closure obstruction;
6. If controlling the hierarchy requires switching to dyadic / countable scale extraction, only then formally record:

$$
T_{\mathsf C\to\mathsf D}.
$$

---

# 28. External primary-source anchors

1. Evan Miller, *On the interaction of strain and vorticity for solutions of the Navier--Stokes equation*, arXiv:2407.02691.
   - projected strain equation;
   - identity
   $$
   \langle-\Delta S,\omega\otimes\omega\rangle=0;
   $$
   - strain-vorticity interaction model;
   - residual/model-cone regularity ratios.

2. Evan Miller, *A regularity criterion for the Navier-Stokes equation involving only the middle eigenvalue of the strain tensor*, arXiv:1710.05569.
   - strain equation;
   - exact enstrophy identity;
   - scale-critical middle-eigenvalue criterion.

3. Borys Álvarez-Samaniego, Wilson P. Álvarez-Samaniego, Pedro G. Fernández-Dalgo, *On the use of the Riesz transforms to determine the pressure term in the incompressible Navier-Stokes equations on the whole space*, arXiv:2004.02588.
   - whole-space pressure reconstruction by Riesz transforms.

---

# 29. Commit state

$$
\boxed{
\begin{aligned}
\text{Route}
&:
\mathrm{Pure\ Continuous\ Nonlocal\ Cancellation},
\\
\text{Essential } \mathsf C\to\mathsf D
&:
\mathrm{Not\ reached},
\\
\text{Pressure obstruction at H¹ growth}
&:
\mathrm{removed},
\\
\text{Explicit }\omega\otimes\omega\text{ obstruction}
&:
\mathrm{removed\ from\ H^1\ growth},
\\
\text{New exact scalar}
&:
\alpha_\nu,
\\
\text{New local relational carrier}
&:
\Lambda_G,
\\
\text{Model-cone equality branch}
&:
\mathrm{collapses\ to\ triviality},
\\
\text{STOP-C09}
&:
\mathrm{Gradient\text{-}Stress/Compressive\text{-}Alignment\ Coercivity},
\\
\text{Next}
&:
\mathrm{Dynamics\ of\ }\Lambda_G\mathrm{\ and\ }\alpha_\nu.
\end{aligned}
}
$$