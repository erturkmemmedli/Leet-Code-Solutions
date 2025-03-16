class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s):
        window = {}
        left = 0
        longest = 0
        for right in range(len(s)):
            if len(window) < 2:
                window[s[right]] = window.get(s[right], 0) + 1
                longest = max(longest, right - left + 1)
            elif s[right] in window:
                window[s[right]] += 1
                longest = max(longest, right - left + 1)
            else:
                while len(window) == 2:
                    window[s[left]] -= 1
                    if window[s[left]] == 0:
                        del window[s[left]]
                    left += 1
                window[s[right]] = 1
        return longest

# Alternative solution

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s):
        window = {}
        longest = 0
        i = j = 0
        
        while i < len(s):
            while len(window) == 2 and s[i] not in window:
                window[s[j]] -= 1
                
                if not window[s[j]]:
                    del window[s[j]]
                
                j += 1
                    
            window[s[i]] = window.get(s[i], 0) + 1
            longest = max(longest, sum(window.values()))
            i += 1
        
        return longest

# Alternative solution

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s):
        window = {}
        start = 0
        answer = 0
        
        for end in range(len(s)):
            window[s[end]] = window.get(s[end], 0) + 1
            
            while len(window) > 2:
                window[s[start]] -= 1
                if window[s[start]] == 0:
                    del window[s[start]]
                start += 1
                
            answer = max(answer, end - start + 1)
        
        return answer
