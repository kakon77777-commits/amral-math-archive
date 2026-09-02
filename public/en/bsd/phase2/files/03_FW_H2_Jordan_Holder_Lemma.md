# 03｜FW-H2 Jordan–Hölder Lemma

Let:

\[
V=E[p]|_{G_{\mathbf Q_p}},
\qquad
\omega=\bar\chi_{\rm cyc}.
\]

If \(V\) is reducible, write:

\[
V^{ss}=\lambda\oplus\mu.
\]

The Weil pairing gives:

\[
\lambda\mu=\omega.
\]

The local forbidden form of Fouquet–Wan Theorem 1.7 is:

\[
\chi\oplus\omega\chi.
\]

## Lemma

\[
V^{ss}\simeq\chi\oplus\omega\chi
\]

for some \(\chi\) iff:

\[
\lambda^2=1
\quad\text{or}\quad
\mu^2=1.
\]

### Proof

If:

\[
\{\lambda,\mu\}
=
\{\chi,\omega\chi\},
\]

comparing determinants:

\[
\omega
=
\omega\chi^2,
\]

thus:

\[
\chi^2=1.
\]

Therefore, the square of one constituent is \(1\).

Conversely, if:

\[
\lambda^2=1,
\]

then:

\[
\mu
=
\omega\lambda^{-1}
=
\omega\lambda,
\]

thus:

\[
V^{ss}
=
\lambda\oplus\omega\lambda.
\]

The case \(\mu^2=1\) is symmetric.

Therefore:

\[
\boxed{
\mathrm{FW17-H2\ FAIL}
\iff
\text{a Jordan--Hölder character is quadratic or trivial}.
}
\]

If \(V\) is irreducible over \(\mathbf F_p\), then it cannot be a direct sum of characters, hence H2 PASS.