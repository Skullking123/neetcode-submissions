class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        combo = []
        partialSum = 0
        def dfs(num, start):
            nonlocal partialSum
            partialSum += num
            combo.append(num)
            # print(f"partial Sum: {partialSum} combo: {combo}")
            

            if partialSum == target:
                res.append(combo.copy())
                partialSum -= num
                combo.pop()
                return
            elif partialSum > target:
                partialSum -= num
                combo.pop()
                return
            else:
                for idx in range(start, len(nums)):
                    dfs(nums[idx], idx)
                partialSum -= num
                combo.pop()
        
        for idx in range(len(nums)):
            dfs(nums[idx], idx)
            # combo = []
            # partialSum = 0

        return res
