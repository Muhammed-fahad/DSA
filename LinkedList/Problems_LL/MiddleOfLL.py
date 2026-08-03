class LinkedLisk:
  def __init__(self, val = 0 , next = None) -> None:
    self.val = val
    self.next = next

def middle(node):
  fast = node
  slow = node
  while fast and fast.next:
    fast = fast.next.next
    slow = slow.next
  return (slow.val)
  
node = LinkedLisk(1, LinkedLisk(2 , LinkedLisk(3 , LinkedLisk(4 , LinkedLisk(5 , LinkedLisk(6))))))
print(middle(node))
