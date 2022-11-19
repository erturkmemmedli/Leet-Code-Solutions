class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        hashmap = {}
        for word in s1.split() + s2.split():
            if hashmap.get(word, 0):
                hashmap[word] += 1
            else:
                hashmap[word] = 1
        return [key for key, val in hashmap.items() if val == 1]
