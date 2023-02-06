class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        trueWindow = collections.deque()
        falseWindow = collections.deque()
        trueK = k
        falseK = k
        maxConfusion = 0
        for key in answerKey:
            trueWindow.append(key)
            falseWindow.append(key)
            if key == 'T':
                falseK -= 1
            else:
                trueK -= 1
            while falseK < 0:
                pop = falseWindow.popleft()
                if pop == 'T':
                    falseK += 1
                    break
            while trueK < 0:
                pop = trueWindow.popleft()
                if pop == 'F':
                    trueK += 1
                    break
            maxConfusion = max(maxConfusion, len(trueWindow), len(falseWindow))
        return maxConfusion
