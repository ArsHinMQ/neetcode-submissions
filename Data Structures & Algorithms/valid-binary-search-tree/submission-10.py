# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: TreeNode = root, left: int | float = float("-inf"), right: int | float = float("inf")):
            if node is None:
                return True
            if left < node.val < right:
                return dfs(node.left, left, node.val) and dfs(node.right, node.val, right)
            return False
        return dfs()
        