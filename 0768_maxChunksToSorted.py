class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        hashmap = {}
        current = None
        duplicates = collections.defaultdict(list)
        for i, num in enumerate(arr):
            if not hashmap:
                hashmap[num] = [i, i]
                current = num
                continue
            if num < current:
                for key in hashmap.keys():
                    if key > num:
                        hashmap[key][1] = i
            elif num == current:
                duplicates[num].append(i)
            else:
                hashmap[num] = [i, i]
                current = num
        listmap = [val for key, val in sorted(hashmap.items())]
        chunks = 1
        high = listmap[0][1]
        for i in range(1, len(listmap)):
            if listmap[i][0] > high:
                chunks += 1
            high = listmap[i][1]
        for item in duplicates:
            for idx in duplicates[item]:
                if idx > hashmap[item][1]:
                    chunks += 1
        return chunks
