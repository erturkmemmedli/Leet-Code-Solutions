class Solution:
    def partitionString(self, s: str) -> int:
        seen = set()
        num_of_substrings = 1

        for char in s:
            if char not in seen:
                seen.add(char)
            else:
                seen = {char}
                num_of_substrings += 1
        
        return num_of_substrings
