class Array(object):
    ''' Represents an array'''

    def __init__(self, capacity, fillValue=None):
        '''Capacity is the static size of the array.
        fillValue is placed at each position'''
        self._items = list()
        for count in range(capacity):
            self._items.append(fillValue)


    def __len__(self):
        '''-> The capacity of the array'''
        return len(self._items)


    def __str__(self):
        return str(self._items)

    def __iter__(self):
        return iter(self._items)

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, key, value):
        self._items[key] = value
