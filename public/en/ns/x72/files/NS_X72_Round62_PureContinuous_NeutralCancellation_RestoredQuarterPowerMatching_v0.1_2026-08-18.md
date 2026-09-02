# NS × X Integration × 24/72 Paradigm in Practice
## Round 62 — Pure Continuous Neutral-Residual Cancellation / Restored Quarter-Power Matching Law

- Date: 2026-08-18
- Version: v0.1
- Status: Proof-Route Experiment / Continuous-Only Schur-Renormalized Matching Branch
- canonical source: UTF-8 Markdown
- canonical math delimiters: inline `$...$`; display `$$...$$`
- Previous round: `NS_X72_Round61_PureContinuous_FastSlowStableBundle_OptimalMatchingExponent_v0.1_2026-08-18.md`
- Goal of this round: In Round 61, treating all same-parity far-neighbor terms as generic $O(j^{-2})$ perturbations yielded a safe overlap
  $$
  j_m=\nu^{-2/7}
  $$
  and a coarse
  $$
  O(\nu^{1/7})
  $$
  matching target. This round examines the remainder of the fast-Schur reduction acting specifically on the **neutral direction**, and discovers that the first-order $j^{-2}$ contribution exhibits exact cancellation, thereby reducing the slow self-drift to $O(j^{-3})$.
- Main results:
  1. Define the neutral residual
     $$
     S_n
     =
     -A_{-2}^{(n)}
     +
     A_0^{(n)}
     -
     A_2^{(n)}
     +
     A_4^{(n)};
     $$
     then
     $$
     \boxed{
     \lim_{n\to\infty}
     n^3S_n
     =
     48K^3;
     }
     $$
  2. If the frozen same-parity characteristic polynomial is
     $$
     F_n(r)
     =
     -A_{-2}^{(n)}
     +
     A_0^{(n)}r
     -
     A_2^{(n)}r^2
     +
     A_4^{(n)}r^3,
     $$
     then
     $$
     F_n'(1)
     =
     -4K+O(n^{-1});
     $$
  3. Therefore, the neutral root has
     $$
     \boxed{
     r_{\rm neu}(n)
     =
     1+
     \frac{12K^2}{n^3}
     +
     O(n^{-4});
     }
     $$
  4. in parity index $n\sim2j$,
     $$
     \boxed{
     r_{\rm neu}
     =
     1+
     \frac{3K^2}{2j^3}
     +
     O(j^{-4});
     }
     $$
  5. the exact rescaled viscous coupling coefficients
     $$
     a_e(j,\nu)
     =
     -\nu
     \frac{
     b_{2j}
     }{
     A_2^{(2j)}
     },
     $$
     $$
     a_o(j,\nu)
     =
     -\nu
     \frac{
     b_{2j+1}
     }{
     A_2^{(2j+1)}
     }
     $$
     satisfy
     $$
     \boxed{
     a_e
     =
     a_j
     \left(
     1+\frac1j+O(j^{-2})
     \right),
     }
     $$
     $$
     \boxed{
     a_o
     =
     a_j
     \left(
     1+\frac2j+O(j^{-2})
     \right),
     }
     $$
     where
     $$
     a_j
     =
     \frac{16\nu j^2}{K};
     $$
  6. after fast-Schur renormalization, the conservative slow matching budget becomes
     $$
     \nu j_m^3,
     \qquad
     j_m^{-1},
     \qquad
     \frac{j_m^{-3}}{\nu j_m^2};
     $$
  7. for
     $$
     j_m=\nu^{-\alpha},
     $$
     these are
     $$
     \nu^{1-3\alpha},
     \qquad
     \nu^\alpha,
     \qquad
     \nu^{5\alpha-1};
     $$
  8. all three balance exactly at
     $$
     \boxed{
     \alpha_\ast=\frac14;
     }
     $$
  9. hence the Schur-renormalized first theorem target returns to
     $$
     \boxed{
     j_m=\nu^{-1/4},
     \qquad
     \operatorname{dist}
     \left(
     E_\nu^{\min},
     E_0^{\rm Jost}
     \right)
     =
     O(\nu^{1/4});
     }
     $$
  10. Round 61's $2/7$ law remains valid as a **pre-Schur generic-error safety budget**; Round 62 explains why it is not expected to be sharp after the exact neutral cancellation is exploited;
  11. full six-dimensional physical stable-plane diagnostics at
      $$
      j_m=\nu^{-1/4}
      $$
      are substantially stronger than the quarter-power target;
  12. at
      $$
      \nu=10^{-8},
      $$
      the largest principal angles are
      $$
      \boxed{
      \theta_{\max,-}
      \approx
      7.27\times10^{-4},
      }
      $$
      and
      $$
      \boxed{
      \theta_{\max,+}
      \approx
      1.82\times10^{-3};
      }
      $$
  13. the normalized quantities
      $$
      \theta_{\max}/\nu^{1/4}
      $$
      decrease strongly over the tested small-viscosity sequence;
  14. empirical log-slopes over the final four points are approximately
      $$
      0.52
      $$
      and
      $$
      0.56\text{--}0.58,
      $$
      again faster than the conservative exponent $1/4$;
  15. Remaining proof obligation: build an actual fast Schur graph and prove that its induced slow projective/Riccati remainder obeys the neutral-cancelled bounds uniformly, then propagate the resulting $O(\nu^{1/4})$ interval to Round 59's positive center functional.
- Non-claims: This round does not yet prove the full
  $$
  O(\nu^{1/4})
  $$
  stable-bundle theorem, nor a positive-viscosity interval. The exact parts are the neutral residual cancellation, neutral-root asymptotic coefficient and viscous-coupling asymptotics; the restored quarter-power theorem is the quantitatively corrected proof target supported by full 6D diagnostics.

---

# 0. Round 61 handoff

Round 61 factorized the endpoint leading parity cubic:

$$
\boxed{
\epsilon+r-r^2-\epsilon r^3
=
-(r-1)
[
\epsilon r^2+(1+\epsilon)r+\epsilon
].
}
\tag{0.1}
$$

Thus each parity has:

$$
\boxed{
1\text{ neutral}
+
1\text{ fast minimal}
+
1\text{ fast growing}.
}
\tag{0.2}
$$

For:

$$
\nu>0,
$$

the two neutral directions couple into a slow stable/unstable pair, while the two fast minimal lines persist.

Round 61 therefore proposed:

$$
E_\nu^{\min}
=
E_{\rm fast,e}^{\min}
\oplus
E_{\rm fast,o}^{\min}
\oplus
E_{\rm slow}^{-}.
$$

Without yet exploiting neutral cancellation, its generic roughness budget gave:

$$
\boxed{
j_m=\nu^{-2/7},
\qquad
O(\nu^{1/7}).
}
\tag{0.3}
$$

Round 61 STOP:

$$
\boxed{
\text{STOP-C65}
=
\text{Fast-Schur / Slow-Riccati Quantitative Gap}.
}
$$

---

# 1. The neutral residual is not $O(j^{-2})$

The same-parity frozen recurrence is:

$$
\boxed{
-
A_{-2}^{(n)}
x_{m-1}
+
A_0^{(n)}
x_m
-
A_2^{(n)}
x_{m+1}
+
A_4^{(n)}
x_{m+2}
=
0.
}
\tag{1.1}
$$

A pure neutral constant profile:

$$
x_m\equiv1
$$

has residual:

$$
\boxed{
S_n
=
-
A_{-2}^{(n)}
+
A_0^{(n)}
-
A_2^{(n)}
+
A_4^{(n)}.
}
\tag{1.2}
$$

Individually:

$$
A_{-2}^{(n)},
A_4^{(n)}
=
O(n^{-2}),
$$

and:

$$
A_0^{(n)}-A_2^{(n)}
$$

also contains $O(n^{-2})$ structure.

But these contributions cancel on the neutral vector.

Exact symbolic evaluation gives:

$$
\boxed{
\lim_{n\to\infty}
n^3S_n
=
48K^3.
}
\tag{1.3}
$$

Therefore:

$$
\boxed{
S_n
=
\frac{
48K^3
}{
n^3
}
+
O(n^{-4}).
}
\tag{1.4}
$$

Designation:

$$
\boxed{
\textbf{Neutral Residual Cancellation}.
}
$$

---

# 2. Neutral frozen root

Define:

$$
\boxed{
F_n(r)
=
-
A_{-2}^{(n)}
+
A_0^{(n)}r
-
A_2^{(n)}r^2
+
A_4^{(n)}r^3.
}
\tag{2.1}
$$

Then:

$$
F_n(1)=S_n.
$$

Also:

$$
\boxed{
F_n'(1)
=
A_0^{(n)}
-
2A_2^{(n)}
+
3A_4^{(n)}.
}
\tag{2.2}
$$

Exact asymptotics give:

$$
\boxed{
F_n'(1)
=
-4K
+
O(n^{-1}).
}
\tag{2.3}
$$

Since the limiting derivative is nonzero, the nearby neutral root is simple.

Put:

$$
r
=
1+
\frac c{n^3}.
$$

Then:

$$
\boxed{
\lim_{n\to\infty}
n^3
F_n
\left(
1+\frac c{n^3}
\right)
=
48K^3
-
4Kc.
}
\tag{2.4}
$$

Hence:

$$
\boxed{
c=12K^2.
}
\tag{2.5}
$$

Therefore:

$$
\boxed{
r_{\rm neu}(n)
=
1+
\frac{
12K^2
}{
n^3
}
+
O(n^{-4}).
}
\tag{2.6}
$$

For:

$$
n=2j+O(1),
$$

$$
\boxed{
r_{\rm neu}
=
1+
\frac{
3K^2
}{
2j^3
}
+
O(j^{-4}).
}
\tag{2.7}
$$

---

# 3. Numerical neutral-root audit

For each parity, let:

$$
r_{\rm neu}^{e/o}(j)
$$

be the local frozen eigenvalue closest to:

$$
1.
$$

Then:

$$
\boxed{
\frac{
j^3
(
r_{\rm neu}^{e/o}(j)-1
)
}{
(3/2)K^2
}
\to1.
}
\tag{3.1}
$$

The included verification checks this directly for both source fibres and both parity sectors.

This confirms that the $j^{-3}$ residual controls the actual local neutral eigenvalue drift, not merely the constant test profile.

---

# 4. Exact viscous coupling normalization

In the desingularized variables:

$$
E_j=e_j/\nu,
\qquad
o_j,
$$

define the one-step parity couplings:

$$
\boxed{
a_e(j,\nu)
=
-\nu
\frac{
b_{2j}
}{
A_2^{(2j)}
},
}
\tag{4.1}
$$

$$
\boxed{
a_o(j,\nu)
=
-\nu
\frac{
b_{2j+1}
}{
A_2^{(2j+1)}
}.
}
\tag{4.2}
$$

Let:

$$
\boxed{
a_j
=
\frac{
16\nu j^2
}{
K
}.
}
\tag{4.3}
$$

Exact symbolic limits give:

$$
\boxed{
\lim_{j\to\infty}
j
\left[
\frac{
a_e(j,\nu)
}{
a_j
}
-
1
\right]
=
1,
}
\tag{4.4}
$$

and:

$$
\boxed{
\lim_{j\to\infty}
j
\left[
\frac{
a_o(j,\nu)
}{
a_j
}
-
1
\right]
=
2.
}
\tag{4.5}
$$

Thus:

$$
\boxed{
a_e
=
a_j
[
1+j^{-1}+O(j^{-2})
],
}
\tag{4.6}
$$

$$
\boxed{
a_o
=
a_j
[
1+2j^{-1}+O(j^{-2})
].
}
\tag{4.7}
$$

The dominant relative coupling correction is therefore:

$$
\boxed{
O(j^{-1}).
}
\tag{4.8}
$$

---

# 5. Schur-renormalized slow error scales

The two fast modes are generated by the $O(j^{-2})$ same-parity coefficients.

But on the neutral direction, their direct self-action cancels to:

$$
O(j^{-3}).
$$

After the fast pair is absorbed into the reference Schur graph, the conservative slow matching budget becomes:

## E1 — cumulative viscous attenuation before matching

$$
\boxed{
\mathcal E_{\rm WKB}
\sim
\nu j_m^3.
}
\tag{5.1}
$$

## E2 — relative coupling / basis drift

$$
\boxed{
\mathcal E_{\rm coup}
\sim
j_m^{-1}.
}
\tag{5.2}
$$

## E3 — neutral self-drift relative to slow gap

The slow gap is:

$$
\asymp
\nu j_m^2.
$$

The neutral drift is:

$$
\asymp
j_m^{-3}.
$$

Hence:

$$
\boxed{
\mathcal E_{\rm neu}
\sim
\frac{
j_m^{-3}
}{
\nu j_m^2
}
=
\frac1{
\nu j_m^5
}.
}
\tag{5.3}
$$

These are the three leading conservative post-Schur errors.

---

# 6. General post-Schur overlap exponent

Set:

$$
\boxed{
j_m=\nu^{-\alpha}.
}
\tag{6.1}
$$

Then:

$$
\boxed{
\mathcal E_{\rm WKB}
=
\nu^{1-3\alpha},
}
\tag{6.2}
$$

$$
\boxed{
\mathcal E_{\rm coup}
=
\nu^\alpha,
}
\tag{6.3}
$$

and:

$$
\boxed{
\mathcal E_{\rm neu}
=
\nu^{5\alpha-1}.
}
\tag{6.4}
$$

A direct perturbative overlap requires:

$$
\boxed{
\alpha<1/3
}
$$

and:

$$
\boxed{
\alpha>1/5.
}
$$

Define:

$$
\boxed{
\beta_{\rm Schur}(\alpha)
=
\min
\{
1-3\alpha,\,
\alpha,\,
5\alpha-1
\}.
}
\tag{6.5}
$$

---

# 7. Restored optimal quarter-power law

Set the three exponents equal:

$$
1-3\alpha
=
\alpha,
$$

and:

$$
5\alpha-1
=
\alpha.
$$

Both give:

$$
\boxed{
4\alpha=1.
}
$$

Therefore:

$$
\boxed{
\alpha_\ast
=
\frac14.
}
\tag{7.1}
$$

At:

$$
\alpha=1/4,
$$

$$
\boxed{
1-3\alpha
=
\alpha
=
5\alpha-1
=
\frac14.
}
\tag{7.2}
$$

Hence the Schur-renormalized matching target is:

$$
\boxed{
j_m
=
\nu^{-1/4},
}
\tag{7.3}
$$

and:

$$
\boxed{
\operatorname{dist}
\left(
E_\nu^{\min}(j_m),
E_0^{\rm Jost}(j_m)
\right)
=
O(
\nu^{1/4}
).
}
\tag{7.4}
$$

Designation:

$$
\boxed{
\textbf{Restored Quarter-Power Matching Law}.
}
$$

The statement (7.4) remains a theorem target; the exponent balance is now structurally self-consistent after neutral cancellation.

---

# 8. Relation to the Round 61 $2/7$ law

Round 61 used:

$$
\boxed{
\mathcal E_{\rm generic}
\sim
\frac{
j_m^{-2}
}{
\nu j_m^2
}
=
\frac1{
\nu j_m^4
}.
}
\tag{8.1}
$$

This corresponds to treating all $O(j^{-2})$ coefficients as generic slow perturbations.

Balancing:

$$
\nu j_m^3
$$

with:

$$
1/(\nu j_m^4)
$$

gave:

$$
\alpha=2/7.
$$

Round 62 shows:

$$
\boxed{
j^{-2}
\text{ is not the correct slow self-drift after neutral projection}.
}
$$

Instead:

$$
\boxed{
j^{-3}
}
$$

appears because of exact cancellation.

Therefore:

- $2/7$ is a valid conservative **pre-Schur** proof budget;
- $1/4$ is the refined **post-Schur** target.

There is no contradiction.

---

# 9. Full six-dimensional quarter-power diagnostics

The verification script computes the physical six-dimensional minimal three-plane and the $\nu=0$ endpoint selected Jost three-plane directly, with no compact hidden-block basis quotient.

Use:

$$
\boxed{
j_m
=
\operatorname{round}
(
\nu^{-1/4}
).
}
\tag{9.1}
$$

The largest principal angle is:

$$
\theta_{\max}
=
\theta_{\max}
(
E_\nu^{\min},
E_0^{\rm Jost}
).
$$

---

# 10. Small fibre

For:

$$
K_-=\sqrt{17}-3,
$$

$$
\boxed{
\begin{array}{c|c|c|c}
\nu
&
j_m
&
\theta_{\max}
&
\theta_{\max}/\nu^{1/4}
\\
\hline
10^{-4}
&
10
&
8.5906\times10^{-2}
&
8.5906\times10^{-1}
\\
10^{-5}
&
18
&
2.5709\times10^{-2}
&
4.5717\times10^{-1}
\\
10^{-6}
&
32
&
7.7570\times10^{-3}
&
2.4532\times10^{-1}
\\
10^{-7}
&
56
&
2.3143\times10^{-3}
&
1.3015\times10^{-1}
\\
10^{-8}
&
100
&
7.2665\times10^{-4}
&
7.2665\times10^{-2}
\end{array}
}
\tag{10.1}
$$

The normalized quarter-power ratio decreases rapidly.

---

# 11. Large fibre

For:

$$
K_+=\sqrt{17}+3,
$$

$$
\boxed{
\begin{array}{c|c|c|c}
\nu
&
j_m
&
\theta_{\max}
&
\theta_{\max}/\nu^{1/4}
\\
\hline
10^{-4}
&
10
&
3.8287\times10^{-1}
&
3.8287
\\
10^{-5}
&
18
&
9.1156\times10^{-2}
&
1.6210
\\
10^{-6}
&
32
&
2.2736\times10^{-2}
&
7.1899\times10^{-1}
\\
10^{-7}
&
56
&
6.3743\times10^{-3}
&
3.5842\times10^{-1}
\\
10^{-8}
&
100
&
1.8174\times10^{-3}
&
1.8174\times10^{-1}
\end{array}
}
\tag{11.1}
$$

Again the normalized ratio decreases strongly.

---

# 12. Empirical principal-angle exponents

A log-log fit over the smallest four viscosities gives approximately:

### small fibre

$$
\boxed{
\theta_{\max}
\sim
\nu^{0.517\ldots}
}
\tag{12.1}
$$

### large fibre

$$
\boxed{
\theta_{\max}
\sim
\nu^{0.566\ldots}
}
\tag{12.2}
$$

These numerical exponents are not claimed as true asymptotic invariants.

They only show:

$$
\boxed{
\nu^{1/4}
}
$$

is a very conservative target in the tested range.

---

# 13. Direct local neutral-drift diagnostic

Let:

$$
r_{\rm neu}^{e/o}(j)
$$

denote the local frozen root nearest:

$$
1.
$$

The verification computes:

$$
\boxed{
D_{e/o}(j)
=
\frac{
j^3
[
r_{\rm neu}^{e/o}(j)-1
]
}{
(3/2)K^2
}.
}
\tag{13.1}
$$

For both fibres and both parities:

$$
\boxed{
D_{e/o}(j)\to1.
}
\tag{13.2}
$$

This independently confirms the exact neutral-residual derivation.

---

# 14. Why full stable-plane convergence can be faster

The quarter-power budget still treats:

$$
j^{-1}
$$

coupling corrections generically.

But:

1. the Round 59 Jost graph already incorporates nontrivial algebraic tail geometry;
2. the two parity coupling corrections are structured rather than arbitrary;
3. the fast Schur graph can absorb part of the local basis variation;
4. reflection and $\mathcal C$ symmetry eliminate several possible mixing channels.

Thus the actual remainder may begin beyond the first conservative:

$$
O(j^{-1})
$$

term in the projective coordinate relevant to the Fredholm functional.

This is consistent with empirical exponents around:

$$
1/2.
$$

No improved exponent is claimed without an explicit Schur/Riccati calculation.

---

# 15. Slow projective coordinate

After eliminating the two fast lines, let the effective slow vector be:

$$
\boxed{
Y_j^{\rm slow}
=
\begin{pmatrix}
E_j\\
o_j
\end{pmatrix}.
}
\tag{15.1}
$$

Define:

$$
\boxed{
z_j
=
\frac{
E_j
}{
o_j
}.
}
\tag{15.2}
$$

For the Round 60 reduced matrix:

$$
M(a)
=
\begin{pmatrix}
1&a\\
a&1+a^2
\end{pmatrix},
$$

the exact projective map is:

$$
\boxed{
z_{j+1}
=
\frac{
z_j+a_j
}{
a_jz_j+1+a_j^2
}.
}
\tag{15.3}
$$

Its two frozen fixed points solve:

$$
\boxed{
z^2+a z-1=0.
}
\tag{15.4}
$$

The stable-amplitude eigenline corresponds to the negative projective root:

$$
\boxed{
z_-(a)
=
-\frac{
a+\sqrt{a^2+4}
}{
2
}.
}
\tag{15.5}
$$

The next rigorous proof should perturb this scalar Riccati map by the exact neutral-cancelled Schur remainder.

---

# 16. Corrected Riccati remainder target

The desired effective equation is:

$$
\boxed{
z_{j+1}
=
\frac{
z_j+a_j
}{
a_jz_j+1+a_j^2
}
+
\mathcal R_j(z_j;\nu).
}
\tag{16.1}
$$

Round 62 identifies the structural scales that should enter:

$$
\boxed{
|\mathcal R_j|
\lesssim
\frac1j
\cdot
a_j
+
\frac1{j^3}
+
\text{higher fast-Schur terms}.
}
\tag{16.2}
$$

Relative to the slow gap:

$$
a_j,
$$

this becomes:

$$
\boxed{
\frac{
|\mathcal R_j|
}{
a_j
}
\lesssim
\frac1j
+
\frac1{
\nu j^5
}
+
\cdots.
}
\tag{16.3}
$$

At:

$$
j=\nu^{-1/4},
$$

both displayed terms are:

$$
\boxed{
O(\nu^{1/4}).
}
\tag{16.4}
$$

This is the quantitative inequality the next round should prove with explicit constants.

---

# 17. Consequence if the quarter-power enclosure is completed

Round 59 rigorously proved:

$$
\boxed{
c_{0,-}>5.79,
\qquad
c_{0,+}>5.33.
}
\tag{17.1}
$$

Suppose Round 63 obtains:

$$
\boxed{
\left|
\frac{
a_3(\nu)
}{
\nu
}
-
c_0
\right|
\le
C_\ast
\nu^{1/4}.
}
\tag{17.2}
$$

Then any explicit:

$$
\nu_s
$$

satisfying:

$$
\boxed{
C_\ast
\nu_s^{1/4}
<
5
}
\tag{17.3}
$$

already yields:

$$
\boxed{
a_3(\nu)>0
\qquad
0<\nu\le\nu_s.
}
\tag{17.4}
$$

The exact Fredholm same-sign identity would then extend the Round 56 hidden-rescue no-go from:

$$
\nu=1
$$

to an actual open viscosity interval adjacent to:

$$
0.
$$

---

# 18. STOP-C66 — Neutral-Cancelled Schur/Riccati Enclosure Gap

$$
\boxed{
\begin{aligned}
\text{layer}
&=
\mathrm{small\text{-}viscosity\ fast\text{-}Schur/slow\text{-}Riccati\ matching},
\\
S_n
&=
-A_{-2}+A_0-A_2+A_4,
\\
n^3S_n
&\to
48K^3,
\\
r_{\rm neu}(n)
&=
1+12K^2n^{-3}+O(n^{-4}),
\\
a_e/a_j
&=
1+j^{-1}+O(j^{-2}),
\\
a_o/a_j
&=
1+2j^{-1}+O(j^{-2}),
\\
\text{post-Schur error budget}
&=
\nu j_m^3
+
j_m^{-1}
+
(\nu j_m^5)^{-1},
\\
\text{optimal overlap}
&=
j_m=\nu^{-1/4},
\\
\text{first theorem target}
&=
O(\nu^{1/4}),
\\
\text{6D physical diagnostics}
&=
\mathrm{faster\ than\ quarter\text{-}power},
\\
\text{remaining task}
&=
\mathrm{explicit\ invariant\ fast\ Schur\ graph}
+
\mathrm{slow\ Riccati\ interval\ remainder},
\\
\text{small-viscosity positivity interval}
&=
\mathrm{not\ yet\ rigorous},
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
\textbf{STOP-C66:
Neutral-Cancelled Schur/Riccati Enclosure Gap}.
}
$$

---

# 19. 24/72 Ledger — Round 62

| Step | object | $B$ | $U$ | $O$ | $L$ | status |
|---|---|---|---|---|---|---|
| C991 | neutral residual $S_n$ | $\mathsf C$ | same-parity transfer | scalar | $\mathsf F$ | EXACT |
| C992 | $n^3S_n\to48K^3$ | $\mathsf C$ | asymptotic cancellation | scalar | $\mathsf F$ | PROVED |
| C993 | frozen neutral root drift | $\mathsf C$ | local spectrum | scalar | $\mathsf F$ | DERIVED |
| C994 | even viscous coupling asymptotic | $\mathsf C$ | slow coupling | scalar | $\mathsf F$ | PROVED |
| C995 | odd viscous coupling asymptotic | $\mathsf C$ | slow coupling | scalar | $\mathsf F$ | PROVED |
| C996 | Schur-renormalized error budget | $\mathsf C$ | fast–slow geometry | relational | $\mathsf F$ | DERIVED |
| C997 | general post-Schur exponent | $\mathsf C$ | matched asymptotics | scalar | $\mathsf F$ | DERIVED |
| C998 | restored $\alpha=1/4$ optimum | $\mathsf C$ | exponent optimization | scalar | $\mathsf F$ | PROVED within budget model |
| C999 | relation to $2/7$ safety law | $\mathsf C$ | route audit | targeted | $\mathsf F$ | CLARIFIED |
| C1000 | 6D quarter-power principal angles | $\mathsf C$ | physical stable bundle | profile | $\mathsf F$ | NUMERICALLY VERIFIED |
| C1001 | neutral-root numerical audit | $\mathsf C$ | frozen spectrum | scalar | $\mathsf F$ | VERIFIED |
| C1002 | reduced slow Riccati map | $\mathsf C$ | projective dynamics | scalar | $\mathsf F$ | EXACT reduced model |
| C1003 | neutral-cancelled Riccati remainder scale | $\mathsf C$ | Schur perturbation | scalar | $\mathsf F$ | TARGET IDENTIFIED |
| C1004 | explicit small-$\nu$ positivity interval | $\mathsf C$ | validated continuation | targeted | $\mathsf F$ | OPEN / STOP-C66 |

---

# 20. Continuous-versus-discrete status

The neutral cancellation is an asymptotic spectral identity of the continuous periodic Floquet operator.

The coefficient label:

$$
n
$$

is its Fourier chart, not a discrete physical substrate.

The Schur/Riccati reduction is a coordinate description of the invariant spectral subspaces of that continuous operator family.

The remaining validation is an interval enclosure of the continuous parameter:

$$
\nu.
$$

Therefore:

$$
\boxed{
T_{\mathsf C\to\mathsf D}
=
\text{NOT YET REACHED}.
}
$$

---

# 21. Strongest results of Round 62

## R62-A — exact neutral cancellation

$$
\boxed{
S_n
=
48K^3n^{-3}
+
O(n^{-4}).
}
$$

## R62-B — neutral root drifts only at cubic order

$$
\boxed{
r_{\rm neu}
=
1+
12K^2n^{-3}
+
O(n^{-4}).
}
$$

## R62-C — exact first coupling corrections

$$
\boxed{
a_e/a_j
=
1+j^{-1}+O(j^{-2}),
}
$$

$$
\boxed{
a_o/a_j
=
1+2j^{-1}+O(j^{-2}).
}
$$

## R62-D — Schur-renormalized optimal overlap

$$
\boxed{
j_m
=
\nu^{-1/4}.
}
$$

## R62-E — corrected theorem target

$$
\boxed{
\operatorname{dist}
(
E_\nu^{\min},
E_0^{\rm Jost}
)
=
O(\nu^{1/4}).
}
$$

## R62-F — physical data are comfortably stronger

At:

$$
\nu=10^{-8},
$$

$$
\boxed{
\theta_{\max,-}
\approx
7.27\times10^{-4},
}
$$

$$
\boxed{
\theta_{\max,+}
\approx
1.82\times10^{-3}.
}
$$

---

# 22. Next round — Explicit Fast-Schur Graph / Validated Slow-Riccati Bound

Round 62 has now identified the cancellation needed to make the quarter-power proof self-consistent.

The next round should stop changing scaling laws and actually build the invariant graph.

Concrete targets:

1. choose the local same-parity eigenbasis:
   $$
   \{
   v_{\rm fast}^{\min},
   v_{\rm neu},
   v_{\rm fast}^{\max}
   \};
   $$

2. write the full six-dimensional rescaled transfer in this biorthogonal basis;

3. solve the two fast coordinates as invariant graphs over the slow neutral pair;

4. exploit:
   $$
   r_{\rm fast}^{\min}=O(j^{-2}),
   \qquad
   r_{\rm fast}^{\max}=O(j^2)
   $$
   to obtain uniform graph contraction;

5. prove the induced neutral self-drift is:
   $$
   O(j^{-3})
   $$
   with explicit constants, not merely asymptotically;

6. prove the coupling corrections:
   $$
   |a_e/a_j-1|
   \le
   C/j,
   $$
   $$
   |a_o/a_j-1|
   \le
   C/j;
   $$

7. derive an explicit interval Riccati map:
   $$
   z_{j+1}
   =
   \frac{
   z_j+a_j
   }{
   a_jz_j+1+a_j^2
   }
   +
   \mathcal R_j;
   $$

8. establish:
   $$
   |\mathcal R_j|
   \le
   C_1a_j/j
   +
   C_2/j^3;
   $$

9. evaluate the bound at:
   $$
   j_m=\nu^{-1/4};
   $$

10. propagate the resulting interval through the Round 59 endpoint pullback and obtain the first explicit:
    $$
    0<\nu\le\nu_s
    \Longrightarrow
    a_3(\nu)>0.
    $$

This becomes:

$$
\boxed{
\textbf{Explicit Fast-Schur Graph / Validated Slow-Riccati Bound}.
}
$$

---

# 23. External primary-source anchors

1. F. Battelli, M. Franca, K. J. Palmer, *Exponential Dichotomy for Noninvertible Linear Difference Equations*, arXiv:2111.04553.
   - primary-source roughness results for exponential dichotomies of finite-dimensional difference equations;
   - relevant to invariant fast/slow graph persistence under coefficient perturbations.

2. Evans M. Harrell II, Manwah Lilian Wong, *On the behavior at infinity of solutions to difference equations in Schroedinger form*, arXiv:1109.4691.
   - develops variation-of-constants comparison and a discrete Liouville–Green/WKB transformation;
   - relevant to comparing the exact slow projective dynamics with a WKB reference equation.

3. Pierre Del Moral, Emma Horton, *A note on Riccati matrix difference equations*, arXiv:2107.12918.
   - studies time-varying Riccati difference equations, duality formulae and uniform bounds;
   - relevant structural context for the planned nonautonomous interval Riccati enclosure.

4. Yuri Latushkin, Shibi Vasudevan, *Fredholm determinants, continued fractions, Jost and Evans functions for a Jacobi matrix associated with the 2D-Euler equations*, arXiv:2401.14037.
   - connects Jost / Evans / Fredholm / continued-fraction descriptions in a hydrodynamic difference equation;
   - relevant to connecting the slow Riccati line back to the Round 59 endpoint Jost functional.

All NS-specific cancellation identities, coupling asymptotics, matching exponent balances and Grassmannian diagnostics are direct results of this project.

---

# 24. Commit state

$$
\boxed{
\begin{aligned}
\text{Route}
&=
\mathrm{Pure\ Continuous\ Neutral\text{-}Cancelled\ Fast\text{-}Schur/Slow\text{-}Riccati},
\\
\text{Essential }\mathsf C\to\mathsf D
&=
\mathrm{Not\ reached},
\\
\text{Generic pre-Schur law}
&=
2/7,
\\
\text{Exact neutral cancellation}
&=
j^{-2}
\to
j^{-3},
\\
\text{Post-Schur optimal overlap}
&=
1/4,
\\
\text{First corrected error target}
&=
O(\nu^{1/4}),
\\
\text{6D physical convergence}
&=
\mathrm{stronger\ than\ corrected\ target},
\\
\text{Remaining proof object}
&=
\mathrm{explicit\ fast\ invariant\ graph}
+
\mathrm{validated\ slow\ Riccati\ remainder},
\\
\text{STOP-C66}
&=
\mathrm{Neutral\text{-}Cancelled\ Schur/Riccati\ Enclosure\ Gap},
\\
\text{Next}
&=
\mathrm{Explicit\ Fast\text{-}Schur\ Graph/Validated\ Slow\text{-}Riccati\ Bound}.
\end{aligned}
}
$$