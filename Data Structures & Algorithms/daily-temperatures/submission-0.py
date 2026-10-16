class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        stack.append(0)
        for i in range(1, len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                tempPtr = stack.pop()
                res[tempPtr] = i - tempPtr
            
            stack.append(i)

        return res

