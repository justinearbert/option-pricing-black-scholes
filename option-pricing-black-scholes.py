import math
from math import log, sqrt, exp,erf
# ca ca marche pas : from spicy.stats import norm donc je vais mettre une autre ligne a la place mais a modifier apres 
def N(x):
    #cdf de la loi normale standards via erf 
    return 0.5 * (1 + erf (x/sqrt(2)))


def black_scholes_calls(S,K,r,sigma,T):
    d1 = (log(S/K)+(r+0.5*sigma**2)*T)/(sigma*sqrt(T))
    d2 = d1 - sigma * sqrt(T)
    call_price = S* N(d1)- K * exp(-r*T)* N(d2)
    return call_price 

# exemple de données

S=100 #spot 
K=100 #strike 
r = 0.02 #2% taux sans risque 
sigma = 0.20 #20% de vol 
T = 1.0 #1an

print("Prix du call (Black Scholes):", black_scholes_calls(S,K,r,sigma,T))

