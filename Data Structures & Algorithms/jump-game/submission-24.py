class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Given an int arr where nums[i] = max jump len at ith pos
        # return true if you can reach the last index starting from index 0 or false
        pos = 0
        target = len(nums) - 1
        
        while pos < target:

            # we can reach our target from our pos
            # we don't need to do any computation
            # exit and return True
            if pos + nums[pos] >= target:
                break

            # examine all the next pos we can jump to and see 
            # which one we can go the furthest if we were to jump 
            # at that pos
            furthestPos = 0
            next = pos
            for possible in range(pos + 1, pos + nums[pos] + 1):
                if possible + nums[possible] > furthestPos:
                    furthestPos = possible + nums[possible]
                    next = possible
            
            # we can't go any further
            if next == pos:
                return False
            
            pos = next
        
        return True