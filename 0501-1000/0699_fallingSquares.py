class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        height = [0]
        position = [0]
        result = []
        maximum_height = 0

        for left_index, side_length in positions:
            i = bisect_right(position, left_index)
            j = bisect_left(position, left_index + side_length)
            h = max(height[i-1:j] or [0]) + side_length

            position[i:j] = [left_index, left_index + side_length]
            height[i:j] = [h, height[j-1]]

            maximum_height = max(maximum_height, h)
            result.append(maximum_height)

        return result
