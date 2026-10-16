class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}

        for index, num in enumerate(nums):
            diff[target - num] = index



        print(diff)
        for index, num in enumerate(nums):
            print(f"{index}, {num}")
            if num in diff:
                if index == diff[num]:
                    continue
                return [min(index, diff[num]), max(index, diff[num])]
        
        return []