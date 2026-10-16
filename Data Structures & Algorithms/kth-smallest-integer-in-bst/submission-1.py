# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.elms = []

        def traverseInOrder(root: Optional[TreeNode], k: int):
            if root.left:
                traverseInOrder(root.left, k)
            
            if len(self.elms) == k:
                return 
            
            self.elms.append(root.val)

            if len(self.elms) == k:
                return 
            
            if root.right:
                traverseInOrder(root.right, k)
            
            # if len(self.elms) == k:
            #     return
            
        traverseInOrder(root, k)
        return self.elms[-1]