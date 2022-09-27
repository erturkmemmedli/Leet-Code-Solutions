class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        self.expenditure = sum([price[i] * needs[i] for i in range(len(price))])
        special_book = {}
        for offer in special:
            item = tuple(offer[:-1])
            if item not in special_book:
                special_book[item] = offer[-1]
            else:
                special_book[item] = min(special_book[item], offer[-1])
        self.dfs(price, special_book, needs, 0)
        return self.expenditure
                
    def dfs(self, price, special, needs, current_cost):
        for offer, cost in special.items():
            after_offer = []
            for i in range(len(needs)):
                amount = needs[i] - offer[i]
                if amount >= 0:
                    after_offer.append(amount)
                else:
                    after_offer = []
                    break
            if after_offer:
                self.dfs(price, special, after_offer, current_cost + cost)
        for i in range(len(needs)):
            current_cost += needs[i] * price[i]
        self.expenditure = min(self.expenditure, current_cost)
        return
