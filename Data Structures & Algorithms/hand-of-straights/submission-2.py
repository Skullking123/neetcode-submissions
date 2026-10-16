class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # You are given an integer arr hand where hand[i] is the value of the ith card and an integer groupSize
        # Rearrange the cards into straights where the cards are consecutively increasing by 1
        # return True if its possible, false otherwise

        # we could try sorting it, then picking out consecutive unique numbers
            # problems: How to consider a number is alr used
            # Iterating over the list over and over for more and more straights is expensive. (Possibly n^2)
        # we could put the card values along with their counts into a min-heap and build our striaghts by drawing the smallest unqiue values

        # if we don't have enough cards
        if len(hand) % groupSize != 0:
            return False
        
        # generate the counts of the values
        # O(n)
        counts = {}
        for card in hand:
            if card not in counts:
                counts[card] = 0
            counts[card] += 1

        # stores (card_value, count)
        # O(n)
        heap = []
        for card, count in counts.items():
            heapq.heappush(heap, [card, count])
        
        # O(nlg(n))
        while len(heap) >= groupSize:
            straight = []
            first = heapq.heappop(heap)
            first[1] -= 1 # decrement the count since we are using it
            straight.append(first)
            # construct our straight
            for _ in range(groupSize - 1):
                (card, count) = heapq.heappop(heap)
                # make sure the cards are consectively increasing by 1
                if card != straight[-1][0] + 1:
                    return False
                count -= 1
                straight.append((card, count))

            # add the card back in if we still have cards of similar value left
            for card, count in straight:
                if count > 0:
                    heapq.heappush(heap, [card, count])
        return len(heap) == 0