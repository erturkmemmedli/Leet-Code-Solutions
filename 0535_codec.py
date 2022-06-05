class Codec:
    def __init__(self):
        self.dictionary = {}

    def encode(self, longUrl):
        hash_val = str(hash(longUrl))
        self.dictionary[hash_val] = longUrl
        return hash_val
        
    def decode(self, shortUrl):
        return self.dictionary[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
