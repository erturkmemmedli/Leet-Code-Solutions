class Solution:
    def reverseString(self, s: List[str]) -> None:
        for i in range(len(s)//2):
            s[i], s[len(s) - 1 - i] = s[len(s) - 1 - i], s[i]

# Alternative solution

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1
