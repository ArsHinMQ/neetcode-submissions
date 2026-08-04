# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root: Optional[TreeNode], left: float = float("-inf"), right: float = float("inf")):
            if root is None:
                return True
            if root.val <= left or root.val >= right:
                return False
            
            return dfs(root.left, left, min(root.val, right)) and dfs(root.right, max(root.val, left), right)

        return dfs(root)