---
title: "Navier–Stokes Forest Coercive Budget Program 03: Signed Pressure–Flux Work, Variable-Radius Telescoping, Slow-Scale Critical Lift, Filter-Switch Defects and Model-Cone Recurrence"
short_title: "NS-FCBP 03"
series: "Navier–Stokes Forest Coercive Budget Program"
cycle: "VI"
version: "v0.1"
date: "2026-08-16"
author: "Neo.K / EveMissLab"
language: "en"
status: "Signed-work critical-lift attempt / slow-scale telescope breakthrough / moving-filter reduction"
epistemic_status: "Generalizes the exact pressure-flux endpoint telescope algebra from geometric radii to arbitrary strictly decreasing radii for one common coarse package. This internal Variable-Radius Pressure–Flux Telescope shows that the summable scale weight in the published geometric theorem is not intrinsic to the telescope. Choosing r_k=r_0(k+1)^(-beta), 1/2<beta<=1, gives finite total parabolic time but a divergent telescope weight sum, producing a genuine non-summable Slow-Scale Critical-Lift Window. A conditional depletion theorem shows that uniformly detected forward work on a set of slabs with divergent weighted density contradicts finite weighted leakage/backscatter. The paper then identifies the main compatibility problem: a single fixed physical filter preserves exact telescoping but loses scale-relative resolution as r_k->0; scale-relative moving filters preserve critical resolution but break exact endpoint telescoping. An exact Moving-Filter Telescope is proved with an explicit positive filter-switch defect. A chain-dependent finest-scale common-filter strategy removes switch defects but replaces them by uniform-in-chain-length observability/leakage/backscatter requirements. A scale-critical Model-Cone Growth Packet is also proved from the Miller strain balance. The remaining Critical Lift is reduced to filter-switch or uniform common-filter packing, weighted backscatter/leakage closure, and active-work observability on a non-summable set of slow slabs. Forest Coercive Budget, Finite Forest Obstruction, atomic CN3, and Navier-Stokes regularity remain OPEN."
canonical_source: "UTF-8 Markdown"
---

# Navier–Stokes Forest Coercive Budget Program 03

# Signed Pressure–Flux Work, Variable-Radius Telescoping, Slow-Scale Critical Lift, Filter-Switch Defects and Model-Cone Recurrence

## 0. Document Positioning

FCBP-02 proved that the filtered route has a complete conditional compiler but still lacks global critical packing.

The dominant barriers were:

- comparable-annulus signed packing;
- weighted backscatter;
- scale-critical commutator recurrence;
- observability.

The pressure--flux work framework is attractive because it already preserves signs and gives an exact endpoint telescope.

The published theorem uses geometric radii:

$$
r_k=\theta^k r_0.
$$

The first question is:

> Is the resulting summable weight $w_k=r_k/r_0$ intrinsic to the PDE telescope, or only to the chosen geometric schedule?

The answer is:

$$
\boxed{
\textbf{it is not intrinsic to the telescope}.
}
$$

This creates the first actual non-summable schedule inside the FCBP architecture.

---

# 1. External fixed-chain pressure--flux ledger

Fix one physical coarse length:

$$
\ell>0.
$$

Let:

$$
U^\ell=S_\ell u,
\qquad
P^\ell=S_\ell p,
$$

$$
R^\ell
=
S_\ell(u\otimes u)
-
U^\ell\otimes U^\ell,
$$

and:

$$
\Pi^\ell
=
-
R^\ell:\nabla U^\ell.
$$

Define the signed combined work distribution:

$$
\boxed{
G^\ell
=
\Pi^\ell
+
\nabla\cdot(P^\ell U^\ell).
}
$$

The external local coarse energy identity is valid for an arbitrary time interval:

$$
I=(t_-,t_+),
$$

radius:

$$
r>0,
$$

and admissible nonnegative weight:

$$
\phi:
$$

$$
\boxed{
\mathcal W_{I,r}[\phi]
+
\mathcal D_{I,r}[\phi]
=
r^{-1}
\left(
K_\phi^\ell(t_-)
-
K_\phi^\ell(t_+)
\right)
+
\mathcal L_{I,r}[\phi].
}
$$

### Status

$$
\boxed{
\mathrm{EXTERNAL/PROVED}.
}
$$

---

# 2. Published geometric-chain theorem

The external theorem fixes:

$$
r_k=\theta^kr_0,
\qquad
0<\theta<1,
$$

and adjacent slabs:

$$
\tau_{k+1}-\tau_k=r_k^2.
$$

The spatial cutoffs:

$$
\chi_k(x)
=
\chi
\left(
\frac{x-x_0}{r_k}
\right)
$$

satisfy:

$$
\boxed{
\chi_{k+1}\le\chi_k.
}
$$

The active weights have common endpoint traces:

$$
\boxed{
\widehat\phi_k(\cdot,\tau_k)
=
\widehat\phi_k(\cdot,\tau_{k+1})
=
\chi_k.
}
$$

With:

$$
w_k=\frac{r_k}{r_0},
$$

the external pressure--flux telescope gives:

$$
\boxed{
\sum_{k=0}^{N-1}
w_k
(
\mathcal W_k^+
+
\mathcal D_k
)
\le
\mathcal E_0^-
+
\sum_{k=0}^{N-1}
w_k|\mathcal L_k|
+
\sum_{k=0}^{N-1}
w_k\mathcal W_k^-.
}
$$

### Status

$$
\boxed{
\mathrm{EXTERNAL/PROVED}.
}
$$

---

# 3. What the external proof actually uses

The endpoint part of the telescope is:

$$
\sum_{k=0}^{N-1}
w_k
(
\mathcal E_k^-
-
\mathcal E_k^+
).
$$

The proof uses:

$$
\boxed{
w_kr_k^{-1}
=
r_0^{-1},
}
$$

and:

$$
\boxed{
\chi_k\le\chi_{k-1}.
}
$$

The constant geometric ratio:

$$
r_{k+1}/r_k=\theta
$$

does not enter this endpoint cancellation algebra.

This observation permits the following internal extension.

---

# 4. Arbitrary decreasing radii

Let:

$$
\boxed{
r_0>r_1>\cdots>r_N>0
}
$$

be arbitrary.

Choose adjacent times:

$$
\boxed{
\tau_{k+1}-\tau_k=r_k^2.
}
$$

Define:

$$
\chi_k(x)
=
\chi
\left(
\frac{x-x_0}{r_k}
\right),
$$

with the same radial nonincreasing reference cutoff.

Then:

$$
\boxed{
\chi_k\le\chi_{k-1}.
}
$$

Use one common coarse package:

$$
(U^\ell,P^\ell,R^\ell)
$$

for every slab.

---

# 5. CIV/VI-3.1 — Variable-Radius Pressure–Flux Telescope

## Theorem 5.1

Suppose every slab carries a nonnegative weight:

$$
\widehat\phi_k
$$

with endpoint traces:

$$
\widehat\phi_k(\cdot,\tau_k)
=
\widehat\phi_k(\cdot,\tau_{k+1})
=
\chi_k.
$$

Set:

$$
\boxed{
w_k=\frac{r_k}{r_0}.
}
$$

Then:

$$
\boxed{
\sum_{k=0}^{N-1}
w_k
(
\mathcal E_k^-
-
\mathcal E_k^+
)
\le
\mathcal E_0^-,
}
$$

and:

$$
\boxed{
\sum_{k=0}^{N-1}
w_k
(
\mathcal W_k^+
+
\mathcal D_k
)
\le
\mathcal E_0^-
+
\sum_{k=0}^{N-1}
w_k|\mathcal L_k|
+
\sum_{k=0}^{N-1}
w_k\mathcal W_k^-.
}
$$

### Proof

Since:

$$
w_kr_k^{-1}=r_0^{-1},
$$

$$
\sum_{k=0}^{N-1}
w_k
(
\mathcal E_k^-
-
\mathcal E_k^+
)
=
\frac1{r_0}
\sum_{k=0}^{N-1}
\left[
K_{\chi_k}^{\ell}(\tau_k)
-
K_{\chi_k}^{\ell}(\tau_{k+1})
\right].
$$

Rearrange:

$$
=
\frac1{r_0}
\left[
K_{\chi_0}^{\ell}(\tau_0)
-
K_{\chi_{N-1}}^{\ell}(\tau_N)
+
\sum_{k=1}^{N-1}
\left(
K_{\chi_k}^{\ell}(\tau_k)
-
K_{\chi_{k-1}}^{\ell}(\tau_k)
\right)
\right].
$$

The terminal energy is nonnegative.

For every interface:

$$
\chi_k\le\chi_{k-1},
$$

hence:

$$
K_{\chi_k}^{\ell}(\tau_k)
-
K_{\chi_{k-1}}^{\ell}(\tau_k)
\le0.
$$

This proves the endpoint inequality.

Apply the local coarse-energy identity slab by slab, multiply by:

$$
w_k,
$$

sum, and separate:

$$
\mathcal W_k
=
\mathcal W_k^+
-
\mathcal W_k^-.
$$

$\square$

---

# 6. Importance of Theorem 5.1

The pressure--flux telescope itself does **not** require geometric radii.

Therefore the summability:

$$
\sum_k
\frac{r_k}{r_0}
<
\infty
$$

in the published geometric chain is not an unavoidable consequence of the endpoint cancellation.

The radius schedule is a genuine FCBP degree of freedom.

---

# 7. Slow-scale schedules

Let:

$$
\boxed{
r_k
=
r_0
(k+1)^{-\beta},
}
$$

with:

$$
\boxed{
\frac12<\beta\le1.
}
$$

Then:

$$
\boxed{
\sum_{k=0}^{\infty}
r_k^2
=
r_0^2
\sum_{k=0}^{\infty}
(k+1)^{-2\beta}
<
\infty.
}
$$

Therefore one may choose:

$$
\tau_{k+1}-\tau_k=r_k^2
$$

so that:

$$
\boxed{
\tau_k\uparrow T_\infty<\infty.
}
$$

By selecting the initial time appropriately, the accumulation time may be placed at:

$$
T_\ast.
$$

---

# 8. Non-summable telescope weights

For the same schedule:

$$
w_k
=
\frac{r_k}{r_0}
=
(k+1)^{-\beta}.
$$

Since:

$$
\beta\le1,
$$

$$
\boxed{
\sum_{k=0}^{\infty}
w_k
=
\infty.
}
$$

Thus the same exact endpoint telescope admits:

- finite total physical parabolic time;
- non-summable scale weights.

---

# 9. CIV/VI-3.2 — Slow-Scale Critical-Lift Window

## Theorem 9.1

For every:

$$
\frac12<\beta\le1,
$$

there exists a decreasing parabolic scale schedule with:

$$
\boxed{
\sum_k
(\tau_{k+1}-\tau_k)
<
\infty
}
$$

but:

$$
\boxed{
\sum_k
w_k
=
\infty.
}
$$

Therefore the FCBP-01 Summable-Weight No-Go does not apply to the variable-radius pressure--flux telescope on this schedule.

### Meaning

A non-summable scale weight can be generated by the **geometry of the radius schedule itself**, without changing the local PDE identity.

$\square$

---

# 10. Borderline logarithmic schedule

The canonical borderline choice is:

$$
\boxed{
\beta=1.
}
$$

Then:

$$
r_k
=
\frac{r_0}{k+1},
$$

$$
\sum_k
r_k^2
<
\infty,
$$

but:

$$
\boxed{
\sum_k
w_k
=
\sum_k
\frac1{k+1}
=
\infty.
}
$$

This produces exactly the logarithmic non-summable weight anticipated in FCBP-01.

---

# 11. Active work extraction

The external finite-chain work theorem gives, on every selected slab:

$$
\boxed{
|\mathcal W_k|
\ge
c_k
\mathfrak A_k(G^\ell).
}
$$

The sign is split into:

$$
\mathcal W_k^+
$$

and:

$$
\mathcal W_k^-.
$$

The external theorem does not claim:

- uniform:
  $$
  c_k;
  $$
- small backscatter;
- summable leakage;
- moving-window observability.

All remain separate obligations.

---

# 12. Weighted active density

For a forward active index set:

$$
\mathcal I_+,
$$

define:

$$
\boxed{
\mathfrak D_{\rm act}(N)
=
\sum_{
\substack{
k<N\\
k\in\mathcal I_+
}
}
w_k
c_k
\mathfrak A_k(G^\ell).
}
$$

A non-summable active set means:

$$
\boxed{
\mathfrak D_{\rm act}(N)
\to\infty.
}
$$

---

# 13. CIV/VI-3.3 — Non-Summable Work-Depletion Criterion

## Theorem 13.1

Assume a variable-radius finite chain satisfies:

$$
\sup_N
\left[
\mathcal E_0^-
+
\sum_{k<N}
w_k|\mathcal L_k|
+
\sum_{k<N}
w_k\mathcal W_k^-
\right]
<
\infty.
$$

Then:

$$
\boxed{
\sup_N
\mathfrak D_{\rm act}(N)
<
\infty.
}
$$

Consequently, a forward active family satisfying:

$$
\boxed{
\mathfrak D_{\rm act}(N)\to\infty
}
$$

is impossible.

### Special case

If:

$$
c_k
\mathfrak A_k(G^\ell)
\ge
a_0>0
$$

on:

$$
\mathcal I_+,
$$

then it suffices that:

$$
\boxed{
\sum_{k\in\mathcal I_+}
w_k
=
\infty.
}
$$

$\square$

---

# 14. Sign is not an error term

The external pressure--flux theorem explicitly warns that a forward-only subchain does not telescope.

Negative intermediate work is part of the cancellation mechanism.

Therefore:

$$
\boxed{
\text{backscatter must remain on the paid side of the ledger}.
}
$$

The Slow-Scale Lift does not require an **unweighted** backscatter bound.

It requires finiteness of the same non-summably weighted backscatter appearing in the telescope:

$$
\boxed{
\sum_k
w_k
\mathcal W_k^-
<
\infty.
}
$$

This is a more natural signed target than the unweighted backscatter condition used in the FCBP-02 algebraic lemma.

---

# 15. Weighted Backscatter Barrier

The external theorem does not provide:

$$
\sum_k
w_k\mathcal W_k^-
<
\infty
$$

as:

$$
N\to\infty.
$$

It only records backscatter explicitly on the right-hand side.

Thus:

$$
\boxed{
\textbf{weighted backscatter closure}
}
$$

remains an open PDE obligation even after the slow-scale schedule produces non-summable weights.

---

# 16. Common physical filter

The pressure--flux chain uses one fixed:

$$
\boxed{
\ell>0
}
$$

for every slab.

This is essential to the exact endpoint telescope because:

$$
K_{\chi_k}^{\ell}
$$

at adjacent slabs is computed from the same resolved field:

$$
U^\ell.
$$

---

# 17. Scale-relative resolution

The external coarse CKN quantities:

$$
\Psi^\ell(r),
\qquad
\Omega^\ell(r)
$$

are Navier--Stokes scale invariant when:

$$
\boxed{
\ell/r
}
$$

is kept fixed.

The filtered-vorticity coercive module likewise works in the scale-relative regime:

$$
\boxed{
\ell\lesssim r.
}
$$

For a single fixed physical:

$$
\ell>0
$$

and:

$$
r_k\to0,
$$

$$
\boxed{
\ell/r_k\to\infty.
}
$$

Thus one fixed infinite-chain filter eventually ceases to be a scale-relative fine filter.

---

# 18. CIV/VI-3.4 — Common-Filter / Critical-Resolution Barrier

## Theorem 18.1

A single fixed:

$$
\ell>0
$$

cannot satisfy:

$$
\ell/r_k
\le
\rho
$$

for all sufficiently large:

$$
k
$$

along any chain with:

$$
r_k\to0.
$$

Hence:

$$
\boxed{
\text{one common physical filter}
}
$$

and:

$$
\boxed{
\text{uniform scale-relative filtering on an infinite fine-scale chain}
}
$$

cannot hold simultaneously.

$\square$

### Safety

The pressure--flux local identity itself remains valid.

What fails is the scale-relative interpretation/compatibility with the filtered critical modules.

---

# 19. Moving relative filters

Set:

$$
\boxed{
\ell_k
=
\sigma r_k.
}
$$

For each slab, define its own coarse package:

$$
U_k
=
S_{\ell_k}u,
$$

$$
P_k
=
S_{\ell_k}p,
$$

$$
R_k
=
S_{\ell_k}(u\otimes u)
-
U_k\otimes U_k.
$$

The local coarse energy identity remains valid separately on every slab.

The endpoint fields, however, now change with:

$$
k.
$$

---

# 20. Moving-filter endpoint energy

Define:

$$
\boxed{
K_{\chi}^{(k)}(t)
=
\frac12
\int
|U_k(x,t)|^2
\chi(x)dx.
}
$$

Then:

$$
\mathcal E_k^-
=
r_k^{-1}
K_{\chi_k}^{(k)}(\tau_k),
$$

and:

$$
\mathcal E_k^+
=
r_k^{-1}
K_{\chi_k}^{(k)}(\tau_{k+1}).
$$

---

# 21. Filter-switch defect

At interface:

$$
\tau_k,
$$

define:

$$
\boxed{
\Delta_k^{filt}
=
K_{\chi_{k-1}}^{(k)}(\tau_k)
-
K_{\chi_{k-1}}^{(k-1)}(\tau_k).
}
$$

This measures the resolved localized kinetic-energy change caused only by switching:

$$
\ell_{k-1}
\to
\ell_k
$$

while keeping the larger spatial cutoff fixed.

---

# 22. CIV/VI-3.5 — Moving-Filter Telescope

## Theorem 22.1

With:

$$
w_k=r_k/r_0,
$$

the moving-filter endpoint sum satisfies:

$$
\boxed{
\sum_{k=0}^{N-1}
w_k
(
\mathcal E_k^-
-
\mathcal E_k^+
)
\le
\mathcal E_0^-
+
\frac1{r_0}
\sum_{k=1}^{N-1}
[
\Delta_k^{filt}
]_+.
}
$$

Consequently:

$$
\boxed{
\begin{aligned}
\sum_{k=0}^{N-1}
w_k
(
\mathcal W_k^+
+
\mathcal D_k
)
\le\;&
\mathcal E_0^-
+
\sum_{k=0}^{N-1}
w_k|\mathcal L_k|
+
\sum_{k=0}^{N-1}
w_k\mathcal W_k^-
\\
&+
\frac1{r_0}
\sum_{k=1}^{N-1}
[
\Delta_k^{filt}
]_+.
\end{aligned}
}
$$

### Proof

Write:

$$
\sum_k
w_k
(
\mathcal E_k^-
-
\mathcal E_k^+
)
=
\frac1{r_0}
\sum_k
\left[
K_{\chi_k}^{(k)}(\tau_k)
-
K_{\chi_k}^{(k)}(\tau_{k+1})
\right].
$$

At interface:

$$
\tau_k,
$$

split:

$$
K_{\chi_k}^{(k)}
-
K_{\chi_{k-1}}^{(k-1)}
=
\left(
K_{\chi_k}^{(k)}
-
K_{\chi_{k-1}}^{(k)}
\right)
+
\left(
K_{\chi_{k-1}}^{(k)}
-
K_{\chi_{k-1}}^{(k-1)}
\right).
$$

The first term is nonpositive because:

$$
\chi_k\le\chi_{k-1}.
$$

The second is:

$$
\Delta_k^{filt}.
$$

Drop the nonnegative terminal energy and retain the positive part of the switch defect.

Then use the slabwise local energy identities.

$\square$

---

# 23. Filter-Switch Packing Problem

A scale-relative moving-filter Critical Lift therefore requires:

$$
\boxed{
\sum_k
[
\Delta_k^{filt}
]_+
<
\infty
}
$$

or a sufficiently weak non-summable-weight-compatible substitute.

Define:

$$
\boxed{
\textbf{FSP — Filter-Switch Packing}.
}
$$

No such universal theorem is proved here.

---

# 24. No automatic sign

Cutoff nesting controls:

$$
K_{\chi_k}^{(k)}
-
K_{\chi_{k-1}}^{(k)}
\le0.
$$

It does **not** control:

$$
\Delta_k^{filt},
$$

because two different resolved fields are compared.

Therefore FSP is a genuine new endpoint compatibility problem, not a notational artifact.

---

# 25. Slow filter ratios

On the power-law slow schedule:

$$
r_k=r_0(k+1)^{-\beta},
$$

and:

$$
\ell_k=\sigma r_k,
$$

one has:

$$
\boxed{
\frac{\ell_k}{\ell_{k-1}}
=
\left(
\frac{k}{k+1}
\right)^{\beta}
=
1-\frac{\beta}{k}
+
O(k^{-2}).
}
$$

Thus successive filter switches become infinitesimal in logarithmic scale.

This suggests a bounded-variation-in-filter route to FSP.

No such localized BV theorem is currently established in the FCBP ledger.

---

# 26. Finest-scale common-filter strategy

There is a second way to avoid the moving-filter defect.

For each finite chain of length:

$$
N,
$$

choose one common filter:

$$
\boxed{
\ell^{(N)}
=
\sigma r_N.
}
$$

Then for every:

$$
k\le N,
$$

$$
\boxed{
\frac{\ell^{(N)}}{r_k}
\le
\sigma.
}
$$

The chain therefore keeps a fine common filter while preserving the exact fixed-filter telescope.

No filter-switch term appears inside that finite chain.

---

# 27. Price of the finest-scale common filter

The coarse package now depends on:

$$
N:
$$

$$
G^{\ell^{(N)}}.
$$

To pass:

$$
N\to\infty,
$$

one needs uniform control of:

1. active-work observability constants;
2. selected detector constants:
   $$
   c_k;
   $$
3. weighted leakage;
4. weighted backscatter;
5. the subfilter residual/coarse-resolution split.

Thus the filter-switch problem is replaced by a **uniform-in-chain-length coarse-observability problem**.

---

# 28. Interaction with filtered stretching

The filtered near-field estimate contains a lower-order factor involving:

$$
(r/\ell)^5.
$$

With:

$$
\ell^{(N)}
=
\sigma r_N,
$$

on an earlier slab:

$$
k<N,
$$

$$
\boxed{
\left(
\frac{r_k}{\ell^{(N)}}
\right)^5
=
\sigma^{-5}
\left(
\frac{r_k}{r_N}
\right)^5.
}
$$

This can become very large as:

$$
N-k
$$

grows.

Therefore the finest-scale common-filter strategy preserves pressure--flux telescoping but does not automatically preserve uniform filtered near-field coercivity across the whole slow chain.

---

# 29. Three filter strategies

The critical-lift problem now has three precise implementations.

### Strategy A — fixed infinite-chain filter

Exact telescope:

$$
\boxed{\mathrm{YES}}.
$$

Uniform scale-relative resolution:

$$
\boxed{\mathrm{NO}}.
$$

### Strategy B — moving relative filters

Scale-relative resolution:

$$
\boxed{\mathrm{YES}}.
$$

Exact telescope:

$$
\boxed{
\text{YES modulo FSP}.
}
$$

### Strategy C — finite-chain finest-scale common filter

Exact finite-chain telescope:

$$
\boxed{\mathrm{YES}}.
$$

Fine-filter condition:

$$
\boxed{\mathrm{YES}}.
$$

Uniform:

$$
N\to\infty
$$

observability/packing:

$$
\boxed{\mathrm{OPEN}}.
$$

---

# 30. CKN visibility and observability

The external coarse-resolution theorem gives:

$$
\boxed{
\Psi(r)
\le
4\Psi^\ell(r)
+
4\Omega^\ell(r).
}
$$

Thus a CKN-bad scale satisfies:

$$
\boxed{
\text{COARSE-VISIBLE}
\vee
\text{SUBFILTER-RESIDUAL}.
}
$$

But even a large coarse quantity:

$$
\Psi^\ell
$$

does not automatically imply a large finite-dimensional signed pressure--flux detector.

The external work explicitly identifies this as a separate coarse observability problem.

---

# 31. Active-work observability bridge

Define:

$$
\boxed{
\textbf{AOB — Active Observability Bridge}
}
$$

as a theorem of the form:

$$
\boxed{
\Psi^\ell(r_k)
\ge
c_0\varepsilon_0
\Longrightarrow
c_k
\mathfrak A_k(G^\ell)
\ge
a_0
}
$$

uniformly on an admissible horizon class.

Current status:

$$
\boxed{
\mathrm{OPEN}.
}
$$

The external pressure--flux theorem is conditional on precisely such a bridge.

---

# 32. Slow-schedule active density

Even with AOB, a non-summable telescope requires active work on a sufficiently large set of slabs.

Define:

$$
\boxed{
\mathcal I_{\rm act}
=
\left\{
k:
c_k
\mathfrak A_k(G^\ell)
\ge
a_0
\right\}.
}
$$

The required weighted density is:

$$
\boxed{
\sum_{k\in\mathcal I_{\rm act}}
w_k
=
\infty.
}
$$

A sparse active set may have:

$$
\sum_{k\in\mathcal I_{\rm act}}
w_k
<
\infty
$$

even though:

$$
\sum_kw_k=\infty.
$$

Thus **schedule non-summability is necessary but not sufficient**.

---

# 33. Active-Slab Density Problem

Define:

$$
\boxed{
\textbf{ASD — Active-Slab Density}.
}
$$

> Prove that dangerous/residual-small horizon activity produces a set of forward detected work slabs with divergent slow-schedule weight, or else route the complementary slabs into backscatter, subfilter residual, commutator, or another critical recurrence branch.

Current status:

$$
\boxed{
\mathrm{OPEN}.
}
$$

---

# 34. Backscatter-compatible obstruction

The pressure--flux telescope already records negative work explicitly.

Therefore a slow-scale contradiction does not require:

$$
\sum_k
\mathcal W_k^-
<
\infty.
$$

It requires only the schedule-compatible condition:

$$
\boxed{
\sum_k
w_k
\mathcal W_k^-
<
\infty.
}
$$

This is weaker and better aligned with the signed PDE identity.

But it remains unproved.

---

# 35. Model-cone recurrence

Return to the Miller strain balance:

$$
\boxed{
\frac12
\frac d{dt}
\|S\|_{\dot H^1}^2
+
\|-\Delta S\|_2^2
=
-
\langle
\mathcal R_{SV},
-\Delta S
\rangle.
}
$$

Define:

$$
\boxed{
\chi_{SV}
=
\frac{
\|\mathcal R_{SV}\|_2
}{
\|-\Delta S\|_2
}.
}
$$

Then:

$$
\boxed{
\frac12
\frac d{dt}
\|S\|_{\dot H^1}^2
\le
(
\chi_{SV}-1
)
\|-\Delta S\|_2^2.
}
$$

---

# 36. CIV/VI-3.6 — Model-Cone Growth Packet

## Theorem 36.1

For:

$$
I=[a,b],
$$

$$
\boxed{
\|S(b)\|_{\dot H^1}^2
-
\|S(a)\|_{\dot H^1}^2
\le
2
\int_a^b
(
\chi_{SV}-1
)_+
\|-\Delta S\|_2^2dt.
}
$$

If:

$$
\boxed{
\|S(b)\|_{\dot H^1}^2
\ge
(1+\delta)
\|S(a)\|_{\dot H^1}^2,
}
$$

then:

$$
\boxed{
\frac{
2
}{
\|S(a)\|_{\dot H^1}^2
}
\int_a^b
(
\chi_{SV}-1
)_+
\|-\Delta S\|_2^2dt
\ge
\delta.
}
$$

The normalized packet is Navier--Stokes scale invariant.

$\square$

---

# 37. External model-cone necessity

Miller's external theorem states that a finite-time blow-up requires:

$$
\boxed{
\limsup_{t\uparrow T_\ast}
\chi_{SV}(t)
\ge1.
}
$$

Thus a hypothetical singular trajectory cannot remain uniformly inside a strictly subcritical model cone.

This supports model-cone excess as a critical recurrence coordinate.

It does not provide a universal finite sum of the packets in Theorem 36.1.

---

# 38. Model-cone role in FCBP

If pressure--flux active work repeatedly fails to be observable while dangerous strain growth persists, the model-cone ledger offers a second critical recurrence channel:

$$
\boxed{
\text{work-visible}
\vee
\text{model-cone excess recurrence}.
}
$$

A theorem connecting the two quantitatively is not yet proved.

---

# 39. Affine-jet versus pressure--flux work

Filtered far-field affine-jet stretching measures an enstrophy-production mechanism of the form:

$$
J\Omega\cdot\Omega.
$$

Pressure--flux work measures resolved kinetic-energy transfer:

$$
\Pi^\ell
+
\nabla\cdot(P^\ell U^\ell).
$$

There is no identity in the current external results equating these observables.

Therefore the FCBP-02 hoped-for direct bridge:

$$
\boxed{
\text{affine-jet stretching}
\Longrightarrow
\text{pressure--flux active work}
}
$$

remains open.

---

# 40. Affine-to-Pressure–Flux Observability Bridge

Define:

$$
\boxed{
\textbf{APF — Affine-to-Pressure--Flux Bridge}
}
$$

as any quantitative implication which converts persistent comparable-annulus signed affine stretching work into:

- active pressure--flux work;
- backscatter;
- subfilter residual;
- or another explicitly paid critical channel.

Current status:

$$
\boxed{
\mathrm{OPEN}.
}
$$

This is the correct cross-observable formulation.

---

# 41. Pressure–flux cancellation barrier

The external combined work is:

$$
\boxed{
\mathcal W
=
\mathcal F+\mathcal P,
}
$$

and the cancellation amount:

$$
\boxed{
\mathcal C^{PF}
=
|\mathcal F|
+
|\mathcal P|
-
|\mathcal W|
\ge0.
}
$$

Therefore large separate flux and pressure activity can be almost invisible to the signed combined detector.

This is one explicit reason AOB/APF cannot be assumed automatically.

---

# 42. Harmonic pressure is physical

The external pressure decomposition writes:

$$
P=P^a+P^h,
$$

with:

$$
P^h
$$

harmonic in the interior.

Only the spatially constant harmonic mode is a gauge.

Higher harmonic polynomial modes perform genuine localized pressure work and must remain in the signed ledger.

Thus harmonic pressure cannot be discarded to manufacture observability.

---

# 43. Main positive breakthrough of FCBP-03

The FCBP-01 summable-weight barrier is **not intrinsic to the pressure--flux telescope**.

Theorem 9.1 provides an exact slow-scale schedule with:

$$
\boxed{
\sum_k
r_k^2
<
\infty,
}
$$

but:

$$
\boxed{
\sum_k
\frac{r_k}{r_0}
=
\infty.
}
$$

This is the first genuine non-summable telescope weight produced inside FCBP.

---

# 44. Why Critical Lift is still open

To convert the schedule breakthrough into a Forest Coercive Budget, one still needs one of the following complete packages.

## Moving-filter package

1. AOB / active-slab density;
2. weighted leakage closure;
3. weighted backscatter closure;
4. Filter-Switch Packing.

## Finest-common-filter package

1. uniform-in-$N$ AOB;
2. uniform weighted leakage/backscatter;
3. uniform residual/coarse-resolution control;
4. compatibility with the filtered residual branch.

Neither package is currently proved.

---

# 45. Slow-Scale Critical-Lift Compiler

## Theorem 45.1

Let:

$$
r_k=r_0(k+1)^{-\beta},
\qquad
\frac12<\beta\le1.
$$

Assume a fixed-filter or moving-filter pressure--flux chain satisfies:

### SL-1 — active density

$$
\sum_{
k\in\mathcal I_+
}
w_k
c_k
\mathfrak A_k
=
\infty.
$$

### SL-2 — paid residual finiteness

$$
\sum_k
w_k
|\mathcal L_k|
+
\sum_k
w_k
\mathcal W_k^-
<
\infty.
$$

### SL-3 — filter compatibility

For a fixed-filter chain there is no switch term.

For a moving-filter chain:

$$
\sum_k
[
\Delta_k^{filt}
]_+
<
\infty.
$$

Then the chain is impossible.

### Proof

Apply Theorem 5.1 or Theorem 22.1 and pass:

$$
N\to\infty.
$$

The left side diverges by SL-1 while the right side remains finite by SL-2--SL-3.

$\square$

---

# 46. Meaning of the compiler

This is the first FCBP closure theorem whose **scale weight itself is non-summable**.

The remaining gap is no longer the existence of a non-summable schedule.

It is the Navier--Stokes control needed to satisfy SL-1--SL-3.

---

# 47. Updated Critical-Lift obligations

FCBP-01/02 used:

$$
CL\mbox{-}DER,
\quad
CL\mbox{-}REM,
\quad
CL\mbox{-}PACK.
$$

After FCBP-03:

### CL-DER

$$
\boxed{
\mathrm{PARTIALLY\ CLOSED}.
}
$$

### CL-REM

$$
\boxed{
\mathrm{OPEN/PARTIAL}.
}
$$

### CL-PACK

A non-summable **schedule** is now available.

The remaining packing problem is compressed to:

$$
\boxed{
\text{FSP}
+
\text{AOB/ASD}
+
\text{weighted leakage/backscatter}.
}
$$

Thus:

$$
\boxed{
CL\mbox{-}PACK
:
\mathrm{PARTIALLY\ OPEN\ WITH\ A\ NEW\ NONSUMMABLE\ ROUTE}.
}
$$

---

# 48. Next paper

The next paper should exploit the new schedule rather than return to geometric scales:

$$
\boxed{
\textbf{
NS-FCBP 04 —
Moving-Filter Telescoping,
Filter-Switch Energy Defects,
Slow-Scale Active Windows
and Borderline Critical Lift
}.
}
$$

Primary tasks:

1. estimate:
   $$
   \Delta_k^{filt};
   $$
2. test bounded variation of localized resolved energy in filter scale;
3. compare moving-filter and finest-common-filter strategies;
4. seek uniform coarse observability as:
   $$
   \ell^{(N)}\to0;
   $$
5. control slow-schedule weighted leakage/backscatter;
6. prove active-window weighted density or route its failure to subfilter/model-cone/commutator recurrence;
7. decide whether SL-1--SL-3 can be obtained from Navier--Stokes structure.

---

# 49. Formal status ledger

$$
\boxed{
\begin{aligned}
\text{external geometric pressure--flux telescope}
&:\ \mathrm{EXTERNAL/PROVED},\\
\text{Variable-Radius Pressure--Flux Telescope}
&:\ \mathrm{PROVED},\\
\text{Slow-Scale Critical-Lift Window}
&:\ \mathrm{PROVED},\\
\text{Non-Summable Work-Depletion Criterion}
&:\ \mathrm{PROVED\ CONDITIONAL},\\
\text{Weighted Backscatter Closure}
&:\ \mathrm{OPEN},\\
\text{Common-Filter/Critical-Resolution Barrier}
&:\ \mathrm{PROVED},\\
\text{Moving-Filter Telescope}
&:\ \mathrm{PROVED},\\
\text{Filter-Switch Packing}
&:\ \mathrm{OPEN},\\
\text{Finest-Scale Common-Filter Strategy}
&:\ \mathrm{DEFINED/OPEN},\\
\text{Active Observability Bridge}
&:\ \mathrm{OPEN},\\
\text{Active-Slab Density}
&:\ \mathrm{OPEN},\\
\text{Model-Cone Growth Packet}
&:\ \mathrm{PROVED},\\
\text{Affine-to-Pressure--Flux Bridge}
&:\ \mathrm{OPEN},\\
\text{Slow-Scale Critical-Lift Compiler}
&:\ \mathrm{PROVED\ CONDITIONAL},\\
\text{Critical Lift}
&:\ \mathrm{OPEN},\\
\text{Forest Coercive Budget}
&:\ \mathrm{OPEN},\\
\text{Finite Forest Obstruction}
&:\ \mathrm{OPEN},\\
CN3_{\rm Atomic}
&:\ \mathrm{OPEN},\\
\text{Navier--Stokes regularity}
&:\ \mathrm{NOT\ PROVED}.
\end{aligned}
}
$$

---

# 50. Conclusion

FCBP-03 changes the Critical-Lift problem substantially.

The weighted pressure--flux telescope was previously treated as scale-weak because the published theorem uses:

$$
r_k=\theta^kr_0,
$$

so:

$$
\sum_k
r_k/r_0
<
\infty.
$$

But the endpoint cancellation itself uses only:

$$
w_kr_k^{-1}=r_0^{-1}
$$

and nested spatial cutoffs.

Therefore arbitrary decreasing radii are allowed at the telescope level.

The slow schedule:

$$
r_k
=
r_0(k+1)^{-\beta},
\qquad
\frac12<\beta\le1,
$$

simultaneously has:

$$
\sum_kr_k^2<\infty
$$

and:

$$
\sum_k r_k/r_0=\infty.
$$

Thus FCBP now has a genuine borderline/non-summable pressure--flux telescope.

The new obstruction is compatibility.

A common physical filter preserves the exact telescope but cannot remain scale relative forever.

Moving scale-relative filters preserve critical resolution but introduce explicit filter-switch endpoint defects.

A finite-chain finest-scale common filter avoids switch defects but shifts the problem to uniform-in-chain-length observability and residual control.

The signed work itself also remains subject to backscatter and pressure--flux cancellation.

Finally, the Miller strain balance gives an independent scale-critical Model-Cone Growth Packet whenever dangerous strain growth occurs.

The new frontier is therefore no longer:

> can one produce a non-summable weight?

That has now been answered.

The frontier is:

$$
\boxed{
\textbf{
can scale-relative observability and endpoint compatibility survive on that non-summable slow schedule?
}
}
$$

That is FCBP-04.

---

# References

1. R. Yu, *Coarse-Grained Resolution and Pressure--Flux Work Depletion for Navier--Stokes CKN Badness*, arXiv:2606.25322.
2. R. Yu, *Filtered Vortex Stretching and Subgrid Defects for the Three-Dimensional Navier--Stokes Equations*, arXiv:2606.27560.
3. R. Yu, *Invisible Defect Cascades for Navier--Stokes Regularity*, arXiv:2606.12756.
4. R. Yu, *Critical Ledgers and Scale-Defect Cascades for Navier--Stokes*, arXiv:2606.13887.
5. E. Miller, *On the interaction of strain and vorticity for solutions of the Navier--Stokes equation*, arXiv:2407.02691.
6. `NS_FCBP_01_CriticalForest_Coercivity_v0.1.md`.
7. `NS_FCBP_02_FilteredStretching_CriticalLift_v0.1.md`.