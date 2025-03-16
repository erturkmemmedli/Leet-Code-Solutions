class Solution(object):
    def lengthOfLongestSubstring(self, s):
        maximum = 0
        start = 0
        end = 0
        dictionary = {}
        for i in range(len(s)):
            if s[i] in dictionary and dictionary[s[i]] + 1 > start:
                start = dictionary[s[i]] + 1
            dictionary[s[i]] = end
            end += 1
            maximum = max(maximum, end - start)
        return maximum

# Alternative solution

class Solution1(object):
    
    def lengthOfLongestSubstring(self, s):
        maximum = 0
        string = ''
        for i in range(len(s)):
            if s[i] not in string:
                string += s[i]
                maximum = max(maximum, len(string))
            else:
                string = string[string.index(s[i]) + 1:]
                string += s[i]
        return maximum

# Alternative solution

class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        longest = 0
        hashmap = {}
        for i, char in enumerate(s):
            if char not in hashmap:
                hashmap[char] = [i]
            else:
                hashmap[char].append(i)
                start = max(start, hashmap[char][-2] + 1)
            longest = max(longest, i - start + 1)
        return longest

# Alternative solution


class Solution:
    def lengthOfLongestSubstring(self, s):
        hashmap = {}
        left = 0
        length = 0
        for char in s:
            if char not in hashmap:
                hashmap[char] = 1
                length = max(length, len(hashmap))
            else:
                hashmap[char] += 1
                while hashmap[char] != 1:
                    hashmap[s[left]] -= 1
                    if hashmap[s[left]] == 0:
                        del hashmap[s[left]]
                    left += 1
        return length

# Alternative solution

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        start = 0
        answer = 0

        for end in range(len(s)):
            while s[end] in window:
                window.remove(s[start])
                start += 1

            window.add(s[end])
            answer = max(answer, len(window))

        return answer
