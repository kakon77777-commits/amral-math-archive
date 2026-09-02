# Round 2 Chirality Correction Report

## 1. Source of Conflict

The 2026 Wetzel triangle paper uses the "congruent copy" convention, explicitly allowing reflection in its normalization and canonical placement. The previous exact tri-normal search only allowed rotation and translation, thus studying the orientation-preserving version:

$$
s_+(\gamma).
$$

For the mirror curve, define:

$$
s_-(\gamma)=s_+(\operatorname{mirror}\gamma).
$$

The true difficulty under the paper's convention is:

$$
\boxed{
s_{\mathrm{cong}}(\gamma)=\min\{s_+(\gamma),s_-(\gamma)\}.
}
$$

Because as long as either chirality can be fitted, the curve is congruently covered.

---

## 2. Chirality Skewness

Definition:

$$
\chi(\gamma)=|s_+(\gamma)-s_-(\gamma)|.
$$

A large $\chi$ indicates that the curve primarily constrains a single chirality; it can be difficult in the orientation-preserving version, yet not a difficult curve for congruent covering.

---

## 3. False Alarm Candidate

The orientation-preserving scale of the previous candidate:

$$
s_+=1.007315039573.
$$

Its mirror scale:

$$
s_-=0.952938974740.
$$

Therefore:

$$
s_{\mathrm{cong}}=0.952938974740,
$$

$$
\chi=0.054376064833.
$$

Thus, $s_+>1$ does not refute the Wetzel covering result; the mirror branch can still be fitted.

---

## 4. Corrected 3-Link Search

The outer objective is changed to:

$$
\max_\gamma\min\{s_+(\gamma),s_-(\gamma)\}.
$$

Equilateral U baseline:

$$
s_{\mathrm{cong}}(U)=0.957829839129.
$$

The 3-link obtained from the corrected search:

$$
s_{\mathrm{cong}}=0.998573794671,
$$

The two branches are respectively:

$$
s_+=0.998574374711,
\qquad
s_-=0.998573794671.
$$

Chirality skewness:

$$
\chi=0.000000580040.
$$

Parameters:

$$
(l_1,l_2,l_3)=(0.3334533250,0.3330911892,0.3334554858),
$$

$$
(\alpha_1,\alpha_3)=(82.34045114^\circ,82.33859136^\circ).
$$

Increase in congruent difficulty relative to the equilateral U:

$$
\Delta s=4.074395554279e-02.
$$

Distance to the certified scale $1$:

$$
1-s_{\mathrm{cong}}=1.426205328654e-03.
$$

---

## 5. Theoretical Branches Must Be Permanently Separated

Subsequent ledgers will simultaneously preserve:

### Orientation-Preserving Version

$$
E_C^{SE(2)}(\gamma).
$$

### Congruent Version Allowing Reflection

$$
E_C^{E(2)}(\gamma)
=
\min\left\{
E_C^{SE(2)}(\gamma),
E_C^{SE(2)}(\operatorname{mirror}\gamma)
\right\}.
$$

If studying the original problem using rotation and translation, use the former; if comparing against the 2026 Wetzel paper, use the latter. The two must no longer be conflated.

---

## 6. Next Round of Corrections

The scoring of the contact ledger reverse generator must incorporate:

1. The minimum of the two chirality branches;
2. Chirality skewness penalty;
3. Contact pressure entropy;
4. Contact signature difference between the two chirality branches;
5. Symmetric and near-symmetric curve families;
6. 4- to 8-links and curvature arcs.

This conflict is preserved as a failure-correction ledger and will not be deleted.