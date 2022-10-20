class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        top = None
        bot = None
        determined = None
        FirstElementCount = 0
        topCount = 0
        botCount = 0
        for i in range(len(tops)):
            if not determined:
                if not top:
                    top = tops[i]
                    bot = bottoms[i]
                    if top != bot:
                        FirstElementCount = 1                
                else:
                    if not FirstElementCount:
                        if tops[i] == top and bottoms[i] == bot:
                            continue
                        elif tops[i] == top:
                            FirstElementCount = 1
                            topCount = 1
                            determined = top
                        elif bottoms[i] == bot:
                            FirstElementCount = 1
                            botCount = 1
                            determined = bot
                        else:
                            return -1
                        continue
                    if tops[i] == top and bottoms[i] == bot:
                        FirstElementCount += 1
                    elif tops[i] == bot and bottoms[i] == top:
                        continue
                    elif tops[i] not in [top, bot] and bottoms[i] not in [top, bot]:
                        return -1
                    elif bottoms[i] == tops[i]:
                        determined = tops[i]
                        if top == tops[i]:
                            topCount = FirstElementCount
                            botCount = i - FirstElementCount
                        if bot == tops[i]:
                            topCount = i - FirstElementCount
                            botCount = FirstElementCount
                    elif bottoms[i] not in [top, bot]:
                        if tops[i] == top:
                            topCount = FirstElementCount + 1
                            botCount = i - FirstElementCount
                            determined = top
                        if tops[i] == bot:
                            topCount = i - FirstElementCount + 1
                            botCount = FirstElementCount
                            determined = bot
                    elif tops[i] not in [top, bot]:
                        if bottoms[i] == bot:
                            botCount = FirstElementCount + 1
                            topCount = i - FirstElementCount
                            determined = bot
                        if bottoms[i] == top:
                            botCount = i - FirstElementCount + 1
                            topCount = FirstElementCount
                            determined = top
            else:
                if tops[i] == determined and bottoms[i] == determined:
                    continue
                elif tops[i] == determined:
                    topCount += 1
                elif bottoms[i] == determined:
                    botCount += 1
                else:
                    return -1
        if not determined:
            return min(FirstElementCount, len(tops) - FirstElementCount)
        else:
            return min(topCount, botCount)
