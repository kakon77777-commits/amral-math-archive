# NS × X Integral × 24/72 Paradigm Practice
## Round 18 — Pure Continuous Weighted Strain–Vorticity Return / Obstruction-Confluence Route

- Date: 2026-08-16
- Version: v0.1
- Status: Proof-Route Experiment / Continuous-Only Weighted Relational Return Branch
- canonical source：UTF-8 Markdown
- canonical math delimiters：inline `$...$`；display `$$...$$`
- Previous round: `NS_X72_Round17_PureContinuous_LevelSurface_HodgeCoherence_v0.1_2026-08-16.md`
- This round's objective: Precisely decompose the critical weighted physical-gradient carrier from Round 17
  $$
  E_M
  $$
  back into strain, vorticity, optimal quotient direction, and directional mismatch, and verify whether this long-distance quotient/Hodge route reconverges to the vortex-stretching / middle-strain obstruction of Round 03.
- Non-claims: This round does not prove that the middle-eigenvalue obstruction can necessarily be eliminated; the main result of this round is the establishment of an exact carrier decomposition and a singularity-obstruction confluence chain.

---

# 0. Round 17 handoff

Let:

$$
Q(t)
=
\mathfrak Q_3[u(t)],
$$

and let the optimal representative be:

$$
v
=
u+\nabla q,
$$

$$
r
=
|v|,
$$

$$
n
=
\frac v{|v|}
$$

for:

$$
r>0.
$$

Round 17 defines the physical weighted-gradient carrier:

$$
\boxed{
E_M
=
\int_{\mathbb R^3}
r
\left[
|\nabla u|^2
+
|(\nabla u)^\top n|^2
\right]dx.
}
\tag{0.1}
$$

and proves:

$$
\boxed{
\frac d{dt}Q^2
\le
C E_M.
}
\tag{0.2}
$$

Therefore:

$$
\boxed{
\int_0^{T_\ast}
E_M(t)dt
<
\infty
}
\tag{0.3}
$$

is sufficient to keep:

$$
Q(t)
$$

bounded.

Round 17 STOP:

$$
\boxed{
\text{STOP-C21}
=
\text{Level Hodge-Coherence / Critical Weighted-Gradient Gap}.
}
$$

---

# 1. Velocity-gradient decomposition

Let:

$$
A
=
\nabla u
=
S+\Omega,
$$

where:

$$
S^\top=S,
$$

$$
\Omega^\top=-\Omega.
$$

In three dimensions:

$$
\boxed{
\Omega n
=
\frac12
\omega\times n.
}
\tag{1.1}
$$

and:

$$
\boxed{
|\Omega|^2
=
\frac12|\omega|^2.
}
\tag{1.2}
$$

Thus:

$$
\boxed{
|\nabla u|^2
=
|S|^2
+
\frac12|\omega|^2.
}
\tag{1.3}
$$

---

# 2. Directional covector channel

Since:

$$
A^\top
=
S-\Omega,
$$

we have:

$$
\boxed{
A^\top n
=
Sn
-
\frac12
\omega\times n.
}
\tag{2.1}
$$

Therefore, the Round 17 carrier becomes:

$$
\boxed{
E_M
=
\int
r
\left[
|S|^2
+
\frac12|\omega|^2
+
\left|
Sn-\frac12\omega\times n
\right|^2
\right]dx.
}
\tag{2.2}
$$

This is the first core exact identity of this round.

---

# 3. Longitudinal–tangential strain decomposition

Let:

$$
s_n
=
n^\top Sn,
$$

and:

$$
t_n
=
(I-n\otimes n)Sn.
$$

Then:

$$
Sn
=
s_n n+t_n.
$$

And:

$$
\omega\times n
$$

and:

$$
n
$$

are orthogonal.

Thus:

$$
\boxed{
\left|
Sn-\frac12\omega\times n
\right|^2
=
s_n^2
+
\left|
t_n-\frac12\omega\times n
\right|^2.
}
\tag{3.1}
$$

Therefore:

$$
\boxed{
\begin{aligned}
E_M
=
\int
r
\Bigg[
&
|S|^2
+
\frac12|\omega|^2
+
s_n^2
\\
&
+
\left|
t_n-\frac12\omega\times n
\right|^2
\Bigg]dx.
\end{aligned}
}
\tag{3.2}
$$

This decomposes the carrier into four non-negative channels:

1. weighted strain amplitude;
2. weighted vorticity amplitude;
3. normal strain;
4. tangential strain–rotation mismatch.

---

# 4. Base weighted strain–vorticity carrier

Define:

$$
\boxed{
W_{SV}
=
\int
r
\left[
|S|^2
+
\frac12|\omega|^2
\right]dx.
}
\tag{4.1}
$$

From:

$$
|\nabla u|^2
=
|S|^2+\frac12|\omega|^2,
$$

it can also be written as:

$$
\boxed{
W_{SV}
=
\int
r|\nabla u|^2dx.
}
\tag{4.2}
$$

Since the directional term is non-negative:

$$
\boxed{
W_{SV}
\le
E_M.
}
\tag{4.3}
$$

Moreover:

$$
|A^\top n|^2
\le
|A|^2,
$$

Therefore:

$$
\boxed{
E_M
\le
2W_{SV}.
}
\tag{4.4}
$$

Thus:

$$
\boxed{
W_{SV}
\le
E_M
\le
2W_{SV}.
}
\tag{4.5}
$$

Named:

$$
\boxed{
\textbf{Weighted Strain–Vorticity Equivalence}.
}
$$

---

# 5. Consequence — directional alignment is not the whole budget

Even if perfect directional matching is achieved:

$$
\boxed{
s_n=0,
}
$$

and:

$$
\boxed{
t_n
=
\frac12\omega\times n,
}
$$

such that:

$$
A^\top n=0,
$$

we still have:

$$
\boxed{
E_M=W_{SV}.
}
$$

Therefore:

$$
\boxed{
\textbf{
no directional alignment can cancel the positive base weighted strain–vorticity energy.
}
}
$$

This is different from vortex-stretching sign cancellation.

For the Round 17 budget, alignment can only eliminate the additional directional penalty; it cannot eliminate the base carrier.

---

# 6. Gauge representation of the directional term

From:

$$
v
=
u+\nabla q
=
rn,
$$

we have:

$$
(\nabla v)^\top n
=
\nabla r.
$$

Also:

$$
\nabla u
=
\nabla v-\nabla^2q.
$$

Therefore:

$$
\boxed{
(\nabla u)^\top n
=
\nabla r
-
\nabla^2q\,n.
}
\tag{6.1}
$$

Thus:

$$
\boxed{
E_M
=
W_{SV}
+
\int
r
\left|
\nabla r-\nabla^2q\,n
\right|^2dx.
}
\tag{6.2}
$$

Therefore, the directional channel of Round 17 simultaneously has two equivalent interpretations:

$$
\boxed{
\text{strain–vorticity mismatch}
}
$$

and:

$$
\boxed{
\text{amplitude-gradient / gauge-curvature mismatch}.
}
$$

---

# 7. Connection to Round 15 Pythagorean geometry

Round 15 already established:

$$
\boxed{
E_M
=
D+H,
}
\tag{7.1}
$$

where:

$$
D
=
\mathfrak D_3(v),
$$

$$
H
=
\mathcal H_Q.
$$

Combining with (6.2):

$$
\boxed{
D+H
=
W_{SV}
+
C_{\rm dir},
}
\tag{7.2}
$$

where:

$$
\boxed{
C_{\rm dir}
=
\int
r
\left|
\nabla r-\nabla^2q\,n
\right|^2dx.
}
\tag{7.3}
$$

From (4.5):

$$
\boxed{
0
\le
C_{\rm dir}
\le
W_{SV}.
}
\tag{7.4}
$$

Therefore, nonlinear-Hodge distortion, quotient dissipation, and physical strain-vorticity geometry are not three independent worlds.

They satisfy an exact bridge.

---

# 8. Weighted strain and weighted vorticity channels

Define:

$$
\boxed{
W_S
=
\int
r|S|^2dx,
}
\tag{8.1}
$$

and:

$$
\boxed{
W_\omega
=
\frac12
\int
r|\omega|^2dx.
}
\tag{8.2}
$$

Then:

$$
\boxed{
W_{SV}
=
W_S+W_\omega.
}
\tag{8.3}
$$

Thus:

$$
\boxed{
\int_0^{T_\ast}
E_Mdt
=
\infty
}
$$

must be accompanied by at least:

$$
\boxed{
\int_0^{T_\ast}
W_Sdt
=
\infty
}
$$

or:

$$
\boxed{
\int_0^{T_\ast}
W_\omega dt
=
\infty,
}
$$

or both diverging together.

This is a weighted relational dichotomy.

---

# 9. Hölder reduction to the unweighted critical gradient norm

Since:

$$
\|r\|_3
=
Q,
$$

by Hölder's inequality:

$$
W_{SV}
=
\int
r|\nabla u|^2dx
\le
Q
\|\nabla u\|_3^2.
$$

From (4.4):

$$
\boxed{
E_M
\le
2Q
\|\nabla u\|_3^2.
}
\tag{9.1}
$$

Therefore, the Round 17 differential inequality:

$$
(Q^2)'
\le
C E_M
$$

gives:

$$
2QQ'
\le
C
Q
\|\nabla u\|_3^2.
$$

For the non-trivial:

$$
Q>0
$$

branch:

$$
\boxed{
Q'
\le
C
\|\nabla u\|_3^2.
}
\tag{9.2}
$$

Thus:

$$
\boxed{
Q(T)
\le
Q(0)
+
C
\int_0^T
\|\nabla u(t)\|_3^2dt.
}
\tag{9.3}
$$

This is a scale-critical unweighted bridge.

---

# 10. Vorticity reduction

In the whole-space divergence-free setting, Riesz-transform / Biot–Savart boundedness gives:

$$
\boxed{
\|\nabla u\|_3
\le
C
\|\omega\|_3.
}
\tag{10.1}
$$

Therefore:

$$
\boxed{
Q'
\le
C
\|\omega\|_3^2.
}
\tag{10.2}
$$

Then by interpolation:

$$
\|\omega\|_3
\le
\|\omega\|_2^{1/2}
\|\omega\|_6^{1/2},
$$

and Sobolev embedding:

$$
\|\omega\|_6
\le
C
\|\nabla\omega\|_2,
$$

we obtain:

$$
\boxed{
Q'
\le
C
\|\omega\|_2
\|\nabla\omega\|_2.
}
\tag{10.3}
$$

---

# 11. Energy–enstrophy-dissipation bridge

Integrating (10.3):

$$
Q(T)
\le
Q(0)
+
C
\int_0^T
\|\omega\|_2
\|\nabla\omega\|_2dt.
$$

By Cauchy-Schwarz:

$$
\boxed{
Q(T)
\le
Q(0)
+
C
\left(
\int_0^T
\|\omega\|_2^2dt
\right)^{1/2}
\left(
\int_0^T
\|\nabla\omega\|_2^2dt
\right)^{1/2}.
}
\tag{11.1}
$$

The energy inequality:

$$
\frac12
\|u(T)\|_2^2
+
\nu
\int_0^T
\|\nabla u\|_2^2dt
\le
\frac12
\|u_0\|_2^2.
$$

And for a divergence-free whole-space:

$$
\|\nabla u\|_2
=
\|\omega\|_2.
$$

Thus:

$$
\boxed{
\int_0^T
\|\omega\|_2^2dt
\le
\frac{
\|u_0\|_2^2
}{
2\nu
}.
}
\tag{11.2}
$$

Substituting back:

$$
\boxed{
Q(T)
\le
Q(0)
+
C
\frac{
\|u_0\|_2
}{
\sqrt{\nu}
}
\left(
\int_0^T
\|\nabla\omega\|_2^2dt
\right)^{1/2}.
}
\tag{11.3}
$$

The constant absorbs numerical factors.

---

# 12. Enstrophy-dissipation necessity

From (11.3):

If there exists a finite maximal time:

$$
T_\ast<\infty
$$

and:

$$
Q(t)\to\infty
$$

along:

$$
t\uparrow T_\ast,
$$

then there must be:

$$
\boxed{
\int_0^{T_\ast}
\|\nabla\omega(t)\|_2^2dt
=
\infty.
}
\tag{12.1}
$$

Named:

$$
\boxed{
\textbf{Critical Quotient-to-Enstrophy-Dissipation Necessity}.
}
$$

Therefore, the Round 17 weighted-gradient obstruction can be pushed back to a pure strain/vorticity derivative obstruction.

---

# 13. Return to the enstrophy identity

Vorticity enstrophy:

$$
Y
=
\|\omega\|_2^2.
$$

exact equation:

$$
\boxed{
\frac12Y'
+
\nu
\|\nabla\omega\|_2^2
=
N(t),
}
\tag{13.1}
$$

where:

$$
\boxed{
N(t)
=
\int
\omega^\top S\omega\,dx.
}
\tag{13.2}
$$

Integrating:

$$
\boxed{
\int_0^T
N(t)dt
=
\frac12
\left[
Y(T)-Y(0)
\right]
+
\nu
\int_0^T
\|\nabla\omega\|_2^2dt.
}
\tag{13.3}
$$

Therefore, if (12.1) occurs:

$$
\boxed{
\int_0^{T_\ast}
N(t)dt
=
+\infty.
}
\tag{13.4}
$$

That is, a finite-time critical quotient blow-up must be accompanied by infinite cumulative vortex-stretching production.

---

# 14. Return to the strain determinant

For a smooth divergence-free field, we have the global identity:

$$
\boxed{
\int
\omega^\top S\omega\,dx
=
-4
\int
\det S\,dx.
}
\tag{14.1}
$$

Thus:

$$
\boxed{
\int_0^{T_\ast}
\left[
-4
\int
\det S\,dx
\right]dt
=
+\infty.
}
\tag{14.2}
$$

Therefore, the long quotient route of Round 18 has reconverged to the strain-spectrum nonlinear production of Round 03.

---

# 15. Return to the middle eigenvalue channel

Round 03 has proved the pointwise algebraic inequality:

$$
\boxed{
-\det S
\le
\frac12
\lambda_2^+
|S|^2.
}
\tag{15.1}
$$

Thus:

$$
N(t)
=
-4
\int
\det Sdx
\le
2
\int
\lambda_2^+
|S|^2dx.
$$

From (13.4):

$$
\boxed{
\int_0^{T_\ast}
\int
\lambda_2^+
|S|^2
dxdt
=
\infty.
}
\tag{15.2}
$$

Therefore:

$$
\boxed{
\textbf{
critical quotient blow-up forces infinite cumulative activity
in the positive middle-strain channel.
}
}
$$

---

# 16. Obstruction Confluence Chain

Chaining Sections 12–15 together:

$$
\boxed{
\begin{aligned}
Q(t)\to\infty
&\Longrightarrow
\int_0^{T_\ast}
\|\nabla\omega\|_2^2dt
=
\infty
\\
&\Longrightarrow
\int_0^{T_\ast}
\int
\omega^\top S\omega
\,dxdt
=
+\infty
\\
&\Longrightarrow
\int_0^{T_\ast}
\int
(-\det S)
\,dxdt
=
+\infty
\\
&\Longrightarrow
\int_0^{T_\ast}
\int
\lambda_2^+
|S|^2
\,dxdt
=
\infty.
\end{aligned}
}
\tag{16.1}
$$

Named:

$$
\boxed{
\textbf{Pure-Continuous Obstruction Confluence Chain}.
}
$$

This is the most important proof-route result of this round.

---

# 17. Why this confluence matters

Round 03 takes the path of:

$$
\boxed{
\text{strain/vorticity geometry}
}
$$

Rounds 12–17 take the path of:

$$
\boxed{
\text{critical dual}
\to
\text{quotient}
\to
\text{one-form}
\to
p\text{-Hodge}
\to
\text{level surfaces}
}
$$

The two paths reconverge in Round 18 to:

$$
\boxed{
\lambda_2^+
\text{ / vortex stretching}
}
$$

Therefore, currently at least two very different Pure-C proof architectures point to the same geometric obstruction.

This cannot be interpreted as:

$$
\boxed{
\text{the obstruction is proven insurmountable}.
}
$$

But it indicates:

$$
\boxed{
\textbf{
the remaining difficulty is becoming representation-stable
across distinct continuous reformulations.
}
}
\tag{17.1}
$$

This is an important proof-map signal.

---

# 18. A base-floor no-go for directional-only repair

From:

$$
E_M
\ge
W_{SV}
=
\int
r
\left(
|S|^2+\frac12|\omega|^2
\right)dx,
$$

any attempt to solely control:

$$
n
$$

's directional alignment, without controlling the weighted strain/vorticity amplitude, cannot independently make:

$$
E_M
$$

integrable.

Thus:

$$
\boxed{
\textbf{
pure directional optimization is insufficient for the Round 17 budget.
}
}
\tag{18.1}
$$

It must be handled together with the amplitude correlation of:

$$
r
$$

and:

$$
|S|,\ |\omega|.
$$

---

# 19. Critical amplitude–gradient carrier

Define:

$$
\boxed{
\mathfrak A_{SV}
=
\int
r
\left(
|S|^2+\frac12|\omega|^2
\right)dx.
}
\tag{19.1}
$$

Under NS scaling, it transforms as:

$$
\mathfrak A_{SV}
\mapsto
\lambda^2
\mathfrak A_{SV}.
$$

Therefore:

$$
\boxed{
\int
\mathfrak A_{SV}(t)dt
}
\tag{19.2}
$$

is a scale-invariant spacetime budget.

From (4.5):

$$
\boxed{
\int E_Mdt<\infty
\Longleftrightarrow
\int\mathfrak A_{SV}dt<\infty
}
\tag{19.3}
$$

up to universal constants.

Therefore, the Round 17 weighted-gradient criterion can be completely rewritten as a weighted strain–vorticity budget criterion.

---

# 20. What ordinary energy still fails to control

Ordinary energy controls:

$$
\int
|\omega|^2
dxdt.
$$

But this round requires:

$$
\int
r|\omega|^2
dxdt
$$

and:

$$
\int
r|S|^2
dxdt.
$$

The extra:

$$
\boxed{
r=|v|
}
$$

is exactly the critical quotient amplitude.

Therefore, the true gap can be described as:

$$
\boxed{
\text{energy-level enstrophy}
\to
\text{critical amplitude-weighted enstrophy}.
}
$$

This is a more relational statement than simply "missing one derivative".

---

# 21. STOP-C22 — Weighted Enstrophy / Vortex-Stretching Return Gap

Define:

$$
\boxed{
\bot_X^{\mathrm{C22}}
=
\left\langle
\begin{array}{l}
\text{layer}
=
\mathrm{weighted\ strain\text{-}vorticity\ return},
\\
\text{critical\ weighted\ carrier}
=
\mathfrak A_{SV},
\\
\text{Round17\ carrier}
=
E_M
\simeq
\mathfrak A_{SV},
\\
\text{directional\ mismatch}
=
\mathrm{nonnegative\ and\ nonessential\ for\ budget\ equivalence},
\\
\text{critical\ quotient\ blowup}
\Rightarrow
\int
\|\nabla\omega\|_2^2
=
\infty,
\\
\text{therefore}
\Rightarrow
\text{infinite cumulative vortex stretching},
\\
\text{therefore}
\Rightarrow
\text{infinite positive middle-strain activity},
\\
\text{missing}
=
\mathrm{unconditional\ suppression\ of\ this\ confluence\ channel},
\\
\text{essential\ discrete\ intrusion}
=
\mathrm{false}.
\end{array}
\right\rangle.
}
$$

Named:

$$
\boxed{
\textbf{STOP-C22:
Weighted Enstrophy / Vortex-Stretching Return Gap}.
}
$$

---

# 22. 24/72 Ledger — Round 18

| Step | object | $B$ | $U$ | $O$ | $L$ | status |
|---|---|---|---|---|---|---|
| C214 | $E_M$ strain-vorticity decomposition | $\mathsf C$ | relational | $\mathsf X$ | $\mathsf F$ | EXACT |
| C215 | longitudinal/tangential split | $\mathsf C$ | geometry | relational | $\mathsf F$ | EXACT |
| C216 | base carrier $W_{SV}$ | $\mathsf C$ | recognition | targeted | $\mathsf F$ | FORM |
| C217 | $W_{SV}\le E_M\le2W_{SV}$ | $\mathsf C$ | comparison | scalar | $\mathsf F$ | PROVED |
| C218 | gauge representation of directional square | $\mathsf C$ | quotient/gauge | relational | $\mathsf F$ | EXACT |
| C219 | Hodge–strain bridge $D+H=W_{SV}+C_{\rm dir}$ | $\mathsf C$ | relational | $\mathsf X$ | $\mathsf F$ | EXACT |
| C220 | $E_M\le2Q\|\nabla u\|_3^2$ | $\mathsf C$ | Hölder | scalar | $\mathsf F$ | PROVED |
| C221 | $Q'\lesssim\|\nabla u\|_3^2$ | $\mathsf C$ | differential | scalar | $\mathsf F$ | PROVED |
| C222 | vorticity interpolation bridge | $\mathsf C$ | Sobolev | scalar | $\mathsf F$ | PROVED |
| C223 | $Q$ blowup $\Rightarrow\int\|\nabla\omega\|_2^2=\infty$ | $\mathsf C$ | necessity | scalar | $\mathsf F$ | PROVED |
| C224 | enstrophy production divergence | $\mathsf C$ | exact identity | relational | $\mathsf F$ | PROVED |
| C225 | determinant return | $\mathsf C$ | strain identity | relational | $\mathsf F$ | PROVED |
| C226 | middle-eigenvalue return | $\mathsf C$ | algebraic geometry | targeted | $\mathsf F$ | PROVED |
| C227 | unconditional suppression of confluence channel | $\mathsf C$ | — | targeted | $\mathsf F$ | OPEN / STOP-C22 |

---

# 23. Continuous-versus-discrete status

This round is a "long-distance return to an old obstruction",

but all connections use:

- continuous weighted integrals;
- continuous quotient representatives;
- continuous strain/vorticity fields;
- continuous Sobolev interpolation;
- continuous spacetime budgets.

There are no:

- dyadic scales;
- atoms;
- packet families;
- profile subsequences;
- discrete mode closure.

Therefore:

$$
\boxed{
T_{\mathsf C\to\mathsf D}
=
\text{NOT YET REACHED}.
}
\tag{23.1}
$$

---

# 24. Pure-C path now forms a loop

The current proof map is no longer just a line.

It begins to form a loop:

$$
\boxed{
\begin{aligned}
\text{Round 03: strain/vorticity}
&\to
\cdots
\\
&\to
\text{Round 14--17: quotient/Hodge/layers}
\\
&\to
\text{Round 18: weighted strain/vorticity}
\\
&\to
\text{Round 03 obstruction core}.
\end{aligned}
}
\tag{24.1}
$$

But this is not circular reasoning.

Because new necessary structures were obtained in between:

- quotient gauge;
- gauge curvature;
- gauge-Hessian distortion;
- continuous dangerous layers;
- Hodge coherence;
- critical weighted-gradient budget.

This is an:

$$
\boxed{
\textbf{obstruction confluence loop}.
}
$$

---

# 25. Next round — Confluence attack

The next round should not open another completely different representation.

Since the two long routes have reconverged,

we will directly attack the confluence core.

Candidate main question:

$$
\boxed{
\textbf{
Can simultaneous largeness of
critical quotient amplitude and middle-strain/vortex-stretching activity
force an additional incompatibility?
}
}
$$

Specifically:

1. Simultaneously retain:
   $$
   Q,
   \quad
   W_{SV},
   \quad
   \lambda_2^+,
   \quad
   N=\int\omega^\top S\omega;
   $$

2. Check whether the optimal quotient gauge
   $$
   \operatorname{div}(|v|v)=0
   $$
   restricts the alignment of:
   $$
   \lambda_2^+
   $$
   in the high-$r$ region;

3. Use continuous superlevels:
   $$
   E_\lambda=\{r>\lambda\}
   $$
   to study the weighted middle-strain activity:
   $$
   \int_{E_\lambda}
   \lambda_2^+
   |S|^2;
   $$

4. Check whether simultaneous concentration of vortex stretching and quotient amplitude forces the payment of the Round 17 level-surface dissipation;

5. This will be the first true:
   $$
   \boxed{
   \text{two-route coupled attack}
   }
   $$
   rather than creating yet another new representation.

---

# 26. External primary-source anchors

1. Evan Miller, *On the interaction of strain and vorticity for solutions of the Navier--Stokes equation*, arXiv:2407.02691.
   - strain–vorticity interaction;
   - global identity
     $$
     \langle S,\omega\otimes\omega\rangle
     =
     -4\int\det S;
     $$
   - nonlinear depletion analysis.

2. Alexis Vasseur, *Regularity criterion for 3D Navier-Stokes equations in terms of the direction of the velocity*, arXiv:0705.2446.
   - direction geometry and regularity criterion;
   - the optimal quotient direction $n$ in this round is not directly equivalent to $u/|u|$, but serves only as an external geometric-context anchor.

3. Hui Chen, Daoyuan Fang, Ting Zhang, *Critical regularity criteria for Navier-Stokes equations in terms of one directional derivative of the velocity*, arXiv:2007.10888.
   - critical gradient regularity criteria background;
   - the $\int\|\nabla u\|_3^2dt$ bridge in this round is only compared with it methodologically.

The $E_M$ decomposition, weighted carrier equivalence, quotient-to-enstrophy-dissipation chain, and obstruction-confluence chain in this round are all directly derived in this document.

---

# 27. Commit state

$$
\boxed{
\begin{aligned}
\text{Route}
&=
\mathrm{Pure\ Continuous\ Weighted\ Strain\text{-}Vorticity\ Return},
\\
\text{Essential }\mathsf C\to\mathsf D
&=
\mathrm{Not\ reached},
\\
\text{Round17 carrier}
&=
E_M,
\\
\text{Equivalent base carrier}
&=
W_{SV},
\\
\text{Directional mismatch}
&=
\mathrm{nonnegative},
\\
\text{Critical quotient blowup}
&\Rightarrow
\mathrm{enstrophy\text{-}dissipation\ divergence},
\\
&\Rightarrow
\mathrm{vortex\text{-}stretching\ divergence},
\\
&\Rightarrow
\mathrm{middle\text{-}strain\ activity\ divergence},
\\
\text{Proof-map structure}
&=
\mathrm{obstruction\ confluence\ loop},
\\
\text{STOP-C22}
&=
\mathrm{Weighted\ Enstrophy/Vortex\text{-}Stretching\ Return\ Gap},
\\
\text{Next}
&=
\mathrm{Coupled\ Confluence\ Attack}.
\end{aligned}
}
$$