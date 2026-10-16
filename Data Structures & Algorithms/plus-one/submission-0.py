from collections import deque
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = deque()
        carryOver = True
        for d in range(len(digits) - 1, -1, -1):
            resDig = digits[d]
            if carryOver:
                resDig = digits[d] + 1

            if resDig > 9:
                resDig -= 10
                res.appendleft(resDig)
                if d == 0:
                    res.appendleft(1)
            else:
                res.appendleft(resDig)
                carryOver = False
        
        return list(res)