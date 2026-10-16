
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        queue = deque()
        queue.append(node)
        visited = set() 

        nodes = {}

        if node == None:
            return None

        while len(queue) != 0:
            visiting = queue.pop()
            neighbors = []
            neighborVal = []

            if visiting.val not in visited:
                # print(visiting.val)
                # print(visiting.neighbors)
                visited.add(visiting.val)
            
                for neighbor in visiting.neighbors:
                    # print(neighbor.val)
                    if neighbor.val not in nodes:
                        new = Node(neighbor.val, [])
                        nodes[neighbor.val] = new
                        neighbors.append(new)

                    else:
                        neighbors.append(nodes[neighbor.val])

                    neighborVal.append(neighbor.val)
                    queue.append(neighbor)
                    
                if visiting.val in nodes:
                    nodes[visiting.val].neighbors = neighbors
                else:
                    nodes[visiting.val] = Node(visiting.val, neighbors)
                
        
        # print(nodes)
        return nodes[1]

            


            

            


