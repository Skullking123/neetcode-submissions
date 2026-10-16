class Solution:
    def rob(self, nums: List[int]) -> int:
        # nums[i] represents the money in ith house
        # the houses are arranged in a circle (first and last are neighbors)
        # can't rob two adj houses
        # return the max amount of money

        # money[house] = max(money[house - 1], money[house - 2] + nums[house])

        # the only thing thats changed from house robber 1 is that you can't rob the first and last in one robbery
        def helper(nums: List[int]) -> int:
            print(nums)
            n = len(nums)
            if n <= 2:
                return max(nums)

            # represents max money you can gain by robbing houses[0:i] inclusively
            money = [0] * n
            money[0] = nums[0]
            money[1] = max(nums[0], nums[1])

            for house in range(2, n):
                money[house] = max(money[house - 1], money[house - 2] + nums[house])
            
            # print(money)
            return money[-1]
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(helper(nums[1:]), helper(nums[:(len(nums) - 1)]))