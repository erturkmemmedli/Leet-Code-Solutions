class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        if preorder == "#": return True
        if len(preorder) < 3: return False
        preorder = preorder.split(",")
        if preorder[-1] != "#" and preorder[-2] != '#': return False
        nullCount = 2
        for i in range(len(preorder)-3, -1, -1):
            if preorder[i] != "#" and nullCount < 2: return False
            if preorder[i] == "#": nullCount += 1
            else: nullCount -= 1
        return nullCount == 1
