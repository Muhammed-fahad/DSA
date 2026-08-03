class LinkedLisk:
  def __init__(self,val=0,next=None) -> None:
    self.val = val
    self.next = next
    
def swap(node):
  current = node
  while current and current.next:
    current.val , current.next.val = current.next.val , current.val
    current = current.next.next
  return node
    
def printll(node):
  current = node
  while current:
    print(current.val , end= " -> ")
    current = current.next
  print("None")
  
node = LinkedLisk(1, LinkedLisk(2 , LinkedLisk(3 , LinkedLisk(4 , LinkedLisk(5 , LinkedLisk(6))))))
swaped = swap(node)
printll(swaped)