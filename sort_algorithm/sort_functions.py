def selectionSort(alist):
    for i in range(0, len(alist), 1):
        min = alist[i]
        index = i
        for j in range(i, len(alist), 1):
            if alist[j] < min:
                min = alist[j]
                index = j
        tmp = alist[j]
        alist[i] = min
        alist[index] = tmp