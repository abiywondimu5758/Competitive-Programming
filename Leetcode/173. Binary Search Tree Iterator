# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.stack = []
        self.inorder(self.root)

    def hasNext(self) -> bool:
        return len(self.stack)>0
        
    def next(self) :
        self.root = self.stack.pop()
        self.inorder(self.root.right)
        return self.root.val

    def inorder(self,root):
        while root:
            self.stack.append(root)
            root = root.left


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
