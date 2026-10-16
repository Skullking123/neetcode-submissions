class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = defaultdict(set)
        cols = defaultdict(set)
        subBoxes = defaultdict(set)

        for x in range(9):
            for y in range(9):  
                row = rows[y]
                col = cols[x]
                XSubBox = int(x / 3)
                YSubBox = int(y / 3)
                subBox = subBoxes[(XSubBox, YSubBox)]

                entry = board[x][y]
                if not entry.isnumeric():
                    continue
                    
                if (entry in row) or (entry in col) or (entry in subBox):
                    return False
                
                row.add(entry)
                col.add(entry)
                subBox.add(entry)
        
        print(rows)
        print(cols)
        print(subBoxes)
        return True

