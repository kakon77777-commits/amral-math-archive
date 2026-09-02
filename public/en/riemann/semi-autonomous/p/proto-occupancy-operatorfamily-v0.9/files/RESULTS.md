# Results

## 1. Exact semantic bridge

`OccupancySelectionOperatorTransfer` has been closed at the symbolic level:

$$
\text{cell occupancy}
+
\text{universal selected family}
\Longrightarrow
\text{all-point operator positivity}.
$$

It does not allow the following substitution:

$$
\text{count lower}
\rightsquigarrow
\text{arbitrary measure operator mass}.
$$

## 2. Count-only exact failure

In the Dirichlet Green model, when the total count is also $2$ but both points are located at $1/5$:

| quantity | exact value |
| --- | ---: |
| Schur determinant | $-254/558009$ |
| certified negative quadratic | $-663194/13755479859$ |
| operator PSD | false |

Therefore, "having two points" and "having one point in each of the left and right cells" possess different operator semantics.

## 3. Exact adaptive cover

| quantity | result |
| --- | ---: |
| root box directly certified | false |
| total tree nodes | $15$ |
| certified leaves | $8$ |
| unresolved leaves | $0$ |
| maximum leaf depth | $7$ |
| minimum first-minor lower | $936790565/9707986602$ |
| minimum determinant lower | $996149099768633906407318481/92259342242007809509970517515625$ |

The root box failure is an interval dependency failure; after the cover family succeeds, the synthesized uncertain-location operator family is strictly positive for all locations.

## 4. Conditional clamped $58$-cell family

| quantity | exact value |
| --- | ---: |
| parent alpha | $21/20$ |
| child alpha | $1$ |
| convex margin | $1/21$ |
| independent location cells | $58$ |
| uniform half-width | $1/500000000000000$ |
| perturbation upper | $12328822128706060288/299401138693037109375$ |
| coercivity lower | $13498624663403281109/2095807970851259765625$ |
| budget critical half-width | $10219558867389/4418649850928252007219200000$ |

Under the parent v0.7 abstract theorem, this is an exact universal location family certificate. It remains a coordinate-dependent dual-atom calibration, not an actual zero occupancy.

## 5. Floating adversarial corner study

| cell half-width | adversarial threshold at $\Delta t=0.02$ |
| ---: | ---: |
| $0.012$ | $1.0458517424$ |
| $0.014$ | $1.0240427949$ |
| $0.015$ | $1.0124640056$ |
| $0.016$ | $1.0004604738$ |
| $0.017$ | $0.9880516263$ |
| $0.018$ | $0.9748129050$ |
| $0.020$ | $0.9471623347$ |

The finest-step values for fixed corners are:

| half-width | $\Delta t=0.005$ threshold |
| ---: | ---: |
| $0.015$ | $1.0124737413$ |
| $0.016$ | $1.0004702150$ |
| $0.017$ | $0.9880613743$ |

These numbers only describe a deterministic corner search, without a universal quantifier.

## 6. Decisions

Retain the occupancy/operator-family main thread; the next node will not revert to pursuing a finer scalar count profile. Prioritize the development of local interval clamped-Green derivative bounds and adaptive location-cell Schur covers to narrow the proof-budget gap of approximately $8\times10^{12}$.

The $\zeta$ occupancy presence theorem and the upper-envelope no-go source certification are maintained as two independent lines of work.