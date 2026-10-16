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
        
        # We scan the entire matrix looking for 0s
        # For every zero, we set the values its row and col to None
        # Then we iterate back over the matrix setting all None to actual 0
        # for row in matrix:
        #     print(row)
        m, n = len(matrix), len(matrix[0])

        for y in range(m):
            for x in range(n):
                if matrix[y][x] != 0:
                    continue
                # mark this col to zero
                for ny in range(m):
                    if matrix[ny][x] != 0:
                        matrix[ny][x] = None
                # mark this row to zero
                for nx in range(n):
                    if matrix[y][nx] != 0:
                        matrix[y][nx] = None
        
        for y in range(m):
            for x in range(n):
                if matrix[y][x] == None:
                    matrix[y][x] = 0
        # print()
        # for row in matrix:
        #     print(row)
        