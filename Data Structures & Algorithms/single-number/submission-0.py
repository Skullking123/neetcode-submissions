class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # given a non-empty arr of integers nums. Every integer appears
        # twice except for one

        # Return the int that appears only once
        # Must be O(n) runtime and O(1) extra space

        # Ideas:
        # Nested for loops
            # Not O(n) runtime
        # Go through, adding elms to a set and checking if the curr elm is in the set
            # Not O(1) space
        # Sort the list and see if for any elm, they are equal to the elm to their left
            # Not O(n) runtime
        # Iterate through, checking if an elm is in a bloomfilter
            # The chance of a false positive would be an issue
        # Two pointer?
            # How would I keep track of what is in my window and still be O(1) space?
        # Bitwise AND?
            # Limited number of bits in a int, can't possibly cover all the possible nums to be found
        # EXTREMELY Dumb idea: We allocate arr that is exactly 20,001 elms long filled with 0
            # set arr[elm] += 1 for elm we come across
            # iterate over the arr and return the elm where arr[elm] == 1
            # technically O(1) space since the arr is always a fixed size
            # Not a scalable solution if the range of nums[i] ever increases beyond current bounds
        
        counts = [0] * 20001

        for elm in nums:
            counts[elm] += 1
        
        for num in range(-10000, 10000 + 1):
            if counts[num] == 1:
                return num
        
        return None