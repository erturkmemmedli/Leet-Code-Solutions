class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        # target ranges:
        # 2 <-> min(a, b) + 1 <-> a + b <-> a + b + 1 <-> max(a, b) + limit + 1 <-> 2 * limit
        counter = Counter()

        for i in range(len(nums) // 2):
            a, b = nums[i], nums[len(nums) - i - 1]
            counter[2] += 2
            counter[min(a, b) + 1] -= 1
            counter[a + b] -= 1
            counter[a + b + 1] += 1
            counter[max(a, b) + limit + 1] += 1

        count = 0
        result = float('inf')

        for i in range(2, 2 * limit + 1):
            count += counter[i]
            result = min(result, count)
        
        return result
