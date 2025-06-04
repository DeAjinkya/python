# factorial of 5 (denoted as 5!) is 5 × 4 × 3 × 2 × 1 = 120

n = 5

fact = 1

for i in range(1,n + 1):
    fact *= i

print(fact)

#This code calculates the factorial of a number n (which is 5 in this case) using a for loop. 
#It initializes the variable fact to 1. Then, 
#it multiplies fact by each integer from 1 to n (inclusive) in the loop, updating the value of fact with each iteration. 
#Finally, it prints the result, which is the factorial of 5 (120).