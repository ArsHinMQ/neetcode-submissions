# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res, count = None, 0
        def dfs(root: Optional[TreeNode]):
            nonlocal res, count
            if root is None:
                return

            dfs(root.left)
            if res is not None:
                return
            count += 1
            if count == k:
                res = root.val
                return
            dfs(root.right)
            if res is not None:
                return

        dfs(root)
        return res

            


            

            


            
        