class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        maximum = 0
        
        for i in range(1, n - 1):
            left = [num for num in nums[:i] if num < nums[i]] + [nums[i]]
            right = [nums[i]] + [num for num in nums[i+1:] if num < nums[i]]
            right = right[::-1]

            left_lis_length = self.lengthOfLIS(left)
            right_lis_length = self.lengthOfLIS(right)

            if left_lis_length >= 2 and right_lis_length >= 2:
                maximum = max(maximum, left_lis_length + right_lis_length - 1)

        return n - maximum

    def lengthOfLIS(self, nums):
        lis = []
        
        for num in nums:
            idx = bisect_left(lis, num)
            if idx == len(lis):
                lis.append(num)
            else:
                lis[idx] = num

        return len(lis)
