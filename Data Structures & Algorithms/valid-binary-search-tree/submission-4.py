# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def validHelper(root: Optional[TreeNode], relMin: int, relMax: int) -> bool:
            if root is None:
                return True
            
            if root.val <= relMin:
                return False
            elif root.val >= relMax:
                return False
            else:
                return validHelper(root.left, relMin, root.val) and validHelper(root.right, root.val, relMax)
        
        return validHelper(root, float('-inf'), float('inf'))