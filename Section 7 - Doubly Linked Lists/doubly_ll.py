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
  
  
