class LinkedList:
  def __init__(self,val=0,next=None) -> None:
    self.val = val
    self.next = next

def palindrome(node):
  fast = node
  slow = node
  prev = None
  while fast and fast.next:
    fast = fast.next.next
    nextnode = slow.next
    slow.next = prev
    prev = slow
    slow = nextnode

  if fast:
    slow = slow.next
   
  while slow and prev:
    if slow.val != prev.val:
      return False
    slow = slow.next
    prev = prev.next
  return True
  

node = LinkedList(1, LinkedList(2 , LinkedList(3 , LinkedList(2 , LinkedList(1)))))
print(palindrome(node))
