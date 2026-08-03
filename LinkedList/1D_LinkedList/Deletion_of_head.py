class LinkedList:
    def __init__(self,val,next=None)->None:
        self.val = val
        self.next = next

def Deletion_of_head(node):
    return node.next

def PrintLL(node):
    current = node
    while(current):
        print(current.val, end = " -> ")
        current = current.next
    print("None")

if __name__ == "__main__":
    node = LinkedList(2,LinkedList(3,LinkedList(4,LinkedList(5))))
    val = Deletion_of_head(node) # Change value here what you want to delete in position 0
    PrintLL(val)