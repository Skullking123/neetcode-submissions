class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # only process if there is more than 1 elm
        if len(nums) <= 1:
            return nums


        forward = [0] * len(nums)
        reverse = [0] * len(nums)

        forward[0] = nums[0]
        reverse[len(nums) - 1] = nums[len(nums) - 1]

        for i in range(1, len(nums)):
            # print(f"forward: {i}")
            forward[i] = nums[i] * forward[i - 1]
        
        for i in range(len(nums) - 2, -1, -1):
            # print(f"reverse: {i}")
            reverse[i] = nums[i] * reverse[i + 1]
        
        # init our return
        res = [0] * len(nums)
        res[0] = reverse[1]
        res[len(nums) - 1] = forward[len(nums) - 2]

        for i in range(1, len(nums) - 1):
            res[i] = forward[i - 1] * reverse[i + 1]
        return res

        