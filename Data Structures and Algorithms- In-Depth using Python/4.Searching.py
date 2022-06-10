# Linear Search Algorithm   O(n)
def linear_search(A,Key):
    index=0
    while index < len(A):
        if A[index] == Key:
            return index
        index = index + 1
    return -1

A=[1,2,4,7,-2]
Key=7
print('Result:',linear_search(A,Key))

# Binary Search Algorithm 
# 1. Iterative approach O(logn)
def binary_iter(A,Key):
    l=0
    r=len(A)-1
    while l <= r:
        mid = (l+r)//2
        if Key == A[mid]:
            return mid
        elif Key < A[mid]:
            r = mid -1
        elif Key > A[mid]:
            l = mid + 1
    return -1

print('Result:', binary_iter(A,77))
        
# 2. Recursive approach O(logn)
def binary_rec(A,Key,l,r):
    if l > r:
        return -1
    else:
        mid = (l+r)//2
        if Key == A[mid]:
            return mid
        elif Key < A[mid]:
            binary_rec(A,Key,l,mid-1)
        elif Key > A[mid]:
            binary_rec(A,Key,mid+1,r)
    return -1

print('Result:', binary_rec(A,4,0,4))
