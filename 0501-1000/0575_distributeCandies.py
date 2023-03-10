class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        candy = set(candyType)
        x = len(candyType) // 2
        y = len(candy)
        return y if y < x else x
      
# Alternative solution

class Solution1:
    def distributeCandies(self, candyType: List[int]) -> int:
        return min(len(candyType) // 2, len(set(candyType)))
