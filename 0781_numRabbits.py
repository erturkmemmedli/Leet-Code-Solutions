from collections import Counter

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        rabbits = Counter(answers)
        result = 0
        for answer, occurance in rabbits.items():
            count = answer + 1
            factor = occurance // count
            additional = 1 if occurance % count else 0
            result += (factor + additional) * count
        return result
