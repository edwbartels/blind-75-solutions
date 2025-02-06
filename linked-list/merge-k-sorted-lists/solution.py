from typing import Optional


# Provided ListNode definition
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# * Solution to problem
class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        lists = [lst for lst in lists if lst]
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]

        for i in range(1, len(lists)):
            base = ListNode(0)
            current = base

            l1 = lists[i - 1]
            l2 = lists[i]

            while l1 and l2:
                if l1.val <= l2.val:
                    current.next = l1
                    l1 = l1.next
                else:
                    current.next = l2
                    l2 = l2.next
                current = current.next

            if l1:
                current.next = l1
            if l2:
                current.next = l2

            lists[i] = base.next

        return lists[-1]


# ! Testing Functions


# Helper to convert list of integer values to linked list nodes. (for testing)
def from_list(lists: list[list[int]]) -> Optional[list[ListNode]]:
    if not lists:
        return None
    if len(lists) > 100:
        raise ValueError("List Length cannot exceed 100")

    result = []
    for lst in lists:
        if not lst:
            result.append(None)
            continue

        if not all(-1000 <= val <= 1000 for val in lst):
            raise ValueError("All values must be between -1000 and 1000")

        if not 0 <= len(lst) <= 100:
            raise ValueError("List Length cannot exceed 100")

        head = ListNode(lst[0])
        current = head

        for val in lst[1:]:
            current.next = ListNode(val)
            current = current.next
        result.append(head)
    return result


# Helper to convert linked list nodes to list of integer values
def to_list(head: Optional[ListNode]) -> list[int]:
    result = []
    current = head

    while current:
        result.append(current.val)
        current = current.next

    return result


# Test function - prints to terminal
def test_solution(input: list[list[int]], output: list[int]) -> None:
    solution = Solution()

    linked_list = from_list(input)
    result = solution.mergeKLists(linked_list)

    success = to_list(result) == output

    print(f"\nInput: head = {input}")
    print(f"Output: {to_list(result)} (Expected: {output})")
    print(f"Success: {success}")


test_solution([[1, 2, 4], [1, 3, 5], [3, 6]], [1, 1, 2, 3, 3, 4, 5, 6])
test_solution([], [])
test_solution([[]], [])
print("\n")
