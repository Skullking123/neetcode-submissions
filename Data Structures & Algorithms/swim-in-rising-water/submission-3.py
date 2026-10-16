class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # given a square 2-D matrix of distinct integers grid, where each integer grid[i][j] represents the 
        # elevation at position (i, j).
        # Rain starts to fall at time = 0, which causes the water level to rise. At time t, the water level across the entire grid is t.
        # You can either swim horizontally or vertically in the grid between two adjacent squares if the original elevation of both
        # squares is less than or equal to the water level at time t.
        # Starting from the top left square (0, 0), return the amount of time it will take until it is possible to reach the bottom right square 
        # (n - 1, n - 1)
        

        # Shortest path from (0, 0) to another point? Dijkstra alg
        # We start at (0, 0) 
        # For every cord that we are at we compute shortest dist of every neighbor that we haven't visited that we can reach
            # dist[neighbor] = max(grid[cord], grid[neighbor]) 
            # then set the next cord to be the neighbor that we haven't visited yet that has the shortest dist
        # return dist[(n-1, n-1)]

        n = len(grid)
        heap = []
        visited = set()
        dist = [[float('inf')] * n for i in range(n)]

        dist[0][0] = grid[0][0]
        # start dijkstras at (0, 0)
        heapq.heappush(heap, (0, 0, 0))

        while heap:
            
            _, cx, cy = heapq.heappop(heap)

            
            # don't revisit cords that we have alr found shortest dists for
            if (cx, cy) in visited:
                continue
            
            # visit only nodes that haven't been visited yet and have shortest dist
            # mark this cord as visited
            visited.add((cx, cy))

            # compute the dist for the neighbors of this cord         
            dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for nx, ny in dirs:
                # bounds check
                if cx + nx < 0 or cx + nx >= n or cy + ny < 0 or cy + ny >= n:
                    continue  
                # don't recompute shortest dists for cords we have alr done
                if (cx + nx, cy + ny) in visited:
                    continue
                # path created using this cord
                path = max(dist[cy][cx], grid[cy + ny][cx + nx])
                # save only the shortest path that we have thus far made 
                dist[cy + ny][cx + nx] = min(dist[cy + ny][cx + nx], path)
                
                heapq.heappush(heap, (dist[cy + ny][cx + nx], cx + nx, cy + ny))
        
        for row in dist:
            print(row)
        return dist[-1][-1]

        # This method doesn't work because in order to determine a cell, we would need to know all 4 directions. We would 
        # not have all the required information needed to calculate each cell at the time we traverse to a cell 
        # maintain a 2d dp arr where dp[i][j] = minimum amount of time it will take to reach (i, j) from (0, 0)
        # Start a bfs at (0, 0)
        # At every cell (i, j), we take the max(grid[i][j], dp[i - 1][j], dp[i][j - 1])
        # Then return dp[-1][-1]


        # dp = [[0] * n for i in range(n)]
        
        
        # return dp[-1][-1]