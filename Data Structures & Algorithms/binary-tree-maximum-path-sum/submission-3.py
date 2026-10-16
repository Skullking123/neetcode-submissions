# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        stack = []
        stack.append(root)
        pSums = {}
        pSums[None] = 0
        res = root.val
        seen = set()
        while stack:
            curr = stack[-1]
            if curr.left and curr.left not in seen:
                stack.append(curr.left)
                continue
            if curr.right and curr.right not in seen:
                stack.append(curr.right)
                continue
            seen.add(curr)
            pSums[curr] = max(curr.val, curr.val + pSums[curr.left], curr.val + pSums[curr.right])
            res = max(res, pSums[curr], pSums[curr.left] + curr.val + pSums[curr.right])
            stack.pop()
        return res