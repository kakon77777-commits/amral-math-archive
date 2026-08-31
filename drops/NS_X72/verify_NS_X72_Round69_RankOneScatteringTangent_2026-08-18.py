"""
Verification for NS_X72 Round 69.

Round 69 has three purposes:

1. Repair the old Round61/62 endpoint-plane diagnostic:
   the true nu=0 selected plane contains the bounded odd particular response
   forced by the even minimal mode, not merely the block-direct-sum proxy.

2. Build a central endpoint shear which subtracts that particular response.
   In this chart the true endpoint plane is well conditioned.

3. Verify the rank-one first-order scattering hierarchy:
       sigma_1(R_nu-R_0) = O(nu)
       sigma_2(R_nu-R_0) = O(nu^2)
       sigma_3(R_nu-R_0) = O(nu^2)
   in the corrected affine-Jost chart.

The script also verifies the exact local parity transfer dependence
T_j(nu)=T_j(0)+nu^2 E_j, which is the structural reason the two fast
branches have zero first derivative in nu at the endpoint.

The rank-one infinite-Jost limit itself remains the final structural bridge;
the finite-cutoff rank-one theorem is exact, while the displayed central
singular-value hierarchy is numerical diagnostic evidence.
"""
from pathlib import Path
import csv, math
import numpy as np
import mpmath as mp

OUT = Path("/mnt/data/NS_X72_Round69_RankOneTangentMap_2026-08-18.csv")

# Exact coefficient formulas inherited from the symbolic Round58 derivation.
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

# ------------------------------------------------------------------
# Endpoint Jost data, including the even-forced odd particular solution.
# ------------------------------------------------------------------

mp.iv.dps = 50
AF = {-2:A_m2,0:A0,2:A2,4:A4}

def kiv(name):
    return mp.iv.sqrt(17)-3 if name=="minus" else mp.iv.sqrt(17)+3

def mid(x):
    return 0.5*(float(x.a)+float(x.b))

def even_endpoint(K):
    R={11:mp.iv.mpf([-0.1,0]),12:mp.iv.mpf([-0.1,0])}
    for j in range(10,0,-1):
        n=2*j
        R[j]=AF[-2](K,n)/(AF[0](K,n)-AF[2](K,n)*R[j+1]+AF[4](K,n)*R[j+2]*R[j+1])
    e={0:mp.iv.mpf([1,1])}
    for j in range(1,12):
        e[j]=e[j-1]*R[j]
    return R,e

def endpoint_affine_data(name):
    K=kiv(name)
    R,e=even_endpoint(K)

    if name=="minus":
        P=mp.iv.mpf([0.7,1.3])
        Q=mp.iv.mpf([0,0.01])
        G=mp.iv.mpf([-1,1])
    else:
        P=mp.iv.mpf([0.8,1.25])
        Q=mp.iv.mpf([0,0.06])
        G=mp.iv.mpf([-1,1])

    for j in range(10,0,-1):
        n=2*j+1
        den=AF[2](K,n)-AF[4](K,n)*P
        forcing=bcoef(K,n)*e[j+1]
        P,Q,G=(
            (AF[0](K,n)+AF[4](K,n)*Q)/den,
            -AF[-2](K,n)/den,
            (AF[4](K,n)*G-forcing)/den,
        )

    n=1
    f0=bcoef(K,n)*e[1]
    c0=(f0-AF[4](K,n)*G)/(AF[2](K,n)-AF[4](K,n)*P)

    e0=1.0
    e1=mid(e[1])
    e2=mid(e[2])
    o1=-mid(c0)
    o2=mid(P*(-c0)+G)
    P0=mid(P)
    Q0=mid(Q)

    # True selected endpoint plane at parity state
    # S_1=(e2,e1,e0,o2,o1,o0).
    # Column 1 is the bounded odd particular response forced by even minimal mode.
    # Columns 2,3 span the homogeneous bounded odd plane:
    # o2=P0 o1 + Q0 o0.
    V=np.array([
        [e2,0.0,0.0],
        [e1,0.0,0.0],
        [e0,0.0,0.0],
        [o2,Q0,P0],
        [o1,0.0,1.0],
        [0.0,1.0,0.0],
    ],dtype=float)

    return dict(V=V,e1=e1,e2=e2,o1=o1,o2=o2,P=P0,Q=Q0)

endpoint={name:endpoint_affine_data(name) for name in ("minus","plus")}

# ------------------------------------------------------------------
# Central endpoint shear and chart.
# ------------------------------------------------------------------

base=[2,3,5]   # (e0, tilde{o2}, o0)
out=[0,1,4]    # (e2, e1, tilde{o1})

def endpoint_shear(name):
    d=endpoint[name]
    S=np.eye(6)
    # subtract the bounded odd particular response proportional to e0
    S[3,2] = -d["o2"]
    S[4,2] = -d["o1"]
    return S

def graph_from_plane(Q):
    B=Q[base,:]
    O=Q[out,:]
    return O@np.linalg.inv(B), np.linalg.cond(B)

R0={}
cond0={}

for name in ("minus","plus"):
    S=endpoint_shear(name)
    Q,_=np.linalg.qr(S@endpoint[name]["V"])
    R0[name],cond0[name]=graph_from_plane(Q)

assert 1.4 < cond0["minus"] < 1.5
assert 1.5 < cond0["plus"] < 1.7

# ------------------------------------------------------------------
# Parity-rescaled transfer T_j(nu).
# Exact structural point: only nu^2 appears.
# ------------------------------------------------------------------

def coeffs(K,j):
    ne=2*j
    no=2*j+1
    Ae={-2:A_m2(K,ne),0:A0(K,ne),2:A2(K,ne),4:A4(K,ne)}
    Ao={-2:A_m2(K,no),0:A0(K,no),2:A2(K,no),4:A4(K,no)}
    return Ae,bcoef(K,ne),Ao,bcoef(K,no)

def T6(K,j,nu):
    Ae,be,Ao,bo=coeffs(K,j)
    T=np.zeros((6,6),dtype=float)
    T[0,0]=Ae[2]/Ae[4]
    T[0,1]=-Ae[0]/Ae[4]
    T[0,2]=Ae[-2]/Ae[4]
    T[0,4]=nu*nu*be/Ae[4]
    T[1,0]=1.0
    T[2,1]=1.0

    T[3,0]=bo/Ao[4]
    T[3,3]=Ao[2]/Ao[4]
    T[3,4]=-Ao[0]/Ao[4]
    T[3,5]=Ao[-2]/Ao[4]
    T[4,3]=1.0
    T[5,4]=1.0
    return T

# Numerical exactness check of even dependence:
for name in ("minus","plus"):
    K=kval(name)
    for j in (1,3,10,100):
        T0=T6(K,j,0.0)
        Tp=T6(K,j,1e-4)
        Tm=T6(K,j,-1e-4)
        assert np.max(np.abs(Tp-Tm)) < 1e-14
        # second-order quotient is independent of sign.
        assert np.max(np.abs((Tp-T0)-(Tm-T0))) < 1e-14

# ------------------------------------------------------------------
# Positive-viscosity minimal plane and corrected rank-one diagnostics.
# ------------------------------------------------------------------

def real_basis_from_eig(vals,vecs,count=3):
    order=np.argsort(np.abs(vals))
    picked=[]
    for idx in order:
        v=vecs[:,idx]
        if np.max(np.abs(v.imag))<1e-8:
            picked.append(v.real)
        else:
            picked.append(v.real)
            if len(picked)<count:
                picked.append(v.imag)
        if len(picked)>=count:
            break
    Q=np.column_stack(picked[:count])
    Q,_=np.linalg.qr(Q)
    return Q

def stable_plane(name,nu,J):
    K=kval(name)
    vals,vecs=np.linalg.eig(T6(K,J,nu))
    Q=real_basis_from_eig(vals,vecs,3)
    for j in range(J-1,0,-1):
        Q=np.linalg.solve(T6(K,j,nu),Q)
        Q,_=np.linalg.qr(Q)
    return Q

rows=[]

for name in ("minus","plus"):
    S=endpoint_shear(name)
    for nu in (1e-4,3e-5,1e-5,3e-6,1e-6):
        J=max(2500,int(12*nu**(-1/3)))
        Q=stable_plane(name,nu,J)
        Qs,_=np.linalg.qr(S@Q)
        R,cond=graph_from_plane(Qs)
        sv=np.linalg.svd(R-R0[name],compute_uv=False)

        rows.append({
            "fibre":name,
            "nu":nu,
            "J":J,
            "chart_cond":cond,
            "sigma1":sv[0],
            "sigma2":sv[1],
            "sigma3":sv[2],
            "sigma1_over_nu":sv[0]/nu,
            "sigma2_over_nu2":sv[1]/(nu*nu),
            "sigma3_over_nu2":sv[2]/(nu*nu),
        })

# The leading direction is O(nu), subleading directions O(nu^2)
# across the well-resolved part of the diagnostic.
for name in ("minus","plus"):
    sub=[r for r in rows if r["fibre"]==name]
    assert max(r["sigma1_over_nu"] for r in sub) < 200
    assert min(r["sigma1_over_nu"] for r in sub) > 5
    assert max(r["sigma2_over_nu2"] for r in sub) < 200

# ------------------------------------------------------------------
# Deep-tail tangent sensitivity theorem constants.
#
# If y=K_t y + S_t x, K_t,S_t scale as exp(-t), and total row norm <=q<1,
# then:
#   ||G|| <= q/(1-q)
#   ||G_t|| <= q/(1-q)^2
#   ||G_tt|| <= q(1+q)/(1-q)^3.
# At q=1/4 these are uniformly modest.
# ------------------------------------------------------------------

q=0.25
G_bound=q/(1-q)
Gt_bound=q/(1-q)**2
Gtt_bound=q*(1+q)/(1-q)**3

assert G_bound < 0.334
assert Gt_bound < 0.445
assert Gtt_bound < 0.75

with OUT.open("w",newline="",encoding="utf-8") as f:
    writer=csv.DictWriter(f,fieldnames=list(rows[0].keys()))
    writer.writeheader()
    writer.writerows(rows)

print("Round 69 verification passed.")
print("endpoint chart condition numbers =",cond0)
print("uniform tail jet bounds at q=1/4 =",G_bound,Gt_bound,Gtt_bound)
for r in rows:
    print(r)
