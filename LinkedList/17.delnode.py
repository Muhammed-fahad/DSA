class LinkedList:
  def __init__(self,val=0,next=None) -> None:
    self.val = val
    self.next = next
    
def delete_node(node):
  node.val = node.next.val
  node.next = node.next.next
  
def printll(node):
  current = node
  while current:
    print(current.val , end= " -> ")
    current = current.next
  print("None")


head = LinkedList(1, LinkedList(2, LinkedList(3, LinkedList(4, LinkedList(5)))))
node_to_delete = head.next.next
delete_node(node_to_delete)
printll(head)