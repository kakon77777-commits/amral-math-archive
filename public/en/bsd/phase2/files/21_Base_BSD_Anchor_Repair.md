# 21｜Base BSD Anchor Repair

## The Issue with v0.3

Banwait–Huang's historical review states:

> Miller verified full BSD for **most** rank 0/1 curves below conductor 5000.

Therefore, we cannot use:

$$
696<5000
$$

to directly deduce that Miller personally verified `696.e1`.

## Correct source

Creutz–Miller, *Second Isogeny Descents and the BSD Conjectural Formula*,
Theorem 1.1:

$$
\boxed{
N<5000,\quad r_{\rm an}\le1
\Longrightarrow
\text{full BSD}.
}
$$

`696.e1`:

$$
N=696,\qquad r_{\rm an}=0.
$$

Thus, full BSD(E) holds; in particular:

$$
\boxed{\operatorname{BSD}(E,2).}
$$

This is a strict source-level repair, which no longer relies on the analytic Sha masquerading as the actual Sha.