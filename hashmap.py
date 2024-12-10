class HashMap:
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]

    def hash(self, key):
        hash = 0
        key = str(key)
        for char in key:
            hash += ord(char)
        return hash % self.MAX
    
    def __setitem__(self, key, value):
        h = self.hash(key)
        found = False
        for i, element in enumerate(self.arr[h]):
            if len(element) >= 2 and element[0] == key:
                self.arr[h][i]  = (key, value)
                found = True
                break        
        if not found:
            self.arr[h].append((key, value))

    def __getitem__(self, key):
        h = self.hash(key)
        for entry in self.arr[h]:
            if entry[0] == key:
                return entry[1]
    
    def __delitem__(self, key):
        h = self.hash(key)
        for index, entry in enumerate(self.arr[h]):
            if entry[0] == key:
                del self.arr[h][index]

