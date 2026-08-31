# NS × X 積分 × 24/72 範式實戰
## Round 63 — Pure Continuous Fast-Difference Schur Elimination / Symmetrized Slow Gauge

- 日期：2026-08-18
- 版本：v0.1
- 狀態：Proof-Route Experiment / Continuous-Only Exact Fast-Elimination Branch
- canonical source：UTF-8 Markdown
- canonical math delimiters：inline `$...$`；display `$$...$$`
- 前一輪：`NS_X72_Round62_PureContinuous_NeutralCancellation_RestoredQuarterPowerMatching_v0.1_2026-08-18.md`
- 本輪目標：Round 62 將 small-viscosity stable-bundle gap壓成
  $$
  \text{fast Schur graph}
  +
  \text{slow Riccati}.
  $$
  本輪尋找一個不依賴病態 local eigenbasis 的 exact Schur coordinate，直接從原三階 parity recurrence消去 fast sector。
- 主要結果：
  1. 以一階差分
     $$
     d^E_j=E_j-E_{j-1},
     \qquad
     d^o_j=o_j-o_{j-1}
     $$
     作 fast variables，可將每個 parity 的三階 recurrence 精確重寫為一個「slow forcing + contractive fast feedback」方程；
  2. fast feedback係數
     $$
     p_j,\ q_j
     $$
     完全不含 viscosity；
  3. 由 Round 59 已認證的 exact coefficient boxes 直接得到，對所有
     $$
     j\ge10
     $$
    ：
     $$
     \boxed{
     \delta_-:=\sup(|p|+|q|)<0.005
     }
     $$
     於 small fibre，
     $$
     \boxed{
     \delta_+:=\sup(|p|+|q|)<0.075
     }
     $$
     於 large fibre；
  4. 因此 fast difference operator
     $$
     I-\mathcal K_{\rm fast}
     $$
     可由 Neumann series 嚴格反演，且
     $$
     \boxed{
     \|(I-\mathcal K_-)^{-1}\|
     <
     \frac{200}{199},
     }
     $$
     $$
     \boxed{
     \|(I-\mathcal K_+)^{-1}\|
     <
     \frac{40}{37};
     }
     $$
  5. fast sector 因而可被 **exactly slaved** 到 slow variables；
  6. exact Schur elimination 可寫成
     $$
     \boxed{
     d^E
     =
     \mathcal D_e
     \bigl(
     s_eE+\nu c_e o
     \bigr),
     }
     $$
     $$
     \boxed{
     d^o
     =
     \mathcal D_o
     \bigl(
     s_oo+\nu c_oE^+
     \bigr),
     }
     $$
     其中
     $$
     \mathcal D_\sigma
     =
     (I-\mathcal K_\sigma)^{-1};
     $$
  7. fast resolvent 本身是 viscosity-independent；正 viscosity 與 endpoint 的差異只進入 slow forcing，而不是 fast inversion；
  8. coefficient asymptotics：
     $$
     p_j,q_j
     \sim
     -\frac{K^2}{16j^2},
     $$
     $$
     s_j
     \sim
     \frac{3K^2}{2j^3},
     $$
     $$
     c_e(j)
     =
     \frac{16j^2}{K}
     \left(
     1+\frac1j+O(j^{-2})
     \right),
     $$
     $$
     c_o(j)
     =
     \frac{16j^2}{K}
     \left(
     1+\frac2j+O(j^{-2})
     \right);
     $$
  9. 定義 symmetrized coupling 與 staggered gauge：
     $$
     \boxed{
     \bar c_j
     =
     \sqrt{
     c_e(j)c_o(j)
     },
     }
     $$
     $$
     \boxed{
     g_j
     =
     \left[
     \frac{
     c_e(j)
     }{
     c_o(j)
     }
     \right]^{1/4};
     }
     $$
  10. 則
      $$
      \boxed{
      \bar c_j
      =
      \frac{16}{K}
      \left(
      j+\frac34
      \right)^2
      \left[
      1+O(j^{-2})
      \right],
      }
      $$
      以及
      $$
      \boxed{
      g_j
      =
      1-\frac1{4j}+O(j^{-2});
      }
      $$
  11. 因此 Round 62 中 two-parity coupling 的 $1/j$ asymmetry，大部分是一個 removable staggered-gauge effect；經
      $$
      j\mapsto j+\frac34
      $$
      與 diagonal gauge 後，slow coupling 的 first nontrivial mismatch降到
      $$
      O(j^{-2});
      $$
  12. 至此「fast Schur graph」不再是 open object；剩餘 singular gap 只在 **symmetrized slow Jost/Riccati scattering / minimal selection**；
  13. full numerical coefficient audit顯示 actual fast feedback遠小於上述 coarse rigorous bounds；在 $j=10$：
      - small fibre：
        $$
        \delta_e\approx0.001759,
        \qquad
        \delta_o\approx0.001575;
        $$
      - large fibre：
        $$
        \delta_e\approx0.065866,
        \qquad
        \delta_o\approx0.059467.
        $$
- 非主張：本輪沒有證明 slow Jost/Riccati minimal-selection matching，也沒有 yet 得到一個完整 positive-viscosity interval。它嚴格完成的是 **fast sector 的 operator-level elimination**，並辨識出 coupling 的 natural symmetrized gauge。

---

# 0. Round 62 handoff

Round 62 proved：

$$
\boxed{
S_n
=
-A_{-2}^{(n)}
+
A_0^{(n)}
-
A_2^{(n)}
+
A_4^{(n)}
=
\frac{
48K^3
}{
n^3
}
+
O(n^{-4}).
}
\tag{0.1}
$$

Hence the frozen neutral root：

$$
\boxed{
r_{\rm neu}(n)
=
1+
\frac{
12K^2
}{
n^3
}
+
O(n^{-4}).
}
\tag{0.2}
$$

It also obtained：

$$
\boxed{
a_e/a_j
=
1+j^{-1}+O(j^{-2}),
}
\tag{0.3}
$$

$$
\boxed{
a_o/a_j
=
1+2j^{-1}+O(j^{-2}),
}
\tag{0.4}
$$

with：

$$
a_j
=
16\nu j^2/K.
$$

Round 62 STOP：

$$
\boxed{
\text{STOP-C66}
=
\text{Neutral-Cancelled Schur/Riccati Enclosure Gap}.
}
$$

---

# 1. Exact difference coordinates

Use the Round 60 rescaled slow pair：

$$
\boxed{
E_j
=
e_j/\nu,
}
\tag{1.1}
$$

and：

$$
\boxed{
o_j.
}
\tag{1.2}
$$

Define the parity differences：

$$
\boxed{
d^E_j
=
E_j-E_{j-1},
}
\tag{1.3}
$$

$$
\boxed{
d^o_j
=
o_j-o_{j-1}.
}
\tag{1.4}
$$

For a generic parity sequence：

$$
x_j,
$$

the exact same-parity recurrence is：

$$
\boxed{
-
A_{-2}
x_{j-1}
+
A_0x_j
-
A_2x_{j+1}
+
A_4x_{j+2}
=
F_j.
}
\tag{1.5}
$$

Write：

$$
x_{j-1}
=
x_j-d_j,
$$

$$
x_{j+1}
=
x_j+d_{j+1},
$$

$$
x_{j+2}
=
x_j+d_{j+1}+d_{j+2}.
$$

Then：

$$
\boxed{
Sx_j
+
A_{-2}d_j
+
(-A_2+A_4)d_{j+1}
+
A_4d_{j+2}
=
F_j,
}
\tag{1.6}
$$

where：

$$
\boxed{
S
=
-A_{-2}+A_0-A_2+A_4.
}
\tag{1.7}
$$

---

# 2. Exact fast-difference coefficients

Define：

$$
\boxed{
D_n
=
-A_2^{(n)}
+
A_4^{(n)}.
}
\tag{2.1}
$$

For the source-filter coefficients：

$$
b_n
=
J_1^{(n)}/\nu,
$$

define：

$$
\boxed{
p_n
=
-\frac{
A_{-2}^{(n)}
}{
D_n
},
}
\tag{2.2}
$$

$$
\boxed{
q_n
=
-\frac{
A_4^{(n)}
}{
D_n
},
}
\tag{2.3}
$$

$$
\boxed{
s_n
=
-\frac{
S_n
}{
D_n
},
}
\tag{2.4}
$$

and：

$$
\boxed{
c_n
=
\frac{
b_n
}{
D_n
}.
}
\tag{2.5}
$$

On the present two fibres and large positive sidebands：

$$
D_n<0,
$$

$$
p_n<0,
\qquad
q_n<0,
$$

while：

$$
s_n>0,
\qquad
c_n>0.
$$

---

# 3. Exact parity difference equations

For the even parity：

$$
n=2j,
$$

the rescaled recurrence becomes：

$$
\boxed{
d^E_{j+1}
=
\nu
c_{2j}
o_j
+
s_{2j}
E_j
+
p_{2j}
d^E_j
+
q_{2j}
d^E_{j+2}.
}
\tag{3.1}
$$

For odd parity：

$$
n=2j+1,
$$

$$
\boxed{
d^o_{j+1}
=
\nu
c_{2j+1}
E_{j+1}
+
s_{2j+1}
o_j
+
p_{2j+1}
d^o_j
+
q_{2j+1}
d^o_{j+2}.
}
\tag{3.2}
$$

These are exact identities，not asymptotic models。

---

# 4. Fast coefficients are genuinely small

From Rounds 53 and 62：

$$
A_{-2}^{(n)}
=
-\frac{
K^3
}{
n^2
}
+
O(n^{-3}),
$$

$$
A_4^{(n)}
=
-\frac{
K^3
}{
n^2
}
+
O(n^{-3}),
$$

and：

$$
D_n
=
-4K
+
O(n^{-1}).
$$

Therefore：

$$
\boxed{
p_n
=
-\frac{
K^2
}{
4n^2
}
+
O(n^{-3}),
}
\tag{4.1}
$$

$$
\boxed{
q_n
=
-\frac{
K^2
}{
4n^2
}
+
O(n^{-3}).
}
\tag{4.2}
$$

At：

$$
n\sim2j,
$$

$$
\boxed{
p_j,q_j
=
-\frac{
K^2
}{
16j^2
}
+
O(j^{-3}).
}
\tag{4.3}
$$

Hence：

$$
\boxed{
|p_j|+|q_j|
=
\frac{
K^2
}{
8j^2
}
+
O(j^{-3}).
}
\tag{4.4}
$$

---

# 5. Neutral drift in difference coordinates

Using：

$$
S_n
=
48K^3n^{-3}
+
O(n^{-4}),
$$

and：

$$
D_n
=
-4K+O(n^{-1}),
$$

we get：

$$
\boxed{
s_n
=
\frac{
12K^2
}{
n^3
}
+
O(n^{-4}).
}
\tag{5.1}
$$

Thus：

$$
\boxed{
s_{2j},
s_{2j+1}
=
\frac{
3K^2
}{
2j^3
}
+
O(j^{-4}).
}
\tag{5.2}
$$

This is exactly the Round 62 neutral-root drift，now appearing as the direct slow forcing term in the difference-Schur equation。

---

# 6. Viscous slow coupling

Since：

$$
b_n
=
-16n^2
[
1+O(n^{-1})
],
$$

and：

$$
D_n
=
-4K
[
1+O(n^{-1})
],
$$

$$
\boxed{
c_n
=
\frac{
4n^2
}{
K
}
[
1+O(n^{-1})
].
}
\tag{6.1}
$$

For the two parities，Round 62 exact limits sharpen this to：

$$
\boxed{
c_e(j)
:=
c_{2j}
=
\frac{
16j^2
}{
K
}
\left[
1+\frac1j+O(j^{-2})
\right],
}
\tag{6.2}
$$

$$
\boxed{
c_o(j)
:=
c_{2j+1}
=
\frac{
16j^2
}{
K
}
\left[
1+\frac2j+O(j^{-2})
\right].
}
\tag{6.3}
$$

So the positive-viscosity slow forcing is：

$$
\nu c_eo
$$

or：

$$
\nu c_oE^+.
$$

---

# 7. Inherited exact tail boxes

Round 59 certified，for all：

$$
j\ge10,
$$

and for both even/odd parity levels：

## small fibre

$$
\boxed{
-0.01
<
A_{-2},A_4
<
0,
}
\tag{7.1}
$$

$$
\boxed{
4
<
A_2
<
5.
}
\tag{7.2}
$$

Therefore：

$$
A_2-A_4
>
4,
$$

and：

$$
\boxed{
|p|+|q|
=
\frac{
-A_{-2}-A_4
}{
A_2-A_4
}
<
\frac{
0.02
}{
4
}
=
0.005.
}
\tag{7.3}
$$

## large fibre

Round 59 certified：

$$
\boxed{
-1.4
<
A_{-2}
<
0,
}
\tag{7.4}
$$

$$
\boxed{
-0.4
<
A_4
<
0,
}
\tag{7.5}
$$

and：

$$
\boxed{
A_2>24.
}
\tag{7.6}
$$

Hence：

$$
\boxed{
|p|+|q|
<
\frac{
1.8
}{
24
}
=
0.075.
}
\tag{7.7}
$$

These are deliberately coarse，but already extremely strong。

---

# 8. Fast-Difference Schur Theorem

For a tail beginning at：

$$
j\ge10,
$$

define：

$$
\boxed{
(\mathcal Kd)_{j+1}
=
p_jd_j
+
q_jd_{j+2}.
}
\tag{8.1}
$$

On：

$$
\ell^\infty,
$$

$$
\boxed{
\|\mathcal K\|
\le
\sup_j
(
|p_j|+|q_j|
).
}
\tag{8.2}
$$

Thus：

### small fibre

$$
\boxed{
\|\mathcal K_-\|
<
\frac1{200},
}
\tag{8.3}
$$

and：

$$
\boxed{
\|
(I-\mathcal K_-)^{-1}
\|
<
\frac{
200
}{
199
}.
}
\tag{8.4}
$$

### large fibre

$$
\boxed{
\|\mathcal K_+\|
<
\frac3{40},
}
\tag{8.5}
$$

and：

$$
\boxed{
\|
(I-\mathcal K_+)^{-1}
\|
<
\frac{
40
}{
37
}.
}
\tag{8.6}
$$

命名：

$$
\boxed{
\textbf{Fast-Difference Schur Theorem}.
}
$$

No local fast eigenvectors are needed。

---

# 9. Resolvent defect

Let：

$$
\boxed{
\mathcal D
=
(I-\mathcal K)^{-1}.
}
\tag{9.1}
$$

Then：

$$
\boxed{
\mathcal D-I
=
\mathcal K
(I-\mathcal K)^{-1}.
}
\tag{9.2}
$$

Therefore：

### small fibre

$$
\boxed{
\|\mathcal D_--I\|
<
\frac1{199}.
}
\tag{9.3}
$$

### large fibre

$$
\boxed{
\|\mathcal D_+-I\|
<
\frac3{37}.
}
\tag{9.4}
$$

The actual coefficients are much smaller than these coarse bounds once：

$$
j>10.
$$

Asymptotically：

$$
\boxed{
\|\mathcal D-I\|_{\text{local tail}}
=
O(j^{-2}).
}
\tag{9.5}
$$

---

# 10. Exact fast elimination

Equations (3.1)–(3.2) may therefore be solved exactly for the fast differences：

$$
\boxed{
d^E
=
\mathcal D_e
\left[
s_eE
+
\nu c_eo
\right],
}
\tag{10.1}
$$

and：

$$
\boxed{
d^o
=
\mathcal D_o
\left[
s_oo
+
\nu c_oE^+
\right].
}
\tag{10.2}
$$

Here：

$$
E^+_j
=
E_{j+1}.
$$

This is the operator-level Schur complement of the two fast parity sectors。

Most importantly：

$$
\boxed{
\mathcal D_e,
\mathcal D_o
\text{ do not depend on }\nu.
}
\tag{10.3}
$$

So positive viscosity changes only the slow source，not the invertibility of the fast sector。

---

# 11. Endpoint and positive-viscosity dynamics use the same fast resolvent

At：

$$
\nu=0,
$$

$$
\boxed{
d^E
=
\mathcal D_e
[
s_eE
],
}
\tag{11.1}
$$

$$
\boxed{
d^o
=
\mathcal D_o
[
s_oo
].
}
\tag{11.2}
$$

For：

$$
\nu>0,
$$

one simply adds：

$$
\boxed{
\nu
\mathcal D_e
[
c_eo
]
}
$$

and：

$$
\boxed{
\nu
\mathcal D_o
[
c_oE^+
].
}
$$

Thus the singular perturbation is now visibly a **slow forcing / slow selection problem**。

The fast graph itself is common to the endpoint and positive-viscosity branches。

---

# 12. Symmetrized coupling

Define：

$$
\boxed{
\bar c_j
=
\sqrt{
c_e(j)c_o(j)
}.
}
\tag{12.1}
$$

From (6.2)–(6.3)：

$$
\boxed{
\frac{
c_ec_o
}{
(16j^2/K)^2
}
=
1+\frac3j+O(j^{-2}).
}
\tag{12.2}
$$

Therefore：

$$
\boxed{
\bar c_j
=
\frac{
16j^2
}{
K
}
\left[
1+\frac{
3
}{
2j
}
+
O(j^{-2})
\right].
}
\tag{12.3}
$$

But：

$$
\boxed{
\left(
j+\frac34
\right)^2
=
j^2
\left[
1+\frac{
3
}{
2j
}
+
\frac{
9
}{
16j^2
}
\right].
}
\tag{12.4}
$$

Hence：

$$
\boxed{
\bar c_j
=
\frac{
16
}{
K
}
\left(
j+\frac34
\right)^2
\left[
1+O(j^{-2})
\right].
}
\tag{12.5}
$$

命名：

$$
\boxed{
\textbf{Three-Quarter Shift Law}.
}
$$

---

# 13. Staggered diagonal gauge

Define：

$$
\boxed{
g_j
=
\left(
\frac{
c_e(j)
}{
c_o(j)
}
\right)^{1/4}.
}
\tag{13.1}
$$

Since：

$$
\frac{
c_e
}{
c_o
}
=
1-\frac1j+O(j^{-2}),
$$

we obtain：

$$
\boxed{
g_j
=
1-\frac1{4j}+O(j^{-2}).
}
\tag{13.2}
$$

Now rescale the slow pair by：

$$
\boxed{
\widetilde E_j
=
g_j
E_j,
}
\tag{13.3}
$$

$$
\boxed{
\widetilde o_j
=
g_j^{-1}
o_j.
}
\tag{13.4}
$$

At frozen level，the two cross-couplings become equal to：

$$
\boxed{
\nu\bar c_j.
}
\tag{13.5}
$$

Also：

$$
\boxed{
\frac{
g_{j+1}
}{
g_j
}
=
1+O(j^{-2}),
}
\tag{13.6}
$$

so the gauge itself introduces no new $O(j^{-1})$ dynamical defect。

---

# 14. Meaning of the gauge

Round 62 treated the parity coupling corrections：

$$
1+\frac1j
$$

and：

$$
1+\frac2j
$$

as separate first-order effects。

Round 63 shows：

$$
\boxed{
\text{their asymmetry is largely coordinate，not dynamical}.
}
$$

After the staggered gauge：

$$
\boxed{
a_{\rm slow}(j,\nu)
=
\nu\bar c_j
=
\frac{
16\nu
}{
K
}
\left(
j+\frac34
\right)^2
[
1+O(j^{-2})
].
}
\tag{14.1}
$$

Thus the natural slow WKB coordinate is not：

$$
j,
$$

but：

$$
\boxed{
j+\frac34.
}
\tag{14.2}
$$

---

# 15. Reduced slow problem after exact fast elimination

Use：

$$
E_{j+1}
=
E_j+d^E_{j+1},
$$

and：

$$
o_{j+1}
=
o_j+d^o_{j+1}.
$$

After substituting the exact resolvents：

$$
\mathcal D_e,
\mathcal D_o,
$$

the full six-dimensional problem has been reduced to a two-component nonlocal slow system。

After the gauge (13.3)–(13.4)，its leading local part is the symmetric Round 60 matrix：

$$
\boxed{
M(
\nu\bar c_j
)
=
\begin{pmatrix}
1
&
\nu\bar c_j
\\
\nu\bar c_j
&
1+
\nu^2\bar c_j^2
\end{pmatrix},
}
\tag{15.1}
$$

up to：

1. exact endpoint neutral drift already carried by：
   $$
   \mathcal D_\sigma s_\sigma;
   $$

2. fast-resolvent nonlocality：
   $$
   O(j^{-2});
   $$

3. gauge variation：
   $$
   O(j^{-2});
   $$

4. higher coupling corrections：
   $$
   O(j^{-2}).
   $$

The fast subspace itself is no longer an unknown。

---

# 16. Projective slow coordinate

Define：

$$
\boxed{
z_j
=
\frac{
\widetilde E_j
}{
\widetilde o_j
}.
}
\tag{16.1}
$$

The leading symmetric local map is：

$$
\boxed{
z_{j+1}
=
\frac{
z_j+\bar a_j
}{
\bar a_jz_j+1+\bar a_j^2
},
}
\tag{16.2}
$$

where：

$$
\boxed{
\bar a_j
=
\nu\bar c_j.
}
\tag{16.3}
$$

The exact reduced problem has the form：

$$
\boxed{
z_{j+1}
=
\frac{
z_j+\bar a_j
}{
\bar a_jz_j+1+\bar a_j^2
}
+
\mathfrak R_j[
z;\nu
],
}
\tag{16.4}
$$

where：

$$
\mathfrak R_j
$$

now contains only slow Jost-scattering / nonlocal-resolvent corrections。

This is the genuine remaining scalar obstruction。

---

# 17. Numerical coefficient audit

The attached CSV evaluates the exact coefficient formulas。

At：

$$
j=10,
$$

the actual fast feedback norms are：

### small fibre

$$
\boxed{
\delta_e
\approx
0.0017591808,
}
\tag{17.1}
$$

$$
\boxed{
\delta_o
\approx
0.0015752900.
}
\tag{17.2}
$$

### large fibre

$$
\boxed{
\delta_e
\approx
0.0658657228,
}
\tag{17.3}
$$

$$
\boxed{
\delta_o
\approx
0.0594670886.
}
\tag{17.4}
$$

They decay as：

$$
K^2/(8j^2).
$$

---

# 18. Symmetrized-coupling audit

For the shifted reference：

$$
\boxed{
c_{\rm shift}(j)
=
\frac{
16
}{
K
}
\left(
j+\frac34
\right)^2,
}
\tag{18.1}
$$

the exact ratio：

$$
\boxed{
\bar c_j/c_{\rm shift}(j)
}
$$

already satisfies：

### small fibre

$$
\boxed{
0.99929\ldots
}
$$

at：

$$
j=10,
$$

and：

$$
0.999999998\ldots
$$

by：

$$
j=10^4.
$$

### large fibre

the $j=10$ ratio is still：

$$
1.0733\ldots,
$$

but falls to：

$$
1.00063\ldots
$$

by：

$$
j=100,
$$

and：

$$
1.00000006\ldots
$$

by：

$$
j=10^4.
$$

This confirms the Three-Quarter Shift Law in the full coefficients。

---

# 19. What has been closed

Before Round 63：

$$
\boxed{
\text{fast Schur graph}
}
$$

was still a proof obligation。

After Round 63：

$$
\boxed{
\text{fast Schur graph}
=
\text{bounded inverse }
(I-\mathcal K_{\rm fast})^{-1}.
}
$$

The two fast parity sectors are therefore not merely asymptotically understood。

They are explicitly and uniquely slaved in an operator norm。

So the remaining problem is no longer：

$$
\text{three-plane matching}.
$$

It is：

$$
\boxed{
\text{one symmetrized slow Jost/Riccati selection problem}.
}
$$

---

# 20. STOP-C67 — Slow Jost-Scattering / Singular Riccati Selection Gap

$$
\boxed{
\begin{aligned}
\text{layer}
&=
\mathrm{small\text{-}viscosity\ exact\ fast\ elimination},
\\
d^E_j
&=
E_j-E_{j-1},
\\
d^o_j
&=
o_j-o_{j-1},
\\
\text{fast feedback}
&=
p_jd_j+q_jd_{j+2},
\\
\delta_-
&<
0.005,
\\
\delta_+
&<
0.075,
\\
\text{fast inverse}
&=
(I-\mathcal K_{\rm fast})^{-1}
\text{ exists rigorously},
\\
\text{viscosity dependence of fast inverse}
&=
0,
\\
\text{neutral drift}
&\sim
3K^2/(2j^3),
\\
\text{symmetrized coupling}
&=
\frac{16\nu}{K}
(j+3/4)^2
[
1+O(j^{-2})
],
\\
\text{parity asymmetry}
&=
\mathrm{gauge\text{-}removable\ at\ }O(j^{-1}),
\\
\text{remaining singular object}
&=
\mathrm{one\ slow\ projective/Jost\ line},
\\
\text{positive small-}\nu\text{ interval}
&=
\mathrm{not\ yet\ proved},
\\
\text{missing}
&=
\mathrm{validated\ slow\ Riccati/Jost\ scattering\ selection}
\\
&\quad
\mathrm{through\ }j\sim\nu^{-1/3},
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
\textbf{STOP-C67:
Slow Jost-Scattering / Singular Riccati Selection Gap}.
}
$$

---

# 21. 24/72 Ledger — Round 63

| Step | object | $B$ | $U$ | $O$ | $L$ | status |
|---|---|---|---|---|---|---|
| C1005 | parity difference coordinates | $\mathsf C$ | exact recurrence transform | relational | $\mathsf F$ | EXACT |
| C1006 | fast coefficients $p,q$ | $\mathsf C$ | Schur feedback | scalar | $\mathsf F$ | EXACT |
| C1007 | slow neutral coefficient $s$ | $\mathsf C$ | endpoint drift | scalar | $\mathsf F$ | EXACT |
| C1008 | viscous slow coefficient $c$ | $\mathsf C$ | parity coupling | scalar | $\mathsf F$ | EXACT |
| C1009 | inherited global tail coefficient boxes | $\mathsf C$ | interval/algebraic bounds | targeted | $\mathsf F$ | CERTIFIED dependency |
| C1010 | small-fibre fast norm | $\mathsf C$ | operator norm | scalar | $\mathsf F$ | PROVED |
| C1011 | large-fibre fast norm | $\mathsf C$ | operator norm | scalar | $\mathsf F$ | PROVED |
| C1012 | Fast-Difference Schur Theorem | $\mathsf C$ | Banach inverse | targeted | $\mathsf F$ | PROVED |
| C1013 | exact fast elimination | $\mathsf C$ | operator Schur complement | relational | $\mathsf F$ | PROVED |
| C1014 | symmetrized coupling $\bar c$ | $\mathsf C$ | slow gauge | scalar | $\mathsf F$ | DERIVED |
| C1015 | Three-Quarter Shift Law | $\mathsf C$ | asymptotic coordinate | scalar | $\mathsf F$ | DERIVED |
| C1016 | staggered gauge $g_j$ | $\mathsf C$ | parity symmetrization | scalar | $\mathsf F$ | DERIVED |
| C1017 | slow nonlocal system | $\mathsf C$ | exact reduced dynamics | relational | $\mathsf F$ | IDENTIFIED |
| C1018 | slow projective Riccati form | $\mathsf C$ | scalar projective dynamics | scalar | $\mathsf F$ | REDUCED |
| C1019 | singular slow-line selection | $\mathsf C$ | Jost scattering | targeted | $\mathsf F$ | OPEN / STOP-C67 |

---

# 22. Continuous-versus-discrete status

The fast difference coordinate is merely a Fourier-sideband representation of the continuous periodic adjoint operator。

The operator：

$$
I-\mathcal K_{\rm fast}
$$

is a bounded spectral-coordinate operator on the continuous Floquet fibre。

The Schur elimination and Riccati variable describe invariant subspaces of that continuous operator family。

No discrete physical mechanism or finite combinatorial closure is introduced。

Therefore：

$$
\boxed{
T_{\mathsf C\to\mathsf D}
=
\text{NOT YET REACHED}.
}
$$

---

# 23. Strongest results of Round 63

## R63-A — exact fast-coordinate identity

$$
\boxed{
d_{j+1}
=
\nu c_j(\text{other slow})
+
s_j(\text{own slow})
+
p_jd_j
+
q_jd_{j+2}.
}
$$

## R63-B — global fast contraction

$$
\boxed{
\delta_-<0.005,
\qquad
\delta_+<0.075.
}
$$

## R63-C — fast Schur inverse exists

$$
\boxed{
\|
\mathcal D_-
\|
<
200/199,
}
$$

$$
\boxed{
\|
\mathcal D_+
\|
<
40/37.
}
$$

## R63-D — fast inverse is viscosity-independent

All $\nu$ dependence sits in the slow forcing。

## R63-E — symmetrized slow coupling

$$
\boxed{
\bar c_j
=
\frac{
16
}{
K
}
(j+3/4)^2
[
1+O(j^{-2})
].
}
$$

## R63-F — parity asymmetry is gauge-removable

$$
\boxed{
g_j
=
1-\frac1{4j}+O(j^{-2}).
}
$$

The remaining singular proof object is a single slow Jost/Riccati line。

---

# 24. Next round — Slow Jost Scattering / First Rigorous Positive-Viscosity Interval

Round 63 has eliminated the fast sector exactly。

The next round should now stop discussing fast eigenvectors entirely。

Concrete targets：

1. work directly with the exact Schur-resolved slow system；
2. apply the staggered gauge：
   $$
   \widetilde E_j=g_jE_j,
   \qquad
   \widetilde o_j=g_j^{-1}o_j;
   $$

3. use the shifted coupling：
   $$
   \bar a_j
   =
   \frac{
   16\nu
   }{
   K
   }
   (j+3/4)^2
   [
   1+O(j^{-2})
   ];
   $$

4. derive a scalar interval Riccati/Jost map with explicit remainder；
5. treat the deep：
   $$
   j\gtrsim\nu^{-1/3}
   $$
   layer by backward stable selection；
6. pull the slow-line interval through the outer Jost region；
7. compare the resulting center functional to the rigorous Round 59：
   $$
   c_{0,-}>5.79,
   \qquad
   c_{0,+}>5.33;
   $$

8. aim first for a concrete：
   $$
   0<\nu\le\nu_s
   $$
   rather than an optimal asymptotic theorem；
9. once one interval is certified，extend it upward by validated continuation；
10. combine with Round 56's rigorous：
    $$
    \nu=1
    $$
    slice。

This becomes：

$$
\boxed{
\textbf{Slow Jost Scattering / First Rigorous Positive-Viscosity Interval}.
}
$$

---

# 25. External primary-source anchors

1. F. Battelli, M. Franca, K. J. Palmer, *Exponential Dichotomy for Noninvertible Linear Difference Equations*, arXiv:2111.04553.
   - roughness and persistence of dichotomies for linear difference equations；
   - relevant to the invariant-subspace control once the fast block has been eliminated。

2. Pierre Del Moral, Emma Horton, *A note on Riccati matrix difference equations*, arXiv:2107.12918.
   - develops time-varying Riccati difference equations，duality formulae and uniform bounds；
   - relevant to the nonautonomous slow projective/Riccati formulation。

3. Yuri Latushkin, Shibi Vasudevan, *Fredholm determinants, continued fractions, Jost and Evans functions for a Jacobi matrix associated with the 2D-Euler equations*, arXiv:2401.14037.
   - relates hydrodynamic difference-equation Jost，Evans，Fredholm and continued-fraction representations；
   - relevant to converting the slow projective line into the endpoint Green/Jost compatibility functional。

All NS-specific difference-Schur identities，resolvent bounds，three-quarter shift and numerical coefficient diagnostics in Round 63 are direct consequences of this project and the certified coefficient boxes from Round 59。

---

# 26. Commit state

$$
\boxed{
\begin{aligned}
\text{Route}
&=
\mathrm{Pure\ Continuous\ Fast\text{-}Difference\ Schur\ Elimination},
\\
\text{Essential }\mathsf C\to\mathsf D
&=
\mathrm{Not\ reached},
\\
\text{Fast sector}
&=
\mathrm{rigorously\ eliminated},
\\
\text{Fast resolvent}
&=
\mathrm{viscosity\text{-}independent},
\\
\text{Parity coupling}
&=
\mathrm{symmetrized\ by\ staggered\ gauge},
\\
\text{Natural slow coordinate}
&=
j+3/4,
\\
\text{Remaining dimension}
&=
1
\text{ projective slow line},
\\
\text{STOP-C67}
&=
\mathrm{Slow\ Jost\text{-}Scattering/Singular\ Riccati\ Selection\ Gap},
\\
\text{Next}
&=
\mathrm{Slow\ Jost\ Scattering/First\ Rigorous\ Positive\text{-}Viscosity\ Interval}.
\end{aligned}
}
$$
