class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            image[i] = list(reversed(image[i]))
        for img in range(len(image)):
            for i in range(len(image[img])):
                image[img][i] ^= 1
        return image
      
# Alternative solution

class Solution1:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)
        for i in range(n):
            for j in range(n//2):
                image[i][j] ^= 1
                image[i][n-1-j] ^= 1
                image[i][j], image[i][n-1-j] = image[i][n-1-j], image[i][j]
            if len(image[i]) % 2 == 1:
                image[i][n//2] ^= 1
        return image
