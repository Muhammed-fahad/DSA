class LinkedList:
    def __init__(self,val,next = None)->None:
        self.val = val
        self.next = next

def Search_element(node,target):
    while(node):
        if(node.val == target):
            return True
        node = node.next
    return False

if __name__ == "__main__":
    head = LinkedList(1,LinkedList(2,LinkedList(3,LinkedList(4,LinkedList(5)))))
    print(Search_element(head,target=6))
    