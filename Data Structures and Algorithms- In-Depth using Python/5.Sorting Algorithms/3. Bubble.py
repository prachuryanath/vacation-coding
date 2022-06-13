# Bubble Sort O(n**2) --> Stable sorting
def bubblesort(A):
    n = len(A)
    for passes in range(n-1,0,-1):
        for i in range(passes):
            if A[i] > A[i+1]:
                temp = A[i]
                A[i] = A[i+1]
                A[i+1] = temp

A = [3,5,2,6,9,8]
print('Original array:', A)
bubblesort(A)
print('Sorted array:',A)