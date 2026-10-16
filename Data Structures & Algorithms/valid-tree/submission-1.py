class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # given n nodes label from 0 to n - 1 and a list of undirected edges, reutnr true if it is a valid tree, false otherwise

        # preprocess the list of edges into an adj matrix
        adj = [[False] * n for i in range(n)]
        for src, dest in edges:
            # the edges are undirected
            adj[src][dest] = True
            adj[dest][src] = True


        # prep for bfs
        visited = set()
        queue = deque()
        queue.append(0)

        while queue:
            curr = queue.popleft()

            # there is a cycle 
            if curr in visited:
                return False
            
            visited.add(curr)

            for neighbor in range(n):
                # not a neighbor 
                if not adj[curr][neighbor]:
                    continue
                
                queue.append(neighbor)
                # erase this edge so we don't traverse it again
                adj[curr][neighbor] = False
                adj[neighbor][curr] = False

        return len(visited) == n

