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

# Alternative solution

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        window = {}
        left = 0
        maxFruits = 0
        for right in range(len(fruits)):
            if len(window) < 2:
                window[fruits[right]] = window.get(fruits[right], 0) + 1
                maxFruits = max(maxFruits, right - left + 1)
            elif fruits[right] in window:
                window[fruits[right]] += 1
                maxFruits = max(maxFruits, right - left + 1)
            else:
                while len(window) == 2:
                    window[fruits[left]] -= 1
                    if window[fruits[left]] == 0:
                        del window[fruits[left]]
                    left += 1
                window[fruits[right]] = 1
        return maxFruits

# Alternative solution

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = {}
        longest = 0
        i = j = 0

        while i < len(fruits):
            while len(basket) == 2 and fruits[i] not in basket:
                basket[fruits[j]] -= 1
                if not basket[fruits[j]]: del basket[fruits[j]] 
                j += 1
            
            basket[fruits[i]] = basket.get(fruits[i], 0) + 1
            longest = max(longest, i - j + 1)
            i += 1
        
        return longest
