class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        self.memo = {}
        return self.dp(questions, 0)

    def dp(self, questions, index):
        if index >= len(questions):
            return 0

        point, step = questions[index]

        if index in self.memo:
            return self.memo[index]

        self.memo[index] = max(point + self.dp(questions, index + step + 1), self.dp(questions, index + 1))
        return self.memo[index]
