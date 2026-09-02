# NS × X Integral × 24/72 Paradigm Practice
## Round 40 — Pure Continuous Hardy–BMO Dual Commutator / Critical Campanato-Transfer Route

- Date: 2026-08-17
- Version: v0.1
- Status: Proof-Route Experiment / Continuous-Only Hardy–BMO Endpoint Branch
- canonical source：UTF-8 Markdown
- canonical math delimiters：inline `$...$`；display `$$...$$`
- Previous round: `NS_X72_Round39_PureContinuous_CriticalEndpoint_DiniHardyCompensation_v0.1_2026-08-17.md`
- This round's objective: Round 39 confirmed that incompressibility provides Hardy-space compensation for the pressure source, but does not automatically provide radial Dini summability. This round switches to the dual route:
  $$
  q\in\mathcal H^1,
  \qquad
  [u\cdot\nabla,\mathcal T_0^\ast]E_p
  \stackrel{?}{\in}
  \mathrm{BMO}.
  $$
  Utilizing the Round 38 pressure self-commutator null identity, we further reduce the BMO partner to the local cofactor $C_S^0$, establishing an exact two-increment commutator representation, the Hardy–BMO energy charging law, and the critical Campanato/Dini threshold.
- Non-claims: This document does not prove that the dual commutator unconditionally belongs to BMO. What is proven here is: the Hardy side can be paid for by incompressible enstrophy, but the BMO side fully inherits the one-total-derivative criticality; the standard Coifman–Rochberg–Weiss $L^p$ commutator estimate itself does not provide the required BMO target.

---

# 0. Round 39 handoff

Round 39 obtained the incompressible pressure source:

$$
\boxed{
q
=
|S|^2-\frac12|\omega|^2
=
\sum_j
\nabla u_j\cdot\partial_j u,
}
\tag{0.1}
$$

where each term is a curl-free / divergence-free product.

Thus, the classical div–curl / incompressibility compensation gives:

$$
\boxed{
\|q\|_{\mathcal H^1}
\lesssim
\|\nabla u\|_2^2.
}
\tag{0.2}
$$

Round 38–39 defect commutator pairing:

$$
\boxed{
\mathcal J_{\rm TR}
=
\left\langle
E,
[D_u,\mathcal T_0]q
\right\rangle,
\qquad
D_u=u\cdot\nabla.
}
\tag{0.3}
$$

Round 39 dual identity:

$$
\boxed{
\mathcal J_{\rm TR}
=
\left\langle
[D_u,\mathcal T_0^\ast]E,
q
\right\rangle.
}
\tag{0.4}
$$

Round 39 STOP:

$$
\boxed{
\text{STOP-C43}
=
\text{Critical Dini / Hardy–Increment Mismatch Gap}.
}
$$

---

# 1. Pressure component disappears from the dual pairing

Round 38 Pressure Self-Commutator Null:

$$
\boxed{
\left\langle
H,
[D_u,\mathcal T_0]q
\right\rangle
=
0,
}
\tag{1.1}
$$

where:

$$
H=\mathcal T_0q.
$$

Since:

$$
E=H+C,
$$

we obtain:

$$
\boxed{
\mathcal J_{\rm TR}
=
\left\langle
C,
[D_u,\mathcal T_0]q
\right\rangle.
}
\tag{1.2}
$$

Dualizing:

$$
\boxed{
\mathcal J_{\rm TR}
=
\left\langle
[D_u,\mathcal T_0^\ast]C,
q
\right\rangle.
}
\tag{1.3}
$$

Define:

$$
\boxed{
\mathcal A_C
=
[D_u,\mathcal T_0^\ast]C.
}
\tag{1.4}
$$

Therefore, the true Hardy–BMO target is not:

$$
[D_u,\mathcal T_0^\ast]E,
$$

but rather:

$$
\boxed{
\mathcal A_C
}
$$

built only from velocity transport and local cofactor geometry.

---

# 2. Hardy–BMO charging law

From the real Hardy–BMO duality:

$$
\boxed{
|\mathcal J_{\rm TR}|
\le
C
\|q\|_{\mathcal H^1}
\|\mathcal A_C\|_{\mathrm{BMO}}.
}
\tag{2.1}
$$

Using (0.2):

$$
\boxed{
|\mathcal J_{\rm TR}|
\le
C
\|\nabla u\|_2^2
\|\mathcal A_C\|_{\mathrm{BMO}}.
}
\tag{2.2}
$$

Named:

$$
\boxed{
\textbf{Hardy–BMO Commutator Charging Law}.
}
$$

This is the first core route reduction of this round.

---

# 3. Energy-dissipation weighted spacetime closure

NS kinetic-energy inequality:

$$
\boxed{
\frac12
\|u(t)\|_2^2
+
\nu
\int_0^t
\|\nabla u(s)\|_2^2ds
\le
\frac12
\|u_0\|_2^2.
}
\tag{3.1}
$$

So if:

$$
\boxed{
\|\mathcal A_C\|_{L_t^\infty\mathrm{BMO}_x}
\le
B_\ast
}
\tag{3.2}
$$

on:

$$
[0,T],
$$

then:

$$
\boxed{
\int_0^T
|\mathcal J_{\rm TR}(t)|dt
\le
\frac{
C
}{
\nu
}
\|u_0\|_2^2
B_\ast.
}
\tag{3.3}
$$

More generally, as long as:

$$
\boxed{
\int_0^T
\|\nabla u\|_2^2
\|\mathcal A_C\|_{\mathrm{BMO}}
dt
<
\infty,
}
\tag{3.4}
$$

the transport–Riesz contribution can be directly added to the defect-energy ledger.

Thus, the Hardy side itself is already connected to the basic energy dissipation.

The real problem is entirely transferred to:

$$
\boxed{
\mathcal A_C\in\mathrm{BMO}.
}
$$

---

# 4. Exact operator factorization

Since:

$$
\mathcal T_0^\ast
$$

commutes with spatial derivatives,

$$
\boxed{
\begin{aligned}
\mathcal A_C
&=
[D_u,\mathcal T_0^\ast]C
\\
&=
\sum_{k=1}^3
[u_k,\mathcal T_0^\ast]
(
\partial_kC
).
\end{aligned}
}
\tag{4.1}
$$

Named:

$$
\boxed{
\textbf{CRW Factorization of the Transport Commutator}.
}
$$

This connects the transport commutator to classical Coifman–Rochberg–Weiss type commutators.

---

# 5. What standard CRW theory actually gives

For a Calderón–Zygmund operator:

$$
T,
$$

the natural strong estimate of classical CRW theory is:

$$
\boxed{
\|[b,T]f\|_{L^p}
\le
C_p
\|b\|_{\mathrm{BMO}}
\|f\|_{L^p},
\qquad
1<p<\infty.
}
\tag{5.1}
$$

Thus, (4.1) gives:

$$
\boxed{
\|\mathcal A_C\|_{L^p}
\le
C_p
\|u\|_{\mathrm{BMO}}
\|\nabla C\|_{L^p}.
}
\tag{5.2}
$$

However, the Hardy–BMO dual route requires:

$$
\boxed{
\mathcal A_C\in\mathrm{BMO},
}
$$

not:

$$
L^p.
$$

Therefore:

$$
\boxed{
\textbf{
standard CRW boundedness does not by itself close the Hardy–BMO route.
}
}
\tag{5.3}
$$

This is a target-space mismatch, not the non-existence of the commutator.

---

# 6. Exact double-increment kernel

Let:

$$
K_0(z)
$$

be:

$$
\mathcal T_0
$$

's even trace-free kernel.

Direct kernel calculation:

$$
\boxed{
\mathcal A_C(x)
=
\operatorname{p.v.}
\int
[
u(x)-u(y)
]
\cdot
\nabla K_0(x-y)
:
C(y)
\,dy.
}
\tag{6.1}
$$

If:

$$
C
$$

is a constant tensor,

the commutator must be zero.

Using:

$$
\nabla\cdot u=0
$$

it can be verified that:

$$
\operatorname{p.v.}
\int
[
u(x)-u(y)
]
\cdot
\nabla K_0(x-y)
dy
=
0.
$$

Thus, it can be losslessly rewritten as:

$$
\boxed{
\mathcal A_C(x)
=
\operatorname{p.v.}
\int
[
u(x)-u(y)
]
\cdot
\nabla K_0(x-y)
:
[
C(y)-C(x)
]
dy.
}
\tag{6.2}
$$

Named:

$$
\boxed{
\textbf{Dual Two-Increment Commutator Identity}.
}
$$

---

# 7. Hardy cancellation replaces the third increment

Round 38 primal pairing:

$$
\delta u
\times
\delta E
\times
\delta q.
$$

Round 40 dual representation:

$$
q\in\mathcal H^1
$$

absorbs the source cancellation into the Hardy test structure,

while the BMO partner is left with only:

$$
\boxed{
\delta u
\times
\delta C.
}
$$

Therefore:

$$
\boxed{
\textbf{
Hardy compensation removes the explicit }q\textbf{ increment,
but does not remove the total derivative threshold.
}
}
\tag{7.1}
$$

It shifts the critical regularity burden from the three-field simplex to the two-field edge.

---

# 8. Local two-increment modulus

Define the uniform translation moduli:

$$
\boxed{
\omega_{u,\infty}(r)
=
\sup_{|z|\le r}
\|\delta_zu\|_\infty,
}
\tag{8.1}
$$

$$
\boxed{
\omega_{C,\infty}(r)
=
\sup_{|z|\le r}
\|\delta_zC\|_\infty.
}
\tag{8.2}
$$

From:

$$
|\nabla K_0(z)|
\lesssim
|z|^{-4},
$$

we have the near-diagonal absolute envelope:

$$
\boxed{
\|\mathcal A_C^{<\ell}\|_\infty
\lesssim
\int_0^\ell
\frac{
\omega_{u,\infty}(r)
\omega_{C,\infty}(r)
}{
r^2
}
dr.
}
\tag{8.3}
$$

Thus, the near part is also controlled by the same quantity for its BMO norm.

Define:

$$
\boxed{
\mathfrak D_{u,C}^{\mathrm{BMO}}(\ell)
=
\int_0^\ell
\frac{
\omega_{u,\infty}(r)
\omega_{C,\infty}(r)
}{
r^2
}
dr.
}
\tag{8.4}
$$

---

# 9. Two-field one-total-derivative threshold

If:

$$
\omega_{u,\infty}(r)
\lesssim
r^{s_u},
$$

$$
\omega_{C,\infty}(r)
\lesssim
r^{s_C},
$$

then:

$$
\mathfrak D_{u,C}^{\mathrm{BMO}}
$$

near zero behaves as:

$$
\boxed{
\int_0
r^{s_u+s_C-2}dr.
}
\tag{9.1}
$$

Therefore, absolute local closure requires:

$$
\boxed{
s_u+s_C>1.
}
\tag{9.2}
$$

The critical endpoint:

$$
\boxed{
s_u+s_C=1
}
\tag{9.3}
$$

once again leaves only a:

$$
\int_0
\frac{dr}{r}
$$

type Dini/log barrier.

Named:

$$
\boxed{
\textbf{Hardy-Absorbed One-Derivative Threshold}.
}
$$

---

# 10. Exact scaling of the two-field endpoint

NS scaling:

$$
u_\Lambda
=
\Lambda
u(\Lambda x,\Lambda^2t),
$$

$$
C_\Lambda
=
\Lambda^4
C(\Lambda x,\Lambda^2t).
$$

Hölder/Campanato seminorm scales:

$$
[u_\Lambda]_{C^{s_u}}
=
\Lambda^{1+s_u}
[u]_{C^{s_u}},
$$

$$
[C_\Lambda]_{C^{s_C}}
=
\Lambda^{4+s_C}
[C]_{C^{s_C}}.
$$

The product scales as:

$$
\boxed{
\Lambda^{5+s_u+s_C}.
}
\tag{10.1}
$$

And:

$$
\mathcal A_C
=
[D_u,\mathcal T_0^\ast]C
$$

scales as:

$$
\boxed{
\Lambda^6.
}
\tag{10.2}
$$

So exact criticality requires:

$$
\boxed{
s_u+s_C=1.
}
\tag{10.3}
$$

Thus, the Hardy–BMO route does not change the total critical derivative count.

It merely redistributes which side carries the cancellation.

---

# 11. Cofactor modulus is strain modulus with amplitude

Round 38:

$$
C
=
S^2-\frac13|S|^2I.
$$

Exact increment:

$$
\boxed{
\begin{aligned}
\delta C
={}&
\frac12
[
(S_x+S_y)\delta S
+
\delta S(S_x+S_y)
]
\\
&-
\frac13
[
(S_x+S_y):\delta S
]
I.
\end{aligned}
}
\tag{11.1}
$$

Therefore:

$$
\boxed{
|\delta C|
\le
C
(
|S_x|+|S_y|
)
|\delta S|.
}
\tag{11.2}
$$

Thus:

$$
\boxed{
\text{BMO commutator endpoint}
\to
\text{velocity increment}
\times
\text{strain amplitude}
\times
\text{strain increment}.
}
\tag{11.3}
$$

It still returns to strain regularity, rather than a new pressure reservoir.

---

# 12. Energy-level Hardy gain is real

From the NS energy:

$$
\nu
\int_0^T
\|\nabla u\|_2^2dt
\le
\frac12\|u_0\|_2^2,
$$

and:

$$
\|q\|_{\mathcal H^1}
\lesssim
\|\nabla u\|_2^2,
$$

we have:

$$
\boxed{
\int_0^T
\|q(t)\|_{\mathcal H^1}dt
\lesssim
\frac{
\|u_0\|_2^2
}{
\nu
}.
}
\tag{12.1}
$$

Therefore, the Hardy pressure-source norm is indeed an energy-level budget in the spacetime $L_t^1$ sense.

This is the strongest usable consequence of the Round 39 incompressibility gain.

---

# 13. But the BMO partner is not energy-level free

If one hopes to rely solely on:

$$
\|\nabla u\|_2,
\qquad
\|\nabla S\|_2
$$

and other low $L^2$ Sobolev quantities to directly control:

$$
\|\mathcal A_C\|_{\mathrm{BMO}},
$$

scaling / concentration immediately shows that this cannot be a simple energy-level estimate.

$\mathrm{BMO}$ preserves for:

$$
\mathcal A_C
$$

the amplitude scaling:

$$
\Lambda^6.
$$

while ordinary $L^2$ derivative norms will lose powers due to spatial integrability.

Therefore:

$$
\boxed{
\textbf{
Hardy energy control does not automatically imply a matching BMO commutator control.
}
}
\tag{13.1}
$$

---

# 14. Standard CRW fallback returns to higher gradients

If we abandon the Hardy–BMO duality,

and instead use:

$$
q\in L^{p'},
\qquad
\mathcal A_C\in L^p,
$$

then the CRW factorization is applicable.

Taking:

$$
p=\frac32,
\qquad
p'=3.
$$

we have:

$$
\boxed{
|\mathcal J_{\rm TR}|
\le
\|q\|_3
\|\mathcal A_C\|_{3/2}
}
\tag{14.1}
$$

and:

$$
\boxed{
\|\mathcal A_C\|_{3/2}
\lesssim
\|u\|_{\mathrm{BMO}}
\|\nabla C\|_{3/2}.
}
\tag{14.2}
$$

---

# 15. CRW fallback quantitative return to Round 05

Sobolev / Hodge:

$$
\boxed{
\|u\|_{\mathrm{BMO}}
\lesssim
\|\nabla u\|_3
\lesssim
\|S\|_2^{1/2}
\|\nabla S\|_2^{1/2}.
}
\tag{15.1}
$$

Cofactor gradient:

$$
|\nabla C|
\lesssim
|S||\nabla S|,
$$

so:

$$
\boxed{
\|\nabla C\|_{3/2}
\lesssim
\|S\|_6
\|\nabla S\|_2
\lesssim
\|\nabla S\|_2^2.
}
\tag{15.2}
$$

Pressure source:

$$
\boxed{
\|q\|_3
\lesssim
\|S\|_6^2
+
\|\omega\|_6^2
\lesssim
\|\nabla S\|_2^2.
}
\tag{15.3}
$$

Therefore:

$$
\boxed{
|\mathcal J_{\rm TR}|
\lesssim
\|S\|_2^{1/2}
\|\nabla S\|_2^{9/2}.
}
\tag{15.4}
$$

This is far higher than the basic energy/enstrophy budget.

Therefore:

$$
\boxed{
\textbf{
the standard CRW }L^p\textbf{ fallback closes legality
but returns directly to the old higher-gradient obstruction.}
}
\tag{15.5}
$$

---

# 16. Why recent generic BMO relaxation no-go matters

The transport–Riesz commutator literature shows:

For broad Riesz interaction classes,

the common:

$$
\|\nabla u\|_\infty
$$

transport regularity cannot generally be directly relaxed to:

$$
\|\nabla u\|_{\mathrm{BMO}}.
$$

Therefore, we cannot automatically claim, just because the Hardy–BMO duality appears in this round, that:

$$
\boxed{
\text{BMO is enough for every part of the transport commutator}.
}
$$

Our special NS pairing indeed has more than generic norm estimates:

- pressure self-null;
- cofactor reduction;
- two-increment cancellation;

But the BMO endpoint still needs to be re-proven using these special structures, rather than applying a generic wishful bound.

---

# 17. Hardy cancellation and two-increment BMO are equivalent route views

Round 38 primal:

$$
\boxed{
\delta u
\,
\delta E
\,
\delta q.
}
$$

Round 40 dual:

$$
\boxed{
q\in\mathcal H^1
}
$$

plus:

$$
\boxed{
\delta u
\,
\delta C.
}
$$

can be understood as:

$$
\boxed{
\text{the Hardy atom cancellation replaces the explicit source increment}.
}
\tag{17.1}
$$

But the critical derivative count remains one.

Therefore, Hardy–BMO is not a completely different physical mechanism.

It is the dual representation of the same commutator cancellation.

---

# 18. Conditional Hardy–BMO closure theorem

Assume smooth NS on:

$$
[0,T],
$$

and:

$$
\boxed{
\mathcal A_C
=
[u\cdot\nabla,\mathcal T_0^\ast]C
\in
L_t^\infty\mathrm{BMO}_x,
}
\tag{18.1}
$$

with:

$$
\|\mathcal A_C\|_{L_t^\infty\mathrm{BMO}}
\le
B_\ast.
$$

then:

$$
\boxed{
\int_0^T
|
\langle
E,
[u\cdot\nabla,\mathcal T_0]q
\rangle
|
dt
\le
C
\nu^{-1}
\|u_0\|_2^2
B_\ast.
}
\tag{18.2}
$$

Thus, the transport–Riesz contribution to the affine-defect energy is globally finite on the interval.

This is a genuine conditional closure.

However, hypothesis (18.1) has not yet been derived from the NS basic energy.

---

# 19. Continuous Campanato formulation

BMO can be defined by mean oscillation:

$$
\boxed{
\|f\|_{\mathrm{BMO}}
=
\sup_{x_0,r>0}
\frac1{|B_r|}
\int_{B_r(x_0)}
|f-f_{B_r}|dx.
}
\tag{19.1}
$$

Therefore, the endpoint of this round can be completely formulated using a continuous radius:

$$
r>0
$$

for its study.

For the near field,

the sufficient carrier is:

$$
\boxed{
\mathfrak D_{u,C}^{\mathrm{BMO}}(\ell)
=
\int_0^\ell
\frac{
\omega_{u,\infty}(r)
\omega_{C,\infty}(r)
}{
r^2
}
dr.
}
\tag{19.2}
$$

while the far field is a nonsingular Campanato oscillation problem.

No Littlewood–Paley dyadic shell is needed.

---

# 20. Critical endpoint remains logarithmic

If:

$$
\omega_u(r)\omega_C(r)
=
O(r),
$$

then:

$$
\boxed{
\mathfrak D_{u,C}^{\mathrm{BMO}}
\sim
\int_0^\ell
\frac{dr}{r}
}
\tag{20.1}
$$

remains logarithmically divergent.

Therefore, the Hardy–BMO route does not miraculously remove the endpoint log of Round 39.

It replaces:

$$
\boxed{
\text{Pair-Dini }(u,q)
}
$$

with:

$$
\boxed{
\text{Campanato-Dini }(u,C).
}
$$

---

# 21. Route comparison

Currently, the transport–Riesz endpoint has three Pure-C representations:

## R38 — primal triple increment

$$
\boxed{
\delta u
\,
\delta E
\,
\delta q,
\qquad
s_u+s_E+s_q=1.
}
$$

## R39 — defect-viscosity Pair-Dini

$$
\boxed{
\nabla E
\quad+\quad
\int
\omega_u\omega_q
\,dr/r.
}
$$

## R40 — Hardy–BMO dual

$$
\boxed{
q\in\mathcal H^1
\quad+\quad
[u\cdot\nabla,\mathcal T_0^\ast]C
\in\mathrm{BMO}.
}
$$

and the local BMO commutator has the:

$$
\boxed{
s_u+s_C=1
}
$$

critical endpoint.

Therefore, all three representations stop at the same total-derivative criticality.

---

# 22. Representation-stable endpoint core

Round 39 previously determined:

$$
\text{Hardy cancellation}
\neq
\text{automatic Dini}.
$$

Round 40 is now more precise:

$$
\boxed{
\text{Hardy cancellation}
\Rightarrow
\text{source side energy-level closure},
}
$$

but:

$$
\boxed{
\text{the missing critical derivative is transferred intact to the BMO partner}.
}
$$

Therefore, the endpoint obstruction is once again representation-stable.

---

# 23. STOP-C44 — Hardy–BMO Transfer / Two-Increment BMO Endpoint Gap

$$
\boxed{
\begin{aligned}
\text{layer}
&=
\mathrm{Hardy\text{-}BMO\ dual\ commutator},
\\
q
&\in
\mathcal H^1,
\\
\|q\|_{\mathcal H^1}
&\lesssim
\|\nabla u\|_2^2,
\\
\text{pressure self component}
&=
0,
\\
\text{dual target}
&=
\mathcal A_C
=
[D_u,\mathcal T_0^\ast]C,
\\
\text{exact kernel}
&=
\delta u
\times
\delta C
\times
\nabla K_0,
\\
\text{Hardy side}
&=
\mathrm{energy\text{-}chargeable},
\\
\text{standard CRW}
&=
L^p\to L^p
\text{ target, not BMO target},
\\
\text{two-field criticality}
&=
s_u+s_C=1,
\\
\text{endpoint}
&=
\mathrm{Campanato/Dini\ logarithmic\ barrier},
\\
\text{CRW fallback}
&\to
\mathrm{higher\text{-}gradient\ Round\ 05},
\\
\text{missing}
&=
\mathrm{unconditional\ BMO/Campanato\ control
of\ the\ special\ cofactor\ transport\ commutator},
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
\textbf{STOP-C44:
Hardy–BMO Transfer / Two-Increment BMO Endpoint Gap}.
}
$$

---

# 24. 24/72 Ledger — Round 40

| Step | object | $B$ | $U$ | $O$ | $L$ | status |
|---|---|---|---|---|---|---|
| C606 | Hardy pressure source | $\mathsf C$ | div–curl compensation | scalar | $\mathsf F$ | STANDARD |
| C607 | cofactor dual reduction | $\mathsf C$ | self-null duality | targeted | $\mathsf F$ | EXACT |
| C608 | Hardy–BMO charging law | $\mathsf C$ | functional duality | scalar | $\mathsf F$ | PROVED conditionally |
| C609 | energy-weighted spacetime charge | $\mathsf C$ | NS energy | targeted | $\mathsf F$ | PROVED conditionally |
| C610 | CRW factorization | $\mathsf C$ | commutator algebra | relational | $\mathsf F$ | EXACT |
| C611 | standard CRW target mismatch | $\mathsf C$ | function-space map | targeted | $\mathsf F$ | IDENTIFIED |
| C612 | dual two-increment identity | $\mathsf C$ | singular integral | relational | $\mathsf F$ | EXACT |
| C613 | Hardy absorbs source increment | $\mathsf C$ | dual representation | $\mathsf X$ | $\mathsf F$ | IDENTIFIED |
| C614 | local BMO Dini carrier | $\mathsf C$ | continuous modulus | scalar | $\mathsf F$ | FORM |
| C615 | two-field derivative threshold | $\mathsf C$ | Hölder/Campanato | targeted | $\mathsf F$ | PROVED |
| C616 | exact critical scaling | $\mathsf C$ | scaling | scalar | $\mathsf F$ | PROVED |
| C617 | cofactor-to-strain modulus return | $\mathsf C$ | tensor algebra | relational | $\mathsf F$ | EXACT |
| C618 | Hardy spacetime energy budget | $\mathsf C$ | energy dissipation | scalar | $\mathsf F$ | PROVED |
| C619 | standard CRW $L^{3/2}$ fallback | $\mathsf C$ | harmonic analysis | targeted | $\mathsf F$ | CONDITIONAL |
| C620 | higher-gradient fallback estimate | $\mathsf C$ | Sobolev/Hodge | scalar | $\mathsf F$ | PROVED |
| C621 | conditional Hardy–BMO closure | $\mathsf C$ | defect energy | targeted | $\mathsf F$ | CONDITIONAL |
| C622 | unconditional special BMO commutator control | $\mathsf C$ | coupled NS | targeted | $\mathsf F$ | OPEN / STOP-C44 |

---

# 25. Continuous-versus-discrete status

This round uses:

- real Hardy space;
- BMO / Campanato mean oscillation;
- continuous balls:
  $$
  B_r(x_0);
  $$
- continuous translation modulus;
- continuous singular-integral kernel.

Does not use:

- atoms as a proof substrate necessity;
- dyadic BMO grid;
- frequency shell index;
- discrete commutator states.

Even if Hardy atomic language is available, it is not the essential representation of this round;

all core conditions have been written in continuous div–curl / Campanato form.

Therefore:

$$
\boxed{
T_{\mathsf C\to\mathsf D}
=
\text{NOT YET REACHED}.
}
$$

---

# 26. Strongest results of Round 40

## R40-A — dual cofactor reduction

$$
\boxed{
\langle
E,
[D_u,\mathcal T_0]q
\rangle
=
\langle
[D_u,\mathcal T_0^\ast]C,
q
\rangle.
}
$$

## R40-B — energy-level Hardy charging

$$
\boxed{
|\mathcal J_{\rm TR}|
\lesssim
\|\nabla u\|_2^2
\|
[D_u,\mathcal T_0^\ast]C
\|_{\mathrm{BMO}}.
}
$$

## R40-C — exact two-increment dual commutator

$$
\boxed{
\mathcal A_C(x)
=
\operatorname{p.v.}
\int
[
u(x)-u(y)
]
\cdot
\nabla K_0(x-y)
:
[
C(y)-C(x)
]
dy.
}
$$

## R40-D — Hardy-absorbed critical endpoint

$$
\boxed{
s_u+s_C=1.
}
$$

Hardy compensation removes the explicit $q$ increment but transfers the critical derivative to the BMO partner.

## R40-E — standard CRW fallback does not solve the target problem

$$
\boxed{
\|\mathcal A_C\|_p
\lesssim
\|u\|_{\mathrm{BMO}}
\|\nabla C\|_p
}
$$

is useful, but it is not the required:

$$
\mathcal A_C\in\mathrm{BMO}.
$$

---

# 27. Next round — Special Cofactor Commutator / Campanato Cancellation

Round 40 shows that generic CRW theory does not directly give the BMO target we need.

But:

$$
C
=
S^2-\frac13|S|^2I
$$

is not an arbitrary tensor.

The next round will directly study this special structure:

1. Fully expand:
   $$
   \delta C
   $$
   into:
   $$
   (S_x+S_y)\delta S;
   $$

2. Split:
   $$
   \delta u
   $$
   into longitudinal / transverse increments;

3. Utilize:
   $$
   \nabla\cdot u=0,
   \qquad
   \operatorname{tr}S=0;
   $$

4. Check whether the angular mean-zero kernel and cofactor trace-free structure further cancel the leading affine increment;

5. If the leading affine term cancels, the critical threshold might, starting from:
   $$
   s_u+s_C=1
   $$
   obtain an extra modulus gain;

6. If the affine term does not vanish, construct a divergence-free affine/quadratic witness to formally prove the endpoint is sharp;

7. Study the Campanato mean oscillation, without requiring a pointwise $L^\infty$ modulus;

8. Maintain continuous balls / radii, without using dyadic BMO grids.

---

# 28. External primary-source anchors

1. Dong Li, Xiaoyi Zhang, *A regularity upgrade of pressure*, arXiv:2106.11852.
   - Incompressibility and the div–curl structure provide a Hardy-space regularity upgrade for the pressure/pressure source, and demonstrate certain endpoint regularity failures.

2. Elias Hess-Childs, Matthew Rosenzweig, Sylvia Serfaty, *Another look at regularity in transport-commutator estimates*, arXiv:2601.02326.
   - For broad Riesz transport commutators, the commonly used Lipschitz-gradient control generally cannot be directly relaxed to BMO; this illustrates that the generic BMO wishful estimate does not hold.

3. Enno Lenzmann, Armin Schikorra, *Sharp commutator estimates via harmonic extensions*, arXiv:1609.08547.
   - Coifman–Rochberg–Weiss, Riesz, and other commutator estimates can be derived from cancellation / integration-by-parts structures, providing the harmonic-analysis background for this round's CRW factorization and special-structure search.

4. Irina Holmes, Michael T. Lacey, Brett D. Wick, *Commutators in the Two-Weight Setting*, arXiv:1506.05747.
   - A modern primary-source extension of the classical Coifman–Rochberg–Weiss result: the BMO symbol controls the $L^p$ boundedness of the Riesz commutator.

The dual cofactor reduction, Hardy–BMO charging law, dual two-increment identity, two-field critical scaling, and higher-gradient CRW fallback in this round are all directly derived in this document.

---

# 29. Commit state

$$
\boxed{
\begin{aligned}
\text{Route}
&=
\mathrm{Pure\ Continuous\ Hardy\text{-}BMO\ Dual\ Commutator},
\\
\text{Essential }\mathsf C\to\mathsf D
&=
\mathrm{Not\ reached},
\\
\text{Pressure source}
&=
\mathcal H^1\text{ at energy/enstrophy level},
\\
\text{Pressure self commutator}
&=
0,
\\
\text{Dual target}
&=
[D_u,\mathcal T_0^\ast]C_S^0,
\\
\text{Hardy side}
&=
\mathrm{energy\text{-}chargeable},
\\
\text{BMO side}
&=
\mathrm{critical\ two\text{-}increment\ problem},
\\
\text{Standard CRW}
&=
\mathrm{wrong\ target\ space\ for\ direct\ closure},
\\
\text{Critical threshold}
&=
s_u+s_C=1,
\\
\text{STOP-C44}
&=
\mathrm{Hardy\text{-}BMO\ Transfer/Two\text{-}Increment\ BMO\ Endpoint\ Gap},
\\
\text{Next}
&=
\mathrm{Special\ Cofactor\ Commutator/Campanato\ Cancellation}.
\end{aligned}
}
$$