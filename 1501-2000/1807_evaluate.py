class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        knowledge = {key: val for key, val in knowledge}
        words = []
        current = []
        for char in s:
            if char == "(":
                if current:
                    word = "".join(current)
                    words.append(word)
                    current = []
            elif char == ')':
                word = "".join(current)
                val = knowledge.get(word, "?")
                words.append(val)
                current = []
            else:
                current.append(char)

        if current:
            word = "".join(current)
            words.append(word)
        return "".join(words)
