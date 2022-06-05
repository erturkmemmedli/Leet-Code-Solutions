class Solution:
    def toLowerCase(self, s: str) -> str:
        return s.lower()
      
# Alternative solution

class Solution1:
    def toLowerCase(self, s: str) -> str:
        lower = ""
        for ch in s:
            if 65 <= ord(ch) <= 90:
                lower += chr(ord(ch) + 32)
            else:
                lower += ch
        return lower
