# 03 | Algorithm 1 Soundness Gates

## S1 — Analytic $\Sha$ must not be misrepresented as actual $\Sha$

The `sha` field can be used as an analytic prediction / gate input; the certificate must preserve the descent provenance.

## S2 — $\dim\Sha[2]$ must not be misrepresented as $\operatorname{ord}_2\#\Sha$

The current security policy accepts $\operatorname{BSD}(E,2)$ only when:

$$
v_2(\Sha_{\mathrm{an}})=0
$$

and the descent pins:

$$
\Sha[2]=0
$$

A positive valuation must be marked as `OPEN / higher 2-power descent needed`.

## S3 — Timeout is UNKNOWN

An mwrank timeout is not a theorem failure.

## S4 — Testing flag contamination

When `skip_filter_S` or `skip_BSD_at_2_check` is enabled, the entire run certificate is automatically downgraded.

## S5 — Deterministic theorem gate

The $\mathcal S\ne\varnothing$ production gate uses a deterministic criterion; bounded search is only used as a cross-check / witness.

## S6 — Provenance

Each PASS records:

```text
predicate
value
evidence_type
backend
semantic_version
file/commit SHA
timestamp
```