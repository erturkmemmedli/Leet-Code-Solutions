from sortedcontainers import SortedList
from collections import defaultdict

class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        self.n = n
        self.movie_map = defaultdict(SortedList)
        self.shop_movie_map = {}
        self.rent_set = set()
        self.rented = SortedList()

        for shop, movie, price in entries:
            self.movie_map[movie].add([price, shop, movie])
            self.shop_movie_map[(shop, movie)] = price

    def search(self, movie: int) -> List[int]:
        result = []
        for price, shop, movie in self.movie_map[movie]:
            if (shop, movie) not in self.rent_set:
                result.append(shop)
                if len(result) == 5:
                    break
        return result

    def rent(self, shop: int, movie: int) -> None:
        price = self.shop_movie_map[(shop, movie)]
        self.rented.add([price, shop, movie])
        self.rent_set.add((shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        price = self.shop_movie_map[(shop, movie)]
        self.rented.remove([price, shop, movie])
        self.rent_set.remove((shop, movie))

    def report(self) -> List[List[int]]:
        return [[shop, movie] for price, shop, movie in self.rented[:5]]


# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()
