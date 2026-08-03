class ListNode:
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

shared = ListNode(2, ListNode(4))
headA = ListNode(1, ListNode(9, ListNode(1, shared)))
headB = ListNode(3, shared)
print(intersection(headA,headB))