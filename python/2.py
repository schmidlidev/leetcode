# Add Two Numbers https://leetcode.com/problems/add-two-numbers/
# https://leetcode.com/submissions/detail/514180487/
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:

    head = ListNode()
    prev = head
    carry = 0
    while l1 or l2 or carry:
        if not l1:
            l1 = ListNode(0)
        if not l2:
            l2 = ListNode(0)

        sum = l1.val + l2.val + carry
        carry = 0
        if sum >= 10:
            sum -= 10
            carry = 1

        node = ListNode(sum)
        prev.next = node
        prev = node

        l1 = l1.next
        l2 = l2.next

    return head.next


l1 = ListNode(9, ListNode(9, ListNode(9)))
l2 = ListNode(1)
l1 = ListNode(0)
l2 = ListNode(0)

result = addTwoNumbers(l1, l2)
while result:
    print(result.val)
    result = result.next
