class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums) - 1
        # the list has been rotated
        if nums[left] > nums[right]:
            # try to find the pivot that seperates the two sorted lists
            # try to find the smallest elm of the right sublist
            while left <= right:
                mid = (right + left) // 2
                if nums[mid] > nums[mid + 1]:
                    if target < nums[0]:
                        left = mid + 1
                        right = len(nums) - 1
                    else:
                        left = 0
                        right = mid
                    break
                # we are in right sublist, go left
                elif nums[mid] < nums[0]:
                    right = mid - 1
                else: # nums[mid] > nums[0] 
                    left = mid + 1

        # do standard binary search on the sublist that our
        # elm should be in if it is present
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return -1













