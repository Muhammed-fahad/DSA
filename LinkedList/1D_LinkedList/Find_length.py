class LinkedList:
    def __init__(self,val,next=None)->None:
        self.val = val
        self.next = next

def Find_length(node):
    count = 0
    while(node):
        count+=1
        node = node.next
    return count


def PrintLL(node):
    current = node
    while(current):
        print(current.val, end = " -> ")
        current = current.next
    print("None")

if __name__ == "__main__":
    node = LinkedList(2,LinkedList(3,LinkedList(4,LinkedList(5,LinkedList(6)))))
    val = Find_length(node) # Change value here what you want to insert in position 0
    print(val)