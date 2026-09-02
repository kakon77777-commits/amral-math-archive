# NS-DCRP-03 — Logarithmic Model-Cone Debt and Scale-Return Exclusion

- date: 2026-08-16
- status: research proof checkpoint
- canonical source: UTF-8 Markdown
- canonical math delimiters: `$...$` and `$$...$$`
- objective: replace the failed raw-tax accumulation route by a scale-invariant logarithmic cone-debt identity and test it directly against MORP recurrent returns.
- no new detector taxonomy is introduced.
- primary external source: Evan Miller, *On the interaction of strain and vorticity for solutions of the Navier--Stokes equation*, arXiv:2407.02691, v2.

---

# 1. Executive result

The previous checkpoint identified two difficulties:

1. scale-normalized recurrence does not imply raw endpoint kinetic-energy equality;
2. a fixed scale-critical raw toll can remain geometrically summable.

This round resolves both issues at once by using the exact strain balance at the logarithmic level.

Let

$$
S=\nabla_{\rm sym}u,
$$

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
\right),
$$

and define

$$
H(t)
=
\|S(t)\|_{\dot H^1}^2,
$$

$$
Z(t)
=
\|-\Delta S(t)\|_2.
$$

Miller's exact identity gives

$$
\frac12H'(t)
+
Z(t)^2
=
-
\langle
-\Delta S(t),
Q(t)
\rangle.
$$

Define

$$
\chi(t)
=
\frac{\|Q(t)\|_2}{Z(t)}
$$

when

$$
Z(t)>0.
$$

The new scale-invariant instantaneous cone debt is

$$
\boxed{
\tau_{SV}(t)
=
\frac{
(\chi(t)-1)_+
Z(t)^2
}{
H(t)
}.
}
$$

Equivalently,

$$
\boxed{
\tau_{SV}(t)
=
\frac{
(\|Q(t)\|_2-Z(t))_+
Z(t)
}{
H(t)
}.
}
$$

Then:

$$
\boxed{
\frac12
\frac d{dt}
\log H(t)
\le
\tau_{SV}(t).
}
$$

Consequently:

$$
\boxed{
H(t)
\le
H(t_0)
\exp
\left(
2
\int_{t_0}^{t}
\tau_{SV}(s)\,ds
\right).
}
$$

Therefore every finite-time blowup in the regularity class for which

$$
H(t)\to\infty
$$

must satisfy

$$
\boxed{
\int_{t_0}^{T_{\max}}
\tau_{SV}(t)\,dt
=
+\infty.
}
$$

This quantity is exactly invariant under Navier--Stokes parabolic scaling.

More strongly, if an actual return changes scale by a factor

$$
\lambda>1
$$

and the two endpoint states agree modulo the admissible scaling / translation / rotation symmetries, then

$$
\boxed{
\int_a^b
\tau_{SV}(t)\,dt
\ge
\frac32
\log\lambda.
}
$$

Hence:

$$
\boxed{
\textbf{
a nontrivial scale-changing return can never be a zero model-cone-debt return.
}
}
$$

This directly attacks the MORP discrete renormalization fixed-point branch without requiring raw endpoint equality.

---

# 2. Exact strain balance

For a sufficiently regular incompressible Navier--Stokes solution on

$$
\mathbb R^3,
$$

write

$$
S
=
\nabla_{\rm sym}u
$$

and

$$
\omega
=
\nabla\times u.
$$

Miller writes the exact strain equation as

$$
\boxed{
\partial_tS
-
\Delta S
-
\frac12
P_{st}
(
\omega\otimes\omega
)
+
Q
=
0,
}
\tag{2.1}
$$

where

$$
\boxed{
Q
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
\tag{2.2}
$$

The key orthogonality is

$$
\boxed{
\langle
-\Delta S,
\omega\otimes\omega
\rangle
=
0.
}
\tag{2.3}
$$

Pairing (2.1) with

$$
-\Delta S
$$

therefore yields

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
-\Delta S,
Q
\rangle.
}
\tag{2.4}
$$

This identity is exact.

---

# 3. Definition of logarithmic model-cone debt

Define

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

On a nontrivial singular branch,

$$
H(t)>0
$$

on a sufficiently late interval; otherwise

$$
S=0
$$

in the corresponding finite-energy strain class and the branch is regular/trivial.

When

$$
Z(t)>0,
$$

define the Miller cone ratio

$$
\chi(t)
=
\frac{
\|Q(t)\|_2
}{
Z(t)
}.
$$

If

$$
Z(t)=0,
$$

set

$$
\tau_{SV}(t)=0.
$$

For

$$
Z(t)>0,
$$

define

$$
\boxed{
\tau_{SV}(t)
=
\frac{
(\chi(t)-1)_+
Z(t)^2
}{
H(t)
}.
}
\tag{3.1}
$$

Because

$$
(\chi-1)_+Z^2
=
(\|Q\|_2-Z)_+Z,
$$

one may equivalently write

$$
\boxed{
\tau_{SV}(t)
=
\frac{
(\|Q(t)\|_2-Z(t))_+
Z(t)
}{
H(t)
}.
}
\tag{3.2}
$$

This is nonnegative.

The associated interval debt is

$$
\boxed{
\mathfrak D_{SV}[a,b]
=
\int_a^b
\tau_{SV}(t)\,dt.
}
\tag{3.3}
$$

---

# 4. Theorem — Logarithmic cone-growth inequality

## Theorem 4.1

Let

$$
u
$$

be a sufficiently regular Navier--Stokes solution on

$$
[a,b]
$$

such that

$$
0<H(t)<\infty
$$

and the quantities in (2.4) are integrable.

Then

$$
\boxed{
\frac12
\frac d{dt}
\log H(t)
\le
\tau_{SV}(t)
}
\tag{4.1}
$$

for almost every

$$
t\in[a,b].
$$

Hence

$$
\boxed{
\frac12
\log
\frac{H(b)}{H(a)}
\le
\mathfrak D_{SV}[a,b].
}
\tag{4.2}
$$

Equivalently,

$$
\boxed{
H(b)
\le
H(a)
\exp
\left(
2\mathfrak D_{SV}[a,b]
\right).
}
\tag{4.3}
$$

### Proof

From (2.4),

$$
\frac12H'
=
-Z^2
-
\langle
-\Delta S,Q
\rangle.
$$

By Cauchy--Schwarz,

$$
-
\langle
-\Delta S,Q
\rangle
\le
Z\|Q\|_2.
$$

Therefore

$$
\frac12H'
\le
-Z^2
+
Z\|Q\|_2.
$$

Thus

$$
\frac12H'
\le
(\chi-1)Z^2.
$$

Since

$$
(\chi-1)Z^2
\le
(\chi-1)_+Z^2,
$$

we obtain

$$
\frac12H'
\le
(\chi-1)_+Z^2.
$$

Divide by

$$
H>0:
$$

$$
\frac12
\frac{H'}{H}
\le
\frac{
(\chi-1)_+Z^2
}{
H
}.
$$

Hence

$$
\frac12
\frac d{dt}
\log H
\le
\tau_{SV}.
$$

Integrating gives (4.2), and exponentiating gives (4.3).

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

# 5. Corollary — finite logarithmic cone debt is a regularity criterion

Miller records that for a maximal

$$
H^3_{df}
$$

mild Navier--Stokes solution, if

$$
T_{\max}<\infty,
$$

then the subcritical strain norm obeys

$$
\boxed{
\lim_{t\uparrow T_{\max}}
\|S(t)\|_{\dot H^1}
=
+\infty.
}
\tag{5.1}
$$

Therefore Theorem 4.1 immediately gives:

## Corollary 5.1

If for some

$$
t_0<T_{\max}
$$

one has

$$
\boxed{
\int_{t_0}^{T_{\max}}
\tau_{SV}(t)\,dt
<
\infty,
}
\tag{5.2}
$$

then

$$
T_{\max}
$$

cannot be a finite blowup time.

Equivalently, finite-time blowup forces

$$
\boxed{
\int_{t_0}^{T_{\max}}
\tau_{SV}(t)\,dt
=
+\infty
}
\tag{5.3}
$$

for every sufficiently late

$$
t_0<T_{\max}.
$$

### Proof

If (5.2) holds, (4.3) gives a uniform bound

$$
H(t)
\le
H(t_0)
\exp
\left(
2
\int_{t_0}^{T_{\max}}
\tau_{SV}
\right)
<
\infty.
$$

This contradicts (5.1).

$$
\square
$$

Status:

$$
\boxed{
\textbf{PROVED in the stated maximal mild-solution class}.
}
$$

---

# 6. Scale invariance

The Navier--Stokes scaling is

$$
u_\lambda(x,t)
=
\lambda
u(\lambda x,\lambda^2t).
$$

The strain scales as

$$
S_\lambda(x,t)
=
\lambda^2
S(\lambda x,\lambda^2t).
$$

Therefore

$$
H_\lambda(t)
=
\|S_\lambda(t)\|_{\dot H^1}^2
=
\lambda^3
H(\lambda^2t).
\tag{6.1}
$$

Also,

$$
-\Delta S_\lambda
=
\lambda^4
(-\Delta S)(\lambda x,\lambda^2t),
$$

so

$$
Z_\lambda(t)^2
=
\lambda^5
Z(\lambda^2t)^2.
\tag{6.2}
$$

Every term in

$$
Q
$$

has the same pointwise scaling degree as

$$
\Delta S,
$$

hence

$$
\|Q_\lambda(t)\|_2^2
=
\lambda^5
\|Q(\lambda^2t)\|_2^2.
\tag{6.3}
$$

Thus

$$
\boxed{
\chi_\lambda(t)
=
\chi(\lambda^2t).
}
\tag{6.4}
$$

Using (6.1) and (6.2),

$$
\tau_{SV,\lambda}(t)
=
\lambda^2
\tau_{SV}(\lambda^2t).
$$

Therefore

$$
\tau_{SV,\lambda}(t)\,dt
=
\tau_{SV}(s)\,ds,
\qquad
s=\lambda^2t.
$$

Hence:

$$
\boxed{
\mathfrak D_{SV}
\text{ is exactly parabolic-scale invariant}.
}
\tag{6.5}
$$

This is the key improvement over raw dissipation debt.

The earlier geometric-summability obstruction does not apply to

$$
\mathfrak D_{SV},
$$

because the normalization by

$$
H
$$

converts the growth estimate into a logarithmic, dimensionless quantity.

---

# 7. Theorem — Scale-Return Cone Debt

## Theorem 7.1

Let

$$
u
$$

be a sufficiently regular Navier--Stokes solution on an actual physical interval

$$
[a,b].
$$

Assume the endpoint strain states are related by a nontrivial Navier--Stokes parabolic scaling with factor

$$
\lambda>1,
$$

up to translations and orthogonal spatial rotations, which preserve the relevant homogeneous Sobolev norms.

Thus schematically,

$$
S(b)
=
\mathcal G
\mathcal S_\lambda
S(a),
$$

where

$$
\mathcal G
$$

is an allowed norm-preserving Euclidean symmetry and

$$
\mathcal S_\lambda S(x)
=
\lambda^2S(\lambda x).
$$

Then

$$
\boxed{
H(b)
=
\lambda^3H(a).
}
\tag{7.1}
$$

Consequently,

$$
\boxed{
\mathfrak D_{SV}[a,b]
\ge
\frac32
\log\lambda.
}
\tag{7.2}
$$

### Proof

By the scaling law (6.1) and norm preservation of translations/rotations,

$$
H(b)
=
\lambda^3H(a).
$$

Apply Theorem 4.1:

$$
\mathfrak D_{SV}[a,b]
\ge
\frac12
\log
\frac{H(b)}{H(a)}.
$$

Using (7.1),

$$
\mathfrak D_{SV}[a,b]
\ge
\frac12
\log(\lambda^3).
$$

Therefore

$$
\boxed{
\mathfrak D_{SV}[a,b]
\ge
\frac32\log\lambda.
}
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

# 8. Immediate exclusion — zero-debt nontrivial scale return

If

$$
\lambda>1,
$$

then

$$
\frac32\log\lambda>0.
$$

Therefore Theorem 7.1 gives:

$$
\boxed{
\lambda>1
\Longrightarrow
\mathfrak D_{SV}[a,b]>0.
}
\tag{8.1}
$$

Hence:

$$
\boxed{
\textbf{
there is no nontrivial finite-$\dot H^1$ actual scale-changing return with zero logarithmic model-cone debt.
}
}
\tag{8.2}
$$

This conclusion does not require:

$$
\|S(a)\|_{\dot H^1}
=
\|S(b)\|_{\dot H^1}.
$$

It therefore removes the normalization mismatch that blocked the previous MORP-04 endpoint-equality route.

---

# 9. Variable-scale return orbit

Consider a sequence of actual return times

$$
t_0<t_1<t_2<\cdots<T
$$

with return scale factors

$$
\lambda_k>1
$$

such that

$$
S(t_{k+1})
=
\mathcal G_k
\mathcal S_{\lambda_k}
S(t_k).
$$

Then Theorem 7.1 gives

$$
\mathfrak D_{SV}[t_k,t_{k+1}]
\ge
\frac32
\log\lambda_k.
$$

Summing,

$$
\boxed{
\sum_{k=0}^{N-1}
\mathfrak D_{SV}[t_k,t_{k+1}]
\ge
\frac32
\sum_{k=0}^{N-1}
\log\lambda_k
=
\frac32
\log
\left(
\prod_{k=0}^{N-1}
\lambda_k
\right).
}
\tag{9.1}
$$

If the total renormalization scale diverges,

$$
\prod_{k=0}^{\infty}\lambda_k
=
+\infty,
$$

then

$$
\boxed{
\sum_{k=0}^{\infty}
\mathfrak D_{SV}[t_k,t_{k+1}]
=
+\infty.
}
\tag{9.2}
$$

Thus the non-summability sought in earlier cycles is available in a genuinely scale-invariant logarithmic coordinate.

This does not by itself contradict blowup.

Rather, it proves that a blowup-compatible scale-return orbit must carry infinite model-cone debt and therefore cannot belong to a true zero-debt equality kernel.

---

# 10. Canonical realization of the MORP model-cone excess

MORP-01 introduced

$$
\mathcal M_{SV}(D)
$$

abstractly as a nonnegative lower-semicontinuous candidate channel measuring model-cone excess.

MORP-04 then used the closed model cone

$$
\chi_{SV}\le1
$$

as the corresponding equality regime.

The natural concrete realization on a finite-$\dot H^1$ return cycle is therefore:

$$
\boxed{
\mathcal M_{SV}^{\log}(D;[a,b])
:=
\mathfrak D_{SV}[a,b]
=
\int_a^b
\frac{
(\chi_{SV}-1)_+
\|-\Delta S\|_2^2
}{
\|S\|_{\dot H^1}^2
}
\,dt.
}
\tag{10.1}
$$

It has the required structural features:

1. nonnegative:

$$
\mathcal M_{SV}^{\log}\ge0;
$$

2. vanishes throughout the closed cone:

$$
\chi_{SV}\le1
\quad\Longrightarrow\quad
\mathcal M_{SV}^{\log}=0;
$$

3. exact parabolic scale invariance;

4. detects the minimum excess necessary for scale growth;

5. on an exact scale return:

$$
\boxed{
\mathcal M_{SV}^{\log}
\ge
\frac32\log\lambda.
}
$$

The remaining technical issue is not the analytic inequality.

It is whether

$$
\mathcal M_{SV}^{\log}
$$

is admissible in the precise MORP compactness topology and return package:

- lower semicontinuity;
- passage to profile limits;
- compatibility with actual/profile return realization.

That is a bridge problem.

The return obstruction itself is already quantified.

---

# 11. Conditional MORP closure theorem for an actual recurrent minimizer

## Theorem 11.1

Assume there exists a minimal MORP obstruction

$$
D_\ast
$$

with a finite-$\dot H^1$ state-visible component satisfying all of the following.

### A. Actual return realization

There is an actual same-history return interval

$$
[a,b]
$$

with a scale factor

$$
\lambda>1.
$$

### B. Exact recurrent state relation

The endpoint strain states satisfy

$$
S(b)
=
\mathcal G
\mathcal S_\lambda
S(a).
$$

### C. Model-cone kernel realization

The MORP zero-cost condition

$$
\mathcal M_{SV}(D_\ast)=0
$$

passes to the concrete logarithmic realization:

$$
\mathcal M_{SV}^{\log}(D_\ast;[a,b])=0.
$$

Then no such

$$
D_\ast
$$

exists.

### Proof

By Theorem 7.1,

$$
\mathcal M_{SV}^{\log}(D_\ast;[a,b])
\ge
\frac32
\log\lambda.
$$

Since

$$
\lambda>1,
$$

the right-hand side is strictly positive.

But assumption C gives

$$
\mathcal M_{SV}^{\log}(D_\ast;[a,b])=0.
$$

Contradiction.

$$
\square
$$

Therefore:

$$
\boxed{
\textbf{
the finite-$\dot H^1$ exact scale-recurrent state-visible branch is empty
once the abstract MORP model-cone kernel is legitimately realized by the logarithmic cone debt.
}
}
\tag{11.1}
$$

Status:

$$
\boxed{
\textbf{CONDITIONAL only on the stated MORP bridge assumptions}.
}
$$

The analytic scale-return inequality itself is unconditional in the stated smooth class.

---

# 12. Relationship to the previous Model-Cone Equality Collapse theorem

DCRP-02 proved, under its finite-enstrophy pairing assumptions,

$$
\mathcal R_{SV}
=
\Delta S
\Longrightarrow
\|S\|_{\dot H^1}=0.
$$

That theorem remains useful.

However DCRP-03 is stronger for scale-normalized recurrence because it does not require raw endpoint equality.

The two mechanisms are:

### Equality-collapse route

$$
\chi\le1
+
H(a)=H(b)
\Longrightarrow
\mathcal R_{SV}=\Delta S
\Longrightarrow
\|S\|_{\dot H^1}=0.
$$

### Log-debt route

$$
H(b)=\lambda^3H(a),
\qquad
\lambda>1
$$

directly gives

$$
\mathfrak D_{SV}[a,b]
\ge
\frac32\log\lambda>0.
$$

Thus the second route is naturally adapted to renormalization returns.

---

# 13. What has actually been removed

Before this round, a putative survivor could be described schematically as

$$
\text{finite-$\dot H^1$}
+
\text{scale recurrent}
+
\text{closed / zero-tax model cone}.
$$

That combination is now inconsistent.

The exact excluded conjunction is:

$$
\boxed{
\begin{aligned}
&\text{finite-$\dot H^1$ state-visible return}\\
&+
\text{actual exact parabolic scale return with }\lambda>1\\
&+
\text{zero logarithmic model-cone debt}
\end{aligned}
\Longrightarrow
\bot.
}
\tag{13.1}
$$

Hence a surviving singular recurrent obstruction must fail at least one bridge:

$$
\boxed{
\begin{aligned}
\text{G1: }&
\text{no actual exact scale return is realized};\\
\text{G2: }&
\text{the state-visible return loses finite }\dot H^1;\\
\text{G3: }&
\text{the abstract model-cone kernel does not pass to }
\mathcal M_{SV}^{\log};\\
\text{G4: }&
\text{the recurrence is only profile/shadow recurrence, not same-history recurrence}.
\end{aligned}
}
\tag{13.2}
$$

This is not introduced as a new taxonomy.

It is the explicit list of hypotheses required to block Theorem 11.1.

---

# 14. Stronger global statement — blowup forces infinite logarithmic model-cone excess

For emphasis, the main analytic statement can be written independently of MORP:

## Theorem 14.1

Let

$$
u\in C([0,T_{\max});H^3_{df})
$$

be a maximal mild three-dimensional Navier--Stokes solution.

Define

$$
S=\nabla_{\rm sym}u,
$$

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
\right),
$$

and

$$
\tau_{SV}
=
\frac{
(\|Q\|_2-\|-\Delta S\|_2)_+
\|-\Delta S\|_2
}{
\|S\|_{\dot H^1}^2
}.
$$

If

$$
T_{\max}<\infty,
$$

then

$$
\boxed{
\int_0^{T_{\max}}
\tau_{SV}(t)\,dt
=
+\infty.
}
\tag{14.1}
$$

More precisely, for every

$$
0<t_0<T_{\max},
$$

$$
\boxed{
\int_{t_0}^{T_{\max}}
\tau_{SV}(t)\,dt
=
+\infty.
}
\tag{14.2}
$$

This is a one-sided refinement of the qualitative threshold

$$
\limsup_{t\uparrow T_{\max}}
\chi_{SV}(t)\ge1.
$$

It does not merely require that the cone ratio touch or exceed one.

It requires the scale-invariant positive excess above one, weighted by

$$
\frac{
\|-\Delta S\|_2^2
}{
\|S\|_{\dot H^1}^2
},
$$

to have infinite total logarithmic debt.

---

# 15. Comparison with Miller's existing perturbative criterion

Miller proves for

$$
0\le\alpha\le1,
\qquad
p=\frac2{1+\alpha},
$$

that finite-time blowup forces divergence of a perturbative integral involving

$$
\frac{
\|Q\|_{\dot H^\alpha}^p
}{
\|S\|_{\dot H^1}^p
}.
$$

For

$$
\alpha=0,
$$

this controls

$$
\int
\frac{
\|Q\|_2^2
}{
\|S\|_{\dot H^1}^2
}
\,dt.
$$

The present cone-debt quantity is different:

$$
\frac{
(\|Q\|_2-Z)_+Z
}{
H
}.
$$

It discards the entire closed-cone region

$$
\|Q\|_2\le Z
$$

and charges only the portion of the perturbation that exceeds the dissipative threshold.

The proof is nevertheless an immediate consequence of the same exact strain balance and Cauchy--Schwarz mechanism.

No priority or novelty claim is made here.

For this project, its value is structural:

$$
\boxed{
\text{it is precisely aligned with the MORP model-cone equality/zero-cost architecture.}
}
$$

---

# 16. Lower-semicontinuity issue

To turn Theorem 11.1 into an unconditional MORP exclusion theorem, one must still show that

$$
\mathcal M_{SV}^{\log}
$$

survives the compactness and profile limits used to produce a minimizer.

The current MORP-02 compactness gives strong local convergence at the state level in

$$
L^3_{\rm loc},
$$

but the logarithmic cone debt contains

$$
\Delta S
$$

and the projected nonlinear residual

$$
Q.
$$

Therefore strong

$$
L^3_{\rm loc}
$$

convergence alone is insufficient to pass (10.1).

A sufficient stronger convergence package would be, on each finite return interval,

$$
S_n\to S
\quad
\text{strongly in }
L^\infty_t\dot H^1_x,
$$

together with

$$
\Delta S_n\to\Delta S
\quad
\text{strongly in }L^2_{t,x},
$$

and

$$
Q_n\to Q
\quad
\text{strongly in }L^2_{t,x}.
$$

Under such a package,

$$
\mathcal M_{SV}^{\log}(D_n)
\to
\mathcal M_{SV}^{\log}(D)
$$

away from the trivial

$$
H=0
$$

branch.

This strong package is not currently proved for the general MORP minimizer.

Hence the next obstruction is no longer an analytic cone-rigidity problem.

It is a compactness / transfer problem for a specific scale-invariant functional.

---

# 17. Next exact proof target

The next proof target is now:

$$
\boxed{
\textbf{Log-Cone Transfer Lemma}.
}
$$

Desired statement:

Let

$$
D_n\to D_\ast
$$

be the MORP minimizing sequence / return-profile convergence in the state-visible finite-$\dot H^1$ branch.

Prove enough compactness or lower-semicontinuity to obtain

$$
\boxed{
\mathcal M_{SV}^{\log}(D_\ast)
\le
\liminf_{n\to\infty}
\mathcal M_{SV}^{\log}(D_n).
}
\tag{17.1}
$$

Then if the minimizing branch has

$$
m_\ast=0
$$

and model-cone kernel saturation,

$$
\mathcal M_{SV}^{\log}(D_\ast)=0.
$$

If the same object is an actual nontrivial scale return with

$$
\lambda>1,
$$

Theorem 7.1 gives

$$
\mathcal M_{SV}^{\log}(D_\ast)
\ge
\frac32\log\lambda>0,
$$

contradiction.

Thus the desired closure chain is:

$$
\boxed{
\begin{aligned}
m_\ast=0
&\Longrightarrow
\mathcal M_{SV}^{\log}(D_\ast)=0\\
&\Longrightarrow
\text{no exact }\lambda>1\text{ state return}\\
&\Longrightarrow
\text{recurrent state-visible minimizer excluded}.
\end{aligned}
}
\tag{17.2}
$$

The only remaining bridge in this chain is the transfer / realization step.

---

# 18. Source verification ledger

The following external facts used above were re-checked against the primary arXiv source:

### Miller strain equation

arXiv:2407.02691v2, equation corresponding to the full strain formulation:

$$
\partial_tS-\Delta S-\frac12P_{st}(\omega\otimes\omega)+Q=0.
$$

### Miller orthogonality identity

$$
\langle-\Delta S,\omega\otimes\omega\rangle=0.
$$

### Exact strain $\dot H^1$ balance

$$
\frac12
\frac d{dt}
\|S\|_{\dot H^1}^2
=
-\|-\Delta S\|_2^2
-
\langle-\Delta S,Q\rangle.
$$

### Blowup continuation fact used by Miller

For a maximal

$$
H^3_{df}
$$

mild solution with

$$
T_{\max}<\infty,
$$

$$
\|S(t)\|_{\dot H^1}\to\infty.
$$

### Miller qualitative model-cone threshold

Finite-time blowup requires

$$
\limsup_{t\uparrow T_{\max}}
\frac{\|Q(t)\|_2}{\|-\Delta S(t)\|_2}
\ge1.
$$

The logarithmic cone-debt theorem in this checkpoint is derived directly from the same exact balance.

---

# 19. End state

The previous frontier was:

$$
\text{Model-Cone-to-Actual-Return Bridge}.
$$

After correcting for scale normalization, the sharper statement is:

$$
\boxed{
\textbf{
Scale-changing recurrence itself forces positive logarithmic cone debt.
}
}
$$

For an exact return factor

$$
\lambda>1,
$$

the mandatory debt is

$$
\boxed{
\mathfrak D_{SV}
\ge
\frac32\log\lambda.
}
$$

For a finite-time blowup,

$$
\boxed{
\mathfrak D_{SV}[t_0,T_{\max})
=
+\infty.
}
$$

The quantity is parabolic-scale invariant.

Thus the old critical-barrier summability obstruction has been bypassed at the analytic level.

The next and only target is:

$$
\boxed{
\textbf{
prove the Log-Cone Transfer Lemma through the MORP compactness/return limit.
}
}
$$

No additional detector family is required.