class Solution:
    def climbStairs(self, n: int) -> int:
        # return the number of distinct ways to climb to the top of the staircase
        # Can only climb either 1 or 2 steps at a time
        # obs that the ways to climb n steps is equal to (# of ways to climb n - 1 steps) + (# of ways to climb n - 2 steps)
            # For every way to climb n - 1 steps, you just need to climb 1 more step to get to n
            # For every way to climb n - 2 steps, you just need to climb 2 steps for one time to get to n
        if n == 1:
            return 1
        steps = [0] * (n + 1) 
        steps[1] = 1
        steps[2] = 2

        for step in range(3, n + 1):
            steps[step] = steps[step - 1] + steps[step - 2]
        
        return steps[n]