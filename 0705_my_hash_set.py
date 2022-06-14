class MyHashSet:
    def __init__(self):
        self.size = 20000
        self.prime = 19997
        self.max_load_factor = 0.7
        self.num_of_keys = 0
        self.hash_table = [None] * self.size
        
    def hash_funcion(self, key):
        return key % self.size
    
    def double_hash(self, key):
        return self.prime - key % self.prime

    def add(self, key: int) -> None:
        hash_value = self.hash_funcion(key)
        if self.hash_table[hash_value] == None:
            self.hash_table[hash_value] = key
            self.num_of_keys += 1
            self.rehash()
            return
        i = 1
        while self.hash_table[hash_value] != None:
            if self.hash_table[hash_value] == key:
                return
            hash_value += i * self.double_hash(key)
            hash_value %= self.size
            i += 1
        self.hash_table[hash_value] = key
        self.num_of_keys += 1
        self.rehash()

    def remove(self, key: int) -> None:
        hash_value = self.hash_funcion(key)
        i = 1
        while self.hash_table[hash_value] != None:
            if self.hash_table[hash_value] == key:
                self.hash_table[hash_value] = -1
                return
            hash_value += i * self.double_hash(key)
            hash_value %= self.size
            i += 1

    def contains(self, key: int) -> bool:
        hash_value = self.hash_funcion(key)
        i = 1
        while self.hash_table[hash_value] != None:
            if self.hash_table[hash_value] == key:
                return True
            hash_value += i * self.double_hash(key)
            hash_value %= self.size
            i += 1
        return False
            
    def rehash(self):
        if self.num_of_keys / self.size >= self.max_load_factor:
            temp = self.hash_table.copy()
            self.size *= 2
            self.hash_table = [False] * self.size
            self.num_of_keys = 0
            for val in temp:
                if val != None and val != -1: self.add(val)

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

# Alternative solution

class MyHashSet1:
    def __init__(self):
        self.table = [False] * (10 ** 6 + 1)

    def add(self, key: int) -> None:
        self.table[key] = True

    def remove(self, key: int) -> None:
        self.table[key] = False

    def contains(self, key: int) -> bool:
        return self.table[key]
