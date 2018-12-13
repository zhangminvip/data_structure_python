from time import time                # import time function from time module
def compute_average(n):
    '''Perform n appends to an empty list and return averave time elapsed'''
    data = []
    start = time()                   # record the start time(in seconds)
    for k in range(n):
        data.append(None)
    end = time()                     # record the end time (in seconds)
    return (end - start) / n         # compute average per operation 


n100 = compute_average(100)
n1000 = compute_average(1000)
n10000 = compute_average(10000)
n100000 = compute_average(100000)
n1000000 = compute_average(1000000)
print(n100,n1000, n10000, n100000, n1000000)