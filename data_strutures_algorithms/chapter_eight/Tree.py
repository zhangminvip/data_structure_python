class Tree:
    '''Abstract base class representing a tree structure'''

    # ---------------------------nested Position class------------------------
    class Position:
        '''An abstraction representing the location of a single element'''

        def element(self):
            '''Return the element stored at this Position'''
            raise NotImplementedError('must be implemented by subclass')

        def __eq__(self, other):
            '''Return True if other Position represents the same location'''
            raise NotImplementedError('must be implemented by subclass')

        def __ne__(self, other):
            '''Return True if other does not represent the same location'''
            return not (self == other)  # opposite of __eq__

    def __iter__(self):
        '''Generate an iteration of the tree's elements'''
        for p in self.positions():   # use same order as position()
            yield p.element()        # but yield each element

    def preorder(self):
        '''Generate a preorder iteration of position in the tree'''
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()):     # start recursion
                yield p

    def _subtree_preorder(self, p):
        '''Generate a preorder iteration of positions in subtree rooted at p'''
        yield p
        for c in self.children(p):
            for other in self._subtree_preorder(c):
                yield other

    def _subtree_preorder(self, p):
        '''Generate a preorder iteration of '''

    def root(self):
        '''Return Position representing the tree's root(or None if empty)'''
        raise NotImplementedError('must be implemented by subclass')

    def parent(self):
        '''Return Position representing p's parent(or None if p is root)'''
        raise NotImplementedError('must be implemented by subclass')

    def num_children(self, p):
        '''Return the number of children that Position p has'''
        raise NotImplementedError('must be implemented by subclass')

    def children(self, p):
        '''Generate an iteration of Positions representing p's children'''
        raise NotImplementedError('must be implemented by subclass')

    def __len__(self):
        '''Return the total number of elements in the tree'''
        raise NotImplementedError('must be implemented by subclass')

    # -----------------concrete methods implemented in this class --------------------
    def is_root(self, p):
        '''Return True if Position p reprements the root of the tree'''
        return self.root() == p

    def is_leaf(self, p):
        '''Return True if Position p does not have any children'''
        return self.num_children() == p

    def is_empty(self):
        '''Return True if the Tree is empty'''
        return len(self) == 0

    def depth(self, p):
        ''' Return the number of levels separating Positon '''

        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    def _height1(self):
        '''Return the height of the tree'''
        return max(self.depth(p) for p in self.positions() if self.is_leaf(p))

    def _height2(self, p):
        '''Return the height of the subtree rooted at Position p'''
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height2(c) for c in self.children(p))

    def height(self, p=None):
        '''Return the height of the subtree rooted at Position p .
        If p is None,Return the height of the entire tree'''

        if p is None:
            p = self.root()
        return self._height2(p)  #start _height2 recursion
