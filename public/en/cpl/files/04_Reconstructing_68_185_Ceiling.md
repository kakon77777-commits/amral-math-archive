# 04 — Reconstructing the Bandwidth-One $68.185\%$ Ceiling
## From a Single Remark to Adversarial Configuration Laws, LP Duality, and Information Indistinguishability

**Status:** First round of structural reconstruction  
**Date:** 2026-08-11  
**Objective:** Identify the actual mathematical mechanism of the bandwidth-one configuration-wise certificate ceiling in Claude's paper, and pinpoint the assumptions that must be broken to reach $70\%$.

---

## 1. This Ceiling is Not Just a Narrative in the Paper

The `Zeta23/PairCeiling/` directory of Anthropic's official Lean companion repository specifically formalizes this optimality remark. The public README explicitly states that it contains a stability inequality and an explicit $N=256$ periodic law; for an appropriate bandwidth-one certificate, this law yields

$$
v\le 0.6818287+2.55\times10^{-6}\left(|r'(1)|+\int_0^1|r''(x)|\,dx\right).
$$

`LawN256.lean` further records the exact-rational simple-point fraction:

$$
p_0=\frac{10909258999421303588095230195816054408197}{16000000000000000000000000000000000000000}=0.681828687463832\ldots,
$$

namely,

$$
\boxed{68.182868746383\%}.
$$

This is already very close to the $0.68185$ used in Remark 1.1 of the paper.

---

## 2. The Observational Domain of the Certificate

Let the form-factor masses of the configuration on the grid $j/N$ be

$$
s_j=\frac{S(j)}{N},\qquad j=1,\dots,N.
$$

Define

$$
C(x)=\sum_{j/N\le x}s_j,
$$

$$
D(x)=C(x)-\frac{x^2}{2},
$$

$$
E(x)=\int_0^xD(t)\,dt.
$$

A certificate $(c_0,r)$ is valid for a configuration with a simple-point fraction $p$ if

$$
c_0+\sum_{j=1}^Ns_jr(j/N)\le p.
$$

And its value on ideal bandwidth-one CUE data is

$$
v(c_0,r)=c_0+\int_0^1r(x)x\,dx.
$$

So the real question is: **Knowing only the bandwidth-one form-factor rows, how high can $v$ be pushed by configuration-wise validity?**

---

## 3. Stability Identity

The core of `Stability.lean` is Abel summation plus two applications of integration by parts:

$$
\sum_js_jr(j/N)-\int_0^1r(x)x\,dx
=
r(1)D(1)-r'(1)E(1)+\int_0^1r''(x)E(x)\,dx.
$$

Therefore,

$$
\left|\sum_js_jr(j/N)-\int_0^1r(x)x\,dx\right|
\le
|r(1)||D(1)|+|r'(1)||E(1)|+\sup|E|\int_0^1|r''|.
$$

This is the QCI bridge that elevates "discrete near-CUE rows" to a "continuous certificate value".

---

## 4. Near-CUE Law

If

$$
|NS(j)-j|\le\tau\qquad(0<j<N),
$$

`NearCUE.lean` proves

$$
\boxed{\sup_{x\in[0,1]}|E(x)|\le\frac1{6N^2}+\frac{\tau}{2N}}.
$$

For the official law:

$$
N=256,\qquad \tau=3\times10^{-40},
$$

thus,

$$
\epsilon_{256}=2.543131510416667e-06\ldots<2.5431316\times10^{-6}.
$$

---

## 5. Signed Ceiling

If

$$
r(1)\ge0,\qquad D(1)\ge0,
$$

then in the signed integration-by-parts version, the edge term is favorable to the upper bound and can be dropped. Thus,

$$
\boxed{
v\le p_0+2.5431316\times10^{-6}\left(|r'(1)|+\int_0^1|r''(x)|\,dx\right).
}
$$

This is the finite-$N$ obstruction directly readable from the currently public Lean repo.

The difference between the $0.68185$ in the paper and the exact law is

$$
0.68185-p_0=2.13125361684385e-05.
$$

If the roughness

$$
R(r)=|r'(1)|+\int_0^1|r''(x)|\,dx
$$

is bounded by approximately

$$
R(r)\lesssim 8.380430,
$$

then this $N=256$ signed witness already suppresses the certificate to around $0.68185$.

**Note:** $p_0$ is the exact fraction of the explicit finite-$N$ law; $0.68185$ is the paper's ceiling expression for a broader certificate class. The two cannot be conflated into the same exact theorem constant.

---

## 6. The Nature of the Adversarial Law

`LawN256.lean` states that this law is a finitely-supported probability law over $256$-periodic marked configurations.

Each configuration has rational positions

$$
x_{c,i}\in[0,256),
$$

marks

$$
m_{c,i}\in\{1,2\},
$$

and

$$
\sum_im_{c,i}=256.
$$

The average form factor is

$$
S(j)=\frac1{256}\sum_cw_c\left|\sum_im_{c,i}e^{2\pi ijx_{c,i}/256}\right|^2,
$$

where

$$
w_c\ge0,\qquad\sum_cw_c=1.
$$

The Lean source describes it as the optimal law for "an exact-rational linear programme over 256-periodic marked configurations".

Therefore, its intuition is:

> Construct a world where the average pair-correlation rows almost perfectly mimic the CUE, but the average simple-point fraction is only about $68.18\%$.

Since the certificate must be valid for every configuration, it must also remain valid when averaged over this probability mixture.

Thus:

$$
\boxed{
\text{bandwidth-one pair observables are almost identical}
\not\Rightarrow
\text{simple fraction}>68.2\%.
}
$$

This is essentially an information-indistinguishability obstruction.

---

## 7. Primal / Dual Reconstruction

From the public source, its conceptual primal can be reconstructed:

$$
\min_{w_c}\sum_cw_cp_c
$$

subject to

$$
w_c\ge0,\qquad\sum_cw_c=1,
$$

and

$$
\sum_cw_cS_c(j)\approx\frac{j}{N},\qquad j=1,\dots,N-1.
$$

The final law suppresses the row error to $3\times10^{-40}$.

The dual side is the certificate: using linear/functional functionals of the observables $S(j)$ to lower-bound $p_c$.

Therefore, the ceiling is a typical minimax / LP-duality phenomenon:

```text
Primal: Find an adversarial law with a low simple fraction, but whose bandwidth-one looks like CUE.
Dual:   Find a certificate that proves a high simple fraction relying solely on bandwidth-one observables.
```

Once the primal law suppresses $p$ to $0.68183$, the dual certificate cannot unconditionally jump to $0.70$.

---

## 8. The First Missing Artifact

The official source specifies an external certificate:

```text
cert_N256_blk_b128m.json
```

SHA-256:

```text
cc3de9917db4d14d844630a4e97dda8387fd6e257e52b6967f430b8914584eb8
```

Both the README and the Lean source state it is "available from the authors", but the public repo does not currently contain this JSON.

Therefore, we can currently reconstruct:

- analytic stability;
- grid-to-continuum bridge;
- Near-CUE error;
- exact $p_0$;
- kernel-checked row enclosures;
- signed ceiling.

But for now, we cannot fully rerun:

$$
\text{configuration generation}\to\text{exact rational LP solve}\to\text{external JSON certificate}.
$$

---

## 9. Escape Classes to $70\%$

Because

$$
\Delta_{70}=0.70-p_0\approx 0.018171312536,
$$

to surpass $70\%$, at least one assumption of the ceiling must be broken:

### A. Support Escape

Increase the Fourier support, for example, Claude's paper estimates

$$
1\to1.04.
$$

### B. Moment Escape

Incorporate higher moments / higher correlations, for example, the fourth-moment conditional route can reach

$$
\frac{13}{18}=72.22\ldots\%.
$$

### C. Structural Escape

Incorporate configuration information not captured by the pair form factor.

### D. Certificate-Class Escape

Abandon the configuration-by-configuration certificate class that only reads bandwidth-one observables.

### E. Zeta-Specific Realizability Escape

Prove that this abstract extremal marked-configuration law cannot be realized by actual zeta zeros.

This last point is particularly important: the ceiling law is an abstract admissible configuration law, not a proof that "there exist actual zeta zeros with this configuration".

---

## 10. New Proposition: Bandwidth-One Escape Problem (BOEP)

Let $\mathfrak C_1$ be the certificate class of all certificates that rely solely on bandwidth-one pair-correlation observables and are configuration-wise valid. Find the minimal additional information $\mathcal I$ such that

$$
\sup_{C\in\mathfrak C_1+\mathcal I}\operatorname{Cert}(C)>0.68185.
$$

The first practical threshold:

$$
\boxed{P_{70}:\operatorname{Cert}\ge0.70.}
$$

This transforms "proportionalism" into a genuinely researchable problem:

$$
\boxed{
\text{What kind of minimal new information must be added to rule out the current extremal law?}
}
$$

---

## 11. Next Steps

1. Build a small-$N$ marked-configuration toy LP to reproduce the primal/dual obstruction.
2. Study the descent of $p_N$ with $N$ and whether it converges to approximately $0.68185$.
3. Compare the "cost of new information" between the support escape and the moment escape.
4. Search for zeta-specific realizability constraints to determine whether the abstract law is subject to additional arithmetic/topological restrictions.
5. If the official JSON is obtained, fully rerun the $N=256$ exact-rational LP.