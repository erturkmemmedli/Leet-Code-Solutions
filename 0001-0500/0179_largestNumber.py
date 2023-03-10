class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        numsString = [str(num) for num in nums]
        maxLength = len(max(numsString, key = len))
        for i, num in enumerate(numsString):
            lngth = len(num)
            while lngth + len(num) <= maxLength * 2:
                numsString[i] += num
                lngth = len(numsString[i])
            numsString[i] += num[:maxLength * 2 - lngth]
        finalNums = []
        for i, num in enumerate(numsString):
            finalNums.append([int(num), i])
        finalNums.sort(reverse = True)
        result = ""
        for _, i in finalNums:
            if not result and nums[i] == 0:
                continue
            result += str(nums[i])
        return result if result else "0"
