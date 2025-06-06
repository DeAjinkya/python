#A = P(1 + R/100) t 

#Compound Interest = A - P 

#Where, 

#A is amount 
#P is the principal amount 
#R is the rate and 
#T is the time span

def compound_interest(p , r, t):
    #calculate
    A = p * (pow((1+r/100),t))
    ci = A - p
    print("compound interest: ",ci)

compound_interest(10000,10.25,5)