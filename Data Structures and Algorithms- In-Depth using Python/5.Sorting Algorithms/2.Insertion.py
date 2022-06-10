# Insertion Sort O(n**2) --> Stable sorting
from turtle import position


def insertionsort(A):
    n = len(A)
    for i in range(1,n):
        cvalue = A[i]
        position = i
        while position > 0 and A[position-1] > cvalue:
            A[position] = A[position-1]
            position = position-1
        A[position] = cvalue

A = [3,5,2,6,9,8]
print('Original array:', A)
insertionsort(A)
print('Sorted array:',A)