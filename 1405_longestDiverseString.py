class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        box = []
        if a != 0:
            box.append([a, "a"])
        if b != 0:
            box.append([b, "b"])
        if c != 0:
            box.append([c, "c"])    
        box.sort(reverse = True)
        output = ""
        while box:
            if len(box) == 1:
                if box[0][0] > 1:
                    return output + box[0][1] * 2
                else:
                    return output + box[0][1]
            if len(box) == 2 and box[0][0] == box[1][0]:
                return output + (box[0][1] + box[1][1]) * box[0][0]
            if len(box) == 3 and box[0][0] == box[1][0] == box[2][0]:
                return output + (box[0][1] + box[1][1] + box[2][1]) * box[0][0]
            if box[0][0] > box[1][0]:
                output += box[0][1] * 2 + box[1][1]
                box[0][0] -= 2
                box[1][0] -= 1
                if box[1][0] == 0:
                    box.pop(1)
                if box[0][0] == 0:
                    box.pop(0)
                box.sort(reverse = True)
            elif box[0][0] == box[1][0]:
                output += box[0][1] + box[1][1]
                box[0][0] -= 1
                box[1][0] -= 1
                if box[1][0] == 0:
                    box.pop(1)
                if box[0][0] == 0:
                    box.pop(0)
                box.sort(reverse = True)
        return output
