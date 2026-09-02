# Round 11 Historical Pressure Memory Audit

The Round 11 optimization retains all existing test curves and only alters the rigid body configuration; it does not delete historical attacks due to low final-state activity.

Therefore, the role of historical memory is not to fix old configurations, but to continuously require that every curve that previously exerted pressure has at least one valid placement.

The current classification is:

- Persistent skeleton: Curves from Rounds 5, 7, 8, 10, and 11;
- Transient pressure: Curves from Rounds 6 and 9.

The curves from Rounds 6 and 9 may evaluate to zero in the final-state leave-one-out, but they are still retained in the 14-family container test set.

This avoids the forgetting problem of "deleting due to current redundancy, only to reopen old gaps later."

Formally:

\[
\mathcal H_n
=
\{\gamma_j:e_j\ge\varepsilon_{\mathrm{attack}},\ j\le n\}
\]

is the historical pressure memory, while:

\[
\mathcal A_n
=
\{\gamma_j:\ell_j\ge\varepsilon_{\mathrm{active}}\}
\]

is the final-state active set.

Generally:

\[
\mathcal A_n
\subsetneq
\mathcal H_n.
\]

The constraint set for container updates should use \(\mathcal H_n\), whereas the compression and interpretation layers may use \(\mathcal A_n\).