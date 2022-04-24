class Codec:
    dictionary = {}

    def encode(self, longUrl):
        hash_val = str(hash(longUrl))
        self.dictionary[hash_val] = longUrl
        return hash_val
        
    def decode(self, shortUrl):
        return self.dictionary[shortUrl]
