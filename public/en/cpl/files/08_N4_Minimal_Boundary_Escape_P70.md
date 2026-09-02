# 08 — Minimal Boundary-Escape Frontier of the Toy $P_{70}$
## How Much More Must Be Known About $S(4)$ to Cross $70\%$?

**Date:** 2026-08-11  
**Status:** numerical column-generation frontier; not yet exact-rational certification  
**Scope:** $N=4$ continuous-position toy model

---

# 0. Problem

The open-band toy only knows:

$$
S(1),S(2),S(3).
$$

Now, add a minimal piece of extra information:

$$
\boxed{
\mathbb E[S(4)]\le B.
}
$$

Re-evaluate:

$$
p_{\min}(B).
$$

The goal is to find:

$$
B^*_{70}
=
\sup\{
B:
p_{\min}(B)\ge0.70
\}.
$$

---

# 1. Continuous column-generation candidate

In this round, we re-evaluated and obtained:

$$
B=3.67
\quad\Longrightarrow\quad
p_{\min}^{cand}
=
69.9981973\%.
$$

Whereas:

$$
B=3.65
\quad\Longrightarrow\quad
p_{\min}^{cand}
=
70.0595514\%.
$$

Thus, the numerical threshold is bounded approximately between:

$$
\boxed{
3.65
<
B^*_{70}
<
3.67
}
$$

Performing local linear interpolation with these two points yields the exploratory value:

$$
B^*_{70}
\approx
3.66941.
$$

**This $3.66941$ is not a theorem.**

It is merely the target position for the next exact certificate.

---

# 2. Why is this conceptually valuable?

The boundary row of the open-band optimum itself is on the order of approximately:

$$
S(4)\approx3.73
$$

Therefore, to push the $N=4$ floor from about:

$$
69.82\%
$$

past:

$$
70\%,
$$

we do not need to forcefully suppress the boundary row down to the CUE value:

$$
1.
$$

We only need to eliminate a small fraction of the most extreme spike freedom.

That is:

$$
\boxed{
\text{Information required to breach $70\%$}
\ll
\text{Knowing the boundary row completely}.
}
$$

This is exactly what the concept of "minimal escape information" aims to measure.

---

# 3. Significance of the dual price

After adding:

$$
S(4)\le B
$$

to the master problem, the numerical dual price of the boundary constraint is approximately:

$$
-0.0307.
$$

This indicates that in the current local regime, slightly tightening $B$ raises the certificate floor proportionally by about:

$$
0.0307.
$$

Intuitively:

> Originally, $S(4)$ was a direction where information could be hidden for free; now, it begins to have a price.

---

# 4. The next certification target

For:

$$
B=3.65
$$

the numerical dual candidate is approximately:

$$
c_0\approx1.12274224,
$$

$$
y_1\approx-0.38437941,
$$

$$
y_2\approx-0.25114540,
$$

$$
y_3\approx-0.11796917,
$$

$$
\mu_4\approx-0.03068556.
$$

If we adjust $c_0$ downward by $5\times10^{-5}$ to leave a safety margin:

$$
c_0=1.12269224,
$$

then the dual objective remains:

$$
\boxed{
0.700545516
=
70.0545516\%.
}
$$

Meanwhile, the numerical global search shows that the minimum reduced-cost for all three multiplicity patterns is approximately:

$$
5\times10^{-5}>0.
$$

Thus, this is a very strong **exact-certificate candidate**.

The remaining work is no longer about finding numbers, but rather taking:

$$
(1,1,1,1)
$$

and converting the positivity of its three-position degrees of freedom into an exact polynomial / SOS / interval certificate.

Once completed, we will obtain the toy model's first true:

$$
\boxed{
P_{70}\text{ escape certificate}.
}
$$

---

# 5. Relationship with the true Claude $1.04$ support

Here:

$$
S(4)
$$

for the $N=4$ toy is located exactly at the normalized boundary:

$$
\alpha=1.
$$

In the true zeta problem, the Claude paper estimates that $70\%$ requires approximately:

$$
\sigma\approx1.04.
$$

The two cannot be equated numerically.

However, they are structurally highly consistent:

$$
\text{open-band ceiling}
\rightarrow
\text{start looking at boundary / beyond-band}
\rightarrow
\text{adversarial feasible set shrinks}.
$$

Therefore, the role of the $N=4$ toy is not to predict:

$$
1.04,
$$

but to dissect:

> **Why does the proportion floor rise once we start charging for the boundary-spike?**

---

# 6. Tools for the next step of rigor

For the fully-simple pattern with three-position degrees of freedom, the most natural next level is not to add more brute-force sampling, but rather:

1. trigonometric polynomial positivity;
2. Fejér–Riesz / Hermitian-square;
3. SOS / SDP relaxation;
4. exact rational rounding;
5. proof-assistant replay.

This is fully compatible with existing exact SOHS / SDP positivity certification techniques.