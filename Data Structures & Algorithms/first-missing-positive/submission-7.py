class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # given an unsorted int array nums. Return the smallest positive integer
        # that is not present in nums
        # Must implement an O(n) alg with O(1) space

        # [-2, -1, 0]
        # [1, 2, 4]

        # non-pos numbers do not change the smallest pos int
        # as they don't affect the range of pos numbers in a list

        # two-pointer doesn't work because we cannot be sure that an elm 
        # that we remove from the window is an elm that doesn't have elm + 1
        # in the list as well since the list isn't sorted

        # stack implementation using a ptr for point to top of the stack in nums
        # [1]
        # [1,2]
        # [1,2,4]
        # [3,1,2]
        
        # [2]
        # [2,3]
        # [2,3,1]
        
        # mark all negatives as 0
        for idx in range(len(nums)):
            if nums[idx] < 0:
                nums[idx] = 0
        # print(nums)
        n = len(nums)
        for idx in range(len(nums)):
            val = abs(nums[idx])
            if val == 0 or val > n:
                continue
            
            if nums[val - 1] > 0:
                nums[val - 1] *= -1
            elif nums[val - 1] == 0:
                nums[val - 1] = -(n + 1)
            # print(nums)
        # print(nums)
        for idx in range(len(nums)):
            if nums[idx] >= 0:
                return idx + 1
        
        return n + 1
            



















