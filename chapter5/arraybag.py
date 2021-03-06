import sys

sys.path.append('..')
from chapter4.arrays import Array


class ArrayBag(object):
    DEFAULT_CAPACITY = 10

    def __init__(self, sourceCollection=None):
        self._items = Array(ArrayBag.DEFAULT_CAPACITY)
        self._size = 0
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)

    def isEmpty(self):
        return len(self) == 0

    def __len__(self):
        return self._size

    def clear(self):
        self._size = 0
        self._items = Array(ArrayBag.DEFAULT_CAPACITY)

    def add(self, item):
        self._items[len(self)] = item
        self._size += 1

    def __iter__(self):
        cursor = 0
        while cursor < len(self):
            yield self._items[cursor]
            cursor += 1

    def __str__(self):
        return '{' + ','.join(map(str, self)) + '}'

    def __add__(self, other):
        print(self._items)
        result = ArrayBag(self)
        for item in other:
            result.add(item)
        return result

    # def __add__(self, other):
    #     print(self._items)
    #     for item in other:
    #         self.add(item)
    #     return self

    def __eq__(self, other):
        if self is other:
            return True
        if type(self) != type(other) or len(self) != len(other):
            return False
        for item in self:
            if not item in other:
                return False
        return True

    def remove(self, item):
        '''
        Precondition: item is in self,
        Raises:keyError if item is not in self,
        postcondition: item is removed from self
        '''
        #check precondition and raise if necessary
        if not item in self:
            raise KeyError(str(item)+'not in bag')
        #search for index of target item
        targetIndex = 0
        for targetItem in self:
            if targetItem == item:
                break
            targetIndex += 1
        # shift items to the left of target up by one position
        for i in range(targetIndex, len(self) -1):
            self._items[i] = self._items[i+1]
        # decrement logical size
        self._size -= 1


