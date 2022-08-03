class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if flowerbed == [0]:
            return n <= 1
        i = 0
        count = 0
        while i < len(flowerbed):
            if flowerbed[i] == 1:
                i += 2
            else:
                if i == 0:
                    if i < len(flowerbed)-1 and flowerbed[i+1] == 0:
                        count += 1
                        i += 2
                    else:
                        i += 1
                elif i > 0 and i < len(flowerbed)-1:
                    if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                        count += 1
                        i += 2
                    else:
                        i += 1
                else:
                    if i > 0 and flowerbed[i-1] == 0:
                        count += 1
                        i += 2
                    else:
                        i += 1
        return count >= n
