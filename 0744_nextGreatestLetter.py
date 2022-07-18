class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target < letters[0] or target >= letters[-1]: return letters[0]
        for l in letters:
            if target < l:
                return l
