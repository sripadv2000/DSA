# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:

        def solve(node, current):
            if not node:
                return 0
            # Build binary number
            current = (2*current) + node.val;
            # If leaf node
            if node.left == None and node.right == None:
                return current
            # Return sum of left and right subtree
            return solve(node.left, current) + solve(node.right, current)
        
        return solve(root, 0)