# DCRP63 / X72-R46 — Axial Pressure-Defect Oscillation versus Floquet Stretching Modulation

**Series:** Independent Navier–Stokes Research Series / X72 Bridge  
**Date:** 2026-08-18  
**Status:** Proof-development checkpoint / final X/T frontier, X-branch compression  
**Immediate predecessor:** `NS_DCRP62_X72R45_AlignedNeutral_PressureGap_XTConfluence_2026-08-18.md`

**Primary internal dependencies**
- DCRP-31 — finite-radius inward PFET and critical same-parent summability NO-GO
- DCRP-35 — positive stretching / inward enstrophy turnover
- DCRP-38 — exact covariance ledger
- DCRP-59/60 — signed residual confluence
- DCRP-61 — aligned-neutral stress-projection equality mode
- DCRP-62 — aligned-neutral pressure-response defect gap and reduction to X/T
- X72 Round37 — pressure-response defect PDE/energy
- X72 Round38 — transport–Riesz triple-increment identity; spatially constant defect null channel
- X72 Round39–41 — critical Dini/Hardy/BMO/Campanato and special cofactor–Piola reductions

**External calibration checked this round**
- Gregory Seregin, *On potential Type II blowups for the Navier-Stokes equations*, arXiv:2606.29468.
- B. Galanti, J. D. Gibbon, M. Heritage, *Vorticity alignment results for the three-dimensional Euler and Navier-Stokes equations*, arXiv:chao-dyn/9709003.
- J. D. Gibbon, D. D. Holm, R. M. Kerr, I. Roulstone, *Quaternions and particle dynamics in the Euler fluid equations*, arXiv:nlin/0512034.

No full Navier–Stokes regularity theorem is claimed.

---

# 0. Executive result

DCRP62 reduced the rank-two global frontier to

$$
\boxed{
\mathsf X\vee\mathsf T,
}
$$

where:

- $\mathsf X$ = X72 pressure / projection / commutator defect;
- $\mathsf T$ = same-parent material/enstrophy turnover.

The immediate question was which branch has the sharper new structure.

DCRP63 audits both and chooses **X**.

The turnover branch is already known to coexist with the DCRP31 inward PFET in one finite normalized package, but no universal signed algebraic relation between the two currents has been proved, and their raw same-parent energy/dissipation payments remain critically summable.

By contrast, DCRP62 supplies a new **signed axial pressure-response identity** that was not present in the old X72 generic defect theory.

The result of DCRP63 is a quantitative normal form for the X branch.

---

## Aligned-neutral finite-compensation setting

Assume the no-turnover exceptional equality package inherited from DCRP61/62:

$$
\boxed{
B(s)=\rho(s)I,
}
$$

$$
\boxed{
S\Omega=\lambda(s)\Omega,
}
$$

with $\lambda$ spatially uniform on the covariance observer support, and

$$
\boxed{
R_B^{tr}=0.
}
$$

Define

$$
\boxed{
Z(s)
=
\int\phi|\Omega|^2dy
=
3\rho(s),
}
$$

and

$$
\boxed{
M_4(s)
=
\int\phi|\Omega|^4dy.
}
$$

The trace covariance ledger gives

$$
\boxed{
Z'
=
\left[
2\lambda-(2-3\gamma)
\right]Z.
}
$$

Let

$$
\boxed{
\lambda_\ast
=
\frac{2-3\gamma}{2}.
}
$$

Then

$$
\boxed{
\frac{Z'}{Z}
=
2(\lambda-\lambda_\ast).
}
$$

DCRP62 gives the exact pressure-response defect relation

$$
\boxed{
E_p\Omega
=
-
\left(
\lambda'
+
\lambda
+
\frac16|\Omega|^2
\right)\Omega.
}
$$

---

## Constant pressure-defect modes are invisible to isotropic covariance

Let

$$
K(s)\in\mathrm{Sym}_0(3)
$$

be **any spatially constant trace-free tensor**.

Because

$$
B=\rho I,
$$

$$
\boxed{
\int\phi\,
\Omega\cdot K(s)\Omega\,dy
=
K:B
=
0.
}
$$

Therefore the covariance-weighted axial pressure-defect pairing is unchanged after quotienting out every constant trace-free tensor:

$$
\boxed{
\int\phi\,
\Omega\cdot(E_p-K)\Omega\,dy
=
\int\phi\,
\Omega\cdot E_p\Omega\,dy.
}
$$

This is exactly the quotient relevant to X72 Round38's constant-defect null channel.

---

## Exact modulation–oscillation identity

Define

$$
\boxed{
\mathfrak A(s)
=
\int
\phi\,
\Omega\cdot(E_p-K)\Omega\,dy.
}
$$

Using the DCRP62 aligned defect identity,

$$
\boxed{
\mathfrak A
=
-(\lambda'+\lambda)Z
-
\frac16M_4.
}
$$

Integrate one DSS period.

Use

$$
\lambda
=
\lambda_\ast
+
\frac12\frac{Z'}{Z}.
$$

After two periodic integrations by parts:

$$
\boxed{
\int_0^{S_0}
\mathfrak A(s)\,ds
=
\frac12
\int_0^{S_0}
\frac{(Z')^2}{Z}\,ds
-
\lambda_\ast
\int_0^{S_0}
Z\,ds
-
\frac16
\int_0^{S_0}
M_4\,ds.
}
$$

Equivalently, because

$$
\frac12\frac{(Z')^2}{Z}
=
2Z(\lambda-\lambda_\ast)^2,
$$

$$
\boxed{
\int_0^{S_0}
\mathfrak A\,ds
=
2
\int_0^{S_0}
Z(\lambda-\lambda_\ast)^2ds
-
\lambda_\ast
\int_0^{S_0}
Zds
-
\frac16
\int_0^{S_0}
M_4ds.
}
$$

This is the central theorem of DCRP63.

It gives an exact trade:

$$
\boxed{
\text{temporal stretching modulation}
\longleftrightarrow
\text{spatial pressure-defect oscillation}.
}
$$

---

## Quantitative spatial oscillation gap

Define the spacetime pressure-defect oscillation modulo spatial constants:

$$
\boxed{
\mathfrak O_p
=
\inf_{
K(\cdot)\in L^2_s\mathrm{Sym}_0(3)
}
\int_0^{S_0}
\int
\phi
|E_p(y,s)-K(s)|_F^2
\,dy\,ds.
}
$$

Define

$$
\boxed{
\mathfrak M_4
=
\int_0^{S_0}
M_4(s)ds,
}
$$

and

$$
\boxed{
\mathfrak B_p
=
\lambda_\ast
\int_0^{S_0}
Z(s)ds
+
\frac16
\mathfrak M_4.
}
$$

Define temporal Floquet modulation action

$$
\boxed{
\mathfrak M_t
=
2
\int_0^{S_0}
Z(s)
(\lambda(s)-\lambda_\ast)^2ds
=
\frac12
\int_0^{S_0}
\frac{(Z')^2}{Z}ds.
}
$$

Then the exact identity is

$$
\boxed{
\int_0^{S_0}\mathfrak A\,ds
=
\mathfrak M_t-\mathfrak B_p.
}
$$

Cauchy–Schwarz gives

$$
\boxed{
|\mathfrak M_t-\mathfrak B_p|
\le
\mathfrak M_4^{1/2}
\mathfrak O_p^{1/2}.
}
$$

Hence:

## Main D63 quantitative gap

$$
\boxed{
\mathfrak O_p
\ge
\frac{
(\mathfrak B_p-\mathfrak M_t)_+^2
}{
\mathfrak M_4
}.
}
$$

Therefore if temporal Floquet modulation is not large enough to pay the pressure budget, the pressure-response defect must carry a strictly positive **spatial oscillation modulo constants**.

This removes the easiest Round38 commutator-null escape.

---

## Exact neutral-rate specialization

If

$$
\boxed{
\lambda(s)\equiv\lambda_\ast,
}
$$

then

$$
\boxed{
Z(s)\equiv Z_0
}
$$

on the no-turnover branch and

$$
\boxed{
\mathfrak M_t=0.
}
$$

Therefore

$$
\boxed{
\mathfrak O_p
\ge
\frac{
\left[
\lambda_\ast
\int Zds
+
\frac16\mathfrak M_4
\right]^2
}{
\mathfrak M_4
}
>0.
}
$$

So the exact constant-rate Aligned-Neutral Floquet Mode cannot hide its D62 pressure defect in a spatially constant tensor.

It **must** generate spatial pressure/cofactor oscillation.

This is important because X72 Round38 explicitly identifies a spatially constant defect as a commutator-null channel.

DCRP63 shows that the strongest aligned-neutral equality mode cannot live entirely in that null channel.

---

## If spatial pressure oscillation vanishes

Suppose instead

$$
\boxed{
\mathfrak O_p=0.
}
$$

Then $E_p$ is spatially constant, modulo the observer, in the exact Hilbert quotient.

The modulation–oscillation identity forces

$$
\boxed{
\mathfrak M_t
=
\mathfrak B_p.
}
$$

Equivalently,

$$
\boxed{
\int_0^{S_0}
Z
(\lambda-\lambda_\ast)^2ds
=
\frac{\lambda_\ast}{2}
\int_0^{S_0}
Zds
+
\frac1{12}
\mathfrak M_4.
}
$$

Thus the stretching eigenvalue must make a quantitatively large time excursion.

In particular,

$$
\boxed{
\frac{
\int
Z(\lambda-\lambda_\ast)^2
}{
\int Z
}
\ge
\frac{\lambda_\ast}{2}.
}
$$

Because

$$
0<\lambda_\ast<\frac12,
$$

$$
\boxed{
\sqrt{\frac{\lambda_\ast}{2}}
>
\lambda_\ast.
}
$$

Therefore the weighted RMS excursion from the neutral mean exceeds the neutral mean itself.

Consequently there exists a time at which

$$
\boxed{
|\lambda-\lambda_\ast|>\lambda_\ast.
}
$$

Hence every spatially constant-defect realization must enter at least one of:

$$
\boxed{
\lambda<0
}
$$

(compressive vorticity eigenvalue),

or

$$
\boxed{
\lambda>2\lambda_\ast
=
2-3\gamma
}
$$

(overstretching excursion).

So the X branch has a new exact alternative:

$$
\boxed{
\text{spatial pressure-defect oscillation}
}
$$

or

$$
\boxed{
\text{large temporal Floquet excursion}.
}
$$

---

## Strategic conclusion

DCRP63 does **not** close X.

It does something more precise:

1. the D62 pressure defect cannot disappear;
2. it cannot remain in X72 Round38's spatially constant commutator-null channel unless the stretching rate undergoes a large periodic modulation;
3. at exact neutral rate, nontrivial spatial pressure-defect oscillation is forced quantitatively.

Thus the next target is no longer the generic X72 defect-energy PDE.

It is the much smaller two-mode X normal form:

$$
\boxed{
\mathsf X_{\rm osc}
\vee
\mathsf X_{\rm mod}.
}
$$

Where:

### $\mathsf X_{\rm osc}$

pressure/cofactor defect has nonzero spatial oscillation modulo constant tensors and therefore lies in the genuinely commutator-relevant Campanato/BMO sector of X72 Round38–41;

### $\mathsf X_{\rm mod}$

pressure defect stays spatially homogeneous only by forcing a large recurrent excursion of the aligned stretching eigenvalue.

The T branch remains the separate material escape.

The next best attack is $\mathsf X_{\rm mod}$, because it is finite-dimensional and may admit a Riccati/Floquet pressure-Hessian contradiction before returning to the critical commutator endpoint.

---

# 1. Setup and notation

Let the finite compensation observer be defined by a fixed cutoff

$$
\boxed{
0\le\phi\in C_c^\infty.
}
$$

Let

$$
\boxed{
B(s)
=
\int
\phi
\Omega\otimes\Omega\,dy.
}
$$

On the finite full-compensation branch,

$$
\boxed{
B(s)=\rho(s)I.
}
\tag{1.1}
$$

Set

$$
\boxed{
Z(s)
=
\operatorname{tr}B(s)
=
3\rho(s).
}
\tag{1.2}
$$

Define

$$
\boxed{
M_4(s)
=
\int
\phi|\Omega|^4dy.
}
\tag{1.3}
$$

---

# 2. No-turnover aligned trace ledger

Assume

$$
\boxed{
R_B^{tr}=0.
}
\tag{2.1}
$$

Assume the exceptional D61 aligned state:

$$
\boxed{
S\Omega=\lambda(s)\Omega
}
\tag{2.2}
$$

through the observer support, with $\lambda$ spatially uniform.

Then total stretching is

$$
\boxed{
\int
\phi
\Omega\cdot S\Omega\,dy
=
\lambda Z.
}
\tag{2.3}
$$

The DCRP35/38 enstrophy ledger gives:

## Theorem D63.1 — Exact Isotropic Aligned Covariance Rate

$$
\boxed{
Z'
=
\left[
2\lambda-(2-3\gamma)
\right]Z.
}
\tag{2.4}
$$

Define

$$
\boxed{
c_\gamma=2-3\gamma,
}
\tag{2.5}
$$

and

$$
\boxed{
\lambda_\ast=\frac{c_\gamma}{2}.
}
\tag{2.6}
$$

Then

$$
\boxed{
\frac{Z'}Z
=
2(\lambda-\lambda_\ast).
}
\tag{2.7}
$$

---

# 3. Pressure-defect quotient by constant tensors

DCRP62 proves:

$$
\boxed{
E_p\Omega
=
-
\left(
\lambda'
+
\lambda
+
\frac16|\Omega|^2
\right)\Omega.
}
\tag{3.1}
$$

Let

$$
\boxed{
K(s)\in\mathrm{Sym}_0(3)
}
\tag{3.2}
$$

be arbitrary and spatially constant.

Because

$$
B=\rho I,
$$

$$
\boxed{
K:B
=
\rho\operatorname{tr}K
=
0.
}
\tag{3.3}
$$

Therefore:

## Theorem D63.2 — Constant-Defect Quotient Neutrality

$$
\boxed{
\int
\phi
\Omega\cdot(E_p-K)\Omega\,dy
=
\int
\phi
\Omega\cdot E_p\Omega\,dy.
}
\tag{3.4}
$$

The isotropic covariance observer annihilates every constant trace-free pressure-defect mode.

---

# 4. Exact axial defect pairing

Define

$$
\boxed{
\mathfrak A_K(s)
=
\int
\phi
\Omega\cdot(E_p-K)\Omega\,dy.
}
\tag{4.1}
$$

By (3.1),

$$
\boxed{
\mathfrak A_K
=
-(\lambda'+\lambda)Z
-\frac16M_4.
}
\tag{4.2}
$$

This is independent of the chosen constant tensor $K$.

---

# 5. Eliminate lambda in favor of covariance modulation

From (2.7),

$$
\boxed{
\lambda
=
\lambda_\ast
+
\frac12
\frac{Z'}Z.
}
\tag{5.1}
$$

Differentiate:

$$
\boxed{
\lambda'
=
\frac12
\left[
\frac{Z''}{Z}
-
\frac{(Z')^2}{Z^2}
\right].
}
\tag{5.2}
$$

Therefore

$$
\boxed{
(\lambda'+\lambda)Z
=
\frac12Z''
-
\frac12\frac{(Z')^2}{Z}
+
\lambda_\ast Z
+
\frac12Z'.
}
\tag{5.3}
$$

---

# 6. One-period modulation–oscillation identity

Integrate (4.2) over one period.

Because $Z$ is periodic,

$$
\boxed{
\int_0^{S_0}Z'ds=0,
}
$$

and

$$
\boxed{
\int_0^{S_0}Z''ds=0.
}
$$

Therefore:

## Theorem D63.3 — Exact Pressure Modulation–Oscillation Trade Law

$$
\boxed{
\begin{aligned}
\int_0^{S_0}
\mathfrak A_K(s)ds
={}&
\frac12
\int_0^{S_0}
\frac{(Z')^2}{Z}ds
\\
&-
\lambda_\ast
\int_0^{S_0}
Zds
\\
&-
\frac16
\int_0^{S_0}
M_4ds.
\end{aligned}
}
\tag{6.1}
$$

Using

$$
Z'/Z=2(\lambda-\lambda_\ast),
$$

equivalently:

$$
\boxed{
\begin{aligned}
\int_0^{S_0}
\mathfrak A_Kds
={}&
2
\int_0^{S_0}
Z(\lambda-\lambda_\ast)^2ds
\\
&-
\lambda_\ast
\int_0^{S_0}
Zds
\\
&-
\frac16
\int_0^{S_0}
M_4ds.
\end{aligned}
}
\tag{6.2}
$$

This identity is exact.

---

# 7. Define the two competing actions

Define temporal modulation:

$$
\boxed{
\mathfrak M_t
=
\frac12
\int_0^{S_0}
\frac{(Z')^2}{Z}ds
=
2
\int_0^{S_0}
Z(\lambda-\lambda_\ast)^2ds.
}
\tag{7.1}
$$

Define the positive baseline pressure budget:

$$
\boxed{
\mathfrak B_p
=
\lambda_\ast
\int_0^{S_0}
Zds
+
\frac16
\mathfrak M_4,
}
\tag{7.2}
$$

where

$$
\boxed{
\mathfrak M_4
=
\int_0^{S_0}
M_4ds.
}
\tag{7.3}
$$

Then Theorem D63.3 is simply

$$
\boxed{
\int_0^{S_0}
\mathfrak A_Kds
=
\mathfrak M_t-\mathfrak B_p.
}
\tag{7.4}
$$

---

# 8. Spatial oscillation norm

Define the quotient oscillation norm:

$$
\boxed{
\mathfrak O_p
=
\inf_K
\int_0^{S_0}
\int
\phi
|E_p-K(s)|_F^2
\,dy\,ds,
}
\tag{8.1}
$$

where the infimum is over time-dependent spatially constant trace-free tensors.

For every such $K$,

$$
|\Omega\cdot(E_p-K)\Omega|
\le
|\Omega|^2|E_p-K|_F.
$$

Therefore spacetime Cauchy–Schwarz gives

$$
\boxed{
\left|
\int_0^{S_0}
\mathfrak A_Kds
\right|
\le
\mathfrak M_4^{1/2}
\left[
\int_0^{S_0}
\int
\phi|E_p-K|_F^2
\right]^{1/2}.
}
\tag{8.2}
$$

Take the infimum.

---

# Theorem D63.4 — Quantitative Pressure-Defect Oscillation Gap

$$
\boxed{
\mathfrak O_p
\ge
\frac{
|\mathfrak B_p-\mathfrak M_t|^2
}{
\mathfrak M_4
}.
}
\tag{8.3}
$$

In particular, if

$$
\mathfrak M_t
\le
(1-\delta)
\mathfrak B_p
$$

for some

$$
0<\delta\le1,
$$

then

$$
\boxed{
\mathfrak O_p
\ge
\delta^2
\frac{
\mathfrak B_p^2
}{
\mathfrak M_4
}
>0.
}
\tag{8.4}
$$

This is the first quantitative lower bound on the **spatially nonconstant component** of the D62 pressure defect.

---

# 9. Exact neutral-rate branch

If

$$
\boxed{
\lambda(s)\equiv\lambda_\ast,
}
\tag{9.1}
$$

then

$$
Z'=0.
$$

Hence

$$
\boxed{
\mathfrak M_t=0.
}
\tag{9.2}
$$

Theorem D63.4 becomes:

## Corollary D63.5 — Constant-Rate Pressure Oscillation Gap

$$
\boxed{
\mathfrak O_p
\ge
\frac{
\left[
\lambda_\ast
\int_0^{S_0}Zds
+
\frac16\mathfrak M_4
\right]^2
}{
\mathfrak M_4
}
>0.
}
\tag{9.3}
$$

Thus the exact constant-rate aligned-neutral branch has unavoidable spatial pressure-response oscillation.

---

# 10. Round38 constant-defect null channel is removed

X72 Round38 identifies:

$$
\boxed{
\text{spatially constant defect}
}
$$

as a transport–Riesz commutator null channel.

Corollary D63.5 says the exact neutral-rate aligned state cannot place its pressure defect entirely in that channel.

Therefore the D62 pressure gap has a genuinely spatial component.

This does **not** prove the Round38 commutator pairing is nonzero.

It proves the easiest exact null mechanism—constant defect—is unavailable.

The remaining oscillatory defect is precisely the kind of state measured by:

- Round38 defect increments;
- Round39 Dini modulus;
- Round40 BMO/Campanato oscillation;
- Round41 affine-defect/special cofactor reduction.

---

# 11. Spatially homogeneous pressure-defect alternative

Suppose

$$
\boxed{
\mathfrak O_p=0.
}
\tag{11.1}
$$

Then Theorem D63.4 forces

$$
\boxed{
\mathfrak M_t
=
\mathfrak B_p.
}
\tag{11.2}
$$

Therefore:

## Theorem D63.6 — Exact Floquet Modulation Cost

$$
\boxed{
\int_0^{S_0}
Z
(\lambda-\lambda_\ast)^2ds
=
\frac{\lambda_\ast}{2}
\int_0^{S_0}
Zds
+
\frac1{12}
\mathfrak M_4.
}
\tag{11.3}
$$

In particular,

$$
\boxed{
\frac{
\int
Z(\lambda-\lambda_\ast)^2ds
}{
\int Zds
}
\ge
\frac{\lambda_\ast}{2}.
}
\tag{11.4}
$$

The spatially constant pressure-defect null mode can survive only through strong temporal stretching modulation.

---

# 12. Large excursion consequence

Since

$$
\boxed{
0<\lambda_\ast<\frac12,
}
\tag{12.1}
$$

we have

$$
\boxed{
\frac{\lambda_\ast}{2}
>
\lambda_\ast^2.
}
\tag{12.2}
$$

If

$$
|\lambda-\lambda_\ast|
\le
\lambda_\ast
$$

for every time, then

$$
(\lambda-\lambda_\ast)^2
\le
\lambda_\ast^2,
$$

which contradicts (11.4), with strictness strengthened further by $\mathfrak M_4>0$.

Therefore:

## Corollary D63.7 — Compression-or-Overstretch Excursion

On the spatially homogeneous pressure-defect branch, there exists a time such that

$$
\boxed{
|\lambda-\lambda_\ast|>\lambda_\ast.
}
\tag{12.3}
$$

Hence:

$$
\boxed{
\lambda<0
}
$$

or

$$
\boxed{
\lambda>2\lambda_\ast
=
2-3\gamma.
}
\tag{12.4}
$$

The stretching eigenvalue must leave the moderate positive neutral band every period.

---

# 13. Interpretation of the two X subbranches

DCRP63 therefore gives:

$$
\boxed{
\mathsf X
\Longrightarrow
\mathsf X_{\rm osc}
\vee
\mathsf X_{\rm mod},
}
\tag{13.1}
$$

inside the aligned/no-turnover finite-compensation regime.

### X_osc — spatial pressure/cofactor oscillation

$$
\boxed{
\mathfrak O_p>0.
}
$$

This is directly relevant to X72 Round38–41 commutator/Campanato machinery.

### X_mod — temporal Floquet modulation

$$
\boxed{
\mathfrak O_p=0,
}
$$

but then

$$
\boxed{
\int
Z(\lambda-\lambda_\ast)^2
\ge
\frac{\lambda_\ast}{2}
\int Z,
}
$$

and every period has a compressive or overstretch excursion.

This is a finite-dimensional eigenvalue-dynamics branch.

---

# 14. Why X is the sharper current priority

The T branch presently carries:

- inward enstrophy turnover from D35/D59;
- inward PFET from D31.

Both occur in a finite normalized matching package.

However:

1. they are different weighted currents;
2. no universal signed pointwise relation is established;
3. D31 already proves the raw physical PFET payments can remain geometrically summable;
4. the enstrophy-time dissipation action is likewise critical/summable in the strict Type-II scaling.

Therefore a direct energy-summation attack on T is currently low leverage.

The X branch instead now has the exact D63 normal form:

$$
\boxed{
\text{spatial defect oscillation}
\vee
\text{large temporal eigenvalue excursion}.
}
$$

The second alternative is finite-dimensional and should be attacked first.

---

# 15. Why the X oscillation gap is genuinely new

Round37 proved only that nonzero pressure-response defect energy may persist.

Round38 showed a spatially constant defect can be completely invisible to the transport commutator pairing.

Round39–41 then encountered a representation-stable critical endpoint in controlling the oscillatory part.

D63 contributes a new lower constraint from the DCRP aligned-neutral geometry:

> the constant null channel cannot absorb the full D62 defect unless the stretching rate pays a specific temporal Fisher/Floquet modulation cost.

Thus the old X72 critical endpoint is now fed by a forced oscillatory defect, not an arbitrary hypothetical one.

---

# 16. Temporal modulation as a Fisher-type action

The quantity

$$
\boxed{
\mathfrak M_t
=
\frac12
\int
\frac{(Z')^2}{Z}
}
$$

is the Fisher action of the scalar covariance mass.

Equivalently,

$$
\boxed{
\mathfrak M_t
=
2
\int
Z
(\lambda-\lambda_\ast)^2.
}
$$

This gives an observer-independent meaning to the temporal escape:

the covariance can hide spatial pressure oscillation only by making its own recurrent mass strongly nonuniform in similarity time.

This is a new native finite-dimensional observer.

---

# 17. Compact-class consequence

On a compact normalized class suppose:

$$
\boxed{
0<Z_-\le Z(s)\le Z_+,
}
$$

and

$$
\boxed{
\mathfrak M_4\ge M_{4,-}>0.
}
$$

Then the exact neutral-rate branch gives a uniform constant

$$
\boxed{
c_{\rm osc}>0
}
$$

such that

$$
\boxed{
\mathfrak O_p\ge c_{\rm osc}.
}
$$

Thus the pressure-defect oscillation becomes a finite native compiler observable.

No uncontrolled tail norm is needed to detect it.

---

# 18. Relation to the D62 material pressure gap

D62's trajectory theorem showed

$$
\int
\xi^\top E_p\xi
<
0.
$$

D63 is different.

It places the defect inside a fixed covariance observer and quotients out every spatially constant trace-free tensor.

The new theorem says the signed pressure mismatch must show up as:

- spatial oscillation;
- or time modulation of the covariance/stretching rate.

This is exactly the local-to-global lift needed before returning to X72 commutator estimates.

---

# 19. T branch remains independent

Nothing in D63 proves:

$$
\boxed{
\mathsf T\Rightarrow\mathsf X.
}
$$

Nor does it prove a universal PFET–enstrophy-flux sign coupling.

DCRP49 already established that apparently related pressure/energy boundary observables can be independent.

Therefore T remains a genuine final escape branch and should not be artificially identified with X.

The current strategy is:

1. compress X as far as possible;
2. if X closes, attack T alone;
3. if X retains one exact equality mode, compare that mode with T/PFET only then.

---

# 20. Status ledger

## PROVED this round

### D63-P1 — exact aligned covariance-rate law

$$
Z'=[2\lambda-(2-3\gamma)]Z.
$$

### D63-P2 — constant trace-free pressure-defect modes are annihilated by isotropic covariance

$$
K:B=0.
$$

### D63-P3 — exact axial pressure modulation–oscillation identity

$$
\int\mathfrak A
=
\frac12\int\frac{Z'^2}{Z}
-
\lambda_\ast\int Z
-
\frac16\int M_4.
$$

### D63-P4 — quantitative spatial pressure-defect oscillation gap

$$
\mathfrak O_p
\ge
\frac{
|\mathfrak B_p-\mathfrak M_t|^2
}{
\mathfrak M_4
}.
$$

### D63-P5 — exact-neutral constant-rate branch has strictly positive spatial oscillation.

### D63-P6 — spatially homogeneous defect requires exact temporal modulation action

$$
\int Z(\lambda-\lambda_\ast)^2
=
\frac{\lambda_\ast}{2}\int Z
+
\frac1{12}\mathfrak M_4.
$$

### D63-P7 — compression/overstretch excursion

$$
\lambda<0
\quad\vee\quad
\lambda>2-3\gamma
$$

at some time each period on the homogeneous-defect branch.

---

# 21. Closed / corrected routes

## Closed

The exact constant-rate aligned-neutral pressure defect cannot hide entirely in the X72 spatially constant commutator-null channel.

## Refined

The X branch is compressed to:

$$
\boxed{
\mathsf X_{\rm osc}
\vee
\mathsf X_{\rm mod}.
}
$$

## Still open

- unconditional Round38–41 closure of the forced spatial oscillation branch;
- dynamical realizability of the large temporal Floquet excursion branch;
- final material turnover branch T.

---

# 22. New STOP

$$
\boxed{
\textbf{
STOP-D63:
The D62 pressure defect cannot remain both aligned-neutral and commutator-null for free. After quotienting every spatially constant trace-free defect, an exact trade law forces either a quantitative spatial pressure-defect oscillation or a large temporal Floquet stretching excursion; at exact neutral rate the spatial oscillation is unavoidable.
}
}
$$

---

# 23. Next autonomous step

## DCRP64 / X72-R47 — Floquet Modulation Excursion Rigidity

**Working title**

> **Aligned Stretching Eigenvalue Excursions, Pressure-Hessian Riccati Dynamics, and Compression/Overstretch Closure**

Primary tasks:

1. assume the X_mod equality branch:
   $$
   \mathfrak O_p=0;
   $$
2. use
   $$
   \lambda<0
   \vee
   \lambda>2-3\gamma
   $$
   excursions together with:
   $$
   H_P\Omega=-(\lambda'+\lambda+\lambda^2)\Omega;
   $$
3. derive a periodic Riccati/Floquet inequality for $\lambda$;
4. use trace-free strain eigenvalues to determine what compression/overstretch forces in the transverse strain plane;
5. test whether one excursion necessarily creates:
   - vorticity tilt;
   - pressure-defect spatial oscillation;
   - rank lift;
   - or material turnover;
6. if X_mod closes, the only X survivor is the forced spatial oscillation branch already connected to X72 Round38–41.

Desired endpoint:

$$
\boxed{
\mathsf X_{\rm mod}\text{ closed}
\quad\vee\quad
\text{one explicit periodic eigenvalue normal form}.
}
$$

---

# 24. One-line checkpoint

The X/T frontier now has a sharp X normal form: the aligned pressure defect must either have a nonzero spatial oscillatory component that escapes Round38's constant-defect null channel, or else the stretching eigenvalue must make a quantitatively large compressive/overstretch excursion every DSS period.

---

**End checkpoint:** DCRP63 / X72-R46  
**Next:** DCRP64 / X72-R47 — Floquet Modulation Excursion Rigidity.
