class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        window = collections.Counter()
        maxFruitCollected, startIndex, temp = 0, 0, 0
        for i, fruit in enumerate(fruits):
            if len(window) < 2 or (len(window) == 2 and fruit in window):
                window[fruit] += 1
                temp += 1
                maxFruitCollected = max(maxFruitCollected, temp)
            elif fruit not in window:
                first, second = window.keys()
                if first == fruits[i-1]:
                    startIndex = self.deleteFromWindow(fruits, window, second, startIndex)
                    temp = window[first]
                else:
                    startIndex = self.deleteFromWindow(fruits, window, first, startIndex)
                    temp = window[second]
                window[fruit] += 1
                temp += 1
                maxFruitCollected = max(maxFruitCollected, temp)
        return maxFruitCollected

    def deleteFromWindow(self, fruits, window, char, index):
        while index < len(fruits):
            window[fruits[index]] -= 1
            if window[char] == 0:
                del window[char]
                return index + 1
            index += 1
