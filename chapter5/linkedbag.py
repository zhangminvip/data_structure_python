from chapter4.node import Node

class LinkedBag(object):
    ''' A link-based bag implementation'''
    '''Head insertion method'''


    def __init__(self, sourceCollection=None):
        self._items = None  # This is a Pointer
        self._size = 0
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)


    def isEmpty(self):
        return len(self) == 0

    def __len__(self):
        return self._size


    def __add__(self, other):
        print(self._items)
        result = LinkedBag(self)
        for item in other:
            result.add(item)
        return result


    def __eq__(self, other):
        if self is other:
            return True
        if type(self) != type(other) or len(self) != len(other):
            return False
        for item in self:
            if not item in other:
                return False
        return True

    def __str__(self):
        return '{' + ','.join(map(str, self)) + '}'

    def __iter__(self):
        cursor = self._items
        while not cursor is None:
            yield cursor.data
            cursor = cursor.next

    def add(self, item):
        self._items = Node(item,self._items)
        self._size += 1


    def remove(self, item):
        if not item in self:
            raise KeyError(str(item)+'not in bag')
        probe = self._items
        trailer = None
        for targetItem in self:
            if targetItem == item:
                break
            trailer = probe    # Save the location of this iter
            probe = probe.next # Jump to the location you are about to iter to
        if probe == self._items:
            self._items = probe.next
        else:
            trailer.next = probe.next
        self._size -= 1




