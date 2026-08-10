# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        data = []
        def dfs(root: Optional[TreeNode]):
            if root is None:
                return
            dfs(root.left)
            data.append(root.val)
            dfs(root.right)
        dfs(root)
        return data
        