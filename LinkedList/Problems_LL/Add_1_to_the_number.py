# Input: 4->5->6
# Output: 4->5->7
# Explanation: 456 + 1 = 457

class LinkedList:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def addOne(head):
    carry = helper(head)

    if carry:
        newHead = LinkedList(carry)
        newHead.next = head
        return newHead

    return head


def helper(node):
    if node is None:
        return 1  # Initial carry (adding one)

    carry = helper(node.next)
    node.val += carry

    if node.val < 10:
        return 0

    node.val = 0
    return 1


def printLL(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


head = LinkedList(4,LinkedList(5,LinkedList(6)))
head = addOne(head)
printLL(head)