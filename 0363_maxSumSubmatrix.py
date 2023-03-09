class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m, n, maximum_sum = len(matrix), len(matrix[0]), -float("inf")

        for left in range(n):
            temp = [0] * m

            for right in range(left, n):
                for i in range(m):
                    temp[i] += matrix[i][right]

                current_sum = 0
                current_list = [0]

                for t in temp:
                    current_sum += t
                    index = bisect.bisect_left(current_list, current_sum - k)

                    if index != len(current_list):
                        maximum_sum = max(maximum_sum, current_sum - current_list[index])

                    bisect.insort(current_list, current_sum)

        return maximum_sum
