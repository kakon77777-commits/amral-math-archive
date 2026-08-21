# DCRP84 / X72-R67 — Logarithmic Capacity of Matched Line Atoms and Absorption into Relative-Scale Escape

**Series:** Independent Navier–Stokes Research Series / X72 Bridge  
**Date:** 2026-08-18  
**Status:** Proof-development checkpoint / nested matched-atom round  
**Immediate predecessor:** `NS_DCRP83_X72R66_SubfilterTraceReroot_AtomTrichotomy_2026-08-18.md`

**Primary internal dependencies**
- DCRP20 — fixed-relative-filter / relative-frequency escape caution
- DCRP24 — persistent derivative-compatible increment / fiber compactness compiler
- DCRP50 — nested-scale / relative-filter compiler caution
- DCRP82–83 — trace ratio, subfilter extraction, and matched material-line atom

**Fresh external calibration**
- Runlong Yu, *Filtered Vortex Stretching and Subgrid Defects for the Three-Dimensional Navier-Stokes Equations*, arXiv:2606.27560.
- Gregory L. Eyink, *The Cascade of Circulations in Fluid Turbulence*, arXiv:physics/0606159.
- Zoran Grujić, *Logarithmic Depletion of Vortex Stretching and Singularity Evasion in the 3D Navier-Stokes Equations*, arXiv:2607.08866. This is used only as calibration that logarithmic geometric effects genuinely occur at critical vorticity concentration; no theorem from it is imported below.

No full Navier–Stokes regularity theorem is claimed.

---

# 0. Executive result

DCRP83 reduced the material-line Kelvin trace gap to:

\[
\boxed{
R_{\rm tr}
\Longrightarrow
R_{\rm ratio}
\vee
R_{\rm atom}
\vee
R_{\rm mult}.
}
\]

The strongest branch was the matched atom \(R_{\rm atom}\):

- a thinner transverse scale \(r_1\ll r_0\) is extracted;
- the active increment displacement also collapses to scale \(r_1\);
- one parabolic line cell retains enough mass to carry a scale-invariant line-increment obstruction.

DCRP84 shows two things.

First:

> **native Morrey energy and ordinary viscous-gradient packing do not directly exclude a nested matched line atom.**

The codimension-two transverse problem is logarithmically critical.

Second, and more importantly:

> **an infinite matched-atom recursion with silent volumetric increment detector is itself an already-known relative-scale escape.**

Thus the apparent \(R_{\rm atom}\) terminal branch is absorbed.

The main late reduction becomes:

\[
\boxed{
R_{\rm tr}
\Longrightarrow
\widetilde{\mathcal S}_{\rm vol}^{\rm active}
\vee
R_{\rm scale}
\vee
R_{\rm state}.
}
\]

Here \(R_{\rm scale}\) is the pre-existing nested-scale / relative-filter / shell-span escape coordinate.

No independent matched-line-atom endpoint remains.

---

# 1. One coherent matched line atom

Fix one matched material-line atom at scale:

\[
\boxed{
r.
}
\]

Use a parabolic line cell with:

- material-line arc length \(O(r)\);
- time length \(O(r^2)\);
- active velocity-increment displacement:
  \[
  |z|\sim r.
  \]

After the D83 displacement/fiber selection, either:

1. a fixed scalar/vector increment component carries a definite fraction of the atom;
2. or increment-fiber/multiplicity compactness fails.

The second route is already:

\[
\boxed{
R_{\rm state}
\vee
\mathfrak F_{\rm fib}.
}
\]

So consider the coherent first route.

Let:

\[
\boxed{
g(x,t)
=
e\cdot
\left[
v(x+z,t)-v(x,t)
\right],
}
\]

for a fixed selected unit vector \(e\) and:

\[
|z|\sim r.
\]

Scale-invariant line strength implies, on a fixed fraction of the line-time atom,

\[
\boxed{
|g|
\gtrsim
\frac{a_0}{r}.
}
\tag{1.1}
\]

This is the CKN-critical velocity-increment amplitude.

---

# 2. Transverse coherence radius

For a selected material line point and time, let:

\[
\boxed{
h\le cr
}
\]

be a transverse coherence radius on which the selected increment component remains a fixed fraction of its centerline value.

Schematically:

\[
\boxed{
|g|
\ge
\frac{a_0}{2r}
}
\]

on a transverse disk of radius \(h\).

Define the aspect ratio:

\[
\boxed{
\Lambda
=
\frac r h
\ge1.
}
\tag{2.1}
\]

There are two immediate alternatives.

---

# 3. Comparable transverse width gives volumetric increment activity

If:

\[
\boxed{
h\ge c_0r,
}
\]

then the line atom occupies a fixed fraction of a full \(r\)-scale tube.

The volumetric quartic increment mass is then:

\[
\iint_{Q_r}
|g|^4
\gtrsim
r^5
\frac1{r^4}
=
r.
\]

The scale-invariant fixed-ratio volumetric increment detector has the form:

\[
\boxed{
\widetilde{\mathcal S}_{\rm vol}
\sim
\frac1r
\iint_{Q_r}
|g|^4.
}
\]

Therefore:

## Theorem D84.1 — Comparable-Tube Atom Absorption

\[
\boxed{
h/r\ge c_0
\Longrightarrow
\widetilde{\mathcal S}_{\rm vol}
\ge c(a_0,c_0)>0.
}
\tag{3.1}
\]

So a matched atom that does not become transversely thin is already absorbed into the existing derivative-compatible increment branch.

---

# 4. Native Morrey energy does not kill a thin atom

Assume:

\[
h\ll r.
\]

On the coherent transverse core:

\[
|g|
\gtrsim
1/r.
\]

Since:

\[
|v(x+z)-v(x)|^2
\le
2|v(x+z)|^2+2|v(x)|^2,
\]

the union of the core tube and its \(z\)-translate carries kinetic energy at least:

\[
\boxed{
E_{\rm atom}(r,h)
\gtrsim
\frac1{r^2}
\cdot
r h^2
=
\frac{h^2}{r}.
}
\tag{4.1}
\]

Equivalently:

\[
\boxed{
E_{\rm atom}(r,h)
\gtrsim
\frac r{\Lambda^2}.
}
\tag{4.2}
\]

But the native branch only gives:

\[
\boxed{
E(B_{Cr})
\lesssim
r.
}
\]

Therefore:

## Theorem D84.2 — Morrey Packing NO-GO

The native linear Morrey law is fully compatible with arbitrarily large:

\[
\Lambda=r/h.
\]

Indeed the minimum kinetic-energy fraction of a thin line atom is only:

\[
\boxed{
\Lambda^{-2}.
}
\]

So no uniform contradiction can come from kinetic-energy packing alone.

---

# 5. Codimension-two logarithmic capacity

The transverse geometry is two-dimensional.

This is the critical codimension for an \(H^1\) point/line trace.

Consider a scalar function on a transverse annulus:

\[
B_r^{(2)}
\setminus
B_h^{(2)}.
\]

Suppose the coherent increment is:

\[
g\sim A
\]

on the inner disk and has dropped by a fixed fraction by radius \(r\).

The energy-minimizing radial connector is logarithmic:

\[
\boxed{
g_{\rm cap}(\rho)
=
A
\frac{
\log(r/\rho)
}{
\log(r/h)
}.
}
\]

Its two-dimensional Dirichlet energy is:

\[
\boxed{
\int_{B_r^{(2)}\setminus B_h^{(2)}}
|\nabla_\perp g_{\rm cap}|^2
dx_\perp
=
\frac{
2\pi A^2
}{
\log(r/h)
}.
}
\tag{5.1}
\]

Thus the disk condenser capacity is:

\[
\boxed{
\operatorname{Cap}_2(B_h,B_r)
=
\frac{2\pi}{\log(r/h)}.
}
\tag{5.2}
\]

For the line atom:

\[
A\sim1/r.
\]

Integrating over:

- arc length \(O(r)\);
- time length \(O(r^2)\);

gives:

## Theorem D84.3 — Logarithmic Gradient-Capacity Floor

On the coherent thin-atom subbranch,

\[
\boxed{
\iint_{Q_{Cr}}
|\nabla g|^2
dxdt
\gtrsim
\frac r{\log\Lambda}.
}
\tag{5.3}
\]

Since:

\[
\nabla g
=
e\cdot
\left[
\nabla v(x+z)-\nabla v(x)
\right],
\]

\[
|\nabla g|^2
\le
2|\nabla v(x+z)|^2
+
2|\nabla v(x)|^2.
\]

Therefore:

## Corollary D84.4 — Scale-Normalized Gradient Floor

\[
\boxed{
\frac1r
\iint_{Q_{C'r}}
|\nabla v|^2
dxdt
\gtrsim
\frac1{\log\Lambda}.
}
\tag{5.4}
\]

This is the sharp qualitative capacity scaling for codimension two.

---

# 6. Why diffusion still does not give a uniform contradiction

The lower bound:

\[
\frac1{\log\Lambda}
\]

degenerates as:

\[
\Lambda\to\infty.
\]

Thus even the unweighted scale-normalized gradient action can tend to zero logarithmically.

The actual prelimit Navier–Stokes kinetic-energy dissipation carries the small Type-II viscosity coefficient:

\[
\varepsilon_n.
\]

So the corresponding viscous payment is only of order:

\[
\boxed{
\frac{
\varepsilon_n r
}{
\log\Lambda
}.
}
\tag{6.1}
\]

This may vanish through:

- \(\varepsilon_n\to0\);
- \(\Lambda\to\infty\);
- or both.

Therefore:

## Theorem D84.5 — Naive Diffusion Packing NO-GO

A nested matched material-line atom cannot be eliminated merely by summing the ordinary viscous-gradient cost.

The codimension-two capacity allows logarithmically cheap transverse concentration.

This is the correct audit.

---

# 7. Why the logarithm matters

In codimension one, a fixed jump across thickness \(h\) has an energy cost that diverges like a power of \(h^{-1}\).

In codimension two, the minimizing connector is logarithmic.

The cost is only:

\[
\boxed{
1/\log(r/h).
}
\]

So the material-line Kelvin trace problem sits exactly at a capacity-critical geometry.

This explains why D82 could not obtain an unconditional volume-to-line trace theorem.

---

# 8. The recursive matched-atom question

Let a matched atom at generation \(j\) have scale:

\[
\boxed{
r_j.
}
\]

To keep the volumetric increment detector silent, its own line trace ratio must again become large.

D82–83 then extract:

\[
\boxed{
r_{j+1}
\le
C
r_j
\Theta_j^{-1/4}.
}
\tag{8.1}
\]

If:

\[
\Theta_j\to\infty,
\]

then:

\[
\boxed{
q_j
:=
\frac{r_{j+1}}{r_j}
\to0.
}
\tag{8.2}
\]

This is decisive.

---

# 9. Internal matching versus generation matching

D83's matched branch means:

\[
\boxed{
\text{child active displacement}
\sim
\text{child transverse width}
\sim
r_{j+1}.
}
\]

So the child has a fixed **internal** relative filter/displacement ratio.

But the parent-to-child generation ratio is:

\[
\boxed{
q_j=r_{j+1}/r_j.
}
\]

If the child trace remains invisible and:

\[
\Theta_j\to\infty,
\]

then:

\[
q_j\to0.
\]

Therefore an infinite silent matched cascade cannot remain in a compact set of adjacent scale ratios.

This is exactly the nested-scale warning already present in DCRP20/DCRP50.

---

# 10. Compact-ratio atom chain is impossible

Assume there exists:

\[
q_->0
\]

such that every consecutive matched atom satisfies:

\[
\boxed{
r_{j+1}\ge q_-r_j.
}
\tag{10.1}
\]

Then (8.1) gives:

\[
\Theta_j
\le
Cq_-^{-4}.
\]

Thus the line-to-volume trace ratio is uniformly bounded.

By D82 trace/volume factorization:

\[
\boxed{
\widetilde{\mathcal S}_{C,j}
=
\Theta_j
\widetilde{\mathcal S}_{T,j}.
}
\]

If the line atom has fixed normalized strength:

\[
\widetilde{\mathcal S}_{C,j}\ge s_0>0,
\]

then:

## Theorem D84.6 — Compact Generation-Ratio Absorption

\[
\boxed{
\widetilde{\mathcal S}_{T,j}
\ge
c(s_0,q_-)>0.
}
\tag{10.2}
\]

Therefore:

\[
\boxed{
\text{matched atom}
+
\text{compact adjacent scale ratios}
\Longrightarrow
\widetilde{\mathcal S}_{\rm vol}^{\rm active}.
}
\tag{10.3}
\]

No silent compact-ratio atom cascade exists.

---

# 11. Infinite silent matched atoms force scale escape

Take the contrapositive.

If an infinite matched line-atom chain keeps:

\[
\widetilde{\mathcal S}_{\rm vol}\to0,
\]

then no positive:

\[
q_-
\]

can bound:

\[
r_{j+1}/r_j
\]

from below.

Therefore:

## Theorem D84.7 — Matched Atom / Relative-Scale Escape

\[
\boxed{
R_{\rm atom}
\Longrightarrow
\widetilde{\mathcal S}_{\rm vol}^{\rm active}
\vee
R_{\rm scale}
\vee
R_{\rm state}.
}
\tag{11.1}
\]

Here:

\[
\boxed{
R_{\rm scale}
:
\inf_j
\frac{r_{j+1}}{r_j}
=0
}
\]

is the existing nested-scale / relative-filter / shell-span noncompactness coordinate.

The \(R_{\rm state}\) term includes:

- failure of coherent displacement selection;
- increment-fiber escape;
- carrier multiplicity;
- temporal/line atom fragmentation.

---

# 12. Absorb the entire D83 trace atom

D83 gave:

\[
R_{\rm tr}
\Longrightarrow
R_{\rm ratio}
\vee
R_{\rm atom}
\vee
R_{\rm mult}.
\]

Now:

\[
R_{\rm ratio}
\subseteq
R_{\rm scale},
\]

and:

\[
R_{\rm mult}
\subseteq
R_{\rm state}.
\]

Use D84.7 on \(R_{\rm atom}\).

Therefore:

## Theorem D84.8 — Trace Gap Absorption

\[
\boxed{
R_{\rm tr}
\Longrightarrow
\widetilde{\mathcal S}_{\rm vol}^{\rm active}
\vee
R_{\rm scale}
\vee
R_{\rm state}.
}
\tag{12.1}
\]

The codimension-two trace defect is no longer an independent terminal coordinate.

---

# 13. Corrected Kelvin terminal reduction

D82 had:

\[
R_K
\Longrightarrow
\widetilde{\mathcal S}_{\rm vol}^{\rm active}
\vee
R_{\rm tr}
\vee
R_{\rm fil}
\vee
R_{\rm state}
\vee
R_{\rm tail}.
\]

Insert D84.8.

Thus:

## Theorem D84.9 — Kelvin Residue without a Trace Terminal

\[
\boxed{
R_K
\Longrightarrow
\widetilde{\mathcal S}_{\rm vol}^{\rm active}
\vee
R_{\rm scale}
\vee
R_{\rm fil}
\vee
R_{\rm state}
\vee
R_{\rm tail}.
}
\tag{13.1}
\]

The formerly mysterious second-order viscous Kelvin residue has now been reduced entirely to already-existing finite-scale/material noncompactness coordinates.

No \(R_K\), \(R_{\rm tr}\), or \(R_{\rm atom}\) terminal label is needed anymore at this resolution.

---

# 14. Correction to the D80 finite terminal compiler

D80 wrote the late material compiler using:

\[
R_{\rm tail},
\quad
R_{\rm fil},
\quad
R_{\rm state},
\quad
R_K.
\]

D84 shows the uniquely Navier–Stokes \(R_K\) label is absorbed, but a pre-existing **scale noncompactness** coordinate must be shown explicitly:

\[
\boxed{
R_{\rm scale}.
}
\]

This is not a new mechanism invented by D84.

It is the old:

- relative-filter escape;
- nested-scale gap;
- shell-span escape;

already warned about in DCRP20/DCRP50 and in the earlier interaction-graph compiler.

The corrected late terminal architecture is therefore:

\[
\boxed{
\mathsf O_{\rm PFET}
\wedge
\left(
\mathsf X
\vee
\widetilde{\mathcal S}_{\rm vol}^{\rm active}
\vee
R_{\rm scale}
\vee
R_{\rm tail}
\vee
R_{\rm fil}
\vee
R_{\rm state}
\right).
}
\tag{14.1}
\]

---

# 15. Morrey and diffusion are diagnostic, not the closing mechanism

The intended D84 attack was:

> perhaps the nested line atom costs too much energy or diffusion.

The audit says no.

For transverse aspect ratio:

\[
\Lambda=r/h,
\]

the minimum kinetic-energy fraction behaves like:

\[
\boxed{
\Lambda^{-2},
}
\]

and the minimum scale-normalized \(H^1\) connector cost behaves like:

\[
\boxed{
1/\log\Lambda.
}
\]

Both can vanish.

Thus the actual closing step is not an energy summation theorem.

It is the **relative-scale compactness theorem** D84.6–7:

> if adjacent matched scales remain comparable, the atom becomes volumetrically visible; if it remains volumetrically invisible, adjacent scale ratios must collapse.

This is much stronger architecturally.

---

# 16. Relationship to the existing persistent increment compiler

Once:

\[
\widetilde{\mathcal S}_{\rm vol}^{\rm active}>0,
\]

the branch re-enters the already-developed DCRP23–26 architecture.

That architecture already distinguishes:

- increment-fiber escape;
- Young oscillation/concentration;
- covariance defect;
- resolved strong-profile covariance;
- pressure-compatible strong-profile kernel.

D84 therefore does not restart the analysis.

It hands the Kelvin branch back to an existing finite-scale compiler.

---

# 17. What remains after D84

The newly isolated high-priority terminal coordinate is:

\[
\boxed{
R_{\rm scale}.
}
\]

It means a same-parent survivor repeatedly skips arbitrarily large bands of relative scales:

\[
\boxed{
r_{j+1}/r_j\to0.
}
\]

This is more specific than generic material noncompactness.

It is now the correct next target.

The question is:

> can a strict same-parent Type-II sequence repeatedly jump across an unbounded relative scale gap without paying the already-existing shell-span / diffusion / far-field source costs?

This is exactly the old scale-escape problem, now reached independently from the Kelvin trace line.

---

# 18. Status ledger

## PROVED this round

### D84-P1 — coherent critical line atom amplitude

\[
|g|\gtrsim1/r.
\]

### D84-P2 — comparable tube width gives positive volumetric increment detector.

### D84-P3 — native Morrey lower cost

\[
E_{\rm atom}\gtrsim r/\Lambda^2
\]

does not exclude large aspect ratio.

### D84-P4 — codimension-two capacity floor

\[
r^{-1}
\iint|\nabla v|^2
\gtrsim
1/\log\Lambda
\]

on the coherent scalar atom subbranch.

### D84-P5 — ordinary viscous-gradient cost is logarithmically cheap; no naive diffusion packing contradiction.

### D84-P6 — compact adjacent generation ratios force bounded trace ratio and hence volumetric increment visibility.

### D84-P7 — infinite silent matched atom chain forces relative-scale escape.

### D84-P8 — full trace defect absorption

\[
R_{\rm tr}
\Longrightarrow
\widetilde{\mathcal S}_{\rm vol}^{\rm active}
\vee
R_{\rm scale}
\vee
R_{\rm state}.
\]

### D84-P9 — Kelvin residue no longer needs an independent terminal coordinate.

---

# 19. What is not proved

D84 does not prove:

- \(R_{\rm scale}\) is impossible;
- persistent positive \(\widetilde{\mathcal S}_{\rm vol}\) depletes a global budget;
- the logarithmic-capacity lower bound produces a uniform filtered-vorticity diffusion payment;
- the existing shell-span compiler already quantitatively closes every \(R_{\rm scale}\) realization.

These are the actual remaining obligations.

---

# 20. New STOP

\[
\boxed{
\textbf{
STOP-D84:
The coherent matched material-line atom is exactly codimension-two critical. If its transverse width stays comparable to its increment scale, it immediately becomes an already-known volumetric derivative-compatible increment defect. If it becomes thin, native Morrey costs only }r/\Lambda^2\textbf{ and the optimal transverse }H^1\textbf{ capacity costs only }1/\log\Lambda\textbf{, so neither energy nor ordinary diffusion gives a uniform contradiction. However an infinite silent matched-atom recursion then forces the adjacent generation ratio }r_{j+1}/r_j\textbf{ to collapse to zero; otherwise the D82 trace ratio would remain bounded and the volumetric increment detector would be positive. Thus }R_{\rm atom}\textbf{ and hence the entire Kelvin trace defect are absorbed into the already-existing persistent volumetric increment branch, relative-scale/shell-span escape, or state compactness failure. No independent Kelvin/trace/line-atom terminal mechanism remains.}
}
\]

---

# 21. Next autonomous step

## DCRP85 / X72-R68 — Relative-Scale Escape / Shell-Span Closure Audit

**Working title**

> **Can a Same-Parent Type-II Survivor Skip Arbitrarily Large Relative Scale Bands without Paying Diffusion Span, Far-Field Source, or Increment-Fiber Debt?**

Primary tasks:

1. assume:
   \[
   R_{\rm scale}:
   \quad
   r_{j+1}/r_j\to0;
   \]
2. insert the DCRP02 interaction-graph supply-migration theorem;
3. compare shell-label escape with:
   - dissipation-span / driver debt;
   - relative IR/far-field source escape;
4. use DCRP20's relative-frequency probability measure;
5. determine whether large scale gaps necessarily produce:
   \[
   P_{\rm diff}
   \vee
   R_{\rm tail}
   \vee
   \mathfrak F_{\rm fib}
   \vee
   \widetilde{\mathcal S}_{\rm active};
   \]
6. audit whether the scale jump can be geometrically summable without losing same-parent material ancestry;
7. seek:
   \[
   R_{\rm scale}
   \Longrightarrow
   \text{already-known paid/native coordinates}.
   \]

Desired endpoint:

\[
\boxed{
\text{Kelvin trace route}
\Longrightarrow
\text{old finite-scale compiler only}.
}
\]

---

# 22. One-line checkpoint

Matched line atoms are not killed by Morrey or diffusion because codimension two is logarithmically critical, but they also cannot form a new compact terminal branch: if adjacent scales stay comparable they become volumetrically visible, and if they remain invisible their generation ratios collapse, so the Kelvin trace route has been reduced entirely to the old relative-scale/shell-span escape problem.

---

**End checkpoint:** DCRP84 / X72-R67  
**Next:** DCRP85 / X72-R68 — Relative-Scale Escape / Shell-Span Closure Audit.
