# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        res = 0
        stack = [root]
        seen = set()
        relDepth = 1
        while stack:

            curr = stack[-1]
            if curr not in seen:
                seen.add(curr)
                if curr.left:
                    stack.append(curr.left)
                    relDepth += 1
                elif curr.right:
                    stack.append(curr.right)
                    relDepth += 1
                else:
                    res = max(res, relDepth)
                    stack.pop()
                    relDepth -= 1
            else: # we have just came back to curr either
                if curr.right and curr.right not in seen:
                    stack.append(curr.right)
                    relDepth += 1
                else:
                    res = max(res, relDepth)
                    stack.pop()
                    relDepth -= 1
    
        return res
                

