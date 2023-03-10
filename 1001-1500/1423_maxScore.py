class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        maxScore = sum(cardPoints[:k])
        temp = maxScore
        for i in range(k):
            temp -= cardPoints[k - i - 1]
            temp += cardPoints[-i - 1]
            maxScore = max(maxScore, temp)
        return maxScore
