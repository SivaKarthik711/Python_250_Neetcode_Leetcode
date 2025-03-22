class MyHashSet:
    def __init__(self, initial_size=1009, load_factor=0.7):
        """Initialize the hash set with a given bucket size and load factor."""
        self.size = initial_size  # Initial bucket size (preferably a prime number)
        self.load_factor = load_factor
        self.buckets = [[] for _ in range(self.size)]
        self.count = 0  # Track number of elements

    def _hash(self, key):
        """Compute hash index for a given key."""
        return hash(key) % self.size

    def _resize(self):
        """Double the bucket size and rehash all elements when load factor is exceeded."""
        new_size = self.size * 2  # Resize strategy: Double the size
        new_buckets = [[] for _ in range(new_size)]

        # Rehash all existing elements into the new buckets
        for bucket in self.buckets:
            for key in bucket:
                new_index = hash(key) % new_size
                new_buckets[new_index].append(key)

        # Update size and buckets
        self.size = new_size
        self.buckets = new_buckets

    def add(self, key):
        """Insert a key into the HashSet if it does not already exist."""
        if self.contains(key):  # Avoid duplicates
            return
        if self.count / self.size >= self.load_factor:  # Check load factor
            self._resize()
        
        index = self._hash(key)
        self.buckets[index].append(key)
        self.count += 1  # Increase element count

    def contains(self, key):
        """Check if a key exists in the HashSet."""
        index = self._hash(key)
        return key in self.buckets[index]

    def remove(self, key):
        """Remove a key from the HashSet if it exists."""
        index = self._hash(key)
        if key in self.buckets[index]:
            self.buckets[index].remove(key)
            self.count -= 1  # Decrease element count

        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)