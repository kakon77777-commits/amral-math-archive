# The Proof-Obligation Principle for Ontological Discreteness
## Formal Proof Obligations for the Claim that "The Universe Is a Digital Computer"

- English Title: **The Proof-Obligation Principle for Ontological Discreteness: Formal Requirements for the Claim that the Universe Is a Digital Computer**
- Version: v0.1
- Date: 2026-08-16
- Type: Computational Ontology / Philosophy of Science / Methodology of Mathematical Logic
- Core Position: This paper does not argue that the world is necessarily continuous, nor does it argue that the world is necessarily discrete; it solely establishes the proof obligations for strong discrete ontology.

---

## Abstract

Propositions such as "the universe is a computer," "it from bit," and "the fundamental layer of the world is discrete information" frequently appear in digital physics, computational cosmology, and informational ontology. However, being simulable by a digital computer, being discretely describable, or being encodable in bits are all insufficient to deduce that the fundamental constitution of the world is itself discrete.

This paper proposes the **Proof-Obligation Principle for Ontological Discreteness**: if one claims that the world is ontologically equivalent to a discrete computational system, one must prove that its discreteness is not an artifact of measurement, representation, approximation, coordinates, quantized spectra, computational interfaces, or observational limits, but rather an irreducible structural invariant across all lossless equivalent representations. If the world potentially possesses a continuous substrate, pre-spacetime structure, hybrid structure, or unknown structure, these possibilities cannot be excluded without proof.

---

# 1. Four Propositions That Must Not Be Conflated

First, we must distinguish:

$$
\boxed{
\text{Computationally describable}
}
$$

$$
\boxed{
\text{Digitally representable}
}
$$

$$
\boxed{
\text{Exactly digitally simulable}
}
$$

$$
\boxed{
\text{Digitally constituted}
}
$$

They are not equivalent.

In particular:

$$
\boxed{
\text{discretely computable}
\neq
\text{ontologically discrete}.
}
\tag{1.1}
$$

---

# 2. Numerical Approximation Does Not Imply Ontological Discreteness

Consider a continuous system:

$$
\frac{dx}{dt}
=
f(x).
$$

It can be processed by a digital computer using:

- finite differences;
- Runge–Kutta;
- spectral methods;
- finite elements;

for arbitrarily fine approximation.

However:

$$
\boxed{
\text{arbitrarily accurate discrete approximation}
\not\Rightarrow
\text{exact discrete ontology}.
}
\tag{2.1}
$$

What numerical methods prove is:

$$
\boxed{
\text{digital computability / approximability},
}
$$

and not:

$$
\boxed{
\text{digital constitution}.
}
$$

---

# 3. World States and Discrete Models

Let the complete state space of the world be:

$$
\mathcal W.
$$

A strong discrete ontology claims the existence of a discrete state space:

$$
\mathcal D
$$

and a discrete computational evolution:

$$
F_t:
\mathcal D
\to
\mathcal D
$$

such that:

$$
\boxed{
\mathcal W
\simeq
\mathcal D.
}
$$

This claim requires at least the following proofs.

---

# 4. Exact Encoding Obligation

There must exist an encoding:

$$
E:
\mathcal W
\to
\mathcal D
$$

and a reconstruction:

$$
R:
\mathcal D
\to
\mathcal W
$$

such that:

$$
\boxed{
R\circ E
=
\operatorname{id}_{\mathcal W}.
}
\tag{4.1}
$$

That is:

$$
\boxed{
\text{lossless exact reconstruction}.
}
$$

If we only have:

$$
R(E(w))
\approx
w,
$$

then it only proves an approximate model.

---

# 5. Dynamical Conjugacy Obligation

Let the true evolution of the world be:

$$
\Phi_t:
\mathcal W
\to
\mathcal W.
$$

A strong digital ontology requires at least:

$$
\boxed{
E\circ\Phi_t
=
F_t\circ E.
}
\tag{5.1}
$$

That is:

$$
\boxed{
\text{world dynamics}
\cong
\text{discrete computational dynamics}.
}
$$

Merely being able to simulate observational outputs is insufficient to establish this conjugacy.

---

# 6. Invariant Preservation Obligation

All relevant physical / logical / mathematical invariants:

$$
I_\alpha
$$

must satisfy:

$$
\boxed{
I_\alpha(w)
=
\widetilde I_\alpha(E(w)).
}
\tag{6.1}
$$

If the discrete representation loses any ontologically necessary invariant,

then:

$$
\boxed{
\mathcal W\not\simeq\mathcal D
}
$$

holds at least for that candidate model.

---

# 7. Essential Discreteness Obligation

The most crucial requirement is not:

> to find a discrete model.

but to prove that:

$$
\boxed{
\textbf{
discreteness itself is representation-independent.
}
}
$$

Namely, there does not exist another lossless equivalent carrier:

$$
\mathcal C
$$

that is continuous, hybrid, or of another non-discrete form, yet equally preserves:

$$
\text{state}
+
\text{dynamics}
+
\text{invariants}.
$$

Otherwise:

$$
\boxed{
\text{discreteness may merely be a representational choice}.
}
$$

---

# 8. The Proof-Obligation Principle for Ontological Discreteness

Formally stated:

$$
\boxed{
\textbf{
Claiming ontological discreteness requires proving
that discreteness is invariant under lossless equivalent representations.
}
}
\tag{8.1}
$$

In plain language:

> If one claims that the world is ontologically discrete, one must prove that this discreteness is not generated by coordinates, observation, measurement, approximation, partitioning, computational interfaces, or representational methods, but is an irreducible structural invariant across all lossless equivalent representations.

---

# 9. Minimum Length Does Not Equal a Discrete World

Even if a future theory proves the existence of:

$$
\ell_{\min}>0,
$$

it still cannot directly imply:

$$
\boxed{
\text{world is discrete}.
}
$$

Because:

$$
\ell_{\min}
$$

may represent:

- an operational measurement cutoff;
- a spectral gap;
- an effective theory boundary;
- a quantized excitation on a continuous substrate;
- noncommutative geometry;
- a pre-spacetime constraint;
- a mixed continuous/discrete structure;
- an as-yet-unknown fundamental form.

Therefore:

$$
\boxed{
\text{minimum observable scale}
\neq
\text{discrete ontology}.
}
\tag{9.1}
$$

---

# 10. Quantization Does Not Equal Discrete Ontology

Observing a discrete spectrum:

$$
E_n
$$

also does not imply:

$$
\boxed{
\text{entire substrate is discrete}.
}
$$

A continuous operator:

$$
H
$$

can perfectly well possess a discrete spectrum.

Therefore:

$$
\boxed{
\text{discrete eigenvalues}
\neq
\text{discrete state-space ontology}.
}
\tag{10.1}
$$

---

# 11. Bit Does Not Equal Ontological Atom

That a physical system can be mapped into:

$$
0/1
$$

symbols, does not mean that:

$$
0,1
$$

are the ontological atoms of the world.

A bit might merely be an:

$$
\boxed{
\text{observation alphabet}
}
$$

or an:

$$
\boxed{
\text{encoding alphabet}.
}
$$

Thus:

$$
\boxed{
\text{information encoded in bits}
\not\Rightarrow
\text{reality made of bits}.
}
\tag{11.1}
$$

---

# 12. Computable Does Not Equal Computer

Suppose a phenomenon:

$$
x(t)
$$

can be evaluated by an algorithm:

$$
A
$$

via computation.

This only supports:

$$
\boxed{
x(t)
\text{ is computationally representable}.
}
$$

It does not imply:

$$
\boxed{
x(t)
\text{ is literally an algorithm}.
}
$$

Likewise:

$$
\boxed{
\text{Universe is computable}
\not\Rightarrow
\text{Universe is a computer}.
}
\tag{12.1}
$$

---

# 13. Weak and Strong Computational Cosmology

## 13.1 Weak computational thesis

$$
\boxed{
\text{The universe admits computational descriptions.}
}
$$

This is compatible with scientific modeling and carries a relatively low burden of proof.

## 13.2 Strong digital ontology

$$
\boxed{
\text{The universe is literally a discrete computational system.}
}
$$

This requires the complete proof obligations outlined in Sections 4–8.

The two must not be conflated.

---

# 14. No Reverse Smuggling of a Continuous World

This paper equally rejects:

$$
\boxed{
\text{failure to find essential discreteness}
\Longrightarrow
\text{the world is necessarily continuous}.
}
$$

Valid epistemic states should at least include:

$$
\boxed{
\mathsf C,
\quad
\mathsf D,
\quad
\mathsf H,
\quad
\mathsf U,
}
$$

where:

- $\mathsf C$: essentially continuous;
- $\mathsf D$: essentially discrete;
- $\mathsf H$: hybrid / mixed;
- $\mathsf U$: unknown, including pre-spacetime, unclassified, or undecidable by current concepts.

When evidence is insufficient:

$$
\boxed{
\mathsf U
\not\Rightarrow
\mathsf D.
}
$$

Likewise:

$$
\boxed{
\mathsf U
\not\Rightarrow
\mathsf C.
}
$$

---

# 15. Pre-Spacetime and Unknown Forms

If the fundamental layer is not:

$$
\text{space}
+
\text{time}
$$

as an ordinary structure,

but rather:

- pre-spacetime;
- a relational substrate;
- a categorical structure;
- an algebraic constraint network;
- a continuous/discrete mixed object;
- an unknown mathematical ontology;

then it cannot be unprovenly renamed as a:

$$
\boxed{
\text{digital computer}.
}
$$

"Can be described by a computer" and "is literally a computer" remain distinct propositions.

---

# 16. Relationship with the Generalized Structural Continuum Hypothesis

If a discrete model:

$$
\mathcal D
$$

can be losslessly continuumized:

$$
\mathcal D
\rightsquigarrow
\mathcal C,
$$

and:

$$
\mathcal C
$$

completely preserves:

$$
\text{state}
+
\text{dynamics}
+
\text{invariants},
$$

then:

$$
\boxed{
\mathcal D
}
$$

's discreteness at least cannot independently serve as evidence for the world ontology.

Therefore:

$$
\boxed{
\text{digital ontology}
}
$$

requires finding an:

$$
\boxed{
\text{essential discreteness witness}.
}
$$

---

# 17. A Formal Refutation Template

For any proposition claiming:

> The fundamental layer of the world is a discrete computer.

one may demand proof of the following five steps:

$$
\boxed{
\begin{aligned}
\mathrm{P1}:&
\quad
\text{Exact encoding};
\\
\mathrm{P2}:&
\quad
\text{Exact reconstruction};
\\
\mathrm{P3}:&
\quad
\text{Dynamical conjugacy};
\\
\mathrm{P4}:&
\quad
\text{Invariant preservation};
\\
\mathrm{P5}:&
\quad
\text{Essential discreteness}.
\end{aligned}
}
\tag{17.1}
$$

If any step is missing:

$$
\boxed{
\text{digital model}
\neq
\text{proven digital ontology}.
}
$$

---

# 18. Minimum Argumentation Standards

Therefore, one must at least distinguish between:

$$
\boxed{
\text{Simulation}
}
$$

$$
\boxed{
\text{Representation}
}
$$

$$
\boxed{
\text{Equivalence}
}
$$

$$
\boxed{
\text{Ontology}.
}
$$

In the chain of reasoning:

$$
\text{Simulation}
\to
\text{Representation}
\to
\text{Equivalence}
\to
\text{Ontology}
$$

every arrow must be independently proven.

One cannot jump directly from the first step to the last.

---

# 19. Core Theorem-like Proposition

The core of this paper can be compressed into:

$$
\boxed{
\textbf{
A discrete computational representation of reality
is not evidence of discrete computational constitution
unless discreteness itself is shown to be invariant under
all relevant lossless equivalent representations.
}
}
\tag{19.1}
$$

---

# 20. Conclusion

If "the universe is a digital computer" is merely a metaphor, it can serve as a research intuition.

If it is to be elevated to an ontological proposition, it must accept the full burden of proof:

$$
\boxed{
R\circ E
=
\operatorname{id}_{\mathcal W},
}
$$

$$
\boxed{
E\circ\Phi_t
=
F_t\circ E,
}
$$

and:

$$
\boxed{
\text{discreteness is an invariant,
not a representation artifact}.
}
$$

Therefore, the minimal conclusion of this paper is not:

$$
\boxed{
\text{the world is continuous}.
}
$$

but rather:

$$
\boxed{
\textbf{
Until essential discreteness is proven,
one must not smuggle in the claim that "the fundamental layer of the world is a discrete computer"
from discrete descriptions, bit encodings, quantized spectra, or digital simulations.
}
}
$$

The shortest version:

> **The universe may compute. That does not prove that the universe is a digital computer.**

And:

$$
\boxed{
\textbf{Please prove it first.}
}
$$