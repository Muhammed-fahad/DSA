class LinkedList:
  def __init__(self, val = 0 , next = None) -> None:
    self.val = val
    self.next = next

def dupirem(node):
  current = node
  while current.next:
    if current.val == current.next.val:
      current.next = current.next.next
    else:
      current = current.next
  return node

def printll(node):
  current = node
  while current:
    print(current.val , end= " -> ")
    current = current.next
  print("None")

node = LinkedList(1 , LinkedList(2 , LinkedList(2 , LinkedList(2 , LinkedList(3 , LinkedList(4 , LinkedList(4)))))))
sorted = dupirem(node)
printll(sorted)