class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        window = {}
        left = 0
        longest = 0
        for right in range(len(s)):
            if len(window) < k:
                window[s[right]] = window.get(s[right], 0) + 1
                longest = max(longest, right - left + 1)
            elif s[right] in window:
                window[s[right]] += 1
                longest = max(longest, right - left + 1)
            else:
                while len(window) == k:
                    window[s[left]] -= 1
                    if window[s[left]] == 0:
                        del window[s[left]]
                    left += 1
                window[s[right]] = 1
        return longest

# Alternative solution

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s, k):
        if not k:
            return 0
        
        window = {}
        longest = 0
        i = j = 0
        
        while i < len(s):
            while len(window) == k and s[i] not in window:
                window[s[j]] -= 1
                if not window[s[j]]:
                    del window[s[j]]
                j += 1
                
            
            window[s[i]] = window.get(s[i], 0) + 1
            longest = max(longest, i - j + 1)
            i += 1
            
        return longest
