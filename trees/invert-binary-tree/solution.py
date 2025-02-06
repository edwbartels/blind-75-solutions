from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node) -> None:
            if not node:
                return

            lft = node.left
            rgt = node.right

            node.left = rgt
            node.right = lft

            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return root


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

    while queue and i < len(lst):
        node = queue.popleft()

        if i < len(lst):
            if lst[i] is not None:
                node.left = TreeNode(lst[i])
                queue.append(node.left)

            i += 1

        if i < len(lst):
            if lst[i] is not None:
                node.right = TreeNode(lst[i])
                queue.append(node.right)
            i += 1

    return root


# Converts Tree to list of values (breadth)
def tree_to_list(root: Optional[TreeNode]) -> list[Optional[int]]:
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        size = len(queue)
        has_children = False

        for _ in range(size):
            node = queue.popleft()

            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)

                if node.left or node.right:
                    has_children = True

            else:
                result.append(None)

        if not has_children:
            queue.clear()

    while result and result[-1] is None:
        result.pop()

    return result


# Test function - prints to terminal
def test_solution(input: list[int], output: list[int]) -> None:
    solution = Solution()

    tree = list_to_tree(input)
    result = solution.invertTree(tree)

    success = tree_to_list(result) == output

    print(f"\nInput: root = {input}")
    print(f"Output: {tree_to_list(result)} (Expected: {output})")
    print(f"Success: {success}")


# Test cases from prompt - (input: list[int], expected_output: list[int])
test_solution([1, 2, 3, 4, 5, 6, 7], [1, 3, 2, 7, 6, 5, 4])
test_solution([3, 2, 1], [3, 1, 2])
test_solution([], [])
test_solution([1, 2, None, 3], [1, None, 2, None, 3])
test_solution([1, None, 2, None, 3], [1, 2, None, 3])
test_solution([1, 2, 3, None, None, None, 4], [1, 3, 2, 4])
test_solution([1], [1])
test_solution([], [])
test_solution([1, 2, 3], [1, 3, 2])

print("\n")
