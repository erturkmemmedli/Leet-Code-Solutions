class Cashier:
    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.discount = discount
        self.hashmap = {products[i]:prices[i] for i in range(len(products))}
        self.count = 0
        
    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.count += 1
        total = 0
        for i, p in enumerate(product):
            total += amount[i] * self.hashmap[p]
        if self.count % self.n == 0:
            total -= total * self.discount / 100
        return total

# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount) 
