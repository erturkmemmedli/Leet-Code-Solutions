class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        cheese = cheeseSlices * 2
        if cheese > tomatoSlices:
            return []
        elif cheese == tomatoSlices:
            return [0, cheeseSlices]
        else:
            tomato = tomatoSlices - cheese
            if tomato % 2 == 1:
                return []
            elif tomato > cheese:
                return []
            else:
                finalTomato = tomato // 2
                finalCheese = cheeseSlices - finalTomato
                return [finalTomato, finalCheese]
