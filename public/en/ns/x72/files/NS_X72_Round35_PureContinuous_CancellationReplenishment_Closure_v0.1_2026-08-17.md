# NS × X Integral × 24/72 Paradigm in Practice
## Round 35 — Pure Continuous Cancellation-Replenishment Budget Closure / Cofactor–Pressure Coherence Route

- Date: 2026-08-17
- Version: v0.1
- Status: Proof-Route Experiment / Continuous-Only Replenishment-Audit Branch
- canonical source：UTF-8 Markdown
- canonical math delimiters：inline `$...$`；display `$$...$$`
- Previous round: `NS_X72_Round34_PureContinuous_CancellationBudget_Dynamics_v0.1_2026-08-17.md`
- This round's objective: Round 34 proved that persistent signed cancellation requires minority-sign replenishment. This round specifically audits the two replenishment supply lines of the determinant net-positive branch:
  $$
  -\nu\int_{d<0}\mathcal G_{\det},
  \qquad
  -\int_{d<0}\operatorname{cof}S:H_p.
  $$
  Decomposes the pressure into isotropic / anisotropic cofactor coherence, reconnects the tensor-diffusion curvature to the higher-gradient budget, and examines whether Kato interface dissipation can absorb the bulk curvature.
- Non-claims: This document does not claim that the cancellation reserve must be exhausted in finite time. What this document proves is: neither of the two replenishments is a free reservoir; pressure requires quartic amplitude and signed tensor coherence, and tensor curvature requires a higher-gradient budget and cannot be universally absorbed by the Kato defect.

---

# 0. Round 34 handoff

Let:

$$
d=-\det S.
$$

In the net-positive dangerous branch:

$$
M_D=\int d\,dx>0,
$$

negative-sign cancellation reserve:

$$
\boxed{
R_D
=
2\int_{\{d<0\}}d_-\,dx.
}
$$

Round 34 exact law:

$$
\boxed{
\begin{aligned}
R_D'
={}&
-2\nu
\int_{\{d<0\}}
\mathcal G_{\det}dx
\\
&-
\frac12
\int_{\{d<0\}}
|S\omega|^2dx
\\
&-
2
\int_{\{d<0\}}
\operatorname{cof}S:H_pdx
\\
&-
\mathcal D_D,
\end{aligned}
}
\tag{0.1}
$$

where:

$$
\mathcal D_D\ge0
$$

is the determinant Kato defect.

Round 34 STOP:

$$
\boxed{
\text{STOP-C38}
=
\text{Cancellation-Reserve / Sign-Selective Replenishment Gap}.
}
$$

---

# 1. Trace-free cofactor algebra

For a trace-free symmetric:

$$
S\in\mathbb R^{3\times3},
$$

Cayley–Hamilton gives:

$$
\boxed{
\operatorname{cof}S
=
S^2
-
\frac12|S|^2I.
}
\tag{1.1}
$$

Therefore:

$$
\boxed{
\operatorname{tr}(\operatorname{cof}S)
=
-\frac12|S|^2.
}
\tag{1.2}
$$

Define the trace-free cofactor:

$$
\boxed{
C_S^0
=
(\operatorname{cof}S)^0
=
S^2
-
\frac13|S|^2I.
}
\tag{1.3}
$$

The 3D trace-free identity:

$$
\operatorname{tr}(S^4)
=
\frac12|S|^4
$$

gives:

$$
\boxed{
|C_S^0|^2
=
\frac16|S|^4,
}
\tag{1.4}
$$

Thus:

$$
\boxed{
|C_S^0|
=
\frac{
|S|^2
}{
\sqrt6
}.
}
\tag{1.5}
$$

Furthermore:

$$
\boxed{
|\operatorname{cof}S|
=
\frac12|S|^2.
}
\tag{1.6}
$$

---

# 2. Pressure Hessian decomposition

Let:

$$
\boxed{
H_p^0
=
H_p
-
\frac{
\Delta p
}{3}
I.
}
\tag{2.1}
$$

Then:

$$
\boxed{
H_p
=
H_p^0
+
\frac{
\Delta p
}{3}I.
}
$$

For whole-space incompressible NS:

$$
\boxed{
-\Delta p
=
|S|^2
-
\frac12|\omega|^2.
}
\tag{2.2}
$$

By tensor orthogonality:

$$
\boxed{
\operatorname{cof}S:H_p
=
C_S^0:H_p^0
+
\frac13
\operatorname{tr}(\operatorname{cof}S)
\Delta p.
}
\tag{2.3}
$$

Substituting (1.2) and (2.2):

$$
\boxed{
\operatorname{cof}S:H_p
=
C_S^0:H_p^0
+
\frac16|S|^4
-
\frac1{12}
|S|^2|\omega|^2.
}
\tag{2.4}
$$

---

# 3. Exact pressure-replenishment split

Thus, the pressure contribution in the determinant reserve is:

$$
\boxed{
\begin{aligned}
-2\operatorname{cof}S:H_p
={}&
-2C_S^0:H_p^0
\\
&-
\frac13|S|^4
+
\frac16|S|^2|\omega|^2.
\end{aligned}
}
\tag{3.1}
$$

This splits the pressure replenishment into:

## P-aniso

$$
\boxed{
-2C_S^0:H_p^0.
}
\tag{3.2}
$$

## P-iso

$$
\boxed{
\frac16|S|^2
\left(
|\omega|^2
-
2|S|^2
\right).
}
\tag{3.3}
$$

Therefore, for the isotropic pressure itself to be replenishing, it is necessary that:

$$
\boxed{
|\omega|^2
>
2|S|^2.
}
\tag{3.4}
$$

Otherwise:

$$
P_{\rm iso}\le0.
$$

---

# 4. Cofactor–pressure coherence

In the negative-reserve region:

$$
A_-(t)
=
\{x:d(x,t)<0\},
$$

define:

$$
\boxed{
U_p
=
\|C_S^0\|_{L^2(A_-)},
}
\tag{4.1}
$$

$$
\boxed{
V_p
=
\|H_p^0\|_{L^2(A_-)}.
}
\tag{4.2}
$$

If:

$$
U_pV_p>0,
$$

define the replenishing coherence:

$$
\boxed{
\rho_p^-
=
-
\frac{
\int_{A_-}
C_S^0:H_p^0dx
}{
U_pV_p
}
\in[-1,1].
}
\tag{4.3}
$$

Then the anisotropic pressure replenishment is exactly:

$$
\boxed{
\mathcal P_{\rm aniso}
=
2
\rho_p^-
U_pV_p.
}
\tag{4.4}
$$

Thus:

$$
\boxed{
\rho_p^->0
}
$$

is the required replenishing alignment.

If:

$$
\rho_p^-<0,
$$

the anisotropic pressure instead erodes the cancellation reserve.

---

# 5. Pressure replenishment requires coherence, not amplitude alone

From:

$$
|C_S^0|
=
|S|^2/\sqrt6,
$$

we have:

$$
\boxed{
U_p
=
\frac1{\sqrt6}
\|S\|_{L^4(A_-)}^2.
}
\tag{5.1}
$$

Thus:

$$
\boxed{
\mathcal P_{\rm aniso}
=
\frac{
2
}{
\sqrt6
}
\rho_p^-
\|S\|_{L^4(A_-)}^2
V_p.
}
\tag{5.2}
$$

Even if:

$$
V_p
$$

is large,

if:

$$
\rho_p^-\approx0,
$$

the anisotropic replenishment remains very weak.

Therefore, the pressure supply is:

$$
\boxed{
\text{amplitude}
\times
\text{cofactor–pressure coherence}.
}
$$

This reconnects to the angular/coherence-locking obstruction from Rounds 26–29.

---

# 6. Hilbert-angle pressure phase

If:

$$
|\rho_p^-|<1,
$$

define:

$$
\boxed{
\theta_p^-
=
\arccos
\rho_p^-.
}
\tag{6.1}
$$

Then:

$$
\boxed{
\mathcal P_{\rm aniso}
=
2U_pV_p
\cos\theta_p^-.
}
\tag{6.2}
$$

Therefore, the Nonstationary Angular-Cancellation Lemma from Round 27 can be directly applied to the time integral:

$$
\int
\mathcal P_{\rm aniso}(t)dt.
$$

If:

$$
|\dot\theta_p^-|
\ge
\Omega>0
$$

and the amplitude modulation is controlled,

then the cumulative anisotropic replenishment is suppressed by:

$$
O(\Omega^{-1}).
$$

Thus:

$$
\boxed{
\textbf{
persistent anisotropic pressure replenishment
requires Hilbert-space coherence locking or strong modulation.
}
}
\tag{6.3}
$$

---

# 7. Pressure replenishment envelope

From:

$$
|\operatorname{cof}S|
=
\frac12|S|^2,
$$

we have:

$$
\boxed{
\begin{aligned}
\left|
2
\int_{A_-}
\operatorname{cof}S:H_pdx
\right|
&\le
\int_{A_-}
|S|^2|H_p|dx
\\
&\le
\|S\|_4^2
\|H_p\|_2.
\end{aligned}
}
\tag{7.1}
$$

The whole-space pressure Hessian is the Riesz-transform matrix applied to:

$$
|S|^2-\frac12|\omega|^2.
$$

Thus:

$$
\boxed{
\|H_p\|_2
\le
C
\left(
\|S\|_4^2
+
\|\omega\|_4^2
\right).
}
\tag{7.2}
$$

Therefore:

$$
\boxed{
\mathcal B_p
:=
\left[
-2
\int_{A_-}
\operatorname{cof}S:H_pdx
\right]_+
\le
C
\left(
\|S\|_4^4
+
\|\omega\|_4^4
\right).
}
\tag{7.3}
$$

Thus, the pressure replenishment has no independent reservoir.

It still burns the Round 30 quartic budget.

---

# 8. Vorticity + isotropic-pressure gate

The Round 34 reserve equation already has the vorticity erosion:

$$
-\frac12|S\omega|^2.
$$

Combining with P-iso:

$$
\boxed{
\begin{aligned}
\mathcal E_{\omega,\rm iso}
={}&
-\frac12|S\omega|^2
+
\frac16|S|^2|\omega|^2
-
\frac13|S|^4.
\end{aligned}
}
\tag{8.1}
$$

If:

$$
|S||\omega|>0,
$$

define:

$$
\boxed{
\alpha_\omega
=
\frac{
3|S\omega|^2
}{
|S|^2|\omega|^2
}.
}
\tag{8.2}
$$

Then:

$$
\boxed{
\mathcal E_{\omega,\rm iso}
=
\frac16
|S|^2|\omega|^2
(1-\alpha_\omega)
-
\frac13|S|^4.
}
\tag{8.3}
$$

Therefore, for the combined vorticity + isotropic pressure to be replenishing, it is necessary that:

$$
\boxed{
\alpha_\omega<1
}
\tag{8.4}
$$

and:

$$
\boxed{
|\omega|^2
>
\frac{
2|S|^2
}{
1-\alpha_\omega
}.
}
\tag{8.5}
$$

Thus it requires:

- strong vorticity amplitude;
- alignment with a below-RMS strain direction.

It is not a generic positive supply.

---

# 9. Exact tensor-diffusion curvature

Round 33 defines:

$$
\mathcal G_{\det}
=
\sum_k
D^2\det(S)
[
\partial_kS,
\partial_kS
].
$$

Since:

$$
\det S
=
\frac13
\operatorname{tr}(S^3)
$$

on trace-free $3\times3$ matrices,

and:

$$
\partial_kS
$$

is also trace-free,

we obtain:

$$
\boxed{
\mathcal G_{\det}
=
2
\sum_k
\operatorname{tr}
\left[
S(\partial_kS)^2
\right].
}
\tag{9.1}
$$

Therefore:

$$
\boxed{
|\mathcal G_{\det}|
\le
2
|S|
|\nabla S|^2.
}
\tag{9.2}
$$

---

# 10. Tensor-curvature replenishment envelope

Define:

$$
\boxed{
\mathcal B_{\rm curv}
=
\left[
-2\nu
\int_{A_-}
\mathcal G_{\det}dx
\right]_+.
}
\tag{10.1}
$$

From (9.2):

$$
\boxed{
\mathcal B_{\rm curv}
\le
4\nu
\int
|S|
|\nabla S|^2dx.
}
\tag{10.2}
$$

By Hölder + Sobolev:

$$
\|S\|_3
\lesssim
\|S\|_2^{1/2}
\|\nabla S\|_2^{1/2},
$$

$$
\|\nabla S\|_3
\lesssim
\|\nabla S\|_2^{1/2}
\|\Delta S\|_2^{1/2},
$$

Thus:

$$
\boxed{
\int
|S|
|\nabla S|^2
\lesssim
\|S\|_2^{1/2}
\|\nabla S\|_2^{3/2}
\|\Delta S\|_2.
}
\tag{10.3}
$$

By Young's inequality:

$$
\boxed{
\mathcal B_{\rm curv}
\le
\frac{\nu}{2}
\|\Delta S\|_2^2
+
C\nu
\|S\|_2
\|\nabla S\|_2^3.
}
\tag{10.4}
$$

Thus, the tensor-curvature replenishment also returns to the Round 05 higher-gradient budget.

---

# 11. Can Kato defect absorb tensor curvature?

The Round 34 determinant Kato defect:

$$
\mathcal D_D
$$

originates from:

$$
\nu
\phi_\varepsilon''(d)
|\nabla d|^2
$$

at the limit near the:

$$
d=0
$$

sign interface.

However:

$$
\mathcal G_{\det}
=
2
\sum_k
\operatorname{tr}
[
S(\partial_kS)^2
]
$$

is a bulk negative-region quantity.

Thus, their support geometries are different.

Below we provide an explicit structural witness.

---

# 12. Bulk–Interface Mismatch Witness

Let the divergence-free polynomial velocity be:

$$
\boxed{
\begin{aligned}
u_1
&=
-x_1
+
\frac12x_1^2
+
\frac12x_2^2,
\\
u_2
&=
-(1+x_1)x_2,
\\
u_3
&=
2x_3.
\end{aligned}
}
\tag{12.1}
$$

It can be verified that:

$$
\nabla\cdot u=0.
$$

Its strain is:

$$
\boxed{
S
=
\operatorname{diag}
(
-1+x_1,
-1-x_1,
2
).
}
\tag{12.2}
$$

For:

$$
|x_1|<1,
$$

$$
\det S
=
2(1-x_1^2)>0,
$$

Thus:

$$
\boxed{
d=-\det S<0.
}
\tag{12.3}
$$

When this region is far from the sign interface, the sharp limit of the determinant Kato defect is zero.

However:

$$
\partial_1S
=
\operatorname{diag}(1,-1,0),
$$

and the remaining derivatives are zero.

Therefore:

$$
\boxed{
\mathcal G_{\det}
=
2
\operatorname{tr}
\left[
S(\partial_1S)^2
\right]
=
-4.
}
\tag{12.4}
$$

Thus:

$$
\boxed{
-2\nu\mathcal G_{\det}
=
8\nu>0
}
\tag{12.5}
$$

provides replenishment in the entire local negative-reserve region,

even without any sign-interface Kato defect.

Therefore, there is no purely local universal bound:

$$
\boxed{
[-\mathcal G_{\det}]_+
\le
C
\times
\text{Kato-interface defect density}.
}
\tag{12.6}
$$

This witness is a local divergence-free structural field and is not claimed to be a whole-space finite-energy NS solution.

---

# 13. Tensor-curvature coherence

From:

$$
|\mathcal G_{\det}|
\le
2|S||\nabla S|^2,
$$

where:

$$
|S||\nabla S|>0
$$

define:

$$
\boxed{
\rho_{\rm curv}
=
-
\frac{
\mathcal G_{\det}
}{
2|S||\nabla S|^2
}
\in[-1,1].
}
\tag{13.1}
$$

Then the tensor-curvature replenishment density is:

$$
\boxed{
-2\nu\mathcal G_{\det}
=
4\nu
|S|
|\nabla S|^2
\rho_{\rm curv}.
}
\tag{13.2}
$$

Thus it also possesses:

$$
\boxed{
\text{amplitude}
\times
\text{signed geometric coherence}.
}
$$

Not all higher-gradient activity replenishes the cancellation.

---

# 14. Total replenishment envelope

Define:

$$
\boxed{
\mathcal E_D
=
\frac12
\int_{A_-}
|S\omega|^2dx
+
\mathcal D_D
}
\tag{14.1}
$$

as the mandatory erosion.

From the Round 34 exact equation and Sections 7 and 10:

$$
\boxed{
R_D'
\le
\mathcal B_{\rm curv}
+
\mathcal B_p
-
\mathcal E_D.
}
\tag{14.2}
$$

where:

$$
\boxed{
\mathcal B_p
\lesssim
\|S\|_4^4
+
\|\omega\|_4^4,
}
\tag{14.3}
$$

and:

$$
\boxed{
\mathcal B_{\rm curv}
\le
\frac{\nu}{2}
\|\Delta S\|_2^2
+
C\nu
\|S\|_2
\|\nabla S\|_2^3.
}
\tag{14.4}
$$

---

# 15. Cancellation-Replenishment Budget Inequality

Integrating (14.2):

$$
\boxed{
\begin{aligned}
R_D(t_1)
+
\int_{t_0}^{t_1}
\mathcal E_Ddt
\le{}&
R_D(t_0)
\\
&+
\int_{t_0}^{t_1}
\left(
\mathcal B_{\rm curv}
+
\mathcal B_p
\right)dt.
\end{aligned}
}
\tag{15.1}
$$

We name this:

$$
\boxed{
\textbf{Cancellation-Replenishment Budget Inequality}.
}
$$

Therefore, persistent determinant cancellation has no new free energy source.

All replenishment is paid for by:

$$
\boxed{
\text{higher derivative}
+
\text{quartic amplitude}
+
\text{coherence}
}
$$

---

# 16. Cancellation Exhaustion Criterion

If in:

$$
[t_0,T)
$$

the net-positive branch:

$$
M_D>0
$$

holds continuously, and:

$$
\boxed{
\int_{t_0}^{T}
\left(
\mathcal B_{\rm curv}
+
\mathcal B_p
\right)dt
<
\infty,
}
\tag{16.1}
$$

but:

$$
\boxed{
\int_{t_0}^{T}
\mathcal E_Ddt
=
\infty,
}
\tag{16.2}
$$

then (15.1) contradicts:

$$
R_D\ge0
$$

Thus:

$$
\boxed{
\textbf{
divergent cancellation erosion forces divergent replenishment supply
or termination of the persistent net-positive cancellation branch.
}
}
\tag{16.3}
$$

This is a conditional exhaustion criterion, not a global regularity theorem.

---

# 17. Replenishment efficiency ratio

Define the interval budget:

$$
\boxed{
\mathfrak R_{\rm rep}(I)
=
\frac{
\int_I
\mathcal E_Ddt
}{
R_D(t_0)
+
\int_I
(
\mathcal B_{\rm curv}
+
\mathcal B_p
)dt
}.
}
\tag{17.1}
$$

If:

$$
\boxed{
\mathfrak R_{\rm rep}(I)>1,
}
\tag{17.2}
$$

then the persistent cancellation reserve must fail or the branch assumption must change before the end of the interval.

This is a continuous budget diagnostic.

---

# 18. Pressure replenishment returns to phase locking

The anisotropic supply is:

$$
\mathcal P_{\rm aniso}
=
2U_pV_p
\rho_p^-.
$$

If:

$$
\rho_p^-
=
\cos\theta_p^-,
$$

then it is completely isomorphic to Round 27's:

$$
A\cos\theta
$$

Thus, long-lived pressure replenishment requires:

$$
\boxed{
\text{cofactor–pressure phase locking}
\vee
\text{strong amplitude modulation}
\vee
\text{phase-speed modulation}.
}
\tag{18.1}
$$

Therefore:

$$
\boxed{
\textbf{
cancellation replenishment and angular phase locking are not separate bosses.
}
}
\tag{18.2}
$$

If pressure is to hide the determinant danger long-term,

it must simultaneously pay for:

- quartic amplitude;
- nonlocal tensor coherence persistence.

---

# 19. Pressure amplitude budget remains old quartic obstruction

3D interpolation:

$$
\|S\|_4^4
\lesssim
\|S\|_2
\|\nabla S\|_2^3.
$$

Hodge identities give:

$$
\|\omega\|_4^4
\lesssim
\|\omega\|_2
\|\nabla\omega\|_2^3
\asymp
\|S\|_2
\|\nabla S\|_2^3.
$$

Therefore:

$$
\boxed{
\mathcal B_p
\lesssim
\|S\|_2
\|\nabla S\|_2^3.
}
\tag{19.1}
$$

Thus, the amplitude supply of the pressure replenishment still returns to the Round 05 / 30 higher-gradient nonlinearity.

---

# 20. No-free-replenishment synthesis

By Round 35:

## tensor-diffusion curvature

requires the:

$$
\boxed{
\nu
\int
|S||\nabla S|^2
}
$$

higher-gradient budget,

and cannot be universally absorbed by the Kato interface defect.

## isotropic pressure

can only replenish under amplitude gates such as:

$$
|\omega|^2>2|S|^2
$$

## anisotropic pressure

requires the:

$$
\boxed{
\rho_p^->0
}
$$

cofactor–pressure coherence,

and its amplitude is controlled by the quartic budget.

## vorticity term

In the net-positive branch:

$$
\boxed{
-\frac12|S\omega|^2
}
$$

directly erodes the reserve.

Thus:

$$
\boxed{
\textbf{No Free Cancellation-Replenishment Principle}.
}
\tag{20.1}
$$

---

# 21. Representation-stable obstruction confluence

Round 04:

$$
\text{nonlocal pressure}
$$

Round 05:

$$
\text{higher-gradient strain}
$$

Round 18:

$$
\text{vorticity interaction}
$$

Round 26–29:

$$
\text{nonlocal coherence / phase lock}
$$

Round 34:

$$
\text{cancellation replenishment}
$$

Round 35 recompresses them into:

$$
\boxed{
\text{replenishment}
=
\text{higher-gradient amplitude}
+
\text{pressure coherence}
-
\text{vorticity erosion}.
}
\tag{21.1}
$$

Thus, the obstruction core is once again representation-stable.

---

# 22. STOP-C39 — Replenishment-Closure / Cofactor–Pressure Coherence Gap

$$
\boxed{
\begin{aligned}
\text{layer}
&=
\mathrm{cancellation\ replenishment\ closure},
\\
\text{tensor curvature}
&=
2\sum_k\operatorname{tr}[S(\partial_kS)^2],
\\
\text{tensor-curvature supply}
&\to
\mathrm{higher\text{-}gradient\ budget},
\\
\text{Kato absorption}
&=
\mathrm{false\ as\ universal\ mechanism},
\\
\text{pressure split}
&=
\mathrm{isotropic}
+
\mathrm{anisotropic},
\\
\text{isotropic replenishment}
&=
\mathrm{amplitude/alignment\ gated},
\\
\text{anisotropic replenishment}
&=
\mathrm{cofactor\text{-}pressure\ coherence},
\\
\text{pressure amplitude}
&\to
\mathrm{quartic\ strain/vorticity},
\\
\text{persistent pressure supply}
&\to
\mathrm{phase/coherence\ locking},
\\
\text{mandatory erosion}
&=
\mathcal D_D
+
\frac12\int_{d<0}|S\omega|^2,
\\
\text{missing}
&=
\mathrm{unconditional\ control\ of\ cofactor\text{-}pressure\ coherence
and\ tensor\text{-}curvature\ replenishment},
\\
T_{\mathsf C\to\mathsf D}
&=
\mathrm{NOT\ REACHED}.
\end{aligned}
}
$$

Named:

$$
\boxed{
\textbf{STOP-C39:
Replenishment-Closure / Cofactor–Pressure Coherence Gap}.
}
$$

---

# 23. 24/72 Ledger — Round 35

| Step | object | $B$ | $U$ | $O$ | $L$ | status |
|---|---|---|---|---|---|---|
| C512 | trace-free cofactor $C_S^0$ | $\mathsf C$ | tensor algebra | relational | $\mathsf F$ | EXACT |
| C513 | cofactor norm identities | $\mathsf C$ | algebraic | scalar | $\mathsf F$ | PROVED |
| C514 | pressure Hessian trace split | $\mathsf C$ | tensor decomposition | relational | $\mathsf F$ | EXACT |
| C515 | exact pressure replenishment split | $\mathsf C$ | sign decomposition | targeted | $\mathsf F$ | EXACT |
| C516 | cofactor–pressure coherence $\rho_p^-$ | $\mathsf C$ | Hilbert geometry | scalar | $\mathsf F$ | FORM |
| C517 | anisotropic pressure factorization | $\mathsf C$ | amplitude/coherence | targeted | $\mathsf F$ | EXACT |
| C518 | Hilbert-angle phase lock | $\mathsf C$ | angular dynamics | scalar | $\mathsf F$ | CONNECTION |
| C519 | pressure quartic envelope | $\mathsf C$ | Riesz / Hölder | targeted | $\mathsf F$ | PROVED |
| C520 | isotropic-vorticity gate | $\mathsf C$ | alignment/amplitude | targeted | $\mathsf F$ | PROVED |
| C521 | exact determinant curvature $\mathcal G_{\det}$ | $\mathsf C$ | second derivative | relational | $\mathsf F$ | EXACT |
| C522 | curvature pointwise envelope | $\mathsf C$ | tensor inequality | scalar | $\mathsf F$ | PROVED |
| C523 | higher-gradient curvature budget | $\mathsf C$ | Sobolev / Young | targeted | $\mathsf F$ | PROVED |
| C524 | Bulk–Interface Mismatch Witness | $\mathsf C$ | local structural field | targeted | $\mathsf F$ | CONSTRUCTED |
| C525 | Kato absorbs curvature | $\mathsf C$ | interface/bulk comparison | targeted | $\mathsf F$ | REFUTED universally |
| C526 | curvature coherence $\rho_{\rm curv}$ | $\mathsf C$ | geometric alignment | scalar | $\mathsf F$ | FORM |
| C527 | total replenishment envelope | $\mathsf C$ | budget synthesis | $\mathsf X$ | $\mathsf F$ | PROVED |
| C528 | cancellation-replenishment inequality | $\mathsf C$ | spacetime budget | targeted | $\mathsf F$ | PROVED |
| C529 | cancellation exhaustion criterion | $\mathsf C$ | continuation logic | targeted | $\mathsf F$ | CONDITIONAL |
| C530 | no-free-replenishment synthesis | $\mathsf C$ | route compression | $\mathsf X$ | $\mathsf F$ | ESTABLISHED |
| C531 | unconditional cofactor-pressure control | $\mathsf C$ | coupled NS | targeted | $\mathsf F$ | OPEN / STOP-C39 |

---

# 24. Continuous-versus-discrete status

New objects in this round:

- trace-free cofactor tensor;
- pressure Hessian trace/deviatoric split;
- Hilbert-space coherence angle;
- tensor-curvature coherence;
- continuous spacetime replenishment budget;
- continuous sign region:
  $$
  \{d<0\}.
  $$

All are continuous tensor / measure / PDE objects.

There are no:

- sign cell enumeration;
- discrete pressure modes;
- discrete curvature events;
- graph replenishment network.

Therefore:

$$
\boxed{
T_{\mathsf C\to\mathsf D}
=
\text{NOT YET REACHED}.
}
$$

---

# 25. Strongest results of Round 35

## R35-A — exact pressure split

$$
\boxed{
-2\operatorname{cof}S:H_p
=
-2C_S^0:H_p^0
-\frac13|S|^4
+\frac16|S|^2|\omega|^2.
}
$$

## R35-B — exact cofactor anisotropy size

$$
\boxed{
|C_S^0|
=
|S|^2/\sqrt6.
}
$$

## R35-C — pressure replenishment coherence

$$
\boxed{
\mathcal P_{\rm aniso}
=
2\rho_p^-U_pV_p.
}
$$

large nonlocal pressure amplitude without positive $\rho_p^-$ does not replenish cancellation.

## R35-D — exact tensor-diffusion curvature

$$
\boxed{
\mathcal G_{\det}
=
2
\sum_k
\operatorname{tr}
[
S(\partial_kS)^2
].
}
$$

## R35-E — Kato absorption no-go

there exist local divergence-free strain fields with:

$$
d<0,
\qquad
\mathcal D_D=0,
\qquad
-\mathcal G_{\det}>0.
$$

Thus, tensor-curvature replenishment can live in the bulk away from the sign interface.

## R35-F — replenishment budget

$$
\boxed{
R_D(t_1)
+
\int_I\mathcal E_D
\le
R_D(t_0)
+
\int_I
(
\mathcal B_{\rm curv}
+
\mathcal B_p
).
}
$$

---

# 26. Next round — Cofactor–Pressure Coherence Dynamics

Round 35 compresses the truly nonlocal replenishment into:

$$
\boxed{
\rho_p^-(t)
=
-
\frac{
\langle C_S^0,H_p^0\rangle_{A_-}
}{
\|C_S^0\|_{2,A_-}
\|H_p^0\|_{2,A_-}
}.
}
$$

The next round will directly investigate:

1. How $\rho_p^-$ evolves with the moving negative-determinant region;
2. The material derivative of $C_S^0$;
3. The time derivative / pressure Poisson differentiation of $H_p^0$;
4. The moving sign-region boundary flux;
5. Whether the pressure replenishment coherence can phase-lock;
6. If rapid dephasing occurs, whether the Round 27 cancellation lemma suppresses the cumulative replenishment;
7. If stable replenishing coherence exists, what pressure/source organization it requires;
8. Maintaining continuous tensor and moving-domain transport without discrete sign-state switching.

---

# 27. External primary-source anchors

1. Maurizio Carbone, Michele Iovieno, Andrew D. Bragg, *Gauge symmetry and dimensionality reduction of the anisotropic pressure Hessian*, arXiv:1911.08652.
   - The anisotropic pressure Hessian is a nonlocal functional in velocity-gradient dynamics, and has a strong alignment structure with the strain eigenframe / vorticity geometry.

2. Josin Tom, Maurizio Carbone, Andrew D. Bragg, *Exploring the turbulent velocity gradients at different scales from the perspective of the strain-rate eigenframe*, arXiv:2005.04300.
   - The DNS / eigenframe-dynamics background where the anisotropic pressure Hessian plays a key role in strain eigenframe rotation.

3. Borys Álvarez-Samaniego, Wilson P. Álvarez-Samaniego, Pedro G. Fernández-Dalgo, *On the use of the Riesz transforms to determine the pressure term in the incompressible Navier-Stokes equations on the whole space*, arXiv:2004.02588.
   - The background of the Riesz-transform representation for whole-space pressure.

4. Evan Miller, *On the interaction of strain and vorticity for solutions of the Navier--Stokes equation*, arXiv:2407.02691.
   - The background of strain–vorticity interaction, higher-gradient identities, and nonlinear depletion.

The cofactor norm identities, pressure replenishment decomposition, tensor-diffusion curvature identity, Bulk–Interface Mismatch Witness, and Cancellation-Replenishment Budget Inequality in this round are all directly derived in this document.

---

# 28. Commit state

$$
\boxed{
\begin{aligned}
\text{Route}
&=
\mathrm{Pure\ Continuous\ Cancellation\text{-}Replenishment\ Closure},
\\
\text{Essential }\mathsf C\to\mathsf D
&=
\mathrm{Not\ reached},
\\
\text{Tensor-curvature supply}
&=
\mathrm{higher\text{-}gradient\ budget},
\\
\text{Universal Kato absorption}
&=
\mathrm{false},
\\
\text{Pressure amplitude supply}
&=
\mathrm{quartic\ budget},
\\
\text{Anisotropic pressure supply}
&=
\mathrm{cofactor\text{-}pressure\ coherence},
\\
\text{Persistent pressure replenishment}
&=
\mathrm{phase\ locking/modulation},
\\
\text{No free replenishment}
&=
\mathrm{established\ as\ route\ map},
\\
\text{STOP-C39}
&=
\mathrm{Replenishment\text{-}Closure/Cofactor\text{-}Pressure\ Coherence\ Gap},
\\
\text{Next}
&=
\mathrm{Cofactor\text{-}Pressure\ Coherence\ Dynamics}.
\end{aligned}
}
$$