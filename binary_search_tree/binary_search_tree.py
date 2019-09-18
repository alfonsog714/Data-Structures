import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack

class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

    """
    Rules of inserting in the binary tree ----
      1. If the current node you're trying to insert is larger than or equal to the parent node, it goes to the right.
      2. If the current node you're trying to insert is less than the parent node, it goes to the left.
    """

  def insert(self, value):
    """
    * `insert` adds the input value to the binary search tree, adhering to the rules of the ordering of elements in a binary search tree.
    """
    # Grab a hold of the current node
    current_tree = self
    # We need to loop through the tree
    checking = True
    while checking is True:
      # If the passed in node's value is greater than the current one, set it to the right
      if value >= current_tree.value:
        current_tree.right = value
      # If the passed in node's value is less than the current node, set it to the left
      elif value < current_tree.value:
        current_tree.left = value
      # If the passed in value

  def contains(self, target):
    """
    * `contains` searches the binary search tree for the input value, returning a boolean indicating whether the value exists in the tree or not.
    """
    pass

  def get_max(self):
    """
    * `get_max` returns the maximum value in the binary search tree.
    """
    pass

  def for_each(self, cb):
    """
    * `for_each` performs a traversal of _every_ node in the tree, executing the passed-in callback function on each tree node value. There is a myriad of ways to perform tree traversal; in this case any of them should work. 
    """
    pass