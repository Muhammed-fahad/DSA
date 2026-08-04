class LinkedList:
  def __init__(self, val=0, next=None):
      self.val = val
      self.next = next

def intersection(headA , headB):
  if not headA or not headB:
    return None
  
  point1 = headA
  point2 = headB
  
  while point1 != point2:
    point1 = point1.next if point1 else headB
    point2 = point2.next if point2 else headA
  
  return point1.val

shared = LinkedList(2, LinkedList(4))
headA = LinkedList(1, LinkedList(9, LinkedList(1, shared)))
headB = LinkedList(3, shared)
print(intersection(headA,headB))