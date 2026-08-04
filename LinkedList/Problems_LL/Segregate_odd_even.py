class LinkedList:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next

def SegreateOddEven(head):

    evenHead = LinkedList(-1)
    oddHead = LinkedList(-1)

    evenTail = evenHead
    oddTail = oddHead

    temp = head

    while temp:
        nextNode = temp.next
        temp.next = None

        if temp.val % 2 == 0:
            evenTail.next = temp
            evenTail = evenTail.next
        else:
            oddTail.next = temp
            oddTail = oddTail.next

        temp = nextNode

    evenTail.next = oddHead.next
    return evenHead.next

def printll(node):
  current = node
  while current:
    print(current.val , end= " -> ")
    current = current.next
  print("None")

if __name__ == "__main__":
    node = LinkedList(1, LinkedList(2 , LinkedList(3 , LinkedList(9 , LinkedList(4 , LinkedList(11))))))
    printll(SegreateOddEven(node))
