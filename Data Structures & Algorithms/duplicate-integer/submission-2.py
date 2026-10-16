class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        elms = set()

        for num in nums:
            if num in elms:
                return True
            else:
                elms.add(num)

        return False