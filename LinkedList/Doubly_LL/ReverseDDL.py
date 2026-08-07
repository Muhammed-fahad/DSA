class DDLinkedList:
    def __init__(self, val=None, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


def printDDL(head):
    while head:
        print(head.val, end=" <-> ")
        head = head.next
    print("None")


def ReverseDDL(head):
    current = head
    temp = None

    while current:
        temp = current.prev

        current.prev = current.next
        current.next = temp

        current = current.prev

    if temp:
        head = temp.prev

    return head


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

head = ReverseDDL(head)
printDDL(head)