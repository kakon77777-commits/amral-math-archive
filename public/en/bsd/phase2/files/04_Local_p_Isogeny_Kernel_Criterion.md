# 04 | Local \(p\)-Isogeny Kernel Criterion

Assume:

\[
E[p]|_{G_{\mathbf Q_p}}
\]

is reducible.

Choose a stable cyclic subgroup:

\[
C\simeq\mathbf Z/p
\]

yielding a local isogeny:

\[
\phi:E\to E'.
\]

Let:

\[
\sigma(P)=\lambda(\sigma)P
\]

for a generator \(P\in C\).

Since:

\[
x(P)=x(-P),
\]

and \(p\) is odd:

\[
x(P)\in\mathbf Q_p
\]

iff:

\[
\sigma(P)=\pm P
\quad\forall\sigma,
\]

iff:

\[
\lambda(G_{\mathbf Q_p})\subset\{\pm1\},
\]

iff:

\[
\lambda^2=1.
\]

Therefore:

\[
\boxed{
\lambda^2=1
\iff
\text{the kernel polynomial of }\ker\phi\text{ has a }\mathbf Q_p\text{-linear factor}.
}
\]

The other JH character:

\[
\mu=\omega\lambda^{-1}
\]

is associated with the dual isogeny:

\[
\widehat\phi:E'\to E
\]

as its kernel character.

Hence:

\[
\boxed{
\mathrm{FW17-H2\ FAIL}
}
\]

iff the kernel polynomial of `phi` or `dual(phi)` has a linear factor over \(\mathbf Q_p\).

## Why is one isogeny + dual sufficient?

- nonsplit reducible extension: the original \(E[p]\) has only one stable line; the quotient constituent appears in the dual kernel;
- split representation: the two constituents are directly captured by \(\phi, \widehat\phi\);
- there is no need to enumerate all local \(p\)-isogenies.