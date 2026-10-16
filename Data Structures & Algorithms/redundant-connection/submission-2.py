class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = [set() for i in range(n + 1)]

        
        cycle = set()
        def dfs(node, parent) -> bool:
            if node in cycle:
                return True
            
            cycle.add(node)
        
            for neighbor in adj[node]:
                if neighbor == parent:
                    continue

                if dfs(neighbor, node):
                    return True            
            
            cycle.remove(node)
            return False                    
        
        for idx in range(n):
            a, b = edges[idx]
            adj[a].add(b)
            adj[b].add(a)

            if dfs(a, b):
                return [a, b]
            cycle = set()

        return edges[0]

        