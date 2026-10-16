class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        sub_boxes = {}
        cols = {}
        rows = {}

        for r in range(9):
            for c in range(9):
                box_x = c // 3
                box_y = r // 3
                if (box_x, box_y) not in sub_boxes:
                    sub_boxes[(box_x, box_y)] = set()
                if r not in rows:
                    rows[r] = set()
                if c not in cols:
                    cols[c] = set()
                elm = board[r][c]
                if elm == ".":
                    continue
                if elm in sub_boxes[(box_x, box_y)] or elm in rows[r] or elm in cols[c]:
                    return False
                rows[r].add(elm)
                cols[c].add(elm)
                sub_boxes[(box_x, box_y)].add(elm)                
        return True