from collections import deque 

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        queue = deque()
        seen = set()

        for x in range(len(grid)):
            for y in range(len(grid[x])):
                queue.append((x, y))

        islands = 0
        while queue: # keep going until all locs are processed 
            (x, y) = queue.popleft() 
            # print(f"({x}, {y})")
            if (x, y) not in seen and grid[x][y] == "1": # skip over any location we haven't seen yet and is land
                islands += 1
                self.numIslandsHelper(grid, (x, y), seen)
        
        return islands

    def numIslandsHelper(self, grid: List[List[str]], loc: (int, int), seen: set):
        queue = deque()
        queue.append(loc)
        while queue:
            (x, y) = queue.popleft()
            print(f"({x}, {y})")
            if grid[x][y] == "1" and (x, y) not in seen:
                if y - 1 >= 0:
                    queue.append((x, y - 1))
                if y + 1 < len(grid[x]):
                    queue.append((x, y + 1))
                if x - 1 >= 0:
                    queue.append((x - 1, y))
                if x + 1 < len(grid):
                    queue.append((x + 1, y))
            print(queue)
            seen.add((x, y))
        print(seen)
