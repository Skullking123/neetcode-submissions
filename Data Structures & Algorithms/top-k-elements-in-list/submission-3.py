class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        freqInOrder = sorted(list(freq.items()), key = lambda x: x[1], reverse = True)
        res = []
        print(freqInOrder)
        for mostFreq in range(k):
            res.append(freqInOrder[mostFreq][0])
        
        return res