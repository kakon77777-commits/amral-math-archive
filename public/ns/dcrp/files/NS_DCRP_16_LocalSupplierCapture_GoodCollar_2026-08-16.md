# NS-DCRP-16 — Good-Collar Localization, Forced Dissipation-Wavenumber Continuation, and Local Supplier Capture

- date: 2026-08-16
- status: research proof checkpoint
- canonical source: UTF-8 Markdown
- canonical math delimiters: `$...$` and `$$...$$`
- objective: close the DCRP-15 Local Supplier Capture / Remote-Supplier Decoupling barrier by constructing a divergence-free localization around a first singular point and proving that bounded localized dissipation wavenumber would force local continuation.
- no full Navier--Stokes regularity claim is made.
- principal internal dependencies: DCRP-09 through DCRP-15 supplier/trace modules; MORP local singular-window architecture.
- external primary calibration: Caffarelli--Kohn--Nirenberg partial regularity; Barker--Prange, arXiv:1812.09115v2; Bradshaw--Grujić, arXiv:1501.01043v2; Cheskidov--Dai, arXiv:1507.06611v6.

---

# 1. Executive result

DCRP-15 identified a genuine gap: the dissipation wavenumber used in DCRP-08 was global, so the critical supplier shell could in principle be spatially remote from a chosen singular point.

This round removes that gap at the level of first-singularity localization.

Let

$$
z_\ast=(x_\ast,T)
$$

be a singular point at the first singular time

$$
T<\infty.
$$

The spatial singular set at time $T$ has one-dimensional Hausdorff measure zero. Therefore one can choose arbitrarily small radii

$$
\rho_k\downarrow0
$$

and positive collar widths

$$
\delta_k>0
$$

such that the closed annulus

$$
\boxed{
A_k=
\left\{
x:
\rho_k-\delta_k
\le
|x-x_\ast|
\le
\rho_k+\delta_k
\right\}
}
\tag{1.1}
$$

contains no singular point at time $T$.

Consequently the solution is smooth, with uniform bounds on every derivative, on a spacetime neighborhood of each fixed collar

$$
A_k\times(T-\tau_k,T].
$$

Choose a cutoff $\chi_k$ which equals one on the inner ball and changes only inside the good collar. Use a Bogovskii correction $b_k$ supported in the collar to define

$$
\boxed{
v_k=\chi_k u-b_k,
}
\tag{1.2}
$$

so that

$$
\boxed{\nabla\cdot v_k=0,}
\tag{1.3}
$$

$$
\boxed{v_k=u}
\tag{1.4}
$$

on a smaller ball around $x_\ast$, and $v_k$ is compactly supported.

The localized field satisfies a forced divergence-free Navier--Stokes equation

$$
\boxed{
\partial_t v_k-\nu\Delta v_k+\mathbb P\nabla\cdot(v_k\otimes v_k)=F_k.
}
\tag{1.5}
$$

Because the collar is regular up to $T$, for every fixed $k$,

$$
\boxed{
F_k\in L^2(T-\tau_k,T;L^2(\mathbb R^3)).
}
\tag{1.6}
$$

Define the localized dissipation wavenumber

$$
\Lambda_k(t)=\lambda_{Q_k(t)}
$$

by

$$
\boxed{
\Lambda_k(t)=
\min\left\{
\lambda_q:
\lambda_p^{-1}\|(v_k)_p(t)\|_\infty<c_0\nu
\quad\forall p>q
\right\}.
}
\tag{1.7}
$$

The main forced continuation theorem is:

> If
>
> $$
> \sup_{t\uparrow T}Q_k(t)<\infty,
> $$
>
> then
>
> $$
> v_k\in L_t^\infty H_x^1\cap L_t^2H_x^2
> $$
>
> up to $T$.

Since $v_k=u$ near $x_\ast$, this makes $(x_\ast,T)$ regular, contradiction.

Hence for every good collar $k$,

$$
\boxed{
\limsup_{t\uparrow T}\Lambda_k(t)=+\infty.
}
\tag{1.8}
$$

At each localized dissipation boundary,

$$
\boxed{
\lambda_{Q_k}^{-1}\|(v_k)_{Q_k}\|_\infty\ge c_0\nu.
}
\tag{1.9}
$$

Because the localized field is compactly supported, the transition collar is smooth up to the singular time, and Littlewood--Paley kernels have rapid off-support decay, a sufficiently high boundary shell cannot achieve the lower bound far outside the localization region or inside the smooth transition collar.

Thus the supplier point lies in the inner region where $v_k=u$, up to an error rapidly decaying in relative frequency.

Selecting the supplier frequency sufficiently large yields a point $x_k$, a time $t_k\uparrow T$, and a frequency $\lambda_k\to\infty$ such that

$$
\boxed{
|x_k-x_\ast|\le C\rho_k,
}
\tag{1.10}
$$

and

$$
\boxed{
\lambda_k^{-1}
|
\Delta_{\sim\lambda_k}u(x_k,t_k)
|
\ge
c_{\rm loc}\nu.
}
\tag{1.11}
$$

Since $\rho_k\downarrow0$,

$$
\boxed{x_k\to x_\ast.}
\tag{1.12}
$$

Therefore

$$
\boxed{
\textbf{
every first singular point admits a sequence of actual,
arbitrarily high-frequency, critical supplier atoms whose centers converge to that singular point.
}
}
\tag{1.13}
$$

This closes the physical-space version of Local Supplier Capture.

The DCRP-09 through DCRP-15 supplier/trace machinery can now be re-applied to the original Navier--Stokes field $u$, not merely to a remote global supplier.

The next unresolved interface is narrower:

$$
\boxed{
\textbf{
Local Supplier Sequence}
\Longrightarrow
\textbf{
the same MORP minimal-return / obstruction sequence}.
}
\tag{1.14}
$$

---

# 2. Good radii around a first singular point

Let

$$
\Sigma_T=
\left\{
x\in\mathbb R^3:
(x,T)\text{ is singular}
\right\}.
$$

The Caffarelli--Kohn--Nirenberg theory gives zero one-dimensional parabolic Hausdorff measure for the spacetime singular set. In particular,

$$
\boxed{\mathcal H^1(\Sigma_T)=0.}
\tag{2.1}
$$

Fix $x_\ast\in\Sigma_T$. The map

$$
d_{x_\ast}(x)=|x-x_\ast|
$$

is one-Lipschitz, so

$$
\boxed{
\mathcal H^1
\left(
d_{x_\ast}
(
\Sigma_T\cap\overline{B_R(x_\ast)}
)
\right)=0.
}
\tag{2.2}
$$

For fixed $R$, the bounded time-slice singular set is closed, hence compact, and its distance image is compact.

Therefore there exists a sequence

$$
\boxed{\rho_k\downarrow0}
\tag{2.3}
$$

outside that distance image.

Set

$$
\boxed{
d_k=
\operatorname{dist}
\left(
\rho_k,
d_{x_\ast}(\Sigma_T)
\right)>0,
}
\tag{2.4}
$$

and

$$
\boxed{
\delta_k=
\min\left\{
\frac{d_k}{4},
\frac{\rho_k}{16}
\right\}.
}
\tag{2.5}
$$

Then

$$
\boxed{
A_k=
\left\{
\rho_k-2\delta_k
\le
|x-x_\ast|
\le
\rho_k+2\delta_k
\right\}
}
\tag{2.6}
$$

contains no point of $\Sigma_T$.

Status:

$$
\boxed{\textbf{PROVED}.}
$$

---

# 3. Uniform collar regularity

Every point $(x,T)$ with $x\in A_k$ is regular. The regular set is open in spacetime. Since $A_k$ is compact, finitely many regularity neighborhoods cover $A_k\times\{T\}$.

Therefore there is $\tau_k>0$ and a slightly enlarged collar $A_k^+$ such that

$$
\boxed{
u\text{ is smooth on }A_k^+\times(T-\tau_k,T].
}
\tag{3.1}
$$

For every integer $m\ge0$,

$$
\boxed{
\sup_{A_k^+\times(T-\tau_k,T]}
|\nabla^m u|<\infty.
}
\tag{3.2}
$$

A standard local pressure decomposition gives smooth control of the local pressure component. The far pressure component is harmonic on the collar and is controlled there by finite kinetic energy and positive spatial separation.

Status:

$$
\boxed{
\textbf{STANDARD LOCAL REGULARITY CONSEQUENCE}.
}
$$

---

# 4. Divergence-free good-collar localization

Choose

$$
\chi_k\in C_c^\infty(B_{\rho_k+\delta_k}(x_\ast))
$$

with

$$
\boxed{
\chi_k\equiv1
\quad\text{on }B_{\rho_k-\delta_k}(x_\ast)
}
\tag{4.1}
$$

and

$$
\boxed{
\operatorname{supp}\nabla\chi_k\subset A_k.
}
\tag{4.2}
$$

Set

$$
f_k=\nabla\chi_k\cdot u.
$$

Since $\nabla\cdot u=0$ and $\chi_k$ is compactly supported,

$$
\int f_k\,dx
=
\int\nabla\cdot(\chi_ku)\,dx
=
0.
$$

Let $\mathcal B_k$ be a Bogovskii operator on a smooth annular domain containing $\operatorname{supp}\nabla\chi_k$ and define

$$
\boxed{
b_k=\mathcal B_k(f_k).
}
\tag{4.3}
$$

Then

$$
\boxed{\nabla\cdot b_k=f_k}
\tag{4.4}
$$

and $b_k$ is supported in the good collar.

Define

$$
\boxed{
v_k=\chi_ku-b_k.
}
\tag{4.5}
$$

Then

$$
\boxed{\nabla\cdot v_k=0,}
\tag{4.6}
$$

$$
\boxed{
v_k=u
\quad
\text{on }B_{\rho_k-\delta_k}(x_\ast),
}
\tag{4.7}
$$

and $v_k$ is compactly supported in a ball of radius $O(\rho_k)$.

---

# 5. Local $L^2$ bound

Bogovskii boundedness and the global energy inequality give, for each fixed $k$,

$$
\boxed{
\sup_{t<T}\|v_k(t)\|_2
\le
M_k<\infty.
}
\tag{5.1}
$$

No uniformity in $k$ is needed for the contradiction on one fixed collar.

---

# 6. Forced localized Navier--Stokes equation

Direct substitution of $v_k=\chi_ku-b_k$ into Navier--Stokes and application of the Leray projector yields

$$
\boxed{
\partial_tv_k
-
\nu\Delta v_k
+
\mathbb P\nabla\cdot(v_k\otimes v_k)
=
F_k.
}
\tag{6.1}
$$

Before Leray projection, the forcing is a finite sum of terms produced by:

- derivatives of $\chi_k$;
- $b_k$ and its time/spatial derivatives;
- collar values of $u,\nabla u,p$;
- the difference between $\chi_k(u\cdot\nabla u)$ and $(v_k\cdot\nabla)v_k$.

All raw forcing terms are supported in, or generated from, the good collar.

By Section 3, for fixed $k$ all collar fields are uniformly smooth up to $T$. Since the Leray projector is bounded on $L^2$,

$$
\boxed{
F_k\in
L^\infty(T-\tau_k,T;L^2(\mathbb R^3))
}
\tag{6.2}
$$

and hence

$$
\boxed{
\int_{T-\tau_k}^{T}
\|F_k(t)\|_2^2\,dt<\infty.
}
\tag{6.3}
$$

Status:

$$
\boxed{
\textbf{PROVED from good-collar regularity and standard Bogovskii bounds}.
}
$$

---

# 7. Localized dissipation wavenumber

Let

$$
(v_k)_q=\Delta_qv_k.
$$

Define

$$
\boxed{
Q_k(t)
=
\min\left\{
q:
\lambda_p^{-1}
\|(v_k)_p(t)\|_\infty
<
c_0\nu
\quad
\forall p>q
\right\}.
}
\tag{7.1}
$$

For smooth $v_k(t)$, $Q_k(t)<\infty$ for each $t<T$.

At an active boundary,

$$
\boxed{
\|(v_k)_{Q_k(t)}(t)\|_\infty
\ge
c_0\nu\lambda_{Q_k(t)}.
}
\tag{7.2}
$$

This follows from minimality of the definition and does not require the equation to be unforced.

---

# 8. Forced Littlewood--Paley $H^1$ estimate

Apply $\Delta_q$ to (6.1), pair with $(v_k)_q$, multiply by $\lambda_q^2$, and sum over $q$.

The nonlinear term is treated by the standard Bony/dissipation-wavenumber decomposition. For the pure velocity flux, the Cheskidov--Dai estimate is valid for every $s>0$. At $s=1$, choosing $c_0$ sufficiently small absorbs the high-frequency nonlinear part into viscosity.

One obtains

$$
\boxed{
\frac12
\frac d{dt}
\|v_k\|_{\dot H^1}^2
+
c_1\nu
\|v_k\|_{\dot H^2}^2
\le
C
f_k^{low}(t)
\|v_k\|_{\dot H^1}^2
+
\mathcal F_k(t),
}
\tag{8.1}
$$

where

$$
\boxed{
f_k^{low}(t)
=
\sum_{q\le Q_k(t)}
\lambda_q
\|(v_k)_q(t)\|_\infty
}
\tag{8.2}
$$

and

$$
\mathcal F_k
=
\sum_q
\lambda_q^2
\langle
(F_k)_q,(v_k)_q
\rangle.
$$

By Cauchy--Schwarz and Young,

$$
\boxed{
|\mathcal F_k|
\le
\frac{c_1\nu}{2}
\|v_k\|_{\dot H^2}^2
+
C\nu^{-1}
\|F_k\|_2^2.
}
\tag{8.3}
$$

Thus

$$
\boxed{
\frac d{dt}
\|v_k\|_{\dot H^1}^2
+
c_2\nu
\|v_k\|_{\dot H^2}^2
\le
C
f_k^{low}(t)
\|v_k\|_{\dot H^1}^2
+
C\nu^{-1}
\|F_k\|_2^2.
}
\tag{8.4}
$$

Status:

$$
\boxed{
\textbf{PROVED modulo the standard Cheskidov--Dai Bony estimate, with forcing treated explicitly}.
}
$$

---

# 9. Forced localized dissipation-wavenumber continuation

## Theorem 9.1

Fix $k$. Suppose there exist $Q_0<\infty$ and $t_0<T$ such that

$$
\boxed{
Q_k(t)\le Q_0
}
\tag{9.1}
$$

for every $t\in(t_0,T)$.

Then

$$
\boxed{
\sup_{t_0<t<T}\|v_k(t)\|_{H^1}<\infty
}
\tag{9.2}
$$

and

$$
\boxed{
\int_{t_0}^{T}
\|v_k(t)\|_{H^2}^2\,dt<\infty.
}
\tag{9.3}
$$

Consequently $(x_\ast,T)$ is regular.

### Proof

Since $Q_k(t)\le Q_0$, only finitely many low modes occur. Bernstein and (5.1) give

$$
\begin{aligned}
f_k^{low}(t)
&\le
\sum_{q\le Q_0}
\lambda_q
\|(v_k)_q(t)\|_\infty\\
&\le
C
\sum_{q\le Q_0}
\lambda_q^{5/2}
\|(v_k)_q(t)\|_2\\
&\le
C(Q_0)M_k
=
L_k.
\end{aligned}
$$

Insert this into (8.4). The force term is integrable by (6.3). Gronwall gives (9.2), and integration gives (9.3).

Since

$$
H^2(\mathbb R^3)\hookrightarrow L^\infty(\mathbb R^3),
$$

we obtain

$$
v_k\in L^2(t_0,T;L^\infty).
$$

This is a Serrin endpoint class:

$$
\frac2{2}+\frac3{\infty}=1.
$$

Hence $v_k$ is regular up to $T$.

But $v_k=u$ near $x_\ast$, so $(x_\ast,T)$ is regular, contradiction.

$$
\square
$$

Status:

$$
\boxed{\textbf{PROVED}.}
$$

---

# 10. Local dissipation wavenumber must diverge

Because $(x_\ast,T)$ is singular, Theorem 9.1 implies for every good collar

$$
\boxed{
\limsup_{t\uparrow T}Q_k(t)=+\infty.
}
\tag{10.1}
$$

Equivalently,

$$
\boxed{
\limsup_{t\uparrow T}\Lambda_k(t)=+\infty.
}
\tag{10.2}
$$

Status:

$$
\boxed{\textbf{PROVED}.}
$$

---

# 11. Choosing a local supplier sequence

For each $k$, choose $N_k$ large enough that

$$
\boxed{
2^{N_k}\rho_k\ge k
}
\tag{11.1}
$$

and all high-frequency localization/collar errors below are less than a fixed small fraction of $c_0\nu2^{N_k}$.

By (10.1), choose

$$
t_k\in
(T-\min\{\tau_k,k^{-1}\},T)
$$

with

$$
\boxed{
Q_k(t_k)\ge N_k.
}
\tag{11.2}
$$

Set

$$
q_k=Q_k(t_k),
\qquad
\lambda_k=2^{q_k}.
$$

Then

$$
\boxed{t_k\uparrow T,}
\tag{11.3}
$$

$$
\boxed{\lambda_k\rho_k\to\infty,}
\tag{11.4}
$$

and

$$
\boxed{
\lambda_k^{-1}
\|(v_k)_{q_k}(t_k)\|_\infty
\ge
c_0\nu.
}
\tag{11.5}
$$

---

# 12. Rapid off-support decay

Let $K$ be the Schwartz kernel of the unit Littlewood--Paley projector. Then

$$
K_q(x)=\lambda_q^3K(\lambda_qx),
$$

and for every $N$,

$$
\boxed{
|K_q(x)|
\le
C_N\lambda_q^3
(1+\lambda_q|x|)^{-N}.
}
\tag{12.1}
$$

Since $v_k$ is supported in a ball of radius $O(\rho_k)$ and has bounded $L^2$ norm, for points a fixed fraction of $\rho_k$ away from the support,

$$
\boxed{
\lambda_k^{-1}
|
(v_k)_{q_k}(x,t_k)
|
\to0.
}
\tag{12.2}
$$

because $\lambda_k\rho_k\to\infty$.

Hence a point realizing a fixed fraction of the supplier $L^\infty$ norm lies within $O(\rho_k)$ of $x_\ast$.

---

# 13. High frequencies are negligible in the smooth collar

Let $C_k$ be a closed subcollar containing the cutoff transition and the support of $b_k$.

Since $v_k$ is smooth with all derivatives uniformly bounded on a neighborhood of $C_k\times(T-\tau_k,T]$, a local smooth cutoff plus the Schwartz-kernel tail gives, for every $M$,

$$
\boxed{
\sup_{
x\in C_k,\,
t\in(T-\tau_k,T]
}
|
(v_k)_q(x,t)
|
\le
C_{k,M}\lambda_q^{-M}.
}
\tag{13.1}
$$

Therefore

$$
\boxed{
\sup_{
x\in C_k,\,
t\in(T-\tau_k,T]
}
\lambda_q^{-1}
|
(v_k)_q(x,t)
|
\to0
}
\tag{13.2}
$$

as $q\to\infty$.

Thus the critical supplier lower bound cannot be attained in the smooth cutoff/Bogovskii collar for $q$ sufficiently large.

---

# 14. Supplier center lies in the inner localization region

Choose $x_k$ with

$$
\boxed{
|
(v_k)_{q_k}(x_k,t_k)
|
\ge
\frac34
\|(v_k)_{q_k}(t_k)\|_\infty.
}
\tag{14.1}
$$

By Sections 12--13, after increasing $N_k$ if needed,

$$
\boxed{
x_k\in B_{\rho_k-\delta_k}(x_\ast).
}
\tag{14.2}
$$

Hence

$$
\boxed{
|x_k-x_\ast|\le\rho_k
}
\tag{14.3}
$$

and therefore

$$
\boxed{x_k\to x_\ast.}
\tag{14.4}
$$

Status:

$$
\boxed{\textbf{PROVED}.}
$$

---

# 15. Comparing localized and original shells

Inside the inner region $v_k=u$. Moreover, the difference $v_k-u$ is supported in the distant transition/exterior region.

With a slightly smaller inner selection region, the chosen $x_k$ has positive distance from $\operatorname{supp}(v_k-u)$ for each fixed $k$.

The Littlewood--Paley kernel tail therefore gives, for every $N$,

$$
\boxed{
|
\Delta_{q_k}(v_k-u)(x_k,t_k)
|
\le
C_{k,N}\lambda_k^{-N}.
}
\tag{15.1}
$$

Choose $q_k$ sufficiently large so that

$$
\boxed{
\lambda_k^{-1}
|
\Delta_{q_k}(v_k-u)(x_k,t_k)
|
\le
\frac{c_0}{4}\nu.
}
\tag{15.2}
$$

From (11.5) and (14.1),

$$
\lambda_k^{-1}
|
(v_k)_{q_k}(x_k,t_k)
|
\ge
\frac{3c_0}{4}\nu.
$$

Hence

$$
\boxed{
\lambda_k^{-1}
|
u_{q_k}(x_k,t_k)
|
\ge
\frac{c_0}{2}\nu.
}
\tag{15.3}
$$

Status:

$$
\boxed{\textbf{PROVED}.}
$$

---

# 16. NEW THEOREM — Local Supplier Capture

## Theorem 16.1

Let $u$ be a smooth finite-energy three-dimensional Navier--Stokes solution on $[0,T)$ with first singular time $T<\infty$. Let $(x_\ast,T)$ be any singular point.

Then there exist sequences

$$
\boxed{t_k\uparrow T,}
\tag{16.1}
$$

$$
\boxed{x_k\to x_\ast,}
\tag{16.2}
$$

and dyadic frequencies

$$
\boxed{\lambda_k\to\infty}
\tag{16.3}
$$

such that

$$
\boxed{
\lambda_k^{-1}
|
\Delta_{\lambda_k}u(x_k,t_k)
|
\ge
c_{\rm loc}\nu
}
\tag{16.4}
$$

for a universal $c_{\rm loc}>0$ up to the fixed Littlewood--Paley convention.

Equivalently,

$$
\boxed{
\textbf{
a first singular point is approached by actual critical
Littlewood--Paley supplier atoms of the original velocity field.
}
}
\tag{16.5}
$$

Status:

$$
\boxed{
\textbf{PROVED within the stated first-singularity / suitable-solution framework}.
}
$$

The theorem should receive independent audit before any public novelty claim.

---

# 17. Relation to established local concentration results

Barker--Prange prove localized smoothing for critical local data and, under a Type-I assumption, concentration of $L^3$, $L^{3,\infty}$, and critical Besov norms on shrinking balls centered at a singular point.

Their result confirms that critical activity may be genuinely centered on a blow-up point rather than at an unrelated global location. The present argument is different: it uses first-singularity geometry, good regular collars, and a forced localized dissipation-wavenumber continuation estimate, and it does not assume Type I.

Bradshaw--Grujić independently show that possible singularity formation requires essential activity in frequency windows whose lower edge diverges toward the first singular time.

No priority claim is made for the general frequency-localization philosophy.

---

# 18. Why the good collar matters

A naive cutoff around $x_\ast$ can create forcing terms that themselves become singular near $T$.

The CKN singular-set geometry lets the cutoff be placed on a radius whose transition collar contains no singular point at time $T$.

Thus

$$
\boxed{
\text{localization forcing is regular,
so high-frequency blowup cannot be blamed on the collar}.
}
\tag{18.1}
$$

That is the local-decoupling mechanism.

---

# 19. Re-entry into the supplier trace pipeline

Theorem 16.1 supplies

$$
\boxed{
\lambda_k^{-1}
|u_{q_k}(x_k,t_k)|
\ge
c_{\rm loc}\nu
}
\tag{19.1}
$$

with

$$
x_k\to x_\ast.
$$

The DCRP-09 heat-memory subtraction only requires a critical shell-amplitude lower bound plus the global kinetic-energy bound. It does not require that $q_k$ be the global dissipation boundary.

Define

$$
\boxed{
g_{q_k}(t)
=
u_{q_k}(t)
-
e^{\nu(t-t_{0,k})\Delta}
u_{q_k}(t_{0,k})
}
\tag{19.2}
$$

with $t_{0,k}$ chosen so the heat memory is a small fraction of the local supplier amplitude.

Then

$$
\boxed{
\lambda_k^{-1}
\|g_{q_k}(t_k)\|_\infty
\ge
c\nu.
}
\tag{19.3}
$$

After normalized recentering, DCRP-14 gives the universal solenoidal trace lift

$$
\boxed{
\|\Pi_{H_\ast}h_k\|
\ge
c_\ast\nu.
}
\tag{19.4}
$$

DCRP-15 gives

$$
\boxed{
\|
\mathcal O_{W_\ast}^Td_k
\|
+
C_{\rm sup}
\mathcal B_{\rm sup}^{res}(k)
\ge
c_{\rm sup}\nu.
}
\tag{19.5}
$$

Thus the supplier trace/residual gap now occurs at centers converging to the actual singular point.

The remote-supplier loophole is removed.

---

# 20. What is now closed

The DCRP-15 frontier was

$$
\boxed{
\text{local singularity}
\Longrightarrow
\text{local supplier}
\ \vee\
\text{paid localization forcing}.
}
$$

The good-collar construction makes the localization forcing regular.

Therefore

$$
\boxed{
\textbf{
local singularity}
\Longrightarrow
\textbf{
local critical supplier sequence}.
}
\tag{20.1}
$$

Status:

$$
\boxed{
\textbf{CLOSED in the present route}.
}
$$

---

# 21. What remains open

The theorem produces an actual local supplier sequence

$$
(x_k,t_k,\lambda_k)
$$

approaching $(x_\ast,T)$.

MORP works with a particular extracted minimal obstruction / return sequence.

It remains to verify that the local supplier sequence can be inserted into, synchronized with, or used to replace that extracted sequence without losing:

- minimality;
- actual return structure;
- zero-cost ledger relations;
- finite-window quotient synchronization.

Thus the next issue is

$$
\boxed{
\textbf{
Local Supplier / MORP Sequence Synchronization}.
}
\tag{21.1}
$$

This is much narrower than Local Supplier Capture.

---

# 22. Potential synchronization shortcut

Suppose the MORP minimal sequence is generated from shrinking actual singular windows around $(x_\ast,T)$.

Theorem 16.1 gives supplier atoms in arbitrarily small physical neighborhoods of $x_\ast$.

For every singular window, choose the first descendant local supplier event satisfying

$$
\lambda^{-1}
|\Delta_\lambda u|
\ge
c_{\rm loc}\nu.
$$

Use that event as the next re-root point/scale.

Then:

- the state is actual;
- the center remains in the singular neighborhood;
- the scale is endogenous to Navier--Stokes;
- the trace lower bound is automatic;
- failure to fit the original return chart is an explicit transition/re-root discrepancy.

This suggests that supplier rooting can be installed as the stopping rule of the actual MORP extraction rather than as an auxiliary sequence.

---

# 23. Remaining time-scale issue

Theorem 16.1 proves

$$
t_k\uparrow T,
\qquad
\lambda_k\to\infty.
$$

It does not prove

$$
\boxed{
\lambda_k^2(T-t_k)\asymp1.
}
\tag{23.1}
$$

Thus the normalized remaining horizon may tend to zero, a finite positive constant, or infinity.

Likewise the supplier wavelength need not be comparable to the original good-collar radius.

These are synchronization issues, not local-capture failures.

They must be handled by the MORP descendant/re-root compiler.

---

# 24. New exact frontier

The next target is

$$
\boxed{
\textbf{
Local Supplier Stopping-Time / MORP Synchronization Lemma}.
}
$$

A sufficient form is:

> Given any actual singular-rooted MORP extraction sequence around $(x_\ast,T)$, one may pass to a descendant/stopping-time refinement whose roots are local supplier events satisfying
>
> $$
> \lambda_n^{-1}
> |\Delta_{\lambda_n}u(x_n,t_n)|
> \ge
> c\nu,
> $$
>
> while preserving the monotone obstruction ordering and charging every re-root discrepancy to the existing transition residual.
>
> Consequently every minimal actual singular obstruction may be assumed, without loss of zero-cost generality, to be supplier-rooted.

If proved, DCRP-15's uniform trace/residual gap applies directly to the very sequence used by MORP minimality.

That would collide with the exact zero-cost minimal obstruction.

---

# 25. Source ledger

## Caffarelli--Kohn--Nirenberg

Used for the singular-set geometry and the existence of arbitrarily small regular collars around a selected first singular point.

## Barker--Prange

Tobias Barker and Christophe Prange, *Localized smoothing for the Navier-Stokes equations and concentration of critical norms near singularities*, arXiv:1812.09115v2.

Relevant established facts:

- localized smoothing is genuinely local for local energy solutions;
- under a Type-I assumption, critical norms concentrate on shrinking balls centered at the singular point;
- perturbed/localized Navier--Stokes equations can be analyzed with explicit local pressure and forcing terms.

DCRP-16 does not assume their Type-I concentration theorem.

## Bradshaw--Grujić

Zachary Bradshaw and Zoran Grujić, *Frequency localized regularity criteria for the 3D Navier-Stokes equations*, arXiv:1501.01043v2.

Used as calibration that frequency windows diverging toward the first singular time are essential to possible singularity formation.

## Cheskidov--Dai

Used for the velocity dissipation-wavenumber Bony estimate. DCRP-16 adds the forcing term explicitly by Cauchy--Schwarz and Young.

---

# 26. End state

The global/local supplier gap from DCRP-15 is closed.

For every first singular point $(x_\ast,T)$ there exist

$$
t_k\uparrow T,
\qquad
x_k\to x_\ast,
\qquad
\lambda_k\to\infty
$$

such that

$$
\boxed{
\lambda_k^{-1}
|
\Delta_{\lambda_k}u(x_k,t_k)
|
\ge
c_{\rm loc}\nu.
}
$$

Thus

$$
\boxed{
\textbf{
the singular point itself is approached by actual critical supplier atoms.
}
}
$$

The supplier modules then give

$$
\boxed{
\|
\mathcal O_{W_\ast}^Td_k
\|
+
C_{\rm sup}
\mathcal B_{\rm sup}^{res}(k)
\ge
c_{\rm sup}\nu
}
$$

with $x_k\to x_\ast$.

The next single frontier is

$$
\boxed{
\textbf{
Local Supplier Stopping-Time / MORP Synchronization Lemma}.
}
$$

If supplier rooting can be installed as a legitimate descendant/stopping rule of the minimal-obstruction extraction, the supplier trace/residual gap collides directly with MORP's zero-cost minimality.
