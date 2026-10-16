from collections import deque
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = []
        digits[len(digits) - 1] += 1
        carryOver = 0
        for idx in range(len(digits) - 1, -1, -1):
            digit = digits[idx]
            addOne = digit + carryOver
            if addOne >= 10:
                carryOver = 1
                addOne -= 10
            else:
                carryOver = 0
            res = [addOne] + res

        if carryOver == 1:
            return [1] + res
        else:
            return res