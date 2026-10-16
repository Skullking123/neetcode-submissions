class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        queue = deque()
        seen = set()

        for x in range(len(grid)):
            for y in range(len(grid[x])):
                queue.append((x, y))

        maxArea = 0
        while queue: # keep going until all locs are processed 
            (x, y) = queue.popleft() 
            # print(f"({x}, {y})")
            if (x, y) not in seen and grid[x][y] == 1: # process any location we haven't seen yet and is land
                area = self.numIslandsHelper(grid, (x, y), seen)
                maxArea = max(maxArea, area)
        
        return maxArea

    def numIslandsHelper(self, grid: List[List[str]], loc: (int, int), seen: set) -> int:
        queue = deque()
        queue.append(loc)
        area = 0
        while queue:
            (x, y) = queue.popleft()
            print(f"({x}, {y})")
            if grid[x][y] == 1 and (x, y) not in seen:
                area += 1
                print(area)
                if y - 1 >= 0 and (x, y - 1) not in seen:
                    queue.append((x, y - 1))
                if y + 1 < len(grid[x]) and (x, y + 1) not in seen:
                    queue.append((x, y + 1))
                if x - 1 >= 0 and (x - 1, y) not in seen:
                    queue.append((x - 1, y))
                if x + 1 < len(grid) and (x + 1, y) not in seen:
                    queue.append((x + 1, y))
            print(queue)
            seen.add((x, y))
        return area