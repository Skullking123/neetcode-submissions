class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        # regardless of however many elms combined, there will always be equal # of elms
        # on either side of the median: (m + n) // 2
        # I need to find the first (m + n) // 2 elements 
        A, B = nums1, nums2
        n, m = len(A), len(B)

        # make A the smaller list to keep it fixed
        if n > m:
            A, B = B, A
        
        total = n + m
        half = total // 2
        
        l = 0
        r = len(A) - 1

        while True:
            # i + j = half

            # i will be the index of aleft, j will be the index of bleft
            # i + 1 will be the index of aright and j + 1 index of bright

            i = (l + r) // 2
            j = half - i - 2
        
            aleft = A[i] if i >= 0 else float('-inf')
            bleft = B[j] if j >= 0 else float('-inf')
            aright = A[i + 1] if i + 1 < len(A) else float('inf')
            bright = B[j + 1] if j + 1 < len(B) else float('inf')
            
            # base case (when to exit and return median)
            # bleft <= bright aleft <= aright
            # bleft and aleft, aright and bright
            if (bleft <= aright and aleft <= bright):
                if total % 2:
                    return min(aright, bright)
                else:
                    return (max(bleft, aleft) + min(aright, bright)) / 2
            elif aleft > bright:
                # overshot cutoff
                r = i - 1
            else: # aright < bleft
                # undershot cutoff
                l = i + 1
