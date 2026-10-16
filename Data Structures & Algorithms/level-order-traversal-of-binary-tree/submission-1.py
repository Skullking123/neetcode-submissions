# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # given a binary tree root, return the level order traversal of it as a nested list
        
        if not root:
            return []

        # just do a layer-by-layer bfs
        queue = deque()
        queue.append(root)
        res = []
        while queue:
            layer = len(queue)
            elms = []
            for _ in range(layer):
                curr = queue.popleft()

                if curr.left:
                    queue.append(curr.left)
                
                if curr.right:
                    queue.append(curr.right)

                elms.append(curr.val)
            
            res.append(elms)
        
        return res
