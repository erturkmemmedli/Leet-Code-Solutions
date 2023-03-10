class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        window = collections.deque()
        hashmap = collections.defaultdict(int)
        letters = collections.defaultdict(int)
        for char in s:
            if len(window) < minSize - 1:
                window.append(char)
                letters[char] += 1
            else:
                window.append(char)
                letters[char] += 1
                if len(letters) <= maxLetters:
                    hashmap["".join(window)] += 1
                    pop = window.popleft()
                    if letters[pop] == 1: del letters[pop]
                    else: letters[pop] -= 1
                else:
                    pop = window.popleft()
                    if letters[pop] == 1: del letters[pop]
                    else: letters[pop] -= 1
        return max(hashmap.values(), default = 0)
