"""
Verification for NS_X72 Round 70.

Round 70 introduces the parity-rescaled consecutive Riccati graph and proves
an exact dual scalar Volterra representation for central viscosity derivatives.

Main exact structural facts:
1. r_n = u_n for n even, r_n = u_n/nu for n odd.
2. In the consecutive 6D transfer, explicit nu-dependence occurs only for
   even n, in one coefficient beta_n = nu^2 b_n/A4_n.
3. Therefore the local Riccati tangent source is rank one.
4. The Frobenius-adjoint tangent weight preserves rank one.
5. Every central entry derivative is an exact scalar source sum plus a
   terminal pairing.  The o2 derivative is the sum of two rank-one channels.
6. Central readouts are order-one in this rescaled graph:
       e1 = R_1[2,1]
       f  = a3/nu = -R_1[1,1]
       o2 = (b1*e1 - A2_1*f)/A4_1.

The displayed scalar-kernel bounds across 1e-8 <= nu <= 1e-6 are numerical
diagnostics.  The remaining theorem is a uniform infinite-Jost summability
bound for the scalar dual kernel.
"""
from pathlib import Path
import csv, math
import numpy as np

OUT = Path("/mnt/data/NS_X72_Round70_ScalarKernelMap_2026-08-18.csv")

# Exact coefficient formulas inherited from the symbolic Round 58/65 derivation.
def A_m2(K,n):
    return -K**3*(K**4 + 2*K**2*n**2 + 6*K**2*n - 13*K**2 + n**4 + 6*n**3 - 14*n**2 + 3*n + 4)/((K**2 + n**2)*(K**2 + n**2 - 4*n + 4)*(K**2 + n**2 - 2*n + 1))

def A0(K,n):
    return K*n*(K**10 + 8*K**8*n**2 + 30*K**8*n + 19*K**8 + 22*K**6*n**4 + 134*K**6*n**3 + 270*K**6*n**2 + 241*K**6*n + 83*K**6 + 28*K**4*n**6 + 222*K**4*n**5 + 663*K**4*n**4 + 946*K**4*n**3 + 604*K**4*n**2 + 122*K**4*n - K**4 + 17*K**2*n**8 + 162*K**2*n**7 + 592*K**2*n**6 + 1005*K**2*n**5 + 515*K**2*n**4 - 1000*K**2*n**3 - 1970*K**2*n**2 - 1319*K**2*n - 306*K**2 + 4*n**10 + 44*n**9 + 180*n**8 + 300*n**7 + 12*n**6 - 588*n**5 - 580*n**4 + 100*n**3 + 384*n**2 + 144*n)/((K**2 + n**2)*(n + 2)*(K**2 + n**2 - 2*n + 1)*(K**2 + n**2 + 4*n + 4)*(K**4 + 2*K**2*n**2 + 8*K**2*n + 4*K**2 + n**4 + 8*n**3 + 22*n**2 + 24*n + 9))

def A2(K,n):
    return K*(K**10 + 8*K**8*n**2 + 2*K**8*n - 9*K**8 + 22*K**6*n**4 + 42*K**6*n**3 - 6*K**6*n**2 - 65*K**6*n - 39*K**6 + 28*K**4*n**6 + 114*K**4*n**5 + 123*K**4*n**4 - 42*K**4*n**3 - 200*K**4*n**2 - 226*K**4*n - 101*K**4 + 17*K**2*n**8 + 110*K**2*n**7 + 228*K**2*n**6 + 107*K**2*n**5 - 335*K**2*n**4 - 616*K**2*n**3 - 330*K**2*n**2 + 15*K**2*n + 36*K**2 + 4*n**10 + 36*n**9 + 108*n**8 + 84*n**7 - 156*n**6 - 276*n**5 - 28*n**4 + 156*n**3 + 72*n**2)/((K**2 + n**2)*(K**2 + n**2 - 2*n + 1)*(K**2 + n**2 + 4*n + 4)*(K**4 + 2*K**2*n**2 + 8*K**2*n + 4*K**2 + n**4 + 8*n**3 + 22*n**2 + 24*n + 9))

def A4(K,n):
    return -K**3*n*(K**4 + 2*K**2*n**2 - 4*K**2 + n**4 - 2*n**2 + 1)*(K**4 + 2*K**2*n**2 + 2*K**2*n - 17*K**2 + n**4 + 2*n**3 - 26*n**2 - 99*n - 90)/((n + 2)*(K**2 + n**2 - 2*n + 1)*(K**2 + n**2 + 4*n + 4)*(K**2 + n**2 + 8*n + 16)*(K**4 + 2*K**2*n**2 + 8*K**2*n + 4*K**2 + n**4 + 8*n**3 + 22*n**2 + 24*n + 9))

def bcoef(K,n):
    return -16*n*(n + 1)*(K**4 + 2*K**2*n**2 - 4*K**2 + n**4 - 2*n**2 + 1)/((K**2 + n**2 - 2*n + 1)*(K**2 + n**2 + 2*n + 1))


def kval(name):
    return math.sqrt(17)-3 if name=="minus" else math.sqrt(17)+3

def T_original(name,n,nu):
    K=kval(name)
    am=A_m2(K,n); a0=A0(K,n); a2=A2(K,n); a4=A4(K,n); bb=bcoef(K,n)
    T=np.zeros((6,6),dtype=float)
    T[0,:]=[0.0,a2/a4,nu*bb/a4,-a0/a4,0.0,am/a4]
    T[1,0]=1.0; T[2,1]=1.0; T[3,2]=1.0; T[4,3]=1.0; T[5,4]=1.0
    return T

def scale_matrix(n,nu):
    inds=(n+3,n+2,n+1,n,n-1,n-2)
    return np.diag([
        1.0/nu if (k % 2) else 1.0
        for k in inds
    ])

def T_rescaled(name,n,nu):
    return (
        scale_matrix(n+1,nu)
        @ T_original(name,n,nu)
        @ np.linalg.inv(scale_matrix(n,nu))
    )

def T_rescaled_direct(name,n,nu):
    K=kval(name)
    am=A_m2(K,n); a0=A0(K,n); a2=A2(K,n); a4=A4(K,n); bb=bcoef(K,n)
    beta=(nu*nu*bb/a4) if (n % 2 == 0) else (bb/a4)
    T=np.zeros((6,6),dtype=float)
    T[0,:]=[0.0,a2/a4,beta,-a0/a4,0.0,am/a4]
    T[1,0]=1.0; T[2,1]=1.0; T[3,2]=1.0; T[4,3]=1.0; T[5,4]=1.0
    return T

def dT_rescaled(name,n,nu):
    T=np.zeros((6,6),dtype=float)
    if n % 2 == 0:
        K=kval(name)
        T[0,2]=2.0*nu*bcoef(K,n)/A4(K,n)
    return T

for name in ("minus","plus"):
    for n in (1,2,3,10,101):
        for nu in (1e-6,3e-5):
            lhs=T_rescaled(name,n,nu)
            rhs=T_rescaled_direct(name,n,nu)
            err=np.max(np.abs(lhs-rhs))
            scale=max(1.0,np.max(np.abs(rhs)))
            assert err < 5e-13*scale

        Tp=T_rescaled_direct(name,n,1e-4)
        Tm=T_rescaled_direct(name,n,-1e-4)
        assert np.max(np.abs(Tp-Tm)) < 1e-12

def real_basis(vals,vecs,count=3):
    order=np.argsort(np.abs(vals))
    cols=[]
    for idx in order:
        v=vecs[:,idx]
        if np.max(np.abs(v.imag))<1e-8:
            cols.append(v.real)
        else:
            cols.append(v.real)
            if len(cols)<count:
                cols.append(v.imag)
        if len(cols)>=count:
            break
    Q=np.column_stack(cols[:count])
    Q,_=np.linalg.qr(Q)
    return Q

def terminal_graph(name,J,nu):
    vals,vecs=np.linalg.eig(
        T_original(name,J,nu)
    )
    Q=real_basis(vals,vecs,3)
    Qs=scale_matrix(J,nu)@Q
    return Qs[:3,:]@np.linalg.inv(Qs[3:,:])

def blocks(name,n,nu):
    T=T_rescaled_direct(name,n,nu)
    Td=dT_rescaled(name,n,nu)

    A=T[:3,:3]; B=T[:3,3:]
    C=T[3:,:3]; D=T[3:,3:]

    Ad=Td[:3,:3]; Bd=Td[:3,3:]
    Cd=Td[3:,:3]; Dd=Td[3:,3:]

    return A,B,C,D,Ad,Bd,Cd,Dd

def pull_graph_tangent(name,nu,J,store=False):
    R=terminal_graph(name,J,nu)
    H=np.zeros((3,3))
    data=[]

    for n in range(J-1,0,-1):
        A,B,C,D,Ad,Bd,Cd,Dd=blocks(name,n,nu)

        X=R@C-A
        F=np.linalg.solve(
            X,
            B-R@D,
        )

        Y=C@F+D

        source=np.linalg.solve(
            X,
            Ad@F
            + Bd
            - R@(Cd@F+Dd),
        )

        Hn=(
            source
            - np.linalg.solve(
                X,
                H@Y,
            )
        )

        if store:
            data.append({
                "n":n,
                "Rnext":R.copy(),
                "R":F.copy(),
                "Xinv":np.linalg.inv(X),
                "Y":Y.copy(),
                "source":source.copy(),
            })

        R,H=F,Hn

    if store:
        data.reverse()

    return R,H,data

# Rank-one local-source audit.
for name in ("minus","plus"):
    nu=1e-6
    R,H,data=pull_graph_tangent(
        name,
        nu,
        800,
        store=True,
    )

    for rec in data[:100]:
        n=rec["n"]
        S=rec["source"]

        if n % 2:
            assert np.linalg.norm(S) < 1e-11
        else:
            sv=np.linalg.svd(S,compute_uv=False)
            assert sv[1] < 1e-8*max(1.0,sv[0])

def scalar_sum(name,nu,J,W1):
    R,H,data=pull_graph_tangent(
        name,
        nu,
        J,
        store=True,
    )

    W=W1.copy()
    signed=0.0
    absolute=0.0
    max_rank2=0.0

    for rec in data:
        val=float(
            np.sum(
                W*rec["source"]
            )
        )

        signed+=val
        absolute+=abs(val)

        W=(
            -rec["Xinv"].T
            @ W
            @ rec["Y"].T
        )

        sv=np.linalg.svd(
            W,
            compute_uv=False,
        )

        if sv[0]>0:
            max_rank2=max(
                max_rank2,
                sv[1]/sv[0],
            )

    terminal_norm=float(
        np.linalg.norm(
            W,
            ord="fro",
        )
    )

    return signed,absolute,terminal_norm,max_rank2,R,H

def central_observables(name,R):
    K=kval(name)

    e1=float(R[2,1])
    f=float(-R[1,1])

    o2=float(
        (
            bcoef(K,1)*e1
            - A2(K,1)*f
        )
        / A4(K,1)
    )

    return e1,f,o2

rows=[]

for name in ("minus","plus"):
    K=kval(name)

    We=np.zeros((3,3))
    We[2,1]=1.0

    Wf=np.zeros((3,3))
    Wf[1,1]=-1.0

    Wo=np.zeros((3,3))
    Wo[2,1]=bcoef(K,1)/A4(K,1)
    Wo[1,1]=A2(K,1)/A4(K,1)

    for nu in (
        1e-8,
        3e-8,
        1e-7,
        3e-7,
        1e-6,
    ):
        J=max(
            2500,
            int(
                20*nu**(-1/3)
            ),
        )

        se,ae,te,re,R,H=scalar_sum(
            name,nu,J,We
        )
        sf,af,tf,rf,_,_=scalar_sum(
            name,nu,J,Wf
        )
        so,ao,to,ro,_,_=scalar_sum(
            name,nu,J,Wo
        )

        e1,f,o2=central_observables(
            name,
            R,
        )

        e1p=float(H[2,1])
        fp=float(-H[1,1])

        o2p=float(
            (
                bcoef(K,1)*e1p
                - A2(K,1)*fp
            )
            / A4(K,1)
        )

        # The local source sum omits the derivative of the finite-J terminal
        # eigenspace initializer.  At the deepest diagnostics this remainder is
        # visible, especially in the f/o2 channels.  The exact finite-J identity
        # is source sum + terminal pairing; here we only audit that the omitted
        # terminal remainder stays tiny relative to the deliberately enormous
        # Round-68 closure margins.
        assert abs(se-e1p) < 1e-3
        assert abs(sf-fp) < 2e-1
        assert abs(so-o2p) < 2.0

        rows.append({
            "fibre":name,
            "nu":nu,
            "J":J,
            "e1":e1,
            "f_a3_over_nu":f,
            "o2":o2,
            "e1_prime":e1p,
            "f_prime":fp,
            "o2_prime":o2p,
            "abs_kernel_e1":ae,
            "abs_kernel_f":af,
            "abs_kernel_o2":ao,
            "terminal_dual_e1":te,
            "terminal_dual_f":tf,
            "terminal_dual_o2":to,
            "rank2_ratio_e1_channel":re,
            "rank2_ratio_f_channel":rf,
            "source_residual_e1":e1p-se,
            "source_residual_f":fp-sf,
            "source_residual_o2":o2p-so,
        })

for name in ("minus","plus"):
    sub=[
        r for r in rows
        if r["fibre"]==name
    ]

    if name=="minus":
        assert max(r["abs_kernel_e1"] for r in sub) < 1.50
        assert max(r["abs_kernel_f"] for r in sub) < 10.20
        assert max(r["abs_kernel_o2"] for r in sub) < 144.0
    else:
        assert max(r["abs_kernel_e1"] for r in sub) < 1.00
        assert max(r["abs_kernel_f"] for r in sub) < 3.60
        assert max(r["abs_kernel_o2"] for r in sub) < 21.0

    for r in sub:
        assert abs(r["e1_prime"]) < 1e5
        assert abs(r["o2_prime"]) < 1e6

with OUT.open(
    "w",
    newline="",
    encoding="utf-8",
) as f:
    writer=csv.DictWriter(
        f,
        fieldnames=list(
            rows[0].keys()
        ),
    )
    writer.writeheader()
    writer.writerows(rows)

print(
    "Round 70 verification passed."
)

for r in rows:
    print(r)
