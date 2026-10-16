class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # Given an m x n matrix of integers matrix
        # If an elm is 0, set its entire row and column to 0's
        # Update the matrix in-place
        
        # maintain two sets for rows and cols
        # We can scan the entire matrix looking for 0s
        # Whenever we find a zero, we store its row and col in their corresponding sets
        # After scanning, we iterate over the stored rows and cols, setting their elms to 0
        # Runtime: O(m * n) 
        # Space: O(m + n)
        
        
        
        cols = set()
        rows = set()
        m, n = len(matrix), len(matrix[0])
        for y in range(m):
            for x in range(n):
                if matrix[y][x] == 0:
                    rows.add(y)
                    cols.add(x)
        
        # iterate over the cols
        for col in cols:
            for y in range(m):
                matrix[y][col] = 0
        
        # iterate over the rows
        for row in rows:
            for x in range(n):
                matrix[row][x] = 0
        