class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        words = sentence.split()
        converted = ""

        for i, word in enumerate(words):
            if word[0] in ['a', 'e', 'i', 'o', 'u']:
                converted += word + 'ma' + 'a' * (i + 1)
            else:
                converted += word[1:] + word[0] + 'ma' + 'a' * (i + 1)
            if i != len(words) - 1:
                converted += " "
            
        return converted
