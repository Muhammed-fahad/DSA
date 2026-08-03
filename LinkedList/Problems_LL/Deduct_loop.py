class LinkedList:
  def __init__(self,val = 0 , next = None) -> None:
    self.val = val
    self.next = next

def cycle(node1):
  visited = set()
  current = node1
  while current:
    if current not in visited:
      visited.add(current)
      current = current.next
    else:
      return ("Its a cycle")
  return ("Its not a cycle")

node1 = LinkedList(1)
node2 = LinkedList(2)
node3 = LinkedList(3)
node1.next = node2
node2.next = node3
node3.next = node1

print(cycle(node1))