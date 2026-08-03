# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:   
        def compare_trees(a: Optional[TreeNode], b: Optional[TreeNode]):
            if a is None and b is None:
                return True
            elif a is None or b is None:
                return False
            elif a.val != b.val:
                return False
            return compare_trees(a.left, b.left) and compare_trees(a.right, b.right)

        def find_sub_tree_root(root: Optional[TreeNode]):
            if root is None:
                return False
            elif root.val == subRoot.val:
                if compare_trees(root, subRoot):
                    return True

            return find_sub_tree_root(root.left) or find_sub_tree_root(root.right)

        return find_sub_tree_root(root)
        


                
        