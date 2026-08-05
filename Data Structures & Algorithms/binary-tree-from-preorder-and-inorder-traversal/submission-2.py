# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        in_table = {val: i for i, val in enumerate(inorder)}
        pre_idx = 0
        def build(in_start: int, in_end: int):
            nonlocal pre_idx
            if in_start > in_end:
                return

            root = TreeNode(preorder[pre_idx])
            index = in_table[preorder[pre_idx]]
            pre_idx += 1

            root.left = build(in_start, index -1)
            root.right = build(index+1, in_end)

            return root

        return build(0, len(inorder)-1)


            