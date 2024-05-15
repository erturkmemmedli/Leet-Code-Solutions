class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        line = 1
        curr = 0
        i = 0

        while i < len(s):
            idx = ord(s[i]) - ord('a')
            pixel = widths[idx]
            i += 1

            if curr + pixel <= 100:
                curr += pixel
            else:
                line += 1
                curr = pixel
            
            
        return [line, curr]
