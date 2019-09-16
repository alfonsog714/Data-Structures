import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Queue:
  def __init__(self):
    self.size = 0
    # Why is our DLL a good choice to store our elements?
    self.storage = DoublyLinkedList()

  def enqueue(self, value):
    self.size += 1
    if self.storage.head is None:
      self.storage.add_to_head(value)
    else:
      self.storage.add_to_tail(value)
  
  def dequeue(self):
    if self.size == 0:
      return
    else:
      self.storage.delete(self.storage.head)

  def len(self):
    return self.size
