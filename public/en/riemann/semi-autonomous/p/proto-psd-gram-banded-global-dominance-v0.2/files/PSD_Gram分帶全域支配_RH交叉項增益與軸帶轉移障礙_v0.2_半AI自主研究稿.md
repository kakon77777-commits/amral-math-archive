# PSD Gram Banded Global Domination: RH Cross-Term Gain and Axis-Band Transfer Obstruction

版本：v0.2  
日期：2026-07-24  
研究型態：Semi-AI Autonomous Mathematical Research  
技術研究主導與本輪判斷：OpenAI Codex (AI Research Collaborator)  
研究場域、授權與審閱脈絡：Neo.K / EveMissLab

## Abstract

The previous node established an $18$-cell adaptive rational rectangle family covering

$$
\Omega=[20,20.5]\times[-0.2,-0.1]
$$

and generated $72$ admissible rank-one test function rays without using any known zeta zero ordinates as fitting data. The main phenomenon observed then was: the first stage of the diagonal non-negative cone almost always selected a single extreme ray, and multiple test functions provided only limited help in guard shaping. Therefore, this round executes the upgrade scheduled in the previous node: retaining the banding and covering, but replacing the diagonal ray cone of

$$
A=\sum_{k=1}^{72}\lambda_kv_kv_k^{\mathsf T},
\qquad \lambda_k\ge0
$$

with the PSD Gram variable in the $22$-dimensional restricted coordinate space

$$
A\succeq0.
$$

This round yields three clear but distinct conclusions.

First, cross-terms have a real effect. Compared to the $72$-ray diagonal baseline, the full-Gram solution reduces the zero-location-independent sample budget of "axis-band supremum times counting upper bound, plus tail term" by $10.89\%$ to $28.66\%$, with an average reduction of $21.08\%$; the holdout mass of the first $50$ known zeros for all $18$ cells also decreased. The full-Gram principal direction and the nearest old ray still differ by $29.22^\circ$ to $70.15^\circ$ under the $C_0$ whitening metric. This indicates that the improvement is not a minor reweighting within the original candidate pool, but a phase shaping formed by new linear combinations.

Second, the improvement is not caused by high-rank mixing. Requesting ranks $1, 2, 4, 8$ for four representative cells respectively, all outputs numerically collapse to rank one; the difference in objective values across the four runs for the same cell does not exceed $2.0\times10^{-9}$. Thus, the mechanism observed so far is "a new rank-one direction in the full space", not "multi-modal PSD mixing".

Third, and crucial for determining the next step: this improvement is far from sufficient to approach the global budget. The full-Gram sample budget still falls between $64.60$ and $142.73$, whereas the target is less than $1$; after adding the continuous axis-band correction of floating-point gradients and second-order envelopes, it falls further between $89.77$ and $354.16$. Among the five axis bands, $[18,23]$ is the largest source of cost for all $18$ cells, accounting for an average of $61.73\%$ of the sample objective. Therefore, this round does not recommend directionlessly increasing the rank, number of rays, or grid density anymore, but rather shifting to the dual problem: proving or disproving "how much positive mass a unit negative direction in the target region necessarily forces onto $[18,23]$".

This manuscript is neither a proof of the RH nor a global zero-side certificate. The execution environment lacks a convex SDP solver; this round uses

$$
A=LL^{\mathsf T}
$$

combined with multi-start SLSQP, thus only guaranteeing the constructive form of PSD, without claiming to find the global optimum of the convex SDP. All continuous envelopes, zero-counting profiles, and tail bounds remain E2 floating-point research objects.

## I. Refinement of the Research Problem

### 1.1 From "Multiple Test Functions" to "Gram Geometry"

Let $\psi$ be a real even function supported on $[-R,R]$, fixing $R=3$ here, and let

$$
G(z)=\int_{-R}^{R}\psi(t)e^{izt}\,dt.
$$

The previous node used non-negative combinations of multiple established candidates $\psi_k$. If the candidates are represented by restricted coordinate vectors $v_k$, the diagonal cone only allows

$$
A\in\mathcal C_{\mathrm{diag}}
=\left\{
\sum_k\lambda_kv_kv_k^{\mathsf T}:\lambda_k\ge0
\right\}.
$$

Although this set contains combinations of multiple test functions, it does not allow cross-terms between any two coordinate directions. This round switches to

$$
\mathcal C_{\mathrm{Gram}}=\mathbb S_+^{22},
$$

thus, in terms of representational capacity, we have

$$
\mathcal C_{\mathrm{diag}}\subseteq\mathcal C_{\mathrm{Gram}}.
$$

This inclusion relation is an algebraic fact; however, since this round performs non-convex search using fixed-rank factorization, the numerical output cannot be interpreted as the optimal solution of the full convex cone.

### 1.2 Structural Constraints and Data Isolation

The original discrete model has $24$ real even compactly supported polynomial bumps. Only two structural zeros are imposed:

$$
G(0)=0,
\qquad
G(i/2)=0.
$$

After $C_0$ whitening, $22$-dimensional coordinates are obtained. These two conditions are not zeta non-trivial zero data. The ordinates of the first $50$ known non-trivial zeros are only used to calculate the holdout after optimization is complete:

$$
H_{50}(A)=\sum_{m=1}^{50}H_A(\gamma_m).
$$

They do not enter into candidate generation, objective functions, constraints, cutting-plane exchanges, or rank selection.

## II. PSD Block and Real-Axis Positivity

Let $g(z)\in\mathbb C^{22}$ be the Fourier transform row of the restricted basis at $z$, and take

$$
A=LL^{\mathsf T}\succeq0.
$$

If the column vectors of $L$ are $\ell_r$, define

$$
\Phi_r(z)=g(z)^{\mathsf T}\ell_r.
$$

The off-axis block used in this round is

$$
B_A(z)
=2\operatorname{Re}\!\left(g(z)^{\mathsf T}Ag(z)\right)
=2\sum_r\operatorname{Re}\!\left(\Phi_r(z)^2\right).
$$

On the real axis, the real even structure implies $\Phi_r(x)\in\mathbb R$, hence

$$
H_A(x)
=g(x)^{\mathsf T}Ag(x)
=\sum_r|\Phi_r(x)|^2
\ge0.
$$

This is exactly the dual nature of the PSD Gram form: on the off-axis, the phase of the squares can be used to make the real part negative; returning to the real axis, it forms a non-negligible non-negative mass.

Each target cell $P$ requires

$$
B_A(z)\le-1,
\qquad z\in P.
$$

Once this unit scale is fixed, the real-axis cost can no longer be eliminated by global scaling.

## III. Zero-Location-Independent Banded Objectives

### 3.1 Five Axis Bands

This round does not put known zeros point-by-point into the objective, but divides $[14,145]$ into:

| Band | Interval | Floating-Point Counting Upper Bound Profile |
|---|---:|---:|
| $A_0$ | $[14,18]$ | $6.6657984212$ |
| $A_1$ | $[18,23]$ | $7.1139985988$ |
| $A_2$ | $[23,35]$ | $9.2128459607$ |
| $A_3$ | $[35,70]$ | $18.2316247098$ |
| $A_4$ | $[70,145]$ | $40.4069834843$ |

For each band $I_j$, use $u_j$ to control

$$
H_A(x)\le u_j,
\qquad x\in I_j.
$$

The sample-based zero-location-independent budget is

$$
\mathcal M_{\mathrm{samp}}(A)
=\langle T,A\rangle
+\sum_{j=0}^{4}\widehat N_j
\max_{x\in\mathcal G_j}H_A(x),
$$

where $\mathcal G_j$ is a dense grid with a step size of $0.05$ within the band, and $\langle T,A\rangle$ is the tail term prototype above $145$.

### 3.2 Tail Term

From the prototype estimate using integration by parts twice,

$$
|G(\gamma)|
\le
\frac{\int_{-R}^{R}|\psi''(t)|\,dt}{\gamma^2}.
$$

Then, using Cauchy–Schwarz to convert the $L^1$ second derivative into an $L^2$-type quadratic form, and multiplying by the floating-point zero density profile, it can be written as

$$
\mathcal T(A)=\langle T,A\rangle.
$$

Here, $T$ is a reproducible floating-point matrix, not a formal certificate with completed interval encapsulation.

### 3.3 Two-Stage Optimization

The first stage minimizes

$$
\mathcal M_{\mathrm{samp}}(A)
$$

and requires core negativity and an arithmetic baseline

$$
\langle Q_{\mathrm{arith}},A\rangle\ge10^{-3}.
$$

The second stage minimizes the positive upper bound of the guard under

$$
\mathcal M_{\mathrm{samp}}(A)
\le1.05\,\mathcal M_{\mathrm{stage\,1}}.
$$

The core initially uses a $9\times7$ grid, and the axis bands initially use a step size of $0.5$; each round finds the worst point on a $161\times121$ dense core grid and a dense axis-band grid with a step size of $0.05$, and adds the worst point of each violating axis band to the active set.

## IV. Continuity Audit

### 4.1 Why Reporting Only Dense Grids is Insufficient

Simply claiming

$$
\max_{z\in\mathcal G_P}B_A(z)<0
$$

cannot rule out positive spikes between grid points. The initial global $L^1$ first-derivative upper bound was overly loose, incorrectly labeling $8$ out of the $18$ cells as "unconfirmable". This was not because positive values actually appeared in the dense core grid, but because the estimator was too coarse.

### 4.2 Gradient Plus Second-Order Envelope

This round retains the coarse estimate for auditing, while adding actual grid gradients. If the core grid spacings are $\Delta x,\Delta y$, first compute

$$
\partial_x B_A(z)
=4\operatorname{Re}\sum_r\Phi_r(z)\Phi_r'(z),
$$

$$
\partial_y B_A(z)
=4\operatorname{Re}\sum_r\Phi_r(z)i\Phi_r'(z).
$$

Then, establish a Hessian floating-point envelope using the support radius, $\|\psi\|_1$, $\|t\psi\|_1$, and $\|t^2\psi\|_1$, extending the maximum grid gradient to the entire cell. The final core upper bound is

$$
U_P
=\max_{\mathcal G_P}B_A
+\frac{\Delta x}{2}\widehat L_x
+\frac{\Delta y}{2}\widehat L_y.
$$

The result is that all $18$ cells pass, and

$$
-0.9923\le U_P\le-0.9606.
$$

Similarly, the real axis bands use the sample maximum of $H_A'$ plus the $H_A''$ envelope, yielding

$$
u_j^{\mathrm{corr}}
=u_j^{\mathrm{samp}}
+\frac{h_j}{2}
\left(
\max_{\mathcal G_j}|H_A'|
+\frac{h_j}{2}\widehat M_{2,A}
\right).
$$

This correction is large in some high-$x$ cells, indicating that the second-order envelope is still conservative; however, even without this correction at all, the sample budget is still at least $64.60$ times away from $1$, so it will not change the directional judgment of this round.

## V. Numerical Results

### 5.1 All 18 Cells

In the table below, "Diagonal" refers to the $72$-ray LP, "Gram" refers to the full $22$-dimensional factorized PSD search; "Corrected" is the budget after adding the continuous axis-band envelope; $A_1$ is the sample cost of the $[18,23]$ band.

| Cell | Diagonal Sample Budget | Gram Sample Budget | Reduction | Corrected Budget | $A_1$ Cost | Holdout | Guard |
|---|---:|---:|---:|---:|---:|---:|---:|
| `X0_Y0` | $79.253$ | $67.833$ | $14.41\%$ | $89.771$ | $43.383$ | $4.719$ | $0.000$ |
| `X1_Y0` | $81.587$ | $64.604$ | $20.82\%$ | $117.455$ | $39.542$ | $5.194$ | $0.000$ |
| `X2_Y0` | $88.359$ | $65.415$ | $25.97\%$ | $174.361$ | $38.439$ | $5.506$ | $0.000$ |
| `X0_Y1` | $160.168$ | $142.731$ | $10.89\%$ | $184.840$ | $94.699$ | $10.666$ | $0.198$ |
| `X1_Y1` | $169.096$ | $137.791$ | $18.51\%$ | $207.393$ | $90.156$ | $12.341$ | $0.213$ |
| `X2_Y1` | $186.421$ | $140.140$ | $24.83\%$ | $266.293$ | $89.697$ | $12.625$ | $0.213$ |
| `x0_Y2` | $108.648$ | $90.564$ | $16.65\%$ | $118.136$ | $57.893$ | $5.767$ | $0.000$ |
| `x1_Y2` | $102.932$ | $87.343$ | $15.15\%$ | $116.940$ | $55.339$ | $6.386$ | $0.000$ |
| `x2_Y2` | $105.775$ | $84.452$ | $20.16\%$ | $134.969$ | $52.227$ | $6.736$ | $0.000$ |
| `x3_Y2` | $109.426$ | $82.850$ | $24.29\%$ | $170.430$ | $49.349$ | $6.764$ | $0.000$ |
| `x4_Y2` | $114.605$ | $83.114$ | $27.48\%$ | $228.466$ | $48.118$ | $6.828$ | $0.000$ |
| `x5_Y2` | $120.882$ | $86.232$ | $28.66\%$ | $245.807$ | $50.968$ | $7.246$ | $0.000$ |
| `x0_Y3` | $156.532$ | $130.567$ | $16.59\%$ | $170.308$ | $83.496$ | $8.317$ | $0.000$ |
| `x1_Y3` | $148.288$ | $125.969$ | $15.05\%$ | $168.855$ | $79.829$ | $9.209$ | $0.000$ |
| `x2_Y3` | $152.418$ | $121.867$ | $20.04\%$ | $195.279$ | $75.371$ | $9.719$ | $0.000$ |
| `x3_Y3` | $157.687$ | $119.618$ | $24.14\%$ | $246.362$ | $71.253$ | $9.763$ | $0.000$ |
| `x4_Y3` | $165.027$ | $120.021$ | $27.27\%$ | $328.030$ | $69.508$ | $9.867$ | $0.000$ |
| `x5_Y3` | $174.067$ | $124.453$ | $28.50\%$ | $354.164$ | $73.570$ | $10.459$ | $0.000$ |

The overall statistics are

$$
\operatorname{mean}
\left(
\frac{\mathcal M_{\mathrm{diag}}-\mathcal M_{\mathrm{Gram}}}
{\mathcal M_{\mathrm{diag}}}
\right)
=0.2107757.
$$

The minimum and maximum improvements are respectively

$$
0.1088656
\quad\text{and}\quad
0.2866441.
$$

### 5.2 New Directions are Not Minor Tweaks of Old Rays

For each rank-one Gram solution, take its principal direction $u_P$, and compare it with the $72$ whitened candidate directions

$$
\theta_P
=\min_k\arccos
\frac{|\langle u_P,v_k\rangle|}
{\|u_P\|\,\|v_k\|}.
$$

yielding

$$
29.22^\circ
\le\theta_P\le
70.15^\circ,
$$

averaging approximately

$$
53.92^\circ.
$$

Therefore, the improvement of the full Gram indeed comes from new directions outside the candidate dictionary.

### 5.3 Rank Sweep

| Cell | Rank $1$ | Rank $2$ | Rank $4$ | Rank $8$ | Output Numerical Rank |
|---|---:|---:|---:|---:|---:|
| `X1_Y0` | $64.6038463421$ | $64.6038463420$ | $64.6038463422$ | $64.6038463424$ | $1$ |
| `X1_Y1` | $137.7908257036$ | $137.7908257022$ | $137.7908257027$ | $137.7908257017$ | $1$ |
| `x2_Y2` | $84.4520409177$ | $84.4520409182$ | $84.4520409179$ | $84.4520409177$ | $1$ |
| `x2_Y3` | $121.8674577314$ | $121.8674577313$ | $121.8674577310$ | $121.8674577312$ | $1$ |

This does not prove that the optimal solution of the convex SDP must be rank one, but it negates the most direct explanation that "the current rank is simply insufficient".

### 5.4 Axis-Band Cost Decomposition

| Axis Band | Sample Cost Range | Average Cost | Average Objective Proportion | Number of Cells as Maximum Band |
|---|---:|---:|---:|---:|
| $[14,18]$ | $1.733$–$7.092$ | $4.001$ | $3.98\%$ | $0$ |
| $[18,23]$ | $38.439$–$94.699$ | $64.602$ | $61.73\%$ | $18$ |
| $[23,35]$ | $11.896$–$28.868$ | $19.573$ | $18.70\%$ | $0$ |
| $[35,70]$ | $0.148$–$1.174$ | $0.487$ | $0.49\%$ | $0$ |
| $[70,145]$ | $0.0147$–$0.0353$ | $0.024$ | $0.02\%$ | $0$ |

The tail term accounts for an average of $15.09\%$. This decomposition converges the problem from a vague "global leakage is too large" to a local analytic problem: how much unavoidable positive mass is left in the real-axis neighborhood directly below when creating a negative squared real part in the off-axis region at $\operatorname{Re}z\approx20$?

## VI. Partial Budget and Unclosed Logic

The partial margin reported in this round is

$$
\Delta_{\mathrm{partial}}
=1-\mathcal M(A)
-\max\!\left(0,\sup_{\mathrm{guard}}B_A\right).
$$

The sample-based range is

$$
-141.9299
\le
\Delta_{\mathrm{partial}}^{\mathrm{samp}}
\le
-63.6038,
$$

The continuously corrected range is

$$
-353.1636
\le
\Delta_{\mathrm{partial}}^{\mathrm{corr}}
\le
-88.7713.
$$

All are negative. More importantly, these are still not complete zero-side budgets, because they do not include:

1. The signed costs of other unknown off-axis zero bands;
2. The argument-principle or winding certificates that zeros actually exist within the target rectangle;
3. The intervalized arithmetic encapsulation of all terms in the explicit formula;
4. The formal reasoning to elevate local conditions to a full critical strip judgment.

Therefore

$$
\texttt{global\_certificate\_pass}=\mathrm{false}
$$

is not a conservative label, but the correct logical state of this round.

## VII. Answer to the Question from the Previous Node

The previous node asked: After "banding, multiple test functions, and covering certificate families", is it possible for the full PSD Gram to break through via cross-terms?

The answer should be split into two sentences.

The first sentence is affirmative:

$$
\text{Cross-terms provided a stable and reproducible }10.9\%\text{–}28.7\%\text{ improvement.}
$$

The second sentence is negative:

$$
\text{This improvement did not bring the global partial budget to the same order of magnitude.}
$$

Therefore, "banding, multiple test functions, and covering certificate families" is the correct research decomposition, but it is not the final missing degree of freedom. Banding revealed the true bottleneck; the full Gram ruled out the simple explanation that "there are just too few candidate rays".

## VIII. Next Node: Dual Axis-Band—Target Region Transfer Certificate

### 8.1 Why We Should Switch to Dual Now

The current best sample budget is still

$$
64.6038>1.
$$

Under such a scale difference, continuing to increase the rank from $8$ to $16$, expanding the $72$ rays into more local variants, or simply refining the grid further, can at most improve the primal upper bound, but cannot answer "whether this function class is in principle impossible to be less than $1$".

What is truly needed is a verifiable lower bound.

### 8.2 Finite-Dimensional Dual Form

Let

$$
C(z)=2\operatorname{Re}\!\left(g(z)g(z)^{\mathsf T}\right),
\qquad
P(x)=g(x)g(x)^{\mathsf T}.
$$

Then the core constraint and axis mass are respectively

$$
\langle C(z),A\rangle\le-1,
\qquad
\langle P(x),A\rangle=H_A(x).
$$

For each band, select a probability measure $\mu_j$, where

$$
\mu_j\ge0,
\qquad
\mu_j(I_j)=1.
$$

Since the supremum is greater than the average,

$$
\widehat N_j\sup_{x\in I_j}H_A(x)
\ge
\widehat N_j\int_{I_j}H_A(x)\,d\mu_j(x).
$$

Thus any matrix

$$
M_\mu
=T+\sum_j\widehat N_j
\int_{I_j}P(x)\,d\mu_j(x)
$$

gives

$$
\mathcal M(A)\ge\langle M_\mu,A\rangle.
$$

If we take only one core point $z_0$, and can prove that some $\eta>1$ makes

$$
M_\mu+\eta C(z_0)\succeq0,
$$

then for all $A\succeq0$ and

$$
\langle C(z_0),A\rangle\le-1
$$

we have

$$
\mathcal M(A)
\ge\langle M_\mu,A\rangle
\ge-\eta\langle C(z_0),A\rangle
\ge\eta
>1.
$$

This is the required axis-band—target region transfer obstruction. A stronger version can take non-negative multipliers $\eta_q$ for multiple core points:

$$
M_\mu+\sum_q\eta_q C(z_q)\succeq0.
$$

This dual certificate has two advantages:

1. It directly provides a lower bound for the primal optimal value, rather than providing yet another new upper bound candidate;
2. If the weights concentrate on $[18,23]$, it can verify whether the dominant band observed in this round is an algorithmic coincidence or an inevitable cost of analytic continuation.

### 8.3 Success and Stopping Criteria for the Next Node

The next node is tentatively named

`RH_Axis_Target_Transfer_Dual_Obstruction_v0.3`.

The success criteria are divided into two levels:

- E2 Success: Find a stable floating dual lower bound on all $18$ cells, which does not collapse under grid refinement and weight perturbation;
- Elevatable Success: Rationalize or intervalize the matrices, weights, core multipliers, and minimum eigenvalue margins to form a verifiable dual certificate.

The stopping criteria must also be explicit:

- If a dual lower bound greater than $1$ can be obtained for every cell, then the current $R=3$, two structural zeros, $22$-dimensional function class under this banded budget should be considered falsified, and the next step is to change the support or function class;
- If the dual lower bound is consistently and significantly less than $1$, then the primal still has theoretical room, and only then is there a reason to go back and introduce a true convex SDP solver, a more complete rank, or a new dictionary;
- If only the dual weights of $[18,23]$ are sufficient to push up the lower bound, then localize the global problem into an analytic uncertainty principle for that band.

## IX. Credibility and Claim Boundaries

This round can claim:

1. Within the saved floating-point discrete model, the full-Gram candidates are constructively PSD;
2. All $18$ cells pass the floating-point negativity audit of the dense core and gradient plus Hessian;
3. The improvement relative to the diagonal baseline, holdout decrease, rank collapse, and $A_1$ dominance phenomenon can be recomputed from the saved outputs;
4. Switching to the dual lower bound in the next step carries more research information than continuing to directionlessly expand the primal.

This round cannot claim:

1. The global optimal solution of the convex SDP has been found;
2. Exact integration or interval arithmetic has been completed;
3. Strict zero-counting and tail bound certificates have been completed;
4. All unknown off-axis zeros have been handled;
5. It has been proven that the target rectangle contains zeros;
6. A proof of the RH, non-RH, or any RH-equivalent proposition has been obtained.

## X. Conclusion

The most important product of this round is not just another set of better numbers, but the separation of mechanisms:

$$
\text{Old ray constraints}
\quad\longrightarrow\quad
\text{Full-space phase shaping can improve},
$$

but

$$
\text{Insufficient high rank}
\quad\not\approx\quad
\text{Current main bottleneck}.
$$

The true main bottleneck is concentrated in

$$
[18,23]
$$

this real axis band that highly overlaps with the target. When the single-band cost of $[18,23]$ is already much greater than $1$ across all $18$ cells, the next valuable question is no longer "can we find an even better function", but:

$$
\boxed{
\text{How much adjacent real-axis positive mass is actually forced by off-axis unit negativity?}
}
$$

If this transfer amount can be dual-certificated, the research will for the first time obtain a structural criterion that is falsifiable, stoppable, and capable of guiding the modification of the function class.