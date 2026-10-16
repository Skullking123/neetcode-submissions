
# Definition for a QuadTree node.
class Node:
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        # Given an n * n matrix grid of 0's and 1's, construct a quad-tree
        # Then return the root of the quad-tree presenting grid

        # A quad-tree is a tree data structure where every node has four children.
        # Each node has two attributes
            # val: True if the node represents a grid of 1's or False if the node represents a grid of 0's
            # isLeaf: True if the node is a leaf node on the tree or False if the node has four
        
        # Each step split the grid into four quandrants 
        # The return val is the root of the resulting tree
        # Base Case: If our grid is a 1 x 1, create a new node with the val isLeaf set to true and val set 
        # to what it needs to be
        # Recursive Case: split the grid into four quandrants and recurse on those four making quad-trees for each of them
        # If all the children the same val set this one to a leaf as well with the same val
        # Otherwise, just set val and save the children and return the root

        # parms are the inclsuive bounds of our grid. Representing the four bounds of our grid
        # O(4^x * n^2)
        # Where x is 2^x = n for an n x n grid
        def quadTree(top, bot, left, right) -> Node:
            # print(top, bot, left, right)
            height = bot - top + 1
            width = right - left + 1
            # if our grid is a 1 x 1. Return a leaf
            if height == 1 and width == 1:
                val = True if grid[top][right] == 1 else False
                return Node(val, True)
            
            topLeft = quadTree(top, bot - (height // 2), left, right - (width // 2))
            topRight = quadTree(top, bot - (height // 2), left + (width // 2), right)
            botLeft = quadTree(top + (height // 2), bot, left, right - (width // 2))
            botRight = quadTree(top + (height // 2), bot, left + (width // 2), right)
            # if all the children have the same val, create a leaf
            all_are_leaves = topLeft.isLeaf == topRight.isLeaf == botLeft.isLeaf == botRight.isLeaf == True
            if all_are_leaves and topLeft.val == topRight.val == botLeft.val == botRight.val:
                return Node(topLeft.val, True)
            else: # otherwise create a new root with its children
                # if the grid has different values, set val to whatever val
                return Node(False, False, topLeft, topRight, botLeft, botRight)
            
        return quadTree(0, len(grid) - 1, 0, len(grid[0]) - 1)




















