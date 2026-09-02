# 12 — Arithmetic Realizability Bridge
## From the Unconditional Prime Side at $\sigma=1$ to the Arithmetic Requirements of $P_{70}/P_{80}/P_{90}/P_{95}/P_{99}$

**Date:** 2026-08-11  
**Status:** source-grounded reconstruction + derived conditional schema  
**Core Question:**

$$
\boxed{
\text{The extremal side already knows how much support is needed;
what exactly must the arithmetic side provide to legitimately realize it?}
}
$$

---

# 0. Known Boundary: Why is Claude Stuck at $\sigma=1$?

Claude Proposition 5.6 decomposes the quadratic mean of the prime polynomial

$$
P_X
$$

as:

$$
\mathcal M[P_X,P_X]
=
D+O_1+O_2.
$$

where the diagonal is:

$$
D
\sim
\frac{TL^3}{6\pi},
$$

and is currently bounded using the Montgomery–Vaughan generalized Hilbert inequality:

$$
\boxed{
O_1\ll L^2X.
}
$$

If:

$$
X=(T/2\pi)^\sigma,
$$

ignoring fixed constants:

$$
\frac{|O_1|}{D}
\ll
\frac{X}{TL}
\asymp
\frac{T^{\sigma-1}}{\log T}.
$$

Thus:

### $\sigma<1$

$$
\frac{|O_1|}{D}\to0.
$$

### $\sigma=1$

$$
\frac{|O_1|}{D}
\ll
\frac1{\log T}
\to0.
$$

### Any Fixed $\sigma>1$

$$
\frac{|O_1|}{D}
\gg
\frac{T^{\sigma-1}}{\log T},
$$

the current absolute value bound fails.

This is not merely a matter of the "proof technique not being elegant enough"; rather, the off-diagonal terms must begin to be **evaluated**, not just **bounded away**.

---

# 1. What Prime-Pair Scale Does the Off-Diagonal Actually Probe?

Claude's $O_1$ contains:

$$
\frac{1}{\log n-\log m}
$$

and:

$$
(n/m)^{iT}
$$

-like oscillations.

For:

$$
n\sim m\sim X,
$$

let:

$$
h=n-m.
$$

When:

$$
|h|\ll X
$$

we have:

$$
\log(n/m)
=
\log\left(1+\frac{h}{m}\right)
\approx
\frac{h}{X}.
$$

The time interval length is $T$, so the near-diagonal region where the off-diagonal cannot sufficiently oscillatory-cancel roughly satisfies:

$$
T|\log(n/m)|
\lesssim1.
$$

That is:

$$
\boxed{
|h|
\lesssim
\frac XT.
}
$$

If:

$$
X=T^\sigma,
$$

then:

$$
\boxed{
H_\sigma
\asymp
T^{\sigma-1}.
}
$$

Expressed in the prime scale $X$:

$$
T=X^{1/\sigma},
$$

thus:

$$
\boxed{
H_\sigma
\asymp
X^{1-1/\sigma}.
}
$$

**This section is a scale inference derived from the explicit $O_1$ formula in Claude Proposition 5.6; it is not a formula directly listed in Claude's original text.**

---

# 2. Prime-Pair Shift Scales Corresponding to CPL Proportions

From the v8 generalized one-delta reconstruction:

| target | $\sigma$ | $H_\sigma$ in $T$ scale | $H_\sigma$ in prime scale $X$ |
|---|---:|---:|---:|
| $70\%$ | $1.042628$ | $T^{0.042628}$ | $X^{0.040885}$ |
| $80\%$ | $1.257848$ | $T^{0.257848}$ | $X^{0.204991}$ |
| $90\%$ | $1.701455$ | $T^{0.701455}$ | $X^{0.412268}$ |
| $95\%$ | $2.260790$ | $T^{1.260790}$ | $X^{0.557677}$ |
| $99\%$ | $4.187215$ | $T^{3.187215}$ | $X^{0.761178}$ |

The physical meaning here is not "we need to know all $h$ up to this point."

Rather:

> When the Dirichlet polynomial grows to $X=T^\sigma$, the near-diagonal pair interactions naturally fall into this additive-shift scale; without sufficient averaged or shift-by-shift prime-pair information, $O_1$ cannot yield the required main term / cancellation.

---

# 3. A Classical Strong Hardy–Littlewood Input

Goldston's pair-correlation notes record the strong prime-pair hypothesis used by Montgomery:

$$
\boxed{
\sum_{n\le N}
\Lambda(n)\Lambda(n+k)
=
\mathfrak S(k)N
+
O_\varepsilon(N^{1/2+\varepsilon}),
}
$$

uniformly for:

$$
0<k\le N.
$$

where:

$$
\mathfrak S(k)
$$

is the prime-pair singular series.

Goldston also notes: this strong error version is sufficient to derive the Strong Pair Correlation:

$$
F(\alpha,T)
=
1+o(1)
$$

up to:

$$
\boxed{
1\le\alpha\le2-\varepsilon.
}
$$

---

# 4. The First Major Boundary: $90\%$ and $95\%$

We reconstructed:

$$
\sigma_{70}\approx1.043<2,
$$

$$
\sigma_{80}\approx1.258<2,
$$

$$
\sigma_{90}\approx1.701<2.
$$

Therefore, within the **classical Montgomery arithmetic heuristic / the strong HL framework compiled by Goldston**:

$$
\boxed{
P_{70},P_{80},P_{90}
}
$$

all still fall within:

$$
\alpha<2
$$

the range that this strong prime-pair hypothesis can supply.

However:

$$
\sigma_{95}\approx2.261>2,
$$

$$
\sigma_{99}\approx4.187>2.
$$

Thus:

$$
\boxed{
P_{95},P_{99}
}
$$

have already stepped outside the standard region where "the shift-by-shift Hardy–Littlewood pair conjecture with square-root error is known to imply SPC."

This is a more substantial **arithmetic regime change** than a mere $q=90\%\to95\%$.

---

# 5. The Second Arithmetic Input: Prime Variance / Short Intervals

The classical Goldston–Montgomery equivalence (contextualized under RH in the original literature) connects the Strong Pair Correlation with the second moment of primes in short intervals:

$$
\int_1^X
\left(
\psi(x+h)-\psi(x)-h
\right)^2dx
\sim
hX\log\frac Xh.
$$

Goldston's notes specifically point out:

> The square-root error of the shift-by-shift twin-prime conjecture only directly gives SPC up to $\alpha<2$;  
> but this weaker, averaged short-interval second-moment hypothesis can supply the full fixed support range for SPC.

So for $P_{95},P_{99}$, the more natural arithmetic hypothesis is not to require an extremely strong pointwise Hardy–Littlewood error for every shift, but rather to require:

$$
\boxed{
\text{a prime short-interval variance asymptotic over a sufficiently wide scale}.
}
$$

---

# 6. Defining Three Tiers of Arithmetic Bridge Hypotheses

To avoid stating "HL is needed" too vaguely, CPL temporarily divides this into three tiers.

## ABH-1 — Direct Prime-Side Trace Hypothesis

For a specified support $\sigma$ and optimized one-delta family, assume Claude's prime-side trace evaluation can be extended such that:

$$
\frac{
(\operatorname{tr}\widetilde G)^2
}{
N\operatorname{tr}(\widetilde G^2)
}
\to
c(\sigma),
$$

where:

$$
c(\sigma)
=
\frac{1}{2-q(\sigma)}.
$$

This is the hypothesis **closest to the Claude proof pipeline**.

It avoids pre-specifying which prime conjecture must be responsible.

---

## ABH-2 — Partial Strong Pair Correlation

Assume:

$$
F(\alpha,T)=1+o(1)
$$

uniformly for:

$$
1\le|\alpha|\le\sigma.
$$

Together with the known $|\alpha|\le1$ region, this provides the full pair data up to $\sigma$ required for the generalized one-delta certificate.

This is in the language of zero/pair-statistics.

---

## ABH-3 — Arithmetic Realization

Using prime-side sufficient conditions, for example:

### For $\sigma<2$

The strong Hardy–Littlewood prime-pair:

$$
\sum_{n\le N}\Lambda(n)\Lambda(n+h)
=
\mathfrak S(h)N+O(N^{1/2+\varepsilon})
$$

classical framework.

### For Larger Fixed $\sigma$

Adopt a:

$$
\int
(\psi(x+h)-\psi(x)-h)^2dx
$$

-type short-interval variance asymptotic, or directly assume the arithmetic input required for full SPC / PCC.

---

# 7. Derived Conditional Theorem Schema

Below is **a conditional schema reconstructed in this study based on Claude's linear-algebra pipeline + the v8 one-delta operator; it is not a verbatim theorem from the source paper.**

If for some fixed:

$$
\sigma>1
$$

one can legitimately extend the prime-side second-trace evaluation of Claude Proposition 5.6 / Theorem 5.8 to the optimized support-$\sigma$ one-delta test family, while keeping all localization / taper errors:

$$
o(N(T,2T)),
$$

such that the corresponding trace ratio is:

$$
c(\sigma)
=
\frac1{2-q(\sigma)},
$$

then the same zero-side inertia + rank–trace mechanism should yield:

$$
\boxed{
\liminf_{T\to\infty}
\frac{
N_0^s(T,2T)
}{
N(T,2T)
}
\ge
q(\sigma).
}
$$

Thus:

### If the Arithmetic Side Can Realize $\sigma=1.04263$

$$
P_{70}
$$

enters conditional closure.

### If It Can Realize $\sigma=1.25785$

$$
P_{80}.
$$

### If It Can Realize $\sigma=1.70146$

$$
P_{90}.
$$

This breaks the problem down very cleanly:

$$
\boxed{
\text{Proportion threshold}
\rightarrow
\text{extremal support}
\rightarrow
\text{arithmetic realization}.
}
$$

---

# 8. How Can the Minimal Arithmetic Problem for $P_{70}$ Be Posed Now?

We no longer ask:

> "Can we prove $70\%$?"

Instead, we ask:

$$
\boxed{
\text{Can we push the prime-side second trace
from }X\le T
\text{ to }
X\le T^{1.04263}
\text{?}
}
$$

Converted to an additive shift:

$$
\boxed{
h
\lesssim
T^{0.04263}.
}
$$

Or in the prime scale:

$$
\boxed{
h
\lesssim
X^{0.04089}.
}
$$

This scale is very small.

But the real difficulty is not that the exponent is small, but rather:

$$
\boxed{
\text{it has already stepped outside the diagonal-only mean-value regime.}
}
$$

Therefore, even just going from:

$$
1
\to
1.0001
$$

is already a qualitative change.

---

# 9. A Noteworthy Historical Comparison

Goldston's notes state that Montgomery's strong Hardy–Littlewood hypothesis allows the program to be carried out up to:

$$
x\le T\le x^{2-\varepsilon},
$$

which is:

$$
\alpha<2.
$$

So from a historical perspective:

$$
P_{90}
$$

requires:

$$
\sigma\approx1.70
$$

which still falls within the range that Montgomery's original prime-pair heuristic was expected to handle.

The first CPL node that truly begins to demand a new arithmetic regime is instead:

$$
\boxed{
P_{95}
}
$$

because:

$$
\sigma_{95}\approx2.26.
$$

This point is highly non-intuitive in the "proportion ladder," but is visible at a glance in the "support ladder."

---

# 10. What is Most Worth Doing in the Next Round?

There are currently three routes.

## Route A — $P_{70}$ Weighted Prime-Pair Hypothesis

Starting from the actual:

$$
O_1
$$

formula in Claude Proposition 5.6, instead of assuming the full Hardy–Littlewood, we only extract **a weighted prime-pair asymptotic sufficient to make the optimized $\sigma=1.04263$ test hold**.

This might be much weaker than the standard pointwise HL.

## Route B — Average-$h$ Hypothesis

Because $O_1$ itself has smooth weights on $n,m$, we might not need a prime-pair asymptotic for:

$$
\forall h
$$

We can investigate:

$$
\sum_h W(h/H)
\left[
\sum_n\Lambda(n)\Lambda(n+h)-\mathfrak S(h)X
\right]
$$

requiring only:

$$
o(\text{main}).
$$

This would be closer to the modern "average Hardy–Littlewood" or short-interval variance.

## Route C — Unconditional Partial Escape

Search for whether there exist currently proven results that, although insufficient to yield:

$$
F(\alpha)\sim1
$$

can provide a one-sided bound for:

$$
1<\alpha<1+\delta
$$

and test whether we can push $67.25\%$ up a bit.

This might not reach $70\%$, but if we can unconditionally break through:

$$
68.185\%
$$

that would be a result on an entirely different level.

---

# 11. Conclusion of This Round

We have advanced from:

$$
\text{"$\sigma>1$ requires prime pairs"}
$$

to:

$$
\boxed{
\text{Target proportion}
\rightarrow
\sigma_q
\rightarrow
X=T^{\sigma_q}
\rightarrow
h\sim X/T
\rightarrow
\text{required arithmetic correlation scale}.
}
$$

This makes the true QCI of $P_{70}$ operational:

$$
\boxed{
X:T\to T^{1.04263}
}
$$

is the first wall.