class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        if rec2[0] >= rec1[2] or rec2[2] <= rec1[0] or rec2[1] >= rec1[3] or rec2[3] <= rec1[1]:
            return False
        if rec1[0] < rec2[0] < rec1[2] or rec1[0] < rec2[2] < rec1[2]:
            return True
        if rec1[1] < rec2[1] < rec1[3] or rec1[1] < rec2[3] < rec1[3]:
            return True
        if rec1[0] > rec2[0] and rec1[1] > rec2[1] and rec1[2] < rec2[2] and rec1[3] < rec2[3]:
            return True
        if rec1[0] < rec2[0] and rec1[1] < rec2[1] and rec1[2] > rec2[2] and rec1[3] > rec2[3]:
            return True
        return False
      
# Alternative solution

class Solution1:
    def isRectangleOverlap(self, rec1, rec2):
        left = max(rec1[0], rec2[0])
        bot = max(rec1[1], rec2[1])
        right = min(rec1[2], rec2[2])
        top = min(rec1[3], rec2[3])
        return left < right and top > bot
