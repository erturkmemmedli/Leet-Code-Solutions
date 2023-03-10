from collections import Counter

class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        answer = 0
        for i in range(32):
            mask = 1 << i
            arr = [1 if num & mask else 0 for num in nums]
            count = Counter(arr)
            answer += count[0] * count[1]
        return answer
