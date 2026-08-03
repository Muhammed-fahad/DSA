class LinkedLisk:
  def __init__(self,val=0,next=None) -> None:
    self.val = val
    self.next = next

def revers(node):
  prev = None
  current = node
  while current:
    nextnode = current.next
    current.next = prev
    prev = current
    current = nextnode
  return prev
    
def printll(node):
  current = node
  while current:
    print(current.val , end= " -> ")
    current = current.next
  print("None")
    
node = LinkedLisk(1, LinkedLisk(2 , LinkedLisk(3 , LinkedLisk(4 , LinkedLisk(5)))))
rev = revers(node)
printll(rev)