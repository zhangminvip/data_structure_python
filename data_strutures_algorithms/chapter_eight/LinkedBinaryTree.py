import BinaryTree

class LinkedBinaryTree(BinaryTree):
    '''Linked representation of  a binary tree structure'''

    class _Node:
        __slots__ = '_element','_parent','_left','_right'
        def __init__(self, element, parent=None, left=None,right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right
        
