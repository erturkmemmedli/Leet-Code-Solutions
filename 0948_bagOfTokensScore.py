class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        i = 0
        j = len(tokens) - 1
        maxScore = 0
        score = 0
        tokens.sort()
        while i <= j:
            if power >= tokens[i]:
                power -= tokens[i]
                score += 1
                i += 1
            elif score >= 1:
                power += tokens[j]
                score -= 1
                j -= 1
            else:
                break
            maxScore = max(maxScore, score)
        return maxScore
