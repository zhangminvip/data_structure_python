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


def quicksort(nums):
    if len(nums) <= 1:
        return nums

    # left subtree
    less = []

    # right subtree
    greater = []

    # base number
    base = nums.pop()

    for x in nums:
        if x < base:
            less.append(x)
        else:
            greater.append(x)

    return quicksort(less) + [base] + quicksort(greater)


nums = [6, 1, 2, 7, 9, 3, 4, 5, 10, 8, 8]

print(quicksort(nums))
