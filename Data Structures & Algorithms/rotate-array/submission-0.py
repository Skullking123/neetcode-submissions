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

        k = k % len(nums)
        
        temp = [0] * len(nums)
        
        for idx in range(len(nums)):
            temp[(idx + k) % len(nums)] = nums[idx]
        
        for idx in range(len(nums)):
            nums[idx] = temp[idx]

















        
