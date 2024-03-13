class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        def count_position(distance):
            answer = 1
            current_position = position[0]

            for i in range(1, len(position)):
                if position[i] - current_position >= distance:
                    answer += 1
                    current_position = position[i]
                
            return answer

        left = 0
        right = position[-1] - position[0]
        
        while left < right:
            mid = right - (right - left) // 2

            if count_position(mid) >= m:
                left = mid
            else:
                right = mid - 1
            
        return left
