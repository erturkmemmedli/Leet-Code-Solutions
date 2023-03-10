from collections import deque

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort(key = lambda x: -x)
        output = deque()
        for card in deck:
            if output: 
                output.appendleft(output.pop())
                output.appendleft(card)
            else:
                output.appendleft(card)
        return output
