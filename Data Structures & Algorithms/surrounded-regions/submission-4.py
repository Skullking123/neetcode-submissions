class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # given an m x n matrix board, containing letters 'X' and 'O', capture regions that are surrounded
        # a region is a series of O's that are connected either horizontally or vertically
        # a region is surrounded if none of the 'O's are on the edge of the board

        # we could reverse the paradigm, find all the O cells that are not surrounded:
            # traverse the edges and perform bfs whenever we find an "O", updating a global set 
            # that will contain all the elms that we managed to visit and are not surrounded
            
            # then we can traverse over the whole board to marking X's on O's that are not in the set
        m = len(board)
        n = len(board[0])
        free = set()

        def bfs(x, y):
            visited = set()

            queue = deque()
            queue.append((x, y))

            dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            while queue:
                cx, cy = queue.popleft()
                if cx < 0 or cx >= n or cy < 0 or cy >= m or board[cy][cx] == "X" or (cx, cy) in visited or (cx, cy) in free:
                    continue
                visited.add((cx, cy))
                for dx, dy in dirs:
                    queue.append((cx + dx, cy + dy))
                
            return visited
        

        for x in range(n):
            if board[0][x] == "O" and board[0][x] not in free:
                free.update(bfs(x, 0))
            if board[m - 1][x] == "O" and board[m - 1][x] not in free:
                free.update(bfs(x, m - 1))
        
        for y in range(1, m - 1):
            if board[y][0] == "O" and board[y][0] not in free:
                free.update(bfs(0, y))
            if board[y][n - 1] == "O" and board[y][n - 1] not in free:
                free.update(bfs(n - 1, y))
        
        for x in range(1, n - 1):
            for y in range(1, m - 1):
                if board[y][x] == "O" and (x, y) not in free:
                    board[y][x] = "X"
        