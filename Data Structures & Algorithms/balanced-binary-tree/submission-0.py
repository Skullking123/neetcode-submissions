# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(curr: Optional[TreeNode]) -> (int, bool):
            if curr is None:
                return (0, True)
            
            leftH, leftB = dfs(curr.left)
            rightH, rightB = dfs(curr.right)

            if not leftB or not rightB:
                return (0, False)
            
            if abs(rightH - leftH) > 1:
                return (0, False)
            
            return (max(leftH, rightH) + 1, True)

        return dfs(root)[1]

            

