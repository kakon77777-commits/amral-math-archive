"""
Verification for NS_X72 Round 68.

Round 68 replaces the tiny-central-coefficient bridge by a coarse central sign cone.

Exact results checked here:
1. the n=1 central recurrence reduction;
2. exact coefficient sign geometry on K=sqrt(17) +/- 3;
3. the small-fibre threshold b_1/(-A4_1) > 1200;
4. rigorous endpoint interval enclosures for
       e1 := u2
       o2 := u5/nu
   using the Round59-style endpoint Jost pullback;
5. the endpoint values lie deeply inside sufficient central sign cones;
6. the derivative bounds
       |e1'| < 1e5, |o2'| < 1e6
   would be sufficient to carry those cones through 0<nu<=1e-6.

The script also supplies fixed-size Riccati tangent diagnostics for e1' and o2'
on several microscopic viscosities. Those derivative values are diagnostics,
not yet a uniform interval theorem.
"""
from pathlib import Path
import csv, math
import numpy as np
import mpmath as mp
import sympy as sp

OUT=Path("/mnt/data/NS_X72_Round68_CentralConeTangentMap_2026-08-18.csv")

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



# ------------------------------------------------------------------
# Exact central recurrence / coefficient geometry.
# ------------------------------------------------------------------

K=sp.symbols("K", positive=True, real=True)
nu=sp.symbols("nu", positive=True, real=True)
e1,o2,u3=sp.symbols("e1 o2 u3", real=True)

# Use exact algebraic K values directly in sympy via the pure formulas.
Km=sp.sqrt(17)-3
Kp=sp.sqrt(17)+3

def sx(f,Kv,n):
    return sp.simplify(f(Kv,n))

geom={}
for name,Kv in (("minus",Km),("plus",Kp)):
    a2=sx(A2,Kv,1)
    a4=sx(A4,Kv,1)
    bb=sx(bcoef,Kv,1)
    geom[name]=(a2,a4,bb)

# Small fibre signs and huge ratio.
a2m,a4m,bm=geom["minus"]
assert sp.sign(a2m)==-1
assert sp.sign(a4m)==-1
assert sp.sign(bm)==1

theta_m=sp.simplify(bm/(-a4m))
assert sp.sign(theta_m-1200)==1

# Large fibre direct-sign geometry.
a2p,a4p,bp=geom["plus"]
assert sp.sign(a2p)==1
assert sp.sign(a4p)==-1
assert sp.sign(bp)==-1

# n=1 recurrence:
# -nu*b1*u2 - A2*u3 + A4*u5 = 0, u5=nu*o2.
# Therefore u3 = nu*(A4*o2-b1*e1)/A2.
central_expr_m=sp.simplify(nu*(a4m*o2-bm*e1)/a2m)
central_expr_p=sp.simplify(nu*(a4p*o2-bp*e1)/a2p)

# Small sufficient cone:
# e1<=-0.1, 0<=o2<=100 => o2/(-e1)<=1000<theta_m.
# Verify the worst numerator sign exactly.
small_worst_num=sp.simplify(a4m*100-bm*(-sp.Rational(1,10)))
assert sp.sign(small_worst_num)==1  # numerator positive, denominator negative -> u3<0.

# Large cone e1<0,o2>0 gives both numerator terms negative and A2>0.
# Sign geometry above is the exact proof.

# ------------------------------------------------------------------
# Rigorous endpoint intervals (Round59 Jost graph in a compact implementation).
# ------------------------------------------------------------------

mp.iv.dps=55

def Kiv(name):
    return mp.iv.sqrt(17)-3 if name=="minus" else mp.iv.sqrt(17)+3

AF={-2:A_m2,0:A0,2:A2,4:A4}

def even_endpoint(Kv):
    R={11:mp.iv.mpf([-0.1,0]),12:mp.iv.mpf([-0.1,0])}
    for j in range(10,0,-1):
        n=2*j
        R[j]=AF[-2](Kv,n)/(AF[0](Kv,n)-AF[2](Kv,n)*R[j+1]+AF[4](Kv,n)*R[j+2]*R[j+1])
    e={0:mp.iv.mpf([1,1])}
    for j in range(1,12):
        e[j]=e[j-1]*R[j]
    return R,e

def endpoint_graph(name):
    Kv=Kiv(name)
    R,e=even_endpoint(Kv)
    if name=="minus":
        P=mp.iv.mpf([0.7,1.3]); Q=mp.iv.mpf([0,0.01]); G=mp.iv.mpf([-1,1])
    else:
        P=mp.iv.mpf([0.8,1.25]); Q=mp.iv.mpf([0,0.06]); G=mp.iv.mpf([-1,1])

    for j in range(10,0,-1):
        n=2*j+1
        den=AF[2](Kv,n)-AF[4](Kv,n)*P
        forcing=bcoef(Kv,n)*e[j+1]
        P,Q,G=(AF[0](Kv,n)+AF[4](Kv,n)*Q)/den, -AF[-2](Kv,n)/den, (AF[4](Kv,n)*G-forcing)/den

    n=1
    f0=bcoef(Kv,n)*e[1]
    c0=(f0-AF[4](Kv,n)*G)/(AF[2](Kv,n)-AF[4](Kv,n)*P)
    e1_iv=e[1]
    o1_iv=-c0
    o2_iv=P*o1_iv+G
    return e1_iv,c0,o2_iv,(P,Q,G)

endpoint={}
for name in ("minus","plus"):
    endpoint[name]=endpoint_graph(name)

e1m,c0m,o2m,_=endpoint["minus"]
e1p,c0p,o2p,_=endpoint["plus"]

# Deep inside the sufficient cones.
assert float(e1m.b) < -0.9
assert float(o2m.a) > 4.0
assert float(o2m.b) < 5.0

assert float(e1p.b) < -0.7
assert float(o2p.a) > 3.0

# The proposed extremely loose derivative bridge is sufficient:
# over length 1e-6:
# |Delta e1| <= 0.1, |Delta o2| <= 1.
Me=1e5
Mo=1e6
strip=1e-6

assert float(e1m.b)+Me*strip < -0.1
assert float(o2m.a)-Mo*strip > 0
assert float(o2m.b)+Mo*strip < 100

assert float(e1p.b)+Me*strip < 0
assert float(o2p.a)-Mo*strip > 0

# ------------------------------------------------------------------
# Fixed-size Riccati tangent diagnostics for e1' and o2'.
# ------------------------------------------------------------------

C=np.array([[0.,0.,1.],[0.,0.,0.],[0.,0.,0.]])
D=np.array([[0.,0.,0.],[1.,0.,0.],[0.,1.,0.]])

def kval(name):
    return math.sqrt(17)-3 if name=="minus" else math.sqrt(17)+3

def blocks(name,n,nuv):
    kv=kval(name)
    am=A_m2(kv,n); a0=A0(kv,n); a2=A2(kv,n); a4=A4(kv,n); bb=bcoef(kv,n)
    A=np.array([[0.,a2/a4,nuv*bb/a4],[1.,0.,0.],[0.,1.,0.]])
    B=np.array([[-a0/a4,0.,am/a4],[0.,0.,0.],[0.,0.,0.]])
    At=np.zeros((3,3)); At[0,2]=nuv*bb/a4
    return A,B,At

def flow(name,nuv,J):
    G=np.zeros((3,3))
    H=np.zeros((3,3))
    for n in range(J,0,-1):
        A,B,At=blocks(name,n,nuv)
        X=G@C-A
        F=np.linalg.solve(X,B-G@D)
        R=D+C@F
        Hn=np.linalg.solve(X,At@F-H@R)
        G,H=F,Hn
    return G,H

rows=[]
for name in ("minus","plus"):
    kv=kval(name)
    A2c=A2(kv,1); A4c=A4(kv,1); bc=bcoef(kv,1)
    for nuv in (1e-8,3e-8,1e-7,3e-7,1e-6):
        J=max(1500,int(15*nuv**(-1/3)))
        G,H=flow(name,nuv,J)

        e1v=float(G[2,1])
        e1prime=float(H[2,1]/nuv)

        a3=-float(G[1,1])
        at=-float(H[1,1])
        f=a3/nuv
        sigma=(at-a3)/(nuv*nuv)

        o2v=float((bc*e1v-A2c*f)/A4c)
        o2prime=float((bc*e1prime-A2c*sigma)/A4c)

        rows.append({
            "fibre":name,
            "nu":nuv,
            "J":J,
            "e1":e1v,
            "e1_prime":e1prime,
            "o2":o2v,
            "o2_prime":o2prime,
            "sigma":sigma,
        })

for r in rows:
    assert r["e1"] < 0
    assert r["o2"] > 0
    assert abs(r["e1_prime"]) < 2
    assert abs(r["o2_prime"]) < 200

with OUT.open("w",newline="",encoding="utf-8") as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0].keys()))
    w.writeheader(); w.writerows(rows)

print("Round 68 verification passed.")
print("theta_minus interval =", endpoint["minus"][0], endpoint["minus"][2])
print("small coefficient ratio b1/(-A4_1) =", mp.iv.mpf([float(sp.N(theta_m,18)),float(sp.N(theta_m,18))]))
print("endpoint minus e1,o2 =", e1m,o2m)
print("endpoint plus  e1,o2 =", e1p,o2p)
for r in rows:
    print(r)
