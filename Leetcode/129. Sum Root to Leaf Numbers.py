# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Iterative DFS
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = [(root,0)]
        totalsum = 0
        while len(stack) > 0:
            root,currentsum = stack.pop()
            currentsum = currentsum*10 + root.val
            if not root.right and not root.left:
                totalsum += currentsum
            if root.right:
                stack.append((root.right,currentsum))
            if root.left:
                stack.append((root.left,currentsum))
        return totalsum
        
# Recursive
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def sum(root,currentsum):
            if not root:
                return 0
            currentsum = currentsum*10 + root.val
            if not root.left and not root.right:
                return currentsum
            x = sum(root.left,currentsum)
            y = sum(root.right,currentsum)
            return x+y
        return sum(root,0)
