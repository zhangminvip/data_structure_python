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

        

