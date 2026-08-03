class LinkedList:
  def __init__(self,val = 0 , next = None) -> None:
    self.val = val
    self.next = next
    
def merge(node1 , node2):
  cur1 = node1
  cur2 = node2
  dummy = LinkedList()
  temp = dummy
  while cur1 and cur2 :
    if cur1.val < cur2.val:
      temp.next = cur1
      cur1 = cur1.next
    else:
      temp.next = cur2
      cur2 = cur2.next
    temp = temp.next
  if cur1:
    temp.next = cur1
  if cur2:
    temp.next = cur2
  return dummy.next

def printll(node):
  current = node
  while current:
    print(current.val , end= " -> ")
    current = current.next
  print("None")

node1 = LinkedList(1 , LinkedList(3 , LinkedList(5)))
node2 = LinkedList(2 , LinkedList(4 , LinkedList(6)))

merged = merge(node1 , node2)
printll(merged)