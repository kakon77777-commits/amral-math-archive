# CSM Paper 01
# Globality Typing and Domain Stratification
## Globality Typing and Domain Stratification in Closure-Space Mathematics

**Version:** v0.1  
**Date:** 2026-08-27  
**Series:** Closure-Space Mathematics / CSM  
**Status:** Globality Typing Paper / Domain and Quantifier-Scope Paper  
**Canonical source:** UTF-8 Markdown  
**Canonical math delimiters:** `$...$` and `$$...$$`  
**Research Status:** A direct extension of CSM Paper 00; establishes rules for globality typing, domain stratification, scope promotion, and cross-domain proof-transfer. This document is not a completed proof of any unsolved Navier--Stokes problem.

---

# Abstract

"Global" is often used as a single intensity modifier in mathematical and scientific discourse, but different global claims may actually quantify over completely different axes: time, space, initial data classes, boundary conditions, forcing, parameters, solution notions, regularity classes, equation families, representation families, formal proof regimes, or physical realization domains. If these differences are ignored, it is easy to erroneously upgrade "holds for all time for a fixed equation" to "holds for the entire equation family," or to falsely elevate a "formal PDE theorem" to "all physical realizations have been proven."

This paper establishes the **Globality Typing Principle** of Closure-Space Mathematics (CSM). Its core assertion is that globality is not a single boolean value, nor is it an unconditionally sortable intensity; rather, it is a typed profile carrying a quantifier scope, domain signature, solution semantics, representation, and interpretation metadata.

This paper defines:

$$
\boxed{
\mathsf{ScopeContract}(Q)
=
\left\langle
\mathsf{DomSig}(Q),
\mathsf{Quant}(Q),
\mathsf{Sem}(Q),
\mathsf{Rep}(Q),
\mathsf{ProofReg}(Q)
\right\rangle.
}
$$

And uses:

$$
\boxed{
\mathsf{GProf}(Q)
=
\left\langle
G_t,
G_x,
G_{\rm data},
G_{\rm sol},
G_{\rm bdry},
G_{\rm force},
G_{\rm par},
G_{\rm reg},
G_{\rm eq},
G_{\rm rep},
G_{\rm phys},
G_{\rm proof}
\right\rangle
}
$$

to represent the globality profile of a proposition.

The first non-collapse principle of this paper is:

$$
\boxed{
\text{Global-in-time}
\neq
\text{Global-across-data}
\neq
\text{Global-across-equations}
\neq
\text{Global-across-physical-realizations}.
}
$$

The second principle is:

$$
\boxed{
\text{Theorem Strengthening}
\neq
\text{Scope Expansion}
\neq
\text{Model Extension}.
}
$$

The third principle is: any theorem promotion from a scope $D_1$ to a broader scope $D_2$ must carry a scope/globality promotion certificate, and cannot be automatically upgraded simply because two problems possess similar equations, identical names, or share local forms.

Navier--Stokes is used as the first large-scale domain-stratification instance. This paper separates the formal/Clay mathematical NS, the physical NS realization domain, and the generalized NS-like equation family, pointing out that the "global" in the Clay problem primarily refers to global-in-time extension within a fixed formal problem and universal quantification over a specified data class; this still does not equate to equation-family globality, nor does it equate to physical-realization globality. The generalized NS-like family must be parameterized by an explicit signature, and all systems that "look like NS" cannot be conflated into a single set.

Finally, this paper connects globality typing back to the CSM closure-space frontier: an unclosed frontier must not only ask "which proposition is still OPEN," but also "which globality axis has not yet been closed." Therefore, the subsequent NS Relative-Global Closure Graph will no longer solely contain proof-route boundaries, but will include a **scope frontier**, a **family-extension frontier**, and an **interpretation frontier**.

---

# 0. Research Status and Non-Claims

This paper does not claim:

1. That "global" possesses a unique, natural numerical intensity;
2. That all globality axes can form a single total order;
3. That inclusion between different PDEs, different solution notions, or different physical models can be established solely by name similarity;
4. That a formal mathematical theorem automatically equates to physical truth;
5. That the generalized NS-like equation family already has a unique canonical boundary;
6. That the Clay Navier--Stokes problem is being redefined;
7. That this paper has proven Clay Navier--Stokes global regularity;
8. That this paper has proven the universal regularity of any generalized NS-like family;
9. That physical NS realizations can be completely covered by a single formal model;
10. That domain stratification itself can replace theorem-level proofs;
11. That a scope expansion certificate always exists;
12. That relative-global closure equals absolute mathematical completeness.

This paper only establishes:

- The typed quantifier semantics of globality;
- Domain signatures;
- Scope contracts;
- Globality profiles;
- Scope comparability and non-comparability;
- The separation of scope restriction / expansion / model extension;
- Certificate conditions for cross-domain theorem transfer;
- The first version of the three-domain stratification for NS and the generalized family signature;
- The coupling of the scope frontier with the closure-space.

---

# 1. Why "Global" is Not Enough as a Single Word

Consider two statements:

1. For a fixed PDE, solutions exist for all finite times;
2. For an entire family of PDEs, all members possess the same property.

Both might be referred to as "global" in natural language, but their quantifier structures are completely different.

The first is closer to:

$$
\forall t\in T,
\qquad
P(u,t),
$$

while the second is:

$$
\forall E\in\mathcal E,
\qquad
P(E).
$$

If we also include initial data:

$$
\forall u_0\in\mathcal D,
\quad
\forall t\in T,
\qquad
P(E,u_0,t),
$$

its scope changes yet again.

Therefore, CSM reconstructs "global" from an adjective into a **quantifier-scope object**.

---

# 2. Scope Contract

For a proposition $Q$, define:

$$
\boxed{
\mathsf{ScopeContract}(Q)
=
\left\langle
\mathsf{DomSig}(Q),
\mathsf{Quant}(Q),
\mathsf{Sem}(Q),
\mathsf{Rep}(Q),
\mathsf{ProofReg}(Q)
\right\rangle.
}
$$

Where:

- $\mathsf{DomSig}$: Domain signatures for equations, space, time, data, boundaries, forcing, parameters, etc.;
- $\mathsf{Quant}$: Quantifiers and uniformity requirements for each axis;
- $\mathsf{Sem}$: Solution notions, equality / equivalence, regularity targets;
- $\mathsf{Rep}$: Representations and projections used;
- $\mathsf{ProofReg}$: Formal systems, admissibility, external theorem sets, and proof verification regimes.

If a theorem claim lacks sufficient fields to determine its scope, CSM denotes it as:

$$
\boxed{
\mathsf{ILL\_SCOPED}.
}
$$

---

# 3. Domain Signature

Version 1:

$$
\boxed{
\mathsf{DomSig}(Q)
=
\left\langle
\mathcal E,
\mathcal X,
\mathcal T,
\mathcal D,
\mathcal S,
\mathcal B,
\mathcal F,
\mathcal P,
\mathcal R,
\mathcal I
\right\rangle.
}
$$

Where:

- $\mathcal E$: equation / operator domain;
- $\mathcal X$: spatial domain / geometry;
- $\mathcal T$: time domain;
- $\mathcal D$: initial / admissible data class;
- $\mathcal S$: solution notion;
- $\mathcal B$: boundary family;
- $\mathcal F$: forcing family;
- $\mathcal P$: parameter / coefficient domain;
- $\mathcal R$: regularity / topology / norm target;
- $\mathcal I$: interpretation / realization context.

CSM does not require all problems to use every field, but any undeclared field cannot be defaulted to "for all possible cases."

---

# 4. Quantifier Envelope

For each axis $a$, define:

$$
\mathsf{Quant}_a(Q)
=
\left\langle
\mathsf{Mode}_a,
\mathsf{Set}_a,
\mathsf{Uniformity}_a
\right\rangle.
$$

$\mathsf{Mode}_a$ may include:

- `all`;
- `exists`;
- `generic`;
- `almost-everywhere`;
- `conditional`;
- `asymptotic`;
- `unknown`.

Thus, even if two theorems both use the word "global," as long as their quantifier envelopes differ, they cannot be directly treated as the same claim.

---

# 5. Globality Profile

Define:

$$
\boxed{
\mathsf{GProf}(Q)
=
\left\langle
G_t,
G_x,
G_{\rm data},
G_{\rm sol},
G_{\rm bdry},
G_{\rm force},
G_{\rm par},
G_{\rm reg},
G_{\rm eq},
G_{\rm rep},
G_{\rm phys},
G_{\rm proof}
\right\rangle.
}
$$

Each component is not a simple $0/1$, but a scope descriptor relative to the declared domain.

Version 1 descriptors:

$$
G_a
\in
\{
\mathsf{LOCAL},
\mathsf{PARTIAL},
\mathsf{FULL}_{D_a},
\mathsf{FAMILY}_{\Sigma},
\mathsf{OPEN},
\mathsf{UNKNOWN}
\}.
$$

Where:

$$
\mathsf{FULL}_{D_a}
$$

only indicates universal validity over the **declared** $D_a$, not universal validity over all possible domains.

This is one of the most important semantic restrictions in this paper.

---

# 6. Globality Typing Principle

CSM defines the:

$$
\boxed{
\textbf{Globality Typing Principle}
}
$$

Any global claim must be reducible to a valid $\mathsf{ScopeContract}$ and $\mathsf{GProf}$.

Therefore:

$$
\boxed{
\text{Global-in-time}
\not\Rightarrow
\text{Global-across-data}.
}
$$

$$
\boxed{
\text{Global-across-data}
\not\Rightarrow
\text{Global-across-equations}.
}
$$

$$
\boxed{
\text{Global-across-equations}
\not\Rightarrow
\text{Global-across-physical-realizations}.
}
$$

Unless there is an additional typed promotion certificate.

---

# 7. Time Globality

For a fixed formal problem:

$$
Q(E,u_0):
\qquad
\forall t\in\mathcal T,
\quad
P(E,u_0,t).
$$

If:

$$
\mathcal T=[0,\infty),
$$

it can be called a global-in-time claim under that formal scope.

But this does not automatically change:

- the equation $E$;
- the data class;
- the solution notion;
- the boundary / forcing;
- the physical interpretation.

Thus, time globality only elevates $G_t$.

---

# 8. Spatial Globality

A "whole-space problem" and "all possible geometries" are not the same thing.

If we fix:

$$
\mathcal X=\mathbb R^d,
$$

then a theorem holding for the entire spatial domain of $\mathbb R^d$ can only be written as:

$$
G_x=\mathsf{FULL}_{\mathbb R^d}.
$$

It does not imply:

$$
G_x=\mathsf{FULL}_{\text{all manifolds / domains}}.
$$

Therefore, whole-space is a spatial-domain choice, not a geometry-family universal quantifier.

---

# 9. Data-Class Globality

If a theorem holds for all:

$$
u_0\in\mathcal D_0
$$

then:

$$
G_{\rm data}=\mathsf{FULL}_{\mathcal D_0}.
$$

But if:

$$
\mathcal D_0\subsetneq\mathcal D_1,
$$

one cannot directly obtain:

$$
\mathsf{FULL}_{\mathcal D_1}.
$$

This is a typical scope expansion, not a standard theorem restatement.

---

# 10. Solution-Notion Globality

The same PDE may have different solution notions:

$$
\mathcal S
=
\{
\text{classical},
\text{strong},
\text{mild},
\text{weak},
\text{suitable},
\ldots
\}.
$$

This paper does not claim that these notions possess a fixed implication hierarchy across all PDEs.

Any:

$$
Q_{\mathcal S_1}
\Rightarrow
Q_{\mathcal S_2}
$$

must be established by known theorems or certificates within the specified problem.

Therefore:

$$
\boxed{
\text{same equation}
\neq
\text{same theorem domain}.
}
$$

---

# 11. Boundary and Forcing Globality

An unforced theorem:

$$
F=0
$$

does not automatically upgrade to a forced theorem.

Similarly:

$$
\mathcal B=\text{periodic}
$$

and:

$$
\mathcal B=\text{no-slip bounded domain}
$$

are different domain signatures.

Therefore:

$$
G_{\rm force}
$$

and:

$$
G_{\rm bdry}
$$

must be recorded independently.

---

# 12. Parameter Globality

For a parameter:

$$
\lambda\in\Lambda,
$$

if the theorem is:

$$
\forall\lambda\in\Lambda,
\quad
P(\lambda),
$$

and the proof constants are uniform with respect to $\lambda$, then a stronger parameter-globality can be recorded.

But if it is merely pointwise:

$$
\forall\lambda,
\quad
\exists C_\lambda,
$$

it is different from the existence of a uniform constant:

$$
\exists C,
\quad
\forall\lambda
$$

Therefore, CSM treats **quantifier order** as part of the globality metadata.

---

# 13. Equation-Family Globality

This is the main layer newly added in this paper.

A theorem for a fixed single equation:

$$
E_0
$$

is not equivalent to a theorem for an equation family:

$$
\mathcal E_{\Sigma}
$$

An equation family must be defined by a signature $\Sigma$, for example:

$$
\Sigma
=
\left\langle
\text{dimension},
\text{transport},
\text{constraint},
\text{dissipation},
\text{projection},
\text{forcing},
\text{boundary},
\text{constitutive class}
\right\rangle.
$$

Only after $\Sigma$ has been explicitly declared is:

$$
\mathsf{FAMILY}_{\Sigma}
$$

a meaningful globality descriptor.

---

# 14. Representation Globality

A proof succeeding in representation $\rho_1$ does not mean the same proof object can be reconstructed in all representations.

Conversely, a search failure under a certain representation does not imply failure across all semantically equivalent representations.

Therefore:

$$
G_{\rm rep}
$$

primarily describes:

- whether the theorem is representation-independent;
- whether the proof certificate can be reconstructed across representations;
- whether a search failure is merely representation-local.

This paper maintains:

$$
\boxed{
\text{Mathematical Identity}
\neq
\text{Search Representation Identity}.
}
$$

---

# 15. Proof-Regime Globality

Formal proof regimes are also scopes.

Let:

$$
\Theta_1,
\Theta_2
$$

be different theorem/proof regimes.

That:

$$
\Theta_1\vdash Q
$$

holds does not equate to:

$$
\Theta_2\vdash Q.
$$

However, if $\Theta_2$ is a conservative extension or already has a formal embedding theorem, a corresponding bridge can be established.

CSM does not assume such bridges on its own.

---

# 16. Physical-Realization Globality

This axis is not a simple set inclusion.

A formal model:

$$
M
$$

and a physical realization:

$$
R
$$

require an interpretation / idealization relation between them:

$$
M
\xleftrightarrow[
\mathsf{Idealize}
]{
\mathsf{Interpret}
}
R.
$$

These relations can be partial, scale-dependent, regime-dependent, or possess model discrepancy.

Therefore:

$$
\boxed{
\operatorname{Prove}(M)
\not\Rightarrow
\operatorname{Prove}(R).
}
$$

Unless the operational meaning of "Prove$(R)$" is separately defined and the interpretation bridge is proven sufficient to carry the inference.

---

# 17. Three Types of "Stronger" Must Not Be Mixed

Consider theorem $Q_0$.

## 17.1 Theorem strengthening

Within the same scope, the conclusion becomes stronger:

$$
Q_1\Rightarrow Q_0,
$$

but the scope remains unchanged.

## 17.2 Scope expansion

The form of the conclusion is largely the same, but the domain of quantification is broadened:

$$
D_0\subsetneq D_1.
$$

## 17.3 Model extension

The model itself is rewritten:

$$
E_0
\mapsto
E_1.
$$

The three must be separated:

$$
\boxed{
\text{Theorem Strengthening}
\neq
\text{Scope Expansion}
\neq
\text{Model Extension}.
}
$$

---

# 18. Scope Restriction

If:

$$
D_1\subseteq D_2,
$$

and the theorem:

$$
\forall x\in D_2,
\quad
Q(x)
$$

is proven, then under the same semantics it can be restricted to:

$$
\forall x\in D_1,
\quad
Q(x).
$$

This direction is called:

$$
\mathsf{ScopeRestrict}.
$$

It is generally safer than scope expansion, but still requires that the theorem target and semantics remain unchanged during the restriction process.

---

# 19. Scope Expansion

In the opposite direction, when:

$$
D_1\subsetneq D_2
$$

then:

$$
\forall x\in D_1,
Q(x)
$$

does not automatically imply:

$$
\forall x\in D_2,
Q(x).
$$

CSM refers to this illegal upgrade as:

$$
\boxed{
\mathsf{ScopeLeak}.
}
$$

---

# 20. Globality Promotion Certificate

To promote from $D_1$ to $D_2$, define:

$$
\boxed{
\mathsf{GPCert}_{D_1\to D_2}(Q)
}
$$

Version 1 fields:

$$
\left\langle
\mathsf{DomainMap},
\mathsf{TargetFidelity},
\mathsf{QuantifierLift},
\mathsf{PremisePreservation},
\mathsf{SolutionCompatibility},
\mathsf{BoundaryCompatibility},
\mathsf{ParameterUniformity},
\mathsf{RepresentationFidelity},
\mathsf{InterpretationStatus},
\mathsf{CounterexampleReflection},
\mathsf{Debt},
\mathsf{ProofRef}
\right\rangle.
$$

Not every bridge requires all fields, but any missing field must be marked as not applicable or as debt, and cannot be silently ignored.

---

# 21. Globality Debt

Define:

$$
\boxed{
\mathsf{GDebt}
=
\mathsf{Debt}_{\rm domain}
\uplus
\mathsf{Debt}_{\rm quant}
\uplus
\mathsf{Debt}_{\rm uniform}
\uplus
\mathsf{Debt}_{\rm sem}
\uplus
\mathsf{Debt}_{\rm rep}
\uplus
\mathsf{Debt}_{\rm phys}
\uplus
\mathsf{Debt}_{\rm proof}.
}
$$

When a claim has been proven in a narrower domain, but the promotion obligations for a broader domain are not yet fulfilled, it can be marked as:

$$
\mathsf{CLOSED}^{+}_{D_1}
\quad+
\quad
\mathsf{OPEN}_{D_2\setminus D_1}.
$$

This is more precise than simply writing "partially proven."

---

# 22. Globality is Not a Total Order

If two theorems:

$$
Q_A,
\qquad
Q_B,
$$

where $Q_A$ is broader on the time axis, but $Q_B$ is broader in data class or equation family, it does not necessarily follow that:

$$
Q_A\succeq Q_B
$$

or:

$$
Q_B\succeq Q_A.
$$

Therefore, CSM uses **partial comparability**.

Define:

$$
Q_A\preceq_G Q_B
$$

holds only when all comparison axes are aligned and the scope of $Q_B$ at least contains that of $Q_A$.

Otherwise, it is marked as:

$$
\boxed{
\mathsf{GLOBALLY\_INCOMPARABLE}.
}
$$

---

# 23. Domain Embedding Does Not Equal Theorem Transfer

Even if there is:

$$
\iota:D_1\hookrightarrow D_2,
$$

it only proves domain embedding.

It also requires:

- equation compatibility;
- solution semantics compatibility;
- target preservation;
- assumptions preservation;
- relevant estimates / invariants preservation.

Thus:

$$
\boxed{
\text{Domain Embedding}
\not\Rightarrow
\text{Theorem Transfer}.
}
$$

---

# 24. Cross-Domain Transfer of Counterexamples

Counterexample transfer has a different direction than theorem promotion.

If the target is a universal claim:

$$
\forall x\in D_2,
\quad
Q(x),
$$

and:

$$
x_\star\in D_1\subseteq D_2
$$

constitutes a true counterexample under the **same target semantics**, then:

$$
\neg Q(x_\star)
$$

can refute the broader universal claim.

However, if the gap between $D_1$ and $D_2$ also crosses model interpretation, solution notion, or modified equations, the counterexample fidelity must be re-examined.

Therefore:

$$
\boxed{
\text{Counterexample Transfer}
\text{ is typed, not name-based.}
}
$$

---

# 25. Cross-Domain Transfer of Obstructions

Whether an obstruction:

$$
O_{D_1}
$$

can transfer to $D_2$ depends on whether the assumptions used by the obstruction are preserved in $D_2$.

Define:

$$
\mathsf{ObsTransferCert}_{D_1\to D_2}(O).
$$

If the obstruction relies on:

$$
A_1,\ldots,A_k,
$$

then it requires at least:

$$
\forall i,
\quad
\mathsf{Preserve}_{D_1\to D_2}(A_i).
$$

Otherwise, the obstruction must remain confined to its original domain.

---

# 26. Scope Frontier

Paper 00 defines the closure frontier:

$$
\partial\mathfrak C(Q).
$$

This paper further defines:

$$
\boxed{
\partial_G\mathfrak C(Q)
}
$$

as the **globality / scope frontier**.

Its members are not simply OPEN theorems, but rather:

- closed on some axes;
- not yet closed on other axes;
- promotion bridges still have debt;
- domain extensions are not yet covered;
- interpretations are not yet established.

Thus, the complete frontier can be written as:

$$
\partial\mathfrak C
=
\partial_{\rm proof}\mathfrak C
\cup
\partial_G\mathfrak C
\cup
\partial_{\rm bridge}\mathfrak C
\cup
\partial_{\rm interp}\mathfrak C.
$$

---

# 27. New Interpretation of Relative-Global Closure

RGC-4 in Paper 00 is: having a completeness certificate for the declared admissible mechanism space and a closed frontier.

This paper adds: the RGC grade must be bound to a globality profile.

Therefore, one cannot simply write:

$$
\mathsf{RGC4}(Q).
$$

but should write:

$$
\boxed{
\mathsf{RGC4}(Q\mid\mathsf{GProf},D,\Theta,\mathcal A).
}
$$

The same proposition can have different closure grades under different globality profiles.

---

# 28. Domain Stratification

CSM does not arrange all domains into a single inclusion chain.

Define the domain graph:

$$
\boxed{
\mathcal G_D
=
(V_D,E_D,\tau_D).
}
$$

edge types may include:

$$
\tau_D(e)
\in
\{
\mathsf{RESTRICTS},
\mathsf{EXTENDS},
\mathsf{GENERALIZES},
\mathsf{SPECIALIZES},
\mathsf{INTERPRETS},
\mathsf{IDEALIZES},
\mathsf{APPROXIMATES},
\mathsf{EMBEDS},
\mathsf{REPRESENTS}
\}.
$$

Only a few edges like `RESTRICTS / EXTENDS` are directly related to set inclusion under specific conditions.

`INTERPRETS` and `IDEALIZES` should not be drawn as standard subset arrows.

---

# 29. Navier--Stokes: formal / Clay mathematical domain

Define:

$$
\boxed{
\mathfrak N_{\rm C}
}
$$

as the Clay / formal mathematical Navier--Stokes target domain.

More precisely, because the formal problem can contain different formal clauses / spatial settings, this paper allows:

$$
\mathfrak N_{\rm C}
=
\{
\mathfrak N_{\rm C}^{(c)}
:\
c\in\mathcal C_{\rm formal}
\}.
$$

Each clause must record its own:

- equation;
- dimension;
- spatial domain;
- data class;
- solution notion;
- regularity target;
- forcing / boundary convention.

This paper does not silently compress different clauses into the same statement.

---

# 30. Where Exactly is the "Global" in Clay NS

Under a fixed formal clause, its typical global regularity / existence target includes at least:

$$
G_t
=
\mathsf{FULL}_{[0,\infty)}
$$

or an equivalent requirement for extension over all finite times, as well as universal quantification over the declared admissible data class.

But this still does not mean:

$$
G_{\rm eq}
=
\mathsf{FAMILY}_{\text{all NS-like equations}}.
$$

Nor does it mean:

$$
G_{\rm phys}
=
\mathsf{FULL}_{\text{all physical fluids}}.
$$

Therefore:

$$
\boxed{
\text{Clay-global}
=
\text{strong globality inside a restricted formal scope}.
}
$$

"Restricted" here does not mean the problem is small, but rather that its quantifier contract has explicit boundaries.

---

# 31. Physical Navier--Stokes realization domain

Define:

$$
\boxed{
\mathfrak N_{\rm P}
}
$$

as the physical NS realization domain.

It is not:

$$
\mathfrak N_{\rm C}
\subseteq
\mathfrak N_{\rm P}
$$

a simple set relation like this.

A more reasonable representation is:

$$
\mathfrak N_{\rm C}
\xleftrightarrow[
\mathsf{Idealize}
]{
\mathsf{Interpret}
}
\mathfrak N_{\rm P}.
$$

Its bridge may rely on:

- continuum approximation;
- constitutive regime;
- Reynolds / Mach / Knudsen-like regime;
- measurement scale;
- neglected physics;
- boundary realization;
- material properties.

This paper does not declare that any single bridge holds completely across all physical regimes.

---

# 32. Generalized NS-like family

Define:

$$
\boxed{
\mathfrak N_{\rm G}^{\Sigma}
}
$$

as the generalized NS-like equation family declared by signature $\Sigma$.

Version 1 signature:

$$
\boxed{
\Sigma_{\rm NSL}
=
\left\langle
 d,
\mathcal X,
\mathcal C,
\mathcal B_{\rm nl},
\mathcal A_{\rm diss},
\mathcal P_{\rm proj},
\mathcal F,
\mathcal B_{\rm bdry},
\mathcal K_{\rm const},
\mathcal S
\right\rangle.
}
$$

Where:

- $d$: dimension family;
- $\mathcal X$: geometry / manifold class;
- $\mathcal C$: constraint class, e.g., divergence-free or its generalized analogue;
- $\mathcal B_{\rm nl}$: nonlinear transport / interaction class;
- $\mathcal A_{\rm diss}$: dissipation operator class;
- $\mathcal P_{\rm proj}$: pressure / projection / constraint enforcement;
- $\mathcal F$: forcing class;
- $\mathcal B_{\rm bdry}$: boundary class;
- $\mathcal K_{\rm const}$: constitutive / coefficient class;
- $\mathcal S$: solution semantics.

Only after $\Sigma_{\rm NSL}$ is explicitly defined does "for all NS-like systems" become a parsable theorem target.

---

# 33. Formal NS Does Not Equal Generalized NS-like Family

Even if:

$$
\mathfrak N_{\rm C}^{(c)}
\in
\mathfrak N_{\rm G}^{\Sigma}
$$

holds under a certain signature, it only carries the meaning of membership / embedding.

It does not imply:

$$
\operatorname{Prove}(
\mathfrak N_{\rm C}^{(c)}
)
\Rightarrow
\operatorname{Prove}(
\mathfrak N_{\rm G}^{\Sigma}
).
$$

Therefore:

$$
\boxed{
\operatorname{Prove}(\mathfrak N_{\rm C})
\not\Rightarrow
\operatorname{Prove}(\mathfrak N_{\rm G}^{\Sigma}).
}
$$

This is the **Equation-Family Non-Collapse Principle**.

---

# 34. Formal NS Does Not Equal Physical NS

By the same logic:

$$
\boxed{
\operatorname{Prove}(\mathfrak N_{\rm C})
\not\Rightarrow
\operatorname{Prove}(\mathfrak N_{\rm P}).
}
$$

This does not negate the physical value of formal PDE theorems, but rather requires that:

$$
\text{formal theorem}
\rightarrow
\text{physical claim}
$$

must pass through an interpretation bridge.

If the physical claim is broader than the validity regime of the formal model, additional scope expansion is required.

---

# 35. The Three Domains Should Not Be Arranged in a Simple Hierarchy

It is prohibited to write without proof:

$$
\mathfrak N_{\rm C}
\subset
\mathfrak N_{\rm P}
\subset
\mathfrak N_{\rm G}.
$$

What is more accurate is a typed graph:

$$
\boxed{
\mathfrak N_{\rm C}
\xrightarrow{
\mathsf{Generalize}
}
\mathfrak N_{\rm G}^{\Sigma}
}
$$

and:

$$
\boxed{
\mathfrak N_{\rm C}
\xleftrightarrow[
\mathsf{Idealize}
]{
\mathsf{Interpret}
}
\mathfrak N_{\rm P}.
}
$$

If necessary, the generalized model family can also establish its own model correspondence edges with the physical domain.

---

# 36. The NS Closure Graph Will Become a Multi-Domain Graph

In the future:

$$
\mathfrak C_{\rm NS}^{\rm rel}
$$

should not consist of just a single route graph.

It should contain at least:

$$
\boxed{
\mathcal G_{\rm NS}
=
\mathcal G_{\rm claim}
\cup
\mathcal G_{\rm route}
\cup
\mathcal G_{\rm obs}
\cup
\mathcal G_{\rm bridge}
\cup
\mathcal G_{\rm domain}
\cup
\mathcal G_{\rm scope}.
}
$$

Where $\mathcal G_{\rm scope}$ specifically tracks on which globality axes a theorem has closed.

---

# 37. Scope-State Node

To manipulate globality within the graph, define:

$$
\boxed{
\mathsf{ScopeState}(Q,a,D_a)
}
$$

to represent the closure state of proposition $Q$ on axis $a$ and domain $D_a$.

For example:

$$
\mathsf{ScopeState}(Q,\text{time},[0,\infty))
=
\mathsf{CLOSED}^{+}
$$

does not require:

$$
\mathsf{ScopeState}(Q,\text{equation-family},\Sigma)
=
\mathsf{CLOSED}^{+}.
$$

Thus, the same theorem can have different closure statuses along different axes.

---

# 38. Scope Hyperedge

Some globality promotions require multiple premises to hold simultaneously:

$$
\{
Q_{D_1},
B_1,
B_2,
U
\}
\Longrightarrow
Q_{D_2}.
$$

Where:

- $B_i$: bridge theorem;
- $U$: uniform estimate / compactness / preservation condition.

Therefore, scope promotion is a hyperedge, not a simple arrow.

---

# 39. Globality Closure Action

Added to the closure family of Paper 00:

$$
\boxed{
\mathsf{Cl}_{\rm globality}.
}
$$

It only allows the following operations:

1. Propagation of a proven universal claim to a valid restriction;
2. Promotion to a broader scope when a $\mathsf{GPCert}$ is present;
3. Propagation of a refutation to a broader universal claim when a counterexample-transfer certificate is present;
4. Axis-separated updates of scope states;
5. Writing all promotion debt into the ledger.

It prohibits name-based generalization.

---

# 40. Scope Reopening

If a scope-level NO-GO is later found to rely on an assumption that only holds in a narrow regime, the broader domain can be re-OPENed.

That is:

$$
\boxed{
\mathsf{BLOCKED}_{D_2}
\longrightarrow
\mathsf{OPEN}_{D_2}
}
$$

if the obstruction transfer certificate is revoked or downgraded.

This is the globality-axis version of the Reopening Principle from Paper 00.

---

# 41. Scope Ledger

Every globality upgrade / downgrade must record:

$$
\mathsf{ScopeLedgerEvent}
=
\left\langle
Q,
D_{\rm from},
D_{\rm to},
\mathsf{Axis},
\mathsf{Action},
\mathsf{CertRef},
\mathsf{DebtDelta},
\mathsf{Version}
\right\rangle.
$$

This prevents subsequent researchers from only seeing a "global theorem" without knowing in which domain it was originally established.

---

# 42. First Batch of Globality Axioms / Protocol Invariants

## G-1 — Scope Explicitness

Any global claim must be bound to a scope contract.

## G-2 — Axis Non-Collapse

Different globality axes must not be merged without proof.

## G-3 — Declared-Full Relativity

$$
\mathsf{FULL}_{D}
$$

is only valid for $D$.

## G-4 — No Upward Scope Promotion

A narrow-domain theorem does not automatically imply a broad-domain theorem.

## G-5 — Typed Counterexample Transfer

Counterexamples can only be transferred along target-preserving inclusions / bridges.

## G-6 — Interpretation Non-Identity

Formal models and physical realizations are not identical just because they share the same name.

## G-7 — Equation-Family Declaration

All equation-family globality must first declare a family signature.

## G-8 — Quantifier-Order Preservation

Swapping quantifier order is considered a theorem change, unless proven equivalent otherwise.

## G-9 — Representation Firewall

Representation-local success/failure does not automatically upgrade to a semantic-global result.

## G-10 — Proof-Regime Firewall

A proof in one formal/admissibility regime does not automatically equal a proof in another.

## G-11 — Scope Debt Visibility

All unpaid promotion obligations must be visible.

## G-12 — Relative-Global Firewall

Relative-global closure must not masquerade as absolute mathematical completeness.

---

# 43. First Batch of Derived Propositions

## Proposition 1 — Restriction Preservation

If $D_1\subseteq D_2$, and $Q$ is a universal claim over $D_2$ under the same semantics, then:

$$
\mathsf{CLOSED}^{+}_{D_2}(Q)
\Rightarrow
\mathsf{CLOSED}^{+}_{D_1}(Q).
$$

### Conditions

The target, solution notion, or equation is not allowed to change during the restriction process.

## Proposition 2 — Expansion Non-Entailment

In general:

$$
\mathsf{CLOSED}^{+}_{D_1}(Q)
\not\Rightarrow
\mathsf{CLOSED}^{+}_{D_2}(Q)
$$

for $D_1\subsetneq D_2$.

## Proposition 3 — Globality Incomparability

If $Q_A$ and $Q_B$ are each broader on different axes, and not all axes are aligned, then $Q_A, Q_B$ can be incomparable under $\preceq_G$.

## Proposition 4 — Counterexample Lift under Inclusion

If the universal target semantics remain unchanged, and $x_\star\in D_1\subseteq D_2$ is a true counterexample to $Q$, then $x_\star$ simultaneously refutes the universal claim over $D_2$.

## Proposition 5 — Physical Non-Transfer

The closure status of a formal theorem cannot directly update the physical-realization scope state without an interpretation certificate.

## Proposition 6 — Family Non-Transfer

A theorem for a single equation member cannot directly update the equation-family scope state to positively closed without a family-uniform proof.

---

# 44. Globality Proof-Obligation Matrix

| Promotion | Minimum Obligation |
|---|---|
| local time $\to$ global time | continuation / blow-up exclusion / appropriate extension theorem |
| one datum $\to$ data class | uniform or pointwise-all proof over declared class |
| one parameter $\to$ parameter family | quantifier order + parameter-uniformity audit |
| one boundary $\to$ boundary family | boundary compatibility theorem |
| unforced $\to$ forced | forcing-dependent estimates / theorem |
| one equation $\to$ equation family | family signature + uniform structural theorem |
| one solution notion $\to$ another | solution-compatibility theorem |
| representation-local $\to$ semantic-global | representation fidelity / reconstruction theorem |
| formal model $\to$ physical realization | interpretation / validation bridge |
| observed proof space $\to$ admissible proof space | route/decomposition completeness certificate |

---

# 45. NS Domain Record v0.1

```yaml
ns_domains:
  clay_formal:
    id: N_C
    relation_kind: formal_problem_family
    globality_focus:
      - time
      - declared_data_class
      - declared_regularities
    non_implications:
      - physical_realization_globality
      - generalized_equation_family_globality

  physical_realization:
    id: N_P
    relation_kind: interpreted_realization_domain
    relation_to_N_C:
      - INTERPRETS
      - IDEALIZES
    not_a_simple_subset: true

  generalized_ns_like:
    id: N_G_Sigma
    relation_kind: signature_parameterized_equation_family
    signature_required: true
    relation_to_N_C:
      - GENERALIZES
      - EMBEDS_when_certified
```

---

# 46. Globality Record v0.1

```yaml
globality_record:
  claim_id: Q-...
  scope_contract:
    equation_domain: ...
    spatial_domain: ...
    time_domain: ...
    data_class: ...
    solution_notion: ...
    boundary_family: ...
    forcing_family: ...
    parameter_domain: ...
    regularity_target: ...
    interpretation_domain: ...
    proof_regime: ...
  axes:
    time: FULL_D | PARTIAL | LOCAL | OPEN | UNKNOWN
    space: FULL_D | PARTIAL | LOCAL | OPEN | UNKNOWN
    data: FULL_D | PARTIAL | LOCAL | OPEN | UNKNOWN
    equation_family: FAMILY_Sigma | PARTIAL | OPEN | UNKNOWN
    physical: PARTIAL | OPEN | UNKNOWN
    proof: FULL_D | PARTIAL | OPEN | UNKNOWN
  promotion_certificates: []
  promotion_debt: []
  ledger_ref: ...
```

---

# 47. The First True Integration of CSM and the NS Proof-Space

In the past, the NS proof-space primarily tracked:

$$
\text{Route}
\rightarrow
\text{Obstruction}
\rightarrow
\text{Survivor}.
$$

After incorporating Paper 01, every survivor must also ask:

> In which globality profile does it survive?

For example, a mechanism might:

- survive under a fixed equation;
- survive under a fixed data class;
- survive only in a vanishing-parameter asymptotic;
- be unknown whether it can enter a broader equation family;
- have absolutely no physical interpretation claim.

Therefore, the survivor record should be expanded to:

$$
\boxed{
\mathsf{SurvivorState}
=
\left\langle
\mathsf{Mechanism},
\mathsf{ScopeContract},
\mathsf{GProf},
\mathsf{ObstructionHistory},
\mathsf{Debt}
\right\rangle.
}
$$

This directly prevents "local survivors from being misinterpreted as global counterexample candidates."

---

# 48. Closure Targets Must Also Be Stratified

In the future, saying:

> "The NS closure space is 90% closed"

is invalid in CSM, unless the metric and globality profile are specified.

What is more accurate is:

$$
\mathsf{ClosureCoverage}
(
Q;
\mathsf{GProf},
\sim,
\Theta,
\mathcal A
).
$$

For example, there can be:

- observed-route closure coverage;
- basin closure coverage;
- obstruction-certified coverage;
- admissible-mechanism coverage;
- scope-axis coverage.

Different coverages cannot be merged into a single unconditional percentage.

---

# 49. Scope-Frontier Vector

Define:

$$
\boxed{
\mathbf F_G(Q)
=
(
F_t,
F_x,
F_{\rm data},
F_{\rm sol},
F_{\rm bdry},
F_{\rm force},
F_{\rm par},
F_{\rm reg},
F_{\rm eq},
F_{\rm rep},
F_{\rm phys},
F_{\rm proof}
).
}
$$

Each $F_a$ represents the unclosed quotient-aware frontier mass / class set on that axis.

This paper does not presuppose that the frontier mass must be a real-valued measure.

Version 1 can initially use:

- class count;
- weighted class count;
- theorem-strength-weighted count;
- obstruction-independence-adjusted count.

---

# 50. Globality Closure Dynamics

As research progresses:

$$
\mathsf{GProf}_{t+1}(Q)
=
\mathfrak U_G(
\mathsf{GProf}_t(Q),
\mathsf{NewCert}_t,
\mathsf{NewObs}_t,
\mathsf{NewDomain}_t,
\mathsf{Revision}_t
).
$$

But globality does not have to increase monotonically.

A theorem might have its scope reduced due to a statement correction:

$$
\mathsf{FULL}_{D_2}
\longrightarrow
\mathsf{FULL}_{D_1},
\qquad
D_1\subsetneq D_2.
$$

This is not a regression in research, but an increase in scope fidelity.

---

# 51. Domain Revision and Descendant Survival

If a parent domain $D$ is revised to $D'$, one cannot simply delete all descendants.

Every descendant $Q_i$ must be re-evaluated:

1. Does its proof actually use the deleted assumption?
2. Is its theorem target still meaningful?
3. Can it be restricted to $D'$?
4. Does an independent re-proof exist?
5. Is the obstruction still valid?
6. Can the representation / tool still be reused?

Therefore:

$$
\boxed{
\text{Parent Domain Revision}
\not\Rightarrow
\text{Descendant Annihilation}.
}
$$

This allows CSM to safely handle "problem framing being rewritten" without discarding the entire historical research space.

---

# 52. Immediate Impact on the NS Research Engineering

When C1--C6, X72, DCRP, MORP, RFP, FCBP, and other NS assets are projected onto the closure graph, each claim must be accompanied by at least:

- claim type;
- formal target;
- domain signature;
- globality profile;
- assumptions;
- proof / no-go / obstruction status;
- route family;
- quotient class;
- bridge dependencies;
- promotion debt;
- provenance.

Therefore, one cannot simply extract:

$$
A,C,L,O,S.
$$

The next version of the NS closure dataset should be expanded to:

$$
\boxed{
A,C,L,O,S,G,D,B,P
}
$$

Where:

- $G$: globality profile;
- $D$: domain signature;
- $B$: bridge set;
- $P$: promotion / proof debt.

---

# 53. Machine-Readable Minimum Schema

```yaml
csm_scope_state:
  schema_version: csm-globality/v0.1
  claim_id: string
  domain_signature:
    equation_domain: object
    spatial_domain: object
    time_domain: object
    data_class: object
    solution_notion: object
    boundary_family: object
    forcing_family: object
    parameter_domain: object
    regularity_target: object
    interpretation_domain: object
  globality_profile:
    time: object
    space: object
    data: object
    solution: object
    boundary: object
    forcing: object
    parameter: object
    regularity: object
    equation_family: object
    representation: object
    physical: object
    proof_regime: object
  status: OPEN | CLOSED_POS | CLOSED_NEG | BLOCKED | CONDITIONAL | UNKNOWN
  promotion_certificates: []
  debt: []
  provenance: []
  ledger_ref: string
```

---

# 54. Validation Scenarios

## Scenario A — Global time, one equation

A fixed PDE is proven to hold for all time.

Correct:

$$
G_t=\mathsf{FULL}_{\mathcal T}.
$$

Incorrect:

$$
G_{\rm eq}=\mathsf{FAMILY}_{\Sigma}
$$

Automatic upgrade without proof.

## Scenario B — One parameter value

Proven:

$$
P(\lambda_0).
$$

Must not be written as:

$$
\forall\lambda\in\Lambda,
P(\lambda).
$$

## Scenario C — Physical agreement in one regime

The formal model agrees with experiments in a certain operating regime.

Must not be written as all physical realizations having been proven.

## Scenario D — Counterexample in a true subdomain

If the target semantics are exactly the same, a subdomain counterexample can refute a broader universal claim.

## Scenario E — Representation failure

A proof search failing in $\rho_1$ must not update the semantic-global status to BLOCKED, unless a representation robustness audit holds.

## Scenario F — Generalized NS-like family

If $\Sigma_{\rm NSL}$ is not declared, then "all NS-like equations" is:

$$
\mathsf{ILL\_SCOPED}.
$$

---

# 55. The Core No-Collapse Family of CSM Paper 01

$$
\boxed{
\text{Local}
\neq
\text{Partial}
\neq
\mathsf{FULL}_{D}.
}
$$

$$
\boxed{
\mathsf{FULL}_{D_1}
\neq
\mathsf{FULL}_{D_2}
\quad
(D_1\neq D_2).
}
$$

$$
\boxed{
\text{Global-in-time}
\neq
\text{Global-across-equations}.
}
$$

$$
\boxed{
\text{Equation-family globality}
\neq
\text{Physical-realization globality}.
}
$$

$$
\boxed{
\text{Domain embedding}
\neq
\text{theorem transfer}.
}
$$

$$
\boxed{
\text{Formal theorem}
\neq
\text{physical proof}.
}
$$

$$
\boxed{
\text{Scope expansion}
\neq
\text{theorem strengthening}.
}
$$

$$
\boxed{
\text{Relative-global closure}
\neq
\text{absolute mathematical completeness}.
}
$$

---

# 56. The Immediate Question for the Next Paper

Paper 00 defines the closure space.

Paper 01 defines the domain / globality typing of the closure space.

The next natural question is:

> Given the existence of typed domains, how do we truly assemble "propositions, routes, obstructions, survivors, NO-GOs, and bridges" into a computable closure graph, and define closure propagation, frontier reduction, and reopening?

Therefore, the proposed next paper is:

$$
\boxed{
\textbf{CSM Paper 02 — Typed Closure Graphs and Obstruction Propagation}
}
$$

Its task is to establish:

- typed claim hypergraph;
- proof-route quotient graph;
- obstruction transfer;
- survivor propagation;
- scope-state graph;
- closure event algebra;
- frontier update rules;
- canonical node / edge schema for the NS closure graph.

---

# 57. Conclusion

The core of CSM Paper 01 is not to split "global" into more nouns, but to transform globality into computable theorem metadata.

A proposition is no longer merely recorded as:

> global / local.

but rather recorded as:

$$
\boxed{
\mathsf{ScopeContract}(Q)
+
\mathsf{GProf}(Q)
+
\mathsf{GPCert}
+
\mathsf{GDebt}.
}
$$

This allows us to precisely distinguish:

- which axes are closed;
- which axes are still open;
- which theorems are only correct in a narrow scope;
- which generalizations truly possess certificates;
- which physical interpretations are not yet established;
- which generalized equation-family claims remain undefined natural language expansions.

For Navier--Stokes, this step establishes a necessary three-domain firewall:

$$
\boxed{
\mathfrak N_{\rm C}
\neq
\mathfrak N_{\rm P}
\neq
\mathfrak N_{\rm G}^{\Sigma}.
}
$$

Clay NS can possess very strong globality within its formal scope, but this globality remains a typed, bounded-by-definition globality, rather than an unbounded globality over all NS-like equations or all physical fluids.

Therefore, the research direction of CSM is not to weaken the power of "global", but to ensure that every type of globality acquires its true quantifier, scope, bridge, and closure status.

Once these fields are projected into the NS closure graph, the "successes, failures, blocked routes, and survivors" of hundreds of past proof routes can, for the first time, be placed into the same relative-global space without generating false closures due to scope bait-and-switch.

---

# Appendix A: Core Symbols

| Symbol | Meaning |
|---|---|
| $\mathsf{ScopeContract}(Q)$ | Proposition scope contract |
| $\mathsf{DomSig}(Q)$ | domain signature |
| $\mathsf{Quant}(Q)$ | quantifier envelope |
| $\mathsf{GProf}(Q)$ | globality profile |
| $G_t$ | time globality |
| $G_x$ | spatial globality |
| $G_{\rm data}$ | data-class globality |
| $G_{\rm eq}$ | equation-family globality |
| $G_{\rm phys}$ | physical-realization globality |
| $G_{\rm proof}$ | proof-regime globality |
| $\mathsf{GPCert}$ | globality promotion certificate |
| $\mathsf{GDebt}$ | globality promotion debt |
| $\partial_G\mathfrak C$ | scope/globality frontier |
| $\preceq_G$ | partial globality preorder |
| $\mathcal G_D$ | domain graph |
| $\mathfrak N_{\rm C}$ | formal / Clay mathematical NS domain |
| $\mathfrak N_{\rm P}$ | physical NS realization domain |
| $\mathfrak N_{\rm G}^{\Sigma}$ | signature-parameterized generalized NS-like family |

---

# Appendix B: Relationship with CSM Paper 00

Paper 00 has established:

- $\Omega^{\rm obs}\neq\Omega^{\rm adm}\neq\Omega^{\rm math}$;
- relative-global closure;
- typed closure-space objects;
- closure status;
- implication / dependency / quotient / obstruction / bridge / generative closure;
- route-completeness certificates;
- RGC-0 through RGC-4;
- The preliminary distinction between the formal, physical, and generalized NS domains.

Paper 01 does not replace the above definitions, but expands the `Globality Typing Principle` into a complete domain / quantifier system, and mandates that the RGC status must be bound to $\mathsf{GProf}$.

---

# Appendix C: Internal Theoretical Lineage

This paper primarily follows from:

1. **CSM Paper 00** — closure space, relative-global closure, RGC, closure debt, frontier;
2. **LSI-PSD** — semantic quotient, route graph, proof basin, obstruction confluence, theorem-strength preorder, Proof-Space Observatory;
3. **UCT / UGC-CUR** — typed non-collapse, bridge certificate, debt, ledger, local-to-absolute gate;
4. **Existing NS research lines** — the non-collapsibility of formal NS and physical interpretation, NS-203 proof-space instrumentation;
5. **NS C1--C6 / X72 / DCRP** — as the actual data sources for the subsequent closure graph, rather than the theorem content of this paper.

---

# Appendix D: Next Steps

The next step should not be to immediately continue any specific local NS proof route.

We should first complete:

$$
\boxed{
\text{CSM Paper 02 — Typed Closure Graphs and Obstruction Propagation}
}
$$

and only then begin the first true:

$$
\boxed{
\text{NS Relative-Global Closure Graph v0.1}.
}
$$

Its first batch of ingest sources should prioritize:

- ETN--X Integration;
- C1 / C2;
- C3--C6;
- X72;
- DCRP;
- Proof Asset Map;
- Curated LSI-PSD NS-203 route / obstruction metadata.

**END OF CSM PAPER 01 v0.1**