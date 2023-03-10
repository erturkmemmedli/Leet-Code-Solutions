class Solution:
    def arrangeWords(self, text: str) -> str:
        textSplitted = text.split()
        textSplitted[0] = textSplitted[0].lower()
        textSplitted.sort(key = len)
        textSplitted[0] = textSplitted[0].capitalize()
        return " ".join(textSplitted)
