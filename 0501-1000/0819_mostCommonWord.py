class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = {}
        curr = ""

        for char in paragraph:
            if char.isalpha():
                curr += char.lower()
            else:
                if curr:
                    words[curr] = words.get(curr, 0) + 1
                    curr = ""
        
        if curr:
            words[curr] = words.get(curr, 0) + 1
            
        for word in banned:
            if word in words:
                del words[word]
            
        return max(words, key=words.get, default=0)
