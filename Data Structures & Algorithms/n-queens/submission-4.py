class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # Placing n queens on a n x n chessboard so that no two queens can attack each other
        # given an integer n, return all distinct solutions to the n-queens puzzle
        # queens are "Q" and "." is empty space

        # we could maintain a set that contains all possible coordinates that can have a queen without any conflicts
            # O(1) lookup for places to put our next queen
            # O(n) to maintain as everytime we put a queen down, we need to remove all spaces that the queen can attack, or add back all spaces when
            # we backtrack
                # There are 4 axises of attack for a queen, each len n
            # O(n^2) space complexity
        # we could just maintain a set that contains only the possible coordinates that have queens and manually calculate if a spot is free
            # O(n^2) to lookup places to put our next queen
            # O(1) to maintain since we are just adding a queen at each iteration
            # O(n) space complexity 
        
        res = []
        board = []
        queens = []
        def dfs(y):
            if y == n:
                res.append(board.copy())
                return
            # set containing all the columns that are dangerous in this row
            danger = set()
            for qx, qy in queens:
                # queens can't be in same column 
                danger.add(qx)
                offset = y - qy
                # queens can't be diagonal to each other
                danger.add(qx + offset)
                danger.add(qx - offset)   

            for x in range(n):
                if x in danger:
                    continue
                board.append(("." * x) + "Q" + ("." * (n - x - 1)))
                queens.append((x, y))
                dfs(y + 1)
                board.pop()
                queens.pop()
        
        dfs(0)
        return res

















