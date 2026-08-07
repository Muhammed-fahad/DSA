class DDLinkedList:
    def __init__(self,val=None,next=None,prev=None):
        self.prev = prev
        self.val = val
        self.next = next

def Deletehead(head):
    nextnode = head.next
    nextnode.prev = None
    printDDL(nextnode)

def printDDL(head):
    current = head
    while(current):
        print(current.val, end=" <-> ")
        current = current.next
    return

if __name__ == "__main__":
    head = DDLinkedList(1)
    second = DDLinkedList(2)
    third = DDLinkedList(3)
    fourth = DDLinkedList(4)

    head.next = second
    second.prev = head

    second.next = third
    third.prev = second

    third.next = fourth
    fourth.prev = third
    Deletehead(head)