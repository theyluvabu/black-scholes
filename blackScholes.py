import math 
from scipy.stats import norm 

# defining varibles needed for calculations 
S = 42 #underlying strike price 
K = 40  #strike price 
T =  0.5 #time to expiration
r = 0.1 #risk-free rate 
vol = 0.2 #volatility (sigma)

#calculating d1 and d2
d1 = (math.log(S/K) + (r + 0.5 * vol**2) * T) / (vol * math.sqrt(T))
d2 = d1 - (vol * math.sqrt(T))

#calculating call option price 
cop = S * norm.cdf(d1) - K * math.exp(-r * T) * norm.cdf(d2)

#calculating put option price
pop = K * math.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)

#printing results 
print('the value of d1 is: ' + str(round(d1, 4)))
print('the value of d2 is: ' + str(round(d2, 4)))
print('the price of the call option is: ' + str(round(cop, 2)))
print('the price of the put option is: ' + str(round(pop, 2)))