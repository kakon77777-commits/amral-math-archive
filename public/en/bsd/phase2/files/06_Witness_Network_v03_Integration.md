# 06｜Witness-Network v0.3 Integration

The certificate for a fixed odd additive prime \(p\) is updated to:

```text
FW_PROFILE
    default = FW17_EXACT

GLOBAL_H1
    E[p] absolutely irreducible over G_Q

LOCAL_H2
    if potentially multiplicative:
        FAIL

    elif local E[p] irreducible over F_p:
        PASS

    else:
        construct local p-isogeny phi
        construct dual phihat

        kernel(phi) Qp-linear root?
        kernel(phihat) Qp-linear root?

        either YES -> FAIL
        both NO    -> PASS

H3
    nonsplit multiplicative witness ell != p
    p ∤ v_ell(Delta)

PERIOD
    modular/Neron p-adic compatibility

FINAL
    all PASS -> fixed additive p certified by Fouquet-Wan
```

## Global consequence

Odd additive primes still only generate a finite table:

\[
\mathcal A_{\rm odd}(E).
\]

Therefore:

\[
\forall p
\]

there is no re-expansion.

The true improvement of v0.3 is:

\[
\boxed{
\text{A2 H2 UNKNOWN}
\to
\text{exact finite local isogeny test}.
}
\]