class LinkedList:
  def __init__(self, val = 0 , next = None) -> None:
    self.val = val
    self.next = next

def remove(node,n):
  current = node
  for _ in range(n):
    current = current.next
  pointer = node
  while current.next:
    current = current.next
    pointer = pointer.next
  pointer.next = pointer.next.next
  return node

def printll(node):
  current = node
  while current:
    print(current.val , end= " -> ")
    current = current.next
  print("None")
  

node = LinkedList(1 , LinkedList(2 , LinkedList(3 , LinkedList(4 ,LinkedList(5)))))
n = int(input("Enter nth node u wanted to remove: "))
removed = remove(node , n)
printll(removed)