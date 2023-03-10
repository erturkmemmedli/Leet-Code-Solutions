class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        d = {}
        for i, ch in enumerate(s):
            d[indices[i]] = ch
        shuffled = ""
        for i in range(len(s)):
            shuffled += d[i]
        return shuffled
      
# Alternative solution

class Solution1:
    def restoreString(self, s: str, indices: List[int]) -> str:
        shuffled = [None] * len(s)
        for char, index in zip(s, indices):
            shuffled[index] = char
        shuffled = ''.join(shuffled)
        return shuffled
