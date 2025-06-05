#Simple interest formula :

#Simple Interest = (P x T x R)/100

#Where:

#P is the Principal amount
#T is the Time period (in years)
#R is the Rate of interest per annum


def fun(p,t,r):
    return (p*t*r)/100

p,t,r = 8,6,8

res = fun(p,t,r)
print(res)

#In this example we defines a function called fun that calculates 
# simple interest based on three input values: principal (p), 
# time (t) in years, and rate of interest (r) per annum. 
# The function returns the result of the simple interest formula.