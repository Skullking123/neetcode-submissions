class Solution:
    def rob(self, nums: List[int]) -> int:
        # nums[i] represents the amount of money the ith house has
        # cannot rob two adjacent houses
        # return the max amount of money you can rob 

        # for the ith house, we can either rob the ith and ith - 2 house, or just rob the ith - 1 house
        
        n = len(nums)
        # only 2 houses, can only rob one of the two
        if n <= 2:
            return max(nums)

        # represents max money you can gain by robbing houses[0:i] inclusively
        money = [0] * n
        money[0] = nums[0]
        money[1] = max(nums[0], nums[1])

        for house in range(2, n):
            money[house] = max(money[house - 1], money[house - 2] + nums[house])
        print(money)
        return money[-1]