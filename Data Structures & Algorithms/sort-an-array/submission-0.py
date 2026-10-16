class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # sort nums in ascending order 
        # do not use any built-in functions and sort it
        # in O(nlog(n)) with the smallest space complexity possible

        # we can do mergesort, is O(nlog(n))
        # have memeroy just be O(nlog(n)) for the max recursion stack
        def mergeSort(left, right): # merge sort the segment from idx: left to idx: right inclusive
            # only one elm, nothing to sort
            print(left, right)
            if left == right:
                return 
            
            # split the list into halves
            mid = (left + right) // 2
            left_left = left
            left_right = mid 
            right_left = mid + 1
            right_right = right
            # in the case of odd lengths, make the right take on the extra elm
            # if right - left + 1 % 2 == 1:
            #     left_right -= 1
            
            # sort each half seperately
            mergeSort(left_left, left_right)
            mergeSort(right_left, right_right)
            
            # merge the two halfs after sorting them
            left_ptr = left_left
            right_ptr = right_left
            res_ptr = 0
            sorted_res = [0] * (right - left + 1)
            while left_ptr <= left_right or right_ptr <= right_right: # keep merging while we still have elms
                if right_ptr > right_right or (left_ptr <= left_right and nums[left_ptr] <= nums[right_ptr]):
                    sorted_res[res_ptr] = nums[left_ptr]
                    res_ptr += 1
                    left_ptr += 1
                else: 
                    sorted_res[res_ptr] = nums[right_ptr]
                    res_ptr += 1
                    right_ptr += 1

            res_ptr = 0 
            cpy_ptr = left
            # copy the sorted result into nums
            while cpy_ptr <= right:
                nums[cpy_ptr] = sorted_res[res_ptr]
                cpy_ptr += 1
                res_ptr += 1
        mergeSort(0, len(nums) - 1)
        return nums
            # [0,1,2,3,4,5]
