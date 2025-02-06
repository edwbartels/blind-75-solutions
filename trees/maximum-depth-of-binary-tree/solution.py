from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


# ! Testing Functions


# Converts List of values to binary tree (breadth)
def list_to_tree(lst: list[int]) -> Optional[TreeNode]:
    if not lst:
        return None

    valid_values = [val for val in lst if val is not None]
    if not all(-100 <= value <= 100 for value in valid_values):
        raise ValueError("All values must be between -100 and 100")

    if len(valid_values) > 100:
        raise ValueError("List Length cannot exceed 100")

    root = TreeNode(lst[0]) if lst[0] is not None else None
    if not root:
        return None

    queue = deque([root])
    i = 1

    while i < len(lst):
        if not queue:
            break

        node = queue.popleft()

        # Handle left child
        if i < len(lst):
            if lst[i] is not None:
                node.left = TreeNode(lst[i])
            queue.append(node.left) if node.left else None
            i += 1

        # Handle right child
        if i < len(lst):
            if lst[i] is not None:
                node.right = TreeNode(lst[i])
            queue.append(node.right) if node.right else None
            i += 1

    return root


# Test function - prints to terminal
def test_solution(input: list[int], output: int) -> None:
    solution = Solution()

    tree = list_to_tree(input)
    result = solution.maxDepth(tree)
    success = result == output

    print(f"\nInput: root = {input}")
    print(f"Output: {result} (Expected: {output})")
    print(f"Success: {success}")


# Test cases from prompt - (input: list[int], expected_output: int)
test_solution([1, 2, 3, None, None, 4], 3)
test_solution([], 0)


print("\n")
