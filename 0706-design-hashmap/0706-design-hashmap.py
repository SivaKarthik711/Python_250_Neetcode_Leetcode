class MyHashMap(object):
    #class variables are writen here
    def __init__(self, intial_size):

        self.size = intial_size #instance variable

        self.bucket = [[] for _ in range(intial_size)]
 
    
    def _hash(self, key):
        return hash(key) % self.size #shared instance variable

        
    def put(self, key, value):
        index = self._hash(key)
        for i, (k, v) in enumerate(self.bucket[index]):
            if k == key:
                self.bucket[index][i] = (key, value)  # Update value if key exists
                return
        self.bucket[index].append((key, value))  # Add new key-value pair

    def get(self, key):
        index = self._hash(key)
        for k, v in self.bucket[index]:
            if k == key:
                return v
        return -1  # Return -1 if key not found

    def remove(self, key):
        index = self._hash(key)
        for i, (k, _) in enumerate(self.bucket[index]):
            if k == key:
                del self.bucket[index][i]  # Remove the key-value pair
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)