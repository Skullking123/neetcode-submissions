class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Given an m xx n grid where you are allowed to move either down or to the
        # right at any point in time
        # Given m and n, return the number of possible unique paths that can be taken from the top-left corner to
        # the bottom-right corner (grid[m - 1][n - 1])

        # We can approach this from a top-down dynamic programming approach
        # Create a m x n grid for our dp, filled with 0s
        # grid[y][x] = # of unique paths to reach (x, y) starting from (0, 0)
        # We do bfs through the entire grid starting at (0, 0) 
            # At every cell (x, y) we reach, we calculate grid[y][x] to be the sum of:
                # the number of unqiue paths that reach the cell above
                # the number of unique paths that reach the cell to the left
        # return grid[m - 1][n - 1]
        
        if m == 1 and n == 1:
            return 1


        prev = defaultdict(lambda : 0)
        prev[(0, 0)] = 1
        queue = deque()
        queue.append((1, 0))
        queue.append((0, 1))
        
        while queue:
            
            layer = len(queue)
            curr = defaultdict(lambda: 0)
            for _ in range(layer):

                x, y = queue.popleft()

                # bounds check:
                # don't do repetitive work
                if (x, y) in curr:
                    continue
                # compute this cell's number of unique paths from the start
                curr[(x, y)] = prev[(x - 1, y)] + prev[(x, y - 1)] # top + left

                # append neighbors to queue
                dirs = [(1, 0), (0, 1)]
                for nx, ny in dirs:
                    if x + nx < 0 or x + nx >= n or y + ny < 0 or y + ny >= m:
                        continue
                    queue.append((x + nx, y + ny))
            prev = curr
            # print(prev)
        return prev[(n - 1, m - 1)]














        grid =[[0] * n for i in range(m)]
        # base case
        grid[0][0] = 1
        
        # start our bfs with the neighbors of our start 
        queue = deque()
        queue.append((1, 0))
        queue.append((0, 1))
        
        while queue:
            
            x, y = queue.popleft()

            # bounds check
            if x < 0 or x >= n or y < 0 or y >= m:
                continue
            # we visited this cell alr
            if grid[y][x] != 0:
                continue


            # compute grid[y][x]
            top = 0
            if y - 1 >= 0:
                top = grid[y - 1][x]
            left = 0
            if x - 1 >= 0:
                left = grid[y][x - 1]
            grid[y][x] = top + left

            # add neighbors to queue
            dirs = [(1, 0), (0, 1)]
            for nx, ny in dirs:
                queue.append((x + nx, y + ny))
        
        return grid[m - 1][n - 1]


