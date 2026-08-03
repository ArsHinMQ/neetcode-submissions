# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root: TreeNode, greatest_in_path: int):
            count = 0
            if root is None:
                return 0
            elif root.val >= greatest_in_path:
                count += 1
                greatest_in_path = root.val

            return count + dfs(root.left, greatest_in_path) + dfs(root.right, greatest_in_path)
        return dfs(root, root.val)
        