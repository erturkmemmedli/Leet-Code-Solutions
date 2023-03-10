class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        indexMap = collections.defaultdict(list, {0 : [-1]})
        maxLength = 0
        for i in range(len(nums)):
            if i == 0:
                if nums[i] == 0:
                    nums[i] = -1
                indexMap[nums[i]].append(i)
                continue
            if nums[i] == 0:
                nums[i] = nums[i-1] - 1
            else:
                nums[i] = nums[i-1] + 1
            indexMap[nums[i]].append(i)
            l = indexMap[nums[i]]
            if len(l) > 1:
                maxLength = max(maxLength, l[-1] - l[0])
        return maxLength
