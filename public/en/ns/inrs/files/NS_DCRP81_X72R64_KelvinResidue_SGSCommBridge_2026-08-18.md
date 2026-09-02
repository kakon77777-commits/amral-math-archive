# DCRP81 / X72-R64 — Mesoscopic Kelvin Decomposition and the SGS-Circulation Bridge

**Series:** Independent Navier–Stokes Research Series / X72 Bridge  
**Date:** 2026-08-18  
**Status:** Proof-development checkpoint / uniquely Navier–Stokes terminal branch  
**Immediate predecessor:** `NS_DCRP80_X72R63_NoncompactAbsorption_TerminalCompiler_2026-08-18.md`

**Primary internal dependencies**
- DCRP33 — second-order viscous Kelvin residue
- DCRP20–26 / RMRM filtered-vorticity branch — differentiated commutator forcing and derivative-compatible increment detector
- DCRP79–80 — material noncompactness compiler

**Fresh external calibration**
- Runlong Yu, *Filtered Vortex Stretching and Subgrid Defects for the Three-Dimensional Navier-Stokes Equations*, arXiv:2606.27560 (2026): the spatially filtered vorticity equation contains the differentiated subgrid-stress forcing \(-\nabla\times\nabla\cdot R_\ell\), controlled in the filtered-enstrophy architecture by diffusion, derivative-compatible increment defects, and localization residuals.
- Drivas–Holm, *Circulation and Energy Theorem Preserving Stochastic Fluids*, arXiv:1808.05308: smooth Navier–Stokes admits generalized Kelvin-type circulation structures, while ordinary deterministic material-loop circulation is not conserved.
- Eyink, *Turbulent Cascade of Circulations* / Kelvin-theorem anomaly work (2006): coarse-grained circulation naturally exposes an interscale circulation flux.

No external theorem is used to prove the exact decomposition below.

No full Navier–Stokes regularity theorem is claimed.

---

# 0. Executive result

DCRP80 left one uniquely Navier–Stokes-specific terminal coordinate:

\[
\boxed{
\mathsf R_K
}
\]

with one-period viscous Kelvin residue

\[
\boxed{
\mathfrak K_n^{\rm visc}(C_n)
=
\varepsilon_n
\int_0^{S_0}
\oint_{C_n(\tau)}
\Delta v_n\cdot dy\,d\tau.
}
\]

DCRP81 shows that this residue is not an irreducible mysterious second-order object.

After mesoscopic filtering it decomposes **exactly** into:

1. filtered viscous circulation;
2. subgrid-stress / commutator circulation flux;
3. filtered-vs-exact material-loop shadowing mismatch.

Let

\[
U_{n,\ell}
=
\varphi_\ell*v_n
\]

and define the subgrid stress

\[
\boxed{
R_{n,\ell}
=
\varphi_\ell*(v_n\otimes v_n)
-
U_{n,\ell}\otimes U_{n,\ell}.
}
\]

Let \(C_{n,\ell}(\tau)\) be the loop transported by the filtered velocity \(U_{n,\ell}\), with the same initial geometric loop as \(C_n(0)\).

Define the filtered circulation

\[
\boxed{
\Gamma_{n,\ell}(\tau)
=
\oint_{C_{n,\ell}(\tau)}
U_{n,\ell}\cdot dy.
}
\]

Then:

## Exact filtered Kelvin law

\[
\boxed{
\frac d{d\tau}
\Gamma_{n,\ell}
=
\varepsilon_n
\oint_{C_{n,\ell}}
\Delta U_{n,\ell}\cdot dy
-
\oint_{C_{n,\ell}}
\nabla\cdot R_{n,\ell}\cdot dy.
}
\]

Define

\[
\boxed{
\mathfrak K_{n,\ell}^{\rm fvisc}
=
\varepsilon_n
\int_0^{S_0}
\oint_{C_{n,\ell}}
\Delta U_{n,\ell}\cdot dy\,d\tau,
}
\]

and

\[
\boxed{
\mathfrak K_{n,\ell}^{\rm sgs}
=
-
\int_0^{S_0}
\oint_{C_{n,\ell}}
\nabla\cdot R_{n,\ell}\cdot dy\,d\tau.
}
\]

Let the endpoint circulation-shadowing mismatch be

\[
\boxed{
\mathfrak M_{n,\ell}
=
\left[
\Gamma_n-\Gamma_{n,\ell}
\right]_{\tau=S_0}
-
\left[
\Gamma_n-\Gamma_{n,\ell}
\right]_{\tau=0}.
}
\]

Then:

## Main exact decomposition

\[
\boxed{
\mathfrak K_n^{\rm visc}
=
\mathfrak M_{n,\ell}
+
\mathfrak K_{n,\ell}^{\rm fvisc}
+
\mathfrak K_{n,\ell}^{\rm sgs}.
}
\]

This identity is exact for every smooth \(n,\ell\).

---

## Mesoscopic filtered viscosity disappears

Assume on the declared loop tube:

- loop lengths are uniformly bounded:
  \[
  \sup_{n,\tau}
  \operatorname{Length}(C_{n,\ell_n}(\tau))
  \le L_*;
  \]
- the loops remain in one fixed normalized compact region;
- the local \(L^2\) kinetic-energy norm is uniformly bounded over one return interval.

For a standard three-dimensional mollifier,

\[
\boxed{
\|\Delta\varphi_\ell\|_2
=
C_\varphi\ell^{-7/2}.
}
\]

Thus:

\[
\boxed{
\|\Delta U_{n,\ell}\|_\infty
\le
C_\varphi
\ell^{-7/2}
\|v_n\|_2.
}
\]

Hence:

\[
\boxed{
|\mathfrak K_{n,\ell}^{\rm fvisc}|
\le
C
\varepsilon_n
\ell^{-7/2}.
}
\]

Choose a mesoscopic filter scale

\[
\boxed{
\ell_n
=
\varepsilon_n^p,
\qquad
0<p<\frac27.
}
\]

Then:

\[
\boxed{
\varepsilon_n
\ell_n^{-7/2}
=
\varepsilon_n^{1-\frac72p}
\to0.
}
\]

Therefore:

\[
\boxed{
\mathfrak K_{n,\ell_n}^{\rm fvisc}
\to0.
}
\]

So the apparently second-order viscous residue cannot survive through the smooth low-frequency filtered sector unless the loop geometry/local energy assumptions themselves fail.

---

## Nonzero Kelvin residue becomes commutator flux or shadowing failure

Suppose:

\[
\boxed{
\limsup_n
|\mathfrak K_n^{\rm visc}|
>0.
}
\]

If:

\[
\boxed{
\mathfrak M_{n,\ell_n}\to0,
}
\]

and the compact loop assumptions hold, then the exact decomposition gives:

\[
\boxed{
\limsup_n
|\mathfrak K_{n,\ell_n}^{\rm sgs}|
>0.
}
\]

Thus:

## Main confluence theorem

\[
\boxed{
\mathsf R_K
\Longrightarrow
\mathsf R_{\rm SGS\mbox{-}circ}
\vee
\mathsf R_{\rm fil}
\vee
\mathsf R_{\rm state}
\vee
\mathsf R_{\rm tail}.
}
\]

Here \(\mathsf R_{\rm SGS\mbox{-}circ}\) is **not a new PDE forcing**.

It is a material-loop projection of the already-known differentiated commutator forcing.

Indeed, if \(\Sigma_{n,\ell}(\tau)\) spans \(C_{n,\ell}(\tau)\), Stokes gives

\[
\boxed{
\begin{aligned}
\mathfrak K_{n,\ell}^{\rm sgs}
&=
-
\int_0^{S_0}
\int_{\Sigma_{n,\ell}}
\left[
\nabla\times\nabla\cdot R_{n,\ell}
\right]\cdot n_\Sigma
\,dA\,d\tau.
\end{aligned}
}
\]

But

\[
\boxed{
-\nabla\times\nabla\cdot R_{n,\ell}
}
\]

is exactly the differentiated subgrid-stress forcing in the filtered vorticity equation.

So \(R_K\) has been reduced from a separate second-order viscous terminal coordinate to a **visibility problem for an already-declared finite-scale commutator force**, plus the already-known material noncompactness branches.

---

# 1. Exact normalized Navier–Stokes setup

Use the DCRP33 normalized prelimit equation:

\[
\boxed{
\partial_\tau v_n
+
(v_n\cdot\nabla)v_n
+
\nabla p_n
=
\varepsilon_n\Delta v_n,
}
\tag{1.1}
\]

with

\[
\boxed{
\nabla\cdot v_n=0,
\qquad
\varepsilon_n\to0.
}
\]

Let \(C_n(\tau)\) be a \(v_n\)-material loop.

Then:

\[
\boxed{
\frac d{d\tau}
\Gamma_n(\tau)
=
\varepsilon_n
\oint_{C_n(\tau)}
\Delta v_n\cdot dy.
}
\tag{1.2}
\]

Integrating:

\[
\boxed{
\Gamma_n(S_0)-\Gamma_n(0)
=
\mathfrak K_n^{\rm visc}.
}
\tag{1.3}
\]

---

# 2. Spatial filtering

Let:

\[
\varphi_\ell(x)
=
\ell^{-3}\varphi(x/\ell),
\]

with smooth compactly supported or Schwartz mollifier.

Define:

\[
\boxed{
U_\ell
=
\varphi_\ell*v,
}
\]

and:

\[
\boxed{
R_\ell
=
\varphi_\ell*(v\otimes v)
-
U_\ell\otimes U_\ell.
}
\]

Filtering (1.1) gives:

## Theorem D81.1 — Exact Filtered Momentum Equation

\[
\boxed{
\partial_\tau U_\ell
+
(U_\ell\cdot\nabla)U_\ell
+
\nabla P_\ell
=
\varepsilon\Delta U_\ell
-
\nabla\cdot R_\ell.
}
\tag{2.1}
\]

---

# 3. Filtered material loop

Let \(C_\ell(\tau)\) satisfy:

\[
\boxed{
\partial_\tau X_\ell(a,\tau)
=
U_\ell(X_\ell(a,\tau),\tau).
}
\tag{3.1}
\]

Choose:

\[
\boxed{
C_\ell(0)=C(0).
}
\tag{3.2}
\]

Define:

\[
\boxed{
\Gamma_\ell(\tau)
=
\oint_{C_\ell(\tau)}
U_\ell\cdot dy.
}
\]

For a vector field \(A\), circulation along its own material loop obeys:

\[
\frac d{d\tau}
\oint_{C_A}A\cdot dy
=
\oint_{C_A}
\left[
\partial_\tau A
+
(A\cdot\nabla)A
\right]\cdot dy,
\]

because:

\[
(\nabla A)^TA
=
\nabla\frac{|A|^2}{2}
\]

has zero circulation.

Insert (2.1).

---

# 4. Exact filtered Kelvin equation

The pressure term is a gradient and integrates to zero.

Therefore:

## Theorem D81.2 — Filtered Kelvin / SGS Circulation Law

\[
\boxed{
\frac d{d\tau}
\Gamma_\ell
=
\varepsilon
\oint_{C_\ell}
\Delta U_\ell\cdot dy
-
\oint_{C_\ell}
\nabla\cdot R_\ell\cdot dy.
}
\tag{4.1}
\]

This is the exact finite-scale circulation identity needed by the terminal compiler.

---

# 5. One-period filtered terms

Define:

\[
\boxed{
\mathfrak K_\ell^{\rm fvisc}
=
\varepsilon
\int_0^{S_0}
\oint_{C_\ell}
\Delta U_\ell\cdot dy\,d\tau,
}
\tag{5.1}
\]

and:

\[
\boxed{
\mathfrak K_\ell^{\rm sgs}
=
-
\int_0^{S_0}
\oint_{C_\ell}
\nabla\cdot R_\ell\cdot dy\,d\tau.
}
\tag{5.2}
\]

Then:

\[
\boxed{
\Gamma_\ell(S_0)-\Gamma_\ell(0)
=
\mathfrak K_\ell^{\rm fvisc}
+
\mathfrak K_\ell^{\rm sgs}.
}
\tag{5.3}
\]

---

# 6. Endpoint loop-shadowing mismatch

Define:

\[
\boxed{
M_\ell(\tau)
=
\Gamma(\tau)-\Gamma_\ell(\tau).
}
\tag{6.1}
\]

Then:

\[
\Gamma(S_0)-\Gamma(0)
=
M_\ell(S_0)-M_\ell(0)
+
\Gamma_\ell(S_0)-\Gamma_\ell(0).
\]

Therefore:

## Theorem D81.3 — Exact Three-Term Kelvin Decomposition

\[
\boxed{
\mathfrak K^{\rm visc}
=
\mathfrak M_\ell
+
\mathfrak K_\ell^{\rm fvisc}
+
\mathfrak K_\ell^{\rm sgs},
}
\tag{6.2}
\]

where:

\[
\boxed{
\mathfrak M_\ell
=
M_\ell(S_0)-M_\ell(0).
}
\tag{6.3}
\]

No approximation has entered yet.

---

# 7. Meaning of \(\mathfrak M_\ell\)

The mismatch contains:

1. field filtering error:
   \[
   v-U_\ell;
   \]
2. geometric loop-flow mismatch:
   \[
   C(\tau)-C_\ell(\tau);
   \]
3. any endpoint material-return mismatch.

Thus if:

\[
\mathfrak M_{\ell_n}\not\to0,
\]

the branch is already in:

\[
\boxed{
\mathsf R_{\rm state}
\vee
\mathsf R_{\rm fil},
}
\]

or, if the loops leave every fixed normalized compact region:

\[
\boxed{
\mathsf R_{\rm tail}.
}
\]

So a nonvanishing mismatch is not a hidden Kelvin equality branch.

---

# 8. Filtered viscous bound

For a loop \(C_\ell\):

\[
\left|
\oint_{C_\ell}
\Delta U_\ell\cdot dy
\right|
\le
\operatorname{Length}(C_\ell)
\|\Delta U_\ell\|_\infty.
\]

By Young's inequality:

\[
\boxed{
\|\Delta U_\ell\|_\infty
\le
\|\Delta\varphi_\ell\|_2
\|v\|_2.
}
\tag{8.1}
\]

In three dimensions:

\[
\boxed{
\|\Delta\varphi_\ell\|_2
=
\ell^{-7/2}
\|\Delta\varphi\|_2.
}
\tag{8.2}
\]

Therefore:

## Theorem D81.4 — Low-Frequency Viscous Kelvin Bound

\[
\boxed{
|\mathfrak K_\ell^{\rm fvisc}|
\le
C_\varphi
\varepsilon
\ell^{-7/2}
\int_0^{S_0}
L_\ell(\tau)
\|v(\tau)\|_{L^2(K_\ell)}
d\tau.
}
\tag{8.3}
\]

Here \(K_\ell\) is any fixed compact region containing the filtered loop and the mollifier neighborhood.

---

# 9. Mesoscopic scale window

Assume:

\[
\sup_{\tau,n}
L_{n,\ell_n}(\tau)
\le L_*,
\]

and:

\[
\int_0^{S_0}
\|v_n(\tau)\|_{L^2(K_*)}d\tau
\le E_*.
\]

Choose:

\[
\boxed{
\ell_n
=
\varepsilon_n^p.
}
\]

Then:

\[
|\mathfrak K_{n,\ell_n}^{\rm fvisc}|
\le
C
\varepsilon_n^{1-\frac72p}.
\]

Hence:

## Theorem D81.5 — Mesoscopic Filtered-Viscosity Vanishing

For every:

\[
\boxed{
0<p<\frac27,
}
\]

\[
\boxed{
\mathfrak K_{n,\ell_n}^{\rm fvisc}
\to0.
}
\tag{9.1}
\]

The filter scale tends to zero but remains large enough that explicit viscosity cannot sustain the low-frequency circulation defect.

---

# 10. Why failure of the mesoscopic hypotheses is already known

If:

\[
L_{n,\ell_n}\to\infty,
\]

the material/filtered loop is filamenting:

\[
\boxed{
\mathsf R_{\rm fil}.
}
\]

If the loop or filter tube leaves every fixed normalized compact set:

\[
\boxed{
\mathsf R_{\rm tail}.
}
\]

If local \(L^2\) control fails on the declared normalized compact class:

\[
\boxed{
\mathsf R_{\rm state}
}
\]

or a retained concentration/energy compactness defect is already present.

Thus the low-frequency estimate does not introduce a new escape.

---

# 11. Subgrid circulation flux is a vorticity commutator projection

Let \(\Sigma_\ell(\tau)\) be a smooth oriented surface spanning \(C_\ell(\tau)\).

By Stokes:

\[
\oint_{C_\ell}
\nabla\cdot R_\ell\cdot dy
=
\int_{\Sigma_\ell}
\nabla\times\nabla\cdot R_\ell
\cdot n_\Sigma\,dA.
\]

Therefore:

## Theorem D81.6 — SGS Circulation / Filtered-Vorticity Forcing Identity

\[
\boxed{
\mathfrak K_\ell^{\rm sgs}
=
\int_0^{S_0}
\int_{\Sigma_\ell}
\mathcal C_\ell^\omega
\cdot n_\Sigma\,dA\,d\tau,
}
\tag{11.1}
\]

where:

\[
\boxed{
\mathcal C_\ell^\omega
=
-\nabla\times\nabla\cdot R_\ell.
}
\tag{11.2}
\]

This is exactly the differentiated subgrid-stress forcing appearing in the filtered-vorticity equation.

So the Kelvin residue has been converted into a surface visibility functional of an already-known commutator field.

---

# 12. Nonzero \(R_K\) reduction

Suppose:

\[
\limsup_n
|\mathfrak K_n^{\rm visc}|
>0.
\]

Take:

\[
\ell_n=\varepsilon_n^p,
\qquad
0<p<2/7.
\]

If:

- loop length stays bounded;
- loop support stays compact;
- local energy stays controlled;
- endpoint circulation shadowing satisfies:
  \[
  \mathfrak M_{n,\ell_n}\to0,
  \]

then D81.3 and D81.5 give:

## Theorem D81.7 — Kelvin-to-SGS Reduction

\[
\boxed{
\limsup_n
|\mathfrak K_{n,\ell_n}^{\rm sgs}|
>0.
}
\tag{12.1}
\]

Therefore:

\[
\boxed{
\mathsf R_K
\Longrightarrow
\mathsf R_{\rm SGS\mbox{-}circ}
\vee
\mathsf R_{\rm fil}
\vee
\mathsf R_{\rm state}
\vee
\mathsf R_{\rm tail}.
}
\tag{12.2}
\]

---

# 13. Relationship to the existing filtered-vorticity compiler

The earlier filtered-vorticity branch already uses:

\[
\boxed{
R_\ell
=
S_\ell(u\otimes u)
-
U_\ell\otimes U_\ell,
}
\]

and:

\[
\boxed{
-\nabla\times\nabla\cdot R_\ell.
}
\]

The differentiated commutator forcing is controlled in that architecture by an estimate of the form:

\[
\boxed{
F_\ell^{\rm com}
\le
\eta P_\ell
+
\frac{C}{\eta}
\widetilde{\mathcal S}^{(3)}_\ell
+
L_\ell^{\rm com}.
}
\]

The critical detector:

\[
\boxed{
\widetilde{\mathcal S}^{(3)}
}
\]

is already scale invariant and already present in the finite obstruction architecture.

Therefore \(\mathsf R_{\rm SGS\mbox{-}circ}\) does **not** require inventing a new PDE forcing or a new derivative-compatible increment detector.

The remaining issue is narrower:

> does the existing volumetric/localized commutator control automatically control the singular material-loop / spanning-surface circulation functional?

That is a **visibility/trace problem**, not a new Navier–Stokes mechanism.

---

# 14. Important STOP against overclaiming

D81 does **not** prove:

\[
\mathfrak K_{n,\ell_n}^{\rm sgs}
\neq0
\Longrightarrow
\widetilde{\mathcal S}^{(3)}\not\to0
\]

under the current hypotheses.

Why not?

Because the Kelvin functional pairs the commutator forcing against a codimension-one spanning surface / codimension-two boundary loop.

Existing filtered-enstrophy commutator estimates are volumetric localized estimates.

A trace/tube-thickening step is needed to pass between them without losing critical scaling.

Thus:

\[
\boxed{
\mathsf R_K
}
\]

is not yet fully eliminated.

But it has been reduced to:

\[
\boxed{
\textbf{
material-loop trace visibility of an already-known SGS commutator forcing.
}
}
\]

This is a much narrower terminal problem.

---

# 15. Tube-thickening candidate

Let:

\[
J_{C_\ell}
\]

be the vector-valued current of the loop.

Instead of pairing the forcing with the singular loop/surface current directly, introduce a tube-thickened current at thickness:

\[
\delta
=
\theta\ell.
\]

Then seek:

\[
\boxed{
\mathfrak K_\ell^{\rm sgs}
=
\langle
\mathcal C_\ell^\omega,
N_{\Sigma_\ell,\delta}
\rangle
+
\mathsf E_{\rm trace},
}
\]

where \(N_{\Sigma,\delta}\) is a smooth approximate surface-normal field.

If:

\[
\mathsf E_{\rm trace}\to0
\]

under bounded curvature/area/tubular radius, the volumetric commutator estimate can be applied directly.

If the trace error does not vanish, the surface geometry itself is losing compactness:

\[
\boxed{
\mathsf R_{\rm fil}
\vee
\mathsf R_{\rm state}.
}
\]

This is the natural next route.

---

# 16. Updated terminal compiler

D80 had:

\[
\boxed{
\mathsf O_{\rm PFET}
\wedge
(
\mathsf X
\vee
\mathsf R_{\rm tail}
\vee
\mathsf R_{\rm fil}
\vee
\mathsf R_{\rm state}
\vee
\mathsf R_K
).
}
\]

D81 replaces the irreducible \(R_K\) label by:

\[
\boxed{
\mathsf R_{\rm SGS\mbox{-}circ}
\vee
\mathsf R_{\rm fil}
\vee
\mathsf R_{\rm state}
\vee
\mathsf R_{\rm tail}.
}
\]

Hence:

## Theorem D81.8 — Refined Terminal Compiler

Under the mesoscopic compact-loop hypotheses:

\[
\boxed{
\mathsf O_{\rm PFET}
\wedge
\left(
\mathsf X
\vee
\mathsf R_{\rm tail}
\vee
\mathsf R_{\rm fil}
\vee
\mathsf R_{\rm state}
\vee
\mathsf R_{\rm SGS\mbox{-}circ}
\right).
}
\tag{16.1}
\]

The uniquely Navier–Stokes-specific “second-order Kelvin” label has disappeared.

The remaining Navier–Stokes content is a finite-scale subgrid commutator visibility problem.

---

# 17. Why this is a real narrowing

Before D81:

\[
\varepsilon_n
\oint
\Delta v_n
\]

could survive through unbounded second derivatives with no obvious finite-scale interpretation.

After D81:

- its mesoscopic filtered viscous component vanishes;
- its loop-shadowing failure is already a material transition defect;
- its surviving compact part is exactly a surface flux of:
  \[
  -\nabla\times\nabla\cdot R_\ell.
  \]

That forcing already belongs to the filtered-vorticity PDE architecture.

So there is no longer a mysterious independent second-order mechanism.

The open issue is only whether a singular surface trace can hide from the already-controlled volumetric commutator detector.

---

# 18. Status ledger

## PROVED this round

### D81-P1 — exact filtered momentum equation.

### D81-P2 — exact filtered Kelvin circulation equation.

### D81-P3 — exact three-term Kelvin decomposition:

\[
\mathfrak K^{\rm visc}
=
\mathfrak M_\ell
+
\mathfrak K_\ell^{\rm fvisc}
+
\mathfrak K_\ell^{\rm sgs}.
\]

### D81-P4 — low-frequency filtered viscous estimate:

\[
|\mathfrak K_\ell^{\rm fvisc}|
\lesssim
\varepsilon\ell^{-7/2}.
\]

### D81-P5 — mesoscopic window:

\[
\ell_n=\varepsilon_n^p,
\qquad
0<p<2/7
\]

forces:

\[
\mathfrak K_{n,\ell_n}^{\rm fvisc}\to0.
\]

### D81-P6 — SGS circulation is exactly a spanning-surface pairing of the differentiated filtered-vorticity commutator forcing.

### D81-P7 — nonzero Kelvin residue reduces to SGS-circulation visibility or already-known loop/material noncompactness.

### D81-P8 — \(R_K\) is no longer an irreducible terminal PDE mechanism.

---

# 19. What is not proved

D81 does not yet prove:

- surface/loop SGS circulation is controlled by the existing volumetric \(\widetilde{\mathcal S}^{(3)}\) detector at critical scaling;
- all filtered-loop shadowing errors vanish;
- material spanning surfaces retain uniform tubular geometry;
- the SGS circulation flux is impossible.

Those are now the precise remaining obligations.

---

# 20. New STOP

\[
\boxed{
\textbf{
STOP-D81:
The second-order viscous Kelvin residue is not an independent mysterious terminal mechanism. After filtering, it decomposes exactly into endpoint material-loop shadowing mismatch, filtered viscous circulation, and SGS circulation flux. At the mesoscopic scale }\ell_n=\varepsilon_n^p,\ 0<p<2/7,\textbf{ bounded loop geometry and local energy force the explicit filtered-viscous term to vanish. Therefore any surviving compact Kelvin residue is exactly a material-surface flux of the already-known filtered-vorticity commutator force }-\nabla\times\nabla\cdot R_{\ell_n}\textbf{. The only remaining gap is whether this codimension-one/codimension-two circulation trace can hide from the existing volumetric derivative-compatible commutator detector; failure of the required loop/surface shadowing is already filamentation/state/tail noncompactness.}
}
\]

---

# 21. Next autonomous step

## DCRP82 / X72-R65 — Loop-Surface Commutator Trace Visibility

**Working title**

> **Tube-Thickening the SGS Circulation Flux into the Existing Volumetric Commutator Detector**

Primary tasks:

1. thicken the material spanning surface \(\Sigma_{n,\ell}\) to a tube of width:
   \[
   \delta_n=\theta\ell_n;
   \]
2. build a smooth approximate surface-current field \(N_{\Sigma,\delta}\);
3. rewrite:
   \[
   \int_{\Sigma}
   \mathcal C_\ell^\omega\cdot n
   \]
   as a volumetric pairing plus a trace error;
4. estimate the volumetric pairing using the existing differentiated-commutator bound:
   \[
   \eta P
   +
   C_\eta\widetilde{\mathcal S}^{(3)}
   +
   L^{\rm com};
   \]
5. show the trace error vanishes under bounded surface area, curvature, and tubular radius;
6. if those geometric bounds fail, route directly to:
   \[
   \mathsf R_{\rm fil}\vee\mathsf R_{\rm state};
   \]
7. seek:
   \[
   \mathsf R_{\rm SGS\mbox{-}circ}
   \Longrightarrow
   \widetilde{\mathcal S}^{(3)}
   \vee
   \mathsf R_{\rm fil}
   \vee
   \mathsf R_{\rm state}
   \vee
   \mathsf R_{\rm loc}.
   \]

Desired endpoint:

\[
\boxed{
\mathsf R_K
\Longrightarrow
\text{already-existing finite-scale defect coordinates only}.
}
\]

---

# 22. One-line checkpoint

The prelimit Kelvin residue has been converted into an ordinary finite-scale commutator visibility problem: under compact loop geometry its explicit viscous low-frequency part vanishes at mesoscopic scale, leaving only the SGS differentiated-commutator circulation flux or already-declared material noncompactness.

---

**End checkpoint:** DCRP81 / X72-R64  
**Next:** DCRP82 / X72-R65 — Loop-Surface Commutator Trace Visibility.
