class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        currEvenSum = 1
        currOddSum = 0
        curr = 0
        result = 0
        for num in arr:
            curr = (curr + num) % 2
            if curr:
                result += currEvenSum
                currOddSum += 1
            else:
                result += currOddSum
                currEvenSum += 1
        return result % (10**9 + 7)
