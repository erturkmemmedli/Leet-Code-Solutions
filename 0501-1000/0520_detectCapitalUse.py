class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if ord(word[0]) <= 90:
            return all(ord(word[i]) <= 90 for i in range(1, len(word))) or all(ord(word[i]) >= 97 for i in range(1, len(word)))
        if ord(word[0]) >= 97:
            return all(ord(word[i]) >= 97 for i in range(1, len(word)))
            
# Alternative solution

class Solution1:
    def detectCapitalUse(self, word: str) -> bool:
        if word[0].islower():
            for i in range(1, len(word)):
                if word[i].isupper(): return False
        else:
            if len(word) > 1:
                if word[1].islower():
                    for j in range(2, len(word)):
                        if word[j].isupper(): return False
                else:
                    for j in range(2, len(word)):
                        if word[j].islower(): return False
        return True

# Alternative solution

class Solution2:
    def detectCapitalUse(self, word: str) -> bool:
        count = 0
        for char in word:
            if 65 <= ord(char) <= 90:
                count += 1
        if len(word) == count or not count: return True
        elif count > 1: return False
        else: return word[0].isupper()
