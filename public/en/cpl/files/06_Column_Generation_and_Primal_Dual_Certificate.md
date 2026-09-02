# 06 — Column Generation, Continuous Pricing, and the Primal/Dual Duality of PairCeiling
## Formally Connecting the Toy LP Back to Anthropic's Certificate Language

**Date:** 2026-08-11  
**Status:** Structural derivation established; numerical floors are exploratory candidates, not yet certified global optima.

---

# 0. The Most Important Result of This Round

In the previous round, we only knew that the small-$N$ toy LP "looked very much like" Anthropic's bandwidth-one adversarial law.

In this round, we can connect the two precisely.

Toy primal:

$$
\min_{w_c}
\sum_c w_c p_c
$$

subject to:

$$
\sum_cw_c=1,
$$

and the open-band row constraints:

$$
\sum_cw_cS_c(j)=\frac{j}{N},
\qquad
j=1,\ldots,N-1.
$$

Its LP dual is:

$$
\max_{y_0,y_1,\ldots,y_{N-1}}
\left[
y_0+\sum_{j=1}^{N-1}\frac{j}{N}y_j
\right]
$$

subject to, for each configuration $\mathcal C_c$:

$$
y_0+\sum_{j=1}^{N-1}y_jS_c(j)
\le p_c.
$$

Now define:

$$
c_0:=y_0,
$$

and the discrete certificate samples:

$$
\boxed{
r_N(j/N):=Ny_j.
}
$$

Since Anthropic's grid masses are:

$$
s_j=\frac{S(j)}{N},
$$

the dual constraint becomes:

$$
\boxed{
c_0+\sum_{j=1}^{N-1}s_jr_N(j/N)\le p_c.
}
$$

This is exactly the discrete form of the configuration-wise certificate inequality used by `PairCeiling`.

And the dual objective:

$$
y_0+\sum_{j=1}^{N-1}\frac{j}{N}y_j
$$

can be rewritten as:

$$
c_0+\sum_{j=1}^{N-1}
\frac{j}{N^2}r_N(j/N).
$$

As $N\to\infty$, if $r_N\to r$ is sufficiently regular, the Riemann sum form becomes:

$$
\boxed{
c_0+\int_0^1 r(x)x\,dx.
}
$$

This, again, is exactly the continuum certificate value of Anthropic's `PairCeiling`.

Therefore:

$$
\boxed{
\text{our primal/dual toy LP}
\longrightarrow
\text{Anthropic PairCeiling certificate}
}
$$

This is not a metaphor, but a discretization of the exact same convex-duality structure.

---

# 1. The Significance of Column Generation Thus Becomes Very Clear

The master LP only includes a small subset of configurations.

Solving the master yields the dual:

$$
(c_0,y_1,\ldots,y_{N-1}).
$$

For any new configuration $\mathcal C$, the reduced cost is:

$$
RC(\mathcal C)
=
p(\mathcal C)
-
\left[
c_0+\sum_{j=1}^{N-1}y_jS_{\mathcal C}(j)
\right].
$$

Using certificate notation:

$$
RC(\mathcal C)
=
p(\mathcal C)
-
\left[
c_0+\sum_{j=1}^{N-1}
\frac{S_{\mathcal C}(j)}{N}
r_N(j/N)
\right].
$$

Therefore:

### If

$$
RC(\mathcal C)<0,
$$

it indicates that the current dual certificate is **not configuration-wise valid**.

We have found a counterexample configuration.

### If

$$
RC(\mathcal C)\ge0
$$

holds for all configurations,

then the dual is a valid certificate over the entire configuration class.

So the pricing problem itself is:

$$
\boxed{
\text{automatically searching for counterexample configurations to the certificate.}
}
$$

This actually has a very direct engineering correspondence with the "candidate theorem → adversarial referee / counterexample search" workflow in the Claude research process.

---

# 2. Continuous-Position Pricing

In the previous round, positions were restricted to $M$ grid sites.

In this round, we no longer enumerate all continuous configurations.

For each multiplicity pattern, for example:

$$
(2,1,1,\ldots,1),
$$

we fix the translation symmetry:

$$
x_1=0,
$$

and for the rest:

$$
x_i\in[0,1)
$$

we directly solve numerically:

$$
\min_{\mathbf x}
RC(\mathbf x).
$$

which is a nonlinear configuration-pricing problem.

After finding a column with a negative reduced cost:

```text
solve master LP
→ read dual prices
→ continuous pricing
→ add most violating configuration
→ solve master again
→ repeat
```

This is standard column generation.

---

# 3. Numerical Candidate Floors

After performing continuous pricing using multiple numerical global-search seeds, we currently obtain:

| $N$ | candidate floor |
|---:|---:|
| $4$ | $69.82311\%$ |
| $5$ | $69.22046\%$ |
| $6$ | $68.89346\%$ |
| $7$ | $68.71442\%$ |

The official $N=256$ exact-rational law:

$$
68.1828687\ldots\%.
$$

Relative gap:

| $N$ | Gap to official $N=256$ law |
|---:|---:|
| 4 | $1.6402$ percentage points |
| 5 | $1.0376$ |
| 6 | $0.7106$ |
| 7 | $0.5316$ |

This is a very strong numerical signal:

$$
\boxed{
\text{After relaxing to continuous positions, the floor of the toy primal indeed rapidly approaches the official law.}
}
$$

However, we cannot claim:

$$
p_N\to0.681828687\ldots
$$

Because:

1. We only have $N=4,\dots,7$;
2. Continuous pricing uses a numerical global optimizer;
3. There is no interval / exact-rational global optimality certificate;
4. The configuration class has not yet been proven to be exactly identical to the official generator.

---

# 4. A New Structural Phenomenon: The One-Double Defect

In the later stages of pricing, the pattern that most frequently and consistently yields a negative reduced cost is:

$$
\boxed{
(2,1,1,\ldots,1).
}
$$

For example:

- $N=4$: $(2,1,1)$;
- $N=5$: $(2,1,1,1)$;
- $N=6$: $(2,1,1,1,1)$;
- $N=7$: A large portion of late-stage pricing is still dominated by the one-double pattern, although $(2,2,\ldots)$ columns were also found in the middle stages.

The simple fraction of the one-double configuration is:

$$
p_{\mathrm{1dbl}}
=
\frac{N-2}{N}.
$$

The primal law does not exclusively use low-simple configurations; it mixes:

$$
\text{fully simple configurations}
$$

with:

$$
\text{collision-defect configurations}
$$

, utilizing positional degrees of freedom to adjust the Fourier rows so that the average pair data returns to CUE.

For now, this can be understood as:

> **Trading sparse multiplicity defects for substantial pair-spectrum tunability.**

This is likely the finite-$N$ shadow of the official marked-configuration extremal law.

---

# 5. Dual Certificate Samples

Numerical master duals:

## $N=4$

$$
(y_0,y_1,y_2,y_3)
\approx
(1,
-0.427637,
-0.251199,
-0.092347).
$$

## $N=5$

$$
(1,
-0.365810,
-0.257489,
-0.146837,
-0.054420).
$$

## $N=6$

$$
(1,
-0.316559,
-0.245610,
-0.167512,
-0.094591,
-0.035543).
$$

## $N=7$

$$
(0.998343,
-0.277556,
-0.227637,
-0.171470,
-0.114935,
-0.064905,
-0.024481).
$$

After rescaling:

$$
r_N(j/N)=Ny_j
$$

, the samples for different $N$ have begun to fall onto a similar smooth negative profile, approaching:

$$
r(1)=0
$$

.

This phenomenon is extremely important because it directly shows:

$$
\boxed{
\text{finite LP dual}
\rightarrow
\text{continuum certificate function }r(x).
}
$$

See figure:

```text
figures/dual_certificate_rescaled_samples.png
```

At present, we should not guess an exact closed-form function; larger $N$ and certified pricing are required.

---

# 6. Why Does This Help Investigate $70\%$?

The official bandwidth-one law has already told us:

$$
p_{\min}\approx0.68183.
$$

To achieve:

$$
P_{70},
$$

is equivalent to requiring the admissible primal laws to satisfy:

$$
p_{\min}\ge0.70.
$$

So now we can directly add any additional mathematical information $\mathcal I$ as new primal constraints:

$$
\mathcal F_1
\rightarrow
\mathcal F_1\cap\mathcal I.
$$

And then re-evaluate:

$$
p_{\min}(\mathcal I).
$$

If:

$$
p_{\min}(\mathcal I)\ge0.70,
$$

we will know that this information is sufficient at the abstract certificate level to break through the bandwidth-one ceiling.

This turns the question of "what new information is needed" into an experimentally testable optimization problem.

---

# 7. Minimal Escape Constraint Search

The next formal problem:

$$
\boxed{
I_{70}^*
=
\arg\min_{\mathcal I}
Cost(\mathcal I)
\quad
\text{s.t.}
\quad
p_{\min}(\mathcal I)\ge0.70.
}
$$

Candidate $\mathcal I$:

### A. Support

Adding information about:

$$
S(\alpha)
$$

in the region:

$$
1<\alpha\le1+\delta
$$

.

### B. Boundary Control

For example:

$$
S(1)\le B.
$$

### C. Higher Moments

Adding to the pair matrix / spectral law:

$$
m_3,m_4,\ldots
$$

### D. Multi-Point Statistics

Introducing three-point or higher correlations.

### E. Zeta Realizability

Adding arithmetic / analytic conditions that true zeta zeros must satisfy, but which abstract marked configurations do not necessarily need to satisfy.

The last one is the most likely to bypass the information barrier of pure pair-correlation.

---

# 8. Integration with the Boundary-Spike Obstruction

The previous round already observed:

$$
S(256)\approx211.432
$$

while all:

$$
j<256
$$

rows are almost entirely CUE-like.

Now, the primal/dual duality explains the reason, which can be stated more precisely:

> The dual certificate has no price in the open band to penalize unobserved boundary spikes.

That is:

$$
y_N
$$

simply does not exist in the bandwidth-one master.

Therefore, the primal can utilize:

$$
S(N)
$$

as a "free direction."

Once a boundary / beyond-band observable is added, it is equivalent to assigning a new dual price to this direction:

$$
y_N.
$$

This is the convex-optimization explanation of the BSO.

---

# 9. Next Round: From Heuristic Pricing to Certificate Pricing

The biggest mathematical gap right now is not the master LP.

The master LP is linear and can be solved exactly.

The real gap is pricing:

$$
\min_{\mathcal C}RC(\mathcal C)
$$

whether it can be globally solved with certification over the continuous marked-configuration space.

The next steps can be divided into three levels:

### Level 1 — Multi-start Numerical

Currently done.

### Level 2 — Interval Branch-and-Bound

For the positions box:

$$
[0,1]^{k-1}
$$

establish interval lower bounds for the Fourier polynomial to prove:

$$
RC\ge-\epsilon.
$$

### Level 3 — Exact Algebraic / SDP Relaxation

Rewrite the trigonometric pricing into:

- unit-circle polynomials;
- moment/SOS relaxations;
- semidefinite bounds;
- rational certificates.

If Level 2/3 is achieved, we will begin to have our own:

$$
\boxed{
\text{small-N certified PairCeiling results}.
}
$$

---

# 10. Conclusion of This Round

The most important thing right now is not the candidate floor itself.

Rather, it is that we have established:

$$
\boxed{
\text{Primal adversarial law}
\;\Longleftrightarrow\;
\text{Dual certificate}
}
$$

and:

$$
\boxed{
\text{Column pricing}
=
\text{certificate counterexample search}.
}
$$

This allows the entire Claude bandwidth-one ceiling to be re-understood as a computable, iterable convex research programme where information constraints can be incrementally added.

The next thing truly worth doing is:

$$
\boxed{
\text{certified pricing}
+
\text{minimal }I_{70}^*\text{ search}.
}
$$