# DCRP95 / X72-R78 — Sign-Coherent SGS Kelvin Phase-Slip Variation and the No-Finite-Crossing-Capacity Audit

**Series:** Independent Navier–Stokes Research Series / X72 Bridge  
**Date:** 2026-08-20  
**Status:** proof-development checkpoint  
**Immediate predecessor:** `NS_DCRP94_X72R77_KelvinResetGraph_NonpositiveSidecar_2026-08-19.md`

## Fresh primary-source calibration
- G. L. Eyink, *The Cascade of Circulations in Fluid Turbulence*, arXiv:physics/0606159.
- G. L. Eyink, *Turbulent Cascade of Circulations*, arXiv:physics/0605014.
- R. Yu, *Filtered Vortex Stretching and Subgrid Defects for the Three-Dimensional Navier–Stokes Equations*, arXiv:2606.27560.
- P. Constantin, M. Ignatova, V. Vicol, *On putative self-similarity for incompressible 3D Euler*, arXiv:2602.17570.

No full Navier–Stokes regularity theorem is claimed.

---

## 0. Executive result

DCRP94 proved that every bounded number of generations contains either a carrier/state replacement or a normalized Kelvin reset
\[
|\delta_n|\ge\delta_*>0.
\]

DCRP95 strengthens this to a **sign-coherent SGS reset**. Refine the finite circulation-state family by orientation/sign. On every material-shadowed repeated-state cycle,
\[
\Gamma_{n+q}
=
\rho_\Gamma^q\Gamma_n
+
\sum_{j=0}^{q-1}\rho_\Gamma^{q-1-j}\delta_{n+j},
\qquad
0<\rho_\Gamma<1.
\]
At recurrence,
\[
\Gamma_{n+q}=\Gamma_n.
\]
If the oriented state satisfies
\[
\sigma\Gamma_n\ge c_\Gamma>0,
\]
then
\[
\sum_{j=0}^{q-1}
\rho_\Gamma^{q-1-j}\sigma\delta_{n+j}
=
(1-\rho_\Gamma^q)\sigma\Gamma_n
\ge
(1-\rho_\Gamma)c_\Gamma.
\]
Therefore
\[
\boxed{
\sum_{j=0}^{q-1}
(\sigma\delta_{n+j})_+
\ge
(1-\rho_\Gamma)c_\Gamma.
}
\]
After removing the filtered-viscous and shadow/state terms by the D81–85 compiler, the same lower bound is carried, up to a fixed constant loss, by the SGS reset.

Hence there exist
\[
c_{\rm slip}>0,\qquad B_*<\infty
\]
such that every \(B_*\)-generation block of the pure compact reset branch contains
\[
\boxed{
\sigma_n\delta_n^{\rm SGS}\ge c_{\rm slip}.
}
\]

Define
\[
\boxed{
\mathcal V_{\Gamma,+}^{\rm SGS}(N)
=
\sum_{n=0}^{N-1}
(\sigma_n\delta_n^{\rm SGS})_+.
}
\]
Then
\[
\boxed{
\mathcal V_{\Gamma,+}^{\rm SGS}(N)
\ge
c_{\rm TV}N-O(1).
}
\]

Thus the last compact reset source is not an occasional or sign-cancelling defect. It is a **positive-density, same-sign coarse circulation-flux conveyor with linearly diverging normalized positive total variation**.

However there is still no finite-capacity contradiction. Eyink’s circulation-cascade theory interprets the turbulent vortex force as a classical analogue of Josephson–Anderson phase slip, but explicitly notes that the classical process is continuous because classical vortices are **not quantized**. Therefore no integer vortex-crossing inventory exists from which every reset must consume one indivisible unit.

The remaining normal form is therefore:
\[
\boxed{
\mathsf C_{\rm slip}
=
\text{Sign-Coherent SGS Kelvin Phase-Slip Conveyor}.
}
\]

---

## 1. Oriented finite circulation states

D88 gives finitely many loop templates \(C_1,\dots,C_M\) and a uniform circulation floor
\[
\max_i\left|\oint_{C_i}U\cdot dy\right|\ge c_\Gamma.
\]
Refine the compact cover by circulation sign. Each state cell has \(\sigma_i\in\{-1,+1\}\) with
\[
\boxed{
\sigma_i\Gamma_i\ge c_\Gamma.
}
\]
Failure of a finite sign-stable refinement is already a state/critical transition.

---

## 2. Sign-coherent cycle debt

For a repeated oriented state cycle of length \(q\le M\),
\[
(1-\rho_\Gamma^q)\Gamma_n
=
\sum_{j=0}^{q-1}\rho_\Gamma^{q-1-j}\delta_{n+j}.
\]
Multiply by \(\sigma=\operatorname{sgn}\Gamma_n\):
\[
\sum_{j=0}^{q-1}\rho_\Gamma^{q-1-j}\sigma\delta_{n+j}
\ge
(1-\rho_\Gamma)c_\Gamma.
\]
Since all weights are at most one,
\[
\boxed{
\sum_{j=0}^{q-1}
(\sigma\delta_{n+j})_+
\ge
(1-\rho_\Gamma)c_\Gamma.
}
\]
Thus one event has
\[
\boxed{
\sigma\delta_{n+j_*}
\ge
\frac{(1-\rho_\Gamma)c_\Gamma}{M}.
}
\]

A finite state-cell mismatch \(\varepsilon_{\rm cyc}\) only reduces this gap by \(O(\varepsilon_{\rm cyc})\).

---

## 3. Mesoscopic decomposition

D81 gives on the declared mesoscopic shadowing branch
\[
\delta_n
=
\delta_n^{\rm fvisc}
+
\delta_n^{\rm SGS}
+
\delta_n^{\rm shadow}.
\]
If the filtered-viscous or shadow contribution is not small, D81–85 already route the branch to:
\[
R_{\rm scale}\vee R_{\rm state}\vee R_{\rm crit}
\vee \widetilde{\mathcal S}_{\rm active}.
\]
On the complementary pure compact branch, at least a fixed fraction of the oriented cycle debt must be SGS:
\[
\boxed{
\sum_{\rm cycle}
(\sigma\delta_n^{\rm SGS})_+
\ge
c_{\rm cyc}^{\rm SGS}>0.
}
\]
Therefore one SGS event per bounded cycle satisfies
\[
\boxed{
\sigma\delta_n^{\rm SGS}\ge c_{\rm slip}>0.
}
\]

---

## 4. Positive-density and linear-total-variation theorem

Partition generations into blocks of \(B_*=M+1\). In every block, either:
1. material/carrier state replacement occurs; or
2. a repeated state cycle occurs and produces a sign-coherent SGS reset.

If state replacement is absent on the pure compact branch,
\[
\boxed{
\liminf_{N\to\infty}
\frac{\#\{n<N:\sigma_n\delta_n^{\rm SGS}\ge c_{\rm slip}\}}{N}
\ge
\frac1{M+1}.
}
\]
Consequently
\[
\boxed{
\mathcal V_{\Gamma,+}^{\rm SGS}(N)
\ge
\frac{c_{\rm slip}}{M+1}N-O(1).
}
\]

This is the main D95 theorem.

---

## 5. Exact coarse circulation-flux meaning

Let
\[
f_\ell=-\nabla\cdot R_\ell.
\]
Eyink decomposes
\[
f_\ell=-\nabla k_\ell+f_\ell^*,
\]
where \(f_\ell^*\) is the turbulent vortex force. Since closed-loop integrals of gradients vanish,
\[
\oint_Cf_\ell\cdot dy
=
\oint_Cf_\ell^*\cdot dy.
\]
The coarse circulation flux is
\[
\boxed{
K_\ell(C,t)
=
-\oint_{C_\ell(t)}f_\ell^*\cdot dy.
}
\]
Thus D81’s SGS reset is the period-integrated circulation flux:
\[
\boxed{
\delta_n^{\rm SGS}
=
\int_{I_n}K_{\ell_n}(C_{n,\ell},t)\,dt
}
\]
up to the fixed sign convention.

By Stokes,
\[
K_\ell(C,t)
=
-\int_{\Sigma_\ell(t)}
[\nabla\times\nabla\cdot R_\ell]\cdot n\,dA.
\]
Hence every D95 phase-slip event carries a fixed signed material-surface flux of the differentiated subgrid stress.

---

## 6. Roughness threshold

Eyink’s increment estimate gives schematically
\[
|f_\ell|=O(\ell^{2h-1})
\]
at a point with local velocity Hölder exponent \(h\). For a uniformly finite-length loop,
\[
h_{\min}>\frac12
\Longrightarrow
K_\ell(C,t)\to0
\qquad(\ell\to0).
\]
Therefore the compact phase-slip conveyor requires:
\[
\boxed{
h\le\frac12
}
\]
somewhere on its recurrent active set, unless loop geometry itself filamentates and leaves the compact branch.

This is a necessary roughness condition, not a contradiction.

---

## 7. Relation to derivative-compatible increment defects

Yu’s 2026 filtered-vorticity theorem controls the differentiated stress forcing using a scale-invariant derivative-compatible velocity-increment defect. Therefore every compact fixed-ratio D95 phase-slip event lies in the same finite-scale increment sector already used in D81–85 and D92:
\[
\boxed{
\mathsf C_{\rm slip}
\Longrightarrow
\widetilde{\mathcal S}_{\rm active}
\vee
R_{\rm scale}
\vee
R_{\rm state}
\vee
R_{\rm crit}.
}
\]
D95 does not reopen this finite-scale classification. Its new contribution is the **linear positive total variation across generations**.

---

## 8. Scale-locality caution

Eyink argues that the circulation cascade is scale-local under appropriate locality/cancellation assumptions, but the line integral defining \(K_\ell\) contains delicate cancellations. Therefore D95 treats scale locality as an externally calibrated subbranch, not an unconditional theorem in the present weak compactness class.

Failure of the locality assumptions is already:
\[
R_{\rm scale}\vee R_{\rm state}.
\]

---

## 9. No quantized crossing capacity

The Josephson–Anderson analogy must not be overread. In superfluids the vortices are quantized. In classical turbulence Eyink explicitly emphasizes that the analogous vortex diffusion is a **continuous process because classical vortices are not quantized**.

Therefore D95 cannot define an integer-valued phase-slip stock \(N_{\rm slip}\) with finite initial inventory.

There is no theorem of the form
\[
|\delta|\ge\delta_0
\Longrightarrow
N_{\rm slip}\mapsto N_{\rm slip}-1
\]
for ordinary classical Navier–Stokes/Euler circulation.

This blocks the simplest finite-capacity closure.

---

## 10. Bounded circulation does not bound reset variation

The recurrence
\[
\Gamma_{n+1}
=
\rho_\Gamma\Gamma_n+(1-\rho_\Gamma)\Gamma_*
\]
with \(\Gamma_0=\Gamma_*\) gives
\[
\Gamma_n\equiv\Gamma_*,
\qquad
\delta_n=(1-\rho_\Gamma)\Gamma_*.
\]
Thus
\[
\sup_n|\Gamma_n|<\infty
\]
while
\[
\sum_{n<N}|\delta_n|
=
N(1-\rho_\Gamma)|\Gamma_*|
\to\infty.
\]
A bounded state amplitude therefore cannot be the missing reset capacity.

---

## 11. Existing energy/Morrey capacities do not close the reset TV

The reset total variation is a line/surface circulation functional. The existing kinetic-energy and Morrey controls are volumetric \(L^2\) controls. D82 already demonstrated the codimension-two trace obstruction: one cannot uniformly convert the loop/surface circulation trace into a globally finite volume capacity without additional regularity.

Therefore current:
- kinetic energy,
- Morrey growth,
- filtered diffusion,
- CKN finite-chain costs

do **not** provide a proved upper bound on
\[
\mathcal V_{\Gamma,+}^{\rm SGS}(\infty).
\]

---

## 12. Martingale mean does not control positive variation

Eyink discusses a possible statistical Kelvin/martingale picture in which the circulation flux may average to zero conditionally because the vortex force oscillates.

But
\[
\mathbb E K_\ell=0
\]
does not imply
\[
\mathbb E|K_\ell|=0.
\]
D95’s object is the positive oriented total variation
\[
\mathcal V_{\Gamma,+}^{\rm SGS}(N)\gtrsim N,
\]
so zero mean circulation flux does not close the conveyor.

---

## 13. Final normal form

### Definition — Sign-Coherent SGS Kelvin Phase-Slip Conveyor
\[
\boxed{
\mathsf C_{\rm slip}
}
\]
is a same-parent shrinking-scale sequence satisfying:
1. nontrivial normalized resolved badness;
2. a finite circulation-state family with \(|\Gamma|\ge c_\Gamma\);
3. no material/carrier state replacement;
4. negligible explicit filtered-viscous reset on the mesoscopic branch;
5. compact loop geometry;
6. one sign-coherent SGS reset \(\sigma\delta^{\rm SGS}\ge c_{\rm slip}\) in every \(B_*\)-generation block;
7. linear positive reset variation \(\mathcal V_{\Gamma,+}^{\rm SGS}(N)\gtrsim N\);
8. SGS reset generated by the coarse vortex-force/circulation flux;
9. failure of every uniform \(C^h\), \(h>1/2\), control on the active slip set;
10. active derivative-compatible increment structure;
11. no known finite total-variation capacity.

This is the unique compact reset-source normal form left by D95.

---

## 14. STOP-D95

\[
\boxed{
\begin{minipage}{0.94\linewidth}
A compact Kelvin-reset conveyor can be sharpened to a sign-coherent SGS phase-slip conveyor. Every material-shadowed repeated oriented circulation-state cycle must replenish the strict Type-II Kelvin contraction by a fixed positive aligned reset. After the filtered-viscous and shadow/state terms are removed, the reset is carried by D81’s SGS circulation flux. Hence one oriented SGS phase-slip event occurs in every bounded number of generations and the positive normalized reset total variation grows at least linearly. Eyink’s circulation-cascade theory shows that persistent flux through shrinking finite-length loops requires roughness at or below the \(h=1/2\) threshold, and also warns that the classical phase-slip process is continuous because classical vortices are not quantized. Therefore no integer vortex-crossing inventory is available as a finite capacity. Bounded circulation amplitude also does not bound reset total variation, and the existing energy/Morrey/filtered-diffusion ledgers do not provide a proved global trace-capacity bound. The final compact source is therefore one explicit Sign-Coherent SGS Kelvin Phase-Slip Conveyor; eliminating it requires a rigidity theorem for the sign/coherence/profile of the circulation anomaly, not another energy or packing tax.
\end{minipage}
}
\]

---

## 15. Next autonomous step

### DCRP96 / X72-R79 — Sign-Coherent Circulation-Anomaly Young Profile

Attack the recurring phase-slip at the level of the derivative-compatible increment Young profile.

Tasks:
1. normalize one recurring oriented loop/filter state;
2. insert the exact increment representation of \(\nabla\cdot R_\ell\);
3. extract the existing cylindrical generalized Young profile;
4. represent the oriented circulation flux as a profile functional;
5. test whether same-sign positive-density phase slip forces:
   - a nonzero barycentric bias,
   - covariance orientation locking,
   - a pressure-compatible kernel,
   - or concentration/fiber escape;
6. route affine/pressure-compatible kernels through D25/D87/X72;
7. determine whether a centered symmetric Young profile can support a nonzero same-sign circulation flux.

Desired endpoint:
\[
\boxed{
\mathsf C_{\rm slip}
\Longrightarrow
\text{biased/locked increment Young profile}
\vee
R_{\rm state}
\vee
R_{\rm crit}.
}
\]

**End checkpoint:** DCRP95 / X72-R78.
