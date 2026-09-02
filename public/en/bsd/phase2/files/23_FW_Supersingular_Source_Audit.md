# 23 | Fouquet–Wan Supersingular Source Audit

For any odd good supersingular prime $p$ of $E_q$.

## H1

Fouquet–Wan requires the global residual representation to be absolutely irreducible.

The mod-$p$ image of the base `696.e1` is maximal; the quadratic twist preserves absolute irreducibility.

PASS.

## H2

FW Theorem 1.7 excludes:

$$
\bar\rho|_{G_{\mathbf Q_p}}^{ss}
=
\chi\oplus\chi_{\rm cyc}\chi.
$$

The good supersingular local residual representation is an irreducible niveau-2 type, so it cannot be a character direct sum.

PASS.

## H3

There is no need to guess the representation normalization.

The original text around FW Theorem 1.1 explicitly states that Assumption 3 is equivalent to:

- the local automorphic representation is special Steinberg;
- twist by an unramified character taking $\ell$ to
  $(-1)\ell^{k/2-1}$;
- the residual representation is ramified.

For weight $k=2$:

$$
(-1)\ell^0=-1.
$$

For an elliptic newform:

$$
a_\ell=-1
$$

i.e., nonsplit multiplicative.

Take:

$$
\ell=29.
$$

`696.e1` is nonsplit multiplicative at 29, and an admissible $q$ makes 29 split in
$\mathbf Q(\sqrt q)$, so the local quadratic twist is trivial.

Moreover:

$$
v_{29}(\Delta)=1,
$$

thus for any odd $p\ne29$, the residual representation remains ramified.

A good supersingular prime $p$ is, of course, not equal to the bad prime 29.

PASS.

## BSD conclusion

Theorem 2.14 first gives:

$$
L(E_q,1)\ne0.
$$

Fouquet–Wan Corollary 1.10 thus gives the corresponding $p$-part BSD; for the period issue, see the next audit.