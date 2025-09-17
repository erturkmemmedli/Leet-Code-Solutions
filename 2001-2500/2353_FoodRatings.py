class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        n = len(foods)
        self.cuisine_map = {}
        self.food_map = {}
        
        for i in range(n):
            f, c, r = foods[i], cuisines[i], ratings[i]

            if c not in self.cuisine_map:
                self.cuisine_map[c] = []
            heappush(self.cuisine_map[c], (-r, f))
            self.food_map[f] = [r, c]

    def changeRating(self, food: str, newRating: int) -> None:
        self.food_map[food][0] = newRating
        cuisine = self.food_map[food][1]
        heappush(self.cuisine_map[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        heap = self.cuisine_map[cuisine]
        r, f = heappop(heap)
        if self.food_map[f][0] == -r:
            heappush(heap, (r, f))
            return f
        else:
            return self.highestRated(cuisine)


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
