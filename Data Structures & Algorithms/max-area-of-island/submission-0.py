class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        visited = set()
        
        def bfs(x: int, y: int) -> int:
            queue = deque()
            queue.append((x,y))
            area = 0
            while len(queue) != 0:
                (qx, qy) = queue.pop()

                
                print(qx, qy)

                if (qx, qy) not in visited and grid[qy][qx] == 1:
                    visited.add((qx, qy))
                    area += 1

                    if qx + 1 in range(len(grid[0])):
                        queue.append((qx + 1, qy))
                    
                    if qx -1 in range(len(grid[0])):
                        queue.append((qx - 1, qy))
                
                    if qy + 1 in range(len(grid)):
                        queue.append((qx, qy + 1))

                    if qy - 1 in range(len(grid)):
                        queue.append((qx, qy - 1))
            return area


        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if (x,y) not in visited and grid[y][x] == 1:
                    maxArea = max(bfs(x,y), maxArea)
        
        return maxArea