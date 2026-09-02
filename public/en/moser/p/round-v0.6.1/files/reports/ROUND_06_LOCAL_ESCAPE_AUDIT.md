# Round 6 Supplementary Audit for Local Out-of-Bounds

Centered at the event root, sampling was performed across seven scale radii, with $900$ eight-dimensional directions per radius, totaling 6300 valid general 5-bar linkage candidates.

Each candidate was first coarsely evaluated using $2048$ phases with dual chirality, and the top $30$ were then verified using $32768$ phases with dual chirality and local refinement.

## Results

Event root:

$$
s_0=0.998903757132509.
$$

Best non-baseline candidate:

$$
s_{\mathrm{local}}=0.998790843965457.
$$

Relative to the event root:

$$
s_{\mathrm{local}}-s_0
=
-1.129131670519e-04.
$$

High-resolution candidates genuinely exceeding the event root:

$$
0.
$$

Therefore, in this multi-scale finite sampling and high-resolution verification, no reproducible local chiral out-of-bounds events were found. This does not constitute a proof of local optimality for the general 5-bar linkage, but it provides stronger support for the local stability of the event root than a single differential evolution failure.