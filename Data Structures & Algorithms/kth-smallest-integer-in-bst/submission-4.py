# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(node: Optional[TreeNode] = root):
            nonlocal k
            if node is None:
                return -1
            r = dfs(node.left)
            if r != -1:
                return r
            k -= 1
            if k == 0:
                return node.val
            return dfs(node.right)
        return dfs()
        