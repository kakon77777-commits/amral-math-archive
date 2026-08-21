# DCRP83 / X72-R66 — Subfilter Scale Extraction, Relative-Filter Escape, and the Parabolic Trace-Atom Trichotomy

**Series:** Independent Navier–Stokes Research Series / X72 Bridge  
**Date:** 2026-08-18  
**Status:** Proof-development checkpoint / material-line trace concentration round  
**Immediate predecessor:** `NS_DCRP82_X72R65_Codim2TraceBarrier_KelvinConcentration_2026-08-18.md`

**Primary internal dependencies**
- DCRP02 — carrier entropy / bounded-locality versus shell/span escape
- DCRP20 — fixed-relative-filter / IR-scale caution
- DCRP24 — derivative-compatible increment fiber escape / Young-profile completion
- DCRP50 — nested-scale / relative-filter compiler caution
- DCRP82 — codimension-two material-loop trace concentration defect

**Fresh external calibration**
- Runlong Yu, *Filtered Vortex Stretching and Subgrid Defects for the Three-Dimensional Navier–Stokes Equations*, arXiv:2606.27560. The derivative-compatible increment envelope samples velocity increments against both the filter and derivative-filter measures, and its critical detector is scale invariant only at fixed relative filter ratio \(\ell=\sigma r\).
- Gregory L. Eyink, *The Cascade of Circulations in Fluid Turbulence*, arXiv:physics/0606159. Coarse-grained circulation defects are local-in-scale objects only after the relevant scale geometry is identified.

No full Navier–Stokes regularity theorem is claimed.

---

# 0. Executive result

DCRP82 isolated the only new Kelvin visibility gap:

\[
\boxed{
\Theta_{{\rm tr},n}\to\infty,
}
\]

where

\[
\boxed{
\Theta_{\rm tr}
=
\frac{
\ell^2
\displaystyle\int_I\int_{C(t)}
f_\ell\,dsdt
}{
\displaystyle
\int_I\int_{T_\ell(C(t))}
f_\ell\,dxdt
},
}
\]

and

\[
\boxed{
f_\ell
=
\mathfrak M_{\ell,4}^{\,4}.
}
\]

DCRP83 proves that this trace blow-up really does force a thinner transverse scale.

But it also proves an important correction:

> **the thinner transverse scale does not automatically produce a fixed-relative-filter Navier–Stokes descendant.**

The original increment displacement scale \(\ell\) and the newly extracted transverse concentration scale \(\delta\) separate.

The exact result is a new three-way normal form:

\[
\boxed{
R_{\rm tr}
\Longrightarrow
R_{\rm ratio}
\ \vee\
R_{\rm atom}
\ \vee\
R_{\rm mult}.
}
\]

Here:

- \(R_{\rm ratio}\) = relative-filter / displacement-to-thickness aspect-ratio escape;
- \(R_{\rm atom}\) = a fixed-share parabolic material-line atom survives and yields a genuine smaller-scale line-increment descendant;
- \(R_{\rm mult}\) = no fixed-share atom survives, so the number of active parabolic material-line cells diverges.

The latter two are respectively the coherent-critical-increment and carrier-multiplicity alternatives already familiar from the earlier DCRP interaction/Young-profile compiler.

Thus D83 does **not** create a new fifth terminal mechanism.

It identifies exactly why naive subfilter rerooting fails and what additional coherence is needed.

---

# 1. Tubular mass function

Assume the filtered material loop \(C(t)\) remains smooth with tubular reach at least \(c\ell\).

Failure of this geometry is already:

\[
\boxed{
R_{\rm fil}\vee R_{\rm state}.
}
\]

For:

\[
0<\rho\le\ell,
\]

define:

\[
\boxed{
A(\rho)
=
\int_I
\int_{T_\rho(C(t))}
f_\ell(x,t)\,dxdt.
}
\tag{1.1}
\]

Define the material-line trace mass:

\[
\boxed{
I_C
=
\int_I
\int_{C(t)}
f_\ell\,dsdt.
}
\tag{1.2}
\]

Tubular coordinates give:

\[
\boxed{
\lim_{\rho\downarrow0}
\frac{A(\rho)}{\pi\rho^2}
=
I_C.
}
\tag{1.3}
\]

The constant \(\pi\) is the area of the unit transverse disk.

---

# 2. Normalized tube-density profile

Define:

\[
\boxed{
H(\rho)
=
\frac{
\ell^2 A(\rho)
}{
\rho^2 A(\ell)
}.
}
\tag{2.1}
\]

Then:

\[
\boxed{
H(\ell)=1,
}
\]

and:

\[
\boxed{
\lim_{\rho\downarrow0}
H(\rho)
=
\pi\Theta_{\rm tr}.
}
\tag{2.2}
\]

Thus trace concentration is exactly the statement that the normalized tube density becomes much larger near the centerline than at the filter-scale tube.

---

# 3. Quantitative subfilter scale extraction

Let:

\[
\widehat\Theta
=
\pi\Theta_{\rm tr}.
\]

Assume:

\[
\widehat\Theta>1.
\]

By continuity there exists:

\[
0<\delta<\ell
\]

such that:

\[
\boxed{
H(\delta)
=
\widehat\Theta^{1/2}.
}
\tag{3.1}
\]

Since:

\[
A(\delta)\le A(\ell),
\]

we have:

\[
\widehat\Theta^{1/2}
=
\frac{
\ell^2A(\delta)
}{
\delta^2A(\ell)
}
\le
\frac{\ell^2}{\delta^2}.
\]

Therefore:

## Theorem D83.1 — Quantitative Thin-Tube Scale

\[
\boxed{
\frac{\delta}{\ell}
\le
\widehat\Theta^{-1/4}.
}
\tag{3.2}
\]

Also:

## Theorem D83.2 — Cross-Section Density Amplification

\[
\boxed{
\frac{
A(\delta)
}{
\delta^2
}
=
\widehat\Theta^{1/2}
\frac{
A(\ell)
}{
\ell^2
}.
}
\tag{3.3}
\]

Thus:

\[
\Theta_{\rm tr}\to\infty
\]

forces:

\[
\boxed{
\delta/\ell\to0.
}
\]

This is the rigorous subfilter transverse-scale extraction missing in D82.

---

# 4. Tunable extraction exponent

More generally, fix:

\[
0<\beta<1.
\]

Choose:

\[
H(\delta_\beta)
=
\widehat\Theta^\beta.
\]

Then:

\[
\boxed{
\frac{
\delta_\beta
}{
\ell
}
\le
\widehat\Theta^{-\beta/2},
}
\tag{4.1}
\]

and:

\[
\boxed{
\frac{
A(\delta_\beta)
}{
\delta_\beta^2
}
=
\widehat\Theta^\beta
\frac{
A(\ell)
}{
\ell^2
}.
}
\tag{4.2}
\]

The choice:

\[
\beta=\frac12
\]

balances scale separation and density amplification and is used below.

---

# 5. Direct rerooting does not preserve the fixed filter ratio

Set:

\[
\boxed{
\Lambda
=
\frac{\ell}{\delta}.
}
\]

D83.1 gives:

\[
\boxed{
\Lambda
\ge
\widehat\Theta^{1/4}
\to\infty.
}
\tag{5.1}
\]

Reroot spatial coordinates at the new transverse scale:

\[
x
=
x_C+\delta y.
\]

Then an original filter displacement:

\[
z=\ell\zeta
\]

becomes:

\[
\boxed{
\frac z\delta
=
\Lambda\zeta.
}
\tag{5.2}
\]

Thus the original filter length in the \(\delta\)-rerooted variables is:

\[
\boxed{
\ell_{\rm rel}^{\rm new}
=
\Lambda
\to\infty.
}
\tag{5.3}
\]

This is not the fixed-relative-filter regime:

\[
\ell=\sigma r.
\]

Therefore:

## Theorem D83.3 — NO-GO to Naive Same-Class Rerooting

Trace concentration alone does not yield a new fixed-ratio filtered-vorticity descendant at scale \(\delta\).

It yields a thin transverse scale together with a divergent filter/thickness aspect ratio.

This is the first essential correction of D83.

---

# 6. Relative-displacement fiber measure

To determine whether the increment displacement itself also descends, resolve the trace mass by displacement.

Suppress the duplicate \(\varphi\)- and \(\nabla\varphi\)-components for notation.

Define a normalized trace displacement measure on the fixed relative variable:

\[
\zeta=\frac z\ell.
\]

Schematically:

\[
\boxed{
d\Pi(\zeta)
=
\frac{
\displaystyle
\int_I\int_C
|\delta_{\ell\zeta}v|^4
\,dsdt\,
d\nu_1(\zeta)
}{
\displaystyle
\int_I\int_C
M_{\varphi,4}^4
\,dsdt
}.
}
\tag{6.1}
\]

This is a probability measure on the fixed compact support of the base kernel.

The derivative-kernel component is treated in parallel.

After subsequence extraction there are two basic possibilities.

---

# 7. Relative displacement stays away from zero

Suppose there exist:

\[
c_0>0,
\qquad
\eta_0>0
\]

such that:

\[
\boxed{
\Pi_n(
|\zeta|\ge c_0
)
\ge
\eta_0.
}
\tag{7.1}
\]

Then after \(\delta_n\)-rerooting those increments occur at separation:

\[
\boxed{
\frac{|z|}{\delta_n}
\ge
c_0
\frac{\ell_n}{\delta_n}
\to\infty.
}
\tag{7.2}
\]

Therefore:

## Theorem D83.4 — Far-Increment Rerooting Branch

A positive fixed share of trace mass at original relative displacement \(O(1)\) becomes a far-increment / divergent-relative-filter carrier after transverse rerooting.

This is:

\[
\boxed{
R_{\rm ratio}.
}
\]

It lies in the existing nested-scale / shell-span / far-locality part of the DCRP compiler.

---

# 8. Relative displacement collapses toward zero

The alternative is:

\[
\boxed{
\Pi_n
\rightharpoonup
\delta_0
}
\tag{8.1}
\]

in the relative displacement variable.

Then the line trace is itself carried by increments at a smaller displacement scale:

\[
\boxed{
s_n=o(\ell_n).
}
\]

For example choose a median displacement scale \(s_n\) such that:

\[
\boxed{
\Pi_n(
|z|\le s_n/\ell_n
)
=
\frac12.
}
\tag{8.2}
\]

Now compare:

\[
\boxed{
\mathcal A_n
=
\frac{s_n}{\delta_n}.
}
\tag{8.3}
\]

After a subsequence, exactly one of:

\[
\mathcal A_n\to0,
\]

\[
\mathcal A_n\to\mathcal A_*\in(0,\infty),
\]

or:

\[
\mathcal A_n\to\infty
\]

holds.

---

# 9. Aspect-ratio escape

If:

\[
\mathcal A_n\to0
\]

or:

\[
\mathcal A_n\to\infty,
\]

the increment displacement scale and the transverse concentration scale separate.

Thus:

\[
\boxed{
\text{trace width}
\not\sim
\text{active displacement scale}.
}
\]

This is again:

\[
\boxed{
R_{\rm ratio}.
}
\]

The route has not produced an isotropic/fixed-ratio local descendant.

---

# 10. Matched subfilter branch

The only route that can produce a same-type local descendant is:

\[
\boxed{
0<c_-\le
\frac{s_n}{\delta_n}
\le c_+<\infty.
}
\tag{10.1}
\]

Now the active increment displacement and the transverse concentration width are comparable.

This is the **matched subfilter branch**.

But one further issue remains:

> the trace mass may be spread over too many parabolic material-line cells to give one fixed-share local descendant.

This is the carrier-entropy problem.

---

# 11. Parabolic material-line cells

Let the original recurrent cylinder have spatial scale \(r\) and time scale:

\[
O(r^2).
\]

Assume the material loop length is:

\[
O(r).
\]

Partition the space-time material line:

\[
\{(x,t):x\in C(t)\}
\]

into parabolic cells with:

- arc length \(O(\delta)\);
- time length \(O(\delta^2)\).

The number of cells satisfies:

\[
\boxed{
N_\delta
\asymp
\left(
\frac r\delta
\right)^3.
}
\tag{11.1}
\]

Let \(m_j\) be the matched-displacement trace mass in cell \(j\), and define:

\[
\boxed{
p_j
=
\frac{m_j}{\sum_km_k},
\qquad
p_{\max}
=
\max_jp_j.
}
\tag{11.2}
\]

---

# 12. Kernel-density gain at the matched smaller scale

Assume a standard nondegenerate mollifier, so on the matched displacement shell:

\[
|z|\sim\delta,
\]

the small-scale kernel density is larger than the original \(\ell\)-scale density by:

\[
\boxed{
\asymp
\left(
\frac{\ell}{\delta}
\right)^3.
}
\tag{12.1}
\]

Therefore the derivative-compatible increment trace mass in one selected \(\delta\)-cell gains the same factor, up to fixed kernel constants.

Let the original scale-normalized line detector be:

\[
\boxed{
\mathcal S_{C;r,\ell}
=
r
\int_I\int_C
\mathfrak M_{\ell,4}^4
\,dsdt.
}
\tag{12.2}
\]

Let:

\[
\mathcal S_{C;\delta}
\]

be the corresponding line detector on one parabolic \(\delta\)-cell at matched filter ratio.

Then:

## Theorem D83.5 — Local-Atom Transfer

\[
\boxed{
\frac{
\mathcal S_{C;\delta}^{\max}
}{
\mathcal S_{C;r,\ell}
}
\gtrsim
\left(
\frac{\ell}{r}
\right)^3
\left(
\frac r\delta
\right)^2
p_{\max}.
}
\tag{12.3}
\]

At fixed outer relative filter ratio:

\[
\ell=\sigma r,
\]

\[
\boxed{
\frac{
\mathcal S_{C;\delta}^{\max}
}{
\mathcal S_{C;r,\ell}
}
\gtrsim
\sigma^3
\left(
\frac r\delta
\right)^2
p_{\max}.
}
\tag{12.4}
\]

This is the exact parabolic atom threshold.

---

# 13. Fixed-share local descendant threshold

If:

\[
\boxed{
p_{\max}
\gtrsim
\left(
\frac\delta r
\right)^2,
}
\tag{13.1}
\]

then:

\[
\boxed{
\mathcal S_{C;\delta}^{\max}
\gtrsim
\mathcal S_{C;r,\ell}.
}
\tag{13.2}
\]

Thus a fixed amount of the scale-normalized line increment obstruction survives in one smaller parabolic cell.

Define this route:

\[
\boxed{
R_{\rm atom}.
}
\]

It produces a genuine smaller-scale **line-increment descendant**.

D83 does not yet claim that this line descendant automatically has the full bounded volumetric reservoir required by DCRP23.

That remains a separate local-to-volumetric bridge.

---

# 14. Why uniform mass spreading is too weak

If the matched trace mass were uniformly distributed over all:

\[
N_\delta
\asymp
(r/\delta)^3
\]

cells, then:

\[
p_{\max}
\asymp
(\delta/r)^3.
\]

Insert into (12.4):

\[
\boxed{
\frac{
\mathcal S_{C;\delta}^{\max}
}{
\mathcal S_{C;r,\ell}
}
\asymp
\frac\delta r
\to0.
}
\tag{14.1}
\]

Therefore simple pigeonhole localization is not enough to create a scale-invariant descendant.

This is the second important NO-GO of D83.

---

# 15. Atom collapse implies multiplicity growth

Suppose:

\[
\boxed{
p_{\max}
=
o\!\left(
(\delta/r)^2
\right).
}
\tag{15.1}
\]

Then the number of active cells satisfies:

\[
\boxed{
N_{\rm act}
\ge
\frac1{p_{\max}}
\gg
\left(
\frac r\delta
\right)^2.
}
\tag{15.2}
\]

Thus if no fixed-share parabolic atom produces a descendant, the trace carrier must fragment across a diverging number of material-line cells.

Define:

\[
\boxed{
R_{\rm mult}.
}
\]

This is a material carrier-entropy / multiplicity noncompactness, already present in the DCRP interaction-graph/state compiler.

---

# 16. D83 trichotomy

Combine the scale-extraction, displacement, and parabolic-atom arguments.

## Theorem D83.6 — Subfilter Trace-Concentration Trichotomy

Assume:

\[
\Theta_{{\rm tr},n}\to\infty
\]

with bounded tubular loop geometry.

Then after subsequence extraction there exists:

\[
\delta_n/\ell_n\to0
\]

such that at least one of:

### A. relative-filter / aspect-ratio escape

\[
\boxed{
R_{\rm ratio};
}
\]

### B. matched fixed-share line descendant

\[
\boxed{
R_{\rm atom};
}
\]

### C. parabolic carrier multiplicity explosion

\[
\boxed{
R_{\rm mult}.
}
\]

Therefore:

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
\tag{16.1}
\]

No arbitrary trace concentration remains.

---

# 17. Absorption into the older compiler

The three D83 routes are not genuinely new mechanisms.

## \(R_{\rm ratio}\)

is exactly a nested-scale / relative-filter / shell-span escape.

DCRP20 and DCRP50 already warned that activity at a shrinking relative filter ratio cannot be silently identified with a fixed-ratio core defect.

DCRP02 routes bounded-locality failure through shell-span/dissipation or far-field locality.

## \(R_{\rm mult}\)

is packet/carrier multiplicity noncompactness:

\[
\boxed{
R_{\rm state}.
}
\]

DCRP02's interaction graph already shows that atom collapse at fixed total supply forces growing interaction degree/coherence.

## \(R_{\rm atom}\)

is not a new terminal defect.

It is a recursively generated smaller-scale critical line-increment carrier.

It must either:

- enter the existing bounded-reservoir increment compiler;
- repeat the trace-concentration mechanism;
- or lose state/filament compactness.

Thus D83 has converted the apparently new \(R_{\rm tr}\) into an existing nested-scale recursion problem.

---

# 18. Important relation to DCRP24 fiber escape

DCRP24 already distinguishes:

\[
\boxed{
\text{increment-fiber escape}
}
\]

from a fiber-tight full Young representation.

D83 adds a different but compatible noncompact coordinate:

\[
\boxed{
\text{physical displacement/filter-ratio escape}.
}
\]

These should not be identified.

The first concerns compactness inside the increment-function fiber at fixed relative scale.

The second concerns the relative scale itself leaving every compact subset of:

\[
(0,\infty).
\]

The final compiler must retain this distinction.

---

# 19. Critical matched atom scaling

The threshold:

\[
p_{\max}
\sim
(\delta/r)^2
\]

is codimension-two.

This is not accidental.

The material-line trace has two transverse spatial directions.

A fixed-share descendant requires enough coherence to overcome exactly two powers of the scale ratio.

The third parabolic power:

\[
(r/\delta)^3
\]

counts:

- one material-line direction;
- two time/spatial parabolic powers.

Thus uniform spreading loses one power:

\[
\delta/r.
\]

This is the precise coherence deficit of naive rerooting.

---

# 20. Why D83 does not yet close the trace branch

The remaining recursive matched-atom branch can in principle form an infinite nested line-concentration cascade.

At each level it may saturate a critical Morrey-type geometry.

D83 does not prove such a nested cascade impossible.

It proves that to survive, the trace branch must choose one of only three explicit strategies:

1. separate displacement and thickness scales;
2. retain a coherent fixed-share atom across scales;
3. fragment into diverging carrier multiplicity.

This is a much narrower endgame.

---

# 21. Updated late compiler

D82 had:

\[
\boxed{
\mathsf O_{\rm PFET}
\wedge
\left(
\mathsf X
\vee
\widetilde{\mathcal S}_{\rm active}
\vee
R_{\rm tr}
\vee
R_{\rm tail}
\vee
R_{\rm fil}
\vee
R_{\rm state}
\right).
}
\]

D83 replaces:

\[
R_{\rm tr}
\]

by:

\[
R_{\rm ratio}
\vee
R_{\rm atom}
\vee
R_{\rm mult}.
\]

Since:

\[
R_{\rm mult}
\subset
R_{\rm state},
\]

the corrected compiler is:

## Theorem D83.7 — Refined Trace Compiler

\[
\boxed{
\mathsf O_{\rm PFET}
\wedge
\left(
\mathsf X
\vee
\widetilde{\mathcal S}_{\rm active}
\vee
R_{\rm ratio}
\vee
R_{\rm atom}
\vee
R_{\rm tail}
\vee
R_{\rm fil}
\vee
R_{\rm state}
\right).
}
\tag{21.1}
\]

The new active target is now clearly:

\[
\boxed{
R_{\rm atom}
\quad\text{versus}\quad
R_{\rm ratio}.
}
\]

---

# 22. Next priority

The strongest surviving trace route is the coherent matched atom:

\[
R_{\rm atom}.
\]

It produces a smaller-scale line increment carrier with fixed normalized strength.

The next question is:

> can an infinite nested sequence of such matched line atoms coexist with the native \(E(R)\lesssim R\) Morrey law and the filtered-vorticity diffusion ledger without becoming a genuine filamentation/Young concentration defect?

This is preferable to attacking generic trace inequalities.

---

# 23. Status ledger

## PROVED this round

### D83-P1 — quantitative subfilter transverse scale

\[
\delta/\ell
\lesssim
\Theta_{\rm tr}^{-1/4}.
\]

### D83-P2 — normalized tube-density amplification

\[
A(\delta)/\delta^2
\sim
\Theta_{\rm tr}^{1/2}
A(\ell)/\ell^2.
\]

### D83-P3 — direct \(\delta\)-rerooting sends the original filter ratio to infinity.

### D83-P4 — relative-displacement tightness away from zero becomes far-increment escape after rerooting.

### D83-P5 — relative-displacement collapse defines a smaller active displacement scale.

### D83-P6 — matched displacement/thickness branch requires parabolic trace-atom analysis.

### D83-P7 — exact local-atom transfer threshold

\[
p_{\max}
\gtrsim
(\delta/r)^2
\]

for a scale-invariant smaller line descendant.

### D83-P8 — uniform cell spreading loses one scale power and cannot produce a strong descendant.

### D83-P9 — atom collapse forces divergent material-line carrier multiplicity.

### D83-P10 — full trace trichotomy

\[
R_{\rm tr}
\Longrightarrow
R_{\rm ratio}
\vee
R_{\rm atom}
\vee
R_{\rm mult}.
\]

---

# 24. What is not proved

D83 does not prove:

- \(R_{\rm ratio}\) is impossible;
- \(R_{\rm atom}\) produces a full volumetric bounded-reservoir descendant;
- an infinite nested matched-atom cascade is impossible;
- \(R_{\rm mult}\) has a globally non-summable entropy cost.

These are now the precise remaining routes.

---

# 25. New STOP

\[
\boxed{
\textbf{
STOP-D83:
Material-line trace concentration does force a quantitatively thinner transverse scale, but it does not automatically create a same-class Navier--Stokes descendant. The new scale satisfies }\delta/\ell\lesssim\Theta_{\rm tr}^{-1/4}\textbf{, so direct rerooting sends the original filter ratio }\ell/\delta\textbf{ to infinity. After resolving the increment displacement, every trace branch must either pay a relative-filter/aspect-ratio escape, produce a matched smaller-scale material-line atom, or fragment into a diverging number of parabolic line cells. In the matched case a scale-invariant descendant requires a cell mass fraction of order }(\delta/r)^2\textbf{; uniform pigeonhole mass }(\delta/r)^3\textbf{ is one power too small. Thus the remaining Kelvin trace problem is no longer generic concentration: it is an explicit coherence-versus-scale-ratio recursion.}
}
\]

---

# 26. Next autonomous step

## DCRP84 / X72-R67 — Nested Matched-Line Atom versus Morrey/Diffusion

**Working title**

> **Can a Critical Material-Line Atom Reproduce Indefinitely without Becoming Filamentation, Diffusion Cost, or a Volumetric Increment Profile?**

Primary tasks:

1. assume the coherent matched branch:
   \[
   R_{\rm atom};
   \]
2. build a nested sequence:
   \[
   r_0>r_1>r_2>\cdots;
   \]
3. track the fixed normalized line detector across generations;
4. combine with native:
   \[
   E(R)\lesssim R;
   \]
5. estimate the minimum tube energy required by a fixed line-increment atom;
6. insert filtered diffusion at the matched scale;
7. test whether:
   - line atom \(\Rightarrow\) volumetric increment mass;
   - or line atom \(\Rightarrow\) direction/gradient filamentation;
8. derive a packing bound for nested matched atoms;
9. seek:
   \[
   R_{\rm atom}
   \Longrightarrow
   \widetilde{\mathcal S}_{\rm active}
   \vee
   R_{\rm fil}
   \vee
   R_{\rm ratio}.
   \]

Desired endpoint:

\[
\boxed{
\text{infinite matched trace-atom cascade}
\Longrightarrow
\text{already-known finite-scale defect}.
}
\]

---

# 27. One-line checkpoint

The trace gap has become a scale-coherence recursion: a subfilter width always exists, but survival requires either divergent filter/thickness aspect ratio, a fixed-share matched material-line atom, or exploding carrier multiplicity; naive rerooting is provably one parabolic power too weak.

---

**End checkpoint:** DCRP83 / X72-R66  
**Next:** DCRP84 / X72-R67 — Nested Matched-Line Atom / Morrey-Diffusion.
