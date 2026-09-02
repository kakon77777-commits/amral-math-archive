# Moser Skew Field Semi-Autonomous Research: Round 15

## ——Curvature Function Modal Spectrum, Hidden Branch Opening, and New Finite-Mode Candidate

**Date:** July 26, 2026  
**Status:** Eight-mode function space exploration; full phase numerical audit; non-interval certificate  
**Continuation of:** Moser Skew Lab v0.14

---

# 1. Curvature Function Coordinates

Direct weighted orthogonalization using $z^k$ produces massive amplitudes in the low-density tails. This round switches to baseline curvature cumulative coordinates:

$$
t(u)=2\int_0^u\rho_0(v)\,dv-1.
$$

In the ideal continuous case:

$$
\rho_0(u)\,du=\frac12\,dt.
$$

Therefore, bounded modes are adopted:

$$
\psi_n(u)=\sqrt{2n+1}\,P_n(t(u)),
\qquad n=1,\ldots,8.
$$

Maximum error of the eight-mode Gram matrix:

$$
2.220e-16.
$$

| Mode | Name | Max Amplitude | Pressure Projection First Derivative |
|---:|---|---:|---:|
| 1 | `translation_like_P1` | 1.732051 | -6.332259e-09 |
| 2 | `width_split_P2` | 2.236068 | 4.809263e-07 |
| 3 | `skew_P3` | 2.645751 | 1.813983e-08 |
| 4 | `shoulder_P4` | 3.000000 | -1.978316e-06 |
| 5 | `tail_skew_P5` | 3.316625 | 4.450454e-09 |
| 6 | `triple_peak_P6` | 3.605551 | 5.430115e-07 |
| 7 | `wave_P7` | 3.872983 | 1.054055e-09 |
| 8 | `wave_P8` | 4.123106 | 3.949364e-07 |

---

# 2. First-Order Isocontour Compensation

The original five parameters are:

$$
p=(w,\beta,\delta,c,\varepsilon).
$$

For each function mode direction $a_k$, find the minimum-norm compensation $q_k$ such that the first-order variations of the four branches are equal:

$$
(G_r-G_1)q_k=-(g_{r,k}-g_{1,k}),
\qquad r=2,3,4.
$$

Thereby establishing the first-order isocontour path:

$$
p(a)=p_0+Qa.
$$

---

# 3. Pressure Projection Hessian

The Hessian in this round is defined as:

> The finite-difference Hessian of the branch-pressure-weighted Lagrangian along the first-order isocontour compensation path.

It is neither a full infinite-dimensional Hessian nor an interval Hessian.

| Eigenvalue Index | Eigenvalue |
|---:|---:|
| 1 | -3.994047425874e-05 |
| 2 | -1.677090218573e-05 |
| 3 | -7.694084915116e-06 |
| 4 | -2.511641939558e-06 |
| 5 | -2.084605783142e-06 |
| 6 | -6.856451325604e-07 |
| 7 | -8.164075413227e-08 |
| 8 | 1.329483966094e-06 |

The result consists of seven negative eigenvalues and one small positive eigenvalue:

$$
1.32948\times10^{-6}.
$$

Thus, the unimodal candidate from Round 13 is not a strict local maximum in this eight-mode space.

---

# 4. Excluded Four-Branch Candidate

If only the original four control branches are optimized, the surface scale obtained is:

$$
0.998914692247305.
$$

However, the full phase audit reveals a new intermediate low-phase branch:

$$
\phi\approx0.1390815,
$$

$$
s\approx0.9989115500.
$$

Therefore, this candidate must be excluded.

This reveals:

$$
\boxed{
\text{Function modes can invalidate the fixed active-set Hessian
by opening new phase valleys.}
}
$$

---

# 5. Effective Newton Direction

Along the pressure projection Newton direction:

$$
a(m)=m\,a_N,
$$

and re-isocontouring the five geometric parameters at each selected $m$.

As $m$ increases:

1. The original four control branches continue to rise;
2. A ninth local minimum appears after $m\approx2.2$;
3. Initially, the new branch remains higher than the control branches;
4. Around $m\approx3.228$, the new branch begins to take over.

Thus, there exists a finite ascent window bounded by the branch opening.

---

# 6. Final Finite-Mode Candidate

Selected:

$$
m=3.2275.
$$

Norm of mode coefficients:

$$
\|a\|_2=0.1291.
$$

Five geometric parameters:

$$
w=0.336103949585649,
$$

$$
\beta=1.405423162911031,
$$

$$
\delta=0.051972968077193,
$$

$$
c=0.580209552730338,
$$

$$
\varepsilon=0.036983383487425.
$$

Mode coefficients:

| Mode | Coefficient |
|---|---:|
| `translation_like_P1` | 0.000636097040 |
| `width_split_P2` | 0.017635433568 |
| `skew_P3` | 0.004755842499 |
| `shoulder_P4` | -0.075223543043 |
| `tail_skew_P5` | 0.010666503454 |
| `triple_peak_P6` | 0.057547527233 |
| `wave_P7` | -0.019001897724 |
| `wave_P8` | -0.082991765217 |

---

# 7. Multi-Resolution Re-verification

| Curve Integration Points | Global Scale | Fifth Branch Residual | Relative to Round 13 |
|---:|---:|---:|---:|
| 6001 | 0.998914480716964 | 3.005e-09 | 1.374e-07 |
| 12001 | 0.998914480716965 | 3.005e-09 | 1.374e-07 |
| 24001 | 0.998914480716971 | 3.005e-09 | 1.374e-07 |
| 48001 | 0.998914480716966 | 3.005e-09 | 1.374e-07 |
| 96001 | 0.998914480716946 | 3.005e-09 | 1.374e-07 |

Highest resolution result:

$$
\boxed{
s_{15}=0.998914480716946
}
$$

Relative to Round 13:

$$
\boxed{
s_{15}-s_{13}=1.374194610326e-07
}
$$

The new intermediate branch remains higher than the global value:

$$
\boxed{
3.004601123457e-09.
}
$$

---

# 8. Full Phase Results

Using:

$$
96001
$$

curve integration points and:

$$
262144
$$

phase points.

Number of contact switches:

$$
18.
$$

Number of local minima:

$$
9.
$$

| Rank | Phase | Scale | Above Global | Signature |
|---:|---:|---:|---:|---|
| 1 | 2.094395102393 | 0.998914480716946 | 0.000e+00 | `120deg` |
| 2 | 4.712388980385 | 0.998914480716949 | 2.776e-15 | `p3|p3|p1` |
| 3 | 0.155043705238 | 0.998914481120860 | 4.039e-10 | `L|p0|p2` |
| 4 | 0.123610811813 | 0.998914481739265 | 1.022e-09 | `L|p0|p2` |
| 5 | 0.138424648493 | 0.998914483721547 | 3.005e-09 | `L|p0|p2` |
| 6 | 1.736148508754 | 1.029348172727573 | 3.043e-02 | `p2|L|p3` |
| 7 | 5.235987755983 | 1.081427088911538 | 8.251e-02 | `p0|p3|p1` |
| 8 | 3.028192453799 | 1.099806229894018 | 1.009e-01 | `p3|p1|p0` |
| 9 | 3.778900491653 | 1.127584185185207 | 1.287e-01 | `p3|p2|L` |

The global minimum is controlled by:

$$
\phi=\frac{2\pi}{3}
$$

and:

$$
\phi=\frac{3\pi}{2}
$$

at almost equal heights within display precision.

---

# 9. Structural Results of This Round

Round 15 yields two layers of results.

## 9.1 Finite-Mode Ascent

The unimodal tanh curvature layer from Round 13 is not a local maximum in the eight-mode space.

## 9.2 Branch Opening Barrier

The ascent cannot extend indefinitely. Curvature density deformation generates a new local minimum between two existing low-phase branches, which eventually takes over the global objective.

Therefore, the new working proposition is:

$$
\boxed{
\text{Curvature function optimization is governed by branch generation,
not just by Hessian negative definiteness.}
}
$$

---

# 10. Limitations

1. Only eight CDF–Legendre modes are studied;
2. The candidate is searched along a specific Newton direction;
3. The five-parameter geometric re-isocontouring uses floating-point SLSQP;
4. The full phase audit is a high-density numerical audit;
5. The fifth branch residual is only about $3\times10^{-9}$;
6. A five-branch event-KKT has not yet been established;
7. Interval or Arb certificates have not yet been performed;
8. No new Moser area upper and lower bounds are proposed.

---

# 11. Directions for Round 16

The next round will no longer use the four-branch KKT, but will establish a five-branch system:

$$
m_1=m_2=m_3=m_4=m_5=s.
$$

The fifth branch is located at:

$$
\phi_5\approx0.13842465.
$$

Research content:

1. Incorporate the Newton multiplier or equivalent mode coordinates into the unknowns;
2. Add $\partial_\phi m_5=0$ for the fifth branch;
3. Recalculate the five-branch pressure;
4. Establish the extended Jacobian;
5. Perform a high-precision difference envelope for $s_{15}-s_{13}$;
6. Perform dedicated interval verification for the fifth branch residual of about $3\times10^{-9}$.

---

# 12. Conclusion

Round 15 candidate:

$$
\boxed{
s_{15}=0.998914480716946
}
$$

Improvement relative to Round 13:

$$
\boxed{
1.374194610326e-07.
}
$$

Simultaneously confirming:

$$
\boxed{
\text{The fixed four-branch Hessian is insufficient;
curvature function directions will generate new active branches.}
}
$$

The most accurate description at present is:

> An eight-mode finite curvature candidate that has passed the full phase numerical audit, located within a narrow ascent window before the fifth branch takes over.