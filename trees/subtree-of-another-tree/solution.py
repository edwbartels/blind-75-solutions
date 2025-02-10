from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        def is_same_tree(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False

            return (
                p.val == q.val
                and is_same_tree(p.left, q.left)
                and is_same_tree(p.right, q.right)
            )

        if is_same_tree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


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

    root = list_to_tree(input[0])
    subRoot = list_to_tree(input[1])
    result = solution.isSubtree(root, subRoot)
    success = result == output

    print(f"\nInput: root = {input}")
    print(f"Output: {result} (Expected: {output})")
    print(f"Success: {success}")


# Test cases from prompt - (input: tuple[list[int], list[int], expected: bool])
test_solution(([1, 2, 3, 4, 5], [2, 4, 5]), True)
test_solution(([1, 2, 3, 4, 5, None, None, 6], [2, 4, 5]), False)

print("\n")
