# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        def build_tree(root: TreeNode, preorder: List[int], inorder: List[int]):
            if root is None or len(inorder) <= 1:
                return

            index = None
            for i, n in enumerate(inorder):
                if n == root.val:
                    index = i
                    break

            left_inorder = inorder[:index]
            right_inorder = inorder[index+1:]

            left_preorder = preorder[1:index+1]
            right_preorder = preorder[index+1:]

            root.left = TreeNode(left_preorder[0]) if left_preorder else None
            build_tree(root.left, left_preorder, left_inorder)

            root.right = TreeNode(right_preorder[0]) if right_preorder else None
            build_tree(root.right, right_preorder, right_inorder)

        build_tree(root, preorder, inorder)
        return root




        