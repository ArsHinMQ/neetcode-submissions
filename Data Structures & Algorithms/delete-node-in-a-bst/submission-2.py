# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def find_node(node: Optional[TreeNode], parent: Optional[TreeNode] = None):
            if node is None:
                return None, parent
            elif node.val == key:
                return node, parent
            elif node.val > key:
                return find_node(node.left, node)
            else:
                return find_node(node.right, node)
            

        node, parent = find_node(root)
        if node is None:
            return root

        if node.right:
            node.val = node.right.val
            if node.right.left:
                original_left = node.left
                node.left = node.right.left
                leftmost = node.left
                while leftmost.left:
                    leftmost = leftmost.left
                leftmost.left = original_left
            node.right = node.right.right
        elif node.left:
            node.val = node.left.val
            node.right = node.left.right
            node.left = node.left.left
        elif parent:
            if parent.val > key:
                parent.left = None
            else:
                parent.right = None
        else:
            root = None

        return root



        
        