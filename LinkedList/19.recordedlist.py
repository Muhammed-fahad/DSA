class LinkedList:
  def __init__(self,val=0,next=None) -> None:
    self.val = val
    self.next = next

def reverse(node):
  temp = None
  current = node
  
  while current :
    nextnode = current.next
    current.next = temp
    temp = current
    current = nextnode
  return temp
    
def record(node):
  fast = node
  slow = node
  
  while fast and fast.next:
    fast = fast.next.next
    slow = slow.next
    
  nextnode = slow.next
  slow.next = None
  reversed = reverse(nextnode)
  
  dummy = LinkedList()
  temp = dummy
  
  while reversed:
    temp.next = node
    node = node.next
    temp = temp.next
    
    temp.next = reversed
    reversed = reversed.next
    temp = temp.next
  
  if node:
    temp.next = node
    
  return dummy.next
  
      
def printll(node):
  current = node
  while current:
    print(current.val , end= " -> ")
    current = current.next
  print("None")

node = LinkedList(1, LinkedList(2 , LinkedList(3 , LinkedList(4 , LinkedList(5 , LinkedList(6))))))
recorded = record(node)
printll(recorded)