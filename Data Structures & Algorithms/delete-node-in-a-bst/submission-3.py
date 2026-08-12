# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return root
        
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
            return root

        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
            return root

        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        replacement = root.right
        while replacement.left:
            replacement = replacement.left
        root.val = replacement.val
        root.right = self.deleteNode(root.right, root.val)
        return root
            
        