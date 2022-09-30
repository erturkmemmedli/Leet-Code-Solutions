class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hashmap = collections.Counter(tasks).most_common()
        leading = hashmap[0][1]
        count = 0
        for letter, occurance in hashmap:
            if occurance == leading:
                count += 1
            else:
                break
        if count <= n:
            possible_length = (n + 1) * (leading - 1) + count
        else:
            possible_length = (n + 1) * leading
        return len(tasks) if possible_length <= len(tasks) else possible_length
