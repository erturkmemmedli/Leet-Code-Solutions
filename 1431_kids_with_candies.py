class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatest = max(candies)
        output = []
        for i in range(len(candies)):
            if candies[i] + extraCandies >= greatest:
                output.append(True)
            else:
                output.append(False)
        return output
