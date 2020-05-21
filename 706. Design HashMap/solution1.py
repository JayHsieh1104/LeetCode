class MyHashMap:

    def __init__(self):
        self.mod_num = 2069
        self.array = [[]] * self.mod_num
        
    def put(self, key: int, value: int) -> None:
        if self.array[key % self.mod_num]:
            for pair in self.array[key % self.mod_num]:
                if pair[0] == key:
                    pair[1] = value
                    return
            self.array[key % self.mod_num].append([key, value])
        else:
            self.array[key % self.mod_num] = [[key, value]]
        

    def get(self, key: int) -> int:
        if not self.array[key % self.mod_num]:
            return -1
        else:
            for pair in self.array[key % self.mod_num]:
                if pair[0] == key:
                    return pair[1]
            return -1
        

    def remove(self, key: int) -> None:
        for i in range(len(self.array[key % self.mod_num])):
                if self.array[key % self.mod_num][i][0] == key:
                    self.array[key % self.mod_num][i], self.array[key % self.mod_num][-1] = self.array[key % self.mod_num][-1], self.array[key % self.mod_num][i]
                    del self.array[key % self.mod_num][-1]
                    return
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)