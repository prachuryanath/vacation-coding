# Iterative approach
def calculate_itr(n):
    while n>0:
        k=n**2
        print(k)
        n=n-1

calculate_itr(4)

# Recursive approach
def calculate_rec1(n):           # Tail recursion O(n)
    if n>0:
        k=n**2
        print(k)
        calculate_rec1(n-1)

def calculate_rec2(n):           # Head recursion O(n)
    if n>0:
        calculate_rec2(n-1)
        k=n**2
        print(k)

def calculate_rec3(n):           # Tree recursion O(2^n)
    if n>0:
        calculate_rec3(n-1)
        k=n**2
        print(k)
        calculate_rec3(n-1)

calculate_rec1(3)
print('\n')
calculate_rec2(3)
print('\n')
calculate_rec3(3)

# Indirect recursion
def calcA(n):                     
    if n>0:
        calcB(n-1)

def calcB(n):
    if n>0:
        calcA(n-1)

# Sum of n natural numbers
def sum_rec(n):
    if n==0:
        return 0
    return sum_rec(n-1)+n

print('Sum of 5 natural numbers:',sum_rec(5))

# Factorial of a number
def fact_rec(n):
    if n==0:
        return 1
    return fact_rec(n-1)*n

print('Factorial of 5:',fact_rec(5))
