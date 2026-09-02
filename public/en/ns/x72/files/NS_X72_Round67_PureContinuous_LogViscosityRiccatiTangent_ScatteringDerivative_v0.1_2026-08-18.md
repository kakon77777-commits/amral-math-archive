# NS × X Integral × 24/72 Paradigm in Action
## Round 67 — Pure Continuous Log-Viscosity Riccati Tangent / Singular Scattering Derivative

- Date: 2026-08-18
- Version: v0.1
- Status: Proof-Route Experiment / Continuous-Only Parameter-Tangent Branch
- Previous round: Round 66 — Fixed-Size Jost–Riccati Graph
- canonical math delimiters: inline `$...$`; display `$$...$$`

## 0. Round 66 handoff

Round 66 produced the fixed-size minimal Jost graph

$$
Y_n^+
=
G_nY_n^-,
\qquad
G_n\in\mathbb R^{3\times3},
$$

with exact pullback

$$
G_n
=
(G_{n+1}C-A_n)^{-1}
(B_n-G_{n+1}D),
$$

and central readout

$$
\boxed{
a_3(\nu)
=
-\,(G_1)_{22}.
}
$$

It also removed the dense-memory wall:

$$
\text{memory}=O(1),
\qquad
\text{time}=O(J).
$$

The remaining problem was continuous parameter continuation through the final singular strip.

---

# 1. Why the correct parameter is $t=\log\nu$

The only explicit viscosity dependence in the transfer matrix is

$$
\beta_n(\nu)
=
\nu
\frac{
b_n
}{
A_4^{(n)}
}.
$$

Directly differentiating with respect to $\nu$ makes the deep-tail coefficient

$$
b_n/A_4
$$

look enormous.

Instead set

$$
\boxed{
t=\log\nu.
}
$$

Then

$$
\boxed{
\partial_t\beta_n
=
\beta_n.
}
$$

So geometric viscosity chunks become fixed-width intervals in $t$, and the tangent forcing has the same natural scale as the transfer coefficient itself.

Designation:

$$
\boxed{
\textbf{Log-Viscosity Gauge}.
}
$$

---

# 2. Exact first Riccati tangent

Define

$$
X_n
=
G_{n+1}C-A_n,
$$

and

$$
R_n
=
D+CG_n.
$$

The Riccati equation is

$$
X_nG_n
=
B_n-G_{n+1}D.
$$

Let

$$
\boxed{
H_n
=
\partial_tG_n.
}
$$

Only $A_n$ depends explicitly on $t$, so define

$$
\boxed{
\dot A_n
=
\partial_tA_n.
}
$$

It has only one nonzero entry:

$$
(\dot A_n)_{13}
=
\beta_n.
$$

Differentiating the exact Riccati equation gives

$$
\boxed{
H_n
=
X_n^{-1}
\left[
\dot A_nG_n
-
H_{n+1}R_n
\right].
}
\tag{2.1}
$$

This is a closed $3\times3$ backward tangent flow.

Memory remains

$$
\boxed{
O(1).
}
$$

---

# 3. Exact second Riccati tangent

Let

$$
\boxed{
K_n
=
\partial_t^2G_n.
}
$$

Since

$$
\partial_t\dot A_n
=
\dot A_n,
$$

a second differentiation gives

$$
\boxed{
K_n
=
X_n^{-1}
\left[
\dot A_nG_n
+
2\dot A_nH_n
-
K_{n+1}R_n
-
2H_{n+1}CH_n
\right].
}
\tag{3.1}
$$

Thus $(G,H,K)$ form a closed fixed-size flow.

The attached verifier independently checks the first and second tangents against centered finite differences in

$$
t=\log\nu.
$$

---

# 4. Central tangent readout

Round 66 central readout:

$$
a_3
=
-\,(G_1)_{22}.
$$

Therefore:

$$
\boxed{
\partial_ta_3
=
-\,(H_1)_{22},
}
\tag{4.1}
$$

and

$$
\boxed{
\partial_t^2a_3
=
-\,(K_1)_{22}.
}
\tag{4.2}
$$

So the entire viscosity sensitivity of the Fredholm obstruction is now a single entry of a fixed-size tangent graph.

---

# 5. Normalized central functional

Define

$$
\boxed{
f(\nu)
=
\frac{
a_3(\nu)
}{
\nu
}.
}
\tag{5.1}
$$

Since

$$
\partial_t
=
\nu\partial_\nu,
$$

we have exactly

$$
\partial_ta_3
=
\nu a_3'(\nu).
$$

Hence

$$
\boxed{
f'(\nu)
=
\frac{
\partial_ta_3-a_3
}{
\nu^2
}.
}
\tag{5.2}
$$

Define the **Riccati scattering derivative**

$$
\boxed{
\Sigma(\nu)
:=
\frac{
\partial_ta_3-a_3
}{
\nu^2
}.
}
\tag{5.3}
$$

Then

$$
\boxed{
\Sigma(\nu)
=
f'(\nu)
}
\tag{5.4}
$$

is not an asymptotic interpretation; it is an exact identity.

This is the key reduction of Round 67.

---

# 6. Why this is the correct singular observable

Round 59 proved the endpoint constants

$$
\boxed{
c_{0,-}>5.79,
}
$$

$$
\boxed{
c_{0,+}>5.33.
}
$$

The desired final bridge is

$$
f(\nu)\to c_0
\qquad
(\nu\to0^+).
$$

Equation (5.4) gives the exact fundamental-theorem representation

$$
\boxed{
f(\nu)
=
c_0
+
\int_0^\nu
\Sigma(s)\,ds,
}
\tag{6.1}
$$

once endpoint continuity is established in the Round 59 Jost chart.

Therefore the last singular bridge does **not** require high-precision reconstruction of the entire minimal bundle.

It is enough to control the total variation:

$$
\boxed{
\int_0^{10^{-6}}
|\Sigma(s)|\,ds.
}
\tag{6.2}
$$

---

# 7. Extremely loose sufficient bound

The smaller rigorous endpoint margin is

$$
c_{0,+}>5.33.
$$

Thus any bound satisfying

$$
\boxed{
\int_0^{10^{-6}}
|\Sigma(s)|\,ds
<
5.33
}
\tag{7.1}
$$

already proves

$$
f(\nu)>0
$$

through the entire final strip.

For example, the absurdly coarse uniform estimate

$$
\boxed{
|\Sigma(\nu)|
<
10^6
\qquad
0<\nu<10^{-6}
}
\tag{7.2}
$$

would imply

$$
f(\nu)
>
5.33-1
>
4.33.
$$

So the final theorem no longer needs a sharp WKB matching constant.

It only needs a very coarse **integrable scattering-derivative bound**.

---

# 8. Actual fixed-size tangent values

The full fixed-size $(G,H,K)$ flow gives:

## Small fibre

$$
\boxed{
\begin{array}{c|c|c}
\nu
&
f_-(\nu)
&
\Sigma_-(\nu)
\\
\hline
3\times10^{-8}
&
5.79052588254
&
10.1368291
\\
10^{-7}
&
5.79052659212
&
10.1370508
\\
3\times10^{-7}
&
5.79052861951
&
10.1368022
\\
10^{-6}
&
5.79053571503
&
10.1360983
\end{array}
}
\tag{8.1}
$$

## Large fibre

$$
\boxed{
\begin{array}{c|c|c}
\nu
&
f_+(\nu)
&
\Sigma_+(\nu)
\\
\hline
3\times10^{-8}
&
5.33175244245
&
-3.4233139
\\
10^{-7}
&
5.33175220223
&
-3.4343036
\\
3\times10^{-7}
&
5.33175151531
&
-3.4357301
\\
10^{-6}
&
5.33174911023
&
-3.4359717
\end{array}
}
\tag{8.2}
$$

These are numerical diagnostics, not uniform interval bounds.

But their magnitude is approximately

$$
O(10),
$$

whereas the coarse bridge proof would tolerate

$$
O(10^6).
$$

There is roughly a five-order-of-magnitude proof margin.

---

# 9. Logarithmic elasticity

Define

$$
\boxed{
\mathcal E(\nu)
=
\frac{
\partial_ta_3
}{
a_3
}.
}
\tag{9.1}
$$

Across the tested microscopic strip:

$$
\boxed{
\mathcal E_\pm(\nu)
=
1+O(10^{-6}).
}
\tag{9.2}
$$

For example at

$$
\nu=10^{-7},
$$

$$
\boxed{
\mathcal E_-
\approx
1.00000017506,
}
$$

$$
\boxed{
\mathcal E_+
\approx
0.99999993559.
}
$$

So the central coefficient is extremely close to being exactly homogeneous of degree one in viscosity near the endpoint.

---

# 10. Singular scattering correction

If

$$
\Sigma(\nu)
\to\sigma
$$

as

$$
\nu\to0^+,
$$

then

$$
\boxed{
f(\nu)
=
c_0
+
\sigma\nu
+
o(\nu),
}
\tag{10.1}
$$

and hence

$$
\boxed{
a_3(\nu)
=
c_0\nu
+
\sigma\nu^2
+
o(\nu^2).
}
\tag{10.2}
$$

The tangent data indicate

$$
\boxed{
\sigma_-
\approx
10.137,
}
\tag{10.3}
$$

$$
\boxed{
\sigma_+
\approx
-3.436.
}
\tag{10.4}
$$

Designation:

$$
\boxed{
\textbf{Singular Jost Scattering Coefficient}.
}
$$

---

# 11. Why this matters for the $\mu=\nu^2$ endpoint formulation

Round 58 observed that after parity rescaling the **local equations** depend on viscosity through

$$
\mu=\nu^2.
$$

A regular local perturbation would therefore suggest an even expansion in $\nu$ for the rescaled variables.

But the actual minimal-at-infinity selection is singular.

The moving boundary layer at

$$
j\sim\nu^{-1/3}
$$

feeds a term linear in $\nu$ back into the center:

$$
f(\nu)-c_0
=
O(\nu),
$$

not merely

$$
O(\nu^2).
$$

So the nonanalyticity is not in the local recurrence coefficients.

It is generated by the **Jost/minimal boundary condition at infinity**.

This explains the Round 60 observation that the central matching defect was numerically linear in viscosity.

---

# 12. Agreement with Round 60

Round 60 found from direct sparse BVPs:

$$
\frac{
f_-(\nu)-c_{0,-}
}{
\nu
}
\approx
10.137,
$$

and

$$
\frac{
f_+(\nu)-c_{0,+}
}{
\nu
}
\approx
-3.435.
$$

Round 67 obtains the same constants independently from the fixed-size tangent:

$$
\Sigma
=
\frac{
\partial_ta_3-a_3
}{
\nu^2}.
$$

Thus two independent representations agree:

1. secant-to-endpoint scattering;
2. local Riccati tangent scattering.

This is a strong internal consistency check.

---

# 13. Why naive interval viscosity failed

A direct interval substitution

$$
\nu\in[\nu_-,\nu_+]
$$

into thousands of Möbius pullbacks treats repeated appearances of the same parameter as independent interval variables.

Even a relative width of order

$$
10^{-3}
$$

can therefore create a false interval explosion.

This is a representation artifact, not physical sensitivity.

The log-tangent flow keeps parameter correlation explicitly and is therefore the correct validated-continuation chart.

---

# 14. New final-bridge target

Before Round 67, the remaining task was phrased as:

$$
\text{prove the entire singular minimal graph converges to the endpoint Jost graph}.
$$

After Round 67, a much weaker sufficient target is available:

$$
\boxed{
\int_0^{10^{-6}}
|\Sigma(s)|\,ds
<
5.33.
}
\tag{14.1}
$$

A practical stronger target is simply:

$$
\boxed{
|\Sigma(\nu)|
<
10^6
\qquad
0<\nu<10^{-6}.
}
\tag{14.2}
$$

The actual observed values are below

$$
11.
$$

Thus the final bridge has become a **coarse tangent-cone theorem** rather than a precision matching theorem.

---

# 15. STOP-C71 — Validated Scattering-Derivative / Total-Variation Gap

$$
\boxed{
\begin{aligned}
\text{layer}
&=
\mathrm{log\text{-}viscosity\ Riccati\ tangent},
\\
t
&=
\log\nu,
\\
H_n
&=
\partial_tG_n,
\\
K_n
&=
\partial_t^2G_n,
\\
\text{memory}
&=
O(1),
\\
\Sigma(\nu)
&=
\frac{
\partial_ta_3-a_3
}{
\nu^2
}
=
\partial_\nu
\left(
a_3/\nu
\right),
\\
\Sigma_-^{\rm num}
&\approx
10.137,
\\
\Sigma_+^{\rm num}
&\approx
-3.436,
\\
\text{endpoint margin}
&>
5.33,
\\
\text{sufficient final bridge}
&=
\int_0^{10^{-6}}
|\Sigma|
<
5.33,
\\
\text{very coarse sufficient uniform bound}
&=
|\Sigma|<10^6,
\\
\text{remaining task}
&=
\mathrm{validated\ tangent\ cone/total\ variation\ bound},
\\
T_{\mathsf C\to\mathsf D}
&=
\mathrm{NOT\ REACHED}.
\end{aligned}
}
$$

Designation:

$$
\boxed{
\textbf{STOP-C71:
Validated Scattering-Derivative / Total-Variation Gap}.
}
$$

---

# 16. 24/72 Ledger — Round 67

| Step | object | $B$ | $U$ | $O$ | $L$ | status |
|---|---|---|---|---|---|---|
| C1059 | log-viscosity gauge | $\mathsf C$ | parameter geometry | scalar | $\mathsf F$ | IDENTIFIED |
| C1060 | first Riccati tangent | $\mathsf C$ | matrix graph flow | relational | $\mathsf F$ | EXACT |
| C1061 | second Riccati tangent | $\mathsf C$ | matrix graph flow | relational | $\mathsf F$ | EXACT |
| C1062 | central tangent readout | $\mathsf C$ | canonical observable | scalar | $\mathsf F$ | EXACT |
| C1063 | normalized functional $f=a_3/\nu$ | $\mathsf C$ | endpoint normalization | scalar | $\mathsf F$ | DEFINED |
| C1064 | scattering derivative identity | $\mathsf C$ | parameter calculus | scalar | $\mathsf F$ | EXACT |
| C1065 | O(1)-memory tangent implementation | $\mathsf C$ | proof architecture | targeted | $\mathsf F$ | VERIFIED |
| C1066 | tangent finite-difference audit | $\mathsf C$ | independent check | scalar | $\mathsf F$ | PASSED |
| C1067 | microscopic elasticity map | $\mathsf C$ | parameter diagnostic | profile | $\mathsf F$ | VERIFIED |
| C1068 | scattering coefficient diagnostics | $\mathsf C$ | singular matching | scalar | $\mathsf F$ | VERIFIED |
| C1069 | Round 60 secant/tangent agreement | $\mathsf C$ | representation cross-check | targeted | $\mathsf F$ | PASSED |
| C1070 | total-variation bridge reduction | $\mathsf C$ | endpoint theorem target | scalar | $\mathsf F$ | EXACT REDUCTION |
| C1071 | validated scattering bound | $\mathsf C$ | tangent cone | targeted | $\mathsf F$ | OPEN / STOP-C71 |

---

# 17. Continuous-versus-discrete status

The tangent graph differentiates a continuous viscosity family of admissible subspaces of the periodic Floquet operator.

The recurrence index is again only a Fourier representation coordinate.

The final proof target is a continuous-parameter total-variation estimate.

Therefore:

$$
\boxed{
T_{\mathsf C\to\mathsf D}
=
\text{NOT YET REACHED}.
}
$$

---

# 18. Next round — Validated Log-Tangent Cone / Final Total-Variation Bridge

Round 67 substantially weakens the required final theorem.

The next attack should not try to reproduce $a_3$ to many digits.

Concrete targets:

1. carry the pointwise graph enclosure and tangent enclosure simultaneously;
2. use the exact tangent map
   $$
   H_n
   =
   X_n^{-1}
   (
   \dot A_nG_n-H_{n+1}R_n
   );
   $$

3. derive a coarse interval cone for
   $$
   \Sigma(\nu)
   =
   (\partial_ta_3-a_3)/\nu^2;
   $$

4. use logarithmic viscosity chunks so parameter dependence remains scale-normalized;
5. seek only an intentionally loose envelope such as
   $$
   |\Sigma|<10^4
   $$
   or even
   $$
   <10^6;
   $$

6. integrate that envelope from the Round 59 endpoint;
7. combine with Round 65's rigorous threshold
   $$
   \nu=10^{-6};
   $$

8. if the total variation is below $5.33$, conclude
   $$
   a_3(\nu)>0
   \quad
   \forall\nu>0;
   $$

9. if successful, viscosity disappears completely from the $\sqrt{17}$ hidden-rescue branch.

This becomes:

$$
\boxed{
\textbf{Validated Log-Tangent Cone / Final Total-Variation Bridge}.
}
$$

---

# 19. External primary-source anchors

Fresh search before this round found:

1. Pierre Del Moral, Emma Horton, *A note on Riccati matrix difference equations*, arXiv:2107.12918.
   - develops time-varying Riccati difference equations, Riccati semigroup formulas and uniform bounds;
   - relevant framework for a validated tangent/perturbation flow.

2. Yuri Latushkin, Shibi Vasudevan, *Fredholm determinants, continued fractions, Jost and Evans functions for a Jacobi matrix associated with the 2D-Euler equations*, arXiv:2401.14037.
   - relates Jost, Evans, Fredholm and continued-fraction data for a hydrodynamic difference equation;
   - relevant to interpreting $\Sigma$ as a Jost-scattering sensitivity of the same Fredholm compatibility object.

These are framework anchors only. All NS-specific tangent identities, central readouts and scattering diagnostics are direct derivations of this series.