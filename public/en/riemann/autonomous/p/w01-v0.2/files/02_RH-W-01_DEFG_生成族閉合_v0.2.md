# RH-W-01-D/E/F/G: Double Vanishing Moments, Correlation Closure, and the Mellin–Fourier Interface
## Riemann Hypothesis GAP Engineering Note v0.2

**研究計畫：** RH GAP Atlas / AI Mathematical Engineering Relay  
**父節點：** `RH-W-01`  
**本輪節點：** A verifiable subfamily of `RH-W-01-A/B/C/D/E/F/G/H`  
**狀態：** `PARTIALLY_CLOSED_BY_GBUMP_FAMILY`  
**日期：** 2026-07-23  
**性質：** Test function generator and scope proof; not a proof of RH, does not establish new positivity results for the Weil quadratic form

---

## 0. Deliverables for this Round

This document constructs a non-empty, parameterizable, and computable family of functions

$$
\mathcal G_{\mathrm{bump}}
\subset \mathcal G_{B0},
$$

such that every $g\in\mathcal G_{\mathrm{bump}}$ exactly satisfies:

$$
\widetilde g(0)=\widetilde g(1)=0,
$$

and its Weil correlation form

$$
f_g(x)=\int_0^\infty g(xy)\overline{g(y)}\,dy
$$

belongs to $C_c^\infty(0,\infty)\subset\mathcal W$.

This round therefore closes the following for this specific subfamily:

- `RH-W-01-A`: Validity of all terms in the explicit formula;
- `RH-W-01-B`: Absolute convergence of the sum over zeros, eliminating ambiguity from ordering;
- `RH-W-01-C`: Removability of the apparent singularity at $x=1$;
- `RH-W-01-D`: Closure of the multiplicative correlation function;
- `RH-W-01-E`: Exact construction of the two vanishing moments;
- `RH-W-01-G`: Explicit conversion between the multiplicative Mellin and additive Fourier representations.

`F` has established a dual-implementation consistency test; `H` has established candidate metadata and validators, but has not yet been formalized in Lean/Isabelle.

---

# 1. Basic Operators

Let

$$
D:=x\frac{d}{dx}
$$

be the Euler differential operator on the multiplicative group $\mathbb R_+$, and define

$$
\mathcal A:=D(D+1).
$$

Take the seed space

$$
\mathscr H:=C_c^\infty(0,\infty),
$$

and the generated family

$$
\mathcal G_{\mathrm{bump}}
:=\mathcal A\mathscr H
=\left\{D(D+1)h:h\in C_c^\infty(0,\infty)\right\}.
$$

Since $D$ is a local differential operator, for any $h\in\mathscr H$:

$$
\operatorname{supp}(\mathcal Ah)
\subseteq\operatorname{supp}(h),
$$

and $\mathcal Ah\in C_c^\infty(0,\infty)$.

Expanding this yields:

$$
\mathcal Ah=x^2h''(x)+2xh'(x).
$$

---

# 2. Mellin Vanishing Theorem

The B0 Mellin transform is given by

$$
\widetilde h(s)=\int_0^\infty h(x)x^s\frac{dx}{x}.
$$

## Theorem 2.1

If $h\in C_c^\infty(0,\infty)$ and $g=\mathcal Ah$, then for all $s\in\mathbb C$:

$$
\boxed{
\widetilde g(s)=s(s-1)\widetilde h(s)
}.
$$

### Proof

Since $h$ is compactly supported on $(0,\infty)$, integration by parts yields no boundary terms:

$$
\widetilde{Dh}(s)
=\int_0^\infty xh'(x)x^s\frac{dx}{x}
=\int_0^\infty h'(x)x^s\,dx
=-s\widetilde h(s).
$$

Therefore:

$$
\widetilde{(D+1)h}(s)=(1-s)\widetilde h(s),
$$

Applying $D$ once more:

$$
\widetilde{D(D+1)h}(s)
=-s(1-s)\widetilde h(s)
=s(s-1)\widetilde h(s).
$$

This completes the proof.

## Corollary 2.2: Double Vanishing Moments

$$
\boxed{
\widetilde g(0)=\widetilde g(1)=0
}.
$$

That is:

$$
\int_0^\infty g(x)\frac{dx}{x}=0,
\qquad
\int_0^\infty g(x)\,dx=0.
$$

These two zeros are not the result of numerical tuning, but are a structural consequence of the operator factor $s(s-1)$.

## Direct Boundary Verification

From

$$
g(x)=\frac{d}{dx}\left(x^2h'(x)\right),
$$

we obtain:

$$
\int_0^\infty g(x)\,dx
=\left[x^2h'(x)\right]_0^\infty=0.
$$

Meanwhile:

$$
\frac{g(x)}x=xh''(x)+2h'(x)
=\frac{d}{dx}\left(xh'(x)+h(x)\right),
$$

thus:

$$
\int_0^\infty g(x)\frac{dx}{x}
=\left[xh'(x)+h(x)\right]_0^\infty=0.
$$

---

# 3. Explicit Parameterized Generator

Define the standard smooth bump function:

$$
\eta(q)=
\begin{cases}
\exp\!\left(-\dfrac1{1-q^2}\right),&|q|<1,\\[6pt]
0,&|q|\geq1.
\end{cases}
$$

Take the parameters:

$$
\theta=(A,\mu,\sigma,\tau),
\qquad
A\in\mathbb C,
\quad\mu,\tau\in\mathbb R,
\quad\sigma>0.
$$

Let

$$
h_\theta(x)
=A\,\eta\!\left(\frac{\log x-\mu}{\sigma}\right)
 e^{i\tau\log x}.
$$

Its support is:

$$
\operatorname{supp}(h_\theta)
\subseteq
\left[e^{\mu-\sigma},e^{\mu+\sigma}\right].
$$

Define:

$$
g_\theta:=D(D+1)h_\theta.
$$

Let

$$
q=\frac{\log x-\mu}{\sigma},
$$

then for $|q|<1$:

$$
\boxed{
 g_\theta(x)
 =A e^{i\tau\log x}
 \left[
 \frac{\eta''(q)}{\sigma^2}
 +\frac{1+2i\tau}{\sigma}\eta'(q)
 +(i\tau-\tau^2)\eta(q)
 \right]
}
$$

and for $|q|\geq1$, $g_\theta(x)=0$.

Finite linear combinations remain valid:

$$
g(x)=\sum_{j=1}^m c_jg_{\theta_j}(x),
$$

because $\mathcal G_{\mathrm{bump}}$ is a linear space, and both the double vanishing moments and compactly supported smoothness are preserved.

**Not Claimed:** This document does not claim that this family is dense in the final Weil test space, nor does it claim that all negative witnesses can be approximated by this family. Those are independent GAPs for `RH-W-02` and `RH-W-05`.

---

# 4. Multiplicative Correlation Closure Theorem

For $g\in C_c^\infty(0,\infty)$, define:

$$
f_g(x)
=\int_0^\infty g(xy)\overline{g(y)}\,dy.
$$

## Theorem 4.1: Support

If

$$
\operatorname{supp}(g)\subseteq[a,b],
\qquad0<a<b<\infty,
$$

then:

$$
\boxed{
\operatorname{supp}(f_g)
\subseteq\left[\frac ab,\frac ba\right]
}.
$$

Because for the integral to be non-zero, we must simultaneously have:

$$
y\in[a,b],
\qquad xy\in[a,b].
$$

For a single $g_\theta$:

$$
\operatorname{supp}(f_{g_\theta})
\subseteq[e^{-2\sigma},e^{2\sigma}].
$$

It is worth noting that this support ratio is independent of the center parameter $\mu$.

## Theorem 4.2: Smooth Closure

$$
\boxed{
f_g\in C_c^\infty(0,\infty)}.
$$

For each $k\geq0$, we can differentiate term-by-term over the finite support:

$$
f_g^{(k)}(x)
=\int_0^\infty y^k g^{(k)}(xy)\overline{g(y)}\,dy.
$$

All derivatives are continuous, and the support still lies within $[a/b,b/a]$. Therefore:

$$
C_c^\infty(0,\infty)\subset\mathcal W,
$$

thus `RH-W-01-D` is closed for this family.

---

# 5. Mellin Correlation Identity

By Fubini's theorem and the change of variables $z=xy$:

$$
\boxed{
\widetilde{f_g}(s)
=\widetilde g(s)\,
\overline{\widetilde g(1-\overline s)}
}.
$$

On the critical line $s=\tfrac12+it$:

$$
\boxed{
\widetilde{f_g}\!\left(\frac12+it\right)
=
\left|
\widetilde g\!\left(\frac12+it\right)
\right|^2
\geq0
}.
$$

This is the squared modulus identity on the Mellin side; it is not equivalent to global positivity on the Weil arithmetic side, nor can it imply RH on its own.

Since $\widetilde g(0)=\widetilde g(1)=0$:

$$
\widetilde{f_g}(0)=\widetilde{f_g}(1)=0.
$$

---

# 6. Hermitian Symmetry and Real-Value Check

The change of variables $y=xz$ gives:

$$
\boxed{
\frac1x f_g\!\left(\frac1x\right)
=\overline{f_g(x)}
}.
$$

Therefore, the paired terms in the explicit formula are:

$$
f_g(x)+\frac1x f_g\!\left(\frac1x\right)
=2\operatorname{Re}f_g(x).
$$

And:

$$
\boxed{
f_g(1)=\int_0^\infty|g(y)|^2dy\geq0}.
$$

These identities constitute the sign and conjugate regression test baseline for `RH-W-01-F`.

---

# 7. Removability of the Apparent Singularity at $x=1$

Let

$$
N_f(x)
=f(x)+x^{-1}f(x^{-1})-2x^{-1}f(1),
$$

$$
D_0(x)=x-x^{-1}.
$$

For $f\in C^1$, we have:

$$
N_f(1)=D_0(1)=0.
$$

Calculating the derivatives:

$$
N_f'(1)=f(1),
\qquad
D_0'(1)=2.
$$

Thus:

$$
\boxed{
\lim_{x\to1}
\frac{N_f(x)}{x-x^{-1}}
=\frac{f(1)}2
}.
$$

For this family $f_g\in C_c^\infty$, the integrand can be continuously extended at $x=1$, hence `RH-W-01-C` is closed.

---

# 8. Validity of Terms in the Explicit Formula

For $f_g\in C_c^\infty(0,\infty)$:

## 8.1 Arithmetic Sum is a Finite Sum

Since $f_g$ is compactly supported, there are only finitely many integers $n$ such that:

$$
f_g(n)\neq0
\quad\text{or}\quad
f_g(1/n)\neq0.
$$

Therefore, the von Mangoldt sum is not a conditionally convergent problem, but a finite sum.

## 8.2 Archimedean Integral is Finite

The integral can only be non-zero within the finite support of $f_g$; the singularity at $x=1$ has been removed in the previous section.

## 8.3 Rapid Vertical Decay of the Mellin Transform

Let $x=e^u$, then:

$$
\widetilde f(\sigma+it)
=\int_{\mathbb R}f(e^u)e^{\sigma u}e^{itu}\,du.
$$

The right side is the Fourier transform of a compactly supported smooth function. Therefore, for any compact real-part interval $I\subset\mathbb R$ and any $N$, we uniformly have:

$$
\sup_{\sigma\in I}
\left|\widetilde f(\sigma+it)\right|
=O_{I,N}\left((1+|t|)^{-N}\right).
$$

The real parts of the non-trivial zeros lie in the compact strip $[0,1]$; combined with the standard Riemann–von Mangoldt zero counting, we obtain:

$$
\sum_\rho|\widetilde f(\rho)|<\infty.
$$

Thus, the sum over zeros for this family converges absolutely, and the symmetric truncation of B0 yields the same value as any usual rearrangement. `RH-W-01-A/B` is closed for this family.

---

# 9. Additive Fourier Representation

Let:

$$
x=e^v,
\qquad y=e^u,
$$

and define the symmetrized function:

$$
\phi(u):=e^{u/2}g(e^u).
$$

Then:

$$
\boxed{
 e^{v/2}f_g(e^v)
 =\int_{\mathbb R}\phi(u+v)\overline{\phi(u)}\,du
}.
$$

That is, the multiplicative correlation becomes a standard additive autocorrelation in logarithmic coordinates.

Meanwhile:

$$
\widetilde g\!\left(\frac12+it\right)
=\int_{\mathbb R}\phi(u)e^{itu}\,du.
$$

Thus, the Fourier autocorrelation theorem re-establishes:

$$
\widetilde{f_g}\!\left(\frac12+it\right)
=|\widehat\phi(t)|^2.
$$

The $e^{u/2}$ weight is explicitly preserved here; lacking this weight would incorrectly map the B0 Mellin critical line to a different Fourier convention.

---

# 10. GAP Status Update

| ID | v0.1 | v0.2 (This Family) | Description |
|---|---|---|---|
| `RH-W-01-A` | reference / recheck | `CLOSED_FOR_GBUMP` | All terms are valid |
| `RH-W-01-B` | open alternatives | `CLOSED_FOR_GBUMP` | Absolute convergence of sum over zeros |
| `RH-W-01-C` | open per family | `CLOSED_FOR_GBUMP` | Limit is $f(1)/2$ |
| `RH-W-01-D` | open | `CLOSED_FOR_GBUMP` | $f_g\in C_c^\infty$ |
| `RH-W-01-E` | open | `CLOSED_FOR_GBUMP` | Exact zero-vanishing by $s(s-1)$ |
| `RH-W-01-F` | open | `PARTIAL_NUMERIC_CROSSCHECK` | Two correlation implementations cross-checked |
| `RH-W-01-G` | open | `CLOSED_FOR_CCINF` | Mellin–Fourier weights fixed |
| `RH-W-01-H` | open | `PARTIAL_SCHEMA_VALIDATED` | Metadata and validators established |

The parent node still cannot be marked as fully closed, because the following are not yet complete:

1. Formalization for a broader class of test functions;
2. Lean/Isabelle proof objects;
3. The final closure topology;
4. Continuity/closability of $Q_{B0}$ in this topology;
5. Compression or density of negative witnesses into this generated family.

---

# 11. What is Not Proved in This Round

This round does not prove:

$$
Q_{B0}(g)\geq0.
$$

Much less does it prove:

$$
\forall g\in\mathcal G_{B0},\quad Q_{B0}(g)\geq0.
$$

This round only engineers the "valid inputs allowed to be fed into the Weil machine." Its value is: subsequent AIs do not need to repeatedly guess how to simultaneously satisfy the two moment conditions, nor can they pass off numerical near-zeros as exact vanishing.

---

# 12. Next Relay Node

It is recommended that the next round simultaneously handles:

$$
\boxed{
\texttt{RH-W-02-A}:
\text{Select candidate closure topology and completion space}
}
$$

and:

$$
\boxed{
\texttt{RH-W-02-B}:
\overline{\operatorname{span}(\mathcal G_{\mathrm{bump}})}^{\,\tau}
\stackrel{?}{=}
\mathcal H_{\mathrm{target}}
}
$$

Until then, it must not be claimed that `GBUMP` can capture all negative witnesses.

---

# Reference Baselines

1. Enrico Bombieri, “The Riemann Hypothesis,” in *The Millennium Prize Problems*, pp. 121–122: Test function classes, explicit formula, and the Weil negativity criterion.
2. Jean-François Burnol, “The Explicit Formula in Simple Terms,” arXiv:math/9810169: Background on multiplicative convolution, local terms, and the Weil criterion.