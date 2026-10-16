# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.lowestLvl = float('-inf')
        self.commonAncestor = root

        self.lowestCommonAncestorHelper(root, p, q, 0)
        return self.commonAncestor

    def lowestCommonAncestorHelper(self, root: TreeNode, p: TreeNode, q: TreeNode, level: int):
        if root is None:
            return
        
        if self.hasBoth(root, p, q):
            if level > self.lowestLvl:
                self.lowestLvl = level
                self.commonAncestor = root

            self.lowestCommonAncestorHelper(root.left, p, q, level + 1)
            self.lowestCommonAncestorHelper(root.right, p, q, level + 1)
            
        else:
            return 

    def hasBoth(self, root: TreeNode, p: TreeNode, q: TreeNode) -> bool:
        return self.has(root, p) and self.has(root, q)

    def has(self, root: TreeNode, node: TreeNode) -> bool:
        if root is None:
            return False
        elif root.val == node.val:
            return True
        elif node.val < root.val:
            return self.has(root.left, node)
        else: # node.val > root.val
            return self.has(root.right, node)



    