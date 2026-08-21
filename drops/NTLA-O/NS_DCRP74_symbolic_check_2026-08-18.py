import sympy as sp

alpha, gamma = sp.symbols('alpha gamma', positive=True, real=True)
kappa = 3 - 2*alpha
rel = {gamma: 1/(alpha+1)}

print('gamma*kappa = 5gamma-2 check:')
print(sp.simplify((gamma*kappa-(5*gamma-2)).subs(rel)))

cg = 2-3*gamma
print('gamma*kappa + c_gamma = 2gamma check:')
print(sp.simplify((gamma*kappa+cg-2*gamma).subs(rel)))

pfet_exp = 3-2*alpha
enst_exp = 1-2*alpha
print('PFET exponent:', pfet_exp)
print('enstrophy turnover exponent:', enst_exp)
print('ell^2 enstrophy exponent:', sp.expand(enst_exp+2))
print('homogeneity difference:', sp.simplify((enst_exp+2)-pfet_exp))

visc_exp = 2-alpha
print('viscous cycle / PFET exponent:', sp.simplify(visc_exp-pfet_exp))
print('expected alpha-1')

K, Z, Pi = sp.symbols('K Z Pi', positive=True, real=True)
Qprime = (gamma*kappa*K-Pi)/Z - K*(-cg*Z)/Z**2
print('Qprime reduced:')
print(sp.simplify(Qprime.subs(rel)))
print('=> 2 gamma K/Z - Pi/Z')
