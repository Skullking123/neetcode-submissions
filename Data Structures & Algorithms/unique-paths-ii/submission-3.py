class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # Given an m x n integer arr grid. There is a robot initially located at the top-left corner
        # The robot tries to move to the bottom-right corner
        # The robot can only move either down or right at any point in time
        # An obstacle and space are marked as 1 or 0 respectively in the grid
        # A path that the robot takes cannot include any obstacles (1)
        # Return the number of possible unique paths that the robot can take to reach the bottom-right corner

        # start bfs from (0, 0)
        # Since the robot can only move down or right, it means
        # that in order for a robot to reach a square [x, y], it must have
            # previously came from either the square above it or to its left
            # thus the number of paths to reach [x, y] is the sum of:
                # number of  paths to reach [x - 1, y]
                # number of paths to reach [x, y - 1]
        
        # Since we for each grid square we only need the square to the left and above it
        # Then we can essentially just memorize the previous diagonal to then process the next

        # previous diagonal
        prev = defaultdict(int)
        queue = deque()
        queue.append((0, 0))

        ndirs = [(1, 0), (0, 1)]

        while queue:    
            curr = defaultdict(int)
            # process layer-by-layer
            # this allows us to distinguish between the diagonals since
            # we only care about the current diagonal and the previous diagonal
            # allowing us to cut down on memory 
            print("iteration")
            for _ in range(len(queue)):
                cx, cy = queue.popleft()

                # we ignore obstacles (the 1s)
                if obstacleGrid[cy][cx]:
                    # this also adds the added property that 
                    # any grid obstacle square will end up with the default value of 0 paths possible
                    continue
                # don't recompute
                if (cx, cy) in curr:
                    continue
                    
                # compute the grid square
                # if the left or above are obstacles, then prev[neighborY][neighborX] will be 0 
                # and effectively be ignored
                curr[(cx, cy)] = prev[(cx - 1, cy)] + prev[(cx, cy - 1)] if (cx, cy) != (0, 0) else 1
                
                for nx, ny in ndirs:
                    # bounds check
                    if cx + nx < 0 or cx + nx >= len(obstacleGrid[0]) or cy + ny < 0 or cy + ny >= len(obstacleGrid):
                        continue
                    queue.append((cx + nx, cy + ny))
            
            # save the previous diagonal
            prev = curr
        print(prev)
        return prev[(len(obstacleGrid[0]) - 1, len(obstacleGrid) - 1)]

















