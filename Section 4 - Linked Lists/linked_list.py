class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class LinkedList:
  def __init__(self, value):
    new_node = Node(value)
    self.length = 1
    self.head = new_node
    self.tail = new_node
  
  def print(self):
    temp = self.head
    while temp != None:
      print(temp.value)
      temp = temp.next

  def append(self, value) -> bool:
    new_node = Node(value)
    if self.head == None: # Or self.length == 0
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next = new_node
      self.tail = new_node
    self.length += 1
    return True
  
  def pop(self):
    if self.length == 0:
      return None
    temp = self.head
    pre = self.head
    while temp.next != None:
      pre = temp
      temp = temp.next
    self.tail = pre
    self.tail.next = None
    self.length -= 1
    if self.length == 0:
      self.head = None
      self.tail = None
    return temp


  def prepend(self, value) -> bool:
    new_node = Node(value)
    if self.length == 0:
      self.head = new_node
      self.tail = new_node
    else:
      new_node.next = self.head
      self.head = new_node
    self.length += 1
    return True
  
  def pop_first(self):
    if self.length == 0:
      return None
    temp = self.head
    self.head = self.head.next
    temp.next = None
    self.length -= 1
    if self.length == 0:
      self.tail = None
    return temp

  def get(self, index: int):
    if index >= self.length or index < 0:
      return None
    temp = self.head
    for _ in range(index):
      temp = temp.next
    return temp
  
  def set_value(self, index: int, value) -> bool:
    temp = self.get(index)
    if temp:
      temp.value = value
      return True
    return False

  def insert(self, index: int, value) -> bool:
    if index > self.length or index < 0:
      return False
    if index == 0:
      return self.prepend(value)
    if index == self.length:
      return self.append(value)
    
    new_node = Node(value)
    temp = self.get(index - 1)
    new_node.next = temp.next
    temp.next = new_node
    self.length += 1
    return True
  
  def remove(self, index: int):
      if index < 0 or index >= self.length:
          return None
      if index == 0:
          return self.pop_first()
      if index == self.length - 1:
          return self.pop()
      pre = self.get(index - 1)
      temp = pre.next
      pre.next = temp.next
      temp.next = No
      self.length -= 1
      return temp

  def reverse(self) -> None:
    # Flip head and tail
    temp = self.head
    self.head = self.tail
    self.tail = temp

    after = temp.next
    before = None

    for _ in range(self.length):

      # Set after to the next Node
      after = temp.next

      # Flip the arrow on temp and point it in the other direction 
      temp.next = before

      # Move before up to temp
      before = temp

      # Move temp across the gap
      temp = after





my_linked_list = LinkedList(4)
my_linked_list.append(3)
print("List 1")
my_linked_list.print()
print("list 2")
my_linked_list.print()
my_linked_list.prepend(10)
print("list 3")
my_linked_list.print()
print("list 4")
my_linked_list.set_value(0, 2)
my_linked_list.print()
print("list 5")
my_linked_list.insert(1, 23)
my_linked_list.print()
