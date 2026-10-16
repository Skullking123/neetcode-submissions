from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if (not q and p) or (q and not p): # one root can't be None when the other isn't
            return False
        
        pQueue = deque()
        qQueue = deque()

        pQueue.append(p)
        qQueue.append(q)

        while pQueue or qQueue:
            pCurr = pQueue.popleft()
            qCurr = qQueue.popleft()

            if (not pCurr and qCurr) or (pCurr and not qCurr):
                return False
            elif not pCurr and not qCurr: # both empty
                continue
            
            if pCurr.val != qCurr.val:
                return False
            
            pQueue.append(pCurr.left)
            pQueue.append(pCurr.right)
            qQueue.append(qCurr.left)
            qQueue.append(qCurr.right)

            
        return True

            