# P/NP Debate Game Research Area | Round 15

## Tractability Proof Systems: Certificates, Normal-Form Escape, and Clocked Enumeration

**Tractability Proof Systems: Certificates, Normal-Form Escape, and Clocked Enumeration**

- **Lead Researcher:** Neo.K (Chuan-Wei Hsu)
- **Collaborator/Editor:** Aletheia
- **Institution:** EveMissLab (Yiyannuo Technology Co., Ltd.)
- **Date:** August 1, 2026
- **Version:** v1.0
- **Research Status:** Round 15 Dual-Hypothesis Rehearsal
- **Prerequisite Document:** `14_Round_14_Complexity_Potential_Energy_Game_and_Certificate_Completeness_Trap.md`

---

## Abstract

Round 14 proposed the **Potential Certificate Completeness Trap**: if the tractability certificate language is too weak, the absence of a certificate cannot imply a super-polynomial lower bound; if it is too strong, it is easy to smuggle the original problem into the certificate. Therefore, Round 15 originally prepared to investigate: is it possible for a sound, complete, and non-circular polynomial-tractability proof system to exist?

This round first makes an important correction: determining whether **arbitrary Turing machine code** runs in polynomial time is indeed generally undecidable; however, this does not prevent us from establishing an **extensionally complete** P normal-form language. Cobham's bounded recursion and Bellantoni–Cook's safe recursion both provide classic results of this kind: a function is computable in polynomial time if and only if it can be expressed by a specific restricted recursive syntax.

Therefore, this round distinguishes between three types of "completeness":

1. **Machine-index completeness**: determining whether every arbitrary machine $M$ is polynomial;
2. **Proof completeness**: whether every polynomial machine has a verifiable runtime proof;
3. **Extensional normal-form completeness**: for every P/FP computable function, there exists an equivalent normal form belonging to a restricted syntax.

The first type cannot be expected in a general Turing-machine setting; the third type, however, already has mature theories. This directly changes the state of the game.

The Equality Team obtains a new strategy: there is no need to start from an arbitrary SAT solver and then prove it is polynomial; one can directly construct SAT within a normal-form language where "syntax guarantees polynomiality." If they successfully construct

$$
t_{\mathrm{SAT}}\in\mathcal G_P
$$

and

$$
\llbracket t_{\mathrm{SAT}}\rrbracket=\chi_{\mathrm{SAT}},
$$

then they directly obtain

$$
P=NP.
$$

The Inequality Team obtains an exact dual: find a semantic property $\mathcal I$, prove that it is preserved by the generation rules of $\mathcal G_P$ such as initial functions, composition, and safe/bounded recursion, but that the SAT characteristic function does not possess $\mathcal I$. If successful, they obtain

$$
\chi_{\mathrm{SAT}}\notin FP,
$$

and thus

$$
P\neq NP.
$$

This is the first time in this series that a "cross-representation invariant" is connected with a known **generative syntax that completely characterizes P**.

This round also proposes a second normal form: **clocked Turing machines**. For an arbitrary machine $M$ and a fixed polynomial clock, establish a machine that halts upon timeout. All clocked machines are in P, and any P language has at least one equivalent clocked representation. This demonstrates that "the index property of whether arbitrary code belongs to P is hard to decide" and "whether P has an effective normal-form presentation" are two different matters.

The next round therefore enters the **Clocked Enumeration and Diagonalization Game**: since P-normal forms can be effectively enumerated, is it possible to defeat them one by one via diagonalization, while keeping the diagonal language in NP?

---

# 1. Three Types of Completeness Must Not Be Confused

## 1.1 Machine-index completeness

Input arbitrary Turing machine code:

$$
\langle M\rangle.
$$

Hope for an algorithm to decide:

$$
M\text{ runs within some polynomial time bound.}
$$

In general, this kind of runtime property is undecidable.

Therefore, one cannot expect a universal classifier to automatically decide P/non-P for arbitrary code.

## 1.2 Proof completeness

Another question is: does every polynomial machine have a finite runtime certificate? This involves formal proof systems, proof strength, formalization, and possible independence, which cannot be conflated with "arbitrary code can be decided by a classifier."

## 1.3 Extensional normal-form completeness

What truly matters is: does there exist a restricted language $\mathcal G_P$ satisfying

$$
t\in\mathcal G_P
\Rightarrow
\llbracket t\rrbracket\in FP,
$$

and

$$
f\in FP
\Rightarrow
\exists t\in\mathcal G_P:
\llbracket t\rrbracket=f.
$$

This kind of completeness is possible, and it is a classic direction in Implicit Computational Complexity.

Therefore:

$$
\boxed{
\text{Inability to classify arbitrary code}
\not\Rightarrow
\text{Inability to give P a complete normal-form language}
}
$$

---

# 2. Bellantoni–Cook / Cobham: Syntax Itself is a Tractability Certificate

Cobham used bounded recursion on notation to characterize polynomial-time computable functions; Bellantoni–Cook used safe recursion to establish a characterization that does not need to explicitly carry an external polynomial time bound.

Written abstractly:

$$
\mathcal G_P
=
\operatorname{Closure}
(\mathcal F_0;\operatorname{Comp},\operatorname{SafeRec}).
$$

Its core result is:

$$
\boxed{
\operatorname{Denote}(\mathcal G_P)=FP.
}
$$

Thus, term membership itself is a kind of **by-construction tractability certificate**.

This is different from the ATC in Round 14:

- ATC: proving the trajectory is polynomial *ex post facto*;
- ICC normal form: syntax design ensures that super-polynomial growth simply cannot be legally generated.

---

# 3. The Equality Team's New Strategy: Writing SAT Directly in P-Normal Form

SAT characteristic function:

$$
\chi_{\mathrm{SAT}}(\varphi)
=
\begin{cases}
1,&\varphi\text{ is satisfiable},\\
0,&\varphi\text{ is unsatisfiable}.
\end{cases}
$$

If the Equality Team can construct:

$$
t_{\mathrm{SAT}}\in\mathcal G_P
$$

and:

$$
\llbracket t_{\mathrm{SAT}}\rrbracket
=\chi_{\mathrm{SAT}},
$$

by soundness:

$$
\chi_{\mathrm{SAT}}\in FP.
$$

Since SAT is NP-complete:

$$
\boxed{P=NP.}
$$

The advantage of this path is that runtime accounting is absorbed by the normal-form meta-theorem.

---

# 4. The Inequality Team's New Strategy: Grammar Invariant Program

The Inequality Team now does not need to hunt down "all possible algorithm forms" one by one, but can perform structural induction on a known extensionally complete P grammar.

Find a semantic property:

$$
\mathcal I(f)
$$

such that it satisfies:

### Base Preservation

All initial functions have:

$$
\mathcal I(f).
$$

### Composition Preservation

If all components have $\mathcal I$, then the composition still has $\mathcal I$.

### Safe Recursion Preservation

If the premise functions of safe recursion all have $\mathcal I$, then the generated function also has $\mathcal I$.

Therefore, structural induction yields:

$$
\forall t\in\mathcal G_P,
\quad
\mathcal I(\llbracket t\rrbracket).
$$

If it can further be proven that:

$$
\neg\mathcal I(\chi_{\mathrm{SAT}}),
$$

then:

$$
\chi_{\mathrm{SAT}}\notin FP,
$$

thus:

$$
\boxed{P\neq NP.}
$$

This forms the **Normal-Form Invariant Problem**.

---

# 5. Is It Just Renaming P/NP?

If we define:

$$
\mathcal I(f):=[f\in FP],
$$

it is of course completely circular.

A valuable $\mathcal I$ must:

1. Be independently defined by more fundamental mathematical structures;
2. Not directly invoke the existence of polynomial algorithms;
3. Be able to prove closure rule by rule;
4. Be able to independently prove that SAT violates it;
5. Withstand scrutiny against barriers like relativization, natural proofs, and algebrization.

The cross-representation invariant, exact quotientability, algebraic preservation, and bridge stability sought in previous rounds now have a clear "domain of induction" for the first time.

---

# 6. The Second Normal Form: Clocked Turing Machines

Take an arbitrary Turing machine $M$, integer $k$, and constant $c$, and establish a clocked machine:

$$
M^{[k,c]}.
$$

On input $x$:

1. Simulate $M(x)$;
2. Execute at most

$$
c(|x|+1)^k
$$

steps;
3. Force halt upon timeout and output a fixed value.

Every $M^{[k,c]}$ is in P.

Enumerating all finite machine descriptions and $(k,c)$:

$$
C_1,C_2,C_3,\ldots
$$

yields an effective enumeration of all clocked polynomial machines.

If $L\in P$, there exist some $M,k,c$ such that:

$$
T_M(n)\le c(n+1)^k,
$$

thus the corresponding clocked machine is equivalent to $M$ on all inputs.

Therefore:

$$
\boxed{
P\text{ has an effective normal-form presentation.}
}
$$

This does not require determining whether an arbitrarily given $M$ itself is polynomial.

---

# 7. Formal Correction to the Round 14 Completeness Trap

The dichotomy in Round 14:

$$
\text{Certificate too weak}\Rightarrow\text{Misses P},
$$

$$
\text{Certificate too strong}\Rightarrow\text{Circular},
$$

needs a third path added:

$$
\boxed{
\text{Change the representation domain, use a by-construction P-normal form.}
}
$$

Therefore:

$$
\boxed{
\text{Classification completeness}
\neq
\text{Representation completeness}.
}
$$

The former is too strong for arbitrary machine indices; the latter already has mature, successful cases.

---

# 8. The Temptation of Clocked Enumeration: Direct Diagonalization?

Since we have:

$$
C_1,C_2,C_3,\ldots
$$

listing all P-normal-form machines, the Inequality Team immediately proposes:

$$
L_D(x_i)=1-C_i(x_i).
$$

This can defeat every $C_i$ via diagonalization.

But to prove $P\neq NP$, we not only need:

$$
L_D\notin P.
$$

We also must have:

$$
\boxed{
L_D\in NP.
}
$$

And this is exactly the difficulty.

---

# 9. Exponent Escalation Trap

The exponents of clocked machines have no common fixed upper bound:

$$
n^{k_1},n^{k_2},n^{k_3},\ldots
$$

If the diagonal machine fully simulates:

$$
C_i
$$

on the $i$-th diagonal input up to:

$$
|x_i|^{k_i},
$$

then its own runtime exponent may also grow with $i$.

This does not guarantee the existence of a fixed $K$:

$$
T_D(n)\le n^K.
$$

Therefore:

$$
\boxed{
\text{Defeating all polynomial exponents one by one}
}
$$

and:

$$
\boxed{
\text{Remaining within a fixed polynomial exponent oneself}
}
$$

form a direct tension.

This is the **Exponent Escalation Trap**.

---

# 10. Universal Simulation Overhead and NP Witness Trap

Even if the exponent issue is manageable, the universal diagonal machine still needs to parse:

$$
\langle C_i\rangle
$$

and simulate its execution, generating universal simulation overhead.

More crucially, a simple complement diagonal:

$$
1-C_i(x_i)
$$

does not naturally provide a polynomial witness.

Therefore:

$$
\boxed{
\text{Diagonalizable}
\not\Rightarrow
\text{NP-verifiable}.
}
$$

The ordinary time hierarchy can construct a decidable language outside $P$; the real difficulty is squeezing the diagonal language into NP.

---

# 11. Relativization Alarm

If the diagonalization argument in the next round still holds exactly as is after adding an arbitrary oracle, it will hit a Baker–Gill–Solovay-type relativization barrier.

Thus, every candidate diagonal construction in the next round must be checked:

$$
\boxed{
\text{Does the argument remain intact after adding an oracle?}
}
$$

If the answer is yes, it is highly suspicious.

---

# 12. Three Equivalent Game Interfaces

After 15 rounds, the traditional problem can be written into three interfaces.

## 12.1 Algorithm Interface

$$
P=NP
\iff
\exists A_{\mathrm{SAT}}\in P.
$$

## 12.2 Normal-Form Interface

If:

$$
\operatorname{Denote}(\mathcal G_P)=FP,
$$

then:

$$
P=NP
\iff
\exists t\in\mathcal G_P:
\llbracket t\rrbracket=\chi_{\mathrm{SAT}}.
$$

## 12.3 Invariant Interface

If it can be proven that:

$$
\forall t\in\mathcal G_P,
\quad
\mathcal I(\llbracket t\rrbracket),
$$

then:

$$
\neg\mathcal I(\chi_{\mathrm{SAT}})
\Rightarrow
P\neq NP.
$$

This third type is currently the clearest structural target for the Inequality Team.

---

# 13. Integration with the Original Dynamic Rate Series

The original series separated:

$$
T_{\mathrm{search}},
T_{\mathrm{exec}},
T_{\mathrm{verify}}
$$

and studied how agents generate new representations, memories, and problem-solving strategies.

Round 15 provides a clean interface for the traditional object layer:

$$
\boxed{
\text{Discovery Dynamics}
\rightarrow
\text{Normal-Form Compilation}
\rightarrow
\text{Traditional Complexity Claim}.
}
$$

No matter how the agent invents new algorithms, as long as it claims the traditional $P=NP$, it must ultimately produce a SAT characteristic function that has a representation in P-normal form.

---

# 14. Eliminations / Corrections in This Round

## Correction 1

Error:

> All algorithms in P cannot be effectively enumerated.

Correction:

$$
\text{Whether an arbitrary machine index is polynomial is generally undecidable,}
$$

but:

$$
\boxed{
P\text{ can be effectively presented by clocked machines / ICC normal forms.}
}
$$

## Correction 2

Error:

> A sound + complete tractability language necessarily does not exist.

Correction:

It is too strong for arbitrary machine classification; however, an extensionally complete P-normal form does exist.

## Retention 1

Certificate failure cannot directly imply a lower bound, unless the certificate/normal form already has a completeness theorem for P.

## Retention 2

Historical discovery costs cannot be secretly counted into traditional runtime.

---

# 15. Battle Results for Both Sides

## Equality Team: Normal-Form Escape

New Mission:

$$
\boxed{
\text{Directly construct }t_{\mathrm{SAT}}\in\mathcal G_P.
}
$$

## Inequality Team: Grammar Invariant Program

New Mission:

$$
\boxed{
\text{Find }\mathcal I\text{ such that the complete P grammar preserves it, while SAT violates it.}
}
$$

This is more suitable for structural induction than previously chasing infinite unknown representations.

---

# 16. Score for This Round

The Equality Team acquired the Bellantoni–Cook/Cobham normal form weapon:

$$
P=NP:14
$$

The Inequality Team converged the universal quantifier into the Grammar Invariant Program:

$$
P\neq NP:14.
$$

...still a tie.

Maybe it's not score manipulation, but some kind of conservation law. *wry smile*.

The score belongs only to the game interface and has no proof significance.

---

# 17. Gateway to Round 16: Clocked Enumeration and Diagonalization Game

Next round plays directly with:

$$
\boxed{
C_1,C_2,C_3,\ldots
}
$$

Since all P-normal-form machines can be effectively enumerated, is it possible to construct:

$$
L_D
$$

to defeat them one by one, while maintaining:

$$
L_D\in NP?
$$

Must directly address:

1. Exponent Escalation;
2. Universal Simulation Overhead;
3. NP Witness Preservation;
4. Self-reference / indexing;
5. Relativization Barrier;
6. Why ordinary time hierarchy diagonalization has not already yielded $P\neq NP$.

---

# 18. External Theoretical References

1. Stephen Bellantoni, Stephen A. Cook, **A New Recursion-Theoretic Characterization of the Polytime Functions**, *Computational Complexity* 2 (1992), 97–110.
2. Alan Cobham, polynomial-time functions via bounded recursion on notation.
3. David Gajser, **Verifying Time Complexity of Turing Machines**, *Theoretical Computer Science* 600 (2015), 86–97.
4. Martin Avanzini, Naohi Eguchi, Georg Moser, **A New Order-theoretic Characterisation of the Polytime Computable Functions**.
5. Implicit Computational Complexity literature on safe recursion, tiering and syntactic characterizations of FP/PTIME.

---

## Ruling for This Round

$$
\boxed{
\text{A complete P normal-form language is not a fantasy; the real difficulty is putting SAT into it, or proving it can never be put in.}
}
$$

More precisely:

$$
\boxed{
\text{Machine-index verification}
\neq
\text{Extensional P presentation}.
}
$$

This distinction corrects an overly pessimistic tendency from Round 14, and also provides both teams with the cleanest dual tasks to date:

$$
\boxed{
P=NP:\quad\text{Construct a P-normal form for SAT};
}
$$

$$
\boxed{
P\neq NP:\quad\text{Find a semantic invariant preserved by the complete P grammar, but violated by SAT}.
}
$$