# Round 9 Interval Certificate Interface Draft

## Existing Objects

1. Explicit decimal curve parameters;
2. Monotonic tangent angle function;
3. One-dimensional integration formula for the $270^\circ$ cusp;
4. Arbitrary-precision dual-algorithm values;
5. Darboux upper and lower sums;
6. Four control branches;
7. One-sided derivatives at $120^\circ$ and $270^\circ$.

## Missing Objects

Partition the phase circle into intervals of fixed active identity:

$$
[0,2\pi)=\bigcup_k I_k.
$$

Prove on each smooth interval:

$$
0\notin s'(I_k),
$$

or enclose the unique stationary point using the interval Newton method.

For special cusps, prove:

$$
D_-s<0<D_+s
$$

holds in a small neighborhood.

## Final Machine-Readable Goal

Establish:

$$
s(\phi)\ge s_{270}-\eta
$$

for all $\phi$, such that:

$$
\eta<s_{270}-s_0.
$$

Currently incomplete.