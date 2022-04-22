class MyHashMap(object):

    def __init__(self):
        self.map = [None] * (10 ** 6 + 1)

    def put(self, key, value):
        self.map[key] = value

    def get(self, key):
        if self.map[key] is None:
            return -1
        else:
            return self.map[key]

    def remove(self, key):
        self.map[key] = None