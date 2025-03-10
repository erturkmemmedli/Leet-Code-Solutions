class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        return self.findAtLeastK(word, k) - self.findAtLeastK(word, k + 1)

    def findAtLeastK(self, word, k):
        vowels = {'a', 'i', 'o', 'u', 'e'}
        window = defaultdict(int)
        count = 0
        consonants = 0
        start = end = 0

        while end < len(word) or start < len(word):            
            if len(window) == 5 and consonants >= k:
                count += len(word) - end + 1
                if word[start] not in vowels:
                    consonants -= 1
                else:
                    window[word[start]] -= 1
                    if window[word[start]] == 0:
                        del window[word[start]]
                start += 1
            else:
                if end == len(word):
                    break
                if word[end] not in vowels:
                    consonants += 1
                else:
                    window[word[end]] += 1
                end += 1
            
        return count
