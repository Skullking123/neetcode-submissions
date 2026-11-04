class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        

        for idx in range(len(nums)):
            nums.append(nums[idx])

        return nums



        idx = 0
        res = []
        n = len(nums)
        
        while idx < 2 * n:
            res.append(nums[idx % n])
            idx += 1

        return res