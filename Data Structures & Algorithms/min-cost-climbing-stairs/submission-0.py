class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        steps = [100 * len(cost)] * (len(cost))
        steps[0] = cost[0]
        steps[1] = cost[1]

        for step in range(2, len(cost)):
            minSteps = min(steps[step - 1] + cost[step], steps[step - 2] + cost[step])
            steps[step] = minSteps
            print(steps)
        

        return min(steps[len(cost) - 1], steps[len(cost) - 2])
        