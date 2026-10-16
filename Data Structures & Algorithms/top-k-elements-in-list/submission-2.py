class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            if num in counts:
                counts[num] = counts[num] + 1
            else:
                counts[num] = 1
        
        res = []
        ordered = list(counts.items())
        ordered.sort(key=lambda x: x[1], reverse=True)
        for place in range(k):
            res.append(ordered[place][0])
            
        
        return res
        


         
        

         