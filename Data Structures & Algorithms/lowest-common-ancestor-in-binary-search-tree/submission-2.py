# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(root: Optional[TreeNode]):
            if root is None:
                return
            elif (root.val >= q.val and root.val <= p.val) or (root.val <= q.val and root.val >= p.val):
                return root
            elif root.val >= q.val and root.val >= p.val:
                return dfs(root.left)
            else:
                return dfs(root.right)

        return dfs(root)


            