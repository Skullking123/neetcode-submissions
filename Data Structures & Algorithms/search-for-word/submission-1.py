class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # return true if the word is present in the grid
        # The same cell may not be used more than once in a word

        # go cell by cell and perform a dfs using our word to dictate whether to go in a 
        # certain direction
        seen = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def dfs(idx: int, x: int, y: int) -> bool:
            if idx == len(word):
                return True
            if (x, y) in seen:
                return False
            if x < 0 or x > len(board[0]) - 1 or y < 0 or y > len(board) - 1:
                return False
            if board[y][x] != word[idx]:
                return False
            
            seen.add((x, y))
            res = False
            for dx, dy in directions:
                nx = x + dx
                ny = y + dy
                res = res or dfs(idx + 1, nx, ny)
            
            seen.remove((x, y))
            return res
        
        for y in range(len(board)):
            for x in range(len(board[0])):
                if dfs(0, x, y):
                    return True
        
        return False



            