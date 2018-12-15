import ctypes


class DynamicArray:
    '''A dynamic array class akin to a simplified Python list'''

    def __init__(self):
        '''Create an empty array'''
        self._n = 0                                      # count actual elements
        self._capacity = 1                               # default array capacity
        self._A = self._make_array(self._capacity)       # low-level array

    def __len__(self):
        '''Return number of elements in the arrays'''
        return self._n

    def __getitem__(self, k):
        '''Return element at index k'''
        if not 0 <= k < self._n:
            raise IndexError('invalid index')
        return self._A[k]                                # retrieve from array

    def append(self, obj):
        '''Add object to end of the array'''
        if self._n == self._capacity:
            self._resize(2 * self._capacity)             # not enough room so double capacity
        self._A[self._n] = obj
        self._n += 1

    def _resize(self, c):                                # nonpublic utitity
        '''Resize internal array to capacity c'''

        B = self._make_array(c)                          # new(bigger) array
        for k in range(self._n):                         # for each existing value
            B[k] = self._A[k]
        self._A = B                                      # use the bigger array
        self._capacity = c

    def _make_array(self, c):                            # nonpublic utitity
        '''Return new array with capacity c'''

        return (c * ctypes.py_object)()                  # see ctypes documentation

    def insert(self, k, value):
        '''Insert value at index k, shifting subsequent values rightward'''
        # (for simplicity, we assume 0 <= k <= n in this version)
        if self._n == self._capacity:                    # not enough room
            self._resize(2 * self._capacity)             # so double capacity
        for j in range(self._n, k, -1):
            self._A[j] = self._A[j -1]
        self._A[k] = value
        self._n += 1

    def remove(self, value):
        '''Remove first occurrence of value(or raise ValueError).'''
        # note: we do not consider shrinking the dynamic array in this version
        for k in range(self._n):
            if self.A[k] == value:                       # found a match !
                for j in range(k, self.n - 1):           # shift others to fill gap
                    self.A[j] = self.A[j+1]
                self.A[self._n - 1] = None               # help garbage collection
                self._n -= 1                             # we have one less item
                return                                   # exit immediately
        raise ValueError('Value not found')              # only reached if no match

    def insertion_sort(A):
        '''Sort list of comparable elements into nondecreasing order'''
        for k in range(1, len(A)):
            cur = A[k]                                   # current element to be inserted
            j = k                                        # find correct index j for current
            while j > 0 and A[j-1] > cur:                # element A[j-1] must be after current
                A[j] = A[j-1]
                j -= 1
            A[j] = cur                                   # cur now in the right place

