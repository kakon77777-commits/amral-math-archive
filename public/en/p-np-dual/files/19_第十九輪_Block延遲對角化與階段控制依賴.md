# P/NP Debate Game Research Area | Round 19

## Block / Delayed Diagonalization: Density Escape, Stage Control, and Conditional Progress

**Block and Delayed Diagonalization: Density Escape, Stage Control, and Conditional Progress**

- **Lead Researcher:** Neo.K (Hsu Chuan-Wei)
- **Collaborative Organization:** Aletheia
- **Institution:** EveMissLab (Yiyannuo Technology Co., Ltd.)
- **Date:** August 1, 2026
- **Version:** v1.0
- **Research Status:** Round 19 Dual-Hypothesis Rehearsal
- **Prerequisite Document(s):** `18_Round_18_Diagonal_Slice_Compression_and_Sparsity_Upward_Separation_Trap.md`
- **Game Stance:** The research has entered the "monster zone of complexity theory," but all conclusions will continue to be strictly stratified.

---

## Abstract

Round 18 discovered: If the diagonal slice only allocates a few designated points to each P machine, the constructed language easily becomes sparse/tally-like; if this sparse language truly falls in $NP-P$, Hartmanis–Immerman–Sewelson's upward-separation result would trigger a higher deterministic/nondeterministic single-exponential time separation. Conversely, if the diagonal family is made too dense, it easily reverts to the uniform exponent barrier and universalization complexity jump of Rounds 16 and 17.

This round therefore tests a natural middle path: instead of single-point diagonalization, it uses length blocks, stages, and delay mechanisms. Let

$$
I_s=[N_s,N_{s+1})
$$

be the $s$-th length block, allowing the language to exhibit different patterns in different blocks, such as SAT-like, empty-like, or some computable local pattern. Intuitively, if SAT-like blocks appear infinitely often and are sufficiently wide, the language can avoid the sparse barrier; if each requirement is only processed at an extremely late stage, it seems possible to buy time for expensive diagonalization.

The result of this round is: **block/delay can indeed avoid the structural trap of being "too sparse," but it cannot eliminate the unbounded polynomial exponent on the same input simply by waiting.** For any fixed $K$ and $k>K$, there is no such thing as "waiting until $n$ is large enough" to make

$$
n^k\le n^K
$$

hold; therefore, the Uniform Exponent Barrier from Round 16 does not disappear just because the block becomes larger.

The real trick of Ladner's delayed diagonalization is not "waiting until the input is large enough to forcefully simulate all high-exponent machines," but rather changing the control mechanism of the construction: the language switches extremely slowly between SAT-like and easy-like phases, and the phase controller only advances after finding a finite counterexample/requirement witness. If we assume $P\neq NP$, the corresponding counterexamples will exist, so the controller will continue to advance; if a certain stage freezes permanently, it usually indicates that a candidate P machine/reduction has succeeded, leading to the originally assumed collapse. That is:

$$
\boxed{
\text{The progress of delayed diagonalization is itself conditional.}
}
$$

This forms the **Freeze-or-Separate Principle (FSP)** of this round:

$$
\text{controller freezes permanently}
\Rightarrow
\text{corresponding collapse / successful simulation event},
$$

$$
\text{controller advances infinitely}
\Rightarrow
\text{diagonal requirements can be satisfied item by item}.
$$

Ladner's theorem is precisely a beautiful example: under the assumption that $P\neq NP$, delayed diagonalization can be used to construct an NP-intermediate language; but this is not a proof of $P\neq NP$, because "the stage always advances" is exactly guaranteed by $P\neq NP$.

This round therefore refines the Density--Uniformity Squeeze from the previous round into a more precise triangular pressure:

$$
\boxed{
\text{Density}
\;\text{vs.}\;
\text{Uniform Exponent}
\;\text{vs.}\;
\text{Stage-Control Knowledge}
}
$$

Round 19 did not achieve a separation, but it found the true location where delayed diagonalization hides its costs: **not the block size, but the evidence required for the stage controller to know when it is safe to advance.** Round 19 thus pushes Round 20 to: Stage Controller Complexity—if we want the controller to advance unconditionally, efficiently, and forever, what exactly does it need to know? Will this controller secretly turn into a SAT/P-equivalence oracle?

---

# 1. Previous Round: Why Change from "Points" to "Blocks"?

The diagonal slice from Round 18:

$$
D=\{x_i:C_i(x_i)=0\}
$$

has two problems.

First, if each machine is allocated very few designated inputs, $D$ easily becomes sparse.

Second, if we directly require:

$$
D(x_i)=1-C_i(x_i),
$$

then to compute $D(x_i)$, we might have to pay:

$$
|x_i|^{k_i},
$$

where $k_i$ is unbounded.

Thus, blocks are proposed:

$$
I_s=[N_s,N_{s+1}).
$$

hoping to use a large length interval to handle the $s$-th requirement, rather than just a single point.

---

# 2. First Thought Experiment: Direct Block Diagonalization

The most direct fantasy is:

In the $s$-th block, for all $x$, define:

$$
D(x)=1-C_s(x).
$$

This way, the entire block is opposite to $C_s$, which naturally guarantees:

$$
D\neq C_s.
$$

But if:

$$
T_{C_s}(n)=n^{k_s},
$$

then deciding $D(x)$ in this block still requires:

$$
n^{k_s}.
$$

Even if:

$$
N_s
$$

is chosen to be enormously large, it cannot make a fixed global $K$ satisfy:

$$
n^{k_s}\le n^K
$$

for all $s$.

---

# 3. Same-Input Exponent Invariance

## Proposition 3.1

Given:

$$
k>K.
$$

then for all:

$$
n>1,
$$

we have:

$$
n^k>n^K.
$$

Therefore, there does not exist a threshold $N$ such that:

$$
\forall n\ge N,
\quad n^k\le n^K.
$$

This seems like nonsense, but it is crucial for block diagonalization.

It illustrates:

$$
\boxed{
\text{"Waiting a bit longer" cannot fix the exponent mismatch on the same input.}
}
$$

This round denotes it as:

$$
\boxed{\mathrm{SIEI}=\text{Same-Input Exponent Invariance}.}
$$

Therefore, if delayed diagonalization is to be effective, what it must do is not:

> Delay the same expensive simulation to a larger input of the same length.

But rather:

> Change the simulated target, input scale, requirement design, or let the unfinished requirement temporarily not affect the current membership computation.

This is the fundamental difference between Ladner-style delay and naive waiting.

---

# 4. Second Fantasy: Amplifying a Single Diagonal Bit into an Entire Dense Block

Suppose we first obtain a bit:

$$
b_s=1-C_s(y_s),
$$

and then define:

$$
\forall x\in I_s,
\quad
D(x)=b_s.
$$

This way, using only one diagonal event, we can fill the entire block as:

$$
\emptyset
$$

or:

$$
\Sigma^{I_s},
$$

which seems to immediately avoid being sparse.

But the membership algorithm must know:

$$
b_s.
$$

If computing $b_s$ still requires an expensive simulation, the cost is merely shifted from "every x" to the "block controller."

Thus, we introduce:

$$
\boxed{\mathrm{AKD}=\text{Amplification Knowledge Debt}.}
$$

Namely:

$$
\text{Amplifying a hard bit into many strings}
$$

does not make the hard bit any easier.

If $b_s$ is easy to compute, then density amplification is easy; but the diagonal power may also vanish as a result.

---

# 5. Third Fantasy: As Long as the Language is Dense Enough, It Will Be Harder

False.

For example:

$$
L=\{x:|x|\text{ is even}\}
$$

is extremely dense, but:

$$
L\in P.
$$

Or the block language:

$$
L=\bigcup_{s\text{ even}}\{0,1\}^{I_s}
$$

can similarly oscillate in density, yet remain trivial.

Therefore:

$$
\boxed{
\text{Density is a barrier-management parameter, not a hardness invariant.}
}
$$

This formally eliminates the intuition that:

$$
\text{dense}
\Rightarrow
\text{hard}
$$

This round calls this:

$$
\boxed{\mathrm{DEHG}=\text{Density Escape without Hardness Gain}.}
$$

---

# 6. True Delayed Diagonalization: Not the Block, but the Controller

The core background of Ladner's theorem is:

Assume:

$$
P\neq NP.
$$

Then there exists:

$$
L\in NP
$$

such that:

$$
L\notin P,
$$

but:

$$
L
$$

is also not NP-complete.

A common way to understand this is to let $L$ switch extremely slowly across different stages/lengths between:

$$
SAT
$$

and:

$$
\emptyset
$$

or their related controlled versions.

Abstractly written as:

$$
L_g
=
\{x:x\in SAT\land g(|x|)\in A\},
$$

where:

$$
g(n)
$$

is an extremely slow-growing, computable stage function.

The real difficulty is not "making $g$ slow."

The real difficulty is:

$$
\boxed{
\text{What event allows }g\text{ to advance from stage }s\text{ to }s+1?
}
$$

---

# 7. Requirement-Driven Stage Controller

Let the sequence of requirements be:

$$
R_1,R_2,R_3,\ldots
$$

For example, alternating requirements:

- The $i$-th P machine does not equal $L$;
- The $i$-th polynomial reduction cannot prove $L$ is NP-complete;
- Or equivalently, causing a disagreement in the corresponding machine in the oracle-machine version.

The stage controller at stage $s$ does:

$$
\text{Search for a finite witness proving that }R_s\text{ has been satisfied.}
$$

After finding the witness:

$$
s\leftarrow s+1.
$$

When not found:

$$
s\text{ remains unchanged}.
$$

Key point: Language membership does not need to complete all future stages at once; it only needs to recompute "which stage we are currently at" within the resources allowed by the input length.

This is the true structure of delayed/lazy diagonalization.

---

# 8. Freeze-or-Separate Principle

This round abstracts the above logic into:

$$
\boxed{\mathrm{FSP}=\text{Freeze-or-Separate Principle}.}
$$

For a certain requirement $R_s$:

## Case A: Finding a finite disagreement witness

Then:

$$
R_s\text{ is satisfied},
$$

and the controller can advance.

## Case B: Never finding a witness

Then the candidate machine/reduction might actually succeed on all relevant inputs.

In Ladner-style constructions, this usually implies:

$$
SAT\in P
$$

or some other collapse that contradicts the assumption:

$$
P\neq NP.
$$

Therefore, under the assumption:

$$
P\neq NP,
$$

Case B is ruled out, and the stage controller must continuously advance.

Thus:

$$
\boxed{
P\neq NP
\Rightarrow
\text{all finite requirements eventually progress}.
}
$$

But note the direction of the quantifier.

Ladner's theorem uses:

$$
P\neq NP
$$

as a premise to guarantee controller progress.

It does not unconditionally deduce from:

$$
\text{controller progress}
$$

that:

$$
P\neq NP.
$$

---

# 9. Assumption-Activated Progress

This is the most important correction of this round.

Definition:

$$
\boxed{\mathrm{AAP}=\text{Assumption-Activated Progress}.}
$$

If the stage unboundedness of a construction:

$$
g(n)\rightarrow\infty
$$

requires first assuming:

$$
P\neq NP,
$$

Then the construction can prove:

> **If $P\neq NP$, then there exist languages with certain fine-grained structures.**

But this structure cannot be reversed and treated as an unconditional proof of $P\neq NP$.

This is exactly the status of Ladner's theorem.

---

# 10. Why Can Ladner Delay Do Blocks, While Naive Direct Diagonalization Cannot?

## Naive direct diagonalization

Requires computing at the moment of input $x$:

$$
1-C_i(x).
$$

Thus directly paying:

$$
|x|^{k_i}.
$$

UEB appears immediately.

## Delayed requirement construction

It does not require the membership algorithm to immediately complete at each stage:

$$
1-C_i(x)
$$

this same-input complement.

Instead:

1. The language currently maintains a known NP-safe mode;
2. The controller slowly searches for a requirement witness;
3. Only after the witness is found does it change the mode for future intervals;
4. For any fixed input, it only needs to reconstruct a finite stage history.

Therefore, what delay solves is:

$$
\boxed{
\text{construction scheduling / finite injury / stage accounting}
}
$$

Rather than:

$$
\boxed{
\text{Compressing an arbitrary }n^{k_i}\text{ into a fixed }n^K.
}
$$

---

# 11. Relationship with the Sparse Barrier of Round 18

Hartmanis–Immerman–Sewelson (1985) proved that, under their single-exponential EXPTIME/NEXPTIME notation:

$$
\boxed{
\exists\text{ sparse }S\in NP-P
\iff
EXPTIME\neq NEXPTIME.
}
$$

The paper also specifically pointed out: Ladner-style delayed diagonalization, under the sole assumption that $P\neq NP$, cannot produce a sparse $NP-P$ witness merely by modifying the construction, unless a higher-order separation is simultaneously obtained.

This is completely consistent with the results of Round 18.

So one of the true functions of the block/density schedule is:

$$
\boxed{
\text{To free the construction from being forced to be sparse.}
}
$$

For example, as long as SAT-like active blocks appear infinitely often, and each active block contains enough strings, the overall language can be non-sparse.

But:

$$
\text{non-sparse}
$$

only means you avoid SUST; it does not mean you gain a lower bound.

---

# 12. Density Schedule as a Third Resource

This round upgrades Round 18's:

$$
\text{Density--Uniformity Squeeze}
$$

to:

$$
\boxed{
\text{Density--Uniformity--Control Triangle}
}
$$

Three vertices:

## 12.1 Density

Too sparse:

$$
\rightarrow
\text{upward-separation pressure}.
$$

## 12.2 Uniform Runtime

Too direct / too universal:

$$
\rightarrow
\text{UEB / UCJ / certificate escalation}.
$$

## 12.3 Stage-Control Knowledge

If adaptive delay is used:

$$
\rightarrow
\text{the controller must know when the requirement has truly been satisfied}.
$$

Therefore, "intermediate density" is not a free third path.

It pushes the cost to:

$$
\boxed{
\text{schedule/controller knowledge}.
}
$$

---

# 13. Block Size Cannot Replace Stage Witness

Assume the requirement:

$$
R_s:
\quad
M_s\neq SAT.
$$

No matter how large the next block:

$$
I_s
$$

is set, the block size itself cannot prove:

$$
M_s\neq SAT.
$$

What truly allows the controller to advance is some:

$$
y_s
$$

such that:

$$
M_s(y_s)\neq SAT(y_s).
$$

Therefore:

$$
\boxed{
\text{geometric delay}
\neq
\text{semantic witness}.
}
$$

This round denotes the cost of needing this witness as:

$$
\boxed{\mathrm{SWD}=\text{Stage Witness Debt}.}
$$

---

# 14. The Equality Team's Counterattack: What if the Stage Freezes Forever?

The Equality Team suddenly realizes that delayed diagonalization suits them very well.

If the construction on a certain candidate machine:

$$
M_s
$$

can never find:

$$
M_s(y)\neq SAT(y),
$$

then it might be precisely because:

$$
M_s=SAT.
$$

If $M_s$ is a polynomial-time machine, this directly yields:

$$
SAT\in P.
$$

So the Equality Team's new slogan is:

> Your controller isn't moving, maybe it's not that the construction is broken; maybe it's that I won. (Smirk)

Thus, delayed diagonalization is inherently a conditional bifurcation machine:

$$
\boxed{
\text{freeze}
\quad\text{vs.}\quad
\text{progress}
}
$$

The two branches correspond to different complexity worlds, respectively.

---

# 15. The Inequality Team's Counterattack: Then Can I Make the Controller Advance Unconditionally?

This is the next truly dangerous idea.

If one could design a polynomially reconstructible controller:

$$
\mathcal C(s,n)
$$

such that it:

1. Eventually advances for every P-machine requirement;
2. Does not assume $P\neq NP$;
3. Accompanies every advance with a sound finite witness;
4. The overall constructed language remains in NP;
5. Ultimately differs from all P machines;

Then it is itself already very close to a constructive proof of:

$$
\boxed{P\neq NP}
$$

So the problem is repositioned as:

$$
\boxed{
\text{How does the stage controller know "it is safe to advance now"?}
}
$$

---

# 16. Controller Completeness Trap

If the controller's rule is:

> Advance if and only if a counterexample is found.

Then it is sound, but whether it progresses depends on whether the counterexample exists.

If changed to:

> Even if no counterexample is found, I will guess and advance at some point in time.

Then it might lose the diagonal guarantee.

If the controller can correctly judge:

$$
\forall y,
\quad
M_s(y)=SAT(y),
$$

it is judging an extremely strong semantic equivalence property.

Thus forming:

$$
\boxed{\mathrm{CCT}=\text{Controller Completeness Trap}.}
$$

- Too conservative: might freeze forever;
- Too aggressive: might miss the requirement;
- Too omniscient: the controller itself carries capabilities close to the original problem.

---

# 17. What Did Ladner's Theorem Truly Teach Us?

Not:

> "Delay can prove $P\neq NP$."

But rather:

$$
\boxed{
\text{If a separation is known, delay can mold the separation into a finer internal structure.}
}
$$

Namely:

$$
P\neq NP
\Rightarrow
\text{There are not only the P and NP-complete layers inside NP.}
$$

This is a **structure-from-separation** theorem,
not a **separation-from-structure** theorem.

This direction cannot be secretly swapped.

---

# 18. Practical Significance of This Round for Both Teams

## $P=NP$ Team

New strategy:

$$
\boxed{
\text{Find a stage requirement that can never produce a disagreement witness.}
}
$$

If the corresponding machine is a P machine deciding SAT, the controller freeze conversely becomes a candidate for an equality certificate.

Of course, proving "there is never a disagreement" is itself the difficulty.

---

## $P\neq NP$ Team

New strategy:

$$
\boxed{
\text{Uproot the progress proofs of all requirements from assumptions, turning them into unconditional structural theorems.}
}
$$

That is, to prove:

$$
\forall s,
\quad
\exists\text{ finite disagreement witness},
$$

without pre-using:

$$
P\neq NP.
$$

This is practically the core of the separation.

---

# 19. Known Barrier Review

## 19.1 Relativization

Ladner-style diagonalization / stage arguments highly rely on diagonalization; Baker–Gill–Solovay tells us that a purely relativizing diagonal argument cannot solve $P$ vs $NP$ alone.

Therefore, if the controller can truly progress unconditionally in the future, we must check whether a non-relativizing ingredient appears in it.

## 19.2 Sparse upward separation

Block/dense phases can avoid sparse witnesses, but this is merely obstacle avoidance, not a lower bound.

## 19.3 Uniform exponent

Delay does not change SIEI; if the same input still requires simulating $n^{k_i}$, UEB remains completely intact.

## 19.4 Discovery vs runtime

The controller "knowing" in the mathematician's mind that a certain requirement should have a counterexample cannot count as the language decider already having that witness.

---

# 20. Erroneous Routes Eliminated in This Round

1. "A large enough block can turn an arbitrary $n^{k_i}$ into a fixed $n^K$." — False, SIEI.
2. "Copying a diagonal bit to the entire block can increase hardness for free." — False, AKD.
3. "It is non-sparse, so it is more likely not in P." — No such inference.
4. "Ladner's theorem has already proven the existence of $NP-P$ via diagonalization." — It takes $P\neq NP$ as a premise.
5. "The stage function is very slow, so the construction is automatically feasible." — Slowness is just scheduling; progress still requires a requirement witness.
6. "As long as we wait forever, a counterexample will always appear." — Guaranteed only when the corresponding separation / non-equivalence already holds.
7. "If the controller freezes, it means the construction failed." — It might precisely mean the candidate machine truly succeeded, which is instead a signal for the Equality Team.

---

# 21. New Concepts Formally Added in This Round

$$
\boxed{\mathrm{SIEI}}
$$
Same-Input Exponent Invariance

$$
\boxed{\mathrm{AKD}}
$$
Amplification Knowledge Debt

$$
\boxed{\mathrm{DEHG}}
$$
Density Escape without Hardness Gain

$$
\boxed{\mathrm{FSP}}
$$
Freeze-or-Separate Principle

$$
\boxed{\mathrm{AAP}}
$$
Assumption-Activated Progress

$$
\boxed{\mathrm{SWD}}
$$
Stage Witness Debt

$$
\boxed{\mathrm{CCT}}
$$
Controller Completeness Trap

And:

$$
\boxed{
\text{Density--Uniformity--Control Triangle}
}
$$

---

# 22. Score of This Round

At the beginning of this round, it looked like the Inequality Team finally got their hands on the big weapon of Ladner's delayed diagonalization.

But upon closer inspection:

$$
\text{Its progress guarantee actually assumes }P\neq NP\text{ first}.
$$

The Equality Team immediately stated:

> Then when you get stuck, maybe it just means I won?

So:

$$
P=NP:18
$$

$$
P\neq NP:18.
$$

The law of conservation of score continues to hold.

This is no longer score control; this is like a Hamiltonian. (Smirk)

The score is merely a game interface and holds no proof significance.

---

# 23. Entrance to Round 20: Stage Controller Complexity

The next round will no longer study the block itself, but rather study:

$$
\boxed{
\text{Who is controlling the block?}
}
$$

Core question:

$$
\boxed{
\text{Can we design an unconditional, efficient, sound, and forever progressing stage controller?}
}
$$

Specifically broken down into:

1. How does the controller confirm that the $s$-th candidate P machine has been defeated?
2. Is a finite disagreement witness sufficient?
3. If the witness has not yet appeared, how does the controller distinguish between "just haven't found it yet" and "it never exists"?
4. If the controller can judge the latter, does it already possess the capability of a SAT/P-machine equivalence oracle?
5. Can non-relativizing algebraic / arithmetization information be used to replace pure search?
6. Does there exist a proof-carrying stage transition:

$$
(s,\pi_s)\rightarrow s+1
$$

where $\pi_s$ can be verified with a fixed polynomial overhead?
7. If all stages have short proofs, will it crash back into the universal certificate compression jump of Round 17?

Round 20 will therefore formally merge four threads:

- delayed diagonalization;
- proof certificates;
- controller knowledge;
- non-relativizing ingredients.

---

# 24. External Theoretical References

1. Richard E. Ladner, 1975/1970s NP-intermediate theorem line; modern complexity lecture notes often use delayed/lazy diagonalization to explain: if $P\neq NP$, there exist languages in NP that are neither in P nor NP-complete.

2. MIT 6.841 / 18.405J Advanced Complexity Theory, Lecture 2: Diagonalization, Ladner's Theorem, Relativization. The lecture notes explicitly demonstrate the method of constructing a Ladner language using polynomial-time oracle machines, SAT-like/empty-like behavior, and delayed requirement search.

3. J. Hartmanis, N. Immerman, V. Sewelson, **Sparse Sets in NP-P: EXPTIME versus NEXPTIME**, Information and Control 65 (1985), 158–181. This paper proves the equivalence between sparse $NP-P$ sets and the single-exponential deterministic/nondeterministic time separation they define, and explicitly discusses that Ladner's delayed diagonalization cannot produce a sparse $NP-P$ witness merely by modification, unless a higher-order separation is obtained.

4. Stephen Mahaney, **Sparse Complete Sets for NP: Solution of a Conjecture of Berman and Hartmanis**, JCSS 25 (1982). If NP has a sparse many-one complete set, then $P=NP$.

5. Baker–Gill–Solovay relativization barrier: Purely relativizing diagonalization cannot solve the original $P$ vs $NP$ alone.

---

## Verdict of This Round

$$
\boxed{
\text{Block / delay can rearrange when to pay the bill, but cannot make the bill itself disappear.}
}
$$

More precisely:

$$
\boxed{
\text{The core resource of Ladner delay is not the block size, but the stage-controller progress.}
}
$$

And if stage progress is guaranteed by:

$$
P\neq NP
$$

then one can only obtain a conditional structural theorem.

Therefore, what is truly worth attacking next is:

$$
\boxed{
\text{Stage Controller Knowledge / Proof Complexity}.
}
$$