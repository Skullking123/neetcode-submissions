class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        ps = []
        for i in range(len(position)):
            ps.append((position[i], speed[i]))
        ps.sort(reverse=True) # sort by their position

        res = 0
        prev = 0
        for pos, spd in ps:
            distLeft = target - pos
            hrsToDest = distLeft / spd
            if hrsToDest > prev:
                res += 1
                prev = hrsToDest

        return res
