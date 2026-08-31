"""
Verification for NS_X72 Round 71.

Exact / rigorous checks:
1. secant Riccati difference identity (random matrix algebra audit);
2. exact coefficient tail monotonicity and bounds
      |b_n/A4_n| <= 14 n^4      on K_- for n>=100,
      |b_n/A4_n| <= 0.054 n^4   on K_+ for n>=100;
3. analytic discrete-envelope budget
      sum_{n>=N} nu*n^2 exp(-c*nu*(n^3-N^3)) < 34
   for c=0.01 (a stronger c=0.02 is used in the final candidate);
4. corrected affine-endpoint central quotient and the conditional
   central-cone bridge:
      ||R_1(nu)-R_1(0)||_max <= 8e4 nu
   is sufficient for the Round68 sign cones when 0<nu<=1e-6;
5. numerical corrected affine-Jost secant slopes down to nu=1e-9.

The final uniform directional Green-factor cone remains open.  The displayed
secant slopes are diagnostics, not the missing theorem.
"""
from pathlib import Path
import contextlib, io, math, runpy
import numpy as np
import sympy as sp

# ------------------------------------------------------------------
# Pinned dependencies.
# ------------------------------------------------------------------

def sha256(path):
    import hashlib
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

assert sha256(
    "/mnt/data/verify_NS_X72_Round58_SmallViscosityEndpoint_2026-08-17.py"
) == "f12e920dd2f4c17cd43166ec437a50ff7804a5526e50f1a33cab8b7ef5fb806d"

assert sha256(
    "/mnt/data/verify_NS_X72_Round69_RankOneScatteringTangent_2026-08-18.py"
) == "8f40973ca8d4d5b4bffa7d601efe22c62820562b6714f92f6fbe18d0af2ebb46"

# ------------------------------------------------------------------
# Exact coefficient construction from Round 58.
# ------------------------------------------------------------------

src=Path("/mnt/data/verify_NS_X72_Round58_SmallViscosityEndpoint_2026-08-17.py")
code=src.read_text(encoding="utf-8")
cut=code.split('with OUT.open("w"',1)[0]
env={}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(cut,str(src),"exec"),env)

A=env["A"]
b=env["b"]
Ksym=env["K"]
nsym=env["n"]

ratio=sp.factor(b/A[4]/nsym**4)

sqrt17=sp.sqrt(17)
Km=sqrt17-3
Kp=sqrt17+3

x=sp.symbols("x", nonnegative=True)
nn=sp.symbols("nn", positive=True)

def prove_decreasing_and_bound(Kv,bound):
    rr=sp.simplify(ratio.subs({Ksym:Kv,nsym:nn}))
    dr=sp.factor(sp.diff(rr,nn))
    num,den=sp.fraction(dr)

    numpoly=sp.Poly(
        sp.expand(
            num.subs(nn,x+100)
        ),
        x,
        extension=sqrt17,
    )
    denpoly=sp.Poly(
        sp.expand(
            den.subs(nn,x+100)
        ),
        x,
        extension=sqrt17,
    )

    assert all(
        sp.sign(c)==-1
        for c in numpoly.all_coeffs()
    )
    assert all(
        sp.sign(c)==1
        for c in denpoly.all_coeffs()
    )

    r100=sp.simplify(
        rr.subs(nn,100)
    )
    assert sp.sign(
        sp.Rational(bound[0],bound[1])
        - r100
    )==1

    return float(sp.N(r100,25))

r100_minus=prove_decreasing_and_bound(
    Km,
    (14,1),
)
r100_plus=prove_decreasing_and_bound(
    Kp,
    (54,1000),
)

# ------------------------------------------------------------------
# Secant Riccati identity algebra audit.
# ------------------------------------------------------------------

rng=np.random.default_rng(1234)

for _ in range(50):
    C=rng.normal(size=(3,3))
    D=rng.normal(size=(3,3))
    B=rng.normal(size=(3,3))
    A0=rng.normal(size=(3,3))
    E=rng.normal(size=(3,3))
    eps=1e-4

    R0n=rng.normal(size=(3,3))
    Rvn=R0n+eps*rng.normal(size=(3,3))

    X0=R0n@C-A0
    Av=A0+eps*E
    Xv=Rvn@C-Av

    if abs(np.linalg.det(X0))<1e-3 or abs(np.linalg.det(Xv))<1e-3:
        continue

    R0=np.linalg.solve(
        X0,
        B-R0n@D,
    )
    Rv=np.linalg.solve(
        Xv,
        B-Rvn@D,
    )

    lhs=Rv-R0
    rhs=np.linalg.solve(
        Xv,
        eps*E@R0
        -(Rvn-R0n)@(C@R0+D),
    )

    assert np.max(
        np.abs(lhs-rhs)
    ) < 5e-10

# ------------------------------------------------------------------
# Analytic scalar summation budget.
# ------------------------------------------------------------------

# For h(x)=nu*x^2 exp(-c nu(x^3-N^3)),
# integral_N^inf h dx = 1/(3c).
# For a nonnegative unimodal h, sum over integers is <= integral + sup h.
# At c=.01, nu<=1e-6, N>=100 the supremum is <0.1.
c=0.01
integral=1/(3*c)

# sup of nu*x^2 exp(-c*nu*(x^3-N^3))
# <= e^(c*nu*N^3) * nu^(1/3)*(2/(3c))^(2/3)*e^(-2/3).
nu_max=1e-6
N0=100
sup_bound=(
    math.exp(c*nu_max*N0**3)
    * nu_max**(1/3)
    * (2/(3*c))**(2/3)
    * math.exp(-2/3)
)

assert integral < 33.34
assert sup_bound < 0.1
assert integral+sup_bound < 34

# Candidate Round71 budget uses c=.02:
# center to N*=2 nu^(-1/3), Green factor <=200, coefficient <=14n^4.
# center contribution <= 14*200*(8/3 + tiny)*nu, tail <=14*200/(3*.02)*nu.
# A deliberately rounded budget below 5.5e4 nu is enough.
center_budget=14*200*3.0
tail_budget=14*200/(3*0.02)
assert center_budget < 8401
assert tail_budget < 46667
assert center_budget+tail_budget < 5.51e4

# ------------------------------------------------------------------
# Corrected endpoint chart + central secant cone.
# ------------------------------------------------------------------

# Load Round69 in silence; it recomputes the certified endpoint-affine graph.
with contextlib.redirect_stdout(io.StringIO()):
    r69=runpy.run_path(
        "/mnt/data/verify_NS_X72_Round69_RankOneScatteringTangent_2026-08-18.py"
    )

endpoint=r69["endpoint"]
R0_map=r69["R0"]
endpoint_shear=r69["endpoint_shear"]
graph_from_plane=r69["graph_from_plane"]
stable_plane=r69["stable_plane"]
kval=r69["kval"]
A2f=r69["A2"]
A4f=r69["A4"]
bcoef=r69["bcoef"]

def central_constants(name):
    K=kval(name)
    d=endpoint[name]
    R0=R0_map[name]

    b1=bcoef(K,1)
    a2=A2f(K,1)
    a4=A4f(K,1)

    # after the endpoint shear:
    # base = (e0, tilde_o2, o0)
    # output=(e2,e1,tilde_o1)
    cden0=(
        a4
        - b1*R0[1,1]
        - a2*R0[2,1]
    )

    L=abs(b1)+abs(a2)

    return {
        "e10":d["e1"],
        "o20":d["o2"],
        "den0":cden0,
        "L":L,
    }

ccm=central_constants("minus")
ccp=central_constants("plus")

assert ccm["e10"] < -0.917
assert 4.16 < ccm["o20"] < 4.17
assert ccm["den0"] > 0.62
assert ccm["L"] < 5.21

assert ccp["e10"] < -0.766
assert 3.71 < ccp["o20"] < 3.73
assert ccp["den0"] < -4.47
assert ccp["L"] < 33.1

# Conditional displacement radius:
# ||Rnu-R0||_max <= 8e4 nu, nu<=1e-6 => delta<=0.08.
delta=0.08

# Small fibre:
den_m=ccm["den0"]-ccm["L"]*delta
num_m=ccm["L"]*delta
x_m=num_m/den_m
e1_upper_m=ccm["e10"]+delta+delta*x_m
o2_lower_m=ccm["o20"]-x_m
o2_upper_m=ccm["o20"]+x_m

assert den_m > 0.20
assert x_m < 2.1
assert e1_upper_m < -0.6
assert o2_lower_m > 2.0
assert o2_upper_m < 7.0

# Large fibre:
den_p=abs(ccp["den0"])-ccp["L"]*delta
num_p=ccp["L"]*delta
x_p=num_p/den_p
e1_upper_p=ccp["e10"]+delta+delta*x_p
o2_lower_p=ccp["o20"]-x_p

assert den_p > 1.8
assert x_p < 1.5
assert e1_upper_p < -0.5
assert o2_lower_p > 2.0

# Thus the Round68 central cones remain valid under delta<=.08.

# ------------------------------------------------------------------
# Corrected affine-Jost secant slope diagnostics.
# ------------------------------------------------------------------

rows=[]

for name in ("minus","plus"):
    S=endpoint_shear(name)
    R0=R0_map[name]

    for nu in (
        1e-6,
        3e-7,
        1e-7,
        3e-8,
        1e-8,
        1e-9,
    ):
        J=max(
            3000,
            int(
                20*nu**(-1/3)
            ),
        )

        Q=stable_plane(
            name,
            nu,
            J,
        )
        Qs,_=np.linalg.qr(
            S@Q
        )
        R,cond=graph_from_plane(
            Qs
        )

        D=R-R0
        sv=np.linalg.svd(
            D,
            compute_uv=False,
        )

        rows.append({
            "fibre":name,
            "nu":nu,
            "J":J,
            "chart_cond":cond,
            "max_entry_secant_slope":
                np.max(np.abs(D))/nu,
            "sigma1_over_nu":
                sv[0]/nu,
            "sigma2_over_nu":
                sv[1]/nu,
            "sigma3_over_nu":
                sv[2]/nu,
        })

for name in ("minus","plus"):
    sub=[
        r for r in rows
        if r["fibre"]==name
    ]
    if name=="minus":
        assert max(
            r["max_entry_secant_slope"]
            for r in sub
        ) < 117
    else:
        assert max(
            r["max_entry_secant_slope"]
            for r in sub
        ) < 13.1

print("Round 71 verification passed.")
print("coefficient ratios at n=100:",r100_minus,r100_plus)
print("sum envelope integral+sup:",integral+sup_bound)
print("candidate n>=100 local budget:",center_budget+tail_budget)
print("central secant cone x-bounds:",x_m,x_p)
for r in rows:
    print(r)
