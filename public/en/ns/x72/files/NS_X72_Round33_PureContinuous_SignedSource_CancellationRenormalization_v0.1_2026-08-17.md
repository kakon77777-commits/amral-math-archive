# NS × X Integral × 24/72 Paradigm Practice
## Round 33 — Pure Continuous Signed-Source / Cancellation-Preserving Renormalization Route

- Date: 2026-08-17
- Version: v0.1
- Status: Proof-Route Experiment / Continuous-Only Signed-Source Branch
- canonical source: UTF-8 Markdown
- canonical math delimiters: inline `$...$`; display `$$...$$`
- Previous round: `NS_X72_Round32_PureContinuous_SourceParticipation_Renormalization_v0.1_2026-08-17.md`
- Objective of this round: Round 32 showed that smooth positive source participation has universal Fisher anti-concentration, but the determinant / $G_Q$ has a sign interface, and the positive part of the raw pressure / Biot–Savart pair kernel destroys principal-value cancellation. This round no longer forces the source to be positive, but directly tracks the signed net, total variation, Jordan balance, cancellation efficiency, and cancellation-preserving kernel renormalization.
- Non-claims: This document does not prove that the signed total variation or renormalized pair variation is unconditionally bounded. This document establishes lossless signed-source bookkeeping, the local determinant Kato route, and the second-difference renormalization of the smooth-branch even Calderón–Zygmund kernel.

---

# 0. Round 32 handoff

Round 32 established for a smooth positive source:

$$
W>0
$$

the following:

$$
\boxed{
\mathfrak J_W
=
\frac{
\mathbb E_{\mu_Q}[W^2]
}{
\mathbb E_{\mu_Q}[W]^2
}
}
$$

and the universal participation dynamics:

$$
\boxed{
(\log\mathfrak J_W)'
=
-2\nu\langle|\nabla\log W|^2\rangle_2
+
\text{tilt selection}
+
\text{relative-source bias}.
}
$$

However, three source classes exhibit representation leakage:

1. determinant:
   $$
   (-\det S)_+;
   $$
2. positive quotient growth:
   $$
   (G_Q)_+;
   $$
3. pair singular kernel:
   $$
   \mathcal C_+.
   $$

The first two have a moving sign interface.

The third may even cause the positive-part pair mass near the diagonal to diverge due to:

$$
|x-y|^{-3}
$$

Round 32 STOP:

$$
\boxed{
\text{STOP-C36}
=
\text{Source-Participation Trapping / Singular-Source Renormalization Gap}.
}
$$

---

# 1. Signed source ledger

Let:

$$
(\Omega,\mu)
$$

be a probability space,

and:

$$
W\in L^1(\mu)
$$

be allowed to be positive or negative.

Define the signed net:

$$
\boxed{
M_W
=
\mathbb E_\mu[W].
}
\tag{1.1}
$$

Define the total variation magnitude:

$$
\boxed{
V_W
=
\mathbb E_\mu[|W|].
}
\tag{1.2}
$$

Naturally, we have:

$$
\boxed{
|M_W|
\le
V_W.
}
\tag{1.3}
$$

---

# 2. Jordan reconstruction

Define:

$$
W_+
=
\max\{W,0\},
$$

$$
W_-
=
\max\{-W,0\}.
$$

Then:

$$
W=W_+-W_-,
$$

$$
|W|=W_++W_-.
$$

Let:

$$
P_W
=
\mathbb E[W_+],
$$

$$
N_W
=
\mathbb E[W_-].
$$

Therefore:

$$
\boxed{
P_W
=
\frac{
V_W+M_W
}{2},
}
\tag{2.1}
$$

$$
\boxed{
N_W
=
\frac{
V_W-M_W
}{2}.
}
\tag{2.2}
$$

Named:

$$
\boxed{
\textbf{Signed-Source Jordan Reconstruction}.
}
$$

Thus, a local signed source does not require establishing an independent differential equation for:

$$
W_+
$$

first in order to determine the positive mass.

As long as:

$$
M_W,
\qquad
V_W
$$

are controllable, we can losslessly reconstruct:

$$
P_W,
\qquad
N_W.
$$

---

# 3. Cancellation coefficient

If:

$$
V_W>0,
$$

define the signed balance:

$$
\boxed{
c_W
=
\frac{
M_W
}{
V_W
}
\in[-1,1].
}
\tag{3.1}
$$

and the unsigned cancellation efficiency:

$$
\boxed{
\kappa_W
=
1-|c_W|
\in[0,1].
}
\tag{3.2}
$$

Interpretation:

$$
|c_W|=1
$$

indicates almost no positive/negative cancellation;

$$
c_W=0
$$

indicates that the signed net is entirely due to equal positive/negative variation cancellation.

Jordan fractions:

$$
\boxed{
\frac{
P_W
}{
V_W
}
=
\frac{
1+c_W
}{2},
}
\tag{3.3}
$$

$$
\boxed{
\frac{
N_W
}{
V_W
}
=
\frac{
1-c_W
}{2}.
}
\tag{3.4}
$$

---

# 4. Magnitude participation

If:

$$
|W|\in L^2(\mu),
$$

define the total-variation participation ratio:

$$
\boxed{
\mathfrak J_{|W|}
=
\frac{
\mathbb E[W^2]
}{
V_W^2
}.
}
\tag{4.1}
$$

Since:

$$
|W|^2=W^2.
$$

This is the total variation measure:

$$
\boxed{
d\nu_{|W|}
=
\frac{
|W|
}{
V_W
}
d\mu
}
\tag{4.2}
$$

with respect to:

$$
\mu
$$

being:

$$
1+\chi^2.
$$

---

# 5. Jordan Occupancy Bound

If a measurable set:

$$
A
$$

carries at least a:

$$
\beta_+
$$

fraction of the positive source:

$$
\boxed{
\int_A
W_+
d\mu
\ge
\beta_+
P_W,
}
\tag{5.1}
$$

Then:

$$
\int_A|W|d\mu
\ge
\beta_+
P_W
=
\beta_+
\frac{
1+c_W
}{2}
V_W.
$$

Applying the Source–Occupancy Lemma to:

$$
|W|
$$

yields:

$$
\boxed{
\mu(A)
\ge
\frac{
\beta_+^2
(1+c_W)^2
}{
4
\mathfrak J_{|W|}
}.
}
\tag{5.2}
$$

Similarly, if $A$ carries a $\beta_-$ fraction of the negative source:

$$
\boxed{
\mu(A)
\ge
\frac{
\beta_-^2
(1-c_W)^2
}{
4
\mathfrak J_{|W|}
}.
}
\tag{5.3}
$$

Named:

$$
\boxed{
\textbf{Jordan Occupancy Bound}.
}
$$

Therefore, the dangerous positive fraction of a signed source can still be used to control occupancy via:

$$
\text{total variation intermittency}
+
\text{signed cancellation balance}
$$

---

# 6. Why this is better than differentiating $W_+$

If:

$$
W
$$

crosses:

$$
0,
$$

the derivative of the positive part:

$$
W_+
$$

contains a moving sign-interface structure.

However:

$$
M_W
=
\mathbb E[W]
$$

preserves signed smoothness,

while:

$$
V_W
=
\mathbb E[|W|]
$$

can be handled by Kato / convex renormalization.

Therefore:

$$
\boxed{
\text{signed net + total variation}
}
$$

is generally more suitable than:

$$
\boxed{
\text{positive part alone}
}
$$

as a continuous renormalized carrier.

---

# 7. Signed determinant equation in convection–diffusion form

Let:

$$
\boxed{
d
=
-\det S.
}
\tag{7.1}
$$

From Round 32:

$$
\boxed{
D_td
=
-\nu
\operatorname{cof}S:\Delta S
+
\frac14
|S\omega|^2
+
\operatorname{cof}S:H_p.
}
\tag{7.2}
$$

For the scalar function:

$$
F(S)=\det S,
$$

the chain rule gives:

$$
\Delta F(S)
=
DF(S):\Delta S
+
\sum_k
D^2F(S)
[
\partial_kS,
\partial_kS
].
$$

Define:

$$
\boxed{
\mathcal G_{\det}
=
\sum_k
D^2\det(S)
[
\partial_kS,
\partial_kS
].
}
\tag{7.3}
$$

Since:

$$
d=-\det S,
$$

we obtain:

$$
\boxed{
D_td
-
\nu\Delta d
=
\nu\mathcal G_{\det}
+
\frac14
|S\omega|^2
+
\operatorname{cof}S:H_p.
}
\tag{7.4}
$$

Let:

$$
\boxed{
F_d
=
\nu\mathcal G_{\det}
+
\frac14
|S\omega|^2
+
\operatorname{cof}S:H_p.
}
\tag{7.5}
$$

Then:

$$
\boxed{
\partial_td
+
u\cdot\nabla d
-
\nu\Delta d
=
F_d.
}
\tag{7.6}
$$

---

# 8. Signed determinant net and total variation

Since:

$$
\nabla\cdot u=0,
$$

if there is sufficient decay:

$$
\boxed{
M_D(t)
=
\int
d\,dx
}
\tag{8.1}
$$

satisfies:

$$
\boxed{
M_D'
=
\int
F_d\,dx.
}
\tag{8.2}
$$

And:

$$
\boxed{
V_D(t)
=
\int
|d|dx
}
\tag{8.3}
$$

is obtained from the scalar parabolic Kato inequality as:

$$
\boxed{
V_D'
\le
\int
\operatorname{sgn}(d)
F_d\,dx
}
\tag{8.4}
$$

in the classical / regularized sense.

More precisely, the smooth convex approximation:

$$
\phi_\varepsilon(d)
=
\sqrt{
d^2+\varepsilon^2
}
$$

generates a nonnegative diffusion defect:

$$
\nu
\phi_\varepsilon''(d)
|\nabla d|^2.
$$

Taking:

$$
\varepsilon\downarrow0
$$

yields the Kato-type total-variation dissipation.

---

# 9. Dangerous determinant positive mass without positive-part PDE

The dangerous determinant production:

$$
\boxed{
P_D
=
\int
d_+dx
}
\tag{9.1}
$$

can be reconstructed as:

$$
\boxed{
P_D
=
\frac{
V_D+M_D
}{2}.
}
\tag{9.2}
$$

The negative determinant mass is:

$$
\boxed{
N_D
=
\frac{
V_D-M_D
}{2}.
}
\tag{9.3}
$$

Therefore:

$$
\boxed{
\textbf{
determinant sign interface can be handled by signed net + Kato total variation,
without differentiating }d_+\textbf{ directly}.
}
}
\tag{9.4}
$$

This is a partial repair of the Round 32 determinant sign-interface leakage.

---

# 10. Net determinant returns to vortex stretching

The whole-space identity:

$$
\boxed{
\int
\omega^\top S\omega\,dx
=
-4
\int
\det Sdx.
}
\tag{10.1}
$$

Thus:

$$
\boxed{
M_D
=
\int
(-\det S)dx
=
\frac14
\int
\omega^\top S\omega\,dx.
}
\tag{10.2}
$$

Therefore, the determinant cancellation coefficient is:

$$
\boxed{
c_D
=
\frac{
\frac14
\int
\omega^\top S\omega dx
}{
\int
|\det S|dx
}.
}
\tag{10.3}
$$

It directly measures:

> how much of the total determinant variation truly remains as net vortex-stretching production.

---

# 11. Strong positive production can arise in two distinct ways

Since:

$$
P_D
=
\frac{
V_D+M_D
}{2},
$$

a large positive determinant production can arise from:

## D1 — large variation, weak cancellation

$$
V_D\gg1,
\qquad
c_D\approx1.
$$

## D2 — large two-sided variation, strong cancellation

$$
V_D\gg1,
\qquad
|c_D|\ll1,
$$

but:

$$
P_D
\sim
V_D/2
$$

is still very large.

Therefore:

$$
\boxed{
\text{small net vortex stretching}
}
$$

does not imply:

$$
\boxed{
\text{small dangerous positive determinant activity}.
}
$$

It could simply be that:

$$
\boxed{
\text{large positive and negative determinant production cancel globally}.
}
$$

Thus, total variation is an indispensable relational carrier.

---

# 12. Signed source cancellation versus concentration

A signed source requires two independent coordinates:

$$
\boxed{
\text{concentration}
=
\mathfrak J_{|W|}
}
$$

and:

$$
\boxed{
\text{cancellation}
=
c_W.
}
$$

A high:

$$
\mathfrak J_{|W|}
$$

indicates that the magnitude is concentrated in a small amount of carrier mass.

A small:

$$
|c_W|
$$

indicates that the positive / negative magnitudes are highly balanced.

Therefore:

$$
\boxed{
\textbf{
magnitude concentration and sign cancellation are logically independent.
}
}
\tag{12.1}
$$

This is precisely the information that the Round 32 positive-source representation failed to express.

---

# 13. Even homogeneous singular kernels

Now we handle the pair singular source.

Consider:

$$
\boxed{
K(z)
=
\frac{
\Omega(e)
}{
|z|^3
},
\qquad
e=\frac z{|z|},
}
\tag{13.1}
$$

where:

$$
\boxed{
\Omega(-e)=\Omega(e),
}
\tag{13.2}
$$

and the spherical mean-zero property:

$$
\boxed{
\int_{\mathbb S^2}
\Omega(e)d\Omega(e)
=
0.
}
\tag{13.3}
$$

The pressure anisotropic Hessian kernel:

$$
3e\otimes e-I
$$

belongs to this class.

The Round 26 exact Biot–Savart strain kernel, as a linear operator in remote vorticity, also possesses the same:

- degree $-3$;
- even angular kernel;
- spherical mean-zero;

structure.

---

# 14. Symmetric second-difference renormalization

Let the scalar / vector source:

$$
f
$$

be sufficiently smooth.

Consider the truncated principal value:

$$
T_\delta f(x)
=
\int_{
\delta<|z|<R_0
}
K(z)
f(x-z)
\,dz.
$$

Since:

$$
K(-z)=K(z),
$$

averaging:

$$
z
\leftrightarrow
-z
$$

yields:

$$
T_\delta f(x)
=
\frac12
\int_{
\delta<|z|<R_0
}
K(z)
[
f(x-z)+f(x+z)
]
dz.
$$

Using the mean-zero property again:

$$
\int_{\delta<|z|<R_0}
K(z)dz=0,
$$

we obtain the exact:

$$
\boxed{
T_\delta f(x)
=
\frac12
\int_{
\delta<|z|<R_0
}
K(z)
\left[
f(x-z)+f(x+z)-2f(x)
\right]
dz.
}
\tag{14.1}
$$

Named:

$$
\boxed{
\textbf{Cancellation-Preserving Second-Difference Renormalization}.
}
$$

---

# 15. Near-diagonal integrability after renormalization

If:

$$
f\in C^2,
$$

Taylor expansion gives:

$$
\boxed{
|f(x+z)+f(x-z)-2f(x)|
\le
C
|z|^2
\sup_{|y-x|\le|z|}
|\nabla^2f(y)|.
}
\tag{15.1}
$$

While:

$$
|K(z)|
\lesssim
|z|^{-3}.
$$

The three-dimensional volume element is:

$$
dz
\sim
r^2drd\Omega.
$$

Therefore, the renormalized absolute magnitude near:

$$
r=0
$$

is at most:

$$
\boxed{
r^{-3}
\cdot
r^2
\cdot
r^2dr
=
r\,dr.
}
\tag{15.2}
$$

Thus:

$$
\boxed{
\int_0^\delta
r\,dr
<
\infty.
}
$$

Therefore, in the smooth branch,

the signed principal-value cancellation can first be compiled into:

$$
\boxed{
\Delta_z^2f(x)
=
f(x+z)+f(x-z)-2f(x)
}
$$

before discussing the absolute magnitude.

---

# 16. Why raw positive extraction diverges but renormalized magnitude need not

The raw positive / absolute kernel:

$$
|K(z)f(x)|
$$

near the diagonal:

$$
\sim
r^{-3}
$$

gives:

$$
\int_0^\delta
r^{-3}r^2dr
=
\int_0^\delta
\frac{dr}{r}
=
\infty.
$$

But the cancellation-preserving source:

$$
K(z)\Delta_z^2f(x)
$$

gives:

$$
\int_0^\delta
r\,dr
<
\infty.
$$

Therefore:

$$
\boxed{
\textbf{
the problem was not singularity alone;
it was taking magnitude before encoding the cancellation.
}
}
\tag{16.1}
$$

This directly corrects the Round 32 Positive-Pair Cancellation-Destruction No-Go:

> positive extraction of the raw kernel is illegal;
> positive magnitude of a losslessly renormalized second-difference kernel can be legal in a smooth branch.

---

# 17. Log-shell cancellation profile

For:

$$
0<r<R_0,
$$

define the signed shell:

$$
\boxed{
\Sigma_f(r;x)
=
\int_{\mathbb S^2}
\Omega(e)
f(x-re)
\,d\Omega(e).
}
\tag{17.1}
$$

Then:

$$
\boxed{
T_\delta f(x)
=
\int_\delta^{R_0}
\frac{
\Sigma_f(r;x)
}{
r
}
dr.
}
\tag{17.2}
$$

The mean-zero property:

$$
\int\Omega=0
$$

removes the constant term.

Evenness:

$$
\Omega(-e)=\Omega(e)
$$

removes the first-order odd term.

Therefore, in the smooth branch:

$$
\boxed{
\Sigma_f(r;x)
=
O(r^2).
}
\tag{17.3}
$$

Thus:

$$
\boxed{
\frac{
\Sigma_f(r;x)
}{
r
}
=
O(r),
}
\tag{17.4}
$$

near:

$$
r=0.
$$

This transforms the principal-value cancellation into a continuous log-radius profile.

---

# 18. Raw shell variation versus signed shell

Define the absolute shell envelope:

$$
\boxed{
A_f(r;x)
=
\int_{\mathbb S^2}
|\Omega(e)|
|f(x-re)|
d\Omega(e).
}
\tag{18.1}
$$

The raw total variation:

$$
\int
A_f(r;x)
\frac{dr}{r}
$$

generally logarithmically diverges.

But the signed shell:

$$
\Sigma_f(r;x)
$$

can be:

$$
O(r^2).
$$

Therefore, define the shell cancellation coefficient:

$$
\boxed{
c_{\rm shell}(r;x)
=
\frac{
\Sigma_f(r;x)
}{
A_f(r;x)
}
}
\tag{18.2}
$$

When generic:

$$
A_f(r;x)\to A_0>0
$$

we have:

$$
\boxed{
c_{\rm shell}(r;x)
=
O(r^2).
}
\tag{18.3}
$$

That is, near the diagonal:

$$
\boxed{
\text{the raw magnitude is huge,
but the signed fraction approaches zero}.
}
$$

This is the continuous quantitative signature of singular-integral cancellation.

---

# 19. Renormalized pair variation

Define:

$$
\boxed{
\widetilde W_f(x,z)
=
\frac12
K(z)
[
f(x+z)+f(x-z)-2f(x)
].
}
\tag{19.1}
$$

Its renormalized total variation:

$$
\boxed{
\widetilde V_f
=
\iint_{
|z|<R_0
}
|
\widetilde W_f(x,z)
|
\,dz\,d\mu_Q(x)
}
\tag{19.2}
$$

can be finite in the smooth / sufficient second-difference regularity branch.

At this point, we can further define:

$$
\boxed{
\widetilde{\mathfrak J}_{\rm pair}
=
\frac{
\mathbb E[
|\widetilde W_f|^2
]
}{
\mathbb E[
|\widetilde W_f|
]^2
}
}
\tag{19.3}
$$

if the second moment is also finite.

Therefore, pair occupancy can be re-legitimized on the:

$$
\boxed{
\text{renormalized pair source}
}
$$

---

# 20. Regularity cost of cancellation-preserving renormalization

Section 15 uses:

$$
C^2
$$

only as the most intuitive sufficient condition.

What is truly needed is the second-difference modulus:

$$
\boxed{
\omega_2(f,r)
=
\sup_x
\sup_{|z|\le r}
|
f(x+z)+f(x-z)-2f(x)
|.
}
\tag{20.1}
$$

As long as:

$$
\boxed{
\int_0^{R_0}
\frac{
\omega_2(f,r)
}{
r
}
dr
<
\infty,
}
\tag{20.2}
$$

the renormalized local singular integral possesses an absolute convergence envelope.

Therefore, the new proof obligation is not:

$$
f\in C^2
$$

itself,

but rather some form of continuous Dini/Besov second-difference control.

---

# 21. Renormalization circularity warning

For pressure:

$$
f_p
=
|S|^2-\frac12|\omega|^2.
$$

controlling:

$$
\omega_2(f_p,r)
$$

requires spatial regularity of the strain / vorticity.

For Biot–Savart strain:

$$
f=\omega.
$$

controlling:

$$
\omega_2(\omega,r)
$$

similarly requires higher spatial regularity.

Therefore:

$$
\boxed{
\text{cancellation-preserving renormalization is structurally legal,
but its absolute-variation budget is not basic-energy free}.
}
\tag{21.1}
$$

This once again connects back to the Round 05/30 higher-derivative budget.

---

# 22. Signed source ledger for nonlocal kernels

For the separated / renormalized pair source:

$$
\widetilde W
$$

we can now simultaneously track:

$$
\boxed{
M_{\widetilde W}
=
\mathbb E[\widetilde W],
}
$$

$$
\boxed{
V_{\widetilde W}
=
\mathbb E[|\widetilde W|],
}
$$

$$
\boxed{
c_{\widetilde W}
=
M_{\widetilde W}/V_{\widetilde W},
}
$$

and:

$$
\boxed{
\mathfrak J_{|\widetilde W|}.
}
$$

Thus, the signed pair source can also be factored into:

$$
\boxed{
\text{magnitude}
\times
\text{concentration}
\times
\text{cancellation}.
}
$$

This preserves more original kernel information than the raw positive-source probability.

---

# 23. Cancellation-First Principle

This round yields a crucial principle for X-integral / representation routing:

$$
\boxed{
\textbf{
For a signed singular operator,
encode the exact cancellation before taking magnitude,
positive part, occupancy, or probability normalization.
}
}
\tag{23.1}
$$

Otherwise:

$$
\boxed{
\text{representation may create a divergence
that the original operator does not possess}.
}
$$

Named:

$$
\boxed{
\textbf{Cancellation-First Principle}.
}
$$

This is the formal correction for the Round 32 positive-pair failure.

---

# 24. STOP-C37 — Signed-Variation / Cancellation-Renormalization Budget Gap

$$
\boxed{
\begin{aligned}
\text{layer}
&=
\mathrm{signed\ source\ renormalization},
\\
\text{local signed source}
&=
M_W+V_W,
\\
\text{positive/negative reconstruction}
&=
(V_W\pm M_W)/2,
\\
\text{cancellation carrier}
&=
c_W=M_W/V_W,
\\
\text{concentration carrier}
&=
\mathfrak J_{|W|},
\\
\text{determinant sign interface}
&=
\text{partially repaired by Kato total variation},
\\
\text{raw pair positive extraction}
&=
\text{illegal near singular diagonal},
\\
\text{even mean-zero kernel}
&=
\text{second-difference renormalizable},
\\
\text{renormalized near-diagonal magnitude}
&=
O(r\,dr),
\\
\text{missing}
&=
\text{unconditional control of signed total variation,
second-difference regularity and renormalized pair participation},
\\
T_{\mathsf C\to\mathsf D}
&=
\text{NOT REACHED}.
\end{aligned}
}
$$

Named:

$$
\boxed{
\textbf{STOP-C37:
Signed-Variation / Cancellation-Renormalization Budget Gap}.
}
$$

---

# 25. 24/72 Ledger — Round 33

| Step | object | $B$ | $U$ | $O$ | $L$ | status |
|---|---|---|---|---|---|---|
| C473 | signed net $M_W$ | $\mathsf C$ | signed measure | scalar | $\mathsf F$ | FORM |
| C474 | total variation $V_W$ | $\mathsf C$ | magnitude measure | scalar | $\mathsf F$ | FORM |
| C475 | Jordan reconstruction | $\mathsf C$ | algebraic measure | targeted | $\mathsf F$ | EXACT |
| C476 | cancellation coefficient $c_W$ | $\mathsf C$ | recognition | scalar | $\mathsf F$ | FORM |
| C477 | magnitude participation $\mathfrak J_{|W|}$ | $\mathsf C$ | measure separation | scalar | $\mathsf F$ | FORM |
| C478 | Jordan Occupancy Bound | $\mathsf C$ | Cauchy / measure | targeted | $\mathsf F$ | PROVED |
| C479 | determinant convection–diffusion equation | $\mathsf C$ | PDE renormalization | relational | $\mathsf F$ | EXACT |
| C480 | determinant Kato variation bound | $\mathsf C$ | convex renormalization | scalar | $\mathsf F$ | CONDITIONAL EXACT/INEQUALITY |
| C481 | determinant positive-mass reconstruction | $\mathsf C$ | Jordan decomposition | targeted | $\mathsf F$ | EXACT |
| C482 | determinant cancellation / vortex stretching | $\mathsf C$ | strain-vorticity bridge | relational | $\mathsf F$ | EXACT |
| C483 | concentration-vs-cancellation split | $\mathsf C$ | signed measure | $\mathsf X$ | $\mathsf F$ | FORM |
| C484 | even mean-zero kernel class | $\mathsf C$ | singular integral | relational | $\mathsf F$ | FORM |
| C485 | second-difference renormalization | $\mathsf C$ | cancellation-preserving transform | targeted | $\mathsf F$ | EXACT |
| C486 | near-diagonal absolute integrability | $\mathsf C$ | second difference | scalar | $\mathsf F$ | PROVED in smooth branch |
| C487 | log-shell cancellation profile | $\mathsf C$ | continuous radius | profile | $\mathsf F$ | EXACT |
| C488 | shell cancellation coefficient | $\mathsf C$ | signed angular average | scalar profile | $\mathsf F$ | FORM |
| C489 | renormalized pair variation | $\mathsf C$ | product measure | scalar | $\mathsf F$ | FORM |
| C490 | Cancellation-First Principle | $\mathsf C$ | representation logic | $\mathsf X$ | $\mathsf F$ | ESTABLISHED |
| C491 | unconditional renormalized variation control | $\mathsf C$ | higher regularity | targeted | $\mathsf F$ | OPEN / STOP-C37 |

---

# 26. Continuous-versus-discrete status

The core new operation of this round:

$$
f(x+z)+f(x-z)-2f(x)
$$

is the continuous symmetric second difference.

The shell parameter:

$$
r\in(0,R_0)
$$

is continuous.

The angular variable:

$$
e\in\mathbb S^2
$$

is continuous.

The signed Jordan decomposition also belongs to continuous measure theory.

There are no:

- atoms;
- shell index $j$;
- discrete cancellation pairs;
- graph singular-integral representations.

Therefore:

$$
\boxed{
T_{\mathsf C\to\mathsf D}
=
\text{NOT YET REACHED}.
}
$$

---

# 27. Strongest results of Round 33

## R33-A — Jordan reconstruction

$$
\boxed{
P_W=\frac{V_W+M_W}{2},
\qquad
N_W=\frac{V_W-M_W}{2}.
}
$$

## R33-B — Jordan occupancy

$$
\boxed{
\mu(A)
\ge
\frac{
\beta_+^2(1+c_W)^2
}{
4\mathfrak J_{|W|}
}
}
$$

for a positive-source-dominant set.

## R33-C — determinant sign-interface repair

$$
\boxed{
P_D
=
\frac{
\int|-\det S|dx
+
\int(-\det S)dx
}{
2}.
}
$$

Therefore, the positive determinant mass can be reconstructed from the signed net + Kato variation.

## R33-D — cancellation-preserving singular-kernel renormalization

$$
\boxed{
T_\delta f(x)
=
\frac12
\int
K(z)
[
f(x-z)+f(x+z)-2f(x)
]dz.
}
$$

## R33-E — renormalized near-diagonal integrability

$$
\boxed{
|K(z)|\sim r^{-3},
\quad
|\Delta_z^2f|\sim r^2
\Rightarrow
|\widetilde W|\,dz
\sim
r\,dr.
}
$$

## R33-F — Cancellation-First Principle

$$
\boxed{
\text{encode cancellation first;
take magnitude / probability second}.
}
$$

---

# 28. Next round — Cancellation Budget Dynamics

Round 33 has upgraded the source decomposition from:

$$
\text{positive only}
$$

to:

$$
\boxed{
\text{net}
+
\text{variation}
+
\text{concentration}
+
\text{cancellation}.
}
$$

The next round will directly investigate:

$$
\boxed{
c_W(t)
=
\frac{
M_W(t)
}{
V_W(t)
}
}
$$

and the dynamics of the renormalized shell cancellation.

Core questions:

1. Does the determinant:
   $$
   c_D(t)
   $$
   have a depletion / anti-cancellation law?

2. Can large positive and negative determinant activities mutually cancel over the long term?

3. How is the shell cancellation coefficient:
   $$
   c_{\rm shell}(r,t)
   $$
   altered by advection / strain / diffusion?

4. Does the total variation of the second-difference renormalized source exhibit Kato-like dynamics?

5. If the signed cancellation rapidly oscillates, does it reconnect with the Round 10 / 27 phase cancellation?

6. If cancellation weakens, does the positive source occupancy directly increase?

7. If cancellation strengthens, must a spatial/angular oscillation budget be paid?

8. Still maintaining continuous radius and signed measures.

---

# 29. External primary-source anchors

1. Borys Álvarez-Samaniego, Wilson P. Álvarez-Samaniego, Pedro G. Fernández-Dalgo, *On the use of the Riesz transforms to determine the pressure term in the incompressible Navier-Stokes equations on the whole space*, arXiv:2004.02588.
   - Background on the Riesz-transform singular-integral representation of whole-space pressure.

2. Benjamin Jaye, Tomás Merchán, *On the problem of existence in principal value of a Calderón-Zygmund operator on a space of non-homogeneous type*, arXiv:1810.13299.
   - Harmonic-analysis background on principal-value existence depending on cancellation and underlying measure geometry.

3. Evan Miller, *On the interaction of strain and vorticity for solutions of the Navier--Stokes equation*, arXiv:2407.02691.
   - Background on strain–vorticity interaction and determinant / nonlinear depletion.

The Jordan source reconstruction, Jordan Occupancy Bound, determinant Kato route, second-difference singular-kernel renormalization, shell cancellation profile, and Cancellation-First Principle in this round are all directly derived in this document.

---

# 30. Commit state

$$
\boxed{
\begin{aligned}
\text{Route}
&=
\mathrm{Pure\ Continuous\ Signed\text{-}Source/Cancellation\ Renormalization},
\\
\text{Essential }\mathsf C\to\mathsf D
&=
\mathrm{Not\ reached},
\\
\text{Signed source carrier}
&=
(M_W,V_W,c_W,\mathfrak J_{|W|}),
\\
\text{Positive source}
&=
\mathrm{Jordan\ reconstructable},
\\
\text{Determinant interface}
&=
\mathrm{Kato\text{-}renormalizable},
\\
\text{Raw pair positive source}
&=
\mathrm{not\ lossless},
\\
\text{Signed even kernel}
&=
\mathrm{second\text{-}difference\ renormalizable},
\\
\text{Renormalized pair magnitude}
&=
\mathrm{locally\ finite\ under\ second\text{-}difference\ regularity},
\\
\text{STOP-C37}
&=
\mathrm{Signed\text{-}Variation/Cancellation\text{-}Renormalization\ Budget\ Gap},
\\
\text{Next}
&=
\mathrm{Cancellation\ Budget\ Dynamics}.
\end{aligned}
}
$$