# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Given the root of a binary tree, return the inorder traversal of its nodes' values

        res = []

        # Runtime: O(n)
        # Space: O(lg(n)) or whatever the height of the tree is
        # Space: O(n + lg(n)) if we include the memory for the output
        def helper(root):

            if root is None:
                return 

            helper(root.left)
            res.append(root.val)
            helper(root.right)

        helper(root)

        return res