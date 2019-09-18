import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack

class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    # Left and right are essentially pointers
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
      # If the passed in node's value is greater than the current one, and there is a value to the right, move down to the right
      if value >= current_tree.value and current_tree.right:
        current_tree = current_tree.right
      # If the passed in node's value is less than the current node, and there is a left node, set current node to the left node
      elif value < current_tree.value and current_tree.left:
        current_tree = current_tree.left
      # If the passed in value is greater than or equal to the current value and there is no right node, make a new node at the current.right and stop loop
      elif value >= current_tree.value and not current_tree.right:
        current_tree.right = BinarySearchTree(value)
        checking = False
      # If the passed in value is less than the current val and there is no left node, make a new node at curret.left and stop loop
      elif value < current_tree.value and not current_tree.left:
        current_tree.left = BinarySearchTree(value)
        checking = False
        
  def contains(self, target):
    """
    * `contains` searches the binary search tree for the input value, returning a boolean indicating whether the value exists in the tree or not.
    """
    # Similar to the loop above, we can traverse that way.
    current_tree = self
    checking = True
    
    
    while checking is True:
      if current_tree.value == target:
        checking = False
        return True
      elif target >= current_tree.value and current_tree.right:
        current_tree = current_tree.right
      elif target < current_tree.value and current_tree.left:
        current_tree = current_tree.left
      elif target >= current_tree.value and not current_tree.right:
        checking = False
        return False
      elif target < current_tree.value and not current_tree.left:
        checking = False
        return False


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