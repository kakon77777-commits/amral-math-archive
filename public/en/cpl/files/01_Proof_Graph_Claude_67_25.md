# 01 — Claude 67.25%: Modular Reconstruction of the Proof Chain

## 1. Target Proposition

The core of the research is:

$$
\liminf_{T\to\infty}
\frac{N_0^s(T,2T)}{N(T,2T)}
\ge0.672500\ldots.
$$

This is not a zero-by-zero verification, but an asymptotic proportion certificate.

---

## 2. Module Z: Zero Side

Restricting the Weil Hermitian form to a finite-dimensional test family $V$ yields the Hermitian compression $\widetilde G$.

By the symmetry of the functional equation:

- A distinct point on the critical line provides a rank-one nonnegative contribution;
- An off-line pair $\{\rho,1-\bar\rho\}$ generates a hyperbolic block in an appropriate basis:

$$
\begin{pmatrix}
0&m\\
m&0
\end{pmatrix},
$$

whose signature is:

$$
(1,1).
$$

Therefore, it can be decomposed as:

$$
\widetilde G=P+Q,
$$

where $P\succeq0$, and the positive index of $Q$ is controlled by the off-line pairs.

---

## 3. Module L: Linear Algebra

Claude Lemma 3.2: If $P,Q$ are Hermitian, and

$$
P\succeq0,\qquad \operatorname{rank}P\le r,\qquad n_+(Q)\le b,
$$

then for $c>0$:

$$
\|P+Q\|_F^2
\ge
c\operatorname{tr}P
-
\frac{c^2}{4}r
+
2c\operatorname{tr}Q
-
c^2b.
$$

Taking $c=2$:

$$
r
\ge
2\operatorname{tr}P
+4\operatorname{tr}Q
-4b
-\|P+Q\|_F^2.
$$

Here, the von Neumann trace inequality is used to control the worst-case coupling of the positive and negative spectral parts.

---

## 4. Module P: Prime Side

Using the explicit formula, the traces of the compression are transformed into prime-power / archimedean integrals.

For $0<\lambda\le1$, the main terms are obtained unconditionally:

$$
\operatorname{tr}\widetilde G\sim N,
$$

$$
\operatorname{tr}\widetilde G^2
\sim
\left(\frac1\lambda+\frac\lambda3\right)N.
$$

The critical structural boundary is:

$$
\lambda\le1.
$$

If it exceeds $1$, the off-diagonal prime sums are no longer automatically suppressed by the diagonal terms, requiring prime-pair / Hardy--Littlewood or equivalent stronger pair-correlation inputs.

---

## 5. Flat window: $2/3$

Combining Z, P, and L yields:

$$
H(\lambda)
=
2-
\frac1\lambda
-
\frac\lambda3.
$$

On the admissible interval $0<\lambda\le1$, the optimal point is:

$$
\lambda=1,
$$

Thus:

$$
H(1)=2-1-\frac13=\frac23.
$$

---

## 6. Window optimisation: $67.25\%$

Section 7.1 optimizes the scale-free functional with respect to the window density $v$:

$$
c_\lambda(v)
=
\frac{
\lambda\left(\int v\right)^2
}{
\int v^2
+
\lambda^2
\iint |s-s'|v(s)v(s')\,ds\,ds'
}.
$$

The Euler / extremal problem gives:

$$
v_\lambda^*(s)=\cos(\sqrt2\lambda s),
$$

and:

$$
c_\lambda^*
=
\frac{\sqrt2\tan\theta}{1+\theta\tan\theta},
\qquad
\theta=\frac\lambda{\sqrt2}.
$$

At $\lambda=1$:

$$
c_1^*=0.753296\ldots,
$$

Thus:

$$
P_{MT}
=
2-
\frac1{c_1^*}
=
0.672500\ldots.
$$

The one-delta extremal result of CCLM17 is used by Claude to explain that: when "only using the values of Montgomery's $F(\alpha)$ on $[-1,1]$" and maintaining the window extremisation of the type in Section 7.1, the Montgomery--Taylor kernel is already extremal; therefore, this sub-framework cannot be improved solely by changing the window.

---

## 7. Higher moments

The existing unconditional main proof only truly uses low-order moments. Claude Section 7.5 connects the sharp positive-eigenvalue lower bound to the one-sided Chebyshev--Markov--Stieltjes / Christoffel function.

If the normalized moments up to order $2m$ are known, the $n_+$ certificate can be improved.

For the conditional $HL^*(4,\lambda)$, as $\lambda\to1$:

$$
m_1=1,\qquad
m_2=\frac43,\qquad
m_3=2,\qquad
m_4=\frac{13}{4}.
$$

The paper obtains:

$$
\Lambda_2(0;1)=\frac5{36},
$$

and:

$$
\frac{N_0^s}{N}
\ge
\frac{13}{18}
\approx72.22\%.
$$

Therefore, a very concrete conditional moment route exists for $P_{70}$.

---

## 8. First Batch of Proof Obligations

### PO-01
Independently prove Lemma 3.2, tracking the equality conditions term by term.

### PO-02
Explicitly derive the $(1,1)$ block from the functional-equation pair, rather than merely accepting the statement.

### PO-03
Redo the normalization to confirm:

$$
\operatorname{tr}\widetilde G\sim N,
\qquad
\operatorname{tr}\widetilde G^2\sim\left(\frac1\lambda+\frac\lambda3\right)N.
$$

### PO-04
Independently solve the $c_\lambda(v)$ extremal problem.

### PO-05
Trace the configuration extremal law for $0.68185$; currently, only the conclusion in Remark 1.1 of the main paper has been confirmed, and the complete derivation has not yet been located in the main text.