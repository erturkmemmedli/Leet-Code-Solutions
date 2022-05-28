class Solution:
    def firstUniqChar(self, s: str) -> int:
        dictionary = {}
        array = []
        for i in range(len(s)):
            if s[i] not in dictionary:
                dictionary[s[i]] = i
                array.append(i)
            else:
                try:
                    array.remove(dictionary[s[i]])
                except:
                    continue
        return array[0] if array else -1
      
# Alternative solution

class Solution1:
    def firstUniqChar(self, s: str) -> int:
        dictionary = {}
        array = [None] * len(s)
        for i in range(len(s)):
            if s[i] not in dictionary:
                dictionary[s[i]] = i
                array[i] = i
            else:
                array[dictionary[s[i]]] = None
                array[i] = None
        for j in array:
            if j is not None: return j
        return -1

# Alternative solution

class Solution2:
    def firstUniqChar(self, s: str) -> int:
        hashset = set()
        hashmap = dict()
        for index, char in enumerate(s):
            if char not in hashset:
                hashset.add(char)
                hashmap[char] = index
            elif char in hashmap:
                del(hashmap[char])
        return min(hashmap.values()) if hashmap else -1
    
# Alternative solution

class Solution3:
    def firstUniqChar(self, s: str) -> int:
        hashset = set()
        hashmap = dict()
        for index, char in enumerate(s):
            if char not in hashset:
                hashset.add(char)
                hashmap[char] = index
            elif char in hashmap:
                del(hashmap[char])
        return next(iter(hashmap.values())) if hashmap else -1
