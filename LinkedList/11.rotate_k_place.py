class LinkedList:
  def __init__(self,val=0,next=None) -> None:
    self.val = val
    self.next = next
    
def rotate(node , k):
  current = node
  length = 1
  while current.next:
    current = current.next
    length += 1
  
  current = node
  for _ in range(length - k -1):
    current = current.next
    
  newnode = current.next
  current.next = None
  
  current = newnode
  
  while current.next:
    current = current.next
  current.next = node
  return newnode

def printll(node):
  current = node
  while current:
    print(current.val , end= " -> ")
    current = current.next
  print("None")
    
node = LinkedList(1, LinkedList(2 , LinkedList(3 , LinkedList(4 , LinkedList(5)))))
k = 2
final = rotate(node , k)
printll(final)