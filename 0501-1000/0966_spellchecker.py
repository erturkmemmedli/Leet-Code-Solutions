class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        wordmap = {}
        capitals = {}
        vowels = {}
        answer = []

        for word in wordlist:
            wordmap[word] = word

        for word in wordlist[::-1]:
            capitals[word.lower()] = word
        
        for word in wordlist[::-1]:
            capitals["".join('*' if c in 'aioue' else c for c in word.lower())] = word

        for query in queries:
            q1 = wordmap.get(query, "")
            q2 = capitals.get(query.lower(), "")
            q3 = capitals.get("".join('*' if c in 'aioue' else c for c in query.lower()), "")
            answer.append(q1 or q2 or q3)

        return answer
