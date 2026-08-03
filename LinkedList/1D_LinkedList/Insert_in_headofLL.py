class LinkedList:
    def __init__(self,val,next=None)->None:
        self.val = val
        self.next = next

def Insert_head(node,val):
    node1 = LinkedList(val)
    node1.next = node
    return node1


def PrintLL(node):
    current = node
    while(current):
        print(current.val, end = " -> ")
        current = current.next
    print("None")

if __name__ == "__main__":
    node = LinkedList(2,LinkedList(3,LinkedList(4,LinkedList(5))))
    val = Insert_head(node,val = 1) # Change value here what you want to insert in position 0
    PrintLL(val)