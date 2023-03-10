class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        restaurantsAfterFiltering = []
        for id, rating, vegan, price, distance in restaurants:
            if not vegan and veganFriendly:
                continue
            if price > maxPrice or distance > maxDistance:
                continue
            restaurantsAfterFiltering.append((id, rating))
        restaurantsAfterFiltering.sort(key = lambda x: [-x[1], -x[0]])
        return [i for i, _ in restaurantsAfterFiltering]
