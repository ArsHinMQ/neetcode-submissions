# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float("-inf")

        def dfs(node: TreeNode):
            nonlocal max_sum
            if node is None:
                return 0

            l = dfs(node.left)
            r = dfs(node.right)
            res = max(node.val + l, node.val + r, node.val)
            max_sum = max(max_sum, l + r + node.val, res)
            return res

        dfs(root)
        return max_sum