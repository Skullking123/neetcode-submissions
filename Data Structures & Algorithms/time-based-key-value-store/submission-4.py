class TimeMap:

    def __init__(self):
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key] = []
        self.timeMap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""
            
        values = self.timeMap[key]

        left = 0
        right = len(values) - 1

        res = -1
        resStr = ""

        while left <= right:
            
            median = (left + right) // 2
            (mk, mt) = values[median]

            if mt <= timestamp:
                if mt > res:
                    res = mt
                    resStr = mk
            
            if mt <= timestamp:
                left = median + 1
            else:
                right = median - 1

        return resStr

            


            
