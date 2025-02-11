from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Solution to problem
class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        if not root or root == p or root == q:
            return root

        p_val = p.val
        q_val = q.val
        curr = root

        while curr:
            if p_val < curr.val and q_val < curr.val:
                curr = curr.left

            elif p_val > curr.val and q_val > curr.val:
                curr = curr.right

            else:
                return curr

        return None


# Converts List of values to binary tree (breadth)
def list_to_tree(
    lst: list[int], p_val: int, q_val: int
) -> tuple[TreeNode, TreeNode, TreeNode]:
    if not lst:
        return None

    p = q = None

    valid_values = [val for val in lst if val is not None]
    if not all(-100 <= value <= 100 for value in valid_values):
        raise ValueError("All values must be between -100 and 100")

    if not 2 <= len(valid_values) <= 100:
        raise ValueError("List Length must be between 2 and 100")

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
                if node.left.val == p_val:
                    p = node.left
                if node.left.val == q_val:
                    q = node.left
            queue.append(node.left) if node.left else None
            i += 1

        # Handle right child
        if i < len(lst):
            if lst[i] is not None:
                node.right = TreeNode(lst[i])
                if node.right.val == p_val:
                    p = node.right
                if node.right.val == q_val:
                    q = node.right
            queue.append(node.right) if node.right else None
            i += 1

    return (root, p, q)


# Test function - prints to terminal
def test_solution(input: tuple[list[int], int, int], output: int) -> None:
    solution = Solution()

    if input[1] == input[2]:
        raise ValueError("Input node values cannot be equal")

    tree = list_to_tree(*input)
    result = solution.lowestCommonAncestor(tree[0], tree[1], tree[2])
    success = result.val == output

    print(f"\nInput: root = {input[0]}, p = {input[1]}, q = {input[2]}")
    print(f"Output: {result.val} (Expected: {output})")
    print(f"Success: {success}")


test_solution(([5, 3, 8, 1, 4, 7, 9, None, 2], 3, 8), 5)
test_solution(([5, 3, 8, 1, 4, 7, 9, None, 2], 3, 4), 3)

print("\n")
