from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        queue = deque()
        queue.append(root)
        
        while queue:
            curr = queue.popleft()

            if curr is None:
                continue
            
            queue.append(curr.left)
            queue.append(curr.right)

            temp = curr.left
            curr.left = curr.right
            curr.right = temp
        
        return root 

