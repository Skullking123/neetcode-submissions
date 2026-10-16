class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Return the minimum number of minutes for all fruits to start rotting
        # If impossible, return -1
        # A fresh fruit rots when it is adjacent to a rotten fruit
        # 0 represents an empty cell
        # 1 represents a fresh fruit
        # 2 represents a rotten fruit

        # rotting spreads to adjacents, so use bfs
        # bfs from rotten fruits
        # need to keep track of remaining fresh fruits to see if any are left at the end
        # we end when we can't reach anymore fresh fruits
        # will need to iterate minute by minute to keep track of minutes

        # get all fresh and rotten fruits
        fresh = 0
        rotten = deque()
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 1:
                    fresh += 1
                elif grid[y][x] == 2:
                    rotten.append((x, y))
        
        if fresh == 0:
            return 0

        # start at -1 because we are starting at already rotting fruits
        minutes = -1 
        # do multi-soruce bfs
        queue = rotten
        seen = set(rotten)
        adj = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while queue:
            minutes += 1
            print(minutes)
            print(queue)
            for _ in range(len(queue)):
                (x, y) = queue.popleft()
                # process adj
                for adjx, adjy in adj:
                    nx = x + adjx
                    ny = y + adjy
                    # bounds check
                    if nx < 0 or nx > len(grid[0]) - 1 or ny < 0 or ny > len(grid) - 1:
                        continue
                    if (nx, ny) in seen:
                        continue
                    if grid[ny][nx] == 0:
                        continue
                    fresh -= 1
                    seen.add((nx, ny))
                    queue.append((nx, ny))
        
        if fresh == 0:
            return minutes
        else:
            return -1
