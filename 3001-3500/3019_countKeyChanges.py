class Solution:
    def countKeyChanges(self, s: str) -> int:
        total_change = 0

        for i in range(1, len(s)):
            if s[i].lower() != s[i - 1].lower():
                total_change += 1
            
        return total_change
