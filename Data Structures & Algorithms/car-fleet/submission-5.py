from math import ceil
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for idx in range(len(position)):
            cars.append((position[idx], speed[idx]))
        cars.sort(reverse=True)
        print(cars)
        res = 0
        prev = 0
        for (pos, sp) in cars:
            time = (target - pos) / sp
            print(f"time: {time}")
            print(f"prev: {prev}")
            if time > prev:
                print('come here')
                res += 1
            prev = max(prev, time)
            print()
        
        return res
