# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        counter = 0
        def dfs(root: TreeNode, greatest_in_path: int):
            nonlocal counter
            if root is None:
                return
            elif root.val >= greatest_in_path:
                counter += 1
                greatest_in_path = root.val

            dfs(root.left, greatest_in_path)
            dfs(root.right, greatest_in_path)
        dfs(root, root.val)
        return counter
        