class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        count_map = defaultdict(int)
        n = len(nums)
        prefix = [0] * (n + 1)
        answer = 0
        
        for i in range(n):
            prefix[i + 1] = prefix[i] + (nums[i] % modulo == k)
        
        for i in range(n + 1):
            j = prefix[i] - k
            answer += count_map[j % modulo]
            count_map[prefix[i] % modulo] += 1
        
        return answer
