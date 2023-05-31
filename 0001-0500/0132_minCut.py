class Solution:
    def minCut(self, s: str) -> int:
        self.check = {}
        self.memo = {}
        return self.findLessCut(s, 0) - 1

    def findLessCut(self, s, idx):
        if idx == len(s):
            return 0

        if idx in self.memo:
            return self.memo[idx]

        minimum = float('inf')

        for i in range(idx, len(s)):
            if self.isPalindrome(s, idx, i):
                minimum = min(minimum, self.findLessCut(s, i + 1) + 1)

        self.memo[idx] = minimum
        return minimum

    def isPalindrome(self, s, left, right):
        if left >= right:
            return True

        if s[left] != s[right]:
            return False

        if (left, right) in self.check:
            return self.check[(left, right)]

        self.check[(left, right)] = self.isPalindrome(s, left + 1, right - 1)
        return self.check[(left, right)]
