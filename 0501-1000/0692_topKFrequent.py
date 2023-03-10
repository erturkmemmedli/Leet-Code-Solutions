class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        hashmap = collections.Counter(words).most_common()
        hashmap.sort(key = lambda x: [-x[1],x[0]])
        return [hashmap[i][0] for i in range(k)]
