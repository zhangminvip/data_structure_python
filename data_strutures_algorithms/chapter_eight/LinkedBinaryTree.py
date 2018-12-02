import BinaryTree

class LinkedBinaryTree(BinaryTree):
    '''Linked representation of  a binary tree structure'''

    class _Node:             #Lightweight, nonpublic class for storing a node
        __slots__ = '_element','_parent','_left','_right'
        def __init__(self, element, parent=None, left=None,right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

    class Position(BinaryTree.Position):
        '''An abstract representing the location of a single element'''

        def __init__(self, container, node):
            self._container  = container
            self._node = node

        def element(self):
            '''Return the element stored at this Position'''
            return self._node._element

        def __eq__(self, other):
            '''Return True if other is a Position representing a same location'''
            return type(other) is type(self) and other._node is self._node

    def _validate(self,p):
        '''Return associated node, if position is vaild '''
        if not isinstance(p, self.Position):
            raise TypeError("p must be proper Position type")
        if p._container is not self:
            raise ValueError('p does not belong to this container ')
        if p._node._parent is p._node:
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node):
        '''Return Position instance if given node(or None if no node)'''
        return self.Position(self, node) if node is not None else None

    #-----------------------binary tree constructor------------------
    def __init__(self):
        '''Create an initial empty binary tree'''
        self._root = None
        self._size = 0

    #-----------------------pubilc accessors--------------------------
    def __len__(self):
        '''Return the total number of elements in the tree'''
        return self._size

    def root(self):
        '''Return the root Position of the tree (or None if tree is empty)'''
        return self._make_position(self._root)

    def parent(self, p):
        '''Return the Position of p's parent(or None if p is root)'''
        node = self._validate(p)
        return self._make_position(node._parent)

    def left(self, p):
        '''Return the Position of p's left child(or None if no left child)'''
        node = self._validate(p)
        return self._make_position(node._left)

    def right(self, p):
        '''Return the Position of p's right child(or None if no right child)'''
        node = self._validate(p)
        return self._make_position(node._right)

    def num_children(self, p):
        '''Return the number of children of Position p'''
        node = self._validate(p)
        count = 0
        if node._left is not None:    #left child exists
            count += 1
        if node._right is not None:   #right child exists
            count += 1
        return count

    def _add_root(self, e):
        '''Place element e at the root of an empty tree and return new Position

        Raise ValueError if tree nonempty
        '''

        if self._root is not None: raise ValueError('Root exists')
        self._size += 1
        self._root = self._Node(e)
        return self._make_position(self._root)

    def _add_left(self, p, e):
        '''Create a new left child for Position p ,storing element e

        Return the Position of new node
        Raise ValueError if Position p is invaild or p already has a left child.
        '''
        node = self._validate(p)
        if node is not None: raise ValueError('Left child exists')
        self._size += 1
        node._left = self._Node(e, node)       # node is its parent
        return self._make_position(node._left)

    def _add_right(self, p, e):
        '''Create a new right child for Position p, storing element e

        Return the Position of new node
        Raise ValueError if Position p is invalid or p already has right child.
        '''
        node = self._validate(p)
        if node is not None:raise ValueError('Right child exists')
        self._size += 1
        node._right = self._Node(e, node)      # node is its parent
        return self._make_position(node._right)

    def _replace(self, p, e):
        '''Replace the element at position p with e, and return old element'''
        node  = self._validate(p)
        old = node._element
        node._element = e
        return old
    




