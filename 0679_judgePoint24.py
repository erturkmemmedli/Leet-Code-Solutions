class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        if len(cards) == 1:
            return abs(cards[0] - 24) <= 0.1
        for i in range(len(cards)):
            for j in range(i+1, len(cards)):
                newList = [card for k, card in enumerate(cards) if k != i and k != j]
                for res in self.generateResults(cards[i], cards[j]):
                    newList.append(res)
                    if self.judgePoint24(newList):
                        return True
                    newList.pop()

    def generateResults(self, a, b):
        result = [a+b, a-b, b-a, a*b]
        if a: result.append(b/a)
        if b: result.append(a/b)
        return result
