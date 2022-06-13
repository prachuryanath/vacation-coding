# Shell Sort O(n^2)
def quicksort(A,low,high):
    if low < high:
        pi = partition(A,low,high)
        quicksort(A,low,pi-1)
        quicksort(A,pi+1,high)

def partition(A,low,high):
    pivot = A[low]
    i = low+1
    j=high
    while True:
        while i<=j and A[i] <= pivot:
            i=i+1
        while i <=j and A[j]>pivot:
            j = j-1
        if i<=j:
            A[i], A[j] = A[j], A[i]
        else:
            break
    A[low], A[j] = A[j], A[low]
    return j  

A = [3,5,2,6,9,8]
print('Original array:', A)
quicksort(A, 0, len(A)-1)
print('Sorted array:',A)
