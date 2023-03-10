class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        summ = sum([i for i in nums if not i % 2])
        output = []
        for value, index in queries:
            if nums[index] % 2 == 0:
                if value % 2 == 0:
                    summ += value
                else:
                    summ -= nums[index]
            else:
                if value % 2 == 1:
                    summ += nums[index] + value
            output.append(summ)
            nums[index] += value
        return output
