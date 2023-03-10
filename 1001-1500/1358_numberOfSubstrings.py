class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        a, b, c, n = 0, 0, 0, len(s)
        occurence = 0
        window = collections.deque()
        for i, char in enumerate(s):
            while a != 0 and b != 0 and c != 0:
                pop = window.popleft()
                if pop == 'a': a -= 1
                if pop == 'b': b -= 1
                if pop == 'c': c -= 1
                occurence += n - i + 1
            if char == 'a': a += 1
            if char == 'b': b += 1
            if char == 'c': c += 1
            window.append(char)
        while len(window) >= 3 and a > 0 and b > 0 and c > 0:
            pop = window.popleft()
            if pop == 'a': a -= 1
            if pop == 'b': b -= 1
            if pop == 'c': c -= 1
            occurence += 1
        return occurence
   
# Alternative solution

class Solution1:
    def numberOfSubstrings(self, s: str) -> int:
        characters, n = [0, 0, 0], len(s)
        occurence = 0
        window = collections.deque()
        for i, char in enumerate(s):
            while all(characters):
                pop = window.popleft()
                characters[ord(pop) - ord('a')] -= 1
                occurence += n - i + 1
            characters[ord(char) - ord('a')] += 1
            window.append(char)
        while len(window) >= 3 and all(characters):
            pop = window.popleft()
            characters[ord(pop) - ord('a')] -= 1
            occurence += 1
        return occurence
