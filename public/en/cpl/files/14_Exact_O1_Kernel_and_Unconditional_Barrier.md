# 14 — The Exact $O_1$ Kernel of Claude Proposition 5.6
## Near-Diagonal Wedge, Selberg-Integral Barrier, and Unconditional Results Audit

**Date:** 2026-08-11  
**Status:** exact algebraic regrouping + asymptotic kernel extraction + literature audit  
**Research Discipline:**
- exact symmetrisation is an algebraic rewriting of the formula in Proposition 5.6;
- near-diagonal form is the leading approximation as $h/m\to0$;
- whether existing unconditional results are sufficient must be judged by the statistic they truly control; one cannot simply plug them in just because they are both called "short intervals".

---

# 0. Claude's Original Off-Diagonal

Claude Proposition 5.6 defines:

$$
a_n=\frac{\Lambda(n)}{\sqrt n},
\qquad
y_n=\log n,
$$

and:

$$
\alpha_n^+
=
\int_0^T\Phi(x)^2n^{ix}\,dx,
$$

$$
\alpha_n^-
=
\int_{-T}^0\Phi(x)^2n^{ix}\,dx.
$$

The off-diagonal is:

$$
O_1
=
\frac{1}{2\pi^2}
\Re
\sum_{n\ne m}
\frac{a_na_m}{i(y_n-y_m)}
\left[
\left(\frac nm\right)^{2iT}
(\alpha_m^++\alpha_n^-)
-
\left(\frac nm\right)^{iT}
(\alpha_n^++\alpha_m^-)
\right].
$$

Claude currently only uses the generalized Hilbert inequality to obtain:

$$
|O_1|\ll L^2X.
$$

Compared with the diagonal:

$$
D\asymp TL^3
$$

this is precisely:

$$
X\lesssim T
$$

which is the origin of the support $\sigma\le1$.

---

# 1. Exact Unordered-Pair Symmetrisation

Since $\Phi^2$ is real and even:

$$
\alpha_n^-=\overline{\alpha_n^+}.
$$

Write:

$$
\alpha_n^+
=
G_T(y_n)+iH_T(y_n),
$$

where:

$$
G_T(y)
=
\int_0^T\Phi(x)^2\cos(xy)\,dx,
$$

$$
H_T(y)
=
\int_0^T\Phi(x)^2\sin(xy)\,dx.
$$

For each unordered pair:

$$
m<n,
$$

let:

$$
\vartheta=\log(n/m)>0,
\qquad
u=T\vartheta.
$$

Combining the ordered terms $(n,m)$ and $(m,n)$ yields exactly:

$$
\boxed{
\begin{aligned}
O_1
=
\frac1{\pi^2}
\sum_{m<n}
\frac{a_ma_n}{\vartheta}
\Big[
&
\big(G_T(y_m)+G_T(y_n)\big)
\big(\sin 2u-\sin u\big)
\\
&+
\big(H_T(y_m)-H_T(y_n)\big)
\big(\cos2u+\cos u\big)
\Big].
\end{aligned}
}
$$

This equality does not use the prime-pair conjecture.

The file `o1_symmetrisation_check.json` in this package checks the original ordered formula against this regrouping using $1000$ sets of random complex data; the maximum floating-point discrepancy is at the scale of machine error. That is merely a programmatic check; the exact proof is the conjugate pairing algebra above.

---

# 2. $G_T$ and Taper $g$

Claude has the full Fourier identity:

$$
\int_{\mathbb R}
\Phi(x)^2e^{ixy}\,dx
=
2\pi g(y).
$$

Thus:

$$
G_T(y)
=
\pi g(y)-E_T(y),
$$

where:

$$
E_T(y)
=
\int_T^\infty
\Phi(x)^2\cos(xy)\,dx.
$$

Therefore, the exact $O_1$ can be decomposed into:

$$
O_1
=
O_{1,g}
+
O_{1,\mathrm{tail}}
+
O_{1,H}.
$$

where $O_{1,g}$ is the leading term we wish to connect with the weighted prime pairs; the $E_T$ and $H_T$ parts are remainder obligations that must be proven separately.

One cannot silently drop $H_T$ just because $g$ appears to be the main term.

---

# 3. Rewriting as Additive Shifts

Let:

$$
n=m+h,
\qquad
h\ge1.
$$

The leading $g$-kernel is:

$$
\boxed{
K_g(m,h)
=
\frac{
g(\log m)+g(\log(m+h))
}{
\pi\sqrt{m(m+h)}\log(1+h/m)
}
\left[
\sin\!\left(2T\log(1+h/m)\right)
-
\sin\!\left(T\log(1+h/m)\right)
\right].
}
$$

Thus:

$$
O_{1,g}
=
\sum_{h\ge1}
\sum_{m+h\le X}
\Lambda(m)\Lambda(m+h)K_g(m,h).
$$

This is the weighted prime-pair sum that the WPPH truly needs to control.

---

# 4. Near-Diagonal Universal Kernel

If:

$$
h=o(m),
$$

then:

$$
\log(1+h/m)
=
\frac hm+O(h^2/m^2),
$$

and:

$$
\frac1{
\sqrt{m(m+h)}\log(1+h/m)
}
=
\frac1h
\left(1+O(h/m)\right).
$$

Further ignoring the taper tail and small variations in $g$, we obtain:

$$
K_g(m,h)
\approx
\frac{2g(\log m)}{\pi h}
\left[
\sin\left(\frac{2hT}{m}\right)
-
\sin\left(\frac{hT}{m}\right)
\right].
$$

Let the local shift scale be:

$$
H(m)=\frac mT,
$$

and:

$$
u=\frac h{H(m)}=\frac{hT}{m}.
$$

Then:

$$
\boxed{
K_g(m,h)
\approx
\frac{2Tg(\log m)}{\pi m}
\kappa(u),
}
$$

where:

$$
\boxed{
\kappa(u)
=
\frac{\sin2u-\sin u}{u}
=
\frac{2\sin(u/2)\cos(3u/2)}{u}.
}
$$

and by continuous extension, define:

$$
\kappa(0)=1.
$$

This is a signed oscillatory kernel, not a positive averaging window.

Therefore, using only an absolute-value mean-square bound will typically lose the cancellation that the WPPH truly relies on.

---

# 5. Not a Shift, but a Wedge

Let:

$$
X=T^\sigma,
$$

and stratify by:

$$
m=T^\alpha
$$

The part that truly steps out of the diagonal-only regime is:

$$
1\le\alpha\le\sigma.
$$

The local shift scale is:

$$
H(m)=\frac mT=T^{\alpha-1}.
$$

Thus, the arithmetic input of $P_{70}$ does not merely handle:

$$
h\sim X/T.
$$

but rather handles a wedge:

$$
\boxed{
1
\lesssim h
\lesssim
T^{\sigma-1},
\qquad
m\in[T,T^\sigma].
}
$$

For a flat/Fejér-type taper:

$$
g(\log m)
\approx
(\sigma-\alpha)\log T.
$$

Therefore, although the top of the wedge has the largest shift, the taper weight approaches zero; the true weight distribution is not uniform.

As a simple diagnostic, the proportion of the flat taper diagonal weight falling in $m\ge T$ is:

$$
\boxed{
1-\frac3{\sigma^2}+\frac2{\sigma^3}.
}
$$

For:

$$
\sigma_{70}\approx1.042628,
$$

it is only about:

$$
0.488\%.
$$

This echoes the finding in v10 that the optimizer's Fourier mass truly located at $|\alpha|>1$ is only about $0.114\%$: $P_{70}$ uses only an extremely thin layer of new information, but crossing the boundary itself remains a qualitative change.

---

# 6. Why Do Existing Unconditional Selberg Integrals Not Directly Solve the WPPH?

Zaccagnini's survey defines:

$$
J(x,\theta)
=
\int_x^{2x}
|\psi(t+\theta t)-\psi(t)-\theta t|^2dt.
$$

and notes that:

$$
J(x,\theta)=o(x^3\theta^2)
$$

can be obtained unconditionally for roughly:

$$
\theta\ge x^{-5/6-\varepsilon(x)}.
$$

If:

$$
H=\theta x,
$$

this means:

$$
H\ge X^{1/6-o(1)}.
$$

However, the maximum shift scale of the $P_{70}$ wedge is only:

$$
H_{\max}
=
X^{1-1/\sigma_{70}}
\approx
X^{0.040885}.
$$

So the ranges themselves are already disjoint:

$$
0.040885
<
\frac16.
$$

Furthermore:

$$
J=o(XH^2)
$$

is the scale for "almost all short intervals having the PNT".

What the WPPH requires is a signed weighted second-correlation constant, close to a variance of the conjectural type:

$$
XH\log(X/H)
$$

rather than merely knowing it is smaller than $XH^2$.

Therefore, this unconditional statement itself is neither in the required range, nor does it provide the required precise constant.

---

# 7. Do the 2026 Higher-Uniformity Results Help?

The almost-all-interval result of Matomäki–Radziwiłł–Shao–Tao–Teräväinen for $\Lambda$ can establish higher-order uniformity / nilsequence discorrelation at:

$$
H\ge X^{1/3+\varepsilon}
$$

and deduce a class of Hardy–Littlewood results involving "a short average over one variable".

This is a very strong new development, but there are still two mismatches for our problem:

1. Range:

$$
\frac13
\gg
0.040885;
$$

2. Statistic: It is not the weighted prime-pair second-trace asymptotic required by Claude's $O_1$.

Thus, one cannot simply see "short-averaged Hardy–Littlewood" and declare that the WPPH has been established.

---

# 8. Conclusion of This Round's Unconditional Audit

The results found so far are insufficient to unconditionally prove, via Claude's $O_1$ pipeline:

$$
P_{70}.
$$

Strictly speaking, they also have not yet provided a clear, proven implication:

$$
67.25\%
\longrightarrow
q>67.25\%
$$

along the generalized-support route.

The reason is not a complete lack of short-interval information, but rather that:

$$
\boxed{
\text{range}
+
\text{statistic}
+
\text{constant/sign}
}
$$

all three must match simultaneously.

---

# 9. The Next Reasonable Question

Rather than continuing to force general short-interval theorems onto the WPPH, it is more reasonable to consider:

## Kernel-Matched Selberg Problem (KMSP)

For the exact kernel in this document:

$$
K_g(m,h)
$$

establish a dedicated weighted correlation bound:

$$
\sum_{h,m}
\Big(
\Lambda(m)\Lambda(m+h)-\mathfrak S(h)
\Big)
K_g(m,h).
$$

The goal is not to first prove the full prime-pair conjecture, but rather to utilize:

- the sign oscillation of $\kappa(u)$;
- the taper wedge;
- the structure of the $H_T$ correction;
- the joint smoothness of $m$ and $h$;

to directly obtain:

$$
o(TL^3)
$$

or a one-sided bound sufficient to improve upon $67.25\%$.

This is currently the most precise proof obligation for the direct arithmetic route.