class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        final = [0 for _ in range(num_people)]
        i = 0
        gift = 1
        while candies:
            if gift < candies:
                final[i] += gift
                candies -= gift
                gift += 1
                i += 1
                if i == num_people: i = 0
            else:
                final[i] += candies
                break
        return final
