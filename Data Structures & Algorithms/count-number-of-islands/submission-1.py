class Solution:

         

    def numIslands(self, grid: List[List[str]]) -> int:
        islandCords = set()
        numIslands = 0

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if ((x, y) not in islandCords and grid[y][x] == "1"):
                    numIslands += 1
                    self.getIslandCords(grid, x, y, islandCords)
        
        return numIslands

    def getIslandCords(self, grid: List[List[str]], x: int, y: int, cords: set):
        if (grid[y][x] == "1"and (x, y) not in cords):
            cords.add((x, y))
            print((x,y))
            if (x - 1 >= 0):
                self.getIslandCords(grid, x - 1, y, cords)
            
            if (x + 1 < len(grid[0])):
                self.getIslandCords(grid, x + 1, y, cords)

            if (y - 1 >= 0):
                self.getIslandCords(grid, x, y - 1, cords)

            if (y + 1 < len(grid)):
                self.getIslandCords(grid, x, y + 1, cords)   




    