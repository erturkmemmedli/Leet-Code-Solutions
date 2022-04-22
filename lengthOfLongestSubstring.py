class Solution(object):
    
    def lengthOfLongestSubstring(self, s):
        maximum = 0
        start = 0
        end = 0
        dictionary = {}
        for i in range(len(s)):
            if s[i] not in dictionary:
                dictionary[s[i]] = end
                end += 1
                maximum = max(maximum, end - start)
            else:
                if dictionary[s[i]] + 1 > start:
                    start = dictionary[s[i]] + 1
                dictionary[s[i]] = end
                end += 1
                maximum = max(maximum, end - start)
        return maximum