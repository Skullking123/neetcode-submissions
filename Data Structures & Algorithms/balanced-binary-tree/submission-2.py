# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        stack = [root]
        heights = {None: 0}
        seen = set()

        while stack:
            curr = stack[-1]
            
            if curr not in seen:
                seen.add(curr)
                if curr.left:
                    stack.append(curr.left)
                elif curr.right:
                    stack.append(curr.right)
                else: # we are at a leaf
                    curr = stack.pop()

                    leftH = heights[curr.left]
                    rightH = heights[curr.right]

                    if abs(leftH - rightH) > 1:
                        return False
                    
                    heights[curr] = 1 + max(leftH, rightH)
            else: # we have come back to the node 
                if curr.right and curr.right not in seen:
                    stack.append(curr.right)
                else:
                    curr = stack.pop()

                    leftH = heights[curr.left]
                    rightH = heights[curr.right]

                    if abs(leftH - rightH) > 1:
                        return False
                    
                    heights[curr] = 1 + max(leftH, rightH)


        return True
            

