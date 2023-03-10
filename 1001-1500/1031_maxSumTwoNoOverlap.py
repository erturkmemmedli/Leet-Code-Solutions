from collections import deque

class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        hash_first = self.slide_window(nums, firstLen)
        hash_second = self.slide_window(nums, secondLen)
        max_sum = 0
        for x1, x2 in hash_first:
            for y1, y2 in hash_second:
                if x1 <= y2 and x2 >= y1:
                    continue
                max_sum = max(max_sum, hash_first[(x1, x2)] + hash_second[(y1, y2)])
        return max_sum
        
    def slide_window(self, nums, length):
        hashmap = {}
        queue = deque()
        summ = 0
        for i in range(len(nums)):
            if len(queue) < length:
                queue.append(nums[i])
                summ += nums[i]
            if len(queue) == length:
                hashmap[(i - length + 1, i)] = summ
                summ -= queue.popleft()
        return hashmap
        
# Alternative solution

class Solution1:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        presum = [0]
        for num in nums:
            presum.append(presum[-1] + num)
        summ = 0
        L = len(presum)
        F = firstLen
        S = secondLen  
        max_first = 0
        for i in range(F, L - S):
            max_first = max(max_first, presum[i] - presum[i - F])
            summ = max(summ, max_first + presum[i + S] - presum[i])
        max_second = 0
        for i in range(S, L - F):
            max_second = max(max_second, presum[i] - presum[i - S])
            summ = max(summ, max_second + presum[i + F] - presum[i])
        return summ
