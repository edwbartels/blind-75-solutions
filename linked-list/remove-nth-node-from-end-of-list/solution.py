from typing import Optional


# Provided ListNode definition
class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None) -> None:
        self.val = val
        self.next = next


# * Solution to problem
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        base = ListNode(0)
        base.next = head

        lead = follow = base

        for _ in range(n):
            if not lead or not lead.next:
                return head
            lead = lead.next

        while lead.next:
            lead = lead.next
            follow = follow.next

        follow.next = follow.next.next

        return base.next


# ! Testing Functions


# Helper to convert list of integer values to linked list nodes. (for testing)
def from_list(values: list[int]) -> Optional[ListNode]:
    if not values:
        return None

    if not all(0 <= val <= 100 for val in values):
        raise ValueError("All Values must be between 0 and 100")

    if len(values) > 30:
        raise ValueError("List Length cannot exceed 30")

    head = ListNode(values[0])
    current = head

    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


# Helper to convert linked list nodes to list of integer values
def to_list(head: Optional[ListNode]) -> list[int]:
    result = []
    current = head

    while current:
        result.append(current.val)
        current = current.next

    return result


# Test function - prints to terminal
def test_solution(input: list[int], n: int, output: list[int]) -> None:
    if not 1 <= n <= len(input):
        raise ValueError(f"n ({n}) must be between 1 and list length ({len(input)})")

    solution = Solution()

    linked_list = from_list(input)
    result = solution.removeNthFromEnd(linked_list, n)

    success = to_list(result) == output

    print(f"\nInput: head = {input}, n = {n}")
    print(f"Output: {to_list(result)} (Expected: {output})")
    print(f"Success: {success}")


# Test cases from prompt - (input: list[int], n: int, expected_output: list[int])
test_solution([1, 2, 3, 4], 2, [1, 2, 4])
test_solution([5], 1, [])
test_solution([1, 2], 2, [2])
print("\n")
