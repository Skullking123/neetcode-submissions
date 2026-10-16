# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder - curr, left, right
        # inorder - left, curr, right
        # reconstruct the binary tree that yielded these orderings

        # in pre-order, the parent will appear before the children
        # in in-order, the parent will appear in between the children
        
        # preorder = [1,2,3,4], inorder = [2,1,3,4]
        # we iterate over pre-order
            # we take the first elm and we set that as our root.
            # then we look at the in-order and iterate through the list until we find our root.
                # the nodes we passed through are the nodes that are supposed to be in the left sub-tree of our root. This gives us the number of 
                    # nodes in the left subtree
                    # because of this, we can tell how many nodes we can skip over in the pre-order list to get to the rightsubtree
                # and the numbers that we have not, must by nodes that are in the right subtree
                # then we recurse down those sublists to make our left and right subtree by reusing this logic
        
        # first pass
        # preorder = [1,2,3,4]  inorder = [2,1,3,4]
        # root = 1, the elms to left of 1 in the in-order are [2]. There is only one element in the left subtree
        # we from 1 in the pre-order we skip 1 to skip over the left subtree elms to get its right subtree elms
        # so our recursive step would look like left = buildTree([2], []) right = buildTree([3, 4], [3, 4])
        # in the left subtree, our root would be 2, there is nothing in the inorder, so there is nothing that comes before or after 2 to give us a 
            #l eft and right subtree here
        # in the right subtree, our root would be 3, there is only a 4 on the right of our root in the inorder, thuse we know there is no left      
            # subtree and that 4 is our right subtree
        
        # print(preorder, inorder)
        index = {}
        for idx in range(len(inorder)):
            index[inorder[idx]] = idx


        # def helper(pre_idx_min, pre_idx_max, in_idx_min, in_idx_max):
            
        #     if pre_idx_min == pre_idx_max:
        #         return None
            
        #     root = preorder[pre_idx_min]

        #     left_cutoff = index[root] - in_idx_min
        #     print(f"root: {root}, {pre_idx_min} {pre_idx_max} {in_idx_min} {in_idx_max} {left_cutoff}")
        #     # print(f"root: {root}, cutoff: {left_cutoff}")
        #     # build our subtrees
        #     left = helper(pre_idx_min + 1, pre_idx_min + left_cutoff, in_idx_min, in_idx_min + left_cutoff)
        #     right = helper(left_cutoff + 1, pre_idx_max, in_idx_min + 1 + left_cutoff, in_idx_max)

        #     return TreeNode(root, left, right)

        # return helper(0, len(preorder), 0, len(inorder))

        # # Too slow, the slicing operations were too expensive


        def helper(p, l, r):
            if l > r:
                return None
            
            root = preorder[p]
            left_cutoff = index[root]            
            # print(f"root: {root} inorder range:{l} to {r} left_cutoff: {left_cutoff}")
            # print(left_cutoff)

            # build our left subtree
            left = helper(p + 1, l, left_cutoff - 1)

            # build our right subtree
            right = helper(p + left_cutoff - l + 1, left_cutoff + 1, r)

            return TreeNode(root, left, right)

        return helper(0, 0, len(inorder) - 1)
