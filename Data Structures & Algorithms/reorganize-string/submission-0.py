class Solution:
    def reorganizeString(self, s: str) -> str:
        # given a string s, rearragne the chars of s so that any two adjacent chars are not the same
        # Return any possible rearrangement of s or return "" if not possible
        
        # base case 
        if len(s) == 1:
            return s

        maxC = 0
        counts = {}
        # O(n)
        for letter in s:
            if letter not in counts:
                counts[letter] = 0
            counts[letter] += 1
            maxC = max(maxC, counts[letter])
        
        if maxC > math.ceil(len(s) / 2):
            return "" 

        heap = []
        # O(n)
        for letter, count in counts.items():
            heapq.heappush(heap, (-count, letter))
        
        # priotize using the more common letters as early as possible
        new = []
        # (-count, letter) of the previous letter that we used
        prev = None
        # O(nlg(n))
        while heap:
            count, letter = heapq.heappop(heap)

            new.append(letter)

            # prevent us from the same letter consecutively
            if prev:
                heapq.heappush(heap, prev)
            
            # update our prev pointer
            if count + 1 == 0:
                prev = None
            else:
                prev = (count + 1, letter)

        return "".join(new)