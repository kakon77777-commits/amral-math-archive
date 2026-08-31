# DCRP96 / X72-R79 — Sign-Coherent Circulation-Anomaly Young Profile, Deviatoric Covariance Lock, and the Barycenter NO-GO

**Series:** Independent Navier–Stokes Research Series / X72 Bridge  
**Date:** 2026-08-20  
**Status:** proof-development checkpoint / circulation-anomaly Young-profile round  
**Immediate predecessor:** `NS_DCRP95_X72R78_SGSPhaseSlip_TotalVariation_2026-08-20.md`

## Primary internal dependencies

- DCRP24 — increment Young profile / fiber escape / actual Reynolds covariance / pressure-compatible kernel.
- DCRP25 — pressure-compatible SGS energy rigidity / affine-kernel collapse.
- DCRP26 — recurrent strong-increment profile \(\Rightarrow\) finite SGS recurrence-window detector.
- DCRP81–85 — Kelvin SGS circulation / trace / scale compiler.
- DCRP92 — finite joint detector.
- DCRP95 — sign-coherent positive-density SGS Kelvin phase-slip conveyor.

## Fresh primary-source calibration

- R. Yu, *Filtered Vortex Stretching and Subgrid Defects for the Three-Dimensional Navier–Stokes Equations*, arXiv:2606.27560 (2026).
  - At critical scaling, bounded derivative-compatible increment defects admit cylindrical generalized Young-measure profiles.
  - The differentiated subgrid stress is controlled by the derivative-compatible increment defect.
  - Cylindrical control alone does not automatically give every full norm/covariance conclusion; DCRP24's fiber-tail split remains necessary.
- G. L. Eyink, *The Cascade of Circulations in Fluid Turbulence*, arXiv:physics/0606159.
- G. L. Eyink, *Turbulent Cascade of Circulations*, arXiv:physics/0605014.

No full Navier–Stokes regularity theorem is claimed.

---

# 0. Executive result

DCRP95 isolated one last compact reset source:

\[
\boxed{
\mathsf C_{\rm slip}
}
\]

= a sign-coherent SGS Kelvin phase-slip conveyor with

\[
\mathcal V_{\Gamma,+}^{\rm SGS}(N)\gtrsim N.
\]

The proposed D96 test was:

> does same-sign circulation slip force a nonzero **barycentric** bias in the increment Young profile?

The answer is:

\[
\boxed{
\textbf{NO}.
}
\]

The SGS circulation functional is quadratic in velocity increments through the Reynolds covariance.

Therefore a centered and sign-symmetric Young measure can carry nonzero circulation flux.

The correct rigidity variable is the **deviatoric second moment**.

After smoothing the recurrent loop-current at a fixed relative normalized scale, define a divergence-free detector field:

\[
\Psi_\Gamma(x,s),
\qquad
\nabla\cdot\Psi_\Gamma=0.
\]

Let:

\[
A_\Gamma
=
\operatorname{Sym}\nabla\Psi_\Gamma.
\]

Then:

\[
\boxed{
\operatorname{tr}A_\Gamma=0.
}
\]

For the symmetric SGS stress \(R\),

\[
\boxed{
\mathfrak F_\Gamma(R)
=
\int
R:A_\Gamma.
}
\]

Hence the isotropic part of \(R\) disappears:

\[
R
=
\frac13(\operatorname{tr}R)I
+
R^0,
\]

\[
\boxed{
\mathfrak F_\Gamma(R)
=
\int
R^0:A_\Gamma.
}
\tag{0.1}
\]

Thus a sign-coherent phase slip forces a **deviatoric covariance projection**:

\[
\boxed{
\sigma\,
\int
R^0:A_\Gamma
\ge
c_\Gamma^{\rm slip}>0,
}
\tag{0.2}
\]

unless:

- the loop-current smoothing loses order-one flux;
- the Young representation loses mass through fiber/concentration escape;
- the material/loop state leaves compactness.

In the full Young representation, write the centered increment variable:

\[
\zeta
=
\xi-m,
\qquad
m=\int\xi\,d\nu(\xi).
\]

Then the oscillatory covariance is:

\[
Q_\nu
=
\int
\zeta\otimes\zeta
\,d\nu(\xi).
\]

With concentration covariance \(Q^c\),

\[
R
=
Q_\nu+Q^c.
\]

The slip functional becomes:

\[
\boxed{
\mathfrak F_\Gamma(\nu,Q^c)
=
\int
A_\Gamma:
\left[
Q_\nu^0+(Q^c)^0
\right].
}
\tag{0.3}
\]

The first moment \(m\) is not the decisive variable.

The phase-slip conveyor therefore forces:

\[
\boxed{
\textbf{oriented nematic / deviatoric covariance locking}
}
\]

or a previously declared concentration/state/scale escape.

---

# 1. Smooth current representation of the loop flux

For a closed loop \(C(s)\), its vector-valued current is formally:

\[
J_C(x,s)
=
\oint_{C(s)}
t(\sigma,s)
\delta_{C(\sigma,s)}(x)
\,d\sigma.
\]

Because \(C\) is closed:

\[
\boxed{
\nabla\cdot J_C=0
}
\]

in distributions.

The raw loop current is codimension two.

D82 already showed why one must not blindly pair arbitrary weak limits with it.

On the pure D95 compact branch:

- loop geometry is in a compact normalized class;
- filter ratio is fixed;
- the recurrent oriented loop state has a finite template family.

Choose one fixed mollifier scale \(\theta>0\) in normalized variables and set:

\[
\boxed{
\Psi_\Gamma
=
\chi_s
\,
\eta_\theta*J_C.
}
\tag{1.1}
\]

Here \(\chi_s\) is the finite normalized time-window cutoff.

Mollification preserves:

\[
\boxed{
\nabla\cdot\Psi_\Gamma=0.
}
\tag{1.2}
\]

If replacing the raw line-current by \(\Psi_\Gamma\) loses an order-one fraction of the SGS circulation flux, the missing part is exactly another line/subfilter/relative-scale trace defect and returns to D82–85.

Therefore D96 studies the complementary **smooth-current visible branch**.

---

# 2. SGS circulation is a linear functional of the covariance

Let:

\[
R_\ell
=
\overline{u\otimes u}_\ell
-
U_\ell\otimes U_\ell
\]

be the symmetric Reynolds/subgrid stress.

The SGS force is:

\[
f_\ell
=
-\nabla\cdot R_\ell.
\]

Pair it with the smooth divergence-free loop current:

\[
\mathfrak F_\Gamma(R_\ell)
=
\int
f_\ell\cdot\Psi_\Gamma
\,dxds.
\]

Integrating by parts:

\[
\boxed{
\mathfrak F_\Gamma(R_\ell)
=
\int
R_\ell:\nabla\Psi_\Gamma
\,dxds.
}
\tag{2.1}
\]

Since \(R_\ell\) is symmetric,

\[
R_\ell:\nabla\Psi_\Gamma
=
R_\ell:
\operatorname{Sym}\nabla\Psi_\Gamma.
\]

Define:

\[
\boxed{
A_\Gamma
=
\operatorname{Sym}\nabla\Psi_\Gamma.
}
\tag{2.2}
\]

Then:

\[
\boxed{
\mathfrak F_\Gamma(R_\ell)
=
\int
R_\ell:A_\Gamma
\,dxds.
}
\tag{2.3}
\]

This is the exact finite-current version of the SGS circulation detector.

---

# 3. The detector is trace-free

Because:

\[
\nabla\cdot\Psi_\Gamma=0,
\]

\[
\operatorname{tr}
(
\operatorname{Sym}\nabla\Psi_\Gamma
)
=
\nabla\cdot\Psi_\Gamma
=
0.
\]

Hence:

\[
\boxed{
\operatorname{tr}A_\Gamma=0.
}
\tag{3.1}
\]

Decompose:

\[
R
=
p_{\rm sgs}I
+
R^0,
\]

where:

\[
p_{\rm sgs}
=
\frac13
\operatorname{tr}R,
\]

and:

\[
\operatorname{tr}R^0=0.
\]

Then:

\[
p_{\rm sgs}I:A_\Gamma
=
p_{\rm sgs}
\operatorname{tr}A_\Gamma
=
0.
\]

Therefore:

## Theorem D96.1 — Isotropic SGS Stress is Circulation-Silent

\[
\boxed{
\mathfrak F_\Gamma(R)
=
\int
R^0:A_\Gamma.
}
\tag{3.2}
\]

Only the deviatoric SGS covariance can contribute to the smooth oriented circulation slip.

This is a pressure-gauge-safe statement.

---

# 4. Young-profile covariance

Let:

\[
\nu_{x,s,z}
\]

denote the critical increment Young profile in the full-representation branch.

Suppress the cylindrical/fiber variables in notation.

Let:

\[
m
=
\int
\xi
\,d\nu(\xi)
\]

be the barycenter.

Define the centered covariance:

\[
\boxed{
Q_\nu
=
\int
(\xi-m)\otimes(\xi-m)
\,d\nu(\xi).
}
\tag{4.1}
\]

If a concentration covariance survives, denote it:

\[
Q^c\ge0.
\]

Then schematically, after the D24 full-representation/fiber audit:

\[
\boxed{
R
=
Q_\nu
+
Q^c.
}
\tag{4.2}
\]

The phase-slip functional is:

\[
\boxed{
\mathfrak F_\Gamma
=
\int
A_\Gamma:
\left[
Q_\nu^0+(Q^c)^0
\right].
}
\tag{4.3}
\]

Therefore the relevant Young-profile order parameter is a **second moment**.

---

# 5. Barycentric bias is NOT necessary

Consider the centered symmetric Young measure:

\[
\boxed{
\nu
=
\frac12
\delta_{e_1}
+
\frac12
\delta_{-e_1}.
}
\tag{5.1}
\]

Then:

\[
m=0.
\]

Also:

\[
\nu(E)=\nu(-E),
\]

so the measure is fully sign-symmetric.

Its covariance is:

\[
\boxed{
Q_\nu
=
e_1\otimes e_1.
}
\tag{5.2}
\]

Take a trace-free detector:

\[
\boxed{
A
=
\operatorname{diag}(1,-1,0).
}
\tag{5.3}
\]

Then:

\[
\boxed{
A:Q_\nu
=
1.
}
\tag{5.4}
\]

Therefore:

## Theorem D96.2 — Centered Symmetry NO-GO

\[
\boxed{
m=0
\ \text{and}\
\nu(\xi)=\nu(-\xi)
\not\Rightarrow
\mathfrak F_\Gamma=0.
}
\tag{5.5}
\]

A sign-coherent circulation anomaly does not require an odd increment bias.

The SGS reset functional is even in the increment variable at the covariance level.

---

# 6. What symmetry DOES kill the slip?

If:

\[
Q_\nu=aI,
\]

then:

\[
Q_\nu^0=0.
\]

Therefore:

\[
A_\Gamma:Q_\nu=0
\]

for every divergence-free current detector.

Thus:

## Theorem D96.3 — Isotropic Second-Moment Silence

\[
\boxed{
Q_\nu
=
aI
\Longrightarrow
\mathfrak F_\Gamma(\nu)=0
}
\]

in the no-concentration branch.

More generally, the exact slip-silent profile set is:

\[
\boxed{
\mathcal K_\Gamma
=
\left\{
Q:
\int
A_\Gamma:Q^0=0
\right\}.
}
\tag{6.1}
\]

This is a codimension-one linear kernel at the covariance level for one fixed detector.

For a finite detector family:

\[
A_{\Gamma,1},
\ldots,
A_{\Gamma,N},
\]

the common silent set is:

\[
\boxed{
\mathcal K_\Gamma^{\rm fin}
=
\bigcap_{j=1}^N
\ker
\mathfrak F_{\Gamma,j}.
}
\tag{6.2}
\]

---

# 7. Pressure-compatible covariance is slip-silent

D24 isolates:

\[
\boxed{
\nabla\times\nabla\cdot R=0.
}
\tag{7.1}
\]

On a simply connected region:

\[
\nabla\cdot R=\nabla q.
\]

For any divergence-free compact test current:

\[
\begin{aligned}
\mathfrak F_\Gamma(R)
&=
-\int
(\nabla\cdot R)\cdot\Psi_\Gamma
\\
&=
-\int
\nabla q\cdot\Psi_\Gamma
\\
&=
\int
q
\nabla\cdot\Psi_\Gamma
\\
&=
0.
\end{aligned}
\]

Therefore:

## Theorem D96.4 — Pressure-Compatible Kernel Exclusion

\[
\boxed{
R\in\mathcal K_{\rm pc}
\Longrightarrow
\mathfrak F_\Gamma(R)=0.
}
\tag{7.2}
\]

Hence the D95 phase-slip conveyor automatically excludes the D24 pressure-compatible covariance kernel on its active slip events.

This is stronger than merely saying pressure-compatible stress does no bulk SGS work.

It also performs zero smooth-loop circulation reset.

---

# 8. Sign-coherent slip forces deviatoric covariance locking

D95 gives a recurring oriented state with:

\[
\boxed{
\sigma
\mathfrak F_\Gamma(R_n)
\ge
c_{\rm slip}>0
}
\tag{8.1}
\]

at positive generation density.

On the full no-concentration branch:

\[
\mathfrak F_\Gamma
=
\int
A_\Gamma:Q_\nu^0.
\]

Thus:

\[
\boxed{
\sigma
\int
A_\Gamma:Q_{\nu_n}^0
\ge
c_{\rm slip}.
}
\tag{8.2}
\]

By Cauchy–Schwarz:

\[
c_{\rm slip}
\le
\|A_\Gamma\|_{L^2}
\,
\|Q_{\nu_n}^0\|_{L^2}.
\]

Hence:

## Theorem D96.5 — Nematic Covariance Gap

\[
\boxed{
\|Q_{\nu_n}^0\|_{L^2}
\ge
\frac{
c_{\rm slip}
}{
\|A_\Gamma\|_{L^2}
}
=:
c_Q>0.
}
\tag{8.3}
\]

The phase-slip conveyor therefore forces a uniform deviatoric covariance amplitude.

More strongly, it forces a **signed projection**:

\[
\boxed{
\sigma
\langle
Q_{\nu_n}^0,
A_\Gamma
\rangle
\ge
c_{\rm slip}.
}
\tag{8.4}
\]

This is the correct "locking" statement.

---

# 9. Concentration / fiber alternative

D24 warns that cylindrical Young control does not automatically provide full norm/covariance representation.

Therefore D96 retains:

\[
\boxed{
R_{\rm fiber}
\vee
R_{\rm conc}
}
\]

as explicit alternatives.

If full representation fails because increment mass escapes along the fiber variable or concentration measure, then the phase-slip is already financed by:

\[
\boxed{
R_{\rm state}
\vee
R_{\rm crit}
\vee
R_{\rm scale}.
}
\]

Only after those branches are removed does the pure covariance locking theorem apply.

---

# 10. Compactness gives a fixed recurring nematic state

D95 already supplies a finite oriented loop-state family.

D92 supplies a finite detector family.

Take a positive-density sequence of slip events on one fixed oriented loop/filter state.

Assume:

- no fiber escape;
- no concentration defect;
- bounded critical reservoir;
- fixed relative filter ratio;
- strong normalized profile compactness.

Extract a subsequence:

\[
\nu_n\to\nu_*,
\qquad
Q_{\nu_n}\to Q_*.
\]

Lower semicontinuity / continuity of the smoothed flux functional yields:

\[
\boxed{
\sigma
\int
A_\Gamma:Q_*^0
\ge
c_{\rm slip}.
}
\tag{10.1}
\]

Therefore:

## Theorem D96.6 — Sign-Locked Young-Profile Limit

The pure compact phase-slip conveyor has a nontrivial limiting increment profile with a fixed oriented deviatoric second moment.

It cannot converge to:

- isotropic covariance;
- zero covariance;
- pressure-compatible covariance;
- any symmetry class contained in \(\mathcal K_\Gamma\).

---

# 11. The correct symmetry-breaking statement

The transformation:

\[
\xi\mapsto-\xi
\]

does **not** reverse the quadratic covariance functional.

Therefore odd symmetry is irrelevant.

Let \(T\) instead be any symmetry of the normalized state such that:

\[
\boxed{
\mathfrak F_\Gamma(T_\#\nu)
=
-
\mathfrak F_\Gamma(\nu).
}
\tag{11.1}
\]

If:

\[
T_\#\nu=\nu,
\]

then:

\[
\mathfrak F_\Gamma(\nu)
=
-\mathfrak F_\Gamma(\nu),
\]

hence:

\[
\boxed{
\mathfrak F_\Gamma(\nu)=0.
}
\tag{11.2}
\]

Therefore:

## Theorem D96.7 — Detector-Reversing Symmetry Breaking

A nonzero same-sign phase-slip profile must break every exact symmetry that reverses the oriented circulation detector.

The relevant symmetry group is determined jointly by:

- loop orientation;
- detector current;
- spatial transformation;
- covariance transformation.

This is more precise than simple increment sign symmetry.

---

# 12. Finite-dimensional covariance cone

At one recurrent slip state, let:

\[
\mathscr S_0^3
\]

be the five-dimensional space of trace-free symmetric \(3\times3\) matrices.

The deviatoric covariance field takes values in:

\[
Q^0(x,s)\in\mathscr S_0^3.
\]

The circulation detector is the linear functional:

\[
\boxed{
L_\Gamma(Q^0)
=
\int
A_\Gamma:Q^0.
}
\tag{12.1}
\]

The phase-slip survivor lies in the open half-space:

\[
\boxed{
\sigma
L_\Gamma(Q^0)
\ge
c_{\rm slip}.
}
\tag{12.2}
\]

The isotropic ray has:

\[
Q^0=0
\]

and is excluded.

The pressure-compatible kernel is a further differential subspace and is excluded.

Thus the final Young-profile survivor is an oriented half-cone of active deviatoric covariance states.

---

# 13. Relation to SGS forward work

The SGS energy transfer is:

\[
\boxed{
\Pi
=
-R:S_U,
}
\tag{13.1}
\]

where:

\[
S_U
=
\operatorname{Sym}\nabla U.
\]

Since:

\[
\operatorname{tr}S_U=0
\]

for incompressible \(U\),

\[
\Pi
=
-R^0:S_U.
\]

Thus the phase-slip and SGS-work detectors are **two linear functionals of the same deviatoric covariance**:

\[
\boxed{
L_\Gamma(Q^0)
=
\langle
A_\Gamma,Q^0
\rangle,
}
\]

\[
\boxed{
L_E(Q^0)
=
-
\langle
S_U,Q^0
\rangle.
}
\tag{13.2}
\]

D26 says the compact recurrent increment profile cannot remain a complete SGS-work phantom.

Therefore the pure compact late survivor is constrained by two recurring projections of the same covariance field.

This is the key new confluence.

---

# 14. Dual-lock cone

At a recurring state define the normalized dual-lock cone:

\[
\boxed{
\mathcal C_{\rm dual}
=
\left\{
Q^0:
\sigma_\Gamma
L_\Gamma(Q^0)
\ge
c_\Gamma^*,
\quad
L_E^+(Q^0)
\ge
c_E^*
\right\}.
}
\tag{14.1}
\]

Here \(L_E^+\) denotes whichever finite SGS recurrence/work coordinate is selected after D26 compression.

D96 does not prove:

\[
\mathcal C_{\rm dual}=\varnothing.
\]

In general two half-space constraints on the PSD covariance cone may be compatible.

Therefore the next problem is algebraic/geometric:

> can the same positive semidefinite covariance remain simultaneously circulation-reset aligned and recurrence-work aligned under the strict DSS/X72 state constraints?

This is the new frontier.

---

# 15. A centered symmetric example survives the first test

Take:

\[
\nu
=
\frac12
(\delta_{e_1}+\delta_{-e_1}).
\]

Then:

\[
m=0,
\qquad
Q=e_1\otimes e_1.
\]

For:

\[
A_\Gamma
=
\operatorname{diag}(1,-1,0),
\]

\[
L_\Gamma(Q)=1.
\]

Choose:

\[
S_U
=
\operatorname{diag}(-1,1,0).
\]

Then:

\[
L_E(Q)
=
-Q:S_U
=
1.
\]

So one elementary rank-one covariance can satisfy both positive projections.

Therefore:

## Theorem D96.8 — Dual-Lock Algebraic Compatibility NO-GO

Pure covariance algebra alone does not exclude simultaneous:

- positive circulation reset;
- positive SGS energy transfer.

Additional dynamical / pressure / rank / X72 constraints are necessary.

This prevents a false "two positive detectors imply contradiction" claim.

---

# 16. Rank implications

The example above is rank one.

D50/D39 already isolate rank-one covariance as a special axial/Burgers-jet branch.

If the late survivor is required to remain genuinely rank two with:

\[
\lambda_{\min}^+(Q)\ge b_0>0,
\]

the admissible dual-lock cone narrows.

D96 does not yet prove it is empty.

But this suggests the correct next attack:

1. impose rank-two spectral gap;
2. impose D50 carrier-plane kernel geometry;
3. impose circulation detector sign;
4. impose SGS forward-work sign;
5. impose the X72 pressure/cofactor recurrence constraints.

This is much narrower than an arbitrary Young measure.

---

# 17. Updated phase-slip compiler

D95 had:

\[
\mathsf C_{\rm slip}.
\]

D96 refines:

\[
\boxed{
\mathsf C_{\rm slip}
\Longrightarrow
R_{\rm fiber}
\vee
R_{\rm conc}
\vee
R_{\rm state}
\vee
R_{\rm scale}
\vee
\mathsf C_{\rm nem}.
}
\tag{17.1}
\]

where:

\[
\boxed{
\mathsf C_{\rm nem}
}
\]

= **sign-locked deviatoric increment-covariance conveyor** satisfying:

\[
\sigma
\langle
A_\Gamma,Q^0
\rangle
\ge
c_{\rm slip}.
\]

On the compact recurrent strong branch, D26 adds a second recurring covariance/work projection.

Therefore:

\[
\boxed{
\mathsf C_{\rm nem}
\Longrightarrow
\mathsf C_{\rm dual}
\vee
R_{\rm state}
\vee
R_{\rm crit}.
}
\tag{17.2}
\]

No barycentric-bias terminal is required.

---

# 18. What has actually been eliminated

D96 eliminates the following false or overly broad endpoints.

## False endpoint A — "nonzero barycenter is necessary"

False.

The circulation functional is quadratic/even at the covariance level.

## False endpoint B — "sign-symmetric increments imply zero slip"

False.

\[
\nu(\xi)=\nu(-\xi)
\]

can have anisotropic covariance.

## True silent endpoint — isotropic covariance

\[
Q=aI
\Longrightarrow
\mathfrak F_\Gamma=0.
\]

## True silent endpoint — pressure-compatible covariance

\[
\nabla\times\nabla\cdot R=0
\Longrightarrow
\mathfrak F_\Gamma=0.
\]

## Surviving compact endpoint

\[
\boxed{
\text{sign-locked active deviatoric covariance}.
}
\]

---

# 19. Status ledger

## PROVED this round

### D96-P1 — smooth divergence-free loop-current detector after the D82 trace split.

### D96-P2 — SGS circulation is a linear functional of symmetric Reynolds covariance:

\[
\mathfrak F_\Gamma(R)
=
\int R:A_\Gamma.
\]

### D96-P3 — \(A_\Gamma\) is trace-free.

### D96-P4 — isotropic SGS covariance is circulation-silent.

### D96-P5 — full Young-profile representation gives slip as a deviatoric second-moment functional.

### D96-P6 — centered/sign-symmetric Young measures can support nonzero slip; barycentric bias is not necessary.

### D96-P7 — pressure-compatible covariance is circulation-silent.

### D96-P8 — same-sign phase slip forces a uniform deviatoric covariance projection and norm gap.

### D96-P9 — compact positive-density phase slip extracts a sign-locked Young-profile limit.

### D96-P10 — every detector-reversing state symmetry must be broken.

### D96-P11 — circulation reset and SGS energy work are two linear projections of the same deviatoric covariance.

### D96-P12 — pure covariance algebra does not exclude simultaneous positive circulation reset and forward SGS work.

### D96-P13 — final compact Young-profile survivor is a dual-locked deviatoric covariance cone, not a barycentric-bias branch.

---

# 20. What is NOT proved

D96 does not prove:

- the dual-lock covariance cone is empty;
- sign-coherent phase slip requires a nonzero first increment moment;
- all centered symmetric Young profiles are harmless;
- a positive circulation covariance projection implies positive SGS energy work;
- the rank-two carrier geometry automatically excludes the dual-lock cone;
- X72 automatically detects every active covariance;
- global Navier–Stokes regularity.

The next frontier is now a finite-dimensional covariance geometry problem coupled to the strict DSS/X72 dynamics.

---

# 21. STOP-D96

\[
\boxed{
\begin{minipage}{0.94\linewidth}
The D95 sign-coherent Kelvin phase-slip conveyor does not force an odd/barycentric bias in the increment Young profile. SGS circulation is generated by the Reynolds covariance, so its smoothed oriented loop detector is a linear functional of the **second moment**: \(\mathfrak F_\Gamma(R)=\int R:A_\Gamma\), where \(A_\Gamma=\operatorname{Sym}\nabla\Psi_\Gamma\) is trace-free. Consequently isotropic covariance is circulation-silent, and the D24 pressure-compatible covariance kernel is also circulation-silent, but a centered sign-symmetric Young measure may still carry positive slip; the explicit measure \(\frac12(\delta_{e_1}+\delta_{-e_1})\) already does so against a suitable trace-free detector. Therefore same-sign positive-density phase slip forces a **deviatoric/nematic covariance lock**, not a barycentric lock: \(\sigma\langle A_\Gamma,Q^0\rangle\ge c_{\rm slip}\). Fiber/concentration loss remains an explicit state/critical escape. On the compact strong-profile branch D26 supplies a second recurrence projection, SGS forward work, and both circulation reset and energy transfer are linear functionals of the same deviatoric covariance. Pure covariance algebra still allows both signs simultaneously, so the remaining survivor is a narrow **dual-locked positive-semidefinite covariance cone**. Eliminating it now requires rank-two carrier geometry, pressure/cofactor/X72 recurrence, or another dynamical compatibility theorem—not generic Young-measure symmetry.
\end{minipage}
}
\]

---

# 22. Next autonomous step

## DCRP97 / X72-R80 — Dual-Lock PSD Cone / Rank-Two X72 Compatibility

**Working title**

> **Can a Rank-Two Positive Semidefinite Increment Covariance Remain Simultaneously Locked to the Oriented Kelvin-Slip Detector and the SGS-Forward-Work Detector under Strict DSS/X72 Recurrence?**

Primary tasks:

1. start from the dual-lock covariance constraints:
   \[
   \sigma_\Gamma A_\Gamma:Q^0\ge c_\Gamma^*,
   \]
   \[
   -S_U:Q^0\ge c_E^*;
   \]
2. impose:
   \[
   Q\ge0,
   \qquad
   \operatorname{rank}Q=2,
   \qquad
   Qn=0,
   \qquad
   \lambda_{\min}^+(Q)\ge b_0;
   \]
3. parameterize:
   \[
   Q=aP_{n^\perp}+B^0_{\rm plane};
   \]
4. compute the dual inequalities as constraints on:
   - plane normal \(n\),
   - planar anisotropy,
   - strain eigenframe,
   - circulation-current detector frame;
5. test whether the fixed-plane / X72 pressure-response branches admit this cone;
6. if the cone is nonempty, classify its extremal rays;
7. send rank-one extremals to the D39 axial/Burgers branch;
8. seek:
   \[
   \mathcal C_{\rm dual}^{\rm rank2}
   \Longrightarrow
   X
   \vee
   R_{\rm state}
   \vee
   R_{\rm crit}
   \vee
   \text{one finite-dimensional extremal conveyor}.
   \]

Desired endpoint:

\[
\boxed{
\mathsf C_{\rm slip}
\Longrightarrow
\text{finite-dimensional rank-two covariance normal form}
\vee
R_{\rm state}
\vee
R_{\rm crit}.
}
\]

**End checkpoint:** DCRP96 / X72-R79.
