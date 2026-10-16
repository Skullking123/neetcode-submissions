class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        # piles[i] = # of stones in the ith pile
        # Alice and Bob take turns, with Alice starting first
        # On each turn, the player can take all the stones in the first X remaining piles
            # Where 1 <= X <= 2m. Then set M = max(M, X), initially M = 1
    

        # [4,3,2,5,10]
        # alice takes first pile. Alice = 4 Bob = 0. X = 1, M = 1
        # Bob takes the  2nd pile. Alice = 4 Bob = 3. X = 1, M = 1
        # alice takes the 3rd and 4th pile. Alice = 11 Bob = 3. X = 1, M = 1
        # Bob takes the last pile. Alice = 11 Bob = 13

        # [6,10,5,3,9]
        # alice takes the bot first and 2nd pile. If Alice were to take [6, 10] = 16. Bob can take [5,3,9] = 17
            # whereas with if she only took [6]. Bob the next turn can only get [10, 5] = 15

        mem = {}

        # brute force
        def dfs(idx, m, turn):

            if idx == len(piles):
                return (0, 0)

            if (idx, m, turn) in mem:
                return mem[(idx, m, turn)]

            # symbolic constants for turn
            ALICE = True
            BOB = False

            # keeps track of their max scores. Whoevers turn it is, is who we are going to maximize
            max_alice_score = 0
            max_bob_score = 0
            
            current_score = 0

            for x in range(min(len(piles) - idx, 2 * m)):
                # we are taking this pile
                current_score += piles[idx + x]
                # calculate the maximum score that you can get the remaining piles
                alice_score, bob_score = dfs(idx + x + 1, max(m, x + 1), not turn)
                
                # Bob and Alice are going to play optimally. So they will attempt to maximize their score
                if turn == ALICE and alice_score + current_score > max_alice_score:
                    max_alice_score = alice_score + current_score
                    max_bob_score = bob_score
                elif turn == BOB and bob_score + current_score > max_bob_score:
                    max_bob_score = bob_score + current_score
                    max_alice_score = alice_score
            
            mem[(idx, m, turn)] = (max_alice_score, max_bob_score)
            return mem[(idx, m, turn)]
            # return (max_alice_score, max_bob_score)

        return dfs(0, 1, True)[0]



















