class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[False] * n for i in range(n)]

        for src, dest in edges:
            adj[src][dest] = True
            adj[dest][src] = True
        
        visited = set()
        queue = deque()
        res = 0
        
        for node in range(n):
            # this node was alr found to be part of a component
            if node in visited:
                continue
            
            queue.append(node)

            # traverse through the component seeing which nodes make it up
            while queue:
                curr = queue.popleft()
                
                visited.add(curr)

                for neighbor in range(n):
                    # not a neighbor 
                    if not adj[curr][neighbor]:
                        continue
                    
                    queue.append(neighbor)
                    # erase this edge so we don't traverse it again
                    adj[curr][neighbor] = False
                    adj[neighbor][curr] = False
            
            res += 1

        return res