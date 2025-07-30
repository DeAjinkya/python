# recursion in python
# fibonacci series
"""
0,1,1,2,3,5,8....so on 

fib(0)=0
fib(1)=1
fib(2)= fib(0) + fib(1)
fib(n)= fib(n-2) + fib(n-1)
"""

def fib(n):
    # base case of recursion
    if (n==0 or n==1):
        return n
    return fib(n-2) + fib(n-1)

print(fib(6)) # 8 (6 is index)