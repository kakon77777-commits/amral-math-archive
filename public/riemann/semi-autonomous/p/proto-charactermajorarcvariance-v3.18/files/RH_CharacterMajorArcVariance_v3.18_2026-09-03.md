工程紀錄 · 第五弧線 v3.18 · 2026-09-03 · CHARACTER_MAJOR_ARC_VARIANCE · MINOR_ARC_FIXED_POWER · ZERO_PACKET_ENERGY · DENSITY_ONLY_NO_GO · RH_CLAIM_FALSE

# Character Major-Arc Variance：Minor-Arc Fixed Power、Character Zero Packets 與 Density-Only No-Go

**RH-CharacterMajorArcVariance v3.18**

本節點承接：

- `RH-PrimeStructuredApproximationGap v3.17`
- `RH-FourPointPrimeDeviation v3.16`
- Maynard–Pandey–Radziwiłł 2026 prime exponential-sum bound
- Chen–Gupta–Li 2026 Dirichlet $L$-zero density estimate
- Chou–Haag–Huryn–Ledoan prime-pair variance framework

v3.17 concluded that ordinary approximation of：

$$
\Lambda
$$

is not the correct fixed-power object。

The correct target is the quadratic pair spectrum：

$$
\boxed{
|S_x(\alpha)|^2.
}
$$

v3.18 sharpens that conclusion further。

The actual-prime branch splits naturally into：

```text
GENUINE MINOR ARCS
    polynomial cancellation available

CHARACTER MAJOR ARCS
    zero-sensitive structured variance

EXTREME / EXCEPTIONAL ZERO PACKETS
    fixed-power blocker
```

The most important correction to v3.17 is：

$$
\boxed{
\text{the pseudorandom/minor-arc side is not intrinsically limited to log-power.}
}
$$

For the pair-spectrum problem, modern pointwise exponential-sum bounds over primes give an actual polynomial saving on genuine minor arcs。

The remaining fixed-power obstruction is therefore concentrated in the structured major arcs and their Dirichlet-character zero packets。

No new zero strip is proved。

**RH_CLAIM = False.**

---

# 0. Claim register

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE

DETERMINISTIC_ETA_M = 1/2

MPR_2026_PRIME_EXPONENTIAL_SUM = EXTERNAL_CURRENT
MINOR_ARC_PRIME_FOURTH_MOMENT_FIXED_POWER = CLOSED_AS_CONSEQUENCE

CHARACTER_RATIONAL_CENTER_DECOMPOSITION = CLOSED
SMOOTH_OFFSET_CHARACTER_DECOMPOSITION = CLOSED
CHARACTER_L2_ORTHOGONALITY = CLOSED

ZERO_KERNEL_SCALING = CLOSED
POLE_ZERO_CROSS_SCALE = x^(1+2 Re rho)
PURE_ZERO_SCALE = x^(4 Re rho - 1)

CHARACTER_MAJOR_ZERO_ENERGY_GATE = CLOSED_AS_SUFFICIENT_SUBGATE

DIRICHLET_ZERO_DENSITY_7_OVER_3 = EXTERNAL_CURRENT
DENSITY_ONLY_FIXED_POWER_CLOSURE = NO

EXCEPTIONAL_MAJOR_ARC_FIXED_POWER = OPEN
PPEU_ETA_POSITIVE = OPEN
PVAA_ETA_POSITIVE = OPEN
ETA_Q_POSITIVE = OPEN

GLOBAL_RH_CERTIFICATE = FALSE
```

---

# 1. Prime exponential sum

Define：

$$
\boxed{
S_N(\alpha)
=
\sum_{n<N}
\Lambda(n)e(n\alpha).
}
$$

Dirichlet approximation writes：

$$
\boxed{
\alpha
=
\frac aq+\epsilon,
}
$$

with：

$$
(a,q)=1,
$$

$$
q\le N^{1/2},
$$

and：

$$
|\epsilon|
\le
\frac1{qN^{1/2}}.
$$

Define：

$$
\boxed{
B(\alpha)
=
\max(
q,\,
qN|\epsilon|
).
}
$$

---

# 2. 2026 exponential-sum input

Maynard–Pandey–Radziwiłł prove：

$$
\boxed{
|S_N(\alpha)|
\le
N^{o(1)}
\left(
\frac{N}{B(\alpha)^{1/2}}
+
N^{19/24}
\right).
}
$$

This improves the classical：

$$
N^{4/5}
$$

generic term to：

$$
N^{19/24}.
$$

Their paper explicitly notes that the：

$$
N/B^{1/2}
$$

term may morally be viewed as arising from possible exceptional zeros with real part close to one。

This is exactly the structural distinction needed in the AMRAL prime branch。

---

# 3. Genuine minor arcs

For：

$$
0<\theta\le\frac12,
$$

define：

$$
\boxed{
\mathfrak m_\theta
=
\{
\alpha:
B(\alpha)\ge N^\theta
\}.
}
$$

Then Section 2 gives：

$$
\boxed{
\sup_{
\alpha\in\mathfrak m_\theta
}
|S_N(\alpha)|
\le
N^{o(1)}
\left(
N^{1-\theta/2}
+
N^{19/24}
\right).
}
$$

---

# 4. Minor-arc fourth moment

Parseval gives：

$$
\boxed{
\int_0^1
|S_N(\alpha)|^2d\alpha
=
\sum_{n<N}
\Lambda(n)^2
=
N^{1+o(1)}.
}
$$

Therefore：

$$
\begin{aligned}
\int_{\mathfrak m_\theta}
|S_N(\alpha)|^4d\alpha
&\le
\sup_{\mathfrak m_\theta}
|S_N|^2
\int_0^1|S_N|^2.
\end{aligned}
$$

Hence：

## Theorem 4.1 · Prime Minor-Arc Fourth Moment

$$
\boxed{
\int_{\mathfrak m_\theta}
|S_N(\alpha)|^4d\alpha
\ll
N^{
\max(
3-\theta,\,
31/12
)
+o(1)
}.
}
$$

Relative to the：

$$
N^3
$$

pair-spectrum fourth-moment scale, the prime exponential sum has minor-arc saving：

$$
\boxed{
\eta_{\rm minor}
=
\min(
\theta,\,
5/12
).
}
$$

At the maximal Dirichlet-approximation threshold：

$$
\theta=\frac12,
$$

one gets：

$$
\boxed{
\int_{\mathfrak m_{1/2}}
|S_N|^4
\ll
N^{31/12+o(1)}.
}
$$

This is a saving：

$$
\boxed{
5/12.
}
$$

This theorem controls the **prime fourth-moment component** on genuine minor arcs。

A complete PPEU proof must still localize the deterministic pair-model polynomial consistently；that localization is not silently assumed here。

---

# 5. Smooth major-arc sum

Let：

$$
w\in C_c^\infty((0,\infty))
$$

be nonzero and supported in a fixed compact interval。

Define：

$$
\boxed{
S_w(x,\alpha)
=
\sum_n
\Lambda(n)
w(n/x)
e(n\alpha).
}
$$

For：

$$
\alpha
=
\frac aq+\epsilon,
\qquad
(a,q)=1,
$$

define the character-twisted sum：

$$
\boxed{
S_{w,\chi}(x,\epsilon)
=
\sum_n
\Lambda(n)
\chi(n)
w(n/x)
e(n\epsilon).
}
$$

---

# 6. Exact character decomposition at the rational center

For：

$$
(n,q)=1,
$$

character orthogonality gives：

$$
\boxed{
e(an/q)
=
\frac1{\phi(q)}
\sum_{\chi\bmod q}
\tau(\overline\chi)
\chi(a)
\chi(n).
}
$$

Therefore：

## Theorem 6.1

$$
\boxed{
S_w\left(
x,\frac aq+\epsilon
\right)
=
\frac1{\phi(q)}
\sum_{\chi\bmod q}
\tau(\overline\chi)
\chi(a)
S_{w,\chi}(x,\epsilon)
+
\mathcal L_q(x,\epsilon),
}
$$

where the local term：

$$
\mathcal L_q
$$

contains prime powers whose underlying prime divides：

$$
q.
$$

Uniformly for fixed smooth：

$$
w,
$$

$$
\boxed{
\mathcal L_q
\ll
\omega(q)\log x.
}
$$

---

# 7. Mellin / explicit-formula kernel

Define：

$$
\boxed{
W_{x,\epsilon}(s)
=
\int_0^\infty
w(t/x)
e(\epsilon t)
t^{s-1}dt.
}
$$

After passing each character to its inducing primitive character and separating finitely many Euler factors, the explicit formula has the structure：

$$
\boxed{
S_{w,\chi}(x,\epsilon)
=
\delta_\chi
W_{x,\epsilon}(1)
-
\sum_{\rho_\chi}
W_{x,\epsilon}(\rho_\chi)
+
\mathcal R_\chi(x,\epsilon),
}
$$

where：

- $\delta_\chi$ records the pole of the induced principal $L$-function；
- $\rho_\chi$ runs over nontrivial zeros of the inducing primitive Dirichlet $L$-function；
- $\mathcal R_\chi$ contains trivial-zero, local Euler-factor, and shifted-contour terms。

The exact form of：

$$
\mathcal R_\chi
$$

is not needed for the structural reductions below。

---

# 8. Core-arc scaling

Write：

$$
\epsilon=\frac ux.
$$

Changing variables：

$$
t=xv
$$

gives the exact identity：

## Theorem 8.1

$$
\boxed{
W_{x,u/x}(s)
=
x^s
\mathcal W_s(u),
}
$$

where：

$$
\boxed{
\mathcal W_s(u)
=
\int_0^\infty
w(v)e(uv)v^{s-1}dv.
}
$$

Thus a zero：

$$
\rho=\sigma+i\gamma
$$

contributes an amplitude with power scale：

$$
\boxed{
x^\sigma.
}
$$

---

# 9. Pole–zero cross energy scaling

Fix：

$$
U>0.
$$

Define：

$$
\boxed{
C_{w,U}(\rho)
=
\int_{-U}^{U}
|
\mathcal W_1(u)
|^2
|
\mathcal W_\rho(u)
|^2du.
}
$$

Since：

$$
w\ne0,
$$

this is finite and positive for every fixed：

$$
\rho
$$

in a compact vertical strip away from singular endpoints。

Using：

$$
d\epsilon=\frac{du}{x},
$$

Theorem 8.1 gives：

## Theorem 9.1 · Zero Cross Kernel

$$
\boxed{
\int_{|\epsilon|\le U/x}
|
W_{x,\epsilon}(1)
|^2
|
W_{x,\epsilon}(\rho)
|^2
d\epsilon
=
x^{1+2\sigma}
C_{w,U}(\rho).
}
$$

So the natural pair-variance power of a pole–zero interaction is：

$$
\boxed{
1+2\Re\rho.
}
$$

This is the same exponent that appears in rightmost-zero sensitivity of prime-pair variance。

---

# 10. Pure zero fourth-energy scaling

Define：

$$
\boxed{
D_{w,U}(\rho)
=
\int_{-U}^{U}
|
\mathcal W_\rho(u)
|^4du.
}
$$

Then：

## Theorem 10.1

$$
\boxed{
\int_{|\epsilon|\le U/x}
|
W_{x,\epsilon}(\rho)
|^4d\epsilon
=
x^{4\sigma-1}
D_{w,U}(\rho).
}
$$

Thus a zero close to：

$$
\Re\rho=1
$$

also naturally lives at the cubic pair-variance scale in the pure zero channel。

---

# 11. Character zero packet

Define：

$$
\boxed{
Z_\chi(x,\epsilon)
=
\sum_{\rho_\chi}
W_{x,\epsilon}(\rho_\chi),
}
$$

with whatever finite truncation / convergent explicit-formula interpretation is used in the chosen major-arc implementation。

For squarefree：

$$
q,
$$

the pole coefficient of the principal character is：

$$
\boxed{
\frac{\mu(q)}{\phi(q)}.
}
$$

Define：

$$
\boxed{
P_q(x,\epsilon)
=
\frac{\mu(q)}{\phi(q)}
W_{x,\epsilon}(1),
}
$$

and the nonprincipal zero packet in residue：

$$
a:
$$

$$
\boxed{
Z_{q,a}(x,\epsilon)
=
-
\frac1{\phi(q)}
\sum_{\chi\bmod q}
\tau(\overline\chi)
\chi(a)
Z_\chi(x,\epsilon).
}
$$

Principal-character zeta-zero corrections can either be retained inside：

$$
Z_\chi
$$

or separated as a dedicated：

$$
q=1
$$

packet。

---

# 12. Character orthogonality diagonalizes zero energy

For arbitrary complex numbers：

$$
z_\chi,
$$

orthogonality gives：

## Theorem 12.1

$$
\boxed{
\sum_{\substack{
a\bmod q\\
(a,q)=1
}}
\left|
\frac1{\phi(q)}
\sum_{\chi\bmod q}
\tau(\overline\chi)
\chi(a)
z_\chi
\right|^2
=
\frac1{\phi(q)}
\sum_{\chi\bmod q}
|
\tau(\chi)
|^2
|z_\chi|^2.
}
$$

Therefore different characters do not provide a hidden cancellation in the basic quadratic zero-packet energy。

This is one reason the major-arc problem is naturally a **character family energy** problem。

---

# 13. Pole–zero major-arc energy

Define：

$$
\boxed{
\begin{aligned}
\mathfrak Z_2(x;Q,U)
&=
\sum_{\substack{
q\le Q\\
q\ {\rm squarefree}
}}
\sum_{\substack{
a\bmod q\\
(a,q)=1
}}
\\
&\quad\times
\int_{|\epsilon|\le U/x}
|
P_q(x,\epsilon)
|^2
|
Z_{q,a}(x,\epsilon)
|^2
d\epsilon.
\end{aligned}
}
$$

Using Theorem 12.1：

## Theorem 13.1

$$
\boxed{
\begin{aligned}
\mathfrak Z_2(x;Q,U)
&=
\sum_{\substack{
q\le Q\\
q\ {\rm squarefree}
}}
\frac{
|\mu(q)|^2
}{
\phi(q)^3
}
\\
&\quad\times
\sum_{\chi\bmod q}
|
\tau(\chi)
|^2
\int_{|\epsilon|\le U/x}
|
W_{x,\epsilon}(1)
|^2
|
Z_\chi(x,\epsilon)
|^2
d\epsilon.
\end{aligned}
}
$$

This is an exact positive character-energy identity once the zero packets are fixed。

---

# 14. Pure zero major-arc energy

Define：

$$
\boxed{
\mathfrak Z_4(x;Q,U)
=
\sum_{\substack{
q\le Q\\
q\ {\rm squarefree}
}}
\sum_{a\bmod q}^{*}
\int_{|\epsilon|\le U/x}
|
Z_{q,a}(x,\epsilon)
|^4d\epsilon.
}
$$

If the structured major-arc mismatch is represented schematically by：

$$
2\Re(
P_q\overline{Z_{q,a}}
)
+
|Z_{q,a}|^2
+
\text{controlled remainder},
$$

then：

$$
\boxed{
|
2\Re(P\overline Z)+|Z|^2
|^2
\le
8|P|^2|Z|^2
+
2|Z|^4.
}
$$

Thus：

$$
\boxed{
\mathfrak Z_2+\mathfrak Z_4
}
$$

is the natural positive zero-energy pair controlling the character-zero part of PVAA on core major arcs。

---

# 15. Character Major Zero Energy gate

Define：

## CMZE$(\eta)$

For a suitable polynomial major-arc range：

$$
Q=x^\theta,
$$

and fixed：

$$
U,
$$

$$
\boxed{
\mathfrak Z_2(x;Q,U)
+
\mathfrak Z_4(x;Q,U)
\ll
x^{3-\eta+o(1)}.
}
$$

Together with：

- a compatible fixed-power principal-model localization；
- the fixed-power minor-arc estimate；
- explicit-formula remainder control；

CMZE would provide a pair-adapted route toward PPEU / PVAA。

CMZE is a **major-arc subgate**, not by itself a complete PPEU theorem。

---

# 16. Single-zero channel scale

Suppose for scale auditing that a single primitive：

$$
\chi\bmod q
$$

and a single zero：

$$
\rho=\sigma+i\gamma
$$

dominate one zero packet on the core arc。

For primitive：

$$
\chi,
$$

$$
|\tau(\chi)|^2=q.
$$

The pole–zero channel has conductor weight：

$$
\boxed{
\frac{
q
}{
\phi(q)^3
}
=
q^{-2+o(1)}.
}
$$

Thus Theorem 9.1 gives the isolated-channel scale：

$$
\boxed{
q^{-2+o(1)}
x^{1+2\sigma}.
}
$$

The pure one-character fourth-energy channel has coefficient weight：

$$
\boxed{
\frac{
q^2
}{
\phi(q)^3
}
=
q^{-1+o(1)},
}
$$

and therefore scale：

$$
\boxed{
q^{-1+o(1)}
x^{4\sigma-1}.
}
$$

These are channel scales, not lower bounds for the complete zero packet after all zero–zero interference。

---

# 17. Slanted conductor frontier

Write：

$$
q=x^\kappa.
$$

To make the isolated pole–zero channel no larger than：

$$
x^{3-\eta},
$$

it is sufficient that：

$$
\boxed{
\sigma
\le
1-\frac{\eta}{2}
+\kappa.
}
$$

For the pure zero channel it is sufficient that：

$$
\boxed{
\sigma
\le
1-\frac{\eta}{4}
+\frac{\kappa}{4}.
}
$$

Thus large conductor itself discounts a zero in the pair-spectrum energy。

For fixed：

$$
q,
$$

as：

$$
x\to\infty,
$$

the pole–zero criterion reduces to：

$$
\boxed{
\sigma
\le
1-\frac{\eta}{2}.
}
$$

This explains why a single fixed-conductor rightmost zero is a genuine fixed-power obstruction。

---

# 18. Current Dirichlet zero-density theorem

The current character-family zero-density input used in the 2026 prime exponential-sum work is：

$$
\boxed{
\sum_{\chi\bmod q}
N(\sigma,T,\chi)
\ll_\varepsilon
(qT)^{
\frac73(1-\sigma)
+\varepsilon
}.
}
$$

The exponent：

$$
\frac73
$$

improves Huxley's earlier：

$$
\frac{12}{5}.
$$

Combined with classical density input in the complementary range, this already yields the intermediate prime exponential-sum exponent：

$$
\boxed{
67/84
}
$$

before the stronger direct Dirichlet-polynomial argument reaches：

$$
19/24.
$$

---

# 19. Density-only no-go

A density estimate of the generic form：

$$
\boxed{
\sum_\chi
N(\sigma,T,\chi)
\ll
(qT)^{
A(1-\sigma)
+o(1)
}
}
$$

counts how many zeros lie to the right of：

$$
\sigma.
$$

But as：

$$
\sigma\to1,
$$

the right side remains compatible with：

$$
\boxed{
\text{one zero at }
\Re\rho=1-o(1).
}
$$

For fixed：

$$
q
$$

and fixed zero height, Theorem 9.1 assigns such a zero the pole–zero power：

$$
\boxed{
x^{3-o(1)}.
}
$$

Therefore：

## Theorem 19.1 · Density-Only No-Go

A zero-density theorem of the above counting form, **without an additional fixed zero-free strip or weighted suppression of the extreme zeros**, cannot by itself imply：

$$
\boxed{
\mathfrak Z_2
\ll
x^{3-\eta}
}
$$

for any fixed：

$$
\eta>0.
$$

This statement concerns the logical strength of the density estimate alone。

It does not assert that such an extreme zero exists。

---

# 20. Relation to the 2026 exponential-sum theorem

Maynard–Pandey–Radziwiłł explicitly observe that the：

$$
N/B^{1/2}
$$

term in their prime exponential-sum bound can morally be viewed as arising from possible exceptional zeros with：

$$
\Re s
$$

close to one。

They further note that this term can be improved for all：

$$
q
$$

outside a thin exceptional set。

This is strong external confirmation of the AMRAL classification：

```text
GENERIC MINOR / NONEXCEPTIONAL STRUCTURE
    polynomially tractable

EXCEPTIONAL MAJOR ARCS
    zero-sensitive blocker
```

---

# 21. Guth–Maynard and character zero-density progress

Guth–Maynard's 2026 Annals result gives the zeta zero-density estimate：

$$
\boxed{
N(\sigma,T)
\le
T^{
30(1-\sigma)/13
+o(1)
}.
}
$$

The character-family：

$$
7/3
$$

estimate extends the same new large-values philosophy to Dirichlet $L$-functions。

These are major advances in controlling the **population** of right-half-plane zeros。

But neither theorem excludes a single power-dominant rightmost zero。

That distinction is exactly what matters for fixed-power pair variance。

---

# 22. Character-zero frontier versus PPEU

The single-endpoint prime-pair gate：

$$
\boxed{
E_{\rm pair}(x)
\ll
x^{3-\eta+o(1)}
}
$$

already implies：

$$
\Theta
\le
1-\eta/2.
$$

v3.18 explains the same exponent from the major-arc kernel：

$$
x^{1+2\sigma}.
$$

Thus the prime-pair variance lower-bound phenomenon and the character-major-arc zero-packet picture are two representations of the same rightmost-zero sensitivity。

---

# 23. Revised prime-side architecture

After v3.18：

```text
DETERMINISTIC FOUR-POINT MODEL
    eta_M = 1/2

GENUINE PRIME MINOR ARCS
    fixed power available
    current generic fourth-moment saving >= 5/12 at theta=1/2

CHARACTER MAJOR ARCS
    pole + zero packets

ZERO POPULATION
    strong density theorems

EXTREME ZERO ENERGY
    fixed-power blocker

PPEU / PVAA
    OPEN
```

This supersedes the weaker v3.17 statement that the entire pseudorandom side should be viewed as merely logarithmic-strength。

---

# 24. Canonical next gate

Define：

## Exceptional Major-Arc Energy $\operatorname{EMAE}(\eta)$

Choose a polynomial major-arc parameter：

$$
Q=x^\theta.
$$

Prove that after removing the explicit principal singular-series model：

$$
\boxed{
\text{character-zero structured variance}
\ll
x^{3-\eta+o(1)}.
}
$$

Equivalently, close CMZE together with the explicit-formula remainder and arc-overlap terms。

The strongest candidate theorem should isolate：

- low conductor；
- low / saddle-point zero height；
- exceptional real zeros；
- ordinary complex zeros；
- principal zeta zeros；

rather than treating all zeros only through a density count。

---

# 25. Why the next theorem must be weighted

A uniform fixed zero-free strip for **every** Dirichlet $L$-function would certainly close the extreme-zero problem, but it is much stronger than necessary。

The major-arc energy automatically includes：

- Gauss-sum weights；
- conductor powers；
- arc widths；
- Mellin/saddle-point decay in zero height。

Therefore the desired theorem may allow some zeros closer to one provided their total **weighted pair-spectrum energy** is power-small。

This is the main opening left after the density-only no-go。

---

# 26. Suggested v3.19 direction

Recommended：

`RH-ExceptionalZeroEnergy v3.19`

Tasks：

1. define the smoothed zero packets：
   $$
   Z_\chi(x,\epsilon)
   $$
   with an explicit zero-height truncation；
2. use the saddle-point localization：
   $$
   |\gamma|
   \asymp
   x|\epsilon|;
   $$
3. dyadically decompose：
   - conductor $q$；
   - height $T$；
   - real part $\sigma$；
4. insert the current：
   $$
   7/3
   $$
   Dirichlet zero-density theorem；
5. compute the total contribution of all **non-extreme** zero boxes；
6. isolate exactly the parameter region where density already gives：
   $$
   x^{3-\eta};
   $$
7. identify the residual **extreme-zero box**；
8. treat possible exceptional real zeros separately using Deuring–Heilbronn repulsion；
9. determine whether all remaining complex extreme zeros reduce to a finite / sparse family；
10. formulate the weakest weighted extreme-zero theorem sufficient for EMAE$(\eta)$。

The purpose of v3.19 is not to prove a uniform Dirichlet zero strip。

It is to determine whether conductor and height weights plus current density theorems already dispose of every region **except** a sharply specified exceptional frontier。

---

# 27. GAP ledger

## CLOSED / REDUCED

### G1. Genuine minor-arc prime fourth moment

```text
FIXED POWER
```

### G2. Character rational-center decomposition

```text
CLOSED
```

### G3. Character quadratic orthogonality

```text
CLOSED
```

### G4. Zero-kernel power scaling

```text
CLOSED
```

### G5. CMZE gate

```text
CLOSED_AS_REDUCTION
```

### G6. Density-only fixed-power route

```text
NO
```

---

## OPEN

### G7. EMAE$(\eta>0)$

```text
OPEN
```

### G8. PVAA / PPEU fixed power

```text
OPEN
```

### G9. FPD / EPV fixed power

```text
OPEN
```

### G10. Complete quartic $\eta_Q>0$

```text
OPEN
```

### G11. RH

```text
OPEN
```

---

# 28. Trust boundary

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE

MINOR-ARC PRIME FOURTH MOMENT FIXED SAVING
    !=
FULL PAIR-VARIANCE FIXED SAVING

CHARACTER ZERO KERNEL SCALING
    = EXACT SMOOTH MAJOR-ARC GEOMETRY

DENSITY-ONLY NO-GO
    = LIMITATION OF THE INPUT THEOREM
    NOT AN ASSERTION THAT EXTREME ZEROS EXIST

NO EMAE PROVED
NO PPEU PROVED
NO ETA_Q PROVED

GLOBAL_RH_CERTIFICATE = FALSE
```

Forbidden：

$$
\int_{\mathfrak m}|S|^4
\ll
N^{3-\delta}
\Longrightarrow
E_{\rm pair}(N)
\ll
N^{3-\delta}.
$$

The deterministic pair model must be localized consistently。

Forbidden：

$$
\text{zero-density exponent improves}
\Longrightarrow
\text{fixed zero strip}.
$$

Forbidden：

$$
\text{one isolated-zero channel scale}
\Longrightarrow
\text{a lower bound for the complete zero packet}
$$

without controlling zero–zero interference。

---

# 29. One-line status

> v3.18 identifies exceptional character major arcs as the fixed-power bottleneck of the actual-prime branch. The August 2026 Maynard–Pandey–Radziwiłł theorem gives $|S_N(\alpha)|\le N^{o(1)}(N/B^{1/2}+N^{19/24})$, so on genuine minor arcs $B\ge N^\theta$ the prime fourth moment is at most $N^{\max(3-\theta,31/12)+o(1)}$, a polynomial saving $\min(\theta,5/12)$ from the cubic pair-spectrum scale. On a smooth major arc $\alpha=a/q+\epsilon$, character orthogonality decomposes the prime sum into twisted character sums. The explicit formula then separates a pole kernel from Dirichlet-zero packets. At core scale $\epsilon=u/x$, the Mellin kernel obeys the exact scaling $W_{x,u/x}(s)=x^s\mathcal W_s(u)$, so a pole–zero interaction has energy $x^{1+2\Re\rho}$ while a pure zero fourth channel has scale $x^{4\Re\rho-1}$. Summing reduced residues diagonalizes the quadratic character-zero energy exactly, producing a positive weighted character-family object. This motivates the Character Major Zero Energy gate CMZE. The current Dirichlet family zero-density theorem $\sum_{\chi\bmod q}N(\sigma,T,\chi)\ll_\varepsilon(qT)^{7(1-\sigma)/3+\varepsilon}$ is powerful enough to improve generic prime exponential sums, but any density estimate of this counting form remains compatible with a single zero at $\Re\rho=1-o(1)$. For fixed conductor such a zero sits at the $x^{3-o(1)}$ pole–zero pair-variance scale. Hence zero density alone cannot yield a fixed $x^{-\eta}$ saving. The next node should combine conductor, height, saddle-point, and density weights to dispose of all non-extreme zero boxes and isolate the smallest exceptional-zero frontier that still obstructs CMZE.

---

# 30. References

1. James Maynard, Mayank Pandey, Maksym Radziwiłł, **Exponential sums over primes**, arXiv:2608.14777, 2026.  
   Main bound:
   $$
   |S_N(\alpha)|
   \le
   N^{o(1)}
   \left(
   N/B^{1/2}
   +
   N^{19/24}
   \right).
   $$

2. Bin Chen, Vishal Gupta, Yung Chi Li, **Large Value Estimates for Dirichlet Polynomials with Characters and Zero Density of Dirichlet $L$-Functions**, arXiv:2507.08296, revised 2026.  
   Character-family zero density:
   $$
   \sum_{\chi\bmod q}
   N(\sigma,T,\chi)
   \ll_\varepsilon
   (qT)^{7(1-\sigma)/3+\varepsilon}.
   $$

3. Larry Guth, James Maynard, **New large value estimates for Dirichlet polynomials**, *Annals of Mathematics* 203 (2026), 623–675.

4. Leon Chou, Summer Haag, Jake Huryn, Andrew Ledoan, **The error term in counting prime pairs**, *Journal of Number Theory* 278 (2026), 422–450.  
   arXiv:2308.14888.

5. D. A. Goldston, **The major arcs approximation for an exponential sum over primes**, *Acta Arithmetica* 92 (2000), 169–179.

6. AMRAL, **RH-PrimeStructuredApproximationGap v3.17**.

---

# 31. Provenance

研究主導：Neo.K

v3.18 minor-arc fixed-power audit、smooth character-major-arc decomposition、character zero-packet orthogonality、zero-kernel scaling、CMZE/EMAE gates、density-only no-go、reference implementation 與 canonical source 整理：ChatGPT / GPT-5.6 Sol

日期：2026-09-03

研究定位：AMRAL 黎曼猜想半自主研究線，第五弧線 exceptional major-arc / weighted character-zero energy 節點。

本文件是 research source artifact，不是 peer-reviewed publication。

所有 claim 必須依 Claim register、GAP ledger 與 Trust boundary 解讀。
