class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # given two ints n and k, return all possible combinations of k
        # numbers chosen from the range [1, n]
        # You may return teh answer in any order

        # for any given n, we can say we can either:
            # use n and then make combinations of size k - 1 out of [1, n - 1]
            # not use n and make combinations of size k out of [1, n - 1]

        # only one way we can make a combination of 0 elements
        if k == 0:
            return [[]]
        
        # print(n, k)

        # use n and make combinations of size k - 1 out of the rest
        include = self.combine(n - 1, k - 1)
        for combo in include: # make sure to actually include n
            combo.append(n)
        
        # don't use n and make combinations of size k out of the rest
        # if there are less possible elms than k, we can't exclude
        exclude = self.combine(n - 1, k) if n > k else []
        
        # combine the two
        include.extend(exclude)
        return include
        