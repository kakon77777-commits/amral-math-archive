# 15 — Matrix Majorant–Inertia Problem (MMIP)
## Finding Unconditional Improvements Using CGdL Tail-Sign SDP and Claude Off-Axis Signature

**Date:** 2026-08-11  
**Status:** literature audit + new research programme  
**Not a claim of results:** This document does not prove a new proportion of $\zeta$ zeros; it merely identifies a hybrid route that might bypass the $\alpha>1$ asymptotic.

---

# 0. Why Revisit CGdL?

Under RH, Chirre–Gonçalves–de Laat (CGdL) improved the Montgomery–Taylor multiplicity constant:

$$
1.3275
$$

to:

$$
1.3208.
$$

Consequently, the simple-zero lower proportion increased from:

$$
67.25\%
$$

to:

$$
67.92\%.
$$

They did not obtain a new asymptotic for $F(\alpha)$ in $|\alpha|>1$.

The core technique is relaxing the bandlimited condition, allowing:

$$
\widehat f(\alpha)\le0
\qquad
(|\alpha|\ge1).
$$

Since the pair form factor:

$$
F(\alpha,T)\ge0,
$$

the integral over the unknown band:

$$
\int_{|\alpha|>1}
\widehat f(\alpha)F(\alpha,T)\,d\alpha
$$

is strictly beneficial for the required upper bound, and thus can be discarded.

This is:

$$
\boxed{
\text{using the sign of the unknown region, rather than its value.}
}
$$

---

# 1. Post-2024/2026, the Prime-Side Sign is Already Unconditional

The unconditional Montgomery theorem by Baluyot–Goldston–Suriajaya–Turnage-Butterbaugh defines the form factor without assuming RH, and proves:

$$
\boxed{
F(\alpha)\ \text{real, even, nonnegative}
}
$$

for all real $\alpha$, while simultaneously yielding the Montgomery asymptotic in:

$$
0\le\alpha\le1
$$

Therefore, the two ingredients of the CGdL prime side:

1. known-band asymptotic;
2. outside-band nonnegativity;

now both have unconditional versions.

This leads to an immediate first guess:

> Can we directly make the CGdL $67.92\%$ unconditional?

The current answer is: we cannot deduce this directly.

---

# 2. The Gap is on the Zero Side, Not the Prime Side

The scalar pair sum in CGdL is:

$$
\sum_{\gamma,\gamma'}
g\!\left(
(\gamma-\gamma')
\frac{\log T}{2\pi}
\right)
w(\gamma-\gamma').
$$

Under RH:

- every zero ordinate $\gamma$ is real;
- $g\ge0$;
- $w(\gamma-\gamma')>0$;
- every off-diagonal scalar term is nonnegative.

Thus, they can directly obtain:

$$
\boxed{
\text{pair sum}
\ge
g(0)\sum_\gamma m_\rho
}
$$

which is their equation (10), thereby lower-bounding the multiplicity sum.

However, moving away from RH, the unconditional form factor of BGSTB uses:

$$
x^{\rho-\rho'}w(\rho-\rho')
$$

or an equivalent functional-equation symmetrisation.

The horizontal displacement of the zeros enters complex arguments; the scalar nonnegative-kernel lower bound of CGdL no longer holds automatically.

Therefore:

$$
\boxed{
\text{BGSTB prime-side positivity}
+
\text{CGdL scalar proof}
\not\Rightarrow
\text{unconditional }67.92\%.
}
$$

---

# 3. Claude Supplies Exactly an Alternative Zero-Side Mechanism

Claude does not require the entire pair sum to be positive.

It writes the finite compression as:

$$
\widetilde G=P+Q,
$$

where:

- critical-line zeros contribute:

$$
P\succeq0;
$$

- each off-axis functional-equation pair contributes an indefinite block with signature:

$$
(1,1)
$$

Then, it controls the positive index and rank using inertia + rank–trace inequality.

Thus, Claude's way of resolving the zero side is via:

$$
\boxed{
\text{block signature}
}
$$

rather than:

$$
\boxed{
\text{scalar termwise positivity}.
}
$$

---

# 4. A New Problem: MMIP

We define:

## Matrix Majorant–Inertia Problem (MMIP)

Find a test / finite compression such that the following three things hold simultaneously.

### M1 — Tail-sign prime control

The Fourier side allows:

$$
\widehat f(\alpha)\le0
\qquad
(|\alpha|\ge1),
$$

and utilizes the unconditional:

$$
F(\alpha)\ge0
$$

to discard the unknown tail, obtaining a better prime-side upper bound just like CGdL.

### M2 — Off-axis block control

The zero side cannot rely on the scalar nonnegative kernel under RH, but must preserve Claude's:

$$
(1,1)
$$

off-axis block signature.

### M3 — Matrix certificate

Establish a new matrix inequality that converts:

- the prime-side tail-sign upper bound;
- the critical-line PSD rank;
- the off-axis positive-index budget;

into a lower bound for:

$$
N_0^s/N
$$

---

# 5. Why Might This Route Bypass the $P_{70}$ Prime-Pair Wall?

The generalized-support route requires genuinely knowing the weighted value of:

$$
F(\alpha)
$$

in:

$$
1<|\alpha|\le1.043
$$

MMIP only wants to use:

$$
F(\alpha)\ge0
$$

and:

$$
\widehat f(\alpha)\le0.
$$

So it might improve the test-function constant without calculating $O_1$ beyond $\sigma=1$ at all.

This is consistent with the language of the previous toy Boundary-Spike study:

> It is not necessary to fully observe the boundary; one can also add a dual price that only restricts its sign/direction.

---

# 6. Constant Targets

Comparison:

| Certificate | Effective $C$ | $2-C$ |
|---|---:|---:|
| Montgomery–Taylor / Claude D | $1.3274993$ | $67.2501\%$ |
| CGdL scalar SDP (RH) | $1.3208$ | $67.92\%$ |
| Bandwidth-one configuration-wise ceiling | $1.31815$ | $68.185\%$ |
| CGdL GRH comparison | $1.3155$ | $68.45\%$ |
| $P_{70}$ | $1.30$ | $70\%$ |

Therefore:

### Phase 1

As long as the matrix-tail certificate achieves:

$$
C<1.3274993,
$$

it is a candidate for an unconditional improvement over Claude's $67.25\%$.

### Phase 2

To break through:

$$
68.185\%
$$

requires:

$$
C<1.31815.
$$

The published CGdL RH constant:

$$
1.3208
$$

itself is not enough to cross this ceiling.

### Phase 3

To reach:

$$
70\%
$$

requires:

$$
C\le1.30.
$$

Whether this is possible relying solely on the current CGdL-type tail sign is completely unknown.

---

# 7. A Possible SDP Formulation

Currently, only a research skeleton is provided.

Choose a family of basis functions:

$$
\{f_1,\ldots,f_d\}.
$$

Establish the Hermitian compression:

$$
G_{ij}=W(f_i,f_j).
$$

Then introduce a Fourier-side majorant matrix kernel:

$$
\widehat{\mathcal K}(\alpha).
$$

Require:

### Known band

For:

$$
|\alpha|\le1
$$

the prime-side trace / Frobenius quantities can be computed via the unconditional Montgomery theorem.

### Unknown band

For:

$$
|\alpha|>1
$$

require an appropriate matrix ordering:

$$
\widehat{\mathcal K}(\alpha)\preceq0,
$$

so that:

$$
F(\alpha)\ge0
$$

can provide a one-sided prime bound.

### Zero side

For a critical zero:

$$
B_{\rm crit}\succeq0.
$$

For an off-axis pair:

$$
B_{\rm off}
$$

maintains an auditable inertia budget, rather than being destroyed by scalar majorisation.

---

# 8. The First Technical Obstruction

The scalar condition:

$$
\widehat f\le0
$$

does not automatically equate to:

$$
\widehat{\mathcal K}\preceq0.
$$

Moreover, a matrix majorant that is beneficial for the prime-side tail might simultaneously destroy the zero-side:

- rank-one critical contribution;
- off-axis hyperbolic block;
- Poisson–Gabor locality;
- decomposition required by Claude Lemma 3.2.

Therefore, the core of MMIP is not "stuffing the CGdL function into Claude".

Instead, it is:

$$
\boxed{
\text{a matrix cone simultaneously compatible with the Fourier tail order and the zero-side inertia.}
}
$$

---

# 9. The First Executable MVP

Do not directly attempt the full zeta theorem.

First, build a finite configuration toy:

1. Take the previous $N=4$ marked configurations;
2. Outside the open-band row constraints, add an abstract observable that is "tail nonnegative, dual coefficient nonpositive";
3. Allow matrix blocks instead of scalar certificates;
4. Use SDP to find the minimum simple fraction;
5. See if it exceeds the scalar bandwidth-one floor;
6. Then convert the feasible matrix inequality into an exact rational / Bernstein or SOS certificate.

This can first answer:

> Do tail-sign + inertia genuinely have synergistic gains in a finite toy world?

If there are no gains even in the toy model, it is not worth directly attacking the full zeta.

---

# 10. Conclusion of This Round

The direct arithmetic route currently encounters short-interval range and precision obstacles.

However, the unconditional $F\ge0$ provides a different piece of information:

$$
\boxed{
\text{We do not know the value of the unknown band,
but we know its direction.}
}
$$

CGdL has already proven in the RH scalar setting that this directional information can improve the constant.

Claude, on the other hand, provides off-axis inertia bookkeeping that does not rely on RH.

Therefore, MMIP is currently the most concrete hybrid research problem:

$$
\boxed{
\text{Tail sign}
+
\text{Matrix inertia}
\stackrel{?}{\Longrightarrow}
\text{unconditional improvement beyond }67.25\%.
}
$$