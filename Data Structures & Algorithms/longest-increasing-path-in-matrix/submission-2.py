class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = [[-1] * len(matrix[0]) for _ in range(len(matrix))]

        def dfs(x, y):
            
            # don't recompute
            if dp[y][x] != -1:
                return dp[y][x]
            
            # try to make the longest increasing path by appending this cord to a neighbor's longest path
            dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            longestNeighborPath = 0
            for nx, ny in dirs:
                # bounds check
                if x + nx < 0 or x + nx >= len(matrix[0]) or y + ny < 0 or y + ny >= len(matrix):
                    continue
                
                # only traverse to cords that have a value greater than us
                if matrix[y + ny][x + nx] > matrix[y][x]:
                    longestNeighborPath = max(longestNeighborPath, dfs(x + nx, y + ny))

            dp[y][x] = longestNeighborPath + 1
            return dp[y][x]
        
        res = 0
        for y in range(len(matrix)):
            for x in range(len(matrix[0])):
                res = max(res, dfs(x, y))

        # for row in dp:
        #     print(row)
        return res