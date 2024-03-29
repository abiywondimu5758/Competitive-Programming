"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        arr = []
        def postorder(root):
            if root is None: return None
            for i in root.children:
                postorder(i)
            arr.append(root.val)
        postorder(root)
        return arr
        
