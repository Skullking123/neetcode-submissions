# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        serial = ""
        queue = collections.deque()
        queue.append(root)
        if root is None:
            return ""
        while queue:
            curr = queue.popleft()
            left = ""
            right = ""
            if curr.left:
                left = f"{curr.left.val}" 
                queue.append(curr.left)
            if curr.right:
                right = f"{curr.right.val}"
                queue.append(curr.right)
            
            serial += f"({curr.val},{left},{right})"

        return serial
            
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        print(data)
        root = None
        ptr = 0
        nodes = {}
        if data == "":
            return None
        
        while ptr < len(data):
            ptr += 1 # move ptr past (
            val = ""
            while data[ptr].isnumeric():
                val += data[ptr]
                ptr += 1
            print(val)

            ptr += 1 # move past the , delimiter to the left value
            left = ""
            while data[ptr].isnumeric():
                left += data[ptr]
                ptr += 1
            
            ptr += 1 # move past the , delimiter to the right value
            right = ""
            while data[ptr].isnumeric():
                right += data[ptr]
                ptr += 1
            
            ptr += 1 # move past the ) so ptr points at the next node to be deserialize
            
            leftNode = None
            if left.isnumeric():
                leftNode = TreeNode(int(left))
                nodes[left] = leftNode
            rightNode = None
            if right.isnumeric():
                rightNode = TreeNode(int(right))
                nodes[right] = rightNode
            currNode = nodes.get(val, TreeNode(0))
            currNode.val = val
            currNode.left = leftNode
            currNode.right = rightNode
            nodes[val] = currNode

            if root is None: # the very first node in the serial str is the root, so if root is None. That means we have haven't processed a node yet
                root = currNode
        
        return root
            