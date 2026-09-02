# Separation of Spectral Novelty and Spatial Exposure Novelty

## 1. Centerline Clearance Gap

For the optimal placement \(g\), define the signed clearance of the centerline:

\[
d_C(s;g)
=
\begin{cases}
\operatorname{dist}(g\gamma(s),\partial C),
&
g\gamma(s)\in C,\\
-\operatorname{dist}(g\gamma(s),C),
&
g\gamma(s)\notin C.
\end{cases}
\]

Define the normal thickness gap:

\[
\boxed{
v_C(s;g)
=
[\rho-d_C(s;g)]_+.
}
\]

If:

\[
v_C(s;g)=0
\]

holds for all \(s\), then the centerline has a pointwise clearance of at least \(\rho\).

## 2. Gap Distribution Entropy

Divide the arc length into \(B\) bins, and let the gap mass of the \(j\)-th bin be:

\[
m_j
=
\int_{I_j}v_C(s;g)ds.
\]

Normalize:

\[
p_j=\frac{m_j}{\sum_km_k}.
\]

Define:

\[
H_{\mathrm{gap}}
=
-\sum_jp_j\log p_j,
\]

and the effective number of gap bins:

\[
N_{\mathrm{gap}}^{\mathrm{eff}}
=
e^{H_{\mathrm{gap}}}.
\]

This is not the area exposure tension itself, but describes how dispersed the exposure is distributed along the centerline.

## 3. Round 6 and Round 7

Round 6 attack:

- Exposed connected components: 4;
- Maximum component proportion:
  \[
  72.4864%;
  \]
- Positive gap arc length ratio:
  \[
  42.6287%;
  \]
- Effective number of gap bins:
  \[
  12.055281.
  \]

Round 7 attack:

- Exposed connected components: 4;
- Maximum component proportion:
  \[
  36.9234%;
  \]
- Positive gap arc length ratio:
  \[
  55.3149%;
  \]
- Effective number of gap bins:
  \[
  17.906819.
  \]

Therefore, the exposed area in Round 7 is more evenly dispersed across multiple lobes and covers a longer section of the centerline.

## 4. Spectral Complexity Decreases Instead

The effective spectral modes of the curvature in Round 6 is approximately:

\[
6.130555.
\]

In Round 7, it is approximately:

\[
4.849191.
\]

Round 7 has fewer effective spectral modes and a lower proportion of high-frequency energy, but the spatial gaps are more dispersed.

Therefore:

\[
\boxed{
\text{Spectral Complexity}
\not\Rightarrow
\text{Spatial Attack Dispersion}.
}
\]

What truly determines the pressure on the non-convex container is the spatial gap formed by the combined effects of curvature phase, rigid placement, and container concavities.

## 5. The Next Residual Attack Switches Modes Again

Fourier-16 residual candidate:

- Maximum exposed component proportion:
  \[
  84.0244%;
  \]
- Effective number of gap bins:
  \[
  5.996579;
  \]
- Maximum clearance gap:
  \[
  0.073573670039.
  \]

It is not of the dispersed lobe type, but is dominated by a single deep gap.

The current three cycles reveal two attack modes:

### Dispersed Coverage Type

- The areas of exposed components are relatively even;
- The affected arc length is longer;
- The effective number of gap bins is larger.

### Local Penetration Type

- The maximum component proportion is high;
- The gaps are deeper;
- The exposure is concentrated in a shorter arc segment.

This is merely an adversarial pattern observed in a limited sample and cannot yet be elevated to a general theorem.

## 6. Tentative Conjecture

**Alternating Exposure Modes Conjecture:**

In the alternating adversarial process between the curve and the non-convex container, if the container expands and rearranges in response to a dispersed coverage attack, the next effective attack may shift to a local penetration type; and vice versa.

The reason may be that the container's patching of a certain gap distribution leaves new vulnerabilities at a different spatial scale.