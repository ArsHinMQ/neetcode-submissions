# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        in_table = {val: i for i, val in enumerate(inorder)}

        pre_index = 0
        def build(in_start: int, in_end: int):
            nonlocal pre_index
            if in_start >= in_end:
                return None
            root = TreeNode(preorder[pre_index])

            pre_index += 1
            in_index = in_table[root.val]
            root.left = build(in_start, in_index)
            root.right = build(in_index + 1, in_end)
            return root
        return build(0, len(inorder))
        