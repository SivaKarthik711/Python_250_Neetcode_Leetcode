class MyHashMap:
    def __init__(self, initial_size=10):
        self.size = initial_size
        self.bucket = [[] for _ in range(initial_size)]

    def _hash(self, key):
        return hash(key) % self.size  # Converts string or int key into a valid index

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
