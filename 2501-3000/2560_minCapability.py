class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        start = min(nums)
        end = max(nums)

        def helper(mid):
            current = 0
            is_last = False

            for num in nums:
                if is_last:
                    is_last = False
                    continue
                if num <= mid:
                    current += 1
                    is_last = True
            
            return current

        while start < end:
            mid = (start + end) // 2
            current = helper(mid)
                
            if current >= k:
                end = mid
            else:
                start = mid + 1
            
        return start

