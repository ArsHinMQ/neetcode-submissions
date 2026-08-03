# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True
        def dfs(root: Optional[TreeNode]):
            nonlocal res
            
            if root is None:
                return 0

            l = 1 + dfs(root.left)
            r = 1 + dfs(root.right)

            if abs(r - l) > 1:
                res = False
            else:
                res = res and True
            return max(l, r)
        dfs(root)
        return res
        