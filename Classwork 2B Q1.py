def Factorial_Recursive( n):
    if (n==0):
        return 1
    else:
        return n * Factorial_Recursive(n-1)

def Factorial_iterative(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * 1
    return fact
n = - 1
while n < 0:
    n = int(input(" enter a postivie integer: "))

f1 = Factorial_iterative( n)
print(" the Iterative Functions returned is:", f1)

f2 =  Factorial_Recursive( n)
print("\nthe Recursive Functions returned is:",f2)