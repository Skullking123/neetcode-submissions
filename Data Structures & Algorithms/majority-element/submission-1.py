class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        res = nums[0]

        for num in nums:
            counts[num] += 1
            if counts[num] > counts[res]:
                res = num
            if counts[res] > len(nums) // 2:
                return res
        
        return res
