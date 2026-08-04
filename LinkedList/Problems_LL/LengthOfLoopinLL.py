# To find the Length of Loop in LL
class LinkedList:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next

def FindMeetingPoint(node):
    slow = node
    fast = node

    while(fast and fast.next):
        slow = slow.next
        fast = fast.next.next

        if(slow == fast):
            return FindLength(slow)    
    return 0
        
def FindLength(slow):
    length = 1
    temp = slow.next

    while temp != slow :
        length += 1
        temp = temp.next
    return length

if __name__ == "__main__":
    
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

    print(FindMeetingPoint(node1))