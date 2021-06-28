# Merge Two Sorted Lists https://leetcode.com/problems/merge-two-sorted-lists/
# * Works but should be improved for legibility.
# https://leetcode.com/submissions/detail/514212882/
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    head = ListNode()
    prev = head
    while l1 or l2:
        if not l1:
            prev.next = l2
            l2 = l2.next
            prev = prev.next
            continue
        if not l2:
            prev.next = l1
            l1 = l1.next
            prev = prev.next
            continue

        if l1.val <= l2.val:
            prev.next = l1
            l1 = l1.next
        else:
            prev.next = l2
            l2 = l2.next

        prev = prev.next
    return head.next
