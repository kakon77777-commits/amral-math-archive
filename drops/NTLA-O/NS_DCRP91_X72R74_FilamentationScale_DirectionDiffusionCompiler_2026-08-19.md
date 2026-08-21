# DCRP91 / X72-R74 — Filamentation-Scale Extraction, Carrier-Lock Compiler, and the Removal of an Independent Material-Filamentation Terminal

**Series:** Independent Navier–Stokes Research Series / X72 Bridge  
**Date:** 2026-08-19  
**Status:** Proof-development checkpoint / Kelvin-forced filamentation round  
**Immediate predecessor:** `NS_DCRP90_X72R73_FiniteTimeTailTransport_NoGo_2026-08-19.md`

**Primary internal dependencies**
- DCRP50 — thickness-scale curvature / filtered vorticity covariance / direction compiler
- DCRP71 — native time-slice Morrey control
- DCRP79–80 — material filamentation as inherited noncompactness
- DCRP85 — relative-scale escape / finite-chain gap debt
- DCRP88–90 — finite-depth Kelvin ancestry and support-escape closure

**Fresh primary-source calibration**
- R. Yu, *Filtered Vortex Stretching and Subgrid Defects for the Three-Dimensional Navier-Stokes Equations*, arXiv:2606.27560 (2026).
- Z. Grujić, *Logarithmic Depletion of Vortex Stretching and Singularity Evasion in the 3D Navier-Stokes Equations*, arXiv:2607.08866 (2026).
- A. Emam, M. Kamal, P. L. Johnson, *Turbulence Without the Viscous Tilting of Vorticity*, arXiv:2606.17330 (2026).
- B. Galanti, J. D. Gibbon, M. Heritage, *Vorticity alignment results for the three-dimensional Euler and Navier-Stokes equations*, arXiv:chao-dyn/9709003.

No external theorem is used to identify a generic material-line tangent with the vorticity direction.

No full Navier–Stokes regularity theorem is claimed.

---

# 0. Executive result

DCRP90 removed tame material support escape.

Thus the D88 finite-depth Kelvin ancestry can no longer evade compactness by transporting a geometrically tame circulation loop to arbitrarily large normalized radius and then returning it to the core.

The remaining material escape was:

\[
\boxed{
R_{\rm fil}
}
\]

= material-line / material-sheet / director / spatial-equicontinuity filamentation.

DCRP91 proves that this is **not an independent terminal coordinate**.

The first part is purely geometric.

Let:

\[
C\subset B_{R_*}\subset\mathbb R^3
\]

be a closed \(C^2\) material loop.

If:

\[
\operatorname{reach}(C)\ge\tau>0,
\]

then the normal tube of radius:

\[
r=\tau/2
\]

is embedded.

Its volume is:

\[
\boxed{
|T_r(C)|
=
\pi r^2L(C).
}
\]

Since:

\[
T_r(C)\subset B_{R_*+r},
\]

we obtain the exact packing bound:

\[
\boxed{
L(C)
\le
\frac43
\frac{
(R_*+r)^3
}{
r^2
}.
}
\]

At \(r=\tau/2\),

\[
\boxed{
L(C)
\le
\frac{16}{3}
\frac{
(R_*+\tau/2)^3
}{
\tau^2
}.
}
\tag{0.1}
\]

Therefore, on the D90 bounded-support branch:

\[
\boxed{
L(C_n)\to\infty
\Longrightarrow
\operatorname{reach}(C_n)\to0.
}
\tag{0.2}
\]

So loop-length explosion is not a separate endpoint.

A bounded-support material-line filament can lose compactness only by:

1. reach collapse / self-approach;
2. curvature-scale collapse;
3. material-map / parameterization / state compactness failure;
4. field/director oscillation at a shrinking spatial scale.

The second part inserts D50.

On the declared **carrier-locked rank-two subbranch**, meaning that the circulation carrier remains coupled to the coherent filtered-vorticity covariance/tube state, D50 gives:

\[
\boxed{
\text{thickness-scale folding}
\Longrightarrow
\text{tube multiplicity}
\vee
\text{rank transition}
\vee
\text{filtered vorticity-gradient gap}
\vee
\text{curvature-gradient transition}.
}
\tag{0.3}
\]

The filtered vorticity-gradient gap further splits into:

\[
\boxed{
\text{magnitude-gradient}
\vee
\text{direction-gradient}.
}
\]

At fixed relative filter scale:

\[
\ell=\sigma r,
\]

the direction branch lies in the same pairwise direction-defect / difference-quotient / filtered-diffusion sector of the 2026 filtered-vorticity theorem.

But DCRP91 does **not** reverse that theorem blindly.

Instead it uses the correct scale dichotomy:

- if the filament witness occurs at a fixed relative scale, it is already an existing finite-scale rank/gradient/direction-diffusion coordinate;
- if the witness is pushed to:
  \[
  \ell/r_{\rm core}\to0,
  \]
  it is exactly:
  \[
  R_{\rm scale},
  \]
  already converted by D85 into a finite-chain gap debt or critical-reservoir escape;
- if carrier-lock fails, the failure is:
  \[
  R_{\rm state}.
  \]

Thus:

# Main filamentation compiler

\[
\boxed{
R_{\rm fil}
\Longrightarrow
R_{\rm state}
\vee
R_{\rm scale}
\vee
R_{\rm FV},
}
\tag{0.4}
\]

where \(R_{\rm FV}\) is an already-existing fixed-relative filtered-vorticity rank/gradient/direction-diffusion witness.

Moreover, \(R_{\rm FV}\) cannot by itself be an indefinitely compact material-regeneration endpoint:

- bounded fixed-scale rank/gradient states belong to a compact finite-scale package;
- D88 Kelvin holonomy forbids indefinitely recycling one compact circulation ancestry;
- unbounded finite-scale gradient/rank amplitudes are themselves state/reservoir noncompactness.

Hence for an **infinite same-parent regeneration chain**:

\[
\boxed{
R_{\rm fil}^{\infty}
\Longrightarrow
R_{\rm scale}
\vee
R_{\rm state}
\vee
\text{existing active finite-scale FV defect}.
}
\tag{0.5}
\]

No new “material filamentation terminal” is required.

---

# 1. Why material lines must not be identified with vorticity directions

A material-line tangent \(t\) obeys the deformation dynamics generated by:

\[
\nabla(\gamma y+U).
\]

The vorticity direction:

\[
\xi=\frac{\Omega}{|\Omega|}
\]

obeys a different equation, and in Navier–Stokes viscosity introduces additional directional realignment.

Therefore the implication:

\[
\boxed{
\text{material-line folding}
\Longrightarrow
\text{vorticity-direction folding}
}
\]

is **not universal**.

D91 uses the vorticity-direction compiler only under the declared carrier-lock condition.

If the circulation-carrying material geometry and the filtered-vorticity covariance geometry cease to shadow one another, this is recorded as:

\[
\boxed{
R_{\rm lock}
\subseteq
R_{\rm state}.
}
\tag{1.1}
\]

This avoids a false material-line/vorticity identification.

---

# 2. Exact tube-volume formula for a closed curve

Let:

\[
C
\]

be a closed embedded \(C^2\) curve of length:

\[
L.
\]

Assume:

\[
0<r<\operatorname{reach}(C).
\]

Choose a smooth orthonormal normal frame:

\[
n_1(s),n_2(s).
\]

The normal tube map is:

\[
\boxed{
F(s,\rho,\theta)
=
C(s)
+
\rho
[
\cos\theta\,n_1(s)
+
\sin\theta\,n_2(s)
].
}
\]

For \(r<\operatorname{reach}(C)\), this map is injective.

Its Jacobian has the form:

\[
J
=
\rho
[
1-\rho\,\kappa_\theta(s)
].
\]

Integrating over:

\[
\theta\in[0,2\pi]
\]

cancels the curvature term:

\[
\int_0^{2\pi}
\kappa_\theta(s)d\theta
=
0.
\]

Therefore:

## Theorem D91.1 — Embedded Tube Volume

\[
\boxed{
|T_r(C)|
=
\pi r^2L(C).
}
\tag{2.1}
\]

No asymptotic error is required for a closed embedded tube below reach.

---

# 3. Bounded support + positive reach gives a length ceiling

Assume:

\[
C\subset B_{R_*}.
\]

Then:

\[
T_r(C)
\subset
B_{R_*+r}.
\]

Thus:

\[
\pi r^2L(C)
\le
\frac{4\pi}{3}(R_*+r)^3.
\]

Hence:

## Theorem D91.2 — Tube-Packing Length Bound

\[
\boxed{
L(C)
\le
\frac43
\frac{
(R_*+r)^3
}{
r^2
}.
}
\tag{3.1}
\]

Set:

\[
r=\tau/2.
\]

If:

\[
\operatorname{reach}(C)\ge\tau,
\]

then:

\[
\boxed{
L(C)
\le
\frac{16}{3}
\frac{
(R_*+\tau/2)^3
}{
\tau^2
}.
}
\tag{3.2}
\]

Therefore:

## Corollary D91.3 — Length Filamentation Forces Reach Collapse

On a fixed bounded-support class:

\[
\boxed{
L(C_n)\to\infty
\Longrightarrow
\operatorname{reach}(C_n)\to0.
}
\tag{3.3}
\]

The D89 “length-first” branch is therefore subsumed by reach/tube degeneration once D90 has closed support escape.

---

# 4. Reach collapse has two geometric realizations

For embedded \(C^2\) curves, small reach occurs through two basic mechanisms.

## A. local curvature scale

There exist points with:

\[
\boxed{
\kappa_{\max}
\gtrsim
\operatorname{reach}(C)^{-1}.
}
\]

This is curvature-scale folding.

## B. global self-approach

Two distinct pieces of the loop approach within:

\[
O(\operatorname{reach}(C))
\]

while curvature remains moderate.

This is tube self-intersection / nearest-point nonuniqueness.

Therefore:

## Theorem D91.4 — Reach-Collapse Split

\[
\boxed{
\operatorname{reach}(C_n)\to0
\Longrightarrow
R_{\rm curv\mbox{-}scale}
\vee
R_{\rm mult}.
}
\tag{4.1}
\]

The second branch is already:

\[
\boxed{
R_{\rm mult}
\subset
R_{\rm state}.
}
\]

---

# 5. Material-map Jacobian degeneration

A material loop is not only a geometric curve.

It also carries an ancestry map.

Let:

\[
J_{\rm line}
=
\left|
\partial_aX(a,s)
\right|.
\]

Suppose the geometric image remains inside a bounded-support positive-reach class, but:

\[
\sup J_{\rm line}\to\infty
\]

or:

\[
\inf J_{\rm line}\to0.
\]

Then the material parameterization/ancestry state loses compactness without necessarily changing the geometric loop class.

This is:

## Theorem D91.5 — Pure Material-Map Filamentation Is State Noncompactness

\[
\boxed{
R_{J}
\subseteq
R_{\rm state}.
}
\tag{5.1}
\]

No new geometric terminal is needed.

---

# 6. Director oscillation scale extraction

Let:

\[
\xi_n
\]

be a normalized direction field on a bounded carrier patch.

If:

\[
\xi_n
\]

fails spatial equicontinuity while remaining bounded in magnitude, then there exist:

\[
x_n,y_n
\]

with:

\[
\ell_n
=
|x_n-y_n|
\to0
\]

such that:

\[
\boxed{
|\xi_n(x_n)-\xi_n(y_n)|
\ge
\delta_0>0.
}
\tag{6.1}
\]

Thus:

## Theorem D91.6 — Director Noncompactness Creates a Vanishing Active Scale

\[
\boxed{
R_{\rm dir\mbox{-}osc}
\Longrightarrow
\ell_n\to0
}
\tag{6.2}
\]

unless the field-state topology itself fails in another coordinate.

So director filamentation is already a relative-scale phenomenon.

---

# 7. Carrier-lock condition

D50 applies to a coherent rank-two filtered-vorticity covariance state.

Let:

\[
C_\ell
\]

be the trace-one positive semidefinite filtered vorticity covariance, and let:

\[
n
\]

be the material carrier plane normal.

Carrier-lock means schematically:

\[
\boxed{
C_\ell n\approx0
}
\tag{7.1}
\]

with a positive rank-two spectral gap:

\[
\boxed{
\lambda_{\min}^{+}(C_\ell)
\ge
b_0>0.
}
\tag{7.2}
\]

Failure gives:

\[
\boxed{
\text{rank lifting / plane spread}
\vee
\text{rank-one collapse}
\vee
\text{carrier-lock failure}.
}
\]

All are already existing rank/state coordinates.

---

# 8. Insert D50 at the filament scale

Suppose curvature/reach filamentation occurs on a carrier-locked rank-two patch at scale:

\[
\ell_n.
\]

D50 proves, along a subsequence, at least one of:

\[
\boxed{
\operatorname{reach}(\Sigma_n)
\le
\ell_n;
}
\]

\[
\boxed{
\lambda_{\min}^{+}(C_{\ell_n})
\to0;
}
\]

\[
\boxed{
|C_{\ell_n}n_n|
\ge
c_{\rm rank}>0;
}
\]

\[
\boxed{
\ell_n^2
\frac{
\eta_{\ell_n}*
|\nabla\Omega_{\ell_n}|^2
}{
\eta_{\ell_n}*
|\Omega_{\ell_n}|^2
}
\ge
c_{\rm grad}>0;
}
\]

or:

\[
\boxed{
\ell_n^2
|\nabla_{\Sigma_n}\mathrm{II}_n|
\ge
c_{\rm II}>0.
}
\]

Thus:

## Theorem D91.7 — Carrier-Locked Filamentation Visibility

\[
\boxed{
R_{\rm curv\mbox{-}scale}
\Longrightarrow
R_{\rm state}
\vee
R_{\rm grad}
\vee
R_{\rm geom2}.
}
\tag{8.1}
\]

Here:

- \(R_{\rm state}\) includes tube multiplicity and rank transitions;
- \(R_{\rm grad}\) is the filtered-vorticity gradient witness;
- \(R_{\rm geom2}\) is second-order tube-geometry transition.

The filament is PDE-visible; it is not merely a geometric decoration.

---

# 9. Magnitude / direction split

Write:

\[
\Omega_\ell
=
\rho_\ell\xi_\ell.
\]

Then:

\[
\boxed{
|\nabla\Omega_\ell|^2
=
|\nabla\rho_\ell|^2
+
\rho_\ell^2|\nabla\xi_\ell|^2.
}
\tag{9.1}
\]

Therefore the D50 gradient witness splits into:

\[
\boxed{
R_{\rm mag}
\vee
R_{\rm dir}.
}
\tag{9.2}
\]

More quantitatively, D50 gives at least one of:

\[
\boxed{
\ell^2
\frac{
\eta_\ell*
|\nabla\rho_\ell|^2
}{
m_\ell
}
\gtrsim
(\ell|\mathrm{II}|)^2
}
\]

or:

\[
\boxed{
\ell^2
\frac{
\eta_\ell*
[
\rho_\ell^2|\nabla\xi_\ell|^2
]
}{
m_\ell
}
\gtrsim
(\ell|\mathrm{II}|)^2.
}
\]

---

# 10. Exact pairwise magnitude/direction identity

For two filtered vorticity states:

\[
\Omega_x
=
\rho_x\xi_x,
\qquad
\Omega_y
=
\rho_y\xi_y,
\]

with:

\[
|\xi_x|=|\xi_y|=1,
\]

one has:

## Theorem D91.8 — Pairwise Vorticity Decomposition

\[
\boxed{
|\Omega_x-\Omega_y|^2
=
(\rho_x-\rho_y)^2
+
2\rho_x\rho_y
[
1-\xi_x\cdot\xi_y
].
}
\tag{10.1}
\]

Thus every fixed-scale pairwise vorticity increment splits exactly into:

- magnitude variation;
- magnitude-weighted direction variation.

This is the finite-difference counterpart of (9.1).

---

# 11. Fixed relative scale versus shrinking relative scale

Let:

\[
r_{\rm core}
\]

be the recurrent core scale.

Consider the filament witness scale:

\[
\ell_n.
\]

There are two cases.

## A. fixed relative scale

There exists:

\[
\sigma_0>0
\]

such that:

\[
\boxed{
\ell_n/r_{\rm core}
\ge
\sigma_0.
}
\tag{11.1}
\]

Then all D50 / filtered-vorticity constants remain uniform on the normalized class.

The witness is already a finite-scale:

\[
\boxed{
R_{\rm FV}
}
\]

coordinate:

- rank transition;
- vorticity-gradient activity;
- direction/magnitude pair defect;
- localization / filtered diffusion sector;
- second-order tube-state transition.

## B. shrinking relative scale

\[
\boxed{
\ell_n/r_{\rm core}\to0.
}
\tag{11.2}
\]

This is exactly:

\[
\boxed{
R_{\rm scale}.
}
\]

D50 had previously left this bridge open.

D83–85 have now developed the relative-filter / subfilter / scale-gap compiler.

Therefore the old D50 “filter-ratio caution” is no longer an unclassified endpoint in the present late chain.

---

# 12. External filtered-vorticity direction calibration

The 2026 filtered-vorticity theorem proves:

1. positive near-field filtered vortex stretching is bounded by a magnitude-weighted pairwise direction defect;
2. the angular defect is converted to a first-order filtered-vorticity difference quotient;
3. that term is absorbed by filtered diffusion up to a lower-order filtered-enstrophy reservoir;
4. differentiated stress forcing is controlled by a scale-invariant derivative-compatible velocity-increment defect.

Therefore the D50 direction branch belongs to an already-developed finite-scale diffusive/commutator sector.

D91 uses this only in the forward direction supported by the theorem.

It does **not** claim:

\[
\boxed{
\text{direction gradient}
\Longrightarrow
\text{positive vortex stretching}
}
\]

without additional hypotheses.

---

# 13. Spectral/scale caution

A large:

\[
\ell^2
\|\nabla\Omega_\ell\|_2^2
\]

can in principle be carried by an even smaller spatial frequency scale.

Therefore D91 does not infer a lower pairwise direction defect from a gradient lower bound without a scale-locality hypothesis.

Instead:

\[
\boxed{
\text{gradient witness at fixed relative scale}
}
\]

is retained as \(R_{\rm FV}\);

while concentration into:

\[
\ll\ell
\]

is:

\[
\boxed{
R_{\rm scale}.
}
\]

This is the correct non-overclaiming split.

---

# 14. Why fixed-scale \(R_{\rm FV}\) is not a new infinite material terminal

Suppose:

- support remains bounded;
- the filament witness stays at one fixed relative scale;
- rank amplitudes / filtered gradient amplitudes remain bounded above;
- carrier-lock remains valid;
- material/state maps remain compact.

Then the normalized package lies in a compact finite-scale state class.

But D88 Kelvin holonomy proves that a nonzero circulation atom cannot recycle one compact material ancestry indefinitely.

Therefore:

## Theorem D91.9 — Fixed-Scale Filament Witness Is Transient or Noncompact

An infinite same-parent regeneration chain cannot survive solely by repeatedly visiting one bounded fixed-scale \(R_{\rm FV}\) state.

It must eventually pay one of:

\[
\boxed{
R_{\rm scale}
\vee
R_{\rm state}
\vee
R_{\rm crit}.
}
\tag{14.1}
\]

where \(R_{\rm crit}\) means amplitude/reservoir blow-up of the finite-scale witness.

Thus \(R_{\rm FV}\) is an active finite-depth witness, not an independent infinite terminal.

---

# 15. Generic material-line filamentation compiler

We can now compile generic material-line complexity without assuming vorticity lock.

On the D90 bounded-support branch:

## loop-length explosion

\[
L\to\infty
\Longrightarrow
\operatorname{reach}\to0.
\]

## reach collapse by self-approach

\[
\Longrightarrow
R_{\rm state}.
\]

## reach collapse by curvature scale

either carrier-lock fails:

\[
\Longrightarrow
R_{\rm state},
\]

or D50 produces:

\[
R_{\rm FV}
\vee
R_{\rm scale}
\vee
R_{\rm state}.
\]

## material-map Jacobian degeneration

\[
\Longrightarrow
R_{\rm state}.
\]

## director oscillation

\[
\Longrightarrow
R_{\rm scale}
\vee
R_{\rm state}
\vee
R_{\rm FV}.
\]

Therefore:

## Theorem D91.10 — Finite-Depth Filamentation Compiler

\[
\boxed{
R_{\rm fil}
\Longrightarrow
R_{\rm state}
\vee
R_{\rm scale}
\vee
R_{\rm FV}.
}
\tag{15.1}
\]

No additional material-filamentation terminal is needed.

---

# 16. Insert D85 scale-gap debt

D85 converted relative-scale escape into:

\[
\boxed{
R_{\rm scale}
\Longrightarrow
\mathfrak D_{\rm gap}
\vee
R_{\rm crit}.
}
\tag{16.1}
\]

Therefore:

## Theorem D91.11 — Filamentation-to-Known-Debt Reduction

\[
\boxed{
R_{\rm fil}
\Longrightarrow
R_{\rm state}
\vee
R_{\rm FV}
\vee
\mathfrak D_{\rm gap}
\vee
R_{\rm crit}.
}
\tag{16.2}
\]

The generic filamentation label has disappeared.

---

# 17. Insert D82–85 increment reduction

D90 already gave:

\[
\boxed{
\text{same-parent material regeneration}
\Longrightarrow
R_{\rm inc}
\vee
R_{\rm fil}
\vee
R_{\rm state}.
}
\]

D82–85 reduce the increment branch to:

\[
\boxed{
R_{\rm inc}
\Longrightarrow
\widetilde{\mathcal S}_{\rm active}
\vee
\mathfrak D_{\rm gap}
\vee
R_{\rm state}
\vee
R_{\rm crit}.
}
\tag{17.1}
\]

Insert D91.11.

Therefore:

# Theorem D91.12 — Material-Regeneration Finite-Coordinate Compiler

\[
\boxed{
\text{same-parent material regeneration}
\Longrightarrow
\widetilde{\mathcal S}_{\rm active}
\vee
R_{\rm FV}
\vee
\mathfrak D_{\rm gap}
\vee
R_{\rm state}
\vee
R_{\rm crit}.
}
\tag{17.2}
\]

No independent:

- tail;
- Kelvin;
- trace;
- line-atom;
- scale;
- material-filamentation

terminal survives in the late material ancestry branch.

All have been converted into already-declared finite-scale / state / critical-reservoir coordinates.

---

# 18. What \(R_{\rm FV}\) contains

The fixed-relative filtered-vorticity witness \(R_{\rm FV}\) is not one scalar.

It is the finite compiler:

\[
\boxed{
R_{\rm FV}
=
R_{\rm rank}
\vee
R_{\rm mag}
\vee
R_{\rm dir}
\vee
R_{\rm geom2}
\vee
R_{\rm loc/diff}.
}
\]

where:

### \(R_{\rm rank}\)

rank-one collapse / rank lifting / plane-spread;

### \(R_{\rm mag}\)

filtered vorticity magnitude-gradient activity;

### \(R_{\rm dir}\)

magnitude-weighted vorticity-direction activity;

### \(R_{\rm geom2}\)

curvature-gradient / second-order tube-state transition;

### \(R_{\rm loc/diff}\)

filtered diffusion / localization reservoir in the external finite-scale balance.

These are all pre-existing coordinates from D50 and the filtered-vorticity program.

---

# 19. Why \(R_{\rm FV}\) is retained instead of falsely called “paid”

The external direction theorem is coercive in a localized filtered-enstrophy balance.

But the present Type-II/same-parent proof still has critical recurrence and scale-weight issues.

Therefore D91 does not write:

\[
R_{\rm FV}
\Longrightarrow
\text{global contradiction}.
\]

It writes:

\[
\boxed{
R_{\rm FV}
=
\text{existing finite-scale PDE-visible coordinate}.
}
\]

The remaining global question is how recurrent \(R_{\rm FV}\) events couple to the existing forest/work/PFET ledgers.

This is a budget problem, not a hidden filament geometry problem.

---

# 20. Relation to X72

No direct implication:

\[
R_{\rm fil}
\Longrightarrow
X
\]

is asserted.

If a rank/shape/pressure-cofactor transition occurs, X72 remains available.

But D91 does not force all vorticity or material-line filamentation into the pressure-response tensor.

This preserves the independence of:

- geometry;
- filtered vorticity;
- pressure/cofactor response;
- PFET.

---

# 21. Relation to D31 PFET

D31 still gives:

\[
\boxed{
\mathcal O_{\rm PFET}>0
}
\]

simultaneously for every nonzero compact strict DSS profile.

D91 does not identify:

\[
\mathcal O_{\rm PFET}
\]

with:

\[
R_{\rm FV}
\]

or:

\[
\mathfrak D_{\rm gap}.
\]

The late architecture therefore remains a joint-obligation statement.

---

# 22. Updated late architecture

The current strict same-parent rank-two branch now carries:

\[
\boxed{
\mathcal O_{\rm PFET}
}
\]

and, on the material-regeneration side, at least one of:

\[
\boxed{
\widetilde{\mathcal S}_{\rm active}
\vee
R_{\rm FV}
\vee
\mathfrak D_{\rm gap}
\vee
R_{\rm state}
\vee
R_{\rm crit}.
}
\]

Remote Eulerian FAR interaction remains separately:

\[
\boxed{
R_{\rm far\mbox{-}amp}
\vee
\text{comparable-annulus/reservoir alternatives}.
}
\]

This is now a finite terminal compiler with no generic “tail” or “filament” placeholder.

---

# 23. Status ledger

## PROVED this round

### D91-P1 — exact embedded tube-volume formula

\[
|T_r(C)|=\pi r^2L(C).
\]

### D91-P2 — bounded support + positive reach gives a uniform loop-length ceiling.

### D91-P3 — bounded-support length explosion forces reach collapse.

### D91-P4 — reach collapse splits into curvature-scale collapse or tube self-approach/multiplicity.

### D91-P5 — pure material-map Jacobian degeneration is state compactness failure.

### D91-P6 — director spatial non-equicontinuity extracts a vanishing active spatial scale.

### D91-P7 — carrier-lock failure is a state/rank transition, not a hidden equality mode.

### D91-P8 — D50 curvature compiler inserted at the filament scale.

### D91-P9 — exact magnitude/direction decomposition of filtered-vorticity gradient and pairwise increments.

### D91-P10 — fixed-relative filament witnesses are existing finite-scale filtered-vorticity coordinates; shrinking relative witnesses are \(R_{\rm scale}\).

### D91-P11 — no independent infinite fixed-scale filamentation terminal on the compact Kelvin ancestry branch.

### D91-P12 — material-filamentation terminal absorbed:

\[
R_{\rm fil}
\Longrightarrow
R_{\rm state}
\vee
R_{\rm FV}
\vee
\mathfrak D_{\rm gap}
\vee
R_{\rm crit}.
\]

### D91-P13 — material-regeneration compiler reduced to already-known finite coordinates.

---

# 24. What is not proved

D91 does not prove:

- recurrent \(R_{\rm FV}\) has a globally non-summable budget;
- every material-line tangent is aligned with vorticity;
- every curvature event creates positive near-field vortex stretching;
- filtered direction-gradient activity automatically implies X72;
- remote Eulerian FAR sources are impossible;
- state/multiplicity noncompactness is impossible;
- global Navier–Stokes regularity.

The remaining problem is now the recurrence/budget of **already-visible finite-scale defects**, not classification of another material escape.

---

# 25. New STOP

\[
\boxed{
\textbf{
STOP-D91:
After D90 closes material support escape, generic material filamentation no longer survives as an independent terminal. In a bounded normalized support, a positive reach bound automatically controls loop length through the exact tube formula }|T_r(C)|=\pi r^2L(C)\textbf{, so length blow-up forces reach collapse. Reach collapse is either tube self-approach/multiplicity, hence state noncompactness, or curvature-scale collapse. On the declared rank-two carrier-locked branch, D50 compiles curvature folding into rank transition, filtered-vorticity gradient/direction activity, or second-order tube geometry; if the carrier-lock fails, that failure is already a state transition. A filament witness pushed to vanishing relative scale is precisely the relative-filter/scale escape already converted by D85 into a finite-chain gap debt. At fixed relative scale it is an already-existing filtered-vorticity finite-scale coordinate; the 2026 direction-defect theorem places its direction sector in the established difference-quotient/diffusion architecture, but D91 does not reverse that theorem or equate material-line and vorticity directions. Thus }R_{\rm fil}\textbf{ is absorbed into }R_{\rm state}\vee R_{\rm FV}\vee\mathfrak D_{\rm gap}\vee R_{\rm crit}\textbf{, and the same-parent material-regeneration branch now terminates only in already-declared finite-scale/state/reservoir coordinates.}
}
\]

---

# 26. Next autonomous step

## DCRP92 / X72-R75 — Finite-Scale Defect Recurrence Confluence

**Working title**

> **Can the Remaining \(R_{\rm FV}\), Increment, Gap-Debt, and Work-Visible Coordinates Be Forced into One Recurrent Joint Budget?**

Primary tasks:

1. start from the D91 finite material-regeneration compiler:
   \[
   \widetilde{\mathcal S}_{\rm active}
   \vee
   R_{\rm FV}
   \vee
   \mathfrak D_{\rm gap}
   \vee
   R_{\rm state}
   \vee
   R_{\rm crit};
   \]
2. remove \(R_{\rm state}\) / \(R_{\rm crit}\) by treating them as explicit noncompact terminals rather than equality states;
3. compare the three finite-scale active coordinates:
   - derivative-compatible velocity increment;
   - filtered-vorticity rank/gradient/direction;
   - CKN bad-scale gap debt;
4. connect all of them to D87 signed-work visibility where possible;
5. determine whether a recurrent same-parent finite-scale defect can remain pressure-compatible/work-orthogonal at every generation;
6. use X72 only on the pressure-perfect recurrent residue;
7. seek:
   \[
   \text{finite-scale recurrent defect}
   \Longrightarrow
   W_+
   \vee
   W_-
   \vee
   X
   \vee
   R_{\rm state}
   \vee
   R_{\rm crit};
   \]
8. audit whether the remaining weighted summability can again be bypassed by ancestry/holonomy rather than raw energy.

Desired endpoint:

\[
\boxed{
\text{late material branch}
\Longrightarrow
\text{one joint finite recurrent defect package}.
}
\]

---

# 27. One-line checkpoint

Material support and material filamentation are now both removed as generic terminal labels: finite-depth Kelvin regeneration can survive only through already-visible increment, filtered-vorticity, scale-gap, state, or critical-reservoir coordinates.

---

**End checkpoint:** DCRP91 / X72-R74  
**Next:** DCRP92 / X72-R75 — Finite-Scale Defect Recurrence Confluence.
