class Solution:
    def findRadius(self, houses, heaters) -> int:
        houses.sort()
        heaters.sort()
        sec = [0]
        for i in range(1, len(heaters)):
            sec.append((heaters[i] + heaters[i-1])//2)
        sec.append(float('inf'))
        part = [[sec[i-1], sec[i]] if not (i-1) else [sec[i-1] + 1, sec[i]] for i in range(1, len(sec))]
        i = 0
        j = 0
        maxi = 0
        while i < len(houses):
            if part[j][0] <= houses[i] <= part[j][1]:
                maxi = max(maxi, abs(heaters[j] - houses[i]))
                i += 1
            else:
                j += 1
        return maxi
