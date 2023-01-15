class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target < letters[0] or target >= letters[-1]: return letters[0]
        for l in letters:
            if target < l:
                return l

# Alternative solution


class Solution:
    def nextGreatestLetter(self, letters, target):
        left, right = 0, len(letters) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return letters[(right + 1) % len(letters)]
