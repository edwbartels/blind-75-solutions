from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Solution to problem
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        if not p or not q:
            return False

        return (
            p.val == q.val
            and self.isSameTree(p.left, q.left)
            and self.isSameTree(p.right, q.right)
        )


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
def test_solution(input: tuple[list[int], list[int]], output: bool) -> None:
    solution = Solution()

    p_tree = list_to_tree(input[0])
    q_tree = list_to_tree(input[1])
    result = solution.isSameTree(p_tree, q_tree)
    success = result == output

    print(f"\nInput: root = {input}")
    print(f"Output: {result} (Expected: {output})")
    print(f"Success: {success}")


# Test cases from prompt - (input: tuple[list[int], list[int], expected: bool])
test_solution(([1, 2, 3], [1, 2, 3]), True)
test_solution(([4, 7], [4, None, 7]), False)
test_solution(([1, 2, 3], [1, 3, 2]), False)

print("\n")
