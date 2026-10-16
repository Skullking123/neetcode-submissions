class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) * len(matrix[0]) - 1

        while left <= right:
            medianIndex = int((left + right) / 2)

            medY = int(medianIndex / len(matrix[0]))
            medX = int(medianIndex % len(matrix[0]))

            value = matrix[medY][medX]

            if target == value:
                return True
            elif target < value:
                right = medianIndex - 1
            else: # target > value
                left = medianIndex + 1
        
        return False


