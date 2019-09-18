from doubly_linked_list import DoublyLinkedList

class LRUCache:
  """
  Our LRUCache class keeps track of the max number of nodes it
  can hold, the current number of nodes it is holding, a doubly-
  linked list that holds the key-value entries in the correct 
  order, as well as a storage dict that provides fast access
  to every node stored in the cache.
  """

  """
  Things I need:
  Max number AKA limit of nodes it can hold
  Current number of nodes it is holding
  A doubly-linked list that holds key-value pairs
  A storage dictionary which I assume acts as the "cache"
  """
  def __init__(self, limit=10):
    self.limit = limit
    self.size = 0
    self.storage = {}
    self.linked_list = DoublyLinkedList()

  """
  Retrieves the value associated with the given key. Also
  needs to move the key-value pair to the end of the order
  such that the pair is considered most-recently used.
  Returns the value associated with the key or None if the
  key-value pair doesn't exist in the cache. 
  """
  def get(self, key):
    # Check if the key exists in the cache
      # If not, return None
      # Else retrieve the item, move it to the head of the linked list and increment its count by 1
    # ----------------------------------------------
    # BRIAN'S SOLUTION -----------------------------
    # Pull the value out of the dict using they key
    if key in self.storage:
      node = self.storage[key]
    # Update position in the list
      self.linked_list.move_to_front(node)
      return node.value[1]
    # Or return none
    else:
      return None
    
    
    
    # ----------------------------------------------
    
    # MY SOLUTION ---------------------------------

    # if self.size is 0 or key not in self.storage:
    #   return None
    # else:
    #   value = self.storage[key]

    #   self.linked_list.delete(value[1])
    #   self.linked_list.add_to_head([key, value[0]])
    #   # print(value)
    #   return value[0]

    # ----------------------------------------------

  """
  Adds the given key-value pair to the cache. The newly-
  added pair should be considered the most-recently used
  entry in the cache. If the cache is already at max capacity
  before this entry is added, then the oldest entry in the
  cache needs to be removed to make room. Additionally, in the
  case that the key already exists in the cache, we simply 
  want to overwrite the old value associated with the key with
  the newly-specified value. 
  """
  def set(self, key, value):
    #Add it to the Linked List (key-value pair)

    # If there's already something with the same key name, overwrite the value
    # Check if there is space
      # If not, delete the oldest item in the cache and linked list
      # Else, add the new item to the head because it's the "most-recently used"

    # BRIAN'S SOLUTION -------

    # If already exists, overwrite value -
    if key in self.storage:
      # update dict
      node = self.storage[key]
      node.value = (key, value)
      # Mark as most recently used - Put in the head of the DLL
      self.linked_list.move_to_front(node)
      return
    
    # If at max capacity, dump the oldest - remove from tail of DLL
    if self.size == self.limit:
      # dump the oldest:
      # remove it from the linked list
      # remove it from the dictionary
      del self.storage[self.linked_list.tail.value[0]]
      self.linked_list.remove_from_tail()
      self.size -= 1
    # Add pair to the cache - add to dict and add its nodes/DLL
    self.linked_list.add_to_head((key, value))
    self.storage[key] = self.linked_list.head
    self.size += 1

    #-----------------------------

    # MY SOLUTION -------
    # if key in self.storage.keys():
    #   saved_value = self.storage[key]

    #   # self.linked_list.move_to_front(saved_value[1])
    #   self.linked_list.delete(saved_value[1])
    #   self.linked_list.add_to_head([key, value])
    #   self.storage[key] = [value, self.linked_list.head]
    #   return

    # if self.limit == self.size:
    #   deleted_node = self.linked_list.tail
    #   self.linked_list.remove_from_tail()
    #   del self.storage[deleted_node.value[0]]
    #   self.size -= 1
    
    # self.linked_list.add_to_head([key, value])
    # self.storage[key] = [value, self.linked_list.head]
    # self.size += 1
    
    # --------------------------------------

"""
{
    'item': ['a', <doubly_linked_list.ListNode object at 0x00320D10>],
    'item2': ['b', <doubly_linked_list.ListNode object at 0x00320C10>],
    'item2': ['b', <doubly_linked_list.ListNode object at 0x00320C10>],
    'item2': ['b', <doubly_linked_list.ListNode object at 0x00320C20>],
    'item2': ['b', <doubly_linked_list.ListNode object at 0x00323C10>],
    'item2': ['b', <doubly_linked_list.ListNode object at 0x00320Z14>],
}

const something = {
    item: ['a', <doubly_linked_list.ListNode object at 0x00320D10>],
    item2: ['b', <doubly_linked_list.ListNode object at 0x00320C10>],
    item2: ['b', <doubly_linked_list.ListNode object at 0x00320C10>],
    item2: ['b', <doubly_linked_list.ListNode object at 0x00320C20>],
    item2: ['b', <doubly_linked_list.ListNode object at 0x00323C10>],
    item2': ['b', <doubly_linked_list.ListNode object at 0x00320Z14>],
}
"""

testing = LRUCache(3)

testing.set('item1', 'a')
testing.set('item2', 'b')
testing.set('item3', 'c')

print(f"Line 108: {testing.get('item1')} - Should be a") # a
print(f"Line 109: {testing.get('item2')} - Should be b") # b
print(f"Line 110: {testing.get('item3')} - Should be c") # c

testing.set('item2', 'z')

print(f"Line 113: {testing.get('item2')} - Should be z") # z

testing.set('item2', 'd')
testing.set('item1', 'f')

print(f"Line 117: {testing.get('item1')} - Should be f") #f
print(f"Line 118: {testing.get('item2')} - Should be d") #d
print(f"Line 119: {testing.get('item3')} - Should be c") #c

testing.set('item3', 'oof')

print(f"Line 122: {testing.get('item3')} - Should be oof") # oof

print("\n--------------------\n")

testing.set('item1', 'a')
testing.set('item2', 'b')
testing.set('item3', 'c')

print(f"Line 128: {testing.get('item1')} - Should be a")

testing.set('item4', 'd')

print(f"Line 131: {testing.get('item1')} - Should be a")
print(f"Line 132: {testing.get('item3')} - Should be c")
print(f"Line 133: {testing.get('item4')} - Should be d")
print(f"Line 134: {testing.get('item2')} - Should be b")