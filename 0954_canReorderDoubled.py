class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        arr.sort(reverse = True)
        counter = collections.defaultdict(int)
        for num in arr:
            if num not in counter and num >= 0 and num // 2 == num / 2:
                counter[num // 2] += 1
            elif num not in counter and num < 0:
                counter[num * 2] += 1
            else:
                counter[num] -= 1
                if counter[num] == 0:
                    del counter[num]
        return not counter
