from chapter5.arraybag import ArrayBag


class ArraySortBag(ArrayBag):
    '''an array-based sorted bag implementation'''

    def __init__(self, sourceCollection=None):
        ArrayBag.__init__(self, sourceCollection)

    def __contains__(self, item):
        '''Return True if item is in self, or False otherwise'''
        left = 0
        right = len(self) - 1
        while left <= right:
            midPoint = (left + right) // 2
            if self._items[midPoint] == item:
                return True
            elif self._items[midPoint] > item:
                right = midPoint-1
            else:
                left = midPoint +1

        return False

    def add(self, item):
        '''add item to self'''
        '''empty or last item , call ArrayBag.add'''

        if self.isEmpty() or item >=self._items[len(self) -1]:
            ArrayBag.add(self,item)
        else:
            '''
            Resize the array if it is full here
            Search for first item >= new item
            '''
            targetIndex = 0
            while item > self._items[targetIndex]:
                targetIndex += 1
            for i in range(len(self),targetIndex, -1):
                self._items[i] = self.items[i-1]
            self.items[targetIndex] = item
            self._size += 1