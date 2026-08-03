class LinkedList:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next


def FindStartingPointofLL(node):
    value = set()
    while(node):
        if(node in value):
            return node.val
        value.add(node)
        node = node.next
    return None

if __name__ == "__main__":
    # Circular LL
    node1 = LinkedList(1)
    node2 = LinkedList(2)
    node3 = LinkedList(3)
    node4 = LinkedList(4)
    node5 = LinkedList(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node3

    # node1 = LinkedList(1, LinkedList(2 , LinkedList(3 , LinkedList(4 , LinkedList(5 , LinkedList(6))))))
    print(FindStartingPointofLL(node1))