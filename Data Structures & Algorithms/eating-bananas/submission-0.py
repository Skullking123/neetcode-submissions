from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        mini = 1
        maxi = max(piles)
        minK = maxi
        while mini <= maxi:
            median = int((mini + maxi) / 2)

            numHrs = 0
            for pile in piles:
                numHrs += ceil(pile / median) 
            
            if numHrs <= h:
                maxi = median - 1
                minK = min(minK, median)
            elif numHrs > h:
                mini = median + 1
        
        return minK



