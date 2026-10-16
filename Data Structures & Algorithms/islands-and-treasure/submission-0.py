class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # The grid is m x n
        # -1 = Water
        # 0 = Treasure chest
        # INF = Land
        # Need to return a grid where each cell is the distance to the nearest treasure
        # Looking for "nearest" so need bfs
        # Run bfs from treasure
        
        # find the treasure
        treasure = []
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] == 0:
                    treasure.append((x, y))
        
        # do bfs from each treasure
        queue = deque(treasure)
        adj = [(1,0), (-1, 0), (0, 1), (0, -1)]
        while queue:
            
            # get curr
            (x, y) = queue.popleft()
            
            # go to adj
            for adjx, adjy in adj:
                nx = x + adjx
                ny = y + adjy
                # bounds check
                print(nx, ny)
                if nx < 0 or nx > len(grid[0]) - 1 or ny < 0 or ny > len(grid) - 1:
                    continue
                # don't process water
                if grid[ny][nx] == -1:
                    continue
                # don't traverse to adj where we can't do better
                if grid[ny][nx] < grid[y][x] + 1:
                    continue

                grid[ny][nx] = grid[y][x] + 1
                queue.append((nx, ny))
        
        