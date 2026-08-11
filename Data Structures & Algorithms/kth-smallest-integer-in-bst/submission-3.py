# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(root: Optional[TreeNode]):
            nonlocal k
            if root is None:
                return

            res = dfs(root.left)
            if res is not None:
                return res
            
            if k == 1:
                return root.val
            k -= 1

            res = dfs(root.right)
            if res is not None:
                return res

            return None

        return dfs(root)
            


        
        