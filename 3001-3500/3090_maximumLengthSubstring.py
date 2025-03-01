class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        start = 0
        window = {}
        result = 0

        for end in range(len(s)):
            while window.get(s[end], 0) == 2:
                window[s[start]] -= 1
                if window[s[start]] == 0:
                    del window[s[start]]
                start += 1

            window[s[end]] = window.get(s[end], 0) + 1
            result = max(result, end - start + 1)
        
        return result
