# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True        
        queue = [root]
        null_seen = False
        while queue:
            node = queue.pop(0)
            if not node:
                null_seen = True
            else:
                if null_seen:
                    return False
                queue.extend([node.left,node.right])
        return True
