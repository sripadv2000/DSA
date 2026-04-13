# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        d = deque()
        depth = 0
        d.append(root)

        while d:
            depth += 1
            levelSize = len(d)
            for i in range(0, levelSize):
                curr = d.popleft()
                if curr.left != None:
                    d.append(curr.left)
                if curr.right != None:
                    d.append(curr.right)
        return depth