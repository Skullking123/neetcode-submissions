class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Given an int arr nums, rotate the array to the right by k steps 
        # where k is non-negative
        
        # For the last k elemenets in the arr, they move to the front
            # The nth becomes the kth element
            # The (n-1)th elm becomes the (k - 1)th elm 
            # The (n-2)th elm becomes the (k - 2)th elm
            # ...
            # ()
            # The (n - k + 1)th elm becomes the 1st elm
        # All the other elms:
            # The 1st elm, becomes the (k + 1)th elm
            # The 2nd elm, becomes the (k + 2)th elm
            # ...
            # The (n - k)th elm, becomes the nth element
        # Generalizing: 
        n = len(nums)
        k = k % n
        
        nums.reverse()
        # print(nums)
        # the original last k elms are now the first k elms
        # but in reverse order... reverse them
        # to get them back in order
        # print(k // 2 - 1)
        for idx in range((k // 2 - 1) + 1):
            temp = nums[idx]
            nums[idx] = nums[k - idx - 1]
            nums[k - idx - 1] = temp
        # print(nums)
        # the original last n - k elms are now the last n - k elms
        # but in reverse order... reverse them
        for idx in range(k, (n + k) // 2):
            temp = nums[idx]
            nums[idx] = nums[n - idx + k - 1]
            nums[n - idx + k - 1] = temp
        

















        
