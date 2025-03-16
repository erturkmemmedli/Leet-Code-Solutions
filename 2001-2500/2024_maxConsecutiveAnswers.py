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

# Alternative solution

class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        true = false = start = answer = 0

        for end in range(len(answerKey)):
            if answerKey[end] == 'T':
                true += 1
            else:
                false += 1

            while true > k and false > k:
                if answerKey[start] == 'T':
                    true -= 1
                else:
                    false -= 1
                start += 1
            
            answer = max(answer, end - start + 1)

        return answer
