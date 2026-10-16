class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        sums = {}

        for index in range(0, len(numbers)):
            sums[numbers[index]] = index
        
        for num in numbers:
            if (target - num) in sums:
                return [min(sums[target - num] + 1, sums[num] + 1), max(sums[target - num] + 1, sums[num] + 1)]
        
        return []
        