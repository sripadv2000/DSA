# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def preorder(node):
            if not node:
                return "null"
            
            # ^ is used as a separator to avoid false matches like 12 matching 2
            return "^" + str(node.val) + preorder(node.left) + preorder(node.right)
        
        full_tree = preorder(root)
        sub_tree = preorder(subRoot)
        
        return sub_tree in full_tree