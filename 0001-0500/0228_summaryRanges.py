class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        first = nums[0]
        last = nums[0]
        i = 1
        answer = []
        while i <= len(nums):
            if i < len(nums) and nums[i] == nums[i-1] + 1:
                last = nums[i]
            else:
                if first == last:
                    answer.append(str(first))
                else:
                    answer.append(str(first) + "->" + str(last))
                if i < len(nums):
                    first = nums[i]
                    last = nums[i]
            i += 1
        return answer
