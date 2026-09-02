# DCRP73 / X72-R56 — Critical Cylinder Mosaic Absorption into Exact Inward Enstrophy Turnover

**Series:** Independent Navier–Stokes Research Series / X72 Bridge  
**Date:** 2026-08-18  
**Status:** Proof-development checkpoint / critical mosaic absorption  
**Immediate predecessor:** `NS_DCRP72_X72R55_CriticalTwistCollapse_CylinderMosaic_2026-08-18.md`

**Primary internal dependencies**
- DCRP-30 / RMRM native bounded-reservoir Morrey branch
- DCRP-35 — enstrophy stretching / inward-turnover dichotomy
- DCRP-38 / 59 — covariance-turnover ledger
- DCRP-56–58 / 71–72 — transparent cylindrical tail and multi-axis mosaic reduction
- DCRP-31 — finite-radius PFET branch

**Literature calibration**
- Chae–Tsai, *On discretely self-similar solutions of the Euler equations*, arXiv:1304.7414.
- Gibbon–Holm–Kerr–Roulstone, *Quaternions and particle dynamics in the Euler fluid equations*, arXiv:nlin/0512034.

No full Navier–Stokes regularity theorem is claimed.

---

# 0. Executive result

DCRP71's scope audit temporarily widened the native global frontier to

\[
\boxed{
\mathsf X_{\rm active}
\ \vee\
\mathsf T
\ \vee\
\mathsf C_{\rm mosaic}^{\rm crit},
}
\]

where DCRP72 reduced the critical transparent tail to a mosaic of straight cylindrical vorticity sectors separated by material vorticity-vacuum corridors.

DCRP73 shows that

\[
\boxed{
\mathsf C_{\rm mosaic}^{\rm crit}
}
\]

is **not an independent third branch**.

Every active cylindrical sector already lies exactly inside the inward-turnover branch \(\mathsf T\).

The reason is elementary once D72 has proved local translation invariance along the cylinder axis.

Let an active sector have fixed axis \(\eta\) and

\[
\boxed{
\Omega=a\,\eta,
}
\]

with

\[
\boxed{
\partial_\eta V=0.
}
\]

Then

\[
\boxed{
(\Omega\cdot\nabla)V
=
a\,\partial_\eta V
=
0.
}
\]

Therefore the similarity-vorticity equation

\[
D_s\Omega+\Omega=(\Omega\cdot\nabla)V
\]

reduces to

\[
\boxed{
D_s\Omega=-\Omega.
}
\]

Thus along every nonzero material vortex particle inside a cylindrical sector,

\[
\boxed{
\Omega(s)
=
e^{-(s-s_0)}\Omega(s_0).
}
\]

In particular:

- there is no vortex stretching;
- material vorticity direction is fixed;
- material vorticity magnitude decays exponentially in similarity time.

For the enstrophy density

\[
\boxed{
e_\omega=\frac12|\Omega|^2,
}
\]

we obtain

\[
\boxed{
D_se_\omega+2e_\omega=0.
}
\]

Since

\[
\nabla\cdot(\gamma y+V)=3\gamma,
\]

the conservative equation is

\[
\boxed{
\partial_se_\omega
+
\nabla\cdot(Ye_\omega)
+
(2-3\gamma)e_\omega
=
0,
}
\]

where

\[
Y=\gamma y+V.
\]

In the strict Type-II interior,

\[
\boxed{
2-3\gamma>0.
}
\]

Now take any fixed nonnegative observer cutoff \(\phi\).

Define

\[
\boxed{
E_\phi(s)
=
\int
\phi e_\omega\,dy.
}
\]

Then

\[
\boxed{
E_\phi'
+
(2-3\gamma)E_\phi
=
\int
(Y\cdot\nabla\phi)e_\omega\,dy.
}
\]

If the Eulerian DSS profile returns after one period,

\[
E_\phi(s+S_0)=E_\phi(s),
\]

so integration over one period gives the exact turnover budget

\[
\boxed{
\int_0^{S_0}
\int
(Y\cdot\nabla\phi)e_\omega\,dy\,ds
=
(2-3\gamma)
\int_0^{S_0}
E_\phi(s)\,ds.
}
\]

For a radial nonincreasing observer,

\[
\phi=\varphi(|y|),
\qquad
\varphi'\le0,
\]

the right side is strictly positive whenever the observed cylindrical vorticity is nonzero.

Since \(\nabla\phi\) points inward in the observer-sign convention, the left side is precisely a positive **inward enstrophy turnover**.

Equivalently, using the DCRP35 sphere flux

\[
\mathcal J_\omega(R)
=
\int_0^{S_0}
\int_{\partial B_R}
e_\omega
Y\cdot n\,dS\,ds,
\]

we obtain

\[
\boxed{
2
\int_0^\infty
[-\varphi'(R)]
\mathcal J_{\omega,\rm in}(R)\,dR
\ge
(2-3\gamma)
\int_0^{S_0}
\int
\phi|\Omega|^2\,dy\,ds.
}
\]

Thus every nonzero periodic cylindrical mosaic pays a positive turnover amount of exactly the same type already isolated in DCRP35/D59.

There is no separate mosaic equality route.

---

## Main confluence theorem

\[
\boxed{
\mathsf C_{\rm mosaic}^{\rm crit}
\Longrightarrow
\mathsf T.
}
\]

Therefore the strongest **native** rank-two global frontier is restored to

\[
\boxed{
\text{rank-two continuation}
\Longrightarrow
\mathsf X_{\rm active}
\ \vee\
\mathsf T.
}
\]

This conclusion no longer relies on the stronger Xue-type sublinear energy law.

The D71 audit remains important because it corrected the route by which the tail is handled:

- the mosaic need not be excluded as a flow geometry;
- it is instead **absorbed exactly into the material-turnover branch**.

This is logically stronger for the proof tree.

---

# 1. Cylindrical translation invariance

D72 proves on every active cylindrical sector:

\[
\boxed{
\partial_\eta V=0.
}
\]

The sector vorticity is:

\[
\boxed{
\Omega=a\eta.
}
\]

Therefore:

## Theorem D73.1 — Cylindrical Stretching Vanishes

\[
\boxed{
(\Omega\cdot\nabla)V=0.
}
\]

Consequently:

\[
\boxed{
\Omega\cdot S\Omega=0.
}
\]

The active cylindrical sector lies exactly on the **zero vortex-stretching** branch.

---

# 2. Material vorticity law

The similarity-vorticity equation is

\[
D_s\Omega+\Omega=(\Omega\cdot\nabla)V.
\]

Hence:

## Theorem D73.2 — Exact Material Cylinder Decay

\[
\boxed{
D_s\Omega=-\Omega.
}
\]

Therefore:

\[
\boxed{
\Omega(X(a,s),s)
=
e^{-(s-s_0)}
\Omega(a,s_0).
}
\]

The direction is material:

\[
\boxed{
D_s\frac{\Omega}{|\Omega|}=0.
}
\]

The amplitude obeys:

\[
\boxed{
D_s|\Omega|
=
-|\Omega|.
}
\]

---

# 3. Material enstrophy density

Let:

\[
e_\omega=\frac12|\Omega|^2.
\]

Then:

\[
\boxed{
D_se_\omega=-2e_\omega.
}
\]

The similarity flow has:

\[
\boxed{
\nabla\cdot Y=3\gamma.
}
\]

Thus:

## Theorem D73.3 — Conservative Cylinder-Enstrophy Equation

\[
\boxed{
\partial_se_\omega
+
\nabla\cdot(Ye_\omega)
+
c_\gamma e_\omega
=
0,
}
\]

where:

\[
\boxed{
c_\gamma=2-3\gamma>0.
}
\]

This is an exact linear transport-loss equation.

---

# 4. Material-volume interpretation

A similarity-material volume element satisfies:

\[
D_s(d\mu_Y)=3\gamma d\mu_Y.
\]

Therefore:

\[
\boxed{
D_s(e_\omega\,d\mu_Y)
=
-(2-3\gamma)
e_\omega\,d\mu_Y.
}
\]

Hence every material cylindrical enstrophy packet decays with multiplier:

\[
\boxed{
e^{-c_\gamma(s-s_0)}.
}
\]

After one DSS period:

\[
\boxed{
\mathcal E_{\rm mat}(s_0+S_0)
=
e^{-c_\gamma S_0}
\mathcal E_{\rm mat}(s_0).
}
\]

Since:

\[
c_\gamma>0,
\]

a nonzero material packet cannot return with the same enstrophy.

---

# 5. Fixed observer ledger

Let:

\[
0\le\phi\in C_c^\infty.
\]

Define:

\[
E_\phi(s)
=
\int
\phi e_\omega\,dy.
\]

Multiply D73.3 by \(\phi\) and integrate:

\[
\boxed{
E_\phi'
+
c_\gamma E_\phi
=
\int
(Y\cdot\nabla\phi)e_\omega\,dy.
}
\]

This is the exact fixed-observer enstrophy ledger for a zero-stretch cylindrical state.

---

# 6. Periodic return forces positive turnover

For an \(S_0\)-periodic Eulerian profile:

\[
E_\phi(s+S_0)=E_\phi(s).
\]

Therefore:

## Theorem D73.4 — Exact Periodic Cylinder Turnover Budget

\[
\boxed{
\int_0^{S_0}
\int
(Y\cdot\nabla\phi)e_\omega\,dy\,ds
=
c_\gamma
\int_0^{S_0}
E_\phi(s)\,ds.
}
\]

The right side is strictly positive whenever the observer sees nonzero cylindrical vorticity.

Thus a recurrent cylindrical sector cannot be maintained by same material alone.

Its Eulerian recurrence requires net inward material/enstrophy replacement.

---

# 7. Radial inward-flux form

Take:

\[
\phi(y)=\varphi(R),
\qquad
R=|y|,
\]

with:

\[
\varphi'(R)\le0.
\]

Then:

\[
Y\cdot\nabla\phi
=
\varphi'(R)Y\cdot n.
\]

By coarea:

\[
\begin{aligned}
&\int_0^{S_0}
\int
(Y\cdot\nabla\phi)e_\omega
\\
&=
\int_0^\infty
\varphi'(R)
\left[
\int_0^{S_0}
\int_{\partial B_R}
e_\omega
Y\cdot n\,dS\,ds
\right]dR.
\end{aligned}
\]

Define:

\[
\boxed{
\mathcal J_\omega(R)
=
\int_0^{S_0}
\int_{\partial B_R}
e_\omega
Y\cdot n\,dS\,ds.
}
\]

Then:

\[
\boxed{
c_\gamma
\int_0^{S_0}
E_\phi ds
=
\int_0^\infty
[-\varphi'(R)]
[-\mathcal J_\omega(R)]\,dR.
}
\]

Therefore:

## Theorem D73.5 — Smoothed Inward-Enstrophy Lower Bound

\[
\boxed{
\int_0^\infty
[-\varphi'(R)]
\mathcal J_{\omega,\rm in}(R)\,dR
\ge
c_\gamma
\int_0^{S_0}
E_\phi(s)\,ds.
}
\]

Equivalently in terms of \(|\Omega|^2\):

\[
\boxed{
2
\int_0^\infty
[-\varphi'(R)]
\mathcal J_{\omega,\rm in}(R)\,dR
\ge
c_\gamma
\int_0^{S_0}
\int
\phi|\Omega|^2\,dy\,ds.
}
\]

---

# 8. Relationship to DCRP35

DCRP35 had the general recurrent enstrophy dichotomy:

\[
\boxed{
\text{positive stretching}
\ \vee\
\text{inward enstrophy turnover}.
}
\]

The cylindrical mosaic satisfies:

\[
\boxed{
\Omega\cdot S\Omega=0.
}
\]

Therefore it lies **exactly** in the turnover side.

D73 does not create a new turnover mechanism.

It identifies the critical mosaic as a concrete equality geometry whose recurrence is possible only through the already existing \(\mathsf T\) channel.

---

# 9. Relationship to DCRP59

DCRP59's turnover branch obeys a lower bound of the form:

\[
\int
[-\varphi']
\mathcal J_{\omega,\rm in}
\gtrsim
(2-3\gamma)
\int
Z_{\rm in}.
\]

D73 recovers the same coefficient directly from the cylindrical zero-stretch equation.

Thus the D59 turnover gap is not merely a covariance artifact.

On the mosaic tail it is the exact physical similarity-enstrophy balance.

---

# 10. Vacuum corridors do not rescue material recurrence

D72 proves that axis changes occur only through material vorticity-vacuum corridors.

Because nonzero vorticity cannot become zero along a smooth material trajectory, a nonzero vortex particle cannot cross through the vacuum corridor and emerge in a different-axis sector.

Therefore the multi-axis mosaic cannot recycle one vortex packet by rotating it through the vacuum.

Each active sector has its own material vorticity population.

Every such population obeys the exponential decay law D73.2.

Thus Eulerian periodicity must be sustained by material relabeling/replacement at the observer level.

---

# 11. Finite sector cycles are impossible without replenishment

Suppose the one-period material return permutes a finite collection of cylindrical sectors.

For a sector material enstrophy:

\[
\mathcal E_j
\mapsto
e^{-c_\gamma S_0}
\mathcal E_j.
\]

After a finite permutation cycle of length \(N\):

\[
\mathcal E_j
\mapsto
e^{-Nc_\gamma S_0}
\mathcal E_j.
\]

If the sector returns to itself and is nonzero:

\[
1=e^{-Nc_\gamma S_0},
\]

impossible because:

\[
c_\gamma>0.
\]

Thus:

## Theorem D73.6 — Finite Material-Sector Cycle NO-GO

A nonzero recurrent cylindrical mosaic cannot be a finite closed material permutation with zero replenishment.

Any recurrent realization needs:

- inward observer turnover;
- or an infinite same-parent material conveyor.

Both belong to the material-turnover branch \(\mathsf T\).

---

# 12. Infinite conveyor interpretation

A formally possible mosaic recurrence is:

\[
A_0
\to
A_1
\to
A_2
\to\cdots
\]

with the Eulerian observer seeing identical recurrent statistics while successive material populations carry the state.

This is not a new equality branch.

It is the strongest form of material replacement.

Hence:

\[
\boxed{
\text{infinite cylinder conveyor}
\subset
\mathsf T.
}
\]

---

# 13. Native branch-tree repair after D71 audit

D71 correctly widened the native frontier temporarily:

\[
\mathsf X_{\rm active}
\vee
\mathsf T
\vee
\mathsf C_{\rm mosaic}^{\rm crit}.
\]

D73 now proves:

\[
\boxed{
\mathsf C_{\rm mosaic}^{\rm crit}
\subseteq
\mathsf T.
}
\]

Therefore:

## Theorem D73.7 — Native Two-Branch Frontier Restored

\[
\boxed{
\text{rank-two continuation}
\Longrightarrow
\mathsf X_{\rm active}
\vee
\mathsf T.
}
\]

This result is native to the bounded-reservoir Morrey branch and does not require the stronger Xue-type sublinear energy assumption.

---

# 14. Why this is stronger than simply excluding the mosaic

A direct geometric NO-GO for all multi-axis mosaics would be useful but is not necessary for the proof tree.

D73 proves something structurally better:

> even if the mosaic exists as a smooth critical Euler geometry, it has no zero-turnover recurrence.

Therefore its entire recurrence problem is already absorbed into the final material branch.

The global proof no longer needs to classify every possible multi-axis harmonic interaction before proceeding.

---

# 15. Updated final two branches

After D73 the native frontier is again:

## X — active pressure/cofactor/transport branch

Some finite same-parent region pays:

\[
\boxed{
\mathfrak a_X>0
}
\]

or the equivalent X72 pressure/shape/transport defect.

## T — material turnover branch

The recurrence is maintained by:

\[
\boxed{
\text{inward enstrophy turnover / material replacement}.
}
\]

The critical mosaic, infinite conveyor, and cylindrical tail all sit inside T.

No third native endpoint remains.

---

# 16. The final T branch now has an exact no-stretch submodel

The cylindrical subbranch of T satisfies the exact law:

\[
\boxed{
\partial_se_\omega
+
\nabla\cdot(Ye_\omega)
+
c_\gamma e_\omega=0.
}
\]

Thus its turnover requirement is quantitatively sharp.

This makes it a useful model for the general T branch.

The remaining major question is whether the same finite annular material package can simultaneously support:

1. D73 inward enstrophy replacement;
2. D31 inward PFET / energy-pressure transfer;
3. same-parent critical scaling;
4. finite-energy Navier–Stokes ancestry.

This is now the highest-leverage T attack.

---

# 17. X versus T priority after D73

The X branch has already been compressed to an active finite pressure/cofactor/shape transition.

The T branch now contains:

- the old D35 turnover escape;
- the D59 covariance-turnover branch;
- the entire native critical cylindrical/mosaic endpoint.

Therefore T is now the broader remaining escape.

The next autonomous priority should be:

\[
\boxed{
\textbf{joint enstrophy-turnover / PFET finite-annulus coupling}.
}
\]

If this coupling can be closed, the material branch collapses substantially.

---

# 18. Status ledger

## PROVED this round

### D73-P1 — cylindrical vortex stretching vanishes

\[
(\Omega\cdot\nabla)V=0.
\]

### D73-P2 — exact material vorticity decay

\[
D_s\Omega=-\Omega.
\]

### D73-P3 — exact conservative cylinder-enstrophy law

\[
\partial_se_\omega+\nabla\cdot(Ye_\omega)+(2-3\gamma)e_\omega=0.
\]

### D73-P4 — exact periodic observer turnover budget.

### D73-P5 — quantitative smoothed inward-enstrophy lower bound.

### D73-P6 — finite material-sector cycles cannot recur without replenishment.

### D73-P7 — critical cylinder mosaic is absorbed into T.

### D73-P8 — native two-branch frontier restored

\[
\boxed{
\mathsf X_{\rm active}\vee\mathsf T.
}
\]

---

# 19. New STOP

\[
\boxed{
\textbf{
STOP-D73:
The native critical cylinder/vacuum mosaic is not an independent endgame branch. D72's local cylinder-line velocity invariance makes vortex stretching identically zero, so material vorticity decays exactly as }e^{-s}\textbf{ and material enstrophy as }e^{-(2-3\gamma)s}\textbf{ after similarity-volume correction. A periodic Eulerian cylinder state therefore requires a strictly positive inward enstrophy/material replacement budget. The entire critical mosaic endpoint is absorbed into the existing T turnover branch, restoring the native global frontier to X-active versus material turnover.
}
}
\]

---

# 20. Next autonomous step

## DCRP74 / X72-R57 — Joint Enstrophy-Turnover / PFET Annulus

**Working title**

> **One Finite Matching Annulus Carrying Both Vorticity Replacement and Energy–Pressure Transfer**

Primary tasks:

1. place D73 inward enstrophy turnover and D31 inward PFET on the same finite normalized annulus;
2. derive exact local flux ledgers for:
   - enstrophy;
   - kinetic energy;
   - Bernoulli/pressure work;
3. test whether zero/weak correlation between the two currents is possible under the actual Euler equations;
4. use D49's independence warning to avoid false universal identification;
5. search for a weaker but sufficient joint-annulus inequality:
   \[
   \mathfrak J_{\omega,\rm in}
   +
   \mathfrak F_{\rm PFET}
   \gtrsim
   \text{recurrent core demand};
   \]
6. perform same-parent scaling audit;
7. determine whether T can be absorbed into:
   - X pressure work;
   - finite annular strain supplier;
   - or one explicit critical conveyor normal form.

Desired endpoint:

\[
\boxed{
\mathsf T
\Longrightarrow
\text{joint finite-annulus tax}
\vee
\text{one explicit material-conveyor equality mode}.
}
\]

---

# 21. One-line checkpoint

The D71 audit has fully reconverged: even if the critical multi-axis cylinder mosaic exists geometrically, its zero-stretch cylindrical dynamics force exact exponential material-enstrophy decay, so periodic recurrence necessarily pays inward material/enstrophy turnover; the native proof tree is again reduced to only active X72 transition versus T turnover.

---

**End checkpoint:** DCRP73 / X72-R56  
**Next:** DCRP74 / X72-R57 — Joint Enstrophy Turnover / PFET Annulus.
