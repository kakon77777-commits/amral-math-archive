---
title: "Navier–Stokes C5-H: All-Order Effective-Volume Defects, Spectral-Multiplicity Ladders, and Asymptotic-Critical Compatibility"
subtitle: "Why Static All-Order Volume Sparseness Cannot Replace Dynamic Interpolation, and How Derivative Defects Factor into Spectral Scale, Physical Multiplicity, and Chain Timing"
version: "v0.1"
date: "2026-08-15"
author: "Neo.K / EveMissLab"
language: "en-US"
status: "Theorem-style all-order derivative audit / static-volume no-go / transition to sign-geometry chains"
epistemic_status: "Exact Fourier-moment log-convexity + Agmon effective-cell factorization + exact algebraic comparison with Grujić–Xu 2024 Theorems 3.5, 3.7, 3.14. Establishes methodological no-go and conditional chain interfaces, not global regularity."
---

# Navier–Stokes C5-H
# All-Order Effective-Volume Defects, Spectral-Multiplicity Ladders, and Asymptotic-Critical Compatibility

## 0. Orientation for this Round

C5-G yielded the first truly theorem-ready fixed-order direct gate.

For any fixed:

$$
k\ge1,
$$

define:

$$
A_k(s)
=
\|D^ku(s)\|_\infty,
$$

$$
L_k(s)
=
\|D^ku(s)\|_2.
$$

The global volume of the component/sign superlevel set is given by:

$$
r_{vol,k}
\lesssim
L_k^{2/3}
A_k^{-2/3}.
$$

Meanwhile, the $d=3$ direct target of Grujić–Xu 2024 Theorem 3.5 is:

$$
r_{dir,k}
\asymp
\frac{
1
}{
2^k
c_{dir,k}
A_k^{3/(2k+3)}
}.
$$

Therefore:

$$
\boxed{
\mathfrak G_k^{dir}
=
r_{vol,k}/r_{dir,k}
}
$$

If at a theorem-admissible later time:

$$
\le1,
$$

it genuinely triggers the published regularity theorem.

Following C5-G, a natural question arises:

> If a hypothetical survivor maintains $\mathfrak G_k^{dir}>1$ for all fixed $k$, can a contradiction be formed as $k\to\infty$?

The answer from C5-H is:

$$
\boxed{
\textbf{Cannot rely solely on a static all-order effective-volume ladder.}
}
$$

More strongly:

1. The $2^{-k}$ spatial factor in Theorem 3.5 allows the high-$k$ direct gate to fail entirely even for perfectly smooth, single-scale analytic profiles;
2. The admissible time window of the direct theorem similarly carries a $4^{-k}$ factor;
3. Thus, fixed-$k$ direct gates do not form a ladder where "higher order implies closer to automatic closure";
4. The true high-order mechanism of Grujić–Xu is:
   $$
   \boxed{
   \textbf{chain-normalized derivative amplitudes}
   +
   \textbf{dynamic interpolation}
   +
   \textbf{component/sign 1D geometry};
   }
   $$
5. Upon incorporating $L^2$ spectral moments, the effective-volume defect can be factored into:
   $$
   \boxed{
   \text{spectral cell scale}
   \times
   \text{physical multiplicity};
   }
   $$
6. The $L^2$ spectral frequency ladder is forced to be monotone by Fourier moment log-convexity;
7. However, the physical multiplicity is completely uncontrolled by log-convexity;
8. Consequently, the scenario where "all fixed-$k$ are diffuse" yields no contradiction at the interpolation level;
9. Using the Theorem 3.14 chain scale, one can define a genuine all-order chain compatibility ratio;
10. Yet, the global-volume route itself cannot even satisfy the high-$k$ chain scale on a generic uncertainty-limited smooth analytic packet;
11. This proves:
    $$
    \boxed{
    \textbf{volume-only geometry is intrinsically too coarse to recover the asymptotic-critical mechanism};
    }
    $$
12. The true scaling gap of Theorem 3.14:
    $$
    \frac1{k+1}
    -
    \frac2{2k+3}
    =
    \frac1{(k+1)(2k+3)}
    $$
    indeed tends to zero;
13. Therefore, if the actual geometry exhibits any fixed-power concentration improvement relative to the energy a-priori scale, the spatial chain burden will eventually be overcome in regimes where theorem constants do not dominate;
14. Thus, a true high-order survivor must be:
    $$
    \boxed{
    \text{asymptotic a-priori saturation}
    \vee
    \text{multiplicity}
    \vee
    \text{chain/time defect};
    }
    $$
15. C5-H formally eliminates:
    $$
    \boxed{
    \textbf{All-Order Static Effective-Volume Closure Program};
    }
    $$
16. The next step must pivot to:
    $$
    \boxed{
    \textbf{component/sign microgeometry + derivative-chain sections + harmonic measure}.
    }
    $$

---

# 1. Fresh primary-source audit

This round re-audits the official 2024 version of record of Grujić–Xu.

## 1.1 Theorem 3.5 — Fixed-order direct gate

In the $d=3$ velocity route,

if $t$ is the $D^ku$ escape time,

the theorem requires the existence of:

$$
\boxed{
s=s(t)
}
$$

located in:

$$
\boxed{
t+
\frac{
1
}{
4^{k+1}
c(M,\|u_0\|_2)^2
A_k(t)^{6/(2k+3)}
}
\le
s
\le
t+
\frac{
1
}{
4^k
c(M,\|u_0\|_2)^2
A_k(t)^{6/(2k+3)}
}.
}
$$

and requires the selected component/sign superlevel set at scale:

$$
\boxed{
\rho
\le
\frac{
1
}{
2^k
c(M)
A_k(s)^{3/(2k+3)}
}
}
$$

to be 1D sparse.

### Hard observation

Both the spatial and time windows of Theorem 3.5 contain:

$$
\boxed{
2^{-k},
\qquad
4^{-k}
}
$$

order-dependent exponential factors.

---

# 2. Theorem 3.7 — Energy-level a-priori sparseness

In $d=3$:

$$
\boxed{
r_{apr,k}
=
c(\|u_0\|_2)
A_k^{-2/(2k+3)}.
}
$$

Thus, the a-priori scale exponent is:

$$
\boxed{
p_k^{apr}
=
\frac2{2k+3}.
}
$$

The direct regularity exponent is:

$$
\boxed{
p_k^{dir}
=
\frac3{2k+3}.
}
$$

The difference is:

$$
\boxed{
p_k^{dir}
-
p_k^{apr}
=
\frac1{2k+3}.
}
$$

---

# 3. Theorem 3.14 — Asymptotic criticality

The velocity chain scale of Theorem 3.14 is:

$$
\boxed{
r_{chain,k}
=
\frac{
1
}{
2
\widetilde{\mathcal C}_k
A_k^{1/(k+1)}
}.
}
$$

The admissible later time is:

$$
\boxed{
s-t
\asymp
\widetilde{\mathcal C}_k^{-1}
A_k(t)^{-2/(k+1)}
}
$$

up to the theorem's factor of $1/4$.

Its constants satisfy:

$$
\boxed{
\widetilde{\mathcal C}_k
\gtrsim
k^2
\mathcal C_k.
}
$$

Theorem 3.14 also utilizes:

- ascending chains;
- descending chains;
- Type-$\mathcal A$/Type-$\mathcal B$ sections;
- harmonic-measure sparseness;
- local-in-time dynamic interpolation.

---

# 4. Grujić–Xu chain-normalized derivative amplitude

The exact definition in the paper is:

$$
\boxed{
\mathcal R(k,c,t)
=
\frac{
A_k(t)^{1/(k+1)}
}{
c^{k/(k+1)}
(k!)^{1/(k+1)}
}.
}
$$

Therefore:

$$
\boxed{
A_k^{1/(k+1)}
=
c^{k/(k+1)}
(k!)^{1/(k+1)}
\mathcal R(k,c,t).
}
$$

What ascending/descending chains compare is not:

$$
A_k
$$

itself,

but rather:

$$
\boxed{
\mathcal R(k,c,t).
}
$$

---

# 5. First correction to C5-G intuition

The C5-G fixed-$k$ direct ratio is a valid theorem-ready gate.

However:

$$
\boxed{
\text{fixed-}k\text{ gate being theorem-ready}
}
$$

does not imply:

$$
\boxed{
\text{all fixed-}k\text{ gates form an asymptotically closing ladder}.
}
$$

One of the reasons is precisely:

$$
2^{-k}.
$$

---

# 6. Smooth single-scale model

The following is merely an inference no-go model,

not an N–S orbit construction.

Take a smooth divergence-free band-limited wavepacket:

$$
u^{model},
$$

with Fourier support located in a small cone:

$$
|\xi|
\sim
\Lambda,
$$

and make a certain derivative direction:

$$
\partial_1^k
$$

nondegenerate.

Then:

$$
\boxed{
A_k
\asymp
\Lambda^kA_0,
}
$$

$$
\boxed{
L_k
\asymp
\Lambda^kL_0.
}
$$

Therefore, the effective-volume radius:

$$
\boxed{
r_{vol,k}
\asymp
\left(
\frac{
L_0^2
}{
A_0^2
}
\right)^{1/3}
}
$$

remains essentially unchanged with $k$.

---

# 7. C5-H.1: All-Order Direct-Gate No-Go

For the §6 model,

the Theorem 3.5 direct scale is:

$$
r_{dir,k}
\asymp
2^{-k}
\Lambda^{-3k/(2k+3)}
A_0^{-3/(2k+3)}.
$$

So:

$$
\boxed{
r_{dir,k}
\sim
2^{-k}
\Lambda^{-3/2}
}
$$

up to subexponential corrections.

Therefore:

$$
\boxed{
\mathfrak G_k^{dir}
=
r_{vol,k}/r_{dir,k}
\to\infty
}
$$

exponentially.

### Conclusion

$$
\boxed{
\textbf{A completely smooth, single-scale analytic profile
can fail every sufficiently high fixed-}k\textbf{ direct gate
under the crude volume certificate.}
}
$$

### Status

This is an inference no-go,

not a counterexample to Theorem 3.5.

Theorem 3.5 is a sufficient criterion,

not a necessary condition.

---

# 8. Direct time-window no-go

For the same model:

$$
A_k
\asymp
\Lambda^k.
$$

The Theorem 3.5 delay is:

$$
\tau_{dir,k}
\asymp
4^{-k}
A_k^{-6/(2k+3)}.
$$

So:

$$
\boxed{
\tau_{dir,k}
\sim
4^{-k}
\Lambda^{-3}
}
$$

up to subexponential factors.

Therefore, the high-$k$ direct admissible windows themselves exhibit exponential Zeno shrinkage.

### Conclusion

$$
\boxed{
\textbf{all-order direct TIME defects also cannot vanish automatically via order escalation}.
}
$$

---

# 9. Why Theorem 3.14 is structurally different

The chain delay is:

$$
\boxed{
\tau_{chain,k}
\asymp
\widetilde{\mathcal C}_k^{-1}
A_k^{-2/(k+1)}.
}
$$

For the single-scale:

$$
A_k\sim\Lambda^k,
$$

$$
\boxed{
\tau_{chain,k}
\sim
\widetilde{\mathcal C}_k^{-1}
\Lambda^{-2}.
}
$$

There is no:

$$
4^{-k}
$$

exponential factor.

This precisely demonstrates:

$$
\boxed{
\textbf{dynamic interpolation is not a simple repetition of the high-order direct criterion}.
}
$$

---

# 10. Rotationally invariant $L^2$ derivative moments

To study the all-order spectral ladder,

define:

$$
\boxed{
M_k(t)
=
\|\Lambda^ku(t)\|_2^2
=
\int_{\mathbb R^3}
|\xi|^{2k}
|\widehat u(\xi,t)|^2d\xi.
}
$$

Let:

$$
\boxed{
L_k^\sharp
=
M_k^{1/2}.
}
$$

All fixed-order component $L^2$ norms are controlled by:

$$
L_k^\sharp
$$

---

# 11. C5-H.2: Fourier Moment Log-Convexity

By Cauchy–Schwarz:

$$
M_k
=
\int
\left(
|\xi|^{k-1}
|\widehat u|
\right)
\left(
|\xi|^{k+1}
|\widehat u|
\right)
d\xi.
$$

So:

$$
\boxed{
M_k^2
\le
M_{k-1}
M_{k+1}.
}
$$

Therefore:

$$
\boxed{
q_k
=
\left(
\frac{
M_{k+1}
}{
M_k
}
\right)^{1/2}
}
$$

is nondecreasing in:

$$
k.
$$

---

# 12. Two-step spectral frequency

Define:

$$
\boxed{
\Lambda_k
=
\left(
\frac{
L_{k+2}^\sharp
}{
L_k^\sharp
}
\right)^{1/2}
=
\left(
\frac{
M_{k+2}
}{
M_k
}
\right)^{1/4}.
}
$$

Since:

$$
\Lambda_k
=
(q_kq_{k+1})^{1/2},
$$

and:

$$
q_k
$$

is nondecreasing,

we obtain:

$$
\boxed{
\Lambda_{k+1}
\ge
\Lambda_k.
}
$$

### Interpretation

$$
\boxed{
\textbf{$L^2$ spectral frequency ladder is monotone}.
}
$$

---

# 13. Agmon inequality on the maximizing derivative component

Let the selected scalar derivative component:

$$
f_k
=
D^\zeta u_i,
\qquad
|\zeta|=k,
$$

satisfy:

$$
\|f_k\|_\infty
=
A_k
$$

after choosing a maximizer among finitely many components.

The 3D Agmon inequality gives:

$$
\boxed{
\|f_k\|_\infty
\le
C_A
\|f_k\|_2^{1/4}
\|D^2f_k\|_2^{3/4}.
}
$$

And:

$$
\|f_k\|_2
\le
L_k^\sharp,
$$

$$
\|D^2f_k\|_2
\le
L_{k+2}^\sharp.
$$

So:

$$
\boxed{
A_k
\le
C_A
L_k^\sharp
\Lambda_k^{3/2}.
}
$$

---

# 14. Spectral-cell multiplicity

Define the effective volume:

$$
\boxed{
V_k^{eff}
=
\frac{
(L_k^\sharp)^2
}{
A_k^2
}.
}
$$

Define:

$$
\boxed{
\mathfrak N_k
=
\Lambda_k^3
V_k^{eff}
=
\Lambda_k^3
\frac{
(L_k^\sharp)^2
}{
A_k^2
}.
}
$$

which is dimensionless.

Agmon gives:

$$
\boxed{
\mathfrak N_k
\ge
C_A^{-2}.
}
$$

### Interpretation

$$
\Lambda_k^{-3}
$$

is the spectral-cell volume.

Therefore:

$$
\boxed{
\mathfrak N_k
}
$$

quantifies how many spectral-sized cells are contained within the derivative effective volume.

It is the:

$$
\boxed{
\textbf{Spectral-Cell Multiplicity}.
}
$$

---

# 15. Exact effective-radius factorization

$$
(V_k^{eff})^{1/3}
=
\boxed{
\mathfrak N_k^{1/3}
\Lambda_k^{-1}.
}
$$

Thus, the global-volume sparseness scale decomposes into:

$$
\boxed{
\text{spectral cell length}
\times
\text{multiplicity penalty}.
}
$$

---

# 16. What log-convexity does and does not control

Log-convexity gives:

$$
\boxed{
\Lambda_k\uparrow.
}
$$

But it does not provide:

$$
\boxed{
\mathfrak N_k\le C.
}
$$

Therefore, high-derivative spectral migration:

$$
\Lambda_k\to\infty
$$

can perfectly well occur simultaneously with:

$$
\mathfrak N_k\to\infty
$$

### Conclusion

$$
\boxed{
\textbf{spectral cascade does not force physical concentration}.
}
$$

This is the core no-go of the all-order effective-volume route.

---

# 17. Direct gate factorization

Ignoring the fixed volume-to-line constant,

$$
r_{vol,k}
=
\mathfrak N_k^{1/3}
\Lambda_k^{-1}.
$$

the direct theorem scale is:

$$
r_{dir,k}
=
\frac1{
2^kc_{dir,k}
A_k^{3/(2k+3)}
}.
$$

So:

$$
\boxed{
\mathfrak G_k^{dir}
\asymp
2^k
c_{dir,k}
\mathfrak N_k^{1/3}
\frac{
A_k^{3/(2k+3)}
}{
\Lambda_k
}.
}
$$

### Three direct coordinates

1. order penalty:
   $$
   2^k;
   $$
2. physical multiplicity:
   $$
   \mathfrak N_k^{1/3};
   $$
3. spectral/peak mismatch:
   $$
   A_k^{3/(2k+3)}/\Lambda_k.
   $$

---

# 18. Direct gate can fail with perfect single-cell concentration

Even if:

$$
\mathfrak N_k
\sim1,
$$

and:

$$
\Lambda_k
\sim\Lambda,
$$

the single-scale model still yields:

$$
\mathfrak G_k^{dir}
\sim
2^k.
$$

So a high-order direct failure does not equate to:

$$
\boxed{
\text{packet multiplicity}.
}
$$

It can simply be an artifact of the theorem's direct-scale structure.

---

# 19. Chain-scale spatial ratio

The Theorem 3.14 spatial target is:

$$
\boxed{
r_{chain,k}
=
\frac1{
2\widetilde{\mathcal C}_k
A_k^{1/(k+1)}
}.
}
$$

Define the volume-certified chain ratio:

$$
\boxed{
\mathfrak G_k^{chain,vol}
=
\frac{
r_{vol,k}
}{
r_{chain,k}
}.
}
$$

Using §15:

$$
\boxed{
\mathfrak G_k^{chain,vol}
=
2
\widetilde{\mathcal C}_k
\mathfrak N_k^{1/3}
\frac{
A_k^{1/(k+1)}
}{
\Lambda_k
}.
}
$$

---

# 20. Chain spectral-to-root ratio

Define:

$$
\boxed{
\mathfrak X_k
=
\frac{
\Lambda_k
}{
A_k^{1/(k+1)}
}.
}
$$

Then:

$$
\boxed{
\mathfrak G_k^{chain,vol}
=
2
\widetilde{\mathcal C}_k
\frac{
\mathfrak N_k^{1/3}
}{
\mathfrak X_k
}.
}
$$

For the volume route to satisfy the chain spatial hypothesis,

it requires:

$$
\boxed{
\mathfrak X_k
\ge
2
\widetilde{\mathcal C}_k
\mathfrak N_k^{1/3}.
}
$$

---

# 21. Relation to Grujić–Xu $\mathcal R$

Since:

$$
A_k^{1/(k+1)}
=
c^{k/(k+1)}
(k!)^{1/(k+1)}
\mathcal R(k,c,t),
$$

So:

$$
\boxed{
\mathfrak X_k
=
\frac{
\Lambda_k
}{
c^{k/(k+1)}
(k!)^{1/(k+1)}
\mathcal R(k,c,t)
}.
}
$$

Therefore:

$$
\boxed{
\textbf{our spatial multiplicity ladder}
}
$$

and

$$
\boxed{
\textbf{Grujić--Xu chain amplitude ladder}
}
$$

are connected by an exact spectral ratio.

---

# 22. All-order state is at least two-dimensional

Grujić–Xu ascending/descending chains control:

$$
\mathcal R(k,c,t)
$$

across $k$.

The C5-H spatial route additionally requires:

$$
\boxed{
\Lambda_k,
\qquad
\mathfrak N_k.
}
$$

Thus, the all-order derivative state is not a single sequence:

$$
A_k.
$$

It is at least:

$$
\boxed{
\Theta_k^{H}
=
\left\langle
\mathcal R_k,
\Lambda_k,
\mathfrak N_k
\right\rangle.
}
$$

---

# 23. C5-H.3: Volume-Only Chain No-Go

Consider the §6 uncertainty-limited band-limited model.

We have:

$$
\boxed{
\Lambda_k
\asymp
\Lambda,
}
$$

$$
\boxed{
A_k^{1/(k+1)}
\to
\Lambda
}
$$

up to constant amplitude roots,

so:

$$
\boxed{
\mathfrak X_k
\asymp1.
}
$$

and:

$$
\boxed{
\mathfrak N_k
\asymp1.
}
$$

But the Theorem 3.14 constants satisfy:

$$
\boxed{
\widetilde{\mathcal C}_k
\gtrsim
k^2\mathcal C_k.
}
$$

Therefore:

$$
\boxed{
\mathfrak G_k^{chain,vol}
\gtrsim
k^2
}
$$

modulo the remaining theorem constants.

### Conclusion

$$
\boxed{
\textbf{Even the chain-scale theorem cannot in general be certified
by a crude global-volume bound at high derivative order.}
}
$$

Again:

this is not a theorem counterexample.

It proves:

$$
\boxed{
\textbf{volume-only sufficient certificate is too coarse}.
}
$$

---

# 24. Why this is geometrically natural

Theorem 3.14 requires:

$$
\boxed{
\text{1D component/sign sparseness}.
}
$$

A high derivative can, with almost no shrinkage in physical volume,

via:

- rapid sign alternation;
- filament geometry;
- directional oscillation;

become highly sparse on line sections.

The global volume:

$$
|V|
$$

is blind to this microgeometry.

Therefore:

$$
\boxed{
\text{small global volume}
}
$$

is a sufficient certificate for 1D sparseness,

but not the full geometry actually utilized by the asymptotic-critical theorem.

---

# 25. Static volume cannot reproduce dynamic interpolation

Therefore:

$$
\boxed{
\textbf{C5 static effective-volume ladder}
}
$$

cannot replace:

$$
\boxed{
\textbf{Grujić--Xu dynamic interpolation}.
}
$$

Theorem 3.14 genuinely utilizes:

- chain-normalized amplitudes;
- local analyticity;
- Type-$\mathcal A$/Type-$\mathcal B$ strings;
- harmonic measure;
- sign/component geometry.

---

# 26. A-priori vs chain exponent gap

Theorem 3.7:

$$
r_{apr,k}
=
a_k
A_k^{-p_k},
$$

$$
p_k
=
\frac2{2k+3}.
$$

Theorem 3.14:

$$
r_{chain,k}
=
b_k
A_k^{-q_k},
$$

$$
q_k
=
\frac1{k+1}.
$$

where:

$$
a_k
=
c(\|u_0\|_2),
$$

$$
b_k
=
\frac1{
2\widetilde{\mathcal C}_k
}.
$$

---

# 27. C5-H.4: Vanishing Chain Exponent Burden

Exact:

$$
\boxed{
q_k-p_k
=
\frac1{
(k+1)(2k+3)
}.
}
$$

So:

$$
\boxed{
q_k-p_k
\sim
\frac1{
2k^2
}
\to0.
}
$$

This is the core exponent fact of Grujić–Xu asymptotic-criticality.

---

# 28. Compare with direct gap

Direct:

$$
q_k^{dir}
=
\frac3{2k+3}.
$$

So:

$$
\boxed{
q_k^{dir}-p_k
=
\frac1{2k+3}
\sim
\frac1{2k}.
}
$$

Chain improvement:

$$
\boxed{
\frac{
q_k-p_k
}{
q_k^{dir}-p_k
}
=
\frac1{k+1}.
}
$$

So purely exponent-wise,

the chain burden is the direct burden multiplied by:

$$
\boxed{
1/(k+1).
}
$$

---

# 29. Effective concentration-gain exponent

Assume:

$$
A_k>1.
$$

Define the actual volume scale:

$$
r_{eff,k}
=
r_{vol,k}.
$$

The concentration gain relative to the a-priori scale is:

$$
\boxed{
\varepsilon_k^{eff}
=
\frac{
\log
(
r_{apr,k}/r_{eff,k}
)
}{
\log A_k
}.
}
$$

That is:

$$
\boxed{
r_{eff,k}
=
r_{apr,k}
A_k^{-\varepsilon_k^{eff}}.
}
$$

---

# 30. C5-H.5: Exact Chain Spatial Gain Condition

The chain spatial condition:

$$
r_{eff,k}
\le
r_{chain,k}
$$

is equivalent to:

$$
\boxed{
\varepsilon_k^{eff}
\ge
\frac1{
(k+1)(2k+3)
}
+
\frac{
\log(a_k/b_k)
}{
\log A_k
}.
}
$$

where:

$$
\boxed{
a_k/b_k
=
2a_k
\widetilde{\mathcal C}_k.
}
$$

### Interpretation

Two burdens are required:

1. geometric exponent burden:
   $$
   1/[(k+1)(2k+3)];
   $$
2. theorem-constant burden:
   $$
   \log(a_k/b_k)/\log A_k.
   $$

---

# 31. Fixed-power gain eventually beats the exponent gap

If along:

$$
k_j\to\infty
$$

we have:

$$
\boxed{
\varepsilon_{k_j}^{eff}
\ge
\varepsilon_0>0,
}
$$

and:

$$
\boxed{
\frac{
\log(a_{k_j}/b_{k_j})
}{
\log A_{k_j}
}
\to0,
}
$$

then for sufficiently large:

$$
j
$$

we have:

$$
\boxed{
r_{eff,k_j}
\le
r_{chain,k_j}.
}
$$

### Status

This only concerns the:

$$
\boxed{
\textbf{spatial chain-scale burden}.
}
$$

The remaining aspects of Theorem 3.14:

- chain;
- time;
- analytic;
- all-order hypotheses;

must still be aligned separately.

---

# 32. Asymptotic a-priori saturation

Conversely,

if the high-$k$ spatial chain gate fails perpetually,

and the theorem constant burden is negligible relative to:

$$
\log A_k,
$$

then there cannot exist any uniform:

$$
\varepsilon_0>0
$$

concentration gain.

Therefore:

$$
\boxed{
\liminf_{k\to\infty}
\varepsilon_k^{eff}
\le0
}
$$

along the survivor subsequence.

This document terms this the:

$$
\boxed{
\textbf{Asymptotic A-Priori Saturation Defect}.
}
$$

### Meaning

The actual spatial concentration of high derivatives cannot improve upon the energy-level a-priori sparseness by any fixed power.

---

# 33. Direct constant burden does not vanish automatically

For the direct theorem:

$$
b_k^{dir}
=
\frac1{
2^k c_{dir,k}
}.
$$

The same calculation gives:

$$
\varepsilon_k^{eff}
\ge
\frac1{
2k+3
}
+
\frac{
k\log2
+
\log(a_kc_{dir,k})
}{
\log A_k
}.
$$

So even if:

$$
1/(2k+3)\to0,
$$

there remains:

$$
\boxed{
k\log2/\log A_k.
}
$$

If:

$$
\log A_k
\sim
k,
$$

this term will not vanish.

### This explains the direct no-go algebraically.

---

# 34. Chain constant burden is structurally milder

Theorem 3.14 does not have the:

$$
2^k
$$

spatial factor,

but only the:

$$
\widetilde{\mathcal C}_k
$$

theorem constant.

If in a certain regime:

$$
\log\widetilde{\mathcal C}_k
=
o(\log A_k),
$$

then the constant burden vanishes.

### Guard

The published theorem gives:

$$
\widetilde{\mathcal C}_k
\gtrsim
k^2\mathcal C_k,
$$

but C5-H does not assume a universal upper growth law.

Therefore:

$$
\boxed{
\text{constant burden must remain explicit}.
}
$$

---

# 35. L2 log-convexity alone cannot eliminate saturation defect

Even if:

$$
\Lambda_k
$$

is monotone,

$\varepsilon_k^{eff}$ still contains:

$$
\mathfrak N_k.
$$

From:

$$
r_{eff,k}
=
\mathfrak N_k^{1/3}\Lambda_k^{-1},
$$

as long as:

$$
\mathfrak N_k
$$

grows,

the actual effective concentration gain can be completely offset.

Therefore:

$$
\boxed{
\textbf{Fourier moment log-convexity alone
cannot force high-order spatial concentration}.
}
$$

---

# 36. Multipacket realization no-go

The following again serves only as an abstract inference example.

Consider:

$$
N
$$

widely separated, almost-disjoint identical wavepackets.

Then:

$$
A_k
$$

roughly maintains the one-packet peak,

but:

$$
L_k^2
$$

is multiplied by approximately:

$$
N.
$$

So:

$$
\boxed{
V_k^{eff}
\sim
N
V_{k,1}^{eff},
}
$$

$$
\boxed{
\mathfrak N_k
\sim
N
\mathfrak N_{k,1}.
}
$$

Therefore:

$$
\boxed{
\textbf{all-order gate failure can be supported by spatial multiplicity
without changing derivative spectral scale}.
}
$$

This continues the C3/C4 carrier multiplicity theme.

---

# 37. All-order derivative defect factorization

Now, the fixed/high-order spatial defect can be organized into:

## H-SPEC — Spectral-root mismatch

$$
\boxed{
\mathfrak X_k
=
\Lambda_k/A_k^{1/(k+1)}
}
$$

is too small.

## H-MULT — Spectral-cell multiplicity

$$
\boxed{
\mathfrak N_k
}
$$

is too large.

## H-SAT — A-priori saturation

The actual concentration gain exponent:

$$
\boxed{
\varepsilon_k^{eff}
}
$$

tends to zero or is non-positive.

## H-TIME — chain/direct time mismatch

Favorable geometry does not fall within the theorem-admissible later window.

## H-CHAIN — derivative-chain structural defect

Ascending/descending/Type-$\mathcal A$/$\mathcal B$ conditions do not conform to the theorem route.

---

# 38. Chain-section compression

Grujić–Xu Definition 3.15 partitions derivative orders into sections:

$$
\boxed{
\ell_0<\ell_1<\cdots,
\qquad
\ell_{i+1}
=
\phi(\ell_i)
\ge
2\ell_i.
}
$$

In each section:

$$
[\ell_i,\ell_{i+1}],
$$

choose:

$$
\boxed{
m_i
}
$$

such that:

$$
\mathcal R(m_i,c(\ell_i),t)
=
\max_{\ell_i\le j\le\ell_{i+1}}
\mathcal R(j,c(\ell_i),t).
$$

C5-H adopts this block compression.

---

# 39. C5-H block state

For each:

$$
m_i,
$$

append the C5 coordinates:

$$
\boxed{
\Theta_i^{block}
=
\left\langle
\mathcal R_{m_i},
\Lambda_{m_i},
\mathfrak N_{m_i},
\varepsilon_{m_i}^{eff},
\mathsf T_{m_i},
\mathsf C_i
\right\rangle.
}
$$

where:

- $\mathsf T$ = theorem timing status;
- $\mathsf C$ = Type-$\mathcal A$/Type-$\mathcal B$/chain metadata.

### Benefit

No longer tracking individually:

$$
k=1,2,3,\ldots
$$

to infinity.

Instead, like the published theorem, we track maxima over exponentially separated derivative blocks.

---

# 40. Block-max derivative escalation

If the survivor continuously pushes the maxima to higher sections:

$$
m_i\to\infty,
$$

that is:

$$
\boxed{
\textbf{Derivative-Block Escape}.
}
$$

If a certain fixed block recurrently assumes the maximum,

then it is a:

$$
\boxed{
\textbf{Fixed-Block Defect}.
}
$$

This is much closer to the published chain structure than simply:

$$
k_j\to\infty
$$

---

# 41. Direct vs chain temporal windows

Direct:

$$
\tau_{dir,k}
\sim
4^{-k}
A_k^{-6/(2k+3)}.
$$

Chain:

$$
\tau_{chain,k}
\sim
\widetilde{\mathcal C}_k^{-1}
A_k^{-2/(k+1)}.
$$

Ratio:

$$
\boxed{
\frac{
\tau_{chain,k}
}{
\tau_{dir,k}
}
\sim
4^k
\widetilde{\mathcal C}_k^{-1}
A_k^{\frac{
2k
}{
(k+1)(2k+3)
}}
}
$$

up to fixed constants.

### Interpretation

The chain mechanism accesses a parametrically different temporal scale.

Therefore:

$$
\boxed{
\textbf{high-order TIME defect must be studied in chain time,
not direct time}.
}
$$

---

# 42. Why direct all-order escalation is a methodological dead end

The C5-G fixed direct theorem remains useful:

For any single fixed:

$$
k
$$

if:

$$
\mathfrak G_k^{dir}\le1
$$

at an admissible time,

the route closes.

But if this does not occur,

raising:

$$
k
$$

does not make the direct criterion progressively easier.

Because of:

- the spatial $2^{-k}$ factor;
- the temporal $4^{-k}$ factor;
- the volume uncertainty floor.

Therefore:

$$
\boxed{
\textbf{direct theorem should remain a fixed-order kill switch,
not the high-order main engine}.
}
$$

---

# 43. Why chain route is the correct asymptotic object

Theorem 3.14:

- replaces the direct exponent with $1/(k+1)$;
- replaces $4^{-k}$ direct timing with chain-scale timing;
- uses $\mathcal R(k,c,t)$;
- synchronizes derivative orders dynamically;
- uses harmonic measure / sign geometry.

Thus, the C5 high-order route must switch from:

$$
\boxed{
\mathfrak G_k^{dir}
}
$$

to:

$$
\boxed{
\left(
\mathcal R_k,
\mathsf{SignGeometry}_k,
\mathsf{ChainType}_k,
\mathsf{Time}_k
\right).
}
$$

---

# 44. Static effective-volume state still has value

Although volume-only cannot fulfill the chain theorem,

it still provides:

$$
\boxed{
\mathfrak N_k
}
$$

as an independent multiplicity defect.

If in the future sign geometry succeeds at a very fine scale,

but:

$$
\mathfrak N_k\to\infty,
$$

it implies:

> line-sparseness is generated by a massive amount of sign-alternating/multipacket structures,

rather than by a small volume.

This is metadata that C5-I should preserve.

---

# 45. Sign geometry vs volume geometry

Two completely different routes:

## Volume concentration

$$
\boxed{
|V_{\lambda,k}|
\ll r^3.
}
$$

is sufficient to deduce 1D sparseness.

## Sign/oscillatory geometry

$$
|V_{\lambda,k}|
$$

can be very large,

yet the occupancy on each selected line remains very small.

Theorem 3.14 can utilize the second type.

Therefore:

$$
\boxed{
\textbf{all-order asymptotic criticality fundamentally needs sign geometry}.
}
$$

---

# 46. C5-H.6: Static All-Order Volume Closure No-Go

## Conclusion

The following inference cannot hold:

$$
\boxed{
\forall k\text{ fixed direct gate fails}
\Rightarrow
\exists k\text{ large volume gate closes}.
}
$$

Even:

$$
\boxed{
k\to\infty
}
$$

cannot guarantee the chain spatial gate by static volume / log-convexity alone.

### Proof ingredients

- band-limited smooth model;
- Agmon uncertainty floor;
- $2^{-k}$ direct factor;
- $k^2$-type chain theorem constants;
- unconstrained multiplicity $\mathfrak N_k$.

---

# 47. What all-order failure really means

If a hypothetical survivor evades:

1. every fixed-$k$ Theorem 3.5 kill switch;
2. Theorem 3.14 chain closure;

it does not have to produce an impossible norm sequence.

It only needs to recurrently maintain a certain set of:

$$
\boxed{
\text{Spectral/Multiplicity/Sign/Time/Chain defects}.
}
$$

This is a compact structural state,

not a scalar contradiction.

---

# 48. C5-H residual motifs

The high-order derivative survivor can now be compressed into:

## H1 — Fixed-Order Direct Kill-Switch Avoidance

$$
\boxed{
\mathfrak G_k^{dir}>1
\vee
\mathsf T_k^{dir}=0.
}
$$

## H2 — Spectral-Cell Multiplicity

$$
\boxed{
\mathfrak N_k\gg1.
}
$$

## H3 — Spectral/Peak-Root Mismatch

$$
\boxed{
\mathfrak X_k
\text{ insufficient}.
}
$$

## H4 — Asymptotic A-Priori Saturation

$$
\boxed{
\varepsilon_k^{eff}\to0
}
$$

in the relevant high-order route.

## H5 — Chain-Time Defect

Theorem 3.14 admissible times are not aligned.

## H6 — Sign-Geometry Defect

Component/sign 1D sparseness does not exist at the chain scale.

## H7 — Chain-Structure Defect

Ascending/descending / Type-A/B hypotheses are unfulfilled.

---

# 49. Relation to C5 temporal phase work

C5-B/C have already addressed physical-time pulse microstructure.

C5-H now reveals another microstructure in the "order dimension":

$$
\boxed{
k\mapsto
\mathcal R_k,
\Lambda_k,\mathfrak N_k.
}
$$

So the subsequent C5 work actually possesses:

- temporal Young state;
- derivative-order chain state;

two distinct compactification axes.

---

# 50. Proposed order-space measure

We can treat the exponentially separated block indices:

$$
i
$$

as a discrete order coordinate.

For a recurrent record:

$$
j,
$$

define the block defect vector:

$$
\boxed{
Z_{j,i}
=
(
\widehat{\mathcal R}_{j,i},
\widehat\Lambda_{j,i},
\widehat{\mathfrak N}_{j,i},
\mathsf{Sign}_{j,i},
\mathsf{Time}_{j,i},
\mathsf{Type}_{j,i}
).
}
$$

Each scalar unbounded coordinate is compactified to:

$$
[0,1].
$$

Finite block windows can extract product limits.

The full infinite order space can then be handled using:

- diagonal subsequences;
- sectionwise defect measures.

This round only defines the direction,

and does not formally expand on it.

---

# 51. A second asymptotic-critical interpretation

Theorem 3.7 a-priori exponent:

$$
\frac1{k+3/2}.
$$

Theorem 3.14 regularity exponent:

$$
\frac1{k+1}.
$$

Difference:

$$
\boxed{
\frac1{
2(k+1)(k+3/2)
}
=
\frac1{
(k+1)(2k+3)
}.
}
$$

So the exponent gap is indeed:

$$
O(k^{-2}).
$$

### C5 interpretation

If the survivor's high-$k$ geometry never crosses the chain gate,

then it must, within this:

$$
O(k^{-2})
$$

increasingly narrow exponent margin,

continuously use:

- constants;
- sign microgeometry;
- multiplicity;
- timing;

to compensate precisely.

This in itself is the:

$$
\boxed{
\textbf{Asymptotic Compensation Problem}.
}
$$

---

# 52. But exponent gap alone is not enough

If theorem constants or multiplicity:

$$
\mathfrak N_k
$$

grow rapidly,

they can completely overwhelm the:

$$
O(k^{-2})
$$

exponent gain.

Therefore:

$$
\boxed{
\text{vanishing exponent gap}
\not\Rightarrow
\text{automatic regularity}.
}
$$

This is perfectly consistent with the fact that the Grujić–Xu theorem itself requires elaborate chain dynamics.

---

# 53. C5-H final derivative audit

Current derivative route:

### Fixed $k$

Genuinely theorem-ready:

$$
\boxed{
\mathfrak G_k^{dir}\le1
+
\text{admissible time}
\Rightarrow
\text{regularity}.
}
$$

### Large $k$

Static volume escalation:

$$
\boxed{
\text{NO-GO as automatic route}.
}
$$

### Correct high-order route

$$
\boxed{
\text{Grujić--Xu chain-normalized dynamic interpolation}.
}
$$

### New C5 role

Track:

$$
\boxed{
\text{chain sign-geometry defects}
}
$$

rather than continuing to track:

$$
V_k^{eff}
$$

in isolation.

---

# 54. Major no-go audit

### NG-H1

$$
\mathfrak G_k^{dir}>1
\ \forall k
\Rightarrow
\text{contradiction}.
$$

FALSE.

### NG-H2

$$
k\to\infty
\Rightarrow
\text{direct gate improves automatically}.
$$

FALSE due to $2^{-k}$ and $4^{-k}$ factors.

### NG-H3

$$
L^2\text{ derivative log-convexity}
\Rightarrow
\text{effective volume shrinks}.
$$

FALSE.

### NG-H4

$$
\Lambda_k\uparrow
\Rightarrow
\mathfrak N_k\text{ bounded}.
$$

FALSE.

### NG-H5

$$
\text{volume-only chain certificate}
\Rightarrow
\text{captures Theorem 3.14 asymptotic mechanism}.
$$

FALSE / too coarse.

### NG-H6

$$
\text{vanishing exponent gap}
\Rightarrow
\text{automatic theorem closure}.
$$

FALSE; constants, timing, sign geometry, and chain structure remain.

---

# 55. X-Integration guards update

## G-DIRFIX

Theorem 3.5 acts as a fixed-order kill switch;

one must not treat $k\to\infty$ as an automatic ladder.

## G-L2LOG

$L^2$ log-convexity only controls the spectral moment ladder.

## G-SPECMULT

Effective volume preserves:

$$
\Lambda_k^{-3}
\times
\mathfrak N_k.
$$

## G-CHAINR

High-order derivative amplitude uses the published:

$$
\mathcal R(k,c,t).
$$

## G-VOLCHAIN

The global-volume certificate must not masquerade as the full sign/harmonic-measure geometry of Theorem 3.14.

## G-GAINEXP

Asymptotic concentration gain must simultaneously preserve the theorem constant burden.

## G-DYNINT

High-$k$ closure must pivot to dynamic interpolation / chain states.

---

# 56. True ETN update

C5-H all-order derivative state:

$$
\boxed{
\Theta^{H}_{j,i}
=
\left\langle
\mathcal R_{j,m_i},
\Lambda_{j,m_i},
\mathfrak N_{j,m_i},
\varepsilon_{j,m_i}^{eff},
\mathsf{Sign}_{j,i},
\mathsf{Time}_{j,i},
\mathsf{ChainType}_{j,i}
\right\rangle.
}
$$

Block sections:

$$
\ell_{i+1}\ge2\ell_i.
$$

---

# 57. C5 strategic status

C5-A:

$$
\text{motif compactness}.
$$

C5-B:

$$
\text{temporal Young oscillation/concentration}.
$$

C5-C:

$$
\text{temporal cross-curvature}.
$$

C5-D:

$$
\text{spatial–matrix incompatibility}.
$$

C5-E:

$$
Q\to\text{gap/derivative/vorticity defects}.
$$

C5-F:

$$
\text{axis/pressure + derivative escalation}.
$$

C5-G:

$$
\text{theorem-ready fixed-order direct gate}.
$$

C5-H:

$$
\boxed{
\textbf{all-order static-volume escalation NO-GO}
}
$$

and repositions the true high-order frontier as:

$$
\boxed{
\textbf{derivative sign geometry + dynamic chain compatibility}.
}
$$

---

# 58. New frontier: C5-I

Formally the next topic:

$$
\boxed{
\textbf{C5-I — Derivative Sign-Geometry Defects,
Chain Sections, and Harmonic-Measure Compatibility}.
}
$$

---

# 59. C5-I proof obligations

## I1 — Sectionwise sign-geometry state

For Grujić–Xu sections:

$$
[\ell_i,\ell_{i+1}],
$$

at the maxima:

$$
m_i
$$

preserve the selected component/sign high-set line geometry.

## I2 — 1D occupancy measure

No longer just preserving total volume,

but preserving:

$$
\boxed{
\text{line-intersection occupancy distributions}.
}
$$

## I3 — Harmonic-measure compatibility

Transform:

- line sparseness;
- analytic radius;
- harmonic-measure majorization;

into compact motif constraints.

## I4 — Type-A / Type-B strings

Directly incorporate the section types from Grujić–Xu Definition 3.15 into the C5 recurrent state.

## I5 — Multiplicity vs sign oscillation

If:

$$
\mathfrak N_k\gg1,
$$

investigate whether it must translate into:

- many line crossings;
- or stronger sign alternation.

## I6 — Chain timing synchronization

Synchronize:

$$
\tau_{chain,k}
$$

with the C5 record-window normalized time state.

## I7 — Dynamic interpolation defect

If Theorem 3.14 never closes,

extract the:

$$
\boxed{
\text{recurrent Type-A/B + sign-geometry defect motif}.
}
$$

## I8 — Theorem 3.14 exact audit

Strictly use the published hypotheses,

to determine which C5 compact states are genuinely sufficient to trigger the asymptotic-critical theorem.

---

# 60. Formal status

$$
\boxed{
\begin{aligned}
\text{Theorem 3.5 direct }2^{-k},4^{-k}\text{ audit}
&:\ \mathrm{VERIFIED},\\
\text{all-order direct automatic closure}
&:\ \mathrm{FALSE/NO\mbox{-}GO},\\
L^2\text{ Fourier moment log-convexity}
&:\ \mathrm{PROVED},\\
\text{spectral frequency monotonicity}
&:\ \mathrm{PROVED},\\
\text{Agmon spectral-cell multiplicity factorization}
&:\ \mathrm{PROVED},\\
\mathfrak N_k\gtrsim1
&:\ \mathrm{PROVED},\\
\text{chain volume-gate factorization}
&:\ \mathrm{PROVED},\\
\text{volume-only chain closure}
&:\ \mathrm{FALSE\ AS\ GENERAL\ AUTOMATIC\ ROUTE},\\
\text{Theorem 3.14 chain amplitude }\mathcal R
&:\ \mathrm{EXTERNAL/VERIFIED},\\
\text{chain exponent gap }1/((k+1)(2k+3))
&:\ \mathrm{PROVED/EXTERNAL\ SCALES},\\
\text{fixed-power concentration gain beats exponent gap}
&:\ \mathrm{PROVED\ CONDITIONAL\ ON\ CONSTANT\ BURDEN},\\
\text{asymptotic a-priori saturation defect}
&:\ \mathrm{DEFINED},\\
\text{static all-order effective-volume closure program}
&:\ \mathrm{CLOSED\ AS\ NO\mbox{-}GO},\\
\text{dynamic sign-geometry chain closure}
&:\ \mathrm{OPEN/NEXT},\\
\text{global regularity}
&:\ \mathrm{OPEN}.
\end{aligned}
}
$$

---

# 61. Conclusion

C5-G provided the:

$$
\boxed{
\text{fixed-}k\text{ theorem-ready direct gate}.
}
$$

C5-H now answers:

> Can we escalate this gate all the way to $k\to\infty$ and resolve it via an all-order effective-volume contradiction?

The answer:

$$
\boxed{
\textbf{No.}
}
$$

Theorem 3.5 itself contains a:

$$
2^{-k}
$$

spatial factor and a:

$$
4^{-k}
$$

temporal factor.

Even a smooth single-scale analytic profile can cause:

$$
\mathfrak G_k^{dir}\to\infty.
$$

Thus, the high-$k$ direct gate is not an automatic ladder.

After incorporating $L^2$ spectral moments,

we obtain:

$$
\boxed{
M_k^2
\le
M_{k-1}M_{k+1},
}
$$

So the spectral frequency:

$$
\Lambda_k
$$

is monotone.

But the effective radius exactly decomposes as:

$$
\boxed{
r_{eff,k}
=
\mathfrak N_k^{1/3}
\Lambda_k^{-1}.
}
$$

where:

$$
\mathfrak N_k
$$

is the spectral-cell multiplicity,

and log-convexity does not control it at all.

Therefore:

$$
\boxed{
\text{high spectral frequency}
\not\Rightarrow
\text{physical concentration}.
}
$$

For the Grujić–Xu chain scale:

$$
\boxed{
\mathfrak G_k^{chain,vol}
=
2
\widetilde{\mathcal C}_k
\mathfrak N_k^{1/3}
\frac{
A_k^{1/(k+1)}
}{
\Lambda_k
}.
}
$$

Furthermore:

$$
A_k^{1/(k+1)}
=
c^{k/(k+1)}
(k!)^{1/(k+1)}
\mathcal R(k,c,t).
$$

So we have finally connected the:

$$
\boxed{
\text{derivative chain amplitude}
}
$$

and the:

$$
\boxed{
\text{spectral frequency + physical multiplicity}
}
$$

into the same all-order state.

But the volume-only certificate remains too coarse;

even an uncertainty-limited smooth packet cannot generally achieve the high-order 1D sparseness scale of the chain theorem.

The true asymptotic-critical exponent gap:

$$
\boxed{
\frac1{k+1}
-
\frac2{2k+3}
=
\frac1{
(k+1)(2k+3)
}
}
$$

indeed tends to zero.

Therefore, any fixed-power concentration improvement is eventually sufficient to overcome the exponent burden—**provided that theorem constants and timing do not dominate**.

Thus, what a high-order hypothetical survivor truly must maintain is not "all norms being large", but rather:

$$
\boxed{
\text{A-Priori Saturation}
\vee
\text{Spectral-Cell Multiplicity}
\vee
\text{Sign-Geometry Defect}
\vee
\text{Chain/Time Defect}.
}
$$

This indicates that the C5 all-order volume route is now complete.

The next round must genuinely delve into the core of the original Grujić–Xu paper, which we have yet to compactify:

$$
\boxed{
\textbf{component/sign 1D microgeometry}
+
\textbf{Type-A/Type-B derivative chains}
+
\textbf{harmonic-measure compatibility}.
}
$$

Formally the next paper:

$$
\boxed{
\textbf{C5-I — Derivative Sign-Geometry Defects,
Chain Sections, and Harmonic-Measure Compatibility}.
}
$$

---

# References

1. Z. Grujić, L. Xu, *Asymptotic Criticality of the Navier–Stokes Regularity Problem*, Journal of Mathematical Fluid Mechanics 26, Article 53 (2024), DOI: 10.1007/s00021-024-00888-x; arXiv:1911.00974.
2. L. Nirenberg, *On elliptic partial differential equations*, Ann. Scuola Norm. Sup. Pisa 13 (1959), 115–162.
3. Z. Grujić, *A geometric measure-type regularity criterion for solutions to the 3D Navier–Stokes equations*, Nonlinearity 26 (2013), 289–296.
4. R. Guberović, *Smoothness of Koch–Tataru solutions to the Navier–Stokes equations revisited*, Discrete Contin. Dyn. Syst. 27 (2010), 231–236.

# Internal dependencies

- `NS_C5G_PressureSignature_VorticityComplement_FixedOrderGate_v0.1.md`
- `NS_C5F_AxisPressureSignature_DerivativeGateEscalation_v0.1.md`
- `NS_C5E_StrainDirection_MiddleGap_DerivativeIntermittency_v0.1.md`
- `NS_C5D_SpatialMatrix_StrongMiddleQuadraticPressureObstruction_v0.1.md`
- `NS_C5C_TemporalCorrelation_CrossCurvatureOrdering_v0.1.md`
- `NS_C5B_TemporalYoung_PulsePhaseCompatibility_v0.1.md`
- `NS_C5A_RecordWindow_MotifCompactness_v0.1.md`
- `NS_C4J_CompensationRigidity_FinalSynchronizationAudit_v0.1.md`
- `NS_C3Y_DerivativeChain_IntermittencyTradeoff_v0.1.md`
- `True ETN / Infinite-Dimensional Tension Field`
- `X_Integral_Unified_Program_v0.2.md`

Next:

$$
\boxed{
\textbf{C5-I — Derivative Sign-Geometry Defects,
Chain Sections, and Harmonic-Measure Compatibility}
}
$$