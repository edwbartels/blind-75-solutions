from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        p1 = head
        p2 = head.next

        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next

        mid = p1.next
        p1.next = None

        prev = None
        current = mid

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        l1 = head
        l2 = prev

        while l2:
            next1 = l1.next
            next2 = l2.next

            l1.next = l2
            l2.next = next1

            l1 = next1
            l2 = next2
