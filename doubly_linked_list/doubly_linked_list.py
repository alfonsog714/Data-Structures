"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""
  def insert_after(self, value):
    current_next = self.next
    self.next = ListNode(value, self, current_next)
    if current_next:
      current_next.prev = self.next

  """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""
  def insert_before(self, value):
    current_prev = self.prev
    self.prev = ListNode(value, current_prev, self)
    if current_prev:
      current_prev.next = self.prev

  """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""
  def delete(self):
    if self.prev:
      self.prev.next = self.next
    if self.next:
      self.next.prev = self.prev

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""

class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node
    self.length = 1 if node is not None else 0

  def __len__(self):
    return self.length
  
  """Wraps the given value in a ListNode and inserts it 
  as the new head of the list. Don't forget to handle 
  the old head node's previous pointer accordingly."""
  def add_to_head(self, value):
    new_node = ListNode(value, None, None)
    if not self.head and not self.tail: #We know that this is first node head/tail
      self.head = new_node
      self.tail = new_node
    else: # We know we're inserting at the beginnning
      new_node.next = self.head
      self.head.prev = new_node
      self.head = new_node
    
    self.length += 1

  """Removes the List's current head node, making the
  current head's next node the new head of the List.
  Returns the value of the removed Node."""
  def remove_from_head(self):
    value = self.head.value
    self.delete(self.head)
    return value


  """Wraps the given value in a ListNode and inserts it 
  as the new tail of the list. Don't forget to handle 
  the old tail node's next pointer accordingly."""
  def add_to_tail(self, value):
    new_node = ListNode(value, None, None)
    if not self.head and not self.tail:
      self.head = new_node
      self.tail = new_node
    else:
      new_node.prev = self.tail
      self.tail.next = new_node # Bring up that a known bad state passed the test
      self.tail = new_node

    self.length += 1

  """Removes the List's current tail node, making the 
  current tail's previous node the new tail of the List.
  Returns the value of the removed Node."""
  def remove_from_tail(self):
    value = self.tail.value
    self.delete(self.tail)
    return value

  """Removes the input node from its current spot in the 
  List and inserts it as the new head node of the List."""
  def move_to_front(self, node):
    if node is self.head:
      return # This returns nothing since the head would already be at the front
    value = node.value
    self.delete(node)
    self.add_to_head(value)

  """Removes the input node from its current spot in the 
  List and inserts it as the new tail node of the List."""
  def move_to_end(self, node):
    if node is self.tail:
      return # This returns nothing since the head would already be at the front
    value = node.value
    self.delete(node)
    self.add_to_tail(value)

  """Removes a node from the list and handles cases where
  the node was the head or the tail"""
  def delete(self, node):
    self.length -= 1
    if node is self.head and node is self.tail:
      self.head = None
      self.tail = None
      #Done, node is effectively deleted
    elif node is self.head:
      self.head = node.next
      node.delete()
    else:
      node.delete()

    
  """Returns the highest value currently in the list"""
  def get_max(self):
    if not self.head and not self.tail: # If there is no head or tail in this linked list
      return None
    max_val = self.head.value
    current = self.head
    while current:
      if current.value > max_val:
        max_val = current.value
      current = current.next

    return max_val