class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Given an int arr where nums[i] = max jump len at ith pos
        # return true if you can reach the last index starting from index 0 or false
        goal = len(nums) - 1

        # we start from goal and work our way backwards
        for i in range(len(nums) - 2, -1, -1):
            # check to see if from i, we can reach our goal
            if i + nums[i] >= goal:
                # our new goal becomes i
                # This is because if we can find another pos
                # that can allow us to jump to i,
                # then we know that we can get to our final target
                goal = i
        
        # if our goal became 0, then it means that
        # if we can reach 0, then we can reach our final target
        # And since we start at 0 anyways, this equivalently is 
        # asking is it possible to reach our final target from where we start 
        return goal == 0