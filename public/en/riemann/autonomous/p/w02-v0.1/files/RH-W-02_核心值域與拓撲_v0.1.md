# RH-W-02: Weil Test Function Core, Range, and Topology
## Riemann Hypothesis GAP Engineering Note v0.1

**研究計畫：** RH GAP Atlas / AI Mathematical Engineering Relay  
**父節點：** `RH-W-02`  
**前置節點：** `RH-W-01`  
**狀態：** `CORE_CLOSED / GLOBAL_BRIDGE_OPEN`  
**日期：** 2026-07-23  
**性質：** Function space and closure engineering; not a proof of RH, establishes no new Weil positivity results

---

# 0. Conclusions of the Current Iteration

Let

$$
D=x\frac{d}{dx},
\qquad
\mathcal A=D(D+1),
$$

and define the compactly supported smooth core with double vanishing moments:

$$
\mathcal C_{00}
:=
\left\{
 g\in C_c^\infty(0,\infty):
 \widetilde g(0)=\widetilde g(1)=0
\right\}.
$$

This iteration proves:

$$
\boxed{
\mathcal A C_c^\infty(0,\infty)=\mathcal C_{00}
}.
$$

Therefore, the analytically generated core established in `RH-W-01`

$$
\mathcal G_{\mathrm{bump}}
:=D(D+1)C_c^\infty(0,\infty)
$$

does not merely cover a portion of the valid functions, but **precisely covers all compactly supported, smooth test functions with double vanishing moments**.

At the same time, under the LF topology of $C_c^\infty$, this iteration establishes:

$$
\text{Atomic dictionary is dense}
\quad+
\quad Q_{B0}\text{ is continuous}
\quad\Longrightarrow\quad
\text{Positivity on the dictionary transfers to }\mathcal C_{00}.
$$

However, this still does not equate to RH. The truly incomplete bridge is:

$$
\mathcal C_{00}
\longrightarrow
\text{A complete Weil test space known to be equivalent to RH}.
$$

---

# 1. Three Layers of Spaces, Not to Be Conflated

## 1.1 The Core Layer

$$
\mathcal C_{00}
\subset C_c^\infty(0,\infty).
$$

Advantages of this layer:

- Arithmetic sums are finite;
- Mellin transforms are entire functions with rapid vertical decay;
- Sums over zeros converge absolutely;
- All related functions and differential operations can be handled at the classical function level;
- Suitable for programming, CAS, and formalization.

## 1.2 The B0 Generalized Layer

The reference class of Bombieri/Clay is the space of decaying functions $\mathcal W$. The Weil criterion is formulated for $g\in\mathcal W$ satisfying two vanishing moments. This layer contains functions that are not compactly supported, so arithmetic sums, sums over zeros, and tail controls are no longer automatically finite.

## 1.3 The Strip Analytic Completion Layer

Lagarias uses the strip analytic test function space $\mathcal A_\delta$ on the Mellin side, with the uniform norm on the closed strip as the topology; in the unconditional case, for $\delta>\tfrac12$, the Weil distribution acts as a continuous linear functional, and the Weil criterion can be formulated on an appropriate $\mathcal A_\delta$.

This engineering project temporarily considers it as the candidate global target:

$$
\widehat{\mathcal A}_{\delta,00}
:=
\left\{
F\in\widehat{\mathcal A}_\delta:
F(0)=F(1)=0
\right\},
\qquad \delta>\frac12.
$$

However, the density and normalization consistency from $\mathcal C_{00}$ to this space have not yet been proven within this project.

---

# 2. Logarithmic Coordinates

Let

$$
x=e^u,
\qquad
G(u):=g(e^u),
\qquad
H(u):=h(e^u).
$$

Then:

$$
D\longleftrightarrow\partial_u,
$$

and

$$
D(D+1)h
\longleftrightarrow
P H:=\partial_u(\partial_u+1)H
=H''+H'.
$$

The two Mellin vanishing moments become:

$$
\widetilde g(0)=0
\Longleftrightarrow
\int_{\mathbb R}G(u)\,du=0,
$$

$$
\widetilde g(1)=0
\Longleftrightarrow
\int_{\mathbb R}e^uG(u)\,du=0.
$$

Define:

$$
\mathscr D_{00}
:=
\left\{
G\in C_c^\infty(\mathbb R):
\int G(u)\,du=0,
\ \int e^uG(u)\,du=0
\right\}.
$$

The problem thus reduces to:

$$
P C_c^\infty(\mathbb R)
\stackrel{?}{=}
\mathscr D_{00}.
$$

---

# 3. Exact Range Theorem

## Theorem 3.1

$$
\boxed{
P C_c^\infty(\mathbb R)=\mathscr D_{00}
}.
$$

Moreover, $P$ is injective on $C_c^\infty(\mathbb R)$, thus:

$$
P:C_c^\infty(\mathbb R)
\longrightarrow
\mathscr D_{00}
$$

is a linear bijection.

## 3.1 Necessity

If

$$
G=H''+H',
\qquad H\in C_c^\infty(\mathbb R),
$$

then:

$$
\int_{\mathbb R}G(u)\,du
=
\int H''(u)\,du+
\int H'(u)\,du
=0.
$$

On the other hand:

$$
\int_{\mathbb R}e^uG(u)\,du
=
\int e^u(H''+H')\,du.
$$

Note that:

$$
\frac{d}{du}\bigl(e^uH'(u)\bigr)
=e^u(H''+H'),
$$

so:

$$
\int e^uG(u)\,du=0.
$$

Hence:

$$
P C_c^\infty(\mathbb R)
\subseteq\mathscr D_{00}.
$$

## 3.2 Sufficiency and Explicit Inversion

Now take any:

$$
G\in\mathscr D_{00}.
$$

First define:

$$
Y(u)
:=
e^{-u}
\int_{-\infty}^{u}e^vG(v)\,dv.
$$

Direct differentiation yields:

$$
Y'(u)+Y(u)=G(u).
$$

Since:

$$
\int_{\mathbb R}e^vG(v)\,dv=0,
$$

when $u$ exceeds the right endpoint of the support of $G$, the integral is zero; when $u$ is to the left of the support, the integral is also zero. Therefore:

$$
Y\in C_c^\infty(\mathbb R).
$$

Integrating $Y'+Y=G$ again:

$$
\int_{\mathbb R}Y(u)\,du
=
\int_{\mathbb R}G(u)\,du
=0.
$$

Define:

$$
H(u):=
\int_{-\infty}^{u}Y(v)\,dv.
$$

Since $Y$ is compactly supported and its total integral is zero, we have:

$$
H\in C_c^\infty(\mathbb R),
\qquad H'=Y.
$$

Finally:

$$
P H
=H''+H'
=Y'+Y
=G.
$$

Therefore:

$$
\mathscr D_{00}
\subseteq
P C_c^\infty(\mathbb R).
$$

## 3.3 Uniqueness

If:

$$
P H=0,
$$

then:

$$
H''+H'=0,
$$

so:

$$
H(u)=c_0+c_1e^{-u}.
$$

The only possible compactly supported solution is:

$$
H=0.
$$

Hence $P$ is injective.

---

# 4. Inversion Formula in Multiplicative Coordinates

For:

$$
g\in\mathcal C_{00},
$$

first define:

$$
y(x)
:=
\frac1x\int_0^x g(t)\,dt.
$$

Then:

$$
(D+1)y=g.
$$

Next define:

$$
h(x)
:=
\int_0^x y(t)\frac{dt}{t}.
$$

Then:

$$
Dh=y,
$$

Thus:

$$
D(D+1)h
=(D+1)Dh
=(D+1)y
=g.
$$

The two vanishing moments precisely guarantee that $y$ and $h$ return to zero on the right side of the support, so $h$ remains a compactly supported smooth function.

**Engineering Significance:** Every valid core input $g$ has a unique seed $h$, rather than only a portion of $g$ being generable by the operator.

---

# 5. Support Preservation and Topological Isomorphism

If:

$$
\operatorname{supp}(G)\subseteq[a,b],
$$

then the above inversion gives:

$$
\operatorname{supp}(Y)
\subseteq[a,b],
\qquad
\operatorname{supp}(H)
\subseteq[a,b].
$$

So $P$ not only preserves compact support, but its inverse operator also does not require expanding the support.

For a fixed compact interval $K$, let:

$$
\mathscr D_K=C_K^\infty(\mathbb R),
$$

equipped with the standard Fréchet seminorms:

$$
p_m(F)=\max_{0\leq j\leq m}
\sup_{u\in K}|F^{(j)}(u)|.
$$

By the integral inversion formula, for each $m$ there exists a constant $C_{K,m}$ depending on $K,m$, such that:

$$
p_m(H)
\leq
C_{K,m}
\,p_{m-1}(G)
$$

or written after unifying the indices:

$$
p_m(H)
\leq
C'_{K,m}p_m(G).
$$

And $P$ is obviously a continuous differential operator. Therefore:

$$
P:\mathscr D_K
\longrightarrow
\mathscr D_{00,K}
$$

is a topological isomorphism between Fréchet spaces.

Taking the strict inductive limit over all compact sets, we obtain:

$$
P:C_c^\infty(\mathbb R)
\longrightarrow
\mathscr D_{00}
$$

is a topological isomorphism at the level of LF spaces.

---

# 6. Density of the Fixed Bump Atomic Dictionary

The previous iteration's program used translations, dilations, modulations, and finite linear combinations of a fixed smooth bump. We now distinguish:

## 6.1 Analytically Complete Family

$$
\mathcal G_{\mathrm{core}}
:=P C_c^\infty(\mathbb R)
=\mathscr D_{00}.
$$

This family is already precisely equal to the complete core, requiring no density argument.

## 6.2 Computable Atomic Dictionary

Let $\eta\in C_c^\infty(\mathbb R)$ be a fixed non-zero bump, and consider the seed atoms:

$$
\eta_{\mu,\sigma}(u)
:=
\eta\!\left(\frac{u-\mu}{\sigma}\right),
\qquad \sigma>0.
$$

Let:

$$
\mathscr A_\eta
:=
\operatorname{span}_{\mathrm{fin}}
\left\{
\eta_{\mu,\sigma}:
\mu\in\mathbb R,
\sigma>0
\right\}.
$$

Standard mollifier approximation gives:

$$
\overline{\mathscr A_\eta}^{\,C_c^\infty}
=C_c^\infty(\mathbb R).
$$

The reason is: for any $H\in C_c^\infty$, the convolution $H*\eta_\varepsilon$ converges uniformly to $H$ in all derivatives; and each convolution integral can be approximated by finite Riemann sums in any finite-order $C^m$ seminorm. Using a diagonal sequence to handle all $m$ simultaneously yields LF convergence.

Since $P$ is continuous and surjective onto $\mathscr D_{00}$:

$$
\boxed{
\overline{P\mathscr A_\eta}^{\,\mathscr D_{00}}
=
\mathscr D_{00}
}.
$$

The modulation parameter $e^{i\tau u}$ is not a necessary condition for density, but it can increase the frequency localization capability of the search dictionary.

---

# 7. Continuity of the B0 Arithmetic Functional on the Core

Define:

$$
f_g(x)
=
\int_0^\infty
 g(xy)\overline{g(y)}\,dy,
$$

and:

$$
Q_{B0}(g)
:=-E_{\mathrm{arith}}(f_g).
$$

## 7.1 Continuity of the Correlation Mapping

On a fixed support layer:

$$
g\mapsto f_g
$$

is a continuous quadratic mapping. If $g$ is supported in $[a,b]$, then $f_g$ is supported in $[a/b,b/a]$, and for each $m$ we have:

$$
p_m(f_g)
\leq
C_{a,b,m}\,p_m(g)^2.
$$

The more general bilinear polarization:

$$
f_{g,h}(x)
:=
\int_0^\infty g(xy)\overline{h(y)}\,dy
$$

satisfies:

$$
p_m(f_{g,h})
\leq
C_{a,b,m}p_m(g)p_m(h).
$$

## 7.2 The Arithmetic Side of the Explicit Formula is a Continuous Distribution

For a fixed compact support $L\subset(0,\infty)$:

- The von Mangoldt sum has only finitely many terms;
- The point evaluations $f(n)$, $f(1/n)$, and $f(1)$ are continuous linear functionals;
- The apparent singularity of the Archimedean integral at $x=1$ is canceled at the first order, so it can be controlled by the $C^1$ seminorm;
- There are no tail terms outside the support.

Therefore, there exists a constant $C_L$ such that:

$$
|E_{\mathrm{arith}}(f)|
\leq
C_L\bigl(p_0(f)+p_1(f)\bigr).
$$

So:

$$
E_{\mathrm{arith}}:
C_c^\infty(0,\infty)
\longrightarrow\mathbb C
$$

is an LF-continuous linear functional.

After composition:

$$
Q_{B0}:\mathcal C_{00}\longrightarrow\mathbb R
$$

is a continuous quadratic form.

---

# 8. Valid Closure Transfer

Let:

$$
\mathcal D_\eta:=P\mathscr A_\eta.
$$

It is known that:

$$
\overline{\mathcal D_\eta}^{\,\mathcal C_{00}}
=
\mathcal C_{00},
$$

and $Q_{B0}$ is continuous. Therefore, if it can be proven in the future that:

$$
\forall g\in\mathcal D_\eta,
\qquad Q_{B0}(g)\geq0,
$$

then for any $g\in\mathcal C_{00}$, taking $g_n\in\mathcal D_\eta$ with $g_n\to g$:

$$
Q_{B0}(g)
=
\lim_{n\to\infty}Q_{B0}(g_n)
\geq0.
$$

Therefore:

$$
\boxed{
Q_{B0}\geq0\text{ on }\mathcal D_\eta
\Longrightarrow
Q_{B0}\geq0\text{ on }\mathcal C_{00}
}.
$$

This corrects the vague issue of "transferring positivity using lower semi-continuity" from older drafts; this layer uses explicit quadratic form continuity.

---

# 9. Why Bare $L^2$ is Not a Valid Unconditional Completion

Mellin–Plancherel gives:

$$
L^2\!\left((0,\infty),\frac{dx}{x}\right)
\cong
L^2\!\left(\frac12+i\mathbb R,\frac{dt}{2\pi}\right).
$$

But one cannot thereby directly extend the Weil quadratic form to bare $L^2$.

Reason 1: $L^2$ elements are merely almost-everywhere equivalence classes; point evaluations are undefined.

Reason 2: Point evaluation is not continuous on $L^2(\mathbb R)$. Take a fixed smooth $\psi$ with $\psi(0)=1$, and let:

$$
\psi_n(t):=\psi(n(t-t_0)).
$$

Then:

$$
\psi_n(t_0)=1,
$$

but:

$$
\|\psi_n\|_{L^2}
=n^{-1/2}\|\psi\|_{L^2}
\longrightarrow0.
$$

The Weil functional involves values of analytic functions at the locations of the zeros; without a Hardy, Sobolev, or strip holomorphic structure, these values cannot be controlled by the bare $L^2$ norm.

So:

$$
\boxed{
\text{Bare }L^2\text{ completion is rejected as an unconditional Weil completion space}
}.
$$

Lagarias uses strip holomorphic functions and the uniform norm on the closed strip precisely to preserve analytic continuation and point evaluation control, rather than merely preserving the $L^2$ class on the critical line.

---

# 10. The Global Bridge Yet to Be Crossed

This iteration only proves the closure transfer of:

$$
\text{Atomic dictionary}
\longrightarrow
\mathcal C_{00}
$$

It has not yet proven:

$$
\overline{\widehat{\mathcal C}_{00}}^{\,\|\cdot\|_{\infty,S_\delta}}
=
\widehat{\mathcal A}_{\delta,00},
\qquad \delta>\frac12.
$$

This proposition is not a formal "smooth functions are usually dense"; the uniform norm acts on an unbounded closed strip, and it requires holomorphy, vertical decay, vanishing at $s=0,1$, and unconditional zero evaluation to be simultaneously compatible.

Therefore, the next true GAP is:

$$
\boxed{
\texttt{RH-W-02-GLOBAL-DENSITY}
}
$$

Its proof obligations are:

1. Precisely fix the complete definition and growth conditions of $\mathcal A_\delta$;
2. Fix the conversion between B0 and Lagarias covariance normalization;
3. Prove the density of the compactly supported Mellin image in the double-vanishing subspace, or find a smaller complete core that is still equivalent to RH;
4. Prove that the Weil functional and quadratic form are continuous under this approximation;
5. If density fails, produce an inapproximable failure witness.

---

# 11. GAP Status

| ID | Status | Current Iteration Verdict |
|---|---|---|
| `RH-W-02-RANGE` | `CLOSED` | $D(D+1)C_c^\infty=\mathcal C_{00}$ |
| `RH-W-02-INVERSE` | `CLOSED` | Explicit unique inverse operator has been given |
| `RH-W-02-SUPPORT` | `CLOSED` | Inversion preserves the same compact support interval |
| `RH-W-02-ATOM-DENSE` | `CLOSED` | Bump atoms are dense in the core after $D(D+1)$ |
| `RH-W-02-Q-LF` | `CLOSED` | $Q_{B0}$ is continuous in the core LF topology |
| `RH-W-02-TRANSFER-CORE` | `CLOSED_CONDITIONAL` | If dictionary positivity holds, it transfers to the complete core |
| `RH-W-02-L2` | `REJECTED` | Bare $L^2$ lacks point evaluation control, cannot serve as unconditional completion |
| `RH-W-02-ADELTA-NORM` | `REFERENCE_AVAILABLE` | Lagarias provides a strip uniform norm candidate |
| `RH-W-02-GLOBAL-DENSITY` | `OPEN` | Density bridge from the core to the RH-equivalent complete space is unproven |
| `RH-W-02-NORMALIZATION` | `OPEN_AUDIT` | B0 negativity and covariance positivity require term-by-term mapping |
| `RH-W-02-RH-SUFFICIENCY` | `BLOCKED_BY_GLOBAL_DENSITY` | Whether core positivity is sufficient to imply RH is not yet closed in this project |

---

# 12. What Was Not Proven in This Iteration

This iteration did not prove that:

$$
Q_{B0}(g)\geq0
$$

holds for any non-trivial infinite family.

Nor did it prove:

$$
Q_{B0}\geq0\text{ on }\mathcal C_{00}
\Longrightarrow RH.
$$

What this iteration accomplished is:

- The core generating family is no longer just a candidate, but is precisely complete;
- Closure transfer within the core has been validated;
- The erroneous completion method of bare $L^2$ has been ruled out;
- The truly remaining global density bridge has been independently registered.

---

# 13. Next Relay Node

It is recommended that the next iteration prioritize:

$$
\boxed{
\texttt{RH-W-02-NORMALIZATION}
}
$$

First, establish a term-by-term invertible conversion between the trace-negativity version of Bombieri/Clay and the covariance-positivity version of Lagarias. Once completed, then process:

$$
\boxed{
\texttt{RH-W-02-GLOBAL-DENSITY}
}
$$

Otherwise, "in which completion space the core is dense" will still be distorted due to incomplete alignment of objects and notations.

---

# Reference Benchmarks

1. Enrico Bombieri, “The Riemann Hypothesis,” in *The Millennium Prize Problems*, explicit formula and Weil negativity criterion.
2. Jeffrey C. Lagarias, “Li Coefficients for Automorphic L-Functions,” Appendix 9: strip test spaces, Weil distribution continuity and covariance formulation.
3. Jean-François Burnol, “The Explicit Formula in Simple Terms,” multiplicative convolution and distributional formulation background.