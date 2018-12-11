class ArrayStack:
    '''LIFO Stack  implementation using a Python list as underlying storage'''

    def __init__(self):
        '''Create an empty stack'''
        self._data = []

    def __len__(self):
        '''Return the number of elements in the stack'''
        return len(self._data)

    def is_empty(self):
        '''Return True if the stack is empty'''
        return len(self._data) == 0

    def push(self, e):
        '''Add element e to the top of the stack'''
        self._data.append(e)                    # new item stored at end of list

    
