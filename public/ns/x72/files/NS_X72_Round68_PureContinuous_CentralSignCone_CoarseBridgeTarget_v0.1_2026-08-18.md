# NS × X 積分 × 24/72 範式實戰
## Round 68 — Pure Continuous Central Sign-Cone Reduction / Coarse Final-Bridge Target

- 日期：2026-08-18
- 版本：v0.1
- 狀態：Proof-Route Experiment / Continuous-Only Central-Cone Branch
- 前一輪：Round 67 — Log-Viscosity Riccati Tangent / Scattering Derivative
- canonical math delimiters：inline `$...$`；display `$$...$$`

## 0. 為什麼這輪改攻中央 cone

Round 67 已把最後 viscosity bridge 壓成：

$$
f(\nu)
=
\frac{a_3(\nu)}{\nu},
$$

以及

$$
\Sigma(\nu)
=
f'(\nu).
$$

若能很粗地控制

$$
\int_0^{10^{-6}}|\Sigma|,
$$

即可完成最後 bridge。

Round 68 再往前一步：甚至不必直接認證 tiny 的

$$
u_3=-a_3.
$$

$n=1$ 的 exact recurrence把它連到兩個 $O(1)$ 的鄰近量，而這兩個量的 sign margin大得多。

---

# 1. Central variables

Define：

$$
\boxed{
e_1
:=
u_2,
}
\tag{1.1}
$$

and the odd rescaled variable：

$$
\boxed{
o_2
:=
\frac{u_5}{\nu}.
}
\tag{1.2}
$$

The canonical normalization remains：

$$
u_0=1,
\qquad
u_1=0,
\qquad
u_{-1}=0.
$$

---

# 2. Exact $n=1$ central identity

The real adjoint recurrence is：

$$
-
A_{-2}^{(n)}u_{n-2}
+
A_0^{(n)}u_n
-
\nu b_nu_{n+1}
-
A_2^{(n)}u_{n+2}
+
A_4^{(n)}u_{n+4}
=
0.
$$

At：

$$
n=1,
$$

the $u_{-1}$ and $u_1$ terms vanish。

Thus：

$$
-\nu b_1u_2
-
A_2^{(1)}u_3
+
A_4^{(1)}u_5
=
0.
$$

Since：

$$
u_5=\nu o_2,
$$

we obtain the exact identity：

$$
\boxed{
u_3
=
\nu
\frac{
A_4^{(1)}o_2
-
b_1e_1
}{
A_2^{(1)}
}.
}
\tag{2.1}
$$

命名：

$$
\boxed{
\textbf{Central Sign-Cone Identity}.
}
$$

---

# 3. Large-fibre cone

For：

$$
K_+
=
\sqrt{17}+3,
$$

exact algebra gives：

$$
\boxed{
A_2^{(1)}>0,
}
$$

$$
\boxed{
A_4^{(1)}<0,
}
$$

$$
\boxed{
b_1<0.
}
$$

Therefore if：

$$
\boxed{
e_1<0,
\qquad
o_2>0,
}
\tag{3.1}
$$

then：

$$
A_4^{(1)}o_2<0,
$$

and：

$$
-b_1e_1<0.
$$

Hence the numerator in (2.1) is strictly negative，while the denominator is positive。

Therefore：

$$
\boxed{
e_1<0
\ \wedge\
o_2>0
\Longrightarrow
u_3<0.
}
\tag{3.2}
$$

This cone has no delicate ratio condition at all。

---

# 4. Small-fibre coefficient geometry

For：

$$
K_-
=
\sqrt{17}-3,
$$

the coefficient signs are：

$$
\boxed{
A_2^{(1)}<0,
}
$$

$$
\boxed{
A_4^{(1)}<0,
}
$$

$$
\boxed{
b_1>0.
}
$$

Define：

$$
\boxed{
\Theta_-
=
\frac{
b_1
}{
-A_4^{(1)}
}.
}
\tag{4.1}
$$

Exact algebraic verification gives：

$$
\boxed{
\Theta_-
>
1200.
}
\tag{4.2}
$$

Numerically：

$$
\Theta_-
=
1273.9800455\ldots.
$$

For $u_3<0$，because $A_2^{(1)}<0$，it suffices that the numerator of (2.1) be positive：

$$
b_1(-e_1)
>
(-A_4^{(1)})o_2.
$$

Equivalently：

$$
\boxed{
\frac{o_2}{-e_1}
<
\Theta_-.
}
\tag{4.3}
$$

The threshold is enormous。

---

# 5. Extremely coarse small-fibre sufficient cone

Suppose only：

$$
\boxed{
e_1
\le
-0.1,
}
\tag{5.1}
$$

and：

$$
\boxed{
0
\le
o_2
\le
100.
}
\tag{5.2}
$$

Then：

$$
\frac{o_2}{-e_1}
\le
1000
<
1200
<
\Theta_-.
$$

Therefore：

$$
\boxed{
e_1\le-0.1,
\quad
0\le o_2\le100
\Longrightarrow
u_3<0.
}
\tag{5.3}
$$

This is deliberately absurdly loose。

The final theorem no longer needs to resolve a coefficient of size $10^{-6}$。

It can work with an order-one sign cone。

---

# 6. Rigorous endpoint cone — small fibre

Using the already-certified endpoint even-ratio pullback and odd affine Jost graph，Round 68 independently reconstructs：

$$
\boxed{
e_{1,-}
\in
[
-0.917580335857451,\,
-0.917580335857450
].
}
\tag{6.1}
$$

Also：

$$
\boxed{
o_{2,-}
\in
[
4.164932082753419,\,
4.164932082753420
].
}
\tag{6.2}
$$

Thus the endpoint is not barely inside the sufficient cone。

It is deep inside：

$$
e_1<-0.9,
$$

$$
4<o_2<5.
$$

Relative to the small-fibre threshold：

$$
o_2/(-e_1)
\approx
4.54,
$$

whereas failure requires a ratio exceeding roughly：

$$
1274.
$$

There is a factor of about：

$$
280
$$

in ratio space before the central sign can even become ambiguous。

---

# 7. Rigorous endpoint cone — large fibre

For：

$$
K_+,
$$

the same endpoint certificate gives：

$$
\boxed{
e_{1,+}
\in
[
-0.766873547629417,\,
-0.766873547194107
].
}
\tag{7.1}
$$

and：

$$
\boxed{
o_{2,+}
\in
[
3.718852854835774,\,
3.718852886233795
].
}
\tag{7.2}
$$

Hence：

$$
\boxed{
e_{1,+}<0,
\qquad
o_{2,+}>0
}
$$

with order-one margins。

So the large-fibre central cone is also deeply satisfied at the rigorous endpoint。

---

# 8. A much weaker final derivative theorem is sufficient

Let：

$$
0<\nu\le10^{-6}.
$$

Suppose one proves only the following grotesquely loose uniform derivative bounds：

$$
\boxed{
|e_1'(\nu)|
<
10^5,
}
\tag{8.1}
$$

$$
\boxed{
|o_2'(\nu)|
<
10^6.
}
\tag{8.2}
$$

Then over the entire remaining strip：

$$
|\Delta e_1|
<
0.1,
$$

and：

$$
|\Delta o_2|
<
1.
$$

Starting from the rigorous endpoint intervals：

### small fibre

$$
e_1
<
-0.817
<
-0.1,
$$

and：

$$
3.16
<
o_2
<
5.17
<
100.
$$

Therefore the small sufficient cone remains valid。

### large fibre

$$
e_1
<
-0.666
<
0,
$$

and：

$$
o_2
>
2.71
>
0.
$$

Thus the large sufficient cone remains valid。

Consequently：

$$
\boxed{
\left[
|e_1'|<10^5
\ \wedge\
|o_2'|<10^6
\right]
\Longrightarrow
a_{3,\pm}(\nu)>0
\quad
\forall
0<\nu\le10^{-6}.
}
\tag{8.3}
$$

命名：

$$
\boxed{
\textbf{Coarse Central-Cone Bridge Lemma}.
}
$$

---

# 9. Actual fixed-size tangent sizes

Round 67's Riccati tangent gives：

$$
e_1'(\nu)
=
\frac{
(\partial_{\log\nu}G_1)_{31}
}{
\nu
}
$$

in the present column/index convention。

Also，from the exact central identity：

$$
o_2
=
\frac{
b_1e_1
-
A_2^{(1)}f
}{
A_4^{(1)}
},
$$

where：

$$
f=a_3/\nu.
$$

Therefore：

$$
\boxed{
o_2'
=
\frac{
b_1e_1'
-
A_2^{(1)}\Sigma
}{
A_4^{(1)}
}.
}
\tag{9.1}
$$

The fixed-size diagnostics over：

$$
10^{-8}
\le\nu\le10^{-6}
$$

show：

### small fibre

$$
\boxed{
e_1'
\approx
-1.489,
}
$$

and：

$$
\boxed{
o_2'
\approx
-142.
}
$$

### large fibre

$$
\boxed{
e_1'
\approx
0.993,
}
$$

and：

$$
\boxed{
o_2'
\approx
19.
}
$$

The attached CSV records the full tested values。

---

# 10. Proof margin

Compare actual diagnostic sizes with the sufficient bounds：

$$
|e_1'|
\lesssim
2
\qquad
\text{vs. required }
10^5,
$$

and：

$$
|o_2'|
\lesssim
200
\qquad
\text{vs. required }
10^6.
$$

So the proof tolerances are looser by roughly：

$$
5\times10^4
$$

for $e_1'$，and：

$$
5\times10^3
$$

for $o_2'$。

This central-cone route has an even larger conditioning margin than the Round 67 direct $\Sigma$ bound。

---

# 11. Relation to the scattering-derivative route

Round 67 reduced the last bridge to：

$$
\int_0^{10^{-6}}
|\Sigma|
<
5.33.
$$

Round 68 does not invalidate that route。

Instead it produces a second，potentially easier closure mechanism：

$$
\boxed{
\text{tiny central sign}
\longleftarrow
\text{coarse order-one central cone}.
}
$$

The two approaches share the same fixed-size Riccati tangent data，but the cone route avoids relying on the cancellation：

$$
\partial_{\log\nu}a_3-a_3.
$$

It therefore may be substantially easier to certify with interval tangent bounds。

---

# 12. Why this is not yet the final theorem

The exact cone reductions and endpoint intervals are rigorous。

The derivative values in Section 9 are still diagnostics。

What remains is to validate a deliberately coarse tangent cone such as：

$$
|e_1'|<10^5,
$$

$$
|o_2'|<10^6
$$

uniformly over：

$$
0<\nu<10^{-6}.
$$

Because the actual values are four to five orders of magnitude smaller，the next certificate does not need a precision Riccati tangent enclosure。

It only needs a stable norm/cone estimate in the correct parity-rescaled coordinates。

---

# 13. STOP-C72 — Coarse Central-Cone Tangent Bound Gap

$$
\boxed{
\begin{aligned}
\text{layer}
&=
\mathrm{final\ viscosity\ bridge\ via\ central\ sign\ cone},
\\
e_1
&=
u_2,
\\
o_2
&=
u_5/\nu,
\\
u_3
&=
\nu
\frac{
A_4^{(1)}o_2-b_1e_1
}{
A_2^{(1)}
},
\\
\text{large-fibre sufficient cone}
&=
e_1<0,\ o_2>0,
\\
\text{small-fibre sufficient cone}
&=
e_1\le-0.1,\ 0\le o_2\le100,
\\
\text{endpoint cones}
&=
\mathrm{rigorously\ deep\ inside},
\\
\text{sufficient derivative bounds}
&=
|e_1'|<10^5,
\quad
|o_2'|<10^6,
\\
\text{actual tangent diagnostics}
&=
|e_1'|<2,
\quad
|o_2'|<200,
\\
\text{remaining task}
&=
\mathrm{validated\ coarse\ tangent\ cone\ on\ }(0,10^{-6}),
\\
T_{\mathsf C\to\mathsf D}
&=
\mathrm{NOT\ REACHED}.
\end{aligned}
}
$$

命名：

$$
\boxed{
\textbf{STOP-C72:
Coarse Central-Cone Tangent Bound Gap}.
}
$$

---

# 14. 24/72 Ledger — Round 68

| Step | object | $B$ | $U$ | $O$ | $L$ | status |
|---|---|---|---|---|---|---|
| C1072 | central variables $e_1,o_2$ | $\mathsf C$ | parity-rescaled core | scalar | $\mathsf F$ | DEFINED |
| C1073 | exact $n=1$ cone identity | $\mathsf C$ | central recurrence | scalar | $\mathsf F$ | EXACT |
| C1074 | large-fibre sign cone | $\mathsf C$ | coefficient geometry | targeted | $\mathsf F$ | PROVED |
| C1075 | small coefficient ratio $\Theta_-$ | $\mathsf C$ | algebraic geometry | scalar | $\mathsf F$ | PROVED $>1200$ |
| C1076 | coarse small-fibre cone | $\mathsf C$ | sign geometry | targeted | $\mathsf F$ | PROVED |
| C1077 | endpoint $e_{1,-}$ interval | $\mathsf C$ | Jost pullback | scalar | $\mathsf F$ | CERTIFIED |
| C1078 | endpoint $o_{2,-}$ interval | $\mathsf C$ | Jost pullback | scalar | $\mathsf F$ | CERTIFIED |
| C1079 | endpoint $e_{1,+}$ interval | $\mathsf C$ | Jost pullback | scalar | $\mathsf F$ | CERTIFIED |
| C1080 | endpoint $o_{2,+}$ interval | $\mathsf C$ | Jost pullback | scalar | $\mathsf F$ | CERTIFIED |
| C1081 | coarse derivative bridge lemma | $\mathsf C$ | parameter variation | targeted | $\mathsf F$ | EXACT CONDITIONAL REDUCTION |
| C1082 | $e_1'$ diagnostics | $\mathsf C$ | Riccati tangent | scalar | $\mathsf F$ | VERIFIED |
| C1083 | $o_2'$ diagnostics | $\mathsf C$ | Riccati/scattering tangent | scalar | $\mathsf F$ | VERIFIED |
| C1084 | uniform coarse tangent cone | $\mathsf C$ | validated parameter bound | targeted | $\mathsf F$ | OPEN / STOP-C72 |

---

# 15. Continuous-versus-discrete status

The central cone is a finite readout of the same continuous Floquet adjoint branch。

The endpoint intervals come from an infinite Jost pullback，not a finite truncation closure。

The missing theorem is a continuous viscosity derivative bound。

Therefore：

$$
\boxed{
T_{\mathsf C\to\mathsf D}
=
\text{NOT YET REACHED}.
}
$$

---

# 16. Next round — Parity-Rescaled Tangent Cone / Final Viscosity Closure

Round 68 has made the final sufficient theorem intentionally crude。

Concrete next targets：

1. abandon the raw graph tangent norm；
2. use the parity-rescaled / Fast-Difference Schur variables of Rounds 58 and 63；
3. differentiate the exact slow system with respect to viscosity；
4. prove only：
   $$
   |e_1'|<10^5,
   $$
   $$
   |o_2'|<10^6;
   $$
5. exploit the viscosity-independent fast resolvents：
   $$
   \|(I-\mathcal K_-)^{-1}\|<200/199,
   $$
   $$
   \|(I-\mathcal K_+)^{-1}\|<40/37;
   $$
6. bound the slow tangent through the WKB layer with extremely coarse constants；
7. invoke the Central Sign-Cone Identity；
8. conclude：
   $$
   a_{3,\pm}(\nu)>0
   \quad
   \forall\nu>0;
   $$
9. if successful，remove viscosity completely from the two $\sqrt{17}$ hidden-rescue circles。

This becomes：

$$
\boxed{
\textbf{Parity-Rescaled Tangent Cone / Final Viscosity Closure}.
}
$$

---

# 17. External primary-source anchors

Fresh literature search before this round：

1. Pierre Del Moral，Emma Horton，*A note on Riccati matrix difference equations*，arXiv:2107.12918.
   - time-varying Riccati matrix difference equations，semigroup/Floquet-type representations and uniform bounds；
   - relevant to coarse nonautonomous tangent bounds.

2. Yuri Latushkin，Shibi Vasudevan，*Fredholm determinants, continued fractions, Jost and Evans functions for a Jacobi matrix associated with the 2D-Euler equations*，arXiv:2401.14037.
   - hydrodynamic difference equations and equivalence of Jost，Evans，Fredholm and continued-fraction objects；
   - relevant to viewing the central cone as a readout of the same Jost/Fredholm compatibility branch.

The NS-specific central recurrence，cone constants，endpoint intervals and derivative margins above are direct results of this series。
