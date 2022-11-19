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

# Alternative solution

import random
import string

class Codec:
    def __init__(self):
        self._encode = {}
        self._decode = {}
        self.characters = string.ascii_letters + string.digits

    def encode(self, longUrl: str) -> str:
        url = longUrl[8:]
        hash_val = 0
        for i, char in enumerate(url):
            hash_val += i * ord(char) * 10000019
        val = hash_val
        self._decode[hash_val] = longUrl
        tiny = ""
        for _ in range(6):
            tiny += self.characters[val % len(self.characters)]
            val = val // len(self.characters)
        tiny_url = 'http://tinyurl.com/' + tiny
        self._encode[tiny] = hash_val
        return tiny_url
        
    def decode(self, shortUrl: str) -> str:
        tiny = shortUrl[-6:]
        return self._decode[self._encode[tiny]]
