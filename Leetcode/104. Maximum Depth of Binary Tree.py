# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Iterative
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = [(root,1)]
        maxDepth = 0
        while stack:
            root, depth = stack.pop()
            maxDepth = max(x,depth)
            if root.left:
                stack.append((root.left,depth + 1))
            if root.right:
                stack.append((root.right,depth + 1))
        return maxDepth

# Recursive
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def md(root):
            if not root:
                return 0
            left = md(root.left)
            right = md(root.right)
            return max(left,right) + 1
        return md(root)
