class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # There are an EVEN number of piles arranged in a row
        # each pile is a pos int number of stones piles[i]
        # Objective of the game is to end with the most stones
        # The total number of stones across all the piles is odd, so there are no ties
        # Alice and Bob take turns, Alice starts first
        # A player takes the entire pile of stones either from the beginning or from the end of the row
        # This continues until there are no more piles left, at which point the person with the most stones wins
        # Assume Alice and Bob play optimally return true if alice wins or false if bob wins

        # [1,2,3,1]
        # Alice takes the first pile: Alice = 1 Bob = 0
        # [2,3,1]
        # Bob takes the first pile: Alice = 1 Bob = 2
        # [3,1]
        # Alice takes the first pile: Alice = 4 Bob = 2
        # [1]
        # Bob takes the first pile: Alice = 4 Bob = 3
        # Game is over, Alice wins
        
        # bob = # of stones bob has
        # alice = # of stones alice has
        # turn = bool for whose turn it is. True = alice, False = bob
        # left = inclusive left bound of piles
        # right = inclusive right bound of piles
        turns = [False] * len(piles)
        def dfs(alice, bob, turn, left, right):
            # we have consumed all piles, determine the winner
            if turn == len(piles):
                return alice > bob
            
            # if its possible alice can win by turn-th turn
            # she wins the whole game
            if turns[turn]:
                return turns[turn]
            
            aliceLeft = 0
            aliceRight = 0
            bobLeft = 0
            bobRight = 0
            # determine how many stones bob and alice 
            # gain this turn 
            if turn % 2 == 0:
                aliceLeft = piles[left]
                aliceRight = piles[right]
            else:
                bobLeft = piles[left]
                bobRight = piles[right]
            
            # Take the left pile
            takeLeft = dfs(alice + aliceLeft, bob + bobLeft, turn + 1, left + 1, right)
            # If alice wins, then she wins the whole game
            # end computation here
            if takeLeft:
                turns[turn] = True
                return True
            
            # only go right if its confirmed that alice couldn't win when we go left
            takeRight = dfs(alice + aliceRight, bob + bobRight, turn + 1, left, right - 1)
            # Same check as before
            if takeRight:
                turns[turn] = True
                return True
            
            # Bob only wins if Alice loses whether we go left or right
            return False

        return dfs(0, 0, 0, 0, len(piles) - 1)




            























        # O(2^n)
        def dfs(alice, bob, turn, left, right):
            # don't repeat computations
            # if (left, right) in mem:
            #     return mem[(left, right)]
            
            # we have processed all the piles, determine the winner
            if left > right:
                return alice > bob
        
            # if its alice's turn
            if turn:
                # determine the outcomes if we take left or right
                takeLeft = dfs(alice + piles[left], bob, False, left + 1, right) == turn
                takeRight = dfs(alice + piles[right], bob, False, left, right - 1) == turn
                # print(f"Alice's turn Alice = {alice} Bob = {bob} bounds = [{left, right}] takeLeft={takeLeft} takeRight={takeRight}")
                # we are assuming alice will make the optimal play
                # if alice can win by doing left or right, then we can say she wins
                if takeLeft or takeRight:
                    return turn
                else:
                    return not turn
                
                # return mem[(left, right)]
            else:
                # determine the outcomes if we take left or right
                takeLeft = dfs(alice, bob + piles[left], True, left + 1, right) == turn
                takeRight = dfs(alice, bob + piles[right], True, left, right - 1) == turn
                # print(f"Bob's turn Alice = {alice} Bob = {bob} bounds = [{left, right}] takeLeft={takeLeft} takeRight={takeRight}")
                # we are assuming bob will make the optimal play
                # if bob can win by doing left or right, then we can say she wins
                if takeLeft or takeRight:
                    return turn
                else:
                    return not turn
                # return mem[(left, right)]
        
        return dfs(0, 0, True, 0, len(piles) - 1)















