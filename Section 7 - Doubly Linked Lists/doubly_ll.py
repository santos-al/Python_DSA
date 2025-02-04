class Node:
  def __init__(self, value):
    self.value = value
    self.next = None
    self.prev = None

class DoublyLinkedList: 
  def __init__(self, value):
    new_node = Node(value)
    self.head = new_node
    self.tail = new_node
    self.length = 1
  
  def printList(self) -> None:
    temp = self.head
    while temp:
      print(temp.value)
      temp = temp.next
  
  def append(self, value) -> bool:
      new_node = Node(value)
      if self.length == 0:
        self.head = new_node
        self.tail = new_node
      else:
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
      self.length += 1
      return True
  
  def pop(self):
    if self.length == 0:
      return None
    temp = self.tail
    if self.length == 1:
      self.head = None
      self.tail = None
    else:
      self.tail = self.tail.prev
      self.tail.next = None
      temp.prev = None
    self.length -= 1
    return temp
  
  def prepend(self, value) -> bool:
    new_node = Node(value)
    if self.length == 0:
      self.head = new_node
      self.tail = new_node
    else:
      self.head.prev = new_node
      new_node.next = self.head
      self.head = new_node
    self.length += 1
    return True
  
  def pop_first(self):
    if self.length == 0:
      return None
    temp = self.head
    if self.length == 1:
      self.head = None
      self.tail = None
    else:
      self.head = self.head.next
      self.head.prev = None
      temp.next = None
    self.length -= 1
    return temp
   
  def get(self, index):
    if index < 0 or index >= self.length:
      return None
    if index < self.length / 2:
      temp = self.head
      for _ in range(index):
        temp = temp.next
      return temp
    else:
      temp = self.tail
      for _ in range(self.length - 1, index, -1):
        temp = temp.prev
      return temp

  def set(self, index, value) -> bool:
    temp = self.get(index)
    if temp:
      temp.value = value
      return True
    return False
  
  def insert(self, index, value) -> bool:
    if index < 0 or index > self.length:
      return False
    if index == 0:
      return self.prepend(value)
    elif index == self.length:
      return self.append(value)
    else: 
      new_node = Node(value)
      before = self.get(index - 1)
      after = before.next
      new_node.prev = before
      new_node.next = after
      before.next = new_node
      after.prev = new_node
    self.length += 1
    return True
  
  def remove(self, index):
    if index < 0 or index >= self.length:
      return None
    if index == 0:
      self.pop_first(index)
    elif index == self.length - 1:
      self.pop(index)
    else:
      temp = self.get(index)
      before = temp.prev
      after = temp.next

      before.next = after
      after.prev = before

      temp.next = None
      temp.prev = None

      self.length -= 1

      if self.length == 0:
        self.head = None
        self.tail = None
      
      return temp

  

# Tests
d_ll = DoublyLinkedList(5)
d_ll.append(6)
d_ll.prepend(4)
d_ll.printList()
d_ll.pop_first()
print("--------------")
d_ll.printList()
print("--------------")
print(d_ll.get(0).value)
print(d_ll.get(1).value)
print("--------------")
d_ll.set(1, 1)
d_ll.printList()
d_ll.prepend(7)
print("------------")
d_ll.printList()
print("--------------")
d_ll.remove(1)
d_ll.printList()