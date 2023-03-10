class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        window = collections.deque()
        currentProduct = 1
        count = 0
        for num in nums:
            if num >= k:
                window = collections.deque()
                currentProduct = 1
            elif num * currentProduct >= k:
                while window and num * currentProduct >= k:
                    currentProduct //= window.popleft()
                window.append(num)
                currentProduct *= num
                count += len(window)
            else:
                window.append(num)
                currentProduct *= num
                count += len(window)
        return count
