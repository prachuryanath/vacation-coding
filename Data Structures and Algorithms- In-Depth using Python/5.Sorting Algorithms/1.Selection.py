# Selection sort O(n**2) --> Unstable sorting

def selectionsort(A):
    n = len(A)
    for i in range(n-1):
        position = i
        for j in range(i+1,n):
            if A[j] < A[position]:
                position=j
        temp = A[i]
        A[i] = A[position]
        A[position] = temp
A = [3,5,2,6,9,8]
print('Original array:', A)
selectionsort(A)
print('Sorted array:',A)