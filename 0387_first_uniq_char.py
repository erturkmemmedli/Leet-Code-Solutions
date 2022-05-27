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
