class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [(temperatures[0], 0)]
        res = [0] * len((temperatures))
        for curr in range(len(temperatures)):
            temp = temperatures[curr]

            while stack and temp > stack[-1][0]:
                (_, prev) = stack.pop()
                res[prev] = curr - prev
            
            stack.append((temp, curr))
        return res

