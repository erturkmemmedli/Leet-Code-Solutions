class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        hashmap = collections.defaultdict(collections.deque)
        for word in words:
            hashmap[word[0]].append(word)
        answer = 0
        for char in s:
            for _ in range(len(hashmap[char])):
                word = hashmap[char].popleft()
                if len(word) == 1:
                    answer += 1
                else:
                    hashmap[word[1]].append(word[1:])
        return answer
