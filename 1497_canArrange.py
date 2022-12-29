class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        total = 0
        counter = collections.Counter()
        for num in arr:
            total += num
            counter[num % k] += 1
        if total % k: return False
        for key in counter.keys():
            if key == 0 and counter[key] % 2: return False
            if k % 2 == 0 and key == k // 2 and counter[key] % 2: return False
            if key != 0 and counter[key] != counter[k - key]: return False
        return True
