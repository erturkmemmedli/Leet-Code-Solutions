class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        sorted_nums = sorted([(num, i) for i, num in enumerate(nums)])
        stack = []

        for i, (num, idx) in enumerate(sorted_nums):
            if not stack:
                stack.append([idx])
                continue
            if num - sorted_nums[i - 1][0] <= limit:
                stack[-1].append(idx)
            else:
                stack.append([idx])

        hashmap = {}
        result = [None] * len(nums)

        for gr in stack:
            gr_s = sorted(gr)
            for i in range(len(gr)):
                hashmap[gr_s[i]] = gr[i]
        
        for k, v in hashmap.items():
            result[k] = nums[v]
        
        return result
