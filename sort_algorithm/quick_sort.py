import random


def Exchange(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp
    return 0


def Partition(A, p, r):
    random_num = random.choice(range(p, r+1))
    Exchange(A, r, random_num)
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            Exchange(A, i, j)
    Exchange(A, i+1, r)
    return i+1


def Quick_sort(A, p, r):
    if p < r:
        q = Partition(A, p, r)
        Quick_sort(A, p, q-1)
        Quick_sort(A, q+1, r)


A = [2, 8, 7, 1, 3, 5, 6, 4]
print('Before sort:', A)
Quick_sort(A, 0, len(A)-1)
print('After sort:', A)
