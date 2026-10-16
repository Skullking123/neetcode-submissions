class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        kFrequent = []
        counts = dict()
        for num in nums:
            if num in counts:
                counts[num] = counts[num] + 1
            else:
                counts[num] = 1
        
        counts = sorted(counts.items(), key=lambda x:x[1])
        for nums in range(0, k):
            (num, count) = counts.pop()
            kFrequent.append(num)

        return kFrequent

         
        

         