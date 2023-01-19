class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([num ** 2 for num in nums])
   
# Alternative solution

class Solution1:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for index in range(len(nums)):
            if nums[index] < 0:
                nums[index] *= -1
            else:
                break
        result = []
        if index > 0 and nums[index] > abs(nums[index - 1]):
            i = index - 1
            j = index - 1
        else:
            i = index
            j = index
        while i >= 0 and j < len(nums):
            if i == j:
                result.append(nums[i] ** 2)
                i -= 1
                j += 1
                continue
            if nums[i] <= nums[j]:
                result.append(nums[i] ** 2)
                i -= 1
            else:
                result.append(nums[j] ** 2)
                j += 1
        if i < 0:
            for k in range(j, len(nums)):
                result.append(nums[k] ** 2)
        if j >= len(nums):
            for k in range(i, -1, -1):
                result.append(nums[k] ** 2)
        return result

# Alternative solution

class Solution2:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if nums[0] >= 0:
            return [num ** 2 for num in nums]
        if nums[-1] < 0:
            return [num ** 2 for num in nums[::-1]]
        for i in range(len(nums)):
            if nums[i] >= 0:
                index = min(i, i-1, key = lambda x: abs(nums[x]))
                break
        squares = [nums[index] ** 2]
        left = index - 1
        right = index + 1
        while left >= 0 and right < len(nums):
            if abs(nums[left]) <= nums[right]:
                squares.append(nums[left] ** 2)
                left -= 1
            else:
                squares.append(nums[right] ** 2)
                right += 1
        if right >= len(nums):
            squares += [nums[i] ** 2 for i in range(left, -1, -1)]
        elif left < 0:
            squares += [nums[i] ** 2 for i in range(right, len(nums))]
        return squares

# Alternative solution

class Solution:
    def sortedSquares(self, nums):
        positiveFirst = len(nums)
        for i in range(len(nums)):
            if nums[i] >= 0:
                positiveFirst = i
                break
        negativeLast = positiveFirst - 1
        result = []
        while negativeLast >= 0 and positiveFirst < len(nums):
            if -nums[negativeLast] <= nums[positiveFirst]:
                result.append(nums[negativeLast] ** 2)
                negativeLast -= 1
            else:
                result.append(nums[positiveFirst] ** 2)
                positiveFirst += 1
        while negativeLast >= 0:
            result.append(nums[negativeLast] ** 2)
            negativeLast -= 1
        while positiveFirst < len(nums):
            result.append(nums[positiveFirst] ** 2)
            positiveFirst += 1
        return result
