class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # top and left side are pacfic
        # bot and right side are atlantic
        # Return as a 2D list where each list is a cell where water can flow to both Pacific and Atlantic 
            # each elm is form [r, c] where r is row and c is col
        # water can flow to adj as long as the adj cell has height equal or lower

        # Probably use dfs to traverse down paths
        # Use a set to keep track of cells can traverse to atlantic and pacific
        # If from a cell while dfs, we are able to traverse to a cell that we already found out has a path to atlantic and pacific
            # then all the cells leading up to that cell is valid and return
        # If the grid is m x n, the run time of this would be O(m * n * m * n) since we're going to be doing a dfs at every cell

        # Maybe instead we gather all the cells that the atlantic and pacific cells can revieve water from.
            # instead of checking if the water has height equal or lower, we check if the height is strictly greater
        # Then union the two sets to get the cells that both atlantic and pacific cells can recieve water from to get all
        # the cells that can flow water to both 
        # probably use bfs
        # as we're finding cells, don't revisit cells that we have already reached
        
        atlantic = set()
        pacific = set()
        def bfs(r: int, c: int, ocean: set):
            seen = set()
            queue = deque()
            queue.append((r, c))
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            ocean.add((r, c))
            seen.add((r, c))
            while queue:
                cr, cc = queue.popleft()
                
                for rDir, cDir in directions:
                    nr = cr + rDir
                    nc = cc + cDir
                    # boundary check
                    if nr < 0 or nr > len(heights) - 1 or nc < 0 or nc > len(heights[0]) - 1:
                        continue
                    # don't revisit
                    if (nr, nc) in seen or (nr, nc) in ocean:
                        continue
                    seen.add((nr, nc))
                    # visit it
                    if heights[nr][nc] >= heights[cr][cc]:
                        ocean.add((nr, nc))
                        queue.append((nr, nc))
        
        # process atlantic 
        # bottom row
        for c in range(len(heights[0])):
            bfs(len(heights) - 1, c, atlantic)
        # right col
        for r in range(len(heights)):
            bfs(r, len(heights[0]) - 1, atlantic)

        # process pacific
        # top row
        for c in range(len(heights[0])):
            bfs(0, c, pacific)
        # left col
        for r in range(len(heights)):
            bfs(r, 0, pacific)
        print(pacific)
        print(atlantic)
        # union the sets
        res = []
        for cord in atlantic:
            if cord in pacific:
                res.append([cord[0], cord[1]])
        
        return res
        


