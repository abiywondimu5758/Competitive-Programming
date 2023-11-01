# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Iterative
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = [(root,1)]
        minDepth = float('inf')
        while stack:
            root, depth = stack.pop()
            if not root.left and not root.right:
                minDepth = min(minDepth,depth)
            if root.left:
                stack.append((root.left,depth + 1))
            if root.right:
                stack.append((root.right,depth + 1))
        return minDepth 

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def md(root):
            if not root:
                return 0
            left = md(root.left)
            right = md(root.right)
            if not left or not right:
                return max(left, right) + 1
            return min(left,right) + 1
        return md(root)
