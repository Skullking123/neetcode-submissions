class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        res = True;
        subBoxes = {}
        rows = {}
        cols = {}

        for row in range(0, 9):
            if (row not in rows):
                rows[row] = set()
            
            for col in range(0, 9):
                if (board[row][col] == "."):
                    continue
                    
                if (col not in cols):
                    cols[col] = set()
                
                subBoxX = int(col / 3)
                subBoxY = int(row / 3)

                if ((subBoxX, subBoxY) not in subBoxes):
                    subBoxes[(subBoxX, subBoxY)] = set()
                

                if (board[row][col] in subBoxes[(subBoxX, subBoxY)]):
                    res = False
                else:
                    subBoxes[(subBoxX, subBoxY)].add(board[row][col])
            
                if (board[row][col] in rows[row]):
                    res = False
                else:
                    rows[row].add(board[row][col])
                
                if (board[row][col] in cols[col]):
                    res = False
                else:
                    cols[col].add(board[row][col])
        print(subBoxes)
        print(cols)
        print(rows)
        return res
        
        