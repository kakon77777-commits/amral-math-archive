# 04 | Execution Environment and Missing Items for Algorithm 1

## Requirements for a Complete Rerun

- SageMath;
- LMFDB local database;
- `lmfdb` Python package and configuration;
- pandas / numpy;
- PARI 2-descent;
- mwrank;
- Sage native 2-isogeny descent;
- Sufficient memory and local data.

---

# Incomplete Items in the Current Environment

Not included in this round:

- Connecting to the local LMFDB PostgreSQL;
- Executing Sage;
- Executing 2-descent;
- Rescanning conductor $<500000$;
- Independently verifying the official 36,687 curve count.

Therefore, we cannot state:

```text
Full Algorithm 1 independently reproduced.
```

---

# Completed Alternative Work

1. Breaking down theorem conditions item by item;
2. Reading the current official implementation;
3. Auditing certificate strength;
4. Obtaining official small-sample fixtures;
5. Independently reproducing Algorithm 2;
6. Establishing the Sage execution plan for the next round.

---

# Minimum Environment Testing for Phase 1 v0.2

First, execute:

```bash
sage -python Algorithm1.py --cond_upper_bound 150
```

The expected output is twelve base curves.

Then, execute:

```bash
sage -python Algorithm2.py output/ec_labels_150.txt
```

Compare:

- curve labels;
- source branch;
- twists up to $1000$;
- file SHA;
- pass/fail metadata.

Proceeding to 500K is only allowed after the small sample is completely consistent.