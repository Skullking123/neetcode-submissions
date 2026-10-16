class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        l = 0
        r = n - 1

        idx = 0
        while idx <= r:
            if nums[idx] == 0:
                temp = nums[l]
                nums[idx] = temp
                nums[l] = 0
                l += 1
                if idx <= l:
                    idx = l
            elif nums[idx] == 2:
                temp = nums[r]
                nums[idx] = temp
                nums[r] = 2
                r -= 1
            else:
                idx += 1
            # print(nums, l, idx, r)
            
            

        # counts = [0] * 3

        # for num in nums:
        #     counts[num] += 1
        
        # # print(counts)
        # elm = 0

        # for idx in range(len(nums)):

        #     while counts[elm] == 0:
        #         elm += 1
        #     # print(elm)
        #     nums[idx] = elm
        #     counts[elm] -= 1


