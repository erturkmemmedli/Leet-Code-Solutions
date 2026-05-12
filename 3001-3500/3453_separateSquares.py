class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        events, total_area = [], 0
        for x, y, l in squares:
            events.append([y, 1, l])
            events.append([y + l, 0, l])
            total_area += l * l
        events.sort()

        combined_width = current_area = previous_height = 0
        for y, is_start, l in events:
            height_diff = y - previous_height
            area_diff = combined_width * height_diff

            if current_area + area_diff >= total_area / 2:
                # curr_area + (combined_width * optimal_height_diff) = total_area / 2
                optimal_height_diff = (total_area / 2 - current_area) / combined_width
                return previous_height + optimal_height_diff

            combined_width += l if is_start else -l
            current_area += area_diff
            previous_height = y
