class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [set() for i in range(n)]

        for src, dest in edges:
            adj[src].add(dest)
            adj[dest].add(src)
        
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

                for neighbor in adj[curr]:        

                    if neighbor in visited:
                        continue
                                    
                    queue.append(neighbor)

            
            res += 1

        return res