# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        lca = root

        def dfs(root: Optional[TreeNode]):
            nonlocal lca

            if root is None:
                return
            elif (root.val >= q.val and root.val <= p.val) or (root.val <= q.val and root.val >= p.val):
                lca = root
                return 
            elif root.val >= q.val and root.val >= p.val:
                lca = root
                return dfs(root.left)
            else:
                lca = root
                return dfs(root.right)

        dfs(root)
        return lca


            