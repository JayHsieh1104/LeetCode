class Bucket:
    def __init__(self):
        self.bucket = []

    
    def update(self, key: int, value: int) -> None:
        found = False
        for i in range(len(self.bucket)):
            if self.bucket[i][0] == key:
                self.bucket[i][1] = value
                found = True
                break
                
        if not found:
            self.bucket.append([key, value])
                
    
    def get(self, key: int) -> int:
        for (k, v) in self.bucket:
            if k == key:
                return v
        return -1
    
        
    def remove(self, key: int) -> None:
        for i in range(len(self.bucket)):
            if self.bucket[i][0] == key:
                self.bucket[i], self.bucket[-1] = self.bucket[-1], self.bucket[i]
                del self.bucket[-1]
                break
            
        
class MyHashMap:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.key_space = 2069
        self.hash_table = [Bucket() for _ in range(self.key_space)]
        

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        self.hash_table[key % self.key_space].update(key, value)

        
    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        return self.hash_table[key % self.key_space].get(key)
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        self.hash_table[key % self.key_space].remove(key)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)