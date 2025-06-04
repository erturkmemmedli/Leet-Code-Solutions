class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        
        n = len(word)
        largest = 'A'

        for i in range(numFriends):
            s = word[i:i+n-numFriends+1]
            if s > largest:
                largest = s
        
        for i in range(numFriends, n):
            if word[i:n] > largest:
                largest = word[i:n]
            
        return largest
