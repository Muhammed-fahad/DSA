class DDLinkedList:
    def __init__(self,val=None,next=None,prev=None):
        self.prev = prev
        self.val = val
        self.next = next

def printDDL(head):
    current = head
    while(current):
        print(current.val, end=" <-> ")
        current = current.next
    return 

def InsertDL(head,element):
    newnode = DDLinkedList(element)
    newnode.next = head
    head.prev = newnode
    printDDL(newnode)

 
if __name__ == "__main__":
    head = DDLinkedList(2)
    second = DDLinkedList(3)
    third = DDLinkedList(4)
    fourth = DDLinkedList(5)

    head.next = second
    second.prev = head

    second.next = third
    third.prev = second

    third.next = fourth
    fourth.prev = third

    InsertDL(head, 1)

