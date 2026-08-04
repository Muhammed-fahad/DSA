class LinkedList:
    def __init__(self,val,next= None):
        self.val = val
        self.next = next

def SortLLBy012(node):
    head_node0 = LinkedList(-1)
    head_node1 = LinkedList(-1)
    head_node2 = LinkedList(-1)

    tail_node0 = head_node0
    tail_node1 = head_node1
    tail_node2 = head_node2

    curr = node

    while curr:
        nextNode = curr.next
        curr.next = None

        if curr.val == 0:
            tail_node0.next = curr
            tail_node0 = tail_node0.next

        elif curr.val == 1:
            tail_node1.next = curr
            tail_node1 = tail_node1.next

        else:
            tail_node2.next = curr
            tail_node2 = tail_node2.next

        curr = nextNode

    tail_node0.next = head_node1.next if head_node1.next else head_node2.next
    tail_node1.next = head_node2.next

    return head_node0.next

def printll(node):
  current = node
  while current:
    print(current.val , end= " -> ")
    current = current.next
  print("None")

node = LinkedList(0, LinkedList(1 , LinkedList(2 , LinkedList(0 , LinkedList(1 , LinkedList(2))))))
printll(SortLLBy012(node))