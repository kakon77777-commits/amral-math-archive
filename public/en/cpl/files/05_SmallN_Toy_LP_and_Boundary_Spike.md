# 05 — Small-$N$ Primal Toy LP and Boundary-Spike Escape
## First Independent Reproduction of the Bandwidth-One Adversarial-Law Mechanism

**Date:** 2026-08-11  
**Status:** Exploratory / toy-model result  
**Limitations:** Not a reproduction of Anthropic's $N=256$ exact-rational LP; this model restricts positions to discrete circular grid points.

---

## 1. Toy primal

Configuration:

$$
n_k\in\{0,1,2\},
\qquad
\sum_{k=0}^{M-1}n_k=N.
$$

Simple fraction:

$$
p(\mathcal C)
=
\frac{\#\{k:n_k=1\}}{N}.
$$

Form factor:

$$
S_{\mathcal C}(j)
=
\frac1N
\left|
\sum_{k=0}^{M-1}n_ke^{2\pi ijk/M}
\right|^2.
$$

Solve for the configuration law $w_c$:

$$
\min_{w_c}\sum_cw_cp_c
$$

subject to:

$$
w_c\ge0,\qquad\sum_cw_c=1,
$$

and:

$$
\sum_cw_cS_c(j)=\frac jN,
\qquad j=1,\ldots,N-1.
$$

---

## 2. Open-band Results

Representative values we have independently solved:

| $N$ | $M$ | $p_{\min}$ |
|---:|---:|---:|
| 4 | 8 | 71.3388% |
| 4 | 12 | 70.8333% |
| 4 | 16 | 70.4798% |
| 4 | 24 | 70.1828% |
| 5 | 10 | 70.9443% |
| 5 | 15 | 70.3565% |
| 5 | 20 | 70.0460% |
| 6 | 18 | 70.0966% |
| 7 | 14 | 70.6078% |
| 8 | 16 | 70.5267% |

Therefore, even within a toy configuration class much narrower than the official one, the following has already emerged:

$$
\boxed{
\text{open-band pair rows perfectly matching CUE}
\not\Rightarrow
\text{simple fraction approaching }1.
}
$$

Our toy floor is around $70\%$; the official, broader rational-position configuration law can push this down to approximately $68.18\%$.

---

## 3. Explicit Mixture for $N=4,M=24$

The LP extremum requires only four support configurations; for details, see:

```text
results/toy_optimal_law_N4_M24.csv
```

After mixing:

$$
\bar S(1)=\frac14,\qquad
\bar S(2)=\frac12,\qquad
\bar S(3)=\frac34,
$$

However:

$$
\bar p
=
0.7018283569\ldots.
$$

The unconstrained closed-band row is instead:

$$
\bar S(4)
\approx3.68563.
$$

---

## 4. The Boundary Spike in the Official $N=256$ Law

Anthropic's `LawN256.lean` gives:

$$
|256S(j)-j|
\le3\times10^{-40},
\qquad
1\le j<256.
$$

But combining the final row enclosure with:

$$
K=2^{140}
$$

yields:

$$
\boxed{
S(256)\approx211.432009142486.
}
$$

That is:

```text
open band j<256:
almost perfect CUE ramp

closed row j=256:
massive spike
```

If we temporarily treat the first $255$ rows as exactly $j/256$, then:

$$
D(1)
=
\frac1{256}\sum_{j=1}^{256}S(j)-\frac12
\approx
\frac{S(256)-1/2}{256}
\approx0.82395316,
$$

which matches the official kernel-checked bound:

$$
|D(1)|\le0.82395317.
$$

This is a rather strong clue: the low simple-fraction extremal law pushes a massive amount of distinguishable information into channels outside/at the boundary of the open band.

---

## 5. Boundary-row cap experiment

Keeping all $j<N$ rows completely unchanged, we only add:

$$
\mathbb E[S(N)]\le B.
$$

For $N=4,M=24$:

| $B$ | $p_{\min}$ |
|---:|---:|
| unconstrained $\approx3.686$ | 70.18% |
| 3.5 | 70.65% |
| 3.0 | 72.49% |
| 2.5 | 74.85% |
| 2.0 | 77.20% |
| 1.5 | 79.55% |
| 1.25 | 80.73% |
| 1.0 | 81.91% |

$N=5,6$ show the same directional trend.

Thus, the toy model has empirically verified:

$$
\boxed{
\text{Adding just one boundary observable can significantly raise the adversarial simple-fraction floor.}
}
$$

---

## 6. Support extension experiment

Enforcing:

$$
S(j)=\min(j/N,1)
$$

to higher rows.

For $N=4,M=24$:

$$
j\le3
\Rightarrow70.18\%,
$$

$$
j\le4
\Rightarrow81.91\%,
$$

$$
j\le5
\Rightarrow88.85\%,
$$

$$
j\le6
\Rightarrow92.46\%.
$$

Other values of $N$ exhibit the same qualitative trend.

**These percentages cannot be directly mapped to Claude's true support thresholds of $1.04, 1.26, 1.70$.**
The toy grid is too narrow, and the row sampling is too coarse.

However, it has already reproduced the mechanism where "support expansion eliminates adversarial laws."

---

## 7. Boundary-Spike Obstruction (BSO)

Tentative definition:

> When only the open-band pair-correlation observables are fixed, a low simple-fraction configuration law can transfer a massive amount of information distinguishing the multiplicity/collision structure to unobserved frequency bands at $\alpha\approx1$ or beyond, making it almost indistinguishable from ideal CUE data within the open band.

Formally:

$$
\mathcal O_{<1}(\mathcal L_{\mathrm{bad}})
\approx
\mathcal O_{<1}(\mathcal L_{\mathrm{CUE}}),
$$

but:

$$
p(\mathcal L_{\mathrm{bad}})
\ll1,
$$

and:

$$
\mathcal O_{\ge1}(\mathcal L_{\mathrm{bad}})
$$

exhibits a strong deviation.

This concept is currently supported by:

1. $S(256)\approx211.43$ in Anthropic's exact $N=256$ law;
2. The boundary spikes in our small-$N$ toy LP.

---

## 8. A New Interpretation of $70\%$

Claude's paper states that for the same route to reach:

$$
70\%
$$

requires a pair-correlation support of approximately:

$$
1.04.
$$

This round provides a more concrete mechanistic conjecture:

$$
\boxed{
\text{The role of $1.04$ might precisely be the point where we start seeing enough data to eliminate boundary-spike extremal laws.}
}
$$

This is not yet a theorem; the next round will require reconstructing the extremal law Claude used to estimate $1.04$.

---

## 9. Next Round

### Route A — Continuous-position column generation

Currently, for the brute-force toy grid:

$$
M/N
$$

as it increases, the floor decreases, but the computational cost explodes.

The next step is to switch to:

```text
Restricted Master LP
        ↓
dual prices
        ↓
configuration pricing problem
        ↓
nonlinear / discrete search
        ↓
new adverse column
        ↓
repeat
```

Goal: To progressively approximate the official continuous rational-position primal without enumerating all configurations.

### Route B — Minimal Escape Information

Define:

$$
I^*_{70}
=
\inf\{
\text{extra observable strength}:
p_{\min}\ge0.70
\}.
$$

Test respectively:

- boundary-row inequality;
- small support extension;
- higher spectral moment;
- zeta-specific realizability constraint.

This will truly turn "$70\%$" into an optimisation problem.