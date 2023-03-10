class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        window = deque()
        vowels = "aeiou"
        maxVowelCount = 0
        current = 0
        for char in s:
            if len(window) < k:
                window.append(char)
                if char in vowels:
                    current += 1
                maxVowelCount = max(maxVowelCount, current)
            else:
                pop = window.popleft()
                if pop in vowels:
                    current -= 1
                window.append(char)
                if char in vowels:
                    current += 1
                maxVowelCount = max(maxVowelCount, current)
        return maxVowelCount
