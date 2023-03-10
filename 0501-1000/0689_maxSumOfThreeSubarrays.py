class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        preSum = [sum(nums[:k])]
        for i in range(len(nums) - k):
            preSum.append(preSum[-1] - nums[i] + nums[i + k])

        leftLook = [None] * len(preSum)
        best = 0
        for i in range(len(preSum)):
            if preSum[i] > preSum[best]:
                best = i
            leftLook[i] = best

        rightLook = [None] * len(preSum)
        best = len(preSum) - 1
        for i in range(len(preSum) -1, -1, -1):
            if preSum[i] >= preSum[best]:
                best = i
            rightLook[i] = best
            
        answer = None
        for mid in range(k, len(preSum) - k):
            left, right = leftLook[mid - k], rightLook[mid + k]
            if not answer or preSum[left] + preSum[mid] + preSum[right] > preSum[answer[0]] + preSum[answer[1]] + preSum[answer[2]]:
                answer = left, mid, right
        return answer
