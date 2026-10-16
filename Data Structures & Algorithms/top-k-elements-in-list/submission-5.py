class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # given an arr of nums and a int k, return the k most frequent elms in the arr

        # get counts of all the nums
        
        freq = [[] for i in range(len(nums) + 1)]
        counts = {}

        for num in nums:
            if num not in counts:
                counts[num] = 0
            counts[num] += 1
        
        for num, count in counts.items():
            freq[count].append(num)
            print(freq)
 
 
        res = []
        for idx in range(len(freq) - 1, -1, -1):
            for num in freq[idx]:
                if len(res) < k:
                    res.append(num)
        return res