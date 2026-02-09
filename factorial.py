import sys
maxRecursion = 10000
sys.setrecursionlimit(maxRecursion)
def factorial(n):
    if n ==0:
        return 1
    return n * factorial(n-1)
print(factorial(5))
print(factorial(1000))
