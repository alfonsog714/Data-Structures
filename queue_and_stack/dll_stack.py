import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
  def __init__(self):
    self.size = 0
    # Why is our DLL a good choice to store our elements?
    self.storage = DoublyLinkedList()

  def push(self, value):
    self.size += 1
    self.storage.add_to_head(value)
  
  def pop(self):
    self.size -= 1
    self.storage.remove_fromt_head()

  def len(self):
    return self.size
