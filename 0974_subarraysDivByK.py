class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix = [0] * k
        prefix[0] = 1
        currentSum = 0
        answer = 0
        for num in nums:
            currentSum += num
            remain = currentSum % k
            answer += prefix[remain]
            prefix[remain] += 1
        return answer

# Alternative solution (which gives TLE error)

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefixSum = [0]
        for num in nums:
            prefixSum.append(prefixSum[-1] + num)
        result = 0
        for i in range(len(prefixSum)):
            for j in range(i+1, len(prefixSum)):
                if (prefixSum[j] - prefixSum[i]) % k == 0:
                    result += 1
        return result
