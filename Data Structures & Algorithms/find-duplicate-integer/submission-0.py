class ListNode:
    def __init__(self, val: int, next: ListNode = None):
        self.val = val
        self.next = next

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # nums is a list of nums that is a length of n + 1 intergers
        # each int is in range [1, n] inclusive
        # we are guranteed that every integer appears exactly once except one integer appears two or more times
        # we can use the array itself as a hash set without creating a new one
            # by marking the positions corresponding to the elements that have alr been encountered
        
        # since we are aiming for O(1) space, we are probably looking at a solution using ptrs
        # since each int is [1, n], each element can be used as an index to another elm in the arr
        # if the list was all distinct, we would never visit the same index twice
        
        slow = 0
        fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow2 = nums[slow2]
            slow = nums[slow]
            if slow2 == slow:
                return slow

        return slow   
        
        
        