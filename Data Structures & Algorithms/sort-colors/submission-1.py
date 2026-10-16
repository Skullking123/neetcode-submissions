class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        counts = [0] * 3

        for num in nums:
            counts[num] += 1
        
        # print(counts)
        elm = 0

        for idx in range(len(nums)):

            while counts[elm] == 0:
                elm += 1
            # print(elm)
            nums[idx] = elm
            counts[elm] -= 1


