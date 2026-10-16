class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # cost[i] is the cost of taking a step from the ith floor of a staircase
        # you can step to either the (i + 1)th floor or (i + 2)th floor
        # can start from either 0th or 1st floor
        # return the minimum cost to reach the top of the staircase

        # obs that the minimum cost to get to i stairs is equivalent to min(minCost[i - 1] + cost[i - 1], minCost[i - 2] + cost[i - 2])
        
        # there is only the 0th or 1st floor
        # since you can start from either, return the min cost

        # memory optimal
        n = len(cost)
        if len(cost) <= 2:
            return min(cost)
        
        prevFloor = 0
        prevPrevFloor = 0
        
        for floor in range(2, n + 1):
            curr = min(prevFloor + cost[floor - 1], prevPrevFloor + cost[floor - 2])
            prevPrevFloor = prevFloor
            prevFloor = curr
        
        return prevFloor




        n = len(cost)
        if len(cost) <= 2:
            return min(cost)

        minCost = [0] * (n + 1) 
        # you can start at either 0, 1
        # minCost[0] = cost[0]
        # minCost[1] = cost[1]

        for floor in range(2, n + 1):
            minCost[floor] = min(minCost[floor - 1] + cost[floor - 1], minCost[floor - 2] + cost[floor - 2])
        print(minCost)
        return minCost[-1] 
