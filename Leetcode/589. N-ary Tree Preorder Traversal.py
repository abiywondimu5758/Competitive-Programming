"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        arr = []
        def postorder(root):
            nonlocal arr
            if not root: return None
            arr.append(root.val)
            for i in root.children:
                postorder(i)
        postorder(root)
        return arr
        
