class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = [set() for i in range(n + 1)]

        for a, b in edges:
            adj[a].add(b)
            adj[b].add(a)
        
        
        stack = []
        visited = set()
        def dfs(node, parent) -> bool:
            stack.append(node)
            # print(node)
            # print(visited)
            if node in visited:
                return node
            
            visited.add(node)
        
            for neighbor in adj[node]:
                if neighbor == parent:
                    continue
                
                res = dfs(neighbor, node)
                if res:
                    return res   
            
            visited.remove(node)
            stack.pop()
            return None             
        
        dfs(edges[0][0], -1)
        print(stack)
        cycle = set()
        end = stack.pop()
        prev = end

        while stack[-1] != end:
            cycle.add((prev, stack[-1]))
            prev = stack[-1]
            stack.pop()
        
        cycle.add((prev, end))

        for idx in range(n - 1, -1, -1):
            if tuple(edges[idx]) in cycle or tuple(edges[idx][::-1]) in cycle:
                return edges[idx]

        return edges[0]

        