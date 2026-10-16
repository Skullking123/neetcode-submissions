class Solution:
    def climbStairs(self, n: int) -> int:
        steps = [0] * (n + 1)
        steps[0] = 1
        steps[1] = 1

        for step in range(2, len(steps)):
            steps[step] = steps[step - 1] + steps[step - 2]
            print(steps)
        
        return steps[n]

