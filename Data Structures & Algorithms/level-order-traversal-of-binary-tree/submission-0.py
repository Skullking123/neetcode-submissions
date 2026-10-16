# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.res = {}

        def levelHelper(root: Optional[TreeNode], level: int):
            if root != None:
                if level not in self.res:
                    self.res[level] = []
                self.res[level].append(root.val)
                levelHelper(root.left, level + 1)
                levelHelper(root.right, level + 1)
        
        levelHelper(root, 0)
        return list(self.res.values())