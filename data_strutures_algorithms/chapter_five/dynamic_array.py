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
            self._resize(2 * self._capacity)
        self._A[self._n] = object
        self._n += 1
