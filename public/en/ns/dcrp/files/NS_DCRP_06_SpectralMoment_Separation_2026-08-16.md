# NS-DCRP-06 — Spectral-Moment Separation, Hellinger Rigidity, and the Derivative-Carrier Boundary

- date: 2026-08-16
- status: research proof checkpoint
- canonical source: UTF-8 Markdown
- canonical math delimiters: `$...$` and `$$...$$`
- objective: attack the DCRP-05 frontier $\beta_{SV}\to0$ and determine exactly what kind of frequency reprofile it forces.
- no full Navier--Stokes regularity claim is made.
- primary external source checked: Evan Miller, arXiv:2407.02691v2, especially Theorems 1.8, 1.9, 1.12, 1.13 and Proposition 1.1.

---

# 1. Executive result

DCRP-05 reduced near-saturation of the old Miller model cone to

$$
\boxed{
\beta_{SV}\to0,
}
$$

where

$$
\beta_{SV}
=
\frac{
\|S\|_{\dot H^1}^2
}{
\|S\|_2
\|-\Delta S\|_2
}.
$$

The initial goal was to prove:

> $\beta_{SV}\to0$ forces a fixed positive fraction of the original strain-energy carrier to move to a remote high-frequency profile.

That statement is false in general.

A two-scale counterexample shows that

$$
\beta_{SV}\to0
$$

may be produced by a high-frequency component whose **base $L^2$ strain mass tends to zero**.

However, the derivative-weighted carrier behaves in the opposite way.

The exact replacement theorem is:

$$
\boxed{
\beta_{SV}
=
\operatorname{Aff}
(
\mu_E,\mu_Z
),
}
$$

where

$$
\mu_E
$$

is the normalized strain-energy spectral measure and

$$
\mu_Z
$$

is the normalized Laplacian-energy spectral measure.

Thus

$$
\boxed{
\beta_{SV}\to0
}
$$

means that these two derivative-level spectral carriers become asymptotically mutually singular.

More quantitatively, define

$$
x_E
=
\frac HE,
$$

$$
x_Z
=
\frac{Z^2}{H},
$$

where

$$
E=\|S\|_2^2,
\qquad
H=\|S\|_{\dot H^1}^2,
\qquad
Z=\|-\Delta S\|_2.
$$

Then

$$
\boxed{
\frac{x_Z}{x_E}
=
\beta_{SV}^{-2}.
}
$$

For the choice

$$
L=\beta_{SV}^{-1/2},
$$

at least

$$
1-\sqrt{\beta_{SV}}
$$

of the $E$-carrier lies below

$$
Lx_E,
$$

while at least

$$
1-\sqrt{\beta_{SV}}
$$

of the $Z$-carrier lies above

$$
x_Z/L.
$$

These two frequency-squared thresholds differ by the factor

$$
\boxed{
\beta_{SV}^{-1}.
}
$$

Equivalently, the corresponding frequency radii differ by

$$
\boxed{
\beta_{SV}^{-1/2}.
}
$$

A second new estimate shows that during any time at which

$$
H'(t)\ge0,
$$

the high derivative scale cannot run arbitrarily faster than the enstrophy amplitude:

$$
\boxed{
\frac{Z^2}{H}
\le
C E^2.
}
$$

and

$$
\boxed{
\frac HE
\le
C\beta_{SV}^2E^2.
}
$$

Thus the $\beta_{SV}\to0$ escape is now confined to a precise configuration:

> a vanishing-$E$-mass ultraviolet tail must carry an asymptotically dominant fraction of the $Z$-mass, while nonlinear transfer must continually compensate its viscous high-frequency loss.

The next proof target is therefore a **Low--High Interaction Tax Lemma**, not another generic diffuse-carrier theorem.

---

# 2. External calibration: Miller's approximate-eigenfunction criterion

Miller's 2026 revision contains the $q=2$ specialization

$$
\boxed{
\int_0^{T_{\max}}
\left(
1-
\frac{
\|S\|_{\dot H^1}^4
}{
\|S\|_2^2
\|-\Delta S\|_2^2
}
\right)^2
\|S\|_2^4
\,dt
=
+\infty
}
\tag{2.1}
$$

for finite-time blowup in the stated mild-solution class.

Therefore the parameter used in DCRP-05 is exactly

$$
\boxed{
\beta_{SV}^2
=
\frac{
\|S\|_{\dot H^1}^4
}{
\|S\|_2^2
\|-\Delta S\|_2^2
}.
}
\tag{2.2}
$$

Miller also proves a regularity criterion based on

$$
\inf_{\rho\in\mathbb R}
\|-\rho\Delta S-S\|_{L^q}.
$$

For

$$
q=2,
$$

the minimization can be computed exactly:

$$
\boxed{
\inf_{\rho\in\mathbb R}
\|-\rho\Delta S-S\|_2^2
=
E
\left(
1-\beta_{SV}^2
\right).
}
\tag{2.3}
$$

Indeed,

$$
\|-\rho\Delta S-S\|_2^2
=
\rho^2Z^2
-
2\rho H
+
E,
$$

whose minimum occurs at

$$
\rho_\ast
=
\frac H{Z^2}.
$$

Hence:

- $\beta_{SV}\approx1$ means the strain is close, in this $L^2$ sense, to a Laplacian eigenfunction shell;
- $\beta_{SV}\to0$ is the opposite extreme.

No novelty claim is made for the appearance of $1-\beta_{SV}^2$; it is already explicit in Miller's Theorem 1.12.

The new task here is to resolve its spectral-measure meaning inside the MORP/DCRP route.

---

# 3. Three canonical spectral measures

Let

$$
X(\xi)
=
|\xi|^2.
$$

Assume

$$
0<E,H,Z<\infty.
$$

Define the strain-energy probability measure

$$
\boxed{
d\mu_E(\xi)
=
\frac{
|\widehat S(\xi)|^2
}{
E
}
\,d\xi.
}
\tag{3.1}
$$

Define the $\dot H^1$ probability measure

$$
\boxed{
d\mu_H(\xi)
=
\frac{
X(\xi)
|\widehat S(\xi)|^2
}{
H
}
\,d\xi.
}
\tag{3.2}
$$

Define the Laplacian-energy probability measure

$$
\boxed{
d\mu_Z(\xi)
=
\frac{
X(\xi)^2
|\widehat S(\xi)|^2
}{
Z^2
}
\,d\xi.
}
\tag{3.3}
$$

All three are generated directly by the same physical state.

No dangerous-certificate mark is inserted.

---

# 4. NEW THEOREM — Hellinger identity

## Theorem 4.1

The Hellinger / Bhattacharyya affinity of

$$
\mu_E
$$

and

$$
\mu_Z
$$

is exactly

$$
\boxed{
\operatorname{Aff}
(
\mu_E,\mu_Z
)
=
\beta_{SV}.
}
\tag{4.1}
$$

Moreover,

$$
\boxed{
d\mu_H
=
\frac1{\beta_{SV}}
\sqrt{
d\mu_E\,d\mu_Z
}.
}
\tag{4.2}
$$

### Proof

Using the common Lebesgue reference measure,

$$
\sqrt{
\frac{
|\widehat S|^2
}{
E
}
\frac{
X^2|\widehat S|^2
}{
Z^2
}
}
=
\frac{
X|\widehat S|^2
}{
\sqrt E\,Z
}.
$$

Integrating,

$$
\operatorname{Aff}
(
\mu_E,\mu_Z
)
=
\frac{
\int X|\widehat S|^2
}{
\sqrt E\,Z
}
=
\frac H{\sqrt E\,Z}
=
\beta_{SV}.
$$

Also,

$$
\frac1{\beta_{SV}}
\frac{
X|\widehat S|^2
}{
\sqrt E\,Z
}
=
\frac{
X|\widehat S|^2
}{
H
},
$$

which is exactly

$$
d\mu_H.
$$

$$
\square
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 5. Corollary — asymptotic derivative-level mutual singularity

Let

$$
d_{\rm TV}
(
\mu_E,\mu_Z
)
$$

denote total variation distance.

For probability measures,

$$
1-
\operatorname{Aff}(\mu_E,\mu_Z)
\le
d_{\rm TV}(\mu_E,\mu_Z).
$$

Hence Theorem 4.1 gives

$$
\boxed{
d_{\rm TV}
(
\mu_E,\mu_Z
)
\ge
1-\beta_{SV}.
}
\tag{5.1}
$$

Therefore:

$$
\boxed{
\beta_{SV}\to0
\Longrightarrow
d_{\rm TV}
(
\mu_E,\mu_Z
)
\to1.
}
\tag{5.2}
$$

Thus the two derivative-level carriers become asymptotically mutually singular.

This is stronger than saying that the variance of frequency grows.

It identifies two explicit state-generated probability measures that separate.

---

# 6. Adjacent Rayleigh frequency scales

Define

$$
\boxed{
x_E
=
\frac HE
=
\mathbb E_{\mu_E}[X],
}
\tag{6.1}
$$

and

$$
\boxed{
x_Z
=
\frac{Z^2}{H}.
}
\tag{6.2}
$$

Then

$$
\frac{x_Z}{x_E}
=
\frac{
EZ^2
}{
H^2
}
=
\beta_{SV}^{-2}.
$$

Hence:

$$
\boxed{
x_Z
=
\beta_{SV}^{-2}x_E.
}
\tag{6.3}
$$

If the corresponding frequency radii are

$$
\kappa_E
=
\sqrt{x_E},
$$

$$
\kappa_Z
=
\sqrt{x_Z},
$$

then

$$
\boxed{
\frac{
\kappa_Z
}{
\kappa_E
}
=
\beta_{SV}^{-1}.
}
\tag{6.4}
$$

Thus $\beta_{SV}$ itself is the inverse adjacent-Sobolev spectral scale ratio.

---

# 7. NEW THEOREM — quantitative two-carrier separation

## Theorem 7.1

Let

$$
L>1.
$$

Then

$$
\boxed{
\mu_E
\left(
X\ge Lx_E
\right)
\le
\frac1L.
}
\tag{7.1}
$$

and

$$
\boxed{
\mu_Z
\left(
X\le\frac{x_Z}{L}
\right)
\le
\frac1L.
}
\tag{7.2}
$$

### Proof of (7.1)

By Markov:

$$
\mu_E
(
X\ge Lx_E
)
\le
\frac{
\mathbb E_{\mu_E}[X]
}{
Lx_E
}
=
\frac1L.
$$

### Proof of (7.2)

On

$$
X\le\frac{x_Z}{L},
$$

one has

$$
X^2
\le
\frac{x_Z}{L}X.
$$

Therefore

$$
\mu_Z
\left(
X\le\frac{x_Z}{L}
\right)
=
\frac{
E
\int_{\{X\le x_Z/L\}}
X^2
|\widehat S|^2/E
}{
Z^2
}.
$$

Equivalently using

$$
\mathbb E_{\mu_E}[X^2]
=
\frac{Z^2}{E}
=
x_Ex_Z,
$$

$$
\mu_Z
\left(
X\le\frac{x_Z}{L}
\right)
\le
\frac{
(x_Z/L)x_E
}{
x_Ex_Z
}
=
\frac1L.
$$

$$
\square
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 8. Corollary — diverging empty spectral corridor

Choose

$$
\boxed{
L
=
\beta_{SV}^{-1/2}.
}
\tag{8.1}
$$

Then:

$$
\boxed{
\mu_E
\left(
X<
\frac{x_E}{\sqrt{\beta_{SV}}}
\right)
\ge
1-\sqrt{\beta_{SV}}.
}
\tag{8.2}
$$

and

$$
\boxed{
\mu_Z
\left(
X>
x_Z\sqrt{\beta_{SV}}
\right)
\ge
1-\sqrt{\beta_{SV}}.
}
\tag{8.3}
$$

The two threshold values satisfy

$$
\frac{
x_Z\sqrt{\beta_{SV}}
}{
x_E/\sqrt{\beta_{SV}}
}
=
\beta_{SV}
\frac{x_Z}{x_E}
=
\beta_{SV}^{-1}.
$$

Therefore the frequency-squared gap is

$$
\boxed{
\beta_{SV}^{-1},
}
\tag{8.4}
$$

and the ordinary frequency gap is

$$
\boxed{
\beta_{SV}^{-1/2}.
}
\tag{8.5}
$$

So as

$$
\beta_{SV}\to0,
$$

almost all of the $E$-carrier lies below one scale and almost all of the $Z$-carrier lies above a scale separated from it by an unbounded factor.

---

# 9. NO-GO — base-carrier fixed-share reprofile is false

The original proposed Moment-Reprofile Lemma would have required that

$$
\beta_n\to0
$$

forces a fixed positive fraction of

$$
\mu_{E,n}
$$

to occur at a remote high frequency.

This is false.

Let

$$
\epsilon_n\downarrow0
$$

and consider the model spectral probability measure

$$
\boxed{
\mu_{E,n}
=
(1-\epsilon_n)\delta_1
+
\epsilon_n\delta_{\epsilon_n^{-2}}.
}
\tag{9.1}
$$

Then:

$$
\mathbb E[X]
=
1-\epsilon_n
+
\epsilon_n^{-1}
\sim
\epsilon_n^{-1},
$$

and

$$
\mathbb E[X^2]
=
1-\epsilon_n
+
\epsilon_n^{-3}
\sim
\epsilon_n^{-3}.
$$

Thus

$$
\beta_n
=
\frac{
\mathbb E[X]
}{
\sqrt{
\mathbb E[X^2]
}
}
\sim
\sqrt{\epsilon_n}
\to0.
$$

But the high-frequency base mass is only

$$
\boxed{
\epsilon_n\to0.
}
$$

On the other hand the associated

$$
\mu_Z
$$

mass at the high point tends to one.

Thus:

$$
\boxed{
\beta_n\to0
\not\Rightarrow
\text{fixed positive remote share in }\mu_{E,n}.
}
\tag{9.2}
$$

Any proof route requiring this implication is invalid.

The correct carrier for the ultraviolet side is derivative-weighted.

Status:

$$
\boxed{
\textbf{NO-GO PROVED at the spectral-measure level}.
}
$$

The same two-scale pattern can be approximated by smooth Fourier packets supported on separated annuli, so this is not an artifact of atomic notation.

---

# 10. Derivative-shell atom/diffuse dichotomy

Let

$$
A_j
=
\{
2^j\le|\xi|<2^{j+1}
\}
$$

be dyadic shells.

Define the Laplacian-energy shell shares

$$
\boxed{
c_j^{(Z)}
=
\mu_Z(A_j).
}
\tag{10.1}
$$

Then

$$
c_j^{(Z)}\ge0,
$$

and

$$
\sum_j
c_j^{(Z)}
=
1.
$$

For any sequence of states there are only two possibilities after subsequence extraction.

### Atomic derivative carrier

There exists

$$
\eta_0>0
$$

and shells

$$
j_n
$$

such that

$$
\boxed{
c_{j_n}^{(Z)}
\ge
\eta_0.
}
\tag{10.2}
$$

### Diffuse derivative carrier

$$
\boxed{
\sup_j
c_{j}^{(Z)}
\to0.
}
\tag{10.3}
$$

In the diffuse case, define

$$
\mathfrak M_Z
=
\left(
\sum_j
(c_j^{(Z)})^2
\right)^{-1}.
$$

Because

$$
\sum_j(c_j^{(Z)})^2
\le
\sup_jc_j^{(Z)}
\sum_jc_j^{(Z)}
=
\sup_jc_j^{(Z)},
$$

one has

$$
\boxed{
\mathfrak M_Z\to\infty.
}
\tag{10.4}
$$

Similarly the Shannon entropy satisfies

$$
\mathfrak H_Z
\ge
-\log
\sum_j
(c_j^{(Z)})^2,
$$

so

$$
\boxed{
\mathfrak H_Z\to\infty.
}
\tag{10.5}
$$

This is a derivative-weighted analogue of the MORP-05 atomic/diffuse split.

No claim is yet made that a fixed $Z$-shell atom automatically yields a nonzero actual Navier--Stokes state profile under symmetry-only normalization.

That bridge remains to be proved.

---

# 11. Exact bridge measure

The middle measure

$$
\mu_H
$$

is not independent.

Theorem 4.1 gives

$$
\boxed{
d\mu_H
=
\frac1{\beta_{SV}}
\sqrt{
d\mu_Ed\mu_Z
}.
}
\tag{11.1}
$$

Thus the $\dot H^1$ carrier is precisely the normalized geometric overlap of the two increasingly separated endpoint derivative carriers.

Consequently:

$$
\boxed{
\beta_{SV}\to0
}
$$

means that the middle Sobolev carrier is supported by an asymptotically small overlap set after renormalization.

This provides a precise interpretation of why weak base-carrier compactness can miss the relevant ultraviolet defect.

---

# 12. Nonlinear compensation estimate

The previous sections are purely spectral.

Now use the Navier--Stokes dynamics.

Let

$$
Q
=
P_{st}
\left(
(u\cdot\nabla)S
+
S^2
+
\frac34\omega\otimes\omega
\right).
$$

For sufficiently regular solutions,

$$
\boxed{
\|Q\|_2
\le
C
\left[
E^{1/2}
H^{1/4}
Z^{1/2}
+
E^{1/4}
H^{3/4}
\right].
}
\tag{12.1}
$$

### Proof

Because

$$
P_{st}
$$

is an $L^2$ orthogonal projection,

$$
\|Q\|_2
\le
\|(u\cdot\nabla)S\|_2
+
\left\|
S^2+\frac34\omega\otimes\omega
\right\|_2.
$$

For the transport term,

$$
\|(u\cdot\nabla)S\|_2
\le
\|u\|_6
\|\nabla S\|_3.
$$

Sobolev and the strain--velocity isometry give

$$
\|u\|_6
\le
C\|\nabla u\|_2
\le
C E^{1/2}.
$$

Interpolation gives

$$
\|\nabla S\|_3
\le
C
\|\nabla S\|_2^{1/2}
\|\nabla S\|_6^{1/2}
\le
C
H^{1/4}
Z^{1/2}.
$$

Thus

$$
\|(u\cdot\nabla)S\|_2
\le
C
E^{1/2}
H^{1/4}
Z^{1/2}.
$$

For the algebraic terms,

$$
\|S^2\|_2
\le
\|S\|_4^2
\le
C
E^{1/4}
H^{3/4}.
$$

The same bound holds for

$$
\omega\otimes\omega
$$

using boundedness of the strain--vorticity zero-order singular integral on

$$
L^4.
$$

This proves (12.1).

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 13. NEW THEOREM — growth-time spectral pinning

Define the scale-invariant shape parameter

$$
\boxed{
\mathfrak R
=
\frac{
H
}{
E^3
}.
}
\tag{13.1}
$$

## Theorem 13.1

At every sufficiently regular time for which

$$
H'(t)\ge0,
$$

one has

$$
\boxed{
\mathfrak R
\le
C_0
\beta_{SV}^2
(1-\beta_{SV}^2)^2
(1+\sqrt{\beta_{SV}})^4.
}
\tag{13.2}
$$

In particular,

$$
\boxed{
\mathfrak R
\le
C_1\beta_{SV}^2.
}
\tag{13.3}
$$

Consequently,

$$
\boxed{
\frac{
Z^2
}{
H
}
\le
C_1E^2,
}
\tag{13.4}
$$

and

$$
\boxed{
\frac HE
\le
C_1
\beta_{SV}^2
E^2.
}
\tag{13.5}
$$

### Proof

DCRP-05 proved the transverse growth estimate

$$
\frac12H'
\le
-Z^2
+
\sqrt{
1-\beta_{SV}^2
}
Z\|Q\|_2.
$$

If

$$
H'\ge0,
$$

then

$$
Z
\le
\sqrt{
1-\beta_{SV}^2
}
\|Q\|_2.
$$

Use (12.1):

$$
1
\le
C
\sqrt{
1-\beta_{SV}^2
}
\left[
E^{1/2}
H^{1/4}
Z^{-1/2}
+
E^{1/4}
H^{3/4}
Z^{-1}
\right].
$$

Since

$$
\beta_{SV}
=
\frac H{\sqrt E\,Z},
$$

one obtains

$$
E^{1/2}
H^{1/4}
Z^{-1/2}
=
\beta_{SV}^{1/2}
\mathfrak R^{-1/4},
$$

and

$$
E^{1/4}
H^{3/4}
Z^{-1}
=
\beta_{SV}
\mathfrak R^{-1/4}.
$$

Therefore

$$
1
\le
C
\sqrt{
1-\beta_{SV}^2
}
\mathfrak R^{-1/4}
\left(
\sqrt{\beta_{SV}}
+
\beta_{SV}
\right).
$$

Raise to the fourth power:

$$
\mathfrak R
\le
C_0
(1-\beta_{SV}^2)^2
\left(
\sqrt{\beta_{SV}}
+
\beta_{SV}
\right)^4.
$$

Since

$$
\left(
\sqrt\beta+\beta
\right)^4
=
\beta^2
(1+\sqrt\beta)^4,
$$

(13.2) follows.

Now

$$
\beta_{SV}^2
=
\frac{
H^2
}{
EZ^2
}
$$

implies

$$
\frac{Z^2}{H}
=
\frac{
H
}{
E\beta_{SV}^2
}
=
\frac{
\mathfrak R
}{
\beta_{SV}^2
}
E^2.
$$

Apply (13.3) to obtain (13.4).

Also,

$$
\frac HE
=
\mathfrak R E^2,
$$

which gives (13.5).

$$
\square
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 14. Interpretation of growth-time pinning

Let

$$
\kappa_E
=
\sqrt{
H/E
},
$$

and

$$
\kappa_Z
=
\sqrt{
Z^2/H
}.
$$

At

$$
H'\ge0,
$$

Theorem 13.1 gives

$$
\boxed{
\kappa_Z
\le
C E,
}
\tag{14.1}
$$

and

$$
\boxed{
\kappa_E
\le
C\beta_{SV}E.
}
\tag{14.2}
$$

while the exact identity

$$
\kappa_Z/\kappa_E
=
\beta_{SV}^{-1}
$$

still holds.

Therefore the derivative-scale separation can grow only by pushing the lower characteristic strain scale downward relative to the enstrophy amplitude while the upper derivative scale remains bounded by the natural amplitude scale

$$
E.
$$

This is a dynamical restriction that is absent from the purely spectral counterexample of Section 9.

---

# 15. Finite kinetic-energy lower bound on $\beta$ during $H$ growth

Let

$$
K(t)
=
\|u(t)\|_2^2.
$$

Fourier Cauchy--Schwarz and the strain--velocity isometry give

$$
\boxed{
H
\ge
\frac{
2E^2
}{
K
}.
}
\tag{15.1}
$$

Indeed,

$$
\|\nabla u\|_2^4
\le
\|u\|_2^2
\|\Delta u\|_2^2,
$$

while

$$
\|\nabla u\|_2^2
=
2E,
$$

and

$$
\|\Delta u\|_2^2
=
2H.
$$

Combining (15.1) with (13.5) at a time with

$$
H'\ge0,
$$

$$
\frac{
2E
}{
K
}
\le
\frac HE
\le
C_1
\beta_{SV}^2
E^2.
$$

Hence:

$$
\boxed{
\beta_{SV}^2E
\ge
\frac{
c
}{
K
}.
}
\tag{15.2}
$$

Since kinetic energy is nonincreasing,

$$
K(t)\le K(0),
$$

one gets the uniform growth-time constraint

$$
\boxed{
H'(t)\ge0
\Longrightarrow
E(t)
\ge
\frac{
c
}{
K(0)\beta_{SV}(t)^2
}.
}
\tag{15.3}
$$

Thus extreme spectral-moment separation during actual $\dot H^1$ growth is possible only at correspondingly large enstrophy.

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 16. Temporal sparsity of extreme-dispersion growth times

For a smooth finite-energy Navier--Stokes solution,

$$
\frac12
\frac d{dt}
K(t)
+
\|\nabla u(t)\|_2^2
=
0.
$$

Since

$$
\|\nabla u\|_2^2
=
2E,
$$

$$
\int_0^T
E(t)\,dt
\le
\frac{
K(0)
}{
4
}.
$$

Define

$$
\boxed{
A_\epsilon
=
\left\{
t:
H'(t)\ge0,
\quad
\beta_{SV}(t)\le\epsilon
\right\}.
}
\tag{16.1}
$$

By (15.3), for

$$
t\in A_\epsilon,
$$

$$
E(t)
\ge
\frac{
c
}{
K(0)\epsilon^2
}.
$$

Therefore

$$
\frac{
c
}{
K(0)\epsilon^2
}
|A_\epsilon|
\le
\int_{A_\epsilon}
E(t)\,dt
\le
\frac{
K(0)
}{
4
}.
$$

Hence

$$
\boxed{
|A_\epsilon|
\le
C
K(0)^2
\epsilon^2.
}
\tag{16.2}
$$

So:

$$
\boxed{
\textbf{
times of simultaneous }\dot H^1\textbf{-growth and extreme spectral separation
have Lebesgue measure }O(\epsilon^2).
}
\tag{16.3}
$$

This does not by itself rule out accumulation at a finite singular time.

It is a quantitative sparsity statement.

---

# 17. Why this still does not close Navier--Stokes

The new results do **not** imply that

$$
\beta_{SV}\to0
$$

is impossible.

A singular cascade could in principle use:

- vanishing base $E$-mass at ultraviolet frequencies;
- almost all $Z$-mass in the same ultraviolet tail;
- increasingly large enstrophy;
- increasingly short time intervals;
- nonlinear transfer sufficient to regenerate the high derivative carrier.

The global kinetic-energy budget controls

$$
\int E\,dt,
$$

but not

$$
\int E^2\,dt.
$$

Indeed Miller's Theorem 1.12 is consistent with finite-time blowup requiring divergence of a critical quantity comparable to

$$
\int E^2\,dt
$$

when

$$
\beta_{SV}\to0.
$$

Therefore the present estimates do not yield a contradiction from time integration alone.

This prevents a false closure claim.

---

# 18. What the counterexample teaches about reprofile

The measure-theoretic no-go in Section 9 shows:

$$
\boxed{
\text{fixed high-frequency share of }\mu_E
}
$$

cannot be the required reprofile mechanism.

The correct object must see at least one derivative-weighted measure.

The natural ultraviolet carrier is

$$
\boxed{
\mu_Z.
}
$$

However a fixed positive shell share in

$$
\mu_Z
$$

still does not automatically imply a nonzero Navier--Stokes state profile after **symmetry-only** rescaling.

The shell can carry large derivative weight while its lower-order / critical amplitude vanishes.

Thus the next bridge must be dynamical:

$$
\boxed{
\text{high derivative carrier}
+
\text{required nonlinear compensation}
\Longrightarrow
\text{nonzero interaction cost or actual profile}.
}
$$

---

# 19. Candidate interaction identity

The exact strain balance is

$$
\frac12H'
+
Z^2
=
-
\langle
-\Delta S,Q
\rangle.
$$

On a growth interval,

$$
-\langle
-\Delta S,Q
\rangle
\ge
Z^2.
$$

When

$$
\beta_{SV}\ll1,
$$

Section 8 shows that the vector

$$
-\Delta S
$$

is spectrally concentrated, in derivative weight, far above the bulk of the base strain-energy carrier.

Therefore the right side must be generated by nonlinear interactions that place a comparable amount of

$$
Q
$$

into the ultraviolet region carrying

$$
-\Delta S.
$$

This is the exact location where low--high paraproduct structure should be used.

A viable next lemma must estimate the ultraviolet pairing

$$
\boxed{
-\left<
P_{>N}\Delta S,
P_{>N}Q
\right>
}
\tag{19.1}
$$

with

$$
N
$$

chosen inside the spectral corridor from Section 8.

The objective is to show that if:

- the base $E$-mass above $N$ is vanishing;
- the $Z$-mass above a much larger frequency is fixed;
- no derivative-shell atom can be reprofilied;

then the nonlinear term cannot compensate

$$
Z^2
$$

without paying a positive cross-scale flux / transition cost.

---

# 20. Next exact target — Low--High Interaction Tax Lemma

The next proof target is:

$$
\boxed{
\textbf{Low--High Interaction Tax Lemma}.
}
$$

A useful sufficient form is the following.

Let

$$
N_-(t)<N_+(t)
$$

be thresholds satisfying

$$
\frac{
N_+(t)
}{
N_-(t)
}
\to\infty,
$$

with

$$
\mu_E
(
|\xi|>N_-
)
\to0,
$$

and

$$
\mu_Z
(
|\xi|<N_+
)
\to0.
$$

Prove that one of the following must occur:

1. **derivative reprofile**

   a dyadic high-frequency shell carries a fixed positive fraction of the $Z$-carrier and produces a nonzero actual state/profile after admissible re-rooting;

2. **cross-scale tax**

   the high-frequency nonlinear pairing obeys a positive lower bound in a native scale-invariant flux coordinate;

3. **insufficient compensation**

   the nonlinear high-frequency term cannot satisfy

   $$
   -\langle
   -\Delta S,Q
   \rangle
   \ge
   Z^2,
   $$

   forcing

   $$
   H'<0.
   $$

Any of these closes one part of the $\beta_{SV}\to0$ escape:

- (1) returns to the MORP atomic reprofile mechanism;
- (2) contradicts a true zero-cost minimal return;
- (3) forbids the required strain-$\dot H^1$ growth.

This is now the single state-visible frontier.

---

# 21. Source ledger

## External primary source

Evan Miller, *On the interaction of strain and vorticity for solutions of the Navier--Stokes equation*, arXiv:2407.02691v2, revised 2026-04-13, journal reference Pure Appl. Analysis 8 (2026), 247--270.

Checked facts used in this checkpoint:

- Proposition 1.1:

  $$
  \langle
  S,\omega\otimes\omega
  \rangle
  =
  -\frac43
  \langle
  S^2,S
  \rangle;
  $$

- Theorem 1.8:

  perturbative strain regularity criterion;

- Theorem 1.9:

  finite-time blowup requires

  $$
  \limsup
  \frac{
  \|Q\|_2
  }{
  \|-\Delta S\|_2
  }
  \ge1;
  $$

- Theorem 1.12:

  approximate-Laplacian-eigenfunction regularity criterion;

- $q=2$ specialization:

  $$
  \int
  (1-\beta_{SV}^2)^2E^2
  \,dt
  =
  +\infty
  $$

  under finite-time blowup;

- Theorem 1.13:

  endpoint lower bound for distance from the Laplacian-eigenfunction family.

No novelty or priority claim is made for Miller's established criteria.

The Hellinger-carrier reformulation and the subsequent deductions are internal derivations for this research program and remain subject to independent mathematical audit.

---

# 22. End state

The original target

$$
\beta_{SV}\to0
\Longrightarrow
\text{fixed-share base reprofile}
$$

is false.

The correct exact structure is:

$$
\boxed{
\beta_{SV}
=
\operatorname{Aff}
(
\mu_E,\mu_Z
).
}
$$

Thus:

$$
\boxed{
\beta_{SV}\to0
\Longrightarrow
\mu_E
\text{ and }
\mu_Z
\text{ become asymptotically mutually singular}.
}
$$

Moreover:

$$
\boxed{
\frac{x_Z}{x_E}
=
\beta_{SV}^{-2},
}
$$

and almost all of the two carriers can be separated by an expanding spectral corridor.

During actual

$$
H'\ge0
$$

times, nonlinear compensation forces

$$
\boxed{
\frac{Z^2}{H}
\le
CE^2
}
$$

and

$$
\boxed{
\beta_{SV}^2E
\ge
\frac c{K(0)}.
}
$$

Therefore the only remaining $\beta_{SV}\to0$ mechanism is a vanishing-base-mass but derivative-dominant ultraviolet tail continually regenerated by nonlinear cross-scale transfer.

The next exact target is:

$$
\boxed{
\textbf{
Low--High Interaction Tax Lemma}.
}
$$

No broader diffuse-carrier taxonomy is required.