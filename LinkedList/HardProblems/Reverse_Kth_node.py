#input: 1 2 3 4 5 6 7    k = 3
#op : 3 2 1 6 5 4 7

class LinkedList:
    def __init__(self,val,next = None):
        self.val = val
        self.next = next

def findKthNode(node,k):
    while node and k>1:
        node = node.next
        k-=1
    return node


def reverse(node):
    prev = None
    curr = node
    
    while curr:
        nextnode = curr.next
        curr.next = prev
        prev = curr
        curr = nextnode
    return prev

def reverseKthNode(head, k):
    dummy = LinkedList(0)
    dummy.next = head
    prevGroup = dummy

    while True:

        kthNode = findKthNode(prevGroup.next, k)
        if kthNode is None:
            break

        nextGroup = kthNode.next
        kthNode.next = None

        groupHead = prevGroup.next
        reversedHead = reverse(groupHead)

        prevGroup.next = reversedHead

        groupHead.next = nextGroup

        prevGroup = groupHead

    printLL(dummy.next)


def printLL(node):
    temp = node
    while(node):
        print(node.val,end=" -> ")
        node = node.next
    return temp

if __name__ == "__main__":
    node = LinkedList(1,LinkedList(2,LinkedList(3,LinkedList(4,LinkedList(5,LinkedList(6))))))
    k = int(input("Enter the Kth element: "))
    reverseKthNode(node,k)