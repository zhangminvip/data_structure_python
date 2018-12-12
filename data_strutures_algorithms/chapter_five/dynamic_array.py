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

    def 