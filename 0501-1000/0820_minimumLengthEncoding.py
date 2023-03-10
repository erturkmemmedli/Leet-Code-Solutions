class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words.sort(key = len, reverse = True)
        sett = set()
        length = 0
        for word in words:
            if word not in sett:
                length += len(word) + 1
                for i in range(len(word)):
                    part = word[i:] 
                    if part not in sett:
                        sett.add(part)
                    else:
                        break
        return length
