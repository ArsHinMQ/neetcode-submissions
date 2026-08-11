# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def dfs(root: Optional[TreeNode]):
            if root.val > val:
                if root.left is None:
                    root.left = TreeNode(val)
                    return
                dfs(root.left)
            else:
                if root.right is None:
                    root.right = TreeNode(val)
                    return
                dfs(root.right)

        if root is None:
            return TreeNode(val)
        dfs(root)
        return root


        