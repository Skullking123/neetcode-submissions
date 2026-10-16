# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def goodNodesHelper(root: TreeNode, relMax: int) -> int:
            if root == None:
                return 0

            if root.val >= relMax:
                return 1 + goodNodesHelper(root.right, root.val) + goodNodesHelper(root.left, root.val)
            else:
                return goodNodesHelper(root.right, relMax) + goodNodesHelper(root.left, relMax)
        
        return goodNodesHelper(root, float("-inf"))