#!/usr/bin/env python3
"""
AMRAL RH v1.3 — Li witness final scalar certificate checker.

This checker verifies ONLY the final sufficient inequality from
RH-OffAxisCell-LiWitnessCompiler v1.3.

It does NOT:
- prove an off-axis zeta zero exists,
- isolate zeta zeros,
- certify extremal membership,
- establish phase enclosures,
- prove RH false.

All numeric inputs must come from an independent rigorous interval pipeline.
For production use, replace Decimal input provenance with directed MPFR/Arb
interval objects and signed certificate metadata.
"""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal, getcontext
import json
import sys

getcontext().prec = 100


@dataclass(frozen=True)
class LiWitnessCertificate:
    n: int
    K: int
    R_lower: Decimal
    R2_upper: Decimal
    cosine_sum_lower: Decimal
    zero_count_upper: int
    Z2_upper: Decimal

    def validate_domain(self) -> None:
        if self.n < 1:
            raise ValueError("n must be >= 1")
        if self.K < 1:
            raise ValueError("K must be >= 1")
        if self.zero_count_upper < self.K:
            raise ValueError("zero_count_upper must be >= K")
        if not (self.R_lower > Decimal(1)):
            raise ValueError("R_lower must be > 1")
        if not (self.R2_upper >= Decimal(1)):
            raise ValueError("R2_upper must be >= 1")
        if not (self.R2_upper < self.R_lower):
            raise ValueError("require R2_upper < R_lower")
        if not (self.cosine_sum_lower > Decimal(0)):
            raise ValueError("cosine_sum_lower must be > 0")
        if self.cosine_sum_lower > Decimal(self.K):
            raise ValueError("cosine_sum_lower cannot exceed K")
        if self.Z2_upper < 0:
            raise ValueError("Z2_upper must be nonnegative")


def exp_half_decimal() -> Decimal:
    # Decimal.exp is available in modern Python.
    return (Decimal("0.5")).exp()


def check_certificate(cert: LiWitnessCertificate) -> dict:
    cert.validate_domain()

    n = cert.n
    K = cert.K

    c0 = Decimal(1) + exp_half_decimal() / Decimal(2)

    extremal_lower = (cert.R_lower ** n) * cert.cosine_sum_lower

    mid_upper = (
        Decimal(cert.zero_count_upper - K)
        * (Decimal(1) + cert.R2_upper ** n)
    )

    tail_upper = c0 * Decimal(n * n) * cert.Z2_upper

    rhs_upper = Decimal(K) + mid_upper + tail_upper
    margin_lower = extremal_lower - rhs_upper

    return {
        "n": n,
        "K": K,
        "c0": str(c0),
        "extremal_lhs_lower": str(extremal_lower),
        "mid_upper": str(mid_upper),
        "tail_upper": str(tail_upper),
        "rhs_upper": str(rhs_upper),
        "margin_lower": str(margin_lower),
        "verdict": "NEGATIVE_LI_WITNESS_SUFFICIENT"
        if margin_lower > 0
        else "NOT_CERTIFIED",
    }


def from_json(obj: dict) -> LiWitnessCertificate:
    return LiWitnessCertificate(
        n=int(obj["n"]),
        K=int(obj["K"]),
        R_lower=Decimal(str(obj["R_lower"])),
        R2_upper=Decimal(str(obj["R2_upper"])),
        cosine_sum_lower=Decimal(str(obj["cosine_sum_lower"])),
        zero_count_upper=int(obj["zero_count_upper"]),
        Z2_upper=Decimal(str(obj["Z2_upper"])),
    )


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: li_witness_certificate_checker.py certificate.json")
        return 2

    with open(sys.argv[1], "r", encoding="utf-8") as f:
        obj = json.load(f)

    cert = from_json(obj)
    result = check_certificate(cert)
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0 if result["verdict"] == "NEGATIVE_LI_WITNESS_SUFFICIENT" else 1


if __name__ == "__main__":
    raise SystemExit(main())
