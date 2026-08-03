class LinkedList:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next

def DeleteMiddleNode(head):
    # Empty list or single node
    if head is None or head.next is None:
        return None

    slow = head
    fast = head
    prev = None

    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    # Delete the middle node
    prev.next = slow.next

    return head

def PrintLL(node):
    current = node
    while(current):
        print(current.val, end = " -> ")
        current = current.next
    print("None")

if __name__ == "__main__":
    node = LinkedList(1 , LinkedList(2 , LinkedList(3 , LinkedList(4 ,LinkedList(5)))))
    PrintLL(DeleteMiddleNode(node))