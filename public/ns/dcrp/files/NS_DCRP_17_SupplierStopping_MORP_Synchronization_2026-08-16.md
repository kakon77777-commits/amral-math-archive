# NS-DCRP-17 — Supplier Stopping-Time Synchronization, Native Obstruction Extraction, and the Excursion-Irreversibility Barrier

- date: 2026-08-16
- status: research proof checkpoint
- canonical source: UTF-8 Markdown
- canonical math delimiters: `$...$` and `$$...$$`
- objective:
  1. install the DCRP-16 local supplier sequence as an actual MORP-compatible return/re-root stopping rule;
  2. prove that supplier-rooted finite-window packages are genuinely native-separated and compact after fixed normalization;
  3. determine whether this already forces a contradiction with MORP minimality.
- no full Navier--Stokes regularity claim is made.
- principal internal dependencies:
  - MORP-01 normalized native obstruction slice and extended cost;
  - MORP-02 defect-completed compactness;
  - MORP-03 actual return/re-root semantics and Minimal Return Rigidity;
  - DCRP-14 through DCRP-16 supplier trace/realization/local-capture modules.
- external calibration:
  - Gallagher--Koch--Planchon, arXiv:1012.0145;
  - Jia--Šverák, arXiv:1201.1592.
- no novelty / priority claim is made without independent audit.

---

# 1. Executive result

DCRP-16 proved that if

$$
z_\ast=(x_\ast,T)
$$

is a first singular point, then there exist actual local supplier events

$$
\boxed{
(t_n,x_n,\lambda_n)
}
$$

with

$$
\boxed{
t_n\uparrow T,
\qquad
x_n\to x_\ast,
\qquad
\lambda_n\to\infty,
}
\tag{1.1}
$$

and

$$
\boxed{
\lambda_n^{-1}
|
\Delta_{\lambda_n}u(x_n,t_n)
|
\ge
c_{\rm loc}\nu.
}
\tag{1.2}
$$

DCRP-14/15 then attach to every such event an actual nonlinear supplier increment and a fixed normalized finite-window package satisfying

$$
\boxed{
\|
\mathcal O_{W_\ast}^T d_n
\|
+
C_{\rm sup}
\mathcal B_{\rm sup}^{res}(n)
\ge
c_{\rm sup}\nu.
}
\tag{1.3}
$$

The first theorem of this round shows that the supplier package is genuinely native-separated.

Let

$$
\mathcal A_\ast d
=
\left(
\mathcal O_{W_\ast}^T d,
\mathcal R_{W_\ast}^{sup}d
\right),
$$

where the second component contains the fixed finite-window residual coordinates used in DCRP-15.

Because exact gauge/null directions are annihilated by

$$
\mathcal A_\ast,
$$

the map descends to the finite-dimensional quotient.

Hence there is a fixed constant

$$
C_A<\infty
$$

such that

$$
\boxed{
\|
\mathcal A_\ast d
\|
\le
C_A
d_{\rm nat}(d).
}
\tag{1.4}
$$

Combining with (1.3),

$$
\boxed{
d_{\rm nat}(d_n)
\ge
a_{\rm sup}
>
0.
}
\tag{1.5}
$$

After homogeneous normalization by

$$
a_{\rm sup},
$$

supplier packages satisfy

$$
d_{\rm nat}\ge1.
$$

Because the normalized supplier package lives in one fixed finite-dimensional quotient/template, norm equivalence gives a uniform package bound

$$
\boxed{
\mathcal N_{\rm pkg}(d_n)
\le
C_\ast.
}
\tag{1.6}
$$

Therefore the singularity produces an actual non-tautological supplier-rooted obstruction slice

$$
\boxed{
\mathscr O_{\rm sup}
\subset
\mathscr O_1.
}
\tag{1.7}
$$

The second theorem installs a canonical supplier stopping rule.

Fix one integer scale gap

$$
L\ge1.
$$

Given an actual singular-rooted supplier window with dyadic reference index

$$
q,
$$

define the next supplier return to be the canonical first later local supplier event satisfying

$$
q'\ge q+L,
$$

with the deterministic spatial/time tie-breaking rule declared in advance.

DCRP-16 guarantees that such later events exist arbitrarily close to

$$
T.
$$

Thus:

$$
\boxed{
\mathsf T_{\rm sup}
:
\mathscr O_{\rm sup}^{act}
\to
\mathscr O_{\rm sup}^{act}
}
\tag{1.8}
$$

is an actual same-history return/re-root map.

This is exactly the type of return rule MORP-03 permits:

- first later native-separated window;
- first later dangerous/native-separated window;
- next member of a declared admissible extraction sequence.

The supplier rule is declared before compactness/minimality.

Thus:

$$
\boxed{
\textbf{
actual supplier return realization is no longer the missing issue on the supplier-rooted slice.
}
}
\tag{1.9}
$$

Moreover, the fixed normalized finite-dimensional supplier slice is sequentially compact.

Therefore the supplier-rooted subprogram has:

$$
\boxed{
\text{XTR}
+
\text{COM}
+
\text{ACTUAL RETURN}.
}
\tag{1.10}
$$

The third theorem is a positive-gap result.

Since:

$$
\mathfrak J
=
\mathsf O_{\rm PFET}
+
\mathcal M_{SV}
+
\widetilde{\mathcal S}^{(3)}
+
\mathsf{Paid}
+
\mathsf R_{\rm nat},
$$

and DCRP-15 places the supplier trace/residual gap inside the first/native-residual channels, there exists

$$
c_J>0
$$

such that every normalized supplier package satisfies

$$
\boxed{
\mathfrak J(d)
\ge
c_J.
}
\tag{1.11}
$$

Hence

$$
\boxed{
m_{\rm sup}
:=
\inf_{d\in\mathscr O_{\rm sup}}
\mathfrak J(d)
>
0.
}
\tag{1.12}
$$

Therefore:

$$
\boxed{
\textbf{
there is no zero-cost supplier-rooted minimal obstruction.
}
}
\tag{1.13}
$$

This is a genuine synchronization gain.

However it does **not** yet prove that the original MORP minimal value

$$
m_\ast
$$

is positive.

MORP-03 explicitly allows a genuine obstruction history to:

- temporarily deplete;
- transfer across channels;
- become visible;
- later regenerate/re-root into a new native-separated window.

Thus a hypothetical zero-cost minimal recurrent orbit could, logically, pass through a positive-cost supplier excursion and only return to the minimal level later.

Choosing the supplier itself as the return window does not preserve Minimal Return Rigidity unless one proves a supplier-specific nonnegative return-depletion inequality.

Therefore the critical NO-GO of this round is:

$$
\boxed{
\textbf{
supplier visibility}
\not\Rightarrow
\textbf{
minimal-orbit contradiction}
}
\tag{1.14}
$$

without an irreversibility/depletion theorem.

The next exact frontier is therefore:

$$
\boxed{
\textbf{
Supplier Excursion Irreversibility / Return-Depletion Lemma}.
}
\tag{1.15}
$$

A sufficient theorem would show that if an actual native-separated orbit starts near a zero-cost invisible window, passes through a local supplier event, and later returns to a zero-cost invisible window, then the complete excursion necessarily pays a fixed strictly positive nonnegative tax:

$$
\boxed{
\Delta_{\rm exc}
\ge
c_{\rm exc}>0.
}
\tag{1.16}
$$

If this is proved, MORP Minimal Return Rigidity gives immediately

$$
\Delta_{\rm exc}=0,
$$

a contradiction.

This is now the single closure-facing frontier of the supplier route.

---

# 2. MORP return semantics audited

MORP-03 defines actual Navier--Stokes evolution/restriction

$$
\mathsf E_{s\to t}
$$

and normalization

$$
\mathsf N_{\rm norm}.
$$

A candidate transition is

$$
\boxed{
\mathsf T
=
\mathsf N_{\rm norm}
\circ
\mathsf E.
}
\tag{2.1}
$$

MORP deliberately rejects rigid fixed-step invariance.

A legitimate obstruction may:

- partially deplete;
- transfer across channels;
- become source dominated;
- later re-root into a new dangerous/native-separated window.

Therefore the actual transition is a return/re-root transition.

A later window

$$
W'
$$

is a native return if

$$
\boxed{
d_{\rm nat}
(
D(W')
)
\ge1.
}
\tag{2.2}
$$

MORP-03 explicitly allows the canonical rule to choose:

1. the first later native-separated window;
2. the first later dangerous-certified native-separated window;
3. the next member of a fixed admissible extraction sequence.

The rule must be fixed before compactness/minimality is used.

The supplier stopping rule below satisfies exactly this semantic requirement once supplier native separation is proved.

---

# 3. Native distance on the fixed supplier window

MORP-01 defines

$$
\boxed{
d_{\rm nat}(D)
=
\operatorname{dist}_{\mathfrak X/\Gamma}
(
D,\Gamma
).
}
\tag{3.1}
$$

Here

$$
\Gamma
$$

contains only declared exact gauge/symmetry directions.

The supplier window from DCRP-15 is a fixed normalized finite-dimensional quotient.

Let

$$
Y_\ast
$$

denote that cleaned quotient.

Let

$$
\mathcal O_\ast^T
:
Y_\ast
\to
H_\ast
$$

be the selected trace map.

Let

$$
\mathcal R_\ast
:
Y_\ast
\to
Z_\ast^{res}
$$

be the concrete finite residual map after all exact quotient nulls have been removed.

Define

$$
\boxed{
\mathcal A_\ast
=
(
\mathcal O_\ast^T,
\mathcal R_\ast
).
}
\tag{3.2}
$$

This is a bounded linear map on the finite-dimensional cleaned quotient.

---

# 4. NEW THEOREM — supplier native separation

## Theorem 4.1

There exists

$$
a_{\rm sup}>0
$$

such that every DCRP-15 normalized supplier package

$$
d_q
$$

satisfies

$$
\boxed{
d_{\rm nat}(d_q)
\ge
a_{\rm sup}.
}
\tag{4.1}
$$

### Proof

DCRP-15 gives

$$
\boxed{
\|
\mathcal O_\ast^Td_q
\|
+
C_{\rm sup}
\|
\mathcal R_\ast d_q
\|
\ge
c_{\rm sup}\nu.
}
\tag{4.2}
$$

Choose a product norm on the target of

$$
\mathcal A_\ast.
$$

Then there is

$$
c_1>0
$$

with

$$
\boxed{
\|
\mathcal A_\ast d_q
\|
\ge
c_1\nu.
}
\tag{4.3}
$$

Since

$$
\mathcal A_\ast
$$

vanishes on exact quotient-null directions, it descends to

$$
Y_\ast.
$$

Boundedness gives

$$
\boxed{
\|
\mathcal A_\ast d
\|
\le
C_A
\|[d]\|_{Y_\ast}.
}
\tag{4.4}
$$

The quotient norm is an admissible realization of native distance on this fixed window, up to a fixed equivalence constant

$$
C_{\rm eq}.
$$

Therefore

$$
d_{\rm nat}(d_q)
\ge
\frac{
c_1
}{
C_AC_{\rm eq}
}
\nu.
$$

Set

$$
\boxed{
a_{\rm sup}
=
\frac{
c_1
}{
C_AC_{\rm eq}
}
\nu.
}
\tag{4.5}
$$

$$
\square
$$

Status:

$$
\boxed{
\textbf{PROVED on the fixed supplier finite-window quotient}.
}
$$

---

# 5. Homogeneous normalization to the unit obstruction slice

The supplier package is a tangent/native direction.

All linearized package constraints are homogeneous.

Therefore define

$$
\boxed{
\widehat d_q
=
a_{\rm sup}^{-1}
d_q.
}
\tag{5.1}
$$

Then

$$
\boxed{
d_{\rm nat}(\widehat d_q)
\ge1.
}
\tag{5.2}
$$

The normalization does not insert the dangerous/singular certificate.

It uses only the native quotient separation already extracted from the actual supplier package.

Thus it passes the MORP non-tautological extraction safety rule.

---

# 6. Uniform package bound from finite dimensionality

On the fixed finite-dimensional quotient

$$
Y_\ast,
$$

let

$$
\mathcal N_{\rm pkg}
$$

be any fixed compactness-control norm used for the supplier slice.

All norms on

$$
Y_\ast
$$

are equivalent.

Therefore there is a fixed constant

$$
C_N
$$

such that

$$
\boxed{
\mathcal N_{\rm pkg}(d)
\le
C_N
d_{\rm nat}(d)
}
\tag{6.1}
$$

after the exact gauge representative is fixed.

Apply to the unit-native supplier package.

One may additionally divide by the exact native norm rather than the lower constant

$$
a_{\rm sup}
$$

to obtain

$$
d_{\rm nat}=1.
$$

Then

$$
\boxed{
\mathcal N_{\rm pkg}
\le
C_\ast
}
\tag{6.2}
$$

with a universal constant for the fixed normalized supplier template.

Thus supplier-rooted packages belong to the MORP unit obstruction geometry.

Status:

$$
\boxed{
\textbf{PROVED on the fixed supplier window}.
}
$$

---

# 7. Supplier-rooted obstruction slice

Define

$$
\boxed{
\mathscr O_{\rm sup}
=
\left\{
d\in
\overline{\mathcal Y_{\rm sup}^{NS}}
:
d_{\rm nat}(d)\ge1,
\quad
\mathcal N_{\rm pkg}(d)\le C_\ast
\right\},
}
\tag{7.1}
$$

where

$$
\mathcal Y_{\rm sup}^{NS}
$$

consists of the actual finite-window tangent packages constructed from local supplier nonlinear increments.

Then

$$
\boxed{
\mathscr O_{\rm sup}
\subset
\mathscr O_1
}
\tag{7.2}
$$

provided the original MORP coordinate map includes the fixed supplier finite-window coordinates, which DCRP-14/15 constructed inside the declared trace/residual architecture.

DCRP-16 gives:

$$
\boxed{
T<\infty
\Longrightarrow
\mathscr O_{\rm sup}\ne\varnothing.
}
\tag{7.3}
$$

This is a concrete supplier-side XTR theorem.

Status:

$$
\boxed{
\textbf{PROVED for the supplier-rooted coordinate slice}.
}
$$

It does not prove universal XTR for every MORP extraction route.

---

# 8. Compactness of the supplier-rooted slice

The fixed normalized supplier quotient is finite dimensional.

The set

$$
\boxed{
\left\{
d:
d_{\rm nat}(d)=1,
\quad
\mathcal N_{\rm pkg}(d)\le C_\ast
\right\}
}
\tag{8.1}
$$

is bounded and closed modulo the exact fixed gauge.

Therefore it is compact.

Hence

$$
\boxed{
\mathscr O_{\rm sup}
\text{ is sequentially compact after fixed native normalization}.
}
\tag{8.2}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

Thus the supplier slice does not carry the original infinite-dimensional COM difficulty.

---

# 9. Canonical supplier stopping rule

Fix once and for all:

- an integer dyadic scale gap

  $$
  L\ge1;
  $$

- a deterministic spatial tie-breaking convention;
- a deterministic time tie-breaking convention.

Let an actual supplier-rooted state have current supplier frequency index

$$
q_n.
$$

Define the admissible future supplier set

$$
\mathfrak S_n
$$

to consist of local supplier events

$$
(t,x,q)
$$

from the same actual singular solution satisfying

$$
\boxed{
t>t_n,
}
\tag{9.1}
$$

$$
\boxed{
q\ge q_n+L,
}
\tag{9.2}
$$

and belonging to a prescribed singular-rooted neighborhood whose radius tends to zero with the extraction level.

DCRP-16 gives supplier events with

$$
q\to\infty,
\qquad
t\uparrow T,
\qquad
x\to x_\ast.
$$

Therefore

$$
\boxed{
\mathfrak S_n\ne\varnothing
}
\tag{9.3}
$$

for every sufficiently late supplier node.

Define

$$
\boxed{
\mathsf S_{\rm sup}
}
$$

to select the smallest admissible dyadic index, then the earliest admissible threshold time, then the declared spatial tie-breaker.

The rule is declared before any compactness/minimality argument.

---

# 10. NEW THEOREM — actual supplier return realization

## Theorem 10.1

Along a hypothetical singular history, the supplier stopping rule defines an infinite actual same-history return sequence

$$
\boxed{
D_1^{sup},
D_2^{sup},
D_3^{sup},
\ldots
}
\tag{10.1}
$$

with

$$
\boxed{
q_{n+1}\ge q_n+L,
}
\tag{10.2}
$$

$$
\boxed{
t_{n+1}>t_n,
}
\tag{10.3}
$$

$$
\boxed{
t_n\uparrow T,
}
\tag{10.4}
$$

and

$$
\boxed{
x_n\to x_\ast.
}
\tag{10.5}
$$

After the fixed supplier normalization,

$$
\boxed{
\widehat D_n^{sup}\in\mathscr O_{\rm sup}.
}
\tag{10.6}
$$

Thus

$$
\boxed{
\mathsf T_{\rm sup}
:
\mathscr O_{\rm sup}^{act}
\to
\mathscr O_{\rm sup}^{act}
}
\tag{10.7}
$$

is an actual original-solution return/re-root map.

### Proof

Existence of arbitrarily late/higher local supplier events is DCRP-16.

The deterministic selection makes the return rule canonical.

The event is taken from the same original Navier--Stokes solution.

Sections 4--8 place every normalized supplier package in

$$
\mathscr O_{\rm sup}.
$$

Iteration gives the infinite actual chain.

$$
\square
$$

Status:

$$
\boxed{
\textbf{PROVED conditional only on the DCRP-16 local-supplier theorem already established in the project}.
}
$$

---

# 11. Relation to MORP-03 actual-return semantics

MORP-03 permits exactly the following return-rule forms:

- first later native-separated window;
- first later dangerous/native-separated window;
- next member of a fixed admissible extraction sequence.

The supplier stopping rule is of the second/third type after Sections 4--7 establish native separation.

Therefore

$$
\boxed{
\textbf{
the supplier stopping rule is semantically admissible as a MORP actual return/re-root rule.
}
}
\tag{11.1}
$$

This closes the purely semantic synchronization problem.

It does not yet prove a return-depletion inequality.

---

# 12. Supplier-rooted positive cost gap

The MORP extended cost is

$$
\boxed{
\mathfrak J
=
\mathsf O_{\rm PFET}
+
\mathcal M_{SV}
+
\widetilde{\mathcal S}^{(3)}
+
\mathsf{Paid}
+
\mathsf R_{\rm nat}.
}
\tag{12.1}
$$

On the supplier package, DCRP-15 gives a fixed trace-or-residual gap.

The selected trace contributes to

$$
\mathsf O_{\rm PFET},
$$

while the finite-window realization residual contributes to

$$
\mathsf R_{\rm nat}
$$

or the declared local paid/residual ledger.

Hence, after unit native normalization and finite-dimensional norm equivalence, there is

$$
\boxed{
c_J>0
}
\tag{12.2}
$$

such that

$$
\boxed{
\mathfrak J(d)
\ge
c_J
\qquad
\forall d\in\mathscr O_{\rm sup}.
}
\tag{12.3}
$$

Therefore

$$
\boxed{
m_{\rm sup}
=
\inf_{
d\in\mathscr O_{\rm sup}
}
\mathfrak J(d)
\ge
c_J>0.
}
\tag{12.4}
$$

Status:

$$
\boxed{
\textbf{PROVED on the supplier-rooted slice}.
}
$$

---

# 13. Corollary — no zero-cost supplier-rooted minimal obstruction

There is no

$$
d_\ast^{sup}\in\mathscr O_{\rm sup}
$$

with

$$
\boxed{
\mathfrak J(d_\ast^{sup})=0.
}
\tag{13.1}
$$

Equivalently,

$$
\boxed{
\mathscr O_{\rm sup}
\cap
\ker\mathfrak J
=
\varnothing.
}
\tag{13.2}
$$

Thus the MORP minimal-invisible branch does not exist **inside the supplier-rooted slice**.

This is a true positive-gap result.

---

# 14. Why this does not imply the global MORP minimal value is positive

The original obstruction slice

$$
\mathscr O_1
$$

is larger than

$$
\mathscr O_{\rm sup}.
$$

Therefore

$$
\boxed{
m_\ast
=
\inf_{\mathscr O_1}\mathfrak J
\le
\inf_{\mathscr O_{\rm sup}}\mathfrak J
=
m_{\rm sup}.
}
\tag{14.1}
$$

A positive supplier gap does not by itself imply

$$
m_\ast>0.
$$

A minimizing invisible sequence could live in other windows/states of the same actual singular history.

Thus:

$$
\boxed{
\textbf{
supplier XTR/COM/visibility}
\neq
\textbf{
global MORP coercive gap}.
}
}
\tag{14.2}
$$

---

# 15. CRITICAL NO-GO — temporary supplier visibility is compatible with MORP semantics

MORP-03 explicitly states that fixed-step invariance is too strong.

A genuine dangerous trajectory may:

- partially deplete;
- transfer across channels;
- become source dominated;
- later re-root into a new dangerous/native-separated window.

Therefore a hypothetical minimal zero-cost orbit may, logically, have the pattern

$$
\boxed{
D_n^{min}
\longrightarrow
S_n^{sup}
\longrightarrow
D_{n+1}^{min},
}
\tag{15.1}
$$

where

$$
\boxed{
\mathfrak J(D_n^{min})=0,
}
\tag{15.2}
$$

$$
\boxed{
\mathfrak J(S_n^{sup})\ge c_J,
}
\tag{15.3}
$$

and

$$
\boxed{
\mathfrak J(D_{n+1}^{min})=0.
}
\tag{15.4}
$$

Nothing in minimality alone forbids the middle excursion.

Thus the following inference is invalid:

$$
\boxed{
\text{supplier event exists}
\Longrightarrow
\text{minimal zero-cost orbit impossible}.
}
\tag{15.5}
$$

Status:

$$
\boxed{
\textbf{NO-GO / LOGICAL CORRECTION}.
}
$$

This is the principal result of the synchronization audit.

---

# 16. Why choosing the supplier itself as the MORP return is not enough

MORP Minimal Return Rigidity assumes

$$
\boxed{
\mathfrak J
(
\mathsf T_{\rm ret}D
)
+
\Delta_{\rm ret}(D)
\le
\mathfrak J(D),
}
\tag{16.1}
$$

with

$$
\Delta_{\rm ret}\ge0.
$$

Suppose

$$
\mathfrak J(D)=0
$$

and choose the later supplier package as

$$
\mathsf T_{\rm ret}D.
$$

But supplier synchronization gives

$$
\mathfrak J(\mathsf T_{\rm ret}D)\ge c_J>0.
$$

Then (16.1) cannot hold.

Therefore:

$$
\boxed{
\textbf{
supplier stopping is an admissible actual return rule,
but it is not automatically a depletion-compatible minimal return rule.
}
}
\tag{16.2}
$$

This distinction must not be hidden.

---

# 17. Actual supplier synchronization achieved

Although supplier stopping does not yet preserve minimality, the following parts of the synchronization problem are now closed:

### actual-history realization

$$
\boxed{
\mathsf T_{\rm sup}
\text{ is generated by one original singular solution}.
}
\tag{17.1}
$$

### local singular-point capture

$$
\boxed{
x_n\to x_\ast.
}
\tag{17.2}
$$

### scale advance

$$
\boxed{
q_{n+1}\ge q_n+L.
}
\tag{17.3}
$$

### native separation

$$
\boxed{
d_{\rm nat}(D_n^{sup})\ge1.
}
\tag{17.4}
$$

### normalized compactness

$$
\boxed{
\mathcal N_{\rm pkg}(D_n^{sup})\le C_\ast.
}
\tag{17.5}
$$

### visibility

$$
\boxed{
\mathfrak J(D_n^{sup})\ge c_J.
}
\tag{17.6}
$$

The only missing ingredient for collision with Minimal Return Rigidity is an irreversible tax across the **complete excursion**.

---

# 18. Supplier excursion

Let

$$
D_n^-
$$

be one native-separated invisible/minimal window.

Let

$$
S_n
$$

be the next local supplier event selected by the supplier stopping rule.

If recurrence exists, let

$$
D_n^+
$$

be the first later native-separated window that returns to the minimal/invisible class.

The complete excursion is

$$
\boxed{
D_n^-
\longrightarrow
S_n
\longrightarrow
D_n^+.
}
\tag{18.1}
$$

A supplier-excursion return map should be defined by

$$
\boxed{
\mathsf T_{\rm exc}(D_n^-)
=
D_n^+.
}
\tag{18.2}
$$

If no such

$$
D_n^+
$$

exists, then the recurrent minimal branch already fails.

Thus only the case in which the system becomes invisible again needs analysis.

---

# 19. Target depletion identity

The desired supplier-specific return law is

$$
\boxed{
\mathfrak J(D_n^+)
+
\Delta_{\rm exc}(D_n^-;S_n;D_n^+)
\le
\mathfrak J(D_n^-),
}
\tag{19.1}
$$

with

$$
\boxed{
\Delta_{\rm exc}\ge0.
}
\tag{19.2}
$$

The crucial new theorem must prove

$$
\boxed{
\Delta_{\rm exc}
\ge
c_{\rm exc}
>
0
}
\tag{19.3}
$$

whenever the middle state contains the supplier trace/residual gap

$$
\mathfrak J(S_n)\ge c_J.
$$

Then for a minimal zero-cost orbit,

$$
\mathfrak J(D_n^-)
=
\mathfrak J(D_n^+)
=
0,
$$

and (19.1) gives

$$
\Delta_{\rm exc}\le0.
$$

Combined with (19.3),

$$
\boxed{\bot.}
$$

This would close the actual recurrent minimal branch.

---

# 20. What can provide irreversibility?

The supplier route has already produced several candidate nonnegative ledgers.

## viscous supplier dissipation

During a supplier-shell energy growth excursion,

$$
\nu
\int
\|\nabla u_Q\|_2^2
\,dt
\ge0.
$$

The difficulty is obtaining a uniform scale-critical lower bound.

## paid backscatter

DCRP-11 gives a heat-filter alternative:

$$
\text{forward work}
\vee
\text{backscatter}.
$$

Backscatter is already on the paid side.

The forward branch remains potentially reversible.

## finite-window realization residual

DCRP-15 gives

$$
O_W^T
+
C
\mathcal B_{\rm sup}^{res}
\ge
c\nu.
$$

If the supplier is invisible in the selected trace, the residual side is already paid/native.

The hard case is a supplier that is genuinely trace-visible but later becomes invisible with negligible residual.

## diffusion between visible and invisible states

If supplier trace amplitude disappears before the next invisible return, viscosity and nonlinear transfer must remove it.

One must show that the disappearance cannot be achieved entirely by sign-indefinite forward redistribution without a strictly positive return tax.

This is the core irreversibility question.

---

# 21. Heat-band excursion identity

DCRP-11 constructed a positive scale-critical heat-band energy

$$
\mathcal B_\lambda^{a,b}(t).
$$

A supplier event forces

$$
\boxed{
\mathcal B_\lambda^{a,b}
\ge
\beta_0\nu^2.
}
\tag{21.1}
$$

A complete excursion from a low-band state to supplier and back to low band has at least one rise and one fall.

The exact identity is

$$
\boxed{
\frac d{dt}
\mathcal B_\lambda^{a,b}
+
\nu\lambda
(D_a-D_b)
+
\lambda(F_{s_a}-F_{s_b})
=
0.
}
\tag{21.2}
$$

The first nontrivial positive term is

$$
\boxed{
\nu\lambda
(D_a-D_b)\ge0.
}
\tag{21.3}
$$

The next route should attempt to prove that a fixed-amplitude excursion cannot have

$$
\boxed{
\nu\lambda
\int_{\rm excursion}
(D_a-D_b)\,dt
\to0
}
\tag{21.4}
$$

while both endpoint observation/residual costs vanish.

If such a lower bound holds, it is the desired irreversible tax.

---

# 22. Why a naive total-variation argument is insufficient

The band energy may rise through forward transfer at the coarse boundary and later fall through forward transfer at the fine boundary.

Thus an energy packet can pass through the band without backscatter.

This is the normal forward-cascade picture.

Therefore

$$
\boxed{
\text{band rises and falls}
\not\Rightarrow
\text{backscatter}.
}
\tag{22.1}
$$

Likewise a fixed amount of energy can pass through increasingly small scales while the raw viscous payment remains summable.

This is the old critical-barrier accumulation problem.

Hence the irreversibility theorem must use additional supplier structure:

- dissipation-wavenumber location;
- finite trace amplitude;
- first-crossing geometry;
- actual return to a native invisible state;
- or repeated recurrence/minimality.

---

# 23. Potential route — supplier residence time

At the supplier boundary,

$$
\lambda^{-1}
\|u_Q\|_\infty
\gtrsim\nu.
$$

If one can prove a scale-invariant lower bound on normalized residence time,

$$
\boxed{
\nu\lambda^2
|I_{\rm sup}|
\ge
\tau_0>0,
}
\tag{23.1}
$$

while the shell remains above a fixed fraction of critical amplitude, then

$$
\|u_Q\|_2^2
\gtrsim
\nu^2\lambda^{-1}
$$

would give

$$
\boxed{
\nu\lambda
\int_{I_{\rm sup}}
\|\nabla u_Q\|_2^2
\,dt
\gtrsim
\nu^2.
}
\tag{23.2}
$$

This would produce the desired non-summable scale-critical excursion tax.

The current corpus does not yet provide (23.1).

The shell may, in principle, spike on a much shorter normalized time interval.

Thus residence-time rigidity is one possible next sublemma.

---

# 24. Potential route — trace disappearance rate

DCRP-14 gives a fixed finite-dimensional supplier trace

$$
\boxed{
\|\Pi_{H_\ast}h(t_{\rm sup})\|
\ge
c\nu.
}
\tag{24.1}
$$

Suppose the next minimal invisible return satisfies

$$
\boxed{
\|\Pi_{H_\ast}h(t_{\rm ret})\|
\approx0.
}
\tag{24.2}
$$

Because

$$
H_\ast
$$

is finite dimensional and fixed in normalized coordinates, one can differentiate each trace coefficient along the normalized forced Stokes/Navier--Stokes increment equation.

A viable theorem would bound

$$
\boxed{
\left|
\frac d{d\tau}
\Pi_{H_\ast}h
\right|
}
\tag{24.3}
$$

by:

- paid flux;
- viscosity;
- finite-window residual;
- low-mode supplier activity.

If all paid/residual terms are small, a fixed drop

$$
c\nu\to0
$$

would require a positive normalized time.

Combining with viscous occupation may yield a strict return tax.

This converts the irreversibility problem into a finite-dimensional trace ODE estimate.

This is currently the most attractive route.

---

# 25. External critical-element calibration

Classical critical-element/profile-decomposition work shows that, under a hypothetical nonempty blowup class and suitable critical-space compactness, minimal singular objects can be extracted.

This supports the general MORP philosophy that a minimizing/critical orbit is meaningful once the topology and transition are controlled.

However those results do not imply that an arbitrary supplier stopping time preserves the minimal element.

Therefore no external theorem closes the excursion-depletion gap automatically.

The issue identified in Sections 15--24 is genuine.

---

# 26. Updated proof-state diagram

The current supplier route is now

$$
\boxed{
\begin{aligned}
\text{finite-time singular point}
&\Longrightarrow
\text{local supplier sequence}\\
&\Longrightarrow
\text{actual supplier nonlinear increment}\\
&\Longrightarrow
\text{finite-window trace/residual gap}\\
&\Longrightarrow
\text{supplier-rooted native obstruction slice}\\
&\Longrightarrow
\text{actual supplier return chain}.
\end{aligned}
}
\tag{26.1}
$$

Every supplier-rooted node satisfies

$$
\boxed{
\mathfrak J\ge c_J>0.
}
\tag{26.2}
$$

But a hypothetical minimal recurrent orbit may have

$$
\boxed{
0
\to
c_J
\to
0
}
\tag{26.3}
$$

across one excursion.

The final unresolved arrow is therefore

$$
\boxed{
\text{visible supplier excursion}
\Longrightarrow
\text{strict irreversible return tax}.
}
\tag{26.4}
$$

---

# 27. What is closed in this round

## supplier XTR

A first singular point generates a non-tautological native-separated supplier package.

## supplier COM

After fixed normalization, the supplier package lies in one fixed finite-dimensional compact quotient.

## supplier ACTUAL RETURN

The local supplier stopping rule yields an actual same-history infinite return/re-root chain.

## supplier positive gap

The supplier-rooted obstruction slice satisfies

$$
m_{\rm sup}>0.
$$

These are genuine reductions of the original MORP XTR/COM/TR difficulties on the supplier subprogram.

---

# 28. What remains open

The single closure-facing gap is

$$
\boxed{
\textbf{
Supplier Excursion Irreversibility / Return-Depletion.
}
}
$$

One must prove that a zero-cost minimal/native orbit cannot pass through a fixed supplier trace event and later return to zero cost without paying a positive nonnegative tax.

This is not a compactness issue.

It is now a dynamical irreversibility issue.

---

# 29. Next exact attack

The next round should attack a finite-dimensional trace version first.

Let

$$
a_j(\tau)
=
\langle
h(\tau),
\psi_j
\rangle,
\qquad
j=1,\ldots,N_\ast,
$$

for an orthonormal basis of

$$
H_\ast.
$$

At supplier time,

$$
\boxed{
|a(\tau_{\rm sup})|
\ge
c\nu.
}
\tag{29.1}
$$

At a true combined-invisible minimal return,

$$
\boxed{
|a(\tau_{\rm ret})|
\to0.
}
\tag{29.2}
$$

Differentiate using the normalized forced supplier increment equation.

The target estimate is

$$
\boxed{
\left|
a'(\tau)
+
\nu
M_\ast a(\tau)
\right|
\le
C
\left(
\mathsf{Flux}_{paid}
+
\mathsf{Residual}_{nat}
\right),
}
\tag{29.3}
$$

where

$$
M_\ast
$$

is the positive finite-dimensional Stokes/Laplacian matrix on

$$
H_\ast.
$$

If the right-hand side vanishes, the trace decays only through strictly positive viscosity, producing an explicit positive dissipation integral.

If the right side is nonzero, it is already paid/native.

A successful estimate would yield

$$
\boxed{
\Delta_{\rm exc}
\ge
c_{\rm exc}\nu^2.
}
\tag{29.4}
$$

That would collide directly with MORP's zero-return-tax equality.

This is the next exact attack.

---

# 30. End state

The supplier stopping-time synchronization problem is now resolved in the following precise sense:

$$
\boxed{
\textbf{
local supplier events define an actual,
native-separated, compact, recurrent stopping chain.
}
}
$$

Every normalized supplier node has a uniform positive extended cost

$$
\boxed{
\mathfrak J\ge c_J.
}
$$

Therefore there is no zero-cost supplier-rooted minimal obstruction.

But MORP explicitly allows temporary visible excursions before a later return.

Thus the proof cannot stop at supplier visibility.

The next and single frontier is

$$
\boxed{
\textbf{
Supplier Excursion Irreversibility / Return-Depletion Lemma}.
}
$$

The preferred next route is the finite-dimensional supplier-trace evolution estimate:

$$
\boxed{
\text{trace drop}
\Longrightarrow
\text{viscous payment}
\ \vee\
\text{paid/native forcing}.
}
$$

If this is proved with a scale-uniform positive lower bound, the actual recurrent zero-cost MORP branch is eliminated.
