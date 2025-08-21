class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        output = []

        prefix_sum = []
        for num in nums:
            prefix_sum.append(num + (prefix_sum[-1] if prefix_sum else 0))

        for query in queries:
            i_left = bisect_left(nums, query)
            i_right = bisect_right(nums, query)

            if i_left == n:
                output.append(query * n - prefix_sum[-1])
            elif i_right == 0:
                output.append(prefix_sum[-1] - query * n)
            elif i_left != i_right:
                left_sum = prefix_sum[i_left]
                left_remaining = query * (i_left + 1) - left_sum
                right_sum = prefix_sum[-1] - prefix_sum[i_right - 1]
                right_remaining = right_sum - query * (n - i_right)
                output.append(left_remaining + right_remaining)
            else:
                left_sum = prefix_sum[i_left - 1]
                left_remaining = query * i_left - left_sum
                right_sum = prefix_sum[-1] - prefix_sum[i_right - 1]
                right_remaining = right_sum - query * (n - i_right)
                output.append(left_remaining + right_remaining)

        return output
