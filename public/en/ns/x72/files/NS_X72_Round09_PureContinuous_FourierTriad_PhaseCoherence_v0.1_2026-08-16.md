# NS × X Integral × 24/72 Paradigm Action
## Round 09 — Pure Continuous Fourier-Triad Geometry / Phase-Coherence Route

- Date: 2026-08-16
- Version: v0.1
- Status: Proof-Route Experiment / Continuous-Only Fourier-Triad Branch
- canonical source：UTF-8 Markdown
- canonical math delimiters：inline `$...$`；display `$$...$$`
- Previous round: `NS_X72_Round08_PureContinuous_TransferDispersion_Feedback_v0.1_2026-08-16.md`
- This round's objective: Substitute the abstract transfer rate $\vartheta$ from Round 08 back into the actual incompressible Navier–Stokes Fourier convolution to establish the continuous triad transfer kernel, commutator weight-gap identity, angular null structure, and phase-sign structure, and rewrite the missing covariance bound of $\zeta_{\tau,s}$ into an explicit signed triad inequality.
- Non-claims: This round does not prove that this signed triad inequality holds unconditionally; instead, this round precisely identifies that radial geometry + amplitude alone is insufficient to determine the transfer sign, and the relative triad phase is an indispensable carrier.

---

# 0. Round 08 handoff

Round 08 defined for the analytic-weighted strain spectrum:

$$
r=|\xi|,
$$

$$
m
=
\mathbb E_\mu[r],
$$

$$
V
=
\operatorname{Var}_\mu(r),
$$

and the local nonlinear transfer rate:

$$
\vartheta(\xi,t).
$$

yielding the exact mean-frequency law:

$$
\boxed{
m'
=
2
\operatorname{Cov}_\mu(r,\vartheta)
-
2\nu
\operatorname{Cov}_\mu(r,r^2)
+
2\tau'V.
}
\tag{0.1}
$$

and proved that:

$$
\boxed{
\operatorname{Cov}_\mu(r,r^2)
\ge
mV>0
}
\tag{0.2}
$$

holds for any nontrivial smooth $L^2$ spectral state.

Define:

$$
\boxed{
\zeta_{\tau,s}
=
\frac{
\operatorname{Cov}_\mu(r,\vartheta)
}{
\nu
\operatorname{Cov}_\mu(r,r^2)
}.
}
\tag{0.3}
$$

If:

$$
\tau'\le0,
$$

then:

$$
\boxed{
\zeta_{\tau,s}\le1
\Longrightarrow
m'\le0.
}
\tag{0.4}
$$

Round 08 STOP:

$$
\boxed{
\text{STOP-C12}
=
\text{Nonlinear Transfer–Dispersion Covariance Gap}.
}
$$

This round directly asks what:

$$
\boxed{
\operatorname{Cov}(r,\vartheta)
}
$$

actually is in the actual NS convolution.

---

# 1. Fourier Navier–Stokes equation

Adopting the Fourier convention:

$$
\widehat f(k)
=
\int_{\mathbb R^3}
e^{-ik\cdot x}
f(x)\,dx.
$$

Let:

$$
P_k
=
I
-
\frac{k\otimes k}{|k|^2}
$$

be the Leray projector symbol.

For an incompressible velocity:

$$
k\cdot\widehat u(k)=0.
$$

The Navier–Stokes Fourier equation is:

$$
\boxed{
\partial_t\widehat u(k)
+
\nu|k|^2\widehat u(k)
=
-i
P_k
\int_{\mathbb R^3}
\left(
k\cdot\widehat u(p)
\right)
\widehat u(q)
\,dp,
}
\tag{1.1}
$$

where:

$$
\boxed{
q=k-p,
\qquad
k=p+q.
}
\tag{1.2}
$$

From:

$$
p\cdot\widehat u(p)=0,
$$

we have:

$$
\boxed{
k\cdot\widehat u(p)
=
q\cdot\widehat u(p).
}
\tag{1.3}
$$

This identity directly connects the triad coupling with the triad geometry.

---

# 2. Continuous triad transfer density

Pairing with:

$$
\overline{\widehat u(k)}
$$

Since:

$$
P_k\widehat u(k)=\widehat u(k),
$$

the projector vanishes in the modal energy pairing.

Define the ordered continuous triad transfer kernel:

$$
\boxed{
\mathcal T(k;p,q)
=
\operatorname{Im}
\left[
\left(
k\cdot\widehat u(p)
\right)
\left(
\widehat u(q)\cdot
\overline{\widehat u(k)}
\right)
\right],
}
\tag{2.1}
$$

where:

$$
k=p+q.
$$

Then:

$$
\boxed{
\frac12
\partial_t
|\widehat u(k)|^2
+
\nu|k|^2|\widehat u(k)|^2
=
\int_{\mathbb R^3}
\mathcal T(k;p,k-p)
\,dp.
}
\tag{2.2}
$$

Let:

$$
\boxed{
\Theta(k)
=
\int
\mathcal T(k;p,k-p)
\,dp.
}
\tag{2.3}
$$

Then:

$$
\Theta(k)
$$

is the nonlinear energy-transfer density of mode $k$.

---

# 3. Global energy conservation is a zero-weight-gap statement

For a smooth decaying incompressible field:

$$
\int_{\mathbb R^3}
u\cdot(u\cdot\nabla u)\,dx
=
0.
$$

In Fourier space:

$$
\boxed{
\int_{\mathbb R^3}
\Theta(k)\,dk
=
0.
}
\tag{3.1}
$$

Therefore, the nonlinear term:

- can move energy from some frequencies to other frequencies;
- but does not create total kinetic energy.

This is triad redistribution, not net creation.

---

# 4. Weighted Fourier multiplier energy

Let:

$$
A=a(\Lambda)
$$

be a real radial Fourier multiplier:

$$
\widehat{Af}(k)
=
a(|k|)\widehat f(k),
$$

where:

$$
a(r)>0.
$$

Define:

$$
E_a
=
\frac12
\|Au\|_2^2.
$$

Then:

$$
\boxed{
\frac d{dt}E_a
+
\nu
\|\Lambda Au\|_2^2
=
\mathcal N_a,
}
\tag{4.1}
$$

where the direct weighted transfer is:

$$
\boxed{
\mathcal N_a
=
\iint
a_k^2
\mathcal T(k;p,q)
\,dp\,dk,
}
\tag{4.2}
$$

Denote:

$$
a_k=a(|k|).
$$

---

# 5. Exact commutator representation

By incompressibility:

$$
\langle
Au,
u\cdot\nabla Au
\rangle
=
0.
$$

Therefore:

$$
\langle
Au,
A(u\cdot\nabla u)
\rangle
=
\langle
Au,
[A,u\cdot\nabla]u
\rangle.
$$

In Fourier space, the triad kernel of:

$$
[A,u\cdot\nabla]u
$$

carries:

$$
a_k-a_q.
$$

Thus:

$$
\boxed{
\mathcal N_a
=
\iint
a_k
(a_k-a_q)
\mathcal T(k;p,q)
\,dp\,dk.
}
\tag{5.1}
$$

This identity is extremely important.

If:

$$
a\equiv1,
$$

then:

$$
a_k-a_q=0
$$

pointwise,

so:

$$
\mathcal N_1=0.
$$

Therefore:

$$
\boxed{
\textbf{
weighted nonlinear growth exists only because
the spectral observation weight does not commute with advection.
}
}
\tag{5.2}
$$

In other words:

$$
\boxed{
\text{cascade signal}
=
\text{transport–observation commutator}.
}
$$

---

# 6. No-free-radial-jump lemma

For a radial:

$$
a=a(r),
$$

by the mean-value theorem:

$$
|a_k-a_q|
\le
\sup_{\rho\in I_{kq}}
|a'(\rho)|
\,
\bigl|
|k|-|q|
\bigr|,
$$

where:

$$
I_{kq}
$$

is the interval between:

$$
|k|
$$

and:

$$
|q|.
$$

By the triangle inequality:

$$
\boxed{
\bigl|
|k|-|q|
\bigr|
\le
|k-q|
=
|p|.
}
\tag{6.1}
$$

Therefore:

$$
\boxed{
|a_k-a_q|
\le
|p|
\sup_{\rho\in I_{kq}}
|a'(\rho)|.
}
\tag{6.2}
$$

Named:

$$
\boxed{
\textbf{No-Free-Radial-Jump Lemma}.
}
$$

Significance:

> If a triad interaction is to make the observation weight cross a large radial gap between $q\to k$, the wavenumber of the mediator mode $p$ must at least bear the geometric size of that gap.

This is not a lower bound on energy cost.

It is an exact frequency-triangle constraint.

---

# 7. Incompressibility angular null

From:

$$
k\cdot\widehat u(p)
=
q\cdot\widehat u(p)
$$

and:

$$
\widehat u(p)\perp p,
$$

we obtain:

$$
\boxed{
\left|
k\cdot\widehat u(p)
\right|
\le
|q|
\sin\theta_{pq}
|\widehat u(p)|,
}
\tag{7.1}
$$

where:

$$
\theta_{pq}
$$

is the angle between $p,q$.

Therefore:

$$
\boxed{
|\mathcal T(k;p,q)|
\le
|q|
\sin\theta_{pq}
|\widehat u(p)|
|\widehat u(q)|
|\widehat u(k)|.
}
\tag{7.2}
$$

In particular:

$$
\boxed{
\theta_{pq}=0
\text{ or }\pi
\Longrightarrow
\mathcal T(k;p,q)=0.
}
\tag{7.3}
$$

Thus, exact collinear triads do not contribute to this ordered transfer channel.

Named:

$$
\boxed{
\textbf{Collinear Triad Null}.
}
$$

---

# 8. Weight-gap × angle upper envelope

Combining (5.1), (6.2), and (7.2):

$$
\boxed{
\begin{aligned}
&
\left|
a_k(a_k-a_q)
\mathcal T(k;p,q)
\right|
\\
&\qquad
\le
a_k
|p|
|q|
\sin\theta_{pq}
\sup_{\rho\in I_{kq}}|a'(\rho)|
|\widehat u(p)|
|\widehat u(q)|
|\widehat u(k)|.
\end{aligned}
}
\tag{8.1}
$$

Thus, a large weighted transfer requires simultaneously satisfying:

1. nontrivial mediator frequency:

$$
|p|>0;
$$

2. non-collinear geometry:

$$
\sin\theta_{pq}>0;
$$

3. modal amplitude overlap;

4. observation-weight gap;

5. relative phase coherence, which has not yet been explicitly written out.

The first four items still cannot determine the sign.

---

# 9. Triad phase carrier

Define the complex interaction product:

$$
\boxed{
Z(k;p,q)
=
\left(
k\cdot\widehat u(p)
\right)
\left(
\widehat u(q)\cdot
\overline{\widehat u(k)}
\right).
}
\tag{9.1}
$$

When:

$$
Z\neq0
$$

write:

$$
\boxed{
Z
=
\mathcal A
e^{i\Phi},
}
\tag{9.2}
$$

where:

$$
\mathcal A=|Z|\ge0,
$$

$$
\Phi\in\mathbb S^1.
$$

Then:

$$
\boxed{
\mathcal T
=
\mathcal A
\sin\Phi.
}
\tag{9.3}
$$

Therefore, the transfer kernel is precisely factored into:

$$
\boxed{
\text{amplitude}
\times
\text{phase coherence}.
}
$$

The angle:

$$
\theta_{pq}
$$

controls the geometric upper bound of:

$$
\mathcal A
$$

but:

$$
\Phi
$$

determines the signed transfer.

---

# 10. Phase-Sign Flexibility Lemma

Fix a non-degenerate triad geometry:

$$
(k,p,q),
\qquad
k=p+q,
$$

and divergence-free modal directions and magnitudes, such that:

$$
\mathcal A>0.
$$

Then:

$$
\mathcal T
=
\mathcal A\sin\Phi.
$$

If we only change the relative complex phase, such that:

$$
\Phi
\mapsto
-\Phi,
$$

then:

$$
\mathcal A
$$

remains unchanged,

the frequency triangle remains unchanged,

the modal magnitudes remain unchanged,

the angle geometry remains unchanged,

but:

$$
\boxed{
\mathcal T
\mapsto
-\mathcal T.
}
\tag{10.1}
$$

Therefore:

$$
\boxed{
\textbf{
frequency geometry + modal magnitudes do not determine
the sign of an individual triad transfer kernel.
}
}
\tag{10.2}
$$

This is an algebraic Fourier-kernel statement.

To elevate this into a global realizability statement for a specific whole-space solution class, one would also need to control all conjugate modes and other simultaneous triads; this document does not make such an overly strong claim.

---

# 11. Restricted observation no-go

Define the observation context:

$$
\Gamma_{\rm triad,amp}
$$

requiring the preservation of:

- $|k|,|p|,|q|$;
- triad angles;
- modal magnitudes;
- signed energy transfer.

Restrict the observation class:

$$
\mathcal Q_{\rm amp/geom}
$$

to only read:

- radial geometry;
- angle geometry;
- modal amplitudes;

but not read the relative complex phase.

By Phase-Sign Flexibility:

there exist identical amplitude/geometry observations corresponding to:

$$
\mathcal T>0
$$

and:

$$
\mathcal T<0.
$$

Thus:

$$
\boxed{
\mathsf X_{\Gamma_{\rm triad,amp}}
}
\tag{11.1}
$$

holds in this restricted class.

A repair requires adding at least:

$$
\boxed{
\Phi
}
$$

or a signed phase-coherence carrier equivalent to:

$$
\sin\Phi
$$

---

# 12. Connection back to strain spectral measure

Fourier strain:

$$
\boxed{
\widehat S_{ij}(k)
=
\frac{i}{2}
\left(
k_j\widehat u_i(k)
+
k_i\widehat u_j(k)
\right).
}
\tag{12.1}
$$

From:

$$
k\cdot\widehat u(k)=0,
$$

we can calculate:

$$
\boxed{
|\widehat S(k)|^2
=
\frac12
|k|^2
|\widehat u(k)|^2.
}
\tag{12.2}
$$

If:

$$
N_u(k)
$$

is the velocity nonlinear Fourier RHS,

then the strain nonlinear RHS is:

$$
N_S
=
\operatorname{sym}
(ik\otimes N_u).
$$

A similar calculation yields:

$$
\boxed{
\operatorname{Re}
\left(
N_S:
\overline{\widehat S}
\right)
=
\frac12
|k|^2
\operatorname{Re}
\left(
N_u\cdot
\overline{\widehat u}
\right).
}
\tag{12.3}
$$

Therefore, where:

$$
\widehat u(k)\neq0
$$

the normalized local nonlinear growth rates are identical:

$$
\boxed{
\vartheta_S(k)
=
\vartheta_u(k).
}
\tag{12.4}
$$

Thus, the:

$$
\vartheta
$$

from Round 08 can be directly expressed using the velocity triad kernel of this round.

---

# 13. Round 08 analytic strain weight as a velocity weight

The Round 08/07 strain spectral measure weight is:

$$
e^{2\tau r}
r^{2s}
|\widehat S|^2.
$$

From (12.2):

$$
e^{2\tau r}
r^{2s}
|\widehat S|^2
=
\frac12
e^{2\tau r}
r^{2s+2}
|\widehat u|^2.
$$

So we define the velocity-side positive weight:

$$
\boxed{
w_{\tau,s}(r)
=
\frac12
e^{2\tau r}
r^{2s+2}.
}
\tag{13.1}
$$

Then the analytic strain normalization is:

$$
G
=
\int
w_{\tau,s}(r_k)
|\widehat u(k)|^2
dk.
$$

---

# 14. Exact triad representation of the covariance numerator

From:

$$
\vartheta(k)
=
\frac{
\Theta(k)
}{
|\widehat u(k)|^2
}
$$

on non-zero modes,

we have:

$$
\boxed{
G
\operatorname{Cov}_\mu(r,\vartheta)
=
\int
w_k
(r_k-m)
\Theta(k)
\,dk.
}
\tag{14.1}
$$

Substituting in:

$$
\Theta(k)
=
\int
\mathcal T(k;p,q)dp,
$$

we obtain:

$$
\boxed{
G
\operatorname{Cov}_\mu(r,\vartheta)
=
\iint
w_k
(r_k-m)
\mathcal A(k;p,q)
\sin\Phi(k;p,q)
\,dp\,dk.
}
\tag{14.2}
$$

This is the actual NS continuous-triad form of the abstract covariance from Round 08.

---

# 15. Exact continuous triad threshold for $\zeta$

Round 08:

$$
\zeta
=
\frac{
\operatorname{Cov}_\mu(r,\vartheta)
}{
\nu
\operatorname{Cov}_\mu(r,r^2)
}.
$$

Using (14.2):

$$
\boxed{
\zeta_{\tau,s}
=
\frac{
\displaystyle
\iint
w_k(r_k-m)
\mathcal A
\sin\Phi
\,dp\,dk
}{
\displaystyle
\nu G
\operatorname{Cov}_\mu(r,r^2)
}.
}
\tag{15.1}
$$

Thus:

$$
\boxed{
\zeta\le1
}
$$

is equivalent to:

$$
\boxed{
\iint
w_k(r_k-m)
\mathcal A
\sin\Phi
\,dp\,dk
\le
\nu G
\operatorname{Cov}_\mu(r,r^2).
}
\tag{15.2}
$$

This is the signed triad inequality that the Pure-C route is currently truly missing.

It no longer contains the abstract:

$$
\vartheta.
$$

---

# 16. What incompressibility and triad geometry already give

From Sections 6–9,

the triad amplitude satisfies:

$$
\boxed{
\mathcal A
\le
|q|
\sin\theta_{pq}
|\widehat u(p)|
|\widehat u(q)|
|\widehat u(k)|.
}
\tag{16.1}
$$

and the spectral weight difference can only span:

$$
\boxed{
||k|-|q||
\le
|p|.
}
\tag{16.2}
$$

Thus, a dangerous positive covariance requires:

$$
\boxed{
\text{radial displacement}
+
\text{non-collinearity}
+
\text{amplitude overlap}
+
\text{positive phase coherence}.
}
\tag{16.3}
$$

If any of these terms continuously degenerates:

- radial displacement $\to 0$;
- angle $\to 0$;
- amplitude overlap $\to 0$;
- $\sin\Phi$ phase cancellation;

then its triad contribution is suppressed.

---

# 17. But these geometric factors do not give a uniform positive tax

No-Free-Radial-Jump and Collinear Null provide:

$$
\boxed{
\text{upper-envelope suppression}.
}
$$

But they do not provide:

$$
\boxed{
\text{forward transfer must pay some strictly positive universal lower cost}.
}
$$

Because:

$$
\sin\theta_{pq}
$$

can be arbitrarily small,

while:

$$
\sin\Phi
$$

can be positive, negative, or close to zero.

Therefore, at present, we cannot deduce from purely pointwise triad geometry that:

$$
\zeta\le1.
$$

This is an important no-go:

$$
\boxed{
\text{triad geometry constrains magnitude but not signed global covariance}.
}
\tag{17.1}
$$

---

# 18. Energy conservation alone does not select cascade direction

Global nonlinear energy conservation only gives:

$$
\int\Theta(k)dk=0.
$$

It indicates that gain and loss must balance.

But for an increasing spectral observation weight:

$$
w(r),
$$

there could still be:

$$
\int
w(r)\Theta(k)dk
>0
$$

or:

$$
<0,
$$

depending on whether energy is moved to higher or lower frequencies.

Therefore:

$$
\boxed{
\text{energy conservation}
\not\Rightarrow
\text{forward suppression}.
}
\tag{18.1}
$$

This is consistent with the phenomenon in known triadic-interaction research where different interaction classes can support different transfer directions.

Thus, invariant conservation itself is not a sufficiently coercive sign.

---

# 19. Continuous phase-coherence functional

Define the centered analytic triad weight:

$$
\boxed{
\mathcal W_m(k)
=
w_{\tau,s}(r_k)
(r_k-m).
}
\tag{19.1}
$$

Define the positive-amplitude measure:

$$
d\Gamma
=
\mathcal A(k;p,q)
\,dp\,dk.
$$

Then the covariance numerator is:

$$
\boxed{
\mathfrak C_{\rm triad}
=
\int
\mathcal W_m(k)
\sin\Phi
\,d\Gamma.
}
\tag{19.2}
$$

That is:

$$
\boxed{
G
\operatorname{Cov}(r,\vartheta)
=
\mathfrak C_{\rm triad}.
}
\tag{19.3}
$$

Therefore, the real high-frequency danger is not that:

$$
\mathcal A
$$

is large in itself.

Rather, it is that:

$$
\boxed{
\mathcal W_m
\text{ and }
\sin\Phi
\text{ produce a sustained positive correlation under the amplitude measure}.
}
\tag{19.4}
$$

---

# 20. Phase-neutral cancellation criterion

If in the amplitude-weighted triad ensemble:

$$
\boxed{
\int
\mathcal W_m
\sin\Phi
\,d\Gamma
\le0,
}
\tag{20.1}
$$

then:

$$
\operatorname{Cov}(r,\vartheta)\le0,
$$

hence:

$$
\zeta\le0<1.
$$

When:

$$
\tau'\le0
$$

then:

$$
m'<0
$$

for a nontrivial state.

More generally,

if:

$$
\boxed{
\int
\mathcal W_m
\sin\Phi
\,d\Gamma
\le
\nu G
\operatorname{Cov}(r,r^2),
}
\tag{20.2}
$$

then:

$$
m'\le0.
$$

Thus, the Pure-C closure has been compressed into:

$$
\boxed{
\text{continuous triad phase-coherence versus viscous dispersion}.
}
$$

---

# 21. A normalized dangerous coherence ratio

Define:

$$
\boxed{
\mathfrak Z_{\tau,s}
=
\frac{
\displaystyle
\int
\mathcal W_m
\sin\Phi
\,d\Gamma
}{
\displaystyle
\nu G
\operatorname{Cov}(r,r^2)
}.
}
\tag{21.1}
$$

From (19.3):

$$
\boxed{
\mathfrak Z_{\tau,s}
=
\zeta_{\tau,s}.
}
\tag{21.2}
$$

But the new representation reveals what was originally hidden in $\zeta$:

$$
\boxed{
\zeta
=
\text{signed phase-coherent triad transfer}
/\text{viscous spectral dispersion}.
}
$$

Thus, the abstract ratio from Round 08 now possesses explicit NS geometry.

---

# 22. STOP-C13 — Triad Phase-Coherence / Commutator-Sign Gap

Define:

$$
\boxed{
\bot_X^{\mathrm{C13}}
=
\left\langle
\begin{array}{l}
\text{layer}
=
\mathrm{continuous\ Fourier\ triad\ transfer},
\\
\text{exact\ kernel}
=
\mathcal T
=
\mathcal A\sin\Phi,
\\
\text{weight\ mechanism}
=
a_k(a_k-a_q),
\\
\text{radial\ constraint}
=
||k|-|q||\le|p|,
\\
\text{angular\ null}
=
\theta_{pq}=0,\pi
\Rightarrow
\mathcal T=0,
\\
\text{conservation}
=
\int\Theta(k)dk=0,
\\
\text{missing}
=
\mathrm{unconditional\ bound\ on\ signed\ phase\text{-}coherent\ weighted\ triad\ integral},
\\
\text{discrete\ intrusion}
=
\mathrm{false}.
\end{array}
\right\rangle.
}
$$

Named:

$$
\boxed{
\textbf{STOP-C13:
Triad Phase-Coherence / Commutator-Sign Gap}.
}
$$

---

# 23. Observation-axis update

Round 03:

$$
\mathsf X_{\Gamma_{\rm amp}}
$$

showed that strain amplitude is insufficient to preserve the nonlinear sign.

Round 08:

$$
\mathsf X_{\Gamma_\alpha}
$$

showed that mean nonlinear growth is insufficient to preserve spectral drift.

Round 09:

$$
\boxed{
\mathsf X_{\Gamma_{\rm triad,amp}}
}
$$

shows that frequency geometry + modal amplitude is still insufficient to preserve the signed triad transfer.

Thus, the observation state must at least include:

$$
\boxed{
\text{relative phase/coherence}.
}
$$

Current information chain:

$$
\boxed{
\text{amplitude}
\to
\text{geometry}
\to
\text{frequency distribution}
\to
\text{phase coherence}.
}
\tag{23.1}
$$

This is an important information hierarchy in the Pure-C route.

---

# 24. Still no essential discrete intrusion

All triads in this round are directly integrated continuously over:

$$
p\in\mathbb R^3
$$

There is no:

- shell index;
- mode graph;
- dyadic decomposition;
- discrete helical class as a necessary proof step;
- finite triad enumeration.

Therefore:

$$
\boxed{
T_{\mathsf C\to\mathsf D}
=
\text{NOT YET REACHED}.
}
\tag{24.1}
$$

The Pure-C route currently is:

$$
\boxed{
\begin{aligned}
\mathsf C_{\rm energy}
&\to
\mathsf C_{\rm critical}
\\
&\to
\mathsf C_{\rm relational}
\\
&\to
\mathsf C_{\rm nonlocal}
\\
&\to
\mathsf C_{\rm projected}
\\
&\to
\mathsf C_{\rm gradient\ geometry}
\\
&\to
\mathsf C_{\rm hierarchy}
\\
&\to
\mathsf C_{\rm Gevrey}
\\
&\to
\mathsf C_{\rm covariance}
\\
&\to
\mathsf C_{\rm triad\ phase}.
\end{aligned}
}
\tag{24.2}
$$

---

# 25. 24/72 Ledger — Round 09

| Step | X object / operation | $B$ | $U$ | $O$ | $L$ | status |
|---|---|---|---|---|---|---|
| C85 | Fourier NS convolution | $\mathsf C$ | $\mathsf P$ continuous convolution | relational | $\mathsf F$ | EXACT |
| C86 | triad transfer $\mathcal T$ | $\mathsf C$ | triadic | targeted | $\mathsf F$ | EXACT |
| C87 | total nonlinear energy conservation | $\mathsf C$ | global | scalar | $\mathsf F$ | EXACT |
| C88 | multiplier commutator identity | $\mathsf C$ | weighted | relational | $\mathsf F$ | EXACT |
| C89 | no-free-radial-jump | $\mathsf C$ | geometry | scalar | $\mathsf F$ | PROVED |
| C90 | collinear triad null | $\mathsf C$ | geometry | scalar | $\mathsf F$ | PROVED |
| C91 | phase decomposition $\mathcal T=\mathcal A\sin\Phi$ | $\mathsf C$ | relational | $\mathsf X$ | $\mathsf F$ | EXACT |
| C92 | geometry/amplitude determines transfer sign | $\mathsf C$ | — | amplitude/geometry only | $\mathsf F$ | REFUTED as observation architecture |
| C93 | strain/velocity transfer equivalence | $\mathsf C$ | linear relation | targeted | $\mathsf F$ | PROVED |
| C94 | covariance triad representation | $\mathsf C$ | global continuous triads | $\mathsf X$ | $\mathsf F$ | EXACT |
| C95 | phase-coherent triad threshold | $\mathsf C$ | feedback | targeted | $\mathsf F$ | EXACT reformulation |
| C96 | unconditional signed triad inequality | $\mathsf C$ | continuous triads | targeted | $\mathsf F$ | OPEN / STOP-C13 |

---

# 26. What has actually been learned

The problem from Round 08:

$$
\operatorname{Cov}(r,\vartheta)
\stackrel{?}{\le}
\nu\operatorname{Cov}(r,r^2).
$$

Round 09 has completely expanded the left side:

$$
\boxed{
G
\operatorname{Cov}(r,\vartheta)
=
\iint
w_k(r_k-m)
\mathcal A
\sin\Phi
\,dp\,dk.
}
$$

Thus, the missing theorem is no longer:

> controlling some abstract covariance.

Rather, it is:

$$
\boxed{
\textbf{
control the signed phase-coherent continuous triad integral.
}
}
$$

Furthermore:

- radial jumps are not free;
- collinear triads do not transfer;
- total energy is only redistributed, not created;
- but the relative phase can flip the transfer sign.

Therefore, the minimal unresolved information has now advanced from amplitude / geometry to:

$$
\boxed{
\textbf{phase organization across the continuous triad field}.
}
$$

---

# 27. Next round — continuous triad phase dynamics

The next round will directly study the dynamics of:

$$
\boxed{
\Phi(k;p,q,t)
}
$$

We cannot just perform an isolated ODE on a single triad, because in the full NS, each mode simultaneously participates in continuum many triads.

Next round objectives:

1. Define the modal amplitude–phase:

$$
\widehat u(k)
=
R_k
e^{i\phi_k}
e_k
$$

in a gauge-safe version;

2. Write:

$$
\Phi
$$

as mode phases + polarization geometry;

3. Derive the exact / admissible form of:

$$
\partial_t\Phi
$$

4. Determine whether phase coherence has a self-dephasing mechanism;

5. If the differentiation of the triad phase introduces quadruple interactions / nested convolutions, check whether continuous resummation can be performed again;

6. Only if the phase dynamics can ultimately be closed via discrete helical sign classes or shell graphs, will we record:

$$
T_{\mathsf C\to\mathsf D}.
$$

At present, premature discretization simply because "shells are commonly used in the literature" is still not permitted.

---

# 28. External primary-source anchors

1. Ganapati Sahoo, Luca Biferale, *Disentangling the triadic interactions in Navier-Stokes equations*, arXiv:1510.09006.
   - Fourier/helical triad structure;
   - different triad classes can contribute to different transfer directions;
   - competition of triadic interaction types.

2. Nicholas M. Rathmann, Peter D. Ditlevsen, *The role of helicity in triad interactions in 3D turbulence investigated in a new shell model*, arXiv:1602.02553.
   - Fourier/helical triads;
   - energy and helicity conservation within nonlinear triadic interactions as the structural starting point.

3. Fabian Waleffe, *The nature of triad interactions in homogeneous turbulence*, Physics of Fluids A 4, 350 (1992).
   - classical exact helical decomposition and triad-instability analysis.
   - This round does not use helical sign classification as a necessary proof tool; it serves only as a triad-structure external anchor.

The commutator, angular-null, phase-flexibility, and covariance-triad formulas in this checkpoint are direct derivations in the present route.

---

# 29. Commit state

$$
\boxed{
\begin{aligned}
\text{Route}
&:
\mathrm{Pure\ Continuous\ Fourier\ Triad\ Geometry},
\\
\text{Essential }\mathsf C\to\mathsf D
&:
\mathrm{Not\ reached},
\\
\text{Abstract transfer rate}
&:
\mathrm{expanded\ into\ actual\ NS\ triads},
\\
\text{Exact weighted mechanism}
&:
\mathrm{transport\text{-}multiplier\ commutator},
\\
\text{Radial jump}
&:
\mathrm{mediator\text{-}limited},
\\
\text{Collinear triad}
&:
\mathrm{null},
\\
\text{Signed transfer}
&:
\mathcal A\sin\Phi,
\\
\text{Geometry + amplitude}
&:
\mathrm{insufficient\ for\ sign},
\\
\text{Round08 }\zeta
&:
\mathrm{signed\ phase\text{-}coherent\ triad\ ratio},
\\
\text{STOP-C13}
&:
\mathrm{Triad\ Phase\text{-}Coherence/Commutator\text{-}Sign\ Gap},
\\
\text{Next}
&:
\mathrm{Continuous\ Triad\ Phase\ Dynamics}.
\end{aligned}
}
$$