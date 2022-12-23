class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        heap = []
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                heapq.heappush(heap, (i + j, -i, nums[i][j]))
        answer = []
        while heap:
            answer.append(heapq.heappop(heap)[2])
        return answer
